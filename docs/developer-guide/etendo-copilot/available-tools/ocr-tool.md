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

The Optical Character Recognition (OCR) Tool is an advanced tool that extracts structured data from images and PDF documents. It uses vision AI models to recognize and extract text, with support for automatic reference template matching, structured output schemas, and multi-provider configuration.

**Key Features:**

- **Automatic Reference Matching**: Searches for similar reference templates in the agent's vector database to guide extraction with visual markers
- **Structured Output Schemas**: Supports predefined schemas (Invoice, Receipt, etc.) and extensible custom schemas
- **Multi-format Support**: JPEG, PNG, WebP, GIF, and multi-page PDF files
- **Multi-provider Support**: Compatible with OpenAI (GPT-4o, GPT-5-mini) and Gemini models
- **Advanced Configuration**: Per-agent model configuration, PDF quality control, and threshold filtering

!!!info
    To be able to include this functionality, the Copilot Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. For more information about the available versions, core compatibility and new features, visit [Copilot Extensions - Release notes](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

## Functionality

This tool automates the process of **text extraction from image-based files or PDFs**. This can be particularly useful for tasks such as document digitization, data extraction, and content analysis. 

Using this tool consists of the following actions:

- **Receiving Parameters**:

    The tool receives an input object that contains the following parameters:

    - **path** (required): The absolute or relative path of the image or PDF file to be processed. The file must exist in the local file system.
    
    - **question** (required): A contextual question or instructions specifying the information to be extracted from the image. Be precise about the data fields needed (e.g., 'Extract invoice number, date, total amount, and vendor name'). Clear instructions improve extraction accuracy.
    
    - **structured_output** (optional): Specify a schema name to use structured output format (e.g., 'Invoice', 'Receipt'). Available schemas are loaded from `tools/schemas/` directory. When specified, the response will follow the predefined schema structure. Leave empty for unstructured JSON extraction.
    
    - **scale** (optional): PDF render scale factor (e.g., 2.0 = ~200 DPI, 3.0 = ~300 DPI). Higher values yield better quality but larger size and slower processing. Default: 2.0.
    
    - **disable_threshold_filter** (optional): When `true`, ignore the configured similarity threshold and return the most similar reference found in the agent database (disables threshold filtering). Default: `false`.
    
    - **force_structured_output_compat** (optional): When `true` (or when the selected model starts with 'gpt-5'), do not use the LLM's structured-output wrapper. Instead the tool will request structured output by embedding the schema JSON directly into the system prompt for compatibility with older agents. Default: `false`.

- Obtaining the File:

    - The tool retrieves the file specified in the **path** parameter. It verifies the existence of the file and ensures it is in a supported format (JPEG, JPG, PNG, WEBP, GIF, PDF).

- PDF Conversion:

    - If the input file is a PDF, it is converted to an image format (JPEG) using the **pypdfium2** library. Each page of the PDF is rendered as a separate image.

- Image Conversion:

    - Other image formats are processed directly or converted to JPEG if necessary.

- Image Processing:

    - The image is processed using a Vision AI model (OpenAI GPT or Google Gemini, depending on configuration). This model interprets the text within the image and extracts the relevant information based on the provided **question**.

- Returning the Result:

    - The tool returns a JSON object containing the extracted information from the image or PDF.

## Advanced Features

### Automatic Reference Template Matching

The OCR Tool includes an intelligent reference system that automatically searches for similar document templates in the agent's vector database. When a similar reference is found, it guides the extraction process by indicating which data fields to extract.

**How it works:**

1. When processing a document, the tool searches the agent's vector database (ChromaDB) for similar reference images
2. Reference images contain visual markers (red boxes) highlighting the relevant data fields to extract
3. The tool uses the reference as a template to prioritize and extract the same fields from the current document
4. This significantly improves extraction accuracy for documents with consistent layouts (invoices, receipts, forms)

**Managing Reference Images:**

- Upload reference images to the agent's database using the `/addToVectorDB` endpoint
- Reference images should have visual markers (typically red boxes) indicating the data fields
- Each agent maintains its own vector database of reference templates
- The similarity threshold can be controlled or disabled using the `disable_threshold_filter` parameter

**When to use references:**

- Processing invoices, receipts, or forms with consistent layouts
- When you need to extract specific fields repeatedly from similar documents
- To improve extraction accuracy by providing visual guidance

### Structured Output Schemas

The tool supports predefined schemas that enforce a specific output structure. This is useful when you need consistent data formats for downstream processing.

**Available schemas:**

Schemas are stored in the `tools/schemas/` directory and can be extended with custom schemas. Common schemas include:

- **Invoice**: Standard invoice fields (number, date, amounts, line items, etc.)
- **Receipt**: Receipt-specific fields
- Custom schemas can be added by creating new schema files in the schemas directory

**Usage:**

```json
{
    "path": "/home/user/invoice.pdf",
    "question": "Extract the invoice information",
    "structured_output": "Invoice"
}
```

The tool will return data following the exact structure defined in the schema, ensuring consistency across all extractions.

**Compatibility mode:**

For older models or agents that don't support native structured output, use the `force_structured_output_compat` parameter. This embeds the schema JSON directly into the system prompt:

```json
{
    "path": "/home/user/invoice.pdf",
    "question": "Extract the invoice information",
    "structured_output": "Invoice",
    "force_structured_output_compat": true
}
```

### Multi-Provider Configuration

The OCR Tool supports multiple AI providers with flexible configuration options:

**Supported Providers:**

- **OpenAI**: Models like `gpt-4o`, `gpt-5-mini` (default: `openai/gpt-5-mini`)
- **Gemini**: Google's Gemini vision models

**Configuration methods (in priority order):**

1. **Environment variable**: Set `COPILOT_OCRTOOL_MODEL` to configure the model globally for all agents
   ```bash
   export COPILOT_OCRTOOL_MODEL="gpt-4o"
   ```

2. **Per-agent configuration**: Configure the model in the **Skills and Tools** tab of the Agent window using the **Model** field. The model must be specified using the format `provider/modelname` (e.g., `openai/gpt-4o`, `google/gemini-1.5-pro`). This allows different agents to use different models for the same tool.

3. **Default**: If no configuration is provided, uses `openai/gpt-5-mini` with OpenAI provider

**Provider detection:**

The provider is automatically detected based on the model name:
- Models starting with `gpt-` use OpenAI provider
- Models starting with `gemini` use Gemini provider

### PDF Quality Control

For PDF documents, you can control the rendering quality using the `scale` parameter:

**Scale values:**

- `2.0`: ~200 DPI (default) - Good balance between quality and performance
- `3.0`: ~300 DPI - Higher quality, recommended for documents with small text
- `4.0`: ~400 DPI - Maximum quality, slower processing and larger memory usage

**Example:**

```json
{
    "path": "/home/user/contract.pdf",
    "question": "Extract all contract clauses",
    "scale": 3.0
}
```

**Considerations:**

- Higher scale values produce better OCR accuracy for small or complex text
- Increases processing time and memory consumption
- Choose based on your document's text size and complexity

### Performance Optimizations

The tool includes several optimizations for better performance:

- **In-memory processing**: Images and PDFs are converted to base64 directly in memory without disk I/O
- **Efficient PDF rendering**: Uses pypdfium2 for fast PDF-to-image conversion
- **Automatic cleanup**: Temporary files are automatically removed after processing
- **Parallel page processing**: Multi-page PDFs are processed efficiently

## Usage Example

    
### Requesting text recognition from an image/pdf


Suppose you have an image at `/home/user/invoice.png` and you want to extract invoice information:

The following is an example image of an invoice:

![](../../../assets/developer-guide/etendo-copilot/available-tools/ocr-tool-2.png)


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

### Advanced Usage: Structured Output with Reference

Suppose you have uploaded a reference invoice image to your agent's vector database, and now you want to extract invoice data with a predefined schema:

- Use the tool with structured output:

    - Input:

        ```json
        {
            "path": "/home/user/new_invoice.pdf",
            "question": "Extract the invoice information following the reference template",
            "structured_output": "Invoice",
            "scale": 3.0,
            "disable_threshold_filter": false
        }
        ```

    - The tool will:
        1. Search for a similar reference invoice in the vector database
        2. Use the reference's visual markers to guide extraction
        3. Render the PDF at 300 DPI for better quality
        4. Return data following the Invoice schema structure

    - Output:

        ```json
        {
            "invoice_number": "INV-2024-001",
            "date": "2024-12-16",
            "currency": "EUR",
            "vendor": {
                "name": "Example Corp",
                "tax_id": "B-12345678",
                "address": "Main Street 123"
            },
            "items": [
                {
                    "description": "Product A",
                    "quantity": 10,
                    "unit_price": 50.00,
                    "total": 500.00
                }
            ],
            "subtotal": 500.00,
            "tax_amount": 90.00,
            "total": 590.00
        }
        ```

### Usage with Custom Model Configuration

You can configure a specific model for OCR processing in multiple ways:

**Option 1: Using environment variables (global configuration)**

```bash
# Use GPT-4o for better accuracy
export COPILOT_OCRTOOL_MODEL="gpt-4o"
```

**Option 2: Using the Agent window (per-agent configuration)**

1. Open the **Agent** window in Etendo Classic
2. Go to the **Skills and Tools** tab
3. Select the OCR Tool from the list
4. In the **Model** field, specify the model using the format `provider/modelname`:
   - For OpenAI: `openai/gpt-4o` or `openai/gpt-5-mini`
   - For Gemini: `google/gemini-1.5-pro`
5. If left empty, the tool will use the default model (`openai/gpt-5-mini`)

This allows you to use different models for different agents depending on their specific needs (e.g., high accuracy for invoices vs. speed for receipts).

### Result Chaining

!!!note
    Remember that the result of the tool can be used in other tools, for example, you can use the result of the OCR Tool in a tool that writes the information in a database or sends it to a web service. 

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.
