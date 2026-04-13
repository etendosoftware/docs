---
tags:
    - How to
    - Esquema contable
    - Financial Management
    - Accounting Setup
---

## Visión general

El **Esquema contable** en Etendo define cómo se registran y estructuran las transacciones financieras de una organización. Cada organización debe estar vinculada al menos a un libro mayor, aunque se pueden asignar varios libros si es necesario, por ejemplo, al utilizar diferentes monedas o al heredar un libro mayor de una organización padre.

Antes de configurar un libro mayor, se recomienda crear primero el [Árbol de cuentas](../basic-features/financial-management/accounting/setup/account-tree.md) que se utilizará para contabilizar transacciones. Una vez hecho esto, se puede crear una nueva configuración de libro mayor y vincularla a la organización.

## Esquema contable

Desde la ventana **Esquema contable**, el proceso de configuración implica:

![alt text](../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/set-up/gl-configuration6.png)

-   Seleccionar la **Organización** para la cual el libro mayor va a estar disponible.
-   Introducir el **Nombre de la configuración del Esquema contable**, por ejemplo, Libro mayor general EUR.  
-   Seleccionar la **Moneda** que se utilizará para contabilizar transacciones en el libro mayor.  
-   Seleccionar la casilla **Permitir negativos** en caso de que se permita la contabilización en negativo, tal y como ya se ha descrito.

!!!info
    Es posible que una organización requiera el mismo árbol de cuentas pero diferentes libros mayores, uno de ellos en **USD** y el otro en **EUR**.

!!! info
    Dado que cada vez que se contabiliza en el libro mayor una transacción de cualquier tipo, se contabiliza en los **dos libros mayores** configurados para la Organización.

Una vez hecho esto, el libro mayor recién creado debe vincularse en el campo Libros mayores desde la ventana [Organización](../basic-features/general-setup/enterprise-model/organization.md). 

Desde la ventana [Esquema contable](../basic-features/financial-management/accounting/setup/general-ledger-configuration.md), los pasos restantes para configurar correctamente el libro mayor son:

- Configurar [Dimensiones](../basic-features/financial-management/accounting/setup/general-ledger-configuration.md#dimension-tab) desde la solapa Dimensiones para añadir las dimensiones obligatorias que se listan a continuación:

    -   Crear un nuevo registro e introducir **Organización** en el campo **Nombre**.
    -   Seleccionar **Organización** en el campo **Tipo**.
    -   Seleccionar {Su Organización} en el campo **Organización de la transacción**.
    -   Seleccionar la casilla **Cuadrado** y la casilla **Obligatorio**.
    -   Crear un nuevo registro e introducir **Cuenta** en el campo **Nombre**.
    -   Seleccionar **Cuenta** en el campo **Tipo**.
    -   Seleccionar el **Árbol de cuentas** ya existente en el campo **Árbol de cuentas**.
    -   Seleccionar la casilla **Obligatorio**.

    También se pueden crear dimensiones no obligatorias, tal y como se describe a continuación, en caso de que sea necesario guardar información adicional como el tercero o el proyecto al contabilizar asientos o cualquier tipo de transacción:

    - Crear un nuevo registro e introducir **Terceros** en el campo **Nombre**.
    - Seleccionar **Terceros** en el campo **Tipo**.
    - Crear un nuevo registro e introducir **Proyecto** en el campo **Nombre**.
    - Seleccionar **Proyecto** en el campo **Tipo**.

    !!!info
        Para revisar las tablas que van a generar contabilidad, visite la solapa [Tablas a contabilizar](../basic-features/financial-management/accounting/setup/general-ledger-configuration.md#active-tables-tab). Es posible habilitar la contabilidad para aquellas que no estén activas para contabilización.


- Configurar las [Contabilidad general](../basic-features/financial-management/accounting/setup/general-ledger-configuration.md#general-accounts) obligatorias desde la solapa Contabilidad general, así como las cuentas a utilizar en caso de Cuadre transitorio o Error transitorio, entre otras. Esas cuentas deben haberse creado previamente tal y como se describe en la sección [Árbol de cuentas](../basic-features/financial-management/accounting/setup/account-tree.md).

- Establecer las [Cuentas por defecto](../basic-features/financial-management/accounting/setup/general-ledger-configuration.md#defaults-tab) desde la solapa Por defecto, que deben copiarse a otras solapas de configuración contable como:

    -   la solapa Contabilidad de producto
    -   la solapa Configuración contable de cuenta financiera
    -   la solapa Contabilidad de tipo impositivo
    -   etc.

!!! info
    Para más información visite [Esquema contable](../basic-features/financial-management/accounting/setup/general-ledger-configuration.md).

---

Este trabajo es una obra derivada de [General Ledger Configuration](https://wiki.openbravo.com/wiki/General_Ledger_Configuration){target="\_blank"} de [Wiki de Openbravo](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.