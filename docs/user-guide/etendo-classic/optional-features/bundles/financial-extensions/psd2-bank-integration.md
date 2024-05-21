---
tags: 
    - Bank transaction
    - Token
    - PSD2
    - OAuth Authentication
    - Account ID
---

# PSD2 Bank Integration

## Overview

This section describes an enhancement of the **Financial Extensions Bundle** in Etendo which uses the **PSD2 (Payment Services Directive 2) feature**. This functionality allows users to securely connect to their bank, synchronize their bank accounts with financial accounts in Etendo, create transactions within specified date ranges and automatically download bank transactions. 

This section serves as a guide for users to understand the functionality and usage of the PSD2 module.

## Connect to the Bank

In the Financial Account window, Etendo shows every account’s imported bank statement with its corresponding bank statement details listed in the **Bank Statement Lines tab**. Through this module, it is possible to directly connect to the bank through the IBAN (International Bank Account Number) and link it with the bank’s internal ID to automatically create and generate the bank statements. 


![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/psd2-bank-integration-0.png)

For this, users must provide necessary **authentication credentials** to connect their bank accounts with Etendo, this allows automating the process of updating financial records with bank account information in order to be able to download the bank transactions needed. 

## Configuration
### OAuth Authentication

Before continuing with the process from the Financial Account window, it is necessary to configure the imported bank statement type provider which is **fundamental to use this functionality**. The configuration process is set up through OAuth in the **OAuth Provider window** in `application`> `oauth-provider`. OAuth facilitates an authentication method through a security protocol for obtaining a token needed to give consent to the bank. This authentication will allow Etendo to get the necessary bank information to access the bank statements.

!!!note
        Even though this module provides generic information about different banks, information about the endpoint must be manually included.


!!! info
        Continue with the setup process in the [OAuth Authentication section](../platform-extensions/oauth-authentication.md) which is part of the [Platform Extensions Bundle](../platform-extensions/overview.md).  
 

## Get token

Once the imported bank statement type provider is configured through the OAuth Authentication method, the following steps are needed to get to download the bank statements: 

From the Financial Account window, the **Get Token button** allows logging into the bank interface, as Etendo will move towards token-based authentication. In the pop-up window, log in to the configured provider by using the **bank’s user and password**, generate the token, and Etendo will use the token generated to get the information needed from the bank. 

![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/psd2-bank-integration-1.png)


!!! info
    The token generated can be seen by going back to the **OAuth Provider window** and seeing that for our user there is a token generated (the user with which the logged in process occurred).

![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/psd2-bank-integration-2.png)


## Get consent

For Etendo to be able to use the token generated, it is necessary to click on the **Get Consent button** in order for the user to authorize Etendo to access the bank information through the token generated.

![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/psd2-bank-integration-3.png)

!!!note
        This step is obligatory since for the consent to be approved, the confirmation must be given.  

!!!info
        The state of the consent (approved or not approved) can be checked in the **OAuth Provider configuration window**. 

## Account Synchronization

The following step is to synchronize the accounts. For this, go to the **Get Bank Account Identifiers** window in `general-setup`> `integrations-configuration` >`psd2`>`get-bank-account-identifiers` and select the bank provider to synchronize the accounts with. This brings the bank accounts synchronized with the chosen provider and starts synchronizing the account IDs. 

![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/psd2-bank-integration-4.png)

Once the process is finished, the synchronization can be checked in the **Bank Integration PSD2** information section from the Financial Account window. The ID obtained is the identifier to be used to request the bank statements. 

![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/psd2-bank-integration-5.png)

## Get bank statements

In the **PSD2 Bank Integration section of the header**, it is also possible to define the import date of the bank statements and the frequency run, e.i., how often the user wants a record to be created: 

- **Import from Date**: Etendo brings bank statement information from the last date when a bank statement was created (when a bank statement was imported). 

- **Import to Date**: if the field remains empty, Etendo brings the information to the current day's date.

!!!info
        In case any of the fields **Import from Date and Import to Date** remain empty, Etendo brings the bank statement information to the current day’s date. 

- **Statement Frequency**: 

    - One per day: if there is already a statement created for that day,  Etendo uses the same statement and includes the information there.
    - One per month: Etendo checks the last statement created within the given month and if there is one created, it enters the statement there. Otherwise, Etendo creates a new one. 
    - One per run: Etendo creates a new statement.
    - One per week: Etendo checks if the last statement created is within the given week.

![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/psd2-bank-integration-6.png)

After defining the requirements for the bank statement creation, complete the process by clicking on the **Get Bank Statement button**. Etendo creates a header record, whose names are related to the dates, and the bank statements lines provide a transaction reference number. 

Etendo processes the bank statements which are ready to be reconciled. 

![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/psd2-bank-integration-7.png)

