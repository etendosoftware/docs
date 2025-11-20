---
tags:
  - How to
  - Telemetry
  - Monitoring
  - Analytics
---

#  How to Add Telemetry to an Etendo Classic Module

##  Overview

The Etendo Telemetry Module adds a thread-safe telemetry layer that lets you audit how end users interact with Etendo Classic. By collecting metrics from servlets, processes, and REST endpoints you can build historical usage dashboards, detect regressions, and better understand feature adoption. This guide explains how to wire telemetry events into any custom module using the `TelemetryUsageInfo` helper and the same approach followed by the `com.etendoerp.telemetry` reference module.

##  Example Module

All of the snippets referenced here come from the `com.etendoerp.telemetry` module, which ships with reusable helpers and sample services. Clone that repository and review the `TrackingUtil` class if you want to see a complete implementation that you can extend in your own module.

##  Telemetry building blocks

`TelemetryUsageInfo` is the core component. It manages telemetry entries through a `ThreadLocal` instance to avoid data races when multiple requests are processed at the same time.

- **Thread-local lifecycle**: call `TelemetryUsageInfo.getInstance()` to obtain the current request scope, and always invoke `TelemetryUsageInfo.clear()` in a `finally` block when you are done.
- **Persistence target**: data is inserted into `ad_session_usage_audit`, which stores session, command, module, and JSON payload information for later analysis.
- **Auto population**: if you omit `userId`, `moduleId`, `objectId`, or `objecttype`, the helper pulls defaults from `SessionInfo` so you can focus on the data that is unique to your module.

###  Required fields before saving

Use the following checklist before calling `saveUsageAudit()`:

| Field | Description | How to set it |
|-------|-------------|---------------|
| `sessionId` | Etendo database session identifier (`#AD_Session_ID`) | Extract from the HTTP request or `SessionInfo` |
| `command` | Logical action being tracked | Choose descriptive constants such as `AGENT_EXECUTION` |
| `userId` | Current user | Omit only if `SessionInfo` already holds the user |
| `moduleId` | Module sending the telemetry event | You can hardcode your module ID in a wrapper |
| `objectId` | Domain object or entity | Use process ID, REST endpoint, or feature identifier |
| `objecttype` | Process type, `P` (process) by default | Optional unless you need custom types |
| `jsonObject` | Optional metadata payload | Use JSON to describe request, response, or timings |

If any required field is empty the helper logs an error and no row is inserted, so validate your payload when debugging.

##  Capturing the session ID

Telemetry events must be tied to an Etendo session. Pick whichever approach fits your entry point:

1. **`VariablesSecureApp` (servlets and controllers)**

   ```java
   VariablesSecureApp vars = new VariablesSecureApp(request);
   String sessionId = vars.getSessionValue("#AD_Session_ID");
   TelemetryUsageInfo telemetry = TelemetryUsageInfo.getInstance();
   telemetry.setSessionId(sessionId);
   ```

2. **`SessionInfo` (secure contexts)**

   ```java
   TelemetryUsageInfo telemetry = TelemetryUsageInfo.getInstance();
   telemetry.setSessionId(SessionInfo.getSessionId());
   ```

3. **`HttpSession` fallback**

   ```java
   HttpSession session = request.getSession(false);
   if (session != null) {
     telemetry.setSessionId((String) session.getAttribute("#AD_Session_ID"));
   }
   ```

4. **Auto population**

   Skipping `setSessionId` forces `TelemetryUsageInfo` to read from `SessionInfo`, which works for simple synchronous processes that already initialize the context.

##  Recording usage data

Once you have the session ID, populate the remaining fields and call `saveUsageAudit()`:

```java
TelemetryUsageInfo telemetry = TelemetryUsageInfo.getInstance();
telemetry.setSessionId(sessionId);
telemetry.setModuleId(MY_MODULE_ID);
telemetry.setCommand("AGENT_USAGE");
telemetry.setObjectId(agentId);
telemetry.setObjecttype("AGENT");
telemetry.setClassname(MyTelemetryHook.class.getName());
telemetry.setTimeMillis(System.currentTimeMillis()); // optional, auto-filled otherwise
telemetry.setJsonObject(jsonMetadata);
telemetry.saveUsageAudit();
```

Always wrap the call in `try/finally` and clear the thread-local instance:

```java
try {
  // configure telemetry
  telemetry.saveUsageAudit();
} catch (Exception e) {
  logger.error("Telemetry failed", e);
} finally {
  TelemetryUsageInfo.clear();
}
```

##  Use case: track REST/API calls

The reference REST service demonstrates how to track incoming HTTP traffic:

```java
public void trackAPICall(HttpServletRequest request, String apiEndpoint) {
  try {
    VariablesSecureApp vars = new VariablesSecureApp(request);
    String sessionId = vars.getSessionValue("#AD_Session_ID");

    JSONObject metadata = new JSONObject();
    metadata.put("endpoint", apiEndpoint);
    metadata.put("method", request.getMethod());
    metadata.put("timestamp", System.currentTimeMillis());

    TelemetryUsageInfo telemetry = TelemetryUsageInfo.getInstance();
    telemetry.setSessionId(sessionId);
    telemetry.setCommand("API_CALL");
    telemetry.setObjectId(apiEndpoint);
    telemetry.setObjecttype("REST");
    telemetry.setClassname(MyRestService.class.getName());
    telemetry.setJsonObject(metadata);
    telemetry.saveUsageAudit();
  } catch (Exception e) {
    logger.error("Failed to track API call", e);
  } finally {
    TelemetryUsageInfo.clear();
  }
}
```

##  Use case: measure process execution time

Wrap long-running commands to measure latency and persist performance data:

```java
public void trackCommandExecution(String command, String objectId) {
  long start = System.currentTimeMillis();
  try {
    TelemetryUsageInfo telemetry = TelemetryUsageInfo.getInstance();
    telemetry.setSessionId(getCurrentSessionId());
    telemetry.setCommand(command);

    executeCommand(command); // your business logic

    long elapsed = System.currentTimeMillis() - start;
    JSONObject metadata = new JSONObject();
    metadata.put("execution_time_ms", elapsed);
    metadata.put("status", "success");

    telemetry.setTimeMillis(elapsed);
    telemetry.setObjectId(objectId);
    telemetry.setObjecttype("P");
    telemetry.setJsonObject(metadata);
    telemetry.saveUsageAudit();
  } catch (Exception e) {
    logger.error("Error tracking command execution", e);
  } finally {
    TelemetryUsageInfo.clear();
  }
}
```

##  Use case: feature adoption tracking

Collect structured metadata for UI or Copilot features to understand adoption patterns:

```java
public void trackFeatureUsage(String featureId, Map<String, Object> featureData) {
  try {
    TelemetryUsageInfo telemetry = TelemetryUsageInfo.getInstance();
    telemetry.setCommand("FEATURE_USAGE");
    telemetry.setObjectId(featureId);
    telemetry.setObjecttype("F");

    JSONObject json = new JSONObject();
    json.put("feature_id", featureId);
    json.put("timestamp", System.currentTimeMillis());
    for (Map.Entry<String, Object> entry : featureData.entrySet()) {
      json.put(entry.getKey(), entry.getValue());
    }

    telemetry.setJsonObject(json);
    telemetry.saveUsageAudit();
  } catch (Exception e) {
    logger.error("Error tracking feature usage", e);
  } finally {
    TelemetryUsageInfo.clear();
  }
}
```

##  Best practices

- **Clear thread-locals**: Always call `TelemetryUsageInfo.clear()` in a `finally` block, especially inside thread pools, to prevent memory leaks.
- **Set the session early**: Populate the session ID as soon as you enter the request, then reuse the same `TelemetryUsageInfo` instance.
- **Use meaningful commands**: Prefer explicit verbs like `AGENT_EXECUTION` or `REPORT_GENERATION` over generic names.
- **Structure JSON consistently**: Reuse common keys (`operation_type`, `status`, `execution_time_ms`) so downstream analytics stay predictable.
- **Fail safe**: Log telemetry exceptions but never propagate them to the end user; telemetry should not block functional flows.

##  Troubleshooting

- **Nothing is saved**: Enable debug logs and print the session, command, user, module, and object values before calling `saveUsageAudit()` to find missing fields.
- **Memory leaks**: Double-check that `TelemetryUsageInfo.clear()` executes in every path, including error branches, when using executors.
- **JSON errors**: Wrap `JSONObject` mutations in try/catch blocks and make sure the metadata only contains serializable values.

With these steps you can extend any Etendo Classic module with reliable telemetry that surfaces how your features perform in production without impacting end-user workflows.
