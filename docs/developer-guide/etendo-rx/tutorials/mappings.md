---
title: How to create Java Mappings
---
## Objective

The aim of this tutorial is to have a step-by-step guide on how to create a new DAS endpoint modeled with a new data structure. This can be useful, for example, to interact with an external system with a different data structure.

In the following sections, you'll find detailed instructions and examples to achieve this goal.

## Creating a Module

### Module Details

| Property        | Value                          |
|-----------------|--------------------------------|
| Java Package    | com.etendoerp.mapping.tutorial |
| Name            | Mappings Tutorial              |
| Description     | Mappings Tutorial              |
| Version         | 1.0.0                          |
| RX Java Package | com.etendorx.mapping.tutorial  |

## Java Mappings

### Creating a Spring Boot Project

Create a new Spring Boot Project by defining the necessary plugins, dependencies, and tasks:

```groovy
plugins {
    id 'java'
    id 'org.springframework.boot'
    id 'io.spring.dependency-management'
}

group = 'com.etendorx.mapping'
version = '1.0.0'

java {
    sourceCompatibility = '11'
}

ext {
    includeInDasDependencies = true
}

repositories {
    mavenCentral()
}

dependencies {
    implementation 'org.springframework.boot:spring-boot-starter'
    testImplementation 'org.springframework.boot:spring-boot-starter-test'
    compileOnly 'org.projectlombok:lombok:1.18.22'
    annotationProcessor 'org.projectlombok:lombok:1.18.22'
    implementation 'com.fasterxml.jackson.core:jackson-annotations:2.13.3'
    // Das core dependency
    implementation project(':com.etendorx.das_core')
    // Generated source project
    implementation project(':com.etendorx.entities')
}

tasks.named('test') {
    useJUnitPlatform()
}
```

## Implementing Product Attributes

### Defining the Main Class

Here is an example of a Java class that implements DTOReadMapping specialized for the projected entity:

```java
package com.etendorx.mapping.tutorial;

import com.etendorx.entities.mapper.lib.DTOReadMapping;
import org.openbravo.model.common.plm.Product;
import org.openbravo.model.materialmgmt.onhandquantity.StorageDetail;
import org.springframework.stereotype.Component;

import java.math.BigDecimal;

@Component("MAPProductAvailableQuantity") 
public class MAPProductAvailableQuantityReadMapping implements DTOReadMapping<Product> {

  @Override
  public BigDecimal map(Product entity) {
    if(entity.getStorageBin() == null || entity.getStorageBin().getMaterialMgmtStorageDetailList() == null) {
      return null;
    }
    return entity.getStorageBin().getMaterialMgmtStorageDetailList().stream()
        .map(StorageDetail::getQuantityOnHand)
        .findFirst()
        .orElse(null);
  }
}
```

> For more details, go to: [How to Define Java Mappings](docs/developer-guide/etendo-rx/how-to-guides/how-to-define-java-mappings/)
{.is-info}




> Accessing Full Code
> All files are available at [this link](https://bitbucket.org/koodu_software/rx_com.etendorx.mapping.tutorial/src/develop/).
{.is-info}

### Mapping Table

Here is the mapping table for the product attributes:

| Name                      | Qualifier                   | Mapping Type | Table     |
|---------------------------|-----------------------------|--------------|-----------|
| MAPProductAttributes      | Various Qualifiers          | Read         | M_Product |

## Creating a New Projection

### Details

| Property  | Value                      |
|-----------|----------------------------|
| Module    | Mappings Tutorial - 1.0.0 - English (USA)    |
| Name      | map                   |

### Window: Table + Columns

**Search:** M_Product

**New Projections:**

| Projection | Tutorial |
|------------|----------|
| Mapping Type | Read    |

### Field Mapping

Here's a detailed view of the field mapping:

| Field Mapping      | Field Mapping | Java Mapping           | Property               |
|--------------------|---------------|------------------------|------------------------|
| available_quantity | Java Mapping  | MAPProductAvailableQuantity | |
| buying_mode        | Direct mapping |                        | name                   |
| category_id        | Direct mapping |                        | productCategory.name   |
| condition          | Direct mapping |                        | name                   |
| currency_id        | Java Mapping   | MAPProductCurrencyId    |                        |
| listing_type_id    | Direct mapping |                        | name                   |
| pictures           | Java Mapping   | MAPProductPictures      |                        |
| price              | Java Mapping   | MAPProductprice         |                        |
| title              | Direct mapping |                        | name                   |
| attributes         | Java Mapping   | MAPProductAttributes    |                        |
| sale_terms         | Java Mapping   | MAPProductSalesTerms    |                        |
| stocked            | Direct mapping |                        | name                   |

## Generate code

Calling `./gradlew generate.entities` you will have a new endpoint in DAS to get the configured data. This call must be **Module Name** + **Entity Name** , for this example: **MAPProduct**.

## Get new mapped data from DAS

```http
GET /MAPProduct/19857ACFC55D45E2AECAF85B2506C3DB HTTP/1.1
Host: localhost:8092
X-TOKEN: (your token) ...
```

You should have a response like this:

```json
{
    "id": "19857ACFC55D45E2AECAF85B2506C3DB",
    "stocked": "Alquiler de oficina",
    "condition": "Alquiler de oficina",
    "title": "Alquiler de oficina",
    "pictures": [
        {
            "source": "http://mla-s2-p.mlstatic.com/968521-MLA20805195516_072016-O.jpg"
        }
    ],
    "currency_id": "EUR",
    "price": 4000,
    "available_quantity": null,
    "listing_type_id": "Alquiler de oficina",
    "buying_mode": "Alquiler de oficina",
    "sale_terms": [
        {
            "id": "WARRANTY_TYPE",
            "value_name": "Garantía del vendedor"
        },
        {
            "id": "WARRANTY_TIME",
            "value_name": "90 días"
        }
    ],
    "attributes": [
        {
            "id": "BRAND",
            "value_name": "Marca del producto"
        },
        {
            "id": "EAN",
            "value_name": "7898095297749"
        }
    ],
    "category_id": "Others"
}
```

