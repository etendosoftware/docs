---
title: Calendario anual y periodos
tags:
    - Fiscal
    - Calendar
    - Gestión Financiera
    - Configuración
    - Contabilidad
---

# Calendario anual y periodos

:material-menu: `Aplicación` > `Gestión Financiera` > `Contabilidad` > `Configuración` > `Calendario anual y periodos`

## Visión general

Las organizaciones de tipo **Entidad Legal con contabilidad** deben tener asignado un calendario fiscal. Otros tipos de organización pueden heredar el calendario fiscal de su organización padre.

Un calendario fiscal define los **Ejercicio** y sus **Periodo** para garantizar una contabilidad precisa y un control adecuado del ciclo financiero. Cada organización solo puede tener asignado **un único calendario fiscal**, que se utiliza para contabilizar transacciones y gestionar la apertura y el cierre de periodos.

### Ventana de calendario fiscal

La **ventana de calendario fiscal** permite al usuario crear y mantener el calendario fiscal de la organización. Cada organización que requiera un calendario necesita tener asignado un calendario y **solo uno**, por lo que se conoce claramente qué calendario se va a utilizar al contabilizar transacciones y al abrir y cerrar el ciclo contable.

![fiscal calendar 1](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/set-up/fiscal-calendar1.png)

- Al crear un calendario, Etendo propone `*` como la organización por defecto:

    - Mantener `*` significa que el calendario se define a **nivel de cliente** y puede ser utilizado por todas las organizaciones bajo ese cliente.

    - Cambiarlo a una organización específica significa que el calendario estará disponible **solo para esa organización**.

Una vez creado el calendario, debe vincularse a la organización correspondiente en la ventana [Organización](../../../general-setup/enterprise-model/organization.md), mediante:

- Habilitar la casilla de verificación **Permitir Control de Periodos**.

- Seleccionar el tipo **organizaciones legales con contabilidad**.

![fiscal calendar 2](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/set-up/fiscal-calendar2.png)

### Ejercicio

La solapa **Ejercicio** se utiliza para definir tantos **Ejercicio** como sea necesario dentro de un calendario.

![fiscal calendar 5](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/set-up/fiscal-calendar5.png)

- Un ejercicio fiscal normalmente cubre **12 meses consecutivos**.

- Utilice el botón **Crear periodos** para generar automáticamente:

    - **12 periodos estándar del calendario** (1 de enero – 31 de diciembre).

    - Un **13.º periodo de ajuste** opcional, fechado el último día del último periodo estándar (p. ej., 31-12-2025), utilizado para ajustes contables mediante **Asientos manuales**.

![fiscal calendar 3](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/set-up/fiscal-calendar3.png)

Una vez creados, todos los periodos deben ser **abiertos** en la ventana [Abrir/Cerrar periodos](#abrircerrar-periodos).

!!!info
    Los periodos del calendario fiscal de una organización pueden revisarse en la solapa **Control de Periodos** de la ventana [Organización](../../../general-setup/enterprise-model/organization.md). 

!!!note
    -   Los **periodos estándar del calendario** se abren para **cada Categoría de documento**, lo que significa que Etendo permite al usuario contabilizar cualquier tipo de documento en el libro mayor dentro de un periodo estándar del calendario abierto.
    -   El **Periodo de ajuste** solo se abre para la categoría de documento **Asientos manuales**, lo que significa que Etendo permite contabilizar únicamente asientos manuales dentro del periodo de ajuste.

### **Periodo**

La solapa **Periodo** lista todos los periodos de un ejercicio. Además, es posible crear **manualmente** los periodos contables de un ejercicio. Esa acción requiere introducir cierta información:

![fiscal calendar 4](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/set-up/fiscal-calendar4.png)

Los campos a tener en cuenta son:

-   Un **Número de periodo** consecutivo: este número se utilizará posteriormente para abrir/cerrar periodos contables consecutivos a la vez.
-   Un **nombre del periodo**.
-   La **Fecha de inicio** del periodo.
-   La **Fecha final** del periodo.
-   El **Tipo de periodo** como tipo de periodo estándar del calendario o periodo de ajuste, según sea necesario.

!!!note
    Los valores de un Periodo también pueden modificarse manualmente, pero solo mientras este Periodo esté en estado **Nunca abierto**; una vez que se haya abierto, ya no será posible.

Etendo comprueba si ya existe otro periodo con la misma fecha de inicio y fecha final registrado en el sistema, y también comprueba si la fecha de un periodo se solapa con la fecha de otro periodo.

Por último, un ejercicio puede:

-   ser **Cerrado**
-   y ser **reabierto**

Ambas acciones se realizan en la ventana [Cierre de año](../../accounting/transactions.md#end-year-close).

---

Este trabajo es una obra derivada de [Calendario anual y periodos](https://wiki.openbravo.com/wiki/Fiscal_Calendar){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.