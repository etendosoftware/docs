---
tags:
  - Etendo Classic
  - Financial Management
  - Financial Account
  - Bank Reconciliation
  - Receivables and Payables
---

# Cuenta Financiera

:material-menu: `Aplicación` > `Gestión Financiera` > `Cobros y Pagos` > `Transacciones` > `Cuenta Financiera`

## Visión General

Una Cuenta Financiera representa una cuenta en una institución financiera, como una cuenta bancaria, una entidad emisora de tarjetas de crédito, un servicio de pago electrónico, así como una caja o caja chica.

Etendo permite al usuario crear tantas Cuentas Financieras como requiera la organización en la ventana Cuenta Financiera, la cual se utiliza por tanto para registrar transacciones monetarias como pagos de facturas, comisiones bancarias, cargos de tarjeta de crédito, etc.

Las obligaciones de pago y los importes pendientes de clientes se crean en las ventanas de Factura de Compra y de Venta. Sin embargo, los cobros de clientes y los pagos a proveedores por estas facturas se registran normalmente en la ventana Cuenta Financiera o en las ventanas Cobro y Pago.

!!! warning
    Es muy importante definir correctamente cada parámetro de cada Cuenta Financiera. Durante el proceso de configuración de la Cuenta Financiera, necesitará información como: los datos de la cuenta bancaria, los métodos de pago permitidos, la/s moneda/s de la cuenta bancaria, la información contable, etc.

## Cuenta

La ventana Cuenta Financiera contiene información esencial, como el número de cuenta bancaria, y permite al usuario realizar un conjunto de procesos, como agregar transacciones de depósito o retiro a la cuenta financiera o importar y conciliar un archivo de extracto bancario.

![Cuenta](../../../../../assets/drive/1G1flRQCPZ_77ab9ntPfNwRfU9TwaaJDf.png)

La **información esencial de la cuenta financiera** que debe completarse en la sección superior de la ventana Cuenta Financiera es:

- El **Nombre** y una **Descripción** de la cuenta.
- La **Moneda** de la cuenta.
- El **Tipo** de cuenta: Existen dos tipos de cuenta: **Banco** y **Caja**.  
  Dependiendo del tipo seleccionado, cambia la información requerida. No es necesario completar la información de la cuenta bancaria si el tipo de cuenta seleccionado es "Caja".  
  Es posible definir tipos de cuenta adicionales ampliando la **Lista** _Tipo de Cuenta Financiera_.
- Si esta es la cuenta **Predeterminada** que se utilizará en las transacciones o no. Cuando se crean facturas, pedidos y otros documentos que incluyen una Cuenta Financiera, esta será la que se muestre por defecto.
- El **Tercero** asociado a esta cuenta bancaria. Por ejemplo, la Institución Financiera que mantiene la cuenta. Esta información se utiliza con fines contables. La dirección de ubicación relacionada con el tercero es solo información visual que se carga cuando se selecciona el tercero.
- El **Saldo Inicial:** En la mayoría de los casos, la empresa ya está en funcionamiento en el momento en que se implementa Etendo. Este campo permite al usuario inicializar el saldo inicial de cada Cuenta Financiera proporcionando el saldo real de la cuenta de caja/banco tal como estaba en la fecha de la última conciliación. Posteriormente, este valor del campo se utiliza como **Saldo Inicial** en la primera conciliación de esta Cuenta Financiera en Etendo. Este campo solo es editable al crear la Cuenta Financiera.
- El **Saldo Actual:** es el saldo de la Cuenta Financiera según los registros de Etendo. Se calcula como la suma del **Saldo Inicial** y cada transacción de la Cuenta Financiera. Este campo se encuentra en la Barra de Estado.
- El **Algoritmo de Conciliación** que se utilizará durante el proceso de conciliación.
  - Si **no se selecciona ningún algoritmo de conciliación** en ese campo, no es posible importar y luego conciliar un archivo de extracto bancario, sino solo Conciliar las transacciones de la cuenta.
  - Si se selecciona un algoritmo de conciliación como el algoritmo **Estándar**, este permite al usuario utilizar el proceso Importar Extracto. Este proceso permite al usuario importar datos desde un archivo a la pestaña Extractos Bancarios Importados y luego usar el proceso Conciliar Extracto para conciliar las transacciones de la cuenta con las líneas del extracto bancario importado. Este algoritmo de conciliación admite el reconocimiento de "transacciones de conceptos contables".
  - Existe otro algoritmo distribuido como módulo denominado Algoritmo de Conciliación Avanzado. Este módulo permite que las líneas del Extracto Bancario Importado se concilien no solo con las transacciones de la cuenta financiera existentes, sino también con pagos, facturas o pedidos. Si no se encuentra ningún documento de transacción de ese tipo, registra un pago de crédito para los Terceros para su uso posterior. Este algoritmo de conciliación admite la creación automática de pagos y transacciones de cuentas financieras (depósitos y retiros), incluida la creación de "transacciones de conceptos contables".
- El campo **Transferencia de Fondos Habilitada** se utiliza para habilitar/mostrar el botón del proceso de transferencia de fondos. Por defecto, cada cuenta financiera está habilitada.

La siguiente sección **Cuenta Bancaria** es visible solo para las cuentas de tipo **Banco** y se utiliza para especificar el número de cuenta bancaria. Esta sección incluye información como:

- El **Número de Cuenta Genérico**: aquí se puede introducir un número de cuenta genérico para identificar la cuenta bancaria. Este campo debe establecerse de forma obligatoria en caso de que se seleccione _Usar Número de Cuenta Genérico_ o _Usar SWIFT + Número de Cuenta Genérico_ en el campo "**Formato de Cuenta Bancaria**".
- El **IBAN**: El Número Internacional de Cuenta Bancaria (IBAN) es un estándar internacional para la numeración de cuentas bancarias.  
  El IBAN consiste en un código de país ISO 3166-1 de dos letras, seguido de dos dígitos de control y hasta treinta caracteres alfanuméricos para el número de cuenta bancaria nacional, denominado BBAN (Número Básico de Cuenta Bancaria). Este campo debe establecerse de forma obligatoria en caso de que se seleccione la opción _Usar IBAN_ en el campo "**Formato de Cuenta Bancaria**". El código IBAN se validará automáticamente al insertar/actualizar el registro, teniendo en cuenta las reglas del banco del país definido.
- El **Código SWIFT**: Corresponde al identificador de código bancario internacional ISO 9362. Debe establecerse de forma obligatoria en caso de que se seleccione la opción _Usar SWIFT + Número de Cuenta Genérico_ en el campo "**Formato de Cuenta Bancaria**".
- **País**: puede seleccionar un país de la lista para especificar si la cuenta bancaria es una cuenta bancaria nacional o extranjera.
- **Formato de Cuenta Bancaria**: Lista que contiene todos los valores posibles para generar el Número de Cuenta Mostrado, que posteriormente será utilizado por otros informes o procesos para obtener el identificador de la cuenta. Los valores posibles son:
  - _Usar Número de Cuenta Genérico_
  - _Usar IBAN_
  - o _Usar SWIFT + Número de Cuenta Genérico_

!!! info
    Tenga en cuenta que otros módulos que amplíen el Formato de Cuenta Bancaria admitido pueden agregar otras opciones.

La sección **Más información** puede incluir información como:

- El campo **Tipo de Límite de Cancelación**, que permite al usuario definir diferentes tipos de límites de cancelación para una cuenta financiera.   
  Este campo se muestra cuando el valor de la propiedad "Límite de cancelación" está establecido en "Y" en la ventana Preferencia.
  - La única opción disponible actualmente es "Importe"
- Y el **Valor del Límite de Cancelación** para el límite de cancelación en un pago. Cuando el tipo seleccionado es Importe, el valor contiene el importe en la moneda de la cuenta financiera.  
  Este campo se muestra cuando el valor de la propiedad "Límite de cancelación" está establecido en "Y" en la ventana Preferencia.

    Tomemos por ejemplo la configuración de un importe de "Límite de Cancelación" de 1,00 $ para una cuenta financiera determinada.

    Al registrar el pago de un cliente en la ventana Agregar Pago, el sistema no permitirá al usuario cancelar un importe superior al límite de cancelación definido.

    Lo mismo se aplica a los pagos a proveedores creados mediante la ventana Agregar Pago o la funcionalidad Propuesta de Pago.

### Botones

#### Agregar Múltiples Pagos

El botón de proceso "Agregar Múltiples Pagos" permite al usuario crear y procesar transacciones de la cuenta financiera seleccionando varios pagos al mismo tiempo.

Los pagos mostrados para selección son aquellos con estado de pago igual a "Pago Realizado" o "Pago Recibido"; por lo tanto, los pagos con estado de pago "Pendiente de Ejecución", por ejemplo, no se mostrarán para selección.

Por defecto, los pagos mostrados son los definidos originalmente para esta cuenta financiera. Sin embargo, el usuario puede eliminar este filtro para mostrar y seleccionar pagos de otras cuentas financieras.

![Agregar múltiples pagos](../../../../../assets/drive/1WDuGJ8r3aCcAzVGC1bFj1pc87CkaEJxG.png)

Las únicas acciones a realizar son introducir una "Fecha de Transacción" y seleccionar tantos pagos como se requieran a la vez.

Los pagos seleccionados se listan como:

- transacciones "**Depósito de Tercero**", en el caso de "Pagos Recibidos"
- o transacciones "**Retiro de Tercero**", en el caso de "Pagos Realizados"

en la pestaña "Transacción" de la Cuenta Financiera.

Todas estas nuevas transacciones se crean ya "procesadas", por lo que pueden ser "reactivadas" si es necesario o finalmente "contabilizadas" en el libro mayor si corresponde.

#### Conciliar

El botón de proceso de cabecera "**Conciliar**" se muestra para las cuentas financieras que no tienen asignado un algoritmo de conciliación.

Ese botón abre la ventana "Conciliación".

La ventana de conciliación tiene tres partes principales:

- la sección superior, que incluye información general como la cuenta financiera que se está conciliando, la fecha del extracto a conciliar, el saldo inicial (o "Saldo Inicial" de la cuenta financiera) y el saldo final como resultado de la conciliación. El saldo final es el último saldo de conciliación de la cuenta financiera.
- la sección central, que incluye una lista de las transacciones pendientes de conciliación, marcadas por tanto como "Saldada" = "No" en la pestaña de transacciones de la cuenta financiera.
- y la sección inferior, que incluye información general sobre saldos, así como tres botones de proceso "Guardar", "Conciliar" y "Cancelar".

El "Saldo Inicial" + los importes "Recibidos" - los importes "Pagados" deben ser iguales al "Saldo Final".

Se puede introducir el saldo final o lo que indica el extracto y luego seleccionar las transacciones pagadas/recibidas, o al contrario.

!!! info
    Es posible crear una transacción de "concepto contable" en caso de que existan pequeñas diferencias entre lo que indican los extractos y las transacciones registradas pendientes de conciliación.

![Ventana de conciliación](../../../../../assets/drive/1N1L6_XETrXBZnbUB3YwVD_RJvVmd0G6V.png)

El botón de proceso "**Guardar**" guarda un "**Borrador**" de la conciliación en la pestaña Conciliaciones de la cuenta financiera y marca la/s transacción/es seleccionada/s como "Saldada" también en la pestaña de transacciones de la cuenta financiera.

Siempre es posible reabrir una conciliación guardada y modificar lo que sea necesario.

!!! info
    Tenga en cuenta que solo puede haber una conciliación en estado borrador en una cuenta financiera.

El botón de proceso "**Conciliar**" concilia las transacciones marcadas como saldadas, por lo que la conciliación se procesa y su estado cambia a "Completada".

Finalmente, el botón de proceso "**Cancelar**" simplemente cierra la ventana de conciliación y elimina el saldo final introducido, si lo hubiera.

#### Importar Extracto

El botón de proceso de cabecera **Importar Extracto** se muestra para las cuentas financieras que tienen asignado un algoritmo de conciliación. Este botón de proceso permite al usuario importar un extracto bancario que, por tanto, se guarda en la pestaña Extractos Bancarios Importados de la cuenta financiera y en la subpestaña Líneas del Extracto Bancario.

!!! info
    Etendo distribuye actualmente el algoritmo de conciliación **Estándar**. El comportamiento del algoritmo de conciliación estándar se explica en la siguiente sección "Conciliar Extracto".

!!! info
    Etendo permite al usuario importar un extracto bancario si previamente se ha instalado un módulo de Formato de Archivo Bancario de Importación.


Etendo distribuye actualmente los siguientes módulos de importación de archivos bancarios:

- Formato de Extracto Bancario OFX
- Importador Genérico de Extracto Bancario CSV
- Importador CSV WePay
- y el español Cuaderno 43

Dependiendo del módulo instalado para este fin, será posible importar archivos de extracto bancario en formato OFX o CSV, entre otros.

El botón de proceso "Importar Extracto" abre la ventana "Importar Archivo Bancario".

![Importar Extracto](../../../../../assets/drive/127lBLYWqTXTFWRW2bCr3BJ3M3RasGZ5W.png)


Esta ventana permite:

- seleccionar un **archivo de extracto bancario**
- y seleccionar el **formato de archivo** del archivo de extracto bancario seleccionado para importar.

#### Conciliar Extracto

Una vez importado un archivo de extracto bancario, el botón "Conciliar Extracto" abre una nueva ventana donde se muestran las líneas del extracto bancario importado y las transacciones financieras existentes. Por defecto, hay un filtro implícito que oculta las líneas del extracto bancario que ya están conciliadas.

![Conciliar Extracto](../../../../../assets/drive/1TBIUGHObHsHlBtGTmHZE_HHg3mK8PtuK.png)

Antes de abrir la ventana, se muestra un pop-up que pregunta si el algoritmo debe ejecutarse contra las líneas del extracto bancario no conciliadas o no. En caso afirmativo, el algoritmo intentará encontrar una coincidencia para todas las líneas del extracto bancario no conciliadas. En caso negativo, se abrirá la ventana de conciliación y el usuario deberá realizar las conciliaciones manualmente.

![Ejemplo 2](../../../../../assets/drive/1GimSn37f-WQGok4aqb0NWFwDg4Xri2ZM.png)

Esta ventana tiene dos grupos de columnas divididos por la columna Conciliar.

- **Líneas del Extracto Bancario Importado** en el lado izquierdo. Esta sección enumera los depósitos del extracto bancario y los pagos:
  - **Fecha:** es la fecha del movimiento realizado en la cuenta bancaria.
  - **Tercero:** es el tercero reportado en la línea del extracto bancario.
  - **Nº de Referencia:** es la referencia del extracto bancario, si la hubiera.
  - **Importe:** es el importe reportado en la línea del extracto bancario, restando el Importe de Salida del Importe de Entrada.
- **Transacción en Etendo** en el lado derecho. Esta sección enumera las transacciones de la cuenta financiera que coinciden con las líneas del extracto bancario:
  - **Conciliar:** proporciona 3 botones para operar con las líneas del extracto bancario (explicados más adelante). Además, la columna puede usarse para filtrar por el estado de conciliación (Sí para mostrar líneas saldadas, No para mostrar líneas no saldadas).
  - **Afinidad:** cuando la conciliación se realiza automáticamente mediante el Algoritmo de Conciliación, este campo muestra el nivel de afinidad de la coincidencia. Si el usuario asocia manualmente una transacción, este campo está vacío. La afinidad es mayor cuando los criterios de coincidencia son los mismos tanto en la transacción de la cuenta financiera como en la línea del extracto bancario.
  - **Tipo de Conciliación:** el tipo de conciliación.
  - **Fecha de Transacción:** es la fecha en que se creó la transacción en la cuenta financiera.
  - **Tercero de Transacción:** es el tercero de la transacción.
  - **Importe de Transacción:** es el importe de la transacción, restando el Importe de Retiro del Importe de Depósito.

Como ya se mencionó, el algoritmo de conciliación disponible es el "algoritmo de conciliación estándar".

El algoritmo de conciliación estándar puede configurarse para conciliar por diferentes conjuntos de criterios:

- **Conciliar por Nombre de Tercero:** Esta opción refuerza la conciliación si el nombre del tercero en la línea del extracto bancario y el tercero de la transacción coinciden.
- **Conciliar por Fecha de Transacción:** Esta opción refuerza la conciliación si la fecha de transacción de la línea del extracto bancario y la fecha de la transacción coinciden.
- **Conciliar por Referencia:** Esta opción refuerza la conciliación si la referencia de la línea del extracto bancario y la referencia de la transacción coinciden.

Todos los criterios anteriores pueden seleccionarse o solo algunos de ellos.

!!! info
    Las transacciones no conciliadas pueden conciliarse manualmente.

Tomemos como ejemplo la situación inicial que se muestra a continuación, donde hay tres líneas de extracto bancario que no coinciden:

![Ejemplo 3](../../../../../assets/drive/1K31lmmG2WiS1k6bunMTXgghMHLw9Chw3.png)

- El icono de "lupa" ayuda a buscar transacciones para conciliar, ya que abre una nueva ventana que muestra las transacciones de la cuenta financiera registradas el mismo día que la línea del extracto bancario o antes. Se pueden seleccionar varias transacciones a la vez para conciliar con una única línea del extracto bancario. En ese caso, el sistema divide automáticamente la línea original del extracto bancario tantas veces como transacciones se seleccionen.

![Ejemplo 4](../../../../../assets/drive/1OL1GtOSH905zxVc9UjliNCM3UztnFK84.png)

Volviendo a nuestro ejemplo, no hay ninguna transacción que coincida con la segunda transacción del archivo de extracto bancario (la que tiene un importe igual a 1.500,00). Si hubiera una coincidencia, podría seleccionarse también mediante el icono de "lupa".

- El icono "+" ayuda a agregar transacciones a la cuenta financiera (e incluso crear un pago para depositar o retirar de la cuenta financiera), ya que abre la ventana "Agregar Transacción".

![Ejemplo 5](../../../../../assets/drive/1MhRo1pZgSopD5v9S3avUHPR5HUWW_XdZ.png)

La imagen anterior muestra que había una transacción "Recibido" pendiente de crear en la cuenta financiera. Una vez creada, queda conciliada.

Volviendo a nuestro ejemplo, la situación actual se muestra en la imagen siguiente:

![Ejemplo 6](../../../../../assets/drive/1YjafVYkcIa5yMvLoNCt5jBMZbdyqUsFo.png)

Solo queda una transacción pendiente de conciliar. El icono de "lupa" ayuda de nuevo a buscar transacciones para conciliar.

Si se selecciona una transacción que casi coincide, Etendo muestra un mensaje que informa de que las transacciones no coinciden totalmente, por lo que se puede realizar una conciliación parcial. El usuario puede establecer la Preferencia 'Conciliar Extracto: ocultar pop-up de confirmación de conciliación parcial' en Y para la ventana Cuenta Financiera, con el fin de ocultar este mensaje de confirmación en el futuro.

!!! info
    Esta última opción requerirá cerrar sesión e iniciar sesión nuevamente.

![Ejemplo 7](../../../../../assets/drive/1U0DAE2Ad9SLeZF4HRRf6o_PkA8FPIk-w.png)

Esta acción concilia la línea del extracto bancario y crea una nueva línea pendiente de conciliar por la diferencia.

- El icono "desconciliar" desconcilia la transacción vinculada al registro individual. El usuario también puede seleccionar múltiples registros y desconciliarlos todos en lote usando el botón **Desconciliar Seleccionados**.

El usuario puede forzar tanto la reactivación como el procesamiento de conciliaciones en caso de que se haya cometido algún error, para permitir reactivar conciliaciones antiguas y poder corregir esos datos.

Este no debe ser el procedimiento estándar, ya que debe realizarse una revisión de los datos antes de validar/procesar una conciliación. En cualquier caso, los errores ocurren y para poder resolver la situación sin un gran impacto para el usuario, ahora existen estos dos botones como funcionalidades avanzadas.

!!! info
    Este proceso afectará el saldo inicial y final de los documentos posteriores siempre que el saldo final cambie para la conciliación que se está editando.

#### Transferencia de Fondos

La funcionalidad de Transferencia de Fondos en la ventana Cuenta Financiera permite el movimiento de dinero entre dos cuentas financieras diferentes dentro de una organización. Esta acción se utiliza normalmente para transferencias internas, como mover fondos de una cuenta bancaria a una caja chica, o entre cuentas en diferentes monedas.

![Transferencia de fondos](../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions/funds-transfer.png)

Campos a destacar:

- **Fecha de transacción**: Es obligatoria. Esta fecha se utiliza para los registros que crea este proceso: fecha de transacción y fecha contable.
- **Depositar en**: Este desplegable muestra todas las cuentas financieras que pertenecen al árbol de organizaciones de la cuenta financiera seleccionada y que tienen habilitado el indicador **Transferencia de Fondos**.
- **Concepto Contable**: El valor predeterminado se establece a partir del **Concepto Contable Predeterminado para Transferencia de Fondos** configurado en la organización de la cuenta financiera o en su organización principal. El usuario puede sobrescribir este parámetro. Este desplegable muestra todos los Conceptos Contables que pertenecen al árbol de organizaciones de la cuenta financiera seleccionada.
- **Importe de depósito**: Obligatorio.
- **Moneda de origen**: No editable. Moneda de la cuenta financiera seleccionada.
- **Moneda de destino**: No editable. Moneda de la cuenta financiera de destino.
- **Multiplicar por**: La tasa de conversión de una moneda a otra:
    - Es nula por defecto.
    - Se muestra solo cuando las monedas son diferentes.
    - En caso de que el usuario deje este valor como nulo, el sistema utiliza la [tasa de conversión](../../general-setup/application/conversion-rates.md) configurada en el sistema para esa fecha. Si no hay nada definido, se muestra un error.
- **Comisión bancaria**: La comisión cobrada por el banco desde/hacia donde se originó/recibió la transacción. No marcada por defecto. Cuando se marca, se muestran dos campos adicionales:
    - Comisión bancaria de origen: Para introducir el importe de la comisión correspondiente.
    - Comisión bancaria de destino: Para introducir el importe de la comisión correspondiente.
- **Descripción**: La descripción se establece como **Transacción de Transferencia de Fondos** por defecto. El usuario puede sobrescribir la descripción si es necesario.

## Pestañas

### Transacción

Las transacciones de una cuenta financiera pueden ser de dos tipos:

- Transacciones de **Depósito**, en el caso de recibir el pago de cualquier tipo de documento (factura, pedido, concepto contable o comisión).
- o transacciones de **Retiro**, en el caso de realizar un pago de cualquier tipo de documento (factura, pedido, concepto contable o comisión).

Estos dos tipos de transacciones pueden crearse de tres formas:

- **Automáticamente**, si el método de pago utilizado para pagar un documento (y asignado a una cuenta financiera determinada) está configurado para ello:
    - Los pagos a proveedores una vez procesados en la ventana Pago se retiran automáticamente de la cuenta financiera.
    - Los pagos de clientes una vez procesados en la ventana Cobro se depositan automáticamente en la cuenta financiera.
    - o los "Pagos de Conceptos Contables" una vez creados en un Libro Diario se depositan/retiran automáticamente de la cuenta financiera.

- **En lote**, agregando varios pagos como transacciones a través de la ventana de proceso Agregar Múltiples Pagos.

- o **Manualmente**, creando un nuevo registro en la pestaña de transacciones de la ventana Cuenta Financiera.

![Pestaña de transacciones](../../../../../assets/drive/1zirkJ20dd1aVDIxtvwQeYybbNxP_tXiI.png)

- Campos a destacar en la pestaña de transacciones:
    - **Tipo de Transacción:** El Tipo de Transacción indica el tipo de transacción a procesar. La pestaña de transacciones también permite al usuario crear transacciones de "Depósito" o "Retiro" basadas en un tipo de transacción de "Concepto Contable" o en un "Pago".
        - Comisión bancaria
        - Depósito de Tercero
        - Retiro de Tercero
    - **Fecha de Transacción:** El campo Fecha de Transacción define la fecha de la transacción que se está procesando.
    - **Fecha Contable:** La fecha en que esta transacción se registra en el libro mayor.
    - **Pago:** Selector de pago.
    - **Concepto Contable:** Selector de concepto de libro mayor.
    - **Moneda:** Indica la moneda que se utilizará al procesar este documento.
    - **Importe del Depósito:** importe en el caso de recibir un pago.
    - **Importe del Retiro:** importe en el caso de realizar un pago.
    - **Dimensiones:** Información de Organización, Tercero y Proyecto.
    - **Importe en Moneda Extranjera**: Solo se muestra en la vista de grilla. Esta columna se rellena si el pago fue recibido o realizado en una moneda diferente a la moneda de la cuenta financiera.
    - **Moneda Extranjera**: Solo se muestra en la vista de grilla. Esta columna se rellena si el pago fue recibido o realizado en una moneda diferente a la moneda de la cuenta financiera.

        !!! info
            Es posible permitir al usuario **recibir o realizar pagos en múltiples monedas** (moneda extranjera), al configurar los métodos de pago asignados a una cuenta financiera determinada. Para más información sobre esta opción, visite [Método de Pago](../../financial-management/receivables-and-payables/setup/payment-method.md).


![Comisión bancaria](../../../../../assets/drive/1hhSs7pd6WDlXjs26eC2SDsJ8vfo5kh7r.png)

1. Si es necesario crear una **Comisión Bancaria**, seleccione **Comisión Bancaria** en el desplegable Tipo de Transacción, introduzca una fecha de transacción y contable y el importe recibido o pagado.

2. Luego guarde y procese la transacción.


![Concepto Contable](../../../../../assets/drive/1C72EAORDre8_Eh44Fv-dwNc_bOlO209D.png)

Para crear una nueva transacción de concepto contable, seleccione `Depósito de Tercero` o `Retiro de Tercero` en el tipo de transacción y seleccione el **Concepto Contable** en el desplegable de Concepto Contable, introduzca una fecha de transacción y contable, seleccione un Concepto Contable, introduzca el importe **recibido** o **pagado** y guarde y procese la transacción.

Si el usuario necesita crear una nueva transacción de pago, se permite seleccionar un pago creado o crear un nuevo pago desde el selector de pago.

- Si el pago está creado, el usuario debe elegir el pago en el selector de pagos.

    ![Selector de pago](../../../../../assets/drive/1kLQZA0e7fHQtD4ZBSby4h-glL5R4DOAH.png)

Los campos de descripción e importe en la pestaña de transacciones se completarán automáticamente y para completar la transacción es necesario guardar y procesar.

Si es necesario crear una transacción de depósito de pago, el usuario debe hacer clic en el botón '+' en el selector de pago y se abrirá un pop-up de agregar pago. En el campo "Documento" debe seleccionarse "**Recibido**".  
Esta ventana permite:

- seleccionar pagos ya creados y procesados
  - usar el campo "Recibido de" para acotar la búsqueda de documentos a pagar
- usar el "Crédito Disponible" del tercero, si lo hubiera, seleccionando el crédito en la grilla de crédito
- introducir el importe del "Pago Real" recibido
- introducir una "Fecha de Pago"
- seleccionar el "Tipo de Transacción" a pagar
- usar otros filtros como el "Nº de Documento" del Pedido o Factura o el "Importe Desde/Hasta"
- y finalmente introducir un "Pago de Concepto Contable" si es necesario, agregando "Conceptos Contables" en una grilla de conceptos contables.  
  El último paso es procesar el pago recién creado y que quede depositado en la cuenta financiera.

![Transacción de depósito de pago](../../../../../assets/drive/1j47oaWj1O4_LLGPha7guEuKBccB3Rn0h.png)

Si es necesario crear una **transacción de retiro de pago**, el usuario debe hacer clic en el botón '+' en el selector de pago y se abrirá un pop-up de agregar pago. En el pop-up de agregar pago, debe seleccionarse la opción "**Pagado**" en el campo "Documento". Esta ventana permite al usuario:

- seleccionar pagos ya creados y procesados
- usar el campo "A Pagar A" para acotar la búsqueda de documentos a pagar
- usar el "Crédito Disponible" del tercero, si lo hubiera, seleccionando el crédito en la grilla de crédito
- introducir una "Fecha de Pago"
- seleccionar el "Tipo de Transacción" a pagar
- usar otros filtros como el "Nº de Documento" del Pedido o Factura o el "Importe Desde/Hasta"
- y finalmente introducir un "Pago de Concepto Contable" si es necesario, agregando "Conceptos Contables" en una grilla de conceptos contables.  
  El último paso es procesar el pago recién creado y que quede depositado en la cuenta financiera.

![Retiro de pago](../../../../../assets/drive/1DbaEJtPopUAIr5_S_L8g3mVOk3TQlqOT.png)

El selector de pago tiene aplicado un filtro explícito (cuenta financiera actual).

![Pago filtrado](../../../../../assets/drive/1DWBNx-RWSxny0gHyXIU2D-0cuKyKY5iA.png)

Es posible agregar pagos de cuentas financieras alternativas haciendo clic en el icono de embudo para limpiar los filtros.

![Pago sin filtro](../../../../../assets/drive/1dtzHFshO4AwVVl5S6FPHiHp9YqHgs4Hy.png)

#### Tipos de Cambio

Esta subpestaña permite al usuario definir un tipo de cambio para usar al contabilizar la transacción de la cuenta financiera en el libro mayor cuando la moneda de la cuenta financiera no es la misma que la moneda del libro mayor.

#### Historial de Contabilización

Esta subpestaña muestra el historial de contabilización de una transacción determinada.

![Historial de contabilización](../../../../../assets/drive/1Bjg-OJiKl8bBeYN36lxwYnIUgtl1dbP3.png)

Como se muestra en la imagen anterior, esta pestaña muestra los asientos del libro mayor creados al contabilizar/descontabilizar una transacción determinada.

### Configuración Contable

La pestaña de configuración contable se utiliza para definir las cuentas de un Libro Mayor a usar al contabilizar transacciones como una comisión bancaria o un depósito.

![Configuración contable](../../../../../assets/drive/1CYADTe8Ks-V7eoJVPSmVP8-8Ighure6S.png)

Como se muestra en la imagen anterior, las cuentas que se detallan a continuación pueden configurarse para una cuenta financiera y un libro mayor.

Sección **General**:

- **Cuenta de Ganancia por Revaluación Bancaria**, esta cuenta se utiliza para acreditar/debitar una ganancia por tipo de cambio:
  - La ganancia correspondiente a una disminución del tipo de cambio al realizar un pago se acredita en esta cuenta.
  - La ganancia correspondiente a un aumento del tipo de cambio al recibir un pago se acredita en esta cuenta.

!!! info
    Recuerde que es posible recibir pagos y realizar pagos en una moneda diferente a la moneda de la cuenta financiera.

En el caso de un tipo de Cuenta Financiera "Caja", la cuenta contable usada para acreditar una ganancia por tipo de cambio es la cuenta "**Ganancia por Revaluación Bancaria**" de la pestaña Valores Predeterminados de la Configuración del Libro Mayor.

- **Cuenta de Pérdida por Revaluación Bancaria** utilizada para debitar/acreditar una pérdida por tipo de cambio:
  - La pérdida correspondiente a un aumento del tipo de cambio al realizar un pago se debita en esta cuenta.
  - La pérdida correspondiente a una disminución del tipo de cambio al recibir un pago se debita en esta cuenta.

En el caso de un tipo de Cuenta Financiera "Caja", la cuenta contable usada para acreditar una ganancia por tipo de cambio es la cuenta "**Pérdida por Revaluación Bancaria**" de la pestaña Valores Predeterminados de la Configuración del Libro Mayor.

- **Cuenta de Comisiones Bancarias** utilizada para debitar/acreditar gastos/ingresos por comisiones.

La casilla de verificación **Habilitar Extracto Bancario** permite al usuario contabilizar Extractos Bancarios. Si se selecciona, se muestran dos campos adicionales:

- **Cuenta de Activo Bancario**
- **Cuenta Transitoria Bancaria**

Dado que la contabilización de un extracto bancario es una contabilización transitoria hasta que las transacciones se hayan saldado definitivamente, la "Cuenta Transitoria Bancaria" debe ser la misma cuenta que la utilizada al saldar.

En cuanto se define una "Cuenta Transitoria Bancaria", el sistema muestra una advertencia indicando que "Al contabilizar Extractos Bancarios, la Cuenta Transitoria Bancaria debe coincidir con la cuenta utilizada al saldar para todos los métodos de pago con el fin de garantizar una contabilidad correctamente equilibrada. ¿Desea propagar este valor a todos los métodos de pago?"

- Si el usuario hace clic en (SÍ), el sistema rellena la Cuenta Transitoria Bancaria seleccionada en el campo "Cuenta de Pago Saldado" de las secciones "Cobro" y "Pago".

Secciones **Cobro / Pago**:

Estas secciones de la pestaña de configuración contable están estrechamente relacionadas con otra pestaña de la ventana Cuenta Financiera, la pestaña Método de Pago.

La pestaña Método de Pago permite al usuario definir qué paso del flujo de trabajo de pago puede contabilizarse en el libro mayor. Esto puede definirse para cada método de pago asignado a la cuenta financiera.

La pestaña "Configuración Contable" permite al usuario seleccionar las cuentas contables a utilizar al contabilizar pagos en tránsito de entrada/salida, transacciones de depósito/retiro o conciliaciones vinculadas a un método de pago determinado.

Es importante destacar que:

- Ninguno de los campos de la sección "**Cobro**" y "**Pago**" es obligatorio, ya que el proceso contable puede ser diferente dependiendo de la configuración del método de pago.
- Sin embargo, si alguno de esos campos está "vacío", por ejemplo la "**Cuenta de Depósito**", mientras se ha configurado para un método de pago determinado asignado a la cuenta financiera que la transacción de "Depósito" debe contabilizarse, el proceso de contabilización generará un error.

En detalle:

Sección **Cobro**:

- **Cuenta de Pago en Tránsito**: Esta es la cuenta que se usará en el primer paso, cuando el recibo del pago se registra en la ventana "Cobro".  
  El Método de Pago utilizado debe tener el valor "Cuenta de Pago en Tránsito" definido en el campo "Al Recibir usar".
- **Cuenta de Pago Depositado**: Esta es la cuenta que se usará para contabilizar la segunda fase, es decir, el "Depósito" del recibo en la Cuenta Financiera. El Método de Pago utilizado debe tener el valor "Cuenta de Pago Depositado" definido en el campo "Al Depositar usar".
- **Cuenta de Pago Saldado**: Esta es la cuenta que se usará para contabilizar el tercer paso, es decir, la conciliación del depósito. El método de pago utilizado debe tener el valor "Cuenta de Pago Saldado" definido en el campo "Al Conciliar usar".

Sección **Pago**:

- **Cuenta de Pago en Tránsito**: Esta es la cuenta que se usará en el primer paso, cuando el pago se realiza en la ventana "Pago". El Método de Pago utilizado debe tener el valor "Cuenta de Pago en Tránsito" definido en el campo "Al Pagar usar".
- **Cuenta de Pago Retirado**: Esta es la cuenta que se usará para contabilizar la segunda fase, es decir, el "Retiro" del pago en la Cuenta Financiera. El Método de Pago utilizado debe tener el valor "Cuenta de Pago Retirado" definido en el campo "Al Retirar usar".
- **Cuenta de Pago Saldado**: Esta es la cuenta que se usará para contabilizar el tercer paso, es decir, la conciliación del retiro. El Método de Pago utilizado debe tener el valor "Cuenta de Pago Saldado" definido en el campo "Al Conciliar usar".

### Método de Pago

Esta pestaña enumera todos los métodos de pago asignados a la cuenta financiera. Un pago puede depositarse en o retirarse de la cuenta financiera si el método de pago utilizado está asignado a la cuenta financiera.

Cada Cuenta Financiera puede tener más de un método de pago asignado, como "Cheque", "Transferencia Bancaria", "Efectivo".

El hecho de asignar un método de pago o un conjunto de métodos de pago a una cuenta financiera determinada significa que es posible gestionar a través de una cuenta financiera determinada solo aquellos pagos vinculados a cualquiera de los métodos de pago asignados a esa cuenta financiera.

Los Métodos de Pago se crean y configuran en la ventana Método de Pago. Una vez creados y configurados, pueden asignarse a una cuenta financiera en esta pestaña. La forma de hacerlo es:

- Hacer clic en la pestaña "**Método de Pago**" de la cuenta financiera.
- Crear un nuevo registro.
- En la lista desplegable "**Método de Pago**", seleccionar un pago.
  - Esta acción completa automáticamente la configuración predeterminada del método de pago.
- Modificar la configuración predeterminada si es necesario.
  - Cualquier cambio en esa configuración no modifica la configuración predeterminada del método de pago, ya que solo se aplica a la forma en que ese método de pago se comportará al utilizarse en la cuenta financiera seleccionada.

En esta pestaña, existe la funcionalidad avanzada (oculta por defecto) denominada **control de estado de factura pagada**, que proporciona una opción de configuración para decidir qué estado de cada pago determina si una factura está pagada o no.

- **Combo de estado de factura pagada**: Establece el estado a partir del cual se considera que una factura está pagada.

Este combo puede establecerse a nivel de método de pago (cobro y pago) en cada cuenta financiera. Por defecto, este combo está establecido como **pago recibido** o **pago realizado**, por lo que se obtiene el comportamiento habitual de Etendo.

!!! info
    Para información adicional sobre la configuración del método de pago, visite el artículo [_Método de Pago_](../../financial-management/receivables-and-payables/setup/payment-method.md).

### Extractos Bancarios Importados

La pestaña enumera los archivos de extracto bancario importados, así como los extractos bancarios creados manualmente.

![Extractos bancarios importados](../../../../../assets/drive/1JYuyMUUrwVxlwti9FdfNcdz_t-DgIPY3.png)

Campos clave a destacar:

- **Nº de Documento:** es el número del extracto bancario importado que proporciona la secuencia de documentos correspondiente.
- **Tipo de Documento:** es la categoría de documento "Archivo de Extracto Bancario" (no "Extracto Bancario").
- **Nombre:** es el nombre dado por Etendo, que es una combinación de las fechas de transacción y la diferencia de importe de entrada/salida.
- **Fecha de Importación:** es la fecha en que se importó el archivo.
- **Fecha de Transacción:** es la fecha a usar al contabilizar el extracto bancario en el libro mayor.
- **Nombre del archivo:** es el nombre del archivo importado.

Un archivo de extracto bancario importado puede ser "**Reactivado**", ya que una vez importado se procesa automáticamente.

Una vez reactivado, la información de la cabecera del extracto bancario, así como las líneas del extracto bancario, pueden modificarse según sea necesario.

Una vez hecho esto, el extracto bancario puede **Procesarse** de nuevo.

Un extracto bancario puede contabilizarse si esto está habilitado en la pestaña de configuración contable de la cuenta financiera.

!!! info
    Si el usuario no puede importar un archivo de extracto bancario, también es posible crear extractos bancarios y líneas de extracto bancario manualmente.

#### Líneas del Extracto Bancario

Esta pestaña enumera todas las líneas de un extracto bancario.

Campos clave a destacar:

- **Nombre del Tercero:** este campo muestra el nombre del tercero en las líneas del extracto bancario.
- **Tercero:** este campo muestra el tercero encontrado en Etendo por el algoritmo de conciliación, si lo hubiera.
- **Concepto Contable:** este campo permite introducir manualmente un Concepto Contable si se sabe que una línea del extracto bancario está relacionada con una transacción contable. Etendo recordará que el texto de una línea del extracto bancario estaba relacionado con una transacción contable determinada la próxima vez que se importe un archivo de extracto bancario.  
  El concepto contable introducido aquí será utilizado por el algoritmo de conciliación al conciliar las líneas del extracto bancario con las transacciones de la cuenta financiera.
- **Importe de Salida:** es el importe cargado de la línea del extracto bancario.
- **Importe de Entrada:** es el importe recibido de la línea del extracto bancario.
- **Transacción de Cuenta Financiera:** es la transacción de la cuenta financiera una vez conciliada con la línea del extracto bancario; puede estar vacía cuando no se ha encontrado ninguna transacción coincidente.
- **Tipo de conciliación:** puede ser "Manual" o "Automática" dependiendo de quién realizó la conciliación, ya sea el algoritmo de conciliación utilizado o el usuario.

### Conciliaciones

La pestaña de conciliaciones muestra las conciliaciones creadas manualmente si no hay ningún algoritmo de conciliación asignado a la cuenta financiera, así como las creadas al conciliar un archivo de extracto bancario importado en caso contrario.

#### Conciliaciones Manuales

- Como ya se explicó, el botón de proceso Conciliar permite al usuario conciliar manualmente las transacciones existentes de la cuenta financiera en la ventana "Conciliación".
- Cada conciliación de este tipo, una vez guardada, se guarda también en esta pestaña en estado "**Borrador**" hasta que finalmente se concilia en la ventana "**Conciliación**", por lo que su estado cambia a "**Completada**".
- Es posible "**Reactivar**" una conciliación de este tipo, por lo que puede modificarse en la ventana "**Conciliación**" y conciliarse desde esa ventana una vez más.

#### Conciliaciones Automáticas

- De igual forma, una vez importado un archivo de extracto bancario, las líneas del extracto bancario pueden conciliarse automáticamente en la ventana "**Conciliación mediante Líneas de Extracto Bancario Importadas**", accesible desde el botón de proceso Conciliar Extracto.
- Cada conciliación de este tipo, una vez guardada, se guarda también en esta pestaña en estado "**Borrador**" hasta que finalmente se concilia en la ventana "Conciliación mediante Líneas de Extracto Bancario Importadas", por lo que su estado cambia a "**Completada**".
- Es posible "**Reactivar**" una conciliación de este tipo, por lo que puede modificarse en la ventana "**Conciliación mediante Líneas de Extracto Bancario Importadas**" y conciliarse desde esa ventana una vez más.

![Conciliaciones](../../../../../assets/drive/1ptaQQlAalghp30dTWFwNGupZaaGIhujf.png)

#### Contabilización de Conciliaciones

Una Conciliación de cualquier tipo puede contabilizarse si el Método de Pago utilizado al crear el pago a conciliar lo permite una vez asignado a la cuenta financiera. Si no es el caso, Etendo muestra una advertencia: "Documento deshabilitado para contabilidad".

Una contabilización de "**Conciliación de Depósito**" se ve así:

a. si el Pago Recibido NO fue contabilizado en la ventana **"Cobro"** y la Transacción de Depósito tampoco fue contabilizada en la ventana "**Cuenta Financiera**":

|                                                                     |                 |                 |
| ------------------------------------------------------------------- | --------------- | --------------- |
| Cuenta                                                              | Debe            | Haber           |
| Al Conciliar usar la "Cuenta de Pago Saldado" (ej.)                 | Importe del pago |                 |
| Créditos de Clientes                                                |                 | Importe del pago |

b. si el Pago Recibido fue contabilizado en la ventana **"Cobro"** y la Transacción de Depósito NO fue contabilizada en la ventana "**Cuenta Financiera**":

|                                                                       |                 |                 |
| --------------------------------------------------------------------- | --------------- | --------------- |
| Cuenta                                                                | Debe            | Haber           |
| Al Conciliar usar la "Cuenta de Pago Saldado" (ej.)                   | Importe del pago |                 |
| Al Recibir usar la "Cuenta de Pago en Tránsito Cobro" (ej.)           |                 | Importe del pago |

c. si el Pago Recibido fue contabilizado o no en la ventana **"Cobro"** y la Transacción de Depósito fue contabilizada en la ventana "**Cuenta Financiera**":

|                                                                     |                 |                 |
| ------------------------------------------------------------------- | --------------- | --------------- |
| Cuenta                                                              | Debe            | Haber           |
| Al Conciliar usar la "Cuenta de Pago Saldado" (ej.)                 | Importe del pago |                 |
| Al Depositar usar la "Cuenta de Depósito" (ej.)                     |                 | Importe del pago |

!!! info
    Cada contabilización será diferente cuando el importe provenga parcial o totalmente de una deuda clasificada como dudosa. En ese caso, la contabilización se realizará como se explica en la página [_Ejecución de Deudas Dudosas_](./doubtful-debt-run.md).

Una contabilización de "**Conciliación de Retiro**" se ve así:

a. si el Pago Realizado NO fue contabilizado en la ventana **"Pago"** y la transacción de Retiro tampoco fue contabilizada en la ventana **Cuenta Financiera**:

|                                                                     |                 |                 |
| ------------------------------------------------------------------- | --------------- | --------------- |
| Cuenta                                                              | Debe            | Haber           |
| Deuda con Proveedores                                               | Importe del pago |                 |
| Al Conciliar usar la "Cuenta de Pago Saldado" (ej.)                 |                 | Importe del pago |

b. si el Pago Realizado fue contabilizado en la ventana **"Pago"** y la transacción de Retiro NO fue contabilizada en la ventana **Cuenta Financiera**:

|                                                                          |                 |                 |
| ------------------------------------------------------------------------ | --------------- | --------------- |
| Cuenta                                                                   | Debe            | Haber           |
| Al Pagar usar la "Cuenta de Pago en Tránsito Pago" (ej.)                 | Importe del pago |                 |
| Al Conciliar usar la "Cuenta de Pago Saldado" (ej.)                      |                 | Importe del pago |

c. si el Pago Realizado fue contabilizado o no en la ventana **"Pago"** y la transacción de Retiro fue contabilizada en la ventana **Cuenta Financiera**:

|                                                                         |                 |                 |
| ----------------------------------------------------------------------- | --------------- | --------------- |
| Cuenta                                                                  | Debe            | Haber           |
| Al Retirar usar la "Cuenta de Retiro" (ej.)                             | Importe del pago |                 |
| Al Conciliar usar la "Cuenta de Pago Saldado" (ej.)                     |                 | Importe del pago |

#### Informes de Conciliaciones

Además, existen dos informes que muestran información sobre cada conciliación; estos informes pueden ejecutarse desde los botones de proceso:

- Detalles de Conciliaciones
- Resumen de Conciliación

#### Elementos Saldados

Esta pestaña muestra las transacciones saldadas o marcadas como conciliadas en una conciliación.

En cuanto una conciliación **manual** o **automática** es "Guardada" en estado "**Borrador**" en la pestaña Conciliaciones, esta subpestaña permite ver las transacciones saldadas en la ventana Conciliación o conciliadas contra una línea del extracto bancario en la ventana Conciliación mediante Líneas de Extracto Bancario Importadas.

No es posible eliminar los elementos saldados desde esta subpestaña, sino desde la ventana "Conciliación" o la ventana "Conciliación mediante Líneas de Extracto Bancario Importadas" cuando la conciliación ha sido "**reactivada**".

La subpestaña de elementos saldados permite ver la siguiente información:

- la **transacción de cuenta financiera** conciliada
- el **pago** conciliado
- la **descripción** de la transacción conciliada, por ejemplo "Factura Nº:..."
- y el **Importe del Depósito** o el **Importe del Retiro** de la transacción saldada.

### Contabilidad

La pestaña de contabilidad es una pestaña de solo lectura que muestra la contabilización de cada transacción de la cuenta financiera.

## Eliminación de Pagos

El objetivo de esta funcionalidad es eliminar y reactivar pagos de forma ágil y sencilla. Además, permite eliminar y reactivar transacciones bancarias y conciliaciones.

!!! info
    Para poder incluir esta funcionalidad, se debe instalar el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, la compatibilidad con el núcleo y las nuevas funcionalidades, visite [Financial Extensions - Notas de versión](../../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

### Transacciones

Desde esta ventana, es posible eliminar y reactivar las transacciones incluidas en una cuenta financiera.

Los pagos pueden encontrarse en esta instancia en los estados Retirado no Saldado, Depositado no Saldado y Pago saldado; en este último caso el pago ya está conciliado y, por tanto, relacionado con una conciliación bancaria y un extracto bancario.

Para eliminar una transacción, seleccione el registro correspondiente en la pestaña Transacción y haga clic en el botón Eliminar Transacción. Si el pago está en estado Depositado no Saldado o Retirado no Saldado, el proceso elimina la transacción de la cuenta financiera y el pago vuelve a su estado anterior. Si el estado es Pago saldado, el proceso también elimina la línea de conciliación relacionada y la línea del extracto bancario relacionada.

Tenga en cuenta que:

Si la conciliación está completada y el resto de las conciliaciones existentes también están completadas, entonces la conciliación en cuestión se reabre para eliminar la línea de conciliación correspondiente y se cierra de nuevo.
Si la conciliación está completada y hay una conciliación en estado Borrador, la conciliación en borrador se cerrará, la conciliación correspondiente se reactivará, la línea de conciliación correspondiente se eliminará, se cerrará de nuevo y la que estaba en estado Borrador se reactivará.

Para reactivar una transacción, seleccione el registro correspondiente en la pestaña Transacción y haga clic en el botón Reactivar Transacción. Si el pago está en estado Depositado no Saldado o Retirado no Saldado, el pago vuelve a su estado anterior pero permanecerá asociado a la cuenta financiera. Si el estado es Pago saldado, el proceso también elimina la línea de conciliación relacionada y la línea del extracto bancario relacionada.

Considere los siguientes casos:

- Si la conciliación está completada y el resto de las conciliaciones existentes están completadas, entonces la conciliación en cuestión se reabrirá para eliminar la línea de conciliación correspondiente y se cerrará de nuevo.
- Si la conciliación está completada y hay una conciliación en estado Borrador, la conciliación en borrador se cerrará, la conciliación correspondiente se reactivará, la línea de conciliación correspondiente se eliminará, se cerrará de nuevo y la que estaba en estado Borrador se reactivará.

![](../../../../../assets/drive/1M_IDKW70W9wRHEkPK6Uw9uLvfD03wyxx.png)

### Conciliaciones

Es posible eliminar y reactivar conciliaciones bancarias.

Las siguientes situaciones son posibles:

- Eliminar una conciliación en estado Completada o Borrador: en este caso, la conciliación correspondiente se elimina, las líneas del extracto bancario asociadas a ella y los pagos conciliados en ella cambian su estado a Depositado no Saldado o Retirado no Saldado.
- Reactivar una conciliación en estado Completada. Las demás conciliaciones existentes también están en estado Completada: en este caso, la conciliación se reactiva y su estado vuelve a Borrador.
- Reactivar una conciliación en estado Completada. Hay otra conciliación en estado Borrador: en este caso, la conciliación en estado Borrador se completa primero y la conciliación seleccionada se reactiva y su nuevo estado será: Borrador.

![](../../../../../assets/drive/1ZyeE1vy7Gri5kslKF1fq1PzohDkwVPwK.png)

## Contabilización Masiva

!!! info
    Para poder incluir esta funcionalidad, se debe instalar el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, la compatibilidad con el núcleo y las nuevas funcionalidades, visite [Financial Extensions - Notas de versión](../../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

La funcionalidad de Contabilización Masiva permite al usuario contabilizar o descontabilizar múltiples registros seleccionándolos y haciendo clic en el botón **Contabilización masiva**. En el caso de la ventana "Cuenta Financiera", esta opción puede utilizarse en tres pestañas: Transacción, Extractos Bancarios Importados y Conciliaciones.

Además, el Estado de Contabilización del/los registro/s se muestra en la barra de estado, en la vista de formulario, o en una columna, en la vista de grilla.

!!! info
    Para más información, visite [la guía de usuario del módulo Contabilización Masiva](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).

## Liquidación Avanzada de Tercero

!!! info
    Para poder incluir esta funcionalidad, se debe instalar el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}. Para más información sobre las versiones disponibles, la compatibilidad con el núcleo y las nuevas funcionalidades, visite [Financial Extensions - Notas de versión](../../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

Etendo permite realizar una liquidación desde una conciliación bancaria.
Desde la ventana **Cuenta Financiera**, una vez que los extractos bancarios ya están importados y procesados, el usuario puede seleccionar el extracto bancario de la cuenta financiera y conciliarlo con la factura a pagar haciendo clic en el botón **Conciliar Extracto**.

![](../../../../../assets/drive/11F6-j76ebOwud3SCfJNtfFhgfuAcjh5d.png)

En la ventana emergente, Etendo muestra una lista de facturas a liquidar, cada una con su número de factura correspondiente; aquí el usuario puede seleccionar la factura correspondiente para compensar con su importe de **Pago Real** a pagar.

![](../../../../../assets/drive/1GufQeDY76qDFzfshhuTzhogcH10T0zxb.png)

Desde la pestaña **Factura de Compensación**, el usuario selecciona la factura que se utilizará para pagar (ya sea de ventas o de compras, dependiendo de la factura previamente seleccionada) y establece el importe necesario de la factura a compensar.

![](../../../../../assets/drive/1nRmzMoT6EiyE2m0yvApx99cpJladJZkA.png)

Tras hacer clic en el botón Aceptar, Etendo abre otra ventana emergente para mostrar la información de la nueva liquidación a crear, para que el usuario confirme los detalles haciendo clic en Aceptar.

![](../../../../../assets/drive/1XvbDRrKkyoporgm2uVTBDg-72m2iOOaa.png)

El registro de liquidación (cobro y pago) también queda registrado en la ventana **Liquidación de Tercero**, donde se mostrará una línea para la factura (de ventas y compras) utilizada para la compensación.

![](../../../../../assets/drive/1v1dM1rAImvwdfJLXtQYzzwKNH6BBALbm.png)

!!! info
    Para más información, visite la [Guía de Usuario del Módulo Liquidación de Tercero](../../../optional-features/bundles/financial-extensions/business-partner-settlement.md).

---

This work is a derivative of [Financial Management](http://wiki.openbravo.com/wiki/Financial_Management){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
