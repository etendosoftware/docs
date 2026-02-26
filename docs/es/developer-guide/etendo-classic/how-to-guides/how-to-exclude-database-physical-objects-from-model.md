---
tags:
  - Cómo hacer
  - Etendo Classic
  - Modelo
  - Base de datos
  - Excluir
  - Objetos físicos
---

# Cómo excluir objetos físicos de la base de datos del modelo

## Visión general

Etendo Classic realiza el seguimiento de los objetos físicos de la base de datos (como tablas, vistas, funciones, secuencias o triggers) mediante una utilidad llamada `dbsourcemanager`. Esta utilidad es capaz de exportar todas las definiciones de objetos del modelo de base de datos a archivos `XML`, que se almacenan en la carpeta `src-db/database/model` (tanto en Core como en los módulos).

Esta herramienta está diseñada para funcionar en un entorno multiplataforma, compatible tanto con Oracle como con PostgreSQL. Esto significa que, en ocasiones, si se utiliza sintaxis o funcionalidades específicas de un Sistema de Gestión de Bases de Datos en particular, es posible que la herramienta no las soporte.

En estos casos, un enfoque posible es crear estos objetos específicos utilizando un Script de Módulo (puede encontrar más información sobre ellos [aquí](../how-to-guides/how-to-create-build-validations-and-module-scripts.md)) y, a continuación, excluirlos del modelo físico de base de datos de Etendo Classic.

## Excluir objetos en módulos

Los objetos se excluyen mediante un archivo llamado `excludeFilter.xml`. Este archivo debe ubicarse dentro de la carpeta `src-db/database/model/` del módulo (si no existe, deberá crearlo) y sigue un formato XML muy sencillo. A continuación se muestra un ejemplo:

```xml
    <?xml version="1.0"?>
      <vector>
        <excludedTable name="TEST_TABLE"/>
        <excludedView name="TEST_VIEW"/>
        <excludedFunction name="TEST_FUNCTION"/>
        <excludeColumn name="TEST_COLUMN"/>
        <excludeConstraint name="TEST_CONSTRAINT"/>
        <excludedTrigger name="TEST_TRIGGER"/>
        <excludedSequence name="TEST\_%"/>
      </vector>
```

Este archivo excluirá del modelo la tabla **TEST_TABLE**, la vista **TEST_VIEW**, la función **TEST_FUNCTION**, la columna **TEST_COLUMN**, la restricción **TEST_CONSTRAINT** y el trigger **TEST_TRIGGER** y, por lo tanto, no se exportarán, ni se eliminarán, ni se modificarán de ninguna manera durante las tareas normales de gestión de base de datos (`update.database` y `export.database`).

Se admite el uso de [comodines SQL](https://www.w3schools.com/sql/sql_wildcards.asp){target="\_blank"}, por lo que se aplicará el mismo tratamiento a todas las secuencias cuyo nombre comience por **TEST_**. Todas las exclusiones cuyo nombre contenga el carácter `%` se tratarán como comodines. Al definir una exclusión usando un comodín, recuerde escapar con una barra invertida los caracteres `_`, salvo que se pretenda utilizarlos como sustituto de cualquier carácter individual.

---

Este trabajo es una obra derivada de [Cómo excluir objetos físicos de la base de datos del modelo](https://wiki.openbravo.com/wiki/How_to_exclude_Database_Physical_Objects_From_Model){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.