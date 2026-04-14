---
title: Rango impuesto
tags:
    - Configuración de impuestos
    - Configuración de impuestos
    - Gestión de IVA
    - Configuración financiera
    - Impuestos de contabilidad
---

# Rango impuesto

:material-menu: `Aplicación` > `Gestión Financiera` > `Contabilidad` > `Configuración` > `Rango impuesto`

## Visión general

La ventana Rango impuesto es donde se definen los impuestos que Etendo aplica automáticamente a los documentos de venta y compra, como pedidos y facturas. Cada rango impuesto especifica el porcentaje a aplicar, a qué transacciones se aplica y cómo se calcula y registra el importe del impuesto en la contabilidad. Configurar correctamente los rangos impuesto garantiza que cada documento lleve el impuesto adecuado sin trabajo manual y que la empresa cumpla con sus obligaciones de información fiscal.

Un rango impuesto se determina mediante una combinación de elementos de configuración, entre los que se incluyen:

- **[Categoría de Impuesto](../setup/tax-category.md)**
- **Índice**
- **Tipo venta/compra**
- **[Categorías de Impuestos de Terceros](../setup/business-partner-tax-category.md)**
- **Origen y destino geográficos (Zona de Impuesto)**
- **Comportamientos fiscales especiales**: Retención (un impuesto deducido en origen antes del pago), Exento de impuestos (no se aplica impuesto), IVA de caja (el impuesto se liquida al cobro/pago y no en la fecha de la factura), Deducible (la empresa puede recuperar el impuesto) y No deducible (el impuesto se trata como un gasto).

Cuando estos parámetros están correctamente configurados, Etendo asigna automáticamente el impuesto correcto a cada línea de transacción según reglas predefinidas.

Los impuestos se asocian primero a las líneas de documento y, después, los importes reales de impuestos se calculan cuando el documento se procesa, garantizando la exactitud contable.

Algunas transacciones requieren dos impuestos separados al mismo tiempo, por ejemplo, IVA y una retención de IRPF en una factura de servicios. Etendo gestiona esto mediante impuestos de agrupación: se crea un impuesto padre que agrupa los impuestos individuales debajo de él. Cuando se selecciona el impuesto padre en una línea de documento, Etendo aplica y calcula automáticamente cada impuesto subyacente por separado. Esto significa que solo hay que elegir un impuesto por línea, incluso cuando se aplican dos impuestos.

## Obtención del impuesto por defecto

Cuando se añade un producto a un pedido o factura, Etendo selecciona automáticamente el impuesto para esa línea. Entender cómo funciona esta selección ayuda a explicar por qué apareció un impuesto concreto en un documento o por qué no se encontró ninguno. El sistema comprueba las siguientes condiciones en orden y se detiene en la primera coincidencia:

1. **Impuesto del proyecto (solo ventas):** Si el pedido de venta se generó a partir de un proyecto, el sistema usa el rango impuesto definido en la línea del proyecto.
2. **Tercero exento de impuestos (solo ventas):** Si el tercero está marcado como exento de impuestos, el sistema selecciona el rango impuesto marcado como exento con la fecha más reciente, relativa a la fecha del pedido o de la factura.
3. **Coincidencia de categoría de impuesto:** El sistema selecciona un impuesto de los definidos en la misma categoría de impuesto que el producto de la línea.
4. **Categoría de impuestos de terceros:** Si el rango impuesto está vinculado a una categoría de impuestos de terceros específica, solo se aplica a los terceros asignados a esa misma categoría, como proveedor o cliente. Los rangos impuesto sin categoría de impuestos de terceros pueden aplicarse a cualquier tercero. Cuando existen ambos, el que tiene una categoría de impuestos de terceros coincidente tiene prioridad.
5. **Proximidad geográfica (Zona de Impuesto):** El sistema evalúa las ubicaciones de origen y destino. Los rangos impuesto definidos para regiones más específicas tienen prioridad sobre los más amplios, por ejemplo, se selecciona un impuesto a nivel de región antes que uno a nivel de país. Esta información se configura en la solapa **Zona de Impuesto**.
6. **Tipo venta/compra:** El sistema filtra los rangos impuesto según si están definidos como Ventas, Compras o Ambos.

Si Etendo no puede encontrar un impuesto que coincida con todas las condiciones aplicables, no se asigna ningún impuesto a la línea. Esto suele significar que todavía no se ha creado un rango impuesto necesario o que falta alguna configuración obligatoria, por ejemplo, una entrada de Zona de Impuesto o un vínculo de Categoría de Impuestos de Terceros.

!!!note
    Hay un filtro adicional que solo se aplica a Pedidos y Facturas: IVA de caja. El IVA de caja es un régimen fiscal en el que la empresa liquida su obligación de IVA cuando la factura se cobra realmente, en lugar de cuando se emite. Etendo marca cada documento automáticamente en función de si la organización y el tercero usan este régimen. Cuando un documento está marcado como IVA de caja, el sistema selecciona solo los rangos impuesto configurados para IVA de caja; cuando no está marcado, selecciona solo los rangos impuesto estándar (sin IVA de caja). Esta marca puede cambiarse manualmente en la cabecera del documento si es necesario.

Una vez seleccionado el impuesto, ya sea el por defecto o uno elegido por el usuario, el sistema calcula un importe aproximado en la línea del documento. Si el impuesto está definido como **nivel de agrupación**, este cálculo preliminar usa el índice del padre en lugar de expandir los índices de los hijos. El importe real del impuesto se calcula cuando el documento se **procesa**.

Las líneas de impuesto en las facturas siguen uno de estos dos comportamientos:

- **Recalcular (por defecto):** La línea de impuesto está vinculada a una línea de factura. Cuando la factura se procesa, el sistema recalcula el importe del impuesto en función de los datos de la línea. Cualquier edición manual de una línea de impuesto recalculada se sobrescribe durante el proceso.
- **No recalcular:** La línea de impuesto se introduce manualmente en la solapa Impuesto de la factura y no está vinculada a ninguna línea de factura. Cuando la factura se procesa, el sistema conserva el importe introducido manualmente tal cual. Esta marca se establece automáticamente cuando un impuesto se crea manualmente y no puede cambiarse después.

!!!info
    **No recalcular** es útil para facturas que incluyen importes de impuestos sin una línea de producto correspondiente. Por ejemplo, al importar mercancías, normalmente existe una factura exenta de impuestos para los productos y una factura separada del agente de aduanas que contiene solo un importe de impuesto, como un arancel, sin ninguna línea de producto.

Cuando se procesa un documento, el sistema calcula los importes finales de impuestos a partir de los impuestos seleccionados, salvo que estén definidos como **No recalcular** en facturas, siguiendo estos pasos:

1. Se eliminan todos los importes de impuestos preliminares mostrados antes del proceso, ya que son aproximados y pueden ser inexactos.
2. Para cada impuesto distinto aplicado a las líneas del documento, el sistema crea un registro de impuesto y calcula el importe en función de las bases imponibles de las líneas asociadas (cada línea tiene solo un impuesto).
3. Para los impuestos definidos como **nivel de agrupación**, el sistema expande el padre en sus rangos impuesto hijos y calcula cada importe de hijo por separado, teniendo en cuenta si los hijos están configurados como en cascada.

## Cabecera

La cabecera define las características principales y el comportamiento del rango impuesto.

![Tax Rate header fields](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/set-up/tax-rate1.png)

Campos a tener en cuenta: 

- **Válido desde**: fecha en la que el impuesto entra en vigor.

    !!! warning
        Si un rango impuesto cambia, por ejemplo, porque el gobierno aumenta el índice del IVA, no edite el rango impuesto existente. Cree un nuevo rango impuesto con el porcentaje actualizado y una nueva fecha de Válido desde. Así se conserva el índice original en los documentos antiguos y se garantiza que el nuevo índice se aplique a partir de la fecha efectiva.

- **Categoría de Impuesto**: cada rango impuesto debe estar vinculado a una [categoría de impuesto](../setup/tax-category.md) como forma de agrupar rangos impuesto similares.
- **Índice**: porcentaje aplicado a la base imponible.
- **Tipo venta/compra**: forma de distinguir entre impuestos de venta y de compra. El tipo de impuesto es otra variable que Etendo tiene en cuenta al recuperar el rango impuesto correcto tanto en transacciones de venta como de compra y también es una variable muy valiosa a tener en cuenta al informar sobre impuestos, ya que hay informes fiscales que requieren presentar la información de impuestos de compra y de venta por separado.

    !!!info
        Existe una opción adicional, **Ambos**, que permite usar el **mismo rango impuesto** tanto para transacciones de compra como de venta.

- **Cálculo del importe de impuestos del documento**: forma en que se va a calcular el importe de impuestos para cada rango impuesto (o %). 
    Las opciones disponibles son:
    - **Importe basado en documento por índice**: Etendo suma todos los importes imponibles del documento que comparten el mismo índice y luego aplica el porcentaje una sola vez al total. Es la opción más habitual. Puede producir diferencias de redondeo muy pequeñas, de unos céntimos, en comparación con el cálculo línea a línea.
    - **Importe base de línea por índice**: Etendo calcula el impuesto por separado para cada línea del documento y luego suma los resultados. Use esta opción cuando la autoridad fiscal o el cliente requiera que el impuesto se muestre y redondee a nivel de línea individual.

- **País/Región** y **País/Región de destino**: impuestos como el IVA y el Impuesto sobre ventas de EE. UU. tienen en cuenta desde dónde y hacia dónde se origina una transacción para determinar si el impuesto se aplica o no.
    Estos dos campos permiten introducir esa información teniendo en cuenta si el impuesto es de tipo **compra** o **ventas**; por lo tanto, al emitir una factura de venta desde F&B US Inc (País USA y Región Nueva York) a un cliente también ubicado en País de destino USA y Región de destino Nueva York, solo se aplicarían los rangos impuesto de ventas creados dentro de esa Zona de Impuesto especificada.

- **Base Imponible**: base imponible a tener en cuenta en el cálculo del importe de impuestos. Las opciones disponibles son:
    - **Imp. línea**
    - **Imp. línea + Impuestos**
    - **Base imponible alternativa**
    - **Base imponible alternativa + Impuestos**

- **Nivel agrupación**: un rango impuesto puede definirse como de agrupación, lo que significa que tendrá algunos rangos impuesto por debajo.
    Los rangos impuesto de agrupación también se establecen como **Impuesto padre**, por lo que sus rangos impuesto hijos pueden vincularse a él. Por ejemplo, se emite una factura de venta a un tercero bajo un régimen de IVA específico que incluye un rango impuesto adicional además del tipo de IVA.
    Para este escenario, es necesario crear tres rangos impuesto: el padre como de agrupación y dos más para el tipo de IVA y para el otro tipo, ambos vinculados al padre.

    !!!info
        Es importante remarcar que al emitir la factura de venta para ese tercero, el rango impuesto mostrado/seleccionado es el de agrupación o el padre.

En la sección **Más información** también hay algunos campos relevantes:

-   **Impuesto padre**: los rangos impuesto que pertenecen a un rango impuesto de agrupación deben vincularse a él en este campo para que el árbol de rangos impuesto esté correctamente estructurado.
-   **Categoría de Impuestos de Terceros**: un rango impuesto puede vincularse a una categoría de impuestos de terceros específica; por lo tanto, solo se aplicará a los terceros que pertenezcan a esa categoría.
-   **Retención**: un rango impuesto puede configurarse como **Retención**, por lo que se gestiona correctamente como un tipo de impuesto separado en los informes fiscales.
    -   Los rangos impuesto de retención son rangos impuesto **Negativo**.
-   **Exento de impuestos**: un rango impuesto puede configurarse como exento; por lo tanto, es el que se muestra automáticamente en las líneas de pedido/factura creadas para un Cliente configurado también como exento de impuestos.
-   **IVA de caja**: este tipo de rangos impuesto se utiliza para soportar el régimen de IVA de caja, que permite a las empresas liquidar el importe de IVA cuando han cobrado/pagado las facturas en lugar de en la creación de la factura. 

    !!!note
        Al usar rangos impuesto de IVA de caja, las cuentas Impuesto repercutido transitorio e Impuesto soportado transitorio deben declararse en la solapa Contabilidad.

-   Los rangos impuesto también pueden configurarse como **No está sujeto a impuestos**. Un rango impuesto no sujeto a impuestos puede vincularse a transacciones sujetas a impuestos que pasan a no estar sujetas a impuestos bajo una situación determinada. Hay informes fiscales que requieren información sobre ambos tipos de impuestos: exentos y no sujetos a impuestos.
-   **Deducible**: la organización puede recuperar el importe del impuesto. El IVA se contabiliza en una cuenta de **Impuesto reclamado** y puede compensarse con las obligaciones fiscales.
-   **No deducible**: la organización no puede recuperar el importe del impuesto. El IVA se trata como un gasto adicional y se contabiliza en la cuenta de **Gastos del producto** en lugar de en Impuesto reclamado.

La forma en que se comportan los rangos impuesto **Deducible** y **No deducible** en términos contables se explica a continuación:

-   Factura de compra que incluye un importe de impuestos **deducible**.  
    El importe de IVA debe contabilizarse en el libro mayor en una cuenta de Impuesto reclamado; por lo tanto, el asiento de la factura de compra es:

|     |     |     |     |
| --- | --- | --- | --- |
| Cuenta | Débito | Crédito contabilizado | Comentarios |
| Gastos del producto | Imp. línea |     | Uno por línea de factura |
| Impuesto reclamado | Impuestos |     | Uno por línea de impuesto |
| Pasivo del proveedor |     | Importe total | Uno por factura |

-   Factura de compra que incluye un importe de impuestos **no deducible**.  
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