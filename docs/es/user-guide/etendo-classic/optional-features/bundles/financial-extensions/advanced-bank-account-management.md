---
tags:
    - Cuenta bancaria
    - Financiero
    - Modificar plan de pagos 
---

# Gestión avanzada de cuentas bancarias

:octicons-package-16: Javapackage: `com.etendoerp.advanced.bank.account.management`

:octicons-package-16: Javapackage: `com.etendoerp.advanced.bank.account.management.template`

## Visión general

<iframe width="560" height="315" src="https://www.youtube.com/embed/7AtGyQ62FHs?si=HisPbmd0KzblSq0O" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Esta sección describe el módulo Advanced Bank Account Management incluido en el bundle Etendo Financial Extensions.

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el bundle Financial Extensions. Para ello, siga las instrucciones del marketplace: [Bundle Financial Extensions](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

Esta funcionalidad mejora la gestión de cuentas bancarias, permitiendo una mayor personalización y control sobre la selección de cuentas bancarias asociadas a clientes y proveedores.

Esta funcionalidad está disponible en las siguientes ventanas: 

- [Terceros](../../../basic-features/master-data-management/master-data.md#advanced-bank-account-management)
- [Factura (Cliente)](../../../basic-features/sales-management/transactions.md#advanced-bank-account-management_1)
- [Factura (Proveedor)](../../../basic-features/procurement-management/transactions.md#advanced-bank-account-management_1)
- [Pedido de venta](../../../basic-features/sales-management/transactions.md#advanced-bank-account-management)
- [Pedido de compra](../../../basic-features/procurement-management/transactions.md#advanced-bank-account-management)
- [Cobros](../../../basic-features/financial-management/receivables-and-payables/transactions.md#advanced-bank-account-management_1)
- [Pago](../../../basic-features/financial-management/receivables-and-payables/transactions.md#advanced-bank-account-management)

## Terceros - Cuenta bancaria
:material-menu: `Aplicación` > `Gestión de Datos Maestros` > `Terceros`

Este módulo introduce la posibilidad de marcar una cuenta bancaria como **Predeterminada** dentro de la pestaña **Cuenta bancaria** de la ventana **Terceros**. Aquí, es posible marcar la casilla **Cuenta predeterminada** para establecer la cuenta que se utilizará en facturas y pedidos. Esta información determina la cuenta bancaria de cada pago.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/advanced-bank-account-management/aba1.png)

## Terceros - Ubicación/Dirección
:material-menu: `Aplicación` > `Gestión de Datos Maestros` > `Terceros` 

El campo **Gestión avanzada de cuentas bancarias** se introduce en la pestaña **Ubicación/Dirección** de la ventana **Terceros** para asociar cuentas bancarias específicas a las diferentes ubicaciones.  

!!!info
    En caso de tener tanto una cuenta bancaria predeterminada como una ubicación con una cuenta bancaria definida, al generar un nuevo documento, la cuenta bancaria de la ubicación tiene prioridad sobre la predeterminada.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/advanced-bank-account-management/aba2.png)

## Ventanas de Pedido de venta/Pedido de compra
:material-menu: `Aplicación` > `Gestión de Ventas` > `Transacciones` > `Pedido de venta`

:material-menu: `Aplicación` > `Gestión de Compras` > `Transacciones` > `Pedido de compra`

También se ha añadido un campo **Cuenta bancaria** en la sección de cabecera de las ventanas **Pedido de compra** y **Pedido de venta**.

Este campo se rellena automáticamente en función de la dirección seleccionada. Si hay una cuenta específica asociada a la dirección, se utiliza esa cuenta; si no hay ninguna cuenta configurada, se selecciona la cuenta predeterminada. En los casos en los que no esté configurada ninguna de las dos opciones, el campo permanece en blanco. Los planes de pago generados a partir de estos **Pedido de compra** y **Pedido de venta** ahora incluyen la información de la cuenta bancaria.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/advanced-bank-account-management/aba3.png)

#### Botón Añadir pago

Además, el botón **Añadir pago** se ha mejorado para incluir un campo **Cuenta bancaria**, lo que permite a los usuarios filtrar pagos por cuenta bancaria. Este botón está presente en las ventanas **Factura (Cliente)** y **Factura (Proveedor)**.


## Ventanas de Factura (Cliente)/Factura (Proveedor)

:material-menu: `Aplicación` > `Gestión de Ventas` > `Transacciones` > `Factura (Cliente)`

:material-menu: `Aplicación` > `Gestión de Compras` > `Transacciones` > `Factura (Proveedor)`

Del mismo modo, se ha añadido un campo **Cuenta bancaria** a las ventanas **Factura (Proveedor)** y **Factura (Cliente)**, que funciona de la misma manera que en los pedidos. El campo se rellena automáticamente en función de la dirección seleccionada, utilizando una cuenta específica si está asociada, recurriendo a la cuenta predeterminada si no se especifica ninguna, o permaneciendo en blanco en caso contrario. 
El plan de pagos hereda la información de la cuenta bancaria de la cabecera.
Además, las facturas creadas a partir de **Pedido de compra** y **Pedido de venta** heredan la información de la cuenta bancaria de los pedidos correspondientes.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/advanced-bank-account-management/aba4.png)

El **Plan de pagos** en las ventanas **Factura (Cliente)** y **Factura (Proveedor)** ahora muestra la información de la cuenta bancaria asociada en la pestaña **Plan de pagos**. 

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/advanced-bank-account-management/aba5.png)

#### Botón Añadir pago

Además, el botón **Añadir pago** se ha mejorado para incluir un campo **Cuenta bancaria**, lo que permite a los usuarios filtrar pagos por cuenta bancaria. Este botón está presente en las ventanas **Factura (Cliente)** y **Factura (Proveedor)**.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/advanced-bank-account-management/aba6.png)


#### Botón Modificar plan de pagos

En la pestaña **Plan de pagos** de las ventanas **Factura (Proveedor)** y **Factura (Cliente)** se encuentra el botón **Modificar plan de pagos**. Esta función permite a los usuarios modificar planes de pago ya creados, añadiendo o eliminando pagos, e incluso especificando la cuenta bancaria para cada registro del plan de pagos.

!!!warning
    Este botón solo está disponible cuando el plan de pagos no tiene pagos asociados.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/advanced-bank-account-management/aba7.png)

## Ventanas de Cobros/Pago
:material-menu: `Aplicación` > `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Transacciones` > `Cobros / Pago` 
### Botón Añadir detalles


Al igual que en el caso del botón **Añadir pago**, el botón **Añadir detalles** se ha mejorado para incluir un campo **Cuenta bancaria**, lo que permite a los usuarios filtrar pagos por cuenta bancaria. Este botón está presente en las ventanas **Cobros** y **Pago**.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/advanced-bank-account-management/aba8.png)

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.