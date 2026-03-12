---
title: Convenciones de codificación Java
tags:
    - Java
    - Codificación
    - Convenciones

status: beta
---

#  Convenciones de codificación Java

!!! example  "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.
##  Visión general

Este documento proporciona una descripción de los estándares de codificación y los principios de codificación utilizados en el desarrollo de Etendo.

En Etendo utilizamos IntelliJ IDEA; para una descripción sobre cómo configurar IntelliJ, consulte este [Cómo hacerlo](../getting-started/installation/install-etendo-development-environment.md).
##  Convenciones de código estándar

Etendo utiliza las convenciones de codificación estándar definidas por Sun en [Convenciones de código para el lenguaje de programación JavaTM](https://www.oracle.com/java/technologies/javase/codeconventions-contents.html){target="\_blank"}.
## Código escaneable: fácil de leer, fácil de cambiar

El código escaneable tiene una característica principal (además de ser legible y comprensible): es código en el que es posible leer y cambiar partes del código sin necesidad de comprender completamente toda la base de código (el resto del código). Por lo tanto, el código escaneable es naturalmente robusto y más fácil de mantener que el código no escaneable.

Al crear código escaneable, un término abstracto es importante: la encapsulación léxica. La encapsulación léxica significa concretamente que el código se agrupa en métodos claramente definidos que no son más largos que una ventana/pantalla.

Otros principios que ayudan a crear código escaneable y, por tanto, mantenible y comprensible:

* Utilice nombres claros, legibles y que revelen la intención para variables, métodos y clases
* Utilice variables intermedias para aumentar la legibilidad (véase más abajo)
* Cree métodos cortos que quepan en una ventana/pantalla
* Defina variables y métodos dentro del ámbito y cerca de donde se utilizan
* Utilice espaciado horizontal para agrupar sentencias
* Mantenga los métodos claros y enfocados. Deje que un método haga una sola cosa: recuperar un valor o cambiar un valor

Estos son los principios principales que ayudan a la escaneabilidad; otros «qué hacer» tratados en este documento también facilitan el mantenimiento, la corrección, la calidad y la robustez.
##  Principios principales de codificación

Además de los facilitadores de legibilidad rápida y de las Convenciones de codificación estándar (más relacionadas con el formato), un programador de Etendo debe seguir estas directrices:

###  Formato

####  Utilice un IDE con formateo automático del código al guardar

Aunque se puede recomendar IntelliJ, hay otros IDE populares disponibles. En cualquier caso, el código fuente siempre debe formatearse automáticamente (cuando se guarda un archivo) utilizando las convenciones estándar de código Java de Sun, tal y como se definen arriba.

Para habilitar el formateo del código al guardar y utilizar el estándar de formateo de código de Etendo, asegúrese de importar las preferencias proporcionadas en la carpeta `config/` en los proyectos de desarrollo. Este paso de importación se describe [aquí](../getting-started/installation/intellij-code-formatting.md).

####  Copyright de Etendo sobre la propiedad intelectual de Etendo (obligatorio)

Cada archivo que sea propiedad intelectual de Etendo debe tener el siguiente mensaje de copyright en la parte superior:

```
/*
 *************************************************************************
 * The contents of this file are subject to the Etendo License
 * (the "License"), you may not use this file except in compliance with
 * the License.
 * You may obtain a copy of the License at  
 * https://github.com/etendosoftware/etendo_core/blob/main/legal/Etendo_license.txt
 * Software distributed under the License is distributed on an
 * "AS IS" basis, WITHOUT WARRANTY OF ANY KIND, either express or
 * implied. See the License for the specific language governing rights
 * and limitations under the License.
 * All portions are Copyright © 2021–2025 FUTIT SERVICES, S.L
 * All Rights Reserved.
 * Contributor(s): Futit Services S.L.
 *************************************************************************
 */
```    

El año en la declaración de copyright es el año actual cuando el archivo es nuevo y contiene dos fechas si el archivo se actualiza en un año diferente al de su creación. Por ejemplo, un archivo creado en 2020 y modificado por última vez en 2025 tendrá los siguientes años: 2020 - 2025, especificados cerca del signo (C):

```
* All portions are Copyright (C) 2020 - 2025  Futit Services S.L.
```

####  Espaciado vertical

Utilice el espaciado vertical para separar diferentes partes del código y hacer que el código sea menos denso de leer. Aquí tiene un ejemplo sin espaciado vertical:

```
try {
    configuration = new Configuration();
    mapModel(configuration);
    setInterceptor(configuration);
    configuration.addProperties(getOpenbravoProperties());
    // add a default second level cache
    if (configuration.getProperties().get(
        Environment.CACHE_PROVIDER) == null) {
    configuration.getProperties().setProperty(
    Environment.CACHE_PROVIDER,
    HashtableCacheProvider.class.getName());
    }
    sessionFactory = configuration.buildSessionFactory();
    log.debug("Session Factory initialized");
} catch (final Throwable t) {
    throw new OBException(t);
}
```

Y aquí tiene el mismo ejemplo con espaciado horizontal para que sea más fácil de leer:

```
try {
    configuration = new Configuration();
 
    mapModel(configuration);
 
    setInterceptor(configuration);
 
    configuration.addProperties(getOpenbravoProperties());
 
    // add a default second level cache
    if (configuration.getProperties().get(
            Environment.CACHE_PROVIDER) == null) {
    configuration.getProperties().setProperty(
    Environment.CACHE_PROVIDER,
    HashtableCacheProvider.class.getName());
    }
 
    sessionFactory = configuration.buildSessionFactory();
 
    log.debug("Session Factory initialized");
} catch (final Throwable t) {
    // this is done to get better visibility of the exceptions
    t.printStackTrace(System.err);
    throw new OBException(t);
}
```
###  Política de documentación del código

Un código bien documentado y comentado es excelente y ayuda a comprender el significado del código, mejorando así la productividad y evitando errores futuros.

La política de documentación del código de Etendo tiene como objetivo combinar un proceso de documentación de código ligero que aporte valor a un desarrollador al navegar por el código de Etendo en su IDE. Los comentarios y la documentación deben ser fáciles de mantener y estar actualizados con el código que describen.

La documentación y los comentarios se pueden dividir en dos partes principales: Javadoc y comentarios en línea.

En Etendo, los comentarios Javadoc tienen dos usos principales: servir como base para generar páginas HTML de Javadoc y documentación técnica, y dar soporte a funcionalidades específicas de los IDE actuales, por ejemplo, mostrar el Javadoc al pasar el ratón sobre métodos y constantes.

Los comentarios en línea se utilizan para aclarar el significado del código y las decisiones de implementación subyacentes que pueden influir en decisiones de desarrollo futuras.

Tenga en cuenta que todos los comentarios y la documentación deben estar en inglés usando la notación de EE. UU. (por ejemplo: organization en lugar de organisation).

####  Javadoc de clase (obligatorio)

Cada clase debe tener una sección Javadoc bien formateada en la parte superior. El comentario de documentación de la clase debe describir la función general de la clase y su relación con otras clases. Los comentarios de documentación de la clase no pueden contener detalles de implementación, ya que pueden cambiar rápidamente con el riesgo de tener comentarios desactualizados. El Javadoc de la clase debe contener anotaciones `@author` con el nombre/login de los desarrolladores que han trabajado en esa clase.

Al escribir comentarios Javadoc de clase, proporcione también anotaciones `@link` y `@see` a clases relacionadas. Esto ayuda a situar la clase en el contexto de otras clases.

A continuación se muestra un ejemplo de documentación de clase de la clase Entity:

```
/**
    * Models the business object type. The Entity is the main concept in the
    * in-memory model. An entity corresponds to a {@link Table} in the database. An
    * Entity has properties which are primitive typed, references or lists of child
    * entities.
    * 
    * @see Property
    * @see ModelProvider
    * 
    * @author iperdomo
    * @author mtaal
    */
```

####  Javadoc de método (obligatorio)

Cada método público en la base de código de Etendo debe tener un comentario Javadoc.

Hay una excepción a esta regla: los getters/setters que no hacen más que obtener o establecer un miembro de la clase no deberían tener un comentario Javadoc. La razón principal es que el Javadoc para estos métodos no aporta mucho valor.

El Javadoc de un método debe describir la lógica general del método sin demasiados detalles de implementación. Deben describirse la entrada y la salida del método. Otras reglas que deben seguirse:

- Cada parámetro debe describirse usando la anotación `@param` (no deje anotaciones `@param` vacías) 
- El valor de retorno debe describirse usando la anotación @return (también aquí, evite anotaciones de retorno vacías) 
- Si el método lanza una UncheckedException, entonces esta excepción debe mencionarse en el Javadoc usando la anotación `@throws. 
- Debe documentarse específicamente si un método puede devolver null para que quien lo invoque pueda tenerlo en cuenta. 

```
/**
* The main entry point. This method walks through the elements in the root
* and parses them. The children of a business object (in the xml) are also
* parsed. Referenced objects are resolved through the
* {@link EntityResolver}.
* <p/>
* After a call to this method the to-be-inserted objects can be retrieved
* through the {@link #getToInsert()} method and the to-be-updated objects
* through the {@link #getToUpdate()} method.
* 
* @param xml
*   the xml string
* @return the list of BaseOBObject present in the root of the xml. This
*   list contains the to-be-updated, to-be-inserted as well as the
*   unchanged business objects
*/
```

o

```
/**
* Validates the values of the properties of the entityObject. The
* validation messages are collected into one ValidationException.
* 
* @param entityObject
*   the entity instance
* @throws ValidationException
*/
public void validate(Object entityObject) {
    ....
}
```

####  Javadoc para miembros de clase

Los miembros no deberían tener Javadoc, ya que un miembro de clase siempre es privado.

####  Javadoc para constantes

Las constantes public final static deben tener JavaDoc. Las constantes privadas no deberían tener Javadoc.

####  Formato de Javadoc

El JavaDoc debe usar construcciones estándar de documentación, como enlazar al Javadoc de otras clases, y utilizar el formato de Javadoc. Visite [esta página](https://www.oracle.com/java/technologies/){target="\_blank"} para más información.

####  Comentarios en línea

Los comentarios en línea pueden ser cruciales para que un desarrollador comprenda el significado del código y esté informado sobre decisiones de implementación anteriores. Sin embargo, al comentar tenga en cuenta lo siguiente:

- La filosofía general es que solo hay una necesidad mínima de comentarios: el propio código debería ser legible (usando nombres descriptivos y variables para almacenar resultados intermedios). 
- Los comentarios solo deberían añadirse si aportan valor y proporcionan una visión más profunda que no sea directamente visible en el propio código. 
- Los comentarios en línea son difíciles de mantener y se desactualizan rápidamente porque el código cambia con rapidez. Por lo tanto, los comentarios deben colocarse lo más cerca posible del código al que se refieren. 
- ¡Elimine los comentarios desactualizados! 

A continuación se muestra un ejemplo de algunos comentarios en línea de la clase OBQuery. En este caso, los comentarios en línea se utilizan para mostrar ejemplos que son gestionados por esa parte del código.

    
```
// The following if is there because the clauses which are added should
// all be and-ed. Special cases which need to be handled:
// left join a left join b where a.id is not null or b.id is not null
// id='0' and exists (from ADModelObject as mo where mo.id=id)
// id='0'
boolean addWhereClause = true;
if (whereClause.trim().length() > 0) {
    if (!whereClause.toLowerCase().contains("where")) {
    // simple case: id='0'
    whereClause = " where (" + whereClause + ")";
        addWhereClause = false;
    } else {
    // check if the where is before the from
    final int fromIndex = whereClause.toLowerCase().indexOf("from");
    int whereIndex = -1;
    if (fromIndex == -1) {
        // already there and no from
        // now find the place where to put the brackets
        // case: left join a left join b where a.id is not null or
        // b.id is not null
 
        whereIndex = whereClause.toLowerCase().indexOf("where");
        check.isTrue(whereIndex != -1, "Where not found in string: " + whereClause);
    } else {
        // example: id='0' and exists (from ADModelObject as mo
        // where mo.id=id)
        // example: left join x where id='0' and x.id=id and exists
        // (from ADModelObject as mo where mo.id=id)
 
        // check if the whereClause is before the first from
        whereIndex = whereClause.toLowerCase().substring(0, fromIndex).indexOf("where");
    }
 
    if (whereIndex != -1) {
        // example: left join x where id='0' and x.id=id and exists
        // (from ADModelObject as mo where mo.id=id)
        addWhereClause = false;
        // now put the ( at the correct place
        final int endOfWhere = whereIndex + "where".length();
        whereClause = whereClause.substring(0, endOfWhere) + " (" + whereClause.substring(endOfWhere) + ")";
    } else { // no whereclause before the from
        // example: id='0' and exists (from ADModelObject as mo
        // where mo.id=id)
        whereClause = " where (" + whereClause + ")";
        addWhereClause = false;
    }
    }
}
```
###  Gestión de excepciones

####  Crear únicamente excepciones que no necesiten ser capturadas (Runtime Exception)

A menudo puede utilizar la OBException estándar u otra excepción existente dentro del código base de Etendo. Sin embargo, cuando sabe que el código que llama va a querer capturar una excepción específica, entonces puede tener sentido crear una excepción propia para el módulo específico que se está desarrollando.

####  Extender OBException

Al crear una nueva excepción, extienda siempre OBException. OBException se encarga del logging. Además, esta excepción es una excepción no comprobada (unchecked Exception). Todas las nuevas excepciones deberían ser excepciones no comprobadas.

####  Añadir información de contexto a su excepción

Al lanzar una nueva excepción o al capturar, empaquetar y volver a lanzar una excepción, es vital que se añada información de contexto al mensaje de la excepción. Solo entonces es posible determinar para qué objeto de negocio o para qué situación falla un método.

```
if ((p = propertiesByName.get(propName)) == null) {
    throw new OBException("Property " + propName
        + " not defined for entity " + this);
}
```

!!!info
    En este caso, el 'this' tiene sentido porque el objeto implementa el método `toString` (consulte el siguiente do).

!!!note
    Al añadir información de contexto a una excepción, tenga en cuenta posibles nuevas excepciones al crear la excepción.

    ``` 
        
        try {
        ...
        } catch (Exception e)
        throw new OBException("Exception when submitting order " +
            order.getId() + " with customer " + 
            order.getCustomer().getId(), e);
        }
    ```

Este lanzamiento de excepción fallará cuando el pedido sea null o el cliente del pedido sea null. Este NPE ocultará entonces la excepción real.
### Usar construcciones de Java

Haga uso de las siguientes construcciones de Java:

- Colecciones tipadas (obligatorio)   
    
    Por lo tanto, no use ninguna de estas construcciones: 

    ```
    List businessPartners = new ArrayList();
    List<Object> businessPartners = new ArrayList<Object>();
    List<?> businessPartners = new ArrayList<?>();
    ```

    Pero hágalo así:
    
    ```
    List<BusinessPartner> businessPartners = new ArrayList<BusinessPartner>();
    ```


- Bucle for mejorado (obligatorio)   
    
    No use el bucle for antiguo:
        
    ``` 
    for (int i = 0; i < businessPartners.size(); i++) {
        ...
    }
    ```

    Pero use esto:
    
    ```
    for (BusinessPartner businessPartner : businessPartners) {
        ...
    }
    ``` 

* Enumeraciones (cuando corresponda)
### Implementar métodos coherentes

Los métodos deben ser pequeños y estar enfocados; un método debe hacer una sola cosa y no tener efectos secundarios más allá de lo que revela el nombre. El nombre del método debe estar alineado con el nivel de abstracción de la clase y debe revelar la intención, ser descriptivo y fácil de leer.

Un método debe o bien responder a una pregunta, es decir, devolver un valor (calculado), o bien realizar un único cambio (establecer un valor).

Los métodos no deben tener más de uno, dos o tres parámetros. Un mayor número de parámetros debe encapsularse en un objeto.

Los parámetros de un método deben tratarse como entrada y no deben ser modificados por el método.
###  Nomenclatura

La nomenclatura es muy importante. Los buenos nombres hacen que los programas sean legibles, aumentan la productividad y evitan errores cuando los desarrolladores cambian código existente. A continuación se incluyen algunas directrices importantes al nombrar clases, métodos y miembros/parámetros en Etendo:

- Los nombres deben estar siempre en inglés (notación US) 
- Los nombres deben ser pronunciables y fáciles de buscar 
- El nombre de una clase y de una interfaz debe ser un sustantivo, mientras que el nombre de un método siempre contiene un verbo 
- Debe quedar claro para el lector qué significa el nombre: el nombre debe revelar la intención 
- Un nombre debe consistir en las palabras/términos que correspondan al marco mental del lector
###  Programación defensiva

La programación defensiva es un enfoque de desarrollo mediante el cual el desarrollador tiene explícitamente en cuenta que se producirán situaciones de error en la aplicación. Esto se hace explícito añadiendo en el código sentencias de comprobación de invariantes y de precondiciones/postcondiciones.

**Protección para casos no implementados**

Al gestionar una lista específica de casos, proteja siempre frente a un caso nuevo que no esté gestionado en el código. Por ejemplo, no haga esto:
    
    ```
    if (value.equals(CASE_ONE)) {
      handleCaseOne();
    } else if (value.equals(CASE_TWO) {
      handleCaseTwo();
    } else if (value.equals(CASE_THREE) {
      handleCaseThree();
    }
    ```

Pero gestione siempre la situación en la que se añade un caso nuevo sin que el código lo conozca:

    ```
    if (value.equals(CASE_ONE)) {
      handleCaseOne();
    } else if (value.equals(CASE_TWO) {
      handleCaseTwo();
    } else if (value.equals(CASE_THREE) {
      handleCaseThree();
    } else {
      throw new ArgumentException("Unhandled case: "  + value);
    }
    ```

**Realice comprobación de invariantes (programación defensiva)**

El "Haga" anterior es un ejemplo de programación defensiva. Con la programación defensiva usted asume que se producirán condiciones ilegales y que las comprobará. Por tanto, un (muy) buen programador tendrá sentencias de comprobación de precondiciones y postcondiciones a lo largo de su código. Aunque Java proporciona la sentencia `assert`, es mejor utilizar una clase de utilidad específica de Etendo para esto: la clase `org.openbravo.base.util.Check`.

Esta clase proporciona métodos para comprobar `false`, `true`, `null`, `instanceof`, etc.
###  Usar variables intermedias para aumentar la legibilidad

```
// less readable
if (writable && (!hasReferenceAttribute || 	
    businessObject.isNewOBObject())) {
    ....
}
    
// more readable, intention revealing
final boolean allowUpdate = writable && 
    (!hasReferenceAttribute || 	
    businessObject.isNewOBObject());
    
if (allowUpdate) {
    ...
}
```
### Uso de logging: cuando sea apropiado

El logging es especialmente apropiado cuando el sistema se está configurando o inicializando. De este modo, más adelante en el log, se puede validar que el sistema se inicializó correctamente.

Además, en el caso de cálculos específicos (como generar una sentencia SQL o ejecutar un script), puede tener sentido registrar el input y el output.

Sin embargo, el principal problema del logging es que el log puede llenarse con bastante rapidez de información menos útil. Por ello, en muchos casos, puede tener más sentido combinar programación defensiva con excepciones con mucha información de contexto, en lugar de optar por un logging extensivo.

A continuación se muestra un ejemplo de cómo hacer uso del logging en Etendo:

- cree un miembro de log estático (private y final) que sea el Logger de log4j
- el nombre del logger es el nombre de la clase
- al registrar un error/excepción haga: `log.error("string", error)` (el orden de los parámetros es importante aquí). Añada información de contexto al mensaje.

```  
public class MyClass {
  private static final Logger log = Logger.getLogger(MyClass.class);
     
  public void myMethod(String param) {
    log.debug('debug code');
    try {
        ....
    } catch (Exception e) {
        log.error("Exception in myMethod with parameter " + param, e);
        ....
    }    
    }
```
### Código y nombre en un único nivel de abstracción/genericidad

Se debe crear una clase/tipo para un nivel genérico/nivel de abstracción específico.

Por ejemplo, considere una clase `Order` con dos subclases `SalesOrder` y `PurchaseOrder`. `Order` se define en un nivel genérico, lo que significa que los métodos de `Order` deben definirse en ese mismo nivel genérico. Un método `getPrice` sería, por ejemplo, un método extraño a nivel de `Order`, pero lógico a nivel de `SalesOrder`. Por otro lado, un método `getCost` sería lógico a nivel de `Order`, ya que tanto `SalesOrder` como `PurchaseOrder` tienen una característica de coste.
###  Preferir ramificación por clase/tipo frente a ramificación por `if`

Cada sentencia `if-then-else` es un ejemplo de ramificación por `if`: en función de alguna condición, un método se comporta de una forma u otra. La ramificación por `if` es fácil y rápida de programar.

Sin embargo, en algunos casos tiene sentido considerar la creación de subclases para separar el comportamiento ramificado en distintas clases. Esto aplica especialmente cuando varias sentencias `if` están relacionadas, comprueban la misma condición y la condición está relacionada con el estado de la instancia.

Tras separar las ramas en distintos subtipos, la única ramificación por `if` que queda es la factoría que suministra la subclase correcta en función de algunos parámetros.

Considere este ejemplo:

```
public class Property {
    private boolean isPrimitive;
        
    public String getTypeName() {		
    final String typeName;
    if (isPrimitive()) {
        typeName = getPrimitiveType().getName();
    } else {
        typeName = getTargetEntity().getClassName();
    }
    return typeName;
    }
    
    public boolean allowNullValues() {
    if (!isPrimitive()) {
        return true;
    }
    return (getPrimitiveType().getName().indexOf('.') != -1);
    }
        
    ....
}
```

En este caso tiene sentido dividir la clase `Property` en una clase `PrimitiveProperty` y una clase `ReferenceProperty`, que ambas extienden una clase `Property`. El resultado es mucho más legible:

```
public class PrimitiveProperty extends Property {
    public String getTypeName() {		
    return getPrimitiveType().getName();
    }
    
    public boolean allowNullValues() {
    return (getPrimitiveType().getName().indexOf('.') != -1);
    }
 
    ...
}
    
public class ReferenceProperty extends Property {
    public String getTypeName() {		
    return getTargetEntity().getClassName();
    }
    
    public boolean allowNullValues() {
    return true;
    }		
    
    ...
}
```
###  Use los prefijos is/has/can para los getters booleanos

Los IDE generarán de forma estándar el getter correcto para un booleano. Sin embargo, al codificar manualmente getters, siempre se debe usar uno de los prefijos: is/has/can.
### Implementar `toString` en casos específicos

Al implementar un nuevo conjunto de objetos, considere implementar el método `toString` de estos objetos. Esto facilita mucho el uso de estos objetos en el registro (logging) y en los mensajes de excepciones.
### No hacer en el manejo de excepciones

**Evitar bloques Catch que no gestionan la excepción**

Un error común es tener un bloque catch (en una estructura try-catch) que solo imprime la excepción, pero no la gestiona posteriormente. Por ejemplo:

```
try {
    properties.load(new FileInputStream(theFile));
} catch (FileNotFoundException e) {
    // TODO Auto-generated catch block
    e.printStackTrace();
} catch (IOException e) {
    // TODO Auto-generated catch block
    e.printStackTrace();
}
```

Esto debería cambiarse por un bloque catch que relance la excepción con nueva información de contexto, o bien añadir un comentario indicando por qué la excepción no necesita gestionarse más.

**No ocultar excepciones capturadas**

Este “no hacer” se refiere a capturar una excepción pero no propagarla como causa de la nueva Exception lanzada:

```
try {
    properties.load(new FileInputStream(theFile));
} catch (Exception e) {
    throw new MyException("Something went wrong: " + e.getMessage());
}
```

El enfoque correcto es este (véase el segundo parámetro en la llamada al constructor):

```
try {
    properties.load(new FileInputStream(theFile));
} catch (Exception e) {
    throw new MyException("Something went wrong: " + e.getMessage() + " when calling with params " + param, e);
}
```

!!!Note
    Observe que en el segundo caso se añadió información de contexto al mensaje de la excepción.

**No lanzar instancias de Exception o Error**

Lanzar una instancia directa de Exception o Error no se considera una buena práctica de programación:

```
if (errorOccurred) {
    throw new Exception("An error occurred");
}
```

En lugar de Error/Exception, siempre debería lanzarse una instancia de `OBException` (o de una subclase). Si está desarrollando un conjunto de clases para un dominio común, entonces puede tener sentido introducir una clase de excepción para ese dominio. Solo introduzca una nueva excepción si tiene sentido que otra parte del código la capture.

Una nueva clase de excepción debería heredar de `OBException`.

```
if (errorOccurred) {
    throw new MySpecificException("An error occurred: " + additionalContextInformation);
}
```

**No crear bloques catch vacíos sin comentario**

Puede haber un motivo para tener un bloque catch vacío. Sin embargo, siempre debe incluirse un comentario en el bloque catch vacío para dejar claro por qué la excepción no se propaga. Por ejemplo, esto está mal:

```
boolean isALong = false;
try {
    Long.parseLong(myStringLong);
    isALong = true;
} catch (NumberFormatException e) {
}
```

y esto es correcto (además, repetir `isALong = false` hace el código más claro):

```
boolean isALong = false;
try {
    Long.parseLong(myStringLong);
    isALong = true;
} catch (NumberFormatException e) {
    // Exception ignore on purpose
    // is not a long in this case	
    isALong = false;
}
```

**No olvidar eliminar los TODO autogenerados**

El código anterior también muestra otro error: dejar TODO autogenerados en el código. Esto debe evitarse, ya que da la impresión de que el desarrollador no terminó su trabajo aquí (“mantenga el camping ordenado”).

**No usar Vector (solo cuando sea realmente necesario)**

En muchas partes del código de Etendo se utiliza un Vector para una colección ordenada. La principal diferencia entre un ArrayList y un Vector es que un Vector está sincronizado y un ArrayList no. Sin embargo, la gran mayoría del código de Etendo se accede en un único hilo. Por tanto, es mejor usar un ArrayList. Solo en el caso poco frecuente de acceso multihilo debería usarse un Vector.

**No extender/implementar una interfaz solo por sus constantes**

Por ejemplo:

```
public interface TheConstants {
    public final String YES = "yes";
}
    
public class MyClass implements TheConstants {
    
    public boolean isYes(String value) {
    return YES.equals(value);
    }
}
```

Como YES está declarado en otro archivo fuente, no es evidente de forma directa para el lector del código de dónde proviene.

**No usar double/float**

Los tipos double (y float) de Java son muy imprecisos para cálculos decimales (por ejemplo, para facturas o gestión de inventario). Por ejemplo, el siguiente programa:

```
final double a = 0.58;
System.err.println(a * 100);
```

imprimirá esto:

```    
57.99999999999999
```

Para cálculos decimales, use siempre BigDecimal.

**No pasar Null**

Aunque no siempre puede evitarse, siempre debe extremarse la precaución al pasar un argumento null a un método. Un método que pueda manejar argumentos null debería indicarlo explícitamente en un comentario.

**No devolver Null**

Al igual que al pasar argumentos null, lo mismo aplica a los valores de retorno. Preferiblemente, los valores de retorno de un método nunca deberían ser null. Se prefiere usar una excepción para indicar que no se encontró un objeto u otra situación de error. Por supuesto, hay casos en los que tiene sentido devolver valores null. Esto debe hacerse con cuidado y el método debería indicar explícitamente en un comentario que puede devolver valores null.

**No mantener código comentado**

El código comentado debería eliminarse lo antes posible. Comentar código es habitual cuando se trabaja sobre código existente. Sin embargo, cuando el trabajo principal ha finalizado, el código comentado debería eliminarse. Hay casos poco frecuentes en los que tiene sentido mantener código comentado durante un tiempo. En ese caso, deben añadirse comentarios adicionales para explicar por qué el código sigue ahí (y comentado).

**Tenga cuidado con parámetros boolean (u otros llamados selectores)**

Un método con parámetros boolean puede resultar confuso, ya que a menudo los argumentos boolean se usan para realizar ramificaciones if dentro de un método. Al ver la llamada al método, no queda claro directamente cuál es el significado de un parámetro boolean (u otro parámetro constante). Por ejemplo, con esta llamada:

```    
BigDecimal mainInventory = computeInventory(product, quantity, false);
``` 

no queda claro qué significa el último parámetro. Esto puede reescribirse de dos formas:

- Método 1: añadir una variable boolean (con un nombre descriptivo) para almacenar el valor y usar la variable en la llamada al método: 

    ```
    final boolean computeForMainLocation = false;
    BigDecimal mainInventory = computeInventory(product, quantity, computeForMainLocation);
    ```

- Método 2: crear dos métodos separados, cada uno cubriendo un caso: 

    ```
    BigDecimal mainInventory = computeInventoryMainLocation(product, quantity);
    BigDecimal subInventory = computeInventorySubLocation(product, quantity);
    ```

El segundo caso es mucho más expresivo. La contrapartida entre ambos métodos es que, en el segundo enfoque, se crean muchos más métodos (con nombres similares), mientras que en el primer enfoque se requiere una variable adicional.

**Evitar condicionales negativos**

Los condicionales negativos son difíciles de leer, y los condicionales doblemente negativos son prácticamente imposibles de leer. Por ejemplo:

```
// less readable
if (!file.exists()) {
    ...
}
    
// almost unreadable
if (!file.wasNotRemoved()) {
    ...
}
```

**No haga esto...**

Algunas cosas que no deberían estar presentes en un archivo fuente Java:

- Miembros static no privados y no final
- Miembros de instancia no privados (genere siempre un accesor para ellos)

**No usar valores constantes directamente; use constantes con nombre**

El código Java nunca debería contener valores constantes directos:

```
return "yes".equals(usage);
// or
if (fieldName.equalsIgnoreCase("TABNAME"))
```

Coloque siempre las constantes en un miembro `public static final` separado de la misma clase o en una clase de constantes separada.

**No cambiar parámetros de entrada**

Evite cambiar el valor de las entradas de un método. Normalmente, quien llama a un método (en Java) no espera esto. Si realmente es necesario cambiar el valor de un parámetro, hágalo explícito en el nombre del método.

**Comparación de String usando ==**

No compare String usando ==:

```    
if (newC_ValidCombination_ID == "") {...}
```

Haga esto:
 
```
if ("".equals(newC_ValidCombination_ID)) {
```

**Tenga cuidado con el tipo del argumento al usar equals**

Considere el siguiente ejemplo:

```
BigDecimal fAmortizationvalue = ....
if (!fAmortizationvalue.equals(0)) {...}
```

Esto está mal (¡la cláusula if siempre es false!), ya que el argumento 0 se convierte a double por Java. Un double siempre es distinto de un BigDecimal.

**Tipos inmutables: métodos que devuelven el objeto adaptado**

Hay ciertos métodos en la API de Java que no modifican el objeto, sino que devuelven un objeto adaptado. Tenga en cuenta que esto aplica especialmente a objetos inmutables. Aquí hay dos ejemplos de código incorrecto:

```
BigDecimal priceList = new BigDecimal(0);
String str = "aaa";
priceList.setScale(PricePrecision, BigDecimal.ROUND_HALF_UP);
str.replace("aaa", "bbb");
```

Los métodos `setScale` y `replace` no cambiarán el objeto `priceList` ni el objeto str, sino que devolverán una nueva instancia. El código correcto es:

```
BigDecimal priceList = new BigDecimal(0);
String str = "aaa";
priceList = priceList.setScale(PricePrecision, BigDecimal.ROUND_HALF_UP);
str = str.replace("aaa", "bbb");
```

**Usar miembros static o no static en un servlet**

Una instancia en ejecución de Etendo solo tendrá una o unas pocas instancias de cada objeto servlet. El contenedor de servlets (Tomcat) puede usar una instancia de servlet para múltiples hilos al mismo tiempo. Esto significa que múltiples hilos acceden a la misma instancia de servlet y llaman a sus métodos, teniendo acceso al mismo miembro (static o no static).

Para evitar problemas multihilo, ninguna clase servlet debería tener miembros static o no static que sean manipulados por los métodos post o get.

**No hacer en nomenclatura**

No use español u otras palabras o terminología que no sea inglés.

No use codificación en los nombres: húngara o de miembro (el guion bajo inicial), no comience el nombre de una interfaz con una I mayúscula.
##  Desarrollo guiado por pruebas

Es crucial que, para la nueva funcionalidad, se creen uno o más casos de prueba en la suite de pruebas de Etendo. Tiene mucho sentido respaldar su desarrollo con casos de prueba:

- Un caso de prueba demuestra que la funcionalidad está implementada y funciona correctamente. 
- Un caso de prueba puede validar que la funcionalidad siga funcionando en el futuro. 
- Los casos de prueba proporcionan un punto de entrada mucho más sencillo (y, por tanto, más productivo) para probar la funcionalidad que iniciar Etendo y recorrer la interfaz web. 
- Un caso de prueba puede utilizarse como demostración y como descripción de cómo debe funcionar el software. 

Los casos de prueba de Etendo deben crearse en la carpeta `src-test` del proyecto de Etendo.

Consulte este [Cómo hacerlo](../how-to-guides/how-to-create-testcases/how-to-create-jest-testcases.md) y este [Cómo hacerlo](../how-to-guides/how-to-create-testcases/how-to-create-junit-testcases.md) para obtener más información sobre cómo crear casos de prueba en Etendo.
##  Calidad y convenciones

Para obtener información sobre este punto, visite [calidad y convenciones](http://www.slideshare.net/srikanthps/practices-for-becoming-a-better-programmer-presentation?src=related_normal&rel=1443810){target="\_blank"}.
##  Tenga en cuenta

También existen algunos constructos estándar de Java que deben utilizarse con cierta precaución y con cierto entendimiento de los procesos subyacentes:

###  ThreadLocal y la reutilización de objetos Thread en Tomcat

Un ThreadLocal es un gran mecanismo para almacenar instancias singleton por thread y hacer que solo estén disponibles en ese thread. Sin embargo, al utilizar ThreadLocals es necesario entender que Tomcat reutiliza instancias de thread de una solicitud a otra (no al mismo tiempo). Esto significa que los datos almacenados en un ThreadLocal en un thread pueden reaparecer en otra solicitud (reutilizando ese mismo objeto Thread).

###  Class.forName y la carga de clases

Cuando necesita cargar dinámicamente una clase, dispone de diferentes opciones de carga de clases. Dentro de Tomcat, el uso de Class.forName funciona. Sin embargo, es importante que entienda cómo funciona la carga de clases de Java cuando se utiliza un mecanismo de carga dinámica de clases. Para más contexto, consulte esto y sus referencias: [Clases Java y carga de clases](https://developer.ibm.com/languages/java/){target="\_blank"}.

###  Bloques synchronized

Los bloques synchronized no siempre son una forma segura de gestionar el acceso multihilo. Consulte aquí una descripción detallada de los procesos subyacentes y posibles soluciones: [Bloqueo con doble comprobación](https://www.cs.umd.edu/~pugh/java/memoryModel/DoubleCheckedLocking.html){target="\_blank"}.

---

Este trabajo es una obra derivada de [Convenciones de codificación Java](http://wiki.openbravo.com/wiki/Java_Coding_Conventions){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.