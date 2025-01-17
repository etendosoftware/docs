---
tags:
    - Copilot
    - OCR
    - Image Recognition
    - Optical Character Recognition
    - Tool
---

# Optical Character Recognition (OCR) Tool

:octicons-package-16: Javapackage: `com.etendoerp.copilot.ocrtool`

## Overview

The Optical Character Recognition (OCR) Tool is a tool that recognizes text from images or pdfs. It can be used in Assistants to extract information from images or pdfs that are uploaded to the chat.

!!!info
    To be able to include this functionality, the Copilot Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. For more information about the available versions, core compatibility and new features, visit [Copilot Extensions - Release notes](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

## Functionality

This tool automates the process of **text extraction from image-based files or PDFs**. This can be particularly useful for tasks such as document digitization, data extraction, and content analysis. 

Using this tool consists of the following actions:

- Receiving Parameters:

    - The tool receives an input object that contains two keys:

        - **path**: The path of the image or PDF file to be processed.
        - **question**: A contextual question specifying the information to be extracted from the image. This is mandatory for precise results.

- Obtaining the File:

    - The tool retrieves the file specified in the **path** parameter. It verifies the existence of the file and ensures it is in a supported format (JPEG, JPG, PNG, WEBP, GIF, PDF).

- PDF Conversion:

    - If the input file is a PDF, it is converted to an image format (JPEG) using the **pypdfium2** library. Each page of the PDF is rendered as a separate image.

- Image Conversion:

    - Other image formats are processed directly or converted to JPEG if necessary.

- Image Processing:

    - The image is processed using a Vision model powered by GPT. This model interprets the text within the image and extracts the relevant information based on the provided **question**.

- Returning the Result:

    - The tool returns a JSON object containing the extracted information from the image or PDF.

## Usage Example

    
### Requesting text recognition from an image/pdf


Suppose you have an image at `/home/user/invoice.png` and you want to extract text related to an invoice information:

The following is an example image of an invoice:

![](../../../assets/developer-guide/etendo-copilot/available-tools/ocr-tool.png)


- Use the tool as follows:

    - Input:

        ```
        {"path": "/home/user/invoice.png", "question": "Give me the content of this invoice"}

        ```

    - Output:

        ``` Json title="Output Json"
        {
            "company": {
                "name": "F&B España, S.A.",
                "tax_id": "B-1579173",
                "address": "Pg. de Gracia, 123 2-1ª",
                "city": "08009 - Barcelona (BARCELONA)"
            },
            "invoice": {
                "title": "This is a Sales invoice",
                "number": "1000000",
                "currency": "EUR",
                "date": "15-02-2011"
            },
            "customer": {
                "name": "Restaurantes Luna Llena, S.A.",
                "contact": "Ana Cortes",
                "phone": "092765188",
                "address": "Pl. Mayor, 78",
                "postal_code": "76764"
            },
            "items": [
                {
                "reference": "ES0024",
                "product_name": "Agua sin Gas 1L",
                "uom": "Unit",
                "quantity": 25000,
                "price": 1.13,
                "total": 28250.00
                },
                {
                "reference": "ES0021",
                "product_name": "Bebida Energética 0,5L",
                "uom": "Unit",
                "quantity": 45000,
                "price": 1.49,
                "total": 67050.00
                },
                {
                "reference": "ES1000",
                "product_name": "Cerveza Ale 0,5L",
                "uom": "Unit",
                "quantity": 33000,
                "price": 2.48,
                "total": 81840.00
                },
                {
                "reference": "ES1002",
                "product_name": "Cerveza Lager 0,5L",
                "uom": "Unit",
                "quantity": 45000,
                "price": 2.64,
                "total": 118800.00
                },
                {
                "reference": "ES0030",
                "product_name": "Cola de Cereza 0,5L",
                "uom": "Unit",
                "quantity": 40000,
                "price": 0.83,
                "total": 33200.00
                },
                {
                "reference": "ES0032",
                "product_name": "Limonada 0,5L",
                "uom": "Unit",
                "quantity": 40000,
                "price": 0.83,
                "total": 33200.00
                },
                {
                "reference": "ES0023",
                "product_name": "Vino Blanco 0,75L",
                "uom": "Unit",
                "quantity": 36000,
                "price": 3.05,
                "total": 109800.00
                },
                {
                "reference": "ES0025",
                "product_name": "Vino Rosado 0,75L",
                "uom": "Unit",
                "quantity": 36000,
                "price": 5.83,
                "total": 209880.00
                },
                {
                "reference": "ES1004",
                "product_name": "Vino Tinto 0,75L",
                "uom": "Unit",
                "quantity": 36000,
                "price": 5.07,
                "total": 182520.00
                },
                {
                "reference": "ES0037",
                "product_name": "Zumo de Naranja 0,5L",
                "uom": "Unit",
                "quantity": 45000,
                "price": 1.13,
                "total": 50850.00
                },
                {
                "reference": "ES1014",
                "product_name": "Zumo de Piña 0,5L",
                "uom": "Unit",
                "quantity": 33000,
                "price": 1.13,
                "total": 37390.00
                }
            ],
            "payment_terms": "30 days",
            "totals": {
                "subtotal": 927640.00,
                "tax": {
                "rate": "IVA 18%",
                "amount": 166975.20
                },
                "total": 1094615.20
            }
        }
        ```

### Result Chaining

!!!note
    Remember that the result of the tool can be used in other tools, for example, you can use the result of the OCR Tool in a tool that writes the information in a database or sends it to a web service. 