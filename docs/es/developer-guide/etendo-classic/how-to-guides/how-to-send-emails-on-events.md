---
title: Cómo enviar correos electrónicos en eventos
tags: 
    - Enviar
    - Correos electrónicos
    - Eventos 
    - Cómo
status: beta
---

# Cómo enviar correos electrónicos en eventos

!!! example "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.
  
## Visión general

Etendo proporciona un mecanismo que permite generar eventos de forma programática para enviar correos electrónicos. El disparo de eventos y la implementación del correo electrónico están desacoplados, siendo posible lanzar eventos genéricos, que son escuchados por otros módulos que implementan el contenido del correo electrónico.

Este procedimiento explica ambas cosas: cómo disparar los eventos y cómo escucharlos para generar el evento.

El servidor de correo electrónico está [configurado](../../../user-guide/etendo-classic/basic-features/general-setup/client/client.md#email-configuration) a nivel de cliente.

## Disparo de eventos de correo electrónico

Un evento se identifica simplemente mediante un `String`.

Los eventos se disparan de forma programática desde cualquier parte del código, como [Procesos](../how-to-guides/how-to-create-a-standard-process-definition.md) o [Manejadores de eventos de negocio](../how-to-guides/how-to-implement-a-business-event-handler.md).

Para disparar un evento necesita:

Inyectar en su clase un `EmailEventManager`

``` java
...
@Inject
private EmailEventManager emailManager;
    ...
```
  
Usar este gestor para crear los eventos:
 
``` java
try {
boolean sent = emailManager.sendEmail("EVT_NAME", "user1@test.abc; user2@test.abc", data);
if (sent) {
    // email was sent
} else {
    // email was not sent
}
} catch (EmailEventException e) {
// something went wrong...
}
```

El primer parámetro es el `nombre del evento` que identifica el evento. El segundo es la lista de destinatarios, separada por punto y coma (;) si hay más de uno. Y, por último, cualquier ` Object ` con los datos que se utilizarán para generar el evento. Tenga en cuenta que, aunque estos datos sean algo genérico (`Object`), el tipo real que el listener esperará puede variar dependiendo del evento.

## Escucha de eventos de correo electrónico

Los eventos de correo electrónico son escuchados por clases que implementan `EmailEventContentGenerator`.

Para escuchar un evento, necesita crear una clase de `EmailEventContentGenerator `:

``` java
public class MyEmailGenerator implements EmailEventContentGenerator {
    @Override
    public boolean isValidEvent(String event, Object data) {
    return "EVT_NAME".equals(event);
    }
 
    @Override
    public String getSubject(Object data, String event) {
    return "New email for you";
    }
 
    @SuppressWarnings("unchecked")
    @Override
    public String getBody(Object data, String event) {
    User usr = (User) data;
    return "Hello " + usr.getFirstName();
    }
 
    @Override
    public String getContentType() {
    return "text/plain; charset=utf-8";
    }
 
    ...
}
```

Vamos a explicar los principales métodos a implementar (hay algunos otros explicados en el javadoc):

- `isValidEvent`: Determina si nuestra clase escucha el evento. Internamente, el emailManager itera sobre todas las clases `EmailEventContentGenerator` ejecutando este método; se intenta enviar el correo electrónico en caso de que devuelva `true`. Siguiendo nuestro ejemplo, el nombre del evento que enviamos antes era `EVT_NAME`, por lo que devolvemos `true` para este evento y `false` para cualquier otro. Tenga en cuenta que una única clase podría escuchar varios eventos.

- `getSubject`: Devuelve un `String ` con el asunto del correo electrónico. También recibe los datos, por lo que este asunto puede ser diferente en función de ellos.

- `getBody`: Devuelve un `String` con el cuerpo del correo electrónico. También recibe los datos, por lo que este cuerpo puede ser diferente en función de ellos. En este ejemplo, esperamos que los datos sean un Usuario, por lo que podemos hacer el cast para generar el cuerpo en función de sus atributos.

  
Cuerpos más avanzados pueden componerse usando plantillas freemarker; de este modo es posible que otro módulo sobrescriba la plantilla sin necesidad de realizar ningún desarrollo en Java. En este [cómo](../how-to-guides/how-to-create-a-navigation-bar-component.md#creating-a-template), se explica cómo pueden crearse las plantillas.

---
Este trabajo es una obra derivada de [Cómo enviar correos electrónicos en eventos](http://wiki.openbravo.com/wiki/How_to_send_emails_on_events){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.