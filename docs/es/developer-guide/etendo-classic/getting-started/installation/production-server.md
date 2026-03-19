---
tags:
  - Primeros pasos
  - Instalación
  - Servidor
  - Producción
  - ISO
---

# Instalar Etendo - Instalación en servidor

## Visión general

Esta guía cubre la instalación de Etendo en un servidor de producción utilizando la **ISO de Etendo**, que automatiza la configuración del sistema operativo y la configuración del entorno base. Copilot y la Interfaz principal (Main UI) se incluyen en la instalación base y se configuran como parte de este proceso.

## Requisitos previos

- [Credenciales de GitHub](use-of-repositories-in-etendo.md)
- **Clave de API de OpenAI** — necesaria para Copilot. Usa tu propia clave de [OpenAI](https://platform.openai.com/account/api-keys){target="_blank"} o contacta con [Etendo](https://etendo.software){target="_blank"} para obtener una. Para más detalles sobre proveedores compatibles, consulta la [guía de instalación de Copilot](../../../etendo-copilot/installation.md#configuration-variables).

!!! info
    La ISO configura automáticamente el stack completo (SO, PostgreSQL, Docker, Tomcat). No se requiere ninguna configuración adicional del sistema.

## Instalación

### 1. Descargar la ISO

Descarga la última ISO de Etendo desde la página [Etendo ISO - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/iso.md).

### 2. Aprovisionar el servidor

Cómo uses la ISO depende de tu infraestructura:

- **Bare metal / servidor físico**: graba la ISO en una unidad USB usando [balenaEtcher](https://etcher.balena.io/#download-etcher){target="_blank"} (Linux/macOS) o [Rufus](https://rufus.ie/en/){target="_blank"} (Windows), y luego arranca desde el USB.
- **AWS**: se publica una AMI oficial de Etendo junto con cada versión de la ISO. Encuentra el ID de la AMI en la página [Etendo ISO - Notas de la versión](../../../../whats-new/release-notes/etendo-classic/iso.md) y luego [lanza una nueva instancia EC2 a partir de ella](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.html){target="_blank"}.
- **Hetzner Cloud**: sube la ISO como una imagen personalizada desde la consola de Hetzner Cloud y crea un nuevo servidor a partir de ella. Consulta la [documentación de Hetzner](https://docs.hetzner.com){target="_blank"} para más detalles.
- **Scaleway**: sube la ISO y utiliza los [modos de arranque personalizados](https://www.scaleway.com/en/docs/instances/how-to/use-boot-modes/){target="_blank"} para aprovisionar una instancia a partir de ella.
- **Otros proveedores cloud**: sube la ISO como una imagen personalizada y crea una nueva instancia a partir de ella. Consulta la documentación de tu proveedor para importar imágenes de SO personalizadas.
- **Máquina virtual**: monta la ISO directamente en tu hipervisor. Se recomiendan [Qemu](https://www.qemu.org/download/){target="_blank"} con [Virt-Manager (Linux)](https://virt-manager.org/download.html){target="_blank"} o [UTM (macOS)](https://mac.getutm.app/){target="_blank"}.

### 3. Arrancar e instalar el SO

Inicia el sistema desde la ISO. Sigue las indicaciones:

- **Conexiones de red**: verifica que se asigna correctamente una dirección IP y que hay acceso a internet.
- **Configuración de almacenamiento**: selecciona el disco de destino.
- **Configuración del perfil**: introduce tu nombre, el nombre del servidor y una contraseña para el usuario `etendo`.

Espera a que finalicen la instalación del sistema operativo y la actualización del servidor. Cuando se solicite, selecciona **Reiniciar ahora**.

Tras el reinicio, la configuración final del servidor se ejecuta automáticamente. Espera a que termine: el entorno base quedará listo.

!!! info "Instalación sin conexión a internet"
    Si no hay conexión a internet disponible durante la instalación, selecciona **Continuar sin internet** en el paso de configuración de red. Tras la instalación del SO y el reinicio, configura la red, conéctate a internet, inicia sesión como superusuario (`sudo su`) y ejecuta `etendo-install`.

### 4. Añadir credenciales de GitHub

Una vez que el servidor esté listo, ve al directorio del proyecto y añade tus credenciales de GitHub en `gradle.properties`. Para generarlas, sigue la guía [Uso de repositorios en Etendo](use-of-repositories-in-etendo.md).

```bash title="Terminal"
cd /opt/EtendoERP
```

```groovy title="gradle.properties"
githubUser=<username>
githubToken=<*******>
```

### 5. Aplicar la plantilla de servidor

Ejecuta la siguiente tarea para configurar todas las variables necesarias para el entorno de servidor:

```bash title="Terminal"
./gradlew setup.applyTemplates --template=server
```

Cuando se solicite, proporciona:

- **URL de Etendo ERP** — la URL completa de tu instalación (p. ej., `http://myserver.com/etendo`). El nombre de contexto y el host se derivan automáticamente.
- **Clave de API de OpenAI** — tu clave para la integración de Copilot (la entrada se enmascara).

!!! info "Disponibilidad"
    `setup.applyTemplates` está disponible a partir de **Etendo 26**, o en versiones anteriores con el [Etendo Gradle Plugin 3.0.0](../../../../whats-new/release-notes/etendo-classic/plugins/etendo-gradle-plugin/release-notes.md) o superior.

!!! info
    Para más detalles sobre plantillas disponibles, opciones y uso avanzado, consulta la guía [Cómo usar Setup Apply Templates](../../how-to-guides/how-to-use-setup-apply-templates.md).

!!! tip "Alternativa: configuración manual"
    Configura las variables directamente en `gradle.properties` y aplícalas ejecutando:
    ```bash
    ./gradlew setup --info
    ```

!!! tip "Alternativa: configuración interactiva"
    Para una configuración totalmente guiada, propiedad por propiedad, ejecuta la configuración interactiva:
    ```bash
    ./gradlew setup -Pinteractive=true --console=plain
    ```
    Para más detalles, consulta la guía [Cómo usar la configuración interactiva](../../how-to-guides/how-to-use-interactive-setup.md).

### 6. Compilar y desplegar

```bash title="Terminal"
./gradlew install smartbuild --info
```

### 7. Configurar Apache

Desde el directorio `/opt/EtendoERP`, ejecuta el script de configuración de Apache:

```bash title="Terminal"
cd utils
sudo ./apache-config.sh <domain>
```

Esto configura Apache como un proxy inverso para el servidor. Una vez completado, las URLs de la Interfaz principal (Main UI) y la Interfaz clásica (Classic UI) se establecen automáticamente en función del dominio proporcionado.

### 8. Iniciar servicios Docker

```bash title="Terminal"
./gradlew resources.up
```

Esto inicia los contenedores de **Copilot** y de la **Interfaz principal (Main UI)**.

### 9. Iniciar Tomcat

```bash title="Terminal"
sudo /etc/init.d/tomcat start
```

## Acceder a la instalación

Una vez que todos los servicios estén en ejecución:

| Interfaz | URL |
|---|---|
| **Interfaz principal (Main UI)** | `https://<server-address>/` |
| **Interfaz clásica (Classic UI)** | `https://<server-address>/<context-name>` |

!!! tip "Credenciales por defecto"
    Usuario: `admin`
    Contraseña: `admin`

    Cambia la contraseña por defecto inmediatamente después del primer inicio de sesión en un entorno de producción.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.