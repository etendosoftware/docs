---
title: Inventario Referenciado
tags:
 - Referenced Inventory
 - Warehouse Management
 - Box
 - Transactions
---

# Inventario Referenciado { #referenced-inventory }

:material-menu: `Aplicación` > `Gestión de Almacén` > `Transacciones` > `Inventario Referenciado`

## Visión general { #overview }

En esta ventana, es posible definir los contenedores o cajas, lo cual incluye cualquier tipo de objeto que pueda contener mercancías.

Muchas empresas mueven y almacenan mercancías agrupadas en un RollTainer, caja o contenedor. Las cajas pueden ser reutilizables o desechables y tienen diferentes tamaños y propósitos, siendo adecuadas para distintos tipos de mercancías.

El Inventario Referenciado es la funcionalidad que identifica uno o varios detalles de almacenamiento (registros de stock) mediante un "Número de referencia".

El Inventario Referenciado para Core incluye la funcionalidad más básica para Empaquetar/Desempaquetar stock.

## Inventario Referenciado { #referenced-inventory_tab }

Esta solapa muestra cualquier inventario referenciado, también conocido como caja, declarado en el sistema independientemente de si está vacío o tiene stock en su interior.

El usuario puede crear nuevas cajas en cualquier momento. Es obligatorio definir una organización, clave de búsqueda y el tipo de inventario referenciado.

Es importante destacar que:

1. No será posible eliminar un registro si el inventario referenciado está vinculado a alguna transacción de Empaquetar/Desempaquetar.
2. La clave de búsqueda es única por cliente. Para evitar esta limitación, puede declarar un prefijo/sufijo diferente en la secuencia del tipo de inventario referenciado.
3. La organización limita el stock que puede empaquetarse (solo el stock declarado en esta organización o en cualquier organización hija).

Desde esta ventana es posible vincular/desvincular stock a/desde un Inventario Referenciado usando los botones Empaquetar y Desempaquetar respectivamente.

## Empaquetar { #box }

Muestra un P&E con el stock aún no vinculado a ningún inventario referenciado (no es posible empaquetar un stock ya empaquetado).

![Empaquetar](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/referenced-inventory/referenced-inventory-1.png)

El usuario puede seleccionar uno o varios registros y especificar la cantidad a empaquetar. También es obligatorio declarar el campo **Movido a** donde se almacenará el stock empaquetado.

Si el hueco actual de cualquiera de los registros seleccionados es diferente de **Movido a**, el sistema realizará automáticamente un Movimiento entre almacenes al confirmar la acción para mover el stock.

La acción de empaquetado puede ejecutarse en diferentes lotes en cualquier momento; es decir, el usuario puede seleccionar cualquier inventario referenciado no vacío para añadir más stock.

!!! info
    Un Inventario Referenciado específico solo puede estar presente en un único hueco, no en varios huecos al mismo tiempo. En caso de que quiera añadir más stock a una caja no vacía, el selector **Movido a** solicitará al usuario que seleccione el hueco actual del inventario referenciado.

Cuando un stock se empaqueta, la clave de búsqueda del inventario referenciado se añadirá automáticamente al final del **Valor atributos** entre corchetes **\[\]** (representación gráfica de una caja). Ejemplo: L582\[1000584\]

Si el stock no tiene atributo, el inventario referenciado se mostrará igualmente en el campo **Valor atributos** para indicar que el stock está actualmente empaquetado. Ejemplo: \[1000584\]

De este modo, la información sobre el inventario referenciado es claramente visible en cualquier lugar donde sea necesario, como el Informe de stock.

## Desempaquetar { #unbox }

Muestra un P&E con el stock actualmente vinculado al inventario referenciado seleccionado.

![Desempaquetar](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/referenced-inventory/referenced-inventory-2.png)

El usuario puede seleccionar uno o varios registros y especificar la cantidad a desempaquetar (por lo que es posible ejecutar un desempaquetado parcial) y el nuevo hueco donde se almacenará el stock tras desempaquetarlo (por defecto se desempaquetará en la ubicación actual).

!!! note
    A diferencia del proceso de empaquetado explicado anteriormente, en el desempaquetado se pueden seleccionar distintos huecos para cada registro.

## Comportamiento de gestión de reservas { #reservation-management-behavior }

Al ejecutar un proceso de Empaquetar/Desempaquetar, el sistema siempre intentará trabajar primero con cantidades no reservadas. Ejemplo: si tenemos 10 unidades disponibles de un producto, de las cuales 2 están reservadas, e intentamos empaquetar/desempaquetar 1 unidad, el sistema intentará empaquetar/desempaquetar primero cualquiera de las 8 unidades no reservadas.

Si el proceso de Empaquetar/Desempaquetar necesita trabajar con cantidades ya reservadas (en el ejemplo anterior, porque estamos empaquetando/desempaquetando 9 o 10 unidades), el sistema intentará reasignar al vuelo cualquier reserva o mostrará un error cuando la reasignación no sea posible. Esto último puede ocurrir, por ejemplo, porque la reserva está forzada a un hueco concreto y el proceso de Empaquetar/Desempaquetar intenta mover el stock a otro hueco.

## Contenido { #contents }

Stock actualmente vinculado a este Inventario Referenciado.

Tenga en cuenta que cualquier stock empaquetado tendrá un valor de atributos vinculado al inventario referenciado.

## Transacciones Empaquetado { #box-transactions }

Muestra cualquier transacción de empaquetado ejecutada en el pasado para este inventario referenciado.

Este tipo de transacciones son en realidad Movimientos entre almacenes creados al vuelo al confirmar el empaquetado, a los cuales el usuario puede acceder en cualquier momento para ver los detalles.

## Transacciones Desempaquetado { #unbox-transactions }

Muestra cualquier transacción de desempaquetado ejecutada en el pasado para este inventario referenciado.

Este tipo de transacciones son en realidad Movimientos entre almacenes creados al vuelo al confirmar el desempaquetado, a los cuales el usuario puede acceder en cualquier momento para ver los detalles.

---

Este trabajo es una obra derivada de [Gestión de Almacén](http://wiki.openbravo.com/wiki/Warehouse_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, usada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.