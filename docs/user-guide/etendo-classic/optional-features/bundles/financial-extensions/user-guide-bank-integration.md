---
tags: 
    - Bank Transaction
    - Salt Edge
    - Bank Integration
    - Bank Statements
    - Open Banking
---

# Bank Integration with Salt Edge

:octicons-package-16: Javapackage: `com.etendoerp.psd2.bank.integration`

## Overview

This module provides **automatic bank integration** functionality for Etendo ERP, allowing users to securely connect their bank accounts and automatically download bank transactions. The integration is powered by **Salt Edge**, a leading Open Banking platform that provides secure access to thousands of banks worldwide.

### What is Salt Edge?

[Salt Edge](https://www.saltedge.com/){target="_blank"} is an Open Banking platform that acts as a secure intermediary between Etendo ERP and banking institutions. Salt Edge:

- **Supports thousands of banks** across multiple countries
- **Handles all authentication** and security requirements with each bank
- **Complies with PSD2** and Open Banking regulations
- **Provides a unified interface** regardless of the bank being used

### How Does It Work?

The integration uses a **centralized middleware** developed by Etendo that serves as an intermediary layer between Etendo ERP and Salt Edge. This architecture provides:

- **Simplified integration**: Etendo ERP doesn't need to handle the technical complexity of Open Banking
- **Enhanced security**: The middleware manages all authentication and encryption
- **Scalability**: Multiple Etendo instances can use the same middleware
- **Maintainability**: Updates to banking APIs are handled at the middleware level

### Key Benefits

- **Automated transaction import**: No need to manually upload bank statement files
- **Real-time synchronization**: Get the latest transactions directly from your bank
- **Multiple bank support**: Connect accounts from different banks simultaneously
- **Secure authentication**: Bank credentials are never stored in Etendo
- **Duplicate prevention**: Automatically filters out duplicate transactions
- **Audit trail**: Complete log of all synchronization operations

!!!info
    To be able to include this functionality, the **Financial Extensions Bundle** must be installed. To do that, follow the instructions from the marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. For more information about the available versions, core compatibility and new features, visit [Financial Extensions - Release notes](https://docs.etendo.software/whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes/).

## Prerequisites

Before using the Bank Integration functionality, ensure that:

1. **Salt Edge API Key**: Your organization must have a Salt Edge API Key. This key is provided by **Futit Services** and is required to access the integration middleware.

2. **User Configuration**: The API Key must be configured in your Etendo user profile (detailed in the setup section below).

3. **Financial Accounts**: You must have Financial Accounts created in Etendo that will be linked to your bank accounts.

!!!warning
    The Salt Edge API Key is provided by Futit Services as part of the integration service. Contact your Etendo administrator or Futit Services support to obtain your API Key.

## Setup

### Step 1: Configure Salt Edge API Key

:material-menu: `Application` > `General Setup` > `Security` > `User`

As an **Administrator** or user with appropriate permissions:

1. Navigate to the **User** window
2. Select your user record
3. In the **PSD2 Bank Integration** tab or section,**API Key** field, enter the API Key provided by Futit Services

![User API Key Configuration](#)

!!!info
    Each user who will perform bank synchronization must have their own API Key configured. The API Key is user-specific and should be kept confidential.

### Step 2: Configure Financial Accounts

:material-menu: `Financial Management` > `Receivables and Payables` > `Transactions` > `Financial Account`

For each financial account you want to synchronize with a bank:

#### 2.1 Set Import Date Range

In the **PSD2 Bank Integration** tab or section of the Financial Account:

- **Import From Date**: Specifies the starting date for importing transactions. 
    - If left empty, the system will use the date of the last imported bank statement
    - Set this date to control how far back transactions should be retrieved

- **Import To Date**: Specifies the end date for importing transactions.
    - If left empty, the system will use the current date
    - Useful for importing historical data up to a specific point

![Financial Account Date Configuration](#)

!!!tip
    **Best Practice for Initial Setup:**
    - Set **Import From Date** to the date when you want to start tracking transactions (e.g., beginning of fiscal year)
    - Leave **Import To Date** empty to always import up to the current date
    - After the first import, you can leave **Import From Date** empty to automatically continue from the last import

!!!note
    **How Date Logic Works:**
    - The system automatically tracks the last import date for each account
    - On subsequent imports, if **Import From Date** is empty, it will start from the last import date
    - This prevents importing the same transactions multiple times

## Bank Connection Flow

### Step 3: Connect Bank Account

Once your user has the API Key configured and the financial account dates are set:

1. Open the **Financial Account** you want to connect
2. Click the **Connect Bank Account** button

    ![Connect Bank Account Button](#)

3. A **Salt Edge connection widget** will open in a popup window

    ![Salt Edge Widget - Bank Selection](#)

4. In the widget:
    - **Search or select your bank** from the list of supported banks
    - Click on your bank to continue

5. You will be **redirected to your bank's login page**

    ![Bank Authentication Page](#)

6. **Log in with your bank credentials** (username, password, and any additional authentication required by your bank)

    !!!warning
        **Important Security Note:**
        - Your bank credentials are entered directly on your bank's website, not in Etendo
        - Salt Edge never stores your bank credentials
        - Etendo never has access to your bank username or password

7. **Authorize the connection**:
    - Your bank will ask you to confirm permission for Salt Edge to access your account information
    - Review the permissions and confirm

8. **Automatic synchronization**:
    - After successful authentication, the system **automatically retrieves your bank accounts**
    - You will be redirected to a **success page** that displays:
        - A confirmation message that your bank connection was successful
        - Confirmation that your accounts have been synchronized
        - Instructions to close the popup window

    !!!success
        **Connection and Synchronization Complete!**
        - The bank connection has been established
        - Your bank accounts have been automatically synchronized
        - Connection details are now visible in the **Bank Connections** tab
        - You can now start importing transactions

9. **Next steps**:
    - Close the popup window
    - Return to your Etendo window
    - You can now proceed to import transactions (see the Importing Transactions section below)

!!!info
    **What happens automatically:**
    - The system creates the connection with Salt Edge
    - Retrieves all accounts associated with your bank connection
    - Links your Salt Edge accounts to your Etendo financial account
    - All connection details are stored in the **Bank Connections** tab
    
    You won't need to manually click "Sync Bank Connections" after connecting - it's done automatically!

## Importing Transactions

There are two ways to import bank transactions:

### Option 1: Manual Import (Single Account)

For importing transactions on-demand for specific accounts:

1. Open the **Financial Account** window.
2. Select one or more financial accounts.
3. Click the **Get Bank Statement** button.

    ![Get Transactions Button](#)

4. The system will:
    - Connect to Salt Edge.
    - Retrieve transactions within the configured date range.
    - Filter out duplicate transactions.
    - Create or update bank statements.
    - Create bank statement lines for each transaction.

5. A summary message will show the results:
    - Number of new transactions imported.
    - Any warnings or errors encountered.

![Import Results Message](#)

!!!tip
    Use this option when you need to immediately import transactions for specific accounts or when you want to review the import results right away.

### Option 2: Automatic Import (Scheduled Process)

For regular, automated imports across all connected accounts:

:material-menu: `General Setup` > `Process Scheduling` > `Process Request`

1. Schedule the **Get Bank Statements** process
2. Configure the frequency (e.g., daily, hourly)
3. The process will automatically:
    - Check all users with API Keys configured
    - Process all financial accounts with active bank connections
    - Import new transactions for each account
    - Log the results

    ![Scheduled Process Configuration](#)

    !!!info
        **Recommended Schedule:**
        - For most businesses: Run once or twice daily (e.g., 6 AM and 6 PM)
        - For high-volume accounts: Run every few hours
        - Consider your bank's update frequency and your business needs

## Understanding the Results

### Bank Statement Creation

When transactions are imported, the system automatically:

1. **Creates or updates Bank Statements**:
    - One bank statement per import period
    - Statement date reflects the import date range
    - Statements are linked to the Financial Account

2. **Creates Bank Statement Lines**:
    - One line per transaction
    - Includes transaction date, description, and amount
    - Stores the Salt Edge transaction ID to prevent duplicates

3. **Logs the Operation** :
    - All synchronization operations are logged in the **Bank Transaction Logs** tab.
    - Logs include execution date, status, request/response data, and error details.
    - Accessible from the Financial Account window for monitoring and troubleshooting.
    - Useful for audit purposes and debugging integration issues.

### Transaction Details

Each imported transaction includes:

- **Transaction Date**: When the transaction occurred
- **Amount**: Transaction amount (positive for credits, negative for debits)
- **Description**: Transaction description from the bank
- **Reference**: Transaction reference or ID
- **Status**: Transaction status (booked, pending, etc.)

![Bank Statement Lines](#)

### Duplicate Prevention

The system prevents duplicate imports by:

- Tracking Salt Edge transaction IDs
- Checking if a transaction was already imported
- Skipping transactions marked as duplicates by Salt Edge

## Connection Management

### Connection Status

Bank connections can have different statuses:

- **Active (AC)**: Connection is working normally
- **Inactive (IN)**: Connection exists but is not being used for transactions
- **Disabled (DI)**: Connection has been disabled (e.g., authentication expired)

### Viewing Bank Connections

To view all your bank connections:

1. Open the **Financial Account** window
2. Navigate to the **Bank Connections** tab
3. Here you can see all connections associated with the financial account, including:
    - Provider Name
    - Salt Edge Connection ID
    - Connection Status
    - Last Refresh Date
    - Fetch Scopes (permissions granted)

### Disconnecting a Bank Connection

If you need to remove a bank connection:

1. Open the **Financial Account** window
2. Navigate to the **Bank Connections** tab
3. Select the connection(s) you want to disconnect
4. Click the **Disconnect Connection** button

    !!!warning
        **Important:**
        - Disconnecting a connection will permanently remove it from both Etendo and Salt Edge
        - You will need to reconnect if you want to use this bank connection again
        - This action cannot be undone
        - Any pending transactions will not be affected, but no new transactions can be imported from this connection

5. After disconnection:
    - The connection is removed from the database
    - The connection is deleted from Salt Edge
    - You can verify the disconnection was successful by checking the Bank Connections tab

### Reconnecting

When the **Get Bank Statements** process runs and encounters a connection issue:

1. The system will attempt to retrieve transactions using the active connections.
2. If a connection fails, the system will:
    - Mark that connection as **Disabled (DI)**.
    - Add a warning message to the process log.
    - Automatically try the next available connection for the same financial account.
3. The process continues attempting connections until it finds a working one or exhausts all active connections.
4. At the end of execution, you can review all warning messages in the process result to identify which connections failed.
5. Failed connections will appear with **Disabled** status in the **Bank Connections** tab of the Financial Account window.
6. To restore a disabled connection, follow the reconnection steps described in the troubleshooting section below.

## Common Issues and Solutions

### Common Issues

- **"No API Key Available"**
    - Ensure your user has the Salt Edge API Key configured.
    - Check that the API Key is correct and active.

- **"Could not get redirect link"**
    - The bank connection service may be temporarily unavailable.
    - Try again in a few minutes.
    - Contact support if the issue persists.

- **"No new transactions found"**
    - Check your Import From/To Date configuration.
    - Verify that there are actually new transactions in your bank account.
    - Ensure the date range covers the period you expect.

- **Connection Status shows "Disabled"**
    - A connection may show as **Disabled** due to:
        - Authentication expiration with the bank.
        - Communication errors with Salt Edge.
        - Bank service temporary unavailability.
    - **Recommended resolution steps:**
        1. First, click the **Sync Bank Connections** button to verify the current health of the connection and refresh its status.
        2. Try executing **Get Bank Statements** again to see if the issue persists.
        3. If the connection still shows as **Disabled**, re-authenticate by clicking **Connect Bank Account** again and following the authentication flow.

### Getting Support

If you encounter issues:

1. Check the **Bank Transaction Logs** tab in the Financial Account window for error details.
2. Verify your API Key is configured correctly.
3. Ensure your date range is appropriate.
4. Contact Futit Services support with:
    - The error message.
    - The financial account affected.
    - The time when the issue occurred.

## Best Practices

1. **Regular Synchronization**: Schedule automatic imports to run daily or multiple times per day.

2. **Date Configuration**: 
    - Use **Import From Date** for initial setup only.
    - Leave it empty afterward to automatically continue from last import.

3. **Reconciliation**: 
    - Review imported transactions regularly.
    - Use Etendo's reconciliation features to match transactions with payments.

4. **Connection Maintenance**:
    - Monitor connection status regularly in the **Bank Connections** tab.
    - Re-authenticate if connections expire or appear disabled.
    - Bank accounts are automatically synchronized when you connect a new bank.
    - Use the **Sync Bank Connections** button only if you need to manually refresh account information (e.g., after adding new accounts at your bank).
    - Use the **Disconnect Connection** button to remove connections you no longer need.

5. **Multiple Banks**:
    - Configure each bank separately.
    - Use clear naming conventions for financial accounts.
    - Each bank connection will automatically retrieve and link all available accounts.

6. **Security**:
    - Keep API Keys confidential.
    - Don't share user credentials.
    - Disconnect bank connections when no longer needed using the **Disconnect Connection** button.
    - Disconnecting removes the connection from both Etendo and Salt Edge permanently.

## Additional Resources

- [Salt Edge Documentation](https://docs.saltedge.com/){target="_blank"}
- [Financial Extensions Bundle Release Notes](https://docs.etendo.software/whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes/){target="_blank"}
- [Bank Reconciliation Guide](../basic-features/financial-management/receivables-and-payables/transactions.md#bank-reconciliation){target="_blank"}
