---
title: Cómo crear un Selector Múltiple
tags: 
    - Selector Múltiple
    - Parámetros
    - Configuración del selector 
    - Entrada del proceso
    - Valores de backend
status: beta
---

# Cómo crear un Selector Múltiple

!!! example "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.

## Visión general

**Selector Múltiple** es una referencia que permite seleccionar múltiples elementos al mismo tiempo. Está pensado para usarse como parámetro de una [Definición de Proceso Estándar](../how-to-guides/how-to-create-a-standard-process-definition.md). La referencia Selector Múltiple se define prácticamente igual que los selectores normales, que permiten seleccionar un único valor. 

## Módulo de ejemplo 

Esta sección está respaldada por un módulo de ejemplo que muestra ejemplos del código mostrado y comentado. El código del módulo de ejemplo puede descargarse desde este [repositorio](https://github.com/etendosoftware/com.etendoerp.client.application.examples){target="\_blank"}. 
 
## Pasos para implementar el proceso

Esta sección explica cómo crear un **selector múltiple de pedidos**.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-multi-selector/how-to-create-a-multi-selector-1.png){: .legacy-image-style}
![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-multi-selector/how-to-create-a-multi-selector-2.png){: .legacy-image-style}

### Definir el selector

- Como **Administrador del sistema**, abra la ventana **Referencia**. 
- Cree un nuevo registro. 
  - Nombre: **Selector múltiple de pedidos** 
  - Referencia padre: Referencia de selector `OBUISEL_Multi` 
- En la solapa **Selector Definido**, establezca las propiedades del selector: 
  - Plantilla: **Plantilla de selector** 
  - Tabla: `C_Order`

### Añadir campos al pop-up del selector

El último paso es definir cuáles son los campos que estarán presentes en el pop-up para seleccionar registros.

- Vaya a la solapa **Campo de Selector Definido** 
- Cree registros: 
  - **Nombre**: es el nombre que verá el usuario (p. ej., Tercero).
  - **Propiedad**: propiedad real desde la que se recupera la información (p. ej., businessPartner). 
  - **Ordenación de columnas** en la rejilla: posición de esta columna en la rejilla (p. ej., 20). 

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-multi-selector/how-to-create-a-multi-selector-3.png){: .legacy-image-style}

### Usar el selector

Este selector puede usarse como parámetro para una **Definición del Proceso**. 

!!! info
    Para más información, visite [Cómo crear una Definición de Proceso Estándar](../how-to-guides/how-to-create-a-standard-process-definition.md).

### Recuperar valores en backend

En el backend, el Java que implementa el proceso recibe un `JSONArray` con los IDs de todas las filas seleccionadas. En caso de que no se seleccione ninguna fila, se recibe un array vacío.

```java   
   
//...
JSONArray orders = params.getJSONArray("orders"); // get the array


// iterate it
for (int i = 0; i < orders.length(); i++) {
    // ...
}
```

## Temas avanzados

### Usar selector con consulta personalizada

Al usar una consulta personalizada para definir el selector, debe existir un alias en la consulta llamado `_identifier`, que se utilizará como identificador legible por el usuario para los registros seleccionados, y otro llamado `id`, que se enviará al backend como id de los registros seleccionados. También se requieren campos para estas columnas de la consulta con los mismos nombres. 

!!! note
    Los selectores múltiples solo pueden usarse como parámetros en **Definición de Proceso Estándar**; no pueden incluirse en **ventanas estándar**.

---
Este trabajo es una obra derivada de [Cómo crear un Selector Múltiple](http://wiki.openbravo.com/wiki/How_to_create_a_Multi_Selector){target="\_blank"} de [Wiki de Openbravo](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.