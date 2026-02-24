---
tags:
  - Copilot
  - Inicialización de cliente
  - Cliente
  - Configuración
---

# Herramienta de configuración inicial del cliente

:octicons-package-16: Paquete Java: `com.etendoerp.copilot.devassistant`

## Visión general

La **ClientInitTool** ayuda a inicializar un nuevo cliente en el sistema Etendo. Recopila de forma interactiva toda la información requerida, invoca la función de backend para aprovisionar el cliente y su administrador, y valida que la creación se haya realizado correctamente.

!!!info
    Para poder incluir esta funcionalidad, debe estar instalado el bundle Copilot Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. Para más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Copilot Extensions - Notas de la versión](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

## Funcionalidad

Esta herramienta automatiza el proceso de **aprovisionamiento de clientes** en Etendo mediante:

- **Recepción de parámetros**
    
    - Acepta un objeto de entrada con:
        
        - `client_name` (string)
        - `client_username` (string)
        - `password` (string)
        - `confirm_password` (string)
        - `currency` (string)
        - `sysadmin_user` (string or null)
        - `sysadmin_password` (string or null)
        - `remote_host` (string or null)

- **Creación del cliente**

    - Valida que las contraseñas coincidan.  
    - Llama a la función `ClientInitTool` para crear el entorno del cliente y la cuenta de administrador, utilizando el host y las credenciales inferidos si no se proporcionan.

- **Devolución del resultado**

    - Devuelve una respuesta JSON indicando éxito o fallo.  
    - En caso de éxito: incluye un mensaje de confirmación, el ID del nuevo cliente y el nombre de usuario del administrador.

## Ejemplo de uso

### Aprovisionamiento de un nuevo cliente

**Entrada**
```json
{
  "client_name": "ACME Corp",
  "client_username": "acmeadmin",
  "password": "Secret123!",
  "confirm_password": "Secret123!",
  "currency": "USD"
}
```

**Salida**
```json title="Output Json"
{
  "status": "success",
  "client_id": "12345",
  "admin_username": "acmeadmin",
  "message": "Client 'ACME Corp' initialized successfully."
}
```

!!!note
    Tras la creación correcta, indique al usuario que inicie sesión con las credenciales del administrador recién creado, configure el acceso al asistente para el cliente y continúe con la configuración de la organización.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.