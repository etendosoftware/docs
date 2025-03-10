---
tags:
    - Copilot
    - Audio Recognition
    - Audio
    - Transcription
---

# Audio Tool

:octicons-package-16: Javapackage: `com.etendoerp.copilot.toolpack`

## Overview

The Audio Tool is a tool that recognizes text from audio files. It can be used in Assistants to extract information from audio files, such as transcribing interviews, meetings, or podcasts. The tool accepts an audio file path as input and returns the text extracted from the audio.

!!!info
    To be able to include this functionality, the Copilot Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. For more information about the available versions, core compatibility and new features, visit [Copilot Extensions - Release notes](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

## Functionality

This tool automates the process of **text extraction from audio files**. This can be particularly useful for tasks such as transcribing conversation or speech from audio recordings. The tool uses a speech-to-text model to convert the audio content into text.

Using this tool consists of the following actions:

- Receiving Parameters:

    - The tool receives an input object that contains the path of the audio file to be processed.
    - **path**: The path of the audio file to be processed.
       
- Obtaining the File:

    - The tool retrieves the file specified in the **path** parameter. It verifies the existence of the file and ensures it is in a supported format (this tool uses the [Whisper model of OpenAI ](https://platform.openai.com/docs/guides/speech-to-text)).


- Returning the Result:

    - The tool returns a JSON object containing the extracted text from the audio file.
    - **message**: The extracted text from the audio file.

## Usage Example

### Requesting text recognition from an audio file

Suppose you have an audio at `/home/user/request.mp3` and you want to extract text related to an invoice information: 

**Audio Content**
``` txt
Can you create a new invoice for the customer John Doe with the following items: 2 Product A, 1 Product B and 3 Product C
```

- Use the tool as follows:

    - Input:

        ```
        {
            "path": "/home/user/request.mp3"
        }
        ```

    - Output:

        ``` Json title="Output Json"
        {
            "message": "Can you create a new invoice for the customer John Doe with the following items: 2 Product A, 1 Product B and 3 Product C"
        }
        ```

!!!note
    Remember that the result of the tool can be used in other tools, for example, you can use the result of the Audio Tool as input for an agent that uses the extracted text to create an invoice.