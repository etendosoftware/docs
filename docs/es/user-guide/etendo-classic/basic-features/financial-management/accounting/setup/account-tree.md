---
title: Árbol de cuentas
tags:
    - Cuenta
    - Árbol
    - Gestión Financiera
    - Configuración
    - Contabilidad
---

# Árbol de cuentas

:material-menu: `Aplicación` > `Gestión Financiera` > `Contabilidad` > `Configuración` > `Árbol de cuentas`

## Visión general  

Un **árbol de cuentas** representa el **Plan de Cuentas (CoA)** de una organización. El CoA es la lista de cuentas utilizada en el libro mayor, incluyendo activos, pasivos, ingresos y gastos.  

Etendo proporciona varias formas de configurar un CoA en función de las necesidades contables de la organización. Los CoA pueden seguir requisitos específicos de cada país, traducirse a diferentes idiomas y adaptarse a las prácticas de la empresa.  

La **ventana Árbol de cuentas** permite a los usuarios:  

- **Revisar y gestionar** un plan de cuentas importado desde un módulo de CoA.  
- **Crear y personalizar** un nuevo plan de cuentas desde cero si es necesario.  

## Configuración del Árbol de cuentas

Etendo ofrece diferentes opciones para la configuración de los CoA: 

- **Instalar un módulo de localización o un plan genérico**: Algunos países como España o Francia requieren que se utilice un plan de cuentas específico en los libros oficiales, por lo que las autoridades pueden ver la misma lista de cuentas y el mismo nivel de detalle en la cuenta de Pérdidas y Ganancias y el Balance. Por otro lado, algunos países como EE. UU. no requieren ese nivel específico de detalle.


    !!!info 
        En el caso de España, Etendo proporciona un [Localization Bundle](../../../../optional-features/bundles/spain-localization/overview.md) que incluye el Plan de Cuentas oficial.

        Por ejemplo, el Spanish Localization Bundle incluye:

        -   el [General Spanish CoA](../../../../optional-features/bundles/spain-localization/overview.md#chart-of-accounts-pgc-2007-general).
        -   el [PYMES Spanish CoA](../../../../optional-features/bundles/spain-localization/overview.md#chart-of-accounts-pgc-2007-pymes).


    Cada organización puede **definir el plan de cuentas que mejor se adapte a sus prácticas**. En ese caso, Etendo proporciona un **módulo de Plan de Cuentas genérico** que ofrece una lista estándar de cuentas que puede evolucionar según las necesidades de la organización. Tras la instalación, el Plan de Cuentas genérico está disponible para su selección durante el proceso de [Crear entidad](../../../../../../developer-guide/etendo-classic/how-to-guides/how-to-run-an-initial-client-setup-process.md) y [Crear organización](../../../../basic-features/general-setup/enterprise-model/initial-organization-setup.md).


- **Importar un archivo CSV con la estructura del árbol de cuentas**: Puede importar un archivo CSV que define la estructura del árbol de cuentas durante el proceso de [Crear entidad](../../../../../../developer-guide/etendo-classic/how-to-guides/how-to-run-an-initial-client-setup-process.md) o [Crear organización](../../../../basic-features/general-setup/enterprise-model/initial-organization-setup.md) si la casilla **Incluir Contabilidad** está seleccionada. En ese caso, se le solicitará que elija el archivo CSV (archivo contable).   

    Este proceso crea:

    - El **Árbol de cuentas** (Plan de Cuentas) de la organización.
    -  La configuración por defecto del [Esquema contable](#esquema-contable).  

    !!! info
        Tal y como se explica en la guía [Cómo crear un módulo de Plan de Cuentas](../../../../../../developer-guide/etendo-classic/how-to-guides/how-to-create-a-chart-of-accounts-module.md), un **módulo de Plan de Cuentas** básicamente contiene el **archivo CSV** con la estructura del árbol de cuentas.


- **Crear el CoA manualmente**: un plan de cuentas también puede [crearse manualmente](../../../../how-to-guides/how-to-create-an-account-tree.md); si este es el caso, se recomienda comenzar a partir de un ejemplo de CoA como el genérico y evolucionarlo según las necesidades de la empresa, en lugar de empezar desde cero.

    !!! tip
        
        - Si se instala y selecciona un módulo de Plan de Cuentas o un archivo CSV contable a **nivel de entidad** mediante el proceso [Crear entidad](../../../../../../developer-guide/etendo-classic/how-to-guides/how-to-run-an-initial-client-setup-process.md), puede compartirse con cualquier organización disponible en la entidad.
        
        - Si se instala un módulo de Plan de Cuentas y luego se selecciona a **nivel de organización** mediante el proceso [Crear organización](../../../../basic-features/general-setup/enterprise-model/initial-organization-setup.md), el plan de cuentas creado automáticamente queda vinculado a la organización que se está creando.

## Ventana Árbol de cuentas

La cabecera principal de Árbol de cuentas permite crear el tipo de cuenta de la organización y, a continuación, definir el Plan de Cuentas. 

![alt text](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/set-up/account-tree8.png)


### Solapa Cuenta Contable

La solapa **Cuenta Contable** lista todos los elementos del plan de cuentas, desde los encabezados del plan de cuentas hasta las subcuentas.

![alt text](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/set-up/account-tree-0.png)

Cada **Plan de Cuentas** en Etendo contiene diferentes tipos de elementos organizados en la siguiente jerarquía:

-   Los elementos **Encabezado**, **Separar** y **Cuenta** ayudan a estructurar los CoA de manera que los informes financieros puedan generarse en base a esa estructura.

    - Encabezado: Encabezado principal (p. ej., Balance, Activos).

    - Separar: Grupos dentro de un encabezado (p. ej., Activos corrientes).

    - Cuenta: Cuenta general (p. ej., Caja, Clientes).

-   El elemento **Subcuenta** permite al usuario contabilizar las transacciones en el libro mayor.

    - Subcuenta: Nivel más bajo, donde se registran las transacciones (p. ej., Caja menor, Banco X).

Además, es bien sabido que cada cuenta, subcuenta en términos de Etendo, debe incluirse en un estado financiero:

-   Los tipos de cuenta **Activos**, **Pasivo** y **Patrimonio neto** deben incluirse en el Balance
-   Los tipos de cuenta **Gasto** e **Ingresos** deben incluirse en la cuenta de Pérdidas y Ganancias.

!!! tip
    La mejor manera de entender cómo se captura un plan de cuentas en Etendo es pulsando el icono **Árbol** ![](../../../../../../assets/drive/12vK4RHPNQ9vkJb_G1nUIneDdx6pLh_CY.png) que se puede encontrar en la barra de herramientas una vez que el usuario está en la solapa Cuenta Contable.

El icono Árbol abre una nueva ventana que muestra una **rama del árbol** por cada estado financiero:

-   Balance
-   Pérdidas y Ganancias
-   Cuentas temporales por defecto: esta rama del árbol de cuentas agrupa cuentas temporales por defecto que no son cuentas del libro mayor.

![alt text](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/set-up/account-tree-1.png)

Además, cada rama del árbol contiene varios elementos estructurados de forma jerárquica; por ejemplo:

-   La rama Balance se divide en:
    -   Activos
    -   Pasivos y Patrimonio neto

![alt text](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/set-up/account-tree-2.png)


Como se muestra en la imagen anterior, **Activos** también se divide en:

-   Activos corrientes
-   Activos a largo plazo
-   Amortización acumulada

Del mismo modo, **Patrimonio neto** también se divide en varias cuentas, en términos de Etendo **subcuentas**, como **Capital social** o **Reservas**.

Volviendo a la solapa **Cuenta Contable**, existen varios **campos básicos** que ayudan a definir cada elemento del plan de cuentas:

![alt text](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/set-up/account-tree-3.png)


-   El **Identificador** y el **Nombre** identifican el elemento del plan de cuentas.
    -   El identificador puede ser una sola letra, una palabra o un número; sin embargo, es importante tener en cuenta que el campo Identificador es el campo que Etendo utiliza al ayudar al usuario a crear un [elemento del árbol de cuentas](#elementos-del-balance).
-   El campo **Naturaleza de la cuenta (crédito/débito)** solo se muestra y, por tanto, es editable si el esquema contable vinculado al árbol de cuentas [NO está configurado como Mantenido centralmente](#esquema-contable).  
    En ese caso, la naturaleza de la cuenta de cada elemento del árbol de cuentas define cómo se mostrará el saldo de esa cuenta en los estados financieros:
    -   Si la naturaleza de la cuenta de un elemento del árbol de cuentas es **Débito contabilizado**, el saldo de esa cuenta se mostrará como **(Débito - Crédito)**.
        -   Los tipos de cuenta **Activos** normalmente se configuran como **Débito contabilizado**, por lo que su saldo deudor se muestra como **positivo** en el Balance.  
            Del mismo modo, su saldo acreedor se muestra como negativo en el Balance.
    -   Si la naturaleza de la cuenta de un elemento del árbol de cuentas es **Crédito contabilizado**, el saldo de esa cuenta se mostrará como **(Crédito - Débito)**.
        -   Los tipos de cuenta **Pasivo** normalmente se configuran como **Crédito contabilizado**, por lo que su saldo acreedor se muestra como **positivo** en el Balance. Lo mismo aplica al tipo de cuenta **Patrimonio neto**.
        -   Los tipos de cuenta **Ingresos** se configuran como **Crédito contabilizado**, por lo que su saldo acreedor se muestra como **positivo** en el informe de Pérdidas y Ganancias.
        -   Los tipos de cuenta **Gasto** se configuran como **Crédito contabilizado**, por lo que su saldo deudor se muestra como **negativo** en el informe de Pérdidas y Ganancias.
-   **Nivel del elemento**. Como ya se ha mencionado, existen cuatro tipos de elementos que ayudan a estructurar un plan de cuentas de manera que los informes financieros puedan generarse inmediatamente en base a la estructura del plan de cuentas.  
    Es importante remarcar que no es obligatorio utilizar los cuatro elementos, sino solo aquellos que ayuden a estructurar correctamente el Plan de Cuentas,  
    teniendo en cuenta que el más bajo, Subcuenta, es el único obligatorio porque los asientos se contabilizan en el libro mayor a través de las subcuentas.  
    Los cuatro tipos de elementos son:
    -   **Encabezado** - los elementos B - Balance y 1000-Activos son elementos de tipo encabezado porque están en la parte superior y tienen otros elementos por debajo.
    -   **Separar** - el elemento 1100 - Activos corrientes y 1500 - Activos a largo plazo son una separación del encabezado 1000-Activos.  
        A menudo, los activos y pasivos en un balance se separan en activos corrientes y activos a largo plazo. El tipo de elemento Separar ayuda a definir este tipo de situaciones.
    -   **Cuenta** - este nivel ayudaría a dividir el elemento 1100 - Activos corrientes en 1110 - Caja, 1200 - Cuentas a cobrar, etc., como forma de distinguir entre los diferentes tipos de activos corrientes.
    -   **Subcuenta** - este nivel es el nivel más bajo de detalle. Por ejemplo, el elemento de cuenta 1110 - Caja puede dividirse en las subcuentas 1120 - Cuenta corriente y 1140 - Subcuenta de caja menor para distinguir, al contabilizar en el libro mayor, las transacciones pagadas con cheque de las pagadas con caja menor.
-   **Tipo de cuenta bancaria**. Las opciones disponibles son **Activos**, **Pasivo**, **Patrimonio neto**, **Ingresos** y **Gasto**.  
    Los tipos de cuenta **Activos**, **Pasivo** y **Patrimonio neto** se incluyen en el Balance, así como en el asiento de cierre del balance, tal y como se describe en el artículo [Crear asiento de regularización](#openclose-period-control).  
    Los tipos de cuenta **Ingresos** y **Gasto** se incluyen en la Cuenta de Resultados, así como en el asiento de cierre de Pérdidas y Ganancias, tal y como se describe en el artículo [Crear asiento de regularización](#openclose-period-control).
-   **Nivel agrupación** define si un elemento del árbol de cuentas agrupa otros niveles por debajo o no; por tanto, los niveles de encabezado, cuenta y separar pueden marcarse como niveles de agrupación, mientras que subcuenta no debería. Puede haber elementos de encabezado que agrupen otros elementos por debajo, por ejemplo el elemento 1000-Activos, mientras que puede haber elementos de encabezado que no necesiten agrupar otros elementos por debajo sino [Personalizar elementos](#operando), por ejemplo el elemento 1900-Total Activos. El primer tipo necesita configurarse como **Nivel agrupación**, el segundo tipo no lo necesita. Además:
    -   Los importes mostrados en informes financieros como el Balance y la Cuenta de Resultados para un elemento no agrupador son la suma de los importes de débito y crédito contabilizados en esa cuenta (subcuenta).  
        El saldo de esa subcuenta en particular se mostrará como positivo o negativo dependiendo de su naturaleza de la cuenta o de lo que esté configurado centralmente en el [Esquema contable](#esquema-contable)
    -   Los importes mostrados en informes financieros como el Balance y la Cuenta de Resultados para un elemento agrupador son la suma de los importes de los elementos por debajo.  
        El saldo de ese elemento agrupador se mostrará como positivo o negativo dependiendo de su naturaleza de la cuenta o de lo que esté configurado centralmente en el [Esquema contable](#esquema-contable).

Adicionalmente, existen otros campos avanzados que también ayudan a configurar escenarios menos habituales. Esos campos son:

-   El campo **Mostrar Valor** define si el saldo de un elemento del plan de cuentas se va a mostrar y tener en cuenta en los informes financieros o no. Las opciones disponibles son:
    -   **Algebraico**, el elemento del plan de cuentas se mostrará en cualquier caso, independientemente del signo de su saldo. Es el más utilizado.
    -   **Solo negativo**, se mostrará solo en caso de que su saldo sea negativo
    -   **Sólo positivo**, igual que el anterior pero solo en caso de que su saldo sea positivo.
-   **Mostrar** define si un elemento del árbol de cuentas se va a mostrar en los informes financieros o no. Puede utilizarse para elementos usados para ejecutar cálculos que no necesitan mostrarse en un informe.
-   **Nodo de Título** define si un elemento del árbol de cuentas se va a mostrar en los informes financieros solo como un **Tratamientos** sin incluir su saldo. Esta opción funciona para elementos de encabezado del árbol de cuentas cuyo saldo no es 100% preciso por cualquier motivo, ya que existe otro elemento que obtiene el valor de saldo correcto mediante operaciones o [Personalizar elementos](#operando) entre un conjunto de elementos determinados.

### Solapa Operando

La solapa **Operando** permite al usuario obtener un elemento del árbol de cuentas como una combinación de una lista dada de elementos existentes.

Una vez que los elementos del árbol de cuentas se han seleccionado en un nuevo registro y en el orden de secuencia correcto, no es necesario especificar un signo, sino únicamente los elementos que se van a incluir. Los elementos operando deben ser elementos ubicados en el mismo nivel dentro del árbol de cuentas; de lo contrario, puede producirse un cálculo **recursivo**.

Por ejemplo, el elemento 1900-Total Activos es la suma de tres elementos operando:

-   activos corrientes
-   activos a largo plazo
-   y amortización acumulada

tal y como se muestra en la imagen siguiente.

![alt text](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/set-up/account-tree-4.png)

### Solapa Traducción

En la solapa **Traducción**, los elementos de cuenta pueden traducirse a cualquier idioma requerido.

![alt text](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/set-up/account-tree-5.png)

---

Este trabajo es una obra derivada de [Árbol de cuentas](https://wiki.openbravo.com/wiki/Account_Tree){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.