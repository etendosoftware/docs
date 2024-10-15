---
title: Etendo Classic Subapp Extensions
---
:octicons-package-16: Javapackage: `com.etendoerp.classic.subapp.extensions`


## Overview

This bundle includes the Etendo Classic Mobile Sub-Application and the Etendo Copilot Sub-Application. Also it includes the configurations in Etendo Classic. 

!!! info

    - Initially, add Etendo Classic Subapp bundle in Etendo Classic. <br>
    To be able to include these sub-applications, the Classic Subapp Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Classic Subapp Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=55A7EF64F7FA43449B249DA7F8E14589){target="\_blank"}. <br>
    For more information about the versions available, core compatibility and new features visit [Etendo Classic Subapp Extensions - Release Notes](../../../../whats-new/release-notes/etendo-mobile/bundles/classic-subapp-extensions/release-notes.md).

    Once the sub-application module is installed in Etendo Classic, the dynamic app will be configured and the apps will be available. Acces must be given to each role from the [Dynamic APPs tab](../../getting-started.md#dynamic-app-role-configuration) in the Role window.


!!!info
    For more information read [Etendo Mobile](../../../../user-guide/etendo-mobile/getting-started.md).


## Etendo Classic Sub App

### Overview

The **Etendo Classic SubApp** is a mobile extension of Etendo Classic, offering users a efficient way to access key business windows based on their role. 

The Etendo Classic Sub-application allows users to access and manage their client’s information directly from Etendo Mobile, providing a quick and efficient way to view data. In addition, thanks to features such as **scanning assistant**, users can see a demonstration of inventory management by scanning products during physical inventory.

### Initial Configuration

To allow Etendo windows to be visible in the sub-application, the user must enter to Etendo Classic under the **administrator** role in `Role`>`Window Access` tab and check the box **Show in mobile** in the required windows to be shown in the app.  

![](../../../../assets/drive/WgAVMD7_UawKp1eedwjq260FyWU41AFdrcP_bK3sS3mm1aM6ZVT7oCnfTd8eiydWSDKpSRQf9eAspqn0PCCNK2sLLd9i_77-LObYTJmA3QbSXK5I4hKxhqT-9Ux788FRmZRdBaZQ.png)

### Welcome Window

In the Welcome window, the user can enter Profile, Settings and Navigation Menu.

![](../../../../assets/user-guide//etendo-mobile/user-interface/HomeSubApp.png){ width="300"}


### Navigation Menu

In the Home option, the user can find an option menu from which they can access to different windows allowed according to their role. From this menu, it is also possible to:

- Go back (Option to Go back to Etendo Mobile)

![](../../../../assets/user-guide/etendo-mobile/user-interface/DrawerSubApp.png){ width="300" }

In the top section of the menu, the name and the user picture will be shown.

### Functional Windows

The user, according to their role, will have access to certain windows. The most common ones are: Product, Business Partner, Sales Invoice, Sales Order, Purchase Invoice, Purchase Order, among others.

The access to these windows are represented by folder icons with their corresponding name.

Each window will show its content splitting the records in small boxes, which will contain a preview of main data of these records. That data is configured by default and a customization must be required in case the user wants to add more fields to eliminate some of them, considering that only a max of 5 fields can be displayed.

The same field present in the preview, will be the criteria by which it is possible to filter if the user wants to search for a record.

Considering as an example the Sales Invoice window, the preview of each record provides information regarding the document number and invoice date.

![](../../../../assets/drive/XZFZ8AALW9g42_1StbQnRpAvIszHoPZrp6QoLw1XUQ68kz4iU5nBYCR6XVwC0k4bGJjZFRbjaGMKfOA7lUVXCtz7At6Tt5p8sJtlYHNny4Z6yn_jfHrthRnxym2n_M0GhXLWDR2p.png){ width="300" }

By clicking any of those boxes, detailed information about the records will be displayed.

The fields will be displayed one below the other. Those with this symbol  “(\*)” in their title are mandatory and those with a pencil icon are editable.

![](../../../../assets/drive/PY4-klREGqUyi4CtP-0Pp3gn95-eE8hr2lCDLVA4uiYTTYNTnx3exMDsx-LHTSXK5NQBo0z0Xy4sxXera3xgCpISdVbxwMzB3QjurnDInYR5oSvUqfBYDtvbElXXneXCZi8AzJmA.png){ width="300" }

**Folders button** 

By selecting the Folders button, the user can access the different tabs of the window with information about the records being browsed.

![](../../../../assets/drive/Q0C8H4uO8zHgfmSaWfGMKR5tKMbWlVLOUwUMYG-_qpJBj471MxMFwx0is-MGR0WqleOE4QcqHhWhIhTfeo2xwIX-ftECC3QyeKdI-ygG7o2kGhHJ4CgAoWEgfc1KZnEHHXpaegHG.png){ width="300" }

When entering any of the tabs, the view will be the same as in the parent window, e.i., the records will be displayed in small boxes and, when entering these, the fields will be displayed one below the other.

![](../../../../assets/drive/XKeIfzzgutwdnJr5kmBVSifBZ1luxaWe3mqYM_U3uHurbAe_0TXkpjjvF5x0RWpIKXRsqYcEifdxpVeNHZjgHZ5-s6uGm8FjIf9RGIfAZoHXZAxlCqzC5H00RUmPBX01SvFgW8v2.png){ width="300" }

![](../../../../assets/drive/PAfojHNtSzl7SKh6VFDroECbrO7Y0ZSYSnyvDieVQxBZkvATVhtJtNPm6PTpeuLOjzdIB-PIRR-wD1SGCZrHJLdKnhnacGsFhWDSyuOUWlhlMnJ74guN7EsUE2sshKzFyoHn2tiT.png){ width="300" }

To navigate in different levels, the user can resort to the system buttons (Android) or the arrow in the upper left corner or gesture (both systems).

In addition, the **path or breadcrumbs** of which records and tabs are being navigated can be displayed at the top of the screen.

**Actions button**

Through this button, the user can access the list of available processes corresponding to the window being browsed and execute them.

**Attachments button** 

Through this button, the user can attach files.

### Manage Records

**Create a record**

To create a new record, the user must click the icon with the symbol “+” and complete the desired fields. Those with the symbol (\*) are mandatory.

To edit a field, the user must click the pencil icon. If the field is a list field, click the search icon to display possible options. After selecting the correct data, press the button “Done”.

![](../../../../assets/drive/3tj34fwiEnwX6YiWsfv8x8ApOWqEjbtQDFERLIEqZJ6LZsXwvlkJffOm-UYEhS1y0onXLf3rtWKy75WpIqy_pn8KSITpMqW6Olqx5CNaGo5vGpex61Tj7WuCy0NxSAjdGUM0hqyt.png){ width="300" }

If the field is a date type, when selecting the search icon a calendar to select the desired date will be displayed.

![](../../../../assets/drive/pJrdHx58VtWi5NCkN446WAu-Fjg1rHgWe5JJLKGFn7DJxasB8uXnXAtSPrI6gAD_Oe_3ZwkK0Pw9JYVPY6GX0R1a2-mUuYESxwzPpWOf02V0T1jskkbxUy5IddR1m2glXXbcBpJd.png){ width="300" }

Free text fields are edited by selecting the field and entering the desired value.

Once the user has entered the required data, click the save icon.

When the Header is complete, data can be entered in the tabs. To do so, access through the Folders button and edit the required fields, in the same way as in the main Header.

Each time a new record is created in the App, the same record will be created in the Etendo Classic as well.

It is important to consider that the document will always remain in **Draft** status and can only be completed through the Etendo Classic.

**Delete a record**

To delete a record, press it and drag it to the left or hold it, select all the desired records and then the delete icon.

Each time a record is deleted in the App, the same record will be deleted in the Etendo Classic as well.

![](../../../../assets/drive/dGqkvbLqxGUxpuU75pgKmYjRffl9bHRLmydMSokrcPVdjhBcnIrUNzxvHzGCvCD_2QDmdE2NlAmc0FuXi11ZeNoUPvwhavOdv1jvTD1IyRgA4MKF9mhD6nCmIU-xV7mEV8DrFnb7.png){ width="300" }

**Edit a record**

To edit a record, select the record and then the field to be edited.

Once the changes have been made, press the save icon.

Each time a record is edited in the App, the same record will be edited in the Etendo Classic as well.

**Search a record**

Records can be searched by inserting a value or keyword in the top **Search** bar. This search bar is located both in the main view of each window and in each tab.

Each window will have certain filters available by field which will match those fields configured by default to be displayed in the preview of each record.

In case the user needs to add more filters or to remove some of them, customization will be required.

Continuing with the example of the Sales Invoice window, the available filters are the document number, which will be entered in the search bar together with the invoice date.

![](../../../../assets/drive/akwqHJKCawDOW20SxB5sxjm_wPN2hW8PfKsU8wAgfYqebtFGAbyTib-mQcX_fUuRhCz9RTDX0Utt1pY0GUF1HuzfwGig3LaOdFdHHLMK2p0DjLUWcvxxYW2agJCmHTx_JRB-8sgp.png){ width="300" }

### Mobile App Scanning Helpers

:octicons-package-16: Javapackage: `com.smf.mobile.scan`

The **Mobile App Scanning Helpers** allows to use the camera to scan codes in [Etendo Mobile](../../../../user-guide/etendo-mobile/getting-started.md) App.

#### Usage Examples

 The module has the Inventory Scan process by default, which is responsible for scanning this code from a mobile and thus, change values of the Physical Inventory lines.

 Now, an example will be shown from the Etendo Mobile application:

 When entering the Physical inventory window and select a record, it will be possible to see the **Actions** button.

 ![](../../../../assets/developer-guide/etendo-classic/bundles/PhysicalInventoryActions.jpeg)

In this button, it is possible to see the process it incorporates, called Inventory Scan.

 ![](../../../../assets/developer-guide/etendo-classic/bundles/ActionsInventoryScan.png)

 When pressing this action, it performs the scanning functions to be able to modify values of the physical inventory item that has been selected.
 
 ![](../../../../assets/developer-guide/etendo-classic/bundles/CameraScanner.png) 

When the arrow to continue is selected, the code of the storage bin in which the product is located must be entered manually or scanned.

 ![](../../../../assets/developer-guide/etendo-classic/bundles/StorageBinBarCode.png) 

 After selecting the storage bin, the product to be modified must be scanned or selected.

 ![](../../../../assets/developer-guide/etendo-classic/bundles/ProductBarcode.jpg) 

 Finally, enter the amount needed to add of that product, press Done and Save.

 ![](../../../../assets/developer-guide/etendo-classic/bundles/ProductQuantity.png) 

 In the meantime, in Etendo Classic a line will be added in the **Scan** tab of the physical inventory line, about the scan and the amount that has been set.

 ![](../../../../assets/developer-guide/etendo-classic/bundles/QuantityCount.png) 

In the physical inventory header, by selecting a scan line, the Process Inventory Count can be run. This takes care of adding to the stock the quantity that has been set on the scanned product.

 ![](../../../../assets/developer-guide/etendo-classic/bundles/Process.png) 

And here, the quantities will be observed before the process:

 ![](../../../../assets/developer-guide/etendo-classic/bundles/QuantityBefore.png) 

 And after:

 ![](../../../../assets/developer-guide/etendo-classic/bundles/QuantityAfter.png) 

It will also be noticed that the Product's Stock has been updated in the indicated storage bin with the quantity of the product:

 ![](../../../../assets/developer-guide/etendo-classic/bundles/ProductStockAfterProcess.png) 


## Etendo Copilot SubApp

:octicons-package-16: Javapackage: `com.etendoerp.subapp.copilot`

### Overview 

The **Etendo Copilot Subapp** is designed to integrate seamlessly with the existing features of Etendo Copilot, extending its functionality to mobile and tablet devices. This subapplication allows users to interact with AI-driven copilot assistants directly from their mobile devices, enhancing productivity and accessibility on the go.

The Etendo Copilot Subapp offers key features such as the ability to **attach files, interact with Copilot assistants, and access specific windows** based on the user’s role. The assistants dynamically appear according to the user’s assigned role, ensuring a personalized experience tailored to their responsibilities within the system.

With compatibility for both mobile phones and tablets, this subapplication ensures flexibility in how users can access and leverage the Copilot assistants, facilitating smoother workflows across different devices.

**Copilot SubApp mobile mode**

![alt text](../../../../assets/user-guide/etendo-mobile/classic-subapp-extensions/etendo-copilot-subapp1.jpg){ width="300" }

**Copilot SubApp tablet mode**

![alt text](../../../../assets/user-guide/etendo-mobile/classic-subapp-extensions/etendo-copilot-subapp2.png)


