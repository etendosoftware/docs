---
title: Configuración interactiva de Etendo

tags:
    - Instalación de Etendo
    - Guía de instalación
    - Gestión de Docker
    - Configuración de PostgreSQL
    - Entorno de Etendo
    - Instalar
    - Instalación de Etendo
    - Instalación interactiva

status: beta
---
# Configuración interactiva de Etendo
## Visión general

!!! example  "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úselo **bajo su propia responsabilidad**. El comportamiento del módulo puede cambiar sin previo aviso. No lo utilice en entornos de producción.

!!! info
    Esta funcionalidad está disponible a partir de Etendo Gradle Plugin [2.1.0](../../../whats-new/release-notes/etendo-classic/plugins/etendo-gradle-plugin/release-notes.md). Para más información, visite [Etendo Gradle Plugin](./etendo-gradle-plugin.md).
    

El sistema de **Configuración interactiva de Etendo** proporciona un asistente de línea de comandos fácil de usar para configurar proyectos de Etendo. Integrado en Etendo Gradle Plugin, guía a los desarrolladores a través de la configuración de propiedades con valores predeterminados inteligentes, gestión segura de datos sensibles y una presentación organizada de las opciones de configuración.
## Inicio rápido

### Uso básico

```bash
# Run interactive configuration (recommended)
./gradlew setup -Pinteractive=true --console=plain

# Standard setup
./gradlew setup
```

### Qué hace la configuración interactiva

1. **Escanea** su proyecto en busca de propiedades configurables desde:

    - **Archivo `gradle.properties` existente**: Lee los valores actuales de las propiedades e identifica los ajustes configurables
    - **Archivos `config.gradle` de los módulos**: Detecta la configuración específica del módulo con metadatos, incluidas descripciones, valores por defecto, ajustes de seguridad y propiedades de proceso

2. **Le guía** a través de la configuración con:

    - **Documentación clara para cada propiedad**: Muestra un texto de ayuda descriptivo que explica qué hace cada propiedad y su propósito
    - **Valores actuales/por defecto mostrados en los avisos**: Muestra los valores existentes entre paréntesis, permitiéndole pulsar Intro para mantenerlos o escribir nuevos valores
    - **Entrada segura para propiedades sensibles**: Detecta automáticamente contraseñas, tokens y secretos, ocultando la entrada durante la escritura
    - **Ejecución de propiedades de proceso**: Ofrece ejecutar tareas de Gradle para la configuración automatizada de ajustes complejos
    - **Propiedades organizadas por grupos lógicos**: Agrupa los ajustes relacionados (Base de datos, Seguridad, API, etc.) para facilitar la navegación

3. **Confirma** su configuración con:

    - **Resumen completo de todos los ajustes**: Muestra una visión general completa de todas las propiedades configuradas, organizadas por grupo
    - **Resultados de ejecución de procesos**: Muestra las propiedades configuradas automáticamente mediante ejecuciones de procesos
    - **Valores sensibles enmascarados por seguridad**: Muestra las propiedades sensibles como asteriscos (********) para proteger las credenciales
    - **Posibilidad de revisar antes de aplicar cambios**: Requiere confirmación explícita (S/N) antes de escribir cualquier cambio en los archivos

4. **Aplica** la configuración mediante:

    - **Escritura en `gradle.properties` con copia de seguridad automática**: Crea archivos de copia de seguridad con marca de tiempo antes de realizar cambios
    - **Conservación de los comentarios y la estructura existentes**: Mantiene el formato del archivo, los comentarios y la organización mientras actualiza los valores
    - **Marcado de procesos ejecutados**: Añade marcadores `EXECUTED:` a las propiedades de proceso que se han ejecutado
    - **Continuación con el proceso normal de configuración**: Se integra sin problemas con el flujo de trabajo de configuración existente de Etendo
## Interfaz de configuración

**Seleccione el modo de configuración principal**

La configuración interactiva presenta tres modos principales de configuración:

- Configuración predeterminada (usar valores actuales/predeterminados)
- Configuración por grupos:

    1. Todos - Configurar todos los grupos
    2. Configuración de base de datos
    3. Configuración de seguridad
    4. Configuración de la aplicación
    
- Salir sin guardar.

**Configurar propiedades**

Al configurar propiedades, el sistema proporciona un contexto enriquecido. Por ejemplo:

```
📋 Database Configuration
==================================================

🔧 Property: bbdd.host
   ℹ️  Database server hostname or IP address
   Current value: localhost
✏️  New value: [Enter to keep current, or type new value]

🔧 Property: bbdd.password
   ℹ️  Database connection password
   Current value: ********
🔐 New value (hidden): [Password input is hidden]
```

**Confirmar la configuración**

Antes de aplicar los cambios, verá un resumen completo:

```
📊 Configuration Summary
============================================================

📋 Database Configuration:
   🔧 bbdd.host = localhost
   🔧 bbdd.password = ********

📋 Security Settings:
   🔧 githubToken = ********

📊 Total: 3 properties configured
🔐 Including 2 sensitive properties (shown masked)

✅ Confirm configuration? (Y/N):
```
## Añadir configuración a módulos personalizados

**Creación de un archivo config.gradle**

Para añadir soporte de configuración interactiva a su módulo personalizado, cree un archivo `config.gradle` en el directorio raíz de su módulo:

``` title="config.gradle"
    modules/
    ├── com.yourcompany.yourmodule/
    │   ├── config.gradle          ← Archivo de configuración
    │   ├── src/
    │   └── build.gradle
```

**Estructura del archivo de configuración**

El archivo `config.gradle` utiliza el formato ConfigSlurper de Groovy, proporcionando una configuración estructurada y con seguridad de tipos:

```groovy
// modules/com.yourcompany.yourmodule/config.gradle

/**
* Configuración interactiva para su módulo personalizado
*/

// Configuración de API
api {
    baseUrl {
        description = "URL base para el servicio de API externo"
        value = "https://api.example.com"
        help = "URL completa incluyendo protocolo y puerto. Ejemplo: https://api.example.com:8443/v1"
        sensitive = false
        required = true
        group = "Configuración de API"
        name = "api.base.url"
        order = 10
    }
    
    apiKey {
        description = "Clave de API para autenticación con el servicio externo"
        value = ""
        help = "Clave secreta obtenida desde el panel de su proveedor de API"
        sensitive = true
        required = false
        group = "Configuración de API"
        name = "API_SECRET_KEY"
        order = 20
    }
    
    timeout {
        description = "Tiempo de espera de solicitudes de API en segundos"
        value = "30"
        help = "Tiempo máximo de espera de respuestas de la API antes de agotar el tiempo"
        sensitive = false
        required = false
        group = "Configuración de API"
        name = "api.timeout.seconds"
        order = 30
    }
    
    // Ejemplo usando el campo name personalizado para una clave específica de gradle.properties
    customEndpoint {
        description = "URL de endpoint de API personalizado"
        value = ""
        name = "custom.api.endpoint"  // Mapea a custom.api.endpoint en gradle.properties
        help = "Endpoint alternativo para operaciones especializadas de la API"
        sensitive = false
        required = false
        group = "Configuración de API"
        order = 40
    }
}

// Propiedades de proceso - Configuración automatizada
automation {
    databaseSetup {
        description = "Configuración automatizada de base de datos"
        value = ""
        help = "Ejecuta tareas de configuración de base de datos, incluyendo creación de esquema y pool de conexiones"
        sensitive = false
        required = false
        process = true  // Esta es una propiedad de proceso
        group = "Configuración automatizada"
        name = "database.setup.automated"
        order = 10
    }
    
    apiIntegration {
        description = "Proceso de configuración de integración de API"
        value = ""
        help = "Configura automáticamente endpoints de API, credenciales y feature flags"
        sensitive = false
        required = false
        process = true  // Esto ejecutará la tarea automation.apiIntegration
        group = "Configuración automatizada"
        name = "api.integration.configure"
        order = 20
    }
}

// Ajustes de funcionalidades
features {
    enableAdvancedReporting {
        description = "Habilitar funcionalidades avanzadas de informes"
        value = "false"
        help = "Activa capacidades mejoradas de informes con generación de gráficos"
        sensitive = false
        required = false
        group = "Ajustes de funcionalidades"
        name = "features.advanced.reporting.enabled"
        order = 10
    }
    
    maxReportSize {
        description = "Tamaño máximo del informe en MB"
        value = "10"
        help = "Limita el tamaño de los informes generados para evitar problemas de memoria"
        sensitive = false
        required = false
        group = "Ajustes de funcionalidades"
        name = "features.reports.max.size.mb"
        order = 20
    }
}

// Ajustes de base de datos (si su módulo necesita configuración de BD separada)
database {
    connectionPool {
        description = "Tamaño del pool de conexiones de base de datos para operaciones del módulo"
        value = "5"
        help = "Número de conexiones concurrentes a la base de datos para este módulo"
        sensitive = false
        required = false
        group = "Ajustes de base de datos"
        name = "database.connection.pool.size"
        order = 10
    }
}
```

**Referencia de propiedades de configuración**

Cada propiedad en su archivo `config.gradle` admite los siguientes metadatos:

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| `description` | String | Sí | Descripción legible para humanos que se muestra a los usuarios |
| `value` | String | Sí | Valor por defecto de la propiedad |
| `sensitive` | Boolean | No | `true` para contraseñas, tokens, secretos (por defecto: `false`) |
| `required` | Boolean | No | `true` para propiedades obligatorias (por defecto: `false`) |
| `process` | Boolean | No | `true` para propiedades de proceso que ejecutan tareas de Gradle (por defecto: `false`) |
| `help` | String | No | Texto de ayuda ampliado con detalles de uso y ejemplos |
| `group` | String | No | Nombre del grupo de visualización (por defecto: autogenerado a partir del nombre del bloque) |
| `order` | Integer | No | Orden de visualización dentro del grupo (recomendado: 10, 20, 30...) |
| `name` | String | No | Nombre de variable para gradle.properties O nombre de tarea para propiedades de proceso |

### Orden de visualización de propiedades

Las propiedades se muestran en la configuración interactiva siguiendo estas reglas:

1. **Primero las propiedades de proceso**: todas las propiedades con `process = true` se muestran antes que las propiedades normales
2. **Después por el campo order**: las propiedades se ordenan por su valor `order` dentro de cada tipo (proceso vs normal)

```groovy
database {
    // Esta propiedad de proceso aparecerá primero (process = true)
    setup {
        description = "Configuración automatizada de base de datos"
        process = true
        order = 10
    }
    
    // Las propiedades normales aparecen después de las propiedades de proceso, ordenadas por order
    host {
        description = "Nombre de host de la base de datos"
        order = 10  // Primera propiedad normal
    }
    
    port {
        description = "Puerto de la base de datos"
        order = 20  // Segunda propiedad normal
    }
    
    password {
        description = "Contraseña de la base de datos"
        order = 30  // Tercera propiedad normal
    }
}
```

### Nomenclatura y mapeo de propiedades

El campo `name` tiene distintos propósitos según el tipo de propiedad:

**Para propiedades normales**  
Utilice el campo `name` para especificar el nombre exacto de la variable que se escribirá en `gradle.properties`:

```groovy
// Ejemplo con el campo name personalizado
myModule {
    debugMode {
        description = "Habilitar modo de depuración"
        help = "🔧 Habilitar depuración detallada para el desarrollo del módulo y la resolución de incidencias"
        value = "false"
        sensitive = false
        required = false
        group = "Configuración de MyModule (Avanzado)"
        order = 20
        name = "MYMODULE_DEBUG"          // Este será el nombre de la variable en gradle.properties
    }
}
```

**Resultado en gradle.properties:**
```properties
MYMODULE_DEBUG=false
```

**Para propiedades de proceso**  
Utilice el campo `name` para especificar el nombre exacto de la tarea de Gradle a ejecutar:

```groovy
// Ejemplo con nombre de tarea personalizado
automation {
    setupDatabase {
        description = "Configuración de la base de datos"
        value = ""
        help = "Ejecuta la configuración automatizada de la base de datos"
        process = true
        group = "Automatización"
        name = "database.configure.production"  // Esto ejecutará la tarea: database.configure.production
    }
}
```

**Nomenclatura por defecto vs. nomenclatura personalizada**

```groovy
api {
    baseUrl {
        description = "URL base de la API"   
        value = "https://api.example.com"
        // Sin el campo 'name' = por defecto "api.baseUrl"
    }
    
    apiKey {
        description = "Clave de API"
        value = ""
        name = "API_TOKEN"             // Nombre personalizado: "API_TOKEN"
    }
}

automation {
    databaseSetup {
        description = "Configurar base de datos"
        process = true
        // Sin el campo 'name' = por defecto la tarea "automation.databaseSetup"
    }
    
    customSetup {
        description = "Proceso de configuración personalizado"
        process = true
        name = "my.custom.task"        // Nombre de tarea personalizado: "my.custom.task"
    }
}
```

**Resultados:**

```properties
# Propiedades normales en gradle.properties
api.baseUrl=https://api.example.com
API_TOKEN=

# Las propiedades de proceso ejecutan tareas
# automation.databaseSetup → ejecuta la tarea "automation.databaseSetup"  
# automation.customSetup → ejecuta la tarea "my.custom.task"
```

- **Sin transformación automática**: nombres de propiedad como `systemUser` permanecen como `systemUser` (no se transforman a `system.user`).
- **Nomenclatura preservada**: todos los nombres de propiedad se mantienen exactamente tal como están escritos en el archivo `config.gradle`.
- **Mapeo personalizado opcional**: utilice el campo `name` cuando necesite claves específicas en `gradle.properties` por compatibilidad.

**Gestión de propiedades sensibles**

El sistema detecta automáticamente las propiedades sensibles en base a:

- **Marcado explícito**: `sensitive = true` en la configuración
- **Detección por patrón**: propiedades que contienen palabras clave como: `password`, `secret`, `token`, `key`, `credential`, `auth`, `private`, `secure`

Ejemplo de configuración de propiedad sensible:

```groovy
security {
    databasePassword {
        description = "Contraseña de base de datos para operaciones específicas del módulo"
        value = ""
        sensitive = true  // Marcada explícitamente como sensible
        required = true
        group = "Ajustes de seguridad"
    }
    
    jwtSecret {
        description = "Secreto de firma JWT para generación de tokens"
        value = ""
        sensitive = true  // Se detectará automáticamente debido a la palabra clave 'secret'
        required = true
        group = "Ajustes de seguridad"
        
    }
}
```
## Propiedades de proceso

### Visión general

Las propiedades de proceso son un tipo especial de propiedad que ejecuta tareas de Gradle para recopilar valores de configuración automáticamente. En lugar de pedir a los usuarios que introduzcan manualmente una configuración compleja, estas propiedades ejecutan procesos automatizados que pueden:

- Ejecutar comandos externos
- Consultar APIs o servicios  
- Generar archivos de configuración
- Configurar integraciones
- Configurar procesos complejos de varios pasos

### Cómo funcionan las propiedades de proceso

1. **Definición**: Marque una propiedad con `process = true` en su configuración
2. **Ejecución de tareas**: Cuando se selecciona, el sistema ejecuta la tarea de Gradle correspondiente
3. **Recopilación de resultados**: La tarea genera la configuración en un archivo JSON
4. **Actualizaciones de propiedades**: Los resultados se aplican automáticamente a gradle.properties
5. **Seguimiento de ejecución**: Los procesos completados se marcan con marcadores `EXECUTED:`

### Ciclo de vida de una propiedad de proceso

```bash
# User selects process property in interactive setup
myModule.variables.setup = "" (process property)

# System prompts for execution
"Execute myModule variables setup process? (Y/n): Y"

# Task execution
"Executing task: myModule.variables.setup..."

# Results applied automatically
myModule.api.endpoint = "https://api.mymodule.com"
myModule.api.key = "********"
myModule.workspace.id = "ws_abc123"

# Original property marked as executed
myModule.variables.setup = "EXECUTED:3_properties_configured"
```

### Creación de propiedades de proceso

**Configuración básica de una propiedad de proceso**

!!! info 
    El nombre de la propiedad (clave) en la configuración **debe coincidir con el nombre de la tarea de Gradle** que se ejecutará. El sistema asigna automáticamente la clave de la propiedad a la tarea de Gradle correspondiente.

```groovy
// Process property that executes automated configuration
myModule {
    variables {
        setup {
            description = "MyModule variables configuration"
            value = ""
            help = "Executes automated setup to configure module integration variables"
            process = true  // Marks this as a process property
            sensitive = false
            required = false
            group = "MyModule Integration"
            order = 1
            // This will execute the Gradle task: "myModule.variables.setup"
        }
    }
}

// Database setup process
database {
    setup {
        description = "Automated database configuration"
        value = ""
        help = "Configures database connection settings and initializes schema"
        process = true
        sensitive = false
        required = false
        group = "Database Configuration"
        order = 1
        // This will execute the Gradle task: "database.setup"
    }
}

// Alternative naming for complex task names
databaseMigration {
    description = "Database migration and schema updates"
    value = ""
    help = "Runs database migrations and schema updates"
    process = true
    group = "Database Configuration" 
    order = 2
    // This will execute the Gradle task: "databaseMigration"
}
```

!!! info "Convención de nomenclatura de tareas"

    - **Clave de propiedad = Nombre de tarea**: `myModule.variables.setup` → ejecuta la tarea `myModule.variables.setup`
    - **Propiedades jerárquicas**: `database.setup` → ejecuta la tarea `database.setup`  
    - **Nombres simples**: `databaseMigration` → ejecuta la tarea `databaseMigration`

### Implementación de tareas para propiedades de proceso

Las propiedades de proceso requieren tareas **Gradle** correspondientes que sigan este patrón:


**Características recomendadas de la tarea**

1. **Admitir el parámetro opcional `output`**: Las tareas deben aceptar un parámetro `output` cuando esté presente, pero no es obligatorio. Cuando se proporciona `output`, la tarea debe escribir los resultados ahí; cuando no está presente, la tarea debe seguir funcionando y o bien llamar al escritor a nivel de proyecto (si existe) sin una ruta explícita, o bien recurrir a la salida por consola.
2. **Usar `project.writeResultsForInteractiveSetup` cuando esté disponible**: Se recomienda llamar al closure registrado en el proyecto para escribir resultados JSON en flujos interactivos.
3. **Proporcionar feedback significativo**: Incluya mensajes de progreso para que el usuario sea consciente de lo que ocurre
4. **Gestionar errores de forma adecuada**: Proporcione mensajes de error claros cuando falle la configuración

!!! note "El parámetro output es opcional"
    El parámetro `output` puede ser proporcionado por el ejecutor interactivo (por ejemplo, cuando la orquestación de la configuración espera salida JSON). Las tareas deben admitir recibir `output` cuando se suministre, pero también deben funcionar cuando `output` no esté presente, ya sea llamando al closure del proyecto sin una ruta o imprimiendo los resultados en la consola.

**Uso del closure de proyecto `writeResultsForInteractiveSetup`**

El sistema de configuración interactiva expone un escritor estándar como un closure registrado en el objeto Gradle `project`: `project.writeResultsForInteractiveSetup(Map results, String outputPath = null)`. Esto permite que las tareas del módulo permanezcan desacopladas de las clases internas del plugin y escriban resultados si el flujo interactivo está activo.

```groovy
// Example task for myModule.variables.setup process property
task 'myModule.variables.setup' {
    description = "Configures MyModule integration variables"

    doLast {
        try {
            // Get the optional output parameter (may be provided by the interactive runner)
            def outputPath = project.findProperty('output')

            // Execute configuration logic
            println "🔧 Configuring MyModule integration..."

            // Your custom configuration logic here
            def apiEndpoint = "https://api.mymodule.com"
            def workspaceId = generateWorkspaceId()
            def apiKey = generateApiKey()

            // Prepare results for the interactive setup
            def results = [
                "myModule.api.endpoint"    : apiEndpoint,
                "myModule.workspace.id"    : workspaceId,
                "myModule.api.key"         : apiKey,
                "myModule.features.enabled": "true",
                "myModule.version"         : "1.0.0"
            ]

            // Use the reusable function for JSON output (if the project has the closure)
            boolean wasWrittenAsJson = false
            if (project.hasProperty('writeResultsForInteractiveSetup')) {
                try {
                    // Call the closure; pass outputPath when present
                    wasWrittenAsJson = outputPath ? project.writeResultsForInteractiveSetup(results, outputPath) : project.writeResultsForInteractiveSetup(results)
                } catch (Exception e) {
                    project.logger.debug("Failed to call project.writeResultsForInteractiveSetup: ${e.message}")
                    wasWrittenAsJson = false
                }
            } else {
                project.logger.lifecycle('Interactive setup writer not registered on project; falling back to console output.')
            }

            if (wasWrittenAsJson) {
                println "✅ MyModule configuration completed: ${results.size()} properties configured"
            } else {
                throw new RuntimeException("Failed to write configuration results")
            }
        } catch (Exception e) {
            throw new RuntimeException("MyModule setup failed: ${e.message}", e)
        }
    }
}
```

**Firma del closure de proyecto**

```
// Callable as a Groovy closure on `project`
boolean writeResultsForInteractiveSetup(Map results, String outputPath = null)
```

- `results`: Mapa de propiedades clave → valor que se van a escribir.
- `outputPath` (opcional): ruta explícita del archivo de salida. Si se omite, el escritor utilizará la propiedad de Gradle `-Poutput=...` cuando esté presente.

El closure devuelve `true` cuando los resultados se han escrito correctamente como JSON (modo interactivo) y `false` cuando no (para que las tareas puedan recurrir a imprimir los valores en la consola).

### Buenas prácticas para propiedades de proceso

1. **Nomenclatura de tareas**: Los nombres de las tareas deben coincidir con la clave de la propiedad (p. ej., `myModule.variables.setup` → `myModule.variables.setup`)
2. **Aceptar el parámetro opcional output**: Las tareas deben aceptar un parámetro `output` cuando se suministre para especificar dónde se escriben los resultados, pero TAMBIÉN DEBEN comportarse de forma razonable cuando no se suministre (fallback a consola o llamada al closure del proyecto sin una ruta explícita).
3. **Salida JSON cuando sea posible**: Se recomienda escribir JSON usando el closure `project.writeResultsForInteractiveSetup` cuando esté disponible; en caso contrario, proporcione un fallback por consola.
4. **Gestión de errores**: Proporcione mensajes de error significativos cuando fallen los procesos
5. **Feedback al usuario**: Incluya mensajes de progreso para informar a los usuarios de lo que está ocurriendo
6. **Validación de resultados**: Asegúrese de que todas las propiedades generadas sean válidas y estén correctamente formateadas

### Ejemplo de propiedad de proceso en la configuración interactiva

Cuando los usuarios se encuentran con propiedades de proceso en la configuración interactiva:

```bash
=== MyModule Integration ===
(2 properties)

🔧 Property: myModule.variables.setup [PROCESS]
   ℹ️  MyModule variables configuration
   💡 Help: Executes automated setup to configure module integration variables
   
🎯 Execute process? (Y/n): Y

🚀 Executing task: myModule.variables.setup...
🔧 Configuring MyModule integration...
✅ MyModule configuration completed: 5 properties configured

📊 Process Results Applied:
   🔧 myModule.api.endpoint = https://api.mymodule.com
   🔧 myModule.api.key = ********
   🔧 myModule.workspace.id = ws_abc123
   🔧 myModule.features.enabled = true
   🔧 myModule.version = 1.0.0

🔖 Process property marked as: EXECUTED:5_properties_configured
```
## Buenas prácticas

### Organización de propiedades

1. **Agrupe las propiedades relacionadas**: Use grupos lógicos como "Configuración de API", "Ajustes de base de datos", "Ajustes de seguridad"
2. **Descripciones claras**: Escriba un texto de ayuda descriptivo que explique el propósito de la propiedad y cualquier restricción
3. **Valores predeterminados razonables**: Proporcione valores predeterminados razonables que funcionen para la mayoría de los usuarios
4. **Use el campo order**: Especifique siempre valores `order` en incrementos de 10 (10, 20, 30...) para permitir la inserción de nuevas propiedades
5. **Marque los datos sensibles**: Marque siempre credenciales, contraseñas y tokens como sensibles

### Convenciones de nomenclatura

1. **Los nombres de las propiedades se conservan exactamente**: Use la convención de nomenclatura que prefiera; los nombres no se transforman automáticamente
2. **Sea descriptivo**: Use nombres de propiedad claros y descriptivos
3. **Evite palabras reservadas**: No use palabras clave reservadas de Gradle o Java
4. **Use el campo name para el mapeo personalizado**: Cuando necesite claves específicas de gradle.properties o nombres de tareas

```groovy
// Good examples - include name field and order for clarity
api {
    baseUrl { 
        description = "API base URL"
        value = "https://api.example.com"
        name = "api.base.url"
        order = 10
    }
    connectionTimeout { 
        description = "Connection timeout in seconds"
        value = "30"
        name = "api.connection.timeout"
        order = 20
    }
    retryAttempts { 
        description = "Number of retry attempts"
        value = "3"
        name = "api.retry.attempts"
        order = 30
    }
    
    // Legacy compatibility example
    systemUser {
        description = "System user for API access"
        value = "etendo_system"
        name = "api.system.user"  // → api.system.user (custom mapping)
        order = 40
    }
}

// Still avoid
api {
    url { /* too generic */ }
    timeout { /* unclear which timeout */ }
    class { /* reserved word */ }
}
```

### Validación de la configuración

El sistema proporciona seguridad de tipos mediante el formato estructurado de ConfigSlurper. Todas las propiedades se validan para garantizar una sintaxis correcta y la presencia de los campos obligatorios durante el proceso de escaneo.
## Pruebas de su configuración

1. Pruebe que su archivo `config.gradle` se detecta correctamente:

    ```bash
    # Run with debug output to see property scanning
    ./gradlew setup -Pinteractive=true --debug --console=plain | grep "config.gradle"

    # Expected output:
    # DEBUG - ✓ Processing config.gradle in modules/com.yourcompany.yourmodule
    # DEBUG - Loaded 5 properties from modules/com.yourcompany.yourmodule/config.gradle
    ```

2. Después de ejecutar la configuración interactiva, verifique que las propiedades se escriben correctamente en `gradle.properties`:

    ```bash
    # Check that your module's properties appear in gradle.properties
    cat gradle.properties | grep "api\."

    # Example output with preserved naming:
    # api.baseUrl=https://api.example.com
    # api.apiKey=your_secret_key
    # api.customEndpoint=custom_value
    # custom.api.endpoint=value_with_custom_name
    ```

3. Ejecute la configuración interactiva y verifique que aparecen las propiedades de su módulo:

    ```bash
    ./gradlew setup -Pinteractive=true --console=plain
    ```

Debería ver los grupos de propiedades de su módulo en el menú de configuración y poder configurarlos individualmente o como parte de la configuración de «todos los grupos».

---
Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L](https://etendo.software){target="_blank"}.