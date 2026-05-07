---
tags:
  - Etendo Classic
  - Financial Management
  - Financial Type Configuration
  - Financing
  - Accounting Transactions
---

# Configuración de Tipo de financiación

:material-menu: `Aplicación` > `Gestión Financiera` > `Contabilidad` > `Transacciones` > `Configuración de Tipo de financiación`

## Descripción general

Esta funcionalidad permite introducir en el sistema todas las financiaciones que tiene la empresa. Es posible explotar la información a través del informe de pool bancario.
Dependiendo del producto financiero utilizado en esta nueva ventana **Financiación**, Etendo genera planes de financiación de forma automática (Leasing, Renting y Préstamos) y también gestiona las facturas y pagos desde esta misma ventana.

Los productos de financiación habituales son:

- Anticipo sobre Facturas
- Aval Bancario
- Confirming
- Comercio Exterior
- Cuenta de Crédito
- Factoring
- Leasing
- Préstamos
- Renting
- Tarjetas de Crédito.

Estos métodos de financiación se cargan en el sistema mediante un dataset.

!!! info
    Para más información, visite [Tipo de financiación](../setup/financial-type.md).


## Cabecera
La cabecera principal contiene los siguientes campos:

- **Organización**: lista desplegable de organizaciones.
- **Tipo de financiación**: lista desplegable de métodos: Anticipo sobre Facturas, Aval Bancario, Confirming, Comercio Exterior, Cuenta de Crédito, Factoring, Leasing, Préstamos, Renting y Tarjetas de Crédito.
- **Banco/Entidad financiera**: lista desplegable de la ventana de terceros.
- **Cuenta Financiera**: lista desplegable de la ventana Cuenta Financiera.
- **Método de Pago**: lista desplegable de los métodos de pago indicados en la cuenta financiera seleccionada.
- **Nombre**: campo libre para añadir información.
- **Fecha**: campo de fecha (fecha de firma del contrato).
- **Fecha de Vencimiento**: campo de fecha.
- **Carencia (Meses)**: campo numérico (enteros).
- **Moneda**: lista desplegable de la ventana de monedas.
- **Importe concedido**: campo numérico con 2 decimales.
- **Importe Dispuesto**: campo numérico con 2 decimales.
- **Importe Disponible**: campo numérico con 2 decimales.
- **Valor Residual**: campo numérico con 2 decimales.
- **Nº de Cuotas**: campo numérico entero.
- **% Interés Anual**: campo numérico de porcentaje con 2 decimales.
- **Comisión Periódica**: campo numérico con 2 decimales.
- **Gastos Financieros de Apertura**: campo numérico con 2 decimales.
- **Frecuencia**: lista desplegable (Mensual, Bimensual, Trimestral, Trimestral, Semestral, Anual).
- **Fecha de Pago**: campo numérico. Entero (límite de 31).
- **Finalidad**: campo libre para añadir información.
- **Garantía**: campo libre para añadir información.
- **% Comisión por Cancelación Anticipada**: campo numérico de porcentaje con 2 decimales.
- **% Comisión por Amortización Anticipada**: campo numérico de porcentaje con 2 decimales.
- **Cuenta contable a largo plazo**: campo informativo para indicar la cuenta contable del árbol de cuentas.
- **Cuenta contable a corto plazo**: campo informativo para indicar la cuenta contable del árbol de cuentas.
- **Cuenta contable de opción de compra**: campo informativo para indicar la cuenta contable del árbol de cuentas.
- **Proyecto**: lista desplegable de la ventana "Proyecto multifase".
- **Centro de costos**: lista desplegable de la ventana "Centro de costos".

![](../../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/transactions/financial-type-configuration/financial-type-configuration-1.png)

## Líneas

Las líneas contienen los siguientes campos:

- **Nº de Cuota**: campo numérico. Entero.
- **Fecha de Amortización/Vencimiento**: campo de fecha.
- **Cuota**: campo numérico con 2 decimales.
- **Amortización/Renting**: campo numérico con 2 decimales.
- **Interés**: campo numérico con 2 decimales.
- **Comisión**: campo numérico con 2 decimales.
- **Amortización Total**: campo numérico con 2 decimales.
- **Amortización Pendiente**: campo numérico con 2 decimales.
- **Factura**: se muestra el enlace a la factura generada (Leasing/Renting).
- **Pago**: se muestra el enlace al pago generado (Préstamo).
- **Tercero Financiero**: lista desplegable de terceros (se utiliza como campo informativo para saber, en el caso de anticipos sobre facturas, Confirming, Comex, cuánto se ha financiado a cada uno).
- **Fecha**: campo de fecha.
- **Proyecto**: lista desplegable de la ventana "Proyecto multifase".
- **Centro de costos**: lista desplegable de la ventana "Centro de costos".

![](../../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/transactions/financial-type-configuration/financial-type-configuration-2.png)

## Contabilidad

Existen tres secciones: "Amortización/Renting", "Interés" y "Comisión". Hay seis campos en total, donde tres de ellos representan el producto y los otros tres el concepto contable. Los 2 campos (producto y concepto contable) no pueden rellenarse en la misma sección. En cada uno de estos campos relacionados, el producto debe indicarse desde la ventana **Productos** o el **Concepto Contable** si está activada la casilla de verificación **Disponible en Facturas Financieras** necesaria para asignar a cada columna. En el caso del tipo de financiación **Préstamo**, es obligatorio rellenar la parte de conceptos contables.

 ![](../../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/transactions/financial-type-configuration/financial-type-configuration-3.png)


## Cálculo de Préstamo, Leasing o Renting en la pestaña de líneas

Rellene los campos necesarios de la cabecera según la descripción de cada uno de ellos indicada en la parte superior del documento. Dicha información permite la creación automática del plan de financiación, que se crea haciendo clic en el botón "Actualizar Plan de Financiación" en el margen superior derecho de la ventana.

![](../../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/transactions/financial-type-configuration/financial-type-configuration-4.png)

### Préstamo:
- **Nº de Cuota**: comienza con el número de cuota 0 y el campo "amortización pendiente" tiene el valor indicado en el campo "importe concedido", mientras que el campo "fecha" tiene la fecha indicada en el campo "fecha" de la cabecera. El resto de las cuotas son correlativas, incrementándose de 1 en 1.
- **Fecha de Amortización/Vencimiento**: para ver la fecha de la cuota número 1 del plan de financiación, se indica al hacer clic en el nuevo botón "Crear Plan de Financiación". Se muestra una ventana emergente para indicar la fecha. Haga clic en "Aceptar". El resto de las líneas se crean con la frecuencia indicada en el campo "Frecuencia", con la fecha de la última cuota creada y la fecha indicada en el campo "fecha de pago". Si se indica una carencia, la fecha indicada al hacer clic en "Crear Plan de Financiación" es la primera cuota de carencia; el resto de las cuotas, tanto de carencia como de amortización, se crean según la frecuencia indicada. Las cuotas de carencia se indican con el número de cuota 0.
- **Cuota**: inicialmente, se calcula la misma cuota para todo el préstamo. Si el tipo de interés cambia durante el período del préstamo, la cuota cambia. Para ello, cambie el 1% del tipo de interés de la cabecera y haga clic en el nuevo botón de la cabecera "Actualizar Plan de Financiación". La información se actualiza desde la siguiente línea hasta la última línea con un pago asociado.
- **Amortización/Renting**: importe amortizado en la cuota.
- **Interés**: interés a pagar en la cuota.
- **Comisión**: se rellena con la información introducida en el campo "Comisión Periódica" de la cabecera, si la hubiera. Si no, el valor es 0.
- **Amortización Total**: suma de los valores de la columna anterior "amortización/renting" respecto a la misma línea calculada. Campo de solo lectura.
- **Amortización Pendiente**: diferencia entre el "importe concedido" indicado en la cabecera y la "amortización total" de la misma línea calculada. Campo de solo lectura.
- **Pago**: se muestra el pago relacionado.
- **Tercero**: si se indica en la cabecera, el tercero se muestra en este campo. Si no, se puede indicar manualmente.
- **Proyecto**: si se indica en la cabecera, la información del proyecto se muestra en este campo. Si no, se puede indicar manualmente.
- **Centro de costos**: si se indica en la cabecera, el centro de costos se muestra en este campo. Si no, se puede indicar manualmente.

 ![](../../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/transactions/financial-type-configuration/financial-type-configuration-5.png)

 ![](../../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/transactions/financial-type-configuration/financial-type-configuration-6.png)

### Leasing:
- **Nº de Cuota**: comienza con el número de cuota 0 y el campo "amortización pendiente" tiene el valor indicado en el campo "importe concedido", mientras que el campo "fecha" tiene la fecha indicada en el campo correspondiente. El resto de las cuotas son correlativas, incrementándose de 1 en 1.
- **Fecha de Amortización/Vencimiento**: para ver la fecha de la cuota número 1 del plan de financiación, se indica al hacer clic en el nuevo botón "Crear Plan de Financiación". Se muestra una ventana emergente para indicar la fecha. Haga clic en "Aceptar". El resto de las líneas se crean con la frecuencia indicada en el campo "Frecuencia", con la fecha de la última cuota creada y la fecha indicada en el campo "fecha de pago". Si se indica una carencia, la fecha indicada al hacer clic en "Crear Plan de Financiación" es la primera cuota de carencia; el resto de las cuotas, tanto de carencia como de amortización, se crean según la frecuencia indicada. Las cuotas de carencia se indican con el número de cuota 0.
- **Cuota**: inicialmente, se calcula la misma cuota para todo el leasing. Si el tipo de interés cambia durante el período del leasing, la cuota cambia. Para ello, cambie el 1% del tipo de interés de la cabecera y haga clic en el nuevo botón de la cabecera "Actualizar Plan de Financiación". La información se actualiza desde la siguiente línea hasta la última línea con una factura asociada. Por último, se incluye una última línea con el valor residual, si lo hubiera, en la misma fecha que la última línea calculada.
- **Amortización/Renting**: importe amortizado en la cuota.
- **Interés**: interés a pagar en la cuota.
- **Comisión**: se rellena con la información introducida en el campo "Comisión Periódica" de la cabecera, si la hubiera. Si no, el valor es 0.
- **Amortización Total**: suma de los valores de la columna anterior "amortización/renting" respecto a la misma línea calculada. Campo de solo lectura.
- **Amortización Pendiente**: diferencia entre el "importe concedido" indicado en la cabecera y la "amortización total" de la misma línea calculada. Campo de solo lectura.
- **Factura**: se muestra la factura relacionada.
- **Pago**: se muestra el pago relacionado.
- **Tercero**: si se indica en la cabecera, el tercero se muestra en este campo. Si no, se puede indicar manualmente.
- **Proyecto**: si se indica en la cabecera, la información del proyecto se muestra en este campo. Si no, se puede indicar manualmente.
- **Centro de costos**: si se indica en la cabecera, el centro de costos se muestra en este campo. Si no, se puede indicar manualmente.

 ![](../../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/transactions/financial-type-configuration/financial-type-configuration-7.png)

 ![](../../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/transactions/financial-type-configuration/financial-type-configuration-8.png)

### Renting
- **Nº de Cuota**: comienza con el número de cuota 0 y el resto de las cuotas son correlativas, incrementándose de 1 en 1.
- **Fecha de Amortización/Vencimiento**: para ver la fecha de la cuota número 1 del plan de financiación, se indica al hacer clic en el nuevo botón "Crear Plan de Financiación". Se muestra una ventana emergente para indicar la fecha. Haga clic en "Aceptar". El resto de las líneas se crean con la frecuencia indicada en el campo "Frecuencia", con la fecha de la última cuota creada y la fecha indicada en el campo "fecha de pago".
- **Cuota**: resultado de dividir el "importe concedido" entre el número de cuotas.
- **Amortización/Renting**: importe amortizado en la cuota.
- **Interés**: interés a pagar en la cuota.
- **Comisión**: se rellena con la información introducida en el campo "Comisión Periódica" de la cabecera, si la hubiera. Si no, el valor es 0.
- **Factura**: se muestra la factura relacionada.
- **Tercero**: si se indica en la cabecera, el tercero se muestra en este campo. Si no, se puede indicar manualmente.
- **Proyecto**: si se indica en la cabecera, la información del proyecto se muestra en este campo. Si no, se puede indicar manualmente.
- **Centro de costos**: si se indica en la cabecera, el centro de costos se muestra en este campo. Si no, se puede indicar manualmente.

 ![](../../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/transactions/financial-type-configuration/financial-type-configuration-9.png)

 ![](../../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/transactions/financial-type-configuration/financial-type-configuration-10.png)

#### Generación de pagos o facturas

Una vez creado el plan de amortización, se pueden generar pagos (préstamos) y facturas (leasing y renting) para cada línea. Esto es posible de forma individual (línea a línea) o en grupos (se pueden seleccionar 3 líneas y se generan 3 pagos/facturas diferentes).

Para ello, seleccione la/s línea/s necesaria/s y haga clic en los botones "Crear Pago" (préstamos) o "Crear Factura" (leasing o renting) que aparecen en el margen superior derecho de la ventana.

**Préstamo**:

 ![](../../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/transactions/financial-type-configuration/financial-type-configuration-11.png)

**Leasing**:


 ![](../../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/transactions/financial-type-configuration/financial-type-configuration-12.png)


**Renting**:

 ![](../../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/transactions/financial-type-configuration/financial-type-configuration-13.png)


##### Cuenta de crédito y tarjetas de crédito informadas en cuentas financieras.

La información de cuenta de crédito y tarjeta de crédito se introduce automáticamente. Para ello, cree una nueva cabecera e indique el método de financiación, "Cuenta de crédito" o "Tarjeta de crédito". A continuación, se habilitará el botón "Añadir Cuenta financiera" en el margen superior derecho.

![](../../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/transactions/financial-type-configuration/financial-type-configuration-14.png)

Al hacer clic en el botón, se muestra una ventana emergente y es posible seleccionar una cuenta financiera (solo se muestran las que tienen marcada la opción "Añadir al pool bancario").

![](../../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/transactions/financial-type-configuration/financial-type-configuration-15.png)

![](../../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/transactions/financial-type-configuration/financial-type-configuration-16.png)

Una vez creada esta cuenta de crédito/tarjeta de crédito en las financiaciones y si es necesario actualizar su información, haga clic en el botón "Actualizar cuenta financiera" en el margen superior derecho.

![](../../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/transactions/financial-type-configuration/financial-type-configuration-17.png)

Los campos que se copian de la cuenta o tarjeta de crédito son los equivalentes en el campo "Cuenta Financiera", el importe del valor residual que se indica en el campo "Importe Disponible" y el importe del "Límite de Crédito" que se indica en el campo "Importe concedido". Todos los demás campos de la cabecera son editables para incluir el resto de la información.

---

This work is a derivative of [Financial Management](http://wiki.openbravo.com/wiki/Financial_Management){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
