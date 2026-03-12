---
tags:
    - Copilot
    - Consultas SQL
    - Acceso a base de datos
    - Automatización de consultas
    - Funcionalidades del agente
---

# Experto SQL

:octicons-package-16: Paquete Java: `com.etendoerp.copilot.toolpack`

## Visión general

Este agente está diseñado para ayudar a los usuarios a leer información de la base de datos. Permite a los usuarios hacer preguntas en lenguaje natural y obtener la consulta SQL que recupera la información que necesitan. Utilice un webhook para obtener la información necesaria para generar la consulta SQL. El usuario puede hacer preguntas sobre la base de datos, y el agente determinará si debe devolver una consulta SQL o ejecutar la consulta y devolver el resultado obtenido.

## Componentes

El agente Experto SQL se compone de los siguientes componentes:

- [Herramienta de llamada a API](../available-tools/openapi-tool.md)

- **DBQueryExec - Webhook**: este webhook permite al agente ejecutar consultas SQL en la base de datos. El agente llama al webhook para ejecutar la consulta en la base de datos y devuelve el resultado al agente. Esta es una forma segura de ejecutar consultas SQL en la base de datos, ya que Etendo gestiona la seguridad de la conexión a la base de datos y la ejecución de la consulta.

## Configuración del agente 

1. Este módulo está incluido en el Copilot Extensions Bundle

    !!! info
        Para poder incluir este agente, debe estar instalado el Copilot Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Copilot Extensions - Notas de la versión](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

2. Compruebe la variable `ETENDO_HOST` necesaria en el archivo `gradle.properties`.
    
    ```groovy title="gradle.properties"
    ETENDO_HOST=http://localhost:8080/etendo
    ```

    !!! warning
        Sustituya http://localhost:8080/etendo por la URL real del sistema Etendo.

3. Se ha creado un nuevo agente llamado **Experto SQL** en la ventana `Application` > `Service` > `Copilot` > `Agent`.

4. Ejecute el proceso **Sincronizar agente**, iniciando sesión con el rol de **Administrador del sistema**.

5. Reinicie la imagen de Docker usando las tareas `./gradlew resources.up`.

6. Configure el acceso al agente desde la ventana [Acceso al agente](../../etendo-copilot/setup-and-usage.md#agent-access-window).

7. Puede usar el agente **Experto SQL** como **Administrador del sistema**

    !!!warning 
        En caso de utilizar este agente con otros roles: 
        
        1. Debe verificarse que el rol tiene habilitada la ejecución de webhooks: 
            ![](../../../assets/user-guide/etendo-copilot/bundles/sql-expert/webhook-service-enabled.png)
        
        2. Debe concederse acceso al rol correspondiente en la ventana [WebHooks](../../../developer-guide/etendo-classic/bundles/platform/etendo-webhooks.md#assign-allowed-roles), en la pestaña **Rol**, para el WebHook **DBQueryExec**. Este webhook se añade automáticamente cuando se instala el módulo.
            ![](../../../assets/user-guide/etendo-copilot/bundles/sql-expert/webhook-setup.png)

## Ejemplos

### Ejemplos de preguntas para la recuperación de información

1. 
    <figure markdown>
    ![Herramienta DBQueryGenerator](../../../assets/user-guide/etendo-copilot/bundles/sql-expert/sql-assistant.png){align=right width=300}
    <br><br>
    **¿Cuál es el importe de la última factura de venta de la organización F&B España - Región Sur?**
    </figure>

2.  

    <figure markdown>
    ![Herramienta DBQueryGenerator](../../../assets/user-guide/etendo-copilot/bundles/sql-expert/sql-assistant-2.png){align=left width=300}
    <br><br>
    **¿Puede decirme cuál es la factura con el importe registrado más alto?**
    </figure>
 
3.
    <figure markdown>
    ![Herramienta DBQueryGenerator](../../../assets/user-guide/etendo-copilot/bundles/sql-expert/sql-assistant-3.png){align=right width=300}
    <br><br>
    **¿Puede ejecutar la suma de los pedidos en el último mes de 2016?**
    </figure>

### Ejemplos de generación de consultas SQL

1. 
    <figure markdown>
    ![Herramienta DBQueryGenerator](../../../assets/user-guide/etendo-copilot/bundles/sql-expert/sql-assistant-3.png){ align=right width=300 }
    <br>
    **¿Puede ejecutar la suma de los pedidos en el último mes?**
    </figure>

2.  <figure markdown>
    ![Herramienta DBQueryGenerator](../../../assets/user-guide/etendo-copilot/bundles/sql-expert/sql-assistant-4.png){ align=right }
    <br>
    **¿Consulta para conocer el nombre de los 5 mejores clientes de enero de 2011?**
    </figure>
    
3.  <figure markdown>
    ![Herramienta DBQueryGenerator](../../../assets/user-guide/etendo-copilot/bundles/sql-expert/sql-assistant-5.png){ align=right }
    <br>
    **¿Consulta para obtener cuál es la factura con el importe registrado más alto?**
    </figure> 

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.