---
tags:
  - Etendo Classic
  - Financial Management
  - Tax Register Type
  - Tax Payment
  - Receivables and Payables
---

# Tipo de Registro de Impuesto

:material-menu: `Application` > `Financial Management` > `Receivables and Payables` > `Setup` > `Tax Register Type`

## Descripción general

Un tipo de registro de impuesto se utiliza para recopilar todos los tipos impositivos de un tipo y tenerlos en cuenta al calcular el importe total de impuestos de un tipo de registro de impuesto determinado dentro de un período de tiempo.

Los tipos de registro de impuesto son una variable clave del proceso de Pago de Impuestos, ya que es este proceso el que calcula el importe total de impuestos de cada tipo de registro de impuesto creado y configurado.

En otras palabras, el proceso "Pago de impuestos" ayuda a calcular el importe de impuestos a pagar a la autoridad tributaria correspondiente o a recibir de ella, como la diferencia entre:

-   los tipos de registro de impuesto de "Ventas" o el importe total de impuestos que cobra una organización y que pagan sus clientes
-   y los tipos de registro de impuesto de "Compras" o el importe total de impuestos que paga una organización a otras empresas por los suministros que recibe.

## Cabecera

La ventana de tipo de registro de impuesto permite al usuario crear tipos de registro de impuesto.

![Tax Register Type Header](../../../../../assets/drive/1wwI271qWNtJQmMZxupMktzWI6S3ByU6w.png)

Como se muestra en la imagen anterior, es posible crear:

-   tipos de registro de impuesto relacionados con "**Ventas**", que por lo tanto incluirán **"Tipos Impositivos"** relacionados con ventas en la pestaña "**Líneas**"
-   así como tipos de registro de impuesto relacionados con "**Compras**", que por lo tanto incluirán **"Tipos Impositivos"** relacionados con compras en la pestaña "**Líneas**"

Además, cada tipo de registro de impuesto debe estar vinculado a un Concepto contable.

Las cuentas contables definidas para ese Concepto contable serán las que se utilicen al contabilizar el pago de impuestos calculado como la diferencia entre el tipo de registro de impuesto de "Ventas" y el de "Compras".

## Líneas

La pestaña de líneas permite al usuario asociar tipos impositivos al tipo de registro de impuesto.

![Tax Register Type Lines](../../../../../assets/drive/1O_4QacWfrELWWRoG5Ye2E73Fa8AIi8i1.png)

Como se muestra en la imagen anterior, cada tipo impositivo seleccionado también debe estar vinculado a un tipo de documento.

Por lo tanto, no solo es posible configurar los tipos impositivos que el proceso de pago de impuestos tomará como parte de un tipo de registro de impuesto, sino también los tipos de documento que se tendrán en cuenta.

Los **tipos de documento de ventas** que pueden vincularse al impuesto de ventas correspondiente son:

-   AR Invoice
-   AR Credit Note
-   Reversed Sales Invoice
-   ES Return Material Sales Invoice

Los **tipos de documento de compras** que pueden vincularse al impuesto de ventas correspondiente son:

-   AP Invoice
-   AP Credit Note
-   Reversed Purchase Invoice

---

This work is a derivative of [Financial Management](http://wiki.openbravo.com/wiki/Financial_Management){target="_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="_blank"} by [Etendo](https://etendo.software){target="_blank"}.
