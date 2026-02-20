---
title: Gestión de MRP 
tags:
    - Gestión de MRP
    - Planificación de la producción
    - Planificación de compras
    - Previsión de ventas
    - Transacciones
---
## Visión general

La Gestión de MRP (MRP) se ocupa de todas las actividades relacionadas con la planificación de una fabricación y las sugerencias para el suministro requerido.

## Planificación de la producción

:material-menu: `Aplicación` > `Gestión de MRP` > `Transacciones` > `Planificación de la producción`

### Visión general

Cree una orden de fabricación integral para solicitar materiales durante un periodo de tiempo especificado.

La Planificación de la producción sugiere órdenes de fabricación y necesidades de material que deben crearse y, con solo hacer clic en un botón, estos documentos se crean automáticamente.

En la sección principal del documento se introduce la información de lo que debe planificarse y para qué periodo de tiempo. El botón **Procesar Planificación de la producción** crea las líneas del plan con información de oferta y demanda:

-   nivel de stock actual (oferta)
-   órdenes de fabricación pendientes (oferta)
-   pedidos de venta contabilizados sin un albarán de salida de mercancías (demanda)
-   stock de seguridad (demanda)
-   previsión de ventas (demanda)

La información que se lista depende del método de planificación utilizado para el producto.

El proceso de MRP equilibra la demanda con la oferta, teniendo en cuenta las fechas de ambas y, en base a esta información, sugiere órdenes de fabricación y necesidades de material a crear. Las líneas generadas pueden actualizarse manualmente. Además, pueden realizarse cambios en la demanda y la oferta y recalcular el plan para ver un nuevo plan.

La Planificación de la producción muestra la demanda de materia prima requerida para las órdenes de fabricación sugeridas, y sugiere necesidades de material sin revisar la oferta y la demanda de la materia prima. Una vez que el planificador completa las necesidades de material, se introducen en la Planificación de compras para calcular si es necesario emitir pedidos de compra.

Una vez que el plan es el deseado, al hacer clic en diferentes botones se crean automáticamente las órdenes de fabricación y las necesidades de material.

### Cabecera

Cree y edite un plan de fabricación.

![](../../../../assets/drive/v9Sv8GL701vVFES6XW-SbEO5ljGyfu6j-Tl7IfLaMNWcbU0TuaVJkkDYd3yr1-CwUJoLt-5rCn58GJKJ2iuUsGwVqbxM5KxM2o0ovovjTbtMqXfuuWFKhs6xImMsFRJ89br7qa22FTV-Y_i6obYI7lA.png)

-   Fecha del documento: fecha en la que se introduce el plan de fabricación
-   Nombre: nombre del plan de fabricación
-   Horizonte temporal: número de días que se tienen en cuenta para el cálculo del plan de fabricación
-   Plazo de seguridad: número de días que se añaden al desfase para el cálculo de la fecha de pedido planificada de las órdenes de fabricación y necesidades de material sugeridas. Por ejemplo, el plazo de fabricación se utiliza para indicar cuánto tiempo tardará un producto desde que se produce hasta que llega al almacén, y el plazo de seguridad se añade por el tiempo necesario para poner el producto en stock (debido a controles de calidad u otros procesos internos).
-   Planificador: filtro para seleccionar solo productos gestionados por un determinado planificador, según se configura en la pestaña [Producto](../../../../user-guide/etendo-classic/basic-features/master-data-management/master-data.md#product) en la sección de Gestión de datos maestros.
-   Tercero: filtro para seleccionar solo productos pedidos por un determinado cliente
-   Categoría de tercero: filtro para seleccionar solo terceros de una determinada categoría de tercero.
-   Producto: filtro para seleccionar solo un determinado producto
-   Categoría de producto: filtro para seleccionar solo productos relacionados con una determinada categoría de producto

!!! info
    Una vez añadida la información en la sección principal, pueden crearse las líneas. Si es necesario, se realizan cambios en las configuraciones haciendo clic en el botón **Recalcular fechas/cantidades**.

### Líneas

Añada productos que se incluirán en su plan. Cada producto se muestra en su propia línea.

!!! info
    Solo los productos que están configurados con la casilla **Producción** y con **Plan de proceso** seleccionado en el producto son ejecutados por el proceso de MRP.

Dependiendo del producto, pueden aparecer diferentes tipos de transacción en las líneas. Todas las transacciones de oferta tienen una cantidad positiva; todas las transacciones de demanda tienen una cantidad negativa.

-   Stock: aparece por defecto para el producto
-   Previsión de ventas: la información aparece si:
    -   la previsión está configurada en la pantalla de previsión de ventas
    -   la previsión está definida en el método de planificación
    -   el método de planificación está vinculado al producto
-   Stock mínimo: aparece por defecto para el producto si está configurado en el campo **Stock de seguridad** del producto.
-   Pedido de venta pendiente: la información aparece si:
    -   el pedido de venta pendiente está definido en el método de planificación
    -   el método de planificación está vinculado al producto
    -   existen pedidos de venta contabilizados sin un albarán de salida de mercancías relacionado para el producto
-   Orden de fabricación sugerida: recomendación generada por MRP para crear un pedido de compra.
    -   la cantidad requerida es la cantidad resultante del balance de toda la oferta y toda la demanda
    -   la Cantidad es la cantidad que aparecerá en la(s) orden(es) de fabricación que se cree(n). En función de las configuraciones del producto, la cantidad puede diferir de la cantidad requerida, por ejemplo, debido a la cantidad mínima para producción, tipo de cantidad, etc.
    -   la Fecha de pedido planificada es la fecha en la que debe crearse y procesarse la Orden de Fabricación. Es un desfase de las fechas en las que se requiere la demanda con el plazo de fabricación configurado en el producto y el plazo de seguridad configurado en la sección principal de este plan. Si la demanda se requiere dentro del marco temporal de los plazos, la fecha se refleja como vencida para indicar que, para obtener el producto a tiempo, ya debería haberse tomado una acción, e indica exactamente cuánto se ha retrasado la acción.
-   Necesidad de material sugerida: recomendación generada por MRP para crear necesidades de material para la materia prima que se requiere utilizar en las órdenes de fabricación sugeridas. La información correcta de materia prima se genera si la información del **Plan de proceso** es correcta.
    -   la Fecha de pedido planificada es la fecha en la que la Necesidad de material debe crearse y completarse. Estas fechas son iguales a las fechas de pedido planificadas de las órdenes de fabricación sugeridas.
    -   la Cantidad aparece en la necesidad de material que se crea. La cantidad se basa en la que figura en la orden de fabricación sugerida combinada con el uso del componente según se define en el **Plan de proceso**.

![](../../../../assets/drive/CybK3PMQnVZL8ddGSu6_bdNgiobsrqsoAozZxR5FPMmOdjckNdwlealsSm6vcAuBS3IaeDbIcClhX5-Ij3iD9PWJXOrdj7od_ZCbX3E7TusOUjlwnE063XfjJyu4rtb3czv-XBFhu1uRLomlQFYxNlo.png)

!!! info
    Al hacer clic en el botón **Generar órdenes de fabricación**, las órdenes de fabricación se crean automáticamente. Los documentos deben procesarse; consulte la sección [Orden de Fabricación](../../../../user-guide/etendo-classic/basic-features/production-management/transactions.md#work-requirement) en la sección de Gestión de producción para más detalles.

!!! info
    Al hacer clic en el botón **Generar necesidades de material**, las necesidades de material se crean automáticamente en borrador. Los documentos deben completarse; consulte la sección [Necesidad de material](../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#requisition) en la sección de Gestión de aprovisionamiento para más detalles.

Las necesidades de material pueden seleccionarse como entrada en el método de planificación de la Planificación de compras para incluirse en los cálculos de ese plan, con el fin de calcular si es necesario crear pedidos de compra.

Una vez que los documentos se crean automáticamente, los números de los documentos aparecen en las columnas **Orden de Fabricación** y **Línea de necesidad de material** de las líneas. El pedido de compra creado está en estado borrador y debe contabilizarse.

!!! info
    Para más información, consulte la sección [_Pedido de compra_](../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#purchase-order).

## Planificación de compras

:material-menu: `Aplicación` > `Gestión de MRP` > `Transacciones` > `Planificación de compras`

### Visión general 

Cree un plan completo y organizado para solicitar compras durante un periodo de tiempo especificado.

La Planificación de compras sugiere pedidos de compra que deben crearse y, con solo hacer clic en un botón, estas compras se crean automáticamente.

En la sección principal del documento se introduce la información de lo que debe planificarse y para qué periodo de tiempo. El botón **Procesar Planificación de compras** crea las líneas del plan con información de oferta y demanda.

-   nivel de stock actual (oferta)
-   pedidos de compra contabilizados sin una entrada de mercancías (oferta)
-   pedidos de venta contabilizados sin un albarán de salida de mercancías (demanda)
-   necesidades de material completadas (demanda)
-   stock de seguridad (demanda)
-   previsión de ventas (demanda)

La información que se lista depende del método de planificación utilizado para el producto.

El proceso de MRP equilibra la demanda con la oferta, teniendo en cuenta las fechas de ambas y, en base a esta información, sugiere pedidos de compra a crear. Las líneas generadas pueden actualizarse manualmente. Además, pueden realizarse cambios en la demanda y la oferta, eliminarse las líneas actuales y reprocesarse el plan para ver una nueva situación.

Una vez que el plan es el deseado, al hacer clic en un botón se crean automáticamente los pedidos de compra.

### Cabecera

Cree y edite un plan de compras.

![](../../../../assets/drive/fy3zYkHMfzPgZxxa622JLdEWaPYWTr4ne_HXdC1DuijCQ7S9EbM7rQteyyZ8m7b_J0XJdflUydjIUtGMZsR6eUGmWTWqx1jnSE0POhkjyczK5QqR6KaL7cgZ3TQfCzqENhDOZb-8MOt_VsGJYePimz4.png)

-   Fecha del documento: fecha en la que se introduce el plan de compras
-   Nombre: nombre del plan de compras
-   Horizonte temporal: número de días que se tienen en cuenta para el cálculo del plan de compras
-   Plazo de seguridad: número de días que se añaden al desfase para el cálculo de la fecha de pedido planificada del pedido de compra sugerido. Por ejemplo, el plazo de compra se utiliza para indicar cuánto tiempo tardará un producto desde que se pide hasta que llega al almacén, y el plazo de seguridad se añade por el tiempo necesario para poner el producto en stock (debido a controles de calidad u otros procesos internos).
-   Planificador: filtro para seleccionar solo productos gestionados por un determinado planificador, según se configura en la pestaña [Producto](../../../../user-guide/etendo-classic/basic-features/master-data-management/master-data.md#product) en la sección de Gestión de datos maestros.
-   Proveedor: filtro para seleccionar solo productos de un determinado proveedor según se configura en la pestaña **Compras** del producto.
-   Producto: filtro para seleccionar solo un determinado producto
-   Categoría de producto: filtro para seleccionar solo productos relacionados con una determinada categoría de producto
-   Tercero: filtro para seleccionar solo productos pedidos por un determinado cliente
-   Categoría de tercero: filtro para seleccionar solo terceros de una determinada categoría de tercero.
-   Botón Procesar Planificación de compras: una vez añadida la información en la sección principal, las líneas se crean mediante el botón **Procesar Planificación de compras**. Si es necesario, se eliminan las líneas, se realizan cambios en las configuraciones y se crean nuevas líneas haciendo clic de nuevo en el botón **Procesar Planificación de compras**.
-   Crear pedido de compra: genera los pedidos de compra correspondientes
-   Crear reservas: este botón solo es visible cuando la funcionalidad de reservas de stock está habilitada. Reserva stock para los pedidos de venta que no están reservados, si hay stock, y para los que no pueden reservarse porque no hay stock crea los pedidos de compra correspondientes y los vincula al pedido de venta

### Líneas

Añada productos que se incluirán en su plan. Cada producto se muestra en su propia línea.

!!! info
    Solo los productos que están configurados con la casilla **Compra** seleccionada en el producto son ejecutados por el proceso de MRP.

Dependiendo del producto, pueden aparecer diferentes tipos de transacción en las líneas. Todas las transacciones de oferta tienen una cantidad positiva; todas las transacciones de demanda tienen una cantidad negativa.

-   Stock: aparece por defecto para el producto
-   Previsión de ventas: la información aparece si:
    -   la previsión está configurada en la pantalla de previsión de ventas
    -   la previsión está definida en el método de planificación
    -   el método de planificación está vinculado al producto
-   Stock mínimo: aparece por defecto para el producto si está configurado en el campo **Stock de seguridad** del producto. 
-   Pedido de compra pendiente: la información aparece si:
    -   el pedido de compra pendiente está definido en el método de planificación
    -   el método de planificación está vinculado al producto
    -   existen pedidos de compra contabilizados sin una entrada de mercancías relacionada para el producto
-   Pedido de venta pendiente: la información aparece si:
    -   el pedido de venta pendiente está definido en el método de planificación
    -   el método de planificación está vinculado al producto
    -   existen pedidos de venta contabilizados sin un albarán de salida de mercancías relacionado para el producto
-   Pedido de compra sugerido: recomendación generada por MRP para crear un pedido de compra.
    -   la cantidad requerida es la cantidad resultante del balance de toda la oferta y toda la demanda
    -   la Cantidad es la cantidad que aparecerá en el/los pedido(s) de compra que se cree(n). En función de las configuraciones del Producto, la cantidad puede diferir de la cantidad requerida, por ejemplo, debido a la cantidad mínima de pedido, tipo de cantidad, etc.
    -   la Fecha de pedido planificada es la fecha en la que el Pedido de compra debe contabilizarse. Es un desfase de las fechas en las que se requiere la demanda con el plazo de compra configurado en el producto y el plazo de seguridad configurado en la sección principal de este plan. Si la demanda se requiere dentro del marco temporal de los plazos, la fecha se refleja como vencida para indicar que, para obtener el producto a tiempo, ya debería haberse tomado una acción, e indica exactamente cuánto se ha retrasado la acción.

![](../../../../assets/drive/w4GSGwyp0V_SmTDWGcL2hTngg6mG4-w6bnc1O7_5-gBRsMFQ4zI2xrh_b1gFyd8FhFeSniYQ4FCm32-BFR5Xd3NYJCtxuRAevOCHkd6aMn5FI7MPlBxT0ktDYMNPq0zIdqL3UkIBsk6Dq84nFjyGtMY.png)

Al hacer clic en el botón **Crear pedidos de compra**, se crea el pedido de compra, siempre que todas las configuraciones se hayan introducido correctamente:

-   la información del proveedor está completa
-   el producto está configurado con la información requerida en la pestaña de compras
-   el precio para el proveedor está introducido en el producto

Una vez que el pedido de compra se crea automáticamente, el número del documento aparece en la columna **Línea de pedido** de la línea. El pedido de compra creado está en estado borrador y debe contabilizarse.

!!! info
    Para más información, consulte la sección [Pedido de compra](../procurement-management/transactions.md#purchase-order).

## Previsión de ventas

:material-menu: `Aplicación` > `Gestión de MRP` > `Transacciones` > `Previsión de ventas`

### Visión general

Cree y edite previsiones de MRP durante un periodo de tiempo especificado para ayudar a planificar las compras necesarias.

Se introduce una previsión de demanda para un determinado cliente para que pueda incluirse en el método de planificación y, por tanto, en los cálculos de la Planificación de la producción y la Planificación de compras. Una previsión se basa en expectativas de demanda futura, no en datos existentes. Por lo tanto, una vez que la información real se introduce en la aplicación en un pedido de venta, la previsión debe eliminarse para evitar duplicidades.

### Cabecera

Cree una previsión de MRP.

![](../../../../assets/drive/lA5q7zm1pYwF2yzFNLc_yIf7a4FNScC0giQ2MKnA5kEMz_eg6XXkvgCyDSu05jBo0N-CoH7-9VfTLaJ-wI0KmDSWLGtrcwPMw2nQMrIcbOrbBzI7A9SzYeiKD2Ep7ZSgYLPWEK_klyPNFH4d6VRu38A.png)

-   Fecha del documento: fecha en la que se introduce la previsión.
-   Tercero: el cliente para el que se espera la demanda. Esto aplica a la previsión tanto en la Planificación de la producción como en la Planificación de compras.

### Líneas

Añada productos que se incluirán en su previsión de MRP. Cada producto se añade creando una línea.

![](../../../../assets/drive/UC2IX8-3_QdWSgE-8FTMibabemse30bN2A1p1pzXreGFH8s-N4Irs8Qe6MB139B0XUSub0p2QJZu5nnE30aDgagISEpbk1ygomDybVXyYUYwSAujXvUvt4wQ1LLM4YLUZtFJvFfRjfVgYQZpWNhG2zA.png)

-   Fecha planificada: fecha que se tiene en cuenta para la demanda en la Planificación de la producción y la Planificación de compras como **Fecha de pedido planificada**.
-   Producto: el producto que se planifica en una Planificación de la producción o Planificación de compras.
-   Cantidad: la cantidad del producto que se requiere para la fecha planificada.

---

- Este trabajo es una obra derivada de [Planificación de necesidades de material](https://wiki.openbravo.com/wiki/Material_Requirement_Planning){target="_blank"} de [Openbravo S.L.U](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, con licencia [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}.