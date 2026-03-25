---
title: Administrar necesidades
tags:
    - Proceso de Compras
    - Necesidades de compra
---

# Administrar necesidades

:material-menu: `Aplicación` > `Gestión de Compras` > `Transacciones` > `Administrar necesidades`

La ventana Administrar necesidades está pensada para proporcionar una visión general de los artículos necesarios.

## Cabecera

Esta ventana permite al usuario gestionar las necesidades independientemente de su estado actual; por lo tanto, pueden cambiar o cerrar una necesidad de material y crear pedidos de compra para esas demandas.

![Requisition window Header](../../../../../assets/drive/1yuE4xa0usvVzSdmthjDWdi12OAqTuJTe.png)

Una **necesidad de material** con estado "Completada" **siempre se puede cambiar**, si es necesario. El usuario debe reactivarla y luego modificarla y contabilizarla.

También es posible **cerrar una necesidad de material en caso de que ya no se necesite el/los artículo/s incluidos**, usando el botón de menú "**Close**" y luego seleccionando la acción "**Close**".

El estado de las líneas de la necesidad de material se cambiará entonces a "Cancelled".

Por último, también es posible **crear pedidos de compra** para aquellas **necesidades de material en estado "Complete"**, usando el botón de menú "**Crear Pedido de Compra (Necesidades de material)**".

En este caso, se muestra una nueva ventana para que el usuario rellene algunos datos, teniendo en cuenta que:

- Si hay **distintos proveedores en las líneas de la necesidad de material, así como tarifa**:
  - los **valores por defecto** introducidos en la ventana "Crear Pedido de Compra (Necesidades de material)" **serán los que se utilicen** en el pedido de compra.
- Si hay **distintos proveedores en las líneas de la necesidad de material, así como tarifa**, y el usuario no introduce ningún valor por defecto en la ventana "Crear Pedido de Compra (Necesidades de material)":
  - **se utilizarán los de las líneas de la necesidad de material** en los pedidos de compra.
- Si **todas las líneas de la necesidad de material tienen el mismo proveedor y tarifa**:
  - **no será necesario seleccionar valores por defecto** en la ventana "Crear Pedido de Compra (Necesidades de material)"; además, solo se creará un pedido de compra.

![Purchase order](../../../../../assets/drive/17OuNS8YpM0VC3MUkLO25DPPHCMwWjq8u.png)

Etendo proporciona información sobre el/los número/s de pedido/s de compra creados tras pulsar el botón OK en la ventana "Crear Pedido de Compra (Necesidades de material)".

Esta acción vincula la necesidad de material y el pedido de compra y, además, se crea una línea de pedido de compra por cada línea de la necesidad de material:

- Una **necesidad de material** vinculada a un pedido de compra cambia su estado de **Completada** a **Cerrado**.
- Una **línea de necesidad de material** vinculada a una línea de pedido de compra cambia su estado de **Open** a **Cerrado**.

Cualquier **pedido de compra** creado a partir de una **Necesidad de material**:

- se listará en la **ventana "Pedido de compra"**.
- tendrá un estado "**Booked**"
- y contendrá **datos heredados de la Necesidad de material**, datos como:
  - Fecha de pedido
  - Fecha de entrega prevista
  - Tercero
  - Tarifa
  - Producto/s

## Líneas

El usuario puede realizar un conjunto de acciones relacionadas con las líneas de la necesidad de material. Es posible crear líneas o demandas de producto o cancelarlas.

- **Se pueden crear manualmente nuevas demandas de producto** dentro de una necesidad de material simplemente **añadiendo nuevas líneas de necesidad de material** antes de crear un pedido de compra.
- **Las demandas de producto existentes o las líneas de necesidad de material pueden cancelarse**, si ya no son necesarias, usando el botón de cabecera "**Cambiar estado**".

### Líneas de OC (Pedido de compra) emparejadas

Esta pestaña permite al usuario revisar la línea de pedido de compra vinculada automáticamente a una línea de necesidad de material o vincular manualmente una línea de pedido de compra existente a la línea de necesidad de material correspondiente.

---

Este trabajo es una obra derivada de [Procurement Management](http://wiki.openbravo.com/wiki/Procurement_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.

---
Esta obra está licenciada bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L.](https://etendo.software){target="_blank"}.