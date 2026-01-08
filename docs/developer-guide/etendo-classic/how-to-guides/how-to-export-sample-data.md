---
tags:
  - How to
  - Export Sample Data
  - Extensions
  - Etendo Classic
---

# How to Export Sample Data

## Overview

The objective of this document is to explain how the Etendo sample data is exported using the `export.sample.data` task.

## Sample Data Dataset

The tables that will be exported when the `export.sample.data` task is run are included in the Client Definition dataset. You can read more about datasets in [Datasets](../concepts/datasets.md).

!!!note 
    The way the `export.sample.data` task currently works, the SQL Where Clause defined in the dataset tables of the Client Definition dataset will be ignored and replaced by a client filter.

## Exporting the Sample Data

To export the sample data of a given client, this `export.sample.data` gradle task, available from the Etendo root folder must be run. It has the following parameters:

  * Client: The name of the client whose sample data will be exported.
  * Module: The module where the sample.data will be exported. The exported sample data will be stored in the referencedata/sampledata/clientName folder relative to the module path. To export to the core sample data folder, 'org.openbravo' must be specified in the client parameter.
  * ExportFormat (optional): It is used to specify the export format of the sample data. Currently there are two available export formats: xml (the default one) and copy. The copy export format will be only available when exporting the sample data from a PostgreSQL database. Sample data exported with the copy format can only be imported in PostgreSQL databases. If the copy parameter is used in an Oracle environment, a warning message will be shown and the xml format will be used instead.

For instance, to export the sample data of the 'F&B International Group' client to core using the COPY format, the following command must be used:

```bash title="Terminal"
./gradlew export.sample.data -Dclient="F&B International Group" -Dmodule=org.openbravo -DexportFormat=copy
```

For a more detailed info, visit [QA Sample Data Export](../how-to-guides/QA-sampledata-export.md).

---

This work is a derivative of [How to Export Sample Data](http://wiki.openbravo.com/wiki/How_to_export_sample_data){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.