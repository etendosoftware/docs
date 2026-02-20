---
tags:
    - Conceptos
    - Modelo de datos
    - Diccionario de aplicación
    - Tabla
    - Columnas
    - Precisión decimal
---

# Modelo de datos

## Visión general

El Modelo de datos de Etendo se define en el Diccionario de aplicación. En el modelo de datos, el Diccionario de aplicación mapea las tablas y columnas físicas de la base de datos en sus propias tablas (`AD_Table` y `AD_Column`) y, sobre esta base, se construye el resto del sistema (ventanas, solapas, campos, etc.).

Este documento explica cómo se definen las tablas y columnas en la base de datos física y cómo se mapean en el Modelo de datos del Diccionario de aplicación.
## Tabla en el Diccionario de Aplicación

Una vez que las [Tabla](../concepts/Tables.md) se definen físicamente en la base de datos, deben mapearse con el Diccionario de Aplicación. Este mapeo se realiza a través de `Application Dictionary` > `Tables and Columns` > solapa `Tabla`, que rellena la tabla `AD_Table`.

### Nomenclatura de tablas

Una tabla definida en el diccionario de aplicación tiene varios nombres que Etendo utiliza de diferentes maneras:

- Nombre lógico (`AD_Table`.name): utilizado por la Capa de Acceso a Datos en los servicios web REST [XML](../concepts/xml-rest-web-services.md) y [JSON](../concepts/JSON_REST_Web_Services.md). Consulte [aquí](../concepts/Data_Access_Layer.md#entity-naming) para más información.
- Nombre físico (`AD_Table`.tablename): es el nombre de la tabla en la base de datos.
- Nombre de clase (`AD_Table`.classname): el nombre de la clase de entidad Java generada](../concepts/Data_Access_Layer.md#generated-business-object-classes).
## Columnas en el Diccionario de Aplicación

Después de definir la tabla en el Diccionario de Aplicación, el siguiente paso es añadirle columnas. Existe un proceso que lee las columnas de la base de datos y las inserta como columnas en la tabla. Este proceso se invoca desde el botón **Crear columnas desde BD** en `Application Dictionary` > `Tables and Columns` > solapa `Tabla`.

Después, es posible comprobar todas las columnas de la tabla en `Application Dictionary` > `Tables and Columns` > `Tabla` > solapa `Columna`, y ajustarlas con más detalle si es necesario. Existe una explicación detallada de todos los campos de esa solapa en la documentación sobre la tabla `AD_Column`.

Las siguientes secciones explican algunos detalles que deben tenerse en cuenta al definir una columna.
### Nomenclatura de columnas

Una columna definida en el Diccionario de Aplicación tiene varios nombres que Etendo utiliza de diferentes maneras:

- El nombre lógico (`AD_Column`.name): este nombre lo utiliza la Data Access Layer para la [detección automática de interfaces compatibles](../concepts/Data_Access_Layer.md#property-naming-and-supported-interfaces) y la [nomenclatura de propiedades XML y Java](../concepts/Data_Access_Layer.md#property-naming).
- El nombre físico de la columna (`AD_Column`.columnname): es el nombre de la columna en la tabla de la base de datos.

!!!important
    Al nombrar columnas relacionadas con información de auditoría, cliente/organización y activo, es muy importante ser preciso en el nombre. Si se utiliza un nombre mal escrito, Etendo no podrá detectar que una entidad es compatible con una determinada interfaz y se deshabilitará un comportamiento automático específico. Consulte [aquí](../concepts/Data_Access_Layer.md#important-interfaces) una lista de interfaces y sus nombres lógicos de columna esperados.
### Definición de objetos de negocio: el isParent

La definición de columna en el diccionario de aplicación también se utiliza para definir estructuras de objetos de negocio en Etendo. Si el campo `isParent` de una columna de clave externa está establecido (marcado/true), entonces esta clave externa modela una asociación de un hijo a un padre. Con esta información, la [Data Access Layer](../concepts/Data_Access_Layer.md) creará automáticamente una asociación (en memoria) del padre al hijo.

Por ejemplo, la tabla `C_OrderLine` tiene una columna `c_order_id`. En el diccionario de aplicación, esta columna está marcada como `isParent` (por lo que `c_order_id` apunta al padre de la línea de pedido: la cabecera del pedido). La capa de acceso a datos traducirá esta columna de clave externa en dos asociaciones en el modelo de entidad:

- Una asociación de muchos a uno desde la entidad de línea de pedido al pedido (su padre)
- Una asociación de uno a muchos desde el pedido a las líneas de pedido; en Java esto da como resultado un miembro de tipo `java.util.List`.

Para más información, consulte [aquí](../concepts/Data_Access_Layer.md#business-object).
### Referencia

Las referencias se utilizan en el Diccionario de Aplicación de Etendo para dos propósitos:

- **Definir el tipo de datos almacenados en una columna**:  
  En función de la referencia que tenga una columna, dicha columna contendrá distintos tipos de datos, por ejemplo valores numéricos, texto plano, enlaces a otras columnas, etc.

- **Definir cómo se representarán en la UI los campos vinculados a una columna**:  
  La referencia de una columna también indica cómo se representarán dentro de las solapas los campos asociados a esa columna, por ejemplo una lista desplegable, un cuadro de texto con un botón para mostrar un selector, etc.  
  Por lo tanto, cada columna en el Diccionario de Aplicación tiene una y solo una referencia.
#### Tipos de Referencias

Existen dos tipos básicos de referencias: **Base** y **Subreferencias**. Las referencias se configuran en `Application Dictionary` > `Tables and Columns` > `Tabla` > solapa `Columna` usando el campo `Referencia` para las referencias de tipo de datos y `Referencia clave` para los subtipos.

##### Referencias base

Estas referencias pueden asociarse directamente a una columna. Algunos ejemplos de referencias de datos son fecha, precio, lista, etc.
#### Subreferencias

Algunas referencias base requieren otra referencia para definir completamente los datos que contendrá la columna. En estos casos se utilizan las subreferencias. Las referencias base definidas en core que requieren una subreferencia son: `Lista`, `Selector` y `Tabla`. Por lo tanto, cuando una de estas referencias base se asocia a una columna, es necesario asociar también a esa columna otra referencia de subtipo. Por ejemplo, para configurar una columna como un selector de Terceros, es necesario establecer la referencia principal de esta columna como `Selector` y la secundaria como `Selector de Terceros`.

!!!info
    Cuando las columnas en el Diccionario de Aplicación se crean automáticamente en función de su descripción física en base de datos mediante el proceso `Diccionario de Aplicación` > `Tablas y Columnas` > `Tabla` > `Crear columnas desde BD`, se establecen las referencias que tienden a ser las adecuadas, pero en algunos casos es necesario cambiarlas. Es una buena práctica revisar todas las referencias asignadas automáticamente para las nuevas columnas después de ejecutar este proceso.
#### Referencias base del core

Las siguientes secciones describen las referencias base definidas en el core.

##### Referencias numéricas

`Integer`, `Number`, `Amount`, `Quantity` y `General Quantity` se utilizan para mantener valores numéricos. Al definir una de estas referencias, es posible incluir el valor mínimo y/o el máximo para la columna si se desea; tenga en cuenta que la comprobación de estos valores se realizará solo en la UI, pero no a nivel de base de datos, por lo que sería posible añadir datos fuera de rango usando cualquier proceso. Para aplicar estas restricciones en base de datos, utilice restricciones de comprobación (check constraints) de base de datos.

![](../../../assets/developer-guide/etendo-classic/concepts/Data_Model-1.png)

Cuando hay un campo en una solapa asociado a una columna con una de estas referencias, la forma en que se representa se verá como en la imagen siguiente.

![](../../../assets/developer-guide/etendo-classic/concepts/Data_Model-2.png)

La descripción física de las columnas que usan estas referencias debe ser `number`.

!!!note
    La forma en que se representan los números decimales se define en el archivo `config/Format.xml` con estas equivalencias:  
    - `euroEdition`: Amount
    - `qtyEdition`: Quantity
    - `priceEdition`: Price
    - `IntegerEdition`: Integer
    - `generalQtyEdition`: General Quantity and Number

##### Precio

La referencia `Price` es similar a las numéricas anteriores y está pensada para almacenar importes monetarios. Al definirla, no permite valores máximos ni mínimos.

La descripción física de las columnas que usan estas referencias debe ser `number`.

##### Referencias de texto

Las referencias `String`, `Text` y `Memo` se utilizan para columnas de texto. La diferencia entre ellas es la longitud del texto que se supone que deben almacenar.

- **String** es para texto corto y siempre se mostrará en la UI como un cuadro de texto de una sola línea.
- **Texto** y **Nota** se muestran en múltiples líneas dependiendo de la longitud definida en el campo `Length`.

La descripción física de las columnas que usan estas referencias debe ser `char`, `varchar` o `nvarchar`.

Así es como se ve una referencia de **texto** en la UI:

![](../../../assets/developer-guide/etendo-classic/concepts/Data_Model-3.png)

##### Enlace URL

La referencia `Link` se utiliza para representar enlaces URL. Las columnas con esta referencia son columnas de texto.

La UI para esta referencia es:

![](../../../assets/developer-guide/etendo-classic/concepts/Data_Model-4.png)

Al hacer clic en el botón junto al cuadro de texto, se abre un nuevo navegador con el enlace del cuadro.

##### Referencias de tiempo

`Date`, `Time`, `DateTime`, `Absolute Time` y `Absolute DateTime` se utilizan para columnas que almacenan valores de fecha u hora. **Fecha** muestra una fecha sin horas; **Hora** muestra hora sin fecha, es decir, solo horas, minutos y segundos; **DateTime** muestra fecha con hora.

Al definir una columna de tipo **Fecha** se aceptan valores máximos y mínimos.

En Oracle, las columnas físicas de base de datos para estas referencias deben ser de tipo `DATE` o `TIMESTAMP`. En PostgreSQL el tipo de dato es `Timestamp without timezone`.

Un ejemplo de cómo se representa un campo para una columna con referencia de fecha es el siguiente:

![](../../../assets/developer-guide/etendo-classic/concepts/Data_Model-5.png)

Tenga en cuenta que se muestra un botón de calendario junto al cuadro de texto; esto facilita la selección de fechas. Al hacer clic en él, se abre un pop-up de calendario:

![](../../../assets/developer-guide/etendo-classic/concepts/Data_Model-6.png)

Y este es un ejemplo de un campo DateTime:

![](../../../assets/developer-guide/etendo-classic/concepts/Data_Model-7.png)

El selector de fecha para esta referencia es como el de la referencia Fecha, pero además añade un selector de hora. Si el valor de entrada está vacío, el valor de este selector de hora es la hora actual.

![](../../../assets/developer-guide/etendo-classic/concepts/Data_Model-8.png)

El formato para mostrar horas y fechas se define en el archivo `config/Openbravo.properties` mediante `dateFormat.sql` y `dateTimeFormat.sql` usando formato SQL. Ejemplo:

```java
dateFormat.sql=DD-MM-YYYY
dateTimeFormat.sql=DD-MM-YYYY HH24:MI:SS 
```

**Hora** y **DateTime** son referencias relativas, lo que significa que el valor almacenado se carga desde el backend con la zona horaria del backend/servidor y se muestra en el cliente/navegador con la zona horaria del propio cliente:

- El valor se almacena con la zona horaria del servidor.
- Al cargar en el cliente, el servidor transforma el valor a UTC y lo envía al cliente. El cliente transforma este valor UTC a la zona horaria del cliente.
- Al guardar en el servidor, el valor en zona horaria del cliente se transforma a UTC y se envía al servidor. El servidor lee este valor UTC, lo transforma a la zona horaria del servidor y lo almacena en la base de datos.

`Absolute Time` y `Absolute DateTime` son, como su nombre indica, referencias absolutas, lo que significa que el valor almacenado en el backend/servidor es exactamente el mismo que se muestra en el cliente/navegador:

- Al pasar la hora/datetime del cliente al servidor, el valor se pasa tal cual se lee de la base de datos, por lo que no hay conversión a UTC. Existen algunos mecanismos en el cliente para mostrar el valor tal como llega, por lo que no hay conversiones aquí.
- Al recibir un valor del cliente, también se almacena tal como llega desde el cliente sin ninguna conversión a UTC.

##### Referencia Sí/No

La referencia `YesNo` se utiliza para columnas que aceptan valores booleanos (sí o no). En la UI se muestra una casilla de verificación; cuando está marcada la columna tomará 'Y' como valor, cuando no lo está tomará 'N'.

Las columnas físicas de base de datos para estas referencias deben ser `CHAR(1)`.

La UI para esta referencia es:

![](../../../assets/developer-guide/etendo-classic/concepts/Data_Model-9.png)

##### Imagen

La referencia **Image BLOB** se utiliza para almacenar imágenes en la base de datos. Todas las imágenes se almacenan físicamente en un campo binario de la tabla `AD_IMAGE`, y la columna de tabla utilizada debe ser una referencia a esta tabla. Los tipos de imagen soportados son los tipos ráster: **PNG**, **JPEG** y **BMP**, y el tipo vectorial **SVG**.

!!!info
    Las imágenes **SVG** están totalmente soportadas en los navegadores Chrome, Firefox, Safari y Microsoft Edge. No en Internet Explorer. En este navegador, las imágenes **SVG** pueden recortarse y no mostrarse correctamente.

![](../../../assets/developer-guide/etendo-classic/concepts/Data_Model-11.png)

La columna de imagen puede tener una acción asociada que define una validación y una transformación a realizar para las imágenes guardadas en la base de datos en función del tamaño original de la imagen. Tenga en cuenta que las imágenes vectoriales _SVG_ nunca aplican para estas acciones.

![](../../../assets/developer-guide/etendo-classic/concepts/Data_Model-12.png)

Las acciones definidas para los valores de tamaño de imagen son:

- **None**. Se puede guardar cualquier imagen y no se realiza ninguna transformación sobre la imagen.
- **Allowed - Exact size**. Solo se permiten imágenes con el tamaño definido en los campos **Ancho de la imagen** y **Altura de imagen**.
- **Allowed - Minimum size**. Solo se permiten imágenes con al menos el tamaño definido en los campos **Ancho de la imagen** y **Altura de imagen**.
- **Allowed - Maximum size**. Solo se permiten imágenes con un máximo del tamaño definido en los campos **Ancho de la imagen** y **Altura de imagen**.
- **Recommended - Exact size**. Si la imagen no tiene el tamaño definido en los campos **Ancho de la imagen** y **Altura de imagen**, se muestra una advertencia al usuario.
- **Recommended - Minimum size**. Si la imagen no tiene al menos el tamaño definido en los campos **Ancho de la imagen** y **Altura de imagen**, se muestra una advertencia al usuario.
- **Recommended - Maximum size**. Si el tamaño de la imagen es mayor que el tamaño definido en los campos **Ancho de la imagen** y **Altura de imagen**, se muestra una advertencia al usuario.
- **Resize - Exact resize (without maintaining the aspect ratio)**. La imagen guardada se redimensiona al tamaño definido en los campos **Ancho de la imagen** y **Altura de imagen**. No se mantiene la relación de aspecto y puede cambiar.
- **Resize - Closest to the maximum size (maintaining aspect ratio)**. La imagen guardada se redimensiona al tamaño definido en los campos **Ancho de la imagen** y **Altura de imagen**. Pero se mantiene la relación de aspecto ajustando el ancho o el alto de la imagen para mantenerse dentro del tamaño definido.
- **Resize - Closest to the maximum size only if larger image**. Similar a la acción anterior, pero el redimensionado se realiza solo si el tamaño de la imagen es mayor que el tamaño definido en los campos **Ancho de la imagen** y **Altura de imagen**.

Cuando hay un campo en una solapa asociado con una de estas referencias, la forma en que se representa se verá como en la siguiente imagen:

![](../../../assets/developer-guide/etendo-classic/concepts/Data_Model-13.png)

##### Botón

Los botones en Etendo también deben estar contenidos en una columna, aunque el valor de esta columna no es modificable directamente por el usuario. Los botones se utilizan para llamar a procesos.

Cuando a una columna se le asigna la referencia `Button` se muestran los siguientes campos adicionales: `Process` y `Ref Search Value`.

![](../../../assets/developer-guide/etendo-classic/concepts/Data_Model-14.png)

En la lista **Proceso**, se seleccionará el proceso que se llama cuando se hace clic en el botón; este campo es obligatorio cuando la referencia es botón.

También está disponible un campo opcional **Ref Search Value**; aquí es posible seleccionar una lista de referencia (consulte la referencia de lista más abajo). Si no se selecciona ningún valor en este campo, el texto dentro del botón será estático (el nombre del proceso), pero si se selecciona una lista de referencia, el texto del cuadro será el nombre del elemento de la lista que tenga el mismo valor que el valor actual en la lista. Por ejemplo, si definimos una lista con los pares valor, nombre como: [{'N', 'Process'}, {'Y','Unprocess'}] y la seleccionamos, cuando el valor de la columna sea 'N' se mostrará 'Process', pero 'Unprocess' cuando sea 'Y'.

Al mostrar una solapa con un botón se ve así:

![](../../../assets/developer-guide/etendo-classic/concepts/Data_Model-15.png)

!!!note
    Al hacer clic en él se abre un pop-up con la interfaz del proceso. Por defecto, antes de abrir este pop-up, las modificaciones del registro actual se guardan automáticamente; tras la ejecución del proceso, el registro actual se refresca. Esta es la razón por la que no se muestran los botones mientras no se hayan completado todos los campos obligatorios. Estos comportamientos por defecto se omiten en caso de que la columna esté desmarcada como `Triggers Autosave`.

###### Botones DocAction

Los botones de acción son un tipo especial de botones utilizados para ejecutar acciones de proceso sobre ciertos documentos (como facturas, pedidos, etc.). Estos botones tienen como nombre de columna **DocAction**.

Cuando se hace clic en ellos se abre un pop-up como el siguiente:

![](../../../assets/developer-guide/etendo-classic/concepts/Data_Model-17.png)

Las acciones disponibles que se muestran en este pop-up dependen del estado del documento y se calculan mediante el método `org.openbravo.erpCommon.ad_actionButton.ActionButtonUtility.docAction`.

###### Botones de contabilización

Otro botón especial es el que se emite en documentos que soportan contabilidad para contabilizar/descontabilizar. El nombre de la columna debe ser `Posted` y el proceso se deja vacío. Estos botones llaman directamente al proceso contable.

##### Lista

La referencia `List` se utiliza para limitar los valores que puede tomar una columna a aquellos definidos en una lista. Cuando una columna se define como referencia de lista, es necesario seleccionar una subreferencia entre las listas existentes en el Diccionario de Aplicación; esto se hace seleccionando el valor correcto en el campo **Referencia clave**.

![](../../../assets/developer-guide/etendo-classic/concepts/Data_Model-18.png)

Las columnas físicas para esta referencia deben ser `VARCHAR(60)`.

Los valores reales que tomará la columna son los definidos como **Identificador** en la lista; para más información consulte la sección [definir listas](#definir-listas).

La UI para listas es una lista desplegable.

###### Cuándo usar listas

Las listas son útiles para mantener listas de valores fijos que rara vez necesitan incluir nuevos valores y cuyo mantenimiento puede realizarse con un rol de Administrador del sistema, no por un usuario estándar.

Vamos a explicarlo mediante un ejemplo. Hay 3 tipos de Módulo: **Módulo**, **Plantillas** y **Packages**. Esta definición no va a cambiar muy a menudo; es posible que en versiones futuras se añada un nuevo tipo de módulo, pero no es algo que vaya a cambiar a diario. Además, si cambia, seguro que ningún usuario estándar tendría que realizar la modificación, sino que tendría que hacerlo el **Administrador del sistema**. Hay dos soluciones posibles para esto:

1. Crear una tabla para los tipos de módulo y añadir en la tabla de módulos una columna de clave foránea a esta tabla.
2. Crear una lista de tipos de módulo y añadir en la tabla de módulos una columna de referencia de lista usando esta nueva referencia.

El segundo enfoque es más fácil de implementar y mantener; adicionalmente, no crea una tabla de base de datos con solo 3 registros fijos. De hecho, entre bastidores, todos los datos de todas las listas en Etendo se almacenan en una única tabla de base de datos (`AD_Ref_List`).

Además, las listas son traducibles, lo que significa que las listas desplegables pueden mostrarse en el idioma del usuario; por tanto, seguir el primer enfoque habría requerido crear una nueva tabla adicional para almacenar traducciones.

###### Definir listas

Las referencias de lista, al igual que el resto de referencias, se gestionan desde `Application Dictionary` > `Referencia` > solapa `Referencia`.

Para crear una nueva, haga clic en **New**, inserte un nombre y seleccione **Lista** como **Referencia padre**. Este paso crea la cabecera de la lista.

En esta cabecera, es posible seleccionar el campo `Display value`. En caso de seleccionarlo, los elementos de la lista se representarán concatenando su valor y su nombre; si no, solo se mostrará el nombre.

El siguiente paso es añadir valores a la lista. Para ello, vaya a la solapa **Lista valores** y cree los valores que necesite. Aquí hay tres campos importantes a tener en cuenta:

- **Identificador**: este es el valor (no visible en la UI) que tomará la columna que use esta referencia cuando se seleccione.
- **Nombre**: es el nombre que se mostrará en la lista desplegable.
- **Secuencia**: es la posición del elemento cuando se renderiza la lista desplegable. Este campo admite nulos; dependiendo de los valores que tenga en los elementos de la lista, la ordenación se realiza de la siguiente manera:
  - Si el valor de este campo es nulo para todos los elementos de la lista, la lista se ordenará alfabéticamente.
  - Si todos los elementos tienen este valor informado, se ordenarán teniéndolo en cuenta.
  - Si algunos elementos lo tienen y otros no, los que lo tengan se mostrarán al principio de la lista ordenados por este número; el resto se mostrará al final ordenado alfabéticamente.

Como consideración adicional, es posible añadir elementos en un módulo distinto al de su cabecera; en este caso, el **Identificador** de los valores debe comenzar con el DBPrefix del módulo para evitar colisiones de nombres.

##### ID

Etendo utiliza UUID como clave primaria para sus tablas. El nombre estándar para una columna de clave primaria es **TableName_ID**, por lo que, por ejemplo, para la tabla `HR_Salary` su columna de clave primaria se llamaría `HR_Salary_ID`. Para poder almacenar UUID, el tipo físico de la columna debe ser `VARCHAR2(32)`. Además, esa columna debe establecerse como clave primaria en la base de datos.

La referencia `ID` se utiliza para columnas de clave primaria. Normalmente, no debería mostrarse al usuario porque esta clave no tiene sentido para él (use identificadores en su lugar), pero si se muestra, la UI para esta referencia es como la referencia **String**, un cuadro de texto de una sola línea.

##### TableDir

La referencia `TableDir` significa **Table Direct**. Como se explicó en la sección anterior, el nombre estándar para una columna de clave primaria es **TableName_ID**; del mismo modo, el nombre estándar para una columna de clave foránea es el nombre de la columna de clave primaria foránea. Por ejemplo, si creamos una nueva tabla llamada `HR_MyTable` y queremos añadir una clave foránea a `HR_Salary`, la columna debería llamarse `HR_MyTable.HR_Salary_ID`. Si se sigue esta regla de nomenclatura, el proceso `Create columns from DB` establecerá esta nueva columna como referencia **TableDir**. Cuando se crea la UI para esta columna, se genera una lista desplegable con todos los elementos de la tabla foránea a los que se puede referir desde el registro actual. Si el nombre de la columna no es el mismo que el nombre de la columna de clave primaria de la tabla foránea, la referencia TableDir no funcionará; será necesario definir una referencia **Tabla** para esa columna.

Las columnas físicas para claves foráneas deben ser de tipo `VARCHAR(32)` para poder almacenar UUID. También es necesario que la tabla física defina una clave foránea hacia la otra tabla.

Esta es la UI para la referencia **TableDir**:

![](../../../assets/developer-guide/etendo-classic/concepts/Data_Model-19.png)

Es una lista desplegable; observe que la etiqueta es un enlace: al hacer clic en ella, el usuario navegará al elemento foráneo seleccionado. Observe también que, aunque el valor real que tomará la columna es el UUID del elemento seleccionado, los UUID no se muestran; en su lugar, los valores mostrados son los identificadores definidos en la tabla foránea.

##### Tabla

La referencia `Table` es similar a **TableDir**, pero no tiene la limitación de nomenclatura; también permite definir una `where clause` para limitar el número de registros que se mostrarán, así como una **order by clause** para mostrarlo en un orden determinado. Cuando se selecciona la referencia **Tabla** para una columna, el campo **Referencia clave** pasa a ser visible, conteniendo una lista de todos los subtipos disponibles de **table dir**; es necesario seleccionar uno de ellos. Estos subtipos definen la tabla a la que hace referencia la columna.

Como la columna para esta referencia también es una clave foránea, debe ser físicamente en base de datos idéntica a las definidas para las referencias **TableDir**.

Visualmente, la UI para esta referencia es idéntica a la de **TableDir**.

###### Cuándo usar referencia de tabla

Normalmente, las referencias **Tabla** se utilizan cuando el nombre de la columna no coincide con el nombre de la columna a la que está enlazada. En este caso es obligatorio usar esta referencia (o la referencia **Selector** si está disponible para esa tabla).

Otro caso es cuando el orden por defecto en la referencia **TableDir** no es apropiado.

!!!info
    No es necesario definir una referencia **Tabla** para limitar los registros que se muestran en una **TableDir**, ya que es posible hacerlo usando una **Validación**.

###### Definir una referencia de tabla

Como todas las referencias, las referencias **Tabla** se definen en `Application Dictionary` > `Referencia` > solapa `Referencia`.

Para crear una nueva:

1. Haga clic en **New**, inserte un nombre y seleccione **Tabla** en el campo **Referencia padre**. Este paso crea la cabecera de la tabla.

2. El siguiente paso es definir la tabla a enlazar. Para ello, vaya a la solapa **Tabla referenciada** y cree un nuevo registro.

3. En el campo **Tabla** seleccione la tabla a la que está enlazada la columna; en el campo `Key column` el valor que se almacenará en la columna (normalmente es la columna de clave primaria); y en **Mostrar columna** la columna que se mostrará en la lista desplegable. Tenga en cuenta que aquí solo se puede seleccionar una columna y no es posible seleccionar el identificador de registro de la tabla. `SQL where clause` y **Order by** son campos opcionales que pueden utilizarse en caso de que queramos restringir los registros a mostrar o si queremos ordenarlos de una manera específica.

!!!note
    Es muy recomendable revisar las referencias de Tabla ya definidas para encontrar una que se ajuste a sus requisitos antes de crear una nueva.

##### Selector

La referencia `Search`, al igual que **Tabla** y **TableDir**, se utiliza para definir columnas que son claves foráneas hacia otras tablas.

Cuando una columna se define para usar una referencia **Selector**, es necesario definir cuál de los subtipos de selector disponibles va a llamar; esto se hace configurando el campo **Referencia clave**.

Como las columnas que usan referencia de selector almacenan claves foráneas (es decir, UUID), deben definirse en base de datos como **VARCHAR(32)** y añadirse una restricción de clave foránea a la tabla.

Visualmente, la diferencia en la UI con **Tabla** y **TableDir** es que, en lugar de mostrar una lista desplegable con todos los valores de la tabla referenciada, se muestra el valor actualmente seleccionado usando algunos filtros.

![](../../../assets/developer-guide/etendo-classic/concepts/Data_Model-21.png)

Cuando se hace clic en el botón junto al cuadro de texto, se abre un pop-up; este pop-up permite seleccionar un valor de entre los disponibles.

![](../../../assets/developer-guide/etendo-classic/concepts/Data_Model-22.png)

###### Cuándo usar referencia de selector

Las referencias de selector son especialmente útiles cuando la tabla foránea tiene un gran número de registros, porque facilitan mucho la tarea de seleccionar un registro.

Solo es posible usar uno de los selectores existentes, los definidos en core. En caso de que ninguno se ajuste a sus requisitos, es posible crear nuevos:

| Nombre del selector     | Tabla referenciada      |
| ----------------------- | ----------------------- |
| Cuenta                  | `C_ValidCombination`    |
| Terceros                | `C_BPartner`            |
| Debt/Payment            | `C_Debt_Payment`        |
| Factura                 | `C_Invoice`             |
| Línea de la factura     | `C_InvoiceLine`         |
| Domicilio               | `C_Location`            |
| Locator                 | `M_Locator`             |
| Parte                   | `C_Order`               |
| Línea de pedido         | `C_OrderLine`           |
| Producto                | `M_Product`             |
| Product Complete        | `M_Product`             |
| Proyecto                | `C_Project`             |
| Shipment/Receipt        | `M_InOut`               |
| Shipment/Receipt Line   | `M_InOutLine`           |

##### Contraseña (no descifrable)

Las columnas con esta referencia se almacenan en la base de datos como un hash del valor que el usuario introdujo; aunque no es posible recuperar el valor original en texto plano, se puede comprobar si un texto plano corresponde a un valor hasheado.

Se utiliza SHA-512 con un salt aleatorio para hashear contraseñas. Anteriormente se utilizaba SHA-1.

Para verificar que un texto plano coincide con un hash (esto es compatible hacia atrás y comprueba ambos algoritmos), use:

```java
boolean matches = PasswordHash.matches(plainTextPassword, hashedPassword);
```

Para generar un nuevo hash use:

```java
String newPassword = PasswordHash.generateHash(plainText);
```

##### Contraseña (descifrable)

El valor de la contraseña se cifra al guardarse; sin embargo, de una forma que permite recuperar la contraseña en texto claro (tal como se introdujo). Un caso de uso de ejemplo es almacenar una contraseña que necesita pasarse posteriormente como texto claro a algún servicio externo (p. ej., la contraseña de un servidor de correo).
#### Referencias en módulos

Se permite que los módulos definan referencias base.

Antes de esto, los módulos de release solo podían definir subreferencias para las referencias base proporcionadas en el core; esto significa que se podían añadir a los módulos nuevas referencias de **Lista**, **Tabla** y **Selector**.
### Validación

Las validaciones permiten filtrar los registros que aparecen en las listas desplegables generadas. Las validaciones son aplicables a las siguientes referencias de datos **Lista**, **Tabla**, **TableDir** y **Botón**.

Cuando una columna tiene una validación, WAD genera un [callout](#callout) para ella (`ComboReload`) para implementar la validación.

#### Definir una validación

Las validaciones se definen en `Application Dictionary` > `Setup` > `Validation Setup` > `Validación`, consisten en una cláusula SQL **where** que se aplicará a la consulta que genera y recupera los datos de la lista desplegable.

Es posible hacer referencia a columnas dentro de la tabla foránea en el código de la validación; para ello, incluya el nombre completo de la tabla. En caso de que la referencia sea de tipo **Lista**, la tabla es `AD_Ref_List` y la columna donde se almacenan los valores es **Costo**.

También es posible usar variables de sesión en el filtro; las variables de sesión van rodeadas por `@`, por lo que `@AD_Client_ID@` hace referencia al cliente con el que el usuario ha iniciado sesión en la aplicación.
### Identificador de registro

Etendo utiliza UUIDs para identificar inequívocamente cada registro internamente dentro de una tabla. Estos valores se almacenan en una columna de la tabla que se define como clave primaria en la base de datos y como columna clave dentro del Diccionario de Aplicación. Los UUIDs son cadenas de 32 caracteres que el sistema genera automáticamente; por ello, estas cadenas tienen muy poca utilidad para el usuario final a la hora de identificar registros. En consecuencia, estos valores se utilizan solo internamente por la aplicación y no se muestran en la UI. En su lugar, los usuarios siempre ven una representación amigable de un registro denominada **identificador de registro**.

Un **identificador de registro** es una simple **concatenación** de los valores de una o varias columnas de un registro dentro de una tabla. Cada tabla definida dentro del Diccionario de Aplicación **DEBE** tener al menos una columna configurada como identificador de registro.

Cuando una de las columnas que forman parte del identificador de registro es una clave foránea a otra tabla, en lugar de concatenar el valor real de la columna (que es un UUID), se toma el identificador de registro del registro correspondiente en la tabla referenciada por la clave foránea y se concatena.

Dado que los identificadores de registro se utilizan para identificar un único registro, deben incluir un conjunto de columnas que se sepa que es único. Esto puede garantizarse a nivel de base de datos añadiendo una restricción única a estas columnas.

#### Definición de un identificador de registro

Los identificadores de registro se definen en `Application Dictionary` > `Tables and Columns` > `Tabla` > `Columna`. Para configurar una columna como parte del identificador de registro de su tabla, marque la casilla `Used as Record identifier`.

Como varias columnas de la misma tabla pueden formar parte del identificador de registro, la forma de definir el orden en que se mostrarán en él se establece en el campo `Secuencia`.
### Callout

Un **Callout** es una pieza de código que se dispara cuando se modifica un campo. El callout está asociado a la columna cuyo campo asociado desencadenará la acción.

##### Qué pueden hacer los Callouts

Los callouts se implementan mediante clases Java, por lo que pueden hacer prácticamente cualquier cosa. Pero debe tenerse en cuenta que se disparan cuando se modifica el campo de la columna a la que están asociados. Esto ocurre antes de guardarlo en la base de datos, por lo que es posible que el registro en la base de datos todavía no exista. Teniendo esto en cuenta, no deberían consultar en la base de datos el registro actual.

Normalmente se utilizan para:

- Cargar o cambiar dinámicamente información en la UI después de un cambio del usuario. Por ejemplo, establecer un precio por defecto cuando se selecciona un producto.
- Mostrar mensajes después de modificar un campo.
- Ejecutar una función Javascript.
- Mover el cursor a un campo.

###### Callouts vs Triggers

Tanto los callouts como los triggers se ejecutan cuando hay cambios en los datos. La principal diferencia entre los callouts y los triggers de base de datos es que los callouts se ejecutan en el front end, mientras que los triggers están en el back end. Esto significa que los callouts deberían afectar principalmente a los datos mostrados en la UI y los triggers a los datos en la base de datos; adicionalmente, los callouts solo se ejecutan cuando el usuario está modificando datos manualmente a través de la UI, pero no se ejecutan en caso de que los mismos datos sean modificados por cualquier otro proceso.

!!!important
    Debido a todas estas razones, no se debería confiar la integridad de los datos únicamente a los callouts. También debería implementarse en la base de datos, mediante triggers o restricciones.

##### Definir un Callout

Existe una [guía](../how-to-guides/How_to_create_a_Callout.md) relacionada con los callouts que puede leer para disponer de un ejemplo paso a paso para la creación de un callout.

###### Diccionario de aplicación

Los callouts se definen en `Application Dictionary` > `Setup` > ventana `Callout` y luego se asocian con la columna que los invocará cuando se modifique.

###### Implementación Java

Los callouts se implementan mediante un Servlet Java.

!!!note
    La forma más sencilla de implementar un callout es usando la clase `SimpleCallout`, que le evita la “fontanería” de construir la respuesta.

Los aspectos a tener en cuenta son:

- El **Comando** con el que se invocan los callouts es siempre **VALOR POR DEFECTO**.
- Los callouts reciben un parámetro llamado `inpLastFieldChanged`; este parámetro tiene el nombre del campo que disparó el callout. Usando este parámetro, es posible reutilizar el mismo callout para diferentes columnas; esto tiene sentido en caso de que la acción para ambas columnas esté relacionada.
- Los callouts deberían usar la plantilla xmlEngine `org/openbravo/erpCommon/ad_callouts/CallOut`.
- Esta plantilla debe recibir un parámetro llamado **array** con la siguiente sintaxis Javascript:

 ```javascript
  var calloutName='MyCalloutName';
  var respuesta = new Array(
  new Array("inpfieldName", "value"),
  new Array('MESSAGE', "Message to display"),
  new Array("EXECUTE", "displayLogic();"),
  new Array("CURSOR_FIELD", "inpfieldName")
  );
 ```
Después de ejecutar un callout con la salida anterior, el resultado sería:

- El campo llamado `inpfieldName` tomaría el valor `value`.
- Se mostraría un mensaje.
- Se ejecutaría la función Javascript `displayLogic()`.
- El campo `inpfieldName` recibiría el foco.

!!!info
    Los tipos de mensajes disponibles: `MESSAGE`, `INFO`, `ERROR`, `SUCCESS`, `WARNING`. `MESSAGE` e `INFO` son equivalentes.

###### Ejecutar en Nuevo

Por defecto, todos los callouts asociados a listas desplegables se ejecutan cada vez que se crea un nuevo registro. Esto se hace para garantizar que toda la lógica implementada en los callouts se ejecute para los valores por defecto que se presentan en el nuevo registro.

En caso de que exista un gran número de listas desplegables con callouts o **ComboReloads**, esto puede causar problemas de rendimiento.

En caso de que se sepa que las validaciones y los callouts para una columna no realizarán ningún cambio al crear un nuevo registro, la ejecución del callout para esa columna puede deshabilitarse durante la creación del nuevo registro. Esto puede hacerse desmarcando el campo **Validar en Nuevo** en la solapa **Columna**.
### Expresiones dinámicas

Valor por defecto, lógica de solo lectura y condición transitoria son valores que permiten una expresión dinámica. Visite [este documento](../concepts/dynamic-expressions.md) que explica cómo se definen las expresiones dinámicas.

---

Este trabajo es una obra derivada de [Modelo de datos](http://wiki.openbravo.com/wiki/Data_Model){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.