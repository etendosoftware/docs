---
title: Cómo crear una tabla basada en HQL
tags:
  - Cómo hacer
  - HQL
  - Tabla
  - Columna
  - Campo
---

# Cómo crear una tabla basada en HQL

## Introducción

Existen tres orígenes de datos disponibles en la definición de una tabla en el diccionario de aplicación:

  * Tabla: una tabla definida realmente en un DBMS.
  * Fuente de datos: se utilizará una fuente de datos manual como origen de datos de esta tabla.
  * Tabla HQL.

El origen de datos _Tabla HQL_ permite definir una tabla sin necesidad de una tabla física en la base de datos y sin tener que definir una fuente de datos manual.

Las tablas basadas en HQL deben definir una consulta `select` HQL, que se utilizará para obtener los registros adecuados cuando se realice una solicitud a su fuente de datos.

## Definir una tabla basada en HQL en el diccionario de aplicación

### Definición de tabla

Cuando se define una tabla basada en HQL en el diccionario de aplicación, no es necesario completar los campos _Nombre tabla BD_ y _Nombre de la clase Java_. Existen dos campos nuevos que deben configurarse para estas tablas:

  * Consulta HQL: la consulta HQL que se utilizará para recuperar los registros de esta tabla.
  * Alias de entidad: el alias de una de las tablas utilizadas en la consulta HQL. Se utilizará para añadir automáticamente los filtros obligatorios de cliente y organización.

Consideraciones de diseño para consultas HQL:

  * Utilice alias para todas las columnas y tablas usadas en la consulta. Esto simplificará la definición de columnas en el diccionario de aplicación.
  * Incluya la cadena _@additional_filters@_ dentro de una cláusula `where` en la consulta HQL. Esa cadena se sustituirá por los filtros obligatorios de cliente y organización, y por los filtros generados a partir de los criterios incluidos en la solicitud a la fuente de datos.
  * Todas las consultas HQL deben incluir una columna que actúe como su clave primaria. El alias de esta columna debe ser _id_.
  * Si una consulta HQL contiene varias cláusulas `from` porque utiliza subconsultas en la cláusula `select` o en la cláusula `where`, entonces debe utilizarse el texto MAINFROM en lugar de FROM en la cláusula `from` principal.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_HQL_Based_Table-1.png)

### Definición de columna

El proceso _Crear columnas de la base de datos_ no aplica a tablas basadas en HQL, por lo que deben crearse manualmente.

Consideraciones en la definición de columnas de tablas HQL en el diccionario de aplicación:

  * El _Nombre columna BD_ y el _Nombre_ de la columna deben ser el alias utilizado para la columna en la consulta HQL.
  * El campo _Parte Izquierda de la Cláusula_ debe completarse con la definición de la parte izquierda de la columna en la consulta HQL. Por ejemplo, si una columna se define en la consulta HQL como `e.name as countryName`, entonces el _Nombre_ y el _Nombre columna BD_ de la columna deben ser `countryName` y su _Parte Izquierda de la Cláusula_ debe ser `e.name`.

Para incluir una clave externa en una columna de una tabla HQL, la columna debe apuntar a la propia entidad referenciada, no a su `id`. Entonces, cuando esa columna se define en el diccionario de aplicación, debe utilizarse la referencia _Tabla_, y debe seleccionarse la instancia de tabla adecuada en el campo _Referencia clave_.

Por ejemplo, si `e` es el alias de la tabla Country y queremos incluir su moneda, debemos introducir `e.currency as countryCurrency` en la consulta HQL. A continuación, debemos seleccionar la referencia _Tabla_ en la definición de esa columna en el diccionario de aplicación y `c_currency` en el campo _Referencia clave_.

## Definición de solapa y campos

La solapa y los campos de una tabla basada en HQL se definen en el diccionario de aplicación del mismo modo que con las tablas estándar.
La única restricción es que todas las solapas asociadas a tablas basadas en HQL serán de solo lectura.

## Temas avanzados

### Insertadores HQL

Los insertadores HQL permiten añadir código a una consulta HQL en un punto especificado en la consulta HQL definida en el diccionario de aplicación.

#### Puntos de inserción HQL en la consulta HQL

Para definir un punto de inserción HQL en su consulta HQL necesita utilizar la cadena `@insertion_point#@`, siendo `#` el índice del punto de inserción. El
índice del primer punto de inyección debe ser 0, el índice del segundo debe ser 1, etc. No puede haber huecos en los índices de los puntos de inserción.

Los puntos de inserción solo pueden definirse en `cláusulas where`. Si la consulta HQL define un punto de inserción pero después no hay ningún `HQLInserter` definido para él, entonces el punto de inserción se sustituirá por `1 = 1` en la consulta HQL.

Por ejemplo, esta consulta HQL define un lugar para introducir los filtros adicionales y un punto de inserción HQL:

```HQL
SELECT 
  e.id, 
  e.name, 
  e.eDICode, 
  e.costingPrecision, 
  e.client, 
  e.client.organization, 
  e.active
FROM 
  UOM AS e
WHERE 
  @additional_filters@
AND 
  @insertion_point_0@
```

#### Definir un insertador HQL

Los insertadores HQL personalizados deben extender la clase `HQLInserter`. Las subclases de la clase `HQLInserter` deben implementar este método:

```java
/**
  * Returns some code to be inserted in a HQL query, and adds query named parameters when needed
  * 
  * @param requestParameters
  *          the parameters of the request. The inserted code may vary depending on these
  *          parameters
  * @param queryNamedParameters
  *          the named parameters of the hql query that will be used to fetch the table data. If
  *          the inserted code uses named parameters, the named parameters must be added to this
  *          map
  * @return the hql code to be inserted
  */
public abstract String insertHql(Map<String, String> requestParameters,
    Map<String, Object> queryNamedParameters);
```

La cadena devuelta por este método se utilizará para sustituir `@insertion_point_#@`.

Los `HQLInserter` se instancian utilizando inyección de dependencias. Se utiliza un `HQLInserter` concreto para sustituir un punto de inyección específico de una tabla concreta. Por ejemplo, el siguiente `HQLInserter` se utiliza para sustituir el `@insertion_point_0@` definido en la consulta HQL de la tabla con id `59ED9B23854A4B048CBBAE38436B99C2`:

```java
  @HQLInserterQualifier.Qualifier(tableId = "59ED9B23854A4B048CBBAE38436B99C2", injectionId = "0")
public class AddPaymentCreditToUseInjector extends HqlInserter {
 
  @Override
  public String insertHql(Map<String, String> requestParameters,
      Map<String, Object> queryNamedParameters) {
    final String strBusinessPartnerId = requestParameters.get("received_from");
    final BusinessPartner businessPartner = OBDal.getInstance().get(BusinessPartner.class,
        strBusinessPartnerId);
    boolean isSalesTransaction = "true".equals(requestParameters.get("issotrx")) ? true : false;
    queryNamedParameters.put("bp", businessPartner.getId());
    queryNamedParameters.put("issotrx", isSalesTransaction);
    return "f.businessPartner.id = :bp and f.receipt = :issotrx";
  }
}
```

### Transformadores HQL

Mientras que los insertadores HQL solo permiten añadir algún criterio en un punto predefinido por el usuario que creó la consulta HQL, los transformadores HQL permiten modificar toda la estructura de la consulta.

Para implementar un transformador HQL, debe crear una subclase de la clase HqlQueryTransformer.
Esta clase tiene un método abstracto que debe implementarse en el transformador HQL personalizado:

```java
/**
  * Returns the transformed hql query
  * 
  * @param hqlQuery
  *          original hql query
  * @param requestParameters
  *          the parameters of the request
  * @param queryNamedParameters
  *          the named parameters of the hql query that will be used to fetch the table data. If
  *          the transformed hql query uses named parameters that did not exist in the original hql
  *          query, the named parameters must be added to this map
  * @return the transformed hql query
  */
public abstract String transformHqlQuery(String hqlQuery, Map<String, String> requestParameters,
    Map<String, Object> queryNamedParameters);
```

Esta función recibe una consulta HQL, un mapa con los parámetros enviados en la solicitud y un mapa con todos los parámetros con nombre que se utilizan en la consulta HQL. Devuelve la consulta HQL transformada y, si en la transformación se han añadido algunos parámetros con nombre a la consulta, deben incluirse en el mapa queryNamedParameters.

Los transformadores HQL se instancian utilizando inyección de dependencias. Para aplicar un transformador HQL a una tabla HQL debe incluir el id de la tabla en el calificador, por ejemplo:

```java
@ComponentProvider.Qualifier("58AF4D3E594B421A9A7307480736F03E")
public class AddPaymentOrderInvoicesTransformer extends HqlQueryTransformer {
```

---
Este trabajo es una obra derivada de [Cómo crear una tabla basada en HQL](http://wiki.openbravo.com/wiki/How_to_create_a_HQL_Based_Table){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.