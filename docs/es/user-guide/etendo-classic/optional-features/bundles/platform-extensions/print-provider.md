---
title: Print Provider
tags:
    - Warehouse Management
    - Print Provider
    - Print
    - Stock
    - PrintNode
---

# Print Provider
:octicons-package-16: Javapackage: `com.etendoerp.print.provider`

## Visión general

El módulo **Print Provider** conecta Etendo con plataformas de impresión, ofreciendo una solución unificada para generar imprimibles directamente desde diferentes áreas del sistema.

Permite que cada organización configure su proveedor de impresión, gestione y sincronice el catálogo de impresoras disponibles, administre plantillas de impresión y ejecute impresiones bajo demanda desde ventanas específicas.

!!! info
    Este módulo incluye por defecto la implementación de un proveedor de impresión específico [Print Node](https://www.printnode.com/){target="_blank"}, y todos los ejemplos de configuración y uso se basan en este proveedor. Este servicio incluye un plan gratuito, aunque si necesita grandes volúmenes de impresión, debe consultar el [service pricing](https://www.printnode.com/pricing){target="_blank"}.    


!!! tip
    Además, este módulo permite la implementación de proveedores de impresión personalizados, expone servicios de back-end reutilizables que pueden ser consumidos por diferentes módulos, y una API pública para imprimir desde desarrollos personalizados. Para más información, visite: [Print Provider - Developer Guide](../../../../../developer-guide/etendo-classic/bundles/platform/print-provider.md)


## Configuración inicial

Antes de utilizar el módulo **Print Provider**, debe completarse una configuración inicial para establecer la conexión entre Etendo y el servicio de impresión seleccionado.

El siguiente ejemplo integra el servicio **PrintNode** con Etendo. Este proveedor está incluido con el módulo, pero su uso es opcional.

La integración con PrintNode requiere seguir la [official documentation](https://www.printnode.com/docs){target="_blank"}. En términos generales, debe crear una cuenta, instalar el software de gestión en el dispositivo responsable de imprimir y generar una clave de API que luego utilizaremos desde Etendo para conectarnos al servicio.

Este proceso incluye:

- [x] Crear una cuenta de **PrintNode** y obtener la **Clave de API**.
- [x] Instalar la configuración del proveedor y las plantillas de impresión en Etendo.
- [x] Configurar el acceso del proveedor.
- [x] Buscar y sincronizar las impresoras disponibles.
 
Una vez completados estos pasos, el sistema estará listo para ejecutar impresiones de forma centralizada y segura.


### Instalar el conjunto de datos del proveedor y de plantillas de impresión

:material-menu: `Aplicación`>`Configuración General` > `Organización` > `Gestión del módulo de Empresa`

Abra la ventana **Gestión del módulo de Empresa** e instale los datos de referencia **Etendo Print Provider** incluidos en el módulo; esto configurará las configuraciones con el proveedor PrintNode y las plantillas de impresión de ejemplo.

![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/platform-extensions/print-provider/install-dataset.png)

### Print Providers

:material-menu: `Configuración General` > `Print Provider Configuration` > `Print Providers`

Esta ventana se utiliza para registrar proveedores de impresión. En este caso, la configuración del proveedor **PrintNode** ya se crea con la instalación del conjunto de datos.

![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/platform-extensions/print-provider/print-provider-window.png)

Aquí se muestra información general como **Identificador** y **Nombre**. También incluye el campo específico **Provider Implementation** que hace referencia al registro creado en la ventana Provider Implementation. Para más información sobre cómo crear un proveedor de impresión, visite [Print Provider - Developer Guide](../../../../../developer-guide/etendo-classic/bundles/platform/print-provider.md)


#### Provider Params

Esta pestaña define los valores de configuración necesarios para la integración con un proveedor de impresión. Esta configuración es esencial para que el sistema se comunique correctamente con sus servicios.

El sistema permite al usuario crear cualquier parámetro que el proveedor de impresión requiera, adaptándose a sus necesidades. Para añadir un nuevo parámetro, utilice los siguientes campos:

   - **Identificador**: Un nombre único que identifica el parámetro.
   - **Param Content**: El valor o la información requerida para el parámetro.
   - **Descripción**: Una breve explicación de la función del parámetro.

En el ejemplo de **PrintNode**, el parámetro **apiKey** debe configurarse con la clave correspondiente para establecer la comunicación con el proveedor.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/platform-extensions/print-provider/api-key-param.png)

!!! info
    Cada organización debe registrar y mantener su propia clave de API. No se recomienda compartir credenciales entre compañías, ya que afectaría a la trazabilidad y a la seguridad.


### Check and Register Printers

:material-menu: `Configuración General` > `Print Provider Configuration` > `Check and Register Printers`

Esta ventana de tipo proceso busca y actualiza la lista de impresoras disponibles para un proveedor específico.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/platform-extensions/print-provider/check-and-register-printers.png)

- **Provider**: menú desplegable que lista todos los proveedores de impresoras que se han configurado previamente en el sistema. El campo siempre se carga con un valor por defecto, pero el usuario tiene la opción de modificarlo.

- **Done**: al hacer clic en este botón, el sistema busca las impresoras disponibles y actualiza la información según el proveedor seleccionado.

### Printers

:material-menu: `Configuración General` > `Print Provider Configuration` > `Printers`

Esta ventana proporciona una vista de las impresoras disponibles por proveedor y permite actualizar la lista directamente desde la API correspondiente, asegurando que siempre se trabaje con dispositivos activos y sincronizados.

![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/platform-extensions/print-provider/printers-window.png)

El registro de impresoras es de solo lectura, excepto para los campos **Activo** y **Valor por defecto**. Solo una impresora puede establecerse como Valor por defecto. Si no se designa ninguna, el sistema selecciona una automáticamente.

La cabecera muestra información general como **Identificador**, **Nombre** y **Provider**, basada en registros definidos previamente.

- **Refresh Print**: al hacer clic en este botón se actualiza la lista de impresoras consultando el endpoint definido en la ventana Print Providers. Las impresoras obtenidas dependerán de cada proveedor y pueden ser locales o en la nube.

### Print Templates

:material-menu: `Configuración General` > `Print Provider Configuration` > `Print Templates`

Esta ventana gestiona las plantillas de impresión. Estas plantillas se asocian con la tabla relacionada desde la cual se obtendrá la información para generar el imprimible. Por defecto, el módulo incluye una plantilla para generar un imprimible desde la ventana **Producto**, utilizando la tabla *m_product*.

Estas configuraciones se distribuyen e instalan automáticamente con el conjunto de datos.

![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/platform-extensions/print-provider/print-template-window.png)

Campos a tener en cuenta:

- **Table**: Tabla asociada, desde la cual se obtendrá información para generar el documento imprimible.
- **Nombre**: Nombre de la plantilla de impresión.
- **Template Line**: Ubicación de la plantilla.


## Generar imprimibles

Este **button** es un componente reutilizable del módulo de proveedor de impresión que puede configurarse en ventanas de Etendo según las necesidades del negocio. Permite la selección múltiple de registros y, al pulsarlo, abre una ventana emergente donde el usuario puede seleccionar opcionalmente un proveedor y una impresora, especificar el número de copias y elegir si desea descargar el archivo generado.

!!!info 
    Al seleccionar múltiples registros, el campo Nº de copias indica el número de copias de cada registro seleccionado.

Por ejemplo, el módulo **Print Provider** integra este botón en la ventana **Producto**, generando un imprimible de código de barras para el producto.

![generate-printable](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/platform-extensions/print-provider/generate-printable.png)

La ventana emergente presenta los siguientes campos. Se permite la selección de múltiples registros.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/platform-extensions/print-provider/generate-printable-popup.png)

   - **Provider**: (Opcional) Seleccione un proveedor de impresión configurado previamente. Si se deja vacío, el sistema opera en **Download-only Mode**: genera el documento y lo descarga como PDF sin enviarlo a ninguna impresora.
   - **Printers**: Solo visible cuando se selecciona un Provider. Muestra las impresoras asociadas al proveedor seleccionado. Carga la impresora por defecto, si está disponible.
   - **Number of Copies**: Solo visible cuando se selecciona un Provider. Número de copias a imprimir. En modo solo descarga este campo se oculta y por defecto es una copia.
   - **Download**: Cuando se establece en **Yes**, el archivo PDF del imprimible generado también se descarga en el navegador. Esta opción está habilitada por defecto y siempre es visible independientemente de si se selecciona un proveedor. En modo solo descarga (sin proveedor seleccionado), este campo debe permanecer establecido en **Yes**; de lo contrario, no se realizará ninguna acción y se mostrará una advertencia.

### Download-only Mode

- Si se seleccionan múltiples registros, todas las etiquetas generadas se combinan en un único PDF para su descarga.
- Si algunos registros no se pueden generar, las etiquetas generadas correctamente se descargan igualmente y se muestra una advertencia indicando cuántas han fallado.
- Si todos los registros fallan al generarse, se muestra un mensaje de error.

!!! tip
    Este modo es ideal para usuarios que solo necesitan copias digitales de sus imprimibles, por ejemplo para adjuntarlas a correos electrónicos, archivarlas o imprimirlas manualmente desde otro dispositivo o aplicación.

### Print & Download Mode

- Si el trabajo de impresión se envía correctamente, se muestra un mensaje de éxito con el ID del trabajo de impresión.
- Si el trabajo de impresión falla pero la etiqueta se generó, el PDF sigue estando disponible para su descarga (cuando Download está habilitado) y se muestra una advertencia.
- Si todos los trabajos de impresión fallan y no se retuvo ninguna etiqueta, se muestra un mensaje de error.

!!! Warning
    El módulo Print Providers actúa como un puente entre Etendo y la impresora. Los problemas operativos de la impresora, como falta de papel, falta de tinta o problemas de conectividad de red, no son gestionados por este sistema.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/platform-extensions/print-provider/send-impresion.png)

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/platform-extensions/print-provider/barcode.png)
---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.