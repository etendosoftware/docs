---
title: Cómo usar Setup Apply Templates
tags:
  - Cómo hacer
  - Gradle
  - Setup
  - Configuración
  - Plantillas
---

# Cómo usar Setup Apply Templates

## Visión general

La tarea de Gradle `setup.applyTemplates` permite configurar rápidamente un proyecto de Etendo usando plantillas predefinidas o personalizadas. Las plantillas son archivos que contienen propiedades, dependencias y módulos que se aplican automáticamente a tu proyecto, agilizando tanto la configuración inicial como las configuraciones específicas por entorno.

El plugin incluye dos plantillas integradas: **local** (para desarrollo local) y **server** (para despliegues en servidor/producción con configuración interactiva). El sistema es extensible: cualquier archivo `.template` añadido a los recursos del plugin se descubre automáticamente y queda disponible.

Esta guía explica cómo usar la tarea, las plantillas disponibles, el formato de plantilla, el soporte de placeholders y cómo crear plantillas personalizadas.

## Requisitos previos

- Un proyecto de Etendo con el plugin de Gradle instalado.
- El proyecto no debería tener ya una **Base de datos** configurada. Si la tiene, usa el flag `--force` para sobrescribir esta comprobación.

## Uso

La tarea puede ejecutarse en cuatro modos diferentes: selección interactiva, plantilla incluida, archivo local o URL remota.

### Modo interactivo

Cuando no se proporcionan opciones, la tarea muestra un menú interactivo para seleccionar entre las plantillas incluidas disponibles:

```bash title="Terminal"
./gradlew setup.applyTemplates
```

Salida:

```text
======================================================
  SELECT A TEMPLATE
======================================================
  1) local
  2) server

  You can also use:
    --template=<name>  (by name)
    --file=<path>      (local file)
    --url=<url>        (remote URL)

  >> Enter your selection (1-2):
```

### Aplicar una plantilla incluida

Usa la opción `--template` para aplicar una de las plantillas incluidas con el plugin:

```bash title="Terminal"
./gradlew setup.applyTemplates --template=local
```

### Aplicar una plantilla desde un archivo local

Usa la opción `--file` para aplicar una plantilla almacenada en tu sistema de archivos local:

```bash title="Terminal"
./gradlew setup.applyTemplates --file=/path/to/custom.template
```

### Aplicar una plantilla desde una URL remota

Usa la opción `--url` para descargar y aplicar una plantilla desde una ubicación remota:

```bash title="Terminal"
./gradlew setup.applyTemplates --url=https://example.com/templates/my-setup.template
```

### Modo forzado

Por defecto, la tarea comprueba si ya existe una **Base de datos** para el proyecto. Si existe, la tarea se aborta para evitar modificaciones no deseadas. Para omitir esta comprobación, usa el flag `--force`:

```bash title="Terminal"
./gradlew setup.applyTemplates --template=local --force
```

!!!warning
    Usar `--force` omite la validación del entorno. Asegúrate de entender las implicaciones antes de aplicar una plantilla a un proyecto ya configurado.

## Opciones disponibles

| Opción | Descripción | Ejemplo |
|---|---|---|
| `--template` | Nombre de una plantilla incluida desde los recursos del plugin | `--template=local` |
| `--file` | Ruta a un archivo `.template` local | `--file=/path/to/custom.template` |
| `--url` | URL a un archivo `.template` remoto | `--url=https://example.com/my.template` |
| `--force` | Omitir la comprobación de existencia de la **Base de datos** | `--force` |

## Plantillas incluidas

### `local` — Desarrollo local

Diseñada para entornos de desarrollo local. La mayoría de valores están preconfigurados con valores por defecto razonables. El único valor que requiere entrada del usuario es la **OpenAI API Key**.

```bash title="Terminal"
./gradlew setup.applyTemplates --template=local
```

#### Configuración interactiva

Al aplicarse, la tarea solicita el siguiente valor:

| # | Prompt | Descripción |
|---|---|---|
| 1 | OpenAI API Key | Tu clave de API de OpenAI para la integración con Copilot. La entrada se enmascara por seguridad. |

### `server` — Despliegue en servidor / producción

Diseñada para entornos de servidor y producción. Esta plantilla usa **placeholders** que se resuelven de forma interactiva durante la ejecución: se solicita al usuario que proporcione valores específicos del entorno.

```bash title="Terminal"
./gradlew setup.applyTemplates --template=server
```

#### Configuración interactiva

Al aplicarse, la tarea solicita los siguientes valores:

| # | Prompt | Variable | Descripción |
|---|---|---|---|
| 1 | URL de Etendo ERP | `context.url` | La dirección web completa de tu aplicación Etendo ERP (p. ej., `http://myserver.com/etendo`). A partir de este valor, se derivan automáticamente `context.name` (último segmento de la ruta) y `context.host` (URL base sin el nombre del contexto). |
| 2 | OpenAI API Key | `openai.api.key` | Tu clave de API de OpenAI para la integración con Copilot. La entrada se enmascara por seguridad. |

**Ejemplo de interacción:**

```text
======================================================
  CONFIGURATION REQUIRED
  Template 'server' needs the following input
  Please type each value and press ENTER
======================================================


  [1/2] Etendo ERP URL (e.g., http://clienthost/mycompanyname)

  >> http://myserver.com/etendo


  [2/2] OpenAI API Key

  >> ****
```

#### Valores derivados

A partir de la entrada `context.url`, se derivan automáticamente los siguientes valores:

| Entrada | Variable derivada | Valor |
|---|---|---|
| `http://myserver.com/etendo` | `context.name` | `etendo` |
| | `context.host` | `http://myserver.com/` |

Estos valores derivados se usan para configurar:

- `etendo.classic.url` → `http://host.docker.internal:80/{context.name}`
- `etendo.classic.host` → `{context.url}`
- `next.public.app.url` → `{context.host}`

## Funcionalidades avanzadas

### Formato de plantilla

Las plantillas usan un formato similar a INI con tres secciones: `[properties]`, `[dependencies]` y `[modules]`.

Dentro de la sección `[properties]`, los comentarios (líneas que empiezan por `#` o `##`) se conservan y se usan como **separadores de sección** en `gradle.properties`. Esto ayuda a organizar la configuración generada en grupos lógicos.

```properties title="example.template"
[properties]
## Main-UI
key1=value1
key2=value2

#COPILOT
key3=value3

[dependencies]
implementation 'com.example:library:1.0.0'

[modules]
com.etendoerp:mymodule:1.0.0
```

#### Soporte de placeholders

Las plantillas pueden usar **placeholders** con el formato `{placeholder.name}` dentro de los valores de propiedades. Cuando la tarea detecta placeholders, solicita automáticamente al usuario los valores y los sustituye antes de aplicar la plantilla.

```properties title="server.template (excerpt)"
[properties]
etendo.classic.host={context.url}
next.public.app.url={context.host}
OPENAI_API_KEY={openai.api.key}
```

Los nombres de placeholders pueden contener letras, números, puntos y guiones bajos (p. ej., `{context.url}`, `{openai.api.key}`).

#### Detalles de secciones

##### `[properties]`

Las propiedades se aplican al archivo `gradle.properties`. Cada línea debe seguir el formato `key=value`.

- Si una propiedad ya existe, se actualiza su valor.
- Si una propiedad no existe, se añade al final.
- Las líneas de comentario (`#` o `##`) dentro de esta sección se escriben como separadores de sección en el archivo de salida.
- Los valores sensibles (claves que contienen `KEY`, `TOKEN`, `PASSWORD` o `SECRET`) se enmascaran en la salida de consola por seguridad.

##### `[dependencies]`

Las dependencias se añaden al bloque `dependencies {}` en `build.gradle`.

- Soporta cualquier configuración válida de dependencias de Gradle (`implementation`, `runtimeOnly`, `testImplementation`, etc.).
- Si una dependencia ya existe, se omite.
- Las nuevas dependencias se agrupan bajo un comentario `// Template Dependencies`.

##### `[modules]`

Los módulos pueden especificarse en dos formatos:

| Tipo | Formato | Ejemplo |
|---|---|---|
| Artefacto | `group:artifact:version` | `com.etendoerp:copilot-extras:1.0.0` |
| Repositorio Git | `git::<url>::branch=<branch>` | `git::https://github.com/etendosoftware/com.etendoerp.task.git::branch=main` |

- Los **módulos de artefacto** se añaden al archivo `artifacts.list.COMPILATION.gradle`. Si ya existen, se omiten.
- Los **módulos Git** se clonan en el directorio `modules/`. Si el directorio destino ya existe, se omite el clonado. Si no se especifica rama, la tarea intenta `main`, luego `master` y después la rama por defecto del repositorio.

### Mecanismo de copia de seguridad

Antes de aplicar cualquier cambio, la tarea crea automáticamente copias de seguridad de los archivos que se van a modificar:

- `gradle.properties` se respalda en `.template-backups/gradle.properties.<timestamp>`
- `build.gradle` se respalda en `.template-backups/build.gradle.<timestamp>`

El formato del timestamp es `yyyyMMdd_HHmmss`. Estas copias de seguridad permiten restaurar configuraciones anteriores si es necesario.

### Creación de plantillas personalizadas

El sistema de plantillas es **extensible**: cualquier archivo `.template` añadido al directorio `src/main/resources/templates/` del plugin se descubre automáticamente y se lista en el menú interactivo. No se requieren cambios de código.

Para crear una plantilla personalizada:

1. Crea un archivo nuevo con la extensión `.template`.
2. Añade las secciones deseadas (`[properties]`, `[dependencies]`, `[modules]`) con el contenido apropiado.
3. Usa la sintaxis `{placeholder.name}` para valores que deban proporcionarse de forma interactiva.
4. Aplícala usando la opción `--file` o `--url`, o añádela al directorio de recursos para su descubrimiento automático.

#### Ejemplo: plantilla personalizada con placeholders

```properties title="staging.template"
[properties]
## Base de datos
bbdd.driver=org.postgresql.Driver
bbdd.url=jdbc:postgresql://{db.host}:5432/{db.name}
context.name={app.context}

## Entorno
environment=staging
log.level=INFO

[dependencies]
implementation 'com.etendoerp:copilot:1.0.0'

[modules]
com.etendoerp:mymodule:1.0.0
```

Aplicarla:

```bash title="Terminal"
./gradlew setup.applyTemplates --file=./staging.template
```

!!!info
    Las plantillas personalizadas cargadas mediante `--file` o `--url` que contengan placeholders también activarán el prompt interactivo. Sin embargo, solo los placeholders que coincidan con las definiciones de prompt integradas mostrarán mensajes descriptivos; el resto usará un prompt genérico.

### Integración CI/CD

La tarea `setup.applyTemplates` puede usarse en pipelines de CI/CD. Como los prompts interactivos requieren entrada del usuario, usa la plantilla `local` o una plantilla personalizada sin placeholders en contextos automatizados.

#### Ejemplo: GitHub Actions

```yaml title=".github/workflows/setup.yml"
- name: Apply Etendo template
  run: ./gradlew setup.applyTemplates --template=local --force
```

#### Ejemplo: plantilla remota en CI

```bash title="Terminal"
./gradlew setup.applyTemplates --url=$TEMPLATE_URL --force
```

!!!info
    Usa siempre el flag `--force` en entornos CI/CD donde el estado de la **Base de datos** puede variar entre ejecuciones. Evita usar la plantilla `server` en CI/CD, ya que requiere entrada interactiva.

### Flujo de ejecución

Cuando se ejecuta la tarea, sigue esta secuencia:

1. **Validación del entorno** — Comprueba si ya existe una **Base de datos** (a menos que se haya establecido `--force`).
2. **Resolución de plantilla** — Carga la plantilla desde el origen especificado (recursos, archivo, URL o selección interactiva).
3. **Resolución de placeholders** — Si la plantilla contiene placeholders, solicita al usuario los valores y los sustituye.
4. **Creación de copia de seguridad** — Crea copias de seguridad con timestamp de `gradle.properties` y `build.gradle`.
5. **Aplicación de plantilla** — Aplica propiedades (con separadores de sección), dependencias y módulos desde la plantilla.
6. **Ejecución de setup** — Ejecuta `./gradlew setup` automáticamente para aplicar los cambios de configuración.

#### Ejemplo de salida

```text
Applying template: local
  [properties] -> gradle.properties
  docker_com.etendoerp.mainui=true
  etendo.classic.url=http://host.docker.internal:8080/etendo
  etendo.classic.host=https://localhost:8080/etendo
  next.public.app.url=https://localhost:3000/
  authentication.class=com.etendoerp.etendorx.auth.SWSAuthenticationManager
  ws.maxInactiveInterval=3600
  docker_com.etendoerp.copilot=true
  COPILOT_HOST=localhost
  COPILOT_PORT=5005
  OPENAI_API_KEY=****
  ETENDO_HOST=http://localhost:8080/etendo
  ETENDO_HOST_DOCKER=http://host.docker.internal:8080/etendo

Template 'local' applied successfully
```

!!!note
    Los valores sensibles (claves API, tokens, contraseñas) se enmascaran automáticamente en la salida de consola.

## Resolución de problemas

| Problema | Causa | Solución |
|---|---|---|
| `Template '<name>' not found in resources` | La plantilla incluida especificada no existe | Ejecuta la tarea sin opciones para ver las plantillas disponibles, o usa `--file`/`--url` en su lugar |
| `Template file not found: <path>` | La ruta del archivo local es incorrecta o el archivo no existe | Verifica la ruta del archivo y asegúrate de que el archivo existe |
| `Failed to load template from URL` | La URL no es accesible o devolvió un error | Comprueba la URL, la conectividad de red y asegúrate de que el servidor remoto es accesible |
| `Database already exists` | El proyecto ya tiene una **Base de datos** configurada | Usa el flag `--force` para omitir esta comprobación, o elimina primero la **Base de datos** existente |
| `Value for '<key>' cannot be empty` | Se proporcionó un valor vacío durante el prompt interactivo | Proporciona un valor no vacío para todos los campos solicitados |
| `Could not find dependencies block in build.gradle` | El archivo `build.gradle` no contiene un bloque `dependencies {}` | Asegúrate de que `build.gradle` tiene un bloque `dependencies { }` válido antes de ejecutar la tarea |
| `Invalid git module format` | La línea del módulo git no sigue el formato esperado | Usa el formato `git::<url>::branch=<branch>` |

---

- This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.