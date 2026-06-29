---
tags:
  - How to
  - Etendo Classic
  - Interactive Setup
  - Configuration
---

# Cómo utilizar el Interactive Setup { #how-to-use-the-interactive-setup }

## Visión General { #overview }

El Interactive Setup es una alternativa a `setup.applyTemplates` que guía al desarrollador a través de cada propiedad de configuración de forma individual, con ayuda en línea, validación y un paso de confirmación antes de aplicar cualquier cambio.

Características principales:

- Guía paso a paso con ayuda en línea para cada propiedad.
- Las entradas sensibles (contraseñas, tokens) se detectan y se ocultan.
- Los ajustes se agrupan por categoría (Base de Datos, Seguridad, Aplicación, etc.).
- Validación integrada y paso de confirmación antes de aplicar los cambios.
- Copias de seguridad automáticas de los archivos de configuración existentes antes de las actualizaciones.

!!! info
    Para una configuración más rápida usando plantillas predefinidas, consulte las guías de [Desarrollo Local](../getting-started/installation/local-development.md) o [Instalación en Servidor](../getting-started/installation/production-server.md), que utilizan `setup.applyTemplates` como método principal.

## Requisitos { #requirements }

- [Requisitos del sistema](../getting-started/installation/requirements.md)
- [PostgreSQL configurado](../getting-started/installation/postgresql-configuration.md)
- [Credenciales de GitHub](../getting-started/installation/use-of-repositories-in-etendo.md)
- Etendo Gradle Plugin [2.1.0](../../../whats-new/release-notes/etendo-classic/plugins/etendo-gradle-plugin/release-notes.md) o superior. Para más información, visite [Etendo Gradle Plugin](../developer-tools/etendo-gradle-plugin.md).

## Iniciar la Configuración Interactiva { #start-interactive-configuration }

Lance el asistente de configuración interactiva:

```bash title="Terminal"
./gradlew setup -Pinteractive=true --console=plain
```

## Navegar por el Menú de Configuración { #navigate-the-configuration-menu }

Se muestra el menú principal de configuración:

```
🎛️  Interactive Setup - Main Menu
============================================================

📋 Choose configuration option:

1️⃣  Default configuration (use current/default values)
2️⃣  Group configuration:
   📦 a. all - Configure all groups
   📋 b. Database Configuration
   📋 c. Security Settings
   📋 d. Application Settings
3️⃣  Exit without saving

🎯 Select an option:
```

## Configurar Propiedades { #configure-properties }

Al seleccionar un grupo de configuración, cada propiedad se presenta de forma individual:

```
📋 Database Configuration
==================================================

🔧 Property: bbdd.host
   ℹ️  Database server hostname or IP address
   Current value: localhost
✏️  New value: [Enter to keep current, or type new value]

🔧 Property: bbdd.port
   ℹ️  Database server port number
   Current value: 5432
✏️  New value: [Enter to keep current, or type new value]

🔧 Property: bbdd.password
   ℹ️  Database connection password
   Current value:
🔐 New value (hidden): [Password input is hidden]
```

!!! tip "Consejos para la Configuración de Propiedades"
    - **Presione Enter** para mantener el valor actual o predeterminado.
    - **Escriba nuevos valores** para sobrescribir los valores predeterminados.
    - **Las propiedades sensibles** (contraseñas, tokens) ocultarán su entrada.
    - **Las propiedades obligatorias** deben tener un valor para continuar.

## Revisar el Resumen de Configuración { #review-configuration-summary }

Antes de aplicar los cambios, se muestra un resumen completo:

```
📊 Configuration Summary
============================================================

📋 Database Configuration:
   🔧 bbdd.host = localhost
   🔧 bbdd.port = 5432
   🔧 bbdd.password = ********

📋 Security Settings:
   🔧 githubToken = ********
   🔧 nexusPassword = ********

📋 Application Settings:
   🔧 context.name = etendo

📊 Total: 6 properties configured
🔐 Including 3 sensitive properties (shown masked)

✅ Confirm configuration? (Y/N):
```

Tras confirmar, las propiedades se guardan en `gradle.properties` (con copia de seguridad automática) y `./gradlew setup` se ejecuta automáticamente.

## Re-ejecutar la Configuración Interactiva { #re-running-interactive-configuration }

La configuración interactiva puede ejecutarse nuevamente en cualquier momento para modificar ajustes o revisar los valores actuales:

```bash title="Terminal"
./gradlew setup -Pinteractive=true --console=plain
```

Esto muestra los valores de configuración actuales, permite modificar cualquier ajuste y crea una nueva copia de seguridad antes de aplicar los cambios.

## Modo Debug { #debug-mode }

Para la resolución de problemas, active la salida de depuración:

```bash title="Terminal"
./gradlew setup -Pinteractive=true --debug --console=plain
```

## Propiedades de Módulos Personalizados { #custom-modules-properties }

Si el proyecto incluye módulos personalizados con un archivo `config.gradle`, sus propiedades de configuración se agregan automáticamente al interactive setup. Los nombres de las propiedades se conservan exactamente tal como están declarados en `config.gradle`, y se admiten claves personalizadas en `gradle.properties`.

!!! info
    Para más detalles sobre la Configuración Interactiva para módulos personalizados, visite la guía de [Etendo Interactive Configuration](../developer-tools/etendo-interactive-configuration.md).

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.
