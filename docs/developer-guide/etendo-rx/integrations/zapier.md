---
title: Create a Zap using Etendo Integration
---

## Overview

This page explains how to set up a zap between Etendo and a third party application like Google Contacts.

!!! info
    Also you can create a trigger from a third party application to create a new business partner in Etendo following similar steps.

## Zap Setup

1. Create a Zapier account in [zapier.com](https://zapier.com/){target="\_blank"}

2. Create new Zap, selecting Etendo as origin app and Google contacts as destination. Select New Business Partner trigger and create a new contact. Then press Try It.
   ![](/assets/drive/9uVuQ5Irprg2Db9QrZWGSbOjPVy2gYENBjTyaTNMBaFHwlwMS_Algpiwxj-5COzJl1QosJH1yJffVdpINjRg_bX38uKp72z7Vejhaj-lth5CV77Dm3EGmFxNKhnSccbQ7Hnyjbgqm5nI1B31Xw.png)

### Configure Etendo application trigger.

1. Connect to new account:
   ![zap-login.png](/assets/legacy/enduserdocumentation/integrations/zapier/zap-login.png)

> Set Etendo username, password and Etendo Rx public URL, you can try using [https://demo.zapier.etendo.cloud](https://demo.zapier.etendo.cloud), or set up your own server following [Zapier Technical Documentation](https://en/technical-documentation/etendo-environment/platform/modules/integrations/zapier-integrations).
> The user and pasword are "zapier" by default.
>  2. Setup trigger to test connection, and then click continue.
> ![setuptrigger.png](/assets/legacy/enduserdocumentation/integrations/zapier/setuptrigger.png) 3. Test Etendo trigger:
> ![testetendotrigger.png](/assets/legacy/enduserdocumentation/integrations/zapier/testetendotrigger.png)

### Configure Google Contact action

1. Choose a google account and login:
   ![googleaccount.png](/assets/legacy/enduserdocumentation/integrations/zapier/googleaccount.png)
2. Map the name, phone and address in the action and click continue.
   ![insertcontactname.png](/assets/legacy/enduserdocumentation/integrations/zapier/insertcontactname.png)
   ![insertphoneadress.png](/assets/legacy/enduserdocumentation/integrations/zapier/insertphoneadress.png)
3. If you choose to test the action, a new contact with demo information will be created.
   ![sendcontacttest.png](/assets/legacy/enduserdocumentation/integrations/zapier/sendcontacttest.png)
4. Publish and turn on the zap.
   ![publishzap.png](/assets/legacy/enduserdocumentation/integrations/zapier/publishzap.png)

### Create new business Partner in Etendo Classic

1. Log in with default credentials (username and password "zapier") in https://classic.rx.etendo.cloud and create a new business partner on the `Master Data Management > Business Partner` window.
   ![create-business-partner.png](/assets/legacy/enduserdocumentation/integrations/zapier/create-business-partner.png)
2. Setup an address and save.
   ![adress.png](/assets/legacy/enduserdocumentation/integrations/zapier/adress.png)

### Check if the contact was created in Google Account

1. Open https://contacts.google.com/ with the associated account and check if the user was created.
   ![googlecontacts.png](/assets/legacy/enduserdocumentation/integrations/zapier/googlecontacts.png)
   ![testcontact.png](/assets/legacy/enduserdocumentation/integrations/zapier/testcontact.png)
