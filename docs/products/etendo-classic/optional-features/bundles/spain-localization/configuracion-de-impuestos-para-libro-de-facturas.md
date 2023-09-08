---
title: Configuración de impuestos para libro de facturas
hide:
    - navigation
---
## Javapakages 
`org.openbravo.module.invoicesregisterbook.estaxes`

## **Introducción**

Esta sección contiene información sobre la configuración de impuestos de los libros de facturas que forman parte del bundle de Localización española de Etendo.

## **Instalación**

El usuario debe instalar este módulo y posteriormente aplicar el conjunto de datos o "Datos de Referencia" en la ruta de aplicación: Configuración General / Organización/ Gestión del Módulo de Empresa a la organización que corresponda.

![](/assets/drive/gGO4D4W1ZWtJV0sluU-2ESwmVQA8_vykqX_CABOqxU9WSAqeKQS42g46yOcZnVDpMG4qUHJO0XGnn1zvcHzKOVcgHMDFEXB3MwaBeyDOPZTwYEH1wdYWTPub9sLhcOcrko6PuYvIyNryJYZoi2dUxKIV9hFEXNlZ5DYtYyYTJ1663ViYtA-aKGEy9XXLYg.png)

Una vez instalado y aplicado este módulo, se puede comprobar la configuración de los libros en la ruta de aplicación: Gestión financiera/ Contabilidad/ Configuración/ Configuración de Libros de Facturas, tal y como se muestra en la siguiente imagen:

![](/assets/drive/jKTQzqVFoz7dxq2qJS-Q2ECPksUf8UxYrLmeKDGG4NFGeQSxG96b-vbxqpaQb71UWuFBFscdPLSXXjD6dIqHoBB-3mCoOypQBeADb8AONAYOjD5Lu-MGfk1njsbQMJ2C3Cp-V18LcZpTZIpJTBZQ4X9b2dEEj-9nzmnM3FceUIHW3hdlgfFtLRx_S-4hYg.png)

Es importante recalcar, que la configuración que se incluye en este dataset, relaciona tipos/rangos de impuesto con el tipo de documento estándar de Etendo (AP Invoice, AR Invoice, etc) a incluir en el correspondiente libro (facturas recibidas o facturas emitidas).

Si se crean nuevos tipos de documento de factura de compra o venta, tendrá que incluirse de forma manual en la configuración de cada libro, relacionados con los impuestos de compra o venta correspondientes.