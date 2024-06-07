---
Title: Known Issues
tags:
    - Known Issues
    - Solved Issues
    - Pending Issues
---

## Overview
This page displays the known issues reported by the support team.

## Know Issues

??? success "EPL-1449 Solved"

    ### [EPL-1449](https://github.com/etendosoftware/etendo_backups_script/issues/1){target="\_blank"} Gradle loses execution permissions when doing an etendo-restore.

    #### Workaround

    Apply the following change in the etendo-restore file to ensure that the gradlew file is excluded from the permission change with chmod:

    ``` bash title="etendo-restore"
    - find /opt/EtendoERP -type f -exec chmod 644 '{}' \+
    + find /opt/EtendoERP -type f ! -name gradlew -exec chmod 644 '{}' \+
    ```

    This workaround is applicable if you have deployed Etendo from the ISO in versions prior to [24.1.4](https://etendo-appliances.s3.eu-west-1.amazonaws.com/etendo/iso/etendo-24Q1.4.iso). Starting from that version, the issue of permission changes on the gradlew file is no longer observed.

??? success "EE-856 Solved"

    ### [EE-856](https://github.com/etendosoftware/com.etendoerp.localization.spain.extensions/issues/34){target="\_blank"} 390 Tax Report dataset duplicates data for 2022 when applied on a server migrated from OB to Etendo after 01-2023.

    #### Workaround

    **Warning:** The following workaround can vary depending on diverse factors, such as:

    - Hand-made taxes
    - Hand-made Tax Categories
    - Taxes dataset applied in an organization other than \*
    - Attemps to apply the datasets, previous to doing the workarounds
    - etc

    If you have some of these caracteristics in your environment, contact with the support team for a custom solution

    ---

    There are two ways to solve the problem, depending on how the taxes and temporal taxes datasets have been applied before:


    1. **Temporal Taxes dataset on "individual" organizations, and Taxes dataset at \* level:**  

        1. Execute this SQL script, which will do the following:

            1. Move the taxes from one of the Oraganizations (the first one where the Temporal Taxes dataset was applied) to \*.

            2. Update the taxes from the \* organization and change their application history IDs (an ID to know which tax was applied), to turn them from the Openbravo ones to the Etendo ones.

            3. Update application history IDs for those temporal taxes that have been created on individual organizations, so the dataset importing process does not detect them and does not put data into them.

            [Different Organizations Taxes Fix](../../../assets/whats-new/release-notes/etendo-clasic/known-issues/fix_taxes_ids_different_orgs.sql)

        2. Install Taxes dataset at \* level. The taxes from the \* organization will be updated.

        3. Execute the fix script where the 390 duplication problem is solved.

            [390 Model Tax Reports 2022 Fix](../../../assets/whats-new/release-notes/etendo-clasic/known-issues/fix_localization_spain_390_2022_ids.sql)   

        4. Apply the dataset update for the 390 tax model.
    
    2. **Taxes and Temporal Taxes datasets both applied at \* level:**

        1. Execute the taxes script designed in the issue [EE-808](#ee-808-problem-when-trying-to-import-the-taxes-configuration-for-spain-dataset-if-the-environment-already-has-imported-the-dataset-related-to-the-303-temporary-taxes-of-openbravo).

            [Taxes Fix for Same Organization](../../../assets/whats-new/release-notes/etendo-clasic/known-issues/fix_taxes_ids_same_org.sql)

        2. Execute the fix script where the 390 duplication problem is solved.
        
            [390 Model Tax Reports 2022 Fix](../../../assets/whats-new/release-notes/etendo-clasic/known-issues/fix_localization_spain_390_2022_ids.sql)

        3. Apply the Taxes dataset update for the corresponding organization.

        4. Apply the dataset update for the 390 tax model.

??? success "EE-808 Solved"

    ### [EE-808](https://github.com/etendosoftware/com.etendoerp.localization.spain.extensions/issues/33){target="\_blank"} Problem when trying to import the 'taxes: configuration for Spain' dataset if the environment already has imported the dataset related to the 303 temporary taxes of Openbravo.

    #### Workaround

    **Warning:** The following workaround can vary depending on diverse factors, such as:

    - Hand-made taxes
    - Hand-made Tax Categories
    - Taxes dataset applied in an organization other than \*
    - Attemps to apply the datasets, previous to doing the workarounds
    - etc

    If you have some of these caracteristics in your environment, contact with the support team for a custom solution

    ---

    There are two ways to solve the problem, depending on how the taxes and temporal taxes datasets have been applied before:

    1. **Temporal Taxes dataset on "individual" organizations, and Taxes dataset at \* level:**
    
        1. Execute this SQL script, which will do the following:

            1. Move the taxes from one of the Oraganizations (the first one where the Temporal Taxes dataset was applied) to \*.

            2. Update the taxes from the \* organization and change their application history IDs (an ID to know which tax was applied), to turn them from the Openbravo ones to the Etendo ones.

            3. Update application history IDs for those temporal taxes that have been created on individual organizations, so the dataset importing process does not detect them and does not put data into them.

            [Different Organizations Taxes Fix](../../../assets/whats-new/release-notes/etendo-clasic/known-issues/fix_taxes_ids_different_orgs.sql)
        
        2. Install Taxes dataset at \* level. The taxes from the \* organization will be updated.
    
    2. **Taxes and Temporal Taxes datasets both applied at \* level:**
        1. Execute the following script, which will update the taxes from the \* organization and change their application history IDs (an ID to know which tax was applied), to turn them from the Openbravo ones to the Etendo ones:
        
            [Taxes Fix for Same Organization](../../../assets/whats-new/release-notes/etendo-clasic/known-issues/fix_taxes_ids_same_org.sql)

        2. Install Taxes dataset at \* level. The taxes from the \* organization will be updated.

    The next steps are the same for both cases:

    1. Execute the following script, which will update the 303 model, changing their Openbravo IDs to Etendo IDs.
        
        [303 Model Tax Reports 2023 Fix](../../../assets/whats-new/release-notes/etendo-clasic/known-issues/fix_localization_spain_303_2023_ids.sql)
    
    2. Install 303 model dataset at individual organizations level. The corresponding parameters will be inserted in the taxes from \* organization, each one associated to their specific individual organization.

??? success "EE-758 Solved"

    ### [EE-758](https://github.com/etendosoftware/com.etendoerp.financial.extensions/issues/17){target="\_blank"} Incorrect BP Settlement Module Functionality with Payment (In/Out) Combination and Credit Usage.

    #### Attention

    The combination of Payments (In/Out) with credit usage in the Business Partner Settlement module is currently experiencing issues. Incorrect values for amount and credit used may result in financial account discrepancies. We advise against combining credit usage with settlement until this issue is resolved.

??? success "EPL-858 Solved"

    ### [EPL-858](https://github.com/etendosoftware/com.etendoerp.gradleplugin/issues/34){target="\_blank"} Etendo does not compile with latest version of gradle plugin in JAR format.

    #### Workaround

    Before execute setup tasks in a etendo project in JAR format you must follow the next steps:

    On the source path, open `build.gradle` and locate the 'etendo' block in the file. Inside of it, add the following propertie:

    ``` groovy title="build.gradle" 
    etendo {
        ignoreCoreJarDependency = true
    }
    ```

    This configuration will allow you to download the source of the project on your local environment. It will be needed for following steps. 

    Now we need to execute the command that will download the source code:

    ```bash title='terminal'
    ./gradlew clean
    ./gradlew expandCore 
    ```
    If you don't want to change the `build.gradle`, you can execute the command `./gradlew expandCore` and add the flag `-PforceExpand=true` at the end of it
