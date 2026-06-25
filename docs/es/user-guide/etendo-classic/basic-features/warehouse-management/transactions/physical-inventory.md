---
title: Physical Inventory
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

<iframe width="560" height="315" src="https://www.youtube.com/embed/xqE_UnYO6cM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Cabecera { #header }

Cree un conteo de inventario para comprobar o actualizar las cantidades de stock.

Complete o confirme los campos a continuación antes de añadir productos a la lista de conteo.

![physical-inventory-1](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/physical-inventory/physical-inventory-1.png)

Todos los campos se rellenan automáticamente cuando se crea un registro nuevo.

Campos a tener en cuenta:

- **Nombre:** Use este campo para hacer referencia al movimiento físico en los informes de almacén y en el libro mayor. Use un nombre significativo.
- **Fecha del movimiento:** fecha del movimiento de inventario físico. Por defecto, es la fecha actual.  
  Etendo usa esta fecha en el registro de contabilización en el libro mayor del documento de Inventario físico. Esto aplica cuando su empresa tiene la contabilidad configurada y el inventario se contabiliza tras el procesamiento. Si la contabilización no aplica a su configuración, contacte con su equipo de finanzas.  
  El **Proceso de Conteo de Inventario** siempre utiliza la fecha actual para actualizar el stock, no este campo.

    !!! warning
        Solo cambie esta fecha cuando tenga la certeza de que no existen movimientos de stock desde el momento en que se creó el inventario. Cambiarla en caso contrario puede provocar desajustes contables.

- **Almacén:** el almacén en el que tiene lugar el inventario físico. Por defecto, toma el valor del almacén definido en sus preferencias de usuario. Cámbielo si está realizando el conteo en un almacén diferente.

## Botones { #buttons }

### Crear lista de conteo de inventario { #create-inventory-count-list }

Disponible cuando el estado del documento es **Procesado: No**.

El proceso **Crear lista de conteo de inventario** puede ejecutarse más de una vez para el mismo inventario físico. Las líneas se crean automáticamente mediante el proceso. Actualícelas manualmente después de su creación si es necesario. El diálogo de filtros de **Crear lista de conteo de inventario** tiene los siguientes parámetros:

![physical-inventory-2](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/physical-inventory/physical-inventory-2.png)

Campos a tener en cuenta:

- **Hueco:** filtra la lista para mostrar solo los productos de este hueco.
- **Categoría de producto:** filtra la lista para mostrar solo los productos que pertenezcan a esta categoría. Déjelo vacío para incluir todas las categorías.
- **Cantidad de inventario:** filtra los productos según las cantidades reales de stock. Las opciones disponibles son:
    - `vacío` - muestra todos los productos independientemente de su cantidad.
    - `0` - muestra solo los productos con cantidad 0 en stock.
    - `<0` - muestra solo los productos con una cantidad negativa en stock.
    - `>0` - muestra solo los productos con una cantidad positiva en stock.
    - `distinto de 0` - muestra solo los productos con una cantidad en stock distinta de 0.
- **Fijar Cantidad Registrada a Cero:** seleccione esta casilla para que el equipo de conteo registre las cantidades desde cero, sin ver lo que el sistema muestra actualmente. Esto se denomina conteo ciego y evita sesgos en los resultados del conteo. Déjela sin seleccionar para mostrar la cantidad actual del sistema como punto de partida para correcciones si el conteo físico difiere.
- **ABC:** filtra la lista para mostrar solo los productos de un grupo de prioridad específico: A = productos más valiosos o de mayor rotación, B = prioridad media, C = prioridad baja. Deje este campo vacío para incluir todos los productos cuando el grupo de productos sea desconocido. Consulte [Informe Pareto de Productos](../analysis-tools/pareto-product-report.md).

### Actualizar cantidad { #update-quantity }

Disponible cuando el estado del documento es **Procesado: No**.

Actualiza el campo **Cantidad teórica** con la última cantidad del producto en Etendo. Úselo cuando haya transcurrido tiempo entre la generación de la lista de conteo y el conteo físico real, y las cantidades puedan haber cambiado.

### Proceso de Conteo de Inventario { #process-inventory-count }

Disponible cuando el estado del documento es **Procesado: No**. Tras la ejecución, el estado del documento cambia a **Procesado: Sí**.

Finaliza el proceso de conteo de Inventario físico una vez introducidas todas las correcciones y actualiza el stock.

### Contabilizar { #post }

Disponible cuando el estado del documento es **Procesado: Sí**. Tras la ejecución, el **Estado contable** cambia de **Sin contabilizar** a **Contabilizado**.

Contabiliza el conteo de inventario en el libro mayor una vez procesado. Para más detalles sobre lo que Etendo registra en el libro mayor, consulte [Contabilidad](#accounting).

## Líneas { #lines }

Las líneas se introducen en el documento de inventario físico de dos formas:

1.  Automáticamente, ejecutando **Crear lista de conteo de inventario** para generar líneas para todos los productos del almacén y los huecos que cumplan las condiciones de filtrado.
2.  Manualmente, línea a línea para productos específicos. Use esta opción cuando solo sea necesario actualizar algunos productos.

La solapa **Líneas** permite añadir o editar productos individuales en la lista de conteo de inventario. Representa la lista de conteo de inventario de un almacén determinado.

![physical-inventory-3](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/physical-inventory/physical-inventory-3.png)

Campos a tener en cuenta:

- **Valor atributos:** identifica la variante específica del producto, como el número de lote, número de serie o talla, si el producto se gestiona de esa forma.
- **Cant.total:** la cantidad real contada en el almacén para este producto en el hueco indicado.
- **UOM:** la unidad de medida del producto.
- **Hueco:** el hueco donde se encuentra el producto.
- **Descripción:** una descripción opcional para la línea.
- **Cantidad teórica:** la cantidad que el sistema muestra actualmente para este producto en el hueco indicado.
- **Cantidad pedido teórico:** la cantidad de este producto ya comprometida en pedidos de compra o venta abiertos para este hueco. Esta cantidad no está disponible para uso libre.



## Contabilidad { #accounting }

Un inventario físico solo puede contabilizarse en el libro mayor cuando existe una diferencia entre **Cant.total** y **Cantidad teórica** para un producto. Cuando los valores coinciden, no hay nada que contabilizar.

Por ejemplo, un producto cuya **Cant.total** es de 6700 unidades en una fecha determinada, mientras que la **Cantidad teórica** en Etendo es de 6000 unidades.

Antes de contabilizar, es necesario que existan dos requisitos a nivel de sistema. Normalmente los configura el administrador del sistema:

1. Debe existir una [Regla de cálculo de costes](../setup.md#costing-rules) validada y activa para la entidad legal de este inventario físico. Esta regla define cómo se calculan los costes de los productos.
2. El [Proceso en segundo plano de cálculo de costes](../../general-setup/process-scheduling/process-request.md#costing) debe haberse ejecutado después de que el inventario fuera procesado. Este proceso calcula el coste del movimiento de inventario.

Si el botón **Contabilizar** no está disponible o devuelve un error, el coste no ha sido calculado aún. Contacte con su administrador del sistema para verificar que la regla de cálculo de costes está activa y que el proceso en segundo plano se ha ejecutado.

Haga clic en **Contabilizar** para que Etendo cree automáticamente los siguientes asientos contables. No se requiere entrada manual. Etendo calcula los importes como la diferencia entre la cantidad contada y la cantidad teórica, multiplicada por el coste unitario del producto.

**La contabilización del Inventario físico crea los siguientes asientos contables si el inventario aumenta:**

|                           |                                                             |                                                             |
| ------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| Cuenta               | Débito                                                   | Crédito                                                  |
| Inmovilizado del producto         | (Cant.total - Cantidad teórica) \* Coste del producto |                                                             |
| Diferencias de almacén |                                                             | (Cant.total - Cantidad teórica) \* Coste del producto |

**La contabilización del Inventario físico crea los siguientes asientos contables si el inventario disminuye:**

|                           |                                                             |                                                             |
| ------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| Cuenta               | Débito                                                   | Crédito                                                  |
| Diferencias de almacén | (Cant.total - Cantidad teórica) \* Coste del producto |                                                             |
| Inmovilizado del producto         |                                                             | (Cant.total - Cantidad teórica) \* Coste del producto |

## Reactivar un inventario físico { #reactivating-a-physical-inventory }

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Warehouse Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Warehouse Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=EFDA39668E2E4DF2824FFF0A905E6A95){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el núcleo y nuevas funcionalidades, visite [Warehouse Extensions - Notas de lanzamiento](../../../../../whats-new/release-notes/etendo-classic/bundles/warehouse-extensions/release-notes.md).

Para corregir un inventario físico que ya ha sido procesado — por ejemplo, después de detectar un error de conteo — reactívelo para realizar cambios. Desde la ventana **Inventario físico**, seleccione el documento correspondiente y haga clic en **Reactivar**.

Una vez que el inventario se reactiva, la barra de estado del documento muestra **No procesado**.

![physical-inventory-4](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/physical-inventory/physical-inventory-4.png)

!!! warning
    No es posible reactivar documentos que incluyan transacciones con cantidades que excedan la cantidad de stock existente para un determinado producto en un determinado hueco. La única excepción es cuando el hueco está configurado para permitir Over Issue, una configuración que permite que los niveles de stock bajen por debajo de cero. Si no puede reactivar y no sabe con certeza si Over Issue aplica a su hueco, contacte con su administrador del sistema. Para más información, visite [Hueco](../../../../../user-guide/etendo-classic/basic-features/warehouse-management/setup.md#storage-bin).

## Contabilización Masiva { #bulk-posting }

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}.

La funcionalidad de **Contabilización Masiva** permite contabilizar o revertir los asientos contables de múltiples documentos de inventario al mismo tiempo. Seleccione los registros que desea procesar y haga clic en **Contabilización Masiva**. Puede comprobar el estado contable de cada registro en la barra de estado (al visualizar un registro individual) o en la columna Estado (al visualizar la grilla de registros).

!!! info
    Para más información, visite [la guía de usuario del módulo Contabilización masiva](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).

*[UOM]: Unidad de medida
*[ABC]: Clasificación ABC — A: productos de mayor valor o rotación, B: prioridad media, C: prioridad baja

---

This work is a derivative of [Warehouse Management](http://wiki.openbravo.com/wiki/Warehouse_Management){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
