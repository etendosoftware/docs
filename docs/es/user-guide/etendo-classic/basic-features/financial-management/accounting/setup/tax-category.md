---
title: Categoría de Impuesto
tags:
    - Categoría de Impuesto
    - Configuración de Producto
    - Gestión Financiera
    - Configuración
    - Contabilidad
---

# Categoría de Impuesto

:material-menu: `Aplicación` > `Gestión Financiera` > `Contabilidad` > `Configuración` > `Categoría de Impuesto`

## Visión general

Una categoría de impuesto se utiliza para agrupar productos o servicios que comparten el mismo **tratamiento fiscal**. Dado que no todos los artículos tienen el mismo tipo impositivo (estándar, reducido o exento), las categorías de impuesto ayudan a organizar estas diferencias y garantizan que los impuestos se apliquen de forma automática y correcta durante las transacciones.

Cada producto o servicio debe asignarse a una categoría de impuesto en la ventana [Producto](../../../master-data-management/master-data.md#product), y los [Rango impuesto](../setup/tax-rate.md) también se vinculan a las categorías. Cuando se crea una transacción, Etendo solo considera los tipos impositivos asociados a la categoría seleccionada, reduciendo la intervención manual y evitando errores.

Factores adicionales, como la [Categoría de Impuestos de Terceros](../setup/business-partner-tax-category.md) y la configuración del tipo impositivo, ayudan al sistema a determinar el **impuesto final aplicable**.

### Cómo funcionan las categorías de impuesto

El proceso de determinación de impuestos sigue esta lógica:

1. La **Categoría de Impuesto del producto** define qué tipos impositivos están disponibles
2. La **Categoría de Impuestos de Terceros** (opcional) filtra aún más los tipos impositivos aplicables
3. La **configuración del tipo impositivo** determina el porcentaje final del impuesto en función de criterios adicionales (ubicación, tipo de documento, etc.)
4. La **selección automática** se produce al crear pedidos o facturas, pero siempre puede sobrescribirse manualmente

Esta estructura permite una gestión fiscal flexible manteniendo la consistencia en todo el sistema.


## Cabecera

Puede crear tantas categorías de impuesto como necesite para organizar distintos tratamientos fiscales en su sistema. Cada categoría se vinculará a tipos impositivos específicos y se asignará a productos. La solapa Cabecera define la información principal de la categoría de impuesto.

![alt text](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/set-up/tax-category1.png)

**Campos a tener en cuenta:**

- **Nombre**: Un nombre descriptivo para identificar la categoría de impuesto (p. ej., "IVA estándar", "IVA reducido", "Exento").
- **Descripción de la Categoría de Impuesto**: Explicación opcional del propósito de la categoría o de los escenarios de uso. Esto ayuda a otros usuarios a entender cuándo utilizar esta categoría.
- **Valor por defecto**: Si está marcado, esta categoría de impuesto se seleccionará automáticamente como valor por defecto al crear nuevos productos o al configurar tipos impositivos.
- **As per BOM** (lista de materiales): Cuando está habilitado, el impuesto se calcula proporcionalmente en función de los componentes de la lista de materiales del producto, en lugar de un único tipo.

    !!!info
        Si la categoría de impuesto está marcada como **As per BOM**, indica que los productos con esta categoría utilizarán los productos incluidos en su lista de lista de materiales para calcular proporcionalmente los impuestos. En este caso, solo debe configurarse **un Rango impuesto** para esta categoría de impuesto marcada como **Nivel agrupación**.

        **Ejemplo de caso de uso**: Un producto en pack que contiene artículos con distintos tipos impositivos (p. ej., una cesta regalo con alimentos al 10% y artículos no alimentarios al 21%) puede utilizar esta funcionalidad para calcular los impuestos proporcionalmente en función del valor y del tipo impositivo de cada componente.

!!!note "Después de crear categorías de impuesto"
    Una vez creadas, las categorías de impuesto deben:

    1. **Vincularse a tipos impositivos** en la ventana [Rango impuesto](../setup/tax-rate.md) - Cada tipo impositivo debe pertenecer al menos a una categoría de impuesto
    2. **Asignarse a productos** en la ventana [Producto](../../../master-data-management/master-data.md#product) - Cada producto debe tener una categoría de impuesto
    3. **Asignarse opcionalmente a terceros** mediante [Categoría de Impuestos de Terceros](../setup/business-partner-tax-category.md) para restringir los impuestos aplicables a clientes o proveedores específicos


## Traducción

La solapa Traducción le permite proporcionar nombres y descripciones traducidos para las categorías de impuesto en varios idiomas. Esto resulta útil para organizaciones multinacionales en las que los usuarios trabajan en distintos idiomas.

Cuando un usuario inicia sesión con una preferencia de idioma específica, verá los nombres de las categorías de impuesto en su idioma, lo que garantiza claridad y reduce la confusión al seleccionar categorías de impuesto durante la introducción de transacciones.

## Casos de uso comunes

### Cuándo crear múltiples categorías de impuesto

Debe crear diferentes categorías de impuesto cuando:

- **Los productos tienen diferentes tipos impositivos**: estándar (21%), reducido (10%), superreducido (4%) o exento (0%)
- **Se aplican diferentes tipos de impuestos**: IVA, impuesto sobre ventas, impuestos especiales o gravámenes especiales
- **Existen reglas fiscales específicas del sector**: transacciones inmobiliarias, régimen agrario, servicios financieros
- **Ventas transfronterizas**: productos nacionales vs. de exportación (sujetos a impuesto vs. tipo cero)
- **Requisitos normativos**: separar artículos declarables vs. no declarables para las autoridades fiscales (p. ej., SII en España)

### Dónde se utilizan las categorías de impuesto

Las categorías de impuesto aparecen en todo el sistema:

| Ventana/Proceso | Uso |
|----------------|-------|
| [Producto](../../../master-data-management/master-data.md#product) | Cada producto debe tener asignada una categoría de impuesto |
| [Rango impuesto](../setup/tax-rate.md) | Cada tipo impositivo debe estar vinculado al menos a una categoría de impuesto |
| [Categoría de Impuestos de Terceros](./business-partner-tax-category.md) | Asignación opcional de categoría de impuesto para restringir los impuestos aplicables a clientes/proveedores específicos |
| Pedidos de venta/Facturas | Las categorías de impuesto determinan qué tipos impositivos están disponibles para su selección |
| Pedidos de compra/Facturas | Las categorías de impuesto filtran los impuestos aplicables en función de la configuración del producto y del proveedor |
| [Concepto contable](../setup/gl-item.md) | Requerido al habilitar conceptos contables para facturas financieras con implicaciones fiscales |

### Ejemplo

Una empresa vende distintos tipos de artículos con diferentes tipos impositivos:

| Tipo de artículo | Rango impuesto | Categoría de Impuesto |
|-------------|-----------|--------------|
| Electrónica | 21%       | IVA estándar |
| Alimentación | 10%       | IVA reducido  |
| Libros       | 0%        | Exento       |

**Pasos de configuración:**

1. **Crear** tres categorías de impuesto:
    - Nombre: "IVA estándar" → Para productos con tipo impositivo estándar
    - Nombre: "IVA reducido" → Para productos con tipo impositivo reducido
    - Nombre: "Exento" → Para productos exentos de impuestos

2. **Configurar tipos impositivos** en la ventana [Rango impuesto](../setup/tax-rate.md):
    - Crear un tipo impositivo del 21% y vincularlo a la categoría "IVA estándar"
    - Crear un tipo impositivo del 10% y vincularlo a la categoría "IVA reducido"
    - Crear un tipo impositivo del 0% y vincularlo a la categoría "Exento"

3. **Asignar productos** a categorías en la ventana [Producto](../../../master-data-management/master-data.md#product):
    - Producto "Portátil" → Categoría de Impuesto: "IVA estándar"
    - Producto "Pan" → Categoría de Impuesto: "IVA reducido"
    - Producto "Novela" → Categoría de Impuesto: "Exento"

**Resultado en transacciones:**

Al crear un pedido de venta o una factura:

- Añadir "Portátil" → Etendo aplica automáticamente un impuesto del 21% (de la categoría IVA estándar)
- Añadir "Pan" → Etendo aplica automáticamente un impuesto del 10% (de la categoría IVA reducido)
- Añadir "Novela" → Etendo aplica automáticamente un impuesto del 0% (de la categoría Exento)

Esta estructura ayuda a centralizar la lógica fiscal, garantiza un cálculo de impuestos preciso y simplifica el mantenimiento fiscal en todo el sistema. Si cambian los tipos impositivos (p. ej., el IVA estándar aumenta del 21% al 23%), solo necesita actualizar la configuración del tipo impositivo: todos los productos vinculados a esa categoría utilizarán automáticamente el nuevo tipo.


---

Este trabajo es una obra derivada de [Categoría de Impuesto](https://wiki.openbravo.com/wiki/Tax_Category){target="\_blank"} por [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, usado bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.