---
title: Gestión Financiera
---

## Visión general

La documentación funcional de Gestión Financiera proporciona una descripción detallada de todas las ventanas del área de aplicación de Gestión Financiera.

## Plan de pago de facturas de compra

:material-menu: `Aplicación` > `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Transacciones` > `Plan de pago de facturas de compra`

### Visión general

La ventana Plan de pago de facturas de compra muestra todos los planes de pago de facturas de compra que no están totalmente pagados.

Esta ventana ofrece otra posibilidad de gestionar la misma información que se encuentra en la solapa Plan de pagos de la ventana Factura de compra para una factura determinada.

La ventaja de esta ventana es que ofrece una vista más inmediata de todos los planes de pago de facturas de compra que todavía tienen un Importe Pendiente por pagar.

#### Plan de pagos

La información del plan de pago de facturas de compra se muestra agrupada en dos secciones.

La sección **Factura** muestra la información detallada a continuación:

- **Factura**. Hay un enlace a la Factura de compra.
- **Nº documento**. Este es el número de documento de la Factura.
- **Terceros**. Este es el tercero contra el que se emite la Factura.
- **Fecha de la factura**. Esta es la fecha de creación de la Factura.
- **Importe total**. Este es el importe total de la Factura.
- **Importe Pendiente**. Este es el importe pendiente de este Plan de pagos.
- **Moneda**. Esta es la moneda de la Factura.

La sección **Plan de pagos** muestra la información detallada a continuación:

- **Método de pago**. Este es el método de pago de la factura de compra.
- **Fecha de vencimiento**. Esta es la "Fecha de vencimiento" original acordada con el Proveedor. Esta fecha se utiliza como la "Fecha de Referencia" en algunos informes financieros.
- **Fecha esperada**. Esta es la fecha en la que se espera que se realice el pago. Cuando se crea el Plan de pagos, esta fecha es la misma que la "Fecha de vencimiento", pero puede modificarse posteriormente.  
  Esta fecha refleja una revisión del Plan de pagos original en la que la "Fecha de vencimiento" ha cambiado.  
  Esta fecha se utiliza como la "Fecha de Referencia" en algunos informes, como el informe de pagos.

!!! info
    Este campo es el único que se puede modificar en esta ventana. Si se modifica, ese cambio también se reflejará en la solapa del plan de pagos de la correspondiente factura de compra.

- **Días Retraso**. Este es el número de días desde la fecha esperada hasta el día actual.
## Pago

:material-menu: `Aplicación` > `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Transacciones` > `Pago`

### Visión general

Los pagos y anticipos a proveedores se pueden realizar y gestionar en la ventana de pago. Los pagos de conceptos contables no relacionados con pedidos/facturas también se pueden gestionar en esta ventana.

Los pagos se pueden realizar contra diferentes tipos de documentos:

- Pedidos de compra; en la práctica, esto es un _anticipo_.  
  Posteriormente, cuando se crea una factura a partir del pedido que ya tiene un pago recibido asociado, la factura hereda automáticamente el pago recibido del pedido.
- Facturas de compra; en la práctica, esto es el pago de una factura de proveedor.  
  Los pagos anteriores a la fecha contable de la factura también se consideran un _anticipo_.
- Y Conceptos contables; en la práctica, esto es el pago de cualquier otro gasto a un proveedor, por ejemplo una multa u otros tipos de comisión no incluidos en una factura.  
  Este tipo de pagos se puede crear en esta ventana añadiendo el Concepto contable correspondiente, así como el importe de "Pagado", o se puede completar automáticamente como un concepto contable si se crea como un pago de Concepto contable en Asientos manuales.  
  Independientemente de cómo se creen, ambos casos se gestionan de la misma manera en función del Método de pago utilizado.

Los pagos se pueden crear **para pagar a** un **único proveedor** o **para pagar a** varios **proveedores** al mismo tiempo.

Al final del proceso, una transacción de "**Pago**" implicará la creación de una transacción de "**Reintegro**" en la Cuenta financiera correspondiente.

La creación de la transacción de reintegro en la cuenta financiera se puede realizar:

- manualmente utilizando el proceso Añadir transacción de la cuenta financiera.
- o automáticamente, si el método de pago utilizado está configurado para ello, lo que implica seleccionar la casilla "Reintegro automático".

### Cabecera

La ventana Pago permite al usuario realizar y gestionar pagos a proveedores para liquidar diferentes tipos de documentos, como pedidos y facturas. Esta ventana también permite al usuario gestionar los pagos a proveedores ya realizados en la ventana de factura de compra, del mismo modo que los pagos de conceptos contables realizados en Asientos manuales.

![](../../../../../assets/drive/1Ie6b5QE33TRiAtdGr4PGVCtT5VvH0nD8.png)

Solo hay unos pocos campos obligatorios que completar al realizar un pago en esta ventana:

- la **Organización** que paga
- el **Número de pago**, que sigue la secuencia de documento correspondiente.
- el **Método de pago** que se va a utilizar para realizar el pago. Existe una casilla en la ventana "Añadir pago" que posteriormente permite seleccionar documentos vinculados a métodos de pago alternativos
- y la **Cuenta financiera** desde la que se va a retirar el dinero en el campo "**Depositar en**".

Otros campos relevantes a tener en cuenta son:

- Campo **Pago a**, es decir, el proveedor al que se le realiza el pago; no es necesario introducirlo al crear un nuevo registro.
  - Si no se selecciona un proveedor, implica la creación de un pago para pagar diferentes documentos de distintos proveedores.
  - Si se selecciona un proveedor, implica la creación de un pago para pagar diferentes documentos del mismo proveedor. En este caso, el valor de los campos "Método de pago" y "Depositar en" cambia si el proveedor tiene asignado un método de pago y una cuenta financiera específicos para utilizar al pagar sus facturas.
- **Nº de referencia**, este campo se utiliza para reflejar el número asociado al pago en el sistema de documentación del proveedor, si existe.
- **Moneda**. Es posible seleccionar una moneda diferente a la moneda de la cuenta financiera al realizar un pago. Para ello, el método de pago utilizado y asignado a la cuenta financiera del pago debe estar configurado para permitir pagos en múltiples monedas.

#### Ventana Añadir pago

El botón **Añadir Detalles de Pago** abre la ventana **Añadir pago**, donde se pueden seleccionar los documentos pendientes de pago.

![](../../../../../assets/drive/1tsg4HMq519UXdo9UqGhV9-wOpqMPJRpy.png)

La ventana **Añadir pago** ya se explica en el artículo de pago de factura de compra.

#### Pago de varios tipos de documento de diferentes proveedores

Si no se ha seleccionado ningún proveedor en el campo "Pago a", es posible pagar diferentes tipos de transacción de distintos proveedores simplemente seleccionándolos.

!!! info
    Etendo permite al usuario filtrar una vez más por un tercero determinado si no se introdujo en el campo "Pago a" por error.

El campo "Pago real" mostrará entonces el valor sumado de todas las transacciones seleccionadas para pagar.

![](../../../../../assets/drive/136-nlDAc31ndG9ibEJoUZk2oUgdZJNcS.png)

Una vez procesado el pago, la solapa Líneas lista todos los pedidos y facturas e incluso conceptos contables incluidos en el pago, al igual que el campo "**Descripción**" de la cabecera del pago.

#### Reactivar un pago

Un pago ya procesado con estado "Pago realizado" o "Pendiente de ejecución" puede ser **Reactivado**. Esta opción permite a los usuarios editar datos de pago incorrectos o eliminar un pago creado erróneamente.

El botón "Reactivar" permite al usuario hacer lo explicado anteriormente, ya que se pueden seleccionar dos acciones diferentes:

- **Reactivar**: esta opción reactiva el pago, manteniendo las líneas de pago.  
  Una vez reactivado el pago, el usuario puede modificar fácilmente la información del pago utilizando el botón "Añadir Detalles de Pago" y procesarlo de nuevo.
- **Reactivar y eliminar líneas**: esta opción reactiva el pago y elimina todas las líneas de pago.  
  Esta opción es la que se debe utilizar si el pago se creó erróneamente y, por tanto, debe eliminarse completamente.  
  Una vez reactivado el pago, el usuario puede eliminar la cabecera del pago sin necesidad de eliminar primero las líneas de pago.

Un pago ya procesado y retirado con estado "Retirado no conciliado" también puede ser "**Reactivado**" como se ha descrito anteriormente, pero una vez que la transacción de reintegro correspondiente se haya eliminado de la cuenta financiera.

#### Contabilizar un pago

Un pago realizado y procesado desde la ventana Pago puede contabilizarse si el método de pago utilizado al crear el pago permite al usuario hacerlo una vez asignado a la cuenta financiera a través de la cual se realiza el pago. Si no es así, Etendo muestra un aviso: "Documento deshabilitado para contabilidad".

Un pago contabilizado tiene el siguiente aspecto:

|                                                           |                |                |
| --------------------------------------------------------- | -------------- | -------------- |
| Cuenta                                                   | Débito         | Crédito        |
| Pasivo del proveedor                                     | Importe de pago |                |
| Al pagar usar la "Cuenta de pagos en tránsito" (salida)   |                | Importe de pago |

#### Anular un pago

Un pago ya procesado con estado "Pendiente de ejecución" puede ser "**Anulado**". El botón de proceso "Reactivar" permite al usuario hacerlo, pero solo para pagos en estado "Pendiente de ejecución".

!!! info
    _Recuerde que un pago puede obtener el estado pendiente de ejecución si el método de pago utilizado y asignado a la cuenta financiera está configurado para tener un "Tipo de Ejecución" automático y además está seleccionada la casilla "En espera"._

La acción de anulación establece la(s) línea(s) de pago como "**Cancelado**", lo que significa que el documento (pedido o factura) en realidad no está pagado y, por tanto, se puede crear o añadir un nuevo pago.

#### Pagos con crédito

El campo "**Crédito generado**", que se puede encontrar en la cabecera de "Pago", permite al usuario generar crédito (o un pago con crédito en términos de Etendo) para un tercero simplemente introduciendo el importe del crédito en ese campo.

No es posible generar crédito en un pago que no esté relacionado con un único proveedor o acreedor; por lo tanto, la funcionalidad de crédito generado requiere que el usuario seleccione un tercero en el campo "Pago a".

La creación de un pago con crédito requiere no seleccionar ningún documento a pagar en la **ventana "Añadir pago"** que se muestra después de pulsar el botón de proceso "**Añadir Detalles de Pago**", sino dejar el importe del crédito para utilizarlo más adelante.

![](../../../../../assets/drive/1J2H_kxh0hRWO5fHEllfFKXZ1oTDQFqPn.png)

Se crea un pago con crédito tras el procesado. Este pago con crédito especifica el importe dejado como crédito en el campo "Descripción" de la cabecera del pago con crédito.

Posteriormente, el crédito disponible generado para ese proveedor se puede utilizar para pagar al proveedor:

- en la ventana "**Añadir pago**" una vez que se crea un nuevo Pago para ese proveedor, simplemente seleccionando el crédito en la sección "Crédito a utilizar".

![](../../../../../assets/drive/18mZnJqpLFZa55nXSpoC-qSAFbS1TKg5l.png)

- o en la ventana "**Seleccionar pagos con crédito**", que se muestra **automáticamente** al completar una nueva factura de proveedor.

!!! info
    En ambos casos, el campo "Descripción" de la cabecera del pago con crédito también especificará las transacciones/documentos donde se utilizó el crédito.

La solapa Origen del crédito usado de la ventana de pago muestra el pago con crédito utilizado para pagar un documento de proveedor (pedido, factura o concepto contable).

#### Pagos en múltiples monedas

Etendo permite al usuario realizar pagos en una moneda diferente a la moneda de la cuenta financiera.

Para utilizar esta opción, el método de pago asignado a la cuenta financiera utilizada para realizar el pago debe estar configurado para permitirlo, lo que implica seleccionar la casilla "Permitir pagos en otras divisas".

#### Anticipos que exceden el importe de la factura a pagar

Etendo permite anticipar añadiendo pagos a los pedidos. La factura de compra creada a partir del pedido heredará el pago realizado para el pedido.

Cuando el importe real anticipado excede el importe de la factura a pagar, la factura de compra permanece como **"Pagado" = "No"** hasta que

- o bien se crea un pago negativo para reflejar que el proveedor devuelve a la organización la diferencia, de modo que el saldo final del pago sea igual al importe de la factura de compra
- o bien se crea un pago con crédito para utilizarlo posteriormente al pagar otra factura al mismo proveedor.  
  Este pago con crédito debe crearse como un nuevo pago relacionado con la factura de compra anticipada; de ese modo, la factura anticipada queda como **"Pagado" = "Sí"**.

### Líneas

La solapa Líneas contiene una lista de los documentos a pagar o ya pagados por el pago.

#### Historial de Ejecuciones

La solapa Historial de Ejecuciones muestra información sobre el historial de intentos de ejecución del pago.

Para algunos tipos de pago, se necesitan algunos pasos adicionales. Por ejemplo, un pago con un cheque que debe completarse con un número de cheque.

En ese caso, el método de pago vinculado al pago debe configurarse para requerir un proceso de **Tipo de Ejecución** "Automático".

Todo lo anterior implica un paso adicional en la ventana Pago, que es ejecutar el pago utilizando el botón de proceso "**Ejecutar Pago**".

Este botón de proceso solo se muestra en el caso de pagos vinculados a un proceso de ejecución automatizada para el cual está seleccionada la casilla "**En espera**".

Si la casilla "En espera" no está seleccionada, el paso adicional sigue siendo necesario, pero se ejecutará automáticamente sin ninguna acción del usuario final.

La solapa Historial de Ejecuciones es de solo lectura y muestra información sobre la ejecución del pago, como la fecha de ejecución, una vez que el pago ha sido ejecutado.

![](../../../../../assets/drive/1o3dY5UJs0fh3LC5ry7249VZ2DZGwE3BQ.png)

#### Tipos de cambio

La solapa Tipos de cambio permite al usuario introducir un tipo de cambio entre la moneda del libro mayor de la organización y la moneda del pago realizado, para utilizarlo al contabilizar el pago en el libro mayor.

#### Origen del crédito usado

Un pago con crédito se puede utilizar para liquidar el pago de más de un documento. Esta tabla registra los documentos en los que se ha utilizado un pago con crédito.

La creación de un pago de "Crédito" ya se explica en la sección Pagos con crédito de este artículo, al igual que cómo un pago de "Crédito" o el crédito disponible se puede utilizar posteriormente para pagar a un proveedor.

Esta solapa de solo lectura muestra el pago con crédito utilizado para pagar un documento de proveedor (pedido, factura o concepto contable).

![](../../../../../assets/drive/1ZRyS-NTJD17sB_CAQbG9-XYa1-a0N3fq.png)

### Eliminación de pagos

El objetivo de esta funcionalidad es eliminar y reactivar pagos de forma ágil y sencilla. Además, permite eliminar y reactivar transacciones bancarias y conciliaciones.

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

Desde esta ventana, es posible eliminar pagos seleccionando el registro correspondiente y haciendo clic en el botón Eliminar pago.  
Por otro lado, es posible reactivar pagos desde la misma ventana con el botón "Reactivación avanzada". Esta funcionalidad permite al usuario reactivar el pago sin eliminar manualmente sus transacciones asociadas, lo cual es necesario si se utiliza el botón estándar "Reactivar". Esto devolverá el pago al estado “Pendiente de pago” y se podrán añadir nuevos detalles del pago.

En ambos casos:

- Si el pago está incluido en la cuenta financiera, es decir, si está en estado Depositado/Retirado no conciliado, la transacción en ella también se eliminará (ventana Cuenta financiera > solapa Transacción).

- Si el pago está conciliado mediante un método automático, entonces, además de la transacción en la cuenta financiera, se eliminará la línea del extracto bancario a la que estaba vinculada (ventana Cuenta financiera > Extractos bancarios importados) y la línea correspondiente de la conciliación bancaria (Cuenta financiera > solapa Reconciliaciones).

!!! info
    Si el pago está contabilizado, se eliminará el asiento contable.

![](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions/PRpic6.png)

### Contabilización masiva

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

La funcionalidad de Contabilización masiva permite al usuario contabilizar o descontabilizar múltiples registros seleccionando los registros correspondientes y haciendo clic en el botón **Contabilización masiva**.

Además, el Estado contable del/de los registro(s) se muestra en la barra de estado, en vista de formulario, o en una columna, en vista de rejilla.

!!! info
    Para más información, visite la [guía de usuario del módulo Bulk Posting](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).

### Liquidación avanzada de terceros

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

  
Desde la ventana **Pago**, es posible crear una liquidación haciendo clic en el botón **Añadir Detalles de Pago**.  
En la ventana emergente, Etendo muestra una lista de facturas a liquidar, cada una con su número de factura correspondiente; aquí el usuario puede seleccionar la factura o facturas correspondientes a compensar. Se establece el **Importe real del pago** a pagar; a continuación, seleccione la(s) factura(s) para crear una liquidación y defina el importe correspondiente a pagar de la/cada factura.

![](../../../../../assets/drive/1VXTbJvoG4le_x7dTVC9lqV3puMIqwh-N.png)

Desde la solapa **Factura desde compensación**, seleccione la(s) factura(s) de venta que se utilizarán para pagar y establezca el importe necesario de la(s) factura(s) a compensar.

Debajo de eso, en la solapa **Total**, Etendo muestra los importes totales de referencia a compensar.

![](../../../../../assets/drive/1T-gLPqseFzIa5If1LX93VlhdYIaOz4-5.png)

Tras hacer clic en el botón Hecho, el sistema compensa las facturas y créditos del tercero correspondiente y crea un registro de liquidación.

![](../../../../../assets/drive/11XJzDLx3VkjhY3Q57pxpyrOGdvrRbXXz.png)

El registro de liquidación se registra en la ventana **Liquidación de terceros**, donde se mostrarán las líneas de las facturas (venta y compra) utilizadas para compensar.

![](../../../../../assets/drive/1LQMshrKSSifD2OpQ0Yjmfc3jPfxYQ2S3.png)

!!! info
    Para más información, visite la [Liquidación de terceros - Guía de usuario](../../../optional-features/bundles/financial-extensions/business-partner-settlement.md).
  
### Gestión avanzada de cuentas bancarias

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el módulo Advanced Bank Account Management del Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

Este módulo incluye la columna Cuenta bancaria en la ventana emergente de Añadir detalles para poder filtrar posibles pagos por cuenta bancaria.

!!! info
    Para más información, visite la [guía de usuario de Advanced Bank Account Management](../../../optional-features/bundles/financial-extensions/advanced-bank-account-management.md).
## Propuesta de Pago

:material-menu: `Aplicación` > `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Transacciones` > `Propuesta de Pago`

### Visión general

La propuesta de pago es una herramienta que ayuda al usuario a realizar pagos seleccionando los documentos relacionados con un método de pago determinado o programados para pagarse antes de una fecha de vencimiento determinada. El sistema propone lo que debe pagarse en función de los criterios de selección proporcionados por el usuario.

Los pasos a seguir son:

- _Introducir_ los criterios de selección, que podrían ser:
  - introducir un tercero determinado cuyas facturas se desean pagar
  - introducir un método de pago determinado, por ejemplo "Transferencia bancaria" si se desea generar de una vez todas las transferencias bancarias del mes
  - o introducir una fecha determinada en el campo "Fecha de vencimiento" si se desea pagar todas las facturas con fecha de vencimiento anterior a esa fecha
  - etc.
- _Ejecutar_ el proceso "**Seleccionar pagos**".  
  Este proceso selecciona los eventos de pago programados de los pedidos/facturas que coinciden con los criterios de selección introducidos y crea una propuesta de pago.
- _Seleccionar_ aquellos documentos (pedidos y/o facturas) de la propuesta que la organización desea pagar.
- _Enviar_ la propuesta.  
  Esta acción rellena la solapa Líneas de la ventana de propuesta de pago.
- _Ejecutar_ el proceso "**Generar pago**".  
  Este proceso genera el pago o pagos teniendo en cuenta que:
  - un pago puede agrupar pedidos/facturas separados a pagar del mismo proveedor en un único pago
  - o agrupar pedidos/facturas separados a pagar independientemente del proveedor en un único pago.

#### Cabecera

La ventana de propuesta de pago permite al usuario introducir un conjunto de criterios de selección que ayudan a realizar pagos de forma masiva.

![Cabecera de Propuesta de Pago](../../../../../assets/drive/1DmluEWtuTWzy0oATmdcPRgODYgZlSz5Z.png)

Los campos a tener en cuenta son:

- **Terceros:** si se introduce un tercero, solo se propondrán los documentos con vencimiento de ese tercero.
- **Método de pago:** si se introduce un método de pago, solo se propondrán los documentos que tengan asignado ese método de pago; sin embargo, también pueden seleccionarse facturas o pedidos pendientes vinculados a métodos de pago diferentes, eliminando los filtros implícitos aplicados (haciendo clic en el icono del embudo).
- **Depositar en:** es posible seleccionar la Cuenta financiera que tiene configurado el método de pago anterior, desde donde se necesita extraer el dinero.
- **Moneda**: es posible seleccionar una moneda si el método de pago seleccionado está configurado para permitir pagos en otras divisas. Si ese es el caso, se muestra un campo que permite al usuario introducir el "Tipo de Cambio" entre la moneda del documento y la moneda de la cuenta financiera.
- **Fecha de vencimiento:** este campo permite al usuario introducir una fecha; por tanto, los documentos de la propuesta tendrán una fecha de vencimiento igual o anterior a la fecha indicada.

El botón de cabecera **Seleccionar pagos** muestra los documentos que coinciden con los criterios de selección introducidos anteriormente.

!!! info
    Tenga en cuenta que los datos mostrados en la rejilla se filtran utilizando los criterios anteriores (filtro implícito). Para ver, por ejemplo, facturas o pedidos pendientes de un Método de pago diferente, es necesario eliminar los filtros haciendo clic en el icono del embudo.

![Seleccionar pagos](../../../../../assets/drive/1DmluEWtuTWzy0oATmdcPRgODYgZlSz5Z.png)

Además, la ventana "Seleccionar pagos" permite al usuario:

- introducir una "**Referencia del Proveedor**", si existe
- modificar el importe de "**Pago**" si el importe a pagar es inferior al importe pendiente
- y seleccionar la casilla "**Cancelaciones**" para cancelar la diferencia entre el importe pendiente y el importe de pago introducido para cada documento/fila seleccionada.

El botón "**Enviar**" finaliza el proceso y hace que la selección se rellene en la solapa Líneas.

Por último, el botón de cabecera **Generar pago** permite al usuario realizar dos acciones:

- **agrupar pagos separados del mismo proveedor en un único pago**,  
  esta opción permite al usuario agrupar pedidos/facturas pendientes del mismo proveedor a pagar en una única transacción de pago.
- o **agrupar todos los pedidos/facturas en un único pago**,  
  esta opción permite al usuario agrupar pedidos/facturas pendientes a pagar en una única transacción de pago, independientemente del proveedor.

Una vez ejecutado:

- Un mensaje del sistema muestra el/los número(s) del/de los pago(s) creado(s).
- La información resumen del pago se refleja en la barra de estado de la ventana Propuesta de Pago.
- Se actualiza la información del Plan de pago y del monitor de pagos de todos los documentos implicados.
- Por último, el estado del pago cambia a _Pendiente de ejecución_ cuando se define un Tipo de Ejecución _Automático_ o a _Pago realizado_ si la ejecución es _Manual_. Si existe un proceso de ejecución definido, puede ejecutarse haciendo clic en el botón Ejecutar Pago.

#### Líneas

La solapa Líneas muestra las transacciones (pedidos y/o facturas) incluidas en la propuesta de pago.

![Líneas de Propuesta de Pago](../../../../../assets/drive/1DmluEWtuTWzy0oATmdcPRgODYgZlSz5Z.png)

Una propuesta de pago puede ser "**Reactivada**", lo que significa que el/los pago(s) creado(s) se eliminan y, por tanto, se eliminan de la ventana Pago.
## Plan de pago de facturas de venta

:material-menu: `Aplicación` > `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Transacciones` > `Plan de pago de facturas de venta`

### Visión general

La ventana de plan de pago de facturas de venta muestra todos los planes de pago de facturas de venta que no están totalmente pagados.

La ventana ofrece otra posibilidad de gestionar la misma información que se puede encontrar en la solapa **Plan de pagos** de la ventana de Factura de venta para una factura determinada.

La ventaja de esta ventana es que ofrece una vista más inmediata de todos los planes de pago de facturas de venta que todavía tienen un **Importe Pendiente** por pagar.

#### Plan de pagos

La información del plan de pago de facturas de venta se muestra agrupada en dos secciones.

La sección **Factura** muestra la información detallada a continuación:

- **Factura**. Hay un enlace a la Factura de venta.
- **Nº documento**. Este es el número de documento de la factura.
- **Terceros**. Este es el tercero contra el cual se emite la factura.
- **Fecha de la factura**. Esta es la fecha de creación de la factura.
- **Importe total**. Este es el importe total de la factura.
- **Importe Pendiente**. Este es el importe pendiente de este plan de pagos.
- **Moneda**. Esta es la moneda de la factura.

La sección **Plan de pagos** muestra la información detallada a continuación:

- **Método de pago**. Este es el método de pago de la factura de venta.
- **Fecha de vencimiento**. Esta es la "Fecha de vencimiento" original acordada con el cliente. Esta fecha se utiliza como la "Fecha de Referencia" en algunos informes financieros, como la \[\[Projects:Payment_Aging_Balance/User_Documentation|Consulta de antigüedad de cobros.
- **Fecha esperada**. Esta es la fecha en la que se espera cobrar el pago. Cuando se crea el plan de pagos, es la misma fecha que la "Fecha de vencimiento", pero puede cambiarse posteriormente.  
  Esta fecha refleja una revisión del plan de pagos original en la que la "Fecha de vencimiento" ha cambiado.  
  Esta fecha se utiliza como la "Fecha de Referencia" en algunos informes, como el informe de pagos.  
  Además, este campo es el único que se puede cambiar en esta ventana. Si se cambia, ese cambio también se reflejará en la solapa de plan de pagos de la correspondiente factura de compra.

**Días Retraso**

Este es el número de días desde la fecha esperada hasta el día actual.
## Cobros

:material-menu: `Aplicación` > `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Transacciones` > `Cobros`

### Visión general

Los pagos y anticipos de clientes recibidos pueden registrarse y gestionarse en la ventana Cobros. Además, los pagos de Concepto contable no relacionados con pedidos/facturas también pueden gestionarse en esta ventana.

Los pagos de clientes pueden recibirse contra:

- Pedidos de venta; en la práctica, esto es un _anticipo_.  
  Posteriormente, cuando se crea una factura a partir del pedido que ya tiene un pago recibido asociado, la factura hereda automáticamente el pago recibido asociado al pedido.
- Facturas de venta; en la práctica, esto es un pago de factura recibido de un cliente.  
  Los pagos anteriores a la fecha contable de la factura también se consideran un _anticipo_.
- Y Conceptos contables; en la práctica, esto es un pago de cualquier otro ingreso recibido de un cliente, por ejemplo, una multa.  
  Este tipo de pagos puede crearse en esta ventana al seleccionar el "Tipo de Transacción" de Concepto contable o puede completarse automáticamente como un pago en esta ventana si se crea en Asientos manuales.  
  Independientemente de cómo se creen, ambos casos se gestionan de la misma manera en función del Método de pago utilizado.

!!! info
    Etendo permite al usuario registrar pagos recibidos de un único cliente o registrar pagos recibidos de varios clientes al mismo tiempo.

Al final del proceso, una transacción de "Cobros" implicará la creación de una transacción de "Depósito" en la Cuenta financiera correspondiente.

La creación de la transacción de depósito en la cuenta financiera puede realizarse:

- manualmente mediante el proceso Añadir transacción de la cuenta financiera.
- o automáticamente si el método de pago utilizado está configurado para ello, lo que implica la selección de la casilla de verificación "Depósito automático".
### Cabecera

La ventana **Cobros** permite al usuario registrar y gestionar los pagos recibidos de clientes contra distintos tipos de documentos emitidos por la organización, como pedidos y facturas. Esta ventana también permite al usuario gestionar los pagos de clientes ya registrados en la ventana de factura de venta, del mismo modo que los pagos recibidos de **Concepto contable** en **Asientos manuales**.

![](../../../../../assets/drive/1fpeZSZHjXcKDr4wXaXJWREQHqKdD_B1c.png)

Solo hay unos pocos campos obligatorios que completar al registrar un cobro en esta ventana:

- la **Organización** que recibe el pago
- el **Número de pago** que sigue la secuencia de documento correspondiente
- el **Método de pago** utilizado para recibir el pago. Hay una casilla de verificación en la ventana "Añadir pago" que posteriormente permite al usuario seleccionar documentos vinculados a métodos de pago alternativos
- y la **Cuenta financiera** donde se va a depositar el dinero.

Otros campos relevantes a tener en cuenta son:

- el **Importe** recibido. No es necesario introducirlo al crear un nuevo registro.
- el campo **Cobrado de** muestra el cliente del que el usuario está recibiendo el pago. No es necesario introducirlo al crear un nuevo registro.
  - **Si no se selecciona un cliente,** implica la creación de un pago que puede cobrar el pago de distintos documentos relacionados con distintos clientes.
  - **Si se selecciona un cliente,** implica la creación de un pago que puede cobrar el pago de distintos documentos del mismo cliente. En este caso, el valor de los campos "Método de pago" y "Depositar en" cambia si el cliente tiene asignado un método de pago específico y una cuenta financiera a utilizar al cobrar sus facturas.
- **Nº de referencia**, este campo se utiliza para reflejar el número impreso en el documento justificativo de pago recibido del cliente.
- y la **Moneda**. Es posible seleccionar una moneda distinta de la moneda de la cuenta financiera al recibir un pago. Para ello, el método de pago utilizado y asignado a la cuenta financiera del pago debe estar configurado para recibir pagos en múltiples divisas.

#### Ventana Añadir pago

El botón **Añadir Detalles de Pago** abre la ventana **Añadir pago**, donde se pueden seleccionar los documentos que se están pagando.

![](../../../../../assets/drive/1xlIbwx_2b4aA_LHx9ud0-vHDkCSc-a36.png)

!!! info
    La ventana "Añadir pago" ya se explica en el artículo [Pago de factura de venta](../../sales-management/transactions.md#payment).

#### Pago de varios tipos de documento de distintos clientes

Si no se ha seleccionado ningún cliente en el campo "Cobrado de", es posible registrar el pago de distintos clientes al mismo tiempo simplemente seleccionando las transacciones a pagar.

!!! info
    Tenga en cuenta que Etendo permite al usuario filtrar una vez más por un tercero determinado si no se introdujo en el campo "Cobrado de" por error. Cuando esto sucede, los pagos deben realizarse ejecutándolos por el importe exacto.

El importe de **Pago real** introducido se distribuye automáticamente entre las deudas pendientes (facturas o pedidos pendientes de pago). Es posible evitar esta distribución automática configurando la Preferencia _Añadir pago: Distribuir importes automáticamente_ a 'N'

![](../../../../../assets/drive/1mt_1DYKUPLmroqfwaT8dTs-QjPhH8wQp.png)

El usuario puede marcar o desmarcar las transacciones según sea necesario, y también puede modificar los importes mostrados en el campo "Importe".

Es importante tener en cuenta que:

- En este escenario, no es posible generar crédito ni reembolsar un importe restante al cliente porque ambas acciones deben estar relacionadas con un único cliente.  
  Por lo tanto, si el importe pagado y reflejado en el campo de pago real es superior a la suma del importe total de las facturas seleccionadas, se muestra un mensaje de error indicando que "Existe una diferencia de importe sin ninguna acción seleccionada".  
  En ese caso, o bien debe disminuirse el importe del pago real o debe seleccionarse otro pedido/factura a pagar.
- Si el Pago real es inferior al Pago esperado, el importe restante puede dejarse como:
  - un **pago insuficiente**, es decir, registrar un pago parcial donde la deuda restante se pagará posteriormente registrando un nuevo pago en
  - o puede ser **cancelado**, si se selecciona, significa registrar un pago parcial donde la deuda restante no se va a pagar; en este último caso:
    - la factura del cliente se establece como totalmente pagada
    - la contabilización de la factura en el libro mayor liquida el importe total de cuentas a cobrar del cliente
    - mientras que la contabilización del pago en el libro mayor utiliza la cuenta de importes de **Cancelaciones** para contabilizar el importe cancelado.

#### Procesamiento de un pago

Hay dos opciones disponibles al **procesar** un cobro creado en esta ventana:

- Procesar cobro(s) recibido(s)
- o Procesar cobro(s) recibido(s) y depositar.

Ambas opciones procesan el cobro, pero la segunda también crea la transacción de "Depósito" correspondiente en la **Cuenta financiera** utilizada.

Esta última opción es la única que se muestra si el método de pago utilizado y asignado a la cuenta financiera donde se va a depositar el dinero está configurado como "Depósito automático" = Sí.

Además:

- Un mensaje del sistema muestra el número del pago creado
- La información resumen del pago se refleja en la **Barra de estado** de la ventana **Cobros**.
- El campo **Descripción** se actualiza con los números de Factura y Pedido pagados y el importe dejado como crédito
- Se introducen registros de detalle del pago en la solapa **Líneas**.
- Este proceso también actualiza la información del **Plan de cobro** y del **Monitor de pagos** de todos los documentos implicados.
- El **Estado del pago** cambia a _Pendiente de ejecución_ cuando se define un **Tipo de Ejecución** _Automático_ o a _Pago recibido_ si la ejecución es _Manual_.  
  Si existe un proceso de ejecución definido, puede ejecutarse haciendo clic en el botón "**Ejecutar Pago**". La información aparecerá en la solapa Historial de Ejecuciones.

Tenga en cuenta que no es necesario procesar:

- los pagos recibidos de clientes en la ventana de factura de venta, ya que allí ya están procesados
- ni los pagos recibidos de **Concepto contable** en la ventana **Asientos manuales**, ya que estos implican el procesamiento automático del cobro.

#### Reactivar un pago

Un pago ya procesado con estado "Pago recibido" o "Pendiente de ejecución" puede ser **Reactivado**. Esta opción permite al usuario editar datos de pago incorrectos o eliminar un pago creado erróneamente.

El botón "Reactivar" permite al usuario hacer lo explicado anteriormente, ya que se pueden seleccionar dos acciones diferentes:

- **Reactivar**: esta opción reactiva el pago, manteniendo las líneas de pago.  
  Una vez reactivado el pago de este modo, el usuario puede modificar fácilmente la información del pago utilizando el botón "Añadir Detalles de Pago" y procesarlo de nuevo.
- **Reactivar y eliminar líneas**: esta opción reactiva el pago y elimina todas las líneas de pago.  
  Esta opción es la que debe utilizarse si el pago se creó erróneamente y, por tanto, debe eliminarse por completo.  
  Una vez reactivado el pago de este modo, el usuario puede eliminar la cabecera del pago sin necesidad de eliminar antes las líneas de pago.

Un pago ya procesado y depositado con estado "Depositado no conciliado" también puede ser "Reactivado" como se describe anteriormente, pero una vez que la transacción de depósito correspondiente se haya eliminado de la cuenta financiera.

#### Contabilizar un pago

Un cobro recibido y procesado en la ventana **Cobros** puede contabilizarse si el método de pago utilizado al crear el pago permite hacerlo una vez asignado a la cuenta financiera a través de la cual se recibe el pago. Si no es así, Etendo muestra un aviso: "Documento deshabilitado para contabilidad".

La contabilización de un cobro recibido es:

|                                                           |                |                |
| --------------------------------------------------------- | -------------- | -------------- |
| Cuenta                                                   | Debe           | Haber          |
| Al cobro usar la "Cuenta de pagos en tránsito" p. ej.     | Importe de pago |                |
| Cuentas a cobrar de clientes                              |                | Importe de pago |

La contabilización será diferente cuando el importe provenga parcial o totalmente de una deuda clasificada como dudoso cobro.

#### Anular un pago

Un pago ya procesado con estado "Pendiente de ejecución" puede ser "**Anulado**". El botón de proceso "Reactivar" permite al usuario hacerlo, pero solo para pagos en estado "Pendiente de ejecución".

!!! info
    _Recuerde que un pago puede obtener un estado pendiente de ejecución si el método de pago utilizado y asignado a la cuenta financiera está configurado para tener un "Tipo de Ejecución" automático y además está seleccionada la casilla "En espera"._

La acción de anulación establece la(s) línea(s) de pago como "**Cancelado**", lo que significa que el documento (pedido o factura) en realidad no está pagado y, por tanto, se puede crear o añadir un nuevo pago.

#### Pagos con crédito

No es posible generar crédito en un pago que no esté relacionado con un único cliente; por lo tanto, la funcionalidad de crédito generado requiere:

- seleccionar un tercero (o cliente) en el campo "**Cobrado de**" de la ventana **Cobros**.
- e introducir el importe a dejar como crédito en el campo "**Importe**" de la ventana **Cobros**.

La creación de un pago con crédito requiere no seleccionar ningún documento a pagar en la ventana "Añadir pago" que se muestra tras pulsar el botón de proceso "Añadir Detalles de Pago", sino dejar el importe para utilizarlo posteriormente.

![](../../../../../assets/drive/1SK4SF6ntwYbSpP5JZMwZNObD5ceJ1I1q.png)

Un pago con crédito estará disponible para el cliente tras procesar el pago como se ha indicado.

Este pago con crédito especifica el importe de crédito generado en el campo "Descripción" de la cabecera del pago con crédito.

Posteriormente, el crédito disponible generado para ese cliente puede utilizarse para pagos posteriores:

- en la ventana "Añadir pago", una vez que se crea un nuevo cobro para ese cliente en la ventana de cobros, simplemente seleccionando una línea y estableciendo el importe en la **rejilla de crédito a utilizar.**

![](../../../../../assets/drive/15yfpM_16EYf7RNcNfI5IJTHrg8Xd-1lx.png)

- o en la ventana "Seleccionar pagos con crédito", que se muestra automáticamente al completar una nueva factura de cliente.

Entonces, el campo "Descripción" de la cabecera del pago con crédito también especificará las transacciones/documentos donde se utilizó el crédito.

La solapa Origen del crédito usado de la ventana de cobros muestra el pago con crédito utilizado para pagar el pago de un documento de cliente (pedido, factura o concepto contable).

#### Pagos en múltiples divisas

Etendo permite al usuario recibir pagos en una moneda distinta de la moneda de la cuenta financiera.

Para ello, el método de pago asignado a la cuenta financiera utilizada para recibir el pago debe estar configurado para permitirlo, lo que implica seleccionar la casilla "Permitir pagos en otras divisas".

#### Anticipos que exceden el importe de la factura a pagar

Etendo permite realizar anticipos añadiendo pagos a los pedidos. La factura de venta creada a partir del pedido heredará el pago realizado para el pedido.

Puede ocurrir que el importe real anticipado exceda el importe de la factura a pagar; por lo tanto, la factura de venta permanece como "Pagado" = "No" hasta que

- o bien se crea un cobro "negativo" para reflejar que la organización devuelve al cliente la diferencia, de modo que el saldo final del pago sea igual al importe de la factura de venta
- o bien se crea un pago con crédito para utilizarlo posteriormente al registrar el pago de otra factura de venta del mismo cliente.  
  Este pago con crédito debe crearse como un nuevo cobro por un importe 0.00 y relacionado con la factura de venta anticipada; de ese modo, la factura anticipada se establece como "Pagado" = "Sí".
### Líneas

La solapa **Líneas** contiene una lista de los documentos pagados por el pago.

#### Historial de Ejecuciones

La solapa **Historial de Ejecuciones** muestra información sobre el historial de los intentos de ejecución del pago.

Para algunos tipos de pago, se necesitan algunos pasos adicionales. Por ejemplo, un cobro recibido con un cheque que debe rellenarse con el número de cheque del cliente.

En ese caso, el método de pago vinculado al pago debe configurarse para requerir un proceso de **Tipo de Ejecución** "Automático".

Todo lo anterior implica un paso adicional a realizar en la ventana **Cobros**, que consiste en ejecutar el pago utilizando el botón de proceso "**Ejecutar Pago**".

Este botón de proceso solo se muestra en caso de pago/s vinculados a un proceso de ejecución automatizada para el cual está seleccionada la casilla "**En espera**".

Si la casilla "En espera" no está seleccionada, el paso adicional sigue siendo necesario, pero se ejecutará automáticamente sin ninguna acción por parte del usuario final.

La solapa **Historial de Ejecuciones** es una solapa de solo lectura que muestra información sobre la ejecución del pago, como la fecha de ejecución, obviamente una vez que el pago ha sido ejecutado.

![](../../../../../assets/drive/1iYYhQ7YfTWNOlhN5amCRAUoKV297gvq7.png)

#### Tipos de cambio

La solapa **Tipos de cambio** permite al usuario introducir un tipo de cambio entre la moneda del libro mayor de la organización y la moneda del cobro recibido, que se utilizará al contabilizar el pago en el libro mayor.

#### Origen del crédito usado

Un pago de crédito puede utilizarse para liquidar el pago de más de un documento. Esta tabla realiza el seguimiento de los documentos en los que se ha utilizado un pago de crédito.

La creación de un pago de "Crédito" ya se explica en la sección de Pagos de crédito de este artículo, al igual que cómo un pago de "Crédito" o el crédito disponible del cliente aparecerá en futuros pagos del cliente.

Esta solapa de solo lectura muestra el pago de crédito utilizado para pagar el pago de un documento de un cliente (pedido, factura o concepto contable).

![](../../../../../assets/drive/1OazvwkBhV5J6jSKEJwYlyyK5PfyYrnQr.png)
### Eliminación de pagos

El objetivo de esta funcionalidad es eliminar y reactivar pagos de una forma ágil y sencilla. Además, permite eliminar y reactivar transacciones bancarias y conciliaciones.

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

Desde esta ventana, es posible eliminar pagos seleccionando el registro correspondiente y, a continuación, haciendo clic en el botón **Eliminar pago**.  
Por otro lado, es posible reactivar pagos desde la misma ventana con el botón **Reactivación avanzada**. Esta funcionalidad permite al usuario reactivar el pago sin eliminar manualmente sus transacciones asociadas, lo cual es necesario si se utiliza el botón del core **Reactivar**. Esto devolverá el pago al estado **Pendiente de pago** y se podrán añadir nuevos detalles del pago.

En ambos casos:

- Si el pago está incluido en la **Cuenta financiera**, es decir, si está en estado **Depositado/Reintegrado no conciliado**, también se eliminará la transacción asociada (ventana **Cuenta financiera** > solapa **Transacciones**).

- Si el pago está conciliado mediante un método automático, entonces, además de la transacción en la **Cuenta financiera**, se eliminará la línea del **Extracto bancario** a la que estaba vinculada (ventana **Cuenta financiera** > **Líneas de extracto bancario importadas**) y la línea correspondiente de la conciliación bancaria ( **Cuenta financiera** > solapa **Reconciliaciones**).

!!! info
    Si el pago está contabilizado, se eliminará el asiento contable.

![](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions/PRpic5.png)
### Contabilización masiva

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el bundle Financial Extensions. Para ello, siga las instrucciones del marketplace: [Bundle Financial Extensions](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

La funcionalidad de Contabilización masiva permite al usuario contabilizar o descontabilizar múltiples registros seleccionando los registros correspondientes y haciendo clic en el botón **Contabilización masiva**.

Además, el Estado contable del/de los registro/s se muestra en la barra de estado, en la vista de formulario, o en una columna, en la vista de cuadrícula.

!!! info
    Para más información, visite [la guía de usuario del módulo Bulk Posting](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).
### Liquidación avanzada de terceros

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el bundle Financial Extensions. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

Desde la ventana **Cobros**, es posible crear una liquidación haciendo clic en el botón **Añadir Detalles de Pago**. En la ventana emergente, Etendo muestra una lista de facturas a liquidar, cada una con su correspondiente número de factura; aquí el usuario puede seleccionar la factura o facturas a compensar. Primero, establezca el **Importe real del pago** a pagar y, a continuación, seleccione la(s) factura(s) para crear una liquidación y defina el importe correspondiente a pagar de la/cada factura.

![](../../../../../assets/drive/14Hd8Odyebc7szAzDDE-i6QimctGQGmAZ.png)

Desde la solapa **Factura desde compensación**, seleccione la(s) factura(s) de compra que se utilizarán para pagar y establezca el importe necesario de la(s) factura(s) a compensar.

Debajo, en la solapa **Total**, Etendo muestra los importes totales de referencia a compensar.

![](../../../../../assets/drive/18JZjM6yNh6hBTBbFDk-130_eYzTmI2As.png)

Tras hacer clic en el botón **Hecho**, el sistema compensa las facturas y los créditos del tercero correspondiente y crea un registro de liquidación.

![](../../../../../assets/drive/1f8SDqKDjiTO59I2Hxzlb3XosxMHDsQFQ.png)

El registro de liquidación se registra en la ventana **Liquidación de terceros**, donde se mostrarán las líneas de la(s) factura(s) (venta y compra) utilizadas para compensar.

![](../../../../../assets/drive/1hLhHQMEICTtf2nc-QF6lrolaOOnwIabv.png)

!!! info
    Para más información, visite la [Guía de usuario del módulo Business Partner Settlement](../../../optional-features/bundles/financial-extensions/business-partner-settlement.md).
### Gestión avanzada de cuentas bancarias

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el módulo Advanced Bank Account Management del bundle Financial Extensions. Para ello, siga las instrucciones del marketplace: [Bundle Financial Extensions](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

Este módulo incluye la columna Cuenta bancaria en la ventana emergente Añadir Detalles de Pago, para poder filtrar los posibles pagos por cuenta bancaria.

!!! info
    Para más información, visite la [Guía de usuario de Advanced Bank Account Management](../../../optional-features/bundles/financial-extensions/advanced-bank-account-management.md).
## Cuenta financiera

:material-menu: `Aplicación` > `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Transacciones` > `Cuenta financiera`

### Visión general

Una Cuenta financiera representa una cuenta en una institución financiera, como una cuenta bancaria, un emisor de tarjeta de crédito, un servicio de pago electrónico, así como una caja o caja chica.

Etendo permite al usuario crear tantas Cuentas financieras como requiera la organización en la ventana de cuenta financiera, la cual se utiliza para registrar transacciones monetarias como pagos de facturas, comisiones bancarias, cargos de tarjeta de crédito, etc.

Las obligaciones de pago y los importes a vencer de los clientes se crean en las ventanas de facturas de compra y de venta. Sin embargo, los cobros de clientes y los pagos a proveedores de estas facturas normalmente se registran en la ventana Cuenta financiera o en las ventanas Cobros y Pago.

!!! warning
    Es muy importante definir correctamente cada parámetro de cada Cuenta financiera. Durante el proceso de configuración de su Cuenta financiera, necesitará información como: la información de la cuenta bancaria, los métodos de pago permitidos, la(s) moneda(s) de la cuenta bancaria, la información contable, etc.
### Cuenta

La ventana **Cuenta financiera** contiene información esencial, como el número de cuenta bancaria, y permite al usuario ejecutar un conjunto de procesos, como añadir transacciones de depósito o reintegro a la cuenta financiera o importar y conciliar un archivo de extracto bancario.

![Cuenta](../../../../../assets/drive/1G1flRQCPZ_77ab9ntPfNwRfU9TwaaJDf.png)

La **información esencial de la cuenta financiera** que se debe completar en la sección superior de la ventana de cuenta financiera es:

- El **Nombre** y una **Descripción** de la cuenta.
- La **Moneda** de la cuenta.
- El **Tipo** de cuenta: existen dos tipos de cuenta: **Banco-Sucursal** y **Efectivo**.  
  En función del tipo seleccionado, cambia la información requerida a introducir. No es necesario completar la información de cuenta bancaria si el tipo de cuenta seleccionado es "Efectivo".  
  Es posible definir tipos de cuenta adicionales ampliando la **Lista** _Tipo de cuenta financiera_.
- Si esta es la cuenta **Valor por defecto** que se utilizará en las transacciones o no. Cuando se crean facturas, pedidos y otros documentos que incluyen una Cuenta financiera, esta será la que se muestre por defecto.
- El **Terceros** asociado a esta cuenta bancaria. Por ejemplo, la entidad financiera que mantiene la cuenta. Esta información se utiliza con fines contables. La dirección de ubicación relacionada con el tercero es solo información visual, que se carga cuando se selecciona el tercero.
- El **Saldo Inicial**: en la mayoría de los casos, la empresa ya está operativa en el momento en que se implementa Etendo. Este campo permite al usuario inicializar el saldo inicial de cada Cuenta financiera proporcionando el saldo real de la cuenta de caja/banco tal y como estaba en la fecha de la última conciliación. Posteriormente, el valor de este campo se utiliza como **Saldo inicial** en la primera conciliación de esta Cuenta financiera en Etendo. Este campo solo es editable al crear la Cuenta financiera.
- El **Saldo corriente**: es el saldo de la Cuenta financiera según los registros de Etendo. Se calcula como la suma del **Saldo Inicial** y cada transacción de la Cuenta financiera. Este campo se muestra en la barra de estado.
- El **Algoritmo de Reconciliación** que se utilizará durante el proceso de conciliación.
  - Si no se selecciona **ningún algoritmo de conciliación** en ese campo, no es posible importar y luego conciliar un archivo de extracto bancario, pero sí realizar el **Proceso de Reconciliación** de las transacciones de la cuenta.
  - Si se selecciona un algoritmo de conciliación como el algoritmo **Estándar**, permite al usuario utilizar el proceso **Importar extracto bancario**. Este proceso permite importar datos desde un archivo a la solapa Líneas de extracto bancario importadas y, a continuación, utilizar el proceso **Conciliación** para conciliar las transacciones de la cuenta con las líneas del extracto bancario importadas. Este algoritmo de conciliación admite el reconocimiento de "transacciones de Concepto contable".
  - Existe otro algoritmo entregado como un módulo denominado Algoritmo de conciliación avanzado. Este módulo permite que las líneas del extracto bancario importadas se concilien no solo con las transacciones existentes de la cuenta financiera, sino también con pagos, facturas o pedidos. Si no se encuentra ningún documento de transacción de ese tipo, registra un pago de crédito para los terceros para su uso posterior. Este algoritmo de conciliación admite la creación automática de pagos y transacciones de cuenta financiera (depósitos y reintegros), incluida la creación de "transacciones de Concepto contable".
- El campo **Habilitada para Transferencia de Fondos** se utiliza para habilitar/mostrar el proceso del botón de transferencia de fondos. Por defecto, todas las cuentas financieras se configuran como habilitadas.

La siguiente sección **Cuenta bancaria** solo es visible para cuentas del tipo **Banco-Sucursal** y se utiliza para especificar el número de cuenta bancaria. Esta sección incluye información como:

- El **Nº de cuenta genérico**: aquí se puede introducir un número de cuenta genérico para identificar la cuenta bancaria. Este campo debe ser obligatorio en caso de que se seleccione _Usar Nº de cuenta genérico_ o _Usar SWIFT + Nº de cuenta genérico_ en el campo "**Formato cuenta bancaria**".
- El **IBAN**: el International Bank Account Number (IBAN) es un estándar internacional para la numeración de cuentas bancarias.  
  El IBAN consta de un código de país ISO 3166-1 de dos letras, seguido de dos dígitos de control y hasta treinta caracteres alfanuméricos para el número de cuenta bancaria nacional, denominado BBAN (Basic Bank Account Number). Este campo debe ser obligatorio en caso de que se seleccione la opción _Mostrar IBAN_ en el campo "**Formato cuenta bancaria**". El código IBAN se validará automáticamente al insertar/actualizar el registro, teniendo en cuenta las reglas definidas para el banco del país.
- El **Código Swift**: corresponde al identificador de código bancario internacional ISO 9362. Debe ser obligatorio en caso de que se seleccione la opción _Usar SWIFT + Nº de cuenta genérico_ en el campo "**Formato cuenta bancaria**".
- **País**: puede seleccionar un país de la lista para especificar si la cuenta bancaria es una cuenta bancaria nacional o una cuenta bancaria extranjera.
- **Formato cuenta bancaria**: lista que contiene todos los valores posibles para generar el número de cuenta mostrado, que posteriormente será utilizado por otros informes o procesos para obtener el identificador de la cuenta. Los valores posibles son:
  - _Usar Nº de cuenta genérico_
  - _Mostrar IBAN_
  - o _Usar SWIFT + Nº de cuenta genérico_

!!! info
    Tenga en cuenta que otros módulos que amplíen el formato de cuenta bancaria admitido pueden añadir otras opciones.

La sección **Más información** puede incluir información como:

- El campo **Tipo de límite de cancelación**, que permite al usuario definir distintos tipos de límites de cancelación para una cuenta financiera.  
  Este campo se muestra cuando el valor de la propiedad "Write-off limit" se establece en "Y" en la ventana Preferencias.
  - La única opción disponible actualmente es "Importe"
- Y el valor **Límite de cancelación** para el límite de cancelación en un pago. Cuando el tipo seleccionado es Importe, el valor contiene el importe en la moneda de la cuenta financiera.  
  Este campo se muestra cuando el valor de la propiedad "Write-off limit" se establece en "Y" en la ventana Preferencias.

    Tomemos, por ejemplo, la configuración de un importe de "Límite de cancelación" de 1,00 $ para una cuenta financiera determinada.

    Al registrar un cobro de un cliente en la ventana Añadir pago, el sistema no permitirá al usuario cancelar un importe superior al límite de cancelación definido.

    Lo mismo se aplica a los pagos a proveedores creados mediante la ventana Añadir pago o la funcionalidad Propuesta de Pago.
#### Botones
##### Añadir múltiples pagos

El botón de proceso "Añadir múltiples pagos" permite al usuario crear y procesar transacciones de cuenta financiera seleccionando varios pagos al mismo tiempo.

Los pagos que se muestran para su selección son aquellos cuyo estado del pago es igual a "Pago realizado" o "Pago recibido"; por lo tanto, los pagos que tengan, por ejemplo, un estado del pago "Pendiente de ejecución" no se mostrarán para su selección.

Por defecto, los pagos mostrados son los definidos originalmente para esta cuenta financiera. Sin embargo, el usuario puede eliminar este filtro para mostrar y seleccionar pagos de otras cuentas financieras.

![Add multiple payments](../../../../../assets/drive/1WDuGJ8r3aCcAzVGC1bFj1pc87CkaEJxG.png)

Las únicas acciones a realizar son introducir una "Fecha de la transacción" y seleccionar tantos pagos como sea necesario a la vez.

Los pagos seleccionados se listan entonces como:

- transacciones "**Depósito de tercero**", en el caso de "Pagos recibidos"
- o transacciones "**Reintegro de tercero**", en el caso de "Pagos realizados"

en la solapa "Transacción" de la Cuenta financiera.

Todas esas nuevas transacciones se crean ya como "Procesado", por lo tanto pueden "Reactivarse" si fuese necesario o, finalmente, "Contabilizarse" en el libro mayor si aplica.

##### Proceso de Reconciliación

El botón de proceso de cabecera "**Proceso de Reconciliación**" se muestra para aquellas cuentas financieras que no tienen asignado un algoritmo de reconciliación.

Ese botón abre la ventana "Conciliación".

La ventana de conciliación tiene tres partes principales:

- la sección superior, que incluye información general como la cuenta financiera que se está conciliando, la fecha del extracto a conciliar, el saldo inicial (o "Saldo Inicial" de la cuenta financiera) y el saldo final como resultado de la conciliación. El saldo final es el saldo de la última conciliación de la cuenta financiera.
- la sección central, que incluye una lista de las transacciones pendientes de conciliar, por lo tanto marcadas como "Comprobación" "No" en la solapa de transacciones de la cuenta financiera.
- y la sección inferior, que incluye información general de saldos, así como tres botones de proceso: "Guardar", "Proceso de Reconciliación" y "Cancelar".

El "Saldo inicial" + los importes "Recibido" - los importes "Pagado" deben ser iguales al "Saldo final".

Puede introducir el saldo final o lo que indique el extracto y luego seleccionar las transacciones pagadas/recibidas, o hacerlo al revés.

!!! info
    Es posible crear una transacción de "Concepto contable" en caso de que existan pequeñas diferencias entre lo que indican los extractos y las transacciones registradas pendientes de conciliar.

![Reconciliation window](../../../../../assets/drive/1N1L6_XETrXBZnbUB3YwVD_RJvVmd0G6V.png)

El botón de proceso "**Guardar**" guarda un "**Borrador**" de la conciliación en la solapa Reconciliaciones de la cuenta financiera y marca la(s) transacción(es) seleccionada(s) como "Comprobación", así como "Comprobación" en la solapa de transacciones de la cuenta financiera.

Siempre es posible reabrir una conciliación guardada y modificar lo que sea necesario.

!!! info
    Tenga en cuenta que solo puede existir una conciliación en estado borrador en una cuenta financiera.

El botón de proceso "**Proceso de Reconciliación**" concilia las transacciones marcadas como comprobadas; por lo tanto, la conciliación se procesa y su estado cambia a "Completada".

Finalmente, el botón de proceso "**Cancelar**" simplemente cierra la ventana de conciliación y elimina el saldo final introducido, si lo hubiera.

##### Importar extracto bancario

El botón de proceso de cabecera **Importar extracto bancario** se muestra para aquellas cuentas financieras que tienen asignado un algoritmo de reconciliación. Este botón de proceso permite al usuario importar un extracto bancario que, por lo tanto, se guarda en la solapa Extractos bancarios importados de la cuenta financiera y en la subsolapa Líneas de extracto bancario.

!!! info
    Actualmente, Etendo proporciona el algoritmo de reconciliación **Estándar**. El comportamiento del algoritmo de reconciliación estándar se explica en la siguiente sección "Conciliación".

!!! info
    Etendo permite al usuario importar un extracto bancario si previamente se ha instalado un módulo de formato de importación de archivo bancario.


Actualmente, Etendo proporciona los siguientes módulos de importación de archivos bancarios:

- OFX Bank Statement Format
- CSV Generic Bank Statement Importer
- WePay CSV Importer
- y el español Cuaderno 43

Dependiendo del módulo instalado para este propósito, será posible importar archivos de extracto bancario en formato OFX o CSV, entre otros.

El botón de proceso "Importar extracto bancario" abre la ventana "Importar archivo bancario".

![Import Statement](../../../../../assets/drive/127lBLYWqTXTFWRW2bCr3BJ3M3RasGZ5W.png)

Esta ventana permite:

- seleccionar un **archivo de extracto bancario**
- y seleccionar el **formato de archivo** del archivo de extracto bancario seleccionado para importar.

##### Conciliación

Una vez que se ha importado un archivo de extracto bancario, el botón "Conciliación" abre una nueva ventana donde se muestran las líneas del extracto bancario importado y las transacciones financieras existentes. Por defecto, existe un filtro implícito que oculta las líneas del extracto bancario que ya están conciliadas.

![Match Statement](../../../../../assets/drive/1TBIUGHObHsHlBtGTmHZE_HHg3mK8PtuK.png)

Antes de abrir la ventana, se muestra un pop up preguntando si el algoritmo debe ejecutarse contra las líneas del extracto bancario no conciliadas o no. Si es así, el algoritmo intentará encontrar una conciliación para todas las líneas del extracto bancario no conciliadas. Si no, se abrirá la ventana de conciliación y el usuario deberá realizar las conciliaciones manualmente.

![Example 2](../../../../../assets/drive/1GimSn37f-WQGok4aqb0NWFwDg4Xri2ZM.png)

Esta ventana tiene dos grupos de columnas divididos por la columna Conciliar.

- **Líneas de extracto bancario importadas** en el lado izquierdo. Esta sección lista los depósitos del extracto bancario y los pagos:
  - **Fecha:** es la fecha del movimiento realizado en la cuenta bancaria.
  - **Terceros:** es el tercero informado en la línea del extracto bancario.
  - **Nº de referencia:** es la referencia del extracto bancario, si existe.
  - **Importe:** es el importe informado en la línea del extracto bancario, restando el Importe Débito del Importe Crédito.
- **Transacción en Etendo** en el lado derecho. Esta sección lista las transacciones de la cuenta financiera que concilian con las líneas del extracto bancario:
  - **Conciliar:** proporciona 3 botones para operar con las líneas del extracto bancario (explicado más adelante). Además, la columna puede utilizarse para filtrar por el estado de conciliación (Sí para mostrar líneas comprobadas, No para mostrar líneas no comprobadas).
  - **Afinidad:** cuando la conciliación se realiza automáticamente mediante el Algoritmo de Reconciliación, este campo muestra el nivel de afinidad de la conciliación. Si el usuario asocia manualmente una transacción, este campo está vacío. La afinidad es mayor cuando los criterios de conciliación son los mismos tanto en la transacción de la cuenta financiera como en la línea del extracto bancario.
  - **Tipo de relación:** el tipo de conciliación.
  - **Fecha de la transacción:** es la fecha en la que se creó la transacción en la cuenta financiera.
  - **Tercero de la transacción:** es el tercero de la transacción.
  - **Importe Transacción:** es el importe de la transacción, restando el Importe del reintegro del Importe del depósito.

Como ya se ha mencionado, el algoritmo de conciliación disponible es el "Algoritmo de reconciliación estándar".

El algoritmo de conciliación estándar puede configurarse para conciliar por diferentes conjuntos de criterios:

- **Asociar nombre del tercero:** esta opción hace que la conciliación sea fuerte si el nombre del tercero de la línea del extracto bancario y el tercero de la transacción coinciden.
- **Asociar fecha de transacción:** esta opción hace que la conciliación sea fuerte si la fecha de la transacción de la línea del extracto bancario y la fecha de la transacción coinciden.
- **Asociar referencia:** esta opción hace que la conciliación sea fuerte si la referencia de la línea del extracto bancario y la referencia de la transacción coinciden.

Se pueden seleccionar todos los criterios anteriores o solo algunos de ellos.

!!! info
    Las transacciones no conciliadas pueden conciliarse manualmente. 

Tomemos, por ejemplo, la situación inicial que se muestra a continuación, donde hay tres líneas del extracto bancario que no concilian:

![Example 3](../../../../../assets/drive/1K31lmmG2WiS1k6bunMTXgghMHLw9Chw3.png)

- el icono de la "lupa" ayuda a buscar transacciones para conciliar, ya que abre una nueva ventana que muestra las transacciones de la cuenta financiera registradas el mismo día que la línea del extracto bancario o antes. Se pueden seleccionar varias transacciones al mismo tiempo para conciliarlas con una única línea del extracto bancario. En ese caso, el sistema divide automáticamente la línea original del extracto bancario tantas veces como transacciones se seleccionen.

![Example 4](../../../../../assets/drive/1OL1GtOSH905zxVc9UjliNCM3UztnFK84.png)

Volviendo a nuestro ejemplo, no hay ninguna transacción que concilie con la segunda transacción del archivo de extracto bancario (la que tiene un importe igual a 1.500,00). Si existiera una conciliación, podría seleccionarse utilizando también el icono de la "lupa".

- el icono "+" ayuda a añadir transacciones a la cuenta financiera (e incluso a crear un pago para depositar o retirar de la cuenta financiera), ya que abre la ventana "Añadir transacción".

![Example 5](../../../../../assets/drive/1MhRo1pZgSopD5v9S3avUHPR5HUWW_XdZ.png)

La imagen anterior muestra que había una transacción "Recibido" pendiente de crearse en la cuenta financiera. Una vez creada, se concilia.

Volviendo a nuestro ejemplo, la situación actual se muestra en la imagen siguiente:

![Example 6](../../../../../assets/drive/1YjafVYkcIa5yMvLoNCt5jBMZbdyqUsFo.png)

Solo hay una transacción pendiente de conciliar. El icono de la "lupa" ayuda de nuevo a buscar transacciones para conciliar.

Si se selecciona una transacción que casi concilia, Etendo muestra un mensaje que informa de que las transacciones no concilian completamente y, por lo tanto, puede realizarse una conciliación parcial. El usuario puede configurar a Y la propiedad 'Match Statement: hide partial match confirmation popup' en la ventana Cuenta financiera para ocultar este mensaje de confirmación en el futuro.

!!! info
    Esta última opción requerirá cerrar sesión e iniciar sesión.

![Example 7](../../../../../assets/drive/1U0DAE2Ad9SLeZF4HRRf6o_PkA8FPIk-w.png)

Esta acción concilia la línea del extracto bancario y crea una nueva línea pendiente de conciliar por la diferencia.

- el icono "desconciliar" desconcilia la transacción vinculada al registro individual. El usuario también puede seleccionar varios registros y desconciliarlos todos en un lote utilizando el botón **Desconciliar seleccionados**.

El usuario puede forzar tanto la reactivación como el procesado de conciliaciones en caso de que se haya cometido algún error, para permitir reactivar conciliaciones antiguas y poder corregir esos datos.

Este no debería ser el procedimiento estándar, ya que debería realizarse una revisión de los datos antes de validar/procesar una conciliación. En cualquier caso, los errores ocurren y, para poder resolver la situación sin un gran impacto para el usuario, ahora existen estos dos botones como funcionalidades avanzadas.

!!! info
    Este proceso impactará en el saldo inicial y el saldo final de los documentos posteriores siempre que cambie el saldo final de la conciliación que se está editando.

##### Movimientos caja-banco

La funcionalidad Movimientos caja-banco en la ventana Cuenta financiera permite el movimiento de dinero entre dos cuentas financieras diferentes dentro de una organización. Esta acción se utiliza normalmente para transferencias internas, como mover fondos desde una cuenta bancaria a una cuenta de caja menor, o entre cuentas de distintas divisas.

![Funds transfer](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions/funds-transfer.png)

Campos a tener en cuenta:

- **Fecha de la transacción**: es obligatoria. Esta fecha se utiliza para los registros que crea este proceso. Fecha de la transacción y fecha contable.
- **Depositar en**: este desplegable muestra todas las cuentas financieras que pertenecen al árbol de organización de la cuenta financiera seleccionada y que tienen habilitada la marca **Movimientos caja-banco**.
- **Concepto contable**: el valor por defecto se establece a partir de **Concepto Contable por defecto en Transferencia de Fondos** configurado en la organización de la Cuenta financiera o en su organización padre. El usuario puede sobrescribir este parámetro. Este desplegable se muestra con todos los Conceptos contables que pertenecen al árbol de organización de la cuenta financiera seleccionada.
- **Importe del depósito**: obligatorio.
- **Divisa desde**: no editable. Divisa de la cuenta financiera seleccionada.
- **Divisa hasta**: no editable. Divisa de la cuenta financiera destino.
- **Multiplicar por**: el tipo de conversión de una divisa a otra:
    - es nulo por defecto
    - se muestra solo cuando las divisas son diferentes
    - en caso de que el usuario deje este valor como nulo, el sistema utiliza el [tipo de conversión](../../general-setup/application/conversion-rates.md) configurado en el sistema para esa fecha. Si no hay nada definido, se muestra un error.
- **Comisión bancaria**: la comisión cobrada por el banco desde/hacia donde se originó/se recibió la transacción. No está marcada por defecto. Cuando se marca, se muestran dos campos más:
    - Comisión bancaria desde: para introducir el importe de la comisión correspondiente.
    - Comisión bancaria hasta: para introducir el importe de la comisión correspondiente.
- **Descripción**: por defecto, la descripción se establece como **Transacción de Movimientos caja-banco**. El usuario puede sobrescribir la descripción si fuese necesario.
#### Solapas

##### Transacción

Las transacciones de una **Cuenta financiera** pueden ser de dos tipos:

- transacciones de **Depósito** en el caso de recibir el pago de cualquier tipo de documento (factura, pedido, concepto contable o comisión)
- o transacciones de **Reintegro** en el caso de realizar un pago de cualquier tipo de documento (factura, pedido, concepto contable o comisión)

Estos dos tipos de transacción se pueden crear de tres maneras:

- **automáticamente**, si el método de pago utilizado para pagar un documento (y asignado a una cuenta financiera determinada) está configurado para ello:
    - los pagos a proveedores, una vez procesados en la ventana **Pago**, se retiran automáticamente de la cuenta financiera
    - los pagos de clientes, una vez procesados en la ventana **Cobros**, se depositan automáticamente en la cuenta financiera.
    - o los "Pagos de conceptos contables", una vez creados en **Asientos manuales**, se depositan/retiran automáticamente de la cuenta financiera.

- **en lote**, añadiendo varios pagos como transacciones a través de la ventana del proceso Añadir múltiples pagos

- o **manualmente**, creando un nuevo registro en la solapa de transacciones de la ventana de cuenta financiera.

![Transaction tab](../../../../../assets/drive/1zirkJ20dd1aVDIxtvwQeYybbNxP_tXiI.png)

- Campos a tener en cuenta en la solapa de transacciones:
    - **Tipo de Transacción:** el Tipo de Transacción indica el tipo de transacción a enviar. La solapa de transacciones también permite al usuario crear transacciones de "Depósito" o "Reintegro" basadas en un tipo de transacción de "Concepto contable" o en un "Pago".
        - Comisión bancaria
        - Depósito de tercero
        - Reintegro de tercero
    - **Fecha de la transacción:** el campo Fecha de la transacción define la fecha de la transacción que se está procesando.
    - **Fecha contable:** la fecha en la que esta transacción se registra en el libro mayor.
    - **Pago:** selector de pago.
    - **Concepto contable:** selector de concepto del libro mayor.
    - **Moneda:** indica la moneda que se utilizará al procesar este documento.
    - **Importe del depósito:** importe en el caso de recibir un pago.
    - **Importe del reintegro:** importe en el caso de realizar un pago.
    - **Dimensiones:** información de Organización, Tercero y Proyecto.
    - **Importe en moneda extranjera**: solo se muestra en vista de cuadrícula. Esta columna se rellena si el pago se recibió o se realizó en una moneda distinta de la moneda de la cuenta financiera.
    - **Moneda Extranjera**: solo se muestra en vista de cuadrícula. Esta columna se rellena si el pago se recibió o se realizó en una moneda distinta de la moneda de la cuenta financiera.

        !!! info
            Es posible permitir al usuario **recibir o realizar pagos en varias divisas** (moneda extranjera) al configurar los métodos de pago asignados a una cuenta financiera determinada. Para más información sobre esta opción, visite [Método de pago](../../financial-management/receivables-and-payables/setup.md#payment-method-configuration).

![Bank fee](../../../../../assets/drive/1hhSs7pd6WDlXjs26eC2SDsJ8vfo5kh7r.png)

1. Si es necesario crear una **Comisión bancaria**, seleccione **Comisión bancaria** en el desplegable Tipo de Transacción, introduzca una fecha de transacción y una fecha contable, y el importe **Recibido** o **Pagado**.

2. A continuación, guarde y procese la transacción.

![GL Item](../../../../../assets/drive/1C72EAORDre8_Eh44Fv-dwNc_bOlO209D.png)

Para crear una nueva transacción de concepto contable, seleccione `Depósito de tercero` o `Reintegro de tercero` en el tipo de transacción y seleccione el **Concepto contable** en el desplegable de concepto contable, introduzca una fecha de transacción y una fecha contable, seleccione un Concepto contable, introduzca el importe **Recibido** o **Pagado**, y guarde y procese la transacción.

Si el usuario necesita crear una nueva transacción de pago, se permite seleccionar un pago creado o crear un nuevo pago desde el selector de pago.

- Si el pago está creado, el usuario debe elegir el pago en el selector de pago.

    ![Payment selector](../../../../../assets/drive/1kLQZA0e7fHQtD4ZBSby4h-glL5R4DOAH.png)

Los campos descripción e importe en la solapa de transacciones se rellenarán automáticamente y, para completar la transacción, es necesario guardar y procesar.

Si es necesario crear una transacción de depósito de pago, el usuario debe hacer clic en el botón '+' en el selector de pago y se abrirá una ventana emergente de añadir pago. Debe seleccionarse "**Recibido**" en el campo "Documento".  
Esta ventana permite:

- seleccionar pagos ya creados y procesados
  - usar el campo "Cobrado de" para acotar la búsqueda de documentos a pagar
- usar el "Crédito disponible" del tercero si lo hubiera, seleccionando el crédito en la cuadrícula de crédito
- introducir el importe de "Pago real" recibido
- introducir una "Fecha de pago"
- seleccionar el "Tipo de Transacción" a pagar
- usar otros filtros como el "Nº documento" del pedido o la factura, o el "Importe desde/hasta"
- y, por último, introducir un "Pago de concepto contable" si fuera necesario, añadiendo "Conceptos contables" en una cuadrícula de conceptos contables.  
  El último paso es procesar el pago recién creado y conseguir que se deposite en la cuenta financiera.

![Payment deposit transaction](../../../../../assets/drive/1j47oaWj1O4_LLGPha7guEuKBccB3Rn0h.png)

Si es necesario crear una **transacción de reintegro de pago**, el usuario debe hacer clic en el botón '+' en el selector de pago y se abrirá una ventana emergente de añadir pago. En la ventana emergente de añadir pago, debe seleccionarse la opción "**Pagado**" en el campo "Documento". Esta ventana permite al usuario:

- seleccionar pagos ya creados y procesados
- usar el campo "A pagar a" para acotar la búsqueda de documentos a pagar
- usar el "Crédito disponible" del tercero si lo hubiera, seleccionando el crédito en la cuadrícula de crédito
- introducir una "Fecha de pago"
- seleccionar el "Tipo de Transacción" a pagar
- usar otros filtros como el "Nº documento" del pedido o la factura, o el "Importe desde/hasta"
- y, por último, introducir un "Pago de concepto contable" si fuera necesario, añadiendo "Conceptos contables" en una cuadrícula de conceptos contables.  
  El último paso es procesar el pago recién creado y conseguir que se deposite en la cuenta financiera.

![Payment withdrawal](../../../../../assets/drive/1DbaEJtPopUAIr5_S_L8g3mVOk3TQlqOT.png)

El selector de pago ha aplicado un filtro explícito (cuenta financiera actual)

![Payment filtered](../../../../../assets/drive/1DWBNx-RWSxny0gHyXIU2D-0cuKyKY5iA.png)

Es posible añadir pagos para cuentas financieras alternativas haciendo clic en el icono del embudo para limpiar los filtros.

![Payment without filter](../../../../../assets/drive/1dtzHFshO4AwVVl5S6FPHiHp9YqHgs4Hy.png)

###### Tipos de cambio

Esta subsolapa permite al usuario definir un tipo de cambio a utilizar al contabilizar la transacción de la cuenta financiera en el libro mayor cuando la moneda de la cuenta financiera no es la misma que la moneda del libro mayor.

###### Historial contable

Esta subsolapa muestra el historial contable de una transacción determinada.

![Accounting history](../../../../../assets/drive/1Bjg-OJiKl8bBeYN36lxwYnIUgtl1dbP3.png)

Como se muestra en la imagen anterior, esta solapa muestra los asientos del libro mayor creados al contabilizar/descontabilizar una transacción determinada en el libro mayor.

##### Configuración contable

La solapa de configuración contable se utiliza para definir las cuentas de un Libro mayor que se usarán al contabilizar transacciones como una comisión bancaria o un depósito.

![Accounting configuration](../../../../../assets/drive/1CYADTe8Ks-V7eoJVPSmVP8-8Ighure6S.png)

Como se muestra en la imagen anterior, las cuentas listadas a continuación se pueden configurar para una cuenta financiera y un libro mayor.

Sección **General**:

- **Cuenta de ganancias por revalorización**, esta cuenta se utiliza para abonar/cargar una ganancia por tipo de cambio:
  - La ganancia correspondiente a una disminución del tipo de cambio al realizar un pago se abona en esta cuenta.
  - La ganancia correspondiente a un aumento del tipo de cambio al recibir un pago se abona en esta cuenta.

!!! info
    Recuerde que es posible recibir pagos y realizar pagos en una moneda distinta de la moneda de la cuenta financiera.

En el caso de un tipo de **Cuenta financiera** "Caja", la cuenta del libro mayor utilizada para abonar una ganancia por tipo de cambio es la cuenta "**Beneficio por plusvalías**" de la solapa Valores por defecto de la configuración del libro mayor.

- **Cuenta de pérdidas por devaluación** utilizada para cargar/abonar una pérdida por tipo de cambio:
  - La pérdida correspondiente a un aumento del tipo de cambio al realizar un pago se carga en esta cuenta.
  - La pérdida correspondiente a una disminución del tipo de cambio al recibir un pago se carga en esta cuenta.

En el caso de un tipo de **Cuenta financiera** "Caja", la cuenta del libro mayor utilizada para abonar una ganancia por tipo de cambio es la cuenta "**Pérdida por minusvalías**" de la solapa Valores por defecto de la configuración del libro mayor.

- **Cuenta de gastos bancarios** utilizada para cargar/abonar gastos/ingresos por comisiones

La casilla de verificación **Contabilización del extracto bancario** permite al usuario contabilizar extractos bancarios. Si se selecciona, se muestran dos campos adicionales:

- **Cuenta Final**
- **Cuenta transitoria**

Dado que la contabilización de un extracto bancario es una contabilización transitoria hasta que las transacciones se hayan conciliado definitivamente, la "Cuenta transitoria" debe ser la misma cuenta que la utilizada al conciliar.

En cuanto se define una "Cuenta transitoria", el sistema muestra un aviso indicando: "When posting Bank Statements, the Bank Transitory Account should match the account used upon clearing for all payment methods in order to ensure properly balanced accounting. Do you want to propagate this value to all payment methods?"

- Si el usuario final pulsa (SÍ), el sistema rellena la Cuenta transitoria seleccionada en el campo "Cuenta de reconciliación" de las secciones "Cobros" y "Pago".

Secciones **Cobros / Pago**:

Estas secciones de la solapa de configuración contable están estrechamente relacionadas con otra solapa de la ventana de cuenta financiera, la solapa Plan de pagos.

La solapa Plan de pagos permite al usuario definir qué paso del flujo de trabajo del pago se puede contabilizar en el libro mayor. Esto se puede definir para cada método de pago asignado a la cuenta financiera

La solapa "Configuración contable" permite al usuario seleccionar las cuentas del libro mayor a utilizar al contabilizar pagos en tránsito de entrada/salida, transacciones de depósito/reintegro o conciliaciones vinculadas a un método de pago determinado.

Es importante remarcar que:

- Ninguno de los campos de la sección "**Cobros**" y "**Pago**" es obligatorio, ya que el proceso contable puede ser diferente dependiendo de la configuración del método de pago.
- Sin embargo, si alguno de esos campos está "vacío", por ejemplo la "**Cuenta de depósito**", y se ha configurado para un método de pago determinado asignado a la cuenta financiera que la transacción de "Depósito" debe contabilizarse, el proceso de contabilización generará un error.

Más en detalle:

Sección **Cobros**:

- **Cuenta de pagos en tránsito** - Esta es la cuenta que se utilizaría en el primer paso, cuando se registra el cobro en la ventana "Cobros".  
  El método de pago utilizado debe tener el valor "Cuenta de pagos en tránsito" definido en el campo "Cuenta de pago".
- **Cuenta de depósito** - Esta es la cuenta que se utilizaría para contabilizar la segunda fase, que es el "Depósito" del cobro en la Cuenta financiera. El método de pago utilizado debe tener el valor "Cuenta de depósito" definido en el campo "Depositar en".
- **Cuenta de reconciliación** - Esta es la cuenta que se utilizaría para contabilizar el tercer paso, que es la conciliación del depósito. El método de pago utilizado debe tener el valor "Cuenta de reconciliación" definido en el campo "Cuenta de reconciliación".

Sección **Pago**:

- **Cuenta de pagos en tránsito** - Esta es la cuenta que se utilizaría en el primer paso, cuando se realiza el pago en la ventana "Pago". El método de pago utilizado debe tener el valor "Cuenta de pagos en tránsito" definido en el campo "Cuenta de pago".
- **Cuenta de reintegro** - Esta es la cuenta que se utilizaría para contabilizar la segunda fase, que es el "Reintegro" del pago en la Cuenta financiera. El método de pago utilizado debe tener el valor "Cuenta de reintegro" definido en el campo "Cuenta del reintegro".
- **Cuenta de reconciliación** - Esta es la cuenta que se utilizaría para contabilizar el tercer paso, que es la conciliación del reintegro. El método de pago utilizado debe tener el valor "Cuenta de reconciliación" definido en el campo "Cuenta de reconciliación".

##### Método de pago

Esta solapa lista todos los métodos de pago asignados a la cuenta financiera. Un pago puede depositarse o retirarse de la cuenta financiera si el método de pago utilizado está asignado a la cuenta financiera.

Cada Cuenta financiera puede tener asignado más de un método de pago, métodos de pago como "Comprobación", "Transferencia bancaria", "Caja".

El hecho de asignar un método de pago o un conjunto de métodos de pago a una cuenta financiera determinada significa que es posible gestionar a través de una cuenta financiera determinada únicamente aquellos pagos vinculados a cualquiera de los métodos de pago asignados a esa cuenta financiera.

Los métodos de pago se crean y configuran en la ventana Método de pago. Una vez creados y configurados, se pueden asignar a una cuenta financiera en esta solapa. La forma de hacerlo es:

- Haga clic en la solapa '**Método de pago**' de la cuenta financiera
- Cree un nuevo registro
- En la lista desplegable '**Método de pago**', seleccione un pago.
  - Esta acción rellena automáticamente la configuración por defecto del método de pago.
- Cambie la configuración por defecto si es necesario
  - Cualquier cambio en esa configuración no cambia la configuración por defecto del método de pago porque solo se aplica a la forma en que ese método de pago se va a comportar al utilizarse para la cuenta financiera seleccionada.

En esta solapa, existe la funcionalidad avanzada (oculta por defecto) denominada **control del estado de factura pagada**; esta funcionalidad proporciona una opción de configuración para poder decidir qué estado de cada pago determina si una factura está pagada o no.

- **Combo de estado de factura pagada**: establece el estado a partir del cual se considera una factura como pagada.

Este combo se puede configurar a nivel de método de pago (cobros y pagos) en cada cuenta financiera. Por defecto, este combo se establece como **cobro recibido** o **pago realizado**, por lo tanto se obtiene el comportamiento habitual de Etendo.

!!! info
    Para información adicional sobre la configuración del método de pago, visite el artículo [_Método de pago_](../../financial-management/receivables-and-payables/setup.md#payment-method).

##### Extractos bancarios importados

La solapa lista los archivos de extracto bancario importados, así como los extractos bancarios creados manualmente.

![Imported bank statements](../../../../../assets/drive/1JYuyMUUrwVxlwti9FdfNcdz_t-DgIPY3.png)

Hay campos clave a tener en cuenta:

- **Nº documento:** es el número del extracto bancario importado, proporcionado por la secuencia de documento correspondiente.
- **Tipo de documento:** es la categoría de documento "Archivo de extracto bancario" (no "Extracto bancario").
- **Nombre:** es el nombre asignado por Etendo, que es una combinación de las fechas de transacción y la diferencia de importe de entrada/salida.
- **Fecha de importación:** es la fecha en la que se importó el archivo.
- **Fecha de la transacción:** es la fecha a utilizar al contabilizar el extracto bancario en el libro mayor.
- **Nombre archivo:** es el nombre del archivo importado

Un archivo de extracto bancario importado puede ser "**Reactivado**" ya que, una vez importado, se procesa automáticamente.

Una vez reactivado, la información de cabecera del extracto bancario, así como las líneas del extracto bancario, se pueden modificar según sea necesario.

Una vez hecho, el extracto bancario puede ser **Procesado** de nuevo.

Un extracto bancario puede contabilizarse si está habilitado en la solapa de configuración contable de la cuenta financiera.

!!! info
    Si el usuario no puede importar un archivo de extracto bancario, también es posible crear extractos bancarios y líneas de extracto bancario manualmente.

###### Líneas de extracto bancario

Esta solapa lista todas las líneas de un extracto bancario.

Hay campos clave a tener en cuenta:

- **Nombre del Tercero:** este campo muestra el nombre del tercero en las líneas del extracto bancario
- **Terceros:** este campo muestra el tercero encontrado en Etendo por el algoritmo de reconciliación, si lo hubiera
- **Concepto contable:** este campo permite introducir manualmente un Concepto contable si se sabe con certeza que una línea del extracto bancario está relacionada con una transacción de concepto contable. Etendo recordará que el texto de una línea del extracto bancario estaba relacionado con una transacción de concepto contable determinada la próxima vez que se importe un archivo de extracto bancario.  
  El concepto contable introducido aquí se utilizará entonces por el algoritmo de reconciliación al conciliar las líneas del extracto bancario con las transacciones de la cuenta financiera.
- **Importe Débito:** es el importe cargado de la línea del extracto bancario
- **Importe Crédito:** es el importe recibido de la línea del extracto bancario
- **ID de transacción:** es la transacción de la cuenta financiera una vez conciliada con la línea del extracto bancario; puede estar vacía cuando no se ha encontrado ninguna transacción coincidente
- **Tipo de relación:** puede ser "Manual" o "Automático" dependiendo de quién haya realizado la conciliación, ya sea el algoritmo de reconciliación utilizado o el usuario.

##### Reconciliaciones

La solapa de reconciliaciones muestra las conciliaciones creadas manualmente si no hay ningún algoritmo de reconciliación asignado a la cuenta financiera, así como las creadas al conciliar un archivo de extracto bancario importado en caso contrario.

###### Reconciliaciones manuales

- Como ya se ha explicado, el botón de proceso Proceso de Reconciliación permite al usuario conciliar manualmente transacciones existentes de la cuenta financiera en la ventana "**Conciliación**".
- Cada conciliación de ese tipo, una vez guardada, también se guarda en esta solapa en estado "**Borrador**" hasta que finalmente se concilia en la ventana "**Conciliación**"; por lo tanto, su estado cambia a "**Completada**".
- Es posible "**Reactivar**" una conciliación de ese tipo, por lo que puede modificarse en la ventana "**Conciliación**" y conciliarse desde esa ventana una vez más.

###### Reconciliaciones automáticas

- Del mismo modo, una vez importado un archivo de extracto bancario, las líneas del extracto bancario pueden conciliarse automáticamente en la ventana "**Conciliar usando líneas de extracto bancario importadas**", accesible desde el botón de proceso Conciliación.
- Cada conciliación de ese tipo, una vez guardada, también se guarda en esta solapa en estado "**Borrador**" hasta que finalmente se concilia en la ventana "Conciliar usando líneas de extracto bancario importadas"; por lo tanto, su estado cambia a "**Completada**".
- Es posible "**Reactivar**" una conciliación de ese tipo, por lo que puede modificarse en la ventana "**Conciliar usando líneas de extracto bancario importadas**" y conciliarse desde esa ventana una vez más.

![Reconciliations](../../../../../assets/drive/1ptaQQlAalghp30dTWFwNGupZaaGIhujf.png)

###### Contabilización de conciliaciones

Una conciliación de cualquier tipo puede contabilizarse si el método de pago utilizado al crear el pago a conciliar permite al usuario hacerlo una vez asignado a la cuenta financiera. Si no es así, Etendo muestra un aviso: "Documento deshabilitado para contabilidad".

La contabilización de una "**Conciliación de depósito**" es:

a. si el cobro recibido NO se contabilizó en la ventana **"Cobros"** y la transacción de depósito tampoco se contabilizó en la ventana "**Cuenta financiera**":

|                                                             |                |                |
| ----------------------------------------------------------- | -------------- | -------------- |
| Cuenta                                                     | Débito         | Crédito        |
| En Cuenta de reconciliación (p. ej.)                        | Importe de pago |                |
| Cobros de clientes                                          |                | Importe de pago |

b. si el cobro recibido se contabilizó en la ventana **"Cobros"** y la transacción de depósito NO se contabilizó en la ventana "**Cuenta financiera**":

|                                                             |                |                |
| ----------------------------------------------------------- | -------------- | -------------- |
| Cuenta                                                     | Débito         | Crédito        |
| En Cuenta de reconciliación (p. ej.)                        | Importe de pago |                |
| En Cuenta de pagos en tránsito (p. ej.)                     |                | Importe de pago |

c. si el cobro recibido se contabilizó en la ventana **"Cobros"** o no, y la transacción de depósito se contabilizó en la ventana "**Cuenta financiera**":

|                                                             |                |                |
| ----------------------------------------------------------- | -------------- | -------------- |
| Cuenta                                                     | Débito         | Crédito        |
| En Cuenta de reconciliación (p. ej.)                        | Importe de pago |                |
| En Cuenta de depósito (p. ej.)                              |                | Importe de pago |

!!! info
    Cada contabilización será diferente cuando el importe provenga parcial o totalmente de una deuda clasificada como dudosa. En ese caso, la contabilización será como se explica en la ventana [_Procesado del dudoso cobro_](../../financial-management/receivables-and-payables/transactions.md#doubtful-debt-run)

La contabilización de una "**Conciliación de reintegro**" es:

a. si el pago realizado NO se contabilizó en la ventana **"Pago"** y las transacciones de reintegro tampoco se contabilizaron en la ventana **Cuenta financiera**:

|                                                             |                |                |
| ----------------------------------------------------------- | -------------- | -------------- |
| Cuenta                                                     | Débito         | Crédito        |
| Pasivo del proveedor                                        | Importe de pago |                |
| En Cuenta de reconciliación (p. ej.)                        |                | Importe de pago |

b. si el pago realizado se contabilizó en la ventana **"Pago"** y las transacciones de reintegro NO se contabilizaron en la ventana **Cuenta financiera**:

|                                                             |                |                |
| ----------------------------------------------------------- | -------------- | -------------- |
| Cuenta                                                     | Débito         | Crédito        |
| En Cuenta de pagos en tránsito (p. ej.)                     | Importe de pago |                |
| En Cuenta de reconciliación (p. ej.)                        |                | Importe de pago |

c. si el pago realizado se contabilizó en la ventana **"Pago"** o no, y las transacciones de reintegro se contabilizaron en la ventana **Cuenta financiera**:

|                                                             |                |                |
| ----------------------------------------------------------- | -------------- | -------------- |
| Cuenta                                                     | Débito         | Crédito        |
| En Cuenta del reintegro (p. ej.)                            | Importe de pago |                |
| En Cuenta de reconciliación (p. ej.)                        |                | Importe de pago |

###### Informes de conciliaciones

Adicionalmente, hay dos informes que muestran información sobre cada conciliación; estos informes se pueden ejecutar desde los botones de proceso:

- Detalles de conciliaciones
- Resumen de conciliación

###### Apuntes conciliados

Esta solapa muestra las transacciones conciliadas o marcadas como conciliadas en una conciliación.

En cuanto una conciliación **manual** o **automática** se "Guarda" en estado "**Borrador**" en la solapa Reconciliaciones, esta subsolapa permite ver las transacciones conciliadas en la ventana Conciliación o conciliadas contra una línea de extracto bancario en la ventana Conciliar usando líneas de extracto bancario importadas.

No es posible eliminar los apuntes conciliados desde esta subsolapa, sino desde la ventana "Conciliación" o desde la ventana "Conciliar usando líneas de extracto bancario importadas" cuando la conciliación haya sido "**reactivada**".

La subsolapa de apuntes conciliados permite ver la siguiente información:

- la **transacción de la cuenta financiera** conciliada
- el **pago** conciliado
- la **descripción** de la transacción conciliada, por ejemplo "Nº de factura:..."
- y el **Importe del depósito** o el **Importe del reintegro** de la transacción conciliada.

##### Contabilidad

La solapa de contabilidad es una solapa de solo lectura que muestra cada contabilización de transacciones de la cuenta financiera.
### Eliminación de pagos

El objetivo de esta funcionalidad es eliminar y reactivar pagos de una forma ágil y sencilla. Además, permite eliminar y reactivar transacciones bancarias y conciliaciones.

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el bundle Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

#### Transacciones

Desde esta ventana, es posible eliminar y reactivar las transacciones incluidas en una **Cuenta financiera**.

En este caso, los pagos pueden encontrarse en los estados **Reintegro no conciliado**, **Depósito no conciliado** y **Pago conciliado**; en este último caso el pago ya está conciliado y, por tanto, relacionado con una conciliación bancaria y un extracto bancario.

Para eliminar una transacción, seleccione el registro correspondiente en la solapa **Transacción** y, a continuación, haga clic en el botón **Eliminar transacción**. Si el pago está en estado **Depósito no conciliado** o **Reintegro no conciliado**, el proceso elimina la transacción de la **Cuenta financiera** y el pago vuelve a su estado anterior. Si el estado es **Pago conciliado**, el proceso también elimina la línea de conciliación relacionada y la línea de extracto bancario relacionada.

Tenga en cuenta que:

Si la conciliación está completada y el resto de las conciliaciones existentes también están completadas, entonces la conciliación en cuestión se reabre para eliminar la línea de conciliación asociada y se cierra de nuevo.  
Si la conciliación está completada y existe una conciliación en estado **Borrador**, la conciliación en borrador se cerrará, la conciliación correspondiente se reactivará, se eliminará la línea de conciliación correspondiente, se cerrará de nuevo y la que estaba en estado **Borrador** se reactivará.

Para reactivar una transacción, seleccione el registro correspondiente en la solapa **Transacción** y, a continuación, haga clic en el botón **Reactivar transacción**. Si el pago está en estado **Depósito no conciliado** o **Reintegro no conciliado**, el pago vuelve a su estado anterior, pero permanecerá asociado a la **Cuenta financiera**. Si el estado es **Pago conciliado**, el proceso también elimina la línea de conciliación relacionada y la línea de extracto bancario relacionada.

Considere los siguientes casos:

- Si la conciliación está completada y el resto de las conciliaciones existentes están completadas, entonces la conciliación en cuestión se reabrirá para eliminar la línea de conciliación correspondiente y se cerrará de nuevo.
- Si la conciliación está completada y existe una conciliación en estado **Borrador**, la conciliación en **Borrador** se cierra, la conciliación correspondiente se reactiva, se elimina la línea de conciliación correspondiente, se cerrará de nuevo y la que estaba en estado **Borrador** se reactivará.

![](../../../../../assets/drive/1M_IDKW70W9wRHEkPK6Uw9uLvfD03wyxx.png)

#### Reconciliaciones

Es posible eliminar y reactivar conciliaciones bancarias.

Pueden darse las siguientes situaciones:

- Eliminar una conciliación en estado **Completada** o **Borrador**: en este caso se elimina la conciliación correspondiente, las líneas de extracto bancario asociadas a la misma y los pagos conciliados en ella cambian su estado a **Depósito no conciliado** o **Reintegro no conciliado**.
- Reactivar una conciliación en estado **Completada**. El resto de conciliaciones existentes también están en estado **Completada**: en este caso la conciliación se reactiva y su estado vuelve a **Borrador**.
- Reactivar una conciliación en estado **Completada**. Existe otra conciliación en estado **Borrador**: en este caso, primero se completa la conciliación en estado **Borrador** y se reactiva la conciliación seleccionada, cuyo nuevo estado será: **Borrador**.

![](../../../../../assets/drive/1ZyeE1vy7Gri5kslKF1fq1PzohDkwVPwK.png)
### Contabilización masiva

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el bundle Financial Extensions. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

La funcionalidad de Contabilización masiva permite al usuario contabilizar o descontabilizar múltiples registros seleccionando los registros correspondientes y haciendo clic en el botón **Contabilización masiva**. En el caso de la ventana "Cuenta financiera", esta opción puede utilizarse en tres solapas: Transacciones, Extractos bancarios importados y Reconciliaciones.

Además, el Estado contable del/de los registro/s se muestra en la barra de estado, en la vista de formulario, o en una columna, en la vista de cuadrícula.

!!! info
    Para más información, visite [la guía de usuario del módulo de Contabilización masiva](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).
### Liquidación avanzada de terceros

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el bundle Financial Extensions. Para ello, siga las instrucciones del marketplace: [Bundle Financial Extensions](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

Etendo permite realizar una liquidación desde una conciliación bancaria.  
Desde la ventana **Cuenta financiera**, una vez que los extractos bancarios ya han sido importados y procesados, el usuario puede seleccionar el extracto bancario desde la cuenta financiera y conciliarlo con la factura a pagar haciendo clic en el botón **Conciliación**.

![](../../../../../assets/drive/11F6-j76ebOwud3SCfJNtfFhgfuAcjh5d.png)

En la ventana emergente, Etendo muestra una lista de facturas a liquidar, cada una con su correspondiente número de factura; aquí el usuario puede seleccionar la factura correspondiente para compensar con su importe de **Pago real** a pagar.

![](../../../../../assets/drive/1GufQeDY76qDFzfshhuTzhogcH10T0zxb.png)

Desde la solapa **Factura desde compensación**, el usuario selecciona la factura que se utilizará para pagar (ya sea de venta o de compra, dependiendo de la factura elegida previamente) y establece el importe necesario de la factura a compensar.

![](../../../../../assets/drive/1nRmzMoT6EiyE2m0yvApx99cpJladJZkA.png)

Tras hacer clic en el botón **Hecho**, Etendo abre otra ventana emergente para mostrar la información de la nueva liquidación que se va a crear, para que el usuario confirme los detalles haciendo clic en **Hecho**.

![](../../../../../assets/drive/1XvbDRrKkyoporgm2uVTBDg-72m2iOOaa.png)

El registro de liquidación (cobro y pago) también se registra en la ventana **Liquidación de terceros**, donde se mostrará una línea para la factura (venta y compra) utilizada para compensar.

![](../../../../../assets/drive/1v1dM1rAImvwdfJLXtQYzzwKNH6BBALbm.png)

!!! info
    Para más información, visite la [Guía de usuario del módulo Business Partner Settlement](../../../optional-features/bundles/financial-extensions/business-partner-settlement.md).
## Ejecución de Pagos

:material-menu: `Aplicación` > `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Transacciones` > `Ejecución de Pagos`

### Visión general

El formulario **Ejecución de Pagos** permite al usuario ejecutar de forma masiva pagos en espera con estado "Pendiente de ejecución".

Lo mismo aplica a pagos que fallaron durante el proceso de ejecución debido a un atasco de papel o cualquier otro problema ocurrido por un fallo de conexión.

Existen algunas opciones de filtrado obligatorias:

- la **Organización**
- el **Método de pago**
- y la **Cuenta financiera**

!!! info
    Tenga en cuenta que el/los método/s de pago utilizado/s al recibir/realizar el/los pago/s correspondiente/s requiere/n un proceso de ejecución automática "En espera" configurado al estar asignado y configurado para una Cuenta financiera determinada.

y algunos otros filtros disponibles como:

- **Fechas Desde/Hasta** del pago
- si el pago es un "**Recibido**" o un "**Pagado**"

Una vez pulsado el botón de proceso "**Selector**", se muestran los pagos a ejecutar.

![Ejecución de Pagos](../../../../../assets/drive/1fX1GLQHOzJHloXOAJSh9X2Y_3SfXqknL.png)

Una vez pulsado el botón de proceso **"Proceso"**, se muestra una nueva ventana que permite al usuario introducir los parámetros de entrada requeridos, como por ejemplo el número de cheque, si el proceso de ejecución seleccionado en el método de pago utilizado era "Proceso simple de impresión de cheques".

Una vez pulsado el botón de proceso "Ejecutar", el pago cambia su estado a "Pago realizado/Pago recibido" o "Reintegro no conciliado/Depósito no conciliado"; por lo tanto, el siguiente pago puede procesarse y, por tanto, ejecutarse.

Tenga en cuenta que pueden seleccionarse varios pagos para ejecutarse agrupados en la misma remesa de pagos.

Si ese es el caso, más de un pago para el mismo tercero puede pagarse con el mismo número de cheque.
## Liquidación de Terceros

:material-menu: `Aplicación` > `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Transacciones` > `Liquidación de Terceros`

### Visión general

Esta funcionalidad permite al usuario crear liquidaciones para facturas, tanto de venta como de compra, desde las ventanas de **Cobros** y **Pago**. También se puede realizar una compensación creando una liquidación desde una conciliación bancaria para crédito de entrada / salida desde la ventana **Cuenta financiera**.

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}.

!!! note
    Para más información, visite [Liquidación de Terceros](../../../optional-features/bundles/financial-extensions/business-partner-settlement.md)
## Pago del impuesto

:material-menu: `Aplicación` > `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Transacciones` > `Pago del impuesto`

### Visión general

El proceso de "Pago del impuesto" ayuda a calcular el importe de los impuestos a pagar a, o a recibir de, la autoridad fiscal.

Impuestos como el IVA se liquidan como la diferencia entre:

- el IVA que una organización repercute y que pagan sus clientes, es decir, el IVA repercutido o IVA cobrado en ventas
- y el IVA que una organización paga a otras empresas por los suministros que recibe, es decir, el IVA soportado o IVA pagado en compras

El proceso de pago del impuesto puede ejecutarse una vez realizada la configuración detallada a continuación:

- Es necesario crear un tercero de tipo Autoridad Fiscal en la ventana de terceros. Este tercero debe configurarse tanto como "Cliente" como "Proveedor" porque, en ocasiones, la organización tendrá que pagar a la autoridad fiscal y, en otras, será al revés.
- Es necesario crear un concepto contable y, a continuación, vincularlo a cada Tipo de registro de impuesto. El concepto contable se utilizará para contabilizar el pago del impuesto correspondiente en el libro mayor.
  - La "**Cuenta de débito del concepto contable**" del concepto contable es la cuenta a utilizar al contabilizar un pago del impuesto a recibir de la autoridad fiscal.
  - La "**Cuenta de crédito del concepto contable**" del concepto contable es la cuenta a utilizar al contabilizar un pago del impuesto a realizar a la autoridad fiscal.
- Se vinculan tantos Tipo de registro de impuesto como sea necesario a los tipos impositivos de cada tipo, para tenerlos en cuenta en el cálculo del pago del impuesto.

#### Cabecera

La ventana de pago del impuesto permite al usuario calcular el importe de los impuestos a pagar a, o a recibir de, la autoridad fiscal dentro de un periodo de tiempo determinado. También permite al usuario generar el pago correspondiente hacia/desde la autoridad fiscal.

![Cabecera del Pago del impuesto](../../../../../assets/drive/1YLUngAGz6MvriT9nplSWvYYnkY7pMnJt.png)

Tal y como se muestra en la imagen anterior, los campos a cumplimentar son:

- **Organización**: la organización para la cual debe calcularse el pago del impuesto
- **Nombre**: el nombre del cálculo del pago del impuesto
- **Terceros**: el tercero de la autoridad fiscal que recibe el pago del impuesto o realiza el pago del impuesto.
- **Moneda**: la moneda del pago del impuesto
- **Fecha de inicio**: la primera fecha a tener en cuenta para el cálculo del impuesto.
  - Impuestos como el IVA se liquidan mensualmente; por tanto, la fecha de inicio puede ser el primer día de un mes determinado.
- **Fecha final**: la última fecha a tener en cuenta para el cálculo del impuesto.
  - Impuestos como el IVA se liquidan mensualmente; por tanto, la fecha final puede ser el último día de un mes determinado.
- **Asiento**: campo de solo lectura que enlaza con el asiento creado una vez que el pago del impuesto se procesa y, por tanto, se incluye en **Asientos manuales**.
- **Casilla Generar pago**: esta casilla permite al usuario configurar si se va a crear un cobro/pago tras procesar el pago del impuesto.
- Esta casilla no debe seleccionarse en aquellos casos en los que la autoridad fiscal deba pagar a la organización pero, en lugar de hacerlo, compense los importes a pagarle por la organización.

El botón **Crear registros de IVA** ejecuta el proceso de pago del impuesto y obtiene el importe del impuesto de cada "Tipo de registro de impuesto", que se rellena automáticamente en la solapa "Cabecera del registro de impuesto".

El botón **Proceso** procesa el pago del impuesto e incluye la contabilización de la liquidación del impuesto en **Asientos manuales**, accesible desde el campo "**Asiento**" de la ventana Pago del impuesto.

El botón "**Desprocesar**" deshace el pago del impuesto y elimina los Asientos manuales creados.

#### Cabecera del registro de impuesto

La solapa Cabecera del registro de impuesto permite al usuario ver el importe del impuesto calculado para cada "Tipo de registro de impuesto" configurado.

![Cabecera del registro de impuesto](../../../../../assets/drive/1WDw5E4PuOhtmQemNXGYCGt40woWtWUYO.png)

#### Líneas

La solapa Líneas es de solo lectura y lista todas las transacciones de impuestos relacionadas con los tipos impositivos configurados como parte de un "Tipo de registro de impuesto".

![Líneas del registro de impuesto](../../../../../assets/drive/1JAQeiows8-fzEHJq0r3TYYD6zWlzRLQ5.png)

Algunos campos relevantes a tener en cuenta son:

- **Impuesto**: el tipo impositivo incluido como parte del "Tipo de registro de impuesto".
- **Impuesto sobre factura**: la factura vinculada al tipo impositivo.
- **Fecha de la factura**: la fecha de la factura.
- **Nº documento**: el número de documento, por ejemplo, un número de factura.
- **Importe exento**: un importe exento de impuesto que no se incluirá en el pago del impuesto. La configuración se realiza en la solapa Cliente del tercero.
- **No es importe IVA**: importe que no se incluye en el cálculo del impuesto.
- **Importe no deducible**: importe que no es deducible.
- **Base imponible**: el importe imponible utilizado para el cálculo del importe del impuesto.
- **Impuestos**: el importe del impuesto.
- **Imp.total**: el importe total bruto del documento/factura.
## Remesas

:material-menu: `Aplicación` > `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Transacciones` > `Remesas`

<iframe width="560" height="315" src="https://www.youtube.com/embed/6z3t-E_sV0E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el bundle Financial Extensions. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

### Visión general

En la ventana Remesas, el usuario puede crear remesas para gestionar cobros o pagos a clientes o proveedores.

Una remesa es un grupo de pagos (cobros/pagos) o pedidos/facturas que puede remitirse al banco para su gestión. El banco gestionará entonces el cobro del dinero a los clientes o el pago a los proveedores.

### Configuración

Para poder utilizar esta funcionalidad, es necesario configurar previamente algunos aspectos.

- Dataset de Remesas: es necesario instalar el dataset de Remesas antes de utilizar la ventana Remesas.

    Para ello, vaya a la ventana *Gestión del módulo de Empresa* y seleccione el dataset correspondiente como se muestra a continuación.

    ![emm.png](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions/enterprise-module-management.png)

    !!! info
        Para más información, visite [Gestión del módulo de Empresa](../../general-setup/enterprise-model/enterprise-module-management.md).

- Tipo remesas: es necesario definir un tipo de remesa con un determinado método de pago en la ventana *Tipo remesas*.

    !!! info
        Para más información, visite [ventana Tipo remesas](../../financial-management/receivables-and-payables/setup.md#remittance-type).

- Cuenta bancaria por defecto del tercero: para cada tercero, es posible definir una cuenta bancaria que se seleccione por defecto cada vez que sea necesario crear una remesa.

    !!! info
        Para más información, visite [Cuenta bancaria](../../master-data-management/master-data.md#remittance) en la sección de Terceros.


### Ventana Remesas

![Ventana Remesas](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions/remittance-window.png)


Tal y como se muestra en la imagen anterior, es necesario completar los campos de la ventana y aparecen distintos botones para continuar con el proceso.


#### Botones

**Seleccionar pagos**

Mediante este botón, el usuario puede seleccionar un pago para incluirlo en la remesa.

**Proceso**

Mediante este botón, el usuario procesa los pagos y agrupa las líneas según las opciones mostradas en su ventana emergente correspondiente.

!!! info
    Si está instalado el módulo Automated Remittance del bundle Financial Extensions, este proceso incluye la configuración de la fecha y la liquidación de la remesa. Para más información, visite [la guía de usuario de Automated Remittance](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/automated-remittance.md).
   

**Seleccionar facturas y pedidos**

En la ventana Remesas, se muestra el botón *seleccionar facturas y pedidos*. Con este botón, el usuario puede seleccionar no solo facturas, sino también pedidos para incluirlos en la remesa. En la ventana emergente que se muestra al pulsar este botón, el usuario puede ordenar y filtrar cada columna; se muestran a la vez cobros y pagos, y se muestran conjuntamente pedidos y facturas.

![filter.png](../../../../../assets/legacy/filter.png)

**Remesa en protesta**

!!!info
    Este botón solo está disponible si está instalado el módulo Automated Remittance del bundle Financial Extensions. Para instalarlo, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}.

El botón Remesa en protesta permite la protesta automática de remesas. Esta función facilita la gestión de protestos y la re-liquidación de futuras remesas.

!!! info
    Para más información, visite [la guía de usuario de Automated Remittance](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/automated-remittance.md).

### Tipos de remesas

Existen dos tipos de remesas:

**Remesas sin descuento:** los pedidos/facturas de compra y/o los pagos (cobros/pagos) se agrupan en una remesa que se envía al banco para su gestión.

- La remesa genera una serie de pagos según la agrupación requerida por el usuario (por tercero, fecha de vencimiento, entre otros). El banco normalmente cobra un importe por la gestión de cada uno de estos pagos, de ahí el intento de agruparlos.
- El banco descuenta el importe de la remesa de la cuenta financiera en el momento en que se envía la remesa, encargándose de gestionar los pagos.

**Remesas para descuento:** los pedidos/facturas de venta y/o los pagos se agrupan en una remesa que se envía al banco. El banco adelanta el importe de la remesa y después la gestiona.

- La remesa genera tantos pagos (cobros/pagos) como los incorporados en la remesa, más uno por el importe global, que es el que se lleva a la cuenta financiera debido al adelanto de dicho importe.
- El banco informa de los pagos (cobros/pagos) que han sido liquidados (normalmente, si en un mes el banco no responde, estos pagos se consideran liquidados) y de aquellos que han sido protestados.

=== "Remesas sin descuento"
    Para crear una remesa sin descuento, siga estos pasos:

    1. Añada una nueva remesa en la ventana Remesas y seleccione “Remesa imprimible” como tipo de remesa, ya que indica que se trata de una remesa sin descuento.

        ![](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions/new-va.png)

    2. Al hacer clic en el botón “Seleccionar facturas y pedidos”, el sistema muestra una ventana emergente con, por defecto, el selector "Mostrar cobros/pagos para métodos de pago alternativos" desmarcado, mostrando únicamente las facturas que tienen el método de pago Remesas.
        Al marcar esta casilla, el sistema muestra todas las facturas y pedidos pendientes de llevar al banco. Seleccione las operaciones que necesite remesar y procese.

        ![](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions/new-va2.png)

        De este modo, el sistema inserta las líneas seleccionadas:

        ![](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions/new-va3.png)

    3. Si no se van a añadir más operaciones a la remesa, procese el pago haciendo clic en el botón "Proceso".

        !!! warning
            Al utilizar el botón "proceso" y agrupar líneas, es necesario que las cuentas bancarias de esas líneas de un documento de remesa coincidan. Si son diferentes entre sí, Etendo muestra una notificación de error como se ve a continuación.

        ![error.png](../../../../../assets/legacy/error.png)

        !!! info
            Las cuentas bancarias pueden definirse en la cabecera de las facturas de [compra](../../procurement-management/transactions.md#remittance_1) y [venta](../../sales-management/transactions.md#remittance_1), así como en los pedidos de [compra](../../procurement-management/transactions.md#remittance) y [venta](../../sales-management/transactions.md#remittance) .


    4. Al procesar, el sistema muestra las siguientes opciones:

        - Sin agrupación: genera un pago por cada una de las líneas seleccionadas.
        - Agrupar por factura: genera un pago por cada factura (en caso de que haya más de una).
        - Agrupar por factura y fecha de vencimiento: genera un pago por cada factura y fecha de vencimiento.
        - Agrupar por tercero: genera tantos pagos como terceros haya en las líneas seleccionadas. Asigna el importe total de todas las líneas que correspondan a cada tercero.
        - Agrupar por tercero y fecha de vencimiento: crea tantos pagos como terceros y fechas de pago haya en las líneas seleccionadas.
        - Agrupar por pedido: genera un pago por cada pedido (en caso de que haya más de uno).
        - Agrupar por pedido y fecha de vencimiento: genera un pago por cada pedido y fecha de vencimiento.


        ![](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions/new-va7.png)

    **Ejemplo**

    Como ejemplo, creemos el pago seleccionando la opción Agrupar por tercero.  
    Al procesar, se han creado los 3 pagos para las 3 líneas incluidas en la remesa debido a que todas ellas corresponden al mismo tercero.

    ![](../../../../../assets/drive/1-UUBayBZD-1QRbyj3yj62RmFsdw5tkE6.png)

    Al navegar al pago, se puede observar que el estado de los pagos creados es "Remitido".

    ![](../../../../../assets/drive/11-m5CC8wd0k4YLB3BjnqKq9ujwa-GJfm.png)

    Cuando la remesa se contabiliza, se obtiene un asiento contable, según las cuentas definidas.

    ##### Liquidar/Protestar remesas

    Una vez que el banco confirma los pagos correspondientes, acceda a la ventana "Liquidar/Protestar remesas" y marque las remesas liquidadas y protestadas.

    !!! info
        La fecha seleccionada es la fecha de contabilización del documento creado.

    ![](../../../../../assets/drive/1wK9U8kZzmOuxtNJAwZ02iWEgYpYRPrSN.png)

    Al liquidar la primera línea, se observa que la línea se ha añadido a la solapa de liquidadas de la remesa correspondiente.

    ![](../../../../../assets/drive/1QpvCzdNsUsa4FJBZwvJWH7YfxuapHAO4.png)

    Una vez que la remesa se contabiliza, se obtiene el asiento contable según la configuración indicada. La contabilización debe realizarse línea a línea de las transacciones liquidadas.
    Las líneas de remesa devueltas aparecerán en la solapa de devueltas.

    La contabilización de las operaciones devueltas se contabiliza del mismo modo que las operaciones liquidadas, del 401 del extracto de remesas al 400, dejando de nuevo la deuda pendiente.

    !!! info
        Las transacciones devueltas pueden gestionarse de nuevo más adelante en otras remesas o directamente en las cuentas financieras.

    El estado de las transacciones de remesa liquidadas cambia a "Reintegrado no conciliado" y, en el caso de pagos, a “Depositado no conciliado”.

    Si uno de los pagos ha sido devuelto, el estado del documento se establece en "Pendiente de ejecución".

    ![](../../../../../assets/drive/1YZ5mcnLw9KQ5KZ4svYJF9S8vrR-xuvzf.png)

    !!! info
        Es posible imprimir tanto las remesas sin descuento como las remesas para descuento desde la impresora de la barra de herramientas.

    ##### Pagos liquidados a la cuenta financiera

    !!! info
        Tras la liquidación, el sistema ha transferido automáticamente estos pagos a la cuenta financiera indicada en los pagos.

    ![](../../../../../assets/drive/1HAoN4VJmSrj-MdVzuICt4x0pKUt6_fvN.png)

    ###### Proceso de Reconciliación de pagos

    La opción Proceso de Reconciliación de pagos en cualquier proceso de remesas se refiere a la acción de comparar y ajustar los registros financieros para garantizar que los pagos se registran de forma precisa y correcta. Mediante el botón *proceso de reconciliación* en la ventana *cuenta financiera*, es posible acceder a la ventana que se muestra a continuación.

    ![](../../../../../assets/drive/1B-eqtToHww-gMuD5CldZ2fwBm2x5-OIu.png)
=== "Remesas para descuento"

    Para crear una remesa para descuento, siga estos pasos:

    1. Cree una remesa desde la ventana Remesas. Seleccione como tipo de remesa "Remesas para descuento". Una vez creada la cabecera, añada las líneas, ya sean facturas, pedidos o pagos, que se vayan a incluir en esta remesa.

        ![](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions/new-va4.png)

    2. Al hacer clic en "Seleccionar facturas y pedidos", el sistema muestra una ventana emergente con, por defecto, el selector "Mostrar cobros/pagos para métodos de pago alternativos" desmarcado, mostrando únicamente las facturas que tienen el método de pago Remesas.
        Al marcar esta casilla, el sistema muestra todas las facturas y pedidos pendientes de llevar al banco. Seleccione las operaciones que necesite remesar y procese.

        ![](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions/new-va5.png)

        El sistema inserta las líneas seleccionadas:

        ![](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions/new-va6.png)

    3. Si no se van a añadir más operaciones a la remesa, procese el pago haciendo clic en el botón "Proceso".

        !!! warning
            Al utilizar el botón "proceso" y agrupar líneas, es necesario que las cuentas bancarias de esas líneas de un documento de remesa coincidan. Si son diferentes entre sí, Etendo muestra una notificación de error como se ve a continuación.

        ![error.png](../../../../../assets/legacy/error.png)

        !!! info
            Las cuentas bancarias pueden definirse en la cabecera de las facturas de [compra](../../procurement-management/transactions.md#remittance_1) y [venta](../../sales-management/transactions.md#remittance_1), así como en los pedidos de [compra](../../procurement-management/transactions.md#remittance) y [venta](../../sales-management/transactions.md#remittance) .


    4. Al procesar, el sistema muestra las siguientes opciones:
        - Sin agrupación: genera un pago por cada una de las líneas seleccionadas.
        - Agrupar por factura: genera un pago por cada factura (en caso de que haya más de una).
        - Agrupar por factura y fecha de vencimiento: genera un pago por cada factura y fecha de vencimiento.
        - Agrupar por tercero: genera tantos pagos como terceros haya en las líneas seleccionadas. Asigna el importe total de todas las líneas que correspondan a cada tercero.
        - Agrupar por tercero y fecha de vencimiento: crea tantos pagos como terceros y fechas de pago haya en las líneas seleccionadas.
        - Agrupar por pedido: genera un pago por cada pedido (en caso de que haya más de uno).
        - Agrupar por pedido y fecha de vencimiento: genera un pago por cada pedido y fecha de vencimiento.

        En este caso, se recomienda seleccionar la opción "Sin agrupación", ya que se generarán tantos pagos como operaciones de la remesa y un pago suma de todas las operaciones, que es el que el banco adelantará. El resto de los pagos se liquidarán según se vayan conociendo.

        ![](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions/new-va7.png)

    5. El siguiente paso es llevar al banco el pago suma de las transacciones de la remesa, ya que en estos casos el banco adelanta el dinero. Desde la ventana de cuenta financiera, añada el pago a la transacción y concílielo con el extracto bancario.
      ![](../../../../../assets/drive/1jeThcgRV1wHyXRiOZpG2N-w-uuMVgAqo.png)

    6. Por último, liquide los pagos ejecutados y/o devuelva los necesarios.
      ![](../../../../../assets/drive/1ZbcAE5TCXIEo4wQU6AHrdtlhaQAVmZeC.png)
      El estado de los cobros liquidados cambió a Liquidado en remesa y el estado de los pagos totales de las operaciones de la remesa cambió a Pago conciliado.
## Dudoso cobro

:material-menu: `Aplicación` > `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Transacciones` > `Dudoso cobro`

### Visión general

Los dudosos cobros son aquellas deudas que es poco probable que la empresa pueda cobrar. Además, un dudoso cobro se convierte en un incobrable cuando ya no existe ninguna duda de que la deuda no es recuperable, por lo tanto:

- **Dudoso cobro**: derecho de cobro que podría convertirse en un incobrable en algún momento del futuro.
- **Incobrable**: derecho de cobro que se ha identificado claramente como no recuperable.

Los dudosos cobros son útiles para dotar provisiones por posibles pérdidas con antelación.

#### Historia de usuario

El siguiente ejemplo ilustra cómo Etendo gestiona la contabilización de los dudosos cobros en el libro mayor.

El cliente Healthy Food Supermarkets, Co., que debe a la empresa 1.000 EUR, está atravesando una situación difícil, por lo que su deuda se considera dudosa.

|                                     |       |        |
| ----------------------------------- | ----- | ------ |
| Cuenta                               | Debe  | Haber  |
| Cuenta de dudoso cobro              | 1000  |        |
| Deudores clientes                   |       | 1000   |

|                                               |       |        |
| --------------------------------------------- | ----- | ------ |
| Cuenta                                         | Debe  | Haber  |
| Cuenta de gastos de dudoso cobro              | 1000  |        |
| Cuenta de provisión para dudoso cobro         |       | 1000   |

El cliente Healthy Food Supermarkets, Co. realiza un cobro de 350 EUR:

|                                     |       |        |
| ----------------------------------- | ----- | ------ |
| Cuenta                               | Debe  | Haber  |
| Cuenta de pagos en tránsito         | 350   |        |
| Cuenta de dudoso cobro              |       | 350    |

|                                               |       |        |
| --------------------------------------------- | ----- | ------ |
| Cuenta                                         | Debe  | Haber  |
| Cuenta de provisión para dudoso cobro         | 350   |        |
| Cuenta de ingresos de dudoso cobro            |       | 350    |

Posteriormente, el cliente entra en quiebra, por lo que su deuda se considera incobrable:

|                                     |       |        |
| ----------------------------------- | ----- | ------ |
| Cuenta                               | Debe  | Haber  |
| Cancelaciones                       | 650   |        |
| Cuenta de dudoso cobro              |       | 650    |

|                                               |       |        |
| --------------------------------------------- | ----- | ------ |
| Cuenta                                         | Debe  | Haber  |
| Cuenta de provisión para dudoso cobro         | 650   |        |
| Cuenta de ingresos de dudoso cobro            |       | 650    |

#### Configuración

Antes de empezar a trabajar con el dudoso cobro, se requieren algunos pasos previos de configuración:

- Configurar la contabilidad para los dudosos cobros. Las cuentas que deben configurarse son:
  - Cuenta de dudoso cobro
  - Cuenta de gastos de dudoso cobro
  - Cuenta de ingresos de dudoso cobro
  - y Cuenta de provisión para dudoso cobro.
- Crear una Preferencia para poder ver el importe de una deuda que ha sido clasificada como dudosa al recibir un cobro.  
  Esta preferencia debe definirse para el Cliente y la Organización que necesite verla.  
  Esta preferencia es un atributo 'Doubtful_Debt_Visibility' cuyo valor debe ser 'Y'
- Crear un Tipo de documento para los dudosos cobros.  
  Este paso no es obligatorio, ya que ya existe un Tipo de documento estándar definido para los dudosos cobros.

#### Dudoso cobro

Los dudosos cobros se definen en la ventana Procesado del dudoso cobro. Tras su creación, aparecerá un registro en la rejilla de esta ventana.

Campos a tener en cuenta:

- **Procesado del dudoso cobro:** un enlace al Procesado del dudoso cobro que generó este Dudoso cobro
- **Programar pago de factura:** un enlace al Plan de pagos de la Factura con la que está relacionado este Dudoso cobro.
- **Importe pendiente de dudoso cobro:** Importe de dudoso cobro que permanece pendiente.

Acciones posibles:

- **Reactivar:** un Dudoso cobro puede reactivarse para poder modificarse o eliminarse posteriormente. Tenga en cuenta que, como cualquier otro documento, no puede reactivarse si está contabilizado. En ese caso, es necesario descontabilizarlo primero.
- **Contabilizar:** un Dudoso cobro puede contabilizarse, creando un asiento en el diario que debería verse así:

|                                     |                      |                      |
| ----------------------------------- | -------------------- | -------------------- |
| Cuenta                               | Debe                 | Haber                |
| Cuenta de dudoso cobro              | Importe de dudoso cobro |                   |
| Deudores clientes                   |                      | Importe de dudoso cobro |

|                                               |                      |                      |
| --------------------------------------------- | -------------------- | -------------------- |
| Cuenta                                         | Debe                 | Haber                |
| Cuenta de gastos de dudoso cobro              | Importe de dudoso cobro |                   |
| Cuenta de provisión para dudoso cobro         |                      | Importe de dudoso cobro |

#### Contabilidad

Información contable relacionada con el dudoso cobro.

### Contabilización masiva

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

La funcionalidad de Contabilización masiva permite al usuario contabilizar o descontabilizar múltiples registros seleccionando los registros correspondientes y haciendo clic en el botón **Contabilización masiva**.

Además, el estado de contabilización del/de los registro/s se muestra en la barra de estado, en la vista de formulario, o en una columna, en la vista de rejilla.

!!! info
    Para más información, visite [la guía de usuario del módulo Bulk Posting](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).
## Procesado del dudoso cobro

:material-menu: `Aplicación` > `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Transacciones` > `Procesado del dudoso cobro`

La ventana **Procesado del dudoso cobro** se utiliza para definir qué deudas, y en qué porcentaje, se consideran de dudoso cobro. Estos Dudosos cobros se muestran posteriormente en la ventana Dudoso cobro.

![Ventana Procesado del dudoso cobro](../../../../../assets/drive/1O6LI7av2TJyYTZyW8aE3gjlakxldIxhy.png)

Algunos campos a tener en cuenta:

- **Método de dudoso cobro:** si hay un Método de dudoso cobro definido, se puede seleccionar para rellenar automáticamente los campos necesarios con los valores proporcionados.
- **Días Retraso:** este campo se utiliza como filtro al seleccionar las deudas existentes. Se puede eliminar posteriormente.
- **Porcentaje:** este campo se utiliza al seleccionar las deudas existentes como el porcentaje por defecto de la deuda que se va a considerar de dudoso cobro. Se puede modificar posteriormente.

**Seleccione el dudoso cobro**. Tras rellenar los campos necesarios, se muestra el botón "Seleccione el dudoso cobro". Al hacer clic, se muestra una nueva ventana emergente para seleccionar las deudas que se van a considerar de dudoso cobro.

![Seleccione el dudoso cobro](../../../../../assets/drive/14aXYdvA41Jd2AkO4x7yD3wesdB3q0LBG.png)

En esta ventana se muestran todas las deudas pendientes, prefiltradas por los parámetros establecidos previamente. Estos filtros se pueden eliminar haciendo clic en el icono del embudo.

Cada fila representa una deuda pendiente, y es posible seleccionar tantas como sea necesario para definirlas como de dudoso cobro.

Para cada línea, es posible editar el campo **Importe de dudoso cobro**. Este es el importe que se va a considerar como de dudoso cobro. Tenga en cuenta que no es posible definir un importe de dudoso cobro mayor que el **Importe Pendiente**.

El campo **Fecha de proceso** también se puede modificar para cada fila. Al hacer clic en el botón OK, los registros seleccionados serán visibles en la solapa Dudoso cobro inferior.

**Proceso**:

Es necesario hacer clic en el botón Proceso después de seleccionar los registros para generar el/los correspondiente/s Dudoso/s cobro/s.

Una vez creados, será posible contabilizarlos o reactivarlos a través de la ventana Dudoso cobro.

#### Dudoso cobro

En esta solapa se muestran los registros seleccionados previamente. Posteriormente, será necesario procesar el Dudoso cobro para que esté disponible en la ventana Dudoso cobro.

![Rejilla de Dudoso cobro](../../../../../assets/drive/1OkWrTJKB0GNeSzk3shtcONfIEuexLMPT.png)

![Edición de Dudoso cobro](../../../../../assets/drive/1LKCMe9ihePjTcHhheD6mvtYeUls6zzKj.png)

---

Este trabajo es una obra derivada de [Gestión Financiera](http://wiki.openbravo.com/wiki/Financial_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.