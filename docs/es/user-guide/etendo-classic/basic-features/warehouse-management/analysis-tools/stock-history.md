---
title: Historial de existencias
tags:
    - Historial de existencias
    - Inventario
    - Gestión de Almacén
    - Informes
    - Análisis de inventario
---

# Historial de existencias

:material-menu: `Aplicación` > `Gestión de Almacén` > `Herramientas de análisis` > `Historial de existencias`

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el paquete Warehouse Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Warehouse Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=EFDA39668E2E4DF2824FFF0A905E6A95){target="_blank"}. Para obtener más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Warehouse Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/warehouse-extensions/release-notes.md).
 

Esta es una ventana de solo lectura en la que el usuario puede consultar el stock diario. Esta funcionalidad actualiza la información diaria recopilada por el proceso en segundo plano que se creó previamente para este propósito. 

La ventana Historial de existencias se rellena únicamente mediante el proceso en segundo plano "Create Stock History". Puede programarse desde la ventana 'Request Processing', donde se puede asignar para qué rol y organización se ejecuta, y la periodicidad con la que se ejecuta.

!!! info
    Consulte la documentación técnica sobre Historial de existencias para ampliar el proceso y calcular los registros del historial diario de existencias. 


No se mostrarán datos en la ventana hasta que se apliquen filtros de búsqueda. Una vez aplicados los filtros, haga clic en el botón de la derecha para completar el proceso. 

![Stock History filter fields](../../../../../assets/drive/10C8VIJpu2FJkojmrZ8aKCZMZo0D0OpMJ.png)

La ventana muestra los siguientes campos a partir de los cuales el usuario puede filtrar y obtener los datos necesarios: 
- Fecha de stock 
- Producto
- Valor del conjunto de atributos
- Almacén
- Ubicación de almacenamiento
- Cantidad en stock
- Cantidad reservada
- Cantidad asignada
- Cantidad en transacción en borrador
 
![Stock History results](../../../../../assets/drive/1MhFI0Ii9bhm8EBBK-UalKWK90_-Gkm_G.png)

Esta funcionalidad incluye un proceso para cerrar el stock y guardar la información histórica.

---

Este trabajo es un derivado de [Warehouse Management](http://wiki.openbravo.com/wiki/Warehouse_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizado bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.