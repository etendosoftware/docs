---
tags:
  - Etendo Classic
  - Financial Management
  - Accounting
  - General Ledger Report
  - Financial Extensions
---

# General Ledger Report Advanced

:material-menu: `Application` > `Financial Management` > `Accounting` > `Analysis Tools` > `General Ledger Report Advanced`

<iframe width="560" height="315" src="https://www.youtube.com/embed/o5V3Op_qYtE?si=DnTJ77x6zSMZ5KrC" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

!!! info
    To be able to include this functionality, the Financial Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. For more information about the available versions, core compatibility and new features, visit [Financial Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

## Overview

This **General Ledger Advanced** report is an enhanced version of the previous [General Ledger Report](./general-ledger-report.md). Its purpose is to expand the filtering criteria, including all the existing accounting dimensions in the table Accounting Transaction Details.

![](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/general-ledger-report-adv-1.png)

In addition to the previous basic filters: Date from, Date to, From amount, To amount, Organization, General Ledger, From Account, To account, and the previous dimension filters: Business partner, Product and Project, the following were added:

- Activity
- 1st Dimension
- 2nd Dimension
- Sales Region
- Sales Campaign
- Cost Center

Moreover, the Organization filter was added, a filter that combines the original Organization field with the Show Related Operations check, to show intercompany transactions. In each filter, more than one option can be selected.

The new **Show Dimensional Entities** field enables the selection of accounting dimensions to be included in the report.

![](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/general-ledger-report-adv-2.png)

In the Group By menu, the following options are added:

- Activity
- 1st Dimension
- 2nd Dimension
- Sales Region
- Sales Campaign
- Cost Center

It is possible to select the desired accounting dimension for the grouping. When generating the report, the selected dimension appears in the header, indicating the grouping criteria used.

![](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/general-ledger-report-adv-4.png)

## Buttons

In the toolbar, you can find the buttons **View**, **Export to PDF** and **Export to Excel** to generate the report. In the case of the View option, a new window is opened with the corresponding report. In the other cases, the report is exported in PDF or Excel format.

![](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/general-ledger-report-adv-3.png)

!!!warning
    If the View or Export to PDF options are chosen, the limit of dimensions to be included is 4 to avoid visualization issues. This is not the case with Export to Excel, in which case you can choose any number of dimensions.

Also, with this functionality you can navigate to the related journal entry directly from the report. This allows easier and more efficient access to information. By clicking on a journal entry, the user can navigate to the Journal Entries Report window, applying all selected filters.

![](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/general-ledger-report-adv-5.png)

---

This work is a derivative of [Financial Management](http://wiki.openbravo.com/wiki/Financial_Management){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
