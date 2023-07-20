---
title: Install Etendo Development Environment
---

## Overview

This section explains how to install a new Etendo environment. It includes:

- A guide for installing Etendo if you are using IntelliJ IDEA Ultimate
- A guide for installing Etendo if you are using IntelliJ Community

## Install Etendo on PC

- [Requirements](/docs.etendo.software/legacy/technical-documentation/etendo-environment/requirements-and-tools/requirements)
- Follow the [Installation Guiede](/docs.etendo.software/legacy/technical-documentation/etendo-environment/setup-and-upgrade/installation)

## How to run Etendo Project in IntelliJ IDEA Ultimate

1.  Open source directory with IntelliJ:

![intellij1.png](/docs.etendo.software/assets/legacy/enduserdocumentation/gettingstarted/intellij1.png)

2.  Open the project. This can be done from the welcome view, from `Open & Import` or from `File` >> `Open`

![intellij2.png](/docs.etendo.software/assets/legacy/enduserdocumentation/gettingstarted/intellij2.png)

3.  The project includes Tomcat configuration. Click on “Add configuration...”

![intellij3.png](/docs.etendo.software/assets/legacy/enduserdocumentation/gettingstarted/intellij3.png)

4.  Select the Tomcat configuration that appears first in the list, check the Tomcat server configuration on your machine, and then click the OK button.

![intellij4.png](/docs.etendo.software/assets/legacy/enduserdocumentation/gettingstarted/intellij4.png)

5.  Run Tomcat or run in development mode.

![intellij5.png](/docs.etendo.software/assets/legacy/enduserdocumentation/gettingstarted/intellij5.png)

## How to run Etendo Project in IntelliJ Community

1.  You can use the Smart Tomcat plugin. To install, go to `File` >> `Settings` >> `Plugins` and search for `“Smart Tomcat”`.

![intellij6.png](/docs.etendo.software/assets/legacy/enduserdocumentation/gettingstarted/intellij6.png)

2.  Download Apache-Tomcat and unzip it.
3.  Go to `Add Configuration` >> `+` >> `Smart Tomcat`. In Tomcat Sever, select the Apache-Tomcat folder. In the same window, set “Tomcat” as the name and change the Context path to the context project name.

![intellij7.png](/docs.etendo.software/assets/legacy/enduserdocumentation/gettingstarted/intellij7.png)

![intellij8.jpeg](/docs.etendo.software/legacy/enduserdocumentation/gettingstarted/intellij8.jpeg)

### Enable Etendo Logs (optional)

1. Open the file `config/ log4j2-web.xml`, find the line `<AppenderRef ref = "Console" />` and uncomment it:

```

<Loggers>
    <Root level="info">
      <AppenderRef ref="RollingFile"/>
      <!-- Add this appender to show log messages in console i.e Eclipse: -->
      <AppenderRef ref="Console"/>  << UNCOMMENT THIS LINE
    </Root>
```

2. Then run `./gradlew smartbuild` and reset the Tomcat.
