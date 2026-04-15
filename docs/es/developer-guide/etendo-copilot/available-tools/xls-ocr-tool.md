---
title: Herramienta OCR para XLS
tags:
    - Copilot
    - Procesamiento de XLS
    - Extracción de datos
    - Excel
    - OCR
    - CSV
---

# Herramienta OCR para XLS

:octicons-package-16: Paquete Java: `com.etendoerp.copilot.toolpack`

## Visión general

La Herramienta OCR para XLS procesa archivos de Excel (`XLS`, `XLSX`, `CSV`) mediante Reconocimiento Óptico de Caracteres (OCR) y modelos de IA de visión para extraer datos estructurados. A diferencia de las herramientas tradicionales de procesamiento de Excel, esta herramienta convierte las hojas de cálculo en imágenes y utiliza modelos de visión avanzados para comprender y extraer datos, lo que la hace especialmente eficaz para diseños complejos, celdas con formato o cuando fallan los métodos de análisis tradicionales.

!!!info
    Para incluir esta funcionalidad, debe estar instalado el Copilot Extensions Bundle. Siga las instrucciones del marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. Para obtener más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Copilot Extensions - Notas de la versión](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

## Funcionalidad

Esta herramienta automatiza el proceso de **extracción inteligente de datos desde archivos de Excel mediante OCR e IA de visión**. Es especialmente útil para procesar hojas de cálculo complejas con diseños irregulares, celdas combinadas, datos con formato o cuando necesita extraer información específica basándose en patrones visuales en lugar de en el análisis de datos estructurados.

El uso de esta herramienta consta de las siguientes acciones:

- **Recepción de parámetros**:

    - La herramienta recibe un objeto de entrada que contiene la ruta del archivo de Excel y una pregunta o instrucción específica para la extracción de datos.
    - **path**: La ruta al archivo de Excel que se va a procesar (admite los formatos `.xls`, `.xlsx` y `.csv`).
    - **question**: Instrucción precisa sobre qué extraer del contenido del archivo (opcional; por defecto, extrae toda la información útil).

- **Procesamiento del archivo**:

    - La herramienta renderiza cada hoja del archivo de Excel como una imagen JPEG de alta resolución utilizando matplotlib.
    - Cada imagen de hoja se procesa mediante un modelo de IA de visión (GPT-4o por defecto) para comprender el contenido.
    - El modelo de IA analiza la representación visual y extrae la información solicitada en función de la pregunta proporcionada.

- **Devolución del resultado**:

    - La herramienta devuelve los datos extraídos como texto estructurado o en formato JSON.
    - **Resultado**: Los datos procesados extraídos del archivo de Excel en función de la pregunta o instrucción específica.
    - **error**: Mensaje de error si el procesamiento falla.

## Detalles técnicos

- **Modelo de visión**: Utiliza GPT-4o por defecto (configurable mediante la variable de entorno `COPILOT_OCRTOOL_MODEL`)
- **Procesamiento de imágenes**: Renderiza hojas de Excel como imágenes con dimensionado automático en función del contenido
- **Gestión de hojas**: Procesa todas las hojas del archivo de Excel
- **Limpieza**: Elimina automáticamente los archivos de imagen temporales tras el procesamiento
- **Gestión de errores**: Gestión de errores robusta con mensajes de error detallados

## Ejemplos de uso

### Extracción de información de productos desde un catálogo

Para un catálogo de productos con imágenes, descripciones y precios:

- **Entrada**:

    ```json
    {
        "path": "/home/user/product_catalog.xlsx",
        "question": "Find all products with their names, SKUs, prices, and descriptions. Focus on items marked as 'Featured' or highlighted."
    }
    ```

- **Salida**:

    ```json
    {
        "featured_products": [
            {
                "name": "Premium Widget",
                "sku": "PWG-001",
                "price": "$29.99",
                "description": "High-quality widget with premium features",
                "status": "Featured"
            }
        ]
    }
    ```

!!!note
    La Herramienta OCR para XLS es ideal para procesar hojas de cálculo heredadas, informes complejos o cualquier archivo de Excel en el que los métodos tradicionales de análisis estructurado sean insuficientes. El enfoque basado en visión permite una extracción de datos más inteligente y flexible basada en la comprensión visual, en lugar de reglas estructurales estrictas.

!!!warning
    El procesamiento de archivos de Excel grandes o de archivos con muchas hojas puede tardar más debido a los pasos de renderizado de imágenes y procesamiento por IA. Considere el tamaño y la complejidad del archivo al utilizar esta herramienta en aplicaciones sensibles al tiempo.