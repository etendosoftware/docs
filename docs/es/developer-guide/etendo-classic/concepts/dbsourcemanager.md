---
title: DBSourceManager
tags:
    - DBSourceManager
    - Arquitectura
    - Biblioteca Java
    - Base de datos

status: beta
---

#  DBSourceManager

!!! example  "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.

##  Visión general

**DBSourceManager** es una biblioteca Java que ayuda con tareas de base de datos relacionadas con el desarrollo. Su funcionalidad más importante es la independencia de la base de datos. Usted podrá centrarse en el desarrollo de funcionalidades de base de datos y dejar que DBSourceManager se encargue de los detalles de implementación de la base de datos.

DBSourceManager se basa en [DDLUtils](https://db.apache.org/ddlutils/){target="\_blank"} y el modelo de base de datos utilizado por DBSourceManager es una extensión del modelo utilizado por **DDLUtils**. DDLUtils soporta una amplia lista de motores de base de datos, pero todas las extensiones creadas en DBSourceManager solo funcionan para **Oracle** y **PostgreSQL**.

El objetivo principal de DBSourceManager es ayudar al desarrollador en la creación y el mantenimiento de objetos físicos de base de datos y datos. La forma en que esto funciona es mediante un conjunto de archivos `XML` que representan objetos físicos de base de datos o registros de tablas. DBSourceManager contiene utilidades que permiten al desarrollador exportar sus objetos a estos archivos `XML`, y que permiten que las modificaciones realizadas en estos archivos `XML` se trasladen a la base de datos actualizándola.

Por lo tanto, el desarrollador puede centrarse en crear y cambiar sus componentes (ya sea en la base de datos o en los archivos `XML`), y DBSourceManager puede trasladar automáticamente los cambios de un lugar al otro.

##  Arquitectura

Como se indicó anteriormente, **DBSourceManager** se basa en el proyecto Apache ddlutils. Internamente, su estructura puede describirse como una serie de clases para gestionar el modelo de base de datos y una serie de clases relacionadas con cómo los objetos y sus cambios se transforman en comandos específicos del RDBMS.

##  Tareas comunes

Las principales tareas que DBSourceManager permite realizar al desarrollador son las siguientes:

* **`export.database`** : esta tarea genera archivos `XML` correspondientes a los objetos físicos de base de datos y al contenido de las tablas del Diccionario de Aplicación. 
* **`update.database`** : esta tarea actualiza la base de datos aplicando los cambios necesarios para transformarla de modo que siga el modelo descrito en los archivos `XML`. 
* **`export.config.script`** : esta tarea genera un script de configuración del sistema actual.

Para más información sobre las tareas de compilación de Etendo, visite [Tareas de compilación de desarrollo](../developer-tools/etendo-gradle-plugin.md#build-tasks). Estas tareas están relacionadas con los [conceptos de modularidad](../concepts/modularity-concepts.md) en Etendo.

##  Más información

DBSourceManager utiliza un mecanismo denominado **Filtros de modelo**, para eliminar intencionadamente algunos objetos no deseados del modelo físico de base de datos. Estos filtros pueden ampliarse mediante módulos. Para saber cómo, puede leer [Cómo excluir objetos físicos de base de datos del modelo](../how-to-guides/how-to-exclude-database-physical-objects-from-model.md).

---

Este trabajo es una obra derivada de [DBSourceManager](http://wiki.openbravo.com/wiki/DBSourceManager){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.