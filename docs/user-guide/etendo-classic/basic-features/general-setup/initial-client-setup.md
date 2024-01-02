---
title: General Setup
---


## Overview

The Initial Client setup process allows to create a Client and besides a Client Admin role with no access restrictions.

The initial client setup process is an automated process which can be run by logging in Etendo as System Administrator role.

This process allows to:

- enter the **name of the client** and the **client admin user name** and a **password**
- enter the **base currency** of the client, that is going to be the currency of the Client regardless an Organization which belongs to it might have a different currency.
- include **Accounting** for the client.
There is a checkbox named *Include Accounting* which allows to select an accounting csv file in the field *Accounting File* or an accounting reference data within the section Reference Data.

Etendo distributes accounting csv file as modules which can be applied as reference data. This kind of modules are part of the Etendo localization for a given country.
If the checkbox *Include Accounting* is selected and an accounting file or reference data is selected, Etendo creates:

   - a [Fiscal Calendar](/user-guide/etendo-classic/basic-features/financial-management/accounting/setup/#fiscal-calendar) which can be shared by all the Legal with Accounting organizations types which belongs to that [Client](/user-guide/etendo-classic/basic-features/general-setup/client/)
   - and an Account Tree or Chart of Accounts and a General Ledger configuration which is shared by all the organizations created within the Client.

The General Ledger Configuration and the Chart of Accounts created by default can be later on customized as explained in the Setup Accounting article of the [Getting Started](/getting-started/overview/).

The General Ledger Configuration is linked to the Account Tree as the Account is a mandatory [dimension](/user-guide/etendo-classic/basic-features/financial-management/accounting/setup/#dimension) of the general ledger configuration.

!!!info
    It is possible to create a client without selecting the Include Accounting checkbox, in fact that is the recommended option. Accounting configuration will then rely on the organization type being created later on in the Client.

!!!info
    Read the [Initial Organization setup](/user-guide/etendo-classic/basic-features/general-setup/enterprise-model/#initial-organization-setup) documetation for more information.

- finally it is possible to apply reference data such as:

   - **Standard document types for orders, invoices, etc**, this one is selected by default as it is necessary for creating transactional data such as orders and invoices.
   - **Document types and default algorithm for bank statements auto-matching**, this one is similar to the previous one but for specific financial flows such as [Payment Outs](/user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions/#payment-out), [Payment In](/user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions/#payment-in) and [Financial Accounts](/user-guide/etendo-classic/basic-features/financial-management/receivables-and-payables/transactions/#financial-account).
   - or reference data such as master data or configuration data (i.e. tax setup) created for Etendo extension bundles.

   Every new Client created in Etendo centrally maintains at least the mandatory accounting dimensions listed below:

- Organization
- Business Partner
- and Product

unless the *Central Maintenance* checkbox is unselected for the Client which would imply the configuration and management of all the accounting dimensions (mandatory and not mandatory) at organization level.