---
title: Gestión de Producción
---

## Orden de Fabricación

:material-menu: `Aplicación` > `Gestión de Producción` > `Transacciones` > `Orden de Fabricación`

### Visión general

En esta ventana, el usuario puede crear y gestionar una orden para que un [_Plan de Producción_](setup.md#process-plan) se ejecute un determinado número de veces para satisfacer los requisitos de producción.

!!! warning
    Importante: antes de crear una orden de fabricación, es necesario tener definido un Plan de Producción.

Una orden de fabricación es un documento que indica qué se debe producir y para qué fecha. La orden de fabricación se crea en base a un plan de producción. Las secuencias con sus detalles relacionados se completan en la orden de fabricación. Una vez que las secuencias se han completado, la información puede sobrescribirse si es necesario.

Una orden de fabricación puede crearse de dos maneras:

- manualmente en la pantalla
- automáticamente como resultado del plan de fabricación en MRP.

### Cabecera

Aquí es posible crear órdenes de producción eligiendo fechas y el modelo de orden de fabricación definido previamente.

![](../../../../assets/user-guide/etendo-classic/basic-features/production-management/transactions/work-requirement-0.png)

**Organización**: organización en la que se ejecutará la producción.

**Tipo de documento**: se utiliza para facilitar el filtrado; por ejemplo, se pueden configurar nombres de departamentos de producción separados como tipos de documento.

**Nº de documento**: número de la orden de fabricación.

**Plan de Producción**: nombre del plan de producción que se utiliza para esta producción.

**Cantidad**: número de lotes a producir. El campo se completa automáticamente en función de la cantidad secundaria introducida y la tasa de conversión.

**F.lanzamiento**: la fecha en la que se crea el documento. Esta fecha se utiliza como referencia para definir la versión correspondiente del plan de producción.

**Fecha de inicio**: fecha en la que se planifica el inicio de la producción.

**Fecha final**: fecha en la que se planifica el fin de la producción.

**Rangos**: tamaño del lote para la producción.

**Incluir fases al insertar**: cuando la casilla está seleccionada, en la orden de fabricación, al copiar la información del plan de producción, se incluyen las secuencias y los productos. La configuración también existe en el plan de producción, pero puede sobrescribirse en esta pantalla si es necesario.

**Cantidad Secundaria**: cantidad total a producir.

**Unidad proceso**: el producto a producir.

**Tiempo estimado**: información del tiempo estimado de ejecución, que se completa cuando se procesa la orden de fabricación. El cálculo es: tiempo estimado tomado del plan de producción x cantidad secundaria en la orden de fabricación.

**Tiempo de ejecución**: información completada del tiempo real de ejecución, tomada del parte de trabajo.

**Procesar Orden de Fabricación**: para insertar la información del plan de producción en la orden de fabricación.

**Crear Parte de Trabajo**: para crear partes de trabajo relacionados con la orden de fabricación una vez que la orden de fabricación se ha procesado. Los partes de trabajo relacionados con todas las secuencias se crean a la vez, por lo que, dependiendo del número de secuencias, se crean uno o más partes de trabajo. Si la casilla de crear estándares está seleccionada en la secuencia, también se ejecuta el proceso de crear estándares para insertar la información del producto en el parte de trabajo. En todos los casos, el procesado del parte de trabajo se ejecuta manualmente.

!!! note
    El proceso Crear estándares solo se completará correctamente si hay existencias suficientes para los productos utilizados (P-) de la secuencia. Si no hay existencias suficientes, no solo fallará el proceso Crear estándares, sino que tampoco se creará ningún Parte de Trabajo. Cuando hay existencias suficientes, el proceso Crear estándares se ejecuta correctamente y, por defecto, la Cantidad Realizada en la solapa Parte de Fabricación se establece en la cantidad completa de la secuencia.

### Secuencia

En esta solapa, el usuario puede añadir o editar secuencias y actividades a realizar para la orden de fabricación relacionada.

Después de procesar la Orden de Fabricación, la información en la solapa Secuencia se completa a partir del Plan de Producción. La solapa principal de la Orden de Fabricación muestra que la Orden de Fabricación está procesada y el Tiempo estimado muestra el total de los tiempos estimados de todas las secuencias.

![](../../../../assets/user-guide/etendo-classic/basic-features/production-management/transactions/work-requirement-1.png)

Los campos de estas dos solapas se toman en su mayoría del Plan de Producción, pero pueden sobrescribirse en la Orden de Fabricación. Para una descripción de estos campos, consulte la sección [Plan de Producción](setup.md#process-plan).

La **Fecha de inicio** y la **Fecha final** de las secuencias se establecen por defecto a partir de la solapa principal de la Orden de Fabricación, pero pueden sobrescribirse.

El **Tiempo estimado** en la secuencia se calcula usando la fórmula: tiempo estimado de la secuencia tomado del plan de producción x cantidad en la secuencia.

La **información del tiempo de ejecución** se completa en base al total de horas reales completadas desde el Parte de Trabajo para la secuencia.

**Cerrar fase**: con este proceso, se cierra la fase de la orden de fabricación. Si todas las fases están cerradas, la orden de fabricación también se cerrará.

### Producto

En esta solapa, es posible añadir o editar productos de entrada/salida a utilizar para la secuencia seleccionada de la orden de fabricación.

La información en la solapa Producto se completa a partir de la información en la solapa de productos de entrada/salida del Plan de Producción, al procesar la Orden de Fabricación.

![](../../../../assets/user-guide/etendo-classic/basic-features/production-management/transactions/work-requirement-2.png)

- **Cant. movida**: valor completado a partir del campo Cantidad en la solapa de productos de entrada/salida del Plan de Producción.

!!! info
    Para una descripción del resto de los campos, consulte el [Plan de Producción](setup.md#process-plan).
## Parte de Trabajo

:material-menu: `Aplicación` > `Gestión de Producción` > `Transacciones` > `Parte de Trabajo`

### Visión general

En esta ventana, el usuario puede editar con precisión lo que se ha producido a partir de una orden de producto seleccionada.

El parte de trabajo registra el trabajo ejecutado por los empleados durante un turno de producción. El documento se utiliza para los siguientes propósitos:

- calcular el coste real relacionado con la producción de un producto.
- realizar el seguimiento del esfuerzo restante en las órdenes de fabricación.

### Parte de Trabajo

Aquí, es posible crear un informe para la orden de fabricación completada para una fecha y hora deseadas.

![](../../../../assets/user-guide/etendo-classic/basic-features/production-management/transactions/work-effort-0.png)

- La Fecha de movimiento, **Comienzo** y **Fin** indican en qué fecha y durante qué turno tuvo lugar la producción.
- El botón Crear estándares (mostrado en la solapa "Parte de Fabricación") se utiliza para ejecutar el proceso que carga toda la información P- y P+, así como los productos de consumo global, máquinas, categorías salariales, coste indirecto y utillajes. Cuando se crean los estándares, también se comprueba el stock de todos los productos P- y aparece un error si algún producto no tiene stock. Para que el proceso Crear estándares finalice correctamente, la **Cantidad Realizada** debe ser mayor que cero.
- Una vez creados los estándares e introducida toda la información correcta relativa a la producción, el parte de trabajo se valida haciendo clic en el botón Validar Parte de Trabajo. En este punto, se actualiza la información de stock. Para P-, el stock disminuye y, para P+, aumenta.
- Opcionalmente, el Parte de Trabajo puede contabilizarse en el diario del libro mayor una vez añadida la [configuración](../../../../user-guide/etendo-classic/basic-features/production-management/getting-started.md#initial-configuration). Si se realiza, se contabiliza la información relacionada con el coste de la materia prima y de los productos producidos.

### Operarios

Aquí, es posible añadir empleados que participaron en la finalización de una orden de fabricación relacionada.

Cualquier tercero que esté configurado como operario en la solapa Operarios de la pantalla Terceros, puede seleccionarse como empleado que trabajó en la producción del producto.

![](../../../../assets/user-guide/etendo-classic/basic-features/production-management/transactions/work-effort-1.png)

### Incidencia

Aquí, es posible añadir incidencias de trabajo que puedan haber ocurrido durante la finalización de una orden de fabricación relacionada.

Esta solapa se utiliza para registrar cualquier incidencia que ocurra durante el parte de fabricación, la cantidad de tiempo de inactividad que causó y una descripción.

![](../../../../assets/user-guide/etendo-classic/basic-features/production-management/transactions/work-effort-2.png)

### Consumo Global

Aquí, es posible añadir el consumo global de productos utilizados para la finalización de una orden de fabricación relacionada.

En esta solapa, se introducen los productos que no están especificados en el plan de producción pero que se utilizan en producción. Por ejemplo, material de embalaje:

![](../../../../assets/user-guide/etendo-classic/basic-features/production-management/transactions/work-effort-3.png)

### Parte de Fabricación

Aquí, es posible añadir detalles de progreso de las órdenes de fabricación especificadas.

La información relacionada con la secuencia ejecutada se introduce en esta solapa:

![](../../../../assets/user-guide/etendo-classic/basic-features/production-management/transactions/work-effort-4.png)

- **Cantidad Necesaria**: cantidad necesaria de la secuencia. Se completa la información cuando se selecciona la fase de la orden de fabricación.
- **Cantidad Realizada:** la cantidad de unidades producidas.
- **Comienzo**: hora real de inicio del parte de fabricación
- **Fin**: hora real de fin del parte de fabricación
- **Cantidad Rechazada**: campo solo informativo de cualquier cantidad rechazada durante la producción de la secuencia.
- **Uso de CC**: el uso real del centro de costes para esta secuencia
- **Casilla Subcontratado**: indicación de que la secuencia está siendo ejecutada por un tercero
- **Casilla Cerrar fase**: se selecciona si se construyó una cantidad parcial, pero la secuencia debe cerrarse indicando que la cantidad restante no se construirá.

### Utillajes

Aquí, es posible añadir o editar utillajes utilizados para completar una parte específica de una orden de fabricación.

La información de esta solapa se completa automáticamente cuando se ejecuta el proceso crear estándares. La información se toma de la información de utillajes en la pantalla de actividad. El uso de utillajes se completa en función del coeficiente de utilización en la pantalla de actividad multiplicado por la cantidad realizada en el parte de trabajo. La información que se completa puede actualizarse con la información real de los utillajes utilizados durante la producción, antes de validar el parte de trabajo.

![](../../../../assets/user-guide/etendo-classic/basic-features/production-management/transactions/work-effort-5.png)

### Producto

Aquí, es posible añadir y editar productos de entrada/salida relacionados con una parte completada de una orden de fabricación.

La información se completa automáticamente cuando se ejecuta el proceso crear estándares, en base a la información de la fase de la orden de fabricación y la cantidad realizada en el parte de trabajo. La información que se completa puede actualizarse con la información real del producto antes de validar el parte de trabajo.

![](../../../../assets/user-guide/etendo-classic/basic-features/production-management/transactions/work-effort-6.png)

!!! info
    Para más detalles sobre los campos, consulte la sección del [_Plan de Producción_](setup.md#process-plan).

### Categoría Salarial / Empleado

Aquí, el usuario puede añadir o editar trabajadores por categoría salarial que participaron en una orden de fabricación.

!!! info
    La información de esta solapa se completa automáticamente cuando se ejecuta el proceso crear estándares, teniendo en cuenta la información de empleados del plan de producción. La información que se completa puede actualizarse con la información real del esfuerzo de los empleados durante la producción antes de validar el parte de trabajo.

![](../../../../assets/user-guide/etendo-classic/basic-features/production-management/transactions/work-effort-7.png)

- **Categoría Salarial**: información tomada de la configuración del centro de costes. La información completada puede actualizarse, por ejemplo, para introducir otra línea para empleados adicionales con diferentes categorías salariales.
- **Terceros**: el nombre del empleado que ejecutó la producción.
- **Cantidad**: el número de empleados de esta categoría salarial que ejecutaron la producción. En la configuración del centro de costes, se define el número de empleados de una categoría salarial concreta que están relacionados con el centro de costes. El valor puede sobrescribirse aquí para reflejar un número diferente de empleados.
- **Costo calculado**: el coste calculado cuando se calculan los costes de producción, que tiene en cuenta el tiempo de uso del centro de costes.
- **Tiempo de ejecución**: el tiempo dedicado por empleado a la producción.

### Costo Indirecto

Aquí, es posible añadir y editar costes indirectos relacionados con una parte completada especificada de una orden de fabricación.

!!! info
    La información de esta solapa se completa automáticamente cuando se ejecuta el proceso crear estándares, en base al coste indirecto introducido en el plan de producción. La información que se completa puede actualizarse con la información real de cualquier coste indirecto relacionado con la producción, antes de validar el parte de trabajo.

![](../../../../assets/user-guide/etendo-classic/basic-features/production-management/transactions/work-effort-8.png)

### Máquina

Aquí, es posible añadir y editar recursos utilizados para completar una parte especificada de una orden de fabricación.

!!! info
    La información de esta solapa se completa automáticamente cuando se ejecuta el proceso crear estándares, en base a la información de máquina introducida en el plan de producción. La información que se completa puede actualizarse con la información real de las máquinas utilizadas durante la producción, antes de validar el parte de trabajo.

![](../../../../assets/user-guide/etendo-classic/basic-features/production-management/transactions/work-effort-9.png)

### Subcontratado

Aquí, es posible añadir facturas correspondientes a la parte subcontratada de una orden de fabricación completada.

!!! info
    Cualquier coste subcontratado de la producción se introduce manualmente en esta solapa en base a las facturas de compra recibidas de la empresa que ejecutó el trabajo subcontratado.

![](../../../../assets/user-guide/etendo-classic/basic-features/production-management/transactions/work-effort-10.png)

### Cómo reactivar Partes de Trabajo

<iframe width="560" height="315" src="https://www.youtube.com/embed/KRcwM9tuMus?si=0w0iPDl9KGgWaLYT" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

!!! info
    Esta funcionalidad está disponible a partir de la versión **1.0.0** del Production Extensions Bundle, desde **Etendo 25.1**. Para poder incluir esta funcionalidad, debe instalarse el Production Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Production Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=7C68641225CE46A6BF8A39993CC8E1E5){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Production Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/production-extensions/release-notes.md). 

Esta funcionalidad es útil cuando el usuario necesita reactivar un parte de trabajo.

Desde la ventana Parte de Trabajo, el usuario puede reactivar un parte generado previamente simplemente seleccionando el registro correspondiente y haciendo clic en el botón Reactivar.

Una vez que el parte se reactiva correctamente, el estado del documento cambia a No procesado, tal y como puede observarse en la barra de estado.

![](../../../../assets/user-guide/etendo-classic/basic-features/production-management/transactions/work-effort-11.png)

!!! note
    No es posible reactivar documentos que incluyan transacciones con cantidades que excedan la cantidad de stock existente para un determinado producto en un determinado hueco. La única excepción es cuando la configuración del hueco permite Over Issue. Para más información, visite [Hueco](../../../../user-guide/etendo-classic/basic-features/warehouse-management/setup.md#storage-bin).

### Cómo anular Partes de Trabajo

<iframe width="560" height="315" src="https://www.youtube.com/embed/KRcwM9tuMus?si=0w0iPDl9KGgWaLYT" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

!!! info
    Esta funcionalidad está disponible a partir de la versión **3.4.0** del Production Extensions Bundle, desde **Etendo 22.1**. Para instalarla, siga las instrucciones del marketplace: [Production Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=7C68641225CE46A6BF8A39993CC8E1E5){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Production Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/production-extensions/release-notes.md). 

Esta funcionalidad es útil cuando el usuario necesita anular un parte de trabajo completado.

Desde la ventana Parte de Trabajo, el usuario puede anular un parte de trabajo completado previamente seleccionando el registro correspondiente y haciendo clic en la acción de documento **Anular**.

La acción **Anular** está disponible cuando:

- El Parte de Trabajo está Completado/Procesado
- El Parte de Trabajo no ha sido anulado previamente
- No existen inconsistencias que impidan la reversión
- El Parte de Trabajo no está contabilizado en el libro mayor

Al ejecutar la acción **Anular**, el sistema automáticamente:

- Crea un documento de Parte de Trabajo de reversión
- Copia la cabecera y las líneas con cantidades negativas
- Genera movimientos de inventario inversos
- Marca el documento original como **ANULADO**

### Contabilización masiva

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

La funcionalidad de Contabilización masiva permite al usuario contabilizar o descontabilizar múltiples registros seleccionando los registros correspondientes y haciendo clic en el botón **Contabilización masiva**.

Además, el Estado contable del/de los registro/s se muestra en la barra de estado, en vista de formulario, o en una columna, en vista de rejilla.

!!! info
    Para más información, visite [Contabilización masiva](../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md) en la documentación del Financial Extensions Bundle.
## Parte de Fabricación

:material-menu: `Aplicación` > `Gestión de Producción` > `Transacciones` > `Parte de Fabricación`

### Visión general

Aquí, el usuario puede editar con precisión lo que se ha producido a partir de una orden de producto seleccionada.

La pantalla **Parte de Fabricación** muestra los **Partes de Trabajo** que no están validados. Los **Partes de Trabajo** listados se crean desde la pantalla **Orden de Fabricación** o directamente en la pantalla **Parte de Trabajo**. La pantalla ofrece una visión general a los operarios de producción de las tareas de producción que están programadas para ejecutarse.

### Parte de Fabricación

En esta ventana, es posible añadir detalles de avance de las **Órdenes de Fabricación** especificadas.

Las pantallas son idénticas a **Parte de Trabajo**, con la excepción de que no se muestra la solapa principal del **Parte de Trabajo**, sino directamente la información en la solapa **Parte de Fabricación**. De este modo, la pantalla ofrece una visión general fácil de leer de los partes de fabricación planificados. La información de **Incidencia** es una solapa en **Parte de Fabricación**. El número de **Parte de Fabricación** se corresponde con el número de **Parte de Trabajo**.

![](../../../../assets/user-guide/etendo-classic/basic-features/production-management/transactions/production-run-0.png)

!!! info
    Para más detalles sobre los campos, consulte la sección [Parte de Fabricación Parte de Trabajo](#parte-de-fabricación).

!!! warning
    La eliminación de un parte de fabricación se realiza en el **Parte de Trabajo** correspondiente, no en esta pantalla.

### Incidencia

En esta solapa, es posible añadir incidencias de trabajo que podrían haber ocurrido durante la finalización de una **Orden de Fabricación** relacionada.

![](../../../../assets/user-guide/etendo-classic/basic-features/production-management/transactions/production-run-1.png)

!!! info
    Consulte la sección [Incidencia Parte](#incidencia) para más detalles.

### Utillajes

Aquí, es posible añadir o editar utillajes utilizados para completar una parte especificada de una **Orden de Fabricación**.

![](../../../../assets/user-guide/etendo-classic/basic-features/production-management/transactions/production-run-2.png)

!!! info
    Consulte la sección [Utillajes Parte de Trabajo](#utillajes) para más detalles.

### Producto

Aquí, es posible añadir y editar productos de entrada/salida relacionados con una parte completada de una **Orden de Fabricación**.

![](../../../../assets/user-guide/etendo-classic/basic-features/production-management/transactions/production-run-3.png)

!!! info
    Consulte la sección [Producto Parte de Trabajo](#producto) para más detalles.

### Categoría Salarial / Operarios

Aquí, es posible añadir o editar operarios de categoría salarial que participaron en una **Orden de Fabricación**.

![](../../../../assets/user-guide/etendo-classic/basic-features/production-management/transactions/production-run-4.png)

!!! info
    Consulte la sección [Categoría Salarial/Operarios Parte de Trabajo](#categoría-salarial--operarios) para más detalles.

### Costo Indirecto

Aquí, es posible añadir y editar costos indirectos relacionados con una parte completada especificada de una **Orden de Fabricación**.

![](../../../../assets/user-guide/etendo-classic/basic-features/production-management/transactions/production-run-5.png)

!!! info
    Consulte la sección [Costo Indirecto Parte de Trabajo](#costo-indirecto) para más detalles.

### Máquina

Aquí, es posible añadir y editar recursos utilizados para completar una parte especificada de una **Orden de Fabricación**.

![](../../../../assets/user-guide/etendo-classic/basic-features/production-management/transactions/production-run-6.png)

!!! info
    Consulte la sección [Máquina Parte de Trabajo](#máquina) para más detalles.

### Subcontratado

Aquí, es posible añadir facturas correspondientes a la parte subcontratada de una **Orden de Fabricación** completada.

![](../../../../assets/user-guide/etendo-classic/basic-features/production-management/transactions/production-run-7.png)

!!! info
    Consulte la sección [Subcontratado Parte de Trabajo](../../../../user-guide/etendo-classic/basic-features/production-management/transactions.md#outsourced) para más detalles.
## Toma de Datos de PCC

:material-menu: `Aplicación` > `Gestión de Producción` > `Transacciones` > `Toma de Datos de PCC`

### Visión general

En esta ventana, es posible crear y editar mediciones e informar hallazgos en puntos de control predefinidos. El objetivo es garantizar la calidad del resultado durante la producción.

Para el ciclo de producción, se puede configurar un Punto de Control de Calidad, con el fin de ejecutar una comprobación relacionada con el proceso de producción. Por ejemplo, comprobaciones sobre maquinaria o herramientas que se utilizan en producción.

La ejecución de las comprobaciones se documenta en la Toma de Datos de PCC.

### Fecha y  turno

Aquí, es posible crear mediciones e insertar los valores recopilados o una fecha y un turno específicos.

La fecha y el turno durante los cuales se documenta un punto de control de calidad concreto, así como la hora en la que tuvo lugar la comprobación. Además, se introduce un nombre de contacto:

![](../../../../assets/user-guide/etendo-classic/basic-features/production-management/transactions/quality-control-report-0.png)

El botón **Crear PCC** se utiliza para completar automáticamente la información en las solapas **Grupos** y **Hora** sobre la(s) comprobación(es) que están configuradas para realizarse durante el turno seleccionado.

![](../../../../assets/user-guide/etendo-classic/basic-features/production-management/transactions/quality-control-report-1.png)

Una vez que se ha ejecutado la acción anterior, aparece el botón **Editar valores medidos del PCC**. Al hacer clic, aparece una ventana emergente en la que se introduce el valor de la comprobación:

![](../../../../assets/user-guide/etendo-classic/basic-features/production-management/transactions/quality-control-report-2.png)

Después de introducir el valor y hacer clic en el botón **Aceptar**, el valor introducido aparece en la solapa **Valores**.

Una vez que el valor se ha introducido de esta forma, aparece el botón **Introducir medición de tiempo**. Al hacer clic, aparece una ventana emergente para procesar la información introducida en la solapa **Hora**:

![](../../../../assets/user-guide/etendo-classic/basic-features/production-management/transactions/quality-control-report-3.png)

### Grupos

En esta solapa, es posible crear y editar puntos de control para la medición relacionada.

La información se completa con cualquier comprobación que tenga lugar durante el turno.

![](../../../../assets/user-guide/etendo-classic/basic-features/production-management/transactions/quality-control-report-4.png)

#### Hora

Aquí, es posible crear y editar horas para los puntos de control relacionados.

La información se completa automáticamente cuando se hace clic en el botón **Crear PCC**: la hora que aparece es la fecha de inicio del turno que está configurada en la información de [Turno de puntos de control](../../../../user-guide/etendo-classic/basic-features/production-management/setup.md#shift). Cuando se completa automáticamente, el estado se procesa.

En el caso de que la información se introduzca manualmente, la información se procesa haciendo clic en el botón **Introducir medición de tiempo**.

![](../../../../assets/user-guide/etendo-classic/basic-features/production-management/transactions/quality-control-report-5.png)

#### Valores

Aquí, es posible crear y editar valores para una medición relacionada.

!!! info
    La información en esta solapa se completa automáticamente cuando se hace clic en el botón **Editar valores medidos del PCC** y se introduce un valor en la pantalla emergente. Alternativamente, se puede introducir manualmente un valor de lo que se midió durante la comprobación.

![](../../../../assets/user-guide/etendo-classic/basic-features/production-management/transactions/quality-control-report-6.png)
## Datos del control de calidad periódico

:material-menu: `Aplicación` > `Gestión de Producción` > `Transacciones` > `Datos del control de calidad periódico`

### Visión general

En esta ventana, el usuario puede crear y editar la recopilación de datos y las mediciones relacionadas con el control de calidad. Esto se realiza en puntos de control predefinidos para un producto fabricado.

!!! info
    Los resultados del control de calidad periódico ejecutado se documentan en esta pantalla.

### Ventana Datos del control de calidad periódico

Es posible crear mediciones en un punto de control predefinido para productos producidos.

En esta pantalla se introduce toda la información general relevante sobre el control de calidad ejecutado, como qué comprobación se ejecutó, cuándo y para qué producto:

![](../../../../assets/user-guide/etendo-classic/basic-features/production-management/transactions/periodic-quality-control-data-0.png)

Después de completar la información de la solapa principal, se hace clic en el botón **Ejecutar control periódico** para completar la información en la solapa **Resultado**.

#### Resultado

En esta solapa, es posible crear y editar pruebas de calidad para un punto de control especificado, y añadir los resultados de las pruebas realizadas.

!!! info
    Toda la información de esta solapa se completa automáticamente mediante el proceso **Ejecutar control periódico**, excepto el campo **Resultado de la prueba**, que se introduce manualmente.

![](../../../../assets/user-guide/etendo-classic/basic-features/production-management/transactions/periodic-quality-control-data-1.png)
## Consumo interno

:material-menu: `Aplicación` > `Gestión de Producción` > `Transacciones` > `Consumo interno`

### Visión general

En esta ventana, es posible definir productos que solo se utilizarán dentro de la empresa.

La pantalla de **Consumo interno** se utiliza para administrar cualquier producto que se use durante la ejecución de tareas de mantenimiento. Al procesarlo, el stock se reduce. Los productos se compran a través del [proceso de aprovisionamiento](../../../../user-guide/etendo-classic/basic-features/procurement-management/getting-started.md). Los productos se configuran como un artículo normal, sin seleccionar la casilla de verificación **Producción**, ya que no forman parte del proceso de producción.

### Cabecera

Aquí, es posible crear productos que se utilizarán dentro de la organización y no se venderán a clientes.

![](../../../../assets/user-guide/etendo-classic/basic-features/production-management/transactions/internal-consumption-0.png)

El nombre es un valor seleccionable en la solapa **Mantenimiento** de la [Parte de Mantenimiento](#parte-de-mantenimiento).

!!! info
    Opcionalmente, el **Consumo interno** puede contabilizarse en el diario del libro mayor una vez añadida la configuración. Si se hace, se contabiliza la información relacionada con el coste del producto.

### Líneas

Aquí, es posible añadir líneas de consumo interno. Cada línea corresponde a un producto.

Se introduce la información del producto, su ubicación en el almacén y la cantidad utilizada durante la tarea de mantenimiento. Al hacer clic en **Procesar Consumo interno**, el nivel de stock disminuye con la **Cant. movida** seleccionada.

![](../../../../assets/user-guide/etendo-classic/basic-features/production-management/transactions/internal-consumption-1.png)

### Cómo reactivar Consumo interno

!!! info
    Esta funcionalidad está disponible a partir de la versión **3.4.0** del Production Extensions Bundle, desde **Etendo 25.1**. Para instalarlo, siga las instrucciones del marketplace: [Production Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=7C68641225CE46A6BF8A39993CC8E1E5){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Production Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/production-extensions/release-notes.md). 

Esta funcionalidad es útil cuando el usuario necesita reactivar un documento de consumo interno.

Desde la ventana **Consumo interno**, el usuario puede reactivar un documento de consumo interno previamente procesado seleccionando el registro correspondiente y haciendo clic en el botón **Reactivar**.

Una vez que el documento se reactiva correctamente:

- El estado del documento vuelve a **Borrador**, tal y como se puede observar en la barra de estado.
- Se eliminan las transacciones de material generadas por el documento, revirtiendo todos los movimientos de inventario.

!!! warning
    No es posible reactivar documentos de consumo interno cuando existen costes calculados asociados a las transacciones del documento. La reactivación solo se permitirá cuando no se hayan realizado cálculos de costes sobre el documento.

### Contabilización masiva

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Financial Extensions Bundle. Para instalarlo, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

La funcionalidad de **Contabilización masiva** permite al usuario contabilizar o deshacer la contabilización de múltiples registros seleccionando los registros correspondientes y haciendo clic en el botón **Contabilización masiva**.

Además, el estado contable del/de los registro/s se muestra en la barra de estado, en la vista de formulario, o en una columna, en la vista de cuadrícula.

!!! info
    Para más información, visite [Contabilización masiva](../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md) en la documentación del Financial Extensions Bundle.
## Parte de Mantenimiento

:material-menu: `Aplicación` > `Gestión de Producción` > `Transacciones` > `Parte de Mantenimiento`

### Visión general

En esta ventana, es posible crear y editar los resultados de un parte de mantenimiento programado.

Este documento se utiliza para registrar la ejecución y los resultados de las tareas de mantenimiento. Cualquier tarea que se confirme en el [mantenimiento programado](#mantenimiento-programado) se puede seleccionar en esta pantalla.

### Parte

Aquí, es posible añadir mantenimientos previamente programados para una fecha específica e informar observaciones.

En la sección principal del documento, se seleccionan la fecha y el turno durante el cual se ejecutaron las tareas.

![](../../../../assets/user-guide/etendo-classic/basic-features/production-management/transactions/maintenance-order-0.png)

- se pulsa el botón **Insertar Mantenimientos** para completar la información en la solapa **Mantenimiento**. En el siguiente caso, no se encuentran mantenimientos programados.

![](../../../../assets/user-guide/etendo-classic/basic-features/production-management/transactions/maintenance-order-1.png)

- **Casilla OK**: para indicar que el mantenimiento finalizó correctamente. En la solapa **Mantenimiento**, esto hace que la casilla **Resultado** aparezca seleccionada.
- **Hora**: tiempo en horas para ejecutar el mantenimiento.
- **Observaciones**: aquí se introducen los resultados de la tarea de mantenimiento.

#### Responsable

En esta solapa, es posible añadir o editar responsables que participaron en un parte de mantenimiento específico.

El operario que ejecutó la tarea de mantenimiento se introduce en esta solapa. Según la información de la sección de configuración, todos los empleados que tengan seleccionada la casilla de operario aparecen en la lista de valores del campo de terceros en esta pantalla.

![](../../../../assets/user-guide/etendo-classic/basic-features/production-management/transactions/maintenance-order-2.png)

### Mantenimiento

En esta solapa, es posible editar las tareas de mantenimiento de un parte específico.

!!! info
    La mayor parte de la información de esta solapa se completa automáticamente al pulsar el botón **Insertar Mantenimientos**, excepto el campo **Consumo interno**. Solo el campo **Consumo interno** y el campo **Observaciones** son actualizables. En esta pantalla, cualquier producto que se haya utilizado para la ejecución de las tareas de mantenimiento se introduce en el campo **Consumo interno**. Para más información, consulte la sección [Consumo interno](#consumo-interno).

![](../../../../assets/user-guide/etendo-classic/basic-features/production-management/transactions/maintenance-order-3.png)

- **Casilla Resultado**: indica que la tarea de mantenimiento se ejecutó correctamente. Si el resultado no es satisfactorio, la tarea se considera igualmente completada. Para cualquier acción de seguimiento, se crea un nuevo mantenimiento programado.
## Insertar Mantenimientos

:material-menu: `Aplicación` > `Gestión de Producción` > `Transacciones` > `Insertar Mantenimientos`

### Visión general

El proceso **Insertar Mantenimientos** ejecuta la carga de las tareas de mantenimiento programadas en el [Mantenimiento Programado](#mantenimiento-programado) en función de la información de mantenimiento en la pantalla de categoría de máquina y/o de máquina.

La creación del plan de mantenimiento se basa en un rango de fechas que se introduce al lanzar el proceso.

![](../../../../assets/user-guide/etendo-classic/basic-features/production-management/transactions/insert-maintenances-0.png)
## Mantenimiento Programado

:material-menu: `Aplicación` > `Gestión de Producción` > `Transacciones` > `Mantenimiento Programado`

### Visión general

Aquí, es posible añadir y editar planes de mantenimiento predefinidos.

La información de **Mantenimiento Programado** se crea de 2 formas posibles:

- completada automáticamente por el proceso **Insertar Mantenimientos**
- manualmente: por ejemplo, para introducir datos cuando una máquina se avería y necesita mantenimiento correctivo.

Cualquier tarea de mantenimiento que tenga un [Parte de Mantenimiento](#parte-de-mantenimiento) vinculado, queda oculta por un filtro por defecto que se aplica a la pantalla.

### Mantenimiento

Aquí, es posible crear y editar tareas de mantenimiento para una fecha específica.

**Mantenimiento Programado** ofrece una visión general de todas las tareas de mantenimiento para un determinado período de tiempo que se introducen mediante el proceso **Insertar Mantenimientos** o manualmente. Independientemente de cómo se hayan creado los registros, la información puede actualizarse para cambiar fechas o añadir **Observaciones**.

Una vez que la tarea de mantenimiento se refleja correctamente, se selecciona la casilla de verificación de confirmación.

![](../../../../assets/user-guide/etendo-classic/basic-features/production-management/transactions/insert-maintenances-1.png)
## Calcular costo estándar

:material-menu: `Aplicación` > `Gestión de Producción` > `Transacciones` > `Calcular costo estándar`

### Visión general

El proceso **Calcular costo estándar** se ejecuta para generar el costo estándar (= teórico) de los productos fabricados.

La información de costos se configura en varias pantallas:

- en el [Plan de Producción](setup.md#process-plan), se define el uso del [Centro de costos](../../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup/cost-center.md)
- en el centro de costos, se definen los siguientes costos:
  - **Información de operarios**: información de categoría salarial, así como la cantidad utilizada por hora para el centro de costos. En base a esto, se calcula el costo del operario. El costo de la categoría salarial se introduce en la pantalla [Categoría Salarial](#salary-category--employee).
  - **Información de máquina**: la máquina y la información de uso se introducen en la pantalla del centro de costos. El costo de la máquina se introduce en la pantalla [Máquina](setup.md#machine_1).
  - **Información de costo indirecto**: se listan todos los ítems de costo indirecto relacionados con un centro de costos. El costo indirecto se introduce en la pantalla [Costo Indirecto](setup.md#indirect-cost_2).
- en el plan de producción, se definen las cantidades y el costo de los materiales utilizados en el proceso de producción.

Para la materia prima, se utiliza la información de la lista de precios para el costo del P-. La lista de precios de compra que se utiliza para el costo de la materia prima se marca como predeterminada.

La información de costos que se calcula para un producto P+ se utiliza cuando ese producto es un P- para otra operación**.**

La fórmula que utiliza el proceso es la siguiente:

(Costo del Centro de costos + Costo Operarios + Costo Máquinas + Costos Indirectos) + (Cantidad P- x Costo P-) = el costo por unidad.

Cuando se calculan los costos del centro de costos, máquinas, operarios y costos indirectos, se multiplican por diferentes valores en función de su unidad de medida:

- Si se utiliza Por hora, el costo se multiplica por el uso del centro de costos en el Plan de Producción
- Si se utiliza Por unidad, el costo se multiplica por la suma de las cantidades de los P+ de la secuencia.
- Si se utiliza Por kilogramo, el costo se multiplica por la suma del peso de todos los P+ de la secuencia.

Para los costos indirectos, está disponible el porcentaje de unidad de medida adicional. Esto añade el porcentaje definido al costo total calculado (centro de costos, operario, máquina, costos indirectos y productos P-). Por ejemplo, si se define como 1.15, se añade un 15% adicional al costo.

!!! info
        Para que el Costo Indirecto se incluya correctamente, es importante la siguiente configuración en la pantalla [Costo Indirecto](setup.md#indirect-cost_2):<br>
            -seleccione Tipo de costo = Producción,<br>
            -un rango de fechas que incluya la fecha del cálculo del costo estándar en la solapa Valores.<br>
        De este modo, se calcula el costo estándar para cada operación.

![](../../../../assets/user-guide/etendo-classic/basic-features/production-management/transactions/calculate-standard-costs-0.png)

El resultado del cálculo aparece en las solapas del Plan de Producción:

En las solapas Operarios, Máquina y Costo Indirecto, el resultado de los costos se completa automáticamente.

---

- Este trabajo es una obra derivada de [Gestión de Producción](http://wiki.openbravo.com/wiki/Production_Management){target="_blank"} por [Openbravo S.L.U](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, con licencia [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}.

- Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L](https://etendo.software){target="_blank"}.