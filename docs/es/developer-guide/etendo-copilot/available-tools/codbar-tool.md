---
tags:
    - Copilot
    - Codbar
    - Reconocimiento de imágenes
    - Código de barras
---

# Herramienta Codbar

:octicons-package-16: Paquete Java: `com.etendoerp.copilot.ocrtool`

## Visión general

La **CodbarTool** es una herramienta que lee códigos de barras de archivos de imagen. Acepta un array de rutas de archivo como entrada y devuelve un array de códigos de barras encontrados en esas imágenes.

!!!info
    Para poder incluir esta funcionalidad, debe estar instalado el bundle Copilot Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. Para más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Copilot Extensions - Notas de la versión](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

## Funcionalidad

Esta herramienta permite a los agentes **leer códigos de barras de múltiples imágenes**, que posteriormente pueden aplicarse en la gestión de inventario, el seguimiento de productos y el procesamiento de documentos, entre otras áreas.

El uso de esta herramienta consiste en las siguientes acciones: 

- Recepción de parámetros: 

    - La herramienta recibe un objeto de entrada que contiene una clave llamada filepath, que es una lista de strings. Cada string representa la ruta del archivo de una imagen que se analizará.
    - Ejemplo de entrada:

        `{"filepath": ["/tmp/test.png", "/tmp/test1.png"]}`

- Procesamiento de imágenes: 

    - Para cada ruta de archivo proporcionada, la herramienta abre la imagen e intenta decodificar cualquier código de barras presente.
    - Utiliza la librería pyzbar para decodificar códigos de barras de las imágenes.

- Devolución del resultado: 

    - Si se encuentran códigos de barras, la herramienta los recopila y los devuelve en una lista.
    - Ejemplo de salida:

        `{"message": ["123456789012", "987654321098", ...]}`


!!!info
    La herramienta utiliza la librería PIL para abrir archivos de imagen.


!!!note
    La **librería pyzbar** se utiliza para decodificar códigos de barras de la imagen. Si no se encuentra ningún código de barras, devuelve None para esa imagen. Si se encuentran códigos de barras, decodifica los datos de cada código de barras.

## Ejemplo de uso

- Suponga que existe una imagen en `/tmp/goods-receipt.png` y desea extraer el código de barras relacionado con la información de la recepción de mercancía:

A continuación se muestra una imagen de ejemplo de una recepción de mercancía: 

![alt text](../../../assets/developer-guide/etendo-copilot/available-tools/ocr-tool-1.jpg)

- La herramienta se utilizará de la siguiente manera: 

    - Entrada

        ```
        `{"filepath": ["/tmp/goods-receipt.png"]}`

        ```

    - Salida

        ```
        `{"message": ['ALV-4066905', '871000003252']}`

        ```

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.