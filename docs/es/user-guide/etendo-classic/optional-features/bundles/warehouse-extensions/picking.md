---
title: Lista de picking
tags: 
    - Listas de picking
    - Picking directo
    - Albaranes de picking
    - Picking de salida
    - Almacén
    - Existencias

---

# Lista de picking


:octicons-package-16: Javapackage: `org.openbravo.warehouse.pickinglist`

:octicons-package-16: Javapackage: `org.openbravo.warehouse.structure`
## Visión general

Esta sección describe el módulo **Etendo Picking List** incluido en el bundle *Warehouse Extensions*.

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Warehouse Extensions Bundle. Para ello, siga las instrucciones del marketplace: [_Warehouse Extensions Bundle_](https://marketplace.etendo.cloud/?#/product-details?module=BAE67A5B5BC4496D9B1CA002BBCDC80E){target="_blank"}. Para más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Warehouse Extensions - Notas de la versión](../../../../../whats-new/release-notes/etendo-classic/bundles/warehouse-extensions/release-notes.md).

Este módulo implementa y mejora la gestión de las **operaciones de picking** dentro de un almacén. Para gestionar y entregar las listas de picking, el módulo hace un uso intensivo de 2 funcionalidades core que deben estar habilitadas:

- [Reserva de existencias](../../../basic-features/warehouse-management/transactions.md#stock-reservation): Cuando se crean listas de picking, los productos incluidos en ellas quedan reservados. Esto significa que ninguna otra lista de picking ni ningún otro proceso puede utilizar esos productos.

- Proyecto de estado del documento: Con esta funcionalidad, el usuario puede saber fácilmente si un pedido de venta está pendiente de ser entregado o no.

En Etendo hay 2 tipos de listas de picking disponibles:

- **Picking de salida** es un proceso dentro de la gestión de almacén que implica la preparación y el movimiento de productos desde sus huecos de almacenamiento en el almacén hasta una **ubicación de salida específica** para su posterior embalaje y envío al cliente.

- **Lista de picking directa al cliente** es un proceso en el que los productos se envían sin pasar por un **hueco de salida intermedio**.
## Configuración inicial

Para poder generar listas de picking, es necesaria cierta configuración:

- **Tipo de documento**: El tipo de documento **Lista de picking** debe definirse para cada organización. El módulo proporciona un conjunto de datos con tipos de documento básicos que se pueden aplicar. Vaya a [Gestión del módulo de Empresa](../../../basic-features/general-setup/enterprise-model/enterprise-module-management.md) y aplique el conjunto de datos **Lista de picking de almacén** para cada organización que utilice listas de picking. Una vez aplicado, se crean los tipos de documento.

    ![picking1](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/picking/picking1.png)


    El conjunto de datos añade tres nuevos tipos de documento, con sus propias secuencias de documento, que aplicarán lo siguiente en cada organización:

    ![picking1.1](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/picking/picking1.1.png)

    1. **Lista de picking**: Se utiliza para el tipo de lista de picking **Lista de picking directa al cliente**. Al usar este tipo de documento, el sistema crea los albaranes desde la ubicación de picking. Cuando se completan, el **Albarán (Cliente)** se completa.

    2. **Lista de picking de salida**: Se utiliza para **Lista de picking de salida**, por lo tanto, el indicador **Usar ubicación de salida** se establece como **Sí** de forma predeterminada. Esto significa que es necesario crear un **Movimiento entre almacenes** para mover los artículos desde el hueco de almacenamiento de los artículos al hueco de almacenamiento de salida. En este caso, debe definirse un hueco de almacenamiento del almacén como **Salida**.

        - Indicador Generar albarán al completar la LP: si está marcado, Etendo genera **Albarán (Cliente)** si la lista de picking se completa. Debe seleccionarse un tipo de documento de **Albarán (Cliente)** en el campo **Albarán para picking**.

    3. **Lista de picking agrupada**: Al usar ubicación de salida y con el indicador **Es lista de picking agrupada** marcado. Este tipo de documento se utiliza al agrupar diferentes listas de picking en una sola lista.

    !!! note
        Estos tipos de documento pueden modificarse o pueden crearse otros nuevos manualmente. Por ejemplo, si no se desea generar el **Albarán (Cliente)** cuando se completan o si se desea modificar el formato de las secuencias de documento.


- **Ubicación de salida del almacén**: Al utilizar **Lista de picking de salida**, es necesario configurar las **ubicaciones de salida en cada almacén** que envía artículos a clientes. En la ventana **Almacén y huecos**, seleccione el almacén y, en la pestaña Hueco de almacenamiento, cree o seleccione el hueco de almacenamiento que represente la ubicación de salida de ese almacén. Rellene el campo tipo seleccionando **Salida**.

    ![picking4](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/picking/picking4.png)

- **Preferencia de cierre automático de la lista de picking**: Al utilizar **Lista de picking de salida**, para establecer automáticamente el estado de la lista de picking de Todo confirmado a Cerrada, está disponible una preferencia `Picking List Auto Close` con valor predeterminado N. Los usuarios pueden habilitar esta preferencia para cerrar automáticamente el picking cuando todas las líneas estén confirmadas.

- **Preferencia de reserva**: Debe configurar una preferencia para habilitar la funcionalidad de reserva de existencias (si el bundle *Warehouse Extensions* está instalado, esta preferencia viene preconfigurada de forma predeterminada; solo necesita realizar este paso si instala el módulo de forma independiente).

    Como Administrador de cliente, vaya a la [ventana Preferencia](../../../basic-features/general-setup/application/preference.md) y cree una nueva como se muestra a continuación:

    ![picking2](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/picking/picking2.png)
## Generación de la lista de picking

Las **listas de picking** se pueden generar mediante el **botón Generar lista de picking** disponible en la ventana [Pedido de venta](../../../basic-features/sales-management/transactions.md#sales-order) y/o crearse manualmente desde la ventana **Lista de picking de almacén**. En ambos casos, el usuario debe seleccionar los pedidos de venta que se incluirán en la lista de picking. El pedido de venta debe estar **reservado y pendiente de envío**, es decir, el estado de entrega debe ser inferior al 100%.

!!! info "Integración de Advanced Warehouse Management"
    Cuando se instala el módulo [Advanced Warehouse Management](advanced-warehouse-management.md), el proceso de picking se puede gestionar mediante tareas, ofreciendo un mayor control y trazabilidad. El sistema ejecuta procesos automáticos en segundo plano que crean y gestionan tareas de picking, y muestra mensajes de advertencia en distintas etapas con enlaces a la ventana de Tareas, donde los usuarios pueden revisar los registros del proceso y los detalles de ejecución.
    
    Esta integración permite:
    
    - Gestión completa del proceso de picking desde el ERP y dispositivos móviles
    - Creación automática de tareas para operaciones de picking y empaquetado
    - Monitorización del proceso en tiempo real y verificación de logs
    - Mayor trazabilidad y control sobre las operaciones de almacén
    
    Para más información sobre el proceso de picking con tareas y la integración con dispositivos móviles, visite [Advanced Warehouse Management](advanced-warehouse-management.md#picking-tasks).

=== ":material-playlist-check: Desde la ventana Pedido de venta"

    ### Desde la ventana Pedido de venta
    :material-menu: `Aplicación` > `Gestión de Ventas` > `Transacciones` > `Pedido de venta`

    Desde la ventana [Pedido de venta](../../../basic-features/sales-management/transactions.md#sales-order), el botón Generar lista de picking admite selección múltiple y es visible cuando todos los pedidos seleccionados están reservados y no se han enviado completamente. Mediante este proceso **se pueden crear ambos tipos de listas de picking**: listas de picking directas y listas de picking de salida.

    Al instalar este módulo, en la cabecera del pedido de venta se añade el indicador **Lista de picking pendiente**. Este se marca cuando una de las líneas del pedido de venta está presente en una lista de picking que no está cerrada. Usando este indicador y los campos Estado de entrega y Fecha de entrega, es posible filtrar la ventana Pedido de venta para identificar los pedidos de venta que deben incluirse en una lista de picking.

    La cabecera del pedido de venta también incluye el indicador **Excluir de la lista de picking**. Si este indicador se establece en Sí, el botón Generar lista de picking no se mostrará para ese pedido.

    !!!info
        El módulo no admite la creación de listas de picking para el mismo pedido de venta para **múltiples almacenes**. Dado que el pedido de venta ya tiene un almacén asignado en la cabecera, la lista de picking se creará únicamente para ese almacén.

    !!!note
        Cuando una línea de pedido de venta se incluye en una lista de picking, debe tener una reserva relacionada. Las existencias reservadas son las que se utilizan en la lista de picking. Los procesos que generan las listas de picking crean automáticamente las reservas si la línea del pedido de venta no tiene una.

    #### Botones

    - **Generar lista de picking**

        Permite generar el documento de selección para el proceso de picking. Este documento contiene la información del pedido de venta y sirve como base para organizar la preparación de la mercancía.

        La generación de este documento es un paso clave en el flujo logístico, ya que reúne en un único lugar toda la información necesaria para recoger los artículos del almacén. Esto permite al usuario gestionar las tareas de picking de forma más ordenada y asegurar que cada pedido se procese correctamente.
        
        Al hacer clic en el botón, se abre una ventana emergente. El primer campo que debe completarse es el tipo de lista de picking. En función del tipo seleccionado, será necesario configurar campos adicionales.

        ![picking.6](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/picking/picking6.png)

        ===  "**Lista de picking directa al cliente**"
            
            Significa que los productos se recogen **directamente de las ubicaciones de almacenamiento** (p. ej., estanterías o huecos) y se **preparan para el envío** al cliente sin moverlos a una ubicación intermedia específica dentro del almacén. Al seleccionarlo, el proceso genera un **Albarán (Cliente)** en **estado Borrador** para cada pedido de venta seleccionado. Las listas de picking también se generan en estado Borrador usando un tipo de documento que tiene desmarcado el indicador Usar ubicación de salida.

            Las listas de picking generadas se pueden agrupar usando el campo Criterio de agrupación en la ventana del proceso Generar lista de picking. 

            Las opciones disponibles son:

            - **No agrupar** (opción por defecto): se genera una lista de picking por cada pedido de venta seleccionado.

            - **Agrupar por tercero**: las listas de picking se agrupan por el tercero y la organización del pedido de venta. Se crea una lista de picking por cada cliente y organización.

            - **Agrupar por organización**: las listas de picking se agrupan por la organización del pedido de venta. Se crea una lista de picking por cada organización.
                
            ---

            El criterio de agrupación por defecto se puede configurar mediante una preferencia:
            
            - Nombre de la preferencia: `Group Picking List`
            - Valores posibles:
                - No agrupar: NG
                - Agrupar por tercero: GBP
                - Agrupar por organización: GO
            
            ---
        
            !!!warning
                Si no hay existencias para al menos uno de los productos, se muestra un mensaje indicando que se ha creado una lista de picking parcial. La reserva, la lista de picking y el albarán se crean con las existencias disponibles.

            !!!warning
                Si ninguno de los productos tiene existencias, no se crea ninguna lista de picking, ningún albarán ni ninguna reserva. Además, se muestra un mensaje de error.


            Cuando la lista de picking se genera desde un pedido de venta, se crea automáticamente un [Albarán (Cliente)](../../../basic-features/sales-management/transactions.md#goods-shipment) en **estado borrador**. A continuación, el operario de almacén recoge los productos de las ubicaciones indicadas en la lista de picking.
            
            Una vez que se verifica que los productos son correctos (usando el botón Validar o un lector de códigos de barras) desde la ventana **Lista de picking de almacén**, se procesa la lista de picking y se completa el albarán, lo que significa que los productos están listos para salir del almacén hacia el cliente.

        === "**Lista de picking de salida**"
            Significa que los productos se recogen de los huecos de almacenamiento, pero en lugar de llevarlos directamente al área de empaquetado/envío, se trasladan a un **hueco de salida predefinido** en el almacén. Desde esta ubicación, los productos se empaquetan y se envían.

            !!! info
                Al generar la lista de picking de salida desde un pedido de venta o manualmente, se crean **Movimiento entre almacenes** en estado borrador para mover los productos desde las ubicaciones de almacenamiento hasta la ubicación de salida.
                En esta ventana, el botón Procesar movimiento finaliza el proceso.

            ![picking10](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/picking/picking10.png)

            El operario de almacén recoge los productos y los lleva a la ubicación de expedición designada (p. ej., un área específica del almacén para productos listos para el envío).


=== ":material-playlist-plus: Desde la ventana Lista de picking de almacén"

    ### Desde la ventana Lista de picking de almacén
    :material-menu: `Aplicación` > `Gestión de Almacén` > `Transacciones` > `Lista de picking de almacén`

    Desde la ventana **Lista de picking de almacén**, solo es posible **crear listas de picking de salida**, pero no es posible crear manualmente **listas de picking directas**. Este último tipo de lista se genera desde la ventana Pedido de venta y el proceso puede finalizarse desde la ventana Lista de picking de almacén. 

    === "**Lista de picking de salida**"
        
        #### Lista de picking de salida

        ![picking5](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/picking/picking5.png) 
        
        ##### Cabecera
        
        Desde la cabecera, es posible crear una lista de picking de salida: 
        
        Campos a tener en cuenta: 

        - **Organización**: una organización es una unidad de su cliente o entidad legal.
        - **Nº de documento**: el número de identificación del picking se genera automáticamente.
        - **Tipo de documento**: determina la secuencia del documento y las reglas de procesamiento.
        - **Hueco de almacenamiento de salida**: es necesario configurar un hueco de almacenamiento de salida en cada almacén que expida. Este hueco se define en la ventana **Almacén y huecos** seleccionando un hueco con el tipo **Salida**.
        - **Fecha del documento**: fecha en la que se realiza la lista de picking y se espera que se complete.
        - **Descripción**: una descripción opcional limitada a 255 caracteres.
        - **F.impresión**: indica la fecha en la que se imprimió un documento. 
        - **Usuario/Contacto**: el usuario identifica un usuario único en el sistema. Puede ser un usuario interno o un contacto de tercero. 


        !!! info
            Cuando se genera una lista de picking de salida, se crean Movimiento entre almacenes en estado borrador para mover los productos desde los huecos de almacenamiento al hueco de salida.

        !!! info
            Los productos incluidos en la lista de picking de salida se reservan automáticamente, garantizando que no puedan ser utilizados por otros procesos o listas de picking.

        ##### Botones

        - **Pedido de venta**
            El botón Pedidos de venta abre una ventana con una rejilla que contiene todos los pedidos de venta pendientes de entrega que **no están en una lista de picking abierta**. 
            Los pedidos de venta que se muestran se filtran por el almacén del hueco de salida definido en la cabecera de la lista de picking.
            Puede ocurrir que un pedido de venta tenga artículos reservados en un almacén **distinto del almacén definido en su cabecera** (debido a la definición de “cantidad disponible” por organización y prioridades). En ese caso, la lista de picking intentará reasignar artículos desde ese almacén al almacén del hueco de salida. Si no hay forma de realizar esta acción, el sistema mostrará un error.

            !!!note
                El sistema asume que los huecos de picking y el hueco de salida deben pertenecer al **mismo almacén**. Por eso el sistema siempre intenta reasignar artículos en el escenario anterior y también filtra los pedidos de venta en función del almacén del hueco de salida.

        - **Asignar**
            Este botón asigna la lista de picking seleccionada al **operario de almacén** elegido en la ventana emergente.

        - **Reasignar**
            Este botón permite al usuario **cambiar el operario asignado** a una lista de picking por uno nuevo. Solo cuando el estado del documento es Asignado.

        ##### Pestaña Línea de movimiento

        La pestaña **Línea de movimiento** se muestra cuando se incluyen **listas de picking de salida**. Incluye todos los Movimiento entre almacenes relacionados con la lista de picking. 

        ![picking8](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/picking/picking8.png)

        Campos a tener en cuenta:

        - **Reserva de existencias**: la reserva relacionada con el movimiento, que enlaza con la línea del pedido de venta.
        - **Motivo de incidencia**: en caso de que la línea esté en estado Incidencia, puede mostrar una descripción de la incidencia.
        - **Group Picking List** y **Lista de picking de almacén**: en caso de que una lista de picking esté agrupada, muestra el enlace a la lista de picking original o a la lista de picking agrupadora.

        ###### Botones de la pestaña Línea de movimiento

        - **Editar artículo**

            Edita las líneas para cambiar los atributos del producto a recoger. Es posible seleccionar **distintos atributos y huecos de almacenamiento**. La cantidad total debe ser igual o inferior a la cantidad de movimiento de la **Reserva de existencias** relacionada. El proceso actualiza las existencias reservadas y los movimientos entre almacenes, eliminando o creando nuevos si es necesario.

            ![picking9](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/picking/picking9.png)

        - **Gestionar incidencia**

            En caso de que haya un problema con la línea, se puede registrar una incidencia. Cuando se registra la incidencia, es posible establecer una descripción del problema. Cuando una línea está en **estado Incidencia**, el estado del documento cambia a **Incidencia**. Cuando la línea ya está en estado Incidencia y la incidencia se ha resuelto, al pulsar el botón de nuevo se cambia el estado de la línea a **Pendiente**. Entonces, el estado del documento también se restablece al valor correspondiente en función del estado de todas las líneas.

            ![picking11](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/picking/picking11.png)

        - **Confirmar**: 
        
            Este botón establece la línea en estado Confirmada. Actualiza el estado de la lista de picking:
            - Si hay una línea en estado Incidencia, el estado se mantiene en `Incidence`.
            - Si todas las líneas están en estado Confirmada, se establece el estado `All Confirmed`.
            - En cualquier otro caso, se establece `In Progress`.

        - **Rechazar** 
        
            Este botón establece la línea en estado Pendiente. Esto es necesario en caso de que el operario de almacén quiera cambiar algo de la línea. Para ello, es necesario hacer clic en el botón Editar: 
        
            Actualiza el estado de la lista de picking:
            - Si hay una línea en estado Incidencia, el estado se mantiene en Incidencia.
            - En cualquier otro caso, se establece In Progress.

        - **Cerrar**
        
            Este botón completa todos los movimientos entre almacenes de la lista de picking que están en **estado confirmada** y actualiza el estado de la lista de picking a **Hecho**. En caso de que el tipo de documento de la lista de picking tenga habilitado el indicador Generar albarán, se crean los albaranes necesarios en estado Borrador.

            ![picking12](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/picking/picking12.png)


    ===  "**Lista de picking directa al cliente**"

        #### Lista de picking directa al cliente
        Aunque la **lista de picking directa** se genera desde la ventana Pedido de venta, desde esta ventana se pueden mostrar y realizar varias acciones:

        ##### Botones

        - **Proceso**

            El botón Proceso procesa la **lista de picking** seleccionada y su **Albarán (Cliente)** asociado. 

        - **Cancelar**

            Se eliminan el albarán asociado y la cabecera de la lista de picking. **Excepto las líneas que estén en un albarán que esté procesado**. Esas líneas, su albarán procesado y la cabecera de la lista de picking no se eliminan. En ese caso, el estado de la lista de picking se establece como Cancelada.

        - **Validar**

            Cuando el operario de almacén ha recogido todos los artículos, el responsable puede verificarlos usando este proceso.

            ![picking7](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/picking/picking7.png)

            El botón abre una ventana que muestra todos los artículos; para cada uno debe establecerse el campo Cantidad verificada. Hay varias formas de hacerlo:

            - Usando un lector escáner de códigos de barras. Si existe un producto con ese código de barras en la rejilla, incrementa la cantidad en 1 unidad.
            - Cambiando manualmente la cantidad en la línea.
            - Introduciendo el código de barras y pulsando Validar código de barras. Si existe un producto con ese código de barras, incrementa la Cantidad verificada en la cantidad establecida en el campo Cantidad.

            !!! info
                Cuando la Cantidad verificada es la Cantidad, la Cantidad pendiente es cero y la línea se marca como verificada (color verde). Cuando todas las líneas están verificadas, la lista de picking puede procesarse. También procesa los albaranes relacionados.
## Ventana Pedido de venta para picking

La ventana Pedido de venta para picking permite **filtrar entre todos los pedidos de venta** que están en el sistema y que están listos para el picking.

Los pedidos de venta deben estar **Completada** y tener la casilla **Excluir de la lista de picking** desmarcada.

Cuando se crean los pedidos de venta, el estado de reserva es **No reservado**.

![picking3](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/picking/picking3.png)

!!!info
    Una vez completado el proceso de picking, el usuario puede continuar con el proceso de embalaje.
    
    Para más información, visite: [Embalaje](packing.md).


---

Este trabajo es una obra derivada de [Gestión de Almacén](http://wiki.openbravo.com/wiki/Warehouse_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.