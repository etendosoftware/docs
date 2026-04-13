---
title: Gestión avanzada de almacén
tags:
    - Gestión de Almacén
    - Avanzado
    - Recepción
    - Inventario
    - Stock
    - Etendo Mobile
---

# Gestión avanzada de almacén
:octicons-package-16: Paquete Java: `com.etendoerp.advanced.warehouse.management`
## Visión general

El módulo **Advanced Warehouse Management** amplía las capacidades estándar de Etendo para ofrecer una gestión de inventario integral, flexible y automatizada, añadiendo integración con dispositivos móviles. Cada acción realizada desde Etendo Mobile se sincroniza automáticamente con Etendo, garantizando una trazabilidad completa y actualizaciones coherentes en las ventanas correspondientes del sistema.

Este módulo permite al usuario:

- Gestionar el inventario en múltiples estados predefinidos y personalizados.
- Realizar ajustes de existencias e inventarios físicos desde dispositivos móviles.
- Automatizar reubicaciones y estados mediante reglas de movimiento.
- Integrar la trazabilidad mediante códigos de barras, que pueden escanearse desde Etendo Mobile.
- Ampliar y optimizar el proceso manual de picking y packing, incorporando la posibilidad de ejecutarlos desde Etendo Mobile.
## Configuración inicial

Para empezar a utilizar este módulo correctamente, deben completarse los siguientes pasos de instalación y configuración:

- [x] Instalar el bundle **Warehouse Extensions**.
- [x] Instalar la app **Etendo Mobile**.
- [x] Habilitar la **Advanced Warehouse App** para los roles de usuario que la utilicen.
- [x] Instalar datasets.
- [x] Configurar los parámetros clave en la ventana **Advanced Warehouse Configuration**.
- [x] Deben crearse los tipos de tarea necesarios para picking y packing.
- [x] Debe definirse la opción de generación de picking a nivel de **Pedido de venta**.

**Pasos a seguir:**

1. Instale el módulo **Advanced Warehouse Management**, parte de **Warehouse Extensions Bundle**.
    
    !!! info
        Para poder incluir esta funcionalidad, debe instalarse el Warehouse Extensions Bundle. Para ello, siga las instrucciones del marketplace: [_Warehouse Extensions Bundle_](https://marketplace.etendo.cloud/?#/product-details?module=BAE67A5B5BC4496D9B1CA002BBCDC80E){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Warehouse Extensions - Notas de la versión](../../../../../whats-new/release-notes/etendo-classic/bundles/warehouse-extensions/release-notes.md).

2. Instale **Etendo Mobile** en un dispositivo Android o iOS y siga los pasos de configuración inicial. Para ello, siga las instrucciones en [Primeros pasos - Etendo Mobile](../../../../etendo-mobile/getting-started.md)

    !!! tip
        Asegúrese de seguir todos los pasos para habilitar la **Advanced Warehouse App**.

3. Instalar datasets

    :material-menu: `Aplicación`>`Configuración General` > `Organización` > `Gestión del módulo de Empresa`
    
    Desde la ventana [Gestión del módulo de Empresa](../../../basic-features/general-setup/enterprise-model/enterprise-module-management.md) es necesario para todos los roles que vayan a utilizar esta funcionalidad.

    Estos datos de referencia incluyen configuraciones necesarias para utilizar estos módulos. 

    - `Warehouse Packing`
    - `Warehouse Picking List`
    - `Advanced Warehouse Management`
    - `Etendo Print Provider`
    - `Stock Logistic Unit`

    ![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/dataset.png)

4. Ventana **Advanced Warehouse Configuration**

    :material-menu:`Aplicación` > `Gestión de Almacén` > `Configuración` > `Advanced Warehouse Configuration`

    Antes de utilizar el módulo, en la ventana `Advanced Warehouse Configuration`, debe configurar las variables clave que definen cómo se gestionan las operaciones de inventario para cada organización.

    !!! warning
        Es obligatorio crear una configuración para la organización con la que esté trabajando.

    ![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/advanced-warehouse-configuration.png)
    
    Campos a tener en cuenta:

    **Cabecera**

    - **Organización**: permite gestionar a qué organización se aplicará la configuración.
    - **Almacén**: es un campo no obligatorio que puede utilizarse para aplicar la configuración a un almacén específico o a todos los almacenes de la organización.
    - **Activo**: se marca o desmarca para habilitar o deshabilitar la configuración.
    - **Configuración de código de barras**

        - **Algoritmo de código de barras**: el algoritmo de código de barras por defecto que permite la interpretación según cualquiera de los estándares definidos por organizaciones internacionales. Las opciones a seleccionar son:

            - [GS1-128](https://www.gs1.org/standards/barcodes){target="_blank"}
            - SimpleBarcode

        - **Configuración de componentes de código de barras**: conjunto de identificadores de aplicación definidos por estándares del sector y utilizados en códigos de barras. Estos identificadores permiten al sistema distinguir diferentes tipos de información, ya que cada AI especifica el tipo de dato que le sigue, como identificadores de producto, números de lote, fechas de caducidad o cantidades.  
        Este campo es obligatorio cuando se selecciona uno de los algoritmos por defecto del módulo (GS1-128 o Simple Barcode). Para algoritmos personalizados definidos por el usuario, este campo puede dejarse en blanco; sin embargo, el sistema mostrará un mensaje de advertencia si permanece vacío. En todos los casos, la configuración de AI es editable.

    Solapa **Preferencias**

    Esta solapa permite crear, editar y eliminar registros de preferencias. Los registros heredan automáticamente el Cliente y la Organización de la cabecera, y estos campos no son editables. Los campos de la solapa replican los disponibles actualmente en la ventana `Configuración General` > `Aplicación` > `Preferencias`.

    Opciones como **Buscar código de barras relacionado**, **Picking – Validación exacta de atributos**, y las preferencias para **Habilitar reservas de existencias** y **Habilitar gestión de unidades de medida** pueden gestionarse como preferencias directamente desde esta solapa.

    **Tabla de preferencias**

    La siguiente tabla resume las preferencias clave disponibles en la configuración avanzada de almacén:

    | Nombre de preferencia | Descripción | Opciones | Valor por defecto |
    |-----------------------|-------------|---------|-------------------|
    | **Picking – Validación exacta de atributos** | Define el nivel de validación aplicado durante el proceso de picking. | **Y**: Requiere coincidencia exacta entre el código escaneado y la lista de picking (producto, atributos y hueco).<br>**N**: Valida solo el producto, sin coincidencia estricta de atributos ni de hueco. | *Y* |
    | **Buscar código de barras relacionado** | Permite a Etendo buscar un producto utilizando múltiples códigos de barras. | **N**: Busca solo el código de barras principal en el campo **UPC/EAN** del producto.<br>**Y**: Busca tanto el código de barras principal como todos los códigos de barras adicionales en la solapa **Código de barras**. | *N* |
    | **Habilitar reservas de existencias** | Habilita o deshabilita la funcionalidad de reserva de existencias. | **Y**: Activa las reservas de existencias.<br>**N**: Desactiva las reservas de existencias. | *N* |
    | **Habilitar gestión de unidades de medida** | Habilita o deshabilita la gestión de unidades alternativas de medida. | **Y**: Activa la funcionalidad de AUOM.<br>**N**: Desactiva la funcionalidad de AUOM. | *N* |
    | **Crear tareas de almacén** | Habilita la generación automática de tareas de almacén (p. ej., tareas de picking) durante la creación de la lista de picking. Cuando está deshabilitado, las tareas no se generan automáticamente y la asignación no está disponible. | **Y**: Genera automáticamente tareas de almacén.<br>**N**: No genera tareas automáticamente. | *Y* |
    | **Días desde la fecha completada de la tarea** | Define cuántos días hacia atrás desde la fecha actual muestra Etendo Mobile las tareas con estado Completada. | Valor numérico que representa el número de días. | *1* |



5. Ventana **Barcode Components Configuration**
    
    :material-menu:`Aplicación` > `Gestión de Almacén` > `Configuración` > `Barcode Components Configuration`

    Esta ventana forma parte de los **ajustes avanzados de código de barras** del sistema Etendo y se utiliza para gestionar y configurar diferentes tipos de códigos de barras. Permite al sistema leer y asociar los códigos escaneados con los productos y su información relevante.

    Permite a los usuarios definir, configurar y aplicar sus propios identificadores para que el sistema pueda leer y asociar diferentes **atributos de producto**, como color, tipo de embalaje, lote o cualquier otro dato relevante, directamente desde los códigos **GS1-128** utilizados en operaciones logísticas.

    !!! tip 
        Las configuraciones que se muestran a continuación están predefinidas en el dataset inicial, aunque pueden modificarse o pueden añadirse nuevos esquemas o tipos de código de barras.
    
    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/barcode-components-configuration-win-1.png)

    !!! note

        El sistema permite configurar libremente cualquier **identificador de aplicación (AI)** para asociarlo a atributos o campos personalizados, proporcionando flexibilidad para adaptarse a diferentes esquemas internos de codificación. El módulo se instala con una configuración predefinida basada en el estándar **GS1-128**, lo que garantiza la correcta interpretación de los códigos conforme a estándares internacionales. No obstante, los usuarios pueden ajustar o redefinir los identificadores según sus necesidades particulares. En tales casos, el sistema interpretará los códigos según la configuración definida por el usuario, pero no interpretará los códigos GS1-128 de la forma estándar.

    Campos a tener en cuenta:

    **Cabecera**

    - **Nombre**: nombre descriptivo de la configuración de código de barras para identificarla fácilmente.  
    - **Descripción**: detalles adicionales sobre el propósito o alcance de esta configuración.  
    - **Separador**: carácter utilizado para delimitar campos de longitud variable en el código, normalmente **FNC1**.  
    - **Aplicar a todos los separadores**: casilla de verificación. Si está marcada (Sí), el separador configurado se añade al final de cada identificador — tanto los AI de longitud fija como los de longitud variable deben terminar con el separador. Si está desmarcada (No), el separador se aplica solo a los identificadores de longitud variable.
    
    Solapa **Líneas de componentes de código de barras**

    - **AI**: código de Identificador de Aplicación definido por GS1 (p. ej., 01 para GTIN, 17 para fecha de caducidad).
    - **Descripción**: explicación de la información que representa el AI (p. ej., identificador de producto, número de lote).
    - **Longitud fija**: indica si la longitud del dato es siempre fija según el *estándar GS1* para ese AI.
   - **Longitud**: (Obligatorio) número esperado de caracteres para AI de longitud fija, o longitud máxima para AI de longitud variable.
    - **Prioridad**: define el orden de lectura cuando hay múltiples identificadores presentes, asegurando que el sistema interprete el código de barras correctamente.  
    - **Entidad**: selector de tipo de entidad. Las opciones son: **Atributo, Hueco, Línea de pedido, Línea de inventario físico, Producto, Inventario de referencia, Línea de envío/recepción**. 
        
        Si se selecciona **Producto**, se habilitan opciones rápidas por defecto mediante casillas de verificación para definir *Lote*, *Número de serie* o *F. caducidad*. Además, puede definirse un valor desde el *Campo de entidad*, que lista los diferentes atributos disponibles para el producto. Cada una de estas opciones es única y no puede combinarse con las demás.

        - **Campo de entidad**: selector de campos disponibles para la entidad seleccionada para asignar el valor del código de barras. Las opciones dependen de lo introducido en Entidad.
        - **Lote**: marque para indicar que el atributo es de tipo lote.
        - **Nº de serie**: marque para indicar que el atributo es de tipo número de serie. 
        - **F. caducidad**: marque para indicar que el atributo es de tipo fecha de caducidad.

    Por defecto, al instalar el dataset, el módulo **incluye dos métodos principales para el reconocimiento de códigos**:

    === ":material-playlist-plus: GS1-128"
        
        El estándar [GS1-128](https://www.gs1.org/standards/barcodes){target="_blank"} es un formato de código de barras utilizado globalmente que codifica información estructurada mediante **Identificadores de Aplicación (AIs)**. Cada AI especifica el tipo de dato incluido, como identificadores de producto, números de lote, fechas de caducidad o detalles logísticos. Esto permite una interpretación detallada y estandarizada de la información de producto y almacén. Para más detalles, consulte la [documentación oficial de GS1-128](https://www.gs1.org/standards/barcodes){target="_blank"}.
        
        !!! info 
            Tal como se indica en el estándar, al utilizar un identificador de longitud variable debe añadirse un separador. El valor declarado por el estándar es **FNC1**
                            
        Esta configuración permite el reconocimiento de diferentes Identificadores de Aplicación (AIs) utilizados en procesos de almacén. Los principales códigos implementados son:

        | Código AI  | Descripción                          | Detalles                                                                 | Tipo de longitud   |
        |-----------|--------------------------------------|-------------------------------------------------------------------------|-------------------|
        | **(01)** | GTIN (Global Trade Item Number)      | Identifica globalmente un producto comercial mediante un código de 14 dígitos. | Longitud fija     |
        | **(10)** | Número de lote                       | Garantiza la trazabilidad en procesos de fabricación y distribución.    | Longitud variable |
        | **(17)** | Fecha de caducidad                   | Indica la fecha de caducidad del producto en formato YYMMDD.            | Longitud fija     |
        | **(21)** | Número de serie                      | Número de serie único de un artículo.                                   | Longitud variable |
        | **(91)** | Código de hueco                      | Identifica la ubicación específica dentro del almacén.                  | Longitud variable |
        | **(92)** | Unidad logística                     | Identifica una unidad logística, como un palé o una caja.               | Longitud variable |
        | **(93)** | Uso libre                            | -                                                                       | -                 |
        | **(94)** | Uso libre                            | -                                                                       | -                 |
        | **(95)** | Uso libre                            | -                                                                       | -                 |
        | **(96)** | Uso libre                            | -                                                                       | -                 |
        | **(97)** | Uso libre                            | -                                                                       | -                 |
        | **(98)** | Uso libre                            | -                                                                       | -                 |
        | **(99)** | Uso libre                            | -                                                                       | -                 |

        Gracias a esta configuración, al escanear un código de barras *GS1-128*, se interpreta la información relevante y se aplica al proceso en curso (recepción, picking, packing). Por ejemplo, cuando lee un identificador 91, lo asocia a un hueco, o cuando lee un identificador 92, lo asocia a una unidad logística.

        !!! warning "Reglas de identificación de códigos de barras"

            Etendo interpreta únicamente los identificadores definidos en esta configuración.
            Los identificadores GS1-128 90–99 son códigos de uso libre y pueden asignarse a atributos de producto personalizados.

            Por defecto:

            - AI 91 y 92 son utilizados por Etendo.
            - AI 93–99 permanecen disponibles para atributos de producto personalizados que se resuelven dinámicamente (p. ej., 93 = color, 94 = talla).

            Los usuarios pueden cambiar tanto los identificadores como los atributos a los que hacen referencia. Sin embargo, cualquier cambio es responsabilidad del usuario y puede causar inconsistencias con el parseo estándar de GS1-128 o con integraciones externas.

            Si se requiere una interpretación diferente, un desarrollador puede crear un **algoritmo de código de barras** personalizado.

        <figure markdown="span">
            ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/barcode-components-configuration-attr-2.png)
            <figcaption> Ejemplo: configuración de entidad de producto personalizada</figcaption>
        </figure>
    
        !!! info "Restricciones y validaciones de configuración"
    
            - Al crear o modificar identificadores (AI), el sistema aplica una serie de validaciones diseñadas para mantener la consistencia y unicidad de las configuraciones.
            - Cada AI debe ser único. No puede haber más de un registro con el mismo número de AI, independientemente de la entidad o del campo asociado.
            - Cuando un AI se asocia a un tipo específico de información como Lote, F. caducidad o Número de serie, ese tipo no puede repetirse dentro de la misma configuración.
            - El sistema permite la inclusión de atributos personalizados en códigos de barras. Durante el escaneo, estos atributos se interpretan dinámicamente como **identificadores adicionales de producto**, junto con los valores estándar, permitiendo la validación y distinción de un producto único.

    === ":material-playlist-plus: Coincidencia directa de cadena"

        Este método permite al sistema leer el código y compararlo exactamente con los códigos de los productos almacenados en el sistema. La comparación es directa y estricta, sin tener en cuenta ninguna estructura adicional en el código.    

        ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/ai-config-direct-1.png)


6. Infraestructura de **Mantenimiento**:

    El módulo [Mantenimiento](../platform-extensions/task.md), instalado automáticamente como dependencia, gestiona eventos y desencadena la creación de tareas y acciones tras cambios dinámicos, habilitando la automatización de flujos de trabajo.

    En concreto, se utiliza al crear una lista de picking.

    !!! warning "Obligatorio"
        Un desarrollador debe completar la configuración inicial descrita en [Mantenimiento - Configuración inicial](../../../../../developer-guide/etendo-classic/bundles/platform/task.md#initial-configuration) para utilizar este módulo.

    Cuando se instala el módulo Advanced Warehouse Management, los Tipos de tarea necesarios para picking y packing desde Etendo Mobile se incluyen por defecto:

    ![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/task-type.png)

    **Algoritmo de usuario**

    Cada Tipo de tarea permite seleccionar el algoritmo de asignación del operario de almacén. Por defecto, se utiliza el algoritmo Round-Robin.

    **Preferencias del sistema**

    Las preferencias `Create Warehouse Task` y `Task From Date Completed Days`, disponibles en la solapa *Preferencias*, se relacionan con la funcionalidad de tareas: `Create Warehouse Task` habilita la creación automática de tareas cuando se completa un picking, y `Task From Date Completed Days` define el número de días por defecto para mostrar tareas completadas.
## Configuración de datos maestros

### Creación de estados de inventario  

`Aplicación` > `Gestión de Almacén` > `Configuración` > `Estado de Inventario`

Los estados de inventario permiten al usuario clasificar y gestionar las unidades de stock según su condición o disponibilidad operativa. El sistema incluye algunos estados predefinidos (como *Bloqueado*, *Dañado*, *En control de calidad*, etc.), pero es posible crear nuevos estados personalizados como `Administrador del sistema` según las necesidades del cliente.

!!!info
    Para más información sobre cómo configurar los estados de inventario, visite [Estado de Inventario](../../../../../developer-guide/etendo-classic/concepts/inventory-status.md).

El nuevo estado estará disponible en **Etendo Mobile** para asignarse a huecos nuevos o existentes mediante las opciones de Mantenimiento **Ajustar** o **Reubicar**. En este último caso, se utilizan las reglas definidas en la ventana `Configuración de reglas de movimiento`, descrita a continuación.

### Ventana Configuración de reglas de movimiento

`Aplicación` > `Gestión de Almacén` > `Configuración` > `Configuración de reglas de movimiento`

Las reglas de movimiento permiten automatizar la reubicación o el cambio de estado del inventario en función de la acción que se esté realizando. El objetivo de esta funcionalidad es automatizar los movimientos de inventario cuando cambian de estado, excluir determinadas ubicaciones de operaciones como el picking o las reservas debido a su estado, evitar errores en la manipulación de productos, gestionar productos especiales (*Dañado*, *Bloqueado*, etc.) y gestionar automáticamente ubicaciones virtuales cuando no existe un destino definido.

Un **Hueco virtual** es una ubicación generada automáticamente por el sistema para mantener correctamente el inventario, incluso cuando no se ha definido una ubicación específica para el estado al que se está moviendo. 

!!! Example
    Si el estado *Disponible* no tiene un hueco asociado, y un usuario marca un producto como *Dañado*, entonces el sistema crea una ubicación virtual en la que depositar el inventario afectado. Esta ubicación virtual hereda las propiedades del hueco donde se encontraba el producto y se asocia exclusivamente al nuevo estado (p. ej., *Disponible*).

Esto permite al usuario mantener la trazabilidad y la consistencia del inventario, incluso si el equipo aún no ha definido todas las ubicaciones físicas. También agiliza las operaciones al evitar errores o bloqueos al trabajar con estados excepcionales.

La aplicación de estas reglas puede verse desde dos funcionalidades de Etendo Mobile:

- Desde las tareas **Reubicar**, una vez que haya seleccionado la ubicación definida en una regla, esto moverá el inventario a la nueva ubicación y, según la regla configurada, cambiará el estado del inventario.

- Desde las tareas **Ajustar**, cuando seleccione el nuevo estado, esto actualizará el estado y, en función de la regla configurada, moverá el inventario a la ubicación definida.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/movement-rules-config.png)

Campos a tener en cuenta: 

- **Desde el localizador**: ubicación de origen.
- **Hasta el localizador**: ubicación de destino.
- **A estado**: estado al que se transferirá el inventario cuando se realice el movimiento.

!!!Note
    Si el campo **A estado** se rellena primero, el campo **Hasta el localizador** se limitará a los Huecos que tengan asignado ese estado.

!!!Info
    Las acciones realizadas mediante reglas de movimiento impactan tanto en Etendo Mobile como en el **Informe Stock** de Etendo, reflejando la ubicación.

### Código de barras

La funcionalidad de código de barras es clave para las operaciones logísticas. Los huecos y los productos con códigos generados estarán disponibles para ser escaneados y gestionados tanto desde **Etendo Mobile** como desde **Etendo**, pero requiere una configuración previa.

- Debe cargarse el conjunto de datos `Advanced Warehouse Management`.
- Desde la ventana **Configuración avanzada de almacén**, puede definir qué código de barras se utilizará por defecto.

Es posible generar estos códigos únicos para los huecos en las ventanas **Almacén y huecos** y **Producto**:

=== "Desde la ventana **Almacén y huecos**"

    1. Seleccione el **Almacén y hueco**.
    2. Haga clic en **Generar código de barras** y confirme con Hecho.

        ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/barcode1.png)

    3. El código generado se muestra en el hueco en el campo **Código de barras**. También puede cargarse manualmente o modificarse.

        ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/barcode2.png)
    
    4. Por otro lado, puede obtener una impresión del código de barras generado haciendo clic en el botón Generar imprimible. Debe seleccionar un proveedor, la impresora y el número de copias.

        ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/barcode-print-1.png)

    !!! info
        Para utilizar la opción de impresión, debe tener el módulo Print Provider. Para más detalles, consulte [Print Provider](../../../../../user-guide/etendo-classic/optional-features/bundles/platform-extensions/print-provider.md)

=== "Desde la ventana **Producto**"

    1. Seleccione el producto.
    
    2. Haga clic en Generar código de barras y confirme con Hecho.
    
    3. El código generado se muestra en la cabecera de la ventana de producto en el campo **UPC/EAN**. También puede cargarse manualmente o modificarse.

        ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/barcode4.png)
    
    4. Puede obtener una impresión del código de barras generado haciendo clic en el botón *Generar imprimible*. Debe seleccionar un proveedor, la impresora y el número de copias.
    
        ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/barcode-print-2.png)

        !!! info
            Para utilizar la opción de impresión, debe tener el módulo Print Provider. Para más detalles, consulte [Print Provider](../../../../../user-guide/etendo-classic/optional-features/bundles/platform-extensions/print-provider.md)
    
    !!! info 
        En la ventana **Producto**, existe una solapa llamada **Código de barras**, donde se listan varios códigos de barras asociados al producto, como los códigos de proveedor. Estos códigos se cargan manualmente, permitiendo especificar el algoritmo utilizado para cifrar el código y la configuración del Identificador de aplicación.
        
        Para configurar cómo el sistema busca códigos de barras:
        
        - En la ventana **Configuración avanzada de almacén**, existe una casilla de verificación denominada `Buscar código de barras relacionado`
        - Si la casilla está habilitada, al escanear un producto desde Etendo Mobile, el sistema buscará coincidencias en todos los códigos listados en la solapa Código de barras, además del código de la cabecera.
## Recepción de entrada

### Visión general

<iframe width="560" height="315" src="https://www.youtube.com/embed/8GvCIj_a0c8?si=lUPwXGKvVXCQBf-O" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

La funcionalidad de [Inventario referenciado (RI)](../../../basic-features/warehouse-management/transactions.md#referenced-inventory) se ha ampliado para gestionar unidades logísticas físicas como **palés** y **cajas**, vinculadas directamente a las [Unidades alternativas de medida (AUOM)](../../../basic-features/master-data-management/master-data.md#alternate-uom-tab) de cada producto. Esto permite definir equivalencias (p. ej., 1 Palé = 100 unidades) y gestionar estas unidades como entidades únicas y trazables en las operaciones de almacén.

El módulo [Stock Logistic Unit](./stock-logistic-unit.md), instalado como dependencia, añade nuevas unidades (Caja, Palé) y tipos de inventario referenciado, permitiendo a los usuarios configurar equivalencias en la solapa **Unidad Alternativa** de la ventana Producto. Una vez definidas, si se requiere una conversión diferente, debe crearse una nueva AUOM.

Cuando se reciben mercancías, el sistema puede generar automáticamente registros de RI para cada unidad logística (Caja o Palé), incluyendo los detalles del producto, la cantidad en unidad base y atributos como lote o fecha de caducidad. Cada unidad se registra como un elemento único desde el momento en que entra en el almacén, garantizando una trazabilidad completa.  

!!! info
    Para una configuración y uso detallados de las unidades logísticas, consulte la documentación de [Stock Logistic Unit](./stock-logistic-unit.md).

### Ventana Recepción de entrada  

:material-menu: `Aplicación` > `Gestión de Compras` > `Transacción` > `Recepción de entrada`

La ventana **Recepción de entrada** mejora el flujo de [albarán](../../../basic-features/procurement-management/transactions/goods-receipt.md) introduciendo un paso intermedio entre el pedido de compra y el albarán. Este paso centraliza múltiples pedidos—even from different suppliers—into a single operation, improving flexibility, automation, and control. It also supports alternative units of measure (AUOM), enabling receipts to be recorded in pallets, boxes, or regrouped into different containers to reflect the actual inflow.

Receipts are always created from purchase orders, not manually. Order lines are loaded with product, quantity, lot, and location details, which can be adjusted (e.g., quantity or unit) to register partial or alternative receipts. This ensures the goods receipt accurately reflects what was physically received and updates the purchase order accordingly.

When AUOMs such as Pallet or Box are used, the system can automatically generate a Referenced Inventory (RI) record linked to the receipt line, representing the logistics unit and ensuring traceability.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inbound-receipt-window-0.png)

Fields to note:

#### Header

- **Organization**: Defines the organization in which the inbound receipt will be created and filter the information.  
- **Document Type**: Loaded by default with *Inbound Receipt* to classify the document type.  
- **Document No**: Unique identifier automatically generated for the receipt, with a sequence specific to this type of document.  
- **Movement Date**: Date on which the physical goods movement is recorded. By default, it is the current date.  
- **Description**: Free text field to add additional information or notes about the receipt.  


#### Lines Tab

The Lines Tab allows you to add and modify individual products from one or more purchase orders, adjusting their quantity and/or unit. It represents the list of products received, displaying the following fields in addition to the basic ones.

![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inbound-receipt-window-1.png)

Fields to note:

- **Line No**: Sequential number automatically assigned to identify the line within the receipt.  
- **Product**: The product being received, linked to the purchase order.  
- **Operative Quantity**: Quantity received expressed in the product's alternative unit of measure. Matches the Ordered Quantity if no AUOM is defined. If an AUOM exists, it indicates the number of pallets, boxes, or other alternative units received.  
- **Alternative UOM**: Alternative unit of measure for the product. If no AUOM is defined, it defaults to the UOM. Used to record the receipt of products in pallets, boxes, or other containers.  
- **Ordered Quantity**: Quantity received expressed in the product's base unit of measure.  
- **UOM**: Base unit of measure of the product (e.g., units, liters, kilograms).  
- **Attribute Set Value**: Attributes associated with the product, such as batch, serial number, or expiration date.  
- **Storage Bin**: Location where the received product will be stored. It can vary between lines, allowing different locations to be assigned to products from the same or different purchase orders.  
- **Purchase Order Line**: Reference to the original purchase order line from which the receipt line was generated.  
- **Grouped by**: Identifier of the grouping to which the line belongs, generated when using the *Group By* button. It shows which lines are part of the same container or packaging unit.  
- **Reference Inventory Type**: Type of referenced inventory associated with the grouping (e.g., Box, Pallet).
- **Goods Receipt Line**: Reference to the goods receipt generated upon completion of the goods receipt.  

#### Available Process

**Create Lines From Order**

Extracts product lines from purchase orders. When clicked, a pop-up shows all available products, even from multiple purchase orders. You can select one or more lines to add to the Lines tab. If a storage bin is defined, it will be assigned to all selected lines; otherwise, it can be set individually per line.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inbound-receipt-create-line-boton.png)

**Create Reference Inventory**

This button appears when at least one line is selected. It allows multiple/mixed grouping into a single type of logistics unit (boxes, pallets, or other types defined in the system). Its function is to gather selected products from the Lines tab into a specific grouping, according to the type of grouping chosen.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inbound-receipt-button-group-1.png)

The grouping is reflected in the Grouped by column of the selected lines (e.g., Box-1).

When the selected elements already belong to logistics units, the button can create a parent logistics unit that contains the selected child logistics units. For example, it is possible to create a pallet that groups previously identified boxes during the reception process. The resulting hierarchy is then reflected in the generated Referenced Inventory, preserving the parent-child relationship and stock traceability.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inbound-receipt-button-group-2.png)

!!! info
    - Only lines from the same Sales Order can be grouped.
    - If a line is already grouped and is included in a new grouping, the previous grouping will be replaced.
    - Child logistics units remain associated with the parent logistics unit created from the button.

!!! warning "Partial grouping"
    If the grouped action includes a line that cannot be nested due to a type incompatibility (e.g., a Pallet inside another Pallet), the system will **not block** the entire receipt. Instead, it processes compatible lines normally and automatically creates a **standalone Referenced Inventory** for the incompatible line. The receipt completes successfully and a **Warning message** is displayed indicating how many lines were processed normally and how many were created as standalone RIs.

**Clear Group By** 

Button allows you to remove a line from your grouping without affecting the rest of the lines in the group.

**Generate Reception Task** 

Allows managing operational receptions from the mobile app through the creation of Reception Tasks. It is available when there is an Inbound Receipt that is not yet completed and has loaded lines.

By pressing the button, a task linked to the selected document is generated and becomes visible in the mobile app and in the Task window of the ERP. 
In the pop-up window, you can assign a user or enable automatic assignment. If multiple records are selected, one task will be created for each record, all assigned to the same user or role defined in the pop-up.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inbound-receipt-popup-1.png)

!!!Info
    For more information, visit [Reception Tasks](#reception-tasks).

**Complete Receipt**

Finishes the receipt, generating and completing the corresponding **goods receipts**. In addition, if the receipt includes products with AUOM (pallet or box), the associated **Inventory Reference** record is automatically created.

**Print Labels**

This button generates barcode labels for **all lines** of the selected Inbound Receipt document.
Each label displays the **GS1-128 barcode** along with human-readable information, including the **product name**, **relevant attributes** (such as lot, expiration date, and serial number when applicable), and the **logistics unit type** (Box or Pallet). If no attributes are defined for a product, the label displays *No attributes*. If no logistics unit applies, the logistics unit line is not shown.

- For **loose products** (without logistics units), the system generates **one barcode label per operative quantity** defined in the receipt line.
  This means that as many labels are printed as units specified in the **Operative Quantity** field.
- For **lines with logistics units (Box or Pallet)** where multiple units are received (for example, 3 boxes), the system generates **one unique barcode label per logistics unit**, since each unit is registered as a unique referenced inventory.
- When products are **grouped into a single logistics unit** using the **Create Reference Inventory** button, the system generates **one single barcode label** for that logistics unit.
  In this case, the label identifies the **logistics unit and its locator**, as it may contain multiple grouped products.

This button is available **only when the Inbound Receipt is completed**.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inbound-receipt-print-header-1.png)

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inbound-receipt-print-header-2.png)

??? example "Print Inbound Receipt - Examples"

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inbound-receipt-print-header-3.png){ width=600 }

    *Label for product **Ale Beer** with all attributes (Lot, Expiration date, and Serial Number) and logistics unit type **Box**.*

    ---

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inbound-receipt-print-header-4.png){ width=600 }

    *Label for a **grouped logistics unit (Pallet)** that can contain multiple different products — no product name or attributes are shown, only the logistics unit reference.*

    ---

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inbound-receipt-print-header-5.png){ width=600 }

    *Label for product **Lager Beer** without attributes defined — displays "No attributes".*

    ---

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inbound-receipt-print-header-6.png){ width=600 }

    *Label for **loose units** of product **Ale Beer** with attributes (Lot, Expiration date, and Serial Number) — no logistics unit is assigned, so the LU line is not shown.*

    ---

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inbound-receipt-print-header-7.png){ width=600 }

    *Label for product **Ale Beer** with all attributes (Lot, Expiration date, and Serial Number) and logistics unit type **Pallet**.*

**Print Line Label**

This action generates **barcode labels only for the selected line or lines** of the Inbound Receipt.
Each label displays the **GS1-128 barcode** along with human-readable information, including the **product name**, **relevant attributes** (such as lot, expiration date, and serial number when applicable), and the **logistics unit type** (Box or Pallet), following the same display rules as the **Print Labels** button.

The label generation follows the same rules described above, applied **only to the selected line or lines**:

- For **loose products**, one barcode label is generated **per operative quantity** defined in each selected line.
- For **multiple logistics units**, one unique label is generated per logistics unit.
- For **grouped logistics units**, a single label is generated identifying the logistics unit.

This button is available **only when the Inbound Receipt is completed**.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inbound-receipt-print-lines-1.png)

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inbound-receipt-print-lines-2.png)

### Workflow

**Receipt Flow**

1. In the receipt flow, the user has a **Purchase Order** that includes product lines configured with an Alternative Unit of Measure (AUOM) of the Box or Pallet type, with its equivalence previously defined in the product window (for example, 1 Pallet = 100 units). 

    ![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inbound-flow-1.png)

2. From the **Inbound Receipt** window, the user creates a new receipt record using the *Create Lines From Order* button, selecting the Purchase Order as the reference document. The system incorporates the order data, such as the product, quantity (in AUOM), attributes (batch, series), and other associated information. 

    ![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inbound-flow-3.png)

    !!!info "Two Ways to Complete the Receipt"
        At this point, you can choose between two workflows to complete the inbound receipt:
        
        **Option 1: Complete from Etendo (ERP)**  
        Continue with steps 3 and 4 below to complete the receipt directly in the **Inbound Receipt** window by pressing the **Complete Receipt** button.
        
        **Option 2: Complete from Etendo Mobile**  
        Use the **Generate Reception Task** button to create a reception task visible in **Etendo Mobile**. This allows warehouse operators to perform the reception directly from their mobile devices. For more information, visit [Reception Tasks](#reception-tasks).

3. When the Complete button is pressed, the system sequentially generates and completes the **Goods Receipt** and creates a record in **Referenced Inventory (RI)** for each logistics unit received (Box or Pallet), respecting the equivalencies defined in AUOM.

    ![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inbound-flow-2.png)

4. The Referenced Inventory is linked to the quantity received, the product, and its corresponding attributes. As a result, the stock is updated in the inventory, increasing the number of units in the defined location and enabling traceability through the generated RI.

    ![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inbound-flow-4.png)

**Partial Receipt Flow**

1. The partial receipt process begins when there is a **Purchase Order** that contains a product line configured with an AUOM, for example, 1 box of pineapple juice equivalent to 12 units. 
2. From the **Inbound Receipt** window, the user initiates a new receipt record using the *Create Lines From Order* button and selects the Purchase Order as a reference. The system automatically loads the order lines, including the product and expected quantity, such as 1 box.
3. Then, in the receipt line, the user modifies the quantity to reflect the partial receipt; for example, if the order is for 1 box (12 units) but only 6 units are received, the user changes the quantity to 6 and, if necessary, adjusts the unit of measure to **units** instead of **box**.
4. Once the actual quantity received has been adjusted, the user completes the receipt by pressing the *Complete* button in the Inbound Receipts window.
5. At that point, the system generates and completes the goods receipt, reflecting the partial quantity actually received. The inventory is updated with the quantity received. The **Purchase Order** will show the percentage received in the status bar.

## Inventory Quality Inspection

### Overview

The **Inventory Quality Inspection** window enables comprehensive management and control of quality inspection processes within warehouse operations. It serves as a centralized tool to register, audit, and execute quality controls, maintaining full traceability between inspections, assigned operator tasks, and resulting stock movements. This functionality ensures that products meet quality standards before being made available for sale or further processing, preventing defective or non-compliant items from entering the distribution chain.

### Inventory Quality Inspection Window

:material-menu: `Application` > `Warehouse Management` > `Transaction` > `Inventory Quality Inspection`

This window allows users to create and manage quality inspection records for inventory items. Inspections can be conducted on existing stock. The system tracks which products need inspection, their current status, location, and the quantities planned for review.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inventory-quality-inspection-window.png)

Fields to note:

#### Header

- **Organization**: Defines the organization in which the quality inspection will be created and filters the available information.  
- **Document No**: Unique identifier automatically generated for the inspection document, following a specific sequence for this document type.  
- **Name**: A descriptive name for the quality inspection record to help identify its purpose or content.  
- **Quality Control Date**: Date on which the inspection is scheduled or performed. By default, it is the current date.  
- **Description**: Free text field to add additional information or notes about the inspection.

#### Lines Tab

The Lines tab lists the products to be inspected, including their current inventory status, location, and planned inspection quantities. Each line represents a product or batch that requires quality inspection.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inventory-quality-inspection-lines.png)

Fields to note:

- **Line No**: Sequential number automatically assigned to identify the line within the inspection document.  
- **Product**: The product being inspected.  
- **Storage Bin**: Current location of the product in the warehouse.  
- **Book Quantity**: The quantity registered in the system's inventory records for this product at the specified location.  
- **UOM**: Unit of measure of the product (e.g., Unit, Box, Kg).  
- **To State**: Target inventory status to be assigned to the product after inspection (e.g., *Available*, *Damaged*, *Blocked*).  
- **Quantity count**: The actual quantity counted or inspected during the quality control process.  
- **Description**: Free text field to add additional notes or observations about the inspection line.  
- **Movement Line**: Reference to the inventory movement line associated with this inspection, if applicable.

#### Buttons

**Process**

Processes the quality inspection document, validating the inspection data and updating the inventory based on the results recorded in the lines. This button is available when the inspection document has lines.

**Generate Task**

Creates a quality inspection task that is visible in both the **Task** window in Etendo and **Etendo Mobile**. This button is available when the inspection document has loaded lines. 

When clicked, a pop-up window appears where you can assign the task to a specific user or enable automatic assignment based on role. If multiple inspection documents are selected, one task will be created for each, all assigned to the same user or role defined in the pop-up.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inventory-quality-inspection-generate-task.png)

### Workflow

The Inventory Quality Inspection process begins in Etendo when a user creates a new record in the **Inventory Quality Inspection** window.

1. **Create Inspection Document**: A new inspection document is created in the **Inventory Quality Inspection** window with the necessary header information (organization, name, quality control date, description).

2. **Add Products to Inspect**: Products requiring inspection are added to the Lines tab. For each line, specify:
    - The product to be inspected
    - Storage bin location
    - Book quantity (system inventory)
    - Any relevant descriptions or notes

    !!!info "Two Ways to Complete the Inspection"
        At this point, you can choose between two workflows to complete the quality inspection:
        
        **Option 1: Complete from Etendo (ERP)**  
        Continue with steps 3 and 4 below to perform the inspection directly in the **Inventory Quality Inspection** window.
        
        **Option 2: Complete from Etendo Mobile**  
        Use the **Generate Task** button to create a quality inspection task visible in **Etendo Mobile**. This allows warehouse operators to perform the inspection directly from their mobile devices. For more information, visit [Quality Inspection Tasks](#quality-inspection-tasks).

3. **Process Inspection**: 
    - Review each product line and update the **To State** field with the new status for the units, then enter the **Quantity count** for the units that match that status.
    - The system will compare the Book Quantity with the Quantity count to identify discrepancies.
    - Assign the appropriate target status based on inspection results.

4. **Complete the Inspection**: Click the **Process** button to finalize the document. The system will:
    - Update the inventory status of inspected products according to the **To State** field
    - Create inventory movements reflecting the inspection results
    - Handle product relocation based on the target status:
        - If a [movement rule](#movement-rules-configuration-window) exists for the target status, the system applies it automatically
        - If no movement rule exists, the system checks if a storage bin is already assigned to that status
        - If no storage bin is found, the system creates a **virtual storage bin** for the target status to maintain inventory consistency
    - Update the **Stock Report** with the new inventory status

5. All changes are reflected in the system, maintaining full traceability of the quality inspection process.

!!!warning "Movement Rules and Storage Bins"
    It is recommended to configure [Movement Rules](#movement-rules-configuration-window) for commonly used inspection statuses (e.g., *Damaged*, *Blocked*) to maintain proper warehouse organization.
## AUOM Stock Reservation

### Overview

The option of stock reservations based on the unit defined in the sales order (AUOM field) has been added, which determines whether the product is sold in its base unit or in an alternative unit (for example, a single bottle or a box of 12).  

!!! info 
    By default, when the module is installed the preferences `Enable Stock Reservations` and `Enable UOM Management` are enabled. For details, see [Stock Logistic Unit - Preference](./stock-logistic-unit.md#preference).

### Reservation Flow

1. The process starts when a **Sales Order** is created with product lines defined with an Alternative Unit of Measure (AUOM) (e.g., 1 Box = 24 Units).
2. In each line, the **Stock Reservation** field is set to *Automatic*, so the system attempts to reserve stock when the order is confirmed.
    ![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/reservation.png)
3. Reservation logic:

    - The system reserves stock in the unit specified in the order line.  
    - If there is enough stock, a full reservation is created.  
    - If not, it reserves the available quantity in that unit and supplements with other AUOMs or base units.  
    - If the total is covered, the reservation is complete; otherwise, it is partial.
    
    ![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/reservation-1.png)

**Examples**

- Order: 10 units; Stock: 5 units + 1 box of 10 → Only 5 units reserved (the box cannot be split).  
- Order: 110 units; Stock: 100 units + 1 box of 10 → Reservation completed with both.  
- If no stock is available in the requested unit, the system still attempts to reserve using other AUOMs.  

### Picking/Packing Flow

In the [Picking](./picking.md) and [Packing](./packing.md) processes. If the **GS1-128** barcodes are configured,  once a [barcode](#barcode) has been validated, the system can identify not only the product, but also its alternative unit of measure (AUOM) and associated attributes, such as batch or expiration date.

During picking, when the code is scanned, the system interprets the structured information it contains (product, batch, expiration date, etc.) and compares it with the reservation, directly recording the corresponding quantity. This ensures that the stock output exact matches the actual product to be prepared.

In packing, the same validation is used when packaging products. The system recognizes what product it is, in what presentation and with what attributes, and assigns it to the corresponding box. This ensures that the shipment reflects exactly what was picked, maintaining complete traceability.

In this way, the Etendo ensures that a single scan comprehensively recognizes the product that is leaving or will leave, taking into account its alternative measurements and attributes, and avoiding errors throughout the chain from order to dispatch.

!!! Example
    Example of barcode with attributes: **01** 95012345678930 **\x1D** **10**L101 **\x1D** **17** 260910 **91** Rn-0-0-0

    where:

    - \x1D = separator for variable values
    - 01 = product identifier
    - 95012345678930 = id product
    - 10 = lot identifier
    - L101 = lot
    - 17 = expiration identifier
    - 260910 = expiration date (YYMMDD)
    - 91 = locator identifier
    - Rn-0-0-0 = logistic unit code

## Using Etendo Mobile

When logging in to Etendo Mobile, the warehouse operator will be presented with the applications and menus available according to his role.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/advanced-warehouse-management.png)

As seen above, the Advanced Warehouse Management option includes the following menus:

- [Reception Tasks](#reception-tasks)
- [Picking Tasks](#picking-tasks)
- [Packing Tasks](#packing-tasks)
- [Relocation Tasks](#relocation-tasks)
- [Adjustment Tasks](#adjustment-tasks)
- [All Tasks](#all-tasks)
### Reception Tasks

It allows creating and controlling receipts directly from the mobile application using **receipt tasks**, which reproduce the same behavior and process flow as the [Goods Receipt](../../../basic-features/procurement-management/transactions/#goods-receipts) and [Inbound Receipt](#inbound-receipt) windows in the ERP.

#### Process Start (Etendo)

The process begins by clicking the **Generate Receiving Task** button in the *Inbound Receipt* window of the ERP. There, the task is assigned to an operator, the priority is defined, and then it is reflected in the mobile application of the assigned operator.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inbound-receipt-popup-1.png)

#### Access to Reception Tasks (Etendo Mobile)

When accessing **Etendo Mobile** in the **Reception Tasks** section, all tasks and their corresponding statuses belonging to the logged-in user will be displayed. By default, tasks are displayed as *Pending* status.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/reception-mobile-1.png)

**Reception Tasks**

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/reception-mobile-2.png)

To perform a **Reception**:

- Access the **Reception Tasks** menu. There, tasks are divided by status: Pending, In Progress, Completed.
- Search for and select the task from the list or using the search engine.
- When a task is selected, a screen with the task information opens.
- Press the **Start Receipt** button.
- **Scan** the products to stock them or **load** them manually.
- If the product has an **Attribute Set** configured (such as batch number, serial number, expiration date or other custom attributes), a pop-up window will appear requesting this information. Complete the required fields and confirm to continue with the reception.

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/reception-mobile-3.png)

- If needed, the **storage bin (locator)** can be modified to change the destination location of the received products.
- Confirm the task with the **End Reception** button.
- Confirm that you want to finish the task.
- See **Success message**.
### Picking Tasks

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/picking-1.png)

The picking process allows the operator to pick the products required for an order efficiently using Etendo Mobile. The complete process flow is detailed below.

!!!Info
    For more information about how to use this functionality in Etendo, visit [Picking](./picking.md).

#### Process Start (Etendo)

The process is started in Etendo when a [Picking List](picking.md#picking-list-generation) is created from a Sales Order. This can be done using the **Generate Picking List** button available in the Sales Order window, which creates a new **task** that will be assigned to a user for execution in Etendo Mobile.

!!!Important
    Remember the only picking lists that are shown in Etendo Mobile are those marked as **Direct Picking List to Customer** type.

When a picking list is generated, the system runs automatic background processes that vary depending on the configuration. In certain situations, some of these processes can fail without the user noticing immediately.

In order to provide greater visibility, the system displays a **warning message** at different stages of the process, that includes a link to the Task window. From there, the user can check the details of each process executed and review the corresponding logs, ensuring better control over the correct completion of operations.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/message-picking-list-1.png)

The processes that must be verified are as follows:

- For a **Picking tasks with active Packing task creation**:

    - Create Shipment
    - Create Picking List
    - Process Picking List
    - Create Packing Task

- For a **Picking tasks without creating a Packing task**:

    - Create Picking List
    - Create Shipment
    - Process Picking List

Example of logs without errors:

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/message-picking-list.png)

Example of logs with errors:

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/message-picking-list-error.png)

#### Access to Picking Tasks (Etendo Mobile)

When accessing **Etendo Mobile** into the **Picking** section, all tasks and their corresponding statuses and priorities, belonging to the logged in user, will be displayed. By default, the tasks are shown in *Pending* status.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/picking-2.png){align=right width=300}
 
This screen contains:

- Refresh and Back buttons.
- A search field to filter tasks.
- Quick filters that limit between `Pending`, `In Process` or `Completed` tasks.
- A list of cards with tasks. 

!!! Note
    As explained above in the Preference tab section of [Initial Setup](#initial-setup), there is a preference to define the days to show tasks in `Completed` status: `Task From Date Completed Days`. This allows the user to define the number of days backwards, from the current date, to be used as a criterion for displaying tasks in Completed status.

<br clear="all">

#### Product Picking

1. The warehouse operator must select a `Pending` task.

2. Once the task is selected, a window opens with the list of products to be picked.

3. To start the process, click on the **Start Picking** button located at the top; once this is done, the task goes to the `In Progress` status.
    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/picking-3.png)

4. Once picking is started, a new window opens with the following items:

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/picking-4.png){align=right width=300}


    - **Scan Barcode:** activates the camera of the mobile device.
    - **Type barcode:** allows to enter the barcode manually. A Validate button is available to trigger the barcode validation process.
    - **Quantity with: `+` and `-` buttons** allows manual loading of the quantity to be scanned.
    - **List of products (N):** list of cards with product information, where (N) is the total quantity of products. 

        - Product
        - Status:
            - <span style="padding:4px;background-color:#F5F5F5;color:#BDBDBD;border-radius:4px;"> 
                Unscanned
            </span>
            - <span style="padding:4px;background-color:#fba643ff;color:white;border-radius:4px;"> 
                Partially Scanned
            </span>
            - <span style="padding:4px;background-color:#00B34C;color:white;border-radius:4px;"> 
                Scanned
            </span>
        - Barcode
        - Locator
        - Attribute Set Value
        - Movement Quantity: total quantity to be collected.
        - AUOM
        - Counted Quantity with buttons `+` and `-`: that allow to add or subtract one by one the quantity manually.

#### Picking Methods

In the picking process, the operator has flexibility in both what to pick and how to do it. On the one hand, even if the system requests a specific code (for example, box BX100020), it is possible to replace it with another equivalent unit (such as BX100023) as long as the product and quantity match, or to adapt to stock availability (for example, delivering 10 individual units instead of a box of 10). These variations are automatically recorded in the reservation and on the goods sheepment.

On the other hand, the system also allows flexibility in the mode of operation through different selection methods:

- Scan the product the requested number of times (ex: 10 scans for 10 units).
- Scan a logistics unit, which automatically loads the requested quantity along with its equivalent in units according to the conversion rate.    
- Manually load "10" in the quantity field and scan once.
- Enter both code and quantity manually.
- Manually enter only the quantity in the Quantity field within a product card, using the + and - buttons or by entering the number from the keypad.

!!! tip
    When scanning a valid product, the Barcode field is automatically filled in, the associated card is displayed and the value 1 is incremented in the product, if the quantity was not previously changed.

!!! tip
    If a quantity other than the default quantity, e.g. 5, was previously entered in the Quantity field, and then the product is scanned, those 5 units will be added directly to the product card.


!!! Warning
    
    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/picking-5.png){align=right width=200}

    Possible error scenarios:

    - If an incorrect code is scanned (does not match any product in the task), the barcode field is highlighted in red, shows a cross and does not add quantity to any product.   <br><br>
    - If an attempt is made to enter a quantity greater than required, the system will charge the maximum defined in the product card. Once the quantity is completed and the product code is re-scanned or reloaded, the system does not add quantity to the product. If the quantity is manually loaded into the product card, the system allows loading the maximum quantity requested.
    
    In both cases, the error message shown is the one displayed in the image.

    

#### Picking Completion

Once at least one unit of any product is registered, the **End Picking** button becomes active. This allows partial picking, meaning only part of the requested quantity can be picked, which is useful when products are missing or unsuitable for use.

After confirmation, the task is marked as Completed.

!!!warning
    For partial picking, the task is closed, and no new task is automatically created for the missing products. Any remaining quantities must be handled manually.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/picking-6.png)

Once completed, the task will appear in the Completed Tasks section, where it is possible to review the validated products and quantities for that specific picking task.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/picking-7.png)


### Packing Tasks

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/packing-mobile-1.png)

The packing process allows the operator to pack the products efficiently using Etendo Mobile. The complete process flow is detailed below.

!!!Info
    For more information about how to use this functionality in Etendo, visit [Packing](./packing.md).

#### Process Start (Etendo)

Packing tasks are linked to a record in the **Packing** window.  The creation of a packing task is triggered after:

- The completion of a picking task (when the Task Type `Picking and Packing` is active).
- From the **Packing** window of Etendo when adding at least one sales order to a new Packing.

#### Access to Packing Tasks (Etendo Mobile)

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/packing-mobile-2.png){align=right width=300}


When accessing Etendo Mobile and selecting the **Packing** menu, the packing main screen with the number of available `Packing` tasks to the current user. 

This screen contains:

- Refresh and Back buttons.
- A search field to filter tasks.
- Quick filters that limit between `Pending`, `In Progress` or `Completed` tasks. By default it shows the `Pending` filter selected, and in the case of tasks in `Completed` status, there is a preference where it is defined from which day it will bring completed tasks.
- A list of cards, where each card represents a packing task and includes the following information:

    - Packing as title: The document reference is shown.
    - Status.
    - Task Type.
    - Priority.

<br clear="all">

#### Product Packing

1. The warehouse operator must **select a task**. To select the task, scroll or enter key data in the search engine.

2. When selecting a task, a screen opens with the packing list number and the **Start Packing** button.

3. When pressing **Start Packing**, the status of the task changes to `In Progress` in both Etendo Mobile and Etendo. 

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/packing-mobile-3.png)

4. The window has the following elements:

    - **Scan Barcode** button to activate the device camera and scan.
    - **Type barcode** allows to enter the barcode manually. A Validate button is available to trigger the barcode validation process.
    - **Select Pack** field to select the destination pack when scanning the product.
    - **Quantity** field that acts as a multiplier to load the quantity when scanning the product.
    - **+ Add Pack** button that allows you to add new boxes.
    - A list of **Product** cards, each showing:

        - Product
        - Status:
            - <span style="padding:4px;background-color:#F5F5F5;color:#BDBDBD;border-radius:4px;"> 
                Unscanned
            </span>
            - <span style="padding:4px;background-color:#fba643ff;color:white;border-radius:4px;"> 
                Scanning
            </span>
            - <span style="padding:4px;background-color:#00B34C;color:white;border-radius:4px;"> 
                Scanned
            </span>
        - Barcode
        - Locator
        - Attribute Set Value
        - Quantity
        - AUOM
        - Packed Quantity with buttons `+` and `-`: that allow to add or subtract one by one the quantity manually.

    - A list of **Packs**, showing:

        - Pack name (or number)
        - Products and their quantities

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/packing-mobile-4.png)


    The view selectors by **Product** or by **Pack** allow:

    - In the **Products** view, when entering a product card, it shows how that product was distributed in the different boxes, allowing you to browse product by product to review the quantities assigned per pack.

    - In the **Packs** view, when entering a pack, the detailed contents are displayed with the possibility of browsing pack by pack to check which products are contained in each pack.

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/packing-mobile-5.png)

    !!! tip 
        In both views, it is possible to modify the quantities loaded and add packs if necessary. However, in order to be able to assign content to the added boxes, one of the following conditions must be met: 

        - The total load of products has not yet been completed, or previously assigned quantities are modified (decreased) to allow their relocation to the new pack.

5. Once packing is started, the user selects or creates a pack and starts loading products by scanning or manually entering data.

    - Each packed product is registered under a specific pack.
    - You can switch between boxes to distribute products as needed.

    !!!Info
        Newly created packs cannot be deleted manually. However, if a pack is left empty (no products added), it will be automatically removed at the end of the process. Only packs with packed products will be saved and displayed.

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/packing-mobile-6.png)


#### Packing Methods

During the packing process, the operator must strictly adhere to what is to be picked, i.e., they can only scan the barcodes listed on the packing document. It is not permitted to substitute boxes for others or change logistics units, as the products have already been reserved during picking and the packing must reflect exactly what was requested.

In terms of how to perform packing, the system offers flexibility in operating methods:

- Scan the product the exact number of times (ex: 10 scans for 10 units).
- Load the amount manually in the Quantity field and then Scan the product. 

- Enter both quantity and code manually, and then press the Validate button to confirm the entry.

- Enter the quantity manually from the **Product** view or from the **Packs** view.

!!! Warning

    Possible error scenarios:

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/packing-mobile-7.png){align=right width=200}

    - If an incorrect code is scanned (does not match any product in the task), the barcode field is highlighted in red, shows a cross and does not add quantity to any product.
    - If an attempt is made to enter more than the required quantity, an error message is also displayed. If the quantity is manually loaded into the product card, the system allows loading the maximum quantity requested.

    In both cases, the error message shown is the one displayed in the image.

#### Packing Completion

Once the products have been packed: 

- The system displays a summary per pack with the products included and the message *Packing completed successfully* is displayed.

- Until confirmed, the contents of the boxes can be edited.

- At the end, you can choose to calculate the weight of the boxes.

- After confirmation, the task is marked as Completed.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/packing-mobile-8.png)

Once completed, the task will appear in the Completed Tasks section. From there, it is possible to review all validated information for that packing task, including:

- In the Product view: which boxes each product was packed into.
- In the Pack view: which products were packed into each pack.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/packing-mobile-9.png)
### Relocation Tasks

Relocation tasks allow products to be moved from their original location to their destination within the same warehouse. Each task is displayed in card format, where the quantity moved and the destination location can be confirmed or adjusted. The information entered is synchronized with the ERP at the end of the task, ensuring consistency between the recorded movement and the stock.

!!!Info
    For more information about how to use this functionality in Etendo, visit [Goods Movements](../../../basic-features/warehouse-management/transactions.md#goods-movement).

#### Process Start (Etendo)

:material-menu: `Application` > `Warehouse Management` > `Transactions` > `Goods Movement`

The relocation process begins in the ERP from the **Generate Relocation Task** button in the Goods Movements window.

Allows the manager to create a relocation task from the **Goods Movement** document. The system takes the information loaded in the record and its lines and sends it to the mobile application, where the operator can execute the movement from the corresponding sub-application. When pressed, a pop-up opens to assign the task manually or automatically and define its priority.

![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/generate-relocation-task.png)

Use of the **Generate Relocation Task** button is subject to system validation that determines its availability. It is only displayed when the *Goods Movement* document has not been processed and does not have a task already assigned to it.

#### Access to Relocation Tasks (Etendo Mobile)

When accessing Etendo Mobile in the Relocation Tasks section, all tasks and their corresponding statuses and priorities belonging to the logged-in user will be displayed. By default, tasks are displayed as Pending.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/relocation-tasks-1.png)

To perform a **relocation**:

- Access the **Relocation Tasks** menu. There, tasks are divided by status: *Pending*, *In Progress*, *Completed*.
- Search for and select the task from the list or using the search engine.
- When a task is selected, a screen with the task information opens.
- Press the **Start Relocation** button.
- Complete **Counted Quantity** field.
- Complete **To Locator** field. (Optional)
- Confirm the task with the **End Relocation** button.
- Confirm that you want to finish the task.
- See Success message.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/relocation-tasks-2.png)
### Adjustment Tasks

Inventory adjustment tasks allow warehouse operators to perform physical counts and stock adjustments directly from the mobile app. These tasks are generated from physical inventories in the ERP system.

This functionality corresponds to the same operation performed in Etendo's **Physical Inventory** window: recording the actual counted quantity of a product and updating the stock accordingly, either by correcting existing quantities or entering stock where there was none previously. When the inventory status changes during the adjustment process, the system automatically moves the product(s) to the storage bins associated with the new status, accurately reflecting the current stock condition.

!!!Info
    For more information about how to use this functionality in Etendo, visit [Physical Inventory](../../../basic-features/warehouse-management/transactions.md#physical-inventory).


#### Process Start (Etendo)

:material-menu: `Application` > `Warehouse Management` > `Transactions` > `Physical Inventory`

The process begins by creating tasks within Etendo using the **Physical Inventory** window. A new record is created with product lines for which stock verification and adjustment is desired. Once this is ready, the task must be generated using the **Generate Task** button.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inventory-task-window-1.png)

#### Access to Adjustment Tasks (Etendo Mobile)

When accessing Etendo Mobile into the Adjustment Tasks section, all tasks and their corresponding statuses and priorities, belonging to the logged in user, will be displayed. By default, the tasks are shown in *Pending* status.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inventory-tasks-mobile.png)

To **Adjust** inventory

- From the Etendo Mobile main menu, navigate to the **Adjustment Tasks** section. Tasks are organized by status: *Pending*, *In Progress*, and *Completed*.
- Search for and select the desired task from the list or using the search function.
- When a task is selected, a screen opens displaying the task information.
- Press the **Start Adjustment** button to begin the process.
- Enter relevant information including storage bin details and quantity counts.
- Scan products to stock them or manually enter the data.
- Confirm the task by pressing the **End Adjustment** button.
- Confirm that you want to complete the task.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inventory-tasks-status-1.png)
### Quality Inspection Tasks

Quality inspection tasks enable warehouse operators to perform product quality verification directly from Etendo Mobile. These tasks allow operators to inspect merchandise, record inspection results, and update inventory status based on product conditions, ensuring that only quality-approved items are available for sale or further processing.

!!!Info
    For more information about how to use this functionality in Etendo, visit [Inventory Quality Inspection](#inventory-quality-inspection).

#### Process Start (Etendo)

The process begins in Etendo by creating tasks from the **Inventory Quality Inspection** window. After creating an inspection document with product lines requiring quality verification, use the **Generate Task** button to create a mobile task.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/inventory-quality-inspection-generate-task.png)

#### Access to Quality Inspection Tasks (Etendo Mobile)

When accessing Etendo Mobile in the **Quality Inspection Tasks** section, all tasks and their corresponding statuses belonging to the logged-in user will be displayed. By default, tasks are shown in *Pending* status.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/quality-inspection-task-mobile-0.png)

To perform a **quality inspection**:

1. From the Etendo Mobile main menu, navigate to the **Quality Inspection Tasks** section. Tasks are organized by status: *Pending*, *In Progress*, and *Completed*.

2. Search for and select the desired task from the list or using the search function.

3. When a task is selected, a screen opens displaying the task information and product lines to be inspected.

4. Press the **Start Inspection** button to begin the quality control process.

5. Products can be scanned using the barcode scanner or entered manually. For each product line, complete the inspection details:
    - Select the **To State** (target status based on inspection results: *Available*, *Damaged*, *Blocked*, etc.)
    - Verify the product and its attributes (batch, expiration date, etc.)
    - Enter the **Quantity count** (actual quantity inspected)
    - Optionally, add notes or rejection reasons in the **Description** field

6. Once all products have been inspected, confirm the task by pressing the **End Inspection** button.

7. Confirm that you want to complete the task.

8. A success message will be displayed, and the inspection results will be synchronized with Etendo.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/quality-inspection-task-mobile-1.png)

!!!note
    When the inspection is completed, the system automatically updates inventory status and applies [Movement Rules](#movement-rules-configuration-window) if configured. Products marked with a different status will be relocated accordingly, or a virtual storage bin will be created if no specific location is defined for that status.

### All Tasks

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management/all-tasks.png)

From this window you can view and work with all types of tasks, like Picking, Packing and Inventory Tasks.


---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.

---