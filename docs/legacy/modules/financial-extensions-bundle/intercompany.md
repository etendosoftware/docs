---
title: Advanced Intercompany Module
---
## **Introduction**

This section describes the Intercompany module included in the Etendo Financial Extensions bundle.

<iframe width="560" height="315" src="https://www.youtube.com/embed/bQjT7iPkYtQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## **Description** 

In case the user has to create orders or invoices among two or more organizations that are different but belong to the same client, this functionality allows automatically generating the corresponding inverse document. 

For example, if Organization A makes a sales transaction to organization B, once the sales invoice is manually created by Organization A, this functionality will automatically create a purchase invoice for Organization B.

## **Installation**

To be able to include this functionality, the Financial Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [_Financial Extensions Bundle_](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558).

## **Set Up**

### **Organization Window**

It is required for each organization using this module to have one business partner assigned.

![](/docs.etendo.software/assets/drive/PlutLfL7AlJBR18T2om4NqgG3qgdPhgtV7vE876GFmU80QIrKOSgJX2AScc0eWEB2TBUAOdVRFIdaOoMIiVZ3FM2IbIHsHSURbzG6sWX0BHArpvjqEk68iMCrwqirI3OD8I2PH3UnFQWiCYW3t5bDK5G8vtpRioFkYRiBab_zup8KCnjTzk6WAUwHw.png)

### **Business Partner Window**

!!! info
    When configuring a new Business Partner, take into account that this business partner should be visible in the inverse organization. 


The Business Partner has to be configured as both vendor and customer, using the corresponding checkboxes.

![](/docs.etendo.software/assets/drive/7bSIJF7R9TzP-VYXO5gkqySKt7G-7YEM5ZRdplKDfRLtoEfc0FUlhr-JctNSn3vItINYI7hiRVZX1l7BV2yoOydAPlu7K4lTb3oKuPdI-k6X5-4JKmDT-q24OQYAHo3FYxFMoB57JitDmgZ3w9Krhf9sXSkXevDHLO00EHXHOjC_zMSY3mgEse7YyA.png)

![](/docs.etendo.software/assets/drive/_S08VOtX0-6seijELCJ5kmLXfIJ93cNS9rIryuyqFFqOMeEC2Uq6zb_HCWjaeg8N-LtXuMRX074PBOERYCsZyV1xibJMiuZe4mde_uyxgvQJjPV9BdEsJK-w8YEeORUaQPXcPebVv3r4QhqCD-3D06jGhZM__U36rx0V2wYbN37w9fHG8o2NRrdYgw.png)

In the Intercompany Documents tab, it is necessary to select the required document types for this business partner.

!!! info
    It is not mandatory to create new document types, but it is recommended.

![](/docs.etendo.software/assets/drive/VT8AxdS0bU_4bD7b8fEIrQF-HK9e2ngLCS5TFjlUBl9ee8W1sysEH9un6GgYTL418D4rvxpIuNOt5JUxLlT2KlJ2UgbXjAZVg4mx6-VexJIx9pwA7yFoY4P0YH1RRd2-hWgMEAnGjZnn9NX53631-9T7MBsxg_RCQP4g1dvj6HqAWMbaECgUfTDT1w.png)

!!! info
    Note: The information in both the source business partner and the target business partner should be the same.

### **Invoices and Orders**

!!! info
    The following information can be applied not only to sales and purchase invoices, but also to sales and purchase orders.

#### Header

The relevant fields are described below:

-   Organization: it is necessary to select an organization configured to work as an intercompany organization (In the following example, the organization “F&B US East Coast”).
-   Business Partner: it is necessary to select a business partner configured to work as an intercompany business partner (In the following example, “Be Soft Drinker, Inc.”).
-   Transaction document: it is necessary to select the document type defined in the intercompany document tab of the business partner (In the following example, the document type “AR Invoice Intercompany”).

![](/docs.etendo.software/assets/drive/CBJAHylu5avoOLB0cuF8RTZZUJFtzQYm24KaV3eRWOB_6H7njxPoJ4ujK_0ZcvPokD8O3q3NZ2B3P4rEASGLEjM9Dadp9YnTsO1hSFBzAMdea3A_OfAUO-T0-BxhX2zqRF_Mh0UsY9ujTx2Pbrjy1TOxp5kpd4QC8fklcmTtfsJMnfrVwUvT7CexMA.png)

#### Lines

The relevant fields are described below:

-   Product: The product must be visible for both organizations (In the following example, “Lemonade”). 
-   G/L items: The necessary G/L items must be visible for both organizations.

![](/docs.etendo.software/assets/drive/Q8Xn1rgR7uOHOSOr_h_l0ITlepOcHfRklfLTj8awb46t_jUCBKoV3-91JsVU5eGDQY2std_xbpvz0b-APJI11e2o9W4epq9rzioSoPB4XdWsnUpZhnCO2jkLmRinTSv4sPHUM3aODSmHiXfyQL320QR_lE8xpOD3whK6lYeLaMCafXC0G9UrVzZakA.png)

#### Product Window

The relevant fields are described below:

-   Price: The price must be equivalent and available in every price list. 
-   Currency: The currency must be the same for both organizations.
-   Tax: The tax in each organization must be equivalent.

#### Complete or book documents

When you complete invoices or book orders, these processes generate the corresponding inverse document and complete or book both the source and the target documents.

![](/docs.etendo.software/assets/drive/op4ZxMClAuIecT10AFiO_n2ecoldgryLCVCYAnyWtjFgkDTaghYPrLdZ6bnDxWnykm_HGTLSmG6SkKQOtp45GnOVk3AgLm2Tbud2Lf1zR0Hsie0HE74sD93Rvl1GDfnFOWEWQVKEAfiuVZzja68OrmqgedNsOCsQ2TbrxzB41wmakZZvGBAscWqiEA.png)

#### Reactivate documents

To reactivate intercompany documents, both documents should not have an associated payment.

!!! info
    Note: This process is only allowed for source documents.
