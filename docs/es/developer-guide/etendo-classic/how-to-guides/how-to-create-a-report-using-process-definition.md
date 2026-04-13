---
tags: 
  - How to
  - Reports
  - Process Definition
  - Menu Entry
---
# Cómo crear un informe usando Definición del Proceso

## Visión general

Esta sección explica cómo añadir un nuevo informe usando una Definición del Proceso y crear una entrada de menú para invocarlo.

!!!info
    Para información de contexto, visite:

    - [Cómo crear una Definición del Proceso estándar](../how-to-guides/how-to-create-a-standard-process-definition.md)
    - [Cómo crear un informe](../how-to-guides/how-to-create-a-report.md).

## Módulo de ejemplo

Esta sección está respaldada por un módulo de ejemplo que incluye el informe simple descrito en este documento. El informe se denomina **Informe simple de productos** y muestra en `PDF` una lista de productos que puede filtrarse por *Categoría del producto*.

El código del módulo de ejemplo puede descargarse desde el repositorio [com.etendoerp.client.application.examples](https://github.com/etendosoftware/com.etendoerp.client.application.examples){target="\_blank"}.

## Definición del informe en Diccionario de la Aplicación

### Definición del Proceso

:material-menu: `Aplicación` > `Diccionario de la Aplicación` > `Definición del Proceso` 

Como rol `Administrador del sistema`, cree un nuevo registro en la ventana **Definición del Proceso**. Campos a tener en cuenta:

- **Patrón de la Interfaz de Usuario**: establezca `Informe (usando plantillas JR)`. Este valor mostrará la solapa Definición Informe.

- **Handler de acción**: si no se establece ninguno cuando se selecciona el Patrón de la Interfaz de Usuario, se establece `org.openbravo.client.application.report.BaseReportActionHandler`.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-report-using-process-definition/1.png)

El `BaseReportActionHandler` es el handler de acción por defecto que se utiliza en los informes. En caso de que desee realizar algunas validaciones Java o incluir parámetros adicionales que no estén definidos en la solapa Parámetros de la Definición del Proceso, es posible utilizar un Handler de acción personalizado que extienda `BaseReportActionHandler`.

### Definición de parámetros

En la solapa **Parámetro** se añaden todos los parámetros necesarios para filtrar los resultados del informe. Sus valores son gestionados por `BaseReportActionHandler` y enviados a Jasper Reports como parámetros. Estos parámetros deben definirse en la plantilla JR con el mismo nombre que el nombre de la columna.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-report-using-process-definition/2.png)

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-report-using-process-definition/3.png)

Cuando el parámetro de filtro es una referencia de Selector, el valor se envía como un **JSONOBject** que incluye 2 claves:

- **value** con el id del `BaseOBObject` seleccionado para usarse en la consulta SQL
- **identifier** con el identificador legible que puede usarse para imprimir en el informe los valores del filtro.

En el caso de Selectores múltiples, el **JSONObject** incluye 4 claves:

- **values** con un `JSONArray` que incluye todos los ids seleccionados.
- **identifiers** con un `JSONArray` que incluye todos los identificadores.
- **strValues** con un String separado por comas con todos los ids seleccionados que puede usarse en una cláusula SQL `IN`.
- **strIdentifiers** con un String separado por comas con todos los identificadores seleccionados.

En la plantilla Jasper, el parámetro debe definirse usando la clase `org.codehaus.jettison.json.JSONObject`. En el ejemplo, se configura un selector múltiple de `Categoría del producto`. Como este parámetro es opcional, el filtro se incluye en la consulta usando un parámetro auxiliar (`AUX_Product_category`).
El parámetro auxiliar tiene una expresión por defecto que devuelve **" 1 = 1 "** cuando no hay ninguna categoría seleccionada y la cláusula where correspondiente cuando se seleccionan algunas categorías:

``` java
("".equals($P{M_Product_Category_ID}.getString("strValues"))) ? " 1 = 1 " : " pc.m_product_category_id IN ("+$P{M_Product_Category_ID}.getString("strValues")+")"
```

Este parámetro se incluye entonces en la consulta usando la notación `$P!{}` para reemplazarlo por el valor del parámetro en lugar de usar parámetros SQL.

```sql
FROM m_product p
    JOIN m_product_category pc ON p.m_product_category_id = pc.m_product_category_id
WHERE $P!{AUX_Product_category}
    AND p.ad_client_id = $P{Current_Client_ID}
```

Los identificadores pueden mostrarse en un Campo de texto con la siguiente expresión:

``` java 
$P{M_Product_Category_ID}.getString("strIdentifiers")
```

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-report-using-process-definition/4.png)

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-report-using-process-definition/5.png)


El `BaseReportActionHandler` y la clase `ReportingUtils` utilizada para generar el informe incluyen algunos parámetros adicionales que pueden usarse en la plantilla:

- **SUBREPORT_DIR**: la ruta donde se encuentra la plantilla principal. Útil para establecer las rutas de los subinformes.
- **jasper_process**: un objeto `org.openbravo.client.application.Process` con la Definición del Proceso del informe.
- **jasper_hbSession**: un objeto `org.hibernate.Session` con la sesión actual de Hibernate.
- **jasper_obContext**: un `org.openbravo.dal.core.OBContext` con el OBContext que ha lanzado el informe.
- **AMOUNTFORMAT**: un objeto `java.text.DecimalFormat` con el formato que se utilizará en importes.
- **QUANTITYFORMAT**: un objeto `java.text.DecimalFormat` con el formato que se utilizará en cantidades.
- **REPORT_FORMAT_FACTORY**: parámetro base de JR con el formato de fecha.
- **Current_Client_ID**: `String` con el `AD_Client_ID` actual. Útil para filtrar el SQL del informe.
- **Readable_Organizations**: `String` separado por comas con las organizaciones legibles del Usuario/Rol que ejecuta el informe. Útil para filtrar el `SQL` del informe.

Dependiendo de la salida del informe, se establecen algunos parámetros adicionales:

- Salida **PDF**:

    - **IS_IGNORE_PAGINATION**: con valor **false** para asegurar que el informe se divida en diferentes páginas.

- Salida **XLS**:

    - **IS_IGNORE_PAGINATION**: con valor **true** para asegurar que el informe no se divida en diferentes páginas y que todos los resultados se muestren en la misma hoja.

- En caso de que se desee añadir más parámetros que no puedan definirse como **Parámetros** de la **Definición del Proceso**, es posible usar un **Handler** personalizado que extienda `BaseReportActionHandler` y sobrescriba el método `addAdditionalParameters`.
    Es posible comprobar todos los parámetros y valores enviados al motor de Jasper Report habilitando el **nivel de log DEBUG** en la clase `org.openbravo.client.application.report.ReportingUtils` modificando `log4j2-web.xml` y, para versiones antiguas, el archivo `log4j.lcf`:

    ``` txt
    DEBUG org.openbravo.client.application.report.ReportingUtils - list of parameters available in the jasper report
    DEBUG org.openbravo.client.application.report.ReportingUtils - parameter name: SUBREPORT_DIR value: /home/gorkaion/src/openbravo/pi-reporting-merge/WebContent/web/org.openbravo.platform.features/jasper/
    DEBUG org.openbravo.client.application.report.ReportingUtils - parameter name: Current_Client_ID value: 23C59575B9CF467C9620760EB255B389
    DEBUG org.openbravo.client.application.report.ReportingUtils - parameter name: REPORT_FORMAT_FACTORY value: org.openbravo.erpCommon.utility.JRFormatFactory@14ffa3fc
    DEBUG org.openbravo.client.application.report.ReportingUtils - parameter name: REPORT_VIRTUALIZER value: net.sf.jasperreports.engine.fill.JRSwapFileVirtualizer@1b670029
    DEBUG org.openbravo.client.application.report.ReportingUtils - parameter name: jasper_process value: OBUIAPP_Process(70889433974B409BAC4F9D7BFB211248) (name: Product Simple Report)
    DEBUG org.openbravo.client.application.report.ReportingUtils - parameter name: M_Product_Category_ID value: {"values":["291B401A38354A2C8247DFF0DFBDF4AE","5525FCABFE9545018EE221E8802AA283"],"identifiers":["Bio","Fruit juice"],"strValues":"'291B401A38354A2C8247DFF0DFBDF4AE', '5525FCABFE9545018EE221E8802AA283'","strIdentifiers":"Bio, Fruit juice"}
    DEBUG org.openbravo.client.application.report.ReportingUtils - parameter name: AMOUNTFORMAT value: java.text.DecimalFormat@674dc
    DEBUG org.openbravo.client.application.report.ReportingUtils - parameter name: QUANTITYFORMAT value: java.text.DecimalFormat@674dc
    DEBUG org.openbravo.client.application.report.ReportingUtils - parameter name: Readable_Organizations value: 'E443A31992CB4635AFCAEABE7183CE85','0','DC206C91AA6A4897B44DA897936E0EC3','7BABA5FF80494CAFA54DEBD22EC46F01','BAE22373FEBE4CCCA24517E23F0C8A48','19404EAD144C49A0AF37D54377CF452D','B843C30461EA4501935CB1D125C9C25A','2E60544D37534C0B89E765FE29BC0B43'
    DEBUG org.openbravo.client.application.report.ReportingUtils - parameter name: jasper_obContext value: org.openbravo.dal.core.OBContext@73b91cd
    DEBUG org.openbravo.client.application.report.ReportingUtils - parameter name: jasper_hbSession value: SessionImpl(PersistenceContext[entityKeys=...
    DEBUG org.openbravo.client.application.report.ReportingUtils - parameter name: IS_IGNORE_PAGINATION value: false
    ```

### Parámetros de lista de botones

Cuando se añade un parámetro de lista de botones, los botones se añaden junto con los botones predefinidos de este tipo de proceso (**Vista**, **Exportar a PDF**, **Exportar a Excel**). Este comportamiento permite añadir lógica adicional al comportamiento estándar de estos procesos, ya que es posible extender el comportamiento base desde la implementación Java del proceso.

A continuación se muestra un ejemplo de una lista de botones que añade dos botones (Botón 1, Botón 2) a este tipo de proceso:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-report-using-process-definition/6.png)

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-report-using-process-definition/7.png)

Para añadir lógica de ejecución a estos botones, debe redefinirse el método `handleCustomAction` dentro de la clase Java del proceso:

```java
  @Override
  protected void handleCustomAction(JSONObject result, Map<String, Object> parameters,
      JSONObject jsonContent, String action) throws JSONException {
    switch (action) {
      case "B1":
        result.put("message", new JSONObject()
            .put("severity", "success")
            .put("text", "Button B1 has been pressed."));
        break;
      case "B2":
        result.put("message", new JSONObject()
            .put("severity", "success")
            .put("text", "Button B2 has been pressed."));
        break;
      default:
        super.handleCustomAction(result, parameters, jsonContent, action);
    }
  }
```

!!! note
    El parámetro action tendrá la información correspondiente a la clave de búsqueda del botón pulsado; los identificadores son obligatorios y se definen junto con el botón en la solapa de referencia de la lista dentro de la referencia.

Una vez realizada la configuración, es necesario compilar.

```bash title="Terminal"
./gradlew smartbuild
```

Después, cuando entre en el proceso, verá sus botones personalizados junto a los botones predefinidos del informe.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-report-using-process-definition/8.png)

Después, cuando pulse los botones, se ejecutará su lógica personalizada.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-report-using-process-definition/9.png)

### Definición de la fuente de datos del informe

Existen dos formas de definir los datos que se mostrarán en el informe:

1. Definir una **consulta** en la plantilla `jrxml`.
2. Proporcionar una **fuente de datos** a la plantilla `jrxml`.

En el caso del segundo enfoque, es necesario usar un **Handler** personalizado que extienda `BaseReportActionHandler` y sobrescriba el método `getReportData`. Este método recibe como argumento un mapa de parámetros que contiene:

- Los parámetros de la `HTTP request`.
- Los parámetros disponibles dentro del Jasper Report. Están disponibles a través de otro mapa al que se puede acceder usando la clave _JASPER_REPORT_PARAMETERS_.

``` java
protected JRDataSource getReportData(Map<String, Object> parameters) {
// Retrieve the report id (HTTP request parameter)
String reportId = (String) parameters.get("reportId");
// retrieve the map of JR Parameters
Map<String, Object> jrParameters = (Map<String, Object>) parameters
.get(JASPER_REPORT_PARAMETERS);
// Here goes the logic to generate the JRDataSource
...
}
```

Esto permite generar los datos del informe de forma dinámica, es decir, en base a algún tipo de lógica construida con el valor de cualquiera de estos parámetros.

### Gestión de mensajes

Es posible mostrar mensajes (`success`, `warning`, etc.) al usuario después de ejecutar un informe basado en una Definición del Proceso.

Esto es útil cuando el informe se genera correctamente, pero el sistema aún necesita informar al usuario sobre posibles incidencias en los datos; por ejemplo, cuando algunos productos tienen transacciones sin coste calculado.

Para habilitar esta funcionalidad, sobrescriba el método `addAdditionalParameters` en su clase Java personalizada que extienda `BaseReportActionHandler`. En este método, puede añadir una nueva entrada al mapa `parameters` con la clave `"message"` y un valor de tipo `OBError`. Por ejemplo:

``` java
OBError msg = new OBError();
msg.setType("Warning");
msg.setMessage("Please review the report for incomplete data.");
parameters.put("message", msg);
```

Este mensaje será capturado automáticamente por BaseReportActionHandler y se mostrará en la UI una vez finalice el informe.

Si no se proporciona el parámetro **message**, el sistema mostrará un mensaje de éxito por defecto:

!!! Success
    Informe generado correctamente.

### Compilación de subinformes en tiempo de ejecución

En caso de que nuestro informe de definición del proceso contenga subinformes, la infraestructura permite compilar los subinformes en tiempo de ejecución. Para ello, deben cumplirse las siguientes condiciones:

1. El nombre del parámetro para el subinforme en el informe principal sigue este patrón: `SUBREP_name_of_the_sub_report_file`.
2. Los subinformes (archivos `JRXML`) se colocan en la misma carpeta que el informe principal.

### Definición Informe

En la solapa **Definición Informe** se definen las plantillas JR del informe. Cada Definición del Proceso solo puede tener una definición de informe. También es necesario definir al menos una plantilla: `HTML`, `PDF` o `Excel`.

- Si las salidas `PDF` y `Excel` comparten la misma plantilla, es posible establecer la plantilla `PDF` y marcar el indicador **Usar PDF como plantilla Excel**.
- Si las salidas `PDF` y `HTML` comparten la misma plantilla, es posible establecer la plantilla `PDF` y marcar el indicador **Usar PDF como plantilla HTML**.
- Si las salidas `HTML`, `PDF` y `Excel` comparten la misma plantilla, entonces debe establecerse la plantilla `PDF` y deben marcarse ambos indicadores.

Las plantillas deben almacenarse en la carpeta **Web**.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-report-using-process-definition/10.png)

### Añadir hipervínculos a un informe

Puede añadir hipervínculos a elementos del informe para permitir la navegación a otro registro, abrir un informe diferente o ejecutar lógica personalizada según sea necesario.

Para ello, seleccione el componente sobre el que desea hacer clic (p. ej., **Campo de texto**, **Imagen**, **Gráfico** o **Subinforme**) y configure sus propiedades de hipervínculo:

- **Destino del enlace**: `"Self"` — abre el enlace en la misma ventana del navegador.
- **Tipo de enlace**: `"Reference"` — indica que se trata de un enlace URL.
- **Expresión de referencia del hipervínculo**: esta es la expresión o URL que se ejecutará al hacer clic.
- **Expresión cuando del hipervínculo**: (Opcional) una expresión booleana para controlar cuándo debe estar activo el hipervínculo.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-report-using-process-definition/11.png)

#### Ejemplo 1: Navegar a un registro específico (p. ej., una factura)

Para abrir una ventana y un registro específicos en el sistema (p. ej., una ventana de Factura con un ID de factura determinado), utilice una expresión como esta en la **Expresión de referencia del hipervínculo**:

```java
"javascript:top.OB.Utilities.openDirectTab('" + $V{OPEN_INVOICE_TAB} + "', '" + $F{C_INVOICE_ID} + "')"
```

Donde:

- `$V{OPEN_INVOICE_TAB}` es el ID de la ventana de la ventana de Factura de venta.
- `$F{InvoiceID}` es el campo que contiene el ID de la factura que desea abrir.

También puede añadir una Expresión cuando del hipervínculo para asegurarse de que el enlace solo sea clicable cuando el informe se esté visualizando en formato `HTML`, o añadir cualquier otra condición según sea necesario.

``` java
$P{OUTPUT_FORMAT}.equalsIgnoreCase("HTML")? Boolean.TRUE: Boolean.FALSE
```

Donde:

- `$P{OUTPUT_FORMAT}` es el formato de salida del informe.

#### Ejemplo 2: Abrir otro informe desde un enlace

También puede usar un hipervínculo para disparar la generación de otro informe. En este caso, en lugar de una URL simple, la Expresión de referencia del hipervínculo debe contener una llamada javascript: a `OB.RemoteCallManager.call(...)`, pasando todos los parámetros requeridos para el informe:

``` javascript
"javascript:top.OB.RemoteCallManager.call('your.custom.ReportActionHandler',"
  + "{"
  + "  _buttonValue: 'HTML',"
  + "  _params: {"
  + "    // Add here all the necessary input parameters"
  + "    Param1: '" + $P{Param1} + "',"
  + "    Param2: '" + $F{FieldFromDataSet} + "',"
  + "    DateParam: '" + $P{DateValue} + "'"
  + "  }"
  + "},"
  + "{"
  + "  processId: '" + $P{processId} + "',"
  + "  reportId: '" + $P{reportId} + "',"
  + "  windowId: null"
  + "},"
  + "function(rpcResponse, data, rpcRequest) {"
  + "  top.OB.Utilities.Action.executeJSON(data.responseActions, null, null, null);"
  + "}"
  + ");"
```

Este fragmento de `JavaScript` realiza una llamada remota al handler del proceso del informe, pasando todos los parámetros que necesita. El informe se generará y se abrirá como resultado de esta acción. Puede personalizar completamente esta lógica para adaptarla a sus necesidades de navegación o integración.

## Resultado

El resultado se muestra en un nuevo formulario con todos los parámetros y el/los botón(es) correspondiente(s) de *Exportar*.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-report-using-process-definition/12.png)

Una vez ejecutado el informe, el resultado se muestra según la acción seleccionada:

- **Vista** abre el informe en una nueva ventana.
- **Exportar a PDF** descarga el informe como un archivo PDF.
- **Exportar a Excel** descarga el informe como un archivo Excel.

El formulario permanece habilitado, lo que permite ejecutar el informe de nuevo con diferentes parámetros.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-report-using-process-definition/13.png)

---

Este trabajo es una obra derivada de [Cómo crear un informe usando Definición del Proceso](http://wiki.openbravo.com/wiki/How_to_create_a_Report_using_Process_Definition){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.