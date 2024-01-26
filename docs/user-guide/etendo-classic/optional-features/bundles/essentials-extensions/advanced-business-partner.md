---
title: Advanced Business Partner
---
## **Introduction**


This section describes the Advanced Business Partner module included in the Etendo Essentials Extensions bundle.

<iframe width="560" height="315" src="https://www.youtube.com/embed/sRvQCM8xZE0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

!!! info
    To be able to include this functionality, the Essentials Bundle must be installed. To do that, follow the instructions from the [Marketplace](https://marketplace.etendo.cloud/#/product-details?module=39AC2D9F72124AC7A1D0A3D005293C9E){target="\_blank"}.

The “Advanced Business Partner” module allows the user to have a general view of business partners information and to assign sequence numbers to business partners.

#### Business Partner General View

In this window, it is possible to see all the business partner information of each record, grouped in the customer, vendor/creditor and employee sections of the header. In the original window “Business Partner”, this information is found in different tabs.

![image_3.png](/assets/legacy/image_3.png)

This change implies, in grid view, the user is able to create, modify and filter business partner information according to their needs.

![image_4.png](/assets/legacy/image_4.png)

#### Sequence Number by Business Partner Category

In this window, it is also possible to create a sequence number for each business partner based on its category. This sequence number can be found in the Document No. field.

![image_5.png](/assets/legacy/image_5.png)

For this, you have to set some preferences and configure the sequence number first, as explained below.

#### Preferences

To be able to configure a business partner sequence number, two preferences are set by default. These can be found in the “Preference” window.

##### Auto Business Partner Document No

![image_6.png](/assets/legacy/image_6.png)

This property allows the automatic generation of sequence numbers for business partners. The default value is Y and, in case it is necessary to disable this automatic generation, a new preference must be created, but with the value N and the option “Selected” checked. In this case, the Document No field will be left blank.

##### Allow Jumps in Business Partner Document No

![image_1.png](/assets/legacy/image_1.png)

This property allows jumping among the different document numbers. The default value is N, so, it is not allowed to remove business partners or change business partner categories. However, it is possible to create a new preference with value Y to enable this option. When the business partner category is changed, the document number is also changed according to the corresponding document sequence.

#### How to Configure Sequences Number

To configure the Sequence Number, go to the “Document Sequence” window, create a new record for each organization and category, set the corresponding table, column and business partner category, and save the record. The table and column fields must be filled with the options seen below.

![image_2.png](/assets/legacy/image_2.png)

!!! info
    For more information, visit [Sequences](/developer-guide/etendo-classic/how-to-guides/how-to-use-advanced-sequences/).