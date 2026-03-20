---
tags:
  - How to
  - Color System
  - UI
  - Extensibility

status: new
---

# How to Configure Color System Support in the UI

## Overview

The color system in Etendo allows assigning visual identifiers (color badges) to records within a grid or form in the Workspace UI, enhancing the user experience by highlighting key information. This feature uses Etendo's extensibility system and can be applied without modifying the core codebase of the graphical interface.

A common use case is applying it to master tables such as **Product Category** (`M_Product_Category`) or **Business Partner Group** (`C_BP_Group`), as these are frequently referenced in main grids like Products or Customers.

## How the Color System Works

For a color to appear in the UI, the field in the main table must reference a master table via a Foreign Key (**TableDir** or **Table** reference). The Workspace UI and Etendo coordinate through an interaction between the metadata and the React frontend:

1. **Metadata injection**: the backend checks whether the data dictionary has the column configured with the **Color** reference type. If so, it injects `colorFieldName` into the graphical metadata to indicate the property name.
2. **Frontend request**: the data-fetching hooks (Datasource) in Next.js evaluate each defined column. If a column specifies `colorFieldName` metadata, the frontend adds the dependency as `_extraProperties` to the API request (e.g., `_extraProperties=M_Product_Category_ID$EM_SMF_Color`), which instructs the backend to perform the corresponding JOINs and return the color value in the JSON response.
3. **Interface rendering**: when processing cells, the frontend checks for the linked color property and renders a **Tag** badge using the hex value, calculating a text color with adequate contrast.

This architecture ensures efficiency without modifying the standard payload. Color values update in real time in the **Form View**, the **Main Grid View**, and during **Inline Editing**.

## Step-by-Step: Configuring Color in Product Category

The following procedure uses `M_Product_Category` as an example.

### 1. Add the Color Column in the Data Dictionary

1. Access the Etendo ERP Classic environment with the **System Administrator** role.
2. Navigate to the **Tables and Columns** window.
3. Search for the master table — in this case, `M_Product_Category` (Product Category). This is the table **being referenced** by the foreign key (e.g., the table that other tables point to via `M_Product_Category_ID`). The color column must be added here, not in the referencing table.
4. In the **Columns** tab, create a new column using the module prefix (e.g., `EM_CRM_Color` or `EM_SMF_Color`).
5. Assign the **Color** reference type to the new column. This is the key step that allows the system to recognize the column's purpose.
6. Set the length to 7 or 10 characters — sufficient to store a hex code such as `#FF0000`.

!!! note
    Using the **Color** reference type allows the backend to detect the column's purpose independently of its name, integrating it transparently into the metadata read by the frontend.

### 2. Apply Database Changes and Show the Column

1. Apply the changes by compiling the system:

    ```bash title="Terminal"
    ./gradlew smartbuild
    ```

2. Navigate to the **Window, Tab and Field** window in Etendo Classic.
3. Search for the **Product Category** window.
4. In the **Field** tab, check if the new column already appears. If it does not, use the **Create Fields from Application Dictionary** process (available in the tab toolbar) to synchronize the window fields with the updated column definition. This step makes the field visible in the Classic ERP interface.

### 3. Verify the Configuration

1. Open the **Product Category** window in Etendo Classic.
2. Select an existing record (e.g., the category *Standard*).
3. Enter a hex color value in the new field (e.g., `#8E44AD`) and save.
4. Open the Workspace UI and navigate to the **Products** window (`M_Product`).
5. In the products grid, locate the **Product Category** column (`M_Product_Category_ID`).

If the configuration is correct, the **Product Category** value will be rendered as a colored **Tag** badge instead of plain text, using the hex color you assigned in the previous step. The badge will automatically calculate a contrasting text color for readability.

!!! info
    This behavior is module-agnostic and variable-agnostic. Any master table with a column configured with the **Color** reference type is automatically supported across grids and forms without additional development.

## Scope and Restrictions

### Affected Fields

Color badge rendering applies only to **Foreign Key fields (TableDir / Table)** that reference a master table with a color column configured. Examples:

- `M_Product_Category_ID` in the Products table — the reference used throughout this guide.
- Any other foreign key column pointing to a master table that has a column with the **Color** reference type configured.

### Fields Not Affected

This feature does not affect:

- Plain text fields (Strings).
- Numeric, date, or boolean fields.
- Static list dropdowns (*List* reference type) defined in Reference domains.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.
