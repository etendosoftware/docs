---
tags:
    - Copilot
    - Docker
    - Ejecución de código
    - Python
    - Bash
---

# Herramienta Docker

:octicons-package-16: Javapackage: `com.etendoerp.copilot.toolpack`

## Visión general

La **DockerTool** es una herramienta que gestiona contenedores Docker para ejecutar código Python o Bash. Permite a los usuarios ejecutar comandos aislados, copiar archivos en contenedores y limpiar los contenedores automáticamente tras un periodo de inactividad.

!!!info
    Para incluir esta funcionalidad, debe estar instalado el Copilot Extensions Bundle. Para obtener instrucciones, visite el marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. Para obtener detalles sobre versiones, compatibilidad con el core y nuevas funcionalidades, consulte [Copilot Extensions - Notas de la versión](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

## Funcionalidad

Esta herramienta facilita la **ejecución de código en entornos Docker aislados**, dando soporte a flujos de trabajo de desarrollo, automatización y tareas del sistema. Las funcionalidades principales incluyen:

### Parámetros

- **Executor**: El tipo de ejecutor para el código (`python` o `bash`).
- **Código**: El código que se ejecutará dentro del contenedor.
- **Archivos a copiar**: Una lista opcional de rutas de archivo para copiar dentro del contenedor para su ejecución.

### Flujo de ejecución

1. **Creación del contenedor**:
    - Se crea un contenedor Docker si aún no existe.
    - Los contenedores se nombran usando el formato `tempenv-copilot-{conversation_id}` para trazabilidad.

2. **Transferencia de archivos**:
    - Los archivos especificados en el parámetro `Archivos a copiar` se suben al contenedor en las rutas indicadas.

3. **Ejecución de comandos**:
    - La herramienta ejecuta el código Python o Bash especificado.
    - La salida se captura y se devuelve al usuario.

4. **Limpieza del contenedor**:
    - Los contenedores se eliminan automáticamente tras 1 hora de inactividad.


## Ejemplo de uso

- **Entrada de ejemplo**

```json
{
    "executor": "bash",
    "code": "ping -c 4 google.com",
    "files_to_copy": []
}
```

- **Salida de ejemplo**

```json
{
    "message": "PING google.com (172.217.12.206): 56 data bytes\n64 bytes from 172.217.12.206: icmp_seq=0 ttl=115 time=12.5 ms\n64 bytes from 172.217.12.206: icmp_seq=1 ttl=115 time=12.3 ms\n64 bytes from 172.217.12.206: icmp_seq=2 ttl=115 time=12.4 ms\n64 bytes from 172.217.12.206: icmp_seq=3 ttl=115 time=12.6 ms\n\n--- google.com ping statistics ---\n4 packets transmitted, 4 packets received, 0.0% packet loss\nround-trip min/avg/max/stddev = 12.3/12.5/12.6/0.1 ms"
}
```

!!!info
    Esta herramienta utiliza la imagen Docker oficial **Python 3.10-slim** para la ejecución y puede ejecutar tanto comandos Python como Bash.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.