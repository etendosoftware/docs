---
title: How to Print Reports with Subreports
tags: 
    - Print
    - Reports
    - Subreports
    - Tree

status: beta
---

#  How to Print Reports with Subreports


!!! example "IMPORTANT: THIS IS A BETA VERSION"
    This page is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**.

##  Overview

In this section, it is explained how to print reports that include subreports.

##  Execution Steps

There are three possible ways to print reports that include subreports:

1. Using the **$P{SUBREP_report_name}** parameter to automatically look for the subreport that will be shown. 

    This option only works on reports that have been processed by using the **Print** button in the **Sales/Purchase Invoice, Sales/Purchase Order, Goods Receipt/Shipment and Payment In/Out** windows. In those cases it is not necessary to include the subreport's .jasper since the .jrxml suffices, because at the time of execution it is being compiled and passed to the main report as a parameter.

2. The next option is defining the .jrxml for a process (in the **Report and Process** window) and then include this process in the menu.

    In this case, the only possible option is using the precompiled subreport (jasper) and refering to it from the .jrxml using `BASE_DESIGN` followed by the jasper path. The main disadvantage of using a precompiled subreports in that it is not translated in runtime so that is only possible to have the subreport in one language.

3. The last possibility is calling **renderJR** from an own java servlet, compiling the .jrxml and passing it as a parameter like described in the first method.
 
    This is done in the **PrintController** class (`PrintController.java`). 

---

This work is a derivative of [How to Print Reports with Subreports](http://wiki.openbravo.com/wiki/How_to_Print_Reports_with_Subreports){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.