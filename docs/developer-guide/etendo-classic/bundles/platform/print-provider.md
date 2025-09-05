---
title: Print Provider - Developer Guide
tags:

  - Print
  - Print Provider
  - PrintNode register
  - Print Provider register
  - Register a Print Provider
status: beta
---

# Print Provider

!!!example "IMPORTANT:THIS IS A BETA VERSION"
    - It is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**, especially in production environments.
    - It should be used with **caution**, and you should always **validate backups** before executing any critical operation.

## Register a new Print Provider

This guide explains how to extend the Print Provider module to integrate an external print provider (e.g., PrintNode, Bartender, Hardware Manager, etc.). The goal is for any module to be able to register its own connector without duplicating common logic and only create buttons pointing to the Send Print Job Action for sending print jobs, which will also automatically resolve the list of available printers and the corresponding print template.

## Architecture

The **main components of the Print Provider module** are:

- **PrintProviderStrategy** (Service Provider Interface): Contract to be implemented by each provider. It exposes three operations

    \- fetchPrinters (Provider) → list of printers (PrinterDTO).

    \- generateLabel (Provider, Table, recordId, TemplateLine, params) → File (PDF).

    \- sendToPrinter (Provider, Printer, copies, labelFile) → String (jobId).

- **Resolve ProviderStrategyResolver**:  Given a Provider (registered in the Print Providers window), find its ProvidersImplementation (Provider Implementation window), load the class (java Implementation), and return an instance of the strategy.

- **PrinterUtils utilities**: Cross-functional helpers 

    \- Carga/validación de entidades (requireProvider, requirePrinter, requireTableByName, resolveTemplateLineFor).

    \- Parámetros de proceso/JSON (requireParam, requireJSONArray, requirePositiveInt).

    \- Parámetros de proveedor (getRequiredParam, providerParamContentCheck).

    \- Plantillas Jasper (resolveTemplateFile, loadOrCompileJasperReport).

    \- Helpers de resultados de proceso (fail, warning).

- **Actions**, ready to use

    \- UpdatePrinters → sincroniza catálogo de impresoras del proveedor (alta/actualiza/inhabilita).

    \- SendGeneratedLabelToPrinter → genera la etiqueta (Jasper) y la envía a la impresora elegida.

- **Modelo de datos clave**

    \- Provider — Configuración del proveedor de impresión (enlaza implementación, parámetros e impresoras).

    \- ProvidersImplementation — Define la clase Java (FQN) de la estrategia/SPI a usar por el proveedor.

    \- ProviderParam — Parámetros clave/valor del proveedor (p. ej., apikey, printersurl, printjoburl).

    \- Printer — Impresora registrada localmente para un proveedor (ID externo, nombre, “default”, activo).

    \- Template — Cabecera de plantilla asociada a una tabla; agrupa sus líneas.

    \- TemplateLine — Variante de plantilla (ruta .jrxml/.jasper, “default”, orden/lineNo).

## How to Create a New Supplier

1. **Create the strategy class**: Create a class in the module that extends `PrintProviderStrategy`. 


    ``` title="Skeleton Example"
    public class MyProviderStrategy extends PrintProviderStrategy {
     // (optional) constants for timeouts, MIME, etc.

     @Override

     public List<PrinterDTO> fetchPrinters(Provider provider) throws PrintProviderException {
       // 1) Validate provider and required params

       final ProviderParam printersUrl = PrinterUtils.getRequiredParam(provider, "printersurl");

       PrinterUtils.providerParamContentCheck(printersUrl, "printersurl");
       // 2) Build HTTP client/request
       // 3) Send and handle InterruptedException (re-set interrupt + rethrow with context)
       // 4) Validate statusCode and parse JSON → List<PrinterDTO>
       // 5) Return list
     }
     @Override

     public File generateLabel(Provider provider, Table table, String recordId,

     TemplateLine templateRef, JSONObject params) throws PrintProviderException {
       // Use PrinterUtils.resolveTemplateFile + loadOrCompileJasperReport
       // Fill report (DOCUMENT_ID, SUBREPORT_DIR)
       // Export PDF to a temp file and return it
     }

     @Override

     public String sendToPrinter(Provider provider, Printer printer, int numberOfCopies, File labelFile)

         throws PrintProviderException {
       // 1) Validate inputs (provider/printer/file)
       // 2) Read required ProviderParams (e.g., printjoburl, apikey)
       // 3) Prepare request body (e.g., base64, title, source)
       // 4) POST; validate response; extract jobId (if available)
     }

     @Override

     public File generateLabel(Provider provider, Table table, String recordId,

                               TemplateLine templateRef, JSONObject params) throws PrintProviderException {
       // Use PrinterUtils.resolveTemplateFile + loadOrCompileJasperReport
       // Fill report (DOCUMENT_ID, SUBREPORT_DIR)
       // Export PDF to a temp file and return it
     }

     @Override

     public String sendToPrinter(Provider provider, Printer printer, int numberOfCopies, File labelFile)

         throws PrintProviderException {
       // 1) Validate inputs (provider/printer/file)
       // 2) Read required ProviderParams (e.g., printjoburl, apikey)
       // 3) Prepare request body (e.g., base64, title, source)
       // 4) POST; validate response; extract jobId (if available)

     }
    }
    ```

    **Contractual conventions**

    - Printer.value stores the external ID of the printer (key for “upsert”).

    - Throw PrintProviderException (extends OBException) for functional/integration failures.

    - Do not log secrets (API keys); log context (statusCode, truncated bodies).

2. **Register the implementation**

    - **AD → Provider Implementation**

        \- Java Implementation: com.mi.modulo.print.MyProviderStrategy

    - **AD → Print Provider**

        \- Reference to the previous implementation.

    - **AD → Provider Param**

        \- Define the keys (reuse if applicable): printersurl, printjoburl, apikey, etc.

        \- Save values (e.g., your API URLs).

## How to Register Labels (Jasper)

1. Create a new record in the **Print Templates** window, indicating the table to which it applies.

2. Indicate the location of your template in the lines tab. `TemplateLine.templateLocation` accepts:

    \- @basedesign@/...

    \- @<módulo>@/...

    \- Rutas relativas a basedesign

**Technical Details**

- The priority applies to the “Default” check; otherwise, you will get the one with the lowest sequence number.

- PrinterUtils.resolveTemplateFile resolves locations in src-loc/design and web.

- PrinterUtils.loadOrCompileJasperReport supports .jrxml (compile) and .jasper (load).

!!! note "Recommended parameters"

    \- DOCUMENT_ID = recordId

    \- SUBREPORT_DIR = template directory (for subreports)

### Printer Update

- The process calls strategy.fetchPrinters(provider) and performs an upsert on Printer:

    \- **Create** if it does not exist (provider, value=externalId).

    \- **Update** name/default if it already exists.

    \- **Deactivate** printers from the provider that were not included in this synchronization.

- Printer.value = external ID; Printer.name is user-friendly; Printer.default marks “default.”

!!!note "Recommendation"
    If the provider's API does not return a single field that can serve as a stable key, one can be composed (e.g.,  < accountId >:< remotePrinterId >).

### Errors

- Use PrintProviderException for exception handling.

- Log the messages you need in AD_MESSAGE. You can access these messages using the String.format and OBMessageUtils.getI18NMessage formatting utilities.

## Workflow and Configuration

!!! Note 
    Remember that the initial configuration must be performed only once, as the system administrator. Provider parameters such as printersurl and apikey must be defined correctly to avoid connection or printer synchronization failures.

1. **Configuration** (one-time)

    - As System administrator, create a record in Providers Implementation indicating the path of your strategy class.

    - As administrator, create a Provider that references the implementation defined in the previous step.

    - In the Provider Params tab, define the required parameters (URLs, API key, etc.).

2. **Discover Printers**

    - UpdatePrinters (Action executed from the Printers window) → use fetchPrinters from the strategy and synchronize Printer.

3. **Generate Label**

    - SendGeneratedLabelToPrinter (Action executed from the button in the desired window) resolves TemplateLine from the table associated with the button window (e.g., button in Product window will resolve table M_Product). This action compiles/loads Jasper and produces the temporary PDF.

4. **Send to printer**

    - sendToPrinter makes the necessary HTTP/SDK call and returns jobId (when available).

### Basic Example

- In the module, create `com.my.module.print.MyProviderStrategy` (extends PrintProviderStrategy).

- Configuration per window
    
    - Provider Implementation:

        \- specify javaImplementation = com.my.module.print.MyProviderStrategy

    - Print Provider:

        \- specify the previously registered provider in providers implementation.

    - ProviderParam:

        \- printersurl: URL for obtaining printers.

        \- printjoburl: URL for sending print jobs.

        \- apikey: Key for authenticating with the middleware.

- Run **Update Printers** from the **Printers** window. The Action delegates responsibility for updating printers to the fetchPrinters implementation.

- Execute **Send label to printer** from the button that has been registered in the desired window. The Action `SendGeneratedLabelToPrinter` delegates the responsibility of:

    \- Generating the printout to your generateLabel implementation.

- Sending the previous print job to your sendToPrinter implementation.


---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.