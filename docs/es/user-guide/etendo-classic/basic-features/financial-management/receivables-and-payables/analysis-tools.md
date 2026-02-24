---
title: Gestión Financiera - Herramientas de análisis
tags:
    - Análisis financiero
    - Gestión de cobros
    - Gestión de pagos
    - Herramientas de informes
    - Etendo Financials
---
## Visión general

Esta sección describe las ventanas relacionadas con los informes financieros en Etendo. Estas son:

[:material-file-document-outline: Informe de previsión de tesorería](#informe-de-previsión-de-tesorería){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Listado de saldos a cobrar por antigüedad](#listado-de-saldos-a-cobrar-por-antigüedad){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Listado de saldos a pagar por antigüedad](#listado-de-saldos-a-pagar-por-antigüedad){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Informe de pagos y cobros](#informe-de-pagos-y-cobros){ .md-button .md-button--primary } <br>

[:material-file-document-outline: Histórico Ejecución de Pagos](#histórico-ejecución-de-pagos){ .md-button .md-button--primary } <br>
## Informe de previsión de tesorería

:material-menu: `Aplicación` > `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Herramientas de análisis` > `Informe de previsión de tesorería`

### **Visión general**

El informe muestra la posición de una cuenta financiera en una fecha futura, teniendo en cuenta los elementos planificados para cobrar o pagar en la cuenta financiera indicada.
## Listado de saldos a cobrar por antigüedad

:material-menu: `Aplicación` > `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Herramientas de análisis` > `Listado de saldos a cobrar por antigüedad`

### Visión general

El informe muestra los saldos a cobrar vencidos a la fecha que el usuario seleccione.

### **Origen de la información**

El origen de la información de este informe son las facturas como origen de los saldos a cobrar y los saldos a pagar.

-   **Factura**
    -   La fecha de vencimiento de una factura depende de las condiciones de pago y se calcula en base a la fecha de la factura.
    -   Si la factura tiene múltiples líneas del plan de pagos, cada línea tiene su propia fecha de vencimiento.
    -   Si existen pagos contra la factura, para este informe solo se consideran aquellos que estén en estado no confirmado a la fecha del filtro de fecha.

### **Multidivisa**

Este informe admite multidivisa.

-   **Factura**: si existe el tipo de cambio a nivel de documento, entonces el importe se calcula en base a ese valor; si no existe, entonces el tipo se toma a nivel de cliente (ventana Conversion Rates).

### **Filtro**

-   **Organización** (Obligatorio).
-   **Esquema contable** (Obligatorio). El usuario puede filtrar los resultados por el esquema contable de la organización. Todos los importes se convertirán a la divisa del esquema contable.
-   **Fecha a** (Obligatorio). Esta es la fecha a partir de la cual se procesará el informe. Las fechas de vencimiento y las fechas de pago se calcularán en base a esta fecha.
-   **Terceros** (Opcional). El usuario puede seleccionar múltiples terceros para filtrar los resultados.
-   **Número de días vencidos: Grupo uno/dos/tres/cuatro** (Obligatorio). Los resultados mostrados se agrupan según los rangos de días que el usuario debe introducir. El usuario puede introducir el día final para cada rango y, a continuación, la aplicación modificará automáticamente el día inicial de los siguientes rangos. Por ejemplo: en el grupo uno el usuario introduce 30, por lo que el rango pasa a ser 0 - 30; en el grupo dos el usuario introduce 60, por lo que el segundo rango es 31 - 60; y así sucesivamente.
-   **Mostrar detalles** (Opcional). Esta casilla ofrece al usuario la opción de mostrar la versión detallada del informe o la resumida. También se utiliza al imprimir y exportar a un archivo xls.
-   **Mostrar dudoso cobro** (Opcional). Esta casilla ofrece al usuario la opción de mostrar información sobre Dudoso cobro en el informe.
-   **Incluir facturas anuladas** (Solo disponible si la Preferencia "Habilitar filtro de documentos anulados en informes de antigüedad" está configurada como Y). Esta casilla ofrece al usuario la opción de incluir/excluir documentos anulados del informe.
-   **Incluir pagos revertidos** (Solo disponible si la Preferencia "Habilitar filtro de documentos de pagos revertidos en informes de antigüedad" está configurada como Y). Esta casilla ofrece al usuario la opción de incluir/excluir pagos revertidos del informe.

![](../../../../../assets/drive/1abmyBz-r9kRr3l7gNXmPgxwZrx-ca-AH.png)

### **Salida HTML/PDF/Excel**

El informe puede generarse en formato HTML, PDF y hoja de cálculo Excel.

### **Listado de saldos a cobrar por antigüedad**

Debe mostrar una tabla con los siguientes datos:

-   **Terceros**. Un tercero con saldos a cobrar pendientes. Esto también es un enlace a la versión detallada del informe para este tercero.
-   **Actual**. La suma de todas las deudas actuales que el tercero tiene con la organización que no están vencidas a la fecha seleccionada.
-   **Primer rango de días**. El importe que el tercero debe a la organización que está vencido y cuya fecha de vencimiento está dentro del rango.
-   **Segundo rango de días**. Igual que el anterior.
-   **Tercer rango de días**. Igual que el anterior.
-   **Cuarto rango de días**. Igual que el anterior.
-   **Quinto rango de días**. Igual que el anterior.
-   **Total**. Actual + todos los importes de los rangos de días.
-   **Crédito contabilizado**. Importe de dinero que el tercero ha dejado como crédito para utilizarlo más adelante. El importe aparece entre paréntesis porque debe restarse al calcular los totales.
-   **Neto**. Total - crédito del tercero.

Si los créditos se contabilizan en la misma cuenta que los saldos a cobrar, entonces el Neto coincidiría con el saldo del tercero. Si los créditos se contabilizan en una cuenta diferente, como anticipos, entonces el saldo del tercero coincidiría con el Total.

Si se selecciona la casilla **Mostrar dudoso cobro**, se muestran dos campos más.

-   **Dudoso cobro**. El importe clasificado como Dudoso cobro para ese tercero en particular.
-   **Porcentaje**. El porcentaje que representa el Dudoso cobro sobre la deuda neta de ese tercero en particular.

Además, cuando se selecciona Mostrar dudoso cobro, el importe Total es la suma de todas las deudas que no son dudosas. Por lo tanto, el Neto es Total + Dudoso - Créditos

![](../../../../../assets/drive/18axihCKiqxA8w_i5HX_UsGM6ZtE4G0U7.png)

### **Detalles del Listado de saldos a cobrar por antigüedad**

Debe mostrar una tabla con los siguientes datos: al hacer clic en el enlace PDF o XLS, se genera un PDF o un archivo de hoja de cálculo.

La información se agrupa por tercero, en caso de que el informe se ejecute para más de uno. Para cada tercero, la información mostrada es:

-   **Nº de documento**. El número del documento y también un enlace al mismo.
-   **Fecha del documento**. La fecha contable del documento.
-   **Tramos de vencimiento**. El importe pendiente de la factura. Se muestra en una columna u otra en función de la fecha de vencimiento y del filtro de fecha.
-   **Neto vencido**. El importe pendiente de la factura a la fecha. Es la suma de los importes en los tramos de vencimiento.
-   **Crédito contabilizado**. Cada línea representa un pago que ha generado crédito, y el importe es el crédito restante para utilizar a la fecha. El importe aparece entre paréntesis porque debe restarse al calcular los totales.
-   **Una línea de resumen para los tramos de vencimiento y el crédito contabilizado**.

Si los créditos se contabilizan en la misma cuenta que los saldos a cobrar, entonces el total Neto vencido coincidiría con el saldo del tercero. Si los créditos se contabilizan en una cuenta diferente, como anticipos, entonces el saldo del tercero coincidiría con el total Neto vencido más el crédito contabilizado (deshaciendo la resta de los créditos al total).

Además, existe una línea de resumen para todos los terceros.

Si se selecciona la casilla **Mostrar dudoso cobro**, se muestran dos campos más.

-   **Dudoso cobro**. El importe clasificado como Dudoso cobro para esa factura en particular.
-   **Porcentaje**. El porcentaje que representa el Dudoso cobro sobre el Neto vencido de esa factura en particular.

Además, cuando se selecciona Mostrar dudoso cobro, el importe Total es la suma de todas las deudas que no son dudosas. Por lo tanto, el Neto vencido es Total + Dudoso - Créditos

![](../../../../../assets/drive/1-9xrAmRtJQym6Hh1Enp8-6BpMW5Tu72Y.png)
## Listado de saldos a pagar por antigüedad

:material-menu: `Aplicación` > `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Herramientas de análisis` > `Listado de saldos a pagar por antigüedad`

### Visión general

El informe muestra los saldos a pagar vencidos a la fecha que seleccione el usuario.

### **Origen de la información**

El origen de la información de este informe son las facturas como origen de los saldos a cobrar y los saldos a pagar.

-   **Factura**
    -   La fecha de vencimiento de una factura depende de las condiciones de pago y se calcula en base a la fecha de la factura.
    -   Si la factura tiene múltiples líneas del plan de pagos, cada línea tiene su propia fecha de vencimiento.
    -   Si existen pagos contra la factura, para este informe solo se consideran aquellos que estén en estado no confirmado a la fecha del filtro de fecha.

### **Multidivisa**

Este informe admite multidivisa.

-   **Factura**: si existe el tipo de cambio a nivel de documento, el importe se calcula en base a ese valor; si no existe, entonces el tipo se toma a nivel de cliente (ventana Conversion Rates).

### **Filtro**

-   **Organización** (Obligatorio).
-   **Esquema contable** (Obligatorio). El usuario puede filtrar los resultados por el esquema contable de la organización. Todos los importes se convertirán a la divisa del esquema contable.
-   **A fecha de** (Obligatorio). Esta es la fecha a partir de la cual se procesará el informe. Las fechas de vencimiento y las fechas de pago se calcularán en base a esta fecha.
-   **Terceros** (Opcional). El usuario puede seleccionar múltiples terceros para filtrar los resultados.
-   **Número de días vencidos: Grupo uno/dos/tres/cuatro** (Obligatorio). Los resultados mostrados se agrupan según los rangos de días que el usuario debe introducir. El usuario puede introducir el día final de cada rango y, a continuación, la aplicación modificará automáticamente el día inicial de los siguientes rangos. Por ejemplo: en el grupo uno, el usuario introduce 30, por lo que el rango pasa a ser 0 - 30; en el grupo dos, el usuario introduce 60, por lo que el segundo rango pasa a ser 31 - 60; y así sucesivamente.
-   **Mostrar detalles** (Opcional). Esta casilla ofrece al usuario la opción de mostrar la versión detallada del informe o la resumida. También se utiliza al imprimir y exportar a un archivo XLS.
-   **Se deben incluir las facturas anuladas** (Solo disponible si la Preferencia "Enable void documents filter in Aging Reports" está configurada como Y). Esta casilla ofrece al usuario la opción de incluir/excluir documentos anulados del informe.
-   **Se deben incluir los pagos revertidos** (Solo disponible si la Preferencia "Enable reversed payment documents filter in Aging Reports" está configurada como Y). Esta casilla ofrece al usuario la opción de incluir/excluir documentos de pago revertidos del informe.

![](../../../../../assets/drive/1Yl2Zd0sXPSwkfD9IN_P-tP2pxy_CSCTR.png)

### **Salida HTML/PDF/Excel**

El informe puede generarse en formato HTML, PDF y hoja de cálculo.

### **Listado de saldos a pagar por antigüedad**

Debe mostrar una tabla con los siguientes datos:

-   **Terceros**. Un tercero con saldos a pagar pendientes. Esto también es un enlace a la versión detallada del informe para este tercero.
-   **Actual**. La suma de todas las deudas actuales que el tercero tiene con la organización y que no están vencidas a la fecha seleccionada.
-   **Primer rango de días**. El importe adeudado al tercero, cuya fecha de vencimiento está dentro del rango.
-   **Segundo rango de días**. Igual que el anterior.
-   **Tercer rango de días**. Igual que el anterior.
-   **Cuarto rango de días**. Igual que el anterior.
-   **Quinto rango de días**. Igual que el anterior.
-   **Total**. Actual + todos los importes de los rangos de días.
-   **Crédito contabilizado**. Importe de dinero que queda como crédito para el tercero para ser utilizado posteriormente. El importe aparece entre paréntesis porque debe restarse al calcular los totales.
-   **Neto**. Total - crédito del tercero.

Si los créditos se contabilizan en la misma cuenta que los saldos a pagar, entonces el Neto coincidirá con el saldo del tercero. Si los créditos se contabilizan en una cuenta diferente, como anticipos, entonces el saldo del tercero coincidirá con el Total.

![](../../../../../assets/drive/1Yl2Zd0sXPSwkfD9IN_P-tP2pxy_CSCTR.png)

### **Detalles del Listado de saldos a pagar por antigüedad**

Muestra una tabla con los siguientes datos: al hacer clic en el enlace PDF o XLS, se genera un archivo PDF o una hoja de cálculo.

La información se agrupa por tercero, en caso de que el informe se ejecute para más de uno. Para cada tercero, la información mostrada es:

-   **Nº de documento**. El número del documento y también un enlace al mismo.
-   **Fecha del documento**. La fecha contable del documento.
-   **Tramos de vencimiento**. El importe pendiente de la factura. Se muestra en una columna u otra en función de la fecha de vencimiento y del filtro a fecha de.
-   **Neto vencido**. El importe pendiente de la factura a fecha. Es la suma de los importes en los tramos de vencimiento.
-   **Crédito contabilizado**. Cada línea representa un pago que ha generado crédito, y el importe es el crédito restante para ser utilizado a fecha. El importe aparece entre paréntesis porque debe restarse al calcular los totales.
-   **Una línea de resumen para los tramos de vencimiento y el Crédito contabilizado**.

Si los créditos se contabilizan en la misma cuenta que los saldos a pagar, entonces el total Neto vencido coincidirá con el saldo del tercero. Si los créditos se contabilizan en una cuenta diferente, como anticipos, entonces el saldo del tercero coincidirá con el total Neto vencido más el Crédito contabilizado (deshaciendo la resta de los créditos al total).

Además, existe una línea de resumen para todos los terceros.

![](../../../../../assets/drive/1E-2_-hP5TV-Ylx8JE-KPHdZ6sZQkdHHG.png)
## Informe de pagos y cobros

:material-menu: `Aplicación` > `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Herramientas de análisis` > `Informe de pagos y cobros`

### Visión general

El **Informe de pagos y cobros** muestra información de cobros y/o pagos, que puede filtrarse mediante un amplio conjunto de filtros disponibles.

La información de cobros y/o pagos se muestra agrupada por el estado del pago; además, también pueden definirse criterios adicionales de agrupación y de ordenación.

El **Informe de pagos y cobros** es un informe dimensional de Etendo que contiene las siguientes opciones específicas de filtrado:

![](../../../../../assets/drive/1PX-rtKZBix9j8-LmDamIE90SjBybrPpM.png)

-   **Fecha**: introduzca una **Fecha desde** y una **Fecha hasta** que se utilizarán al recuperar los datos del pago, en relación con:
    -   la fecha de vencimiento del pago
    -   la fecha de pago del documento
    -   y la fecha del pago
-   **Cuantía de la comisión**: introduzca un **Importe desde** y un **Importe hasta** que se utilizarán al recuperar los datos del pago
-   **Tercero vacío**: seleccione si es necesario o no incluir en el informe pagos no relacionados con un tercero, sino con un **Concepto contable** o una **Comisión**. Las opciones disponibles son:
    -   **Incluir tercero vacío**: si se realiza esta selección, el informe incluye también pagos no relacionados con un tercero.
    -   **Excluir tercero vacío**: si se realiza esta selección, el informe excluye cualquier pago no relacionado con un único tercero.
    -   **Solo tercero vacío**: si se realiza esta selección, el informe solo incluye pagos no relacionados con un único tercero.
-   el estado del pago: las opciones disponibles son:
    -   Pendiente de pago
    -   Pendiente de ejecución
    -   Anulado
    -   Pago realizado
    -   Pago recibido
    -   Depositado no conciliado
    -   Retirado no conciliado
    -   Pago conciliado
-   el **Agente comercial.** Mostrará únicamente Pagos relacionados con Facturas que se hayan facturado para este Agente comercial.
-   el **Método de pago** y la **Cuenta financiera** del pago
-   la casilla de verificación **"Incluir pagos usando crédito"** permite
-   el campo **"Convertir a moneda"** permite al usuario seleccionar una moneda; por tanto, los **"Importe Transacción"** en una moneda distinta de la elegida se convierten a la moneda seleccionada y se muestran en el campo **"Base Imponible"**.
-   el campo "**F.conversión**" permite al usuario definir una fecha para seleccionar el tipo de conversión del sistema para cambiar los importes de transacción.
-   el **Tipo de pago**: las opciones disponibles son:
    -   Cobros
    -   Pagos
    -   Cobros y pagos
-   la casilla de verificación "**Vencido**" permite al usuario incluir en el informe únicamente pagos vencidos.
-   Por último, también es posible definir un **Criterio de agrupación** y un **Criterio de ordenación** adicionales que se utilizarán al mostrar la salida de datos de pagos.
    -   **Criterio de agrupación** como:
        -   Terceros
        -   Proyecto
        -   Categoría de tercero
        -   Moneda
        -   Cuenta (Cuenta financiera)
    -   **Criterio de ordenación** como:
        -   Fecha (Fecha del pago)
        -   Proyecto
        -   Categoría de tercero
        -   Moneda
        -   Fecha de vencimiento (Fecha de vencimiento del pago)
        -   Cuenta (Cuenta financiera)
        -   Terceros

!!! warning
    Tenga en cuenta que, si por ejemplo se selecciona "Terceros" como criterio de agrupación, se eliminará de la lista de criterios de ordenación, ya que agrupar implica ordenar.


El **Informe de pagos y cobros** se lanza pulsando el botón de proceso "**Selector**". Un ejemplo de la salida del informe se muestra en la imagen siguiente:

![](../../../../../assets/drive/1c5purjJlxqlGJ5jZjeFLEW0IfBPMWBXX.png)

Algunos campos relevantes a tener en cuenta son:

-   **Número de factura**: la flecha verde permite al usuario navegar al plan de pagos de la factura de venta/compra si solo se muestra un número de factura en este campo.
-   **Pago**: la flecha verde permite al usuario navegar al pago de la factura/documento
-   **DSO planificado** (Planned Days Sales Outstanding): el número de días entre la fecha de la factura y la fecha en la que debía pagarse, calculado con la fórmula **Fecha de vencimiento (factura) - Fecha de la factura**.
-   **DSO actual** (Current Days Sales Outstanding):
    -   si existe un pago, este campo muestra el número de días entre la fecha de la factura y la fecha del pago, calculado con la fórmula **Fecha del pago - Fecha de la factura**.
    -   si no existe un pago, este campo muestra el número de días que la factura está pendiente de pago, calculado con la fórmula **Fecha actual - Fecha de la factura**.
-   **Vencido** este campo indica si un pago se recibió a tiempo (el número de vencimiento se establece en cero), antes de tiempo (el número de vencimiento es un número negativo) o con retraso (el número de vencimiento es un número positivo)

Una factura marcada con un (*) significa que la factura se ha pagado utilizando un pago de crédito.

Varias facturas marcadas con (**) significa que las facturas se han pagado utilizando el mismo pago de crédito.
## Histórico Ejecución de Pagos

:material-menu: `Aplicación` > `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Herramientas de análisis` > `Histórico Ejecución de Pagos`

### Visión general

La ventana de histórico de ejecución de pagos es una ventana de solo lectura que muestra información relevante de cada ejecución de pagos realizada dentro de una organización.

Una ejecución de pagos puede contener solo un pago o varios pagos agrupados y ejecutados conjuntamente.

Es posible comprobar el estado y el resultado de la ejecución de pagos, así como el resultado y el mensaje de cada pago individual dentro de cada ejecución de pagos.

### Histórico Ejecución de Pagos

En esta ventana se muestran, entre otros datos relevantes, la fecha de ejecución y el estado de ejecución de cada ejecución de pagos, así como el origen de la ejecución.

![](../../../../../assets/drive/1-_lia6e8AfC9M7ON-PzhrWoRitQW9sSs.png)

La ventana **Histórico Ejecución de Pagos** solo muestra los pagos recibidos o realizados que requirieron un paso adicional de ejecución; por lo tanto, se configura un **Tipo de ejecución automática** para el **Método de pago** utilizado al realizar/recibir esos pagos.

El origen de la ejecución del pago puede ser:

-   **Automáticamente desde el proceso de Factura** - lo que significa que el pago se ejecuta automáticamente al completar la factura.
    -   Para obtener esta opción, el método de pago debe configurarse como se describe a continuación:
        -   la casilla de verificación **Cobro automático** está seleccionada para los pagos recibidos
        -   y/o la casilla de verificación **Depósito automático** está seleccionada para los pagos recibidos
        -   y la casilla de verificación **Diferido** no está seleccionada.
-   **Automáticamente desde el proceso de Pago** - lo que significa que el pago se ejecuta automáticamente al crear el pago.
    -   Para obtener esta opción, la casilla de verificación **Diferido** debe estar seleccionada.
-   **Formulario de ejecución de pagos** - lo que significa que el pago se ha ejecutado desde el formulario de ejecución de pagos.
    -   Para obtener esta opción, la casilla de verificación **Diferido** debe estar seleccionada; por lo tanto, el pago diferido puede ejecutarse posteriormente en el formulario de ejecución de pagos.
-   **Ventana de propuesta de pagos** - lo que significa que el pago se ha ejecutado desde la ventana de propuesta de pagos.
    -   Para obtener esta opción, la casilla de verificación **Diferido** debe estar seleccionada; por lo tanto, el pago diferido puede ejecutarse posteriormente desde la ventana de propuesta de pagos.
-   **Ventana de Pagos** - lo que significa que el pago se ha ejecutado en la ventana de pago emitido o en la ventana de pago recibido.
    -   Para obtener esta opción, la casilla de verificación **Diferido** debe estar seleccionada; por lo tanto, el pago diferido puede ejecutarse posteriormente en la ventana de pagos correspondiente.

Hay tres **Estado** disponibles:

-   **Ejecutado**, lo que significa que la ejecución de pagos se ha ejecutado. Los procesos de ejecución automática entregados actualmente por Etendo obtendrán un estado **Ejecutado**.
-   y **Ejecutado parcialmente** y **Pendiente**, que son estados que pueden ser utilizados por módulos como el módulo de impresión de cheques para gestionar aquellos casos en los que un pago no se ejecutó correctamente debido a cualquier problema ocasionado por un fallo de conexión.

#### Pagos

La solapa de pagos lista los pagos ejecutados en una ejecución de pagos.

![](../../../../../assets/drive/1porA4UfbmvSes9QKVmxrwr6b8zRav5vK.png)

#### Parámetros

La solapa de parámetros muestra el valor del/de los parámetro/s del proceso de ejecución de pagos.

Un proceso de ejecución puede tener un conjunto de parámetros definidos.

Por ejemplo, el proceso de ejecución **Print Check simple process** entregado por Etendo solo requiere el número de cheque al ejecutar el pago.

![](../../../../../assets/drive/14j20K8igu1aLPxaZLE1jDu_9jG-ydeaj.png)

---

Este trabajo es una obra derivada de [Gestión Financiera](http://wiki.openbravo.com/wiki/Financial_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.