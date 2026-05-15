---
title: Configuraciones de Rappels
tags:
  - Master Data Management
  - Etendo Classic
  - Business Partner
  - Discount
  - Sales Extensions
---

## Configuraciones de Rappels { #rappel-configurations }

:material-menu: `Aplicación` > `Gestión de Datos Maestros` > `Configuración de terceros` > `Configuraciones de Rappels`

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el módulo Advanced Rappels del bundle Sales Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Sales Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=22CF01FC620140A6AA92CF550EB8DA36){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Sales Extensions - Notas de la versión](../../../../../whats-new/release-notes/etendo-classic/bundles/sales-extensions/release-notes.md).

Los rappels son descuentos basados en el volumen de consumo de un tercero en un periodo de tiempo determinado. Esta funcionalidad permite al usuario configurar y conceder rappels a terceros.

### Requisitos { #requirements }

Antes de que el usuario pueda utilizar esta funcionalidad, es necesario configurar una nueva secuencia de documento y un nuevo tipo de documento que se utilizarán para los Rappels.

#### Secuencia de documento { #document-sequence }

Es necesaria una secuencia de documento específica para los rappels para distinguirlos de otras transacciones.
En esta ventana, cree un nuevo registro y complete los campos correspondientes:

- **Organización**: El nombre de la organización correspondiente.
- **Nombre**: El nombre de la secuencia de documento, en este caso, "Secuencia de rappel"
- **Activo**: Sí
- **Numeración automática**: Sí
- **Incrementar**: 1
- **Valor actual**: 1,000,000
- **Prefijo**: Es opcional y, en este caso, se introduce "RAP-" para indicar que estas transacciones son Rappels.

Guarde el registro y la secuencia de documento para rappels estará disponible.

![document_sequence_new.png](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/business-partner-setup/rappel-configurations/rappel-configurations-1.png)

!!! info
    Para más información, visite [Secuencia de documento (numeración)](../../financial-management/accounting/setup/document-sequence.md)

#### Tipo de documento { #document-type }

Es necesario un tipo de documento específico para los rappels.
En esta ventana, cree un nuevo registro y complete los campos correspondientes:

- **Organización**: El nombre de la organización correspondiente
- **Nombre**: El nombre del tipo de documento, en este caso, "Rappel"
- **Categoría de LM**: En este caso, seleccione "Factura de clientes"
- **Etiqueta de impresión**: En este caso, "Rappel"
- **Tipo doc. base**: "Factura de clientes"
- **Doc.numéricamente controlado**: Sí
- **Secuencia de documento (numeración)**: En este caso, "Secuencia de rappel"
- **Tabla**: C_invoice
- **Operación de venta**: Sí
- **Es rappel**: Sí

Guarde el registro y el tipo de documento para rappels estará disponible.
Después de guardarlo, es necesario seleccionar "rappel" en el campo "Documento cancelado" y guardar de nuevo.

![document_type_new.png](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/business-partner-setup/rappel-configurations/rappel-configurations-2.png)


!!! warning
    Para cada organización, es posible configurar únicamente un tipo de documento "rappel".

!!! info
    Para más información, visite [Tipo de documento](../../financial-management/accounting/setup/document-type.md)

### Configuraciones de Rappels { #rappel-configurations_1 }

En esta ventana, el usuario puede configurar todos los aspectos necesarios para conceder rappels a determinados terceros.

![rappel_configuration_window_new.png](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/business-partner-setup/rappel-configurations/rappel-configurations-3.png)

#### Cabecera { #header }

Esta ventana contiene los datos generales de la configuración. Los campos relevantes se describen a continuación:

- **Nombre**: Indica el nombre asignado al rappel.
- **Moneda**: El usuario puede seleccionar la moneda del rappel.
- **Incluir productos**: El usuario puede definir si los productos seleccionados se incluyen o se excluyen ("todos excepto los definidos" o "solo los definidos").
- **Incluir categorías de producto**: El usuario puede definir si las categorías de producto seleccionadas se incluyen o se excluyen ("todos excepto los definidos" o "solo los definidos").
- **Incluir marcas**: El usuario puede seleccionar determinadas marcas para incluirlas o excluirlas ("todos excepto los definidos" o "solo los definidos").
- **Incluir ubicaciones**: El usuario puede seleccionar determinadas ubicaciones para incluirlas o excluirlas ("todos excepto los definidos" o "solo los definidos").
- **Almacén**: Proporciona información sobre el almacén de los productos. Por defecto, este campo está vacío. Esto ocurre salvo para facturas creadas a partir de albaranes.
- **Periodicidad**: Proporciona información sobre la periodicidad sugerida del rappel ("anual", "semestral", "mensual" o "trimestral").
- **Tipo de rappel**: El usuario puede seleccionar el tipo de rappel; puede ser según el importe del consumo o la cantidad de productos consumidos ("importe" o "cantidad").

Una vez completada esta información, el usuario puede guardar la configuración y utilizar los botones de la ventana para configurar aspectos específicos de cada rappel.

#### Botones { #buttons }

En la parte superior de esta ventana se pueden encontrar cuatro botones diferentes.

- **Añadir Categorías de Productos**: Con este botón, el usuario puede seleccionar una o más categorías de producto y añadirlas al rappel.
- **Añadir Productos**: Con este botón, el usuario puede añadir uno o más productos al rappel.
- **Añadir terceros**: Con este botón, el usuario puede añadir uno o más terceros al rappel, y se debe asignar una fecha desde y una fecha hasta para determinar el periodo de validez del rappel creado.
- **Copiar rappel**: Con este botón, el usuario puede copiar las características de un rappel existente al rappel seleccionado.

#### Solapa { #tabs }

- **Categoría del producto**: En esta solapa se muestran las categorías de producto asignadas al Rappel. También es posible asignar nuevas categorías desde esta solapa.
- **Producto**: En esta solapa se muestran los productos asignados al Rappel. También es posible asignar nuevos productos desde esta solapa.
- **Parámetros de rappel**: En esta solapa se puede asignar al rappel el porcentaje de descuento y los importes mínimo y máximo.
- **Terceros**: En esta solapa se muestra el tercero al que aplica el Rappel. Aquí es posible seleccionar la "fecha desde" y la "fecha hasta". Esta solapa también contiene una subsolapa llamada "Ubicación de terceros", donde se indica la ubicación del tercero.
- **Marca**: En esta solapa se pueden seleccionar las marcas de los productos a los que aplica (o no) el Rappel.

Recuerde que las opciones seleccionadas en las solapas "Categoría del producto", "Producto" y "Marca" deben seguir una lógica determinada: la prioridad es la opción seleccionada en la solapa "Categoría del producto". Esto significa que los filtros más específicos aplican sobre las categorías de producto incluidas o excluidas.

Al seleccionar la opción "solo los definidos" en los campos "incluir categorías de producto" e "incluir productos" de la cabecera, si en la solapa "categoría del producto" el usuario selecciona "agua", y en la solapa "producto" el usuario selecciona "vino blanco", el rappel solo incluirá los productos pertenecientes a la categoría "agua" y no "vino blanco".
>
!!! warning
    Al seleccionar la opción "todos excepto los definidos" en el campo "Incluir categorías de producto" y la opción "solo los definidos" en el campo "incluir productos", si en la solapa "categoría del producto" el usuario selecciona "agua", y en la solapa "producto" el usuario selecciona "agua con gas", el rappel no incluirá el producto "agua con gas" a pesar de lo definido en la solapa "producto", ya que la prioridad está en la "categoría del producto" definida.

---

Este trabajo es una obra derivada de [Gestión de Datos Maestros](https://wiki.openbravo.com/wiki/Master_Data_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.
