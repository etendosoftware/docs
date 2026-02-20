---
title: Modelo 347
tags:
    - Modelo 347
    - Localización Española
---

:octicons-package-16: Javapackage: `org.openbravo.module.aeat347apr.es`
:octicons-package-16: Javapackage: `org.openbravo.module.aeat347apr.es.es_es`
## **Introducción**

Esta sección describe la generación de la declaración: “**Modelo AEAT 347 - Declaración anual de operaciones con terceros**” como un fichero de texto ("*.txt") válido conforme a los requerimientos de la Hacienda Pública española, por lo que se publicará una nueva versión de este módulo cuando dichos requerimientos cambien.

El fichero del 347 se genera desde el "**Generador de declaraciones de impuestos**" que se encuentra en la ruta de aplicación: "Gestión financiera / Contabilidad / Herramientas de análisis / Generador de declaraciones de impuestos".

El Modelo/Declaración 347 forma parte del módulo de Localización Española de Etendo.
## **Descripción del módulo**

### **Obligados a presentar la declaración**

De acuerdo con la normativa de la Hacienda Pública española, están obligados a presentar el modelo 347:

Todas aquellas personas físicas o jurídicas, de naturaleza pública o privada que desarrollen actividades empresariales o profesionales, siempre y cuando hayan realizado operaciones que, en su conjunto, respecto de otra persona o entidad, cualquiera que sea su naturaleza o carácter, hayan superado la cifra de 3.005,06€ durante el año natural al que se refiere la declaración. Para el cálculo de la cifra de 3.005,06 € se computan de forma separada las entregas de bienes y servicios y las adquisiciones de los mismos.

De acuerdo con la normativa, no están obligados a presentar el modelo 347:

-   Quienes realicen en España actividades empresariales o profesionales sin tener en territorio español la sede de su actividad, un establecimiento permanente o su domicilio fiscal.
-   Las personas físicas y entidades en atribución de rentas en el Impuesto sobre la Renta de las Personas Físicas, por las actividades que tributen en dicho impuesto por el método de estimación objetiva y, simultáneamente, en el Impuesto sobre el Valor Añadido por los regímenes especiales simplificado o de la agricultura, ganadería y pesca o del recargo de equivalencia, salvo por las operaciones por las que emitan factura.
-   Los obligados tributarios que no hayan realizado operaciones que en su conjunto superen la cifra de 3.005,06€
-   Los obligados tributarios que hayan realizado exclusivamente operaciones no declarables.
-   Los obligados tributarios que deban informar sobre las operaciones incluidas en los libros registro de IVA (modelo 340) salvo que realicen operaciones que expresamente deban incluirse en el modelo 347.

### **Operaciones declarables**

Las operaciones declarables y que, por tanto, se incluyen en el modelo 347 son las que se detallan a continuación:

1.  Tanto las entregas de bienes y prestaciones de servicios realizadas por el declarante como sus adquisiciones de bienes y servicios incluyéndose, en ambos casos, tanto las operaciones típicas y habituales como las ocasionales e incluso las operaciones inmobiliarias. Debe tenerse en cuenta que dichas operaciones se incluirán estén o no sujetas al IVA y, en el primer caso, también las exentas de dicho impuesto.

Además, se incluyen de forma específica y aparte:

-   los arrendamientos de locales de negocio
-   los importes superiores a 6.000,00€ percibidos en metálico de cada una de las personas o entidades relacionadas en la declaración
-   las cantidades que se perciban en contraprestación por transmisiones de bienes inmuebles que constituyan entregas sujetas a IVA
-   y las prestaciones de servicios de/a no residentes (incluyendo Canarias, Baleares, Ceuta y Melilla) que no estén sujetos a retención.

Los importes que se incluyen en el modelo 347 son los “importes totales” de la contraprestación en euros (€). En los supuestos de operaciones sujetas y no exentas de IVA se añaden, por tanto, a la base imponible, las cuotas del impuesto y recargos de equivalencia repercutidos. Los importes además se declaran netos de las devoluciones o descuentos y bonificaciones concedidos.

Las operaciones que se incluyen en el modelo 347 son las realizadas por el declarante en el año natural a que se refiere la declaración y la fecha que se tiene en cuenta para su inclusión en el 347 es la fecha contable de la factura.

Las operaciones que en ningún caso se incluirán en el 347 por ser no declarables son las que se detallan a continuación:

-   aquellas que hayan supuesto entregas de bienes o prestaciones de servicios por las que los obligados tributarios no debieron expedir y entregar factura o documento equivalente
-   aquellas operaciones realizadas al margen de la actividad empresarial o profesional
-   aquellas efectuadas a título gratuito
-   los arrendamientos de bienes exentos de IVA
-   las importaciones y exportaciones de mercancías, así como las entregas y adquisiciones de bienes que supongan envíos entre el territorio peninsular español o las islas Baleares y las islas Canarias, Ceuta y Melilla.
-   Todas aquellas que se incluyan en otros modelos de la Administración Tributaria como por ejemplo aquellas cuya contraprestación haya sido objeto de retención o ingreso a cuenta; las operaciones intracomunitarias de bienes y servicios que se declaran en el modelo 349 o las operaciones incluidas en los libros registro que deben incluirse en el modelo 340.

El nuevo módulo de generación del Modelo 347 no incluye las operaciones que se describen a continuación y que deberían incluirse en el modelo 347, por ser relativas a Administraciones Públicas, entidades aseguradoras y colegios profesionales:

-   las subvenciones, auxilios o ayudas satisfechas por las entidades integradas en las distintas Administraciones Públicas
-   las operaciones de seguros realizadas por las entidades aseguradoras
-   las prestaciones de servicios realizadas por las agencias de viajes
-   los cobros por cuenta de terceros de honorarios profesionales o de derechos derivados de la propiedad intelectual, industrial, de autor u otros por cuenta de sus socios, asociados o colegiados efectuados por sociedades, asociaciones, colegios profesionales u otras entidades que, entre sus funciones, realicen las del cobro
-   las operaciones sujetas al impuesto sobre la producción, los servicios y la importación en las ciudades de Ceuta y Melilla.

Además, no se incluye en el módulo de funcionalidad el supuesto de Declaración Complementaria para aquellos casos en que deban incluirse sólo las operaciones que, debiendo haber sido declaradas en otra declaración del mismo ejercicio presentada con anterioridad, no se incluyeron. Estas operaciones deberán ser incluidas por el usuario manualmente, a través de la página de la AEAT tal y como se explica en la sección de este documento "Declaración Complementaria".
## **Instalación del módulo**

Para la instalación del módulo **“Modelo AEAT 347 - Declaración de operaciones con terceros”** (Spain AEAT Modelo 347 for APR), el usuario debe seguir los pasos que se describen a continuación en función de la situación de partida:

-   Instalación de la última versión disponible de Etendo 
-   o la instalación del módulo de Localización Española.

!!! info
    Para la instalación del módulo de Localización Española, visite [_Marketplace_](https://marketplace.etendo.cloud/#/product-details?module=003B475055DD421B9483B5BE15AA48C5){target="_blank"}. 

Es importante recalcar que el módulo del Modelo AEAT 347 incluye el correspondiente conjunto de datos (dataset) que relaciona los rangos de impuestos de España con los parámetros del 347. Este conjunto de datos se debe aplicar a la Organización para la cual se necesita obtener el 347, tal y como se explica en el siguiente apartado.

### **Aplicación del Módulo**

Una vez instalado el módulo del 347 por cualquiera de los procedimientos anteriores, el usuario debe aplicar el conjunto de datos o dataset del módulo 347 a la organización legal con contabilidad que corresponda, desde la ventana "Gestión del Módulo de Empresa".

El módulo de impuestos para España es válido para todos los modelos de declaración de impuestos, en este caso el modelo 347, y debe estar instalado previamente.

!!! info
    Es fundamental recalcar que el usuario debe tener el módulo de impuestos para España instalado y aplicado a la organización (\*) o bien a la organización legal para la que se quiera obtener el 347.
## **Module Configuration**

### **347 Model Configuration**

Once the 347 Model dataset has been applied, you can check in the application path: Financial Management / Accounting / Setup / Tax Report that the 347 model for the corresponding period is created as an annual tax report.

![](../../../../../assets/drive/2u88N7Cgi-SP2bdf8o4omVD0u1Up3nn33id19ei0bDPUxydw-cF9LLBl-YAE_5CNlQR7_9-rgia_VhhUwgW6QTKQgrHCC1qu4jTyfflLyVH9uDdav7NQWS47_h1ntt7M7800npJGiAbWAqRnzHfhIQ.png)

In the “Tax Report Sections” tab, 3 groups have been created for the 347 model:

-   347 File Name. This section contains:
    -   an “input” parameter that will be displayed when generating the 347 so that the user manually enters the “347 txt file name” to be generated.
-   Identification and Totals. This section contains:
    -   2 “constant” parameters that the system will take into account when including operations, since it will only include those that exceed the limit amounts detailed below:  
          
        -   Limit amount for including operations with third parties = 3.005,06€
        -   Limit amount for cash collections received = 6.000,00€
    -   and 5 “input” parameters that will be displayed when generating the 347 so that the user manually enters them, which are:  
          
        -   Name and surname of the contact person: This input parameter could be changed to a constant type and, therefore, the value of that constant should be specified, which in this case would be the name of the contact person, for scenarios in which the same person submits the report. If so, this parameter would not need to be filled in each time the report is generated.
        -   Phone number of the contact person. This input parameter could be changed to a constant type and, therefore, the value of that constant should be specified, which in this case would be the phone number of the contact person, for scenarios in which the same person submits the report. If so, this parameter would not need to be filled in each time the report is generated.
        -   Substitute report (yes/no)
        -   No. of the report to be substituted
        -   Tax ID of the legal representative
-   **Operations with third parties**. This section contains:
    -   5 “output” parameters linked to the corresponding tax key, which, associated with the tax rates of the tax module for Spain, will include purchase/sale operations in the 347:
        -   Goods acquisitions - Key A
        -   Goods deliveries - Key B
        -   Provision of services - Key A
        -   Services provided - Key B
        -   Real estate transfers - Key B

In the path Financial Management / Accounting / Setup / AEAT347 Document Type, the user can specify the document types that the 347 must take into account. The operation of this parameterization screen is that if no document type is specified, Etendo will take into account all invoice-type document types that can be posted.

If the user enters any document type, only those will be taken into account.

![](../../../../../assets/drive/OkdImkuzASfTUs2ne-BnPzKROain8Y-Z59B-4m3DX8xAjhoK-wvSJEmH6P1OBX-eIC9AGQXKGViX6K-0zMZHeGnfVD3v-eKgTvojkYKe-vEXykDdGYstwWmsUW4vRRjUAreAq7ndNhtf8zVm3rwbug.png)

### **Tax Configuration**

This 347 model generation module is based on the tax module for Spain, since it uses the tax ranges included in that module. In addition, it includes a dataset that links the tax ranges of the tax module for Spain with the 347 parameters listed below, depending on the type of operation:

-   **Goods acquisitions – Acquisition “A”**
-   **Goods deliveries – Deliveries “B”**
-   **Provision of services– Acquisition “A”**
-   **Services provided– Deliveries “B”**
-   **Real estate transfers – Deliveries “B”**

The user can check in the application path: Financial Management / Accounting / Setup / Tax Rate - Tax Parameter tab that the “tax rates/taxes” that must be included in the 347 have been associated with the corresponding 347 tax parameter:

-   Purchase/acquisition VAT types (domestic), including acquisitions of real estate and investment goods, have been associated with the “Goods acquisitions” parameter, which corresponds to the 347 operation key => “A”
-   Sales/delivery VAT types (domestic) (including Equivalence Surcharge) have been associated with the “Goods deliveries” parameter, which corresponds to the 347 operation key => “B”
-   VAT types for “reverse charge NON-EU” (in cases of NON-intra-community provision of services) have been associated with the “Provision of services” parameter, which corresponds to the 347 operation key => “A”
-   VAT types for deliveries of real estate (domestic) have been associated with the “Real estate transfers” parameter, which corresponds to the 347 operation key => “B”; since it must be reported twice as a sales operation and the amount of the real estate transfer must be stated separately.
-   Specific VAT types have been created for provision of services (domestic and international), associated with specific tax categories for services, which have been associated with the 347 parameters “Provision of services – operation key A” or “Services provided – operation key B” depending on whether the reporting company receives or provides the services.
-   VAT types for services from/to Canary Islands, Balearic Islands, Ceuta and Melilla have been associated either with the “Provision of services” parameter operation key of the 347 => “B” or with the “Service operations (Acquisition)” parameter operation key of the 347 => “A”, respectively, since only service operations are included in the 347 and not goods operations involving shipments of goods between the Spanish mainland territory or the Balearic Islands and the Canary Islands, Ceuta and Melilla
-   Finally, specific VAT types have been created for rentals (with and without withholdings associated with 2 BP tax category types, respectively). VAT types for rentals without withholdings have been associated with the 347 parameters “Provision of services – operation key A” or “Services provided – operation key B” depending on whether the company is the tenant or landlord of the rented premises or office and subject to VAT.

### **Business Premises Configuration**

In the 347 model, leases of business premises must be included, which is why in the application path: Master Data Management / Product a new parameter “Rented premises” has been created.

If so, the user must enter into the system the information detailed below, as it is necessary to include it in the 347 model:

-   **Situation**. The user must choose one of the following options:
    -   Premises abroad
    -   Valid cadastral reference in the Basque Country or Navarre
    -   Valid cadastral reference except in the Basque Country or Navarre
    -   Without cadastral reference
-   **Cadastral reference.** Free text field.
-   **Street type.** The user must choose the street type from a standardized list according to the Spanish INE.
-   **Street name**. Free text field.
-   **Numbering type**. The user must choose the numbering type from a standardized list.
-   **Number**. Free text field.
-   **Number qualifier**. Free text field.
-   **Block**. Free text field.
-   **Portal**. Free text field.
-   **Staircase**. Free text field.
-   **Floor or apartment**. Free text field.
-   **Door**. Free text field.
-   **Complement**. Additional address data, if any.
-   **Locality or Town**. Free text field.
-   **Municipality**.
-   **Municipality code**. The user must choose the municipality code from a standardized list according to the Spanish INE.
-   **Province code.** The user must choose the province code from a list of two-digit numeric province codes.
-   **Postal code**. The user must choose the postal code.

In the case of "Premises abroad" the data to be included are:

-   **Street type.**
-   **Street name**.

The 347 reflects this type of operations separately as explained in the corresponding use case.
## **Generación del modelo 347**

El modelo 347 se genera desde la ruta de aplicación: Gestión Financiera / Contabilidad / Herramientas de análisis / Generador de declaraciones de impuestos.

![](../../../../../assets/drive/I8vKXFszVIXPVZhyPNt7q1dl52OyNIGw-JWKniQBLnKUq21l25J9MbdniTdtPtnNIB1Q3aKoP3thNPaSWwmlwa3xdcBYC6jQWnQUxks9w9nH2cMZEKWtJMgTrWme0TlsVbG5dqhEh14CHBKAqglBiA.png)

El usuario deberá introducir los siguientes datos para generar el modelo 347:

-   **Organización** para la cual quiere generar el Modelo 347. El sistema mostrará el calendario asociado a la organización en un campo no editable.
-   **Esquema contable**
-   **Declaración**. El usuario debería seleccionar aquí el modelo 347 del periodo impositivo que corresponda.
-   **Ejercicio**. El usuario puede introducir el año natural para el cual quiere generar el modelo 347
-   **Periodo**. El valor “Anual” debería mostrarse por defecto.

Una vez introducidos los datos anteriores, el usuario puede introducir los parámetros de entrada del 347 en el botón de proceso “Parámetros de entrada”

![](../../../../../assets/drive/BTVvmrL7eUYl5NhX1-PKOO_Aa_50C1NZd8bWXZAiD4oQsYc32KxEQKKhjq1bzpwL084nWtTneQN0cn2Fd9zQVoUqkGtIrzR8LnkUklnypDnn9CSFjpknNIHs5c6lV8fV4nsqaxBlFplBnEuRQ2_8pA.png)

y una vez introducidos los parámetros de entrada, como por ejemplo el "Nombre del Fichero" o la "Persona/Teléfono de contacto", el usuario puede generar el fichero del Modelo 347 a través del botón de proceso “Generar fichero”.

Es entonces cuando se genera el fichero de texto ("\*.txt") del Modelo 347 conforme a los requerimientos de la AEAT, que puede presentarse directamente en la web de la AEAT.

En el módulo [](http://centralrepository.openbravo.com/openbravo/org.openbravo.forge.ui/sso/ForgeModuleDetail/Spain-AEAT-Modelo-347-For-APR)"Spain AEAT Modelo 347 for APR", se genera un fichero zip que contiene tres ficheros:

-   el fichero "txt" ya mencionado de igual formato y, por tanto, igualmente válido para la presentación del Modelo 347 a partir de 2014
-   un fichero denominado "Facturas.csv"
-   y un fichero denominado "Metalico.csv"

*Los dos ficheros adicionales de formato \*.csv sólo se generan si la declaración del 347 tiene contenido*.

El fichero "Facturas.csv":

-   contiene un listado con información del tipo "Tercero", "Fecha Contable", "Impuesto", "Base Imponible", "Cuota", "Total" etc, de todas las facturas susceptibles de incluirse en el fichero txt.

El fichero "Metalico.csv":

-   contiene un listado con información del tipo "Cuenta Financiera", "Identificación de Transacción", "Tercero", "Fecha Contable", "Importe" y "Ejercicio (de devengo)" de todos los cobros en efectivo susceptibles de incluirse en el fichero txt.
## **Casos de usuario**

### **Operaciones de compra y venta**

Etendo permite la introducción y contabilización de facturas de compra y de venta, a través de la ventana correspondiente.

El modelo 347 recogerá, agrupando por "tercero" y "clave \[A (compras) o B (ventas)\]", las siguientes operaciones de compra/venta que superen la cifra de 3.005,06 euros:

-   compra/venta de bienes/servicios (no sujetos a retención) dentro del territorio de aplicación del impuesto (IVA), España y Baleares
-   compra/venta de servicios desde/hacia el resto del mundo, incluyendo Canarias, Ceuta y Melilla.

No se van a tener en cuenta:

-   operaciones de compra/venta de bienes/servicios intracomunitarias, por reflejarse en otro modelo de Hacienda, el Modelo 349, excepto las operaciones que no se incluyen en el Modelo 349.
-   importaciones/exportaciones de bienes.

#### **Operaciones de compra y venta acogidas a RECC**

Etendo permite la introducción y contabilización de facturas de compra y de venta acogidas al RECC (Régimen Especial de Criterio de Caja).

Para ello:

-   la "Organización" debe estar acogida a este régimen
-   o bien no estar acogida, pero sí alguno de los proveedores de los cuales recibe facturas de compra.

Estas organizaciones deben tener aplicado el juego de datos del módulo "Spain AEAT Modelo 347 Cash VAT compatible".

Este módulo incluye un juego de datos que relaciona los impuestos de IVA de Caja con los parámetros correspondientes del Modelo 347.

Las transacciones de compra/venta se recogen en el Modelo 347 de forma anual conforme al criterio de devengo general de IVA y marcadas como "Operación de IVA de Caja". Además, se incluye la parte correspondiente anual devengada conforme al criterio de IVA de Caja en otro campo.

**Transmisión de inmuebles**

Etendo permite la introducción y contabilización de transmisiones (ventas) de bienes inmuebles sujetas a IVA.

Este tipo de operaciones se recogen de forma separada en el modelo 347.

Es por ello que se ha creado en el módulo de impuestos para España:

-   categorías de impuestos específicas para los B. Inmuebles (IVA Normal B.Inmuebles e IVA Reducido B.Inmuebles)
-   rangos de impuestos (IVA) de compra/venta de bienes inmuebles

y en el conjunto de datos del 347:

-   un parámetro específico denominado "Transmisiones de Inmuebles" ligado a los impuestos de venta de bienes inmuebles.

#### **Transmisión de inmuebles sujetas a RECC**

Este tipo de transacciones también se incluyen en el Modelo 347 de forma separada, en cómputo anual, y marcadas como "Operación IVA Caja".

### **Arrendamientos**

Etendo permite la introducción y contabilización de facturas de compra y de venta que incluyan arrendamiento de locales de negocio sujetos a IVA.

Solo en el caso de arrendamientos de locales de negocio por parte del propietario de dicho local, se deberá además incluir información adicional sobre dicho inmueble/local, en un registro de tipo Inmueble específico. Para ello, aquellos locales que se den de alta en el maestro de productos susceptibles de ser alquilados deberán configurarse como tales tras activar el nuevo parámetro "Local arrendado".

Esto implica rellenar datos como los que se muestran en la siguiente imagen:

![](../../../../../assets/drive/dE833IZAyk5YYiQiYB9eDDk6wxK_0btiWm0ZxEGjetv8EO6eEVaFX1l49jftJWX3Kzpsjf7CYhV2xKGpTzoPPIHnWOtBreM6VjXKc9pppnC3uX0Da8TQSwz_CSSxFmBEVhREbwCzxTxCExDC9scqtRA.png)

Este tipo de operaciones tienen que reportarse de forma separada en el 347 tal y como se muestra en la siguiente imagen:

![Arrendamiento fichero.png](../../../../../assets/drive/jbFjoMyVVnHbJWnBIr3G76slsiwl0sB1cuiVHPyZU3Fxi0xayrKTqa6KnmpwSN6pZAUm3FPIwxGY8b7sfijsMd2dXLmxmn4WI85_Pr8_F41aL7Y3GQUXNZYqaM4uvGleErZpzWqX3KiMv6ElEGHuxt8.png)

La transacción de venta (B) con el cliente "Cliente Arrendamiento" por un importe anual de 30.310,50, incluye además el arrendamiento de un inmueble por un importe de 13.370.50.

#### **Arrendamientos en RECC**

Estas operaciones se reflejan de forma anual en el modelo 347, marcadas como tal, incluyéndose también la información referente al registro del inmueble arrendado por el declarado.

### **Cobros en efectivo**

Etendo permite la introducción y contabilización de facturas de venta y sus correspondientes cobros en efectivo depositados y contabilizados en Etendo a través de cuentas financieras del tipo "Caja".

Se recomienda configurar el método de pago "Contado" asociado a la cuenta financiera "Caja" como se detalla a continuación:

-   Permitido para cobro
-   Depósito automático en cuenta
-   Cuenta de depósito = Cuenta contable para depósito.
-   los cobros que para un tercero (cliente) y para un periodo, por ejemplo 2014, que lógicamente será el periodo/año para el cual generamos el 347, superen el umbral de 6.000,00 €
    -   Dicho cobro puede referirse a operaciones incluidas en facturas de venta contabilizadas en 2014 o años anteriores.

![Cobro Efectivo 2.png](../../../../../assets/drive/rQsEfez1_-0gnYadOcq2Dp9ptPt-fpXnvDJr-dZQKfhGd4CbMhpIZl8--qafNSbneZvk0iTvjQdOyesMqfRe8UKT1l8bwOYiPd4PojgZsEHUXOjQ5o5TiOrFYFxOVfBKW4hIp9qC0W8mkxbVsM54wz4.png)

![Cobro Efectivo 1.png](../../../../../assets/drive/Lxv-BIcYyAGs73YiuQW3z8G7HaswKFky4KLo0tygiKNTTsVyOQuux39shCmeBOucaw5We-Pq56fRIDdRr4VeMlWN2ffdh1Pw-u931b7tv1Ejq87qM-waVMN6DMHFg4VKOpgsvPeTu6Qwfx0BT3Rf_3k.png)

En el fichero ejemplo anterior se puede comprobar que:

-   los cobros en efectivo tanto del "Cliente Efectivo" (por importe de 18.000,00) como del "Cliente Efectivo Varios" (por importe de 6.560,00) se especifican de forma separada en las posiciones (101-115). La diferencia entre estos cobros es:
    -   para el "Cliente Efectivo Varios", la operación que generó el cobro en efectivo en el año 2014 se devengó y se declaró en el año 2013.  
        Esa es la razón por la cual no aparece importe de operación alguno en las posiciones 83-98 y el año de devengo de la operación es 2013.
    -   para el "Cliente efectivo B", la operación que generó el cobro en efectivo se devenga y se cobra en el año 2014, y forma parte del total de operaciones por importe de 81.675,00.

Faltaría un último caso:

El caso en el que un cobro/s del año en curso (2014), sea un cobro/s de transacciones devengadas en un periodo/año anterior y, por tanto, ya declaradas, y transacciones devengadas en el periodo/año en curso y, por tanto, no declaradas, tal y como se muestra en la siguiente imagen:

![Efectivo C 1.png](../../../../../assets/drive/UNvoZgjSZH4I3jP_aiFtWoh588bAF9cXNFgxPj9QwdIVRaSs2LQPqaO0OfaumKmjQOuONVkzQGnDksNIoLc7WsaMn_lM2LfMrDdYTlFaM7rQA2UzZu06m4Yujf8I4zN_3XE-sPOl7SnRi8i7pXJkujA.png)

![Efectivo C 2.png](../../../../../assets/drive/fUbrPtlbC-3LRPMGAoFSLSg5WJL9aJnB-ArVFC3JAq-ED3T3EyPf4rNPjlEEPdIhSqX31YFcp95zSSdXDdxNAwR0Jj6APn121ZA20w1dwxW571BuD2nXIjhchVDKE4BEHosSqTq9cd39qycG3KI9u5M.png)

En la imagen anterior, se ha producido un cobro en el año 2014 por importe de 48.188,25; de los cuales 7.350,75 son por operaciones realizadas y declaradas en el año 2014 y el resto 40.837,50 por operaciones realizadas y declaradas en un ejercicio anterior (2013).

#### **Cobros en efectivo en RECC**

Todo lo dicho en este apartado aplica igualmente a las operaciones de venta en IVA de Caja que se cobran en efectivo, salvo que en este caso no aplicaría un "Ejercicio" de devengo anterior a 2014, ya que el periodo de validez de este régimen comenzó el 1 de enero de 2014.

Además del importe anual de las operaciones y el importe anual devengado en criterio de IVA de Caja, debe añadirse el importe percibido en metálico, junto con el ejercicio de devengo de dichas operaciones.

### **Presentación del modelo 347 en formato electrónico**

La presentación telemática del modelo 347 en formato electrónico requiere que las empresas tengan un NIF español así como un certificado electrónico emitido por la “Fábrica Nacional de Moneda y Timbre” (FNMT) u otro certificado válido y reconocido por Hacienda.

La presentación telemática puede realizarse a través de la página web de la [Hacienda Pública española](https://sede.agenciatributaria.gob.es/Sede/procedimientoini/GI27.shtml){target="_blank"}.

#### **Datos en los ficheros csv**

Tal y como ya se ha mencionado, con el módulo "Spain AEAT Modelo 347 for APR" se generan, además del fichero "txt" del Modelo 347, dos ficheros adicionales "\*.csv", un fichero denominado "Facturas.csv" y otro fichero denominado "Metalico.csv".

El fichero csv "XXXFacturas.csv" incluye las siguientes columnas:

-   "**Tipo de documento**".  
    Estas son las facturas estándar (AP/AR Invoice, AP/AR Credit Memo..etc) de Etendo
-   "**Número de documento**"  
    O número de factura/abono.
-   "**Tercero**"  
    Cliente o proveedor.
-   "**NIF/CIF**" del tercero.
-   "**Fecha Factura**"
-   "**Fecha Contable**"  
    Fecha contable de la factura.
-   "**Impuesto**"  
    Impuestos del dataset de impuestos para España ligados al parámetro del Modelo 347 correspondiente.
-   "**IVA de Caja**"  
    Esta columna nos indica si la factura está o no sujeta a IVA de Caja.
-   "**Cuota**"  
    Cuota ligada al tipo de impuesto incluido en la factura
-   "**Base Imponible**"  
    Base imponible ligada al impuesto incluido en la factura.
-   "**Total**"  
    Suma de la base imponible y la cuota. Este valor es el que hay que tener en cuenta ya que el 347 incluye importes totales, incluido el IVA, al ser una declaración de operaciones con terceros y no una liquidación de IVA.
-   "**Tipo de Línea**"  
    Dado que en el 347 se tiene que incluir de forma separada tanto los arrendamientos como las transmisiones de bienes inmuebles y operaciones de inversión del sujeto pasivo, por tanto, en este campo las opciones que hay son "vacío" para operaciones de compra/venta normales, "Arrendamientos", "Transmisión B. Inmuebles" e "Inversión Sujeto Pasivo".

El fichero csv "XXXMetálico.csv" incluye las siguientes columnas:

-   "**Cuenta Financiera**"  
    Cuentas financieras de tipo "Caja" de Etendo.
-   "**Línea de Transacción**"  
    Número de línea de la transacción en la pestaña "**Transacción**" de la cuenta financiera.
-   "**Identificador de Transacción**"  
    Identificador formado por la cuenta financiera, la divisa, el número de cobro, la fecha del cobro, el tercero y el importe del depósito/cobro.
-   "**Tercero**"
-   "**NIF/CIF**" del tercero.
-   "**Fecha Contable**"  
    Fecha contable del cobro.
-   "**Ejercicio**"  
    Ejercicio en el cual se devengó la operación o factura que se cobra. Este ejercicio puede ser 2014 o anterior para declaraciones del ejercicio 2014.
-   "**Importe transacción**"  
    Importe del cobro en metálico.

Estos ficheros csv nos van a permitir saber, por ejemplo:

-   qué tercero se debe incluir en la declaración y con qué importes por haberse superado el límite de 3.005,06 € en el volumen anual de operaciones realizadas con él.
-   qué tercero no se debe incluir en la declaración por no haberse superado el límite de 3.005,06 € en el volumen anual de operaciones realizadas con él.
-   cuáles son las facturas de compra cuya suma equivale al "Importe Anual/Trimestral de Operaciones" realizadas con un proveedor en concreto
-   o bien cuáles son los cobros en efectivo cuya suma equivale al "Importe percibido en metálico" de un cliente en concreto, incluido en la declaración.

#### **Presentación de declaraciones sustitutivas**

Es necesario presentar una declaración sustitutiva cuando dicha declaración tenga por objeto anular y sustituir completamente a otra declaración anterior para el mismo periodo ya enviada a Hacienda, en la cual se hubieran incluido datos inexactos o erróneos.

Para ello, el usuario deberá realizar en la aplicación los cambios en los datos/transacciones pertinentes y volver a generar la declaración 347 como fichero indicando:

-   que la declaración es sustitutiva
-   el número de la declaración original que se sustituye

![](../../../../../assets/drive/beimgAXSJ1DvjNuJHa1G2tIQaIYdpHt769PulMwVmx7Y7bT0NJvb08DTbx5rt5GTBVuWu7XxfJ5ZTGw7iyFufV-kRKiw2OCLzoNH17Ul6h3y5ajyc1CcVbAr-XqjfQKBAnUFcjLZ7g1n27uXFZtbX5c.png)

---

Este trabajo es una obra derivada de [Openbravo Localización Española](https://wiki.openbravo.com/wiki/Openbravo_Localizaci%C3%B3n_Espa%C3%B1a){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo licencia [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.