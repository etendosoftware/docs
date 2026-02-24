---
tags:
  - How to
  - Telemetry
  - Monitoring
  - Analytics
---

#  Cómo añadir telemetría a un módulo de Etendo

##  Visión general

El **Módulo de telemetría de Etendo** añade una capa de telemetría segura para hilos que le permite auditar cómo interactúan los usuarios finales con Etendo. Al recopilar métricas de servlets, procesos y endpoints REST, puede crear paneles históricos de uso, detectar regresiones y comprender mejor la adopción de funcionalidades. Esta guía explica cómo integrar eventos de telemetría en cualquier módulo personalizado usando el helper `TelemetryUsageInfo` y el mismo enfoque seguido por el módulo de referencia `com.etendoerp.telemetry`.

##  Módulo de ejemplo

Todos los fragmentos referenciados aquí provienen del módulo [com.etendoerp.telemetry](https://github.com/etendosoftware/com.etendoerp.telemetry){target="_blank"}, que incluye helpers reutilizables y servicios de ejemplo. **Clone** ese repositorio y revise la clase `TrackingUtil` si quiere ver una implementación completa que pueda ampliar en su propio módulo.

##  Bloques de construcción de la telemetría

`TelemetryUsageInfo` es el componente principal. Gestiona las entradas de telemetría mediante una instancia `ThreadLocal` para evitar condiciones de carrera cuando se procesan múltiples solicitudes al mismo tiempo.

- **Ciclo de vida de ThreadLocal**: llame a `TelemetryUsageInfo.getInstance()` para obtener el ámbito de la solicitud actual, e invoque siempre `TelemetryUsageInfo.clear()` en un bloque `finally` cuando termine.
- **Destino de persistencia**: los datos se insertan en `ad_session_usage_audit`, que almacena información de sesión, comando, módulo y payload JSON para su análisis posterior.
- **Autorrelleno**: si omite `userId`, `moduleId`, `objectId` u `objecttype`, el helper obtiene valores por defecto desde `SessionInfo` para que pueda centrarse en los datos que son únicos de su módulo.

###  Campos obligatorios antes de guardar

Use la siguiente lista de verificación antes de llamar a `saveUsageAudit()`:

| Campo | Descripción | Cómo configurarlo |
|-------|-------------|-------------------|
| `sessionId` | Identificador de sesión de base de datos de Etendo (`#AD_Session_ID`) | Extraer de la solicitud HTTP o de `SessionInfo` |
| `command` | Acción lógica que se está registrando | Elija constantes descriptivas como `AGENT_EXECUTION` |
| `userId` | Usuario actual | Omitir solo si `SessionInfo` ya contiene el usuario |
| `moduleId` | Módulo que envía el evento de telemetría | Puede fijar el ID de su módulo en un wrapper |
| `objectId` | Objeto o entidad de dominio | Use el ID del proceso, el endpoint REST o el identificador de la funcionalidad |
| `objecttype` | Tipo de proceso, `P` (proceso) por defecto | Opcional salvo que necesite tipos personalizados |
| `jsonObject` | Payload de metadatos opcional | Use JSON para describir solicitud, respuesta o tiempos |

Si algún campo obligatorio está vacío, el helper registra un error y no se inserta ninguna fila, por lo que debe validar su payload al depurar.

##  Captura del ID de sesión

Los eventos de telemetría deben estar vinculados a una sesión de Etendo. Elija el enfoque que mejor se adapte a su punto de entrada:

1. **`VariablesSecureApp` (servlets y controladores)**

   ```java
   VariablesSecureApp vars = new VariablesSecureApp(request);
   String sessionId = vars.getSessionValue("#AD_Session_ID");
   TelemetryUsageInfo telemetry = TelemetryUsageInfo.getInstance();
   telemetry.setSessionId(sessionId);
   ```

2. **`SessionInfo` (contextos seguros)**

   ```java
   TelemetryUsageInfo telemetry = TelemetryUsageInfo.getInstance();
   telemetry.setSessionId(SessionInfo.getSessionId());
   ```

3. **Fallback de `HttpSession`**

   ```java
   HttpSession session = request.getSession(false);
   if (session != null) {
     telemetry.setSessionId((String) session.getAttribute("#AD_Session_ID"));
   }
   ```

4. **Autorrelleno**

   Omitir `setSessionId` fuerza a `TelemetryUsageInfo` a leer desde `SessionInfo`, lo cual funciona para procesos síncronos simples que ya inicializan el contexto.

##  Registro de datos de uso

Una vez que tenga el ID de sesión, complete el resto de campos y llame a `saveUsageAudit()`:

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

Envuelva siempre la llamada en `try/finally` y limpie la instancia thread-local:

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

##  Caso de uso: seguimiento de llamadas REST/API

El servicio REST de referencia muestra cómo registrar el tráfico HTTP entrante:

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

##  Caso de uso: medir el tiempo de ejecución de procesos

Envuelva comandos de larga duración para medir la latencia y persistir datos de rendimiento:

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

##  Caso de uso: seguimiento de adopción de funcionalidades

Recopile metadatos estructurados para funcionalidades de UI o de Copilot para comprender patrones de adopción:

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

##  Buenas prácticas

- **Limpiar thread-locals**: llame siempre a `TelemetryUsageInfo.clear()` en un bloque `finally`, especialmente dentro de pools de hilos, para evitar fugas de memoria.
- **Configurar la sesión pronto**: complete el ID de sesión en cuanto entre en la solicitud y reutilice la misma instancia de `TelemetryUsageInfo`.
- **Usar comandos significativos**: prefiera verbos explícitos como `AGENT_EXECUTION` o `REPORT_GENERATION` frente a nombres genéricos.
- **Estructurar el JSON de forma consistente**: reutilice claves comunes (`operation_type`, `status`, `execution_time_ms`) para que la analítica posterior sea predecible.
- **A prueba de fallos**: registre las excepciones de telemetría, pero nunca las propague al usuario final; la telemetría no debe bloquear los flujos funcionales.

##  Resolución de problemas

- **No se guarda nada**: habilite logs de depuración e imprima los valores de sesión, comando, usuario, módulo y objeto antes de llamar a `saveUsageAudit()` para localizar campos faltantes.
- **Fugas de memoria**: verifique que `TelemetryUsageInfo.clear()` se ejecuta en todas las rutas, incluidas las ramas de error, cuando use ejecutores.
- **Errores de JSON**: envuelva las mutaciones de `JSONObject` en bloques try/catch y asegúrese de que los metadatos solo contienen valores serializables.

Con estos pasos puede ampliar cualquier módulo de Etendo con una telemetría fiable que muestre cómo rinden sus funcionalidades en producción sin afectar a los flujos de trabajo del usuario final.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.