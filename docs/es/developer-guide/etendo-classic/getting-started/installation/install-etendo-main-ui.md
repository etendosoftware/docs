---
title: Instalar Etendo Main UI
tags:
  - Desarrollo
  - Instalación
  - Main UI
  - Docker
  - Etendo
  - Nueva UI
  - Instalar Nueva UI
status: beta
---

# Instalar Etendo Main UI

## Visión general

!!! example " **IMPORTANTE: ESTA ES UNA VERSIÓN BETA**"
    - Está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**, especialmente en entornos de producción.
    - Debe utilizarse con **precaución**, y siempre debe **validar las copias de seguridad** antes de ejecutar cualquier operación crítica.

Esta guía proporciona instrucciones para instalar y ejecutar Etendo Main UI, una interfaz de usuario moderna basada en React/TypeScript que ofrece una nueva experiencia de frontend para Etendo. La Main UI se ejecuta como un servicio en contenedor junto con su instancia de Etendo.

## Requisitos

1. Proyecto **Etendo** configurado correctamente.
2. Este proyecto depende de las siguientes herramientas:

    - [Docker](https://docs.docker.com/get-docker/){target="_blank"}: versión `26.0.0` o superior
    - [Docker Compose](https://docs.docker.com/compose/install/){target="_blank"}: versión `2.26.0` o superior

    !!! warning
        Evite instalar Docker mediante [Snap](https://snapcraft.io){target="_blank"}, ya que puede quedar restringido por este sandbox y no tener acceso a directorios del host como `/opt/`, lo que puede impedir que los contenedores Docker de Etendo se inicien correctamente.

        Recomendación: instale Etendo usando la [última ISO](../../../../whats-new/release-notes/etendo-classic/iso.md)(que incluye Docker) o instale Docker siguiendo la guía de instalación oficial de su distribución.

    !!! info
        El módulo [Docker Management](../../bundles/platform/docker-management.md), incluido como dependencia, permite la distribución de la infraestructura dentro de los módulos de Etendo, que incluyen contenedores Docker para cada servicio.

3. ### Token de acceso de Entidad
    
    :material-menu: `Aplicación` > `Configuración General` > `Entidad` > `Entidad`

    Debe configurarse un token de cifrado de un solo uso para la autenticación. Este token es necesario para que **Etendo Main UI** inicie una sesión.

    1. Acceda a Etendo Classic como `System Administrator`.
    2. Vaya a `Entidad` > pestaña `Secure Web Service Configuration`.
    3. Haga clic en el botón **Generar Clave** para crear un token. El tiempo de caducidad se mide en minutos; si se establece en 0, el token no caduca.
    
    ![alt text](../../../../assets/developer-guide/etendo-mobile/getting-started/token.png)
    
    !!! info 
        Este token no requiere ninguna acción; solo necesita generarse para que el proceso de autenticación funcione correctamente.

## Instalación

Etendo Main UI se distribuye dentro del bundle [Platform Extensions](../../../../whats-new/release-notes/etendo-classic/bundles/platform-extensions/release-notes.md), que incluye la **infraestructura de Main UI** y todos los módulos de backend necesarios para la nueva interfaz.

!!! info
    Para poder incluir esta funcionalidad, debe instalarse el Platform Extensions Bundle.  
    Para ello, siga las instrucciones del marketplace: [Platform Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=5AE4A287F2584210876230321FBEE614){target="_blank"}.  
    Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Platform Extensions - Notas de la versión](../../bundles/platform/overview.md).

## Ejecutar Etendo Main UI

El ejemplo de configuración más sencillo utiliza **Main UI ejecutándose en Docker** y **Tomcat** ejecutándose localmente.  
Otras configuraciones se detallan en la sección [Configuración avanzada](#configuración-avanzada).

### Configuración interactiva (recomendado)

1. Puede configurar Main UI de forma interactiva ejecutando:

    ```bash
    ./gradlew setup -Pinteractive=true --console=plain
    ```

    Esto le guiará a través del proceso de configuración de todas las variables necesarias. Para más información, visite la guía de [Instalación interactiva](../../../../getting-started/interactive-installation.md).

2. Inicie los servicios Docker:
    
    ```bash title="Terminal"
        ./gradlew resources.up
    ```

    Esto iniciará el contenedor de **Main UI** junto con cualquier otro servicio Docker configurado.

### Configuración manual

1. Añada las siguientes líneas al archivo `gradle.properties`:

    ``` groovy title="gradle.properties"
        docker_com.etendoerp.mainui=true
        etendo.classic.url=http://host.docker.internal:8080/etendo
        etendo.classic.host=http://localhost:8080/etendo
        authentication.class=com.etendoerp.etendorx.auth.SWSAuthenticationManager
        ws.maxInactiveInterval=3600
        next.public.app.url=http://localhost:3000
    ```

    | Variable | Propósito (explicación simple) | Notas | Valor recomendado (local) | Valor recomendado (producción) |
    |---------|------------------------------|--------|-----------------------------|--------------------------------|
    | **docker_com.etendoerp.mainui** | Habilita el servicio Docker de Main UI. | El valor por defecto puede variar según el entorno. | `true` | `true` |
    | **etendo.classic.url** | URL del backend utilizada por el servidor de Main UI para conectarse a Etendo Classic. | Si Main UI se ejecuta en Docker y Tomcat se ejecuta localmente, debe usarse `host.docker.internal`. | `http://host.docker.internal:8080/etendo` | `https://your.backend.etendo.cloud/etendo` |
    | **etendo.classic.host** | URL del lado del cliente que el navegador utiliza para realizar solicitudes directas a Etendo Classic. | URL que el navegador utiliza para solicitudes directas. En modo híbrido con Docker, use `localhost` | `http://localhost:8080/etendo` | `https://your-domain.com/etendo` |
    | **authentication.class** | Clase Java que gestiona la autenticación entre Main UI y Etendo Classic. | Requerida para la autenticación de Secure Web Services. | `com.etendoerp.etendorx.auth.SWSAuthenticationManager` | `com.etendoerp.etendorx.auth.SWSAuthenticationManager` |
    | **ws.maxInactiveInterval** | Duración de la sesión (en segundos) para la conexión WebSocket de Main UI. | *No* afecta al tiempo de espera de sesión de Etendo Classic. El valor recomendado es 3600 segundos (1 hora). | `3600` | `3600` |
    | **next.public.app.url** | URL pública donde los usuarios acceden a la aplicación Main UI. | Debe apuntar a la URL del frontend accesible; para uso local, lo habitual es localhost. | `http://localhost:3000` | `https://your.frontend.etendo.cloud` |

3. Ejecute los siguientes comandos para configurar el módulo y actualizar los recursos:

    ```bash title="Terminal"
        ./gradlew setup
    ```

4. Inicie los servicios Docker:
    
    ```bash title="Terminal"
        ./gradlew resources.up
    ```

    Esto iniciará el contenedor de **Main UI** junto con cualquier otro servicio Docker configurado.

## Acceder a la Main UI

Una vez que todos los servicios estén en ejecución, la Main UI estará disponible en:

[http://localhost:3000](http://localhost:3000) (puerto por defecto)

!!!info
    La URL exacta puede variar en función de su configuración de Docker.

## Configuración avanzada

Esta sección está dirigida a desarrolladores que deseen contribuir o personalizar directamente el código base de **Main UI**.

### Requisitos para desarrollo

1. **Node.js** versión ^18.0.0 o superior
2. **pnpm** versión ^9.15.2 (gestor de paquetes)
3. Todos los requisitos de la instalación básica anterior.

### Instalación manual de módulos (solo desarrollo)

Para entornos de desarrollo, necesita instalar manualmente los módulos requeridos:

- `com.etendoerp.openapi`
- `com.etendoerp.etendorx`
- `com.etendoerp.metadata`
- `com.etendoerp.metadata.template`

**Comandos rápidos de clonado**

```bash
cd modules

# Clone required modules for development
git clone git@github.com:etendosoftware/com.etendoerp.etendorx.git
git clone git@github.com:etendosoftware/com.etendoerp.openapi.git 
git clone git@github.com:etendosoftware/com.etendoerp.metadata.git
git clone git@github.com:etendosoftware/com.etendoerp.metadata.template.git
```

### Estructura del proyecto de desarrollo

El workspace está organizado como un entorno único con múltiples paquetes:

```
com.etendorx.workspace-ui/
├── packages/
│   ├── api-client/          # Cliente API para comunicación con el backend
│   ├── ComponentLibrary/    # Componentes de UI reutilizables
│   └── MainUI/             # Aplicación principal
├── package.json
├── pnpm-workspace.yaml
└── README.md
```

### Pasos de instalación para desarrollo

1. Clone el repositorio de desarrollo de Main UI:

    ```bash
    git clone https://github.com/etendosoftware/com.etendorx.workspace-ui.git
    cd com.etendorx.workspace-ui
    ```

2. Instale todas las dependencias del proyecto usando `pnpm`:

    ```bash
    pnpm install
    ```

    Este comando instalará las dependencias de todos los paquetes del workspace.

3. Cree un archivo `.env.local` en el directorio `packages/MainUI`:

    ```bash
    cd packages/MainUI
    touch .env.local
    ```

4. Añada la configuración de su backend:

    ```env
    ETENDO_CLASSIC_URL=http://localhost:8080/etendo
    ```
    !!!info
        Sustituya las URLs por las URLs reales de su backend de Etendo.

5. Compile los paquetes necesarios en el orden correcto:

    ```bash
    # Build API Client first (dependency for other packages)
    pnpm --filter @workspaceui/api-client build

    # Build Component Library
    pnpm --filter @workspaceui/componentlibrary build
    ```

6. Inicie el servidor de desarrollo de Main UI:

    ```bash
    pnpm dev
    ```

    La aplicación estará disponible en [http://localhost:3000](http://localhost:3000) por defecto.

### Flujo de trabajo de desarrollo

**Comandos a nivel raíz (recomendado)**

El workspace proporciona alias prácticos a nivel raíz para tareas comunes:

```bash title="Aliases"
# Start Main UI development server
pnpm dev

# Build all packages
pnpm build

# Run tests across all packages
pnpm test

# Lint all packages
pnpm lint

# Fix lint issues automatically
pnpm lint:fix

# Format code across all packages
pnpm format

# Auto-fix formatting issues
pnpm format:fix

# Clean all build artifacts
pnpm clean

# Install dependencies
pnpm install
```

**Comandos por paquete individual**

Cada paquete también puede ejecutarse de forma independiente usando comandos de workspace de pnpm:

```bash title="Comando"
# Run MainUI development server
pnpm --filter @workspaceui/mainui dev

# Build API Client
pnpm --filter @workspaceui/api-client build

# Build Component Library
pnpm --filter @workspaceui/componentlibrary build

# Run tests for API Client
pnpm --filter @workspaceui/api-client test

# Lint specific package
pnpm --filter @workspaceui/mainui lint
```

**Linting y formateo**

El proyecto utiliza Biome para linting y formateo en todos los paquetes:

```bash
# Lint all packages
pnpm lint

# Fix lint issues
pnpm lint:fix

# Format code
pnpm format

# Auto-fix formatting
pnpm format:fix
```

### Detalles de los paquetes

**API Client (`@workspaceui/api-client`)**

Contiene definiciones TypeScript y funciones de API para comunicarse con el backend de Etendo. Proporciona:

- APIs de autenticación
- APIs de metadatos
- APIs de datasource
- APIs de integración con Copilot

**Component Library (`@workspaceui/componentlibrary`)**

Una colección de componentes React reutilizables construidos con Material-UI. Incluye:

- Componentes de formulario (inputs, selectores, etc.)
- Componentes de navegación
- Componentes modales y de diálogo
- Componentes de visualización de datos

**Main UI (`@workspaceui/mainui`)**

La aplicación principal de Next.js que proporciona la interfaz de usuario completa. Funcionalidades:

- Arquitectura moderna React/TypeScript
- Renderizado del lado del servidor con Next.js
- Integración del tema de Material-UI
- Diseño responsive

### Ejecutar pruebas

Ejecute las suites de pruebas para asegurar que todo funciona correctamente

```bash
# Run all tests
pnpm test

# Build for production
pnpm build
```

El entorno de desarrollo ya está listo para compilar y personalizar Etendo Main UI.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.