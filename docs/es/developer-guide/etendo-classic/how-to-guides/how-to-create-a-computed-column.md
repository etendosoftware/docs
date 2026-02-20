---
title: Cómo crear una columna calculada
tags:
  - Cómo
  - Columna calculada
  - Lógica SQL
  - Etendo classic
---

# Cómo crear una columna calculada

## Visión general

Una columna calculada es una columna de una tabla que se calcula mediante una expresión _SQL_ y que no existe explícitamente en el esquema de la base de datos.

Las columnas calculadas tienen estas características:

  * Se calculan cuando se lee un registro de la base de datos.
  * No se persisten, no existe una columna real en el esquema de la base de datos para una columna calculada.
  * Se calculan usando una expresión SQL que puede utilizar columnas de la definición de tabla del diccionario de aplicación en la que se define la columna.
  * Se pueden usar en la definición de un campo (del mismo modo que una columna "normal"), se pueden ordenar y filtrar, pero no se pueden editar.

## Módulo de ejemplo

Esta sección está respaldada por un módulo de ejemplo que muestra ejemplos del código mostrado y comentado.

El código del módulo de ejemplo se puede descargar desde este repositorio: [com.etendoerp.client.application.examples](https://github.com/etendosoftware/com.etendoerp.client.application.examples)

!!!Note
    El módulo de ejemplo también contiene implementaciones de otras guías.

## Definición de una columna calculada

Definir una columna calculada es sencillo.

1. Vaya a la ventana **Tablas y columnas**.
2. Vaya a la tabla en la que desea añadir la columna calculada.
3. A continuación, en la solapa hija de columnas, cree una nueva columna y establezca el campo **SQL**.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Computed_Column-1.png)


El campo **SQL** debe ser una expresión SQL:

  * Si es una expresión SQL de tipo select, entonces todas las tablas en la cláusula from deben usar un alias.
  * Puede referirse a otras columnas de la tabla usando su nombre sin alias.

Este es un ejemplo de la columna de cantidad total de línea mostrada arriba:

```hql
(SELECT sum(ol.qtyOrdered) FROM c_orderline ol WHERE ol.c_order_id=c_order_id)
```

Lo que puede ver es que la cláusula from utiliza una tabla con alias; el `c_order_id` del final es la columna sin alias de la tabla principal.

!!!Note
    * Una columna calculada se puede usar en la definición de un campo para una columna de Etendo, igual que cualquier otra columna.
    * Una columna calculada que utilice una _referencia de cadena_ debe tener una longitud mayor que cero, porque este es el número de caracteres que se van a mostrar en la vista de formulario.
    * El campo es siempre de solo lectura; se recalcula/se establece automáticamente al actualizar o insertar un registro.
    * Es posible filtrar y ordenar por columnas/campos calculados.

## Caso de uso: mostrar totales en una cabecera

En la sección "Definición de una columna calculada" se mostró un ejemplo de expresión SQL. El ejemplo anterior calcula la suma de las cantidades de una línea. Puede añadir una columna calculada como un campo a una solapa/ventana:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Computed_Column-2.png)

y mostrarla en la cuadrícula:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Computed_Column-3.png)

o en el formulario:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Computed_Column-4.png)

## Implicaciones de rendimiento

### Filtrado y ordenación

Cuando las columnas calculadas se utilizan para filtrar u ordenar la cuadrícula, su valor necesita calcularse para todas las filas existentes antes de que se pueda aplicar cualquier límite de paginación; esto puede tener un impacto muy importante en términos de rendimiento.

En general, al definir columnas calculadas, deberían configurarse como no filtrables ni ordenables. La única excepción a esta regla es cuando se garantiza que el número de registros en la tabla para la que se crean va a ser siempre reducido o que siempre se mostrará como una subsolapa, donde el número de filas por registro padre no puede ser grande.

### Evaluación diferida

Las columnas calculadas se evalúan de forma diferida. Esto significa que su consulta no se ejecuta cuando se recupera la entidad en la que están definidas, sino cuando se accede a una de ellas.

Por ejemplo, **Estado del envío** es una columna calculada de la entidad **Parte**:

```java
// load one order
OBCriteria<Order> qOrder = OBDal.getInstance().createCriteria(Order.class);
qOrder.setMaxResults(1);
Order order = qOrder.list().get(0);
```

El código anterior carga una parte; en este punto **Estado del envío** aún no se ha calculado, lo que significa que el SQL no se ha ejecutado en la base de datos.

Si después tenemos este código:

```java
// load computed columns
System.out.println(order.getDeliveryStatus());
``` 

es en este punto cuando la consulta de la columna calculada se ejecuta en la base de datos y la propiedad **Estado del envío** toma valor.

!!!Note
    En caso de que haya muchas columnas calculadas en la misma entidad, se evalúan todas juntas cuando se calcula la primera.

#### Limitaciones

Para que las columnas calculadas sean diferidas, se mapean en su entidad como una propiedad `many-to-one` (llamada `computedColumns`) enlazada a una entidad virtual; es en esta entidad virtual donde se ubican las columnas calculadas reales como propiedades de fórmula de Hibernate.

![](../../../assets/developer-guide/etendo-classic/how-to- guides/How_to_create_a_Computed_Column-6.png)

Esta complejidad adicional es transparente cuando se trabaja con clases Java generadas del _DAL_, como se ha visto antes: `order.getDeliveryStatus()` rellena el valor de la columna calculada, aunque internamente lo está recuperando desde la entidad virtual.

Pero este modelo también impone algunas limitaciones que deben tenerse en cuenta al manipular columnas calculadas en filtros u ordenación.

!!!Note
    Al usar columnas calculadas en HQL para filtrar u ordenar, se evalúan. Esto debe hacerse con cuidado (o incluso evitarse si es posible) porque podría tener implicaciones de rendimiento.

Al trabajar con HQL (es decir, `OBQuery`), no se puede acceder directamente a las columnas calculadas, ya que no son propiedades de la entidad.

---
Este trabajo es una obra derivada de [Cómo crear una columna calculada](http://wiki.openbravo.com/wiki/How_to_create_a_Computed_Column){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.