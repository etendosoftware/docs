---
title: Noticias de Etendo
tags:
  - Noticias de Etendo
  - Nuevas funcionalidades
  - Notas de la versión
  - Documentación funcional
  - Versiones
---

![](../assets/whats-new/etendo-news/etendo-news-0.png)

#

## Enero 2026

### Warehouse Extensions

<div class="grid cards" markdown>

- :material-warehouse: **Warehouse Extensions 3.6.0: Ejecución más rápida, controles más sólidos y operaciones de almacén más fluidas**
    
    ---

    ![](../assets/whats-new/etendo-news/advanced-warehouse-management.png){ width=500 align="right"}

    Con **Warehouse Extensions** versión [3.6.0](./release-notes/etendo-classic/bundles/warehouse-extensions/release-notes.md) (compatible desde **Etendo 25.4**), se añadió un módulo clave de control para ayudar a los equipos de almacén y contabilidad a **evitar costosos errores relacionados con fechas** en las operaciones diarias de almacén.

    **Nuevo módulo Material Management Rules ⚡**

    El nuevo módulo [Material Management Rules](../user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/overview.md#material-management-rules) añade una regla clara para decidir si Etendo debe permitir **transacciones de almacén con fechas anteriores a la fecha actual**—una fuente habitual de inconsistencias y reprocesos cuando intervienen la valoración de costes y los movimientos de stock. **Comportamiento por defecto:** la preferencia **Allow Backdated Cost Transactions** está configurada por defecto como **Y** (se permiten transacciones con fecha anterior) y puede configurarse según su política.

</div>

### Platform Extensions

<div class="grid cards" markdown>

- :material-chart-bar: **🖥️ Main UI Beta 0.10.0 y refuerzo de la plataforma para Etendo 25.4**
    
    ---

    ![](../assets/whats-new/etendo-news/new-ui-0.10.0.png){ width=500 align="right"}

    El bundle **Platform Extensions** se ha actualizado a [3.14.0](./release-notes/etendo-classic/bundles/platform-extensions/release-notes.md), incorporando una ronda de mejoras de la plataforma orientadas a la usabilidad diaria y la estabilidad.
    
    **Etendo Main UI – Beta 0.10.0**

    - **Mejoras en filtros de rejillas y tablas**: mejoras en los selectores de tipo de filtro y en el desplegable de filtros de tabla, restaurando un filtrado fiable en rejillas de alto volumen.
    - **Mejora de usabilidad de Copilot**: se añadió **soporte de entrada multilínea**, facilitando la redacción de prompts más largos y solicitudes estructuradas.
    - **Entrada de datos más rápida**: se incorporó un botón **Nuevo registro** directamente en los formularios.
    - **Procesos desde el menú**: ejecute **procesos e informes** directamente desde el menú, abriéndose los procesos manuales en una **nueva pestaña**.
    - **Exportaciones y navegación más limpias**: se corrigió la ordenación de la exportación CSV y se solucionaron problemas visuales al navegar por listas largas de subpestañas.
    - **Más acciones a mano**: se añadió **Imprimir registro** a la barra de herramientas.

</div>

### Producción


<div class="grid cards" markdown>

- :material-factory: **Anular partes de trabajo y reactivar consumo interno**
    
    ---

    ![](../assets/whats-new/etendo-news/production-void-reactivate.png){ width=500 align="right"}

    Los equipos de producción a veces necesitan corregir lo que ya se ha procesado. Con **Production Extensions Bundle [3.4.0](./release-notes/etendo-classic/bundles/production-extensions/release-notes.md)**, dispone de dos controles de alto impacto que hacen que las correcciones de producción sean más rápidas, seguras y totalmente auditables.

    **Anular partes de trabajo completados**  
    Ahora puede **anular un parte de trabajo completado/procesado** directamente desde la ventana Parte de trabajo. El sistema gestiona la reversión por usted. La acción solo está disponible cuando el parte de trabajo está completado, no está ya anulado, no tiene inconsistencias que impidan la reversión y **no está contabilizado en el libro mayor**.
    
    - Documentación: [Cómo anular partes de trabajo](../user-guide/etendo-classic/basic-features/production-management/transactions.md#how-to-void-work-efforts)
    - Blog: [Mejoras en la gestión de producción con Etendo Production Extensions](https://etendo.software/en/blog/improvements-production-management-etendo-production-extensions/)

    **Reactivar consumo interno**  
    Si un documento de Consumo interno se procesó por error, ahora puede **reactivarlo** para corregir cantidades, ubicaciones o productos sin limpieza manual. El documento vuelve a **Borrador** y se eliminan las **transacciones de material** generadas, revirtiendo los movimientos de inventario. La reactivación se bloquea cuando existen **costes calculados** asociados a las transacciones del documento.

    - Documentación: [Cómo reactivar consumo interno](../user-guide/etendo-classic/basic-features/production-management/transactions.md#how-to-reactivate-internal-consumption)

</div>
## Diciembre 2025

### Etendo

<div class="grid cards" markdown>

- :octicons-rocket-24: **¡Nueva versión de Etendo: ya está disponible la versión 25.4!**
    
    ---

    ![alt text](../assets/whats-new/etendo-news/etendo-25-4.png){ width=500 align="right"}

    ¡Ya está aquí la última versión [25.4](./release-notes/etendo-classic/release-notes.md) de Etendo! **Todos los módulos soportados** se han actualizado completamente para garantizar una integración fluida y el máximo rendimiento.

    Esta versión incorpora potentes mejoras diseñadas para aumentar la eficiencia, la automatización y el control en todas sus operaciones:

    **Rendimiento significativamente mejorado en la finalización de envíos de mercancía**  
    La finalización de envíos de mercancía ahora es más rápida y fluida que nunca, eliminando cuellos de botella y acelerando las operaciones diarias de almacén.
    
    - Blog: [Etendo 25.4 acelera la finalización de envíos de mercancía: adiós a los cuellos de botella](https://etendo.software/en/blog/etendo-25-4-goods-shipment-performance/)

    **Selección automática del Tipo de documento por Terceros**  
      
    Etendo ahora admite Tipos de documento específicos por Terceros en todos los procesos automáticos, como *Crear factura desde pedido*. Esto significa que las facturas se generan utilizando el Tipo de documento configurado para cada Terceros, en lugar de depender únicamente de los valores por defecto a nivel de organización, mejorando la precisión, el cumplimiento y la flexibilidad.

    **Cálculos de comisiones de ventas más flexibles y precisos**  
        
    Se han resuelto los problemas de comisiones basadas en margen, y ahora las comisiones pueden calcularse en la divisa deseada. Esto proporciona mayor transparencia, precisión y adaptabilidad para la gestión de incentivos de ventas.
      
    - Documentación: [Comisión](../user-guide/etendo-classic/basic-features/sales-management/setup/commission.md)
    - Blog: [Comisiones de ventas en ERP: cómo Etendo convierte los incentivos en resultados reales de negocio](https://etendo.software/en/blog/sales-commissions-erp-etendo/)

</div>

### Warehouse Extensions

<div class="grid cards" markdown>

- :material-warehouse: **Actualización de Warehouse & Logistics Extensions: tareas móviles, control de calidad y unidades logísticas**
    
    ---

    ![](../assets/whats-new/etendo-news/advanced-warehouse-management.png){ width=500 align="right"}

    Con la versión [3.5.0](./release-notes/etendo-classic/bundles/warehouse-extensions/release-notes.md) del bundle **Warehouse Extensions**, se han introducido varias mejoras funcionales en las operaciones móviles de almacén, el control de calidad de inventario, el procesamiento de códigos de barras y la gestión de unidades logísticas.

    **Nuevas pantallas de tareas móviles de almacén**  
    
    Se han añadido nuevas pantallas adaptadas a móvil para soportar las operaciones principales de almacén, incluyendo [Recepción](../user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management.md#reception-tasks), [Reubicación](../user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management.md#relocation-tasks), [Ajuste de inventario](../user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management.md#adjustment-tasks) e [Inspección de calidad de inventario](../user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management.md#inventory-quality-inspection) (tanto en móvil como en ERP).
    
    Estas pantallas incluyen validación de calidad a nivel de línea, generación automática de movimientos de inventario por inspección, soporte para unidades de medida alternativas y múltiples mejoras de usabilidad como desplazamiento automático, filtros y validaciones.

    - Blog: [Recepción de entrada en Etendo Logistics](https://etendo.software/en/blog/inbound-receipt-etendo-logistics/)

    **Mejoras en la inspección de calidad de inventario**  
      
    Se incluye la posibilidad de realizar inspecciones de calidad en todos los almacenes, utilizando el sistema de tareas, garantizando que todos los productos del almacén estén en condiciones óptimas, lo que mejora la trazabilidad y la precisión de los datos.

    - Documentación: [Inspección de calidad de inventario](../user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management.md#inventory-quality-inspection)

    **Gestión avanzada de códigos de barras**  
    
    La gestión de códigos de barras se ha ampliado para soportar *atributos personalizados*, incluyendo información de lote y fecha de caducidad, así como la capacidad de definir dinámicamente otros atributos. También se ha implementado el manejo de códigos de barras para identificar cajas y palés. 
    Se ha mejorado la lógica de procesamiento y validación de códigos de barras para garantizar una ejecución de tareas más rápida y fiable.

    **Mejoras en etiquetas e impresión de códigos de barras**  
    
    El botón [Imprimir etiqueta](../user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management.md#buttons) ahora está disponible desde la ventana *Recepción de entrada*, con soporte para imprimir etiquetas para cajas, palés y productos en función de la cantidad operativa.
    
    **Priorización de tareas y orden de ejecución**  
    
    Las tareas de almacén ahora muestran la *prioridad directamente en las tarjetas de tareas*, permiten ordenar por número de secuencia y almacenan las prioridades en una *tabla personalizada gestionada por el usuario*, proporcionando mayor flexibilidad y control sobre la ejecución de tareas.

    **Mejoras en la gestión de unidades logísticas**  
    
    Se ha añadido soporte para *inventario referenciado de cajas y palés*, incluyendo la *creación de unidad logística al completar el Albarán (Proveedor)*.  
    Una solapa *Stock por unidades logísticas* rediseñada ahora muestra el inventario agrupado, mejorando la visibilidad y el control de stock.  
    Las preferencias de configuración relacionadas con las unidades logísticas se han refactorizado y ampliado para soportar estos escenarios.

    - Documentación: [Unidad logística de stock](../user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/stock-logistic-unit.md)
    - Blog: [Control de ventas y stock por formatos de embalaje en Etendo](https://etendo.software/en/blog/sales-stock-control-packaging-formats-etendo/)

    **Mejoras de rendimiento y usabilidad**  
    
    Se ha mejorado el rendimiento de carga de pantallas, se aplica actualización automática al volver desde las pantallas de detalle de tareas y se ha normalizado la nomenclatura en botones, campos, columnas y mensajes para mantener la consistencia.

</div>

### Platform Extensions

<div class="grid cards" markdown>

- :material-chart-bar: **🖥️ Actualización de Platform Extensions: UI más inteligente, informes y gestión de Mantenimiento**
    
    ---

    ![](../assets/whats-new/etendo-news/new-ui-0.9.0.png){ width=500 align="right"}

    El bundle Platform Extensions, en la versión [3.13.0](./release-notes/etendo-classic/bundles/platform-extensions/release-notes.md) compatible con **Etendo 25**, aporta compatibilidad total con **Etendo 25.4** e incorpora mejoras clave centradas en la usabilidad, la flexibilidad de informes y la eficiencia operativa, ayudando a los equipos a trabajar más rápido y con mayor control.

    **Nueva UI de Etendo – Beta 0.9.0**  
    
    La Workspace UI continúa evolucionando con mejoras orientadas a la usabilidad en *filtros, rejillas y navegación*, ofreciendo una experiencia de usuario más limpia, rápida e intuitiva.
        
    - Documentación: [Mejoras de UI](../user-guide/new-ui/ui-improvements.md)
    - Blog: [Nueva interfaz de Etendo: mejoras beta para filtros y rejillas](https://etendo.software/en/blog/etendo-new-interface-beta-improvements-filters-grids/)

    **Gestión de tareas más potente con prioridades**  
    
    El módulo **Mantenimiento** ahora incluye **gestión de prioridades de tareas**, permitiendo a los equipos organizar, priorizar y ejecutar el trabajo en función del impacto en el negocio.
      
    - Documentación: [Mantenimiento – Gestión de prioridades](../user-guide/etendo-classic/optional-features/bundles/platform-extensions/task.md)

</div>

### Sales Extensions

<div class="grid cards" markdown>

- :octicons-rocket-24: **Actualización de Sales Extensions: presupuestos más inteligentes y creación de pedidos sin fricciones**
    
    ---

    El bundle **Sales Extensions** en la versión [3.2.0](./release-notes/etendo-classic/bundles/sales-extensions/release-notes.md) cierra la compatibilidad, siendo ahora compatible únicamente con **Etendo 25.4 y posteriores**.

    **Selección automática del Tipo de documento desde presupuestos a pedidos**  

    El módulo *Presupuesto avanzado* ahora aplica automáticamente el *Tipo de documento específico por Terceros* al crear un **Pedido de venta desde un presupuesto**.  
    Esta mejora elimina ajustes manuales, reduce errores y garantiza que cada documento de ventas siga la configuración fiscal y comercial correcta definida para cada cliente.

    - Documentación: [Presupuesto de ventas](../user-guide/etendo-classic/basic-features/sales-management/transactions.md#sales-quotation)

</div>

### Copilot Extensions

<div class="grid cards" markdown>

- :material-robot: **Actualización de Copilot Extensions: mejoras funcionales y capacidades de IA ampliadas**
    
    
    ![](../assets/whats-new/etendo-news/copilot-december.png){ width=500 align="right"}

    ---

    Con la versión [3.11.0](./release-notes/etendo-copilot/bundles/release-notes.md) del bundle **Copilot Extensions**, totalmente compatible con **Etendo 25.4**, se han introducido varias mejoras funcionales y ampliaciones de capacidades en Copilot, agentes y herramientas.

    **Mejoras en Copilot**

    - **Mejora de herramientas, soporte de modelos y evaluación de tareas**  
        Copilot ahora proporciona una gestión estructurada del directorio de esquemas de herramientas, añade soporte para el *modelo gemini-3-pro-preview* e incluye un evaluador de tareas mejorado para una ejecución más precisa de tareas automatizadas y de varios pasos.
    
    **Mejoras en agentes:**

    - **Mejoras en Purchase Invoice Expert**  
        El agente [Factura (Proveedor)](../user-guide/etendo-copilot/bundles/overview.md#invoice-supervisor) se ha actualizado con prompts mejorados, ejemplos prácticos y validaciones adicionales, incluyendo la **validación del importe total**, para garantizar una mayor precisión al crear o procesar facturas de proveedor.

    - **Alineación de Product Generator con Headless API**  
        El agente [Product Generator](../user-guide/etendo-copilot/bundles/overview.md#data-initialization-supervisor) ahora utiliza la **especificación de Headless API**, mejorando la consistencia con los servicios backend y garantizando flujos de creación de datos más predecibles.

    **Actualizaciones de Tool Pack:**

    - **Capacidades avanzadas de OCR Tool**  
      La herramienta [OCR Tool](../developer-guide/etendo-copilot/available-tools/ocr-tool.md) se ha ampliado con funciones avanzadas de reconocimiento, mejorando la extracción de texto y ampliando su aplicabilidad a documentos más complejos. Ahora soporta coincidencia automática de plantillas de referencia, esquemas de salida estructurados y configuración multiproveedor.

</div>

### Financial Extensions

<div class="grid cards" markdown>

- :material-chart-bar: **Actualización de Financial Extensions: informes avanzados y correcciones en remesas**
    
    ---

    ![](../assets/whats-new/etendo-news/purchase-invoice-dimensional-report.png){ width=500 align="right"}

    Con la versión [3.9.0](./release-notes/etendo-classic/bundles/financial-extensions/release-notes.md) del bundle **Financial Extensions**, se han introducido varias mejoras en los informes financieros avanzados y en el procesamiento automatizado de remesas.

    
    **Análisis dimensional facturas compras como Definición del Proceso**  
    
    El **Análisis dimensional facturas compras** se ha migrado a una **Definición del Proceso**, lo que permite una ejecución más consistente, una mejor integración con los procesos de Etendo y una mayor mantenibilidad de las funcionalidades de informes avanzados. El informe original (no basado en proceso) se ha ocultado para evitar duplicidades y garantizar el uso consistente de la nueva versión basada en proceso.

    - Documentación: [Análisis dimensional facturas compras](../user-guide/etendo-classic/basic-features/procurement-management/analysis-tools.md#purchase-invoice-dimensional-report)
    - Blog: [El nuevo Análisis dimensional facturas compras en Etendo: más rápido, moderno y más flexible](https://etendo.software/en/blog/purchase-invoices-dimensional-report-etendo/)

    **Customer Statement Report migrado a definición de proceso**
    El **Customer Statement Report** se ha migrado a una definición de proceso, alineándolo con el modelo estándar de ejecución de informes y mejorando la usabilidad y la extensibilidad futura.
    
    - Documentación: [Customer Statement Report](../user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools.md#customer-statement)      

</div>
## Noviembre 2025

### Financial Extensions

<div class="grid cards" markdown>

- :material-chart-bar: **🚀 Nuevo módulo: Ajustar impuesto de factura**
    
    ---

    ![texto alternativo](../assets/whats-new/etendo-news/adjust-invoice-tax.png){ width=500 align="right"}

    En la versión [3.6.0](./release-notes/etendo-classic/bundles/financial-extensions/release-notes.md) del bundle Financial Extensions compatible con **Etendo 25**, el nuevo módulo [Adjust Invoice Tax](../user-guide/etendo-classic/optional-features/bundles/financial-extensions/adjust-invoice-tax.md) le permite corregir importes de impuestos de facturas por céntimos (± 0.01 en la divisa de la factura), tanto en facturas de venta como en facturas de compra, cuando todavía están en estado Borrador. Esto ayuda a conciliar diferencias de redondeo que a menudo provocan rechazos de facturas, desajustes fiscales o desequilibrios contables al integrarse con sistemas externos o autoridades fiscales. Beneficios clave:
		
    - Evita errores de integración y fiscales debidos a variaciones de redondeo.
    - Mantiene la trazabilidad completa: todos los ajustes manuales se registran para auditoría y control.
	- Admite cualquier divisa y funciona listo para usar para clientes en la versión core 23+ con el bundle Financial Extensions instalado.
    ---

    - Documentación: [Adjust Invoice Tax](../user-guide/etendo-classic/optional-features/bundles/financial-extensions/adjust-invoice-tax.md)
    - Blog: [¿Su factura fue rechazada por unos pocos céntimos? Descubra cómo Etendo resuelve problemas de redondeo y desequilibrios contables](https://etendo.software/en/blog/invoice-tax-adjustment/){target="_blank"}

</div>

### Platform Extensions

<div class="grid cards" markdown>

- :material-chart-bar: **🖥️ Nueva UI: Beta 0.8.0**
    
    ---

    ![](../assets/whats-new/etendo-news/new-ui-0.8.0.png){ width=500 align="right"}

    En la versión [3.12.0](./release-notes/etendo-classic/bundles/platform-extensions/release-notes.md) del bundle Platform Extensions compatible con **Etendo 25**, se publicó una nueva actualización: en noviembre se lanzó una beta de la nueva **UI del espacio de trabajo**, ofreciendo a los usuarios acceso anticipado a la interfaz renovada: mejor aspecto y experiencia, navegación más intuitiva y flujos de trabajo modernizados. 
    
    --- 
    - Documentación: [Mejoras de la UI](../user-guide/new-ui/ui-improvements.md)
    - Documentación: [Nueva UI - Instalar Etendo Main UI](../developer-guide/etendo-classic/getting-started/installation/install-etendo-main-ui.md)

</div>

### Copilot Extensions

<div class="grid cards" markdown>

- :material-chart-bar: **Memoria del agente y flujos de trabajo de IA más inteligentes**
    
    ---

    ![](../assets/whats-new/etendo-news/ai-memory.png){ width=500 align="right"}

    En la versión [3.10.0](./release-notes/etendo-copilot/bundles/release-notes.md) del bundle Copilot Extensions compatible con **Etendo 25**, esta versión introduce la herramienta Memory Tool, que habilita una “memoria del agente” persistente: ahora los agentes pueden almacenar, actualizar y recuperar contexto entre sesiones, gracias a un backend de base de datos vectorial (Chroma).💡 Qué significa esto para su flujo de trabajo:
	
    - Los agentes se vuelven más “con estado”: pueden recordar interacciones anteriores o datos clave para mejorar la continuidad y reducir pasos redundantes.
	- Mejor automatización: al configurar agentes (generación de texto, tareas, integraciones), ahora puede apoyarse en la memoria para mantener el contexto a lo largo del tiempo, lo que mejora la productividad y los procesos impulsados por IA.
    
    --- 
    - Documentación: [Cómo personalizar un agente con memorias del agente](../developer-guide/etendo-copilot/how-to-guides/how-to-customize-an-agent-with-agent-memories.md)
    
</div>
## Septiembre 2025

### Etendo

<div class="grid cards" markdown>

- :octicons-rocket-24: **¡Nueva versión de Etendo: ya está disponible la versión 25.3!**
    
    ---

    ![Tipo de documento](../assets/whats-new/etendo-news/document-type.png){ width=500 align="right"}

    ¡Ya está aquí la última versión [25.3](./release-notes/etendo-classic/release-notes.md) de Etendo! Se han actualizado todos los módulos compatibles para una integración completa.
    
    En esta última versión, se ha añadido una nueva funcionalidad: la posibilidad de configurar tipos de documento para facturas, pedidos y envíos/recepciones en función del tercero seleccionado: 

    - Documentación: [Tipo de documento](../user-guide/etendo-classic/basic-features/master-data-management/master-data.md#document-type)
    - Blog: [¿Sigue creando facturas manualmente? Descubra cómo Etendo 25.3 automatiza la selección del tipo de documento por cliente](https://etendo.software/en/blog/document-type-tab-etendo-25-3/){target="_blank"}

</div>

<div class="grid cards" markdown>

- :octicons-rocket-24: **¡Nueva versión del plugin de Etendo Gradle: ya está disponible la versión 2.2.0!**

    ¡Ya está aquí la última versión [2.2.0](./release-notes/etendo-classic/plugins/etendo-gradle-plugin/release-notes.md) del plugin de Etendo Gradle!
    
    Disfrute de un nuevo asistente de instalación interactiva que le guía a través de la configuración de Etendo: configure con facilidad los ajustes del sistema central y las variables específicas de módulo para los bundles. Acelere los despliegues, reduzca los errores de configuración y póngase en marcha más rápido.

    - Documentación: [Instalación interactiva](../getting-started/interactive-installation.md)

</div>

### Platform Extensions

<div class="grid cards" markdown>

- :octicons-package-16: **¿Necesita generar imprimibles usando proveedores de impresión? Conozca el nuevo módulo**
    
    En la versión [3.10.0](./release-notes/etendo-classic/bundles/platform-extensions/release-notes.md) del bundle Platform Extensions, se añadió el módulo [Print Provider](../user-guide/etendo-classic/optional-features/bundles/platform-extensions/print-provider.md).
    
    Permite usar el servicio **Print Node** de forma predeterminada o ampliar el módulo para implementar múltiples servicios. También permite crear plantillas de impresión que pueden ejecutarse desde diferentes ventanas de Etendo.
</div>

### Financial Extensions

<div class="grid cards" markdown>

- :material-chart-bar: **Control total sobre documentos no contabilizados: identifique, revise y contabilice fácilmente varios documentos pendientes en un solo lugar**

    --- 

    ![documentos-no-contabilizados](../assets/whats-new/etendo-news/not-posted-documents.png){ width=500 align="right"}

    En la versión [3.4.0](./release-notes/etendo-classic/bundles/financial-extensions/release-notes.md) del bundle Financial Extensions compatible con **Etendo 25**, la ventana **Not Posted Documents**, parte del módulo **Bulk Posting**, introduce una forma más inteligente y eficiente de gestionar los registros contables. Ahora los usuarios pueden:  

    - **Filtrar por múltiples tipos de documento** para acotar exactamente lo que necesitan.  
    - **Navegar rápidamente** directamente a cualquier documento no contabilizado desde la cuadrícula de resultados.  
    - **Ejecutar acciones de contabilización masiva** para un procesamiento más rápido y consistente.  
    - **Refinar búsquedas** con filtros avanzados como organización, fecha contable y estado contable.
    --- 
    - Documentación: [Not Posted Documents](../user-guide/etendo-classic/basic-features/financial-management/accounting/transactions.md#not-posted-documents)
    - Blog: [¿Listo para el cierre contable? Descubra la ventana centralizada de Etendo para Not Posted Documents](https://etendo.software/en/blog/not-posted-documents-window-etendo/){target="_blank"}

</div>

<div class="grid cards" markdown>

- :material-chart-bar: **Balance sumas y saldos avanzado: profundice en los asientos del libro mayor y exporte a PDF y Excel**

    ![balance-sumas-y-saldos](../assets/whats-new/etendo-news/trial-balance.png)

    En la versión [3.4.0](./release-notes/etendo-classic/bundles/financial-extensions/release-notes.md) del bundle Financial Extensions, el informe **Balance sumas y saldos** incorpora nuevas capacidades: descubra el informe de Balance sumas y saldos renovado, obtenga información inmediata y accionable con navegación en un clic a los asientos del libro mayor, compatibilidad completa con todas las dimensiones contables y exportaciones mejoradas a Excel y PDF para compartir o auditar. Análisis más rápido, trazabilidad más clara y una salida profesional para potenciar sus flujos financieros.

    ---
    - Documentación: [Balance sumas y saldos](../user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools.md#trial-balance)
    - Blog: [Balance sumas y saldos en Etendo: funcionalidades avanzadas para un análisis contable superior](https://etendo.software/en/blog/trial-balance-in-etendo/){target="_blank"}

- :material-view-list: **Planificación financiera más inteligente con Presupuesto (Proyecciones)**

    ![presupuesto](../assets/whats-new/etendo-news/budget.png)
    
    En la versión [3.5.0](./release-notes/etendo-classic/bundles/financial-extensions/release-notes.md) y [1.29.0](./release-notes/etendo-classic/bundles/financial-extensions/release-notes.md) del bundle Financial Extensions compatible con **Etendo 23** y superior, la ventana **Presupuesto**, parte del módulo **Financial Report Budget**, permite a las organizaciones planificar con antelación, controlar el gasto y tomar decisiones financieras basadas en datos, todo en un solo lugar.

    Con **Presupuesto**, los usuarios pueden establecer objetivos de ingresos y gastos, compararlos con el rendimiento real y visualizar al instante las desviaciones. El análisis multidimensional por **Proyecto**, **Centro de costos**, **Terceros** o **Producto**, combinado con herramientas como **Exportar a Excel**, **Copiar Presupuesto** y **Comparación de datos reales**, convierte la presupuestación en un proceso dinámico y estratégico.

    - Elaborar presupuestos flexibles y realizar el seguimiento de las desviaciones en tiempo real.  
    - Comparar los resultados planificados y reales directamente dentro de contabilidad.
    - Analizar por múltiples dimensiones para obtener información más profunda.  
    - Exportar, copiar y reutilizar presupuestos para acelerar la planificación financiera. 
    ---
    - Documentación: [Presupuesto](../user-guide/etendo-classic/basic-features/financial-management/accounting/transactions.md#budget)
    - Blog: [Cómo los presupuestos y las proyecciones en Etendo impulsan la rentabilidad y el control financiero](https://etendo.software/en/blog/budgets-in-etendo/){target="_blank"}

</div>

### Warehouse Extensions

<div class="grid cards" markdown>

- :material-view-list: **Logística inteligente, más simple: trazabilidad total con unidades logísticas de palé y caja**

    Con la versión [3.3.0](./release-notes/etendo-classic/bundles/warehouse-extensions/release-notes.md) del paquete Warehouse Extensions, el módulo **Stock Logistic Unit** transforma la forma en que los almacenes realizan el seguimiento y la gestión de mercancías. Introduce contenedores flexibles como **cajas**, **palés** o **unidades de manipulación personalizadas**, que mantienen cada movimiento bajo control, desde la recepción hasta la reserva de stock en ventas.

    - Realizar el seguimiento de los productos en cada paso con trazabilidad en tiempo real y la unidad logística correcta.  
    - Crear y gestionar automáticamente cajas y palés de producto durante las operaciones de almacén.
    - Definir tipos de unidad logística y capacidades para ajustarse a los contenedores reales de cada producto.
    - Priorizar reservas y ventas por caja o palé

    ---
    - Documentación: [Stock Logistic Unit](../user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/stock-logistic-unit.md)

- :material-view-list: **Potencia de almacén de nueva generación: recepciones más inteligentes, productos trazables y control móvil completo**

    En la versión [3.3.0](./release-notes/etendo-classic/bundles/warehouse-extensions/release-notes.md) del bundle Warehouse Extensions, el módulo **Advanced Warehouse Management** evoluciona hacia un ecosistema completo para la logística moderna: más rápido, más preciso y totalmente trazable.  

    **Novedades:**

    - **Lectura de códigos de barras GS1-128** para identificar productos, lotes y fechas de caducidad en un solo escaneo.  
    - Gestión completa de **fechas de caducidad, lotes y unidades logísticas** (cajas y palés) para un control de stock preciso.  
    - Una nueva ventana **Inbound Receipt** para registrar fácilmente la mercancía entrante y asignarla a palés o cajas directamente a su llegada.  
    - Dos nuevas **tareas móviles de inventario** — *Inventory Adjustment* y *Inventory Relocation* — que simplifican las correcciones de almacén y los movimientos internos en tiempo real.
    
    ---
    - Documentación: [Advanced Warehouse Management](../user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management.md)

</div>
## Agosto 2025

### Financial Extensions

<div class="grid cards" markdown>

- :material-chart-bar: **Balance Sheet and P&L Report Advanced: informes más potentes**

    ---

    ![alt text](../assets/whats-new/etendo-news/balance-sheet-advanced.png){ width=500 align="right"}

    En la versión [3.3.0](./release-notes/etendo-classic/bundles/financial-extensions/release-notes.md) del bundle Financial Extensions, el **Balance Sheet and P&L Report Advanced** incorpora nuevas capacidades:

    - Añade soporte para dimensiones contables adicionales.
    - Permite comparaciones en paralelo de hasta cuatro años.

    ---

    - Documentación: [Balance Sheet and P&L Report Advanced](../user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools.md#balance-sheet-and-pl-structure-advanced)
    - Blog: [Desbloquee el poder del análisis financiero avanzado con Etendo](https://etendo.software/en/blog/unlock-the-power-of-advanced-financial-analysis-with-etendo/){target="_blank"}


</div>

### Platform Extensions

<div class="grid cards" markdown>

- :material-new-box: **Pruebe la Alpha de Etendo Main UI, la nueva interfaz de Etendo**

    ---

    ![new-ui](../assets/whats-new/etendo-news/new-ui.png){ width=500 align="right"}
    
    En la versión [3.7.1](./release-notes/etendo-classic/bundles/platform-extensions/release-notes.md) del bundle Platform Extensions, presentamos la versión Alpha de Etendo Main UI. Las primeras compilaciones incluyen 0.2.0, 0.4.0, 0.4.1 y 0.5.0.

    Descubra una experiencia elegante y moderna, diseñada para aumentar la productividad y simplificar las tareas diarias:

    - Nueva identidad visual que moderniza la plataforma.
    - Flujos de trabajo mejorados para potenciar todo lo que ya hace en Etendo.
    - Diseño contemporáneo e intuitivo para una navegación más rápida y mayor claridad.
    - Más funcional y más fácil de usar.

    ---

    - Pruébelo en el entorno de demostración: [Livebuilds](../live-builds/overview.md)
    - Documentación: [Instale Etendo Main UI](../developer-guide/etendo-classic/getting-started/installation/install-etendo-main-ui.md) hoy y ayude a dar forma a la experiencia Etendo de próxima generación.
    - Blog: [Ya puede probar la nueva interfaz de Etendo: descubra la versión Alpha](https://etendo.software/en/blog/you-can-now-try-etendos-new-interface-discover-the-alpha-version/)

</div>

<div class="grid cards" markdown>
- :octicons-package-16: **Potencie la observabilidad con OpenTelemetry en sus servicios dockerizados 🚀**

    En la versión [3.7.0](./release-notes/etendo-classic/bundles/platform-extensions/release-notes.md) del bundle Platform Extensions, se ha integrado OpenTelemetry para proporcionar observabilidad unificada para servicios dockerizados. Recopile métricas, trazas y logs en un único lugar para detectar picos de latencia, cuellos de botella y errores de comunicación antes de que afecten a los usuarios. Es compatible con exportadores y backends habituales para adaptarse a su stack de monitorización.

    Más información: [Cómo usar OpenTelemetry](../developer-guide/etendo-rx/how-to-guides/how-to-use-opentelemetry.md)

- :octicons-package-16: **Los Webhooks hacen que las integraciones sean más fáciles que nunca 🚀**
    
    A partir de la versión [3.7.0](./release-notes/etendo-classic/bundles/platform-extensions/release-notes.md) del bundle Platform Extensions, los [Webhooks](../developer-guide/etendo-classic/bundles/platform/etendo-webhooks.md) ya pueden usar **POST**. Esto significa que Etendo puede enviar automáticamente información a otras aplicaciones o servicios en tiempo real, haciendo que sus integraciones sean más rápidas y fluidas, sin complicaciones técnicas.

</div>
   
### Copilot Extensions

<div class="grid cards" markdown>

- :material-robot: **Etendo Copilot 3.5.0: más inteligente, más rápido y más fácil de usar 🚀**
    
    ---

    ![](../assets/whats-new/etendo-news/mcp.png){ width=500 align="right"}

    Con la versión [3.5.0](./release-notes/etendo-copilot/bundles/release-notes.md) del bundle Copilot Extensions, Copilot da un gran paso adelante. Estas son las novedades:

    -  **Conversaciones más potentes**: un nuevo chat a pantalla completa con selector de conversaciones facilita cambiar y hacer seguimiento de distintas tareas.  
    - **Herramientas más inteligentes**: nuevas herramientas como [Excel OCR](../developer-guide/etendo-copilot/available-tools/xls-ocr-tool.md) (leer datos desde imágenes de hojas de cálculo) y [Memory Tool](../developer-guide/etendo-copilot/available-tools/memory-tool.md) le ayudan a trabajar más rápido con datos complejos.  
    - **Mejores integraciones**: el nuevo soporte de MCP Server le permite conectar y gestionar herramientas externas y APIs de forma sencilla.
    ---

    - Documentación: [Cómo configurar servidores MCP en agentes](../developer-guide/etendo-copilot/how-to-guides/how-to-configure-mcp-servers-on-agents.md)
    - Blog: [¿Cansado de integraciones lentas y caras? Descubra cómo MCP está cambiando las reglas del juego](https://etendo.software/en/blog/discover-how-mcp-is-changing-the-game/){target="_blank"}
    - Blog: [Gmail al alcance de su mano con Etendo Copilot: productividad sin fricciones](https://etendo.software/en/blog/gmail-at-your-fingertips-with-etendo-copilot-seamless-productivity/){target="_blank"}
</div>

### Warehouse Extensions

<div class="grid cards" markdown>

- :material-view-list: **Potencia de almacén todo en uno: picking, packing y app móvil ahora en Etendo 25 🚀**

    Con la versión [3.2.2](./release-notes/etendo-classic/bundles/warehouse-extensions/release-notes.md) del bundle Warehouse Extensions, obtiene el paquete completo: picking más inteligente, packing más rápido y una app móvil para tomar el control desde cualquier lugar. 
    Optimice sus operaciones de almacén y entregue con rapidez y precisión — todo incluido en Etendo 25.

</div>
## Julio 2025

### Etendo

<div class="grid cards" markdown>
- :octicons-rocket-24: **¡Nueva versión de Etendo: ya está disponible la versión 25.2!**

    ¡Ya está aquí la última versión [25.2.x](./release-notes/etendo-classic/release-notes.md) de Etendo! Se han actualizado todos los módulos compatibles para una integración completa.  

</div>

### Copilot Extensions

<div class="grid cards" markdown>

- :material-robot: **Nuevo agente Invoice Supervisor: subir Factura (Proveedor) a Etendo nunca ha sido tan fácil**

    ![alt text](../assets/whats-new/etendo-news/invoice-supervisor.png)
    
    En la versión [3.1.0](./release-notes/etendo-copilot/bundles/release-notes.md) del bundle Copilot Extensions, se añade el agente **Invoice Supervisor** para crear automáticamente **Factura (Proveedor)** procesando múltiples PDF o imágenes empaquetadas en un ZIP. Gracias al OCR, extrae proveedor, número de factura, divisa, artículos, cantidades y totales, y luego los deja en borrador en Etendo para su revisión.

    - Documentación: [Invoice Supervisor](../user-guide/etendo-copilot/bundles/overview.md#invoice-supervisor)
    - Blog: [¿Cómo reduzco la carga operativa de mi equipo de compras? ¡Con el agente Invoice Supervisor!](https://etendo.software/en/blog/how-do-i-reduce-the-operational-burden-on-my-purchasing-team-with-agent-invoice-supervisor/){target="_blank"}

- :material-robot: **Las cargas masivas de datos son cosa del pasado: integración con Google Drive y Sheets en Copilot**

    ![alt text](../assets/whats-new/etendo-news/copilot-drive.png)
    En la versión [3.2.0](./release-notes/etendo-copilot/bundles/release-notes.md) del bundle Copilot Extensions, se añade la nueva funcionalidad para conectar Copilot con **Google Drive** y **Google Sheets** y utilizar agentes para crear **productos** o **terceros** de forma masiva desde una hoja de cálculo mediante el módulo **Mantenimiento**. Ideal para importaciones de datos a gran escala.

    - Documentación: [Data Initialization Supervisor](../user-guide/etendo-copilot/bundles/overview.md#data-initialization-supervisor)
    - Blog: [Carga masiva de datos en Etendo con Google Sheets: automatice y optimice con IA](https://etendo.software/en/blog/bulk-data-upload-in-etendo-with-google-sheets-automate-and-optimize-with-ai/){target="_blank"}

</div>

### Platform Extensions

<div class="grid cards" markdown>

- :octicons-package-16: **Impulse la productividad del equipo: conozca el nuevo módulo Mantenimiento**
    
    En la versión [2.14.0](./release-notes/etendo-classic/bundles/platform-extensions/release-notes.md) y [3.2.0](./release-notes/etendo-classic/bundles/platform-extensions/release-notes.md) del bundle Platform Extensions, se añadió el módulo [Mantenimiento](../user-guide/etendo-classic/optional-features/bundles/platform-extensions/task.md). Le permite organizar, automatizar y hacer seguimiento de los flujos de trabajo. Perfecto para equipos y agentes que necesitan una gestión estructurada de tareas.

- :octicons-package-16: **Etendo SSO: inicie sesión sin contraseñas** 

    ![alt text](../assets/whats-new/etendo-news/sso-login.png)
    
    En la versión [2.14.0](./release-notes/etendo-classic/bundles/platform-extensions/release-notes.md) y [3.2.0](./release-notes/etendo-classic/bundles/platform-extensions/release-notes.md) del bundle Platform Extensions, se añadió **Etendo SSO Login**, que habilita la autenticación **Single Sign-On**, simplificando el inicio de sesión de los usuarios y mejorando la seguridad mediante proveedores de identidad externos, como Google, Microsoft, LinkedIn, GitHub y Facebook.

    - Documentación: [Etendo SSO Login](../user-guide/etendo-classic/optional-features/bundles/platform-extensions/etendo-rx.md#etendo-sso-login)
    - Blog: [Etendo SSO: inicie sesión sin contraseñas y con total seguridad](https://etendo.software/en/blog/etendo-sso-log-in-without-passwords-and-with-complete-security/)

</div>

### Warehouse Extensions

<div class="grid cards" markdown>

- :material-view-list: **Picking List: precisión de preparación de pedidos que escala**

    Aumente su precisión y velocidad con el módulo [Picking List](../user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/picking.md), incluido en la versión [1.12.0](./release-notes/etendo-classic/bundles/warehouse-extensions/release-notes.md) del bundle Warehouse Extensions. Reserve stock al instante a medida que se generan las listas de picking, eliminando conflictos y agilizando los flujos de trabajo. Elija entre un picking de salida eficiente o un picking directo al cliente simplificado; en ambos casos, su equipo de almacén obtiene visibilidad estructurada y control sobre los pedidos pendientes. Precisión, planificación y rendimiento, todo en uno, para acelerar la entrega y la satisfacción del cliente.

- :fontawesome-solid-boxes-packing: **Packing: empaquetado optimizado, envíos sin errores**

    En la versión [1.12.0](./release-notes/etendo-classic/bundles/warehouse-extensions/release-notes.md) del bundle Warehouse Extensions, se añade el módulo [Packing](../user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/packing.md), diseñado para aportar estructura y velocidad al envío de mercancías. Una vez que se procesa un documento de salida de mercancías, el personal de almacén puede seleccionar la unidad de manipulación óptima (caja) para cada artículo, garantizando que cada producto quede correctamente embalado y listo para su expedición. Este módulo minimiza los errores de manipulación y mejora la organización de los envíos, aportando a su almacén el acabado profesional que merece cada pedido.

</div>

<div class="grid cards" markdown>

- :octicons-device-mobile-16: **Advanced Warehouse Management: inventario impulsado por móvil**

    ---

    ![alt text](../assets/whats-new/etendo-news/packing.png){ width=500 align="right"}

    En la versión [1.12.0](./release-notes/etendo-classic/bundles/warehouse-extensions/release-notes.md) del bundle Warehouse Extensions, desbloquee operaciones de almacén sin fricciones con el módulo [Advanced Warehouse Management](../user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management.md), una subaplicación móvil repleta de funcionalidades que se integra en profundidad con Etendo Mobile para ofrecer trazabilidad completa y operaciones de almacén automatizadas.
    
    - Escanee códigos de barras. 
    - Ejecute **ajustes de stock**.
    - Aplique **reubicación** y reglas automatizadas. 
    - Potencie sus flujos de **picking** y **packing**.
        
    Todo desde su dispositivo móvil. Cada acción se sincroniza en tiempo real con Etendo; diga adiós a los cuellos de botella y garantice datos consistentes en toda su operativa.

    - Blog: [Pedidos perfectos en minutos: el cambio que su almacén necesita se llama Etendo Mobile](https://etendo.software/en/blog/perfect-orders-in-minutes-the-change-your-warehouse-needs-is-called-etendo-mobile/){target="_blank"}

</div>
## Mayo 2025

### Etendo

<div class="grid cards" markdown>

- :octicons-rocket-24: **¡Nueva versión de Etendo: ya está disponible la versión 25.1!**

    ---

    <iframe align="right" width="560" height="315" src="https://www.youtube.com/embed/OtHb45n2dgU?si=dttVeLQxnf97HGjN" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

    ¡Ya está aquí la última versión [25.1.x](./release-notes/etendo-classic/release-notes.md) de Etendo! Esta versión incorpora actualizaciones de compatibilidad con **Java 17**, **PostgreSQL 16**, **Tomcat 9** y dependencias de terceros, garantizando una pila tecnológica moderna y robusta. Se han actualizado todos los módulos compatibles para una integración completa.  
    ¿Quiere saber más? Consulte la [guía de actualización para desarrolladores](../developer-guide/etendo-classic/developer-changelog/apichanges.md).

</div>

<div class="grid cards" markdown>

- :octicons-rocket-24: **Nuevos estados de envío y facturación en los pedidos de compra y albaranes (proveedor)**

    ---  
    Esta versión introduce una visibilidad mejorada en los procesos de aprovisionamiento. En la ventana [Pedido de compra](../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#purchase-order), la barra de estado ahora muestra los porcentajes de envío y facturación. A nivel de línea, verá cantidades detalladas de lo que se ha facturado y enviado.  
    Del mismo modo, la ventana [Albarán (Proveedor)](../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#goods-receipts) muestra los porcentajes de facturación tanto a nivel de cabecera como de línea.

- :octicons-rocket-24: **Excluya promociones y descuentos fácilmente con una simple casilla de verificación**

    ---
    Una nueva casilla de verificación en la sección *Más información* de las líneas de [Pedido de venta](../user-guide/etendo-classic/basic-features/sales-management/transactions.md#lines_1) y [Factura (Cliente)](../user-guide/etendo-classic/basic-features/sales-management/transactions.md#lines_5) permite a los usuarios **cancelar descuentos y promociones automáticos**. Esto le ofrece un mayor control sobre los precios a nivel de línea.

- :octicons-rocket-24: **Navegación mejorada en el proceso Crear facturas desde pedidos**

    ---
    Ahora es más fácil trabajar con pedidos. El proceso [Crear facturas desde pedidos](../user-guide/etendo-classic/basic-features/sales-management/transactions.md#create-invoices-from-orders) incluye mejoras de navegación que le permiten acceder a los pedidos filtrados de forma más eficiente.

- :octicons-rocket-24: **Anulación mejorada de la Factura (Proveedor) con referencia del proveedor**

    ---  
    Al anular una Factura (Proveedor), Etendo crea un documento inverso que ahora referencia el documento de anulación del proveedor. El proceso de [reactivación de factura](../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#reactivate) incluye un nuevo campo `Referencia del proveedor` para garantizar una trazabilidad clara y la alineación.

</div>
## Abril 2025

### Etendo

<div class="grid cards" markdown>

- :octicons-rocket-24: **Recuerde: puede simplificar el cálculo de comisiones con Etendo**

    ---

    Con **Etendo**, la gestión de las [comisiones de ventas](../user-guide/etendo-classic/basic-features/sales-management/setup/setup.md#commission) es más ágil y flexible. Las comisiones pueden calcularse en función de pedidos de venta o facturas, utilizando distintos criterios y filtros, como las cantidades vendidas o los importes facturados: 

    ![Criterios de comisión](../assets/whats-new/etendo-news/commission-criteria.png)

    Una vez calculadas, los pagos a los agentes de ventas pueden generarse automáticamente. 
    Puede configurar las comisiones para que se apliquen a todas las facturas o solo a las pagadas, y decidir si se incluyen las facturas sin un agente de ventas asignado.
    <br>
    --- 

    <iframe width="560" height="315" src="https://www.youtube.com/embed/vQGzo7cbCYQ?si=2zC3RQmYD1ImkoLo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

</div>

### Copilot Extensions

<div class="grid cards" markdown>

- :material-robot: **Copilot admite modelos de múltiples proveedores como OpenAI, Ollama, Anthropic y Deepseek, así como entrada de imágenes para modelos compatibles**

    ---

    ![texto alternativo](../assets/whats-new/etendo-news/multi-models-support.png)
    
    - En la versión [1.13.0](./release-notes/etendo-copilot/bundles/release-notes.md) del bundle Copilot Extensions, Etendo Copilot amplía sus capacidades al admitir múltiples proveedores, entre ellos:

        - **Anthropic**: se especializa en generación de código, lo que lo convierte en la mejor opción para tareas relacionadas con código.
        - **Deepseek**: una alternativa rentable para tareas generativas similares a OpenAI.
        - **Ollama (modelos autoalojados)**: ideal para usuarios que ejecutan sus propios modelos en su infraestructura.

    - Además, ahora las imágenes pueden ser procesadas directamente por los modelos de lenguaje sin necesidad de una herramienta independiente para el preprocesamiento.


</div>
## Marzo 2025

### Etendo Mobile

<div class="grid cards" markdown>

- :material-share: **Reciba y comparta archivos con Etendo Mobile**

    ---

    ![](../assets/whats-new/etendo-news/share-files-mobile.png)

    Se ha añadido una nueva funcionalidad a Etendo Mobile para agilizar la integración con aplicaciones externas. Con la nueva opción [Compartir archivos](../user-guide/etendo-mobile/), ahora puede recibir archivos desde aplicaciones externas y utilizarlos directamente en subaplicaciones como:

    - **Documents Manager**, donde puede ver archivos directamente en Etendo Mobile.
    - **Copilot**, donde agentes especializados pueden extraer información de imágenes, transformar audios en pedidos de venta y mucho más.

    Esta funcionalidad mejora el flujo de datos y la eficiencia en toda su plataforma.

    Pruébelo ahora usando el botón *Demo Try* en la aplicación, o descargue la última versión desde App Store o Play Store.

</div>

### Financial Extensions

<div class="grid cards" markdown>

- :material-chart-bar: **Ahora en los informes financieros avanzados puede ver dimensiones contables.**
    ---

    ![texto alternativo](../assets/whats-new/etendo-news/financial-reports-advanced.png)

    En la versión [1.25.0](./release-notes/etendo-classic/bundles/financial-extensions/release-notes.md) del bundle Financial Extensions, se incluyen mejoras en los informes financieros avanzados. En esta versión, el [General Ledger Report Advanced](../user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/#general-ledger-report-advanced) y el [Journal Entries Report Advanced](../user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/#journal-entries-report-advanced) le permitirán ver y filtrar por las dimensiones contables deseadas.
    Además, puede navegar a las entidades relacionadas en cada informe.

</div>

### Etendo

<div class="grid cards" markdown>

- :octicons-rocket-24: **¡25.1 Release Candidate ya disponible!**

    La nueva versión [25.1](./release-notes/etendo-classic/release-notes.md) de Etendo incorpora las últimas mejoras del stack. Aunque esta versión se encuentra actualmente en estado Release Candidate (RC), ya puede explorar el [registro de cambios de la API](../developer-guide/etendo-classic/developer-changelog/apichanges.md) detallado para revisar los cambios y mejoras incluidos en esta versión.

- :material-trending-up: **Incidencia corregida**
    
    ---
    A partir de la versión [24.3.7](./release-notes/etendo-classic/release-notes.md), se ha corregido un error que afectaba a los selectores desplegables en los informes dimensionales. En entornos que ejecutaban Etendo 24.3.6 o versiones anteriores, el primer registro en los cuadros combinados se mostraba incorrectamente, mostrando una concatenación de todos los valores en lugar del valor individual correcto. Este problema se debía a una gestión incorrecta de las etiquetas `<option>` en HTML.

    El error se ha resuelto en 24.3.7, y Etendo 24.4.0 o versiones posteriores no se vieron afectadas, ya que la refactorización para corregir el problema ya estaba incluida en esa versión. 
    
    *Consulte más detalles en la incidencia [#629](https://github.com/etendosoftware/etendo_core/issues/629)*.

</div>
## Febrero 2025

### Etendo ISO

<div class="grid cards" markdown>

- :material-trending-up: **Optimizaciones**
    
    ---
    A partir de la versión [24.4.3](https://etendo-appliances.s3.eu-west-1.amazonaws.com/etendo/iso/etendo-24Q4.3.iso), la ISO de Etendo incluye mejoras de rendimiento con ajustes optimizados de memoria y base de datos para mejorar la eficiencia del sistema. *Consulte más detalles en la incidencia [#573](https://github.com/etendosoftware/etendo_core/issues/573)*.

</div>

### Copilot Extensions

<div class="grid cards" markdown>

- :material-robot: **Ahora puede clonar agentes con un solo clic**

    ---

    ![copilot-clone.png](../assets/whats-new/etendo-news/copilot-clone.png)
    
    En la versión [1.12.0](./release-notes/etendo-copilot/bundles/release-notes.md) del bundle Copilot Extensions, se añade la funcionalidad para [clonar agentes](../user-guide/etendo-copilot/setup-and-usage.md#buttons) y bases de conocimiento, lo que le permite modificar y personalizar los asistentes de los agentes según sus necesidades.

</div>

<div class="grid cards" markdown>

-   :material-robot: **Mejoras en las bases de conocimiento de los agentes**

    --- 

    En la versión [1.12.0](./release-notes/etendo-copilot/bundles/release-notes.md) del bundle Copilot Extensions, se añaden nuevas capacidades:

    ![knowledge-base-files-news.png](../assets/whats-new/etendo-news/knowledge-base-files-news.png)

    Para más información, visite la documentación de la ventana [Archivo de base de conocimiento](../user-guide/etendo-copilot/setup-and-usage.md#knowledge-base-file-window).

</div>

### Financial Extensions

<div class="grid cards" markdown>

- :octicons-package-16: **Gestión de activos mejorada con dimensiones contables**

    ---

    ![dimension.png](../assets/whats-new/etendo-news/financial-dimension.png)

    En la versión [1.22.0](./release-notes/etendo-classic/bundles/financial-extensions/release-notes.md) del bundle Financial Extensions, el módulo [Accounting Dimensions Assets](../user-guide/etendo-classic/basic-features/financial-management/assets/overview.md#accounting-dimensions-assets) mejora la gestión de activos al permitir a los usuarios asignar dimensiones contables a los activos, como Terceros, Actividad y Centro de costos, entre otras. Estas dimensiones se transfieren a las líneas de amortización. Además, las amortizaciones ahora se agrupan por período (mensual o anual), mejorando la precisión de los informes financieros y garantizando un seguimiento coherente de la depreciación de activos.

- :octicons-package-16: **Obtenga un mejor control con la ventana Documentos no contabilizados**

    ---

    ![](../assets/whats-new/etendo-news/financial-not-posted.png)

    En la versión [1.22.0](./release-notes/etendo-classic/bundles/financial-extensions/release-notes.md) del bundle Financial Extensions, con la última versión de [Contabilización masiva](../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md#not-posted-documents-window), la ventana Documentos no contabilizados proporciona una vista completa de todas las transacciones financieras completadas que aún no se han contabilizado. Este informe garantiza que no se pasen por alto transacciones pendientes antes de cerrar un período contable o ejecutar informes financieros.

    Los usuarios pueden filtrar por rango de fechas y navegar directamente a documentos no contabilizados, incluidos asientos, facturas, pagos y transacciones financieras, entre otros, agilizando el proceso de contabilización.

</div>
## Enero 2025

### Copilot Extensions 

<div class="grid cards" markdown>

- :material-robot: **Ahora puede usar varios archivos en conversaciones con un agente**

    ---

    ![](../assets/whats-new/etendo-news/attach-multiple-files-copilot.png)

    En la versión [1.10.0](./release-notes/etendo-copilot/bundles/release-notes.md) del bundle Copilot Extensions, se han añadido nuevas funcionalidades:

</div>

<div class="grid cards" markdown>

-   :material-robot: **[Subir varios archivos](../user-guide/etendo-copilot/getting-started.md#attach-files)**
    
    ---
    
    Ahora es posible adjuntar varios archivos a la vez en Etendo Copilot, optimizando la gestión documental y mejorando la experiencia de usuario.

-   :octicons-package-16: **Gestión automática de permisos**
    
    ---

    Al crear un nuevo agente, los permisos necesarios se generarán automáticamente para su ejecución en el rol actual, reduciendo la fricción en la configuración.

-   :octicons-package-16: **Visualización optimizada**
    
    ---
    
    La ventana del agente ahora muestra el módulo al que pertenece cada agente, mejorando la organización y la navegación.

-  :material-tools: **Tool Pack: Nueva herramienta para leer archivos Excel y CSV** 
    
    ---
    
    Se ha añadido [XLS Tool](../developer-guide/etendo-copilot/available-tools/xls-tool.md) en las herramientas disponibles, lo que permite a los agentes leer y procesar datos directamente desde archivos Excel o CSV, facilitando la automatización y la integración de información estructurada.

</div>
## Diciembre 2024

### Etendo

<div class="grid cards" markdown>

- :octicons-rocket-24: **¡Nueva versión de Etendo: ya está disponible la versión 24.4!**

    Se ha publicado la versión [24.4.0](./release-notes/etendo-classic/release-notes.md) de Etendo para el último trimestre del año. Se han actualizado todos los paquetes para garantizar la integración con esta nueva versión. Además, esta versión incluye todos los errores corregidos durante el trimestre.

- **El proceso de completado de documentos permite de nuevo el uso de Pago a crédito como método de pago.** 

    A partir de ahora, el completado vuelve a ser de un registro cada vez y se añade al botón [Bulk Completion](../user-guide/etendo-classic/optional-features/bundles/essentials-extensions/bulk-completion.md) instalando el bundle Essentials Extensions.

</div>

### Essentials Extensions

<div class="grid cards" markdown>

- :octicons-package-16: **Gestionar documentos nunca había sido tan rápido y fácil**

    ![](../assets/whats-new/etendo-news/bulk-completion.png)
    
    En la versión [1.7.0](./release-notes/etendo-classic/bundles/essentials-extensions/release-notes.md) del bundle Essentials Extensions, puede gestionar sin esfuerzo múltiples registros con la funcionalidad [Bulk Completion](../user-guide/etendo-classic/optional-features/bundles/essentials-extensions/bulk-completion.md). Seleccione los registros que desea completar, reactivar o cerrar, y procéselos todos a la vez con un solo clic.
</div>


### Warehouse Extensions

<div class="grid cards" markdown>

- :octicons-package-16: **Reserva automática de stock más precisa**

    ![](../assets/whats-new/etendo-news/automatic-warehouse-reservation.png)

    En la versión [1.10.0](./release-notes/etendo-classic/bundles/warehouse-extensions/release-notes.md) del bundle Warehouse Extensions, con el módulo [Automatic Warehouse Reservation](../user-guide/etendo-classic/optional-features/bundles/warehouse-extensions/overview.md#automated-warehouse-reservation), las reservas de stock pueden limitarse únicamente al almacén especificado en la cabecera del pedido. De este modo, puede asegurarse de que sus pedidos utilicen siempre el almacén correcto.
</div>

### Financial Extensions

<div class="grid cards" markdown>

- :octicons-package-16: **Remesas automatizadas: simplifique la gestión de remesas automatizando el proceso de liquidación y protesto.**

    ---

    ![](../assets/whats-new/etendo-news/automated-remittances.png)

    En la versión [1.21.0](./release-notes/etendo-classic/bundles/financial-extensions/release-notes.md) del bundle Financial Extensions, con el módulo [Automated remittances](../user-guide/etendo-classic/optional-features/bundles/financial-extensions/automated-remittance.md), al procesar remesas se crean instrucciones bancarias y se liquidan automáticamente con la fecha actual. 

    También se ha añadido el botón Protest Remittance, lo que permite devolver recibos en remesas de cobro desde un único lugar.

- :octicons-package-16: **La gestión de cuentas bancarias y pagos permite una mayor automatización**
    
    --- 

    ![](../assets/whats-new/etendo-news/advanced-bank-account.png )

    En la versión [1.21.0](./release-notes/etendo-classic/bundles/financial-extensions/release-notes.md) del bundle Financial Extensions, con el módulo [Advanced Bank Account Management](../user-guide/etendo-classic/optional-features/bundles/financial-extensions/advanced-bank-account-management.md), se ha añadido la posibilidad de establecer una cuenta bancaria por defecto en la configuración de terceros, así como de definir cuentas bancarias para cada ubicación. 
    También se ha añadido la posibilidad de seleccionar la cuenta bancaria al añadir pagos e incluso editar planes de pago con el botón Modify Payment.
</div>

### Copilot Extensions 

<div class="grid cards" markdown>

- :material-robot: **Copilot permite el uso de múltiples modelos de IA de distintos proveedores.**
    
    ---

    En la versión [1.9.0](./release-notes/etendo-copilot/bundles/release-notes.md) del bundle Copilot Extensions, se ha añadido el tipo de asistente Multi-Model Assistant; estos agentes amplían el tipo `Langchain` con la particularidad de que puede utilizarse con modelos de varios proveedores como Anthropic o Gemini, además de los modelos OpenAI existentes.
    Además, se ha añadido la ventana AI Models, donde el usuario puede gestionar los modelos que utilizarán los distintos agentes.
</div>
## Noviembre 2024

### Copilot Extensions

:material-robot: **¡Nueva versión de Etendo Copilot disponible!**

Nueva versión del bundle Copilot Extensions [1.8.0](./release-notes/etendo-copilot/bundles/release-notes.md) 

<div class="grid cards" markdown>
-  **Mejore el desarrollo de sus herramientas Python con el agente Code Run**

    ---
    El agente [Code Run](../developer-guide/etendo-copilot/bundles/dev-assistant.md#code-run), combinado con la herramienta [Docker Tool](../developer-guide/etendo-copilot/available-tools/docker-tool.md), introduce una forma segura y eficiente de ejecutar código Python y Bash dentro de contenedores Docker aislados. Esta herramienta revoluciona la manera en que se gestionan las tareas de programación. El asistente se especializa en gestionar contenedores Docker para ejecutar scripts de Python, garantizando un entorno fiable y aislado.

    Equipado con capacidades avanzadas, el agente prioriza Python para la resolución de incidencias, gestiona dinámicamente las instalaciones de librerías, integra comandos Bash para operaciones flexibles y gestiona el procesamiento de archivos con precisión. Tanto si está resolviendo incidencias, automatizando tareas o probando scripts, esta herramienta garantiza eficiencia y seguridad. Transforme su flujo de trabajo de desarrollo con esta potente incorporación a Etendo.
</div>
## Octubre 2024

### Copilot Extensions

:material-robot: **¡Nueva versión de Etendo Copilot disponible!**

Nueva versión del bundle Copilot Extensions [1.7.0](./release-notes/etendo-copilot/bundles/release-notes.md)  

<div class="grid cards" markdown>
-  **¡Impulse su flujo de trabajo de desarrollo con el nuevo Dev Assistant!**

    ---
    El módulo [Dev Assistant](../developer-guide/etendo-copilot/bundles/dev-assistant.md) optimiza y acelera su flujo de trabajo de desarrollo en Etendo. Con agentes especializados, ahora puede crear fácilmente botones, ventanas, solapas, tablas, controladores de eventos, informes Jasper y procesos en segundo plano. 

    Estos agentes están diseñados para mejorar la productividad y reducir la complejidad, permitiendo una gestión y construcción eficientes de todos los componentes dentro de Etendo. ¡Lleve su proceso de desarrollo al siguiente nivel!
</div>

<div class="grid cards" markdown>
-  **Copilot en móvil: ¡pruebe Copilot en sus dispositivos móviles y tabletas!**

    ---
    La nueva [subaplicación Etendo Copilot](../user-guide/etendo-copilot/bundles/overview.md#etendo-copilot-subapp) le permite interactuar con agentes impulsados por IA desde cualquier lugar. Ahora puede adjuntar archivos, acceder a ventanas específicas por rol y recibir asistencia personalizada en tiempo real directamente en su móvil o tableta. Disfrute de una integración fluida con todas las funcionalidades habituales de Etendo, ¡al alcance de su mano!

</div>

### Dependency Manager
:octicons-package-16: **Gestionar los módulos y dependencias de Etendo nunca ha sido tan fácil**
![](../assets/whats-new/etendo-news/devassistant.png)

El módulo [Dependency Manager](../developer-guide/etendo-classic/getting-started/installation/dependency-manager.md) permite a los usuarios acceder a todos los paquetes publicados en los repositorios de Etendo Software directamente desde la interfaz de Etendo. Con la ventana de Gestión de dependencias, puede explorar los bundles disponibles, comprobar los detalles de versión y las dependencias, e instalar nuevos paquetes fácilmente. El módulo también permite actualizar, eliminar y modificar los módulos instalados, ofreciéndole un control total sobre su entorno.
## Septiembre 2024

### Etendo

:octicons-rocket-24: **¡Nueva versión de Etendo: ya está disponible la versión 24.3!**

Se ha publicado la versión [24.3.0](./release-notes/etendo-classic/release-notes.md) de Etendo para el tercer trimestre del año. Se han actualizado todos los paquetes para garantizar la integración con esta nueva versión. Además, esta versión incluye todos los errores corregidos durante el trimestre.

### Copilot Extensions

:material-robot: **¡Nueva versión de Etendo Copilot disponible!**

Nueva versión del bundle Copilot Extensions [1.5.0](./release-notes/etendo-copilot/bundles/release-notes.md)  

<div class="grid cards" markdown>
- **Nueva actualización de funcionalidad: compatibilidad con archivos Zip para agentes LangChain**
    
    ![](../assets/whats-new/etendo-news/LangChain.png)

    Nos complace anunciar una nueva funcionalidad en los agentes LangChain: la posibilidad de subir archivos `.zip` directamente a la base de conocimiento. Estos archivos `.zip` pueden contener una variedad de formatos, incluidos `.txt`, `.pdf`, `.md`, `.py`, `.java` y `.js`.
    Esta mejora permite a los desarrolladores entrenar agentes con código fuente de ejemplo.
    ¡Potencie las capacidades de su agente con esta potente nueva funcionalidad!

</div>
## Agosto 2024

### Copilot Extensions

[:material-robot: **¡Nueva versión de Etendo Copilot disponible!**](../user-guide/etendo-copilot/getting-started.md): Aumente su productividad

![](../assets/whats-new/etendo-news/copilot.png)

La versión más reciente [1.4.0](./release-notes/etendo-copilot/bundles/release-notes.md) del bundle Copilot Extensions incorpora las siguientes mejoras clave en Etendo Copilot:

<div class="grid cards" markdown>

-   **Nuevas capacidades:**
    
    ---
    - **Consultas a base de datos:** Utilice consultas a la base de datos del sistema como bases de conocimiento para automatizar tareas bajo condiciones específicas.
    -  **Copilot Stream:** Realice el seguimiento en tiempo real de qué agente o herramienta está trabajando.
    -  **UX mejorada:** El chat ahora conserva el último agente utilizado para una interacción fluida.

-   **Actualizaciones de agentes:**
    
    ---
    -  **Agentes Langchain:** Ahora gestionan bases de conocimiento locales, manteniendo sus datos seguros.
    -  **Agentes LangGraph:** Gestione un equipo de agentes, delegando tareas de forma eficiente. 
     
</div>

Estas actualizaciones hacen que Etendo Copilot sea más potente, seguro y fácil de usar, impulsando la eficiencia a nuevos niveles.


### Platform Extensions

[:simple-docker: **Gestión de Docker**](../developer-guide/etendo-classic/bundles/platform/docker-management.md)

![](../assets/whats-new/etendo-news/docker.gif){align=right width=400}

- En la versión [1.18.0](./release-notes/etendo-classic/bundles/platform-extensions/release-notes.md) del bundle Platform Extensions, se ha introducido el nuevo módulo **Gestión de Docker**.
- Este módulo simplifica el despliegue de servicios al permitirle configurar toda la infraestructura que su servicio requiere mediante módulos de Etendo.
- El servicio de base de datos PostgreSQL está incluido en el módulo, haciendo que la instalación del servicio sea más rápida y sencilla que nunca.

[:simple-apachetomcat: **Servicio Tomcat dockerizado**](../developer-guide/etendo-classic/bundles/platform/dockerized-tomcat-service.md)

- En la versión [1.18.0](./release-notes/etendo-classic/bundles/platform-extensions/release-notes.md) del bundle Platform Extensions, se ha introducido el nuevo módulo **Servicio Tomcat dockerizado**, que simplifica la instalación de Etendo en cualquier servidor.
- Con este módulo, la configuración de Etendo se convierte en un proceso rápido y directo, eliminando las complejidades típicamente asociadas a la configuración del servidor. 



### Warehouse Extensions
[:octicons-package-16: **Operaciones de producto**](../user-guide/etendo-classic/optional-features/bundles/procurement-extensions/purchase-invoice-validation.md)

![](../assets/whats-new/etendo-news/product-operation.png)

En la versión [1.8.0](./release-notes/etendo-classic/bundles/warehouse-extensions/release-notes.md) del bundle Warehouse Extensions, se ha incluido la funcionalidad **Operaciones de producto**. Este módulo le permite centralizar y controlar todos los movimientos de producto con Operaciones de producto. Visualice cada transacción, desde envíos y recepciones hasta costes y ubicación, en un único lugar. Simplifique el análisis y obtenga una visión clara del rendimiento de sus operaciones.
## Julio 2024

### Copilot Extensions

<div class="grid cards" markdown>

-   [:material-tools: **Tool Pack**](../developer-guide/etendo-copilot/available-tools/overview.md)

    ---
    
    El módulo Tool Pack, disponible desde la versión [1.3.1](./release-notes/etendo-copilot/bundles/release-notes.md) del bundle Etendo Copilot, incluye una colección de herramientas diseñadas para mejorar las capacidades de los agentes de Etendo Copilot. Este módulo habilita funcionalidades como la lectura y escritura de archivos, la navegación por directorios y el envío de correos electrónicos, ampliando significativamente el alcance operativo de los agentes.

-   [:material-tools: **OCR Tool**](../developer-guide/etendo-copilot/available-tools/ocr-tool.md)

    ---

    Desde la versión [1.3.0](./release-notes/etendo-copilot/bundles/release-notes.md) del bundle Copilot Extensions, se ha incluido la posibilidad de añadir un parámetro a la herramienta OCR Tool para especificar y detallar el análisis sobre imágenes, y se ha añadido la herramienta lectora Codbar a la herramienta capaz de leer códigos de barras en imágenes.

-   [:material-robot: **Purchase Expert**](../user-guide/etendo-copilot/bundles/copilot-purchase-expert.md)
    
    ---   

    A partir de la versión [1.3.0](./release-notes/etendo-copilot/bundles/release-notes.md) del bundle Copilot, se incluyó la herramienta [Attach File tool](../developer-guide/etendo-copilot/available-tools/attach-file-tool.md), una herramienta capaz de añadir adjuntos a cualquier registro en Etendo.

-   [:material-robot: **Dev Assistant**](../developer-guide/etendo-copilot/bundles/dev-assistant.md)

    ---

    Desde la versión [1.1.0](./release-notes/etendo-copilot/bundles/release-notes.md) en adelante, se incluyó el agente [Reference Creator](../developer-guide/etendo-copilot/bundles/dev-assistant.md#reference-creator), capaz de crear referencias de tipo lista para ser utilizadas en el proceso de desarrollo.

</div>

:material-bug: **Incidencias corregidas**

En la versión [1.2.1](./release-notes/etendo-copilot/bundles/release-notes.md), se ha resuelto la incidencia [#5](https://github.com/etendosoftware/com.etendoerp.copilot.extensions/issues/5){target="_blank"}, que provocaba un renderizado incorrecto de los saltos de línea en los bloques de código.

### Financial Extensions

[:octicons-package-16: **Regularización de IVA**](../user-guide/etendo-classic/optional-features/bundles/financial-extensions/overview.md/#vat-regularization)

En la versión [1.16.1](./release-notes/etendo-classic/bundles/financial-extensions/release-notes.md) de este bundle, se ha incluido el módulo [Regularización de IVA](../user-guide/etendo-classic/optional-features/bundles/financial-extensions/overview.md/#vat-regularization), que le permite **ajustar fácilmente las cuentas** para garantizar que **se ajuste el saldo de IVA**.

---
## Junio 2024

### Etendo

:octicons-rocket-24: **¡Nueva versión disponible!**

Se ha publicado la versión [24.2.0](./release-notes/etendo-classic/release-notes.md) de Etendo, correspondiente al segundo trimestre del año. Se han actualizado todos los bundles para garantizar una integración fluida con esta nueva versión.

:material-bug: **Incidencias corregidas**

En la versión [24.1.8](./release-notes/etendo-classic/release-notes.md), se ha resuelto la incidencia [#270](https://github.com/etendosoftware/etendo_core/issues/270){target="_blank"}, que provocaba la **ejecución inesperada de callouts** en la ventana **Pedido de venta**.

### Copilot Extensions

:material-trending-up: **Optimizaciones**

A partir de la versión [1.2.0](./release-notes/etendo-copilot/bundles/release-notes.md) de este paquete, se han corregido errores y se han realizado mejoras de estabilidad en Copilot. Esta actualización también introduce mejoras visuales en el chat, al permitir introducir **texto en más de una línea**.

### Financial Extensions

[:octicons-package-16: **Clonación de asiento del libro mayor**](../user-guide/etendo-classic/basic-features/financial-management/accounting/transactions.md/#gl-journal-clone)

A partir de la versión [1.15.0](./release-notes/etendo-classic/bundles/financial-extensions/release-notes.md) de este bundle, se incluye el módulo GL Journal Clone, que permite clonar el Asiento simple del libro mayor.

---
## Mayo 2024

### Copilot Extensions

[:material-robot: **Experto SQL**](../user-guide/etendo-copilot/bundles/sql-expert.md)

En la versión [1.1.0](./release-notes/etendo-copilot/bundles/release-notes.md) del bundle Copilot Extensions, se ha incluido el Experto SQL.  
Con este agente, se le permitirá **formular preguntas** en lenguaje natural, y el sistema generará automáticamente la consulta SQL necesaria para devolver los datos en código o en lenguaje natural.

---
## Abril 2024

### Copilot Extensions

[:material-robot: **Agente Purchase Expert**](../user-guide/etendo-copilot/bundles/overview.md#order-expert)

En la versión [1.1.0](./release-notes/etendo-copilot/bundles/release-notes.md) del bundle Copilot Extensions, se ha incluido el Agente Purchase Expert.
Sus pedidos de compra se simplifican con el nuevo agente de Copilot. Interactúe mediante **texto o subiendo imágenes o PDFs** con los datos del pedido de compra, y el agente generará automáticamente un borrador.

### Localización española

:material-trending-up: **Optimizaciones**

A partir de la versión [1.9.4](./release-notes/etendo-classic/bundles/localization-spain-extensions/release-notes.md) de este bundle, hemos simplificado el mantenimiento sustituyendo las dependencias de los módulos `org.openbravo.util.saaj.impl` y `org.openbravo.util.javax.xml.soap` por las nuevas dependencias Maven [Jakarta SOAP Implementation](https://mvnrepository.com/artifact/com.sun.xml.messaging.saaj/saaj-impl/1.5.3){target="_blank"} y [Jakarta SOAP with Attachments API](https://mvnrepository.com/artifact/jakarta.xml.soap/jakarta.xml.soap-api/1.4.2){target="_blank"}.

Para aprovechar estas mejoras, al actualizar a la versión [1.9.4](./release-notes/etendo-classic/bundles/localization-spain-extensions/release-notes.md) o superior, asegúrese de eliminar manualmente los módulos antiguos del directorio `/modules` para que la nueva compilación utilice las nuevas dependencias.

---
## Marzo 2024

### Etendo

:material-trending-up: **Optimizaciones**

A partir de la versión [24.1.0](./release-notes/etendo-classic/release-notes.md), se ha actualizado el soporte para [Tomcat 9](https://tomcat.apache.org/download-90.cgi){target="_blank"}.

### Copilot Extensions

[:material-tools: **OCR Tool**](../developer-guide/etendo-copilot/available-tools/ocr-tool.md)

En la versión [1.0.0](./release-notes/etendo-copilot/bundles/release-notes.md) del bundle Copilot Extensions, se ha incluido la herramienta OCR Tool.
Con esta herramienta diseñada para el **reconocimiento óptico de caracteres**, podrá extraer texto de imágenes o archivos PDF.

### Procurement Extensions

[:octicons-package-16: **Purchase Invoice Validation**](../user-guide/etendo-classic/optional-features/bundles/procurement-extensions/purchase-invoice-validation.md)

En la versión [1.0.0](./release-notes/etendo-classic/bundles/procurement-extensions/release-notes.md) del bundle Procurement Extensions, se ha incluido la funcionalidad Purchase Invoice Validation. Ahora, podrá **evitar la duplicación de Factura (Proveedor)** mediante reglas establecidas y validaciones automáticas.

### Platform Extensions

:material-trending-up: **Optimizaciones**

A partir de la versión [1.13.2](./release-notes/etendo-classic/bundles/platform-extensions/release-notes.md) de este bundle, se ha eliminado la dependencia del módulo `org.openbravo.util.javax.xml.soap` ya que no era necesaria para ningún módulo de este bundle. En caso de que esta dependencia sea necesaria para el desarrollo, recomendamos utilizar la dependencia de Maven [Jakarta SOAP with Attachments API](https://mvnrepository.com/artifact/jakarta.xml.soap/jakarta.xml.soap-api/1.4.2){target="_blank"}.

---
Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L](https://etendo.software){target="_blank"}.