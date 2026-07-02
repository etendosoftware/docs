---
tags:
  - Etendo
  - Gestión financiera
  - Contabilidad
  - Informes de impuestos
  - Informes financieros
---

# Creación de informes de impuestos { #create-tax-report }

## Descripción general { #overview }

Un informe de impuestos resume los importes de impuestos recaudados o pagados durante un período; por ejemplo, el IVA de ventas recaudado o el IVA de compras pagado.

El trabajo con informes de impuestos implica dos pasos secuenciales. Primero, defina la estructura del informe en **Configuración informes de impuestos**: especifique qué impuestos se incluyen, si el informe cubre ventas o compras y cómo se muestra cada línea. Segundo, genere el informe en **Creación de informes de impuestos**: seleccione una organización y un rango de fechas y, a continuación, ejecute el informe para obtener el resultado.


## Configuración informes de impuestos { #tax-report-setup }

:material-menu: `Aplicación` > `Gestión Financiera` > `Contabilidad` > `Herramientas de análisis` > `Configuración informes de impuestos`

Utilice esta ventana para crear o editar definiciones de informes de impuestos. Cada definición controla qué impuesto se declara, si cubre ventas o compras y cómo se muestran los importes.

![Tax Report Setup](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/create-tax-report/tax-report-setup.png)

- **Nombre:** La etiqueta utilizada para identificar esta definición de informe.
- **Impuesto:** El impuesto específico que cubrirá este informe (por ejemplo, IVA 21% o IVA 10%). Selecciónelo de la lista de impuestos ya configurados en su sistema.
- **Operación de venta:** Marque esta opción para un informe de impuestos de ventas; déjela sin marcar para un informe de impuestos de compras.
- **Informe:** Si está marcado, esta definición de informe de impuestos aparece en la lista del formulario Creación de informes de impuestos y puede seleccionarse para su generación. Si no está marcado, la definición se guarda pero no está disponible para su selección.
- **Mostrar:** Si está marcado, esta línea de impuesto aparece como una fila visible en el resultado del informe. Si no está marcado, la línea de impuesto sigue contribuyendo a los totales calculados pero la fila individual queda oculta. Utilice esta opción cuando deba aparecer un subtotal sin mostrar cada línea que lo compone.
- **Nivel agrupación:** Marque esta casilla solo si este impuesto es una categoría de agrupación que contiene subimpuestos (por ejemplo, un impuesto padre "IVA" que agrupa "IVA 10%" e "IVA 21%"). Si el impuesto es independiente y no tiene subimpuestos, déjela sin marcar. En caso de duda, consulte la estructura de impuestos con su administrador del sistema.
- **Negativo:** Si está marcado, el informe se imprime con valores negativos; de lo contrario, se imprime con valores positivos.
- **Activo:** Controla si esta definición de informe de impuestos está activa. Cuando no está marcado, la definición se deshabilita y se oculta del sistema sin eliminarse. Desmarque este campo para retirar una definición sin perder su configuración.

## Creación de informes de impuestos { #create-tax-report_1 }

:material-menu: `Aplicación` > `Gestión Financiera` > `Contabilidad` > `Herramientas de análisis` > `Creación de informes de impuestos`


![Create Tax Report](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/create-tax-report/create-tax-report.png)

Utilice este formulario para ejecutar un informe de impuestos previamente configurado para una organización y un rango de fechas específicos. Complete los siguientes campos:

- **Fecha desde:** El primer día del período del informe.
- **Fecha hasta:** El último día del período del informe.
- **Informes de impuestos:** La definición del informe que se ejecutará. La lista muestra todas las definiciones de informes de impuestos que tienen el indicador **Informe** habilitado en Configuración informes de impuestos.
- **Organización:** La empresa o sucursal para la que se genera el informe. En una configuración multiorganización, seleccione la entidad legal correcta para el período fiscal que se va a declarar.

Una vez completados los campos, haga clic en **OK** para generar el informe. El informe muestra los importes de impuestos —desglosados por las líneas de impuesto definidas en Configuración informes de impuestos— para el rango de fechas y la organización seleccionados. Utilice este resultado para verificar que sus totales de impuestos coinciden con lo que presentará a las autoridades fiscales al liquidar los impuestos del período.


---

This work is a derivative of [Financial Management](http://wiki.openbravo.com/wiki/Financial_Management){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
