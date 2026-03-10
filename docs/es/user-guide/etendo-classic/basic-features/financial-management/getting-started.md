---
title: Gestión Financiera - Primeros pasos
tags:
    - Etendo Classic
    - Gestión Financiera
    - Automatización contable
    - Gestión de pagos y cobros
    - Cierre de fin de año
---

![cover-getting-started.png](../../../../assets/getting-started/overview/cover-getting-started.png)
# Gestión Financiera - Primeros pasos
## Visión general

Etendo genera automáticamente una representación contable de todas las transacciones dentro de la empresa que tienen relevancia económica.

La contabilidad es el sistema de seguimiento de los activos, las deudas, los ingresos y los gastos de una empresa.  
En Etendo, la mayoría de los asientos contables se crean automáticamente al contabilizar [documentos](../financial-management/accounting/setup/document-type.md).

- [Albarán (Proveedor)](../procurement-management/transactions.md#goods-receipts) y [Factura (Proveedor)](../procurement-management/transactions.md#purchase-invoice) en el área de negocio [Gestión de Compras](../procurement-management/getting-started.md)
- [Albarán (Cliente)](../sales-management/transactions.md#goods-shipment) y [Factura (Cliente)](../sales-management/transactions.md#sales-invoice) en el área de negocio [Gestión de Ventas](../sales-management/getting-started.md).

Los asientos contables no relacionados directamente con [documentos](../financial-management/accounting/setup/document-type.md) gestionados dentro de un área de aplicación determinada pueden crearse y contabilizarse en [Asientos manuales](../financial-management/accounting/transactions.md#gl-journal). Por ejemplo, un asiento de provisión por depreciación de existencias.

Hay tres formas de contabilizar en Etendo:

- Contabilizar manualmente cada documento usando el botón de proceso *Contabilizar*.  
El botón de proceso *Contabilizar* se puede encontrar en la ventana utilizada para crear un documento determinado. Por ejemplo, una factura de proveedor se crea y, por tanto, podría contabilizarse en la [ventana Factura (Proveedor)](../procurement-management/transactions.md#purchase-invoice). Este botón se muestra para los usuarios contables si el atributo *ShowAcct* es visible para ellos. Esta configuración se habilita mediante una [Preferencias](../general-setup/application/preference.md).

- Contabilizar manualmente todos los documentos/transacciones relacionados con una tabla de base de datos determinada, por ejemplo la tabla *Facturas*, usando el proceso [Proceso contable](../financial-management/accounting/transactions.md#gl-posting-by-db-tables)

- o contabilizar automáticamente transacciones contables de cualquier tipo planificando el *Proceso del servidor contable* en la ventana [Procesamiento de Peticiones](../general-setup/process-scheduling/process-request.md).

Las actividades contables tales como:

- crear y abrir los periodos contables
- introducir y contabilizar transacciones contables
- gestionar las cuentas a pagar y a cobrar, así como la amortización de activos
- revisar y presentar informes financieros y fiscales a las autoridades oficiales
- y cerrar el año contable

se realizan dentro del área de aplicación Gestión Financiera.

Por último, Etendo dispone de un *sistema contable integrado* que combina contabilidad general y contabilidad analítica:

- La *contabilidad general* tiene como objetivo explotar principalmente dimensiones como *Cuenta* (o *Subcuenta* en términos de Etendo)
- La *contabilidad analítica* tiene como objetivo explotar otras dimensiones como *Centro de costos* o *Campaña* para obtener una información financiera ligeramente diferente, pero también rica.

En otras palabras, Etendo permite contabilizar transacciones en el libro mayor, que pueden incluir diferentes dimensiones:

- Esas dimensiones pueden mantenerse de forma centralizada en la [Entidad](../general-setup/client.md) y, por tanto, están disponibles para todas las organizaciones dentro de esa Entidad.  
Además, las Organizaciones de esa Entidad también pueden tener dimensiones adicionales configuradas por separado en su [Esquema contable](../financial-management/accounting/setup/general-ledger-configuration.md).

Estas dimensiones quedan entonces disponibles solo para esa Organización.

- Por otro lado, esas dimensiones no pueden mantenerse de forma centralizada en la [Entidad](../general-setup/client.md), sino mantenerse de forma independiente en el [Esquema contable de la Organización](../financial-management/accounting/setup/general-ledger-configuration.md#dimension-tab).

Esta área de aplicación cubre el flujo de negocio [Cierre de periodo hasta informe financiero](../financial-management/getting-started.md#period-end-close-to-financial-report) y el flujo de negocio [Gestión de cuentas a pagar y a cobrar](../financial-management/getting-started.md#payables-and-receivables-management).
## Gestión de pagos y cobros

<iframe width="560" height="315" src="https://www.youtube.com/embed/DmeLeQkg-cg?si=See53a-gprwcumPw" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

La Gestión de pagos y cobros aborda los cobros de clientes y los pagos a proveedores, así como otros pagos no relacionados con facturas, sino con pedidos (anticipos) o con apuntes de mayor (G/L Items).

![payment-workflow.png](../../../../assets/user-guide/etendo-classic/basic-features/financial-management/payment-workflow.png)

### Configuración

La siguiente configuración debe realizarse antes de ejecutar el proceso:

- [Tipos de documento de pagos y cobros](../financial-management/accounting/setup/document-type.md).
- [Método de pago](../financial-management/receivables-and-payables/transactions.md#payment-method).
- [Cuenta financiera](../financial-management/receivables-and-payables/transactions.md#financial-account).
- [Terceros](../master-data-management/master-data.md#business-partner) para utilizar los Métodos de pago y las Cuentas financieras configurados anteriormente.

!!!note
    No es necesario realizar ninguna configuración adicional para el proceso de negocio de Gestión de pagos y cobros si se va a utilizar la entidad de ejemplo Food & Beverage (F&B) que Etendo incluye por defecto para explorarlo. El conjunto de datos de ejemplo ya contiene los roles, almacenes, terceros, productos y precios preconfigurados.

### Ejecución

En términos generales, el proceso de negocio de *Gestión de pagos y cobros* puede dividirse en los siguientes pasos:

- la creación de los pedidos y facturas a pagar
- la creación de pagos no relacionados con pedidos/facturas
- la revisión del estado de los pagos pendientes
- el cobro de los pagos realizados por los clientes
- el pago de las facturas del proveedor
- el registro de las transacciones de la cuenta financiera
- y la conciliación de las transacciones de la cuenta financiera

#### Creación de los pedidos/facturas a pagar

En los procesos de negocio [Procure to Pay](../procurement-management/getting-started.md#procure-to-pay-business-flow) y [Order to Cash](../procurement-management/getting-started.md#procure-to-pay-business-flow) se ha visto cómo se han generado los pedidos y las facturas.

Cada vez que se contabiliza un Pedido de compra o de venta, o se completa una Factura (Proveedor) o una Factura (Cliente), se crea un Plan de pagos para ese Pedido / Factura.

Un plan de pagos contiene el/los importe/s de pago esperados para el documento y su cumplimiento. Al mismo tiempo, se activa la sección Payment Monitor de la factura, que permite realizar el seguimiento del estado de pago de la factura directamente desde la ventana de la factura.

!!!note
    La sección Payment Monitor permite realizar el seguimiento del estado de pago de las facturas de compra y de venta directamente desde la ventana de la factura. En esta sección es posible saber si una factura está totalmente pagada o no. Si la factura no se ha pagado completamente, entonces Payment Monitor informa al usuario de cuánto se ha recibido, cuánto está pendiente, la fecha de vencimiento del siguiente pago y el importe que se espera recibir en esa fecha. El estado se actualiza automáticamente cuando se produce cualquier acción de pago y mediante un proceso en segundo plano. La fecha en la que se calculó por última vez el estado del pago se muestra en el formulario. El filtrado de la rejilla permite filtrar facturas en función del criterio de totalmente pagada o no.

#### Creación de pagos no relacionados con pedidos/facturas

En el proceso de negocio [Period End Close to Financial Report](../financial-management/getting-started.md#period-end-close-to-financial-report) se ha visto cómo se puede realizar o recibir un pago utilizando un [Asientos manuales](../financial-management/accounting/transactions.md#gl-journal); por tanto, no está relacionado con un pedido/factura, sino con un apunte de mayor (G/L Item).

Un pago de apunte de mayor (G/L Item) creado en Asientos manuales implica:

- la creación de un [Pago realizado](../financial-management/receivables-and-payables/transactions.md#payment-out) si la información del pago se introduce en la línea de *Crédito contabilizado* del asiento manual.

El estado de este pago sería *Pago realizado* o *Pendiente de ejecución* o *Retirado no conciliado*, en función de la [configuración](../financial-management/receivables-and-payables/setup.md#payment-method-configuration) del método de pago utilizado y vinculado a la cuenta financiera de la que se retira el dinero.

- O la creación de un [Cobros](../financial-management/receivables-and-payables/transactions.md#payment-in) si la información del pago se introduce en la línea de *Débito contabilizado* del asiento manual.

El estado de este pago sería *Pago recibido* o *Pendiente de ejecución* o *Depositado no conciliado*, en función de la [configuración](../financial-management/receivables-and-payables/setup.md#payment-in-configuration) del método de pago utilizado y vinculado a la cuenta financiera en la que se va a depositar el dinero.

#### Revisión del estado de los pagos pendientes

De forma periódica, el personal de finanzas revisa el estado de los pagos pendientes de cobro / de pago consultando:

- El [Informe de pagos y cobros](../financial-management/receivables-and-payables/analysis-tools.md#payment-report) y filtrando por el estado Pendiente de pago, lo que significa que todavía no se ha recibido ni realizado ningún pago contra el pedido o la factura.

     La casilla de verificación Vencido permite acotar la búsqueda y mostrar únicamente los pagos vencidos.  
     Tipo de pago muestra Cobros, Pagos o ambos.

- Además, las ventanas de Factura (Cliente) y Factura (Proveedor) en vista de rejilla están disponibles para buscar facturas abiertas estableciendo el campo Pago completado en No.

#### Cobro de los pagos del cliente

Cuando se recibe un pago, el personal de finanzas puede registrarlo de diferentes maneras:

- En la ventana [Cobros](../financial-management/receivables-and-payables/transactions.md#payment-in) seleccionando las Facturas (Cliente) y/o Pedidos contra los que se recibe el pago.

!!!note
    Muchas empresas no desean conceder crédito a determinados clientes y, por tanto, pueden tener una condición de pago que requiera el pago contra un pedido. En la práctica, esto es un anticipo de una factura. Posteriormente, cuando se crea una factura a partir de un pedido que ya tiene un pago recibido asociado, la factura hereda automáticamente el pago recibido contra el pedido.

- Usando el botón Add Payment directamente dentro de la Factura (Cliente) correspondiente. Puede ser el caso cuando el usuario ha recibido un único pago para una factura concreta y prefiere buscar esa factura para asignarle el pago.

- También es posible automatizar la recepción de un pago al completar una Factura (Cliente) mediante la configuración del [Método de pago](../financial-management/receivables-and-payables/transactions.md#payment-method).

Si el cobro no se produce a tiempo:

- Se puede modificar la Fecha prevista del [Plan de pagos](../sales-management/transactions.md#payment-plan_1), evitando que la deuda venza.

- El Importe vencido del Plan de pagos puede:
     dividirse en dos o más importes con vencimiento en una fecha prevista posterior.
    o agruparse en un único importe con vencimiento en una fecha prevista posterior.

- El saldo pendiente de un cliente puede darse de baja total o parcialmente.

#### Pago de las facturas del proveedor

Hay 3 formas de pagar las facturas del proveedor:

- Usando el proceso Propuesta de pago. Este proceso permite el pago automático de un gran número de facturas en función de las fechas de vencimiento de las líneas del Plan de pagos asociado a las Facturas (Proveedor) abiertas. El personal de finanzas puede solicitar una propuesta de todas las facturas a pagar en función de una serie de criterios, revisar esa propuesta y, a continuación, realizar el pago automáticamente.

- En la ventana Payment Out seleccionando las Facturas (Proveedor) y/o Pedidos contra los que se realiza el pago.

!!!note
    Muchas empresas no tienen crédito concedido y, por tanto, puede que se les exija realizar un pago contra un pedido de compra. En la práctica, esto es un anticipo de una factura de compra. Posteriormente, cuando se crea una factura a partir de un pedido que ya tiene un pago realizado asociado, la factura hereda automáticamente el pago realizado contra el pedido.
  
  

- Usando el botón Add Payment directamente dentro de la Factura (Proveedor) correspondiente. Puede ser el caso cuando el usuario necesita realizar un único pago para una factura concreta y prefiere buscar esa factura para asignarle el pago.

- También es posible automatizar la realización de un pago al completar una Factura (Proveedor) mediante la configuración del Método de pago.

#### Registro de las transacciones de la cuenta financiera

El personal de finanzas registra las retiradas y los depósitos como transacciones en la ventana [Cuenta financiera](../financial-management/receivables-and-payables/transactions.md#financial-account) pulsando el botón Add Transaction y seleccionando los pagos recibidos o realizados.
Este paso del proceso también puede automatizarse completamente mediante la configuración del [Método de pago](../financial-management/receivables-and-payables/setup.md#payment-method-configuration), de modo que los pagos se retiren o depositen automáticamente cuando se completen.

#### Conciliación de las transacciones de la cuenta financiera

El personal de finanzas recibe un extracto bancario (en papel o electrónico) y concilia las transacciones de la Cuenta financiera marcadas como Depositado / Retirado no conciliado con las transacciones reales del extracto bancario. Este proceso puede realizarse:

- Manualmente (conciliando una a una las transacciones de la Cuenta financiera de Etendo con las líneas del extracto bancario) utilizando el botón Reconcile de la ventana Cuenta financiera.

- Automáticamente importando primero el extracto y, a continuación, realizando el emparejamiento del extracto mediante un algoritmo de conciliación.

Además, cualquier transacción (cobros y pagos) que figure en el extracto bancario y no esté reflejada en la Cuenta financiera también debe introducirse en Etendo para poder conciliarla.

Por último, el personal de finanzas imprime los informes de conciliación (Detalles de conciliación, Resumen de conciliaciones) que explican cualquier diferencia entre el saldo final mostrado para la Cuenta financiera en Etendo y el saldo final mostrado en el extracto bancario.
## Contabilidad
### Cierre de periodo hasta informe financiero

<iframe width="560" height="315" src="https://www.youtube.com/embed/8WAyKf16HmY?si=lHqZ4KLHM-9siwQ8" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

El flujo de negocio *Cierre de periodo hasta informe financiero* gestiona la apertura y el cierre de periodos.

![periodendclose-tofinancialreport.png](../../../../assets/user-guide/etendo-classic/basic-features/financial-management/periodendclose-tofinancial-report.png)

#### Configuración

Esta sección detalla la configuración contable básica y no tan básica necesaria antes de la ejecución del flujo de negocio *Cierre de periodo hasta informe financiero*.

#### Configuración básica

Hay tres conceptos contables de Etendo que deben explicarse antes de describir la configuración contable básica:

- [Calendario anual y periodos](../financial-management/accounting/setup/fiscal-calendar.md)

Un calendario fiscal en Etendo es el año y los periodos, normalmente meses, en los que las transacciones financieras y los asientos se contabilizan en el libro mayor.

- [Árbol de cuentas](../financial-management/accounting/setup/account-tree.md)

Un árbol de cuentas es la forma en que Etendo captura el *Plan de cuentas* (CoA) de una Organización.

El plan de cuentas es una lista de todas las cuentas utilizadas en el libro mayor de una organización.

Cuentas como las cuentas del balance (activos, pasivos y patrimonio neto) y las cuentas de la cuenta de resultados (ingresos, gastos, ganancias y pérdidas).

!!!Note 
    Es importante remarcar que en Etendo, los informes financieros como el Balance y la Cuenta de resultados se generan en base a la estructura del Plan de cuentas.

- [Esquema contable](../financial-management/accounting/setup/general-ledger-configuration.md)

La configuración del libro mayor recoge las reglas contables a utilizar al contabilizar las transacciones financieras de la organización en el libro mayor. Reglas contables como la *Moneda* y el *Plan de cuentas*, entre otras.

Dicho esto, la configuración contable detallada en esta sección es la requerida para *entidades legales con contabilidad*, incluidas las unidades de negocio, ya que estos tipos de organización son los únicos a los que se les puede asignar:

- un Plan de cuentas
- un Esquema contable
- y un Calendario anual y periodos

Obviamente, estos tipos de organización permiten contabilizar transacciones en el libro mayor.
El resto de tipos de Organización se comportan tal y como se explica en la sección [Crear organización](../general-setup/enterprise-model/initial-organization-setup.md) y en la sección [Organización](../general-setup/enterprise-model/organization.md).

Muy brevemente:

- Las organizaciones *legal sin contabilidad* no requieren contabilidad, por lo tanto no requieren ninguna configuración contable básica ni avanzada.
- Las organizaciones *genéricas*, sin embargo, pueden tener su propio Esquema contable y Plan de cuentas, pero los periodos contables no se pueden abrir y cerrar de forma independiente a su nivel.
Este tipo de organización hereda el Calendario anual y periodos de la organización *legal con contabilidad* a la que pertenecen.
- y, por último, las de tipo *Organización* también pueden tener un esquema contable y un plan de cuentas, pero con el objetivo de ser compartidos entre todas las organizaciones por debajo.
Este tipo de organización no puede tener asignado un calendario fiscal y, además, no se permiten transacciones dentro de ella.

Adicionalmente, algunos países como España o Francia requieren que se utilice un *Plan de cuentas* específico en los libros oficiales, de modo que las autoridades puedan ver la misma lista de cuentas y el mismo nivel de detalle en la cuenta de resultados y en el balance.

Por otro lado, hay países como EE. UU. donde no se requiere un *Plan de cuentas* específico.

Para esos casos, Etendo proporciona un módulo de Plan de cuentas genérico que incluye un plan de cuentas de ejemplo que puede modificarse según sea necesario.
Se recomienda partir de un plan de cuentas de ejemplo como el genérico y evolucionarlo según las necesidades de la organización, en lugar de empezar desde cero.

La configuración de impuestos del país es otro elemento clave de la configuración contable básica.
Puede haber paquetes de localización que incluyan la configuración de los impuestos del país, mientras que puede haber otros que no la incluyan.
El módulo de CoA genérico no incluye ninguna configuración de impuestos.

#### Ejecución 

En general, el flujo de negocio Cierre de periodo hasta informe financiero puede dividirse en los siguientes pasos una vez que se ha abierto el periodo contable:

- la apertura de la contabilidad
- la revisión de las transacciones contables
- la creación de transacciones contables y pagos de elementos de libro mayor
- la impresión del Balance sumas y saldos
- los ajustes necesarios antes del cálculo del resultado
- los ajustes necesarios antes del cierre del año contable
- la impresión de la cuenta de resultados y el balance preliminares
- el cierre del año contable
- y la impresión de la cuenta de resultados y el balance finales

##### Apertura de la contabilidad

Este primer paso implica inicializar el saldo de las cuentas del libro mayor y de las cuentas financieras o bancos. La forma de hacerlo en Etendo es:

- El saldo de las cuentas del libro mayor puede inicializarse utilizando un [Asientos manuales](../financial-management/accounting/transactions.md#gl-journal) configurado como *Apertura*, por lo que ese asiento se establece como el *Asiento de apertura del libro mayor*.
Se puede crear una línea de asiento para cada cuenta y su saldo de apertura; una vez hecho, el asiento manual validará que el Débito total de todas las entradas sea igual al Crédito total.
- El saldo de las cuentas financieras puede inicializarse en la ventana [Cuenta financiera](../financial-management/receivables-and-payables/transactions.md#financial-account), en el campo *Saldo Inicial*; por lo tanto, las cuentas financieras o bancos correspondientes deben crearse previamente.

##### Revisión de las transacciones contables

Como ya se ha mencionado, en Etendo la mayoría de los asientos contables se crean automáticamente al contabilizar documentos como una factura de proveedor o una factura de cliente.
Por ejemplo, la contabilidad de una factura de proveedor tomará:

- la configuración de la cuenta de gasto para el producto que se está comprando en la pestaña [Contabilidad](../master-data-management/master-data.md#accounting) de la ventana *Producto*
- la configuración de la cuenta de pasivo del proveedor para el proveedor en la pestaña [Contabilidad proveedor](../master-data-management/master-data.md#vendor-accounting) de la ventana *Terceros*
- y la configuración de la cuenta de impuesto soportado en la pestaña [Contabilidad](../financial-management/accounting/setup/tax-rate.md#accounting) de la ventana *Rango impuesto*.

Etendo permite revisar y corregir, si es necesario, los asientos contables de documentos transaccionales como las facturas.
Del mismo modo, Etendo permite descontabilizar documentos transaccionales contabilizados incorrectamente, uno a uno, para corregirlos y contabilizarlos correctamente de nuevo.

Adicionalmente, el informe [Detalles de transacciones contables](../financial-management/accounting/analysis-tools.md#accounting-transaction-details) muestra todas las transacciones contabilizadas en el libro mayor con todos los detalles y el informe [Transacciones no contabilizadas](../financial-management/accounting/transactions.md#not-posted-transaction-report) muestra las transacciones que deben contabilizarse pero que aún no se han contabilizado.

Por último, Etendo permite corregir de forma masiva errores contables, si los hubiera; por ejemplo, una cuenta de pasivo de proveedor asignada incorrectamente a un proveedor o a un conjunto de proveedores.
La forma de hacerlo es:

- ejecutar el proceso [Reinicializar cuentas](../financial-management/accounting/transactions.md#reset-accounting) para la tabla afectada, por ejemplo la tabla *C_Invoice* (tabla de Factura (Proveedor) y Factura (Cliente)).
- corregir la configuración contable
- volver a contabilizar las transacciones utilizando la funcionalidad [Proceso contable](../financial-management/accounting/transactions.md#gl-posting-by-db-tables).
Esta funcionalidad realiza una contabilización masiva de toda la contabilidad o solo de la contabilidad de una tabla, por ejemplo la tabla *C_Invoice* (tabla de Factura (Proveedor) y Factura (Cliente)).

##### Creación de transacciones contables y pagos de elementos de libro mayor

Como ya se ha mencionado, los asientos contables no relacionados con documentos gestionados dentro de un área de aplicación determinada pueden crearse y contabilizarse en el libro mayor utilizando un [Asientos manuales](../financial-management/accounting/transactions.md#gl-journal).
Un asiento manual también puede utilizarse para realizar y/o recibir pagos no relacionados con pedidos/facturas, sino con elementos de libro mayor.
Los pagos de elementos de libro mayor también se gestionan dentro del área de [Gestión de pagos y cobros](../financial-management/getting-started.md#payables-and-receivables-management).

##### Impresión del Balance sumas y saldos para comprobar que Débito=Crédito

El [Balance sumas y saldos](../financial-management/accounting/analysis-tools.md#trial-balance) es una lista que indica los saldos de cada cuenta del libro mayor en un momento determinado.

El propósito del balance de sumas y saldos es comprobar que los débitos son iguales a los créditos. Si los débitos no son iguales a los créditos, eso significa que se ha contabilizado un asiento erróneo.

Etendo no permite contabilizar asientos que no cuadren. Un asiento manual solo puede contabilizarse si el Débito es igual al Crédito; sin embargo, podría haber situaciones en las que, al contabilizar una factura, las diferencias de redondeo hagan que el débito no sea exactamente igual al crédito. 

En estas situaciones, la diferencia se contabiliza en una cuenta transitoria específica. Las cuentas [Transitoria](../financial-management/accounting/setup/general-ledger-configuration.md#general-accounts) se configuran en el Esquema contable.

##### Ajustes necesarios antes del cálculo del resultado

La cuenta de resultados de una organización muestra el rendimiento financiero de la organización durante un periodo de tiempo (normalmente un año) como la diferencia entre:

- los ingresos de la organización
- y los gastos de la organización

Para obtener un cálculo del resultado preciso, hay algunos ajustes que deben realizarse primero:

- la organización necesita *revisar los ingresos y los gastos* para asegurarse de que los contabilizados dentro del periodo que se va a cerrar son los que deben contabilizarse, independientemente de si están pagados o no. Este tipo de ajuste no es necesario si la organización sigue el método contable de devengo, que es el método contable de Etendo.
Bajo el método de devengo, los ingresos se registran tan pronto como se prestan los servicios o se entregan los bienes y, por lo tanto, se facturan, independientemente de cuándo se reciba el efectivo.
Del mismo modo, los gastos se reconocen tan pronto como la empresa recibe bienes o servicios y, por lo tanto, se factura, independientemente de cuándo los pague realmente.

- la organización necesita calcular el *Coste de los bienes vendidos* (CoGS). El CoGS es el importe que la empresa pagó por los bienes que vendió a lo largo del periodo. Este cálculo depende del método de control de inventario. Hay dos métodos principales: el método perpetuo y el método periódico:

   el método perpetuo lo utiliza cualquier empresa que mantiene información en tiempo real sobre los niveles de inventario y que realiza el seguimiento del inventario artículo por artículo.
   Este método permite un registro muy preciso del Coste de los bienes vendidos, que es la suma del coste de todos los artículos vendidos durante el periodo.

   El método periódico lo utiliza cualquier empresa que realiza recuentos de inventario a intervalos regulares.
   Al utilizar este método, el Coste de los bienes vendidos se calcula utilizando la siguiente ecuación:
   (Inventario inicial + Compras de inventario - Inventario final = Coste de los bienes vendidos)
   Además, si una empresa está gestionando costes de inventario unitarios cambiantes, debe utilizarse un método específico de cálculo del CoGS, que podría ser FIFO, LIFO o coste medio.

Por último, una cuenta de resultados puede separar los *Gastos operativos* como salarios y alquiler del *Gastos no operativos* como un litigio.

Los gastos operativos son los gastos relacionados con la operación normal del negocio y es probable que también se incurran en periodos futuros.

Esto permite el cálculo del *Resultado operativo* como la diferencia entre el *Beneficio bruto* y el *Total de gastos operativos*.

##### Ajustes necesarios antes del cierre del año contable

Otros ajustes necesarios pueden ser:

- Los importes a largo plazo deben reclasificarse a importes a corto plazo. El importe a largo plazo reclasificado a corto plazo es el importe con vencimiento en el próximo año.
Este proceso suele hacerse, por ejemplo, para deudas a largo plazo. En Etendo, este tipo de transacción puede crearse manualmente utilizando un [Asientos manuales](../financial-management/accounting/transactions.md#gl-journal).
- Los impuestos como el IVA deben liquidarse periódicamente.
Es importante remarcar que el saldo de las cuentas de IVA debe ser igual a 0 en el último periodo del año, ya sea porque la organización debe pagar a las autoridades fiscales o al contrario.
- La amortización de activos debe contabilizarse correctamente dentro del periodo que se está cerrando, ya que este ajuste afectará a:

   la cuenta de resultados, ya que la amortización es un gasto
   y al lado del débito del balance, ya que los activos se reducirán por el importe de la amortización del periodo.

##### Impresión de la cuenta de resultados y el balance preliminares

Una vez configurado, Etendo permite obtener e imprimir la cuenta de resultados y el balance siempre que sea necesario, ya que la estructura de estos informes se basa en el árbol del plan de cuentas.

Es muy útil imprimir estos informes financieros antes del cierre del año, ya que permite hacerse una idea de si faltan ajustes por realizar antes del cierre del año o no.

Durante el ciclo contable hay otros informes que también pueden imprimirse:

- el [Libro mayor](../financial-management/accounting/analysis-tools.md#general-ledger-report) lista todas las entradas de débito y todas las entradas de crédito de cada cuenta en T dentro de un periodo de tiempo determinado
- el [Diario asientos](../financial-management/accounting/analysis-tools.md#journal-entries-report) lista en orden cronológico cada asiento contabilizado en el libro mayor.

##### El cierre del año fiscal

Etendo permite realizar las comprobaciones detalladas a continuación antes del cierre del año fiscal:

- Ejecutar el informe [Transacción no contabilizada](../financial-management/accounting/transactions.md#not-posted-transaction-report) para verificar que no hay transacciones y/o documentos en estado *Completado* que aún no se hayan contabilizado.
- Comprobar que no hay documentos que sigan teniendo estado *Borrador*, especialmente aquellos que requieren ser [contabilizados](../financial-management/accounting/setup/general-ledger-configuration.md#active-tables-tab).
- Desprogramar el [Proceso del servidor contable](../general-setup/process-scheduling/process-request.md), de modo que se pueda asegurar un escenario estable.
- Comprobar el saldo actual de la/s [Cuenta/s financiera/s](../financial-management/receivables-and-payables/transactions.md#financial-account) en Etendo y compararlo con la información proporcionada por los bancos. Es posible ajustar el saldo de la cuenta financiera utilizando elementos de libro mayor o [cómo transferir fondos entre cuentas financieras](../../how-to-guides/how-to-transfer-funds-between-financial-accounts.md).

Antes de ejecutar el proceso de cierre de año, los periodos contables pueden [cerrarse](../financial-management/accounting/setup/openclose-period-control.md) para no permitir más contabilizaciones dentro de esos periodos, excepto el *periodo 13*.
El *periodo 13* es un *periodo de ajuste* que puede utilizarse para contabilizar los ajustes necesarios en el libro mayor mediante [Asientos manuales](../financial-management/accounting/transactions.md#gl-journal) antes de cerrar el año.

El proceso *Crear asiento de regularización* puede ejecutarse desde la ventana [Cierre de año](../financial-management/accounting/transactions.md#end-year-close).

El proceso de cierre de fin de año puede ejecutarse para tipos de organización *legal con contabilidad*, ya que ese tipo de organización tiene configurados un *Calendario anual y periodos* y un *Esquema contable*.

Hay una casilla de verificación en la pestaña [Contabilidad general](../financial-management/accounting/setup/general-ledger-configuration.md#general-accounts) de la ventana *Esquema contable* que muestra cómo va a ser el resultado del cierre de fin de año para el libro mayor de la organización.
Esa casilla se llama *Revertir Balance de Cuentas Permanentes*. 

- Si está marcada, el proceso de cierre de año incluye un asiento para revertir las cuentas de balance, además del asiento de cierre de P&L.
- Si no está marcada, el proceso de cierre de año incluye solo el asiento de cierre de P&L.

Etendo utiliza el periodo de ajuste (p. ej., 31 de diciembre) para contabilizar las transacciones de cierre, si las hubiera, y la primera fecha del siguiente periodo (p. ej., 1 de enero) para contabilizar las transacciones de apertura, si las hubiera.

!!!info
    Para más información, visite la ventana [Cierre de año](../financial-management/accounting/transactions.md#end-year-close).

##### Impresión de la cuenta de resultados y el balance finales

Una vez que se ha cerrado un año, cada informe financiero contiene las transacciones de cierre y apertura correspondientes:

- el [Balance](../financial-management/accounting/analysis-tools.md#balance-sheet-and-pl-structure) mostrará la situación financiera de la organización a fecha de fin del periodo contable cerrado.
Etendo permite obtener un balance de dos columnas:
          Una columna muestra los saldos a fecha de fin del periodo contable más reciente
          y la otra columna muestra los saldos a fecha de fin del periodo anterior.

Este balance permite ver cómo ha cambiado la posición financiera de la organización a lo largo del tiempo.

- la [Cuenta de resultados](../financial-management/accounting/analysis-tools.md#balance-sheet-and-pl-structure) mostrará el rendimiento de la organización durante el año cerrado

Y además: 

- el [Diario del libro mayor](../financial-management/accounting/analysis-tools.md#general-ledger-report) permite mostrar, para un periodo contable determinado, las siguientes entradas contabilizadas por el proceso Crear asiento de regularización:
    el asiento de saldo de apertura
    el asiento de saldo de cierre
    y el asiento de cierre de P&L
## Activos 
### Adquisición de activos hasta su baja

<iframe width="560" height="315" src="https://www.youtube.com/embed/_PhqumhZr8U?si=KKUCdccNMHP6f0SV" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Gestiona el ciclo de vida global de los activos desde la adquisición hasta su baja, incluyendo la amortización y otras depreciaciones.

![asset-acq-disp-business-process.png](../../../../assets/user-guide/etendo-classic/basic-features/financial-management/asset-acq-disp-business-process.png)
## Relación con otras áreas

Gestión Financiera tiene conexión con otras áreas de la aplicación, ya que existen documentos o transacciones en esas áreas que pueden contabilizarse y, por tanto, formar parte de un diario del libro mayor para finalmente gestionarse dentro del área de aplicación de Gestión Financiera.

- [Gestión de Compras](../procurement-management/getting-started.md) ya que allí se contabilizan las Factura (Proveedor) y también pueden contabilizarse los Albarán (Cliente) así como los pagos a proveedores o Pagos emitidos.
- [Gestión de Ventas](../sales-management/getting-started.md) ya que allí se contabilizan las Factura (Cliente) y también puede contabilizarse el Albarán (Cliente) así como los cobros de clientes o Cobros.
- [Gestión de Almacén](../warehouse-management/getting-started.md) ya que allí se contabiliza el inventario físico.
- Gestión de Producción, ya que para el procesamiento de la orden de trabajo se consumen materias primas y se contabilizan a precio de coste, así como los productos fabricados.

---

Este trabajo es una obra derivada de [Gestión Financiera](http://wiki.openbravo.com/wiki/Financial_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.