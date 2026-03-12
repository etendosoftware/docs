---
title: Gestión de Proyectos y Servicios - Primeros pasos
tags: 
 - Primeros pasos
 - Proyecto multifase
 - Informe de gasto
 - Progreso de Proyectos
 - Tipo de proyecto
 
---

![cover-getting-started.png](../../../../assets/getting-started/overview/cover-getting-started.png)
# Gestión de Proyectos y Servicios - Primeros pasos

## Visión general

La funcionalidad de Gestión de Proyectos y Servicios es esencial para que las empresas gestionen proyectos, servicios o ambos. Ayuda a las organizaciones a planificar, ejecutar, supervisar y optimizar proyectos y servicios de forma eficiente, integrándolos con otras funcionalidades como Gestión de Compras, Gestión de Ventas, Gestión Financiera, etc.

El módulo de Gestión de Proyectos y Servicios consta de:

- [Proyecto multifase](../project-and-service-management/transactions.md#multiphase-project) para gestionar proyectos con fases y tareas.
- [Informe de gasto](../project-and-service-management/transactions.md#expense-sheet) para gestionar costes relacionados con proyectos.

![](../../../../assets/user-guide/etendo-classic/basic-features/project-and-services-management/getting-started/project-and-service-diagram.png)

Como se observa en este diagrama, tras configurar la información que se muestra [a continuación](#configuración), para gestionar un proyecto, el usuario debe introducir un [Proyecto multifase](../project-and-service-management/transactions.md#multiphase-project) en la ventana correspondiente. Esta ventana permite registrar el progreso de un proyecto en diferentes [Fase](../project-and-service-management/transactions.md#project-phase-tab). Cada proyecto incluye una o más fases y, en cada fase, una o más [Mantenimiento](../project-and-service-management/transactions.md#project-task-subtab). Para cada una de estas fases, es posible realizar un proceso de [aprovisionamiento a pago](../procurement-management/getting-started.md#procure-to-pay-business-flow), para las compras necesarias del proyecto, o un proceso de [pedido a cobro](../sales-management/getting-started.md#order-to-cash-business-flow) para las ventas necesarias del proyecto. Para registrar los gastos del proyecto requeridos, se utiliza la ventana de [Informe de gasto](../project-and-service-management/transactions.md#expense-sheet). Una vez que una fase se cierra, el usuario puede revisar la rentabilidad utilizando las [Herramientas de análisis](../project-and-service-management/analysis-tools.md) disponibles. Este flujo se realiza para cada una de las fases de un proyecto y, una vez completadas todas las fases, el proyecto puede ser [Cerrado](../project-and-service-management/transactions.md#process-buttons).

### Conceptos clave

Los conceptos clave de gestión de proyectos y servicios mencionados en este capítulo son:

- [Terceros](../master-data-management/master-data.md#business-partner):
    - Proveedor: tercero que suministra bienes y/o servicios. En la gestión de proyectos y servicios, el proveedor es el vendedor de los bienes suministrados relacionados con el proyecto, la empresa de consultoría a la que se subcontrataron servicios de consultoría y el empleado al que se le reembolsan gastos relacionados con un proyecto.
    - Cliente: la parte a la que se venden bienes o servicios. En la gestión de proyectos y servicios, el cliente es a quien se le cargan los costes y gastos del proyecto.
    - Empleado: persona que trabaja en la empresa. En la gestión de proyectos y servicios, la información del empleado se utiliza para el cálculo del coste del proyecto, en base a los [Informe de tiempo](../project-and-service-management/transactions.md#expense-sheet).
- [Pedido de venta](../sales-management/transactions.md#sales-order): documento que lista los bienes y/o servicios proporcionados a un cliente y las condiciones de la venta.
- [Factura (Cliente)](../sales-management/transactions.md#sales-invoice): documento utilizado para administrar un derecho de cobro. El documento lista los bienes y/o servicios proporcionados a un cliente y las condiciones de la venta.
- [Factura (Proveedor)](../procurement-management/transactions.md#purchase-invoice): documento utilizado para administrar una obligación de pago. El documento lista los bienes y/o servicios proporcionados por un proveedor.
- [Tipo de proyecto](../project-and-service-management/setup.md#project-type): plantilla utilizada para crear fácilmente fases y tareas en un proyecto multifase. Esto es especialmente útil para completar automáticamente fases y tareas según la plantilla sin realizar el proceso manualmente.
- [Proyecto multifase](../project-and-service-management/transactions.md#multiphase-project): formulario utilizado para registrar un proyecto, los gastos planificados, los márgenes, para quién se ejecutará el proyecto y las fases y tareas del proyecto.
- [Fase](../project-and-service-management/transactions.md#project-phase-tab): un periodo de tiempo durante el cual se ejecutan determinadas actividades.
- [Tarea](../project-and-service-management/transactions.md#project-task-subtab): actividades que se ejecutan durante una fase del proyecto.
- [Informe de gasto](../project-and-service-management/transactions.md#expense-sheet): formulario utilizado para registrar gastos de artículos y tiempo para un proyecto.

### Configuración

A continuación se introduce en la aplicación para el módulo de gestión de proyectos y servicios:

- [**Dimensión proyecto**](../financial-management/accounting/setup/general-ledger-configuration.md#dimension-tab): para poder seleccionar proyectos en pedidos y facturas, la dimensión de proyecto se crea como un nuevo registro con tipo Proyecto en la pestaña Dimensión de la ventana [Esquema contable](../financial-management/accounting/setup/general-ledger-configuration.md).

- [**Producto**](../master-data-management/master-data.md#product):
    - Tipos de producto **Servicios** y **Tipo de gasto**: para los productos del informe de gasto se configuran productos con tipo de producto Servicios (para tiempo) y tipo de producto Tipo de gasto (para gastos).
    - Tipo de producto **Artículo**: se utiliza el proceso estándar de [aprovisionamiento a pago](../procurement-management/getting-started.md#procure-to-pay-business-flow) para la compra de productos relacionados con el proyecto.

- [**Terceros**](../master-data-management/master-data.md#business-partner):
    - Cliente: el tercero para el que se ejecuta el proyecto se configura como cliente.
    - Proveedor: el tercero que suministra productos relacionados con el proyecto se configura como proveedor.
    - Empleado:
        - Se completa la información del proveedor para poder crear facturas de compra para reembolsar gastos.
        - Se completa la categoría salarial para calcular el coste del tiempo dedicado al proyecto según lo documentado en los informes de tiempo.

- [**Tipo de proyecto**](../project-and-service-management/setup.md#project-type): se puede crear una plantilla con fases y tareas estándar para generar fácilmente fases y tareas en un proyecto multifase.

### Ejecución

El [Proyecto multifase](../project-and-service-management/transactions.md#multiphase-project) tiene la siguiente secuencia de eventos:

- La creación del Proyecto multifase con la siguiente información:
    - Importes planificados y márgenes relacionados con el proyecto en la sección Importes de la cabecera.
    - Información necesaria para crear un Pedido de venta en la sección Más información de la cabecera.
    - Opcionalmente, con el botón [**Establecer el tipo de proyecto**](../project-and-service-management/transactions.md#process-buttons), se utiliza un Tipo de proyecto existente para crear las fases y tareas. Alternativamente, sin utilizar un tipo de proyecto, las fases y tareas se crean manualmente en el Proyecto multifase.
    - Fechas de inicio y fin para el proyecto global y para fases y tareas.
    - Una vez introducida esta información, el estado del proyecto cambia a [Parte](../project-and-service-management/transactions.md#process-buttons).
- El coste planificado frente al real se supervisa en el informe [Rentabilidad de Proyectos](../project-and-service-management/analysis-tools.md#project-profitability) en base a lo siguiente:
    - Los informes de tiempo y los gastos de artículos se informan en [Informe de gasto](../project-and-service-management/transactions.md#expense-sheet) relacionados con el proyecto. En base a la categoría salarial del empleado en el momento del proyecto, la aplicación calcula el coste del tiempo dedicado.
    - Se crean facturas de compra para cualquier compra, coste de subcontratación o reembolso de gastos relacionados con el proyecto. Esto se realiza mediante [Crear facturas de gastos AP](../project-and-service-management/transactions.md#create-ap-expense-invoices).
    - Se crean facturas de venta como resultado de los Informe de gasto del proyecto. Esto se realiza mediante el proceso [Crear pedidos de venta según gastos](../project-and-service-management/transactions.md#create-sales-orders-from-expenses).
    - Al final de cada fase, se crea un Pedido de venta relacionado con la fase desde el Proyecto multifase utilizando el proceso [Generar pedido de venta de la fase](../project-and-service-management/transactions.md#process-button). La información para la creación del Pedido de venta se toma de la definición del proyecto y se realiza para el cliente del proyecto. Posteriormente, esto da lugar a la creación de una Factura (Cliente).
- El progreso del proyecto se supervisa de dos maneras. Para cada proyecto, las [Fase](../project-and-service-management/transactions.md#project-phase-tab) y [Mantenimiento](../project-and-service-management/transactions.md#project-task-subtab) pueden marcarse como completadas en la casilla de verificación destinada a tal fin. Además, puede utilizarse el informe [Progreso de Proyectos](../project-and-service-management/analysis-tools.md#project-progress). Recuerde que la precisión de la información del informe depende del uso de las casillas de verificación Completado en las pestañas Fase y Tarea.
- Tras la finalización de todas las fases, el estado del Proyecto multifase se cambia a [Parte Cerrada](../project-and-service-management/transactions.md#process-buttons).

!!!info
    Recuerde que esta es una visión general de la Gestión de Proyectos y Servicios; visite las secciones [Configuración](../project-and-service-management/setup.md), [Transacciones](../project-and-service-management/transactions.md) y [Herramientas de análisis](../project-and-service-management/analysis-tools.md) para obtener información más específica.

## Relación con otras áreas

Gestión de Proyectos y Servicios interactúa con los siguientes módulos:

- [Gestión de Compras](../procurement-management/getting-started.md):
    - Los materiales relacionados con el proyecto se solicitan utilizando el proceso de aprovisionamiento a pago.
    - Se generan facturas de compra para los gastos pagados a empleados y para los bienes solicitados a proveedores.
- [Gestión de Ventas](../sales-management/getting-started.md): se generan pedidos de venta y facturas de venta para el cliente para el que se ejecuta el proyecto.
- [Gestión de Almacén](../warehouse-management/getting-started.md): los materiales solicitados para el proyecto pueden recibirse en existencias.
- [Gestión Financiera](../financial-management/getting-started.md): la información de las facturas de venta y compra creadas se envía a cuentas a pagar y a cobrar.

---

Este trabajo es una obra derivada de [Gestión de Proyectos y Servicios](https://wiki.openbravo.com/wiki/Project_and_Service_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.