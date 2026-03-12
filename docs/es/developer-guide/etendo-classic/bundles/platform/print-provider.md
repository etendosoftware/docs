---
title: Proveedor de impresión - Guía del desarrollador
tags:
  - Impresión
  - Proveedor de impresión
  - Registro de PrintNode
  - Registro de proveedor de impresión
  - Registrar un proveedor de impresión
---

# Proveedor de impresión

## Registrar un nuevo Proveedor de impresión

Esta guía explica cómo ampliar el módulo de Proveedor de impresión para integrar un proveedor de impresión externo (p. ej., PrintNode, Bartender, Hardware Manager, etc.). El objetivo es que cualquier módulo pueda registrar su propio conector sin duplicar la lógica común y solo crear botones que apunten a la Acción Enviar trabajo de impresión para enviar trabajos de impresión, lo que también resolverá automáticamente la lista de impresoras disponibles y la plantilla de impresión correspondiente.

## Arquitectura

Los **componentes principales del módulo Proveedor de impresión** son:

- **PrintProviderStrategy** (Service Provider Interface): contrato que debe implementar cada proveedor. Expone tres operaciones

    - `fetchPrinters` (Proveedor): lista de impresoras (PrinterDTO).

    - `generateLabel` (Proveedor, Tabla, recordId, Línea de plantilla, params): Archivo (PDF).

    - `sendToPrinter` (Proveedor, Impresora, copias, labelFile): String (jobId).


### Implementación del proveedor
:material-menu: `Configuración General` > `Configuración del Proveedor de impresión` > `Implementación del proveedor`

!!! info
    El acceso a esta ventana está restringido a usuarios con el rol de Administrador del sistema (Sys). Los usuarios operativos no podrán modificar estos ajustes.

Esta ventana permite registrar proveedores de impresión de terceros como PrintNode. Aquí puede configurar credenciales, URLs de endpoint y la implementación Java específica que cumple con el contrato de PrintProviderStrategy. Cada organización puede mantener sus propios proveedores de impresión.

![](../../../../assets/developer-guide/etendo-classic/bundles/platform/print-provider/provider-implementation-window-1.png)

Campos a tener en cuenta:

- **Módulo**: indica el módulo donde se exportará la configuración del Proveedor de impresión.
- **Nombre**: nombre descriptivo del proveedor.
- **Implementación Java**: ruta al archivo Java donde se encuentra la implementación del proveedor. Debe cumplir con el contrato establecido, definiendo cómo se muestran las impresoras, cómo se genera la impresión y cómo se envía a la impresora.

- **Resolver ProviderStrategyResolver**: dado un Proveedor (registrado en la ventana [Proveedores de impresión](../../../../user-guide/etendo-classic/optional-features/bundles/platform-extensions/print-provider.md#print-providers)), encuentra su ProvidersImplementation (ventana [Implementación del proveedor](../../../../user-guide/etendo-classic/optional-features/bundles/platform-extensions/print-provider.md#provider-implementation)), carga la clase (implementación Java) y devuelve una instancia de la estrategia.

    **Utilidades PrinterUtils**: ayudas transversales

    - Carga/validación de entidades (requireProvider, requirePrinter, requireTableByName, resolveTemplateLineFor).
    - Parámetros de proceso/JSON (requireParam, requireJSONArray, requirePositiveInt).
    - Parámetros del proveedor (getRequiredParam, providerParamContentCheck).
    - Plantillas Jasper (resolveTemplateFile, loadOrCompileJasperReport).
    - Ayudas de resultado de proceso (fail, warning).

- **Acción**, listas para usar

    - UpdatePrinters: sincroniza el catálogo de impresoras del proveedor (añadir/actualizar/deshabilitar).
    - SendGeneratedLabelToPrinter: genera la etiqueta (Jasper) y la envía a la impresora seleccionada.

- **Modelo de datos clave**

    - Provider: configuración del proveedor de impresión (vincula implementación, parámetros e impresoras).
    - ProvidersImplementation: define la clase Java (FQN) de la estrategia/SPI que utilizará el proveedor.
    - ProviderParam: parámetros clave/valor del proveedor (p. ej., apikey, printersurl, printjoburl).
    - Printer: impresora registrada localmente para un proveedor (ID externo, nombre, “predeterminada”, activa).
    - Template: cabecera de plantilla asociada a una tabla; agrupa sus líneas.
    - TemplateLine: variante de plantilla (ruta .jrxml/.jasper, “predeterminada”, orden/lineNo).

## Cómo crear un nuevo proveedor

1. **Crear la clase de estrategia**: cree una clase en el módulo que extienda `PrintProviderStrategy`. 


    ``` title=" MyProviderStrategy.java - Skeleton Example"
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

    **Convenciones contractuales**

    - Printer.value almacena el ID externo de la impresora (clave para el “upsert”).
    - Lance PrintProviderException (extiende OBException) para fallos funcionales/de integración.
    - No registre secretos (claves API); registre el contexto (statusCode, cuerpos truncados).

2. **Registrar la implementación**

    - **AD: Implementación del proveedor**

        - Implementación Java: com.mi.modulo.print.MyProviderStrategy

    - **AD: Proveedor de impresión**

        - Referencia a la implementación anterior.

    - **AD: Parámetro del proveedor**

        - Defina las claves (reutilice si aplica): printersurl, printjoburl, apikey, etc.
        - Guarde los valores (p. ej., sus URLs de API).

## Cómo registrar etiquetas (Jasper)

1. Cree un nuevo registro en la ventana **Plantillas de impresión**, indicando la tabla a la que aplica.

2. Indique la ubicación de su plantilla en la pestaña de líneas. `TemplateLine.templateLocation` acepta:

    - @basedesign@/...
    - @<módulo>@/...
    - Rutas relacionadas con basedesign

**Detalles técnicos**

- La prioridad aplica a la marca “Predeterminada”; en caso contrario, obtendrá la de menor número de secuencia.
- `PrinterUtils.resolveTemplateFile` resuelve ubicaciones en `src-loc/design` y web.
- `PrinterUtils.loadOrCompileJasperReport` soporta `.jrxml` (compilar) y `.jasper` (cargar).

!!! note "Parámetros recomendados"
    - DOCUMENT_ID = recordId
    - SUBREPORT_DIR = directorio de la plantilla (para subinformes)

## Inyección de parámetros personalizados con hooks

El módulo Proveedor de impresión soporta un mecanismo de hooks que permite a módulos externos inyectar parámetros personalizados de JasperReports durante la generación de etiquetas. Esta capacidad habilita escenarios avanzados de personalización en los que la lógica de negocio necesita añadir o modificar parámetros del informe antes de que el informe se renderice.

### Interfaz de hook

Los módulos pueden implementar la interfaz `GenerateLabelHook` para personalizar parámetros de JasperReports. La ejecución del hook ocurre durante la fase `generateLabel`, antes de que el informe se rellene con datos.

**Características clave:**

- **Ejecución específica por tabla**: cada hook declara a qué tablas aplica mediante `tablesToWhichItApplies()`.
- **Ordenación basada en prioridad**: los hooks se ejecutan en orden de prioridad (valores más bajos primero), permitiendo controlar la secuencia de ejecución.
- **Acceso completo al contexto**: los hooks reciben un objeto `GenerateLabelContext` que proporciona acceso a la configuración del proveedor, metadatos de la tabla, ID del registro, información de la plantilla y el mapa de parámetros.
- **Integración CDI**: los hooks se descubren y gestionan automáticamente mediante CDI.

### Implementación de un hook

Para crear un hook personalizado:

1. **Crear una clase** que implemente `GenerateLabelHook`
2. **Anotar** con `@Dependent` para el descubrimiento por CDI
3. **Implementar los métodos requeridos**:
   - `execute(GenerateLabelContext context)`: lógica principal para añadir/modificar parámetros
   - `tablesToWhichItApplies()`: devuelve la lista de IDs de tabla donde aplica este hook
   - `getPriority()` (opcional): devuelve la prioridad de ejecución (por defecto: 100)

### Ejemplo: generación de códigos de barras personalizados

El siguiente ejemplo demuestra un hook que genera etiquetas de códigos de barras personalizadas para documentos de negocio. Este hook reemplaza la consulta por defecto a base de datos por una fuente de datos personalizada que contiene información de códigos de barras calculada.

```java title="CustomDocumentLabelHook.java"
package com.etendoerp.examples.hooks;

import java.util.ArrayList;
import java.util.List;
import javax.enterprise.context.Dependent;

import com.etendoerp.print.provider.api.GenerateLabelHook;
import com.etendoerp.print.provider.api.PrintProviderException;
import com.etendoerp.print.provider.dto.BarcodeLabelDTO;
import net.sf.jasperreports.engine.data.JRBeanCollectionDataSource;

/**
 * Hook that adds custom parameters for document label generation.
 * Generates barcode data and provides it as a custom data source.
 */
@Dependent
public class CustomDocumentLabelHook implements GenerateLabelHook {

  private static final List<String> TABLES_TO_WHICH_IT_APPLIES = List.of(
      "YOUR_DOCUMENT_TABLE_ID",      // Document header table ID
      "YOUR_DOCUMENT_LINE_TABLE_ID"  // Document line table ID
  );

  @Override
  public void execute(GenerateLabelContext context) throws PrintProviderException {
    try {
      final String recordId = context.getRecordId();

      // Retrieve the document record
      BaseOBObject currentRecord = getDocumentRecord(recordId);

      if (currentRecord == null) {
        throw new PrintProviderException("Document not found: " + recordId);
      }

      // Resolve the lines to process
      List<DocumentLine> lines = resolveDocumentLines(currentRecord);

      // Generate barcode data for each line
      List<BarcodeLabelDTO> barcodeData = generateBarcodeData(lines);

      // Create a JRBeanCollectionDataSource with the barcode data
      JRBeanCollectionDataSource dataSource = new JRBeanCollectionDataSource(barcodeData);

      // Add the datasource as a parameter
      // IMPORTANT: This replaces the SQL query in the jasper template
      context.addParameter("REPORT_DATA_SOURCE", dataSource);

    } catch (PrintProviderException e) {
      throw e;
    } catch (Exception e) {
      throw new PrintProviderException("Failed to add barcode parameters: " + e.getMessage(), e);
    }
  }

  protected List<BarcodeLabelDTO> generateBarcodeData(List<DocumentLine> lines) {
    List<BarcodeLabelDTO> result = new ArrayList<>();

    for (DocumentLine line : lines) {
      // Build barcode based on business rules (product info, quantities, etc.)
      String barcode = buildBarcodeForLine(line);
      String barcodeWithSeparator = buildBarcodeWithSeparator(line);

      result.add(new BarcodeLabelDTO(barcode, barcodeWithSeparator));
    }

    return result;
  }

  @Override
  public int getPriority() {
    return 50;  // Medium priority
  }

  @Override
  public List<String> tablesToWhichItApplies() {
    return TABLES_TO_WHICH_IT_APPLIES;
  }
}
```

### API de contexto del hook

`GenerateLabelContext` proporciona los siguientes métodos:

| Method                                   | Description                                |
| ---------------------------------------- | ------------------------------------------ |
| `addParameter(String key, Object value)` | Añade o actualiza un parámetro de JasperReports  |
| `getParameter(String key)`               | Recupera el valor actual de un parámetro |
| `getParameters()`                        | Devuelve una vista de solo lectura de todos los parámetros |
| `getProvider()`                          | Obtiene la configuración del proveedor            |
| `getTable()`                             | Obtiene los metadatos de la tabla objetivo             |
| `getRecordId()`                          | Obtiene el ID del registro que se está imprimiendo           |
| `getTemplateLine()`                      | Obtiene la referencia de la línea de plantilla           |
| `getJsonParameters()`                    | Obtiene los parámetros JSON de la solicitud  |

### Fuentes de datos personalizadas

Los hooks pueden proporcionar fuentes de datos personalizadas estableciendo el parámetro `REPORT_DATA_SOURCE`. Cuando este parámetro está presente, el Proveedor de impresión lo utilizará en lugar de la conexión por defecto a base de datos:

```java
// Create a custom data source from a collection
List<MyDataDTO> data = prepareCustomData();
JRBeanCollectionDataSource dataSource = new JRBeanCollectionDataSource(data);

// Set it as the data source
context.addParameter("REPORT_DATA_SOURCE", dataSource);
```

Esto es especialmente útil cuando:

- Los datos necesitan transformaciones complejas antes del renderizado
- Los datos provienen de múltiples fuentes (base de datos + APIs externas)
- La lógica de negocio requiere campos calculados que no están presentes en la base de datos
- La optimización de rendimiento requiere datos preagregados

### Buenas prácticas

1. **Gestión de errores**: envuelva siempre la lógica de negocio en bloques try-catch y lance `PrintProviderException` con mensajes significativos.

2. **Seguridad ante nulos**: valide que los objetos requeridos estén presentes antes de acceder a ellos:

   ```java
   if (context.getTable() == null) {
       throw new PrintProviderException("Table information is required");
   }
   ```

3. **Coordinación de prioridades recomendada**: use valores de prioridad para controlar el orden de ejecución cuando múltiples hooks aplican a la misma tabla:

   - Hooks del sistema/core: 1-30
   - Hooks estándar de negocio: 31-70
   - Hooks personalizados/de extensión: 71-100

4. **Registro (logging)**: use logging SLF4J para ayudar en la resolución de incidencias:

   ```java
   private static final Logger log = LoggerFactory.getLogger(MyHook.class);

   log.debug("Executing hook for record: {}", recordId);
   ```

5. **Rendimiento**: mantenga la ejecución del hook ligera. Evite consultas pesadas a base de datos o llamadas a APIs externas que puedan ralentizar la generación de etiquetas.

### Actualización de impresoras

- El proceso llama a strategy.fetchPrinters(provider) y realiza un upsert sobre Printer:

    - **Crear** si no existe (provider, value=externalId).
    - **Actualizar** nombre/predeterminada si ya existe.
    - **Desactivar** impresoras del proveedor que no se incluyeron en esta sincronización.

- Printer.value = ID externo; Printer.name es amigable para el usuario; Printer.default marca “predeterminada”.

    !!!note "Recomendación"
        Si la API del proveedor no devuelve un único campo que pueda servir como clave estable, se puede componer una (p. ej.,  < accountId >:< remotePrinterId >).

### Errores

- Use `PrintProviderException` para la gestión de excepciones.
- Registre los mensajes que necesite en AD_MESSAGE. Puede acceder a estos mensajes usando las utilidades de formateo `String.format` y `OBMessageUtils.getI18NMessage`.

## Flujo de trabajo y configuración

!!! Note 
    Recuerde que la configuración inicial debe realizarse solo una vez, como administrador del sistema. Los parámetros del proveedor como printersurl y apikey deben definirse correctamente para evitar fallos de conexión o de sincronización de impresoras.

1. **Configuración** (una sola vez)

    - Como administrador del sistema, cree un registro en Implementación de proveedores indicando la ruta de su clase de estrategia.
    - Como administrador, cree un Proveedor que referencie la implementación definida en el paso anterior.
    - En la pestaña Parámetros del proveedor, defina los parámetros requeridos (URLs, clave API, etc.).

2. **Descubrir impresoras**

    - UpdatePrinters (Acción ejecutada desde la ventana Impresoras): use fetchPrinters de la estrategia y sincronice Printer.

3. **Generar etiqueta**

    - `SendGeneratedLabelToPrinter` (Acción ejecutada desde el botón en la ventana deseada) resuelve TemplateLine desde la tabla asociada con la ventana del botón (p. ej., un botón en la ventana Producto resolverá la tabla M_Product). Esta acción compila/carga Jasper y produce el PDF temporal.

4. **Enviar a la impresora**

    - `sendToPrinter` realiza la llamada HTTP/SDK necesaria y devuelve jobId (cuando esté disponible).

### Ejemplo básico

- En el módulo, cree `com.my.module.print.MyProviderStrategy` (extiende `PrintProviderStrategy`).

- Configuración por ventana
    - Implementación del proveedor:

        - especifique javaImplementation = com.my.module.print.MyProviderStrategy

    - Proveedor de impresión:

        - especifique el proveedor previamente registrado en implementación de proveedores.

    - ProviderParam:

        - printersurl: URL para obtener impresoras.
        - printjoburl: URL para enviar trabajos de impresión.
        - apikey: clave para autenticarse con el middleware.

- Ejecute **Actualizar impresoras** desde la ventana **Impresoras**. La Acción delega la responsabilidad de actualizar impresoras a la implementación de fetchPrinters.

- Ejecute **Generar imprimible** desde el botón que se ha registrado en la ventana deseada. La Acción `SendGeneratedLabelToPrinter` delega la responsabilidad de:

    - Generar la impresión a su implementación de generateLabel.
    - Enviar el trabajo de impresión anterior a su implementación de sendToPrinter.

---
Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L.](https://etendo.software){target="_blank"}.