---
title: Audit Trail
tags:
    - Audit trail
    - Security
    - Monitor
---

# Audit Trail

:material-menu: `Application` > `General Setup` > `Security` > `Audit Trail`

## Overview

Audit Trail allows the user to monitor every data change done in any table or entity through the user interface.

Audit trail feature monitors data changes such as:

- Insert
- Update
- Delete

Audit trail feature must be enabled by the "System Administrator Role" in the Application Dictionary, as the first thing to do is to configure the table/s for which this feature is going to be enabled.

Once a change has been made in a table for which the audit trail feature has been enabled, it is possible to monitor that change through the user interface by using the action button "Audit Trail".

![](../../../../assets/drive/V-wLKxec4uzSuG-eFItBU00cQYeO5SNhiLTDkY78kPRaK6e-P_R_z39-K5icHtUSX-WjoeFL34_Iv45c0aym2FRV9_F_e0W6QA0U8Lim_qkovbX44ihOl-nH-mKEio1pSpfQDqlm.png)

## Audit Trail

Audit Trail view displays read-only information about all the recorded data changes done in the tables for which the audit trail feature has been enabled.

![](../../../../assets/drive/CkScAz_BHFw9uZIejCEG18y9IOkyiO23K5CMqCRWCkc-DEAWZ0x5G8RyDwjqApky49FILfUisRIJUnqS_Sfob0j128cKfhFFQhfOI92bmbTAPsN1TyfGVMaPXeoj9tbBzqsTB-r4.png)

The changes done in a given table, column and record are viewed by showing the corresponding record ID or UI of the records in the database.

## Configuration

In order to track audit information, the system administrator needs to perform two tasks:

- Enable the audit trail for one or more tables in the system
- Run the 'Update Audit Trail infrastructure' process

In the following sections, a step-by-step guide with more detailed information is provided.

## Enabling audit trail for a table

Enabling/disabling the audit trail feature for a table is done in the Table definition in the Application Dictionary.

- Switch to the System Administrator role
- Go to Application Dictionary > Tables and Columns
- Navigate to the table for which you want to enable the Audit Trail
- Switch to Edit View
- Mark the "Fully Audited" checkbox and save

### Audit Inserts

When a table is flagged as Fully Audited, the users can decide if they want to audit the insertions done in that table.

![](../../../../assets/drive/ebTtUMQskmHQd1Fd5BWoW0_lKwtwgNTn41V1uJKV4RGTKR_uXKuR_PqU4rzTUBVQct38OejbovWWycB-z1A7YEvwNedzpv6VCi38eHb2telDh9994cV4vCW1QEOGlDw1Ojs11Und.png)

If the Audit Inserts field is checked in a table, when a new row is inserted in that table several records will be inserted in the Audit Trail table, one for each column in the audited table. These records will contain the original value of the columns of the new row.

Usually, it is not necessary to store this information, because the original value of a column could be easily obtained by using the Old Value and New Value fields of the Audit Trial table that correspond with that column. If the Audit Inserts field is left unchecked, only one row will be inserted in the Audit Trial table for each record inserted in the audited table. At least this one record needs to be inserted in the Audit Trial table to be able to store which process was used to create the record in the audited table.

### Excluding columns

By default, when a table is audited, modifications in any of its columns are audited. In some cases, it makes sense not to audit changes for some of them. This can be configured by setting the _Exclude Audit_ flag in _Tables and Columns > Table > Column_ tab.

![](../../../../assets/drive/Xy3wTyW3wrUeerAoND_Rw2c6wVVhxkq_AEzzTjBLLpiBg6VsMWcQjAn6T4te4akp_o-x381v3wT3012cttvLqjKWRsd-Tfe0Go0FX1KGlG_vSG57Bm4yo8ZnB0gxdTSV3qi7f-4b.png)

## Running the System Compilation

The audit trail system uses a number of generated triggers (one per table to be audited) to collect the audit data for all changes.

These triggers need to be regenerated, when executing a system compilation, once the following actions have been performed:

- The Audit Trail feature has been enabled or disabled for a table
- There has been any structural change to a table being audited (i.e. new columns, changed columns)

## The Audit Trail Popup

For the set of tables for which the audit trail feature has been enabled, the button ![](../../../../assets/drive/tmlPernhlkGB49t7gLt12N3zfxbYevzxuPC65DZavmEO8p5UBe2_sO_YD6lBTkhBvnNrQ64jkRAnuahaKRTGnLPGUvmSEX_K5_Ekh5Ojd-21ZyZ4KWEFIjujNg_xqg_PCFahXdJo.png) is shown in the toolbar of the corresponding windows. It gives access to the Audit Trail Popup.

This popup allows examination of the history of the record which is currently shown in the window. It has two main view modes which allow examining the following data:

- 'Record history' of a single record
- 'Deleted records' of a single tab

## The 'Record History' view

This view is displayed when the popup is opened from an existing record via the new toolbar button.

The top area always shows a reference to the entity (i.e. Sales Order) and the record "1000175 - 2016-04-03 00:00:00.0-0.00" for which the history is displayed.

Then a number of filters are available which allow some restriction on the changes displayed to ease the use of records with many modifications.

The grid in the lower area shows all changes done to this record while the audit trail feature was enabled. The changes are shown sorted from the most recent change back to earlier changes.

!!! info
    Only fields which are visible in the corresponding tab are shown here.

A row in this grid corresponds to a single changed field. For changes to an existing record, the number of grid entries shown correspond to the number of fields changed. For new record creations or record deletion, one row in the grid is shown per field of the inserted/deleted record.

![](../../../../assets/drive/xuE5w_TI2LS9M4nl1fyqWctoD-pU08N6dq7mQJT7qr-wsocs2FehRp7Gu1jGCsJUu_UZeo1hmDjBPQRFV_d1aM26q9zxMjXPX5GbX-SZOJYuZTwo1PYtoD-oi3XRzlyS723rbaWL.png)

Finally, a link just on top of the grid allows switching to the 'Deleted Records' view. Following that link will show deleted records for the tab from which the Audit Trail popup was opened.

### Disable filtering by User

The User filter can be removed from both the 'Record History' and the 'Deleted Records' view. This can be interesting for performance reasons when the number of users available is high. In order to do this, go to General Setup|Application|Preference and add the following preference: Show Audit Trail User filter with value Y.

## The 'Deleted Records' view

This view allows examination of records which have been deleted from a tab and are otherwise no longer accessible in the user interface.

The general layout of the view is similar to the record history view.

An info on the top shows a reference to the entity for which the deleted records are shown. Directly below, a number of filters is available to restrict the records shown.

Then a grid displays all deleted records belonging to this tab/entity. Here one row shown corresponds to a single deleted record and the columns shown are the same as the ones shown in the normal grid view of the same tab.

![](../../../../assets/drive/lsX2HjGHdMbgCKFRs-_KuE1qmeMs2u9cZ5PXrJ5RmYw08PYbdJ6KB_dY93TwaW9ycfaNUc9fEWmsMFKPipMYza0ZCPZdMcl4c9sjFemg7ndkntS2ai5Rs-eePUDaFXXNdKFJ6VOV.png)

This view offers a number of navigation choices to view related or more detailed information.

### Navigation: Back to history

The first one is Back to history. Following this link, the view is just switched back to 'Record History' showing the same records as shown before going to the deleted records view.

### Navigation: History of selected record

The next one, View history of selected deleted record below, allows examining the detailed history of a deleted record, instead of the summary view which is shown here.

This detailed history is displayed in the same 'Record History' view, however its top info area notes the fact that the history of a deleted record is displayed.

The following screenshot shows an example of the history view of the same deleted 'Sales Order' entry. Compared with the previous example of this view, new history entries corresponding to the deletion are shown in addition to the older information about the record creation and modification.

![](../../../../assets/drive/GtW2mnbfKHPPLTLwrt_Kqjlbdm7lo_7CLDntpxMg4vRZnjAaRkOeUzxOg19gnju2DAgUuLBNrm0szABl1MVSV5Ft9_5ASwBs9jTI9IYuQt1iBTBU3r2z5J-octdDlOzNknRzXKKz.png)

### Navigation: Child Tabs

As the last method of navigation, the popup allows filtering records based on a parent record. This can be useful to search for deleted lines belonging to a sales order.

There are two possible ways based on the status of the parent record: still existent or already deleted.

If the parent record (i.e. a Sales Order) does still exist, then the following steps can be done two view its deleted lines:

- Go to the lines tab of the Sales Order
- Click the audit trail icon to open the record history view
- Use the 'Deleted Records' links to switch to deleted records view

As the lines tab is not a top level tab (it has a parent tab Sales Order) the deleted records view is automatically filtered to only show lines belonging to the current Sales Order. As visual information that the information shown is filtered, the top info area shows:

![](../../../../assets/drive/TLPq4qy1yN9UkGD66_5njmuYw_ks8rUXRuOSuS6oXS_BmY92i1kLNyPns4CRsopMKIif0JPp6uJfWpDHgeKgtD07RAR8XcmrVEafUyhiVJ-OEUHhxUF3i77gURAyQPl8yK7PZMLk.png)

If the parent record (i.e. a Sales Order) does not exist anymore, then the same can be accomplished by using the following steps:

- Go to the 'Deleted Records' view of the Sales Order tab
- Search the Sales Order for which the deleted lines should be shown
- Click the _Lines_ link just below the grid

Then the deleted records view will show the deleted lines belonging to the selected (deleted) Sales Order.

## A generated Audit Trail Window

The second interface to view audit data is a normal generated window which is based on the AuditTrail entity, and allows browsing all audit information filtered by the currently active client. Open the Application menu and navigate to General Setup, Security and select Audit Trail.

It offers a raw view of the audit data, meaning that no translation of raw values is done, but instead the raw column values of each change are displayed.

Simultaneously, this window allows a much more flexible filtering/searching.

![](../../../../assets/drive/rw7tPRLbT6ngBKyscK7lPe8F8irNUTp74vKBpDDST539eM5zHpl99Sr2fMXFLMcFks6BVhyNsMfFaSeWHgHYSr2vF2GDYjZ6a5fyAa3Nj2QEcpUhGAL6xOPIVwY177LL6kESljcr.png)

## Limitations

The audit trail feature will record all data changes (for the table for which it has been enabled) with the following exceptions:

- text fields of types (char,varchar) with a length >= 4k will not be audited
- text fields of types (nchar,nvarchar) with a length >= 2k will not be audited
- BLOB fields (binary stored inside the database) will not be audited

## Etendo Advanced Security

The **Etendo Advanced Security** module allows the user to customize several security features such as the following:

- Password Security
- Password History
- User Lockout
- Multiple Session Verification
- Changing Password after Login
- Expiration Time (Autolock Password)

!!! info
    For more information, visit the [Etendo Advanced Security module User Guide](../../../../user-guide/etendo-classic/optional-features/bundles/platform-extensions/etendo-advanced-security.md).

---

This work is a derivative of [General Setup](https://wiki.openbravo.com/wiki/General_Setup){target="_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="_blank"} by [Etendo](https://etendo.software){target="_blank"}.