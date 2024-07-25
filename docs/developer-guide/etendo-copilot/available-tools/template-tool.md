---
tags:
    - Copilot
    - IA
    - Tool
    - Template
---

# Template Tool

:octicons-package-16: Javapackage: `com.etendoerp.copilot.toolpack`

## Overview

The **Template Tool** is a template for creating new tools in Python-based applications. It is designed to provide a basic structure on which to build custom functionality. The input parameters it accepts are: input1 and input2. The output consists of a message that confirms a predetermined action.

!!!info
    To be able to include this functionality, the Copilot Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. For more information about the available versions, core compatibility and new features, visit [Copilot Extensions - Release notes](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

## Functionality

This tool is useful for developers who want to create new tools quickly following a standard format. It can be used as a starting point to develop specific functions without having to worry about the initial code setup. It provides the user with:

- Standardization: It facilitates the creation of new tools following a standard format, ensuring consistency in development.
- Development Speed: It speeds up the development process by providing a predefined basic structure.
- Flexibility: It allows developers to modify and customize functionality according to the specific needs of their application.

Using this tool consists of the following actions:

- **Processing Arguments**

    It takes input parameters that are in JSON format. If the input is a string, it converts it to a JSON object; if it is already a JSON object, it uses it directly.

- **Accessing Parameters**
    
    It extracts the values of input1 and input2 from the provided JSON object.

- **Personalized Code**
    
    It contains a space where you can add specific code to perform the desired actions using input1 and input2.

- **Returning the Result**

    It returns a message that currently reads `{“message”: “Mail sent successfully”}`, but can be customized according to the action performed.

## Usage Example

Imagine you want to create a tool that adds two numbers together. We would use the Template Tool as follows:
    
- input1: 3
- input2: 5

We can add the necessary code inside the **code here** section to perform the addition:

```
result = p_input1 + p_input2
return {“message”: f “Sum result is {result}”}
```