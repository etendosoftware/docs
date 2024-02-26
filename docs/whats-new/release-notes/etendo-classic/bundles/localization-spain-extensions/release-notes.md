---
title: Versiones Disponibles
tags:
  - Release Notes
  - Localizacion Española
  - Versiones
---
:octicons-package-16: Javapackage: `com.etendoerp.localization.spain.extensions`

:material-store: Etendo Marketplace:  [Bundle de Localizacion Española](https://marketplace.etendo.cloud/#/product-details?module=003B475055DD421B9483B5BE15AA48C5){target="_blank"}

## Introducción

| Versión | Fecha de Publicación | Desde Core | Hasta Core | Estado | GitHub|
| :--- | :--- | :--- | :--- | :---: | :---: |
| [1.9.0](#190) | 06/02/2024 | 22.4.3 | 23.4.x | CS | :white_check_mark:|
| [1.8.0](#180) | 26/01/2024 | 22.4.3 | 23.4.x | C  | :white_check_mark:|
| [1.7.0](#170) | 24/01/2024 | 22.4.3 | 23.4.x | C  | :white_check_mark:|
| [1.6.0](#160) | 29/12/2023 | 22.4.3 | 23.4.x | C  | :white_check_mark:|
| [1.5.2](#152) | 10/11/2023 | 22.4.3 | 23.3.x | C  | :white_check_mark:|
| [1.5.1](#151) | 01/11/2023 | 22.4.3 | 23.3.x | C  | :white_check_mark:|
| [1.5.0](#150) | 29/09/2023 | 22.4.3 | 23.3.x | C  | :white_check_mark:|
| [1.4.1](#141) | 19/09/2023 | 22.4.3 | 23.2.8 | C  | :white_check_mark:|
| [1.4.0](#140) | 27/06/2023 | 22.4.3 | 23.2.8 | C  | :white_check_mark:|
| [1.3.0](#130) | 24/05/2023 | 22.4.3 | 23.1.5 | C  | :white_check_mark:|
| [1.2.1](#121) | 26/04/2023 | 22.4.3 | 22.4.5 | C  |                   |
| [1.2.0](#120) | 03/03/2023 | 22.4.3 | 22.4.5 | C  |                   |
| [1.1.0](#110) | 03/02/2023 | 22.4.3 | 22.4.5 | C  |                   |
| [1.0.5](#105) | 12/01/2023 | 21.4.0 | 22.4.5 | C  |                   |
| [1.0.4](#104) | 07/12/2022 | 21.4.0 | 22.3.0 | C  |                   |
| 1.0.3 | 06/10/2022 | 21.4.0 | 22.3.x | C  |                   |
| [1.0.2](#102) | 11/07/2022 | 21.4.0 | 22.2.2 | C  |                   |
| [1.0.1](#101) | 16/06/2022 | 21.4.0 | \*     | C  |                   |
| 1.0.0 | 01/01/2022 | 21.4.0 | \*     | C  |                   |


## Versiones Disponibles

### 1.9.0
- Parámetros modelo 347 - Rangos nuevos 2023 \
Se asociaron nuevos parámetros de impuestos a los siguientes rangos:
  - Adquisiciones IVA 0% 
  - Entregas IVA 0%  
  - Entregas IVA 0+RE 0+0% 
  - Entregas IVA 0+RE 0+0% (+0% IVA) 
  - Entregas IVA 0+RE 0+0% (+0% RE) 
  - Entregas IVA 5% 
  - Entregas IVA+RE 21+1.75% 
  - Entregas IVA+RE 21+1.75% (+1.75%) 
  - Entregas IVA+RE 21+1.75% (+21%) 
  - Entregas IVA+RE 5+0.62% 
  - Entregas IVA+RE 5+0.62% (+0.62%) 
  - Entregas IVA+RE 5+0.62% (+5%) 
  - Servicios Prestados 0% 
### 1.8.0
- Nuevo diseño de registro - Modelo de impuestos 390 - Versión 2023 \
Se agregaron al parámetro "Recargo de Equivalencia" del grupo "IVA Devengado" los impuestos siguientes, declarados en las casillas que se explican a continuación:
    - Recargo de equivalencia - Tipo 0% - Base imponible [663]
    - Recargo de equivalencia - Tipo 0% - Cuota [664]
    - Recargo de equivalencia - Tipo 0,62% - Base imponible [665]
    - Recargo de equivalencia - Tipo 0,62% - Cuota [666]
### 1.7.0
- [EE-301](https://github.com/etendosoftware/com.etendoerp.localization.spain.extensions/issues/18) Se agregó un nuevo estado 'No Declarable en SII' para facturas de venta que tengan todos sus productos relacionados a impuestos configurados como 'No Declarables en SII'.
- [EE-796](https://github.com/etendosoftware/com.etendoerp.localization.spain.extensions/issues/19) Se corrigió el error en el que la página T303DID00 no se genera de forma correcta para el 303 del último periodo.
- Se añadió el nuevo diseño de registro para el Modelo de Declaración de Impuestos 190, versión 2023.
- Se añadió la oficina impositiva de Bizkaia en la configuración del SII para facturas recibidas.
### 1.6.0
- Se actualizó la compatibilidad de Core incluyendo hasta 23.4.x
- [EE-779](https://github.com/etendosoftware/com.etendoerp.localization.spain.extensions/issues/16){target="\_blank"} Se corrigió error al crear un libro de facturas simplificado con un socio comercial sin CIF
### 1.5.2
- [EE-741](https://github.com/etendosoftware/com.etendoerp.localization.spain.extensions/issues/9){target="\_blank"} Se añadió la traducción de la ventana 'Valued Stock Report'
- [EE-728](https://github.com/etendosoftware/com.etendoerp.localization.spain.extensions/issues/8){target="\_blank"} Se agregó la traducción faltante para la ventana 'Pending Goods Receipts'
- [EE-736](https://github.com/etendosoftware/com.etendoerp.localization.spain.extensions/issues/7){target="\_blank"} Se corrigió la validación 'Acogida al SII' de la configuración SII
### 1.5.1
- [EE-730](https://github.com/etendosoftware/com.etendoerp.localization.spain.extensions/issues/5){target="\_blank"} Se corrigió una traducción errónea en un campo de la ventana 'Producto'
- [EE-729](https://github.com/etendosoftware/com.etendoerp.localization.spain.extensions/issues/4){target="\_blank"} Se añadió una traducción faltante para las opciones que aparecen al hacer click derecho sobre las columnas de una ventana
- [EE-725](https://github.com/etendosoftware/com.etendoerp.localization.spain.extensions/issues/3){target="\_blank"} Se añadió una traducción faltante para la ventana 'Marca'
### 1.5.0
- Se actualizó la compatibilidad de Core incluyendo hasta 23.3.x
### 1.4.1
- [EE-720](https://github.com/etendosoftware/com.etendoerp.localization.spain.extensions/issues/2){target="\_blank"} Se renombró a minúsculas el java package del modulo `org.openbravo.localization.spain.referencedata.translation.eses` 
### 1.4.0
- Se actualizó la compatibilidad de Core incluyendo hasta 23.2.x
### 1.3.0
- Se publicaron todos los paquetes en GitHub
### 1.2.1
- Se resolvió problemas funcionales de la localización española utilizando las dependencias en formato JAR.

### 1.2.0
- Se añadieron nuevos rangos de impuestos:
	Adquisiciones IVA 0%
  Adquisiciones IVA 0+RE 0+0%
  Adquisiciones IVA+RE 21+1.75%
  Adquisiciones IVA+RE 5+0.62%
  Adquisiciones intracomunitarias 5%
  Entregas IVA 0%
  Entregas IVA 0+RE 0+0%
  Entregas IVA 5%
  Entregas IVA+RE 21+1.75%
  Entregas IVA+RE 5+0.62% 
  Servicios prestados 0%
  
  (**)Al tratarse de impuestos temporales, el campo "válido desde" tiene indicada la fecha "01-01-9999". Para que estos nuevos rangos puedan ser utilizados tendrá que editarse la misma y poner una fecha real (Ej. 01-01-2023).
  
- Se incluyen los parámetros del modelo 303 y modelo 349 a los nuevos rangos temporales.

- Se actualiza el modelo 303, en función del nuevo diseño de registro publicado por la [AEAT](https://sede.agenciatributaria.gob.es/Sede/ayuda/disenos-registro/modelos-300-399.html)

- Actualización del módulo "epígrafes"

### 1.1.0
- Se actualizó la compatibilidad de Core desde 22.4.3 a 22.4.x
- Se añadió la dependencia de la traducción del módulo de Default Jobs

### 1.0.5
- Se actualizó la compatibilidad de Core a 22.4.x
- Se eliminó la dependencia de Cash VAT Management
- Se eliminó la dependencia del modulo JAX-WS-JAVA API

### 1.0.4
- Se eliminaron los módulos de Facturacion Electrónica
- Se añadió la traducción de Libro de Facturas 


### 1.0.2

Version actualizada para ser compatible con Etendo 22Q2

### 1.0.1

##### Errores Solucionados

EE-171 -  SII versión 1.9.213100 - Se envían incorrectamente las facturas con NOI

**org.openbravo.module.sii**

En facturas proveedor con proveedores extranjeros (NOI) se estaba cortando a 9 caracteres el taxid lo que provocaba que se enviasen mal al SII las facturas y que luego Etendo diese error "Factura no encontrada".

##### EE-115 - **Intrastat “Null Pointer Exception” cuando el campo TaxId es vacío**

**org.openbravo.module.intrastat**

Al intentar generar el archivo Intrastat, si uno de los terceros incluidos en el fichero no tenía información en el campo TaxId, se mostraba un error “null pointer exception” y el archivo no se generaba.  
Ahora se visualizará un mensaje de error con el siguiente texto:

-   En Inglés: *“The value of the Tax ID field is empty for the business partner with Search Key ...”*
-   En Castellano: *"El valor del campo CIF/NIF se encuentra vacío para el tercero con Identificador ..."*

