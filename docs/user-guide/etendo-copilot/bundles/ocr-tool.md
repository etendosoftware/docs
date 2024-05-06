---
tags:
    - Copilot
    - IA
    - Machine Learning
    - OCR
    - Image Recognition
---

# Optical Character Recognition (OCR) Tool

:octicons-package-16: Javapackage: com.etendoerp.copilot.ocrtool

!!! info
    To be able to include this functionality, the Copilot Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. 
    
## Overview

The Optical Character Recognition (OCR) Tool is a tool that recognizes text from images or pdfs. It can be used in Copilot Apps to extract information from images or pdfs that are uploaded to the chat.

## Setup

In order to use this tool, it is necessary to:

1. Go to `Application` >`Service`> `Copilot` > `Copilot App`
2. Select the **OCR Tool** option in the **Tool** tab.
3. Update the application by clicking the **Sync OpenAI Assistant** button.
4. Now your Copilot App is ready to use the OCR Tool to recognize text from images or pdf that you upload in the chat.

## Requesting Text Recognition from an Image/PDF

After the configuration, you can upload an image or pdf to the chat and the tool will recognize the text:
    
1. Open Copilot button and open a chat with the OpenAI Assistant.
2. Upload an image or pdf to the chat. If you specify the information you want to extract from the image, the tool will return the information in the chat.
3. The tool will recognize the text and return it in the chat.

We attach an image of an invoice

![](../../../assets/developer-guide/etendo-copilot/available-tools/ocr-tool.png)

and Copilot will return the recognized(and interpreted) text in the chat.

![](../../../assets/developer-guide/etendo-copilot/available-tools/ocr-tool.gif)

!!! Info "Technical Details for Developers"
    More information about how the OCR Tool can be found in the [OCR Tool Developer Guide](../../../developer-guide/etendo-copilot/available-tools/ocr-tool.md) page.