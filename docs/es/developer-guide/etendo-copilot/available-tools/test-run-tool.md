---
tags:
  - Copilot
  - Herramienta
  - Prueba
  - Ejecutar prueba
  - Ejecución de pruebas
  - Gradle
---

# Herramienta de ejecución de pruebas

:octicons-package-16: Paquete Java: `com.etendoerp.copilot.toolpack`

## Visión general

La **Herramienta de ejecución de pruebas** está diseñada para ejecutar pruebas Java utilizando Gradle, proporcionando una forma eficiente de ejecutar pruebas en proyectos Java dentro de un entorno específico.

!!!info
    Para incluir esta funcionalidad, debe estar instalado el Copilot Extensions Bundle. Para más información, siga las instrucciones en el marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. Para información sobre versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Copilot Extensions - Notas de la versión](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

## Funcionalidad

Esta herramienta es especialmente útil para ejecutar y validar suites de pruebas Java. Puede utilizarse en varios escenarios, como:

- Ejecutar pruebas específicas o grupos de pruebas para asegurar que las funcionalidades están correctamente implementadas.
- Integrar pruebas automatizadas en el flujo de trabajo de desarrollo.

El proceso consta de las siguientes acciones:

**Recepción de parámetros**

La herramienta recibe los siguientes parámetros de entrada:

- `test_targets`: Una o más pruebas o paquetes a ejecutar.
- `working_directory`: El directorio donde se encuentra el script `gradlew`.

**Ejecución de pruebas**

- Se construye y ejecuta un comando de Gradle con las pruebas especificadas.
- La ejecución se realiza en el directorio de trabajo especificado.

**Devolución del resultado**

Devuelve un resumen de la ejecución de las pruebas junto con el detalle de las pruebas superadas y fallidas.

## Ejemplo de uso

Si desea ejecutar pruebas específicas en el directorio `/path/to/erp`, el formato de entrada y salida sería el siguiente:

- **Entrada**

```json
{
  "test_targets": ["com.etendoerp.webhookevents.WebhookSetupTest"],
  "working_directory": "/path/to/erp"
}
```

- **Salida**

```json
{
  "summary": "Algunas pruebas fallaron. Revise los detalles a continuación.",
  "details": {
    "passed_tests": [
      "Prueba 1 SUPERADA>"
    ],
    "failed_tests": [
      "Prueba 2 FALLIDA> Motivo"
    ]
  },
  "raw_logs": "Registros completos en caso de fallo"
}
```

---
Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L](https://etendo.software){target="_blank"}.