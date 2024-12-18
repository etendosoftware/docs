---
tags:
  - Copilot
  - IA
  - Tool
  - Test
  - Gradle
---

# Test Run Tool

:octicons-package-16: Javapackage: `com.etendoerp.copilot.toolpack`

## Overview

La **Test Run Tool** está diseñada para ejecutar pruebas Java usando Gradle, proporcionando una forma eficiente de ejecutar pruebas en proyectos Java dentro de un entorno específico.

!!!info
    Para incluir esta funcionalidad, el Copilot Extensions Bundle debe estar instalado. Para más información, sigue las instrucciones del marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. Para información sobre versiones disponibles, compatibilidad con el núcleo y nuevas características, visita [Copilot Extensions - Release notes](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

## Functionality

Esta herramienta es especialmente útil para ejecutar y validar el conjunto de pruebas de Java. Puede ser utilizada en varias situaciones, como por ejemplo:

- Ejecutar pruebas concretas o grupos de pruebas para asegurarse de que las funcionalidades están correctamente implementadas.
- Integrar pruebas automáticas en el flujo de trabajo de desarrollo.

Este proceso consiste en las siguientes acciones:

- **Receiving Parameters**

    La herramienta recibe los siguientes parámetros de entrada:
    - `test_targets`: Uno o más tests o paquetes que se desean ejecutar.
    - `working_directory`: El directorio donde se encuentra el script `gradlew`.

- **Running Tests**
    - Se construye y ejecuta un comando Gradle con los tests especificados.
    - La ejecución se lleva a cabo en el directorio de trabajo especificado.

- **Returning the Result**
    Devuelve un resumen de la ejecución de tests junto con los detalles de las pruebas pasadas y fallidas.

## Usage Example

Si desea ejecutar pruebas específicas en el directorio `/path/to/erp`, el formato de entrada y salida sería el siguiente:

- **Input**
```json
{
  "test_targets": ["com.etendoerp.webhookevents.WebhookSetupTest"],
  "working_directory": "/path/to/erp"
}
```

- **Output**
```json
{
  "summary": "Some tests failed. Review the details below.",
  "details": {
    "passed_tests": [
      "Test 1 PASSED>"
    ],
    "failed_tests": [
      "Test 2 FAILED> Reason"
    ]
  },
  "raw_logs": "Complete logs in case of failure"
}
```