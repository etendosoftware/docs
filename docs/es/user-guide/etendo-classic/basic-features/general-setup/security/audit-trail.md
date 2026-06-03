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

El Histórico de auditoría permite a los usuarios monitorizar cada cambio de datos realizado en cualquier registro del sistema a través de la interfaz de usuario.

La funcionalidad de Histórico de auditoría monitoriza cambios de datos como:

- Inserción
- Actualización
- Eliminación

Esta funcionalidad debe ser habilitada por el Administrador del sistema. Para ello, el administrador configura qué tablas de datos deben ser rastreadas — esto se realiza en un área de administración técnica denominada Diccionario de la Aplicación.

Una vez que se ha realizado un cambio en una tabla para la que se ha habilitado la funcionalidad de Histórico de auditoría, es posible monitorizar ese cambio a través de la interfaz de usuario utilizando el botón de acción **Histórico de auditoría**.

![](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/security/audit-trail/audit-trail-1.png)

## Ventana de Histórico de auditoría { #audit-trail-window }

La vista de Histórico de auditoría muestra información de solo lectura sobre todos los cambios de datos registrados realizados en las tablas para las que se ha habilitado la funcionalidad de Histórico de auditoría.

![](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/security/audit-trail/audit-trail-2.png)

Para cada cambio rastreado, la ventana muestra qué tabla y campo fueron modificados, junto con un ID único que identifica el registro específico que fue cambiado.

## Configuración { #configuration }

Para realizar el seguimiento de la información de auditoría, el administrador del sistema debe llevar a cabo dos tareas:

- **Habilitar el Histórico de auditoría** para una o más tablas del sistema
- Ejecutar el proceso **Applying Configuration Changes**

En las siguientes secciones se proporciona una guía paso a paso con información más detallada.

## Habilitar el Histórico de auditoría para una tabla { #enabling-audit-trail-for-a-table }

El Administrador del sistema habilita o deshabilita el Histórico de auditoría para una tabla abriendo la definición de la tabla en el Diccionario de la Aplicación.

- Cambie al rol de **Administrador del sistema**
- Vaya al menú Aplicación y navegue a **Diccionario de la Aplicación** > **Tablas y columnas**
- **Navegue hasta la tabla** para la que desea habilitar el Histórico de auditoría
- Cambie a **Vista de edición**
- Marque la casilla **Completamente auditado** y guarde

### Inserciones en auditoría { #audit-inserts }

De forma predeterminada, cuando una tabla está configurada como **Completamente auditado**, el sistema no registra una entrada separada por cada nuevo elemento añadido — solo registra que se creó un nuevo registro. Si también necesita capturar los valores exactos que se introdujeron al crear por primera vez un registro, marque el campo **Inserciones en auditoría** en esa tabla. Esto es opcional y habitualmente no es necesario.

![](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/security/audit-trail/audit-trail-3.png)

### Excluir columnas { #excluding-columns }

De forma predeterminada, todos los campos de una tabla auditada son rastreados. Si desea dejar de rastrear los cambios en un campo específico — por ejemplo, un campo de notas que cambia con frecuencia y no es importante auditar — puede excluirlo. Para ello, abra la solapa **Columna** dentro de **Diccionario de la Aplicación** > **Tablas y columnas**, busque el campo que desea excluir y marque la casilla **Excluir Auditoría**.

![](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/security/audit-trail/audit-trail-4.png)

## Applying Configuration Changes { #applying-configuration-changes }

Tras habilitar o deshabilitar el Histórico de auditoría para una tabla, o tras cualquier cambio en la estructura de esa tabla, el administrador del sistema debe ejecutar el proceso Applying Configuration Changes para aplicar la actualización. Hasta que se ejecute este proceso, el Histórico de auditoría no reflejará la configuración más reciente. Contacte con su administrador del sistema si no está seguro de si esto se ha realizado.

## El popup de Histórico de auditoría { #the-audit-trail-popup }

Para el conjunto de tablas para las que se ha habilitado la funcionalidad de Histórico de auditoría, se muestra el botón ![](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/security/audit-trail/audit-trail-5.png) en la barra de herramientas de las ventanas correspondientes. Este da acceso al popup de Histórico de auditoría.

Este popup permite examinar el historial del registro que se muestra actualmente en la ventana. Tiene dos modos de vista principales que permiten examinar los siguientes datos:

- **Historial del registro** de un único registro
- **Registros eliminados** de una única solapa

## Vista de historial del registro { #record-history-view }

Esta vista se muestra cuando el popup se abre desde un registro existente mediante el nuevo botón de la barra de herramientas.

El área superior siempre muestra el tipo de registro (por ejemplo, **Pedido de venta**) y el registro específico — como *1000175 - 2016-04-03* — cuyo historial se muestra.

A continuación, hay disponibles varios filtros que permiten restringir los cambios mostrados para facilitar el uso en registros con muchas modificaciones.

La cuadrícula del área inferior muestra todos los cambios realizados en este registro mientras la funcionalidad de Histórico de auditoría estuvo habilitada. Los cambios se muestran ordenados desde el cambio más reciente hacia los cambios anteriores.

!!! info
    Solo se muestran aquí los campos que son visibles en la solapa correspondiente.

Cada fila de la cuadrícula muestra un campo modificado. Si se editó un registro, verá una fila por cada campo que fue cambiado. Si se creó o eliminó un registro, verá una fila por cada campo de ese registro.

![](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/security/audit-trail/audit-trail-6.png)

Por último, un enlace justo encima de la cuadrícula permite cambiar a la vista de Registros eliminados. Al seguir ese enlace se mostrarán los registros eliminados de la solapa desde la que se abrió el popup de Histórico de auditoría.

## Deshabilitar el filtrado por usuario { #disable-filtering-by-user }

El filtro de Usuario puede eliminarse tanto de la vista **Historial del registro** como de la vista **Registros eliminados**. Esto puede ser de interés por razones de rendimiento cuando el número de usuarios disponibles es alto. Para ello, vaya a **Aplicación** > **Configuración General** > **Aplicación** > [`Preferencia`](../application/preference.md) y añada la siguiente preferencia: Show Audit Trail User filter con valor Y.

## Vista de registros eliminados { #deleted-records-view }

Esta vista permite examinar registros que han sido eliminados de una solapa y que, de otro modo, ya no son accesibles en la interfaz de usuario.

El diseño general de la vista es similar al de la vista de historial del registro.

El área superior muestra el tipo de registro para el que se muestran los registros eliminados. Justo debajo, hay disponibles varios filtros para restringir los registros mostrados.

A continuación, una cuadrícula muestra todos los registros eliminados pertenecientes a esta solapa. Aquí, cada fila mostrada corresponde a un único registro eliminado y las columnas mostradas son las mismas que las que se muestran en la vista de cuadrícula normal de la misma solapa.

![](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/security/audit-trail/audit-trail-7.png)

Esta vista ofrece varias **opciones de navegación** para ver información relacionada o más detallada.

### Opciones de navegación { #navigation-choices }

#### Volver al historial { #back-to-history }

La primera es Volver al historial. Al seguir este enlace, la vista simplemente vuelve a Historial del registro mostrando los mismos registros que se mostraban antes de ir a la vista de registros eliminados.

#### Historial del registro seleccionado { #history-of-selected-record }

La siguiente, Ver historial del registro eliminado seleccionado a continuación, permite examinar el historial detallado de un registro eliminado, en lugar de la vista de resumen que se muestra aquí.

Este historial detallado se muestra en la misma vista de 'Historial del registro'; sin embargo, su área de información superior indica que se está mostrando el historial de un registro eliminado.

La siguiente captura de pantalla muestra un ejemplo de la vista de historial de la misma entrada de Pedido de venta eliminada. En comparación con el ejemplo anterior de esta vista, se muestran nuevas entradas de historial correspondientes a la eliminación, además de la información anterior sobre la creación y modificación del registro.

![](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/security/audit-trail/audit-trail-8.png)

#### Solapas hijas { #child-tabs }

Como último método de navegación, el popup permite filtrar registros en función de un registro padre. Esto puede ser útil para buscar líneas eliminadas pertenecientes a un pedido de venta.

Hay dos formas posibles en función del estado del registro padre: aún existente o ya eliminado.

Si el registro padre (p. ej., un Pedido de venta) todavía existe, entonces pueden realizarse los siguientes pasos para ver sus líneas eliminadas:

1. Vaya a la solapa de líneas del Pedido de venta
2. Haga clic en el icono de Histórico de auditoría para abrir la vista de historial del registro
3. Utilice los enlaces de 'Registros eliminados' para cambiar a la vista de registros eliminados

Como la solapa de líneas no es una solapa de nivel superior (tiene una solapa padre Pedido de venta), la vista de registros eliminados se filtra automáticamente para mostrar solo las líneas pertenecientes al Pedido de venta actual. Como información visual de que la información mostrada está filtrada, el área de información superior muestra:

![](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/security/audit-trail/audit-trail-9.png)

Si el registro padre (p. ej., un Pedido de venta) ya no existe, entonces se puede lograr lo mismo siguiendo estos pasos:

1. Vaya a la vista de Registros eliminados de la solapa Pedido de venta
2. Busque el Pedido de venta para el que deben mostrarse las líneas eliminadas
3. Haga clic en el enlace Líneas justo debajo de la cuadrícula

Entonces, la vista de registros eliminados mostrará las líneas eliminadas pertenecientes al Pedido de venta (eliminado) seleccionado.

## Una ventana de Histórico de auditoría generada { #a-generated-audit-trail-window }

La segunda forma de ver los datos de auditoría es una ventana de búsqueda estándar. Abra el menú **Aplicación**, vaya a **Configuración General** > **Seguridad** y seleccione **Histórico de auditoría**. Esta ventana permite explorar toda la información de auditoría filtrada por el cliente actualmente activo.

Esta ventana muestra los datos de auditoría sin formato exactamente tal como están almacenados en el sistema. Los valores aparecen tal como se registran internamente — por ejemplo, las fechas o las referencias de código pueden no mostrarse con las mismas etiquetas que se ven en otras partes de la aplicación. Utilice esta ventana cuando necesite buscar o filtrar entre todos los registros de auditoría.

Esta ventana también ofrece opciones de filtrado y búsqueda más flexibles que la vista de popup.

![](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/security/audit-trail/audit-trail-10.png)

## Limitaciones { #limitations }

La funcionalidad de Histórico de auditoría registrará todos los cambios de datos (para la tabla para la que se ha habilitado) con las siguientes excepciones:

- Los campos de texto muy largos (habitualmente los utilizados para almacenar notas o descripciones que superan una cierta longitud) no serán auditados.
- Los archivos o datos binarios adjuntos a los registros (como los documentos adjuntos) no serán auditados.

Si necesita rastrear los cambios en estos tipos de campos, contacte con su administrador del sistema.

## Etendo Advanced Security

El módulo **Etendo Advanced Security** permite al usuario personalizar varias funcionalidades de seguridad como las siguientes:

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
