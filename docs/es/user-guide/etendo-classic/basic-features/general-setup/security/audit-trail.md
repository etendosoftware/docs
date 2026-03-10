---
title: Histórico de auditoría
tags:
    - Histórico de auditoría
    - Seguridad
    - Monitor
---

# Histórico de auditoría

:material-menu: `Aplicación` > `Configuración General` > `Seguridad` > `Histórico de auditoría`

## Visión general

El Histórico de auditoría permite al usuario monitorizar cada cambio de datos realizado en cualquier tabla o entidad a través de la interfaz de usuario.

La funcionalidad de histórico de auditoría monitoriza cambios de datos como:

- Inserción
- Actualización
- Eliminación

Esta funcionalidad debe ser habilitada por el rol de Administrador del sistema en el Diccionario de la Aplicación, ya que lo primero que debe hacerse es configurar la(s) tabla(s) para las que se va a habilitar esta funcionalidad.

Una vez que se ha realizado un cambio en una tabla para la que se ha habilitado la funcionalidad de histórico de auditoría, es posible monitorizar ese cambio a través de la interfaz de usuario utilizando el botón de acción **Histórico de auditoría**.

![](../../../../../assets/drive/V-wLKxec4uzSuG-eFItBU00cQYeO5SNhiLTDkY78kPRaK6e-P_R_z39-K5icHtUSX-WjoeFL34_Iv45c0aym2FRV9_F_e0W6QA0U8Lim_qkovbX44ihOl-nH-mKEio1pSpfQDqlm.png)

## Histórico de auditoría

La vista de Histórico de auditoría muestra información de solo lectura sobre todos los cambios de datos registrados realizados en las tablas para las que se ha habilitado la funcionalidad de histórico de auditoría.

![](../../../../../assets/drive/CkScAz_BHFw9uZIejCEG18y9IOkyiO23K5CMqCRWCkc-DEAWZ0x5G8RyDwjqApky49FILfUisRIJUnqS_Sfob0j128cKfhFFQhfOI92bmbTAPsN1TyfGVMaPXeoj9tbBzqsTB-r4.png)

Los cambios realizados en una tabla, columna y registro determinados se visualizan mostrando el ID de registro correspondiente o el UI de los registros en la base de datos.

## Configuración

Para realizar el seguimiento de la información de auditoría, el administrador del sistema debe realizar dos tareas:

- **Habilitar el histórico de auditoría** para una o más tablas del sistema
- Ejecutar el proceso **Actualizar la infraestructura del histórico de auditoría**

En las siguientes secciones se proporciona una guía paso a paso con información más detallada.

## Habilitar el histórico de auditoría para una tabla

La habilitación/deshabilitación de la funcionalidad de histórico de auditoría para una tabla se realiza en la definición de la tabla en el Diccionario de la Aplicación.

- Cambie al rol de **Administrador del sistema**
- Vaya a **Diccionario de la Aplicación > Tablas y Columnas**
- **Navegue hasta la tabla** para la que desea habilitar el Histórico de auditoría
- Cambie a **Vista de edición**
- Marque la casilla **Completamente auditado** y guarde

### Inserciones en auditoría

Cuando una tabla está marcada como **Completamente auditado**, los usuarios pueden decidir si desean auditar las inserciones realizadas en esa tabla.

![](../../../../../assets/drive/ebTtUMQskmHQd1Fd5BWoW0_lKwtwgNTn41V1uJKV4RGTKR_uXKuR_PqU4rzTUBVQct38OejbovWWycB-z1A7YEvwNedzpv6VCi38eHb2telDh9994cV4vCW1QEOGlDw1Ojs11Und.png)

Si el campo Inserciones en auditoría está marcado en una tabla, cuando se inserta una nueva fila en esa tabla se insertarán varios registros en la tabla de Histórico de auditoría, uno por cada columna de la tabla auditada. Estos registros contendrán el valor original de las columnas de la nueva fila.

Normalmente, no es necesario almacenar esta información, porque el valor original de una columna podría obtenerse fácilmente utilizando los campos Valor anterior y Valor nuevo de la tabla de Histórico de auditoría que corresponden con esa columna. Si el campo Inserciones en auditoría se deja sin marcar, solo se insertará una fila en la tabla de Histórico de auditoría por cada registro insertado en la tabla auditada. Al menos este registro debe insertarse en la tabla de Histórico de auditoría para poder almacenar qué proceso se utilizó para crear el registro en la tabla auditada.

### Excluir columnas

De forma predeterminada, cuando una tabla está auditada, se auditan las modificaciones en cualquiera de sus columnas. En algunos casos, tiene sentido no auditar los cambios de algunas de ellas. Esto se puede configurar estableciendo el indicador **Excluir Auditoría** en `Tablas y Columnas` > `Tabla` > pestaña `Columna`.

![](../../../../../assets/drive/Xy3wTyW3wrUeerAoND_Rw2c6wVVhxkq_AEzzTjBLLpiBg6VsMWcQjAn6T4te4akp_o-x381v3wT3012cttvLqjKWRsd-Tfe0Go0FX1KGlG_vSG57Bm4yo8ZnB0gxdTSV3qi7f-4b.png)

## Ejecutar la compilación del sistema

El sistema de histórico de auditoría utiliza una serie de triggers generados (uno por tabla a auditar) para recopilar los datos de auditoría de todos los cambios.

Estos triggers deben regenerarse al ejecutar una compilación del sistema, una vez que se hayan realizado las siguientes acciones:

- Se ha habilitado o deshabilitado la funcionalidad de Histórico de auditoría para una tabla
- Ha habido algún cambio estructural en una tabla que está siendo auditada (p. ej., nuevas columnas, columnas modificadas)

## El popup de Histórico de auditoría

Para el conjunto de tablas para las que se ha habilitado la funcionalidad de histórico de auditoría, se muestra el botón ![](../../../../../assets/drive/tmlPernhlkGB49t7gLt12N3zfxbYevzxuPC65DZavmEO8p5UBe2_sO_YD6lBTkhBvnNrQ64jkRAnuahaKRTGnLPGUvmSEX_K5_Ekh5Ojd-21ZyZ4KWEFIjujNg_xqg_PCFahXdJo.png) en la barra de herramientas de las ventanas correspondientes. Este da acceso al popup de Histórico de auditoría.

Este popup permite examinar el historial del registro que se muestra actualmente en la ventana. Tiene dos modos de vista principales que permiten examinar los siguientes datos:

- **Historial del registro** de un único registro
- **Registros eliminados** de una única pestaña

## Vista de historial del registro

Esta vista se muestra cuando el popup se abre desde un registro existente mediante el nuevo botón de la barra de herramientas.

El área superior siempre muestra una referencia a la entidad (p. ej., Pedido de venta) y el registro *1000175 - 2016-04-03 00:00:00.0-0.00* para el que se muestra el historial.

A continuación, hay disponibles varios filtros que permiten restringir los cambios mostrados para facilitar el uso en registros con muchas modificaciones.

La cuadrícula del área inferior muestra todos los cambios realizados en este registro mientras la funcionalidad de histórico de auditoría estuvo habilitada. Los cambios se muestran ordenados desde el cambio más reciente hacia los cambios anteriores.

!!! info
    Solo se muestran aquí los campos que son visibles en la pestaña correspondiente.

Una fila en esta cuadrícula corresponde a un único campo modificado. Para cambios en un registro existente, el número de entradas mostradas en la cuadrícula corresponde al número de campos modificados. Para la creación de nuevos registros o la eliminación de registros, se muestra una fila en la cuadrícula por cada campo del registro insertado/eliminado.

![](../../../../../assets/drive/xuE5w_TI2LS9M4nl1fyqWctoD-pU08N6dq7mQJT7qr-wsocs2FehRp7Gu1jGCsJUu_UZeo1hmDjBPQRFV_d1aM26q9zxMjXPX5GbX-SZOJYuZTwo1PYtoD-oi3XRzlyS723rbaWL.png)

Por último, un enlace justo encima de la cuadrícula permite cambiar a la vista de Registros eliminados. Al seguir ese enlace se mostrarán los registros eliminados de la pestaña desde la que se abrió el popup de Histórico de auditoría.

### Deshabilitar el filtrado por usuario

El filtro de Usuario puede eliminarse tanto de la vista **Historial del registro** como de la vista **Registros eliminados**. Esto puede ser interesante por razones de rendimiento cuando el número de usuarios disponibles es alto. Para ello, vaya a `Configuración General` > `Aplicación` > `Preferencia` y añada la siguiente preferencia: Show Audit Trail User filter con valor Y.

## Vista de registros eliminados

Esta vista permite examinar registros que han sido eliminados de una pestaña y que, de otro modo, ya no son accesibles en la interfaz de usuario.

El diseño general de la vista es similar al de la vista de historial del registro.

En la parte superior se muestra una información con una referencia a la entidad para la que se muestran los registros eliminados. Justo debajo, hay disponibles varios filtros para restringir los registros mostrados.

A continuación, una cuadrícula muestra todos los registros eliminados pertenecientes a esta pestaña/entidad. Aquí, cada fila mostrada corresponde a un único registro eliminado y las columnas mostradas son las mismas que las que se muestran en la vista de cuadrícula normal de la misma pestaña.

![](../../../../../assets/drive/lsX2HjGHdMbgCKFRs-_KuE1qmeMs2u9cZ5PXrJ5RmYw08PYbdJ6KB_dY93TwaW9ycfaNUc9fEWmsMFKPipMYza0ZCPZdMcl4c9sjFemg7ndkntS2ai5Rs-eePUDaFXXNdKFJ6VOV.png)

Esta vista ofrece varias **opciones de navegación** para ver información relacionada o más detallada.

### Opciones de navegación

#### Volver al historial

La primera es Volver al historial. Al seguir este enlace, la vista simplemente vuelve a Historial del registro mostrando los mismos registros que se mostraban antes de ir a la vista de registros eliminados.

#### Historial del registro seleccionado

La siguiente, Ver historial del registro eliminado seleccionado a continuación, permite examinar el historial detallado de un registro eliminado, en lugar de la vista de resumen que se muestra aquí.

Este historial detallado se muestra en la misma vista de 'Historial del registro'; sin embargo, su área de información superior indica el hecho de que se está mostrando el historial de un registro eliminado.

La siguiente captura de pantalla muestra un ejemplo de la vista de historial de la misma entrada de Pedido de venta eliminada. En comparación con el ejemplo anterior de esta vista, se muestran nuevas entradas de historial correspondientes a la eliminación, además de la información anterior sobre la creación y modificación del registro.

![](../../../../../assets/drive/GtW2mnbfKHPPLTLwrt_Kqjlbdm7lo_7CLDntpxMg4vRZnjAaRkOeUzxOg19gnju2DAgUuLBNrm0szABl1MVSV5Ft9_5ASwBs9jTI9IYuQt1iBTBU3r2z5J-octdDlOzNknRzXKKz.png)

#### Pestañas hijas

Como último método de navegación, el popup permite filtrar registros en función de un registro padre. Esto puede ser útil para buscar líneas eliminadas pertenecientes a un pedido de venta.

Hay dos formas posibles en función del estado del registro padre: aún existente o ya eliminado.

Si el registro padre (p. ej., un Pedido de venta) todavía existe, entonces pueden realizarse los siguientes pasos para ver sus líneas eliminadas:

1. Vaya a la pestaña de líneas del Pedido de venta
2. Haga clic en el icono de histórico de auditoría para abrir la vista de historial del registro
3. Utilice los enlaces de 'Registros eliminados' para cambiar a la vista de registros eliminados

Como la pestaña de líneas no es una pestaña de nivel superior (tiene una pestaña padre Pedido de venta), la vista de registros eliminados se filtra automáticamente para mostrar solo las líneas pertenecientes al Pedido de venta actual. Como información visual de que la información mostrada está filtrada, el área de información superior muestra:

![](../../../../../assets/drive/TLPq4qy1yN9UkGD66_5njmuYw_ks8rUXRuOSuS6oXS_BmY92i1kLNyPns4CRsopMKIif0JPp6uJfWpDHgeKgtD07RAR8XcmrVEafUyhiVJ-OEUHhxUF3i77gURAyQPl8yK7PZMLk.png)

Si el registro padre (p. ej., un Pedido de venta) ya no existe, entonces se puede lograr lo mismo siguiendo estos pasos:

1. Vaya a la vista de Registros eliminados de la pestaña Pedido de venta
2. Busque el Pedido de venta para el que deben mostrarse las líneas eliminadas
3. Haga clic en el enlace Líneas justo debajo de la cuadrícula

Entonces, la vista de registros eliminados mostrará las líneas eliminadas pertenecientes al Pedido de venta (eliminado) seleccionado.

## Una ventana de Histórico de auditoría generada

La segunda interfaz para ver los datos de auditoría es una ventana normal generada que se basa en la entidad AuditTrail y permite explorar toda la información de auditoría filtrada por el cliente actualmente activo. Abra el menú Aplicación y navegue a Configuración General, Seguridad y seleccione Histórico de auditoría.

Ofrece una vista en bruto de los datos de auditoría, lo que significa que no se realiza ninguna traducción de valores en bruto, sino que se muestran los valores de columna en bruto de cada cambio.

Simultáneamente, esta ventana permite un filtrado/búsqueda mucho más flexible.

![](../../../../../assets/drive/rw7tPRLbT6ngBKyscK7lPe8F8irNUTp74vKBpDDST539eM5zHpl99Sr2fMXFLMcFks6BVhyNsMfFaSeWHgHYSr2vF2GDYjZ6a5fyAa3Nj2QEcpUhGAL6xOPIVwY177LL6kESljcr.png)

## Limitaciones

La funcionalidad de histórico de auditoría registrará todos los cambios de datos (para la tabla para la que se ha habilitado) con las siguientes excepciones:

- los campos de texto de tipos (char,varchar) con una longitud >= 4k no se auditarán
- los campos de texto de tipos (nchar,nvarchar) con una longitud >= 2k no se auditarán
- los campos BLOB (binarios almacenados dentro de la base de datos) no se auditarán

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