---
title: Plugin de pruebas de Etendo
tags:
  - Plugin
  - Gradle
  - Pruebas
  - JUnit
  - Spock
---

## Visión general

Este artículo describe cómo utilizar el Plugin de pruebas de Etendo. Este plugin proporciona un entorno de pruebas estandarizado compatible con Groovy, Spock, JUnit 4/5 y Mockito para proyectos de Etendo Classic.

---

## Instalación

Añada el plugin a su archivo `build.gradle`:

```groovy title="build.gradle"
plugins {
    id 'com.etendoerp.testing.gradleplugin' version '<version>'
}
```

!!! info
    Consulte las versiones disponibles del plugin en las [Notas de la versión](../../../whats-new/release-notes/etendo-classic/plugins/etendo-testing-plugin/release-notes.md).

## Estructura de pruebas

El plugin incluye los siguientes directorios de pruebas de forma predeterminada:

```
src-test/
├── src/          → Fuentes de pruebas Java
├── test/groovy/  → Pruebas Groovy/Spock
├── resources/    → Recursos de pruebas
```

También incluye dinámicamente fuentes de pruebas desde:

- `modules/**/src-test/src`
- `modules_core/**/src-test`

---

## Ejemplo de uso

Ejecutar pruebas:

```bash
./gradlew test
```

Generar informes:

- Los informes HTML de Spock están habilitados mediante `spock-reports`
- Utilice los informes de pruebas estándar de Gradle en `build/reports/tests/test/index.html`

---

## Opciones avanzadas

Puede añadir bibliotecas adicionales a `lib/test/` y se incluirán automáticamente:

```groovy
testImplementation fileTree(project.projectDir) {
    include "lib/test/*.jar"
}
```

El plugin también registra una tarea auxiliar opcional:

```bash
./gradlew depsTest
```

Que inyecta dependencias en tiempo de compilación en `testImplementation`.

---

## Tecnologías utilizadas

- Groovy 3.0.9  
- Spock Framework 2.0 (Groovy 3)
- JUnit 4.13.1 + JUnit Platform
- Mockito 5.0.0
- Spock Reports 2.0

---

## Compatibilidad

| Versión del plugin | Gradle | Java |
|--------------------|--------|------|
| 1.0.0              | 7.0+   | 11+  |
| 2.0.0              | 8.0+   | 17+  |

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.