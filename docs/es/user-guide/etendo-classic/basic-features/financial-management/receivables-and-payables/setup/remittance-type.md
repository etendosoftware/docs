---
tags:
  - Etendo Classic
  - Financial Management
  - Remittance Type
  - Remittance Configuration
  - Receivables and Payables
---

# Tipo de Remesa

:material-menu: `Application` > `Financial Management` > `Receivables and Payables` > `Setup` > `Remittance Type`

Para configurar el método de pago de remesas es necesario ejecutar previamente un conjunto de datos que haya creado este método de pago y el proceso de ejecución.

!!! info
    El campo "Diferido" debe estar siempre marcado para los métodos de pago que se apliquen a remesas.

![](../../../../../assets/drive/1Qe3mdTduM3wJctZkC3N8z-yLRL_Gq6Y_.png)

!!! info
    No se definirá ninguna contabilidad para ninguna de las transacciones asociadas al método de pago de remesas, de modo que no se genere una doble contabilización. La contabilidad de las remesas se configura desde la ventana de tipos de remesa.


El siguiente paso es la configuración del tipo de remesa y la asignación de las cuentas contables para su contabilización.
Es posible crear tantos tipos de remesa como cuentas financieras disponibles, de modo que se puedan asignar las cuentas contables adecuadas a cada una de ellas.

Se definen las siguientes cuentas:<br>
**Cuenta de envío:** la cuenta que se utilizará en la contabilización de la remesa.<br>
**Cuenta de liquidación:** cuenta que se utilizará para la contabilización de la liquidación de la remesa, que hace referencia al importe cobrado o pagado.

![](../../../../../assets/drive/1fUwM5P-aNQOSlIm1u_mYfDAdQzbPO6ur.png)

Para finalizar el proceso, se deben asociar los métodos de pago aplicables a cada cuenta financiera.

!!! info
    Es importante que aquellos bancos desde los que se vayan a realizar transacciones de remesa tengan un tercero asociado.

![](../../../../../assets/drive/1lNuqadYEmnZeOl8RcS3hXS_2-N7GrVfg.png)


## Remesas sin descuento

Para configurar Remesas sin descuento, defina este método de pago desde la ventana Método de Pago.  

![](../../../../../assets/drive/11mLuoH5qVVh_8tjnepUL12O6oaOkIoY2.png)


![](../../../../../assets/drive/1Y0pJr2nUKDJEYbp85_a75ifAKQ70IIqO.png)

!!! info
    Para crear una remesa sin descuento, acceda a la [ventana Remesa](../../financial-management/receivables-and-payables/transactions/remittance.md). 

## Remesa al descuento

Para configurar Remesas al descuento, defina el tipo desde la casilla de verificación Remesa al descuento como se muestra en la imagen a continuación: 

![](../../../../../assets/drive/1xW3siKWbirKqZAazQzIoLoPcGMknNwjk.png)



![](../../../../../assets/drive/12vjozrcXO3zaa1j9_e0P9xj3TD9kJ-FI.png)

!!! info
    Para crear una remesa al descuento, acceda a la [ventana Remesa](../../financial-management/receivables-and-payables/transactions/remittance.md).

---

This work is a derivative of [Financial Management](http://wiki.openbravo.com/wiki/Financial_Management){target="_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="_blank"} by [Etendo](https://etendo.software){target="_blank"}.
