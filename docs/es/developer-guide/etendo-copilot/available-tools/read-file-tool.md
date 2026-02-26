---
tags:
    - Copilot
    - Herramienta
    - Leer
    - Archivo
---

# Herramienta de lectura de archivos

:octicons-package-16: Paquete Java: `com.etendoerp.copilot.toolpack`

## Visión general

La **Herramienta de lectura de archivos** está diseñada para leer el contenido de archivos a partir de un parámetro de ruta de archivo. Proporciona una forma sencilla de acceder al contenido de archivos de texto en el sistema local.

!!!info
    Para poder incluir esta funcionalidad, debe estar instalado el Copilot Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. Para obtener más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Copilot Extensions - Notas de la versión](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

## Funcionalidad

Esta herramienta es especialmente útil para acceder al contenido de un archivo para su procesamiento o visualización. Puede utilizarse en varias situaciones, como:

- Leer archivos de configuración.
- Acceder a logs y archivos de log.
- Visualizar o procesar datos almacenados en archivos de texto.

Este proceso consta de las siguientes acciones.

- **Recepción de parámetros**

    La herramienta recibe un parámetro de entrada llamado `filepath`, que es la ruta del archivo que se va a leer.

- **Lectura del archivo**
    - Abre el archivo especificado por `filepath`.
    - Lee todo el contenido del archivo.

- **Devolución del resultado**
    Devuelve un diccionario con el contenido del archivo bajo la clave `message`.

## Ejemplo de uso

Si desea leer el contenido del archivo `/tmp/test.txt`:
    
- **Entrada**
```
{ "filepath": "/tmp/test.txt" }
```
- **Salida**
```
{ "message": "Content of the read file..." }
```

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.