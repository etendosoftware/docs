---
title: Gestión de Compras

tags:
    - Proceso de compras
    - Necesidad de material
    - Albarán (Proveedor)
    - Pedido de compra
---

## Visión general

La gestión de compras se ocupa de todas las actividades relacionadas con la compra de bienes y servicios a proveedores externos y de los informes correspondientes.

El proceso comienza con la creación y administración de necesidades de material y los pedidos de compra correspondientes, hasta el momento en que la mercancía se recibe en el almacén.
## Necesidad de material

:material-menu: `Aplicación` > `Gestión de Compras` > `Transacciones` > `Necesidad de material`

Una necesidad de material es un documento que especifica una solicitud para pedir productos.

El usuario puede crear necesidades de material y monitorizarlas en esta ventana:

![Ventana de necesidad de material](../../../../assets/drive/1ihaEseE5RnNH7INNbaRLyvZC0P2q-hTl.png)

### Cabecera

La cabecera de la necesidad de material permite introducir los siguientes datos:

- El tercero o proveedor; este es un campo opcional que puede ser cumplimentado por el solicitante en caso de que se conozca; por lo tanto:
  - El proveedor introducido en la cabecera será el que se utilice para cada línea de necesidad de material, salvo que se cambie a nivel de líneas para una línea concreta.
  - Si no hay ningún proveedor informado en la cabecera de la necesidad de material, se utilizará el configurado por defecto para el producto en su ventana de datos maestros, solapa *Compras*.
  - Si no hay ningún tercero o proveedor en la cabecera, ni en las líneas, ni configurado en el producto, el usuario deberá introducirlo al crear el pedido de compra desde la necesidad de material.
- La tarifa de compra. Este también es un campo opcional a cumplimentar, en caso de que el solicitante la conozca, y su comportamiento es el mismo que el descrito anteriormente, ya que está vinculada a Terceros.

Además, el sistema rellena los siguientes datos:

- El Nº de documento, que es el número de la necesidad de material.
- El solicitante, que es el usuario que está introduciendo la necesidad de material.

![Necesidad de material](../../../../assets/drive/1G5HR3bMmJXW837o-6qzZ0CTe418q5JB7.png)

A continuación, el solicitante puede pasar a la solapa "Líneas" para introducir datos adicionales.

### Líneas

Cada línea de necesidad de material muestra una demanda de producto para una fecha específica.

La solapa "Líneas" de la necesidad de material recoge los siguientes datos de demanda:

- La *Fecha de necesidad*, es decir, la fecha en la que se requiere que llegue el producto.
- El *Producto*, artículos/productos que deben comprarse.
- La *Cantidad* solicitada, o la *Cantidad Operativa* solicitada si el producto tiene configurada una *unidad de medida alternativa (AUM)*.
- La *Unidad* del producto, o la *Unidad Alternativa* del producto, en función de la configuración del producto respecto a la unidad de medida.
- El *Tercero:* este es un campo opcional que el usuario puede introducir si el proveedor informado en la cabecera de la necesidad de material debe cambiarse para una línea concreta.

!!! info
    Si no hay un proveedor informado en la cabecera de la necesidad de material ni en la línea de necesidad de material, el proveedor utilizado será el configurado por defecto para el producto; por lo tanto, este campo a nivel de línea también puede utilizarse para sobrescribir el valor por defecto.

- La *tarifa de compra*: este también es un campo opcional que puede introducirse si la tarifa informada a nivel de cabecera o la información de tarifa por defecto del producto debe sobrescribirse para una línea concreta.
- El *Precio tarifa*: este es el precio de la tarifa correspondiente para una fecha determinada. Es un campo opcional que puede rellenarse automáticamente en función de la tarifa introducida a nivel de cabecera o puede ser sobrescrito por el usuario para una línea de producto concreta.
- El *Precio unitario:* este puede ser igual al precio tarifa o no, en función de la fórmula: \[precio unitario = precio tarifa - descuento\]. Es un campo opcional que puede rellenarse automáticamente en función de la tarifa introducida a nivel de cabecera o puede ser sobrescrito por el usuario para una línea de producto concreta.
- El *Descuento*, si lo hubiera, se basa en la tarifa utilizada.

![Líneas de necesidad de material](../../../../assets/drive/1CtrCvBCrvUuxYDlaFysmkKu0-0XhemfC.png)

Es posible introducir tantas líneas de necesidad de material como demandas de productos.

El último paso es registrar la *Necesidad de material* como *Completada* utilizando el botón de cabecera "Completar"; entonces:

- La *barra de estado de la cabecera de la necesidad de material* nos informa de que la necesidad de material está *Completada*.
- La *barra de estado de las líneas de necesidad de material* nos informa de que la *cantidad de pedido de compra asociada* para cada línea es igual a 0**, ya que todavía no hay ningún pedido de compra vinculado a cada línea de necesidad de material, y el estado de la(s) línea(s) de necesidad de material es *Abierta*.

Es importante remarcar que las *Necesidades de material* no tienen ningún impacto en:

- La cantidad disponible de los artículos
- El coste de los artículos
## Administrar necesidades

:material-menu: `Aplicación` > `Gestión de Compras` > `Transacciones` > `Administrar necesidades`

La ventana Administrar necesidades está pensada para proporcionar una visión general de los artículos necesarios.

### Cabecera

Esta ventana permite al usuario gestionar las necesidades de material independientemente de su estado actual; por lo tanto, puede modificar o cerrar una necesidad de material y crear pedidos de compra para esas demandas.

![Cabecera de la ventana Necesidad de material](../../../../assets/drive/1yuE4xa0usvVzSdmthjDWdi12OAqTuJTe.png)

Una **necesidad de material** con estado "Completada" **siempre se puede modificar**, si es necesario. El usuario debe reactivarla y, a continuación, modificarla y registrarla.

También es posible **cerrar una necesidad de material en caso de que ya no se necesiten los artículos incluidos**, utilizando el botón de menú "**Cerrar**" y, a continuación, seleccionar la acción "**Cerrar**".

El estado de las líneas de necesidad de material se cambiará entonces a "Cancelada".

Por último, también es posible **crear pedidos de compra** para aquellas **necesidades de material en estado "Completada"**, utilizando el botón de menú "**Crear Pedido de Compra (Necesidades de material)**".

En este caso, se muestra una nueva ventana para que el usuario complete algunos datos, teniendo en cuenta que:

- Si hay **distintos proveedores en las líneas de necesidad de material, así como distintas tarifas**:
  - los **valores por defecto** introducidos en la ventana "Crear Pedido de Compra (Necesidades de material)" **serán los que se utilicen** en el pedido de compra.
- Si hay **distintos proveedores en las líneas de necesidad de material, así como distintas tarifas**, y el usuario no introduce ningún valor por defecto en la ventana "Crear Pedido de Compra (Necesidades de material)":
  - **los de las líneas de necesidad de material serán los que se utilicen** en los pedidos de compra.
- Si **todas las líneas de necesidad de material tienen el mismo proveedor y la misma tarifa**:
  - **no será necesario seleccionar valores por defecto** en la ventana "Crear Pedido de Compra (Necesidades de material)"; además, solo se creará un pedido de compra.

![Pedido de compra](../../../../assets/drive/17OuNS8YpM0VC3MUkLO25DPPHCMwWjq8u.png)

Etendo proporciona información sobre el/los número/s de pedido/s de compra creado/s tras pulsar el botón OK en la ventana "Crear Pedido de Compra (Necesidades de material)".

Esta acción vincula la necesidad de material y el pedido de compra y, además, se crea una línea de pedido de compra por cada línea de necesidad de material:

- Una **necesidad de material** vinculada a un pedido de compra cambia su estado de **Completada** a **Cerrado**.
- Una **línea de necesidad de material** vinculada a una línea de pedido de compra cambia su estado de **Abierto** a **Cerrado**.

Cualquier **pedido de compra** creado a partir de una **Necesidad de material**:

- se listará en la **ventana "Pedido de compra"**.
- tendrá el estado "**Registrado**"
- y contendrá **datos heredados de la Necesidad de material**, como:
  - Fecha de pedido
  - Fecha comprometida
  - Terceros
  - Tarifa
  - Producto/s

### Líneas

El usuario puede realizar un conjunto de acciones relacionadas con las líneas de necesidad de material. Es posible crear líneas o demandas de producto, o bien cancelarlas.

- **Se pueden crear manualmente nuevas demandas de producto** dentro de una necesidad de material simplemente **añadiendo nuevas líneas de necesidad de material** antes de crear un pedido de compra.
- **Las demandas de producto existentes o las líneas de necesidad de material se pueden cancelar**, si ya no son necesarias, utilizando el botón de cabecera "**Cambiar estado**".

#### Líneas de pedido de compra (Pedido de compra) asociadas

Esta solapa permite al usuario revisar la línea de pedido de compra vinculada automáticamente a una línea de necesidad de material o vincular manualmente una línea de pedido de compra existente a la línea de necesidad de material correspondiente.
## Necesidad a Pedido

:material-menu: `Aplicación` > `Gestión de Compras` > `Transacciones` > `Necesidad a Pedido`

La ventana Necesidad a Pedido muestra todas las necesidades de material **"Completadas"** que coinciden con los criterios utilizados en la sección de **"Filtro"** y también muestra las líneas de necesidad de material seleccionadas como bloqueadas; por lo tanto, la misma demanda de producto no puede incluirse más de una vez en un pedido de compra.

![Necesidad a pedido](../../../../assets/drive/1Xl_R8oaUrOaO0SK4wB5BYNw3wJDEjHBX.png)

En otras palabras, la sección superior de esta ventana muestra las líneas de necesidad de material encontradas que todavía no están vinculadas a un pedido.  
Estas son las líneas que el usuario puede añadir al área **"Bloquear"** en la sección inferior de la ventana.

Una línea de necesidad de material bloqueada no puede ser modificada por ningún otro usuario, hasta que quien la bloqueó la desbloquee.  
De este modo, durante el tiempo en que las líneas de necesidad de material están bloqueadas:

- La misma demanda de producto no se incluirá en un pedido de compra por error.
- El equipo de compras tendrá la oportunidad de revisar el stock y contactar con diferentes proveedores si fuera necesario para negociar un precio para los productos.
- Si no hay actividad durante 3 días, el sistema elimina el bloqueo de las líneas.

Una necesidad de material puede desbloquearse manualmente por el responsable de compras o por quien la bloqueó, moviéndola de nuevo a la parte superior de la pantalla **"Necesidad a Pedido"** mediante el botón **"Eliminar"**.

Una vez que las demandas de producto estén claras y bloqueadas, el último paso a realizar en esta ventana es crear un pedido de compra para esas necesidades utilizando el botón de proceso **"Crear"**.
## Pedido de compra

:material-menu: `Aplicación` > `Gestión de Compras` > `Transacciones` > `Pedido de compra`

La ventana **Pedido de compra** permite al usuario gestionar pedidos que, una vez registrados, se enviarán a los proveedores externos. En otras palabras, es un documento para registrar productos y/o servicios que se van a comprar y documentar.

![Ventana de pedido de compra](../../../../assets/user-guide/etendo-classic/basic-features/procurement-management/transactions/purchaseorder.png)

Una vez registrado el documento, puede enviarse al proveedor externo y puede pagarse por adelantado si es necesario.

Los pedidos de compra pueden crearse y registrarse en la sección de cabecera de la ventana de pedido de compra.

### Cabecera

La **cabecera del pedido de compra** permite introducir la siguiente información:

- **Organización:** entidad organizativa dentro de la entidad.
- **Documento transacción**, que en este caso se establece por defecto como "**Pedido de compra**".
- **Nº de documento**, o el número de pedido de compra de la compañía.
- **Fecha de pedido:** esta fecha también se establece por defecto en Etendo en función de la fecha del sistema, pero siempre puede modificarse.
- **Terceros**: el usuario final debe seleccionar el proveedor al que se emite el pedido de compra.
- **Dirección**: se completa automáticamente una vez seleccionado el tercero, en función de la dirección o ubicación configurada como "Dirección de envío".
- **Almacén**: aunque Etendo lo establezca por defecto en función de las opciones seleccionadas en el "Perfil", debe ser verificado por el usuario final.
- **Fecha comprometida**: es la fecha en la que la organización o entidad legal requiere que se entreguen los artículos.
- **Método de pago**, **Condiciones de pago** y **Tarifa**: se establecen por defecto en Etendo una vez seleccionado un tercero.
- **Nº de referencia**, texto libre que puede encontrarse en la sección "Más información"; puede utilizarlo para guardar el número de pedido del proveedor, si existe.

En la **Barra de estado** de la cabecera, el usuario puede encontrar la siguiente información:

- **Estado doc.**: estado del documento del pedido. El pedido puede estar en estado registrado, borrador, cerrado, entre otros.
- **Importe total**: importe bruto total del pedido.
- **Imp. total líneas**: importe neto total del pedido.
- **Moneda**: moneda del pedido.
- **Estado del envío**: indica en % qué cantidad del pedido se ha recibido.  
- **Estado de factura**: indica en % qué cantidad del pedido se ha facturado.  

**Una vez que la información de la cabecera esté correctamente cumplimentada, puede ir a la solapa "Líneas" para introducir la información de la(s) línea(s) del pedido de compra**.

!!! info
    Para aprender cómo introducir líneas de pedido de compra, visite la siguiente sección [Líneas](../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#lines_2).

Es posible realizar hasta **tres acciones posibles respecto a un pedido de compra**, utilizando el **botón de cabecera "Registrar"**:

- **Procesarlo**, en caso de que quiera procesarlo pero no registrarlo como final, porque podría necesitar cambiarlo más adelante.
- **Anularlo**, en caso de que ese pedido de compra ya no sea necesario y, por tanto, deba anularse.
- **Registrarlo**, en caso de que sea correcto y definitivo.

!!! info
    Si existen productos BOM no almacenables y no se han explotado, el botón Registrar los explota automáticamente.

### Líneas

Una vez que la cabecera del pedido de compra se ha cumplimentado correctamente y se ha guardado, cada línea del pedido de compra puede crearse en esta solapa.

Las líneas del pedido de compra pueden crearse de tres formas diferentes:

**1\. Creando manualmente nuevos registros en la solapa "Líneas"**.

Los campos del pedido de compra que puede completar se describen a continuación:

- **Producto**. Puede seleccionar un artículo o producto de la lista o utilizar el icono del selector de producto.
- **Cant. pedido**, o **Cantidad Operativa** si el producto tiene configurada una *unidad de medida alternativa (AUM)*. Esta es la cantidad necesaria del producto/artículo.
- **Unidad** del producto, o **Unidad Alternativa** del producto, dependiendo de la configuración del producto respecto a la unidad de medida.
- **Valor atributos. Un atributo asociado a un producto como parte de un conjunto de atributos.**
- **Precio unitario**. Este proviene de la **Tarifa** seleccionada en la cabecera, pero siempre puede modificarse.
- **Imp. línea. El importe final de una línea específica, basado únicamente en cantidades y precios.**
- **Impuesto**. El impuesto de compra normalmente lo completa el sistema, dependiendo de la configuración de impuestos.

**2\. Recuperando todas las líneas de pedidos de compra creados previamente.** En este caso, debe utilizar el botón de proceso "**Copiar desde Pedidos**".

Este botón de proceso habilita la ventana **Copiar desde Pedidos Elegir y Editar**.

La ventana "Copiar desde Pedidos Elegir y Editar" permite buscar los pedidos a copiar utilizando las opciones de filtro disponibles.

La información de líneas de los pedidos seleccionados se insertará en la(s) línea(s) del pedido de compra; después, esa información puede modificarse manualmente.

**3\. Copiando líneas de otros pedidos de compra.**

En este caso, debe utilizar el botón de proceso **"Copiar líneas"**.

Este botón de proceso habilita una nueva ventana llamada "Copiar líneas desde pedido", que permite crear líneas de pedido seleccionando los productos ya comprados al proveedor del pedido, teniendo en cuenta los *Días consumo* configurados para el proveedor.

En la **Barra de estado** de cada línea, puede encontrar información sobre:

- **Cant.entregada**: número de productos recibidos de la línea.
- **Cant.facturada**: número de productos facturados de la línea.

#### Botón Explotar

El botón **Explotar** se muestra al seleccionar una línea con un producto BOM no almacenable y el producto aún no se ha explotado. Al explotar un producto, los componentes de la lista de materiales de los que se compone el producto seleccionado se muestran en el pedido.

!!! info
    Una vez que lo haya explotado, no puede comprimirlo. Debe eliminar todas las líneas (primero los componentes de la lista de materiales y después el producto BOM) e insertar de nuevo el producto BOM no almacenable.

#### Línea de impuesto

Para cada línea del pedido de compra, Etendo completa automáticamente en esta solapa la información relacionada con el impuesto de línea.

La solapa Línea de impuesto informa sobre cada línea del pedido de compra:

- **tipo impositivo aplicado**
- **importe de impuesto calculado**
- **base imponible**

!!! info
    No es posible crear manualmente una nueva línea ni modificar las existentes.

#### Descuentos

Lista información sobre los descuentos aplicados automáticamente en función de la configuración del proveedor y/o introducidos manualmente para el pedido de compra.

![Descuentos](../../../../assets/drive/1AavUV8S8kQ2dp0P_W9lw06XfmAf5d_g-.png)

#### Plan de pagos

Muestra el importe total previsto a pagar al registrar el pedido, así como el/los importe(s) pagado(s) por adelantado o pagado(s) contra la(s) factura(s) del pedido.

La información del Plan de pagos es necesaria a nivel de pedido porque los proveedores podrían solicitar un **pago por adelantado** de la totalidad o parte de una deuda antes de su fecha de vencimiento.

Los planes de pagos del pedido de compra **no muestran ni gestionan fechas de vencimiento válidas**, sino el plan de pagos de la(s) factura(s) de compra correspondiente(s).

Esta solapa también muestra información sobre los pagos regulares realizados contra la(s) factura(s) de este pedido, como importes pagados.

Por último, el plan de pagos de un pedido de compra se **eliminará**:

- si el pedido de compra se **reactiva**
- o si el pedido de compra se **anula**

#### Detalles del pago

Muestra los detalles de los pagos (pagos por adelantado o pagos regulares) realizados para el pedido o para la(s) factura(s) del pedido.

### Cómo reactivar un pedido de compra cerrado

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Financial Extensions Bundle. Para ello, siga las instrucciones del [marketplace](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

!!! warning "Aviso de dependencia"
    Este módulo depende del módulo [**Finalización masiva**](../../optional-features/bundles/essentials-extensions/bulk-completion.md), ya que las acciones de procesamiento de **pedido** deben realizarse utilizando procesos modernos que permitan el disparo de Hooks, en lugar del procesamiento heredado. Debido a este requisito, las acciones heredadas de **cerrar/reactivar** para pedidos se ocultarán y estas acciones solo estarán disponibles a través del botón **Finalización masiva**.

Etendo permite al usuario reactivar pedidos de compra cerrados seleccionando el/los necesario(s) y haciendo clic en el botón Deshacer cierre.

![](../../../../assets/drive/1cyLa7pjnsNgXtnSEK2lZX9s35imhD2Kq.png)

Una vez finalizado el proceso, el estado del pedido de compra pasa a registrado.

!!! info
    Consulte la documentación técnica sobre Advanced Financial Docs Processing para ampliar el proceso.

### Eliminación de pagos

El objetivo de esta funcionalidad es eliminar y reactivar pagos de forma ágil y sencilla. Además, permite eliminar y reactivar transacciones bancarias y conciliaciones.

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

Desde esta ventana, es posible eliminar pagos asociados a un pedido de compra seleccionando el documento correspondiente y, a continuación, haciendo clic en el botón Eliminar pago. Si existe una factura asociada al pedido, también se eliminará la relación de esta factura con el pago en cuestión (ventana Factura (Proveedor) > solapa Plan de pagos).

Si el pago está incluido en la cuenta financiera, es decir, si está en estado Depositado/Retirado no conciliado, también se eliminará la transacción en ella (ventana Cuenta financiera > solapa Transacción).

Si el pago se concilia mediante un método automático, entonces, además de la transacción en la cuenta financiera, se eliminará la línea del extracto bancario a la que estaba vinculada (ventana Cuenta financiera > Extractos bancarios importados) y la línea correspondiente de la conciliación bancaria (Cuenta financiera > Conciliaciones).

!!! info
    Si el pago está contabilizado, el asiento contable también se elimina.

![](../../../../assets/user-guide/etendo-classic/basic-features/procurement-management/transactions/PRpic2.png)

### Intercompany

En caso de que el usuario tenga que crear pedidos o facturas entre dos o más organizaciones diferentes pero que pertenecen a la misma entidad, esta funcionalidad permite generar automáticamente el documento inverso correspondiente.

!!! info
    Para más información, visite [la guía de usuario del módulo Intercompany](../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/intercompany.md).

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

### Finalización masiva

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Essentials Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Essentials Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=39AC2D9F72124AC7A1D0A3D005293C9E){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Essential Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/essentials-extensions/release-notes.md).

La funcionalidad de Finalización masiva permite al usuario completar, reactivar o cerrar múltiples registros seleccionándolos y haciendo clic en el botón **Finalización masiva**. Esto facilita la gestión de registros y la hace más eficiente, reduciendo el tiempo dedicado a procesar registros individuales.

!!! info
    Para más información, visite [la guía de usuario del módulo Bulk Completion](../../optional-features/bundles/essentials-extensions/bulk-completion.md).

### Advanced Bank Account Management

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el módulo Advanced Bank Account Management del Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

Este módulo añade un nuevo campo a la cabecera de la ventana Pedido de compra: **Cuenta bancaria**. Este campo se completa automáticamente con la cuenta bancaria relacionada con la dirección o el tercero del pedido.

![bank-account-3.png](../../../../assets/legacy/bank-account-3.png)

!!! info
    Para más información, visite la [guía de usuario de Advanced Bank Account Management](../../optional-features/bundles/financial-extensions/advanced-bank-account-management.md).
## Albarán (Proveedor)

:material-menu: `Aplicación` > `Gestión de Compras` > `Transacciones` > `Albarán (Proveedor)`

Un **Albarán (Proveedor)** es un documento emitido para reconocer la recepción de los artículos listados en él. En otras palabras, es un documento utilizado para registrar en Etendo los detalles de los artículos recibidos físicamente en el almacén.

### Cabecera

Los **Albarán (Proveedor)** pueden emitirse y contabilizarse en la sección de cabecera de la ventana de albarán.

![Cabecera de albaranes](../../../../assets/user-guide/etendo-classic/basic-features/procurement-management/transactions/goodsreceipt2.png)

Los campos a completar en la **cabecera del Albarán (Proveedor)** son:

- **Tipo de documento**, que se completa por defecto como "MM Receipt".
- **Almacén**, donde se ubicarán los bienes.
- **Terceros**, tercero que entrega los bienes.
- **Fecha del movimiento**, fecha de entrega de los bienes.
- **Fecha contable**, fecha contable en caso de contabilizar el **Albarán (Proveedor)**.
- **Pedido de compra**, número de pedido de compra enlazado automáticamente por Etendo, en caso de que el **Albarán (Proveedor)** se cree automáticamente desde un **Pedido de compra**.
- **Nº de referencia**, el equipo de almacén puede introducir aquí el número del albarán del proveedor (*Delivery Note*); de este modo, el número interno del **Albarán (Proveedor)** y el número del albarán del proveedor quedan vinculados.

En la **barra de estado** de la cabecera, el usuario puede encontrar la siguiente información:
 
- **Estado doc.**: estado del documento del albarán.
- **Estado de factura**: indica en % qué cantidad del albarán ha sido facturada. 

**Una vez que la información de cabecera se haya completado correctamente, puede ir a la solapa "Líneas" para introducir "Línea/s de Albarán (Proveedor)"**.

!!! info
    Para aprender cómo introducir líneas de albarán, visite la siguiente sección [Líneas](../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#lines_3)

Si un **Albarán (Proveedor)** se completa y, por tanto, queda **contabilizado**:

- La **cantidad disponible de los artículos recibidos se incrementa** en la cantidad recibida.

Si un **Albarán (Proveedor) "Completada" se anula** porque los bienes han sido devueltos al proveedor:

- La **cantidad disponible de los artículos devueltos se reduce** en la cantidad de bienes devueltos. Etendo crea automáticamente un nuevo **"Albarán (Proveedor)"** para exactamente los mismos artículos, pero con cantidades **"negativas"**.

!!! info
    Para saber más sobre devoluciones de bienes, visite *Devolución a proveedor* y *Devolución a albarán de proveedor*.

El proveedor puede enviar una **"Factura (Proveedor)"** junto con el **"albarán del proveedor"** (*Delivery Note*) de los bienes entregados; por tanto:

- Desde la ventana de **Albarán (Proveedor)**, es posible generar la factura del proveedor correspondiente usando el botón de proceso de cabecera "**Crear factura del albarán**".

Esta acción implica un **vínculo entre el albarán y la factura de compra**, de modo que el usuario puede conocerlo al consultar la factura de compra correspondiente.

!!! info
    Para saber más, visite [Factura (Proveedor)](../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#purchase-invoice).

### Líneas

Una vez que la cabecera del albarán se haya completado correctamente y guardado, cada artículo recibido puede listarse como una línea de albarán independiente.

Existen varias formas de crear líneas de albarán.

1.**El usuario siempre puede crear manualmente líneas de albarán.**  
Esta es la forma a la que el usuario puede recurrir en caso de que no exista un pedido de compra contabilizado ni una factura de compra completada de la que recuperar datos para los bienes recibidos.

Como consecuencia, la información a completar manualmente es:

- los bienes o artículos recibidos
- la cantidad recibida
- el hueco donde se almacenarán los artículos

El botón **Explotar** se muestra al seleccionar una línea con un producto BOM no almacenable y el producto aún no ha sido explotado. Al explotar un producto, los componentes de la lista de materiales de los que consta el producto seleccionado se muestran en el albarán. Una vez explotado, no puede comprimirse. Debe eliminar todas las líneas (primero los componentes de la lista de materiales y después el producto BOM) e insertar de nuevo el producto BOM no almacenable.

2.Por otro lado, también es posible **crear "automáticamente" líneas de albarán**, usando el botón de proceso de cabecera **"Crear líneas de"**.

Esto permite al usuario seleccionar los pedidos o facturas pendientes de recibir.

Por ejemplo, una vez seleccionado un pedido de compra, se muestran las líneas del pedido de compra pendientes de recibir.

Entonces, el usuario puede seleccionar las líneas de compra recibidas, cambiar la cantidad si fuese necesario y ubicarlas en el almacén.

Finalmente:

- Si se selecciona un pedido de compra/línea, esta acción **vincula cada línea de albarán con la línea de pedido de compra correspondiente**; lo mismo aplica a la factura de compra.

En la **barra de estado** de cada línea, puede encontrar información sobre la **Cant.facturada**, el número de productos facturados de la línea.

#### Contabilidad

Información contable relacionada con la recepción de material.

Un **"Albarán (Proveedor)" puede contabilizarse** si la tabla "**MaterialMgmtShipmentInOut**" está configurada como activa para contabilidad en la solapa \[*Tablas a contabilizar*\] de la configuración del libro mayor de la organización.

La contabilización de un **"Albarán (Proveedor)"** tiene este aspecto:

![Contabilización de albaranes](../../../../assets/user-guide/etendo-classic/basic-features/procurement-management/transactions/goodsreceipt3.png)

La contabilización de un **"Albarán (Proveedor)"** requiere el cálculo del coste de los productos contenidos.

En el caso de un albarán, esto es:

- el precio de compra de los productos
- o el *coste estándar* por defecto de los productos en caso de calcular el coste usando un *Algoritmo de cálculo de costes* estándar.

Si no existe un pedido de compra relacionado, el proceso Costing Server utiliza el más reciente de los siguientes tres valores:

- el último precio de pedido de compra del proveedor del albarán para el producto.
- la tarifa de compra del producto.
- o el *coste por defecto* del producto.

Además:

- La organización de **Entidad Legal** necesita tener configurada una *Regla de cálculo de costes* validada.
- Y el *Costing Background Process* debe estar planificado para la **Entidad**, de modo que pueda buscar y permitir que el proceso *Costing Server* calcule el coste de las transacciones.

Una vez calculados los costes, el **Albarán (Proveedor) puede contabilizarse** en el libro mayor.

En el caso de un albarán que contenga productos de **Gasto** sin la casilla **Ventas** seleccionada, es posible usar el precio de compra del producto en lugar del coste del producto para contabilizar el albarán.

Esto funciona si la casilla *Registrar con precio de compra* está seleccionada para los productos.

En este caso, es necesario que exista un **"Pedido de compra"** relacionado con el **"Albarán (Proveedor)"** contabilizado.

#### Anulación

Es posible anular totalmente un albarán usando el botón de cabecera **"Cerrar"** y seleccionando después la acción "**Anular**".

Esta acción crea un **nuevo documento** que **revierte el albarán.**

La acción de anulación permite especificar una "**Fecha de anulación**" y una "**Fecha contable de anulación**" del nuevo documento:

- **Fecha de anulación**: es la fecha del movimiento del nuevo documento que revierte el albarán.
- **Fecha contable de anulación**: es la fecha contable del nuevo documento que revierte el albarán.

Ambos campos toman por defecto las fechas del documento original y validan que las fechas introducidas no sean anteriores a la **Fecha del movimiento** y a la **Fecha contable** del **Albarán (Proveedor)**, respectivamente.

La acción de anulación implica que:

- Etendo genera automáticamente un **nuevo documento** en la ventana **Albarán (Proveedor)** e **informa del número de documento** creado. El número de documento también se muestra en el campo descripción del albarán. Este nuevo documento se crea como se describe a continuación:
  - El "**Documento transacción**" utilizado por Etendo es "**MM Receipt**".
  - Este documento es **exactamente igual que el original** que se está revirtiendo, **pero la cantidad de movimiento es negativa.**
  - Una vez creado el **nuevo documento**, puede **cambiar** tanto la "**Fecha del movimiento**" como la "**Fecha contable**" del nuevo documento antes de contabilizarlo.

#### Landed Cost

La solapa **Landed Cost** permite asignar costes adicionales al albarán.

![Ventana de landed cost](../../../../assets/drive/1YND6qqNXSCzLiiq_PICSVr3GymXZi6_o.png)

Es posible introducir tantos tipos/líneas de landed cost como sea necesario.

Algunos campos relevantes a tener en cuenta son:

- **Tipo de Landed Cost**: es el tipo de landed cost que se va a asignar al albarán.
- **Línea de la factura**: sirve para seleccionar la línea de factura de landed cost correspondiente, si existe, que coincida con el tipo de landed cost que se está introduciendo.  
  Si se selecciona una línea de factura, el importe de la línea de factura se completa en el siguiente campo "Importe".
- **Importe**: es el importe del landed cost. Este importe puede ser una "estimación" o un importe "real" en caso de seleccionar una línea de factura.
- **Algoritmo de Distribución de Landed Cost**: es el distribuido por Etendo "Distribución por importe", lo que significa que el importe del landed cost se distribuirá entre las líneas del albarán proporcionalmente por el importe de la línea de albarán.

Una vez completados todos los elementos anteriores, incluida la línea de factura de compra de landed cost correspondiente, tanto el **Albarán (Proveedor)** como el *procesar asociación* de Landed Cost se ejecutan haciendo clic en el botón de proceso "**Completada**".

### Cómo reactivar albaranes

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Warehouse Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Warehouse Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=EFDA39668E2E4DF2824FFF0A905E6A95){target="\_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Warehouse Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/warehouse-extensions/release-notes.md).

Desde la ventana **Albarán (Proveedor)**, es posible reactivar un movimiento generado previamente seleccionando el documento correspondiente y haciendo clic en el botón **Reactivar**.

Una vez que el albarán se reactiva correctamente, el estado del documento cambia a **Borrador**, tal y como puede observarse en la barra de estado.

![](../../../../assets/drive/1-Z-wUYZfcGDizQ_Kkp8TUYXTs-KnM67H.png)

!!! warning
    Nota: no es posible reactivar documentos que incluyan transacciones con cantidades que excedan la cantidad de stock existente para un determinado producto en un determinado hueco. La única excepción es cuando la configuración del hueco permite Over Issue. Para más información, visite [Hueco](../../../../user-guide/etendo-classic/basic-features/warehouse-management/setup.md#storage-bin).

### Contabilización masiva

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

La funcionalidad de **contabilización masiva** permite al usuario contabilizar o deshacer la contabilización de múltiples registros seleccionando los registros correspondientes y haciendo clic en el botón **Contabilización masiva**.

Además, el estado contable del/de los registro/s se muestra en la barra de estado, en vista de formulario, o en una columna, en vista de rejilla.

!!! info
    Para más información, visite [la guía de usuario del módulo Bulk Posting](../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).

### Finalización masiva

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Essentials Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Essentials Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=39AC2D9F72124AC7A1D0A3D005293C9E){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Essential Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/essentials-extensions/release-notes.md).

La funcionalidad de **finalización masiva** permite al usuario completar, reactivar o anular múltiples registros seleccionándolos y haciendo clic en el botón **Finalización masiva**. Esto facilita y hace más eficiente la gestión de registros, reduciendo el tiempo dedicado a procesar registros individuales.

!!! info
    Para más información, visite [la guía de usuario del módulo Bulk Completion](../../optional-features/bundles/essentials-extensions/bulk-completion.md).
## Albaranes pendientes de recibir

:material-menu: `Aplicación` > `Gestión de Compras` > `Transacciones` > `Albaranes pendientes de recibir`

Esta ventana permite al usuario:

- **Usar las opciones de Filtro** para acotar la búsqueda de pedidos de compra pendientes de entregar. Es posible buscar por:
    - Terceros
    - Desde Fecha de pedido -> Hasta Fecha de pedido
    - Número de Pedido de compra
- Introducir una **"Fecha de recepción".**
- **Seleccionar** las **"Líneas de pedido de uno o varios pedidos de compra" entregadas**, que se muestran agrupadas por Terceros y Pedido de compra.
- **Cambiar** la **"Cantidad"** de los bienes que se están recibiendo, si es necesario.
- **Introducir** la **"Ubicación del albarán"** o hueco dentro de un almacén.
- **Procesarlo** para crear los albaranes correspondientes.

![Ventana de albaranes pendientes de recibir](../../../../assets/drive/1hGrJ6YXXd1p20ZdLQefX1o6_8nVogOd8.png)
## Factura (Proveedor)

:material-menu: `Aplicación` > `Gestión de Compras` > `Transacciones` > `Factura (Proveedor)`

### Vista general

La ventana **Factura (Proveedor)** permite al usuario registrar y gestionar las facturas del proveedor.

Esta etapa de la cadena **normalmente viene después de la contabilización y gestión de los "Albaranes (Proveedor)"**.

Una factura de compra es un estado detallado de los bienes o servicios proporcionados por un proveedor. Indica la cantidad y el precio de cada producto o servicio proporcionado o por proporcionar.

Los proveedores podrían enviar la/s factura/s de compra correspondiente/s junto con el/los albarán/es de entrega adjunto/s a los bienes, lo que implica que las Facturas (Proveedor) pueden generarse automáticamente desde la ventana **Albarán (Proveedor)**, pero es posible que no sea el caso; por lo tanto, una **Factura (Proveedor)** también puede crearse desde cero en la ventana **Factura (Proveedor)**.

Los gastos de compra pueden reconocerse tan pronto como la factura de compra se contabilice; sin embargo, si se configura un plan de gasto postpuesto, es posible diferir el reconocimiento del gasto según sea necesario.

Las facturas de proveedor pueden registrarse, contabilizarse y gestionarse en la sección de cabecera de la ventana **Factura (Proveedor)**.
### Cabecera

**Cabecera** lista los principales términos y condiciones relacionados con la factura de proveedor.

!!! info
    En la mayoría de los casos, el campo principal (y el único) necesario para crear un nuevo documento de factura de proveedor es el campo **Terceros**. Todos los demás campos se rellenarán automáticamente en función del **Terceros** seleccionado, las preferencias del Usuario conectado y otros parámetros por defecto del sistema.

Algunos otros campos a tener en cuenta son:

- **Documento transacción** con valor por defecto "Factura AP" o el *tipo de documento* de factura de proveedor, que puede cambiarse manualmente a "Nota de crédito AP" o "Factura de proveedor revertida".
  - Los tipos de documento "Nota de crédito AP" y "Factura de proveedor revertida" pueden considerarse facturas de proveedor de abono; la diferencia entre ellas es que:
    - El tipo "Nota de crédito AP" debe contener o bien una "Cant.facturada" > 0 o bien un "Imp. línea" > 0.  
      Lo anterior implica que las facturas configuradas como "Nota de crédito" no deberían estar relacionadas con "Parte" o "Envíos".
    - El tipo "Factura de proveedor revertida" debe contener o bien una "Cant.facturada" < 0 o bien un "Imp. línea" < 0. Estos son los tipos de factura que pueden estar relacionados con "Parte" o "Envíos" de devolución.
- **Nº de documento**. Puede rellenar manualmente el número de factura del proveedor en este campo, si la secuencia de documento asociada al documento transacción "Factura AP" está configurada para permitirlo; en caso contrario, el sistema lo proporcionará automáticamente como un número de factura de proveedor "Interno".
- **Fecha de la factura**: la fecha en la que se registra la factura. Se utiliza para calcular cuándo vence el pago de la factura. Por defecto es la fecha actual, pero siempre puede cambiarse.
- **Fecha contable**: la fecha que se utilizará en el asiento de contabilización de la Factura (Proveedor) en el libro mayor. Por defecto es el campo **Fecha de la factura**, pero siempre puede cambiarse.
- **Condiciones de pago**: indica **cómo** debe pagarse una factura. Se establece por defecto según la pestaña Proveedor/Acreedor de la ventana *Terceros*.
- **Método de pago**: define **cuándo** debe pagarse una factura de proveedor. Se establece por defecto según la pestaña Proveedor/Acreedor de la ventana *Terceros*.
- **Referencia del Proveedor**: es un campo no obligatorio que puede utilizarse para introducir el número de factura del proveedor.

Hay 3 formas de introducir líneas en la factura de proveedor; dos de ellas desde la cabecera de la factura y la última desde la pestaña **Líneas**:

1. Seleccionando productos de pedidos o albaranes pendientes de facturar mediante los botones **Crear Líneas Desde Pedido** y **Crear Líneas Desde Albarán**.
2. Copiando todos los productos de la factura elegida seleccionada en el histórico de todas las facturas para diferentes terceros mediante el botón **Copiar líneas**.
3. Manualmente, línea a línea, en la pestaña **Líneas**. Esta opción se utiliza si el documento subyacente (Pedido de compra o Albarán (Proveedor)) no existe en el sistema antes de que se realice la facturación.

El botón **Completar** finaliza la creación del documento de factura con la cumplimentación de la pestaña **Plan de pagos** y la sección Monitor de pagos en la Cabecera. Si en las líneas hay productos BOM no almacenables y no se han explotado, el botón Completar los explotará automáticamente.

Una vez completada, una factura de proveedor puede:

- **contabilizarse** en el libro mayor utilizando el botón [Contabilizar](#post)
- **anularse** utilizando el botón [Reactivar](#reactivate)
- y **pagarse** utilizando el botón [Añadir pago](#add-payment).

![Ventana de factura de proveedor](../../../../assets/drive/1JvS1mOjiiyATJENTs5SuQIyEAr-UHmE3.png)
### Líneas

Una vez que la cabecera de la **Factura (Proveedor)** se ha completado correctamente y se ha guardado, las líneas de la factura de compra pueden registrarse en esta solapa.

Las líneas enumeran cada producto que se va a comprar y sus características.

Los campos a tener en cuenta son:

- **Línea de factura financiera** se selecciona cuando la línea de factura no es un producto, sino una cuenta no configurada como producto sino como un *Concepto contable*, o un inmovilizado no configurado como producto.  
  Al seleccionarla, el campo de producto desaparece de la pantalla y aparece un campo de cuenta relacionado con la línea de la factura de compra.
- **Valor atributos**: el campo se muestra si el producto de la línea tiene *Atributo* (color, talla, número de serie o varios de ellos a la vez, etc.).
- **Línea de Pedido de compra y Línea de Albarán (Proveedor)**: referencias a la línea del pedido de compra y a la línea del albarán que se está facturando.

Tal y como ya se ha mencionado, los gastos de compra pueden diferirse, por lo que no se reconocen en la fecha contable de compra, sino dentro de un número determinado de periodos contables.

Cuando se crea una línea de factura de compra, es posible definir a nivel de línea si la línea va a provocar que el gasto se difiera. Los campos relevantes son:

- **Gasto postpuesto**: cuando se marca este indicador, el grupo de campos del plan de gastos pasa a ser visible, permitiendo a los usuarios configurar los tres campos siguientes.
- **Tipo de plan de gastos**: este campo especifica la frecuencia de la distribución del gasto, que actualmente es "mensual".
- **Número de periodo**: este campo especifica la duración de un plan de gastos.  
  Por ejemplo, si una empresa compra un seguro empresarial para la duración de un año, el número de periodos a introducir sería 12, ya que la empresa desea distribuir ese gasto durante 12 meses.
- **Periodod inicial**: el primer periodo abierto en el que se va a reconocer el gasto.

Estos campos pueden establecerse por defecto si están configurados para el **Producto**.

Si se configura un plan de gastos, implica una contabilidad específica de la factura de compra.

El botón **Explotar** se muestra al seleccionar una línea con un producto BOM no almacenable y el producto aún no está explotado. Al explotar un producto, los componentes de la lista de materiales de los que consta el producto seleccionado se muestran en la factura. Una vez explotado, no puede comprimirse. Debe eliminar todas las líneas (primero los componentes de la lista de materiales y después el producto BOM) e insertar de nuevo el producto BOM no almacenable.

El botón **Match LC Cost** se muestra cuando la línea del pedido de compra contiene una "cuenta" o un "producto" configurado como *Tipo de Landed Cost*.

Este botón de proceso permite **conciliar** tanto el landed cost "**estimado**" registrado en la ventana de *Landed Cost* como el que se está **facturando** en la línea de factura. Ambos deben ser del **mismo tipo de landed cost**.

Una vez seleccionado, el botón **"Match LC Cost"** abre la **ventana de selección y edición "Match LC Cost"**.

En esta ventana solo se mostrarán documentos de Landed Cost procesados. Permite seleccionar el landed cost correspondiente, introducir un importe a conciliar en el campo "Imp. Asociado" y, a continuación, seleccionar la casilla de verificación "**Procesar Asociación**".

!!! warning
    Tenga en cuenta que, si la casilla de verificación "Procesar Asociación" no se selecciona aquí, la conciliación de landed cost deberá procesarse en la ventana de *Landed Cost* mediante el botón **Procesar Asociación**.

#### Línea de impuesto

La información de impuestos de línea se completa automáticamente para cada línea de factura de compra al completar la factura.

La solapa de solo lectura **Línea de impuesto** detalla la información de impuestos para cada línea de una factura de compra en función de su solapa **Impuesto**, que se completa automáticamente según la configuración de impuestos.
### Impuesto

Esta sección resume la información relacionada con los impuestos para toda la **Factura (Proveedor)**. Contiene tantos registros como tipos impositivos utilizados en la factura.

El campo **Importe del impuesto** refleja el valor del impuesto calculado automáticamente en función del tipo impositivo y de la configuración de la base imponible.

!!! info 

    Es posible añadir una funcionalidad que permita ajustes controlados en los importes de impuestos de la factura para conciliar pequeñas **diferencias de redondeo** con sistemas externos o cuando las facturas se presentan a **entidades gubernamentales**. Es compatible tanto con facturas de **Ventas** como de **Compra**, ofrece **ajustes manuales y automatizados** para correcciones mínimas a nivel de céntimos y registra todos los cambios para garantizar la **auditabilidad**, asegurando que el total final de la factura coincida con requisitos externos, gubernamentales o regulatorios.
    
    Para poder incluir esta funcionalidad, debe estar instalado el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. 
    
    Para más información, visite: [Guía de usuario de Ajustar impuesto de factura](../../optional-features/bundles/financial-extensions/adjust-invoice-tax.md)
    
    Esta funcionalidad es compatible a partir de Etendo 23.
### Botones

#### Contabilizar/Descontabilizar

Una factura de proveedor puede contabilizarse en el libro mayor cuando sea necesario en una **Fecha contable** determinada mediante este botón de proceso. Una vez contabilizada, puede descontabilizarse con el mismo botón.

#### Reactivar

![pop-up-reactivate](../../../../assets/user-guide/etendo-classic/basic-features/procurement-management/transactions/pop-up-reactivate.png)

Mediante este botón, el usuario tiene dos opciones: reactivar o anular la factura **Completada**.

En el caso de la opción **Reactivar**, el registro pasa de estado **Completada** a estado **Borrador**.

Con la opción **Anular**, es posible anular totalmente una factura de proveedor. Esta acción crea un nuevo documento que revierte la factura.

![pop-up-void](../../../../assets/user-guide/etendo-classic/basic-features/procurement-management/transactions/popup-void.png)

La anulación permite especificar una **Fecha de anulación** y una **Fecha contable de anulación** para el nuevo documento que revierte la factura.

Ambos campos de fecha anteriores toman la fecha actual como fecha predeterminada y validan que las fechas introducidas no sean anteriores a la fecha de la factura y a la fecha contable de la factura, respectivamente.

Además, esta ventana de proceso incluye un campo **Referencia del Proveedor** para introducir el número de referencia del proveedor con el fin de referirse al documento revertido resultante de la anulación de la factura. Aquí puede introducir el número correspondiente o dejar el campo en blanco para completarlo más adelante.

Esta acción implica que:

- Etendo genera automáticamente un nuevo documento en la ventana *Factura (Proveedor)* que revierte la factura original.
- Etendo también informa del número del nuevo documento. Este nuevo documento se crea tal y como se describe a continuación:
    
    El documento de transacción utilizado por Etendo es la *Factura Rectificativa*. Este documento es exactamente igual que el original que se está revirtiendo, pero la cantidad facturada es negativa.

- Una vez creado el nuevo documento, puede cambiar tanto la *Fecha de la factura* como la *Fecha contable* del nuevo documento antes de contabilizarlo. También puede introducir la **Referencia del Proveedor** si no se introdujo antes o modificar la existente.

- La solapa *Factura Rectificativa* lista la factura original que se está revirtiendo, ya que ahora ambas quedan vinculadas.

    Y también es posible anular parcialmente una factura de proveedor mediante:

    - La creación manual de cualquiera de los documentos de compra revertidos disponibles, en la ventana [Factura (Proveedor)](#purchase-invoice):
        
        - **Nota de crédito** o
        - **Factura Rectificativa**

    - que, además, deben vincularse manualmente a la/s factura/s que se están revirtiendo en la solapa **Factura Rectificativa**.
    
    Para obtener más información, visite [Factura Rectificativa](../sales-management/transactions.md#reversed-invoices).

    La contabilización de la **Nota de crédito** tiene el mismo aspecto que la contabilización de la **Factura Rectificativa**. La principal diferencia entre estos dos tipos de documento de compra revertidos es:

    - La cantidad facturada de la **Nota de crédito** es una cantidad positiva.
    - y la cantidad de la **Factura Rectificativa** es una cantidad negativa.

    !!!note
        Recomendamos encarecidamente utilizar el tipo de documento **Factura Rectificativa** al anular parcialmente facturas de proveedor.

#### Añadir pago

Se pueden realizar pagos contra una factura de proveedor mediante el botón **Añadir pago**, que abre la ventana emergente de Añadir pago.

#### Contabilización masiva

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

La funcionalidad de **Contabilización masiva** permite al usuario contabilizar o descontabilizar múltiples registros seleccionando los registros correspondientes y haciendo clic en el botón **Contabilización masiva**.

Además, el estado de contabilización del/de los registro/s se muestra en la barra de estado, en vista de formulario, o en una columna, en vista de rejilla.

!!! info
    Para más información, visite [la guía de usuario del módulo Bulk Posting](../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).

#### Finalización masiva

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Essentials Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Essentials Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=39AC2D9F72124AC7A1D0A3D005293C9E){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Essential Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/essentials-extensions/release-notes.md).

La funcionalidad de **Finalización masiva** permite al usuario completar, reactivar o anular múltiples registros seleccionándolos y haciendo clic en el botón **Finalización masiva**. Esto facilita y hace más eficiente la gestión de registros, reduciendo el tiempo dedicado a procesar registros individuales.

!!! info
    Para más información, visite [la guía de usuario del módulo Bulk Completion](../../optional-features/bundles/essentials-extensions/bulk-completion.md).

!!!warning
    La opción de anulación masiva falla cuando está instalado el módulo [Validación de Factura (Proveedor)](../../optional-features/bundles/procurement-extensions/purchase-invoice-validation.md). Esto se debe a que el módulo incluye una preferencia predeterminada que impide la duplicación de facturas con el mismo tercero, ejercicio contable y referencia del proveedor. Dado que la anulación masiva intenta revertir facturas, se produce duplicación, ya que la referencia del proveedor para cada factura revertida no puede modificarse. Como resultado, el módulo impide que el proceso de anulación masiva funcione.
    ![popup-bulk-void](../../../../assets/user-guide/etendo-classic/basic-features/procurement-management/transactions/popup-bulk-void.png)

#### Eliminar pago

El objetivo de la funcionalidad de **Eliminación de pagos** es eliminar y reactivar pagos de forma ágil y sencilla. Además, permite eliminar y reactivar transacciones bancarias y conciliaciones.

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

Desde esta ventana, es posible eliminar pagos asociados a una factura de proveedor seleccionando el documento correspondiente y, a continuación, haciendo clic en el botón **Eliminar pago**. Si existe un pedido asociado a la factura, también se eliminará la relación de este pedido con el pago en cuestión (ventana Pedido de compra > solapa **Plan de pagos**).

Si el pago está incluido en la cuenta financiera, es decir, si está en estado Depositado/Retirado no conciliado, la transacción en dicha cuenta también se eliminará (ventana Cuenta financiera > solapa Transacción).

Si el pago está conciliado mediante un método automático, entonces, además de la transacción en la cuenta financiera, se eliminará la línea del extracto bancario a la que estaba vinculada (ventana Cuenta financiera > Extractos bancarios importados) y la línea correspondiente de la conciliación bancaria (Cuenta financiera > Conciliaciones).

!!! info
    Si el pago está contabilizado, el asiento contable también se elimina.

![](../../../../assets/user-guide/etendo-classic/basic-features/procurement-management/transactions/PRpic4.png)

#### Desanular

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Financial Extensions Bundle. Para ello, siga las instrucciones del [marketplace](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

Etendo permite al usuario reactivar facturas de proveedor anuladas seleccionando la/s necesaria/s y haciendo clic en el botón **Desanular**.

![](../../../../assets/drive/1UisxZzbpppLvN_rdL__TJg8tLeh5sMfW.png)

Una vez finalizado el proceso, el estado de la factura de ventas pasa a **Completada**.

???+ note 
    En el caso de la versión estándar del módulo, es necesario que el usuario también desanule la factura revertida correspondiente.
!!! warning
    Recuerde que este proceso de reactivación afecta a la contabilidad, ya que, si la información original no se elimina manualmente del documento reactivado, la información contable se duplicará.

!!! info
    Consulte la documentación técnica sobre [Advanced Financial Docs Processing](../../../../developer-guide/etendo-classic/bundles/financial-extensions-bundle/overview.md#advanced-financial-docs-processing) para ampliar el proceso.

#### Modificar Plan de Pagos

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el módulo Advanced Bank Account Management del Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

El módulo Advanced Bank Account Management añade un nuevo campo a la cabecera de la ventana Factura (Proveedor): **Cuenta bancaria**. Este campo se completa automáticamente con la cuenta bancaria relacionada con la dirección o el tercero de la factura. Además, se añade el botón **Modificar Plan de Pagos** para una mejor gestión de pagos.

![bank-account.png](../../../../assets/user-guide/etendo-classic/basic-features/procurement-management/transactions/bank-account.png)

!!! info
    Para más información, visite la [guía de usuario de Advanced Bank Account Management](../../optional-features/bundles/financial-extensions/advanced-bank-account-management.md).
### Intercompany

En caso de que el usuario tenga que crear pedidos o facturas entre dos o más organizaciones que son diferentes pero pertenecen a la misma entidad, esta funcionalidad permite generar automáticamente el documento inverso correspondiente.

!!! info
    Para más información, visite [la guía de usuario del módulo Intercompany](../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/intercompany.md).

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}. Para más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).
## Facturas cuadradas

:material-menu: `Aplicación` > `Gestión de Compras` > `Transacciones` > `Facturas cuadradas`

Esta ventana ayuda al usuario a contabilizar las discrepancias entre el inventario y la contabilidad financiera de aquellos artículos para los que se contabilizaron los correspondientes albaranes.

Las discrepancias mencionadas anteriormente se deben principalmente a diferencias entre:

- el **precio unitario neto del artículo registrado al registrar el pedido de compra** y, posteriormente, **al contabilizar el correspondiente Albarán (Proveedor)**.
- y el **precio unitario neto "final" del artículo registrado al contabilizar la factura (proveedor)**.

En la ventana, hay un listado de todas las facturas que están asociadas a albaranes. La asociación de los documentos se realiza cuando los documentos se crean utilizando la información del otro documento: por ejemplo, haciendo clic en **Crear factura del albarán** en el albarán o haciendo clic en el botón **Crear líneas de** al crear un albarán para seleccionar la factura.

![Ventana Facturas cuadradas](../../../../assets/user-guide/etendo-classic/basic-features/procurement-management/transactions/matched-purchase-invoices.png)

#### Factura cuadrada

La solapa **Factura cuadrada** lista cada línea de factura contabilizada vinculada a las correspondientes líneas de albarán, que también podrían estar contabilizadas o no.

Existe un botón de cabecera "**Contabilizar**" que es el que contabiliza las discrepancias entre inventario y contabilidad financiera, si las hubiera, una vez seleccionada la línea adecuada.

El proceso general para contabilizar las discrepancias en contabilidad se detalla a continuación:

Un documento de *Factura de conciliación* puede contabilizarse si se ha calculado el coste de los productos incluidos en un *Albarán (Proveedor)*. Para obtenerlo:

- Se requiere una *Regla de cálculo de costes* validada en la entidad legal de la Factura cuadrada,
- y debe ejecutarse el proceso en segundo plano *Proceso en segundo plano de cálculo de costes*.

En el caso de productos de "Gasto" que no tengan seleccionada la casilla "Ventas", es posible utilizar el precio de compra del producto en lugar del coste del producto siempre que esté seleccionada la casilla *Registrar con precio de compra*. En este caso, es necesario que un "Pedido de compra" esté relacionado con el "Albarán (Proveedor)".

#### Contabilidad

Información contable relacionada con las facturas cuadradas.

### Contabilización masiva

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

La funcionalidad de **Contabilización masiva** permite al usuario contabilizar o descontabilizar múltiples registros seleccionando los registros correspondientes y haciendo clic en el botón **Contabilización masiva**.

Además, el estado de contabilización del/de los registro/s se muestra en la barra de estado, en la vista de formulario, o en una columna, en la vista de rejilla.

!!! info
    Para más información, visite [la guía de usuario del módulo Bulk Posting](../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).
## Devolución a proveedor (RTV)

:material-menu: `Aplicación` > `Gestión de Compras` > `Transacciones` > `Devolución a proveedor`

Esta ventana permite al usuario crear un documento de Devolución de material en caso de que un producto determinado deba enviarse de vuelta, ya sea para su devolución con reembolso o sustitución, o para ser reparado.

### Cabecera

El usuario puede crear un pedido de compra y procesarlo.

Una vez que el documento de Devolución de material es aceptado por el Proveedor, el usuario puede procesarlo haciendo clic en el botón **Registrar**. El documento cambia de *Borrador* a *Registrado*.

![Ventana de devolución a proveedor](../../../../assets/drive/1PKb2NIyq5HtvO_4abDPQjajObdcGFiPH.png)

Solo los documentos *Registrados* pueden enviarse al proveedor.

!!! warning
    Tenga en cuenta que el botón **Elegir/Editar lineas** desaparece cuando el documento de Devolución a proveedor está en estado *Registrado*.

### Líneas

Añada productos para incluirlos en su pedido de compra. Cada producto se añade creando una línea.

La solapa Líneas no es editable, ya que las líneas devueltas siempre provienen de líneas de albarán, para evitar:

- Ver valores positivos mientras que en la BD son negativos.
- Introducir líneas que no estén vinculadas a las líneas del albarán original.
- Editar atributos, productos y, por tanto, tener productos o atributos diferentes de la línea de envío.

Para introducir nuevas líneas debe hacer clic en el botón de proceso ELEGIR/EDITAR Líneas.

**Aspectos a tener en cuenta:**

- Los únicos campos editables son:
  - **Devuelto**: cantidad que desea devolver. Al seleccionar la fila, la cantidad no se establece por defecto, ya que el sistema no puede saber cuántos artículos se devuelven.
  - **Precio unitario (field)**: precio del pedido de compra original.
  - **Motivos de devolución**: el motivo por el que devuelve el artículo.
  - y **Unidad de Devolución**, solo en caso de que esté habilitada la preferencia *unidad de medida alternativa (AUM)*.  
    En ese caso, se muestra la AUM "principal" del producto para el flujo de compra si existe; en caso contrario, se muestra la **Unidad** del producto. El usuario siempre puede cambiarla a la **Unidad** del producto.

Puede definir los Motivos de devolución a nivel de cabecera. En este caso, al seleccionar una línea, esta hereda lo seleccionado en la cabecera, pero puede modificarlo como desee.

- Solo se pueden seleccionar documentos de albarán de material que aún no hayan sido devueltos; en caso de que una línea de albarán se haya devuelto completamente, no se mostrará.
- Cuando una línea de albarán se ha devuelto parcialmente, aún puede devolver el resto. Lo que ya ha devuelto para esa línea se muestra en el campo **Cant. devuelta otras R**.

**Validación:**

- No se permite devolver una cantidad superior a la **Cant. envío/recepción**. En caso de hacerlo, se muestra un mensaje.
- Tenga en cuenta que esta validación tiene en cuenta el campo **Cant. devuelta otras RM**.

!!! info
    Para editar una línea debe volver a hacer clic en el botón **Elegir/Editar lineas**; la línea aparece seleccionada y entonces puede modificar cualquiera de los campos editables.

!!! info
    Para eliminar una línea debe desmarcar la línea y, a continuación, hacer clic en Hecho.

### Finalización masiva

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Essentials Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Essentials Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=39AC2D9F72124AC7A1D0A3D005293C9E){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Essential Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/essentials-extensions/release-notes.md).

La funcionalidad de Finalización masiva permite al usuario completar, reactivar o cerrar múltiples registros seleccionándolos y haciendo clic en el botón **Finalización masiva**. Esto facilita y hace más eficiente la gestión de registros, reduciendo el tiempo dedicado a procesar registros individuales.

!!! info
    Para más información, visite [la guía de usuario del módulo Bulk Completion](../../optional-features/bundles/essentials-extensions/bulk-completion.md).
## Devolución a albarán de proveedor

:material-menu: `Aplicación` > `Gestión de Compras` > `Transacciones` > `Devolución a albarán de proveedor`

Desde esta ventana, el usuario puede entregar al proveedor los bienes devueltos.

### Cabecera

El usuario puede crear y editar un albarán.

El campo **RMA ref. proveedor** se completa automáticamente o no en función de:

- Si se rellena antes de seleccionar una línea, entonces no se completará automáticamente para evitar sobrescribirlo.
- Si selecciona una/s línea/s donde todas pertenecen al mismo documento de **Devolución a proveedor**, se completará automáticamente.
- Si selecciona una/s línea/s pero una de ellas pertenece a un documento de **Devolución a proveedor** diferente, entonces no se completará automáticamente.

Una vez que el documento está listo, puede procesarlo haciendo clic en el botón **Completar**. El documento cambia de *Borrador* a *Completada*.

!!! warning
    Tenga en cuenta que el botón **Elegir/Editar lineas** desaparece cuando el documento de Devolución a proveedor está en estado *Completada*.

![Devolución a albarán de proveedor](../../../../assets/drive/1wuiYHH8xsIwjLRgp0VzWUqAtev43BzD8.png)

Para facturar estos documentos debe usar la ventana **Factura (Proveedor)**. Se contemplan todos los escenarios:

- Si el proveedor envía una factura solo para ese documento específico, debe seleccionar un tipo de documento *Factura de compra rectificativa* y después seleccionar las líneas mediante el botón *Crear líneas*.
- Si el proveedor envía una factura con el pedido de compra original más el pedido de materiales devueltos, debe seleccionar un tipo de documento *Factura (Proveedor)* y después seleccionar las líneas mediante el botón *Crear líneas*.
- Si el proveedor no envía una factura por el pedido de materiales devueltos pero quiere mantenerlo como crédito para que usted pueda usarlo más adelante, debe:
  - Crear una *Factura de compra rectificativa* para estos materiales devueltos.
  - Dejarlo como crédito para usarlo más adelante mediante la ventana **Pago**.
  - Cuando cree la **Factura (Proveedor)** para el **Pedido de compra** original, puede consumir ese crédito.

### Líneas

Añada productos que estén incluidos en su albarán. Cada producto se muestra en su propia línea.

La solapa Líneas no es editable, ya que las líneas siempre provienen de las líneas de devolución a proveedor, para evitar:

- Ver valores positivos mientras que en la BD son negativos.
- Introducir líneas que no estén vinculadas a líneas de devolución.
- Editar atributos, productos y, por tanto, tener productos o atributos diferentes a los de la línea de devolución.

!!! info
    Para introducir nuevas líneas, el usuario debe hacer clic en el botón ELEGIR/EDITAR lineas.

**Aspectos a tener en cuenta:**

- Los campos editables son:
  - **Enviar cantidad**, ese valor se establece automáticamente cuando selecciona la línea,
  - y **Unidad de Devolución**, solo en caso de que esté habilitada una preferencia de unidad de medida alternativa (AUM); independientemente de ello, la unidad del producto siempre se muestra ahí por defecto.  
    El usuario puede cambiarla si es necesario, a la AUM primaria del producto configurada para el flujo de compras.
- El usuario solo puede seleccionar líneas de **Devolución a proveedor** que estén pendientes de ser enviadas a ese proveedor específico.
- El sistema propone los diferentes huecos desde los que se puede recoger el artículo. Dependiendo de cómo esté configurado el producto, pueden darse tres escenarios:
  - Producto con un atributo de instancia (p. ej.: número de serie): el sistema propondrá solo un hueco, tal y como se muestra arriba.
  - Producto con un atributo no de instancia (p. ej.: color): el sistema podría proponer varios huecos. Véase la imagen inferior.
  - Producto sin atributos: similar al segundo escenario.

**Validaciones:**

- No está permitido enviar más que la **Cantidad disponible**.
- No está permitido enviar más que la cantidad **Pendiente**.
- El sistema también valida que no puede enviar más que la cantidad **Pendiente** al seleccionar ambas líneas.

!!! info
    Para editar una línea, debe hacer clic de nuevo en el botón **Elegir/Editar lineas**; la línea aparece seleccionada y entonces puede modificar cualquiera de los campos editables.

!!! info
    Para eliminar una línea, debe desmarcar la línea y después hacer clic en Hecho.

Si no hay suficiente stock disponible para un producto en una línea seleccionada, será posible definir una cantidad a enviar y seleccionarla si existe al menos un hueco con estado de inventario de sobreemisión para el almacén de la **Devolución a albarán de proveedor**; en este caso, la nueva línea lo usará como hueco y se creará un stock negativo cuando se procese el documento.

#### Contabilidad

El envío de RTV puede contabilizarse **si la tabla "MaterialMgmtShipmentInOut" está** activa para contabilidad **en la configuración del libro mayor correspondiente.**

### Contabilización masiva

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

La funcionalidad de Contabilización masiva permite al usuario contabilizar o descontabilizar múltiples registros seleccionando los registros correspondientes y haciendo clic en el botón **Contabilización masiva**.

Además, el Estado de contabilidad del/de los registro/s se muestra en la barra de estado, en vista de formulario, o en una columna, en vista de rejilla.

!!! info
    Para más información, visite [la guía de usuario del módulo Bulk Posting](../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).
## Landed Cost

:material-menu: `Aplicación` > `Gestión de Compras` > `Transacciones` > `Landed Cost`

La ventana **Landed Cost** permite al usuario asignar costes adicionales como flete, seguro o aranceles a uno o varios **Albarán (Proveedor)**; por lo tanto, el coste de los productos incluidos en el/los albarán(es) se ajusta según corresponda.

Todos esos costes son necesarios para colocar el producto en el almacén de la organización.

Cada vez que se registra un landed cost para un albarán de productos valorado a coste "Average", se crea un ajuste de landed cost.

Los landed costs distribuidos y asignados a productos valorados a coste "Average" implican un cambio en el valor de inventario del producto. En otras palabras, el coste calculado ("Coste Total") del albarán de productos deberá ajustarse igual que el coste "Average" del producto.

!!! info
    Tenga en cuenta que el "Coste Unitario" de la transacción del albarán no cambiará, ya que este tipo de ajuste no es un ajuste de coste unitario, sino un coste "extra".

Todo lo anterior tendrá un impacto contable; por lo tanto, el valor de inventario del producto puede ser el mismo que el valor contable del producto.

Por otro lado, si se registra un landed cost para un albarán de productos valorado a coste "Standard", no se creará ningún ajuste de coste, sino una "Variance" entre el coste "standard" definido para el producto y su coste "actual". Esta variación deberá contabilizarse en una cuenta de "Landed Cost Variance", para que pueda analizarse posteriormente.

La ventana **Landed Cost** permite:

- registrar landed cost "**estimated**" que posteriormente puede conciliarse con el landed cost "actual" por **Tipo de Landed Cost**,
- o registrar directamente landed cost "**actual**" por **Tipo de Landed Cost**.

La ventana **Landed Cost** también permite contabilizar los landed costs una vez procesados.

Escenario de Landed Cost "**Estimated**":

- Se registra un pedido de compra y, después, el correspondiente **Albarán (Proveedor)** y la **Factura (Proveedor)**.  
  En este punto se calcula el coste "average" de los productos incluidos en el albarán.
- Después, los landed costs "estimated" (p. ej., costes de flete) se asignan al **Albarán (Proveedor)** y se registran en la ventana **Landed Cost**.  
  El coste de los productos incluidos en el albarán se ajusta entonces igual que la contabilidad del inmovilizado del producto.
- Después, se registra una **Factura (Proveedor)** que incluye el importe real del coste de flete y se contabiliza en el libro mayor.
- A continuación, es posible conciliar el landed cost "estimated" con el landed cost "invoiced".  
  El coste de los productos incluidos en el albarán se ajusta una vez más si existen diferencias entre los importes de landed cost estimados y reales.

Escenario de Landed Cost "**Actual**":

- Se registra un pedido de compra y, después, el correspondiente **Albarán (Proveedor)** y la **Factura (Proveedor)**.  
  En este punto se calcula el coste "average" de los productos incluidos en el albarán.
- Después, se crea un documento de landed cost para registrar el landed cost real en el **Albarán (Proveedor)**.  
  El coste de los productos incluidos en el albarán se ajusta entonces igual que la contabilidad del inmovilizado del producto.

En resumen, la funcionalidad de landed cost sigue los siguientes pasos detallados:

- **Landed Cost Process**:
  - Se crea un documento de landed cost que incluye tantos tipos de landed cost e importes como sea necesario.
  - Este documento de landed cost puede relacionarse con un único **Albarán (Proveedor)**, con varios **Albarán (Proveedor)** o con líneas específicas de **Albarán (Proveedor)**.
  - Este documento de landed cost puede registrar landed cost "actual" en caso de seleccionar la factura correspondiente; por lo tanto, el proceso y la conciliación del landed cost se realizan en un solo paso.
  - Se procesa el landed cost.
    - Esta acción crea un *ajuste de landed cost* vinculado al documento de landed cost.  
      Este ajuste de coste tiene tantas líneas de ajuste como productos incluidos en el/los **Albarán (Proveedor)** seleccionados; por lo tanto, el coste de esos productos se ajusta según corresponda.
- **Landed Cost Post**:
  - Una vez que un documento de landed cost se procesa, puede contabilizarse en el libro mayor; por lo tanto, también se ajusta la contabilidad del inmovilizado del/de los producto(s).
- **Landed Cost Matching**:
  - La factura de landed cost se registra y se contabiliza en el libro mayor posteriormente.
  - Después, el landed cost "estimated" registrado en el documento de landed cost puede conciliarse con los landed costs reales por **Tipo de Landed Cost** en la factura de landed cost.
  - La conciliación de landed cost puede generar un ajuste de coste adicional para el/los producto(s) si los importes de landed cost estimados no fueron iguales a los importes de landed cost reales.
- **Landed Cost Matching Post**:
  - Una vez conciliados los landed costs, pueden contabilizarse; por lo tanto:
    - la contabilidad del inmovilizado del/de los producto(s) se ajusta una vez más si corresponde,
    - y la contabilización del landed cost obtiene la *Dimensión de contabilidad* de la factura de landed cost.
### Cabecera

Un documento de **Landed Cost** puede crearse, procesarse y contabilizarse en esta ventana.

![Cabecera de landed cost](../../../../assets/drive/1YND6qqNXSCzLiiq_PICSVr3GymXZi6_o.png)

Algunos campos a tener en cuenta son:

- **Organización**: es la organización o entidad legal para la cual es necesario registrar el landed cost.
- **Fecha de Referencia**: es la fecha en la que se está creando el documento de landed cost.

**Costo**

Un documento de **Landed Cost** puede tener tantos costes (líneas) como tipos de landed cost a asignar a los **Albarán (Proveedor)** seleccionados.

![Solapas de landed cost](../../../../assets/drive/1jbfoYTDqyRZiF3bTwPQkG8OmjpLr0zau.png)

Algunos campos a tener en cuenta son:

- Tipo de Landed Cost: es el tipo de landed cost que se va a asignar al/los albarán(es) o a la(s) línea(s) de albarán seleccionadas en la solapa **Entrega**.
- **Línea de la factura**: sirve para seleccionar la línea de factura de landed cost correspondiente, si ya está registrada, que coincida con el tipo de landed cost que se está introduciendo.  
  Si se selecciona una línea de factura, el importe de la línea de factura se completa en el siguiente campo "Importe".
- **Importe**: es el importe del tipo de landed cost. Este importe puede ser "estimado" o "real" en caso de seleccionar una línea de factura.
- **Moneda**: es la moneda del tipo de landed cost.
  - Es importante remarcar que un documento de landed cost puede incluir tantos tipos de landed cost como se requiera, en la moneda requerida.  
    Por ejemplo, un documento de landed cost puede incluir dos líneas de tipo de landed cost, una en USD y otra en EUR.  
    En este escenario, se creará un ajuste de landed cost que incluirá dos líneas. Los importes del ajuste de coste se calcularán en la moneda configurada para la entidad legal a la que pertenece la transacción de producto.
- **Algoritmo de Distribución de Landed Cost**: hay un algoritmo disponible distribuido por Etendo que es "Distribución por importe".  
  Este algoritmo distribuye el importe del tipo de landed cost proporcionalmente por el importe de la(s) línea(s) de albarán entre el/los albarán(es) seleccionados.

Una vez que se ha(n) seleccionado albarán(es) en la solapa **Entrega**, el documento de landed cost (cabecera) puede procesarse usando el botón de proceso "**Proceso**".

Esta acción crea un ajuste de landed cost vinculado al documento de landed cost.

Este ajuste de coste tiene tantas líneas de ajuste como productos incluidos en el/los albarán(es) seleccionado(s); por tanto, el coste de esos productos se ajusta según corresponda.

Una vez procesado, un documento de landed cost puede:

- **"Reactivarse"**; esta acción anula el ajuste de landed cost vinculado al documento de landed cost.
- o **"Contabilizarse"**, por lo que la contabilidad de **Inmovilizado del producto** también se ajusta en consecuencia.

La contabilización de **Landed Cost** crea los siguientes asientos contables en el caso de un tipo de landed cost de "Producto":

|                 |                                                                                                                                                           |                                |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| Cuenta         | Debe                                                                                                                                                     | Haber                         |
| Inmovilizado del producto   | Importe de Landed Cost "estimado".<br><br>(\*)Este apunte contable toma la **Dimensión de contabilidad** del albarán, como "Proveedor" o "Producto". Consulte el enlace "Detalle". |                                |
| Gastos del producto |                                                                                                                                                           | Importe de Landed Cost "estimado" |

La contabilización de **Landed Cost** crea los siguientes asientos contables en el caso de un tipo de landed cost de "Cuenta":

|                   |                                                                                                                                                           |                                |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| Cuenta           | Debe                                                                                                                                                     | Haber                         |
| [*Inmovilizado del producto*] | Importe de Landed Cost "estimado".<br><br>(\*)Este apunte contable toma la **Dimensión de contabilidad** del albarán, como "Proveedor" o "Producto". Consulte el enlace "Detalle". |                                |
| [*Concepto contable*]      |                                                                                                                                                           | Importe de Landed Cost "estimado" |

##### Procesar Asociación

La asociación entre un landed cost "estimado" y un landed cost "facturado" puede procesarse en:

**1.** La ventana **ALBARÁN (PROVEEDOR)** antes de procesar y usando el botón de proceso "**Completada**"

Este escenario tiene lugar siempre que toda la información relacionada con landed cost indicada a continuación esté disponible e introducida en la solapa Landed Cost del **Albarán (Proveedor)**:

- tipos de landed cost
- importes de landed cost
- líneas de factura de landed cost relacionadas

Este escenario crea automáticamente:

- un documento de landed cost en la ventana **Landed Cost** relacionado con el albarán, que contiene toda la información introducida en la solapa "Landed Cost" del **Albarán (Proveedor)**.  
  Este documento de landed cost ya está procesado y asociado; por tanto, las únicas acciones pendientes son contabilizar el documento de landed cost (cabecera) y contabilizar la asociación de landed cost.
- un ajuste de landed cost que ajusta el coste de cada producto incluido en el **Albarán (Proveedor)**.

**2**. La ventana **Landed Cost FACTURA (PROVEEDOR)**, usando el botón de proceso Match LC Cost que se puede encontrar en cada línea de factura de compra de landed cost. Después de eso, se selecciona la casilla de verificación **"Procesar Asociación"**.

Este escenario tiene lugar siempre que:

- se introdujeron todos los datos relacionados con landed cost excepto la información de la línea de factura de landed cost en la solapa Landed Cost de la ventana **Albarán (Proveedor)**.
- se introdujeron todos los datos relacionados con landed cost excepto la información de la línea de factura de landed cost en la solapa **Costo** de la ventana **Landed Cost**.

Este escenario crea automáticamente:

- un nuevo ajuste de landed cost que ajusta una vez más el coste de cada producto incluido en el **Albarán (Proveedor)** si:
  - el importe del tipo de landed cost registrado no es el mismo que el facturado
  - y la casilla de verificación "Ajustar Asociación" está seleccionada.
- la única acción pendiente es contabilizar la asociación de landed cost.

**3.** La ventana **LANDED COST**, usando el botón de proceso "**Procesar Asociación**"

Este escenario tiene lugar cuando la asociación se ha ejecutado en la factura de compra de landed cost (consulte el escenario 2 anterior), pero allí no se seleccionó la casilla de verificación "Procesar Asociación".

Este escenario crea automáticamente:

- un nuevo ajuste de landed cost que ajusta una vez más el coste de cada producto incluido en el **Albarán (Proveedor)** si el importe del tipo de landed cost registrado no es el mismo que el facturado y la casilla de verificación "Ajustar Asociación" está seleccionada.
- la única acción pendiente es contabilizar la asociación de landed cost.

**4.** La ventana **LANDED COST**, usando el botón de proceso "**Proceso**".

Este escenario tiene lugar cuando toda la información relacionada con landed cost se introduce en la ventana **Landed Cost**:

- tipos de landed cost
- importes de landed cost
- líneas de factura de landed cost relacionadas
- y albarán(es)

Este escenario crea automáticamente:

- un ajuste de landed cost que ajusta el coste de cada producto incluido en el/los **Albarán (Proveedor)**.
- las únicas acciones pendientes son contabilizar el documento de landed cost (cabecera) y contabilizar la asociación de landed cost.

##### Contabilizar Asociación

Una asociación de landed cost puede contabilizarse después de ser procesada. Esta contabilización tendrá diferentes asientos contables dependiendo de los escenarios listados a continuación:

1\. Landed cost "**estimado**" **igual** a landed cost "**facturado**"

- En el caso de un tipo de landed cost de "producto"

|                     |                                           |                                                                                                                                                                        |
| ------------------- | ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cuenta             | Debe                                     | Haber                                                                                                                                                                 |
| [*Gastos del producto*] | Importe de Landed Cost "estimado"="facturado" |                                                                                                                                                                        |
| [*Gastos del producto*] |                                           | Importe de Landed Cost "estimado"="facturado"<br><br>(\*)Este apunte contable toma la **Dimensión de contabilidad** de la factura de landed cost, como "Terceros". Consulte el enlace "Detalle". |

- En el caso de un tipo de landed cost de "cuenta"

|              |                                           |                                                                                                                                                                        |
| ------------ | ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cuenta      | Debe                                     | Haber                                                                                                                                                                 |
| [*Concepto contable*] | Importe de Landed Cost "estimado"="facturado" |                                                                                                                                                                        |
| [*Concepto contable*] |                                           | Importe de Landed Cost "estimado"="facturado"<br><br>(\*)Este apunte contable toma la **Dimensión de contabilidad** de la factura de landed cost, como "Terceros". Consulte el enlace "Detalle". |

El propósito de los asientos anteriores es que la contabilidad del gasto de landed cost tome las "dimensiones de contabilidad" de la factura de landed cost.

2\. Landed cost "**estimado**" distinto de landed cost "**facturado**" y **"Ajustar Asociación" = No**.

Esta última configuración ("Ajustar Asociación" = No) conlleva NO crear un ajuste de landed cost que lleve la diferencia al coste del producto (contabilidad del producto); por tanto, esa diferencia permanece bien en el haber (estimado>facturado) o bien en el debe (estimado<facturado) de la cuenta de gastos del producto.

- En el caso de un tipo de landed cost de "producto"

|                     |                               |                                                                                                                                                            |
| ------------------- | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cuenta             | Debe                         | Haber                                                                                                                                                     |
| [*Gastos del producto*] | Importe de Landed Cost "facturado" |                                                                                                                                                            |
| [*Gastos del producto*] |                               | Importe de Landed Cost "facturado"<br><br>(\*)Este apunte contable toma la **Dimensión de contabilidad** de la factura de landed cost, como "Terceros". Consulte el enlace "Detalle". |

- En el caso de un tipo de landed cost de "cuenta"

|              |                               |                                                                                                                                                            |
| ------------ | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cuenta      | Debe                         | Haber                                                                                                                                                     |
| [*Concepto contable*] | Importe de Landed Cost "facturado" |                                                                                                                                                            |
| [*Concepto contable*] |                               | Importe de Landed Cost "facturado"<br><br>(\*)Este apunte contable toma la **Dimensión de contabilidad** de la factura de landed cost, como "Terceros". Consulte el enlace "Detalle". |

3\. Landed cost "**estimado**" **mayor** que landed cost "**facturado**". **"Ajustar Asociación" = Sí**

Esta última configuración ("Ajustar Asociación" = Sí) conlleva crear un ajuste de landed cost que lleva la diferencia al coste del producto (haber de la contabilidad del producto).

- En el caso de un tipo de landed cost de "producto"

|                     |                                |                                                                                                                                                            |
| ------------------- | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cuenta             | Debe                          | Haber                                                                                                                                                     |
| [*Gastos del producto*] | Importe de Landed Cost "estimado" |                                                                                                                                                            |
| [*Gastos del producto*] |                                | Importe de Landed Cost "facturado"<br><br>(\*)Este apunte contable toma la **Dimensión de contabilidad** de la factura de landed cost, como "Terceros". Consulte el enlace "Detalle". |
| [*Inmovilizado del producto*]   |                                | Importe de Landed Cost de la diferencia (estimado>facturado)                                                                                                         |

- En el caso de un tipo de landed cost de "cuenta"

|                   |                                |                                                                                                                                                            |
| ----------------- | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cuenta           | Debe                          | Haber                                                                                                                                                     |
| [*Concepto contable*]      | Importe de Landed Cost "estimado" |                                                                                                                                                            |
| [*Concepto contable*]      |                                | Importe de Landed Cost "facturado"<br><br>(\*)Este apunte contable toma la **Dimensión de contabilidad** de la factura de landed cost, como "Terceros". Consulte el enlace "Detalle". |
| [*Inmovilizado del producto*] |                                | Importe de Landed Cost de la diferencia (estimado>facturado)                                                                                                         |

4\. Landed cost "**estimado**" **menor** que landed cost "**facturado**". **"Ajustar Asociación" = Sí**

Esta última configuración ("Ajustar Asociación" = Sí) conlleva crear un ajuste de landed cost que lleva la diferencia al coste del producto (debe de la contabilidad del producto).

- En el caso de un tipo de landed cost de "producto"

|                     |                                                    |                                                                                                                                                            |
| ------------------- | -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cuenta             | Debe                                              | Haber                                                                                                                                                     |
| [*Inmovilizado del producto*]   | Importe de Landed Cost de la diferencia (estimado<facturado) |                                                                                                                                                            |
| [*Gastos del producto*] | Importe de Landed Cost de la diferencia (estimado<facturado) |                                                                                                                                                            |
| [*Gastos del producto*] |                                                    | Importe de Landed Cost "facturado"<br><br>(\*)Este apunte contable toma la **Dimensión de contabilidad** de la factura de landed cost, como "Terceros". Consulte el enlace "Detalle". |

- En el caso de un tipo de landed cost de "cuenta".

|                   |                                                    |                                                                                                                                                            |
| ----------------- | -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cuenta           | Debe                                              | Haber                                                                                                                                                     |
| [*Inmovilizado del producto*] | Importe de Landed Cost de la diferencia (estimado<facturado) |                                                                                                                                                            |
| [*Concepto contable*]      | Importe de Landed Cost de la diferencia (estimado<facturado) |                                                                                                                                                            |
| [*Concepto contable*]      |                                                    | Importe de Landed Cost "facturado"<br><br>(\*)Este apunte contable toma la **Dimensión de contabilidad** de la factura de landed cost, como "Terceros". Consulte el enlace "Detalle". |

##### Cancelar Asociación

Una asociación de landed cost puede cancelarse usando el botón de proceso de cabecera "**Cancelar Asociación**". Antes de eso, la asociación de landed cost debe estar "Descontabilizada".

La acción de cancelar la asociación implica que:

- Los importes asociados actuales no se eliminan de la solapa **Importe Asociado**.
- Debe ejecutarse una nueva asociación en la(s) factura(s) de compra de landed cost correspondiente(s).
- Los importes de asociación correctos se actualizarán entonces en la solapa **Importe Asociado**.
#### Importe Asociado

La solapa **Importe Asociado** es una solapa de solo lectura que permite revisar las líneas de **Factura (Proveedor)** conciliadas con las líneas de **Landed Cost**.

#### Contabilidad Coste

Esta solapa proporciona información contable del documento **Landed Cost**.

Como cualquier otra solapa de contabilidad, esta solapa muestra los asientos del libro mayor de la contabilización de **Landed Cost**.
#### Entrega

La solapa **Entrega** permite al usuario seleccionar el/los albarán/es o la/s línea/s de albarán a los que se van a asignar los tipos de landed cost registrados.

Una vez que la cabecera de **Landed Cost** se ha cumplimentado correctamente y se ha guardado, se puede registrar una línea de albarán en esta solapa.

Los importes de landed cost introducidos en la solapa "Costo" pueden asignarse/distribuirse entre el/los albarán/es introducidos aquí.

Algunos campos relevantes a tener en cuenta son:

- **Albarán (Proveedor)**: sirve para seleccionar un albarán; por tanto, los importes de landed cost se distribuirán entre todas las líneas del albarán.
- **Línea de albarán**: sirve para seleccionar una línea de albarán específica.

Tenga en cuenta que, en un registro, es necesario seleccionar un albarán o una línea de albarán.
#### Importe de la Línea de Albarán

**Importe de la Línea de Albarán** es una solapa de solo lectura que muestra información detallada sobre la línea de **Tipo de Landed Cost** asignada a cada línea de albarán, así como el importe de **Landed Cost** distribuido a cada línea de albarán.

Es importante remarcar que el **Importe** distribuido se calcula teniendo en cuenta la precisión de **Costo** definida para la **Moneda**.
#### Contabilidad

Esta solapa proporciona información contable de **Landed Cost Matching**.

### Contabilización masiva

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

La funcionalidad de **Contabilización masiva** permite al usuario contabilizar o descontabilizar múltiples registros seleccionando los registros correspondientes y haciendo clic en el botón **Contabilización masiva**. En este caso, esta funcionalidad puede utilizarse en la ventana **Landed Cost** y en la solapa **Costo**.

Además, el Estado de contabilidad del/de los registro/s se muestra en la barra de estado, en la vista de formulario, o en una columna, en la vista de cuadrícula.

!!! info
    Para más información, visite [la guía de usuario del módulo Bulk Posting](../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).

---

Este trabajo es una obra derivada de [Gestión de Compras](http://wiki.openbravo.com/wiki/Procurement_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.

---
Esta obra está licenciada bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L.](https://etendo.software){target="_blank"}.