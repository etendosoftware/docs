---
title: Ventana Modificación de precios
tags:
  - Master Data Management
  - Etendo Classic
  - Pricing
  - Discount
  - Promotions
---

## Ventana Modificación de precios { #discounts-and-promotions-window }

:material-menu: `Aplicación` > `Gestión de Datos Maestros` > `Tarifas` > `Modificación de precios`

### Visión general { #overview }

Modificación de precios es una funcionalidad flexible que le permite ajustar automáticamente los precios en las líneas de pedidos y facturas según reglas de negocio configurables. Puede definir cuándo y cómo se aplican las promociones usando filtros (como Terceros, Productos, Tarifas y Características), configurar el tipo de descuento (porcentaje, importe fijo o precio fijo) y controlar la disponibilidad de la promoción por día y hora. Se pueden aplicar múltiples promociones en una cascada priorizada. La configuración también permite traducir los nombres de las promociones y realizar el seguimiento de los descuentos aplicados en documentos procesados mediante una solapa opcional de solo lectura.

### Cabecera { #header }
Define la configuración principal y las condiciones para aplicar Modificación de precios a pedidos y facturas.

![alt text](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/pricing/discounts-and-promotions/discounts-and-promotions-1.png)

Campos a tener en cuenta:

#### Sección principal { #main-section }

- **Organización**: Organización para la que el descuento o la promoción estará disponible.
- **Tipo de descuento/promoción**: Define el tipo de regla utilizada para ajustar precios. Por defecto, Etendo incluye el tipo _Ajuste de precios_, pero es posible ampliar y añadir tipos personalizados según las necesidades de la organización.
- **Nombre**: Identificador interno de la promoción.
- **Nombre impreso**: Etiqueta mostrada a los usuarios finales y en informes. Si está vacío, toma como valor por defecto el Nombre.
- **Descripción**: Texto corto opcional que describe la promoción (hasta 255 caracteres).
- **Activo**: Habilita la promoción para su uso. Los registros inactivos se conservan para auditoría/informes.

#### Opciones del Filtro { #filter-options }

- **Fecha de inicio**: Fecha en la que la promoción pasa a ser válida.
- **Fecha final**: Fecha hasta la que la promoción permanece válida (inclusive).
- **Prioridad**: Orden de aplicación cuando se aplican varias promociones. Número menor = mayor prioridad.
- **Aplicar próximo descuento/promoción**: Si está marcado, también se aplicarán las promociones posteriores que correspondan.
- **Filtro**:

    Cada uno de los siguientes campos admite dos métodos de filtrado que definen cómo se tratarán los registros relacionados configurados en las solapas durante la evaluación de la promoción. Estas opciones proporcionan flexibilidad para definir el alcance de una promoción en relación con Terceros, Productos, Tarifas y Organizaciones.

    - **Modo selección Grupo Terceros**
    - **Conjunto de Terceros Incluidos**
    - **Modo selección terceros**
    - **Modo selección Categoría de producto**
    - **Modo selección de producto**
    - **Modo selección Tarifas**
    - **Organizaciones incluidas**
    - **Referencias Externas al Tercero Incluídas**

        | Método                    | Descripción                                                                                                   |
        |---------------------------|---------------------------------------------------------------------------------------------------------------|
        | **Todos excepto los definidos** | **(Valor por defecto)** La promoción se aplica a todos los registros **excepto** a los listados en la solapa correspondiente. |
        | **Solo los definidos**    | La promoción se aplica **solo** a los registros listados en la solapa correspondiente.                       |

    Algunos filtros tienen métodos de filtrado diferentes, que se describen a continuación:

    - **Características Incluidas**: Define cómo se filtran las características del producto para aplicar la promoción. Hay tres métodos disponibles:
    
        | Método                        | Descripción                                                                                 |
        |-------------------------------|---------------------------------------------------------------------------------------------|
        | **Todas las características** | **(Valor por defecto)** La promoción se aplica independientemente de las características del producto. |
        | **Todos los valores definidos** | El producto debe coincidir con **todas** las características definidas para que se aplique la promoción. |
        | **Cualquiera de los definidos** | El producto debe coincidir con **cualquiera** de las características definidas para que se aplique la promoción. |

    - **Excluir Características**: Define cómo se filtran las características del producto para excluir la promoción. Hay dos métodos disponibles:

        | Método                        | Descripción                                                                                                   |
        |-------------------------------|---------------------------------------------------------------------------------------------------------------|
        | **Todos los valores definidos** | **(Valor por defecto)** El producto debe coincidir con **todas** las características definidas para que no se aplique la promoción. |
        | **Cualquiera de los definidos** | El producto debe coincidir con **cualquiera** de las características definidas para que no se aplique la promoción. |

#### Definición { #definition }

- **% de descuento**: Porcentaje de descuento a aplicar al precio.
- **Importe del descuento**: Importe fijo a restar del precio.
- **Fijo precio estándar**: Precio final asignado al producto cuando se aplica la promoción.
- **Cantidad desde**: Cantidad mínima requerida para que se aplique la promoción.
- **Cant. hasta**: Cantidad máxima elegible para la promoción.
- **Es múltiple**: El descuento se aplica solo si la cantidad es múltiplo de un valor definido.
    - **Unidades por paquete**: Esta opción se muestra solo si _Es múltiple_ está habilitado. Define el número de unidades consideradas por paquete.

#### Disponibilidad { #availability }
Esta sección define los días y horas en los que la promoción está activa. Si no se configura ninguna disponibilidad, la promoción se aplicará siempre.

- **Toda la semana**: Indicador para habilitar la promoción durante toda la semana.
    - **Comienzo**: Hora de inicio diaria de la promoción.
    - **Fin**: Hora de fin diaria de la promoción.
- **Lunes – Domingo**: Indicadores para habilitar la promoción en días concretos de la semana.
    - **Comienzo**: Hora de inicio para el día de la semana especificado.
    - **Fin**: Hora de fin para el día de la semana especificado.

### Solapa { #tabs }

- **Traducción**: Permite definir el idioma, así como el **Nombre** y el **Nombre impreso** traducidos correspondientes para cada idioma.
- **Grupos de Terceros**: Permite incluir o excluir Grupos de Terceros de una promoción o descuento.
- **Terceros**: Permite incluir o excluir Terceros específicos de una promoción o descuento.
- **Conjunto de Terceros**: Permite definir Conjuntos de Terceros a los que se aplicará una promoción o descuento.
- **Categoría del producto**: Permite incluir o excluir Categorías del producto de una promoción o descuento.
- **Productos**: Permite incluir o excluir Productos individuales de una promoción o descuento.
- **Tarifa**: Permite seleccionar Tarifas para incluir o excluir de una promoción o descuento.
- **Organización**: Permite seleccionar Organizaciones para incluir o excluir de una promoción o descuento.
- **Características**: Permite seleccionar Características del producto a incluir en una promoción o descuento.
- **Excluir Características**: Permite seleccionar Características del producto a excluir de una promoción o descuento.
- **Tercero Externo** Permite seleccionar Tercero Externo para incluir o excluir de una promoción o descuento.

### Botones { #buttons }

- **Añadir Organizaciones**: Añade registros de Organización en la solapa *Organización* para incluirlos o excluirlos de la promoción.
    ![alt text](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/pricing/discounts-and-promotions/discounts-and-promotions-2.png)
- **Añadir Categorías de Productos**: Añade registros de Categoría del producto en la solapa *Categoría del producto* para incluirlos o excluirlos de la promoción.
    ![alt text](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/pricing/discounts-and-promotions/discounts-and-promotions-3.png)
- **Añadir Productos**: Añade registros de Producto en la solapa *Productos* para incluirlos o excluirlos de la promoción.
    ![alt text](../../../../../../assets/user-guide/etendo-classic/basic-features/master-data-management/pricing/discounts-and-promotions/discounts-and-promotions-4.png)

### ¿Cómo se definen las promociones? { #how-promotions-are-defined }

El proceso para configurar una promoción es sencillo:

1. **Identificar la promoción**: Use los campos **Nombre** y **Nombre impreso** para identificar la promoción. _Nombre impreso_ se mostrará al usuario final, mientras que _Nombre_ se usa internamente.

2. **Definir el periodo activo**: Configure **Fecha de inicio** y **Fecha final** para definir cuándo será válida la promoción.

3. **Controlar la prioridad y la cascada de la promoción**: Use **Prioridad** para determinar el orden en el que se aplicarán las promociones si hay más de una válida. Habilite **Aplicar próximo descuento/promoción** si desea que se apliquen promociones posteriores después de esta.

4. **Configurar filtros**: Use la sección **Opciones del Filtro** para determinar dónde se aplica la promoción:
    - Seleccione el **método de inclusión** para cada filtro (Terceros, Productos, Tarifas, Características y Organizaciones).
    - Defina los valores reales del filtro en las sub-solapas correspondientes o use los botones disponibles.

    !!! tip
        La configuración de filtros es clave para garantizar que la promoción se aplique solo en los escenarios previstos.

5. **Definir la lógica del descuento**: En la sección **Definición**, configure el descuento:
    - **Importe del descuento** y/o **% de descuento** para ajustar el precio.
    - **Fijo precio estándar** para sobrescribir el precio final.
    - **Cantidades mínima y máxima** para aplicar la promoción solo para determinadas cantidades.

    !!! tip
        Use **Fijo precio estándar** para promociones que deban forzar un precio específico, y **Cantidades mínima/máxima** para promociones basadas en volumen.

6. **Establecer la disponibilidad de la promoción (opcional)**: En la sección **Disponibilidad**, configure cuándo estará activa la promoción; si no se configura ninguna disponibilidad, la promoción se aplicará siempre:

    - Use **Toda la semana** para aplicar la promoción todos los días.
    - Opcionalmente, habilite días individuales (**Lunes** a **Domingo**) para ajustar con precisión cuándo está activa la promoción.
    - Para cada día (o Toda la semana), configure **Comienzo** y **Fin** para definir el rango horario válido.

    !!! tip
        Configurar la disponibilidad garantiza que las promociones se apliquen correctamente según el horario comercial, días especiales o estrategias de marketing basadas en el tiempo.

### ¿Cómo se aplican las promociones? { #how-promotions-are-applied }

Las reglas de descuento y promoción se aplican automáticamente a las [Línea pedido de venta](../../sales-management/transactions.md#lines-1) y a las [líneas de factura de venta](../../sales-management/transactions.md#lines-5) en función de los filtros que configure. Por ejemplo, orientando la promoción a determinados Grupos de Terceros o a productos específicos durante un periodo de tiempo definido.

Etendo calcula el precio final en tres pasos:

- **Tarifa**: El precio base definido en la tarifa de precios del producto.
- **Precio estándar**: El primer nivel de descuento. Puede provenir de la tarifa o ajustarse manualmente en la línea.
- **Precio real**: El precio final que aparecerá en el documento tras aplicar las promociones.

Si se aplican varias promociones, se aplicarán por orden de prioridad. Cada nueva promoción se aplica sobre el precio resultante de la anterior (cascada).

Los ajustes de precio son visibles inmediatamente al editar la línea; verá el precio final antes de procesar el documento.

!!! info
    Aunque el descuento se muestra al instante, el registro de **Modificación de precios** solo se crea una vez que el documento se procesa. Consulte la sección [Configuración opcional](#configuración-opcional) para saber cómo mostrar esta información en la ventana del documento.

### Configuración opcional { #optional-configuration }

La solapa de solo lectura **Modificación de precios** puede añadirse a las siguientes ventanas para mostrar los descuentos aplicados a cada precio:

- Pedido de compra
- Pedido de venta
- Factura de compra
- Factura de venta
- Presupuesto de venta

!!! tip
    Para mostrar esta solapa en las ventanas mencionadas, simplemente marque la casilla **Activo** en la solapa correspondiente en la ventana **ventanas, solapas y campos**. 
    Esta acción debe ser realizada por un desarrollador, con rol de administrador del sistema, y usando una **Plantilla** de desarrollo para exportar la configuración y evitar que se pierdan los cambios.

---

Este trabajo es una obra derivada de [Gestión de Datos Maestros](https://wiki.openbravo.com/wiki/Master_Data_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.
