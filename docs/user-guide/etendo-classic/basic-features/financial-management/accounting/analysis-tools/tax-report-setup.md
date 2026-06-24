---
tags:
  - Etendo Classic
  - Financial Management
  - Accounting
  - Tax Report Setup
  - Financial Reports
---

# Tax Report Setup

:material-menu: `Application` > `Financial Management` > `Accounting` > `Analysis Tools` > `Tax Report Setup`

## Overview

A Tax Report summarizes the tax amounts collected or paid during a period — for example, sales VAT collected or purchase VAT paid. Before generating a Tax Report, define its structure in this window.

## Tax Report Setup

Use this window to create or edit Tax Report definitions. Each definition controls which tax is reported, whether it covers sales or purchases, and how figures are displayed. The following fields define the Tax Report:

![](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/analysis-tools/tax-report-setup/tax-report-setup-1.png)

- **Name:** The name of the Report.
- **Tax:** The tax shown in the report.
- **Sales Transaction:** Checked if it is a Sales Tax Report, unchecked if it is a Purchase Tax Report.
- **Report:** If checked, this Tax Report definition appears in the list on the Create Tax Report form and can be selected for generation. If unchecked, the definition is saved but not available for selection.
- **Shown:** If checked, this tax line appears as a visible row in the report output. If unchecked, the tax line still contributes to calculated totals but the individual row is hidden. Use this when a sub-total should appear without showing every line that feeds into it.
- **Summary Level:** Check this box only if this tax is a grouping category that contains sub-taxes underneath it (for example, a "VAT" parent that groups "VAT 10%" and "VAT 21%"). If the tax stands alone with no sub-taxes, leave this unchecked. If unsure, check the tax structure with your system administrator.
- **Negative:** If checked, the report is printed in negative values; otherwise, it is printed in positive values.
- **Active:** If it is an active Tax Report.

Once the Tax Report is configured, use the [Create Tax Report](create-tax-report.md) form to generate the report.

---

This work is a derivative of [Financial Management](http://wiki.openbravo.com/wiki/Financial_Management){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
