---
title: Categoría del producto
tags:
  - Master Data Management
  - Etendo Classic
  - Product
  - Product Category
---

## Categoría del producto { #product-category }

:material-menu: `Aplicación` > `Gestión de Datos Maestros` > `Configuración de productos` > `Categoría del producto`

### Visión general { #overview }

Los productos similares pueden agruparse en diferentes categorías, que deben crearse con el objetivo de ayudar a su gestión y análisis.

Puede que desee agrupar productos similares dentro de la misma categoría para obtener información de aprovisionamiento y ventas resumida por cada categoría. Esto es posible debido a que el "Grupo de productos" es una de las "Dimensiones" de los informes de compras y ventas.

Para obtener más información, visite Herramientas de análisis de aprovisionamiento y Herramientas de análisis de ventas.

Además, cada categoría del producto permite al usuario configurar un conjunto diferente de cuentas contables que se utilizarán al contabilizar transacciones relacionadas con el producto, como facturas de compra y de venta.

### Categoría del producto { #product-category_1 }

La ventana Categoría del producto permite al usuario crear y configurar cada grupo de productos que su empresa pueda necesitar.

![](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/product-setup/product-category/product-category-1.png)

Tal y como se muestra en la imagen anterior, la creación de una categoría del producto requiere introducir la siguiente información para cada categoría:

- un **Identificador** o nombre corto que ayuda a encontrar fácilmente la categoría
- un **Nombre**
- una **Descripción**
- y el indicador **Nivel agrupación**, que ayuda a organizar las categorías del producto en una estructura jerárquica.

Las categorías del producto pueden organizarse en una estructura jerárquica, que posteriormente puede ser explotada por otros informes o procesos. Para obtener más información sobre cómo trabajar con árboles, visite la sección Estructura de árbol.

### Contabilidad { #accounting }

Cada categoría del producto permite al usuario configurar un conjunto diferente de cuentas contables.

![](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/product-setup/product-category/product-category-2.png)

Existe un conjunto de cuentas relacionadas con el producto que debe configurarse correctamente para la configuración del libro mayor de la organización.

El proceso "Copiar cuentas" de la solapa Valores predeterminados de la pantalla Configuración del libro mayor permite completar automáticamente al menos las obligatorias que se muestran en la imagen anterior.

Las cuentas establecidas automáticamente por Etendo siempre pueden modificarse si es necesario.

La lista completa de cuentas relacionadas con el producto es:

- **Inmovilizado del producto**: este campo almacena la cuenta predeterminada que se utilizará para registrar transacciones de inventario tales como:
  - Recuentos de inventario
  - Movimientos de inventario
  - y Recepción de mercancías

Esta cuenta suele ser una cuenta de activo.

- **Gastos del producto**: este campo almacena la cuenta predeterminada que se utilizará para registrar los gastos de compra del producto.  
  Esta cuenta suele ser una cuenta de gastos.
- **Gasto de producto a periodificar**: este campo almacena la cuenta predeterminada que se utilizará para registrar gastos diferidos.  
  Esta cuenta suele ser una cuenta de activo.
- **Ingresos por el producto**: este campo almacena la cuenta predeterminada que se utilizará para registrar los ingresos por ventas del producto.  
  Esta cuenta suele ser una cuenta de ingresos.
- **Ingreso de producto a periodificar**: este campo almacena la cuenta predeterminada que se utilizará para registrar ingresos diferidos.  
  Esta cuenta suele ser una cuenta de pasivo.
- **Costo del producto**: este campo almacena la cuenta predeterminada que se utilizará para registrar el coste de los bienes vendidos.  
  Esta cuenta suele ser una cuenta de gastos.
- **Devolución de Ingresos por el Producto**: este campo almacena la cuenta predeterminada que se utilizará para registrar devoluciones de ventas.  
  Esta cuenta suele ser una cuenta de ingresos.
- **Devolución del Costo del Producto**: este campo almacena la cuenta predeterminada que se utilizará para registrar recepciones de material devuelto.  
  Esta cuenta suele ser una cuenta de gastos.
- **Desviación pr. factura**: este campo almacena la cuenta predeterminada que se utilizará para registrar diferencias de precio entre recepciones de mercancías contabilizadas y facturas de compra registradas.  
  Esta cuenta suele ser una cuenta de activo.

!!! info
    El botón de acción "Copiar cuentas" permite al usuario copiar las cuentas predeterminadas en esta ventana a la solapa Contabilidad del producto.

### Productos asignados { #assigned-products }

Productos asignados es una vista de todos los productos que pertenecen a una categoría del producto.

Como nota adicional, los productos no reales, como los productos de descuento, deberían pertenecer a un grupo de productos específico, denominado por ejemplo "Otros", como forma de mantenerlos aislados de los reales.

Para obtener más información sobre los productos de descuento, visite Descuento.

### Traducción { #translation }

Mantiene traducciones de las categorías del producto a diferentes idiomas.

---

Este trabajo es una obra derivada de [Gestión de Datos Maestros](https://wiki.openbravo.com/wiki/Master_Data_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.
