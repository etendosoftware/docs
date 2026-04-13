---
tags:
    - Validación de la estructura de cuentas
    - Subcuenta
    - Árbol de cuentas
---

# Validación de la estructura de cuentas

:octicons-package-16: Paquete Java: `com.etendoerp.account.structure.validation`

## Visión general

Este módulo ayuda a prevenir errores comunes de configuración al crear o modificar subcuentas en el Árbol de cuentas. Valida la estructura y la configuración para evitar discrepancias en informes financieros como la Cuenta de resultados o el Balance de situación.

El módulo incluye la preferencia de sistema **"Habilitar validaciones de subcuentas"**, que está configurada como `SÍ` de forma predeterminada, garantizando que la validación esté activa desde el momento en que se instala el módulo.

## Validaciones realizadas

El módulo aplica las siguientes validaciones:

- Verifica que la cuenta tenga un padre a nivel de **Separar** o **Cuenta**.
- Comprueba que la cuenta tenga **un dígito más que su cuenta padre**.
- Asegura que el **Tipo de cuenta** (Activo, Pasivo, Patrimonio neto, Ingresos, Gastos, Memo) y la **Naturaleza de la cuenta (crédito/débito)** coincidan con los de su padre a nivel de Separar.

Si alguna validación falla, el sistema impide guardar la cuenta, evitando posibles errores en los informes financieros.

Estas validaciones se activan no solo al crear o modificar cuentas, sino también al **mover registros en la vista de árbol**, garantizando la consistencia de los datos incluso al reorganizar la estructura de cuentas.

### Exclusión de la validación

La casilla de verificación **"Excluir de la validación de subcuentas"** permite flexibilidad en la configuración de la estructura de cuentas. Al establecer este campo en **SÍ** para cuentas específicas, dichas cuentas quedarán excluidas de todas las validaciones mencionadas anteriormente. Esto resulta especialmente útil para cuentas que requieren una estructura o configuración diferente y que no necesitan seguir las reglas estándar de validación.

![Pestaña Valor del elemento - Excluir de la validación de subcuentas](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/account-structure-validation/account-structure-validation.png)

!!! info
    Para más información sobre el Árbol de cuentas, visita [Árbol de cuentas - Pestaña Valor del elemento](../../../basic-features/financial-management/accounting/setup/account-tree.md#element-value-tab).

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.

---