---
title: Cómo configurar el Tiempo de Expiración de sesión
tags: 
  - Cómo hacer
  - Configuración
  - Tiempo de Expiración de sesión
  - Seguridad
---

# Cómo configurar el Tiempo de Expiración de sesión

## Visión general

Etendo Classic incluye un mecanismo de tiempo de expiración de sesión que cierra la sesión de los usuarios tras un periodo definido de inactividad. Esta funcionalidad ayuda a garantizar la seguridad y una gestión eficiente de los recursos.

Esta guía explica cómo configurar el ajuste de tiempo de expiración de sesión en Etendo Classic, incluyendo los pasos para aplicar y exportar la configuración.

## ¿Qué es el Tiempo de Expiración de sesión?

El tiempo de expiración de sesión define la duración de la inactividad del usuario que desencadena la finalización automática de la sesión.  

- Por ejemplo, con un tiempo de expiración configurado en **60 minutos**, un usuario que permanezca inactivo durante ese tiempo cerrará su sesión automáticamente.  
- Si un usuario cierra el navegador sin seleccionar **Cerrar sesión**, la sesión seguirá expirando tras el periodo de tiempo de expiración configurado.


## Personalización del Tiempo de Expiración de sesión
:material-menu: `Aplicación` > `Diccionario de la Aplicación` > `Mapeo de Implementación del Diccionario`

Siga estos pasos para configurar un tiempo de expiración de sesión personalizado:

1. Inicie sesión como **Administrador del sistema**.
2. Vaya a `Diccionario de la Aplicación > Mapeo de Implementación del Diccionario`.
3. Busque el objeto llamado `Timeout`.
4. Cambie a la solapa `Parámetros` y localice el parámetro **Tiempo de Expiración**.
5. Establezca el **Identificador** con el valor de tiempo de expiración deseado (en minutos).

!!!tip
    Tiempo de expiración de sesión por defecto: **60 minutos**

!!!info 
    Antes de exportar esta configuración, asegúrese de que exista una **plantilla activa**, ya que este es un valor del núcleo del sistema que no puede modificarse a menos que haya una plantilla activa.

![alt text](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-configure-session-timeout/ad-implementation-mapping.png)

## Aplicación de los cambios

Después de modificar el parámetro de tiempo de expiración, aplique los cambios usando la siguiente tarea de Gradle:

```bash title="Terminal"
./gradlew smartbuild
```
Este comando regenera el archivo `web.xml` y aplica los cambios necesarios.


## Exportación de la configuración

Si hay una plantilla activa y desea exportar la configuración modificada del tiempo de expiración de sesión, ejecute:

```bash title="Terminal"
./gradlew export.config.script
```

!!!note
    Este paso solo es necesario cuando se distribuye la configuración como parte de una plantilla. Si no se exporta, el cambio puede perderse en futuras compilaciones o actualizaciones.


---

- Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L.](https://etendo.software){target="_blank"}.