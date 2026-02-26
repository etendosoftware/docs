---
title: Empaquetado
tags: 
    - Empaquetado
    - Albarán (Cliente)
    - Empaquetar
    - Albaranes
    - Calcular peso

---

# Empaquetado


:octicons-package-16: Javapackage: `org.openbravo.warehouse.packing`

## Visión general

Esta sección describe el módulo **Etendo Packing** incluido en el bundle *Warehouse Extensions*.

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Warehouse Extensions Bundle. Para ello, siga las instrucciones del marketplace: [_Warehouse Extensions Bundle_](https://marketplace.etendo.cloud/?#/product-details?module=BAE67A5B5BC4496D9B1CA002BBCDC80E){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Warehouse Extensions - Notas de la versión](../../../../../whats-new/release-notes/etendo-classic/bundles/warehouse-extensions/release-notes.md).

Este módulo agiliza y mejora la gestión de las **operaciones de empaquetado** dentro del almacén. Una vez que se ha procesado un **albarán**, comienza el proceso de empaquetado. El empaquetado se realiza en base a cada documento individual de albarán. Para cada producto, el operario de almacén determina la unidad de manipulación adecuada (caja) en la que empaquetar el artículo. Solo los productos clasificados como **artículos** son aptos para el empaquetado.

!!! warning
    Este módulo incluye documentación sobre cómo realizar el proceso de **Empaquetado** desde Etendo. Para más información sobre la configuración y la gestión de tareas de empaquetado desde **Etendo Mobile**, consulte la documentación del módulo: [Advanced Warehouse Management - Packing](./advanced-warehouse-management.md#packing).


## Configuración inicial

En Etendo, es posible calcular el **peso del empaquetado**. Para ello, se requieren algunas configuraciones previas en otras ventanas para poder calcular el peso de cada caja:

- Ventana [**Producto**](../../../basic-features/master-data-management/master-data.md#product): aquí es posible definir el peso y la unidad de medida (UdM) del producto.

    ![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/packing/packing-10.png)
    
    - Campos a tener en cuenta:
        - Peso
        - Unidad para peso: solo muestra unidades de medida que estén definidas como `Is weight`

- Ventana [**Unidad de medida**](../../../basic-features/master-data-management/product-setup.md#unit-of-measure): este módulo añade un nuevo campo **Is weight**. En esta ventana también es posible definir la **Conversión** entre UdM, es decir, entre la UdM del producto y la UdM de la caja.

    ![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/packing/packing-11.png)

- Ventana [**Organización**](../../../basic-features/general-setup/enterprise-model/organization.md): este módulo añade un nuevo campo **UOM Packing**. Esta UdM es la predeterminada para cada *caja*. Esto es necesario para realizar la conversión entre la UdM de empaquetado del Producto y la UdM de empaquetado de la caja.

    ![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/packing/packing-12.png)


## Ventana de empaquetado

:material-menu: `Aplicación` > `Gestión de Almacén` > `Transacciones` > `Packing`

El proceso de empaquetado puede iniciarse desde la ventana **Empaquetado** y/o desde la ventana [Albarán (Cliente)](../../../basic-features/sales-management/transactions.md#goods-shipment). Desde cualquiera de las dos ventanas, el procedimiento de empaquetado será el mismo, así como la información de empaquetado mostrada a través de la solapa `Packing Box` y la solapa Contenido, que se visualizan en ambas ventanas.

!!! info
    Si el proceso se inicia desde la ventana Albarán (Cliente), es posible realizar el empaquetado únicamente para **un envío específico**. Al realizar el empaquetado desde la ventana Empaquetado, es posible seleccionar **más de un envío para empaquetar**, ya que varios documentos se agrupan para empaquetarse todos a la vez o de forma individual. 

El sistema ejecuta procesos automáticos en segundo plano que varían en función de la configuración. En determinadas situaciones, algunos de estos procesos pueden fallar sin que el usuario lo advierta inmediatamente.

Para proporcionar una mayor visibilidad, el sistema muestra un **mensaje de advertencia** en diferentes etapas del proceso, como al crear un empaquetado, completarlo o reactivarlo, que incluye un enlace a la ventana de Tareas. Desde allí, el usuario puede comprobar los detalles de cada proceso ejecutado y revisar los logs correspondientes, garantizando un mejor control sobre la correcta finalización de las operaciones.

- Para **tareas de empaquetado**:

    - Process Packing
    - Process Packing Header
    - Complete Packing from Shipment
    - Complete Packing from Packing

### Cabecera

![packing9](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/packing/packing-9.png)

Campos a tener en cuenta: 

- **Organización**: una organización es una unidad de su cliente o entidad legal.
- **Document No**: el número de identificación del empaquetado se genera automáticamente.
- **Fecha**: la fecha de creación del empaquetado. 
- **Terceros**: se seleccionará el cliente para el que se está realizando el empaquetado.
- **Dirección**: la dirección indica la ubicación de un tercero.
- **Descripción**: una descripción opcional limitada a 255 caracteres.

!!! info
    En caso de que el proceso se inicie desde la ventana Albarán (Cliente), el documento debe tener el estado **Completada**, y el campo **Packing Required** debe estar seleccionado. Una vez cumplidas estas condiciones, el botón **Empaquetar** pasa a estar disponible, permitiendo al usuario proceder con el empaquetado de los productos.

    ![packing1](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/packing/packing-1.png)

    Tanto si el proceso se inicia desde la ventana Albarán (Cliente) como desde la ventana Empaquetado, se crea un registro en la **ventana de empaquetado**. Por tanto, esta es una ventana centralizada donde es posible consultar todos los empaquetados realizados y completar el proceso de empaquetado. 


### Solapa Packing Box

La solapa **Packing Box** del Albarán (Cliente) y de la ventana Empaquetado es una solapa **informativa** que muestra las nuevas cajas de empaquetado.

![packing2](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/packing/packing-2.png)

Campos a tener en cuenta:

- **Box Number**: el número de caja del albarán
- **Peso**: indica el peso de la caja
- **Unidad**: la unidad de medida del peso de la caja
- **Número de envío**: número para realizar el seguimiento del envío
- **Weight Calculated**: estado que determina si el peso ya ha sido calculado o no.


### Subsolapa Contenido
En la solapa Packing Box, la solapa **Contenido** es una solapa hija donde se muestra el **contenido de la caja**.

![packing3](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/packing/packing-3.png)

Campos a tener en cuenta:

- **Producto**: identifica un artículo que se compra o se vende en esta organización.
- **Valor atributos**: muestra los atributos del producto cuando aplica, como lote, número de serie o fecha de caducidad.
- **Cantidad Operativa**: cantidad introducida en la unidad de medida alternativa del producto.
- **Unidad Alternativa**: unidad de medida alternativa utilizada para introducir la cantidad operativa (por ejemplo, caja o palé).
- **Cantidad**: indica la cantidad de producto en la caja
- **Unidad**: la unidad define una unidad de medida única no monetaria


### Botones

- **Pick Shipments**
    
    Este botón **solo se muestra** en la ventana Empaquetado, ya que permite seleccionar **todos los albaranes disponibles** que necesitan ser empaquetados.

    ![packing8](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/packing/packing-8.png)

    El criterio para mostrar qué albaranes pueden seleccionarse es el siguiente:

    - Albaranes que pertenecen al tercero definido en la cabecera y en la misma dirección.
    - Albaranes que están marcados como Packing Required.
    - Albaranes que no han sido empaquetados.

    Tras seleccionar los albaranes deseados, el proceso continúa desde el botón Empaquetar

- **Empaquetar**

    !!! info
        
        - Si el usuario inicia el proceso desde la ventana **Albarán (Cliente)**, este botón pasa a estar disponible una vez que el documento está en estado **Completada** y el campo **Packing Required** está marcado.
        - Si el proceso se inicia desde la ventana **Empaquetado**, este botón es visible una vez que el albarán está creado y en estado Completada, permitiendo al usuario proceder con el empaquetado de los productos.

    Al pulsar el botón Empaquetar:

    ![packing4](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/packing/packing-4.png)

    Se abre un pop-up que muestra todos los productos con sus cantidades. 
    
    1. El usuario debe **introducir la cantidad** para cada producto en cada caja.
    
        Existen tres formas diferentes de introducir la cantidad:

        - Usando un **lector de códigos de barras**: si existe un producto con código de barras, se actualiza la cantidad en la caja correspondiente. Usar el lector de códigos de barras será útil en caso de empaquetar muchos productos. 
        - Introduciendo manualmente la **cantidad en la caja**: la introducción manual es útil cuando solo se van a empaquetar unos pocos productos; cuando hay muchos productos, se recomienda usar el lector de códigos de barras. 
        - Introduciendo el **número de código de barras** y pulsando **Validar código de barras**. Si existe un producto con ese código de barras, se actualizan las cantidades en la caja correspondiente.

        !!! note
            Cuando la suma de las cantidades de todas las cajas es igual a la Cantidad del producto, entonces se marca como validado (color verde). El empaquetado será posible una vez que todos los productos estén validados.

    2. Si es necesario, se pueden añadir cajas con el botón **Añadir caja**.

        ![packing7](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/packing/packing-7.png)

        !!! info
            Después de añadir el albarán, y de haberse realizado la acción de empaquetado, si el usuario elimina alguno de los albaranes que se van a empaquetar, entonces se eliminan todas las cajas y el empaquetado debe iniciarse de nuevo. 

    3. El indicador **Calcular peso** permite calcular (o no) el peso de cada una de las cajas. Esto es configurable y el indicador puede estar marcado por defecto o no mediante la [preferencia](../../../basic-features/general-setup/application/preference.md) `Calculate Weight Packing`.
    
        !!!warning

            En caso de que falte algo en la configuración, el proceso de empaquetado continúa, pero se muestra una advertencia indicando que el peso no se ha podido calcular correctamente. 
            
            ![packing5](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/packing/packing-5.png)

            Si se muestra el mensaje anterior, la UdM debe estar configurada tanto en la Organización como en cada producto. Incluso si cada producto tiene una UdM configurada, al empaquetar se tomará la UdM definida en la Organización y se realizarán las conversiones correspondientes si fuese necesario.

    4. Una vez que todos los productos han sido validados en sus cajas correspondientes, el proceso se completa haciendo clic en el botón **Empaquetar**.


- **Completar empaquetado**

    Una vez creadas todas las cajas y su contenido, pulse el botón Completar empaquetado. La información de las cajas, como el peso, la unidad y el Número de envío, no se puede editar. Este botón **completa** todas las cajas a la vez. Este botón está presente tanto en la ventana **Albarán (Cliente)** como en la ventana **Empaquetado**. 

- **Reactivar empaquetado**
    
    Una vez que todo se ha completado, el botón Reactivar empaquetado permite al usuario **reactivar** el empaquetado y **editar** la información que sea necesaria. Este botón también está presente tanto en la ventana **Albarán (Cliente)** como en la ventana **Empaquetado**. 

    ![packing6](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/packing/packing-6.png)


---

Este trabajo es una obra derivada de [Gestión de Almacén](http://wiki.openbravo.com/wiki/Warehouse_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.

---