---
tags:
  - Etendo Classic
  - Gestión financiera
  - Contabilidad
  - Configuración informes de impuestos
  - Informes financieros
---

# Configuración informes de impuestos { #tax-report-setup }

:material-menu: `Aplicación` > `Gestión Financiera` > `Contabilidad` > `Herramientas de análisis` > `Configuración informes de impuestos`

## Descripción general { #overview }

Un informe de impuestos resume los importes de impuestos recaudados o pagados durante un período, por ejemplo, el IVA de ventas recaudado o el IVA de compras pagado. Antes de generar un informe de impuestos, es necesario definir su estructura en esta ventana.

## Configuración informes de impuestos { #tax-report-setup_1 }

Use esta ventana para crear o editar definiciones de informes de impuestos. Cada definición controla qué impuesto se informa, si cubre ventas o compras y cómo se muestran las cifras. Los siguientes campos definen el informe de impuestos:

![](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/tax-report-setup/tax-report-setup-1.png)

- **Nombre:** El nombre del informe.
- **Impuesto:** El impuesto que se muestra en el informe.
- **Operación de venta:** Marcado si es un informe de impuestos de ventas; desmarcado si es un informe de impuestos de compras.
- **Informe:** Si está marcado, esta definición de informe de impuestos aparece en la lista del formulario Creación de informes de impuestos y puede seleccionarse para su generación. Si está desmarcado, la definición se guarda pero no está disponible para su selección.
- **Mostrar:** Si está marcado, esta línea de impuesto aparece como una fila visible en el resultado del informe. Si está desmarcado, la línea de impuesto sigue contribuyendo a los totales calculados, pero la fila individual queda oculta. Use esta opción cuando deba aparecer un subtotal sin mostrar cada línea que lo compone.
- **Nivel agrupación:** Marque esta casilla solo si este impuesto es una categoría de agrupación que contiene subimpuestos subordinados (por ejemplo, un impuesto padre "IVA" que agrupa "IVA 10%" e "IVA 21%"). Si el impuesto está definido de forma independiente sin subimpuestos, deje esta casilla desmarcada. En caso de duda, consulte la estructura de impuestos con su administrador del sistema.
- **Negativo:** Si está marcado, el informe se imprime con valores negativos; de lo contrario, se imprime con valores positivos.
- **Activo:** Si es un informe de impuestos activo.

Una vez configurado el informe de impuestos, use el formulario [Creación de informes de impuestos](create-tax-report.md) para generar el informe.

---

Este trabajo es una obra derivada de [Financial Management](http://wiki.openbravo.com/wiki/Financial_Management){target="\_blank"} por [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.
