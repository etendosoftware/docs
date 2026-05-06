---
tags:
  - Etendo Classic
  - Financial Management
  - Payment Run
  - Payment Execution
  - Receivables and Payables
---

# Remesa de pagos

:material-menu: `Application` > `Financial Management` > `Receivables and Payables` > `Analysis Tools` > `Payment Run`

## Descripción general

La ventana Remesa de pagos es una ventana de solo lectura que muestra información relevante de cada remesa de pagos ejecutada dentro de una organización.

Una remesa de pagos puede contener un único pago o varios pagos agrupados y ejecutados conjuntamente.

Es posible consultar el estado y el resultado de la remesa de pagos, así como el resultado y el mensaje de cada pago individual dentro de cada remesa.

## Remesa de pagos

En esta ventana se muestran la fecha de ejecución y el estado de ejecución de cada remesa de pagos, junto con otros datos relevantes como el origen de la ejecución.

![](../../../../../assets/drive/1-_lia6e8AfC9M7ON-PzhrWoRitQW9sSs.png)

La ventana Remesa de pagos solo muestra los pagos recibidos o realizados que requirieron un paso de ejecución adicional, por lo que se configura un tipo de ejecución automática para el método de pago utilizado al realizar o recibir dichos pagos.

El origen de la ejecución del pago puede ser:

-   **Automáticamente desde el proceso de factura**: lo que significa que el pago se ejecuta automáticamente al completar la factura.
    -   Para obtener esta opción, el método de pago debe estar configurado de la siguiente manera:
        -   La casilla Cobro automático está marcada para los pagos recibidos.
        -   Y/o la casilla Depósito automático está marcada para los pagos recibidos.
        -   Y la casilla Diferido no está marcada.
-   **Automáticamente desde el proceso de pago**: lo que significa que el pago se ejecuta automáticamente al crear el pago.
    -   Para obtener esta opción, la casilla Diferido debe estar marcada.
-   **Formulario de ejecución de pago**: lo que significa que el pago se ha ejecutado desde el formulario de ejecución de pago.
    -   Para obtener esta opción, la casilla Diferido debe estar marcada, de modo que el pago diferido pueda ejecutarse posteriormente en el formulario de ejecución de pago.
-   **Ventana de propuesta de pago**: lo que significa que el pago se ha ejecutado desde la ventana Propuesta de pago.
    -   Para obtener esta opción, la casilla Diferido debe estar marcada, de modo que el pago diferido pueda ejecutarse posteriormente desde la ventana de propuesta de pago.
-   **Ventana de pagos**: lo que significa que el pago se ha ejecutado en la ventana de pagos salientes o de pagos entrantes.
    -   Para obtener esta opción, la casilla Diferido debe estar marcada, de modo que el pago diferido pueda ejecutarse posteriormente en la ventana de pagos correspondiente.

Hay tres estados disponibles:

-   Ejecutado, lo que significa que la remesa de pagos se ha ejecutado. Los procesos de ejecución automática proporcionados actualmente por Etendo obtendrán todos el estado "Ejecutado".
-   Y "Ejecutado parcialmente" y "Pendiente", que son estados que pueden ser utilizados por módulos como el módulo de Impresión de cheques para gestionar los casos en los que un pago no se ejecutó correctamente debido a algún problema derivado de un fallo de conexión.

## Pagos

La pestaña de pagos enumera los pagos ejecutados en una remesa de pagos.

![](../../../../../assets/drive/1porA4UfbmvSes9QKVmxrwr6b8zRav5vK.png)

## Parámetros

La pestaña de parámetros muestra el valor del parámetro o parámetros del proceso de ejecución de pagos.

Un proceso de ejecución puede tener definido un conjunto de parámetros.

Por ejemplo, el proceso de ejecución "Print Check simple process" proporcionado por Etendo solo requiere el número de cheque al ejecutar el pago.

![](../../../../../assets/drive/14j20K8igu1aLPxaZLE1jDu_9jG-ydeaj.png)

---

This work is a derivative of [Financial Management](http://wiki.openbravo.com/wiki/Financial_Management){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
