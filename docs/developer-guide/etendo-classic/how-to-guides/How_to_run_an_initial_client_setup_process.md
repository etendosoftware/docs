---
tags: 
  - configuration
  - setup process
  - client
  - organization
  - System Administrator
---

#  How to run an initial client setup process

## Overview

The Initial Client setup process allows to create a Client and also a *Client Admin* role with no access restrictions.

The initial client setup process is an automated process which can be run by logging in Etendo as *System Administrator* role.


This process allows to:

- Enter the name of the client and the client admin user name and a password.
- Enter the base currency of the client, that is going to be the currency of the Client regardless of if an Organization which belongs to it might have a different currency.
- Include Accounting for the client.

!!!info
    There is a checkbox named *Include Accounting* which allows to select an accounting csv file in the field *Accounting File* or an accounting reference data within the section *Reference Data*.

!!!info
    Etendo distributes accounting csv file as modules which can be applied as reference data. This kind of modules are part of the Etendo localization for a given country.

If the checkbox *Include Accounting* is selected and an accounting file or reference data is selected, Etendo creates:

  - a [Fiscal Calendar](../../../basic-features/financial-management/accounting/setup/#fiscal-calendar.md) which can be shared by all the *Legal with Accounting* organizations types which belongs to that Client and 
  - an [Account Tree](../../../basic-features/financial-management/accounting/setup/#account-tree.md) or *Chart of Accounts* and a [General Ledger configuration](../../../basic-features/financial-management/accounting/setup/#glconfig.md) which is shared by all the organizations created within the Client.

The *General Ledger Configuration* and the *Chart of Accounts* created by default can be later on customized. 

!!!info
    For more information, read [General Setup](../../../basic-features/general-setup/getting-started/.md). 


The *General Ledger Configuration* is linked to the *Account Tree* as the *Account* is a mandatory [dimension](../../../basic-features/financial-management/accounting/setup/#dimension.md) of the general ledger configuration.

!!!note
    It is possible to create a client without selecting the *Include Accounting* checkbox, in fact that is the recommended option. Accounting configuration will then rely on the organization type being created later on in the Client.

!!!info
    For more information, read [Initial Organization Setup](../../../basic-features/general-setup/enterprise-model/#initial-organization-setup.md).

- Finally, it is possible to apply reference data such as:

  - Standard document types for orders, invoices, etc, this one is selected by default as it is necessary for creating transactional data such as orders and invoices.
  - Document types and default algorithm for bank statements auto-matching, this one is similar to the previous one but for specific financial flows such as [Payment Outs](../../../basic-features/financial-management/receivables-and-payables/transactions/#payment-out.md), [Payment In](../../../etendo-classic/basic-features/financial-management/receivables-and-payables/transactions/#payment-in.md) and [Financial Accounts](../../../basic-features/financial-management/receivables-and-payables/transactions/#financial-account.md).
  - or reference data such as master data or configuration data (i.e. tax setup) created for Etendo extension modules.

Every new [Client](../../../basic-features/general-setup/client/.md) created in Etendo centrally maintains at least the mandatory accounting dimensions listed below:

- Organization
- Business Partner
- and Product

unless the *Central Maintenance* checkbox is unselected for the Client which would imply the configuration and management of all the accounting dimensions (mandatory and not mandatory) at organization level.


This work is a derivative of [Initial Client Setup](https://wiki.openbravo.com/wiki/Initial_Client_Setup){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
