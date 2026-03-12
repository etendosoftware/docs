---
tags:
  - How to
  - PickandExecute
  - Definición del Proceso
  - action handler
  - Acciones
  - Patrón estándar de UI
---

# Cómo crear un proceso de Seleccionar y Ejecutar

## Visión general

**Seleccionar y Ejecutar (P&E)** es un caso de **Definición del Proceso** con **patrón estándar de UI**.

Esta sección añadirá un nuevo proceso de Seleccionar y Ejecutar y lo asociará con la **ventana Pedido de ventas**.

La implementación requiere experiencia en desarrollo.

Las siguientes páginas de conceptos proporcionan información de base sobre action handlers y desarrollo JavaScript:

- [Action Handler](how-to-create-client-event-handler-actions.md)
- [Desarrollo del lado del cliente y API](../concepts/client-side-development-and-api.md)
- [Convenciones de codificación JavaScript](../concepts/javascript-coding-conventions.md)

## Pasos para implementar el proceso

### Visión general

Los procesos P&E aprovechan los mismos conceptos base en el Diccionario de la Aplicación. Se utilizarán **Ventana, Solapas y Campos** para definir el grid editable que se mostrará, una nueva **Referencia** para el parámetro del proceso; y después se implementará un **action handler** que se ejecutará cuando el usuario pulse el botón **Hecho**.

### Implementación

#### Definir la ventana

1. Cree una nueva ventana
2. Rellene los campos obligatorios
3. Seleccione **Seleccionar y Ejecutar** como tipo de ventana

    ![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Pick_and_Execute_Process-1.png)

4. Siguiendo los mismos conceptos, se requiere una **Tabla** como fuente de datos.

    - En caso de que sea necesario mezclar información de varias tablas, existen diferentes opciones:

      - Una vista de base de datos utilizada para crear una tabla en [Diccionario de la Aplicación](how-to-create-a-table.md).
      - Una tabla basada en una [Consulta HQL](how-to-create-a-hql-based-table.md).
      - Una tabla basada en un [origen de datos manual](how-to-create-a-table-based-on-a-user-defined-datasource.md).

    ![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Pick_and_Execute_Process-2.png)

5. Cree los campos necesarios que se convertirán en las columnas del grid. Seleccione una **Columna** y preste atención a algunas propiedades importantes:

    - **Mostrar:** Debe estar marcada para generar un campo. Si Mostrar no está marcada, no se generará ningún campo.
    - **Sólo lectura:** La mayoría de las veces todos los campos serán de sólo lectura. Si desea que un usuario pueda modificar algunos datos, por ejemplo la cantidad, déjelo sin marcar.
    - **Mostrar en la relación:** Define si el campo se mostrará en el grid. Se puede definir un campo como mostrado pero no mostrado en el grid, de modo que se generará un campo pero no se mostrará. Esto es útil para recuperar datos al grid y enviarlos al proceso.
    - **Posición en grid:** Define la secuencia de los campos en el grid.

    ![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Pick_and_Execute_Process-3.png)

#### Definir la referencia

Después de definir la ventana, es necesario definir una nueva Referencia.

1. Cree una nueva Referencia
2. Seleccione en el desplegable Referencia base: Referencia de ventana
3. Guarde

    ![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Pick_and_Execute_Process-4.png)

4. Vaya a la solapa Ventana
5. Cree un nuevo registro
6. Seleccione la ventana recién creada
7. Guarde

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Pick_and_Execute_Process-5.png)

#### Definir el proceso

Existe una nueva ventana para procesos: **Definición del Proceso**

1. Abra la ventana Definición del Proceso
2. Cree un nuevo registro
3. Defina el patrón de UI: Estándar (parámetros definidos en el Diccionario)
4. Establezca el Handler (clase Java que implementa el proceso)
5. Guarde

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Pick_and_Execute_Process-6.png)

##### Parámetros

La Referencia de ventana es una implementación de un **parámetro enriquecido**.

1. Vaya a la solapa Parámetros
2. Cree un nuevo registro
3. Rellene los campos obligatorios. El nombre del parámetro será el nombre mostrado en el título del proceso en ejecución.
4. Seleccione Referencia de ventana
5. Seleccione la ventana que definió previamente
6. Guarde

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Pick_and_Execute_Process-7.png)

#### Añadir un botón a Pedido de ventas

##### Crear una columna

Se requiere una nueva columna para asociarla a un botón.

!!!info
    Para más información, visite [Cómo añadir un campo a una solapa de ventana](how-to-add-a-field-to-a-window-tab).

1. Cree una nueva columna en la tabla `C_Order`. Sintaxis `PostgreSQL`:

    ```
    ALTER TABLE c_order ADD COLUMN em_obexapp_pick1 character(1);
    ALTER TABLE c_order ALTER COLUMN em_obexapp_pick1 SET DEFAULT 'N'::bpchar;
    ```

2. Vaya a: Tablas y Columnas
3. Abra el registro `C_Order`
4. Ejecute el proceso: **Crear columnas de la base de datos**
5. Vaya a la solapa **Columna**
6. Seleccione la columna recién creada
7. Cambie la referencia de: Sí/No a Botón
8. Seleccione el proceso definido

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Pick_and_Execute_Process-8.png)

##### Crear un campo

1. Vaya a Ventana, Solapas y Campos
2. Busque Pedido de ventas
3. Cree un nuevo campo asociado con la columna

  ![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Pick_and_Execute_Process-9.png)

#### Implementación Java

En el caso de un action handler de Seleccionar y Ejecutar, extienda de **BaseProcessActionHandler** e implemente el método **doExecute**.

```java title="PickExampleActionHandler.java"
/*
  *************************************************************************
  * The contents of this file are subject to the Openbravo  Public  License
  * Version  1.1  (the  "License"),  being   the  Mozilla   Public  License
  * Version 1.1  with a permitted attribution clause; you may not  use this
  * file except in compliance with the License. You  may  obtain  a copy of
  * the License at http://www.openbravo.com/legal/license.html
  * Software distributed under the License  is  distributed  on  an "AS IS"
  * basis, WITHOUT WARRANTY OF ANY KIND, either express or implied. See the
  * License for the specific  language  governing  rights  and  limitations
  * under the License.
  * The Original Code is Openbravo ERP.
  * The Initial Developer of the Original Code is Openbravo SLU
  * All portions are Copyright (C) 2011 Openbravo SLU
  * All Rights Reserved.
  * Contributor(s):  ______________________________________.
  ************************************************************************
  */
package org.openbravo.client.application.examples;
 
import java.util.Map;
 
import org.apache.log4j.Logger;
import org.codehaus.jettison.json.JSONArray;
import org.codehaus.jettison.json.JSONObject;
import org.openbravo.client.application.ApplicationConstants;
import org.openbravo.client.application.process.BaseProcessActionHandler;
 
/**
  * @author iperdomo
  *
  */
public class PickExampleActionHandler extends BaseProcessActionHandler {
 
  private static final Logger log = Logger.getLogger(PickExampleActionHandler.class);
 
  @Override
  protected JSONObject doExecute(Map<String, Object> parameters, String content) {
    try {
      JSONObject request = new JSONObject(content);
 
      log.info(">> parameters: " + parameters);
      // log.info(">> content:" + content);
 
      // _selection contains the rows that the user selected.
      JSONArray selection = new JSONArray(
          request.getString(ApplicationConstants.SELECTION_PROPERTY));
 
      log.info(">> selected: " + selection);
 
      // _allRows contains all the rows available in the grid
      JSONArray allRows = new JSONArray(request.getString(ApplicationConstants.ALL_ROWS_PARAM));
 
      log.info(">> allRows: " + allRows);
 
      // A Pick and Execute process can have several buttons (buttonList)
      // You can know which button was clicked getting the value of _buttonValue
      log.info(">> clicked button: " + request.getString(ApplicationConstants.BUTTON_VALUE));
 
      return request;
    } catch (Exception e) {
      log.error("Error processing request: " + e.getMessage(), e);
    }
    return new JSONObject();
  }
}
```

## Probar el proceso

Dado que la estructura de alguna entidad se ha modificado al añadir una nueva columna, es necesario reiniciar el servidor tomcat.

- Después de reiniciar, debería poder ir a la ventana Pedido de ventas y ver un nuevo botón.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Pick_and_Execute_Process-10.png)

## Temas avanzados

### Seleccionar por defecto

La fuente de datos (tabla o vista) definida en la solapa puede establecer qué filas se seleccionarán por defecto cuando el usuario lance el proceso. Solo es necesario crear una columna `c_ob_selected`, que se convertirá en una propiedad `obSelected` en la entidad generada. Cuando el valor de esta columna sea **Y**, la fila se seleccionará por defecto. Aquí tiene un ejemplo funcional:
`M_RM_RECEIPT_PICK_EDIT.xml`.

!!!note
    Al registrar la columna en el Diccionario de la Aplicación debe utilizarse la referencia **Sí/No**.

### Función de Validación

Defina, a nivel de campo, una función de validación JavaScript. En un campo editable, cuando el usuario introduzca un valor, se ejecutará esta función.

1. Vaya a Ventana, Solapas y Campos
2. Seleccione su ventana y la solapa
3. Vaya al campo Cantidad

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Pick_and_Execute_Process-11.png)

#### Definición JavaScript

- El proveedor de componentes debe registrar un nuevo recurso global.
- Si la función devuelve false, la celda se marcará con un error.
- En el JavaScript, defina una función de validación, por ejemplo:

```javascript
OB.OBHT = {};
OB.OBHT.validate = function (item, validator, value, record) {
  // item has access to grid: item.grid
  // from the grid you can get all selected records and edited values, e.g.
  //   * item.grid.getSelection()
  //   * item.grid.getEditedRecord()
  // grid has access to view: grid.view
  // view has access to parentWindow: view.parentWindow (the window running the process)
  // parentWindow has access to currentView
  // currentView has getContextInfo
  // debugger;
  if (window.console) {
    console.log("validation function!", value);
  }
  return true;
};
```

### Función de Selección

Se puede definir una función de selección a nivel de solapa. Esta función se llamará cuando el usuario seleccione/deseleccione una fila.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Pick_and_Execute_Process-12.png)

Y defina una función JavaScript en su archivo estático `.js` cargado:

```javascript
OB.OBHT.selectionChanged = function (grid, record, recordList) {
  if (window.console) {
    console.log("selection function!");
    console.log(grid, record, recordList);
  }
};
```

Si desea cambiar cualquier valor del registro seleccionado, utilice la siguiente instrucción:

```javascript
grid.setEditValue(grid.getRecordIndex(record), columnName, newColumnValue)
```

### Realizar varias acciones después de la ejecución

Después de que el proceso se ejecute, se puede realizar una serie de acciones.

!!!info
    Para más información sobre varias acciones después de la ejecución, consulte [Cómo crear una Definición de Proceso estándar](how-to-create-a-standard-process-definition.md).

Este trabajo es una obra derivada de [Cómo crear un proceso de Seleccionar y Ejecutar](http://wiki.openbravo.com/wiki/How_to_create_a_Pick_and_Execute_Process){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.