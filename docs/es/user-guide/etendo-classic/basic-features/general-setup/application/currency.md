---
title: Moneda
tags:
    - Moneda
    - Rangos de conversión
    - Configuración
---

# Moneda

:material-menu: `Aplicación` > `Configuración General` > `Aplicación` > `Moneda`

### Visión general

- Las monedas y los rangos de conversión son configuraciones básicas en Etendo.
- Las monedas utilizadas en todo el mundo se crean automáticamente y se listan en la ventana de moneda una vez finalizada la instalación de Etendo.

    !!! info
        Todas estas monedas están vinculadas a la **organización del sistema (\*)**, lo que significa que esas monedas se compartirán entre todas las organizaciones del sistema.

### Moneda

La ventana Moneda permite al usuario visualizar o crear y configurar las monedas que se utilizarán en transacciones monetarias.

![alt text](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/application/currency.png)

Como se muestra en la imagen anterior, los datos relevantes de la moneda son:

- El **código ISO** de la moneda. Los códigos ISO de moneda son códigos utilizados en todo el mundo para la representación de monedas y fondos.
- El **símbolo** de la moneda, que puede colocarse a la derecha o a la izquierda de un importe.
- y la **precisión** de la moneda o número de decimales a utilizar al calcular importes en esa moneda.

Etendo permite al usuario configurar tres tipos de precisión de moneda:

- La **precisión estándar**, con valor por defecto 2, es la que se utiliza de forma general, excepto para los cálculos de importes de precios y costes, que pueden utilizar una precisión diferente.  
  Esta precisión es la que se utiliza para calcular importes de pedidos y facturas como "Imp. línea", "Imp. total líneas" e "Importe total"; por lo tanto, no debería ser superior a 2, a menos que la moneda permita pagar cantidades menores que 0.01.
- La **precisión de coste**, con valor por defecto 2, es la que se utiliza para los cálculos de coste de producto. Se recomienda cambiarla a 4.
- y la **precisión de precio** es la que se utiliza para los precios unitarios/de tarifa, que pueden tener más de 2 decimales de precisión porque los importes finalmente se redondean a 2 mediante la precisión estándar.

    !!! warning
        Los cambios en la precisión de la moneda solo pueden realizarse a nivel de cliente; por lo tanto, es necesario utilizar el rol `System Admin`.

#### Rangos de conversión

La solapa Rangos de conversión lista los rangos de conversión disponibles para una moneda determinada.

![alt text](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/application/currency-conversion-rates.png)

Un rango de conversión es el tipo válido al que una moneda puede convertirse en otra dentro de un período de tiempo determinado.

Esto implica que una única moneda podría tener varios rangos de conversión en función de:

- La **moneda** a la que podría convertirse.
- y el **período de validez**.

!!! info
    - Los rangos de conversión de moneda también pueden crearse en la ventana [Rangos de conversión](./conversion-rates.md); por lo tanto, pueden revisarse en esta solapa.
    - Etendo recomienda que los rangos de conversión se configuren en la ventana **Rangos de conversión**, ya que es necesario definir tanto *Multiplicar por* (USD - €) como *Dividir por* (€ - USD) para definir correctamente el cambio entre dos monedas.

#### Traducción

Las monedas pueden traducirse a cualquier idioma si es necesario.

![alt text](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/application/currency-translation.png)

---

Este trabajo es una obra derivada de [Configuración General](https://wiki.openbravo.com/wiki/General_Setup){target="_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="_blank"} por [Etendo](https://etendo.software){target="_blank"}.