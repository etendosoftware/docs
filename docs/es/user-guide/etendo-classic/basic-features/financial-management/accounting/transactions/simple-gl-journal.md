---
tags:
  - Etendo Classic
  - Financial Management
  - Simple G/L Journal
  - GL Journal
  - Accounting Transactions
---

# Asiento de Diario Simple

:material-menu: `Application` > `Financial Management` > `Accounting` > `Transactions` > `Simple G/L Journal`

## Visión General

En Etendo existe una ventana de Asiento de Diario que permite al usuario introducir manualmente asientos de diario en el sistema. Esta ventana tiene tres solapas (Lote, Cabecera y Líneas) y, en algunos casos, esto puede resultar complicado para el usuario, ya que podría ser suficiente con solo dos niveles (Cabecera y líneas). Otro inconveniente de esta ventana es que solo se pueden seleccionar esquemas contables, por lo que al contabilizar el asiento de diario solo hay una entrada en la tabla fact\_Acct.

##### Ventajas del Asiento de Diario Simple

-   Es una ventana más sencilla, ya que no es necesario introducir un lote. Hay un nivel menos de entrada de datos.
-   Es más sencillo buscar asientos de diario. Sin el nivel de lote, es posible buscar directamente asientos específicos.
-   En esta ventana es posible ver asientos de diario que se han creado utilizando la ventana Asiento de Diario, por lo que también es posible buscar asientos de diario en ella.

## Cabecera

Una cabecera de asiento de diario puede incluir diarios, que pueden contener varias líneas de asiento.

Campo importante a destacar:

-   *Multi-libro mayor*: un indicador.
    -   Si no está marcado, a partir de ese momento se muestra el campo Libro Mayor.
    -   Si está marcado, el sistema no mostrará el campo Libro Mayor y no se tendrá en cuenta para las siguientes operaciones.

## Líneas

La solapa de líneas permite al usuario introducir los asientos del diario, así como la información relacionada con el pago del concepto contable.

Un campo a destacar:

-   Concepto Contable: desplegable donde se muestran todos los Conceptos Contables. Tiene una visualización lógica y solo se muestra cuando **Multi-libro mayor** está marcado en la cabecera.

!!! info
    Si **Multi-libro mayor** no está marcado, en su lugar se muestra el campo Cuenta.


### Contabilidad

Información contable relacionada con el Asiento de Diario.

Al Contabilizar la Cabecera:

-   Todos los asientos contables se crean con combinaciones de cuentas (Cuenta) o concepto contable. No puede haber líneas mixtas.
-   Si **Multi-Libro Mayor** está:
    -   No marcado: solo puede seleccionar cuentas que pertenezcan a un único esquema contable (definido en la cabecera), por lo que al contabilizar el documento habrá un único asiento de diario. Este comportamiento no cambiará. El proceso de contabilización es exactamente igual que en la ventana Asiento de Diario.
    -   Marcado: el usuario selecciona Conceptos Contables y, dado que puede tener diferentes combinaciones válidas al contabilizar el documento, tendrá tantas entradas como cuentas distintas en las que esté definido el concepto contable y la organización definida en la cabecera.

### Tipos de Cambio

La solapa de tipos de cambio permite al usuario introducir un tipo de cambio entre la moneda del libro mayor general de la organización y la moneda del Asiento de Diario, que se utilizará al contabilizar el Asiento de Diario en el libro mayor.

!!! info
    Esta solapa solo se mostrará cuando Multi-Libro Mayor esté habilitado.

## Reversión de Asiento de Diario

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el paquete Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el núcleo y nuevas funcionalidades, visite [Financial Extensions - Notas de versión](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

Esta funcionalidad es especialmente útil para empresas que realizan un cierre mensual, en lugar de un cierre de año, pero con pagos pendientes (entrantes o salientes). Permite al usuario abrir o cerrar el período sin tener en cuenta los pagos hasta que se realicen.

Para utilizar esta funcionalidad, tanto en las ventanas "Asiento de Diario" como en "Asiento de Diario Simple", el usuario puede hacer clic en el botón "Revertir Asiento" en la barra de herramientas al seleccionar un asiento.

![](../../../../../../assets/drive/185JazYlxodMfPSx-2B4RgVe9UVadeUks.png)

De esta manera, Etendo crea automáticamente un asiento de reversión que compensa el importe en las columnas de haber y debe.
>
!!! info
    Es importante tener en cuenta que, por defecto, el documento de reversión se creará como borrador. Por eso Etendo muestra la opción "procesar documento" al hacer clic en el botón "Revertir Asiento". De esta manera, el usuario puede completar el documento.

Como se puede observar a continuación, Etendo muestra una notificación de éxito en verde con el nuevo número de Asiento de Diario.

![](../../../../../../assets/drive/1QAaLd-Rkiay5X6sKozqV80H7ykVoes53.png)

Al comparar el Asiento de Diario original con el Asiento de Diario de reversión, las columnas de debe y haber muestran la compensación, ya que los importes están invertidos.

##### Asiento de Diario original

![](../../../../../../assets/drive/1l7-FyYg87NhJheS_L7GTATeJsvvoA41K.png)

##### Asiento de Diario de Reversión

![](../../../../../../assets/drive/1tZDhsR7UlZUz7itZlxDBVouv9QHIj-_G.png)

### Opción de cambio de descripción en la ventana Asiento de Diario Simple

Si el asiento de diario se crea en la ventana Asiento de Diario Simple, el usuario puede cambiar la descripción del asiento de diario, una vez que hace clic en el botón "Revertir Asiento", en la ventana emergente correspondiente.

![](../../../../../../assets/drive/1Uec9_qgFGGKWDLNsWvN7CZDwuQXAjp0J.png)

Esto resulta útil para distinguir entre el asiento de diario original y el de reversión.

## Contabilización Masiva

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el paquete Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el núcleo y nuevas funcionalidades, visite [Financial Extensions - Notas de versión](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

La funcionalidad de Contabilización Masiva permite al usuario contabilizar o descontabilizar múltiples registros seleccionando los registros correspondientes y haciendo clic en el botón **Contabilización Masiva**.

Además, el Estado de Contabilización del/los registro/s se muestra en la barra de estado, en vista de formulario, o en una columna, en vista de grilla.
>
!!! info
    Para más información, visite [la guía del usuario del módulo Contabilización Masiva](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).

## Clonado de Asiento de Diario

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el paquete Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el núcleo y nuevas funcionalidades, visite [Financial Extensions - Notas de versión](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

Con esta funcionalidad, el usuario puede clonar fácilmente un asiento seleccionado. Esta función no solo duplica el asiento, sino que también crea una descripción detallada que incluye el número de pedido original.

Para ello, seleccione el registro a clonar y haga clic en el botón copiar registro de la barra de herramientas.

![](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/transactions/gljournalclone.png)

De esta manera, se genera una copia del registro original, incluyendo una descripción y un número de copia, como se muestra a continuación.

![](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/transactions/gljournalclone2.png)

Esta funcionalidad mejora la eficiencia en la gestión de asientos de diario, facilitando la replicación y el registro preciso de transacciones.

---

This work is a derivative of [Financial Management](http://wiki.openbravo.com/wiki/Financial_Management){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
