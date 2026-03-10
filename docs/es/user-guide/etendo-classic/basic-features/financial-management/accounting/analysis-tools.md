---
title: Informes - Contabilidad
tags:
    - Etendo Classic
    - Informes financieros
    - Análisis contable
    - Balance
    - Libro mayor
---

## Visión general

Esta sección describe las ventanas relacionadas con los informes financieros de contabilidad en Etendo. Estas son:

[:material-file-document-outline: Datos de contabilidad](#datos-de-contabilidad){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Cuadros plan general contable](#cuadros-plan-general-contable){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Cuadros plan general contable avanzado](#cuadros-plan-general-contable-avanzado){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Balance sumas y saldos](#balance-sumas-y-saldos){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Libro mayor](#libro-mayor){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Libro mayor avanzado](#libro-mayor-avanzado){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Diario asientos](#diario-asientos){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Diario asientos avanzado](#libro-mayor-avanzado){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Creación de informes de impuestos](#creación-de-informes-de-impuestos){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Extracto de cuenta de Cliente](#extracto-de-cuenta-de-cliente){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Configuración informes de impuestos](#configuración-informes-de-impuestos_1){ .md-button .md-button--primary } <br>
## Datos de contabilidad

:material-menu: `Aplicación` > `Gestión Financiera` > `Contabilidad` > `Herramientas de análisis` > `Datos de contabilidad`

### Visión general

La ventana de datos de contabilidad es una lista detallada de cada apunte contable de un esquema contable.

Etendo tiene un sistema contable integrado que combina la contabilidad financiera y la contabilidad analítica.

-   La **contabilidad financiera** permite al usuario utilizar dimensiones contables como "Organización", la "Cuenta" y la "Fecha contable":
    -   Estas dimensiones son siempre **obligatorias,** lo que significa que deben especificarse cada vez que un documento se contabiliza en el libro mayor.
-   La **contabilidad analítica** permite al usuario utilizar otras dimensiones como "Producto", "Terceros" y "Zona de venta".
    -   Estas dimensiones pueden configurarse como obligatorias u opcionales en la configuración del esquema contable de la organización si el cliente al que pertenece la organización no **"mantiene centralmente"** la Dimensión de contabilidad.
    -   En caso contrario, si el cliente **"mantiene centralmente"** la Dimensión de contabilidad, algunas de las dimensiones analíticas anteriores pueden configurarse en la ventana Cliente (p. ej., "Producto", "Proyecto", "Centro de costos"), mientras que otras deben configurarse en la configuración del esquema contable de la organización (p. ej., "Zona de venta", "Campaña").

Etendo permite al usuario contabilizar transacciones en el libro mayor solo si se especifican las dimensiones financieras y las dimensiones analíticas obligatorias, mientras que siempre existe la opción de especificar las analíticas opcionales.

### Cabecera

Este informe lista cada transacción contabilizada en el libro mayor mostrando cada dimensión contable especificada.

![](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/acct-transaction-details-1.png)

Los filtros de columna permiten al usuario filtrar la información que se va a mostrar por cualquiera de las dimensiones contables.
## Cuadros plan general contable
:material-menu: `Aplicación` > `Gestión Financiera` > `Contabilidad` > `Herramientas de análisis` > `Cuadros plan general contable`

### Visión general

El motor de informes de Cuadros plan general contable permite al usuario lanzar el Balance de situación y la Cuenta de Pérdidas y Ganancias, que deben configurarse previamente.

El informe de Balance de situación es un resumen cuantitativo de la situación financiera de una organización en un momento específico. Este informe muestra un resumen de los saldos de activos, pasivos y patrimonio neto.

El informe de Pérdidas y Ganancias muestra los ingresos, los gastos y el beneficio neto de una organización.

Estos informes deben configurarse antes de poder lanzarse en la ventana [Configuración de informes contables](../accounting/setup/balance-sheet-and-pl-structure-setup.md).

### Cabecera

![](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/balance-sheet-and-pl-structure-1.png)

Como se muestra en la imagen anterior, los datos a cumplimentar son:

- El **Esquema contable** del que se debe obtener la información contable.
- El **Informe contable** a lanzar. Este campo lista los informes creados y configurados en la ventana [Configuración de informes contables](./setup.md#configuración-de-informes-contables).
- La **Organización**. Este campo lista la organización para la cual se ha configurado el informe en la ventana de configuración de Cuadros plan general contable.

    - Si el informe está configurado para un tipo de organización "Legal con contabilidad", en este campo solo se muestra esa. Los saldos de las cuentas mostrados en el informe serán una consolidación de las organizaciones que pertenezcan a ella, si las hubiera.
    - Si el informe está configurado para un tipo de organización "Genérica", las organizaciones mostradas en este campo son, como mínimo, la organización genérica y el tipo de organización legal con contabilidad al que pertenece, todas ellas vinculadas al esquema contable seleccionado.

- El **Nivel de cuenta**, que define hasta qué nivel de detalle se va a mostrar en el informe; las opciones disponibles son las mismas que los niveles del elemento árbol de cuentas:

    - Encabezado: solo se muestran los elementos de tipo "encabezado", incluyendo información contable resumida hasta ese nivel.
        - Cuenta: en este caso se muestran los elementos "encabezado" y "cuenta", incluyendo información contable resumida hasta cada uno de esos niveles.
            - Separar: en este caso se muestran los elementos "encabezado", "cuenta" y "separar", incluyendo información contable resumida hasta cada uno de esos niveles.
                - Subcuenta: en este caso se muestran los elementos "encabezado", "cuenta", "separar" y "subcuenta", incluyendo información contable resumida hasta cada uno de esos niveles. Es importante recordar que los asientos contables se contabilizan a nivel de subcuenta.

- El indicador **Mostrar solo cuentas con valor** permite al usuario ver que el informe no muestra elementos de cuenta con saldo de cuantía *cero*, pero sí los elementos definidos como Título, que siempre se muestran independientemente del importe de su saldo.
- El indicador **Mostrar códigos de cuenta** permite al usuario hacer que el informe muestre (o no) la clave de búsqueda del nivel de elemento.

En la sección **Filtros primarios**, es posible especificar:

- Un **Número de página inicial** para el informe, en caso de que el informe necesite integrarse. Esto es útil cuando el informe debe integrarse como parte de un informe o documento mayor.
- Un **Ejercicio** y un **Ejercicio de referencia** para obtener un informe comparativo normalmente entre el "Ejercicio" actual y el anterior introducido como "Ejercicio de referencia". El informe tiene un filtro **Comparar con**, por lo que puede lanzarse solo para un ejercicio concreto, sin obligar a compararlo con otro ejercicio.
- Y, por último, **A fecha** (Fecha hasta) y **A fecha de referencia** (pueden introducirse los filtros Fecha desde); estos filtros se comportan de forma diferente según el informe:
    -   En el caso del informe de Balance de situación, puede introducirse un valor de "Fecha hasta" para que el informe muestre la información de saldos de cuenta hasta esa fecha.
    -   En el caso del informe de Pérdidas y Ganancias, pueden introducirse una "Fecha hasta" y una "Fecha desde" para que el informe muestre la información contable dentro de ese periodo de tiempo (un año, un trimestre, un mes, etc.).

**Ejemplo de informe de Balance de situación**

!!! info
    Tenga en cuenta que la palabra "Provisional" (en\_US) \[o "Provisional" (es\_ES)\] se muestra siempre que al menos uno de los periodos para los que se ha lanzado el informe aún no esté cerrado.

![](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/balance-sheet-report-1.png)

**Ejemplo de informe de Pérdidas y Ganancias**
 
![](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/profit-and-loss-report-1.png)
## Cuadros plan general contable Avanzado
:material-menu: `Aplicación` > `Gestión Financiera` > `Contabilidad` > `Herramientas de análisis` > `Cuadros plan general contable Avanzado`

<iframe width="560" height="315" src="https://www.youtube.com/embed/_vyLPYVFycU?si=WXJE2bGLZ_TMr9JX" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Visión general 

!!! info
    Esta funcionalidad está disponible a partir de la versión **3.4.0** del Financial Extensions Bundle, compatible con **Etendo 25.1**. Para instalarla, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

El informe **Cuadros plan general contable Avanzado** es una versión mejorada del anterior [Cuadros plan general contable](#cuadros-plan-general-contable). Su propósito es ampliar los criterios de filtrado, incluyendo todas las dimensiones de contabilidad disponibles y la posibilidad de comparar múltiples ejercicios o periodos.

### Cabecera

![](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/balance-sheet-and-pl-structure-2.png)

Campos a tener en cuenta:

Además de las anteriores **Opciones del informe**: 

- Esquema contable
- Informe contable general
- Organización
- Nivel de cuenta
- Mostrar solo cuentas con valor (marcar)
- Mostrar códigos de cuenta (marcar)
- Mostrar modo apaisado (marcar)

Se añadieron las siguientes dimensiones:    

- Terceros  
- Producto   
- 1.ª dimensión
- 2.ª dimensión 
- Proyecto 
- Actividad    
- Zona de venta    
- Campaña de ventas
- Centro de costos

!!! info
    En cada filtro de dimensión, se puede seleccionar más de una opción.

Además, aparte de los anteriores **Filtros primarios**: 

- Ejercicio
- A fecha (solo para Balance)
- Fecha de inicio (solo para Pérdidas y ganancias)
- Fecha final (solo para Pérdidas y ganancias)
- Comparar con (marcar)
- Ejercicio de referencia
- A fecha de referencia (solo para Balance)
- Desde fecha de referencia (solo para Pérdidas y ganancias)
- Hasta fecha de referencia (solo para Pérdidas y ganancias)
- Número de página inicial, impreso en el informe.


!!! info 
    - Ahora es posible comparar hasta **cuatro ejercicios** simultáneamente.
    - Además, se han añadido **nuevos campos** para permitir la selección de fechas y periodos específicos según las necesidades de cada informe, proporcionando una mayor flexibilidad en el análisis.
 

### Botones

En este informe, se añaden los botones **Vista**, **Exportar a PDF** y **Exportar a Excel** en la barra superior, lo que le permite visualizar la información directamente o exportarla en distintos formatos según sea necesario.

![](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/balance-sheet-and-pl-structure-3.png)

**Ejemplo de informe de Pérdidas y ganancias**

![alt text](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/balance-sheet-and-pl-structure-4.png)
## Balance sumas y saldos

:material-menu: `Aplicación` > `Gestión Financiera` > `Contabilidad` > `Herramientas de análisis` > `Balance sumas y saldos`

<iframe width="560" height="315" src="https://www.youtube.com/embed/o5V3Op_qYtE?si=DnTJ77x6zSMZ5KrC" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

!!! warning
    Si no dispone del [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}, el informe permanecerá en una versión heredada con funcionalidad limitada. No podrá navegar directamente al Esquema contable desde Terceros cuando el informe esté agrupado por esta dimensión, y no estarán disponibles las mejoras de interfaz ni las opciones mejoradas para exportar el informe a Excel y PDF.

### Visión general

El **Balance sumas y saldos** verifica que el total de débitos sea igual al total de créditos.

Aunque normalmente se ejecuta al final de un periodo antes de preparar el Balance de situación y la Cuenta de pérdidas y ganancias, en Etendo puede generarse en cualquier momento.

Para una **Organización** y un **Esquema contable** seleccionados, el informe muestra:

- El saldo de la cuenta en la fecha de inicio
- El total de débitos dentro del periodo seleccionado
- El total de créditos dentro del periodo seleccionado
- El saldo de la cuenta en la fecha final

En la parte inferior del informe, **el total de débitos debe ser igual al total de créditos**.


### Cabecera

![alt text](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/trial-balance-window-1.png)

Campos clave a tener en cuenta:

#### Filtros principales

- **Fecha de inicio**: La fecha a partir de la cual se toma el saldo de la cuenta.
- **Fecha final**: La fecha hasta la cual se calcula el saldo de la cuenta, usando la fórmula:  
  `Saldo a fecha final = Saldo a fecha de inicio + Total débitos − Total créditos`
- **Organización**: La organización para la cual se genera el Balance sumas y saldos. Puede ejecutarse para:
    - Tipo de organización **Legal con Accounting**.
    - Tipo de organización **Genérica**, que debe pertenecer a una organización *Legal con Accounting*. Estas organizaciones heredan el esquema contable de la entidad legal a la que pertenecen y pueden contabilizar transacciones.
    - Entidades de tipo **Organización**, que pueden compartir un esquema contable entre múltiples organizaciones que pertenecen a ellas. Aunque este tipo no puede contabilizar transacciones directamente, el Balance sumas y saldos resume la información contable de todas las organizaciones relacionadas que comparten el mismo esquema contable.
- **Esquema contable**: El esquema contable asociado a la organización seleccionada.

#### Filtro Avanzado

Esta sección proporciona opciones adicionales para refinar el informe de Balance sumas y saldos:

- **Nivel de cuenta**: Define el nivel de detalle que se mostrará en el informe. Las opciones incluyen:

    - **Encabezado**
    - **Cuenta**
    - **Separar**
    - **Subcuenta** (por defecto)
    
    !!! info 
        Por defecto, el informe se genera a nivel de **Subcuenta**. Esto garantiza que, para cada subcuenta en el árbol de cuentas, el total de débitos sea igual al total de créditos.

- **Número de página inicial**: Establece el número de página donde comienza el informe. Útil al integrar este informe en documentos más amplios.

- **Importe del asiento de apertura al saldo inicial**: Esta opción está seleccionada por defecto. Controla cómo se muestra el saldo de apertura (p. ej., 1 de enero de 2021) en el informe:

    - Para cuentas de pasivo con un saldo de apertura negativo, el importe puede aparecer en la columna **Saldo a fecha** o en la columna **Crédito contabilizado**.
    - Para cuentas de activo con un saldo de apertura positivo, el importe puede aparecer en la columna **Saldo a fecha** o en la columna **Débito contabilizado**.

    !!! note
        Esta configuración solo se aplica si la **Fecha desde** del informe coincide con la fecha contable de apertura (p. ej., 1 de enero de 2021). En caso contrario, el saldo de apertura siempre se muestra en la columna **Saldo a fecha**.

- **Desde cuenta / Hasta cuenta**: Permite especificar un rango de subcuentas a incluir en el informe (solo disponible cuando el nivel de cuenta está establecido en *Subcuenta*).

#### Dimensiones

Puede refinar el informe de Balance sumas y saldos seleccionando **Dimensiones** adicionales, como:

- **Terceros**
- **Producto**
- **Proyecto**

Estas dimensiones se registran cuando las transacciones se contabilizan en el libro. Las transacciones siempre se vinculan a través de subcuentas.

- **Agrupar por**: Permite agrupar el informe por una dimensión específica. Las opciones disponibles son *Terceros*, *Producto* y *Proyecto*.  
  Por ejemplo, si selecciona *Terceros*, el informe mostrará resultados agrupados por cada tercero, y podrá navegar directamente al Esquema contable de ese tercero desde el informe.

- **Incluir importes cero**: Cuando está habilitado, el informe muestra todas las subcuentas, incluidas aquellas con saldos cero.


### Botones

- **Vista**: Abre los resultados del informe en una nueva ventana. Desde allí, puede navegar directamente al Esquema contable:
  
    - Haciendo clic en el número de cuenta de cada subcuenta.
    - O bien, si el informe está agrupado por Terceros, haciendo clic en el nombre del tercero para acceder a su vista del Esquema contable.

    <figure markdown="span">
        ![alt text](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/trial-balance-report-1.png)
        <figcaption>Ejemplo de la salida del informe sin agrupar</figcaption>
    </figure>

    <figure markdown="span">
        ![alt text](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/trial-balance-report-2.png)
        <figcaption>Ejemplo del informe agrupado por Terceros</figcaption>
    </figure>

    En ambos casos, hay enlaces disponibles para **navegar directamente al Esquema contable**.

- **Exportar a PDF**: Genera una versión en PDF del informe. Este archivo puede imprimirse o almacenarse para su revisión posterior. La salida en PDF respeta las mismas reglas de agrupación aplicadas en el selector.

- **Exportar a Excel**: Genera un archivo Excel del informe. El archivo exportado también sigue las mismas reglas de agrupación aplicadas en el selector.
## Libro mayor

:material-menu: `Aplicación` > `Gestión Financiera` > `Contabilidad` > `Herramientas de análisis` > `Libro mayor`

### Visión general

El informe de Libro mayor lista cada “subcuenta” del libro mayor y sus asientos de débito y crédito dentro de un periodo de tiempo determinado.
   
![](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/general-ledger-report-1.png)

Tal y como se muestra en la imagen anterior, los campos a cumplimentar para lanzar este informe son:

- la *"Organización"* para la cual se requiere la información contable.  
    Una vez más, la información contable proporcionada por este informe depende del tipo de organización seleccionada, de forma que:
    - la información contable mostrada podría estar relacionada únicamente con una organización “Genérica” perteneciente a una “Entidad Legal con contabilidad”
    - o podría ser una consolidación en caso de seleccionar una “Entidad Legal con contabilidad” o una “Organización” que tenga otras organizaciones por debajo.
- la opción *"Mostrar saldos abiertos"*, que ocultará aquellos asientos cuyo saldo sea cero. (Por ejemplo, eliminando asientos de cuentas a cobrar/a pagar de facturas una vez que estas han sido pagadas).
- y el correspondiente *"Esquema contable"*, que también dependerá de la Organización seleccionada previamente.

Es posible acotar la información contable que se mostrará en el informe mediante:

- un rango de “importes”
- un conjunto de *"subcuentas"*
- y un conjunto de *"Dimensión de contabilidad"* como terceros, producto y proyecto

Por último, también es posible:

- *"Grupo"* la información por cualquiera de las dimensiones contables
- e introducir un *"Número de página inicial"* para el informe

Una vez que todos los datos se han introducido correctamente, el botón "Selector" muestra el resultado del informe en la misma ventana:

- los asientos mostrados para cada subcuenta se ordenan por fecha contable y, además, se muestra el saldo de la subcuenta para cada asiento.

Las flechas de la barra de herramientas permiten al usuario navegar por el resultado del informe mostrado en la ventana.

El informe de Libro mayor también puede visualizarse y guardarse en formato Excel y en formato PDF:

- Formato Excel pulsando el botón de acción *"Exportar a Excel"* de la barra de herramientas:
    - Este formato contiene una lista de todos los asientos por cada subcuenta sin agrupar; por lo tanto, es posible agruparlos según se desee.
    - También lista las correspondientes dimensiones contables de cada asiento.
-   Formato PDF pulsando el botón de acción *"Imprimir registro"* de la barra de herramientas:
    - Este formato incluye un saldo "Inicial" de cada subcuenta, el saldo "Subtotal" de cada subcuenta para el periodo indicado y calcula el saldo "Total" de cada subcuenta.

![](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/general-ledger-report-2.png)
## Libro mayor avanzado

:material-menu: `Aplicación` > `Gestión Financiera` > `Contabilidad` > `Herramientas de análisis` > `Libro mayor avanzado`

<iframe width="560" height="315" src="https://www.youtube.com/embed/o5V3Op_qYtE?si=DnTJ77x6zSMZ5KrC" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

### Visión general

Este informe **Libro mayor avanzado** es una versión mejorada del anterior [Libro mayor](#libro-mayor). Su propósito es ampliar los criterios de filtrado, incluyendo todas las dimensiones contables existentes en la tabla Datos de contabilidad.

![](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/general-ledger-report-adv-1.png)

Además de los filtros básicos anteriores: Fecha desde, Fecha hasta, Importe desde, Importe hasta, Organización, Esquema contable, Desde cuenta, Hasta cuenta, y los filtros de dimensión anteriores: Terceros, Producto y Proyecto, se añadieron los siguientes:

- Actividad
- 1.ª dimensión
- 2.ª dimensión
- Zona de venta
- Campaña de ventas
- Centro de costos

Además, se añadió el filtro Organización, un filtro que combina el campo Organización original con la casilla de verificación Mostrar operaciones relacionadas, para mostrar transacciones intercompañía. En cada filtro, se puede seleccionar más de una opción.

El nuevo campo **Mostrar entidades dimensionales** permite seleccionar las dimensiones contables que se incluirán en el informe.

![](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/general-ledger-report-adv-2.png)

En el menú Agrupar por, se añaden las siguientes opciones:

- Actividad
- 1.ª dimensión
- 2.ª dimensión
- Zona de venta
- Campaña de ventas
- Centro de costos

Es posible seleccionar la dimensión contable deseada para la agrupación. Al generar el informe, la dimensión seleccionada aparece en la cabecera, indicando el criterio de agrupación utilizado.

![](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/general-ledger-report-adv-4.png)

### Botones

En la barra de herramientas, puede encontrar los botones **Vista**, **Exportar a PDF** y **Exportar a Excel** para generar el informe. En el caso de la opción Vista, se abre una nueva ventana con el informe correspondiente. En los otros casos, el informe se exporta en formato PDF o Excel.

![](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/general-ledger-report-adv-3.png)

!!!warning
    Si se eligen las opciones Vista o Exportar a PDF, el límite de dimensiones a incluir es 4 para evitar problemas de visualización. Esto no ocurre con Exportar a Excel, en cuyo caso puede elegir cualquier número de dimensiones.

Además, con esta funcionalidad puede navegar al asiento relacionado directamente desde el informe. Esto permite un acceso a la información más sencillo y eficiente. Al hacer clic en un asiento, el usuario puede navegar a la ventana Diario asientos, aplicando todos los filtros seleccionados.

![](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/general-ledger-report-adv-5.png)
## Diario asientos

:material-menu: `Aplicación` > `Gestión Financiera` > `Contabilidad` > `Herramientas de análisis` > `Diario asientos`

### Visión general

El Informe de Diario asientos es una lista de todos los comprobantes de diario de una organización y esquema contable, mostrados en orden cronológico.

Un asiento es el registro de datos financieros en un comprobante de diario, de forma que el débito sea igual al crédito y los débitos se introduzcan antes que los créditos.

![](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/journal-entries-report-1.png)

Tal y como se muestra en la imagen anterior, la sección "Filtros principales" permite al usuario especificar:

-   la "*Organización*" y el "*Esquema contable*" para los que se requieren los datos financieros obtenidos de los asientos.

El "Filtro Avanzado" es ahora una sección plegable. En esta sección, es posible especificar:

- una **Cuenta desde/hasta** para mostrar asientos con al menos una línea que utilice una cuenta definida dentro del rango.
- un `Tipo de documento` para acotar los datos financieros que se mostrarán en el informe únicamente a los relacionados con ese tipo de documento en particular.
    - Si el tipo de documento seleccionado tiene asociado un número de documento, por ejemplo un tipo de documento de factura, será posible acotar los datos mostrados a un "**Número de Documento**" específico.
- el "**Número de página inicial**" *que se mostrará en el formato PDF del informe*
- el **"Número de asiento inicial"** que se mostrará en el formato PDF del informe
- la **"Descripción del asiento"** que se mostrará en el formato PDF del informe

El resto de las casillas de verificación están seleccionadas por defecto para mostrar:

- los asientos *"**regulares**"*:
    - estos asientos son los generados al contabilizar cualquiera de los tipos de documento de Etendo o al contabilizar un diario de Esquema contable que no esté marcado como "Apertura".
- los asientos *"**de apertura**"*:
    - estos asientos son generados automáticamente por Etendo tras el cierre de un ejercicio fiscal determinado
    - estos asientos también pueden generarse manualmente al contabilizar un diario de Esquema contable siempre que sus asientos estén marcados como "Apertura".
- los asientos "**de cierre**":
    - estos asientos son generados automáticamente por Etendo tras el cierre de un ejercicio fiscal determinado
- y, por último, los asientos *"**de cierre de PyG**"*:
    - estos asientos son generados automáticamente por Etendo tras el cierre de un ejercicio fiscal determinado

Por último, y del mismo modo que para el resto de informes financieros, el Diario asientos puede ejecutarse en:

- formato *HTML*. Un ejemplo de la salida HTML:

![](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/journal-entries-report-2.png)

- formato *PDF* utilizando el botón de acción "Imprimir registro" de la barra de herramientas
- o formato *XML* utilizando el botón de acción "Exportar a Excel" de la barra de herramientas.
## Diario asientos avanzado

:material-menu: `Aplicación` > `Gestión Financiera` > `Contabilidad` > `Herramientas de análisis` > `Diario asientos avanzado`

<iframe width="560" height="315" src="https://www.youtube.com/embed/o5V3Op_qYtE?si=DnTJ77x6zSMZ5KrC" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

### Visión general

Este informe **Diario asientos avanzado** es una versión mejorada del anterior [Diario asientos](#diario-asientos). Su propósito es ampliar los criterios de filtrado, incluyendo todas las dimensiones de contabilidad existentes en la tabla Datos de contabilidad.

![](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/journal-entries-report-adv-1.png)


Además de los filtros básicos anteriores: Fecha desde, Fecha hasta, Organización, Esquema contable y los filtros avanzados anteriores: Desde cuenta, Hasta cuenta, Documento, Documento N°, se añadieron los siguientes:

- Terceros
- Producto
- 1.ª Dimensión
- 2.ª Dimensión
- Proyecto
- Actividad
- Zona de venta
- Campaña de ventas
- Centro de costos

El nuevo campo **Mostrar entidades dimensionales** permite seleccionar las dimensiones de contabilidad que se incluirán en el informe.

![](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/journal-entries-report-adv-2.png)

Tras utilizar los campos y casillas de verificación disponibles, el informe filtra las transacciones incluidas en las dimensiones seleccionadas, para la organización y el esquema contable seleccionados y para un periodo determinado, si fuese necesario. En cada filtro, se puede seleccionar más de una opción.

### Botones

En la barra superior, puede encontrar los botones **Vista**, **Exportar a PDF** y **Exportar a Excel** para generar el informe. En el caso de la opción Vista, se abre una nueva ventana con el informe correspondiente. En los otros casos, el informe se exporta en formato PDF o Excel.

![](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/journal-entries-report-adv-3.png)

!!!warning
    Si se eligen las opciones Vista o Exportar a PDF, el límite de dimensiones a incluir es 4 para evitar problemas de visualización. Este no es el caso de Exportar a Excel, en cuyo caso puede elegir cualquier número de dimensiones.

Además, con esta funcionalidad puede navegar a la transacción relacionada directamente desde el número de asiento de los informes. Esto mejora la trazabilidad y agiliza el análisis contable.

![](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/journal-entries-report-adv-4.png)
## Creación de informes de impuestos

:material-menu: `Aplicación` > `Gestión Financiera` > `Contabilidad` > `Herramientas de análisis` > `Creación de informes de impuestos`

### Visión general

Este formulario permite al usuario crear diferentes Informes de impuestos según las necesidades específicas del usuario.

Para explicar el uso de este proceso, es necesario comprender la ventana Configuración informes de impuestos.

##### Configuración informes de impuestos

Esta ventana permite al usuario crear o modificar diferentes Informes de impuestos para los distintos impuestos existentes. En las siguientes líneas, se explicará cómo crear un nuevo Informe de impuestos:

![](../../../../../assets/drive/1I29H6eckLq6K7WR7wzgmYPgjZ4PRcUiV.png)

La ventana tiene algunos parámetros para indicar el Informe de impuestos creado:

- **Nombre:** El nombre del Informe.
- **Impuesto:** El impuesto que se mostrará en el informe.
- **Operación de venta:** Marcado si es un Informe de impuestos de ventas, desmarcado si es un Informe de impuestos de compras.
- **Informe:** Si está marcado, aparecerá en el formulario Creación de informes de impuestos para poder seleccionarlo.
- **Mostrar:** Si está marcado, aparecerá en el formulario Creación de informes de impuestos para poder seleccionarlo.
- **Nivel agrupación:** Si está marcado, el tipo impositivo se define como un impuesto padre que tiene impuestos dependientes: los impuestos hijo. Si un impuesto no va a tener ningún “hijo”, no debe marcarse como resumen.
- **Negativo:** Si está marcado, el informe se imprimirá con valores negativos; en caso contrario, se imprimirá con valores positivos.
- **Activo:** Si es un Informe de impuestos activo.

Una vez configurado el Informe de impuestos, aparecerá en el formulario Creación de informes de impuestos:

##### Creación de informes de impuestos

Esta ventana permite imprimir Informes previamente definidos por el usuario. Para imprimir el Informe, es necesario completar algunos campos:

![](../../../../../assets/drive/174ocSJCYYPhTy_2AmynTHIQv93BlA4rB.png)

- **Fecha de inicio:** Fecha de inicio del Informe.
- **Fecha final:** Última fecha del Informe.
- **Informes de impuestos:** En esta lista aparecerán todos los Informes de impuestos creados para poder seleccionarlos.
- **Organización:** Organización para la cual se imprimirá el Informe.

Una vez introducidos estos campos, será posible imprimir el Informe, que mostrará el importe durante esas fechas.

![](../../../../../assets/drive/1hDOABUzDouOzwfy4lBICVjVpUzKlnsB0.png)
## Extracto de cuenta de Cliente

:material-menu: `Aplicación` > `Gestión Financiera` > `Contabilidad` > `Herramientas de análisis` > `Extracto de cuenta de Cliente`

!!! info
    Esta funcionalidad está disponible a partir de la versión **3.8.0** de Financial Extensions Bundle, compatible con **Etendo 25.1**. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

!!! warning
    Si no dispone de [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}, el informe permanecerá en una versión heredada con funcionalidad limitada.

### Visión general

El **Extracto de cuenta de Cliente** es un informe consolidado que muestra todas las transacciones de un tercero contabilizadas en el libro mayor durante un período especificado. Este informe proporciona un historial financiero completo de la relación comercial, mostrando débitos, créditos y saldos acumulados para cada transacción.

Este informe puede generarse para terceros configurados como:

- **Cliente**: Muestra transacciones relacionadas con clientes (facturas de venta, cobros recibidos, etc.).
- **Proveedor**: Muestra transacciones relacionadas con proveedores (facturas de compra, pagos realizados, etc.).
- **Cliente/Proveedor**: Muestra todas las transacciones de terceros con ambos roles.

El informe agrega transacciones de diversas fuentes, incluidas:

- Facturas de venta / Facturas de compra
- Cobro / Pago
- Transacciones financieras
- Conciliaciones

!!! warning
    En el informe solo se incluyen transacciones *Contabilizado*. Las transacciones *Completada* pero no *Contabilizado* no se tienen en cuenta.

El Extracto de cuenta de Cliente proporciona la siguiente información para cada transacción:

- **Número de Documento**: Identificación de la transacción.
- **Fecha contable**: Fecha en la que se contabilizó la transacción.
- **Tipo de documento**: Tipo de transacción (p. ej., factura de clientes, factura de proveedores, transacción de cuenta financiera).
- **Débito/Crédito**: Importes financieros de cada transacción.
- **Saldo neto**: Saldo acumulado calculado como \[Débito - Crédito\] para cada transacción, mostrando el saldo acumulado a lo largo del período.

!!! note
    Los importes negativos se resaltan mediante el uso de paréntesis ( ).

### Cabecera

![](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/customer-statement-report-1.png)

Como se muestra en la imagen anterior, se pueden configurar los siguientes parámetros:

- **Tipo informe**: Define el tipo de informe a generar. Las opciones incluyen:
    - **Cliente**: Muestra transacciones relacionadas con clientes.
    - **Proveedor**: Muestra transacciones relacionadas con proveedores.
    - **Cliente/Proveedor**: Muestra todas las transacciones de terceros con ambos roles. El informe muestra las transacciones de proveedor y de cliente por separado, dividiéndolas en secciones diferenciadas.
- **Organización**: La organización para la que se generará el extracto.
- **Esquema contable**: El esquema contable asociado a la organización seleccionada.
- **Terceros**: El tercero (cliente, proveedor o ambos) para el que se generará el extracto.
- **Fecha de inicio**: Fecha de inicio del período a incluir en el informe.
- **Fecha final**: Fecha final del período a incluir en el informe.
- **Multidivisa**:
    - **Sin marcar** (por defecto): No agrupa los registros por divisa y muestra todos los importes en la divisa del Esquema contable.
    - **Marcado**: Agrupa los registros por divisa y muestra los importes en la divisa original. El informe se dividirá por cada divisa diferente, cada una con su saldo inicial y final aislados del resto.
- **Sumar saldo inicial**:
    - **Sin marcar** (por defecto): El informe muestra un Saldo inicial al comienzo y, a continuación, lista cada transacción con su Saldo neto. El Saldo final es igual al Saldo inicial más el último Saldo neto.
    - **Marcado**: El Saldo inicial se agrega al Saldo neto de cada transacción, haciendo que el Saldo final sea igual al último Saldo neto mostrado.

### Botones

En la barra de herramientas, puede encontrar los siguientes botones para generar el informe:

- **Vista**: Abre los resultados del informe en una nueva ventana para su visualización inmediata.
- **Exportar a PDF**: Genera una versión en PDF del informe que puede imprimirse o almacenarse.
- **Exportar a Excel**: Genera un archivo Excel del informe para su posterior análisis o personalización.

Un ejemplo de la salida del Extracto de cuenta de Cliente:

![](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/customer-statement-report-2.png)
## Configuración informes de impuestos

:material-menu: `Aplicación` > `Gestión Financiera` > `Contabilidad` > `Herramientas de análisis` > `Configuración informes de impuestos`

### Visión general

Etendo permite al usuario crear diferentes Informes de impuestos según las necesidades específicas del usuario.

Para explicar el uso de este proceso, es necesario comprender la ventana Configuración informes de impuestos.

##### Configuración informes de impuestos

Esta ventana permite al usuario crear o modificar diferentes Informes de impuestos para los distintos impuestos existentes. En las siguientes líneas, se explicará cómo crear un nuevo Informe de impuestos:

![](../../../../../assets/drive/1j91z0YQV6PrYedzt7qrf5NsIhMHgxAP6.png)

La ventana tiene algunos parámetros para indicar el Informe de impuestos creado:

- **Nombre:** El nombre del Informe.
- **Impuesto:** El impuesto que se mostrará en el informe.
- **Operación de venta:** Marcado si es un Informe de impuestos de ventas; desmarcado si es un Informe de impuestos de compras.
- **Informe:** Si está marcado, aparecerá en el formulario Creación de informes de impuestos para poder seleccionarlo.
- **Mostrar:** Si está marcado, aparecerá en el formulario Creación de informes de impuestos para poder seleccionarlo.
- **Nivel agrupación:** Si está marcado, el tipo impositivo se define como un impuesto padre que tiene impuestos dependientes: los impuestos hijo. Si un impuesto no va a tener ningún “hijo”, no debe marcarse como resumen.
- **Negativo:** Si está marcado, el informe se imprimirá con valores negativos; en caso contrario, se imprimirá con valores positivos.
- **Activo:** Si es un Informe de impuestos activo.

Una vez que se ha configurado el Informe de impuestos, aparecerá en el formulario Creación de informes de impuestos:

##### **Creación de informes de impuestos**

Esta ventana permite imprimir Informes previamente definidos por el usuario. Para imprimir el Informe, es necesario completar algunos campos:

![](../../../../../assets/drive/17xPpINQrk2rcbebH6-hCCsIjwDP0X7qH.png)

- **Fecha de inicio:** Fecha de inicio del Informe
- **Fecha final:** Última fecha del Informe
- **Informes de impuestos:** En esta lista aparecerán todos los Informes de impuestos creados para poder seleccionarlos.
- **Organización:** Organización para la cual se imprimirá el Informe.

Una vez introducidos estos campos, será posible imprimir el Informe, que mostrará el importe durante esas fechas.

![](../../../../../assets/drive/1eqmh8_yS9iZrrp0PpT70hpDlT5MhrACN.png)

---

Este trabajo es una obra derivada de [Gestión Financiera](http://wiki.openbravo.com/wiki/Financial_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.