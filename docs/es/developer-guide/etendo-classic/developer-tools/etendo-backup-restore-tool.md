---
title: Plugin de copia de seguridad y restauración de Etendo
tags: 
  - Plugin
  - Gradle
  - Copia de seguridad
  - Restauración
---

## Visión general

Este artículo explica cómo utilizar el plugin de copia de seguridad y restauración de Etendo en Etendo Classic. Este plugin le permite generar y restaurar copias de seguridad de Etendo de forma sencilla.

## Instalar plugin

Para utilizar la herramienta de copia de seguridad y restauración de Etendo, debe añadir el id del plugin en el archivo `build.gradle`, con la versión seleccionada.

``` groovy  title="build.gradle"
plugins {
    id 'com.etendoerp.etendobackup' version '<version>'
}
```

!!! info
    Para conocer las versiones disponibles del plugin, visite las [Notas de la versión](../../../whats-new/release-notes/etendo-classic/plugins/etendo-backup-restore-plugin/release-notes.md).

Para resolver las dependencias del plugin, debe añadir las siguientes líneas al inicio del archivo `settings.gradle`

``` groovy  title="settings.gradle"
pluginManagement {
    repositories {
        maven {
            url 'https://maven.pkg.github.com/etendosoftware/com.etendoerp.etendobackup'
            credentials {
                username "${githubUser}"
                password "${githubToken}"
            }
        }
        mavenCentral()
    }
}
```

!!! warning
    Asegúrese de tener sus credenciales de Github (`githubUser` y `githubToken`) configuradas en el archivo `gradle.properties`.

## Tarea de copia de seguridad

Para ejecutar la copia de seguridad, ejecute

``` bash title="Terminal"
./gradlew backup -PbkpMode=<mode>
```

Donde el modo puede ser `manual` o `auto`. Si no se especifica el parámetro, el modo por defecto es `manual`.

### Archivo de propiedades de copia de seguridad

El archivo `backup.properties` se encuentra dentro de la carpeta `config` en la raíz del proyecto.
Si no existe, ejecute `./gradlew setup` para generar los archivos faltantes.

También puede proporcionar una ubicación personalizada de `backup.properties` añadiendo el siguiente bloque dentro de `build.gradle`.
``` groovy title="build.gradle"
backup {
    configPath = "/path/to/backup.properties"
}
```

`backup.properties` contiene la mayoría de las propiedades que debe personalizar antes de ejecutar la copia de seguridad.

* `USER`
Configura el usuario que ejecutará la copia de seguridad.

* `GROUP`
Configura el grupo relacionado con el usuario que ejecuta la copia de seguridad.

* `BACKUPS_DIR`
Configura la ruta donde se almacenará la copia de seguridad.

    !!! warning
        Asegúrese de que el directorio donde se almacenarán las copias de seguridad ya esté creado y de que el usuario configurado tenga permisos de escritura sobre él.

* `BACKUPS_TMP_DIR`
Configura la ruta donde se creará el directorio temporal para almacenar los archivos generados.

* `ATTACH_COPY`
Configura un indicador (`yes` o `no`) para incluir en la copia de seguridad los adjuntos externos (si están contenidos).

* `ATTACH_IN_BKP`
Configura un indicador (`yes` o `no`) para incluir en la copia de seguridad los adjuntos de origen.

#### Propiedades de correo electrónico

Estas propiedades se utilizan cuando la copia de seguridad se ejecuta en modo `auto`.

* `EMAIL_FROM`
Configura la dirección que envía los correos electrónicos.
* `EMAIL_SERVER`
Configura la dirección del servidor de correo electrónico.
* `EMAIL_PORT`
Configura el puerto del servidor de correo electrónico.
* `EMAIL_USER`
Configura la dirección del usuario que envía los correos electrónicos.
* `EMAIL_PASSWORD`
Configura la contraseña del usuario de correo electrónico.
* `EMAIL_ENVIRONMENT`
Especifica el entorno para el envío de correos electrónicos.

Dependiendo del `STATE` final, se utilizan las siguientes propiedades para especificar la dirección de correo electrónico a la que enviar los correos.

!!! failure "Error" 
    * `EMAIL_ERROR_TO`
      Configura la dirección de correo electrónico a la que se enviarán los correos de error.
    * `EMAIL_ERROR_CC`
      Configura la dirección de correo electrónico a la que se enviarán copias (CC) en caso de error.
    * `EMAIL_ERROR_SUBJECT`
      Configura el asunto del correo de error.

!!! warning 
    * `SEND_EMAIL_ON_WARNING`
      Especifica si se debe enviar una notificación por correo electrónico en caso de advertencia durante el proceso de copia de seguridad. Los valores aceptados son `yes` o `no`.
    * `EMAIL_WARNING_TO`
      Configura la dirección de correo electrónico a la que se enviarán los correos de advertencia.
    * `EMAIL_WARNING_CC`
      Configura la dirección de correo electrónico a la que se enviarán copias (CC) en caso de advertencia.
    * `EMAIL_WARNING_SUBJECT`
      Configura el asunto del correo de advertencia.

!!! success 
    * `SEND_EMAIL_ON_SUCCESS`
      Especifica si se debe enviar una notificación por correo electrónico en caso de éxito durante el proceso de copia de seguridad. Los valores aceptados son `yes` o `no`.
    * `EMAIL_WARNING_TO`
      Configura la dirección de correo electrónico a la que se enviarán los correos de éxito.
    * `EMAIL_WARNING_CC`
      Configura la dirección de correo electrónico a la que se enviarán copias (CC) en caso de éxito.
    * `EMAIL_WARNING_SUBJECT`
      Configura el asunto del correo de éxito.

!!! note
    Para enviar el correo electrónico a múltiples cuentas, separe las direcciones con `;`.<br>
    Por ejemplo: `EMAIL_ERROR_CC=user1@etendo.software;user2@etendo.software`

### Estados finales
Los siguientes son los posibles estados al final de la tarea `backup`:

!!! failure "Error" 
    Ocurre cuando falla la creación de la copia de seguridad. Se debe enviar un correo electrónico según las propiedades especificadas.

!!! warning
    La copia de seguridad finaliza con mensajes de advertencia. Si el indicador `SEND_EMAIL_ON_WARNING` está configurado en yes, se debe enviar un correo electrónico según las propiedades especificadas.

!!! success
    La copia de seguridad finaliza sin advertencias ni errores. Si el indicador `SEND_EMAIL_ON_SUCCESS` está configurado en yes, se debe enviar un correo electrónico según las propiedades especificadas.

## Tarea de restauración

!!! warning
    El usuario que ejecute la restauración debe tener acceso `SUDO`.

Para ejecutar la restauración, ejecute

``` bash title="Terminal"
./gradlew restore -PbackupPath=/path/to/backup
```

Sustituya `/path/to/backup/` por la ubicación de la copia de seguridad que se va a restaurar.

Se mostrará un menú donde puede elegir múltiples opciones a realizar.

!!! warning
    Asegúrese de que todas las opciones seleccionadas sean correctas. Los directorios de destino seleccionados y la base de datos serán SOBRESCRITOS.

1. *Verificación de usuario*<br>
  Debe ejecutar la restauración con acceso `SUDO` (recomendado). En caso de no tener permisos, tendrá la opción de introducir la contraseña de `SUDO`.

2. *Destino de fuentes*<br>
  Puede seleccionar la ubicación en la que se restaurarán las fuentes. La ruta por defecto se establece en el directorio raíz del proyecto desde el que se está ejecutando el comando de restauración.

3. *Verificación de adjuntos*<br>
  Puede seleccionar mantener o ignorar la copia de adjuntos (externos o contenidos dentro de las fuentes).

4. *Verificación de propiedades*<br>
  Puede seleccionar qué propiedades utilizar.

    !!! info
        Las propiedades configuran las opciones que utilizará la base de datos en la restauración.

    - *Propiedades del proyecto*<br>
      Obtenidas del archivo `gradle.properties` dentro del proyecto actual que ejecuta la restauración. 
      Puede cambiar estas propiedades para seleccionar, por ejemplo, el nombre de la base de datos a restaurar.
      Una vez finalizada la restauración, las propiedades dentro de `config/Openbravo.properties` se actualizarán con las seleccionadas.

    - *Propiedades de las fuentes originales*<br>
      Obtenidas del archivo `gradle.properties` dentro de las fuentes originales.
      La base de datos se restaurará con las opciones originales (esto podría sobrescribir una base de datos existente)
      Las propiedades dentro de `config/Openbravo.properties` no cambiarán.

5. *Propiedades de la base de datos*<br>
  Al final, se mostrará un mensaje con las propiedades que utilizará la base de datos para ser restaurada. Estas propiedades dependen de las seleccionadas previamente.


---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.