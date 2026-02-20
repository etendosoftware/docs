---
title: Modelo 303
tags:
    - Modelo 303
    - Localización Española
---

## Paquetes Java

:octicons-package-16: Paquete Java: `org.openbravo.module.aeat303.es` <br>

## **Introducción**

El presente manual de usuario explica el contenido y funcionamiento del nuevo módulo comercial de Etendo, **"Modelo AEAT303"**, compatible con Etendo 21.4 o versiones posteriores. Este módulo forma parte del bundle de Localización española, al igual que todas las dependencias relacionadas.
## **Descripción del módulo**

El módulo Modelo AEAT303 - Impuesto sobre el Valor Añadido - Autoliquidación permite a las empresas cumplir con sus obligaciones fiscales de "Autoliquidación de IVA" como diferencia entre el IVA devengado y el IVA deducible, a través de la presentación del Modelo 303 como un fichero de texto válido conforme a los requerimientos establecidos por la Agencia Tributaria española (Orden EHA/3786/2008).

La estructura válida del fichero se puede encontrar en el siguiente enlace de la AEAT: [](http://www.aeat.es/AEAT/Contenidos_Comunes/La_Agencia_Tributaria/Ayuda/Disenyos_de_registro/Ayudas/Trimestrales_Mensuales/303_2009.pdf)[_Modelo 303 - Fichero_](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-303/presentacion-electronica-modelo-303-fichero.html){target="_blank"}.

El fichero del Modelo 303 contiene la siguiente información:

-   **Información genérica**
    -   NIF
    -   Apellidos o razón social - nombre
    -   Ejercicio
    -   Periodo
-   **IVA devengado** (IVA repercutido en ventas), incluyendo:
    -   IVA devengado conforme al régimen general - base, cuota y tipo
    -   IVA devengado conforme al régimen especial de recargo de equivalencia, especificado por tipo de IVA - base, cuota y tipo
    -   IVA devengado en las adquisiciones intracomunitarias de bienes - base y cuota
-   **IVA deducible** (IVA soportado en compras), incluyendo:
    -   operaciones interiores de bienes y servicios - base y cuota
    -   operaciones interiores de bienes de inversión - base y cuota
    -   importaciones de bienes - base y cuota
    -   importaciones de bienes de inversión - base y cuota
    -   adquisiciones intracomunitarias de bienes - base y cuota
    -   adquisiciones intracomunitarias de bienes de inversión - base y cuota
    -   regularizaciones
-   **Diferencia** - resultado de la liquidación como diferencia del IVA devengado - IVA soportado deducible, incluyendo otras operaciones tales como:
    -   entregas intracomunitarias de bienes - base
    -   exportaciones - base
    -   operaciones no sujetas o con inversión del sujeto pasivo - base
-   **Datos bancarios y otros.**

Dicho fichero se genera en Etendo desde el Generador de declaraciones de impuestos que se encuentra en la ruta de aplicación: "Gestión Financiera || Contabilidad || Herramientas de análisis || Generador de declaraciones de impuestos"

El fichero se puede:

1.  **prevalidar** en la página web de la AEAT, en el siguiente enlace: [**_Formulario del 303 para su presentación (predeclaración)_**](https://www2.agenciatributaria.gob.es/es13/h/ie93030b.html){target="_blank"}.
2.  y, posteriormente, **presentar** en el siguiente enlace de la AEAT: [**_Presentación del Modelo_**_._](https://www2.agenciatributaria.gob.es/es13/h/ie93030a.html){target="_blank"}.

La autoliquidación de IVA puede ser:

-   "**A ingresar**" (casilla 48>0), en el caso de que el IVA devengado > IVA deducible. El IVA a ingresar se reflejará en la casilla \[I\], posición 860.
-   "**A compensar**" (casilla 48<0), en el caso de que el IVA devengado < IVA deducible. El IVA a compensar se reflejará en la casilla \[49\], posición 804.
-   "**A devolver**" (casilla 48<0 e inscripción en el Registro de devolución mensual), en el caso de que el IVA devengado < IVA deducible. El IVA a devolver se reflejará en la casilla \[50\], posición 822.
-   "**Cero**" o "**Sin actividad**" (casilla 48=0).
## **Presentación del Modelo 303**

Los obligados a presentar el modelo 303 son:

-   Los sujetos pasivos que realicen actividades a las que aplique el Régimen General del Impuesto (IVA) o cualquier otro de los regímenes del mismo, a excepción del Régimen especial de agricultura, ganadería y pesca, del Régimen de recargo de equivalencia y del Régimen Simplificado.

La presentación del modelo 303 puede ser mensual o trimestral.

La presentación será obligatoria por vía telemática (fichero de texto válido) para los sujetos pasivos que:

-   tengan forma jurídica de sociedad anónima o sociedad de responsabilidad limitada
-   y/o estén inscritos en el "Régimen de devolución mensual".

### **Novedades a partir del 1 de julio de 2010**

**MODIFICACIÓN TIPOS IMPOSITIVOS IVA**

La Ley 26/2009 de Presupuestos Generales del Estado para 2010 modificó los tipos general y reducido del Impuesto sobre el Valor Añadido con efectos a partir del 1 de julio, de forma que el tipo general pasa del 16% al 18% y el tipo reducido pasa del 7% al 8%, sin que se haya producido alteración alguna en relación con el tipo superreducido del 4% y con los tipos del recargo de equivalencia.

**Cumplimentación de declaraciones**

En las autoliquidaciones de IVA, modelo 303, correspondientes a los períodos iniciados desde julio de 2010 (correspondientes al mes 07 o al 3T), se puede dar la situación de que en un mismo período de liquidación hayan de reflejarse operaciones gravadas según los nuevos tipos impositivos (18%, 8%) junto con otras devengadas en períodos anteriores y a las que les sean de aplicación los tipos vigentes hasta el 30 de junio (7% o 16%).

En estos supuestos deberá consignarse en las casillas correspondientes la suma algebraica de las bases imponibles. De igual forma se procederá con las casillas correspondientes a las cuotas devengadas.

En cuanto a las casillas relativas a los tipos impositivos, se consignará el tipo resultante del cociente entre la cuota y la base imponible declarada, cualquiera que sea el resultado y si este cociente no da un número entero, se harán constar los dos primeros decimales del número resultante.

En las autoliquidaciones modelo 303 correspondientes al 1T o 2T de 2010 o a los meses 01 a 06 de 2010 no se pueden consignar bases ni cuotas a los nuevos tipos impositivos del 18% o 8%.

!!! info
    Los cambios expuestos en esta sección implican una modificación del contenido de los datos de referencia del módulo.

### **Novedades a partir del 1 de septiembre de 2012**

**MODIFICACIÓN TIPOS IMPOSITIVOS IVA Y RECARGO DE EQUIVALENCIA**

El Real Decreto Ley 20/2012 de medidas para garantizar la estabilidad presupuestaria y de fomento de la competitividad modificó los tipos general y reducido del Impuesto sobre el Valor Añadido con efectos a partir del 1 de septiembre, de forma que el tipo general pasa del 18% al 21% y el tipo reducido pasa del 8% al 10%, sin que se haya producido alteración alguna en relación con el tipo superreducido del 4%. Igualmente, los tipos de recargo de equivalencia pasan del 4% al 5,2% y del 1% al 1,4%.

**Cumplimentación de declaraciones**

En las autoliquidaciones de IVA, modelo 303, correspondientes a los períodos iniciados desde septiembre de 2012 (correspondientes al mes 09 o al 3T), se puede dar la situación de que en un mismo período de liquidación hayan de reflejarse operaciones gravadas según los nuevos tipos impositivos junto con otras devengadas en períodos anteriores y a las que les sean de aplicación los tipos vigentes hasta el 30 de agosto.

En estos supuestos, deberá consignarse en las casillas correspondientes la suma algebraica de las bases imponibles. De igual forma se procederá con las casillas correspondientes a las cuotas devengadas.

En cuanto a las casillas relativas a los tipos impositivos, se consignará el tipo resultante del cociente entre la cuota y la base imponible declarada, cualquiera que sea el resultado y si este cociente no da un número entero, se harán constar los dos primeros decimales del número resultante.

En las autoliquidaciones modelo 303 correspondientes al 1T o 2T de 2012 o a los meses 01 a 08 de 2012 no se pueden consignar bases ni cuotas a los nuevos tipos impositivos.

!!! info
    Los cambios expuestos en esta sección implican una modificación del contenido de los datos de referencia del módulo.
## **Instalación y aplicación del módulo**

### **Instalación**

!!! info
    Para la instalación del módulo **“AEAT - Modelo 303”** visite [Marketpace](https://marketplace.etendo.cloud/#/product-details?module=003B475055DD421B9483B5BE15AA48C5){target="_blank"}. 



### **Aplicación del módulo**

El módulo del Modelo 303 incluye unos datos de referencia que relacionan los tipos/rangos de impuestos para España con los parámetros del 303, por tanto:

-   Una vez instalado el módulo, los datos de referencia deben aplicarse a la Entidad legal con Contabilidad que corresponda, en la ruta de aplicación: Configuración General / Organización / Gestión del módulo de Empresa.

![](../../../../../assets/drive/EhxTBUvs6RBHj5qryz08lOpzAmCekUOmboNjz-E3OUuIK92wRMMzhOul3GuQ1hHMAutQbKIBKSi4NRQ0lPVDxWALgH4Fzsmc47MYlVJZZAOHS5giW468E6SMHsBjt2vqa8pn93TEZUBvHqiUId8oegI.png)
## **Contenido del módulo**

Al instalar y aplicar este nuevo módulo, el usuario podrá comprobar que:

-   Se han creado dos nuevos informes, el Modelo 303 mensual y el trimestral para la(s) organización(es) en la ruta de aplicación: Gestión Financiera || Contabilidad || Configuración || Declaración de Impuestos, tal y como se muestra en la siguiente imagen:  
     

![](../../../../../assets/drive/MAZZa2VuPorWEk1BAyrZHON1lh2tNqdkQna7BJhsI0E5g4R9ML0BrK9Xvpicq7ZG4xqlzAMn_0JEJBOskqgZvemex1fqHA8u9dvn6XT1190PDLTHuuzsunhwnbZ9PeooUmrqd6oiKCt-fI-J7ONuNsU.png)

-   La pestaña "Sección de Impuestos" contiene la definición de toda la información que se va a incluir en el Modelo 303 y, por tanto, en el fichero del 303 que se generará desde la ventana "Generador de Declaraciones de Impuestos". De todas estas secciones cabe destacar las secciones "IVA Devengado", "IVA Deducible" y "Diferencia".  
    Por ejemplo, la sección "IVA Devengado" incluye los parámetros siguientes en la pestaña "Parámetro de declaración":
    -   IVA Devengado - Régimen Ordinario
    -   IVA Devengado - Recargo de Equivalencia
    -   IVA Devengado - Adquisiciones Intracomunitarias

Estos parámetros se ligan a los tipos de impuestos en función de que las operaciones ligadas a ellos deban declararse, por ejemplo, como parte del IVA Devengado en Régimen Ordinario o bien como parte del IVA Devengado por Recargo de Equivalencia.

![](../../../../../assets/drive/zC4megIrlvdoyIVRkdw2ET8DrB6IV8rIcxQMRlZH4qJAHIO8TFlmif7eUuqb6NRoM6vvzm1mP5BLwsBOKFLQhDOLPbloFfYy6AVDe9p820rJKJem-Jy9UIlCzCafEWf15srFfJUOfrBR9fm5GSiUVsg.png)

-   Por tanto, los rangos de impuestos se han asociado al correspondiente parámetro del 303, con el fin de que las transacciones completadas y contabilizadas ligadas a dichos impuestos se tengan en cuenta en una u otra casilla/posición del fichero.  
     

![](../../../../../assets/drive/Vxz9LkuESteDKaeIzQmhO9gu10wFqL8QU579ZxLacwnA5WlhWtA-wkXgQvBfe7ZJCX6ksbd4XfoRk4U7sKTbnAQAWBbTgFBYJau2aJstONlCeoFElqPArRuDIf_dGIaD50o6yGJkxowqixFQAJ18Beo.png)

-   Por último, el Generador de Declaraciones de Impuestos permite la generación del fichero para la presentación de la declaración-liquidación del Modelo 303, desde la ruta de aplicación: Gestión Financiera || Contabilidad || Herramientas de análisis || Generador de Declaraciones de Impuestos, tal y como se muestra en la siguiente imagen:  
     

![](../../../../../assets/drive/612TP0yYxrPiuET6z7IkyF40fr5KGP6XC5cxCTbrK5eg6K1Im1xh_XYc3PzLVeMApJERGkm_9QHTuvuTl4slrb_t8TktOSrtNeisdNQcSpzodyq9c8wptIpFshledbtdup6U7-Kmw5FiEvBYOvfqsDI.png)
## **Configuration**

### **Tax / VAT Configuration**

The user must navigate to the application path: "General Setup / Enterprise Module Management", select the legal organization with accounting, and apply the modules in the specified order:

-   first the tax module if it is not previously applied and at level (\*)
-   and then the 303 module at Legal Organization with accounting level

### **303 Model Configuration**

The 303 model configuration is installed by default and can be checked in the application path: Financial Management//Accounting//Setup//Tax Report.

For both the monthly and quarterly 303 model, in the "Report Section" tab, 11 sections have been created, one for each group of information to be included when generating the Model 303 file:

![](../../../../../assets/drive/5e_DW0KWWXZ8E1fET-mk_Y2oq6YGls8fZL-zmAGlO8wzUqgFH0zKq0ir2QP6CK-SOWttp263yE5VKCjPLKuz5ubn63i8nzztWYzLioqT1Ar_RTn9zlNOCtG9T5CRG2wD0fzJpACMuAA7-vycnuQo390.png)

-   **File**
    -   This section contains an "Input" type parameter, so the user can enter the name of the 303 file when generating it.
-   **Declaration Type**
    -   This section contains 8 "Input" type parameters, one for each declaration type, so the user can mark the corresponding one when generating the file.
        -   Compensation
        -   Refund
        -   Payment
        -   Zero result
        -   Payment by bank direct debit
        -   Payment to tax current account
        -   Refund to tax current account
        -   Refund by transfer abroad
-   **No Activity**
    -   This section contains 1 "Input" type parameter so the user can mark a VAT settlement as "No Activity".
-   **Constants**
    -   This section includes all constant values required by the 303, such as:
        -   Model = 303
        -   Page = 01
        -   End of record identifier = </T30301>
-   **Identification**
    -   This section includes 4 "Output" parameters corresponding to identification data of the organization for which the file is generated and 1 "Input" parameter of type "checkbox" which is "Registered in the monthly refund register" which could be configured as a constant.
-   **Accrued VAT**
    -   This section includes 3 "Output" type parameters, one for each type of accrued VAT.
        -   "Accrued VAT - General Regime" VAT. This parameter is linked to tax ranges whose operations are taxed under the general regime, for example, deliveries of goods and services within the territory of application of the tax.
        -   "Accrued VAT - Equivalence Surcharge". This parameter is linked to tax ranges whose operations are taxed under the equivalence surcharge regime, for example, deliveries of goods to retailers within the territory of application of the tax.
        -   "Accrued VAT - Intra-Community Acquisitions”. This parameter is linked to tax ranges of intra-community acquisitions of goods

The complete list of tax ranges linked to each of these parameters can be consulted in the annex at the end of this document.

-   **Deductible VAT**
    -   This section includes a total of 12 parameters, 6 "Output" type parameters and 6 "Input" type parameters.  
        The "Output" type parameters correspond to the type of Deductible VAT from which information can be obtained from Etendo, for example "Deductible VAT for supported quotas in current domestic operations".  
        The "Input" type parameters correspond to types of Deductible VAT for which information cannot be obtained from Etendo, for example "Deductible VAT for compensation Special Regime A.G and P.(quota)

The complete list of tax ranges linked to each of these parameters can be consulted in the annex at the end of this document.

-   **Difference**
    -   This section includes 4 "Input" type parameters so the user can enter the following information when generating the file:
        -   % Attributable to the State Administration %.  
            Taxpayers who are taxed jointly in the State Administration and in the Provincial Councils of the Basque Country or the Foral Community of Navarra, must state the % of the volume of operations in common territory and therefore must be taxed in the State Administration; the rest of taxpayers will state 100%.  
            This data could be configured as a constant.
        -   Quotas to be compensated from previous periods. Taxpayers must state, when applicable, the positive quotas to be compensated from previous periods.
        -   Result of the annual regularization. In the last settlement of the year, the result of the annual regularization for investments will be stated
        -   To deduct (supplementary self-assessment), exclusively in the case of supplementary declaration, the result of the last declaration submitted for the same concept, corresponding to the same fiscal year and period, will be stated.
    -   And, in addition, 3 output parameters corresponding to non-taxable operations that give rise to the right to deduction:
        -   Intra-Community deliveries of goods. This parameter is linked to the tax ranges listed below:
            -   Intra-community deliveries (%N=>0%)
            -   Intra-community deliveries (%R=>0%)
            -   Intra-community deliveries (%SR=>0%)
            -   Intra-community deliveries Investment Goods (%N=>0%)
        -   Exports and similar operations. This parameter is linked to the tax ranges listed below:
            -   Deliveries to Canary Islands, Ceuta and Melilla (%N=>0%)
            -   Deliveries to Canary Islands, Ceuta and Melilla (%SR=>0%)
            -   Deliveries to Canary Islands, Ceuta and Melilla (%R=>0%)
            -   Exports (%N=>0%)
            -   Exports (%R=>0%)
            -   Exports (%SR=>0%)
            -   Exports Investment Goods (%N=>0%)
        -   Non-taxable operations or with reverse charge. This parameter is linked to the tax ranges listed below:
            -   Services to Canary Islands, Ceuta and Melilla (%N=>0%)
            -   Services to Canary Islands, Ceuta and Melilla (%SR=>0%)
            -   Services to Canary Islands, Ceuta and Melilla (%R=>0%)
            -   International services provided (%N=>0%)
            -   International services provided (%R=>0%)
            -   Services provided EU (%N=>0%)
            -   Services provided EU (%R=>0%)
-   **Refund**
    -   This section includes an "Input" type parameter which is the bank account to be used in case of refund declaration. This data could be configured as a constant.
-   **Payment**
    -   This section includes 5 "Input" type parameters related to "To be paid" declarations:
        -   the bank account to be used in case of payment declaration. This data could be configured as a constant.
        -   Not stated
        -   Cash
        -   Direct debit
        -   Domiciliation
-   **Supplementary**
    -   This section includes 2 input type parameters:
        -   Supplementary declaration, as a checkbox (yes/no)
        -   Receipt No., of the previous declaration being supplemented.

### **Document Types and Date**

When generating the valid text file to declare the VAT settlement Model 303, the following is taken into account:

-   The deductible (supported) VAT registered and posted in Purchase Invoices/Credit Memos, which the user can register in the application path: Procurement Management || Transactions || Purchase Invoice (Vendor), for the following document types:
    -   AP Invoice (Purchase invoice)
    -   Negative AP Invoice (Purchase credit)
    -   AP Credit Memo (Purchase credit)
-   The accrued VAT registered and posted in Sales Invoices/Credit Memos that the user can issue in the application path:    Sales Management || Transactions || Sales Invoice (Customer), for the following document types:
    -   AR Invoice (Sales invoice)
    -   Negative AR Invoice (Sales credit)
    -   AR Credit Memo (Sales credit)

The current version of the module does not take into account the Etendo document types without APRM listed below, which could be linked to a tax range, as they are considered not to be used for posting invoices that include VAT:

-   Bank statement
-   Cash journal
-   Settlements and manual entries

**The date that is taken into account** for including purchase/sales invoices in the 303 declaration/file is the **posting date**, which implies that:

-   Purchase/sales invoices with posting date from June 1, 2010 to June 30, 2010 will be included in the Monthly declaration corresponding to June 2010; in case of monthly declaration type, to be submitted before August 20, 2010.
-   Purchase/sales invoices with posting date from April 1, 2010 to June 30, 2010 will be included in the quarterly declaration corresponding to the second quarter of the year; in case of quarterly declaration type, to be submitted before August 20, 2010.
## **Caso de Usuario**

### **IVA Devengado - escenarios**

Tal y como se ha explicado con anterioridad, el principal objetivo del modelo 303 es que las empresas españolas puedan autoliquidar el IVA regularmente como diferencia entre el IVA Devengado en facturas emitidas de Venta y el IVA soportado deducible.

El fichero del 303 recoge desde la posición 72 a la 357, la base imponible, tipo y cuota del IVA devengado en las operaciones de venta bajo el régimen general, especificando por tipo de IVA (16%/18%, 7%/8% y 4%), régimen de recargo de equivalencia especificado por tipo de IVA (4%, 1% y 0,5%) así como la base y cuota del IVA devengado en las adquisiciones intracomunitarias.

#### **IVA devengado - régimen general**

Durante el periodo correspondiente (mes/trimestre), el usuario contabilizará en Etendo las facturas/abonos de venta emitidas tanto por la entrega de bienes como por la prestación de servicios dentro del territorio de aplicación del impuesto/IVA (Península y Baleares).

Se tendrán en cuenta:

1.  las facturas/abonos emitidas por la venta de productos o por la prestación de servicios, contabilizadas en la ruta de aplicación "Gestión de Ventas || Transacciones || Factura (Cliente)"
2.  las facturas/abonos financieros emitidos desde la ruta de aplicación: "Gestión de Ventas || Transacciones || Factura (Cliente)", marcados como "Factura Financiera" a nivel de línea de factura de venta, ligadas a un concepto contable previamente creado y asignado a una categoría de impuesto.
3.  las líneas de impuesto manualmente introducidas por el usuario en la ruta de aplicación: "Gestión de Ventas || Transacciones || Factura (Cliente) - Cabecera - Impuestos"

El fichero del 303 recogerá dichas transacciones dentro del mes/trimestre correspondiente, teniendo en cuenta la fecha de contabilización de dichas facturas, ya que el IVA se devenga cuando se realiza la puesta a disposición de los bienes o la prestación del servicio lo cual conlleva la facturación correspondiente, facturas que deben contabilizarse para tenerse en cuenta.

Los productos/servicios/conceptos contables tiene que estar ligados a una de las siguientes categorías de impuestos:

-   IVA Normal
-   IVA Reducido
-   IVA Super reducido
-   IVA Normal Servicios
-   IVA Reducido Servicios
-   IVA Super Reducido Servicios
-   IVA Normal B. Inmuebles
-   IVA Reducido B. Inmuebles
-   IVA Normal Bienes Inversión

Las líneas de facturas tienen que tener un rango de impuesto asociado a uno de los parámetros del 303 de la sección "IVA Devengado - Régimen General".

#### **IVA devengado - régimen de recargo de equivalencia**

Durante el periodo correspondiente (mes/trimestre), el usuario contabilizará en Etendo las facturas/abonos de venta emitidas por la entrega de bienes dentro del territorio de aplicación del impuesto/IVA (Península y Baleares) a terceros minoristas que se encuentren en régimen de recargo de equivalencia.

En estos casos, el emisor de la factura incluye, además del IVA, el tipo (%) de recargo correspondiente.

Se tendrán en cuenta:

1.  las facturas/abonos emitidas por la venta de productos, contabilizadas en la ruta de aplicación "Gestión de Ventas || Transacciones || Factura (Cliente)"
2.  las facturas/abonos financieros emitidos desde la ruta de aplicación: "Gestión de Ventas || Transacciones || Factura (Cliente)", marcados como "Factura Financiera" a nivel de línea de factura de venta, ligadas a un concepto contable previamente creado y asignado a una categoría de impuesto.
3.  las lineas de impuesto manualmente introducidas en el usuario en la ruta de aplicación: "Gestión de Ventas || Transacciones || Factura (Cliente) - Cabecera - Impuestos"

El fichero del 303 recogerá dichas transacciones dentro del mes/trimestre correspondiente, teniendo en cuenta la fecha de contabilización de dichas facturas, ya que el IVA se devenga cuando se realiza la puesta a disposición de los bienes, lo cual conlleva la facturación correspondiente, facturas que deben contabilizarse para tenerse en cuenta.

Los productos/servicios/conceptos contables tiene que estar ligados a una de las siguientes categorías de impuestos:

-   IVA Normal
-   IVA Reducido
-   IVA Super reducido

Las líneas de facturas tienen que tener un rango de impuesto asociado a uno de los parámetros del 303 de la sección "IVA Devengado - Recargo de Equivalencia".

#### **IVA devengado - Adquisiciones intracomunitarias**

Durante el periodo correspondiente (mes/trimestre), el usuario registrará y contabilizará en Etendo las facturas/abonos de compra recibidos de sus proveedores/acreedores (no residentes en territorio de aplicación del impuesto, pero residentes en la Unión Europea que son operadores intracomunitarios), por la adquisición de bienes dentro del territorio de aplicación del impuesto/IVA (Península y Baleares).

Se tendrán en cuenta:

1.  las facturas/abonos registradas en el sistema por la compra de productos, contabilizadas en la ruta de aplicación "Gestión de Compras || Transacciones || Factura (Proveedor)"
2.  las facturas/abonos financieros emitidos desde la ruta de aplicación: ""Gestión de Compras || Transacciones || Factura (Proveedor)", marcados como "Factura Financiera" a nivel de línea de factura de compra, ligadas a un concepto contable previamente creado y asignado a una categoría de impuesto.
3.  las líneas de impuesto manualmente introducidas en el usuario en la ruta de aplicación: "Gestión de Compras || Transacciones || Factura (Proveedor) - Cabecera - Impuestos"

Los productos/conceptos contables tienen que estar relacionados con una de las siguientes categorías de impuesto:

-   IVA Normal
-   IVA Reducido
-   IVA Super Reducido

Las líneas de facturas tienen que tener un rango de impuesto asociado a uno de los parámetros del 303 de la sección "IVA Devengado - Adquisiciones Intracomunitarias".

Es importante recalcar que el caso de las adquisiciones intracomunitarias se considerarán realizadas en el territorio de aplicación del impuesto cuando:

-   se encuentre en este territorio el lugar de la llegada de la expedición o transporte con destino al adquirente.
-   y cuando el adquirente haya comunicado al vendedor el número de identificación a efectos del impuesto sobre el Valor Añadido atribuido por la Administración española.

Este régimen se caracteriza por el gravamen en destino de las entregas intracomunitarias realizadas entre empresas. Esto significa que se aplique una exención en el país de origen y que se considere realizado el hecho imponible en el de destino, con motivo de la adquisición. A esto se le denomina adquisición intracomunitaria de bienes, y se altera de esta manera la regla general del impuesto, al ser el sujeto pasivo del impuesto el que compra y no el que vende.

El sujeto pasivo/adquiriente es, por tanto, quien debe liquidar el IVA y, por tanto, deberá autorrepercutirse el IVA y a su vez deducírselo, si aplica. Es por ello que este tipo de operaciones, como las operaciones de Inversión de Sujeto Pasivo aparecen tanto en la sección de IVA devengado como en la sección de IVA deducible.
### **VAT Deductible - scenarios**

As previously explained, the main objective of Form 303 is for Spanish companies to regularly self-assess VAT as the difference between Output VAT on issued Sales invoices and deductible Input VAT.

The 303 file includes, from position 357 to 612, the taxable base and tax amount, in most cases, of Input VAT that is deductible on domestic transactions, imports and intra-Community acquisitions of current goods (goods and services) and capital goods.

#### **VAT deductible - input VAT on domestic current transactions**

During the corresponding period (month/quarter), the user will record and post in Etendo the purchase invoices/credit notes received from their suppliers/creditors both for the purchase of goods and for services provided to the Company within the territory of application of the tax/VAT (Mainland Spain and Balearic Islands), as well as financial invoices.

Products/services/accounting concepts must be related to one of the following tax categories:

-   Standard VAT
-   Reduced VAT
-   Super Reduced VAT
-   Standard VAT Services
-   Reduced VAT Services
-   Super Reduced VAT Services
-   Standard VAT Real Estate
-   Reduced VAT Real Estate

Invoice lines must have a tax rate associated with one of the 303 parameters in the section "VAT Deductible - For input VAT on domestic current transactions".

#### **VAT deductible - domestic capital goods transactions**

During the corresponding period (month/quarter), the user will record and post in Etendo the purchase invoices/credit notes received from their suppliers/creditors both for the purchase of capital goods (capital goods are considered those with a value greater than €3,000.00) within the territory of application of the tax/VAT (Mainland Spain and Balearic Islands), as well as financial invoices.

Products/services/accounting concepts must be related to one of the following tax categories:

-   Standard VAT Capital Goods

Invoice lines must have a tax rate associated with one of the 303 parameters in the section "VAT Deductible - Domestic capital goods transactions".

#### **VAT deductible - for VAT accrued on imports of goods**

During the corresponding period (month/quarter), the user will record and post in Etendo the purchase invoices/credit notes received from their suppliers/creditors (non-residents in the territory of application of the tax), for the import of goods within the territory of application of the tax/VAT (Mainland Spain and Balearic Islands), as well as financial invoices.

Products/accounting concepts must be related to one of the following tax categories:

-   Standard VAT
-   Reduced VAT
-   Super Reduced VAT

Invoice lines must have a tax rate associated with one of the 303 parameters in the section "VAT Deductible - For VAT accrued on imports of current goods".

#### **VAT deductible - imports of capital goods**

During the corresponding period (month/quarter), the user will record and post in Etendo the purchase invoices/credit notes received from their suppliers/creditors (non-residents in the territory of application of the tax), for the import of capital goods within the territory of application of the tax/VAT (Mainland Spain and Balearic Islands), as well as financial invoices.

Products/accounting concepts must be related to one of the following tax categories:

-   Standard VAT Capital Goods

Invoice lines must have a tax rate associated with one of the 303 parameters in the section "VAT Deductible - Imports of capital goods".

#### **VAT deductible - intra-Community acquisitions of goods**

During the corresponding period (month/quarter), the user will record and post in Etendo the purchase invoices/credit notes received from their suppliers/creditors (non-residents in the territory of application of the tax, but residents in the European Union who are intra-Community operators), for the acquisition of goods within the territory of application of the tax/VAT (Mainland Spain and Balearic Islands), as well as financial invoices.

Products/accounting concepts must be related to one of the following tax categories:

-   Standard VAT
-   Reduced VAT
-   Super Reduced VAT

Invoice lines must have a tax rate associated with one of the 303 parameters in the section "VAT Deductible - intra-Community acquisitions of current goods".

As already mentioned, it is important to emphasize that intra-Community acquisitions will be considered carried out in the territory of application of the tax when:

-   the place of arrival of the dispatch or transport to the acquirer is located in this territory.
-   and when the acquirer has communicated to the seller the identification number for Value Added Tax purposes assigned by the Spanish Administration.

This regime is characterized by taxation at destination of intra-Community supplies made between companies. This means that an exemption is applied in the country of origin and that the taxable event is considered to occur in the country of destination, due to the acquisition. This is called an intra-Community acquisition of goods, and the general rule of the tax is altered in this way, since the taxable person is the buyer and not the seller.

The taxable person/acquirer is therefore the one who must settle the VAT and, therefore, must self-charge the VAT and in turn deduct it, if applicable. That is why this type of transactions, like Reverse Charge transactions, appear both in the Output VAT section and in the Input VAT section.

#### **VAT deductible - intra-Community acquisitions of capital goods**

During the corresponding period (month/quarter), the user will record and post in Etendo the purchase invoices/credit notes received from their suppliers/creditors (non-residents in the territory of application of the tax, but residents in the European Union who are intra-Community operators), for the acquisition of capital goods within the territory of application of the tax/VAT (Mainland Spain and Balearic Islands), as well as financial invoices.

Products/accounting concepts must be related to one of the following tax categories:

-   Standard VAT Capital Goods

Invoice lines must have a tax rate associated with one of the 303 parameters in the section "VAT Deductible - intra-Community acquisitions of capital goods".
### **Diferencia - escenarios**

El fichero del 303 recoge, desde la posición 629 a la 804, los datos relativos a la diferencia entre el IVA devengado y el IVA deducible, junto con otro tipo de información adicional necesaria para el cálculo del resultado final de la casilla \[48\].

Desde Etendo, el usuario puede obtener la diferencia entre el IVA devengado y el IVA deducible, así como parte de la información adicional necesaria para el cálculo del resultado final; el resto debe introducirse por parte del usuario como "parámetros de entrada" a la hora de generar el fichero.

La información que el usuario puede obtener desde el sistema son las bases imponibles para un periodo determinado (mes/trimestre) respecto de las operaciones que a continuación se detallan:

-   **Entregas intracomunitarias** - en este caso, el sistema tiene en cuenta las facturas/abonos/facturas financieras de venta a clientes no residentes en territorio de aplicación del impuesto, pero residentes en la Unión Europea, emitidos y contabilizados, por la entrega exenta de IVA de bienes fuera del territorio de aplicación del impuesto/IVA (Península y Baleares).  
    Las líneas de facturas tienen que tener un rango de impuesto asociado a uno de los parámetros del 303 de la sección "Diferencia - Entregas intracomunitarias".
-   **Exportaciones y operaciones asimiladas** - lo mismo aplica a las exportaciones; en este caso, el sistema tiene en cuenta las facturas/abonos/facturas financieras de venta emitidas y contabilizadas a clientes extranjeros, por la entrega exenta de IVA de bienes fuera del territorio de aplicación del impuesto/IVA (Península y Baleares).  
    Las líneas de facturas tienen que tener un rango de impuesto asociado a uno de los parámetros del 303 de la sección "Diferencia - Exportaciones y operaciones asimiladas".
-   **Operaciones no sujetas o con inversión del sujeto pasivo** que origina derecho a deducción - este caso aplica a facturas/abonos/facturas financieras de venta emitidos y contabilizados por la prestación de servicios de la empresa fuera del territorio de aplicación del impuesto; servicios exentos, pero que originan derecho a deducción.  
    Las líneas de facturas tienen que tener un rango de impuesto asociado a uno de los parámetros del 303 de la sección "Diferencia - Operaciones no sujetas o con inversión del sujeto pasivo".

El resto de datos deben ser introducidos manualmente por el usuario a la hora de generar el modelo 303 desde la ventana "Generador de declaraciones de impuestos", tal y como se muestra en la pantalla siguiente:

![](../../../../../assets/drive/1aOcwK47kn7zNbQB4UYWQgR7MrNA0sPoc7gech6cMPSdUr6ozKUpHPmXThitLJ-cH-J1CGwfirc3uiEWM5eWv4b_uTTVtgibwWIKX_45wOoSiXPSsu6KqC7-Uqbpf806myQtrgX_zTtxob5SkKC21jY.png)
### **Devoluciones - escenarios**

#### **Devoluciones - Devolución/Devolución cuenta corriente tributaria**

Para este tipo de declaraciones, y siempre que el checkbox "Inscrito en el Registro de devolución mensual" esté marcado, los siguientes campos son obligatorios:

- IBAN
- Marca SEPA

#### **Devoluciones - Devolución por transferencia al extranjero**

Para este tipo de declaraciones, y siempre que el checkbox "Inscrito en el Registro de devolución mensual" esté marcado, los siguientes campos son obligatorios: 

- Domiciliación/Devolución - IBAN (cuenta bancaria)
- Devolución - Banco/Nombre del banco
- Devolución - Dirección del banco/Dirección del banco
- Devolución - Ciudad/Ciudad
- Devolución - Código país/Código de país
- Devolución - Marca SEPA
### Configuración previa antes de generar el informe

#### **Actividades del I.A.E.**

En el Modelo 303, para generar el informe mensual - último periodo, a partir de 2022, se deben declarar las principales actividades del I.A.E. (Impuesto de Actividades Económicas) en las que la empresa trabaja habitualmente.

El módulo Epígrafes I.A.E., instalado como dependencia del 303, añade una nueva solapa a la ventana de Organización en la que puede indicar todas las actividades en las que su empresa ha estado trabajando. El modelo 303 debe incluir como mínimo una actividad principal, que debe estar marcada en la aplicación como por defecto, y como máximo 5 actividades. En caso de incluir más de 5 actividades, se incluirán en el informe las 5 primeras según el número de línea.

![](../../../../../assets/drive/xWyc9Dzkqn1i48qdwqYjwylIUK39OllwglsbxorOf_u8TNJXZr4J4fAxALMyMvi6eCiATDGan8Z0C2No0SA-NVcsiXBPGo1qvj6VLamQwVYMTUgnW5oMaiouFU-eY65XVXK_YZPPzg6z6Rns5Bl-9IpSiIjKz-NCaNr6oG1tsoCdlsSPPfFyGqmH_pPBnQ.png)

En el módulo de Epígrafes I.A.E. se incluye el conjunto correspondiente a la clave 1. Si desea incluir un epígrafe que pertenezca a cualquier otra clave, tan sólo debe crear un nuevo registro en la ventana Epígrafes I.A.E. e incluirlo en un registro de la solapa de Actividades del I.A.E. de la ventana de Organización.

Para el modelo 303, los campos 'Epígrafe I.A.E.' y 'Código' son obligatorios
### **Generación del modelo 303**

Tal y como ya se ha explicado, el modelo 303 de autoliquidación de IVA se genera como un fichero de texto válido conforme a los requerimientos de la AEAT desde la ruta de aplicación: Gestión Financiera || Contabilidad || Herramientas de análisis || Generador de Declaraciones de Impuestos || Generador de Declaraciones de Impuestos

Una vez que el usuario ha introducido los datos genéricos, tales como "organización", "ejercicio", "periodo":

![](../../../../../assets/drive/dNa0Xp7cP15EVu-NquNiO27FfKbbDTYXfLQ5Wm4I8LxL3ah4xw4_v3_PB6zShaBBNuFB1dwW9O15LSxabPohtRNc3xjWGMrgxQzdvqRagqs2C0A6Pwq3DJ5-FVhdBE-RMxe09uIGBEXM5YE7NQ3KRWg.png)

se pueden introducir los parámetros de entrada, o datos que no pueden obtenerse de Etendo, a través del botón de proceso "Parámetros de entrada".

!!! info
    Es importante recalcar que algunos de los parámetros de entrada que se introducen a continuación, como por ejemplo "Inscrito en el Registro de devolución mensual", pueden configurarse como parámetros "Constantes" con el fin de no tener que introducirlos cada vez que se genera el fichero del 303.

La forma de hacerlo es:

-   buscar el parámetro de entrada del 303 en la ventana "Declaración de Impuestos", pestaña "Sección de declaración". Por ejemplo, el parámetro de entrada "Inscrito en el Registro de devolución mensual" que se encuentra en la Sección de declaración "Identificación".
-   cambiar el parámetro de tipo "Entrada" a "Constante". En el campo "Valor constante" añadir "1", en caso de inscripción en el registro de devolución mensual, o bien añadir "2", en caso de que el sujeto pasivo no esté inscrito en el registro de devolución mensual.

Es importante recalcar que si se produce una actualización de los datos de referencia de este módulo, los cambios de parámetros de entrada a constante se sobreescribirán, por lo que será necesario volver a configurarlos.

Las secciones de la nueva ventana que se muestra se corresponden con las secciones definidas para el Modelo 303:

Secciones: "**Fichero**", "**Tipo de declaración**" y "**Sin actividad**":

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/modelo-303/seccion-fichero-tipo-dec-sin-act.png)

Secciones: "**IVA deducible**", **"Liquidación-resultado"** y **"Banco"**:

![](../../../../../assets/drive/TmR4r-g0sbW3iYqVXO4M4IvKdyIKxp9t7FxwjL1i2srAJVnSK7obME0S7xZnd6ZBOMGwzsfbYZJ3BTDwjwzwSbpLmbioI49r1hX4YpyFrXeUYauG-D8tNEiGXqROzpI6RWJlewDrm-lQspoLPFfMR9M.png)

Secciones: **"Complementaria"**, **"Tributación por razón de territorio"** y **"Información adicional"**

![](../../../../../assets/drive/SZHf8tnfL96mKnbhdEg4Oev3PSB8moMCC7k5MqXfkkR5aY3E9FR_QjNwZ5xOFytKPdafxQv5QLaccO557RenGMZlkPMDoskLe9TXqfiVJ4s1Fi1wPM32-UMQMA7MFoExjgiZlbR9y1EhG_2uz3_Fd9E.png)

Una vez que el fichero se ha generado, tendrá este aspecto:

![Fichero.png](../../../../../assets/drive/7TUbkV18JCkTIs6aoBVNgXYoCr6vvEfFk1_kWdHjMi8-VjOMmEIsWBEWeRgj8AJ8VsbXNifrzXOGd6u19snnZEyhWLrsUty88vVrYwvnAU3FRzuTZRvteHfLFXle7Ajk4deKF124p9-bySu6AweMwpk.png)
### **Pre-validation of Form 303**

The file generated in Etendo can be pre-validated at the following AEAT link:

[_Form 303 for filing (pre-declaration), FY 2014 onwards (General Regime)_](https://www2.agenciatributaria.gob.es/es13/h/ie43030b.html){target="_blank"}.

Once on that link, the user can import the file using the option "Optional: Import data from file". The data obtained from the file will be displayed for validation.

After validating the data, Form 303 can be filed at the following link, for which a valid certificate is required: [_Filing, FY 2014 onwards (General Regime)_](https://www.agenciatributaria.gob.es/AEAT.sede/procedimientoini/G414.shtml){target="_blank"}, for which an electronic identification certificate or electronic DNI is required.
## **Anexo**

Este anexo incluye el listado completo de los rangos de impuestos asociados a los parámetros del modelo 303 de las secciones "IVA Devengado" e "IVA Deducible" sólo para los tipos de IVA vigentes en la actualidad (2012):

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

---

Este trabajo es una obra derivada de [Openbravo Localización Española](https://wiki.openbravo.com/wiki/Openbravo_Localizaci%C3%B3n_Espa%C3%B1a){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.