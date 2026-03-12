---
title: Uso de repositorios en Etendo
tags:
    - Repositorios
    - Paquetes
    - Token de acceso
---

# Uso de repositorios en Etendo

## Visión general
Etendo admite cualquier repositorio de paquetes Maven, pero esta guía se centra en configurar las credenciales para los repositorios estándar de Etendo.

!!! tip
    De forma predeterminada, Etendo Classic y los bundles de extensiones se descargan desde los [repositorios de GitHub de Etendo](https://github.com/etendosoftware){target=_isblank}.

Para acceder a los repositorios de GitHub de Etendo y resolver dependencias, necesita las credenciales adecuadas. Esto implica usar un **Token de acceso personal**. Esta guía explica cómo configurar y utilizar estas credenciales.

## Token de GitHub

### Generación de un Token de acceso personal

!!! info
    Como parte de su licencia de Etendo, recibirá una invitación por correo electrónico para unirse al **equipo de partners de Etendo** en GitHub. Debe crear o asociar una cuenta de GitHub con el correo electrónico invitado. Su usuario tendrá entonces acceso de lectura a todos los repositorios de Etendo.

Siga estos pasos para generar un Token de acceso personal:

1. Inicie sesión en su **cuenta de GitHub**.
2. Haga clic en su foto de perfil en la esquina superior derecha y seleccione **Configuración**.
3. Vaya a **Configuración de desarrollador** en el menú de la izquierda y haga clic en **Tokens de acceso personal**.

    ![personal-access-tokens.png](../../../../assets/developer-guide/etendo-classic/getting-started/instalation/use-of-repositories-in-etendo/personal-access-tokens.png) 

4. Haga clic en **Generar nuevo token (clásico)**.

5. Proporcione un **Nombre** para su token y seleccione los permisos necesarios. Como mínimo, asegúrese de que el permiso `read:packages` esté seleccionado.

    !!! warning
        Se recomienda encarecidamente establecer una fecha de caducidad para el token. Sin embargo, también puede optar por dejarlo sin fecha de caducidad.

    ![new-personal-access-token.png](../../../../assets/developer-guide/etendo-classic/getting-started/instalation/use-of-repositories-in-etendo/new-personal-access-token.png) 

6. Haga clic en *Generar token* y copie el valor del token.

    !!! warning
        No podrá volver a ver el token, así que asegúrese de copiarlo y almacenarlo de forma segura.

### Configuración del Token de GitHub en proyectos de Etendo

Después de generar un **Token de acceso personal**, configúrelo en su proyecto de Etendo siguiendo estos pasos:

1. Abra el archivo `gradle.properties` en su proyecto.
2. Añada las siguientes líneas, sustituyendo `YOUR_GITHUB_USERNAME` y `YOUR_PERSONAL_ACCESS_TOKEN` por su nombre de usuario de GitHub y su token reales:
        
    ```properties title="gradle.properties"
    nexusUser=
    nexusPassword=
    githubUser=YOUR_GITHUB_USERNAME
    githubToken=YOUR_PERSONAL_ACCESS_TOKEN
    context.name=etendo
    bbdd.sid=etendo
    bbdd.port=5432
    ```

3. Guarde el archivo `gradle.properties`.

### Uso del Token de acceso personal en tareas de Gradle

Una vez configurado su **Token de GitHub**, las tareas de Gradle pueden interactuar sin problemas con los repositorios de GitHub de Etendo. Por ejemplo, al ejecutar el siguiente comando:

```bash title="Terminal"
./gradlew dependencies
```

Gradle utilizará automáticamente su *Token de acceso personal* para autenticarse con GitHub y resolver dependencias de forma segura.

### Revocación de un Token de acceso personal

Si ya no necesita un token o sospecha que se ha visto comprometido, revóquelo inmediatamente siguiendo estos pasos:

1. Vaya a su página de **Configuración** en GitHub.
2. Vaya a **Configuración de desarrollador** en la barra lateral izquierda.
3. Haga clic en **Tokens de acceso personal**.
4. Localice el token que desea revocar y haga clic en **Revocar**.
5. Confirme la revocación.

El token se invalidará inmediatamente y ya no podrá utilizarse.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.