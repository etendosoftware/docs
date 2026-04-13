---
title: Rango impuesto
tags:
    - Impuesto
    - Índice
    - Gestión Financiera
    - Configuración
    - Contabilidad
---

# Rango impuesto

:material-menu: `Aplicación` > `Gestión Financiera` > `Contabilidad` > `Configuración` > `Rango impuesto`

## Visión general

Cada rango impuesto en Etendo es una combinación de diferentes variables como la categoría de impuesto, el índice y la categoría de impuestos de terceros, entre otras. Si todas esas variables están correctamente configuradas, el rango impuesto correcto se completa automáticamente en cada transacción empresarial.

Es posible crear *Rango impuesto* que son una *Combinación* de más de un rango impuesto. Ese escenario puede aplicarse a un tercero que está sujeto a IVA e Impuesto sobre la Renta al mismo tiempo mientras alquila una oficina a un tercero fuera de sus actividades empresariales "normales".

### Aplicación de impuestos

Los impuestos se aplican a pedidos y facturas. En este proceso, hay dos pasos: asociar el impuesto deseado a la línea y procesar el documento que aplicará el impuesto y calculará el importe real.

### Obtención del impuesto por defecto

Cuando en una línea de documento (pedido o factura) se selecciona un producto, se asocia un impuesto por defecto a esta línea. Tenga en cuenta que podemos seleccionar el impuesto que queramos para esta línea. La selección del impuesto por defecto se realiza mediante el procedimiento almacenado de BD C\_GetTax. Las reglas seguidas por este procedimiento son las siguientes:

Para transacciones de venta con un proyecto asociado, si un proyecto tiene un rango impuesto, se toma este rango impuesto. Esto funciona cuando un pedido es generado por un Proyecto (Pedido). En este caso, el impuesto se toma directamente del impuesto de la línea del proyecto. Para transacciones de venta, si un tercero está marcado como exento de impuestos, el impuesto seleccionado será el que esté marcado como exento con la fecha más reciente relativa a la fecha del pedido o de la factura.

En caso contrario, el impuesto se selecciona de entre los definidos en la misma categoría de impuesto que el producto en la línea. Los impuestos con categoría de impuestos de terceros definida solo pueden aplicarse a aquellos terceros con la misma categoría de impuesto (para proveedor o cliente). Si el impuesto no tiene una categoría de impuestos de terceros, puede aplicarse a cualquier tercero (con o sin una categoría de impuesto asociada). Si un impuesto con categoría de impuestos de terceros y otro sin ella pueden aplicarse ambos, se seleccionará el que tenga categoría de impuestos de terceros. Además, se tienen en cuenta las ubicaciones “hasta” y “desde”. En primer lugar, se seleccionan aquellos impuestos definidos para regiones más cercanas (si un impuesto es para región y otro para país, se seleccionará el de región). Esta información se asocia al rango impuesto, a través de la solapa “Zona de Impuesto”. Los impuestos se aplican teniendo en cuenta si están definidos como Ventas, Compra o Ambos.

Aparte de estas reglas, y solo en el caso de Pedidos y Facturas de Compra/Venta, el sistema filtra los rangos impuesto teniendo en cuenta también el indicador IVA de caja definido en la cabecera del documento, que se establece automáticamente en función de la configuración de la organización y del tercero para documentos de venta y compra respectivamente (aunque puede sobrescribirse manualmente después). Así, en caso de que el documento esté habilitado para el régimen de IVA de caja, el sistema obtendrá un rango impuesto de IVA de caja y viceversa.

Una vez seleccionado el impuesto (el por defecto, u otro seleccionado por el usuario), se calcula un importe aproximado mediante los callouts SL\_Order\_Tax o SL\_Invoice\_Tax. Si el impuesto está marcado como nivel de agrupación, el cálculo se realizará usando el índice definido en el impuesto padre, sin desglosarlo ni tomar los valores reales de sus hijos. Además, en este punto se rellenan las tablas c\_order\_tax y c\_invoice\_tax con los impuestos. El importe real se calcula cuando se procesa el documento.

Al crear una nueva factura, es posible introducir impuestos manualmente y marcarlos como “no recalcular”. En este caso, el impuesto se aplica con el importe introducido en la solapa Impuesto de la factura, por lo que no se realizará ningún recálculo al procesar la factura. Cuando un impuesto en una factura está marcado como recalculado, si el impuesto se edita manualmente, todos los cambios se perderán al procesar la factura. Esto se debe a que el importe de impuestos de la factura se recalcula. Los impuestos “no recalcular” no están asociados a ninguna línea de factura, mientras que los recalculados sí lo están. Por tanto, cuando un impuesto proviene de una línea, se marcará como recalcular. Si se crea manualmente, no se marcará, y este valor no será actualizable.

No recalcular impuestos es útil para facturas que incluyen líneas de impuesto sin un producto. Por ejemplo, puede utilizarse para productos importados: estos productos suelen tener una factura exenta de impuestos y otra factura creada por el agente de aduanas sin ningún producto, pero con un importe de impuestos para los productos importados.

### Cálculo del importe real

Cuando se procesan estos documentos (c\_order\_post y c\_invoice\_post), los impuestos e importes reales se calculan a partir de los impuestos seleccionados (salvo que estén definidos como “no recalcular” para facturas) siguiendo estos pasos:

Se elimina cada impuesto de las tablas C\_OrderTax o C\_InvoiceTax. Esto se hace porque los impuestos en estas tablas antes del proceso del documento son solo informativos y pueden ser inexactos.

Se crea una nueva línea en las tablas C\_OrderTax o C\_InvoiceTax para cada impuesto diferente aplicado a las líneas del documento (cada línea tendrá solo un impuesto). El importe pagado al impuesto se calcula a partir de la base imponible de las líneas que están asociadas a este impuesto.

Para impuestos definidos como nivel de agrupación, se inserta una nueva línea por cada uno de sus hijos y el importe se calcula teniendo en cuenta si los hijos son en cascada o no.

### Impuesto

La ventana Rango impuesto permite al usuario crear tantos rangos impuesto como sean necesarios.

![](../../../../../../assets/drive/1CNDReMFRW2DoxDedviRdGoWwXmcDGTAp.png)

Los campos a completar para configurar correctamente un rango impuesto son:

-   **"Válido desde"**, que es la fecha a partir de la cual un rango impuesto pasa a ser válido.  
    Por ejemplo, un rango impuesto existente incrementa su índice; en este caso:
    -   se recomienda crear un nuevo rango impuesto configurado con los nuevos requisitos, en lugar de cambiar el rango impuesto original, que puede seguir en uso si fuese necesario.  
        De ese modo, habrá dos rangos impuesto que son exactamente iguales para una organización determinada, pero con distinto índice (%) y distinta fecha válido desde.
-   **"Categoría de Impuesto"**, ya que cada rango impuesto debe estar vinculado a una categoría de impuesto determinada como forma de agrupar rangos impuesto similares.
-   **"Índice"**, que es el % o índice del impuesto.
-   **"Tipo venta/compra"** como forma de distinguir entre impuestos de venta y de compra.  
    El tipo de impuesto es otra variable que Etendo tiene en cuenta al recuperar el rango impuesto correcto tanto en transacciones de venta como de compra. También es una variable muy valiosa a tener en cuenta al informar sobre impuestos, ya que hay informes fiscales que requieren presentar la información de impuestos de compra y de venta por separado.  
    Existe una opción adicional que es "Ambos"; esta opción permite usar el mismo rango impuesto tanto para transacciones de compra como de venta.
-   **"País/Región"** y **"País/Región de destino"**.  
    Impuestos como el *IVA* y el *Impuesto sobre ventas de EE. UU.* tienen en cuenta desde dónde/hacia dónde se realiza una transacción para determinar si está sujeta al impuesto o no.  
    Estos dos campos permiten al usuario introducir esa información teniendo en cuenta si el impuesto es de tipo "Compra" o "Ventas"; por lo tanto, al emitir una factura de venta desde F&B US Inc (País USA y Región Nueva York) a un cliente también ubicado en País de destino USA y Región de destino Nueva York, solo se aplicarían los rangos impuesto de ventas creados dentro de esa Zona de Impuesto especificada.
-   **"Nivel agrupación"**, un rango impuesto puede definirse como de agrupación, lo que significa que tendrá algunos rangos impuesto por debajo.  
    Los rangos impuesto de agrupación también se establecen como "*Impuesto padre*", por lo que sus rangos impuesto hijos pueden vincularse a él.  
    Por ejemplo, se emite una factura de venta a un tercero bajo un régimen de IVA específico que incluye un rango impuesto adicional además del tipo de IVA.  
    Para este escenario, es necesario crear tres rangos impuesto: el padre como de agrupación y dos más para el tipo de IVA y para el otro tipo, ambos vinculados al padre.  
    *"Es importante remarcar que al emitir la factura de venta para ese tercero, **el rango impuesto mostrado/seleccionado es el de agrupación** o el padre."*
-   **"Base Imponible"**, que es la base imponible a tener en cuenta en el cálculo del importe de impuestos. Las opciones disponibles son:
    -   Imp. línea
    -   Imp. línea + Impuestos
    -   Base imponible alternativa
    -   Base imponible alternativa + Impuestos
-   **"Cálculo del importe de impuestos del documento"** que es la forma en que se va a calcular el importe de impuestos por cada rango impuesto (o %). Las opciones disponibles son:
    -   "Importe basado en documento por índice"; esta opción implica que el importe de impuestos se va a calcular como importe de impuestos = (suma de bases imponibles al mismo índice \* índice del impuesto)
    -   "Importe base de línea por índice"; esta opción implica que el importe de impuestos se va a calcular por línea como importe de impuestos = (base imponible línea 1 \* índice del impuesto) + (base imponible línea 2 \* índice del impuesto) + ....+ (base imponible línea n + índice del impuesto).

En la sección "Más información" también hay algunos campos relevantes:

-   **"Impuesto padre"**, los rangos impuesto que pertenecen a un rango impuesto de agrupación deben vincularse a él en este campo para que el árbol de rangos impuesto esté correctamente estructurado.
-   **"Categoría de Impuestos de Terceros"**, un rango impuesto puede vincularse a una categoría de impuestos de terceros específica; por lo tanto, solo se aplicará a los terceros que pertenezcan a esa categoría.
-   **"Retención"**, un rango impuesto puede configurarse como "Retención", por lo que se gestiona correctamente como un tipo de impuesto separado en los informes fiscales.
    -   Los rangos impuesto de retención son rangos impuesto "*Negativo*".
-   **Exento de impuestos**. Un rango impuesto puede configurarse como exento; por lo tanto, es el que se muestra automáticamente en las líneas de pedido/factura creadas para un Cliente configurado también como exento de impuestos.
-   **IVA de caja**. Este tipo de rangos impuesto se utiliza para soportar el régimen de IVA de caja, que permite a las empresas liquidar el importe de IVA cuando han cobrado/pagado las facturas en lugar de en la creación de la factura. Al usar rangos impuesto de IVA de caja, las cuentas Impuesto repercutido transitorio e Impuesto soportado transitorio deben declararse en la solapa Contabilidad.
-   Los rangos impuesto también pueden configurarse como **"No está sujeto a impuestos"**. Un rango impuesto no sujeto a impuestos puede vincularse a transacciones sujetas a impuestos que pasan a no estar sujetas a impuestos bajo una situación determinada. Hay informes fiscales que requieren información sobre ambos tipos de impuestos: exentos y no sujetos a impuestos.
-   Rangos impuesto específicos pueden configurarse como **"Deducible"** (para aquellas Organizaciones para las que NO se permite la deducción de impuestos).
-   Rangos impuesto específicos pueden configurarse como **"No deducible"** (para aquellas Organizaciones para las que se permite la deducción de impuestos).

La forma en que se comportan los rangos impuesto Deducible y No deducible en términos contables se explica a continuación:

-   Factura de compra que incluye un importe de impuestos 100% deducible.  
    El importe de IVA debe contabilizarse en el libro mayor en una cuenta de Impuesto reclamado; por lo tanto, el asiento de la factura de compra es:

|     |     |     |     |
| --- | --- | --- | --- |
| Cuenta | Débito | Crédito contabilizado | Comentarios |
| Gastos del producto | Imp. línea |     | Uno por línea de factura |
| Impuesto reclamado | Impuestos |     | Uno por línea de impuesto |
| Pasivo del proveedor |     | Importe total | Uno por factura |

## Factura de compra que incluye un importe de impuestos NO deducible

El importe de IVA no puede contabilizarse en el libro mayor en una cuenta de Impuesto reclamado, ya que significa un gasto; por lo tanto, el asiento de la factura de compra es:

|     |     |     |     |
| --- | --- | --- | --- |
| Cuenta | Débito | Crédito contabilizado | Comentarios |
| Gastos del producto | Imp. línea + Impuestos |     | Uno por línea de factura y rango impuesto |
| Pasivo del proveedor |     | Importe total | Uno por factura |

!!! info
    Para poder utilizar la funcionalidad descrita a continuación, debe estar instalado el Financial Extensions Bundle. Para ello, siga las instrucciones en el marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).   

El mismo comportamiento puede aplicarse para el impuesto no deducible. 

Por defecto, el importe contable que se genera en las facturas de proveedor cuando se utiliza un rango impuesto no deducible se asigna a la cuenta contable de gastos configurada en la solapa "Contabilidad" del producto. Con esta mejora, el importe de ese impuesto no deducible puede asignarse a una cuenta específica, la configurada en la contabilidad del propio rango impuesto. Para ello, marque la casilla "Usar la cuenta configurada" ubicada dentro de la solapa "Contabilidad" en la ventana "Rango impuesto". 

![](../../../../../../assets/drive/vgIVffeOmiu30VHVRRMlIlN41BbaPKe2vydojUxBx1boZS64zEcr5NgKw6fh0iMflSP60qpC-gb2f36uFWzzast-6LFJ2mV1IAkboxENkBoWlmzrxsBMSu-sudz9F7X6n-mzSD7Q.png)

Como usuario administrador del sistema, active el campo de plantilla contable en la solapa Tabla activa de la ventana Configuración del libro mayor y, a continuación, establezca la plantilla llamada Factura de compra no deducible. 

![](../../../../../../assets/drive/jd75sTt-TOwSTJGK4Zc0Z89aBGk9emQ2OxMIsQ-90Ku8KewJpoRffN8bIdUft-R37ud1xdrkWuzLEyUUZxY6Lk8Wdz-dfK5HfJsUfP2NPmxKSE274RPJRgLwAXE7I6YbO5GpV6eH.png)

Esta casilla, "Usar la cuenta configurada", solo será visible si previamente se marcó la casilla bajo el encabezado "Impuesto no deducible". El valor por defecto de esta casilla será NO.

![](../../../../../../assets/drive/Nn8EaIsRTZnkCxDRlhahXZsX_A1UGjiokZHVkHfTxQCyhd9mOvS8f_IrcGX6YwX_vHu3NQsqvJ-M5JLYAzxUE-NDdb5K1HwTPruHSxRaoj8pNuHgFHhhNSqh86-xmctvh1rcoiYF.png)

![](../../../../../../assets/drive/idDd6mEz0pXGB5MWi7L2wgYeas5dOXuCJCVhH_Zb2a4TWYGbHc1fgGwHEy5Yyv4ss9G-zP736NwP95l5IgFScpal65Z8G-ueARkHn6ije6drfpJAcR7XlxrXqeVLLMGgA5DJzvGV.png)

El importe de IVA debe contabilizarse en el libro mayor en una cuenta de Impuesto reclamado; por lo tanto, el asiento de la factura de compra es:

|     |     |     |     |
| --- | --- | --- | --- |
| Cuenta | Débito | Crédito contabilizado | Comentarios |
| Gastos del producto | Imp. línea |     | Uno por línea de factura |
| Impuesto reclamado | Impuestos |     | Uno por línea de impuesto |
| Pasivo del proveedor |     | Importe total | Uno por factura |



Ejemplos de rangos impuesto:

-   **Rango impuesto simple**
    -   *"Rango impuesto de IVA de compra al 18%"* perteneciente a la categoría de impuesto "IVA normal para productos", con País/Región establecido en España y País/Región de destino establecido en España.
-   **Rango impuesto de agrupación**
    -   "Rango impuesto de IVA de ventas de servicios al 18,00% + Retención (-15,00%)" perteneciente a la categoría de impuesto "IVA normal para servicios" y a la categoría de impuestos de terceros "Terceros sujetos a IVA e Impuesto sobre la Renta".  
        Este debe configurarse como tipo de agrupación, teniendo dos rangos impuesto por debajo que deben pertenecer a la misma categoría de impuesto y categoría de impuestos de terceros:
        -   "Rango impuesto de IVA de ventas de servicios al 18,00% + Retención (-15,00%) (IVA 18%)", índice = 18,00
        -   "Rango impuesto de IVA de ventas de servicios al 18,00% + Retención (-15,00%)" (R -15%)", índice = -15,00

### **Zona de Impuesto**

La zona de impuesto define el país/región de origen y el país/región de destino donde aplica un rango impuesto determinado, para aquellos casos en los que no es suficiente definir solo un "Origen" País/Región y solo un "Destino" País/Región a nivel de cabecera.

Por ejemplo, un rango impuesto de "Exportación" debe detallar como País/Región de origen la ubicación de la organización del almacén y como País/Región de destino el resto de países y regiones a los que es posible exportar los bienes. Este rango impuesto se aplicaría a transacciones de venta entre la organización "local" y sus clientes ubicados en el extranjero.

Lo mismo aplicaría a un rango impuesto de "Importación"; en este caso, el País/Región de origen serían todos los países desde los que se pueden importar bienes y el País/Región de destino sería el de la Organización.

### **Traducción**

Los rangos impuesto pueden traducirse a cualquier idioma requerido.

### **Contabilidad**

La solapa Contabilidad permite al usuario configurar la cuenta que se utilizará al contabilizar transacciones de rangos impuesto en el libro mayor.

-   la cuenta *"Impuesto repercutido"* es la cuenta utilizada al contabilizar importes de impuestos de venta
-   la cuenta *"Impuesto reclamado"* es la cuenta utilizada al contabilizar importes de impuestos de compra.
-   la cuenta *"Impuesto repercutido transitorio"* es la cuenta transitoria utilizada al contabilizar importes de impuestos de venta bajo el régimen de IVA de caja.
-   la cuenta *"Impuesto soportado transitorio"* es la cuenta transitoria utilizada al contabilizar importes de impuestos de compra bajo el régimen de IVA de caja.

![](../../../../../../assets/drive/15wOKJ7_50pNLBMCTWm7Rd_vJyGOZqcB0.png)

El asiento de una factura de compra es:

|     |     |     |     |
| --- | --- | --- | --- |
| Cuenta | Débito | Crédito contabilizado | Comentarios |
| Gastos del producto | Imp. línea |     | Uno por línea de factura |
| Impuesto reclamado | Impuestos |     | Uno por línea de impuesto. Para el régimen de IVA de caja se utiliza la cuenta *Impuesto soportado transitorio* en su lugar. |
| Pasivo del proveedor |     | Importe total | Uno por factura |

Y el asiento de una factura de venta es:

|     |     |     |     |
| --- | --- | --- | --- |
| Cuenta | Débito | Crédito contabilizado | Comentarios |
| Cuentas a cobrar de clientes | Importe total |     | Uno por factura |
| Ingresos por el producto |     | Imp. línea | Uno por línea de factura |
| Impuesto repercutido |     | Impuestos | Uno por línea de impuesto. Para el régimen de IVA de caja se utiliza la cuenta *Impuesto repercutido transitorio* en su lugar. |

Los rangos impuesto de retención "Negativo" necesitan tener información contable específica en esta solapa para que los importes de retención se contabilicen en una cuenta diferente.

El asiento siguiente aplica en el caso de que la funcionalidad "Permitir negativo" no esté habilitada ni para la configuración del libro mayor utilizada al contabilizar ni para el Tipo de documento, que en este caso es una "Factura AP"

En otras palabras, un asiento de retención negativa significa un asiento de débito negativo que se convertirá en un asiento de crédito positivo si no está habilitada la funcionalidad de negativos.

|     |     |     |     |
| --- | --- | --- | --- |
| Cuenta | Débito | Crédito contabilizado | Comentarios |
| Gastos del producto | Imp. línea |     | Uno por línea de factura |
| Impuesto reclamado | Impuestos |     | Uno por línea de impuesto. Para el régimen de IVA de caja se utiliza la cuenta *Impuesto soportado transitorio* en su lugar. |
| Impuesto reclamado |     | Importe de retención | Uno por línea de retención |
| Pasivo del proveedor |     | Importe total | (Imp. línea+Impuestos-Importe de retención) |

---

Este trabajo es una obra derivada de [Rango impuesto](https://wiki.openbravo.com/wiki/Tax_Rate){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.