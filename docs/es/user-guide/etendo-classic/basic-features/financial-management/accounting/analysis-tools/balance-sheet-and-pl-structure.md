---
tags:
  - Etendo Classic
  - Financial Management
  - Accounting
  - Balance Sheet
  - Financial Reports
---

# Balance de Situación y Estructura de P&L

:material-menu: `Aplicación` > `Gestión Financiera` > `Contabilidad` > `Herramientas de Análisis` > `Balance de Situación y Estructura de P&L`

## Visión General

El motor de informes de Balance de Situación y Estructura de P&L permite al usuario generar el Balance de Situación y el Estado de Pérdidas y Ganancias, los cuales deben configurarse previamente.

El informe de Balance de Situación es un resumen cuantitativo de la situación financiera de una organización en un momento específico. Este informe muestra un resumen de los saldos de activos y pasivos y patrimonio neto.

El informe de Pérdidas y Ganancias muestra los ingresos, gastos y el beneficio neto de una organización.

Estos informes deben configurarse antes de generarse en la ventana [Configuración de Balance de Situación y Estructura de P&L](../accounting/setup/balance-sheet-and-pl-structure-setup.md).

## Cabecera

![](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/balance-sheet-and-pl-structure-1.png)

Como se muestra en la imagen anterior, los datos a completar son:

- El **Libro Mayor** del que se debe obtener la información contable.
- El **Informe Contable** a generar. Este campo lista los informes creados y configurados en la ventana [Configuración de Balance de Situación y Estructura de P&L](./setup/balance-sheet-and-pl-structure-setup.md).
- La **Organización**. Este campo lista la organización para la que se ha configurado el informe en la ventana de configuración de Balance de Situación y Estructura de P&L.

    - Si el informe está configurado para un tipo de organización "Entidad Legal con Contabilidad", solo se muestra esa organización en este campo. Los saldos de cuentas mostrados en el informe serán una consolidación de las organizaciones que le pertenecen, si las hubiera.
    - Si el informe está configurado para un tipo de organización "Genérica", las organizaciones mostradas en este campo son al menos la organización genérica y el tipo de organización de entidad legal con contabilidad al que pertenece, todas ellas vinculadas al libro mayor seleccionado.

- El **Nivel de Cuenta**, que define hasta qué nivel de detalle se mostrará en el informe. Las opciones disponibles son las mismas que los niveles de elementos del árbol de cuentas:

    - Título: solo se muestran los elementos de "título", incluyendo información contable resumida hasta ese nivel.
        - Cuenta: en este caso se muestran los elementos de "título" y "cuenta", incluyendo información contable resumida hasta cada uno de esos niveles.
            - Desglose: en este caso se muestran los elementos de "título", "cuenta" y "desglose", incluyendo información contable resumida hasta cada uno de esos niveles.
                - Subcuenta: en este caso se muestran los elementos de "título", "cuenta", "desglose" y "subcuenta", incluyendo información contable resumida hasta cada uno de esos niveles. Es importante recordar que los asientos contables se registran a nivel de subcuenta.

- La casilla **Mostrar solo cuentas con valor** permite al usuario ver que el informe no muestra elementos de cuenta con saldo de importe *cero*, pero sí los elementos definidos como Título, que siempre se muestran independientemente de su importe.
- La casilla **Mostrar Códigos de Cuenta** permite al usuario mostrar u ocultar la Clave de Búsqueda del Nivel de Elemento.

En la sección **Filtros Primarios**, es posible especificar:

- Un **Número de página inicial** para el informe, en caso de que deba integrarse. Resulta útil cuando el informe debe incorporarse como parte de un informe o documento más extenso.
- Un **Año** y un **Año de Referencia** para obtener un informe comparativo, normalmente entre el "Año" actual y el anterior introducido como "Año de Referencia". El informe dispone de un filtro **Comparar con**, de modo que puede generarse solo para un año concreto sin necesidad de compararlo con otro.
- Por último, se pueden introducir los filtros **A Fecha** (Fecha Hasta) y **A Fecha de Referencia** (Fecha Desde). Estos filtros se comportan de manera diferente según el informe:
    -   En el caso del informe de Balance de Situación, se puede introducir un valor de "Fecha Hasta" para obtener que el informe muestre información sobre el saldo de cuentas hasta esa fecha.
    -   En el caso del informe de P&L, se pueden introducir una "Fecha Hasta" y una "Fecha Desde" para que el informe muestre información contable dentro de ese periodo de tiempo (un año, un trimestre, un mes, etc.).

**Ejemplo de Informe de Balance de Situación**

!!! info
    Tenga en cuenta que la palabra "Provisional" (en\_US) \[o "Provisional" (es\_ES)\] se muestra siempre que al menos uno de los periodos para los que se ha generado el informe no esté cerrado aún.

![](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/balance-sheet-report-1.png)

**Ejemplo de Informe de P&L**
 
![](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/profit-and-loss-report-1.png)

---

Este trabajo es una obra derivada de [Financial Management](http://wiki.openbravo.com/wiki/Financial_Management){target="\_blank"} por [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.
