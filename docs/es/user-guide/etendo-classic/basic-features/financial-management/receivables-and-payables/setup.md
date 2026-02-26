---
title: Configuración de Gestión Financiera
---
## Visión general

Esta sección describe las ventanas necesarias para configurar las transacciones de gestión financiera relativas a la gestión de cobros y pagos en Etendo. Las ventanas correspondientes son:

[:material-file-document-outline: Tipo de registro de impuesto](#tipo-de-registro-de-impuesto){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Método de pago](#método-de-pago){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Algoritmo de Reconciliación](#algoritmo-de-reconciliación){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Formato Fichero Banco](#formato-fichero-banco){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Proceso de Ejecución](#proceso-de-ejecución){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Tipo remesas](#tipo-remesas){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Método de dudoso cobro](#método-de-dudoso-cobro){ .md-button .md-button--primary } <br>
## Tipo de registro de impuesto

:material-menu: `Aplicación` > `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Configuración` > `Tipo de registro de impuesto`

### Visión general

Un tipo de registro de impuesto se utiliza para recopilar todos los rangos de impuesto de un tipo que se deben tener en cuenta al calcular el importe total del impuesto de un tipo de registro de impuesto determinado dentro de un periodo de tiempo.

Los tipos de registro de impuesto son una variable clave del proceso **Pago del impuesto**, ya que es el proceso que calcula el importe total del impuesto de cada tipo de registro de impuesto creado y configurado.

En otras palabras, el proceso "Pago del impuesto" ayuda a calcular el importe de los impuestos a pagar a, o a recibir de, la autoridad fiscal correspondiente como la diferencia entre:

-   los tipos de registro de impuesto de "Ventas" o el importe total del impuesto que una organización repercute y que pagan sus clientes
-   y los tipos de registro de impuesto de "Compra" o el importe total del impuesto que una organización paga a otras empresas por los suministros que recibe.

### Cabecera

La ventana de tipo de registro de impuesto permite al usuario crear tipos de registro de impuesto.

![Cabecera del Tipo de registro de impuesto](../../../../../assets/drive/1wwI271qWNtJQmMZxupMktzWI6S3ByU6w.png)

Tal y como se muestra en la imagen anterior, es posible crear:

-   tipos de registro de impuesto relacionados con "**Ventas**", que por tanto incluirán **rangos de impuesto relacionados con ventas** en la pestaña "**Líneas**"
-   así como tipos de registro de impuesto relacionados con "**Compra**", que por tanto incluirán **rangos de impuesto relacionados con compras** en la pestaña "**Líneas**"

Además, cada tipo de registro de impuesto debe estar vinculado a un elemento de mayor (G/L Item).

Las cuentas contables definidas para ese elemento de mayor serán las que se utilizarán al contabilizar el pago del impuesto calculado como la diferencia entre el tipo de registro de impuesto de "Ventas" y el tipo de registro de impuesto de "Compra".

### Líneas

La pestaña de líneas permite al usuario asociar rangos de impuesto al tipo de registro de impuesto.

![Líneas del Tipo de registro de impuesto](../../../../../assets/drive/1O_4QacWfrELWWRoG5Ye2E73Fa8AIi8i1.png)

Tal y como se muestra en la imagen anterior, cada rango de impuesto seleccionado también debe estar vinculado a un tipo de documento.

Por tanto, no solo es posible configurar los rangos de impuesto que serán tenidos en cuenta por el proceso de pago del impuesto como parte de un tipo de registro de impuesto, sino también los tipos de documento que se tendrán en cuenta.

Los **tipos de documento de ventas** que se pueden vincular al impuesto de ventas correspondiente son:

-   Factura de clientes (AR)
-   Abono de clientes (AR)
-   Factura de ventas revertida
-   Factura de ventas de devolución de material ES

Los **tipos de documento de compra** que se pueden vincular al impuesto de ventas correspondiente son:

-   Factura de proveedores (AP)
-   Abono de proveedores (AP)
-   Factura de compra revertida
## Método de pago

:material-menu: `Aplicación` > `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Configuración` > `Método de pago`

### Visión general

Los **Método de pago** representan medios de pago empleados por su empresa o por un tercero, tales como:

-   Efectivo
-   Tarjeta de crédito
-   PayPal
-   Cheque
-   Adeudo directo
-   Orden permanente
-   Transferencia bancaria
-   Pagaré

Cada **transacción de pago** está asociada a un **Método de pago**. Un método de pago define cómo se va a gestionar un cobro/pago dentro del ciclo de cobros y pagos de gestión de cobros y pagos y, además, cómo se va a contabilizar.

Los **Método de pago** están asociados a cuentas financieras, de manera que los cobros y pagos puedan registrarse en un banco o en una caja.

Los métodos de pago que pueden utilizarse dentro de la gestión de cobros y pagos son los asignados a una cuenta financiera; por lo tanto, si es necesario modificar cualquier configuración del método de pago, debe hacerse en la solapa Método de pago de la cuenta financiera.

Es posible asociar múltiples **Método de pago** a una única cuenta financiera.

Por ejemplo, tanto los pagos mediante cheque como los pagos electrónicos pueden asociarse a una única cuenta financiera, ya que cada método de pago tiene su propia configuración.
#### Ciclo de pago

Para comprender mejor la configuración de un **Método de pago**, es necesario entender el flujo de eventos dentro del ciclo de pago:

-   **Parte:** el pedido de venta o el pedido de compra se utiliza en este proceso de gestión de cobros y pagos en el caso de un pago anticipado:
    -   cuando se contabiliza la factura de venta o la factura de compra, la información de pago puede generarse para el pedido desde la ventana de Cobro o desde la ventana de Pago.
-   **Factura:** la factura de compra genera una deuda con un proveedor y la factura de venta un derecho de cobro frente a un cliente.
-   **Entrega o Pago:** el registro de la transferencia de dinero de entrada o de salida antes de que la transacción se confirme en nuestra cuenta bancaria o caja.
-   **Actualización de la Cuenta financiera:** la adición de la transacción en la Cuenta financiera como un "Depósito" o como un "Reintegro", relacionada con el movimiento del dinero de entrada o de salida de nuestra cuenta bancaria o caja.
-   **Conciliación:** la confirmación del movimiento del dinero tras recibir el extracto bancario o el saldo de caja.

En la imagen siguiente se muestra un flujo de trabajo de pago simple:

![](../../../../../assets/drive/1MwU8f0EaeyCjJveISM3RGAnFAfSHfq4N.png)


A continuación se describe la forma de crear cada etapa del pago en Etendo:

**Primera etapa:**

Una "**Entrega**" puede registrarse en:

-   la ventana Factura de venta mediante el botón de proceso "Añadir pago".
-   y en la ventana Cobro mediante el botón de proceso "Añadir Detalles de Pago".

Un "**Pago**" puede registrarse en:

-   la ventana Factura de compra mediante el botón de proceso "Añadir pago".
-   y en la ventana Pago mediante el botón de proceso "Añadir Detalles de Pago".

Las etapas de pago anteriores pueden crear un **evento contable** en función de la configuración contable del método de pago.

-   Si está configurado para contabilizar en esta etapa, las Entregas y los Pagos pueden contabilizarse en la ventana Cobro / ventana Pago mediante el botón de proceso "Contabilizar" o ejecutando el proceso en segundo plano de contabilidad.

**Segunda etapa:**

Un "**Depósito**" puede registrarse en:

-   la Cuenta financiera mediante el botón de proceso "Añadir transacción".
-   y en la ventana Cobro mediante el botón de proceso "Añadir Detalles de Pago" y, a continuación, la Acción: "Procesar cobro(s) recibido(s) y depósito"

Un "**Reintegro**" puede registrarse en:

-   la Cuenta financiera mediante el botón de proceso "Añadir transacción".
-   y en la ventana Pago mediante el botón de proceso "Añadir Detalles de Pago" y, a continuación, la acción: "Procesar pago(s) realizado(s) y reintegro"

Las etapas de pago anteriores pueden crear un **evento contable** en función de la configuración contable del método de pago.

-   Si está configurado para contabilizar en esta etapa, los Depósitos y los Reintegros pueden contabilizarse en la ventana Cuenta financiera mediante el botón de proceso "Contabilizar" o ejecutando el proceso en segundo plano de contabilidad.

**Tercera y última etapa:**

Una "**Conciliación**" puede registrarse en:

-   la solapa Conciliación de la ventana Cuenta financiera.

La etapa de pago anterior puede crear un **evento contable** en función de la configuración contable del método de pago.

-   Si está configurado para contabilizar en esta etapa, las Conciliaciones pueden contabilizarse en la solapa Conciliación de la ventana Cuenta financiera mediante el botón de proceso "Contabilizar" o ejecutando el proceso en segundo plano de contabilidad.
#### Estado del pago

Para comprender mejor la configuración del método de pago, también es necesario entender el **estado del pago** relacionado con los pasos del proceso.

Durante todo el ciclo de pagos, el pago se define por un estado para que el usuario conozca el último paso del proceso que tuvo lugar y el siguiente paso que debería tener lugar.

En la siguiente explicación y en el diagrama inferior, se explican los diferentes estados del pago.

-   **Pendiente de pago:** Este estado aparece cuando se ha creado una entrega/pago en la ventana de cobros o en la ventana de pagos, pero no tiene detalles de lo que se va a cobrar o pagar.
-   **Pendiente de ejecución:** Este estado aparece cuando se ha creado y procesado la entrega/pago y existe un proceso de ejecución automatizado pendiente de ejecutar.  
    Este es un estado *opcional* que se omitirá si:
    -   el método de pago es Manual
    -   o si el método de pago es Automático y no está configurado como "En espera".
-   **Pago cobrado/realizado:** Este estado aparece cuando la entrega/pago se ha completado y procesado.
-   **Depositado/retirado no conciliado:** Este estado aparece cuando la entrega/pago se ha añadido a la pantalla de cuenta financiera; por lo tanto, se ha creado la transacción de depósito/reintegro correspondiente en la cuenta financiera.
-   **Pago conciliado:** Este estado aparece cuando se ha ejecutado la conciliación del depósito/reintegro.

![](../../../../../assets/drive/1Ol1gtQAffG_S_bYKW6zAKbUK-Ez2qNRX.png)


Con más detalle, la forma en que esos estados del pago cambian dentro del ciclo de pagos de cobros y pagos es:

1\. La **Entrega** del dinero de entrada o el **Pago** del dinero de salida, antes de que la transacción se confirme en la cuenta bancaria, cambia el estado del pago a:

-   **Pendiente de ejecución**, si existe un proceso de ejecución configurado en el método de pago utilizado para la cuenta financiera
-   o **Pago cobrado** en el caso de una entrega de dinero de entrada
-   o **Pago realizado** en el caso de un pago de dinero de salida.

Si existe un proceso de ejecución configurado en el método de pago, la acción adicional de ejecutar ese proceso cambia el estado de "Pendiente de ejecución" a "Pago cobrado" o "Pago realizado".

2\. El **Depósito** del pago en la cuenta financiera cambia el estado del pago de **"Pago cobrado"** a **"Depositado no conciliado"**

y el **Reintegro** del pago desde la cuenta financiera cambia el estado del pago de **"Pago realizado"** a **"Retirado no conciliado"**.

3\. La **Compensación** o conciliación de los pagos cambia el estado del pago de **"Depositado no conciliado"** o **"Retirado no conciliado"** a **"Pago conciliado"**.
#### Método de pago

La imagen siguiente muestra la ventana **Método de pago**. Esta es la ventana donde se configuran los métodos de pago.

Sin embargo, los métodos de pago se asignan a las cuentas financieras; por lo tanto, también se puede definir una configuración diferente de un método de pago determinado en la solapa de método de pago de la ventana de cuenta financiera.

![](../../../../../assets/drive/10h0Lmw3yZ6rITkSq7q4nijmHlH_6jg5-.png)

Como consecuencia, el mismo método de pago puede tener diferentes **Versión** de configuración en función de la cuenta financiera a la que se haya asignado.

Es muy importante remarcar que:

-   la **configuración de un método de pago creada en una cuenta financiera sobrescribe la configuración "genérica" de ese método de pago** al gestionar pagos asociados a ese método de pago en esa cuenta financiera.
-   además, **los métodos de pago que se pueden utilizar**:
    -   por ejemplo, al emitir una factura de ventas
    -   o al asignar un método de pago por defecto a un proveedor

**son aquellos que ya están asignados a una cuenta financiera**.

En otras palabras, no es posible utilizar un método de pago si no está asignado a una cuenta financiera.

Por último, si es necesario revisar el método de pago asignado a un tercero, los pasos a seguir son:

-   navegar a la cuenta financiera asignada a ese tercero, si existe
-   y después a la solapa de método de pago de la cuenta financiera.

La configuración del **Método de pago** incluye las siguientes funcionalidades:

-   si se va a utilizar para **recibir cobros** y/o **realizar pagos**
-   si implica una **ejecución manual**, por ejemplo "Efectivo", o una **ejecución automática**, por ejemplo "Comprobación"
-   si va a **crear automáticamente el registro de la transferencia de dinero** antes de que la transacción se confirme en nuestra cuenta bancaria o caja.
    -   esto es una "**Entrega**" en caso de recibir un cobro
    -   esto es un "**Pago**" en caso de realizar un pago
-   si va a **añadir automáticamente la transacción en la cuenta financiera** relacionada con el movimiento de dinero de entrada o salida de nuestra cuenta bancaria o caja.
    -   esto es un "**Depósito**" en caso de recibir un cobro
    -   esto es un "**Reintegro**" en caso de realizar un pago
-   si permite al usuario **recibir o realizar pagos en otras divisas** distintas de la divisa de la cuenta financiera
-   y, por último, cómo se va a **contabilizar** el pago.

!!! info
    Para obtener más información, visite la sección [Flujo de trabajo de contabilización de pagos](../../financial-management/receivables-and-payables/setup.md#accounting-payment-workflow).


Los **Método de pago** se pueden configurar como se explica a continuación en detalle:
#### **Configuración del Método de pago**

##### Configuración de Cobros:

-   **Permitido:** Si está marcado, el Método de pago está habilitado para recibir cobros.
-   **Cobro automático:** Si está marcado, al completar una Factura de Ventas el cobro se recibe automáticamente.  
    Para poder usar esta opción, el cliente correspondiente necesita tener una "Cuenta financiera" definida por defecto en la pestaña de cliente de la ventana Tercero. El motivo es:
    -   esta marca crea automáticamente una transacción de "Entrega" en la ventana Cobros. Un cobro requiere una cuenta financiera.
-   **Depósito automático en cuenta:** Si está marcado, al completar la Entrega el cobro se deposita automáticamente en la cuenta financiera.  
    Para poder usar esta opción, el cliente correspondiente necesita tener una "Cuenta financiera" definida por defecto en la pestaña de cliente de la ventana Tercero. El motivo es:
    -   esta marca crea automáticamente una transacción de "Depósito" en la pestaña de transacciones de la ventana de cuenta financiera. Un depósito requiere una cuenta financiera.
-   **Recibir cobros en otras divisas:** Si está marcado, es posible recibir cobros en divisas distintas de la divisa por defecto de la Cuenta financiera.
    -   Lo anterior significa que, por ejemplo, una factura de ventas en USD puede depositarse en una Cuenta financiera configurada en EUR. Para ello, los clientes correspondientes deben tener asignada una Tarifa de Ventas en USD. Las opciones son:
        -   Introducir un tipo de cambio determinado al crear el cobro en la ventana Factura de Ventas, usando el botón **Añadir pago**.
        -   Seleccionar tanto la divisa USD como un tipo de cambio determinado, al recibir manualmente el cobro en la ventana Cobros, o al crear manualmente el depósito del cobro en la pestaña de transacciones de la ventana Cuenta financiera, usando el botón **Añadir transacción** y después el botón **Añadir pago**.
-   **Tipo de Ejecución**. Hay cobros que pueden requerir o no un paso adicional para ejecutarse. Por tanto, existen dos tipos de ejecución:
    -   **Manual:** este es el tipo de ejecución por defecto, salvo que se cambie a "Automático". Este tipo implica la "Recepción" del cobro como un evento manual sin necesidad de ningún paso adicional del sistema. Por ejemplo, cobro en efectivo.
    -   **Automático:** si el tipo de ejecución se cambia a "Automático", Etendo permite al usuario elegir un "Proceso de Ejecución"; es decir, la "Recepción" del cobro requiere ejecutar un paso adicional, por ejemplo el registro de un "Número de cheque".  
        Hay tres procesos de ejecución disponibles:
        -   **Proceso de Ejecución Simple** - este proceso no requiere ninguna acción, ya que cambia automáticamente el estado del pago de Pendiente de ejecución a Cobro recibido.
        -   **Proceso simple de impresión de cheque** - este proceso muestra una ventana que permite al usuario introducir un número de cheque al procesar el cobro en la ventana Cobros, y cambia el estado del pago de Pendiente de ejecución a Pago realizado. El número de cheque introducido se guarda como el "Número de referencia" del Pago.
            -   En caso de que haya más de un pago y se introduzca un número de cheque determinado, el proceso guarda automáticamente tantos números de cheque consecutivos como pagos. Esos números también se guardan como "Número de referencia" de los Pagos.
        -   **Dejar como crédito** - este proceso utiliza la funcionalidad de Devolución de materiales, ya que permite al usuario convertir un cobro/pago negativo en un crédito positivo para el tercero (cliente/proveedor).
    -   **En espera:**
        -   Si no está marcado, el pago, una vez procesado, también se ejecuta automáticamente. Esto aplica al "Proceso de Ejecución Simple", donde no se requiere ninguna acción adicional.
        -   Si está marcado, el pago se procesa pero no se ejecuta. Debe ejecutarse manualmente una vez que el pago obtenga el estado de pago "Pendiente de ejecución" en la ventana Cobros, usando el botón "Ejecutar pago". Esto aplica al "Proceso simple de impresión de cheque", donde, por ejemplo, es necesario introducir un número de cheque.
-   **Cuenta del cobro:** Cuenta que se utilizará para contabilizar la Entrega del cobro.
    -   Normalmente se dejaría en blanco si la transacción financiera se va a crear más adelante en el flujo de trabajo o si no se requiere ninguna contabilización en esta etapa del ciclo; en caso contrario, se puede asignar la "Cuenta de pagos en tránsito" para que:
        -   la Entrega del cobro se contabilice en la "Cuenta de pagos en tránsito" definida en la pestaña Configuración contable de la ventana de cuenta financiera.
-   **Cuenta de depósito:** Cuenta que se utilizará para contabilizar el Depósito del cobro.
    -   Normalmente se dejaría en blanco si no se requiere ninguna transacción financiera para el evento Depósito o si no se requiere ninguna contabilización en esta etapa; en caso contrario, se puede asignar la "Cuenta de pagos depositados" para que:
        -   el Depósito del cobro se contabilice en la "Cuenta de depósito" definida en la pestaña Configuración contable de la ventana de cuenta financiera.
-   **Cuenta de reconciliación:** Cuenta que se utilizará para contabilizar la Conciliación del cobro.
    -   Normalmente se configuraría como la "Cuenta de reconciliación", pero podría dejarse en blanco si la Entrega del cobro o si el Depósito del cobro ya se han contabilizado anteriormente en el proceso. Si se configura como "Cuenta de reconciliación":
        -   la Conciliación del cobro se contabiliza en la "Cuenta de reconciliación" definida en la pestaña Configuración contable de la ventana de cuenta financiera.

##### Configuración de Pagos:

-   **Permitido:** Si está marcado, el Método de pago está habilitado para realizar pagos.
-   **Pago Automático:** Si está marcado, al completar una Factura de Compra el pago se recibe automáticamente.  
    Para poder usar esta opción, el proveedor correspondiente necesita tener una "Cuenta financiera" definida por defecto en la pestaña de proveedor de la ventana Tercero. El motivo es:
    -   esta marca crea automáticamente una transacción de "Pago" en la ventana Pagos. Un pago requiere una cuenta financiera.
-   **Reintegro automático en cuenta:** Si está marcado, al completar el pago, el pago se retira automáticamente de la cuenta financiera.  
    Para poder usar esta opción, el proveedor correspondiente necesita tener una "Cuenta financiera" definida por defecto en la pestaña de proveedor de la ventana Tercero. El motivo es:
    -   esta marca crea automáticamente una transacción de "Reintegro" en la pestaña de transacciones de la ventana de cuenta financiera. Un reintegro requiere una cuenta financiera.
-   **Permitir pagos en otras divisas:** Si está marcado, es posible realizar pagos en divisas distintas de la divisa por defecto de la Cuenta financiera.
    -   La información anterior significa que, por ejemplo, una factura de compra en USD puede retirarse en una Cuenta financiera configurada en EUROS. Para poder usar esta opción, el proveedor correspondiente necesita tener asignada una Tarifa de Compra en USD.
    -   Será posible introducir un tipo de cambio determinado al crear el pago en la ventana Factura de Compra, usando el botón "Añadir pago".
    -   Será posible seleccionar tanto la divisa USD como un tipo de cambio determinado, al realizar "manualmente" el pago en la ventana Pagos, o al crear "manualmente" el reintegro del pago en la pestaña de transacciones de la ventana de cuenta financiera, usando el botón "Añadir transacción" y después el botón "Añadir pago".
-   **Tipo de Ejecución**. Igual que lo anterior, pero para los pagos realizados.
-   **Cuenta de pago:** Cuenta que se utilizará para contabilizar el pago.
    -   Normalmente se dejaría en blanco si la transacción financiera se va a crear más adelante en el flujo de trabajo o si no se requiere ninguna contabilización en esta etapa del ciclo; en caso contrario, se puede asignar la "Cuenta de pagos en tránsito" para que:
        -   el pago se contabilice en la "Cuenta de pagos en tránsito (Pagos)" definida en la pestaña Configuración contable de la ventana de cuenta financiera.
-   **Cuenta del reintegro:** Cuenta que se utilizará para contabilizar el Reintegro del pago.
    -   Normalmente se dejaría en blanco si no se requiere ninguna transacción financiera para el evento Reintegro o si no se requiere ninguna contabilización en esta etapa; en caso contrario, se puede asignar la "Cuenta de pagos retirados" para que:
        -   el Reintegro del pago se contabilice en la "Cuenta de reintegro" definida en la pestaña Configuración contable de la ventana de cuenta financiera.
-   **Cuenta de reconciliación:** Cuenta que se utilizará para contabilizar la Conciliación del pago.
    -   Normalmente se configuraría como la "Cuenta de reconciliación", pero podría dejarse en blanco si el pago o si el reintegro ya se han contabilizado anteriormente en el proceso. Si se configura como "Cuenta de reconciliación":
        -   la Conciliación del pago se contabiliza en la "Cuenta de reconciliación" definida en la pestaña Configuración contable de la ventana de cuenta financiera.

Una de las funcionalidades clave que permite la configuración del método de pago es que dos de las tres etapas del ciclo de pago pueden automatizarse:

![](../../../../../assets/drive/1V8vW4qdKyJxH9BGNX5xWZaRmXNJvbSkr.png)

Tal y como se muestra en la imagen anterior, si se seleccionan **Cobro automático/Pago Automático y Depósito automático en cuenta/Reintegro automático en cuenta**, las acciones manuales a ejecutar son:

-   la creación y contabilización de la factura de ventas/compra
-   la conciliación del cobro/pago en la cuenta financiera

porque tanto las transacciones de Cobros/Pagos como las de Depósito/Reintegro se crean automáticamente.

Si **NO** se seleccionan **Cobro automático/Pago Automático y Depósito automático en cuenta/Reintegro automático en cuenta**, las acciones manuales a ejecutar son:

-   la creación y contabilización de la factura de ventas/compra
-   la creación del Cobro/Pago
-   y la creación de la transacción de Depósito/Reintegro en la cuenta financiera, salvo que se seleccionen las acciones "Procesar pago(s) realizado(s) y reintegro" o "Procesar cobro(s) recibido(s) y depósito" al procesar el pago.

##### **Flujo de trabajo de contabilización de pagos**

Etendo permite un proceso flexible de contabilización de pagos; esto significa que un pago asociado a un método de pago determinado puede contabilizarse o no en cualquiera de sus etapas del Ciclo de pago.

Tal y como ya se ha descrito, un cobro recibido de un cliente pasa por las siguientes etapas:

-   Paso 1 - la "Entrega" del cobro
-   Paso 2 - el "Depósito" de la Entrega en la Cuenta financiera
-   Paso 3 - y, por último, la "Conciliación" del Depósito una vez que se ha recibido el extracto bancario.

Una situación análoga ocurre al realizar un pago a un proveedor:

-   Paso 1 - el "Pago"
-   Paso 2 - el "Reintegro" del pago desde la Cuenta financiera
-   Paso 3 - y, por último, la "Conciliación" del Reintegro una vez que se ha recibido el extracto bancario.

![](../../../../../assets/drive/1dugshR9aHhF3ahlQd03ILe6xTAPKVg0a.png)

Para cada paso, es posible especificar la cuenta por defecto para los ciclos de cobros y pagos de forma independiente.

Cada cuenta financiera necesita tener al menos una cuenta por defecto tanto para el ciclo de cobros como para el ciclo de pagos, ya sea en el paso 1, en el paso 2 o en el paso 3.

Tanto en el lado de pagos como en el de cobros, el primer paso que contiene una cuenta representa el momento en el que se cancelan la deuda con el proveedor o los derechos de cobro del cliente.

Por ejemplo, si la Cuenta de cobro está vacía y usted especifica una Cuenta de depósito, los derechos de cobro del cliente se cancelan en el momento del depósito, no en el momento del registro del cobro.

Cualquier paso posterior que tenga una cuenta compensará la cuenta del paso anterior con la cuenta de ese paso para representar la disminución del riesgo.

En otras palabras, cada una de las etapas puede contabilizarse en las ventanas/pestañas donde se crean si existe un valor definido en los campos "Cuenta de ...".

Por ejemplo:

-   si para un método de pago se selecciona el valor "**Cuenta de pagos en tránsito**" en el campo "**Cuenta del cobro**", eso significa que:
    -   la Entrega del cobro puede contabilizarse en la ventana Cobros usando el botón de proceso "Contabilizar".
    -   el derecho de cobro del cliente se va a cancelar contra la "**Cuenta de pagos en tránsito**" definida en la pestaña Configuración contable de la ventana de cuenta financiera.
-   si para un método de pago se selecciona el valor "**Cuenta de pagos depositados**" en el campo "**Cuenta de depósito**", eso significa que:
    -   el Depósito del cobro puede contabilizarse en la pestaña de transacciones de la ventana de cuenta financiera usando el botón de proceso "Contabilizar".
    -   la Entrega del cobro se va a cancelar contra la "**Cuenta de depósito**" definida en la pestaña Configuración contable de la ventana de cuenta financiera.
-   si para un método de pago se selecciona el valor "**Cuenta de reconciliación**" en el campo "**Cuenta de reconciliación**"
    -   eso significa que la conciliación del depósito puede contabilizarse en la pestaña Conciliación de la ventana de cuenta financiera usando el botón de proceso "Contabilizar".
    -   el Depósito del cobro se va a cancelar contra la "**Cuenta de reconciliación**" definida en la pestaña Configuración contable de la ventana de cuenta financiera.

!!! note
    Si alguna cuenta se deja vacía, implica que el botón de proceso "Contabilizar" se muestra como "Contabilizar: Deshabilitado para contabilidad" en la ventana correspondiente.
## Algoritmo de Reconciliación

:material-menu: `Aplicación` > `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Configuración` > `Algoritmo de Reconciliación`

### Visión general

Etendo permite al usuario conciliar las transacciones de depósito y reintegro de una cuenta financiera de dos maneras:

1.  **Automáticamente** asociando las líneas del extracto bancario (importadas o no) con las transacciones de la cuenta financiera.  
    En este caso, es necesario un algoritmo de reconciliación para dirigir el proceso de asociación.
2.  **Manualmente** utilizando el botón de proceso Conciliar de la ventana de cuenta financiera.  
    Esta forma de conciliación no requiere un algoritmo de reconciliación.

Etendo entrega de serie el algoritmo de reconciliación "**Estándar**", que puede encontrarse y configurarse en la ventana **Algoritmo de Reconciliación**.

#### Algoritmo de Reconciliación

La ventana de algoritmo de reconciliación lista y permite al usuario configurar el/los algoritmo/s a utilizar al asociar las líneas del extracto bancario con las transacciones de la cuenta financiera.

Tal y como se muestra en la imagen anterior, el algoritmo de reconciliación "**Estándar**" tiene tres casillas de verificación que permiten al usuario configurar el proceso de asociación de transacciones de la cuenta financiera:

-   **Asociar nombre del tercero:** esta opción obtiene una asociación fuerte si el nombre del tercero de la línea del extracto bancario coincide con el nombre del tercero de la transacción de la cuenta financiera.
-   **Asociar referencia:** esta opción obtiene una asociación fuerte si la referencia de la línea del extracto bancario coincide con la referencia de la transacción de la cuenta financiera.
-   **Asociar fecha de transacción:** esta opción obtiene una asociación fuerte si el nombre del tercero de la línea del extracto bancario coincide con el nombre del tercero de la transacción de la cuenta financiera.

!!! info
    Es posible seleccionar todas las comprobaciones anteriores a la vez o solo algunas de ellas para configurar cómo obtener una asociación fuerte.
## Formato Fichero Banco

:material-menu: `Aplicación` > `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Configuración` > `Formato Fichero Banco`

### Visión general

Etendo permite al usuario importar un fichero de extracto bancario a la cuenta financiera de una organización si se ha configurado un formato de fichero bancario para la organización.

Etendo proporciona algunos módulos que, una vez instalados, permiten al usuario importar ficheros de extracto bancario en Etendo en diferentes formatos:

-   Formato de extracto bancario OFX
-   Importador genérico de extracto bancario CSV
-   Importador CSV de WePay
-   y el español Cuaderno 43

Una vez que se importa un fichero de extracto bancario a la cuenta financiera de una organización:

-   la información general, como el nombre del fichero y la fecha de importación, se guarda en la solapa Extractos bancarios importados de la cuenta financiera
-   y el contenido del fichero de extracto bancario se guarda línea a línea en la solapa correspondiente Líneas de extracto bancario.

#### Formato Fichero Banco

La ventana Formato Fichero Banco lista los módulos de formato de fichero bancario instalados para una organización.

![Formato Fichero Banco](../../../../../assets/drive/1m1UirW3EvMahtJQK5imtme5TZTf-Iy9w.png)

Tal y como se muestra en la imagen anterior, un formato de fichero bancario puede aplicarse a la organización en la ventana Gestión de Módulos de Empresa después de ser instalado; por lo tanto, está disponible para cualquier organización del cliente.

#### Excepciones
Se pueden añadir excepciones a un formato de importación de fichero bancario; por lo tanto, no se tienen en cuenta en el proceso de importación.  
Es posible definir el texto a excluir al asociar transacciones y líneas de extracto bancario en una cuenta financiera determinada o en todas ellas.
## Proceso de Ejecución

:material-menu: `Aplicación` > `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Configuración` > `Proceso de Ejecución`

### Visión general

Algunos tipos de pago requieren que se ejecute una actividad adicional al completar el pago.

Por ejemplo, un pago con cheque puede requerir el registro del número de cheque y la impresión del cheque.

En general, el proceso de ejecución es una definición de la(s) **actividad(es)** que el sistema o el usuario debe ejecutar para que un pago quede finalmente registrado como:

-   **realizado/retirado de la cuenta financiera**
-   o **recibido/depositado en la cuenta financiera**.

#### Proceso

La ventana de proceso de ejecución lista los procesos de ejecución disponibles.

Etendo entrega por defecto los procesos de ejecución descritos a continuación:

-   **Proceso de Ejecución Simple** - este proceso ejecuta una actividad del sistema que cambia el estado del pago de "Pendiente de ejecución" a "Pago recibido"/"Pago realizado" (o "Depositado no conciliado"/"Retirado no conciliado")
-   **Proceso simple de impresión de cheque** - este proceso abre una ventana que permite al usuario introducir un número de cheque mientras procesa el pago.
-   **Dejar como crédito** - este proceso utiliza la funcionalidad de Devolución de materiales, ya que permite al usuario cambiar un cobro/pago negativo a un crédito positivo para el tercero (cliente/proveedor).

Los pagos que requieren que se ejecute una actividad independiente deben configurarse para que funcionen; esto implica la selección de la opción "**Automático**" en el campo "**Proceso de Ejecución**". Por lo tanto, se puede seleccionar un proceso de ejecución de los listados anteriormente al configurar el método de pago.

#### Parámetro

La solapa Parámetro permite al usuario configurar la actividad adicional a ejecutar al completar un pago. Por ejemplo, para registrar un número de cheque.

![Solapa Parámetro](../../../../../assets/drive/17seAr4S-i9aqgCgpcrr01lDo4hXD22Rn.png)

Tal y como se muestra en la imagen anterior, el "**Proceso simple de impresión de cheque**" tiene un parámetro llamado "**Número de cheque**". Ese parámetro es de tipo "**Entrada**" en el "**Tipo de Parámetro**", cuyo "**Tipo de Entrada**" es "**Texto**".

La configuración anterior significa que el número de cheque debe ser introducido por el usuario como texto.

Un **tipo de parámetro "Entrada"** también puede ser una casilla de verificación; por lo tanto, en lugar de introducir un texto, el usuario debe seleccionar o no una casilla de verificación. También es posible definir si el valor por defecto de la casilla de verificación va a ser "Sí" o "No".

Además, los tipos de parámetro también pueden ser una "**Constante**"; por lo tanto, se puede especificar el "**Texto por Defecto**" de la constante.

!!! info
    El registro de valores para cualquiera de los tipos de parámetro definidos anteriormente se guarda en la solapa Parámetro de la ejecución de pago correspondiente.
## Tipo remesas 

:material-menu: `Aplicación` > `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Configuración` > `Tipo remesas`

Para configurar el método de pago de remesas es necesario ejecutar previamente un conjunto de datos que haya creado este método de pago y el proceso de ejecución. 

!!! info
    El campo "En espera" siempre debe estar marcado para los métodos de pago que se apliquen a remesas.

![](../../../../../assets/drive/1Qe3mdTduM3wJctZkC3N8z-yLRL_Gq6Y_.png)

!!! info
    No se definirá contabilidad para ninguna de las transacciones asociadas al método de pago de remesas, de forma que no se genere una doble contabilización. La contabilidad de remesas se configura desde la ventana de tipos de remesas.


El siguiente paso es la configuración del tipo de remesa y la asignación de las cuentas contables para su contabilización.
Es posible crear tantos tipos de remesas como cuentas financieras disponibles, de forma que se puedan asignar las cuentas contables adecuadas a cada una de ellas. 

Se definen las siguientes cuentas:<br>
**Cuenta de envío:** la cuenta que se utilizará en la contabilización de la remesa.<br>
**Cuenta de liquidación:** cuenta que se utilizará para la contabilización de la liquidación de la remesa, que hace referencia al importe que ha sido cobrado o pagado.

![](../../../../../assets/drive/1fUwM5P-aNQOSlIm1u_mYfDAdQzbPO6ur.png)

Para finalizar el proceso, se deben asociar los métodos de pago aplicables a cada cuenta financiera. 

!!! info
    Es importante que aquellos bancos desde los que se vayan a realizar transacciones de remesas tengan un tercero asociado.

![](../../../../../assets/drive/1lNuqadYEmnZeOl8RcS3hXS_2-N7GrVfg.png)


### Remesas sin descuento
Para configurar remesas sin descuento, defina este método de pago desde la ventana Método de pago.  

![](../../../../../assets/drive/11mLuoH5qVVh_8tjnepUL12O6oaOkIoY2.png)


![](../../../../../assets/drive/1Y0pJr2nUKDJEYbp85_a75ifAKQ70IIqO.png)

!!! info
    Para crear una remesa sin descuento, vaya a la [ventana Remesas](../../financial-management/receivables-and-payables/transactions.md#remittance). 

### Remesar para descuento

Para configurar remesas para descuento, defina el tipo desde la casilla de verificación Remesar para descuento, tal y como se muestra en la siguiente imagen: 

![](../../../../../assets/drive/1xW3siKWbirKqZAazQzIoLoPcGMknNwjk.png)



![](../../../../../assets/drive/12vjozrcXO3zaa1j9_e0P9xj3TD9kJ-FI.png)

!!! info
    Para crear una remesa para descuento, vaya a la [ventana Remesas](../../financial-management/receivables-and-payables/transactions.md#remittance).
## Método de dudoso cobro

:material-menu: `Aplicación` > `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Configuración` > `Método de dudoso cobro`

### Visión general

A través de esta ventana, es posible definir un Método de dudoso cobro, que estará disponible para utilizarse como plantilla al crear una nueva ejecución de dudoso cobro.

#### Método de dudoso cobro

![Método de dudoso cobro](../../../../../assets/drive/1aJifeptvA2B8lIiaFEBtvNIbXUcJpRxO.png)

Campos a tener en cuenta:

-   **Días Retraso:** este campo se utiliza como filtro al seleccionar las deudas existentes. Puede eliminarse posteriormente.
-   **Porcentaje:** este campo se utiliza al seleccionar las deudas existentes como el porcentaje por defecto de la deuda que se va a considerar como de dudoso cobro. Puede modificarse posteriormente.

---
Este trabajo es una obra derivada de [Gestión Financiera](http://wiki.openbravo.com/wiki/Financial_Management){target="_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="_blank"} por [Etendo](https://etendo.software){target="_blank"}.