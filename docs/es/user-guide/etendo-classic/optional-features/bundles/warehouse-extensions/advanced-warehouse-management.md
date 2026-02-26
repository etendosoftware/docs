---
title: Gestión Avanzada de Almacén
tags:
    - Gestión de Almacén
    - Avanzado
    - Recepción
    - Inventario
    - Stock
    - Etendo Mobile
---

# Gestión Avanzada de Almacén
:octicons-package-16: Javapackage: `com.etendoerp.advanced.warehouse.management`

## Visión general

El módulo **Gestión Avanzada de Almacén** amplía las capacidades estándar de Etendo para ofrecer una gestión de inventario completa, flexible y automatizada, añadiendo integración con dispositivos móviles. Cada acción realizada desde Etendo Mobile se sincroniza automáticamente con Etendo, garantizando una trazabilidad completa y actualizaciones consistentes en las ventanas correspondientes del sistema.

Este módulo permite al usuario:

- Gestionar el inventario en múltiples estados predefinidos y personalizados.
- Realizar ajustes de stock e inventarios físicos desde dispositivos móviles.
- Automatizar reubicaciones y estados mediante reglas de movimiento.
- Integrar la trazabilidad usando códigos de barras, que pueden escanearse desde Etendo Mobile.
- Ampliar y optimizar el proceso manual de picking y packing, incorporando la posibilidad de ejecutarlos desde Etendo Mobile.

## Configuración inicial

Para empezar a utilizar este módulo correctamente, deben completarse los siguientes pasos de instalación y configuración:

- [x] Instalar el bundle **Warehouse Extensions**.
- [x] Instalar la app **Etendo Mobile**.
- [x] Habilitar la **Advanced Warehouse App** en los roles de usuario que la utilicen.
- [x] Instalar datasets.
- [x] Configurar los parámetros clave en la ventana **Advanced Warehouse Configuration**.
- [x] Deben crearse los tipos de tarea necesarios para picking y packing.
- [x] Debe definirse la opción de generación de picking a nivel de pedido de venta.

**Pasos a seguir:**

1. Instalar el módulo **Gestión Avanzada de Almacén**, parte de **Warehouse Extensions Bundle**.
    
    !!! info
        Para poder incluir esta funcionalidad, debe instalarse el Warehouse Extensions Bundle. Para ello, sigue las instrucciones del marketplace: [_Warehouse Extensions Bundle_](https://marketplace.etendo.cloud/?#/product-details?module=BAE67A5B5BC4496D9B1CA002BBCDC80E){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visita [Warehouse Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/warehouse-extensions/release-notes.md).

2. Instalar **Etendo Mobile** en un dispositivo Android o iOS y seguir los pasos de configuración inicial. Para ello, sigue las instrucciones en [Getting Started - Etendo Mobile](../../../../etendo-mobile/getting-started.md)

    !!! tip
        Asegúrate de seguir todos los pasos para habilitar la **Advanced Warehouse App**.

3. Instalar datasets

    :material-menu: `Aplicación`>`Configuración General` > `Organización` > `Gestión del módulo de Empresa`
    
    Desde la ventana [Gestión del módulo de Empresa](../../../basic-features/general-setup/enterprise-model/enterprise-module-management.md) es requerido para todos los roles que vayan a utilizar esta funcionalidad.

    Estos datos de referencia incluyen configuraciones necesarias para usar estos módulos. 

    - `Warehouse Packing`
    - `Warehouse Picking List`
    - `Advanced Warehouse Management`
    - `Etendo Print Provider`
    - `Stock Logistic Unit`

    ![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/dataset.png)

4. Ventana **Advanced Warehouse Configuration**

    :material-menu:`Aplicación` > `Gestión de Almacén` > `Configuración` > `Advanced Warehouse Configuration`

    Antes de utilizar el módulo, en la ventana `Advanced Warehouse Configuration`, debes configurar las variables clave que definen cómo se gestionan las operaciones de inventario para cada organización.

    !!! warning
        Es obligatorio crear una configuración para la organización con la que estás trabajando.

    ![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/advanced-warehouse-configuration.png)
    
    Campos a tener en cuenta:

    **Header**

    - **Organización**: permite gestionar a qué organización se aplicará la configuración.
    - **Almacén**: es un campo no obligatorio que puede utilizarse para aplicar la configuración a un almacén específico o a todos los almacenes de la organización.
    - **Activo**: se marca o desmarca para habilitar o deshabilitar la configuración.
    - **Barcode Configuration**

        - **Barcode Algorithm**: el algoritmo de código de barras por defecto que permite la interpretación según cualquiera de los estándares definidos por organizaciones internacionales. Las opciones a seleccionar son:

            - [GS1-128](https://www.gs1.org/standards/barcodes){target="_blank"}
            - SimpleBarcode

        - **Barcode Components Configuration**: conjunto de identificadores de aplicación definidos por estándares de la industria y utilizados en códigos de barras. Estos identificadores permiten al sistema distinguir diferentes tipos de información, ya que cada AI especifica el tipo de dato que le sigue, como identificadores de producto, números de lote, fechas de caducidad o cantidades.  
        Este campo es obligatorio cuando se selecciona uno de los algoritmos por defecto del módulo (GS1-128 o Simple Barcode). Para algoritmos personalizados definidos por el usuario, este campo puede dejarse en blanco; sin embargo, el sistema mostrará un mensaje de advertencia si permanece vacío. En todos los casos, la configuración de AI es editable.

    Pestaña **Preference**

    Esta pestaña permite crear, editar y eliminar registros de preferencia. Los registros heredan automáticamente el Cliente y la Organización de la cabecera, y estos campos no son editables. Los campos de la pestaña replican los disponibles actualmente en la ventana `Configuración General` > `Aplicación` > `Preferencia`.

    Opciones como **Search Related Barcode**, **Picking – Exact Attribute Validation**, y las preferencias para **Enable Stock Reservations** y **Enable UOM Management** pueden gestionarse como preferencias directamente desde esta pestaña.

    **Tabla de preferencias**

    La siguiente tabla resume las preferencias clave disponibles en la configuración avanzada de almacén:

    | Preference Name | Descripción | Opciones | Valor por defecto |
    |-----------------|-------------|---------|-------------------|
    | **Picking – Exact Attribute Validation** | Define el nivel de validación aplicado durante el proceso de picking. | **Y**: Requiere coincidencia exacta entre el código escaneado y la Picking List (producto, atributos y hueco).<br>**N**: Valida solo el producto, sin coincidencia estricta de atributos o hueco. | *Y* |
    | **Search Related Barcode** | Permite a Etendo buscar un producto usando múltiples códigos de barras. | **N**: Busca solo el código de barras principal en el campo **UPC/EAN** del producto.<br>**Y**: Busca tanto el código de barras principal como todos los códigos de barras adicionales en la pestaña **Barcode**. | *N* |
    | **Enable Stock Reservations** | Habilita o deshabilita la funcionalidad de reserva de stock. | **Y**: Activa las reservas de stock.<br>**N**: Desactiva las reservas de stock. | *N* |
    | **Enable UOM Management** | Habilita o deshabilita la gestión de unidades de medida alternativas. | **Y**: Activa la funcionalidad AUOM.<br>**N**: Desactiva la funcionalidad AUOM. | *N* |
    | **Create Warehouse Tasks** | Habilita la generación automática de tareas de almacén (p. ej., tareas de picking) durante la creación de la Picking List. Cuando está deshabilitado, las tareas no se generan automáticamente y la asignación no está disponible. | **Y**: Genera automáticamente tareas de almacén.<br>**N**: No genera tareas automáticamente. | *Y* |
    | **Task From Date Completed Days** | Define cuántos días hacia atrás desde la fecha actual muestra Etendo Mobile las tareas con estado Completado. | Valor numérico que representa el número de días. | *1* |



5. Ventana **Barcode Components Configuration**
    
    :material-menu:`Aplicación` > `Gestión de Almacén` > `Configuración` > `Barcode Components Configuration`

    Esta ventana forma parte de la **advanced barcode settings** del sistema Etendo y se utiliza para gestionar y configurar diferentes tipos de códigos de barras. Permite al sistema leer y asociar los códigos escaneados con productos y su información relevante.

    Permite a los usuarios definir, configurar y aplicar sus propios identificadores para que el sistema pueda leer y asociar diferentes **atributos de producto**, como color, tipo de embalaje, lote o cualquier otro dato relevante, directamente desde los códigos **GS1-128** utilizados en operaciones logísticas.

    !!! tip 
        Las configuraciones mostradas a continuación están predefinidas en el dataset inicial, aunque pueden modificarse o añadirse nuevos esquemas o tipos de código de barras.
    
    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/barcode-components-configuration-win-1.png)

    !!! note

        El sistema permite configurar libremente cualquier **application identifier (AI)** para asociarlo a atributos o campos personalizados, proporcionando flexibilidad para adaptarse a distintos esquemas internos de codificación. El módulo se instala con una configuración predefinida basada en el estándar **GS1-128**, lo que asegura la correcta interpretación de los códigos conforme a estándares internacionales. No obstante, los usuarios pueden ajustar o redefinir los identificadores según sus necesidades particulares. En esos casos, el sistema interpretará los códigos según la configuración definida por el usuario, pero no interpretará los códigos GS1-128 de forma estándar.

    Campos a tener en cuenta:

    **Header**

    - **Nombre**: nombre descriptivo de la configuración de código de barras para identificarla fácilmente.  
    - **Descripción**: detalles adicionales sobre el propósito o alcance de esta configuración.  
    - **Separator**: carácter utilizado para delimitar campos de longitud variable en el código, normalmente **FNC1**.  
    - **Apply To All Separators**: casilla de verificación. Si está marcada (Sí), el separador configurado se añade al final de cada identificador — tanto los AI de longitud fija como los de longitud variable deben terminar con el separador. Si está desmarcada (No), el separador se aplica solo a los identificadores de longitud variable.
    
    Pestaña **Barcode Component Lines**

    - **AI**: código de Application Identifier definido por GS1 (p. ej., 01 para GTIN, 17 para fecha de caducidad).
    - **Descripción**: explicación de la información que representa el AI (p. ej., identificador de producto, número de lote).
    - **Fixed Length**: indica si la longitud del dato es siempre fija según el *estándar GS1* para ese AI.
   - **Length**: (Obligatorio) número esperado de caracteres para AI de longitud fija, o longitud máxima para AI de longitud variable.
    - **Priority**: define el orden de lectura cuando hay múltiples identificadores, asegurando que el sistema interprete el código de barras correctamente.  
    - **Entity**: selector de tipo de entidad. Las opciones son: **Attribute, Locator, Order Line, Physical Inventory Line, Product, Reference Inventory, Shipping/Receiving Line**. 
        
        Si se selecciona **Product**, se habilitan opciones rápidas por defecto mediante casillas para definir *Lote*, *Número de serie* o *F. caducidad*. Además, puede definirse un valor desde *Entity Field*, que lista los distintos atributos disponibles para el producto. Cada una de estas opciones es única y no puede combinarse con las demás.

        - **Entity Field**: selector de campos disponibles para la entidad seleccionada para asignar el valor del código de barras. Las opciones dependen de lo introducido en Entity.
        - **Lote**: marcar para indicar que el atributo es de tipo lote.
        - **Serial No.**: marcar para indicar que el atributo es de tipo número de serie. 
        - **F. caducidad**: marcar para indicar que el atributo es de tipo fecha de caducidad.

    Por defecto, al instalar el dataset, el módulo **incluye dos métodos principales para el reconocimiento de códigos**:

    === ":material-playlist-plus: GS1-128"
        
        El estándar [GS1-128](https://www.gs1.org/standards/barcodes){target="_blank"} es un formato de código de barras usado globalmente que codifica información estructurada mediante **Application Identifiers (AIs)**. Cada AI especifica el tipo de dato incluido, como identificadores de producto, números de lote, fechas de caducidad o detalles logísticos. Esto permite una interpretación detallada y estandarizada de la información de producto y almacén. Para más detalles, consulta la [documentación oficial de GS1-128](https://www.gs1.org/standards/barcodes){target="_blank"}.
        
        !!! info 
            Tal y como indica el estándar, al usar un identificador de longitud variable debe añadirse un separador. El valor declarado por el estándar es **FNC1**
                            
        Esta configuración permite el reconocimiento de diferentes Application Identifiers (AIs) utilizados en procesos de almacén. Los principales códigos implementados son:

        | AI Code  | Descripción                          | Detalles                                                                 | Tipo de longitud |
        |----------|--------------------------------------|-------------------------------------------------------------------------|------------------|
        | **(01)** | GTIN (Global Trade Item Number)      | Identifica globalmente un producto comercial mediante un código de 14 dígitos. | Longitud fija    |
        | **(10)** | Número de lote                       | Garantiza la trazabilidad en procesos de fabricación y distribución.    | Longitud variable |
        | **(17)** | F. caducidad                         | Indica la fecha de caducidad del producto en formato YYMMDD.            | Longitud fija    |
        | **(21)** | Número de serie                      | Número de serie único de un artículo.                                   | Longitud variable |
        | **(91)** | Código de hueco                      | Identifica la ubicación específica dentro del almacén.                  | Longitud variable |
        | **(92)** | Unidad logística                     | Identifica una unidad logística, como un palé o una caja.               | Longitud variable |
        | **(93)** | Uso libre                            | -                                                                       | -                |
        | **(94)** | Uso libre                            | -                                                                       | -                |
        | **(95)** | Uso libre                            | -                                                                       | -                |
        | **(96)** | Uso libre                            | -                                                                       | -                |
        | **(97)** | Uso libre                            | -                                                                       | -                |
        | **(98)** | Uso libre                            | -                                                                       | -                |
        | **(99)** | Uso libre                            | -                                                                       | -                |

        Gracias a esta configuración, al escanear un código de barras *GS1-128*, interpreta la información relevante y la aplica al proceso en curso (recepción, picking, packing). Por ejemplo, cuando lee un identificador 91, lo asocia a un hueco, o cuando lee un identificador 92, lo asocia a una unidad logística.

        !!! warning "Reglas de identificación de códigos de barras"

            Etendo interpreta únicamente los identificadores definidos en esta configuración.
            Los identificadores GS1-128 90–99 son códigos de uso libre y pueden asignarse a atributos de producto personalizados.

            Por defecto:

            - AI 91 y 92 son usados por Etendo.
            - AI 93–99 quedan disponibles para atributos de producto personalizados que se resuelven dinámicamente (p. ej., 93 = color, 94 = talla).

            Los usuarios pueden cambiar tanto los identificadores como los atributos a los que hacen referencia. Sin embargo, cualquier cambio es responsabilidad del usuario y puede causar inconsistencias con el parseo estándar de GS1-128 o con integraciones externas.

            Si se requiere una interpretación diferente, un desarrollador puede crear un **Barcode Algorithm** personalizado.

        <figure markdown="span">
            ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/barcode-components-configuration-attr-2.png)
            <figcaption> Ejemplo: configuración de entidad de producto personalizada</figcaption>
        </figure>
    
        !!! info "Restricciones y validaciones de configuración"
    
            - Al crear o modificar identificadores (AI), el sistema aplica una serie de validaciones diseñadas para mantener la consistencia y unicidad de las configuraciones.
            - Cada AI debe ser único. No puede existir más de un registro con el mismo número de AI, independientemente de la entidad o del campo asociado.
            - Cuando un AI se asocia a un tipo de información específico como Lote, F. caducidad o Número de serie, ese tipo no puede repetirse dentro de la misma configuración.
            - El sistema permite incluir atributos personalizados en códigos de barras. Durante el escaneo, estos atributos se interpretan dinámicamente como **identificadores de producto adicionales**, junto con los valores estándar, permitiendo la validación y distinción de un producto único.

    === ":material-playlist-plus: Direct String Match"

        Este método permite al sistema leer el código y compararlo exactamente con los códigos de los productos almacenados en el sistema. La comparación es directa y estricta, sin tener en cuenta ninguna estructura adicional en el código.    

        ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/ai-config-direct-1.png)


6. Infraestructura de **Task**:

    El módulo [Task](../platform-extensions/task.md), instalado automáticamente como dependencia, gestiona eventos y dispara la creación de tareas y acciones tras cambios dinámicos, habilitando la automatización de workflows.

    En concreto, se utiliza al crear una Picking List.

    !!! warning "Requerido"
        Un desarrollador debe completar la configuración inicial descrita en [Task - Initial Configuration](../../../../../developer-guide/etendo-classic/bundles/platform/task.md#initial-configuration) para utilizar este módulo.

    Cuando se instala el módulo Gestión Avanzada de Almacén, los tipos de tarea requeridos para picking y packing desde Etendo Mobile se incluyen por defecto:

    ![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/task-type.png)

    **User Algorithm**

    Cada tipo de tarea permite seleccionar el algoritmo de asignación del operario de almacén. Por defecto, se utiliza el algoritmo Round-Robin.

    **System Preferences**

    Las preferencias `Create Warehouse Task` y `Task From Date Completed Days`, disponibles en la pestaña *Preference*, están relacionadas con la funcionalidad de tareas: `Create Warehouse Task` habilita la creación automática de tareas cuando se completa un picking, y `Task From Date Completed Days` define el número de días por defecto para mostrar tareas completadas.
## Configuración de Datos Maestros

### Creación de Estados de Inventario  

`Aplicación` > `Gestión de Almacén` > `Configuración` > `Inventory Status`

Los estados de inventario permiten al usuario clasificar y gestionar las unidades de stock según su condición o disponibilidad operativa. El sistema incluye algunos estados predefinidos (como *Bloqueado*, *Dañado*, *En Control de Calidad*, etc.), pero es posible crear nuevos estados personalizados como `Administrador del Sistema` según las necesidades del cliente.

!!!info
    Para más información sobre cómo configurar estados de inventario, visita [Inventory Status](../../../../../developer-guide/etendo-classic/concepts/inventory-status.md).

El nuevo estado estará disponible en **Etendo Mobile** para asignarlo a huecos nuevos o existentes usando las opciones de tarea **Ajustar** o **Reubicar**. En este último caso, se utilizan las reglas definidas en la ventana `Movement Rules Configuration`, descrita a continuación.

### Ventana de Configuración de Reglas de Movimiento

`Aplicación` > `Gestión de Almacén` > `Configuración` > `Movement Rules Configuration`

Las reglas de movimiento permiten automatizar la reubicación o el cambio de estado del inventario en función de la acción que se esté realizando. El propósito de esta funcionalidad es automatizar los movimientos de inventario cuando cambian de estado, excluir determinadas ubicaciones de operaciones como el picking o las reservas debido a su estado, evitar errores en la manipulación de productos, gestionar productos especiales (*Dañado*, *Bloqueado*, etc.) y gestionar automáticamente ubicaciones virtuales cuando no existe un destino definido.

Un **Hueco Virtual** es una ubicación generada automáticamente por el sistema para mantener correctamente el inventario, incluso cuando no se ha definido una ubicación específica para el estado al que se está moviendo. 

!!! Example
    Si el estado *Disponible* no tiene un hueco asociado, y un usuario marca un producto como *Dañado*, entonces el sistema crea una ubicación virtual en la que depositar el inventario afectado. Esta ubicación virtual hereda las propiedades del hueco donde estaba ubicado el producto y queda asociada exclusivamente al nuevo estado (p. ej., *Disponible*).

Esto permite al usuario mantener la trazabilidad y la consistencia del inventario, incluso si el equipo todavía no ha definido todas las ubicaciones físicas. También agiliza las operaciones al evitar errores o bloqueos al trabajar con estados excepcionales.

La aplicación de estas reglas puede verse desde dos funcionalidades de Etendo Mobile:

- Desde las tareas de **Reubicar**, una vez seleccionada la ubicación definida en una regla, esto moverá el inventario a la nueva ubicación y, según la regla configurada, cambiará el estado del inventario.

- Desde las tareas de **Ajustar**, cuando seleccionas el nuevo estado, esto actualizará el estado y, dependiendo de la regla configurada, moverá el inventario a la ubicación definida.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/movement-rules-config.png)

Campos a tener en cuenta: 

- **From Locator**: Ubicación origen.
- **To Locator**: Ubicación destino.
- **To State**: Estado al que se transferirá el inventario cuando se realice el movimiento.

!!!Note
    Si el campo **To State** se rellena primero, el campo **To Locator** se limitará a los **Huecos** que tengan asignado ese estado.

!!!Info
    Las acciones realizadas mediante reglas de movimiento impactan tanto en Etendo Mobile como en el **Informe Stock** de Etendo, reflejando la ubicación.

### Código de barras

La funcionalidad de código de barras es clave para las operaciones logísticas. Los huecos y los productos con códigos generados estarán disponibles para ser escaneados y gestionados tanto desde **Etendo Mobile** como desde **Etendo**, pero requiere una configuración previa.

- Debe cargarse el conjunto de datos `Advanced Warehouse Management`.
- Desde la ventana **Advanced Warehouse Configuration**, puedes definir qué código de barras se utilizará por defecto.

Es posible generar estos códigos únicos para los huecos en las ventanas **Almacén y huecos** y **Producto**:

=== "Desde la ventana **Almacén y huecos**"

    1. Selecciona el **Almacén y hueco**.
    2. Haz clic en **Generate Barcode** y confirma con Done.

        ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/barcode1.png)

    3. El código generado se muestra en el hueco en el campo **Código de barras**. También puede cargarse manualmente o modificarse.

        ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/barcode2.png)
    
    4. Por otro lado, puedes obtener una impresión del código de barras generado haciendo clic en el botón Generate Printable. Debes seleccionar un proveedor, la impresora y el número de copias.

        ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/barcode-print-1.png)

    !!! info
        Para usar la opción de impresión, debes tener el módulo Print Provider. Para más detalles, consulta [Print Provider](../../../../../user-guide/etendo-classic/optional-features/bundles/platform-extensions/print-provider.md)

=== "Desde la ventana **Producto**"

    1. Selecciona el producto.
    
    2. Haz clic en Generate Barcode y confirma con Done.
    
    3. El código generado se muestra en la cabecera de la ventana de producto en el campo **UPC/EAN**. También puede cargarse manualmente o modificarse.

        ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/barcode4.png)
    
    4. Puedes obtener una impresión del código de barras generado haciendo clic en el botón *Generate Printable*. Debes seleccionar un proveedor, la impresora y el número de copias.
    
        ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/barcode-print-2.png)

        !!! info
            Para usar la opción de impresión, debes tener el módulo Print Provider. Para más detalles, consulta [Print Provider](../../../../../user-guide/etendo-classic/optional-features/bundles/platform-extensions/print-provider.md)
    
    !!! info 
        En la ventana **Producto**, existe una pestaña llamada **Barcode**, donde se listan varios códigos de barras asociados al producto, como los códigos de proveedor. Estos códigos se cargan manualmente, permitiendo especificar el algoritmo utilizado para encriptar el código y la configuración del Identificador de Aplicación.
        
        Para configurar cómo el sistema busca códigos de barras:
        
        - En la ventana **Advanced Warehouse Configuration**, hay una casilla de verificación denominada `Search Related Barcode`
        - Si la casilla está habilitada, al escanear un producto desde Etendo Mobile, el sistema buscará coincidencias en todos los códigos listados en la pestaña Barcode, además del código de cabecera.
## Albarán de entrada

### Visión general

La funcionalidad de [Inventario Referenciado (RI)](../../../basic-features/warehouse-management/transactions.md#referenced-inventory) se ha ampliado para gestionar unidades logísticas físicas como **palés** y **cajas**, vinculadas directamente a las [Unidades Alternativas (AUOM)](../../../basic-features/master-data-management/master-data.md#alternate-uom-tab) de cada producto. Esto permite definir equivalencias (p. ej., 1 Palé = 100 unidades) y gestionar estas unidades como entidades únicas y trazables en las operaciones de almacén.

El módulo [Stock Logistic Unit](./stock-logistic-unit.md), instalado como dependencia, añade nuevas unidades (Caja, Palé) y tipos de inventario referenciado, permitiendo a los usuarios configurar equivalencias en la pestaña **Unidad Alternativa** de la ventana Producto. Una vez definida, si se requiere una conversión diferente, debe crearse una nueva AUOM.

Cuando se reciben mercancías, el sistema puede generar automáticamente registros de RI para cada unidad logística (Caja o Palé), incluyendo detalles del producto, cantidad en unidad base y atributos como lote o fecha de caducidad. Cada unidad se registra como un ítem único desde el momento en que entra en el almacén, garantizando trazabilidad completa.  

!!! info
    Para una configuración y uso detallados de las unidades logísticas, consulta la documentación de [Stock Logistic Unit](./stock-logistic-unit.md).

### Ventana Albarán de entrada  

:material-menu: `Aplicación` > `Gestión de Compras` > `Transacciones` > `Inbound Receipt`

La ventana **Inbound Receipt** mejora el flujo de [albaranes](../../../basic-features/procurement-management/transactions.md#goods-receipts) introduciendo un paso intermedio entre el pedido de compra y el albarán. Este paso centraliza múltiples pedidos —incluso de distintos proveedores— en una única operación, mejorando la flexibilidad, la automatización y el control. También soporta unidades alternativas (AUOM), permitiendo registrar recepciones en palés, cajas o reagrupar en distintos contenedores para reflejar la entrada real.

Las recepciones siempre se crean a partir de pedidos de compra, no manualmente. Las líneas del pedido se cargan con detalles de producto, cantidad, lote y ubicación, que pueden ajustarse (p. ej., cantidad o unidad) para registrar recepciones parciales o alternativas. Esto garantiza que el albarán refleje con precisión lo recibido físicamente y actualice el pedido de compra en consecuencia.

Cuando se usan AUOM como Palé o Caja, el sistema puede generar automáticamente un registro de Inventario Referenciado (RI) vinculado a la línea de recepción, representando la unidad logística y asegurando la trazabilidad.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inbound-receipt-window-0.png)

Campos a tener en cuenta:

#### Cabecera

- **Organización**: Define la organización en la que se creará el albarán de entrada y filtra la información.  
- **Document Type**: Cargado por defecto con *Inbound Receipt* para clasificar el tipo de documento.  
- **Nº documento**: Identificador único generado automáticamente para la recepción, con una secuencia específica para este tipo de documento.  
- **Fecha del movimiento**: Fecha en la que se registra el movimiento físico de mercancía. Por defecto, es la fecha actual.  
- **Descripción**: Campo de texto libre para añadir información adicional o notas sobre la recepción.  

#### Pestaña Líneas

La pestaña Líneas permite añadir y modificar productos individuales de uno o varios pedidos de compra, ajustando su cantidad y/o unidad. Representa la lista de productos recibidos, mostrando los siguientes campos además de los básicos.

![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inbound-receipt-window-1.png)

Campos a tener en cuenta:

- **Line No**: Número secuencial asignado automáticamente para identificar la línea dentro de la recepción.  
- **Producto**: El producto que se está recibiendo, vinculado al pedido de compra.  
- **Cantidad Operativa**: Cantidad recibida expresada en la unidad alternativa del producto. Coincide con la **Cant. pedido** si no hay AUOM definida. Si existe AUOM, indica el número de palés, cajas u otras unidades alternativas recibidas.  
- **Unidad Alternativa**: Unidad alternativa del producto. Si no hay AUOM definida, por defecto toma la unidad. Se usa para registrar la recepción de productos en palés, cajas u otros contenedores.  
- **Cant. pedido**: Cantidad recibida expresada en la unidad base del producto.  
- **Unidad**: Unidad base del producto (p. ej., unidades, litros, kilogramos).  
- **Valor atributos**: Atributos asociados al producto, como lote, número de serie o fecha de caducidad.  
- **Hueco**: Ubicación donde se almacenará el producto recibido. Puede variar entre líneas, permitiendo asignar distintas ubicaciones a productos del mismo o de distintos pedidos de compra.  
- **Línea del pedido de compra**: Referencia a la línea original del pedido de compra desde la que se generó la línea de recepción.  
- **Grouped By**: Identificador de la agrupación a la que pertenece la línea, generado al usar el botón *Group By*. Muestra qué líneas forman parte del mismo contenedor o unidad de embalaje.  
- **Reference Inventory Type**: Tipo de inventario referenciado asociado a la agrupación (p. ej., Caja, Palé).
- **Línea de albarán**: Referencia al albarán generado al completar el albarán.  

#### Botones

**Crear Líneas Desde Pedido**

Extrae líneas de producto desde pedidos de compra. Al pulsarlo, un pop-up muestra todos los productos disponibles, incluso de múltiples pedidos de compra. Puedes seleccionar una o varias líneas para añadirlas a la pestaña Líneas. Si se define un hueco, se asignará a todas las líneas seleccionadas; en caso contrario, puede establecerse individualmente por línea.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inbound-receipt-create-line-boton.png)

**Create Reference Inventory**

Este botón aparece cuando hay al menos una línea seleccionada. Permite agrupar múltiples/mixtas líneas en un único tipo de unidad logística (cajas, palés u otros tipos definidos en el sistema). Su función es reunir los productos seleccionados de la pestaña Líneas en una agrupación específica, según el tipo de agrupación elegido.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inbound-receipt-button-group-1.png)

La agrupación se refleja en la columna Grouped by de las líneas seleccionadas (p. ej., Box-1). 

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inbound-receipt-button-group-2.png)

!!! info
    - Solo se pueden agrupar líneas del mismo Pedido de venta.  
    - Si una línea ya está agrupada y se incluye en una nueva agrupación, la agrupación anterior será reemplazada.

**Clear Group By** 

Este botón permite eliminar una línea de su agrupación sin afectar al resto de líneas del grupo.

**Generate Reception Task** 

Permite gestionar recepciones operativas desde la app móvil mediante la creación de Tareas de recepción. Está disponible cuando existe un Inbound Receipt que aún no está completado y tiene líneas cargadas.

Al pulsar el botón, se genera una tarea vinculada al documento seleccionado y pasa a ser visible en la app móvil y en la ventana Task del ERP.  
En la ventana emergente, puedes asignar un usuario o habilitar la asignación automática. Si se seleccionan múltiples registros, se creará una tarea por cada registro, todas asignadas al mismo usuario o rol definido en el pop-up.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inbound-receipt-popup-1.png)

!!!Info
    Para más información, visita [Tareas de recepción](#reception-tasks).

**Complete Receipt**

Finaliza la recepción, generando y completando los **albaranes pendientes de recibir** correspondientes. Además, si la recepción incluye productos con AUOM (palé o caja), se crea automáticamente el registro asociado de **Inventory Reference**.

**Print Labels**

Este botón genera etiquetas de código de barras para **todas las líneas** del documento Inbound Receipt seleccionado.  
Cada etiqueta se crea con el **conjunto completo de atributos definidos durante la recepción**, incluyendo datos del producto y atributos como lote, número de serie, fecha de caducidad e inventario referenciado cuando aplique.

- Para **productos sueltos** (sin unidades logísticas), el sistema genera **una etiqueta de código de barras por cantidad operativa** definida en la línea de recepción.  
  Esto significa que se imprimen tantas etiquetas como unidades se indiquen en el campo **Cantidad Operativa**.
- Para **líneas con unidades logísticas (Caja o Palé)** donde se reciben múltiples unidades (por ejemplo, 3 cajas), el sistema genera **una etiqueta de código de barras única por unidad logística**, ya que cada unidad se registra como un inventario referenciado único.
- Cuando los productos se **agrupan en una única unidad logística** usando el botón **Create Reference Inventory**, el sistema genera **una única etiqueta de código de barras** para esa unidad logística.  
  En este caso, la etiqueta identifica la **unidad logística y su hueco**, ya que puede contener múltiples productos agrupados.

Este botón está disponible **solo cuando el Inbound Receipt está completado**.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inbound-receipt-print-header-1.png)

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inbound-receipt-print-header-2.png)

??? example "Imprimir Inbound Receipt - Ejemplos"

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inbound-receipt-print-header-3.png)

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inbound-receipt-print-header-4.png)

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inbound-receipt-print-header-5.png)

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inbound-receipt-print-header-6.png)

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inbound-receipt-print-header-7.png)

**Print Line Label**

Esta acción genera **etiquetas de código de barras solo para la línea o líneas seleccionadas** del Inbound Receipt.  
Cada etiqueta contiene el **conjunto completo de atributos asignados en el momento de la recepción** para las líneas seleccionadas.

La generación de etiquetas sigue las mismas reglas descritas anteriormente, aplicadas **solo a la línea o líneas seleccionadas**:

- Para **productos sueltos**, se genera una etiqueta de código de barras **por cantidad operativa** definida en cada línea seleccionada.
- Para **múltiples unidades logísticas**, se genera una etiqueta única por unidad logística.
- Para **unidades logísticas agrupadas**, se genera una única etiqueta identificando la unidad logística.

Este botón está disponible **solo cuando el Inbound Receipt está completado**.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inbound-receipt-print-lines-1.png)

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inbound-receipt-print-lines-2.png)

### Flujo de trabajo

**Flujo de recepción**

1. En el flujo de recepción, el usuario tiene un **Pedido de compra** que incluye líneas de producto configuradas con una Unidad Alternativa (AUOM) de tipo Caja o Palé, con su equivalencia previamente definida en la ventana de producto (por ejemplo, 1 Palé = 100 unidades). 

    ![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inbound-flow-1.png)

2. Desde la ventana **Inbound Receipt**, el usuario crea un nuevo registro de recepción usando el botón *Crear Líneas Desde Pedido*, seleccionando el Pedido de compra como documento de referencia. El sistema incorpora los datos del pedido, como el producto, la cantidad (en AUOM), los atributos (lote, serie) y otra información asociada. 

    ![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inbound-flow-3.png)

    !!!info "Dos formas de completar la recepción"
        En este punto, puedes elegir entre dos flujos de trabajo para completar el albarán de entrada:
        
        **Opción 1: Completar desde Etendo (ERP)**  
        Continúa con los pasos 3 y 4 a continuación para completar la recepción directamente en la ventana **Inbound Receipt** pulsando el botón **Complete Receipt**.
        
        **Opción 2: Completar desde Etendo Mobile**  
        Usa el botón **Generate Reception Task** para crear una tarea de recepción visible en **Etendo Mobile**. Esto permite a los operarios de almacén realizar la recepción directamente desde sus dispositivos móviles. Para más información, visita [Tareas de recepción](#reception-tasks).

3. Al pulsar el botón Completar, el sistema genera y completa secuencialmente el **Albarán** y crea un registro en **Inventario Referenciado (RI)** para cada unidad logística recibida (Caja o Palé), respetando las equivalencias definidas en AUOM.

    ![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inbound-flow-2.png)

4. El Inventario Referenciado queda vinculado a la cantidad recibida, el producto y sus atributos correspondientes. Como resultado, el stock se actualiza en el inventario, incrementando el número de unidades en la ubicación definida y habilitando la trazabilidad mediante el RI generado.

    ![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inbound-flow-4.png)

**Flujo de recepción parcial**

1. El proceso de recepción parcial comienza cuando existe un **Pedido de compra** que contiene una línea de producto configurada con una AUOM; por ejemplo, 1 caja de zumo de piña equivalente a 12 unidades.  
2. Desde la ventana **Inbound Receipt**, el usuario inicia un nuevo registro de recepción usando el botón *Crear Líneas Desde Pedido* y selecciona el Pedido de compra como referencia. El sistema carga automáticamente las líneas del pedido, incluyendo el producto y la cantidad esperada, como 1 caja.  
3. A continuación, en la línea de recepción, el usuario modifica la cantidad para reflejar la recepción parcial; por ejemplo, si el pedido es de 1 caja (12 unidades) pero solo se reciben 6 unidades, el usuario cambia la cantidad a 6 y, si es necesario, ajusta la unidad de medida a **unidades** en lugar de **caja**.  
4. Una vez ajustada la cantidad real recibida, el usuario completa la recepción pulsando el botón *Completar* en la ventana Inbound Receipts.  
5. En ese momento, el sistema genera y completa el albarán, reflejando la cantidad parcial realmente recibida. El inventario se actualiza con la cantidad recibida. El **Pedido de compra** mostrará el porcentaje recibido en la barra de estado.
## Inventory Quality Inspection

### Visión general

La ventana **Inventory Quality Inspection** permite una gestión y control completos de los procesos de inspección de calidad dentro de las operaciones de almacén. Sirve como una herramienta centralizada para registrar, auditar y ejecutar controles de calidad, manteniendo la trazabilidad completa entre las inspecciones, las tareas asignadas a los operarios y los movimientos de stock resultantes. Esta funcionalidad garantiza que los productos cumplan los estándares de calidad antes de ponerse a la venta o de continuar con su procesamiento, evitando que artículos defectuosos o no conformes entren en la cadena de distribución.

### Ventana Inventory Quality Inspection

:material-menu: `Aplicación` > `Gestión de Almacén` > `Transacciones` > `Inventory Quality Inspection`

Esta ventana permite a los usuarios crear y gestionar registros de inspección de calidad para artículos de inventario. Las inspecciones pueden realizarse sobre stock existente. El sistema registra qué productos necesitan inspección, su estado actual, ubicación y las cantidades planificadas para revisión.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inventory-quality-inspection-window.png)

Campos a tener en cuenta:

#### Header

- **Organización**: Define la organización en la que se creará la inspección de calidad y filtra la información disponible.  
- **Nº documento**: Identificador único generado automáticamente para el documento de inspección, siguiendo una secuencia específica para este tipo de documento.  
- **Nombre**: Nombre descriptivo del registro de inspección de calidad para ayudar a identificar su propósito o contenido.  
- **Quality Control Date**: Fecha en la que la inspección está programada o se realiza. Por defecto, es la fecha actual.  
- **Descripción**: Campo de texto libre para añadir información adicional o notas sobre la inspección.

#### Pestaña Lines

La pestaña Lines lista los productos a inspeccionar, incluyendo su estado de inventario actual, ubicación y cantidades planificadas para inspección. Cada línea representa un producto o lote que requiere inspección de calidad.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inventory-quality-inspection-lines.png)

Campos a tener en cuenta:

- **Line No**: Número secuencial asignado automáticamente para identificar la línea dentro del documento de inspección.  
- **Producto**: El producto que se está inspeccionando.  
- **Hueco**: Ubicación actual del producto en el almacén.  
- **Cantidad teórica**: Cantidad registrada en los registros de inventario del sistema para este producto en la ubicación especificada.  
- **Unidad**: Unidad de medida del producto (p. ej., Unidad, Caja, Kg).  
- **To State**: Estado de inventario objetivo que se asignará al producto tras la inspección (p. ej., *Available*, *Damaged*, *Blocked*).  
- **Cant.total**: Cantidad real contada o inspeccionada durante el proceso de control de calidad.  
- **Descripción**: Campo de texto libre para añadir notas u observaciones adicionales sobre la línea de inspección.  
- **Línea de movimiento**: Referencia a la línea de movimiento de inventario asociada a esta inspección, si aplica.

#### Botones

**Proceso**

Procesa el documento de inspección de calidad, validando los datos de inspección y actualizando el inventario en base a los resultados registrados en las líneas. Este botón está disponible cuando el documento de inspección tiene líneas.

**Generate Task**

Crea una tarea de inspección de calidad que es visible tanto en la ventana **Task** en Etendo como en **Etendo Mobile**. Este botón está disponible cuando el documento de inspección tiene líneas cargadas. 

Al hacer clic, aparece una ventana emergente donde puedes asignar la tarea a un usuario específico o habilitar la asignación automática basada en rol. Si se seleccionan múltiples documentos de inspección, se creará una tarea para cada uno, todas asignadas al mismo usuario o rol definido en el pop-up.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inventory-quality-inspection-generate-task.png)

### Flujo de trabajo

El proceso de Inventory Quality Inspection comienza en Etendo cuando un usuario crea un nuevo registro en la ventana **Inventory Quality Inspection**.

1. **Create Inspection Document**: Se crea un nuevo documento de inspección en la ventana **Inventory Quality Inspection** con la información necesaria de cabecera (organización, nombre, fecha de control de calidad, descripción).

2. **Add Products to Inspect**: Se añaden a la pestaña Lines los productos que requieren inspección. Para cada línea, especifica:
    - El producto a inspeccionar
    - Ubicación del hueco
    - Cantidad teórica (inventario del sistema)
    - Cualquier descripción o nota relevante

    !!!info "Two Ways to Complete the Inspection"
        En este punto, puedes elegir entre dos flujos de trabajo para completar la inspección de calidad:
        
        **Option 1: Complete from Etendo (ERP)**  
        Continúa con los pasos 3 y 4 a continuación para realizar la inspección directamente en la ventana **Inventory Quality Inspection**.
        
        **Option 2: Complete from Etendo Mobile**  
        Usa el botón **Generate Task** para crear una tarea de inspección de calidad visible en **Etendo Mobile**. Esto permite a los operarios de almacén realizar la inspección directamente desde sus dispositivos móviles. Para más información, visita [Quality Inspection Tasks](#quality-inspection-tasks).

3. **Process Inspection**: 
    - Revisa cada línea de producto y actualiza el campo **To State** con el nuevo estado para las unidades; después, introduce la **Cant.total** para las unidades que correspondan a ese estado.
    - El sistema comparará la **Cantidad teórica** con la **Cant.total** para identificar discrepancias.
    - Asigna el estado objetivo adecuado en función de los resultados de la inspección.

4. **Complete the Inspection**: Haz clic en el botón **Proceso** para finalizar el documento. El sistema:
    - Actualizará el estado de inventario de los productos inspeccionados según el campo **To State**
    - Creará movimientos de inventario que reflejen los resultados de la inspección
    - Gestionará la reubicación del producto en función del estado objetivo:
        - Si existe una [movement rule](#movement-rules-configuration-window) para el estado objetivo, el sistema la aplica automáticamente
        - Si no existe una movement rule, el sistema comprueba si ya hay un hueco asignado a ese estado
        - Si no se encuentra ningún hueco, el sistema crea un **virtual storage bin** para el estado objetivo para mantener la consistencia del inventario
    - Actualizará el **Informe Stock** con el nuevo estado de inventario

5. Todos los cambios se reflejan en el sistema, manteniendo la trazabilidad completa del proceso de inspección de calidad.

!!!warning "Movement Rules and Storage Bins"
    Se recomienda configurar [Movement Rules](#movement-rules-configuration-window) para los estados de inspección de uso común (p. ej., *Damaged*, *Blocked*) para mantener una correcta organización del almacén.

## Reserva de existencias AUOM

### Visión general

Se ha añadido la opción de reservas de stock basadas en la unidad definida en el pedido de venta (campo AUOM), que determina si el producto se vende en su unidad base o en una unidad alternativa (por ejemplo, una botella suelta o una caja de 12).  

!!! info 
    Por defecto, cuando el módulo está instalado, las preferencias `Enable Stock Reservations` y `Enable UOM Management` están habilitadas. Para más detalles, consulta [Stock Logistic Unit - Preference](./stock-logistic-unit.md#preference).

### Flujo de reserva

1. El proceso comienza cuando se crea un **Pedido de venta** con líneas de producto definidas con una Unidad Alternativa (AUOM) (p. ej., 1 Caja = 24 Unidades).
2. En cada línea, el campo **Reserva de existencias** se establece como *Automatic*, por lo que el sistema intenta reservar stock cuando se confirma el pedido.
    ![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/reservation.png)
3. Lógica de reserva:

    - El sistema reserva stock en la unidad especificada en la línea del pedido.  
    - Si hay stock suficiente, se crea una reserva completa.  
    - Si no, reserva la cantidad disponible en esa unidad y complementa con otras AUOM o unidades base.  
    - Si se cubre el total, la reserva es completa; en caso contrario, es parcial.
    
    ![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/reservation-1.png)

**Ejemplos**

- Pedido: 10 unidades; Stock: 5 unidades + 1 caja de 10 → Solo se reservan 5 unidades (la caja no se puede dividir).  
- Pedido: 110 unidades; Stock: 100 unidades + 1 caja de 10 → Reserva completada con ambos.  
- Si no hay stock disponible en la unidad solicitada, el sistema igualmente intenta reservar usando otras AUOM.  

### Flujo de Picking/Packing

En los procesos de [Picking](./picking.md) y [Packing](./packing.md). Si los códigos de barras **GS1-128** están configurados, una vez que se ha validado un [código de barras](#barcode), el sistema puede identificar no solo el producto, sino también su unidad alternativa (AUOM) y los atributos asociados, como lote o F. caducidad.

Durante el picking, cuando se escanea el código, el sistema interpreta la información estructurada que contiene (producto, lote, fecha de caducidad, etc.) y la compara con la reserva, registrando directamente la cantidad correspondiente. Esto garantiza que la salida de stock coincida exactamente con el producto real a preparar.

En el packing, se utiliza la misma validación al empaquetar productos. El sistema reconoce qué producto es, en qué presentación y con qué atributos, y lo asigna a la caja correspondiente. Esto asegura que el envío refleje exactamente lo que se ha recogido, manteniendo una trazabilidad completa.

De este modo, Etendo garantiza que un único escaneo reconozca de forma integral el producto que sale o va a salir, teniendo en cuenta sus medidas alternativas y atributos, y evitando errores a lo largo de toda la cadena desde el pedido hasta la expedición.

!!! Example
    Ejemplo de código de barras con atributos: **01** 95012345678930 **\x1D** **10**L101 **\x1D** **17** 260910 **91** Rn-0-0-0

    donde:

    - \x1D = separator para valores variables
    - 01 = identificador de producto
    - 95012345678930 = id del producto
    - 10 = identificador de lote
    - L101 = lote
    - 17 = identificador de caducidad
    - 260910 = fecha de caducidad (AAMMDD)
    - 91 = identificador de hueco
    - Rn-0-0-0 = código de unidad logística
## Uso de Etendo Mobile

Al iniciar sesión en Etendo Mobile, al operario de almacén se le presentarán las aplicaciones y menús disponibles según su rol.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/advanced-warehouse-management.png)

Como se ve arriba, la opción Advanced Warehouse Management incluye los siguientes menús:

- [Tareas de recepción](#tareas-de-recepción)
- [Tareas de picking](#tareas-de-picking)
- [Tareas de packing](#tareas-de-packing)
- [Tareas de reubicación](#tareas-de-reubicación)
- [Tareas de ajuste](#tareas-de-ajuste)
- [Todas las tareas](#todas-las-tareas)

### Tareas de recepción

Permite crear y controlar recepciones directamente desde la aplicación móvil usando **tareas de recepción**, que reproducen el mismo comportamiento y flujo de proceso que las ventanas [Albarán](../../../basic-features/procurement-management/transactions/#goods-receipts) y [Inbound Receipt](#inbound-receipt) en el ERP.

#### Inicio del proceso (Etendo)

El proceso comienza haciendo clic en el botón **Generate Receiving Task** en la ventana *Inbound Receipt* del ERP. Allí, la tarea se asigna a un operario, se define la prioridad y, a continuación, se refleja en la aplicación móvil del operario asignado.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inbound-receipt-popup-1.png)

#### Acceso a las tareas de recepción (Etendo Mobile)

Al acceder a **Etendo Mobile** en la sección **Tareas de recepción**, se mostrarán todas las tareas y sus estados correspondientes pertenecientes al usuario que ha iniciado sesión. Por defecto, las tareas se muestran con estado *Pendiente*.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/reception-mobile-1.png)

**Tareas de recepción**

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/reception-mobile-2.png)

Para realizar una **recepción**:

- Accede al menú **Tareas de recepción**. Allí, las tareas se dividen por estado: Pendiente, En curso, Completada.
- Busca y selecciona la tarea desde la lista o usando el buscador.
- Al seleccionar una tarea, se abre una pantalla con la información de la tarea.
- Pulsa el botón **Start Receipt**.
- **Escanea** los productos para ubicarlos en stock o **cárgalos** manualmente.
- Si el producto tiene configurado un **Conjunto atributos** (como número de lote, número de serie, fecha de caducidad u otros atributos personalizados), aparecerá una ventana emergente solicitando esta información. Completa los campos requeridos y confirma para continuar con la recepción.

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/reception-mobile-3.png)

- Si es necesario, se puede modificar el **hueco (locator)** para cambiar la ubicación destino de los productos recibidos.
- Confirma la tarea con el botón **End Reception**.
- Confirma que deseas finalizar la tarea.
- Ver **mensaje de éxito**.

### Tareas de picking

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/picking-1.png)

El proceso de picking permite al operario recoger de forma eficiente los productos requeridos para un pedido usando Etendo Mobile. El flujo completo del proceso se detalla a continuación.

!!!Info
    Para más información sobre cómo usar esta funcionalidad en Etendo, visita [Picking](./picking.md).

#### Inicio del proceso (Etendo)

El proceso se inicia en Etendo cuando se crea una [Picking List](picking.md#picking-list-generation) desde un Pedido de venta. Esto puede hacerse usando el botón **Generate Picking List** disponible en la ventana de Pedido de venta, que crea una nueva **tarea** que se asignará a un usuario para su ejecución en Etendo Mobile.

!!!Important
    Recuerda que las únicas picking lists que se muestran en Etendo Mobile son las marcadas como tipo **Direct Picking List to Customer**.

Cuando se genera una picking list, el sistema ejecuta procesos automáticos en segundo plano que varían según la configuración. En determinadas situaciones, algunos de estos procesos pueden fallar sin que el usuario lo note inmediatamente.

Para proporcionar mayor visibilidad, el sistema muestra un **mensaje de advertencia** en diferentes etapas del proceso, que incluye un enlace a la ventana Task. Desde allí, el usuario puede comprobar los detalles de cada proceso ejecutado y revisar los logs correspondientes, asegurando un mejor control sobre la correcta finalización de las operaciones.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/message-picking-list-1.png)

Los procesos que deben verificarse son los siguientes:

- Para **tareas de picking con creación activa de tarea de packing**:

    - Create Shipment
    - Create Picking List
    - Process Picking List
    - Create Packing Task

- Para **tareas de picking sin crear una tarea de packing**:

    - Create Picking List
    - Create Shipment
    - Process Picking List

Ejemplo de logs sin errores:

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/message-picking-list.png)

Ejemplo de logs con errores:

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/message-picking-list-error.png)

#### Acceso a las tareas de picking (Etendo Mobile)

Al acceder a **Etendo Mobile** en la sección **Picking**, se mostrarán todas las tareas y sus estados y prioridades correspondientes, pertenecientes al usuario que ha iniciado sesión. Por defecto, las tareas se muestran con estado *Pendiente*.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/picking-2.png){align=right width=300}
 
Esta pantalla contiene:

- Botones de actualizar y volver.
- Un campo de búsqueda para filtrar tareas.
- Filtros rápidos que limitan entre tareas `Pendiente`, `En curso` o `Completada`.
- Una lista de tarjetas con tareas.

!!! Note
    Como se explicó anteriormente en la sección de la pestaña Preference de [Initial Setup](#initial-setup), existe una preferencia para definir los días a mostrar las tareas en estado `Completada`: `Task From Date Completed Days`. Esto permite al usuario definir el número de días hacia atrás, desde la fecha actual, que se utilizará como criterio para mostrar tareas en estado Completada.

<br clear="all">

#### Picking de producto

1. El operario de almacén debe seleccionar una tarea `Pendiente`.

2. Una vez seleccionada la tarea, se abre una ventana con la lista de productos a recoger.

3. Para iniciar el proceso, haz clic en el botón **Start Picking** ubicado en la parte superior; una vez hecho esto, la tarea pasa al estado `En curso`.
    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/picking-3.png)

4. Una vez iniciado el picking, se abre una nueva ventana con los siguientes elementos:

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/picking-4.png){align=right width=300}


    - **Scan Barcode:** activa la cámara del dispositivo móvil.
    - **Type barcode:** permite introducir el código de barras manualmente. Hay un botón Validate disponible para lanzar el proceso de validación del código de barras.
    - **Quantity with: `+` and `-` buttons** permite la carga manual de la cantidad a escanear.
    - **List of products (N):** lista de tarjetas con información del producto, donde (N) es la cantidad total de productos.

        - Producto
        - Estado:
            - <span style="padding:4px;background-color:#F5F5F5;color:#BDBDBD;border-radius:4px;"> 
                Sin escanear
            </span>
            - <span style="padding:4px;background-color:#fba643ff;color:white;border-radius:4px;"> 
                Escaneado parcialmente
            </span>
            - <span style="padding:4px;background-color:#00B34C;color:white;border-radius:4px;"> 
                Escaneado
            </span>
        - Código de barras
        - Locator
        - Valor atributos
        - Cantidad de movimiento: cantidad total a recoger.
        - AUOM
        - Cantidad contada con botones `+` y `-`: que permiten sumar o restar de uno en uno la cantidad manualmente.

#### Métodos de picking

En el proceso de picking, el operario tiene flexibilidad tanto en qué recoger como en cómo hacerlo. Por un lado, aunque el sistema solicite un código específico (por ejemplo, caja BX100020), es posible sustituirlo por otra unidad equivalente (como BX100023) siempre que el producto y la cantidad coincidan, o adaptarse a la disponibilidad de stock (por ejemplo, entregar 10 unidades sueltas en lugar de una caja de 10). Estas variaciones se registran automáticamente en la reserva y en el albarán de salida.

Por otro lado, el sistema también permite flexibilidad en el modo de operación mediante diferentes métodos de selección:

- Escanear el producto el número de veces solicitado (ej.: 10 escaneos para 10 unidades).
- Escanear una unidad logística, que carga automáticamente la cantidad solicitada junto con su equivalente en unidades según la tasa de conversión.    
- Cargar manualmente "10" en el campo de cantidad y escanear una vez.
- Introducir tanto el código como la cantidad manualmente.
- Introducir manualmente solo la cantidad en el campo Cantidad dentro de una tarjeta de producto, usando los botones + y - o introduciendo el número desde el teclado.

!!! tip
    Al escanear un producto válido, el campo Código de barras se completa automáticamente, se muestra la tarjeta asociada y se incrementa el valor 1 en el producto, si la cantidad no se había cambiado previamente.

!!! tip
    Si previamente se introdujo en el campo Cantidad una cantidad distinta de la cantidad por defecto, por ejemplo 5, y luego se escanea el producto, esas 5 unidades se añadirán directamente a la tarjeta del producto.


!!! Warning
    
    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/picking-5.png){align=right width=200}

    Posibles escenarios de error:

    - Si se escanea un código incorrecto (no coincide con ningún producto de la tarea), el campo de código de barras se resalta en rojo, muestra una cruz y no añade cantidad a ningún producto.   <br><br>
    - Si se intenta introducir una cantidad mayor que la requerida, el sistema cargará el máximo definido en la tarjeta del producto. Una vez completada la cantidad y se vuelve a escanear o recargar el código del producto, el sistema no añade cantidad al producto. Si la cantidad se carga manualmente en la tarjeta del producto, el sistema permite cargar la cantidad máxima solicitada.
    
    En ambos casos, el mensaje de error mostrado es el que se visualiza en la imagen.

    

#### Finalización del picking

Una vez que se registra al menos una unidad de cualquier producto, el botón **End Picking** se activa. Esto permite el picking parcial, es decir, solo se puede recoger parte de la cantidad solicitada, lo cual es útil cuando faltan productos o no son aptos para su uso.

Tras la confirmación, la tarea se marca como Completada.

!!!warning
    Para el picking parcial, la tarea se cierra y no se crea automáticamente una nueva tarea para los productos faltantes. Cualquier cantidad restante debe gestionarse manualmente.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/picking-6.png)

Una vez completada, la tarea aparecerá en la sección de Tareas completadas, donde es posible revisar los productos y cantidades validados para esa tarea de picking específica.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/picking-7.png)


### Tareas de packing

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/packing-mobile-1.png)

El proceso de packing permite al operario empaquetar los productos de forma eficiente usando Etendo Mobile. El flujo completo del proceso se detalla a continuación.

!!!Info
    Para más información sobre cómo usar esta funcionalidad en Etendo, visita [Packing](./packing.md).

#### Inicio del proceso (Etendo)

Las tareas de packing están vinculadas a un registro en la ventana **Packing**. La creación de una tarea de packing se dispara tras:

- La finalización de una tarea de picking (cuando el tipo de tarea `Picking and Packing` está activo).
- Desde la ventana **Packing** de Etendo al añadir al menos un pedido de venta a un nuevo Packing.

#### Acceso a las tareas de packing (Etendo Mobile)

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/packing-mobile-2.png){align=right width=300}


Al acceder a Etendo Mobile y seleccionar el menú **Packing**, se muestra la pantalla principal de packing con el número de tareas `Packing` disponibles para el usuario actual.

Esta pantalla contiene:

- Botones de actualizar y volver.
- Un campo de búsqueda para filtrar tareas.
- Filtros rápidos que limitan entre tareas `Pendiente`, `En curso` o `Completada`. Por defecto muestra seleccionado el filtro `Pendiente` y, en el caso de tareas en estado `Completada`, existe una preferencia donde se define desde qué día traerá las tareas completadas.
- Una lista de tarjetas, donde cada tarjeta representa una tarea de packing e incluye la siguiente información:

    - Packing como título: se muestra la referencia del documento.
    - Estado.
    - Tipo de tarea.
    - Prioridad.

<br clear="all">

#### Packing de producto

1. El operario de almacén debe **seleccionar una tarea**. Para seleccionar la tarea, desplázate o introduce datos clave en el buscador.

2. Al seleccionar una tarea, se abre una pantalla con el número de la lista de packing y el botón **Start Packing**.

3. Al pulsar **Start Packing**, el estado de la tarea cambia a `En curso` tanto en Etendo Mobile como en Etendo.

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/packing-mobile-3.png)

4. La ventana tiene los siguientes elementos:

    - Botón **Scan Barcode** para activar la cámara del dispositivo y escanear.
    - **Type barcode** permite introducir el código de barras manualmente. Hay un botón Validate disponible para lanzar el proceso de validación del código de barras.
    - Campo **Select Pack** para seleccionar el bulto destino al escanear el producto.
    - Campo **Cantidad** que actúa como multiplicador para cargar la cantidad al escanear el producto.
    - Botón **+ Add Pack** que permite añadir nuevas cajas.
    - Una lista de tarjetas de **Producto**, cada una mostrando:

        - Producto
        - Estado:
            - <span style="padding:4px;background-color:#F5F5F5;color:#BDBDBD;border-radius:4px;"> 
                Sin escanear
            </span>
            - <span style="padding:4px;background-color:#fba643ff;color:white;border-radius:4px;"> 
                Escaneando
            </span>
            - <span style="padding:4px;background-color:#00B34C;color:white;border-radius:4px;"> 
                Escaneado
            </span>
        - Código de barras
        - Locator
        - Valor atributos
        - Cantidad
        - AUOM
        - Cantidad empaquetada con botones `+` y `-`: que permiten sumar o restar de uno en uno la cantidad manualmente.

    - Una lista de **Packs**, mostrando:

        - Nombre (o número) del pack
        - Productos y sus cantidades

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/packing-mobile-4.png)


    Los selectores de vista por **Producto** o por **Pack** permiten:

    - En la vista **Productos**, al entrar en una tarjeta de producto, se muestra cómo se distribuyó ese producto en las diferentes cajas, permitiendo navegar producto a producto para revisar las cantidades asignadas por pack.

    - En la vista **Packs**, al entrar en un pack, se muestra el contenido detallado con la posibilidad de navegar pack a pack para comprobar qué productos contiene cada pack.

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/packing-mobile-5.png)

    !!! tip 
        En ambas vistas, es posible modificar las cantidades cargadas y añadir packs si es necesario. Sin embargo, para poder asignar contenido a las cajas añadidas, debe cumplirse una de las siguientes condiciones:

        - La carga total de productos aún no se ha completado, o se modifican (disminuyen) cantidades asignadas previamente para permitir su reubicación al nuevo pack.

5. Una vez iniciado el packing, el usuario selecciona o crea un pack y comienza a cargar productos escaneando o introduciendo datos manualmente.

    - Cada producto empaquetado se registra bajo un pack específico.
    - Puedes cambiar entre cajas para distribuir los productos según sea necesario.

    !!!Info
        Los packs recién creados no pueden eliminarse manualmente. Sin embargo, si un pack se deja vacío (sin productos añadidos), se eliminará automáticamente al final del proceso. Solo se guardarán y mostrarán los packs con productos empaquetados.

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/packing-mobile-6.png)


#### Métodos de packing

Durante el proceso de packing, el operario debe ceñirse estrictamente a lo que se debe empaquetar; es decir, solo puede escanear los códigos de barras listados en el documento de packing. No se permite sustituir cajas por otras ni cambiar unidades logísticas, ya que los productos ya han sido reservados durante el picking y el packing debe reflejar exactamente lo solicitado.

En cuanto a cómo realizar el packing, el sistema ofrece flexibilidad en los métodos de operación:

- Escanear el producto el número exacto de veces (ej.: 10 escaneos para 10 unidades).
- Cargar la cantidad manualmente en el campo Cantidad y luego escanear el producto.

- Introducir manualmente tanto la cantidad como el código y, a continuación, pulsar el botón Validate para confirmar la entrada.

- Introducir la cantidad manualmente desde la vista **Producto** o desde la vista **Packs**.

!!! Warning

    Posibles escenarios de error:

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/packing-mobile-7.png){align=right width=200}

    - Si se escanea un código incorrecto (no coincide con ningún producto de la tarea), el campo de código de barras se resalta en rojo, muestra una cruz y no añade cantidad a ningún producto.
    - Si se intenta introducir más cantidad de la requerida, también se muestra un mensaje de error. Si la cantidad se carga manualmente en la tarjeta del producto, el sistema permite cargar la cantidad máxima solicitada.

    En ambos casos, el mensaje de error mostrado es el que se visualiza en la imagen.

#### Finalización del packing

Una vez que los productos han sido empaquetados:

- El sistema muestra un resumen por pack con los productos incluidos y se muestra el mensaje *Packing completed successfully*.

- Hasta que se confirme, el contenido de las cajas puede editarse.

- Al final, puedes elegir calcular el peso de las cajas.

- Tras la confirmación, la tarea se marca como Completada.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/packing-mobile-8.png)

Una vez completada, la tarea aparecerá en la sección de Tareas completadas. Desde allí, es posible revisar toda la información validada para esa tarea de packing, incluyendo:

- En la vista Producto: en qué cajas se empaquetó cada producto.
- En la vista Pack: qué productos se empaquetaron en cada pack.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/packing-mobile-9.png)

### Tareas de reubicación

Las tareas de reubicación permiten mover productos desde su ubicación original a su destino dentro del mismo almacén. Cada tarea se muestra en formato tarjeta, donde se puede confirmar o ajustar la cantidad movida y la ubicación destino. La información introducida se sincroniza con el ERP al final de la tarea, garantizando la consistencia entre el movimiento registrado y el stock.

!!!Info
    Para más información sobre cómo usar esta funcionalidad en Etendo, visita [Movimiento entre almacenes](../../../basic-features/warehouse-management/transactions.md#goods-movement).

#### Inicio del proceso (Etendo)

:material-menu: `Aplicación` > `Gestión de Almacén` > `Transacciones` > `Movimiento entre almacenes`

El proceso de reubicación comienza en el ERP desde el botón **Generate Relocation Task** en la ventana Movimiento entre almacenes.

Permite al responsable crear una tarea de reubicación a partir del documento **Movimiento entre almacenes**. El sistema toma la información cargada en el registro y sus líneas y la envía a la aplicación móvil, donde el operario puede ejecutar el movimiento desde la subaplicación correspondiente. Al pulsarlo, se abre un pop-up para asignar la tarea manual o automáticamente y definir su prioridad.

![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/generate-relocation-task.png)

El uso del botón **Generate Relocation Task** está sujeto a una validación del sistema que determina su disponibilidad. Solo se muestra cuando el documento *Movimiento entre almacenes* no ha sido procesado y no tiene ya una tarea asignada.

#### Acceso a las tareas de reubicación (Etendo Mobile)

Al acceder a Etendo Mobile en la sección Tareas de reubicación, se mostrarán todas las tareas y sus estados y prioridades correspondientes pertenecientes al usuario que ha iniciado sesión. Por defecto, las tareas se muestran como Pendiente.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/relocation-tasks-1.png)

Para realizar una **reubicación**:

- Accede al menú **Tareas de reubicación**. Allí, las tareas se dividen por estado: *Pendiente*, *En curso*, *Completada*.
- Busca y selecciona la tarea desde la lista o usando el buscador.
- Al seleccionar una tarea, se abre una pantalla con la información de la tarea.
- Pulsa el botón **Start Relocation**.
- Completa el campo **Counted Quantity**.
- Completa el campo **To Locator**. (Opcional)
- Confirma la tarea con el botón **End Relocation**.
- Confirma que deseas finalizar la tarea.
- Ver mensaje de éxito.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/relocation-tasks-2.png)

### Tareas de ajuste

Las tareas de ajuste de inventario permiten a los operarios de almacén realizar recuentos físicos y ajustes de stock directamente desde la app móvil. Estas tareas se generan a partir de inventarios físicos en el sistema ERP.

Esta funcionalidad corresponde a la misma operación realizada en la ventana **Inventario físico** de Etendo: registrar la cantidad real contada de un producto y actualizar el stock en consecuencia, ya sea corrigiendo cantidades existentes o introduciendo stock donde antes no lo había. Cuando el estado de inventario cambia durante el proceso de ajuste, el sistema mueve automáticamente el/los producto(s) a los huecos asociados al nuevo estado, reflejando con precisión la condición actual del stock.

!!!Info
    Para más información sobre cómo usar esta funcionalidad en Etendo, visita [Inventario físico](../../../basic-features/warehouse-management/transactions.md#physical-inventory).


#### Inicio del proceso (Etendo)

:material-menu: `Aplicación` > `Gestión de Almacén` > `Transacciones` > `Inventario físico`

El proceso comienza creando tareas dentro de Etendo usando la ventana **Inventario físico**. Se crea un nuevo registro con líneas de producto para las que se desea verificación y ajuste de stock. Una vez listo, la tarea debe generarse usando el botón **Generate Task**.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inventory-task-window-1.png)

#### Acceso a las tareas de ajuste (Etendo Mobile)

Al acceder a Etendo Mobile en la sección Tareas de ajuste, se mostrarán todas las tareas y sus estados y prioridades correspondientes, pertenecientes al usuario que ha iniciado sesión. Por defecto, las tareas se muestran con estado *Pendiente*.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inventory-tasks-mobile.png)

Para **ajustar** inventario

- Desde el menú principal de Etendo Mobile, navega a la sección **Tareas de ajuste**. Las tareas se organizan por estado: *Pendiente*, *En curso* y *Completada*.
- Busca y selecciona la tarea deseada desde la lista o usando la función de búsqueda.
- Al seleccionar una tarea, se abre una pantalla que muestra la información de la tarea.
- Pulsa el botón **Start Adjustment** para iniciar el proceso.
- Introduce la información relevante, incluyendo detalles del hueco y recuentos de cantidad.
- Escanea productos para ubicarlos en stock o introduce los datos manualmente.
- Confirma la tarea pulsando el botón **End Adjustment**.
- Confirma que deseas completar la tarea.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inventory-tasks-status-1.png)

### Tareas de inspección de calidad

Las tareas de inspección de calidad permiten a los operarios de almacén realizar la verificación de calidad del producto directamente desde Etendo Mobile. Estas tareas permiten inspeccionar mercancía, registrar resultados de inspección y actualizar el estado de inventario en función de la condición del producto, garantizando que solo los artículos aprobados por calidad estén disponibles para la venta o para su procesamiento posterior.

!!!Info
    Para más información sobre cómo usar esta funcionalidad en Etendo, visita [Inventory Quality Inspection](#inventory-quality-inspection).

#### Inicio del proceso (Etendo)

El proceso comienza en Etendo creando tareas desde la ventana **Inventory Quality Inspection**. Tras crear un documento de inspección con líneas de producto que requieren verificación de calidad, utiliza el botón **Generate Task** para crear una tarea móvil.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inventory-quality-inspection-generate-task.png)

#### Acceso a las tareas de inspección de calidad (Etendo Mobile)

Al acceder a Etendo Mobile en la sección **Tareas de inspección de calidad**, se mostrarán todas las tareas y sus estados correspondientes pertenecientes al usuario que ha iniciado sesión. Por defecto, las tareas se muestran con estado *Pendiente*.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/quality-inspection-task-mobile-0.png)

Para realizar una **inspección de calidad**:

1. Desde el menú principal de Etendo Mobile, navega a la sección **Tareas de inspección de calidad**. Las tareas se organizan por estado: *Pendiente*, *En curso* y *Completada*.

2. Busca y selecciona la tarea deseada desde la lista o usando la función de búsqueda.

3. Al seleccionar una tarea, se abre una pantalla que muestra la información de la tarea y las líneas de producto a inspeccionar.

4. Pulsa el botón **Start Inspection** para iniciar el proceso de control de calidad.

5. Los productos pueden escanearse usando el lector de códigos de barras o introducirse manualmente. Para cada línea de producto, completa los detalles de inspección:
    - Selecciona el **To State** (estado destino según los resultados de la inspección: *Available*, *Damaged*, *Blocked*, etc.)
    - Verifica el producto y sus atributos (lote, fecha de caducidad, etc.)
    - Introduce la **Cant.total** (cantidad real inspeccionada)
    - Opcionalmente, añade notas o motivos de rechazo en el campo **Descripción**

6. Una vez inspeccionados todos los productos, confirma la tarea pulsando el botón **End Inspection**.

7. Confirma que deseas completar la tarea.

8. Se mostrará un mensaje de éxito y los resultados de la inspección se sincronizarán con Etendo.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/quality-inspection-task-mobile-1.png)

!!!note
    Cuando se completa la inspección, el sistema actualiza automáticamente el estado de inventario y aplica las [Movement Rules](#movement-rules-configuration-window) si están configuradas. Los productos marcados con un estado diferente se reubicarán en consecuencia, o se creará un hueco virtual si no se define una ubicación específica para ese estado.

### Todas las tareas

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/all-tasks.png)

Desde esta ventana puedes ver y trabajar con todos los tipos de tareas, como Picking, Packing y tareas de inventario.


---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.