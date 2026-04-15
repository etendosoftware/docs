---
title: Rango impuesto
tags:
    - Tax Setup
    - Tax Configuration
    - VAT Management
    - Financial Setup
    - Accounting Taxes
---

# Rango impuesto

:material-menu: `Aplicación` > `Gestión Financiera` > `Contabilidad` > `Configuración` > `Rango impuesto`

## Overview

La ventana de Rango impuesto es donde se definen los impuestos que Etendo aplica automáticamente a los documentos de ventas y compras, como pedidos y facturas. Cada rango de impuesto especifica el porcentaje a cobrar, a qué transacciones se aplica y cómo se calcula y registra el importe del impuesto en tus cuentas. Configurar correctamente los rangos de impuesto garantiza que cada documento lleve el impuesto adecuado sin trabajo manual y que tu empresa cumpla con sus obligaciones de declaración fiscal.

Un rango de impuesto se determina por una combinación de elementos de configuración, entre ellos:

- **[Categoría de Impuesto](../setup/tax-category.md)**
- **Percentage rate**
- **Tipo venta/compra**
- **[Categorías de Impuestos de Terceros](../setup/business-partner-tax-category.md)**
- **Geographic origin and destination (Tax Zone)**
- **Special tax behaviors**: Retención (un impuesto deducido en origen antes del pago), Exento de impuestos (no se aplica impuesto), IVA de caja (el impuesto se liquida al pagar en lugar de en la fecha de la factura), Deducible (la empresa puede recuperar el impuesto) y No deducible (el impuesto se trata como un gasto).

Cuando estos parámetros están configurados correctamente, Etendo asigna automáticamente el impuesto correcto a cada línea de transacción.

Los impuestos se **asocian a las líneas del documento** primero, y después los importes reales del impuesto se calculan cuando el documento se **procesa**, garantizando la precisión contable.

Algunas transacciones requieren dos impuestos separados al mismo tiempo; por ejemplo, IVA y una retención de impuesto sobre la renta en una factura de servicios. Etendo gestiona esto mediante impuestos de resumen: creas un impuesto padre que agrupa los impuestos individuales debajo de él. Cuando seleccionas el impuesto padre en una línea de documento, Etendo aplica y calcula automáticamente cada impuesto subyacente por separado. Esto significa que solo tienes que elegir un impuesto por línea, incluso cuando se aplican dos impuestos.


## Obtaining Default Tax

Cuando añades un producto a un pedido o factura, Etendo selecciona automáticamente el impuesto para esa línea. Entender cómo funciona esta selección ayuda a explicar por qué apareció un impuesto concreto en un documento, o por qué no se encontró ningún impuesto. El sistema comprueba las siguientes condiciones en orden y se detiene en la primera coincidencia:

1. **Project tax (sales only):** Si el pedido de venta se generó a partir de un Proyecto, el sistema usa el rango de impuesto definido en la línea del proyecto.
2. **Tax-exempt business partner (sales only):** Si el tercero está marcado como exento de impuestos, el sistema selecciona el rango de impuesto con la fecha más reciente marcado como exento, en relación con la fecha del pedido o de la factura.
3. **Tax category match:** El sistema selecciona un impuesto de los definidos en la misma categoría de impuesto que el producto de la línea.
4. **Business partner tax category:** Si el rango de impuesto está vinculado a una categoría de impuestos de tercero específica, solo se aplica a los terceros asignados a esa misma categoría (como proveedor o cliente). Los rangos de impuesto sin una categoría de impuestos de tercero pueden aplicarse a cualquier tercero. Cuando existen ambos, el que tiene una categoría de impuestos de tercero coincidente tiene prioridad.
5. **Geographic proximity (Tax Zone):** El sistema evalúa las ubicaciones de origen y destino. Los rangos de impuesto definidos para regiones más específicas tienen prioridad sobre las más amplias (por ejemplo, se selecciona un impuesto a nivel de región antes que uno a nivel de país). Esta información se configura en la pestaña **Zona de Impuesto**.
6. **Sales/Purchase type:** El sistema filtra los rangos de impuesto según estén definidos como Ventas, Compras o Ambos.

Si Etendo no puede encontrar un impuesto que coincida con todas las condiciones aplicables, no se asigna ningún impuesto a la línea. Esto normalmente significa que aún no se ha creado un rango de impuesto requerido o que falta una configuración necesaria (por ejemplo, una entrada de Zona de Impuesto o un enlace de Categorías de Impuestos de Terceros).

!!!note
    Hay un filtro adicional que solo se aplica a Pedidos y Facturas: IVA de caja. El IVA de caja es un régimen fiscal en el que una empresa liquida su obligación de IVA cuando la factura se paga realmente, en lugar de cuando se emite. Etendo marca automáticamente cada documento según si la organización y el tercero usan este régimen. Cuando un documento está marcado como IVA de caja, el sistema selecciona solo los rangos de impuesto configurados para IVA de caja; cuando no está marcado, el sistema selecciona solo los rangos de impuesto estándar (no IVA de caja). Esta marca se puede cambiar manualmente en la cabecera del documento si es necesario.

Una vez seleccionado el impuesto (ya sea el predeterminado o uno elegido por el usuario), el sistema calcula un importe de impuesto aproximado en la línea del documento. Si el impuesto está definido como **summary**, este cálculo preliminar usa el rango padre en lugar de expandir los rangos hijo. El importe real del impuesto se calcula cuando el documento se **procesa**.

Las líneas de impuesto en las facturas siguen uno de dos comportamientos:

- **Recalculate (default):** La línea de impuesto está vinculada a una línea de factura. Cuando se procesa la factura, el sistema recalcula el importe del impuesto en función de los datos de la línea. Cualquier edición manual de una línea de impuesto recalculada se sobrescribe durante el procesamiento.
- **No Recalculate:** La línea de impuesto se introduce manualmente en la pestaña Impuestos de la factura y no está vinculada a ninguna línea de factura. Cuando se procesa la factura, el sistema conserva el importe introducido manualmente tal cual. Esta marca se establece automáticamente cuando un impuesto se crea manualmente (y no puede cambiarse después).

!!!info
    **No Recalculate** es útil para facturas que incluyen importes de impuesto sin una línea de producto correspondiente. Por ejemplo, al importar mercancías, normalmente hay una factura exenta de impuestos para los productos y una factura separada del agente de aduanas que contiene solo un importe de impuesto (como aranceles aduaneros) sin líneas de producto.


Cuando un documento se procesa, el sistema calcula los importes finales de impuesto a partir de los impuestos seleccionados (salvo que estén definidos como **No Recalculate** en facturas) siguiendo estos pasos:

1. Se eliminan todos los importes preliminares de impuesto mostrados antes del procesamiento, ya que son aproximados y pueden ser inexactos.
2. Para cada impuesto distinto aplicado a las líneas del documento, el sistema crea una entrada de impuesto y calcula el importe en función de las bases imponibles de las líneas asociadas (cada línea tiene solo un impuesto).
3. Para los impuestos definidos como **summary**, el sistema expande el padre en sus rangos de impuesto hijo y calcula cada importe hijo por separado, teniendo en cuenta si los hijos están configurados como cascade.

## Cabecera

La cabecera define las características principales y el comportamiento del rango de impuesto.

![Tax Rate header fields](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/set-up/tax-rate1.png)

Campos a tener en cuenta: 

- **Válido desde**: Fecha en la que el impuesto entra en vigor.

    !!! warning
        Si un rango de impuesto cambia (por ejemplo, si el gobierno aumenta el tipo de IVA), no edites el rango de impuesto existente. Crea un nuevo rango de impuesto con el porcentaje actualizado y una nueva fecha de Válido desde. Esto preserva el rango original en documentos anteriores y garantiza que el nuevo rango se aplique a partir de la fecha de entrada en vigor.

- **Categoría de Impuesto**: Todo rango de impuesto debe estar vinculado a una determinada [categoría de impuesto](../setup/tax-category.md) como forma de agrupar rangos de impuesto similares.
- **Rate (%)**: Porcentaje aplicado a la base imponible.
- **Tipo venta/compra**: La forma de distinguir entre impuestos de ventas y de compras. El tipo de impuesto es otra variable que Etendo tiene en cuenta al recuperar el rango de impuesto correcto tanto en transacciones de ventas como de compras, y también es una variable muy valiosa a tener en cuenta al informar impuestos, ya que hay informes fiscales que requieren presentar la información de impuestos de compras y ventas por separado.

    !!!info
        Existe una opción adicional que es **Ambos**; esta opción permite que se use el **mismo rango de impuesto** tanto para transacciones de compras como de ventas.

- **Cálculo del importe de impuestos del documento**: La forma en que se va a calcular el importe del impuesto para cada rango de impuesto (o %). 
    Las opciones disponibles son:
    - **Document based amount by rate**: Etendo suma todos los importes imponibles del documento que comparten el mismo rango de impuesto y luego aplica el porcentaje una sola vez al total. Esta es la opción más habitual. Puede producir diferencias de redondeo muy pequeñas (unos céntimos) en comparación con el cálculo línea a línea.
    - **Line base amount by rate**: Etendo calcula el impuesto por separado para cada línea del documento y luego suma los resultados. Usa esta opción cuando la autoridad fiscal o tu cliente requiera que el impuesto se muestre y redondee a nivel de línea individual.

- **Country/Region** y **Destination Country/Region**: Impuestos como el IVA y el impuesto sobre ventas de EE. UU. tienen en cuenta dónde se origina una transacción y dónde tiene destino para determinar si el impuesto se aplica.
    Estos dos campos permiten introducir esa información teniendo en cuenta si el impuesto es de tipo **compra** o **venta**; por tanto, al emitir una factura de venta desde F&B US Inc (país USA y región New York) a un cliente ubicado también en Destination Country USA y Destination Region New York, solo se aplicarían los rangos de impuesto de ventas creados dentro de esa Zona de Impuesto especificada.

- **Base Imponible**: La base imponible a tener en cuenta en el cálculo del importe del impuesto. Las opciones disponibles son:
    - **Imp. línea**
    - **Imp. línea + Tax Amount**
    - **Alternate Tax Base Amount**
    - **Alternate Tax Base Amount + Tax Amount**

- **Nivel agrupación**: Un rango de impuesto puede definirse como resumen, lo que significa que tendrá **some tax rates underneath**.
    Los rangos de impuesto de resumen también se establecen como **Impuesto padre**, por lo que sus rangos de impuesto hijo pueden vincularse a él. Por ejemplo, se emite una factura de venta a un tercero bajo un régimen de IVA específico que incluye un rango de impuesto adicional además del rango de IVA.
    Para este escenario, es necesario crear tres rangos de impuesto: el padre como resumen y otros dos para el rango de IVA y para el otro rango, ambos vinculados al padre.

    !!!info
        Es importante señalar que, al emitir la factura de venta para ese tercero, el rango de impuesto mostrado/seleccionado es el de resumen o padre.

En la sección **More Information**, también hay algunos campos relevantes:

-   **Impuesto padre**: los rangos de impuesto que pertenezcan a un rango de impuesto de resumen deben vincularse a él en este campo para que el árbol de rangos de impuesto esté correctamente estructurado.
-   **Categorías de Impuestos de Terceros**: un rango de impuesto puede vincularse a una categoría de impuestos de tercero específica, por lo que solo se aplicará a los terceros pertenecientes a esa categoría.
-   **Retención**: un rango de impuesto puede establecerse como **Retención**, por lo que se gestiona correctamente como un tipo de impuesto separado en los informes fiscales.
    -   Los rangos de impuesto de retención son rangos de impuesto **Negativo**.
-   **Exento de impuestos**: un rango de impuesto puede establecerse como exento, por lo que será el que se muestre automáticamente en las líneas de pedido/factura creadas para un determinado cliente también marcado como exento de impuestos.
-   **IVA de caja**: este tipo de rangos de impuesto se usa para dar soporte al régimen de IVA de caja, que permite a las empresas liquidar el importe del IVA cuando han cobrado/pagado las facturas en lugar de en la creación de la factura. 

    !!!note
        Al usar rangos de impuesto de IVA de caja, las cuentas transitorias de Impuesto repercutido e Impuesto soportado transitorio deben declararse en la pestaña Contabilidad.

-   Los rangos de impuesto también pueden configurarse como **No está sujeto a impuestos**. Un rango de impuesto no sujeto a impuestos puede vincularse a transacciones sujetas a impuesto que pasan a no estar sujetas a impuestos bajo una determinada situación. Hay informes fiscales que requieren información sobre ambos tipos de impuestos, exento y no sujeto a impuestos.
-   **Deducible**: La organización puede recuperar el importe del impuesto. El IVA se contabiliza en una cuenta de **Impuesto reclamado** y puede compensarse con las obligaciones fiscales.
-   **No deducible**: La organización no puede recuperar el importe del impuesto. El IVA se trata como un gasto adicional y se contabiliza en la cuenta de **Gastos del producto** en lugar de en Impuesto reclamado.

La forma en que se comportan los rangos de impuesto **Deducible y No deducible** en términos contables se explica a continuación:

-   Factura de compra que incluye un importe de impuesto **deducible**. El importe del IVA se contabiliza en una cuenta de Impuesto reclamado:

|     |     |     |     |
| --- | --- | --- | --- |
| Account | Debit | Credit | Comments |
| Gastos del producto | Imp. línea |     | One per invoice line |
| Impuesto reclamado | Tax Amount |     | One per tax line |
| Vendor Liability |     | Total Gross Amount | One per invoice |

-   Factura de compra que incluye un importe de impuesto **no deducible**. El importe del IVA no puede contabilizarse en una cuenta de Impuesto reclamado porque representa un gasto:

|     |     |     |     |
| --- | --- | --- | --- |
| Account | Debit | Credit | Comments |
| Gastos del producto | Imp. línea + Tax Amount |     | One per invoice line and tax rate |
| Vendor Liability |     | Total Gross Amount | One per invoice |

De forma predeterminada, el importe contable que se genera en las facturas de proveedor cuando se usa un rango de impuesto no deducible se asigna a la cuenta de gasto contable configurada en la pestaña **Contabilidad** del producto. En caso de que el usuario necesite contabilizar el importe del impuesto no deducible en una cuenta específica, debe marcarse la casilla **Use the configured account** situada dentro de la pestaña Contabilidad en la ventana Rango impuesto. En este caso, debe estar instalado el módulo **Accounting Template Module** del paquete Financial Extensions.

!!!info
    Para más información, visita [Accounting Template Module user guide](../../../../optional-features/bundles/financial-extensions/accounting-template-module.md). 


### Zona de Impuesto

La zona de impuesto define el país/región de origen y el país/región de destino donde se aplica un determinado rango de impuesto, para aquellos casos en los que no basta con definir solo un **Origen** país/región y solo un **Destination** país/región a nivel de cabecera.

Por ejemplo, un rango de impuesto de **Export** debe detallar como País/Región de origen la ubicación de la organización del almacén y como País/Región de destino el resto de países y regiones a los que es posible exportar las mercancías. Este rango de impuesto se aplica a transacciones de ventas en las que el vendedor es tu propia empresa (el origen) y el comprador está ubicado en otro país (el destino). El país y la región de origen en esta pestaña deben coincidir con la dirección configurada para tu entidad legal en Etendo.

Lo mismo se aplicaría a un rango de impuesto de **Import**; en este caso, País/Región de origen serían todos los países desde los que se pueden importar mercancías y País/Región de destino sería la ubicación propia de la organización.

### Traducción

La pestaña Traducción permite al usuario traducir el **Nombre**, la **Descripción** y el **Identificador de impuestos** del rango de impuesto a cualquier idioma habilitado en el sistema. Esto garantiza que la información del rango de impuesto se muestre en el idioma adecuado cuando los usuarios trabajan con Etendo en una configuración regional distinta de la predeterminada.

Cada fila de la rejilla representa un idioma disponible. Para traducir un rango de impuesto, selecciona la fila del idioma correspondiente e introduce los valores traducidos en los campos **Nombre** y **Descripción**. La columna **Traducción** indica si se ha proporcionado una traducción manual para ese idioma.

![Tax Rate translation tab](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/set-up/tax-rate-translation.png)

### Contabilidad

La pestaña Contabilidad permite al usuario configurar la cuenta que se utilizará al contabilizar transacciones de rango de impuesto en el libro mayor.

- **Impuesto repercutido** es la cuenta utilizada al contabilizar importes de impuestos de ventas.
- **Impuesto reclamado** es la cuenta utilizada al contabilizar importes de impuestos de compras.


![Tax Rate accounting tab](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/set-up/tax-rate2.png)

Una contabilización de factura de compra tiene este aspecto:

|     |     |     |     |
| --- | --- | --- | --- |
| Account | Debit | Credit | Comments |
| Gastos del producto | Imp. línea |     | One per invoice line |
| Impuesto reclamado | Tax Amount |     | One per tax line. For Cash VAT regime the *Tax Credit Transitory* account is used instead. |
| Vendor Liability |     | Total Gross Amount | One per invoice |

Y una contabilización de factura de venta tiene este aspecto:

|     |     |     |     |
| --- | --- | --- | --- |
| Account | Debit | Credit | Comments |
| Customer Receivable | Total Gross Amount |     | One per invoice |
| Product Revenue |     | Line Net Amount | One per Invoice Line |
| Impuesto repercutido |     | Tax Amount | One per Tax Line. For Cash VAT regime the *Tax Due Transitory* account is used instead. |

Los rangos de impuesto de retención **Negativo** necesitan tener información contable específica en esta pestaña para que los importes de retención se contabilicen en una cuenta diferente.

Los asientos contables siguientes se aplican cuando no se permiten importes negativos en la configuración del Libro Mayor o en el tipo de documento de factura AP (AP significa Accounts Payable). En ese caso, un importe de retención —que por naturaleza es negativo— se convierte automáticamente en un asiento de crédito positivo en los registros contables. Si tu sistema está configurado para permitir importes negativos, la retención se contabilizará directamente como un débito negativo.

|     |     |     |     |
| --- | --- | --- | --- |
| Account | Debit | Credit | Comments |
| Gastos del producto | Imp. línea |     | One per Invoice Line |
| Impuesto reclamado | Tax Amount |     | One per tax line. For Cash VAT regime the *Tax Credit Transitory* account is used instead. |
| Impuesto reclamado |     | Withholding Amount | One per withholding line |
| Vendor Liability |     | Total Gross Amount | (Line Net Amount+Tax Amount-Withholding Amount) |



## Examples

- **Simple tax rate**
    - Example: *Purchase VAT 18%*.
    - Use case: local purchase of goods subject to standard VAT.
    - Typical settings: Tax Category = **Normal VAT for Products**; Rate = **18%**; Origin = **Spain**; Destination = **Spain**.
    - Behaviour: when applied to a purchase invoice, VAT posts to the configured **Tax Credit** account.

- **Summary tax rate (combined tax + withholding)**
    - Example: *Service VAT 18% + Withholding 15%*.
    - Use case: a service invoice where both VAT and an income-tax withholding apply.
    - How to set it up:
        - Create a **Parent** tax rate of type **Summary** and assign it to the tax category **Normal VAT for Services** and to the appropriate **Business Partner Tax Category**.
        - Add two **child** tax rates under the parent (both must use the same tax and partner categories). For each child tax rate, open its record and set the **Parent Tax Rate** field (found under the More Information section of the Header tab) to point to the parent tax rate you just created. This is what links the child to the parent and builds the summary structure.
            - *Service VAT* — Rate: **18%** (positive).
            - *Withholding (Income Tax)* — Rate: **-15%** (negative withholding).
    - Behaviour: select the parent (summary) tax on the document line; during processing, the system uses the children to calculate and post the separate tax and withholding amounts.
    
    !!!note
        Withholding rates typically post to a different account — configure the child tax accounting accordingly.


---

This work is a derivative of [Tax Rate](https://wiki.openbravo.com/wiki/Tax_Rate){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.