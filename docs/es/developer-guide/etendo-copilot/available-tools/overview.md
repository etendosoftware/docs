---
title: Herramientas disponibles - Visión general
tags:
    - Copilot
    - Herramientas
    - Documentación
    - Índice
---

# Herramientas disponibles - Visión general

:octicons-package-16: Paquete Java: `com.etendoerp.copilot.toolpack`

## Visión general

Este documento proporciona una lista completa de todas las herramientas disponibles en el ecosistema de **Etendo Copilot**. Cada herramienta está diseñada para ampliar las capacidades del asistente Copilot, permitiéndole realizar tareas específicas e interactuar con diversos sistemas y servicios.

!!!info
    Para poder incluir esta funcionalidad, debe estar instalado el Copilot Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. Para obtener más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Copilot Extensions - Notas de la versión](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

## Categorías de herramientas

### Herramientas de integración de sistemas

| Nombre de la herramienta | Descripción | Funcionalidades clave | Cuándo usarla |
|-----------|-------------|--------------|-------------|
| [Herramienta de llamada a API](api-call-tool.md) | Ejecutar llamadas HTTP a API de servicios externos | Integración con API REST, soporte de autenticación | Usar para interacciones con API REST |
| [Herramienta de inicialización de cliente](client-init-tool.md) | Inicializar configuraciones de cliente | Configuración de cliente, gestión de configuración |  |
| [Herramienta de Docker](docker-tool.md) | Gestionar contenedores e imágenes de Docker | Ciclo de vida de contenedores, gestión de imágenes | Usar para entornos con contenedores |
| [Herramienta de carga de token OAuth](load-oauth-token-tool.md) | Obtener y gestionar de forma segura tokens OAuth | Gestión de tokens, autenticación segura | Usar para autenticación segura |
| [Herramienta de inicialización de organización](org-init-tool.md) | Inicializar la configuración de la organización | Configuración de la organización, configuración |  |

### Herramientas de gestión de archivos

| Nombre de la herramienta | Descripción | Funcionalidades clave | Cuándo usarla |
|-----------|-------------|--------------|-------------|
| [Herramienta de adjuntar archivo](attach-file-tool.md) | Adjuntar archivos a conversaciones o procesos | Adjuntar archivos, gestión de metadatos |  |
| [Herramienta de copia de archivos](file-copy-tool.md) | Copiar archivos entre ubicaciones | Operaciones de archivos, gestión de rutas | Usar para duplicar archivos |
| [Herramienta de descarga de archivos](file-downloader-tool.md) | Descargar archivos desde URLs | Descargas HTTP, guardado de archivos | Usar para obtener archivos remotos |
| [Herramienta de impresión de directorio](print-directory-tool.md) | Listar y mostrar el contenido de directorios | Navegación por directorios, listado de archivos |  |
| [Herramienta de lectura de archivos](read-file-tool.md) | Leer el contenido de archivos de texto | Lectura de archivos, extracción de contenido | Usar para examinar el contenido de archivos |
| [Herramienta de descompresión](uncompress-tool.md) | Extraer archivos comprimidos y archivos | Extracción de archivos, múltiples formatos |  |
| [Herramienta de escritura de archivos](write-file-tool.md) | Escribir y editar archivos de texto | Creación de archivos, escritura de contenido, copias de seguridad | Usar al crear o modificar archivos |

### Herramientas de IA y procesamiento de datos

| Nombre de la herramienta | Descripción | Funcionalidades clave | Cuándo usarla |
|-----------|-------------|--------------|-------------|
| [Herramienta de audio](audio-tool.md) | Procesar y analizar archivos de audio | Procesamiento de audio, reconocimiento de voz | Usar para análisis de voz y audio |
| [Herramienta de memoria](memory-tool.md) | Gestionar memorias persistentes usando una base de datos vectorial | Operaciones CRUD, búsqueda semántica, aislamiento de usuario | Usar para almacenamiento persistente de información |
| [Herramienta de OCR](ocr-tool.md) | Reconocimiento óptico de caracteres para imágenes | Extracción de texto, procesamiento de imágenes | Usar para extraer texto de imágenes |
| [Herramienta de PDF a imágenes](pdf-to-images-tool.md) | Convertir páginas PDF a formatos de imagen | Procesamiento de PDF, conversión de imágenes |  |
| [Herramienta de Tavily](tavily-tool.md) | Realizar búsquedas web usando el motor de búsqueda Tavily | Búsqueda en Internet, recuperación de información | Usar para búsqueda web y recopilación de información |

### Herramientas de documentos y hojas de cálculo

| Nombre de la herramienta | Descripción | Funcionalidades clave | Cuándo usarla |
|-----------|-------------|--------------|-------------|
| [Herramienta de Etendo SQL a CSV](etendo-sql-to-csv-tool.md) | Ejecutar consultas SQL en Etendo y exportar resultados a CSV | Consultas a base de datos, exportación a CSV, validación de seguridad | Usar para consultas a base de datos y exportación |
| [Herramienta de Google Drive](google-drive-tool.md) | Interactuar con servicios de Google Drive | Almacenamiento en la nube, gestión de archivos | Usar para integración con Google Workspace |
| [Herramienta de Google Spreadsheet](google-spreadsheet-tool.md) | Gestionar documentos de Google Sheets | Operaciones de hojas de cálculo, manipulación de datos | Usar para integración con Google Workspace |
| [Herramienta de plantillas](template-tool.md) | Generar documentos a partir de plantillas | Procesamiento de plantillas, generación de documentos |  |
| [Herramienta de XLS](xls-tool.md) | Gestionar archivos de hojas de cálculo de Excel | Procesamiento de Excel, extracción de datos |  |

### Herramientas de comunicación

| Nombre de la herramienta | Descripción | Funcionalidades clave | Cuándo usarla |
|-----------|-------------|--------------|-------------|
| [Herramienta de envío de correo electrónico](send-email-tool.md) | Enviar correos electrónicos mediante servicios configurados | Envío de correo, soporte de adjuntos | Usar para notificaciones y comunicación |

### Herramientas de desarrollo y pruebas

| Nombre de la herramienta | Descripción | Funcionalidades clave | Cuándo usarla |
|-----------|-------------|--------------|-------------|
| [Herramienta de códigos de barras](codbar-tool.md) | Generar y procesar códigos de barras | Generación de códigos de barras, varios formatos |  |
| [Herramienta de definición de proceso Jasper](process-definition-jasper-tool.md) | Gestionar definiciones de informes Jasper | Procesamiento de informes, gestión de definiciones |  |
| [Herramienta de creación de tareas](task-creator-tool.md) | Crear y definir nuevas tareas | Creación de tareas, gestión de flujos de trabajo | Usar para automatización de flujos de trabajo |
| [Herramienta de gestión de tareas](task-management-tool.md) | Gestionar tareas y flujos de trabajo existentes | Operaciones de tareas, gestión de estados | Usar para automatización de flujos de trabajo |
| [Herramienta de ejecución de pruebas](test-run-tool.md) | Ejecutar pruebas y procedimientos de validación | Ejecución de pruebas, informes de resultados | Usar para validación y pruebas |

### Herramientas de traducción y localización

| Nombre de la herramienta | Descripción | Funcionalidades clave | Cuándo usarla |
|-----------|-------------|--------------|-------------|
| [Herramienta de traducción de XML](xml-translation-tool.md) | Traducir el contenido y la estructura de XML | Procesamiento de XML, servicios de traducción |  |



!!! tip "Resolución de problemas"

    Para incidencias con herramientas específicas:

    - Consulte la documentación de cada herramienta para conocer los requisitos de configuración.
    - Verifique que todas las variables de entorno necesarias estén configuradas.
    - Asegúrese de que dispone de los permisos adecuados para las operaciones del sistema de archivos.
    - Valide la conectividad de red para las herramientas de servicios externos.
    - Revise los registros de errores para obtener información detallada de depuración.