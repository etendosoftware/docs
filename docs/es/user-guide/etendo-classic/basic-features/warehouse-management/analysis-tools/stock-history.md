---
title: Historial de existencias
---

## Historial de existencias

:material-menu: `Aplicación` > `Gestión de Almacén` > `Herramientas de análisis` > `Historial de existencias`

!!! info
    Para poder incluir esta funcionalidad, el paquete Warehouse Extensions Bundle debe estar instalado. Para ello, siga las instrucciones del marketplace: [Warehouse Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=EFDA39668E2E4DF2824FFF0A905E6A95){target="_blank"}. Para obtener más información sobre las versiones disponibles, la compatibilidad con core y las nuevas funcionalidades, visite [Warehouse Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/warehouse-extensions/release-notes.md).
 

Esta es una ventana de solo lectura en la que el usuario puede consultar el stock diario. Esta funcionalidad actualiza la información diaria recopilada por el proceso en segundo plano que se creó previamente para este propósito. 

La ventana Historial de existencias se completa únicamente mediante el proceso en segundo plano "Create Stock History". Puede programarse desde la ventana "Request Processing", donde se puede asignar para qué rol y organización se ejecuta, y la periodicidad con la que se ejecuta.

!!! info
    Consulte la documentación técnica sobre Historial de existencias para ampliar el proceso y calcular los registros del historial diario de existencias. 


No se mostrarán datos en la ventana hasta que se apliquen filtros de búsqueda. Una vez aplicados los filtros, haga clic en el botón de la derecha para completar el proceso. 

![](../../../../../assets/drive/10C8VIJpu2FJkojmrZ8aKCZMZo0D0OpMJ.png)

La ventana muestra los siguientes campos a partir de los cuales el usuario puede filtrar y obtener los datos necesarios: 
- Fecha de existencias 
- Producto
- Valor del conjunto de atributos
- Almacén
- Ubicación de almacén
- Cantidad en stock
- Cantidad reservada
- Cantidad asignada
- Cantidad en transacción en borrador
 
![](../../../../../assets/drive/1MhFI0Ii9bhm8EBBK-UalKWK90_-Gkm_G.png)

Esta funcionalidad incluye un proceso para cerrar el stock y guardar la información histórica.

---

Este trabajo es un derivado de [Gestión de Almacén](http://wiki.openbravo.com/wiki/Warehouse_Management){target="\_blank"} por [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizado bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="_blank"}.