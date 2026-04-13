---
title: Categoría de LM
tags:
    - LM
    - Categoría
    - Gestión Financiera
    - Configuración
    - Contabilidad
---

# Categoría de LM

:material-menu: `Aplicación` > `Gestión Financiera` > `Contabilidad` > `Configuración` > `Categoría de LM`

## Visión general

En esta ventana, el usuario puede **ver, crear y gestionar Categorías de LM utilizadas para clasificar los asientos contables en el Libro Mayor**.

![](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/set-up/gl-category/gl-category.png)

Las Categorías de LM (Libro Mayor) actúan como **identificadores de clasificación que posteriormente se asignan a** [Tipo de documento](./document-type.md). Una vez que una Categoría de LM se vincula a un Tipo de documento, **todos los asientos contables generados a partir de ese documento se categorizan automáticamente durante la contabilización**, garantizando una clasificación coherente sin intervención manual.

Estas categorías pueden aplicarse a diarios generados a partir de documentos, diarios introducidos manualmente o diarios importados, y se utilizan principalmente para **informes, análisis y agrupación de líneas del libro mayor a través de diferentes orígenes**.

El propósito principal de la ventana Categoría de LM es **definir un conjunto controlado de clasificaciones contables** que estandarice cómo se agrupan y analizan los apuntes del libro mayor.

Las Categorías de LM se crean normalmente cuando:

- Un nuevo **Tipo de documento** requiere una clasificación contable diferenciada.
- Existe la necesidad de **diferenciar los asientos contables** en los informes financieros (por ejemplo, separar diarios operativos de asientos de ajuste o de cierre).
- Los diarios importados o creados manualmente deben estar **claramente identificados por su origen o propósito empresarial**.

Una vez creadas, las Categorías de LM se asignan en la ventana **Tipo de documento**. A partir de ese momento, cada documento contabilizado usando ese Tipo de documento aplicará automáticamente la Categoría de LM correspondiente a sus asientos contables. Se desaconseja crear categorías innecesarias o excesivamente granulares, ya que las categorías están pensadas para representar **clasificaciones estables y de alto nivel** en lugar de detalles transaccionales.

## Cabecera

![](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/set-up/gl-category/gl-category2.png)

Campos a tener en cuenta:

- **Entidad**: La entidad a la que pertenece esta categoría.
- **Organización**: La organización que utilizará la categoría.
- **Nombre**: Un identificador descriptivo del registro que se utiliza como opción de búsqueda por defecto. Tiene una longitud de hasta 60 caracteres.
- **Descripción**: Información adicional sobre la categoría.
- **Activo**: Un indicador que señala si este registro está disponible para su uso o desactivado.

    !!!info
        Es posible desactivar categorías que ya no desea que los usuarios seleccionen; las contabilizaciones existentes permanecen sin cambios.

- **Tipo de categoría**: Indica el origen del diario para esta categoría. Los diarios pueden generarse a partir de un documento, introducirse manualmente o importarse.
- **Valor por defecto**: Cuando está marcado, esta categoría se selecciona por defecto para los nuevos registros que utilicen esta categoría. Esta opción acelera la introducción de datos cuando sea necesario.

## Ejemplo

Seleccione la opción de crear nuevo, rellene los campos correspondientes y guárdelo.

![](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/set-up/gl-category/gl-category3.png)

La categoría creada está disponible para su uso en asientos de diario, importaciones y procesamiento de documentos.

![](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/set-up/gl-category/gl-category4.png)


---
Este trabajo es una obra derivada de [Categoría de LM](https://wiki.openbravo.com/wiki/G/L_Category){target="\_blank"} de [Wiki de Openbravo](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.