---
title: Using Etendo Copilot Context Features
description: Learn how to interact with Etendo Copilot, capture context, and configure user preferences for an enhanced ERP experience.
slug: /user-guide/etendo-copilot/using-context-features
---

# Using Etendo Copilot Context Features

## Activating Copilot

1. Open any window in the Etendo ERP (e.g., Sales Order, Inventory).
2. Locate the **Copilot button** in the toolbar at the top of the window.
3. Click the button to launch the Copilot interface.
4. Ask a question or provide an instruction (e.g., "What information can you give me about this window?").

The Copilot button is available across all ERP windows, making it easy to access assistance wherever you are.

## Understanding Context in Copilot

Copilot enhances its responses by automatically capturing context based on your actions in the ERP. It supports three key context types:

### Active Window Context

Copilot identifies the currently active window, such as "Purchase Order" or "Product List," and includes this information in its responses. For example:

- **Action**: Open the "Sales Order" window and activate Copilot.
- **Question**: "What information can you give me about this window?"
- **Response**: Copilot provides details related to the "Sales Order" window.

### Selected Record Context

When you select a record in a list or grid, Copilot captures its details (e.g., ID, name, or other relevant fields) and uses this data to assist you. For example:

- **Action**: Select a product from the "Product" grid and activate Copilot.
- **Question**: "What info can you give me about this record?"
- **Response**: Copilot returns information specific to the selected product.

### Edited Record Context

If you're editing a record in a form, Copilot detects the form’s edit mode and captures the current input values, including unsaved changes. For example:

- **Action**: Edit a "Customer" record, change the name, and activate Copilot.
- **Question**: "What info can you give me about this record?"
- **Response**: Copilot includes the updated name and other form fieldwork.

> **Tip**: Ensure the correct window or record is active before asking Copilot a question to get the most accurate response.

## Configuring User Preferences

You can customize Copilot by setting a default prompt that tailors its behavior to your needs. This is done in the ERP’s Preferences section.

### Setting a Default Prompt

1. Navigate to the **Preferences** section in the Etendo ERP (typically under user settings or administration).
2. Create a new preference for "Copilot Default Prompt."
3. Enter a prompt using placeholders like `@ORG_NAME@` or `@USERNAME@`. For example:

```
You are working in the organization '@ORG_NAME@' (ID: @AD_ORG_ID@) under the client '@CLIENT_NAME@' (ID: @AD_CLIENT_ID@). You are logged in as @USERNAME@ (User ID: @AD_USER_ID@) with the role '@ROLE_NAME@' (Role ID: @AD_ROLE_ID@). The current warehouse in use is '@WAREHOUSE_NAME@' (Warehouse ID: @M_WAREHOUSE_ID@).
```

### Available placeholders

| Placeholder      | Replace with value                 |
| ---------------- | ---------------------------------- |
| @AD_CLIENT_ID@   | User client ID                     |
| @CLIENT_NAME@    | User client name                   |
| @AD_ORG_ID@      | Current organization ID selected   |
| @ORG_NAME@       | Current organization name selected |
| @AD_USER_ID@     | Current user id                    |
| @USERNAME@       | Current username                   |
| @AD_ROLE_ID@     | Selected role ID                   |
| @ROLE_NAME@      | Selected role name                 |
| @M_WAREHOUSE_ID@ | Selected warehouse ID              |
| @WAREHOUSE_NAME@ | Selected warehouse name            |

Your custom prompt persists across sessions, ensuring a consistent experience.

## Examples of Use

Here are practical examples based on real-world scenarios:

### Example 1: Checking Window Details

- **Scenario**: You’re in the "Purchase Order" window.
- **Steps**: Click the Copilot button and ask, "What information can you give me about this window?"
- **Result**: Copilot describes the "Purchase Order" window’s purpose and key fields.

### Example 2: Analyzing a Selected Record

- **Scenario**: You select a customer record in the "Business Partner" grid.
- **Steps**: Click the Copilot button and ask, "What info can you give me about this record?"
- **Result**: Copilot provides the customer’s ID, name, and other details.

### Example 3: Reviewing an Edited Record

- **Scenario**: You’re editing a product’s price in a form.
- **Steps**: Click the Copilot button and ask, "What info can you give me about this record?"
- **Result**: Copilot reflects the new price and other edited fields.

### Example 4: Confirming User Context

- **Scenario**: You want to verify your configured prompt.
- **Steps**: Click the Copilot button and ask, "What is my context?"
- **Result**: Copilot returns your organization, role, and other details from the default prompt.

## Additional Notes

- Copilot’s accuracy depends on the context it captures. Double-check that the correct window or record is active.
- For advanced configurations or troubleshooting, refer to the [Developer Guide](https://docs.etendo.software/developer-guide/etendo-copilot/).
