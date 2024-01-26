# How to Start RX as a Service from Source Code

This document guides you through the process of starting the RX service from the source code, including generating JAR files and launching various components.

## 1. Generating JARs

Ensure you have built the JAR files necessary for different service components. Use these commands in your terminal:

```bash
./gradlew com.etendorx.entities:build 
./gradlew com.etendorx.das:build -x test
./gradlew com.etendorx.config:build -x test
./gradlew com.etendorx.auth:build -x test
```

## 2. Starting the Config Server

Before initiating the Config Server, confirm that your configuration files are correctly set up.

**Configuration Files:**
Ensure the required files, such as `service.yaml`, are present in the designated directory (`/path/to/directory/rxconfig`).

**Setting Environment Variables:**
Configure the necessary environment variables to direct the Config Server to these files:

```bash
export SPRING_PROFILES_ACTIVE=native
export SPRING_CLOUD_CONFIG_SERVER_NATIVE_SEARCH_LOCATIONS=$(pwd)/rxconfig
```

**Starting the Config Service:**

```bash
java -jar modules_core/com.etendorx.config/build/libs/com.etendorx.config-1.1.0.jar
```

## 3. Starting DAS

Use this command to start the DAS service, ensuring the correct path and version for the generated entities jar.

```bash
java -Dloader.path=modules_gen/com.etendorx.entities/build/libs/com.etendorx.entities-1.1.0-plain.jar -jar modules_core/com.etendorx.das/build/libs/com.etendorx.das-1.1.0.jar
```

!!!info
    - **Validation:** Confirm that all paths and filenames in the commands align with your project structure.
    - **Dependencies:** Check that all necessary dependencies are installed prior to executing these commands.
    - **Testing:** Testing each step in a development setting before production deployment is recommended.

## 4. Starting AUTH

To initiate the AUTH service, execute the following command, making sure the path and version of the generated entities jar are correct.

```bash
java -jar modules_core/com.etendorx.auth/build/libs/com.etendorx.auth-1.1.0.jar
```

## 5. Starting EDGE

To initiate the EDGE service, execute the following command, making sure the path and version of the generated entities jar are correct.

```bash
java -jar modules_core/com.etendorx.edge/build/libs/com.etendorx.edge-1.1.0.jar
```

### Disclaimer: Advanced Knowledge Required

This guide assumes a fundamental understanding of Java development environments, including familiarity with Gradle build commands and Java application deployment. It is intended for users with intermediate to advanced technical skills in software development and system administration. New users or those unfamiliar with the concepts discussed may need additional resources or assistance. 