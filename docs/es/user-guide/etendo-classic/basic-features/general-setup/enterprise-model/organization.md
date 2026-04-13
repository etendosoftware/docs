---
title: Organización
tags:
    - Organización
    - Cliente
---

# Organización

:material-menu: `Aplicación` > `Configuración General` > `Organización` > `Organización`

## Visión general

Una **organización** es una empresa de un Cliente. Cada cliente debe tener al menos una organización creada ejecutando el proceso Crear organización. El proceso de creación de una organización finaliza después de establecerla como **Lista**.

En otras palabras, el proceso de creación de una organización finaliza después de establecerla como **Lista**, ya que Etendo requiere realizar algunas comprobaciones que validan que la organización se ha creado correctamente y que la estructura de la organización es válida. Si una organización no se crea correctamente, Etendo mostrará un error al intentar establecerla como lista.

!!!warning
    Una vez que una organización se establece como lista, ya no se pueden realizar cambios en la organización. Se pueden añadir nuevas organizaciones, pero no se pueden situar por encima de la organización actual. Se pueden añadir por debajo o al mismo nivel.

## Organización

La ventana **Organización** permite al usuario mantener las organizaciones creadas mediante el proceso Crear organización.

Existen diferentes tipos de datos que quedan por introducir o modificar para una organización:

- El **Nombre social** de la organización; este nombre, si existe, será el que se utilice en los informes financieros y fiscales.
- La casilla de verificación **Nivel agrupación** informa a Etendo si una organización va a ser una organización padre o no.  
Si una organización se establece como resumen, podría seleccionarse como Organización padre al ejecutar el proceso Crear organización.  
Este indicador siempre puede modificarse independientemente de si la organización ya está establecida como lista, ya que siempre es posible añadir organizaciones por debajo de una existente.
- La casilla de verificación **Permitir Control de Periodos** solo se muestra para organizaciones Entidad legal con contabilidad.

    ![](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/enterprise-model/organization-window.png)

    Si está habilitada, permite seleccionar un Calendario fiscal para el cual los periodos fiscales correspondientes pueden abrirse o cerrarse en la ventana Control de Periodos de Apertura/Cierre.

- El proceso de **periodos de apertura y cierre** impacta en las organizaciones situadas por debajo de la entidad legal con contabilidad.
- El Esquema contable de la organización.  
    Por ejemplo, las organizaciones de entidad legal con contabilidad necesitan registrar y contabilizar las transacciones financieras, como facturas y pagos, en el libro mayor.  
    Etendo permite personalizar la forma en que las transacciones financieras se contabilizan en el libro mayor; esto significa personalizar la configuración del Esquema contable para satisfacer las necesidades de la organización.  
    Este campo se establece automáticamente por defecto en Etendo, lo que significa que se crea un esquema contable por defecto, si:
    - un Pack de Localización que contenga un módulo de plan contable localizado
    - o un archivo CSV contable
    - o el módulo de Plan contable genérico está instalado y luego se selecciona al crear la organización ejecutando el proceso Crear organización.
- El elemento de mayor predeterminado para Transferencia de fondos se utiliza para establecer el valor por defecto del parámetro Elemento de mayor en el proceso Transferencia de fondos desde la Cuenta financiera.

**Información heredada**

Este grupo de campos está contraído por defecto con los siguientes campos de solo lectura.

- la **Organización con control de periodos** de la organización.
- la **Organización propietaria del calendario** de la organización.
- el calendario de la **Organización propietaria del calendario** de la organización.
- la **Entidad Legal** de la organización.
- la **Unidad de Negocio** de la organización.

Los campos anteriores se obtienen automáticamente y se establecen con los valores adecuados al establecer la organización como lista.

Una organización solo puede tener asignada una configuración de esquema contable salvo que:

1. la organización tenga la suya propia y, además, herede otra de su organización padre
2. o si la **funcionalidad avanzada de configuración de esquema contable** está habilitada a nivel de sistema.

La forma de permitir que una organización tenga asignada más de una configuración de esquema contable se describe a continuación:

- Como Administrador del sistema, establezca su propia plantilla como **En Desarrollo**. Guarde.
- Una vez hecho, navegue a la ventana **Ventanas, solapas y campos**
- Busque la ventana **Organización**
- Navegue a la solapa **Solapa** y haga doble clic en la solapa **Esquema contable**
- Establézcala como **Activo**. Guarde.
- Los pasos detallados anteriores muestran la solapa Esquema contable, que permite asignar más de una configuración de esquema contable a una organización.

El cliente de ejemplo Food & Beverage (F&B) suministrado con Etendo ilustra el escenario 1 anterior:

- Cada organización del cliente de ejemplo F&B se ha creado ejecutando el proceso **Crear organización**.
- El *F&B International Group* es un Tipo de Organización **Organización**.  
  Se seleccionó un archivo CSV contable mientras se creaba, del mismo modo que la divisa *USD*; por lo tanto, esta organización tiene asignada la configuración de esquema contable *F&B International Group US/A/Dollar*.

![](../../../../../assets/drive/tLSZQxp8xgwVv1GQOCVPR1ChHCnrGZ2-UQzAddoZKw4FvXouGcLHhfnVJBS4CS4i2lHeEhxCwDy9SDIRpBmVxuKagI42qJ8Ol4kBnBZOKMxq0fiF6wEqW3BGHXfKEzxaaJjPK6HT.png)

Esta configuración de esquema contable también puede compartirse con las organizaciones situadas por debajo, por ejemplo *F&B US, Inc* y *F&B España S.A.*.

- Del mismo modo, también se seleccionó un archivo CSV contable al crear la organización **Entidad legal con contabilidad** *F&B España S.A.* del mismo modo que la divisa EUR; por lo tanto, esta organización tiene asignada la configuración de esquema contable *F&B España, S.A US/A/Euro*.  
  Como consecuencia, *F&B España S.A.* tiene asignadas dos configuraciones de esquema contable: la suya propia y la heredada.
- Además, cada una de las configuraciones de esquema contable mencionadas anteriormente está vinculada a un árbol de cuentas o plan contable diferente.
- Por lo tanto, cada vez que una transacción de *F&B US Inc* se contabiliza en el libro mayor, Etendo abre una nueva ventana llamada **Diario asientos** que muestra el asiento creado para la configuración de esquema contable *F&B International Group US/A/Dollar* en USD y en las cuentas correspondientes de un plan contable determinado.
- Cada vez que una transacción de *F&B España S.A.* se contabiliza en el libro mayor, Etendo abre dos nuevas ventanas, una por cada configuración de esquema contable: una de ellas en USD y la otra en EUR, ambas en cuentas diferentes.

El botón de acción del árbol ![](../../../../../assets/drive/_YumQFCw0KLD-SFUaGI8zjTteIM6MCZo-pEA8IHbI757561hE9StOwYttf2lqUdlmcm8s7G6XtIR5ZjDwckNhEt8q9yIKTqpduMk-kYk3g5NPe24Pvq9DVCg_803cj5Y_cVbz1FX.png) permite arrastrar y soltar una organización dentro de un modelo empresarial, siempre que no esté **Validar**.

El proceso **Validar** tiene en cuenta la lista de requisitos siguiente por tipo de organización:

- _Tipo de organización_:
    - Sin requisitos
- _Tipo genérico_
    - tener un tipo de organización **Entidad Legal** por encima en el árbol del modelo empresarial.
- _Entidad legal sin contabilidad_
    - no tener otro tipo de organización **Entidad Legal** por encima en el árbol del modelo empresarial.
- Entidad legal con contabilidad
    - tener su propia configuración de esquema contable o una heredada
    - permitir el control de periodos
    - tener asignado un calendario fiscal

Una vez que una organización se establece como lista:

- La organización recién creada no puede moverse hacia arriba o hacia abajo dentro del árbol empresarial y no puede eliminarse.
- No es posible crear nuevas organizaciones por encima en el árbol, pero sí por debajo o al mismo nivel.

### Información

La solapa **Información** permite al usuario añadir información relevante de una organización, como la ubicación y el número de identificación fiscal.

![](../../../../../assets/drive/EsSwADTSSP7pJ1foh5fXjLZBaL1lb-u2MwMI9KFZaxpgC9ayM66e0NmIcdCOhXEzWLBG78RrjGI7VN_l1mdQg6COaMO0_lQhaXwafKPnSphAcus_1aqxM2Glbickzi645CuxqPVi.png)

Los campos a completar son:

- la ubicación de la organización
- el número de identificación fiscal, si es necesario
- el número DUNS, si existe
- el usuario que actuará como contacto principal de la organización. Este contacto de la organización se utiliza en algunos informes fiscales localizados (informes fiscales españoles), que requieren una persona de contacto.
- El número de factura de compra que se utilizará para los pagos. Hay dos opciones disponibles:
    - **Número de documento de factura** (número interno)
    - o **Número de factura del proveedor**  
        - Cualquiera de los anteriores se incluirá en el campo de descripción del pago para informar sobre el número de factura que se está pagando.  
        - Esto también cambia lo que se mostrará en varias ventanas de compras, como el botón _Añadir pago_ en la factura de compra o _Añadir Detalles de Pago_ en Pago emitido

Por último, la casilla de verificación Impuesto no deducible permite configurar una Organización como una _organización no deducible fiscalmente_, si está habilitada.

Este es el caso de organizaciones como las del Sector Público, para las cuales no se permite la deducción de impuestos. En este caso:

- el impuesto de compra se contabiliza como un gasto
- y las facturas de venta emitidas están exentas de impuestos

El campo Tipo impositivo de ventas exento permite introducir un tipo impositivo de ventas exento por defecto que se utilizará en las facturas de venta de las organizaciones no deducibles fiscalmente.

### Control de Periodos

La solapa **Control de Periodos** es una solapa de solo lectura que lista el estado del periodo del calendario fiscal de una organización.

![](../../../../../assets/drive/kwmxym70AykyaAYetGSTUoXl5ucDq29sJTt2mo3R0vCsxeSSnyIrP_1jtd36ENRoQHLrrHfFs3__qR6w2wn1hAbwEYbLmQtJ2SUoYa35ffgOHUiWFXUDDwnaL_Vt_ebrZIeAbDBo.png)

**El estado**

Se divide en dos columnas. Una representa el estado con un código de colores, lo que facilita entender la situación de un vistazo. La otra representa el estado por su nombre, lo que permite filtrar los registros mostrados. Los posibles valores de estado son:

- Todos nunca abiertos, en color gris. Periodos creados recientemente.
- Todos abiertos, en color verde. Todos los tipos de documento están abiertos para este periodo.
- Todos cerrados, en color rojo. Todos los tipos de documento están cerrados para este periodo.
- Mixto, en color naranja. No todos los tipos de documento tienen el mismo valor de estado en este periodo. Para más información, consulte la solapa Documentos a continuación.
- Todos cerrados permanentemente, en color rojo. Todos los tipos de documento están cerrados permanentemente para este periodo.

Esta solapa puede utilizarse para buscar un periodo (p. ej., Jan-19) y obtener su estado actual.

Como se muestra en la imagen siguiente, el periodo Feb-19 tiene un estado mixto, lo que significa que no todos los tipos de documento tienen el mismo valor de estado dentro de la organización *F&B España S.A.* que tiene asignado el **Calendario España**.

![](../../../../../assets/drive/cjahc3FYZMghn48UlTxGriply3wDhO6ZrX7BsdnjoN5X3rcwWWdLMoeiUbYQ-z--lNwxjsqgmI0d4-8dldLYHy4kY5CqUaj4n7ZAWfg0ML8NxMm9M5ykXpt9kzkh5O-sI2KEjpnz.png)

Para más información, consulte Control de Periodos de Apertura/Cierre.

#### Documentos

La solapa **Documentos** es una solapa de solo lectura que lista el estado de la categoría de documento para un periodo seleccionado de una organización.

![](../../../../../assets/drive/p2dQZKtljDS-XwNG0QoRVerVIGFhmR02mySLnF1RE_Cdjv1_jPAGhBCTccBupCha87MLhjnIjUOZGqEaJ1BndBl_sPUl2AGkTI23CJfcnbdB0fDJTRLXaN7oZ2EGhfHTa18bH_Ss.png)

Para más información, consulte Documentos en la ventana Control de Periodos de Apertura/Cierre.

### Conjunto de datos

La solapa **Conjunto de datos** permite ver los datos de referencia aplicados a la organización e informa en caso de que exista alguna actualización disponible de los datos de referencia aplicados.

![](../../../../../assets/drive/eIRJ-zXUf_s6qjf9H9aPP6ynr5hrgULf6DqAwhPtKq4PeR86LpUlWRS8FmcHglGxffMZzBw4AV0vBcyc0xXQO5HV6cxmc6pB0P_qF67nS2NknaRuS58DK3izsNbbO-xj7PM9zLAO.png)

### Almacén

Relación de almacenes con stock disponible priorizados de la Organización.

![](../../../../../assets/drive/6fsqpwBtDAXTJbyug4QSODfEv9-GzyhEMHMQQYgnsIufDr4S4GOCjrOOCSSeGz_u4GnkuVlaUPnOiH83pQbORHhsf2pLzKJKAaPERxaqCNXaHXgWRTz8-sIFqQzg4h_NTOJHKPmC.png)

En esta solapa, es posible definir el/los almacén/es de la organización; de este modo, la cantidad disponible de una organización es la suma del stock disponible de su/s almacén/es.

Es posible definir la prioridad de cada almacén de la organización; por lo tanto, Etendo propone primero los bienes del almacén con mayor prioridad.

---

Este trabajo es una obra derivada de [Configuración General](https://wiki.openbravo.com/wiki/General_Setup){target="_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="_blank"} por [Etendo](https://etendo.software){target="_blank"}.