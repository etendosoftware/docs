---
title: Histórico de auditoría
tags:
    - Histórico de auditoría
    - Seguridad
    - Monitor
---

# Histórico de auditoría { #audit-trail }

:material-menu: `Aplicación` > `Configuración General` > `Seguridad` > `Histórico de auditoría`

## Descripción general { #overview }

El Histórico de auditoría permite monitorizar cada cambio de datos realizado en cualquier registro del sistema a través de la interfaz de usuario. La funcionalidad realiza el seguimiento de los siguientes tipos de cambios:

- **Inserción** — se creó un nuevo registro
- **Actualización** — se modificó un registro existente
- **Eliminación** — se eliminó un registro

El Administrador del sistema habilita el seguimiento de auditoría para cada tabla antes de que se registre cualquier cambio. Consulte [Configuración](#configuration) a continuación.

## Configuración { #configuration }

Para realizar el seguimiento de la información de auditoría, el Administrador del sistema completa dos pasos:

1. Habilitar el Histórico de auditoría para una o más tablas.
2. Ejecutar el proceso **Update Audit Trail Infrastructure**.

Ambos pasos se describen en las secciones siguientes.

## Habilitar el Histórico de auditoría para una tabla { #enabling-audit-trail-for-a-table }

:material-menu: `Diccionario de la Aplicación` > `Tablas y columnas`

!!! info
    El **Diccionario de la Aplicación** es un área de configuración del sistema accesible únicamente para los Administradores del sistema. No forma parte de los menús de negocio habituales.

El Administrador del sistema habilita o deshabilita el Histórico de auditoría para una tabla a través de la definición de la tabla en el Diccionario de la Aplicación.

1. Cambie al rol de **Administrador del sistema**.
2. Vaya a `Diccionario de la Aplicación` > `Tablas y columnas`.
3. Navegue hasta la tabla para la que desea habilitar el Histórico de auditoría.
4. Cambie a **Vista de edición**.
5. Marque la casilla **Completamente auditado** y guarde.

### Inserciones en auditoría { #audit-inserts }

De forma predeterminada, cuando una tabla está configurada como **Completamente auditado**, el sistema registra que se creó un nuevo registro, pero no guarda los valores introducidos en ese momento.

Para guardar también esos valores iniciales, marque el campo **Inserciones en auditoría** en esa tabla. Esto es opcional.

![](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/security/audit-trail/audit-trail-3.png)

### Excluir columnas { #excluding-columns }

De forma predeterminada, todos los campos de una tabla auditada son rastreados. Para dejar de rastrear los cambios en un campo específico — por ejemplo, un campo de notas que cambia con frecuencia y no es importante auditar — abra la solapa **Columna** dentro de `Diccionario de la Aplicación` > `Tablas y columnas`, busque el campo y marque la casilla **Excluir Auditoría**.

![](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/security/audit-trail/audit-trail-4.png)

## Update Audit Trail Infrastructure { #update-audit-trail-infrastructure }

Tras habilitar o deshabilitar el Histórico de auditoría para una tabla, o tras cualquier cambio en la estructura de esa tabla, ejecute el proceso **Update Audit Trail Infrastructure**. Hasta que se ejecute este proceso, el Histórico de auditoría no reflejará la configuración más reciente.

Ejecute el proceso desde la ventana [Solicitud de proceso](../process-scheduling/process-request.md):

1. Vaya a `Aplicación` > `Configuración General` > `Programación de procesos` > `Solicitud de proceso`.
2. Seleccione la **Organización**.
3. Seleccione **Update Audit Trail Infrastructure** en el campo **Proceso**.
4. Establezca la **Temporización** en **Ejecutar inmediatamente**.
5. Haga clic en **Programar proceso**.

!!! tip
    Para verificar que el proceso se completó correctamente, vaya a `Aplicación` > `Configuración General` > `Programación de procesos` > [`Monitor de procesos`](../process-scheduling/process-monitor.md) y compruebe el estado de la ejecución.

## Visualización de los datos de auditoría { #viewing-audit-data }

Existen dos formas de visualizar los datos de auditoría: el **Popup de Histórico de auditoría**, que muestra el historial de un registro específico, y la **Ventana de Histórico de auditoría**, que permite realizar búsquedas en todos los registros de auditoría.

## El popup de Histórico de auditoría { #the-audit-trail-popup }

Para cada tabla en la que el Histórico de auditoría está habilitado, el botón ![](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/security/audit-trail/audit-trail-5.png) aparece en la barra de herramientas de la ventana correspondiente. Al hacer clic en él se abre el popup de Histórico de auditoría.

El popup muestra el historial del registro que se muestra actualmente en la ventana. Tiene dos modos de vista:

- **Historial del registro** — muestra los cambios de un único registro
- **Registros eliminados** — muestra los registros eliminados de una única solapa

## Vista de historial del registro { #record-history-view }

Esta vista se muestra cuando se hace clic en el botón de Histórico de auditoría desde un registro existente.

El área superior muestra el tipo de registro (por ejemplo, **Pedido de venta**) y el registro específico — como *1000175 - 2016-04-03* — cuyo historial se muestra. A continuación, los filtros permiten restringir los cambios mostrados, lo que resulta útil en registros con muchas modificaciones.

La cuadrícula muestra todos los cambios realizados en el registro mientras el Histórico de auditoría estuvo habilitado, ordenados desde el cambio más reciente hasta el más antiguo.

!!! info
    Solo se muestran los campos visibles en la solapa correspondiente.

Cada fila representa un campo modificado. Si se editó un registro, aparece una fila por cada campo que cambió. Si se creó o eliminó un registro, aparece una fila por cada campo de ese registro.

![](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/security/audit-trail/audit-trail-6.png)

Un enlace situado encima de la cuadrícula permite cambiar a la vista de Registros eliminados, donde se muestran los registros eliminados de la solapa desde la que se abrió el popup.

## Vista de registros eliminados { #deleted-records-view }

Esta vista muestra los registros que han sido eliminados de una solapa y que ya no son accesibles a través de la interfaz habitual.

El área superior muestra el tipo de registro. A continuación, los filtros permiten restringir los registros mostrados. La cuadrícula presenta una fila por cada registro eliminado, con las mismas columnas que la vista de cuadrícula normal de esa solapa.

![](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/security/audit-trail/audit-trail-7.png)

### Opciones de navegación { #navigation-options }

#### Volver al historial { #back-to-history }

Seleccione **Volver al histórico** para volver a la vista de Historial del registro, mostrando los mismos registros que antes.

#### Historial del registro seleccionado { #history-of-selected-record }

Seleccione **Ver historial del registro eliminado seleccionado** para ver el historial completo de cambios de un registro eliminado específico. Esto abre la vista de Historial del registro, que indica que se está mostrando el historial de un registro eliminado.

La siguiente captura de pantalla muestra el historial de un Pedido de venta eliminado. Incluye entradas correspondientes a la eliminación, así como la creación y modificación anteriores del registro.

![](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/security/audit-trail/audit-trail-8.png)

#### Solapas hijas { #child-tabs }

El popup permite filtrar registros eliminados en función de un registro padre. Esto resulta útil para buscar líneas eliminadas pertenecientes a un pedido de venta.

**Si el registro padre todavía existe:**

1. Vaya a la solapa de líneas del Pedido de venta.
2. Haga clic en el icono de Histórico de auditoría para abrir la vista de Historial del registro.
3. Haga clic en el enlace **Registros eliminados** para cambiar a la vista de Registros eliminados.

Dado que la solapa de líneas tiene un padre (el Pedido de venta), la vista se filtra automáticamente para mostrar solo las líneas pertenecientes a ese Pedido de venta. El área superior confirma que el filtro está activo:

![](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/security/audit-trail/audit-trail-9.png)

**Si el registro padre también ha sido eliminado:**

1. Vaya a la vista de Registros eliminados de la solapa Pedido de venta.
2. Busque el Pedido de venta cuyas líneas eliminadas desea ver.
3. Haga clic en el enlace **Líneas** situado debajo de la cuadrícula.

La vista mostrará entonces las líneas eliminadas pertenecientes a ese Pedido de venta.

## Deshabilitar el filtrado por usuario { #disable-filtering-by-user }

El filtro de Usuario puede eliminarse tanto de la vista Historial del registro como de la vista Registros eliminados. Esto resulta útil cuando el número de usuarios en el sistema es elevado y afecta al rendimiento.

Vaya a `Aplicación` > `Configuración General` > `Aplicación` > [`Preferencias`](../application/preference.md) y cree un nuevo registro de preferencia con la propiedad **Mostrar filtro de usuarios en Histórico de Auditoría** con el valor `Y`.

## Ventana de Histórico de auditoría { #audit-trail-window }

La ventana de Histórico de auditoría muestra una vista de solo lectura (es decir, puede consultar pero no modificar nada aquí) de todos los cambios de datos registrados en las tablas para las que el Histórico de auditoría está habilitado.

![](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/security/audit-trail/audit-trail-2.png)

Esta ventana muestra los datos de auditoría tal como están almacenados internamente por el sistema. Algunos valores pueden aparecer de forma diferente a como se ven en las pantallas habituales — por ejemplo, una fecha puede mostrarse en un formato distinto, o un elemento puede identificarse mediante un código interno en lugar de su nombre. Esto es lo esperado. Utilice esta ventana para buscar o filtrar en todos los registros de auditoría.

Para cada cambio rastreado, la ventana muestra qué tabla y campo fueron modificados, junto con un identificador único que identifica el registro específico que fue cambiado.

![](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/security/audit-trail/audit-trail-10.png)

## Limitaciones { #limitations }

El Histórico de auditoría registra todos los cambios de datos para las tablas habilitadas, con las siguientes excepciones:

- Los campos de texto muy largos (como notas o descripciones que superan una cierta longitud) no son auditados.
- Los archivos o datos binarios adjuntos a los registros (como documentos adjuntos) no son auditados.

Para rastrear los cambios en estos tipos de campos, contacte con su administrador del sistema.

## Etendo Advanced Security { #etendo-advanced-security }

El módulo **Etendo Advanced Security** permite personalizar varias funcionalidades de seguridad, entre ellas:

- Seguridad de contraseñas
- Historial de contraseñas
- Bloqueo de usuario
- Verificación de múltiples sesiones
- Cambio de contraseña después del inicio de sesión
- Tiempo de caducidad (bloqueo automático de contraseña)

!!! info
    Para más información, visite la [Guía del usuario del módulo Etendo Advanced Security](../../../optional-features/bundles/platform-extensions/etendo-advanced-security.md).

---

Este trabajo es una obra derivada de [Configuración General](https://wiki.openbravo.com/wiki/General_Setup){target="_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="_blank"} por [Etendo](https://etendo.software){target="_blank"}.
