---
title: How to create Java Mappings
---

## Objective

The aim of this guide is to walk you through the process of defining a new Java mapping, a powerful tool used to transform data structures. Specifically, you'll learn how to create a Java class to map a field within a predefined entity into a new structure, suitable for use in REST services exposed by the DAS service.

## Theory

### Requirements

To create a Java mapping, you'll need a new Java class located in your module's Java package. Here's what you need to know:

- **Interface Implementation**: The class must implement the `DTOReadMapping` interface. Since this interface is a Java generic, you must specify the particular entity that the new Java class extends.
- **Return Type**: While the `map` method by default returns an `Object`, it's advised to specify the particular data type to return. This can be any Java class that can be serialized to a JSON object, whether simple or composed.
- **Qualifier**: As this class is automatically instantiated and injected, you must specify a unique string as a qualifier for later reference in the configuration.

### Mapping Definitions

The following table attributes must be defined:

| Name         | Qualifier                | Mapping Type | Table           |
|--------------|--------------------------|--------------|-----------------|
| (Mapping Name) | (Unique Identifier)     | Read / Write | (DB Object Type)|

- **Name**: The name of the Java mapping, used for reference and easy configuration.
- **Qualifier**: A unique string to identify the object in injection.
- **Mapping Type**: Specify a different Java class for read and write operations. 'Read' exposes data in the required format (GET request), while 'Write' is used when the DAS service receives data (POST, PUT).
- **Table**: The database object mapped in the class.

### Example: Defining the Main Class

Here's an example of a Java class implementing `DTOReadMapping` specialized for the Product entity:

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

#### Using Spring Boot Qualifier

The `@Component` annotation is used as a Spring Boot qualifier to define the unique identifier:

```java
@Component("MAPProductAvailableQuantity")
```

#### Customizing Return Types

You can customize the return type. For example, to return a BigDecimal:

```java
@Override
public BigDecimal map(Product entity) {
  // Code Implementation
  return BigDecimal.ZERO;
}
```

Or, you can return a POJO annotated with Jackson:

```java
@Getter
@Setter
@AllArgsConstructor
public class MAPProductAttributes {
  @JsonProperty("id") String id;
  @JsonProperty("value_name") String valueName;
}

@Override
public Iterable<MAPProductAttributes> map(Product entity) {
  // Code Implementation
}
```

### Mapping Table in Etendo Classic

As a System Administrator in Etendo Classic, you must define the mapping table. For example, as a Product attribute:

| Name                     | Qualifier               | Mapping Type | Table      |
|--------------------------|-------------------------|--------------|------------|
| MAPProductAttributes     | Various Qualifiers      | Read         | M_Product  |

This comprehensive guide should provide you with the foundation needed to define and work with Java mappings in your projects.
