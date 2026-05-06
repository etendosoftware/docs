---
tags:
  - Etendo Classic
  - Financial Management
  - Accounting
  - Journal Entries Report
  - Financial Extensions
---

# Informe de Asientos Contables Avanzado

:material-menu: `Aplicación` > `Gestión Financiera` > `Contabilidad` > `Herramientas de Análisis` > `Informe de Asientos Contables Avanzado`

<iframe width="560" height="315" src="https://www.youtube.com/embed/o5V3Op_qYtE?si=DnTJ77x6zSMZ5KrC" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el núcleo y nuevas funcionalidades, visite [Financial Extensions - Notas de versión](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

## Visión General

Este informe **Asientos Contables Avanzado** es una versión mejorada del anterior [Informe de Asientos Contables](./journal-entries-report.md). Su propósito es ampliar los criterios de filtrado, incluyendo todas las dimensiones contables existentes en la tabla Detalles de Transacciones Contables.

![](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/journal-entries-report-adv-1.png)


Además de los filtros básicos anteriores: Fecha desde, Fecha hasta, Organización, Libro Mayor y los filtros avanzados anteriores: Desde cuenta, Hasta cuenta, Documento, N.º de Documento, se han añadido los siguientes:

- Tercero
- Producto
- 1.ª Dimensión
- 2.ª Dimensión
- Proyecto
- Actividad
- Región de Ventas
- Campaña de Ventas
- Centro de Coste

El nuevo campo **Mostrar Entidades Dimensionales** permite seleccionar las dimensiones contables que se incluirán en el informe.

![](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/journal-entries-report-adv-2.png)

Tras utilizar los campos y casillas disponibles, el informe filtra las transacciones incluidas en las dimensiones seleccionadas, para la organización y el libro mayor seleccionados y para un periodo determinado, si es necesario. En cada filtro se puede seleccionar más de una opción.

## Botones

En la barra superior, se encuentran los botones **Ver**, **Exportar a PDF** y **Exportar a Excel** para generar el informe. En el caso de la opción Ver, se abre una nueva ventana con el informe correspondiente. En los otros casos, el informe se exporta en formato PDF o Excel.

![](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/journal-entries-report-adv-3.png)

!!!warning
    Si se eligen las opciones Ver o Exportar a PDF, el límite de dimensiones a incluir es 4 para evitar problemas de visualización. Esto no aplica a Exportar a Excel, en cuyo caso se puede elegir cualquier número de dimensiones.

Además, con esta funcionalidad es posible navegar a la transacción relacionada directamente desde el número de asiento de los informes. Esto mejora la trazabilidad y agiliza el análisis contable.

![](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/journal-entries-report-adv-4.png)

---

Este trabajo es una obra derivada de [Financial Management](http://wiki.openbravo.com/wiki/Financial_Management){target="\_blank"} por [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.
