---
title: Modelo 303
tags:
    - Modelo 303
    - Localización Española
    - Gestión Financiera
    - Contabilidad
    - Herramientas de análisis
---

:octicons-package-16: Javapackage: `org.openbravo.module.aeat303.es`

# Modelo 303

## Descripción General

El módulo **Modelo AEAT303 - Impuesto sobre el Valor Añadido - Autoliquidación** permite a las empresas cumplir con sus obligaciones fiscales de autoliquidación de IVA. El resultado es la diferencia entre el IVA Devengado y el IVA Deducible. El módulo genera el Modelo 303 como un fichero de texto válido conforme a los requerimientos de la Agencia Tributaria española (Orden EHA/3786/2008). Es parte del bundle de [Localización Española](overview.md) de Etendo.

!!! info
    Compatible con Etendo 21.4 o versiones posteriores.

Consulte la estructura válida del fichero en el siguiente enlace de la AEAT: [_Modelo 303 - Fichero_](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-303/presentacion-electronica-modelo-303-fichero.html){target="_blank"}.

El fichero del Modelo 303 contiene la siguiente información:

-   **Información genérica**
    -   NIF
    -   Apellidos o Razón Social - Nombre
    -   Ejercicio
    -   Periodo
-   **IVA devengado** (IVA repercutido en ventas), incluyendo:
    -   IVA devengado conforme al régimen general - Base, Cuota y Tipo
    -   IVA devengado conforme al régimen especial de recargo de equivalencia, especificado por tipo de IVA - Base, Cuota y Tipo
    -   IVA devengado en las adquisiciones intracomunitarias de bienes - Base y Cuota
-   **IVA Deducible** (IVA soportado en compras), incluyendo:
    -   operaciones interiores de bienes y servicios - Base y Cuota
    -   operaciones interiores de bienes de inversión - Base y Cuota
    -   importaciones de bienes - Base y Cuota
    -   importaciones de bienes de inversión - Base y Cuota
    -   adquisiciones intracomunitarias de bienes - Base y Cuota
    -   adquisiciones intracomunitarias de bienes de inversión - Base y Cuota
    -   regularizaciones
-   **Diferencia** - Resultado de la liquidación como diferencia del IVA devengado - IVA soportado deducible, incluyendo otras operaciones tales como:
    -   entregas intracomunitarias de bienes - Base
    -   exportaciones - Base
    -   operaciones no sujetas o de inversión de sujeto pasivo - Base
-   **Datos bancarios y otros.**

Genere el fichero en Etendo desde el **Generador de declaraciones de impuestos**:

:material-menu: `Gestión Financiera` > `Contabilidad` > `Herramientas de análisis` > `Generador de declaraciones de impuestos`

Una vez generado, el fichero puede:

1.  **Pre-validarse** en la página web de la AEAT: [_Formulario del 303 para su presentación (predeclaración)_](https://www2.agenciatributaria.gob.es/es13/h/ie93030b.html){target="_blank"}.
2.  **Presentarse** en el siguiente enlace de la AEAT: [_Presentación del Modelo_](https://www2.agenciatributaria.gob.es/es13/h/ie93030a.html){target="_blank"}.

La autoliquidación de IVA puede ser:

!!! info
    Las "casillas" corresponden a los campos del formulario oficial de la AEAT. Las "posiciones" indican la ubicación de cada dato dentro del fichero de texto generado.

-   *A ingresar* (casilla 48>0): cuando el IVA Devengado > IVA deducible. El IVA a ingresar se refleja en la casilla \[I\], posición 860.
-   *A compensar* (casilla 48<0): cuando el IVA Devengado < IVA deducible. El IVA a compensar se refleja en la casilla \[49\], posición 804.
-   *A devolver* (casilla 48<0 e inscripción en el Registro de devolución mensual): cuando el IVA Devengado < IVA deducible. El IVA a devolver se refleja en la casilla \[50\], posición 822.
-   *Cero* o *Sin actividad* (casilla 48=0).

## Presentación del Modelo 303

Los obligados a presentar el Modelo 303 son:

-   Los sujetos pasivos que realicen actividades a las que aplique el Régimen General del Impuesto (IVA) o cualquier otro de los regímenes del mismo, a excepción del Régimen especial de agricultura, ganadería y pesca, del Régimen de recargo de equivalencia y del Régimen Simplificado.

La presentación del Modelo 303 puede ser mensual o trimestral.

La presentación es obligatoria por vía telemática (fichero de texto válido) para los sujetos pasivos que:

-   tengan forma jurídica de sociedad anónima o sociedad de responsabilidad limitada
-   y/o estén inscritos en el "Régimen de devolución mensual".

??? info "Novedades a partir del 1 de julio de 2010"

    **MODIFICACIÓN TIPOS IMPOSITIVOS IVA**

    La Ley 26/2009 de Presupuestos Generales del Estado para 2010, modificó los tipos general y reducido del Impuesto sobre el Valor Añadido con efectos a partir del 1 de julio, de forma que el tipo general pasa del 16% al 18% y el tipo reducido pasa del 7% al 8%, sin que se haya producido alteración alguna en relación con el tipo superreducido del 4% y con los tipos del recargo de equivalencia.

    **Cumplimentación de declaraciones**

    En las autoliquidaciones de IVA, Modelo 303, correspondientes a los períodos iniciados desde julio de 2010 (correspondientes al mes 07 ó al 3T), se puede dar la situación de que en un mismo período de liquidación hayan de reflejarse operaciones gravadas según los nuevos tipos impositivos (18%, 8%) junto con otras devengadas en períodos anteriores y a las que les sean de aplicación los tipos vigentes hasta el 30 de junio (7% ó 16%).

    En estos supuestos deberá consignarse en las casillas correspondientes la suma algebraica de las bases imponibles. De igual forma se procederá con las casillas correspondientes a las cuotas devengadas.

    En cuanto a las casillas relativas a los tipos impositivos, se consignará el tipo resultante del cociente entre la cuota y la base imponible declarada, cualquiera que sea el resultado y si este cociente no da un número entero, se hará constar los dos primeros decimales del número resultante.

    En las autoliquidaciones Modelo 303 correspondientes al 1T ó 2T de 2010 o a los meses 01 a 06 de 2010 no se puedan consignar bases ni cuotas a los nuevos tipos impositivos del 18% ó 8%.

    !!! info
        Los cambios expuestos en esta sección implican una modificación del contenido de los datos de referencia del módulo.

??? info "Novedades a partir del 1 de septiembre de 2012"

    **MODIFICACIÓN TIPOS IMPOSITIVOS IVA Y RECARGO DE EQUIVALENCIA**

    El Real Decreto Ley 20/2012 de medidas para garantizar la estabilidad presupuestaria y de fomento de la competitividad, modificó los tipos general y reducido del Impuesto sobre el Valor Añadido con efectos a partir del 1 de septiembre, de forma que el tipo general pasa del 18% al 21% y el tipo reducido pasa del 8% al 10%, sin que se haya producido alteración alguna en relación con el tipo superreducido del 4%. Igualmente, los tipos de recargo de equivalencia pasan del 4% al 5,2% y del 1% al 1,4%.

    **Cumplimentación de declaraciones**

    En las autoliquidaciones de IVA, Modelo 303, correspondientes a los períodos iniciados desde septiembre de 2012 (correspondientes al mes 09 ó al 3T), se puede dar la situación de que en un mismo período de liquidación hayan de reflejarse operaciones gravadas según los nuevos tipos impositivos junto con otras devengadas en períodos anteriores y a las que les sean de aplicación los tipos vigentes hasta el 30 de agosto.

    En estos supuestos, deberá consignarse en las casillas correspondientes la suma algebraica de las bases imponibles. De igual forma se procederá con las casillas correspondientes a las cuotas devengadas.

    En cuanto a las casillas relativas a los tipos impositivos, se consignará el tipo resultante del cociente entre la cuota y la base imponible declarada, cualquiera que sea el resultado y si este cociente no da un número entero, se hará constar los dos primeros decimales del número resultante.

    En las autoliquidaciones Modelo 303 correspondientes al 1T ó 2T de 2012 o a los meses 01 a 08 de 2012 no se puedan consignar bases ni cuotas a los nuevos tipos impositivos.

    !!! info
        Los cambios expuestos en esta sección implican una modificación del contenido de los datos de referencia del módulo.


## Instalación y Aplicación del Módulo

!!! info
    Si el bundle **Localización Española** todavía no está instalado en su entorno Etendo, solicítelo a su administrador o acceda al [Marketplace](https://marketplace.etendo.cloud/#/product-details?module=003B475055DD421B9483B5BE15AA48C5){target="_blank"} para adquirirlo. Una vez instalado, continúe con los pasos de esta sección.

Una vez instalado el bundle **Localización Española** — el cual incluye el módulo **Tax Report: Modelo 303 (Spain)** —, aplique su conjunto de datos a la organización legal con contabilidad desde:

:material-menu: `Configuración General` > `Organización` > `Gestión del módulo de Empresa`:

1. Seleccione la **Organización** legal con contabilidad. Es la organización que representa a la entidad legal con obligaciones fiscales en España y que tiene configurada una contabilidad activa.
2. En **Datos de referencia**, marque las siguientes opciones:
    - `Tax Report: Modelo 303 (Spain) - 3.0.0 - Spanish (Spain)`
    - `Taxes: configuration for Spain (Impuestos para España) - 3.0.0 - Spanish (Spain)` (solo si no lo ha aplicado antes; si ya lo hizo al instalar otro módulo de la Localización Española, puede omitirlo).
3. Haga clic en **Aceptar**.

!!! note
    **Si el dataset no aparece en la lista:** verifique que (1) el módulo `Tax Report: Modelo 303 (Spain)` está instalado y (2) ha seleccionado una organización distinta de `*` — debe ser siempre una organización legal. Si tras seleccionar la organización correcta las opciones siguen sin aparecer, espere unos segundos y vuelva a comprobar.

![Gestión del módulo de Empresa](../../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/modelo-303/gestion-modulo-empresa.png)


## Actividades del I.A.E.

En el Modelo 303, a partir de 2022, el informe mensual del último periodo debe incluir las principales actividades del I.A.E. (Impuesto de Actividades Económicas) en las que la empresa trabaja habitualmente.

El módulo **Epígrafes I.A.E.**, instalado como dependencia del 303, añade una nueva solapa a la ventana **Organización** donde puede indicar todas las actividades en las que su empresa ha estado trabajando. El Modelo 303 debe incluir como mínimo una actividad principal, marcada en la aplicación como por defecto, y como máximo 5 actividades. Si incluye más de 5 actividades, el informe tomará las 5 primeras según el número de línea.

![Organización - Actividades del IAE](../../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/modelo-303/organizacion-actividades-iae.png)

El módulo **Epígrafes IAE** incluye el conjunto correspondiente a la clave 1. Si desea incluir un epígrafe que pertenezca a cualquier otra clave, cree un nuevo registro en la ventana **Epígrafes IAE** e inclúyalo en la solapa **Actividades del IAE** de la ventana **Organización**.

Para el Modelo 303, los campos **Epígrafe IAE** y **Código** son obligatorios.

## Generación del Modelo 303

El Modelo 303 de autoliquidación de IVA se genera como un fichero de texto válido conforme a los requerimientos de la AEAT desde:

:material-menu: `Gestión Financiera` > `Contabilidad` > `Herramientas de análisis` > `Generador de declaraciones de impuestos`

Introduzca los datos genéricos: **Organización**, **Ejercicio** y **Periodo**.

![Generador de declaraciones - Datos genéricos](../../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/modelo-303/generador-declaraciones-datos-genericos.png)

A continuación, introduzca los parámetros de entrada — datos que no se obtienen automáticamente de Etendo — mediante el botón de proceso **Parámetros de entrada**.

!!! info
    Algunos parámetros de entrada, como **Inscrito en el Registro Devolución Mensual**, pueden configurarse como parámetros constantes para no tener que introducirlos cada vez que se genera el fichero del 303.

Para configurar un parámetro como constante:

1. Acceda a :material-menu: `Gestión Financiera` > `Contabilidad` > `Configuración` > `Declaración de Impuestos`.
2. Localice la sección de declaración que contiene el parámetro a configurar. El parámetro **Inscrito en el Registro de devolución mensual** se encuentra en la sección **Identificación**.
3. En ese parámetro, cambie el tipo de *Entrada* a *Constante*.
4. En el campo **Valor constante** (*Constant Value*), introduzca `1` si el sujeto pasivo está inscrito en el registro de devolución mensual, o `2` si no lo está.

!!! warning
    Si se produce una actualización de los datos de referencia de este módulo, los cambios de parámetros de tipo *Entrada* a *Constante* se sobreescriben. Vuelva a configurarlos tras cada actualización.

Las secciones de la ventana de parámetros se corresponden con las secciones definidas para el Modelo 303.

Secciones **Fichero**, **Tipo de declaración** y **Sin actividad**:

![Secciones Fichero, Tipo de declaración y Sin actividad](../../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/modelo-303/seccion-fichero-tipo-dec-sin-act.png)

Secciones **IVA deducible**, **Liquidación-resultado** y **Banco**:

![Secciones IVA deducible, Liquidación-resultado y Banco](../../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/modelo-303/seccion-iva-deducible-liquidacion-banco.png)

Secciones **Complementaria**, **Tributación por razón de territorio** y **Additional Information** *(este nombre aparece en inglés en la aplicación)*:

![Secciones Complementaria, Tributación por razón de territorio y Additional Information](../../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/modelo-303/seccion-complementaria-tributacion.png)

Una vez generado, el fichero tiene el siguiente aspecto:

![Fichero generado del Modelo 303](../../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/modelo-303/fichero-generado-303.png)

## Pre-validación y Presentación

Pre-valide el fichero generado en Etendo en el siguiente enlace de la AEAT:

[_Formulario del modelo 303 para su presentación (predeclaración) ejercicio 2014 y siguientes (Régimen General)_](https://www2.agenciatributaria.gob.es/es13/h/ie43030b.html){target="_blank"}.

En ese enlace, importe el fichero mediante la opción **Optativo: Importar datos de fichero**. Los datos del fichero se muestran para su validación.

Una vez validados los datos, preséntelo en el siguiente enlace — se requiere certificado electrónico de identificación o DNI electrónico: [_Presentación ejercicio 2014 y siguientes (Régimen General)_](https://www.agenciatributaria.gob.es/AEAT.sede/procedimientoini/G414.shtml){target="_blank"}.

## Referencia

Esta sección es de consulta opcional. Describe cómo Etendo clasifica internamente cada tipo de factura en las casillas del Modelo 303. Si solo necesita generar el fichero, vaya directamente a [Generación del Modelo 303](#generacion-del-modelo-303).

### Secciones del Modelo 303

La configuración del Modelo 303 se instala por defecto. Compruébela en:

:material-menu: `Gestión Financiera` > `Contabilidad` > `Configuración` > `Declaración de Impuestos`

Tanto para el Modelo 303 mensual como trimestral, la solapa **Sección de declaración** contiene 11 secciones, una por cada grupo de información a incluir al generar el fichero del Modelo 303:

![Declaración de Impuestos - Secciones del 303](../../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/modelo-303/declaracion-impuestos-secciones.png)

-   **Fichero**
    -   Esta sección contiene un parámetro de tipo *Entrada* para introducir el nombre del fichero 303 al generarlo.
-   **Tipo de declaración**
    -   Esta sección contiene 8 parámetros de tipo *Entrada*, uno por cada tipo de declaración, para marcar el correspondiente al generar el fichero.
        -   Compensación
        -   Devolución
        -   Ingreso
        -   Resultado cero
        -   Ingreso domiciliación bancaria
        -   Ingreso cuenta corriente tributaria
        -   Devolución cuenta corriente tributaria
        -   Devolución por transferencia al extranjero
-   **Sin Actividad**
    -   Esta sección contiene 1 parámetro de tipo *Entrada* para marcar una liquidación de IVA como *Sin Actividad*.
-   **Constantes**
    -   Esta sección incluye todos los valores constantes que requiere el 303, tales como:
        -   Modelo = 303
        -   Página = 01
        -   Identificador de fin de registro = </T30301>
-   **Identificación**
    -   Esta sección incluye 4 parámetros de *Salida* que se corresponden con datos de identificación de la organización para la cual se genera el fichero, y 1 parámetro de *Entrada* de tipo checkbox: **Inscrito en el Registro de devolución mensual**, que puede configurarse como constante.
-   **IVA Devengado**
    -   Esta sección incluye 3 parámetros de tipo *Salida*, uno por cada tipo de IVA devengado.
        -   **IVA Devengado - Régimen General**: ligado a los rangos de impuestos cuyas operaciones tributan en régimen general, por ejemplo, las entregas de bienes y servicios dentro del territorio de aplicación del impuesto.
        -   **IVA Devengado - Recargo de Equivalencia**: ligado a los rangos de impuestos cuyas operaciones tributan en régimen de recargo de equivalencia, por ejemplo, las entregas de bienes a minoristas dentro del territorio de aplicación del impuesto.
        -   **IVA Devengado - Adquisiciones Intracomunitarias**: ligado a los rangos de impuestos de adquisiciones intracomunitarias de bienes.

Consulte el listado completo de los rangos de impuesto ligados a cada parámetro en el anexo al final de este documento.

-   **IVA Deducible**
    -   Esta sección incluye un total de 12 parámetros: 6 de tipo *Salida* y 6 de tipo *Entrada*.  
        Los parámetros de tipo *Salida* se corresponden con los tipos de IVA Deducible obtenibles desde Etendo, por ejemplo, **IVA Deducible por cuotas soportadas en operaciones interiores corrientes**.  
        Los parámetros de tipo *Entrada* se corresponden con tipos de IVA Deducible para los que no se obtiene información de Etendo, por ejemplo, **IVA Deducible por compensación Régimen Esp. A.G y P.(cuota)**.

Consulte el listado completo de los rangos de impuesto ligados a cada parámetro en el anexo al final de este documento.

-   **Diferencia**
    -   Esta sección incluye 4 parámetros de tipo *Entrada* para introducir la siguiente información al generar el fichero:
        -   **% Atribuible a la Administración del Estado**: los sujetos pasivos que tributen conjuntamente en la Administración del Estado y en las Diputaciones del País Vasco o la Comunidad Foral de Navarra deben indicar el porcentaje del volumen de operaciones en territorio común. El resto de sujetos pasivos indican un 100%. Este dato puede configurarse como constante.
        -   **Cuotas a compensar de periodos anteriores**: indique, cuando sea aplicable, las cuotas positivas a compensar procedentes de periodos anteriores.
        -   **Resultado de la regularización anual**: en la última liquidación del año, indique el resultado de la regularización anual por inversiones.
        -   **A deducir (autoliquidación complementaria)**: exclusivamente en el caso de declaración complementaria, indique el resultado de la última declaración presentada por el mismo concepto, correspondiente al mismo ejercicio y periodo.
    -   Esta sección incluye además 3 parámetros de salida correspondientes a operaciones no sujetas que originan derecho a deducción:
        -   **Entregas Intracomunitarias de bienes**: ligado a los rangos de impuestos siguientes:
            -   Entregas intracomunitarias (%N=>0%)
            -   Entregas intracomunitarias (%R=>0%)
            -   Entregas intracomunitarias (%SR=>0%)
            -   Entregas intracomunitarias Bienes Inversión (%N=>0%)
        -   **Exportaciones y Operaciones asimiladas**: ligado a los rangos de impuestos siguientes:
            -   Entregas a Canarias,Ceuta y Melilla (%N=>0%)
            -   Entregas a Canarias,Ceuta y Melilla (%SR=>0%)
            -   Entregas a Canarias,Ceuta y Melilla (%R=>0%)
            -   Exportaciones (%N=>0%)
            -   Exportaciones (%R=>0%)
            -   Exportaciones (%SR=>0%)
            -   Exportaciones Bienes Inversión (%N=>0%)
        -   **Operaciones no sujetas o con inversión del sujeto pasivo**: ligado a los rangos de impuestos siguientes:
            -   Servicios a Canarias, Ceuta y Melilla (%N=>0%)
            -   Servicios a Canarias, Ceuta y Melilla (%SR=>0%)
            -   Servicios a Canarias, Ceuta y Melilla (%R=>0%)
            -   Servicios prestados internacional (%N=>0%)
            -   Servicios prestados internacional (%R=>0%)
            -   Servicios prestados UE (%N=>0%)
            -   Servicios prestados UE (%R=>0%)
-   **Devolución**
    -   Esta sección incluye un parámetro de tipo *Entrada*: la cuenta bancaria a utilizar en caso de declaración a devolver. Este dato puede configurarse como constante.
-   **Ingreso**
    -   Esta sección incluye 5 parámetros de tipo *Entrada* relativos a declaraciones *A ingresar*:
        -   la cuenta bancaria a utilizar en caso de declaración a ingresar. Este dato puede configurarse como constante.
        -   No consta
        -   Efectivo
        -   Adeudo en cuenta
        -   Domiciliación
-   **Complementaria**
    -   Esta sección incluye 2 parámetros de tipo *Entrada*:
        -   Declaración complementaria, como un checkbox (si/no)
        -   Nº Justificante de la declaración anterior que se complementa.

### Tipos de Documento y Fecha

Al generar el fichero de texto válido para declarar el Modelo 303 de liquidación de IVA, se tiene en cuenta:

-   El IVA (soportado) deducible registrado y contabilizado en las facturas y abonos de compra, que puede registrar en: :material-menu: `Gestión de Compras` > `Transacciones` > `Factura (Proveedor)`, para los siguientes tipos de documento:
    -   `AP Invoice` (Factura de compra)
    -   `AP Invoice` negativa (Abono de compra)
    -   `AP Credit Memo` (Abono de compra)
-   El IVA devengado registrado y contabilizado en las facturas y abonos de venta que puede emitir en: :material-menu: `Gestión de Ventas` > `Transacciones` > `Factura (Cliente)`, para los siguientes tipos de documento:
    -   `AR Invoice` (Factura de venta)
    -   `AR Invoice` negativa (Abono de venta)
    -   `AR Credit Memo` (Abono de venta)

La versión actual del módulo no tiene en cuenta los tipos de documento de Etendo sin APRM que se enumeran a continuación, por considerarse que no deben utilizarse para la contabilización de facturas que incluyan IVA:

-   Extracto bancario
-   Diario de Caja
-   Liquidaciones y asientos manuales

**La fecha que se tiene en cuenta** para la inclusión de las facturas de compra y venta en la declaración del 303 es la **fecha de contabilización**, lo que implica que:

-   Las facturas con fecha de contabilización dentro de un mes determinado se incluyen en la declaración mensual de ese mes.
-   Las facturas con fecha de contabilización dentro de un trimestre determinado se incluyen en la declaración trimestral correspondiente.

### IVA Devengado - Escenarios

El principal objetivo del Modelo 303 es que las empresas españolas autoliquiden el IVA regularmente como diferencia entre el IVA Devengado en facturas emitidas de venta y el IVA soportado deducible.

El fichero del 303 recoge desde la posición 72 a la 357 la base imponible, tipo y cuota del IVA devengado en las operaciones de venta bajo el régimen general, especificando por tipo de IVA (16%/18%, 7%/8% y 4%), régimen de recargo de equivalencia especificado por tipo de IVA (4%, 1% y 0,5%), así como la base y cuota del IVA devengado en las adquisiciones intracomunitarias.

#### IVA Devengado - Régimen General

Durante el periodo correspondiente (mes/trimestre), registre y contabilice en Etendo las facturas y abonos de venta emitidos tanto por la entrega de bienes como por la prestación de servicios dentro del territorio de aplicación del impuesto/IVA (Península y Baleares).

Se tienen en cuenta:

1.  Las facturas y abonos emitidos por la venta de productos o por la prestación de servicios, contabilizados en: :material-menu: `Gestión de Ventas` > `Transacciones` > `Factura (Cliente)`.
2.  Las facturas y abonos financieros emitidos desde: :material-menu: `Gestión de Ventas` > `Transacciones` > `Factura (Cliente)`, marcados como **Factura Financiera** a nivel de línea de factura de venta, ligados a un concepto contable previamente creado y asignado a una categoría de impuesto.
3.  Las líneas de impuesto introducidas manualmente en: :material-menu: `Gestión de Ventas` > `Transacciones` > `Factura (Cliente)` > `Cabecera` > `Impuestos`.

El fichero del 303 recoge dichas transacciones dentro del mes/trimestre correspondiente, teniendo en cuenta la fecha de contabilización. El IVA se devenga cuando se realiza la puesta a disposición de los bienes o la prestación del servicio, lo que conlleva la facturación correspondiente. Las facturas deben contabilizarse para que se tengan en cuenta.

Los productos, servicios y conceptos contables deben estar ligados a una de las siguientes categorías de impuestos:

-   IVA Normal
-   IVA Reducido
-   IVA Super reducido
-   IVA Normal Servicios
-   IVA Reducido Servicios
-   IVA Super Reducido Servicios
-   IVA Normal B. Inmuebles
-   IVA Reducido B. Inmuebles
-   IVA Normal Bienes Inversión

Las líneas de facturas deben tener un rango de impuesto asociado a uno de los parámetros del 303 de la sección **IVA Devengado - Régimen General**.

#### IVA Devengado - Régimen de Recargo de Equivalencia

Durante el periodo correspondiente (mes/trimestre), registre y contabilice en Etendo las facturas y abonos de venta emitidos por la entrega de bienes dentro del territorio de aplicación del impuesto/IVA (Península y Baleares) a terceros minoristas en régimen de recargo de equivalencia.

En estos casos, el emisor de la factura incluye, además del IVA, el tipo (%) de recargo correspondiente.

Se tienen en cuenta:

1.  Las facturas y abonos emitidos por la venta de productos, contabilizados en: :material-menu: `Gestión de Ventas` > `Transacciones` > `Factura (Cliente)`.
2.  Las facturas y abonos financieros emitidos desde: :material-menu: `Gestión de Ventas` > `Transacciones` > `Factura (Cliente)`, marcados como **Factura Financiera** a nivel de línea de factura de venta, ligados a un concepto contable previamente creado y asignado a una categoría de impuesto.
3.  Las líneas de impuesto introducidas manualmente en: :material-menu: `Gestión de Ventas` > `Transacciones` > `Factura (Cliente)` > `Cabecera` > `Impuestos`.

El fichero del 303 recoge dichas transacciones dentro del mes/trimestre correspondiente, teniendo en cuenta la fecha de contabilización. El IVA se devenga cuando se realiza la puesta a disposición de los bienes, lo que conlleva la facturación correspondiente. Las facturas deben contabilizarse para que se tengan en cuenta.

Los productos, servicios y conceptos contables deben estar ligados a una de las siguientes categorías de impuestos:

-   IVA Normal
-   IVA Reducido
-   IVA Super reducido

Las líneas de facturas deben tener un rango de impuesto asociado a uno de los parámetros del 303 de la sección **IVA Devengado - Recargo de Equivalencia**.

#### IVA Devengado - Adquisiciones Intracomunitarias

Durante el periodo correspondiente (mes/trimestre), registre y contabilice en Etendo las facturas y abonos de compra recibidos de proveedores no residentes en el territorio de aplicación del impuesto pero residentes en la Unión Europea (operadores intracomunitarios), por la adquisición de bienes dentro del territorio de aplicación del impuesto/IVA (Península y Baleares).

Se tienen en cuenta:

1.  Las facturas y abonos registrados en el sistema por la compra de productos, contabilizados en: :material-menu: `Gestión de Compras` > `Transacciones` > `Factura (Proveedor)`.
2.  Las facturas y abonos financieros emitidos desde: :material-menu: `Gestión de Compras` > `Transacciones` > `Factura (Proveedor)`, marcados como **Factura Financiera** a nivel de línea de factura de compra, ligados a un concepto contable previamente creado y asignado a una categoría de impuesto.
3.  Las líneas de impuesto introducidas manualmente en: :material-menu: `Gestión de Compras` > `Transacciones` > `Factura (Proveedor)` > `Cabecera` > `Impuestos`.

Los productos y conceptos contables deben estar relacionados con una de las siguientes categorías de impuesto:

-   IVA Normal
-   IVA Reducido
-   IVA Super Reducido

Las líneas de facturas deben tener un rango de impuesto asociado a uno de los parámetros del 303 de la sección **IVA Devengado - Adquisiciones Intracomunitarias**.

Las adquisiciones intracomunitarias se consideran realizadas en el territorio de aplicación del impuesto cuando:

-   se encuentre en este territorio el lugar de la llegada de la expedición o transporte con destino al adquirente.
-   el adquirente haya comunicado al vendedor el número de identificación a efectos del IVA atribuido por la Administración española.

Este régimen se caracteriza por el gravamen en destino de las entregas intracomunitarias realizadas entre empresas. Se aplica una exención en el país de origen y el hecho imponible se considera realizado en el de destino, con motivo de la adquisición. Esto se denomina *adquisición intracomunitaria de bienes*, y altera la regla general del impuesto: el sujeto pasivo es quien compra, no quien vende.

El sujeto pasivo/adquiriente es quien debe liquidar el IVA. Debe autorrepercutirse el IVA y a su vez deducírselo, si aplica. Por ello, este tipo de operaciones — como las de Inversión de Sujeto Pasivo — aparecen tanto en la sección de IVA devengado como en la de IVA deducible.

### IVA Deducible - Escenarios

El principal objetivo del Modelo 303 es que las empresas españolas autoliquiden el IVA regularmente como diferencia entre el IVA Devengado en facturas emitidas de venta y el IVA soportado deducible.

El fichero del 303 recoge desde la posición 357 a la 612 la base imponible y cuota, en la mayoría de los casos, del IVA soportado deducible en operaciones interiores, importaciones y adquisiciones intracomunitarias de bienes corrientes (bienes y servicios) y de bienes de inversión.

#### IVA Deducible - Cuotas Soportadas en Operaciones Interiores Corrientes

Durante el periodo correspondiente (mes/trimestre), registre y contabilice en Etendo las facturas y abonos de compra recibidos de proveedores tanto por la compra de bienes como por los servicios prestados a la empresa dentro del territorio de aplicación del impuesto/IVA (Península y Baleares), así como las facturas financieras.

Los productos, servicios y conceptos contables deben estar relacionados con una de las siguientes categorías de impuesto:

-   IVA Normal
-   IVA Reducido
-   IVA Super Reducido
-   IVA Normal Servicios
-   IVA Reducido Servicios
-   IVA Super Reducido Servicios
-   IVA Normal B. Inmuebles
-   IVA Reducido B. Inmuebles

Las líneas de facturas deben tener un rango de impuesto asociado a uno de los parámetros del 303 de la sección **IVA Deducible - Por cuotas soportadas en operaciones interiores corrientes**.

#### IVA Deducible - Operaciones Interiores Bienes de Inversión

Durante el periodo correspondiente (mes/trimestre), registre y contabilice en Etendo las facturas y abonos de compra recibidos de proveedores por la compra de bienes de inversión (se consideran bienes de inversión los bienes con un valor superior a 3.000,00 €) dentro del territorio de aplicación del impuesto/IVA (Península y Baleares), así como las facturas financieras.

Los productos, servicios y conceptos contables deben estar relacionados con la siguiente categoría de impuesto:

-   IVA Normal Bienes Inversión

Las líneas de facturas deben tener un rango de impuesto asociado a uno de los parámetros del 303 de la sección **IVA Deducible - Operaciones interiores bienes de inversión**.

#### IVA Deducible - Por Cuotas Devengadas en Importaciones de Bienes

Durante el periodo correspondiente (mes/trimestre), registre y contabilice en Etendo las facturas y abonos de compra recibidos de proveedores no residentes en el territorio de aplicación del impuesto, por la importación de bienes dentro del territorio de aplicación del impuesto/IVA (Península y Baleares), así como las facturas financieras.

Los productos y conceptos contables deben estar relacionados con una de las siguientes categorías de impuesto:

-   IVA Normal
-   IVA Reducido
-   IVA Super Reducido

Las líneas de facturas deben tener un rango de impuesto asociado a uno de los parámetros del 303 de la sección **IVA Deducible - Por cuotas devengadas en las importaciones de bienes corrientes**.

#### IVA Deducible - Importaciones Bienes de Inversión

Durante el periodo correspondiente (mes/trimestre), registre y contabilice en Etendo las facturas y abonos de compra recibidos de proveedores no residentes en el territorio de aplicación del impuesto, por la importación de bienes de inversión dentro del territorio de aplicación del impuesto/IVA (Península y Baleares), así como las facturas financieras.

Los productos y conceptos contables deben estar relacionados con la siguiente categoría de impuesto:

-   IVA Normal Bienes Inversión

Las líneas de facturas deben tener un rango de impuesto asociado a uno de los parámetros del 303 de la sección **IVA Deducible - Importaciones bienes de inversión**.

#### IVA Deducible - Adquisiciones Intracomunitarias de Bienes

Durante el periodo correspondiente (mes/trimestre), registre y contabilice en Etendo las facturas y abonos de compra recibidos de proveedores no residentes en el territorio de aplicación del impuesto pero residentes en la Unión Europea (operadores intracomunitarios), por la adquisición de bienes dentro del territorio de aplicación del impuesto/IVA (Península y Baleares), así como las facturas financieras.

Los productos y conceptos contables deben estar relacionados con una de las siguientes categorías de impuesto:

-   IVA Normal
-   IVA Reducido
-   IVA Super Reducido

Las líneas de facturas deben tener un rango de impuesto asociado a uno de los parámetros del 303 de la sección **IVA Deducible - adquisiciones intracomunitarias de bienes corrientes**.

Las adquisiciones intracomunitarias se consideran realizadas en el territorio de aplicación del impuesto cuando:

-   se encuentre en este territorio el lugar de la llegada de la expedición o transporte con destino al adquirente.
-   el adquirente haya comunicado al vendedor el número de identificación a efectos del IVA atribuido por la Administración española.

Este régimen se caracteriza por el gravamen en destino de las entregas intracomunitarias realizadas entre empresas. Se aplica una exención en el país de origen y el hecho imponible se considera realizado en el de destino, con motivo de la adquisición. Esto se denomina *adquisición intracomunitaria de bienes*, y altera la regla general del impuesto: el sujeto pasivo es quien compra, no quien vende.

El sujeto pasivo/adquiriente es quien debe liquidar el IVA. Debe autorrepercutirse el IVA y a su vez deducírselo, si aplica. Por ello, este tipo de operaciones — como las de Inversión de Sujeto Pasivo — aparecen tanto en la sección de IVA devengado como en la de IVA deducible.

#### IVA Deducible - Adquisiciones Intracomunitarias de Bienes de Inversión

Durante el periodo correspondiente (mes/trimestre), registre y contabilice en Etendo las facturas y abonos de compra recibidos de proveedores no residentes en el territorio de aplicación del impuesto pero residentes en la Unión Europea (operadores intracomunitarios), por la adquisición de bienes de inversión dentro del territorio de aplicación del impuesto/IVA (Península y Baleares), así como las facturas financieras.

Los productos y conceptos contables deben estar relacionados con la siguiente categoría de impuesto:

-   IVA Normal Bienes Inversión

Las líneas de facturas deben tener un rango de impuesto asociado a uno de los parámetros del 303 de la sección **IVA Deducible - adquisiciones intracomunitarias de bienes de inversión**.

### Diferencia - Escenarios

El fichero del 303 recoge desde la posición 629 a la 804 los datos relativos a la diferencia entre el IVA Devengado y el Deducible, junto con otra información adicional necesaria para el cálculo del resultado final (casilla \[48\]).

Desde Etendo puede obtener la diferencia entre IVA Devengado y Deducible, así como parte de la información adicional necesaria. El resto debe introducirse como parámetros de entrada al generar el fichero.

La información disponible desde el sistema corresponde a las bases imponibles para un periodo determinado (mes/trimestre) respecto de las siguientes operaciones:

-   **Entregas intracomunitarias**: el sistema tiene en cuenta las facturas, abonos y facturas financieras de venta a clientes no residentes en el territorio de aplicación del impuesto pero residentes en la Unión Europea, emitidos y contabilizados, por la entrega exenta de IVA de bienes fuera del territorio de aplicación del impuesto/IVA (Península y Baleares).  
    Las líneas de facturas deben tener un rango de impuesto asociado a uno de los parámetros del 303 de la sección **Diferencia - Entregas Intracomunitarias**.
-   **Exportaciones y operaciones asimiladas**: el sistema tiene en cuenta las facturas, abonos y facturas financieras de venta emitidas y contabilizadas a clientes extranjeros, por la entrega exenta de IVA de bienes fuera del territorio de aplicación del impuesto/IVA (Península y Baleares).  
    Las líneas de facturas deben tener un rango de impuesto asociado a uno de los parámetros del 303 de la sección **Diferencia - Exportaciones y Operaciones Asimiladas**.
-   **Operaciones no sujetas o con inversión del sujeto pasivo** que originan derecho a deducción: aplica a facturas, abonos y facturas financieras de venta emitidos y contabilizados por la prestación de servicios de la empresa fuera del territorio de aplicación del impuesto, servicios exentos pero que originan derecho a deducción.  
    Las líneas de facturas deben tener un rango de impuesto asociado a uno de los parámetros del 303 de la sección **Diferencia - Operaciones no sujetas o con inversión del sujeto pasivo**.

Introduzca el resto de datos manualmente al generar el Modelo 303 desde la ventana **Generador de declaraciones de impuestos**:

![Generador de declaraciones de impuestos - Diferencia](../../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/modelo-303/generador-declaraciones-diferencia.png)

### Devoluciones - Escenarios

#### Devoluciones - Devolución/Devolución Cuenta Corriente Tributaria

Para este tipo de declaraciones, y siempre que el check **Inscrito en registro de devolución mensual** esté marcado, los siguientes campos son obligatorios:

- **IBAN**
- **Marca SEPA**: indique si la cuenta bancaria pertenece a la zona SEPA. Consulte con su entidad bancaria si no está seguro.

#### Devoluciones - Devolución por Transferencia al Extranjero

Para este tipo de declaraciones, y siempre que el check **Inscrito en registro de devolución mensual** esté marcado, los siguientes campos son obligatorios:

- **IBAN** (cuenta bancaria para la devolución)
- **Nombre del banco** (*Bank name*)
- **Dirección del banco** (*Bank address*)
- **Ciudad** (*City*)
- **Código de país** (*Country code*)
- **Marca SEPA**: indique si la cuenta bancaria pertenece a la zona SEPA. Consulte con su entidad bancaria si no está seguro.

??? info "Anexo — Listado completo de rangos de impuesto"

    Este anexo incluye el listado completo de los rangos de impuestos asociados a los parámetros del Modelo 303 de las secciones **IVA Devengado** e **IVA Deducible** incluidos en el dataset del módulo:

    ### **IVA Devengado**

    #### **IVA Devengado - Régimen General**

    -   Arrendamiento 18% (cobros)
    -   Arrendamientos 18% -21%R (cobros) (+18%)
    -   Arrendamiento 21% (cobros)
    -   Arrendamientos 21% -21%R (cobros) (+21%)
    -   Entregas Bienes Inversión 18%
    -   Entregas Bienes Inversión 21%
    -   Entregas IVA 18%
    -   Entregas IVA 8%
    -   Entregas IVA 21%
    -   Entregas IVA 10%
    -   Entregas IVA 4%
    -   Entregas IVA+RE 18+4% (+18%)
    -   Entregas IVA+RE 8+1% (+8%)
    -   Entregas IVA+RE 21+5.2% (+21%)
    -   Entregas IVA+RE 10+1.4% (+10%)
    -   Entregas IVA+RE 4+0.5% (+4%)
    -   Inversión Sujeto Pasivo no UE 18% (-18%)
    -   Inversión Sujeto Pasivo no UE 8% (-8%)
    -   Inversión Sujeto Pasivo no UE 21% (-21%)
    -   Inversión Sujeto Pasivo no UE 10% (-10%)
    -   Inversión Sujeto Pasivo UE 18% (-18%)
    -   Inversión Sujeto Pasivo UE 8% (-8%)
    -   Inversión Sujeto Pasivo UE 21% (-21%)
    -   Inversión Sujeto Pasivo UE 10% (-10%)
    -   Servicios prestados nacional 18%
    -   Servicios prestados nacional 21%
    -   Servicios prestados nacional 18% -15%R (+18%)
    -   Servicios prestados nacional 18% -7%R (+18%)
    -   Servicios prestados nacional 21% -21%R (+21%)
    -   Servicios prestados nacional 21% -9%R (+21%)
    -   Servicios prestados nacional 8%
    -   Servicios prestados nacional 10%
    -   Servicios prestados nacional 4%
    -   Transmisión B.Inmuebles 18%
    -   Transmisión B.Inmuebles 8%
    -   Transmisión B.Inmuebles 21%
    -   Transmisión B.Inmuebles 10%

    #### **IVA Devengado - Recargo de equivalencia**

    -   Entregas IVA+RE 18+4% (+4%)
    -   Entregas IVA+RE 8+1% (+1%)
    -   Entregas IVA+RE 21+5.2% (+5.2%)
    -   Entregas IVA+RE 10+1.4% (+1.4%)
    -   Entregas IVA+RE 4+0.5% (+0.5%)

    #### **IVA Devengado - Adquisiciones Intracomunitarias**

    -   Adquisiciones intracomunitarias 18% (-18%)
    -   Adquisiciones intracomunitarias 8% (-8%)
    -   Adquisiciones intracomunitarias 21% (-21%)
    -   Adquisiciones intracomunitarias 10% (-10%)
    -   Adquisiciones intracomunitarias 4% (-4%)
    -   Adquisiciones intracomunitarias Bienes Inversión 18% (-18%)
    -   Adquisiciones intracomunitarias Bienes Inversión 21% (-21%)

    ### **IVA Deducible**

    #### **IVA Deducible - Por cuotas soportadas en operaciones interiores corrientes**

    -   Adquisición B.Inmuebles 18%
    -   Adquisición B.Inmuebles 8%
    -   Adquisición B.Inmuebles 21%
    -   Adquisición B.Inmuebles 10%
    -   Adquisiciones IVA 18%
    -   Adquisiciones IVA 8%
    -   Adquisiciones IVA 21%
    -   Adquisiciones IVA 10%
    -   Adquisiciones IVA 4%
    -   Arrendamiento 18% (pagos)
    -   Arrendamiento 21% (pagos)
    -   Arrendamientos 18% -21%R (pagos) (+18%)
    -   Arrendamientos 21% -21%R (pagos) (+21%)
    -   Inversión Sujeto Pasivo no UE 18% (+18%)
    -   Inversión Sujeto Pasivo no UE 8% (+8%)
    -   Inversión Sujeto Pasivo no UE 21% (+21%)
    -   Inversión Sujeto Pasivo no UE 10% (+10%)
    -   Inversión Sujeto Pasivo UE 18% (+18%)
    -   Inversión Sujeto Pasivo UE 8% (+8%)
    -   Inversión Sujeto Pasivo UE 21% (+21%)
    -   Inversión Sujeto Pasivo UE 10% (+10%)
    -   Prestación servicios nacional 18%
    -   Prestación servicios nacional 21%
    -   Prestación servicios nacional 18% -15%R (+18%)
    -   Prestación servicios nacional 18% -1%R (18%)
    -   Prestación servicios nacional 18% -7%R (+18%)
    -   Prestación servicios nacional 21% -21%R (+21%)
    -   Prestación servicios nacional 21% -1%R (+21%)
    -   Prestación servicios nacional 21% -9%R (+21%)
    -   Prestación servicios nacional 8%
    -   Prestación servicios nacional 10%
    -   Prestación servicios nacional 4%

    #### **IVA Deducible - Operaciones interiores bienes de inversión**

    -   Adquisición Bienes Inversión18%
    -   Adquisición Bienes Inversión 21%

    #### **IVA Deducible - Por cuotas devengadas en las importaciones de bienes corrientes**

    -   Adquisiciones a Canarias,Ceuta y Melilla 18%
    -   Adquisiciones a Canarias,Ceuta y Melilla 8%
    -   Adquisiciones a Canarias,Ceuta y Melilla 21%
    -   Adquisiciones a Canarias,Ceuta y Melilla 10%
    -   Adquisiciones a Canarias,Ceuta y Melilla 4%
    -   Importaciones 18%
    -   Importaciones 8%
    -   Importaciones 21%
    -   Importaciones 10%
    -   Importaciones 4%

    #### **IVA Deducible - Importaciones bienes de inversión**

    -   Importaciones Bienes Inversión 18%
    -   Importaciones Bienes Inversión 21%

    #### **IVA Deducible - En adquisiciones intracomunitarias de bienes de corrientes**

    -   Adquisiciones intracomunitarias 18% (+18%)
    -   Adquisiciones intracomunitarias 8% (+8%)
    -   Adquisiciones intracomunitarias 21% (+21%)
    -   Adquisiciones intracomunitarias 10% (+10%)
    -   Adquisiciones intracomunitarias 4% (+4%)

    #### **IVA Deducible - Adq. Intracomunitarias bienes de inversión**

    -   Adquisiciones intracomunitarias Bienes Inversión 18% (+18%)
    -   Adquisiciones intracomunitarias Bienes Inversión 21% (+21%)

*[AEAT]: Agencia Estatal de Administración Tributaria
*[IVA]: Impuesto sobre el Valor Añadido
*[NIF]: Número de Identificación Fiscal
*[IAE]: Impuesto de Actividades Económicas
*[UE]: Unión Europea
*[IBAN]: International Bank Account Number
*[SEPA]: Single Euro Payments Area

---

This work is a derivative of [Openbravo Localización Española](https://wiki.openbravo.com/wiki/Openbravo_Localizaci%C3%B3n_Espa%C3%B1a){target="_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}. This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Etendo](https://etendo.software){target="_blank"}.
