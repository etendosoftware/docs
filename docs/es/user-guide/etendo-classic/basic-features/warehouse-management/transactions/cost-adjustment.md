---
title: Ajuste de Costes
tags:
 - Cost Adjustment
 - Warehouse Management
 - Average Cost
 - Transactions
---

# Ajuste de Costes { #cost-adjustment }

:material-menu: `Aplicación` > `Gestión de Almacén` > `Transacciones` > `Ajuste de Costes`

## Visión general { #overview }

La ventana **Ajuste de Costes** permite al usuario revisar los ajustes de costes de las transacciones de producto provocados por cambios en los precios de compra, la asignación de **Landed Cost** o correcciones manuales/de coste negativo.

Una vez que el coste de una **"Product Transaction"** ha sido calculado por el proceso de **Costing Background** y de acuerdo con lo configurado para el/los producto(s) en la **Regla de costes** correspondiente, no puede recalcularse ni eliminarse.

Sin embargo, y bajo determinadas circunstancias, el coste calculado de una transacción de producto necesitaría ajustarse; por ejemplo, el precio de compra de una transacción de compra cambia después de recibir el producto.

Si ese es el caso, el coste calculado de la recepción deberá ajustarse al nuevo precio de compra.

La funcionalidad de **Ajuste de Costes** se encarga de gestionar los ajustes creados sobre el coste de una transacción ya calculada.

Es importante remarcar que esta funcionalidad tiene en cuenta el **algoritmo de cálculo de costes** utilizado para calcular los costes; por lo tanto, se comporta de forma diferente en función de:

- Si el algoritmo de cálculo de costes utilizado es **"Average"**, el coste de una transacción cambia y, como consecuencia, cambia el coste del producto implicado.  
  En ese caso, se crea en esta ventana una transacción de ajuste de costes para reflejar ese cambio; dicha transacción de ajuste de costes puede contabilizarse en el libro mayor para que el valor de inventario del producto sea el mismo que su valor contable.
- Sin embargo, si el algoritmo de cálculo de costes utilizado es **"Standard"**, el coste de una transacción no puede cambiar ni ajustarse, del mismo modo que el coste **"Standard"** del producto implicado permanece igual.  
  En ese caso, no se creará ninguna transacción de ajuste de costes en esta ventana.

Como consecuencia de lo anterior, la ventana **Ajuste de Costes** gestiona los ajustes de costes creados para productos y, por tanto, para transacciones de producto valoradas con el algoritmo de coste **"Average"**.

Existen diferentes tipos de **"cost adjustments sources"** que conducen al coste **"average"** correcto de un producto.

Por ejemplo, transacciones de recepción que no se contabilizaron en el mismo orden en que ocurrieron, o transacciones de recepción a las que es necesario añadir **Landed Cost** a su coste ya calculado; todo ello impactará y, por tanto, requerirá que cambie el coste **"average"** del producto.

Es importante remarcar que:

- los ajustes de costes son acumulativos; por lo tanto, una transacción de producto puede tener más de un ajuste de cualquier tipo si es necesario para que el coste medio de esa transacción de producto sea el correcto.
- existen dos tipos de transacciones:
  - aquellas transacciones cuyos costes deben ajustarse como "**source**" del ajuste; por ejemplo, un albarán de proveedor cuyo coste debe ajustarse debido a un cambio del precio de compra
  - aquellas transacciones cuyos costes deben ajustarse "**not as source**", sino como consecuencia de ajustar las transacciones fuente; por ejemplo, un albarán de cliente cuyo coste debe ajustarse porque cambió el coste del albarán de proveedor correspondiente.

Lo anterior implica que, por ejemplo, una cabecera de ajuste de costes de **"Price Difference Correction"** puede tener dos líneas de ajuste: una marcada como **Fuente** = Yes y la otra marcada como **Fuente** = No.

- además, existen dos tipos de ajustes:
  - aquellos configurados como **"Unit Cost" = "Yes"**, lo que significa que el ajuste va a cambiar el **Coste Unitario** de la transacción que se está ajustando, además de su **Coste Total**.  
    Este es el caso de ajustes como **"Price Difference Correction"**, **"Backdated Transactions"** y **"Manual Cost Correction"** configurados como **unit cost**, ya que estos cambian el coste **"basic"** de una transacción.
  - aquellos configurados como **"Unit Cost" = "No"**, lo que significa que el ajuste no va a cambiar el **Coste Unitario** de la transacción que se está ajustando, sino únicamente su **Coste Total**.  
    Este es el caso de costes **"extra"** como **"Landed Cost"**, o ajustes realizados para gestionar el coste en escenarios de **"Negative Stock"**, o **"Manual Cost Correction"** no configurados como **unit cost**, sino como un coste **"extra"**.

Imaginemos un escenario en el que solo existe una transacción de recepción de 1 unidad de un producto, valorada a 10,00 €/unidad. En ese caso, los costes de la recepción son los siguientes, que pueden revisarse en la ventana **Producto**, solapa **Transacciones**:

- Trx Orginal Cost: 10,00
- Total Cost : 10,00
- Unit Cost : 10,00

Se contabiliza para la recepción una corrección manual de costes configurada como **"Unit Cost" = "Yes"** por un importe de 2,00 €. Esa corrección crea un ajuste de costes que cambia el coste de la recepción como se muestra a continuación:

- Trx Orginal Cost: 10,00
- Total Cost : 12,00 (10,00 + 2,00)
- Unit Cost : 12,00 (10,00 + 2,00)

Nuevo coste medio del producto = Coste Total / Stock = 12,00 € / 1 unidad = 12,00 €/unidad

Después de eso, el precio de compra cambia de 10,00 €/unidad a 12,00 €/unidad.

Ese cambio en el precio es un ajuste de coste unitario, que crea un ajuste de 0,00 € porque el coste unitario de la transacción ya es 12,00.

Esto implica que no hay cambio en el coste medio del producto; se mantiene en 12,00 €/unidad.

Sin embargo, imaginemos ahora que la corrección manual de costes contabilizada para la recepción por un importe de 2,00 € se configuró como **"Unit Cost" = No**; es decir, es un coste extra que también debe tenerse en cuenta. Esa corrección cambia el coste de la recepción como se muestra a continuación; el coste unitario no cambia:

- Trx Orginal Cost: 10,00
- Total Cost : 12,00 (10,00 + 2,00)
- Unit Cost : 10,00

Después de eso, el precio de compra cambia de 10,00 €/unidad a 12,00 €/unidad.

Ese cambio en el precio crea un ajuste de costes en la recepción de 2,00 = 12,00 - 10,00 €; por lo tanto, cambian los costes calculados de la recepción:

- Trx Orginal Cost: 10,00
- Total Cost : 14,00 (12,00 + 2,00)
- Unit Cost : 12,00 (10,00 + 2,00)

Ahora, este nuevo escenario implica un cambio en el coste medio a 14,00 €/unidad; este nuevo coste medio incluye un coste extra de 2,00 €/unidad.

Como se ha mencionado brevemente, Etendo admite diferentes fuentes de ajustes de costes con el objetivo de cubrir distintos escenarios reales. Esos diferentes tipos de fuentes de ajustes de costes se explican en la siguiente sección.

## Cabecera { #header }

Los documentos de ajuste de costes se crean automáticamente mediante el proceso **Costing Background** o el proceso **Price Correction Background**, según corresponda, en función del origen del ajuste.

Una vez creado automáticamente, puede revisarse en esta ventana.

![Ajuste de Costes](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/cost-adjustment/cost-adjustment-1.png)

Algunos campos relevantes a tener en cuenta son:

- **Tipo de documento**: este es el tipo de documento "Ajuste de Costes".
- **Fecha de Referencia**: esta es la fecha en la que se crea el ajuste de costes.
- **Proceso Fuente**: las opciones disponibles son:
    - Transacción retroactiva
    - Landed Cost
    - Corrección manual de costes
    - Corrección de stock negativo
    - Corrección de diferencia de precio

Todos ellos se explicarán en detalle en las siguientes secciones.

## Transacción retroactiva { #backdated-transaction }

El origen de este ajuste de costes es una transacción de producto (es decir, un **Albarán (Proveedor)**) que debería haberse contabilizado en una fecha anterior, pero no fue así.

Como consecuencia, el coste calculado de las transacciones fechadas con posterioridad a esa fecha anterior dada necesita ajustarse, al igual que el coste "Promedio" calculado del producto.

Este tipo de origen de ajuste de costes no aplica a productos valorados a coste "Estándar".

El coste "Estándar" de un producto permanece tal y como fue definido, porque el coste de un producto valorado a "Estándar" es siempre el mismo, independientemente de la fecha en la que se contabilice una transacción de ese producto.

En el caso de un producto valorado con el algoritmo de cálculo de costes "Promedio":

- Un **Albarán (Proveedor)** con fecha 06/01/2015 (**Fecha del movimiento**) se contabiliza con fecha 06/01/2015 (fecha de transacción). Una vez contabilizado, este **Albarán (Proveedor)** implica que el coste del producto (basado en el precio correspondiente de la **Línea de pedido de compra**) es 105,00 €/unidad.
- Un **Albarán (Cliente)** con fecha 07/01/2015 (**Fecha del movimiento**) también se contabiliza en Etendo con fecha 07/01/2015 (fecha de transacción). Una vez contabilizado, este **Albarán (Cliente)** implica que el coste del producto vendido es 105,00 €/unidad.
- Posteriormente, un **Albarán (Proveedor)** del mismo producto con fecha 02/01/2015 (**Fecha del movimiento**) se contabiliza en Etendo con fecha 07/01/2015 (fecha de transacción). Una vez contabilizado, este **Albarán (Proveedor)** implica que el coste del producto (basado en el precio correspondiente de la **Línea de pedido de compra**) es 100,00, a partir del 02/01/2015.
- Esta última entrega con **Fecha del movimiento** 02/01/2015 es el origen de un ajuste de costes por transacción retroactiva que ajusta el coste del producto vendido con fecha 07/01/2015 de 105,00 €/unidad a 102,50 €/unidad; además, el coste promedio calculado cambia de 105,00 a 102,50 a partir del 06/01/2015.

Las transacciones que deberían haberse contabilizado en una fecha anterior conllevan la creación de ajustes de costes de tipo "Transacción retroactiva".

!!! info
    Se crean automáticamente una cabecera y línea(s) en la ventana **Ajuste de Costes** con los ajustes correspondientes.

Este tipo de ajuste cambia el "Coste Unitario" de las transacciones del producto, así como el "Coste Total" y, por lo tanto, el coste "Promedio" del producto.

Los ajustes de costes por transacción retroactiva se crean:

- ejecutando el proceso "**Ajuste Retroactivo de Transacciones**" en las reglas de coste existentes
- o marcando la casilla "**Transacción Ajustada Retroactivamente**" al crear una nueva regla de coste.

De ambas formas, es posible introducir una fecha "Ajustar retroactivamente desde", que no debe formar parte de un período cerrado.

Una vez que el proceso **Ajuste Retroactivo de Transacciones** está habilitado en la regla de coste correspondiente, los ajustes de costes por transacción retroactiva se calculan automáticamente mediante el proceso **Costing background** cuando aplique.

## Contabilización de ajustes retroactivos { #backdated-adjustments-posting }

Un ajuste de costes retroactivo puede contabilizarse en el libro mayor en esta ventana.

En nuestro ejemplo anterior, la última entrega con **Fecha del movimiento** 02/01/2015 es la fuente de un ajuste de costes de transacción retroactivo que ajusta el coste del producto vendido de 105,00 €/unidad a 102,50 €/unidad.

Ese ajuste puede contabilizarse en el libro mayor. La contabilización se verá como se muestra a continuación:

|                      |                   |                   |
| -------------------- | ----------------- | ----------------- |
| Cuenta               | Débito            | Crédito           |
| _Inmovilizado del producto_      | Importe del Ajuste |                   |
| _Costo del producto_ |                   | Importe del Ajuste |

## Landed Cost

El origen de este ajuste de costes es la contabilización de costes adicionales que deben distribuirse y, por tanto, asignarse como costes adicionales del producto.

Los *landed cost* son costes como el transporte, el seguro, los aranceles aduaneros y otros costes necesarios para colocar el producto en el almacén de la organización.

Los ajustes de *landed cost* modifican el coste calculado de las transacciones de recepción cambiando su "Coste Total", del mismo modo que también cambia el coste "Promedio" del producto implicado.

El "Coste Unitario" de la transacción de recepción no cambia, ya que este tipo de ajuste no es un ajuste de coste unitario, sino un coste extra.

Este tipo de origen de ajuste de costes no aplica a productos valorados a coste "Estándar", en el sentido de que:

- siempre que se añada un *landed cost* a un producto valorado a coste estándar, no se crea ningún ajuste de costes, pero la "Desviación" entre el coste "estándar" definido para el producto y su coste "real" se contabiliza en una cuenta de "Desviación de Landed Cost", para que pueda analizarse posteriormente.

Por ejemplo:

- se contabiliza un pedido de compra que contiene un producto. Después, se contabilizan el albarán (proveedor) correspondiente y la factura de compra del producto, y se contabilizan en el libro mayor.
- posteriormente, se contabiliza una factura de compra que incluye costes adicionales como el coste de transporte y los cargos aduaneros, y se contabiliza en el libro mayor.
- la ventana Landed Cost permite asignar los costes de transporte y los cargos aduaneros al albarán (proveedor), *landed cost* que también se concilian con la factura ya contabilizada.

No es necesario ejecutar ningún proceso en segundo plano específico ni habilitar ninguna preferencia para obtener un ajuste de costes de "Landed Cost".

Los ajustes de costes de "Landed Cost" se crean tras procesar el documento de *landed cost* correspondiente en la ventana Landed Cost, o tras procesar la conciliación de *landed cost*.

!!! info
    Se crea automáticamente una cabecera y línea(s) en la ventana Ajuste de Costes de este tipo de ajuste de costes con el ajuste correspondiente.

Tal y como se ha mencionado, el ajuste de *landed cost* no cambia el "Coste Unitario" de las transacciones de un producto, sino su "Coste Total", del mismo modo que el coste "Promedio" del producto. Esto significa que:

- el coste unitario de cada transacción es el original (precio \* unidades)
- y el coste total de cada transacción incluye los ajustes necesarios para obtener el coste promedio deseado del producto.

## Contabilización de ajustes de Landed Cost { #landed-cost-adjustments-posting }

Los ajustes de Landed Cost pueden contabilizarse en el libro mayor en la ventana **Landed Cost**, siempre que dichos ajustes se hayan creado para productos incluidos en una transacción de **Albarán (Proveedor)**.

- En este caso, la transacción de **Albarán (Proveedor)** es la fuente del ajuste.

Además, los ajustes de Landed Cost también pueden crearse para productos incluidos en una transacción de **Albarán (Cliente)**.

- En este caso, la transacción de **Albarán (Cliente)** no es la fuente del ajuste, sino el **Albarán (Proveedor)**.
- En este caso, los ajustes de Landed Cost deben contabilizarse en la ventana **Ajuste de Costes**.

## Corrección manual de costes { #manual-cost-correction }

El origen de este ajuste de costes es un cambio manual del coste de una transacción de producto específica.

Este tipo de ajuste solo aplica a transacciones de producto valoradas a coste "Promedio". No tiene sentido cambiar manualmente el coste de una transacción valorada a coste "Estándar".

Por ejemplo:

- es necesario ajustar un movimiento entre almacenes, por lo que el coste de la transacción "Movimiento desde" se cambia (incrementa) manualmente por el usuario final
- el cambio anterior implica que el coste de la transacción "Movimiento a" también debe cambiarse (incrementarse), por lo que se crea el ajuste de costes correspondiente de tipo "Corrección manual de costes".

No es necesario ejecutar ningún proceso en segundo plano específico ni habilitar ninguna preferencia para obtener un ajuste de costes de tipo "Corrección manual de costes".

Los ajustes de costes de tipo "Corrección manual de costes" se crean después de cambiar el coste de una transacción de producto en la ventana Producto, solapa "Transacciones", utilizando el botón de proceso "Ajuste manual de costes".

Se crea automáticamente una cabecera y línea(s) en la ventana Ajuste de Costes de este tipo de ajuste de costes con el ajuste correspondiente.

Este tipo de ajuste cambia el "Coste Total" de la transacción de producto; sin embargo, el "Coste Unitario" de la transacción de producto puede cambiarse o no, dependiendo de lo que el usuario final desee obtener.

Hay una casilla de verificación llamada "**Coste Unitario**" que se muestra siempre que se seleccione la casilla de verificación "**Incremental**":

- Si el usuario no selecciona la casilla de verificación "**Incremental**", significa contabilizar un nuevo coste total de la transacción que permanecerá como "**Permanente**". Esto significa que ya no se modificará.
- Si el usuario selecciona la casilla de verificación "Incremental", significa contabilizar un coste adicional para asignar al coste total de la transacción. Además, este coste adicional puede formar parte del coste unitario (**casilla Coste Unitario = Sí**) de la transacción o no (**casilla Coste Unitario = No**). Este último caso significa un coste extra, como un landed cost.

**Contabilización del ajuste de Corrección manual de costes**

Este tipo de ajuste puede contabilizarse en el libro mayor en esta ventana.

En nuestro ejemplo anterior, el coste de la transacción "Movimiento desde" se cambia (incrementa) manualmente por el usuario final; por lo tanto, el coste de la transacción "Movimiento a" también debe cambiarse (incrementarse).

Ese ajuste puede contabilizarse en el libro mayor. La contabilización se verá como se muestra a continuación:

Ajuste de la transacción **"Movimiento desde"**:

|                                                                                                 |                                                  |                                                |
| ----------------------------------------------------------------------------------------------- | ------------------------------------------------ | ---------------------------------------------- |
| Cuenta                                                                                          | Débito                                           | Crédito                                        |
| [_Diferencias de almacén_](../../../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup/general-ledger-configuration.md#defaults-tab) | Importe del ajuste de la transacción "Movimiento desde" |                                                |
| [_Inmovilizado del producto_](../../../../../user-guide/etendo-classic/basic-features/master-data-management/master-data/product.md#accounting)                            |                                                  | Importe del ajuste de la transacción "Movimiento a" |

Ajuste de la transacción **"Movimiento a"**:

|                                                                                                 |                                                |                                                |
| ----------------------------------------------------------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| Cuenta                                                                                          | Débito                                         | Crédito                                        |
| [_Inmovilizado del producto_](../../../../../user-guide/etendo-classic/basic-features/master-data-management/master-data/product.md#accounting)                            | Importe del ajuste de la transacción "Movimiento a" |                                                |
| [_Diferencias de almacén_](../../../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup/general-ledger-configuration.md#defaults-tab) |                                                | Importe del ajuste de la transacción "Movimiento a" |

## Corrección de stock negativo { #negative-stock-correction }

El origen de este ajuste de costes es contabilizar una transacción, es decir, un albarán (cliente), que convierte el stock de un producto en una cantidad negativa. Este tipo de corrección solo está implementado para el cálculo de costes **"Promedio"**.

En el momento de contabilizar una nueva entrada de ese artículo, independientemente de si esa entrada convierte el stock del artículo en un valor positivo/negativo/cero, se crea un ajuste de corrección de coste negativo y se relaciona con esa nueva entrada, para conseguir que el stock restante de ese producto se valore al último precio de compra, en el caso del cálculo de coste **"Promedio"**.

Por ejemplo:

- se contabiliza un pedido de compra de 100 unidades a un precio de compra determinado
- después se recibe la mercancía y el coste de la mercancía se calcula en base al precio de compra del pedido
- a continuación se contabiliza un albarán (cliente) de 100 unidades
- y posteriormente se contabiliza otro albarán (cliente) de 5 unidades, lo que provoca un stock negativo del producto.

Se creará un ajuste de costes de corrección de stock negativo siempre que se contabilice una transacción de entrada del producto, como un albarán (proveedor). Ese ajuste se asignará al albarán (proveedor).

Este tipo de ajuste no cambia el **"Coste Unitario"** del albarán (proveedor), pero sí su **"Coste Total"**, del mismo modo que cambia el coste **"Promedio"** del producto implicado. Esto significa que:

- el coste unitario de cada transacción es el coste original (precio \* unidades)
- y el coste total de cada transacción incluye los ajustes necesarios para obtener el coste promedio deseado.

Hay dos acciones que debe realizar para obtener ajustes de costes de corrección de stock negativo:

- Configurar la preferencia **Permitir Correcciones de Stock Negativo** con Valor=Y en la ventana _Preferencias_
- Planificar el **proceso de Costing Background** en la ventana _Procesamiento de Peticiones_

## Contabilización del Ajuste de Corrección de Stock Negativo { #negative-stock-correction-adjustment-posting }

Este tipo de ajuste puede contabilizarse en el libro mayor en esta ventana.

En nuestro ejemplo anterior, se crea un ajuste de este tipo cada vez que se contabiliza una nueva transacción de entrada, como un albarán (proveedor), para el producto que tiene stock negativo.

Ese ajuste puede contabilizarse en el libro mayor. La contabilización se mostrará como se indica a continuación en el caso de un importe del ajuste negativo; en caso contrario, si el importe del ajuste es positivo:

|                                                                                                 |                   |                   |
| ----------------------------------------------------------------------------------------------- | ----------------- | ----------------- |
| Cuenta                                                                                          | Debe              | Haber             |
| [_Diferencias de almacén_](../../../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup/general-ledger-configuration.md#defaults-tab) | Importe del Ajuste |                   |
| [_Inmovilizado del producto_](../../../../../user-guide/etendo-classic/basic-features/master-data-management/master-data/product.md#accounting)                            |                   | Importe del Ajuste |

## Corrección de diferencia de precio { #price-difference-correction }

El origen de este ajuste de costes es un cambio en el precio de compra de un pedido o en el precio de compra de una factura después de recibir los bienes.

La Corrección de diferencia de precio se lanza únicamente para Transacciones de tipo _Entrega_. Otras transacciones, como devoluciones de material o transacciones de salida, no se tienen en cuenta, ya que no deberían modificar el coste "Promedio" debido a una corrección de precio.

Esos bienes se recibieron a un precio que ha cambiado; por lo tanto, el coste calculado de la entrega debe ajustarse, al igual que el coste calculado "Promedio" del producto.

El coste "Estándar" permanecería tal y como se estableció.

Por ejemplo:

- se contabiliza un pedido de compra para un producto a un precio de compra determinado
- después se recibe el producto y se calcula el coste "Promedio" del producto en base al precio de compra del pedido correspondiente.
- se contabiliza un albarán (cliente) de ese producto; por lo tanto, esa transacción de salida obtiene el coste "Promedio" calculado del producto.
- posteriormente se recibe y contabiliza una factura de compra para el producto a un precio superior al precio de compra del pedido
- es necesario crear un ajuste de costes de corrección de diferencia de precio para ajustar el Albarán (Proveedor) y, a continuación, afectar a la transacción de Albarán (Cliente) en base al nuevo coste Promedio calculado del producto.

Los cambios en el precio de compra conllevan la creación de ajustes de costes de "Corrección de diferencia de precio".

Se crea automáticamente una cabecera y línea(s) en la ventana **Ajuste de Costes** de este tipo de ajuste de costes con el ajuste correspondiente.

Este tipo de ajuste modifica el "Coste Unitario" y el "Coste Total" de las transacciones, al igual que el coste "Promedio" de los productos.

Los ajustes de corrección de "Diferencia de precio" pueden realizarse de forma automática o manual:

- para que Etendo realice automáticamente los ajustes de costes de corrección de diferencia de precio, es necesario activar y planificar el Proceso en segundo plano de corrección de precios
- para que el usuario pueda realizar manualmente los ajustes de costes de corrección de diferencia de precio, es necesario ejecutar manualmente el "Procesar ajuste de diferencia de precio"

Como se muestra en la imagen siguiente, este proceso permite seleccionar la Organización para la que debe ejecutarse, introducir una fecha de movimiento determinada y seleccionar un producto o conjunto de productos para los que deban crearse ajustes de costes de corrección de diferencia de precio.

![Ajuste de costes](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/cost-adjustment/cost-adjustment-2.png)

Adicionalmente, el Proceso en segundo plano de cálculo de costes también puede crear ajustes de costes de corrección de diferencia de precio, solo si:

- la preferencia de propiedad "Habilitar correcciones automáticas de diferencia de precio" está establecida en "Y"
- y el Proceso en segundo plano de cálculo de costes se ejecuta después de contabilizar el Pedido de compra, el Albarán (Proveedor) y la Factura de compra correspondientes, incluyendo la diferencia de precio.

## Contabilización del Ajuste de Corrección de Diferencia de Precio { #price-difference-correction-adjustment-posting }

Este tipo de ajuste puede contabilizarse en el libro mayor en esta ventana.

En nuestro ejemplo anterior, un cambio en el precio del pedido de compra (incremento) implica que tanto el coste calculado del "**Albarán (Proveedor)**" como el coste calculado del "**Albarán (Cliente)**" deben ajustarse, al igual que el coste "**medio**" del producto.

Ese ajuste puede contabilizarse en el libro mayor. La contabilización se verá como se muestra a continuación:

**Ajuste de Albarán (Proveedor)**

|                                                                                 |                                 |                                 |
| ------------------------------------------------------------------------------- | ------------------------------- | ------------------------------- |
| Cuenta                                                                           | Débito                          | Crédito                         |
| [_Product Asset_](../../../../../user-guide/etendo-classic/basic-features/master-data-management/master-data/product.md#accounting)            | Importe del ajuste de Albarán (Proveedor) |                                 |
| [_Invoice Price Difference_](../../../../../user-guide/etendo-classic/basic-features/master-data-management/master-data/product.md#accounting) |                                 | Importe del ajuste de Albarán (Proveedor) |

**Ajuste de Albarán (Cliente)**

|                                                                           |                                  |                                  |
| ------------------------------------------------------------------------- | -------------------------------- | -------------------------------- |
| Cuenta                                                                     | Débito                            | Crédito                           |
| [_Cost of Goods Sold_](../../../../../user-guide/etendo-classic/basic-features/master-data-management/master-data/product.md#accounting) | Importe del ajuste de Albarán (Cliente) |                                  |
| [_Product Asset_](../../../../../user-guide/etendo-classic/basic-features/master-data-management/master-data/product.md#accounting)      |                                  | Importe del ajuste de Albarán (Cliente) |

### Línea { #line }

Un documento de ajuste de costes puede tener tantas líneas de ajuste como productos incluidos en las recepciones a las que se hayan asignado costes adicionales.

Existen dos tipos de transacciones de ajustes de costes:

- "**fuente**", por ejemplo una recepción de proveedor (V+) cuyo precio de compra ha cambiado
- "**no fuente**", por ejemplo un envío a cliente (C-) cuyo coste debe ajustarse debido a que se está ajustando el coste de la recepción del proveedor.

![Ajuste de costes](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/cost-adjustment/cost-adjustment-3.png)

Algunos campos relevantes a tener en cuenta son:

- **Operaciones de almacén**: las transacciones disponibles son:
    - Recepción de proveedor (V+)
    - Envío a cliente (C-)
    - Entrada de inventario (I+)
    - Salida de inventario (I-)
    - Movimiento desde (M-)
    - Movimiento hacia (M+)
    - Producción (P+)
    - Producción (P-)
    - Consumo interno (D-)
    - Consumo interno (D+)
- **Importe del Ajuste**: es el importe del ajuste de costes.  
  Un importe de ajuste también puede revisarse en la ventana **Producto**, en la solapa "**Transacción**", solapa "**Coste de la transacción**", siempre relacionado con una "**Línea de Ajuste de Coste**".
- **Fuente**: las opciones disponibles son "Sí" o "No", ya que una transacción de producto puede ser la fuente de un ajuste o no.
- **Línea de Ajuste de Costes Padre**: en el caso de un ajuste de costes que no es la fuente, este campo muestra la línea de ajuste de costes fuente.
- **Necesita contabilización**: las opciones disponibles son "Sí" o "No". La mayoría de los ajustes de costes deben contabilizarse en el libro mayor, ya que implican un incremento/disminución del valor del inmovilizado del producto; sin embargo, existen otros cuyo ajuste de costes es 0,00 y no requieren contabilización.
- **Coste Unitario**: las opciones disponibles son "Sí" o "No".
  - Existen ajustes de costes como la corrección de diferencia de precio que impactan en el coste unitario del producto.
  - Existen ajustes de costes como el coste adicional que no impactan en el coste unitario del producto.  
    Es importante remarcar que cada **Transacción de producto** tiene los costes que se listan a continuación:
    - "**Coste Original Trx**", que es el coste original de la transacción de producto
    - "**Coste Total**", que es la suma del coste original y todos los costes de ajuste
    - "**Coste Unitario**", que es la suma del coste original y todos los ajustes del coste unitario; es decir, el coste que no incluye el coste adicional.
- **Transacción Retroactiva**: un ajuste de costes puede marcarse como transacción retroactiva si aplica.  
  Por ejemplo, un ajuste de costes de una transacción retroactiva puede tener dos líneas: una que es la transacción retroactiva como fuente y otra que no es la fuente ni una transacción retroactiva.
- **Permitir Correcciones de Stock Negativo**: un ajuste de costes puede marcarse como corrección de stock negativo si aplica.  
  Por ejemplo, un ajuste de costes de una transacción retroactiva puede tener dos líneas: una que es la transacción retroactiva como fuente y otra que no es la fuente, pero sí una corrección de stock negativo.

### Contabilidad { #accounting }

Esta solapa proporciona información contable del **Ajuste de Costes**.

![Ajuste de costes](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/cost-adjustment/cost-adjustment-4.png)

Los asientos mostrados en esta solapa son diferentes en función de la fuente del ajuste, pero la contabilización de coste adicional se gestiona en la ventana **Landed Cost**.

Las líneas de ajuste de coste adicional siempre se crean como "Necesita contabilización" = No.

A continuación se muestran algunos ejemplos de cada tipo de ajuste de costes:

**Corrección de precio**: ajuste de costes causado por una disminución del precio de compra

|                        |                        |                        |
| ---------------------- | ---------------------- | ---------------------- |
| Cuenta                 | Débito                 | Crédito                |
| Desviación pr. factura | Importe del ajuste de costes |                        |
| Inmovilizado del producto |                        | Importe del ajuste de costes |

**Corrección de precio**: ajuste de costes causado por un incremento del precio de compra

|                        |                        |                        |
| ---------------------- | ---------------------- | ---------------------- |
| Cuenta                 | Débito                 | Crédito                |
| Inmovilizado del producto | Importe del ajuste de costes |                        |
| Desviación pr. factura |                        | Importe del ajuste de costes |

**Transacciones retroactivas**: ajuste sobre una transacción de albarán de recepción del producto.

El coste del producto se reduce.

|                       |                        |                        |
| --------------------- | ---------------------- | ---------------------- |
| Cuenta                | Débito                 | Crédito                |
| Diferencias de almacén | Importe del ajuste de costes |                        |
| Inmovilizado del producto |                        | Importe del ajuste de costes |

**Transacciones retroactivas**: ajuste sobre una transacción de albarán de envío del producto.

El coste del producto se reduce.

|               |                        |                        |
| ------------- | ---------------------- | ---------------------- |
| Cuenta        | Débito                 | Crédito                |
| Costo del producto | Importe del ajuste de costes |                        |
| Inmovilizado del producto |                        | Importe del ajuste de costes |

**Corrección negativa**: ajuste que implica un incremento del coste del producto.

|                       |                        |                        |
| --------------------- | ---------------------- | ---------------------- |
| Cuenta                | Débito                 | Crédito                |
| Inmovilizado del producto | Importe del ajuste de costes |                        |
| Diferencias de almacén |                        | Importe del ajuste de costes |

**Corrección manual de costes**: ajuste causado por un incremento manual del coste del producto.

|                       |                        |                        |
| --------------------- | ---------------------- | ---------------------- |
| Cuenta                | Débito                 | Crédito                |
| Inmovilizado del producto | Importe del ajuste de costes |                        |
| Diferencias de almacén |                        | Importe del ajuste de costes |

## Contabilización masiva { #bulk-posting }

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}.

La funcionalidad de **contabilización masiva** permite al usuario contabilizar o descontabilizar múltiples registros seleccionando los registros correspondientes y haciendo clic en el botón **Contabilización masiva**.

Además, el Estado contable del/de los registro/s se muestra en la barra de estado, en la vista de formulario, o en una columna, en la vista de cuadrícula.

!!! info
    Para más información, visite [la guía de usuario del módulo Bulk Posting](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).
