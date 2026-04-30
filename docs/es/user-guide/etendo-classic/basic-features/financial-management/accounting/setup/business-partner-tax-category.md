---
title: Categoría de Impuestos de Terceros
tags:
    - Business Partner
    - Tax Category
    - Financial Management
    - Setup
    - Accounting
---


# Categoría de Impuestos de Terceros

:material-menu: `Aplicación` > `Gestión Financiera` > `Contabilidad` > `Configuración` > `Categoría de Impuestos de Terceros`

## Visión general

No todos los terceros están sujetos a los mismos impuestos. Un proveedor nacional sujeto a IVA y a retención de IRPF debe tratarse de forma diferente a un cliente de exportación con tipo cero, o a un tercero cuya actividad lo exime de impuestos. La **Categoría de Impuestos de Terceros** es el elemento de configuración que recoge estas diferencias: es un grupo con nombre que el administrador del sistema o el contable asigna a clientes y proveedores para que Etendo sepa qué tipos impositivos les aplican.

Esta configuración se realiza una sola vez, durante la configuración inicial del esquema fiscal. Una vez que cada tercero tiene asignada una categoría, esta funciona en segundo plano: cada vez que un usuario crea un pedido o una factura, Etendo lee la categoría de impuestos del tercero y la usa como uno de los filtros para determinar qué tipo impositivo se rellena automáticamente en la línea del documento. El usuario no tiene que preocuparse por ello: el impuesto correcto aparece por sí solo.

## Ventana Categoría de Impuestos de Terceros

La ventana muestra todas las categorías de impuestos de terceros existentes y permite crear nuevas. Es posible definir tantas categorías como requiera la estructura fiscal de la empresa.

![Ventana Categoría de Impuestos de Terceros mostrando la lista de categorías y el formulario de cabecera](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/setup/business-partner-tax-category/business-partner-tax-category.png)

### Campos

- **Nombre**: El identificador de la categoría. Utilice una etiqueta clara y descriptiva que refleje el tratamiento fiscal que representa, como *IVA estándar*, *IVA + Retención de IRPF* o *Exento de IVA*. Este nombre aparece en la ventana Tercero al asignar la categoría a un cliente o proveedor.
- **Descripción**: Un campo opcional de texto libre para notas internas que expliquen el propósito o el alcance de la categoría. Solo es visible en esta ventana y ayuda a otros administradores a entender cuándo usar cada categoría.
- **Activo**: Cuando está marcado, la categoría está disponible para asignarse a terceros. Desactivar una categoría no la elimina de los terceros ya asignados, pero la oculta de las listas de selección para nuevas asignaciones.

## Asignación de la categoría a un tercero

Una vez creadas las categorías, cada tercero que requiera un tratamiento fiscal específico debe vincularse a la categoría adecuada. Esto se hace en la ventana [**Tercero**](../../../master-data-management/master-data.md):

- Para clientes: abra la solapa [**Cliente**](../../../master-data-management/master-data.md#customer) del registro del tercero y establezca el campo **Categoría Imp. Tercero**.
- Para proveedores y acreedores: abra la solapa [**Proveedor/Acreedor**](../../../master-data-management/master-data.md#vendorcreditor) y establezca el mismo campo.

Un mismo tercero puede actuar tanto como cliente como proveedor. En ese caso, ambas solapas pueden tener asignada una categoría de impuestos, y cada una puede ser diferente si el tratamiento fiscal difiere entre compras y ventas.

!!!note
    Si un tercero no tiene asignada una categoría de impuestos, Etendo no filtra los tipos impositivos por este criterio para ese tercero. Todos los tipos impositivos que cumplan las condiciones restantes (categoría de impuesto del producto, zona geográfica, tipo de documento) se consideran al seleccionar el impuesto predeterminado.

## Cómo funciona con los tipos impositivos

La Categoría de Impuestos de Terceros es una de las varias condiciones que Etendo evalúa cuando determina el impuesto predeterminado para una línea de documento. La lógica completa de selección se describe en la página [Tipo impositivo](tax-rate.md). En resumen, los pasos relevantes son:

1. Etendo lee la **Categoría de Impuesto** vinculada al producto en la línea del documento. Esto reduce el conjunto de tipos impositivos candidatos.
2. Entre esos candidatos, Etendo filtra además por **Categoría de Impuestos de Terceros**: un tipo impositivo que tenga asignada una categoría de impuestos de terceros específica solo se aplica a los terceros de esa categoría. Un tipo impositivo sin categoría de impuestos de terceros asignada se aplica a cualquier tercero.
3. Cuando existen ambos tipos (específico y sin restricción), el tipo impositivo que coincide con la categoría del tercero tiene prioridad.
4. A continuación se aplican filtros adicionales (zona geográfica, tipo de documento, indicador de IVA de caja) para llegar al tipo impositivo final.

Esto significa que configurar la Categoría de Impuestos de Terceros en un tipo impositivo (en la ventana [Tipo impositivo](tax-rate.md), dentro de la sección **Más información** de la solapa Cabecera) y asignar una categoría coincidente a un tercero son pasos complementarios. Uno sin el otro no produce ningún efecto de filtrado.

La página [Categoría de Impuesto](tax-category.md) describe cómo se agrupan los productos a efectos fiscales, lo que constituye el punto de partida de la misma cadena de determinación.

!!!info
    Independientemente del tipo impositivo que Etendo seleccione automáticamente, el usuario siempre puede elegir manualmente un tipo impositivo diferente en cualquier línea de documento si el escenario de negocio específico lo requiere.

---

Este trabajo es una obra derivada de [Categoría de Impuestos de Terceros](https://wiki.openbravo.com/wiki/Business_Partner_Tax_Category){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.

---

---