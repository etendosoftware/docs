---
title: User Interface Improvements
tags:
    - New UI
    - Improvements

status: new
---

# User Interface Improvements

## Overview

This section details the user interface improvements available in the New UI.

## UI Improvements and Enhancements

### Regional Date Formatting

All dates displayed in the user interface now adapt automatically to the regional configuration settings of your browser. This provides a personalized and localized view of date information, making the interface more intuitive and easier to read for users across different regions.

!!! warning
    This regional formatting applies exclusively to the user interface display layer. The underlying data processing follows these rules:

- **Display/View:** Dates are formatted according to your browser's regional settings
- **Backend Operations:** Date values are processed and stored using the configuration specified in `gradle.properties`
- **Database Storage:** All date values are persisted in the database using the standard format defined in the application configuration
- **Data Editing/Saving:** When creating or modifying records, dates are internally converted to the configured format before being saved

This dual-layer approach ensures consistency in data storage while providing a user-friendly viewing experience tailored to each user's regional preferences.

**Benefits:**

- Dates automatically display in your preferred regional format without manual configuration.
- Improved readability and intuitive date interpretation for international teams.
- Consistent data integrity and standardized storage across the entire system.
- Seamless experience for users in different geographical locations.

**Example - Table with Regional Date Display:**

<figure markdown="span">
    ![Etendo Classic Date Format](../../assets/user-guide/newui/classic-date.png){ align=left }
    <figcaption>**Etendo Classic:** Dates in Etendo Classic display in the standard format configured in the system.
    </figcaption>
</figure>


**Example - New UI with Regional Configuration (en-US):**


<figure markdown="span">
    ![New UI Date Format with Regional Configuration](../../assets/user-guide/newui/newui-date.png)
    <figcaption>**Etendo Main UI:** In the Etendo Main UI the same table displays dates automatically formatted according to the browser's regional settings. In this example `en-US` (United States) is applied, so dates appear in `MM/DD/YYYY` format. Users in other regions will see their corresponding regional formats, providing a localized and intuitive experience.</figcaption>
</figure>

### Enhanced Attachment Management

The New UI introduces a completely redesigned attachment management system that provides a more agile, visual, and comprehensive way to handle file attachments, both from form view and directly from grid records.

#### Attachments Section in Form View

The attachments section has been redesigned to be more intuitive. Files are now displayed as tags or chips, allowing for quick identification.

![Attachment Section Expanded](../../assets/user-guide/newui/Attachment-section-expanded.png)

**File Upload**

There are two main ways to upload files within a record:

1. **Drag & Drop:** Drag one or multiple files directly from your computer to the dotted "Drop Zone" in the attachments section.
2. **File Explorer:** Click on the upload zone (or upload icon) to open your operating system's file selector.

![Upload Modal Preview](../../assets/user-guide/newui/Upload-Modal-Preview.png)

!!! note
    When dropping the file, a confirmation modal will open where you can verify the selected file and add an optional description before uploading it.

![Upload Modal With File](../../assets/user-guide/newui/Upload-Modal-With-File.png)

**Import from URL**

The option to attach external resources via a link is included using the "Import from URL" button (*functionality subject to configuration*).

#### Preview and Quick Edit

Clicking on any uploaded attachment name will open an advanced preview window.

**Features within the preview:**

- **Integrated Viewer:** View images and PDF documents directly without needing to download them.
- **Description Editing:** You can modify the file description "in place". Click the **Pencil** icon, edit the text, and save changes with the **Check** icon, all without leaving the preview.
- **Individual Management:** Dedicated buttons to **Download** or **Delete** the file you are viewing.

#### Bulk Actions

To facilitate handling multiple files, global action buttons have been incorporated in the attachments section header:

- **Download All:** Generates and downloads a compressed file (.zip) containing all attachments associated with the record.
- **Delete All:** Allows you to delete all attachments from the record in a single step (requires security confirmation).

![Bulk Actions](../../assets/user-guide/newui/Bulk-Actions.png)

#### Quick Upload from Grid (Drag & Drop on Rows)

It is now possible to attach files without needing to enter each record. From the main table/grid view:

1. Select a file on your computer.
2. Drag it over the desired record row.
3. The row will highlight indicating it is a valid target.
4. When dropped, the file will be automatically attached to that record.

![Drop File in Grid](../../assets/user-guide/newui/Drop-File-in-Grid.gif)



