---
tags:
  - Cómo hacer
  - Swagger
  - Servicios web seguros
  - Servicios web seguros
  - Servicios web
---

# Cómo utilizar Servicios web seguros

## Visión general

Este módulo permite llamar a cualquier **servicio web de Etendo** estándar del mismo modo que al endpoint `/ws`, pero utilizando autenticación mediante token.

Este método de autenticación también permite definir el contexto de las llamadas eligiendo el rol y/o la organización al solicitar un token. También es posible renovar un token para actualizar la fecha de caducidad o cambiar el rol/organización.

Además de la implementación de autenticación, el módulo incluye utilidades para desarrolladores y servicios web útiles, como jsonDal (para acceder a la capa de acceso a datos de OB con json).

## Configuración

!!! Warning
    Se requiere un nombre de dominio válido y un certificado `SSL/TLS` para utilizar **Servicios web seguros**. Instale un certificado o contacte con su administrador para evitar errores en tiempo de ejecución al generar tokens en instancias de servidor.

!!! Info
    De forma predeterminada, se utiliza el **algoritmo de cifrado ES256**. Para cambiar a un algoritmo heredado, cree una preferencia con la propiedad `Encryption Algorithm` y establezca su valor en `HS256`.

### Configuración de token

:material-menu: `Aplicación` > `Configuración General` > `Entidad` > `Entidad`

En la pestaña **Configuración de Secure Web Services**, el *Administrador del sistema* puede gestionar la clave SWS y configurar la caducidad del token.

A partir de **Etendo 26.1**, la clave se genera automáticamente durante `./gradlew install` — no se requiere ninguna acción manual para instalaciones nuevas. Para versiones anteriores o para rotar la clave, utilice uno de los siguientes métodos:

1. **Desde la línea de comandos:**

    ```bash
    ./gradlew generate.sws.keys
    ```

2. **Desde la UI:** Abra la pestaña **Configuración de Secure Web Services** y haga clic en **Generar Clave**.

!!! warning
    Ambos métodos **sobreescribirán la clave SWS existente**. Todos los tokens firmados con la clave anterior se invalidarán inmediatamente.

El campo **Intervalo en Minutos** controla durante cuánto tiempo los tokens permanecen válidos, expresado en **minutos** (`0` = sin expiración).

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-use-secure-web-services/SWS.png)

!!! warning "Recomendación de seguridad"
    Los tokens sin expiración representan un riesgo en producción: si un token es comprometido, permanece válido indefinidamente. Establezca un tiempo de expiración razonable y rote los tokens periódicamente.


## Swagger de Servicios web seguros

!!! info
    Para más información, visite [Swagger de Servicios web seguros](https://demo.etendo.cloud/etendo/web/com.smf.securewebservices/doc/#/Login/post_sws_login){target="_blank"}.


---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.
---