---
tags:
  - Etendo RX
  - oAuth
  - Inicio de sesión SSO
  - Middleware
---

# Etendo RX 
:octicons-package-16: Paquete Java: `com.etendoerp.etendorx`

## Inicio de sesión SSO de Etendo

Etendo le permite autenticarse utilizando estas cuentas de proveedores externos: **Google**, **Microsoft**, **LinkedIn**, **GitHub** y **Facebook**. El uso del protocolo Single Sign-On (SSO) es posible gracias a la integración a través de:

- [Servicio EtendoAuth Middleware](#configurar-etendo-para-iniciar-sesión-con-el-servicio-etendoauth-middleware-recomendado)
- [Implementación personalizada de Auth0](#cómo-integrar-su-propio-proveedor-de-inicio-de-sesión-auth0-con-etendo-opcional)

### Configurar Etendo para iniciar sesión con el servicio EtendoAuth Middleware (Recomendado)

Para habilitar el inicio de sesión en **Etendo** utilizando proveedores externos (Google, Microsoft, LinkedIn, GitHub o Facebook), debe realizar dos pasos principales:

- [x] Habilitar la funcionalidad SSO (Single Sign-On) mediante una preferencia del sistema
- [x] Configurar los ajustes de conexión en `gradle.properties`

---

1. #### Habilitar la preferencia de inicio de sesión SSO

    1. Inicie sesión como **Administrador del sistema**
    2. Vaya a la ventana **Preferencias**
    3. Cree una nueva preferencia con la siguiente configuración:

        - **Propiedad**: `Allow SSO Login`  
        - **Seleccionado**: Sí  
        - **Costo**: `Y`

        ![Preferencia SSO](../../../../assets/developer-guide/etendo-classic/bundles/platform/etendo-rx/NewSSOPreference.png)

2. #### Configurar la integración con EtendoAuth Middleware

    - **Configuración interactiva**

        Puede configurar rápidamente el Single Sign-On usando la [Configuración interactiva](../../../../developer-guide/etendo-classic/developer-tools/etendo-interactive-configuration.md):

        ```bash
        ./gradlew setup -Pinteractive=true --console=plain
        ```

        Seleccione **Configuración SSO** y el asistente le guiará paso a paso durante el proceso de configuración.

    - **Configuración manual**

        Para autenticarse mediante **EtendoAuth Middleware**, siga estos pasos:

        1. Abra el archivo `gradle.properties`
        2. Añada las siguientes propiedades:

            ```title="gradle.properties"
            sso.auth.type=Middleware
            sso.middleware.url=https://sso.etendo.cloud
            sso.middleware.redirectUri=http://localhost:8080/etendo/secureApp/LoginHandler.html
            authentication.class=com.etendoerp.etendorx.auth.SWSAuthenticationManager
            ```

            !!! warning
                Este módulo no puede configurarse junto con [Etendo Advanced Security](overview.md#etendo-advanced-security) porque ambos utilizan la propiedad `authentication.class`. 

            !!!note
                Durante el desarrollo, puede usar `localhost`. Sin embargo, para producción, establezca su dominio real.

            Con estos ajustes, Etendo podrá autenticar usuarios mediante proveedores de inicio de sesión externos usando el middleware.

            !!! warning "Posible desajuste en la configuración de SSO"

                ![SSO mal configurado](../../../../assets/developer-guide/etendo-classic/bundles/platform/etendo-rx/MissconfigError.png){width=400 align=right }
            
                Si se omite alguno de los pasos anteriores, al intentar iniciar sesión usando un proveedor externo se mostrará el siguiente mensaje de error:           

                Para resolver este problema, asegúrese de que tanto la preferencia de SSO como la entrada correspondiente en `gradle.properties` estén correctamente configuradas y sean coherentes entre sí.

    !!! info
        Para más información sobre el uso de la funcionalidad de inicio de sesión SSO, visite la [Guía de usuario de inicio de sesión SSO](../../../../user-guide/etendo-classic/optional-features/bundles/platform-extensions/etendo-rx.md#etendo-sso-login).

### Cómo integrar su propio proveedor de inicio de sesión Auth0 con Etendo (Opcional)

Esta opción se recomienda solo si necesita implementar su propio servicio de autenticación y no puede utilizar el servicio EtendoAuth Middleware. Siga esta guía para configurar una aplicación de Auth0 y habilitar el inicio de sesión social en Etendo.


1. #### Crear una nueva aplicación de Auth0

    1. Vaya al panel de control de Auth0:
    [https://manage.auth0.com/dashboard](https://manage.auth0.com/dashboard)
    2. Regístrese o inicie sesión en su cuenta de Auth0. 
    3. Cree una nueva aplicación para la integración con Etendo:

        - En el menú de la izquierda, vaya a **Aplicaciones** → **Aplicaciones**.
        - Haga clic en **Crear aplicación** en la esquina superior derecha.
            ![Aplicaciones](../../../../assets/developer-guide/etendo-classic/bundles/platform/etendo-rx/Applications.png)
        - Elija un nombre y seleccione **Aplicación web regular**.


2. #### Elegir la pila tecnológica

    1. Después de crear la aplicación, elija la tecnología utilizada en el proyecto. Para Etendo, seleccione **Java**.

        ![Elegir tecnología](../../../../assets/developer-guide/etendo-classic/bundles/platform/etendo-rx/ProjectTechnology.png)

    2. Será redirigido a la solapa **Inicio rápido** de la aplicación recién creada.

        ![Inicio rápido de la aplicación](../../../../assets/developer-guide/etendo-classic/bundles/platform/etendo-rx/AppQuickStart.png)


3. #### Configurar proveedores de inicio de sesión social

    1. En el menú de la izquierda, vaya a **Autenticación** → **Social**.

        ![Social](../../../../assets/developer-guide/etendo-classic/bundles/platform/etendo-rx/SocialConnection.png)

    2. Haga clic en **Crear conexión social**.

    3. Elija los proveedores de inicio de sesión social seleccionados (Google, Facebook, etc.).

        ![Nueva conexión social](../../../../assets/developer-guide/etendo-classic/bundles/platform/etendo-rx/NewSocialConnection.png)

    4. Siga los pasos de configuración proporcionados por `Auth0` para cada proveedor.

        ![Configurar nueva conexión social](../../../../assets/developer-guide/etendo-classic/bundles/platform/etendo-rx/ConfigNewSocialConn.png)

    5. Tras la configuración, vaya a la solapa **Aplicaciones** dentro de la conexión y enlácela con su aplicación.

        ![Enlazar social con la aplicación](../../../../assets/developer-guide/etendo-classic/bundles/platform/etendo-rx/SocialAppSelected.png)

    6. Repita este proceso para cada proveedor que desee habilitar.


4. #### Recuperar y establecer credenciales

    1. Vuelva a la aplicación y vaya a la solapa **Ajustes**.

        ![Ajustes de la aplicación](../../../../assets/developer-guide/etendo-classic/bundles/platform/etendo-rx/AppSettings.png)

    2. Localice las siguientes credenciales:
        - **Dominio**
        - **ID de cliente**
        - **Secreto de cliente**

    3. Añádalas al archivo `gradle.properties` con el siguiente formato:

        ``` title="gradle.properties"
        sso.domain.url=your-domain.auth0.com
        sso.client.id=your-client-id
        sso.client.secret=your-client-secret
        sso.auth.type=Auth0
        authentication.class=com.etendoerp.etendorx.auth.SWSAuthenticationManager
        ```

        !!! warning
            Este módulo no puede configurarse junto con [Etendo Advanced Security](overview.md#etendo-advanced-security) porque ambos utilizan la propiedad `authentication.class`.


5. #### Configurar URLs de callback y cierre de sesión

    En la solapa **Ajustes**, configure las siguientes URLs permitidas:

    - **Allowed Callback URLs:**

        Las URLs a las que Auth0 redirige tras un inicio de sesión correcto.

        ```
        http://localhost:8080/etendo/secureApp/LoginHandler.html,
        http://localhost:8080/etendo,
        http://localhost:8080/etendo/web/com.etendoerp.etendorx/LinkAuth0Account.html
        ```

    - **Allowed Logout URLs:**

        Las URLs a las que Auth0 redirige después de que el usuario cierre sesión.
        ```
        http://localhost:8080/etendo,
        http://localhost:8080/etendo/web/com.etendoerp.etendorx/resources/logout-auth0.html
        ```

        ![URIs de la aplicación](../../../../assets/developer-guide/etendo-classic/bundles/platform/etendo-rx/AllowedURIs.png)

    !!!note
        Durante el desarrollo, puede usar `localhost`. Sin embargo, para producción, establezca su dominio real en **URI de inicio de sesión de la aplicación**. Si todavía está en desarrollo, puede dejarlo en blanco.


6. #### Establecer la URL de callback

    Añada la URL de callback a `gradle.properties`:

    ```title="gradle.properties" 
    sso.callback.url=http://localhost:8080/etendo/secureApp/LoginHandler.html
    ```

7. #### Compilar el proyecto

    Una vez configuradas todas las propiedades, compile el proyecto:

    ```bash title="Terminal"
    ./gradlew setup smartbuild
    ```

8. #### Iniciar sesión mediante proveedores externos
    
   
    1. Inicie el servidor Tomcat.
    2. Abra la página de inicio de sesión de Etendo y haga clic en **Usar una cuenta social para iniciar sesión** 
    3. Aquí verá la página de inicio de sesión de `Auth0` con los proveedores configurados.

    ![Inicio de sesión Auth0](../../../../assets/developer-guide/etendo-classic/bundles/platform/etendo-rx/LoginAuth0.png)

    !!!tip
        Personalice la pantalla de inicio de sesión en **Branding** > **Universal Login** en el panel de control de Auth0.

!!! info
    Para más información sobre el uso de la funcionalidad de inicio de sesión SSO, visite la [Guía de usuario de inicio de sesión SSO](../../../../user-guide/etendo-classic/optional-features/bundles/platform-extensions/etendo-rx.md#etendo-sso-login).

## Proveedor OAuth

### Visión general

Esta sección describe el servicio de **autenticación OAuth** incluido en el módulo `Etendo RX`.

El proceso de autenticación OAuth facilita la **configuración del tipo de proveedor**, permitiendo a los usuarios **autenticarse de forma segura y autorizar el acceso** a su información usando su proveedor preferido.

OAuth habilita un método de autenticación mediante un protocolo de seguridad para obtener un token necesario para realizar **llamadas API** y acceder a recursos específicos en nombre de su propietario. Esta autenticación permite a **Etendo** recuperar la información necesaria para acceder a **aplicaciones de terceros**.

### Ventana Proveedor OAuth

:material-menu: `Aplicación`> `Etendo RX`> `Proveedor OAuth`.

Este documento explica cómo configurar un proveedor OAuth para solicitar tokens de acceso. Además, se explica la implementación para conectar **Google Drive** con **Etendo** a través de Etendo Middleware.

Puede elegir entre dos métodos:


- [Etendo Middleware](#configuración-de-etendo-middleware-recomendado) 
    
    Utilice el proveedor preconfigurado ofrecido por **Etendo Middleware**, que simplifica el proceso (método recomendado).

- [Proveedor personalizado](#configurar-manualmente-un-proveedor-opcional)  
    
    Configure manualmente un proveedor externo si prefiere no usar nuestro middleware, lo que le da control total sobre la configuración.

!!! warning
    Al utilizar configuraciones manuales, **EtendoRX** debe estar instalado y configurado correctamente, ya que gestiona la comunicación con los proveedores OAuth directamente. Para más información, visite [Etendo RX](../../../etendo-rx/getting-started.md)



### Configuración de Etendo Middleware (Recomendado)

#### Variables de configuración

Añada las siguientes propiedades al archivo `gradle.properties`:

```properties title="gradle.properties"
## Middleware Configs
sso.middleware.url=https://sso.etendo.cloud
sso.middleware.redirectUri=http://localhost:8080/etendo/secureApp/LoginHandler.html
```
!!!note
    Durante el desarrollo, puede usar `localhost`. Sin embargo, para producción, establezca su dominio real.

#### Compilar el entorno

Ejecute el siguiente comando para compilar y configurar el entorno:

```bash
./gradlew setup smartbuild
```

#### Crear la conexión con Etendo Middleware

- Inicie sesión como **admin**.
- Abra la ventana **Proveedor oAuth**.
- Use el botón de la barra de herramientas: **Crear proveedor de Etendo Middleware**.
  
    ![Configurar proveedor de Middleware](../../../../assets/developer-guide/etendo-classic/bundles/platform/etendo-rx/CreateMiddlewareConfigs.png)

- Tras hacer clic en el botón, actualice la cuadrícula. Aparecerá un nuevo registro que contiene la configuración por defecto para conectar con **Etendo Middleware**.

    ![Proveedor de Etendo Middleware](../../../../assets/developer-guide/etendo-classic/bundles/platform/etendo-rx/EtendoMiddlewareConfigs.png)

#### Obtener token de acceso

- Seleccione el middleware recién creado.
- Haga clic en **Obtener token de Middleware**.

    ![Obtener token de Middleware](../../../../assets/developer-guide/etendo-classic/bundles/platform/etendo-rx/GetMiddlewareToken.png)

- Elija el **scope de Google Drive** deseado:

    ![Selección de scope de Drive](../../../../assets/developer-guide/etendo-classic/bundles/platform/etendo-rx/DriveScopeSelection.png)

    - **Google Drive – Nivel de acceso de edición**
    
        Concede a la aplicación permiso para **crear, actualizar, eliminar y gestionar** archivos creados a través de Etendo.  

        !!! warning 
            Solo serán accesibles los archivos con nivel de acceso **Editar**.  
    
        !!!warning
            Con este scope, la aplicación solo puede gestionar archivos que se hayan creado desde Etendo o que se hayan abierto explícitamente con él.

    - **Google Drive – Nivel de acceso de sólo lectura**

        Concede a la aplicación permiso para **leer archivos existentes** en la cuenta del usuario (incluidos archivos no creados por Etendo).  
        No se permiten modificaciones: solo lectura de información o contenido del archivo.

        !!! warning 
            Solo serán accesibles los archivos con nivel de acceso **Sólo lectura**.

- Acepte la pantalla de consentimiento de Google.

    ![Consentimiento del proveedor](../../../../assets/developer-guide/etendo-classic/bundles/platform/etendo-rx/ProviderConsent.png)

#### Token creado en la solapa Información del token

Una vez completado el flujo, se generará un **token de acceso** y podrá verse en la solapa **Información del token**.

!!! info
    Los tokens obtenidos a través de **Etendo Middleware** son válidos durante **1 hour**.  
    Tras la caducidad, debe solicitarse un nuevo token para mantener el acceso a los servicios de terceros conectados.


![Nuevo token de Middleware](../../../../assets/developer-guide/etendo-classic/bundles/platform/etendo-rx/NewMiddlewareToken.png)

### Configurar manualmente un proveedor (Opcional)

Este método está pensado para usuarios que prefieren registrar un proveedor OAuth personalizado sin usar EtendoMiddleware. Proporciona control total sobre los parámetros de registro, autorización y gestión de tokens.

!!! warning
    La configuración manual del proveedor requiere que **EtendoRX** esté instalado y habilitado. RX es responsable de gestionar la conexión directa con proveedores OAuth externos. Para más información, visite [Etendo RX](../../../etendo-rx/getting-started.md)



![Ventana Proveedor OAuth](../../../../assets/developer-guide/etendo-classic/bundles/platform/etendo-rx/oAuthProviderWindow.png)

#### Cabecera

Campos a tener en cuenta:

- **Organización**: Define el alcance de organización para este proveedor.
- **URL de API oAuth**:  URL base del proveedor externo de la API OAuth. Se utiliza como endpoint principal para la comunicación con los servicios de autenticación y token del proveedor. (opcional)
- **Activo**: Casilla para habilitar o deshabilitar esta configuración de proveedor.

#### Sección: Registro

Esta sección define cómo se registra su aplicación en el proveedor OAuth. Incluye credenciales, el flujo de autorización, los scopes solicitados y las URLs esenciales para completar la autenticación.

Campos a tener en cuenta:

- **Costo:** Identificador técnico interno del proveedor.
- **ID para cliente:** `client_id` proporcionado por el proveedor OAuth.
- **Secreto de cliente:** `client_secret` proporcionado por el proveedor OAuth.
- **Scope:** Lista de permisos solicitados (estos scopes pueden encontrarse en la documentación del proveedor; p. ej., openid, profile, email, https://www.googleapis.com/auth/drive).
- **Nombre de cliente:** Nombre visible para el cliente.
- **Tipo de concesión de autorización:** Tipo de flujo (p. ej., authorization_code, client_credentials, password).
- **URI de redirección:** URL de redirección para recibir el código de autorización o token. Debe apuntar a la URL del servicio de autenticación de RX.
- **Método de desafío de código:** Método PKCE (S256 o plain).
- **Método de autenticación de cliente:** Método para enviar credenciales del cliente (p. ej., client_secret_post, client_secret_basic).
- **URI de token:** Endpoint para intercambiar el código de autorización por tokens (access_token y refresh_token opcional).

#### Sección: Proveedor

Esta sección define los endpoints del proveedor OAuth necesarios para que su aplicación se conecte y valide tokens correctamente.

- **URI de autorización:** Endpoint para iniciar el flujo de autorización.
- **URI de información de usuario:** Endpoint para obtener los datos del usuario usando el access_token.
- **Atributo de nombre de usuario:** Atributo utilizado para identificar al usuario (p. ej., email, sub).
- **Endpoint de autorización:** Endpoint utilizado para solicitar el token del proveedor a través del servicio de autenticación de RX.
- **URI del conjunto JWK:** URL donde el proveedor publica claves públicas para verificar JWT firmados.


### Solapa Información del token

Esta solapa almacena los tokens generados a través del ERP. Aunque por motivos de seguridad no se muestran los tokens completos, está disponible la siguiente información:

- **Usuario:** Usuario del ERP que generó el token.
- **Proveedor:** Proveedor OAuth desde el que se emitió el token.
- **Válido hasta:** Fecha y hora de caducidad del token.


### Botones

- **Actualizar configuración**
    
    Reinicia los servicios definidos en **Configuración RX**, útil si se realizaron cambios de configuración.

- **Obtener token:** 
    Inicia el flujo de autorización con el proveedor OAuth externo.

    Si todo está correctamente configurado, al hacer clic en **Obtener token** y aceptar el consentimiento se generará el token de acceso deseado. 
    
    Tras actualizar la cuadrícula en la solapa **Información del token**, aparecerá un nuevo registro.

!!! info
    Para revocar el acceso, simplemente elimine el registro del token. Una vez eliminado, la conexión con el servicio de terceros dejará de ser válida.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.