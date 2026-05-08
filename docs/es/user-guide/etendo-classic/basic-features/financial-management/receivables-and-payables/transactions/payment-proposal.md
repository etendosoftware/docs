---
tags:
  - Etendo Classic
  - Financial Management
  - Payment Proposal
  - Supplier Payments
  - Receivables and Payables
---

# Propuesta de Pago { #payment-proposal }

:material-menu: `Aplicación` > `Gestión Financiera` > `Cobros y Pagos` > `Transacciones` > `Propuesta de Pago`

## Visión General { #overview }

La propuesta de pago es una herramienta que ayuda al usuario a realizar pagos seleccionando los documentos relacionados con un método de pago determinado o programados para pagarse antes de una fecha de vencimiento determinada. El sistema propone lo que debe pagarse en función de los criterios de selección proporcionados por el usuario.

Los pasos a seguir son:

- _Introducir_ los criterios de selección, que podrían ser:
  - introducir un tercero determinado cuyas facturas se quieren pagar
  - introducir un método de pago determinado, por ejemplo "Transferencia Bancaria" si se quieren generar a la vez todas las transferencias bancarias del mes
  - o introducir una fecha determinada en el campo "Inc. documentos hasta esta fecha" si se quieren pagar todas las facturas con fecha de vencimiento anterior a esa fecha
  - etc.
- _Ejecutar_ el proceso "**Seleccionar Pagos Esperados**".  
  Este proceso selecciona los eventos de pago programados de los pedidos/facturas que coinciden con los criterios de selección introducidos y realiza una propuesta de pago.
- _Seleccionar_ los documentos (pedidos y/o facturas) de la propuesta que la organización desea pagar.
- _Enviar_ la propuesta.  
  Esta acción rellena la pestaña Líneas de la ventana de propuesta de pago.
- _Ejecutar_ el proceso "**Generar Pagos**".  
  Este proceso genera el pago o los pagos teniendo en cuenta que:
  - un pago puede agrupar pedidos/facturas separados a pagar del mismo proveedor en un único pago.
  - o agrupar pedidos/facturas separados a pagar independientemente del proveedor en un único pago.

### Cabecera { #header }

La ventana de propuesta de pago permite al usuario introducir un conjunto de criterios de selección que le ayudan a realizar pagos de forma masiva.

![Cabecera Propuesta de Pago](../../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions/payment-proposal/payment-proposal-1.png)

Los campos a destacar son:

- **Tercero:** si se introduce un tercero, solo se propondrán los documentos vencidos de ese tercero.
- **Método de Pago:** si se introduce un método de pago, solo se propondrán los documentos que tengan asignado ese método de pago; sin embargo, las facturas o pedidos pendientes vinculados a diferentes métodos de pago también pueden seleccionarse eliminando los filtros implícitos aplicados (haciendo clic en el icono de embudo).
- **Pagado Desde:** es posible seleccionar la Cuenta Financiera que tiene configurado el método de pago anterior, desde donde se necesita extraer el dinero.
- **Moneda**: es posible seleccionar una moneda si el método de pago seleccionado está configurado para permitir realizar pagos en múltiples monedas. En ese caso, se muestra un campo que permite al usuario introducir el "Tipo de Cambio" entre la moneda del documento y la moneda de la cuenta financiera.
- **Inc. documentos hasta esta fecha:** Este campo permite al usuario introducir una fecha; por tanto, los documentos de la propuesta tendrán una fecha de vencimiento igual o anterior a la fecha indicada.

El botón de cabecera **Seleccionar Pagos Esperados** muestra los documentos que coinciden con los criterios de selección introducidos anteriormente.

!!! info
    Tenga en cuenta que los datos mostrados en la grilla se filtran usando los criterios anteriores (filtro implícito). Para ver facturas o pedidos pendientes de un Método de Pago diferente, por ejemplo, es necesario limpiar los filtros haciendo clic en el icono de embudo.

![Seleccionar Pagos Esperados](../../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions/payment-proposal/payment-proposal-1.png)

Además, la ventana "Seleccionar Pagos Esperados" permite al usuario:

- introducir una "**Referencia de Proveedor**", si la hubiera
- modificar el importe del "**Pago**" si el importe a pagar es inferior al importe pendiente
- y seleccionar la casilla de verificación "**Cancelación**" para cancelar la diferencia entre el importe pendiente y el importe del pago introducido por cada documento/fila seleccionado.

El botón "**Enviar**" finaliza el proceso y consigue que la selección se rellene en la pestaña Líneas.

Finalmente, el botón de cabecera **Generar Pagos** permite al usuario realizar dos acciones:

- ya sea **agrupar pagos separados del mismo proveedor en un pago**,  
  esta opción permite al usuario agrupar pedidos/facturas pendientes del mismo proveedor para pagarlos en una única transacción de pago.
- o **agrupar todos los pedidos/facturas en un pago**,  
  esta opción permite al usuario agrupar pedidos/facturas pendientes para pagarlos en una única transacción de pago, independientemente del proveedor.

Una vez ejecutado:

- Un mensaje del sistema muestra el/los número/s del/los pago/s creado/s.
- La información de resumen del pago se refleja en la Barra de Estado de la ventana Propuesta de Pago.
- La información del Plan de Pago y del Monitor de Pagos de todos los documentos involucrados se actualiza.
- Finalmente, el Estado del Pago cambia a _Pendiente de Ejecución_ cuando se define un Tipo de Ejecución _Automático_, o a _Pago Realizado_ si la ejecución es _Manual_. Si hay un proceso de ejecución definido, puede ejecutarse haciendo clic en el botón Ejecutar Pago.

### Líneas { #lines }

La pestaña de líneas muestra las transacciones (pedidos y/o facturas) incluidas en la propuesta de pago.

![Líneas Propuesta de Pago](../../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions/payment-proposal/payment-proposal-1.png)

Una propuesta de pago puede ser "**Reactivada**", lo que significa que el/los pago/s creado/s se eliminan y, por tanto, se eliminan de la ventana Pago.

---

This work is a derivative of [Financial Management](http://wiki.openbravo.com/wiki/Financial_Management){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
