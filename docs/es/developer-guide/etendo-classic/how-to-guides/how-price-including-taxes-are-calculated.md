---
title: Cómo se calculan los precios con impuestos incluidos
tags: 
    - Cálculo de impuestos
    - Tarifas
    - Importe neto
    - Importe bruto
    - Rango impuesto

status: beta
---
  

# Cómo se calculan los precios con impuestos incluidos

!!! example "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.

## Visión general

Desde la disponibilidad de la funcionalidad **Tarifas con impuestos incluidos**, han surgido algunas dudas sobre cómo se calculan los precios/importes netos y los importes de impuestos.

El cálculo puede dividirse en dos pasos:

1. Calcular el **Importe neto** a partir de un **Importe bruto** dado y, a continuación, el **Rango impuesto** correspondiente.
2. Calcular los **Impuestos** a partir del **Importe neto** recién calculado, que luego debe ajustarse para que el **Importe neto** más los **Impuestos** sea igual al **Importe bruto**. 

## Cálculo del importe neto

Cuando se está calculando el **Importe neto**, puede que no exista un único rango con el que trabajar, sino una relación de **diferentes rangos de impuestos**.

Los [Impuestos en cascada](../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup/tax-rate.md) hacen que el cálculo de un importe neto a partir de un importe bruto dado sea algo más difícil. Normalmente, el importe bruto se dividiría por el rango para obtener el importe neto, pero el rango puede no ser único; en otras palabras, puede no estar disponible y, por lo tanto, **tiene que calcularse**.

Para calcular el rango de impuesto, es necesario calcular el importe de impuesto que corresponde al precio bruto. Si el importe de impuesto se divide por el precio bruto, se obtiene el rango de impuesto:

```   
            tax amount of gross price
tax rate = ---------------------------
                gross price
```
    

Una vez obtenido el rango de impuesto, se puede calcular el precio neto:

``` 
                gross price  
net price = -----------------
                tax rate
``` 

Si se sustituye el rango de impuesto por la fórmula anterior y se simplifica, se obtiene:

```
                                    gross price
net price = gross price * ( ------------------------------ )
                                gross price + tax amount
```    

Este método devuelve el resultado exacto, pero su implementación requiere **redondear** el importe de impuesto calculado.

El importe bruto total se utiliza para calcular el importe neto, que una vez dividido por la cantidad, permite obtener el precio neto. 

La fórmula utilizada es:

``` 
                                                gross amount 
    net price = gross amount * ( ------------------------------------------- ) / quantity
                                  gross amount + tax amount of gross amount
```    

## Cálculo de impuestos

Una vez calculado el importe neto, es el momento de calcular el **importe final de impuestos** del Pedido o de la Factura.

Cuando se calculan los impuestos, es importante considerar diferentes configuraciones posibles. Los importes de impuestos pueden redondearse a nivel de **línea o documento**.

Además, una única línea puede tener importes de impuestos de diferentes rangos de impuestos, si se están utilizando rangos de impuestos en cascada. Por ello, restar el importe neto al importe bruto no es una opción válida.

Como se conocen los importes netos, se utilizan los métodos estándar para calcular los importes de impuestos basados en importes netos. Sin embargo, el importe neto calculado debe **redondearse a la precisión estándar** de la divisa.
  
Puede haber algunos problemas de redondeo cuando se trabaja con impuestos calculados a nivel de documento:

En algunos casos, la suma de los importes de impuestos y el importe neto puede no ser igual al importe bruto total. La diferencia se ajustará al completar el documento en los importes de impuestos, **sumando o restando** la diferencia al mayor importe de impuesto para que la suma final sea correcta.

También es posible que la suma de los importes netos de línea no sea igual al importe neto total. La diferencia se ajustará al completar el documento, sumando o restando la diferencia al mayor importe neto de línea para que la suma final sea correcta.


**Algunos ejemplos con diferentes impuestos y precios brutos** 

| Ejemplo de impuesto | Importe bruto | Importe neto | Neto redondeado | Impuestos     | Impuesto ajustado |
|---------------------|---------------|--------------|------------------|---------------|-------------------|
| Simple 21%          | 1.53          | 1.26446      | 1.26             | 0.26          | 0.27              |
| Simple 21%          | 1.21          | 1.00         | 1.00             | 0.21          | 0.21              |
| Simple 21%          | 1.64          | 1.35537      | 1.36             | 0.29          | 0.28              |
| 6.25% + 1%          | 1.56          | 1.454545     | 1.45             | 0.09 + 0.01   | 0.10 + 0.01       |
| 6.25% + 1%          | 1.61          | 1.501165     | 1.50             | 0.10 + 0.01   | 0.10 + 0.01       |
| 6.25% + 1%          | 1.65          | 1.538461     | 1.54             | 0.10 + 0.02   | 0.09 + 0.02       |

  

Este trabajo es una obra derivada de [Cómo se calculan los precios con impuestos incluidos](http://wiki.openbravo.com/wiki/How_Price_Including_Taxes_are_Calculated){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.