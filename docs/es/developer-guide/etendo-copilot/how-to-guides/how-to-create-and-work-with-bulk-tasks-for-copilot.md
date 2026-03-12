---
tags:
    - How to
    - Copilot
    - Bulk
    - Mantenimiento
---

# Cómo crear y trabajar con tareas masivas para Copilot

## Visión general

Este artículo explica cómo crear y trabajar con tareas masivas para Copilot. Esto resulta útil cuando desea crear múltiples tareas a la vez y ejecutarlas en segundo plano con Copilot.

### Concepto y casos de uso
Cuando necesita utilizar un agente de IA para realizar tareas con un alto volumen de iteraciones, estará limitado en la cantidad que puede manejar y en su velocidad. Entonces nace el concepto de tareas masivas, que consiste en almacenar solicitudes en una ventana del módulo `Mantenimiento`. 

!!!warning
    Es necesario considerar que estas tareas deben estar *aisladas* entre sí. Es decir, no necesitan información unas de otras. Por ejemplo, al cargar datos desde un archivo de Excel, cada fila se ejecutará por separado.

Estas solicitudes pueden ejecutarse manualmente o procesarse en un proceso en segundo plano ya incluido en el módulo Copilot.

## Añadir tareas de Copilot
El módulo Etendo Copilot incluye:

- **Botón Añadir tarea de Copilot**: Este botón en la ventana `Mantenimiento` le permite enviar un archivo CSV/XLSX/ZIP para crear tareas masivas.
- **Creador de tareas masivas**: Este agente está configurado con la herramienta [Task Creator Tool](../available-tools/task-creator-tool.md) para crear tareas masivas basadas en un archivo zip o en un archivo CSV/XLSX. Este agente puede añadirse a un agente supervisor para encadenarlo con otros agentes.

En ambas opciones, los requisitos son los mismos:

- **Archivo CSV/XLSX/ZIP**: El archivo que contiene los datos a procesar.
- **Pregunta**: La descripción o solicitud que se utilizará como base de la tarea. En el caso del agente `Creador de tareas masivas`, este se encargará de reformular la tarea para convertirla en tareas singulares. Pero para las otras opciones, es necesario proporcionar la base de la tarea en forma singular.
- **Grupo de ejecución**: Grupo opcional. Si no se establece, utiliza el ID de conversación. Se utiliza para identificar las tareas que pertenecen al mismo grupo.
- **Tipo de tarea**: ID de tipo de tarea opcional. Si no se establece, crea automáticamente uno llamado "Copilot". Se utiliza para identificar el tipo de tarea.
- **Estado**: ID de estado opcional. Por defecto es "Pendiente". Se utiliza para identificar el estado de la tarea. Después de que la tarea se procese, el estado se actualizará a `Completed`.
- **Agente**: El agente que procesará las tareas. Si no se especifica el agente, se seleccionará el agente que utilizó la herramienta. En el caso del agente `Creador de tareas masivas`, se seleccionará el agente supervisor que lo contiene.
- **Agrupar por**: Parámetro opcional. Una lista de nombres de columnas (o una cadena separada por comas) para agrupar filas por sus valores. Cuando se especifica, las filas con los mismos valores en estas columnas se agruparán en una única tarea, pasando los datos como un array JSON. Esto es útil para procesar registros relacionados juntos (p. ej., todas las líneas de pedido para el mismo documento). Si no se especifica, cada fila se convierte en una tarea independiente.
- **Vista previa**: Parámetro booleano opcional. Cuando se establece en `true`, la herramienta devolverá una vista previa de cómo se crearían las tareas sin crearlas realmente. Esto es útil para validar la estructura de la tarea antes de crear un gran número de tareas.

!!! info
    Cuando se crean las tareas, se creará una tarea por fila en el caso de archivos CSV/XLSX (a menos que se use `groupby`), una por archivo en el caso de archivos ZIP, y una por archivo en el caso de otros archivos. La solicitud de la tarea tendrá el siguiente formato:
    
    - **Sin agrupar por**: `BASE_TASK - [FILE_NAME/ROW DATA]`
    - **Con agrupar por**: `BASE_TASK - [JSON array with grouped rows]`

### Ejemplo
Por ejemplo, si tiene un archivo CSV con los siguientes datos:

```csv title="products.csv"
SKU,Description,Category,Price
33601251,FAN 38*30 NATURAL FIBER,Others,6100
33600292,BOTTLE OPENER,Others,10500
33600139,RUBBER BATH MAT,Decoration,3900
33600228,TREE,Plants,11500
33600739,ROUND METAL BUCKET,Others,9000
33600356,BAG 14X7X15,Others,1000
33600337,PIANO MUSIC BOX,Decoration,12000
```

Y el objetivo es insertar estos productos en Etendo. Para este ejemplo utilizaremos el agente `Data Initialization Supervisor` que contiene el agente `Product Generator` que puede crear productos en Etendo. Los pasos para crear las tareas masivas son:

#### Usar el botón `Add Copilot Task`

1. Vaya a la ventana **Mantenimiento**.
2. Haga clic en el botón `Add Copilot Task`. Esto abrirá una ventana para establecer los parámetros de las tareas masivas.
    ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-create-and-work-with-bulk-tasks-for-copilot/how-to-create-and-work-with-bulk-tasks-for-copilot.png)

    1. Establezca el parámetro **Pregunta** con la descripción de la tarea, en forma singular, que se utilizará como base de la tarea. Por ejemplo, `Create product with this data:`.
    2. Seleccione el **Agente**. En este caso, seleccione el agente `Data Initialization Supervisor`.
    3. Seleccione el **Archivo** a procesar. En este caso, seleccione el archivo CSV con los datos de productos.
    4. Establezca un identificador para el **Grupo de ejecución**. Por ejemplo, `Product Load 01/04/2025`. Esto puede utilizarse para identificar las tareas que pertenecen al mismo grupo.
    5. Establezca un **Elemento separador**. Este es el carácter que se utilizará para separar los datos del archivo CSV. Por ejemplo, `,` o `;`.
  
3. Haga clic en el botón `Done`. Y se crearán las tareas.
    
    ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-create-and-work-with-bulk-tasks-for-copilot/how-to-create-and-work-with-bulk-tasks-for-copilot-1.png)

#### Usar la `Task Creator Tool` en un agente

1. Vaya al agente que contiene la `Task Creator Tool`.
2. Abra una conversación con el agente.
3. Adjunte a la conversación el archivo CSV con los datos de productos.
4. Envíe alguna solicitud como:

    ``` text
    Create bulk tasks for the attached file.
    - Question/request: "Create product with this data:".
    - The group id is 'Product Load 01/04/2025'. 
    - The agent ID is 'A9E0861E88B1460A98CAF55DCB2BEE82'. 
    - Not indicate task type and status, to use the defaults.
    ```

    !!! info
        Este uso de la `Task Creator Tool` es un ejemplo; el agente puede tener suposiciones o simplificaciones que pueden cambiar la forma de utilizarla. Esto puede hacerse personalizando el prompt del agente.

5. El agente creará las tareas basándose en los datos del archivo usando la `Task Creator Tool`.

    ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-create-and-work-with-bulk-tasks-for-copilot/how-to-create-and-work-with-bulk-tasks-for-copilot-2.png)

#### Usar el agente `Bulk Task Creator`
Este agente sabe cómo usar la `Task Creator Tool` estratégicamente, convirtiendo la solicitud en tareas singulares. Los pasos para crear las tareas masivas son:

1. Añada el agente `Bulk Task Creator` a un agente supervisor. En este caso, utilizaremos el agente `Data Initialization Supervisor` que contiene el agente `Product Generator`.
2. Abra una conversación con el agente supervisor.
3. Adjunte a la conversación el archivo CSV con los datos de productos.
4. Envíe alguna solicitud como: 
   
    ``` text
    Create the products in the attached file.
    ```

    ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-create-and-work-with-bulk-tasks-for-copilot/how-to-create-and-work-with-bulk-tasks-for-copilot-3.png)

5. El agente supervisor delegará la tarea al agente `Bulk Task Creator`, que creará las tareas basándose en los datos del archivo y luego las procesará.

### Opciones avanzadas: agrupar datos relacionados

Cuando trabaje con datos que tienen relaciones entre filas (como líneas de pedido que pertenecen al mismo pedido, o líneas de factura para la misma factura), puede usar el parámetro `groupby` para crear una tarea por grupo en lugar de una tarea por fila.

#### Cuándo usar Agrupar por

Use el parámetro `groupby` cuando:

- **Los registros relacionados deben procesarse juntos**: Por ejemplo, todas las líneas de un pedido de venta deberían procesarse como una única tarea de creación de pedido.
- **Se necesita contexto de múltiples filas**: Cuando el agente de IA necesita ver todos los datos relacionados a la vez para tomar mejores decisiones.
- **Reducir la sobrecarga de tareas**: En lugar de crear cientos de tareas individuales, puede crear menos tareas con datos agrupados.

#### Ejemplo de Agrupar por: líneas de pedido

Suponga que tiene un archivo Excel con datos de líneas de pedido:

```csv title="order_lines.csv"
DocumentNo,Product,Quantity,Price
ORD-001,Laptop,2,1200
ORD-001,Mouse,2,25
ORD-002,Keyboard,5,80
ORD-002,Monitor,3,350
```

Sin agrupar por, esto crearía **4 tareas separadas** (una por fila). Con agrupar por, puede agrupar por `DocumentNo` para crear **2 tareas** (una por pedido).

**Usar la Task Creator Tool con agrupar por:**

```text
Create bulk tasks for the attached file.
- Question: "Create a sales order with these lines:"
- Group by: DocumentNo
- The group id is 'Order Load December 2025'
- The agent ID is 'A9E0861E88B1460A98CAF55DCB2BEE82'
```

Esto creará 2 tareas:

1. **Tarea 1**: `Create a sales order with these lines: - [{"DocumentNo": "ORD-001", "Product": "Laptop", "Quantity": 2, "Price": 1200}, {"DocumentNo": "ORD-001", "Product": "Mouse", "Quantity": 2, "Price": 25}]`
2. **Tarea 2**: `Create a sales order with these lines: - [{"DocumentNo": "ORD-002", "Product": "Keyboard", "Quantity": 5, "Price": 80}, {"DocumentNo": "ORD-002", "Product": "Monitor", "Quantity": 3, "Price": 350}]`

Cada tarea ahora contiene un array JSON con todas las líneas de ese pedido específico, lo que permite al agente procesar el pedido completo en una única ejecución.

#### Modo de vista previa

Antes de crear un gran número de tareas, puede usar el parámetro `preview` para validar la estructura de la tarea:

```text
Create bulk tasks for the attached file in preview mode.
- Question: "Create product with this data:"
- Preview: true
- The agent ID is 'A9E0861E88B1460A98CAF55DCB2BEE82'
```

La herramienta devolverá una vista previa mostrando cuántas tareas se crearían y su estructura, sin crearlas realmente en la base de datos.

## Cómo procesar tareas de Copilot
Las tareas pueden procesarse de dos maneras:

- **Procesamiento manual**: El usuario puede procesar las tareas manualmente en la ventana `Mantenimiento`. Seleccione las tareas a procesar y haga clic en el botón `EXECUTE TASK WITH COPILOT`. Después de que la tarea se procese, el estado se actualizará a `Completed` y el resultado se mostrará en el campo `Response`.

- **Procesamiento en segundo plano**: Las tareas pueden procesarse automáticamente en segundo plano. Vaya a la ventana `Process Request` para programar el proceso en segundo plano llamado `Execute Copilot Bulk Tasks`. En cada ejecución, el proceso tomará 10 tareas para procesar, por lo que es necesario ejecutar el proceso múltiples veces para procesar todas las tareas.

Después de que la tarea se procese, el estado se actualizará a `Completed` y el resultado se mostrará en el campo `Response`. Además, la respuesta completa del agente se almacenará en el campo `RAW Response`, y el campo `Conversation ID` contendrá el identificador de la conversación con el agente.

### Ejemplo

Por ejemplo, procesaremos algunas tareas creadas en el ejemplo anterior, de forma manual.

1. Vaya a la ventana `Mantenimiento`.
2. Seleccione las tareas a procesar.
3. Haga clic en el botón `EXECUTE TASK WITH COPILOT`.
    ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-create-and-work-with-bulk-tasks-for-copilot/how-to-create-and-work-with-bulk-tasks-for-copilot-4.png)
4. Las tareas se procesarán y el estado se actualizará a `Completed`.
    ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-create-and-work-with-bulk-tasks-for-copilot/how-to-create-and-work-with-bulk-tasks-for-copilot-5.png)
5. En el campo `Response` se mostrará el resultado de la tarea. La respuesta completa del agente está disponible en el campo `RAW Response`, y el campo `Conversation ID` contiene el identificador de la conversación del agente.
    ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-create-and-work-with-bulk-tasks-for-copilot/how-to-create-and-work-with-bulk-tasks-for-copilot-6.png)

Para las tareas restantes, programaremos el proceso en segundo plano para procesarlas.

1. Vaya a la ventana `Process Request`.
2. Cree un registro seleccionando el proceso `Execute Copilot Bulk Tasks`. Se recomienda programar el proceso para que se ejecute de vez en cuando, dependiendo de la necesidad específica. Para este caso, lo haremos cada 10 minutos.
    ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-create-and-work-with-bulk-tasks-for-copilot/how-to-create-and-work-with-bulk-tasks-for-copilot-7.png)
3. Haga clic en el botón `Schedule Process`.
4. El proceso se programará y procesará las tareas en segundo plano.
    ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-create-and-work-with-bulk-tasks-for-copilot/how-to-create-and-work-with-bulk-tasks-for-copilot-8.png)
5. Las tareas seleccionadas son las tareas ejecutadas:
    ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-create-and-work-with-bulk-tasks-for-copilot/how-to-create-and-work-with-bulk-tasks-for-copilot-9.png)

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.