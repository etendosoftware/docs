---
title: Return to Vendor
tags:
    - Procurement Process
---

# Return to Vendor (RTV)

:material-menu: `Application` > `Procurement Management` > `Transactions` > `Return to Vendor`

This window allows the user to create a Return Material document in case a given product needs to be sent back either to be returned for a refund or replacement, or to be repaired.

## Header

The user can create a purchase order and process it.

Once the Return Material document is accepted by the Vendor, the user can process it by clicking the button **Book**. The document changes from *Draft* to *Booked*.

![Return to vendor window](../../../../../assets/drive/1PKb2NIyq5HtvO_4abDPQjajObdcGFiPH.png)

Only *Booked* documents can be shipped to the vendor.

!!! warning
    Notice the button **Pick/Edit lines** disappears when the Return to vendor document is in status *Booked*.

## Lines

Add products to be included in your purchase order. Each product is added by creating a line.

The Lines tab is not editable, since the returned lines always come from receipt lines, to avoid:

- Seeing positive values while negative in the DB.
- Entering lines that are not linked to the original receipt lines.
- Editing attributes, products and so having either the products or attributes different from the shipment line.

To enter new lines you need to click the process button PICK/EDIT Lines.

**Things to consider:**

- The only editable fields are:
  - **Returned**: Quantity you wish to return. When selecting the row, the quantity is not set by default since the system cannot know how many items return.
  - **Net Unit Price**: Price of the original purchase order.
  - **Return reason**: The reason why you return the item.
  - and **Returned UOM**, only in case \*alternative unit of measure (AUM)\*preference is enabled.
    In that case, product's "primary" AUM for the purchase flow is shown if any, otherwise product's UOM is shown. The user can always change it to product's UOM.

You can define the Return Reason at header level. In this case when picking a line it inherits what selected in the header but you can modify it as you wish.

- Only Material receipt documents that have not been still returned can be picked it, in case a Receipt line has been fully returned it will not be shown.
- When a Receipt line has been partially returned you can still return the rest. What you have already returned for that line is shown in the field **Return Qty other R.**

**Validations:**

- You are not allowed to return more quantity than the **Ship/Receipt Qty**. In case you do it a message is shown.
- Notice that this validation takes into account the **Return Qty other RM** field

!!! info
    To edit a line you need to click again the **Pick/Edit Lines** button and the line appears selected and then you can modify any of the editable fields.

!!! info
    To delete a line you need to unmark the line and then click Done.

## Bulk Completion

!!! info
    To be able to include this functionality, the Essentials Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Essentials Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=39AC2D9F72124AC7A1D0A3D005293C9E){target="_blank"}. For more information about the available versions, core compatibility and new features, visit [Essential Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/essentials-extensions/release-notes.md).

The Bulk Completion functionality allows the user to complete, reactivate or close multiple records by selecting them and clicking the **Bulk Completion** button. This makes records management easier and more efficient, reducing the time spent processing individual records.

!!! info
    For more information, visit [the Bulk Completion module user guide](../../../optional-features/bundles/essentials-extensions/bulk-completion.md).

---

This work is a derivative of [Procurement Management](http://wiki.openbravo.com/wiki/Procurement_Management){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.
