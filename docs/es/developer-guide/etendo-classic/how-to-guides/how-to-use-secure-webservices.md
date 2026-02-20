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

## Configuración inicial
:material-menu: `Aplicación` > `Configuración General` > `Entidad` > `Entidad`

Es necesario configurar la clave de cifrado y el tiempo de expiración de los tokens de autenticación en la ventana **Entidad** con el rol de *Administrador del sistema*.

Si el campo *Tiempo de expiración* es igual a `0`, los tokens no caducan.

Genere una clave aleatoria con el botón **Generar Clave**.

!!! Info 
    De forma predeterminada, se utiliza el **algoritmo de cifrado ES256**; es posible cambiarlo configurando una nueva preferencia con la propiedad `Encryption Algorithm` y estableciendo su valor en `HS256` para utilizar un algoritmo heredado.

!!! Warning
    Se requiere un nombre de dominio válido y un certificado `SSL/TLS` para utilizar **Servicios web seguros**. Instale un certificado o contacte con su administrador para evitar errores en tiempo de ejecución al generar tokens en instancias de servidor.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-use-secure-web-services/SWS.png)


## Swagger de Servicios web seguros

!!! info
    Para más información, visite [Swagger de Servicios web seguros](https://demo.etendo.cloud/etendo/web/com.smf.securewebservices/doc/#/Login/post_sws_login){target="_blank"}.


---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.