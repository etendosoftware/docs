---
tags: 
  - Etendo classic
  - platform extensions
  - bundles
  - beta
  - dependency
  - dependency manager
---

# Dependency Manager

## Overview

With this development, the user can have all the available dependencies ... , configure them and check information about versions, validations, etc. 

## Module Management

In this window, the user can see all the java packages to be installed(?) and select the corresponding version in the **versions** tab. Once one of the versions is selected, the dependencies of such version can be found in the **dependencies** subtab.

(Screenshot of the Module Management window)

### Add Dependency 

This button is used to install all the dependecies part of a specific version of the selected module. The popup window shows all the dependencies to be installed.

!!!note
    A warning notification is shown to inform the user about versions compatibility before installing the dependencies shown.

(Screenshot showing the pop up window shown after clicking "add dependency")

Once the process is done, the **Dependency Management** window is opened and all the installed dependencies are shown.

## Dependency Management

In this window, the user can find all the dependencies installed in the previous step.

(Screenshot of the window with one record open so we can show the fields)

Fields to note:

- **Active**: Checkbox
- **Group**: First part of the Javapackage
- **Artifact**: Second part of the Javapackage
- **Version**: Version of the module
- **Format**: 
    - Source:
    - Jar:
    - Local:
- **Installation Status**:
    - Pending download:
    - Installed:
- **Version Status**:
    - Untracked:
    - Update Available:
    - Updated:
- **External Dependency**: Checkbox

### Change Version 

This button is used

### Change Format 

This button is used to change the format of the module. The options are source, jar or local.

- In case the module is originally in local format, the options in the **Change format** popup window are jar or source.

- In case the module is originally in source format, the only option in the **Change format** popup window is jar.

- In case the module is originally in jar format, the only option in the **Change format** popup window is source. In this case, the window shows a warning notification to remind the user that the original directory is deleted once the process is finished.

## Add Local Dependencies 

This process, also part of the Etendo Dependencies Management, is used to add local dependencies to the Dependency Management

## Update Packages Information

Since the information about packages is updated frequently, the user can execute this process to update the list of packages with the latest information.

!!!info
    The same process can be executed from the **Module Management** window, selecting one record and clicking the **Update packages** button.