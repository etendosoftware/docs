---
tags:
    - Cómo hacer
    - Crear herramienta
    - Herramienta de Copilot
    - Dependencias de Python
---

# Cómo crear herramientas de Copilot

## Visión general

Esta guía proporciona instrucciones paso a paso para ayudarle a crear herramientas personalizadas para **Etendo Copilot**. Aprenderá a:

- Definir la estructura de módulo requerida.
- Especificar las entradas de la herramienta y las dependencias.
- Registrar y probar sus herramientas en **Etendo Classic**.
- Integrar sus herramientas con **Etendo Classic** utilizando la **API de Webhooks de Eventos**.

Esto permite una interacción fluida entre sus herramientas basadas en Python y la plataforma Etendo.


## Etendo Copilot
La infraestructura de **Etendo Copilot** le permite crear herramientas que amplían la funcionalidad de los agentes. Estas herramientas se desarrollan en Python y se ejecutan en el contenedor Docker donde opera Copilot.
En esta guía, aprenderá a crear una nueva herramienta de Copilot en un módulo dedicado. Sin embargo, también es posible añadir herramientas a un módulo existente. Cada módulo puede contener una o varias herramientas.

!!! note "Etendo Copilot se basa en Langchain"
    Las librerías de Langchain están disponibles por defecto en Copilot. Puede utilizarlas en sus herramientas. Consulte la [documentación de Langchain](https://python.langchain.com/){target="_blank"} para más información.

### Requisitos

El bundle **Copilot Extensions** debe estar instalado en **Etendo Classic**. Si no está instalado, siga la [Guía de instalación de Etendo Copilot](../../../developer-guide/etendo-copilot/installation.md){target="_blank"} para configurarlo.


### Crear una nueva herramienta
En este ejemplo, creará una herramienta que realiza un **ping** a un host especificado. La herramienta se llamará `PingTool` y estará ubicada en el paquete `com.etendoerp.copilot.pingtool`.

1. Crear un módulo de Etendo Classic: todas las herramientas de Copilot deben ubicarse dentro de un módulo de **Etendo Classic**. Para crear un nuevo módulo, siga los pasos de [Cómo crear un módulo](../../etendo-classic/how-to-guides/how-to-create-a-module.md).
    
    !!! warning
        Para que la herramienta funcione correctamente y sea reconocida por la infraestructura de Copilot, el módulo debe incluir el archivo `build.gradle`. Este archivo se crea cuando el módulo se prepara para ser publicado. Consulte [Cómo publicar módulos en el repositorio de GitHub](../../../developer-guide/etendo-classic/how-to-guides/how-to-publish-modules-to-github-repository.md)

    
    La estructura del módulo será la siguiente:

    ``` 
    modules
    └── com.etendoerp.copilot.pingtool
        ├── src-db 
        │   └── database
        │       └── sourcedata
        │           ├── AD_MODULE.xml
        │           ├── AD_MODULE_DBPREFIX.xml
        │           ├── AD_MODULE_DEPENDENCY.xml
        │           └── ETCOP_TOOL.xml
        ├── tools 
        │   └── PingTool.py
        ├── build.gradle
        └── tools_deps.toml
    ```

    *src-db*: contiene la estructura de base de datos del módulo. Esta carpeta se crea automáticamente al crear y exportar el módulo desde **Etendo Classic**.
   
    *tools*: contiene las herramientas del módulo. Un módulo puede contener una o más herramientas.
   
    *build.gradle*: contiene las configuraciones del módulo.

    *tools_deps.toml*: define las dependencias de Python para las herramientas del módulo. Estas dependencias se instalan automáticamente dentro del contenedor Docker de Copilot cuando se carga la herramienta.

    

2. Crear la herramienta en Python. Es necesario usar un `Dict` como entrada. Para ello, defina una clase usando `pydantic` para especificar la estructura de la entrada. 
    Para `PingTool`, cree una clase llamada `PingToolInput` dentro del archivo `PingTool.py`. Aquí tiene un ejemplo:
    
    !!! warning 
        El `SearchKey` de la herramienta debe coincidir con el nombre de la clase que extiende la clase `ToolWrapper`.

    ```python title="PingTool.py"

    import os
    from typing import Type, Dict

    from copilot.core.tool_input import ToolInput, ToolField

    from copilot.core.tool_wrapper import ToolWrapper  # Import the ToolWrapper class from the copilot.core.tool_wrapper module. This class is the one that must be extended to create a new tool.


    class PingToolInput(ToolInput):
        host: str = ToolField(
            title="Host",
            description='''The host to ping.''',
        )
        message_to_print: str = ToolField(
            default="default message!",  # Default value of the input, if there is no default value, the input is mandatory.
            title="Message to print",
            description=" Custom message to print before the ping result.",
        )


    class PingTool(ToolWrapper):
        name: str = 'PingTool'  # Name of the tool
        # Description of the tool.
        # This description tells Copilot what the tool does and based on this description it will decide if this tool will solve the user's request.
        description: str = (
            '''This tool receives a hostname and returns the ping result.''')
        args_schema: Type[ToolInput] = PingToolInput  # The args_schema attribute must be a Pydantic model that defines the inputs of the tool.
        
        #return_direct = True  # If return_direct is True, the tool will return the result directly, without execute any other tool. If return_direct is not defined, the tool output can be used as input of another tool. This is only available for tools in the Langchain agent. In the OpenAI agent, the return_direct attribute is taken into account, and the tool output can be used as input of another tool.

        def run(self, input_params: Dict, *args,
                **kwargs):  # The run method is the one that will be executed when the tool is executed.
            import requests  # Import the necessary libraries to execute the tool.
            # It is recommended to import the libraries inside the run method to avoid conflicts with other tools.
            host = input_params.get('host')  # Get the host input from the input_params dictionary.
            # Get the message_to_print input from the input_params dictionary
            # or from the args attribute that contains the default values of the inputs.
            message_to_print = input_params.get('message_to_print') or self.args.get('message_to_print').get('default')
            print('MESSAGE:' + message_to_print)
            response = requests.get(host)
            return {"status_code": response.status_code}  # The run method must return a dictionary with the outputs of the tool.
    ```
    
    !!! note "Variables de entorno"
        Copilot lee automáticamente el archivo `gradle.properties` de **Etendo Classic** y las expone como variables de entorno (puntos reemplazados por guiones bajos). Por ejemplo:

        - `COPILOT_PORT` → `COPILOT_PORT`
        - `bbdd.sid` → `bbdd_sid`

        Puede acceder a estas variables de entorno en sus herramientas.
        
    
3. Crear el archivo `tools_deps.toml` en la carpeta raíz del módulo. Este archivo define dependencias en formato TOML:
    
    ``` toml
    [ToolName]
    dependency_name = "dependency_version"
    dependency_name = "dependency_version"
    ```
    Para nuestro ejemplo, el contenido del archivo será el siguiente:

    ``` toml
    [PingTool]
    requests = "*"
    ```

    La versión puede especificarse con los siguientes operadores:
    
    ``` toml
    [PingTool]
    requests = "*" # Installing latest version
    requests = "==2.26.0" # Installing a specific version
    requests = ">=2.26.0" # Greater than or equal to a certain version
    requests = "<=2.26.0" # Less than or equal to a certain version
    requests = ">2.26.0" # Greater than a certain version
    requests = "<2.26.0" # Less than a certain version
    requests = ">=2.26.0,<=2.26.1" # Using version ranges
    requests = "~=2.26.0" # Tilde operator (~) for installing compatible versions
    ```
    
    !!! tip
        Durante la carga del servicio de Copilot, la herramienta se cargará y las dependencias se instalarán. Además, las dependencias se probarán para garantizar que se han instalado correctamente.


    !!! warning "Nombre diferente de la dependencia al instalar e importar"
        
        Si el nombre de la dependencia es diferente del nombre del paquete que se importa en la herramienta, es necesario especificarlo. 
        
        Por ejemplo, si la dependencia se instala con el nombre `pyscopg2-binary` pero se importa con el nombre `psycopg2`, podemos usar un `|` para especificar ambos nombres. 
        
        Si no se realiza esta aclaración, la herramienta no podrá importar la dependencia para comprobar si está instalada correctamente; esto lanzará una advertencia, pero la herramienta podrá ejecutarse.
        
        El contenido del archivo será el siguiente:

        ``` toml
        [ToolName]
        "pyscopg2-binary|psycopg2" = "*"
        ```

4. Reiniciar el servicio de Copilot: 

    ``` Title="Termina"
    ./gradlew resources.stop
    ```

    ``` Title="Termina"
    ./gradlew resources.up
    ```

5. Abra la ventana **Habilidad/Herramienta** en **Etendo Classic** (rol System Administrator). Cree un nuevo registro con:

    - *Identificador*: debe coincidir con el nombre de la clase de la herramienta.
    - *Nombre*: el nombre de la herramienta. Se muestra en la UI de Copilot.
    - *Módulo*: establezca el módulo creado en el paso 1.
    - *Descripción*: se completa automáticamente desde la clase de Python al sincronizar la herramienta.
    - *Información JSON*: contiene una descripción JSON de la herramienta, entradas y salidas. Se completa automáticamente al sincronizar la herramienta.

    Para recuperar la información de parámetros desde la definición de la herramienta, ejecute **Sincronizar estructura de herramienta**. 
 
    !!! Warning Before Sync Tool Structure
        Es obligatorio tener Copilot en ejecución y la herramienta cargada en el contenedor de Copilot. Si la herramienta no está cargada, el proceso no recuperará los parámetros de la herramienta.

    ![how-to-create-copilot-tools.png](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-create-copilot-tools/how-to-create-copilot-tools.png)

6. Después de definir la herramienta, exporte las configuraciones al módulo:
    
    ```bash title="Terminal"
    ./gradlew export.database
    ```

7. Una vez definida la **Herramienta de Copilot**, esta herramienta debe asociarse al/los agente(s). Para ello, debe crearse un registro en la pestaña *tools* de la ventana **Agente**; este registro permitirá activar o desactivar la herramienta.

    ![how-to-create-copilot-tools-2.png](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-create-copilot-tools/how-to-create-copilot-tools-2.png)

    !!! note
        Recuerde ejecutar el proceso `Sync Agent` después de vincular la herramienta; de lo contrario, la herramienta no estará disponible en el agente.


8. Para probar la herramienta desarrollada, puede solicitar a un agente que tenga la herramienta asociada que realice la acción requerida; el agente ejecutará la herramienta y devolverá el resultado.


## Interactuar con Etendo

Al crear herramientas que necesiten interactuar con **Etendo Classic**, el mejor enfoque es utilizar la **API de Webhooks de Eventos**. Esta API simplifica la autenticación y permite que sus herramientas disparen webhooks con datos.

### Utilizar la API de Webhooks de Eventos de Etendo Classic

La **API de Webhooks de Eventos de Etendo Classic** es una funcionalidad estándar en Etendo y permite una integración más sencilla con herramientas mediante utilidades de Copilot. Por ejemplo, si necesita disparar un WebHook llamado `UpdateOrderDescription` para actualizar un pedido en Etendo Classic, recibiendo un número de documento y una descripción como parámetros, puede hacerlo creando una herramienta específica.

### Herramienta de ejemplo: UpdateSOTool

Aquí tiene un ejemplo de una herramienta que dispara el WebHook `UpdateOrderDescription`:

```python

from typing import Type, Dict

from copilot.core.etendo_utils import call_webhook, get_etendo_token, get_etendo_host
from copilot.core.tool_input import ToolInput, ToolField
from copilot.core.tool_wrapper import ToolWrapper, ToolOutput, ToolOutputMessage

class UpdateSOToolInput(ToolInput):
   documentNo: str = ToolField(description="DocumentNo of the Sales Order")
   description: str = ToolField(description="New description to set in the Sales Order")

class UpdateSOTool(ToolWrapper):
   name: str = "UpdateSOTool"
   description: str  = "Set description in a Sales Order by DocumentNo2"
   args_schema: Type[ToolInput] = UpdateSOToolInput
   return_direct: bool = False

   def run(self, input_params: Dict = None, *args, **kwargs) -> ToolOutput:
       documentNo = input_params['documentNo']
       description = input_params['description']
       token = get_etendo_token()
       # Build the body of the request
       body = {
           "documentNo": documentNo,
           "description": description
       }
       url = get_etendo_host()
       response = call_webhook(url=url, webhook_name="UpdateOrderDescription", access_token=token, body_params=body)
       return ToolOutputMessage(message=response)
```

### Explicación de los componentes de la herramienta

La herramienta anterior aprovecha utilidades proporcionadas por Copilot Core:

- `get_etendo_token()`: esta función devuelve el token de autenticación para Etendo Classic, permitiendo que la herramienta opere dentro de la sesión del usuario. Copilot, actuando como un "proxy", gestiona estas sesiones.

- `get_etendo_host()`: esta función devuelve la URL de la instancia de Etendo Classic, que es necesaria para disparar el WebHook. Esta URL de host se configura como `ETENDO_HOST` en el archivo de configuración `gradle.properties`.

- `call_webhook(url:String, webhook_name:String, access_token:String, body_params:Dict)`: esta función dispara el WebHook, pasando la URL de Etendo Classic, el nombre del WebHook, el token de autenticación y los parámetros necesarios por el WebHook.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.