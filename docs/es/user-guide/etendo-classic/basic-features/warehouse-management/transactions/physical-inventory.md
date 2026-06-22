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

## Descripción general { #overview }

La ventana **Inventario físico** permite registrar y procesar operaciones de conteo de mercancías en Etendo. Úsela para comparar los conteos físicos de stock con las cantidades del sistema y detectar discrepancias. Ajuste los niveles de stock en consecuencia.

<iframe width="560" height="315" src="https://www.youtube.com/embed/xqE_UnYO6cM" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Cabecera { #header }

El proceso de conteo de mercancías requiere crear un conteo de inventario para comprobar o actualizar las cantidades de stock.

La sección **Cabecera** identifica el proceso de **Inventario físico** y lista sus parámetros principales.

![physical-inventory-1](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/physical-inventory/physical-inventory-1.png)

Todos los campos se rellenan automáticamente cuando se crea un registro nuevo.

Algunos de los campos a tener en cuenta son:

- **Nombre:** Este campo se utiliza para hacer referencia al movimiento físico no solo en los informes de almacén, sino también en el libro mayor; por lo tanto, es importante utilizar un nombre significativo.
- **Fecha del movimiento:** fecha del movimiento de inventario físico. Por defecto, es la fecha actual.  
  Esta fecha se utiliza en el registro de contabilización en el libro mayor del documento de Inventario físico, si aplica.  
  Tenga en cuenta que el **Proceso de Conteo de Inventario** siempre utiliza la fecha actual para actualizar el stock, no este campo.

    !!! warning
        Cambie esta fecha solo cuando tenga la certeza de que no existen movimientos de stock desde el momento en que se creó el inventario. Cambiarla en caso contrario puede provocar desajustes contables.
        
- **Almacén:** el almacén en el que tiene lugar el inventario físico. Por defecto, toma el valor de la sesión desde el menú superior de navegación Preferencias de Usuario.

Hay 2 formas de **introducir líneas** en el documento de inventario físico:

1.  Automáticamente, creando una lista de los productos disponibles en el almacén y en los huecos definidos en la cabecera del inventario físico que cumplan las condiciones de filtrado especificadas por el botón **Crear lista de conteo de inventario**.
2.  Manualmente, línea a línea para determinados productos. Esto se utiliza cuando solo es necesario actualizar algunos productos.

### Crear lista de conteo de inventario { #create-inventory-count-list }

El proceso **Crear lista de conteo de inventario** puede ejecutarse más de una vez para el mismo inventario físico. Las líneas se crean automáticamente mediante el proceso **Crear lista de conteo de inventario**. Pueden actualizarse manualmente después de su creación. El diálogo de filtros de **Crear lista de conteo de inventario** tiene los siguientes parámetros:

![physical-inventory-2](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/physical-inventory/physical-inventory-2.png)

Los campos a tener en cuenta son:

- **Hueco:** solo se filtrarán los productos de este hueco.
- **Categoría del producto:** solo se filtrarán los productos que pertenezcan a una categoría de producto determinada; en caso contrario, se mostrarán todos los productos.
- **Cantidad de inventario:** incluye o excluye productos en el inventario físico en función de las cantidades reales. Las opciones disponibles son:
    - `vacío` - se mostrarán todos los productos en el inventario físico independientemente de su cantidad.
    - `0` - se mostrarán solo los productos con cantidad 0 en stock.
    - `<0` - se mostrarán solo los productos con una cantidad negativa en stock.
    - `>0` - se mostrarán solo los productos con una cantidad positiva en stock.
    - `distinto de 0` - se mostrarán solo los productos con una cantidad en stock distinta de 0.
- **Fijar Cantidad Registrada a Cero:** seleccione esta casilla para que el equipo de conteo registre las cantidades desde cero, sin ver lo que el sistema muestra actualmente. Esto se denomina conteo ciego y evita sesgos en los resultados del conteo. Déjela sin seleccionar para mostrar la cantidad actual del sistema como punto de partida para correcciones si el conteo físico difiere.
- **ABC:** filtra la lista para mostrar solo los productos de un grupo de prioridad específico: A = productos más valiosos o de mayor rotación, B = prioridad media, C = prioridad baja. Deje este campo vacío para incluir todos los productos cuando el grupo de productos sea desconocido. Consulte [Informe Pareto de Productos](../analysis-tools/pareto-product-report.md).

## Líneas { #lines }

La solapa Líneas permite al usuario añadir o editar productos individuales que se incluirán en la lista de conteo de inventario. Representa la lista de conteo de inventario de un almacén determinado.

![physical-inventory-3](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/physical-inventory/physical-inventory-3.png)

Algunos campos relevantes a tener en cuenta son:

- **Valor atributos:** identifica la variante o instancia de atributo específica del producto, como el número de lote, número de serie o talla.
- **Cant.total:** la cantidad real contada en el almacén para este producto en el hueco indicado.
- **Unidad:** la unidad de medida del producto.
- **Hueco:** el hueco donde se encuentra el producto.
- **Descripción:** una descripción opcional para la línea.
- **Cantidad teórica:** la cantidad que el sistema muestra actualmente para este producto en el hueco indicado.
- **Cantidad pedido teórico:** la cantidad reservada o comprometida en pedidos abiertos para este producto en este hueco.

### Botones { #buttons }

#### Actualizar cantidad { #update-quantity }

Actualiza el campo **Cantidad teórica** actual con la última cantidad del producto desde la aplicación. Esto es útil cuando transcurre un tiempo significativo entre la generación del inventario físico en Etendo y el conteo físico real, en caso de que la cantidad haya cambiado desde que se generó la lista de conteo.

#### Proceso de Conteo de Inventario { #process-inventory-count }

Finaliza el proceso de conteo de Inventario físico después de que se hayan introducido todas las correcciones y actualiza el stock.

#### Contabilizar { #post }

Permite contabilizar el conteo de inventario en el libro mayor una vez procesado.

## Contabilidad { #accounting }

Un inventario físico solo puede contabilizarse en el libro mayor en caso de que exista una diferencia entre **Cant.total** y **Cantidad teórica** para un producto. De lo contrario, no habrá nada que contabilizar en el libro mayor.

Por ejemplo, un producto cuya **Cant.total** es de 6700 unidades en una fecha determinada, mientras que la **Cantidad teórica** en Etendo es de 6000 unidades.

La contabilización de un Inventario físico implica tener calculado el coste del producto:

- Se requiere una [Regla de cálculo de costes](../setup.md#costing-rules) validada en la entidad legal del Inventario físico.
- El proceso en segundo plano [Proceso en segundo plano de cálculo de costes](../../general-setup/process-scheduling/process-request.md#cálculo-de-costes) debe haberse ejecutado.
- Una vez calculado el coste, el Inventario físico puede contabilizarse.

Al hacer clic en **Contabilizar**, Etendo crea automáticamente los siguientes asientos contables. Estos son generados por el sistema — no se requiere entrada manual. Los importes se calculan como la diferencia entre la cantidad contada y la cantidad teórica, multiplicada por el coste unitario del producto.

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
    Para poder incluir esta funcionalidad, debe instalarse el Warehouse Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Warehouse Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=EFDA39668E2E4DF2824FFF0A905E6A95){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el núcleo y nuevas funcionalidades, visite [Warehouse Extensions - Notas de lanzamiento](../../../../../whats-new/release-notes/etendo-classic/bundles/warehouse-extensions/release-notes.md).

Para corregir un inventario físico que ya ha sido procesado — por ejemplo, después de que se detecte un error de conteo — reactívelo para realizar cambios. Desde la ventana Inventario físico, seleccione el documento correspondiente y haga clic en el botón Reactivar.

Una vez que el inventario se reactiva correctamente, la barra de estado del documento mostrará No procesado, confirmando que la reactivación se realizó con éxito.

![physical-inventory-4](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/physical-inventory/physical-inventory-4.png)

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