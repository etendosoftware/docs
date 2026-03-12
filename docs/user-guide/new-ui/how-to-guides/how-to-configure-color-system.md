---
tags:
  - How to
  - Color System
  - UI
  - Extensibility
---

# How to Configure Color System Support in the UI

## Overview

The color system in Etendo allows you to assign visual identifiers (color badges) to records within a grid or form in the Workspace UI, enhancing the user experience by highlighting key information. This feature leverages Etendo's extensibility system, allowing it to be applied transparently without altering the core codebase of the graphical interface.

An excellent (and highly visual) use case is applying it to master tables such as the **Product Category (M_Product_Category)** or **Business Partner Group (C_BP_Group)**, as these are heavily used within main grids (like the Products or Customers grid).

## How does the relationship work?

For the color to be reflected in the UI, the field in question within the main table must point to a master table via a Foreign Key (**TableDir** or **Table** Reference).

The current implementation in Workspace UI and Etendo works in coordination through an interaction between the metadata and the React frontend:

1. **Metadata Injection:** The backend determines if a child table needs a color by checking if the table it points to has a property following a naming convention that implies a color. If so, it injects `colorFieldName` as the field metadata at the dictionary level.
2. **Frontend Request:** The data fetching hooks (Datasource) in NextJS actively evaluate each defined column. If any column specifies the `colorFieldName` metadata, the frontend adds this requested dependency on the fly as `_extraProperties` to the API Request (e.g., `_extraProperties=M_Product_Category_ID$EM_SMF_Color`). This forces the backend to perform the corresponding JOINs and dump the final color value into the JSON response.
3. **Dynamic Interface Detection:** When rendering the cells, the frontend is completely agnostic and independent. It scans all the *keys* of the fetched records and if any key dynamically contains the word `color` (or similar variables like `smfcolor`), it automatically assigns the visual component in the form of a wrapped 'Tag', using the recovered hex value, its prefix, and deducting a text with good contrast.

This explicit architecture ensures efficiency without corrupting the standard payload. Similarly, it updates in real time in the **Form View**, the **Main Grid View**, and when mutating information via **Inline Editing** (where the client fetches the record again requesting the color `_extraProperties` upon successful save).

## Step-by-Step: Configuring Color in Product Category

Below is the exact procedure to test and implement this easily using the `M_Product_Category` table as an example:

### 1. Add the Color column in the Data Dictionary

1. Log into your **Etendo ERP Classic** environment with the **System Administrator** role.
2. Go to the **Tables and Columns** window.
3. Search for the master table of interest, in this case, `M_Product_Category` (Product Category).
4. On the *Columns* tab, create a new column using your module prefix (for example, `EM_CRM_Color`, `EM_SMF_Color`, or your active testing module prefix).
5. Configure it as a **String** type with a length of 7 or 10 characters—enough to store a hex code like `#FF0000`.

!!!note "Key Note"
      Thanks to the resolution logic between the metadata and how our Frontend evaluates the JSON keys when rendering ([extractColorContext]), Etendo will auto-assign to the palette any variable whose naming convention includes the "color" word suffix.

### 2. Apply DB changes and show the column in the window

After defining the column in the data dictionary, you must materialize it in your database:
1. Apply the changes compiling the system via console (e.g., `gradlew smartbuild` or rebuilding the database appropriately).
2. Navigate to the **Window, Tab and Field** window within the Etendo environment.
3. Search for the corresponding window, in this case, **Product Category**.
4. Make sure to reload the tab or manually add/create the corresponding record in the **Field** tab for the new column, allowing it to appear in the classic ERP interface ready for use.

### 3. The Visual Test (The Visual Magic!)

1. Open the **Product Category** window in Etendo Classic.
2. Select an existing record, for example, the category titled "Standard" (or whichever you decide to use).
3. Write an identifying and eye-catching hexadecimal value in the new assigned color field. For example: `#8E44AD` (a dark purple color), and hit save on the record.
4. Now, go to the **NextJS frontend of Workspace UI**.
5. Open the respective main window for **Products** (`M_Product`).
6. In the resulting products grid, search for the "Product Category" column (`M_Product_Category_ID`).
7. **Surprise!** If this category normally appeared as simple blue text detailing "Standard", you'll now witness an appealing change. When requesting the data, the frontend will detect the configuration to request metadata for that color (`_extraProperties`) and inject the request. The database will process it in its JOINs, Workspace will capture the "color" key for that column, and it will end up painting it in a beautiful rounded purple badge.

The brilliance of this design is that everything is **completely module-agnostic**. You can create independent modules for your clients, adding exactly the same tracking variables referred to as `EM_Client_Color` to tables such as Currencies, Payment Methods, Sales Representatives, or Warehouses... and they will instantly pop up colored across the grid and form in the UI without needing a single additional *if* programmed on the frontend visual side.

## Scope and Restrictions

### What fields are affected?

The dynamic logic for metadata injection and color badge rendering **only affects fields defined as Foreign Keys (TableDir / Table)** targeting a master table that already has the color column configured. Some concise examples include:

* `M_Product_Category_ID` pointing in the Products table.
* `Priority_ID` reflecting in the Tasks table.
* `C_Currency_ID` translating to the Invoices table.

### What is NOT affected?

This current control mechanism **DOES NOT affect or interfere with**:

* Regular and simple static text fields (Strings).
* Numbers, Dates, or Boolean values.
* Hardcoded static lists in the dictionary (Dropdowns of type *List* defined fixedly within Reference lists domains in the system).

---
