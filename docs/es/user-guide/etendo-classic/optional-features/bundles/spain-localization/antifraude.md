---
title: Antifraud
tags: 
    - Spanish Localization
    - Electronic Invoicing
    - Antifraud Law
status: new
---

:octicons-package-16: Javapackage: `com.etendoerp.antifraud`

## Introduction
This section describes the **Etendo Antifraud** module, included in the Spanish Localization bundle.

!!! info 
    - To include this functionality, it is necessary to install the **Spanish Localization** bundle, starting from versions **1.34.0** on Etendo 24.4 and **3.5.0** on Etendo 25.1
    - To do this, follow the Marketplace instructions: [Spanish Localization](https://marketplace.etendo.cloud/#/product-details?module=003B475055DD421B9483B5BE15AA48C5).
    - For more information about available versions, core compatibility and new features, visit [Spanish Localization - Release Notes](https://docs.etendo.software/whats-new/release-notes/etendo-classic/bundles/localization-spain-extensions/release-notes/).

!!! warning
    The module includes multiple restrictions in the invoicing flow, required by law in Etendo. Keep this in mind when using it, and plan your processes following the new flows.

The Antifraud module includes new functionalities and restrictions in the invoicing flow and data management, designed to guarantee the integrity, preservation, readability, traceability and immutability of the data. The module is framed within [Law 11/2021](https://www.boe.es/buscar/pdf/2021/BOE-A-2021-11473-consolidado.pdf){target="_blank"}, in force since *July 9, 2021*, on measures to prevent and combat tax fraud, and [Royal Decree 1007/2023](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2023-24840){target="_blank"}, in force since *December 5, 2023*, which approves the Regulation establishing the requirements that computer or electronic systems and programs supporting the invoicing processes of entrepreneurs and professionals must adopt, and the standardization of invoicing record formats.

## Configuration

### Configure Digital Certificate

You must configure a digital certificate for the corresponding legal organizations. To do this, [follow this guide](./funcionalidades-generales-para-sifs.md#carga-de-certificados-digitales). 

### Backup generation process
An annual backup generation process has been created, in response to the following requirement:

> Have and apply backup policies based on implementing a secure backup system based on 3, 2, 1 policies, through encryption. A BACKUP COPY MUST NOT BE TAMPERABLE. ENCRYPTED AND NOT TAMPERABLE AND ENSURE THEY ARE MADE. Normally it would be an annual copy of the last 5 years. DEFINE THE PROTOCOL.
    
Once at the beginning of each year (date and time available to the user), an automatic backup process will run automatically for those who have the Spanish localization bundle installed.

#### Initial Configuration

!!! warning
    The initial configuration of this process can only be performed by a developer, as it involves access to the customer's server

To configure this process and start using it on the server, the user must run the following command on it:

``` bash title="Terminal"
sudo modules/com.etendoerp.antifraud/scripts/setup-yearly-backup
```

This command will run an initial configuration script for the process, in which the user will be asked for the directory where the ERP is located and the date (minute, hour, day and month of the server) on which the annual backup process should be executed.

The script will create a scheduled process to run the backups once a year, on the specified date. In addition, a configuration file with root-only permissions will be created (by default saved in `/etc`, named `yearly-backup.conf`), which can be edited by the user to define variables such as the backup password, the URL of the servers to which copies will be sent, the number of backups to keep (must be 5 or more), etc.

#### Process Description

This process consists of the following steps:

1. Create backups of the database, sources and ERP attachments
2. Initialize a counter of successfully completed backups
3. Try to save a local ERP backup in a folder designated by the user, or `/backups-annual` if none was designated
4. Backups will be encrypted. That is, a password will be needed to use them
5. This password must be added in the backup configuration file `yearly-backup.conf` created with the configuration script, in the variable `ANNUAL_BACKUP_PASSWORD`
6. If the backup was successful, increment the successful backup counter by 1
7. Perform rotation of local backups (if there are more annual backups than those defined in the configured rotation variable, the oldest one is deleted)
8. Synchronize backup copies using the available plugins (S3, label, samba, or sftp). There is also the option for the partner/provider to develop their own synchronization method and use it
9. In case the local backup was not successful due to lack of space on the server, what is done in each synchronization plugin is to create the backup while simultaneously sending it, so as not to occupy server space
10. Increment the successful backup counter by 1 for each plugin that has finished correctly
11. Finally, if the local backup was performed correctly, and if the option is enabled by the user, copies are made to external servers (using rsync, or scp) and the counter is incremented if they finished successfully
12. If 3 or more copies were not successfully made, the process will end with a warning specifying this

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/antifraude/configuracion-backup.png)


The backup process will generate in each location where it was specified a compressed and encrypted file: `backup-<year>.<compression format>.asc`

If an error occurred during backup generation, and the 3 required copies were not achieved, an email will be sent to the configured recipient if it was set (email configuration is the same as for Etendo automatic backups)

To access the contents of the backup, it must first be decrypted using the following command:

```bash title="Terminal"
sudo openssl enc -d -des3 -a -salt -pbkdf2 -in [encrypted backup name] -out [name to give to the decrypted backup + compression extension used] -k [decryption password]
```

The command will decrypt the backup and it can then be decompressed and used normally.

!!! info
    The user will be responsible for ensuring that they have at least 3 copies of each annual backup. To do this, they must configure the servers where it will be synchronized and the methods to do so

### Digital Signatures of Documents

There is an option to add digital signatures when printing PDF documents using the dedicated toolbar button.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/antifraude/boton-imprimir-firma.png)

To digitally sign a document, the following conditions must first be met:

- Have a valid certificate issued by the AEAT loaded in the system, for the legal organization of the invoice to be printed. It must be loaded following the guide [Upload Digital Certificates by Legal Organization](#carga-certificados-digitales-organizacion-legal)
- Have an internet connection.
- Have an environment with a production instance (if it is not a production environment, this will be notified in the printed document via watermark).
    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/antifraude/documento-no-oficial.png)

- The invoice must be issued. If it is in draft, this will be shown with a watermark so it can be easily differentiated
    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/antifraude/documento-borrador.png)


If everything is met, the printing process will add an electronic signature to the generated PDF, with the signer's data (data present in the certificate)
    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/antifraude/datos-firmante.png)


### Document number generation when issuing an invoice

:material-menu: `Application` > `Financial Management` > `Accounting` > `Setup` > `Document Type`

The calculation of the document number for invoices has been modified so that it is performed when completing them.

#### Initial Configuration

In the `Document Type` window, the field `Sequence For Issued Invoices` was added. To calculate the invoice document number upon issuing, it is mandatory to assign a new sequence (different from the one assigned in the `Document No. (numeration)` field) in the new field.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/antifraude/secuencia-facturas-emitidas.png)

#### Process Description

When creating an invoice, a document number is still assigned when saving it in draft status, but it will be replaced upon completion by the next number in the sequence assigned in the `Sequence for Issued Invoices` field. This avoids possible gaps in numbering, thus ensuring better traceability of invoicing data.

!!! warning
    When trying to complete an invoice with a date earlier than another previously completed one, the system will throw an error. To complete the new invoice, its date must be changed to one equal to or later than the completed invoice with the latest date.

### Chained Hashing of Audit Records

:material-menu: `Application` > `General Setup` > `Security` > `Audit Discrepancies`

Every 6 hours, a background process is executed, which checks for all audit records generated in the quarter that there are no changes compared to the state they had when they were created.

To check this, the process generates the hash code of each audit record and compares it with the hash code automatically generated when the record was created. If these codes differ, then the system detects that an audit discrepancy has occurred, and this is recorded in the new window :material-menu: `Application` > `General Setup` > `Security` > `Audit Discrepancies`.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/antifraude/discrepancias-auditoria.png)

From this window you can navigate to the audit record for which changes were detected, and the date on which the discrepancy was detected is also shown

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/antifraude/registro-discrepancia.png)

!!! warning
    Due to the use of database functions present only in more recent versions, this functionality is only available in Antifraud module versions compatible with Core 25. In versions compatible with Core 24 it is not available. It is recommended to upgrade to Core 25Qx to guarantee the immutability and traceability of audit records
## Restrictions

### Cash Payments/Collections Reaching/Exceeding 1,000 Euros

A validation has been implemented when making payments/collections. It blocks cash payments when the total cash amount (historical + the one being attempted now) for the same transaction reaches or exceeds EUR 1,000. This restriction has been implemented in response to the following requirement of Law 11/2021, of July 9, on measures to prevent and combat tax fraud, in its Article XV:

> …Law 7/2012, of October 29, amending tax and budget regulations and adapting financial regulations to intensify actions in the prevention and fight against fraud, in line also followed by other countries in our environment, determined the limitation on the use of cash for certain economic transactions. The positive results of said rule motivate the modification introduced in the substantive regime of cash payments, aimed at deepening the fight against tax fraud, reducing the general limit of cash payments from 2,500 to 1,000 euros …

It applies if at least one of the parties has tax residence in Spain (the organization of the document or that of the business partner). If both organizations are outside Spain, it does not intervene. If the country cannot be determined, it acts conservatively and applies the validation.

This restriction is activated only if the payment method is marked as `Cash`. This is a new field introduced in the `Payment Method` window.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/antifraude/es-efectivo.png)

The method groups as the same transaction in the following cases:

If an invoice is paid:

- The current invoice.
- Other invoices from the same order.
- Invoices that share goods shipments with the current one (it searches for invoice lines linked to the same goods shipments).

If an order is paid:

- The order.
- All invoices created from that order.

The method calculates whether to raise an error as follows:

1. Quick review of the current payment: if the amount of the current payment (converted to EUR) is ≥ 1,000, it blocks directly and raises an error.
2. Check by selected documents:
    
    * It iterates through the selected lines and accumulates the current cash amount per document.
    * For each detected document:
        
        - It adds the historical cash payments linked to its due dates and to payments whose method is cash, converted to EUR using each payment date.
        - The accumulated current cash amount for that group is added.
        - If the total (historical + current) ≥ EUR 1,000, it blocks and returns an error.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/antifraude/limite-efectivo.png)


### Draft Invoices, Orders and Goods Shipments

A new restriction has been added in the sales flow, due to the following requirement of the anti-fraud law:

> …Royal Decree 1007/2023, there is an obligation of a generic nature and that does not require regulatory development whereby any computer management system, among which must be included systems that generate goods shipments, proforma invoices or drafts, must preserve the generated records, even when these usually end up becoming an invoice. Therefore, it would not be legal and would be subject to sanction, the use of systems that generate preparatory documents for invoices or simplified invoices, without the computer system itself having control elements for the preservation of such preparatory documents duly linked to the invoices or to the invoicing records that are finally issued or not, in the absence of an invoice, so that they are recorded and preserved in the system…

With the installation of the Antifraude module, if an issuer (Legal Organization) uses a SIF of any type (SII, Verifactu or TicketBAI) it will not be possible to delete invoices, orders or goods shipments from the sales flow, even if they are in draft status. If an attempt is made, the following error will be raised:

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/antifraude/eliminar-registro.png)


As a result, the possibility to deactivate these elements has been included, to perform a logical deletion of records that are no longer desired, so that they no longer appear in the window or in other processes.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/antifraude/desactivar-registro.png)

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/antifraude/registro-desactivado.png)


In addition, a new informational field has been added in sales invoices, which will be filled in when the invoice is issued with information about related orders/goods shipments, if any. This is to guarantee the traceability of the invoice in all possible cases. This field contains all this information in JSON format. By default, the field is not shown, since its use is only for audits. It can be chosen to display it if needed in the system configuration. That is, by checking the shown checkbox for the field, in the `Windows, Tabs and Fields` window, accessible only by the system administrator user.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/antifraude/datos-trazabilidad-factura.gif)


### Reactivation and Unposting of Collections, Journal Entries and/or Related Transactions

Modification/deletion of collections, journal entries and/or financial account transactions that have already been processed and/or posted is prohibited.

> With the objective of not allowing the production and possession of programs and computer systems that allow the manipulation of accounting and management data, the obligation is established that computer or electronic systems that support accounting or business management processes comply with certain requirements that guarantee the integrity, preservation, accessibility, readability, traceability and immutability of records, requirements whose technical specification may be subject to regulatory development, including the possibility of submitting it to certification. Likewise, in accordance with said regulation, a specific sanctioning regime is established, derived from the mere production of these systems or programs, or their possession without adequate certification…

If the user attempts to reactivate, modify, unpost, etc. the document, an error message will be displayed specifying that opposite-sign movements must be made to cancel the effects of the document. That is, generate a journal entry with amounts opposite to those generated by the collection/journal entry to be deleted (the debit amount as credit, and vice versa).

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/antifraude/borrar-contabilidad.png)

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/antifraude/error-borrado.gif)


### Delete Entity and Reset Accounting Processes

These processes have been restricted, due to one of the requirements necessary to ensure compliance with the anti-fraud law, which specifies that the system must not provide tools for mass deletion of data.

According to Law 11/2021, amended by the General Tax Law (art. 29.2.j): 

> computer systems and programs that support accounting, invoicing or management processes must guarantee the integrity, preservation, accessibility, readability, traceability and immutability of records, without interpolations, omissions or alterations that are not duly recorded in the systems themselves. 

Mass deletion of data contradicts these obligations and is implicitly prohibited both by the record integrity regime and by the sanctioning regime of art. 201-bis of the LGT. In addition, Royal Decree 1007/2023 expressly prohibits the alteration or deletion of records without preserving their traceability.


If an attempt is made to use the ‘Delete Entity’ process to delete an entity that has any of its reachable organizations configured to use some SIF, an error will be raised:

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/antifraude/borrar-cuenta.png)

In the case of the `Reset Accounting` process, the system does not allow selecting the `Delete existing/current entries` option, marking this field as read-only.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/antifraude/reinicializar-cuenta.png)

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.