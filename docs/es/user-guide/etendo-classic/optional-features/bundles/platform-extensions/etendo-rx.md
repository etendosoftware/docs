---
tags: 
    - Inicio de sesión SSO 
    - Google
    - Microsoft
    - Platform
    - Bundle
    - Etendo RX
---

# Etendo RX
:octicons-package-16: Paquete Java: `com.etendoerp.etendorx`

## Inicio de sesión SSO de Etendo

<iframe width="560" height="315" src="https://www.youtube.com/embed/S0bn2S7V07g?si=uK2sm_Nfn_W1RwxK" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Etendo le permite autenticarse utilizando estas cuentas de proveedores externos: **Google**, **Microsoft**, **LinkedIn**, **GitHub** y **Facebook**. El uso del protocolo de inicio de sesión único (Single Sign-On) es posible gracias a la integración con el servicio **EtendoAuth** o a una implementación personalizada de Auth0.

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Platform Extensions Bundle. Para ello, siga las instrucciones del marketplace: [_Platform Extensions Bundle_](https://marketplace.etendo.cloud/#/product-details?module=5AE4A287F2584210876230321FBEE614){target="\_blank"}. Para obtener más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Platform Extensions - Notas de la versión](../../../../../whats-new/release-notes/etendo-classic/bundles/platform-extensions/release-notes.md).

### Configuración inicial

Para utilizar esta funcionalidad, los desarrolladores deben seguir algunos pasos de configuración.

!!! info
    Para leer sobre esta configuración, visite la [Guía del desarrollador](../../../../../developer-guide/etendo-classic/bundles/platform/etendo-rx.md#etendo-sso-login).

### Iniciar sesión en Etendo con un proveedor externo

Al acceder a la pantalla de inicio de sesión de Etendo, verá botones de los **proveedores disponibles** para autenticarse.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/platform-extensions/etendo-rx/SSOLogin2.png)

!!! warning
    La **primera vez** que utilice uno de estos proveedores, verá un mensaje como:

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/platform-extensions/etendo-rx/SSOLogin1.png)

    Esto significa que todavía no ha vinculado su cuenta de Etendo con su cuenta del proveedor externo.

### Cómo vincular su cuenta de Etendo con una cuenta externa

1. Inicie sesión en Etendo como de costumbre con su **nombre de usuario y contraseña**.  
2. Vaya a su **perfil de usuario**, como se muestra a continuación.  
3. Verá una sección llamada **"Vincular usuario con"**.  
4. Haga clic en el proveedor que desea vincular.

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/platform-extensions/etendo-rx/SSOLogin3.png)

5. Autorice al proveedor externo a utilizar la información de la cuenta para iniciar sesión en Etendo 

!!!info
    Puede vincular varios proveedores al mismo usuario.

### Inicios de sesión futuros con una cuenta externa

La próxima vez que inicie sesión en Etendo:

- Haga clic en el **botón del proveedor** en la pantalla de inicio de sesión.
- Si ya está vinculado, iniciará sesión automáticamente **sin introducir su nombre de usuario y contraseña de Etendo**.

!!!info
    La autenticación se gestiona de forma segura mediante Auth0.

---
Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L](https://etendo.software){target="_blank"}.