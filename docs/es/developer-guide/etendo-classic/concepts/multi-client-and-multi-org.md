---
title: Multi-Entidad y Multi-Organización
tags:
    - Multi-Entidad
    - Multi-Organización
    - Conceptos
    - Data Access Layer

status: beta
---

# Multi-Entidad y Multi-Organización

!!! example  "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.
  
## Visión general

Este documento describe multi-entidad y multi-organización desde la perspectiva de desarrollo. Para una comprensión funcional sobre estas funcionalidades, lea la [Documentación funcional](../../../user-guide/etendo-classic/basic-features/general-setup/getting-started.md).

## Estructura

A nivel de base de datos y de diccionario de aplicación, todas las tablas deben tener la estructura necesaria para soportar multi-entidad y multi-organización. Se describe en el [documento de Tablas de base de datos](../concepts/tables.md#clientorganization).

## Filtrado de datos

Esta sección explica el código necesario para filtrar correctamente los datos relativos a entidad y organización con el fin de evitar accesos a información no permitida. Estos filtros son diferentes en caso de que el desarrollo esté utilizando `XSQL` o `DAL`.

### Data Access Layer

La [Data Access Layer](../concepts/data-access-layer.md) proporciona varias interfaces para facilitar la consulta de datos: OBCriteria y OBQuery ???. Estas clases de servicio se encargan de la seguridad y del filtrado automático sobre entidades y organizaciones legibles.

El filtrado sobre entidades y organizaciones legibles puede deshabilitarse llamando a los métodos correspondientes (`setFilterReadableOrganizations/setFilterReadableClients`).

Cuando se consulta directamente un objeto (el método `OBDal.get`), entonces no se realiza ningún filtrado sobre entidad/organización legible.

La capa de acceso a datos también comprueba el acceso de lectura al acceder a un objeto en memoria. Estas comprobaciones diferencian entre entidades legibles y entidades legibles derivadas. Para las entidades legibles derivadas, un usuario solo puede ver el valor de las propiedades identificadoras.

También hay casos en los que tiene sentido crear sus propias consultas HQL y ejecutarlas directamente. Para soportar esto, el servicio OBDal proporciona dos métodos de conveniencia que pueden utilizarse para añadir cláusulas in de eadableClients/readableOrganizations a la cláusula where:

```java 
OBDal.getInstance().getReadableOrganizationsInClause();
OBDal.getInstance().getReadableClientsInClause();
```

La capa de acceso a datos también comprueba el acceso de escritura a entidades/organizaciones cuando se inserta/actualiza un objeto. Esta comprobación se realiza para cada objeto que se guarda (consulte [aquí](../concepts/data-access-layer.md#write-access) para más información). Una comprobación adicional que se realiza es que un objeto solo puede referirse a objetos en el árbol natural de su propia organización.

### OrganizationStructureProvider

La clase `OrganizationStructureProvider` es una clase de utilidad Java diseñada para ayudar en tareas muy comunes relacionadas con organizaciones. Por ejemplo, esta clase contiene métodos para encontrar si una organización pertenece al árbol natural de otra organización, para averiguar el árbol natural padre de una organización,
o el árbol de hijos de una organización.

Se recomienda encarecidamente que, si se está utilizando el DAL, se utilice también esta clase si es necesario realizar cualquiera de estas tareas.

### XSQL - Definición

Todas las consultas utilizadas para mostrar o modificar datos deben incluir filtro por entidad y organización. La única excepción a esta regla son las consultas que afectan únicamente a filas seleccionadas por un ID conocido (que se ha obtenido, en la mayoría de los casos, a partir de una consulta que sigue la regla); en este caso, como se sabe que esa fila es accesible por el usuario, el filtro no es necesario.

En la cláusula where de `XSQL`, la consulta debe verse así:

```SQL
SELECT ...     
    FROM ...
WHERE ...
    AND AD_CLIENT_ID IN ('1')
    AND AD_ORG_ID IN ('1')
        ...
```

Y la sección de parámetros: 

```XML 
<Parameter name="adClientId" optional="true" type="replace" after="AND AD_CLIENT_ID IN (" text="'1'"/>

<Parameter name="adOrgId" optional="true" type="replace" after="AND AD_ORG_ID IN (" text="'1'"/>
```

Esto creará un par de parámetros: `adClientId` y `adOrgID`; cómo pasarlos se explica en la siguiente sección.

### XSQL - Uso en Java

#### Entidad

Solo la entidad actualmente conectada es accesible aunque el rol tenga permiso para diferentes entidades. Adicionalmente, dependiendo del nivel de usuario definido para el rol y del nivel de acceso para la tabla a la que se está accediendo, se concede o deniega el acceso a la entidad 0 (sistema).

Para obtener la lista de entidades accesibles (entidad actual y 0 en caso de que se pueda acceder), se utiliza el método `Utility.getContext`, que tiene la siguiente estructura:

``` java
public static String getContext(ConnectionProvider conn, VariablesSecureApp vars, String context, String window)
```

o

``` java
public static String getContext(ConnectionProvider conn, VariablesSecureApp vars, String context, String window, int accessLevel)
```

En el primer caso, no se pasa el nivel de acceso, por lo que no se tiene en cuenta para calcular si la entidad 0 es accesible. Esta es la forma en que generalmente se utiliza para código manual. Una llamada estándar a este método sería:

``` java
String strClient = Utility.getContext(this, vars, "#User_Client", "");
```
  
El segundo recibe el nivel de acceso para la tabla a la que se está accediendo; esta es la forma en que las ventanas WAD obtienen la lista de entidades.

#### Organización

Hay tres niveles de acceso a organización: **Editable**, **Accesible** y **Referenciable**.

##### Editable

Solo los datos en una organización editable pueden modificarse. Las organizaciones editables son aquellas concedidas explícitamente al rol.

La lista de organizaciones editables se obtiene con:

``` java
Utility.getContext(conn, vars, "#User_Org", windowId, accesslevel)
```

Este tipo debe utilizarse al mostrar datos que el usuario puede modificar. Por ejemplo, una ventana de proceso que muestra registros sobre los que el usuario puede realizar una acción.

##### Accesible

Los datos accesibles pueden verse pero no modificarse. La lista de organizaciones accesibles consiste en el árbol estándar de su orgList; es decir, todas las organizaciones concedidas, sus ancestros y sus organizaciones descendientes. Para obtenerla:

``` java
Utility.getContext(conn, vars, "#AccessibleOrgTree", windowId, accesslevel)
```

Este tipo debe utilizarse al mostrar datos informativos. Por ejemplo, en informes. También se utiliza para combos en filtros. Por ejemplo, un combo mostrado en un filtro para un informe.

##### Referenciable

Un registro puede hacer referencia a otros registros con datos definidos en el árbol estándar de la organización del registro padre.

``` java
Utility.getReferenceableOrg(vars, currentOrg)
```
  

##### Selectores (Búsquedas)

Los selectores son un caso que merece una atención específica; tienen dos elementos principales: **Filtro** y **Datos**.

###### Filtro

Cuando se utiliza un combo en un filtro, la lista de organizaciones que recibe es la accesible:

``` java
Utility.getContext(conn, vars, "#AccessibleOrgTree", windowId, accesslevel)
```

Si se utiliza otro selector dentro del filtro, no debe pasarse ninguna organización (no tiene efecto en la implementación actual; consulte el capítulo siguiente).

###### Datos

Como el propósito principal de los selectores es seleccionar datos para ser referenciados desde otros registros, implementan el filtrado **Referenciable**.

Cuando se llama a un selector desde una ventana que no va a recibir un registro al que referenciar (por ejemplo, un filtro en un informe), no filtrará por organizaciones referenciables sino por accesibles.

La implementación para selectores requiere:

* Añadir una variable de entrada a todos los selectores para obtener la organización (definida en `Application Dictionary` > `Reference` > `Reference` > `Selector Reference` Columns) 
* En los comandos _VALOR POR DEFECTO_ y _CLAVE_ leer esta variable con: 

``` java
vars.getStringParameter("inpAD_Org_ID");
```

* Añadir una nueva variable oculta en el `HTML` y almacenar ahí el valor leído. 
* En el comando _DATOS_ leer la información del input oculto del `HTML` y usarla para obtener la lista referenciable de organizaciones usando: 

``` java
Utility.getSelectorOrgs(conn, vars, readOrg);
```

* Usar la lista obtenida para filtrar la consulta. 

El método `Utility.getSelectorOrgs` mencionado anteriormente devuelve las organizaciones referenciables o las accesibles dependiendo de si la organización pasada está vacía o no.

Esta implementación permite obtener automáticamente la lista referenciable de organizaciones para las ventanas WAD y, por defecto, las accesibles para código manual. Si fuera deseable que alguna ventana manual obtuviera la lista referenciable en lugar de la accesible, solo sería necesario modificar el javascript
que llama al selector para incluir la organización.

### SQL - AD_IsOrgIncluded

`AD_IsOrgIncluded` es una función almacenada de base de datos que puede utilizarse para saber si dos organizaciones pertenecen al mismo árbol o no.

Recibe 3 parámetros:

* `p_orgid`. Comprueba que esta organización es descendiente de la organización `p_parentorgid`. 
* `p_parentorgid`. Comprueba que esta organización es ancestro de la organización `p_orgid`. 
* `p_clientid`. Es la entidad en la que se espera que estén ambas organizaciones. 

Esta función devuelve -1 en caso de que la 2ª organización no sea ancestro de la 1ª o el nivel en la jerarquía en caso de que sí lo sea.

## Transacciones

Al desarrollar procesos transaccionales debe tenerse en cuenta que esos procesos solo deben afectar a filas en entidad y organizaciones editables. También deben comprobar que todos los objetos involucrados en el proceso están en una organización correcta (por ejemplo, usando la función `AD_IsOrgIncluded`).

### Datos específicos de organización

Es posible definir una estructura que permita definir objetos en una organización y cambiar algunos de sus atributos para otra organización inferior en la jerarquía del árbol de organizaciones. Actualmente el core de Etendo lo implementa para productos usando la tabla `M_Product_Org`. En este caso es posible definir productos, por ejemplo, en la organización *, y sobrescribir algunos de sus atributos para otras organizaciones. El efecto sería que, por defecto, se utilizan los atributos definidos para el producto en la organización * excepto en el caso de que se sobrescriban en la organización actual. Esta gestión debe realizarse manualmente al desarrollar procesos que utilicen estas tablas.

Por ejemplo, esta consulta es parte del proceso `MRP_ProcessPlan_Recalculate`; busca los valores que se sobrescriben en la organización actual y los toma si existen:

``` sql
SELECT QTY, planneddate, plannedorderdate, M_PRODUCT.M_PRODUCT_ID,
            COALESCE(M_PRODUCT_ORG.CAPACITY, M_PRODUCT.CAPACITY) AS CAPACITY,
            COALESCE(M_PRODUCT_ORG.DELAYMIN, M_PRODUCT.DELAYMIN, 0) AS DELAYMIN,
            COALESCE(M_PRODUCT_ORG.QTYTYPE, M_PRODUCT_ORG.QTYTYPE, 'E') AS qtytype,
            COALESCE(M_PRODUCT_ORG.QTYMIN, M_PRODUCT_ORG.QTYMIN, 0) AS qtymin,
            COALESCE(M_PRODUCT_ORG.QTYSTD, M_PRODUCT_ORG.QTYSTD, 1) AS qtystd
        INTO v_Qty, v_planneddate, v_plannedorderdate, v_Product,
            v_capacity, v_delaymin, v_qtytype, v_qtymin, v_qtystd
    FROM M_PRODUCT INNER JOIN MRP_RUN_PRODUCTIONLINE ON MRP_RUN_PRODUCTIONLINE.M_PRODUCT_ID = M_PRODUCT.M_PRODUCT_ID
                                                    AND MRP_RUN_PRODUCTIONLINE_ID = p_Run_ProductionLine_ID
                    LEFT JOIN M_PRODUCT_ORG ON M_PRODUCT.M_PRODUCT_ID = M_PRODUCT_ORG.M_PRODUCT_ID
                                            AND M_PRODUCT_ORG.AD_ORG_ID = MRP_RUN_PRODUCTIONLINE.AD_ORG_ID;
```

---

Este trabajo es una obra derivada de [Multi-Entidad y Multi-Organización](http://wiki.openbravo.com/wiki/Multi-Client_and_Multi-Org){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.