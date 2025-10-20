---
title: Alert
tags:
    - Alert
    - Notifications
    - Monitor
    - Alert Rule
---

:material-menu: `Application` > `General Setup` > `Application` > `Alert`

### Overview

Alerts are notifications which inform about events happening whenever an alert rule has been properly defined to monitor those events.

The way "_Alerts_" work in Etendo is described below:

- Alert rules need to be previously defined as SQL queries. SQL queries define the event that is going to be monitored.  
  For instance, _"Products without a defined price"_, _"Products under stock"_ or _"Bank account without accounting information"_
- An alert rule can be applied to every Etendo user or just to a set of them. Alert recipients are the Etendo users for which a given event is going to be monitored.
- An Etendo background process is permanently checking if the SQL query defined in each of the active rule alerts return any record.
  - If that is the case, Etendo creates and returns a new _alert instance,_ which is saved in the _"Alert Management"_ window in _"New"_ status.

The _number of alerts instances_ informing about events being monitored happening is shown in the "Top Navigation" menu:

![](../../../../../assets/drive/z341Sqx0_VIs2wSRDSm-6Jlq_2MmxWxxFa406LPjtgffjFTdFIds94ov5CwjlKGP7vDSEyxAdiYnVGN3m0AaIZjGIz2WkrZSmPlCagaI-KmACHhix0-qaazsTFjJ3D9sG0sTkbHv.png)

Alerts instances can be visualized and managed in the _Alert Management_ window which is opened by clicking the "Alert" option of the Top Navigation menu.

![](../../../../../assets/drive/-wFUIZt2K33Chbp-czLqJmO7f1hP5fcD2jkcZaI7CtnhlHHbdh7lk1_ayiFKbrcfx8slOlIXVjeiIe15gmt_CkcTwhWQGhAbfXXGCMaF6-ba5l_OGBnMsKpP8CkL23o7AwzywwMX.png)

Alerts can have 4 different status:

- _New_ - new alerts instances which reflect the events monitored happening.
- _Pending_ - acknowledge alert instances for which an end-user action is pending to be done to get them solved or fixed.
- _Ignore_ - not applicable alert instances which must be ignored.
- _Solved_ - alert instances solved as the event happening is fixed or solved.

The way to manage alerts instances is by manually selecting and moving them to the next or previous status once they are manually acknowledged, ignored or solved.

### Alert Rule

Alert window allows the definition of alert rules as SQL queries which define the event to be monitored and how it will be monitored.

Alerts are defined by entering below data:

- The _"Name"_ of the alert which is the event to be monitored.
- The _"SQL"_ query.
- and the _"Tab"_ where the alert instance can be fixed or solved.

![](../../../../../assets/drive/7FDlwrebuc8IysmRIryYm81mF7QPheC-khbM3NdpZUdAIlXzkhZMDvasxwUPYPDMEyJcP_oM5t16sfAW3ZOCyVNUmR8nE4WWZkLYexMWFuKDHaCb0j8Axa1AetNm9j5rEVq36Kri.png)

#### Translation

Alerts can be translated to any language required.

#### Alert Recipient

Alerts can be allocated to specific users or contact or to all of them.

!!! warning
    If no _Role_ or _User_ is configured in the _Alert Recipient tab_ of a given alert, that alert will apply to any Etendo user or role.

Etendo supports alerts notification to user or roles by email:

- for this, it is required to properly configure _e-mail_ server, account and password for the corresponding client in the header of the Client window, section "Request Management".

#### Alert

Alert tab list the events happening which generate the corresponding alert.

![](../../../../../assets/drive/qRqaP9bx7a04XzXIrzdpZZ3eS3OaglF9SMM3xvRYaL3Vrkhcxz_EI5BxPbtrnQoW_DXad8d-_oQBJntpSgZdchM9RtWisxif2I3GWPM2Yda4XlbPG_kkWIqlvgDl5cvOObV43F4W.png)

---

This work is a derivative of [General Setup](https://wiki.openbravo.com/wiki/General_Setup){target="_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="_blank"} by [Etendo](https://etendo.software){target="_blank"}.