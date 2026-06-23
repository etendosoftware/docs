---
title: Producción LDM
tags:
 - Bill of Materials
 - BOM Production
 - Warehouse Management
 - Transactions
---

# Producción LDM { #bill-of-materials-production }

:material-menu: `Aplicación` > `Gestión de Almacén` > `Transacciones` > `Producción LDM`

## Descripción general { #overview }

Utilice esta ventana para agrupar componentes en un único producto mediante una lista de materiales configurada previamente.

!!! info "Este no es un proceso de fabricación"
    A pesar del nombre, este proceso **no forma parte de la producción**. Combina productos existentes en un **producto empaquetado**. No hay fabricación real implicada. Utilícelo, por ejemplo, para agrupar un ordenador con su teclado o un dispositivo con cables de alimentación específicos para cada región.

### Requisitos previos { #prerequisites }

Antes de crear un registro de Producción LDM, configure correctamente el producto empaquetado en la ventana [Producto](../../master-data-management/master-data/product.md#bill-of-materials):

- La casilla de verificación **Lista de materiales** está habilitada en el producto.
- La solapa **Lista de materiales** está cumplimentada con todos los productos componentes y sus cantidades.
- Se ha hecho clic en el botón **Comprobar LDM** para marcar el producto como listo.

### Paso a paso { #step-by-step }

El proceso completo de empaquetado sigue estos pasos:

1. **Configurar el producto** — configure la casilla de verificación de Lista de materiales, la solapa Lista de materiales y haga clic en **Comprobar LDM** en el registro del producto.
2. **Cumplimentar la cabecera de Producción LDM** — establezca la organización, el nombre y la fecha del movimiento.
3. **Añadir líneas en la solapa Plan de producción** — seleccione el producto empaquetado, la cantidad de producción y el hueco de destino.
4. **Hacer clic en Crear/Procesar producción (primer clic)** — el sistema genera la lista de Líneas a partir de la configuración de la Lista de materiales. Revise y ajuste las cantidades si es necesario.
5. **Hacer clic en Crear/Procesar producción (segundo clic)** — el sistema confirma y ejecuta el empaquetado, descontando los componentes del stock y añadiendo el producto empaquetado.

## Cabecera { #bom-production }

La cabecera de Producción LDM es la primera sección que se debe cumplimentar al crear un nuevo registro de empaquetado.

- **Organización:** la organización a la que pertenece este registro.
- **Nombre:** identifica esta ejecución de empaquetado; se utiliza como referencia en los informes.
- **Fecha del movimiento:** la fecha en la que se ejecuta el empaquetado.

![Cabecera de Producción LDM](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/bill-of-materials-production/bill-of-materials-production-1.png)

## Plan de producción { #production-plan }

Añada uno o más productos empaquetados a producir en esta ejecución.

- **Producto:** el producto empaquetado a producir. Debe tener la casilla de verificación **Lista de materiales** habilitada y su [solapa Lista de materiales](../../master-data-management/master-data/product.md#bill-of-materials) configurada.
- **Cant.producción:** el número de productos empaquetados a producir.
- **[Hueco](../../../../../user-guide/etendo-classic/basic-features/warehouse-management/setup.md#storage-bin):** el hueco en el que se almacena el producto empaquetado resultante.

![Solapa Plan de producción](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/bill-of-materials-production/bill-of-materials-production-2.png)

## Líneas { #io-products }

Esta solapa muestra las entradas (componentes consumidos) y la salida (el producto empaquetado creado) para esta ejecución.

Después de cumplimentar la solapa Plan de producción, haga clic en **Crear/Procesar producción** para generar la lista de componentes. El sistema calcula las cantidades en función de la configuración de la Lista de materiales y la cantidad de producción. Para obtener más detalles sobre cómo ejecutar este proceso, consulte el Flujo de trabajo en dos clics a continuación.

![Solapa Líneas](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/bill-of-materials-production/bill-of-materials-production-3.png)

Campos clave en esta solapa:

- **Producto:** el componente que se está consumiendo.
- **Cant. movida:** cantidad del componente a consumir, calculada a partir de la Lista de materiales y la cantidad de producción.
- **[Hueco](../../../../../user-guide/etendo-classic/basic-features/warehouse-management/setup.md#storage-bin):** el hueco desde el que se obtiene el stock del componente.
- **Forzar el uso del almacén del hueco seleccionado:** cuando está habilitado, el stock se obtiene exclusivamente del almacén del hueco seleccionado. Cuando está deshabilitado, el sistema buscará los componentes en todos los almacenes disponibles para su organización, no solo en el que contiene el hueco seleccionado.

### Flujo de trabajo en dos clics { #two-click-workflow }

1. **Primer clic** — genera la lista de componentes y sus cantidades en función de la configuración de la Lista de materiales. Revise esta lista y realice los ajustes necesarios.
2. **Segundo clic** — confirma y ejecuta la producción. Los componentes se descuentan del stock y el producto empaquetado se añade al stock.

En el popup de confirmación, seleccione la casilla de verificación **Cant.producto exigida en stock** para permitir que el proceso se ejecute únicamente cuando todos los componentes estén disponibles en stock. Tras una ejecución correcta, el stock de los componentes disminuye y el stock del producto empaquetado aumenta. Para verificar el resultado, consulte el [Informe Stock](../analysis-tools/stock-report.md) o el [Informe Movimiento de Productos](../analysis-tools/product-movements-report.md).

!!! warning
    Si no selecciona esta casilla de verificación y no hay suficiente stock de un componente, el sistema utilizará el stock disponible. Esto puede dar lugar a menos productos empaquetados que la cantidad solicitada. Para evitar ejecuciones parciales, seleccione siempre la casilla de verificación antes de confirmar.

## Contabilización masiva { #bulk-posting }

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}.

La funcionalidad de Contabilización masiva permite al usuario contabilizar o deshacer la contabilización de múltiples registros seleccionando los registros correspondientes y haciendo clic en el botón **Contabilización Masiva**.

Además, el Estado contable del/de los registro/s se muestra en la barra de estado, en la vista de formulario, o en una columna, en la vista de cuadrícula.

!!! info
    Para más información, visite [la guía de usuario del módulo Bulk Posting](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).

---

Este trabajo es una obra derivada de [Gestión de Almacén](http://wiki.openbravo.com/wiki/Warehouse_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, usada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.
