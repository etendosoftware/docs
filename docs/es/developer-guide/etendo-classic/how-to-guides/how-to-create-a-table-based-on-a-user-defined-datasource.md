---
title: Cómo crear una tabla basada en una fuente de datos definida por el usuario
tags: 
    - Tabla
    - Definida por el usuario
    - Fuente de datos 
status: beta
---

# Cómo crear una tabla basada en una fuente de datos definida por el usuario

!!! example "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.

## Visión general

Se pueden establecer dos orígenes de datos diferentes para las tablas definidas en el diccionario de aplicación: **Tabla** (tablas y vistas de base de datos) y **Fuente de datos**. Existen dos motivos principales para utilizar una tabla basada en una fuente de datos.

- Utilizar como objetos de origen de datos elementos distintos de tablas o vistas de base de datos. Por ejemplo, se puede definir una tabla basada en una fuente de datos que utilice como origen de datos una *hoja de cálculo de Google Docs*, un *archivo CSV*, datos obtenidos de un *servicio web*, etc. 
- Resolver problemas relacionados con el rendimiento. Por ejemplo, la ventana Devolución de cliente tiene una ventana de seleccionar y ejecutar que sufre problemas de rendimiento en sistemas con volúmenes muy altos. La causa de este problema es que la tabla utilizada en esa ventana de seleccionar y ejecutar se basa en una vista de base de datos muy compleja. Se puede crear una fuente de datos definida por el usuario para construir esa vista manualmente.

!!!info
    Definir una fuente de datos requiere un esfuerzo considerable (es necesario programar el filtrado, la paginación, la ordenación, etc.). Si se ajusta a sus necesidades, se puede utilizar una [Tabla basada en HQL](../how-to-guides/how-to-create-a-hql-based-table.md).  

  
## Creación de la fuente de datos Java

[Esta sección](../concepts/datasources.md) describe cómo crear una fuente de datos Java y proporciona [algunos ejemplos](../concepts/datasources.md#datasource-examples).

Si la fuente de datos es de solo lectura (por ejemplo, para utilizarse en una ventana de seleccionar y ejecutar), entonces se recomienda crear una nueva clase que extienda la clase `ReadOnlyDataSourceService`. Si la fuente de datos también se va a utilizar para añadir, actualizar o eliminar registros existentes, entonces se recomienda extender la clase `DefaultDataSourceService`.

La fuente de datos debe sobrescribir el método `getEntity()`. Se puede utilizar esta plantilla; lo único que debe cambiarse es el valor de la constante `AD_TABLE_ID`.

``` java
//Table ID of the datasource based table defined in the application dictionary
private static final String AD_TABLE_ID = "A9BC62219E644720867F6402B0C25933";
 
@Override
public Entity getEntity() {
return ModelProvider.getInstance().getEntityByTableId(AD_TABLE_ID);
}
```

## Definición de la fuente de datos en el diccionario de aplicación

[Esta sección](../concepts/datasources.md#datasource-definition) describe cómo definir una fuente de datos en el diccionario de aplicación.

Se debe marcar el indicador 'Utilizar como origen de datos de tabla' en las fuentes de datos que se vayan a utilizar como origen de datos para tablas definidas en el diccionario de aplicación. Si este indicador está marcado:

- Se ocultará la subpestaña Campos de la fuente de datos de la ventana Fuente de datos. Las columnas devueltas por la fuente de datos que se utilizarán como origen de datos de tabla se definirán en la ventana Tabla y columnas, por lo que definirlas también en la ventana Fuente de datos sería redundante y confuso. 
- Las fuentes de datos con este indicador marcado se mostrarán en el desplegable Fuente de datos de la pestaña de cabecera de Tabla. 

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-table-based-on-a-user-defined-datasource-2.png){: .legacy-image-style}

## Definición de la tabla y sus columnas

[Esta sección](../how-to-guides/how-to-create-a-table.md#registering-the-table-within-the-application-dictionary) describe cómo definir en el diccionario de aplicación tablas basadas en tablas o vistas de base de datos.

El campo **Origen de datos** permite al usuario seleccionar el tipo de origen de datos para la tabla que está definiendo. Este campo es un desplegable que contiene dos opciones: Fuente de datos y Tabla. Si se selecciona la opción Tabla, se ocultará el desplegable Fuente de datos. Si se selecciona la opción Fuente de datos, se ocultarán los campos **Nombre tabla BD** y **Nombre de la clase Java**, y se mostrará el desplegable Fuente de datos. Este desplegable se utilizará para seleccionar la fuente de datos definida por el usuario que actuará como origen de datos de la tabla.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-table-based-on-a-user-defined-datasource-3.png){: .legacy-image-style}

No es posible utilizar **Crear columnas de la base de datos** para definir las columnas de tablas basadas en una fuente de datos, por lo que deberán añadirse manualmente.

## Definición de la ventana, sus pestañas y sus campos

Una vez que se han definido la tabla y sus columnas, es el turno de la ventana. Las ventanas con pestañas asociadas a tablas basadas en una fuente de datos se definen exactamente de la misma forma que las pestañas asociadas a tablas basadas en tablas de base de datos. [Esta sección](../how-to-guides/how-to-create-a-window.md) describe cómo hacerlo.

## Consideraciones de diseño

Existen algunas consideraciones de diseño que deben tenerse en cuenta al crear una tabla basada en una fuente de datos:

- Las pestañas asociadas a tablas basadas en una fuente de datos no pueden tener subpestañas. 
- No se genera ninguna clase Java para las tablas basadas en una fuente de datos. 
- Las fuentes de datos manuales deben implementar el filtrado, la ordenación y la paginación de las tablas. Si la fuente de datos manual que se está definiendo no admite filtrar claves foráneas basándose en su id, se debe desmarcar el indicador Support Filtering Foreign Key Columns Using Their ID. Por ejemplo, el criterio construido al filtrar la organización '*' usando su id sería: {fieldName: 'organization', operator: 'equals', value: '0'}. 

## Ejemplo: una ventana basada en una hoja de cálculo de Google

Esta sección es un resumen de una tabla basada en una fuente de datos que utiliza una hoja de cálculo de Google como su origen de datos.

En este ejemplo, una hoja de cálculo de Google que sirve como un gestor de incidencias

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-table-based-on-a-user-defined-datasource-4.png)

se utiliza como origen de datos para una ventana de Etendo

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-table-based-on-a-user-defined-datasource-5.png){: .legacy-image-style}

La ventana definida en este ejemplo tiene la misma funcionalidad que si se hubiera definido basándose en una tabla de base de datos. Es posible:

- Obtener registros 
- Actualizar registros en la vista de rejilla y formulario
- Crear nuevos registros 
- Ordenar la rejilla usando cualquier columna 
- Filtrar la rejilla

Cuando se actualiza un registro desde la ventana de Etendo, la hoja de cálculo de Google se actualiza en tiempo real. Si la hoja de cálculo de Google se actualiza manualmente, la rejilla de Etendo debe refrescarse para obtener los registros actualizados.

### Fuente de datos Java

Implementar la fuente de datos Java es el paso que más tiempo consume de todo el proceso. En esta sección, solo se va a demostrar la operación de obtención.

Esta fuente de datos se utilizará en una ventana de Etendo y permitirá obtener, añadir, actualizar y eliminar registros. En este caso, es muy conveniente extender la clase `DefaultDataSourceService`.

Esta es la implementación del método fetch:


``` java
    @Override
    public String fetch(Map<String, String> parameters) {
    int startRow = 0;
    final String startRowStr = parameters.get(JsonConstants.STARTROW_PARAMETER);
    if (startRowStr != null) {
        startRow = Integer.parseInt(startRowStr);
    }
    final List<JSONObject> jsonObjects = fetchJSONObject(parameters);
    final JSONObject jsonResult = new JSONObject();
    final JSONObject jsonResponse = new JSONObject();
    try {
        jsonResponse.put(JsonConstants.RESPONSE_STATUS, JsonConstants.RPCREQUEST_STATUS_SUCCESS);
        jsonResponse.put(JsonConstants.RESPONSE_STARTROW, startRow);
        jsonResponse.put(JsonConstants.RESPONSE_ENDROW, jsonObjects.size() + startRow - 1);
        jsonResponse.put(JsonConstants.RESPONSE_DATA, new JSONArray(jsonObjects));
        jsonResponse.put(JsonConstants.RESPONSE_TOTALROWS,
            parameters.get(JsonConstants.RESPONSE_TOTALROWS));
        jsonResult.put(JsonConstants.RESPONSE_RESPONSE, jsonResponse);
    } catch (JSONException e) {
        try {
        jsonResponse.put(JsonConstants.RESPONSE_STATUS, JsonConstants.RPCREQUEST_STATUS_SUCCESS);
        } catch (JSONException ex) {
        log.error("Error while building the response status", ex);
        }
    }
    return jsonResult.toString();
    }
```

La fuente de datos debe devolver una cadena Json con los siguientes atributos:

- `status`: indica si la obtención (fetch) se ha realizado correctamente. Si es correcta, se deben proporcionar estos otros atributos: 
- `startRow`: índice de la primera fila devuelta por la fuente de datos en la solicitud de obtención actual. 
- `endRow`: índice de la última fila devuelta por la fuente de datos en la solicitud de obtención actual. 
- `totalRows`: número total de filas que la fuente de datos puede devolver dados los filtros de la solicitud de obtención actual. 
- `data`: un array Json que contiene todos los objetos obtenidos. 

Se ha creado una clase de conveniencia llamada `GoogleSpreadsheet` como enlace entre la fuente de datos y la API de Google Docs. Su implementación puede encontrarse aquí.

Los objetos de datos se recuperan usando el método `fetchJSONObject`:

``` java
    private List<JSONObject> fetchJSONObject(Map<String, String> parameters) {
    final String startRowStr = parameters.get(JsonConstants.STARTROW_PARAMETER);
    final String endRowStr = parameters.get(JsonConstants.ENDROW_PARAMETER);
    int startRow = -1;
    int endRow = -1;
    // Obtains the startRow and endRow parameters
    if (startRowStr != null) {
        startRow = Integer.parseInt(startRowStr);
    }
    if (endRowStr != null) {
        endRow = Integer.parseInt(endRowStr);
    }
    // Retrieves the user credentials for Google Docs
    String username = OBPropertiesProvider.getInstance().getOpenbravoProperties()
        .getProperty("googleUsername");
    String password = OBPropertiesProvider.getInstance().getOpenbravoProperties()
        .getProperty("googlePassword");
    ListFeed feed = null;
    try {
        // Retrieves the Google Spreadsheet
        GoogleSpreadsheet spreadsheet = new GoogleSpreadsheet(SPREADSHEET_NAME, username, password);
        // Sets the sorting given the _sortBy parameter
        String sortByColumn = parameters.get(JsonConstants.SORTBY_PARAMETER);
        if (sortByColumn != null && !sortByColumn.isEmpty()) {
        spreadsheet.setOrderBy(sortByColumn);
        }
        // Sets the ID parameter if a specific record must be fetched
        String recordId = parameters.get(JsonConstants.ID);
        if (recordId != null && !recordId.isEmpty()) {
        spreadsheet.setRecordId(recordId);
        }
        // Retrieves the ListFeed given the spreadsheet name, user credentials, sorting criteria and
        // record ID
        feed = spreadsheet.getFeed();
    } catch (Exception e) {
        log.error("Error retrieving the feed", e);
    }
    // Retrieves the actual records to be returned given the feed, startRow, endRow and parameters
    final List<Map<String, Object>> data = getData(parameters, feed, startRow, endRow);
    // Converts the records to its Json representation
    final DataToJsonConverter toJsonConverter = OBProvider.getInstance().get(
        DataToJsonConverter.class);
    toJsonConverter.setAdditionalProperties(JsonUtils.getAdditionalProperties(parameters));
    return toJsonConverter.convertToJsonObjects(data);
    }
```

El método `getData` devuelve los registros que realmente se devolverán dado el `ListFeed` y el criterio de filtrado:

``` java 
    protected List<Map<String, Object>> getData(Map<String, String> parameters, ListFeed feed,
        int startRow, int endRow) {
    List<Map<String, Object>> result = new ArrayList<Map<String, Object>>();
    Map<String, String> filterCriteria = new HashMap<String, String>();
    try {
        // Builds the criteria based on the fetch parameters
        JSONArray criterias = (JSONArray) JsonUtils.buildCriteria(parameters).get("criteria");
        for (int i = 0; i < criterias.length(); i++) {
        final JSONObject criteria = criterias.getJSONObject(i);
        filterCriteria.put(criteria.getString("fieldName"), criteria.getString("value"));
        }
    } catch (JSONException e) {
        log.error("Error while building the criteria", e);
    }
    // Obtains all the feed entries
    List<ListEntry> entries = feed.getEntries();
    for (ListEntry entry : entries) {
        CustomElementCollection elements = entry.getCustomElements();
        IssueTrackerItem issue = new IssueTrackerItem(elements);
        // Adds to the result only the entries that are not filtered out
        if (applyFilter(issue, filterCriteria)) {
        result.add(issue.toMap());
        }
    }
    return result;
    }
```

Se ha creado otra clase de conveniencia llamada `IssueTrackerItem` para gestionar cada registro del gestor de incidencias.

### Fuente de datos de seguridad

Las fuentes de datos deben implementar un mecanismo de seguridad. El método `checkFetchDatasourceAccess` permite implementar un acceso de seguridad a una DataSource cuando se utiliza el método fetch(). El método `checkEditDatasourceAccess` se utiliza para implementar el mecanismo de seguridad en las operaciones de añadir, eliminar y actualizar. Se puede sobrescribir en fuentes de datos específicas para aplicar un mecanismo de seguridad particular. Este es un ejemplo de implementación del método `checkFetchDatasourceAccess`:

``` java
    @Override
    public void checkFetchDatasourceAccess(Map<String, String> parameter) {
    final OBContext obContext = OBContext.getOBContext();
    try {
        final Entity entity = ModelProvider.getInstance().getEntityByTableId(AD_TABLE_ID);
        if (entity != null) {
        obContext.getEntityAccessChecker().checkReadableAccess(entity);
        }
    } catch (OBSecurityException e) {
        handleExceptionUnsecuredDSAccess(e);
    }
    }
 
 
    @Override
    public void checkEditDatasourceAccess(Map<String, String> parameter) {
    // To implement security mechanism: add, remove and update.
    }
```

Para implementar el mecanismo de seguridad, se han implementado 3 métodos de comprobación en la clase `EntityAccessChecker`:

- `checkReadableAccess`(Entity entity): comprueba si una entidad es legible para el usuario actual. 
- `checkDerivedAccess`(Entity entity): comprueba si una entidad es derivada para el usuario actual. 
- `checkWritableAccess`(Entity entity): comprueba si una entidad es escribible para el usuario actual. 

### Definición de la fuente de datos en el diccionario de aplicación

Es muy fácil definir la fuente de datos en el diccionario de aplicación. Simplemente asegúrese de introducir el nombre correcto de la clase Java y de marcar el indicador **Utilizar como origen de datos de tabla**.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-table-based-on-a-user-defined-datasource-6.png){: .legacy-image-style}
  

### Definición de la tabla y las columnas en el diccionario de aplicación

Asegúrese de seleccionar la opción 'Fuente de datos' en el desplegable 'Origen de datos'. La fuente de datos definida en el paso anterior debería mostrarse en el desplegable 'Fuente de datos'.

La tabla no se basa en una tabla de base de datos, por lo que sus columnas deben añadirse manualmente:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-table-based-on-a-user-defined-datasource-7.png){: .legacy-image-style}

Al menos una columna debe definirse como clave primaria.

El nombre de las columnas en el diccionario de aplicación es el mismo que el título de las columnas en la hoja de cálculo de Google; esto simplifica la implementación de la fuente de datos.

### Definición de la ventana, la pestaña y los campos en el diccionario de aplicación

Definir la ventana, la pestaña y el campo en el diccionario de aplicación se realiza de la misma forma que con las tablas estándar:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-table-based-on-a-user-defined-datasource-8.png){: .legacy-image-style}

---
Este trabajo es una obra derivada de [Cómo crear una tabla basada en una fuente de datos definida por el usuario](http://wiki.openbravo.com/wiki/How_to_Create_a_Table_Based_on_a_User_Defined_Datasource){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.