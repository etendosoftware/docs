---
title: User Interface Improvements
tags:
    - New UI
    - Improvements
status: new
---

# User Interface Improvements

## Overview

This section details the user interface improvements available in the **Etendo New UI**.

## Etendo UI Improvements and Enhancements

### Regional Date Formatting

All dates displayed in the user interface now adapt automatically to the regional configuration settings of your browser. This provides a personalized and localized view of date information, making the interface more intuitive and easier to read for users across different regions.

!!! warning

    This regional formatting applies exclusively to the user interface display layer. The underlying data processing follows these rules:

    - **Display/View:** Dates are formatted according to your browser's regional settings
    - **Backend Operations:** Date values are processed and stored using the configuration specified in `gradle.properties`
    - **Dates automatically display in your preferred regional format** without manual configuration.

**Example Etendo Classic UI**

<figure markdown="span">
    ![Etendo Classic Date Format](../../assets/user-guide/newui/classic-date-1.png)
    <figcaption>Etendo Classic UI: Dates in Etendo Classic UI display in the standard format configured in the system.
    </figcaption>
</figure>

**Example Etendo UI with Regional Configuration (en-US):**

<figure markdown="span">
    ![New UI Date Format with Regional Configuration](../../assets/user-guide/newui/newui-date-1.png)
    <figcaption>Etendo UI: In the Etendo UI the same table displays dates automatically formatted. In this example `en-US` (United States) is applied, so dates appear in `MM/DD/YYYY` format. </figcaption>
</figure>

### Attachment Management

The **Etendo UI** introduces a completely redesigned attachment management system that provides a more agile, visual, and comprehensive way to handle file attachments, both from **form view** and directly from **grid records**.

#### Attachments Section in Form View

The attachments section has been redesigned to be more intuitive. Files are now displayed as tags or chips, allowing for quick identification.

![Attachment Section Expanded](../../assets/user-guide/newui/attachment-section-expanded-1.png)

**File Upload**

![Upload Modal Preview](../../assets/user-guide/newui/upload-modal-preview-1.png){align=right width=300}

There are two main ways to upload files within a record:

1. **Drag & Drop:** Drag one or multiple files directly from your computer to the dotted **Drop Zone** in the attachments section.

    !!! note
        When dropping the file, a confirmation modal will open where you can verify the selected file and add an optional description before uploading it.

2. **File Explorer:** Click on the upload zone (or upload icon) to open your operating system's file selector.

#### Preview and Quick Edit

![Upload Modal With File](../../assets/user-guide/newui/upload-modal-with-file-1.png){align=right width=300}

Clicking on any uploaded attachment name will open an advanced preview window.

**Features within the preview:**

- **Integrated Viewer:** View images and PDF documents directly without needing to download them.
- **Description Editing:** You can modify the file description _in place_. Click the **Pencil** icon, edit the text, and save changes with the **Check** icon, all without leaving the preview.
- **Individual Management:** Dedicated buttons to **Download** or **Delete** the file you are viewing.

#### Attachments Bulk Actions

![Bulk Actions](../../assets/user-guide/newui/bulk-actions-1.png)

To facilitate handling multiple files, global action buttons have been incorporated in the attachments section header:

- **Download All:** Generates and downloads a compressed file (`.zip`) containing all attachments associated with the record.
- **Delete All:** Allows you to delete all attachments from the record in a single step (requires security confirmation).

#### Quick Upload from Grid (Drag & Drop on Rows)

It is possible to attach files without needing to enter each record. From the main grid view:

![](../../assets/user-guide/newui/drop-file-in-grid-1.gif)

### Advanced Filters

![](../../assets/user-guide/newui/advanced-filters-modal.png)

The **Advanced Filters** modal is a powerful filtering component that enables users to create complex, multi-condition filters directly from the grid interface. It provides an intuitive way to build sophisticated queries using logical operators and multiple filter groups.

!!! info "Key Features"
    - **Multiple Filter Types:** Support for string, number, date, boolean, and select-type fields.
    - **Logical Operators:** Combine conditions using AND/OR operators.
    - **Filter Groups:** Nest multiple conditions within groups for complex query logic.
    - **Dynamic Operators:** Available operators change based on the field type selected.
    - **Add/Remove Conditions:** Dynamically add or delete individual filter conditions.
    - **Add/Remove Groups:** Create nested filter groups to organize complex logic.
    - **Clear All:** Reset all filters to start fresh.
    - **Apply/Validation:** Only valid conditions (with column, operator, and value) are applied.

#### Supported Operators by Field Type

| Field Type | Supported Operators |
|-----------|---------------------|
| **String** | - `=` Equals<br> - `≠` Not equals<br>Contains<br>Not contains<br>Starts with<br>Ends with<br>Is empty<br>Is not empty |
| **Number** | `=` Equals<br>`≠` Not equals<br>`>` Greater than<br>`<` Less than<br>`≥` Greater or equal<br>`≤` Less or equal |
| **Date** | `=` Equals<br>`≠` Not equals<br>Before<br>After<br>Today<br>This week<br>This month |
| **Boolean** | yes<br>no |
| **Select (Dropdown)** | `=` Equals<br>`≠` Not equals |

#### Using the Advanced Filters

1. **Click the Filter Icon** in the grid header to open the Advanced Filters modal.
2. **Select a Column** from the dropdown in the first filter row.
3. **Choose an Operator** appropriate for the field type.
4. **Enter or Select a Value** based on the operator type.
5. **Add More Conditions** by clicking *Add Condition* button.
6. **Create Filter Groups** for complex logic using *Add Group* button.
7. **Review Your Filters** - The status shows the number of active filters.
8. **Click Apply Filters** button to execute the query.
9. **Clear Filters** by clicking *Clear All* button to reset and start over.

#### Example Scenarios

<figure markdown="span">
    ![Advanced Filters Example 1](../../assets/user-guide/newui/advanced-filters-modal-1-example.png)
    <figcaption>Example 1: Simple filter with one condition selecting a specific organization.</figcaption>
</figure>

<figure markdown="span">
    ![Advanced Filters Example 2](../../assets/user-guide/newui/advanced-filters-modal-2-example.png)
    <figcaption>Example 2: Multiple conditions combined with AND logic to narrow down search results.</figcaption>
</figure>

<figure markdown="span">
    ![Advanced Filters Example 3](../../assets/user-guide/newui/advanced-filters-modal-3-example.png)
    <figcaption>Example 3: Complex filter with a grouped condition. The main filter checks if Document Status is Booked, AND the group checks if Total Gross Amount is either greater than 10 AND less than 100.</figcaption>
</figure>

---

This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"} by [Futit Services S.L](https://etendo.software){target="\_blank"}.
