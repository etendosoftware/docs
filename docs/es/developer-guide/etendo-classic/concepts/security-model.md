---
title: Modelo de seguridad
tags:
    - Seguridad
    - Modelo
    - Servlets
    - Data Access Layer

status: beta
---

# Modelo de seguridad

!!! example  "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.
  
## Visión general

Esta sección analiza cómo los diferentes conceptos de seguridad de Etendo influyen en el desarrollo en Etendo.

El concepto de seguridad de Etendo consta de tres partes principales:

- Multi-Client/Multi-organization: define qué entidad/organizaciones son visibles para un usuario y referenciables desde otras entidad/organizaciones. 
- Nivel de acceso a datos (de una tabla): define la entidad/organización permitida para los datos almacenados en una tabla específica. Consulte el campo nivel de acceso de `AD_Table`. 
- Definición de acceso: Etendo dispone de varias definiciones de acceso, que permiten un control de acceso granular; consulte las tablas del paquete `org.openbravo.model.ad.access`. 

Esta sección tratará la seguridad y las definiciones de acceso desde la perspectiva de un desarrollador. Cuando sea necesario, se utilizarán referencias a la documentación funcional.

El desarrollador puede trabajar en dos modos en Etendo:

1. Tradicional: usando sqlc, etc. 
2. Capa de acceso a datos: usando la nueva capa de acceso a datos. 

Ambos enfoques se analizan por separado.

## Conceptos de seguridad y los Servlets de Etendo

Las tablas del paquete `org.openbravo.model.ad.access` definen el control de acceso para ventanas/solapas, procesos, flujo de trabajo, etc.

Las comprobaciones de seguridad que usan esta tabla están implementadas por el servlet `HttpSecureAppServlet`. Cualquier servlet que extienda esta clase heredará automáticamente esta implementación de seguridad.

## Conceptos de seguridad y XSQL y código manual

Etendo proporciona una forma estándar de ampliar consultas SQL con filtros para entidades y organizaciones accesibles. Esto se analiza en detalle en esta sección de la guía del desarrollador:

- [Definición de XSQL](../concepts/multi-client-and-multi-org.md#xsql---definition)
- [Uso de XSQL en Java](../concepts/multi-client-and-multi-org.md#xsql---java-usage) 

## Conceptos de seguridad y la Data Access Layer

Para el desarrollador, la [Data Access Layer](../concepts/data-access-layer.md) proporciona varias interfaces ([OBCriteria](https://github.com/etendosoftware/etendo_core/blob/main/src/org/openbravo/dal/service/OBCriteria.java){target="\_blank"} y [OBQuery](https://github.com/etendosoftware/etendo_core/blob/main/src/org/openbravo/dal/service/OBQuery.java){target="\_blank"}) que se encargan automáticamente de aspectos específicos de seguridad:

- filtro para `clients`/`organizations` legibles 
- filtro para tablas legibles (basado en `AD_Window_Access`) 

Además, se realizan comprobaciones al recuperar el valor de una propiedad. La capa de acceso a datos distingue entre los dos siguientes modos de lectura (a nivel de objeto):

- legible directo: todas las propiedades del objeto son legibles; esta legibilidad está definida por la tabla `AD_Window_Access` 
- legible derivado: solo son legibles las propiedades id e identificador; las entidades legibles derivadas son las entidades que no son directamente legibles, pero a las que se hace referencia desde entidades directamente legibles. 

La **DAL** también comprueba el acceso de escritura al cambiar propiedades de un objeto de negocio. El acceso de escritura también se comprueba cuando un objeto se guarda en la base de datos. Se realizan las siguientes comprobaciones:

- el usuario tiene acceso de escritura a la `client`/`organization` 
- el usuario tiene acceso de escritura a la tabla del objeto (definida en la tabla `AD_Window_Access`) 
- la `client`/`organization` del objeto se ajusta al nivel de acceso de la tabla
- el objeto solo hace referencia a otros objetos que están en el árbol natural de organizaciones del propio objeto 

La capa de acceso a datos también realiza comprobaciones específicas de autorización cuando se elimina un objeto: el usuario debe tener acceso al objeto y este debe ser eliminable.

!!! info 
    - Para mucha más información sobre cómo la **Data Access Layer** implementa la seguridad, consulte [este enlace](./data-access-layer.md#security-and-validation).
    - Para más información sobre la **Data Access Layer y multi-client/multi-organization**, consulte [este enlace](./multi-client-and-multi-org.md#data-access-layer).

## Administradores de la aplicación

Existe un indicador de administrador en la ventana **Rol** que permite a los usuarios realizar configuraciones en diferentes niveles en función de su rol.

Hay 4 niveles diferentes en Etendo:

**Nivel de Sistema**

- No existe indicador para el nivel de **Sistema**. 
- Los usuarios que inician sesión como **Administrador del Sistema** pueden configurar ajustes a nivel de **Sistema**. 
- Estos ajustes estarán disponibles para todos. 

**Nivel de entidad**

- Existe un nuevo indicador **Administrador de la Entidad** en la solapa **Rol**. 
- Los usuarios pueden configurar ajustes a nivel de entidad si el rol con el que han iniciado sesión tiene el indicador habilitado. 
- Estos ajustes están disponibles para todos los usuarios de la entidad del rol. 

**Nivel de organización**

- Existe un nuevo indicador **Administrador de la Organización** en la solapa **Permiso a organizaciones**. 
- Los usuarios pueden configurar ajustes a nivel de organización en todas las organizaciones del rol con el que han iniciado sesión que tengan el indicador habilitado. 
- Estos ajustes están disponibles para todos los usuarios que inicien sesión en esa organización. 

**Nivel de rol**

- Existe un nuevo indicador **Administrador de Rol** en la solapa **Asignación de usuario**. 
- Los usuarios pueden configurar ajustes a nivel de **Rol** en todos los roles a los que esté asignado con el indicador habilitado. 
- Estos ajustes están disponibles para todos los usuarios que inicien sesión con ese rol. 

### Actualización desde MPs anteriores

Cuando se crea un rol manualmente, todos los indicadores se establecen en false de forma predeterminada. Existe un script de módulo definido para establecer en true los indicadores según las siguientes reglas:

**Administrador de la Entidad**

- Todos los roles con acceso a la organización **(*)** y al formulario **Configuración inicial de entidad y organización**. 

**Administrador de la Organización**

- Todas las organizaciones asignadas de un rol con acceso al formulario **Configuración inicial de entidad y organización**. 

**Administrador de Rol**

- Todos los roles asignados a un usuario si al menos uno de los roles tiene acceso a la ventana **Rol**. 

Tenga en cuenta que este script de módulo solo rellena los indicadores la primera vez que se añaden estos indicadores. En las siguientes actualizaciones del core, los indicadores no se actualizarán y la configuración deberá realizarse manualmente.

### Roles creados por la configuración inicial de entidad y organización

Los formularios **Configuración inicial de entidad** y **Configuración inicial de organización** crean automáticamente algunos usuarios y roles. Estos tienen el indicador inicializado a true.

**Configuración inicial de entidad**

- El rol creado tiene el indicador **Administrador de la Entidad** establecido en true. 
- El usuario creado tiene asignado el nuevo rol con **Administrador de Rol** establecido en true. 

**Configuración inicial de organización**

- El rol y la organización creados tienen el indicador **Administrador de la Organización** establecido en true. 
- El usuario creado tiene asignado el nuevo rol con **Administrador de Rol** establecido en true. 


---

Este trabajo es una obra derivada de [Modelo de seguridad](http://wiki.openbravo.com/wiki/Security_Model){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, usado bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.