---
title: Esquema contable
tags:
    - General
    - Ledger
    - Configuration
    - Financial Management
    - Setup
    - Accounting
---

# Esquema contable

:material-menu: `Aplicación` > `Gestión Financiera` > `Contabilidad` > `Configuración` > `Esquema contable`

## Visión general

La **configuración del libro mayor (GL)** define cómo se contabilizan las transacciones financieras de una organización en el libro mayor.

Se crea una configuración de GL siempre que se seleccione un módulo de referencia de **archivo CSV o un Plan de Cuentas (CoA)** durante el proceso de [Crear entidad](../../../general-setup/getting-started.md#initial-client-setup) o los procesos de [Crear organización](../../../general-setup/enterprise-model/initial-organization-setup.md).

La configuración del libro mayor creada por defecto puede personalizarse posteriormente para adaptarse a las necesidades de la organización.

- Si se configura a **nivel de entidad**, el GL se asigna a la organización (\*) y está disponible para todas las organizaciones dentro de esa entidad.

- Si se configura a **nivel de organización**, el GL está disponible solo para esa organización y sus descendientes.

!!!info
    Además de una configuración del libro mayor, esos archivos contables también crean el Árbol de cuentas o Plan de Cuentas de la organización y las cuentas por defecto del libro mayor.

!!!info
    Etendo proporciona archivos contables a través de los módulos de Plan de Cuentas incluidos en un [Localization Bundle](../../../../optional-features/bundles/spain-localization/overview.md) si está disponible para su país.

Adicionalmente, una configuración del libro mayor también puede crearse **manualmente**, pero una vez que se haya creado el correspondiente [Árbol de cuentas](#árbol-de-cuentas).

!!!info
    Para más información, visite [Cómo crear una configuración del libro mayor](../../../../how-to-guides/how-to-create-a-general-ledger-configuration.md).

Por último, es importante remarcar que la configuración del GL y el CoA están vinculados, ya que **Cuenta** es una dimensión obligatoria del GL.

### Ventana Esquema contable

La ventana Esquema contable permite al usuario revisar y mantener las configuraciones del libro mayor creadas por defecto y crear nuevas si es necesario.

![alt text](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/set-up/gl-configuration1.png) 

Campos a tener en cuenta:

Una configuración del libro mayor creada por **Valor por defecto** puede modificarse para adaptarse a las necesidades de la organización cambiando las características siguientes:

1. El campo **Moneda**:

    - La moneda por defecto proviene de la configuración de entidad/organización.
    - Puede cambiarse antes de que comience la contabilización.
    - Una organización puede tener **múltiples GL en diferentes monedas**.

        - Ejemplo: F&B España contabiliza tanto en USD (heredada) como en EUR (GL propio).
        - Resultado: dos informes de asiento, uno por libro mayor.

2. La casilla de verificación **Permitir negativos**: define si se permiten contabilizaciones negativas.

    - Activada: las anulaciones se contabilizan con importes negativos.
    - Desactivada: las anulaciones se vuelven a contabilizar con signos de débito/crédito opuestos.

        Por ejemplo, una factura de compra genera la contabilización siguiente:

        |     |     |     |     |
        | --- | --- | --- | --- |
        | Cuenta | Débito | Crédito | Comentarios |
        | Gastos del producto | Importe neto de línea |     | Una por línea de factura |
        | Impuesto reclamado | Importe de impuesto |     | Una por línea de impuesto |
        | Pasivo del proveedor |     | Importe total | Una por factura |

        Al anular:

        - Permitir negativos = SÍ (las contabilizaciones aparecen como valores negativos).
        - Permitir negativos = NO (las contabilizaciones se reclasifican: débito ↔ crédito).

3. La casilla de verificación **Centralizado**:

    - **Centralizado**: cuando es SÍ, el campo **Naturaleza de la cuenta (crédito/débito)** se oculta en la pestaña Valor del elemento de la ventana [Árbol de cuentas](#árbol-de-cuentas).

        - Es posible definir a nivel de libro mayor si los saldos de cualquier tipo de cuenta se van a mostrar como **Positivo** o **Negativo** en los estados financieros si se selecciona la casilla Centralizado:

            - Los saldos de **Activos Débito** se muestran como Positivo en el Balance.
            - Los saldos de **Pasivos Crédito** se muestran como Positivo en el Balance.
            - Los saldos de **Patrimonio neto Crédito** se muestran como Positivo en el Balance.
            - Los saldos de **Gastos Débito** se muestran como Positivo en la Cuenta de resultados.
            - Los saldos de **Ingresos Crédito** se muestran como Positivo en la Cuenta de resultados.

        !!!info
            Es posible desmarcar cualquiera de las casillas anteriores para mostrar cualquiera de los saldos como negativo.

        ![alt text](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/set-up/gl-configuration7.png)

    - **Centralizado**: cuando es NO, el campo **Naturaleza de la cuenta (crédito/débito)** no se oculta en la pestaña Valor del elemento de la ventana [Árbol de cuentas](#árbol-de-cuentas). Por lo tanto, la naturaleza de la cuenta de cada elemento del árbol de cuentas define cómo se mostrará el saldo de esa cuenta en los estados financieros.

    !!!info
        Es importante remarcar que la casilla **Centralizado** **no está seleccionada por defecto** para los libros mayores creados por defecto, ya que los correspondientes archivos CSV contables o los datos de referencia importados tienen su propia configuración mediante la Naturaleza de la cuenta (crédito/débito).

### Pestaña Dimensiones

La pestaña **Dimensiones** permite al usuario configurar las dimensiones del libro mayor de la organización o añadir dimensiones contables adicionales **no centralizadas** en la entidad.

Etendo permite al usuario gestionar dimensiones contables obligatorias y no obligatorias que deben introducirse en la sección Dimensiones de los documentos, que pueden contabilizarse en el libro mayor.

Las dimensiones obligatorias pueden rellenarse o no dependiendo de la categoría del documento que se esté creando. Por ejemplo, **Terceros** y **Producto** son dimensiones obligatorias que deben rellenarse en una factura de compra, pero pueden rellenarse o no en un diario de libro mayor.

Existen **dos dimensiones obligatorias** a nivel de configuración del libro mayor de la organización, que son:

-   La **Cuenta**, ya que cualquier documento/transacción contabilizado en el libro mayor debe contabilizarse en una cuenta contable (o subcuenta en términos de Etendo) de un determinado árbol de cuentas o plan de cuentas.
-   La **Organización**, ya que cualquier documento/transacción contabilizado en el libro mayor debe contabilizarse en el libro mayor de una organización.

![alt text](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/set-up/gl-configuration2.png)

Además, si una organización pertenece a una entidad que centraliza las dimensiones contables, es posible añadir en esta pestaña otras dimensiones como las que se listan a continuación, que incluso pueden configurarse como **Obligatorio** para la organización:

-   Actividad
-   Activo
-   Campaña
-   Ubicación origen
-   Ubicación destino
-   Región de ventas

A continuación se muestra un ejemplo del libro mayor de una organización para el cual se han seleccionado las dimensiones siguientes en esta pestaña porque la organización pertenece a una entidad que no centraliza las dimensiones contables:

-   Dimensiones obligatorias:
    -   Organización
    -   y Cuenta
-   Dimensiones no obligatorias que se establecen como **Obligatorio** aquí:
    -   Terceros, Producto y Proyecto
-   Dimensión no obligatoria:
    -   Región de ventas

La configuración anterior significa que cada vez que se contabiliza en el libro mayor una transacción de cualquier tipo (factura de compra, factura de venta, diario de libro mayor), deben introducirse todas las dimensiones obligatorias anteriores, mientras que existe la opción de introducir información de región de ventas si la hubiera.

!!!note
    Algunas dimensiones aparecen en algunas transacciones y otras no. Eso depende del documento que se esté creando. Por ejemplo, la dimensión **Cuenta** siempre aparece en la pestaña Líneas de un diario de libro mayor; sin embargo, no aparece en la pestaña Líneas de una factura de compra, ya que esos datos se toman automáticamente de las cuentas (subcuentas) configuradas para el producto, para el tercero y para los impuestos, si los hubiera.

### Pestaña Tablas a contabilizar

La pestaña **Tablas a contabilizar** permite al usuario definir qué tablas y, por tanto, qué transacciones se van a contabilizar en el libro mayor y cuáles no.

Las tablas listadas a continuación son tablas **aptas para contabilizar**:

|     |     |
| --- | --- |
| Nombre de la Tabla | Ventana |
| FinancialMgmtAmortization | Amortización |
| Factura | Factura de compra  <br>  <br>Factura de venta |
| Parte | Pedido de compra  <br>  <br>Pedido de venta |
| FIN\_BankStatement | Cuenta financiera - Extracto bancario |
| FIN\_Finacc\_Transaction | Cuenta financiera - Transacciones |
| FIN\_Payment | Cobro  <br>  <br>Pago |
| FIN\_Reconciliation | Cuenta financiera - Conciliación |
| FinancialMgmtGLJournal | Diario del libro mayor |
| MaterialMgmtShipmentInOut | Recepción de mercancía  <br>  <br>Salida de mercancía |
| MaterialMgmtInternalConsumption | Consumo interno |
| MaterialMgmtInventoryCount | Inventario físico |
| ProcurementReceiptInvoiceMatch | Facturas emparejadas |
| ProcurementPOInvoiceMatch | Pedidos de compra emparejados |
| MaterialMgmtInternalMovement | Movimiento de mercancías |
| MaterialMgmtProductionTransaction | Orden de trabajo  <br>  <br>Producción de lista de materiales |
| FinancialMgmtBankStatement | Flujo de pagos antiguo - Extracto bancario  <br>  <br>Establecer Activo = No |
| FinancialMgmtCashJournal | Flujo de pagos antiguo - Diario de caja  <br>  <br>Establecer Activo = No |
| FinancialMgmtDPManagement | Flujo de pagos antiguo - Gestión de deuda-pago  <br>  <br>Establecer Activo = No |
| FinancialMgmtSettlement | Flujo de pagos antiguo - Liquidaciones  <br>  <br>Establecer Activo = No |

Por ejemplo, los registros de la tabla **FinancialMgmtAmortization** son las transacciones de amortización que pueden contabilizarse.

!!! note
    Los registros de las tablas anteriores pueden contabilizarse cuando la casilla de verificación **Activo** de estas tablas está establecida como **Sí**.

!!! info
    Existe un indicador llamado **Desactivar para Background** junto a cada tabla anterior, que permite que una tabla determinada no sea tomada por el proceso de contabilización en segundo plano. En otras palabras, es posible configurar que las transacciones relacionadas con una determinada **Tabla**, por ejemplo la tabla Factura, no sean tomadas por ese proceso y, por tanto, no se contabilicen automáticamente.

#### Subpestaña Documentos

La pestaña **Documentos** permite al usuario definir qué tipos de documento de una tabla permiten contabilización negativa y si utilizan un proceso contable diferente del proceso por defecto basado en una plantilla contable determinada.

![alt text](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/set-up/gl-configuration5.png)

### Pestaña Contabilidad general

La pestaña **Contabilidad general** permite al usuario definir las cuentas que se utilizarán en los asientos de cuadratura y en el proceso de cierre de fin de año.

![alt text](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/set-up/gl-configuration3.png)

Campos a tener en cuenta:

- La cuenta obligatoria **Resumen de contabilidad** se rellena por defecto como parte de la configuración del libro mayor. Esa cuenta forma parte del plan de cuentas de la organización.

    !!!info
        Si no se selecciona un CSV contable o datos de referencia al ejecutar el proceso Crear entidad o el proceso Crear organización, esta cuenta obligatoria debe introducirse manualmente aquí una vez que se haya creado el árbol de cuentas y, por tanto, la correspondiente subcuenta de resumen de contabilidad (o resultado neto).

    - La cuenta Resumen de contabilidad se utiliza en el **proceso de cierre de año**, ya que el asiento de cierre de P&L reinicia todas las cuentas de tipo ingresos y gastos y contabiliza la diferencia en esta cuenta.

    - Contiene un conjunto de cuentas de **Suspense** que deben crearse bajo una rama específica del árbol de cuentas tal y como se explica en la ventana [Árbol de cuentas](#árbol-de-cuentas).

    - Esas cuentas también pueden ser proporcionadas por los archivos contables; de hecho, el CoA genérico proporciona estas cuentas.

- La cuenta **Cuenta de asiento no cuadrado** se muestra si se selecciona la casilla **Utilizar cuenta de asiento no cuadrado**. Esta cuenta se utiliza en aquellos casos en los que un asiento contable no puede cuadrarse mientras se contabiliza. Si no hay una cuenta en este campo, Etendo muestra un error.

- La cuenta **Cuenta de error** se muestra si se selecciona la casilla **Utilizar cuenta de error**. Esta cuenta se utiliza en aquellos casos en los que ocurre una excepción o error que impide que un asiento contable se contabilice. Si no hay una cuenta en este campo, Etendo mostrará un error.

- La cuenta **Reservas**, si existe, recibe automáticamente el saldo de cierre de P&L de un año determinado. Si no hay una cuenta en este campo, no se moverá automáticamente nada desde la cuenta **Resumen de contabilidad** a la cuenta **Reservas**.

- La cuenta **Saldo de moneda** se muestra si se selecciona la casilla **Utilizar saldo de moneda**. Esta cuenta se utiliza en aquellos casos en los que existen diferencias de redondeo de moneda al contabilizar una transacción. Por ejemplo, podría ocurrir que el total de la factura convertido a una moneda determinada no coincida al 100% con la suma de cada línea de factura convertida a la misma moneda.

- La casilla de verificación **Revertir Balance de Cuentas Permanentes** permite al usuario incluir o no un asiento para revertir los saldos de las cuentas de balance durante el proceso de cierre de fin de año.

### Pestaña Valores por defecto

La pestaña **Valores por defecto** permite al usuario mantener o añadir un conjunto de **cuentas por defecto** para utilizar al contabilizar un determinado tipo de transacciones.

Las cuentas **Obligatorio Valor por defecto** se rellenan por defecto como parte de la [configuración del libro mayor](#esquema-contable). Esas cuentas forman parte del plan de cuentas de la organización.

!!!info
    Si no se selecciona un csv contable o datos de referencia al ejecutar los procesos [Crear entidad](../../../../../../developer-guide/etendo-classic/how-to-guides/how-to-run-an-initial-client-setup-process.md) y [Crear organización](../../../general-setup/enterprise-model/initial-organization-setup.md), estas cuentas obligatorias deben introducirse manualmente aquí una vez que se haya creado el [Árbol de cuentas](#árbol-de-cuentas) y, por tanto, las subcuentas correspondientes.

![alt text](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/set-up/gl-configuration4.png)

El botón **Copiar cuentas** permite seleccionar cuentas asignadas por defecto a cada [Grupos de Terceros](../../../master-data-management/business-partner-setup.md#business-partner-category) o [Categoría del producto](../../../master-data-management/product-setup.md#product-category).

!!!info
    Las cuentas asignadas por defecto a cada grupo de terceros, por ejemplo, también pueden asignarse por defecto a cada proveedor o cliente utilizando el botón de acción **Copiar cuentas**, esta vez desde la ventana [Grupos de Terceros](../../../master-data-management/business-partner-setup.md#business-partner-category).

!!!note
    Es posible sobrescribir estos valores por defecto a nivel de grupo de terceros, permitiendo que los pasivos de proveedor y los derechos de cobro de cliente de distintos terceros se contabilicen en cuentas diferentes. Este último cambio de configuración debe realizarse en las pestañas de proveedor y/o cliente de las ventanas de [Terceros](../../../master-data-management/master-data.md#business-partner).

Las cuentas por defecto son:

-   Derechos de cobro de cliente
-   Anticipos de cliente
-   Descuadre
-   Ingresos por descuadre
-   Pasivo del proveedor
-   Anticipo de proveedor
-   Recepciones no facturadas
-   Cuenta de gasto por incobrables
-   Cuenta de ingreso por incobrables
-   Cuenta de provisión para deudas dudosas
-   Cuenta de deudas dudosas
-   Activo del producto
-   Gastos del producto
-   Gastos diferidos del producto
-   Ingresos del producto
-   Ingresos diferidos del producto
-   Coste de ventas del producto
-   Devolución de ingresos del producto
-   Devolución de coste de ventas del producto
-   Variación de precio de factura
-   Diferencias de almacén
-   Revalorización de inventario
-   Trabajo en curso
-   La cuenta por defecto de activo bancario se rellena como:
    -   la cuenta de depósito
    -   la cuenta de retirada
    -   la cuenta de pago cobrado (Cobro)
    -   la cuenta de pago cobrado (Pago)
-   La cuenta por defecto de banco en tránsito se rellena como:
    -   la cuenta de cobro en tránsito
    -   la cuenta de pago en tránsito
-   La cuenta por defecto de gasto bancario se rellena como:
    -   la cuenta de comisiones bancarias
-   Cuenta de ganancia por revalorización bancaria
-   Cuenta de pérdida por revalorización bancaria
-   Impuesto devengado
-   Impuesto reclamado
-   Amortización
-   Amortización acumulada

---

Este trabajo es una obra derivada de [Configuración del libro mayor](https://wiki.openbravo.com/wiki/General_Ledger_Configuration){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.