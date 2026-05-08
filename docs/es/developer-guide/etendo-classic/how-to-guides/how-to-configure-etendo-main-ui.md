---
tags:
  - How to
  - Etendo Classic
  - Main UI
  - Docker
  - Configuration
---

# Cómo Configurar la Main UI de Etendo { #how-to-configure-etendo-main-ui }

## Descripción General { #overview }

La Main UI de Etendo es una interfaz de usuario moderna basada en React/TypeScript incluida en la instalación base de Etendo. Se ejecuta como un servicio Docker contenerizado junto a la instancia de Etendo y se inicia automáticamente con `./gradlew resources.up`.

Esta guía cubre la configuración manual de las variables de la Main UI y la configuración avanzada de desarrollo para contribuidores.

## Requisitos { #requirements }

- Proyecto de Etendo correctamente configurado. Consulte las guías de [Desarrollo Local](../getting-started/installation/local-development.md) o [Instalación en Servidor](../getting-started/installation/production-server.md).
- [Docker](https://docs.docker.com/get-docker/){target="_blank"} versión `26.0.0` o superior
- [Docker Compose](https://docs.docker.com/compose/install/){target="_blank"} versión `2.26.0` o superior

!!! warning
    Evite instalar Docker mediante [Snap](https://snapcraft.io){target="_blank"} — sus restricciones de sandbox pueden impedir que los contenedores Docker de Etendo accedan correctamente a los directorios del host. Instale Docker siguiendo la guía oficial para su distribución.

!!! info
    El módulo [Docker Management](../bundles/platform/docker-management.md), incluido como dependencia, gestiona la distribución de infraestructura dentro de los módulos de Etendo mediante contenedores Docker.

## Token de Acceso de Entidad { #client-access-token }

:material-menu: `Aplicación` > `Configuración General` > `Entidad` > `Entidad`

Se debe configurar un token de cifrado de un solo uso para la autenticación. Este token es necesario para que la Main UI inicie una sesión.

1. Acceda a Etendo Classic como `System Administrator`.
2. Navegue a `Entidad` > pestaña `Secure Web Service Configuration`.
3. Haga clic en **Generar Clave** para crear un token. El tiempo de expiración está en minutos; establézcalo en `0` para que no expire.

![Client Access Token](../../../assets/developer-guide/etendo-mobile/getting-started/token.png)

!!! info
    Este token no requiere ninguna acción adicional — solo necesita ser generado para que el proceso de autenticación funcione correctamente.

## Configuración { #configuration }

### Usando la Configuración Interactiva { #using-the-interactive-setup }

Ejecute el asistente de configuración interactivo para establecer todas las variables requeridas:

```bash title="Terminal"
./gradlew setup -Pinteractive=true --console=plain
```

Para un recorrido completo, consulte la guía [Cómo Usar la Configuración Interactiva](./how-to-use-interactive-setup.md).

Luego inicie los servicios Docker:

```bash title="Terminal"
./gradlew resources.up
```

### Configuración Manual { #manual-configuration }

Agregue las siguientes variables a `gradle.properties`:

```groovy title="gradle.properties"
docker_com.etendoerp.mainui=true
etendo.classic.url=http://host.docker.internal:8080/etendo
etendo.classic.host=http://localhost:8080/etendo
authentication.class=com.etendoerp.etendorx.auth.SWSAuthenticationManager
ws.maxInactiveInterval=3600
next.public.app.url=http://localhost:3000
```

| Variable | Descripción | Local | Producción |
|---|---|---|---|
| `docker_com.etendoerp.mainui` | Habilita el servicio Docker de la Main UI. | `true` | `true` |
| `etendo.classic.url` | URL del backend utilizada por el servidor de la Main UI para conectarse a Etendo Classic. Use `host.docker.internal` cuando la Main UI se ejecuta en Docker y Tomcat se ejecuta localmente. | `http://host.docker.internal:8080/etendo` | `https://your.backend.etendo.cloud/etendo` |
| `etendo.classic.host` | URL del lado del cliente que el navegador utiliza para realizar solicitudes directas a Etendo Classic. | `http://localhost:8080/etendo` | `https://your-domain.com/etendo` |
| `authentication.class` | Clase Java que gestiona la autenticación entre la Main UI y Etendo Classic. | `com.etendoerp.etendorx.auth.SWSAuthenticationManager` | `com.etendoerp.etendorx.auth.SWSAuthenticationManager` |
| `ws.maxInactiveInterval` | Duración de la sesión en segundos para la conexión WebSocket de la Main UI. No afecta el tiempo de espera de sesión de Etendo Classic. | `3600` | `3600` |
| `next.public.app.url` | URL pública desde la que los usuarios acceden a la Main UI. | `http://localhost:3000` | `https://your.frontend.etendo.cloud` |

Aplique la configuración e inicie los servicios:

```bash title="Terminal"
./gradlew setup
./gradlew resources.up
```

## Acceder a la Main UI { #access-the-main-ui }

Una vez que todos los servicios estén en ejecución, la Main UI está disponible en:

| Entorno | URL |
|---|---|
| **Local** | [http://localhost:3000](http://localhost:3000){target="_blank"} |
| **Producción** | `https://<server-address>/` |

## Configuración Avanzada { #advanced-configuration }

Esta sección es para desarrolladores que desean contribuir o personalizar directamente el código fuente de la Main UI.

### Requisitos Adicionales { #additional-requirements }

- **Node.js** versión `^18.0.0` o superior
- **pnpm** versión `^9.15.2`

### Módulos Requeridos { #required-modules }

Instale los siguientes módulos en el directorio `modules/`:

```bash title="Terminal"
cd modules
git clone git@github.com:etendosoftware/com.etendoerp.etendorx.git
git clone git@github.com:etendosoftware/com.etendoerp.openapi.git
git clone git@github.com:etendosoftware/com.etendoerp.metadata.git
git clone git@github.com:etendosoftware/com.etendoerp.metadata.template.git
```

### Estructura del Proyecto { #project-structure }

```
com.etendorx.workspace-ui/
├── packages/
│   ├── api-client/          # Cliente API para la comunicación con el backend
│   ├── ComponentLibrary/    # Componentes de UI reutilizables
│   └── MainUI/              # Aplicación principal
├── package.json
├── pnpm-workspace.yaml
└── README.md
```

### Configuración del Entorno de Desarrollo { #development-setup }

1. Clone el repositorio de desarrollo de la Main UI:

    ```bash title="Terminal"
    git clone https://github.com/etendosoftware/com.etendorx.workspace-ui.git
    cd com.etendorx.workspace-ui
    ```

2. Instale las dependencias:

    ```bash title="Terminal"
    pnpm install
    ```

3. Cree `packages/MainUI/.env.local` y agregue la URL del backend:

    ```env title=".env.local"
    ETENDO_CLASSIC_URL=http://localhost:8080/etendo
    ```

4. Compile los paquetes requeridos en orden:

    ```bash title="Terminal"
    pnpm --filter @workspaceui/api-client build
    pnpm --filter @workspaceui/componentlibrary build
    ```

5. Inicie el servidor de desarrollo:

    ```bash title="Terminal"
    pnpm dev
    ```

    La aplicación está disponible en [http://localhost:3000](http://localhost:3000){target="_blank"}.

### Comandos de Desarrollo { #development-commands }

**Comandos a nivel raíz:**

```bash title="Terminal"
pnpm dev          # Iniciar el servidor de desarrollo de la Main UI
pnpm build        # Compilar todos los paquetes
pnpm test         # Ejecutar pruebas en todos los paquetes
pnpm lint         # Verificar el estilo de código en todos los paquetes
pnpm lint:fix     # Corregir automáticamente los problemas de estilo de código
pnpm format       # Formatear el código en todos los paquetes
pnpm format:fix   # Corregir automáticamente los problemas de formato
pnpm clean        # Limpiar todos los artefactos de compilación
```

**Comandos por paquete:**

```bash title="Terminal"
pnpm --filter @workspaceui/mainui dev
pnpm --filter @workspaceui/api-client build
pnpm --filter @workspaceui/componentlibrary build
pnpm --filter @workspaceui/api-client test
pnpm --filter @workspaceui/mainui lint
```

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.
