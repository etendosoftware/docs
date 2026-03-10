---
tags:
    - Copilot
    - Herramientas
    - Creador
    - Agentes
    - Agente de desarrollo
    - Asistente de desarrollo
---

# Asistente de desarrollo

:octicons-package-16: Paquete Java:  `com.etendoerp.copilot.devassistant`
## Visión general

Esta página proporciona una visión general de las herramientas, la funcionalidad y los ejemplos de uso de los distintos agentes de desarrollo disponibles en Etendo. **Dev Assistant** agiliza la gestión del flujo de trabajo para los desarrolladores ofreciendo agentes especializados que simplifican tareas como la creación de botones, ventanas, solapas y tablas, manejadores de eventos, informes Jasper, procesos en segundo plano y más. Estos agentes están diseñados para mejorar la productividad y reducir la complejidad, facilitando que los desarrolladores creen y gestionen de forma eficiente distintos componentes dentro de la plataforma Etendo.

<iframe width="560" height="315" src="https://www.youtube.com/embed/58U9LThdTGo?si=kSxA3MAf22U8fdHh" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

!!!info
    Para poder incluir esta funcionalidad, debe estar instalado el Copilot Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="_blank"}. Para más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Copilot Extensions - Notas de la versión](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

!!!warning
    Tenga en cuenta que los agentes se encuentran actualmente en su fase de pruebas beta.
## Agentes

### Supervisor de Dev Assistant
El Agente de Desarrollo optimiza la gestión del flujo de trabajo para desarrolladores ofreciendo asistentes especializados que simplifican tareas como la creación de botones, ventanas, solapas y tablas, manejadores de eventos, informes Jasper, procesos en segundo plano y más.

**Funcionalidad**

El Agente de Desarrollo actúa como un asistente integrado que automatiza y acelera tareas repetitivas en el ciclo de vida de una aplicación, permitiéndole centrarse en la lógica de negocio y la experiencia de usuario. Su función principal es eliminar la “fontanería” y el código repetitivo: genera y configura automáticamente los elementos de la interfaz, vincula la lógica de eventos, construye informes y orquesta procesos en segundo plano, todo ello sin que usted tenga que escribir manualmente decenas de archivos o parámetros. Al integrarse directamente en su entorno de desarrollo, garantiza que cada componente cumpla con las convenciones de su proyecto y minimiza los errores de configuración, optimizando así su productividad y la calidad del código.

**Miembros del equipo**
#### Creador de procesos en segundo plano

**Creador de procesos en segundo plano** es un agente especializado en la creación automática de procesos en segundo plano en Java. El agente lee código previamente indexado y utiliza ejemplos de clases que extienden `DalBaseProcess` para construir nuevos procesos en segundo plano.

**Herramientas**

- [Herramienta de llamada a la API](../available-tools/openapi-tool.md)
- [Herramienta de lectura de archivos](../available-tools/read-file-tool.md)
- [Herramienta de escritura de archivos](../available-tools/write-file-tool.md)

**Funcionalidad**

El Creador de procesos en segundo plano genera procesos en segundo plano en Java utilizando ejemplos indexados de clases que extienden `DalBaseProcess`. Para configurar el agente correctamente, debe proporcionar los siguientes parámetros:

- **Paquete Java**: El paquete Java donde se guardará el nuevo proceso. Debe seguir el formato `java.package.of.the.module`.
- **Nombre**: El nombre del archivo Java que se creará.
- **Identificador**: Una clave que se utilizará para localizar el proceso en otras ventanas cuando sea necesario.
- **Descripción del código**: El propósito y la lógica que debe cumplir el proceso en segundo plano.

**Ejemplo de uso**

1. Para utilizar este agente, es necesario iniciar sesión con el rol `System Administrator` y configurar el acceso del rol. Para ello, vaya a la ventana **Agente**, seleccione Creador de procesos en segundo plano y sincronícelo. A continuación, vaya a la ventana **Acceso de agente** y otorgue acceso al rol.

    ![background.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/BG1.png)

2. Abra Copilot y seleccione Creador de procesos en segundo plano; a continuación, solicite al agente lo que necesita crear.

3. A continuación, este es el resultado proporcionado por el agente.

    ![background.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/BG2.png)
    ![background.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/BG3.png)
#### Creador de procesos de botón

El **Agente de creación de procesos de botón** simplifica el proceso de creación y registro de botones y definiciones de proceso en Etendo Classic. Al automatizar el flujo de trabajo mediante webhooks, elimina la necesidad de configuración manual, garantizando que sus procesos y botones se configuren de forma correcta y eficiente.

**Herramientas**

- [ApiCallTool](../available-tools/openapi-tool.md) 
    
- [ReadFileTool](../available-tools/read-file-tool.md)

- [WriteFileTool](../available-tools/write-file-tool.md)

**Funcionalidad**

El **Agente de creación de procesos de botón** automatiza la creación de un botón y el registro de un proceso en Etendo Classic mediante una llamada a un webhook. A través de una llamada a un webhook, la herramienta garantiza la configuración correcta validando los parámetros necesarios, como el prefijo del módulo, el Paquete Java y el nombre del proceso, asegurando que el Identificador esté correctamente formado. A continuación, genera una clase Java para el botón, que extiende `BaseProcessActionHandler`, y registra este botón en la Ventana, Solapa y Tabla deseadas dentro del sistema Etendo.

Además, define y registra el proceso creando una definición de proceso y asociándola con los Parámetros requeridos, incluyendo atributos como el nombre de base de datos, la Longitud y la Referencia, garantizando la integración y la funcionalidad dentro del sistema.

Al crear un botón o registrar un proceso, el agente solicitará la siguiente información:

- **Paquete Java**: El paquete Java del módulo donde se creará la clase del botón (p. ej., `com.etendoerp.module`).
- **Prefijo del módulo**: Un prefijo para el módulo (p. ej., `COPDEV`).
- **Ventana**: La ventana en Etendo donde aparecerá el botón.
- **Solapa**: La solapa específica dentro de la ventana donde se ubicará el botón.
- **Tabla**: La tabla asociada al proceso.
- **Nombre del proceso**: El nombre del proceso que se va a crear.
- **Identificador**: Un identificador único para el proceso que incluya el prefijo del módulo (p. ej., `COPDEV_ActualizarDescripciónPedido`).
- **Parámetros**: Parámetros opcionales para el proceso, incluyendo:
    - **BD_NAME**: El nombre de la columna de base de datos.
    - **NAME**: El nombre del parámetro.
    - **LENGTH**: La longitud del campo del parámetro.
    - **SEQNO**: El número de secuencia del parámetro.
    - **REFERENCE**: Una referencia para el parámetro (si está vinculado a otro campo o tabla).
- **Comentario de ayuda**: Un comentario de ayuda opcional para el proceso.
- **Descripción**: Una descripción opcional para el proceso.

La llamada al webhook utilizada para registrar el proceso en Etendo requerirá los siguientes parámetros del cuerpo:

```json
body_params = {
    "Prefix": "COPDEV",
    "SearchKey": "COPDEV_ActualizarDescripciónPedido",
    "ProcessName": "ActualizarDescripciónPedidos",
    "HelpComment": "This process updates the description of associated orders.",
    "Description": "A process to update the description of the associated sales orders based on a text input.",
    "Parameters": [
        {
            "BD_NAME": "text_parameter",
            "NAME": "Description Text",
            "LENGTH": 255,
            "SEQNO": 10,
            "REFERENCE": "Text"
        }
    ],
    "JavaPackage": "com.etendoerp.copilot.devassistant"
}
```

Esta llamada registra el proceso en el sistema y adjunta los parámetros necesarios.

**Ejemplo de uso** 

El proceso y el botón se registrarán automáticamente, y se notificará al usuario.

![ButtonProcess.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/button-process-1.png)

En este punto, tendremos creada la clase Java del botón junto con el proceso registrado.

![ButtonProcess2.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/button-process-2.png)
#### Ejecución de código

**Ejecución de código** es un agente diseñado para ejecutar comandos de Python en un entorno controlado. Traduce la solicitud a comandos de Python o Bash para completar la tarea.

**Herramientas**

- [Herramienta Docker](../available-tools/docker-tool.md)

**Funcionalidad**

Ejecución de código permite a los usuarios ejecutar scripts y comandos de Python de forma dinámica, incluso si faltan dependencias o configuraciones. Las funcionalidades clave incluyen:

1. Ejecución dinámica de código:

    - Permite ejecutar fragmentos de código Python.

    - Ejemplo: `print('Hello, World!')`.


2. Solicitudes en lenguaje natural:

    - Los usuarios pueden proporcionar tareas en lenguaje natural (p. ej., "Ping Google"), y el agente las traduce a comandos ejecutables de Python o Bash.


3. Gestión automática de dependencias:

    - Identifica e instala librerías faltantes cuando una tarea las requiere.

    - Ejemplo: `!pip install numpy`.


4. Gestión de errores:

    - Proporciona mensajes de error significativos para comandos no válidos o entradas faltantes.


5. Gestión flexible de tareas:

    - Soporta operaciones con archivos y flujos de trabajo de varios pasos combinando Python y Bash.


**Ejemplo de uso**

1. Inicie sesión en el sistema con el rol de **Administrador del Sistema** y configure el agente en la ventana **Agente**. Sincronícelo y conceda acceso al rol en la ventana **Acceso del agente**.

2. Abra Copilot y seleccione **Ejecución de código**. A continuación, solicite al agente lo que necesita ejecutar.

3. Ejemplo de interacción y resultado:

    ![code-run-example.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/code-run-example.png)

    **Entrada:**

    - "Cree un programa en Python que calcule la suma de los números entre 1 y 100."

    **Ejecución:**

    - El agente procesa la solicitud y ejecuta el siguiente código Python:

      ```python
      def calculate_sum(start, end):
          return sum(range(start, end + 1))

     # Calculate the sum of numbers between 1 and 100
      result = calculate_sum(1, 100)
      print(f'The sum of numbers between 1 and 100 is: {result}')
      ```

    **Resultado:**

    - El agente muestra el resultado del programa:

      ```
      The sum of numbers between 1 and 100 is: 5050
      ```
#### Etendo Code Expert 

**Etendo Code Expert** es un agente diseñado para leer archivos indexados y proporcionar respuestas relacionadas con su contenido. 

**Funcionalidad**

Con este agente es posible realizar **preguntas de desarrollo de código** y, en base al código de Etendo indexado, el agente proporcionará posibles sugerencias o soluciones de código. Puede resumir, responder preguntas técnicas, sugerir mejoras en el código de programación y ofrecer asistencia general sobre archivos.

Este agente es útil para evitar la necesidad de revisar manualmente todos los archivos. Además, si es necesario, se pueden configurar múltiples archivos.


**Ejemplo de uso** 

1. Para utilizar este agente, es necesario iniciar sesión con el rol `System Administrator` y configurar el acceso del rol. Este agente no incluye la ruta configurada a los archivos indexados. Para ello, vaya a la ventana **Archivo de base de conocimiento** en `Application`>`Service`>`Copilot`>`Knowledge Base File` y seleccione el archivo `EtendoJAvaSourceCode` y, en la **Solapa Ruta del archivo**, especifique la ruta donde se encuentran los archivos de código que necesita que el agente lea. 
		
	<figure markdown="span">
		![code-expert.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/etendo-code-expert3.png)
		<figcaption>En este ejemplo, utilizando la ruta mostrada en la imagen, obtendremos todos los archivos con extensión Java del código fuente del core de Etendo</figcaption>
	</figure>


2.  A continuación, vaya a la ventana **Agente**, configure Etendo Code Expert y sincronícelo. Después, vaya a la ventana **Acceso del agente** y conceda acceso al rol.  

3. Comience a utilizar el agente. Abra Copilot y seleccione Etendo Code Expert.

    ![code-expert.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/etendo-code-expert1.png)

4. Pregunte al agente lo que necesita crear.

    ![code-expert.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/etendo-code-expert2.png)
#### Creador de manejadores de eventos

Este agente es capaz de crear **manejadores de eventos** en Etendo Classic. Solo necesita proporcionar el Paquete Java del módulo donde debe exportarse y especificar la acción que se debe realizar.

**Herramientas**

- [Herramienta de lectura de archivos](../available-tools/read-file-tool.md)
  
- [Herramienta de escritura de archivos](../available-tools/write-file-tool.md)

**Funcionalidad**

**Creador de manejadores de eventos** es un agente diseñado para crear automáticamente manejadores de eventos en Java. Utiliza código indexado en su base de conocimiento para leer clases que extienden `EntityPersistenceEventObserver`, proporcionando ejemplos para construir un nuevo manejador de eventos. Para generar un manejador de eventos, el agente requiere los siguientes parámetros:
  
- **Paquete Java**: El paquete donde se guardará el archivo.
- **Nombre archivo**: El nombre del archivo que se va a crear.
- **Entidad**: La entidad que se va a observar.
- **Descripción**: Una descripción de la funcionalidad que debe implementar el manejador de eventos.

**Ejemplo de uso**

1. Para utilizar este agente, es necesario iniciar sesión con el rol `System Administrator` y configurar el acceso del rol. Para ello, vaya a la ventana **Agente**, seleccione Creador de manejadores de eventos y sincronícelo. A continuación, vaya a la ventana **Acceso de agente** y otorgue acceso al rol.

2. Abra Copilot y seleccione Creador de manejadores de eventos; a continuación, solicite al agente lo que necesita crear.

    ![eventhandler.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/event-handler-creator-1.png)

3. A continuación, este es el resultado proporcionado por el agente.

    ![eventhandler.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/event-handler-creator-2.png)
#### Creador de informes Jasper

El **Agente Jasper** está diseñado para facilitar la creación, edición y registro de informes dentro de la plataforma Etendo. Usando JasperReports, permite a los desarrolladores definir la estructura del informe, aplicar estilos, gestionar parámetros y registrar los informes en el sistema para utilizarlos en diferentes módulos.

!!!info
    Este agente simplifica el proceso verificando que todos los campos utilizados en un informe estén correctamente definidos en la base de datos, evitando así errores comunes como **Campo no encontrado**. También permite integrar logotipos, aplicar estilos y realizar agrupaciones de datos para garantizar que los informes cumplan los requisitos del negocio.

**Herramientas**

- **JasperTool**

- [OCRTool](../available-tools/ocr-tool.md)

- [ReadFileTool](../available-tools/read-file-tool.md)

- [WriteFileTool](../available-tools/write-file-tool.md)

**Funcionalidad**

**Creación de informes**

El agente Jasper solicita los siguientes parámetros para crear un informe:

- **Ruta de almacenamiento del informe**: La ubicación en el sistema de archivos donde se guardará el archivo del informe.
- **Nombre del informe**: El nombre que se asignará al informe.
- **Idioma de codificación del informe**: El idioma en el que se codificará el informe (por defecto es UTF-8).
- **Parámetros del informe**: Una lista de parámetros que aceptará el informe.
- **Consulta SQL**: La consulta SQL que proporcionará los datos al informe.
- **Estilos del informe**: Definición de los estilos visuales aplicados al informe.
- **Agrupación de datos**: Configuración de la agrupación de datos dentro del informe.
- **Imagen o logotipo en el informe**: Especificación de imágenes o logotipos a incluir.
- **Distribución de datos**: Estructura de cómo se organizarán los datos en el informe.

**Registro de informes**

Una vez creado el informe, puede registrarse en el sistema. El agente solicita los siguientes argumentos:

- **Nombre del informe**: Nombre que se utilizará para registrar el informe en el sistema.
- **Prefijo del módulo**: Prefijo que identifica el módulo donde se registrará el informe.
- **Identificador**: Clave única para identificar el informe en el sistema.
- **Comentarios de ayuda**: Información adicional para ayudar a comprender el propósito del informe.
- **Descripción**: Descripción detallada del informe.
- **Ruta del informe**: Ruta donde se almacena el informe.
- **Parámetros**: Lista de parámetros registrados que pueden utilizarse al ejecutar el informe.

**Edición de informes**

El agente también permite editar informes existentes. Las acciones disponibles incluyen:

- **Modificación de parámetros**: Permite editar cualquier parámetro de informe ya registrado.
- **Actualización de la consulta SQL**: Modificación de la consulta SQL utilizada por el informe.
- **Cambio de estilos y agrupaciones**: Actualización de los estilos visuales y de la configuración de agrupación de datos.

**Ejemplo de uso**

1. Para utilizar este agente, es necesario iniciar sesión con el rol `System Administrator` y configurar el acceso del rol. Para ello, vaya a la ventana **Agente**, seleccione Creador de informes Jasper y sincronícelo. Luego, vaya a la ventana **Acceso del agente** y otorgue acceso al rol.  

2. Abra Copilot y seleccione Creador de informes Jasper

3. En función de la solicitud, el Agente Jasper devolverá:

**Creación de informes**

![CreateReport.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/create-report.png)


**Registro de informes**

![RegistrateReport.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/RegistrateReport.png)

Después de ejecutar el smartbuild, podremos ver el proceso del informe creado:

![RegistrateReport3.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/RegistrateReport3.png)

Como puede ver en la imagen, también añade los parámetros e incluso en la solapa **Definición Informe**, define la plantilla PDF del informe y en el **Menú**, crea la definición del proceso que hemos definido en el paso anterior.

![RegistrateReport4.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/RegistrateReport4.png)

![RegistrateReport5.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/RegistrateReport5.png)


Finalmente, podemos observar el informe creado y establecer el parámetro elegido para ver la versión impresa.

![RegistrateReport6.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/RegistrateReport6.png)


**Edición de informes**

![EditReport.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/edit-report.png)
#### Creador de mensajes

El **Creador de mensajes** agiliza el proceso de creación y registro de AD_Messages en Etendo Classic. Al utilizar un webhook, garantiza una creación de mensajes eficiente y sin errores, cumpliendo las convenciones de nomenclatura y las mejores prácticas.

**Herramientas**

- [ApiCallTool](../available-tools/openapi-tool.md)

**Funcionalidad**

El **Creador de mensajes** facilita la creación de AD_Messages interactuando con Etendo Classic mediante un webhook. Valida los parámetros de entrada, aplica el formato correcto para los identificadores y registra el mensaje con el módulo correspondiente. Este agente admite tanto mensajes paramétricos como no paramétricos y garantiza que los mensajes sean utilizables inmediatamente en código Java.

El agente realiza las siguientes tareas:

- **Valida los parámetros de entrada**: garantiza que se proporcionen correctamente los campos obligatorios como el paquete Java del módulo, el identificador, el tipo de mensaje y el mensaje de texto.
- **Aplicación del formato del identificador**: confirma que los identificadores siguen el formato requerido: `PREFIX_DescriptiveName`, donde:
  - `PREFIX` es el prefijo del módulo en mayúsculas.
  - `DescriptiveName` está en CamelCase.
  - La longitud total no supera los 32 caracteres.
- **Validación del tipo de mensaje**: confirma que el tipo de mensaje es `"I"` (Informativo) o `"E"` (Error).
- **Registra el AD_Message**: guarda el mensaje en el sistema, vinculándolo al módulo especificado.

Al crear un mensaje, el agente solicitará la siguiente información:

- **Paquete Java del módulo**: el paquete Java del módulo donde se creará el mensaje (p. ej., `com.etendoerp.module`).
- **Identificador**: un identificador único para el mensaje siguiendo el formato `PREFIX_DescriptiveName`.
- **Tipo de mensaje**: el tipo de mensaje:
  - `"I"` para mensajes informativos.
  - `"E"` para mensajes de error.
- **Mensaje de texto**: el contenido del mensaje.

Notas:

- **Módulo en desarrollo**: el módulo debe estar configurado en modo de desarrollo para permitir que el agente lo cree.

- **Usabilidad en Java**: tras su creación, el AD_Message puede utilizarse en Java con:  
  `OBMessageUtils.messageBD("MESSAGE_SEARCH_KEY")`.

- **Mensajes paramétricos**: si el mensaje requiere parámetros, puede añadirse `%s` al texto, y el agente proporcionará un fragmento de código para usar `String.format`.  
  Ejemplo:  
  **Mensaje de texto**: `"The value %s is invalid."`  
  **Uso en Java**:  
  ```java
  String formattedMessage = String.format(OBMessageUtils.messageBD("PREFIX_InvalidValue"), value);
  ```

**Ejemplo de uso**

1. Proporcione las entradas requeridas:
    - Paquete Java del módulo: `com.etendoerp.module`
    - Identificador: `MODPREFIX_InvalidInput`
    - Tipo de mensaje: `E`
    - Mensaje de texto: `"The input provided is not valid."`

    ![MessageCreator_1.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/message-creator-1.png)

2. El agente valida y envía la solicitud al webhook.

3. Tras una creación correcta, el sistema confirmará:
    - Mensaje creado con la clave: `MODPREFIX_InvalidInput`.

    ![MessageCreator_2.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/message-creator-2.png)

4. El mensaje está listo para su uso en Java:
    ```java
    OBMessageUtils.messageBD("MODPREFIX_InvalidInput");
    ```
#### Creador de Módulos

Etendo Classic le permite crear módulos que proporcionan funcionalidad adicional y que pueden desplegarse de forma independiente. Estos módulos pueden abarcar desde informes adicionales hasta paquetes de contenido (traducciones, plan contable, etc.).

**Herramientas**

- [ApiCallTool](../available-tools/openapi-tool.md)

**Funcionalidad**

El Creador de Módulos agiliza el proceso de construir módulos independientes que mejoran Etendo Classic con nuevas funcionalidades, como informes adicionales o paquetes de contenido como traducciones o planes contables. Mediante el `CreateModuleWebHook`, la herramienta automatiza varios pasos críticos. Comienza validando detalles esenciales como el paquete Java del módulo, el nombre, la descripción, la versión y el prefijo de base de datos, asegurando que todo esté correctamente formateado y completo. Tras la validación, asigna el prefijo de base de datos necesario, registra el módulo dentro del sistema y permite la inclusión opcional de dependencias.

Para comenzar a crear su módulo en Etendo, siga los pasos a continuación.

- Proporcione la siguiente información:

- **Javapackage**: El paquete Java del módulo (p. ej., `com.etendoerp.copilot.prueba`).
- **Nombre del Módulo**: Un nombre para su módulo (p. ej., `Test Module`).
- **Descripción**: Una breve descripción de la funcionalidad del módulo.
- **Ayuda/Comentario**: Texto de ayuda adicional o comentarios sobre el módulo (opcional).
- **Versión**: La versión del módulo (p. ej., `1.0.0`).
- **Tipo**: El tipo de módulo. Las opciones son "M" para módulo estándar, "T" para módulo plantilla.
- **DBprefix**: Un prefijo para los objetos de base de datos asociados al módulo (debe estar en mayúsculas, p. ej., `LAPY`).
- **Licencia**: El tipo de licencia del módulo. Las opciones son:
    - `Apache License 2.0`
    - `Openbravo Public License`
    - `Mozilla Public License 1.1`
    - `Etendo Commercial License`

- Llame al `CreateModuleWebHook`. El `CreateModuleWebHook` simplifica el proceso de creación automatizando varios pasos. Este webhook:

- Validará todos los parámetros (como el nombre del módulo, la versión y la licencia).
- Asignará el prefijo de base de datos.
- Registrará el módulo.
- Opcionalmente, añadirá dependencias del módulo.

- Al invocar el webhook, los **parámetros del body** deben seguir esta estructura:

```json
body_params = {
  "Javapackage": "com.etendoerp.copilot.test",
  "SearchKey": "testmodule",
  "ModuleName": "Test Module",
  "HelpComment": "This is a test module created for demonstration purposes.",
  "Description": "This module adds test functionality to Etendo Classic.",
  "Version": "1.0.0",
  "Prefix": "LAPY",
  "Type": "M",
  "ModuleLicense": "Etendo Commercial License"
}
```

!!!note
    El prefijo de base de datos debe estar siempre en mayúsculas.

**Ejemplo de uso**

1. Para utilizar este agente, es necesario iniciar sesión con el rol `System Administrator` y configurar el acceso del rol. Para ello, vaya a la ventana **Agente**, seleccione Creador de Módulos y sincronícelo. Luego, vaya a la ventana **Acceso de Agente** y conceda acceso al rol.

2. Abra Copilot y seleccione Creador de Módulos; a continuación, solicite al agente lo que necesita crear.

![ModuleCreation.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/module-creator.png)

Si vamos a la ventana **Módulo** podemos encontrar el registro creado.

![ModuleCreation2.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/module-creator-2.png)

El módulo también tendrá la dependencia; en este caso **Core**, con el prefijo y el paquete de datos mencionados por el usuario.

![ModuleCreation3.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/module-creator-3.png)

![ModuleCreation4.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/module-creator-4.png)

![ModuleCreation5.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/module-creator-5.png)

Una vez que se haya llamado al webhook, automáticamente:

- Registrará el módulo en Etendo.
- Asignará el **Paquete Java** y el **prefijo de base de datos**.
- Gestionará la **licencia** especificada.
- Configurará las **dependencias del módulo** básicas.

Puede confirmar que el módulo se ha creado navegando a la ventana `Módulo` en Etendo.

!!!note
    Si su módulo depende de otros módulos (además del módulo Core), debe añadir manualmente estas dependencias en la solapa `Dependency` de la ventana del módulo.

!!!info
    Para una mayor personalización y desarrollo, consulte la guía oficial [Guía del desarrollador de Etendo](../../etendo-classic/how-to-guides/how-to-create-a-page-in-etendo-documentation.md) para ver pasos más detallados.
#### Creador de traducciones de módulos

**Herramientas**

- [Herramienta de traducción XML](../available-tools/xml-translation-tool.md)

**Funcionalidad**

El Creador de traducciones de módulos traduce automáticamente el contenido de un módulo.

Antes de usar el agente, el usuario deberá tener ya creado un módulo de traducción con los archivos XML a traducir.
!!!note
    Para más información, consulte [Cómo crear y actualizar módulos de traducción](../../../developer-guide/etendo-classic/how-to-guides/how-to-create-and-update-translation-modules.md){target="_blank"}.

A continuación, proporcione al agente la ruta al módulo de traducción (por ejemplo, `/modules/com.etendoerp.mymodule.es_ES`) y traducirá automáticamente todos los archivos al idioma deseado.

**Ejemplo de uso**
1. Cree un nuevo módulo en la ventana `Módulo`
    - Marque el indicador "Es un módulo de traducción".
    - Seleccione el idioma del módulo (por ejemplo, `Español (España)`). 
    - Debe depender del módulo que desea traducir.

2. Si es la primera vez que se configura el idioma:
    - En la ventana `Idioma`, busque el idioma seleccionado y marque la casilla de verificación "Idioma del Sistema".
    - Ejecute el botón `Verify Languages``.
![](../../../assets/drive/6WuHosAvU6L3iCuQ8tLMzV9c_gTxjhk7whON6b3eWd67uR9bJKlrynGI686XRxXjNXngvQcL_5u8kmI-RnBCxq7ofI1QlZB1MlyTFRU2yf6Ukdrqy6768L7Wo6osm7Spy7nCHAbguCxp81ulGHaThEN57W--AXtajOXOuPzdj8ikaOeV4ZEj5r7UhjtuCw.png)

3. A continuación, vaya a la ventana "Import/Export Language", seleccione el idioma y ejecute el proceso de exportación (esto puede tardar un tiempo en finalizar).
![](../../../assets/drive/fSONWx4HIzELPexas8U20mjvn5nJk774cD_YAickqJG7dmvdLXlBOTGbOIKYMGpMB8EKzU3kjl6FrvLdls6SChKoj97VYKL9sHE9UKF1hX7M1T3b8XIGZ9cbR36-fDYADIMa2XvOX8UM0uFyXyCNukb_j1AHWoHTcFmXIzfSJA2-WMfDrqtZeNhXTL5L6w.png)

4. El paso anterior generará archivos XML para todos los módulos en la carpeta `attachments/lang/es_ES`. Localice el módulo que desea traducir y copie los archivos al módulo de traducción en la carpeta `modules/<JAVAPACKAGE.OF.THE.MODULE>/referencedata/translation/es_ES`.
![](../../../assets/drive/ZfvOyXa64_eeQCCVz-c5tcjgrfgoQVsfqkUhnYxW6ORFoyXfXqb3fLk3yqageghTnCGzdD5EbbOaftppa2X3isDBNPXYF0PtpbW0p4ve9cmRO-FxzCWWi7vE4p5VYD2ZJ8Ojfm_wq6CiXRUkiajLxB82MviBtLrPEaWcVvbz-JaTIkIQ5750LctJGZ43Iw.png)

5. Ahora, para usar este agente es necesario iniciar sesión con el rol `System Administrator` y configurar el acceso del rol. Para ello, vaya a la ventana **Agente**, seleccione Creador de traducciones de módulos y sincronícelo. A continuación, vaya a la ventana **Acceso de agente** y conceda acceso al rol.

6. Abra Copilot y seleccione Creador de traducciones de módulos; a continuación, solicite al agente que traduzca los archivos de su módulo (por ejemplo, `/modules/<JAVAPACKAGE.OF.YOUR.MODULE>`).
![alt text](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/module-translation.png)

7. Para aplicar los cambios, ejecute estos comandos:

``` bash title="Terminal"
./gradlew install.translation -Dmodule=javapackage
./gradlew smartbuild -Dlocal=no
```
#### Creador de Referencias

El **Creador de Referencias** crea referencias en el Diccionario de Aplicación (AD) de Etendo. Esta herramienta permite, por ejemplo, añadir nuevas referencias de lista a un módulo específico dentro de la base de datos de Etendo mediante una solicitud HTTP a un webhook.

Es especialmente útil en el proceso de desarrollo, ya que permite a administradores del sistema o desarrolladores definir nuevas referencias que posteriormente pueden utilizarse en las aplicaciones. Esta herramienta automatiza la creación de estas referencias, garantizando la **consistencia y el cumplimiento** de los estándares de calidad en la configuración.

**Herramientas**

- [Herramienta de llamada a API](../available-tools/openapi-tool.md)

**Funcionalidad**

El **Creador de Referencias** está diseñado para facilitar la creación de referencias; por ejemplo, es posible crear una lista de referencias en el Diccionario de Aplicación (AD) de Etendo proporcionando al agente los parámetros de entrada necesarios.

**Ejemplo de uso** 

1. Para utilizar este agente, es necesario iniciar sesión con el rol `System Administrator` y establecer en desarrollo el módulo en el que se exportarán los cambios.

2. Abra Copilot y seleccione Creador de Referencias

    ![alt text](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/create-references-0.png)

3. Pregunte al agente qué tipo de referencia necesita crear

    ![alt text](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/create-references1.png)

4. La herramienta Crear Referencias procesará estos parámetros, verificará el token de acceso, construirá el cuerpo de la solicitud y llamará al webhook de Etendo para crear la referencia.

    En la ventana Referencia, Etendo muestra todos los campos con la información correspondiente generada y, en la solapa Referencia de lista, es posible ver la nueva referencia de lista creada. 

    ![alt text](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/create-references-2.png)


5. Una vez que el desarrollador valida el desarrollo y se realizan las modificaciones manuales necesarias, es posible exportar los cambios en el módulo correspondiente.

    ```title="Terminal"
    ./gradlew export.database --info
    ```
#### Agente de Tabla y Columna

El **Agente de Tabla y Columna** es un asistente inteligente que automatiza la creación y gestión de estructuras de base de datos dentro de la plataforma Etendo. Está diseñado específicamente para ayudar a los desarrolladores a gestionar de forma eficiente **Tabla**, **Columna** y **Vista**, garantizando que todas las operaciones sigan los estándares internos de Etendo y las reglas de consistencia de la base de datos.  

**Funcionalidad**

Este agente guía a los desarrolladores a través del proceso de creación o modificación de entidades de base de datos, validando automáticamente la información del módulo y aplicando procedimientos específicos de Etendo como el registro de tablas, la sincronización y la corrección de elementos. Utiliza la OpenAPI de Etendo y webhooks dedicados para garantizar que cada paso —como crear una tabla, añadir una columna o generar una vista— se ejecute correctamente y en la secuencia adecuada.  

Cuando se solicita, el agente:  

- Crea nuevas tablas, incluyendo todas las columnas obligatorias y los metadatos.  
- Añade, modifica o elimina columnas con los tipos de datos adecuados.  
- Valida y registra vistas dentro de la base de datos.  
- Ejecuta los procesos **TableChecker** y **SyncTerms** para garantizar la integridad y la sincronización de los datos.  
- Gestiona automáticamente los elementos relacionados y mantiene las convenciones de nomenclatura y las dependencias.  

**Herramientas**

- [Herramienta de llamada a API](../available-tools/api-call-tool.md)


**Ejemplo de uso**

1. Inicie sesión como **Administrador del Sistema** y verifique que el módulo esté configurado en **modo de desarrollo**.  
2. Abra **Copilot** y seleccione **Agente de Tabla y Columna**.  
3. Solicite al agente que cree o modifique una tabla (por ejemplo, “Cree una nueva tabla para reseñas de clientes con columnas: ID, Cliente, Valoración y Comentario”).  
4. El agente creará la tabla, añadirá las columnas especificadas, ejecutará el **TableChecker**, sincronizará los términos y finalizará la configuración.  
5. Recompile usando `./gradlew smartbuild --info` y reinicie Tomcat para aplicar los cambios.  

Este agente garantiza que todas las actualizaciones de la base de datos se realicen de forma segura, coherente y en pleno cumplimiento de los estándares de desarrollo de Etendo.
#### Agente de Ventanas, Solapas y Campos

!!!warning
    El agente de ventanas, solapas y campos se encuentra actualmente en fase de pruebas **beta**. Aunque está diseñado para automatizar el proceso de creación de **Ventana**, **Solapa** y **Campo**, hay casos en los que las tareas pueden no completarse totalmente. En concreto, puede haber problemas al añadir claves foráneas, nombrar correctamente los elementos, etc.

    Para obtener resultados óptimos, se recomienda proceder paso a paso y ser lo más específico posible en sus instrucciones al agente. Esto ayudará a mitigar posibles errores y a garantizar una finalización de tareas más precisa.

El **Agente de Ventanas, Solapas y Campos** es un asistente de desarrollo especializado para Etendo que automatiza la creación y el registro de **Ventana**, **Solapa** y **Campo** en el **Application Dictionary (AD)**. Ya no gestiona la creación de tablas o columnas, sino que se centra en la configuración y el enlace de los elementos de la interfaz de usuario dentro de Etendo.

**Funcionalidad**

Este agente agiliza el proceso de definir y registrar estructuras de interfaz interactuando directamente con la OpenAPI de Etendo. Valida los datos, recupera la información existente cuando es necesario y garantiza que todos los elementos se creen y sincronicen correctamente dentro del AD.  

Cuando se solicita, el agente puede: 

- Crear y registrar **Ventana**, verificando si ya existe una y reutilizándola cuando corresponda.  
- Añadir **Solapa** a ventanas existentes, gestionando automáticamente la jerarquía y los niveles de solapa.  
- Crear **Campo** asociados a una solapa y a su tabla subyacente.  
- Recuperar datos de **Ventana**, **Solapa** o **Tabla** existentes para dar soporte a tareas de edición o ampliación.  
- Generar automáticamente **Descripción** y **comentarios de ayuda** para todos los elementos creados, garantizando que se sigan los estándares de documentación y usabilidad de Etendo.  
- Sincronizar la terminología y actualizar los metadatos faltantes mediante los procesos **Sync Terms** y **Elements Handler**.

El agente opera mediante un flujo de trabajo guiado que incluye validación de datos, sincronización, registro de componentes y verificación de elementos, garantizando consistencia, precisión y cumplimiento de las mejores prácticas de Etendo.

**Herramientas**

- [Herramienta de llamada a API](../available-tools/api-call-tool.md)

**Ejemplo de uso** 

1. Para utilizar este agente, es necesario iniciar sesión con el rol `System Administrator` y establecer el módulo en el que se exportarán los cambios en desarrollo.

2. Abra Copilot y seleccione el Creador de Tablas, Ventanas y Solapas  
    ![dev-assistant.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/dev-assistant-1.png)

3. Solicite al asistente lo que necesita crear.  
    ![dev-assistant.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/dev-assistant5.png)

4. Con la tarea completada, es necesario recompilar con un smartbuild y reiniciar Tomcat

    ```title="Terminal"
    ./gradlew smartbuild --info
    ```
    ![dev-assistant2.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/dev-assistant2.png)

5. Ventana en el sistema: la ventana puede visualizarse con el rol de usuario.  
    ![dev-assistant3.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/dev-assistant3.png)
    ![dev-assistant4.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/dev-assistant4.png)

6. Una vez que el desarrollo es validado por el desarrollador y se realizan las modificaciones manuales necesarias, es posible exportar los cambios en el módulo correspondiente.

    ```title="Terminal"
    ./gradlew export.database --info
    ```
#### Creador de Webhooks

**Creador de Webhooks** es un agente diseñado para facilitar la creación y el registro de webhooks en Java. Un webhook actúa como un comunicador entre aplicaciones o servicios, permitiendo que los datos se envíen automáticamente de un sistema a otro en tiempo real cuando ocurre un evento específico.

**Herramientas**

- [Herramienta de llamada a API](../available-tools/openapi-tool.md)
- [Herramienta de lectura de archivos](../available-tools/read-file-tool.md)
- [Herramienta de escritura de archivos](../available-tools/write-file-tool.md)

**Funcionalidad**

Este agente simplifica la creación de webhooks generando automáticamente los archivos Java necesarios y registrándolos en el sistema Etendo ERP, tomando como ejemplo el código de indexación leyendo las clases que extienden `BaseWebhookService`. Es necesario proporcionar información útil:

- **Paquete del Módulo**: El paquete Java donde se guardará el nuevo proceso. Debe seguir el formato `java.package.of.the.module`.
- **Nombre del Webhook**: El nombre del archivo Java que se creará.
- **Parámetros**: Los parámetros se añadirán al webhook para su uso.

**Ejemplo de uso**

1. Para utilizar este agente, es necesario iniciar sesión con el rol `System Administrator` y configurar el acceso del rol. Para ello, vaya a la ventana **Agente**, seleccione Creador de Webhooks y sincronícelo. Luego, vaya a la ventana **Acceso de agente** y conceda acceso al rol.

2. Abra Copilot y seleccione Creador de Webhooks; a continuación, solicite al agente lo que necesita crear.

	![webhook.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/wh-1.png)

3. A continuación, este es el resultado proporcionado por el agente.

    ![webhook.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/wh-2.png)

    ![webhook.png](../../../assets/developer-guide/etendo-copilot/bundles/dev-assistant/wh-3.png)
### Supervisor de pruebas
Un supervisor que permite generar pruebas para un Módulo de Etendo completo mediante un flujo de trabajo, comprobando los archivos sin pruebas y generándolas. El supervisor también ejecutará las pruebas y proporcionará feedback al usuario.

**Funcionalidad**

Este agente recibe un Módulo de Etendo y comprobará los archivos Java y JavaScript, determinando cuáles tienen pruebas y cuáles no.

- El agente generará un informe con los resultados y sugerirá al usuario generar pruebas para los archivos que no las tengan.
- El agente generará las pruebas de Java y React.

**Miembros del equipo**

#### Java Test Checker

    Este agente, al recibir un Módulo de Etendo, comprobará los archivos Java, determinando cuáles tienen pruebas y cuáles no. El agente generará un informe con los resultados y sugerirá al usuario generar pruebas para los archivos que no las tengan.

    !!!info
        Este agente está pensado y diseñado para usarse como parte de un supervisor de tipo Langgraph; puede utilizarse de forma individual, pero no dispone de funcionalidad completa.

    **Herramientas**

    - [Herramienta de impresión de directorio](../available-tools/print-directory-tool.md)

#### Java Test Executor

    Este agente está diseñado para ejecutar pruebas para un Paquete Java; puede utilizarse para ejecutar:

    - Todas las pruebas.
    - Pruebas de un módulo.
    - Pruebas de un único archivo Java.

    Esto depende de la entrada del usuario. El agente ejecutará las pruebas y proporcionará feedback al usuario.

    !!!info
        Este agente está pensado y diseñado para usarse como parte de un supervisor de tipo Langgraph; puede utilizarse de forma individual, pero no dispone de funcionalidad completa.

    **Herramientas** 

    - [Herramienta de ejecución de pruebas](../available-tools/test-run-tool.md)

#### Java Test Generator

    Este agente genera pruebas para un único archivo Java. Lee el archivo Java y crea un archivo de prueba con el mismo nombre y el sufijo `Test` en el mismo paquete. El agente genera métodos de prueba para cada método del archivo Java. El agente dispone de una base de conocimiento con las clases Java de Etendo Classic.
    Este agente generará las pruebas y las ejecutará, comprobando errores y proporcionando feedback al usuario.

    !!!info
        Este agente está pensado y diseñado para usarse como parte de un supervisor de tipo Langgraph; puede utilizarse de forma individual, pero no dispone de funcionalidad completa.

    **Herramientas**

    - [Herramienta de lectura de archivos](../available-tools/read-file-tool.md)
    - [Herramienta de escritura de archivos](../available-tools/write-file-tool.md)
    - [Herramienta de ejecución de pruebas](../available-tools/test-run-tool.md)


#### Agente de pruebas de React

    El **Agente de pruebas de React** es un agente especializado en crear y gestionar pruebas de componentes React usando `TypeScript` y `@testing-library/react-native`. Su enfoque principal es generar archivos de prueba de alta calidad para componentes React y React Native dentro de módulos de **subaplicación de Etendo**.

    Detecta componentes React (archivos `.tsx` o `.jsx`) que no tienen archivos de prueba correspondientes en el directorio `__tests__`. Analiza la estructura del componente, las props y las dependencias, genera archivos de prueba con Jest y React Testing Library, y cubre escenarios clave como renderizado, interacciones de usuario, cambios de estado y casos límite.

    !!!info
        Este agente está diseñado para usarse dentro del ecosistema de Etendo como parte de un agente LangGraph **Supervisor de pruebas**. No obstante, puede utilizarse de forma independiente con funcionalidad limitada.

    **Herramientas**

    - [Herramienta de lectura de archivos](../available-tools/read-file-tool.md)
    - [Herramienta de escritura de archivos](../available-tools/write-file-tool.md)


**Ejemplo de uso**

1. Para utilizar este agente, es necesario iniciar sesión con el rol `System Administrator` y configurar el acceso del rol. Para ello, vaya a la ventana **Agente**, seleccione `Test Supervisor` y sincronícelo. A continuación, vaya a la ventana **Acceso de agente** y conceda acceso al rol.

2. Abra Copilot y seleccione `Test Supervisor`; a continuación, solicite al agente lo que necesite crear. Una entrada sugerida podría ser `Generate tests for the module com.etendoerp.examplemodule`.

3. El agente generará las pruebas y las ejecutará, comprobando errores y proporcionando feedback al usuario.
### Agente de refactorización

Un agente experto en refactorización de código centrado en mejorar la claridad, el mantenimiento y la originalidad, preservando la funcionalidad. El agente analiza archivos de código, identifica áreas de mejora y sugiere cambios en nombres de variables, documentación y estructuras para una mejor legibilidad. Garantiza que las importaciones, los nombres de métodos y los nombres de entidades permanezcan sin cambios para mantener la funcionalidad. El flujo de trabajo incluye análisis de código, confirmación del usuario, aplicación de cambios y verificación de las actualizaciones. Se proporcionan explicaciones claras y un resumen de los cambios para la comprensión del usuario.

**Funcionalidad**

- El agente de refactorización recibe una ruta de archivo.
- El agente leerá el archivo.
- El agente puede consultar la base de conocimientos para obtener sugerencias.
- El agente escribirá el archivo con los cambios, sobrescribiendo el archivo original.
- El agente leerá el archivo de nuevo para verificar los cambios.

**Herramientas**

- [Herramienta de lectura de archivos](../available-tools/read-file-tool.md)
- [Herramienta de escritura de archivos](../available-tools/write-file-tool.md)

**Ejemplo de uso**

1. Para utilizar este agente, es necesario iniciar sesión con el rol `System Administrator` y configurar el acceso del rol. Para ello, vaya a la ventana **Agente**, seleccione Agente de refactorización y sincronícelo. A continuación, vaya a la ventana **Acceso del agente** y conceda acceso al rol.
2. Abra Copilot y seleccione Agente de refactorización; después, solicite al agente lo que necesita refactorizar. Por ejemplo, una entrada sugerida podría ser `Refactor the file located in the path /modules/com.etendoerp.module/src/com/etendoerp/module/MyClass.java changing the variables to spanish`.
3. El agente leerá el archivo, lo analizará y sugerirá cambios.
4. El agente escribirá el archivo con los cambios, sobrescribiendo el archivo original.
### Agente de prueba Java único

Este agente está diseñado para generar pruebas para un único archivo Java o para un módulo de Etendo Classic.

**Funcionalidad**

- Este agente recibe una ruta de archivo Java o una ruta de módulo, pero su funcionalidad principal es generar pruebas para un único archivo Java.
- En el caso de un Módulo proporcionado, el agente comprobará los archivos sin pruebas y las generará para ellos.
- El comportamiento esperado del agente es leer el archivo Java y generar un archivo de prueba con el mismo nombre y el sufijo `Test` en el mismo paquete.
- El agente también generará los métodos de prueba para cada método del Java.
- Este agente dispone de una Base de Conocimiento con las clases Java de Etendo Classic.

**Herramientas**

- [Herramienta de impresión de directorio](../available-tools/print-directory-tool.md)
- [Herramienta de lectura de archivos](../available-tools/read-file-tool.md)
- [Herramienta de escritura de archivos](../available-tools/write-file-tool.md)

!!!warning Descargo de responsabilidad
    Los generadores de pruebas proporcionados por esta herramienta están diseñados para ofrecer de forma eficiente un lote inicial de casos de prueba, en función de los parámetros proporcionados. Sin embargo, es importante tener en cuenta que las pruebas generadas sirven como punto de partida y pueden requerir trabajo adicional para:

    - Corregir posibles errores en los casos de prueba generados.
    - Mejorar la cobertura de pruebas.
    - Adaptarlas a los escenarios específicos de su proyecto o entorno.

    Recomendamos revisar cuidadosamente las pruebas generadas, ejecutarlas en el entorno de desarrollo y realizar los ajustes necesarios para garantizar que cumplen los requisitos funcionales y de calidad esperados.

**Ejemplo de uso**

1. Para utilizar este agente, es necesario iniciar sesión con el rol `System Administrator` y configurar el acceso del rol. Para ello, vaya a la ventana **Agente**, seleccione Generador de pruebas Java y sincronícelo. A continuación, vaya a la ventana **Acceso de agente** y conceda acceso al rol.
2. Abra Copilot y seleccione Agente de prueba Java único; a continuación, solicite al agente lo que necesita crear. Una entrada sugerida podría ser ```Generar pruebas para el archivo Java ubicado en la ruta /modules/com.etendoerp.module/src/com/etendoerp/module/MyClass.java```.
3. El agente generará las pruebas y las ejecutará, comprobando si hay errores y proporcionando comentarios al usuario.
### Inicializador de Entidad/Organización

Este agente ayuda al usuario a inicializar entidades u organizaciones. 

**Funcionalidad**

- Recopilar de forma interactiva toda la información requerida para crear una nueva entidad u organización.  
- Ejecutar la creación de la entidad u organización y validar automáticamente que se ha completado correctamente.  
- Después de crear una **entidad**:  
    - Indicar al usuario que inicie sesión utilizando las credenciales del administrador de la entidad recién creada.  
    - Solicitar al usuario que configure el acceso de este asistente para la entidad.  
    - Solicitar la creación de organizaciones bajo esa entidad.  
- Después de crear una **organización**:  
    - Indicar al usuario que inicie sesión con las credenciales del administrador para continuar configurando la organización.  
- Gestionar fallos de inicialización indicando al usuario que verifique:  
    - Que está utilizando el rol y la organización correctos.  
    - Sus permisos actuales (solo un Administrador del Sistema puede crear entidades; un Administrador de Entidad solo puede crear organizaciones).  
- Inferir automáticamente el host y las credenciales del usuario a partir del contexto de la sesión, evitando solicitudes explícitas de estos detalles.    

**Herramientas**

- [Herramienta de configuración inicial de la organización](../available-tools/org-init-tool.md)
- [Configuración inicial de la entidad](../available-tools/client-init-tool.md)

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.