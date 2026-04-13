---
title: Webhooks de Etendo | Documentación técnica
---

:octicons-package-16: Paquete Java: `com.etendoerp.webhookevents`

## Visión general

### ¿Qué es un Webhook?

Un webhook es un método utilizado por las aplicaciones web para enviar notificaciones o datos en tiempo real a otras aplicaciones o servidores. Los webhooks operan mediante callbacks HTTP, lo que significa que una aplicación envía una solicitud HTTP a una URL especificada (la URL del webhook) cuando ocurre un evento determinado.

En términos sencillos, un webhook actúa como un mensajero que entrega un mensaje (carga útil de datos) de una aplicación a otra cuando se cumplen ciertas condiciones. Los webhooks permiten que las aplicaciones se comuniquen y compartan información automáticamente, facilitando la integración de distintos servicios y la creación de flujos de trabajo sin fricciones.

Al utilizar webhooks, puede mantener sus aplicaciones sincronizadas, automatizar procesos y ampliar la funcionalidad de sus aplicaciones con un esfuerzo mínimo.

Esta documentación le guiará a través del proceso de configuración y uso de webhooks en Etendo Classic. Los webhooks le permiten ejecutar acciones mediante una llamada a una URL, proporcionando una forma potente de integrarse con servicios externos.

## Descripción del Webhook

### Campos de cabecera del Webhook

| Campo                         | Descripción                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| Módulo                       | Módulo en el que se creará el webhook                                       |
| Nombre                       | Nombre del webhook                                                          |
| Descripción                  | Descripción del webhook                                                     |
| Clase Java                   | Clase en la que se creó el servicio del webhook                             |
| Permitir dar acceso al rol   | Marque si se permite dar acceso a roles mediante servicios web seguros       |
| Activo                       | Estado del webhook (Activo por defecto)                                     |

![Cabecera del Webhook](../../../../assets/developer-guide/etendo-classic/bundles/platform/etendo-webhooks/WebhookHeader.png)

### Campos de solapas del Webhook

La ventana de Webhook tiene 2 solapas: Acceso y Parámetros.

La solapa de parámetros le permite crear parámetros que se utilizarán en la llamada a la URL.

La solapa de acceso le permite crear accesos que se utilizarán en la llamada a la URL.

#### Parámetros

| Campo       | Descripción                                              |
|------------|----------------------------------------------------------|
| Nombre     | Nombre del parámetro que se utilizará en la llamada a la URL |
| Es obligatorio | Si el parámetro es obligatorio o no                  |
| Activo     | Estado del parámetro (Activo por defecto)                |

#### Acceso de usuario

Permitir ejecución mediante token.

| Campo   | Descripción                                                                                      |
|--------|--------------------------------------------------------------------------------------------------|
| Activo | Estado del acceso (Activo por defecto)                                                           |
| Token  | Selector con el token que se utilizará en la llamada a la URL creado en la ventana User API Token |

#### Rol permisos

Si necesita permitir usuarios autenticados con SWS, lea la guía: [Cómo usar servicios web seguros](../../how-to-guides/how-to-use-secure-webservices.md). Para ello, debe añadir roles a los que se les permita ejecutar un webhook en la solapa **Rol permisos**.

## Ejemplo de uso del Webhook

### Configuración de Webhooks

1. Navegue a la nueva opción de menú: `Aplicación → Configuración general → Aplicación → Eventos de Webhook → Webhooks`
2. Cree un nuevo webhook completando los campos obligatorios:

    | Campo       | Valor                                                      |
    |------------|------------------------------------------------------------|
    | Nombre     | Alerta                                                     |
    | Descripción | Crear alerta con mensaje personalizado                     |
    | Clase Java | com.etendoerp.webhookevents.ad_alert.AdAlertWebhookService |

    ![Alerta de Webhook](../../../../assets/developer-guide/etendo-classic/bundles/platform/etendo-webhooks/WebhookAlert.png)

3. Sitúese en la solapa "Parámetros" y cree los siguientes parámetros:

    | Campo   | Valor                    |  Es obligatorio     |
    |--------|--------------------------|---------------------|
    | Nombre | description              | :white_check_mark:  |
    | Nombre | rule                     | :white_check_mark:  |

![Parámetros del Webhook](../../../../assets/developer-guide/etendo-classic/bundles/platform/etendo-webhooks/WebhookParams.png)

### Rol permisos

#### Generación de clave API

1. Para dar permiso de ejecución a un usuario, vaya a: `Aplicación → Configuración general → Aplicación → Eventos de Webhook → User API Token`
2. Cree una nueva API con el Nombre: `<<user>> token`
    ![Token de Webhook](../../../../assets/developer-guide/etendo-classic/bundles/platform/etendo-webhooks/WebhookToken.png)
3. Tras guardar, ejecute la opción “Get API Key” y guarde el token resultante (cadena aleatoria de longitud 64) en su portapapeles.
    ![Cadena del token de Webhook](../../../../assets/developer-guide/etendo-classic/bundles/platform/etendo-webhooks/WebhookTokenString.png)

#### Asignación de acceso al Webhook a usuarios

1. Navegue a: `Aplicación → Configuración general → Aplicación → Eventos de Webhook → Webhooks`
2. Seleccione el webhook creado y abra la solapa de acceso.
3. Cree una nueva línea y seleccione el registro de API creado previamente.

![Acceso al Webhook](../../../../assets/developer-guide/etendo-classic/bundles/platform/etendo-webhooks/WebhookAccess.png)

### Acceso a servicios web seguros

#### Asignar roles permitidos

En la ventana Webhooks, añada los roles permitidos para ejecutar el webhook.

![Rol del Webhook](../../../../assets/developer-guide/etendo-classic/bundles/platform/etendo-webhooks/WebhookRole.png)

### Ejecución del Webhook

Para ejecutar el webhook, realice una solicitud GET utilizando un cliente REST como Postman con la siguiente sintaxis:

```
URL=http://localhost:8080/
CONTEXT=etendo
WEBHOOK_ENDPOINT=/webhooks/
[VARS]
WEBHOOK_NAME=name=alert
DESCRIPTION=new alert description
RULE=649BBFA37BA74FA59AEBE7F28524B0C8
```

#### URL de ejemplo:

*Con token*

APIKEY=8b1012f0d442406ed602d87c13edcee9

```
http://localhost:8080/etendo/webhooks/?name=Alert&apikey=<api-key>&description=new alert description&rule=649BBFA37BA74FA59AEBE7F28524B0C8
```

*Con token sws*

```
http://localhost:8080/etendo/webhooks/?name=Alert&description=new alert description&rule=649BBFA37BA74FA59AEBE7F28524B0C8
```

Añada como autorización Bearer Token el JWT obtenido mediante el inicio de sesión SWS.

#### Respuesta esperada

!!! success
    Este webhook crea una alerta, y puede visualizarla en la ventana "Gestión de Alertas".

    La respuesta devolverá un código de estado **200** y el **ID de alerta**, por ejemplo:
    ```
    {
      "created": "91FEABC1604E404CB565FC79435C4344"
    }
    ```

### Ejemplo de uso de código

```java title="AdAlertWebhookService.java"
/**
 * Example webhoook to take as a starting point.
 * This service receive a description and a alert rule ID and insert one standard alert
 */
public class AdAlertWebhookService extends BaseWebhookService {
  private static final Logger log = LogManager.getLogger();
  
  @Override
  public void get(Map<String, String> parameter, Map<String, String> responseVars) {
    Alert alert = new Alert();
    alert.setAlertRule(OBDal.getInstance().get(AlertRule.class, parameter.get("rule")));
    alert.setDescription(parameter.get("description"));
    alert.setReferenceSearchKey("");
    OBDal.getInstance().save(alert);
    OBDal.getInstance().flush();
    responseVars.put("created", alert.getId());
  }
}
```

## Casos de uso

### Visibilidad de tokens

!!! note
    :eye: Los usuarios pueden visualizar los tokens de su perfil actual.

!!! warning
    :warning: Otros usuarios no pueden acceder al token de otro usuario. La ventana API Token y la solapa de acceso del webhook estarán vacías.

### Gestión de errores

!!! failure
    Si un usuario llama a un webhook sin un token o incluye un token de API incorrecto, el backend responderá con una respuesta **401** y un mensaje.

!!! failure
    Si un usuario llama a un webhook con un nombre de webhook incorrecto, el backend responderá con una respuesta **404** y un mensaje.

!!! failure
    Si un usuario llama a un webhook sin acceso, el backend responderá con una respuesta **401** y un mensaje.

!!! failure
    Si un usuario llama a un webhook sin un parámetro obligatorio requerido, el backend responderá con una respuesta **500** y un mensaje.

!!! failure
    Si un usuario llama a un webhook sin un parámetro que ha pasado a ser obligatorio (después de que se cambie la configuración del backend), el backend responderá con una respuesta **500** y un mensaje.

!!! failure
    Si un usuario llama a un webhook con el acceso revocado, el backend responderá con una respuesta **401** y un mensaje.

---
Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L](https://etendo.software){target="_blank"}.