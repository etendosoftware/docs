---
tags:
    - How to
    - Configuración del correo electrónico
    - SMTP
    - Configuración General
    - Configuración multinivel
---

# Cómo configurar el correo electrónico

## Visión general

Etendo soporta una **configuración SMTP multinivel** que permite definir los ajustes de correo de forma independiente en tres niveles: **Entidad**, **Organización** y **Usuario**. Al enviar un documento por correo electrónico (p. ej. una factura o un pedido), el sistema resuelve qué configuración utilizar siguiendo una cascada de prioridad:

1. **Nivel de usuario** — si el usuario tiene una configuración de correo electrónico activa, tiene prioridad.
2. **Nivel de organización** — si no se encuentra una configuración a nivel de usuario, se utiliza la configuración de la organización.
3. **Nivel de entidad** — la configuración de respaldo, compartida por todas las organizaciones y usuarios de esa entidad.

Este diseño permite a una empresa establecer un servidor SMTP global a nivel de entidad, permitiendo que organizaciones o usuarios específicos lo sobrescriban con sus propias credenciales.

!!! info
    Cada nivel puede almacenar más de un registro de configuración SMTP. **Solo un registro puede marcarse como Valor por defecto por nivel**, y ese será el que se seleccione para ese nivel cuando se evalúe la cascada.

---

## Referencia de campos

En una instalación estándar de Etendo, el mismo conjunto de campos está disponible a nivel de **Entidad**, **Organización** y **Usuario**.

![Campos de configuración del correo electrónico](../../../assets/user-guide/etendo-classic/how-to-guides/how-to-configure-email/email-configuration-fields.png)

- **Servidor SMTP** nombre de host o dirección IP del servidor SMTP (p. ej. `smtp.gmail.com`).
- **Puerto Smtp** puerto utilizado por el servidor SMTP (p. ej. `465` para SSL, `587` para STARTTLS o `25` para conexiones sin cifrar).
- **Conexión de seguridad Smtp** modo de seguridad de transporte a utilizar al conectar con el servidor SMTP. Las opciones disponibles son **Ninguno**, **STARTTLS** y **SSL**. Debe coincidir con la configuración del servidor.
- **Timeout conexión Smtp** timeout de comunicación en segundos. Tras este tiempo, el proceso de envío de correo se detiene.
- **Autenticación SMTP** indica si el servidor SMTP requiere autenticación con usuario y contraseña antes de enviar correos. Si se habilita, **Cuenta del servidor SMTP** y **Contraseña del servidor SMTP** pasan a ser obligatorios.
- **Cuenta del servidor SMTP** usuario SMTP utilizado para autenticación. Obligatorio cuando **Autenticación SMTP** está habilitada.
- **Contraseña del servidor SMTP** contraseña de la cuenta SMTP. Obligatorio cuando **Autenticación SMTP** está habilitada.
- **Dirección de envío del servidor SMTP** dirección de correo que aparece en la cabecera `From` de los correos salientes. Debe completarse para enviar documentos por correo correctamente.
- **Nombre del remitente** nombre para mostrar opcional junto a la dirección del remitente.
- **Dirección de respuesta (Reply-To)** si se establece, las respuestas se dirigen a esta dirección en lugar de a la dirección del remitente.

---

## Nivel de entidad

:material-menu: `Aplicación` > `Configuración General` > `Entidad` > `Entidad` > pestaña **Configuración del correo electrónico**

La subpestaña **Configuración del correo electrónico** de la ventana Entidad define los ajustes SMTP globales utilizados como último recurso cuando no hay disponible ninguna configuración a nivel de organización o de usuario.

En una instalación estándar de Etendo, el mismo conjunto de campos está disponible a nivel de **Entidad**, **Organización** y **Usuario**. La siguiente tabla describe cada campo, si es obligatorio para configurar un SMTP funcional y su valor por defecto típico al crear un nuevo registro.

![Client Email Configuration](../../../assets/user-guide/etendo-classic/how-to-guides/how-to-configure-email/client-email-configuration.png)

| Campo | Descripción | Requerido | Valor por defecto |
|---|---|---|---|
| **Servidor SMTP** | Nombre de host o dirección IP del servidor SMTP (p. ej. `smtp.gmail.com`). | Sí | Vacío |
| **Puerto Smtp** | Puerto utilizado por el servidor SMTP (p. ej. `465` para SSL, `587` para STARTTLS o `25` para conexiones sin cifrar). | Sí | Vacío |
| **Conexión de seguridad Smtp** | Selecciona el modo de seguridad de transporte a utilizar al conectar con el servidor SMTP (**Ninguno**, **STARTTLS** o **SSL**). Debe coincidir con la configuración del servidor. | Sí (recomendado) | `Ninguno` |
| **Timeout conexión Smtp** | Timeout de comunicación con el servidor SMTP definido en segundos. Tras este tiempo, el proceso de envío de correo se detendrá. | No | Vacío (se usa el valor por defecto del sistema) |
| **Autenticación SMTP** | Indica si el servidor SMTP requiere autenticación con usuario y contraseña antes de enviar correos. Si se habilita, **Cuenta del servidor SMTP** y **Contraseña del servidor SMTP** pasan a ser obligatorios. | No | Desmarcado |
| **Cuenta del servidor SMTP** | Usuario SMTP (a menudo la dirección de correo) utilizado para autenticación. Obligatorio cuando la Autenticación SMTP está habilitada. | Condicional (si la autenticación está habilitada) | Vacío |
| **Contraseña del servidor SMTP** | Contraseña de la cuenta SMTP. Este valor debería almacenarse cifrado y es obligatorio cuando la Autenticación SMTP está habilitada. | Condicional (si la autenticación está habilitada) | Vacío |
| **Dirección de envío del servidor SMTP** | Dirección de correo que aparece en la cabecera `From` de los correos salientes. No es un campo obligatorio en base de datos, pero debe completarse para enviar documentos por correo correctamente. | No | Vacío |
| **Nombre del remitente** | Nombre para mostrar opcional junto a la dirección del remitente al enviar correos. | No | Vacío |
| **Dirección de respuesta (Reply-To)** | Si se establece, las respuestas al correo enviado se dirigirán a esta dirección en lugar de a la dirección del remitente. | No | Vacío |

---

## Nivel de organización

:material-menu: `Aplicación` > `Configuración General` > `Organización` > `Organización` > pestaña **Configuración del correo electrónico**

Cada organización puede definir sus propios ajustes SMTP en la subpestaña **Configuración del correo electrónico**. Cuando existe y está activa, esta configuración sobrescribe los ajustes a nivel de entidad para todos los correos enviados por usuarios de esa organización.

![Organization Email Configuration](../../../assets/user-guide/etendo-classic/how-to-guides/how-to-configure-email/organization-email-configuration.png)

Los campos disponibles a nivel de organización son los mismos que los descritos en la sección [Nivel de entidad](#nivel-de-entidad) anterior, con el mismo comportamiento de **Requerido** y **Valor por defecto**. Se pueden crear múltiples registros por organización; **solo uno puede marcarse como Valor por defecto**, y esa es la configuración que utiliza la cascada para esa organización.

---

## Nivel de usuario

:material-menu: `Aplicación` > `Configuración General` > `Seguridad` > `Usuario` > pestaña **Configuración del correo electrónico**

Un usuario individual puede tener sus propias credenciales SMTP configuradas en la subpestaña **Configuración del correo electrónico** de la ventana Usuario. Esto tiene la máxima prioridad en la cascada: si el usuario tiene una configuración activa válida, siempre se utilizará independientemente de los ajustes de organización o entidad.

![User Email Configuration](../../../assets/user-guide/etendo-classic/how-to-guides/how-to-configure-email/user-email-configuration.png)

Los campos disponibles a nivel de usuario son los mismos que los descritos en la sección [Nivel de entidad](#nivel-de-entidad) anterior, con el mismo comportamiento de **Requerido** y **Valor por defecto**.

!!! info
    La casilla **Valor por defecto** en una configuración a nivel de usuario determina qué registro se selecciona cuando un usuario tiene definido más de un registro de configuración de correo. Al igual que en otros niveles, **solo una configuración de correo de usuario puede marcarse como Valor por defecto al mismo tiempo**.

---

## Cómo funciona la cascada

Cuando se dispara un correo (p. ej. al enviar una factura), Etendo resuelve la configuración SMTP de la siguiente manera:

```
¿El usuario que envía tiene una configuración de correo por defecto utilizable?
  ├── SÍ  → usar configuración a nivel de usuario
  └── NO  → subir por el árbol de organización buscando una configuración utilizable
              ├── ENCONTRADA     → usar configuración a nivel de organización
              └── NO ENCONTRADA  → usar configuración a nivel de entidad (debe existir)
```

Una configuración se considera **utilizable** solo si tiene informados **Servidor SMTP** y **Dirección de envío del servidor SMTP**. Las configuraciones a las que les falte cualquiera de estos campos se omiten silenciosamente y la cascada continúa al siguiente nivel.

!!! warning
    La omisión solo aplica a **configuraciones incompletas** (falta el host SMTP o la dirección de envío). Si se encuentra una configuración completa pero las credenciales son incorrectas o el servidor no es accesible, la operación de envío **falla con un error** — no hace fallback al siguiente nivel.

---

## Probar la configuración

Una vez completados los campos SMTP, haz clic en el botón **Probar conexión SMTP** (arriba a la derecha de la ventana) para verificar que Etendo puede alcanzar el servidor con las credenciales proporcionadas.

!!! info
    El campo **Fecha de última prueba** se actualiza automáticamente después de cada prueba, y la casilla **Prueba satisfactoria** refleja si la última prueba fue correcta. Una prueba satisfactoria no garantiza que todos los correos se entreguen, pero confirma que la conexión y la autenticación funcionan correctamente.

---

## Ejemplo: configuración de Gmail

- Servidor SMTP: `smtp.gmail.com`
- Autenticación SMTP: `Sí`
- Cuenta del servidor SMTP: una cuenta válida de Gmail (p. ej. `user@gmail.com` o `user@tudominio` si usas Google Workspace)
- Contraseña del servidor SMTP: la contraseña o el token específico de aplicación de la cuenta
- Dirección de envío del servidor SMTP: la misma que la dirección de la cuenta
- Conexión de seguridad Smtp: `SSL`
- Puerto Smtp: `465`
- Timeout conexión Smtp: `600` (10 minutos)

!!! warning
    Gmail requiere usar una **contraseña de aplicación** (si 2FA está habilitado) u OAuth2. Google eliminó el soporte de "acceso de aplicaciones menos seguras" en 2022, por lo que la autenticación simple usuario/contraseña ya no está soportada.

## Ejemplo: servidor corporativo (STARTTLS)

Para la mayoría de servidores de correo corporativos o on-premise:

- Servidor SMTP: `mail.tudominio.com`
- Autenticación SMTP: `Sí`
- Cuenta del servidor SMTP: `user@tudominio.com`
- Contraseña del servidor SMTP: la contraseña de la cuenta
- Dirección de envío del servidor SMTP: `user@tudominio.com`
- Conexión de seguridad Smtp: `STARTTLS`
- Puerto Smtp: `587`
- Timeout conexión Smtp: `600`

Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="_blank"} por [Etendo](https://etendo.software){target="_blank"}.