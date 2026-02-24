---
title: Procesos
tags:
  - Conceptos
  - Procesos SQL
  - Procesos Java
  - Métodos de ejecución
  - Programación de procesos
---
# Procesos
  
## Visión general

Un proceso es una serie sistemática de acciones dirigidas a un fin. Un proceso recibe algunos parámetros y, teniéndolos en cuenta, realiza algunas acciones para obtener un resultado. Etendo define dos tipos principales de procesos: _Procesos SQL_ y _Procesos Java_.

Todos los procesos (así como los [Informes](../../../developer-guide/etendo-classic/how-to-guides/How_to_create_a_Report.md)) se gestionan desde la misma ventana: `Application Dictionary > Informes y procesos`. 

Una vez definido un proceso, puede añadirse al menú para ser llamado directamente desde allí, puede invocarse mediante un botón o puede programarse para ejecutarse en segundo plano.

Los procesos en segundo plano pueden configurarse como _Prevenir ejecuciones concurrentes_. Antes de que se ejecute un proceso con este atributo, se comprueba que no existan otras instancias del mismo proceso ejecutándose al mismo tiempo; en ese caso, se aborta la nueva ejecución.

### Parámetros

Cuando un proceso (SQL o Java) o un informe Jasper se configura como _Estándar_, se genera y muestra automáticamente un mensaje emergente al invocarlo; este mensaje tiene este aspecto:

![](../../../assets/developer-guide/etendo-classic/concepts/Processes-0.png)

Este emergente tiene una sección con información sobre el proceso; esta información se obtiene del campo _Ayuda_ en la solapa _Informes y procesos_.

También solicita una serie de parámetros y, finalmente, hay dos botones: _Aceptar_ para iniciar el proceso y _Cancelar_ para cerrar el emergente y no hacer nada más. En caso de que el proceso no requiera ningún parámetro, esa sección estaría vacía.

Cuando este tipo de proceso requiere parámetros, deben definirse en la solapa `Application Dictionary > Informes y procesos > Parámetro`.


![](../../../assets/developer-guide/etendo-classic/concepts/Processes-1.png)

Los parámetros se definen de forma muy similar a como se definen las columnas. En función del campo _Referencia_, la UI generada asignada al parámetro será diferente.

Veamos algunos de los campos más importantes en esta solapa:

  * *Nombre columna BD* : este es el nombre con el que se pasará el parámetro al proceso. Cuando el proceso vaya a utilizar este parámetro, tendrá que usar este nombre. 
  
!!!note
      Tenga en cuenta que `Postgresql` distingue entre mayúsculas y minúsculas. En caso de que el parámetro haga referencia a una columna existente en la base de datos (por ejemplo, si es un parámetro de tipo búsqueda), entonces el campo _Nombre columna BD_ debe tener las mismas mayúsculas/minúsculas que la columna en el Diccionario de Aplicación. 
  
  * *Secuencia* : es un valor numérico para ordenar el parámetro en el emergente. 
  * *Elemento de aplicación* : es el [Elemento](Element_and_Synchronize_Terminology.md) que se utilizará para obtener la etiqueta; de este modo, los parámetros son traducibles. 
  
!!!note 
    También es posible establecer o no este elemento como *Mantenido centralmente*. 

  * *Referencia*, *Clave de búsqueda de referencia* y *Validación*: estos tres campos funcionan exactamente igual que los mismos al definir referencias para columnas. 
  * *Rango* : si está marcado, el emergente mostrará dos parámetros para definir un rango: el primer parámetro se llamará como se especifica en el campo _Nombre columna BD_ y el segundo tendrá el mismo nombre con el sufijo _HASTA_. 

### Definición de procesos

Los procesos pueden ser de dos tipos diferentes: _Procesos SQL_ y _Procesos Java_. Los procesos SQL se implementan en el lenguaje SQL y son ejecutados por el motor de base de datos. Los procesos Java se implementan en el lenguaje Java y son ejecutados por el servidor de aplicaciones.

#### Procesos SQL

Los _Procesos SQL_ se implementan mediante procedimientos almacenados de base de datos. 

!!!info
    Para más información, consulte [Cómo crear un procedimiento almacenado](../../../developer-guide/etendo-classic/how-to-guides/.How_to_create_a_Stored_Procedure.md).

Los procesos SQL se definen en `Application Dictionary > Informes y procesos`. El único campo a tener en cuenta para este tipo de procesos es *Procedimiento*: es el nombre del procedimiento en la base de datos. 

!!!note
    Como los procedimientos SQL se asignan a módulos, deben nombrarse siguiendo las reglas de nomenclatura: el nombre del procedimiento debe comenzar con el
    DBPrefix del módulo.

Como el emergente para procesos SQL siempre se genera automáticamente, el campo *Patrón de la Interfaz de Usuario* debe establecerse como _Estándar_.

En caso de que el proceso requiera algún parámetro, es posible definirlos. 

!!!info
    Para saber más sobre cómo hacerlo, consulte [Parámetros](#parámetros).

#### Procesos Java

Los procesos Java se implementan mediante clases Java. 

!!!info
    Para más información, consulte [Cómo crear un proceso Java](../../../developer-guide/etendo-classic/how-to-guides/.How_to_create_a_Java_Based_Process.md).

Los procesos Java también se definen en la ventana `Application Dictionary > Informes y procesos`. Dependiendo del _Patrón de la Interfaz de Usuario_ que utilicen, pueden dividirse en _Estándar_ y _Manual_. Además, si el _Patrón de la Interfaz de Usuario_ se establece como _Manual_, es necesario incluir una entrada en la solapa *Process mapping* para hacerlo accesible en el `web.xml`.

!!!note
    El emergente utilizado para invocar procesos Java definidos con _Estándar_ _Patrón de la Interfaz de Usuario_ se genera automáticamente de la misma forma que se hace la interfaz para los procesos SQL.

Para configurar un proceso Java para que tenga UI Estándar, simplemente establezca el campo _Patrón de la Interfaz de Usuario_ como _Estándar_ en la cabecera de `Application Dictionary > Informes y procesos`.

También es necesario indicar la clase Java que va a implementar el proceso. Esto se hace añadiendo un nuevo registro en la solapa *Process class*. Al menos un registro en esta solapa debe estar marcado como predeterminado.

!!!info
    Si el proceso requiere parámetros, pueden definirse en la solapa *Parámetro* tal y como se explica en la sección [Parámetros](#parámetros) de este documento.

### Ejecución de procesos

!!!note
    Es necesario definir la compilación del proceso para poder ejecutarlo.
    Este paso puede realizarse ejecutando ` ./gradlew smartbuild ` y
    reiniciando Tomcat posteriormente.  

  
Los procesos pueden ejecutarse desde la interfaz de usuario desde un menú o con un botón. También pueden programarse para ejecutarse en segundo plano sin ninguna interacción del usuario.

#### Ejecutar un proceso desde una opción de menú

Para ejecutar un proceso desde una opción de menú, necesita definir una nueva opción de menú que ejecute el proceso. Los menús se definen en `General Setup > Application > Menu`. En el campo *Acción* debe seleccionarse la entrada *Proceso*; después, en el campo *Proceso* seleccione el proceso. Se ejecutará inmediatamente y, a continuación, se guardará.

Por último, pulse el botón *Árbol* para organizar la nueva opción de menú en el árbol de menús; ahora el proceso definido puede ejecutarse seleccionando este nuevo menú creado.

#### Ejecutar un proceso desde un botón

Para ejecutar un proceso con un botón, necesita definir una columna que haga referencia a un botón. En `Application Dictionary > Tables and Columns`, vaya a la columna que desea utilizar para ejecutar el proceso y, en el campo *Referencia*, seleccione la entrada *Botón*; después, en el campo *Proceso* seleccione el proceso que desea ejecutar y guarde.

Al ejecutar un proceso con un botón, el ID de registro del registro actual seleccionado de la tabla se pasará al proceso. Esto permite ejecutar funciones para registros específicos.

#### Ejecutar un proceso en segundo plano

Los procesos en segundo plano se definen en `General Setup > Process Scheduling > Process Request`. 

!!!info
    Para más información, consulte [Cómo crear un proceso en segundo plano](../../../developer-guide/etendo-classic/how-to-guides/how-to-create-a-background-process.md).

En esta ventana puede definir un proceso en segundo plano. El proceso a ejecutar puede seleccionarse en el campo *Proceso*. A continuación, defina la programación del proceso en segundo plano y quedará listo para su uso.

!!!note
    No es necesaria ninguna interacción del usuario para ejecutar el proceso; por lo tanto, no aparecerá ningún emergente solicitando parámetros adicionales.

##### Parar un proceso en segundo plano
 
  
En la ventana Monitor de procesos se muestra un botón *Parar Proceso* en aquellos procesos que implementan la interfaz KillableProcess mientras un proceso se está ejecutando (Estado = Procesando). La interfaz KillableProcess le permitirá parar su proceso utilizando un mecanismo de parada.

**Mecanismo para parar**

El mecanismo que su proceso en segundo plano utiliza para pararse a sí mismo puede variar entre implementaciones. Sin embargo, la idea principal en cualquier implementación debería ser comprobar periódicamente algún indicador durante la ejecución para ver si se ha solicitado una parada y, si el indicador está establecido, abortar de algún modo la ejecución del resto del trabajo del job.


Veamos un ejemplo:

aquí tenemos un proceso dummy que simplemente imprime el identificador en el log para todos los terceros:

```java    
    package com.openbravo.example.killprocess.process;

    import org.apache.log4j.Logger;
    import org.hibernate.ScrollMode;
    import org.hibernate.ScrollableResults;
    import org.openbravo.dal.service.OBCriteria;
    import org.openbravo.dal.service.OBDal;
    import org.openbravo.model.common.businesspartner.BusinessPartner;
    import org.openbravo.scheduling.ProcessBundle;
    import org.openbravo.service.db.DalBaseProcess;
    import org.openbravo.service.db.DbUtility;
    import org.quartz.JobExecutionException;

    public class DummyProcess extends DalBaseProcess {
     
      private static final Logger log4j = Logger.getLogger(DummyProcess.class);
     
      @Override
      protected void doExecute(ProcessBundle bundle) throws Exception {
        try {
     
          // Get all business partners
          final OBCriteria<BusinessPartner> bpCri = OBDal.getInstance().createCriteria(
              BusinessPartner.class);
          bpCri.setFetchSize(1000);
          final ScrollableResults partnerScroller = bpCri.scroll(ScrollMode.FORWARD_ONLY);
          int i = 1;
          // Loop all business partners using a ScrollabeResults to avoid performance issues
          while (partnerScroller.next()) {
            final BusinessPartner bp = (BusinessPartner) partnerScroller.get()[0];
            // Print the Identifier for every business partner
            log4j.info(bp.getIdentifier());
     
            if ((i % 100) == 0) {
              OBDal.getInstance().getSession().clear();
            }
            i++;
     
          }
          partnerScroller.close();
        } catch (Exception ex) {
          Throwable e = DbUtility.getUnderlyingSQLException(ex);
          log4j.error("Error in DummyProcess", e);
          throw new JobExecutionException(e.getMessage(), e);
        }
     
      }
     
    }
```

*Proceso parable*

Ahora veremos el mismo proceso, pero con la interfaz `KillableProcess` implementada con el método kill.

```java
    package com.openbravo.example.killprocess.process;

    import org.apache.log4j.Logger;
    import org.hibernate.ScrollMode;
    import org.hibernate.ScrollableResults;
    import org.openbravo.dal.service.OBCriteria;
    import org.openbravo.dal.service.OBDal;
    import org.openbravo.model.common.businesspartner.BusinessPartner;
    import org.openbravo.scheduling.KillableProcess;
    import org.openbravo.scheduling.ProcessBundle;
    import org.openbravo.service.db.DalBaseProcess;
    import org.openbravo.service.db.DbUtility;
    import org.quartz.JobExecutionException;
    
    public class DummyProcessKillable extends DalBaseProcess implements KillableProcess {
     
      private static final Logger log4j = Logger.getLogger(DummyProcessKillable.class);
     
      // Add a variable 'stop' to control the kill implementation and set false by default
      private boolean stop = false;
     
      @Override
      protected void doExecute(ProcessBundle bundle) throws Exception {
        try {
     
          // Get all business partners
          final OBCriteria<BusinessPartner> bpCri = OBDal.getInstance().createCriteria(
              BusinessPartner.class);
          bpCri.setFetchSize(1000);
          final ScrollableResults partnerScroller = bpCri.scroll(ScrollMode.FORWARD_ONLY);
          int i = 1;
          // Loop all business partners using a ScrollabeResults to avoid performance issues
     
          // Only continue with the process if the variable 'stop' is false
          while (partnerScroller.next() && !stop) {
            final BusinessPartner bp = (BusinessPartner) partnerScroller.get()[0];
            // Print the Identifier for every business partner
            log4j.info(bp.getIdentifier());
            // Add a timeout of 30 seconds
            Thread.sleep(30000);
     
            if ((i % 100) == 0) {
              OBDal.getInstance().getSession().clear();
            }
            i++;
     
          }
          partnerScroller.close();
        } catch (Exception ex) {
          Throwable e = DbUtility.getUnderlyingSQLException(ex);
          log4j.error("Error in DummyProcess", e);
          throw new JobExecutionException(e.getMessage(), e);
        }
     
      }
     
      @Override
      public void kill(ProcessBundle bundle) throws Exception {
        bundle.getLog().log("process killed")
        // When kill is called set variable 'stop' to true so the process will be interrupted in the
        // next iteration: while (partnerScroller.next() && !stop)
        stop = true;
      }
     
    }
```

Comentemos el código. En primer lugar, necesitamos implementar la interfaz KillableProcess.

```java
    
    public class DummyProcessKillable extends DalBaseProcess implements KillableProcess {
```

Creamos una variable `stop` que se utilizará para comprobar la continuidad de la ejecución.

    
    
    // Add a variable 'stop' to control the kill implementation and set false by default
      private boolean stop = false;

En el bucle principal del proceso, añadimos la comprobación para detener la ejecución cuando la variable se establece en true.

    
    
          // Only continue with the process if the variable 'stop' is false
          while (partnerScroller.next() && !stop) {

También hemos añadido un sleep (30 segundos) para hacer que el tiempo de ejecución sea más largo.

  
```java
            Thread.sleep(30000);
```

Por último, implementamos el método kill que establece `stop` a true.

```java
    
    
      @Override
      public void kill(ProcessBundle bundle) throws Exception {
        bundle.getLog().log("process killed")
        // When kill is called set variable 'stop' to true so the process will be interrupted in the
        // next iteration: while (partnerScroller.next() && !stop)
        stop = true;
      }
```

Ahora podemos parar el proceso desde el Monitor de procesos. 

Cuando un proceso se para, el estado en el monitor de procesos será *Parado por el usuario*.

---

Este trabajo es una obra derivada de [Procesos](http://wiki.openbravo.com/wiki/Processes){target="\_blank"} de [Wiki de Openbravo](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, usado bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.