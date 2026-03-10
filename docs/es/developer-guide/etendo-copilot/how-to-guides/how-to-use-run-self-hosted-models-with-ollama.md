---
tags:
    - Cómo hacer
    - Modelo
    - Copilot
    - Ollama
---

# Cómo ejecutar modelos autoalojados con Ollama

## Visión general

Este artículo explica cómo ejecutar y utilizar modelos autoalojados con Ollama en Copilot. Copilot utiliza por defecto modelos LLM alojados por proveedores cloud. Sin embargo, puede utilizar sus propios modelos alojándolos en sus propios servidores. Esto puede ser útil por motivos de privacidad o para utilizar modelos que no están disponibles en OpenAI. Ollama permite ejecutar modelos autoalojados en un contenedor Docker.

### Ejecutar Ollama como un contenedor Docker.
Copilot incluye un archivo Docker Compose que permite ejecutar Ollama con las tareas de Gradle del módulo Docker. Para ver más información sobre el módulo Docker, visite la documentación de [Gestión de Docker](../../etendo-classic/bundles/platform/docker-management.md).

Para habilitar el archivo compose para Ollama, es necesario añadir la siguiente línea en el archivo `gradle.properties`:

```groovy title="gradle.properties"
docker_com.etendoerp.copilot.ollama=true
```

Después de eso, puede ejecutar el siguiente comando para iniciar el contenedor de Ollama:

```bash title="Terminal"
./gradlew resources.up --info
```

### Instalar un modelo

Los [modelos disponibles en Ollama](https://ollama.com/search){target=_isblank} deben instalarse para poder utilizarse. Esto se realiza solo una vez porque la configuración del contenedor permite que los modelos se persistan, por lo que reiniciar el contenedor no afectará a la disponibilidad de los modelos una vez instalados.

Para instalar los modelos, es necesario entrar en el contenedor de Ollama y ejecutar el siguiente comando:

```bash title="Terminal"
docker exec -it etendo-ollama-1 bash
```

Esto abrirá una shell dentro del contenedor. Una vez dentro del contenedor, puede instalar el modelo usando el siguiente comando (por ejemplo, para instalar el modelo llama3.2:3b):

```bash title="Docker Terminal"
ollama run llama3.2:3b
```

Después de instalar el modelo, debe crear un registro en la ventana [Modelo de IA](../../../user-guide/etendo-copilot/setup-and-usage.md#ai-models-window) en Copilot, con la siguiente información:

- Proveedor: "ollama"
- Modelo: "llama3.2:3b"

### Usar el modelo en Copilot
- Finalmente, puede usar el modelo en Copilot seleccionando el registro creado en el selector de modelos en la ventana [Agente](../../../user-guide/etendo-copilot/setup-and-usage.md#agent-window).

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.