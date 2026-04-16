---
title: Actividad (ABC)
tags:
    - ABC
    - Activity
    - Dimension
    - Costing
    - Accounting
    - Financial Management
    - Setup
---

# Actividad (ABC)

:material-menu: `Aplicación` > `Gestión Financiera` > `Contabilidad` > `Configuración` > `Actividad (ABC)`

## Overview

La Actividad (ABC) forma parte de la funcionalidad de **Costeo Basado en Actividades (ABC) de Etendo**. Es una [**dimensión de contabilidad**](general-ledger-configuration.md#dimension-tab) que puede configurarse para una determinada configuración del libro mayor, permitiendo a las organizaciones analizar los costes en función de las actividades que los generan, en lugar de depender únicamente de las dimensiones contables tradicionales.

En Etendo, una Actividad representa un tipo de trabajo, proceso u operación dentro de una organización. Las actividades pueden habilitarse en una configuración del Libro mayor y utilizarse posteriormente en asientos contables para mejorar el **análisis de costes**.

!!!note
    Activity y [Centro de costos](./cost-center.md) son ambas dimensiones analíticas de contabilidad utilizadas para el análisis de costes, pero cumplen propósitos diferentes. Activity registra los costes según *qué trabajo se realizó* (un proceso u operación), mientras que Centro de costos registra los costes según *qué departamento o unidad* los incurrió. Ambas dimensiones pueden utilizarse conjuntamente para obtener desgloses de costes más detallados.

## Prerequisites

Antes de que se puedan seleccionar actividades en las transacciones, la **dimensión Activity debe estar habilitada** en la Configuración del Libro mayor de la organización.

Vaya a :material-menu: `Aplicación` > `Gestión Financiera` > `Contabilidad` > `Configuración` > `Esquema contable`. Abra la pestaña [**Dimensión**](general-ledger-configuration.md#dimension-tab), añada **Activity** como dimensión para el libro mayor correspondiente y, opcionalmente, márquela como obligatoria si cada transacción debe incluir una actividad. Guarde el registro. Una vez guardado, el campo Activity aparece en los formularios de transacción de esa organización.

Si el campo Activity no aparece después de completar el paso anterior, es posible que un desarrollador deba realizar una configuración adicional.

!!!info "For Developers"
    Habilitar la dimensión Activity en la Configuración del Libro mayor no es suficiente por sí solo para que el campo aparezca en las ventanas de transacción. Un desarrollador también debe configurar la columna Activity en el **Diccionario de la Aplicación** para cada pestaña de ventana donde el campo deba ser visible. Esto implica establecer la columna como mostrada y, si es necesario, añadir lógica de visualización para que el campo solo aparezca cuando la dimensión Activity esté activa para el libro mayor de la organización. Después de cualquier cambio en el Diccionario de la Aplicación, debe ejecutarse un smartbuild para compilar y aplicar las actualizaciones al sistema.

    Como referencia, consulte [How to Add a Field to a Window Tab](../../../../../../developer-guide/etendo-classic/how-to-guides/how-to-add-a-field-to-a-window-tab.md) y [How to Define Display Logic Evaluated at Server Level](../../../../../../developer-guide/etendo-classic/how-to-guides/how-to-define-display-logic-evaluated-at-server-level.md).

## Managing Activities

La ventana **Actividad (ABC)** permite a los usuarios definir y gestionar actividades por organización.

Mediante esta ventana, es posible:

- Crear **múltiples actividades** para una organización.

- Definir **actividades de resumen** para construir una estructura jerárquica.

- Agrupar **actividades relacionadas** para simplificar los informes y el análisis de costes.

Esta estructura ayuda a las organizaciones a comprender cómo se distribuyen los costes entre distintas áreas operativas.

![Ventana Actividad (ABC) mostrando los campos para definir actividades por organización](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/setup/abc-activity1.png)

Algunos campos a tener en cuenta para crear tantas actividades como sea necesario:

- **Organización**: Entidad organizativa dentro del cliente.
- **Identificador**: Un código corto utilizado para encontrar rápidamente esta actividad en cuadros de búsqueda y listas desplegables. Por ejemplo, introduzca *ASSEM* para una actividad de Assembly.
- **Nombre**: El nombre completo de la actividad tal como aparece en informes y formularios de transacción. Por ejemplo, *Assembly* o *Packaging*.
- **Descripción**: Opcional. Una breve explicación de lo que cubre esta actividad, para referencia interna.
- **Ayuda/Comentario**: Opcional. Orientación adicional para otros usuarios que trabajen con esta actividad.
- **Nivel agrupación**: Cuando está habilitado, esta actividad actúa como contenedor padre para agrupar subactividades. Las actividades de resumen no pueden asignarse directamente a transacciones; solo pueden asignarse sus actividades hijas.
- **Activo**: Cuando está marcado, esta actividad está disponible para su selección en transacciones. Desmárquelo para retirar una actividad sin eliminarla; dejará de aparecer en las listas desplegables, pero se conservarán sus datos históricos.

## Using Activities in Transactions

Una vez que la dimensión Activity está habilitada en la Configuración del Libro mayor y se han creado actividades, el campo **Activity** aparece en la sección **Dimensiones** al contabilizar transacciones, como facturas, asientos contables y otros documentos contables. Seleccione la actividad aplicable en la lista desplegable para etiquetar esa transacción con fines de seguimiento de costes.

## Example

Una empresa manufacturera quiere analizar sus costes operativos con más detalle, por lo que define las siguientes actividades ABC:

- **Producción** (Actividad de resumen)

    - **Assembly**

    - **Packaging**

- **Logística** (Actividad de resumen)

    - **Warehousing**

    - **Shipping**

Cuando se contabilizan facturas, gastos u otros asientos contables, los usuarios pueden asignar una **Activity** a cada asiento.

Más adelante, la empresa puede informar fácilmente sobre cuánto coste generó Producción frente a Logística, o profundizar en actividades específicas como Assembly o Shipping.

Este enfoque proporciona una mejor visibilidad de los costes, favorece una toma de decisiones más informada y mejora el análisis financiero dentro de Etendo ERP.

## Viewing Cost Reports by Activity

Una vez que las actividades se asignan a las transacciones contabilizadas, los costes pueden filtrarse y analizarse por actividad utilizando las herramientas de análisis contable:

- [Accounting Transaction Details](../analysis-tools.md#accounting-transaction-details): Una lista detallada de cada asiento del libro mayor, filtrable por Activity y otras dimensiones.
- [General Ledger Report](../analysis-tools.md#general-ledger-report): Una vista resumida de las transacciones contabilizadas que admite el filtrado por dimensiones contables, incluida Activity.


---

Este trabajo es una obra derivada de [ABC Activity](https://wiki.openbravo.com/wiki/ABC_Activity){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.