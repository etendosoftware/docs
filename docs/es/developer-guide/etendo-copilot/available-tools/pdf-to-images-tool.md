---
tags:
    - Copilot
    - PDF
    - Imágenes
    - Herramienta
---

# Herramienta de PDF a Imágenes

:octicons-package-16: Paquete Java: `com.etendoerp.copilot.toolpack`

## Visión general

La **Herramienta de PDF a Imágenes** es una herramienta que convierte un archivo PDF en un array de imágenes, donde cada imagen representa una página del PDF. La herramienta utiliza bibliotecas especializadas de Python para el procesamiento de PDF y la gestión de imágenes para lograr esta conversión de forma eficiente.

!!!info
    Para poder incluir esta funcionalidad, debe estar instalado el Copilot Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. Para obtener más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Copilot Extensions - Notas de la versión](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

## Funcionalidad

Esta herramienta permite a los agentes convertir documentos PDF a formatos de imagen. Esto es especialmente útil para escenarios en los que es necesario procesar páginas individuales de un PDF como imágenes, como en el archivado digital, la revisión de documentos o tareas posteriores de análisis de imágenes.

Es de gran valor para cualquier flujo de trabajo automatizado que requiera gestionar contenidos PDF como datos de imagen. Simplifica el proceso de convertir páginas PDF a imágenes, garantizando que cada página se renderice con precisión y se guarde como una imagen de alta calidad. Esta herramienta es esencial en ámbitos como el archivado digital, donde los documentos deben conservarse en un formato fácilmente accesible y visualizable, y en aplicaciones que implican análisis de imágenes, donde cada página de un documento PDF puede procesarse de forma independiente.

El uso de esta herramienta consta de las siguientes acciones:

- **Recepción de parámetros** 

    La herramienta recibe un objeto de entrada que contiene la siguiente clave:

    - path

        (str): la ruta al archivo PDF que se va a convertir.

- **Procesamiento**

    - Validación: la herramienta primero comprueba si la ruta del PDF proporcionada apunta a un archivo existente. Si el archivo no existe, lanza una excepción con un mensaje de error relevante.

    - Carga del PDF: la herramienta utiliza la biblioteca pypdfium2 para cargar el documento PDF.

    - Renderizado de páginas: para cada página del PDF:

        - La página se renderiza con una escala de 2.0 para producir una imagen de alta calidad.

        - El bitmap renderizado se convierte a continuación en una imagen PIL (Python Imaging Library).

    - Almacenamiento temporal: cada imagen convertida se almacena temporalmente en el sistema de archivos en una ruta predefinida (`/tmp/page_{page_number}.png`).

    - Recopilación de resultados: las rutas a las imágenes almacenadas se recopilan en una lista, que se devuelve como salida final.

- **Devolución del resultado**

    Una vez completado el proceso de conversión, la herramienta devuelve una lista de rutas de archivo, cada una apuntando a la imagen convertida correspondiente para cada página del PDF.


## Ejemplo de uso

Si tiene un archivo PDF ubicado en `/home/user/document.pdf` y desea convertir sus páginas en imágenes, utilizaría la herramienta de la siguiente manera:

- **Entrada**:

```
{
  "path": "/home/user/document.pdf"
}
```

- **Salida**:

```
[
  "/tmp/page_0.png",
  "/tmp/page_1.png",
  "/tmp/page_2.png"
  // rutas para todas las páginas
]
```

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.