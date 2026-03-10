---
title: Liquidación de terceros
tags: 
    - Liquidación
    - Pago
    - Terceros
---

# Liquidación de terceros

:octicons-package-16: Javapackage: `com.etendoerp.advanced.bpsettlement`

:octicons-package-16: Javapackage: `org.openbravo.financial.bpsettlement`


## Visión general

Este módulo proporciona un nuevo documento donde es posible **liquidar deudas o crédito** de terceros que son tanto clientes como proveedores. Cuando un tercero es Cliente y Proveedor, es posible tener crédito como ambos tipos. Pero no es posible consumir un crédito de cliente en un documento de Pago. Del mismo modo, no es posible mezclar facturas de compra o de venta en un único documento de pago. En algunos escenarios, cuando un tercero tiene facturas de venta y de compra, es deseable cancelar ambas deudas sin necesidad de una transacción financiera.

En este documento, debe seleccionar las facturas o el importe de crédito que se desea liquidar. Cuando el documento se procesa, se crean un *Cobros* y un *Pago*. Ambos tienen un importe total de cero, por lo que no se crea ninguna transacción financiera. El importe liquidado en cada pago se compensa mediante una línea de *Concepto contable*. Ambos pagos utilizan el mismo Concepto contable, por lo que el saldo del mismo tras el proceso es cero.

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el bundle Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).


## Configuración inicial

No se requiere ninguna configuración específica para trabajar con este módulo. Se espera que los terceros ya estén completamente definidos como **Cliente** y **Proveedor** con sus correspondientes **Cuenta financiera** y **Moneda**.

También es necesario tener al menos un **Concepto contable** definido para las Organizaciones donde se necesiten estas liquidaciones.

## Ventana Liquidación de terceros

:material-menu: `Aplicación` > `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Transacciones` > `Liquidación de terceros`

![CS](../../../../../assets/drive/1annoerkei9LaS96_BUY5bysMxH8_E803.png)

En esta ventana se registran todas las liquidaciones. En una nueva, debe seleccionar:

- **Tipo**: Crédito o Factura
- **Fecha de Liquidación**
- **Terceros**
- **Concepto contable**: el saldo del Concepto contable después del proceso de liquidación no se verá afectado, por lo tanto, se puede crear y utilizar para ello una cuenta contable específica fuera del árbol de cuentas.

Dependiendo del tipo de liquidación, el botón de proceso seleccionado en la parte superior y las solapas hijas inferiores cambian en consecuencia para mostrar los pagos de crédito o las facturas a liquidar.

### Botones

#### Liquidación de crédito

![CS](../../../../../assets/drive/1annoerkei9LaS96_BUY5bysMxH8_E803.png)

En las liquidaciones de crédito, debe seleccionar los pagos de crédito que se requieren liquidar. Al hacer clic en el botón **Agregar Cobros/Pagos a Crédito**, se abre un popup donde puede seleccionar desde 2 rejillas los pagos de *Crédito de entrada* y *Crédito de salida*. En la sección Totales, se calculan los importes totales de los pagos de crédito seleccionados.

!!! warning
    No puede cerrar y añadir los pagos de crédito hasta que los importes totales de cada rejilla sean los mismos. Esto significa que *Importe de crédito de entrada* e *Importe de crédito de salida* deben ser iguales, por lo tanto el pago de crédito es 0.00

![IS](../../../../../assets/drive/1xh1LMaTcJWuLXzNeqesDDY0niWC1VLv6.png)

#### Liquidación de facturas

![IS](../../../../../assets/drive/16rHvcenj5_bk5_qSmaiq55vc-DtdPa2x.png)

Al igual que en las liquidaciones de crédito, al hacer clic en **Agregar Facturas no Pagadas** se abre un popup con 2 rejillas. En este caso, las rejillas muestran *facturas no pagadas*. Una vez más, no es posible crear pagos de liquidación hasta que el **Pending amount** sea 0.00, como se muestra en la imagen siguiente:

![IS](../../../../../assets/drive/1_6G9sHyHAhvjBD4ktBmlwmj1E8QUivF7.png)

#### Procesar Liquidación

Dependiendo del estado de la liquidación, hay disponibles diferentes acciones:

- **Borrador**: en este estado solo es posible procesar la liquidación.
- **Procesado**: en este estado es posible **Cancelar** o **Reactivar** la liquidación.
- **Cancelado**: en este estado no es posible realizar ninguna acción.


**Proceso**

Cuando la liquidación se **procesa**, se crean un *Cobros* y un *Pago*. Cada pago incluye todos los pagos de crédito o facturas que se seleccionaron en la liquidación.

Vea las imágenes siguientes en el caso de pagos de liquidación relacionados con facturas.

<figure markdown="span">
    ![IS](../../../../../assets/drive/1jh-cvFM4r4uHBH11jspb2XVnp_GthyfW.png)
    <figcaption>**Cobro**</figcaption>
</figure>

<figure markdown="span">
    ![IS](../../../../../assets/drive/15MCP7JSy_YEdnBeOB8CUgNSRmtc75VZR.png)
    <figcaption>**Pago**</figcaption>
</figure>

Los pagos generados se establecen en la cabecera de **Liquidación de terceros**; las facturas se insertan como **Líneas de pago**, mientras que los pagos de crédito se añaden al pago como *Crédito usado*.

Como el importe total del pago de liquidación debe ser cero, se añade una línea de pago adicional utilizando el **Concepto contable seleccionado**.

El importe en las líneas relacionadas con el *Concepto contable* es el mismo en ambos pagos, por lo tanto el efecto neto sobre el saldo del Concepto contable es nulo. En otras palabras, el saldo del Concepto contable no se altera por el proceso de liquidación.

    Contabilización del Cobro de liquidación:
    2722.50 Cuenta contable de Concepto contable (55500) DEBE
    2722.50 Cuenta de clientes (43000) HABER

    Contabilización del Pago de liquidación:
    2722.50 Cuenta de proveedores (40000) DEBE
    2722.50 Cuenta contable de Concepto contable (55500) HABER

Finalmente, como el **Importe del pago de liquidación** es cero, no se crea ninguna **Transacción** en la Cuenta financiera del pago, por lo tanto no será necesario incluirla en ninguna conciliación.

**Reactivar**

Cuando se reactiva una liquidación, los pagos generados se cancelan creando un pago inverso. Este proceso restaurará la deuda o el crédito para que vuelva a estar disponible y las facturas vuelvan a estar no pagadas. Los pagos generados se eliminan de la cabecera, pero se mantiene la selección de crédito o facturas, por lo que es posible añadir nuevos elementos, eliminar algunos elementos y/o editar los importes liquidados.

!!! info
    La liquidación se deja en estado Borrador para que sea posible procesarla de nuevo cuando sea necesario.

**Cancelar**
Al igual que en el proceso de Reactivar, los pagos de liquidación se cancelan creando un pago inverso y el crédito o las facturas liquidadas vuelven a estar disponibles o no pagadas. Pero, en este caso, estos pagos no se eliminan de la cabecera de la liquidación y el estado cambia a Cancelado.

!!! info
    En este estado, ya no es posible modificar la liquidación.

## Usar la funcionalidad desde otras ventanas.

- [Cobro](../../../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#advanced-business-partner-settlement-1)

- [Pago](../../../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#advanced-business-partner-settlement)

- [Cuenta financiera](../../../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#advanced-business-partner-settlement-2)
  

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.