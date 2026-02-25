---
title: Return to Vendor Shipment
tags:
    - Procurement Process
---

# Return to Vendor Shipment

:material-menu: `Application` > `Procurement Management` > `Transactions` > `Return to Vendor Shipment`

From this window, the user can deliver the returned goods to the vendor.

## Header

The user can create and edit a goods receipt.

The **RMA vendor ref.** field is populated automatically or not based on:

- If it is filled before selecting a line, then it will not be populated automatically to avoid override it.
- If you select a line/s where all of them belong to the same Return to Vendor document, it will be populated automatically.
- If you select a line/lines but one of them belongs to a different Return to Vendor document, then it will not be populated automatically.

Once the document is ready, you can process it by clicking the button **Complete**. The document changes from *Draft* to *Completed*.

!!! warning
    Notice the button **Pick/Edit lines** disappears when the Return to vendor document is in status *Completed*.

![Return to vendor shipment](../../../../../assets/drive/1wuiYHH8xsIwjLRgp0VzWUqAtev43BzD8.png)

To invoice these documents you must use the **Purchase invoice** window. All scenarios are covered:

- If the vendor sends an invoice just for that specific document you need to select a *Reverse purchase invoice* document type and then select the lines through the *Create lines* from button.
- If the vendor sends an invoice with the original purchase order plus the return materials order you need to select a *Purchase invoice* document type and then select the lines through the *Create lines* from button.
- If the vendor does not send an invoice for the return materials order but wants to keep it as credit where you can use it later, you have to:
  - Create a *Reverse purchase invoice* for these returned materials.
  - Leave it as credit to be used later through the **Payment out** window.
  - When you create the Purchase invoice for the original Purchase order you can consume that credit.

## Lines

Add products which are included in your goods receipt. Each product is shown on its own line.

The Lines tab is not editable, since the lines always come from return to vendor lines, to avoid:

- Seeing positive values while negative in the DB.
- Entering lines that are not linked to return lines.
- Editing attributes, products and so having either the products or attributes different from the return line.

!!! info
    To enter new lines, the user needs to click the button PICK/EDIT Lines.

**Things to consider:**

- Editable fields are:
  - **Ship Qty**, that value is set automatically when you select the line,
  - and **Returned UOM**, only in case an alternative unit of measure (AUM) preference is enabled, regardless product's UOM is always shown there by default.
    The user can change it if required, to the product's primary AUM configured for the procurement flow.
- The user can only select Return to Vendor lines that are pending to be shipped to that specific vendor.
- The system proposes the different storage bins from where the item can be picked. Depending how the product is configured we could have three scenarios:
  - Product with an instance attribute (i.e: Serial number): The system will propose only one storage bin as it is shown above.
  - Product with a non-instance attribute (i.e: Colour): The system could propose several storage bins. See below image
  - Product without attributes. Similar to second scenario.

**Validations:**

- You are not allowed to ship more than the **Available Qty.**
- You are not allowed to ship more than the **Pending** quantity.
- The system also validates you cannot ship more than the **Pending** quantity when selecting both lines.

!!! info
    To edit a line, you need to click the **Pick/Edit Lines** button again, the line appears selected and then you can modify any of the editable fields.

!!! info
    To delete a line, you need to unmark the line and then click Done.

If there is not enough available stock for a product in a selected line, then it will be possible to define a Ship Quantity and select it. if there is at least one storage bin with overissue inventory status for the Return To Vendor Shipment's warehouse, in this case the new line will use it as storage bin and it will create a negative stock when the document is processed.

### Accounting

The RTV shipment can be posted **if the table "MaterialMgmtShipmentInOut" is** active for accounting **in the corresponding general ledger configuration.**

## Bulk Posting

!!! info
    To be able to include this functionality, the Financial Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}. For more information about the available versions, core compatibility and new features, visit [Financial Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

The Bulk Posting functionality allows the user to post or unpost multiple records by selecting the corresponding records and clicking the **Bulk posting** button.

Also, the Accounting Status of the record/s is shown in the status bar, in form view, or in a column, in grid view.

!!! info
    For more information, visit [the Bulk Posting module user guide](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).

---

This work is a derivative of [Procurement Management](http://wiki.openbravo.com/wiki/Procurement_Management){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.
