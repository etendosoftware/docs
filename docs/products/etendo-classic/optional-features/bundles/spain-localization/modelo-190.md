---
title: Modelo 190
hide:
    - navigation
---
## Javapakages 
`org.openbravo.module.aeat190.es`

## **Introducción**

Esta sección explica el contenido y funcionamiento del módulo **"Modelo 190"**, incluído dentro del bundle de Localización Española para Etendo.

**Descripción del Modelo**

El módulo **Modelo 190** permite a las empresas cumplir con sus obligaciones fiscales relativas a la obligatoriedad de declarar las retenciones e ingresos a cuenta sobre rendimientos del trabajo y de actividades económicas, premios y determinadas ganancias patrimoniales e imputaciones de renta.

La presentación del Modelo 190 por vía telemática deberá efectuarse en el plazo comprendido entre los días 1 y 31 de enero de cada año, en relación con las cantidades retenidas y los ingresos a cuenta efectuados correspondientes al año natural inmediato anterior.

Con este módulo, el Modelo 190 se puede presentar a Hacienda como un fichero de texto válido, obtenido a través del "Generador de Declaraciones de Impuestos".

## **Contenido del fichero Modelo 190**

El fichero generado por Etendo, que cumple con el formato requerido por la Agencia Tributaria, contiene:

-   Una primera sección, llamada *registro tipo 1*, con información relativa a la empresa que presenta el informe, CIF, nombre de la empresa, persona de contacto y resumen de los detalles presentados.
-   Una segunda sección, llamada *registros tipo 2*, con la información relativa a la retención e ingresos a cuenta practicada a la empresa agrupada por tercero y año.

De esta forma, el informe puede contar con un único registro de tipo 1 y cero o varios registros de tipo 2.

Si el usuario abre el fichero generado con un editor de texto plano, verá una sucesión de números y letras prácticamente ilegibles para el ser humano. Si desea comprobar el contenido del fichero e incluso modificarlo antes de ser enviado a la Agencia Tributaria, puede importar dicho fichero en la AEAT (Ver abajo).

## **Instalación y aplicación del módulo**

### **Instalación**

Para su instalación del Modelo 190 de Etendo, el usuario debe seguir los pasos que se describen a continuación en función de la situación de partida:

-   Instalación de la última versión disponible de Etendo 
-   o la instalación del módulo de Localización Española.

!!! info
    Para la instalación del módulo de Localización Española, visite [_Marketplace_](https://marketplace.etendo.cloud/#/product-details?module=003B475055DD421B9483B5BE15AA48C5){target="_blank"}. 


### **Aplicación del módulo**

El módulo del Modelo AEAT 190 incluye el correspondiente "conjunto de datos" o "configuración" que relaciona los tipos/rangos de impuestos (retenciones, en este caso) para España con los parámetros del 190, por tanto:

-   Una vez instalado el módulo, la "configuración del Modelo 190" debe aplicarse a la **Entidad legal con Contabilidad** que corresponda, en la ruta de aplicación: Configuración General || Organización || **Gestión del módulo de Empresa.**
-   Importante, antes de aplicar esta configuración es importante haber aplicado previamente la configuración del módulo de impuestos, puesto que el Modelo 190 depende de éste.

![](/docs/assets/drive/NPmuokqQMPVWHGO_5axvvqS3kqWJ7TUYhtrgII9Adx2R4lsxQxCOECCclQxInjaTso4hIHruR7f8UNtrSAMuTvupjpsmZW-osW83k_TFV3UE_QFFP8igDGJf6ctmSmSFP5WLMyHfV8lI19X_wgXEO24.png)

Al instalar y aplicar este nuevo módulo, el usuario podrá comprobar que:

-   se han creado un nuevo informe, el modelo 190 anual que se encuentra en la ruta de aplicación: Gestión Financiera || Contabilidad || Configuración || Declaración de impuestos, tal y como se muestra en la siguiente imagen:  
     

![](/docs/assets/drive/0DGnsbvGSRglnOfedtcm1BRq0hExCnVLCnWNfG9twk0cA9ktqHih10dD1ufrzq3uGu1oafipUnxtCc7W08aw753gYX3AzuoAMZ6ZAyknSHIwLa9eAw-kajDMk6DOjGpTM5IOKb0pxrmcm5Dj31wI2ZM.png)

-   los rangos de impuestos se han asociado al correspondiente Parámetro del informe 190, con el fin de que las transacciones ligadas a dichos impuestos completadas y contabilizadas en el sistema, se tenga en cuenta en una u otra casilla/posición del fichero, tal y como se muestra en la siguiente imagen:  
     

![](/docs/assets/drive/jH29-HkAFNLN3w0RKpitrmjGJ918EMfwdfbMQmfE7qEeFhSAB-tRR9z-pNWDz34lm9xlhMN1ADfKDKwicm4h6282rQATMsMggwZUCfu4ZX6aBmki3PF1g8O_dzJVRa7i55QIMWkesDoXacrd4Rb9_RQ.png)

-   y, por último, el generador de declaraciones de impuestos permite la generación del fichero para la presentación de la declaración-liquidación del modelo 190, desde la ruta de aplicación: Gestión Financiera || Contabilidad || Herramientas de análisis || Generador de declaraciones de impuestos, tal y como se muestra en la siguiente imagen:  
     

![](/docs/assets/drive/duCdxzeDZl6Ym8W_h-APG_n78tbJ09PZ9MLqx11_Q2x96V2K1-TrVAh5I-apRPNWffmsIybEKB06xmRie5bzRHyi9Ljf70g6ekwyusOk8ZR5lg9_7cllbMklo9vRjRB73JbKdW4q8XxdL9CwrMW3eZE.png)

## **¿Qué se incluye en el Modelo 190 generado por Etendo?**

El informe generado por Etendo incluye únicamente las retenciones referentes a actividades económicas, puesto que es la información que el ERP maneja actualmente.

El resto de información que se incluye en el Modelo 190, como retenciones e ingresos a cuenta por rendimientos del trabajo, determinadas ganancias patrimoniales o premios, no está registrada en el ERP y, por lo tanto, no se puede incluir en el informe.

Sin embargo, si usted desea incluir esta información en su declaración, tan sólo debe importar el fichero generado por Etendo como se indica en [_Modelo 190_](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/declaraciones-informativas-ayuda-tecnica/modelos-190-198/modelo-190-formulario.html){target="_blank"}.

### **Tipos de documentos y retenciones que se incluyen en el informe**

El modelo 190 es un informe de retenciones, así que sólo se tendrán en cuenta facturas de compra con retenciones a terceros ubicados en España que estén contabilizadas y pagadas (parcialmente o completamente).

Dentro de las facturas de compra, se soportan todo el rango disponible actualmente:

-   Facturas de compra (AP Invoice)
-   Facturas de abono de compra (AP Credit Memo)
-   Facturas de compra negativas (AP Invoice negativas)
-   Facturas de tipo "Reversal" (Reversed Purchase Invoice)

### **Retenciones asociadas a parámetros del informe**

Las retenciones que vienen asociadas a los parámetros del modelo 190 son:

-   Details-Withholding\_G\_01, Clave tributaria G - subclave 01:
    -   Prestación servicios nacional 0% -15%R (-15%)
    -   Prestación servicios nacional 16% -15%R (-15%)
    -   Prestación servicios nacional 18% -15%R (-15%)
-   Details-Withholding\_G\_03, Clave tributaria G - subclave 03:
    -   Prestación servicios nacional 0% -7%R (-7%)
    -   Prestación servicios nacional 16% -7%R (-7%)
    -   Prestación servicios nacional 18% -7%R (-7%)
-   Details-Withholding\_H\_04, Clave tributaria H - subclave 04:
    -   Prestación servicios nacional 18% -1%R (-1%)

### **Retención proporcional al pago**

La retención a incluir en el fichero del modelo 190 es proporcional a la percepción íntegra efectivamente satisfecha durante el ejercicio correspondiente:

-   por ejemplo, si tenemos una factura contabilizada pero pagada en un 50% en 2011, el informe del 190 del 2011 incluirá la parte proporcional de la retención práctica en la factura, esto es, el 50%.

Además, si durante un ejercicio se han satisfecho facturas correspondientes a ejercicios anteriores, el fichero del modelo 190 incluirá una línea por cada uno de los pagos efectuados durante dicho ejercicio, correspondientes a facturas devengadas en años anteriores, indicando, por tanto, el año de devengo.

### **Cantidades indebidas o excesivamente percibidas en ejercicios anteriores**

El fichero del modelo 190 tiene en cuenta los datos relativos a cantidades reintegradas por sus perceptores en el ejercicio, como consecuencia de haber sido indebida o excesivamente percibidas en ejercicios anteriores, en estos supuestos:

-   cada reintegro se relaciona bajo la misma clave y, en su caso, subclave de percepción bajo la cual se incluyeron en su día las cantidades indebidas o excesivamente satisfechas
-   se refleja su importe en el campo "Percepción íntegra"
-   el campo "Signo de la percepción íntegra" se cumplimenta con la letra "N" (importe negativo)
-   y se consigna el valor (0) en el campo "Retenciones practicadas"
-   finalmente, se hace constar en el campo "Ejercicio devengo" el año en el que se devengaron originariamente las percepciones reintegradas.

!!! info
    Cuando se hayan producido reintegros procedentes de una misma persona o entidad que correspondan a percepciones originariamente devengadas en varios ejercicios, su importe se desglosa en varios apuntes o registros, de forma que cada uno de ellos refleje exclusivamente reintegros de percepciones correspondientes a un mismo ejercicio.


## **Generación del modelo 190**

Tal y como ya se ha explicado, el modelo 190, se genera como un fichero de texto válido conforme a los requerimientos de la AEAT desde la ruta de aplicación: **Gestión Financiera || Contabilidad || Herramientas de análisis || Generador de declaraciones de impuestos || Generador de declaraciones de impuestos**

Una vez que el usuario ha introducido los datos genéricos, tales como "organización", "ejercicio", "periodo" y otros, puede introducir los parámetros de entrada propios del 190:

![](/docs/assets/drive/Jbjc9g-xJ_iZ2B6_xDHfLV9umzxu0_R-HS5ss8jpczAYl654wdnKknjU_i6b8wqIRhiWQbeArp2hMAGaZTsj5_zoOHLAIEq-s8BhhTEbnFmoHYcfRaLoVcxI1TlCjyjuUQeXbM7ZN7AZAuBE9Z4YjXg.png)

En este caso, se puede especificar el nombre del fichero (si no queremos el que el sistema da por defecto), y la información necesaria en caso de generar una declaración sustitutiva.

## **Importación del modelo 190 en AEAT**

Una vez generado el fichero, el mismo tendrá que cargarse en la AEAT en la página correspondiente de [Agencia Tributaria](https://sede.agenciatributaria.gob.es/Sede/procedimientoini/GI10.shtml){target="_blank"}.