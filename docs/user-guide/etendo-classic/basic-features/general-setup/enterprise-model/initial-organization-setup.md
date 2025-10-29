---
title: Initial Organization Setup
tags:
    - Organization
    - Setup
    - Client
    - Enterprise
    - Model
---

# Initial Organization Setup

:material-menu: `Application` > `General Setup` > `Enterprise Model` > `Initial Organization Setup`

## Overview

An **Organization** is an enterprise of a Client. A client can have at least one or even more than one organization as the way of configuring different types of enterprise models.

Overall organizations can be:

- independent legal entities with a different Tax ID number
- enterprise groups with the aim of getting aggregated figures for the group
- or business areas of the client such as departments

Besides, organizations can be structured:

- by **country or region**
- by **area or function**
- and so on, according to the enterprise model needs.

All of the above provides an insight about the different scenarios which need to be covered while modeling the enterprise.

- There could be organizations which require to share master data such as business partners and products while having its own chart of account, taxes, financial reporting and transactional data. That could be the case of independent legal entities belonging to the same enterprise group.

- There could be organizations sharing master data and even the same chart of accounts. That could be the case of divisions or departments within the same independent legal entity.

- There could be organizations created with the aim of just grouping data, for which its own transactional data is not required.

All of the above is possible due to the fact that there are different [types of Organizations](../enterprise-model/organization-type.md) and besides organizations can be structured in a hierarchical way:

- At the highest level of the tree, there is an organization named (\*).
    - (\*) organization is created at the same time that the _system client_ is created, and it is shared among the different _client/s_ in the system.
    - Master data created at (\*) organization level is accessible for all the organization beneath it
    - (\*) organization is not an independent legal entity, therefore transactional data is not allowed.
    - Every organization created later on will be created below (\*) organization.
- At a lower level of the tree, there can be parent organization/s which can have child organization/s beneath it/them.
    - Master data such as business partners and products created at parent organization level is accessible for all the child organization/s beneath it.
- At the lowest level of the tree, there can be child organization/s with no organizations beneath it/them.
    - Master data such as business partners and products created at child organization level will not be accessible for the rest of the child organizations, if any.

## Initial Organization Setup

As already mentioned, Organizations are created by running the Initial Organization Setup process and not only that, once an organization has been created it must be set as **Ready** in the Organization window.

![](../../../../../assets/drive/jaLNPOFQoCLMgujXvhC3sL--3PKbCLcfdvQubK5VvyRy85PwL7t_4V38fCTBCmrioEfhBQKvWWVq87sbLZsuP9D-YMUodiBeLsQrhbY-cnruPAjkkigHou5kknI1D0ZYc4-G0RiB.png)

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
        - And there could be as many organizations type **organization** in a branch as required.
    - Legal with accounting - an independent legal entity with a unique Tax ID number which requires accounting, therefore:
        - This organization requires a General Ledger and therefore an Account Tree or Chart of Accounts, as well as a Fiscal Calendar because the accounting periods can and must be opened and closed at its level.
        - This organization type allows the **consolidation** of the Balance Sheet and P&L reports only for the Chart of Accounts it has assigned.
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
- the parent organization. While creating an organization, it is possible to select the organization to which the organization being created will belong to. The parent organization would need to be set as **Summary**.
    - A generic organization can not be the parent organization of a legal entity organization, but the other way around.
- the organization location/address
- and the organization currency

Besides:

- There is a checkbox named **Include Accounting** which allows the user to select for an organization:
    - an accounting CSV file in the field **Accounting File**
    - or a Chart of Accounts module reference data in the section **Reference Data**. Reference data coming from extensions modules is master data such as Taxes, Chart of Accounts, etc to be applied from the already installed modules.

This action creates:

- a General Ledger configuration which is automatically linked to the Organization being created
- and an Account Tree or Chart of Accounts which is also linked to the Organization being created

This step does not create a Fiscal Calendar as the [Initial Client Setup](../../../../../developer-guide/etendo-classic/how-to-guides/how-to-run-an-initial-client-setup-process.md) process does, because Fiscal Calendars need to be created ad hoc for the **Legal with Accounting** Organizations for which **Allow Period Control** feature is going to be enabled.

!!! note
    This step does not imply to manage accounting within an organization, but just to include an accounting file or an accounting reference data in an organization.

Accounting management relies on the organization type being created.

It is not mandatory to select **Include Accounting** checkbox while creating a legal entity with accounting organization for instance because:

- a legal entity with accounting can inherit the client chart of accounts
- or, later, both the Chart of Accounts and the General Ledger configuration can be created manually and be linked to the organization.
- if the checkbox **Include Accounting** is selected, it is possible to select for the organization being created below dimensions to be used while posting the organization's documents to the ledger:
    - Mandatory accounting dimensions such as Business Partner and Product and not mandatory accounting dimensions such as Project and Sales Region while creating an Organization in a Client which does not centrally maintain the accounting dimensions.  
    In that case, the dimensions selected in here will all be listed in the dimensions tab of the organization's general ledger configuration, therefore will be available just for that organization.
    - Additional accounting dimensions such as Project or Campaign while creating an Organization in a Client which centrally maintains the accounting dimensions.  
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

## Examples

1. **Etendo Demo Data**:

    Etendo includes demo data for demonstration purposes, which includes an Enterprise Model composed by a set of organizations.

    ![](../../../../../assets/drive/Vuf4G00AIK2uWFXjxHE733lf2QkM1WNhX1Eh29LCef9KNoZMGGnkD0O1vnkML26wZ7V_PHQHSgKtBgTxaB5Y3od9pFqzriF1nCYm7ysoMCJKrPf9-6jKp017i2QCIHKCBbV82bZn.png)

    - An organization type **Organization** named F&B International Group.
        - This organization is not a legal entity and it does not allow transactions
        - This organization allows the creation and configuration of master data to be shared among a group of organizations beneath it.
    - Two **legal entities with accounting** named *F&B España* and *F&B US* that belong to F&B International Group.
    - Below the legal entities with accounting organizations there are four **Generic** organizations, which are not legal entities but belong to a legal entity and besides allow transactional data entry:
        - F&B US West Coast
        - F&B US East Coast
        - F&B España - Region Norte
        - F&B España - Region Sur

2. **How to create each Organization type**:

    The basic variables to take into account while creating an organization of the type **Organization** are:

    - Organization Type = Organization
    - Include Accounting = Yes  
        If the accounting configuration at this level needs to be shared by all the organizations underneath the one being created.
    - Accounting Dimensions = Business Partner, Product and Project

    The basic variables to take into account while creating an organization of the type **Legal with accounting** are:

    - Organization Type = Legal with accounting
    - Include Accounting = Yes
    - Accounting Dimensions = Business Partner, Product and Project

    The basic variables to take into account while creating an organization of the type **Legal without accounting** are:

    - Organization Type = Legal without accounting
    - Include Accounting = No

    The basic variables to take into account while creating an organization of the type **Generic** are:

    - Organization Type = Generic
    - Include Accounting = Yes  
        If this organization requires its own accounting configuration besides the inherited one, otherwise include accounting = No
    - Parent organization = should be a **Legal with Accounting** organization.

3. **Enterprise Models examples**:

    ![](../../../../../assets/drive/h9cS1Sgl07mpOdqMyrCNa-D3w4typy34vJcGl9wb5xk8vnpOkO4dPBwmBwY1JygGfPEeaQvh7katpn2-_fdTLWn5FyeIEPwZcNdkhkkKn0FUjTCTRLUosk2YcYwMoBegzLlVMzmCFCRzQztOKA.png)

    ![](../../../../../assets/drive/0mFr7Nl9jVy9ZVIfNVOl8pKVHpLv2h6waw6r0iGBnpjTs8A0P4wYIWAHFbYJKGrduahpu1QbmH4UXDq9n27_ffdvfgAcd8_plxvBEXx8cY7j7eWRjIvLBtByLU0-9Zw1iKsVttxtv3ecG9oNZA.png)

    ![](../../../../../assets/drive/2IIoZGBxPH1gigLWVMWKxE0GxWoAtAFJX2yheNUuOYoy_orJdRJII2rVZUpGcA8j4aJavDIoRIi1WJDymLDxqAbg-r-u6z4E91SRafrj9bX-EK4M8nhpqUqM1ufnYsgBc51D3HXAxZDPuy7R5A.png)

---

This work is a derivative of [General Setup](https://wiki.openbravo.com/wiki/General_Setup){target="_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="_blank"} by [Etendo](https://etendo.software){target="_blank"}.