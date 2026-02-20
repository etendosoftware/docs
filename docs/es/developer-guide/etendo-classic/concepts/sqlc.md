---
title: SQLC
tags:
    - SQL
    - SQLC
    - Clase Java
    - Sentencias

status: beta
---

# SQLC

!!! example  "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.

!!! warning
    En general, cualquier código nuevo debería escribirse utilizando la nueva [Capa de acceso a datos](../concepts/data-access-layer.md). El código basado en `SqlC/xsql` solo debería utilizarse en casos especiales o cuando exista código antiguo.
## Visión general

**SqlC** es una herramienta que **genera una clase Java a partir de un archivo con sentencias SQL**. La clase Java contiene el código necesario para conectarla a una base de datos, dar formato a la sentencia, ejecutarla y devolver el conjunto de resultados desde la base de datos. Esta es una función común para la ejecución de cualquier sentencia. SqlC evita esta tarea repetitiva generando el código Java a partir de las definiciones de las sentencias deseadas.
## Un ejemplo sencillo

Este ejemplo sencillo muestra cómo usar SqlC con una sentencia SQL `select` simple.

``` SQL
    SELECT Attribute, Value, AD_Window_ID 
    FROM AD_Preference 
    WHERE AD_User_ID = ?
```

Para que SqlC genere una clase java que ejecute esta consulta, es necesario colocarla en un archivo xml; por ejemplo: `src/org/openbravo/howto/Howto_data.xsql`.

    
``` XML
    <?xml version="1.0" encoding="UTF-8" ?>
     
    <SqlClass name="HowtoData" package="org.openbravo.howto">
        <SqlMethod name="select" type="preparedStatement" return="multiple">
        <Sql>
            SELECT Attribute, Value, AD_Window_ID 
            FROM AD_Preference 
            WHERE AD_User_ID = ? 
        </Sql>
        <Parameter name="adUserId"/>
        </SqlMethod>
    </SqlClass>
```

Esto indica a SqlC que se debe generar una clase java `org.openbravo.howto.HowtoData`. Esta clase se utilizará para contener el resultado de la consulta y contendrá un método llamado `select` con un parámetro llamado `adUserId`. El método ejecutará la sentencia `select` y devolverá un array de objetos HowtoData que contienen el resultado de la consulta.

El siguiente fragmento muestra las partes interesantes de la clase generada desde la perspectiva de su usuario.

``` java
    package org.openbravo.howto;
     
    class HowtoData implements FieldProvider {
     
        public String attribute;
        public String value;
        public String adWindowId;
     
        public String getField(String fieldName) {
        if (fieldName.equalsIgnoreCase("attribute"))
            return attribute;
        else if (fieldName.equalsIgnoreCase("value"))
            return value;
        else if (fieldName.equalsIgnoreCase("ad_window_id") || fieldName.equals("adWindowId"))
            return adWindowId;
        else {
            log4j.debug("Field does not exist: " + fieldName);
            return null;
        }
        }
     
        public static HowtoData[] select(ConnectionProvider connectionProvider, String adUserId) throws ServletException {
```

Como se muestra, la clase contiene tres atributos `public` de tipo `String` que se corresponden con las columnas resultado en la sentencia `select`. Sin embargo, los nombres de los atributos se han modificado para ajustarse al estilo camelCase, que se utiliza habitualmente en java.

Además, se generó un único método `getField` para permitir obtener datos mediante el nombre del campo, que puede pasarse tanto en estilo camelCase como mediante el nombre original de la columna en la sentencia `select`.

Por último, para la sentencia `select` se generó un método java llamado `select` que toma un parámetro correspondiente a la definición del parámetro en el archivo xsql. El método ejecuta la consulta y devuelve su resultado mediante un array del tipo de la clase generada.
## Conceptos básicos

Después del breve ejemplo, esta sección explica los conceptos básicos que son aplicables a todos los casos de uso de SqlC. Una vez mostrados, la siguiente sección se divide en los diferentes tipos de sentencias y cómo utilizar cada una de ellas con SqlC.

### Convención de nomenclatura

Los archivos fuente para SqlC son archivos XML con la extensión xsql. Solo los archivos con esta extensión serán recogidos por los scripts de compilación de Etendo. Cuando se ejecuta la herramienta SqlC, se genera una única clase Java por cada archivo xsql. Esta clase contiene un método por cada sentencia definida en el archivo xsql. Los patrones de nombre de archivo para los archivos fuente y el archivo generado resultante son los siguientes:

```
* <parte arbitraria>_data.xsql => <parte arbitraria>Data.java 
```

Cada archivo debe residir dentro de una carpeta que coincida con el paquete Java en el que se espera el archivo generado. La ubicación del archivo fuente xsql en la estructura de directorios debe coincidir con el paquete declarado dentro del archivo.

### Estructura de los archivos fuente y generados

No existe un DTD o XSD formal para la estructura de los archivos xsql. En su lugar, la estructura se explica aquí de manera informal.

Como cada archivo xsql corresponde a un único archivo Java generado, debe contener exactamente una etiqueta XML para definir la clase Java. De forma opcional, se puede especificar un único comentario de clase, que se traslada como un comentario javadoc a nivel de clase en el archivo Java generado.

``` XML
<SqlClass name="HowtoData" package="org.openbravo.howto">
<SqlClassComment>Example for a sqlc generated class</SqlClassComment>
</SqlClass>
```

Los dos atributos de `SqlClass` definen el nombre de la clase Java y el nombre del paquete, y deben ser nombres permitidos para clases y paquetes Java.

La clase Java generada implementa una interfaz simple denominada `FieldProvider`.

``` java
public interface FieldProvider {
public String getField(String fieldName);
}
```

Como ya se mostró en el ejemplo anterior, este método es una forma de acceder a los datos de la clase. Alternativamente, se puede acceder directamente a los atributos generados.

### Visibilidad de la clase generada

De forma predeterminada, la clase Java generada no contendrá un modificador de acceso especial. Esto significa que la clase solo puede utilizarse desde dentro del paquete Java en el que está definida. No es visible desde otros paquetes Java.

Si una clase generada debe tener una visibilidad diferente, entonces puede utilizarse el atributo opcional **accessModifier**. El valor de este atributo se utilizará para definir la visibilidad de la clase generada.

El siguiente ejemplo muestra cómo definir una clase generada como public, de modo que pueda utilizarse desde cualquier paquete.
 
```XML

    <SqlClass name="PublicHowtoData" package="org.openbravo.howto" accessModifier="public">
    ...
    </SqlClass>

package org.openbravo.howto;
 
public class PublicHowtoData implements FieldProvider {
    ...
}
```

### Definición de SqlMethod: partes comunes

La parte central de un archivo xsql son las sentencias definidas en su interior. Aquí se muestran las partes comunes de la definición de un `SqlMethod`. Los atributos que son específicos de cada tipo de sentencia se explican en los capítulos correspondientes más adelante.

```
<SqlMethod
name="name"
static="true,false"
type="{constant,preparedStatement,statement,callableStatement}"
connection="true,false"
<SqlMethodComment></SqlMethodComment>
<Sql>
    sql statement
</Sql>
</SqlMethod>
```

Esta etiqueta XML define una única sentencia / método Java. El atributo name corresponde directamente al método Java que se creará para la sentencia.

De forma predeterminada, todos los métodos se generan como métodos static; este comportamiento puede cambiarse con el atributo static.

El atributo type distingue entre lo siguiente:

- constant 
    - Sin acceso a base de datos 
    - Función de utilidad para rellenar una instancia de una clase de datos 

- preparedStatement,statement 
    - Estos son los tipos principales y corresponden a consultas a base de datos o select. 
    - La diferencia entre ambos es el uso de un JDBC statement o un JDBC PreparedStatement para ejecutar la sentencia. 

- callableStatement 
    - Este tipo solo se utiliza para llamadas a métodos PL 

### Gestión de conexión / transacción

De forma predeterminada, cada invocación de un método generado por SqlC se ejecuta dentro de una única transacción que se confirma (commit) automáticamente. Además, cada invocación obtiene una nueva conexión a base de datos del pool de conexiones para ejecutar la sentencia.

Para este propósito, cada método Java generado contiene un parámetro adicional de tipo `ConnectionProvider` que no está incluido en la lista de parámetros definida en el archivo xsql.

 
    public static HowtoData[] select(ConnectionProvider connectionProvider, String adUserId) throws ServletException {

El método generado obtiene su conexión a base de datos a través de esta interfaz.

!!!info
    Si la invocación del método se realiza desde un Servlet Java que extiende la clase `HttpSecureAppServlet` de Etendo, entonces la propia clase del servlet puede pasarse aquí, ya que implementa indirectamente esa interfaz.  
  
Sin embargo, en algunas circunstancias, este comportamiento predeterminado no es el deseado. Si varias sentencias deben ejecutarse dentro de una única transacción, esta gestión automática de transacciones no es suficiente.

En este caso, el atributo opcional connection permite una gestión de transacción/conexión más granular. Si se añade con el valor true, la firma del método generado es ligeramente diferente, como se muestra aquí:

```
public static HowtoData[] select(Connection conn, ConnectionProvider connectionProvider, String adUserId) throws ServletException {
```

Aquí, se puede pasar explícitamente un objeto de conexión a la función. Si quien llama deshabilita el autocommit para esta conexión y luego pasa la misma conexión en varias invocaciones de métodos, podrá controlar la transacción con más detalle.
## Tipos de sentencias

El siguiente capítulo explica un único tipo de sentencia con más detalle y describe los distintos atributos adicionales que son necesarios / útiles en su contexto.

### Consultas

Este primer grupo, y el tipo de sentencias más común, lanza consultas a la base de datos. Este grupo puede dividirse aún más observando el tipo de datos devueltos por la consulta:

#### Devolución de varias filas

Este tipo de sentencia SQL ya se trató en el primer ejemplo sencillo de este documento de conceptos. La consulta devuelve un número de filas igual o mayor que cero y la función Java generada devuelve un array de la clase generada, donde cada entrada del array representa una única fila del `ResultSet`.

!!!note
    Si el usuario de la función solo necesita la primera fila del resultado, entonces debería utilizarse en su lugar el siguiente tipo de sentencia de consulta.  

#### Devolución de una única fila

Este tipo de sentencia SQL difiere únicamente en la forma en que se devuelve el resultado de la consulta. La propia consulta se envía a la base de datos del mismo modo que en las consultas que devuelven varias filas. Sin embargo, el código Java generado lee únicamente la primera fila del `ResultSet` desde la base de datos y la devuelve al usuario.

Este enfoque tiene una serie de beneficios en comparación con leer varias filas y utilizar solo la primera fila.

El primer beneficio se produce cuando el `ResultSet` de la consulta es enorme. Al leer varias filas, el resultado completo y enorme necesita transferirse desde la base de datos a Java. Además, en Java es necesario reservar un array enorme para almacenar el resultado, lo cual puede desbordar fácilmente la memoria disponible.

El segundo beneficio es una mejor usabilidad y un código más legible al utilizar la función generada. El siguiente ejemplo breve muestra código de ejemplo que realiza la misma actividad usando los dos tipos diferentes de sentencias.

```
// sampleCall is defined as returns="multiple"
SampleData[] rows = SampleData.sampleCall(this);
if (rows != null && rows.length > 0) {
SampleData row = rows[0];
...
}
```

```
// sampleCall is defined as returns="single"
SampleData row = SampleData.sampleCall(this);
...
}
```

!!!info
    Este tipo de consulta devuelve una única fila, pero no indica a la base de datos que solo se necesita una única fila. La base de datos aún necesita consultar y devolver todas las filas, lo que potencialmente conlleva una gran sobrecarga. Para evitarlo, la sentencia `select` necesita tener añadidas las partes correspondientes de LIMIT/OFFSET o ROWNUM.  

#### Devolución de un único valor

Si el usuario de una consulta solo necesita un único valor, entonces es posible un modo aún más simple devolviendo directamente un único valor en lugar de un registro o incluso un array de registros.

Este tipo de sentencia es similar al que devuelve una única fila. Envía la consulta a la base de datos y obtiene la primera fila del `ResultSet`.

La diferencia es que aquí solo se lee la primera columna de la primera fila del `ResultSet` y se devuelve al usuario.

La forma más general de pasar esta columna al llamador es especificar un tipo de retorno `"String"`. De este modo, el valor se lee del `ResultSet` con `getString` y se pasa al usuario sin modificar. En el caso de que la consulta no devuelva ningún registro, se devuelve un valor `null`.

Cuando el tipo de retorno se especifica como `"boolean"`, entonces se devuelve un valor `true` si la primera columna no es igual a `"0"`; en todos los demás casos se devuelve un valor `false`.

Cuando el tipo de retorno se especifica como `"date"`, entonces se devuelve un `String` que se construye leyendo la primera columna de la base de datos como una fecha y formateándola como un `String` usando el formato de fecha `"dateFormat.java"`, que se especifica en el archivo de configuración `"Openbravo.properties"` ???. Si la consulta no devuelve ninguna fila, entonces se devuelve al llamador un valor `null`.

Para estos tres tipos de valores de retorno es posible especificar un valor por defecto. Esto se realiza añadiendo el atributo opcional `default=<value>` a la definición de `SqlMethod`. En este caso, se devuelve al llamador el `defaultValue` si la consulta no devuelve ninguna fila.
### Parámetros y modificación de la consulta en tiempo de ejecución

Esta parte explica cómo pasar parámetros a la sentencia de base de datos para completar valores en tiempo de ejecución o incluso modificar parte de la sentencia SQL completa en tiempo de ejecución. Esto aplica a todos los tipos de sentencias que se describen aquí.

Los parámetros que se definen en el archivo xsql acabarán como parámetros de tipo `String` para la clase java generada. El tipo de dato de todos los parámetros siempre será `String`. Los parámetros de la clase generada estarán en el mismo orden en el que aparecen los parámetros en el archivo xsql.

!!!note
    Si modifica una sentencia existente en algún archivo xsql y reordena algunos parámetros, recuerde comprobar si ha cambiado el orden de los parámetros del archivo java. Si es así, todos los llamadores deben actualizarse para pasar los valores de los parámetros en la ubicación correcta. Como todos los parámetros son de tipo `String`, estos cambios no serán detectados por el compilador de java y pueden provocar errores difíciles de encontrar si el llamador pasa un valor específico en un parámetro diferente (después del cambio de orden).  

!!!info
    Si el mismo parámetro (con el mismo nombre) se especifica varias veces para una sentencia, aun así solo se generará un único parámetro java. La ubicación de este único parámetro corresponde a la posición del primer parámetro (de los duplicados) en el archivo xsql.  

#### Parámetros obligatorios

El tipo de parámetros más común son los parámetros no opcionales. Estos simplemente especifican un único valor y una posición predefinida en la sentencia SQL. Un ejemplo de esto es el parámetro `adUserId` en el primer ejemplo. En tiempo de ejecución, su valor se pasa como parámetro a la sentencia JDBC o `preparedStament` y a la ubicación del signo de interrogación correspondiente `?` en la sentencia.

#### Parámetros opcionales

El segundo grupo son los parámetros opcionales. Estos permiten añadir opcionalmente y/o modificar partes de la sentencia SQL en tiempo de ejecución.

Para poder modificar una parte de la sentencia en tiempo de ejecución, es necesario definir una ubicación para la modificación. Esto puede hacerse de dos maneras.

La primera manera es no definir explícitamente una ubicación para el cambio en tiempo de ejecución. En este caso, la ubicación utilizada es directamente después de la palabra `WHERE` en la sentencia SQL. Sin embargo, para hacer el cambio más explícito, no se recomienda esta forma abreviada.

La segunda manera, recomendada, es especificar la ubicación explícitamente usando el atributo `after` en la definición del parámetro. De este modo, se puede referenciar una parte explícita de la consulta para este propósito. El siguiente ejemplo mostrará cómo se ve esto en la práctica.

#### Parámetros opcionales sin tipo

La forma más sencilla de añadir una cláusula `WHERE` opcional a una consulta es pasar un parámetro para ello en tiempo de ejecución e ignorar la parte opcional en caso contrario.

El siguiente ejemplo utiliza esto para consultar todos los pedidos en la base de datos o consultar todos los pedidos de un tercero específico.

```
<SqlMethod name="selectOrders" type="preparedStatement" return="multiple">
<Sql>
    SELECT * from C_Order c
    WHERE 1=1
    ORDER BY c.documentno
</Sql>
<Parameter name="bpartner" optional="true" after="WHERE 1=1">
    <![CDATA[ AND c.C_BPARTNER_ID = ? ]]>
</Parameter>
</SqlMethod>
```

Lo que ocurre en tiempo de ejecución para este ejemplo está definido por el valor del parámetro `bpartner`. Si el valor no es null y no es la `String` vacía `""`, entonces la sentencia SQL ejecutada es la siguiente:

```
SELECT * FROM C_Order c
WHERE 1=1
AND c.C_BPARTNER_ID = ?
ORDER BY c.documentno
```

Si el valor del parámetro es null o la `String` vacía `""`, entonces el parámetro opcional se ignora completamente para la ejecución de la sentencia.

La forma recomendada de especificar la ubicación `AFTER` es añadir cláusulas extra como `WHERE 1=1` o `AND 2=2` a la sentencia. Esto no cambiará el comportamiento de la consulta y siempre se evalúan como true, además de proporcionar una forma sencilla de ver los lugares en la consulta donde se colocarán las partes opcionales.

#### Parámetros opcionales de tipo none

Una variación de esto es un parámetro opcional de `type="none"`. Usando esto, es posible añadir una `String` constante a una sentencia SQL dependiendo del valor de un parámetro.

```
<SqlMethod name="selectOrders" type="preparedStatement" return="multiple">
<Sql>
    SELECT * from C_Order c
    WHERE 1=1
    ORDER BY c.documentno
</Sql>
<Parameter name="processed" optional="true" type="none" after="WHERE 1=1" text="AND c.processed = 'Y'"/>
</SqlMethod>
```

En este ejemplo, si el valor del parámetro es el nombre del parámetro (aquí: `processed`), entonces la parte opcional definida por el parámetro se añade a la sentencia; en caso contrario, la parte opcional se ignora para la ejecución de la sentencia.

#### Parámetros opcionales de tipo argument

Una segunda variación es un parámetro opcional de `type="argument"`. Esto puede usarse para añadir opcionalmente una parte fija y pasar el valor completo del parámetro (un valor arbitrario) a la consulta.

``` SQL
<SqlMethod name="selectOrders" type="preparedStatement" return="multiple">
<Sql>
    SELECT * from C_Order c
    WHERE 1=1
    ORDER BY c.documentno
</Sql>
<Parameter name="processed" optional="true" type="argument" after="WHERE 1=1">
    <![CDATA[ AND c.C_BPARTNER_ID IN ]]>
</Parameter>
</SqlMethod>
```

Aquí, de nuevo, el parámetro opcional se ignora completamente si el valor del parámetro es null o la `String` vacía `""`. En caso contrario, la sentencia ejecutada incluye la parte fija del parámetro seguida del valor del parámetro, sin usar un marcador de posición `?` de la sentencia/`preparedStament`.

Asuma que el valor del parámetro en tiempo de ejecución es `"('17','18','19')"`; entonces la sentencia ejecutada será:

``` SQL
SELECT * FROM C_Order c
WHERE 1=1
AND c.C_BPARTNER_ID IN ('17','18','19')
ORDER BY c.documentno
```

!!!Note
    El valor del parámetro se pasa exactamente tal como se especifica y no se escapa ni se codifica. El llamador de la función debe asegurarse de que no se pasen valores no verificados en el parámetro para evitar inyecciones SQL.  

#### Parámetros opcionales de tipo replace

La última variación de parámetros opcionales se define con `type="replace"`. Estos permiten reemplazar completamente una parte de una sentencia SQL por una parte nueva.

``` SQL
<SqlMethod name="countFrom" type="preparedStatement" return="String" default="">
    <Sql>
    <![CDATA[
        SELECT COUNT(*) FROM FACT_ACCT
    ]]>
    </Sql>
    <Parameter name="tablename" optional="true" type="replace" after="FROM " text="FACT_ACCT"/>
</SqlMethod>
```

En este ejemplo, el parámetro `tablename` puede usarse para cambiar el nombre de la tabla sobre la que se ejecuta el recuento.

!!! note 
    El valor del parámetro se pasa exactamente tal como se especifica y no se escapa ni se codifica. El llamador de la función debe tener cuidado de que no se pasen valores no verificados en el parámetro para evitar inyecciones SQL.
### Consultas desplazables (eficientes en memoria)

Las consultas que devuelven varias filas, tal y como se describe en [Devolver varias filas](#devolver-varias-filas) arriba, pueden consumir una enorme cantidad de memoria cuando devuelven muchas filas. Esto no es un problema si solo se devuelven pocas filas (<1000), pero si el número de filas no está acotado y puede ser mucho mayor, entonces las consultas desplazables, tal y como se describen aquí, pueden funcionar mucho mejor. Este tipo de consultas solo cambia la forma de invocar el `SqlcMethod` desde Java; el texto SQL en sí no necesita modificarse. La interfaz modificada permite obtener las filas de resultado una a una, en lugar de un gran array que contenga todos los datos.

Para utilizar este tipo, use un tipo de retorno desplazable.

``` XML
<?xml version="1.0" encoding="UTF-8" ?>
 
<SqlClass name="HowtoData" package="org.openbravo.howto">
    <SqlMethod name="select" type="preparedStatement" return="scrollable">
    <Sql>
        SELECT Attribute, Value, AD_Window_ID 
        FROM AD_Preference 
        WHERE AD_User_ID = ? 
    </Sql>
    <Parameter name="adUserId"/>
    </SqlMethod>
</SqlClass>
```

Esto creará una clase Java como la siguiente:
 
``` java
package org.openbravo.howto;
 
class HowtoData implements FieldProvider, ScrollableFieldProvider {


public boolean hasData() {}
public boolean next() throws ServletException {}
public ReportGeneralLedgerData get() throws ServletException {}
public void close() {}
 
public static HowtoData select(ConnectionProvider connectionProvider, String adUserId) throws ServletException {
```

Como se ve aquí, el método `select` ya no devuelve un `HowtoData`, sino una instancia de la clase `HowtoData`. Esta instancia puede utilizarse después para recuperar el resultado fila a fila.

!!!info "Importante"
    Llame siempre al método `close()` cuando utilice un `SqlMethod` desplazable. Es recomendable hacerlo usando un bloque try-finally, tal y como se muestra en los ejemplos siguientes.  
  
Si desea pasar los datos a Jasper Reports usando el método estándar renderJR, no es necesario hacer nada especial, ya que existe una versión de renderJR que puede usar directamente esos `SqlMethod` desplazables, tal y como se muestra a continuación:

```java
HowtoData data = null;
try {
    data= HowtoData.select( .... );
    renderJR(..., data, ....);
} finally {
    if (data != null) {
    data.close();
    }
}
```
  
Si desea simplemente usar un `SqlMethod` desplazable en su propio código, puede obtener los resultados fila a fila, tal y como se muestra en el siguiente ejemplo. Un bucle simple es suficiente.

``` java
HowtoData data = null;
try {
    data= HowtoData.select( .... );
    while (data.next()) {
    HowtoData oneRow = data.get();
    }
} finally {
    if (data != null) {
    data.close();
    }
}
```
### Campos adicionales

La etiqueta de campo opcional permite añadir columnas adicionales que no pertenecen al `ResultSet` a la clase, las cuales se rellenan y se devuelven en las ejecuciones de los métodos.

Esta etiqueta necesita dos atributos obligatorios: `name` y `value`. El atributo `name` especifica el nombre definido por el usuario del campo adicional. El atributo `value` especifica el valor que debe contener el campo.

Se pueden usar dos valores posibles:

- **void**: Al usar el valor void, el campo adicional se rellenará con la cadena vacía "" y es simplemente un campo adicional rellenado que puede ser utilizado por quien invoque el método.
- **count**: Al usar este valor, cada registro contendrá su índice dentro del `ResultSet`, donde el primer registro tiene el índice uno.
### Actualizaciones

El segundo grupo de posibles sentencias son las actualizaciones de base de datos. Esto incluye las siguientes sentencias SQL:

- INSERT 
- UPDATE 
- DELETE 

Para todas estas sentencias, la base de datos devuelve el número de filas afectadas en lugar de un resultado de consulta. En SqlC, el `returnType` correspondiente para el `SqlMethod` es `rowCount`. Especificar este `returnType` da como resultado dos acciones. En primer lugar, el tipo de retorno de la función Java generada se cambia a `int`, correspondiente al número de filas afectadas por la sentencia. En segundo lugar, este tipo es utilizado implícitamente por SqlC para saber que la sentencia SQL es una actualización en lugar de una consulta.

Otro ejemplo breve muestra cómo se ven el archivo xsql y el método Java generado para sentencias de tipo actualización.

```XML
<SqlMethod name="setInDevelopment" type="preparedStatement" return="rowCount">
<Sql>
        UPDATE ad_module
        SET isIndevelopment = 'Y'
        WHERE ad_module_id = ?
</Sql>
<Parameter name="adModuleId"/>
</SqlMethod>
``` 

``` java
public static int setInDevelopment(ConnectionProvider connectionProvider, String adModuleId) throws ServletException {
 
    ...
 
    return(updateCount);
    }
```
### Llamadas a funciones PL

Esta sección describe cómo se puede usar SqlC para llamar a funciones PL y procedimientos PL. Los procedimientos PL son métodos que se ejecutan dentro del DBMS y que no devuelven un valor de resultado (esto se puede comparar con un método que devuelve `void` en Java). Las funciones PL son similares, pero sí devuelven un resultado de función. Además, ambos tipos de métodos PL pueden tener parámetros de tipo `out`. Estos no aceptan un valor de entrada, sino que se usan para devolver un valor de resultado a través de este parámetro. Usando esta funcionalidad, un método PL puede devolver más de un valor de resultado por llamada de función. Si un método PL no contiene parámetros de tipo `out`, entonces se puede usar una sentencia `select` como forma alternativa de llamar al método, lo cual algunos desarrolladores consideran más intuitivo. Sin embargo, si hay parámetros de tipo `out`, debe usarse una llamada de función SqlC como la que se presenta aquí.

Primero, un ejemplo sencillo si la función PL no tiene ningún parámetro de tipo `out`.

``` XML
<SqlMethod name="process1003900000" type="callableStatement" return="object" object="ActionButtonData">
    <Sql><![CDATA[
    CALL C_TAXPAYMENT_POST(?)
    ]]></Sql>
    <Parameter name="adPinstanceId"></Parameter>
</SqlMethod>
```

``` java
    public static ActionButtonData process1003900000(ConnectionProvider connectionProvider, String adPinstanceId) throws ServletException {
 
    ...
 
    return (objectActionButtonData);
    }
```

La definición es similar a la definición de sentencias de actualización. Los atributos necesarios para definir la llamada a la función PL son:

- **type="callableStatement"**: Esto indica a SqlC que el `SqlMethod` es una llamada a una función PL. Generará código para ello usando un `callableStatement` de JDBC.
- **return="object"**: Esto especifica que el valor de retorno de la función Java será un objeto.
- object="ActionButtonData": Esto especifica la clase Java que se usará como valor de retorno. Los atributos de la clase Java se usan para transportar los valores de retorno del método PL de vuelta al llamador.
- **import="<fully qualified classname>"** (opcional): Este atributo opcional se puede usar si la clase del atributo `object` no está en el mismo paquete Java que la clase generada por SqlC. El valor de la sentencia `import` se usa entonces para generar una sentencia `import` de Java que importa la clase desde un paquete diferente. Solo se usará el atributo `import` del primer `SqlMethod` para este propósito.

En este ejemplo no teníamos ningún valor de retorno que transportar de vuelta al código Java. SqlC sigue usando un objeto como valor de retorno, pero su tipo puede ser simplemente la clase generada por SqlC y, en esencia, no se utiliza.

La segunda clase de llamadas a funciones PL son aquellas que sí devuelven datos al llamador mediante un parámetro de tipo `out`. Estas se usan rara vez en el core de Etendo, ya que la mayoría de los métodos PL que devuelven datos son funciones PL que pueden usarse mucho más fácilmente como parte de una sentencia SQL `select` simple.

Otro ejemplo describe el uso de esta clase de llamadas a funciones:

``` XML
<SqlMethod name="nextDocType" type="callableStatement" return="object" object="CSResponse">
    <Sql><![CDATA[
    CALL AD_Sequence_DocType(?,?,?,?)
    ]]></Sql>
    <Parameter name="cDocTypeId"/>
    <Parameter name="adClientId"/>
    <Parameter name="updateNext"/>
    <Parameter name="razon" type="out"/>
</SqlMethod>
```

 
``` java
class CSResponse {
    String razon;
}
 
class DocumentNoData implements FieldProvider {
    public static CSResponse nextDocType(ConnectionProvider connectionProvider, String cDocTypeId, String adClientId, String updateNext) throws ServletException {
    CSResponse objectCSResponse = new CSResponse();
 
    ...
    objectCSResponse.razon = ...
    ...
 
    return(objectCSResponse);
    }
}
```

La diferencia con el ejemplo anterior es que aquí el procedimiento PL `AD_Sequence_DocType` tiene un cuarto parámetro `razon` de tipo `out`. SqlC espera que la clase Java que se usa para transportar el resultado tenga un atributo accesible con el mismo nombre `razon`. El valor del parámetro `out` se obtendrá después de la llamada a la función y se almacenará en el atributo de una instancia de la clase de resultado (aquí: `objectCSResponse.razon`). Este valor puede leerse posteriormente de forma sencilla desde el llamador.

En este ejemplo se usa una clase (CSResponse) distinta de la clase generada por SqlC (`DocumetNoData`) para transportar el valor de retorno. Alternativamente, se podría haber usado la clase generada por SqlC para lograr el mismo efecto.
### Constantes

El tipo de sentencia es diferente de los descritos anteriormente. No realiza ninguna interacción con la base de datos.

En su lugar, el propósito de la función java generada es crear, rellenar y devolver una única instancia de la clase de datos con valores proporcionados como parámetros.

La función generada crea un nuevo objeto del tipo de la clase de datos. A continuación, todos los campos que corresponden a una columna devuelta por la última función procesada en el archivo xsql se inicializan con algún valor. Si el campo corresponde a una subetiqueta `Parameter` del método, entonces el campo se inicializa con el valor del parámetro proporcionado; en caso contrario, se inicializa con una cadena vacía “” .

La lista de parámetros de la función generada contiene exactamente los parámetros especificados en las subetiquetas `Parameter` presentes; todos los parámetros de la función son de tipo String.

---

Este trabajo es una obra derivada de [SQLC](http://wiki.openbravo.com/wiki/SQLC){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.