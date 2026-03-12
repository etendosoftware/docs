# Cómo iniciar RX como servicio desde el código fuente

Este documento le guía a través del proceso de iniciar el servicio RX desde el código fuente, incluyendo la generación de archivos JAR y el arranque de varios componentes.

## 1. Generación de JARs

Asegúrese de haber construido los archivos JAR necesarios para los distintos componentes del servicio. Use estos comandos en su terminal:

```bash
./gradlew com.etendorx.entities:build 
./gradlew com.etendorx.das:build -x test
./gradlew com.etendorx.config:build -x test
./gradlew com.etendorx.auth:build -x test
```

## 2. Inicio del servidor de configuración

Antes de iniciar el servidor de configuración, confirme que sus archivos de configuración están correctamente configurados.

**Archivos de configuración:**
Asegúrese de que los archivos requeridos, como `service.yaml`, estén presentes en el directorio designado (`/path/to/directory/rxconfig`).

**Configuración de variables de entorno:**
Configure las variables de entorno necesarias para dirigir el servidor de configuración a estos archivos:

```bash
export SPRING_PROFILES_ACTIVE=native
export SPRING_CLOUD_CONFIG_SERVER_NATIVE_SEARCH_LOCATIONS=$(pwd)/rxconfig
```

**Inicio del servicio de configuración:**

```bash
java -jar modules_core/com.etendorx.config/build/libs/com.etendorx.config-1.1.0.jar
```

## 3. Inicio de DAS

Use este comando para iniciar el servicio DAS, asegurándose de que la ruta y la versión sean correctas para el JAR de entidades generado.

```bash
java -Dloader.path=modules_gen/com.etendorx.entities/build/libs/com.etendorx.entities-1.1.0-plain.jar -jar modules_core/com.etendorx.das/build/libs/com.etendorx.das-1.1.0.jar
```

!!!info
    - **Validación:** Confirme que todas las rutas y los nombres de archivo en los comandos se alinean con la estructura de su proyecto.
    - **Dependencias:** Verifique que todas las dependencias necesarias estén instaladas antes de ejecutar estos comandos.
    - **Pruebas:** Se recomienda probar cada paso en un entorno de desarrollo antes del despliegue en producción.

## 4. Inicio de AUTH

Para iniciar el servicio AUTH, ejecute el siguiente comando, asegurándose de que la ruta y la versión del JAR de entidades generado sean correctas.

```bash
java -jar modules_core/com.etendorx.auth/build/libs/com.etendorx.auth-1.1.0.jar
```

## 5. Inicio de EDGE

Para iniciar el servicio EDGE, ejecute el siguiente comando, asegurándose de que la ruta y la versión del JAR de entidades generado sean correctas.

```bash
java -jar modules_core/com.etendorx.edge/build/libs/com.etendorx.edge-1.1.0.jar
```

### Descargo de responsabilidad: se requieren conocimientos avanzados

Esta guía asume una comprensión fundamental de los entornos de desarrollo Java, incluyendo familiaridad con los comandos de compilación de Gradle y el despliegue de aplicaciones Java. Está destinada a usuarios con habilidades técnicas intermedias a avanzadas en desarrollo de software y administración de sistemas. Los usuarios nuevos o aquellos que no estén familiarizados con los conceptos tratados pueden necesitar recursos adicionales o asistencia.

---
Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L](https://etendo.software){target="_blank"}.