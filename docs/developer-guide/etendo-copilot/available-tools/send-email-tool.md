---
tags:
    - Copilot
    - IA
    - Machine Learning
    - Tool
    - Send
    - Email
---

# Send Email Tool

## Overview

The **Send Email Tool** is designed to send emails. This tool facilitates sending emails in an efficient and structured way. It accepts the following input parameters: subject (the email subject), mailto (the recipient's email address), and html (the HTML content of the email). As output, it returns a message indicating the result of sending the mail. This tool provides the user with:

- Automation: It automates the sending of emails in web applications and systems.
- Flexibility: It allows you to select between different sending methods (Resend or SMTP), depending on the environment configuration.
- Efficiency: It facilitates the management of email notifications and communications, improving operational efficiency.

This tool is essential for developers and system administrators who need to easily integrate email functionalities into their applications or services.

## Functionality

This tool is useful in any application or service that needs to send emails automatically. It can be used for notifications, updates, order confirmations, password resets, among other things.

This process consists of the following actions:

- **Processing Arguments** 

    It takes the input parameters specifying the subject, recipient and HTML content of the mail.

- **Verifying Sending Method** 

    It determines the sending method using a `MAIL_METHOD` environment variable. Two main methods are supported:

    - Resend: Uses the Resend API to send the mail. It needs the Resend API key, stored in the environment variable
    `RESEND_API_KEY`.
    - SMTP: Uses the SMTP protocol to send mail. It configures and sends mail using an SMTP server such as Gmail.

- **Sending Mail**
    
    Depending on the sending method, configures and sends mail with the information provided.

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

Imagine you want to send a notification email. The input parameters for the assistant would be:

- `subject`: Account update
- `mailto`: user@example.com
- `html`: 
    ```html
    <h1>Account Upgrade</h1>
    <p>Your account has been successfully upgraded.</p>
    <p><p>Your account has been successfully upgraded.
    ```


The Send Email Tool will process these parameters and select the configured sending method. It will then send the mail and return a message indicating whether the mail was sent successfully.