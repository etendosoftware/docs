---
title: Cómo crear un agente de hojas de cálculo y tareas
tags:
    - Cómo
    - Etendo Copilot
    - Agente
    - Hoja de cálculo
    - Tareas
    - Google Drive
---


# Cómo crear un agente de hojas de cálculo y tareas

## Visión general

Basado en la guía oficial sobre [Cómo crear un agente](./how-to-create-an-agent.md), este documento proporciona una guía detallada para crear un agente que pueda aprovechar Google Drive, gestionar Google Sheets e incorporar la funcionalidad de creación de tareas de Etendo.

1.  ### Definición del prompt del agente

	El primer paso es establecer el propósito principal del agente y sus reglas operativas. Esto se logra mediante un prompt claro y conciso que sirve como su conjunto principal de instrucciones.

	**Prompt:**

	```title="Prompt"
	You are an agent that can interact with Google Sheets and Google Drive.
	For this, you can load an OAuth token and receive an "alias" for the token. 
	This alias is for security purposes, so you can use it in the future without exposing the token directly.
	```

	Este prompt define la identidad del agente y su método seguro para gestionar las credenciales de autenticación.

2. ### Autenticación

	Estas herramientas requieren un token de Google OAuth 2.0 para funcionar. El agente utiliza este token para autenticar sus solicitudes a las API de Google. Para obtener un token, siga los pasos de la guía [Proveedor OAuth](../../etendo-classic/bundles/platform/etendo-rx.md#oauth-provider).

	#### Ejemplos de uso

	Una vez configuradas las herramientas, puede interactuar con el agente usando lenguaje natural. El agente interpretará su solicitud y utilizará la herramienta adecuada.

	1. **Ejemplo: creación de un archivo**

		Puede indicar al agente que cree un nuevo Google Sheet.

		* **Su prompt:**
			```
			Create a new Google Sheet named 'Q3 Sales Report'.
			```
		* **Respuesta del agente:**
			```
			The Google Sheet 'Q3 Sales Report' has been created successfully. You can access it here: [link](https://docs.google.com/spreadsheets/d/your-new-sheet-id)
			```

	2. **Ejemplo: escritura de datos en un archivo**

		Después de crear el archivo, puede pedir al agente que añada datos.

		* **Su prompt:**
			```
			In the 'Q3 Sales Report' sheet, add a header row with the following columns: 'ProductID', 'Region', 'UnitsSold', 'SaleDate'.
			```
		* **Respuesta del agente:**
			```
			The header row has been added to the 'Q3 Sales Report' sheet.
			```

3. ###  Ampliación de la funcionalidad con tareas

	Puede mejorar aún más el agente habilitando la creación de tareas dentro de Etendo. Añada el siguiente texto al prompt del agente definido en el primer paso:

	```title="Prompt"
	Additionally, you can create tasks in Etendo. The Task Creation Tool requires a csv to create the tasks, so if you want to use a Google Sheet, you must download it as a csv first.

	The ID of the agent that can create products (Product Creator):"767849A7D3B442EB923A46CCDA41223C"
	```

	Este fragmento proporciona al agente un contexto crucial:

	1.  Especifica el **flujo de trabajo** para crear tareas a partir de un Google Sheet (es decir, primero debe convertirse a CSV).
	2.  Proporciona el **ID de otro agente**, que puede utilizarse como contexto o para la comunicación entre agentes.

	Para interactuar con Tareas, el agente necesita las herramientas adecuadas. Debe definirlas en la pestaña **Habilidad/Herramienta**.
	
	!!! info 
		Para más información, visite el enlace: [Documentación de tareas asíncronas](../../etendo-classic/bundles/platform/task.md)

4. ### Finalización de la configuración del agente

	Una vez que el prompt del agente esté completamente definido y todas las herramientas necesarias estén asociadas, el paso final es vincularlas.

	Navegue a la ventana **Agente** en Etendo y, en la pestaña **Habilidades/Herramientas**, asigne:
	
	- [GoogleDriveTool](../available-tools/google-drive-tool.md): Gestiona archivos y carpetas en Google Drive.
	- [Herramienta de Google Spreadsheets](../available-tools/google-spreadsheet-tool.md): Lee y escribe datos en Google Sheets.
	- [Herramienta de creación de tareas](../available-tools/task-creator-tool.md): Automatiza la creación de tareas en función del contenido de un archivo. Admite los formatos **ZIP**, **CSV**, **XLS** y **XLSX**.
		
	Al completar este paso, activa todas las capacidades del agente. Ahora puede orquestar flujos de trabajo sin problemas entre **Google Drive** y **Etendo**, como leer datos de un **Google Sheet** y usar esos datos para **crear tareas** automáticamente.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.