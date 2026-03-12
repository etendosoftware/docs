---
title: Cómo desarrollar un proceso en segundo plano DAL
tags:
  - Cómo hacer
  - Proceso en segundo plano
  - Desarrollo Java
  - Data Access Layer
  - DAL
  - Operaciones de base de datos
  - Programación de procesos
---

#  Cómo desarrollar un proceso en segundo plano DAL

##  Visión general

Un proceso en segundo plano es un proceso que se ejecuta a intervalos regulares. Para esta sección desarrollaremos un proceso en segundo plano para el siguiente escenario:

_Supongamos que nuestro cliente quiere tener información de ventas de los últimos 6 meses de cada producto en el campo descripción._

Un proceso en segundo plano necesita (re)calcular los números de ventas de forma regular y guardarlos en el campo **Descripción** de cada producto que esté marcado como vendido. La solapa de nuestra ventana principal de Producto debería terminar siendo similar a:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_develop_a_DAL_background_process-0.png)

Tenga en cuenta que este es un ejercicio sencillo y que estamos demostrando cómo se desarrolla un proceso en segundo plano. El ejemplo anterior probablemente se implementaría mejor añadiendo primero un nuevo campo a la tabla de base de datos `M_PRODUCT` que contuviera esta información. Sin embargo, para el propósito de este ejercicio, simplemente lo almacenaremos en el campo **Descripción**.

En esta sección se mostrará cómo un proceso Java puede implementarse como un proceso en segundo plano. No obstante, un proceso Java también puede llamarse directamente desde la interfaz de usuario y tener una interfaz de usuario que permita introducir parámetros.

!!!info
      Para una descripción genérica de los procesos Java, consulte [Procesos](../../../developer-guide/etendo-classic/concepts/Processes.md).

##  Definición dentro del diccionario de aplicación

Los procesos en segundo plano se definen dentro de la ventana `Application Dictionary` > `Report and Process`. Utilice el rol de **Administrador del sistema** para crear un nuevo registro como se indica a continuación:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_develop_a_DAL_background_process-1.png)
  
Los siguientes campos son vitales para la definición de un proceso en segundo plano:

  * **Módulo** \- Su módulo personalizado al que pertenecerá este nuevo proceso en segundo plano; tenga en cuenta que esto indicará en consecuencia la ubicación en el disco duro y el paquete al que debe pertenecer
  * **Identificador** \- Identificador único del proceso; una buena práctica es usar el nombre de la clase
  * **Nombre** \- Un nombre amigable para el usuario del proceso
  * **Patrón de la Interfaz de Usuario** \- Debe establecerse en Manual, ya que Etendo ERP no necesita generar ninguna ventana de UI
  * **Es en segundo plano** \- Indica que este proceso es un proceso en segundo plano, lo que en consecuencia también muestra el campo **Nombre de la clase Java**
  * **Nombre de la clase Java** \- La especificación completa del nombre de la clase incluyendo el paquete (este paquete debe seguir la estructura de paquetes de su módulo especificado anteriormente): `com.etendoerp.client.application.examples.ProductRevenueCalculation`

##  Proceso y clase DalBaseProcess

Antes de continuar, decida cómo realizará el proceso en segundo plano las operaciones de base de datos. Tenemos dos opciones:

 - Usar el archivo XSQL que se convertirá en una clase Java por la librería core SQLC en tiempo de ejecución. Si se utiliza esta opción, su clase Java en segundo plano debería _implementar_ la **interfaz de Proceso** e implementar el método `execute` para realizar nuestras tareas.
  
!!!info
      Encuentre esta interfaz en `src/org/openbravo/scheduling/Process.java`.

 - Usar la nueva Data Access Layer, que proporciona POJOs de capa intermedia mediante los cuales podemos manipular tablas de base de datos. Si se utiliza este método, su clase Java en segundo plano debe _extender_ la **clase DalBaseProcess** e implementar el método `doExecute` que realiza su tarea. Esto le dará acceso al contexto de datos correcto proporcionado por DAL y, al mismo tiempo, se encargará de la autenticación y los privilegios.
  
!!!info
      Encuentre la clase abstracta en `src/org/openbravo/service/db/DalBaseProcess.java` .

Dado que el primer método acabará quedando obsoleto debido a la dependencia de base de datos, el segundo es la opción prudente.

!!!note
      Es beneficioso tener cierto conocimiento de la API Hibernate Criteria al usar el DAL. Lea más información para una descripción detallada de esta [API](https://docs.jboss.org/hibernate/core/3.3/reference/en/html/querycriteria.html){target="\_blank"}.

La Data Access Layer se trata en varios otros artículos y secciones.

!!!info
      Para más información, lea el manual de referencia de [Data Access Layer](../../../developer-guide/etendo-classic/concepts/Data_Access_Layer.md).

##  Implementación

El módulo de ejemplo implementa el proceso en segundo plano en `modules/org.openbravo.client.application.examples/src/org.openbravo.client.application.examples.ProductRevenueCalculation.java`

```java title="ProductRevenueCalculation.java"
// assign the background process to a package that belongs to the 
// main package of the module this custom development belongs to  
package com.etendoerp.client.application.examples;
  
import java.math.BigDecimal;
import java.util.Calendar;
 
import org.hibernate.Criteria;
import org.hibernate.criterion.Projections;
import org.hibernate.criterion.Restrictions;
import org.openbravo.dal.service.OBCriteria;
import org.openbravo.dal.service.OBDal;
import org.openbravo.model.common.order.OrderLine;
import org.openbravo.model.common.plm.Product;
import org.openbravo.scheduling.ProcessBundle;
import org.openbravo.scheduling.ProcessLogger;
import org.openbravo.service.db.DalBaseProcess;
import org.quartz.JobExecutionException;
 
// the background process needs to extend DalBaseProcess since
// we will be using DAL objects to perform database operations
public class ProductRevenueCalculation extends DalBaseProcess {
 
  static int counter = 0;
 
  private ProcessLogger logger;
 
  // abstract method doExecute needs to be implemented and carries
  // with itself the ProcessBundle object deriving from Openbravo Quartz
  // scheduler
  public void doExecute(ProcessBundle bundle) throws Exception {
 
    logger = bundle.getLogger(); // this logger logs into the LOG column of
    // the AD_PROCESS_RUN database table
    BigDecimal sumAmount = BigDecimal.ZERO;
 
    logger.log("Starting background product revenue calculation. Loop " + counter + "\n");
 
    // define time 6 months ago from today which is the timespan that our
    // calculation will consider
    Calendar timeSixMonthsAgo = Calendar.getInstance();
    timeSixMonthsAgo.add(Calendar.DAY_OF_MONTH, -180);
 
    try {
      // get all products that are sold (M_PRODUCT.ISSOLD = 'Y')
      final OBCriteria<Product> productList = OBDal.getInstance().createCriteria(Product.class);
      productList.add(Restrictions.eq(Product.PROPERTY_SALE, true));
 
      logger.log("No of products = " + productList.list().size() + "\n");
 
      // loop through all products that are sold and calculate revenues
      // for each
      for (Product product : productList.list()) {
 
        sumAmount = BigDecimal.ZERO;
 
        // select lines from C_ORDERLINE table that match the product
        final Criteria orderLineList = OBDal.getInstance().createCriteria(OrderLine.class)
            .add(Restrictions.eq(OrderLine.PROPERTY_PRODUCT, product));
 
        // filter out lines that belong to sales (as opposed to
        // purchase) and fit within the last six months
        //
        // when you want to filter on a property of an associated entity
        // then the property of that association needs an alias, see
        // here: http://www.javalobby.org/articles/hibernatequery102/
        orderLineList.createAlias(OrderLine.PROPERTY_SALESORDER, "order")
            .add(Restrictions.eq("order.salesTransaction", true))
            .add(Restrictions.gt("order.orderDate", timeSixMonthsAgo.getTime()));
 
        // Sum line amounts grouped by product
        orderLineList.setProjection(Projections.projectionList()
            .add(Projections.sum(OrderLine.PROPERTY_LINENETAMOUNT))
            .add(Projections.groupProperty(OrderLine.PROPERTY_PRODUCT)));
 
        // due to grouping and sum operation there will really only be
        // one resulting record but in theory there could be more (a
        // list)
        for (Object o : orderLineList.list()) {
          // the query returns a list of arrays (columns of the query)
          final Object[] os = (Object[]) o;
          sumAmount = (BigDecimal) os[0];
          final Product p = (Product) os[1];
          logger.log(p.getName() + " Amount " + sumAmount + "\n");
        }
        product.setDescription("6 monthRevenue = " + sumAmount);
      }
 
    } catch (Exception e) {
      // catch any possible exception and throw it as a Quartz
      // JobExecutionException
      throw new JobExecutionException(e.getMessage(), e);
    }
  }
}
```

##  Compilación de la aplicación

Usando la compilación por línea de comandos, utilice `./gradlew smartbuild` para compilar el código manual de la aplicación y desplegarlo en el contexto de Tomcat. A continuación, reinicie Tomcat.

##  Programación

Para que un proceso en segundo plano se ejecute, primero necesita ser programado. Usando el rol **Etendo Client Admin** (por lo tanto, no el rol de Administrador del sistema) navegue a `General Setup` > `Process Scheduling` > ventana `Process Request` e introduzca un nuevo registro.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_develop_a_DAL_background_process-2.png)

Los siguientes campos son importantes:

  * **Proceso** \- determina qué proceso en segundo plano programar. Solo los procesos en segundo plano están disponibles en el desplegable
  * **Programado** \- hay varias formas de programar un proceso en función del requisito de si el proceso necesita ejecutarse una vez o repetidamente. Use la opción _Programado_ para nuestro propósito
  * **Frecuencia** \- con qué frecuencia necesita ejecutarse el proceso. En función de su selección, los campos de abajo cambiarán en consecuencia para que pueda introducir el intervalo apropiado. Seleccione _02 - Cada n minutos_ para poder ver los resultados inmediatamente
  * **Intervalo en Minutos** \- cada cuántos minutos debe ejecutarse el proceso en caso de que se haya seleccionado _02 - Cada n minutos_ arriba. Introduzca _10_
  * **Núm de Repeticiones** \- el número de veces que una solicitud de proceso se repetirá después de su primera ejecución. Tenga en cuenta que 10 repeticiones darán un total de 11 ejecuciones del proceso. Introduzca _5_

Guarde el registro y haga clic en el botón **Programar Proceso** para que el proceso finalmente quede programado.

!!!note
      Es necesario usar el rol de Administrador de Etendo para que el proceso en segundo plano tenga acceso a los productos de BigBazaar. El cliente del rol que introduce la solicitud del proceso en segundo plano se utiliza para determinar los privilegios de acceso.
  
##  Monitorización

Para ver las ejecuciones del proceso, el estado y el log que generó, use `General Setup` > `Process Scheduling` > ventana `Process Monitor`. Tras uno o dos minutos de programar el proceso, deberían verse entradas relacionadas con las ejecuciones del nuevo proceso.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_develop_a_DAL_background_process-4.png)

##  El resultado

Para poder obtener resultados significativos, introduzca y complete un Pedido de venta (`Sales Management` > `Transactions` > `Sales Order`) ya que el proceso en segundo plano calcula los ingresos dentro de los últimos 6 meses y la base de datos de demostración puede contener registros más antiguos que eso. Por ejemplo, introduzca un nuevo Pedido de venta para un tercero, e introduzca una línea para un determinado producto, y luego complete el pedido de venta.

A continuación, navegue a la ventana `Master Data Management` > `Product` y encuentre el producto. Tras uno o dos minutos, cuando el proceso haya recalculado el campo **Descripción**, debería poder ver lo siguiente:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_develop_a_DAL_background_process-5.png)

Este trabajo es una obra derivada de [Cómo desarrollar un proceso en segundo plano DAL](http://wiki.openbravo.com/wiki/How_to_develop_a_DAL_background_process){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.