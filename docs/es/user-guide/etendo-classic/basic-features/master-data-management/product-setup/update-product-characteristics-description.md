---
title: Actualizar descripción de las características de producto
tags:
  - Master Data Management
  - Etendo Classic
  - Product
  - Product Characteristic
---

## Actualizar descripción de las características de producto { #update-product-characteristics-description }

:material-menu: `Aplicación` > `Gestión de Datos Maestros` > `Configuración de productos` > `Actualizar descripción de las características de producto`

### Visión general { #overview }

Cada variante tiene su _Descripción de característica_ de producto y este campo se calcula automáticamente cuando:

- Se crean variantes
- Cuando se cambia el valor de una característica, por ejemplo de _Azul_ a _Azul oscuro_

Por ejemplo, si las características de una variante son Color y Talla y los valores son Azul y XL, el resultado de la descripción sería: _Color: Azul, Talla: XL_

Si posteriormente cambia Azul por Azul oscuro, la nueva descripción sería _Color: Azul oscuro, Talla: XL_

En todos estos escenarios, la _Descripción de característica_ se actualiza sin necesidad de ejecutar este proceso.

Este proceso debe utilizarse únicamente en algunos casos especiales:

- Cuando se cambia el nombre de la Característica, por ejemplo de Color a Tono
- Cuando, a través de la base de datos, se modifican características o valores

---

Este trabajo es una obra derivada de [Gestión de Datos Maestros](https://wiki.openbravo.com/wiki/Master_Data_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.
