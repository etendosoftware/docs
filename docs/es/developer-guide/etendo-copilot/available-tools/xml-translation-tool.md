---
tags:
    - Copilot
    - Herramienta de traducción
    - Traducción de módulos
    - Idioma
    - Localización
---

#  Herramienta de traducción XML

:octicons-package-16: Javapackage: `com.etendoerp.copilot.xmltranslationtool`

## Visión general

La XMLTranslationTool traduce directamente el contenido de los archivos XML en función del atributo de idioma especificado dentro del XML, lo que permite una localización eficaz y precisa en diferentes idiomas. 

!!!info
    Para poder incluir esta funcionalidad, debe estar instalado el Copilot Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. Para obtener más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Copilot Extensions - Notas de la versión](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

## Funcionalidad

La XMLTranslationTool permite a los agentes traducir el contenido de archivos XML de un idioma a otro, según se especifica dentro del propio XML. Esto resulta especialmente útil en escenarios en los que se requieren versiones localizadas del contenido XML para diferentes regiones o idiomas.

Esta herramienta es ideal para flujos de trabajo automatizados que necesitan gestionar traducciones XML de forma eficiente, permitiendo una adaptación fluida del contenido a varios idiomas. Al traducir directamente el contenido XML en función de los atributos de idioma especificados, garantiza una localización precisa del texto sin editar manualmente archivos individuales.

El uso de esta herramienta consta de las siguientes acciones:

- **Recepción de parámetros** 
    La herramienta recibe un objeto de entrada que contiene la siguiente clave:

    - relative_path 

        (str): La ruta relativa al directorio de archivos XML donde se requiere la traducción.

- **Procesamiento**

    1. Validación: La herramienta primero verifica si el relative_path proporcionado apunta a un directorio existente. Si el directorio no existe, devuelve un mensaje de error indicando el problema.

    2. Cálculo de ruta: Calcula la ruta absoluta del directorio XML en función de la ruta relativa proporcionada.

    3. Iteración de archivos XML: Para cada archivo XML del directorio:

        - Condición de omisión: Si un archivo ya está traducido, omite el proceso de traducción.

        - Proceso de traducción:
            
            - La herramienta utiliza la API de OpenAI para traducir el contenido de texto de cada archivo XML según el idioma de destino especificado en los atributos del XML.

            - Cada elemento no localizado se marca como "translated" después del procesamiento.

            - Si todos los archivos ya están traducidos, se devuelve un mensaje indicándolo.

    4. Recopilación de resultados: Las rutas de los archivos XML traducidos correctamente se recopilan en una lista, que se devuelve como salida final.

- **Devolución del resultado**

    Una vez completado el proceso de traducción, la herramienta devuelve una lista de rutas de archivos, cada una apuntando a un archivo XML traducido correctamente.

## Ejemplo de uso

Si tiene archivos XML ubicados en `/modules/com.etendoerp.webhookevents.es_es` que necesitan traducción, utilizaría la herramienta de la siguiente manera:

- **Entrada**:

```
{
  "relative_path": "/modules/com.etendoerp.webhookevents.es_es"
}
```

- **Salida**:

```
{
  "translated_files_paths": [
    "Successfully translated file /modules/com.etendoerp.webhookevents.es_es/AD_REF_LIST_TRL_es_ES.xml",
    "Successfully translated file /modules/com.etendoerp.webhookevents.es_es/AD_ELEMENT_TRL_es_ES.xml"
  ]
}
```

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.