---
tags:
  - Cómo hacer
  - Swagger
  - Secure Web Services
  - Servicios web
---

# Cómo utilizar Secure Web Services

## Descripción general

Este módulo permite llamar a cualquier **web service de Etendo** estándar del mismo modo que al endpoint `/ws`, pero utilizando autenticación mediante token. El módulo Secure Web Services expone sus endpoints bajo el prefijo de ruta `/sws/` — por ejemplo, el endpoint de inicio de sesión es `/sws/login`.

Este método de autenticación también permite definir el contexto de las llamadas eligiendo el rol y/o la organización al solicitar un token. La renovación y las actualizaciones de caducidad del token se gestionan a través del endpoint `/sws/login`.

!!!info
    Consulte la [referencia Swagger](https://demo.etendo.cloud/etendo/web/com.smf.securewebservices/doc/){target="_blank"} para conocer el flujo completo.

Además de la implementación de autenticación, el módulo incluye utilidades para desarrolladores y web services útiles, como `jsonDal` (para acceder al OB Data Access Layer con json).

## Configuración

!!! Warning
    Se requiere un nombre de dominio válido y un certificado `SSL/TLS` para utilizar **Secure Web Services**. Instale un certificado o contacte con su administrador para evitar errores en tiempo de ejecución al generar tokens en instancias de servidor.

!!! Info
    De forma predeterminada, se utiliza el **algoritmo de cifrado ES256**. Para cambiar a un algoritmo heredado, cree una preferencia con la propiedad `Encryption Algorithm` y establezca su valor en `HS256`.

### Configuración de token

:material-menu: `Aplicación` > `Configuración General` > `Entidad` > `Entidad`

En la solapa **Configuración de Secure Web Services**, el *Administrador del sistema* puede gestionar la clave SWS y configurar la caducidad del token.

A partir de **Etendo 26.1**, la clave se genera automáticamente durante `./gradlew install` — no se requiere ninguna acción manual para instalaciones nuevas. Para versiones anteriores o para rotar la clave, utilice uno de los siguientes métodos:

1. **Desde la línea de comandos:**

    ```bash
    ./gradlew generate.sws.keys
    ```

2. **Desde la UI:** Abra la solapa **Configuración de Secure Web Services** y haga clic en **Generar Clave**.

!!! warning
    Ambos métodos **sobreescribirán la clave SWS existente**. Todos los tokens firmados con la clave anterior se invalidarán inmediatamente.

El campo **Tiempo de expiración** controla durante cuánto tiempo los tokens permanecen válidos, expresado en **minutos** (`0` = sin expiración).

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-use-secure-web-services/SWS.png)

!!! warning "Recomendación de seguridad"
    Los tokens sin expiración representan un riesgo en producción: si un token es comprometido, permanece válido indefinidamente. Establezca un tiempo de expiración razonable y rote los tokens periódicamente.

### Solicitud de token con Rol, Organización y Almacén

El endpoint `/sws/login` emite un token JWT vinculado a un contexto específico de Etendo. Para vincular el token a un rol y/o organización concretos, incluya los campos opcionales `role` y `organization` en el cuerpo de la solicitud junto con las credenciales requeridas. El campo `warehouse` también es opcional y sigue el mismo patrón.

Los valores de `role`, `organization` y `warehouse` son IDs de registro internos (cadenas hexadecimales de 32 caracteres) o `"0"` para utilizar el valor predeterminado asignado por el servidor.

**Parámetros del cuerpo de la solicitud**

| Campo | Requerido | Tipo | Descripción |
|---|---|---|---|
| `username` | Sí | string | Nombre de usuario de Etendo |
| `password` | Sí | string | Contraseña de Etendo |
| `role` | No | string | ID del rol al que se vincula el token |
| `organization` | No | string | ID de la organización a la que se vincula el token |
| `warehouse` | No | string | ID del almacén al que se vincula el token |

**Ejemplo de solicitud — vinculada a un rol y organización específicos**

```json
{
  "username": "admin",
  "password": "admin",
  "role": "A97CFB945DC84D5BB0B7EC0CE8571F87",
  "organization": "2E60544D37534C0B89E765FE29BC0B43"
}
```

**Ejemplo de respuesta**

```json
{
  "status": "success",
  "token": "eyJhbGciOiJFUzI1NiJ9.<payload>.<signature>",
  "roleList": [
    {
      "id": "A97CFB945DC84D5BB0B7EC0CE8571F87",
      "name": "Sales Representative",
      "orgList": [
        {
          "id": "2E60544D37534C0B89E765FE29BC0B43",
          "name": "F&B US, Inc.",
          "warehouseList": [
            {
              "id": "B2D40D8A5D644DD89E329DC297309055",
              "name": "USA East Coast"
            }
          ]
        }
      ]
    }
  ]
}
```

!!! note
    Cuando se omiten `role` y `organization`, el servidor asigna al contexto del token el rol por defecto y la organización por defecto del usuario. Utilice los campos explícitos para anular este comportamiento y restringir el token a un ámbito más limitado.

## Swagger de Secure Web Services

!!! info
    Para más información, visite [Swagger de Secure Web Services](https://demo.etendo.cloud/etendo/web/com.smf.securewebservices/doc/#/Login/post_sws_login){target="_blank"}.


---

This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.