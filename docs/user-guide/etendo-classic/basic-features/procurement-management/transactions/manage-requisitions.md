---
title: Manage Requisitions
tags:
    - Procurement Process
    - Purchase Requisitions
---

# Manage Requisitions

:material-menu: `Application` > `Procurement Management` > `Transactions` > `Manage Requisitions`

Manage Requisitions window is intended to be used to provide an overall picture of the items needed.

## Header

This window allows the user to manage requisitions regardless of their current status, therefore they can change or close a requisition and create purchase orders for those demands.

![Requisition window Header](../../../../../assets/drive/1yuE4xa0usvVzSdmthjDWdi12OAqTuJTe.png)

A **requisition** with status "Completed" **can always be changed**, if required. The user needs to reactivate it and then change it and book it.

It is also possible to **close a requisition in case there is no need of the included item/s anymore**, by using the menu button "**Close**" and then select the action "**Close**".

Requisition lines status will then be changed to "Cancelled".

Finally, it is also possible to **create purchase orders** for those **requisitions in status "Complete"**, by using the menu button "**Create Purchase Order**".

In this case, a new window is shown for the user to fill in some data by taking into account that:

- If there are **different suppliers in the requisition lines as well as price list**:
  - the **defaulted ones** entered in the window "Create Purchase Order" **will be the ones used** in the purchase order.
- If there are **different suppliers in the requisition lines as well as price list**, and the user does not enter any defaulted ones in the window "Create Purchase Order":
  - **the ones in the requisition lines will be the ones used** in the purchase orders.
- If **all the requisition lines have the same supplier and price list**:
  - **there will not be any need for selected defaulted ones** in the window "Create Purchase Order", besides only one purchase order will be created.

![Purchase order](../../../../../assets/drive/17OuNS8YpM0VC3MUkLO25DPPHCMwWjq8u.png)

Etendo provides information about the purchase order/s number/s created after pressing the OK button in the "Create Purchase Order" window.

This action links the requisition and the purchase order, and besides a purchase order line is created for each requisition line:

- A **requisition** linked to a purchase order changes its status from **Completed** to **Closed**.
- A **requisition line** linked to a purchase order line changes its status from **Open** to **Closed**.

Any **purchase order** created from a **Requisition**:

- will be listed in the **"Purchase Order" window**.
- will have a "**Booked**" status
- and will contain **data inherited from the Requisition**, data such as:
  - Order Date
  - Scheduled Delivery Date
  - Business Partner
  - Price List
  - Product/s

## Lines

The user can perform a set of actions regarding requisition lines. It is possible for them to either create lines or product demands or to cancel them.

- **New product demands can be manually created** within a requisition by just **adding new requisition lines** before creating a purchase order.
- **Existing product demands or requisition lines can be cancelled**, if they are not required anymore, by using the header button "**Change Status**".

### Matched PO (Purchase order) Lines

This tab allows the user to either review the purchase order line automatically linked to a requisition line or to manually link an existing purchase order line to the corresponding requisition line.

---

This work is a derivative of [Procurement Management](http://wiki.openbravo.com/wiki/Procurement_Management){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.
