---
title: Localización Española
---
:octicons-package-16: Javapackage: com.etendoerp.localization.spain.extensions

## Descripción
El bundle de Localización Española contiene los módulos que añaden funcionalidades a Etendo para ajustar el ERP a los requerimientos legales y/o fiscales españoles.

## Módulos

- [Spain SII](/products/etendo-classic/optional-features/bundles/spain-localization/sii-para-iva)
- [Tax Report: Modelo 303 (Spain)](/products/etendo-classic/optional-features/bundles/spain-localization/modelo-303)
- [Withholding Report: Modelo 190 (Spain)](/products/etendo-classic/optional-features/bundles/spain-localization/modelo-190)
- [Spain AEAT Modelo 347 for APR](/products/etendo-classic/optional-features/bundles/spain-localization/modelo-347)
- [Modelo 349](/products/etendo-classic/optional-features/bundles/spain-localization/modelo-349)
- [Impuestos para España](/products/etendo-classic/optional-features/bundles/spain-localization/impuestos-para-españa)
- [Intrastat](/products/etendo-classic/optional-features/bundles/spain-localization/intrastat)
- [Tax Report: Modelo 390 (Spain)](/products/etendo-classic/optional-features/bundles/spain-localization/modelo-390)
- [Libro de Facturas](/products/etendo-classic/optional-features/bundles/spain-localization/libro-de-facturas)
- [Configuración de Impuestos para Libro de Facturas](/products/etendo-classic/optional-features/bundles/spain-localization/configuracion-de-impuestos-para-libro-de-facturas)
- Incoterms
- European Union Countries
- Provincias de España
- Legal Representative of the Organization
- I.A.E. Epigraphs (Epígrafes del I.A.E.)
- CIF and NIF validator
- Validador de número de cuenta financiera
- Check Printing
- Tipo de Número de Identificación de Tercero
- Professional Localization pack Spain (España) Datasets
- Multidimensional Tax Report
- Cuaderno 43
- 3 digits ISO country codes
- Métodos de Pago
- Tax Report Launcher
- Spanish Tax Module Improvements
- Nueva versión del módulo de Impuestos de España
- Condiciones de pago
- Chart of accounts: PGC 2007 General
- Chart of accounts: PGC 2007 PYMEs
- Professional Localization pack Spain (España)
- Localization pack Spain (España)
- Traducción al español del módulo 'Default Jobs'
- JSON Datasource Translation: Spanish Spain (es_ES)
- Workspace & Widgets Translation: Spanish Spain (es_ES)
- User Interface Selector Translation: Spanish Spain (es_ES)
- Traducción al Español del módulo Payment Report
- Number To Word
- User Interface Client Kernel Translation Spanish Spain(esES)
- Translation: Spanish-Spain (es_ES) español-España
- Openbravo Multi Business Partner Selector
- Orders Awaiting Delivery Spanish (Spain) Translation
- Smartclient Translation: Spanish Spain (es_ES)
- Query/List Widget Translation Spanish Spain (es_ES)
- Widgets Collection Translation Spanish Spain (es_ES)
- Advanced Payables and Receivables - Spanish Translation
- User Interface Application Translation Spanish Spain (es_ES)
- Alerts: Accounting
- SOAP with Attachments API for Java Implementation
- Payment Method Type
- Javax XML SOAP API
- HTML Widget Translation Spanish Spain (es_ES)
- OpenID Service Integration Translation Spanish Spain
- Integration with Google APIs Translation Spanish Spain
- Openbravo 3.0 Translation Pack: Spanish Spain (es_ES)

## Incoterms

:octicons-package-16: Javapackage: org.openbravo.module.incoterms

Este módulo añade el listado de Incoterms a Etendo Classic.

Los Incoterms or International Commercial Terms son una serie de términos de venta internacionales, publicados por la Cámara Internacional de Comercio y ampliamente utilizados en transacciones comerciales internacionales. Son utilizados para dividir costos de transacción y responsabilidades entre compradores y vendedores.

## European Union Countries

:octicons-package-16: Javapackage: org.openbravo.module.eucountries

Este módulo identifica qué países pertenecen a la Unión Europea.

## Provincias de España

:octicons-package-16: Javapackage: org.openbravo.spain.regions

Este módulo añade el listado de provincias españolas al ERP.

## Legal Representative of the Organization

:octicons-package-16: Javapackage: org.openbravo.module.organization.representative.es

Este módulo añade a la ventana de la Organización una pestaña que permite configurar el Representante Legal de la Organización. Pueden declararse uno o varios Representantes.

La pestaña “Representante Legal” que se añade a la ventana de Organización permite configurar el Representante Legal de la organización, dato que es obligatorio para el Modelo 390.

## I.A.E. Epigraphs (Epígrafes del I.A.E.)

:octicons-package-16: Javapackage: org.openbravo.module.epigrafes.iae.es

Este módulo agrega en la ventana de Organización una pestaña titulada “Actividades del IAE”, donde se pueden indicar todas las actividades en las que la empresa ha estado trabajando. Es posible seleccionar los Epígrafes del Impuesto sobre Actividades Económicas (IAE) que estén asociados a la Organización.

El tipo de información agregada por este módulo se requiere en determinados modelos tributarios oficiales, por ejemplo en el Modelo 390.

En este módulo se incluye el conjunto correspondiente a la clave 1. Si se desea incluir un epígrafe que pertenezca a cualquier otra clave, se debe crear un nuevo registro en la ventana Epígrafes IAE e incluirlo en un registro de la solapa “Actividades del IAE” de la ventana de Organización.

## CIF and NIF validator

:octicons-package-16: Javapackage: org.openbravo.module.cifnifvalidator

:octicons-package-16: Javapackage: org.openbravo.module.cifnifvalidator.es_es

Este módulo implementa un callout que comprueba si se ha introducido un Número de Identificación Fiscal (NIF) válido al configurar un tercero.

El Número de Identificación Fiscal (NIF) permite identificar de forma inequívoca a personas físicas o jurídicas.

## Validador de número de cuenta financiera

:octicons-package-16: Javapackage: org.openbravo.module.finactvalidator.es

Este módulo permite validar el número de cuenta financiera de la organización y el número de cuenta de banco del tercero, de acuerdo con la normativa española. Verifica que se ajusten al formato definido para España, y que los dígitos de control sean correctos.

## Check Printing

:octicons-package-16: Javapackage: org.openbravo.finance.checkprinting

:octicons-package-16: Javapackage: org.openbravo.finance.checkprinting.es_es

Este módulo permite la impresión de cheques desde Etendo. Además, provee un sistema para buscar datos históricos y poder volver a imprimir un cheque en caso de error.

Este módulo incluye el dataset "Check Printing Infraestructure" que crea un formato de impresión llamado "Standard Format", un método de pago denominado “Check" y un proceso de ejecución llamado "Check Printing".

### Ejecutar pago

Después de crear un pago, permanecerá en “Awaiting Execution”. Se necesita un paso adicional para ejecutarlo y proveer el primer número para la secuencia de los cheques, esto puede hacerse a través del formulario de “Payment Execution”.

Para seleccionar los pagos que serán impresos, tras hacer click en “Process” aparece un pop up que requiere un número para el cheque. Este número es opcional.
El sistema creará automáticamente las entradas en la ventana “Check Printing” en estado “Not Printed”. Además, el sistema asociará automáticamente el tipo de documento “Check” y el número de secuencia.

### Imprimir cheques

Se genera una nueva ventana para imprimir cheques. Esta puede encontrarse en _Gestión Financiera > Gestión de cobros y pagos > Transacciones > Impresión de cheques_. La información de esta ventana será automáticamente completada cuando se ejecuten transacciones payment out que están usando el método de pago “Check”.

La ventana aplica un primer filtro para mostrar solamente los cheques que están en estado “Not printed”. Ese filtro puede ser removido para mostrar todos los cheques, incluidos los que están en estado “Printed”.

Para imprimir uno o varios cheques, se deben seleccionar y presionar el botón “Imprimir”.

## Tipo de Número de Identificación de Tercero

:octicons-package-16: Javapackage: org.openbravo.module.bptaxidkey

Este módulo añade el campo “Número de identificación de tercero” a la ventana de Terceros. Este dato es utilizado por los Libros de Registro de Facturas.

## Professional Localization pack Spain (España) Datasets

:octicons-package-16: Javapackage: org.openbravo.proflocalization.spain.dataset

Este módulo contiene un dataset que añade permisos para ciertas ventanas y procesos incluidos en el pack de Localización Española para el rol de Finanzas.

## Multidimensional Tax Report

:octicons-package-16: Javapackage: org.openbravo.module.invoicetaxreportenhanced30

:octicons-package-16: Javapackage: org.openbravo.module.invoicetaxreportenhanced30.es_es

Este módulo genera un informe que permite al usuario obtener un listado de aquellas transacciones registradas en el sistema que tienen implicaciones fiscales.

El módulo permite obtener los datos necesarios para cumplimentar modelos de la AEAT que no se generan como un fichero válido desde Etendo. Por ejemplo, el Modelo 115 (Trimestral) de Retenciones e ingresos a cuenta sobre rentas procedentes del arrendamiento de inmuebles urbanos.

La información obtenida mediante este módulo es útil para que las empresas puedan completar manualmente y enviar los informes requeridos por las autoridades. Se le brinda al usuario final información fiscal relevante, que luego puede ser clasificada según las necesidades.

## Cuaderno 43

:octicons-package-16: Javapackage: org.openbravo.module.cuaderno43.es

Este módulo implementa el formato de importación bancaria “Cuaderno 43” (Norma AEB 43). Los Cuadernos o Normas AEB (Asociación Española de la Banca) son una serie de normas o protocolos comunes a todas las entidades bancarias que operan en España y que fijan las características de los ficheros informáticos emitidos o recibidos por una entidad financiera.

## 3 digits ISO country codes

:octicons-package-16: Javapackage: org.openbravo.module.countryisocode

Los códigos ISO de países son utilizados a nivel mundial para representar a cada país con dígitos. Este módulo provee el dataset que vincula los países con su código ISO.

## Métodos de Pago

:octicons-package-16: Javapackage: org.openbravo.spanishdefaultdata.paymentmethods

Este módulo contiene las formas de pago más utilizadas en España, las cuales pueden ser utilizadas en el módulo de gestión avanzada de cobros y pagos. Incluye Recibo domiciliado, Recibo, Letra Aceptada, Crédito Documentario, Contrato Adjudicación, etc.

El módulo de Métodos de Pago refiere a las formas de pago utilizadas por las empresas, por ejemplo contado o tarjeta de crédito. Etendo define un flujo de pagos basado en la configuración de Métodos de Pago.

## Tax Report Launcher

:octicons-package-16: Javapackage: org.openbravo.module.taxreportlauncher

:octicons-package-16: Javapackage: org.openbravo.module.taxreportlauncher.es

Este módulo consiste en un launcher de impuestos que permite la definición de informes y de sus parámetros, e incluye la clase java asociada que contiene la lógica de negocios que será aplicada.

Este módulo permite crear y enviar formularios de informe de impuestos desde Etendo. Es posible ingresar los datos requeridos en un formulario en particular y generar un fichero que luego puede ser enviado a las autoridades.
Los impuestos para una localización determinada se instalan con módulos que extienden de este.

### Configuración de declaraciones de impuestos

Para habilitar el uso del launcher de declaraciones de impuestos, se deben descargar e instalar los siguientes módulos:

- Tax Report Launcher
- Módulos individuales de informes para los informes de impuestos que se quieren utilizar.
- Módulos de códigos de transacción y de clave tributaria.

Cuando estos módulos están instalados, es necesario asociar los rangos de impuestos con los parámetros de las declaraciones de impuestos.

#### Códigos de transacción

Los códigos de transacción representan transacciones en las que se paga IVA. Por ejemplo, una compra de bienes. Hay dos códigos de transacción predeterminados en Etendo: E para transacciones de venta y A para transacciones de compra. Los códigos de transacción están en un módulo que se puede descargar y aplicar.

#### Claves y subclaves de impuestos

El sistema fiscal español designa un conjunto específico de letras para cada tipo de ingreso (por ejemplo, la P representa la renta de una propiedad alquilada). Las claves y subclaves de impuestos están en un módulo que se puede descargar y aplicar.

#### Asociar un rango de impuestos con un parámetro de impuestos

- Se realiza a partir de la ruta _Gestión Financiera > Contabilidad > Configuración > Rango Impuesto._
- En la vista de cuadrícula, se selecciona la tasa de impuestos que se desea asociar con un parámetro de impuestos.
- Se selecciona la pestaña “Parámetro de declaración”.
- En la lista de Parámetros del informe de impuestos, se debe seleccionar el parámetro que se desea asociar con la tasa de impuestos.
- Clic en “Guardar”.

#### Usar el Generador de Declaraciones de Impuestos para generar un informe

- Ruta: _Gestión Financiera > Contabilidad > Herramientas de análisis > Generador de declaraciones de impuestos_.
- Seleccionar de la lista de “Declaración de impuestos” cuál es el informe requerido.
- Seleccionar la organización para la cual se quiere generar el informe de impuestos. Para ello, la organización debe ser del tipo entidad legal con contabilidad.
- Seleccionar el esquema contable que se desea utilizar para el informe de impuestos. Se puede seleccionar el esquema de contabilidad propio de la organización o un esquema de contabilidad de una organización padre.
- Seleccionar un calendario. El sistema establece de forma predeterminada el calendario de la organización, pero se puede seleccionar cualquier otro. Esto es especialmente útil cuando el calendario de la organización no se basa en años naturales (de enero a diciembre), pero el informe requiere períodos y años naturales.
- En la lista “Año”, se debe seleccionar el año fiscal para el que se desea crear el informe.
- En la lista “Período”, se debe seleccionar el período para el que se desea crear el informe. Por ejemplo, si el informe se ha configurado para enviarse al final de cada trimestre, se puede seleccionar el trimestre correcto de la lista.
- Al hacer clic en “Parámetros de entrada”, aparece una ventana que muestra campos a completar con información necesaria para el informe. Los campos que aparecen dependen de la configuración del informe fiscal y deben ser completados.
- En el campo “Nombre de archivo” se asigna al informe un nombre de archivo.
- Click en “Generar archivo electrónico”.
- Aparece un mensaje que pregunta si desea ver o guardar el archivo. Tras seleccionar la opción “Guardar”, se debe especificar una ubicación de archivo.


## Spanish Tax Module Improvements

:octicons-package-16: Javapackage: org.openbravo.module.taximprovements.es

:octicons-package-16: Javapackage: org.openbravo.module.taximprovements.es_es

Este módulo añade campos en la ventana de “Rango de impuestos” para mejorar la configuración y administración de los impuestos de España. Los campos añadidos son: Tipo de libro, Inversión de sujeto pasivo, Recargo de equivalencia e Impuesto intracomunitario.

- Tipo de Libro (“Tax Book Type”): El usuario puede configurar si un rango de impuesto debe ser reportado en la compra (recibido) o en la venta (enviado) del Libro de Facturas.
- Inversión de Sujeto Pasivo ("Reverse Charge"): El usuario puede seleccionar este check para indicar que un rango de impuesto es una tasa de impuesto de cargo inverso
- Recargo de equivalencia ("Equivalent Charge"): El usuario puede seleccionar este check para indicar que un rango de impuesto es un recargo de equivalencia.
- Impuesto Intracomunitario ("Intra Community Tax"): El usuario puede seleccionar este check para indicar que un rango de impuesto es intracomunitario.

## Nueva versión del módulo de Impuestos de España

Este módulo incluye en los impuestos españoles el IGIC Canario y el IPSI aplicable en Ceuta y Melilla.

## Condiciones de pago

:octicons-package-16: Javapackage: org.openbravo.spanishdefaultdata.paymentterms

Este módulo contiene las condiciones de pago más utilizadas en España. Entre ellas se incluyen el pago en "30 días", "60 días", "90 días", "120 días", "50% en el acto, resto 60 días", "20% a 10 días resto a 30 días" y "20% a 15 días, 40% a 30 días, resto a 60 días".

## Chart of accounts: PGC 2007 General

:octicons-package-16: Javapackage: org.openbravo.localization.spain.referencedata.accounts

Este módulo añade el Plan de Cuentas General (Modelo Normal) conforme a los requerimientos vigentes en España.

Etendo puede configurarse para realizar la contabilidad en base a distintos esquemas contables.

El cuadro de cuentas define las cuentas contables y la estructura del balance de situación y de la cuenta de resultados. La estructura de la cuenta de resultados es de una sola columna. El cuadro de cuentas definido permite utilizar las cuentas contables y obtener la información del balance y la cuenta de resultados.

El Plan de Cuentas General tiene la siguiente estructura:

- Marco Conceptual de la Contabilidad
- Normas de registro y valoración
- Cuentas anuales
- Cuadro de cuentas
- Definiciones y relaciones contables

El Plan de Cuentas que añade este módulo es el que debe ser utilizado si una empresa cumple alguna de estas condiciones:

- El total de las partidas del activo de la empresa supera los dos millones ochocientos cincuenta mil euros.
- El importe neto de la cifra anual de negocios supera los cinco millones setecientos mil euros.
- El número medio de trabajadores empleados durante el ejercicio es superior a cincuenta.
- La empresa ha emitido valores admitidos a negociación en mercados regulados o sistemas multilaterales de negociación, de cualquier Estado miembro de la Unión Europea.
- Forma parte de un grupo de sociedades que formule o debiera haber formulado cuentas anuales consolidadas.
- La moneda funcional es distinta del euro.
- Se trata de una entidad financiera que capta fondos del público, asumiendo obligaciones respecto a los mismos.

## Chart of accounts: PGC 2007 PYMEs

:octicons-package-16: Javapackage: org.openbravo.localization.spain.referencedata.accounts.pymes

Este módulo añade el Plan de Cuentas PYMES conforme a los requerimientos vigentes en España.

Etendo puede configurarse para realizar la contabilidad en base a distintos esquemas contables.

El cuadro de cuentas define las cuentas contables y la estructura del balance de situación y de la cuenta de resultados. La estructura de la cuenta de resultados es de una sola columna. El cuadro de cuentas definido permite utilizar las cuentas contables y obtener la información del balance y la cuenta de resultados.

El Plan de Cuentas que añade este módulo es el utilizado por las pequeñas y medianas empresas en España. Tiene la siguiente estructura:

- Marco Conceptual de la Contabilidad
- Normas de registro y valoración
- Cuentas anuales
- Cuadro de cuentas
- Definiciones y relaciones contables

## Professional Localization pack Spain (España)

Este módulo ofrece a las empresas españolas un set de módulos que adaptan Etendo a los requerimientos comerciales de España, permitiendo realizar procesos de manera rápida y eficaz. Incluye una gestión avanzada de cuentas a cobrar y a pagar.

## Localization pack Spain (España)

:octicons-package-16: Javapackage: org.openbravo.localization.spain30

Este módulo ofrece a las empresas españolas un set de módulos que adaptan Etendo a los requerimientos comerciales de España, permitiendo realizar procesos de manera rápida y eficaz.

## Traducción al español del módulo 'Default Jobs'

:octicons-package-16: Javapackage: com.smf.jobs.defaults.es_es

## JSON Datasource Translation: Spanish Spain (es_ES)

:octicons-package-16: Javapackage: org.openbravo.service.datasource.es_es

## Workspace & Widgets Translation: Spanish Spain (es_ES)

:octicons-package-16: Javapackage: org.openbravo.client.myob.es_es

## User Interface Selector Translation: Spanish Spain (es_ES)

:octicons-package-16: Javapackage: org.openbravo.userinterface.selector.es_es

## Traducción al Español del módulo Payment Report

:octicons-package-16: Javapackage: org.openbravo.financial.paymentreport.es_es

## Number To Word

:octicons-package-16: Javapackage: org.openbravo.numbertoword

:octicons-package-16: Javapackage: org.openbravo.numbertoword_es

:octicons-package-16: Javapackage: org.openbravo.numbertoword.es_es

## User Interface Client Kernel Translation Spanish Spain(esES)

:octicons-package-16: Javapackage: org.openbravo.client.kernel.es_es

## Translation: Spanish-Spain (es_ES) español-España

:octicons-package-16: Javapackage: org.openbravo.localization.spain.referencedata.translation.esES

## Openbravo Multi Business Partner Selector

:octicons-package-16: Javapackage: org.openbravo.utility.multiplebpselector

:octicons-package-16: Javapackage: org.openbravo.utility.multiplebpselector.es_es

## Orders Awaiting Delivery Spanish (Spain) Translation

:octicons-package-16: Javapackage: org.openbravo.reports.ordersawaitingdelivery.es_es

## Smartclient Translation: Spanish Spain (es_ES)

:octicons-package-16: Javapackage: org.openbravo.userinterface.smartclient.es_es

## Query/List Widget Translation Spanish Spain (es_ES)

:octicons-package-16: Javapackage: org.openbravo.client.querylist.es_es

## Widgets Collection Translation Spanish Spain (es_ES)

:octicons-package-16: Javapackage: org.openbravo.client.widgets.es_es

## Advanced Payables and Receivables - Spanish Translation

:octicons-package-16: Javapackage: org.openbravo.advpaymentmngt.es_es

## User Interface Application Translation Spanish Spain (es_ES)

:octicons-package-16: Javapackage: org.openbravo.client.application.es_es

## Alerts: Accounting

:octicons-package-16: Javapackage: org.openbravo.alerts.accounting30

:octicons-package-16: Javapackage: org.openbravo.alerts.accounting30.es_es

## SOAP with Attachments API for Java Implementation

:octicons-package-16: Javapackage: org.openbravo.util.saaj.impl

## Payment Method Type

:octicons-package-16: Javapackage: org.openbravo.module.paymentmethod.type

## Javax XML SOAP API

:octicons-package-16: Javapackage: org.openbravo.util.javax.xml.soap

## HTML Widget Translation Spanish Spain (es_ES)

:octicons-package-16: Javapackage: org.openbravo.client.htmlwidget.es_es

## OpenID Service Integration Translation Spanish Spain

:octicons-package-16: Javapackage: org.openbravo.service.integration.openid.es_es

## Integration with Google APIs Translation Spanish Spain

:octicons-package-16: Javapackage: org.openbravo.service.integration.google.es_es

## Openbravo 3.0 Translation Pack: Spanish Spain (es_ES)

:octicons-package-16: Javapackage: org.openbravo.v3.translation.pack.es_es
