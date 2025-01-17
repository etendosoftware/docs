---
title: Format XML
tags:
  - Concepts
  - Configuration
  - Numeric Formatting
  - XML Configuration
  - Format Mask
---

# Format XML

## Overview

`Format.xml` is a configuration file for Etendo installation that allows configuring the format output for numeric values. It is used by the different **numeric references** in Application Dictionary, but also can be used in **manual** code. By default, Etendo ships a `Format.xml.template` that can be copied as it is without any modification.

!!!info
    If you are building Etendo from sources, the setup-properties binary makes a copy of it for you.

## Format.xml example

```xml
    <?xml version="1.0" encoding="UTF-8" ?>
    <!-- license -->
    <Formats>
    <!-- other formats -->
       <Number name="euroEdition"
           decimal="." grouping="," formatOutput="#0.00" formatInternal="#0.00" />
    <!-- other formats -->
    </Formats>
```

### Attributes

  * **name**: Name of the format, used to identify it.
  * **decimal**: Symbol (character) to be used as decimal separator.
  * **grouping**: Symbol (character) to be used as grouping separator (used in thousands).
  * **formatOutput**: Format mask used to mask and print numeric inputs. It must be `DecimalFormat` output format type: For more information, see [DecimalFormat](https://docs.oracle.com/javase/tutorial/java/data/numberformat.html){target="\_blank"} class.
  * **formatInternal**: Used internally by `XmlEngine`.

## Application dictionary - format name mapping

| AD Reference     | Output format       |
|------------------|---------------------|
| Decimal, Amount  | `euroEdition`       |
| Quantity         | `qtyEdition`        |
| Price            | `priceEdition`      |
| Integer          | `integerEdition`    |
| Number           | `generalQtyEdition` |
| Others numeric   | `generalQtyEdition` |

## Important Notes

Ultimately, copy `$EtendoERP/config/Format.xml.template` as `Format.xml` and `./gradlew compile.complete -Dtab=xx -Dtr=no` because this way the changes will be permament and will not be lost upon the next rebuild.

## Export to CSV format

The export to CSV functionality uses the `Format.xml` information to format the data (specifically, it uses the decimal separator defined for the system for numeric values).

This can be overwritten in case it is needed, by using the following preferences:

  * **CSV Decimal Separator**: If this preference is defined, this will be used as the decimal separator for numbers.
  * **CSV Field Separator**: If this preference is defined, this will be used as the field separator. Otherwise, a single comma `,` will be used.
  * **CSV Text Encoding**: If this preference is set, this will be used as the encoding type of the generated file. The default encoding used is the Windows iso-8859-1, which will work correctly in Windows environments which use Microsoft Excel. Other popular encodings such as UTF-8 can be used in Linux or Mac environments which use other spreadsheets.

This work is a derivative of [Format xml](http://wiki.openbravo.com/wiki/Format.xml){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.