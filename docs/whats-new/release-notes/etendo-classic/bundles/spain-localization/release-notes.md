---
title: Versiones Disponibles
---
## Introducción

En esta página se documentarán las versiones disponibles del paquete `com.etendoerp.localization.spain.extensions`

## Versiones Disponibles

| Versión | Fecha de Publicación | Desde Core | Hasta Core | Estado | GitHub|
| :--- | :--- | :--- | :--- | :---: | :---: |
| 1.4.1 | 19/09/2023 | 22.4.3 | 23.2.x | CS | :white_check_mark:|
| 1.4.0 | 27/06/2023 | 22.4.3 | 23.2.x | C  | :white_check_mark:|
| 1.3.0 | 24/05/2023 | 22.4.3 | 23.1.5 | C  | :white_check_mark:|
| 1.2.1 | 26/04/2023 | 22.4.3 | 22.4.5 | C  |                   |
| 1.2.0 | 03/03/2023 | 22.4.3 | 22.4.5 | C  |                   |
| 1.1.0 | 03/02/2023 | 22.4.3 | 22.4.5 | C  |                   |
| 1.0.5 | 12/01/2023 | 21.4.0 | 22.4.5 | C  |                   |
| 1.0.4 | 07/12/2022 | 21.4.0 | 22.3.0 | C  |                   |
| 1.0.3 | 06/10/2022 | 21.4.0 | 22.3.x | C  |                   |
| 1.0.2 | 11/07/2022 | 21.4.0 | 22.2.2 | C  |                   |
| 1.0.1 | 16/06/2022 | 21.4.0 | \*     | C  |                   |
| 1.0.0 | 01/01/2022 | 21.4.0 | \*     | C  |                   |


## Notas
### Version 1.4.1
- [EE-720](https://github.com/etendosoftware/com.etendoerp.localization.spain.extensions/issues/2){target="\_blank"} Se renombró a minúsculas el java package del modulo `org.openbravo.localization.spain.referencedata.translation.eses` 
### Version 1.4.0
- Se actualizó la compatibilidad de Core incluyendo hasta 23.2.x
### Versión 1.3.0
- Se publicaron todos los paquetes en GitHub
### Versión 1.2.1
- Se resolvió problemas funcionales de la localización española utilizando las dependencias en formato JAR.

### Versión 1.2.0
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

### Versión 1.1.0
- Se actualizó la compatibilidad de Core desde 22.4.3 a 22.4.x
- Se añadió la dependencia de la traducción del módulo de Default Jobs

### Version 1.0.5
- Se actualizó la compatibilidad de Core a 22.4.x
- Se eliminó la dependencia de Cash VAT Management
- Se eliminó la dependencia del modulo JAX-WS-JAVA API

### Version 1.0.4
- Se eliminaron los módulos de Facturacion Electrónica
- Se añadió la traducción de Libro de Facturas 


### Versión 1.0.2

Version actualizada para ser compatible con Etendo 22Q2

### Versión 1.0.1

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

