---
tags:
    - Cómo hacer
    - Transferencias de fondos
    - Cuenta financiera
    - Transacciones bancarias
    - Gestión de tesorería
---

## Visión general

Existen muchas situaciones en las que una empresa necesita transferir fondos para modificar o ajustar el saldo de cuentas bancarias y/o de caja:


- un cheque ingresado en la cuenta bancaria equivocada
- una cuenta bancaria sin fondos...etc.

En Etendo, las cuentas bancarias y de caja se representan como [Cuenta financiera](../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#financial-account).

Existen varios tipos de transferencias de fondos en función del tipo de cuenta financiera utilizado y de la organización para la que se realiza la transferencia de fondos:

- De una cuenta bancaria a otra cuenta bancaria dentro de la misma organización.
- De una cuenta bancaria de una organización a una cuenta bancaria de otra organización.
- Lo mismo aplica a las cuentas de caja.

## Artículos recomendados

La transferencia de fondos entre cuentas financieras requiere una comprensión clara de cómo crear un [Concepto contable](../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup/gl-item.md).

También es muy recomendable comprender cómo funcionan en Etendo las [Cuenta financiera](../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#financial-account) y la [Combinación de cuentas](../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup/account-combination.md).

## Pasos de ejecución

En Etendo, la empresa del ejemplo deberá retirar dinero de una cuenta bancaria o de caja y depositarlo en otra cuenta bancaria o de caja.
En otras palabras, la empresa necesita modificar el saldo de las cuentas bancarias o de caja cuando sea necesario. Esa acción puede tener o no comisiones.
En cualquier caso, los pasos a seguir son:

- Creación del concepto contable
        ya que es necesario mantener en algún lugar el saldo de fondos en tránsito desde el momento en que se retira de una cuenta financiera hasta el momento en que se deposita en otra cuenta financiera.
- Creación de una transacción de retirada
        en la cuenta bancaria de la que se retiran los fondos.
- Creación de una transacción de depósito
        en la cuenta bancaria en la que se van a depositar los fondos.


## Creación del Concepto contable

Un [Concepto contable](../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup/gl-item.md) es el elemento contable que se utiliza para contabilizar fondos en tránsito. Es clave configurar el concepto contable con las cuentas de débito y crédito correctas en el campo Solapa contabilidad. La forma de hacerlo es:

- Una vez creado el concepto contable, haga clic en la *Solapa contabilidad* de la ventana [Concepto contable](../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup/gl-item.md).
- Cree un nuevo registro para el libro mayor de cada organización y asigne la misma [Combinación de cuentas](../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup/account-combination.md) para débito y crédito.

Por ejemplo, las combinaciones de cuentas de muestra que podrían utilizarse son:

- Configuración del libro mayor de EE. UU.:
        1140 Checking In-Transfer
- Configuración del libro mayor español:
        55500 - Partidas pendientes de aplicación

## Creación de la transacción de retirada

Debe crearse una transacción de retirada en la Cuenta financiera de la que se van a retirar los fondos. Este paso del proceso puede tener o no comisiones.

La empresa de este ejemplo necesita:

- navegar a la ventana [Cuenta financiera](../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#financial-account)
- seleccionar el banco del que se va a retirar el dinero, por ejemplo Banco A
- pulsar el botón de proceso *Añadir transacción*
- una vez en esa nueva ventana, seleccionar el *Tipo de Transacción* Concepto contable
- introducir una *Fecha de la transacción*
- seleccionar el *Concepto contable* creado previamente
- y, por último, indicar el importe *Pagado*, por ejemplo 100,00 USD.

Esta nueva transacción se muestra a continuación en la *solapa Transacción* de la ventana *Cuenta financiera*. Etendo muestra claramente el importe de retirada registrado.
El siguiente paso es contabilizar la transacción de retirada. 

!!!note
        Es posible contabilizarla manualmente utilizando el botón de proceso Post o puede contabilizarse automáticamente si el Proceso del servidor de contabilidad está habilitado en la ventana [Procesamiento de Peticiones](../../../user-guide/etendo-classic/basic-features/general-setup/process-scheduling/process-request.md).

La contabilización tendrá el siguiente aspecto:

| Cuenta                          | Débito  | Crédito |
|----------------------------------|--------|--------|
| [Débito del concepto contable](../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup/gl-item.md#accounting)   | Importe pagado |        |
| [Banco A - Cuenta de retirada](../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#accounting-configuration)              |        | Importe pagado |


### Creación de la comisión bancaria

La empresa de este ejemplo necesita crear la transacción de retirada tal y como se ha descrito anteriormente y una transacción adicional para reflejar la comisión bancaria. La forma de hacerlo es:

- pulsar una vez más el botón de proceso *Añadir transacción*
- seleccionar el *Tipo de Transacción* Comisión
- introducir una *Fecha de la transacción*
- y, por último, indicar el importe *Pagado*, por ejemplo 1,00 USD.

!!!info
        Una comisión bancaria también puede registrarse en una cuenta financiera utilizando un Concepto contable creado previamente denominado Bank Interest. La contabilidad de Bank Interest podría configurarse como '7010 Interest income' para crédito y '7020 Interest expense' para débito.


En este ejemplo, se crearán dos transacciones en la *solapa Transacción* de la *Cuenta financiera*, una para la retirada y otra para la comisión.
Las transacciones de comisión también pueden contabilizarse del mismo modo que la transacción de retirada.



| Cuenta                          | Débito  | Crédito |
|----------------------------------|--------|--------|
| [Banco A - Cuenta de comisión bancaria](../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#accounting-configuration)   | Importe pagado |        |
| [Pago - Retirada](../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#accounting-configuration)              |        | Importe pagado |


## Creación de la transacción de depósito

El paso final es crear una transacción de depósito en la Cuenta financiera en la que deben depositarse los fondos.
La empresa de este ejemplo necesita:

- navegar a la ventana [Cuenta financiera](../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#financial-account)
- seleccionar el banco en el que se va a depositar el dinero, por ejemplo Banco B
- pulsar el botón de proceso *Añadir transacción*
- una vez en esa nueva ventana, seleccionar el *Tipo de Transacción* Concepto contable
- introducir una *Fecha de la transacción*
- seleccionar el *Concepto contable* creado previamente
- y, por último, indicar el importe *Recibido*, en este ejemplo 100,00 USD.

Esta nueva transacción se muestra a continuación en la *solapa Transacción* de la ventana *Cuenta financiera*. Etendo muestra claramente el importe de depósito registrado.
El siguiente paso es contabilizar la transacción de depósito. Es posible contabilizarla manualmente utilizando el botón de proceso *Post* o puede contabilizarse automáticamente si el Proceso del servidor de contabilidad está habilitado en la ventana [Procesamiento de Peticiones](../../../user-guide/etendo-classic/basic-features/general-setup/process-scheduling/process-request.md) window.


La contabilización tendrá el siguiente aspecto:


| Cuenta                          | Débito  | Crédito |
|----------------------------------|--------|--------|
| [Banco B - Cuenta de depósito](../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#accounting-configuration)   | Importe recibido |        |
| [Crédito del concepto contable](../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup/gl-item.md#accounting)              |        | Importe recibido |

## Transferencia de fondos entre cuentas de caja

La empresa de este ejemplo necesita seguir exactamente los mismos pasos de ejecución. La única diferencia es el *Tipo de cuenta financiera* a utilizar. En esta ocasión se utilizará un tipo de cuenta financiera *Caja* al crear la transacción de retirada y la transacción de depósito.
Transferencia de fondos entre diferentes organizaciones

## Transferencia de fondos entre diferentes organizaciones 

La empresa de este ejemplo necesita seguir exactamente los mismos pasos de ejecución. La única diferencia es la *Organización* que se va a utilizar. En esta ocasión:

- el *Concepto contable para el importe en tránsito a retirar* debe crearse en *Organización A*
- la *transacción de retirada* debe crearse en una *Cuenta financiera* de *Organización A*
- el *Concepto contable para el importe en tránsito a depositar* debe crearse en *Organización B*
- y, por último, la *transacción de depósito* debe crearse en una *Cuenta financiera* de *Organización B*

La contabilización de la transacción de retirada en Organización A tendrá el siguiente aspecto:

| Cuenta                          | Débito  | Crédito |
|----------------------------------|--------|--------|
| [Débito del concepto contable](../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup/gl-item.md#accounting)   | Importe pagado |        |
| [Banco A - Cuenta de retirada](../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#accounting-configuration)              |        | Importe pagado |

La contabilización de la transacción de depósito en Organización B tendrá el siguiente aspecto:


| Cuenta                          | Débito  | Crédito |
|----------------------------------|--------|--------|
| [Banco B - Cuenta de depósito](../../../user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions.md#accounting-configuration)   | Importe recibido |        |
| [Crédito del concepto contable](../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup/gl-item.md#accounting)              |        | Importe recibido |

## Resultado

Esto completa la transferencia de fondos entre cuentas financieras. Como resultado:

- el saldo del Banco A se reduce en 101,00 USD
- el saldo del Banco B se incrementa en 100,00 USD

El escenario anterior es solo una transferencia de fondos entre cuentas financieras de la misma organización.

En el caso de una transferencia de fondos entre cuentas financieras de diferentes organizaciones:

- el saldo del Banco A de la organización A se reduce en 101,00 USD
- el saldo del Banco B de la organización B se incrementa en 100,00 USD

El escenario anterior significaría, de algún modo, un gasto en la Organización A y un ingreso en la Organización B.

---

Este trabajo es una obra derivada de [Guías prácticas](https://wiki.openbravo.com/wiki/How_To){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.