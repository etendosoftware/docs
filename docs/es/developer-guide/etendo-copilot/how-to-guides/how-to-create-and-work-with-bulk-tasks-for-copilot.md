---
tags:
    - How to
    - Copilot
    - Bulk
    - Tasks
---

# Cómo crear y trabajar con tareas masivas para Copilot

## Visión general

Este artículo explica cómo crear y trabajar con tareas masivas para Copilot. Esto es útil cuando quieres crear múltiples tareas a la vez y ejecutarlas en segundo plano con Copilot.

### Concepto y casos de uso
Cuando necesitas hacer uso de un agente de IA para realizar tareas con un alto volumen de iteraciones, estará limitado en la cantidad que puede manejar y en su velocidad. Entonces nace el concepto de tareas masivas, que consiste en almacenar solicitudes en una ventana del módulo `Tasks`. 

!!!warning
    Es necesario considerar que estas tareas deben estar *aisladas* entre sí. Es decir, no necesitan información unas de otras. Por ejemplo, al cargar datos desde un archivo Excel, cada fila se ejecutará por separado.

Estas solicitudes pueden ejecutarse manualmente o procesarse en un proceso en segundo plano ya incluido en el módulo Copilot.

## Añadir tareas de Copilot
El módulo Etendo Copilot incluye:

- **Add Copilot Task Button**: Este botón en la ventana `Tasks` permite enviar un archivo CSV/XLSX/ZIP para crear tareas masivas.
- **Bulk Task Creator**: Este agente está configurado con la herramienta [Task Creator Tool](../available-tools/task-creator-tool.md) para crear tareas masivas basadas en un archivo zip o un archivo CSV/XLSX. Este agente puede añadirse a un agente supervisor para encadenarlo con otros agentes.

En ambas opciones, los requisitos son los mismos:

- **CSV/XLSX/ZIP file**: El archivo que contiene los datos a procesar.
- **Question**: La descripción o solicitud que se utilizará como base de la tarea. En el caso del agente `Bulk Task Creator`, se encargará de reformular la tarea para convertirla en tareas singulares. Pero para las otras opciones, es necesario proporcionar la base de la tarea en forma singular.
- **Execution Group**: Grupo opcional. Si no se establece, utiliza el ID de la conversación. Se utiliza para identificar las tareas que pertenecen al mismo grupo.
- **Task Type**: ID de tipo de tarea opcional. Si no se establece, crea automáticamente uno llamado "Copilot". Se utiliza para identificar el tipo de tarea.
- **Estado**: ID de estado opcional. Por defecto es "Pendiente". Se utiliza para identificar el estado de la tarea. Después de que la tarea se procese, el estado se actualizará a `Completed`.
- **Agent**: El agente que procesará las tareas. Si no se especifica el agente, se seleccionará el agente que utilizó la herramienta. En el caso del agente `Bulk task creator`, se seleccionará el agente supervisor que lo contiene.
- **Groupby**: Parámetro opcional. Una lista de nombres de columna (o una cadena separada por comas) para agrupar filas por sus valores. Cuando se especifica, las filas con los mismos valores en estas columnas se agruparán en una única tarea, pasando los datos como un array JSON. Esto es útil para procesar registros relacionados juntos (p. ej., todas las líneas de pedido para el mismo documento). Si no se especifica, cada fila se convierte en una tarea separada.
- **Preview**: Parámetro booleano opcional. Cuando se establece en `true`, la herramienta devolverá una vista previa de cómo se crearían las tareas sin crearlas realmente. Esto es útil para validar la estructura de las tareas antes de crear un gran número de tareas.

!!! info
    Cuando se crean las tareas, se creará una tarea por fila en el caso de archivos CSV/XLSX (a menos que se use `groupby`), una por archivo en el caso de archivos ZIP, y una por archivo en el caso de otros archivos. La solicitud de la tarea tendrá el siguiente formato:
    
    - **Without groupby**: `BASE_TASK - [FILE_NAME/ROW DATA]`
    - **With groupby**: `BASE_TASK - [JSON array with grouped rows]`

### Ejemplo
Por ejemplo, si tienes un archivo CSV con los siguientes datos:

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

Y el objetivo es insertar estos productos en Etendo. Para este ejemplo usaremos el agente `Data Initialization Supervisor` que contiene el agente `Product Generator` que puede crear productos en Etendo. Los pasos para crear las tareas masivas son:

#### Usando el botón `Add Copilot Task`

1. Ve a la ventana **Tasks**.
2. Haz clic en el botón `Add Copilot Task`. Esto abrirá una ventana para establecer los parámetros de las tareas masivas.
    ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-create-and-work-with-bulk-tasks-for-copilot/how-to-create-and-work-with-bulk-tasks-for-copilot.png)

    1. Establece el parámetro **Question** con la descripción de la tarea, en forma singular, que se utilizará como base de la tarea. Por ejemplo, `Create product with this data:`.
    2. Selecciona el **Agent**. En este caso, selecciona el agente `Data Initialization Supervisor`.
    3. Selecciona el **File** a procesar. En este caso, selecciona el archivo CSV con los datos de productos.
    4. Establece un identificador para el **Execution Group**. Por ejemplo, `Product Load 01/04/2025`. Esto puede usarse para identificar las tareas que pertenecen al mismo grupo.
    5. Establece un **Elemento separador**. Este es el carácter que se utilizará para separar los datos del archivo CSV. Por ejemplo, `,` o `;`.
  
3. Haz clic en el botón `Done`. Y se crearán las tareas.
    ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-create-and-work-with-bulk-tasks-for-copilot/how-to-create-and-work-with-bulk-tasks-for-copilot-1.png)

#### Usando la `Task Creator Tool` en un agente

1. Ve al agente que contiene la `Task Creator Tool`.
2. Abre una conversación con el agente.
3. Adjunta a la conversación el archivo CSV con los datos de productos.
4. Envía una solicitud como:

    ``` text
    Create bulk tasks for the attached file.
    - Question/request: "Create product with this data:".
    - The group id is 'Product Load 01/04/2025'. 
    - The agent ID is 'A9E0861E88B1460A98CAF55DCB2BEE82'. 
    - Not indicate task type and status, to use the defaults.
    ```

    !!! info
        Este uso de la `Task Creator Tool` es un ejemplo; el agente puede tener suposiciones o simplificaciones que pueden cambiar la forma de usarla. Esto puede hacerse personalizando el prompt del agente.

5. El agente creará las tareas basadas en los datos del archivo usando la `Task Creator Tool`.

![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-create-and-work-with-bulk-tasks-for-copilot/how-to-create-and-work-with-bulk-tasks-for-copilot-2.png)

#### Usando el agente `Bulk Task Creator`
Este agente sabe cómo usar la `Task Creator Tool` de forma estratégica, convirtiendo la solicitud en tareas singulares. Los pasos para crear las tareas masivas son:

1. Añade el agente `Bulk Task Creator` a un agente supervisor. En este caso, usaremos el agente `Data Initialization Supervisor` que contiene el agente `Product Generator`.
2. Abre una conversación con el agente supervisor.
3. Adjunta a la conversación el archivo CSV con los datos de productos.
4. Envía una solicitud como: 
   
    ``` text
    Create the products in the attached file.
    ```

    ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-create-and-work-with-bulk-tasks-for-copilot/how-to-create-and-work-with-bulk-tasks-for-copilot-3.png)

5. El agente supervisor delegará la tarea al agente `Bulk Task Creator`, que creará las tareas basadas en los datos del archivo y luego las procesará.

### Opciones avanzadas: Agrupar datos relacionados

Cuando trabajas con datos que tienen relaciones entre filas (como líneas de pedido que pertenecen al mismo pedido, o líneas de factura para la misma factura), puedes usar el parámetro `groupby` para crear una tarea por grupo en lugar de una tarea por fila.

#### Cuándo usar Groupby

Usa el parámetro `groupby` cuando:

- **Related records should be processed together**: Por ejemplo, todas las líneas de un pedido de ventas deberían procesarse como una única tarea de creación de pedido.
- **Context from multiple rows is needed**: Cuando el agente de IA necesita ver todos los datos relacionados a la vez para tomar mejores decisiones.
- **Reducing task overhead**: En lugar de crear cientos de tareas individuales, puedes crear menos tareas con datos agrupados.

#### Ejemplo de Groupby: Líneas de pedido

Supón que tienes un archivo Excel con datos de líneas de pedido:

```csv title="order_lines.csv"
DocumentNo,Product,Quantity,Price
ORD-001,Laptop,2,1200
ORD-001,Mouse,2,25
ORD-002,Keyboard,5,80
ORD-002,Monitor,3,350
```

Sin groupby, esto crearía **4 separate tasks** (una por fila). Con groupby, puedes agrupar por `DocumentNo` para crear **2 tasks** (una por pedido).

**Using the Task Creator Tool with groupby:**

```text
Create bulk tasks for the attached file.
- Question: "Create a sales order with these lines:"
- Group by: DocumentNo
- The group id is 'Order Load December 2025'
- The agent ID is 'A9E0861E88B1460A98CAF55DCB2BEE82'
```

Esto creará 2 tareas:

1. **Task 1**: `Create a sales order with these lines: - [{"DocumentNo": "ORD-001", "Product": "Laptop", "Quantity": 2, "Price": 1200}, {"DocumentNo": "ORD-001", "Product": "Mouse", "Quantity": 2, "Price": 25}]`
2. **Task 2**: `Create a sales order with these lines: - [{"DocumentNo": "ORD-002", "Product": "Keyboard", "Quantity": 5, "Price": 80}, {"DocumentNo": "ORD-002", "Product": "Monitor", "Quantity": 3, "Price": 350}]`

Cada tarea ahora contiene un array JSON con todas las líneas de ese pedido específico, permitiendo al agente procesar el pedido completo en una única ejecución.

#### Modo Preview

Antes de crear un gran número de tareas, puedes usar el parámetro `preview` para validar la estructura de las tareas:

```text
Create bulk tasks for the attached file in preview mode.
- Question: "Create product with this data:"
- Preview: true
- The agent ID is 'A9E0861E88B1460A98CAF55DCB2BEE82'
```

La herramienta devolverá una vista previa mostrando cuántas tareas se crearían y su estructura, sin crearlas realmente en la base de datos.

## Cómo procesar tareas de Copilot
Las tareas pueden procesarse de dos maneras:

- **Procesamiento manual**: El usuario puede procesar las tareas manualmente en la ventana `Tasks`. Selecciona las tareas a procesar y haz clic en el botón `EXECUTE TASK WITH COPILOT`. Después de que la tarea se procese, el estado se actualizará a `Completed` y el resultado se mostrará en `Response`.

- **Procesamiento en segundo plano**: Las tareas pueden procesarse automáticamente en segundo plano. Ve a la ventana `Process Request` para programar el proceso en segundo plano llamado `Execute Copilot Bulk Tasks`. En cada ejecución, el proceso tomará 10 tareas para procesar, por lo que es necesario ejecutar el proceso múltiples veces para procesar todas las tareas.

Después de que la tarea se procese, el estado se actualizará a `Completed` y el resultado se mostrará en `Response`.

### Ejemplo

Por ejemplo, procesaremos algunas tareas creadas en el ejemplo anterior, de forma manual

1. Ve a la ventana `Tasks`.
2. Selecciona las tareas a procesar.
3. Haz clic en el botón `EXECUTE TASK WITH COPILOT`.
    ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-create-and-work-with-bulk-tasks-for-copilot/how-to-create-and-work-with-bulk-tasks-for-copilot-4.png)
4. Las tareas se procesarán y el estado se actualizará a `Completed`.
    ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-create-and-work-with-bulk-tasks-for-copilot/how-to-create-and-work-with-bulk-tasks-for-copilot-5.png)
5. En el campo `Response` se mostrará el resultado de la tarea.
    ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-create-and-work-with-bulk-tasks-for-copilot/how-to-create-and-work-with-bulk-tasks-for-copilot-6.png)

Para las tareas restantes, programaremos el proceso en segundo plano para procesarlas.

1. Ve a la ventana `Process Request`.
2. Crea un registro seleccionando el proceso `Execute Copilot Bulk Tasks`. Se recomienda programar el proceso para que se ejecute de vez en cuando, dependiendo de la necesidad específica. Para este caso, lo haremos cada 10 minutos.
    ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-create-and-work-with-bulk-tasks-for-copilot/how-to-create-and-work-with-bulk-tasks-for-copilot-7.png)
3. Haz clic en el botón `Schedule Process`.
4. El proceso se programará y procesará las tareas en segundo plano.
    ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-create-and-work-with-bulk-tasks-for-copilot/how-to-create-and-work-with-bulk-tasks-for-copilot-8.png)
5. Las tareas seleccionadas son las tareas ejecutadas:
    ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-create-and-work-with-bulk-tasks-for-copilot/how-to-create-and-work-with-bulk-tasks-for-copilot-9.png)

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.