---
title: Transacciones de Proyectos y Servicios
tags: 
 - Proyecto multifase
 - Informe de gasto
 - Crear pedidos de venta según gastos
 - Crear facturas de gastos AP

---
# Transacciones de Proyectos y Servicios

## Visión general

Esta sección describe las diferentes ventanas que se utilizan para las transacciones incluidas en el proceso de Gestión de Proyectos y Servicios en Etendo. Estas son:

[:material-file-document-outline: Proyecto multifase](#proyecto-multifase){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Informe de gasto](#informe-de-gasto){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Crear pedidos de venta según gastos](#crear-pedidos-de-venta-según-gastos){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Crear facturas de gastos AP](#crear-facturas-de-gastos-ap){ .md-button .md-button--primary } <br>

## Proyecto multifase 

:material-menu: `Aplicación` > `Gestión de Proyectos y Servicios` > `Transacciones` > `Proyecto multifase`

### Visión general

Esta ventana se utiliza para gestionar un proyecto, sus fases y tareas relacionadas, y para completar las facturas de venta relacionadas. Para los proyectos se monitorizan los siguientes aspectos:

- La visión general de costes: en base a la visión general de costes planificados introducida en el proyecto multifase, una vez que se crean documentos que referencian el proyecto, el coste real puede compararse con ellos.
- La planificación: en base a las fechas de inicio y fin planificadas, se puede monitorizar el progreso del proyecto.

!!! important
    Desde la ventana de proyecto multifase, se generan pedidos de venta en estado borrador al final de cada fase completada. Esto se realiza con el botón [**Generar pedido de venta de la fase**](../project-and-service-management/transactions.md#process-button) a nivel de la solapa Fase del proyecto.

### Cabecera

![](../../../../assets/user-guide/etendo-classic/basic-features/project-and-services-management/transactions/multiphase-project.png)

Aquí, los campos a tener en cuenta son:

- Organización: organización del proyecto.
- Clave de búsqueda: campo utilizado para filtrar registros fácilmente.
- Nombre: nombre del proyecto. El nombre debe ser único entre Proyectos de servicio y proyectos multifase.
- Fase actual: campo para realizar un seguimiento manual de la fase actual del proyecto.
- Fecha de inicio: fecha de inicio del proyecto.
- Fecha de fin planificada: fecha de fin programada del proyecto.
- Fecha de fin real: fecha de fin real del proyecto.
- Descripción: campo de notas.
- Representante de ventas: contacto comercial relacionado con este proyecto.
- Responsable: gestor del proyecto.

En la sección Importes:

- Contrato legalmente vinculante: si está marcado, indica si el documento es legalmente vinculante.
- Límite de precio: solo se muestra si Contrato legalmente vinculante está marcado. El importe y la cantidad comprometidos son el importe y la cantidad máximos a cobrar. Se ignora si el importe o la cantidad es cero.
- Importe del contrato: solo se muestra si Contrato legalmente vinculante está marcado. El importe comprometido es independiente del importe planificado. Usted utilizaría el importe planificado para su estimación realista, que puede ser mayor o menor que el importe comprometido.
- Cantidad del contrato: solo se muestra si Contrato legalmente vinculante está marcado. El importe comprometido es independiente del importe planificado. Usted utilizaría el importe planificado para su estimación realista, que puede ser mayor o menor que el importe comprometido.
- Ingresos por servicios: ingresos esperados por servicios (consultoría).
- Gastos planificados: gastos esperados.
- Coste de servicios prestados: coste interno esperado de los servicios (mano de obra x horas x coste).
- Coste subcontratado: coste esperado de servicios ejecutados por terceros.
- Coste total del servicio: información completada de Coste de servicios prestados + Coste subcontratado.
- Gastos refacturados: por defecto toma los gastos planificados, pero puede sobrescribirse por el importe real que se facturará al tercero.
- % margen de servicio planificado: información completada con el porcentaje de beneficio o pérdida en los servicios: (Ingresos por servicios - Coste de servicios prestados - Coste subcontratado) x 100/Ingresos por servicios.
- % margen de gastos planificado: información completada con el porcentaje de beneficio o pérdida en los gastos: (Gastos refacturados - Gastos planificados) x 100/Gastos refacturados.

En la sección Más información:

- Tercero: el cliente al que se le cobra el proyecto.
- Dirección del tercero: dirección del tercero.
- Usuario/Contacto: usuario que trabaja para el tercero.
- Referencia del pedido: número de referencia del tercero que aparecerá en el pedido de venta.
- Método de pago: método de pago del tercero que aparecerá en el pedido de venta.
- Condiciones de pago: condiciones de pago del tercero que aparecerán en el pedido de venta.
- Tarifa: tarifa relacionada con el tercero.
- Moneda: moneda relacionada con el tercero.
- Almacén: almacén utilizado para enviar al tercero.

#### Botones de proceso

- Establecer el tipo de proyecto: para seleccionar un tipo de proyecto con el fin de copiar las fases y tareas de ese tipo de proyecto al proyecto multifase. En base a las duraciones de las fases y tareas en el tipo de proyecto, se sobrescriben la fecha de inicio y la fecha de fin en el proyecto multifase.
- Cambiar estado del proyecto: para cambiar el estado del proyecto. Los estados del proyecto multifase son:
    - Abierto: estado inicial, comparable con el estado Borrador en otros documentos.
    - Pedido: estado para indicar que se pueden generar los pedidos de venta.
    - Pedido cerrado: estado final del proyecto. Al cambiar a este estado, el campo Fecha de fin real se completa automáticamente con la fecha del sistema. Una vez que el estado del proyecto es Pedido cerrado, el proyecto no se puede volver a abrir.
    !!!info
        Para utilizar este botón, deben completarse los campos Tercero y Representante de ventas de la cabecera.
- Copiar detalles: se copia la información de fase(s) del proyecto y tarea(s) del proyecto desde otro proyecto multifase.

### Solapa Fase del proyecto

En esta solapa se pueden definir las fases individuales del proyecto.

![](../../../../assets/user-guide/etendo-classic/basic-features/project-and-services-management/transactions/project-phase.png)

En esta solapa se muestran los siguientes campos:

- Organización: organización de la fase
- Número de secuencia: numeración de las líneas introducidas. Por defecto 10,20,30,..etc.
- Nombre: nombre de la fase.
- Producto: producto o servicio que se vende en la fase.
- Cantidad: cantidad del producto a vender en la fase.

    !!!note
        Los campos anteriores se copian del [Tipo de proyecto](../project-and-service-management/setup.md#project-type) si se utiliza la funcionalidad [Establecer el tipo de proyecto](#botones-de-proceso).

- Precio unitario neto: cuando se completa, este es el nuevo precio unitario que aparecerá para la fase en el pedido de venta, sobrescribiendo así el precio unitario neto de la tarifa.
- Fecha de inicio: fecha de inicio planificada de la fase.
- Fecha de fin planificada: fecha de fin planificada de la fase.

    !!!note 
        La Fecha de inicio y la Fecha de fin planificada de la fase se calculan en base a la fecha de inicio y la Duración estándar en días definida en el [Tipo de proyecto](../project-and-service-management/setup.md#project-type) si se utiliza la funcionalidad [Establecer el tipo de proyecto](#botones-de-proceso).

- Fecha de fin: fecha de fin real a completar manualmente. Esta fecha no se completa al seleccionar y guardar la casilla de verificación Fase completada.
- Casilla de verificación Fase completada: para establecer la fase como completada. Para establecer la fase como Fase completada, no es obligatorio que la(s) tarea(s) relacionada(s) con esta fase se establezcan como completadas primero. Sin embargo, una vez marcada la casilla Fase completada, las tareas de esta fase también se marcan como completadas.

En la sección Más información:

- Límite de precio: el importe y la cantidad comprometidos son el importe y la cantidad máximos a cobrar. Se ignora si el importe o la cantidad es cero.
- Importe del contrato: el importe comprometido es independiente del importe planificado. Usted utilizaría el importe planificado para su estimación realista, que puede ser mayor o menor que el importe comprometido.
- Descripción: una descripción está limitada a 255 caracteres.
- Fase estándar: fase del proyecto con información de rendimiento estándar con trabajo estándar.
- Pedido de venta: identificador único y una referencia a un Pedido de venta originado a partir de la secuencia de documentos definida para este tipo de documento.

#### Botón de proceso

- Generar pedido de venta de la fase: para crear un pedido de venta al completar una fase. A partir del pedido de venta, se crea una factura de venta para documentar que el cliente debe pagar por el trabajo ejecutado en el proyecto.

    !!!info
        El pedido de venta creado incluye todas las líneas de la fase y sus tareas relacionadas.

### Subsolapa Tarea del proyecto

En esta subsolapa se definen las tareas individuales necesarias para completar la fase del proyecto.

![](../../../../assets/user-guide/etendo-classic/basic-features/project-and-services-management/transactions/project-task.png)

En esta subsolapa se muestran los siguientes campos:

- Organización: organización de la tarea
- Número de secuencia: numeración de las líneas introducidas. Por defecto 10,20,30,..etc.
- Nombre: nombre de la tarea
- Producto: producto o servicio que se vende relacionado con esta tarea.
- Cantidad: cantidad del producto a vender para la tarea.

    !!!note
        Los campos anteriores se copian del Tipo de proyecto si se utiliza la funcionalidad Establecer el tipo de proyecto.

- Precio unitario neto: cuando se completa, este es el nuevo precio unitario que aparecerá para la tarea en el pedido de venta, sobrescribiendo así el precio unitario neto de la tarifa.
- Fecha de inicio: fecha de inicio planificada
- Fecha de fin planificada: fecha de fin planificada

    !!!note
        La Fecha de inicio y la Fecha de fin planificada de la tarea se calculan en base a la fecha de inicio y la Duración estándar en días definida en el Tipo de proyecto si se utiliza la funcionalidad Establecer el tipo de proyecto.

- Fecha de fin: fecha de fin real a completar manualmente. Esta fecha no se completa al seleccionar y guardar la casilla de verificación Tarea completada.
- Casilla de verificación Tarea completada: para establecer la tarea como completada.

En la sección Más información:

- Tarea estándar: tarea estándar del proyecto en una fase del proyecto con esfuerzo estándar
- Límite de precio: el importe y la cantidad comprometidos son el importe y la cantidad máximos a cobrar. Se ignora si el importe o la cantidad es cero.
- Importe del contrato: el importe comprometido es independiente del importe planificado. Usted utilizaría el importe planificado para su estimación realista, que puede ser mayor o menor que el importe comprometido.
- Descripción: una descripción está limitada a 255 caracteres.

## Informe de gasto

:material-menu: `Aplicación` > `Gestión de Proyectos y Servicios` > `Transacciones` > `Informe de gasto`

### Visión general

Un Informe de gasto se utiliza para registrar partes de horas y gastos de artículos.

En base a las partes de horas, se calcula el coste relacionado con los operarios asignados al proyecto y puede consultarse en el informe [Rentabilidad de Proyectos](../project-and-service-management/analysis-tools.md#project-profitability).

Para los gastos de artículos, se documenta el coste que los operarios han realizado relacionado con proyectos. En base a esto, el seguimiento para reembolsar el coste al operario se realiza con la creación de una [Factura (Proveedor)](../procurement-management/transactions.md#purchase-invoice). Para vincular las facturas correspondientes al proyecto, existe un campo de dimensión de proyecto en la cabecera de la ventana Factura (Proveedor).

Tanto para partes de horas como para gastos de artículos, se puede indicar si al cliente relacionado con el proyecto se le facturan estos costes. El seguimiento de esto es que se crea un [Pedido de venta](../sales-management/transactions.md#sales-order) para crear una [Factura (Cliente)](../sales-management/transactions.md#sales-invoice).

### Cabecera

En esta ventana, el usuario puede crear y procesar un informe de gasto.

![](../../../../assets/user-guide/etendo-classic/basic-features/project-and-services-management/transactions/expense-sheet.png)

Los campos de esta solapa son:

- Organización: organización del gasto.
- Nº de documento: número completado del informe de gasto.
- Operarios: operario que realizó el gasto relacionado con un proyecto o dedicó tiempo a un proyecto. Es importante remarcar que los operarios:
    - deben crearse como [Operarios](../master-data-management/master-data.md#employee) en la ventana Tercero,
    - deben crearse como [Usuario](../general-setup/security/user.md) de Etendo en la ventana Usuario,
    - y, finalmente, el operario y el usuario deben estar relacionados entre sí.
    Esa relación puede establecerse seleccionando el registro de tercero del operario en el registro de Usuario del operario, como se muestra en la imagen siguiente.
- Fecha del informe: fecha para la que se introduce el gasto.

 ![](../../../../assets/user-guide/etendo-classic/basic-features/project-and-services-management/transactions/user.png)

### Solapa Líneas

En esta solapa, el usuario puede añadir líneas de partes de horas y de gastos regulares al informe. Cada gasto se añade a una línea individual y puede o no facturarse a clientes.

![](../../../../assets/user-guide/etendo-classic/basic-features/project-and-services-management/transactions/expense-sheet-lines.png)

Los campos a tener en cuenta en esta solapa son:

- Casilla de verificación Parte de horas: para indicar si el gasto es de tiempo o de artículos.
- Producto: producto relacionado con la línea de gasto. Tal y como se ve en la sección [configuración](../project-and-service-management/getting-started.md#configuration), para partes de horas aparecen los productos configurados con tipo Servicio. Para gastos de artículos aparecen los productos configurados con tipo Gasto.
- Cantidad: cantidad para el producto registrado.
- UdM: unidad de medida del producto.
- Nº de línea: numeración de la línea. Por defecto 10,20,30,...etc.
- Importe del gasto: no visible en parte de horas. Campo completado con la información del importe.
- Importe convertido: no visible en parte de horas. Importe del gasto convertido a la moneda del cliente.
- Moneda: moneda del gasto introducido.
- Casilla de verificación Refacturación: casilla para indicar si al cliente (el tercero relacionado con el proyecto) se le facturará este gasto.
- Tercero: solo visible cuando se selecciona la casilla de verificación Refacturación. El tercero al que se factura el gasto. El valor se completará en base a la información del proyecto introducida.
- Precio unitario neto: precio relacionado con el producto.
- Fecha del gasto: fecha relacionada con el gasto informado.
- Proyecto: proyecto al que se relaciona el gasto.
- Fase del proyecto: fase del proyecto a la que se relaciona el gasto.
- Tarea del proyecto: tarea del proyecto a la que se relaciona el gasto.

### Botón de proceso

- Procesar/Desprocesar gastos: una vez introducida la información correspondiente del informe, puede procesar el gasto. Si el documento está procesado, es posible seleccionarlo y desprocesarlo para editarlo si es necesario.

## Crear pedidos de venta según gastos

:material-menu: `Aplicación` > `Gestión de Proyectos y Servicios` > `Transacciones` > `Crear pedidos de venta según gastos`

Este es un proceso que genera automáticamente pedidos de venta por cliente para todos los gastos pendientes de facturar. Para que el proceso cree el pedido de venta con la información correcta, el cliente debe estar configurado con la solapa [Cliente] de la ventana Tercero completada.
Este proceso está integrado con el módulo [Gestión de Ventas](../sales-management/getting-started.md):

- Todos los pedidos de venta generados pueden revisarse y modificarse a través de ese módulo.
- El proceso de facturación puede ejecutarse posteriormente.
- Existe una casilla de verificación Completar y procesar pedidos de venta automáticamente para indicar si los pedidos de venta deben crearse en estado contabilizado o no.

El proceso crea un Pedido de venta de tipo Pedido de almacén con su correspondiente Albarán si se selecciona la casilla de verificación Completar y procesar pedidos de venta automáticamente.

![](../../../../assets/user-guide/etendo-classic/basic-features/project-and-services-management/transactions/create-sales-orders-from-expenses.png)

## Crear facturas de gastos AP

:material-menu: `Aplicación` > `Gestión de Proyectos y Servicios` > `Transacciones` > `Crear facturas de gastos AP`

Este es un proceso que genera automáticamente Facturas (Proveedor) para Cuentas a pagar en base a todos los gastos a reembolsar al operario. Se generarán Facturas (Proveedor) separadas para cada proyecto. 

Para que el proceso se complete correctamente, el operario debe tener la solapa Proveedor en el Tercero completada, incluyendo la siguiente información:

- Una tarifa de compra
- El método de pago de OC
- Las condiciones de pago de OC
- La cuenta financiera de OC

Este proceso está integrado directamente con el módulo [Gestión de Compras](../procurement-management/getting-started.md): todas las facturas de compra generadas pueden revisarse y modificarse a través de ese módulo.

![](../../../../assets/user-guide/etendo-classic/basic-features/project-and-services-management/transactions/create-ap-expense-invoices.png)

---

Este trabajo es una obra derivada de [Gestión de Proyectos y Servicios](https://wiki.openbravo.com/wiki/Project_and_Service_Management){target="\_blank"} de [Wiki de Openbravo](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.