---
tags:
    - Copilot
    - IA
    - PDF
    - Images
    - Tool
---

# PDF to Images Tool

:octicons-package-16: Javapackage: `com.etendoerp.copilot.toolpack`

## Overview

The **PDF to Images Tool** is a tool that converts a PDF file into an array of images, with each image representing a page of the PDF. The tool utilizes specialized Python libraries for PDF processing and image handling to achieve this conversion efficiently.

!!!info
    To be able to include this functionality, the Copilot Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. For more information about the available versions, core compatibility and new features, visit [Copilot Extensions - Release notes](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md){target="\_blank"}.

## Functionality

This tool allows assistants to convert PDF documents into image formats. This is particularly useful for scenarios where individual pages of a PDF need to be processed as images, such as in digital archiving, document review, or further image analysis tasks.

It is invaluable for any automated workflow that requires handling PDF contents as image data. It simplifies the process of converting PDF pages to images, ensuring each page is accurately rendered and saved as a high-quality image. This tool is essential in fields such as digital archiving, where documents need to be preserved in an easily accessible and viewable format, and in applications involving image analysis, where each page of a PDF document can be independently processed.

Using this tool consists of the following actions:

- **Receiving Parameters** 

    The tool receives an input object that contains the following key:

    - path

        (str): the path to the PDF file to be converted.

- **Processing**

    - Validation: The tool first checks if the provided PDF path points to an existing file. If the file does not exist, it raises an exception with a relevant error message.

    - PDF Loading: The tool uses the pypdfium2 library to load the PDF document.

    - Page Rendering: For each page in the PDF:

        - The page is rendered at a scale of 2.0 to produce a high-quality image.

        - The rendered bitmap is then converted to a PIL (Python Imaging Library) image.

    - Temporary Storage: Each converted image is temporarily stored on the filesystem at a predefined path (`/tmp/page_{page_number}.png`).

    - Collecting Results: Paths to the stored images are collected in a list, which is returned as the final output.

- **Returning the Result**

    Once the conversion process is completed, the tool returns a list of file paths, each pointing to the respective converted image for each page of the PDF.


## Usage Example

If you have a PDF file located at `/home/user/document.pdf` and you want to convert its pages into images, you would use the tool as follows:

- **Input**:

```
{
  "path": "/home/user/document.pdf"
}
```

- **Output**:

```
[
  "/tmp/page_0.png",
  "/tmp/page_1.png",
  "/tmp/page_2.png"
  // paths for all pages
]
```