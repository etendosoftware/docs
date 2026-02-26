---
tags:
    - Etendo Copilot
    - Automatización de correo electrónico
    - SMTP
    - API de Resend
    - Notificaciones
    - Herramienta
---

# Herramienta de envío de correo electrónico

:octicons-package-16: Paquete Java: `com.etendoerp.copilot.toolpack`

## Visión general

La **Herramienta de envío de correo electrónico** está diseñada para enviar correos electrónicos. Esta herramienta facilita el envío de correos de forma eficiente y estructurada. Acepta los siguientes parámetros de entrada: subject (el asunto del correo), mailto (la dirección de correo del destinatario) y html (el contenido HTML del correo). Como salida, devuelve un mensaje indicando el resultado del envío del correo.

!!!info
    Para poder incluir esta funcionalidad, debe estar instalado el Copilot Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. Para más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Copilot Extensions - Notas de la versión](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

Esta herramienta proporciona al agente:

- Automatización: automatiza el envío de correos electrónicos en aplicaciones y sistemas web.
- Flexibilidad: permite seleccionar entre diferentes métodos de envío (Resend o SMTP), en función de la configuración del entorno.
- Eficiencia: facilita la gestión de notificaciones y comunicaciones por correo electrónico, mejorando la eficiencia operativa.

Esta herramienta es esencial para desarrolladores y administradores de sistemas que necesitan integrar fácilmente funcionalidades de correo electrónico en sus aplicaciones o servicios.

## Configuración

Para utilizar esta herramienta, es necesario configurar la variable `MAIL_METHOD`:

- SMTP: utiliza el protocolo SMTP para enviar correo. Configura y envía correo utilizando un servidor SMTP como Gmail. SMTP es el valor por defecto para esta variable. Además, deben configurarse las credenciales: `MAIL_FROM` con el correo del remitente y `SMTP_PASSWORD` con la contraseña del remitente.

Por ejemplo:

``` groovy title="gradle.properties"
MAIL_METHOD=SMTP
MAIL_FROM= example@example.com
SMTP_PASSWORD= ******
```
- resend: en este caso, se utiliza el [servicio de API de Resend](https://resend.com/){target="\_blank"}, diseñado para reenviar solicitudes de correo electrónico. En caso de seleccionar esta opción, es necesario configurar la variable `RESEND_API_KEY`. Por ejemplo:

``` groovy title="gradle.properties"
MAIL_METHOD=resend
RESEND_API_KEY=******
```

## Funcionalidad

Esta herramienta es útil en cualquier aplicación o servicio que necesite enviar correos electrónicos automáticamente. Puede utilizarse para notificaciones, actualizaciones, confirmaciones de pedidos, restablecimientos de contraseña, entre otras cosas.

Este proceso consta de las siguientes acciones:

- **Procesamiento de argumentos**

    Toma los parámetros de entrada que especifican el asunto, el destinatario y el contenido HTML del correo.

- **Verificación del método de envío**

    Determina el método de envío utilizando una variable de entorno `MAIL_METHOD`. Las opciones se mencionan en la sección [Configuración](#configuración) anterior.

- **Envío del correo**
    
    En función del método de envío, configura y envía el correo con la información proporcionada.

- **Devolución del resultado**
    
    Devuelve un mensaje indicando si el correo se envió correctamente o si hubo un error. Por ejemplo:
    
    ```
    { “message”: “Mail sent successfully”}
    ```
 
    si el correo se envió correctamente.

    ```
    { “message”: “Mail method not supported”}
    ```
    
    si el método de envío no es compatible.

## Ejemplo de uso

Imagine que desea enviar un correo electrónico de notificación. Los parámetros de entrada para el agente serían:

- `subject`: Actualización de cuenta
- `mailto`: user@example.com
- `html`: 
    ```html
    <h1>Account Upgrade</h1>
    <p>Your account has been successfully upgraded.</p>
    <p><p>Your account has been successfully upgraded.
    ```

La Herramienta de envío de correo electrónico procesará estos parámetros y seleccionará el método de envío configurado. A continuación, enviará el correo y devolverá un mensaje indicando si el correo se envió correctamente.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.