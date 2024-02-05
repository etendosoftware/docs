---
title: Etendo Webhooks | Technical Documentation
---

:octicons-package-16: Javapackage: com.etendoerp.webhookevents

## Overview

This documentation will guide you through the process of setting up and using webhooks in Etendo Classic. Webhooks allow you to execute actions via a URL call, providing a powerful way to integrate with external services.

## Description of Webhook header fields

| Variable        | Description                                                |
|-----------------|------------------------------------------------------------|
| Name            | Webhook name                                               |
| Description     | Webhook description                                        |
| Event Class     | Event class in which the webhook service was created       |
| Java Class      | Class in which the webhook service was created             |
| Module          | Module in which the webhook will be created                |
| Organization    | The client’s organizational entity.                        |
| Active          | Webhook status (Active by default)                         |

## Setting up Webhooks

1. Navigate to the new menu option: `Application → General Setup → Application → Webhook Events → Webhooks`
2. Create a new webhook by filling in the required fields:

    | Variable        | Value                                                      |
    |-----------------|------------------------------------------------------------|
    | Name            | Alert                                                      |
    | Description     | Create alert with custom message                           |
    | Event Class     | Java                                                       |
    | Java Class      | com.etendoerp.webhookevents.ad_alert.AdAlertWebhookService |
            
    ![Webhook Alert](/assets/developer-guide/etendo-classic/bundles/WebhookAlert.png)

3. Focus on "Params" tab and create the following params:

    | Variable        | Value                    |  Is required       |
    |-----------------|--------------------------|--------------------|
    | Name            | description              | :white_check_mark: |
    | Name            | rule                     | :white_check_mark: | 
        
![Webhook Params](/assets/developer-guide/etendo-classic/bundles/WebhookParams.png)
        

## API Key Generation

1. To give execution permission to a user, go to: `Application → General Setup → Application → Webhook Events → User API Token`
2. Create a new API with the Name: `<<user>> token`
3. After saving, run the “Get API Key” option, and save the resulting token (64-length random string) to your clipboard.
    
![Webhook Token](/assets/developer-guide/etendo-classic/bundles/WebhookToken.png)
    

## Assigning Webhook Access to Users

1. Navigate to: `Application → General Setup → Application → Webhook Events → Webhooks`
2. Select the created webhook and open the access tab.
3. Create a new row and select the previously created API record.

![Webhook Access](/assets/developer-guide/etendo-classic/bundles/WebhookAccess.png)

## Executing the Webhook

To execute the webhook, make a GET request using a REST client like Postman with the following syntax:

```
URL=http://localhost:8080/
CONTEXT=etendo
WEBHOOK_ENDPOINT=/webhooks/
[VARS]
WEBHOOK_NAME=name=alert
APIKEY=8b1012f0d442406ed602d87c13edcee9
DESCRIPTION=new alert description
RULE=649BBFA37BA74FA59AEBE7F28524B0C8
```

Example URL:

```
http://localhost:8080/etendo/webhooks/?name=Alert&apikey=<api-key>&description=new alert description&rule=649BBFA37BA74FA59AEBE7F28524B0C8
```

!!! success
    This webhook creates an alert, and you can visualize it in the "Alert Management" window.

    The response will return a status code **200** and the **alert ID**, for example: 
    ```
    {
      "created": "91FEABC1604E404CB565FC79435C4344"
    }
    ```


## Example code usage

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

## Use Cases

### Tokens Visibility

!!! note
    :eye: Users can visualize tokens of their current profile.

!!! warning
    :warning: Other users cannot access another user's token. The API Token Window and webhook access tab will be empty.

### Error Handling

!!! failure
    If a user calls a webhook without a token or includes an incorrect API token, the backend will respond with a **401** response and a message.

!!! failure
    If a user calls a webhook with an incorrect webhook name, the backend will respond with a **404** response and a message.

!!! failure
    If a user calls a webhook without access, the backend will respond with a **401** response and a message.


!!! failure
    If a user calls a webhook with a missing required parameter, the backend will respond with a **500** response and a message.

!!! failure
    If a user calls a webhook without a newly required parameter (after the backend configuration is changed), the backend will respond with a **500** response and a message.

!!! failure
    If a user calls a webhook with revoked access, the backend will respond with a **401** response and a message.