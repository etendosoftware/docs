## Navigation 

To get to a window, type a part of its name in the **Create New button** or the **Quick Launch button**. Etendo also offers a tree menu for easy discovery.

### Quick Launch

!!! info
    For more information about Quick Launch functionalities, see the Quick Menu section in the Top Navigation Bar section.


### Application menu tree structure

The Application menu is used to make all the application elements accessible to the user. Also, the last three searches are shown in this window.

![Application menu navigation](../../assets/getting-started/user-interface/navigation/application-menu.png)

#### Icon references

There are different types of menu items which are identified with different icons:

|     |     |
| --- | --- |
| ![](../../assets/getting-started/user-interface/navigation/icon-folder.png) | Folders are used to organize other items within them. They can be expanded or collapsed to show their contents by clicking them. |
| ![](../../assets/getting-started/user-interface/navigation/icon-report.png) | Reports explode information from Etendo Classic. |
| ![](../../assets/getting-started/user-interface/navigation/icon-process.png) | Processes allow complex operations to be performed. Some examples would be to import data from a file or the automatic creation of invoices from purchase orders. |
| ![](../../assets/getting-started/user-interface/navigation/icon-window.png) | Windows allow the user to create, modify or query records. By records, it is meant any entity that has its own data within Etendo Classic, such as a product, an order, an invoice, etc. |

## Application Areas 

Etendo is split into different application areas. Each area is represented by a separate folder accessible from the Application menu in **the top navigation** screen area.

### Window structure

The Toolbar contains action buttons and process buttons. Action buttons are generic and can be applied to almost all selected records.  Process buttons are record specific and depend on the record status and the active level (header or lines or lower).

![Window structure](../../assets/getting-started/user-interface/navigation/window-structure.png)

|     |     |
| --- | --- |
| 1   | Action buttons |
| 2   | Process buttons |

### Buttons

The action buttons perform the following actions:   
 

|     |     |
| --- | --- |
| ![Create new record](../../assets/getting-started/user-interface/navigation/btn-create-new-record.png) | Create a new record in a form
| ![Insert new row](../../assets/getting-started/user-interface/navigation/btn-insert-new-row.png) | Insert a new row in grid view
| ![Save your changes](../../assets/getting-started/user-interface/navigation/btn-save.png) | Save your changes in the database
| ![Close current record](../../assets/getting-started/user-interface/navigation/btn-close-record.png) | Close the current record and return to grid view
| ![Cancel changes](../../assets/getting-started/user-interface/navigation/btn-cancel.png) | Cancel changes and return to last saved state
| ![Delete current record](../../assets/getting-started/user-interface/navigation/btn-delete.png) | Delete the current selected record(s) from the database |
| ![Refresh current data](../../assets/getting-started/user-interface/navigation/btn-refresh.png) | Refresh the current data from the database
| ![Export to spreadsheet](../../assets/getting-started/user-interface/navigation/btn-export-spreadsheet.png) | Export to spreadsheet
| ![Upload new attachment](../../assets/getting-started/user-interface/navigation/btn-upload-attachment.png) | Upload new attachment
| ![Copy record](../../assets/getting-started/user-interface/navigation/btn-copy-record.png) | Copy record
| ![Print record](../../assets/getting-started/user-interface/navigation/btn-print.png) | Print record
| ![Send email](../../assets/getting-started/user-interface/navigation/btn-email.png) | Email
| ![Show audit trail](../../assets/getting-started/user-interface/navigation/btn-audit-trail.png) | Show audit trail
| ![Get a direct link](../../assets/getting-started/user-interface/navigation/btn-direct-link.png) | Get a direct link to this view or record
| ![Form personalization](../../assets/getting-started/user-interface/navigation/btn-form-personalization.png) | Form personalization
| ![Save view](../../assets/getting-started/user-interface/navigation/btn-save-view.png) | Save view |.png
| ![Show table and form](../../assets/getting-started/user-interface/navigation/btn-table-and-form.png) | Show table and form |.png

#### Email

Clicking the **Email** button opens the **Email Options** popup, which allows sending an email directly from the current document to the business partner's contact.

![Email popup](../../assets/getting-started/user-interface/navigation/email-popup.png)

The popup contains the following fields:

- **From**: The sender email address, populated automatically based on the system email configuration. Read-only.
- **To**: Editable text field for the recipient's email address. Includes a **Select recipient** button that opens a contact selector to pick from the business partner's contacts. When multiple contacts exist, the system preloads the email using the following order:
    1. The contact marked as **Default** in the Contact tab of the Business Partner window.
    2. If no Default contact exists, the last modified contact in the list.
- **Subject**: Subject line of the email.
- **CC**: Additional recipients to copy on the email.
- **BCC**: Recipients copied without being visible to others.
- **Reply-to**: Email address where replies will be directed if different from the From address.
- **Message Body**: Free-text body of the email. The following references can be used and will be automatically replaced with the document values when sending:

    | Reference | Description |
    | --- | --- |
    | `@cus_ref@` | The reference of the customer |
    | `@our_ref@` | The reference of the document |
    | `@cus_nam@` | The name of the customer |
    | `@sal_nam@` | The name of the sales rep. |
    | `@bp_nam@` | The Business Partner name |
    | `@doc_date@` | The document date |
    | `@doc_desc@` | The document description |
    | `@doc_nextduedate@` | The next due date (if any) |
    | `@doc_lastduedate@` | The last due date (if any) |

- **Template to use**: Dropdown to select a predefined email template, which will populate the subject and body automatically.
- **Attached Documents**: Lists the documents already attached to the record. Each attachment can be optionally archived. Additional files can be attached using the **Add Attachment** button.

!!! tip
    To ensure the correct recipient is preloaded automatically, mark the desired contact as **Default** in the Contact tab of the Business Partner window.

Multiple recipients can be added in the **To**, **CC**, and **BCC** fields by separating email addresses with `;` or `,`. The system validates all addresses before sending — if any is invalid, the send action is blocked and a validation message is displayed.

---
This work is a derivative of [User Interface Introduction](http://wiki.openbravo.com/wiki/User_Interface_Introduction){target="_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="_blank"} by [Etendo](https://etendo.software){target="_blank"}.