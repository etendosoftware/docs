---
title: Cómo conectar Etendo Copilot con Gmail mediante Pipedream
tags:
    - Etendo Copilot
    - Gmail
    - Pipedream
status: beta
---

# Cómo conectar Etendo Copilot con Gmail mediante Pipedream

## Visión general

<iframe width="560" height="315" src="https://www.youtube.com/embed/taAPYMPWpLM?si=_xZf1LQUnPAmQcHF" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Imagine a un responsable de departamento trabajando con Etendo Copilot que, de repente, necesita revisar su correo electrónico para consultar los últimos mensajes de clientes antes de tomar una decisión.  

En el pasado, esto requería cambiar de pestaña, buscar el hilo de Gmail y luego volver a Copilot — una interrupción típica del flujo de trabajo.  

Con la **integración con Gmail** mediante [Pipedream](https://pipedream.com){target="_blank"}, puede simplemente pedirle al agente:

- *“Enumere mis correos recientes de Gmail”*
- *“Resuma todos los correos no leídos y ordénelos por relevancia”*
- *“Busque los correos enviados a `client@example.com` y enumere sus últimas compras”*
- *“Envíe un correo a `client@example.com` con la lista de precios más reciente”*

El agente se conecta de forma segura a su cuenta de **Gmail** (con su autorización previa), recupera los mensajes y responde en línea en el chat. Todo ello sin salir de Copilot.

**¿Por qué es útil?**

- **Información centralizada**: Acceda a los datos del ERP y a los correos en el mismo lugar.  
- **Ahorro de tiempo**: No es necesario cambiar de aplicación ni copiar/pegar información.  
- **Más eficiente**: Su agente dispone de todo el contexto de sus correos y puede ayudarle a redactar correos, utilizando información de cualquier agente e incluso usando adjuntos.


## Cómo funciona

El flujo es simple pero potente:

1. [Pipedream](https://mcp.pipedream.com/){target="_blank"} gestiona la conexión segura con Gmail y expone la configuración de MCP.  
2. En **Etendo**, usted registra esa configuración como un servidor MCP.  
3. Por último, vincula el MCP a su agente de Copilot.  

A partir de ese momento, cualquier consulta relacionada con Gmail se redirige automáticamente al MCP de Pipedream, que obtiene los datos y devuelve la respuesta al chat.



## Requisitos previos

- Etendo y [Etendo Copilot](../installation.md) instalados.  
- Una cuenta de Google para conectar.  
- Acceso a Pipedream


!!! info 
	Para más información, visite [Cómo configurar servidores MCP en agentes de Etendo](./how-to-configure-mcp-servers-on-agents.md).  



## Conectar Gmail en Pipedream

1. Abra [Servidor MCP de Gmail | Pipedream](https://mcp.pipedream.com/app/gmail).  
2. Conecte su cuenta de Gmail y acepte la pantalla de consentimiento de Google.  
	![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-connect-etendo-copilot-with-gmail-via-pipedream/sign-in.png)
3. Seleccione la opción **VS Code** y copie la **configuración del servidor MCP** mostrada. 
	![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-connect-etendo-copilot-with-gmail-via-pipedream/mcp-server-config.png)

## Crear el servidor MCP en Etendo 
:material-menu: `Aplicación` > `Servicios` > `Copilot` > `Configuración de servidores MCP`

1. Inicie sesión en **Etendo** con el rol de **Administrador del sistema**.  
2. Vaya a la ventana `Configuración de servidores MCP`.  
3. Cree un nuevo registro con los siguientes valores:  

![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-connect-etendo-copilot-with-gmail-via-pipedream/create-mcp-server.png)

   - **Nombre**: p. ej., *Gmail de Pipedream*  
   - **Descripción**: (Opcional) p. ej., *Conexión a Gmail mediante MCP de Pipedream*
   - **Estructura JSON**: Pegue la configuración JSON copiada desde Pipedream. 
   - **Módulo**: (Opcional) Para exportar esta configuración a un módulo de desarrollo.


## Vincular el MCP al agente
:material-menu: `Aplicación` > `Servicios` > `Copilot` > `Agente`

1. Vaya a la ventana `Agente`.  
2. Abra el agente (o cree uno nuevo) al que desea dar acceso a la cuenta de Gmail y vaya a la pestaña **Servidores MCP**.  
3. Añada una nueva línea seleccionando el servidor MCP recién creado.  
4. **Guarde** los cambios y **sincronice el agente**.

![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-connect-etendo-copilot-with-gmail-via-pipedream/add-mcp-to-agent.png)


## Probar la integración con Gmail

-  Inicie una conversación con el agente y pregunte algo relacionado con Gmail, por ejemplo:  

	![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-connect-etendo-copilot-with-gmail-via-pipedream/mcp-gmail-use-example.png)

-  Envíe correos directamente desde el agente
    
    ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-connect-etendo-copilot-with-gmail-via-pipedream/send-email.png)

    ![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-connect-etendo-copilot-with-gmail-via-pipedream/example-email.png)


---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.