---
title: Cómo añadir un campo canvas a un Formulario o Cuadrícula
tags:
    - Cómo
    - Campo canvas
    - Personalización de formularios
    - Personalización de cuadrículas
    - Desarrollo JavaScript
    - Componentes de UI
    - Eventos JavaScript
---

# Cómo añadir un campo canvas a un Formulario o Cuadrícula

## Visión general

Esta guía explica cómo integrar campos canvas en formularios y cuadrículas dentro de Etendo, permitiendo añadir componentes visuales personalizados como botones, enlaces y etiquetas calculadas.  
Los campos canvas ofrecen una presentación e interacción dinámica de datos, aprovechando conocimientos de desarrollo JavaScript para su implementación.

## Introducción

Un campo canvas permite al usuario añadir cualquier componente visual a un formulario o a una fila en una cuadrícula.  
Este concepto puede utilizarse para añadir un campo calculado a un formulario y a una cuadrícula.  
Los componentes visuales que se pueden añadir son, por ejemplo, botones, enlaces y etiquetas (calculadas).

En esta sección, añadiremos un botón y un campo calculado al formulario y a cada fila de la cuadrícula.  
Ilustraremos cómo la información del registro y del formulario puede utilizarse para obtener información dinámica del Formulario/Cuadrícula.

La implementación de campos canvas requiere experiencia en desarrollo JavaScript.  
Consulte las siguientes páginas de conceptos para obtener información de base sobre el desarrollo JavaScript:

- [Desarrollo del lado del cliente y API](../concepts/client-side-development-and-api.md)
- [Convenciones de codificación JavaScript](../concepts/javascript-coding-conventions.md) 

También tiene sentido estudiar la siguiente página: [Arquitectura de Etendo](../concepts/etendo-architecture.md).

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-add-a-canvas-field-to-a-form-or-grid/canvas-field-to-a-form-or-grid-1.png)

## Módulo de ejemplo

Esta sección se apoya en un módulo de ejemplo que muestra ejemplos del código mostrado y comentado.

El código del módulo de ejemplo puede descargarse desde este repositorio: [com.etendoerp.client.application.examples](https://github.com/etendosoftware/com.etendoerp.client.application.examples){target="\_blank"}

## Pasos principales de desarrollo para crear un nuevo campo canvas

El desarrollo consta de 2 pasos:

1. Implementar el propio canvas; normalmente esto se hace en JavaScript. 
2. Especificar la clase JavaScript del canvas en la definición del campo de la solapa/ventana. 

### Implementación de su canvas en JavaScript

El primer paso es implementar su clase canvas en JavaScript. Esto se hace en 2 pasos:

- Crear un archivo de [javascript](../concepts/client-side-development-and-api.md#adding-javascript-to-etendo) con su clase JavaScript y colocarlo en el directorio correcto; la convención es ubicar los archivos js en el siguiente directorio dentro de su módulo: `web/[module.java.package]/js` 
- Registrar el archivo JavaScript (y otros recursos estáticos como archivos css) en Etendo usando un [ComponentProvider](../concepts/etendo-architecture.md#component-provider) 

El módulo de ejemplo implementa un botón y un campo calculado en el archivo `example-canvas-field.js`.

El primer ejemplo del archivo implementa un botón que muestra el identificador del registro actual:

```javascript title="example-canvas-field.js"
isc.defineClass('OBEXAPP_SalesOrderActionButton', isc.OBGridFormButton);
 
isc.OBEXAPP_SalesOrderActionButton.addProperties({
  noTitle: true,
  title: OB.I18N.getLabel('OBUISC_Identifier'),
  click: function() {
    var info = '';
    if (this.record) {
      info = this.record._identifier;
    } else if (this.canvasItem) {
      info = this.canvasItem.form.getValue(OB.Constants.IDENTIFIER);
    }
    isc.say(info);
  }
});
```

El segundo ejemplo muestra un campo calculado que divide 2 valores del registro actual y muestra el resultado de forma formateada.  
También ilustra varios métodos que se llaman cuando cambia el contexto/entorno (por ejemplo, cuando cambia un valor en el formulario):


```javascript title="example-canvas-field.js"
isc.defineClass('OBEXAPP_SalesOrderCalculated', isc.Label);
 
isc.OBEXAPP_SalesOrderCalculated.addProperties({
  height: 1,
  width: 1,
  overflow: 'visible',
  contents: '',
  initWidget: function() {
    if (this.canvasItem) {
      this.computeContents(this.canvasItem.form.getValue('grandTotalAmount'), this.canvasItem.form.getValue('summedLineAmount'));
    }
 
    this.Super('initWidget', arguments);
  },
  
  // is called when the form gets redrawn
  redrawingItem: function() {
    this.computeContents(this.canvasItem.form.getValue('grandTotalAmount'), this.canvasItem.form.getValue('summedLineAmount'));
  },
  
  // is called when a field on the form changes its value
  onItemChanged: function() {
    this.computeContents(this.canvasItem.form.getValue('grandTotalAmount'), this.canvasItem.form.getValue('summedLineAmount'));
  },
  
  // is called in grid-display mode when the canvas is created/used
  // for a record
  setRecord: function(record) {
    this.computeContents(record.grandTotalAmount, record.summedLineAmount);
  },
  
  computeContents: function(val1, val2) {
    var num;
    if (!val2) {
      this.setContents('');
    } else {
      num = OB.Utilities.Number.JSToOBMasked(val1/val2, 
          OB.Format.defaultNumericMask,
          OB.Format.defaultDecimalSymbol,
          OB.Format.defaultGroupingSymbol,
          OB.Format.defaultGroupingSize);
      
      this.setContents(num);
    }
  }
});
```

El archivo JavaScript se registra en el [ComponentProvider](../concepts/etendo-architecture.md#component-provider) del módulo de ejemplo de la siguiente manera:


```java title="ExampleComponentProvider.java"
@Override
public List<ComponentResource> getGlobalComponentResources() {
  final List<ComponentResource> globalResources = new ArrayList<ComponentResource>();
  globalResources.add(createStaticResource(
      "web/org.openbravo.client.application.examples/js/example-canvas-field.js", false));
.....
```

### Definición del canvas en el Campo de solapa (ADField)

El siguiente paso es crear un nuevo campo en la solapa y establecer su campo de clase de cliente:  

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-add-a-canvas-field-to-a-form-or-grid/canvas-field-to-a-form-or-grid-2.png)

También es posible añadir propiedades en línea en el campo `Clientclass`; por ejemplo, `OBEXAPP_SalesOrderActionButton {"title": "Mi botón de acción"}`

### El resultado

El resultado se muestra tanto en la cuadrícula como en el formulario:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-add-a-canvas-field-to-a-form-or-grid/canvas-field-to-a-form-or-grid-3.png)

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-add-a-canvas-field-to-a-form-or-grid/canvas-field-to-a-form-or-grid-4.png)

## Eventos JavaScript pasados al canvas

Al implementar su canvas, debe tener en cuenta que el canvas se utiliza en 3 situaciones diferentes:

- Al mostrar una fila en la cuadrícula 
- Al editar una fila en la cuadrícula 
- En vista de formulario, al editar un registro 

Los 2 últimos casos son similares.

En modo de visualización de cuadrícula, se aplica lo siguiente:

- En modo cuadrícula, se establecen las siguientes propiedades en el canvas:

    - `grid`: el objeto de cuadrícula 
    - `rowNum`: el número de fila/índice de registro para el que se utiliza el canvas 
    - `record`: el registro para el que se utiliza el canvas 
    - `colNum`: la columna en la que se muestra el canvas 
    - `field`: el campo donde se utiliza el canvas

- Un canvas puede crearse y agruparse (pooled), por lo que con el tiempo se crea una vez y se reutiliza cuando los registros se desplazan a la vista.  
  Cuando se utiliza un canvas para un registro, entonces se llama al método setRecord en él (si el canvas tiene este método). 

En modo de edición de formulario o edición de cuadrícula, se aplica lo siguiente:

- Se establecerá la propiedad canvasItem apuntando al elemento de formulario; el canvasItem puede utilizarse para acceder al propio formulario y a la cuadrícula (si se edita en la cuadrícula): 
  
    - `this.canvasItem.form`: la instancia del formulario 
    - `this.canvasItem.form.grid`: en caso de edición en cuadrícula 

- Si el canvas tiene una propiedad noTitle con el valor `true`, entonces en modo formulario no se muestra ningún título/etiqueta. 
- Cambios en el formulario: el canvas puede capturar eventos de cambio de formulario/valor implementando 2 métodos (ambos sin argumentos): 
    - `onItemChanged`: se llama cuando cambia un valor en el formulario 
    - `redrawingItem`: se llama justo antes de que el formulario se vuelva a dibujar 

## Añadir acciones del lado del servidor

La implementación del botón puede ampliarse fácilmente con una acción del lado del servidor. Etendo soporta el [concepto de action handler](../concepts/etendo-architecture.md#implementing-server-side-actions-callable-from-the-client) para este propósito.

---

Este trabajo es una obra derivada de [How to add a canvas field to a form or grid](http://wiki.openbravo.com/wiki/How_to_add_a_canvas_field_to_a_Form_or_Grid){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, usado bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.