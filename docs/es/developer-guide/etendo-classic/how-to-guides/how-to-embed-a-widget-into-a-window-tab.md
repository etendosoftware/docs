---
tags:
  - How to
  - Etendo Classic
  - Widget
  - Tab
---

#  Cómo incrustar un widget en una solapa de ventana

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_embed_a_Widget_into_a_Window_Tab-0.png) 
Este documento sigue siendo un trabajo en curso. Puede contener imprecisiones o errores.   

##  Introducción

Este procedimiento asume familiaridad tanto con el funcionamiento de ventanas, solapas y campos como con la definición de widgets en general.
  
Este procedimiento describe cómo incrustar un widget en una solapa de una ventana generada. En detalle, mostrará las restricciones/diferencias en la propia definición del widget y explica los dos ejemplos siguientes:

  1. Cómo incrustar un widget simple en una solapa.
  2. Cómo incrustar un widget QueryList en una solapa que filtra sus datos según el registro mostrado actualmente.

##  Cómo colocar un widget en una solapa

En esta parte definiremos dos widgets sencillos y los colocaremos en una ventana/solapa generada.

El objetivo de esta sección es mostrar cómo definir una ventana/solapa generada que se vea como en la siguiente captura de pantalla.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_embed_a_Widget_into_a_Window_Tab-2.png)

Widget incrustado en una solapa

En este ejemplo, un widget se coloca junto a algunos campos normales en una solapa de demostración. Este widget ocupa una sola columna pero cuatro filas en la parte superior derecha y no tiene etiqueta de campo (para usar el espacio adicional de la etiqueta para el propio contenido). El contenido del widget muestra entradas de Twitter que incluyen el texto "Openbravo".

El resto de esta sección asume que se realicen las siguientes acciones:

  * Creación de una tabla.
  * Creación de una ventana y solapa para mostrar esta tabla.

A continuación, se centra en cómo añadir los dos widgets en las posiciones mostradas arriba en esta solapa. Esto constará de cuatro pasos básicos para cada uno de los widgets:

  1. Definir el propio widget.
  2. Definir una nueva entrada de referencia para usar el widget.
  3. Añadir una nueva columna y campo a la tabla y solapa.
  4. Configurar el nuevo campo para que coincida con el diseño mostrado arriba.

El tercer paso utiliza el mismo flujo que añadir cualquier otro campo y se describe en detalle en estos otros dos documentos.

El primer paso es crear una nueva definición de widget que mostrará el contenido de Twitter que coincida con 'Openbravo'. Este widget reutilizará el código del widget de Twitter ya definido e incluido con la distribución de Openbravo 3.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_embed_a_Widget_into_a_Window_Tab-4.png)

Definición del widget de Twitter

Un detalle importante en esta definición es que el parámetro se define como **Fija** ya que, para los widgets incrustados en una ventana/solapa, no existen instancias de widget como se describe aquí.

El siguiente paso es definir una referencia que pueda usarse en la columna para el widget.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_embed_a_Widget_into_a_Window_Tab-6.png)

Definición de referencia para el widget de Twitter

Los detalles importantes en esta definición son:

  * En la solapa de referencia: _Referencia padre_ = **OBKMO_Widget in Form Reference**
  * En la solapa 'Widget in Form': desmarcar _Widget Class' & unmark_ _Show Field Title_ _para usar el espacio adicional disponible para el propio contenido del widget._

El último paso para este widget es añadir una columna CHAR(1) a la tabla y un nuevo campo a la solapa de demostración. La columna debe definirse según los siguientes detalles:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_embed_a_Widget_into_a_Window_Tab-8.png)

Definición de columna para el widget de Twitter

El último paso es añadir un campo de formulario a la solapa y configurar este campo de formulario con los detalles de UI deseados, que consisten en:

  * Sequence No: para el orden habitual de los campos.
  * Colspan: para definir cuántas columnas debe ocupar el campo/widget.
  * Rowspan: para definir cuántas filas debe ocupar el campo/widget.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_embed_a_Widget_into_a_Window_Tab-10.png)

Definición de campo para el widget de Twitter

##  Cómo vincular un widget al registro actual

El objetivo de esta sección es crear un widget QueryList similar al widget existente _Factura a cobrar_ disponible para su colocación en el espacio de trabajo, que muestra datos para todos los terceros.

Para ver los cambios realizados en el widget, es necesario refrescar todo el espacio de trabajo, no solo la solapa. Esto puede hacerse en la solapa Espacio de trabajo - Gestionar espacio de trabajo - Refrescar

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_embed_a_Widget_into_a_Window_Tab-14.png)

Factura a cobrar en el espacio de trabajo

El widget que se va a crear aquí debería mostrarse en su lugar en la ventana Terceros y mostrar únicamente los datos del registro mostrado actualmente.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_embed_a_Widget_into_a_Window_Tab-16.png)

Factura a cobrar en la ventana Terceros

En comparación con el widget original _Facturas a cobrar_, deben realizarse los siguientes cambios:

  1. Eliminación de la columna _Terceros_, ya que el nuevo widget debe filtrarse por el tercero actual.
  2. Eliminación de la definición de parámetro editable por el usuario.
  3. Adición de un nuevo parámetro con nombre **businessPartnerID** que se vincule al registro actual.
  4. Cambios en la consulta HQL para ajustarla a los dos últimos cambios listados aquí.

A continuación se muestra la HQL modificada en detalle. Al examinar la HQL para el parámetro con nombre recién añadido, puede verse que la definición del parámetro con nombre es idéntica a la de un parámetro con nombre "normal", como se usaría para un valor editable por el usuario.

```
  SELECT
    inv.id AS invoiceId,
    inv.documentNo AS documentNo,
    inv.businessPartner.id AS businessPartnerId,
    inv.businessPartner.name AS businessPartnerName,
    inv.invoiceDate AS invoiceDate,
    inv.grandTotalAmount AS grandTotalAmount,
    inv.currency.iSOCode AS currency,
    inv.paymentTerms.name AS paymentTerms,
    inv.outstandingAmount AS outstandingAmount,
    inv.daysTillDue AS daysTillDue,
    inv.dueAmount AS dueAmount,
    inv.organization.name AS organizationName
  FROM
    Invoice AS inv
  WHERE
    inv.businessPartner.id = :businessPartnerID
  AND inv.processed = true
  AND inv.paymentComplete = false
  AND inv.salesTransaction = true
  AND inv.client.id = :client
  AND inv.organization.id IN (:organizationList)
  AND @optional_filters@
  ORDER BY
    inv.invoiceDate
```

La última e interesante diferencia está en la definición del nuevo parámetro **businessPartnerID**, de modo que tome automáticamente el valor de _id_ del registro mostrado actualmente.

Para lograrlo, debe crearse una nueva entrada de parámetro con los siguientes detalles:

  * _Nombre columna BD_ = _businessPartnerID_ coincidiendo con el parámetro con nombre en la consulta.
  * _Fija_ = sin marcar.
  * _Lógica del valor por defecto_ = ${formValues.id} para referirse a la propiedad _id_ del registro mostrado actualmente.

Esta definición dinámica de parámetros y las reglas de nomenclatura para las propiedades se explican con más detalle en esta sección de la documentación de Widgets.

Copiar la definición del widget _Facturas a cobrar_ y realizar los ajustes descritos arriba dará lugar a una definición de parámetro como se ve en la siguiente imagen:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_embed_a_Widget_into_a_Window_Tab-18.png)

Definición de parámetro del widget de facturas

La colocación de esta definición de widget en la definición de terceros funciona exactamente como se describe en la sección anterior siguiendo sus pasos de:

  * Definir una nueva referencia para el widget.
  * Añadir una nueva columna usando esta referencia.
  * Añadir un nuevo campo usando esta columna + configurar su diseño.

Con esto concluye este procedimiento, que colocó la información sobre facturas cobrables del tercero actual directamente en la vista de un usuario que está consultando la solapa de Terceros.

---

Este trabajo es una obra derivada de [Cómo incrustar un widget en una solapa de ventana](http://wiki.openbravo.com/wiki/How_to_embed_a_Widget_into_a_Window_Tab){target="\_blank"} de [Wiki de Openbravo](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.