---
tags:
  - Etendo Classic
  - Financial Management
  - Matching Algorithm
  - Bank Reconciliation
  - Receivables and Payables
---

# Algoritmo de Reconciliación { #matching-algorithm }

:material-menu: `Application` > `Financial Management` > `Receivables and Payables` > `Setup` > `Matching Algorithm`

## Descripción general { #overview }

Etendo permite al usuario conciliar las transacciones de depósito y retirada de una cuenta financiera de dos maneras:

1.  **Automáticamente**, asociando las líneas del extracto bancario (importadas o no) con las transacciones de la cuenta financiera.  
    En este caso, es necesario un algoritmo de reconciliación para guiar el proceso de asociación.
2.  **Manualmente**, utilizando el botón de proceso Conciliación manual de la ventana Cuenta financiera.  
    Esta forma de conciliación no requiere un algoritmo de reconciliación.

Etendo incluye de forma predeterminada el algoritmo de reconciliación "**Estándar**", que puede consultarse y configurarse en la ventana **Algoritmo de Reconciliación**.

## Algoritmo de Reconciliación { #matching-algorithm_1 }

La ventana Algoritmo de Reconciliación lista y permite al usuario configurar el/los algoritmo/s que se utilizarán al asociar las líneas del extracto bancario con las transacciones de la cuenta financiera.

Como se muestra en la imagen anterior, el algoritmo de reconciliación "**Estándar**" dispone de tres casillas de verificación que permiten al usuario configurar el proceso de asociación de transacciones de la cuenta financiera:

-   **Asociar nombre del tercero:** Esta opción obtiene una coincidencia sólida si el nombre del tercero de la línea del extracto bancario coincide con el nombre del tercero de la transacción de la cuenta financiera.
-   **Asociar referencia:** Esta opción obtiene una coincidencia sólida si la referencia de la línea del extracto bancario coincide con la referencia de la transacción de la cuenta financiera.
-   **Asociar fecha de transacción:** Esta opción obtiene una coincidencia sólida si el nombre del tercero de la línea del extracto bancario coincide con el nombre del tercero de la transacción de la cuenta financiera.

!!! info
    Es posible seleccionar todas las verificaciones anteriores a la vez o solo algunas de ellas para configurar cómo obtener una coincidencia sólida.

---

This work is a derivative of [Financial Management](http://wiki.openbravo.com/wiki/Financial_Management){target="_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="_blank"} by [Etendo](https://etendo.software){target="_blank"}.
