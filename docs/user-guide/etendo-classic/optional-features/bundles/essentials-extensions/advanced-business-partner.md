---
tags:
    - Advanced Business Partner
    - Essentials Extensions
    - Business Partner
    - Sequence
---

# Advanced Business Partner
:octicons-package-16: Javapackage: `com.etendoerp.advanced.businesspartner` 

## Overview
This section describes the Advanced Business Partner module included in the Etendo Essentials Extensions bundle.

<iframe width="560" height="315" src="https://www.youtube.com/embed/sRvQCM8xZE0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

!!! info
    To be able to include this functionality, the Essentials Bundle must be installed. To do that, follow the instructions from the [Marketplace](https://marketplace.etendo.cloud/#/product-details?module=39AC2D9F72124AC7A1D0A3D005293C9E){target="_blank"}.

The **Advanced Business Partner** module allows the user to have a general view of business partners information and to assign sequence numbers to business partners.


## Business Partner General View

:material-menu: `Application` > `Master Data Management` > `Business Partner General View`

The Business Partner General View centralizes all partner data — customer, vendor, and employee information — in a single window, eliminating the need to navigate between tabs to consult or update commercial conditions.

In this window, all business partner information is consolidated in a single form: the Customer, Vendor/Creditor, and Employee sections are visible directly in the main view, without switching between tabs as required in the standard Business Partner window.

![Business Partner General View in form mode, showing Customer, Vendor/Creditor and Employee sections](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/essentials-extensions/advanced-business-partner/advanced-business-partner-3.png)

In grid view, fields from different tabs of the standard window — such as payment method, price list, and purchase pricelist — are available as columns. This allows filtering, comparing, and editing multiple business partners at once without opening each record individually.

![Business Partner General View in grid mode with filter applied on Payment Method column](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/essentials-extensions/advanced-business-partner/advanced-business-partner-4.png)


## Document Sequence

:material-menu: `Application` > `Financial Management` > `Accounting` > `Setup` > `Document Sequence`

In this window, it is also possible to create a **sequence number** for each business partner based on its category. This sequence number can be found in the **Document No** field in the **Business Partner** window.

![image_5.png](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/essentials-extensions/advanced-business-partner/advanced-business-partner-5.png)

For this, you have to set some *preferences* and configure the *sequence number* first, as explained below.

### Preferences

:material-menu: `Application` > `General Setup` > `Application` > `Preference`

In order to configure a business partner sequence number, two preferences must be enabled. These can be found in the **Preferences** window.

#### Auto Business Partner Document No

This property allows the automatic generation of sequence numbers for business partners. The default value is *N* and, in case it is necessary to enable this automatic generation, **a new preference must be created**, but with the value `Y` and the option `Selected` checked. When is disabled, the *Document No* field will be left blank.

![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/essentials-extensions/advanced-business-partner/advanced-business-partner-6.png)

#### Allow Jumps in Business Partner Document No

This property allows jumping among the different document numbers. The default value is *N*, so, it is not allowed to **remove business partners** or **change business partner categories**.

![image_1.png](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/essentials-extensions/advanced-business-partner/advanced-business-partner-1.png)

However, it is possible to **create a new preference** with value *Y*, and the option `Selected` checked to enable this option. When the business partner category is changed, the document number is also changed according to the corresponding document sequence.

### How to Configure Sequences Number

:material-menu: `Application` > `Financial Management` > `Accounting` > `Setup` > `Document Sequence`

To configure the **Sequence Number**, go to the *Document Sequence* window, create a new record for each organization and category, set the corresponding table, column and business partner category, and save the record. The table and column fields must be filled with the options seen below.

![image_2.png](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/essentials-extensions/advanced-business-partner/advanced-business-partner-2.png)

!!! info
    For more information, visit [Sequences](../../../../../developer-guide/etendo-classic/how-to-guides/how-to-use-advanced-sequences.md).


---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.