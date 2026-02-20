---
tags:
    - How to
    - Exportar Agente
    - Distribuir Agente
    - Copilot
    - Conjuntos de datos
    - Exportar Herramienta
    - Distribuir Herramienta
---

# Cómo exportar herramientas y agentes

## Visión general

Al desarrollar en Etendo Copilot, es posible exportar agentes y herramientas. Esta documentación detalla cómo exportarlos y cómo asegurarse de que, al instalar el módulo, las configuraciones estén listas para usar, permitiendo un proceso **listo para usar**.

## Exportación de agentes

Existen dos métodos principales para exportar agentes: exportarlos como un conjunto de datos donde los agentes configurados se exportan dentro de un conjunto de datos de Etendo Classic, o exportarlos como Administrador del Sistema, donde el/los agente(s) definidos con el rol Administrador del Sistema se exportan directamente junto con el módulo.

### Exportación de agentes como conjuntos de datos

Los agentes deben exportarse como un conjunto de datos, en caso de que se requiera una instalación opcional y con nivel de acceso a datos `Cliente/Organización`.

1. Configuración inicial del agente:
    - Configure el agente y las herramientas en el entorno donde se realiza el desarrollo.
    - Asegúrese de incluir todos los campos necesarios para exportar. Asegúrese de configurar correctamente las solapas **Base de Conocimiento**, **Habilidades/Herramientas** y **Miembros del Equipo**, así como los registros en la ventana **Archivo de la Base de Conocimiento**.

    
    <figure markdown="span">
    ![](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-export-tools-and-assistants/exportcopilot1.png)
  <figcaption>Ejemplo de agente con solapas completas.</figcaption>
</figure>

2. Crear y configurar un Conjunto de datos:
    - Como Administrador del Sistema, vaya a la ventana **Conjunto de datos** y cree un nuevo registro seleccionando el módulo en desarrollo.
    - Defina el **Identificador** y el **Nombre** del conjunto de datos.
    - Establezca el **Acceso datos** en **Sistema/Organización** (recomendado para agentes de usuario).

3. Añadir tablas al Conjunto de datos

    Para cada ventana o solapa a exportar, cree un registro en la solapa **Tabla**. Especifique la tabla correspondiente y añada la cláusula **HQL/SQL Where** adecuada.

    - **Agente:** Tabla `etcop_app` 
    ```sql title="Where Clause"
    id in ('<AssistantID>')
    ```
    - **Base de Conocimiento:** Tabla `etcop_app_source`
    ```sql title="Where Clause"
    etcopApp.id in ('<AssistantID>')
    ```
    - **Habilidades/Herramientas:** Tabla `etcop_app_tool`
    ```sql title="Where Clause"
    `copilotApp.id in ('<AssistantID>')
    ```
    - **Miembros del Equipo:** Tabla `ETCOP_Team_Member`
    ```sql title="Where Clause"
    copilotApp.id in ('<AssistantID>')
    ```
    - **Archivo de la Base de Conocimiento:** Tabla `etcop_file`
    ```sql title="Where Clause"
    id in ('<knowladgeBaseFileID>')
    ```
    
    <figure markdown="span">
    ![](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-export-tools-and-assistants/exportcopilot2.png)
    <figcaption>Ejemplo de configuración de la ventana Conjunto de datos en el módulo Copilot Purchase Expert</figcaption>
    </figure>

4. Botón Exportar Datos de Referencia
    - Ejecute el proceso **Exportar Datos de Referencia**, que creará la carpeta `referencedata/` dentro del módulo seleccionado, con todos los registros que se exportaron según la configuración del conjunto de datos. 

    !!!note
        Verifique que todos los registros requeridos se generen en el archivo `.XML`.


5. Incluir datos de referencia en el módulo
    - Marque la casilla **Incluir datos de referencia** en la definición del módulo y añada una descripción al conjunto de datos haciendo referencia al agente exportado.

    <figure markdown="span">
    ![](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-export-tools-and-assistants/exportcopilot3.png)
    <figcaption>Ejemplo de configuración en el módulo Copilot Purchase Expert</figcaption>
    </figure>

    - Cuando se instale el módulo, el conjunto de datos estará disponible para su aplicación en la ventana **Gestión del módulo de Empresa**.

    <figure markdown="span">
    ![](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-export-tools-and-assistants/exportcopilot4.png)
    <figcaption>Ejemplo de conjuntos de datos distribuidos</figcaption>
    </figure>


### Exportación de agentes como Administrador del Sistema

Al exportar agentes que deben estar preconfigurados en una instalación de módulo, deben crearse con el rol Administrador del Sistema. Estos agentes solo serán editables por el Administrador del Sistema, pero pueden ejecutarse tanto por el `Administrador del Sistema` como por usuarios con niveles de acceso a datos `Cliente/Organización`.

1. Crear agente con rol Administrador del Sistema:

    - Inicie sesión como Administrador del Sistema.
    - Configure el agente y sus solapas, asegurándose de seleccionar el módulo (en desarrollo) en el campo **Módulo**.
    - Si el agente debe restringirse para uso exclusivo del Administrador del Sistema, marque la casilla **Aplicación del Sistema**. En caso contrario, déjela sin marcar para permitir la ejecución en todos los niveles de acceso a datos.

    <figure markdown="span">
    ![](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-export-tools-and-assistants/exportcopilot5.png)
    <figcaption>Ejemplo de agente exportado y disponible solo como Administrador del Sistema</figcaption>
    </figure>

2. **Exportar la base de datos**.
    - Ejecute el comando `./gradlew export.database` para exportar el agente junto con el módulo.

## Exportación de herramientas

**Configuración de la herramienta**: al definir una herramienta, seleccione el módulo (en desarrollo) en el campo **Módulo**, y ejecute el comando `./gradlew export.database` para exportar la herramienta junto con el módulo.

<figure markdown="span">
![](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-export-tools-and-assistants/exportcopilot6.png)
<figcaption>Ejemplo de configuración de herramienta</figcaption>
</figure>

!!!info
    Para más información, visite [Cómo crear una herramienta de Copilot](../how-to-guides/how-to-create-copilot-tools.md).

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.