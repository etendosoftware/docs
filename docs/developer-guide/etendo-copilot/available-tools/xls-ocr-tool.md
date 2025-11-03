---
title: XLS OCR Tool
tags:
    - Copilot
    - XLS Processing
    - Data Extraction
    - Excel
    - OCR
    - CSV
---

# XLS OCR Tool

:octicons-package-16: Javapackage: `com.etendoerp.copilot.toolpack`

## Overview

The XLS OCR Tool processes Excel files (`XLS`, `XLSX`, `CSV`) using Optical Character Recognition (OCR) and Vision AI models to extract structured data. Unlike traditional Excel processing tools, this tool converts spreadsheet sheets into images and uses advanced vision models to understand and extract data, making it particularly effective for complex layouts, formatted cells, or when traditional parsing methods fail.

!!!info
    To include this functionality, the Copilot Extensions Bundle must be installed. Follow the instructions from the marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. For more information about available versions, core compatibility, and new features, visit [Copilot Extensions - Release notes](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

## Functionality

This tool automates the process of **intelligent data extraction from Excel files using OCR and Vision AI**. It is particularly useful for processing complex spreadsheets with irregular layouts, merged cells, formatted data, or when you need to extract specific information based on visual patterns rather than structured data parsing.

Using this tool consists of the following actions:

- **Receiving Parameters**:

    - The tool receives an input object containing the file path of the Excel file and a specific question or instruction for data extraction.
    - **path**: The path to the Excel file to be processed (supports `.xls`, `.xlsx`, and `.csv` formats).
    - **question**: Precise instruction on what to extract from the file content (optional, defaults to extracting all useful information).

- **Processing the File**:

    - The tool renders each sheet of the Excel file as a high-resolution JPEG image using matplotlib.
    - Each sheet image is processed by a Vision AI model (GPT-4o by default) to understand the content.
    - The AI model analyzes the visual representation and extracts the requested information based on the provided question.

- **Returning the Result**:

    - The tool returns the extracted data as structured text or JSON format.
    - **result**: The processed data extracted from the Excel file based on the specific question or instruction.
    - **error**: Error message if the processing fails.

## Technical Details

- **Vision Model**: Uses GPT-4o by default (configurable via `COPILOT_OCRTOOL_MODEL` environment variable)
- **Image Processing**: Renders Excel sheets as images with automatic sizing based on content
- **Sheet Handling**: Processes all sheets in the Excel file
- **Cleanup**: Automatically removes temporary image files after processing
- **Error Handling**: Graceful error handling with detailed error messages

## Usage Examples

### Extracting product information from a catalog

For a product catalog with images, descriptions, and pricing:

- **Input**:

    ```json
    {
        "path": "/home/user/product_catalog.xlsx",
        "question": "Find all products with their names, SKUs, prices, and descriptions. Focus on items marked as 'Featured' or highlighted."
    }
    ```

- **Output**:

    ```json
    {
        "featured_products": [
            {
                "name": "Premium Widget",
                "sku": "PWG-001",
                "price": "$29.99",
                "description": "High-quality widget with premium features",
                "status": "Featured"
            }
        ]
    }
    ```

!!!note
    The XLS OCR Tool is ideal for processing legacy spreadsheets, complex reports, or any Excel file where traditional structured parsing methods are insufficient. The vision-based approach allows for more intelligent and flexible data extraction based on visual understanding rather than strict structural rules.

!!!warning
    Processing large Excel files or files with many sheets may take longer due to the image rendering and AI processing steps. Consider the file size and complexity when using this tool in time-sensitive applications.
