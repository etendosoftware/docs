---
tags:
  - Cómo hacer
  - Swagger
  - Secure Web Services
  - Servicios web
---

# Cómo utilizar Secure Web Services

## Descripción general { #overview }

El módulo **Secure Web Services** proporciona autenticación mediante token JWT para las llamadas estándar a los web services de Etendo. Todos los servicios se exponen bajo el prefijo de ruta `/sws/`. La autenticación se realiza a través de `/sws/login`, y los servicios de datos como `obRest` están disponibles en `/sws/com.smf.securewebservices.obRest/`. Esto reemplaza el endpoint `/ws` basado en sesión por una alternativa segura basada en token (consulte [How to Create a New REST Webservice](how-to-create-a-new-rest-webservice.md) para más contexto sobre el framework `/ws`).

Restrinja el token a un rol, organización y almacén específicos en el momento del inicio de sesión. Una vez emitido, incluya el token en el encabezado `Authorization` de cada solicitud posterior.

!!! info
    Consulte la [referencia Swagger](https://demo.etendo.cloud/etendo/web/com.smf.securewebservices/doc/){target="_blank"} para conocer el flujo completo.

El módulo también incluye utilidades para desarrolladores y web services adicionales, como [`jsonDal`](../concepts/json-rest-web-services.md), para acceder al OB Data Access Layer con JSON.

## Configuración { #setup }

!!! warning
    Se requiere un nombre de dominio válido y un certificado SSL/TLS para utilizar **Secure Web Services**. Instale un certificado o contacte con su administrador para evitar errores en tiempo de ejecución al generar tokens en instancias de servidor.

!!! info
    De forma predeterminada, se utiliza el algoritmo de cifrado **ES256**. Para cambiar a un algoritmo heredado, cree una preferencia con la propiedad `Encryption Algorithm` y establezca su valor en `HS256`.

### Configuración de token { #token-configuration }

:material-menu: `Aplicación` > `Configuración General` > `Entidad` > `Entidad`

En la solapa **Configuración de Secure Web Services**, el **Administrador del Sistema** gestiona la clave SWS y configura la caducidad del token.

A partir de **Etendo 26.1**, la clave se genera automáticamente durante `./gradlew install` — no se requiere ninguna acción manual para instalaciones nuevas. Para versiones anteriores o para rotar la clave, utilice uno de los siguientes métodos:

1. **Desde la línea de comandos:**

    ```bash
    ./gradlew generate.sws.keys
    ```

2. **Desde la UI:** Abra la solapa **Configuración de Secure Web Services** y haga clic en **Generar Clave**.

!!! warning
    Ambos métodos sobreescriben la clave SWS existente. Todos los tokens firmados con la clave anterior quedan invalidados de forma inmediata.

El campo **Tiempo de expiración del token** controla durante cuánto tiempo los tokens permanecen válidos, expresado en minutos (`0` = sin expiración).

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-use-secure-web-services/SWS.png)

!!! warning "Recomendación de seguridad"
    Los tokens sin expiración representan un riesgo en producción: si un token es comprometido, permanece válido indefinidamente. Establezca un tiempo de expiración razonable y rote los tokens periódicamente.

## Autenticación { #authentication }

### Obtención de un token { #obtaining-a-token }

El endpoint `/sws/login` emite un token JWT restringido a un contexto específico de Etendo. Incluya los campos opcionales `role`, `organization` y `warehouse` en el cuerpo de la solicitud para restringir el token a un contexto concreto. Si se omiten, se asignan los valores predeterminados del servidor para cada campo según el usuario.

Los valores de `role`, `organization` y `warehouse` son IDs de registro internos (cadenas hexadecimales de 32 caracteres) o `"0"` para utilizar el valor predeterminado asignado por el servidor.

**Parámetros de consulta**

| Parámetro | Predeterminado | Descripción |
| :--- | :--- | :--- |
| `showRoles` | `true` | Incluye el array `roleList` en la respuesta |
| `showOrgs` | `true` | Incluye `orgList` dentro de cada entrada de rol |
| `showWarehouses` | `true` | Incluye `warehouseList` dentro de cada entrada de organización |

Establezca estos parámetros en `false` para reducir el payload de la respuesta cuando no se necesita descubrir el contexto.

**Parámetros del cuerpo de la solicitud**

| Campo | Requerido | Tipo | Descripción |
| :--- | :--- | :--- | :--- |
| `username` | Sí | string | Nombre de usuario de Etendo |
| `password` | Sí | string | Contraseña de Etendo |
| `role` | No | string | ID del rol al que se restringe el token |
| `organization` | No | string | ID de la organización a la que se restringe el token |
| `warehouse` | No | string | ID del almacén al que se restringe el token |

Reemplace `https://<your-host>` con la URL de su instancia de Etendo. Todas las rutas que aparecen a continuación son relativas a esa base.

**Ejemplo de solicitud — restringida a un rol y organización específicos**

```http
POST https://<your-host>/etendo/sws/login
Content-Type: application/json

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

El `roleList` en la respuesta lista todos los roles, organizaciones y almacenes disponibles para el usuario. Utilice estos IDs para solicitar un token con un ámbito más restringido en una llamada posterior.

### Uso del token { #using-the-token }

Incluya el token en el encabezado `Authorization` de cada llamada a la API:

```
Authorization: Bearer <token>
```

**Ejemplo — obtención de productos mediante `obRest`**

El segmento que sigue a `obRest/` es el nombre de la entidad tal como está definido en el Diccionario de Aplicación — coincide con el campo **Nombre** del registro `AD_Table` (por ejemplo, `Product`, `BusinessPartner`, `Order`). Reemplace `Product` por cualquier otro nombre de entidad para consultar ese conjunto de datos. `maxResults` es un parámetro de paginación estándar que limita el número de registros devueltos.

```http
GET https://<your-host>/etendo/sws/com.smf.securewebservices.obRest/Product?maxResults=10
Authorization: Bearer eyJhbGciOiJFUzI1NiJ9.<payload>.<signature>
```

### Renovación del token { #token-renewal }

Para renovar un token sin volver a introducir las credenciales, llame a `/sws/login` con el token existente en el encabezado `Authorization: Bearer` en lugar de `username` y `password`. No incluya `username` ni `password` en el cuerpo al renovar — el servidor ignora las credenciales cuando hay un encabezado `Authorization: Bearer` válido presente. El servidor emite un nuevo token con una fecha de expiración renovada, manteniendo el mismo contexto. Incluya `role`, `organization` o `warehouse` en el cuerpo para cambiar el ámbito del token en el momento de la renovación.

**Ejemplo de solicitud de renovación — mismo ámbito (cuerpo vacío)**

Envíe un cuerpo vacío para renovar el token y mantener sin cambios el ámbito de rol, organización y almacén existente.

```http
POST https://<your-host>/etendo/sws/login
Authorization: Bearer eyJhbGciOiJFUzI1NiJ9.<payload>.<signature>
Content-Type: application/json

{}
```

**Ejemplo de solicitud de renovación — cambio de ámbito en la renovación**

Incluya cualquier combinación de `role`, `organization` o `warehouse` en el cuerpo para cambiar el ámbito del token sin volver a introducir las credenciales. Omita cualquier campo que no desee modificar.

```http
POST https://<your-host>/etendo/sws/login
Authorization: Bearer eyJhbGciOiJFUzI1NiJ9.<payload>.<signature>
Content-Type: application/json

{
  "role": "B14F5D9A3EC741C2A9F860DE48A3B721",
  "organization": "2E60544D37534C0B89E765FE29BC0B43"
}
```

Ambas variantes devuelven la misma estructura de respuesta que el inicio de sesión inicial: una nueva cadena `token` y, cuando el parámetro de consulta `showRoles` es `true`, el array `roleList` completo.

## Swagger de Secure Web Services { #secure-web-services-swagger }

!!! info
    Para más información, visite [Swagger de Secure Web Services](https://demo.etendo.cloud/etendo/web/com.smf.securewebservices/doc/#/Login/post_sws_login){target="_blank"}.

---

This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.
