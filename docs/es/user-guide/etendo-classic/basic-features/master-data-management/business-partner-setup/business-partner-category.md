---
title: Grupos de Terceros
tags:
  - Master Data Management
  - Etendo Classic
  - Business Partner
  - Accounting
---

## Visión general { #overview }

Los terceros pueden agruparse en diferentes categorías con el objetivo de facilitar su gestión y análisis.

Puede que desee agrupar los proveedores de un determinado tipo de productos dentro de la misma categoría, para poder comparar los precios de compra que su empresa obtuvo de ellos en relación con el mismo tipo de productos.

O puede que desee agrupar los clientes ubicados en su país dentro de la misma categoría, distinta de la que agrupa a los clientes ubicados en el extranjero, para poder comparar las cifras de ventas nacionales y extranjeras.

Todo lo anterior es posible debido a que el Grupo de Terceros es una dimensión de los informes de compras y ventas.

Para obtener más información, visite las herramientas de análisis de aprovisionamiento y las herramientas de análisis de ventas.

Por último, también es importante que tenga en cuenta que cada grupo de terceros permite al usuario configurar un conjunto diferente de cuentas contables del libro mayor que se utilizarán al contabilizar transacciones como las cuentas a cobrar de clientes o las deudas con proveedores.

## Grupos de Terceros { #business-partner-category }

:material-menu: `Aplicación` > `Gestión de Datos Maestros` > `Configuración de terceros` > `Grupos de Terceros`

La ventana **Grupos de Terceros** permite al usuario crear y configurar cada grupo de terceros que su organización pueda necesitar.

![](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/business-partner-setup/business-partner-category/business-partner-category-1.png)

Tal y como se muestra en la imagen anterior, la creación de un grupo de terceros requiere introducir la siguiente información para cada grupo:

- una clave de búsqueda o nombre corto que ayude a encontrar fácilmente un grupo
- un **Nombre**
- y una **Descripción**

### Contabilidad { #accounting }

Cada grupo de terceros permite al usuario configurar un conjunto diferente de cuentas contables.

![](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/business-partner-setup/business-partner-category/business-partner-category-2.png)

Existen varias cuentas relacionadas con terceros que deben configurarse correctamente para la configuración del libro mayor de la organización.

El proceso **Copiar cuentas** de la solapa **Valores por defecto** de la pantalla de configuración del libro mayor permite al usuario completar automáticamente, al menos, las obligatorias que se muestran en la imagen anterior.

Las cuentas establecidas automáticamente por Etendo siempre pueden modificarse si fuese necesario.

Estas cuentas contables son las que se utilizarán al contabilizar transacciones relacionadas con terceros, tales como:

- Cuentas a cobrar de clientes, contabilización de facturas de venta.  
  Para obtener más información, visite Sales Invoice
- Anticipos de clientes, contabilización de cobros de clientes por adelantado.  
  Para obtener más información, visite Payment In
- Deudas con proveedores, contabilización de facturas de compra.  
  Para obtener más información, visite Purchase Invoice
- Anticipos a proveedores, contabilización de pagos a proveedores por adelantado.  
  Para obtener más información, visite Payment Out
- Recepciones de mercancía no facturadas, contabilización de recepción de mercancía.  
  Para obtener más información, visite Goods Receipt
- Importes de ajuste, o importes que su empresa esperaba cobrar de un cliente y que ya no se van a cobrar.  
  Para obtener más información, visite Payment In
- Importes de ajuste de ingresos, o importes que su empresa debía pagar a un proveedor y que ya no se van a pagar.  
  Para obtener más información, visite Payment Out
- Cuenta de deudas dudosas, contabilización de deudas dudosas.  
  Para obtener más información, visite Doubtful Debt Run
- Cuenta de gasto por incobrables, importe de gasto clasificado como incobrable.  
  Para obtener más información, visite Doubtful Debt Run
- Cuenta de ingresos por incobrables, importe de ingreso clasificado como incobrable.  
  Para obtener más información, visite Doubtful Debt Run
- Cuenta de provisión para deudas dudosas, importe utilizado para provisionar frente a posibles incobrables.  
  Para obtener más información, visite Doubtful Debt Run

El botón de acción **Copiar cuentas** permite al usuario copiar las cuentas establecidas por defecto en esta ventana a:

- la solapa **Contabilidad de cliente**
- o la solapa **Contabilidad de proveedor**
