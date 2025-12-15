---
title: How to Change Fonts in Etendo Reports
tags:
    - Etendo reports
    - Custom fonts
    - JasperReports
    - Report Customization

status: beta
---

# How to Change Fonts in Etendo Reports
 
!!! example  "IMPORTANT: THIS IS A BETA VERSION"
    It is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**.

## Overview

This section explains how to **change the fonts** used in Etendo reports. Updating the default fonts can be useful in two main scenarios: enhancing the visual appearance of the reports with more readable or brand-aligned **typography**, or ensuring proper display of **languages** whose characters are not supported by the standard font set, such as Japanese, Arabic, or Vietnamese. Replacing the default fonts with ones that support the required character sets allows the reports to render correctly across different languages.

!!!info
    For more information visit, [How to Create a Module](../how-to-guides/how-to-create-a-module.md) and [How to Create a Report](../how-to-guides/how-to-create-a-report.md). 

Etendo uses **Jasper Reports** tool to create reports:


## Changing the font in Jasper Reports

When changing the font in **Jasper Reports** the software [Jaspersoft Studio](https://community.jaspersoft.com/download-jaspersoft/){target="\_blank"} will be very helpful.

In the above  link, find a detailed tutorial that describes **how to handle** custom fonts in Jaspersoft Studio. In short, these are the steps to carry out:

1. Get the desired `font's .ttf` file from the pc or from the Internet. 
2. Create the Font Extension, go to **Preferences window**.

    ![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-change-fonts-in-etendo-reports/how-to-change-fonts-in-Etendo-reports-0.png)

3. Click on `JasperSoft Studio > Fonts`. Click **Add** . At this point provide a unique name for the Font Extension and the path to its extension by selecting the path of the downloaded `.ttf file`. 
4. Once done, set a PDF Encoding type for the new font in the wizard. 
5. Change the **fontName** and **pdfFontName** used in the text fields wanted to have being displayed with the new font in our report. Accomplish that by either using Jaspersoft Studio or making changes directly in the `.jrxml` file using a text editor. 
6. And, for the document(s), do not forget to to choose the same PDF Encoding type as the one set for the font in step 4. 
7. Export the font into a `.jar` file. Once again, Jaspersoft Studio can lend us a hand with doing this: Go to `JasperSoft Studio > Fonts` and this time click **Export** . Select the font and export it into a `.jar` file. 
8. Create a new module to keep the `.jar` file. Inside the module folder, create a subfolder `/lib/runtime` and put the exported `.jar` file in there. 

    ![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-change-fonts-in-etendo-reports/how-to-change-fonts-in-Etendo-reports-1.png)

9. Stop tomcat.
10. Execute `./gradlew smartbuild`
11. Restart tomcat. 

## Result

The following screenshots show the results after successfully carrying out the steps mentioned above:

 **Jasper Report** where the font of the title has been replaced with another font:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-change-fonts-in-etendo-reports/how-to-change-fonts-in-Etendo-reports-2.png)
  
---
This work is a derivative of [How to Change Fonts in Openbravo Reports](http://wiki.openbravo.com/wiki/How_to_Change_Fonts_in_Openbravo_Reports){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}. 

