---
title: How to Use Setup Apply Templates
tags:
  - How to
  - Gradle
  - Setup
  - Configuration
  - Templates
---

# How to Use Setup Apply Templates

## Overview

The `setup.applyTemplates` Gradle task allows you to quickly configure an Etendo project using predefined or custom templates. Templates are files that contain properties, dependencies, and modules that are applied automatically to your project, streamlining both initial setup and environment-specific configurations.

The plugin ships with two built-in templates: **local** (for local development) and **server** (for server/production deployments with interactive configuration). The system is extensible — any `.template` file added to the plugin resources is automatically discovered and made available.

This guide explains how to use the task, the available templates, the template format, placeholder support, and how to create custom templates.

## Prerequisites

- An Etendo project with the Gradle plugin installed.
- The project should not have a database already configured. If it does, use the `--force` flag to override this check.

## Usage

The task can be executed in four different modes: interactive selection, bundled template, local file, or remote URL.

### Interactive Mode

When no options are provided, the task presents an interactive menu to select from the available bundled templates:

```bash title="Terminal"
./gradlew setup.applyTemplates
```

Output:

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

### Apply a Bundled Template

Use the `--template` option to apply one of the templates included with the plugin:

```bash title="Terminal"
./gradlew setup.applyTemplates --template=local
```

### Apply a Template from a Local File

Use the `--file` option to apply a template stored on your local filesystem:

```bash title="Terminal"
./gradlew setup.applyTemplates --file=/path/to/custom.template
```

### Apply a Template from a Remote URL

Use the `--url` option to download and apply a template from a remote location:

```bash title="Terminal"
./gradlew setup.applyTemplates --url=https://example.com/templates/my-setup.template
```

### Force Mode

By default, the task checks whether a database already exists for the project. If it does, the task aborts to prevent unintended modifications. To skip this check, use the `--force` flag:

```bash title="Terminal"
./gradlew setup.applyTemplates --template=local --force
```

!!!warning
    Using `--force` skips the environment validation. Make sure you understand the implications before applying a template to an already-configured project.

## Available Options

| Option | Description | Example |
|---|---|---|
| `--template` | Name of a bundled template from plugin resources | `--template=local` |
| `--file` | Path to a local `.template` file | `--file=/path/to/custom.template` |
| `--url` | URL to a remote `.template` file | `--url=https://example.com/my.template` |
| `--force` | Skip the database existence check | `--force` |

## Bundled Templates

### `local` — Local Development

Designed for local development environments. Most values are preconfigured with sensible defaults. The only value that requires user input is the **OpenAI API Key**.

```bash title="Terminal"
./gradlew setup.applyTemplates --template=local
```

#### Interactive Configuration

When applied, the task prompts for the following value:

| # | Prompt | Description |
|---|---|---|
| 1 | OpenAI API Key | Your OpenAI API key for Copilot integration. Input is masked for security. |

### `server` — Server / Production Deployment

Designed for server and production environments. This template uses **placeholders** that are resolved interactively during execution — the user is prompted to provide environment-specific values.

```bash title="Terminal"
./gradlew setup.applyTemplates --template=server
```

#### Interactive Configuration

When applied, the task prompts for the following values:

| # | Prompt | Variable | Description |
|---|---|---|---|
| 1 | Etendo ERP URL | `context.url` | The full web address of your Etendo ERP application (e.g., `http://myserver.com/etendo`). From this value, `context.name` (last path segment) and `context.host` (base URL without the context name) are derived automatically. |
| 2 | OpenAI API Key | `openai.api.key` | Your OpenAI API key for Copilot integration. Input is masked for security. |

**Example interaction:**

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

#### Derived Values

From the `context.url` input, the following values are automatically derived:

| Input | Derived Variable | Value |
|---|---|---|
| `http://myserver.com/etendo` | `context.name` | `etendo` |
| | `context.host` | `http://myserver.com/` |

These derived values are used to configure:

- `etendo.classic.url` → `http://host.docker.internal:80/{context.name}`
- `etendo.classic.host` → `{context.url}`
- `next.public.app.url` → `{context.host}`

## Advanced Features

### Template Format

Templates use an INI-like format with three sections: `[properties]`, `[dependencies]`, and `[modules]`.

Within the `[properties]` section, comments (lines starting with `#` or `##`) are preserved and used as **section separators** in `gradle.properties`. This helps organize the generated configuration into logical groups.

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

#### Placeholder Support

Templates can use **placeholders** in the format `{placeholder.name}` within property values. When the task detects placeholders, it automatically prompts the user for values and substitutes them before applying the template.

```properties title="server.template (excerpt)"
[properties]
etendo.classic.host={context.url}
next.public.app.url={context.host}
OPENAI_API_KEY={openai.api.key}
```

Placeholder names can contain letters, numbers, dots, and underscores (e.g., `{context.url}`, `{openai.api.key}`).

#### Section Details

##### `[properties]`

Properties are applied to the `gradle.properties` file. Each line must follow the `key=value` format.

- If a property already exists, its value is updated.
- If a property does not exist, it is appended.
- Comment lines (`#` or `##`) within this section are written as section separators in the output file.
- Sensitive values (keys containing `KEY`, `TOKEN`, `PASSWORD`, or `SECRET`) are masked in console output for security.

##### `[dependencies]`

Dependencies are added to the `dependencies {}` block in `build.gradle`.

- Supports any valid Gradle dependency configuration (`implementation`, `runtimeOnly`, `testImplementation`, etc.).
- If a dependency already exists, it is skipped.
- New dependencies are grouped under a `// Template Dependencies` comment.

##### `[modules]`

Modules can be specified in two formats:

| Type | Format | Example |
|---|---|---|
| Artifact | `group:artifact:version` | `com.etendoerp:copilot-extras:1.0.0` |
| Git repository | `git::<url>::branch=<branch>` | `git::https://github.com/etendosoftware/com.etendoerp.task.git::branch=main` |

- **Artifact modules** are added to the `artifacts.list.COMPILATION.gradle` file. If already present, they are skipped.
- **Git modules** are cloned into the `modules/` directory. If the target directory already exists, the clone is skipped. If no branch is specified, the task tries `main`, then `master`, then the repository default.

### Backup Mechanism

Before applying any changes, the task automatically creates backups of the files that will be modified:

- `gradle.properties` is backed up to `.template-backups/gradle.properties.<timestamp>`
- `build.gradle` is backed up to `.template-backups/build.gradle.<timestamp>`

The timestamp format is `yyyyMMdd_HHmmss`. These backups allow you to restore previous configurations if needed.

### Creating Custom Templates

The template system is **extensible**: any `.template` file added to the plugin's `src/main/resources/templates/` directory is automatically discovered and listed in the interactive menu. No code changes are required.

To create a custom template:

1. Create a new file with the `.template` extension.
2. Add the desired sections (`[properties]`, `[dependencies]`, `[modules]`) with the appropriate content.
3. Use `{placeholder.name}` syntax for values that should be provided interactively.
4. Apply it using the `--file` or `--url` option, or add it to the resources directory for automatic discovery.

#### Example: Custom Template with Placeholders

```properties title="staging.template"
[properties]
## Database
bbdd.driver=org.postgresql.Driver
bbdd.url=jdbc:postgresql://{db.host}:5432/{db.name}
context.name={app.context}

## Environment
environment=staging
log.level=INFO

[dependencies]
implementation 'com.etendoerp:copilot:1.0.0'

[modules]
com.etendoerp:mymodule:1.0.0
```

Apply it:

```bash title="Terminal"
./gradlew setup.applyTemplates --file=./staging.template
```

!!!info
    Custom templates loaded via `--file` or `--url` that contain placeholders will also trigger interactive prompting. However, only placeholders that match the built-in prompt definitions will display descriptive messages — other placeholders will use a generic prompt.

### CI/CD Integration

The `setup.applyTemplates` task can be used in CI/CD pipelines. Since interactive prompts require user input, use the `local` template or a custom template without placeholders in automated contexts.

#### Example: GitHub Actions

```yaml title=".github/workflows/setup.yml"
- name: Apply Etendo template
  run: ./gradlew setup.applyTemplates --template=local --force
```

#### Example: Remote Template in CI

```bash title="Terminal"
./gradlew setup.applyTemplates --url=$TEMPLATE_URL --force
```

!!!info
    Always use the `--force` flag in CI/CD environments where the database state may vary between runs. Avoid using the `server` template in CI/CD as it requires interactive input.

### Execution Flow

When the task runs, it follows this sequence:

1. **Environment validation** — Checks if a database already exists (unless `--force` is set).
2. **Template resolution** — Loads the template from the specified source (resources, file, URL, or interactive selection).
3. **Placeholder resolution** — If the template contains placeholders, prompts the user for values and substitutes them.
4. **Backup creation** — Creates timestamped backups of `gradle.properties` and `build.gradle`.
5. **Template application** — Applies properties (with section separators), dependencies, and modules from the template.
6. **Setup execution** — Runs `./gradlew setup` automatically to apply the configuration changes.

#### Example Output

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
    Sensitive values (API keys, tokens, passwords) are automatically masked in the console output.

## Troubleshooting

| Issue | Cause | Solution |
|---|---|---|
| `Template '<name>' not found in resources` | The specified bundled template does not exist | Run the task without options to see available templates, or use `--file`/`--url` instead |
| `Template file not found: <path>` | The local file path is incorrect or the file does not exist | Verify the file path and ensure the file exists |
| `Failed to load template from URL` | The URL is unreachable or returned an error | Check the URL, network connectivity, and ensure the remote server is accessible |
| `Database already exists` | The project already has a configured database | Use the `--force` flag to skip this check, or remove the existing database first |
| `Value for '<key>' cannot be empty` | An empty value was provided during interactive prompting | Provide a non-empty value for all prompted fields |
| `Could not find dependencies block in build.gradle` | The `build.gradle` file does not contain a `dependencies {}` block | Ensure `build.gradle` has a valid `dependencies { }` block before running the task |
| `Invalid git module format` | The git module line does not follow the expected format | Use the format `git::<url>::branch=<branch>` |

---

- This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.
