---
tags:
  - Etendo Classic
  - Financial Management
  - Payment Method
  - Payment Cycle
  - Receivables and Payables
---

# Método de Pago

:material-menu: `Application` > `Financial Management` > `Receivables and Payables` > `Setup` > `Payment Method`

## Descripción general

Los **Métodos de Pago** representan los medios de pago utilizados por la empresa o por un tercero, tales como:

-   Efectivo
-   Tarjeta de crédito
-   PayPal
-   Cheque
-   Domiciliación bancaria
-   Orden permanente
-   Transferencia bancaria
-   Pagaré

Cada **transacción de pago** está asociada a un **Método de Pago**. Un método de pago define cómo se gestionará un cobro/pago dentro del ciclo de pago de cobros y pagos, y además cómo se contabilizará.

Los **Métodos de Pago** están asociados a Cuentas Financieras, de modo que los pagos pueden registrarse en un banco o libro de caja.

Los métodos de pago que pueden utilizarse dentro de la gestión de cobros y pagos son los asignados a una Cuenta Financiera; por lo tanto, si es necesario modificar la configuración de algún método de pago, debe hacerse en la pestaña Método de Pago de la cuenta financiera.

Es posible asociar múltiples **Métodos de Pago** a una única Cuenta Financiera.

Por ejemplo, tanto los pagos con cheque como los pagos electrónicos pueden asociarse a una única Cuenta Financiera, ya que cada método de pago tiene su propia configuración.

## Ciclo de Pago

Para comprender mejor la configuración de un **Método de Pago**, es necesario entender el flujo de eventos dentro del ciclo de pago:

-   **Pedido:** el pedido de venta o el pedido de compra se utiliza en este proceso de gestión de cobros y pagos en el caso de un pago anticipado:
    -   cuando se contabiliza la factura de venta o de compra, se puede generar la información de pago del pedido desde la ventana Cobros o desde la ventana Pagos.
-   **Factura:** la factura de compra genera una deuda con el proveedor y la factura de venta un derecho de cobro sobre el cliente.
-   **Cobro o Pago:** el registro de la transferencia de dinero entrante o saliente antes de que la transacción sea confirmada en la cuenta bancaria o libro de caja.
-   **Actualización de la Cuenta Financiera:** la incorporación de la transacción en la Cuenta Financiera como un "Depósito" o como una "Retirada", relacionada con el movimiento del dinero entrante o saliente de la cuenta bancaria o libro de caja.
-   **Conciliación:** la confirmación del movimiento de dinero tras recibir el extracto bancario o el saldo de caja.

En la imagen a continuación se muestra un Flujo de Pago Simple:

![](../../../../../assets/drive/1MwU8f0EaeyCjJveISM3RGAnFAfSHfq4N.png)


A continuación se describe la forma de crear cada etapa de pago en Etendo:

**Primera etapa:**

Un "**Cobro**" puede registrarse en:

-   la ventana Factura (Cliente) utilizando el botón de proceso "Añadir pago".
-   y en la ventana Cobros utilizando el botón de proceso "Añadir detalles".

Un "**Pago**" puede registrarse en:

-   la ventana Factura (Proveedor) utilizando el botón de proceso "Añadir pago".
-   y en la ventana Pagos utilizando el botón de proceso "Añadir detalles".

Las etapas de pago anteriores pueden generar un **evento contable** según la configuración contable del método de pago.

-   Si está configurado para contabilizar en esta etapa, los Cobros y Pagos pueden contabilizarse en la ventana Cobros / Pagos utilizando el botón de proceso "Contabilizar" o ejecutando el proceso de contabilización en segundo plano.

**Segunda etapa:**

Un "**Depósito**" puede registrarse en:

-   la Cuenta Financiera utilizando el botón de proceso "Añadir transacción".
-   y en la ventana Cobros utilizando el botón de proceso "Añadir detalles" y luego la acción: "Procesar cobro(s) recibido(s) y depositar"

Una "**Retirada**" puede registrarse en:

-   la Cuenta Financiera utilizando el botón de proceso "Añadir transacción".
-   y en la ventana Pagos utilizando el botón de proceso "Añadir detalles" y luego la acción: "Procesar pago(s) realizado(s) y retirar"

Las etapas de pago anteriores pueden generar un **evento contable** según la configuración contable del método de pago.

-   Si está configurado para contabilizar en esta etapa, los Depósitos y Retiradas pueden contabilizarse en la ventana Cuenta Financiera utilizando el botón de proceso "Contabilizar" o ejecutando el proceso de contabilización en segundo plano.

**Tercera y última etapa:**

Una "**Conciliación**" puede registrarse en:

-   la pestaña Conciliación de la ventana Cuenta Financiera.

La etapa de pago anterior puede generar un **evento contable** según la configuración contable del método de pago.

-   Si está configurado para contabilizar en esta etapa, las Conciliaciones pueden contabilizarse en la pestaña Conciliación de la ventana Cuenta Financiera utilizando el botón de proceso "Contabilizar" o ejecutando el proceso de contabilización en segundo plano.

## Estado del Pago

Para comprender mejor la configuración del método de pago, también es necesario entender el **estado del pago** relacionado con los pasos del proceso.

Durante todo el Ciclo de Pago, el pago se define mediante un estado para que el usuario conozca el último paso del proceso que tuvo lugar y el siguiente que debe realizarse.

En la siguiente explicación y diagrama, se describen los diferentes Estados del Pago.

-   **En espera de pago:** Este estado aparece cuando se ha creado un Cobro/Pago en la ventana Cobros o en la ventana Pagos, pero no tiene detalles sobre lo que se va a cobrar o pagar.
-   **En espera de ejecución:** Este estado aparece cuando el Cobro/Pago ha sido creado y procesado y hay un proceso de ejecución automático pendiente de ejecutarse.  
    Este es un estado *opcional* que se omitirá si:
    -   el Método de Pago es Manual
    -   o si el Método de Pago es Automático y no está configurado como "Diferido".
-   **Cobro recibido/Pago realizado:** Este estado aparece cuando el Cobro/Pago ha sido completado y procesado.
-   **Depositado/Retirado sin confirmar:** Este estado aparece cuando el Cobro/Pago ha sido añadido a la pantalla de Cuenta Financiera, por lo que la transacción de Depósito/Retirada correspondiente ha sido creada en la Cuenta Financiera.
-   **Pago confirmado:** Este estado aparece cuando se ha ejecutado la conciliación del Depósito/Retirada.

![](../../../../../assets/drive/1Ol1gtQAffG_S_bYKW6zAKbUK-Ez2qNRX.png)


Con más detalle, la forma en que cambian esos estados de pago dentro del ciclo de pago de cobros y pagos es:

1\. El **Cobro** del dinero entrante o el **Pago** del dinero saliente, antes de que la transacción sea confirmada en la cuenta bancaria, cambia el estado del pago a:

-   **En espera de ejecución**, si hay un proceso de ejecución configurado en el método de pago utilizado para la cuenta financiera
-   o **Cobro recibido** en el caso de un cobro de dinero entrante
-   o **Pago realizado** en el caso de un pago de dinero saliente.

Si hay un proceso de ejecución configurado en el método de pago, la acción adicional de ejecutar dicho proceso cambia el estado de "En espera de ejecución" a "Cobro recibido" o "Pago realizado".

2\. El **Depósito** del pago en la cuenta financiera cambia el estado del pago de **"Cobro recibido"** a **"Depositado sin confirmar"**

y la **Retirada** del pago de la cuenta financiera cambia el estado del pago de **"Pago realizado"** a **"Retirado sin confirmar"**.

3\. La **Confirmación** o conciliación de los pagos cambia el estado del pago de **"Depositado sin confirmar"** o **"Retirado sin confirmar"** a **"Pago confirmado"**

## Método de Pago

La imagen a continuación muestra la ventana Método de Pago. Esta es la ventana donde se configuran los métodos de pago.

Sin embargo, los métodos de pago se asignan a cuentas financieras; por lo tanto, también se puede definir una configuración diferente de un método de pago determinado en la pestaña de método de pago de la ventana de cuenta financiera.

![](../../../../../assets/drive/10h0Lmw3yZ6rITkSq7q4nijmHlH_6jg5-.png)

Como consecuencia, el mismo método de pago puede tener diferentes "versiones" de configuración según la cuenta financiera a la que haya sido asignado.

Es muy importante destacar que:

-   la **configuración de un método de pago creado en una cuenta financiera reemplaza la configuración "genérica" de dicho método de pago** al gestionar los pagos asociados a ese método de pago en esa cuenta financiera.
-   más aún, **los métodos de pago que pueden utilizarse**:
    -   al emitir una factura de venta, por ejemplo
    -   o al asignar un método de pago predeterminado a un proveedor

**son los que ya están asignados a una cuenta financiera**.

En otras palabras, no es posible utilizar un método de pago si no está asignado a una cuenta financiera.

Finalmente, si es necesario revisar el método de pago asignado a un tercero, los pasos a seguir son:

-   navegar a la cuenta financiera asignada a dicho tercero, si existe
-   y luego a la pestaña de método de pago de la cuenta financiera.

La configuración del Método de Pago incluye las siguientes características:

-   si se va a utilizar para **recibir cobros** y/o **realizar pagos**
-   si implica una **ejecución manual**, por ejemplo "Efectivo" o una **ejecución automática**, por ejemplo "Cheque"
-   si va a **crear automáticamente el registro de la transferencia de dinero** antes de que la transacción sea confirmada en la cuenta bancaria o libro de caja.
    -   eso es un "**Cobro**" en caso de recibir un pago
    -   eso es un "**Pago**" en caso de realizar un pago
-   si va a **añadir automáticamente la transacción en la cuenta financiera** relacionada con el movimiento del dinero entrante o saliente de la cuenta bancaria o libro de caja.
    -   eso es un "**Depósito**" en caso de recibir un pago
    -   eso es una "**Retirada**" en caso de realizar un pago
-   si permite al usuario **recibir o realizar pagos en otras divisas** distintas a la divisa de la cuenta financiera
-   y finalmente, cómo se va a **contabilizar** el pago.

!!! info
    Para más información, consulte la sección [Flujo contable de pagos](#flujo-contable-de-pagos).


Los Métodos de Pago pueden configurarse según se describe a continuación en detalle:

## Configuración del Método de Pago

### Configuración de Cobros:

-   **Cobros permitidos:** Si está marcado, el Método de Pago está habilitado para recibir cobros.
-   **Cobro automático:** Si está marcado, al completar una Factura (Cliente) el pago se recibe automáticamente.  
    Para utilizar esta opción, el cliente correspondiente debe tener una "Cuenta Financiera" definida por defecto en la pestaña de cliente de la ventana Tercero. El motivo es:
    -   esta opción crea automáticamente una transacción de "Cobro" en la ventana Cobros. Un cobro requiere una cuenta financiera.
-   **Depósito automático:** Si está marcado, al completar el Cobro el pago se deposita automáticamente en la cuenta financiera.  
    Para utilizar esta opción, el cliente correspondiente debe tener una "Cuenta Financiera" definida por defecto en la pestaña de cliente de la ventana Tercero. El motivo es:
    -   esta opción crea automáticamente una transacción de "Depósito" en la pestaña de transacciones de la ventana de cuenta financiera. Un depósito requiere una cuenta financiera.
-   **Recibir cobros en múltiples divisas:** Si está marcado, es posible recibir cobros en otras divisas distintas a la divisa predeterminada de la Cuenta Financiera.
    -   Esto significa que, por ejemplo, una factura de venta en USD puede depositarse en una Cuenta Financiera configurada en EUR. Para ello, los clientes correspondientes deben tener asignada una Lista de Precios de Venta en USD. Las opciones son:
        -   Introducir un tipo de cambio determinado al crear el pago en la ventana Factura (Cliente), utilizando el botón **Añadir pago**.
        -   Seleccionar tanto la divisa USD como un tipo de cambio determinado, al recibir manualmente el cobro en la ventana Cobros, o al crear manualmente el depósito del pago en la pestaña de transacciones de la ventana Cuenta Financiera, utilizando el botón **Añadir transacción** y luego el botón **Añadir cobro/pago**.
-   **Tipo de ejecución**. Hay pagos que pueden o no requerir un paso adicional a ejecutar. Por lo tanto, existen dos tipos de ejecución:
    -   **Manual:** este es el tipo de ejecución predeterminado, a menos que se cambie a "Automático". Este tipo implica la "Recepción" del pago como un evento manual sin necesidad de ningún paso adicional del sistema. Por ejemplo, el pago en efectivo.
    -   **Automático:** si el tipo de ejecución se cambia a "Automático", Etendo permite al usuario elegir un "Proceso de Ejecución"; en otras palabras, la "Recepción" del pago requiere ejecutar un paso adicional, como por ejemplo el registro de un "Número de cheque".  
        Existen tres procesos de ejecución disponibles:
        -   **Simple Execution Process** - este proceso no requiere ninguna acción, ya que cambia automáticamente el estado del pago de En espera de ejecución a Cobro recibido.
        -   **Print Check simple process** - este proceso muestra una ventana que permite al usuario introducir un número de cheque durante el procesamiento del pago en la ventana Cobros, y cambia el estado del pago de En espera de ejecución a Pago realizado. El número de cheque introducido se guarda como "Número de referencia" del Pago.
            -   En caso de que haya más de un pago y se introduzca un número de cheque determinado, el proceso guarda automáticamente tantos números de cheque consecutivos como pagos haya. Esos números también se guardan como "Número de referencia" de los Pagos.
        -   **Leave as Credit** - este proceso utiliza la funcionalidad de Devolución de materiales y permite al usuario convertir un cobro/pago negativo en un crédito positivo para el tercero (cliente/proveedor).
    -   **Diferido:**
        -   Si no está marcado, el pago una vez procesado también se ejecuta automáticamente; esto aplica al "Simple Execution Process" donde no se necesita ninguna acción adicional.
        -   Si está marcado, el pago se procesa pero no se ejecuta. Debe ejecutarse manualmente una vez que el pago obtenga el Estado de Pago "En espera de ejecución" en la ventana Cobros utilizando el botón "Ejecutar pago". Esto aplica al "Print Check simple process" donde es necesario introducir un número de cheque, por ejemplo.
-   **Al recibir cobro usar:** Cuenta que se utilizará para contabilizar el Cobro del pago.
    -   Normalmente se dejará en blanco si la transacción financiera se va a crear más adelante en el flujo de trabajo o si no se requiere ningún asiento en esta etapa del ciclo; de lo contrario, se puede asignar la "Cuenta de tránsito del pago" para que:
        -   el Cobro del pago se contabilice en la "Cuenta de tránsito del cobro" definida en la pestaña Configuración contable de la ventana de cuenta financiera.
-   **Al depositar usar:** Cuenta que se utilizará para contabilizar el Depósito del pago.
    -   Normalmente se dejará en blanco si no se requiere transacción financiera para el evento de Depósito o si no se requiere ningún asiento en esta etapa; de lo contrario, se puede asignar la "Cuenta de pago depositado" para que:
        -   el Depósito del pago se contabilice en la "Cuenta de depósito" definida en la pestaña Configuración contable de la ventana de cuenta financiera.
-   **Al conciliar usar:** Cuenta que se utilizará para contabilizar la Conciliación del pago.
    -   Normalmente se establecerá en la "Cuenta de pago confirmado", pero podría dejarse en blanco si el Cobro del pago o el Depósito del pago ya se han contabilizado anteriormente en el proceso. Si se establece en "Cuenta de pago confirmado":
        -   la Conciliación del pago se contabiliza en la "Cuenta de pago confirmado" definida en la pestaña Configuración contable de la ventana de cuenta financiera.

### Configuración de Pagos:

-   **Pagos permitidos:** Si está marcado, el Método de Pago está habilitado para realizar pagos.
-   **Pago automático:** Si está marcado, al completar una Factura (Proveedor) el pago se recibe automáticamente.  
    Para utilizar esta opción, el proveedor correspondiente debe tener una "Cuenta Financiera" definida por defecto en la pestaña de proveedor de la ventana Tercero. El motivo es:
    -   esta opción crea automáticamente una transacción de "Pago" en la ventana Pagos. Un pago requiere una cuenta financiera.
-   **Retirada automática:** Si está marcado, al completar el pago, el pago se retira automáticamente de la cuenta financiera.  
    Para utilizar esta opción, el proveedor correspondiente debe tener una "Cuenta Financiera" definida por defecto en la pestaña de proveedor de la ventana Tercero. El motivo es:
    -   esta opción crea automáticamente una transacción de "Retirada" en la pestaña de transacciones de la ventana de cuenta financiera. Una retirada requiere una cuenta financiera.
-   **Realizar pagos en múltiples divisas:** Si está marcado, es posible realizar pagos en otras divisas distintas a la divisa predeterminada de la Cuenta Financiera.
    -   La información anterior significa que una factura de compra en USD puede retirarse en una Cuenta Financiera configurada en EUROS, por ejemplo. Para utilizar esta opción, el proveedor correspondiente debe tener asignada una Lista de Precios de Compra en USD.
    -   Será posible introducir un tipo de cambio determinado al crear el pago en la ventana Factura (Proveedor), utilizando el botón "Añadir pago".
    -   Será posible seleccionar tanto la divisa USD como un tipo de cambio determinado, al realizar "manualmente" el pago en la ventana Pagos, o al crear "manualmente" la retirada del pago en la pestaña de transacciones de la ventana de cuenta financiera, utilizando el botón "Añadir transacción" y luego el botón "Añadir cobro/pago".
-   **Tipo de ejecución**. Igual que el anterior pero para los pagos realizados.
-   **Al realizar pago usar:** Cuenta que se utilizará para contabilizar el pago.
    -   Normalmente se dejará en blanco si la transacción financiera se va a crear más adelante en el flujo de trabajo o si no se requiere ningún asiento en esta etapa del ciclo; de lo contrario, se puede asignar la "Cuenta de tránsito del pago" para que:
        -   el pago se contabilice en la "Cuenta de tránsito del pago (salida)" definida en la pestaña Configuración contable de la ventana de cuenta financiera.
-   **Al retirar usar:** Cuenta que se utilizará para contabilizar la Retirada del pago.
    -   Normalmente se dejará en blanco si no se requiere transacción financiera para el evento de Retirada o si no se requiere ningún asiento en esta etapa; de lo contrario, se puede asignar la "Cuenta de pago retirado" para que:
        -   la Retirada del pago se contabilice en la "Cuenta de retirada" definida en la pestaña Configuración contable de la ventana de cuenta financiera.
-   **Al conciliar usar:** Cuenta que se utilizará para contabilizar la Conciliación del pago.
    -   Normalmente se establecerá en la "Cuenta de pago confirmado", pero podría dejarse en blanco si el pago o la retirada ya se han contabilizado anteriormente en el proceso. Si se establece en "Cuenta de pago confirmado":
        -   la Conciliación del pago se contabiliza en la "Cuenta de pago confirmado" definida en la pestaña Configuración contable de la ventana de cuenta financiera.

Una de las características clave permitidas por la configuración del método de pago es lograr que dos de las tres etapas del ciclo de pago puedan automatizarse:


![](../../../../../assets/drive/1V8vW4qdKyJxH9BGNX5xWZaRmXNJvbSkr.png)


Como se muestra en la imagen anterior, si se seleccionan el **Cobro/Pago Automático y el Depósito/Retirada Automático**, las acciones manuales a ejecutar son:

-   la creación y contabilización de la factura de venta/compra
-   la conciliación del cobro/pago en la cuenta financiera

porque las transacciones de Cobro/Pago y Depósito/Retirada se crean automáticamente.

Si el **Cobro/Pago Automático y el Depósito/Retirada Automático NO están seleccionados**, las acciones manuales a ejecutar son:

-   la creación y contabilización de la factura de venta/compra
-   la creación del Cobro/Pago
-   y la creación de la transacción de Depósito/Retirada en la cuenta financiera, a menos que se seleccionen las acciones "Procesar pago(s) realizado(s) y retirar" o "Procesar cobro(s) recibido(s) y depositar" durante el procesamiento del pago.

## Flujo contable de pagos

Etendo permite un proceso de contabilización de pagos flexible; esto significa que un pago asociado a un método de pago determinado puede contabilizarse o no en cualquiera de sus etapas del Ciclo de Pago.

Como ya se ha descrito, un pago recibido de un cliente pasa por las siguientes etapas:

-   Paso 1 - el "Cobro" del pago
-   Paso 2 - el "Depósito" del Cobro en la Cuenta Financiera
-   Paso 3 - y finalmente la "Conciliación" del Depósito una vez recibido el extracto bancario.

Una situación análoga ocurre al realizar un pago a un proveedor:

-   Paso 1 - el "Pago"
-   Paso 2 - la "Retirada" del pago de la Cuenta Financiera
-   Paso 3 - y finalmente la "Conciliación" de la Retirada una vez recibido el extracto bancario.

![](../../../../../assets/drive/1dugshR9aHhF3ahlQd03ILe6xTAPKVg0a.png)

Para cada paso, es posible especificar la cuenta predeterminada para los ciclos de cobros y pagos de forma independiente.

Cada cuenta financiera debe tener al menos una cuenta predeterminada para el ciclo de cobros y el de pagos, ya sea en el paso 1, paso 2 o paso 3.

Tanto en el lado de los pagos como en el de los cobros, el primer paso que contenga una cuenta representa el momento en que se cancela la deuda con el proveedor o los derechos de cobro sobre el cliente.

Por ejemplo, si la Cuenta de cobro del pago está vacía y se especifica una Cuenta de depósito, los derechos de cobro sobre el cliente se cancelan en el momento del depósito, no en el momento del registro del cobro.

Cualquier paso posterior que tenga una cuenta compensará la cuenta del paso anterior con la cuenta de ese paso para representar la disminución del riesgo.

En otras palabras, cada una de las etapas puede contabilizarse en las ventanas/pestañas donde se crean si hay un valor definido en los campos "Al...usar".

Por ejemplo:

-   si para un método de pago se selecciona el valor "**Cuenta de tránsito del pago**" en el campo "**Al recibir cobro usar**", eso significa que:
    -   el cobro del pago puede contabilizarse en la ventana Cobros utilizando el botón de proceso "Contabilizar".
    -   los derechos de cobro sobre el cliente se cancelarán por la "**Cuenta de tránsito del cobro**" definida en la pestaña de configuración contable de la ventana de cuenta financiera.
-   si para un método de pago se selecciona el valor "**Cuenta de pago depositado**" en el campo "**Al depositar usar**", eso significa que:
    -   el depósito del pago puede contabilizarse en la pestaña Transacciones de la ventana de cuenta financiera utilizando el botón de proceso "Contabilizar".
    -   el cobro del pago se cancelará por la "**Cuenta de depósito**" definida en la pestaña de configuración contable de la ventana de cuenta financiera.
-   si para un método de pago se selecciona el valor "**Cuenta de pago confirmado**" en el campo "**Al conciliar usar**"
    -   eso significa que la conciliación del depósito puede contabilizarse en la pestaña Conciliación de la ventana de cuenta financiera utilizando el botón de proceso "Contabilizar".
    -   el depósito del pago se cancelará por la "**Cuenta de pago confirmado**" definida en la pestaña de configuración contable de la ventana de cuenta financiera.

!!! note
    Si cualquier cuenta se deja vacía, implica que el botón de proceso "Contabilizar" se muestra como "Contabilizar: Deshabilitado para contabilidad" en la ventana correspondiente.

---

This work is a derivative of [Financial Management](http://wiki.openbravo.com/wiki/Financial_Management){target="_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="_blank"} by [Etendo](https://etendo.software){target="_blank"}.
