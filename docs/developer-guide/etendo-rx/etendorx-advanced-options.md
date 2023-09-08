---
title: EtendoRX Advanced options
---

## EtendoRX Advanced options

#### Generation of entities

- To generate the entities run

`./gradlew generate.entities --info`

!!! info
    The properties will be taken from the 'gradle.properties' file.

- Gradle command line parameters
  - `-Pgenerate=<true-false> ` Specifies if the generation of the 'metadata.json' files should be generated automatically (Requires the 'com.etendoerp.etendorx' module installed). If the value does not match with 'true' then is evaluated as false. By default the generation is always true.
  - `-PexcludedModules=<modules>` A comma separated list of modules to exclude from the 'metadata.json' generation
  - `-PincludedModules=<modules>` A comma separated list of modules to include in the generation of the 'metadata.json'

```
Examples:
Omiting the generation of the 'metadata.json'
> ./gradlew generate.entities -Pgenerate=false --info

Excluding modules in the generation of the 'metadata.json'
> ./gradlew generate.entities -PexcludedModules=com.etendoerp.module1,com.etendoerp.module2 --info

Specifing the only modules to generate the 'metadata.json'
> ./gradlew generate.entities PincludedModules=com.etendoerp.module1,com.etendoerp.module2 --info
```

- Debug mode

`./gradlew generate.entities --info -Pdebug=true`

Optional command line parameters

`'-Pport=<port number>' Specifies the port`

To debug the generate-entities JAR copy the path location of the file obtained
from the console output after the '-cp'
![rx1.png](/assets/legacy/etendorx/etendorx-advanced-options/rx1.png)

Using intellij go to File -> Project Structure -> Libraries
Press '+' -> New project library -> Java -> Paste the path location of the JAR file
![rx2.png](/assets/legacy/etendorx/etendorx-advanced-options/rx2.png)

In the Intellij External Libraries you would see the 'generate-entities" JAR file.
Go to 'generate.entities.jar' -> com -> etendorx.gen -> GenerateEntitiesApplication and set a breakpoint.
![rx3.png](/assets/legacy/etendorx/etendorx-advanced-options/rx3.png)

In the 'Intellij configurations' create a new 'Remote JVM Debug' configuration
using the specified port and press 'debug'.
![rx4.png](/assets/legacy/etendorx/etendorx-advanced-options/rx4.png)
