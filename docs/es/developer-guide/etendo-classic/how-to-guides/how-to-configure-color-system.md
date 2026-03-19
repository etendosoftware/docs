---
tags:
  - How to
  - Color System
  - UI
  - Extensibility

status: new
---

# Cómo configurar el soporte del sistema de color en la UI

## Visión general

El sistema de color en Etendo permite asignar identificadores visuales (etiquetas de color) a registros dentro de una rejilla o formulario en la UI de Workspace, mejorando la experiencia de usuario al resaltar información clave. Esta funcionalidad utiliza el sistema de extensibilidad de Etendo y puede aplicarse sin modificar el código base de la interfaz gráfica.

Un caso de uso común es aplicarlo a tablas maestras como **Categoría de producto** (`M_Product_Category`) o **Grupo de terceros** (`C_BP_Group`), ya que se referencian con frecuencia en rejillas principales como Productos o Clientes.

## Cómo funciona el sistema de color

Para que un color aparezca en la UI, el campo en la tabla principal debe referenciar una tabla maestra mediante una clave foránea (referencia **TableDir** o **Tabla**). La UI de Workspace y Etendo se coordinan mediante una interacción entre los metadatos y el frontend en React:

1. **Inyección de metadatos**: el backend comprueba si el diccionario de datos tiene la columna configurada con el tipo de referencia **Color**. Si es así, inyecta `colorFieldName` en los metadatos gráficos para indicar el nombre de la propiedad.
2. **Petición del frontend**: los hooks de obtención de datos (Datasource) en Next.js evalúan cada columna definida. Si una columna especifica metadatos `colorFieldName`, el frontend añade la dependencia como `_extraProperties` a la petición de la API (p. ej., `_extraProperties=M_Product_Category_ID$EM_SMF_Color`), lo que indica al backend que realice los JOIN correspondientes y devuelva el valor de color en la respuesta JSON.
3. **Renderizado de la interfaz**: al procesar las celdas, el frontend comprueba la propiedad de color enlazada y renderiza una insignia **Tag** usando el valor hex, calculando un color de texto con contraste adecuado.

Esta arquitectura garantiza eficiencia sin modificar el payload estándar. Los valores de color se actualizan en tiempo real en la **Vista de formulario**, la **Vista principal de rejilla** y durante la **edición en línea**.

## Paso a paso: configurar Color en Categoría de producto

El siguiente procedimiento usa `M_Product_Category` como ejemplo.

### 1. Añadir la columna Color en el diccionario de datos

1. Accede al entorno Etendo ERP Classic con el rol **Administrador del sistema**.
2. Navega a la ventana **Tablas y columnas**.
3. Busca la tabla maestra — en este caso, `M_Product_Category` (Categoría de producto).
4. En la pestaña **Columnas**, crea una nueva columna usando el prefijo del módulo (p. ej., `EM_CRM_Color` o `EM_SMF_Color`).
5. Asigna el tipo de referencia **Color** a la nueva columna. Este es el paso clave que permite al sistema reconocer el propósito de la columna.
6. Establece la longitud en 7 o 10 caracteres — suficiente para almacenar un código hex como `#FF0000`.

!!! note
    Usar el tipo de referencia **Color** permite al backend detectar el propósito de la columna independientemente de su nombre, integrándola de forma transparente en los metadatos leídos por el frontend.

### 2. Aplicar cambios en base de datos y mostrar la columna

1. Aplica los cambios compilando el sistema:

    ```bash title="Terminal"
    ./gradlew smartbuild
    ```

2. Navega a la ventana **Ventana, pestaña y campo** en Etendo Classic.
3. Busca la ventana **Categoría de producto**.
4. En la pestaña **Campo**, añade o recarga el registro de la nueva columna para que aparezca en la interfaz del ERP Classic.

### 3. Verificar la configuración

1. Abre la ventana **Categoría de producto** en Etendo Classic.
2. Selecciona un registro existente (p. ej., la categoría *Standard*).
3. Introduce un valor de color hex en el nuevo campo (p. ej., `#8E44AD`) y guarda.
4. Abre la UI de Workspace y navega a la ventana **Productos** (`M_Product`).
5. En la rejilla de productos, localiza la columna **Categoría de producto** (`M_Product_Category_ID`).

El frontend detecta la configuración de color, añade el parámetro de petición `_extraProperties` y renderiza el valor de la categoría como una insignia coloreada.

!!! info
    Este comportamiento es agnóstico al módulo y agnóstico a la variable. Cualquier tabla maestra con una columna configurada con el tipo de referencia **Color** se soporta automáticamente en rejillas y formularios sin desarrollo adicional.

## Alcance y restricciones

### Campos afectados

El renderizado de insignias de color se aplica solo a **campos de clave foránea (TableDir / Tabla)** que referencian una tabla maestra con una columna de color configurada. Ejemplos:

- `M_Product_Category_ID` en la tabla Productos.
- `Priority_ID` en la tabla Tareas.
- `C_Currency_ID` en la tabla Facturas.

### Campos no afectados

Esta funcionalidad no afecta a:

- Campos de texto plano (Strings).
- Campos numéricos, de fecha o booleanos.
- Desplegables de lista estática (tipo de referencia *List*) definidos en dominios de referencia.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.