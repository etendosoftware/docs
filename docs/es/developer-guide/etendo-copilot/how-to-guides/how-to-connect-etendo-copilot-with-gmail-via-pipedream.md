---
title: Cómo conectar Etendo Copilot con Gmail mediante Pipedream
tags:
    - Etendo Copilot
    - Gmail
    - Pipedream
status: beta
---

# Cómo conectar Etendo Copilot con Gmail mediante Pipedream { #how-to-connect-etendo-copilot-with-gmail-via-pipedream }

## Descripción general { #overview }

<iframe width="560" height="315" src="https://www.youtube.com/embed/taAPYMPWpLM?si=_xZf1LQUnPAmQcHF" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Imagine a un responsable de departamento trabajando con Etendo Copilot que, de repente, necesita revisar su correo electrónico para consultar los últimos mensajes de clientes antes de tomar una decisión.  

En el pasado, esto requería cambiar de solapa, buscar el hilo de Gmail y luego volver a Copilot — una interrupción típica del flujo de trabajo.  

Con la **integración con Gmail** mediante [Pipedream](https://pipedream.com){target="_blank"}, puede simplemente pedirle al agente:

- *"Enumere mis correos recientes de Gmail"*
- *"Resuma todos los correos no leídos y ordénelos por relevancia"*
- *"Busque los correos enviados a `client@example.com` y enumere sus últimas compras"*
- *"Envíe un correo a `client@example.com` con la lista de precios más reciente"*

El agente se conecta de forma segura a su cuenta de **Gmail** (con su autorización previa), recupera los mensajes y responde en línea en el chat. Todo ello sin salir de Copilot.

Esta guía le muestra tres pasos: conectar su cuenta de Gmail en Pipedream, registrar esa conexión en Etendo y vincularla a su agente.

**¿Por qué es útil?**

- **Información centralizada**: Acceda a los datos del ERP y a los correos en el mismo lugar.  
- **Ahorro de tiempo**: No es necesario cambiar de aplicación ni copiar/pegar información.  
- **Más eficiente**: Su agente dispone de todo el contexto de sus correos y puede ayudarle a redactar correos, utilizando información de cualquier agente e incluso usando adjuntos.


## Cómo funciona { #how-it-works }

El flujo es simple pero potente:

1. [Pipedream](https://mcp.pipedream.com/){target="_blank"} gestiona la conexión segura con Gmail y expone la configuración de MCP (Model Context Protocol) — una forma estándar para que los asistentes de IA se conecten de forma segura a servicios externos como Gmail.  
2. En **Etendo**, usted registra esa configuración como un servidor MCP.  
3. Por último, vincula el MCP a su agente de Copilot.  

A partir de ese momento, cualquier consulta relacionada con Gmail se redirige automáticamente al MCP de Pipedream, que obtiene los datos y devuelve la respuesta al chat.



## Requisitos previos { #prerequisites }

- Etendo y [Etendo Copilot](../installation.md) instalados.  
- Una cuenta de Google para conectar.  
- Una cuenta gratuita en [Pipedream](https://pipedream.com){target="_blank"}.


!!! info 
	Para más información, visite [Cómo configurar servidores MCP en agentes de Etendo](./how-to-configure-mcp-servers-on-agents.md).  



## Conectar Gmail en Pipedream { #connect-gmail-in-pipedream }

1. Abra [Gmail MCP Server | Pipedream](https://mcp.pipedream.com/app/gmail).  
2. Conecte su cuenta de Gmail y acepte la pantalla de consentimiento de Google.  
	![Pantalla de conexión de cuenta de Gmail en Pipedream](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-connect-etendo-copilot-with-gmail-via-pipedream/sign-in.png)
3. En el panel de configuración, seleccione la opción **VS Code** en el desplegable (este formato es necesario para que Etendo pueda leer la configuración) y, a continuación, haga clic en **Copy** para copiar el texto de **MCP Server Config** que aparece.
	![Panel MCP Server Config en Pipedream](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-connect-etendo-copilot-with-gmail-via-pipedream/mcp-server-config.png)

## Crear el servidor MCP en Etendo { #create-the-mcp-server-in-etendo }
:material-menu: `Aplicación` > `Servicios` > `Copilot` > `Configuración de servidores MCP`

1. Inicie sesión en **Etendo** con el rol de **Administrador del Sistema**.  
2. Navegue a la ventana `Configuración de servidores MCP`.  
3. Cree un nuevo registro con los siguientes valores:  

![Formulario de nuevo registro de servidor MCP en Etendo](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-connect-etendo-copilot-with-gmail-via-pipedream/create-mcp-server.png)

   - **Nombre**: p. ej., *Pipedream Gmail*  
   - **Descripción**: (Opcional) p. ej., *Conexión a Gmail mediante MCP de Pipedream*
   - **JSON Structure**: Pegue el texto de código copiado desde Pipedream en el paso anterior. Esta es la configuración que Etendo utiliza para conectarse a su cuenta de Gmail.
   - **Módulo**: Déjelo en blanco a menos que su equipo técnico le haya indicado que lo complete.


## Vincular el MCP al agente { #link-the-mcp-to-the-agent }
:material-menu: `Aplicación` > `Servicios` > `Copilot` > `Agente`

1. Navegue a la ventana `Agente`.  
2. Abra el agente al que desea otorgar acceso a Gmail (o cree uno nuevo) y vaya a la solapa **Servidores MCP**.  
3. Añada una nueva línea seleccionando el servidor MCP recién creado.  
4. Haga clic en **Guardar** para registrar los cambios y, a continuación, haga clic en **Sync Agent** — esto aplica la nueva conexión con Gmail al agente para que pueda comenzar a utilizarla de inmediato.

![Solapa Servidores MCP en el registro del agente en Etendo](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-connect-etendo-copilot-with-gmail-via-pipedream/add-mcp-to-agent.png)


## Probar la integración con Gmail { #test-the-gmail-integration }

1. Inicie una conversación con el agente y pregunte algo relacionado con Gmail, por ejemplo:

   ![Chat del agente mostrando un ejemplo de consulta de Gmail](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-connect-etendo-copilot-with-gmail-via-pipedream/mcp-gmail-use-example.png)

2. Envíe correos directamente desde el agente:

   ![Ejemplo de envío de correo desde el agente](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-connect-etendo-copilot-with-gmail-via-pipedream/send-email.png)

   ![Ejemplo de correo enviado resultante](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-connect-etendo-copilot-with-gmail-via-pipedream/example-email.png)


---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.
