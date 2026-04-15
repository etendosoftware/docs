---
title: Combinación de cuentas
tags:
    - Cuenta
    - Combinación
    - Gestión Financiera
    - Configuración
    - Contabilidad
---

# Combinación de cuentas

:material-menu: `Aplicación` > `Gestión Financiera` > `Contabilidad` > `Configuración` > `Combinación de cuentas`

## Visión general

Una combinación de cuentas representa **una cuenta del Esquema contable tal y como la utiliza una organización específica**. Esta ventana le permite revisar qué cuentas del esquema contable están disponibles para una organización y ver detalles básicos sobre cada combinación de cuentas.

El propósito principal de esta ventana es **ver y gestionar, de una sola vez, estas combinaciones válidas de dimensiones contables** para que Etendo sepa exactamente dónde y cómo contabilizar las transacciones financieras.

![](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/set-up/account-combination/account-combination-1.png)


!!!info
    El usuario no puede crear combinaciones de cuentas directamente desde esta ventana. Se generan automáticamente cuando crea cuentas (o subcuentas) en un Árbol de cuentas para un Esquema contable. Para añadir o editar las cuentas subyacentes, utilice la ventana [Árbol de cuentas](account-tree.md).

!!! warning
    La ventana **Combinación de cuentas** permite al usuario eliminar cuentas. Esta acción implica que se eliminan de esta ventana, pero no de la ventana Árbol de cuentas.

## Cabecera

En esta ventana, el usuario puede ver todas las combinaciones de cuentas para el *Esquema contable* y la *Organización* seleccionados, filtrar y buscar combinaciones para encontrar cuentas específicas rápidamente.

![](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/set-up/account-combination/account-combination-2.png)

Campos a tener en cuenta:

- **Esquema contable**: el esquema contable al que pertenece la cuenta.
- **Organización**: la organización que utilizará la cuenta.
- **Cuenta**: la cuenta (del Árbol de cuentas) asociada a esta combinación.
- **Activo**: si esta combinación de cuentas está habilitada para contabilizar.
- **Totalmente correcta**: esta casilla indica que están presentes todos los elementos requeridos para una combinación de cuentas.

!!!note

    - Una cuenta en el Árbol de cuentas puede producir múltiples combinaciones de cuentas si la cuenta se utiliza en varias organizaciones o esquemas contables.
    - Las combinaciones de cuentas son necesarias para contabilizar: si falta una combinación necesaria, cree o ajuste la cuenta en el Árbol de cuentas y la combinación se creará automáticamente.
    - Utilice esta ventana para verificar que una organización tiene las cuentas correctas del esquema contable antes de contabilizar transacciones.

## Ejemplo

Revisemos un ejemplo para entender mejor esta funcionalidad.  
Suponga que una empresa tiene la siguiente configuración:

- **Esquema contable:** F&B International Group US/A/US Dollar  
- **Organización:**  
    - F&B International Group 1  
    - F&B International Group 2 
- **Árbol de cuentas:**  
    - **4100 – Ingresos - Producto**

Cuando se crea la cuenta **Ingresos - Producto** en el Árbol de cuentas, Etendo genera automáticamente **Combinación de cuentas** para cada organización que utiliza el esquema contable:

| Esquema contable | Organización | Cuenta | Activo |
|---------------|-------------|---------|--------|
| F&B International Group US/A/US Dollar   | F&B International Group 1            | 4100 – Ingresos - Producto | Sí |
| F&B International Group US/A/US Dollar   | F&B International Group 2      | 4100 – Ingresos - Producto | Sí |

Cada fila representa una **combinación de cuentas diferente**, aunque hagan referencia a la misma cuenta en el Árbol de cuentas.

### Contabilizar una transacción

Cuando se contabiliza una factura de venta para **F&B International Group 2**, Etendo:

1. Identifica la **Organización** de la transacción (F&B International Group 2)
2. Utiliza el Esquema contable **F&B International Group US/A/US Dollar**
3. Busca una **combinación de cuentas totalmente correcta** que incluya:
    - Esquema contable F&B International Group US/A/US Dollar
    - F&B International Group 2
    - Cuenta Ingresos - Producto

Si la combinación de cuentas correspondiente existe y está activa, la transacción se contabiliza correctamente.

### Combinaciones faltantes

Si la cuenta **Ingresos - Producto** no se definió correctamente para **F&B International Group 2** en el Árbol de cuentas:

- La combinación de cuentas requerida **no existe**
- La transacción **no se puede contabilizar**
- El usuario debe actualizar el **Árbol de cuentas**
- Una vez corregido, Etendo **crea la combinación de cuentas faltante**

### Por qué son importantes las combinaciones de cuentas

Este ejemplo muestra cómo las combinaciones de cuentas actúan como un **puente** entre:

- La estructura de cuentas (Árbol de cuentas)
- La estructura organizativa
- La contabilización de transacciones financieras

Al validar las combinaciones de cuentas con antelación, Etendo garantiza que las transacciones siempre se contabilicen en la **cuenta y organización correctas**, manteniendo la precisión y la consistencia en los informes financieros.

Como conclusión, la ventana Combinación de cuentas define la identidad contable de una transacción. Indica a Etendo qué cuenta y qué dimensiones analíticas deben utilizarse conjuntamente al contabilizar en el esquema contable, garantizando precisión, consistencia e informes financieros significativos.

---
Este trabajo es una obra derivada de [Combinación de cuentas](https://wiki.openbravo.com/wiki/Account_Combination){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.