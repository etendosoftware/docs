---
title: How to Copy and Paste Images in Etendo
tags:
    - How to
    - Copy Images
    - Paste Images
    - Rich Text
    - Base64
---
## Copy and Paste Images in Etendo

### Overview

This section explains how to use rich text areas to save images in Etendo.

### How to include images with rich text areas

First, the user must define a column in the database where the corresponding image is saved.

!!! info
    To do this, it is important to remember that this column must have the enough size to store a codified image in base64 format. For example: a 2 MB image contains 3 million characters.


![](../../../assets/drive/wO0NOA64kTnYqRjQ8KTrcBJiMmq2AGvuS6oYHOQ75hZ13OvUYgFkAK2S7iE-SGeRh5PcE5eNA8rgbpzg0LwgGGh-R4fk1yHCI9orYLKJJXDD9noH4K0ernCNFMkZCKBo_4owHCPkqrpxgOcFN2NjHMI0NchPj0r1VminCsMvbp0begvcFdO8FI8DjE5jAA.png)

Once the column is defined, the user must log in with the System Administrator role, go to Application Dictionary | Windows, Tables and Columns, find the corresponding table, in our case “product” and create columns from the database with the “Create column from DB” button. 

In the recently created column, the reference “rich text area” must be selected. 

Also, a field for the corresponding image must be created. 

Finally, it is necessary to compile executing:

```bash title="Terminal"
./gradlew smartbuild
```


![](../../../assets/drive/zd0NYsbcmx0ehnHRsCxb21zazxL6sYuBxqjAOoH74QmK1CTccI-dDyqzmMrTiJDrusrcdifTRiiCPPomRAdduh1LipsA2FHTP84kstjAI8SwL3a7-DkSSmCqbVYsyXF_d1El8Z9QqPqphc4oqIB-wFYadh3OODSzp8QCHSyGBAGZSX8OczGKNApmreM8eg.png)

As seen in the image above, the “image” field was created, in which it is possible to paste content to store in base64 format in the database. In this way, this information is available for later.