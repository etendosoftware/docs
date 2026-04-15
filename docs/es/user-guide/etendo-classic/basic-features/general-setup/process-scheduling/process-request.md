---
title: Procesamiento de Peticiones
tags:
    - Procesamiento de Peticiones
    - Programación
    - Proceso en segundo plano
---

# Procesamiento de Peticiones

:material-menu: `Aplicación` > `Configuración General` > `Planificador de procesos` > `Procesamiento de Peticiones`

## Visión general

Un proceso en segundo plano es una acción del sistema solicitada por el usuario, quien debe proporcionar valores de parámetros auxiliares para ejecutar dicha acción.

La ventana Procesamiento de Peticiones permite al usuario revisar y añadir procesos en segundo plano, que pueden programarse o desprogramarse según sea necesario.

## Ventana Procesamiento de Peticiones

![alt text](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/process-scheduling/process-request.gif)

La información a completar para programar un proceso en segundo plano es:

1. Seleccione la **Organización** para la cual se va a programar el proceso en segundo plano.

2. Seleccione un **Proceso** o un **Grupo de Procesos** de la lista correspondiente. Para programar un Grupo de Procesos, marque el indicador **Grupo**; esto habilitará el campo **Grupo de Procesos**.

    !!! info
        Un Grupo de Procesos se programa de la misma manera que un proceso individual. Sin embargo, no puede programar un Grupo de Procesos y un proceso individual al mismo tiempo.
        
        Consulte la sección [Ventana Grupo de Procesos](../process-scheduling/process-group.md) para más detalles.

3. Seleccione el **Programado**. Las opciones de Programado se describen a continuación:

    === "**Ejecutar inmediatamente**"
        
        - Ejecuta el proceso inmediatamente.
        - No se requieren parámetros de configuración adicionales.

    === "**Ejecutar más tarde** "
        
        - Ejecuta el proceso una vez en un momento futuro especificado.
        - Campos de la sección **Programación**:
            - **Fecha inicio** y **Comienzo**: definen cuándo ocurrirá la primera ejecución.

    === "**Programar**"

        - Ejecuta el proceso de forma recurrente.
        - Campos de la sección **Programación**:
            - **Fecha inicio** y **Comienzo**: definen cuándo ocurrirá la primera ejecución.
            - **Frecuencia**: seleccione con qué frecuencia debe ejecutarse el proceso. Las opciones incluyen *cada n segundos*, *cada n minutos*, *cada hora*, *diariamente*, *semanalmente*, *mensualmente* o introduciendo una *Expresión Cron* personalizada. En función de la frecuencia seleccionada, pueden aparecer campos adicionales para una programación más precisa.
            - **Número de Repeticiones**: establezca cuántas veces debe repetirse el proceso después de la ejecución inicial. Por ejemplo, introducir 3 dará como resultado un total de 4 ejecuciones.
            - **Finaliza**: especifique cuándo debe dejar de ejecutarse el proceso. Puede establecer una *Fecha finalización* y una *Hora de finalización* para determinar el fin de la programación.

    !!! info
        - Los procesos definidos como **Ejecutar inmediatamente** y **Ejecutar más tarde** son ejecuciones únicas y pueden estar *Programados* o *Reprogramados*.
        - Los procesos definidos como **Programar** son ejecuciones recurrentes y pueden estar *Programados* o *Desprogramados*.

4. Seleccione la casilla **Seguridad basada en el Rol** para asegurar que solo el usuario que programa un proceso pueda monitorizarlo en la ventana del monitor de procesos; de lo contrario, cualquier usuario que comparta el mismo rol que el que programó el proceso podrá monitorizarlo.
    
    !!!tip
        En ambos casos, es necesario que el rol tenga acceso al proceso en la pestaña **Acceso a Proceso** de la ventana **Rol**.


### Monitor de Procesos

El monitor de procesos es una pestaña de solo lectura que permite revisar el estado de los procesos ejecutados por la petición actual.  
La información mostrada es la misma que en el [Monitor de Procesos](../process-scheduling/process-monitor.md).

![](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/process-scheduling/process-request/process-monitor.png)

### Procesos en Grupo

En caso de que el proceso ejecutado por el procesamiento de peticiones sea un **grupo de procesos**, aquí encontrará la información sobre las ejecuciones de los procesos del grupo para cada ejecución del grupo de procesos.

![](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/process-scheduling/process-request/process-group.png)


## Procesos clave en segundo plano

Existen algunos procesos en segundo plano que se configuran por defecto en la ventana de procesamiento de peticiones:

!!! info
    Todos estos procesos pueden programarse si se inicia sesión como **Administrador del sistema**.

- ### Servidor contable

    Este proceso busca y contabiliza automáticamente transacciones en estado **Completada** configuradas como **Contabilizado = No**.

    Este proceso permite que documentos como facturas de compra, facturas de venta o asientos del libro mayor se contabilicen automáticamente sin ninguna acción del usuario, salvo programar este proceso.

- ### Alerta
    
    Este proceso comprueba si la consulta SQL definida en cada regla de alerta activa devuelve algún registro para crear la instancia de alerta correspondiente.

    Este proceso también elimina las instancias de alertas fijas para asegurar que no se muestren más.

- ### Monitor de pagos

    Este proceso comprueba el estado de pago de la factura y actualiza la sección **Monitor de pagos** de la factura.  


Además, existen otros procesos en segundo plano que también pueden programarse y, por lo tanto, monitorizarse:

- ### Ejecutar pagos pendientes

    Este proceso comprueba y ejecuta cobros y pagos vinculados a un método de pago que tenga un Proceso de Ejecución de Pago **Automático**, que no estén configurados como **En espera** y que no requieran ninguna entrada para ejecutarse.

- ### Cálculo de costes
    Este proceso calcula el coste de las transacciones de material.

    El **Proceso en segundo plano de cálculo de costes** es el proceso encargado de buscar transacciones de mercancías cuyo coste aún no se ha calculado. Estas incluyen:

    - Recepciones de mercancía
    - Salidas de mercancía
    - Inventario físico
    - Movimientos de mercancía
    - Consumos internos
    - Producciones

    Este proceso considera únicamente transacciones cuya propiedad **Costing Status** sea:

    - No calculado
    - **Pendiente**.

    El proceso en segundo plano de cálculo de costes llama al proceso Servidor de cálculo de costes, que calcula el coste de cada transacción y tiene en cuenta lo configurado en la **Regla de cálculo de costes** definida para los productos; por lo tanto, o bien se tiene en cuenta la dimensión **Almacén** al calcular los costes, o bien se calcula el coste **medio** o **estándar** para los productos.

    Las transacciones se calculan secuencialmente ordenadas por la fecha de **Proceso de Transacción**, que es la fecha y hora en la que se procesó el documento que originó la transacción.

    Algunos algoritmos de cálculo de costes como **FIFO** implementan el estado de cálculo de costes **Pendiente** como una forma de retrasar el cálculo de costes de una o varias transacciones hasta la siguiente ejecución. De este modo, el proceso de cálculo de costes no se detiene para el resto de transacciones con estado No calculado o Pendiente, para las cuales sí es posible calcular el coste.

    !!! warning
        - El **proceso en segundo plano de cálculo de costes** debe configurarse para cada entidad legal definida en el cliente, ya que este proceso se ejecuta a nivel de entidad legal (Organización).
        
        - Es importante remarcar que si el proceso se programa a nivel de organización (\*), se ejecutará para todas las entidades legales definidas en el Cliente; por lo tanto, no sería necesario configurar el proceso más de una vez.

    !!! failure
        Si el Servidor de cálculo de costes muestra un error, el proceso en segundo plano se detiene y no es posible calcular el coste de ninguna transacción nueva hasta que se corrija el error.
        El mensaje de error puede consultarse en la ventana Monitor de Procesos.

    !!! info
        Aunque el proceso en segundo plano de cálculo de costes pueda haber **fallado**, el monitor de procesos podría mostrar un Éxito. Consulte el campo **Histórico del Proceso** para obtener el mensaje real del resultado.

- ### Corrección de precio

    El proceso en segundo plano de corrección de precio busca recepciones de mercancía que, o bien tengan un pedido de compra relacionado que haya sido reactivado y contabilizado después de completar las recepciones de mercancía, o bien tengan una factura de compra relacionada.

    Después, este proceso comprueba y compara si:

    - El precio del pedido de compra ha cambiado antes de que se contabilizara la factura
    - El precio de la factura de compra no es el mismo que el precio del pedido de compra.

    Si el precio de compra ha cambiado, se crea un ajuste de costes de **Corrección de precio** para los productos incluidos en la(s) recepción(es) de mercancía.

    !!! info
        Existe un proceso de menú denominado **Procesar ajuste de diferencia de precio** que ajusta manualmente todas las recepciones de mercancía ya facturadas, si fuese necesario.

    Puede ver los cambios en la ventana [Ajuste de Costes](../../warehouse-management/transactions.md#cost-adjustment).

- ### Conciliar líneas de factura y albarán con pedido de venta

    !!! info
        Este proceso está disponible a partir de **Etendo 25.4**.

    Este proceso actualiza las tablas de conciliación de ventas (Facturas de venta conciliadas y Pedidos de venta conciliados) para documentos de venta existentes.

    El proceso busca facturas de venta y salidas de mercancía de ventas completadas, cerradas, anuladas o revertidas dentro de un periodo configurable (definido por la preferencia `MatchedSalesDaysBack`), y crea o actualiza registros de conciliación entre:

    - Pedidos de venta y salidas de mercancía
    - Pedidos de venta y facturas de venta
    - Salidas de mercancía y facturas de venta

    Esta información de conciliación se utiliza para la trazabilidad y los cálculos del estado de la factura. El proceso no contabiliza ningún asiento contable.
    
    !!! info
        Este ejemplo muestra que el proceso debe ejecutarse. A partir de **Etendo 25.4**, esta información de conciliación se completa automáticamente al completar salidas de mercancía. Sin embargo, si las tablas conciliadas muestran cero registros, es necesario ejecutar este proceso para recalcular y completar los datos.

        ![alt text](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/process-scheduling/process-request/match-sales-order-invoice-and-shipment-lines-process.png)
        
    !!! info
        La preferencia `MatchedSalesDaysBack` se establece por defecto en 90 días. Para aumentar este periodo, puede crearse un nuevo registro para esta preferencia y el proceso puede volver a ejecutarse.

---

Este trabajo es una obra derivada de [Configuración General](https://wiki.openbravo.com/wiki/General_Setup){target="_blank"} de [Wiki de Openbravo](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="_blank"} por [Etendo](https://etendo.software){target="_blank"}.