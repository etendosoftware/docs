---
title: Session Preferences
tags:
    - Session
    - Preferences
    - Settings
---

:material-menu: `Application` > `General Setup` > `Application` > `Session Preferences`

Session preferences allow showing or hiding accounting tabs or translation tabs for a given user, role, client and organization.

![](../../../../../assets/drive/VAr7jhdNC8mm1JlSp-Jq-dBswsbSAMKpcuq_Tg6_Z3yKcxRbc3N8IgLn-gimlxHoPzGvtOl0i3k7wPCdqKKG8zO1xgcS5xvh-sC1T0yO2qeanxvBMqt-P8TUPDo9n-ASz4p2LjaL.png)

As shown in the image above, session preferences window allow the user to setup a list of session preferences for the user, the role, the client and the organization entered while login in Etendo.

That user will need to have access rights to this window to get these preferences setup.

Available session preferences which can be shown or hidden are:

- **Enable Accounting** (previously called _Show accounting tabs_), this option allows showing the tabs defined as "accounting tabs" in a window, besides this option allows showing the process buttons that "Post" a document.  
  The complete list of accounting tabs is listed below. This option if selected set the "ShowAcct preference to "Yes".

|                                |                              |
| ------------------------------ | ---------------------------- |
| Window Name                    | Tab/Sub-Tab Name             |
| General Ledger Configuration   | General Ledger Configuration |
| General Ledger Configuration   | Documents                    |
| General Ledger Configuration   | General_Accounts             |
| General Ledger Configuration   | Defaults                     |
| Accounting Transaction Details | Header                       |
| Asset Group                    | Accounting                   |
| Asset                          | Accounting                   |
| Business Partner               | Customer Accounting          |
| Business Partner               | Vendor Accounting            |
| Business Partner               | Employee Accounting          |
| Business Partner Category      | Accounting                   |
| Financial Account              | Accounting History           |
| Financial Account              | Accounting Configuration     |
| Financial Account              | Accounting                   |
| G/L Item                       | Accounting                   |
| Product                        | Accounting                   |
| Product Category               | Accounting                   |
| Tax Rate                       | Accounting                   |
| Warehouse and storage bin      | Accounting                   |

- **Show Translation tabs**, this option allows showing translation tabs.  
  Translation tabs are shown in many Etendo windows. This option, if selected, sets the "ShowTrl" preference to "Yes".
- **Show Audit** - same way, this option allows showing the Audit Trail information. Audit Trail information can be found as well in many Etendo windows under the group section "Audit".  
  This option, if selected, sets the "ShowAuditDefault" preference to "Yes".
- **Theme or skin** - there are two possible options, "Default" or "Classic" skin or "2.50 to 3.00 Compatible".
- **Transaction Range** - this one is about the number of days (counting backwards from current day) used in the implicit filter of sales order or purchase order by example. Implicit filters are the filters used not to show documents that have been completed the last x days to avoid overflow.
- **"Records Range"** and **"Selector registry range"** only applies to 2.50 views. Etendo 3 allows scrolling down to see all the records in a window, tab or selector.

Finally, the **Save Preferences** button allows saving the changes.

---

This work is a derivative of [General Setup](https://wiki.openbravo.com/wiki/General_Setup){target="_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="_blank"} by [Etendo](https://etendo.software){target="_blank"}.