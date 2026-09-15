---
tags:
  - How to
  - Etendo Classic
  - Semantic Search
  - pgvector
  - PostgreSQL
status: beta
---

# How to Configure Semantic Search

## Overview

This guide configures the semantic search capability of the [Extended Database Utilities](../developer-tools/etendo-database-extended-module.md) module. Semantic search indexes the text of records so a query finds them by meaning. A search for *late delivery complaint* reaches a record that says *the shipment arrived after the agreed date*, which no keyword search does.

The capability is off until somebody turns it on. Installing the module, compiling Etendo, running `update.database`, or starting the application never installs the PostgreSQL extension and never creates a vector object.

!!!warning "This module is in `BETA` phase"
    The behavior described here may change without notice. Validate it thoroughly before using it in a production environment.

## Objective

Index the Business Partner table so an integration can search business partners by meaning, and keep that index up to date as records change.

## Prerequisites

- Etendo with the `com.etendoerp.db.extended` module installed.
- PostgreSQL with the `vector` extension available to be created, version 0.5.0 or later. Version 0.5.0 is the first that supports HNSW indexes.
- A database role allowed to run `CREATE EXTENSION`.
- An OpenAI-compatible embeddings endpoint and its API key.

!!!warning "The indexed text leaves the tenant"
    The value of every indexed column of every affected record is sent to the configured embeddings endpoint. Review which columns a source indexes before activating it. The endpoint is configurable, so the traffic can be directed to the Etendo LLM proxy, to an Azure OpenAI deployment, or to a gateway inside the network instead of to a public API.

## Steps

### 1. Store the API key

The module never holds the key itself. It holds the *name* of where the key lives, and reads the value from there at run time.

Add the key to `gradle.properties` or to the environment of the application server, for example:

```properties title="gradle.properties"
semantic.search.api.key=sk-...
```

### 2. Configure the embedding provider

:material-menu: `Search Indexes` > `Embedding Provider`

Create a record. The fields that decide where the traffic goes and what it costs are these:

| Field | Description |
| --- | --- |
| **Provider Type** | The API dialect the endpoint speaks. `OpenAI` is the only one implemented, and it is also what every OpenAI-compatible gateway serves, so it is the right choice for the Etendo LLM proxy and for an Azure OpenAI deployment as well. It is not the name of the company behind the model. |
| **API Endpoint** | Base URL of the embeddings API, up to and including `/v1` and no further. The path of the call is added by the module and is never configured here. Leave it empty to call OpenAI itself. |
| **Embedding Model** | The model as the endpoint names it, for example `text-embedding-3-small`. A provider-agnostic gateway serves more than one provider and has to be told which one to use: there the format is `provider/model`. |
| **Vector Dimensions** | Length of the vector the model returns. It has to match the model. The ceiling is 2000, which is the limit for an indexable vector column. |
| **API Key Reference** | The name of the property or environment variable holding the key, never the key itself. |
| **Request Timeout** | Seconds a single embedding request may take before it is abandoned. It bounds one request, not the whole run. |
| **Embedding Batch Size** | Texts sent per provider request. It bounds both the request and the transaction the scheduled process holds while delivering it. |
| **Max Input Characters** | Longest text sent for a single record. A model rejects an input past its token limit and the whole batch fails with it, so this keeps one oversized record from stopping the records batched alongside it. Characters are not tokens: a token is roughly four characters for English text, and fewer for other languages. |
| **Retry Limit** | Delivery attempts before an event stops being recovered automatically. It keeps a permanent failure, such as a revoked key, from being retried forever at the provider's expense. |

=== "OpenAI directly"

    | Field | Value |
    | --- | --- |
    | Provider Type | `OpenAI` |
    | API Endpoint | *(empty)* |
    | Embedding Model | `text-embedding-3-small` |
    | Vector Dimensions | `1536` |

=== "Etendo LLM proxy"

    | Field | Value |
    | --- | --- |
    | Provider Type | `OpenAI` |
    | API Endpoint | `https://llm.etendo.software/v1` |
    | Embedding Model | `openai/text-embedding-3-small` |
    | Vector Dimensions | `1536` |

    The proxy is provider-agnostic, so the provider is named in the model field.

=== "Azure OpenAI"

    | Field | Value |
    | --- | --- |
    | Provider Type | `OpenAI` |
    | API Endpoint | `https://<resource>.openai.azure.com/openai/v1` |
    | Embedding Model | *(the deployment name)* |
    | Vector Dimensions | *(what the deployed model returns)* |

!!!warning "Changing the model later does not re-embed anything"
    Changing **Embedding Model** on a source that already has a collection leaves the existing vectors as they are. If the new model has a different vector size, the collection no longer matches, and activation reports that instead of repairing it. Repairing means dropping every vector the collection holds.

### 3. Create the search source

:material-menu: `Search Indexes` > `Search Sources`

A search source names one table and the way its records are indexed.

| Field | Description |
| --- | --- |
| **Table** | The table to index. |
| **Vector Namespace** | Logical partition the embeddings of this source are stored under. |
| **Embedding Provider** | The provider configured in the previous step. |
| **Distance Metric** | How similarity is measured. Cosine is the recommended default for text embeddings. It is applied when the collection is created. |
| **Indexing Enabled** | When checked, changes to the table are captured for indexing. |
| **Filter Column** and **Filter Value** | Optional. Index only the records whose column matches the value, instead of the whole table. |
| **Configuration Version** | Version counter of the configuration. Every queued event carries the version it was created under, and events from an older version are discarded instead of indexed. |

**Index On Insert**, **Index On Update**, and **Index On Delete** decide which changes enqueue an event. Leave all three checked unless there is a reason not to:

- Turning off **Index On Insert** leaves records created from now on out of the index until a backfill picks them up.
- Turning off **Index On Delete** leaves the vectors of deleted records in the collection, where a search keeps returning them.

!!!info "The filter is compiled into the trigger"
    A record that does not match the filter never reaches the queue at all. That is also why changing the filter does not remove the vectors of records that matched before, and why the change takes effect after the next `update.database`.

### 4. Choose the columns

In the **Source Columns** tab, add one record per column to index.

| Field | Description |
| --- | --- |
| **Embedding Content** | When checked, the value of this column is part of the embedded text. Unchecked columns are still stored as filterable metadata, they just do not contribute to the vector. |
| **Reindex On Change** | Whether a change to this column enqueues a re-embedding. Leave it off for a column that is only metadata to filter by, so editing it does not pay for an embedding that would come out the same. |
| **Sequence Number** | The order the column values are concatenated in before being embedded. |

A source needs at least one active column with **Embedding Content** checked. Without one there is no text to embed, and activation reports the source as not ready.

### 5. Define the search targets

In the **Search Target** tab, define what an API client can ask for.

| Field | Description |
| --- | --- |
| **Search Target Key** | The name a caller uses to search this target through the API. |
| **Filter Display Logic** | Optional. Restricts which indexed records this target returns, using display logic syntax over the configured metadata columns, for example `@IsSOTrx@='Y'`. The field names have to be columns configured on the source. |

!!!warning "The target key is a contract"
    Changing **Search Target Key** breaks every caller already asking for the old one.

### 6. Activate the source

Select the sources in the **Search Sources** grid and press **Activate Vector Indexing**.

The action installs the PostgreSQL extension and the runtime storage once per database, then prepares each selected source: it creates the vector collection if it is missing and installs the database triggers that capture changes.

A source that cannot be prepared is reported with the reason rather than prepared, so a configuration mistake surfaces here instead of as a queue full of failures. Activation does not enqueue any records.

### 7. Schedule the background processes

Schedule these at System level, once for the whole instance, through :material-menu: `General Setup` > `Process Scheduling` > `Process Request`.

| Process | Purpose |
| --- | --- |
| **Process Vector Outbox** | Drains the queue: recovers events left behind by an interrupted run, embeds and stores the pending ones, and purges events that finished more than thirty days ago. |
| **Process Vector Reindex** | Walks the table of a requested reindex, in chunks, from where it last stopped. |
| **Requeue Failed Vector Events** | Puts failed events back in the queue once the cause of the failure is fixed. |

Nothing is indexed until **Process Vector Outbox** runs.

### 8. Index the records that already existed

Triggers only capture what changes from the moment they exist, so the records already in the table are not in the index.

Select the sources and press **Request Reindex**. The action records the request. The walk itself is performed by **Process Vector Reindex** in bounded chunks, and its progress is visible in the **Reindex Request** tab: **Status**, **Enqueued Records**, **Estimated Records**, and **Last Enqueued Record**.

Requesting a reindex on a source that is already walking restarts it from the beginning and discards the progress made so far. The action asks for confirmation before doing so.

## Result

Every change to an indexed column of the source table enqueues an event, visible in the **Outbox** tab of the source and, across every source, in :material-menu: `Search Indexes` > `Outbox Monitor`. **Process Vector Outbox** embeds those events and stores the vectors, and the configured search targets answer queries over them.

## Monitor and troubleshoot

The **Outbox Monitor** window lists every indexing event of every source, with its **Status**, **Attempt Count**, **Last Error**, and **Processed At**.

| Symptom | Cause and action |
| --- | --- |
| Events stay pending | **Process Vector Outbox** is not scheduled, or it is not running. |
| Events are failed with the same error | Read **Last Error**. After fixing the cause, run **Requeue Failed Vector Events** to put them back in the queue. |
| An event reached the retry limit | It stays failed and is not recovered automatically. Requeue it once the cause is fixed. |
| A search fails with `VECTOR_COLLECTION_NOT_FOUND` | **Vector Namespace** has no collection behind it. Activate the source. |
| Activation reports a dimension mismatch | The collection was created for a model with a different vector size. Repairing means dropping every vector it holds, so the action reports it instead of doing it. |
| A record was never indexed | It existed before the triggers did. Request a reindex. |

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.
