---
title: Developer Guide - Explore Etendo Data with Postgres and Chart MCP
status: beta
tags:
  - How to
  - Etendo Copilot
  - MCP
  - Postgres MCP
  - Chart MCP
  - Data Analytics
---

# How to Explore Etendo Data with Postgres and Chart MCP

## Overview

!!! example "IMPORTANT: THIS IS A BETA VERSION"
    It is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**. The module behavior may change without notice. Do not use it in production environments.

This guide shows how to turn raw transactional data in Etendo into immediate, actionable insights using **Etendo Copilot** plus two **Model Context Protocol (MCP)** servers:

- **Postgres MCP**: Builds and runs dynamic SQL over the Etendo database (no need for predefined reports).
- **Chart MCP**: Renders fast inline visualizations (line, bar, pie) directly in the Copilot conversation.

You ask a business question in natural language. The agent:
1. Interprets intent.
2. Generates SQL (through Postgres MCP) within the allowed safety scope.
3. Retrieves the result set.
4. Chooses a suitable chart type (through Chart MCP).
5. Returns a short analytical summary plus the visualization.

## Typical Business Questions

Examples of natural language prompts that benefit from this setup:

- "Show the month over month evolution of purchases and sales for the last year."  
- "Compare total amount by customer in the last quarter."  
- "What percentage of total January sales does each product represent?"  
- "Show the average stock of the last six months."  

## Value for Functional Areas

Without waiting for a BI team or creating a custom report:

- Meetings stay data-driven and agile.
- Decisions are supported with current figures, not outdated exports.
- Etendo becomes an interactive insight surface instead of only a transactional ERP.
- Adoption improves because data becomes conversational and immediate.

## Architecture at a Glance

```
User Question → Copilot Agent → (Postgres MCP → SQL → Result Rows) → (Chart MCP → Visualization) → Consolidated Answer
```

## Prerequisites

- Etendo Copilot installed and configured.
- Access to the Etendo PostgreSQL database (read-only credentials recommended).
- Two MCP server configurations created in Etendo Classic (System Administrator role).

## Step 1. Configure Postgres MCP

Create a new **MCP Server Configuration** record.

**Recommended (restricted) configuration JSON**:
```json
{
  "command": "uvx",
  "args": ["postgres-mcp", "--access-mode=restricted"],
  "env": {
    "DATABASE_URI": "postgresql://username:password@localhost:5432/etendo_db"
  }
}
```

### Notes

- Use a dedicated database user with the minimum read-only privileges needed for analytical queries.
- The `--access-mode=restricted` flag helps limit exposure of system catalogs or unintended objects.
- If your deployment uses a different host, port or database name, adjust `DATABASE_URI` accordingly.

!!! warning "Security"
    Never expose production write credentials. Use a controlled, read-only user. Apply network restrictions (firewall / VPC) as appropriate.

## Step 2. Configure Chart MCP

Create a second **MCP Server Configuration** record.

**Configuration JSON**:
```json
{
  "command": "npx",
  "args": ["-y", "@xingjiexu/quickchart-mcp-server"]
}
```

### Notes

- This server turns tabular data coming from Postgres MCP into quick charts.
- It auto-selects simple chart types (line, bar, pie) aligned with the data pattern.

## Step 3. Link MCP Servers to the Agent

1. Open the **Agent** window (System Administrator).
2. Select (or create) the target Copilot agent.
3. Go to the **MCP** tab.
4. Add both MCP server records (Postgres MCP and Chart MCP).
5. Save.

## Step 4. Adjust the Agent Prompt

Ensure the agent system / base prompt instructs the following sequence:

1. First: generate and run safe SQL using Postgres MCP to obtain the dataset strictly needed.
2. Then: request a visualization from Chart MCP choosing the most suitable chart type.
3. Finally: produce a concise business summary plus the chart.

Suggested prompt fragment:

> When a user asks for metrics, trends, comparisons or composition:  
> 1) Use Postgres MCP to craft the minimal SQL needed.  
> 2) Validate column meaning (avoid leaking irrelevant tables).  
> 3) Use Chart MCP to render an appropriate chart (line for time series, bar for ranking, pie for composition).  
> 4) Return: short insight paragraph + chart.  
> If data is insufficient, ask a clarifying question instead of guessing.

## Step 5. Test the Flow

Try the following conversation:

**User**: "Show the month over month evolution of purchases and sales for the last year."  
**Agent (internal)**: Generates SQL via Postgres MCP → Receives rows with monthly totals.  
**Agent (internal)**: Calls Chart MCP → Produces a line chart with two series (Purchases vs Sales).  
**Agent (answer)**: Provides an insight: trend, peaks, slowdown months + chart.

## Chart Selection Logic (Heuristic)

| Goal | Data Shape | Recommended Chart |
|------|------------|-------------------|
| Trend over time | Date + 1..N series numeric | Line |
| Ranking / Top N | Category + metric | Bar |
| Composition (Parts of Whole) | Categories summing to 100% | Pie |

!!! note
    If the dataset is too small (e.g., a single row) or a chart adds no value, the agent should skip chart generation and provide only a textual summary.

## Troubleshooting

| Symptom | Possible Cause | Action |
|---------|----------------|--------|
| No data returned | Wrong schema or restricted user | Validate connection string and user grants |
| Chart not generated | Chart MCP not linked | Verify MCP tab includes Chart MCP |
| SQL error | Unsupported function or typo | Simplify query; rephrase question |
| Sensitive table accessed | Prompt not constraining scope | Reinforce prompt instructions and restrict DB grants |

## Best Practices

- Keep SQL minimal (only needed columns and rows).
- Aggregate in SQL, not in the agent reasoning layer.
- Return business meaning, not just numbers.
- Log queries in a safe audit table for review if compliance requires it.
- Rotate the database read-only password periodically.

## Example Combined Answer (Abstract)

```
Monthly sales grew steadily Q1–Q2, plateaued in July, and dipped 8% in August before recovering. Purchases tracked a similar curve but lagged one month, indicating inventory smoothing. Peak sales: June. Peak purchases: July.

[Inline multi-series line chart]
```

## Limitations

- Complex BI calculations (multi-level allocations, advanced statistical models) are out of scope for the basic Postgres + Chart MCP pairing.
- Very large result sets may be truncated. Design prompts that encourage aggregation.
- Chart styles are intentionally simple (fast insight > aesthetic depth).

## Related References

- Concept: [Model Context Protocol (MCP)](../concepts/model-context-protocol.md)
- How to Configure MCP Servers: [How to Configure MCP servers on a Etendo Agent](how-to-configure-mcp-servers-on-agents.md)
- GitHub MCP Servers: https://github.com/modelcontextprotocol/servers
