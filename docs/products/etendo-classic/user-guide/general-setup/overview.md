---
title: General Setup
---

## Overview

This section describes the steps that need to be performed first to configure Etendo.
Etendo installations require at least a **Client** and an **Organization**. Client and Organization are the two key concepts within the General Setup.

In other words, it is not possible to issue an invoice or to post a journal entry to the ledger in Etendo, if there is no Client and Organization properly created and configured.

The first steps to follow to configure Etendo are:

- The **Installation of the** **Localization Packs** if available for the country.

Etendo can be localized for any country thanks to a key Etendo feature which is Modularity.

A Localization Pack can include at least:

-the complete **translation** for the official language(s) in the country.
The language is automatically available once the localization Pack has been successfully installed, therefore it can be selected as described at [profile](/docs/getting-started/user-interface/workspace#profile).

-the **chart of accounts** that defines the accounting structure if any to comply with the approved local practice and laws.
The Chart of Accounts is available for selection just while running either the Initial Client Setup or the Initial Organization Setup.

-and the setup of the **taxes** which comply with the in-country tax authorities requirements.
The setup of the taxes is also available for selection while running either the Initial Client Setup or the Initial Organization Setup, and even in the "Enterprise Module Management" window.

!!! info
    The localization pack as well as any other modules or packs can be installed in the application path **General Setup / Application /Module Management** which is accessible while logging as **Etendo/Etendo** and changing the Role to "System Administrator".

This can be considered the first basic step while setting Etendo instances as it is required to install first the localization packs if any, in order to apply the accounting reference data or Chart of Accounts while creating either the "Client" or the "Organization" later on.

- The **Initial Client Setup**:

A **Client** in Etendo is the top-most level of configuration and data within Etendo.

Above means that certain configurations such as users, customers, vendors and other [master data](https://docs/en/end-user-documentation/etendo-environment/functional-documentation/business-management/masterdata-management) can be managed in a client and therefore be available across all the organizations within the client.

!!! info
    Each client can host at least one or even more than one organization that can be used to model your enterprise.

The Initial Client setup is the process which creates a Client in Etendo. A Client cannot be created manually.

This process besides creating a Client allows selecting the reference data included in the module/s or pack/s already installed.
All that data, if applied to the Client, will be shared by all the organizations which belong to the Client.

> There is a "System Client" which is automatically created by Etendo as part of the Etendo installation process.
!!! info
    This client handles application data such as tables, columns and fields and it also manages some data which can be shared across all the Clients such as currencies, countries and regions and units of measure.

- the **Initial Organization setup**:

An **Organization** is the second level of configuration and data.

Organizations can be structured in a hierarchical way within a Client providing multiple options while modeling your enterprise.

There are different types of Organizations which can either be independent legal entities or not.
Legal entities can either require accounting or not and Not Legal Entities can either allow transactional data or not.

The **Initial Organization setup** is the **process** which creates Organizations in Etendo.

!!! info
    An Organization can be created once the Client it belongs to has been created.

An Organization cannot be created manually.

Same way, this process besides creating an Organization allows selecting the reference data included in the module/s or pack/s already installed.

This time the data, if applied to the Organization, will be available just for the Organization being created.

!!! info
    There is an Organization named (\*) which is automatically created at the same time that the "System Client" is created. Every organization created later on will hierarchically be located below it.

- The **Users and Roles setup**:

Etendo security can be split into "Functional" and "Data" security.
"**Functional**" security manage the access rights to Etendo entities such as Windows and Processes by properly setting up [users](https://docs/en/end-user-documentation/etendo-environment/functional-documentation/business-configuration/general-setup#user) and [roles](https://docs/en/end-user-documentation/etendo-environment/functional-documentation/business-configuration/general-setup#role):

A **User** is an entity which can log into Etendo whenever it has a password and at least one role assigned.
Each person accessing Etendo should have a different user assigned properly configured.

A **Role** is the connection between users and access rights to Organizations, Windows, Processes and Forms in Etendo.
Access rights are first configured at role level, roles are then assigned to the user/s.

Etendo creates two users by default, the "System" user and the "Etendo" user:

- the "**System**" user is the owner of Etendo application data. It is not possible to log into Etendo as "System" user.
- the "**Etendo** " user is a "super" user which has access to any Etendo Client.

The password assigned to this user is "Etendo ", however it can be changed if needed in the [user](https://docs/en/end-user-documentation/etendo-environment/functional-documentation/business-configuration/general-setup#user) window.

This user is assigned to the "System Administrator Role", a role with no access restrictions.
**Data security** is an advance setting as it manages the access rights to subsets of data within Etendo entities such as Windows and Processes, by properly setting up the [Data Access Level](https://docs/en/end-user-documentation/etendo-environment/functional-documentation/business-configuration/general-setup#role-access) at table level and the [role](https://docs/en/end-user-documentation/etendo-environment/functional-documentation/business-configuration/general-setup#role):

!!! info
    Data Access level defines the client and/or the organization each record is going to be visible from.

Every [table](https://docs/en/end-user-documentation/etendo-environment/functional-documentation/business-configuration/general-setup#role-access) in Etendo has a "Data Access Level" column.

User Access Level allows limiting the records which will be accessible in entities such as [Windows, Processes, Forms, Widget Classes and Views](https://docs/en/end-user-documentation/etendo-environment/functional-documentation/business-configuration/general-setup#role) for a role, or even limit the access to a given entity.

### Basic Setup Diagram

The diagram below shows the Etendo "basic" General Setup flow for a legal entity with accounting. This flow is one part of the overall Business setup flow.

![](/docs/assets/drive/18h9kcOERmyWWpbyF7PsZJoOuFDHXtJ_q.png)

In the example above, the "**Accounting**" data can not be shared across all the organization/s of the client because it was not applied at client level but to the Organization being created.

This setup would fit in the case of a Client which has **one or more independent legal entities with accounting underneath**, same as the sample client shipped with Etendo by default (F&B sample client).

There is a close relationship between the **general setup** which allows the creation and configuration of an **enterprise**, and the **accounting configuration area** because to set a "**Legal with Accounting**" Organization as ready, it requires below accounting items to be properly created and configured first:

1. a [Fiscal Calendar](https://docs/en/financial-management-setup-accounting#fiscal-calendar)

2. and an organization's [General Ledger configuration](https://docs/en/financial-management-setup-accounting#general-ledger-configuration) which includes a dimension that is the [Account Tree](https://docs/en/financial-management-setup-accounting#account-tree) or "Chart of Accounts".

!!! info
    The Fiscal Calendar, once manually created, can be available to all the organizations within the client if it is created for the (\* (asterisk)) organization.

A defaulted **General Ledger configuration** and the **Chart of Accounts** can be automatically created if an "**Accounting**" reference data such as a "**Localization Pack**" containing a Chart of Accounts module is installed and applied to the Organization. Moreover, in case there is no Localization Pack for your country, Etendo delivers a Generic Chart of Accounts module which, if installed and applied, creates a sample Chart of Accounts and a defaulted General Ledger configuration which can be later on customized to meet the needs of your organization.

!!! info
    Back to the General Setup area, above Etendo basic setup is also briefly explained in the [Business Setup section](https://docs/en/end-user-documentation/etendo-environment/functional-documentation/business-configuration).

## Clear Report Cache

!!! info
    To be able to include this functionality, the Platform Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Platform Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=5AE4A287F2584210876230321FBEE614).

![](/docs/assets/drive/1QOK6qRnoFyXzZwsY4Cgwo22iBZ2CITgV.png)

In this window, the user, in general a developer, can delete the report cache data by clicking the “Done” button. This has technical purposes.  
After clicking it, a success message will be shown indicating the completion of the process.

!!! info
    For more information, visit [Platform Extensions Bundle | Technical Documentation](/docs/legacy/modules/platform-extensions-bundle)

## **Attachments Configuration**

#### **Introduction**

Client configuration of the Attachment Method to be used. Each attachment method can include its own extra fields to complete the configuration of the attachment method. It is only possible to have one active configuration on each client.

#### **Header**

Shows all configuration related to the attachment method used to save attachments. Each Attachment Method can include its own specific configuration fields like: server URL, user, password, language, etc.

## Application

### Create Sequences

In this window the `Create Sequences` the process is executed.

When selecting the organization and executing the process, Etendo creates the sequences for the type of fields "Transactional Sequence" or "Non transactional Sequence".

The main advantage of these new sequences is dynamic masking, which makes it possible to add dates or dynamic strings.

![](/docs/assets/drive/12h763OVeuLSs-GkZq5-zTPZMMV0UzuV9.png)

!!! warning
    The user can run this process only after a developer configures the sequence fields using transactional or non-transactional sequences.

!!! info
    For more information about this configuration, visit the technical documentation about [Sequences](/docs/legacy/technical-documentation/etendo-environment/platform/sequences).

After that, in `Financial Management>Accouting>Setup>Document Sequence` window the user can see and edit the sequences generated.

![sequenceslist.png](/docs/assets/legacy/technicaldocumentation/platform/sequenceslist.png)

| _List of sequences generated by the process_ |

### Conversion Rate Download Rule

!!! info
    To be able to include this functionality, the Financial Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558).

This module automatically generates conversion ranks with a background process using Apilayer. It allows keeping currency conversions up to date.

Conversion rate, also called currency exchange rate, is the rate at which one currency may be converted into another one within a given period of time. Currency is an accepted medium of monetary exchange that may vary across countries.

![](/docs/assets/drive/1zFe45U_EkZAD3OWHF2CY89LpaZ2NDcj1.png)

Fields to note:

- From Currency: Original currency
- To Currency : Target currency
- Tolerance: The maximum difference allowed between the new conversion rate and the previous one. This is used to insert or not the new downloaded rate.

### Currency

#### **Introduction**

Currencies and conversion rates are basic settings in Etendo.

Currencies used worldwide are automatically created and listed in the currency window once Etendo installation is completed.

!!! info
    All these currencies are linked to the system organization (\*), that means that those currencies will be shared by all the organizations in the system.

#### **Currency**

Currency window allows the user to visualize or to create and configure the currencies to use in monetary transactions.

![](/docs/assets/drive/Id_-XkKhJGKz4E4IgrcdchCEUtwHOz2EE8QQ_GiPaqSU470JxMUXCRZAIVHbLnAjQATCkVBbBy-1AbEPbzOR-EItV6nxocGv5sBtAkabdwigmNQiaO7qcrF0yUAdIxkmozBdAn-t.png)

As shown in the image above, currency relevant data is:

- the currency _ISO code_. Currency ISO codes are worldwide used codes for the representation of currencies and funds.
- the currency _symbol_ which can be placed at the right or at the left of an amount
- and the currency _precision_ or number of decimals to use while calculating amounts in that currency.

Etendo allows the user to setup three types of currency precision:

- the **standard precision,** defaulted to 2, is the one used overall but for prices and cost amounts calculations which can use a different precision.  
  This precision is the one used to calculate order and invoices amounts such as "Line Net Amount", "Total Net Amount" and "Total Gross Amount", therefore it should not be bigger than 2 unless the currency allows the user to pay smaller quantities than 0.01
- the **costing precision,** defaulted to 2, is the one used for product cost calculations. It is recommended to change it up to 4
- and the **price precision** is the one used for unit/list prices which can have more than 2 decimals precision because amounts are finally rounded to 2 by the standard precision.

!!! warning
    Changes on currency precision can only be made at client level, therefore System Admin Role needs to be used.

#### **Conversion Rates**

Conversion rates tab lists the available conversion rates for a given currency.

![](/docs/assets/drive/WLfdO4txHazfD7hrPCx81A_8FTa07TqNpNlv_ZIyEEBcbJt907KdDTIkZ71Y9Qa4d2opmcOfqNopEEYG-bvxrJT4V_y8ELvirA4MLN7JpMH8rdtBHgnAsHtMNZfkMJEM_c68jzIx.png)

A conversion rate is the valid rate at which one currency may be converted into another one within a given period of time.

This implies that a single currency might have several conversion rates depending on:

- the currency at which might be converted
- and the period of validity

!!! info
    Currency conversion rates can be also created in the Conversion Rates window, therefore it can be reviewed in this tab.

Etendo recommends conversion rates to be configured in the Conversion Rates window, as it is required to defined both the "Multiple Rate By" (USD - €) and the "Divide Rate By" (€ - USD) to properly defined the exchange of two currencies.

#### **Translation**

Currencies can be translated to any language if required.

![](/docs/assets/drive/h1lRXjQBmJVNgWlx_tv7RGfyF56NqhAfh872qimAXBSDYMLLQouPXNbHMF9dcByVgIoOc261XbWARBiXrTLsvtRQ8e8-rg-5wncWfV6QQxf6l1kRrHoe7u_xGC38Hq5GIdKojK94.png)

### **Conversion Rates**

#### **Introduction**

Conversion rate also called currency exchange rate is the rate at which one currency may be converted into another one.

!!! info
    Conversion rates can only be created at system organization level (\*), which implies they are available for all the organizations within the client.

#### **Conversion Rate**

Conversion rates window allows the user to create the rates to be used for multi currency transactions.

Etendo requires the user to enter and maintain currency exchange rate in both senses, that means to enter at the same time the two rates below:

- a _Multiple rate by_ which is the rate by which the base amount will be multiplied for to calculate the converted amount.
- and a _Divide rate by_ which is the rate by which the base amount will be divided by to calculate the converted amount.

For instance, USD exchange rate to EUR should have a _Multiple rate by_ = 0.68 setting and a _Divide rate by_ = 1.47 setting, as shown in the image below:

![](/docs/assets/drive/0jd4xH1XIAHAk9o1yEa-ApHM2BcsMBuMK8YX9QPMH6u-A_h5M7O3lOaNA8xrMycgog-vAV-WgQhfCHf9UjwM6ftv1zZT_Fld28RaOTuwRU0Xw8V0Ql_A7KNgO20zKgYlvzlWcXs7.png)

### **Country and Region**

#### **Introduction**

Countries and regions are basic settings to share within Etendo.

Countries and their corresponding regions are automatically created and listed in this window once Etendo installation is completed.

!!! info
    All these countries and regions are linked to the system organization (\*), that means that those countries and regions will be shared by all the organizations in the system.

#### **Country**

This window allows the user to visualize and/or to create and maintain the countries and the regions to be used in daily business activities.

![](/docs/assets/drive/7wlTKkSY89CblxbUfLmnLafkVTgPVlmk7_I-SS8d0mFe3lrRH3_5VN_PvJeClUPP1ZC9uhTTcLDdH3GhKAH2nuqpJgJgAEBwdJnVkTX1GtYu7OmXavxslpmGx84aoeNbNS2m8sCu.png)

As shown in the image above, country relevant data is:

- the _country ISO code_.
  - Country ISO codes are worldwide used codes for the representation of the countries.
- the _address print format_.
- whether it has any kind of _regions_ such as states or not. "Has regions" flag needs to be enable to enter regions in the Region tab.
- the _region name_
- the country _IBAN code_ of the country
  - IBAN or _International Bank Account Number_ is a system of numbering that was created to categorize the bank accounts worldwide.
- the country _IBAN code length_ of the country.
- the _Phone number format_
- the default _language_
- and the default _currency_

#### **Translation**

Countries and regions can be translated to any language.

![](/docs/assets/drive/J2nmC6HSXqsQMZ1gnwrSmgZ0GuXGZBR-l91sYP3vxBIZw_VxBHsjFzNhZg3aoxzWrIVgWjYl5oRXcb8pc9dh61OFDA4-B4XKaQEGctSmKA63gsKy0t7CqTHgF10Qq1XvPtWn4U1x.png)

#### **Region**

Regions tab allows the user to visualize and/or to create and maintain the regions of any type of country.

!!! info
    Country regions are simply defined by a name and a description.

### **Preference**

#### **Introduction**

A preference is a type of session value which can either be an attribute or a property.

!!! info
    Every time a user logs in Etendo, a new session is opened.

While logging in, the user enters several variables such as the _Role_, the _Client_ and the _Organization_ and, once in, the user navigates to a _Window_.

All those variables have a key influence on the session values the user will get.

In other words, _Preferences_ allow the user to define session values, session values which can either be a property or an attribute defined for a single client or for all of them, or for a single organization or for all of them.

!!! info
    Preferences can be assigned to the system or to a specific module, therefore, while exporting that module, the preferences it has assigned will also be exported, so those general settings can be reused.

For instance, there is an existing _Property_ named "_Implements an alternative Invoice Process button_". That existing property is currently assigned to the Module "Advanced Payables and Receivables Management" with a value = "Y" for any client, organization, user, role and window:

- Above preference means that if the Advanced Payables and Receivables Management module is installed, it will use an alternative invoice process button, besides every user logging in Etendo will get that feature working regardless of its role, user and the client or the organization it is working on.

For instance, there is an _Attribute_ named _"Autosave"_ which is currently assigned to the system with a value ="Y". This attribute is visible and therefore applicable to System client and to (\*) organization for any user, role and window.

- The preference above means that every user logging in Etendo will get that feature working regardless of its role and user and the client or the organization it is working on.

#### **Preference**

Preference window allows the user to define and maintain session values which can be visible and therefore applied to different levels such as Client, Organization, User, Role and Window.

##### **Preference Definition**

![](/docs/assets/drive/ORFZT6LvzmxT-rOY-l1Xw07GvftHNxLMJU6RxtHo8LmMioTFNJMYUcITNJlA5xrvFyW8PMzRi2grIoMM-tFBiotCV4s3YNbUzC5G7UyavRacVSjEpYLuQQtdo9v_aTHWIgVHoM1w.png)

As shown in the image above there is one field named "_Property List_" which is key in defining a preference as a property or as an attribute:

- if the _Property List_ checkbox is _checked_, the preference is configured as a **property** to be taken from an existing list of properties.  
  There are many types of properties already created, besides _modules can add new properties to that list_ with the aim of getting those other modules or even the system can use them by setting the corresponding properties values.  
  Some of the available properties are listed and briefly explained below:
  - **Enable UOM Management**  
    If set to Value = "Y" at "System" level, it allows the user to define alternative UOM for a product, besides product's UOM.  
    Same way, a new field named "_Operative Quantity_" will then be shown in purchase, inventory and sales transaction documents, therefore "Ordered Quantity", "Movement Quantity" and "Invoiced Quantity" always shows "Operative Quantity" entered by the end-user, converted to the product's UOM.  
    **Enable automatic Price Difference Corrections**  
    If set to Value = "Y", it allows the creation of Price Difference correction cost adjustments.
  - **Enable Negative Stock Corrections**  
    If set to Value = "Y", it allows the creation of Negative Stock correction cost adjustments.
  - **Enable Cancel and Replace**  
    If set to Value = "Y", it allows to Cancel and Replace booked sales orders.
  - **Cancel and Replace - Associate shipment lines to new order**  
    This preference requires "Enable Cancel and Replace" preference enabled, and it only works if "Create netting shipment on Cancel and Replace" preference is not enabled  
    If set to Value = "Y", it assigns the shipment(s) related to the cancelled sales order lines to the replaced sales order lines.
  - **Cancel and Replace - Create netting goods shipment**  
    This preference requires "Enable Cancel and Replace" preference enabled, and it only works if "Cancel and Replace - Associate shipment lines to new order" preference is not enabled  
    If set to Value = "Y", it automatically creates and completes a "netting" goods shipment related to the cancelled, voided and replaced sales orders.
  - **CSV Text Encoding**  
    If set to Value = "Y" allows to specify the encoding to be used in the Export to CSV process
  - **Grid configuration**  
    If set to Value = "Y" every time a user changes a grid view, those changes are saved in this window linked to this property.
  - **Implements customer Credit Used calculation**  
    This property is currently assigned to the Advanced Payables and Receivables management module with a property value ="Y". This property avoids the C_BP_SOCREDITUSED_REFRESH function calculation.
  - **Implements an alternative Invoice Process button**  
    This property is also assigned to the Advanced Payables and Receivables management module with a property value ="Y". This property avoids the usage of core invoice process button.
  - **Implements an alternative Financial Management**  
    Same applies to this which allows an alternative financial management for that module.
  - **Implements Payment Monitor management**  
    Same applies to this, which disables core's background process and button on the invoice header that manage the payment monitor.
  - **Recent views shown in the workspace** property set to "Y"  
    This allows that the recent views are shown in the user workspace
  - **Show MRP and Production fields** property set to "Y"  
    This allows that the MRP and production fields are shown
  - **Not allow changing exchange rate and amount**  
    If you set this property with value = "Y", exchange rate and amount are read-only in Add Payment from Sales Invoice, Purchase Invoice, Payment In, Payment Out, Financial Account, in Select Expected Payments from Payment Proposal and in Funds Transfer from Financial Account.
  - **Write-off limit**  
    This property with a property value ="Y" allows configuring write-off limit in Add Payment from Sales Invoice, Purchase Invoice, Payment In, Payment Out, Financial Account and in Select Expected Payments from Payment Proposal. The write-off limit is set for each Financial Account in Financial Account window.
  - **Show Product Characteristics Parents**  
    Values can be 1,2,3,4, etc. The number means how many levels in the hierarchy tree the user wants to show in form view in the Product window. For example, if the tree is: Colour->Green->Green light->0034
  - **Allow Multiple Tabs of Window**  
    If set to Value = _'Y'_ allows opening more than one tab of a single window.
  - **Attach By Default**
    - If set to Value = 'Y' the "Print Document" popup will not be shown, this popup is the one which asks if the user want to attach the document or instead of it just print it without attaching. When the value of the preference is set to 'Y' the document will be automatically attached.
    - If set to Value = 'N' the "Print Document" popup will not be shown, this popup is the one which asks if the user wants to attach the document or instead of it just print it without attaching. When the value of the preference is set to 'N' the document won't be attached.
    - If Value is Undefined the "Print Document" popup will be shown with two options: "Yes" and "No, just print it". If "Yes" is selected, the document will be attached. If "No, just print it" is selected, the document won't be attached.
  - **Direct Print**
    - If set to Value = 'Y' the Direct Print mode is enabled.
    - If set to Value = 'N' or Undefined, the standard print mode is used.
  - **Allow Where Parameter**
    - If set to Value = 'Y', it allows getting the "\_where" parameter from manual datasources. A warning will be shown if the "\_where" parameter is sent.
    - If set to Value = 'N' or Undefined, it will not allow getting the "\_where" parameter from manual datasources. An exception will be thrown if the "\_where" parameter is sent.
  - **Allow Unsecured Datasource Request**
    - If set to Value = 'Y', it allows doing unsecured datasource request. A warning will be shown if the current role does not have access.
    - If set to Value = 'N' or Undefined, it will not allow doing unsecured datasource request. It is required to have a role with enough access permissions. An OBSecurityException is thrown if current role does not have access.
  - **External Rebuild**, when this preference is defined as system level with its value set to _Y_, it will not be possible to rebuild the system from Module Manager Console after installing/updating modules. It forces rebuilding the system from command line.
  - **Bypass Access Level Entity Check**, when this preference is defined with its value set to _Y_, it will allow bypassing the check that compares role's user level with entity's access level to completely prevent accessing latter one.
  - **Translate Yes/No Reference in Export To CSV**, when this preference is defined with its value set to _Y_, the value of the columns whose reference is _Yes/No_ will be translated to the current context language when exporting the grid of a standard window into CSV.
  - **Disable Linked Items Section**, when this preference is defined for a window with its value set to _Y_, the Linked Items section will be disabled for that window. If there is not any window defined in the visibility settings, this section will be disabled for every window in the application.
  - **Enable Screen Reader**, If this preference is set to _Y_ the full screen reader will be enabled. This will improve the accessibility to visual impaired people.
  - **Excel Export Format**, this preference allows setting the export format to be used when generating Excel reports. Two values are supported: _XLS_ or _XLSX_. When this preference is not defined, _XLSX_ is the default Excel export format.
  - **"Filter by documents processed since N days ago"** is related to Create Lines From in Sales/Purchase Invoice. It limits transactions starting from the current date to the defined days ago. If the preference is not defined then queries retrieve all records created since one year ago (365 days), else it will be filtered by the count of days defined as the preference value.

![](/docs/assets/drive/U-6eYqg2DbvQutUsYua4ZGYyN6m1Eg0Kf0kmS2ONtUO0l12g9IUSmE9NWCAHuLBjiy9IQt_dS1PG71TEorFR55Jg3z2S_UUBUq8NwYaCp-BUa1b5d6q9ZIquttmiYsoQzFKV4rR6.png)

- if the _Property List_ checkbox is _not checked_, the preference is configured as an **attribute**. An attribute is a free text attribute which can get whatever value.

![](/docs/assets/drive/t1vw7KGogAD0Tqp1UIoVESm6KBOrDcv9f2BuzzDGdaNP9yXkId4n_YODwWpbnzvGiSKEktpKJqAUtwwlUpKH3DR1Z6t51QShE5mUAWtuaksNDKhgeu-_YxYsnlwXySWaLwsyOfaU.png)

- **"ShowAuditDefault"** attribute allows enabling the Audit Trail feature. Audit Trail feature allows tracking every change done to any Etendo table or entity.
- **"ShowAcct"** attribute allows showing Post buttons and Accounting tab whenever its value is set to "Y".
- **"ForcedLinkWindowDBTableName"** where "DBTableName" is the name of the table in database.  
  This attribute allows a direct navigation to the window which UUID is set as attribute value, instead of using the standard navigation logic.
- **"ModalModuleModuleJavaPackage"** where "ModuleJavaPackage" is the name of the module's Java Package name or _"ModalModuleModuleUUID"_ where Module UUID is the unique identifier of the module in the data base.  
  This attribute defines whether the processes within a module invoked from a menu or a button or a tab are opened in browser popups (attribute value = "N") or in modal popups (attribute value ="Y").
  - _Browser popups_ implies the deployment of the process in a new window in the browser
  - _Modal popups_ implies the deployment of the process in another layer inside the application window.
- **"ModalProcessProcessUUID"** where Process UUID is the UUID of the process.  
  This attribute defines whether a given process is opened in modal popup (attribute value ="Y") or in browser popup (attribute value ="N").
  - This attribute has a higher preference than ModalModule, therefore it is possible to define all processes in a module to open in modal popups but some of them.
- **"SaveAttachmentsOldWay"**  
  This attribute defines whether attachments should be saved using the old attachment model.

##### **Preferences Visibility**

Preference visibility section defines the _levels_ where a preference is going to be used and therefore applied.

Preference levels can be set to a given value or left empty. If a level is left empty, the preference will be valid for any value of that level.

For instance, if user level is empty, any user will be able to see that preference. In case the same preference has values at different levels, the most specific one will then be used.

Available levels are:

- _Client_ - if this level is set to empty or to System, the preference will be visible from any client used to log in.
- _Organization_ - if this level is set to empty or to (\*), the preference will be visible from any organization used to log in.
- _User_ - if this level is set to a given user, only that user will be able to see that preference once logged in.
- _Role_ - if this level is set to a given role, only that role will be able to see that preference.
- _Window_ - if this level is set to a given window, only that window will be able to see that preference.

##### **Preference Priority**

Preference Priority section defines _priority_ of multiple preferences defined for same Property

Preference Priority will be applied while loading the default Preferences of the Logged in Role.

- Check Priority by Client **(Visible at client)** :
  - Undefined client visibility is handled as SYSTEM.
  - If pref1 or pref2 either of them which does not set to SYSTEM CLIENT will be considered.
  - If pref1 or pref2 both have value set and both not set to SYSTEM CLIENT, then it will check Next Priority Level.
- Check Priority by Organization **(Visible at Organization)** :
  - If pref1 or pref2 either of them which has value set will be considered.
  - If pref1 or pref2 both have values set then, It will check the depth of the value in Organization Tree and Highest Organization's Preferences will be Considered.
  - If pref1 or pref2 both have the same value set then it will check Next Priority Level.
- Check Priority by user **(Visible at User)** :
  - If pref1 or pref2 either of them which has value set will be considered.
  - If pref1 or pref2 both have value set then it will check Next Priority Level.
- Check Priority by Role **(Visible at Role)** :
  - If pref1 or pref2 either of them which has value set will be considered.
  - If pref1 or pref2 both have a value set then it will check Next Priority Level.
- Check Priority by Window **(Visible at Window)** :
  - If pref1 or pref2 either of them which has value set will be considered.
  - If pref1 or pref2 both have a value set then it will check Next Priority Level.
- **SAME PRIORITY**:
  - If all the above levels are the same then it will and will consider preference with column **"selected"=true**.

##### **Preferences Values**

When logging in Etendo or entering the role or the organization, the preferences visible for that user, role, client, organization or window are stored in the Etendo session. Those session values can be obtained by using the method: _org.openbravo.erpCommon.utility.Utility.getContext method._

Additionally:

- It is possible to look for the value of a given preference by using the method: _org.openbravo.erpCommon.businessUtility.Preferences.getPreferenceValue_.  
  This method shows an exception in case:
  - a preference property does not have a value defined for the required visibility level
  - or there is a conflict caused by the definition of more than one property values for the same preference property for a given visibility level

Conflicts can be manually resolved by checking and modifying the preference.

### **Session Preferences**

Session preferences allow showing or hiding accounting tabs or translation tabs for a given user, role, client and organization.

![](/docs/assets/drive/VAr7jhdNC8mm1JlSp-Jq-dBswsbSAMKpcuq_Tg6_Z3yKcxRbc3N8IgLn-gimlxHoPzGvtOl0i3k7wPCdqKKG8zO1xgcS5xvh-sC1T0yO2qeanxvBMqt-P8TUPDo9n-ASz4p2LjaL.png)

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

### Number to Word Converter

!!! info
    To be able to include this functionality, the Platform Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Platform Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=5AE4A287F2584210876230321FBEE614).

This module provides the infrastructure to convert a number into its equivalent in words. This functionality is especially useful while printing checks.

Once installed, this module creates a new window which can be found in the application path: **General Setup // Application**

Some fields to note are:

**Organization** that is the legal entity which requires printing checks in a given language.  
**Language** that is the language's words into which the amounts to pay needs to be converted.  
**Javaclass** that is the route where the Javaclass that converts amounts into a given language is located.

The "javaclass" field is required but empty by default unless another module such as the Number to Word (Spanish) or the Number to Word (English) is installed and properly applied to the legal entity for which it is required to print checks. Additionally, the Javaclass can be filled in manually.

![](/docs/assets/drive/1YjGbvShn-Mwb6iNpbajKgNo77ukscR3n.png)

### **Window Personalization**

#### **Introduction**

Etendo allows the customization of grid and form views. Customize windows and form views are stored once saved in the Window Personalization window. Etendo windows can be shown in _Form View_ and in _Grid View_, both ways can be customized as required.

#### **Window Personalization**

Window Personalization lists and maintains the customized form views.

![](/docs/assets/drive/xS4tDlk0VJ49snDskpuJfugXl-ziE6vT8HMe7op-QkP_NzRwF-Rr7rgisAd3RnIXQLgaJ0h6hK07xGi2hbhGd37GcHr8q8zyW0zzZ4bOYdxQzByOqDjw202Qn0WoHMxu7WoIXCHU.png)

Once a form has been customized, saved and listed in the _"Window Personalization"_ window, it is possible to configure the levels of visibility where that form personalization will apply.

### **Alert**

#### **Introduction**

Alerts are notifications which inform about events happening whenever an alert rule has been properly defined to monitor those events.

The way "_Alerts_" work in Etendo is described below:

- Alert rules need to be previously defined as SQL queries. SQL queries define the event that is going to be monitored.  
  For instance, _"Products without a defined price"_, _"Products under stock"_ or _"Bank account without accounting information"_
- An alert rule can be applied to every Etendo user or just to a set of them. Alert recipients are the Etendo users for which a given event is going to be monitored.
- An Etendo background process is permanently checking if the SQL query defined in each of the active rule alerts return any record.
  - If that is the case, Etendo creates and returns a new _alert instance,_ which is saved in the _"Alert Management"_ window in _"New"_ status.

The _number of alerts instances_ informing about events being monitored happening is shown in the "Top Navigation" menu:

![](/docs/assets/drive/z341Sqx0_VIs2wSRDSm-6Jlq_2MmxWxxFa406LPjtgffjFTdFIds94ov5CwjlKGP7vDSEyxAdiYnVGN3m0AaIZjGIz2WkrZSmPlCagaI-KmACHhix0-qaazsTFjJ3D9sG0sTkbHv.png)

Alerts instances can be visualized and managed in the _Alert Management_ window which is opened by clicking the "Alert" option of the Top Navigation menu.

![](/docs/assets/drive/-wFUIZt2K33Chbp-czLqJmO7f1hP5fcD2jkcZaI7CtnhlHHbdh7lk1_ayiFKbrcfx8slOlIXVjeiIe15gmt_CkcTwhWQGhAbfXXGCMaF6-ba5l_OGBnMsKpP8CkL23o7AwzywwMX.png)

Alerts can have 4 different status:

- _New_ - new alerts instances which reflect the events monitored happening.
- _Pending_ - acknowledge alert instances for which an end-user action is pending to be done to get them solved or fixed.
- _Ignore_ - not applicable alert instances which must be ignored.
- _Solved_ - alert instances solved as the event happening is fixed or solved.

The way to manage alerts instances is by manually selecting and moving them to the next or previous status once they are manually acknowledged, ignored or solved.

#### **Alert Rule**

Alert window allows the definition of alert rules as SQL queries which define the event to be monitored and how it will be monitored.

Alerts are defined by entering below data:

- The _"Name"_ of the alert which is the event to be monitored.
- The _"SQL"_ query.
- and the _"Tab"_ where the alert instance can be fixed or solved.

![](/docs/assets/drive/7FDlwrebuc8IysmRIryYm81mF7QPheC-khbM3NdpZUdAIlXzkhZMDvasxwUPYPDMEyJcP_oM5t16sfAW3ZOCyVNUmR8nE4WWZkLYexMWFuKDHaCb0j8Axa1AetNm9j5rEVq36Kri.png)

#### **Translation**

Alerts can be translated to any language required.

#### **Alert Recipient**

Alerts can be allocated to specific users or contact or to all of them.

!!! warning
    If no _Role_ or _User_ is configured in the _Alert Recipient tab_ of a given alert, that alert will apply to any Etendo user or role.

Etendo supports alerts notification to user or roles by email:

- for this, it is required to properly configure _e-mail_ server, account and password for the corresponding client in the header of the Client window, section "Request Management".

#### **Alert**

Alert tab list the events happening which generate the corresponding alert.

![](/docs/assets/drive/qRqaP9bx7a04XzXIrzdpZZ3eS3OaglF9SMM3xvRYaL3Vrkhcxz_EI5BxPbtrnQoW_DXad8d-_oQBJntpSgZdchM9RtWisxif2I3GWPM2Yda4XlbPG_kkWIqlvgDl5cvOObV43F4W.png)

## **Client**

Client folder collects client basic configuration as well as the role of the client to assign to those users not linked to a Google account.

#### **Introduction**

A client is an independent entity composed of at least an organization. A client can include and manage master data such as users, customers and vendors. That master data is then shared among all the organizations which belong to that client.

Etendo allows the user to create more than one Client and more than one Organization within each Client to model your enterprise according to your needs.

Normally, it is enough creating just one Client which hosts multiple organizations that can be used to model your enterprise, the main reasons for this are:

- a client can manage master data that is therefore available to all organizations within that client
- besides, each organization can also manage its own master data and have its own transactional data
- finally, a Client cannot share any master data with another Client.

Clients are created by running the Initial Client setup process available for the "System Administrator" role.

Organizations are created by running the Initial Organization setup process available for the "Client Administrator" role.

#### **Client**

The Client window allows the user to view and maintain the clients created by running the Initial Client Setup process.

![](/docs/assets/drive/wMk7KssPzOXZVKhjV7qnWPlXL7Jxp4k-0URRQOskHEzl8S2Bm-YYnS9alftc1syx4nGMulhABjv_qKTWCD8QksvoikpfUN0DQCMBGXnTR-SKMjk2Ic7tMe5M7CZaE-yz5FCMtuXB.png)

!!! info
    The field "Days To Password expiration" allows the user to set a day limit during which a password may be valid for users. The limit will be reset every time a user changes his password.

The value of the field determines the day limit during which a password must be valid for users:

- If it is set to 0, no day limit will be applied.
- If the value is greater than 0, the day limit will apply after the last date of user update password date.

Setting the value will apply the configuration to all Users from that Client.

A relevant field to note is the **"Central Maintenance"** checkbox under the section "Accounting Dimensions".

This checkbox, if selected, allows the user to configure that the Client centrally maintains key accounting dimensions such as "Organization", "Business Partner" or "Cost Center", therefore the configuration set in here is shared by all the organizations of the client.

New Clients created by running the Initial Client Setup process are created as "Centrally Maintained" by default with the mandatory accounting dimensions (Organization, Business Partner, Product) selected.

The organizations of the Client which require to have additional dimensions not listed in here, for instance "Campaign" or "Sales Region", will have to configure them in the Dimension tab of the organization's general ledger configuration.

Existing clients are not set as "Central Maintained" by default because the accounting dimensions which were set are the ones which were configured in the Dimension tab of the corresponding organization's general ledger configuration.

It is now possible to change existing Clients as "Centrally Maintained", this action overrides what is configured for the organization in relation to the accounting dimensions that can be centrally maintained in the Client, those dimensions are:

- Mandatory dimensions:
  - Organization
  - Business Partner
  - and Product

Mandatory dimensions can be filled in or not depending on the document category being created. For instance, "Organization" needs to be always specified in the document's header regardless of the document being created, however "Business Partner" and "Product" are mandatory dimensions that need to be filled in a purchase invoice but can be filled in a G/L Journal if needed.

- Non Mandatory dimensions:
  - Project
  - Cost Center
  - 1st Dimension, this is a free text dimension which can be customized as required (i.e. it could be customized as "Department"), same as the next one
  - and 2nd Dimension

Non mandatory dimensions can be filled in or not depending on what is needed and regardless of the document category being created.

Above dimensions are then shown either in the header or/and in the lines of the documents to be posted to the ledger within a section named "Dimensions".

Besides, there is a financial report named Accounting Transaction Details which shows every ledger entry of an organization's general ledger detailing every dimension value entered.

Finally:

!!! info
    It is important to remark that the settings displayed in the client window in both the "Accounting Dimensions" section and in the Dimensions tab is the defaulted configuration provided by Etendo.

This defaulted configuration is populated from the Dimension Mapping window.

It is always possible to customize the defaulted configuration, for instance:

- if a client needs to show and therefore make available the organization dimension in the lines of the documents, below actions need to happen:
  - check the checkbox "Show in Lines" for the Organization dimension
  - and delete or modify the records linked to the "Organization" accounting dimension in the Dimension tab as all those records are defaulted not to show Organization in any document category lines.

#### **Information**

Information tab allows the user to add, edit and maintain client generic information such as default units of measure and images.

![](/docs/assets/drive/xj_ATfvJhEVYxSBgsLALNk4ZzrjF9oF5bONVGhnh_MFd676cYAJ-y_SPwBYm8QRYOZeFR7Vl1JakOWLL7-6FmeWEASYdUDRk_e672LxTfNp7z-hc9dred0Imhz4zKW8kuv-FA_1Q.png)

Additional information allowed to be specified:

- _Discount calculated from Line Amounts_ excluding taxes and charges
- Default _units of measure_ for:
  - _volume_
  - _weight_
  - _length_
  - and _time_
- _Price List_
- _Product for freight_
- _Check shipment Organization_ to monitor that the organization shipping the goods is the same as the organization of the customer.
- _Check Order Organization_ to monitor that the organization ordering the goods is the same as the organization of the vendor.
- _Group Invoice lines in accounting_ to get invoices having many invoice lines, do not generate as many accounting lines as invoice lines but a summarized number of accounting lines per account.
- Company _Logos_ for:
  - the _Company Image_
  - the _Company Menu_
  - and _Company Documents_
- _Allow Negative stock_ to do this, Etendo does not check stock if that is not required.

#### **Email Configuration**

Documents such as orders or invoices can be sent out by email. Email configuration tab allows the user to configure the email server, account and password, variables which require to be properly set up prior to sending documents by email.

![](/docs/assets/drive/39VWRTt1ZP4Xnxtq9P8nnTWYiFGuxRrPtT_D6sOzAaefl61XCFVGf8My_6SP0a1sODWMVaXB2Lrz3am4UOlKoblc1V8ubFZlQwD679lQjDUYzK-ET3pdoLDP2pekKPTNzZw55-Ma.png)

"Email Configuration" tab gathers the email configuration required for sending out documents such as orders or invoices.

!!! info
    It is important to know the smtp server configuration which is going to be used in order to properly fill the information below:

- **Smtp Server**, email server with SMTP
- **SMTP Authentication**, "yes/no" flag to define if the email server requires authentication or not before sending emails.
- **SMTP Server Account**, email server username in case of authentication required.
- **SMTP Server Password**, email server password in case of authentication required.
- **SMTP Server Sender Address**, email address to send emails from.
- **SMTP Connection Security**, security level needed for the SMTP servers connection. Available options are:
  - None
  - STARTTLS
  - SSL
- **SMTP Port**, port required for your SMTP server
- **SMTP Connection Timeout**, maximum amount of time (in seconds) allowed for an SMTP connection to connect or communicate.

In the provided screenshot, you can see a valid configuration for a gmail account:

- **Smtp Server**, [smtp.gmail.com](http://smtp.gmail.com)
- **SMTP Authentication**, "yes"
- **SMTP Server Account**, a valid gmail account (including the @gmail.com or @yourdomain)
- **SMTP Server Password**, the password for this gmail account
- **SMTP Server Sender Address**, email address to send emails from.
- **SMTP Connection Security**, SSL
- **SMTP Port**, 465
- **SMTP Connection Timeout**, 600 (10 minutes)

#### **Dimensions**

Dimensions tab allows the user to configure whether a given accounting dimension is going to be available in the header and/or in the lines of a given document category or not.

This tab can be used to configure accounting dimensions availability at document level only if the client is set as "Centrally Maintained". This setting is specific to the document and accounting dimension and it overwrites the configuration in the header.

For example, if a client needs to display project dimension in the header and lines in all documents less in amortization document, the client window should have the following configuration:

![](/docs/assets/drive/Z99sk_o2Vu9v8vGHzhGXw0tmp5rkwyxGAKUAdt-1-ve8kenhAGjDhIvu3Ixf8rRRk4pc5hoN8msS1KUk5WTs0z0JUd4D8LxV1ItpgEEXu2OActIg73-ikeOb9k7mKGTi1btTJety.png)

The configuration in dimensions tab is populated by the configuration that exists in the Dimension Mapping window.

## **CRM Connector**

### **CRM Connector Configuration**

The concrete CRM connector must add a configuration in this window to enable it to connect to the external system and to define the properties and filters used by Etendo to map with the external system information.

#### **API Property**

An API property is like a Map which matches an external API key with an Etendo Message. It defines the data type and any other related configuration.

#### **Property Options**

It allows the user to define options accepted by parent property.

#### **Filter**

Filters for external business partner integration. The filter has a defined type and it is linked to one or many properties.

#### **Filter Options**

It allows the user to define options accepted by the parent filter.

#### **Address Mapping**

In this tab, the user can define addresses and determine the properties that should be used for each location column mapping.

## **Enterprise Model**

Enterprise Model folder allows the user to create and model the Organizations which belong to a Client.

#### **Introduction**

Datasets allow the user to define reference data such as master data or configuration data for modules or even for Etendo core.

Reference data can be imported or applied to organizations in the "Enterprise Module Management" window by just selecting the organization for which the reference data needs to be applied and the reference data to apply or to import.

![](/docs/assets/drive/GCwDdNOwwnsS4qqc5AOasqxELrfP6UKdw6AY3ffwJuGxF0qL36O0MLh6_BZI9TPXNT8ywlVdzqL7nn4gf-opz7Zxo-tX5Ap1o99nZMhU3fLcn3mofw12qESDtmyyLrJJcRh2zdX7.png)

- If a reference data is applied at (\*) organization, every organization in the system will have access to that data.
- If a reference data is applied at a parent organization, all the organizations which belong to it will have access to that data.
- If a reference data is only applied to an organization which does not have any organization underneath in the tree, only that organization will have access to that data.

### **Initial Organization Setup**

#### **Introduction**

An Organization is an enterprise of a Client. A client can have at least one or even more than one organization as the way of configuring different types of enterprise models.

Overall organizations can be:

- independent legal entities with a different Tax ID number
- enterprise groups with the aim of getting aggregated figures for the group
- or business areas of the client such as departments

Besides, organizations can be structured:

- by _country or region_
- by _area or function_
- and so on, according to the enterprise model needs.

All of the above provides an insight about the different scenarios which need to be covered while modeling the enterprise.

There could be organizations which require to share master data such as business partners and products while having its own chart of account, taxes, financial reporting and transactional data. That could be the case of independent legal entities belonging to the same enterprise group.

There could be organizations sharing master data and even the same chart of accounts. That could be the case of divisions or departments within the same independent legal entity.

There could be organizations created with the aim of just grouping data, for which its own transactional data is not required.

All of the above is possible due to the fact that there are different types of Organizations, see the section below, and besides organizations can be structured in a hierarchical way:

- At the highest level of the tree, there is an organization named (\*).
  - (\*) organization is created at the same time that the _system client_ is created, and it is shared among the different _client/s_ in the system.
  - Master data created at (\*) organization level is accessible for all the organization beneath it
  - (\*) organization is not an independent legal entity, therefore transactional data is not allowed.
  - Every organization created later on will be created below (\*) organization.
- At a lower level of the tree, there can be parent organization/s which can have child organization/s beneath it/them.
  - Master data such as business partners and products created at parent organization level is accessible for all the child organization/s beneath it.
- At the lowest level of the tree, there can be child organization/s with no organizations beneath it/them.
  - Master data such as business partners and products created at child organization level will not be accessible for the rest of the child organizations, if any.

#### **Initial Organization Setup**

As already mentioned, Organizations are created by running the Initial Organization Setup process and not only that, once an organization has been created it must be set as "Ready" in the Organization window.

![](/docs/assets/drive/jaLNPOFQoCLMgujXvhC3sL--3PKbCLcfdvQubK5VvyRy85PwL7t_4V38fCTBCmrioEfhBQKvWWVq87sbLZsuP9D-YMUodiBeLsQrhbY-cnruPAjkkigHou5kknI1D0ZYc4-G0RiB.png)

As shown in the image above, an organization can be created by providing the relevant data below:

- the name of the organization
- the name of the user of the organization
  - Etendo creates a new user and a new role which only has access to the newly created organization.
    - This user can be later on changed by assigning new roles to it.
    - And the role can also be later on changed by assigning new organizations to it.
- the organization type. The options available are:
  - Organization - an organization which is not a legal entity and does not allow transactional data entering.
    - This type of organization allows the creation and configuration of master data to be shared among a group of organizations of any type belonging to it, for instance Business Partners, Chart of Accounts, etc.
    - It does not require general ledger as it does not allow entering transactions, but it can have a given General Ledger configuration to be shared among the organizations underneath
    - The accounting periods can not be opened and closed independently at its level.
    - And there could be as many organizations type "organization" in a branch as required.
  - Legal with accounting - an independent legal entity with a unique Tax ID number which requires accounting, therefore:
    - This organization requires a General Ledger and therefore an Account Tree or Chart of Accounts, as well as a Fiscal Calendar because the accounting periods can and must be opened and closed at its level.
    - This organization type allows the "consolidation" of the Balance Sheet and P&L reports only for the Chart of Accounts it has assigned.
    - Transactions are allowed for this organization type.
    - And finally, there can only be one legal entity per tree branch, therefore the organizations underneath inherit the General Ledger configuration and the Fiscal Calendar of the legal with accounting organization.
  - Legal without accounting - an independent legal entity with a unique Tax ID number which does not require accounting because it is managed in a separated system, therefore:
    - This organization type does not need a general ledger nor a chart of accounts and will not support financial reports at its level.
    - Transactions are allowed for this organization type. Transactions which will not be posted to the ledger.
    - It can not have another legal entity in an upper/lower level of the enterprise tree structure.
  - Generic - an organization which is not a legal entity but must belong to a legal entity placed at an upper level in the organization tree structure. For instance, departments or divisions within an organization or legal entity.
    - There could be as many generic organizations as required per tree branch, but always under a legal entity.
    - This organization type allows transactional data entry, it can have its own general ledger configuration and can inherit the general ledger configuration of the legal entity with accounting they belong to.
    - The accounting periods can not be opened and closed independently at its level.
- the parent organization. While creating an organization, it is possible to select the organization to which the organization being created will belong to. The parent organization would need to be set as "Summary".
  - A generic organization can not be the parent organization of a legal entity organization, but the other way around.
- the organization location/address
- and the organization currency

Besides:

- There is a checkbox named "Include Accounting" which allows the user to select for an organization:
  - an accounting CSV file in the field "Accounting File"
  - or a Chart of Accounts module reference data in the section "Reference Data". Reference data coming from extensions modules is master data such as Taxes, Chart of Accounts, etc to be applied from the already installed modules.

This action creates:

- a General Ledger configuration which is automatically linked to the Organization being created
- and an Account Tree or Chart of Accounts which is also linked to the Organization being created

This step does not create a Fiscal Calendar as the Initial Client Setup process does, because Fiscal Calendars need to be created ad hoc for the "Legal with Accounting" Organizations for which "Allow Period Control" feature is going to be enabled.

!!! info
    Note that this step does not imply to manage accounting within an organization, but just to include an accounting file or an accounting reference data in an organization.

Accounting management relies on the organization type being created.

It is not mandatory to select "Include Accounting" checkbox while creating a legal entity with accounting organization for instance because:

- a legal entity with accounting can inherit the client chart of accounts
- or, later, both the Chart of Accounts and the General Ledger configuration can be created manually and be linked to the organization.
- if the checkbox "Include Accounting" is selected, it is possible to select for the organization being created below dimensions to be used while posting the organization's documents to the ledger:
  - Mandatory accounting dimensions such as "Business Partner" and "Product" and not mandatory accounting dimensions such as "Project" and "Sales Region" while creating an Organization in a "Client" which does not centrally maintain the accounting dimensions.  
    In that case, the dimensions selected in here will all be listed in the dimensions tab of the organization's general ledger configuration, therefore will be available just for that organization.
  - Additional accounting dimensions such as "Project" or "Campaign" while creating an Organization in a "Client" which centrally maintains the accounting dimensions.  
    Once more, the dimensions selected in here will be listed in the dimensions tab of the organization's general ledger configuration, therefore will be available just for that organization.

It is possible to apply reference data such as:

- Document types and default algorithm for bank statements auto-matching, this one is similar to the previous one but for specific financial flows such as Payment Outs, Payment In and Financial Accounts.
- or reference data such as master data or configuration data (i.e. tax setup) created for Etendo extension modules.

Finally, it is important to remark that:

- Each organization, of any type, can have its own general ledger configuration/s and currency/ies (apart from the one inherited from its parent) if it is configured to be that way for the Organization
- A calendar is mandatory just for the legal entities with accounting. This organization type is the only one which can have a calendar assigned, the rest can inherit it.
- Financial reports are run by general ledger configuration and therefore by currency, as each general ledger configuration has only one currency allowed.
- Financial Reports such as the Balance Sheet and the P&L as well as Tax Reports can only be created at the level of Legal Entity with accounting.
  - Rest of reports such as sales, procurement and warehouse reports can be launched for any organization type.
- A general ledger configuration should not be assigned to the (\*) organization because that one will then be shared by all the organizations underneath.

#### **Examples**

**1.** Etendo Demo Data:

Etendo includes demo data for demonstration purposes, which includes an "Enterprise Model" composed by a set of organizations.

![](/docs/assets/drive/Vuf4G00AIK2uWFXjxHE733lf2QkM1WNhX1Eh29LCef9KNoZMGGnkD0O1vnkML26wZ7V_PHQHSgKtBgTxaB5Y3od9pFqzriF1nCYm7ysoMCJKrPf9-6jKp017i2QCIHKCBbV82bZn.png)

- An organization type "Organization" named F&B International Group.
  - This organization is not a legal entity and it does not allow transactions
  - This organization allows the creation and configuration of master data to be shared among a group of organizations beneath it.
- Two "legal entities with accounting" named "F&B España" and "F&B US" that belong to F&B International Group.
- Below the legal entities with accounting organizations there are four "Generic" organizations, which are not legal entities but belong to a legal entity and besides allow transactional data entry:
  - F&B US West Coast
  - F&B US East Coast
  - F&B España - Region Norte
  - F&B España - Region Sur

**2.** How to create each Organization type:

The basic variables to take into account while creating an organization of the type "Organization" are:

- Organization Type = Organization
- Include Accounting = Yes  
  If the accounting configuration at this level needs to be shared by all the organizations underneath the one being created.
- Accounting Dimensions = Business Partner, Product and Project

The basic variables to take into account while creating an organization of the type "Legal with accounting" are:

- Organization Type = Legal with accounting
- Include Accounting = Yes
- Accounting Dimensions = Business Partner, Product and Project

The basic variables to take into account while creating an organization of the type "Legal without accounting" are:

- Organization Type = Legal without accounting
- Include Accounting = No

The basic variables to take into account while creating an organization of the type "Generic" are:

- Organization Type = Generic
- Include Accounting = Yes  
  If this organization requires its own accounting configuration besides the inherited one, otherwise include accounting = No
- Parent organization = should be a "Legal with Accounting" organization.

**3.** Enterprise Models examples:

![](/docs/assets/drive/h9cS1Sgl07mpOdqMyrCNa-D3w4typy34vJcGl9wb5xk8vnpOkO4dPBwmBwY1JygGfPEeaQvh7katpn2-_fdTLWn5FyeIEPwZcNdkhkkKn0FUjTCTRLUosk2YcYwMoBegzLlVMzmCFCRzQztOKA.png)

![](/docs/assets/drive/0mFr7Nl9jVy9ZVIfNVOl8pKVHpLv2h6waw6r0iGBnpjTs8A0P4wYIWAHFbYJKGrduahpu1QbmH4UXDq9n27_ffdvfgAcd8_plxvBEXx8cY7j7eWRjIvLBtByLU0-9Zw1iKsVttxtv3ecG9oNZA.png)

![](/docs/assets/drive/2IIoZGBxPH1gigLWVMWKxE0GxWoAtAFJX2yheNUuOYoy_orJdRJII2rVZUpGcA8j4aJavDIoRIi1WJDymLDxqAbg-r-u6z4E91SRafrj9bX-EK4M8nhpqUqM1ufnYsgBc51D3HXAxZDPuy7R5A.png)

### Organization type

#### Introduction

An organization can be a Legal Entity, a Business Unit or neither of both. You can also select if transactions are allowed or not for this organization type.

#### Organization Type

Etendo default Organization types are:

**Organization** - an organization which is not a legal entity and does not allow transactional data entering.

- This type of organization allows the creation and configuration of master data to be shared among a group of organizations of any type belonging to it, for instance Business Partners, Chart of Accounts, etc.
- It does not require a general ledger as it does not allow entering transactions but it can have a given General Ledger configuration to be shared among the organizations underneath.
- The accounting periods can not be opened and closed independently at its level.
- And there could be as many organizations type "organization" in a branch as required.

**Legal with accounting** - an independent legal entity with a unique Tax Id number which requires accounting, therefore:

- this organization requires General Ledger and therefore an Account Tree or Chart of Accounts, as well as a Fiscal Calendar because the accounting periods can and must be opened and closed at its level.
- This organization type allows the "consolidation" of the Balance Sheet and P&L reports only for the Chart of Accounts it has assigned.
- Transactions are allowed for this organization type.
- And finally, there can only be one legal entity per tree branch, therefore the organizations underneath inherit the General Ledger configuration and the Fiscal Calendar of the legal with accounting organization.

**Legal without accounting**\- an independent legal entity with a unique Tax Id number which does not require accounting because it is managed in a separated system, therefore:

- this organization type does not need a general ledger nor a chart of accounts and will not support financial reports at its level.
- Transactions are allowed for this organization type. Transactions which will not be posted to the ledger.
- It can not have another legal entity in an upper/lower level of the enterprise tree structure.

**Generic** - an organization which is not a legal entity but must belong to a legal entity placed at an upper level in the organization tree structure. For instance departments or divisions within an organization or legal entity.

- There could be as many generic organizations as required per tree branch but always under a legal entity.
- This organization type allows transactional data entry, can have its own general ledger configuration and can inherit the general ledger configuration of the legal entity with accounting they belong to.
- The accounting periods can not be opened and closed independently at its level.

Additionally, an organization type can be configured as:  
**"Legal Entity"**  
**"Business Unit"**
**"Legal Entity with Accounting"**  
**"Transactions Allowed"**

!!! info
    Note that any of Etendo Organization types are configured as "Business Unit"

### **Organization**

#### **Introduction**

An organization is an enterprise of a Client. Each client must have at least one organization created by running the Initial Organization Setup process. The process of creating an organization ends after setting it as "Ready".

In other words, the process of creating an organization ends after setting it as "Ready" since Etendo requires performing some checking which validates that the organization has been properly created and that the organization structure is valid. If an organization is not properly created, Etendo will display an error when trying to set it up as ready.

Once an organization is set as ready, no changes can be made to the organization anymore. New organizations can be added, but cannot be placed above the current organization. They can be added underneath or at the same level.

#### **Organization**

The Organization window allows the user to maintain the organizations created by the Initial Organization Setup process.

There are different types of data left to be entered or changed for an organization:

- The Legal Name of the organization, this name, if any, will be the one used in the financial and tax reports.
- The Summary level checkbox informs Etendo if an organization is going to be a parent organization or not.  
  If an organization is set as summary, it could be selected as "Parent Organization" while running the Initial Organization Setup process.  
  This flag can always be changed regardless if the organization is already set as ready, as it is always possible to add organizations underneath an existing one.
- The Allow Period Control checkbox is only shown for "legal with accounting" organizations.

![](/docs/assets/drive/35uC1djW49ivi4h02RbbcaNyghZdV2ttZh-LGAZNR9ndREhkn74Dc06RJc6n4_htYuBL4OMH1uYDtMgr0qovmyhA6Pk7N-c7XWjF1e0C7Og1RQZb4y7SThakjOIZDfW8lhxjloWQ.png)

If enabled, it allows selecting a Fiscal Calendar for which the corresponding fiscal periods can be opened or closed in the Open/Close Period Control window.

- Opening & Closing periods process impacts to the organizations underneath the "legal entity with accounting" organization.
- The organization's General Ledger.  
  For instance, legal entities with accounting organizations need to record and post the financial transactions such as invoices and payments to the ledger.  
  Etendo allows customizing the way that the financial transactions are posted to the ledger, that means customizing the General Ledger configuration to meet the organization's needs.  
  This field is automatically defaulted by Etendo, which means that a general ledger is created by default, if :
  - a Localization Pack containing a localized chart of accounts module
  - or an accounting CSV file
  - or the Generic Chart of Accounts Module is installed and then selected while creating the organization by running the Initial Organization Setup process.
- The Default G/L Item for Funds Transfer is used to set default value for G/L Item parameter in Funds Transfer Process from the Financial Account.

**Inherited Information**

This field group is collapsed by default with the following read-only fields.

- the organization's **Period Control Allowed Organization**.
- the organization's **Calendar Owner Organization**.
- Calendar of the organization's **Calendar Owner Organization**.
- the organization's **Legal Entity**.
- the organization's **Business Unit**.

Above fields are automatically fetched and set with proper values when setting organization as ready.

An organization can have only one general ledger configuration assigned unless:

1.  the organization has its own one and besides inherits another one from its parent organization
2.  or if the _advanced general ledger configuration feature_ is enabled at system level.

The way to allow an organization to have more than one general ledger configuration assigned is described below:

- As System Administrator, set your own "template" as "In Development". Save.
- Once done, navigate to the "Windows, Tabs, and Fields" window
- Find the "Organization" window
- Navigate to the "Tab" tab and double click on the "General Ledgers" tab
- Set it as "Active". Save.
- Above detailed steps shows the General Ledger tab, which allows assigning more than one general ledger configuration to an organization.

Food & Beverage (F&B) sample client shipped with Etendo illustrates scenario 1 above:

- Every F&B sample client organization has been created by running the "Initial Organization Setup" process.
- The "F&B International Group" is an "Organization" Organization Type.  
  An Accounting CSV file was selected while it was created, in the same way as the "USD" currency, therefore this organization has the "F&B International Group US/A/Dollar" general ledger configuration assigned.

![](/docs/assets/drive/tLSZQxp8xgwVv1GQOCVPR1ChHCnrGZ2-UQzAddoZKw4FvXouGcLHhfnVJBS4CS4i2lHeEhxCwDy9SDIRpBmVxuKagI42qJ8Ol4kBnBZOKMxq0fiF6wEqW3BGHXfKEzxaaJjPK6HT.png)

This general ledger configuration can also be shared by the organizations underneath, for instance "F&B US, Inc" and "F&B España S.A."

- Same way, an accounting CSV file was also selected while creating the "Legal with Accounting" organization "F&B España S.A." same way as EUR currency, therefore this organization has the "F&B España, S.A US/A/Euro" general ledger configuration assigned.  
  As a consequence, "F&B España S.A." has two general ledger configurations assigned, its own one and the inherited one.
- Besides, each of the general ledger configurations mentioned above are linked to a different account tree or chart of accounts.
- Therefore, every time that an "F&B US Inc" transaction is posted to the ledger, Etendo opens a new window named "Journal Entries Report" which shows the journal entry created for the "F&B International Group US/A/Dollar" general ledger configuration in USD and in the corresponding accounts of a given Chart of Accounts.
- Every time that an "F&B España S.A." transaction is posted to the ledger, Etendo opens two new windows, one per each general ledger configuration, one of them in USD and the other one in EUR, both of them in different accounts.

The tree action button

![](/docs/assets/drive/_YumQFCw0KLD-SFUaGI8zjTteIM6MCZo-pEA8IHbI757561hE9StOwYttf2lqUdlmcm8s7G6XtIR5ZjDwckNhEt8q9yIKTqpduMk-kYk3g5NPe24Pvq9DVCg_803cj5Y_cVbz1FX.png)

allows dragging and dropping an organization within an enterprise model, whenever it is not "Set as Ready".

**"Set as Ready"** process takes into account the list of requirements below per organization type:

- _Organization type_:
  - No requirements
- _Generic type_
  - to have a "Legal Entity" organization type up in the enterprise model tree.
- _Legal without accounting_
  - not to have another "Legal Entity" organization type up in the enterprise model tree.
- Legal with accounting
  - to have its own general ledger configuration or an inherited one
  - to allow period control
  - to have a fiscal calendar assigned

Once an organization is set as ready:

- The organization newly created can not be moved up or down within the enterprise tree and can not be deleted.
- It is not possible to create new organizations up in the tree but underneath or at the same level.

#### **Information**

Information tab allows the user to add relevant information of an organization, information such as location and tax ID number.

![](/docs/assets/drive/EsSwADTSSP7pJ1foh5fXjLZBaL1lb-u2MwMI9KFZaxpgC9ayM66e0NmIcdCOhXEzWLBG78RrjGI7VN_l1mdQg6COaMO0_lQhaXwafKPnSphAcus_1aqxM2Glbickzi645CuxqPVi.png)

Fields to fill in are:

- the organization Location
- the Tax ID number, if required
- the DUNS number, if any
- the User who will act as the main organization Contact. This organization contact is used in some localized fiscal reports (Spanish fiscal reports), that requires a contact person.
- The purchase invoice number which will be used for payments. There are two options available:
  - "Invoice Document Number" (internal number)
  - or "Supplier's Invoice Number"  
    \- Any of the above will be included in the payment description field to inform about the invoice number being paid.  
    \- This also changes what is going to be shown in several purchase windows such as _Add Payment_ button in purchase invoice or _Add details_ in Payment Out

Finally, the checkbox Tax Not Deductible allows configuring an Organization as a _non tax deductible organization,_ if enabled.

That is the case of Organizations like Public Sector organizations for which tax deduction is not allowed. In this case:

- the purchase tax is posted as an expense
- and the issued sales invoices are tax-exempt

The field Sales Tax Exempt Rate allows entering a by default exempt sales tax rate to be used in the sales invoices by the non-tax-deductible organizations.

#### **Period Control**

Period Control tab is a read-only tab which lists the fiscal calendar period status of an organization.

![](/docs/assets/drive/kwmxym70AykyaAYetGSTUoXl5ucDq29sJTt2mo3R0vCsxeSSnyIrP_1jtd36ENRoQHLrrHfFs3__qR6w2wn1hAbwEYbLmQtJ2SUoYa35ffgOHUiWFXUDDwnaL_Vt_ebrZIeAbDBo.png)

**The Status**

It is split in two columns. One that represents the Status with a color code, making it easier to understand the situation at a quick glance. The other one represents the Status by its name, making it possible to filter the records shown. The possible Status values are:

- All Never Opened, colored in gray. Recently created Periods.
- All Opened, colored in green. All the Document Types are open for this Period.
- All Closed, colored in red. All the Document Types are closed for this Period.
- Mixed, colored in orange. Not all the Document Types have the same Status value in this Period. For more information refer to the Documents Tab below.
- All Permanently Closed, colored in red. All the Document Types are Permanently Closed for this Period.

This tab can be used for searching for a period (i.e. Jan-19) and get its current status.

As shown in the image below, the period Feb-19 has a mixed status, meaning that not all the Document Types have the same Status value within the Organization "F&B España S.A." which has the "Calendario España" assigned.

![](/docs/assets/drive/cjahc3FYZMghn48UlTxGriply3wDhO6ZrX7BsdnjoN5X3rcwWWdLMoeiUbYQ-z--lNwxjsqgmI0d4-8dldLYHy4kY5CqUaj4n7ZAWfg0ML8NxMm9M5ykXpt9kzkh5O-sI2KEjpnz.png)

For more information, see Open/Close Period Control.

#### **Documents**

Documents tab is a read-only tab which lists the Document Category status for a selected period of an organization.

![](/docs/assets/drive/p2dQZKtljDS-XwNG0QoRVerVIGFhmR02mySLnF1RE_Cdjv1_jPAGhBCTccBupCha87MLhjnIjUOZGqEaJ1BndBl_sPUl2AGkTI23CJfcnbdB0fDJTRLXaN7oZ2EGhfHTa18bH_Ss.png)

For more information, see Documents in the Open/Close Period Control window.

#### **Data Sets**

Data sets tab allows viewing the reference data applied to the organization and informs in case there is any update of a reference data applied available.

![](/docs/assets/drive/eIRJ-zXUf_s6qjf9H9aPP6ynr5hrgULf6DqAwhPtKq4PeR86LpUlWRS8FmcHglGxffMZzBw4AV0vBcyc0xXQO5HV6cxmc6pB0P_qF67nS2NknaRuS58DK3izsNbbO-xj7PM9zLAO.png)

#### **Warehouse**

Relation of prioritized on-hand warehouses of the Organization.

![](/docs/assets/drive/6fsqpwBtDAXTJbyug4QSODfEv9-GzyhEMHMQQYgnsIufDr4S4GOCjrOOCSSeGz_u4GnkuVlaUPnOiH83pQbORHhsf2pLzKJKAaPERxaqCNXaHXgWRTz8-sIFqQzg4h_NTOJHKPmC.png)

In this tab, it is possible to define the organization's warehouse/s, that way the quantity on hand of an organization is the sum of the available stock of its warehouse/s.

It is possible to define the priority of each organization's warehouse/s therefore Etendo proposes first the goods of the warehouse with a higher priority.

## **Security**

Security folder allows creating and configuring basic security entities such as users, user roles and access rights.

### **User**

#### **Introduction**

A user is an entity which can log into Etendo whenever it has a password and at least one role assigned to it.

![](/docs/assets/drive/uYk0-n-xUoagkerOKb87gcQ11qfxJ4C2C_uPR-SR_HlmbDw89FyUm7UY86xbdoD3TjOPpEBVFu0aITdVibP7fnpylt_fn8SttMp0fH3HkNOAle71cVvxAmMtvbMPkBN4rHrhr21j.png)

As shown in the image above, Etendo allows the user to sign in by entering a username and a password previously created in Etendo. The user assigned to that username will be able to sign in only in case it has at least one user role assigned to it.

#### **User**

User window allows the user to create as many Etendo users as required. Each person accessing Etendo can have a different user assigned.

![](/docs/assets/drive/Xu1oqRnWMgbWI8-qp1RP-stpJ2YwNnKLJr04-gRcVOrIEkJm_er9fWwpe4F2Ncy_u3pATEEGw7t59JJrUW2y9QSsmNWTT9XXlC0cZuqlakWhF2KIfYfw6IaJhrseTY1tKjE0Uavl.png)

As shown in the image above, a user can be created by entering the basic information below:

- the _User First and Last Name_
- the _"User Name"_ and the _"Password"_ to use for logging into Etendo
- and in the case of being an "Employee", the employee business partner records in the field "Business Partner", under the "More Information" section.
- the _"Expired Password"_ checkbox: if it is checked, the user's password will be set as expired and when the user logs in, he will be forced to change it.

#### **User Roles**

Roles are the connection between users and access rights. Each user can have more than one role assigned, however, a user can only log into Etendo by using just one role.

![](/docs/assets/drive/IdpYeASr5qFi9zCa5EgsKRJfg54EoyBsxbVbj3d7DIbN-8XztHzj2QI35lguEXIKt6FxAmkozQnh7sGeMaKYD4m7-x5QSemv2M48ShmpCxhVWCLFwGa4e94oA1yl4K7-JprsrIcf.png)

For instance, it is possible to create and configure a role for Sales, a role for Finance, a role for Warehouse, and another role for Procurement.

Those roles will have to be configured to allow access to either sales, finance, warehouse or procurement windows, processes and forms. To learn more about how to do this, visit Role.

Whenever there is a new member in the organization, a new user could be created and assigned to any of the existing roles instead of creating and configuring new users permissions every time.

There can be a user having a given role set up as "Role Administrator", that user will be able to add new users to that role.

![](/docs/assets/drive/6lcpMBWvPHq9NQ2VCpAiYVfd_SBR-7j3aDTZ9c4QyqmQi7Nguuid_7y8TQNEXkh7pLH26YU7fKgqpdMEgi1L3aXyKnoyf6PTz-tutOmotGaFFhh7BG_2-QoafKz4JSrmS8mpXVzS.png)

### **Role**

#### **Introduction**

The aim of a role is to group user/s depending on what parts of Etendo they are allowed to access to and therefore to work in.

!!! info
    Etendo comes with a "super" user named "admin" (_password "admin"_) which can be used to sign in for the first time.

The admin user has several roles assigned:

- the _System Administrator Role_ (this one is assigned to it by default)
  - this role enables admin users to have admin rights to all the existing Clients.
- the _F&B International Group Admin Role_ demo data (this one is also assigned to it by default)
  - this role enables admin users to have "F&B demo data" Client admin rights.
- and besides:
  - every time a new "Client" is created by running the Initial Client Setup process, Etendo automatically creates for that Client a _"Client Admin"_ user linked to a _"Client Admin role"_:
    - the client admin role enables "Client Admin" user to have admin access rights to that Client and all the organization/s of that client once signed in.
    - the newly created client admin role is also assigned to the admin user by default, therefore it will be possible for the admin user to access the newly created Client.

Finally, every time a new "Organization" is created by running the Initial Organization Setup process, a new user and a new role are created and linked to each other, this time the new user role will only enable the user to access that Organization once signed in.

Having said that, Etendo allows the creation of as many new "Roles" as required to be later on assigned to the existing and/or new users.

!!! info
    Roles group user/s depend on the tasks they do and therefore the parts of Etendo they should have access to parts such as windows, processes, forms, widgets and views.

#### **Permissions Inheritance**

It is possible to configure roles to retrieve their access to the different Etendo elements automatically, by inheriting them from other "parent" roles. This configuration is possible thanks to a feature known as Role Inheritance.

Having a role, it is possible to assign one or more template roles to it. This way, all the elements which are accessible by these template roles will be available automatically for that role as well.

Besides, any change done in a permission of a template role will be propagated automatically to every role inheriting from it.

!!! info
    Notice that it is only possible to inherit permissions from template roles, which are manual roles as well.

When inheriting from multiple roles, the permission application order is determined by the sequence number of each inheritance. This means that if a particular permission is inherited from multiple inheritance, the permission will be taken from the inheritance with higher sequence number.

This process eases the role management, specially when the number of roles defined for a Client is high. Thus, it is possible to define template roles to give access for a particular set of elements, and then create multiple combinations of functional roles in order to give personalized access for the different users. This is illustrated in the picture below.

![](/docs/assets/drive/vyHTH7_aVNAVElZ2_BGWT5QcVh9MD3w_DCfz20k4Bu6mxa_QCvrKo2ufgIMmvqericF1SZnMm4ONeysEKiw2kON-47niJ5HlcjaVqGiiqPkcNyg9k0FOmnZHHfbqpioJ9At6rbTI.png)

The current list of inheritable elements include the following: organizations, windows, tabs, fields, processes, forms, widgets, views, process definitions, preferences and alert recipients.

For the case of preferences and alert recipients, there are some restrictions to make them inheritable:

- A preference is inheritable if it has a template role set in the Visible At Role field.
- It is not possible to create more than one preference with exactly the same visibility settings for a template role.
- An alert recipient is inheritable if it has the User field empty.
- It is not possible to create more than one inheritable alert recipient with the same alert rule for a template role.

!!! info
    It is important to note that this mechanism takes into account the permissions manually given to the roles. This kind of not inherited access is not affected (not modified) in any case by the inheritance process.

It is also possible to force the recalculation of the permissions of a role, using the _Recalculate Permissions_ process. But following the common flows of a Role configuration, all the inheritances are calculated automatically, so this process is not necessary. For this reason, it remains hidden.

As mentioned before, the changes (create, edit or remove) done in a permission which belongs to a template role will be propagated automatically to all the roles currently inheriting from it. For this reason, a warning message is displayed on the _User Interface_ in order to inform users about the implications of this kind of action.

This warning message is similar to the one shown below. It appears when creating or editing a record that belongs to a template role, in a tab of an inheritable entity.

![](/docs/assets/drive/ibtK-OMAXBsv2UVQXFaPN7YvQMlh2rgo41Vt21hwrkhk0Grj3gy0Y_7tYhGZU4JZaX7i75-eo6xHmT7P7bHhUWyy2xIpcK5VB8rC7PqSxERaqBP7HXaLXKSeiyNf_1Sj_ZXhxDzb.png)

#### **Role**

The Role window allows the user to review, create, configure and maintain the roles to use in a given client.

![](/docs/assets/drive/8MOJrcJaif8MbvpR7NwOIA6JjqOIlmOf3df8nsTRJa7Zq02aanCB7SGImtBiEGqou4crWjRy_nGJNhUVj3rHpcNyYOVw8H-F_X4veFkEtGw_6KCGoJxom1R_MkOlm0pJhIbEYzMB.png)

As already described, there are roles automatically created by Etendo which can be reviewed in this window.

Besides, this window allows the user to create new roles for a given client. Roles creation can properly be done by using a Client Admin user & role.

The fields to fill in are:

- the Name and a brief Description of the role
- the "User level" which is a step forward _"Data Access Level"_ to be defined at Role level.
  - User level allows the user to limit the records which will be accessible in entities such as windows, processes or forms for a role; or even to limit the access to a given entity for a role:
    - Every table in Etendo has a "Data Access Level" defined. The options available are:
      - System, this level allows the user to see System Client records and (\*) organization records, for instance application dictionary records.
      - System/Client, this level allows the user to see any Client record and (\*) organization records, for instance master data related records such as Countries.
      - Client/Organization, this level allows the user to see any Client record but System Client and any Organization including (\*) Organization, for instance master data related records such as Products.
      - Organization, this level allows the user to see any Client record but System Client and any Organization record but (\*) Organization records, for instance transactional data records such as Purchase Orders.
  - User Level available options are:
    - _System_, if a table is defined as "System" data access level, a user role which has this user level assigned will be able to see the records of any Client including System Client records, in an entity such as a given window or form.
    - _Client_, if a table is defined as "System/Client" data access level, a user role which has this user level assigned will be able to see the records belonging to any Client but System Client, in an entity such as a given window or form.
      - On the other hand, if a table is defined as "System" data access level, a user role which has this user level assigned will not be able to see any record as all of them will belong to System Client.
    - _Client + Organization_, if a table is defined as "Client/Organization" data access level, a user role which has this user level assigned will be able to see the records belonging to any Client but System Client and any Organization including (\*) organization, in an entity such as a given window or form.
    - _Organization_, if a table is defined as "Client/Organization" data access level, a user role which has this user level assigned will only be able to see the records belonging to a given organization but (\*) organization, in an entity such as a given window or form.
  - Additionally, depending on the role's user level, no data at all is visible based on the table's access level. This restriction can be bypassed by setting _Bypass Access Level Entity Check_ preference to _Y_, the cases when entity is not accessible are:
    - If access level is System and user level is not System
    - If access level is Organization and user level is not Organization or Client+Organization
    - If access level is Client/Organization and user level is not Client, Organization not Client/Organization
    - If access level is System/Client and user level is not System or Client/Organization
- Manual check. The role automatically gets all standard user plus admin privileges, even when new elements such as windows, processes, forms, widget classes, organizations are added unless the Manual check is enabled.
  - If the manual check is enabled, it will be possible to manually assign access to windows, processes, etc by manually selecting them in the corresponding tab or by using the process button "Grant Access".
  - Grant Access process button allows the user to select:
    - the _module_ or application area for which access is required, modules such as Financial Management or Production Management among others.
    - and the _entities_ of the module selected for which access is required, entities such as windows, processes or forms among others.
  - If the Grant Access process is executed for a role marked as _template_, the granted accesses will be propagated automatically to the roles inheriting from it.
- Template check is shown for roles which have a manual access assignment (Manual flag is Yes). Roles marked as template are those that can be used by other roles to retrieve their permissions automatically, using the Role Inheritance mechanism.
  - For this reason, just template roles can be selected in the Inherit From field of the Role Inheritance tab.
- Restrict backend access: If checked, this role will not have access to the backend (ERP). It will however have access to other applications (such as the WebPOS).
- For Portal Users: If checked, this role will have a simplified (portal) interface, where he only has available the workspace widgets. Portal interface changes the look and feel of the workspace. Top page menu and left-side menu are hidden. Usually a role for Portal Users gives access to users only to their own information using widgets.
- Portal Admin: If checked, the Portal Role will have Portal Administrator privileges.
- Is Web Service Enabled: If checked, web services will be able to obtain data for users with this role. It applies to both JSON REST and XML REST web services.
- Advanced check is shown for roles that have an automatic access assignment (Manual flag is _No_) and automatically grants access for such roles to all Advanced Features.
  - Manually created roles (Manual flag is _Yes_) have their own configuration which can include advanced features or not so this flag is not shown for them.
- Client Administrator checkbox allows a role to admin other users' _Workspace_ as well as _Customized Forms"_:
  - In other words, a client administrator role can assign widgets to the workspace of any client user as well as customized forms.

#### **Org Access**

Org Access tab allows the user to define the organization/s to which a given role will have access rights to.

As already mentioned, every record in Etendo belongs to an organization, therefore the only way for a user role to edit a record which belongs to an organization is to provide that user role with access to that organization.

![](/docs/assets/drive/vE-K35fSEj9-BIvgbMGezZvFFgFx4-bfY-LNbMosiyjun4B_-bSKiWnHr-K7bpJSnYwrSypNacZYFmcO9x46g3yGgrHxrywB-z2Agfywx-qVesqxPN9ruiBg45aTxqkyn15BsOkb.png)

- _Organization Administrator_ checkbox allows a role to admin other users' _Workspace_ as well as _Customized Forms"_:
  - In other words, an organization administrator can assign widgets to the workspace of any user of the organization as well as customized forms.

#### **User Assignment**

The User Assignment tab allows the user to add users to a given role.

![](/docs/assets/drive/iBeXu8RdIKr-srDU5Q-1Y5e5wYtbvNbXqD8KtMx8MK2gHEXc9BJUcYsA19OgHzCNv7chh30Ws8bVjbtjFkllwl5w8kZZ2ZoAbiXLOeFJDzwEisQu04z8dGAj3CmIy0OOxneMJtz6.png)

"_Role Administrator_" checkbox allows the user to administer the given role for:

- Widgets: they will be able to set default widgets that will be seen by other users with the same role.
- Saved Views: this user will be able to share with other users with the same role the views she saved.

!!! info
    As _Role Administrator_ flag allows the user to modify behavior of other users with the same role, it should only be granted to trusted users.

#### **Window Access**

This tab lists and/or allows the user to add the windows to which a role will have access to.

As already mentioned, every time a new role is created and saved without selecting the "Manual" checkbox, Etendo automatically fills in all the windows in the Window Access tab.

The information above means that the newly created role will have access to every Etendo window.

![](/docs/assets/drive/vt5fH1QoVLs_KcIpoESYAQqhSe01e6oHVVFbF-UQy6fwJnDu8B4qOgQDCI34dQheclrgChwDy-IuurthKMqxAljaRU-jVczgUCGnXrXDTv2vERvhxlgGjRy7SA6ivWpqpYMBhcmQ.png)

Having said that, if the "Manual" checkbox is selected, it will be required to _manually_ add a subset of windows which will be accessible for a given role, or it will be required to automatically add them by using the action process "Grant Access". This process will allow window access for a given Etendo module or area such as Projects, Finance or Sales.

_Editable Field_ checkbox defines if the accessible data in a window can be edited by the role or not.

#### **Tab Access**

It defines whether a tab is editable or read-only for a concrete role.

In a window accessible by a role, it is possible to define for each of its tabs if they are editable or not through the _Editable Tab_ check.

If the window is editable (_Editable Field_ is checked), by default all its tabs will be editable. But it is possible to define some of them not to be editable for this role by adding them in this tab and setting to false the _Editable Tab_ check. Note this is only true if the table behind the tab is editable for the role.

In the same way, having a non-editable window, it is possible to define some of its tabs as editable by checking _Editable Tab_.

#### **Field Access**

It defines whether a field is editable or read-only for a concrete role.

Field Access tab works very similarly to Tab Access tab, allowing the user to define write access up to a field granularity level.

So if a tab is editable for a role, a concrete set of fields can be made read-only for that role, adding a new row in this tab for each field and setting false _Editable Field_ of each of them. Or in the other way around: in a non-editable tab, fields can be editable if they are added and their _Editable Field_ property is checked.

When editing a tab with some fields defined not to be editable in this way, backend checks modifications in that tab to prevent this to happen. Note this also affects the field in case it was modified by, for example, a callout or a default expression. This is controlled by the _Check on Save_ property, unflagging it, this check will not be performed allowing thus the field to be modified by a callout.

#### **Report and Process Access**

This tab lists and/or allows the user to add the reports and processes to which a role will have access to.

As already mentioned, every time a new role is created and saved without selecting the "Manual" checkbox, Etendo automatically fills in all the reports and processes in the Report and Process Access tab.

Above means that the newly created role will have access to every Etendo report and process.

![](/docs/assets/drive/jeSO8cKGRMnO5jlOseLchbPh4OE2fDeLeAAS0VSOIngREivxtfTmTPmNLaDwnn7ujstw7z6Pgqp0oZLZAHxwT1XwtyGmlZdj-vuNEBXnBq1dFNo5UvBFIC_CIAJc6Tn2gweJJPKq.png)

Having said that, if the "Manual" checkbox is selected, it will be required to manually add a subset of report and process which will be accessible for a given role, or it will be required to automatically add them by using the action process "Grant Access". This process will allow report or process access for a given Etendo module or area such as Projects, Finance or Sales.

_Editable Field_ checkbox defines if the accessible data in a report or process can be edited by the role or not.

By default, access to processes in a standard window given from a button is inherited from the permission to the window. So if the role has access to the window, it will be possible to execute all the processes defined in that window, regardless if there are explicit entries for them in _Report and Process Access_ tab. This default behavior can be changed in two different ways:

- To revoke this inherited access and manually decide case by case which are the accessible processes, it is possible to define a "Secured Process" Preference (at system level or for that specific window) with "Y" as value.
- If the developer defined the process as _Requires Explicit Access Permission_. In this case, permissions will never be inherited for that process.

#### **Form Access**

This tab lists and/or allows adding the forms to which a role will have access to.

As already mentioned, every time a new role is created and saved without selecting the "Manual" checkbox, Etendo automatically fills in all the forms in the Form Access tab.

The information above means that the newly created role will have access to every Etendo form.

![](/docs/assets/drive/h71SGbrOND-3ZRiDfheu69SJe6ZUIfQdyVOKmL_RaRtqSCRmQ84JoLrhPok37CDsfNRt0BbqoKwNzchby0i1ffWbKxN1JZZy2wBjC_akKrtaYwtR9FNCgEJaYGEFtse9xsx2kG4_.png)

Having said that, if the "Manual" checkbox is selected, it will be required to manually add a subset of forms which will be accessible for a given role, or it will be required to automatically add them by using the action process "Grant Access". This process will allow form access for a given Etendo module or area such as Projects, Finance or Sales.

Editable Field checkbox defines if the accessible data in a form can be edited by the role or not.

#### **Widget Class Access**

This tab lists and/or allows adding the widget classes to which a role will have access to.

![](/docs/assets/drive/UJdYTlYdE7iCbPZXvMLbM-FtRsvCjm1H0ogLpoAgaHlt18r4-hS0gB0jXOCtea26kAn3l9phNMuoqFO5uvrKDqHnd_99mcY6FqmqGhHKwcwIiozXLsji0LHlgp6KWLzKuvVYq6S_.png)

Widgets are _User Interface_ elements which can either be placed in the Users' Workspace tab or be part of a generated window.

#### **View Implementation**

View implementation tab allows the user to select customized views.

A view implementation is a completely custom implementation of a main view.

The access to a _custom view_ can be controlled through this role access tab.

![](/docs/assets/drive/5OCz4Fl8K2i8uYaKdMnh3lg-DT_9IQBDjimbD37HCtwzOs74M-OTqbTorDwTzxEQaWJBKZRxkhNJc_jF-4kjLOllZSlfZe_9kcngt9KUQB0X3KVYFyeOblGXuzo0LCGDI-C_QlvI.png)

For additional information about views, visit How to implement a new main view.

#### **Process Definition**

Grants access to Process Definition. By default, access to process definitions in a window (given from a button), is inherited from the permission to the window. To cancel this inherited access and manually decide case by case which are the accessible processes, it is necessary to define a "Secured Process" Preference (at system level or for that specific window) with "Y" as value.

![](/docs/assets/drive/IFXcBPxniL5TViWp3QIr2LiircvQoutdDPZ4K-zMHibWBRtwsI2fNh8dTXWG5H8_GROHo17oFdKjb-Kuj696jezS3flqH9VJL8yAlFYFV0__mtN4aDKFHrIuosLt28EfSLpfT5iR.png)

Access when the process is invoked from a standard window button is inherited in the same way that for Processes.

#### **Role Inheritance**

It allows defining an inheritance for a role. An inheritance is a relationship between two roles: if role A inherits from role B, that means that all the permissions that role B has for different application elements like organizations, windows, reports, processes, widgets etc. will be automatically inherited by role A, allowing it to access those elements in the same way as B. It is also possible to define an inheritance hierarchy, i.e., a role can inherit from different roles, and the priority (order) to inherit the permissions is defined by the sequence number. This means that if two inheritances have accesses in common, the accesses of the inheritance with lower sequence number will be overridden with the accesses of the inheritance with higher sequence number.

Within this tab is where the Role Inheritance configuration of a particular role is set.

![](/docs/assets/drive/KI9-ImqA0ErnTQS_fepHzt63s_3ExEUeRwCXREoaE2NKc1e13FAmtPhHnCQC4CPLwWzbUvWZbertcWG81CDPmYaZzLhN8IrliDLcJ9V48S3VxosZwI2vzSlPc0suV5WKwYcPi8JF.png)

The fields to fill in are:

- **Inherit From**: In this field, it should be selected the role whose permissions will be inherited. It defines the role that will be used to retrieve access to its permissions automatically.
- **Sequence Number**: It defines the order in the application of the role inheritance, when having multiple records in the tab. The lower this value is, the earlier will be retrieved the permissions of the related template role. This means that if the same permission is accessed by two template roles selected to inherit from them, the permission related to the inheritance with higher sequence number will override the other one.

### Role Access

This window defines access to DB /database tables and columns for selected roles.  
Edit a role to give or withhold the necessary access to tables and columns tables.

#### Table Access

Create or edit access to DB tables for a selected role. The user can give access to the needed information by selecting the options displayed in the table tab.

![](/docs/assets/drive/ltwp9ZQne8C_2iz5c7u3hay0dodgaB28TeFFxVkLJqhFV3Zgq9LMahoeVrH2BRiz6NH9n1QeCsDSrOoPD_CtKV8cYZULNDDPG5Fly-WhZo5h7_2ASJRlnoS_GinX2nYC6efQebJ6uZYnYAeyabg.png)

### **Audit Trail**

#### **Introduction**

Audit Trail allows the user to monitor every data change done in any table or entity through the user interface.

Audit trail feature monitors data changes such as:

- Insert
- Update
- Delete

Audit trail feature must be enabled by the "System Administrator Role" in the Application Dictionary, as the first thing to do is to configure the table/s for which this feature is going to be enabled.

Once a change has been made in a table for which the audit trail feature has been enabled, it is possible to monitor that change through the user interface by using the action button "Audit Trail".

![](/docs/assets/drive/V-wLKxec4uzSuG-eFItBU00cQYeO5SNhiLTDkY78kPRaK6e-P_R_z39-K5icHtUSX-WjoeFL34_Iv45c0aym2FRV9_F_e0W6QA0U8Lim_qkovbX44ihOl-nH-mKEio1pSpfQDqlm.png)

#### **Audit Trail**

Audit Trail view displays read-only information about all the recorded data changes done in the tables for which the audit trail feature has been enabled.

![](/docs/assets/drive/CkScAz_BHFw9uZIejCEG18y9IOkyiO23K5CMqCRWCkc-DEAWZ0x5G8RyDwjqApky49FILfUisRIJUnqS_Sfob0j128cKfhFFQhfOI92bmbTAPsN1TyfGVMaPXeoj9tbBzqsTB-r4.png)

The changes done in a given table, column and record are viewed by showing the corresponding record ID or UI of the records in the database.

#### **Configuration**

In order to track audit information, the system administrator needs to perform two tasks:

- Enable the audit trail for one or more tables in the system
- Run the 'Update Audit Trail infrastructure' process

In the following sections, a step-by-step guide with more detailed information is provided.

#### **Enabling audit trail for a table**

Enabling/disabling the audit trail feature for a table is done in the Table definition in the Application Dictionary.

- Switch to the System Administrator role
- Go to Application Dictionary > Tables and Columns
- Navigate to the table for which you want to enable the Audit Trail
- Switch to Edit View
- Mark the "Fully Audited" checkbox and save

##### **Audit Inserts**

When a table is flagged as Fully Audited, the users can decide if they want to audit the insertions done in that table.

![](/docs/assets/drive/ebTtUMQskmHQd1Fd5BWoW0_lKwtwgNTn41V1uJKV4RGTKR_uXKuR_PqU4rzTUBVQct38OejbovWWycB-z1A7YEvwNedzpv6VCi38eHb2telDh9994cV4vCW1QEOGlDw1Ojs11Und.png)

If the Audit Inserts field is checked in a table, when a new row is inserted in that table several records will be inserted in the Audit Trail table, one for each column in the audited table. These records will contain the original value of the columns of the new row.

Usually, it is not necessary to store this information, because the original value of a column could be easily obtained by using the Old Value and New Value fields of the Audit Trial table that correspond with that column. If the Audit Inserts field is left unchecked, only one row will be inserted in the Audit Trial table for each record inserted in the audited table. At least this one record needs to be inserted in the Audit Trial table to be able to store which process was used to create the record in the audited table.

##### **Excluding columns**

By default, when a table is audited, modifications in any of its columns are audited. In some cases, it makes sense not to audit changes for some of them. This can be configured by setting the _Exclude Audit_ flag in _Tables and Columns > Table > Column_ tab.

![](/docs/assets/drive/Xy3wTyW3wrUeerAoND_Rw2c6wVVhxkq_AEzzTjBLLpiBg6VsMWcQjAn6T4te4akp_o-x381v3wT3012cttvLqjKWRsd-Tfe0Go0FX1KGlG_vSG57Bm4yo8ZnB0gxdTSV3qi7f-4b.png)

#### **Running the System Compilation**

The audit trail system uses a number of generated triggers (one per table to be audited) to collect the audit data for all changes.

These triggers need to be regenerated, when executing a system compilation, once the following actions have been performed:

- The Audit Trail feature has been enabled or disabled for a table
- There has been any structural change to a table being audited (i.e. new columns, changed columns)

#### **The Audit Trail Popup**

For the set of tables for which the audit trail feature has been enabled, a new button

![](/docs/assets/drive/tmlPernhlkGB49t7gLt12N3zfxbYevzxuPC65DZavmEO8p5UBe2_sO_YD6lBTkhBvnNrQ64jkRAnuahaKRTGnLPGUvmSEX_K5_Ekh5Ojd-21ZyZ4KWEFIjujNg_xqg_PCFahXdJo.png)

is shown in the toolbar of the corresponding windows. It gives access to the Audit Trail Popup.

This popup allows examination of the history of the record which is currently shown in the window. It has two main view modes which allow examining the following data:

- 'Record history' of a single record
- 'Deleted records' of a single tab

#### **The 'Record History' view**

This view is displayed when the popup is opened from an existing record via the new toolbar button.

The top area always shows a reference to the entity (i.e. Sales Order) and the record "1000175 - 2016-04-03 00:00:00.0-0.00" for which the history is displayed.

Then a number of filters are available which allow some restriction on the changes displayed to ease the use of records with many modifications.

The grid in the lower area shows all changes done to this record while the audit trail feature was enabled. The changes are shown sorted from the most recent change back to earlier changes.

!!! info
    Only fields which are visible in the corresponding tab are shown here.

A row in this grid corresponds to a single changed field. For changes to an existing record, the number of grid entries shown correspond to the number of fields changed. For new record creations or record deletion, one row in the grid is shown per field of the inserted/deleted record.

![](/docs/assets/drive/xuE5w_TI2LS9M4nl1fyqWctoD-pU08N6dq7mQJT7qr-wsocs2FehRp7Gu1jGCsJUu_UZeo1hmDjBPQRFV_d1aM26q9zxMjXPX5GbX-SZOJYuZTwo1PYtoD-oi3XRzlyS723rbaWL.png)

Finally, a link just on top of the grid allows switching to the 'Deleted Records' view. Following that link will show deleted records for the tab from which the Audit Trail popup was opened.

##### **Disable filtering by User**

The User filter can be removed from both the 'Record History' and the 'Deleted Records' view. This can be interesting for performance reasons when the number of users available is high. In order to do this, go to General Setup|Application|Preference and add the following preference: Show Audit Trail User filter with value Y.

#### **The 'Deleted Records' view**

This view allows examination of records which have been deleted from a tab and are otherwise no longer accessible in the user interface.

The general layout of the view is similar to the record history view.

An info on the top shows a reference to the entity for which the deleted records are shown. Directly below, a number of filters is available to restrict the records shown.

Then a grid displays all deleted records belonging to this tab/entity. Here one row shown corresponds to a single deleted record and the columns shown are the same as the ones shown in the normal grid view of the same tab.

![](/docs/assets/drive/lsX2HjGHdMbgCKFRs-_KuE1qmeMs2u9cZ5PXrJ5RmYw08PYbdJ6KB_dY93TwaW9ycfaNUc9fEWmsMFKPipMYza0ZCPZdMcl4c9sjFemg7ndkntS2ai5Rs-eePUDaFXXNdKFJ6VOV.png)

This view offers a number of navigation choices to view related or more detailed information.

##### **Navigation: Back to history**

The first one is Back to history. Following this link, the view is just switched back to 'Record History' showing the same records as shown before going to the deleted records view.

##### **Navigation: History of selected record**

The next one, View history of selected deleted record below, allows examining the detailed history of a deleted record, instead of the summary view which is shown here.

This detailed history is displayed in the same 'Record History' view, however its top info area notes the fact that the history of a deleted record is displayed.

The following screenshot shows an example of the history view of the same deleted 'Sales Order' entry. Compared with the previous example of this view, new history entries corresponding to the deletion are shown in addition to the older information about the record creation and modification.

![](/docs/assets/drive/GtW2mnbfKHPPLTLwrt_Kqjlbdm7lo_7CLDntpxMg4vRZnjAaRkOeUzxOg19gnju2DAgUuLBNrm0szABl1MVSV5Ft9_5ASwBs9jTI9IYuQt1iBTBU3r2z5J-octdDlOzNknRzXKKz.png)

##### **Navigation: Child Tabs**

As the last method of navigation, the popup allows filtering records based on a parent record. This can be useful to search for deleted lines belonging to a sales order.

There are two possible ways based on the status of the parent record: still existent or already deleted.

If the parent record (i.e. a Sales Order) does still exist, then the following steps can be done two view its deleted lines:

- Go to the lines tab of the Sales Order
- Click the audit trail icon to open the record history view
- Use the 'Deleted Records' links to switch to deleted records view

As the lines tab is not a top level tab (it has a parent tab Sales Order) the deleted records view is automatically filtered to only show lines belonging to the current Sales Order. As visual information that the information shown is filtered, the top info area shows:

![](/docs/assets/drive/TLPq4qy1yN9UkGD66_5njmuYw_ks8rUXRuOSuS6oXS_BmY92i1kLNyPns4CRsopMKIif0JPp6uJfWpDHgeKgtD07RAR8XcmrVEafUyhiVJ-OEUHhxUF3i77gURAyQPl8yK7PZMLk.png)

If the parent record (i.e. a Sales Order) does not exist anymore, then the same can be accomplished by using the following steps:

- Go to the 'Deleted Records' view of the Sales Order tab
- Search the Sales Order for which the deleted lines should be shown
- Click the _Lines_ link just below the grid

Then the deleted records view will show the deleted lines belonging to the selected (deleted) Sales Order.

#### **A generated Audit Trail Window**

The second interface to view audit data is a normal generated window which is based on the AuditTrail entity, and allows browsing all audit information filtered by the currently active client. Open the Application menu and navigate to General Setup, Security and select Audit Trail.

It offers a raw view of the audit data, meaning that no translation of raw values is done, but instead the raw column values of each change are displayed.

Simultaneously, this window allows a much more flexible filtering/searching.

![](/docs/assets/drive/rw7tPRLbT6ngBKyscK7lPe8F8irNUTp74vKBpDDST539eM5zHpl99Sr2fMXFLMcFks6BVhyNsMfFaSeWHgHYSr2vF2GDYjZ6a5fyAa3Nj2QEcpUhGAL6xOPIVwY177LL6kESljcr.png)

#### **Limitations**

The audit trail feature will record all data changes (for the table for which it has been enabled) with the following exceptions:

- text fields of types (char,varchar) with a length >= 4k will not be audited
- text fields of types (nchar,nvarchar) with a length >= 2k will not be audited
- BLOB fields (binary stored inside the database) will not be audited

## Etendo Advanced Security

!!! info
    To be able to include this functionality, the Platform Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [_Platform Extensions Bundle_](https://marketplace.etendo.cloud/#/product-details?module=5AE4A287F2584210876230321FBEE614){target="\_blank"}

The **Etendo Advanced Security** module allows the user to customize several security features such as the following:

- Password Security
- Password History
- User Lockout
- Multiple Session Verification
- Changing Password after Login
- Expiration Time (Autolock Password)

!!! info
    For more information about the module configuration visit the [Technical Documentation](https://docs/en/technical-documentation/bundles/platform-extensions-bundle#etendo-advanced-security#etendo-advanced-security)

### **Password Security**

This functionality is executed when the password is changed, either because the user needs to change it or because the system requires it. The process can be done from the **Change Password** field in the navigation bar and/or from the **User** window.

From the **Change Password** process, Etendo will ask for the current password and the new one to make the change. After clicking on **Apply,** a series of checks will be verified to finally execute the corresponding changes.

![](/docs/assets/drive/sQNqx26cwCGfPld7D47SHw_QnmdO5-zHlJ41yN28V3yKv95xq6PMGqHobkKuh8rQa11RNvI6bMpkWMk9k0H6P_n8DilZ0NfQ56yjBZYaP85WyQWXC7shoMt7zU6nxO-3-JMUXzwRJ2ASii0YDJpUN6s.png)

!!! info
    The password must be no less than 8 characters long and its structure must contain at least three of the following characters: letters, uppercase letters, lowercase letters, numbers and symbols.

If the new password does not comply with the above mentioned conditions, a popup appears with an error message indicating the conditions to be fulfilled.

![](/docs/assets/drive/shTQdtbDJq_FrCieCra0q6YLlv5akL6vFAS2Xr9sogzi6IMddd-qi9HJDwKKhxY0fCqpUfcFa-l0agc03ypnwtH_eFpDR6SLWNPVi4edc--fKnZsuzeFwnNC_ITWGd5q07zMCr1ImePmG5cOLmSH_rQ.png)

This process can also be executed from the **User** window by applying the same password requirements mentioned above.

![](/docs/assets/drive/JNG3VeVWDWewBfz_iijE7kUBTZBV-8DUBQAWaiEa1uyxhOxYZxmbC_bavwTW85z0LJ_S9ibzN1XVz8pGIZQZz675KBO8H8vaO1LJ8BXxO3Sl5AOqOvOV2hgDKjMObk6CWCpmB8ChETBvqkEICBJ0SI4.png)

**Etendo Advanced Security** verifies the changes, and if the new password does not fulfill the required conditions, Etendo shows an error message at the moment of registering the changes.

![](/docs/assets/drive/jUjckeZt5RPHdHYZcD0xN9BXUkKoNLOYPrkLIkG4pyqPJBYvFFtkWWKBzgy3pZ2Qr1M-kGZPzd2YXiNxOuOlNdVj26PDen8jOxw-44zBzZsX1G3eNTiIzIHidjO8eiDmrY-uU-XhkUxG2RiUbahRbbQ.png)

### **Password History**

When changing the password, one of the conditions to be fulfilled is that the new password cannot be the same as a previously used one. Etendo creates records of the previously used passwords so, if the user enters a previously used one, the system informs with an **error message.**

This security feature can be configured only with **System Administrator permissions**. To do this, go to the **System Info** window, within the group field **Password Security**, and check the field called **Enable Password History**, according to your preference.

![](/docs/assets/drive/s0Xj63FWSlAuip3ZzJB0OWyHiF-cM8zs8EruyfZEM7qA3Pt1hvcNZkRDHWzSb9t3GkzqrqbRwIuP5hghTfyal4441tIbtMQrNyu1CPQmhLOwJkM1EcQ85tEz5TDRbOQazN15k5hzX-b6NyleAak3u1s.png)

When the configuration of the feature **Password Security** is active and the user **changes the password** to a previously used one, Etendo will show an **error message** explaining the failure in saving the password.

![](/docs/assets/drive/x4qql4v3biKPnkWDrD86UUS4mJkw0HuajIK5AmXZKT0OKjP5LdGjzhtd6L8BkkPsR-a9duOtg9uK6OHWjJbig-vSHrltxOd2TfjU5-_lwfH74sKnuekNk4A-heIRIniDxvEb5F45Ms0SxKbRQdy-ztg.png)

The following example shows the same error message when changing the password from the **Change Password** process.

![](/docs/assets/drive/1VTtHPNlLr0N3fvL1vVQ7FO2lzWcQti5I.png)

!!! info
    Etendo also allows entering the same password an indefinite number of times. In case the user wishes to maintain the same password, just keep the field **Enable Password History** from the System Info window **unchecked**. 

### **User Lockout** 

Another feature of this module is the **blocking** of the user after N number of **unsuccessful login attempts**. When entering a wrong password, Etendo shows an error message indicating the number of attempts left.

In this example, the system shows that there is one attempt left.

![](/docs/assets/drive/C-pmD7RKuMzM6e1fSFHSwLWAusC2cL1U9gKlvxWxe7VRa64uuLwaQ7dm4Cmi_Z773XQsfFzfSPrdfMGDNdnNgKPuWobU4xTlxFtOirr34LPiLMT9bI3LONLsmydtloKyd48GYi_1hRnovcHduVsDwGE.png)

Even if in the next attempt the user is not able to log in correctly, Etendo leaves another message indicating that the user has been blocked.

![](/docs/assets/drive/e_vXv3RF7iceBBddpDNUMwewnLYcr5W7LzjhyzrUMPnGe6oT9v9TeXiGc-8MLQpF_Xv1POEZdvMmIRL5bwfai6-hfaEirW4IKlsrBVzcLndzbtRTYeO0_fwou-fTO00rxDtw2lJJi7LY5LoW7vWPEb8.png)

!!! info
    By default, Etendo configures five attempts to enter the right password. 

To configure the number of unsuccessful login attempts, it is necessary to create a preference from the **Preference** window. In the **Value** field, add the desired number of login attempts, and also select the preference **Maximum number of password attempts** from the **Property** field.

![](/docs/assets/drive/5nXDi_OVP9kEESFxQsu1DJywuIEhpJfGl7UvWYPV4UO1CkEhcs2aXMQQIt51lJrww8TfMAUWMfjky2zRtpqhzzdsYygdDt8VhJAe0HNHAWpFbbTbX7c0khUaD9Dn9so89idLPpfmVAqR9bVfS4h4IAU.png)

!!! warning
    It is important to note that once the new password has been entered, if the user enters again a wrong password, the system will automatically block the login at the first try. 

### **Multiple Session Verification**  

Another functional innovation that facilitates this module is the ability to allow or block to have multiple sessions opened from another browser.

From the **User** window, within the **More Information** field, it is possible to configure the check that allows having several sessions active at the same time. The check is called **Allow multiple sessions**.

![](/docs/assets/drive/vcMT58GIgiB2QsZcR-bt5xyajWgf9isk7sxrFJuwkUW27BKnmLIjcb2YZIEJUB-YE-scGv_n3rZ1jTwKGKwLumx4KAIjSp0SsN1jK4saZNChsH8q2JRn5RS3Q6TkXVdVLa1r7C5wXTPmrfVkJyChjRA.png)

In case the user just wants one session allowed to be activated, uncheck the **Allow multiple sessions** checkbox from the **User** window and, **only with System Administrator permissions**, check the **Enable single session verification** field in the **Session Security** field from the **System Info** window.

![](/docs/assets/drive/Prfolo_qyMafrXpr9dUe_ASCkalv-LjArCWEcMCPSWWi2IzyypsQytDTUlSeMgq_mSbgCYKtebK9aawUzMNotE2V25Lg-RrJ2f21l6m75dS4Z11d76gidgZfFrxy1BQgjVl7EvJg2xQISvt1efahvCc.png)

This way, when trying to log in, the system verifies that an active session already exists informing the user.

![](/docs/assets/drive/IkC8pMQVLKRCkr3SI1oYDJsaSirmOHxS31Z5ZmwhCzOnMnwXW88ZFHcyTCnp0Vpm9BxY_RJbpWIdrQG0g5DhURD1RSzW2nexd9hGTeCxTNWhaAWaopvCG-r7JieCNHkLjpCb7HW3v3JXDjofFCHEyAU.png)

!!! info
    By default, Etendo with this module installed, only allows to have one session active. 

### **Changing Password after Login**

After logging in for the **first time** with a user, Etendo asks to **change the password**. When trying to log in, the system mentions that the password has expired and that the user needs to change it to a new one to be able to log in.

![](/docs/assets/drive/aJIN1JP1Oau9HSzi_O2NF-rcQBAdE58v59GVg5NoLiQvgTobqai4mOU07aw0D786KJfL0EBJ_rcaQ86-vf8FmZo3gKZnhLaE_yE3Ynzk46CQkhg0abwcMPLKPw2OjUlvFa75h5zkhSW4i97OviTl8mo.png)

Once the change has been made, the user is redirected to the main interface of the application.

### **Expiration Time (Autolock Password)**

As part of the security management, Etendo also allows the management of the days for the **password expiration time**.

From the **Preferences** window, it is possible to adjust the period of time required for the user to be obliged to change the password. Do it by adding the desired amount of days for the password expiration in the **Value** field.

![](/docs/assets/drive/4o5-tsn6u1mWXedVD-rp5GQNpc6RZ6cAroo-BrZc6xPUevOI0COBerM1NnEmySSSMLMBicOBI1Gidh-4D3QkOMPvJI72977qKSYFHtFJ0UtZnChiIcSYi0Nz3Uu_9H5k39FZ7ozJjeyUbxifnWGamz0.png)

!!! info
    Consider that by default, Etendo configures 30 days for the password expiration time. 

After the number of days established for the password expiration, when trying to log in, a message is displayed explaining the need to be redirected to the **login to change the password**, i.e. the user is marked as **password expired**.

Besides, Etendo notifies the user with a message announcing the amount of **remaining days** for the password expiration. In this example, the user has two days left.

![](/docs/assets/drive/0g12hmyWCTy2ecyVLmptMQSLE6ocCBLGSJLJlYa3EqwCNE-NyYSxy-aO9jg88OWefWDsRso8RDce3Zas0q5Q29fUdcrtSeZ-nA13uwNokmr2vnlKM4HabnGCzy5r3stbAmsCoEgMhzno5T6LLr4tyYM.png)

!!! info
    By default, the system activates this message when there are **seven days** left to change the password.

## **Process Scheduling**

Process Scheduling folder allows the user to schedule and monitor Etendo background processes.

### **Process Request**

#### **Introduction**

A background process is a system action requested by the user, who has to previously provide auxiliary parameter values to execute that action.

There are two background processes which are listed by default in the process request window, those are:

- the _Accounting Server Process_.  
  This process searches for and automatically "Posts" transactions in status "Completed" set as "Posted" = No.
  - Above means that this process allows documents such as purchase invoices, sales invoices or GL journals get automatically posted without any user action but to schedule this process.
- and the Heartbeat Process.  
  This process collects information about Etendo installations, if scheduled.

Besides, there are other background processes which can also be scheduled and therefore monitored:

- the _Costing Background Process_. This process calculates the cost of the material transactions.
- the _Alert Process_. This process checks if the SQL Query defined in each active alert rule returns any record in order to create the corresponding alert instance.  
  This process also removes the _fixed_ alerts instances to ensure they are not shown anymore.
- the _Execute Pending Payments_ process. This process checks and executes Payment In and Payment Out linked to a payment method having an "_Automatic_" _Payment Execution Process_, which are not set as "Deferred" and do not require any input to be executed.
- and the _Payment Monitor_ process. This process checks the invoice's payment status and updates the invoice's "Payment monitor" section.

!!! info
    All the processes above can be scheduled if logged as System Administrator.

#### **Process Request**

Process Request window allows the user to review and add background processes, which can be scheduled or unscheduled as required.

![](/docs/assets/drive/Tjhctxd0gIiAgpntricdUhTGgTKf0FvXQjbYcsgOtJ-9XmH8AYJW2pYsyelS-1LnQv91vGZ2Vf_M_gxJjeQJ5lAZNx9iKTqzdi7QTlb-WbHXAEIcouqQ3Qo5BafXEmMPgIRbdS-J.png)

The information to fill in to schedule a background process is:

- select the _Organization_ for which the background process is going to be scheduled
- select the _Process_ to schedule from the list of processes available
- select the _Timing_. Timing options available are:
  - _Run Immediately_, this one does not require entering any additional parameter values but just to press the action button "Schedule Process".
  - _Run Later_, this one requires entering additional parameter values prior to "Schedule the Process":
    - the Start Date
    - and the Start Time
  - _Schedule_, this one requires to also enter additional information:
    - the Start Date
    - the Start Time
    - the Frequency, options available are options such as "Every n seconds", "Every n minutes", "Hourly", "Daily", etc. Depending on the frequency selected, two new fields are populated to enter:
      - the "Interval in Seconds" and the "Number of Repetitions"
      - the "Interval in Minutes" and the "Number of Repetitions"
      - the "Hourly Interval" and the "Number of Repetitions"
      - the "Daily options" and the "Daily Interval"
      - etc.

!!! info
    Note that "Number of Repetitions" is the number of times the process will be scheduled after its first execution. E.g. A value of 3 means that the process will be scheduled 4 times.

- select the _"Security based on Role"_ checkbox to get that only the user who schedules a process can monitor it in the process monitor window, otherwise any user sharing the same role as the one who scheduled the process will be allowed to monitor it.  
  In both cases, it is required that the role have access to the process in the process access tab of the Role window.
- and, finally, configure by when a process needs to finish. "_Finishes_" field allows entering:
  - a _Finish Date_
  - and a _Finish Time_

Process defined as "Run Immediately" and "Run Later" can either be _Scheduled_ or _Rescheduled_.

Processes defined as "Schedule" can either be _Scheduled_ or _Unscheduled_.

#### **Costing Background Process**

The **Costing Background Process** is the process in charge of searching for goods transactions, such as:

- Goods Receipts
- Goods Shipments
- Physical Inventory
- Goods Movements
- Internal Consumptions
- and Productions

for which its cost has not been calculated yet.

This process considers only transactions having its **"Costing Status"** property as:

- **"Not Calculated"**
- or **"Pending"**.

Costing background process:

- calls the Costing Server process which calculates the cost of each transaction
- and takes into account what configured in the Costing Rule defined for the products, therefore either "Warehouse" dimension is taken into account while calculating the costs, or either "average" or "standard" cost is calculated for the products.

!!! info
    The "Costing Background process" needs to be configured for each Legal entity defined in the client, as this process runs at legal entity (Organization) level.

!!! info
    Note: It is important to remark that if the process is scheduled at (\*) organization level, it will run for all the Legal Entities defined in the Client, therefore it would not be necessary to configure the process more than once.

The transactions are calculated sequentially ordered by the _Transaction Process_ date that is the date and time when the document that originated the transaction was processed.

If the _Costing Server_ throws an error, the background process stops and it is not possible to calculate any new transaction cost until the error is fixed.

The error message can be checked in the Process Monitor window.

!!! info
    Note that although the Costing Background might have failed the process monitor might show a _Success_. Please refer to the _Process Log_ field to get the real result message.

Some costing algorithms such as "FIFO" implement the "Pending" Costing Status as a way to delay the cost calculation of a given transaction/s until the next run.

This way, the costing calculation process is not stopped for the rest of the transactions having a _Not Calculated_ or _Pending_ status, for which it is possible to calculate the cost.

#### **Price Correction Background Process**

Price correction background process searches for Goods Receipts that:

- either have a purchase order related which has been reactivated and booked after completing the Goods Receipts
- or have a purchase invoice related

After that, this process checks and compares whether:

- order purchase price has been changed before booking the invoice
- invoice purchase price is not the same as purchase order price

If the purchase price has changed, a Price Correction cost adjustment is created for the products included in the Goods Receipt(s).

There is a process named "Process Price Different Adjustment" that manually adjusts if required all Goods Receipts already invoiced prior to upgrading Etendo to manage the Cost Adjustments feature.

#### **Process Group**

Process Request has been modified in order to be able to schedule a process group. There is a check Group. Marking the check, a field called Process Group will appear, and you will be able to select a Process Group.

The schedule of a process group will work exactly as the schedule of a single process. It is not possible to schedule a process group and a single process at the same time.

More information in Process Group.

![](/docs/assets/drive/Qq-ABfaxFfvLhrdl-xyZsj0jhuXMJWXDnEdt8B5iYUu7ij_TWKdTUoS29xOSGZNJfpMqB0s_7QVGYI-bBYuZp0G-Hr1yEJkanZEeIAQ7qY07TOXUpsuOGJirzkyfUko2w-mtEPyv.png)

#### **Process Monitor**

Process monitor is a read-only tab that allows reviewing the status of processes executed by this request. More information in Process Monitor.

![](/docs/assets/drive/v8HLIJJYI6RlI8-i5h00aJ5Ynz8NuDcCs6srpwZrZWIpsHKrCJ5NhEHcqwHu85BlXz3enXj9v-XJ00GWsPU0BJ6U4qfPVajQPVcpy6AwTUSjZkN_eY27v_q8kcMzk4u8wcWODAL9.png)

#### **Processes in Group**

In case that the process executed by the process request is a process group, you will find here the information about the executions of the processes in the group for each process group execution. More information in Process Group.

![](/docs/assets/drive/1-YKBRq-gs3FtBuSize6FhzqtgT17IZlE.png)

### **Process Monitor**

#### **Introduction**

Process monitor feature allows reviewing the status of processes executed by a user as well as the ones scheduled in the process request window.

In other words, there are two types of processes which can be monitored in this window:

- _transactional_ processes such as Generate Average Cost or Generate Invoices
- and _background_ processes scheduled in the process request

In any case, only the users having a role which have access to a given process/processes will be able to monitor it/them in this window.

Besides, and as already explained, _"Security based on role"_ definition at process request level will allow defining the users which will be able to monitor a given background process in this window.

#### **Process Execution**

Process Monitor window shows read-only information about individual process execution.

![](/docs/assets/drive/1n5-1WsQVWLDXUzuynPBRi1mruhlS9uPb.png)

As shown in the image above, process monitor window provides the information below per each process executed:

- the _Name_
- the _User_ who run the process
- the _Start and End time_
- the _Duration_
- the _Status_
- and the _Channel_. The options available are:
  - _Direct_ for transactional process executed manually by the user
  - Process Scheduler for background processes scheduled in the Process Request window.

#### **Processes in Group**

In case the process executed is a process group, you will find here the information about the executions of the processes in the group. More information in Process Group

![](/docs/assets/drive/1-YKBRq-gs3FtBuSize6FhzqtgT17IZlE.png)

### **Process Group**

#### **Introduction**

Create a Process Group to be able to schedule and execute a group of processes as a single unit from the Process Scheduler. The batch of processes will be executed in series.

The purpose of this functionality is being able to schedule and execute a group of processes as a single unit from the Process Scheduler.

- The Process Group creates an entry in the Process Request Window and Process Monitor window.
- Each individual process executed in a Progress Group is broken out as a separate entry in the Process Request Window and Process Monitor window.
- Each individual process is listed in the Process Monitor window, regardless if it ran successfully or with error.
- The log for each is listed in its own entry.

#### **Process Group**

It creates a Process Group to be able to schedule and execute a group of processes as a single unit from the Process Scheduler. The batch of processes will be executed in series.

A Process Group is a set of processes sorted in a certain sequence.

Process Group (Header): Contains information about the process group.

**Process Group Options**

There are two options that can be selected defining a Process Group

![](/docs/assets/drive/E2KNZetYy11WqMd1jRFYVQsjkQodMAYF63N2y2wYFfkZu8ooMYqJUfvnTdOh0iQu1Gp2NJtbEWCqQFBQGrqnHUTbyLTrdxCY-OUrnYhC997G7hOFYRvo-5ZOsjMWbhwg-PLQLJk5.png)

##### **Prevent Concurrent Execution of a Process Group**

As the Prevent Concurrent Executions of a single process, mark the Prevent Concurrent Executions checkbox in a Process Group means that just before launch an execution of a Process Group the system will check if there is another instance of the same Process Group running (for the same Client and same Organization). If there is, the system will abort the execution and will show an error message in the log: _Concurrent attempt to execute._

##### **Stop the group execution when a process fails**

By default, if a process that is part of a Process Group fails, the following processes will be executed.

Marking this check-box "Stop the group execution when a process fails" the execution of following processes will be aborted in case of a process failure.

This option is useful if the processes are dependent between them.

#### **Process Group List**

It creates a Process inside a Process Group with a sequence number.

Process Group List contains the list of processes that are part of the group, sorted in a certain order.

![](/docs/assets/drive/APyS4fin8Sb72dYf0TP1ZvLLpkZbsyrQ1Tv8_ABv1Byjurr0B1v8PanDaEytiR0NIhAS_TIbnsTe0aR5xQVNDybH_CicNv-TiGPgHq3deGKEyT8NuL3sPvf0J88asLgU9WWOtrMd.png)

#### **Other Considerations**

#### **Error Result**

A process group will show an Error result if it has one or more Error results in the processes that conform the group.

#### **Permissions**

Process Group is a window, so you can manage permissions for creation of Process Group as you wish: Only System, some clients, some organizations, some roles, etc...

#### **Empty Groups**

You can not launch executions of empty groups. If you try, you will receive this error: No processes on the group: nameOfTheGroup.

#### **Prevent Concurrent Execution Co-Exists**

Prevent executions of single processes and group processes will co-exist. Which means that none of them overrides the other and both can be set at the same time.

#### **Process Group as Source Data**

!!! info
    Only for developers

Process Group can be considered as Source Data which means that, working as System Administrator, you can assign a "Group Process" and/or a "Group Process List" to your module in order to distribute them as part of your module.

![](/docs/assets/drive/fSrbl6KIduQt_nL4aZ2wOWGWgcd8H03rnndIVD5YhTx0J1bkdD-m5K57TXKQOuPDm8QtsLi4V_egrxJvgdOWEsV7TPykZRBr_1McjEMny9HXf9kowbFRXFhqcZm9MRhJ0PvT4xoJ.png)
