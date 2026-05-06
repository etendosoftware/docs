---
tags:
  - Etendo Classic
  - Financial Management
  - Accounting
  - Journal Entries Report
  - Financial Reports
---

# Informe de Asientos Contables

:material-menu: `Aplicación` > `Gestión Financiera` > `Contabilidad` > `Herramientas de Análisis` > `Informe de Asientos Contables`

## Visión General

El Informe de Asientos Contables es una lista de todos los vouchers de diario de una organización y libro mayor, mostrados en orden cronológico.

Un asiento contable es el registro de datos financieros en un voucher de diario, de modo que el débito sea igual al crédito y los débitos se introduzcan antes que los créditos.

![](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/journal-entries-report-1.png)

Como se muestra en la imagen anterior, la sección "Filtros Primarios" permite al usuario especificar:

-   la "*Organización*" y el "*Libro Mayor*" para los que se requieren los datos financieros tomados de los asientos contables.

La sección "Filtros Avanzados" es ahora una sección desplegable. En esta sección, es posible especificar:

- un rango **Desde/Hasta Cuenta** para mostrar los asientos contables que tengan al menos una línea con una cuenta definida en el rango.
- un Tipo de Documento para acotar los datos financieros a mostrar en el informe únicamente a los relacionados con ese tipo de documento concreto.
    - Si el tipo de documento seleccionado tiene asociado un número de documento, por ejemplo un tipo de documento de factura, será posible acotar los datos mostrados a un "**Número de Documento**" específico.
- el "**Número de Página Inicial**" *a mostrar en el formato PDF del informe*
- el **"Número de Asiento Inicial"** a mostrar en el formato PDF del informe
- la **"Descripción del Asiento**" a mostrar en el formato PDF del informe

El resto de las casillas están seleccionadas por defecto para mostrar:

- los asientos contables *"**regulares**"*:
    - estos asientos son los generados al contabilizar cualquiera de los tipos de documento de Etendo o al contabilizar un Asiento Manual de Libro Mayor sin marcar como "Apertura".
- los asientos contables *"**de apertura**"*:
    - estos asientos se generan automáticamente por Etendo tras el cierre de un ejercicio fiscal determinado
    - estos asientos también pueden generarse manualmente al contabilizar un Asiento Manual de Libro Mayor cuando sus asientos están marcados como "Apertura".
- los asientos contables de **"cierre"**:
    - estos asientos se generan automáticamente por Etendo tras el cierre de un ejercicio fiscal determinado
- y por último los asientos contables *"**de cierre de P&L**"*:
    - estos asientos se generan automáticamente por Etendo tras el cierre de un ejercicio fiscal determinado

Por último, y de la misma manera que para el resto de informes financieros, el Informe de Asientos Contables puede generarse en:

- formato *HTML*. Ejemplo de salida en HTML:

![](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/journal-entries-report-2.png)

- formato *PDF* mediante el botón de acción "Imprimir Registro" de la barra de herramientas
- o formato *XML* mediante el botón de acción "Exportar a Excel" de la barra de herramientas.

---

Este trabajo es una obra derivada de [Financial Management](http://wiki.openbravo.com/wiki/Financial_Management){target="\_blank"} por [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.
