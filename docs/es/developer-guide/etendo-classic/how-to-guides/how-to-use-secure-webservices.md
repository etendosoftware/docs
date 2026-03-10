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

Además de la implementación de autenticación, el módulo incluye utilidades para desarrolladores y servicios web útiles, como jsonDal (para acceder a la **capa de acceso a datos de OB** con json).

## Configuración

!!! Info
    De forma predeterminada, se utiliza el **algoritmo de cifrado ES256**; es posible cambiarlo configurando una nueva preferencia con la propiedad `Encryption Algorithm` y estableciendo su valor en `HS256`.

!!! Warning
    Se requiere un nombre de dominio válido y un certificado `SSL/TLS` para utilizar **Servicios web seguros**. Instale un certificado o contacte con su administrador para evitar errores en tiempo de ejecución al generar tokens en instancias de servidor.

### Configuración automática (26Q1+)

A partir de **26Q1**, la clave de Servicios Web Seguros se **genera automáticamente** al ejecutar la tarea `./gradlew install`. No se requiere configuración manual para instalaciones nuevas.

- La clave generada utiliza el algoritmo **ES256** por defecto.
- El tiempo de expiración del token se establece en **0** (sin expiración) por defecto.
- El tiempo de expiración puede modificarse posteriormente desde la ventana Entidad (valor expresado en **minutos**, donde `0` significa sin expiración).

!!! warning "Recomendación de seguridad"
    Si bien la expiración por defecto es `0` (sin expiración) para facilitar la configuración inicial, el equipo de Etendo recomienda establecer un tiempo de expiración razonable en entornos productivos. Los tokens sin expiración representan un riesgo de seguridad: si un token es comprometido, permanece válido indefinidamente. Se recomienda definir una política de expiración y rotar los tokens periódicamente.

### Instalaciones existentes

Para instancias instaladas antes de 26Q1, la clave SWS puede generarse o rotarse de dos formas:

1. **Desde la UI:** Navegue a :material-menu: `Aplicación` > `Configuración General` > `Entidad` > `Entidad`, abra la pestaña **Secure Web Service Configuration** y utilice el botón **Generar Clave**.

2. **Desde la línea de comandos:** Ejecute la siguiente tarea Gradle:

    ```bash
    ./gradlew generate.sws.keys
    ```

!!! warning
    Ambos métodos **sobreescribirán la clave SWS existente**. Todos los tokens firmados con la clave anterior se invalidarán inmediatamente.

### Configuración manual (Opcional)

:material-menu: `Aplicación` > `Configuración General` > `Entidad` > `Entidad`

También es posible configurar o rotar manualmente la clave de cifrado y el tiempo de expiración de los tokens de autenticación en la ventana Entidad con el rol de *Administrador del sistema*.

El tiempo de expiración se expresa en **minutos** (establezca `0` para que no expire).

Utilice el botón **Generar Clave** para generar una nueva clave aleatoria.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-use-secure-web-services/SWS.png)


## Swagger de Servicios web seguros

!!! info
    Para más información, visite [Swagger de Servicios web seguros](https://demo.etendo.cloud/etendo/web/com.smf.securewebservices/doc/#/Login/post_sws_login){target="_blank"}.


---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.