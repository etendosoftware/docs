---
tags:
  - Etendo Classic
  - Financial Management
  - Accounting
  - Customer Statement
  - Financial Extensions
---

# Extracto de Tercero

:material-menu: `Aplicación` > `Gestión Financiera` > `Contabilidad` > `Herramientas de Análisis` > `Extracto de Tercero`

!!! info
    Esta funcionalidad está disponible a partir de la versión **3.8.0** del Financial Extensions Bundle, compatible con **Etendo 25.1**. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el núcleo y nuevas funcionalidades, visite [Financial Extensions - Notas de versión](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

!!! warning
    Si no dispone del [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}, el informe permanecerá en una versión heredada con funcionalidad limitada.

## Visión General

El **Extracto de Tercero** es un informe consolidado que muestra todas las transacciones de un tercero contabilizadas en el libro mayor durante un periodo determinado. Este informe proporciona un historial financiero completo de la relación comercial, mostrando los débitos, créditos y saldos acumulados de cada transacción.

Este informe puede generarse para terceros configurados como:

- **Cliente**: Muestra las transacciones relacionadas con el cliente (facturas de venta, cobros recibidos, etc.).
- **Proveedor**: Muestra las transacciones relacionadas con el proveedor (facturas de compra, pagos realizados, etc.).
- **Cliente/Proveedor**: Muestra todas las transacciones de terceros con ambos roles.

El informe agrega transacciones de diversas fuentes, entre ellas:

- Facturas de Venta / Facturas de Compra
- Cobro / Pago
- Transacciones Financieras
- Conciliaciones

!!! warning
    En el informe solo se incluyen las transacciones en estado *Contabilizado*. Las transacciones *Completadas* pero no *Contabilizadas* no se tienen en cuenta.

El Extracto de Tercero proporciona la siguiente información para cada transacción:

- **Número de Documento**: Identificación de la transacción.
- **Fecha Contable**: Fecha en que se contabilizó la transacción.
- **Tipo de Documento**: Tipo de transacción (p. ej., Factura de Cliente, Factura de Proveedor, Transacción de Cuenta Financiera).
- **Débito/Crédito**: Importes financieros de cada transacción.
- **Saldo Neto**: Saldo acumulado calculado como \[Débito - Crédito\] para cada transacción, mostrando el saldo en ejecución a lo largo del periodo.

!!! note
    Los importes negativos se destacan mediante el uso de paréntesis ( ).

## Cabecera

![](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/customer-statement-report-1.png)

Como se muestra en la imagen anterior, se pueden configurar los siguientes parámetros:

- **Tipo de Informe**: Define el tipo de informe a generar. Las opciones incluyen:
    - **Cliente**: Muestra las transacciones relacionadas con el cliente.
    - **Proveedor**: Muestra las transacciones relacionadas con el proveedor.
    - **Cliente/Proveedor**: Muestra todas las transacciones de terceros con ambos roles. El informe muestra las transacciones de proveedor y cliente por separado, dividiéndolas en secciones distintas.
- **Organización**: La organización para la que se generará el extracto.
- **Libro Mayor**: El libro mayor asociado a la organización seleccionada.
- **Tercero**: El tercero (cliente, proveedor o ambos) para el que se generará el extracto.
- **Fecha de Inicio**: Fecha de inicio del periodo a incluir en el informe.
- **Fecha de Fin**: Fecha de fin del periodo a incluir en el informe.
- **Multidivisa**:
    - **Desmarcado** (por defecto): No agrupa los registros por divisa y muestra todos los importes en la divisa del Libro Mayor.
    - **Marcado**: Agrupa los registros por divisa y muestra los importes en la divisa original. El informe se dividirá por cada divisa diferente, cada una con su saldo inicial y final aislado del resto.
- **Sumar Saldo Inicial**:
    - **Desmarcado** (por defecto): El informe muestra un Saldo Inicial al comienzo, luego lista cada transacción con su Saldo Neto. El Saldo Final equivale al Saldo Inicial más el Saldo Neto final.
    - **Marcado**: El Saldo Inicial se agrega al Saldo Neto de cada transacción, de modo que el Saldo Final equivale al último Saldo Neto mostrado.

## Botones

En la barra de herramientas, se encuentran los siguientes botones para generar el informe:

- **Ver**: Abre los resultados del informe en una nueva ventana para su visualización inmediata.
- **Exportar a PDF**: Genera una versión en PDF del informe que puede imprimirse o almacenarse.
- **Exportar a Excel**: Genera un archivo Excel del informe para su análisis o personalización posterior.

Ejemplo de salida del Extracto de Tercero:

![](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/customer-statement-report-2.png)

---

Este trabajo es una obra derivada de [Financial Management](http://wiki.openbravo.com/wiki/Financial_Management){target="\_blank"} por [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.
