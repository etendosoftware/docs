---
title: How to add a canvas field to a Form or Grid
tags:
  - How to
  - Canvas Field
  - Form Customization
  - Grid Customization
  - JavaScript Development
  - UI Components
  - JavaScripts Events
---

#  How to add a canvas field to a Form or Grid

## Overview

This guide explains how to integrate canvas fields into forms and grids within Etendo, enabling the addition of customized visual components such as buttons, links, and calculated labels. 
Canvas fields offer dynamic data presentation and interaction, leveraging JavaScript development expertise for implementation.

##  Introduction

A canvas field allows the user to add any visual component to a form or a row in a grid. 
This concept can be used to add a calculated field to a form and grid. 
Visual components which can be added are for example buttons, links and (computed) labels.

In this section, we will be adding a button and a calculated field to the form and to every row in the grid.
We will illustrate how information from the record and form can be used to get dynamic information from the Form/Grid.

The implementation of canvas fields requires javascript development experience. 
See the following concept pages for background information on javascript development:

  * [Client Side Development and API](../concepts/Client_Side_Development_and_API.md)
  * [JavaScript Coding Conventions](../concepts/JavaScript_Coding_Conventions.md) 

It also makes sense to study the following page: [Etendo Architecture](../concepts/Etendo_Architecture.md).

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_add_a_canvas_field_to_a_Form_or_Grid-0.png)

##  Example Module

This section is supported by an example module which shows examples of the code shown and discussed.

The code of the example module can be downloaded from this repository: [com.etendoerp.client.application.examples](https://github.com/etendosoftware/com.etendoerp.client.application.examples)

##  Main development steps for creating a new canvas field

The development consists of 2 steps:

  1. Implement the canvas itself, normally this is done in javascript. 
  2. Specify the canvas javascript class in the field definition of the tab/window 

###  Implementing your canvas in javascript

The first step is to implement your canvas class in javascript. This is done in 2 steps:

  * Create a  [javascript](../concepts/Client_Side_Development_and_API.md#adding-javascript-to-etendo) file with your javascript class and place it in the correct directory, the convention is to place js files in the following directory in your module: web/[module.java.package]/js 
  * Register the javascript file (and other static resources such as css files) in Etendo using a [ComponentProvider](../concepts/Etendo_Architecture.md#component-provider) 

The example module implements a button and a calculated field in the `example-canvas-field.js` file.

The first example in the file implements a button which shows the identifier of the current record:

    
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

The second example shows a calculated field which divides 2 values from the current record and displays the result in a formatted way. 
It also illustrates several methods which are called when the context/environment changes (for example when a value on the form changes):

    
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

The javascript file is registered in the example modules' [ComponentProvider](../concepts/Etendo_Architecture/#component-provider) like this:

    
```java title="ExampleComponentProvider.java"
@Override
public List<ComponentResource> getGlobalComponentResources() {
  final List<ComponentResource> globalResources = new ArrayList<ComponentResource>();
  globalResources.add(createStaticResource(
      "web/org.openbravo.client.application.examples/js/example-canvas-field.js", false));
.....
```

###  Defining the canvas in the Tab-Field (ADField)

The next step is to create a new field in the tab, and set its client class field:  

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_add_a_canvas_field_to_a_Form_or_Grid-1.png)

It is also possible to add in-line properties in the `"Clientclass"` field, for example, 'OBEXAPP_SalesOrderActionButton {"title": "My Action Button"}'

###  The result

The result is shown in both the grid and the form:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_add_a_canvas_field_to_a_Form_or_Grid-2.png)

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_add_a_canvas_field_to_a_Form_or_Grid-3.png)

##  Javascript events passed to the canvas

When implementing your canvas, you should take into account that the canvas is used in 3 different situations:

  * When displaying a row in the grid 
  * When editing a row in the grid 
  * In form view, when editing a record 

The last 2 cases are similar.

In grid-display mode the following applies:

  * In grid mode the following properties are set on the canvas: 
    * `grid`: the grid object 
    * `rowNum`: the row number/record index for which the canvas is used 
    * `record`: the record for which the canvas is used 
    * `colNum`: the column in which the canvas is shown 
    * `field`: the field where the canvas is used 
  * A canvas can be created and pooled, so over time it is created once and re-used when records are scrolled into view. 
  When a canvas is used for a record, then the setRecord method on it is called (if the canvas has this method). 

In form-edit or grid-edit mode, the following applies:

  * The canvasItem property will be set pointing to the form item the canvasItem can be used to get to the form itself and to the grid (if editing in the grid): 
    * `this.canvasItem.form`: the form instance 
    * `this.canvasItem.form.grid`: in case of grid editing 
  * If the canvas has a property noTitle with the value `true` then in form mode no title/label is displayed 
  * Form changes: the canvas can capture form/value change events by implementing 2 methods (both without arguments): 
    * `onItemChanged`: is called when a value on the form changes 
    * `redrawingItem`: is called just before the form is redrawn 

##  Adding server side actions

The button implementation can easily be extended with a server side action. Etendo Classic supports the [action handler concept](../concepts/Etendo_Architecture.md#actionhandler-server-side-calling-from-the-client)  for this purpose.

---

This work is a derivative of ["How to add a canvas field to a form or grid"](http://wiki.openbravo.com/wiki/How_to_add_a_canvas_field_to_a_Form_or_Grid){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}. 