---
tags:
  - Gestión de bases de datos  
  - Herramientas de base de datos
  - PostgreSQL
  - Particionado de tablas
  - Tabla
status: beta
---

# Utilidades ampliadas de base de datos (BETA)

:octicons-package-16: Javapackage: `com.etendoerp.db.extended`


!!! example  "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    - Está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úselo **bajo su propia responsabilidad**, especialmente en entornos de producción.
    - Debe utilizarse con **precaución**, y siempre debe **validar las copias de seguridad** antes de ejecutar cualquier operación crítica.

## Visión general

El módulo **Utilidades ampliadas de base de datos** añade herramientas avanzadas de PostgreSQL a Etendo para gestionar **tablas particionadas**. El particionado divide grandes conjuntos de datos en segmentos más pequeños, mejorando el rendimiento, la escalabilidad y la mantenibilidad.

Esta guía cubre los requisitos, la configuración y el uso para particionar y desparticionar tablas.

### ¿Por qué particionar?

- **Consultas más rápidas** al escanear solo las particiones relevantes.  
- **Mantenimiento más sencillo** mediante una organización lógica de los datos.  
- **Crecimiento escalable** sin degradar el rendimiento.

### Recomendaciones

- Cree siempre una **copia de seguridad completa de la base de datos** antes de realizar cambios.  
- Planifique una **estrategia de particionado** clara basada en el uso de los datos y las tablas críticas.
- Pruebe exhaustivamente primero en **entornos no productivos**.   

## Requisitos

Deben cumplirse los siguientes requisitos antes de usar el módulo:

- **[Etendo 25](../../../whats-new/release-notes/etendo-classic/release-notes.md)** o superior.
- **[Python 3](https://docs.python.org/3.13/){target="_blank"}** – última versión de la rama 3.
- **[PostgreSQL](https://www.postgresql.org/docs/16/index.html){target="_blank"}** – versión 16 o superior.
- **Etendo DBSM (Database Source Manager)** – versión **1.2.0-beta**, configurada en el archivo `artifacts.list.COMPILATION.gradle` dentro del entorno de Etendo. 

## Instalación del módulo

1. Clone el código del módulo en la carpeta `/modules` dentro del entorno de Etendo:

    ```bash title="Terminal"
    cd modules
    git clone git@github.com:etendosoftware/com.etendoerp.db.extended.git
    ```

2. Compile el entorno.

    ```bash
    ./gradlew update.database smartbuild
    ```

## Configuración del entorno Python

Para preparar el entorno Python necesario para este módulo:

1. Cree un entorno virtual:

    ```bash title="Terminal"
    python3 -m venv modules/com.etendoerp.db.extended/.venv
    ```

2. Active el entorno virtual:

    ```bash title="Terminal"
    source ./modules/com.etendoerp.db.extended/.venv/bin/activate
    ```

3. Instale los paquetes de Python requeridos:

    ```bash title="Terminal"
    pip3 install pyyaml psycopg2-binary
    ```

## Particionar una tabla

El particionado de una tabla altera su estructura física para mejorar el rendimiento de las consultas en conjuntos de datos muy grandes. Este proceso debe ejecutarse con precaución y requiere los permisos adecuados.

### Ventana Configuración de tabla particionada

:material-menu: `Aplicación`> `Partición`> `Configuración de tabla particionada`

![Configuración de tablas particionadas](../../../assets/developer-guide/etendo-classic/developer-tools/partitioned_tables_config.png)

1. Inicie sesión como **Administrador del sistema**.
2. Acceda a la ventana **Configuración de tabla particionada**.
3. Defina cómo deben particionarse las tablas:

    - Cree un nuevo registro de configuración.
    - Seleccione la tabla que desea particionar.
    - Elija una columna para el particionado (**debe referenciar una fecha**).
    
        !!! Question "¿Por qué una referencia de fecha?"
            Esto se debe a que el script de particionado utiliza la columna seleccionada para extraer el año de cada registro y, a continuación, agrupa los datos en particiones basadas en ese año. Por lo tanto, la columna debe tener una referencia de fecha.

    - Guarde la configuración.


### Aplicar el particionado

1. Detenga el **servidor Tomcat**.
2. Ejecute los siguientes comandos para particionar la(s) tabla(s):

    ```bash title="Terminal"
    python3 modules/com.etendoerp.db.extended/tool/migrate.py
    ./gradlew update.database -Dforce=yes smartbuild
    ```

    - El primer comando ejecuta el proceso de particionado basado en la configuración establecida en el diccionario de datos.
    - El segundo comando actualiza la base de datos regenerando las estructuras de tablas para reflejar el particionado.

        !!! note
            Aquí se ejecuta un `update.database` forzado porque, tras particionar una tabla, la estructura de la base de datos cambia debido a que una o más tablas pasan a estar particionadas. Este paso garantiza que la estructura actualizada se aplique correctamente, incluyendo el manejo de tablas particionadas, que el **DB Source Manager** predeterminado no gestionaría adecuadamente.


## Desparticionar una tabla

Antes de iniciar el desarrollo, las tablas deben estar **sin particionar** porque la tarea `export.database` no admite tablas particionadas.

La herramienta de desparticionado restaura las tablas a su estado original, sin particionar, garantizando la compatibilidad con los flujos de trabajo de desarrollo.

!!! warning
    La tarea `export.database` no puede ejecutarse sobre tablas particionadas. Desparticione siempre las tablas necesarias antes de ejecutar esta tarea.

### Pasos para desparticionar una tabla

1. Ejecute el siguiente comando, sustituyendo "table_name1", "table_name2", etc., por el nombre de la(s) tabla(s) que desea desparticionar.

    !!!info 
        Es posible desparticionar una o varias tablas listando sus nombres separados por comas (sin espacios entre nombres).

    ```bash
    python3 modules/com.etendoerp.db.extended/tool/unpartition.py "table_name1,table_name2,..."
    ```

    **Ejemplo:**

    - Desparticionar una única tabla:

        ```bash
        python3 modules/com.etendoerp.db.extended/tool/unpartition.py "c_order"
        ```

    - Desparticionar varias tablas:
    
        ```bash
        python3 modules/com.etendoerp.db.extended/tool/unpartition.py "c_order,c_invoice"
        ```

2. Regenerar la estructura de la base de datos:

    Tras desparticionar, ejecute el siguiente comando para actualizar los metadatos de la base de datos:

    ```bash
    ./gradlew update.database -Dforce=yes smartbuild
    ```

    Este paso restaura la base de datos a un estado consistente y funcional al reflejar los cambios realizados durante el proceso de desparticionado.

!!!warning  "Este módulo está en fase `BETA`"
    El comportamiento del módulo puede cambiar sin previo aviso. No lo utilice en entornos de producción sin una validación exhaustiva.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.