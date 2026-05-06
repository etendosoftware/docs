---
tags:
  - Etendo Classic
  - Financial Management
  - G/L Journal
  - General Ledger
  - Accounting Transactions
---

# Asiento de Diario

:material-menu: `Application` > `Financial Management` > `Accounting` > `Transactions` > `G/L Journal`

## Visión General

Un asiento de diario (Libro Mayor) permite al usuario registrar asientos en el libro mayor y crear pagos de conceptos contables.

Como ya se ha explicado, la mayoría de los asientos contables se crean al contabilizar documentos como facturas de compra, facturas de venta, etc.

Los asientos contables que no corresponden a un Tipo de Documento existente deben registrarse en el libro mayor mediante un Asiento de Diario.

Además, un Asiento de Diario puede utilizarse para crear **Pagos de Concepto Contable** o pagos no relacionados con pedidos o facturas.

!!! info
    Esta funcionalidad es muy útil al registrar la nómina de los empleados en el libro mayor, ya que el pago de la nómina puede crearse al mismo tiempo.


Por último, un Asiento de Diario también puede configurarse como **plantilla**.

Esta funcionalidad permite al usuario crear los mismos asientos que los contenidos en el Asiento de Diario configurado como plantilla.

Esta funcionalidad también es muy útil al registrar la nómina de los empleados, por ejemplo.

### Lote

Un lote de asientos de diario permite al usuario agrupar asientos de diario de características similares que pueden procesarse todos al mismo tiempo.

![](../../../../../../assets/drive/1dR_rouWq3IFHDFHv_CBfLdywl7lBkLQz.png)

Como se muestra en la imagen anterior, un *lote de asientos de diario* puede contener los siguientes datos:

-   el **período contable**
-   la **fecha contable**
-   y la **moneda**

Ninguno de los datos anteriores es obligatorio en este punto, ya que un asiento de diario puede contener varios diarios con diferentes períodos y fechas contables. Lo mismo se aplica a la moneda, ya que un asiento de diario puede contener varios diarios de distintas configuraciones de libro mayor general.

Una vez creado y guardado un lote, es posible crear tantos Asientos de Diario como se requiera, que una vez listos pueden completarse y procesarse al mismo tiempo como un lote **único**.

Un asiento de diario y, por tanto, su contenido puede configurarse como **Plantilla**; esa plantilla puede utilizarse posteriormente al crear un nuevo asiento de diario mediante el botón de proceso **Copiar Líneas** tal como se describe en la siguiente sección.

##### Asiento de Diario configurado como "Plantilla"

Como ya se ha mencionado, un Asiento de Diario y, por tanto, su contenido puede configurarse como **Plantilla**. Para ello, es necesario seguir los pasos que se describen a continuación:

**1.** **Crear un asiento de diario** para contabilizar la nómina del empleado correspondiente al período de enero de 2022, por ejemplo. Ese Asiento de Diario debe marcarse como **Plantilla**.

**2.** Crear un **nuevo asiento de diario** para contabilizar la nómina del empleado correspondiente al período de enero de 2022. Introduzca una **Fecha Contable** y un **Período**:

![](../../../../../../assets/drive/1FoRVJ89HIyQt4zO2WhyYkSm3riRyKGpx.png)

**3.** Presione el botón de proceso **Copiar Detalles**.

Se muestra una nueva ventana con todas las plantillas disponibles:

![](../../../../../../assets/drive/1xUX_ZaY1POd69AUGYWN2FCf6Bjx7_-F9.png)

!!! info
    Tenga en cuenta que es posible buscar una plantilla utilizando el número de documento del asiento de diario configurado como plantilla y los campos de descripción.

**4.** **Seleccione una plantilla y haga clic en Aceptar**. Después de esto, Etendo rellena el Asiento de Diario creado más recientemente con los mismos asientos; solo las fechas son diferentes.

Puede ser necesario cambiar los importes de los asientos. Para ello, es posible editar las Líneas del Asiento de Diario y modificar los importes.

El último paso es contabilizar el Asiento de Diario, de modo que los asientos correspondientes se registren en el libro mayor.

## Cabecera

Una cabecera de asiento de diario puede incluir diarios, que pueden contener varias líneas de asiento.

![](../../../../../../assets/drive/137QIrGJeaxPlR9pTnhh0delXq_Xwqt0y.png)

Una cabecera de Asiento de Diario contiene los siguientes datos:

-   La organización y la configuración del Libro Mayor General de la organización que, una vez seleccionada, establece por defecto el campo **Moneda** con la de la configuración del libro mayor general, por ejemplo USD. Sin embargo, la moneda puede cambiarse a EUR, por ejemplo. Etendo aplicará la tasa de conversión EUR -> USD correspondiente, ya que el registro en el libro mayor debe realizarse en USD.
-   La *fecha del documento*, que no tiene que ser la misma que la fecha contable.
    La fecha del documento se rellena automáticamente con la fecha actual por defecto, pero siempre puede cambiarse.
-   El *período contable* y la *fecha contable* dentro de ese período. Estas fechas pueden rellenarse automáticamente con los valores introducidos en el lote del diario, si lo hubiera; sin embargo, siempre pueden cambiarse.

Existe una casilla de verificación denominada ***Apertura*** que puede marcarse simplemente para indicar que un diario contiene **asientos de saldo de apertura de cuentas.**

Existe una **lista de acciones** que pueden ejecutarse desde la cabecera del Asiento de Diario:

-   El botón **Copiar Detalles** permite al usuario copiar los asientos de un diario configurado como ***Plantilla*** al diario actual.
-   El botón **Completar** permite al usuario completar el Asiento de Diario una vez introducidas las líneas de diario correspondientes, siempre que el importe total del debe coincida con el importe total del haber.
-   El botón **Contabilizar/Descontabilizar** permite al usuario Contabilizar/Descontabilizar un Asiento de Diario una vez completado.
-   El botón **Cerrar** permite al usuario cerrar un Asiento de Diario para el que no se requiere ninguna otra acción, o reactivarlo si no está ya contabilizado.
-   El botón **Procesar Lote** completa el/los Asiento/s de Diario del lote.

!!! info
    Tenga en cuenta que al **completar un Asiento de Diario, se creará un pago de **Concepto Contable**** para cada línea de diario que tenga marcada la casilla **Partidas Abiertas**, tal como se explica en la sección de creación de pagos de concepto contable.


!!! info
    El Diario se completará aunque falle la creación de alguno de los Pagos. En este caso, se muestra un mensaje de error indicando las Líneas que intentaron crear un Pago pero fallaron.


## Líneas

La solapa de líneas permite al usuario introducir los asientos del diario, así como la información relacionada con el pago del concepto contable.

### Contabilidad

Información contable relacionada con el Asiento de Diario.

## Asiento de Diario Diferido
### Duplicar Asientos de Diario

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el paquete Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el núcleo y nuevas funcionalidades, visite [Financial Extensions - Notas de versión](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

<iframe width="560" height="315" src="https://www.youtube.com/embed/K7XOBkmRLAQ?si=l-p9u_IvzFmMc46F" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Esta funcionalidad permite al usuario duplicar un asiento de diario tantas veces como sea necesario, indicando la regularidad y el período en que se debe realizar la primera copia. A partir de la segunda copia, la duplicación tendrá lugar con la regularidad correspondiente.
A continuación se muestra el proceso para crear un asiento de diario desde cero y duplicarlo posteriormente.

1- Acceda a la ventana "Asiento de Diario" y cree una cabecera:

![](../../../../../../assets/drive/1O9MpaLX0Ewh-OI8GW3z1h8E9ERRqoOQ4.png)

2- Cree un nuevo registro:

![](../../../../../../assets/drive/1mxbJexaQrgCCMkvjYdJILcAmCb8Y8ohF.png)

3- Cree las líneas (a registrar) y complete el asiento. Una vez realizados estos tres pasos, el botón "Crear Plan Diferido" se mostrará en el margen superior derecho.


![](../../../../../../assets/drive/194RVxWW4vIWYQVLBrgYBi2P8ADNOH0bR.png)

4 - Haga clic en el botón y se mostrará una ventana emergente con tres campos:
• Tipo de Plan de Gasto: regularidad de las copias.
    • Número de Períodos: número de copias requerido.
    • Período: período en el que se realizará la primera copia.


![](../../../../../../assets/drive/1cwaYerXmbWqaJu5HXlH8-yoaxvrf5935.png)

5 - Una vez introducida esta información, haga clic en el botón "Listo" y se generarán tantos registros como el número de copias indicado.

![](../../../../../../assets/drive/1jJr_ZWLzgVbkF1mXz835JWRVBQhQcJ_l.png)


Por defecto, esta funcionalidad solo está disponible para la ventana "Asiento de Diario", ya que las copias de registros se agrupan bajo una única cabecera. También es posible duplicar estos asientos en el "Asiento de Diario Simple" solo si hay una preferencia configurada en la ventana "Preferencia" con la propiedad "Mostrar Botón Crear Plan Diferido" y el valor "Y".

![](../../../../../../assets/drive/1CMGcvXoHxCcfYwskpj4OOwC_XBaPWDG0.png)

Una vez configurada esta preferencia, el botón se habilitará en el "Asiento de Diario Simple". El flujo es el mismo, pero las copias duplicadas no se crearán bajo una cabecera. Es decir, esta información no se mostrará en la ventana "Asiento de Diario", excepto si la información a copiar ya se encuentra en ella, en cuyo caso se mostrará.

![](../../../../../../assets/drive/1RflwaoqNOmVWf7b6_Bo5MFeO_KlJqg1-.png)

## Reversión de Asiento de Diario

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el paquete Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el núcleo y nuevas funcionalidades, visite [Financial Extensions - Notas de versión](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

Esta funcionalidad es especialmente útil para empresas que realizan un cierre mensual, en lugar de un cierre de año, pero con pagos pendientes (entrantes o salientes). Permite al usuario abrir o cerrar el período sin tener en cuenta los pagos hasta que se realicen.

Para utilizar esta funcionalidad, tanto en las ventanas "Asiento de Diario" como en "Asiento de Diario Simple", el usuario puede hacer clic en el botón "Revertir Asiento" en la barra de herramientas al seleccionar un asiento.

![](../../../../../../assets/drive/185JazYlxodMfPSx-2B4RgVe9UVadeUks.png)

De esta manera, Etendo crea automáticamente un asiento de reversión que compensa el importe en las columnas de haber y debe.
>
!!! note
    Por defecto, el documento de reversión se crea como borrador. Por eso Etendo muestra la opción "procesar documento" al hacer clic en el botón "Revertir Asiento". De esta manera, el usuario puede completar el documento.

Como se puede observar a continuación, Etendo muestra una notificación de éxito en verde con el nuevo número de Asiento de Diario.

![](../../../../../../assets/drive/1QAaLd-Rkiay5X6sKozqV80H7ykVoes53.png)

Al comparar el Asiento de Diario original con el Asiento de Diario de reversión, las columnas de debe y haber muestran la compensación, ya que los importes están invertidos.

##### Asiento de Diario original

![](../../../../../../assets/drive/1l7-FyYg87NhJheS_L7GTATeJsvvoA41K.png)

##### Asiento de Diario de Reversión

![](../../../../../../assets/drive/1tZDhsR7UlZUz7itZlxDBVouv9QHIj-_G.png)


Esto resulta útil para distinguir entre el asiento de diario original y el de reversión.

## Contabilización Masiva

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el paquete Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el núcleo y nuevas funcionalidades, visite [Financial Extensions - Notas de versión](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

La funcionalidad de Contabilización Masiva permite al usuario contabilizar o descontabilizar múltiples registros seleccionando los registros correspondientes y haciendo clic en el botón **Contabilización Masiva**.

Además, el Estado de Contabilización del/los registro/s se muestra en la barra de estado, en vista de formulario, o en una columna, en vista de grilla.
>
!!! info
    Para más información, visite [la guía del usuario del módulo Contabilización Masiva](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).

---

This work is a derivative of [Financial Management](http://wiki.openbravo.com/wiki/Financial_Management){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
