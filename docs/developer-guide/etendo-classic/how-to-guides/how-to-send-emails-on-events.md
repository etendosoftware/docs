---
title: How to Send Emails on Events
tags: 
    - Send
    - Emails
    - Events 
    - Howto

status: beta
---

#  How to Send Emails on Events

!!! example "IMPORTANT: THIS IS A BETA VERSION"
    This page is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**.
  
##  Overview

Etendo provides a mechanism that allows to programmatically generate events to send emails. Event triggering and email implementation is decoupled, being possible to launch generic events, that are listened by other modules that implement the email contents.

This how to explains both, how to trigger the events and how to listen to them to generate the event.

Email server is [configured](../../../user-guide/etendo-classic/basic-features/general-setup/client/client.md#email-configuration) at client level.

##  Triggering email events

An event is identified simply by a `String`.

Events are triggered programmatically from any piece of code, such as [Processes](../how-to-guides/how-to-create-a-standard-process-definition.md)  or [Business Event Handlers](../how-to-guides/how-to-implement-a-business-event-handler.md).

To trigger an event you need to:

Inject in your class a ` EmailEventManager `

```
    ...
    @Inject
    private EmailEventManager emailManager;
    ...
```
  
Use this manager to create the events:
 
```
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

First parameter is the _event name_ that identifies the event. Second one is the list of recipients, semicolon (;) separated if more than one. And finally, any ` Object ` with the data that will be used to generate the event. Note even this data is something generic ( ` Object ` ), the actual type the listener will expect can vary depending on the event.

##  Listening to email events

Email events are listened by classes implementing ` EmailEventContentGenerator` .

To listen to an event, you need to create a class of `EmailEventContentGenerator ` :

```
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
    return "Hello " + usr.getFirstName;
    }
 
    @Override
    public String getContentType() {
    return "text/plain; charset=utf-8";
    }
 
    ...
}
```

Let's explain the main methods to implement (there are some other ones explained in the javadoc):

` isValidEvent `

    Determines whether our class listens to the event. Internally, the emailManager iterates over all ` EmailEventContentGenerator ` classes executing this method, email is tried to be sent in case it returns ` true ` . Following our example, the name of the event we sent before was "EVT_NAME", so we return ` true ` for this event and ` false ` for any other one. Note that a single class could listen to several events. 

` getSubject `

    Returns an ` String ` with the subject of the email. It also receives the data, so this subject can be different based on it. 

` getBody `

    Returns an ` String ` with the body of the email. It also receives the data, so this subject can be different based on it. In this example, we expect data to be a User, so we can cast it to generate the body based on its attributes. 

  
More advanced bodies can be composed using freemarker templates, in this way it is possible to other module to override the template without needing to do any Java coding. In  this [how to](../how-to-guides/how-to-create-a-navigation-bar-component.md#creating-a-template), it is explained how templates can be created.

---

This work is a derivative of [How to Send Emails on Events](http://wiki.openbravo.com/wiki/How_to_send_emails_on_events){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.