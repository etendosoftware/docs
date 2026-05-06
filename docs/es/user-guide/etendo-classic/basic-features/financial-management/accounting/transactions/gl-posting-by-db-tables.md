---
tags:
  - Etendo Classic
  - Financial Management
  - Accounting
  - GL Posting
  - Ledger Entries
---

# Contabilización por Tablas de BD

:material-menu: `Application` > `Financial Management` > `Accounting` > `Transactions` > `GL Posting by DB Tables`

## Visión General

La Contabilización por Tablas de BD permite al usuario contabilizar masivamente las transacciones relacionadas con una tabla transaccional determinada o con todas ellas.

![](../../../../../../assets/drive/1tAh4RfUDcPvDgSG9PeBYX79MhpW-csWW.png)

Como se muestra en la imagen anterior, la funcionalidad **Contabilización por Tablas de BD** permite al usuario:

-   seleccionar una Organización o todas ellas si no se selecciona una organización concreta
-   seleccionar una Tabla o todas ellas si no se selecciona una tabla concreta
-   y seleccionar una **Fecha Desde** y **Fecha Hasta**; si no se seleccionan fechas, se contabilizarán todas las transacciones disponibles.

Tras ejecutar el proceso, Etendo informa sobre el número de asientos del libro mayor registrados en el libro mayor para cada tabla, con el fin de contabilizar de nuevo la/s tabla/s transaccional/es en el libro mayor.

![](../../../../../../assets/drive/1nfPHEpviK8sRPB5BEZbSM4xYx32HgHeX.png)

Este proceso puede lanzarse cuando sea necesario:

-   Puede ejecutarse si hay transacciones pendientes de contabilizar de forma masiva cuando el Proceso de Servidor de Contabilidad no está habilitado o no lo está para un conjunto determinado de tablas.
-   También puede ejecutarse tras ejecutar el proceso Restablecer Contabilidad, como forma de regenerar los asientos del libro mayor.

---

This work is a derivative of [Financial Management](http://wiki.openbravo.com/wiki/Financial_Management){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
