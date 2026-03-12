---
title: Gestión Financiera - Activos
tags:
    - Activos
    - Amortización
    - Categoría de Activos
    - Dimensiones contables de Activos
---

# Gestión Financiera - Activos

## Visión general

Esta sección describe las ventanas relacionadas con los activos, parte de la Gestión Financiera en Etendo. Estas son:

[:material-file-document-outline: Activos](#activos){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Categoría de Activos](#categoría-de-activos){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Amortización](#amortización){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Informe de amortización de activos (Excel)](#informe-de-amortización){ .md-button .md-button--primary } <br>


## Activos

:material-menu: `Aplicación` > `Gestión Financiera` > `Activos` > `Activos`

### Visión general

El usuario puede definir los activos propiedad de la empresa y configurar sus características de amortización. 

### Ventana Activos

![](../../../../../assets/drive/1SggpQOnJ2aCqlJS7Ds8KulWXK1pCaoKR.png)

Campos a tener en cuenta:

-   **Organización** : Entidad organizativa dentro del cliente.
-   **Identificador** : Un método rápido para encontrar un registro en particular.
-   **Nombre** : Un identificador no único para un registro/documento, a menudo utilizado como herramienta de búsqueda.
-   **Grupo de activos** : Una clasificación de activos basada en características similares definidas en la [ventana Categoría de Activos](#ventana-categoría-de-activos). Los campos de configuración se completarán automáticamente según las características definidas en esta ventana. 
-   **Nº de documento** : Un identificador generado automáticamente para todos los documentos.
-   **Descripción** : Un espacio para escribir información adicional relacionada.
-   **Moneda** : Un medio aceptado de intercambio monetario que puede variar entre países.
-   **Producto** : Un artículo producido por un proceso.
-   **Nivel agrupación** : Cuando está marcado, agrupa otros activos y los muestra en vista de árbol. 
-   **Estático** : Evita mover el registro a la vista de árbol.
-   **Amortizar** : El activo se utiliza internamente y se amortizará.
-   **Tipo de amortización** : Lineal. Indica el método utilizado para amortizar este activo.
-   **Tipo de cálculo** : Indica cómo se calculará la amortización: Tiempo (mensual o anual) o Porcentaje (anual).
-   **% anual amortización** : Porcentaje anual de amortización.
-   **Amortizar** : Planificación del activo.
-   **Vida útil - Años** : Años de vida útil del activo.
-   **Vida útil - Meses** : Meses de vida útil del activo.
-   **Cada mes es de 30 días** : Si está marcado, calcula el plan de amortización considerando cada mes como un mes de 30 días y los años de 365 días. Si no está marcado, considera los días reales de cada mes y los años bisiestos.
-   **Fecha compra** : Fecha de compra.
-   **Fecha baja** : Fecha de fin de vida útil.
-   **Fecha inicio** : Fecha de inicio de la amortización. El plan de amortización se calculará a partir de esta fecha.
-   **Fecha fin** : Fecha de fin de la amortización.
-   **Valor del activo** : Valor del activo.
-   **Valor residual** : Importe del valor residual del activo.
-   **Importe de amortización** : Importe de amortización.
-   **Importe amortizado previamente** : Este importe se resta del importe de amortización al calcular el plan de amortización. Importe total a amortizar = Importe de amortización - Importe amortizado previamente
-   **Amortizado real** : Valor amortizado.
-   **Proyecto** : Identificador de un proyecto definido dentro del módulo Project & Service Management.

#### Botones

- **Crear amortización**: El botón Crear amortización completa la solapa Amortización de activos. Crea el plan de amortización en base a la definición del activo.

- **Recalcular amortización**: El botón Recalcular amortización permite al usuario actualizar la información cuando sea necesario. 

### Solapa Amortización de activos

Las amortizaciones del activo para un activo seleccionado se añaden en esta solapa. 

![](../../../../../assets/drive/167vATAwJuJhpPE2by-QgZN1_jyrDsyWZ.png)

-   **Nivel** : Una línea que indica la posición de esta solicitud en el documento.
-   **Amortización** : La amortización o reducción del valor de un producto a lo largo del tiempo.
-   **% Amortización** : Porcentaje de amortización
-   **Importe a amortizar** : Importe de amortización
-   **Moneda** : Un medio aceptado de intercambio monetario que puede variar entre países.

La solapa Amortización de activos muestra el plan de amortización del activo en base a su vida útil y su valor, que es el importe a amortizar. El valor del activo se divide a lo largo de su vida útil (meses o años), por lo tanto cada línea del plan de amortización representa un porcentaje del importe total de amortización del activo.

!!! note
    Es importante remarcar que las líneas del plan de amortización propuesto pueden eliminarse manualmente siempre que no estén procesadas y contabilizadas. En ese caso, el proceso de crear amortización puede ejecutarse nuevamente, por lo tanto el plan de amortización se recalcula. Esto es muy útil en aquellos casos en los que el valor de un activo cambia o la vida útil de un activo cambia una vez que su amortización ha comenzado.

Sin embargo, existe una restricción al eliminar líneas si el usuario planea hacer clic en el botón Recalcular amortización después. Las líneas deben eliminarse siempre comenzando por la última y sin dejar líneas sin eliminar entre medias. Por ejemplo, teniendo líneas de amortización como:

-   Línea 10 - línea del plan de amortización de enero
-   Línea 20 - línea del plan de amortización de febrero
-   Línea 30 - línea del plan de amortización de marzo

La línea de amortización de febrero no puede eliminarse hasta que se elimine la línea de amortización de marzo.

El proceso asume que si existe la línea de amortización de marzo, entonces existe la línea de amortización de febrero.

### Solapa contabilidad

El usuario puede crear y editar cuentas de mayor para ser utilizadas en transacciones que incluyan un activo seleccionado.

![assets3](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/assets/assets3.png)

- **Esquema contable**: El libro que contiene todas las transacciones financieras registradas para la entidad legal.
- **Amortización acumulada**: Cuenta de amortización acumulada. 
- **Amortización**: Cuenta de amortización.

Las cuentas mostradas están configuradas por defecto y pueden modificarse. 

### Dimensiones contables de Activos

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Financial Extensions Bundle. 
    Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}.
    Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite
    [Financial Extensions - Notas de la versión](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

Además de las dimensiones de Producto existentes para los activos, este módulo permite a los usuarios seleccionar **dimensiones contables adicionales** que 
se transferirán automáticamente a las líneas de amortización, permitiendo una mejor integración con los procesos contables. 

Las dimensiones que el usuario puede aplicar al proceso de creación del activo son las siguientes: 

- **Terceros**
- **Proceso**
- **Usuario1**
- **Usuario2** 
- **Zona de venta**
- **Campaña**
- **Centro de costos**

!!! info
    Al crear o recalcular la planificación de amortización de un activo, las dimensiones contables especificadas se transfieren a las líneas de la planificación de amortización.

![assets1](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/assets/assets1.png)

!!! info
    Para más información sobre la configuración de Dimensiones, visite [Dimensiones](../../../../etendo-classic/basic-features/financial-management/accounting/setup/general-ledger-configuration.md#dimension-tab).

#### Botones 

- **Crear amortización**: El botón Crear amortización genera las líneas de amortización en la solapa Amortización de activos relacionadas con el activo seleccionado. Además, estas mismas líneas se añaden en la ventana Amortización, agrupándolas únicamente según el **periodo de amortización** (mensual o anual) en caso de tipo de cálculo (tiempo) e incluso anual para el tipo de cálculo (porcentaje).
 

## Categoría de Activos

:material-menu: `Aplicación` > `Gestión Financiera` > `Activos` > `Categoría de Activos`

### Visión general

Los activos pueden agruparse en diferentes categorías con el objetivo de ayudar a su gestión y análisis de amortización.

### Ventana Categoría de Activos 

La ventana Categoría de Activos permite al usuario crear y configurar cada categoría de activos que su organización pueda necesitar.

![](../../../../../assets/drive/17CmG5FAA86HDWLrAmjuHIgpNsdwAn_ya.png)

Como se muestra en la imagen anterior, la creación de una categoría de activos requiere que el usuario introduzca la siguiente información para cada categoría:

-   **Nombre** o nombre corto que ayuda a encontrar fácilmente una categoría.
-   **Descripción** un espacio para escribir información adicional relacionada.
-   **Amortizar** indica si los activos de este grupo se amortizarán.
-   **Tipo de amortización** Lineal. Indica el método utilizado para amortizar este activo.
-   **Tipo de cálculo** indica cómo se calculará la amortización: Tiempo (mensual o anual) o Porcentaje (anual).
-   **Amortización anual** Porcentaje anual utilizado para amortizar este activo.
-   **Amortizar** se refiere a los periodos elegidos entre asientos de amortización (mensual, anual).
-   **Vida útil - Meses** Años de vida útil del activo.
-   **Vida útil - Años** Meses de vida útil del activo.

La configuración de amortización se heredará de la categoría de activos al crear un nuevo activo desde la ventana Activos.

### Solapa contabilidad

Cada categoría de activos permite al usuario configurar un conjunto diferente de cuentas a utilizar para contabilizar la amortización del activo.

![](../../../../../assets/drive/1jZl_RGgZw2i1Ogq4d1D-fhNcd59AI6ev.png)

## Amortización

:material-menu: `Aplicación` > `Gestión Financiera` > `Activos` > `Amortización`

### Visión general

En la ventana Amortización, se registran las amortizaciones de activos, agrupadas por fecha. Además, desde esta ventana, estos registros se procesan y se contabilizan en el libro mayor.

### Ventana Amortización

Desde la cabecera, se crean amortizaciones para periodos concretos.

![assets4](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/assets/assets4.png)


Campos a tener en cuenta: 

- **Organización**: Entidad organizativa dentro del cliente.
- **Nombre**: Un identificador no único para un registro/documento, a menudo utilizado como herramienta de búsqueda.
- **Descripción**: Un espacio para escribir información adicional relacionada.
- **Fecha contable**: La fecha en la que el activo debe contabilizarse.
- **Fecha de inicio**: Fecha a partir de la cual comienza la amortización. 
- **Amortización total**: Importe de amortización. 
- **Moneda**: Un medio aceptado de intercambio monetario que puede variar entre países.
- **Proyecto**: Identificador de un proyecto definido dentro del módulo Project & Service Management.

### Solapa Líneas

Cada línea muestra los activos amortizados y los detalles de la amortización.

![assets5](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/assets/Assets5.png)


Campos a tener en cuenta: 

- **Nivel**: Indica la línea única para un documento. 
- **Activos**: El activo a amortizar.
- **% Amortización**: Porcentaje de amortización (calculado por Tiempo o Porcentaje).
- **Importe a amortizar**: Importe de amortización.
- **Moneda**: Indica la moneda que se utilizará al procesar este documento.
- **Proyecto**: Identificador de un proyecto definido dentro del módulo Project & Service Management.

### Solapa contabilidad

Información contable relacionada con la amortización una vez que el documento está contabilizado.

Campos a tener en cuenta: 

- **Fecha contable**: La fecha en la que esta transacción se registra en el libro mayor. Esta fecha también indica a qué periodo contable dentro del ejercicio fiscal pertenecerá esta transacción.
- **Cuenta**: La cuenta utilizada. 
- **Débito contabilizado**: El importe del débito de la cuenta indica el importe de la transacción convertido a la moneda contable de esta organización.
- **Crédito contabilizado**: El importe del crédito de la cuenta indica el importe de la transacción convertido a la moneda contable de esta organización.

![assets6](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/assets/assets6.png)

!!!info 
    Para más información sobre la funcionalidad de Cuenta financiera, visite [Cuenta financiera](../../../basic-features/financial-management/receivables-and-payables/transactions.md#financial-account).

### Dimensiones contables de Activos

<iframe width="560" height="315" src="https://www.youtube.com/embed/1a1UNCnNNcI?si=DbicgZnWjtmkScDh" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}.Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).


Este módulo permite que, en la ventana Amortización, a diferencia de la operativa estándar en la que las amortizaciones de activos se agrupaban según fechas específicas, se agrupen los registros de amortización **solo por periodos** (mensual o anual) en caso de tipo de cálculo (tiempo) e incluso anual para el tipo de cálculo (porcentaje). Además, en la agrupación no se consideran las dimensiones.
Adicionalmente, las dimensiones contables se mantienen en las líneas de amortización para ser utilizadas en la generación de asientos contables.

![assets2](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/assets/assets2.png)


### Contabilización masiva

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

La funcionalidad de Contabilización masiva permite al usuario contabilizar o deshacer la contabilización de múltiples registros seleccionando los registros correspondientes y haciendo clic en el botón **Contabilización masiva**.

Además, el Estado contable del/de los registro/s se muestra en la barra de estado, en vista de formulario, o en una columna, en vista de rejilla.
> 
!!! info
    Para más información, visite [la guía de usuario del módulo Bulk Posting](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).

## Cómo reactivar amortizaciones

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

Etendo permite procesar y desprocesar múltiples amortizaciones. Este proceso está disponible para amortizaciones que comparten el mismo estado. El estado de la amortización puede verse en la barra de estado.  

![](../../../../../assets/drive/1je7Yl7FTqlDAhFlb8wTQKBDUF3pSn0Qu.png)


## Informe de amortización de activos (Excel)

:material-menu: `Aplicación` > `Gestión Financiera` > `Activos` > `Informe de amortización de activos (Excel)`

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

El informe de amortización permite descargar informes en Excel. El informe puede encontrarse en Gestión Financiera > Activos > Herramientas de análisis > Informe de amortización de activos. 

![](../../../../../assets/drive/FCyjH9Cqjoxlpce_Q2Adrf0qcnEwMumykLuNZ5DvkPgw5L1GNfFz4EDeMvEQzQ4ud9ZTFjcAk-1Y0l45vCDs1ONk0KMn-TzkhKKAEL17m3fV85B2lbrmxRnIhAM4-R1zOqVfr8sU_3AoWConwvRkI4I.png)

Este informe permite filtrar por organización, fecha, activo o cualquier descripción particular, categoría y configuración del esquema contable.  

![](../../../../../assets/drive/v044uU7hYLEk9gHyJ_rQT4PafeiO44KV81IWajtztUpPd9hLqZiPs9ivfPP69HxfwwK-35rPk_nzpLHsSXeXpUUfVDnFw7k4jsQ4AvDJIwDMCPWrsiRDyLPKgLCb0WDOB4GPZVU2urwKJ3sq1BhSXnA.png)

Una vez filtrada la información, se descarga una hoja de Excel como se muestra en la siguiente imagen:

![](../../../../../assets/drive/X4RYGKFzkl-VVrKXiztozXKKOQIFqIwXJMgUUeLzdGESddbVChKWbf6L2XnMO1aQg2wCfXit-Tw-w3TXDP_FLWBluY08K6JG6kHf_w2Mz5fRWBfzbbfV6edBbPzULPPPWxAALvtVBmxhKLtC_DwAzgg.png)

Este informe tiene en cuenta las líneas de amortización de cada Activo. Es decir, el informe se generará incluso si las líneas de amortización no están procesadas o contabilizadas. 

Es necesario filtrar por fecha ya que la información se obtiene en base a este filtrado. Es decir, el periodo acumulado, el valor neto y los campos posteriores del informe dependerán de este filtrado.

Por ejemplo: Fecha de periodo filtrada 01-01-2022 y 31-12-2022

**Periodo:** Se mostrará el total de las líneas de amortización entre 01/01/2022 y 12/31/2022. <br>
**Acumulado:** Se mostrará la suma de las líneas de amortización entre 01/01/2022 y 12/31/2022 y el total de las líneas de amortización anteriores a 01/01/2022. <br>
**Valor neto:** Se mostrará el valor del activo menos el campo Acumulado.  <br>
**Posterior:** Se mostrarán las líneas de amortización posteriores al 31-12-2022.  <br>

!!! info
    Cuando se completa la fecha de fin en la ventana Activos, ese Activo no aparecerá en el informe si la fecha filtrada es posterior a la fecha de fin del Activo.

---

Este trabajo es una obra derivada de [Gestión Financiera](http://wiki.openbravo.com/wiki/Financial_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.


---
Esta obra está licenciada bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L](https://etendo.software){target="_blank"}.