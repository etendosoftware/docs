---
tags:
  - Etendo Classic
  - Financial Management
  - Accounting
  - General Ledger Report
  - Financial Reports
---

# Libro mayor { #general-ledger-report }

:material-menu: `Aplicación` > `Gestión Financiera` > `Contabilidad` > `Herramientas de análisis` > `Libro mayor`

## Descripción general { #overview }

El informe Libro mayor lista cada "subcuenta" del libro mayor y sus asientos de débito y crédito dentro de un periodo de tiempo determinado.
   
![](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/general-ledger-report/general-ledger-report-1.png)

Como se muestra en la imagen anterior, los campos a completar para generar este informe son:

- la *"Organización"* para la que se requiere la información contable.  
    Una vez más, la información contable proporcionada por este informe depende del tipo de organización seleccionado:
    - la información contable mostrada puede estar relacionada únicamente con una organización "Genérica" perteneciente a una "Entidad Legal con Contabilidad"
    - o puede ser una consolidación en caso de seleccionar una "Entidad Legal con Contabilidad" u "Organización" que tenga otras organizaciones subordinadas.
- la opción *"Mostrar Balance de Apertura"*, que ocultará los asientos cuyo saldo sea cero. (P. ej., eliminando asientos de cobros/pagos de facturas una vez que estas han sido pagadas.)
- y el *"Libro mayor"* correspondiente, que también dependerá de la Organización seleccionada previamente.

Es posible acotar la información contable a mostrar en el informe por:

- un rango de "*importes*"
- un conjunto de *"subcuentas"*
- y un conjunto de *"dimensiones contables"* como tercero, producto y proyecto

Por último, también es posible:

- *"agrupar"* la información por cualquiera de las dimensiones contables
- e introducir un *"Número de Página Inicial"* para el informe

Una vez introducidos correctamente todos los datos, el botón "Buscar" muestra el resultado del informe en la misma ventana:

- los asientos contables mostrados para cada subcuenta se ordenan por fecha contable y, además, se muestra el saldo de la subcuenta para cada asiento contable.

Las flechas de la barra de herramientas permiten al usuario navegar por el resultado del informe mostrado en la ventana.

El informe Libro mayor también puede visualizarse y guardarse en formato Excel y PDF:

- Formato Excel pulsando el botón de acción *"Exportar a Excel"* de la barra de herramientas:
    - Este formato contiene una lista de todos los asientos contables por cada subcuenta sin agrupar, por lo que es posible agruparlos según se desee.
    - También lista las dimensiones contables correspondientes de cada asiento contable.
-   Formato PDF pulsando el botón de acción *"Imprimir Registro"* de la barra de herramientas:
    - Este formato incluye un saldo "Inicial" de cada subcuenta, el saldo "Subtotal" de cada subcuenta para el periodo determinado y calcula el saldo "Total" de cada subcuenta.

![](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/general-ledger-report/general-ledger-report-2.png)

---

Este trabajo es una obra derivada de [Financial Management](http://wiki.openbravo.com/wiki/Financial_Management){target="\_blank"} por [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.
