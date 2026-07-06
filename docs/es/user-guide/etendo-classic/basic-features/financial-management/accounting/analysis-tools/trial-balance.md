---
tags:
  - Etendo Classic
  - Financial Management
  - Accounting
  - Trial Balance
  - Financial Extensions
---

# Balance sumas y saldos { #trial-balance }

:material-menu: `Aplicación` > `Gestión Financiera` > `Contabilidad` > `Herramientas de análisis` > `Balance sumas y saldos`

<iframe width="560" height="315" src="https://www.youtube.com/embed/o5V3Op_qYtE?si=DnTJ77x6zSMZ5KrC" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el núcleo y nuevas funcionalidades, visite [Financial Extensions - Notas de versión](../../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

!!! warning
    Si no dispone del [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}, el informe permanecerá en una versión heredada con funcionalidad limitada. No será posible navegar directamente al Libro mayor desde el Tercero cuando el informe esté agrupado por esta dimensión, y las mejoras de interfaz y las opciones mejoradas para exportar el informe a Excel y PDF no estarán disponibles.

## Descripción general { #overview }

El **Balance sumas y saldos** verifica que el total de débitos sea igual al total de créditos.

Aunque habitualmente se genera al final de un periodo antes de preparar el Balance de situación y la Cuenta de resultados, en Etendo puede generarse en cualquier momento.

Para una **Organización** y un **Libro mayor** seleccionados, el informe muestra:

- El saldo de la cuenta en la fecha de inicio
- El total de débitos dentro del periodo seleccionado
- El total de créditos dentro del periodo seleccionado
- El saldo de la cuenta en la fecha de fin

En la parte inferior del informe, el **total de débitos debe ser igual al total de créditos**.


## Cabecera { #header }

![alt text](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/trial-balance/trial-balance-1.png)

Campos clave a destacar:

### Filtros primarios { #primary-filters }

- **Fecha de inicio**: La fecha a partir de la cual se toma el saldo de la cuenta.
- **Fecha de fin**: La fecha hasta la cual se calcula el saldo de la cuenta, utilizando la fórmula:  
  `Saldo a Fecha de Fin = Saldo a Fecha de Inicio + Total Débitos − Total Créditos`
- **Organización**: La organización para la que se genera el Balance sumas y saldos. Puede generarse para:
    - Tipo de organización **Entidad Legal con Contabilidad**.
    - Tipo de organización **Genérica**, que debe pertenecer a una organización *Entidad Legal con Contabilidad*. Estas organizaciones heredan el libro mayor de la entidad legal a la que pertenecen y pueden contabilizar transacciones.
    - Entidades de tipo **Organización**, que pueden compartir un libro mayor entre múltiples organizaciones que les pertenecen. Aunque este tipo no puede contabilizar transacciones directamente, el Balance sumas y saldos resume la información contable de todas las organizaciones relacionadas que comparten el mismo libro mayor.
- **Libro mayor**: El libro mayor asociado a la organización seleccionada.

### Filtros avanzados { #advanced-filters }

Esta sección proporciona opciones adicionales para refinar el informe de Balance sumas y saldos:

- **Nivel de Cuenta**: Define el nivel de detalle a mostrar en el informe. Las opciones incluyen:

    - **Título**
    - **Cuenta**
    - **Desglose**
    - **Subcuenta** (por defecto)
    
    !!! info 
        Por defecto, el informe se genera al nivel de **Subcuenta**. Esto garantiza que, para cada subcuenta del árbol de cuentas, el total de débitos sea igual al total de créditos.

- **Número de Página Inicial**: Establece el número de página en que comienza el informe. Útil cuando se integra este informe en documentos más extensos.

- **Importe de la entrada inicial al saldo inicial**: Esta opción está seleccionada por defecto. Controla cómo se muestra el saldo de apertura (p. ej., 1 de enero de 2021) en el informe:

    - Para las cuentas de pasivo con saldo de apertura negativo, el importe puede aparecer en la columna **Saldo a Fecha** o en la columna **Crédito**.
    - Para las cuentas de activo con saldo de apertura positivo, el importe puede aparecer en la columna **Saldo a Fecha** o en la columna **Débito**.

    !!! note
        Esta configuración solo aplica si la **Fecha Desde** del informe coincide con la fecha contable de apertura (p. ej., 1 de enero de 2021). De lo contrario, el saldo de apertura siempre se muestra en la columna **Saldo a Fecha**.

- **De la Cuenta / A la Cuenta**: Permite especificar un rango de subcuentas a incluir en el informe (solo disponible cuando el nivel de cuenta está configurado como *Subcuenta*).

### Dimensiones { #dimensions }

Es posible refinar el informe de Balance sumas y saldos seleccionando **Dimensiones** adicionales, como:

- **Tercero**
- **Producto**
- **Proyecto**

Estas dimensiones se registran cuando se contabilizan las transacciones en el libro mayor. Las transacciones siempre se vinculan a través de subcuentas.

- **Agrupar Por**: Permite agrupar el informe por una dimensión específica. Las opciones disponibles son *Tercero*, *Producto* y *Proyecto*.  
  Por ejemplo, si se selecciona *Tercero*, el informe mostrará los resultados agrupados por cada tercero, y es posible navegar directamente al Libro mayor de ese tercero desde el informe.

- **Incluir Importes a Cero**: Cuando está activado, el informe muestra todas las subcuentas, incluidas las que tienen saldos en cero.


## Botones { #buttons }

- **Ver**: Abre los resultados del informe en una nueva ventana. Desde allí, es posible navegar directamente al Libro mayor:
  
    - Haciendo clic en el Número de Cuenta de cada subcuenta.
    - O, si el informe está agrupado por Tercero, haciendo clic en el nombre del tercero para acceder a su vista de Libro mayor.

    <figure markdown="span">
        ![alt text](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/trial-balance/trial-balance-2.png)
        <figcaption>Ejemplo de salida del informe sin agrupar</figcaption>
    </figure>

    <figure markdown="span">
        ![alt text](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/trial-balance/trial-balance-3.png)
        <figcaption> Ejemplo del informe agrupado por Tercero</figcaption>
    </figure>

    En ambos casos, hay enlaces disponibles para **navegar directamente al Libro mayor**.

- **Exportar a PDF**: Genera una versión en PDF del informe. Este archivo puede imprimirse o almacenarse para su revisión posterior. El PDF respeta las mismas reglas de agrupación aplicadas en la búsqueda.

- **Exportar a Excel**: Genera un archivo Excel del informe. El archivo exportado también sigue las mismas reglas de agrupación aplicadas en la búsqueda.

---

Este trabajo es una obra derivada de [Financial Management](http://wiki.openbravo.com/wiki/Financial_Management){target="\_blank"} por [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.
