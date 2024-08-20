---
tags:
  - PSD2 Service
  - Financial Account
  - Redsys
  - .p12 File
  - Bank Integration
  - Etendo RX
---

# PSD2 Integration

:octicons-package-16: Javapackage: `com.etendoerp.psd2.bank.integration`

:octicons-package-16: Javapackage: `com.etendorx.psd2.bank.integration`

## Overview

Etendo is able to integrate with several banking entities using the PSD2 protocol (Payment Services Directive 2) through the [Redsys](https://redsys.es/){target="_blank"} API, which acts as a service provider. 
The integration is carried out only with **banks that support Redsys**, thus guaranteeing secure and efficient communication for obtaining financial transactions, balance inquiries and movements compatible with the PSD2 protocol.

!!!info
    For more information about banks supported by Redsys visit [Banks supported by Redsys](https://redsys.es/psd2.html){target="_blank"}.

## Dokerized Services

To start the integration, first of all it is necessary to raise all the services related to this module, in particular the RX Service. RX is a service that exposes a reactive development platform and the PSD2 service, which is the one that is really interacting with Redsys. To do this, first edit the `gradel.properties` file by adding these configuration variables:

- `docker_com.etendoerp.etendorx=true`
- `docker_com.etendorx.psd2.bank.integration=true`

Then, it is necessary to **execute the command** in the terminal: 

```
`./gradlew resourse.up`
```

!!!info
    For more information about how to handle Dockerizations Etendo visit [Docker Management developer guide](../../../../developer-guide/etendo-classic/bundles/platform/dependency-manager.md). 

## Service Configuration in Etendo

### Configuration in the RX config window 

In the RX config window, add a new record as shown below. This configuration indicates the **URL** where the PSD2 service is running.

![alt text](../../../../assets/developer-guide/etendo-classic/bundles/financial/tech-doc-psd2-integration-0.png)

### Configuration in the RX service window 

!!!info
    For the configuration in the RX service window, follow the tutorial defined in the [Adding the token value](../../../../developer-guide/etendo-rx/tutorials/creating-a-new-microservice.md#adding-the-token-value) in the Creating a New Microservice section of the documentation. 

### Configuration of the PSD2 HUB service in Redsys

**Redsys** is a technology platform that provides payment services in Spain. It works with banks and other payment service providers to facilitate secure electronic transactions, including card payments and mobile payment solutions.

Redsys acts as an **intermediary in payment processing**, offering payment gateway services and transaction security. So, it is necessary to create an account in Redsys in order to integrate the Etendo with the bank provider. 

- To create an account in Redsys, login to the [Sandbox Registration Page](https://market.apis-i.redsys.es/psd2/xs2a/user/register){target="_blank"}.

![alt text](../../../../assets/developer-guide/etendo-classic/bundles/financial/tech-doc-psd2-integration-1.png)

- Create a new service under the title `<Client Name>-API` by entering in the [Application Registration Section](https://market.apis-i.redsys.es/psd2/xs2a/application){target="_blank"}.

![alt text](../../../../assets/developer-guide/etendo-classic/bundles/financial/tech-doc-psd2-integration-2.png)

- Choose a tittle to create the application: 

![alt text](../../../../assets/developer-guide/etendo-classic/bundles/financial/tech-doc-psd2-integration-3.png)

- After adding the required information, the application will be created:

![alt text](../../../../assets/developer-guide/etendo-classic/bundles/financial/tech-doc-psd2-integration-4.png)

- At the bottom of the same page the **Subscription** section is shown, click on **See Details** to subscribe to the HUB of your choice.

![alt text](../../../../assets/developer-guide/etendo-classic/bundles/financial/tech-doc-psd2-integration-5.png)


## Certificate and Generation of the P12 file

At the moment of integrating the **Etendo financial accounts with the corresponding bank** using the PSD2 security protocol and the payment service provider Redsys, it is crucial to understand certain key concepts and the role of specific components, such as the **.p12 file**. This document provides an overview of PSD2, Redsys, and the role of a .p12 file in this integration.

### PSD2 Definition

The **Revised Payment Services Directive (PSD2)** is an European Union legislation designed to regulate payment services and payment service providers in the EU and the European Economic Area (EEA). 

Its main objectives are:

- Improving the security of electronic payments: it implements stricter authentication requirements to reduce fraud.
- Encouraging innovation and competition: allows Etendo to access users' bank account information (by giving consent), promoting the emergence of new financial services.
- Consumer protection: increases transparency and establishes new liability rules for unauthorized payments.

### .p12 file utility for a PSD2 integration with Redsys

A .p12 file (also known as PKCS#12) is a **file container** that can store one or more X.509 certificates, as well as the associated private key. These files are used to secure communications and authenticate the identity of participants in a transaction.

The following are the functions of the .p12 file:

-  **Authentication**: Verifies the identity of the bank account user accessing account information or initiating payments, ensuring that they are who they claim to be.

- **Encryption**: Protects the confidentiality of communications between Etendo, the bank and Redsys.

- **Integrity**: Ensures that messages have not been altered during transmission by means of digital signatures.

For this integration, it is necessary to guarantee crucial aspects to ensure **security and compliance** with PSD2 regulations:

- The user through Etendo and the bank need to authenticate each other.

- Communications between the Etendo user and the bank must be encrypted to ensure that sensitive data (such as customer credentials and financial transactions) cannot be intercepted or manipulated. 

- Some operations may require the digital signature of messages to ensure their integrity and authenticity.

To guarantee this, two types of certificates are required:

**QSealC (Qualified Electronic Seal Certificate)**: Used to digitally sign messages and guarantee their integrity and authenticity.

**QWAC (Qualified Website Authentication Certificate)**: Used to authenticate the server and enable secure communication.

!!!info
    These certificates are issued by authorized trust service providers, through the [URL eIDAS Dashboard](https://esignature.ec.europa.eu/efda/tl-browser/#/screen/home){target="_blank"}, you can locate the authorized certifying entities for the issuance of the EIDAS certificate.

!!!note
    For both certificates, it is an **indispensable condition to be registered with the Bank of Spain**, which is the banking supervisor of these certificates. Contact the service provider for more information.


### Generating the .p12 file

There are two ways of generating the .p12 file: 

1. Save the server certificate and private key: Copy the contents of the server certificate and private key into separate files, e.g. `cert.cer` and `key.pem`.

Create the P12 file: Using the [KeyStore Explorer application](https://keystore-explorer.org/){target="_blank"}. This application provides an intuitive interface and facilitates the creation of the .p12 file.

2. It is also possible to perform this procedure using the **OpenSSL tool**.

These are the specific commands:

```
openssl pkcs12 -export -out api-testkeypar.p12 -inkey key.pem -in cert.cer -name "api-test" -passout pass:keystore_password -passin pass:cert_password

```

!!!info
    To protect the P12 file a password will be prompted. This password will be required each time the P12 file is used for authentication or digital signature.

### OpenSSL command explained

- **export**: Indicates that a PKCS#12 file is being created.
- **out `testkeypar.p12`**: Specifies the name of the output PKCS#12 file.
- **inkey `key.pem`**: Specifies the file containing the private key.
- **in `cert.cer`**: Specifies the file containing the public certificate.
- **name `api-test`**: Assigns the alias `api-test` to the certificate inside the PKCS#12 file.
- **passout pass**: *keystore_password*: Specifies the keystore password. This sets the password to protect the PKCS#12 file.
- **passin pass:`cert_password`**: Specifies the password for the private key, if the key is encrypted.

## Productive certificates

Once the **QSealC** and **QWAC** certificates have been obtained, the .p12 file must be generated as previously explained, taking into account that the server certificate corresponds to the QWAC certificate and the private key corresponds to the QSealC certificate.

## .p12 Configuration

Once the .p12 has been generated it is necessary to indicate the values of the parameters with which it has been generated as well as the path where it is located within the OAuth provider configuration window for each of the providers, as shown below.

![alt text](../../../../assets/developer-guide/etendo-classic/bundles/financial/tech-doc-psd2-integration-8.png)


The fields to be completed are:

- **Keystore Path**: Path to .p12 file
- **Keystore Password**: Password of the .p12 file
- **Certificate Alias**: Alias of the certificate
- **Certificate Password**: Password of the private key.

These parameters allow the integration to make use of the .p12 to secure communications and authenticate the identity of the transaction participants.

