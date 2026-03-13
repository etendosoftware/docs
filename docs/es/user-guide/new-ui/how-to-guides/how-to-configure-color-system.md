---
tags:
  - How to
  - Color System
  - UI
  - Extensibility
---

# Cómo Configurar el Soporte al Sistema de Colores en la UI

## Visión General

El sistema de colores en Etendo permite asignar identificadores visuales (pastillas de color) a registros dentro de una grilla o formulario en Workspace UI, mejorando la experiencia del usuario al destacar información clave. Esta funcionalidad aprovecha el sistema de extensibilidad de Etendo para aplicarse transparentemente sin necesidad de alterar el código base de la interfaz gráfica.

Un excelente caso de uso (y uno de los más visuales) es aplicarlo a tablas maestras como la **Categoría de Producto (M_Product_Category)** o el **Grupo de Terceros (C_BP_Group)**, ya que estas son muy utilizadas dentro de grillas principales (como la grilla de Productos o la de Terceros/Clientes).

## ¿Cómo funciona la relación con la otra tabla?

Para que el color se refleje en la UI, el campo en cuestión en la tabla principal debe apuntar a una tabla maestra a través de una Foreign Key (Referencia **TableDir** o **Table**). 

La implementación actual en Workspace UI y Etendo funciona de manera coordinada gracias a una simbiosis entre la metadata y el frontend de React:

1. **Inyección de Metadata:** El backend deduce si una tabla hija necesita mostrar un color verificando si el diccionario de datos tiene configurada la columna con la Referencia asignada al tipo "Color". De ser así, inyecta `colorFieldName` indicando cómo se llama esta propiedad hacia la metadata gráfica.
2. **Petición del lado del Front:** Los hooks de obtención de datos (Datasource) en NextJS revisan activamente cada columna definida. Si alguna especifica la metadata `colorFieldName`, el frontend añade al vuelo esa dependencia para solicitarla en la Request a la API (ej: `_extraProperties=M_Product_Category_ID$EM_SMF_Color`). Esto le fuerza al backend a hacer los JOIN correspondientes y volcar el valor final del color al formato JSON.
3. **Renderizado en la Interfaz:** Al momento de procesar las celdas, el frontend comprueba si recibió esta propiedad vinculada al color y le asigna automáticamente el componente visual en forma de 'Tag' (pastilla envuelta), usando el valor hexa recuperado y calculando un texto con buen contraste de legibilidad.

Esta arquitectura explícita garantiza eficiencia sin corromper el payload estándar. De igual manera, se actualiza en tiempo real tanto en la **Vista de Formulario (Form View)**, en la **Vista de Grilla Principal (Grid View)**, y a la hora de mutar la información por medio de la **Edición en Línea (Inline Editing)** (donde el cliente vuelve a efectuar una petición del registro pidiendo los `_extraProperties` de colores al guardar exitosamente).

## Paso a Paso: Configurar el Color en la Categoría de Productos

A continuación, se detalla el procedimiento exacto para probar e implementar esto utilizando la tabla `M_Product_Category` como ejemplo:

### 1. Agregar la columna de Color en el Diccionario de Datos

1. Ingresa a tu entorno de **Etendo ERP Classic** con el rol de **System Administrator** (Administrador del Sistema).
2. Ve a la ventana **Tables and Columns** (Tablas y Columnas).
3. Busca la tabla maestra de interés, en este caso `M_Product_Category` (Categoría de Producto).
4. En la pestaña de *Columns*, crea una nueva columna utilizando tu prefijo de módulo (por ejemplo `EM_CRM_Color` o usar el prefijo de tu módulo de pruebas activo).
5. Asigna a esta nueva columna el tipo de referencia **Color**. Esta es la instrucción clave y mejor práctica para que el sistema reconozca oficial y estructuradamente que este campo soportará colores.
6. La longitud ideal es de 7 o 10 caracteres; suficientes para guardar en su interior un código hexadecimal (`#FF0000`).

!!!note "Nota clave"
      Al utilizar el Reference "Color", el backend detectará explícita y correctamente el propósito de tu columna sin depender del nombre exacto bajo el que la registres, integrándola transparentemente a la metadata que lee el frontend.

### 2. Aplicar la tabla en la BD y mostrar la columna

Luego de definir la columna en el diccionario de datos, debes materializarla en la base de datos:
1. Aplica los cambios mediante el proceso clásico compilando en consola (ej. `gradlew smartbuild` o reconstruyendo de manera apropiada la base de datos).
2. Ve a la ventana **Window, Tab and Field** (Ventana, Pestaña y Campo) dentro del entorno Etendo.
3. Busca la ventana correspondiente, en este caso **Product Category**.
4. Asegúrate recargar la pestaña o cerciorarte de agregar/crear el registro para la pestaña central de **Field** respecto a esa nueva columna, logrando así que el campo esté listo para ser usado y se visualice en la interfaz del ERP clásico.

### 3. Prueba de Fuego (¡La Magia Visual!)

1. Abre la ventana **Product Category** (Categoría de Producto) en Etendo Classic.
2. Selecciona un registro existente, por ejemplo la categoría titulada "Standard" (o directamente sobre la que decidas usar).
3. Escribe un valor hexadecimal identificativo y bien llamativo sobre el nuevo campo de color. Por ejemplo: `#8E44AD` (Un color púrpura oscuro), y guarda finalmente el registro.
4. Ahora, ve a través del frontend de **NextJS de Workspace UI**.
5. Abre la ventana principal respectiva para **Products** (Productos o `M_Product`).
6. En aquella grilla resultante de productos, busca la columna "Categoría de Producto" (`M_Product_Category_ID`).
7. **¡Sorpresa!** Si esta categoría suele verse como un simple texto azul detallando el contenido "Standard", ahora notarás un cambio muy atractivo. Al pedirse los datos, el frontend detectará que hay una configuración para pedir metadatos de ese color (`_extraProperties`), inyectará la petición extra, la base de datos lo procesará automáticamente por detrás y la UI terminará pintando el texto en una hermosa pastilla redondeada color púrpura.

Lo genial de este diseño es que todo ha quedado **totalmente agnóstico de módulos y variables específicas**. Siempre que la tabla maestra cuente con una columna configurada con el Reference "Color", el componente subyacente de UI la aprovechará sin problemas. Uno puede aplicarlo a tablas de Monedas, Métodos de Pago, Vendedores o Almacenes... e instantáneamente brotarán coloreadas en la grilla y formulario sin que se requiera programar ni un solo componente auxiliar.

## Restricciones y Análisis de Alcance

### ¿A qué campos afecta y permite intervenir?

La lógica dinámica de inyección de metadata y renderizado de pastillas de color **solo afecta a campos (Fields) definidos como tipo de Referencia Foránea (Foreign Keys / TableDir / Table)** hacia la tabla maestra que ya cuenta con la columna de color configurada. Algunos ejemplos concisos incluyen:

* `M_Product_Category_ID` apuntando en la tabla de Productos.
* `Priority_ID` reflejándose en la tabla de Tareas.
* `C_Currency_ID` visualizándose en la tabla de Facturas.

### ¿A qué campos NO afecta o resultan omitidos?

Su dinámica de control actual **NO afectará o incidirá bajo los elementos a continuación especificables**:

* Campos de texto estáticos y regulares (Cadenas o *Strings* convencionales).
* Valores Numéricos, Fechas naturales o datos de tipo Booleanos.
* Listas estáticas predefinidas en el sistema (Es decir, menús desplegables del propio tipo *List* codificados de forma fija o *hardcodeada* bajo los dominios de las Listas de Referencia en el diccionario).

---