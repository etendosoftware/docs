---
tags: 
 - getting started
 - installations
 - client
 - organization
 - setup
---

![cover-getting-started.png](/assets/getting-started/overview/cover-getting-started.png)
#

## Overview

This section describes the steps that need to be performed first to configure Etendo.
Etendo installations require at least a [Client](/user-guide/etendo-classic/basic-features/general-setup/client/) and an [Organization](/user-guide/etendo-classic/basic-features/general-setup/enterprise-model/#organization). Client and Organization are the two key concepts within the General Setup.

In other words, it is not possible to issue an invoice or to post a journal entry to the ledger in Etendo if there is no Client and Organization properly created and configured.

The first steps to follow to configure Etendo are:

#### Installation of the Localization Bundle if available for the country

!!!info
    Read the [Install Modules](/developer-guide/etendo-classic/getting-started/installation/install-modules-in-etendo/) documentation to install the Localization bundle. 

This can be considered the first basic step while setting Etendo instances as it is required to install first the localization bundle if any, in order to apply the accounting reference data or Chart of Accounts while creating either the Client or the Organization later on.

A Localization Bundle can include at least:

- the complete **translation** for the official language(s) in the country.
The language is automatically available once the localization bundle has been successfully installed, therefore it can be selected as described at [profile](/getting-started/user-interface/workspace#profile).

- the **chart of accounts** that defines the accounting structure if any to comply with the approved local practice and laws.
The Chart of Accounts is available for selection just while running either the Initial Client Setup or the Initial Organization Setup.

- and the setup of the **taxes** which comply with the in-country tax authorities requirements.
The setup of the taxes is also available for selection while running either the [Initial Client setup](/user-guide/etendo-classic/basic-features/general-setup/initial-client-setup/) or the [Initial Organization setup](/user-guide/etendo-classic/basic-features/general-setup/enterprise-model/#initial-organization-setup), and even in the Enterprise Module Management window.

#### Initial Client Setup

A [Client](/user-guide/etendo-classic/basic-features/general-setup/client/) in Etendo is the top-most level of configuration and data within Etendo.

Above means that certain configurations such as users, customers, vendors and other [master data](/user-guide/etendo-classic/basic-features/master-data-management/master-data) can be managed in a client and therefore be available across all the organizations within the client.

!!! info
    Each client can host at least one or even more than one organization that can be used to model your enterprise.

The [Initial Client setup](/user-guide/etendo-classic/basic-features/general-setup/initial-client-setup/) is the process which creates a Client in Etendo. A Client cannot be created manually.

This process besides creating a Client allows selecting the reference data included in the bundle/s already installed.
All that data, if applied to the Client, will be shared by all the organizations which belong to the Client.

!!! info
    There is a System Client which is automatically created by Etendo as part of the Etendo installation process.
    This client handles application data such as tables, columns and fields and it also manages some data which can be shared across all the Clients such as currencies, countries and regions and units of measure.

#### Initial Organization setup

An **Organization** is the second level of configuration and data.

Organizations can be structured in a hierarchical way within a Client providing multiple options while modeling your enterprise.

There are different types of Organizations which can either be independent legal entities or not.
Legal entities can either require accounting or not and Not Legal Entities can either allow transactional data or not.

The [Initial Organization setup](/user-guide/etendo-classic/basic-features/general-setup/enterprise-model/#initial-organization-setup) is the **process** which creates Organizations in Etendo.

!!! info
    An Organization can be created once the Client it belongs to has been created.

An Organization cannot be created manually.

Same way, this process besides creating an Organization allows selecting the reference data included in the bundle/s already installed.

This time the data, if applied to the Organization, will be available just for the Organization being created.

!!! info
    There is an Organization named (\*) which is automatically created at the same time that the System Client is created. Every organization created later on will hierarchically be located below it.

#### Users and Roles setup

Etendo security can be split into Functional and Data security.
**Functional** security manage the access rights to Etendo entities such as Windows and Processes by properly setting up [users](/user-guide/etendo-classic/basic-features/general-setup/security#user) and [roles](/user-guide/etendo-classic/basic-features/general-setup/security#role):

A **User** is an entity which can log into Etendo whenever it has a password and at least one role assigned.
Each person accessing Etendo should have a different user assigned properly configured.

A **Role** is the connection between users and access rights to Organizations, Windows, Processes and Forms in Etendo.
Access rights are first configured at role level, roles are then assigned to the user/s.

Etendo creates two users by default, the System user and the Admin user:

- the **System** user is the owner of Etendo application data. It is not possible to log into Etendo as System user.
- the **Admin** user is a **super** user which has access to any Etendo Client.

The password assigned to this user is Etendo, however it can be changed if needed in the [user](/user-guide/etendo-classic/basic-features/general-setup/security#user) window.

This user is assigned to the System Administrator Role, a role with no access restrictions.
**Data security** is an advance setting as it manages the access rights to subsets of data within Etendo entities such as Windows and Processes, by properly setting up the [Data Access Level](/user-guide/etendo-classic/basic-features/general-setup/security#role-access) at table level and the [role](/user-guide/etendo-classic/basic-features/general-setup/security#role):

!!! info
    Data Access level defines the client and/or the organization each record is going to be visible from.

Every [table](/user-guide/etendo-classic/basic-features/general-setup/security#role-access) in Etendo has a Data Access Level column.

User Access Level allows limiting the records which will be accessible in entities such as Windows, Processes, Forms, Widget Classes and Views for a [role](/user-guide/etendo-classic/basic-features/general-setup/security#role), or even limit the access to a given entity.

### Basic Setup Diagram

The diagram below shows the Etendo basic General Setup flow for a legal entity with accounting. This flow is one part of the overall Business setup flow.

![](/assets/user-guide/etendo-classic/basic-features/general-setup/getting-started/basic-general-setup.png)

In the example above, the **Accounting** data can not be shared across all the organization/s of the client because it was not applied at client level but to the Organization being created.

This setup would fit in the case of a Client which has **one or more independent legal entities with accounting underneath**, same as the sample client shipped with Etendo by default (F&B sample client).

There is a close relationship between the general setup which allows the creation and configuration of an enterprise, and the accounting configuration area because to set a Legal with Accounting Organization as ready, it requires below accounting items to be properly created and configured first:

1. a [Fiscal Calendar](/user-guide/etendo-classic/basic-features/financial-management/accounting/setup#fiscal-calendar)

2. and an organization's [General Ledger configuration](/user-guide/etendo-classic/basic-features/financial-management/accounting/setup#general-ledger-configuration) which includes a dimension that is the [Account Tree](/user-guide/etendo-classic/basic-features/financial-management/accounting/setup/#account-tree) or Chart of Accounts.

!!! info
    The Fiscal Calendar, once manually created, can be available to all the organizations within the client if it is created for the (\* (asterisk)) organization.

A defaulted **General Ledger configuration** and the **Chart of Accounts** can be automatically created if an **Accounting** reference data such as a **Localization Bundle** containing a Chart of Accounts module is installed and applied to the Organization. Moreover, in case there is no Localization Bundle for your country, Etendo delivers a Generic Chart of Accounts module which, if installed and applied, creates a sample Chart of Accounts and a defaulted General Ledger configuration which can be later on customized to meet the needs of your organization.

## Business setup diagram

The diagram below shows the business setup flow.
This business setup flow goes from the Generic setup and Master Data areas to the Accounting and Warehouse setup areas.

![](/assets/user-guide/etendo-classic/basic-features/general-setup/getting-started/Quick_Guide_Diagram_new.png)

If you want to know more about the basic setup of the business configurations in Etendo, please review the different articles in the General Setup section.

By following this setup flow you should be able to have your own version of Etendo ready to execute the basic Business Flows.