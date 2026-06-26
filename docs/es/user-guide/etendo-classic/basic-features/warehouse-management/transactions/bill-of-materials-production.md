---
title: Producción LDM
tags:
 - Lista de materiales
 - Producción LDM
 - Gestión de Almacén
 - Transacciones
---

# Producción LDM { #bill-of-materials-production }

:material-menu: `Aplicación` > `Gestión de Almacén` > `Transacciones` > `Producción LDM`

## Descripción general { #overview }

La ventana **Producción LDM** registra el empaquetado de componentes individuales en un producto terminado y empaquetado. Defina qué componentes conforman el paquete en la configuración de la LDM del producto y, a continuación, utilice esta ventana para ejecutar el proceso de empaquetado: el sistema descuenta los componentes del stock y añade el producto empaquetado.

Utilice esta ventana para ensamblar o empaquetar productos físicamente antes del envío — por ejemplo, para agrupar un portátil con un teclado y un cable de alimentación en una única unidad de venta, o para agrupar piezas de repuesto en un kit de mantenimiento.

!!! info "Este no es un proceso de fabricación"
    A pesar del nombre, este proceso **no forma parte de la producción**. No se realiza ninguna fabricación — solo se agrupan productos terminados ya existentes. Si necesita realizar un seguimiento de órdenes de producción reales u órdenes de trabajo, utilice un módulo de fabricación dedicado.

Para el proceso paso a paso completo, consulte [Inicio rápido](#quick-start) a continuación. Para obtener detalle a nivel de campo, consulte cada sección.

## Requisitos previos { #prerequisites }

Antes de crear un registro de Producción LDM, confirme que lo siguiente está configurado en la ventana [Producto](../../master-data-management/master-data/product.md#bill-of-materials):

- [X] La casilla de verificación **Lista de materiales** está habilitada en el producto.
- [X] La solapa **Lista de materiales** está cumplimentada con todos los productos componentes y sus cantidades.
- [X] Se ha hecho clic en el botón **Comprobar LDM** para marcar el producto como listo.

## Inicio rápido: cómo empaquetar un producto { #quick-start }

1. **Configurar el producto** — habilite la casilla de verificación **Lista de materiales**, cumplimente la solapa **Lista de materiales** y haga clic en **Comprobar LDM** en el registro del producto.
2. **Cumplimentar la cabecera de Producción LDM** — establezca la organización, el nombre y la fecha del movimiento.
3. **Añadir líneas en la solapa Plan de producción** — seleccione el producto empaquetado, la cantidad de producción y el hueco de destino.
4. **Hacer clic en Crear/Procesar producción (primer clic)** — el sistema genera la lista de E/S Productos a partir de la configuración de la LDM. Revise y ajuste las cantidades si es necesario.
5. **Hacer clic en Crear/Procesar producción (segundo clic)** — el sistema confirma y ejecuta el empaquetado, descontando los componentes del stock y añadiendo el producto empaquetado. Antes de confirmar, revise las opciones del popup en [Crear/Procesar producción](#createprocess-production) — esas casillas de verificación afectan a qué stock de almacén se utiliza y si se permite una ejecución parcial.

## Cabecera { #header }

La cabecera de Producción LDM es la primera sección que se debe cumplimentar al crear un nuevo registro de empaquetado.

![Cabecera de Producción LDM](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/bill-of-materials-production/bill-of-materials-production-1.png)

- **Organización:** organización a la que pertenece este registro.
- **Nombre:** identificador para esta ejecución de empaquetado; se utiliza como referencia en los informes.
- **Fecha del movimiento:** fecha en la que se ejecuta el empaquetado.


### Plan de producción { #production-plan }

Añada uno o más productos empaquetados a producir en esta ejecución.

![Solapa Plan de producción](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/bill-of-materials-production/bill-of-materials-production-2.png)

- **Producto:** producto empaquetado a producir. Debe tener la casilla de verificación **Lista de materiales** habilitada y su [solapa Lista de materiales](../../master-data-management/master-data/product.md#bill-of-materials) configurada.
- **Cant.producción:** número de productos empaquetados a producir.
- **[Hueco](../../../../../user-guide/etendo-classic/basic-features/warehouse-management/setup.md#storage-bin):** hueco en el que se almacena el producto empaquetado resultante.


#### E/S Productos (Entrada/Salida) { #io-products }

Esta solapa muestra las entradas (componentes consumidos) y la salida (el producto empaquetado creado) para esta ejecución.

Haga clic en **Crear/Procesar producción** para rellenar esta solapa. Para el proceso en dos clics, consulte [Inicio rápido](#quick-start).

![Solapa E/S Productos](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/bill-of-materials-production/bill-of-materials-production-3.png)

Campos clave en esta solapa:

- **Producto:** componente que se está consumiendo.
- **Cant. movida:** cantidad del componente a consumir, calculada a partir de la LDM y la cantidad de producción.
- **[Hueco](../../../../../user-guide/etendo-classic/basic-features/warehouse-management/setup.md#storage-bin):** hueco desde el que se obtiene el stock del componente.

### Contabilidad { #accounting }

![Solapa Contabilidad](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/bill-of-materials-production/bill-of-materials-production-5.png)

La solapa **Contabilidad** se rellena automáticamente después de hacer clic en **Contabilizar**. Muestra los asientos contables generados por la ejecución de empaquetado — una línea por movimiento contable. No se requiere ninguna entrada manual.

Cada línea incluye la organización, el libro mayor, la fecha contable, la cuenta (como Inmovilizado del producto o Ajustes de almacén) y el importe en débito o crédito. Esta solapa es de solo lectura. Utilícela para verificar que el empaquetado se ha registrado correctamente en el libro mayor.


## Botones { #buttons }

### Crear/Procesar producción { #createprocess-production }

Este botón tiene dos propósitos diferentes según si las líneas de E/S Productos ya existen o no:

- **Primer clic** — si no existen todavía líneas de E/S Productos, el sistema las genera automáticamente en función de la configuración de la LDM y la cantidad de producción. Las líneas pueden revisarse y ajustarse manualmente antes de continuar.
- **Segundo clic** — si las líneas de E/S Productos ya existen (generadas o introducidas manualmente), el sistema ejecuta el movimiento de stock: los componentes se eliminan del stock y el producto empaquetado se añade al stock.

![Botón Crear/Procesar producción](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/bill-of-materials-production/bill-of-materials-production-4.png)

En el popup de confirmación:

- Seleccione la casilla de verificación **Cant.producto exigida en stock** para permitir que el proceso se ejecute únicamente cuando todos los componentes estén disponibles en stock. Tras una ejecución correcta, el stock de los componentes disminuye y el stock del producto empaquetado aumenta. Para verificar el resultado, consulte el [Informe Stock](../analysis-tools/stock-report.md) o el [Informe Movimiento de Productos](../analysis-tools/product-movements-report.md).

    !!! warning
        Si no selecciona esta casilla de verificación y no hay suficiente stock de un componente, el sistema utilizará el stock que haya disponible. Esto puede dar lugar a menos productos empaquetados que la cantidad solicitada. Para evitar ejecuciones parciales, seleccione siempre la casilla de verificación antes de confirmar.

- **Forzar el uso del almacén del hueco seleccionado:** cuando está habilitado, el stock se obtiene exclusivamente del almacén del hueco seleccionado. Cuando está deshabilitado, el sistema busca los componentes en todos los almacenes disponibles para su organización, no solo en el que contiene el hueco seleccionado. Habilite esta opción cuando los componentes se registran por separado por ubicación y necesita extraer stock de una ubicación de almacén específica. Déjela deshabilitada para permitir que el sistema encuentre los componentes en toda su organización.

### Contabilizar { #post }

Contabiliza el registro de Producción LDM actual en el libro mayor. Utilice este botón para registrar la transacción de empaquetado de un único registro una vez que se ha procesado.

### Contabilización Masiva { #bulk-posting }

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}.

Contabilizar un registro lo registra en el libro mayor. Utilice la Contabilización Masiva para contabilizar o revertir la contabilización de múltiples registros de empaquetado a la vez, sin necesidad de abrirlos individualmente.

Seleccione los registros a contabilizar y haga clic en el botón **Contabilización Masiva**. El estado contable de uno o más registros se muestra en la barra de estado al visualizar un único registro (vista de formulario), o en una columna dedicada al visualizar la lista de registros (vista de grilla).

!!! info
    Para más información, visite [la guía de usuario del módulo Bulk Posting](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).

*[LDM]: Lista de Materiales
*[E/S]: Entrada/Salida — componentes consumidos y producto empaquetado creado

---

Este trabajo es una obra derivada de [Gestión de Almacén](http://wiki.openbravo.com/wiki/Warehouse_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, usada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.
