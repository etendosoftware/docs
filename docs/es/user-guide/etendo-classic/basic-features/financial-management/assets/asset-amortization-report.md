---
tags:
  - Etendo Classic
  - Financial Management
  - Assets
  - Asset Amortization Report
  - Financial Extensions
---

# Informe de amortización de activos (Excel)

:material-menu: `Application` > `Financial Management` > `Assets` > `Asset Amortization Report (Excel)`

!!! info
    Para poder incluir esta funcionalidad, se debe instalar el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el núcleo y nuevas funcionalidades, visite [Financial Extensions - Notas de versión](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

## Descripción general

El informe de amortización permite descargar informes en formato Excel. El informe se encuentra en Gestión Financiera > Activos > Herramientas de análisis > Informe de amortización de activos.

![](../../../../../assets/drive/FCyjH9Cqjoxlpce_Q2Adrf0qcnEwMumykLuNZ5DvkPgw5L1GNfFz4EDeMvEQzQ4ud9ZTFjcAk-1Y0l45vCDs1ONk0KMn-TzkhKKAEL17m3fV85B2lbrmxRnIhAM4-R1zOqVfr8sU_3AoWConwvRkI4I.png)

Este informe permite filtrar por organización, fecha, activo o cualquier descripción particular, categoría y configuración contable.

![](../../../../../assets/drive/v044uU7hYLEk9gHyJ_rQT4PafeiO44KV81IWajtztUpPd9hLqZiPs9ivfPP69HxfwwK-35rPk_nzpLHsSXeXpUUfVDnFw7k4jsQ4AvDJIwDMCPWrsiRDyLPKgLCb0WDOB4GPZVU2urwKJ3sq1BhSXnA.png)

Una vez filtrada la información, se descarga una hoja de Excel tal como se muestra en la siguiente imagen:

![](../../../../../assets/drive/X4RYGKFzkl-VVrKXiztozXKKOQIFqIwXJMgUUeLzdGESddbVChKWbf6L2XnMO1aQg2wCfXit-Tw-w3TXDP_FLWBluY08K6JG6kHf_w2Mz5fRWBfzbbfV6edBbPzULPPPWxAALvtVBmxhKLtC_DwAzgg.png)

Este informe tiene en cuenta las líneas de amortización de cada activo. Es decir, el informe se generará incluso si las líneas de amortización no están procesadas ni contabilizadas.

Es necesario filtrar por fecha, ya que la información se presenta en función de dicho filtro. Es decir, el período acumulado, el valor neto y los campos posteriores del informe dependerán de este filtro.

Por ejemplo: Fecha de período filtrada del 01-01-2022 al 31-12-2022

**Período:** Se mostrará el total de las líneas de amortización entre el 01/01/2022 y el 31/12/2022. <br>
**Acumulado:** Se mostrará la suma de las líneas de amortización entre el 01/01/2022 y el 31/12/2022 más el total de las líneas de amortización anteriores al 01/01/2022. <br>
**Valor neto:** Se mostrará el valor del activo menos el campo Acumulado. <br>
**Posterior:** Se mostrarán las líneas de amortización posteriores al 31-12-2022. <br>

!!! info
    Cuando se rellena la fecha de fin en la ventana Activos, ese activo no aparecerá en el informe si la fecha filtrada es posterior a la fecha de fin del activo.

---

This work is a derivative of [Financial Management](http://wiki.openbravo.com/wiki/Financial_Management){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
