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

El Histórico de auditoría permite supervisar cada cambio de datos realizado en cualquier registro del sistema a través de la interfaz de usuario. La funcionalidad realiza el seguimiento de los siguientes tipos de cambios:

- **Nueva entrada (Inserción)** — se creó un nuevo registro
- **Cambio (Actualización)** — se modificó un registro existente
- **Eliminación (Borrado)** — se eliminó un registro

El Administrador del sistema habilita el seguimiento de auditoría para cada pantalla — por ejemplo, Pedidos de compra o Proveedores. En Etendo, cada pantalla almacena sus datos en lo que el sistema denomina una tabla; este término aparece en los pasos de configuración que se describen a continuación. Consulte [Configuración del Administrador del sistema](#system-administrator-setup) más adelante.

Esta página está organizada en dos secciones. **Configuración del Administrador del sistema** cubre la configuración técnica inicial — los usuarios de negocio pueden pasar directamente a [Uso del Histórico de auditoría](#using-the-audit-trail), ya que el administrador del sistema se encarga de la configuración. **Uso del Histórico de auditoría** explica cómo consultar los datos de auditoría una vez completada la configuración.

## Configuración del Administrador del sistema { #system-administrator-setup }

Para realizar el seguimiento de la información de auditoría, el Administrador del sistema completa dos pasos:

1. Habilitar el Histórico de auditoría para una o más tablas.
2. Actualizar la infraestructura del Histórico de auditoría recompilando la aplicación.

Ambos pasos se describen en las secciones siguientes.

### Habilitar el Histórico de auditoría para una tabla { #enabling-audit-trail-for-a-table }

:material-menu: `Diccionario de la Aplicación` > `Tablas y columnas`

!!! info
    El **Diccionario de la Aplicación** es un área de configuración del sistema accesible únicamente para los Administradores del sistema. No forma parte de los menús de negocio habituales.

El Administrador del sistema habilita o deshabilita el Histórico de auditoría para una tabla a través de la definición de la tabla en el Diccionario de la Aplicación.

1. Cambie al rol **Administrador del Sistema**. Para ello, haga clic en su nombre de usuario en la esquina superior derecha de la pantalla y seleccione **Administrador del Sistema** en la lista de roles.
2. Vaya a `Diccionario de la Aplicación` > `Tablas y columnas`.
3. En la lista que aparece, busque y abra la entrada correspondiente a la pantalla que desea auditar — por ejemplo, **Pedido de compra**.
4. Cambie a **Edit View** haciendo clic en el icono de lápiz en la barra de herramientas.
5. Marque la casilla **Completamente auditado** y haga clic en **Guardar** (el icono de disquete en la barra de herramientas).

#### Inserciones en auditoría { #audit-inserts }

De forma predeterminada, cuando una tabla está configurada como **Completamente auditado**, el sistema registra que se creó un nuevo registro, pero no guarda los valores introducidos en ese momento.

Para guardar también esos valores iniciales, marque el campo **Inserciones en auditoría** en esa tabla. Esto es opcional.

![](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/security/audit-trail/audit-trail-3.png)

#### Excluir columnas { #excluding-columns }

De forma predeterminada, todos los campos de una tabla auditada son rastreados. Para dejar de rastrear los cambios en un campo específico — por ejemplo, un campo de descripción que cambia con frecuencia y no es importante auditar — abra la solapa **Columna** dentro de `Diccionario de la Aplicación` > `Tablas y columnas`, busque el campo y marque la casilla **Excluir Auditoría**.

![](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/security/audit-trail/audit-trail-4.png)

### Actualizar infraestructura de Histórico de auditoría { #update-audit-trail-infrastructure }

Tras habilitar o deshabilitar el Histórico de auditoría para una tabla, o tras cualquier cambio en la estructura de esa tabla, el Administrador del sistema debe actualizar la infraestructura del sistema recompilando la aplicación. Hasta que lo haga, el Histórico de auditoría no refleja la configuración más reciente.

!!! warning
    Este paso requiere detener y reiniciar el servidor de aplicaciones. Planifíquelo durante una ventana de mantenimiento y coordínelo con el resto del equipo.

El Administrador del sistema debe ejecutar el siguiente comando desde el directorio raíz de Etendo:

```
./gradlew update.database compile.complete smartbuild
```

La secuencia completa es:

1. Detener Tomcat.
2. Ejecutar el comando anterior.
3. Iniciar Tomcat.

### Deshabilitar el filtrado por usuario { #disable-filtering-by-user }

El Administrador del sistema puede eliminar el filtro de usuario tanto de la vista **Histórico de auditoría - Histórico de registro** como de la vista **Histórico de auditoría - Registros eliminados**. Esto resulta útil cuando el número de usuarios en el sistema es elevado y afecta al rendimiento.

1. Vaya a `Aplicación` > `Configuración General` > `Aplicación` > [`Preferencias`](../application/preference.md).
2. Haga clic en **Nuevo**.
3. Introduzca `Show Audit Trail User filter` en el campo **Propiedad**.
4. Escriba `Y` en el campo **Valor**.
5. Haga clic en **Guardar**.

## Uso del Histórico de auditoría { #using-the-audit-trail }

Existen dos formas de consultar los datos de auditoría: el **popup de Histórico de auditoría**, que muestra el historial de un registro específico, y la **ventana de Histórico de auditoría**, que permite realizar búsquedas en todos los registros de auditoría.

### El popup de Histórico de auditoría { #the-audit-trail-popup }

Para cada tabla en la que el Histórico de auditoría está habilitado, el botón **Audit Trail** ![](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/security/audit-trail/audit-trail-5.png) aparece en la barra de herramientas de la ventana correspondiente. Al hacer clic en él se abre el popup de Histórico de auditoría.

El popup muestra el historial del registro que se muestra actualmente en la ventana. Tiene dos modos de vista:

- **Histórico de auditoría - Histórico de registro** — muestra los cambios de un único registro
- **Histórico de auditoría - Registros eliminados** — muestra los registros eliminados de una única solapa

### Vista de historial del registro { #record-history-view }

Esta vista se abre cuando usted hace clic en el botón **Audit Trail** desde un registro existente.

En la parte superior del popup se muestran el tipo de registro (por ejemplo, **Sales Order**) y el registro específico — como *1000175 - 2016-04-03* (el número de pedido y la fecha). Estos datos identifican de quién está viendo el historial. A continuación, los filtros permiten restringir los cambios mostrados, lo que resulta útil en registros con muchas modificaciones.

La grilla muestra todos los cambios realizados en el registro mientras el Histórico de auditoría estuvo habilitado, ordenados desde el cambio más reciente hasta el más antiguo.

!!! info
    Solo se muestran los campos visibles en la solapa correspondiente.

Cada fila representa un campo modificado. Si se editó un registro, aparece una fila por cada campo que cambió. Si se creó o eliminó un registro, aparece una fila por cada campo de ese registro.

![](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/security/audit-trail/audit-trail-6.png)

Para cambiar a la vista de Registros eliminados, haga clic en el enlace **Ver registros eliminados** situado encima de la grilla. Esta vista muestra los registros eliminados de la solapa actual.

### Vista de registros eliminados { #deleted-records-view }

Esta vista muestra los registros que han sido eliminados de una solapa y que ya no son accesibles a través de la interfaz habitual.

El área superior muestra el tipo de registro. A continuación, los filtros permiten restringir los registros mostrados. La grilla presenta una fila por cada registro eliminado, con las mismas columnas que la vista de grilla normal de esa solapa.

![](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/security/audit-trail/audit-trail-7.png)

**Volver al historial**

Seleccione **Volver al histórico** para volver a la vista de historial del registro, mostrando los mismos registros que antes.

**Historial del registro seleccionado**

Seleccione **Ver histórico del registro seleccionado** para ver el historial completo de cambios de un registro eliminado específico. Esto abre la vista de historial del registro, que indica que el sistema está mostrando el historial de un registro eliminado.

La siguiente captura de pantalla muestra el historial de un Pedido de venta eliminado. Incluye entradas correspondientes a la eliminación, así como la creación y modificación anteriores del registro.

![](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/security/audit-trail/audit-trail-8.png)

**Solapas secundarias**

Cuando un registro tiene líneas — por ejemplo, un Pedido de venta tiene líneas de pedido — el popup puede filtrar las líneas eliminadas para mostrar solo las pertenecientes a un Pedido de venta específico. Esto se denomina filtrado por registro padre.

**Si el registro padre todavía existe:**

1. Vaya a la solapa de líneas del Pedido de venta.
2. Haga clic en el icono de Histórico de auditoría para abrir la vista de historial del registro.
3. Haga clic en el enlace **Ver registros eliminados** para cambiar a la vista de Registros eliminados.

Dado que la solapa de líneas tiene un padre (el Pedido de venta), la vista se filtra automáticamente para mostrar solo las líneas pertenecientes a ese Pedido de venta. El área superior confirma que el filtro está activo:

![](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/security/audit-trail/audit-trail-9.png)

**Si el registro padre también ha sido eliminado:**

1. Vaya a la vista de Registros eliminados de la solapa Pedido de venta.
2. Busque el Pedido de venta cuyas líneas eliminadas desea ver.
3. Haga clic en el enlace **Líneas** situado debajo de la grilla.

La vista mostrará entonces las líneas eliminadas pertenecientes a ese Pedido de venta.

### Ventana de Histórico de auditoría { #audit-trail-window }

La ventana de **Histórico de auditoría** muestra una vista de solo lectura de todos los cambios de datos registrados en las tablas para las que el Histórico de auditoría está habilitado. No es posible realizar ediciones desde esta ventana.

![](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/security/audit-trail/audit-trail-2.png)

Esta ventana muestra los datos de auditoría tal como están almacenados internamente por el sistema. Algunos valores pueden aparecer de forma diferente a como se ven en las pantallas habituales — por ejemplo, una fecha puede mostrarse en un formato distinto, o un elemento puede identificarse mediante un código interno en lugar de su nombre. Esto es lo esperado. Utilice los campos de búsqueda y filtro de la parte superior de la ventana para encontrar el registro que busca.

Para cada cambio rastreado, la ventana muestra qué pantalla (por ejemplo, Pedidos de compra) y qué campo fueron modificados. También muestra un código asignado por el sistema que identifica el registro exacto — no es necesario utilizar este código; está disponible únicamente como referencia.

![](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/security/audit-trail/audit-trail-10.png)

## Limitaciones { #limitations }

El Histórico de auditoría registra todos los cambios de datos para las tablas habilitadas, con las siguientes excepciones:

- Los campos de texto muy largos (como notas o descripciones que superan una cierta longitud) no son auditados.
- Los archivos o datos binarios adjuntos a los registros (como documentos adjuntos) no son auditados.

Estos tipos de campo no pueden ser auditados por el Histórico de auditoría estándar. Si su proceso de negocio requiere rastrearlos, plantee el requisito al administrador del sistema, quien le indicará si existe alguna solución alternativa disponible.

*[UI]: Interfaz de usuario
*[ID]: Identificador interno asignado por el sistema para distinguir de forma única un registro

---

Este trabajo es una obra derivada de [Configuración General](https://wiki.openbravo.com/wiki/General_Setup){target="_blank"} de [Wiki de Openbravo](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="_blank"} por [Etendo](https://etendo.software){target="_blank"}.
