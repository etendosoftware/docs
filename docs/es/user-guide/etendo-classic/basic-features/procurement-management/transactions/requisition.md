---
title: Necesidad de material
tags:
    - Proceso de Compras
    - Necesidades de compra
---

# Necesidad de material

:material-menu: `Aplicación` > `Gestión de Compras` > `Transacciones` > `Necesidad de material`

Una Necesidad de material es un documento que especifica una solicitud para pedir productos.

El usuario puede crear necesidades de material y monitorizarlas en esta ventana:

![Ventana de Necesidad de material](../../../../../assets/drive/1ihaEseE5RnNH7INNbaRLyvZC0P2q-hTl.png)

## Cabecera

La cabecera de la Necesidad de material permite introducir los siguientes datos:

- El tercero o proveedor; este es un campo opcional que puede ser rellenado por el solicitante en caso de que se conozca, por lo tanto:
  - El proveedor introducido en la cabecera será el que se utilice para cada línea de la necesidad de material, a menos que se cambie a nivel de líneas para una línea en particular.
  - Si no hay ningún proveedor introducido en la cabecera de la necesidad de material, se utilizará el configurado por defecto para el producto en su ventana de datos maestros, pestaña *Compras*.
  - Si no hay ningún tercero o proveedor en la cabecera, ni en las líneas, ni configurado en el producto, el usuario tendrá que introducirlo al crear el pedido de compra a partir de la necesidad de material.
- La tarifa de compra. Este también es un campo opcional a rellenar, en caso de que el solicitante la conozca, y su comportamiento es el mismo que el descrito anteriormente, ya que está vinculada al Tercero.

Además, el sistema rellena los siguientes datos:

- El Nº de documento, que es el número de la Necesidad de material.
- El solicitante, que es el usuario que introduce la necesidad de material.

![Necesidad de material](../../../../../assets/drive/1G5HR3bMmJXW837o-6qzZ0CTe418q5JB7.png)

El solicitante puede entonces pasar a la pestaña "Líneas" para introducir datos adicionales.

## Líneas

Cada línea de la necesidad de material muestra una demanda de producto para una fecha específica.

La pestaña "Líneas" de la Necesidad de material recoge los siguientes datos de demanda:

- La *fecha necesaria*, es decir, la fecha en la que se requiere que llegue el producto.
- El *producto*, artículos/productos que necesitan comprarse.
- La *cantidad* solicitada, o la *cantidad operativa* solicitada si el producto tiene configurada una *unidad de medida alternativa (AUM)*.
- La *UdM* del producto, o la *UdM alternativa* del producto, dependiendo de la configuración del producto respecto a la unidad de medida.
- El *tercero:* este es un campo opcional que el usuario puede introducir si el proveedor introducido en la cabecera de la necesidad de material necesita cambiarse para una línea en particular.

!!! info
    Si no hay un proveedor introducido en la cabecera de la necesidad de material, ni en la línea de la necesidad de material, el proveedor utilizado será el configurado por defecto para el producto; por lo tanto, este campo a nivel de línea también puede utilizarse para sobrescribir el valor por defecto.

- La *tarifa de compra*: este también es un campo opcional que puede introducirse si la tarifa introducida a nivel de cabecera o la información de tarifa por defecto del producto debe sobrescribirse para una línea en particular.
- El *precio neto de tarifa*: este es el precio de la tarifa correspondiente para una fecha determinada. Es un campo opcional que puede rellenarse automáticamente en función de la tarifa introducida a nivel de cabecera o puede ser sobrescrito por el usuario para una línea de producto en particular.
- El *precio neto unitario:* este puede ser igual al precio neto de tarifa o no, en función de la fórmula: \[precio neto unitario = precio neto de tarifa - descuento\]. Es un campo opcional que puede rellenarse automáticamente en función de la tarifa introducida a nivel de cabecera o puede ser sobrescrito por el usuario para una línea de producto en particular.
- El *descuento*, si lo hubiera, se basa en la tarifa utilizada.

![Líneas de Necesidad de material](../../../../../assets/drive/1CtrCvBCrvUuxYDlaFysmkKu0-0XhemfC.png)

Es posible introducir tantas líneas de necesidad de material como demanda de productos.

El último paso es registrar la *Necesidad de material* como *Completada* usando el botón de cabecera "Completar"; entonces:

- La *barra de estado de la cabecera de la necesidad de material* nos informa de que la Necesidad de material está *Completada*.
- La *barra de estado de las líneas de la necesidad de material* nos informa de que la *cantidad de pedido de compra emparejada* para cada línea es igual a 0**, ya que todavía no hay ningún pedido de compra vinculado a cada línea de la necesidad de material, y el estado de la(s) línea(s) de la necesidad de material es *Abierta*.

Es importante remarcar que las *Necesidades de material* no tienen ningún impacto en:

- Cantidad disponible de los artículos
- Coste de los artículos

---

Este trabajo es una obra derivada de [Procurement Management](http://wiki.openbravo.com/wiki/Procurement_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.

---
Esta obra está licenciada bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L.](https://etendo.software){target="_blank"}.