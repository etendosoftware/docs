---
title: Herramienta XLS
tags:
    - Copilot
    - Procesamiento de XLS
    - Extracción de datos
    - Excel
    - Google Sheets
    - CSV
---

# Herramienta XLS

:octicons-package-16: Paquete Java: `com.etendoerp.copilot.toolpack`

## Visión general

La Herramienta XLS procesa archivos `XLS` o `CSV` para extraer datos. Está diseñada para facilitar tareas como el análisis del contenido de hojas de cálculo, el procesamiento de datos tabulares y la extracción de información específica de archivos XLS. La herramienta acepta la ruta del archivo de un archivo de datos y devuelve datos procesados en función de los parámetros definidos.

!!!info
    Para incluir esta funcionalidad, debe estar instalado el bundle Copilot Extensions Bundle. Siga las instrucciones del marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. Para más información sobre versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Copilot Extensions - Notas de la versión](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

## Funcionalidad

Esta herramienta automatiza el proceso de **extracción de datos desde archivos XLS**. Es especialmente útil para tareas como la lectura de datos financieros, la extracción de detalles de clientes o el análisis de registros de inventario. La herramienta admite lógica de procesamiento personalizable para gestionar estructuras de datos diversas.

El uso de esta herramienta consta de las siguientes acciones:

- **Recepción de parámetros**:

    - La herramienta recibe un objeto de entrada que contiene la ruta del archivo XLS que se va a procesar y parámetros opcionales para la extracción de datos.
    - **ruta**: La ruta del archivo XLS que se va a procesar.
    - **Parámetros**: Parámetros de extracción opcionales como el nombre de la hoja, filas específicas o Columna.

- **Procesamiento del archivo**:

    - La herramienta lee el archivo XLS desde la ruta especificada, verifica su existencia y garantiza que el formato del archivo sea compatible.
    - Procesa el archivo en función de los parámetros de entrada para extraer los datos requeridos.

- **Devolución del resultado**:

    - La herramienta devuelve un objeto JSON que contiene los datos extraídos.
    - **Datos**: Los datos procesados extraídos del archivo XLS.

## Ejemplo de uso

### Extracción de datos desde un archivo XLS

Suponga que tiene un archivo de Excel en `/home/user/data.xls` y desea extraer información de clientes del archivo:

**Contenido XLS**
``` txt
| ID de cliente | Nombre     | Valor compra |
|---------------|------------|--------------|
| 1001          | John Doe   | 500          |
| 1002          | Jane Smith | 300          |
```

- Utilice la herramienta de la siguiente manera:

    - **Entrada**:

        ```
        {
            "path": "/home/user/data.xls",
            "parameters": {
                "sheet": "Customers",
                "columns": ["Customer ID", "Name", "Purchase Amount"]
            }
        }
        ```

    - **Salida**:

        ```Json title="JSON de salida"
        {
            "data": [
                {"Customer ID": "1001", "Name": "John Doe", "Purchase Amount": 500},
                {"Customer ID": "1002", "Name": "Jane Smith", "Purchase Amount": 300}
            ]
        }
        ```

!!!note
    El resultado de la herramienta puede utilizarse como entrada para otros procesos. Por ejemplo, los datos de clientes extraídos pueden utilizarse para generar campañas de marketing personalizadas o facturas.

---
Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L](https://etendo.software){target="_blank"}.