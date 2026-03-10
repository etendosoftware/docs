---
tags:
    - Copilot
    - Reconocimiento de audio
    - Audio
    - Transcripción
---

# Herramienta de audio

:octicons-package-16: Paquete Java: `com.etendoerp.copilot.toolpack`

## Visión general

La Herramienta de audio es una herramienta que reconoce texto a partir de archivos de audio. Puede utilizarse en Agentes para extraer información de archivos de audio, como transcribir entrevistas, reuniones o podcasts. La herramienta acepta como entrada la ruta de un archivo de audio y devuelve el texto extraído del audio.

!!!info
    Para poder incluir esta funcionalidad, debe estar instalado el Copilot Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. Para más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Copilot Extensions - Notas de la versión](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

## Funcionalidad

Esta herramienta automatiza el proceso de **extracción de texto a partir de archivos de audio**. Esto puede ser especialmente útil para tareas como transcribir conversaciones o discursos a partir de grabaciones de audio. La herramienta utiliza un modelo de conversión de voz a texto para convertir el contenido de audio en texto.

El uso de esta herramienta consta de las siguientes acciones:

- Recepción de parámetros:

    - La herramienta recibe un objeto de entrada que contiene la ruta del archivo de audio que se va a procesar.
    - **ruta**: La ruta del archivo de audio que se va a procesar.
       
- Obtención del archivo:

    - La herramienta recupera el archivo especificado en el parámetro **ruta**. Verifica la existencia del archivo y garantiza que esté en un formato compatible (esta herramienta utiliza el [modelo Whisper de OpenAI ](https://platform.openai.com/docs/guides/speech-to-text)).


- Devolución del resultado:

    - La herramienta devuelve un objeto JSON que contiene el texto extraído del archivo de audio.
    - **Mensaje**: El texto extraído del archivo de audio.

## Ejemplo de uso

### Solicitud de reconocimiento de texto a partir de un archivo de audio

Suponga que tiene un audio en `/home/user/request.mp3` y desea extraer texto relacionado con la información de una factura: 

**Contenido de audio**
``` txt
Can you create a new invoice for the customer John Doe with the following items: 2 Product A, 1 Product B and 3 Product C
```

- Utilice la herramienta de la siguiente manera:

    - Entrada:

        ```
        {
            "path": "/home/user/request.mp3"
        }
        ```

    - Salida:

        ``` Json title="Output Json"
        {
            "message": "Can you create a new invoice for the customer John Doe with the following items: 2 Product A, 1 Product B and 3 Product C"
        }
        ```

!!!note
    Recuerde que el resultado de la herramienta puede utilizarse en otras herramientas; por ejemplo, puede usar el resultado de la Herramienta de audio como entrada para un agente que utilice el texto extraído para crear una factura.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.