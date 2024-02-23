---
title: "Optical Character Recognition (OCR) Tool"
tags:
    - Copilot
    - IA
    - Machine Learning
    - OCR
    - Image Recognition
---
:octicons-package-16: Javapackage: com.etendoerp.copilot.ocrtool

## Overview
Optical Character Recognition (OCR) Tool is a tool that recognizes text from images or pdfs. It is a tool that can be used in Copilot Apps to extract information from images or pdfs that are uploaded to the chat.

## Functionality


1. Add Copilot OCR Tool dependency in the Etendo Classic project, In `build.gradle`, add:
    ```groovy
    implementation('com.etendoerp:copilot.ocrtool:1.0.0')
    ```

3. Restart Docker image using `./gradlew copilot.stop` and `./gradlew copilot.start` tasks

4. You need to do a _update.database smartbuild_ to compile the environment of Etendo Classic.

``` bash title="Terminal"
./gradlew update.database smartbuild --info
``` 

4. After that, you must configure the tool in a Copilot App, in order to do that, go to _Copilot App_ and pick the _OCR Tool_ option in the _Tool_ tab.

5. Update you application:
    - If its an OpenAI Assistant, click in the _Sync OpenAI Assistant_ button.
    - If its a Langchain App, restart copilot with the following commands:
    ``` bash title="Terminal"
    ./gradlew copilot.stop
    ./gradlew copilot.start
    ```

5. Now your Copilot App is ready to use the OCR Tool to recognize text from images or pdf that you upload in the chat.

## Examples

!!! info 
    It is important to clarify that this is a first version subject to improvements. Maybe the tool is not able to recognize all the images or pdfs that are presented to it.
    The Tool in general returns the information in json format, but the information in the JSON may not reach the user directly, since Copilot can reinterpret the information summarizing it. It is recommended to either specify the result you expect well or ask it to show you the complete JSON.
    
### Requesting text recognition from an image/pdf

After the configuration, you can upload an image or pdf to the chat and the tool will recognize the text:
    
1. Open Copilot button and open a chat with the OpenAI Assistant.
2. Upload a image or pdf to the chat. If you specify the information you want to extract from the image, the tool will return the information in the chat.
3. The tool will recognize the text and return it in the chat.


We attach an image of an invoice

![](../../../assets/developer-guide/etendo-copilot/available-tools/ocr-tool.png)

and Copilot will return the recognized(and interpreted) text in the chat.

![](../../../assets/developer-guide/etendo-copilot/available-tools/ocr-tool.gif)
### Result chaining
Remember that the result of the tool can be used in other tools, for example, you can use the result of the OCR Tool a tool that writes the information in a database or sends it to a web service. 
   

