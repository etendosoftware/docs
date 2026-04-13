---
tags: 
    - Seguridad avanzada
    - Contraseña
    - Bloqueo de usuario
    - Bloqueo automático de contraseña
    - Historial de contraseñas
---

# Etendo Advanced Security
:octicons-package-16: Javapackage: `com.etendoerp.advanced.security` 

## Visión general
Esta sección describe el módulo Etendo Advanced Security incluido en el bundle Platform Extensions.

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Platform Extensions Bundle. Para ello, siga las instrucciones del marketplace: [_Platform Extensions Bundle_](https://marketplace.etendo.cloud/#/product-details?module=5AE4A287F2584210876230321FBEE614){target="\_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Platform Extensions - Notas de la versión](../../../../../whats-new/release-notes/etendo-classic/bundles/platform-extensions/release-notes.md).

El módulo **Etendo Advanced Security** permite al usuario personalizar varias funcionalidades de seguridad como las siguientes:

- Seguridad de contraseñas
- Historial de contraseñas
- Bloqueo de usuario
- Verificación de múltiples sesiones
- Cambio de contraseña tras el inicio de sesión
- Tiempo de caducidad (bloqueo automático de contraseña)

!!! info
    Para más información sobre la configuración del módulo, visite la [Guía del desarrollador](../../../../../developer-guide/etendo-classic/bundles/platform/overview.md#etendo-advanced-security).

## Seguridad de contraseñas

Esta funcionalidad se ejecuta cuando se cambia la contraseña, ya sea porque el usuario necesita cambiarla o porque el sistema lo requiere. El proceso puede realizarse desde el campo **Cambiar contraseña** en la barra de navegación y/o desde la ventana **Usuario**.

Desde el proceso **Cambiar contraseña**, Etendo solicitará la contraseña actual y la nueva para realizar el cambio. Tras hacer clic en **Aplicar,** se verificarán una serie de comprobaciones para finalmente ejecutar los cambios correspondientes.

![](../../../../../assets/drive/sQNqx26cwCGfPld7D47SHw_QnmdO5-zHlJ41yN28V3yKv95xq6PMGqHobkKuh8rQa11RNvI6bMpkWMk9k0H6P_n8DilZ0NfQ56yjBZYaP85WyQWXC7shoMt7zU6nxO-3-JMUXzwRJ2ASii0YDJpUN6s.png)

!!! info
    La contraseña debe tener una longitud mínima de 8 caracteres y su estructura debe contener al menos tres de los siguientes tipos de caracteres: letras, letras mayúsculas, letras minúsculas, números y símbolos.

Si la nueva contraseña no cumple las condiciones mencionadas anteriormente, aparece un popup con un mensaje de error indicando las condiciones que deben cumplirse.

![](../../../../../assets/drive/shTQdtbDJq_FrCieCra0q6YLlv5akL6vFAS2Xr9sogzi6IMddd-qi9HJDwKKhxY0fCqpUfcFa-l0agc03ypnwtH_eFpDR6SLWNPVi4edc--fKnZsuzeFwnNC_ITWGd5q07zMCr1ImePmG5cOLmSH_rQ.png)

Este proceso también puede ejecutarse desde la ventana **Usuario** aplicando los mismos requisitos de contraseña mencionados anteriormente.

![](../../../../../assets/drive/JNG3VeVWDWewBfz_iijE7kUBTZBV-8DUBQAWaiEa1uyxhOxYZxmbC_bavwTW85z0LJ_S9ibzN1XVz8pGIZQZz675KBO8H8vaO1LJ8BXxO3Sl5AOqOvOV2hgDKjMObk6CWCpmB8ChETBvqkEICBJ0SI4.png)

**Etendo Advanced Security** verifica los cambios y, si la nueva contraseña no cumple las condiciones requeridas, Etendo muestra un mensaje de error en el momento de registrar los cambios.

![](../../../../../assets/drive/jUjckeZt5RPHdHYZcD0xN9BXUkKoNLOYPrkLIkG4pyqPJBYvFFtkWWKBzgy3pZ2Qr1M-kGZPzd2YXiNxOuOlNdVj26PDen8jOxw-44zBzZsX1G3eNTiIzIHidjO8eiDmrY-uU-XhkUxG2RiUbahRbbQ.png)

### Historial de contraseñas

Al cambiar la contraseña, una de las condiciones que deben cumplirse es que la nueva contraseña no puede ser la misma que una utilizada previamente. Etendo crea registros de las contraseñas usadas anteriormente, por lo que, si el usuario introduce una ya utilizada, el sistema informa con un **mensaje de error.**

Esta funcionalidad de seguridad puede configurarse solo con **permisos de Administrador del Sistema**. Para ello, vaya a la ventana **Información del Sistema**, dentro del campo de grupo **Seguridad de contraseñas**, y marque el campo llamado **Habilitar historial de contraseñas**, según sus preferencias.

![](../../../../../assets/drive/s0Xj63FWSlAuip3ZzJB0OWyHiF-cM8zs8EruyfZEM7qA3Pt1hvcNZkRDHWzSb9t3GkzqrqbRwIuP5hghTfyal4441tIbtMQrNyu1CPQmhLOwJkM1EcQ85tEz5TDRbOQazN15k5hzX-b6NyleAak3u1s.png)

Cuando la configuración de la funcionalidad **Seguridad de contraseñas** está activa y el usuario **cambia la contraseña** por una utilizada previamente, Etendo mostrará un **mensaje de error** explicando el fallo al guardar la contraseña.

![](../../../../../assets/drive/x4qql4v3biKPnkWDrD86UUS4mJkw0HuajIK5AmXZKT0OKjP5LdGjzhtd6L8BkkPsR-a9duOtg9uK6OHWjJbig-vSHrltxOd2TfjU5-_lwfH74sKnuekNk4A-heIRIniDxvEb5F45Ms0SxKbRQdy-ztg.png)

El siguiente ejemplo muestra el mismo mensaje de error al cambiar la contraseña desde el proceso **Cambiar contraseña**.

![](../../../../../assets/drive/1VTtHPNlLr0N3fvL1vVQ7FO2lzWcQti5I.png)

!!! info
    Etendo también permite introducir la misma contraseña un número indefinido de veces. En caso de que el usuario desee mantener la misma contraseña, simplemente mantenga el campo **Habilitar historial de contraseñas** de la ventana Información del Sistema **sin marcar**. 

## Bloqueo de usuario

Otra funcionalidad de este módulo es el **bloqueo** del usuario tras N **intentos de inicio de sesión fallidos**. Al introducir una contraseña incorrecta, Etendo muestra un mensaje de error indicando el número de intentos restantes.

En este ejemplo, el sistema muestra que queda un intento.

![](../../../../../assets/drive/C-pmD7RKuMzM6e1fSFHSwLWAusC2cL1U9gKlvxWxe7VRa64uuLwaQ7dm4Cmi_Z773XQsfFzfSPrdfMGDNdnNgKPuWobU4xTlxFtOirr34LPiLMT9bI3LONLsmydtloKyd48GYi_1hRnovcHduVsDwGE.png)

Incluso si en el siguiente intento el usuario no puede iniciar sesión correctamente, Etendo deja otro mensaje indicando que el usuario ha sido bloqueado.

![](../../../../../assets/drive/e_vXv3RF7iceBBddpDNUMwewnLYcr5W7LzjhyzrUMPnGe6oT9v9TeXiGc-8MLQpF_Xv1POEZdvMmIRL5bwfai6-hfaEirW4IKlsrBVzcLndzbtRTYeO0_fwou-fTO00rxDtw2lJJi7LY5LoW7vWPEb8.png)

!!! info
    Por defecto, Etendo configura cinco intentos para introducir la contraseña correcta. 

Para configurar el número de intentos de inicio de sesión fallidos, es necesario crear una preferencia desde la ventana **Preferencias**. En el campo **Costo**, añada el número deseado de intentos de inicio de sesión y, además, seleccione la preferencia **Número máximo de intentos de contraseña** en el campo **Propiedad**.

![](../../../../../assets/drive/5nXDi_OVP9kEESFxQsu1DJywuIEhpJfGl7UvWYPV4UO1CkEhcs2aXMQQIt51lJrww8TfMAUWMfjky2zRtpqhzzdsYygdDt8VhJAe0HNHAWpFbbTbX7c0khUaD9Dn9so89idLPpfmVAqR9bVfS4h4IAU.png)

!!! warning
    Es importante tener en cuenta que, una vez introducida la nueva contraseña, si el usuario vuelve a introducir una contraseña incorrecta, el sistema bloqueará automáticamente el inicio de sesión en el primer intento. 

## Verificación de múltiples sesiones  

Otra innovación funcional que facilita este módulo es la capacidad de permitir o bloquear tener múltiples sesiones abiertas desde otro navegador.

Desde la ventana **Usuario**, dentro del campo **Más información**, es posible configurar la casilla que permite tener varias sesiones activas al mismo tiempo. La casilla se llama **Permitir múltiples sesiones**.

![](../../../../../assets/drive/vcMT58GIgiB2QsZcR-bt5xyajWgf9isk7sxrFJuwkUW27BKnmLIjcb2YZIEJUB-YE-scGv_n3rZ1jTwKGKwLumx4KAIjSp0SsN1jK4saZNChsH8q2JRn5RS3Q6TkXVdVLa1r7C5wXTPmrfVkJyChjRA.png)

En caso de que el usuario solo quiera permitir una sesión activa, desmarque la casilla **Permitir múltiples sesiones** de la ventana **Usuario** y, **solo con permisos de Administrador del Sistema**, marque el campo **Habilitar verificación de sesión única** en el campo **Seguridad de sesión** de la ventana **Información del Sistema**.

![](../../../../../assets/drive/Prfolo_qyMafrXpr9dUe_ASCkalv-LjArCWEcMCPSWWi2IzyypsQytDTUlSeMgq_mSbgCYKtebK9aawUzMNotE2V25Lg-RrJ2f21l6m75dS4Z11d76gidgZfFrxy1BQgjVl7EvJg2xQISvt1efahvCc.png)

De este modo, al intentar iniciar sesión, el sistema verifica que ya existe una sesión activa e informa al usuario.

![](../../../../../assets/drive/IkC8pMQVLKRCkr3SI1oYDJsaSirmOHxS31Z5ZmwhCzOnMnwXW88ZFHcyTCnp0Vpm9BxY_RJbpWIdrQG0g5DhURD1RSzW2nexd9hGTeCxTNWhaAWaopvCG-r7JieCNHkLjpCb7HW3v3JXDjofFCHEyAU.png)

!!! info
    Por defecto, Etendo con este módulo instalado solo permite tener una sesión activa. 

## Cambio de contraseña tras el inicio de sesión

Tras iniciar sesión por **primera vez** con un usuario, Etendo solicita **cambiar la contraseña**. Al intentar iniciar sesión, el sistema indica que la contraseña ha caducado y que el usuario necesita cambiarla por una nueva para poder iniciar sesión.

![](../../../../../assets/drive/aJIN1JP1Oau9HSzi_O2NF-rcQBAdE58v59GVg5NoLiQvgTobqai4mOU07aw0D786KJfL0EBJ_rcaQ86-vf8FmZo3gKZnhLaE_yE3Ynzk46CQkhg0abwcMPLKPw2OjUlvFa75h5zkhSW4i97OviTl8mo.png)

Una vez realizado el cambio, el usuario es redirigido a la interfaz principal de la aplicación.

## Tiempo de caducidad (bloqueo automático de contraseña)

Como parte de la gestión de seguridad, Etendo también permite la gestión de los días del **tiempo de caducidad de la contraseña**.

Desde la ventana **Preferencias**, es posible ajustar el periodo de tiempo requerido para que el usuario esté obligado a cambiar la contraseña. Hágalo añadiendo la cantidad de días deseada para la caducidad de la contraseña en el campo **Costo**.

![](../../../../../assets/drive/4o5-tsn6u1mWXedVD-rp5GQNpc6RZ6cAroo-BrZc6xPUevOI0COBerM1NnEmySSSMLMBicOBI1Gidh-4D3QkOMPvJI72977qKSYFHtFJ0UtZnChiIcSYi0Nz3Uu_9H5k39FZ7ozJjeyUbxifnWGamz0.png)

!!! info
    Tenga en cuenta que, por defecto, Etendo configura 30 días para el tiempo de caducidad de la contraseña. 

Tras el número de días establecido para la caducidad de la contraseña, al intentar iniciar sesión se muestra un mensaje explicando la necesidad de ser redirigido al **inicio de sesión para cambiar la contraseña**, es decir, el usuario queda marcado como **contraseña caducada**.

Además, Etendo notifica al usuario con un mensaje anunciando la cantidad de **días restantes** para la caducidad de la contraseña. En este ejemplo, al usuario le quedan dos días.

![](../../../../../assets/drive/0g12hmyWCTy2ecyVLmptMQSLE6ocCBLGSJLJlYa3EqwCNE-NyYSxy-aO9jg88OWefWDsRso8RDce3Zas0q5Q29fUdcrtSeZ-nA13uwNokmr2vnlKM4HabnGCzy5r3stbAmsCoEgMhzno5T6LLr4tyYM.png)

!!! info
    Por defecto, el sistema activa este mensaje cuando quedan **siete días** para cambiar la contraseña.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.