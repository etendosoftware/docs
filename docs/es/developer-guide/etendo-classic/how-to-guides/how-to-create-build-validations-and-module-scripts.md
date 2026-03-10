---
tags: 
  - Cómo hacer
  - Validaciones de compilación
  - Scripts de módulo
---
#  Cómo crear validaciones de compilación y scripts de módulo

##  Visión general

Esta sección proporciona información sobre cómo crear tanto una **Validación de compilación** como un **Script de módulo**. Ambos son conceptos muy similares y también se implementan de una forma muy parecida.
## Validaciones de compilación

Una validación de compilación en Etendo es una clase Java que se **ejecuta al principio** de la tarea `update.database`.

El uso principal de las validaciones de compilación es **detener la compilación** porque la instancia está en un estado tal que reconstruir el sistema no se puede hacer de forma segura. En los módulos, las validaciones pueden utilizarse para detener la compilación en caso de que el módulo no pueda instalarse de forma segura en el sistema por algún motivo.

Así, por ejemplo, una validación podría utilizarse para comprobar si **el usuario ha realizado un paso manual de configuración necesario que no se puede automatizar**. O una validación también podría utilizarse para **comprobar si el usuario ha rellenado algunos datos que son necesarios para que el módulo se instale correctamente**.

Las validaciones de compilación son una pieza de código diferente en Etendo, ya que se distribuyen como binarios (clases compiladas), que se ejecutan directamente sin compilarse durante la ejecución.

!!!note
      Las validaciones de compilación no deberían ser un caso habitual. Normalmente, solo deberían ser necesarias cuando hubo un error en una versión anterior del módulo o del Core. El resultado final de una validación es que, si detecta lo que estaba destinada a detectar, el usuario tendrá que realizar acciones manuales para corregir el problema, y esto debería evitarse si es posible por todos los desarrolladores.

### Introducción a la implementación de validaciones de compilación

Los pasos principales para crear una validación de compilación son:

  1. Escribirla (crear una clase Java para cada validación que quiera realizar).
  2. Compilarla (las validaciones de compilación se compilan por separado del resto del código de Etendo, usando una tarea específica de compilación de Gradle).
  3. Probarla (probar cuidadosamente la validación antes de incluirla en su módulo o en el Core).

Para crear una validación de compilación, primero cree una clase que extienda la clase `org.openbravo.buildvalidationBuildValidation`. Esta es una clase abstracta que tiene un método abstracto: `List<String> execute()`

Este método debe implementarse. La clase se cargará al principio de la tarea `update.database`, y se llamará a este método. Se debe devolver una **lista de cadenas**. Si la lista está vacía, la compilación continuará. Si la lista contiene al menos una cadena, se mostrará cada cadena al usuario y la compilación se detendrá. Se supone que cada cadena es un mensaje de error significativo, que muestra al usuario qué necesita corregir en su sistema para que la validación se supere.

### Escritura de la validación de compilación

Como se acaba de explicar, una validación de compilación no es más que una clase que extiende la clase `org.openbravo.buildvalidation.BuildValidation`, e implementa el **método abstracto execute**. Veamos un ejemplo:

```java title="ValidationExample.java"
public class ValidationExample extends BuildValidation {
 
  public List<String> execute() {
    try {
      ConnectionProvider cp = getConnectionProvider();
      PreparedStatement ps = cp
          .getPreparedStatement("SELECT COUNT(*) FROM C_Bpartner WHERE name IS NULL");
      ps.execute();
      ResultSet rs = ps.getResultSet();
      rs.next();
      ArrayList<String> errors = new ArrayList<String>();
      if (rs.getInt(1) > 0) {
        errors
            .add("There are business partners which don't have a defined name. Please fill the name of every business partner before installing the module MyModule.");
      }
      return errors;
    } catch (Exception e) {
      return handleError(e);
    }
  }
}
```

En este ejemplo, pueden verse los puntos principales de cualquier validación de compilación:

  * La clase implementa la clase **BuildValidation** y su correspondiente método execute.
  * En el **método**, puede realizarse la validación (es decir, comprobar si la instancia de Etendo cumple alguna regla específica). Existe un método conveniente `getConnectionProvider()`, proporcionado por la superclase abstracta, que permite realizar consultas directas a la Base de datos. Es importante remarcar que **las validaciones solo deberían realizar consultas a la Base de datos, nunca deberían cambiar el contenido de la Base de datos**. Si es necesario cambiar la Base de datos, pueden utilizarse los scripts de módulo.
  * Finalmente, el método devuelve una **lista de cadenas de error**, que puede estar vacía si la validación fue correcta, o puede contener uno o más errores si el sistema no cumplía la validación.

También puede usar `SqlClass` si es necesario realizar las operaciones de Base de datos.

```java  title="ValidationExample2.java"
public class ValidationExample2 extends BuildValidation {
 
  public List<String> execute() {
    try {
      ConnectionProvider cp = getConnectionProvider();
      ArrayList<String> errors = new ArrayList<String>();
      int numBpartners=Integer.parseInt(ValidationExample2Data.queryBPartners(cp));
      if (numBpartners > 0) {
        errors.add("There are business partners which don't have a defined name. Please fill the name of every business partner before installing the module MyModule.");
      }
      return errors;
    } catch (Exception e) {
      return handleError(e);
    }
  }
}
```

Esto necesita el siguiente archivo `xsql`:

```xml title="ValidationExample2Data.xsql"
<?xml version="1.0" encoding="UTF-8" ?>
 
<SqlClass name="ValidationExample2Data" package="org.openbravo.buildvalidation">
  <SqlMethod name="queryBPartners" type="preparedStatement" return="string">
      <SqlMethodComment></SqlMethodComment>
      <Sql><![CDATA[
          SELECT COUNT(*) FROM C_Bpartner WHERE name IS NULL
          ]]>
      </Sql>
  </SqlMethod>
</SqlClass>
```

!!!info
      Los archivos fuente de la clase deben estar dentro de la carpeta del módulo, en: `src-util/buildvalidation/src`. Y deben seguir las reglas estándar de **paquetes Java**. La carpeta no existirá si es la primera validación, por lo que será necesario crearla.

### Compilación de la validación de compilación

Las validaciones de compilación deberían compilarse usando, como máximo, la última **versión de JDK** soportada.
  
Para compilar la validación de compilación, use el siguiente comando:

```bash
./gradlew compile.buildvalidation -Dmodule=javapackageofmodule
```

!!!info
      En caso de compilar las validaciones de **Etendo Core**, la propiedad module debe establecerse en `org.openbravo`.

Esta tarea compilará las clases Java y las copiará a la carpeta de **compilación** correcta en el módulo, o en `src-util/buildvalidation` del Core.

### Ejecución de la validación de compilación

Las validaciones de compilación se ejecutarán automáticamente en la tarea `update.database`, o en `update.database.mod` si se está aplicando el módulo.

!!!warning
      Las validaciones no se compilarán en esta tarea; deben haberse compilado previamente para poder ejecutarse.

Otro punto importante a remarcar es que las validaciones de compilación se ejecutarán en cada versión del módulo o del Core en la que estén presentes. El desarrollador debe tener esto en cuenta (es recomendable no diseñar validaciones que dependan de la versión; siempre deberían diseñarse para ser genéricas).

!!!note
      Al añadir una validación a Etendo Core, recuerde **incluir las clases binarias** contenidas en
      `src-util/buildvalidation/build/classes/` en el repositorio a medida que se añaden los archivos fuente. Si no, no se ejecutarán (porque las clases no se compilan por defecto en el proceso de compilación; solo se ejecutan si los archivos binarios están ahí).

### Definición de los límites de ejecución de la validación de compilación
  
Las validaciones de compilación proporcionan por defecto un par de mecanismos que permiten controlar cuándo deben ejecutarse:

#### Límites de versión de la validación de compilación

Es posible definir una dependencia con dos versiones de un módulo concreto para identificar cuándo debe ejecutarse la validación de compilación:

  * **Primera versión de ejecución**: define la primera versión desde la cual debe ejecutarse la validación de compilación. Antes de una actualización, si el módulo dependiente tiene una versión menor o igual que esta versión, la validación de compilación **NO** se ejecutará. Al establecer este límite, se garantiza que esta versión y las anteriores no requieren la ejecución de la validación de compilación.

  * **Última versión de ejecución**: define la última versión del módulo dependiente para la cual debe ejecutarse la validación de compilación. Antes de una actualización, si el módulo dependiente tiene una versión mayor o igual que esta versión, la validación de compilación **NO** se ejecutará.

De este modo, la validación de compilación puede ejecutarse solo cuando realmente se necesita, evitando cálculos de tiempo adicionales al actualizar la Base de datos.

El módulo dependiente y sus versiones límite pueden establecerse sobrescribiendo el método
`getBuildValidationLimits()` en nuestra subclase `BuildValidation`:

```java
@Override
protected ExecutionLimits getBuildValidationLimits() {
  return new ExecutionLimits("0", new OpenbravoVersion(3, 0, 28207), new OpenbravoVersion(3, 0, 29495));
}
```

Siguiendo este ejemplo de código, estamos estableciendo que nuestra validación de compilación solo debe ejecutarse al actualizar el módulo core (id = "0") desde una versión entre _3.0.28207_ (primera versión de ejecución) y _3.0.29495_ (última versión de ejecución). De este modo, evitamos la ejecución de la validación de compilación en aquellos casos en los que no aplica.

#### Ejecutar solo una vez

En caso de que sea necesario ejecutar la validación de compilación solo una vez, esto puede cubrirse estableciendo únicamente la **Última versión de ejecución**.

Por ejemplo, si al añadir una comprobación en la versión _1.7.0_ de un módulo, queremos ejecutar la validación de compilación al actualizar desde versiones anteriores a esta versión. Entonces podemos definir sus límites como sigue:

```java
@Override
protected ExecutionLimits getBuildValidationLimits() {
  return new ExecutionLimits(ad_module_id, null, new OpenbravoVersion(1, 7, 0));
}
```

Donde `ad_module_id` es el **UUID** del módulo.

De este modo, la validación de compilación se ejecutará al actualizar el módulo desde cualquier versión anterior a _1.7.0_ y no se volverá a ejecutar.

#### Ejecutar en la instalación

También es posible configurar si la validación de compilación debe ejecutarse al instalar el módulo dependiente definido con el método `getBuildValidationLimits()`. Por defecto, la validación de compilación se ejecutará al instalar el módulo dependiente.

Pero en caso de que no queramos ejecutarla, debe sobrescribirse el método `executeOnInstall()` como sigue:

```java
@Override
protected boolean executeOnInstall() {
  return false;
}
```
## Scripts de módulo

Un **script de módulo** es una tarea que se ejecuta cuando se está aplicando un módulo en la **Base de datos**. Se supone que esta tarea realiza operaciones que deben hacerse en la base de datos y que no pueden realizarse de otra manera.

Conceptualmente, son extremadamente similares a las **Validaciones de compilación**, y los pasos principales para crear un **Script de módulo** son prácticamente los mismos, por lo que es recomendable leer la sección anterior antes de esta.

Los puntos principales de los scripts de módulo son los siguientes:

  * Mientras que las validaciones de compilación se ejecutan al principio de `update.database`, los scripts de módulo se ejecutan a mitad del proceso, cuando las claves foráneas y los triggers de la base de datos han sido deshabilitados.
  * Al igual que con las validaciones de compilación, los scripts de módulo se ejecutarán cada vez que se invoque un `update.database` o `update.database.mod` para ese módulo en particular. Esto significa que **el script debe construirse de tal manera que pueda ejecutarse repetidamente sin problemas**, y esta es una consideración muy importante que el desarrollador debe tener en cuenta.
  * El script de módulo nunca debería fallar. Si falla, la compilación se detendrá, pero como ya se ha iniciado, **el sistema estará en un estado inconsistente** (por ejemplo, todas las claves foráneas y los triggers estarán desactivados). El desarrollador debe evitar esto a toda costa si es posible.

### Introducción a la implementación de scripts de módulo

Al igual que con las validaciones de compilación, un script de módulo es una clase Java que extiende la clase abstracta `org.openbravo.modulescript.ModuleScript` e implementa el método `execute()`. Este método `execute` será llamado por la tarea `update.database`. Este método incluirá la lógica del script de módulo; aquí se realizarán todas las operaciones.

### Escritura del script de módulo

A continuación se muestra un **script de módulo** muy sencillo, que simplemente establece el valor de alguna columna a un valor por defecto en caso de que el valor de la columna sea nulo:

```java title="ModuleScriptExample.java"
public class ModuleScriptExample extends ModuleScript {
 
  public void execute() {
    try {
      ConnectionProvider cp = getConnectionProvider();
      PreparedStatement ps = cp
          .getPreparedStatement("UPDATE mytable SET mycolumn=0 WHERE mycolumn IS NULL");
      ps.executeUpdate();
    } catch (Exception e) {
      handleError(e);
    }
  }
}
```

Los dos puntos principales importantes a tener en cuenta al construir el script son:

  * El script nunca debería fallar. Un fallo dejará al usuario en una situación muy poco amigable (con la compilación detenida a mitad), y **debe evitarse a toda costa**. En este caso, este script no fallará a menos que la tabla no exista.
  * El script debe diseñarse de forma que pueda ejecutarse un **número indefinido de veces**. Este script de ejemplo, por ejemplo, puede ejecutarse varias veces sin problemas (la primera vez establecerá todas las filas que tengan un valor nulo y, después de eso, solo se modificarán las nuevas filas que se hayan insertado; las filas modificadas previamente no se modificarán de nuevo a menos que vuelvan a tener el valor nulo supuestamente incorrecto).

  
!!!info
      Los propios archivos fuente de la clase deben estar dentro de la carpeta del módulo, en la carpeta: `src-util/modulescript/src`. Y deben seguir las reglas estándar de **paquetes Java**. La carpeta no existirá si es el primer script, por lo que será necesario crearla.

### Compilación del script de módulo

Los scripts de módulo deben compilarse utilizando, como máximo, la última **versión de JDK** soportada.

Para compilar el script de módulo, utilice el siguiente comando:

```bash
./gradlew compile.modulescript -Dmodule=<javapackage>
```

!!!info
      En caso de compilar los scripts de **Etendo Core**, la propiedad del módulo debe establecerse en `org.openbravo`.

Esta tarea compilará las clases Java y las copiará a la carpeta de **compilación** correcta en el módulo, o en `src-util/modulescript` de Core.

### Ejecución del script de módulo

Los **scripts de módulo** se ejecutarán automáticamente en la tarea `update.database`, o en `update.database.mod` si se está aplicando el módulo.

!!!warning
      Los scripts de módulo no se compilarán en esta tarea; deben haberse compilado previamente para poder ejecutarse.

Otro punto importante a remarcar es que los scripts de módulo funcionan como las **validaciones de compilación** en lo relativo a los criterios de ejecución; es decir, se ejecutarán en cada versión del módulo, o de Core, en la que estén presentes. El desarrollador debe tener esto en cuenta (es recomendable no diseñar scripts que sean **dependientes de la versión**; siempre deben diseñarse para ser **genéricos**).

Y, como se explicó anteriormente, los scripts también deben diseñarse para producir el mismo resultado si se ejecutan múltiples veces, porque se ejecutarán cada vez que el sistema se recompila o el módulo se actualiza.

!!!info
      Si está añadiendo un script de módulo a Etendo Core, recuerde que necesita **incluir las clases binarias** contenidas en `src-util/modulescript/build/classes/` en el repositorio, del mismo modo que se añaden los archivos fuente. Si no, no se ejecutarán (porque las clases no se compilan por defecto en el proceso de compilación; solo se ejecutan si los archivos binarios están ahí).

### Definición de los límites de ejecución del script de módulo

Los scripts de módulo proporcionan por defecto un par de mecanismos que permiten controlar cuándo deben ejecutarse:

#### Límites de versión del módulo

Es posible definir una dependencia con dos versiones de un módulo en particular para identificar cuándo debe ejecutarse el script de módulo:

  * **Primera versión de ejecución**: define la primera versión desde la cual debe ejecutarse el script de módulo. Antes de una actualización, si el módulo dependiente tiene una versión menor o igual que esta versión, el script de módulo **NO** se ejecutará. Al establecer este límite, nos aseguramos de que esta versión y las anteriores no requieren la ejecución del script de módulo.

  * **Última versión de ejecución**: define la última versión del módulo dependiente para la cual debe ejecutarse el script de módulo. Antes de una actualización, si el módulo dependiente tiene una versión mayor o igual que esta versión, el script de módulo **NO** se ejecutará.

De este modo, el script de módulo puede ejecutarse solo cuando realmente se necesita, evitando cálculos de tiempo extra al actualizar la base de datos.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_build_validations_and_module_scripts-0.png)

El módulo dependiente y sus versiones límite pueden establecerse sobrescribiendo el método `getModuleScriptExecutionLimits()` en nuestra subclase de `ModuleScript`:

```java
@Override
protected ModuleScriptExecutionLimits getModuleScriptExecutionLimits() {
  return new ModuleScriptExecutionLimits("0", new OpenbravoVersion(3,0,27029), 
      new OpenbravoVersion(3,0,27050));
}
```

Siguiendo este ejemplo de código, estamos estableciendo que nuestro `modulescript` solo debe ejecutarse al actualizar el módulo core (id = "0") desde una versión entre _3.0.27029_ (primera versión de ejecución) y _3.0.27050_ (última versión de ejecución). De este modo, evitamos la ejecución de nuestro `modulescript` en aquellos casos en los que no aplica.

#### Ejecutar solo una vez

Un caso típico de uso de `modulescripts` es rellenar los valores de una columna recién añadida. Por lo tanto, es necesario ejecutar el `modulescript` una vez. Esto puede cubrirse estableciendo solo la **Última versión de ejecución**.

Por ejemplo, si añadimos una nueva columna en la versión _1.5.0_ de un módulo, queremos ejecutar el `modulescript` al actualizar desde versiones anteriores a esta versión. Así, podemos definir sus límites de la siguiente manera:

```java
@Override
protected ModuleScriptExecutionLimits getModuleScriptExecutionLimits() {
  return new ModuleScriptExecutionLimits(ad_module_id, null, 
      new OpenbravoVersion(1,5,0));
}
 ```

Donde `ad_module_id` es el **UUID** del módulo.

De este modo, el `modulescript` se ejecutará al actualizar el módulo desde cualquier versión anterior a _1.5.0_ y no se ejecutará más.

#### Ejecutar en instalación

También es posible configurar si el script de módulo debe ejecutarse al instalar el módulo dependiente definido con el método `getModuleScriptExecutionLimits()` o durante la tarea gradle `install`. Por defecto, el script de módulo se ejecutará en los siguientes casos:

  * Al instalar el módulo dependiente
  * En la tarea `install`

Pero en caso de que no queramos ejecutarlo en estos casos, debe sobrescribirse el método `executeOnInstall()` de la siguiente manera:

```java
@Override
protected boolean executeOnInstall() {
  return false;
}
```

#### Ejecutar solo en `install`

En caso de que queramos configurar un `modulescript` para que se ejecute solo en cada `install`, **no** sobrescribimos el método `executeOnInstall()` y definimos los límites de ejecución de la siguiente manera:

```java
@Override
protected ModuleScriptExecutionLimits getModuleScriptExecutionLimits() {
  return new ModuleScriptExecutionLimits(ad_module_id, null, 
      new OpenbravoVersion(0,0,0));
}
```

Este trabajo es una obra derivada de [Cómo crear validaciones de compilación y scripts de módulo](http://wiki.openbravo.com/wiki/How_to_create_build_validations_and_module_scripts){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.