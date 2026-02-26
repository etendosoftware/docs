---
title: Gestión de Datos Maestros
---

## Visión general

Esta sección describe el proceso de Gestión de Datos Maestros. Uno de los pasos a realizar durante la configuración de Etendo es definir los datos maestros que se utilizarán en otras áreas de la aplicación Etendo.

La Gestión de Datos Maestros ayuda a organizar y centralizar en un único repositorio los datos clave de la organización.

Disponer de un único repositorio de datos evita la duplicación de datos, proporciona una forma única de codificación de datos y es un aspecto clave para garantizar la coherencia y la trazabilidad de los procesos de negocio de cualquier tipo.

!!! info
    La creación de datos maestros es una parte del flujo general de Configuración del Negocio en Etendo y, como cualquier otra configuración, es necesaria antes de introducir transacciones.
## Vista general de terceros

:material-menu: `Aplicación` > `Gestión de Datos Maestros` > `Vista general de terceros`

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el módulo Advanced Business Partner del Essentials Bundle. Para ello, siga las instrucciones del marketplace: [Advanced Business Partner](https://marketplace.etendo.cloud/#/product-details?module=39AC2D9F72124AC7A1D0A3D005293C9E){target="_blank"}. Para más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Essentials Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/essentials-extensions/release-notes.md).

El módulo “Advanced Business Partner” permite al usuario disponer de una vista general de la información de los terceros y asignar números de secuencia a los terceros.

!!! info
    Para más información, visite [Advanced Business Partner](../../../../user-guide/etendo-classic/optional-features/bundles/essentials-extensions/advanced-business-partner.md) en la documentación del Essentials Extensions Bundle.
## Convertidores de moneda

:material-menu: `Aplicación` > `Gestión de Datos Maestros` > `Convertidores de moneda`

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el módulo Advanced Bank Account Management del Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}. Para más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

En esta ventana, puede configurar los ajustes de acceso para la configuración de la API de moneda. Para más información, visite: [Currency API Configuration - Guía del desarrollador](../../../../developer-guide/etendo-classic/bundles/financial-extensions-bundle/overview.md#currency-api-configuration)
## Terceros

:material-menu: `Aplicación` > `Gestión de Datos Maestros` > `Terceros`

### Visión general

La ventana de datos maestros de terceros es el lugar donde el usuario puede organizar y centralizar fácilmente los datos de terceros.

Etendo permite al usuario introducir la información de datos maestros de terceros cuando sea necesario a medida que se desarrolla la actividad empresarial; por lo tanto, el procedimiento descrito a continuación explica cómo configurar un único tercero de cualquier tipo.
### Cabecera

Aquí, el usuario puede definir y configurar terceros para utilizarlos posteriormente en transacciones.

![](../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/bp-header.png)

Campos a tener en cuenta:

- **[Grupos de Terceros](../master-data-management/business-partner-setup.md#business-partner-category)**: Campo clave para que el usuario seleccione una categoría a la que va a pertenecer el tercero, bajo los siguientes tipos:

    - Clientes
    - Proveedores
    - Operarios

- **Identificador**: o nombre corto que le ayudará a identificar y buscar un tercero determinado
- **Nombre comercial**
- **Nombre fiscal**: si se conoce. Si se conoce, es el que se utiliza en documentos oficiales como facturas e informes fiscales; en caso contrario, se utilizará el nombre comercial.
- **Descripción**: se utiliza para describir el tercero, si es necesario.
- **URL**: la URL del tercero, si se conoce.
- **Nº de referencia**: que puede utilizarse como una forma adicional de identificar un tercero.
- **Días consumo**: información que se utilizará al crear pedidos de venta o pedidos de compra para ese tercero en particular, mediante un proceso denominado *Copiar líneas*.  
    
    !!! info
        Para más información sobre este proceso, visite las secciones [Pedido de venta](../sales-management/transactions.md#sales-order) y [Pedido de compra](../procurement-management/transactions.md#purchase-order).

- **Crédito límite**: Etendo informará cuando se supere el límite de crédito introducido en este campo para el tercero al contabilizar facturas de venta.
- **Consentimiento para el Procesamiento de Datos del Cliente**: casilla de verificación en el modelo de datos de terceros, para reflejar si un contacto determinado consiente o no que sus datos puedan ser utilizados por la organización.
### Botones

**Establecer nueva moneda**

La moneda del tercero se completa automáticamente con la moneda de la **Tarifa** asignada al tercero. Una vez completada, puede cambiarse, si es necesario, utilizando el botón **Establecer nueva moneda**.

!!! note
    Normalmente, la moneda del tercero es la misma que la moneda de la tarifa asignada. Sin embargo, puede ocurrir que un tercero que tenga asignada, por ejemplo, una tarifa en EUR, tenga USD como moneda por defecto. En ese caso, todas las transacciones contabilizadas en EUR para ese tercero se convertirán a USD; por lo tanto, el saldo del tercero se calcula en USD.

El proceso **Establecer nueva moneda** permite definir:

- una nueva moneda para el tercero
- así como el tipo de cambio de moneda que se utilizará para convertir el saldo del cliente a la nueva moneda.

    ![](../../../../assets/drive/qMRCmdApUN-s9LYIxySdzxh9-vQezR1tP5kqzLUpO62BELBpiwE71zR3QJW9tn2RbSdVXCj5Po2IAXX5AzeBX4QkyQb6G6ns7jw4UTzPUMEeqUPYjfAjvO4jkMueDO_Ko1855ty312Mk3e2JPQ.png)

Campos a tener en cuenta:

- **Moneda**: aquí puede introducirse la nueva moneda del tercero, por ejemplo *EUR*. Al principio, la moneda mostrada en la ventana **Establecer nueva moneda** es la moneda de la tarifa del tercero; en nuestro ejemplo, *USD*.

- **Establecer importe**: casilla de verificación. Si se selecciona, Etendo actualizará el saldo del tercero con el importe introducido en el campo **Importe en moneda extranjera**, para que sea coherente con la nueva moneda.

- **Importe en moneda extranjera**: solo se muestra si se selecciona la casilla **Establecer importe**. Aquí, Etendo permite al usuario introducir manualmente el importe equivalente en la nueva moneda que sustituirá o actualizará el saldo del tercero.

- **Usar tipo de cambio por defecto**: casilla de verificación. Utiliza el tipo de cambio definido en la ventana [Rangos de conversión](../general-setup/application/conversion-rates.md) para recalcular el saldo del tercero de USD a EUR, en nuestro caso. Si esta casilla no está seleccionada, se muestra un nuevo campo *Índice* para permitir introducir un tipo de cambio específico.

Adicionalmente, un tercero puede tener **crédito disponible en una moneda determinada**. Si ese es el caso, Etendo informa al usuario porque el crédito disponible del tercero deberá convertirse a la nueva moneda; por lo tanto, podrá consumirse en la nueva moneda.

![alt text](../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/set-new-currency.png)

Este proceso crea automáticamente tres nuevos pagos, en caso de que el tercero tenga crédito disponible:

- un **pago de elemento de contabilidad** en EUR, que mueve el importe del crédito a la cuenta del libro mayor definida en el elemento de contabilidad seleccionado, en el *CRÉDITO*.
- un **pago reembolsado** en EUR, que mueve el importe del crédito a una cuenta de prepago en el *DÉBITO*.
- y un pago de importe **Cero** que es un pago de crédito en USD (nueva moneda). Este pago de crédito mueve el importe del crédito a una cuenta de prepago en el *CRÉDITO*.

!!! Example
  
    Tomemos como **ejemplo** un tercero que tiene una tarifa en EUR

    - Moneda de la tarifa: EUR
    - Saldo actual: 306.00 EUR
    - Crédito disponible: 100.00 EUR

    Como el crédito reduce el saldo, el saldo neto es 206.00 EUR (306.00 – 100.00).

    **Ejecutar Establecer nueva moneda**

    La empresa decide que este tercero debe operar ahora en USD, por lo que el usuario ejecuta el proceso **Establecer nueva moneda** y selecciona USD como nueva moneda.

    Etendo detecta que el tercero todavía tiene crédito disponible en EUR.
    Ese crédito debe convertirse a la nueva moneda, por lo que el sistema aplica el tipo de cambio 1 EUR = 1.19 USD.

    **Lo que Etendo hace automáticamente**

    Una vez finaliza el proceso:

    - La moneda del tercero cambia de EUR a USD.
    - El saldo actual pasa a ser 245.14 USD, calculado como 206.00 EUR × 1.19 = 245.14 USD
    - Etendo también crea tres pagos automáticos para mover correctamente el crédito disponible de EUR a USD, manteniendo la coherencia contable.

    **Transacciones futuras**

    Ahora que la moneda del tercero es USD, veamos qué ocurre con las nuevas facturas:

    - Usted crea una nueva factura de venta en EUR (porque la tarifa sigue estando en EUR).

        - Total de la factura: 41.50 EUR
        - Etendo la convierte a USD: 41.50 × 1.19 = 49.38 USD

    - El nuevo saldo del tercero pasa a ser: 245.14 + 49.38 = 294.52 USD

    - Más adelante, usted crea otra factura de venta en USD por 100.00 USD. Al completarla, Etendo muestra que el tercero tiene crédito disponible en USD, convertido desde el crédito anterior en EUR: 100 EUR × 1.19 = 119.00 USD

    ![alt text](../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/credit-usd.png)

    En resumen, el proceso **Establecer nueva moneda** actualiza la moneda del tercero y convierte saldos y créditos a la nueva moneda utilizando el tipo elegido; los saldos existentes y el crédito disponible se recalculan para que todo coincida con la nueva moneda y las transacciones futuras, incluso si se crean en la moneda anterior (EUR), seguirán convirtiéndose correctamente y reflejándose en la nueva moneda del tercero (USD).
### Solapas y subsolapas

No es lo mismo dar de alta y configurar un cliente que un proveedor/acreedor o un operario; por esa razón, la ventana Terceros tiene tres solapas principales y, por tanto, subsolapas que le permiten configurar cada tipo principal de tercero por separado:

- **Cliente** 
    - Contabilidad cliente
- **Proveedor**
    - Contabilidad proveedor
- **Operarios**
    - Contabilidad empleado

Las solapas y subsolapas mencionadas anteriormente se describen en los siguientes capítulos de esta sección.

!!! Important
    
    Podría haber otros tipos de terceros que requieran ser dados de alta como terceros en esta ventana; terceros que no tienen nada que ver ni con un cliente, ni con un proveedor/acreedor ni con un operario.

    Ese es el caso de los bancos. Los bancos deben crearse en la cabecera de la ventana de terceros introduciendo únicamente la información básica de cabecera y sin datos en ninguna de las solapas de la ventana de terceros, salvo Direcciones y Personas de contacto. La razón de esto es que los terceros de tipo *Banco* son necesarios en el flujo financiero de [Remesas](../financial-management/receivables-and-payables/transactions.md#remittance).

    Para más información sobre este flujo, visite [Cuenta financiera](../financial-management/receivables-and-payables/transactions.md#financial-account).
#### Cliente

!!! note
    Los datos relacionados con el cliente se pueden introducir y configurar una vez que se habilita la casilla **Cliente**.

![](../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/customer-tab.png)

Como se muestra arriba, existe una lista de datos relevantes que se deben introducir para los clientes junto con la información del saldo actual del cliente. Puede seleccionar cualquier dato, como por ejemplo la **Tarifa**, desde una lista de valores creada previamente o, si es necesario, crearlo navegando a la ventana correspondiente y, a continuación, seleccionarlo.

Campos a tener en cuenta:

- **Tarifa**: la seleccionada será la que se aplique al crear documentos de venta como pedidos de venta o facturas (Cliente) para ese cliente.  

    !!! info
        Para más información, visite [Tarifa](../master-data-management/pricing.md#price-list).

    Las tarifas se definen en una moneda determinada, que puede ser la misma que la moneda del cliente o no.  
    En caso de que no lo sea, el saldo del cliente se calculará teniendo en cuenta el tipo de conversión definido en la ventana [Rangos de conversión](../general-setup/application/conversion-rates.md) o el introducido en el proceso **Establecer nueva moneda**, que se puede ejecutar para cambiar la moneda de un tercero.

- **Método de pago**: el seleccionado será el que se aplique al crear y gestionar los cobros recibidos de ese cliente.  
    Si una **Cuenta financiera** está vinculada al cliente, el método de pago a seleccionar aquí será uno de los métodos de pago vinculados a la cuenta financiera.

    !!! info  
        Para más información, visite [Método de pago](../financial-management/receivables-and-payables/transactions.md#payment-method).

- **Condiciones de pago**: la seleccionada será la que se utilice al gestionar el plan de pagos de las facturas (Cliente).

    !!! info
        Para más información, visite [Condiciones de pago](./business-partner-setup.md#payment-term).

- **Cuenta financiera**: la seleccionada será la que se utilice al cobrar y conciliar los pagos realizados por ese cliente. 

    !!! info
        Para más información, visite [Cuenta financiera](../financial-management/receivables-and-payables/transactions.md#financial-account).

- **Facturación**: existen algunos términos de facturación que se pueden utilizar al generar facturas (Cliente).

    !!! info
        Para más información, visite [Facturar](../sales-management/transactions.md#generate-invoices).

    - **Después de entregar el pedido**: la factura podría generarse automáticamente una vez que se hayan enviado todos los bienes del pedido de venta.
    - **Después de la entrega**: los bienes del pedido de venta se facturarán automáticamente a medida que se envíen, incluso si hay envíos parciales.
    - **No facturar**: no se generará ninguna factura automáticamente.
    - **Inmediato**: la factura se generará en la siguiente ejecución del proceso **Facturar**.
    - **Calendario del cliente después de la entrega**: la factura se generará de acuerdo con el calendario acordado con el cliente y una vez que se hayan enviado los bienes pedidos. Si esta es la opción seleccionada, se muestra automáticamente un nuevo campo denominado *Calendario de facturación* para que seleccione el *Calendario de facturación* o calendario correspondiente.

        !!! info 
            Para más información, visite [Calendario de facturación](../master-data-management/business-partner-setup.md#invoice-schedule).

- **Crédito límite**: si la suma de todos los pagos pendientes supera el límite de crédito especificado para un cliente, el sistema le avisará indicando que este cliente ha alcanzado el límite de crédito cada vez que se seleccione este tercero en un documento de venta (pedido, albarán o factura).

- **Exento de impuestos**: para definir un cliente como exento de impuestos cuando corresponda; por lo tanto, solo se aplican aquellos tipos impositivos que también estén definidos como exentos.

- **Agente comercial**: aquí, el usuario puede seleccionar un agente comercial del cliente. Un agente comercial es un empleado configurado como tal.

- **Bloqueo de proveedor**: esta casilla permite bloquear un cliente, por lo que algunos documentos específicos no se pueden completar para él. Si está marcada, se muestra la sección de bloqueo con la siguiente configuración, que obviamente se puede cambiar según sea necesario:
    - **Pedido de venta:** bloqueado
    - **Albarán (Cliente):** bloqueado
    - **Factura (Cliente):** bloqueado
    - **Cobros:** no bloqueado

    La configuración predeterminada anterior significa que no es posible completar un pedido de venta, un albarán (Cliente) o una factura (Cliente) para el cliente; solo es posible recibir un cobro.

Sección **Más información**

- **Categoría Imp. Tercero**: este campo se puede encontrar en la sección *Más información*.  
    Puede utilizar una categoría de impuestos de terceros para conseguir que los documentos de venta creados para un cliente solo puedan tener un conjunto específico de tipos impositivos vinculados a esa categoría de impuestos.  
    
    !!! info
        Para más información, visite [Categoría de Impuestos de Terceros](../financial-management/accounting/setup/business-partner-tax-category.md).

- **Día de vencimiento**: indica el día del mes, el primer vencimiento, en el que vencen las facturas.

- **2ndo día de vencimiento**: indica el día del mes, el segundo vencimiento, en el que vencen las facturas.

- **3er día de vencimiento**: indica el día del mes, el tercer vencimiento, en el que vencen las facturas. 

- **Cumpleaños**: datos sobre el cliente.

- **Lugar de Nacimiento**: datos sobre el cliente.

**Contabilidad cliente**

La solapa **Contabilidad cliente** permite al usuario configurar las cuentas contables que se utilizarán al contabilizar transacciones relacionadas con el cliente, como los cobros de clientes y los anticipos de clientes, en el libro mayor.

![](../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/customer-accounting-tab.png)

Como se muestra arriba, puede configurar, para cada cliente y libro mayor, las cuentas que se utilizarán en:

- las transacciones de **Cuentas a cobrar de clientes**, como la contabilización de facturas (Cliente).

    !!! info  
        Para más información, visite [Factura (Cliente)](../sales-management/transactions.md#sales-invoice).

- las transacciones de **Prepago del cliente**, como aquellos casos en los que la empresa que envía los bienes requiere que el cliente adelante una parte o la totalidad del importe de la deuda.  

Inicialmente, estas cuentas se heredan de las cuentas predeterminadas del libro mayor de la organización para el que se está creando el tercero. El usuario siempre puede cambiarlas.

!!! important
    Es posible configurar la creación de nuevas cuentas correlativas para los terceros tal y como se describe en la solapa Libro mayor de la ventana [Organización](../general-setup/enterprise-model/organization.md).
#### Proveedor/Acreedor

!!! note
    Los datos relacionados con el proveedor o acreedor se pueden introducir y configurar una vez que se habilita la casilla **Proveedor**.

![](../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/vendor-tab.png)

Como se muestra en la imagen anterior, existe una lista de datos relevantes que deben introducirse para proveedores o acreedores, también conocidos como proveedores:

- **Tarifa de compra**: la seleccionada será la que se aplique al crear documentos de compra como pedidos de compra o facturas para ese proveedor.  
    Si un Tercero ya ha generado Crédito, no será posible seleccionar una Tarifa en una Moneda diferente de la del Crédito generado. En ese caso, es posible convertir el Crédito a una Moneda diferente.  
    
    !!! info
        Para más información, visite [Tarifa](../master-data-management/pricing.md#price-list).

- **Método de pago**: el seleccionado será el que se aplique al crear y gestionar los pagos realizados a ese proveedor.  
    Si una cuenta financiera está vinculada al proveedor, el método de pago a seleccionar será un método de pago vinculado a esa cuenta financiera.  
  
    !!! info
        Para más información, visite [Método de pago](../financial-management/receivables-and-payables/transactions.md#payment-method).

- **Condiciones de pago**: la seleccionada será la que se utilice al gestionar los planes de pago de facturas de proveedor. 

    !!! info
        Para más información, visite [Condiciones de pago](../master-data-management/business-partner-setup.md#payment-term).

- **Día de vencimiento**: tal y como se indica en las Condiciones de pago, el Día de vencimiento de la OC se utiliza en combinación con la Fecha de vencimiento fija en las condiciones de pago, que debe establecerse en Y, y con el Día laborable siguiente establecido en N. La fecha de vencimiento del pago se basa en las condiciones de pago definidas en combinación con el Día de vencimiento de la OC.
    
    !!! example
        Por ejemplo, la condición de pago definida es de 30 días y el Día de vencimiento se establece en 10. Si la fecha de la factura es el día 1 del mes, en base a la condición de pago de 30 días, la fecha de vencimiento del pago es el día 1 del mes siguiente, pero como el Día de vencimiento está establecido en 10, la fecha de vencimiento del pago resultante es el día 10 del mes siguiente.

- **Día de vencimiento 2**: se puede establecer un segundo Día de vencimiento de la OC para combinarlo con las condiciones de pago y el primer Día de vencimiento de la OC.
    
    !!! example
        Por ejemplo, la condición de pago es de 30 días, el valor del Día de vencimiento es 10 y el Día de vencimiento 2 es 20. El ejemplo indicado en Día de vencimiento permanecerá igual. Sin embargo, si la fecha de la factura es el día 11 del mes, la fecha de vencimiento del pago será el día 20 del mes siguiente: se tienen en cuenta los 30 días de las condiciones de pago y, dado que ya se ha superado el día 10 del mes, se tiene en cuenta el segundo vencimiento del día 20.

- **Día de vencimiento 3**: se puede establecer un tercer Día de vencimiento de la OC para combinarlo con las condiciones de pago y el primer y segundo Día de vencimiento de la OC.

- **Cuenta financiera**: la seleccionada será la que se utilice al retirar y conciliar los pagos realizados a un proveedor.

    !!! info
        Para más información, visite [Cuenta financiera](../financial-management/receivables-and-payables/transactions.md#financial-account).

- **Categoría de Impuesto**: puede utilizar una categoría de impuestos de terceros para conseguir que los documentos de compra registrados de un proveedor solo puedan tener un conjunto específico de tipos impositivos vinculados a esa categoría de impuestos.  
    
    !!! info
        Para más información, visite [Categoría de Impuesto](../financial-management/accounting/setup/tax-category.md).

- **Bloqueo de proveedor**: esta casilla permite bloquear un proveedor, por lo que algunos documentos específicos no podrán completarse para él. Si está marcada, se muestra la sección Bloqueo de proveedor con la siguiente configuración, que puede modificarse según sea necesario:

    - **Pedido de compra:** Bloqueado
    - **Albarán (Proveedor):** No bloqueado
    - **Factura (Proveedor):** Bloqueado
    - **Pago:** Bloqueado

    La configuración predeterminada anterior significa que no es posible completar ni un pedido de compra, ni una factura de proveedor, ni realizar un pago, pero sí recibir mercancía enviada por el proveedor.

    Como ya se ha mencionado, si un tercero de cualquier tipo está bloqueado, no es posible Completar (o contabilizar) algunos tipos de documento. Sin embargo, siempre es posible Anularlos. Etendo muestra un mensaje de error indicando que no es posible completar un documento para un tercero establecido como **bloqueado**.

**Contabilidad proveedor**

La solapa Contabilidad proveedor permite al usuario configurar las cuentas contables que se utilizarán al contabilizar transacciones relacionadas con el proveedor, como pasivos del proveedor y pagos por adelantado del proveedor, en el libro mayor.

![](../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/vendor-accounting-tab.png)

El usuario puede configurar, para cada proveedor o acreedor y para el esquema contable disponible, las cuentas contables que se utilizarán en:

- las transacciones de **Pasivo del proveedor**, como la contabilización de facturas de compra.  
    
    !!! info
        Para más información, visite [Factura (Proveedor)](../procurement-management/transactions.md#purchase-invoice).

- las transacciones de **Pagos por adelantado del proveedor**, como aquellos casos en los que el proveedor de los bienes requiere que la empresa pague por adelantado una parte o la totalidad del importe de la deuda.  
    
    !!! info
        Para más información, visite [Pagos por adelantado del proveedor](../financial-management/receivables-and-payables/transactions.md#payment-out).

Inicialmente, estas cuentas se heredan de las cuentas por defecto del Esquema contable asignado a la Organización para la que se está creando el tercero. El usuario siempre puede cambiarlas.

!!! important
    Es posible configurar la creación de nuevas cuentas correlativas para los terceros que se están creando, tal y como se describe en la solapa Org Schema de la ventana [Organización](../general-setup/enterprise-model/organization.md).
#### Operarios

!!! note
    Un tercero puede configurarse como operario una vez que se habilita la casilla de verificación **Operarios**.

![](../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/employee-tab.png)

La solapa Operarios permite al usuario establecer cuáles de sus terceros son *Operarios*.

Un operario puede:

- ser designado como **Agente comercial** de un cliente.

- definirse como el **responsable de uno o varios proyectos de la empresa**.  
     
    !!! info
        Para más información, visite [Projects and Services Management](../project-and-service-management/getting-started.md).

- asignarse a un **proceso de producción** como un recurso.  
     
    !!! info
        Para más información, visite [Gestión de Producción](../production-management/getting-started.md).

- y puede **emitir informes de gasto** como parte de su participación en un proyecto de la empresa.  
     
    !!! info
        Para más información, visite [Informe de gasto](../project-and-service-management/transactions.md#expense-sheet).

**Contabilidad empleado**

En esta solapa, el usuario puede añadir las cuentas contables que se utilizarán al contabilizar transacciones relacionadas con operarios, como la contabilización de nóminas.

![](../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/employee-accounting-tab.png)

Como puede ver en la imagen anterior, actualmente no es necesario definir ninguna cuenta contable para la contabilidad de operarios. Esto se debe a que no existe ninguna transacción susceptible de contabilizarse para operarios.

En cualquier caso, este es el lugar al que deberían apuntar los módulos o funcionalidades relacionados con *Recursos Humanos* al definir las cuentas que se utilizarán en cualquier transacción de operarios susceptible de contabilizarse.

**Categoría salarial**

En esta solapa, el usuario puede configurar la categoría salarial del operario seleccionando una de las opciones que se definieron previamente en la ventana [Categoría Salarial](../master-data-management/business-partner-setup.md#salary-category).

![](../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/cost-salary-category.png)
#### Cuenta bancaria

La solapa **Cuenta bancaria** permite al usuario listar y configurar las cuentas bancarias de terceros.

Es posible configurar y establecer correctamente las cuentas bancarias de terceros para que se utilicen al realizar o recibir pagos de terceros de cualquier tipo.

!!! important
    Se recomienda encarecidamente que el usuario configure correctamente las cuentas bancarias, ya que Etendo las utilizará según sea necesario dentro de los procesos de gestión de pagos de Etendo.

![](../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/bank-account-tab.png)

Campos a tener en cuenta:

- **Nombre**
- Indicador **Activo**: se recomienda mantener solo una cuenta bancaria como **Activo** para evitar errores; de lo contrario, asegúrese de que se utilice la cuenta bancaria correcta.
- **País**: aquí, el usuario puede seleccionar un país de la lista para especificar si la cuenta bancaria es una cuenta bancaria nacional o una cuenta bancaria extranjera.
- **Usuario/Contacto**: en caso de que quiera asociar un contacto a esta cuenta bancaria.
- **Formato cuenta bancaria**: lista que contiene todos los valores posibles para generar la **Cuenta mostrada**, que posteriormente será utilizada por otros informes o procesos para obtener el identificador de la cuenta. Los valores posibles son:
    - _Usar nº de cuenta genérico._
    - _Mostrar IBAN_
    - _Usar SWIFT + nº de cuenta genérico._

    !!! note
        Otros módulos que amplían el **Formato cuenta bancaria** soportado pueden añadir otras opciones.

- **Generic Account No**: aquí se puede introducir un número de cuenta genérico para identificar la cuenta bancaria. Este campo debe informarse obligatoriamente en caso de que se seleccione _Usar nº de cuenta genérico._ o _Usar SWIFT + nº de cuenta genérico._ en el campo **Formato cuenta bancaria**.

- **IBAN**: el International Bank Account Number (IBAN) es un estándar internacional para la numeración de cuentas bancarias.  
    El IBAN consta de un código de país ISO 3166-1 de dos letras, seguido de dos dígitos de control y de hasta treinta caracteres alfanuméricos para el número de cuenta bancaria nacional, denominado BBAN (Basic Bank Account Number). Este campo debe informarse obligatoriamente en caso de que se seleccione _Mostrar IBAN_ en el campo **Formato cuenta bancaria**. El código IBAN se validará automáticamente al insertar/actualizar el registro, teniendo en cuenta las reglas definidas para el banco del país.
- **Código Swift**: corresponde al identificador del código bancario internacional ISO 9362. Debe informarse obligatoriamente en caso de que se seleccione _Usar SWIFT + nº de cuenta genérico._ en el campo **Formato cuenta bancaria**.
- **Cuenta mostrada**: se genera automáticamente en función del valor seleccionado en **Formato cuenta bancaria**. Este campo es de solo lectura y lo utilizan otros informes o procesos.

**Gestión avanzada de cuentas bancarias**

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el módulo Advanced Bank Account Management del Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

Esta funcionalidad introduce la posibilidad de marcar una cuenta bancaria como **Valor por defecto** dentro de la solapa **Cuenta bancaria** de la ventana **Terceros**. Aquí es posible marcar la casilla **Cuenta por defecto** para establecer la cuenta que se utilizará en los documentos para diferentes transacciones.

![](../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/advanced-bank-account-tab.png)

!!! note
    Si no se selecciona ninguna cuenta bancaria como predeterminada, se utiliza la última creada cuando no se selecciona ninguna cuenta bancaria en pedidos/facturas.

!!! warning
    Solo puede seleccionarse una cuenta bancaria como predeterminada para cada tercero.
#### Tipo de documento

<iframe width="560" height="315" src="https://www.youtube.com/embed/8-MOprz-4FI?si=rc5geP_xaKmKvjsK" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

!!! info
    Esta funcionalidad está disponible en Etendo 25.3 o versiones posteriores.

Esta solapa introduce flexibilidad al personalizar las asignaciones de tipo de documento a facturas, pedidos, albaranes y recepciones, específicamente en función del tercero.

![](../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/document-type.png)

Esta funcionalidad proporciona un control granular sobre la asignación de documentos transaccionales, sobrescribiendo el tipo de documento por defecto configurado a nivel de organización. Esto es útil, ya que cada país, región e incluso cada empresa puede utilizar diferentes tipos de documentos con sus respectivos números de secuencia imprimibles e incluso personalizados.

Cuando se crea un documento de transacción (pedido, factura, albarán o recepción) y se vincula a un tercero, el sistema primero comprueba la solapa **Tipo de documento** para obtener la configuración correcta. Esta configuración puede mejorar significativamente la experiencia del usuario cuando los documentos se crean repetidamente.

![](../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/document-type2.png)

Campos a tener en cuenta:

1. **Organización**: Especifica la organización a la que se aplica esta regla específica de asignación de documentos (p. ej., F&B US Inc.).
2. **Tipo doc. base**: Seleccione el tipo de documento de transacción, como pedido, factura o albarán/recepción.
3. **Operación de venta**: Casilla de verificación utilizada para distinguir la dirección del documento.

    - Marcada: Corresponde a documentos de ventas (p. ej., pedidos de venta, facturas de venta, albaranes (Cliente)).
    - Desmarcada: Corresponde a documentos de compras (p. ej., pedidos de compra, facturas de compra, albaranes (Proveedor)).

4. **Tipo de documento**: Seleccione el tipo de documento específico disponible para la categoría elegida y la dirección de la transacción.

**Prioridad de selección del tipo de documento**

1. Coincidencia exacta: Etendo busca una regla directa definida para el tercero y la organización específica.
2. Árbol organizativo: Si no se encuentra una coincidencia exacta, Etendo navega hacia arriba por el árbol organizativo para encontrar una coincidencia.
3. Por defecto: Si no existe ninguna regla, Etendo utiliza el tipo de documento por defecto configurado para la organización.

!!! warning
     Esta funcionalidad no está disponible para documentos creados mediante un proceso en segundo plano/botón como “Facturar desde albarán” en la ventana **Albarán (Cliente)**. En este caso, el tipo de documento que se utilizará es el definido a nivel de organización, en lugar del definido a nivel de la solapa **Tipo de documento**.
#### Direcciones

Las ubicaciones de terceros y los detalles completos de la dirección pueden configurarse en esta solapa.

Los terceros pueden tener diferentes detalles de dirección en función de la dirección/ubicación utilizada, ya sea para fines de *Albaranes (Proveedor)/(Cliente)* o para fines de *Facturas*.

![](../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/location-address.png)

Campos a tener en cuenta:

- **Direcciones**: Si hace clic en este campo, se abre el cuadro selector de ubicación, donde puede introducir la siguiente información:
    - la **1ª línea de dirección**
    - la **2ª línea de dirección**, si es necesario
    - el **Código postal de la cuenta**
    - la **Población en que está domiciliada la cuenta**
    - el **País**: se puede seleccionar uno de la lista, si existe
    - la **Provincia**: una vez seleccionado el país, puede seleccionar una provincia del país seleccionado, de la lista, si existe.

- **Teléfono**: El número de teléfono para contactar con el tercero.
- **Teléfono alternativo**: para un teléfono alternativo, si existe.
- **Nombre**: Referido al nombre de la dirección. Este campo se completa automáticamente por Etendo, una vez que la información de Direcciones ha sido configurada. El usuario puede cambiarlo según sea necesario.
- **Fax**: El número de fax para contactar con el tercero.
- Casilla **Dirección de envío**: El usuario debe marcarla si la dirección que se está configurando debe utilizarse para transacciones relacionadas con Albaranes (Proveedor)/(Cliente).
- Casilla **Dirección de facturación**: El usuario debe marcarla si la dirección que se está configurando debe utilizarse para transacciones de facturas de venta o compra.

**Gestión avanzada de cuentas bancarias**

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el módulo Advanced Bank Account Management del Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

El campo Gestión avanzada de cuentas bancarias se introduce en la solapa Direcciones de la ventana Terceros para **asociar cuentas bancarias específicas** a las diferentes ubicaciones.

!!! warning
    En caso de tener tanto una cuenta bancaria por defecto como una ubicación con una cuenta bancaria definida, al generar un nuevo documento, la cuenta bancaria de la ubicación tiene prioridad sobre la cuenta por defecto.

![](../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/location-address-abam.png)
#### Personas de contacto

La solapa **Personas de contacto** permite al usuario añadir y configurar los contactos del tercero con los que usted trabaja.

![](../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/contact.png)

Campos a tener en cuenta:

- **Nombre** y **Apellidos** del contacto.
- **Correo electrónico** del contacto.
- **Teléfono** del contacto.
- **Observaciones**: para introducir información adicional.
- **Cargo** en el tercero.
- Indicador **Activo**: para indicar si este contacto está disponible para su uso o deshabilitado. 
- **Autorización comercial**: esta casilla de verificación se selecciona para indicar si el cliente desea o no recibir información comercial de la organización.
#### Descuentos

La solapa **Descuentos** permite al usuario añadir y configurar los descuentos de terceros.

![](../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/master-data/basic-discount.png)

Es posible introducir tantos **Descuento** como se hayan acordado con sus terceros, completando la siguiente información:

- el **Descuento** que se aplicará al crear transacciones de venta/compra para ese tercero puede seleccionarse de la lista (si existe) o crearse navegando a la ventana **Descuento**.
- **Cliente:** esta casilla debe seleccionarse si el descuento se va a aplicar a un Tercero configurado como *Cliente*.
- **Proveedor:** esta casilla debe seleccionarse si el descuento se va a aplicar a un Tercero configurado como *Proveedor*.
- **Aplicar en pedido:** esta casilla debe seleccionarse en caso de que el descuento pueda aplicarse en pedidos de venta o de compra, según corresponda.
- Cálculo **En cascada** del descuento. Por ejemplo, si el primer descuento es del 10% y el segundo del 5%, un cálculo en cascada del descuento total no será del 15% sino del 14,5%.

    Un descuento no aplicado **En cascada** significa que afecta a la cantidad total de la línea del documento. Un descuento aplicado **En cascada** significa que afecta a la cantidad de la línea del documento que queda tras aplicar todos los descuentos anteriores.

    !!! example
        Un ejemplo para explicar la diferencia entre un descuento **En cascada** y uno que no es **En cascada** es el siguiente:

        Tres **Descuento**, cada uno del 10%; los dos primeros se definen como no **En cascada** y el tercero como **En cascada**. Sobre una línea de factura de 1.000 USD:

        - El primer descuento creará una línea de -100 USD (10% de 1.000 USD)
        - El segundo descuento también creará una línea de -100 USD (10% de 1.000 USD)
        - El tercero, sin embargo, creará un descuento basado en aplicar los descuentos anteriores en cascada, por lo que:
        - 1.000 USD - 10% = 900 USD (aplicando el 1er descuento **En cascada**)
        - 900 USD - 10% = 810 USD (aplicando el 2º descuento **En cascada**)
        - 10% de 810 USD = 81 USD. Por lo tanto, el tercer descuento será de -81 USD.
        - En total -100 -100 -81 = -281 USD para los tres descuentos (un descuento total del 28,1%)
#### Configuración de Rappel

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el módulo Advanced Rappels del Sales Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Sales Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=22CF01FC620140A6AA92CF550EB8DA36){target="_blank"}. Para más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Sales Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/sales-extensions/release-notes.md).

Los rappels son descuentos basados en el volumen de consumo de un tercero en un periodo de tiempo determinado. Esta funcionalidad permite al usuario configurar y conceder rappels a terceros.

Con esta funcionalidad, se muestra la solapa “Configuraciones de Rappel” en los terceros incluidos en las configuraciones de Rappel. Además, en la ventana Terceros, el usuario puede crear rappels mediante el botón **Crear Rappel**.

![bp_window.png](../../../../assets/legacy/bp_window.png)

Para poder hacerlo, es necesario configurar determinados aspectos en la ventana **Configuraciones de Rappel**.

!!! info
    Para más información, visite [Configuraciones de Rappel](../master-data-management/business-partner-setup.md#rappel-configurations).

La solapa **Configuración de Rappel** se puede encontrar en la sección de solapas de la ventana Terceros. En esta solapa, el usuario puede encontrar los rappels configurados para cada tercero.

Para crear un nuevo rappel, el usuario debe seleccionar una de las configuraciones disponibles en esta solapa y hacer clic en el botón **Crear Rappel**. Aparecerá una ventana emergente en la que el usuario puede seleccionar un tercero al que se asignará el Rappel, y también configurar un periodo de fechas en el que se tendrán en cuenta los consumos para calcular los descuentos, determinado por la información *fecha desde* y *fecha hasta*.

![bp_pop_up_new.png](../../../../assets/legacy/bp_pop_up_new.png)

Cuando se crea el rappel, se crea automáticamente una factura de venta, como se muestra a continuación.

![created_rappel.png](../../../../assets/legacy/created_rappel.png)

Cada vez que se concede un rappel a un tercero, se genera automáticamente una nueva factura de venta para mostrar el importe del descuento. Esta factura tiene una secuencia específica para distinguirla del resto, según las opciones introducidas al configurar la secuencia, y un importe negativo, ya que se trata de un descuento. Esta factura está en estado Borrador.

!!! info
    Para más información, visite [Factura (Cliente)](../sales-management/transactions.md#advanced-rappels).
## Información de terceros

:material-menu: `Aplicación` > `Gestión de Datos Maestros` > `Información de terceros`

#### Visión general

En esta sección, el usuario puede ver información relacionada con los pedidos, albaranes/recepciones, facturas y activos de terceros.

### Elegir tercero

El usuario puede seleccionar un tercero para comenzar a ver las transacciones relacionadas.

![](../../../../assets/drive/4OnjuhWdUoTUGTSu8zWxiV2-AAuj2bKugSYsd0tnIK9CgAS12oX62u4KgxFW35THxZKqIH0Epr-E-q5w4w4y4kbkWR3wCKNTQFosue5bPRC3CMXbOgCNgkzsvXCtZ7OsB53ZD69KhpH-BmTZbQ.png)

#### Pedidos tercero

El usuario puede ver los pedidos relacionados con un tercero específico.

![](../../../../assets/drive/pwcD_Hw4nDDMhW7FDa69spb3uNGrBrfB8AwS8Ni77RyIi6_uPAsIWmWPzkvPoCBe5IIcW_GeFmxgvB4KPxoI6TmwiK2nAsFyOKd7GvbMXzpAyt2DwTPDnyKijbLgejiWZYCnj28D9-y9hZNuDw.png)

### Albaranes tercero

El usuario puede ver los albaranes relacionados con un tercero específico.

![](../../../../assets/drive/DKEnqi6tY-_9PGf13-ntaqJCDwbfHlm8mJl2k4WwaIJ8dZibpai1E-LZhuf8DkUS4dSX2sm5eua0uzGLLdXreV-YW1KnyHvSI1zWRcJDHEjh0DJVslYgN3RBEuTiqjK0g5qpe02UP8ZUf24qyw.png)

### Facturas tercero

El usuario puede ver las facturas relacionadas con un tercero específico.

![](../../../../assets/drive/GVk5WiJ9CXXVM8khajRov6_24IGCsm0l8nD6ARDMyUL6Os5gle_r3LDHUsq1i-2lAXyf5aZRlgxep-kCgSGkbjMCoGNKVMCDwp-R5Z2pK1-5VYxgk4bswYEc4tcJ_iZGuh5Toi2DcEQIWz9Lsw.png)
## Producto

:material-menu: `Aplicación` > `Gestión de Datos Maestros` > `Producto`

#### Visión general

La ventana de datos maestros de producto es el lugar donde puede organizar y centralizar fácilmente los datos clave de los artículos de cualquier tipo que pueda gestionar como parte de los procesos y/o actividades de la organización.

Las organizaciones gestionan una variedad de artículos diferentes que pueden ser necesarios para el desempeño de sus actividades diarias.

Es posible cargar información de **Producto** en Etendo de forma masiva usando el módulo Import Data, o uno a uno usando la ventana **Producto**.

Esta sección describe cómo configurar **Productos** individualmente.

#### Producto

La ventana **Producto** permite la creación de artículos tales como productos, materias primas, recursos, servicios, etc.

La información requerida para crear un **Producto** en Etendo viene determinada por la naturaleza del **Producto**, su tipo de producto.

Hay cuatro tipos de producto disponibles:

- **Artículo**. El tipo de producto más utilizado es *Artículo*. El inventario mantenido para reventa, los materiales que se incorporan a un proceso de producción y los productos semielaborados o terminados creados mediante producción son ejemplos de productos definidos usando el tipo de producto *Artículo*.
  - Un artículo debe marcarse como ***Almacenado*** si se requiere el seguimiento de cantidades del artículo; en caso contrario, no es necesario marcarlo como *Almacenado*.
  - Un artículo debe marcarse como ***Producción*** si el artículo se utiliza en fabricación.
  - Si un artículo es un producto intermedio o terminado, su lista de materiales (BOM) debe detallarse en la solapa **Lista de materiales**.
- **Servicios**. Este tipo de producto se utiliza para identificar prestaciones como servicios profesionales, transporte, telefonía y otros artículos que no se corresponden con bienes materiales.
  - Por lo tanto, un servicio no es almacenable, pero puede comprarse o venderse.
  - Un servicio puede tener una lista de materiales que se definirá en la solapa **Lista de materiales**.
- **Recurso** y **Gasto**. Estos tipos de producto pueden utilizarse para distinguir entre diferentes tipos de productos que pueden comprarse o venderse, pero no pueden almacenarse.
  - El tipo Recurso puede utilizarse para configurar recursos como recursos financieros, legales o naturales utilizados por la organización.
  - El tipo Gasto puede utilizarse para configurar gastos como gastos de viaje que se usarán al informar los gastos de **Operarios**.

Los tipos de producto no confieren tratamientos contables diferentes. En otras palabras, todos los tipos de producto contabilizan de la misma manera al comprarse, almacenarse o venderse.

Todos ellos utilizan las cuentas del libro mayor definidas en la solapa **Contabilidad** de la ventana **Producto**.

![](../../../../assets/drive/BP3_HION2Ye59yb2o2KNzsNK4o72pdd_v6DVNj5SsrL_3bZCZbH-OG4Snsia_DB_BItoQaJxuJf4vOe1jlrwPhZTswRuf1I8aUTCLlHP1s-NU-625ScthOFj8fgeIrknNz2MdE6kbDgecxTFSw.png)

Los datos clave adicionales a completar son:

- **Unidad**, es decir, la unidad de medida que se utilizará al comprar, almacenar y vender un producto, por ejemplo *Unidades*.  
  Un producto también puede tener unidades alternativas además de la unidad del producto.
- **Categoría del producto**, es obligatorio seleccionar una categoría del producto a la que pertenecerá el producto.  
  Para saber más, visite Categoría del producto
- **Categoría de Impuesto**, esta categoría es clave para gestionar los impuestos relacionados con el producto. Impuestos como el IVA dependen del tipo de producto.  
  Para saber más, visite Categoría de Impuesto
- La casilla **Compra** puede seleccionarse para indicar que el producto puede comprarse a un proveedor externo. Esta casilla es principalmente informativa, ya que no añade lógica de negocio por sí misma, salvo en lo relativo a MRP.  
  En ese caso, si está seleccionada, MRP comprará el producto si es necesario; en caso contrario, lo producirá.
- La casilla **Ventas** puede seleccionarse para indicar que el producto se vende o puede venderse a terceros o clientes externos. Esta casilla es informativa, ya que no añade lógica de negocio por sí misma.
- La casilla **Almacenado** se selecciona si el producto forma parte del inventario; por lo tanto, se registran en Etendo las transacciones de movimientos de inventario correspondientes.  
  Este indicador ya no puede modificarse para un producto si dicho producto forma parte de cualquier documento relacionado con ventas, compras, inventario o producción, independientemente del estado del documento.
- La casilla **Producción** se selecciona si el producto forma parte de un proceso de producción. Una vez seleccionada, aparece un campo adicional para seleccionar un *Plan de Producción*.  
  Para saber más, visite [Plan de Producción](../production-management/setup.md#process-plan)
- **Conjunto atributos**, un producto puede tener un grupo de características o un conjunto de atributos, como ***Color y talla***, a tener en cuenta al pedir o almacenar el producto.
  - Si aquí se selecciona un **Conjunto atributos**, Etendo muestra un nuevo campo llamado *Valor atributos*.  
    Para saber más, visite Conjunto atributos
- **Valor atributos**, si se selecciona un valor del conjunto de atributos como *Azul y grande*, Etendo muestra un nuevo campo llamado *Usar conjunto de atributos como*.
- **Usar conjunto de atributos como**, una vez seleccionado un conjunto de atributos, este puede utilizarse como se describe a continuación según el criterio seleccionado en este campo:
  - **Valor por defecto**: significa que el valor del conjunto de atributos definido se establecerá por defecto en cada transacción, pero se permite cambiarlo.  
    En otras palabras, el usuario no tendrá que preocuparse de configurarlo cada vez que cree transacciones como albaranes de entrada y salida.
    - Por ejemplo, puede configurarse para que el valor por defecto del atributo Talla de un producto sea Mediana (porque es el más utilizado).  
      De este modo, cada vez que se seleccione ese producto, su valor de conjunto de atributos se establecerá en Mediana (salvo que se seleccione desde stock, en cuyo caso el valor del conjunto de atributos se establece en el valor con el que el producto está almacenado).  
      Es posible sobrescribir este valor del conjunto de atributos, a Pequeña o Grande, por ejemplo.
  - **Sobrescribir especificación**: significa que el valor del conjunto de atributos especificará completamente el producto; no obstante, el valor del conjunto de atributos puede cambiarse para este producto.
    - Por ejemplo, al producto Cerveza sin alcohol se le asigna el conjunto de atributos Graduación alcohólica y el valor del conjunto de atributos 0% en la ventana **Producto**. Esta definición especifica completamente el producto: se supone que la Cerveza sin alcohol tiene una graduación alcohólica del 0%. Pero, en el proceso de producción, pueden producirse desviaciones y esta graduación puede pasar a 0,01%. Usando la opción Sobrescribir especificación, el responsable de producción podrá registrar esta desviación en el proceso de **Producción** para el producto Cerveza sin alcohol.
  - **Especificación**: significa que el valor del conjunto de atributos especificará completamente el producto. El valor del conjunto de atributos siempre tendrá este valor y no se permitirá ningún otro valor.
    - Por ejemplo, al producto Vaqueros grandes azules se le asigna el conjunto de atributos Talla y Color con los valores Grande y Azul. Esto define el producto y no cambiará. Las transacciones se realizan y completan con este producto, sin obligar a volver a establecer el valor del conjunto de atributos. El usuario puede entonces consultar todos los productos que tengan talla Grande o color Azul sin tener que consultar las transacciones, sino únicamente la definición del producto.  
      Para saber más sobre atributos, visite el artículo Cómo gestionar atributos y conjuntos de atributos.
- **UPC/EAN**, utilizado para almacenar información de código de barras
- La casilla **Lista de materiales** se selecciona cuando el producto es un paquete de otros productos, tal como se lista en la solapa **Lista de materiales**.
- **Ingreso postpuesto**: este indicador solo es visible para productos con el indicador **Ventas** marcado e indica que, _por defecto_, los ingresos por ventas de este producto deben diferirse. Cuando este indicador está marcado, se hace visible el grupo de campos Plan de ingresos, permitiendo a los usuarios configurar los dos campos siguientes.
  - **Tipo de plan de ingresos**: este campo especifica la frecuencia por defecto de la distribución de ingresos. Actualmente, solo se admiten planes de ingresos mensuales.
  - **Número de periodo**: este campo especifica la duración por defecto de un plan de ingresos. Por ejemplo, una suscripción anual a una revista se definirá con un plan de ingresos de 12 periodos mensuales, mientras que un abono de esquí de temporada tendrá un plan de ingresos de 5 periodos mensuales.
  - **Periodo por defecto**: este campo especifica el primer periodo en el que se reconocerán los ingresos. Las opciones disponibles son:
    - _Mes actual_. Esta opción establecerá el Periodo de inicio del plan de ingresos en el mismo periodo que el periodo contable de la factura.
    - _Mes siguiente_. Esta opción establecerá el Periodo de inicio del plan de ingresos en el siguiente periodo contable de la factura.
    - _Manual_. Esta opción no establecerá ningún periodo de inicio del plan de ingresos; por lo tanto, se podrá seleccionar un periodo de inicio al crear la línea de la factura de cliente.
- **Gasto postpuesto**: este indicador solo es visible para productos con el indicador **Compra** marcado e indica que, _por defecto_, los gastos de compra de este producto deben diferirse. Cuando este indicador está marcado, se hace visible el grupo de campos Plan de gastos, permitiendo a los usuarios configurar los dos campos siguientes.
  - **Tipo de plan de gastos**: este campo especifica la frecuencia por defecto de la distribución de gastos. Actualmente, solo se admiten planes de gastos mensuales.
  - **Número de periodo**: este campo especifica la duración por defecto de un plan de gastos.
  - **Periodo por defecto**: este campo especifica el primer periodo en el que se reconocerá el gasto. Las opciones disponibles son:
    - _Mes actual_. Esta opción establecerá el Periodo de inicio del plan de gastos en el mismo periodo que el periodo contable de la factura.
    - _Mes siguiente_. Esta opción establecerá el Periodo de inicio del plan de gastos en el siguiente periodo contable de la factura.
    - _Manual_. Esta opción no establecerá ningún periodo de inicio del plan de gastos; por lo tanto, se podrá seleccionar un periodo de inicio al crear la línea de la factura de proveedor.

Estos valores se utilizan cuando se crea una factura para un producto que tiene un plan de gastos y/o un plan de ingresos.

Del mismo modo, estos valores también se utilizan cuando se crea una factura a partir de otro documento (por ejemplo: el proceso Facturar que crea facturas a partir de pedidos de venta). Del mismo modo, estos valores pueden modificarse transacción por transacción.

Para saber más, visite el artículo Cómo gestionar ingresos y gastos diferidos.

- **Registrar con precio de compra**: este indicador se utiliza al contabilizar un documento de **Albarán (Proveedor)** o una **Factura (Proveedor)** conciliada en el libro mayor.  
  Normalmente, se utiliza el coste del producto al contabilizar esas transacciones; sin embargo, esta casilla permite usar el precio de compra del producto en su lugar.  
  Esta funcionalidad solo funciona para el tipo de producto *Gasto* que no tenga seleccionada la casilla *Ventas*.

!!! info
    Tenga en cuenta que, en este caso, es necesario que un **Pedido de compra** esté relacionado con el **Albarán (Proveedor)**; de lo contrario, se mostrará un mensaje de error, ya que se requiere el precio de compra del producto.

- **Retornable**: este indicador se utiliza para indicar si un producto puede devolverse y, en caso de que lo sea, se muestra un nuevo campo. Al intentar devolver un producto no retornable desde la ventana Devolución de cliente, se mostrará un error.

![](../../../../assets/drive/8P_B_7zs64s6GpnSTeK9UQ6lBzvVnqGD9qOV3QR0WnAk_vPEZtjWJclvPzCvLx2HhU2oJuV4AjbxdhmspKkr3cWr20QacqX-VnigfqEjCIv9_blgPk1mEIloiZOBk5oCT6y41jQh9JI7HKA5vQ.png)

- **Días de Retraso en Devolución**: en este campo, es posible configurar la cantidad máxima de días antes de que un producto ya no pueda devolverse. Si el campo se deja en blanco, el producto puede devolverse sin limitaciones de tiempo. Al intentar devolver un producto cuyo periodo ha expirado, aparecerá un mensaje de advertencia.

![](../../../../assets/drive/QyvN8QXk9YDUur102n0wpiAY2QPyWux7iOpGMyvUkSVWGsoatyBdBBoMx5sxfWxo7dLX--2yo9cchrXV5yDH9nwpLqtOKLW9bsm4j0XFN9rCTCuusTntdbtxsRzu9Pu5pUinLOQ17lH_GAOymA.png)

!!! info
    **Nota**: Si **Almacenado** no está marcado y **Lista de materiales** está marcado, el precio del producto debería ser 0. Esto se debe a que, en ese caso especial, el precio del producto es la suma de los precios de los componentes de la lista de materiales de los que se compone. Si se desea crear una promoción, debe utilizarse «Descuentos y promociones».

##### Variantes

El producto puede marcarse como **Es genérico**. Esto significa que se crearán variantes de este producto basadas en algunas características como color, talla, etc. La definición de estas características tiene lugar en el producto genérico, por lo que puede decirse que un producto genérico es como una plantilla en la que las nuevas variantes heredarán todos los atributos (impuestos, precios, imagen) de este producto. Debido a esto, un producto genérico no puede utilizarse en transacciones, sino sus variantes.

!!! info
    Nota: Los productos marcados como genéricos no pueden utilizarse en operaciones de transacción como pedidos de venta, pedidos de compra, albaranes, etc.

Cuando se marca este indicador, se muestran dos botones:

![](../../../../assets/drive/XpdGDkmZecBZmb-qxyiA42-f6IdA9oTfYqig24hQZtSRsKLgItWO3U5jf-8kuTgHlMfKrUU9BQBSPfay8YoWSPKaYr74W9TXIgzumMG6T2sjq1g1w7zA9N2e2xZHPlGCykvLXWfU-wyAyH_5cw.png)

- Muestra todas las variantes que se han creado o no para ese producto genérico específico. Es muy útil cuando:
  - El usuario no quiere generar todas las variantes, sino solo algunas. El botón permite al usuario seleccionar las combinaciones posibles.
  - El usuario añade un valor más, por ejemplo, rojo cuando antes tenía verde y blanco y las variantes ya se crearon en el pasado. Mostrará las nuevas combinaciones.

Por ejemplo, imagine que el producto genérico Camiseta Modelo A tiene las características:

- Color: Azul, Blanco
- Talla: S, M, L

Pero todavía no se han creado variantes. Si pulsa el botón, puede ver todas las combinaciones posibles:

![](../../../../assets/drive/YysrJ-lndKNj6qUEzE5IIaNziDxMduILgMa9XP3Vde2NskD-oIug-d3Ce12C4gZSJCDuqDqyXcTXL0IPRSEkRP3ezOIsF321Zy1pizzXHcUKuWlzNUPivH7sfIyDZhFxOcZUzCprjCYdNRs3Ag.png)

Entonces pueden seleccionarse todas las combinaciones o elegir solo algunas. Una vez realizada la selección pulsando Hecho, las combinaciones se crearán como **Productos**. Estos nuevos productos tendrán el campo **Producto genérico** completado con el producto que se marcó como genérico. Se puede decir que es su producto padre.

![](../../../../assets/drive/1aZDzwrJXxLjUZhwgGhhHarCA-AsNLDbdSpLvVj2LzAvReay3gMmfC33auIHYoELn1pSKNSYrBWIckgesfl75Lza6jjZVMfXeNw1236dsTpVUMp0Aqmm19kJjAzp0ZRElYQc4F9iujwJ1X-P0A.png)

- Crea/explota todas las variantes de producto, es decir, todas las combinaciones basadas en las características definidas.

Otro botón que puede aparecer es ![](../../../../assets/drive/ZBo4NfiZAG6XK2iCAGS7jK--_4wffCzZHmp5z-8S0KrHU0Qs1U2_HkeL6MWD6KRZAFaYzjui8tmsOW9NKMbp3OkOLM27pUoQXBMC0YcHdCSLzQojA3Twi5IWuQwHEAcwlmjD4bnRYlMJ915Gpg.png). Solo aparece cuando el producto genérico o la nueva variante de producto tiene relacionada una característica no variante. Dos escenarios:

1. **Producto genérico**: este botón permite introducir el valor de esa característica.  
   Imagine que la característica es Línea de moda, que tiene tres valores: Sport, Vintage, Classic.  
   A diferencia de las características que son variantes, los usuarios no pueden introducir el valor mediante la solapa **Configuración de características**.
2. **Producto variante**: este botón permite al usuario introducir/actualizar la característica que no es variante.

Una vez creada una variante, sus características y valores pueden visualizarse en la vista de cuadrícula o en la vista de formulario:

- Vista de cuadrícula: hay una nueva columna **Descripción de característica**. Esta columna se calcula y no es editable. Muestra las características con sus valores como texto. Esta columna tiene un nuevo selector de búsqueda para encontrar variantes de producto en función de sus características.

![](../../../../assets/drive/uxKcLraqzQTO5YQDc1QPoXzbekSyMuKoCGy0FpkRmreW9hbxKJOcZm-4R2kHVRAf7h-VaVYDoMlqncOk-iCWOZv5d7Nyo6OJIjsJXdlA1e276uJ2iD7YbUTpyY3R8BMUphQJGPqHG9z8Q3oCRw.png)

Pulse el botón ![](../../../../assets/drive/XY6pNhuZ1_Zz62KSiGF0yVwR7duvGEGLzXb-sj8RZ0wfgcF2VLemqd37yK-hJshznCtz8tSACOFULk0CQo4f4CVrbR2W8-8CaBBUOtxsLXq2rnyATymb5aOTZaihm1mdEJEopKzbefJYQnNLrA.png) y se abre una ventana emergente para seleccionar valores:

![](../../../../assets/drive/Wtk1v4OXf3cYQZQRJVMZZu6bvKWAF94yM7GMeugxV3zLYTJez8HaVSdzgIFurmZ4Y_-kCpYQnv58HewpHMGgyqom8Xtn30PLliwlV8zGlfmMmqPg0yqLfFhLLvB7Mij9Ro9gs7SY4lz-zqhJXg.png)

- Vista de formulario: las variantes de producto tienen una nueva sección llamada _Descripción de característica_. Esta sección contiene tantos campos como características diferentes tenga el producto.

Existe una preferencia **Mostrar padres de características de producto**: los valores pueden ser 1, 2, 3, 4, etc. El número indica cuántos niveles del árbol jerárquico quiere mostrar el usuario en la vista de formulario en la ventana **Producto**. Por ejemplo, si el árbol es: Color->Verde->Verde claro->0034.

Se pueden añadir nuevos valores de una característica existente. Por ejemplo, el color rojo cuando ya se dispone de Azul y Blanco. Cuando esto ocurre, este nuevo valor se añade automáticamente a todos los productos genéricos que ya tienen la característica Color. Este nuevo valor estará presente en la solapa de configuración, pero desactivado. Si el usuario quiere utilizarlo en un producto específico para crear nuevas variantes, puede simplemente activar el valor y usar el botón *Gestionar características*.

##### Modificar Impuesto

- **Modificar Impuesto**: esta casilla permite que los servicios modifiquen los impuestos del producto al que están vinculados. Esto permite modificar el cálculo de impuestos de un producto en función de una condición del servicio. Por ejemplo, se vende un nuevo mueble de cocina a un cliente; los impuestos aplicados al mueble podrían cambiar si la instalación del mueble también la proporciona el vendedor del mueble. Además, esta funcionalidad solo aplica a los pedidos. Los documentos que se crean posteriormente tomarán la información del documento de pedido.

Esta modificación de impuestos se implementa mediante un servicio vinculado al producto. Este servicio debe marcarse como capaz de modificar los impuestos de los productos vinculados y también debe especificarse la configuración de los productos a los que se modificarán los impuestos y la nueva categoría de impuesto a aplicar.

Para configurarlo, vaya a la ventana **Producto** y cree un nuevo servicio. Un servicio es simplemente un producto con el campo Tipo de producto establecido en Servicios. También deben activarse el campo Vinculado a producto y el campo **Modificar Impuesto**. Cuando este campo se activa, se hace visible una nueva solapa llamada **Modificar Categorías de Impuestos**. En esta solapa se define la configuración de las categorías de impuestos de los productos que este servicio modificará cuando esté vinculado y la nueva categoría de impuesto a aplicar.

![](../../../../assets/drive/260ftQHLj7KxqXuouydWqLebx8YSli0i-k7OQh7rvpv1tfbcFB7zqhatrWcMd2F8tFMwLJEA-7xbc9LAtOdi1MNYioVlWheErN2eiFnhvq77HU-oyLHyiUTvrE_T1ruWbkDwOAPwpytv6_sM5w.png)

Para facilitar el proceso de configuración, se han añadido dos componentes:

1.- Modificar Impuesto para Categoría del producto (Botón): ventana Seleccionar y ejecutar para asignar las categorías del producto y las categorías de impuestos en la misma acción.

![](../../../../assets/drive/8ToxP9o606fpE3T0LM-yFPrDkN_UcfbtRPVfoZvh6Oa_riBLBhSKHPfMvurIv4ijKgDJWyVFo4Bqjxe9tP0uzGw_GUbOBHq5j_s26JnOYPHDpzmwnQnxrdWC4yeQJfjs9glD0TVmOro6OA1wDg.png)

2.- Copiar configuración de Modificar Impuesto del servicio (Botón): ventana Seleccionar y ejecutar donde se muestran los servicios que modifican impuestos. El usuario puede seleccionar uno o varios servicios, y la configuración actual se asignará a los servicios seleccionados. Una vez ejecutado el proceso, la configuración antigua (si existe) se eliminará y se añadirá una nueva. Este proceso ayuda a desplegar la misma configuración en múltiples servicios.

![](../../../../assets/drive/kiBwqlQgDgPUsbPgVV_vcxX_KBYPiHR4IO7ESfJQQOz6oZqgYal_8hA6Umn-Ik7g_ZfacpN64S_51WsHE-uruqBmRsEHWDRw94xVzBKRwBUiC_WGyGV8E_H3-ZLIVpb1kYpIFggvv_VmQz8n2w.png)
### Precio

Un producto puede formar parte de muchas Versiones de tarifa que son válidas para un periodo de tiempo determinado.

![](../../../../assets/drive/djRxxYVfhjv8e71EzysdOeoAUbQHqZSVuQbECB5EJ88BVtBo7FJ5weuwe6rrpxjxcXMKUX8pZKFgAE_lj5WdhmABdxh0Q09e9wdLPK8VBKNf6jBK8E56qbc6oQRtDcmHgxnxclqBQGsbm2B_rg.png)

Hay dos formas en las que el usuario puede hacer que un producto forme parte de una Tarifa:

1.  **seleccionando la/s Tarifa/s** e introduciendo los valores de *Precio unitario* y *Precio tarifa* en la solapa Tarifa, mientras se crea el producto.  
    Como consecuencia, el producto que se está creando también formará parte de la Tarifa seleccionada.
2.  **seleccionando el producto** e introduciendo los valores de *Precio unitario* y *Precio tarifa*, mientras se crea la *Tarifa*.  
    Como consecuencia, la Tarifa, así como los valores de *Precio unitario* y *Precio tarifa*, se mostrarán automáticamente en la solapa *Tarifa* del producto.  
    Para obtener más información, visite Tarifa.

#### Versión de Regla de Precio

Esta solapa solo estará disponible cuando se seleccione el campo Is Price Rule Based. Esta solapa ofrece la posibilidad de añadir Reglas de Precio de Servicios al Servicio a partir de una fecha determinada.

![](../../../../assets/drive/oKeZYS9ty3rxPOvfQd1nAc-VteGicSiOkI71kDF0mKBqomlsHjkbrtbMU3I36bDAbhM22cr0vlpMQ9FohG59E2YDtYddX5mFScwzgxcCvihP_y3C7SNdYqdnyIKewEei_gERVk0Nq-e4Gp_7Bg.png)

En esta ventana también es posible definir importes máximos y mínimos que se tendrán en cuenta al mostrar servicios.

Estos importes definen un intervalo entre precios de producto, de manera que el servicio solo estará disponible para añadirse en caso de que la suma de los productos seleccionados esté dentro del intervalo.

Para servicios con regla de cantidad: Cantidad única, la cantidad de la línea es relevante, ya que solo se añadirá un servicio.

Para servicios con regla de cantidad: Según producto, la cantidad de la línea no es relevante; solo importa el precio del producto, ya que se añadirán tantos servicios como productos se seleccionen. Solo si los precios de todos los productos están dentro del tramo, se mostrará el servicio.

Además, si una vez que se ha añadido un servicio (aún no entregado) al albarán, cambia el precio del producto relacionado, se activará una validación y, en caso de que el servicio ya no cumpla las reglas del tramo, se eliminará del albarán actual y se mostrará un pop-up indicándolo.
### Contabilidad

La solapa Contabilidad permite al usuario configurar las cuentas contables que se utilizarán al contabilizar transacciones relacionadas con el producto, como la compra o la venta del producto, en el libro mayor.

![](../../../../assets/drive/bLlVeOrdKF3rI3NdVa69a-CAwtO63JpdbyF0fzkMEG1pdmZU8u7bOlhffyM-HCwVnYA_y0kd51iPvCELamYYdp5RA9a7wVithXN1EWh_T73K304xQYB-gApjFi0-6vcof5HZBzUyIUrkpT82JQ.png)

Tal y como se muestra en la pantalla anterior, puede configurar para cada producto y libro mayor algunas cuentas que se utilizarán en las transacciones que se listan a continuación:

- **Inmovilizado del producto**: este campo almacena la cuenta por defecto que se utilizará para registrar transacciones de inventario tales como:
  - Recuentos de inventario
  - Movimientos de inventario
  - y Albarán (Proveedor)

Esta cuenta suele ser una cuenta de activo.

- **Gastos del producto**: este campo almacena la cuenta por defecto que se utilizará para registrar las compras del producto:
  - Normalmente, esta cuenta puede configurarse como un tipo de cuenta de *Gasto* en caso de no gestionar *Inventario perpetuo*.  
    En ese caso, el gasto se contabiliza en el momento en que se compran los bienes, al precio de compra.  
    El ingreso se contabiliza en el momento en que se venden los bienes, al precio de venta.  
    No gestionar *Inventario perpetuo* implica la necesidad de ajustar manualmente el valor del inventario al final del año.  
    Ese ajuste de inventario implica calcular la diferencia entre el *Valor final del inventario* y el *Valor inicial del inventario*.
  - Sin embargo, esta cuenta también puede configurarse como una cuenta de *Activo* en caso de gestionar *Inventario perpetuo*.  
    En ese caso, el gasto debe contabilizarse cuando el producto se vende al cliente como *Coste de los bienes vendidos* al coste del producto.  
    En Etendo, el ingreso se contabiliza en el momento en que se venden los bienes al precio de venta y el coste de los bienes vendidos se contabiliza en el momento del envío de los bienes al coste del producto.  
    Gestionar *Inventario perpetuo* no implica la necesidad de ajustar el valor del inventario al final del año.
- **Gasto de producto a periodificar**: este campo almacena la cuenta por defecto que se utilizará para registrar gastos diferidos.  
  Esta cuenta suele ser una cuenta de activo.
- **Ingresos por el producto**: este campo almacena la cuenta por defecto que se utilizará para registrar los ingresos por ventas del producto.  
  Esta cuenta suele ser una cuenta de ingresos.
- **Ingreso de producto a periodificar**: este campo almacena la cuenta por defecto que se utilizará para registrar ingresos diferidos.  
  Esta cuenta suele ser una cuenta de pasivo.
- **Costo del producto**: este campo almacena la cuenta por defecto que se utilizará para registrar el coste de los bienes vendidos.  
  Esta cuenta suele ser una cuenta de gasto.
- **Devolución de Ingresos por el Producto**: este campo almacena la cuenta por defecto que se utilizará para registrar devoluciones de ventas.  
  Esta cuenta suele ser una cuenta de ingresos.
- **Devolución del Costo del Producto**: este campo almacena la cuenta por defecto que se utilizará para registrar.  
  Esta cuenta suele ser una cuenta de gasto.
- **Desviación pr. factura**: este campo almacena la cuenta por defecto que se utilizará para registrar diferencias de precio entre Albaranes (Proveedor) contabilizados y Facturas (Proveedor) registradas.  
  Esta cuenta suele ser una cuenta de activo.

Inicialmente, estas cuentas se heredan de las cuentas por defecto de la configuración del libro mayor de la organización para la cual se está creando el producto. El usuario final siempre puede modificarlas.

!!! info
    Además, es importante remarcar que es posible configurar la creación de nuevas cuentas correlativas para los productos, tal y como se describe en la solapa Libros mayores de la ventana Organización.

#### Lista de materiales

Esta solapa permite editar los componentes de la lista de materiales de los que consta el producto seleccionado.

La Lista de materiales aplica a productos marcados como **Lista de materiales**.

Esta solapa proporciona información de la lista de productos contenidos y su cantidad para la producción de la Lista de materiales.

Si la Categoría de Impuesto del producto está marcada como **As per BOM**, esta solapa también proporciona información del precio de cada producto en la lista de la Lista de materiales. El precio y la cantidad de esta lista se utilizan para realizar la división del importe base para calcular los impuestos en función de los impuestos configurados para cada producto de la lista.

![](../../../../assets/drive/s-cRF1Q5kJQ4sPgBi-R9mMhT6v5JerM6U2qcFr0KgUyU79r0KE3mbTxN5oifJP1_M7XiW8G4j-vLYv6CSF8kr0XnyfO4DVGmazBfVB0aTjpfKS5qgLbYc6ZcBGUki-fBkZNVWmn9pYbVOqlIzw.png)
### Regla de cálculo de costes

La solapa **Regla de cálculo de costes** permite al usuario revisar las reglas de cálculo de costes que se aplican al producto dentro de un rango de fechas determinado.

Las reglas de cálculo de costes se aplican a los productos configurados como tipo *Artículo* y marcados como **Almacenado**.

Esta solapa proporciona información sobre la(s) regla(s) de cálculo de costes validada(s) que se aplica(n) al producto en un rango de fechas determinado, así como el **Algoritmo de cálculo de costes** definido para esa regla.

Las reglas de cálculo de costes se pueden crear y validar en la ventana **Regla de cálculo de costes**, relacionada con la entidad legal / organización correspondiente.

La moneda utilizada por la regla de cálculo de costes es la moneda configurada para la organización.

![](../../../../assets/drive/pUP_Yr9n3YIRGELLgfbQGwgdZ2Hbfpn79YXYVdLLoqnm0fsbUkFho_XUijntiFcDgbpRUNu323utJkWNYXS2b9KaazDnoEfi9kr-p_Mr3XD-gRh5udUjkbV1y6IBy3xPiUuQ-w0PW6Wk45oSVw.png)
### Costo

La solapa **Costo** recopila y resume la información relacionada con el coste del producto como resultado de cada transacción del producto. Los costes del producto son válidos durante un rango de fechas fijo y pueden calcularse utilizando un algoritmo de cálculo de costes *Average* o *Standard*.

Una de las primeras cosas que debe hacer al crear o importar un producto en Etendo es informar a Etendo sobre:

1.  el **Costo** inicial de los productos, si lo hubiera, introduciéndolo en esta solapa.  
    Siga leyendo para aprender cómo hacerlo.
2.  y el **Stock** inicial de los productos, si lo hubiera, creando y contabilizando un Inventario físico.

En general, esta solapa permite:

- **definir el Coste** de los productos almacenables; ese coste puede ser un coste estándar o un coste medio.
- **definir el Coste** de los productos no almacenables; en este caso debe ser un coste estándar.

Del mismo modo, también debe definirse para la **Organización** una Regla de cálculo de costes *Standard* o *Average* como forma de calcular el coste de las transacciones de los productos dentro de esa organización.

- **revisar el coste medio** calculado por el Servidor de Costes cuando se utiliza un Algoritmo de cálculo de costes *Average*.

Tenga en cuenta que, al utilizar un algoritmo de cálculo de costes *Standard*, el coste de cada transacción del producto es el *coste estándar por defecto* introducido en esta solapa.  
!!! info
    El *coste estándar por defecto* puede ser utilizado por el método de Coste por defecto siempre que no sea posible obtener el precio de una transacción para la cual sea necesario calcular su coste.

Los algoritmos *Average* sobrescriben el comportamiento del método de *Coste por defecto*, priorizando el uso del *Coste medio* actual, si existe.

- y, por último, disponer de una vista de todas las transacciones de entrada del producto que han impactado en el cálculo del coste del producto.
  - Las transacciones de entrada, como los albaranes de proveedor, son las que impactan en el cálculo del coste del producto; por lo tanto, el campo *Operaciones de almacén* las refleja claramente una a una.
  - De forma similar, un ajuste manual de coste *permanente* ejecutado en una transacción de salida, como un *Movimiento de mercancías desde* (M-), impacta en el cálculo del coste del producto; por lo tanto, el campo *Operaciones de almacén* refleja claramente este tipo de transacciones de salida.
  - La última transacción informa sobre:
    - el último coste, válido hasta una fecha final determinada
    - y la cantidad total de unidades de ese producto que están valoradas a ese coste.

Aquí también son visibles los costes calculados por el motor *legacy*.

Es posible reconocerlos por su tipo de coste:

- **Legacy Average**
- y **Legacy Standard**.

![](../../../../assets/drive/N1fWn0tV0yzS8dZULfJfiKeIOSvJzfYe-IBCo_TJSVqUavfD-zU4UlJlAhkg7CGNOV5uT__6-46NOHmWzyI3DBaYGwH_2TNdoblDMnC6VwDRzWILLf1k6YWZ8PRAPNWEjcMpSzqz81vqpObEBw.png)

La forma de definir el **Costo** de un producto implica introducir la siguiente información detallada:

- La **Organización** para la cual aplican los costes calculados. Tenga en cuenta que la organización debe ser de tipo *Entidad Legal*.
- El **Tipo de costo**. Hay dos tipos de coste disponibles: _Standard_ y _Average_.
- El **Costo** del producto; ese coste puede ser el coste unitario estándar del producto o el coste unitario medio del producto.
- Una **Fecha de inicio** desde la cual es válido el coste inicial del producto introducido.
- Una **Fecha final**, hasta la cual es válido el coste inicial del producto introducido; por ejemplo, 31-12-9999.  
  Esto equivale a decir que el coste introducido es válido hasta que un nuevo movimiento de ese producto tenga fecha en un día anterior a 31-12-9999. Obviamente, ese nuevo movimiento de entrada cambiará el coste del producto.

Además:

- el **indicador Manual** permite al usuario diferenciar las transacciones de coste introducidas manualmente de las creadas automáticamente por Etendo.
  - las creadas manualmente por usted al introducir la información de coste por defecto del producto deben marcarse como Manual.
  - las automáticas relacionadas con la contabilización de Transacciones de material no se marcarán como Manual.
- el **indicador Permanente** bloquea la posibilidad de eliminar el coste manualmente. Todos los costes deben establecerse como Permanente.
- el **Almacén** permite disponer de un coste diferente por almacén cuando se desee y siempre que la Regla de cálculo de costes definida permita hacerlo.

!!! warning
    Tenga en cuenta que no debe completar este campo si la Regla de cálculo de costes no tiene marcado el campo Dimensión de Almacén.
### Transacciones

La solapa **Transacciones** es una vista resumida de todas las transacciones de un producto.

No existe una forma para que el usuario cree directamente nuevas transacciones de producto en la solapa de transacciones.

Las transacciones de producto de cualquier tipo se guardan automáticamente y se listan en esta solapa a medida que se contabilizan en Etendo.

![](../../../../assets/drive/20u-EUxoETZhWKS6geaudh3OZbjEc0CvxOFx_0njFvaHCzsro7CxBXExfQSPgKnKNX4eRyw4uvcYUIXZSBINAPMX-3nGhUoqA1K08zWlRefUU00gCNAQEvXbU-7RboBfWCxzGUK4OrStxUZ3kQ.png)

Tal y como se muestra en la imagen anterior, Etendo guarda y nos informa de los siguientes datos relevantes para cada tipo de transacción de producto:

- **Hueco** donde el producto ha sido almacenado o del que se ha retirado
- **Cant. movida**, como el número de unidades de producto movidas internamente o bien de entrada o de salida
- **Fecha del movimiento**, como la fecha de la transacción del producto
- **Tipo de movimiento**, como por ejemplo:
  - **Albarán (Cliente)**, este tipo puede tener:
    - una cantidad movida negativa cuando un producto se envía a un cliente en un documento de **Albarán (Cliente)**.
    - una cantidad movida positiva cuando un producto se devuelve desde un cliente en una recepción de devolución de material.
  - Consumo interno, como las unidades consumidas en actividades internas tales como proyectos, reparaciones. Este tipo puede ser:
    - **Positivo** si las unidades del producto reducen el stock del almacén
    - o **Negativo** si se cancela una transacción de consumo interno; esto funciona como cuando se cancela un envío.
  - Entrada de inventario, esto se relaciona con un recuento de inventario físico superior al stock contabilizado para un producto en Etendo.
  - Salida de inventario, esto se relaciona con un recuento de inventario físico inferior al stock contabilizado para un producto en Etendo.
  - Movimiento desde, esto se relaciona con movimientos de mercancía desde un almacén y hueco
  - Movimiento a, esto se relaciona con movimientos de mercancía hacia un almacén y hueco
  - **Producción**, como las unidades de un producto incluidas en un esfuerzo de trabajo. Este tipo puede ser:
    - **Positivo**, para P+ cuando los productos se añaden al almacén
    - o **Negativo**, para P- cuando los productos se consumen
  - Recepciones de proveedor, este tipo puede tener:
    - una cantidad movida positiva cuando un producto se recibe de un proveedor en un documento de **Albarán (Proveedor)**.
    - una cantidad movida negativa cuando un producto se devuelve a un proveedor en un envío de devolución a proveedor.

Etendo también nos informa sobre la información específica de:

- **Línea de Albarán (Proveedor)/(Cliente)**
- **Línea de almacén**
- **Línea de movimiento**
- **Línea de producción**
- o **Asunto proyecto**

de la transacción del producto, según corresponda.

También es posible revisar:

1\. El **Costing Status** de una transacción.

El estado de cálculo de costes de una transacción puede ser cualquiera de los que se listan a continuación y tiene mucho que ver con el proceso en segundo plano de cálculo de costes:

- **Not Calculated**. Este estado significa que el proceso en segundo plano de cálculo de costes todavía no ha tomado la transacción para calcular su coste.
- **Cost Calculated**. Este estado significa que el proceso en segundo plano de cálculo de costes ya ha tomado la transacción y su coste ha sido calculado.
- **Pendiente**. Este estado se ha implementado para evitar que el proceso en segundo plano de cálculo de costes lance un error cuando no es posible calcular el coste de una transacción.  
  Este estado no es utilizado por los algoritmos de cálculo de costes implementados actualmente en Etendo, pero puede ser utilizado por otros algoritmos de cálculo de costes como FIFO para aquellos casos en los que se contabiliza una transacción de salida de producto sin contabilizar su correspondiente transacción de entrada de producto.
- **Omitir**. Este estado se ha implementado para que el proceso en segundo plano de cálculo de costes no tenga en cuenta las transacciones establecidas como *Omitir* al calcular costes.  
  Este estado no es utilizado por los algoritmos de cálculo de costes implementados actualmente en Etendo, pero podría ser utilizado por otros algoritmos de cálculo de costes.

2\. y si el coste de una transacción ha sido calculado o no.

En cuanto una transacción de producto tiene su coste calculado por el proceso en segundo plano de cálculo de costes, el campo *Es coste calculado* toma el valor *Sí*.

Una vez calculado el coste de una transacción, también puede ver:

- **Coste Original Trx**, que es el coste original de la transacción
- **Coste Total**, que es la suma del coste original de la transacción y todos los costes de ajuste de cualquier tipo.
- **Coste Unitario**, que es la suma del coste original y todos los ajustes de tipo *coste unitario*.
- **Moneda** utilizada para los cálculos.

Adicionalmente, el campo ***Coste Permanente*** informa de si el coste de una transacción es permanente o no. En caso de ser permanente, ya no se modificará.

Por último, es importante remarcar que, en el caso del algoritmo de coste *Promedio*, el coste *promedio* de un producto se calcula como *Promedio móvil*.

El coste promedio de un producto se calcula en base al flujo de transacciones del producto; por lo tanto, es la suma o resta del *Coste Total* de las transacciones listadas para el producto, dividido entre la suma de la *Cantidad acumulada* de las transacciones.

Por ejemplo, el coste promedio de un producto cuyas transacciones se listan a continuación es igual a 23.33 = (2000.00-1000.00+2500.00)/(100-50+100):

- albarán de proveedor para una cantidad movida 100 con un coste total de 2000
- albarán de cliente para una cantidad movida -50 con un coste total de 1000
- albarán de proveedor para una cantidad movida 100 con un coste total de 2500

##### Ajuste manual de coste

Adicionalmente, el coste de una transacción puede modificarse haciendo clic en el botón de proceso Ajuste manual de coste. Tras hacer clic en este botón, se abre un nuevo popup:

![](../../../../assets/drive/qDJuH3rx2ZvsvrA9Tjl0WZZjwJors5Xu2P2UgEjiBK_jhHX9vbYN3ZKcvH1mLIMWqUTNtrP4iKcFtp3VTDiwTHyLRpzsk4TUvxWl4QXo-ErSsQ4LbqtWnkCi2TWf1ftOhyL97RTpP5BbSEjL-Q.png)

Este pop-up permite introducir los siguientes datos detallados:

- **Importe de coste total**: es el nuevo coste total de la transacción de producto
- **Fecha contable**: es la fecha en la que este cambio manual, que implicará un ajuste de coste, se contabilizará en el libro mayor
- **Incremental**:
  - si no está marcado, el importe introducido en el campo de importe de coste total es el nuevo coste total de la transacción que, además, se establecerá como un coste *Permanente* que ya no podrá ajustarse.
  - si está marcado, el importe introducido en el campo de importe de coste total se añadirá al coste total actual; además, se muestra la casilla **Coste Unitario**.
- **Coste Unitario**: esta casilla solo se muestra si se selecciona la casilla *Incremental*.
  - si no está marcada, el importe incremental introducido en el campo de importe de coste total no se considerará parte del coste unitario de la transacción, sino del coste total. Esto es como introducir un coste *extra* como *Landed Cost*, que no cambia el coste unitario de esa transacción, pero sí el coste total.
  - si está marcada, el importe incremental introducido en el campo de importe de coste total se considerará parte del coste unitario de la transacción.

Para información adicional sobre qué ajuste de coste es, o no es, coste unitario, revise la sección Ajustes de coste - Visión general.

Una vez hecho, se creará un ajuste de coste de *corrección manual de coste*.

Este ajuste de coste puede revisarse y contabilizarse en el libro mayor en la ventana de Ajuste de coste.

Del mismo modo, este ajuste de coste también puede revisarse en la solapa **Costes Transacción**.

#### Costes Transacción

Los registros de **Costes Transacción** se crean automáticamente mediante el proceso en segundo plano de cálculo de costes y luego se listan para el producto en esta solapa.

En cuanto una transacción de producto tiene su coste calculado, se crea un nuevo registro en esta solapa.

En cuanto una transacción de producto tiene su coste ajustado, se crea un nuevo registro en esta solapa haciendo referencia a una **Línea de Ajuste de Coste**.

![](../../../../assets/drive/4lIc4FKc7VmCIoWFVPcV9fVkCqtBn2xTicXNsiin-P85rYySX2jwvUPGUAd3IdEaCUCSQo2hSgp_fuUP2Pp1HhXd6jUX03CePAe2AxypVuOVORVnJejwASLUrEmAGQyLBDCNm1GBXWaYr1N8ew.png)

Algunos campos relevantes a tener en cuenta son:

- **Fecha de coste**: es la fecha en la que el coste ha sido calculado (p. ej., la fecha contable de un albarán de proveedor)
- **Costo**: es el coste total calculado por el proceso en segundo plano de cálculo de costes
- **Moneda**: es la moneda utilizada para calcular el coste.  
  La moneda del coste es la moneda de la entidad legal; por lo tanto, una transacción de producto que tenga una moneda diferente (una tarifa en moneda USD, por ejemplo) tendrá su coste calculado en la moneda heredada (p. ej., EUR)
- **Línea de Ajuste de Coste**: si un coste calculado proviene de un ajuste de coste, este campo rellena la línea de ajuste de coste que provoca ese coste.  
  En última instancia, el coste total de una transacción de producto es la suma de todos los costes listados en esta solapa, tanto los originales como los ajustados, que pueden formar parte del coste unitario o no (p. ej., landed costs).
- **Coste Unitario**: este campo detalla si el coste calculado forma parte del coste unitario del producto o no.
- **Fecha contable**: es la fecha contable en la que el coste ha sido calculado y contabilizado en el libro mayor (p. ej., la fecha contable de un albarán de proveedor contabilizado en el libro mayor)
### Compras

La información de la solapa **Compras** se utiliza para productos que se planifican mediante el plan de compras.

En esta solapa, se introduce la información necesaria para la creación del plan de compras y para la creación automática de **Pedidos de compra** a partir del plan de compras.

Además, el proceso de solicitud utiliza la información de **Terceros** para la creación automática de **Pedidos de compra**.

![](../../../../assets/drive/jUizYPPOFt4WfdpL71z7Pxe8z7aMWc7Qnzz0rYE488WWt0fvBY9jKgswYbddRYo1rOzmYGsAmV0zOCGvwuo2BfwWDr4gG94qfwrNTjpfcA3XYq1sNH2wNg495KlwPCY52uGyT_FhGRQWxDzbMw.png)

- **Terceros**, el proveedor que aparecerá en el **Pedido de compra** cuando se cree automáticamente desde la solicitud o desde el plan de compras.
- **Valoración calidad**: valoración de calidad del proveedor. Campo solo informativo que no es utilizado por el proceso MRP.
- **Casilla Proveedor actual**: indicación del proveedor por defecto que será tenido en cuenta por el proceso MRP.
- **UPC/EAN**: Universal Product Code/European Article Number (código de barras) del producto tal y como lo utiliza el proveedor seleccionado. Solo informativo; esta información no aparece en un **Pedido de compra** creado.
- **Moneda**: moneda del pedido de compra.
- **Precio tarifa**: campo solo informativo del precio neto de tarifa que debe actualizarse manualmente en el **Pedido de compra** creado automáticamente desde el plan de compras.
- **Precio vigente desde**: la fecha a partir de la cual los precios introducidos son válidos. Solo informativo; no se utiliza en el proceso MRP.
- **Precio de compra**: campo solo informativo del **Precio unitario** que debe actualizarse manualmente en el **Pedido de compra** creado automáticamente desde el plan de compras.
- **Último precio de pedido de compra**: el **Precio unitario** del **Pedido de compra** añadido más recientemente.
- **Pr. última factura**: el **Precio unitario** de la **Factura (Proveedor)** añadida más recientemente.
- **Unidad**: la unidad de medida del producto.
- **Cantidad mínima de pedido**: una cantidad mínima de pedido para el proveedor. En el plan de compras, la cantidad de los pedidos de compra sugeridos será este valor o superior.
- **Cant. paquetes pedido**: campo solo informativo sobre el empaquetado del producto. Esta información no se tiene en cuenta para la creación de la información en el plan de compras ni para la creación de **Pedidos de compra**.
- **Tiempo de entrega esperado**: tiempo en días naturales entre el momento en que el producto se pide al proveedor y el momento en que se recibe en stock. En el plan de compras, esta información se utiliza para calcular cuándo deben realizarse los pedidos de compra, dando como resultado la fecha de pedido planificada para el pedido de compra sugerido.
- **Costo por pedido**: campo solo informativo de un importe fijo que debe añadirse manualmente al **Pedido de compra** creado automáticamente desde el plan de compras.
- **Nº de producto del proveedor**: la referencia del proveedor para el producto.
- **Categoría proveedor**: campo solo informativo para añadir información de la categoría del proveedor.
- **Descatalogado**: campo solo informativo para indicar que este producto ya no se utiliza. El plan de compras no tiene en cuenta esta configuración al generar el plan ni al crear **Pedidos de compra**. Al seleccionarlo, aparece el campo **Descatalogado por fecha** para indicar cuándo se descataloga el producto. Solo con fines informativos.
- **Tipo Cantidad**:
    - **Exacto**: cada pedido de compra sugerido es por la cantidad exacta requerida. Por ejemplo, si la demanda es de 85 unidades, la cantidad del pedido de compra sugerido es 85 unidades.
    - **Múltiple**: la cantidad que aparece como cantidad del pedido de compra sugerido es un múltiplo de la cantidad estándar (tal y como se define en esta pantalla). Por ejemplo, si la cantidad estándar es 20 unidades y la demanda es de 85 unidades, la cantidad del pedido de compra sugerido es 100.
- **Fabricante**: campo solo informativo para indicar el fabricante del producto.
- **Cantidad Std.**: cantidad que se tiene en cuenta en combinación con el **Tipo Cantidad** para el valor de cantidad del pedido de compra sugerido.
- **Capacidad**: cantidad por día que el proveedor puede suministrar. En base a este campo y al tiempo de entrega, se calcula la fecha del pedido de compra. El número de días se calcula como el valor máximo entre el tiempo de entrega y la cantidad requerida / capacidad.
### Producción

La solapa Producción se utiliza para productos que se planifican mediante el plan de producción.

La información de esta solapa es utilizada principalmente por el MRP para procesar el Plan de Producción y el Plan de Compras. El campo Hueco se completa para los productos en producción para indicar el hueco por defecto en el que se almacenará el producto cuando salga de producción.

- **Hueco**: ubicación por defecto del producto en el almacén.
- **Método de planificación**: definición de los elementos de suministro y demanda que se tienen en cuenta y con qué porcentaje para la creación del Plan de Producción y del Plan de Compras. Para más detalles, consulte la sección [Método de planificación](../material-requirement-planning/setup.md#planning-method).
- **Planificador**: la persona responsable de la ejecución del plan de MRP del producto. Para más detalles, consulte la sección [Planificador](../material-requirement-planning/setup.md#planner).
- **Capacidad**: capacidad de producción por día para el producto.
- **Cantidad desde:** cantidad mínima que debe introducirse en un requerimiento de trabajo.
- **Tipo Cantidad**:
    - **Exacto**: cada requerimiento de trabajo sugerido es para la cantidad estándar (según se define en esta pantalla). Aparecen múltiples requerimientos de trabajo sugeridos para cubrir la demanda total. Por ejemplo, si la cantidad estándar es de 20 unidades y la demanda es de 85 unidades, aparecen 5 líneas de requerimientos de trabajo sugeridos con cantidad 20.
    - **Múltiple**: la cantidad que aparece como cantidad del requerimiento de trabajo sugerido es un múltiplo de la cantidad estándar (según se define en esta pantalla). Por ejemplo, si la cantidad estándar es de 20 unidades y la demanda es de 85 unidades, la cantidad del requerimiento de trabajo sugerido es 100.
- **Cantidad Std.**: cantidad que se tiene en cuenta en combinación con el Tipo Cantidad para el valor de cantidad del requerimiento de trabajo sugerido.
- **Retraso Mínimo**: plazo de fabricación del producto.
- **Stock Mín.**: el nivel mínimo de stock que siempre debe existir en el almacén. Por ejemplo, si existe un stock mínimo de 1000 unidades y el stock es de 900 unidades, se sugiere un requerimiento de trabajo (Plan de Producción) o un pedido de compra (Plan de Compras) por 100 unidades. Normalmente, los productos de bajo coste o los productos con un plazo de entrega muy largo se configuran con un nivel de stock mínimo.
- **Máximo stock no reservado**: stock máximo sin tener en cuenta el stock pre-reservado. Este campo solo es visible cuando la funcionalidad de reserva de stock está habilitada. Consulte el siguiente ejemplo para entender cómo funciona:

1.  _Stock Mín._ y _Máximo stock no reservado_ son 200 y 1000 unidades, respectivamente
2.  Existen varios pedidos de venta que deben entregarse por un total de 3000 unidades
3.  Estos pedidos de venta generarán los pedidos de compra correspondientes (pre-reservados) al lanzar el MRP
4.  Actualmente hay 80 unidades en stock
5.  Cuando se lanza el MRP, creará los correspondientes pre-reservados y, al estar por debajo del stock mínimo, creará otro pedido de compra:
    1.  Como el _Máximo stock no reservado_ está definido, el sistema creará un pedido de compra de 920 unidades (1000-80)
    2.  Si este parámetro no estuviera definido, funcionaría como de costumbre y crearía un pedido de compra de 120 unidades (200-80)

- **ABC**: valor utilizado en la gestión de almacén para indicar una combinación del nivel de stock y el coste de una pieza. El valor se calcula ejecutando el Informe de Producto Pareto.
### Traducción

Los nombres de los productos se pueden traducir a cualquier idioma.

La forma de hacerlo es tan sencilla como:

- seleccionar primero el idioma requerido
- y luego introducir el nombre del producto traducido a ese idioma.

#### Características

Relación de características asignadas al **Producto**.

Campos:

- **Secuencia**: Orden de las características
- **Característica**: Lista todas las características definidas en la ventana _Característica de producto_
- **Variante**: Cuando está marcada, explotará/creará combinaciones con sus valores. Si no está marcada, no creará combinaciones con otras características. Por ejemplo:
  - Característica Color: Variante marcada con valor Azul y Blanco
  - Característica Talla: Variante marcada con valor M y L
  - Característica Línea de moda: Variante no marcada con valor Sport
  - Creará cuatro variantes/productos y en todos ellos con la característica Sport
- **Explotar Solapa de Configuración**: Indicador disponible en Productos genéricos y Características de variante. Cuando está marcado, los valores de la característica de variante seleccionada se insertan automáticamente en la solapa _Configuración de características_. Si no está marcado, los valores deben añadirse manualmente.
- **Define precio**: Cada valor de esa característica definirá el precio del nuevo producto. Sobrescribirá el precio definido para el producto genérico. Este precio se define en la solapa _Configuración de características_.
- **Tipo de tarifa**: Se muestra cuando _Define precio_ está marcado. Permite al usuario seleccionar en qué tipo de tarifa desea sobrescribir el precio. Por ejemplo:
  - El producto genérico tiene dos tarifas: una es para ventas y la otra para compra
  - Usted selecciona el valor _Tarifas de venta_. Entonces, al crear las variantes de producto, solo sobrescribirá el precio en las tarifas definidas como Ventas
  - Lo contrario si el valor seleccionado es _Tarifa de compra_
- **Define imagen**: Cada valor de esa característica definirá la imagen del nuevo producto. Sobrescribirá la imagen del producto genérico. Esta imagen se define en la solapa _Configuración de características_.
- **Subconjunto de característica**: Lista todos los subconjuntos incluidos para la Característica seleccionada (p. ej., Pantalones)

Una vez guardado el registro, todos los valores de la característica se rellenan en la solapa de configuración de características.

**Configuración de características**

La solapa Configuración de características contiene los valores disponibles para cada característica asignada al producto genérico. En esta solapa también se definen los modificadores de precio para crear las variantes.

Campos a tener en cuenta:

- **Valor de característica**: No puede ser editable, ya que se rellena automáticamente al seleccionar la característica
- **Código**: Código del valor. Hereda lo que se ha definido en la ventana de característica de producto
- **Pr. estándar**: Este campo se muestra cuando la característica está marcada como _Define precio_. El objetivo de este campo es disponer de precios diferentes por valor. Por ejemplo, en función de las tallas
- **Imagen**: Este campo se muestra cuando la característica está marcada como _Define imagen_. El objetivo de este campo es disponer de imágenes diferentes por valor. Por ejemplo, en función del color.
### Stock

Esta solapa muestra el Stock disponible para este Producto en la Aplicación. Solo muestra los Huecos para los que la cantidad disponible del Producto no es 0.

Para cada hueco no vacío, también muestra información sobre:

- la cantidad reservada
- y la cantidad asignada
### Coste Unitario

La solapa **Coste Unitario** muestra información sobre el *Coste Unitario* (Coste Unitario) real del producto.

El *Coste Unitario* de un Producto es el valor de cada unidad almacenada del producto, independientemente del algoritmo de cálculo de costes utilizado para calcular el coste de ese producto.

Este coste se calcula utilizando el *Stock Total* de un producto y el *Valor Total* del stock del producto, según la fórmula siguiente:

- Coste Unitario = Valor total del stock / Stock Total

De este modo, el coste unitario calculado es independiente del *Algoritmo de cálculo de costes* utilizado para calcular el coste de cada transacción y producto; por lo tanto, este coste unitario es compatible con todos los *Algoritmos de cálculo de costes* (Promedio, Estándar, FIFO, ...)

En esta solapa, va a existir un registro para:

- cada Organización que sea una Entidad Legal y que tenga definida una Regla de cálculo de costes
- o para cada Organización y Almacén, siempre que la Dimensión de Almacén esté definida como una dimensión de coste de la Regla de cálculo de costes actual definida para la *Entidad Legal*.

![](../../../../assets/drive/KaTTAE01N7KuTheqE-4REVj2b6H1QQnWqxpNvt2oNR_y9sqdYUsBOhQw1RHg_KP10n4NoI5gVpUXfgb0KPHOYx5Ab-RCWIAWvUyboKczDdnTHaWWVfw-bhUDAE4pMsAvEyt3qNtfHeKj7DAQ5A.png)

#### Categorías de Productos

El usuario puede definir si un producto de una determinada categoría de producto puede relacionarse con un producto de tipo 'Servicios' creando una relación entre una Línea de pedido del producto de Servicios y otra Línea de Pedido de venta del producto perteneciente a las categorías de producto incluidas/excluidas.

Esta solapa solo estará disponible cuando el campo ‘Categorías de producto incluidas’ del Servicio tenga un valor. Contiene todas las categorías de producto relacionadas con el servicio.

![](../../../../assets/drive/PYJo6PQVwfGTLbk5f39Z5opQ3qM4D81lk9qWKX7k1Z-E9RzZC5ZnB9EK4fcWtb37L_ZP_fcJbcnAQdXMF1vLAzXuhseG993zL5eDG2xL-nt-jexrA3D-d4VupddMJEeKGixjbQZFXUBoayzGQQ.png)

En la solapa está disponible la siguiente información sobre los productos relacionados:

- **Identificador**: Identificador de la Categoría del producto.
- **Nombre**: Nombre de la Categoría del producto.
- **Descripción**: Descripción de la Categoría del producto.

Esta solapa no es editable; no es posible añadir registros manualmente ni editarlos. Solo permite eliminar registros. Para añadir nuevos registros, es necesario hacer clic en el botón ‘Relacionar categorías de producto’ (visible solo cuando el campo ‘Categorías de producto incluidas’ tiene un valor). Este botón abrirá un Pick & Edit mostrando todas las categorías de producto no relacionadas con el servicio.

![](../../../../assets/drive/n_0U2RkOiXABiP8XeiREnMyOPLHm9-Xsu9hNM-PE6c248gNtomNeOzXROYJJzMpkuRJvKH0GnNDpOp3FSaBOAVURspU8rHeGLY_dhWofqyWmnQ00gJ8yGwuTDxy_PZ_SyzDTmPk6vf2eBeXEDQ.png)

#### Versión de Regla de Precio de Categoría

#### Productos

El usuario puede definir si un producto puede relacionarse con un producto de tipo 'Servicios' creando una relación entre una Línea de pedido del producto de Servicios y otra Línea de Pedido de venta del producto incluido/excluido.

Esta solapa solo estará disponible cuando el campo ‘Productos incluidos’ del Servicio tenga un valor. Contiene todos los productos relacionados con el servicio.

![](../../../../assets/drive/QhyN8Mqa2ybLbU9ny5se3_Z-JsGEIYGIAma4LQhBS4U4TUdZWUQTe3-Y3NP7bwlaQSxr6Fea2aB0K2g-slUF8XLmuN6aDN-3LCgqCjfSl0cl4uyn1c8YgL-w_AuZi8t4jXcDyF-cr2CpqKm-xg.png)

En la solapa está disponible la siguiente información sobre los productos relacionados:

- **Identificador**: Identificador del Producto.
- **Nombre**: Nombre del Producto.
- **Marca**: Identificador de la Marca del Producto.
- **Categoría del producto**: Categoría del producto a la que pertenece el producto.
- **Producto genérico**: Producto genérico del Producto, si tiene.
- **Descripción de característica**: Características del Producto, si tiene.

Esta solapa no es editable; no es posible añadir registros manualmente ni editarlos. Solo permite eliminar registros. Para añadir nuevos registros, es necesario hacer clic en el botón ‘Relacionar productos’ (visible solo cuando el campo ‘Productos incluidos’ tiene un valor). Este botón abrirá un Pick & Edit mostrando todos los productos no relacionados con el servicio.

![](../../../../assets/drive/LB2xjm1Lcu3JfY4eab8BA9hFgvjRLJCvaIW52jrLlGSoox67pJL73fBfqhzWBAVBGBGnXAOiaIu7F4O8bYsnbRWsmbZj3ddYGqWZ0vFpcJZdbTdSWIMtGuLFMcFDTONgqvFSgqwm3eW0fNIFxw.png)

#### Versión de Regla de Precio de Producto
### Solapa de UOM alternativa

!!! info
    Para habilitar esta funcionalidad, el usuario debe definir la preferencia **Habilitar la gestión de UOM** en el campo Propiedad con valor Y.

![](../../../../assets/drive/zu1QFJc_LPSBeJOGOOGHLNMjKi-WsPgjKPEaD4-BnQJEKbvhU1jz0WXeW-RHyDOEXYAx67_-Z7F6SIGVxBkGdZT828fkrjzAeu35psYO4H_dSFcw8YosbJailPqSWhZyjhCsN01vu0kqIyTG1g.png)

Campos a tener en cuenta:

- **Unidad**, es la unidad de medida alternativa del producto, por ejemplo *Palet*. Es importante remarcar que cualquier unidad de medida debe crearse y configurarse en la ventana [Unidad de medida](./product-setup.md#unidad-de-medida).
- **Rangos**, es la conversión entre la unidad de medida alternativa del producto (AUM) y la unidad de medida del producto. Por ejemplo, si la conversión de la AUM del producto a la UOM del producto es 50, significa que 1 Palet representa 50 Unidades.
- **Gtin**, es el *Global Trade Item Number* del producto definido en la AUM correspondiente.
- **Ventas**, **Compra** y **Logística**, estos campos permiten definir el uso de la AUM del producto dentro de los flujos de Ventas, Compra e Inventario.  
  Los valores permitidos son:
  
    - **Primario**: la AUM del producto definida en esta solapa se utiliza como unidad de medida por defecto en el flujo seleccionado (Ventas o Compra), al crear un documento de venta o compra como un pedido o un albarán/recepción.  
    Solo se puede definir una AUM Primaria por Producto y flujo.  
    Por ejemplo, si *Palet* es la AUM primaria definida para un producto dentro del flujo de Compra, significa que cada vez que se cree un documento de compra, *Palet* será la unidad de medida por defecto que se mostrará.
    - **Secundario**: la AUM del producto definida en esta solapa se puede seleccionar para el flujo seleccionado al crear un Documento.  
    Por ejemplo, si *Palet* es la AUM secundaria definida para un producto dentro del flujo de Ventas, mientras que *Paquete* es la primaria, significa que cada vez que se cree un documento de venta, *Paquete* será la unidad de medida por defecto que se mostrará, pero el usuario final puede cambiarla a *Palet*.
    - **No aplicable**: la AUM definida en esta solapa para el producto no estará disponible para su selección al crear Documentos para el flujo seleccionado.  
    Esta es la opción a seleccionar para *Logística*, ya que el uso de unidades de medida alternativas actualmente está implementado solo para ventas y compras. Las transacciones/documentos de inventario siempre hacen referencia a la unidad de medida del producto.

#### Modificar Categorías de Impuestos

Define la modificación de impuestos para productos vinculados a servicios. Los productos vinculados a este servicio que pertenezcan a la categoría configurada cambiarán la categoría de impuesto cuando se vinculen a este servicio.
### Stock por unidad logística

Permite visualizar el stock por unidades logísticas (inventario referenciado) de una forma más clara y organizada.

!!! info
    Para más información, visite [Unidad logística de stock](../../optional-features/bundles/warehouse-extensions/stock-logistic-unit.md#product---stock-by-logistic-unit).

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el módulo **Unidad logística de stock**, parte de Warehouse Extensions Bundle. Para ello, siga las instrucciones del marketplace: [_Warehouse Extensions Bundle_](https://marketplace.etendo.cloud/?#/product-details?module=BAE67A5B5BC4496D9B1CA002BBCDC80E){target="_blank"}. Para más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Warehouse Extensions - Notas de la versión](../../../../../whats-new/release-notes/etendo-classic/bundles/warehouse-extensions/release-notes.md).

---

Este trabajo es una obra derivada de [Gestión de Datos Maestros](https://wiki.openbravo.com/wiki/Master_Data_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.