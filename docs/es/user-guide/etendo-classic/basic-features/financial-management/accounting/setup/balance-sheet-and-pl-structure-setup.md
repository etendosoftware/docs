---
title: Configuración de la estructura del Balance y PyG
tags:
    - Balance
    - Estructura de PyG
    - Informes
    - Archivo CSV
    - Contabilidad
---

# Configuración de la estructura del Balance y PyG

:material-menu: `Aplicación` > `Gestión Financiera` > `Contabilidad` > `Configuración` > `Configuración de la estructura del Balance y PyG`

## Visión general

La Configuración de la estructura del Balance y PyG permite a los usuarios definir cómo Etendo genera sus dos principales **informes financieros**:

- Balance
- Pérdidas y Ganancias (PyG)

Esta configuración determina qué cuentas aparecen en cada informe y cómo se agrupan y calculan. Una vez configurados, estos informes pueden generarse desde la ventana [Balance y PyG Estructura Avanzada](../analysis-tools.md#balance-sheet-and-pl-structure-advanced).

Un punto clave es que ambos informes se construyen en base al **[Árbol de cuentas de la organización](./account-tree.md)** (Plan de cuentas). Por lo tanto, el árbol de cuentas debe estar correctamente estructurado para obtener informes financieros significativos y precisos.

La estructura del Balance y PyG depende completamente del Árbol de cuentas:

- **Árboles de cuentas importados** (archivos CSV o datos de referencia):

    Etendo proporciona planes de cuentas localizados, como el Plan General Contable español, ya estructurados para producir informes de Balance y PyG conformes.

- **Creados manualmente**:
    El usuario debe diseñar cuidadosamente la jerarquía, ya que la estructura del informe refleja directamente la forma en que las cuentas están organizadas en el árbol.

## Cabecera

Cada registro creado en esta ventana representa un **informe financiero**. Al definir un informe, el [tipo de organización](../../../general-setup/enterprise-model/organization-type.md) seleccionado es crucial porque determina el alcance de los datos financieros:

- Si la organización seleccionada es una **Legal con Contabilidad** que tiene otras organizaciones por debajo, la información financiera proporcionada por los informes será un **roll-up** de la información financiera de las organizaciones que pertenecen a ella. Roll-up significa que produce un Balance **agregado**. Para obtener un Balance **consolidado**, las transacciones entre organizaciones (transacciones intercompany) deben eliminarse del informe resultante.
- Lo mismo aplica en el caso de organizaciones que son de **Tipo de Organización** y que tienen otras organizaciones por debajo compartiendo la misma configuración de esquema contable y, por lo tanto, el mismo árbol de cuentas.
- Si la organización seleccionada es una **organización genérica** que pertenece a una Legal con Contabilidad, la información financiera proporcionada por los informes será únicamente la información financiera de esa organización.

![alt text](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/set-up/balance-sheet-and-pl-structure-setup/balance-sheet-and-pl-structure-setup-1.png)

Campos a tener en cuenta en esta ventana:

- **Esquema contable**: del cual se requiere la información contable.
- **Nombre del informe**: p. ej., Balance.
- **Tipo informe**: las opciones disponibles son:
    - **Punto en el tiempo**: este tipo se utiliza para informes como el Balance, ya que el saldo de las cuentas debe referirse a una fecha específica.
    - **Periódico**: este tipo se utiliza para informes como PyG, ya que el saldo de las cuentas utilizadas debe referirse a un período de tiempo específico, por ejemplo un mes, un trimestre, un año, etc.
- **Cuadrado**: este indicador debe activarse siempre que el informe deba lanzarse solo para tipos de organización **Legal con Contabilidad**, ya que ese es el nivel empresarial en el que se garantiza el equilibrio contable.
- **Activo**: este indicador debe marcarse como activo para el informe de Balance.

### Categoría de agrupación

La pestaña **Categoría de agrupación** permite a los usuarios definir secciones dentro del informe. Cada categoría de agrupación crea un salto de página, ayudando a organizar el informe en secciones claras.

![alt text](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/set-up/balance-sheet-and-pl-structure-setup/balance-sheet-and-pl-structure-setup-2.png)

#### Nodos

Desde la subpestaña **Nodos** es posible definir la información mostrada en el informe.

![alt text](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/set-up/balance-sheet-and-pl-structure-setup/balance-sheet-and-pl-structure-setup-3.png)

Un nodo de informe se define por:

- El **Nombre** del nodo.
- La **Cuenta Contable** que se va a mostrar en el informe.
    
    !!! info
        Los elementos de cuenta seleccionados aquí suelen ser **tipos de nivel de elemento de encabezado**, por lo tanto, el saldo calculado del nodo tendrá en cuenta y mostrará el saldo de todos los elementos de cuenta de otros tipos que estén por debajo de él.

## Configuración de la estructura del Balance - Ejemplo

Esta configuración define cómo Etendo genera un **Balance** mostrando la posición financiera de la empresa en una fecha específica.

- **Nombre del informe**: Balance
- **Tipo informe**: Punto en el tiempo, ya que los saldos se calculan para una fecha específica.
- **Cuadrado**: Sí, ya que el Balance debe estar cuadrado a nivel de Legal con Contabilidad.

    - **Categoría de agrupación**: Balance

        - **Nodos**: Activo, vinculado al encabezado del árbol de cuentas que agrupa todas las cuentas de activo.
        - **Nodos**: Pasivo y Patrimonio neto, vinculado al encabezado que agrupa las cuentas de pasivo y patrimonio.

!!! note
    Etendo calcula cada nodo **sumando todas las cuentas** ubicadas bajo el encabezado correspondiente del árbol de cuentas. Un [Árbol de cuentas](./account-tree.md#element-value-tab) correctamente estructurado es esencial para obtener resultados precisos.

## Configuración de la estructura de Pérdidas y Ganancias (PyG) - Ejemplo

Esta configuración define cómo Etendo genera un **informe de Pérdidas y Ganancias** para un período seleccionado.

- **Tipo informe**: Periódico, ya que los ingresos y los gastos se calculan a lo largo de un rango de tiempo.
- **Cuadrado**: No, ya que este informe no representa un balance en una fecha específica.
    - **Categoría de agrupación**: Pérdidas y Ganancias
        - **Nodos**: Pérdidas y Ganancias, vinculado al encabezado del árbol de cuentas que agrupa todas las cuentas de ingresos y gastos.

!!! note
    Etendo calcula el resultado comparando los ingresos totales y los gastos totales del período seleccionado.
    El nodo anterior debe ser un elemento del Árbol de cuentas correctamente configurado. Para más información, visite [Árbol de cuentas](./account-tree.md).

!!! info
    Para más información sobre los informes de estructura de Balance y PyG visite: [Balance y PyG Estructura Avanzada](../../accounting/analysis-tools.md#balance-sheet-and-pl-structure-advanced). 

---

Este trabajo es una obra derivada de [Configuración de la estructura del Balance y PyG](https://wiki.openbravo.com/wiki/Balance_sheet_and_P%26L_structure_Setup){target="\_blank"} por [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.