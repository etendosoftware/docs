---
title: Entidad
tags:
    - Configuración de entidad de Etendo
    - Gestión de datos maestros
    - Dimensiones contables
    - Configuración del correo electrónico
---

# Entidad

:material-menu: `Aplicación` > `Configuración General` > `Entidad` > `Entidad`

## Visión general

Una **entidad** es una entidad independiente compuesta por al menos una organización. Una entidad puede incluir y gestionar datos maestros como Usuarios, Clientes y Proveedores. Esos datos maestros se comparten entre todas las organizaciones que pertenecen a esa entidad.

Etendo permite al usuario crear más de una Entidad y más de una Organización dentro de cada Entidad para modelar su empresa según sus necesidades.

Normalmente, es suficiente con crear solo una Entidad que aloje múltiples organizaciones que puedan utilizarse para modelar su empresa; las principales razones son:

- una entidad puede gestionar datos maestros que, por tanto, están disponibles para todas las organizaciones dentro de esa entidad
- además, cada organización también puede gestionar sus propios datos maestros y tener sus propios datos transaccionales
- por último, una Entidad no puede compartir ningún dato maestro con otra Entidad.

Las entidades se crean ejecutando el proceso [proceso de creación de entidad](../../../../../developer-guide/etendo-classic/how-to-guides/how-to-run-an-initial-client-setup-process.md) disponible para el rol de Administrador del Sistema.

Las organizaciones se crean ejecutando el proceso de configuración inicial de la organización disponible para el rol de Administrador de la Entidad.

## Entidad

La ventana Entidad permite al usuario ver y mantener las entidades creadas al ejecutar el proceso **Crear entidad**.

![Client Window](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/client/client-window.png)

!!! info
    El campo **Días para la Caducidad de Contraseña** permite al usuario establecer un límite de días durante el cual una contraseña puede ser válida para los usuarios. El límite se restablecerá cada vez que un usuario cambie su contraseña.

El valor del campo determina el límite de días durante el cual una contraseña debe ser válida para los usuarios:

- Si se establece en 0, no se aplicará ningún límite de días.
- Si el valor es mayor que 0, el límite de días se aplicará a partir de la última fecha de actualización de la contraseña del usuario.

Al establecer el valor, se aplicará la configuración a todos los Usuarios de esa Entidad.

Un campo relevante a tener en cuenta es la casilla de verificación **Centralizado** dentro de la sección Dimensiones contables.

Esta casilla, si se selecciona, permite al usuario configurar que la Entidad mantenga de forma centralizada dimensiones contables clave como Organización, Tercero o Centro de coste; por tanto, la configuración establecida aquí se comparte entre todas las organizaciones de la entidad.

Las nuevas Entidades creadas al ejecutar el proceso de creación de entidad se crean, por defecto, como mantenidas de forma centralizada con las dimensiones contables obligatorias (Organización, Tercero, Producto) seleccionadas.

Las organizaciones de la Entidad que necesiten disponer de dimensiones adicionales no listadas aquí, por ejemplo Campaña o Región de ventas, deberán configurarlas en la pestaña Dimensiones de la configuración del libro mayor de la organización.

Ahora es posible cambiar Entidades existentes a **mantenidas de forma centralizada**; esta acción sobrescribe lo configurado para la organización en relación con las dimensiones contables que pueden mantenerse de forma centralizada en la Entidad. Esas dimensiones son:

- Dimensiones obligatorias:
    
    - Organización
    - Tercero
    - y Producto

Las dimensiones obligatorias pueden rellenarse o no en función de la categoría de documento que se esté creando. Por ejemplo, Organización debe especificarse siempre en la cabecera del documento independientemente del documento que se esté creando; sin embargo, Tercero y Producto son dimensiones obligatorias que deben rellenarse en una factura de compra, pero pueden rellenarse en un Diario de mayor (G/L) si es necesario.

- Dimensiones no obligatorias:

    - Proyecto
    - Centro de coste
    - 1ª Dimensión, es una dimensión de texto libre que puede personalizarse según se requiera (p. ej., podría personalizarse como Departamento), igual que la siguiente
    - y 2ª Dimensión

Las dimensiones no obligatorias pueden rellenarse o no en función de lo que se necesite e independientemente de la categoría de documento que se esté creando.

Las dimensiones anteriores se muestran después en la cabecera y/o en las líneas de los documentos que se contabilizarán en el libro mayor, dentro de una sección denominada Dimensiones.

Además, existe un informe financiero denominado **Datos de contabilidad** que muestra cada apunte del libro mayor de una organización detallando cada valor de dimensión introducido.

!!! info
    Es importante remarcar que la configuración mostrada en la ventana de entidad, tanto en la sección Dimensiones contables como en la pestaña Dimensiones, es la configuración predeterminada proporcionada por Etendo.

Esta configuración predeterminada se rellena desde la ventana **Asignación de dimensiones** (Administrador del Sistema).

Siempre es posible personalizar la configuración predeterminada; por ejemplo:

- Si una entidad necesita mostrar y, por tanto, poner a disposición la dimensión *organización* en las líneas de los documentos, deben realizarse las siguientes acciones:

    - Marcar la casilla **Mostrar en líneas** para la dimensión Organización
    - y eliminar o modificar los registros vinculados a la dimensión contable Organización en la pestaña Dimensiones, ya que todos esos registros están predeterminados para no mostrar Organización en las líneas de ninguna categoría de documento.

### Información

La pestaña Información permite al usuario añadir, editar y mantener información genérica de la entidad, como las unidades de medida predeterminadas e imágenes.

![Client Information Tab](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/client/client-information-tab.png)

Información adicional que se permite especificar:

- **Importe calculado de descuento de una línea** excluyendo impuestos y cargos
- Unidades de medida predeterminadas para:

    - **Volumen**
    - **Peso**
    - **Longitud**
    - y **Hora**

- **Tarifa**
- **Portes del producto**
- **Comprobar organización albarán** para controlar que la organización que envía la mercancía sea la misma que la organización del cliente.
- **Comprobar organización pedido** para controlar que la organización que realiza el pedido sea la misma que la organización del proveedor.
- **Agrupar líneas de factura en contabilidad** para que, en facturas con muchas líneas, no se generen tantas líneas contables como líneas de factura, sino un número resumido de líneas contables por cuenta.
- **Logotipo** de la empresa para:

    - la **Imagen de la empresa**
    - el **Menú de la empresa**
    - y los **Documentos de la empresa**

- **Permitir stock negativo**; para ello, Etendo no comprueba el stock si no es necesario.

### Configuración del correo electrónico

La pestaña **Configuración del correo electrónico** permite configurar el servidor SMTP utilizado
para enviar documentos por correo electrónico (p. ej., pedidos o facturas).

El correo electrónico puede configurarse en tres niveles: Entidad, Organización y Usuario.
Para la referencia completa de campos e instrucciones de configuración, consulte
[Cómo configurar el correo electrónico](../../../how-to-guides/how-to-configure-email.md).

### Dimensiones

La pestaña Dimensiones permite al usuario configurar si una dimensión contable determinada va a estar disponible en la cabecera y/o en las líneas de una categoría de documento determinada.

Esta pestaña puede utilizarse para configurar la disponibilidad de dimensiones contables a nivel de documento solo si la entidad está configurada como mantenida de forma centralizada. Esta configuración es específica del documento y de la dimensión contable, y sobrescribe la configuración de la cabecera.

Por ejemplo, si una entidad necesita mostrar la dimensión proyecto en la cabecera y en las líneas en todos los documentos excepto en el documento de amortización, la ventana Entidad debería tener la siguiente configuración:

![Client Dimensions Tab](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/client/client-dimensions-tab.png)

La configuración en la pestaña Dimensiones se rellena a partir de la configuración existente en la ventana Asignación de dimensiones.

---

Este trabajo es una obra derivada de [Configuración General](https://wiki.openbravo.com/wiki/General_Setup){target="_blank"} de [Wiki de Openbravo](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="_blank"} por [Etendo](https://etendo.software){target="_blank"}.

---

---