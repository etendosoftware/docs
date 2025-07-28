---
tags:
    - Etendo Copilot
    - Email Automation
    - SMTP
    - Resend API
    - Notifications
    - Tool
---

# Send Email Tool

:octicons-package-16: Javapackage: `com.etendoerp.copilot.toolpack`

## Overview

The **Send Email Tool** is designed to send emails. This tool facilitates sending emails in an efficient and structured way. It accepts the following input parameters: subject (the email subject), mailto (the recipient's email address), and html (the HTML content of the email). As output, it returns a message indicating the result of sending the mail. 

!!!info
    To be able to include this functionality, the Copilot Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. For more information about the available versions, core compatibility and new features, visit [Copilot Extensions - Release notes](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

This tool provides the agent with:

- Automation: It automates the sending of emails in web applications and systems.
- Flexibility: It allows selecting between different sending methods (Resend or SMTP), depending on the environment configuration.
- Efficiency: It facilitates the management of email notifications and communications, improving operational efficiency.

This tool is essential for developers and system administrators who need to easily integrate email functionalities into their applications or services.

## Setup

To use this tool, it is necessary to configure the variable `MAIL_METHOD`:

- SMTP: It uses the SMTP protocol to send mail. It configures and sends mail using an SMTP server such as Gmail. The SMTP is the default value for this variable. Additionally, credentials must be setup: `MAIL_FROM` with the sender email and `SMTP_PASSWORD` with the sender password.

For example:

``` groovy title="gradle.properties"
MAIL_METHOD=SMTP
MAIL_FROM= example@example.com
SMTP_PASSWORD= ******
```
- resend: In this case, the [resend API service](https://resend.com/){target="\_blank"} is used, designed to resend email requests. In case this is selected, it is necessary to set up the variable `RESEND_API_KEY`. For example:

``` groovy title="gradle.properties"
MAIL_METHOD=resend
RESEND_API_KEY=******
```

## Functionality

This tool is useful in any application or service that needs to send emails automatically. It can be used for notifications, updates, order confirmations, password resets, among other things.

This process consists of the following actions:

- **Processing Arguments** 

    It takes the input parameters specifying the subject, recipient and HTML content of the mail.

- **Verifying Sending Method** 

    It determines the sending method using a `MAIL_METHOD` environment variable. The options are mentioned in the [Setup](#setup) section above.

- **Sending Mail**
    
    Depending on the sending method, it configures and sends mail with the information provided.

- **Returning the Result**
    
    Returns a message indicating if the mail was sent successfully or if there was an error. For example:
    
    ```
    { “message”: “Mail sent successfully”}
    ```
 
    if the mail was sent successfully.

    ```
    { “message”: “Mail method not supported”}
    ```
    
    if the sending method is not supported.

## Usage Example

Imagine you want to send a notification email. The input parameters for the agent would be:

- `subject`: Account update
- `mailto`: user@example.com
- `html`: 
    ```html
    <h1>Account Upgrade</h1>
    <p>Your account has been successfully upgraded.</p>
    <p><p>Your account has been successfully upgraded.
    ```


The Send Email Tool will process these parameters and select the configured sending method. It will then send the mail and return a message indicating whether the mail was sent successfully.