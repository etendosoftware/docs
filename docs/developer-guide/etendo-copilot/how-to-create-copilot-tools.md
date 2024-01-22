---
title: How to create Copilot tools
tags:
    - Copilot
    - IA
    - Machine Learning
---
## Overview
This article explains how to create a new tool for Copilot.

## Etendo Copilot

Etendo Copilot module allows the creation of tools that add functionality to it. These tools are developed in Python and run in the Docker container where Copilot runs. Next, we explain how to create a new tool for Copilot, in a new module. But you can also add a new tool in an existing module and it can contain several tools.

!!! note "Etendo Copilot is based on Langchain"
    The Langchain libraries are available by default in Copilot. You can use them in your tools. See [Langchain documentation](https://python.langchain.com/) for more information.

### Requirements
- Copilot module installed in Etendo Classic. If you do not have it, you can install it using the getting started guide for the Copilot API. [Installation](/developer-guide/etendo-copilot/installation/){target="_blank"}.

### Create a new tool
For this example, we will create a tool that will allow us to make a ping to a host. The tool will be called `Ping Tool` and will be located in the `com.etendoerp.copilot.pingtool` package.

!!! note "Create the classic module"
    
    Copilot tools are created within an etendo classic module. So the first thing we have to do is create an etendo classic module. 

1. The structure of the module will be as follows:

    ``` 
    modules
    └── com.etendoerp.copilot.pingtool
        ├── src-db 
        │   └── database
        │       ├── sourcedata
        │       ├── AD_MODULE.xml
        │       ├── AD_MODULE_DBPREFIX.xml
        │       └── AD_MODULE_DEPENDENCY.xml
        ├── tools 
        │   └── PingTool.py
        ├── .gitignore
        ├── build.gradle
        └── tools_deps.toml
    ```
    **src-db**: Contains the database structure of the module. This folder is created automatically when creating and exporting the module from Etendo Classic.
   
    **tools**: Contains the tools of the module. Can contain one or more tools.
    
    **.gitignore**: Contains the files that will be ignored by git.
   
    **build.gradle**: Contains the configuration of the module. This file is created when the module is prepared to be published. See 
    [How to publish modules to GitHub repository](/developer-guide/etendo-classic/how-to-guides/how-to-publish-modules-to-github-repository/)
    
   
    **tools_deps.toml**: Contains the dependencies of the tools of the module. This file contains the dependencies of the tools of the module.


2. Create the file `PingTool.py` in the `tools` folder. This file will contain the code of the tool. The code of the tool will be as follows, the comments explain the code:

    ```python
    import os
    from copilot.core.tool_wrapper import ToolWrapper # Import the ToolWrapper class from the copilot.core.tool_wrapper module. This class is the one that must be extended to create a new tool.

    class PingTool (ToolWrapper):
        name = 'PingTool' # Name of the tool
        description = ('''This tool receives a hostname and returns the ping result.''') # Description of the tool. This description tells Copilot what the tool does and based on this description it will decide if this tool will solve the user's request.

        def run(self, host: str, *args, **kwargs): # The run method is the one that will be executed when the tool is executed. The inputs of the method are the inputs of the tool.
            import requests # Import the necessary libraries to execute the tool. It is recommended to import the libraries inside the run method to avoid conflicts with other tools.
            response = requests.get(host)
            return {"status_code": response.status_code}  # The run method must return a dictionary with the outputs of the tool.
    ``` 
    **Note**: The name of the tool must be the same as the name of the class that extends the ToolWrapper class.

3. In case the tool needs more than one input, its necessary to use a Dict as input. In order to do that, we have to create a new class that defines the inputs of the tool using pydantic. Here is an example of a tool that receives a Dict as input, with the structure of the Dict defined in a class:

    ```python
    import os
    from typing import Type, Dict

    from pydantic import BaseModel, Field

    from copilot.core.tool_wrapper import ToolWrapper  # Import the ToolWrapper class from the copilot.core.tool_wrapper module. This class is the one that must be extended to create a new tool.


    class PingToolInput(BaseModel):
        host: str = Field(
            title="Host",
            description='''The host to ping.''',
        )
        message_to_print: str = Field(
            default="default message!",  # Default value of the input, if there is no default value, the input is mandatory.
            title="Message to print",
            description=" Custom message to print before the ping result.",
        )


    class PingTool(ToolWrapper):
        name = 'PingTool'  # Name of the tool
        # Description of the tool.
        # This description tells Copilot what the tool does and based on this description it will decide if this tool will solve the user's request.
        description = (
            '''This tool receives a hostname and returns the ping result.''')
        args_schema: Type[
            BaseModel] = PingToolInput  # The args_schema attribute must be a Pydantic model that defines the inputs of the tool.
        return_direct = True

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
    !!! note "Enviroment variables"
        Automatically, Copilot reads the gradle.properties file of Etendo Classic and add configuration as environment variables. The name of the environment variable will be the same as the name of the property. The only difference is that the . is replaced by _. For example, if we have the property `COPILOT_PORT` in the gradle.properties file, Copilot will create the environment variable `COPILOT_PORT`. If we have the property `bbdd.sid` in the gradle.properties file, Copilot will create the environment variable `bbdd_sid`.
         This allows us to use the environment variables in the tools. 
        

4. Create the file `tools_deps.toml` in the root folder of the module. This file will contain the dependencies of the tools of the module. The content of the file follows the TOML format. The content of the file will be as follows this format:

    ``` toml
    [ToolName]
    dependency_name = "dependency_version"
    dependency_name = "dependency_version"
    ```
    For our example, the content of the file will be as follows:

    ``` toml
    [PingTool]
    requests = "*"
    ```
    The name of the tool must be the same as the name of the class that extends the ToolWrapper class. In our case, the name of the tool is `PingTool` and the name of the class that extends the ToolWrapper class is also `PingTool`. During the load of copilot, the tool will be loaded and the dependencies will be installed. Additionally, the dependencies will be tested to ensure that they are installed correctly.

    The version of the dependency can be specified or not. If the version is not specified, the latest version will be installed. If the version is specified, the version specified will be installed. The version can be specified with the following operators:
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


    !!! warning "Different name of depedency while installing and importing"
        If the name of the dependency is different from the name of the dependency that is imported in the tool, it is necessary to specify the name of the dependency that is imported in the tool. For example, if the dependency is installed with the name `pyscopg2-binary` but is imported with the name `psycopg2`, we can use a | to specify both names. The content of the file will be as follows:


        ``` toml
        [PingTool]
        requests2 = "*" 

        [OtherTool]
        "pyscopg2-binary|psycopg2" = "*"   # First name is the name of the dependency that is installed, second name is the name of the dependency that is imported. In the tool code, we will do import psycopg2
        ```

5. Finally, we have to start Copilot and check that the tool and it dependencies are installed correctly. After starting Copilot, we can try to call the tool asking Copilot to execute it or, for example, list us which tools are available.
