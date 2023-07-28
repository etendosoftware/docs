---
title: Financial Management - Assets
---
## Overview

This section describes the windows related to assets, part of the Financial Management in Etendo. These are:

- Assets
- Asset Group
- Amortization
- Amortization Report


## **Assets**

### **Introduction**

The user can define amortization characteristics for assets owned by the company.

#### **Assets**

The user can define assets owned by the company and create an amortization for them.

![](/docs.etendo.software/assets/drive/1SggpQOnJ2aCqlJS7Ds8KulWXK1pCaoKR.png)

Fields to note:

-   **Organization** : Organizational entity within client.
-   **Search Key** : A fast method for finding a particular record.
-   **Name** : A non-unique identifier for a record/document often used as a search tool.
-   **Asset Category** : A classification of assets based on similar characteristics.
-   **Document No.** : An automatically generated identifier for all documents.
-   **Description** : A space to write additional related information.
-   **Currency** : An accepted medium of monetary exchange that may vary across countries.
-   **Product** : An item produced by a process.
-   **Summary Level** : A means of grouping fields in order to view or hide additional information.
-   **Static** : Prevents from moving the record into the tree
-   **Depreciate** : The asset is used internally and will be depreciated
-   **Depreciation Type** : Depreciation Type
-   **Calculate Type** : Calculate type
-   **Annual Depreciation %** : Depreciation annual %
-   **Amortize** : Asset schedule
-   **Usable Life - Years** : Years of the usable life of the asset
-   **Usable Life - Months** : Months of the usable life of the asset
-   **Every Month Is 30 Day** : When calculating the amortization plan every month will be considered as a 30 day month and years of 365 days (no leap-years).
-   **Purchase Date** : Purchase date
-   **Cancellation Date** : Cancellation date
-   **Depreciation Start Date** : Depreciation Start Date. The amortization plan will be calculated starting from this date.
-   **Depreciation End Date** : Depreciation end date
-   **Asset Value** : Asset value
-   **Residual Asset Value** : Residual asset value amount
-   **Depreciation Amt.** : Depreciation Amount
-   **Previously Depreciated Amt.** : This amount is subtracted to the Depreciation amount when calculating the amortization plan. Total amount to be depreciated = Depreciation Amount - Previously Depreciated Amount
-   **Depreciated Value** : Depreciated value
-   **Project** : Identifier of a project defined within the Project & Service Management module.
-   **Create Amortization** : it will create (or recalculate) the amortization plan based on the asset definition.

### **Asset Amortization**

The user can add asset amortizations for a selected asset.

![](/docs.etendo.software/assets/drive/167vATAwJuJhpPE2by-QgZN1_jyrDsyWZ.png)

-   **Line No.** : A line stating the position of this request in the document.
-   **Amortization** : The depreciation or reduction of a product value over time.
-   **Amortization Percentage** : Amortization Percentage
-   **Amortization Amount** : Amortization Amount
-   **Currency** : An accepted medium of monetary exchange that may vary across countries.

The *Create Amortization* process populates the Asset Amortization tab.

The Asset Amortization tab shows the depreciation plan of the asset based on its usable life-time and its value that is the amount to be depreciated. The asset value is split within its usable life (months or years), therefore each depreciation plan line represents a percentage of the total depreciation amount of the asset.

It is important to remark that the proposed depreciation plan lines can be manually removed whenever they are not processed and posted. In that case, the create amortization process can be executed once again, therefore the depreciation plan is recalculated. This is very useful in those cases where the value of an asset changes or the usable life-time of an asset changes once its depreciation has started.

There is a restriction though, when removing lines, if the user plans to click the Recalculate Amortization button afterwards. The lines must be removed always starting from the latest one and without leaving undeleted lines in between. For example, having amortization lines such as:

-   Line 10 - January depreciation plan line
-   Line 20 - February depreciation plan line
-   Line 30 - March depreciation plan line

The depreciation line of February cannot be removed until the depreciation line of March is removed.

The process assumes that if the March depreciation line exists, then the February depreciation line exists.

#### **Accounting**

The user can create and edit G/L accounts to be used in transactions which include a selected asset.

![](/docs.etendo.software/assets/drive/1huSwZWBa8W1gwPd3rvluydFF5jNOMU2k.png)

## **Asset Group**

### **Introduction**

Assets can be grouped into different categories with the aim of helping their depreciation management and analysis.

#### **Asset Category**

Asset category window allows the user to create and configure every asset category your organization may need.

![](/docs.etendo.software/assets/drive/17CmG5FAA86HDWLrAmjuHIgpNsdwAn_ya.png)

As shown in the image above, the creation of an asset category requires the user to enter below listed information for each category:

-   **Name** or short name which helps to easily find a category
-   **Description**
-   **Depreciate** indicates if the assets of this group will be depreciated.
-   **Depreciation Type** method used to depreciate the asset.
-   **Calculate Type** indicates how the depreciation will be calculated (Time or Percentage)
-   **Annual Depreciation** Annual percentage used to depreciate this asset.
-   **Amortize** it refers to the periods chosen between depreciation entries (monthly, yearly).
-   **Usable Life - Months** Years of the usable life of the asset
-   **Usable Life - Years** Months of the usable life of the asset

Depreciation configuration will be inherited from the asset category when creating a new asset.

#### **Accounting**

Each asset category allows the user to configure a different set of accounts to use to post asset depreciation.

![](/docs.etendo.software/assets/drive/1jZl_RGgZw2i1Ogq4d1D-fhNcd59AI6ev.png)

## **Amortization**

### **Introduction**

The user can create and edit amortization for a selected year.

### **Header**

In the header, the user creates amortizations for particular periods.

![](/docs.etendo.software/assets/drive/1w9ObbOLgqEa3WC4p5N5wW4C1HSl1gBPk.png)

### **Lines**

In each line, the user adds amortized assets and details of amortization.

![](/docs.etendo.software/assets/drive/1meY53s5Ivsbk_i6wd1TY7ZNPv9JIF258.png)

#### **Accounting**

Accounting information related to the amortization

![](/docs.etendo.software/assets/drive/15yAiipNMuH7eorzPtiPFAQOpqpm78P-o.png)

### How to Reactivate Amortizations

!!! info
    To be able to include this functionality, the Financial Extensions Bundle must be installed. To do that, follow the instructions from the [marketplace](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558).

Etendo allows multiple amortizations to be processed and unprocessed. This process is available for amortizations which share the same status. The status of the amortization can be seen in the status bar.  

![](/docs.etendo.software/assets/drive/1je7Yl7FTqlDAhFlb8wTQKBDUF3pSn0Qu.png)

### Bulk Posting

!!! info
    To be able to include this functionality, the Financial Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558)

The Bulk Posting functionality allows the user to post or unpost multiple records by selecting the corresponding records and clicking the “Bulk posting” button.

Also, the Accounting Status of the record/s is shown in the status bar, in form view, or in a column, in grid view.
> 
!!! info
    For more information, visit [Bulk Posting](https://docs.etendo.software/en/modules/financial-extensions-bundle#bulk-posting) in the Financial Extensions Bundle Documentation.


## Amortization Report

!!! info
    To be able to include this functionality, the Platform Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Platform Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=5AE4A287F2584210876230321FBEE614)



The new Amortization report allows downloading excel reports. The report can be found in Financial Management > Assets > Analysis Tools > Asset Amortization Report. 

![](/docs.etendo.software/assets/drive/FCyjH9Cqjoxlpce_Q2Adrf0qcnEwMumykLuNZ5DvkPgw5L1GNfFz4EDeMvEQzQ4ud9ZTFjcAk-1Y0l45vCDs1ONk0KMn-TzkhKKAEL17m3fV85B2lbrmxRnIhAM4-R1zOqVfr8sU_3AoWConwvRkI4I.png)

This report allows filtering by organization, date, asset or any particular description, category and general ledger configuration.  

![](/docs.etendo.software/assets/drive/v044uU7hYLEk9gHyJ_rQT4PafeiO44KV81IWajtztUpPd9hLqZiPs9ivfPP69HxfwwK-35rPk_nzpLHsSXeXpUUfVDnFw7k4jsQ4AvDJIwDMCPWrsiRDyLPKgLCb0WDOB4GPZVU2urwKJ3sq1BhSXnA.png)

Once the information is filtered, an excel sheet is downloaded as shown in the following image:

![](/docs.etendo.software/assets/drive/X4RYGKFzkl-VVrKXiztozXKKOQIFqIwXJMgUUeLzdGESddbVChKWbf6L2XnMO1aQg2wCfXit-Tw-w3TXDP_FLWBluY08K6JG6kHf_w2Mz5fRWBfzbbfV6edBbPzULPPPWxAALvtVBmxhKLtC_DwAzgg.png)

This report takes into account the amortization lines of each Asset. That is to say, the report will still be generated even if the amortization lines are not processed or posted. 

It is necessary to filter by date since the information comes out over this filtering. That is, the accumulated period, net value and subsequent report fields will depend on this filtering.

For example: Period date filtered 01-01-2022 and 31-12-2022

**Period:** The total of the amortization lines between 01/01/2022 and 12/31/2022 will be shown.
**Accumulated:** The sum of the amortization lines between 01/01/2022 and 12/31/2022 and the total amortization lines prior to 01/01/2022 will be shown. 
**Net Value:** The Asset value minus the Accumulated field will be shown. 
**After:** The amortization lines after 31-12-2022 will be shown. 

!!! info
    When the end date within the Assets window is filled in, that Asset will not appear in the report if the filtered date is after the end date of the Asset.


