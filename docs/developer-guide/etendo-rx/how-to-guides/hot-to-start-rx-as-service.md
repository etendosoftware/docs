# How to start RX as a service

## 1. Generating JARs
First, ensure that you build the JAR files necessary for the different service components. Execute the following commands in your terminal:

```bash title='terminal'
./gradlew com.etendorx.entities:build 
./gradlew com.etendorx.das:build -x test
./gradlew com.etendorx.config:build -x test
./gradlew com.etendorx.auth:build -x test
```

## 2. Starting the Config Server
Before launching the Config Server, ensure that your configuration files are prepared.

**Configuration Files:**
   The required configuration files (e.g., `servicio.yaml`) should already exist in the specified directory (`/ruta/al/directorio/rxconfig`).

**Setting Environment Variables:**
   Set the necessary environment variables for the Config Server to use these configuration files:

   ```bash title='terminal'
   export SPRING_PROFILES_ACTIVE=native
   export SPRING_CLOUD_CONFIG_SERVER_NATIVE_SEARCHLOCATIONS=`pwd`/rxconfig
   ```

**Start Config service**
   
```bash title='terminal'
java -jar modules_core/com.etendorx.config/build/libs/com.etendorx.config-1.1.0.jar
```

## 3. Starting DAS
To start the DAS service, use the following command. Make sure to specify the correct path to the generated entities jar and the appropriate version.

```bash title='terminal'
java -Dloader.path=modules_gen/com.etendorx.entities/build/libs/com.etendorx.entities-1.1.0-plain.jar -jar modules_core/com.etendorx.das/build/libs/com.etendorx.das-1.1.0.jar
```

!!!info
    - **Validation:** Ensure that all paths and file names mentioned in the commands match your project's structure.
    - **Dependencies:** Verify that all necessary dependencies are installed before running these commands.
    - **Testing:** It is recommended to test each step in a development environment before deploying it to production.

## 4. Starting AUTH
To start the AUTH service, use the following command. Make sure to specify the correct path to the generated entities jar and the appropriate version.

```bash title='terminal'
java -jar modules_core/com.etendorx.auth/build/libs/com.etendorx.auth-1.1.0.jar
```


