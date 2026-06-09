---
title: Inventario físico
tags:
 - Physical Inventory
 - Warehouse Management
 - Inventory Count
 - Transactions
---

# Inventario físico { #physical-inventory }

:material-menu: `Aplicación` > `Gestión de Almacén` > `Transacciones` > `Inventario físico`

La ventana **Inventario físico** permite al usuario ejecutar el proceso de conteo de mercancías en Etendo.

<iframe width="560" height="315" src="https://www.youtube.com/embed/xqE_UnYO6cM" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Cabecera { #header }

El proceso de conteo de mercancías requiere crear un conteo de inventario para comprobar o actualizar las cantidades de stock.

Estos son los pasos que deben seguirse para crear un conteo de inventario:

**1.** La sección **Cabecera** identifica el proceso de "Inventario físico" y lista sus parámetros principales.

![Cabecera](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/physical-inventory/physical-inventory-1.png)

Todos los campos se rellenan automáticamente cuando se crea un registro nuevo.

Algunos de los campos a tener en cuenta son:

- **Nombre:** este campo se utiliza para referenciar el movimiento físico no solo en los informes de almacén, sino también en el libro mayor; por lo tanto, es importante usar un nombre significativo.
- **Fecha del movimiento:** es la fecha en la que se crea el movimiento y, por defecto, es la fecha actual. Esta fecha también se utiliza en el registro de contabilización del documento de Inventario físico en el libro mayor, si aplica. Siempre puede modificarse, pero el usuario debe tener en cuenta que no es posible registrar inventarios físicos en el pasado (el **Proceso de Conteo de Inventario** siempre toma la fecha actual y no la Fecha del movimiento para actualizar el stock). La Fecha del movimiento debería ser la fecha actual, a menos que el usuario pueda garantizar que no se han procesado transacciones de almacén mientras tanto.
- **Almacén:** almacén en el que tiene lugar el inventario físico. Por defecto, toma el valor de la sesión desde el menú superior de navegación Preferencias de Usuario.

**2.** Hay 2 formas de **introducir líneas** en el documento de inventario físico:

1.  Automáticamente, creando una lista de los productos disponibles en el almacén y en los huecos definidos en la cabecera del inventario físico que cumplan las condiciones de filtrado especificadas por el botón **Crear lista de conteo de inventario**.
2.  Manualmente, línea a línea para determinados productos. Esto se utiliza cuando solo es necesario actualizar algunos productos.

El proceso **Crear lista de conteo de inventario** puede ejecutarse más de una vez para el mismo inventario físico. Aunque las líneas se crean automáticamente mediante el proceso **Crear lista de conteo de inventario**, estas líneas pueden actualizarse posteriormente de forma manual. El diálogo de filtros de **Crear lista de conteo de inventario** tiene los siguientes parámetros:

![Cabecera 2](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/physical-inventory/physical-inventory-2.png)

Los campos a tener en cuenta son:

- **Hueco:** solo se filtrarán los productos de este hueco.
- **Categoría del producto:** solo se filtrarán los productos que pertenezcan a una categoría de producto determinada; en caso contrario, se mostrarán todos los productos.
- **Cantidad de inventario:** incluye o excluye productos en el inventario físico en función de las cantidades reales. Las opciones disponibles son:
    - vacío - se mostrarán todos los productos en el inventario físico independientemente de su cantidad
    - 0 - se mostrarán solo los productos en el inventario físico que tengan cantidad 0 en stock.
    - <0 - se mostrarán solo los productos en el inventario físico que tengan una cantidad negativa en stock.
    - \>0 - se mostrarán solo los productos en el inventario físico que tengan una cantidad positiva en stock.
    - distinto de 0 - se mostrarán solo los productos en el inventario físico que tengan una cantidad en stock distinta de 0.
- **Establecer Cantidad teórica a cero:** esta casilla establece el campo **Cant.total** de la lista de conteo a cero. Cuando la casilla no está seleccionada, la **Cant.total** toma por defecto el mismo valor que la **Cantidad teórica** (Cantidad disponible) del producto.
    - La primera opción se utiliza para inventarios físicos ciegos, en los que las personas que cuentan los artículos en el almacén no necesitan conocer las cantidades esperadas.
    - La segunda opción se utiliza para permitir al usuario introducir el conteo de cantidad "real" en el almacén y el hueco. Una vez procesado el conteo de inventario, la cantidad teórica mostrada por el sistema se actualizará a la cantidad contada introducida por el usuario.
- **ABC:** informe de productos Pareto

## Líneas { #lines }

La solapa Líneas permite al usuario añadir o editar productos individuales que se incluirán en la lista de conteo de inventario. Representa la lista de conteo de inventario de un almacén determinado.

Algunos campos relevantes a tener en cuenta son:

- **Cant.total:** es el stock real (contado físicamente) del producto en el **Hueco** del almacén.
- **Cantidad teórica:** es el stock del producto en el **Hueco** según Etendo.
- **Costo:** es el coste unitario del producto.  
  Este campo es opcional. Puede rellenarse con el coste si se conoce cuando el stock de un producto se incrementa; en caso contrario, se utiliza el método de Coste por defecto para valorar esa transacción que incrementa el stock del producto.

Los botones de proceso son:

- **Actualizar cantidad** actualiza el campo **Cantidad teórica** actual con la última cantidad del producto desde la aplicación. Esto se utiliza en caso de que haya cambiado desde que se generó la lista de conteo. Es útil en situaciones en las que transcurre un tiempo significativo entre la generación del inventario físico en Etendo y el conteo físico real.
- **Proceso de Conteo de Inventario** finaliza el proceso de conteo de Inventario físico después de que se hayan introducido todas las correcciones y actualiza el stock.
- **Contabilizar** permite contabilizar el conteo de inventario una vez procesado.

## Contabilidad { #accounting }

Un inventario físico solo puede contabilizarse en el libro mayor en caso de que exista una diferencia entre "Cant.total" y "Cantidad teórica" para un producto. De lo contrario, no habrá nada que contabilizar en el libro mayor.

Por ejemplo, un producto cuya "Cant.total" es de 6700 unidades en una fecha determinada, mientras que la "Cantidad teórica" en Etendo es de 6000 unidades.

Ese inventario físico puede contabilizarse una vez procesado, si se ha calculado el coste del producto.

**La contabilización del Inventario físico crea los siguientes asientos contables si el inventario aumenta:**

|                           |                                                             |                                                             |
| ------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| Cuenta               | Débito                                                   | Crédito**                                                  |
| Inmovilizado del producto         | (Cant.total - Cantidad teórica) \* Coste del producto |                                                             |
| Diferencias de almacén |                                                             | (Cant.total - Cantidad teórica) \* Coste del producto |

**La contabilización del Inventario físico crea los siguientes asientos contables si el inventario disminuye:**

|                           |                                                             |                                                             |
| ------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| Cuenta               | Débito                                                   | Crédito                                                  |
| Diferencias de almacén | (Cant.total - Cantidad teórica) \* Coste del producto |                                                             |
| Inmovilizado del producto         |                                                             | (Cant.total - Cantidad teórica) \* Coste del producto |

## Cómo reactivar inventarios físicos { #how-to-reactivate-physical-inventories }

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Warehouse Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Warehouse Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=EFDA39668E2E4DF2824FFF0A905E6A95){target="_blank"}.

Desde la ventana Inventario físico, es posible reactivar un inventario generado previamente con solo seleccionar el documento correspondiente y hacer clic en el botón Reactivar.

Una vez que el inventario se reactiva correctamente, el estado del documento cambia a No procesado, tal y como puede observarse en la barra de estado.

![](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/physical-inventory/physical-inventory-3.png)

!!! warning
    No es posible reactivar documentos que incluyan transacciones con cantidades que excedan la cantidad de stock existente para un determinado producto en un determinado hueco. La única excepción es cuando la configuración del hueco permite Over Issue. Para más información, visite [Hueco](../../../../../user-guide/etendo-classic/basic-features/warehouse-management/setup.md#storage-bin).

## Contabilización masiva { #bulk-posting }

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}.

La funcionalidad de Contabilización masiva permite al usuario contabilizar o deshacer la contabilización de múltiples registros seleccionando los registros correspondientes y haciendo clic en el botón **Contabilización masiva**.

Además, el Estado contable del/de los registro/s se muestra en la barra de estado, en la vista de formulario o en una columna, en la vista de cuadrícula.

!!! info
    Para más información, visite [la guía de usuario del módulo Contabilización masiva](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).

---

Este trabajo es una obra derivada de [Gestión de Almacén](http://wiki.openbravo.com/wiki/Warehouse_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, usada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.