---
tags:
  - Copilot
  - Inicialización de la organización
  - Organización
  - Configuración
---

# Herramienta de configuración inicial de la organización

:octicons-package-16: Paquete Java: `com.etendoerp.copilot.devassistant`

## Visión general

La **OrgInitTool** ayuda a inicializar o crear una nueva organización en el sistema Etendo. Recopila de forma interactiva toda la información requerida, invoca la función de backend para aprovisionar la organización y su administrador, y valida que la creación se haya realizado correctamente.

!!!info
    Para poder incluir esta funcionalidad, debe estar instalado el bundle Copilot Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. Para más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Copilot Extensions - Notas de la versión](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

## Funcionalidad

Esta herramienta automatiza el proceso de **aprovisionamiento de la organización** en Etendo mediante:

- **Recepción de parámetros**
    - Acepta un objeto de entrada con:
        - `org_name` (string)
        - `org_username` (string)
        - `password` (string)
        - `confirm_password` (string)
        - `client_admin_user` (string o null)
        - `client_admin_password` (string o null)
        - `remote_host` (string o null)

- **Creación de la organización**
    - Valida que las contraseñas coincidan.  
    - Llama a la función `OrgInitTool` para:
        - Crear el entorno de la organización.
        - Configurar la cuenta de administrador.

- **Devolución del resultado**
    - Devuelve una respuesta JSON indicando éxito o fallo.  
    - En caso de éxito: incluye un mensaje de confirmación, el ID de la nueva organización y el nombre de usuario del administrador.

## Ejemplo de uso

### Creación de una nueva organización

**Entrada**
```json
{
  "org_name": "EventsCo",
  "org_username": "eventsadmin",
  "password": "Passw0rd!",
  "confirm_password": "Passw0rd!",
  "client_admin_user": "acmeadmin"
}
```

**Salida**
```json title="Output Json"
{
  "status": "success",
  "org_id": "67890",
  "admin_username": "eventsadmin",
  "message": "Organization 'EventsCo' initialized successfully."
}
```

!!!note
    Tras la creación correcta, indique al usuario que inicie sesión con las credenciales del administrador para continuar con la configuración de la organización.

---
Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L](https://etendo.software){target="_blank"}.