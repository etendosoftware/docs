---
tags:
  - How to
  - Etendo classic
  - Create Accounts File
  - Árbol de cuentas
  - Plan de cuentas
  - CSV
---

# Cómo crear archivos de cuentas

## Visión general
Etendo permite importar el Plan de cuentas mediante un archivo [CSV](https://en.wikipedia.org/wiki/Comma-separated_values){target="\_blank"} (valores separados por comas) con una estructura concreta. Este archivo CSV se incluye posteriormente en un módulo que puede distribuirse e instalarse desde [Etendo marketplace](https://marketplace.etendo.cloud/#/){target="\_blank"}.

Para crear el archivo CSV, se recomienda utilizar cualquier software de hoja de cálculo que admita la exportación a CSV, como [LibreOffice Calc](https://www.libreoffice.org/){target="\_blank"}.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/CSVfile.png)

## Estructura del archivo

El archivo es un archivo de texto plano, con comas (,) como separador de campos, que define todas las cuentas. Para garantizar que su plan de cuentas se importe correctamente, el archivo debe estar codificado usando el conjunto de caracteres [UTF-8](https://en.wikipedia.org/wiki/UTF-8){target="\_blank"}.

Para crear su propio archivo CSV, puede descargar el [archivo CSV del Plan de cuentas español](../../../assets/developer-guide/etendo-classic/how-to-guides/COA.csv) y utilizarlo como plantilla para adaptarlo a sus necesidades, o puede crear el archivo completo desde cero.

Cada campo del archivo comprende una línea.

| Nombre del campo        | Descripción                                                       | Obligatorio | Longitud y tipo                  |
|-------------------------|-------------------------------------------------------------------|-------------|----------------------------------|
| Identificador           | Este es el identificador único que define la cuenta.              | Sí          | Hasta 20 caracteres alfanuméricos |
| Nombre                  | El nombre de la cuenta                                            | Sí          | Hasta 60 caracteres              |
| Descripción             | Breve descripción de la cuenta                                    | No          | Hasta 255 caracteres             |
| Tipo de cuenta bancaria | Define el tipo de la cuenta. Define el tipo de la cuenta. Puede contener cualquier texto, pero solo se utiliza el primer carácter. Este primer carácter debe ser uno de los siguientes:  <ul><li>A:Activos</li><li>L:Pasivo</li><li>O:Patrimonio neto</li><li>E:Gasto</li><li>R:Ingresos</li><li>M:Nota</li></ul>                                | Sí          | Cualquier longitud, pero solo se utiliza el primer carácter. |
| Naturaleza de la cuenta (crédito/débito) | Define el signo de la cuenta en los informes. Una cuenta tiene dos columnas: débito y crédito. Los importes se añaden a una de las columnas en cada asiento. Al final del día, una cuenta tendrá dos importes: importes de débito e importes de crédito. El signo de la cuenta completa (debido a los movimientos de débito y crédito) puede establecerse siguiendo una de las siguientes reglas: <ul><li>N: Natural (el signo es siempre positivo)</li><li>D: Débito (el signo es positivo si el importe del débito es mayor que el del crédito; negativo en caso contrario)</li><li>C: Crédito (el signo es positivo si el importe del crédito es mayor que el del débito; negativo en caso contrario)</li><li>E: Vacío</li></ul>                  | Sí          | Cualquier longitud, pero solo se utiliza el primer carácter. |
| Controlado por documento | Si esta es una cuenta por defecto utilizada en la configuración del libro mayor, escriba "Sí". En caso contrario, escriba "No". Los registros con este campo establecido en Sí se procesan durante el proceso de configuración inicial del cliente | Sí | Debe ser Sí, No o vacío |
| Resumen de cuenta       | Este campo define la cuenta como una cuenta de resumen.           | Sí          | Debe ser Sí, No o vacío         |
| Cuenta por defecto      | Consulte a continuación para más detalles.                        | Sí          | Consulte a continuación el conjunto de valores válidos |
| Parent_Value            | Define la cuenta padre de la cuenta. La cuenta padre se ignora durante el proceso de configuración inicial del cliente.                             | No        | Debe ser el identificador de una cuenta de resumen válida |
| Nivel del elemento      | Define el nivel de la cuenta. El último nivel que corresponde con Resumen de cuenta = N, debe ser S (Subcuenta). Cualquier otro nivel puede añadirse a los existentes. Como están definidos en el diccionario como una lista de referencia, puede editar esta lista y modificar los valores mostrados para este campo, estableciendo todos los nuevos valores que necesite. Lo único que debe tenerse en cuenta es que el nivel más bajo debe ser 'S' Subcuenta, ya que los informes contables utilizan este valor. Los siguientes niveles se definen por defecto en Etendo Classic:<ul><li>C: Cuenta</li><li>D: Desglose</li><li>E: Encabezado</li><li>S: Subcuenta</li></ul>                                 | No        | Ilimitado, pero solo se utiliza la primera letra. |
| Operandos               | Si la cuenta es el producto de un cálculo entre otras cuentas, puede definir aquí los operandos. Por ejemplo, si el valor de la cuenta A es el resultado de sumar el valor de las cuentas B y C, el valor de la columna de operandos en el plan de cuentas sería B+C. Esta funcionalidad solo funciona si los operandos referidos ya se han insertado antes; de lo contrario, el sistema no puede encontrarlos al intentar insertarlos. | No | Ilimitado |
| Mostrar Valor           | El usuario puede, opcionalmente, establecer aquí el valor para el campo "Mostrar Valor" de la solapa Element Value. | No | Positivo, Negativo, Algebraico (valor por defecto si la celda está vacía) |
| Nodo de Título          | El usuario puede, opcionalmente, activar aquí el indicador "Nodo de Título" de la solapa Element Value. | No | Sí, No (valor por defecto si la celda está vacía) |

## ¿Qué cuentas deben definirse?

La forma en que defina su archivo de cuentas depende principalmente de si existen normas oficiales en su país. Por ejemplo, en países como Francia o España existen planes de cuentas estándar e informes contables generales. En este caso, debe definir un plan de cuentas con la estructura de los informes contables generales que incluya todas las cuentas. Otros países, como EE. UU., no tienen un plan definido, por lo que debe definir un plan general que se adapte a su empresa. La estructura del archivo debe incluir el Balance (con Activos, Pasivo y Patrimonio neto) y una cuenta de Pérdidas y Ganancias (con Gastos e Ingresos).

## Jerarquía de cuentas

El informe contable general tiene una estructura jerárquica. El Balance tiene dos lados, siguiendo la ecuación Activos = Pasivo + Patrimonio neto. El lado de Activos del balance está compuesto por diferentes tipos de activos: Activos corrientes y Activos a largo plazo, y cada uno puede tener diferentes subcuentas.

Los niveles de esta jerarquía pueden diferir de un árbol de cuentas a otro; el único requisito es que el último nivel, donde se realiza la contabilización, debe comenzar con la letra S (de Subcuenta).

La columna *Parent_Value* del archivo de cuentas crea la relación jerárquica entre cuentas. Esta columna especifica qué cuenta es la cuenta padre de la cuenta.

## Cuentas por defecto

Etendo Classic realiza la mayoría de los asientos contables automáticamente. Para habilitar los asientos contables automáticos, es necesario definir las cuentas por defecto. Con esta información, Etendo Classic construye el asiento contable con el número de cuenta definido en el plan de cuentas.

Las cuentas por defecto obligatorias se definen en el archivo del plan de cuentas con una constante que debe escribirse literalmente en la columna *Cuenta por defecto*. La siguiente tabla incluye una explicación de estas cuentas.

| Valor por defecto          | Tipo           | Descripción                                                             | Ejemplo de nombre de la cuenta                                   |
|----------------------------|----------------|-------------------------------------------------------------------------|-------------------------------------------------------------------|
| A_ACCUMDEPRECIATION_ACCT   | Activos        | Cuenta utilizada por el proceso de amortización para mostrar la depreciación de un activo | Amortización acumulada                                        |
| A_DEPRECIATION_ACCT        | Gasto          | Cuenta utilizada por el proceso de amortización para definir la pérdida de valor causada por la depreciación de un activo | Gasto por depreciación                                             |
| B_ASSET_ACCT               | Activos        | La cuenta utilizada para los movimientos de una cuenta bancaria         | Cuenta bancaria                                                     |
| B_EXPENSE_ACCT             | Gasto          | Cargos realizados por el banco                                          | Comisión bancaria                                                      |
| B_INTRANSIT_ACCT           | Activos        | Cuenta utilizada para el periodo entre la liquidación y el registro del extracto bancario | Banco en tránsito                                                  |
| B_REVALUATIONGAIN_ACCT     | Ingresos       | Cuenta para los ingresos debidos a beneficios por revalorizaciones de moneda extranjera | Beneficio por plusvalías                                            |
| B_REVALUATIONLOSS_ACCT     | Gasto          | Cuenta para los gastos debidos a pérdidas por revalorizaciones de moneda extranjera | Pérdida por minusvalías                                            |
| C_RECEIVABLE_ACCT          | Activos        | Cuenta para los cobros pendientes de una factura. Se crean en el proceso de facturación y se cancelan cuando el cobro se realiza o se anula.                | Cuentas a cobrar                                              |
| C_PREPAYMENT_ACCT          | Activos        | La cuenta Prepago del cliente indica la cuenta que se utilizará para registrar anticipos de un cliente. Cualquier pago contra un pedido o cualquier pago que genere crédito se considera un anticipo. | Prepago del cliente                                              |
| CB_ASSET_ACCT              | Activos        | Cuenta para la caja menor utilizada por la empresa                      | Caja menor                                                       |
| CB_CASHTRANSFER_ACCT       | Activos        | Cuenta utilizada para el dinero transferido desde o hacia la caja menor | Transferencia en caja menor                                           |
| CB_DIFFERENCES_ACCT        | Gasto          | Cuentas para diferencias en caja menor                                  | Diferencias de caja menor                                           |
| CURRENCYBALANCING_ACCT     | Gasto          | Cuenta utilizada para el ajuste de divisa (redondeo)                    | Ajuste de divisa                                               |
| DEFAULT_ACCT               | Gasto          | Cuenta utilizada cuando no existe una cuenta definida para otro valor por defecto | Cuenta por defecto                                                  |
| INCOMESUMMARY_ACCT         | Patrimonio neto | Cuenta utilizada para calcular el resultado del periodo. También se utiliza para mostrar el resultado en el balance antes del proceso de cierre | Resumen de contabilidad                                                   |
| NOTINVOICEDRECEIPTS_ACCT   | Pasivo         | Cuenta utilizada para los albaranes que aún no se han facturado. Solo se utiliza si la empresa está configurada para contabilizar envíos | Albaranes no facturados                                            |
| P_ASSET_ACCT               | Activos        | Cuenta utilizada para inmovilizados                                     | Inmovilizado del producto                                                    |
| P_COGS_ACCT                | Gasto          | Cuenta para el coste de los bienes vendidos. Se utiliza en el envío del producto | Coste de los bienes vendidos                                               |
| P_COGS_RETURN_ACCT         | Gasto          | Cuenta para el coste de los bienes devueltos. Se utiliza en el envío de una devolución de un producto | Coste de los bienes devueltos                                           |
| P_EXPENSE_ACCT             | Gasto          | Cuenta utilizada para los gastos de facturas de compra                  | Costo del servicio                                                    |
| P_INVOICEPRICEVARIANCE_ACCT | Gasto         | Desviación del precio de factura                                        | Desviación pr. factura                                           |
| P_REVENUE_ACCT             | Ingresos       | Cuenta utilizada para los ingresos de facturas de venta                 | Ventas                                                            |
| P_REVENUE_RETURN_ACCT      | Ingresos       | Cuenta utilizada para las devoluciones de facturas de venta             | Devolución                                                          |
| RETAINEDEARNING_ACCT       | Patrimonio neto | Cuenta utilizada para beneficios y pérdidas de periodos anteriores. Recibe el valor del resumen de contabilidad si está definido | Reservas                                                |
| SUSPENSEBALANCING_ACCT     | Nota           | Cuenta utilizada en el proceso contable si el asiento contable no está cuadrado y está definido para generar un asiento contable | Cuenta de asiento no cuadrado                                               |
| SUSPENSEERROR_ACCT         | Nota           | Cuenta utilizada cuando el proceso contable produce un error y está definido para generar un asiento contable | Cuenta de error                                                   |
| T_CREDIT_ACCT              | Activos        | Impuesto que la empresa tiene a su favor                                | Impuestos a cobrar                                                  |
| T_CREDIT_TRANS_ACCT        | Activos        | Cuenta transitoria para el IVA de caja que aún no ha sido cobrado por la empresa | Impuestos transitorios a cobrar                                       |
| T_DUE_ACCT                 | Pasivo         | Impuesto adeudado por la empresa                                        | Impuesto repercutido                                                          |
| T_DUE_TRANS_ACCT           | Pasivo         | Cuenta transitoria para el IVA de caja que aún no ha sido cobrado por la empresa | Impuesto transitorio repercutido                                               |
| V_LIABILITY_ACCT           | Pasivo         | Cuenta para los pagos pendientes de una factura. Se crean en el proceso de facturación y se cancelan cuando el pago se realiza o se anula | Cuentas a pagar                                                 |
| V_PREPAYMENT_ACCT          | Pasivo         | La cuenta Pagos por adelantado del proveedor indica la cuenta utilizada para registrar anticipos de un proveedor. Cualquier pago contra un pedido o cualquier pago que genere crédito se considera un anticipo. | Pagos por adelantado del proveedor                                                |
| W_DIFFERENCES_ACCT         | Gasto          | Ganancias o pérdidas debidas a diferencias en el inventario             | Pérdida de inventario                                                   |
| W_INVENTORY_ACCT           | Activos        | Cuenta utilizada para registrar el valor de su inventario               | Cuenta de activo de inventario                                          |
| WRITEOFF_ACCT              | Gasto          | Cuenta utilizada para importes incobrables                              | Deudas incobrables                                                        |

## Exportación del Plan de cuentas al archivo CSV

Una vez que hemos introducido todas las cuentas en nuestra hoja de cálculo, es el momento de exportarla a un archivo CSV. Al exportar, el software le permitirá configurar el formato CSV concreto a utilizar. Es importante asegurarse de que se introducen los siguientes valores:

- Conjunto de caracteres: *UTF-8*
- Delimitador de campo: , (coma)
- Delimitador de texto: " (comillas dobles)

![](../../../assets/developer-guide/etendo-classic/how-to-guides/CSVfile_Export.png)

!!!note
    Si posteriormente desea editar este archivo CSV en su software de hoja de cálculo, recuerde utilizar esta configuración al abrirlo.

## Plan de cuentas en Etendo Classic

Después del [proceso de configuración inicial del cliente](how-to-run-an-initial-client-setup-process.md), el usuario puede encontrar el Plan de cuentas correspondiente en la ventana *Árbol de cuentas* de Etendo Classic.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/chartofaccountsics.png)

---

Este trabajo es una obra derivada de [Creación de archivos de cuentas](https://wiki.openbravo.com/wiki/Creating_Accounts_Files){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.