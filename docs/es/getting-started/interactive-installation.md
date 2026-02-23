---
title: Instalar Etendo - Guía interactiva

tags:
    - Instalación de Etendo
    - Guía de instalación
    - Gestión de Docker
    - Configuración de PostgreSQL
    - Entorno de Etendo
    - Instalar
    - Instalación interactiva

status: beta
---
# Instalar Etendo - Guía interactiva

## Visión general

!!! example  "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsalo **bajo tu propia responsabilidad**. El comportamiento del módulo puede cambiar sin previo aviso. No lo utilices en entornos de producción. 

Utiliza el Sistema de Configuración Interactiva para instalar y configurar Etendo. El asistente te guía por cada ajuste, aplica valores predeterminados seguros y realiza cambios solo después de que los confirmes.

Beneficios clave:

- Guía paso a paso con ayuda en línea para cada propiedad.
- La entrada sensible (contraseñas, tokens) se detecta y se oculta.
- Los ajustes se agrupan por categoría (Base de datos, Seguridad, Aplicación, etc.).
- Validación integrada y un paso de confirmación antes de aplicar cambios.
- Copias de seguridad automáticas de los archivos de configuración existentes antes de actualizarlos.
- Configuración más rápida y con menos errores en comparación con la edición manual.

## Requisitos

Antes de comenzar, es necesario disponer de:

- [Requisitos del sistema](../getting-started/requirements.md).
- [PostgreSQL configurado correctamente](../developer-guide/etendo-classic/getting-started/installation/postgresql-configuration.md). 
- Credenciales de GitHub listas. Obtén acceso a [Uso de repositorios en Etendo - Guía del desarrollador](../developer-guide/etendo-classic/getting-started/installation/use-of-repositories-in-etendo.md). 
    
    
        

- Etendo Gradle Plugin [2.1.0](../whats-new/release-notes/etendo-classic/plugins/etendo-gradle-plugin/release-notes.md) o superior. Para más información, visita [Etendo Gradle Plugin](../developer-guide/etendo-classic/developer-tools/etendo-gradle-plugin.md).

## Proceso de instalación interactiva

### Preparar el entorno

Elige el formato de instalación y prepara los archivos base:


=== ":octicons-file-zip-24: Source Format"

    1. Clona el proyecto Etendo Base en el directorio `/opt`:
        ```bash title="Terminal"
        cd /opt/
        git clone https://github.com/etendosoftware/etendo_base.git EtendoERP
        ```

    2. Ve al directorio de instalación:
        ```bash title="Terminal"
        cd /opt/EtendoERP
        ```

    3. Añade las credenciales de GitHub al archivo `gradle.properties`:
        ```groovy title="gradle.properties"
        githubUser=<username>
        githubToken=<*******>
        ```

    4. Expande Etendo Base:
        ```bash title="Terminal"
        ./gradlew expand
        ```
=== ":material-language-java: JAR Format"

    1. Clona el proyecto Etendo Base en el directorio `/opt`:
        ```bash title="Terminal"
        cd /opt/
        git clone https://github.com/etendosoftware/etendo_base.git EtendoERP
        ```

    2. Ve al directorio de instalación:
        ```bash title="Terminal"
        cd /opt/EtendoERP
        ```

    3. Añade las credenciales de GitHub al archivo `gradle.properties`:
        ```groovy title="gradle.properties"
        githubUser=<username>
        githubToken=<*******>
        ```

    4. Descomenta la dependencia del core en `build.gradle`:
        ```groovy title="build.gradle"
        implementation('com.etendoerp.platform:etendo-core:<version>')
        ```

=== ":material-docker: Docker Format"

    1. Clona el proyecto Etendo Base en el directorio `/opt`:
        ```bash title="Terminal"
        cd /opt/
        git clone https://github.com/etendosoftware/etendo_base.git EtendoERP
        ```

    2. Ve al directorio de instalación:
        ```bash title="Terminal"
        cd /opt/EtendoERP
        ```

    3. Añade las credenciales de GitHub al archivo `gradle.properties`:
        ```groovy title="gradle.properties"
        githubUser=<username>
        githubToken=<*******>
        ```
    4. Añade la dependencia del bundle Platform Extensions:
        ```groovy title="build.gradle"
        dependencies {
            implementation ('com.etendoerp:platform.extensions:2.6.0') // 2.6.0 o superior.
        }
        ```

    5. Expande Etendo Base:
        ```bash title="Terminal"
        ./gradlew expand
        ```

### Iniciar la configuración interactiva

Inicia el asistente de configuración interactiva:

```bash title="Terminal"
./gradlew setup -Pinteractive=true --console=plain
```

### Iniciar la configuración de Etendo con Gradle

Lanza el comando ./gradlew setup --info

### Navegar por el menú de configuración

Será posible ver el menú principal de configuración:

```
🎛️  Configuración interactiva - Menú principal
============================================================

📋 Elige una opción de configuración:

1️⃣  Configuración por defecto (usar valores actuales/por defecto)
2️⃣  Configuración por grupos:
   📦 a. all - Configurar todos los grupos
   📋 b. Configuración de base de datos
   📋 c. Ajustes de seguridad
   📋 d. Ajustes de la aplicación
3️⃣  Salir sin guardar

🎯 Selecciona una opción:
```

### Configurar propiedades

Al seleccionar un grupo de configuración, se te guiará por cada propiedad, por ejemplo:

```
📋 Configuración de base de datos
==================================================

🔧 Propiedad: bbdd.host
   ℹ️  Nombre de host o dirección IP del servidor de base de datos
   Valor actual: localhost
✏️  Nuevo valor: [Enter para mantener el actual, o escribe un nuevo valor]

🔧 Propiedad: bbdd.port
   ℹ️  Número de puerto del servidor de base de datos
   Valor actual: 5432
✏️  Nuevo valor: [Enter para mantener el actual, o escribe un nuevo valor]

🔧 Propiedad: bbdd.password
   ℹ️  Contraseña de conexión a la base de datos
   Valor actual: 
🔐 Nuevo valor (oculto): [La entrada de contraseña está oculta]
```

!!! tip "Consejos de configuración de propiedades"
    - **Pulsa Enter** para mantener el valor actual/por defecto.
    - **Escribe nuevos valores** para sobrescribir los valores por defecto.
    - Las **propiedades sensibles** (contraseñas, tokens) ocultarán tu entrada.
    - Las **propiedades obligatorias** deben tener un valor para continuar.

### Revisar el resumen de configuración

Antes de aplicar los cambios, se mostrará un resumen completo:

```
📊 Resumen de configuración
============================================================

📋 Configuración de base de datos:
   🔧 bbdd.host = localhost
   🔧 bbdd.port = 5432
   🔧 bbdd.password = ********

📋 Ajustes de seguridad:
   🔧 githubToken = ********
   🔧 nexusPassword = ********

📋 Ajustes de la aplicación:
   🔧 context.name = etendo

📊 Total: 6 propiedades configuradas
🔐 Incluye 3 propiedades sensibles (mostradas enmascaradas)

✅ ¿Confirmar configuración? (Y/N):
```

**Lista de verificación de revisión**

- [X] Todas las propiedades obligatorias tienen valores.
- [X] Los detalles de conexión a la base de datos son correctos.
- [X] Las credenciales de GitHub/Nexus están configuradas correctamente.
- [X] El nombre de contexto de la aplicación es el deseado.

### Completar la instalación

Tras confirmar la configuración:

1. **Las propiedades se guardan** en `gradle.properties` (con copia de seguridad automática).
2. **La configuración tradicional se ejecuta** automáticamente.
3. **La instalación continúa** con los ajustes configurados.

Completa el proceso de instalación:

=== ":octicons-file-zip-24: Source Format"

    ```bash title="Terminal"
    # Instalación
    ./gradlew install smartbuild
    
    # Iniciar Tomcat
    sudo /etc/init.d/tomcat start
    ```

=== ":material-language-java: JAR Format"

    ```bash title="Terminal"
    # Dependencias
    ./gradlew dependencies
    
    # Instalación
    ./gradlew install smartbuild
    
    # Iniciar Tomcat
    sudo /etc/init.d/tomcat start
    ```

=== ":material-docker: Docker Format"

    ```bash title="Terminal"
    # Lanzar servicios Docker
    ./gradlew resources.up
    
    # Instalación
    ./gradlew install smartbuild
    ```

### Acceder a tu instalación

Abre el navegador y navega a:

- **Instalación estándar**: `https://<Public server IP>/<Context Name>`
- **Desarrollo local**: `http://localhost:8080/etendo`


## Funcionalidades avanzadas

### Volver a ejecutar la configuración interactiva

Es posible ejecutar la configuración interactiva de nuevo en cualquier momento:

```bash title="Terminal"
./gradlew setup -Pinteractive=true --console=plain
```

Esto:

- Mostrará los valores de configuración actuales.
- Permitirá al usuario modificar cualquier ajuste.
- Creará nuevas copias de seguridad antes de aplicar los cambios.

### Modo depuración

Para la resolución de problemas, habilita la salida de depuración:

```bash title="Terminal"
./gradlew setup -Pinteractive=true --debug --console=plain
```
### Configuración de propiedades de módulos personalizados

Si tu proyecto incluye módulos personalizados con un archivo `config.gradle`, sus propiedades de configuración se añaden automáticamente a la configuración interactiva. Los nombres de las propiedades se conservan exactamente como se declaran en `config.gradle`, y se admiten claves personalizadas en `gradle.properties`.

!!! info 
    Visita la [Guía del desarrollador](../developer-guide/etendo-classic/developer-tools/etendo-interactive-configuration.md) para obtener detalles sobre la Configuración Interactiva para módulos personalizados.

---
Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L](https://etendo.software){target="_blank"}.

---