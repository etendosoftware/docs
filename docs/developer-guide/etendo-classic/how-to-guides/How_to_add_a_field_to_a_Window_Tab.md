---
tags:
  - Etendo
  - Etendo Classic
  - Customization
  - UI Design
  - Application Dictionary
  - Modules
---

# How to add a field to a Window Tab

## Overview

The objective of this section is to show how you can add a new field to a tab in Etendo Classic.

It is closely related to the previous [How to add Columns to a Table](/developer-guide/etendo-classic/how-to-guides/How_to_add_Columns_to_a_Table/) section which showed how to add new columns to a table.

### Add the fields to the window

The process to add new fields to an existing window is the same as the one to add fields to a new (empty) window. Going to Application Dictionary | Window, Tabs and Fields, we need to search for the _Production Run_ window. Then, for that window, mark its _Incidence_ tab.

![](/assets/developer-guide/etendo-classic/how-to-guides/How_to_add_a_field_to_a_Window_tab_0.png)

Now, we use the Create Fields process on this tab to let it add all columns
of the underlying _MA_WEIncidence_ table to this tab if they have not been previously
added.

This will then add one new field to the tab matching the new column
and automatically place the field into the module.

![](/assets/developer-guide/etendo-classic/how-to-guides/How_to_add_a_field_to_a_Window_tab_1.png)

As a last step, the Synchronize Terminology process should be run to
synchronize our newly added fields to the elements created for the columns
they are based on, so that the UI labels for the new fields get the names
defined in those elements.

If this window should also be used in _classic UI mode_ then now _ant
smartbuild_ should be execute to compile the changed window.

To see the changes in the new UI just switch role away from the _System
Administrator_ role used for this section and go to the changed window to see it
having the new field as the one shown here:

![](/assets/developer-guide/etendo-classic/how-to-guides/How_to_add_a_field_to_a_Window_tab_2.png)

---

This work is a derivative of [How to add a field to a window tab](http://wiki.openbravo.com/wiki/How_to_add_a_field_to_a_Window_Tab){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
