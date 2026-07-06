---
tags:
    - How to
    - Configuración del correo electrónico
    - SMTP
    - Configuración General
    - Configuración multinivel
---

# Cómo configurar el correo electrónico { #how-to-configure-email }

## Visión general { #overview }

Etendo soporta una **configuración SMTP multinivel** que permite definir los ajustes de correo de forma independiente en tres niveles: **Entidad**, **Organización** y **Usuario**. Este diseño permite a una empresa establecer un servidor SMTP global a nivel de entidad, permitiendo que organizaciones o usuarios específicos lo sobrescriban con sus propias credenciales.

---

## Prerrequisitos { #prerequisites }

- Rol **Administrador de la Entidad** para configurar el correo a nivel de Entidad.
- Rol **Administrador de la Organización** para configurar el correo a nivel de Organización.
- Rol **System Administrator** para configurar el correo a nivel de Usuario.

---

## Cómo funciona la cascada { #how-the-cascade-works }

Cuando Etendo envía un correo (p. ej. una factura), resuelve la configuración SMTP utilizando el siguiente orden de prioridad:

1. **Nivel de usuario** — si el usuario que envía tiene una configuración de correo por defecto activa, se utiliza.
2. **Nivel de organización** — si no se encuentra una configuración a nivel de usuario, se utiliza la configuración por defecto de la organización.
3. **Nivel de entidad** — si no se encuentra una configuración a nivel de organización, se utiliza la configuración por defecto de la entidad como último recurso.

Una configuración se considera **utilizable** solo si tiene informados **Servidor SMTP** y **Dirección de envío del servidor SMTP**. Las configuraciones a las que les falte cualquiera de estos campos se omiten silenciosamente y la cascada continúa al siguiente nivel.

!!! warning
    La omisión solo aplica a **configuraciones incompletas** (falta el host SMTP o la dirección de envío). Si se encuentra una configuración completa pero las credenciales son incorrectas o el servidor no es accesible, la operación de envío **falla con un error** — no hace fallback al siguiente nivel.

---

## Referencia de campos { #field-reference }

El mismo conjunto de campos está disponible a nivel de **Entidad**, **Organización** y **Usuario**.

![Campos de configuración del correo electrónico](../../../assets/user-guide/etendo-classic/how-to-guides/how-to-configure-email/email-configuration-fields.png)

| Campo | Descripción |
| --- | --- |
| **Servidor SMTP** | Nombre de host o dirección IP del servidor SMTP (p. ej. `smtp.gmail.com`). |
| **Puerto Smtp** | Puerto utilizado por el servidor SMTP (p. ej. `465` para SSL, `587` para STARTTLS o `25` para conexiones sin cifrar). |
| **Conexión de seguridad Smtp** | Modo de seguridad de transporte. Las opciones disponibles son **Ninguno**, **STARTTLS** y **SSL**. Debe coincidir con la configuración del servidor. |
| **Timeout conexión Smtp** | Timeout de comunicación en segundos. Tras este tiempo, el proceso de envío de correo se detiene. |
| **Autenticación SMTP** | Indica si el servidor SMTP requiere autenticación. Si se habilita, **Cuenta del servidor SMTP** y **Contraseña del servidor SMTP** pasan a ser obligatorios. |
| **Cuenta del servidor SMTP** | Usuario SMTP utilizado para autenticación. Obligatorio cuando **Autenticación SMTP** está habilitada. |
| **Contraseña del servidor SMTP** | Contraseña de la cuenta SMTP. Obligatorio cuando **Autenticación SMTP** está habilitada. |
| **Dirección de envío del servidor SMTP** | Dirección de correo que aparece en la cabecera `From` de los correos salientes. Obligatorio para enviar documentos por correo correctamente. |
| **Nombre del remitente** | Nombre para mostrar opcional junto a la dirección del remitente. |
| **Dirección de respuesta (Reply-To)** | Si se establece, las respuestas se dirigen a esta dirección en lugar de a la dirección del remitente. |

---

## Ejemplos { #examples }

### Gmail { #gmail }

- **Servidor SMTP**: `smtp.gmail.com`
- **Autenticación SMTP**: `Sí`
- **Cuenta del servidor SMTP**: una cuenta válida de Gmail (p. ej. `user@gmail.com` o `user@tudominio` si se usa Google Workspace)
- **Contraseña del servidor SMTP**: la contraseña de aplicación o el token específico de la cuenta
- **Dirección de envío del servidor SMTP**: la misma que la dirección de la cuenta
- **Conexión de seguridad Smtp**: `SSL`
- **Puerto Smtp**: `465`
- **Timeout conexión Smtp**: `600` (10 minutos)

!!! warning
    Gmail requiere usar una **contraseña de aplicación** (si 2FA está habilitado) u OAuth2. Google eliminó el soporte de "acceso de aplicaciones menos seguras" en 2022, por lo que la autenticación simple usuario/contraseña ya no está soportada.

### Servidor corporativo (STARTTLS) { #corporate-server-starttls }

Para la mayoría de servidores de correo corporativos o on-premise:

- **Servidor SMTP**: `mail.tudominio.com`
- **Autenticación SMTP**: `Sí`
- **Cuenta del servidor SMTP**: `user@tudominio.com`
- **Contraseña del servidor SMTP**: la contraseña de la cuenta
- **Dirección de envío del servidor SMTP**: `user@tudominio.com`
- **Conexión de seguridad Smtp**: `STARTTLS`
- **Puerto Smtp**: `587`
- **Timeout conexión Smtp**: `600`

---

This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.
