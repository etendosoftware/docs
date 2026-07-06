---
title: Rappels
tags:
  - Master Data Management
  - Etendo Classic
  - Business Partner
  - Discount
---

## Rappels { #volume-discount }

:material-menu: `Aplicación` > `Gestión de Datos Maestros` > `Configuración de terceros` > `Rappels`

### Visión general { #overview }

Los rappels son descuentos que se aplican tras alcanzar un determinado volumen de ventas de productos específicos o de grupos de productos.

Los rappels son incentivos destinados a fomentar la compra de bienes en mayores cantidades. Este incentivo se ofrece normalmente para trasladar parte de las eficiencias económicas obtenidas mediante pedidos más grandes, mejorar las relaciones con los clientes e incrementar el volumen total de ventas.

### Rappels { #volume-discounts }

La ventana **Rappels** permite al usuario crear y configurar correctamente los rappels relacionados con productos específicos y/o grupos de productos, que posteriormente se asignan a los terceros seleccionados.

![](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/business-partner-setup/volume-discount/volume-discount-1.png)

Tal y como se muestra en la imagen anterior, se puede crear un rappel introduciendo únicamente los siguientes datos en la ventana de cabecera "Rappel":

- el "**Nombre**" del rappel
- la "**Moneda**"
- el "**Modo selección de producto**" al que se aplicará el rappel. Las opciones disponibles son:
  - Solo los definidos - lo que significa que se aplica a todos los productos definidos en la solapa "Producto" inferior.
  - o Todos excepto los definidos - lo que significa que se aplica a todos los productos excepto a los definidos en la solapa "Producto" inferior.
- el "**Modo selección Categoría de producto**" al que se aplicará el rappel. Las opciones disponibles son:
  - Solo los definidos - lo que significa que se aplica a todas las categorías de producto definidas en la solapa "Categoría del producto" inferior.
  - o Todos excepto los definidos - lo que significa que se aplica a todos los grupos de productos excepto a los definidos en la solapa "Categoría del producto" inferior.
- **Escalado** - Un rappel puede ser escalado, lo que significa que es posible definir un conjunto de rangos de importes con un descuento diferente. Para obtener más información, consulte la solapa "Escala" inferior.

### Categoría del producto { #product-category }

Un rappel puede configurarse para un conjunto de categorías de producto o puede configurarse para todas las categorías de producto excepto para un conjunto de ellas.

Por lo tanto, y en función del criterio adoptado, aquí puede seleccionar las categorías de producto para incluirlas o excluirlas de un rappel determinado.

### Producto { #product }

Un rappel puede configurarse para un conjunto de productos o puede configurarse para todos los productos excepto para un conjunto de ellos.

Por lo tanto, y en función del criterio adoptado, aquí puede seleccionar los productos para incluirlos o excluirlos de un rappel determinado.

### Escala { #volume-discount-parameters }

Los parámetros de un rappel son un % de descuento, así como el importe mínimo hasta el cual se aplica dicho % de descuento.

Además, también es posible configurar no solo un importe mínimo a partir del cual se aplicará un % de descuento determinado, sino un conjunto de rangos de importes a los que se aplicará un % de descuento diferente.

Por ejemplo, podría configurar un rappel que se aplique:

- un 2% al rango de importes =0,00 a 9.999,99
- un 5% al rango de importes = 10.000,00 a 24.999,99
- y un 10% a un importe mínimo a partir de 25.000,00

### Terceros { #business-partners }

Los rappels pueden asignarse a terceros seleccionados dentro de un periodo de tiempo determinado.

También puede hacer que un rappel se aplique a un tercero seleccionado a partir de una determinada "Fecha de validez desde".

Aunque el rappel tiene más sentido para la "Operación de venta", también es posible crear y configurar rappels para que se apliquen a proveedores seleccionados mediante:

- desmarcar el indicador "Operación de venta"
- y eliminar el filtro "Cliente" al seleccionar terceros en el selector de terceros.
