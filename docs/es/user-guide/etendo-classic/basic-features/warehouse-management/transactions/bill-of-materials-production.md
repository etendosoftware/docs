---
title: Producción LDM
tags:
 - Bill of Materials
 - BOM Production
 - Warehouse Management
 - Transactions
---

# Producción LDM { #bill-of-materials-production }

:material-menu: `Aplicación` > `Gestión de Almacén` > `Transacciones` > `Producción LDM`

## Visión general { #overview }

Cree y ejecute procesos de producción utilizando las listas de materiales definidas previamente.

A diferencia de lo que sugiere el nombre, este proceso **no forma parte de la producción**. Esta configuración se utiliza para combinar diferentes productos finales en otro **producto empaquetado**. Por ejemplo, para un ordenador que se envía con diferentes teclados o productos que se envían con diferentes cables de alimentación. No hay una producción real implicada en la creación del nuevo producto.

La configuración de esta pantalla se combina con configuraciones en la pantalla de producto:

- la casilla de verificación de lista de materiales está seleccionada para el producto
- la pestaña de lista de materiales está cumplimentada

## Cabecera { #bom-production }

En esta sección se selecciona la organización, un nombre del empaquetado que se ejecutará, así como una fecha en la que tendrá lugar.

## Plan de producción { #production-plan }

Añada listas de materiales a producir en un plan de producción especificado.

En esta sección, se selecciona el producto y el número que se ejecuta. Además, debe seleccionarse el hueco en el que se almacenará el resultado de la Producción.

Tal y como se indica en la Visión general, el producto que se selecciona debe configurarse correctamente primero:

- la casilla de verificación de lista de materiales está seleccionada
- la pestaña de lista de materiales está cumplimentada con la información de los componentes que se combinan más la cantidad para cada componente
- se ha hecho clic en el botón Verificar LDM para dejar el producto listo para su uso

## Líneas { #io-products }

Cree y edite los productos que se van a utilizar en la producción.

Después de cumplimentar la pestaña Plan de producción, se hace clic en el botón **Crear/Procesar producción** para generar la información en esta sección. En base a la configuración de la información en la pestaña de lista de materiales del producto combinada con la cantidad de producción en la pestaña del plan de producción, se generó la información de los **componentes a utilizar y qué cantidad**.

Después de hacer clic en el botón **Crear/Procesar producción** por segunda vez, se ejecutan los cambios.

En el popup, puede seleccionarse la casilla de verificación 'La cantidad del producto debe estar en stock', de modo que el proceso solo se ejecute si los componentes están en stock. Tras procesarse correctamente, el stock de los componentes disminuye y el stock del producto empaquetado aumenta.

!!! warning
    Actualmente, los procesos implicados en la Producción LDM no admiten stock negativo. Por este motivo, si la casilla de verificación 'La cantidad del producto debe estar en stock' no está seleccionada y no hay suficiente stock de los productos consumidos, se utilizará la cantidad disponible en stock para completar las cantidades en las líneas de la pestaña \[Líneas\].

Existe una verificación denominada **Forzar el uso del almacén del hueco seleccionado.** Cuando está habilitada, se utilizará el mismo Almacén del Hueco seleccionado para obtener el stock que se va a consumir. Si no está habilitada, el proceso tendrá en cuenta todos los Almacenes disponibles para el establecido en la cabecera del Documento.

## Contabilización masiva { #bulk-posting }

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}.

La funcionalidad de Contabilización masiva permite al usuario contabilizar o deshacer la contabilización de múltiples registros seleccionando los registros correspondientes y haciendo clic en el botón **Contabilización masiva**.

Además, el Estado contable del/de los registro/s se muestra en la barra de estado, en la vista de formulario, o en una columna, en la vista de cuadrícula.

!!! info
    Para más información, visite [la guía de usuario del módulo Bulk Posting](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).
