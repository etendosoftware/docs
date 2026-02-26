---
title: Proveedor de impresión
tags:
    - Warehouse Management
    - Proveedor de impresión
    - Impresión
    - Stock
    - PrintNode
---

# Proveedor de impresión
:octicons-package-16: Javapackage: `com.etendoerp.print.provider`

## Visión general

El módulo **Proveedor de impresión** conecta Etendo con plataformas de impresión, ofreciendo una solución unificada para generar imprimibles directamente desde diferentes áreas del sistema.

Permite que cada organización configure su proveedor de impresión, gestione y sincronice el catálogo de impresoras disponibles, administre plantillas de impresión y ejecute impresiones bajo demanda desde ventanas específicas.

El sistema proporciona un flujo de trabajo de impresión sencillo con un solo clic: el usuario selecciona la impresora y la plantilla, y Etendo genera el documento en el formato requerido y lo envía directamente al proveedor de impresión.

!!! info 
    Este módulo incluye por defecto la implementación de un proveedor de impresión específico, [Print Node](https://www.printnode.com/){target="_blank"}, y todos los ejemplos de configuración y uso se basan en este proveedor. Este servicio incluye un plan gratuito, aunque si requiere grandes volúmenes de impresión, debería consultar la [tarificación del servicio](https://www.printnode.com/pricing){target="_blank"}.    


!!! tip
    Además, este módulo permite la implementación de proveedores de impresión personalizados, expone servicios de back-end reutilizables que pueden ser consumidos por diferentes módulos, y una API pública para imprimir desde desarrollos personalizados. Para más información, visite: [Proveedor de impresión - Guía del desarrollador](../../../../../assets/user-guide/developer-guide/etendo-classic/bundles/platform/print-provider.md)


## Configuración inicial

Antes de utilizar el módulo **Proveedor de impresión**, debe completarse una configuración inicial para establecer la conexión entre Etendo y el servicio de impresión seleccionado.

El siguiente ejemplo integra el servicio **PrintNode** con Etendo. Este proveedor se incluye con el módulo, pero su uso es opcional.

La integración con PrintNode requiere seguir la [documentación oficial](https://www.printnode.com/docs){target="_blank"}. En términos generales, debe crear una cuenta, instalar el software de gestión en el dispositivo responsable de imprimir y generar una clave de API que luego utilizaremos desde Etendo para conectarnos al servicio.

Este proceso incluye:

- [x] Crear una cuenta de **PrintNode** y obtener la **clave de API**.
- [x] Instalar la **configuración del proveedor** y las **plantillas de impresión** en Etendo.
- [x] Configurar el **acceso del proveedor**.
- [x] Buscar y sincronizar las impresoras disponibles. 
 
Una vez completados estos pasos, el sistema estará listo para ejecutar impresiones de forma centralizada y segura.


### Instalar el conjunto de datos del proveedor y de plantillas de impresión

:material-menu: `Aplicación`>`Configuración General` > `Organización` > `Gestión del módulo de Empresa`

Abra la ventana **Gestión del módulo de Empresa** e instale los datos de referencia **Etendo Print Provider** incluidos en el módulo; esto configurará las parametrizaciones con el proveedor PrintNode y las plantillas de impresión de ejemplo.

![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/platform-extensions/print-provider/install-dataset.png)

### Proveedores de impresión

:material-menu: `Configuración General` > `Configuración del proveedor de impresión` > `Proveedores de impresión`

Esta ventana se utiliza para registrar proveedores de impresión. En este caso, la configuración del proveedor **PrintNode** ya se crea con la instalación del conjunto de datos.

![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/platform-extensions/print-provider/print-provider-window.png)

Aquí se muestra información general como **Identificador** y **Nombre**. También incluye el campo específico **Implementación del proveedor**, que hace referencia al registro creado en la ventana Implementación del proveedor. Para más información sobre cómo crear un proveedor de impresión, visite [Proveedor de impresión - Guía del desarrollador](../../../../../assets/user-guide/developer-guide/etendo-classic/bundles/platform/print-provider.md)


#### Parámetros del proveedor

Esta solapa define los valores de configuración necesarios para la integración con un proveedor de impresión. Esta configuración es esencial para que el sistema se comunique correctamente con sus servicios.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/platform-extensions/print-provider/print-provider-tab.png)

El sistema permite al usuario crear cualquier parámetro que el proveedor de impresión requiera, adaptándose a sus necesidades. Para añadir un nuevo parámetro, utilice los siguientes campos:

   - **Identificador**: Un nombre único que identifica el parámetro.
   - **Contenido del parámetro**: El valor o la información requerida para el parámetro.
   - **Descripción**: Una breve explicación de la función del parámetro.

En el ejemplo de **PrintNode**, el parámetro **apiKey** debe configurarse con la clave correspondiente para establecer la comunicación con el proveedor.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/platform-extensions/print-provider/api-key-param.png)

!!! info
    Cada organización debe registrar y mantener su propia clave de API. No se recomienda compartir credenciales entre compañías, ya que afectaría a la trazabilidad y la seguridad.


### Comprobar y registrar impresoras

:material-menu: `Configuración General` > `Configuración del proveedor de impresión` > `Comprobar y registrar impresoras`

Esta ventana de tipo proceso busca y actualiza la lista de impresoras disponibles para un proveedor específico.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/platform-extensions/print-provider/check-and-register-printers.png)

- **Proveedor**: menú desplegable que lista todos los proveedores de impresión que se han configurado previamente en el sistema. El campo siempre se carga con un valor por defecto, pero el usuario tiene la opción de modificarlo.

- **Hecho**: al hacer clic en este botón, el sistema busca las impresoras disponibles y actualiza la información según el proveedor seleccionado.

### Impresoras

:material-menu: `Configuración General` > `Configuración del proveedor de impresión` > `Impresoras`

Esta ventana ofrece una vista de las impresoras disponibles por proveedor y permite actualizar la lista directamente desde la API correspondiente, asegurando que siempre se trabaje con dispositivos activos y sincronizados.

![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/platform-extensions/print-provider/printers-window.png)

El registro de impresoras es de solo lectura, excepto para los campos **Activo** y **Valor por defecto**. Solo se puede establecer una impresora como Valor por defecto. Si no se designa ninguna, el sistema selecciona una automáticamente.

La cabecera muestra información general como **Identificador**, **Nombre** y **Proveedor**, basada en registros definidos previamente. 

- **Actualizar impresión**: al hacer clic en este botón se actualiza la lista de impresoras consultando el endpoint definido en la ventana Proveedores de impresión. Las impresoras obtenidas dependerán de cada proveedor y pueden ser locales o estar en la nube.

### Plantillas de impresión

:material-menu: `Configuración General` > `Configuración del proveedor de impresión` > `Plantillas de impresión`

Esta ventana gestiona las plantillas de impresión. Estas plantillas se asocian con la tabla relacionada desde la cual se obtendrá la información para generar el imprimible. Por defecto, el módulo incluye una plantilla para generar un imprimible desde la ventana **Producto**, utilizando la tabla *m_product*.

Estas configuraciones se distribuyen e instalan automáticamente con el conjunto de datos.

![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/platform-extensions/print-provider/print-template-window.png)

Campos a tener en cuenta:

- **Tabla**: Tabla asociada, desde la cual se obtendrá la información para generar el documento imprimible.
- **Nombre**: Nombre de la plantilla de impresión. 
- **Línea de plantilla**: Ubicación de la plantilla.


## Generar imprimibles

Este **botón** es un componente reutilizable del módulo de proveedor de impresión que puede configurarse en las ventanas de Etendo según las necesidades del negocio. Permite la selección múltiple de registros a imprimir y, al pulsar el botón, se abre una ventana emergente que permite seleccionar el proveedor, la impresora deseada y el número de copias. Una vez confirmado, el sistema genera el imprimible utilizando la plantilla seleccionada y envía el trabajo de impresión al proveedor configurado.

!!!info 
    Al seleccionar múltiples registros para imprimir, el campo Copias documentos indica el número de copias de cada registro seleccionado.

Por ejemplo, el módulo **Proveedor de impresión** integra este botón en la ventana **Producto**, generando una etiqueta de código de barras para el producto.

![generate-printable](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/platform-extensions/print-provider/generate-printable.png)

La ventana emergente permite seleccionar un proveedor de impresión previamente configurado, asignar la impresora correspondiente desde la lista de dispositivos disponibles y especificar el número de copias. Se permiten selecciones múltiples.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/platform-extensions/print-provider/generate-printable-popup.png)

   - **Proveedor**: Seleccione el proveedor de impresión configurado previamente.
   - **Impresoras**: Solo muestra las impresoras asociadas al proveedor seleccionado. Carga la impresora por defecto, si está disponible.
   - **Copias documentos**: Número de copias a imprimir.

!!! Warning
    El módulo Proveedores de impresión actúa como un puente entre Etendo y la impresora. Los problemas operativos de la impresora, como falta de papel, falta de tinta o problemas de conectividad de red, no son gestionados por este sistema.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/platform-extensions/print-provider/send-impresion.png)

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/platform-extensions/print-provider/barcode.png)
---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.