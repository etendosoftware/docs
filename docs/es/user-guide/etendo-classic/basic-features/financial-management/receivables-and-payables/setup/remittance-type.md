---
tags:
  - Etendo Classic
  - Financial Management
  - Remittance Type
  - Remittance Configuration
  - Receivables and Payables
---

# Tipo de Remesa { #remittance-type }

:material-menu: `Application` > `Financial Management` > `Receivables and Payables` > `Setup` > `Remittance Type`

Para configurar el método de pago de remesas es necesario ejecutar previamente un conjunto de datos que haya creado este método de pago y el proceso de ejecución.

!!! info
    El campo "En espera" debe estar siempre marcado para los métodos de pago que se apliquen a remesas.

![](../../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/setup/remittance-type/remittance-type-1.png)

!!! info
    No se definirá ninguna contabilidad para ninguna de las transacciones asociadas al método de pago de remesas, de modo que no se genere una doble contabilización. La contabilidad de las remesas se configura desde la ventana Tipo de Remesa.


El siguiente paso es la configuración del tipo de remesa y la asignación de las cuentas contables para su contabilización.
Es posible crear tantos tipos de remesa como cuentas financieras disponibles, de modo que se puedan asignar las cuentas contables adecuadas a cada una de ellas.

Se definen las siguientes cuentas:<br>
**Cuenta envio a remesa:** la cuenta que se utilizará en la contabilización de la remesa.<br>
**Cuenta de liquidación:** cuenta que se utilizará para la contabilización de la liquidación de la remesa, que hace referencia al importe cobrado o pagado.

![](../../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/setup/remittance-type/remittance-type-2.png)

Para finalizar el proceso, se deben asociar los métodos de pago aplicables a cada cuenta financiera.

!!! info
    Es importante que aquellos bancos desde los que se vayan a realizar transacciones de remesa tengan un tercero asociado.

![](../../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/setup/remittance-type/remittance-type-3.png)


## Remesas sin descuento { #non-discount-remittances }

Para configurar Remesas sin descuento, defina este método de pago desde la ventana Método de pago.  

![](../../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/setup/remittance-type/remittance-type-4.png)


![](../../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/setup/remittance-type/remittance-type-5.png)

!!! info
    Para crear una remesa sin descuento, acceda a la [ventana Remesa](../transactions/remittance.md). 

## Remesa al Descuento { #remit-for-discount }

Para configurar Remesas al Descuento, defina el tipo desde la casilla de verificación Remesa al Descuento como se muestra en la imagen a continuación: 

![](../../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/setup/remittance-type/remittance-type-6.png)



![](../../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/setup/remittance-type/remittance-type-7.png)

!!! info
    Para crear una remesa al descuento, acceda a la [ventana Remesa](../transactions/remittance.md).

---

This work is a derivative of [Financial Management](http://wiki.openbravo.com/wiki/Financial_Management){target="_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="_blank"} by [Etendo](https://etendo.software){target="_blank"}.
