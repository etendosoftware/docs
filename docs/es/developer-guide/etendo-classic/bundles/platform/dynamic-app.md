---
tags:
  - Aplicación dinámica
  - Subaplicación
  - Etendo Mobile
---
# Aplicación dinámica 
:octicons-package-16: Javapackage: `com.etendoerp.dynamic.app`

## Visión general
Esta página explica cómo configurar y exportar aplicaciones dinámicas en Etendo Classic, que se muestran dinámicamente en Etendo Mobile.

### Ventana Aplicación dinámica
:material-menu: `Aplicación` > `Configuración General` > `Aplicación` > `Aplicación dinámica`

Con el rol `System Administrator`, en la ventana **Aplicación dinámica**, especifique las rutas y versiones para cada subaplicación. Estos ajustes determinan cómo se muestran las subaplicaciones cuando los usuarios inician sesión en Etendo Mobile.

![](../../../../assets/developer-guide/etendo-classic/bundles/platform/dynamic-app/dynamic-app.png)

Campos a tener en cuenta:

- **Módulo**: El módulo que puede exportar la configuración de la ventana.
- **Nombre**: Nombre con el que se mostrará la aplicación.
- **Ubicación del directorio**: La ruta donde se encuentra el bundle de la aplicación compilada. En desarrollo, la ruta debe estar vacía `/`, pero en producción, la ruta es `/<javapackage>/web/`.
- **Activo**: Para seleccionar si esta aplicación está activa o no.

### Solapa Versión de la aplicación dinámica 
Permite versionar la aplicación, habilitando tanto versiones de desarrollo como de producción.

Campos a tener en cuenta:

- **Nombre**: Nombre de la versión de la aplicación, p. ej. `dev` o `1.0.0`.
- **Nombre archivo**: El nombre del bundle de la aplicación compilada, por defecto `dist.js`.
- **Valor por defecto**: Esta marca define que esta versión es productiva.
- **Es de desarrollo**: Esta marca define que esta versión está en desarrollo y puede desplegarse localmente.
- **Activo**: Para seleccionar si esta versión de la aplicación está activa o no.
- **Recibir archivos externos** Identifica subaplicaciones que permiten recibir archivos compartidos desde aplicaciones externas y son capaces de gestionarlos.


---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.