---
title: Guía de usuario - Primeros pasos - Etendo Mobile
tags:
    - Etendo Mobile
    - Aplicaciones móviles
    - Subaplicaciones dinámicas
    - Configuración
    - Integración de aplicaciones
---

![alt text](../../assets/user-guide/etendo-mobile/getting-started/cover-getting-started-mobile.png)

# Guía de usuario - Primeros pasos - Etendo Mobile

## Visión general

Etendo Mobile es una **aplicación móvil** que permite a los usuarios acceder rápidamente a diferentes servidores de Etendo Classic y utilizar las subaplicaciones instaladas en cada instancia. Puede probar la aplicación inmediatamente usando el modo de demostración o realizar una configuración manual completa para conectarse a sus propios servidores y subaplicaciones.


## Inicio rápido - Prueba de demostración 

**Lista de verificación**
 
- [x] Descargue la aplicación Etendo.
- [x] Utilice el botón **Prueba de demostración** para acceder a las subaplicaciones oficiales.

---

1. ### Descargue la aplicación Etendo 

    Etendo Mobile está disponible tanto en Play Store como en App Store:

    === ":simple-homeassistantcommunitystore: Play store"

        La aplicación está disponible en Play Store. Descárguela aquí: [_Descargue la aplicación aquí._](https://play.google.com/store/apps/details?id=com.smf.mobile.etendo_app_loader){target=_blank}

        ![](../../assets/user-guide/etendo-mobile/getting-started/EtendoPlayStore.png)
        <a href="https://play.google.com/store/apps/details?id=com.smf.mobile.etendo_app_loader" target="_blank"><img src="/assets/user-guide/etendo-mobile/getting-started/etendo-playstore.png" alt="playstore.png"></a>

    === ":simple-appstore: App Store "

        La aplicación está disponible en App Store. Descárguela aquí: [_Descargue la aplicación aquí._](https://apps.apple.com/us/app/etendo/id6451114033){target=_blank}

        <a href="https://apps.apple.com/us/app/etendo/id6451114033" target="_blank"><img src="/assets/user-guide/etendo-mobile/getting-started/etendo-appstore.png" alt="appstore.png"></a>

2. ### Modo Prueba de demostración

    Una vez instalada la aplicación, ábrala y pulse el botón **Prueba de demostración** para entrar en la aplicación sin necesidad de credenciales. Esto le permite explorar y probar inmediatamente las subaplicaciones oficiales instaladas en el servidor [https://demo.etendo.cloud](https://demo.etendo.cloud).

    !!! info
        El modo de demostración proporciona acceso a subaplicaciones preconfiguradas con fines de prueba.

    ![](../../assets/user-guide/etendo-mobile/getting-started/demo-try.png)


## Configuración del entorno de la entidad

**Lista de verificación**

- [x] Etendo Classic: Instalar las subaplicaciones requeridas (desarrollador).
- [x] Etendo Classic: Configurar las subaplicaciones dinámicas para el rol correspondiente.
- [x] Etendo Mobile: Configurar la URL del servidor.
- [x] Etendo Mobile: Iniciar sesión y usar las aplicaciones.
---
1. ### Instalar subaplicaciones en Etendo Classic

    !!! warning
        Algunos pasos de configuración inicial y la instalación de bundles que contienen las subaplicaciones disponibles o el desarrollo de nuevas subaplicaciones deben ser realizados por un desarrollador o administrador del sistema. Para más información, consulte la [Guía del desarrollador - Primeros pasos - Etendo Mobile](../../developer-guide/etendo-mobile/getting-started.md)

    **Subaplicaciones disponibles para instalar**

    A continuación, puede encontrar las subaplicaciones distribuidas por Etendo, disponibles para su instalación, y su documentación.

    - [Subaplicación Etendo Classic](./bundles/mobile-extensions/etendo-classic-subapp.md)
        
        Proporciona a los usuarios una forma eficiente de acceder a la información clave de las ventanas del sistema, garantizando acceso en modo lectura, en función de su rol. 
    
    - [Subaplicación Gestor de documentos](./bundles/mobile-extensions/overview.md#documents-manager-subapp) 
    
        Es una implementación de ejemplo de subaplicación capaz de recibir archivos externos y renderizarlos dentro de Etendo Mobile.

    - [Subaplicación Etendo Copilot](../etendo-copilot/bundles/overview.md#etendo-copilot-subapp)
    
        Diseñada para integrarse sin problemas con las funcionalidades existentes de Etendo Copilot, ampliando su funcionalidad a dispositivos móviles y tabletas.

    - [Subaplicación Advanced Warehouse Management](../etendo-classic/optional-features/bundles/warehouse-extensions/advanced-warehouse-management.md)
    
        Amplía las capacidades estándar de almacén de Etendo al habilitar una gestión de inventario eficiente, automatizada y orientada a movilidad. Permite a los usuarios gestionar existencias, realizar ajustes, ejecutar picking y packing, y garantizar sincronización en tiempo real y trazabilidad mediante escaneo de códigos de barras, todo desde Etendo Mobile.


    !!!info
        Para configurar subaplicaciones dinámicas, debe instalar el bundle correspondiente: 
        
        - [Mobile Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=55A7EF64F7FA43449B249DA7F8E14589){target="\_blank"}
        - [Copilot Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}
        - [Warehouse Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=EFDA39668E2E4DF2824FFF0A905E6A95){target="\_blank"}

2. ### Token de acceso de la entidad
    :material-menu: `Aplicación` > `Configuración General` > `Entidad` > `Entidad`

    Debe configurarse un token de cifrado de un solo uso para la autenticación. Este token es necesario para que **Etendo Mobile** inicie una sesión.

    1. Acceda a Etendo Classic como `System Administrator`.
    2. Navegue a la pestaña `Entidad` > `Secure Web Service Configuration`.
    3. Haga clic en el botón **Generar Clave** para crear un token. El tiempo de caducidad se mide en minutos; si se establece en 0, el token no caduca.
    ![alt text](../../assets/developer-guide/etendo-mobile/getting-started/token.png)

    !!! info
        Este token no requiere ninguna acción; solo necesita generarse para que el proceso de autenticación funcione correctamente.

3. ### Configurar roles y subaplicaciones dinámicas
    :material-menu: `Aplicación` > `Configuración General` > `Seguridad` > `Rol`

    1. Abra la ventana **Rol**.
    2. Seleccione el **Rol** al que se le dará acceso a las subaplicaciones.
    3. Asegúrese de que la casilla `Is Web Service Enabled` esté seleccionada.
    4. En la pestaña **Aplicaciones dinámicas**, cree una entrada de configuración para cada subaplicación para asignar el acceso en función del rol.
    5. Configure los siguientes campos:
        - **Aplicación:** seleccione la subaplicación en la lista desplegable.
        - **Versión:** asigne la versión que se utilizará.
        - **Activo:** marque como activo para habilitar el acceso.

        !!! info
            Recuerde que las subaplicaciones deben estar instaladas previamente.

        ![alt text](../../assets/user-guide/etendo-mobile/getting-started/getting-started-mobile-3.png)


4. ### Configurar la URL del servidor en Etendo Mobile

    1. Abra la aplicación Etendo.
    2. Haga clic en el icono de engranaje en la pantalla de bienvenida para abrir Ajustes.
    3. Haga clic en **Añadir nuevo enlace**, introduzca la URL de su servidor de Etendo Classic y haga clic en **Añadir nuevo enlace** de nuevo para guardar.

    ![alt text](../../assets/user-guide/etendo-mobile/getting-started/url-setup.png)

    !!!info
        Puede añadir varias URL de servidor, modificarlas o eliminarlas según sea necesario.

5. ### Iniciar sesión en la aplicación

    ![alt text](../../assets/user-guide/etendo-mobile/getting-started/getting-started-mobile-2.jpg){ width="250" align="left" }

    1. Introduzca sus credenciales de usuario asignadas por su administrador del sistema.
    2. El usuario iniciará sesión con su **Valor por defecto** de Rol, Organización, Entidad y Almacén.

    !!!note
        El usuario permanece con la sesión iniciada hasta que elija cerrar sesión.
    
    <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> 



## Funcionalidades de Etendo Mobile

### Compartir archivos

![](../../assets/user-guide/etendo-mobile/getting-started/share-files.gif){ width="250" align="right" }

Etendo Mobile admite la **recepción de archivos** desde aplicaciones externas para que puedan ser utilizados por subaplicaciones.

- La [Subaplicación Gestor de documentos](./bundles/mobile-extensions/overview.md#documents-manager-subapp) puede recibir y mostrar archivos externos dentro de Etendo Mobile.
- La [Subaplicación Etendo Copilot](../etendo-copilot/bundles/overview.md#etendo-copilot-subapp) puede recibir cualquier archivo externo y procesarlo mediante agentes en un único paso sencillo.

!!!warning
    La funcionalidad de compartir archivos permite que los archivos se abran mediante un selector en cualquier subaplicación compatible.

!!!info
    Para más detalles técnicos, consulte la guía [Crear nueva subaplicación](../../developer-guide/etendo-mobile/tutorials/create-new-subapplication.md).


---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.