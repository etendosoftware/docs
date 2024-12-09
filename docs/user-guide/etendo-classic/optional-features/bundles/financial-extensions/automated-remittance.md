---
tags:
- automated
- remittance
- accounting
- financial
- extensions
- bundle
---

# Automated Remittance

:octicons-package-16: Javapackage: `com.etendoerp.automated.remittance` 

## Overview

This section describes the Automated Remittance module included in the Etendo Financial Extensions bundle.

!!! info
    To be able to include this functionality, the Financial Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}.


This functionality allows the user to automatically process and protest remittances. To better understand this section, it is necessary to visit the [Remittance user guide](../../../basic-features/financial-management/receivables-and-payables/transactions.md#remittance).

!!!important
    Remember this functionality is available from 3.15.0 version of the `org.openbravo.module.remittance` module.

## Setup

To be able to use this functionality, it is necessary to install the Automated Remittance dataset before using the Remittance window.

For this, go to the [Enterprise Module Management](../../../../../user-guide/etendo-classic/basic-features/general-setup/enterprise-model.md#enterprise-module-management) window and select the corresponding dataset as shown below. This includes the necessary payment method to be used in the protest functionality, explained below.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/automated-protest-remittance/Enterprise%20Module%20Management.png)

## Automated Remittance Process

This functionality allows the automatic processing of remittances. This functionality is activated by selecting the Process Automated checkbox in the header of the [Remittance](../../../basic-features/financial-management/receivables-and-payables/transactions.md#remittance) window.


1. Activation: To activate the automated processing, the Process Automated checkbox in the Remittance header is selected by default. This selection is included once the module is installed. If the manual processing is preferred, the user can uncheck this option.

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/automated-protest-remittance/process-automated-check.png)

    Once the Process button is used, Etendo automatically creates the corresponding lines in the Bank Instructions and Settled tabs, as explained below.

2. Generation of Bank Instructions: When this option is activated, the system will automatically generate the corresponding Bank Instructions.

3. Future Date Processing: Remittance lines will be processed with a specified date, automating the entire workflow. This lines can be found in the Settled tab.

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/automated-protest-remittance/remittance.png)

!!!note
    The invoice selection, grouping and processing steps already existed; what's new is the automation of the remittance processing by selecting the Process Automated checkbox.

## Automated Remittance Protest

The Protest Remittance button allows the automatic protest of remittances. This function facilitates the management of protests and the re-settlement of remittances.

1. Remittance Selection: In the Settled tab, of the Remittance window, select the remittance to be protested.

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/automated-protest-remittance/remittance-selection.png)

2. Return Generation: By pressing the Protest Remittance button and selecting a return date, the system will automatically generate the return of the remittance.

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/automated-protest-remittance/protest-generation.png)

3. Negative Invoice Payment: The return will include the generation of a negative payment of the invoice to be returned, allowing the remittance to be settled again in the future.

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/automated-protest-remittance/negative-invoice-payment.png)

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/automated-protest-remittance/negative.png)