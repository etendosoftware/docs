---
title: Cómo modularizar el Selector de ubicación
tags:
    - Selector de ubicación
    - Modularización
    - Modularizar
    - Personalizar

status: beta
---

# Cómo modularizar el Selector de ubicación

!!! example "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.

## Visión general

En esta sección se explica cómo modificar y modularizar el **Selector de ubicación**.

## Artículos recomendados

Antes de leer esta guía, es necesario tener una comprensión adecuada del concepto de [Modularidad](../concepts/modularity-concepts.md) de Etendo y de [cómo crear un módulo](../how-to-guides/how-to-create-a-module.md), ya que en esta guía se da por supuesto el conocimiento de estos artículos.

En caso de que trabaje con scripts de configuración o plantillas de forma habitual, el siguiente enlace a un artículo podría ser de su interés, ya que describe [cómo crear un script de configuración](../how-to-guides/how-to-create-a-configuration-script.md).

## Pasos de ejecución

Los pasos necesarios para cambiar y modularizar el **Selector de ubicación** son los siguientes:

1. Defina su propio **Módulo** y expórtelo. A continuación se generará la carpeta del módulo, por ejemplo:

    ```
    modules/com.etendoerp.locationexample/
    ```

2. Cree la carpeta de código fuente para el **Módulo** que acabamos de crear previamente. Para nuestro ejemplo, debería verse así:

    ```
    src/ com/etendoerp/locationexample/info/
    ```

3. Copie los archivos originales del Selector de ubicación en la carpeta recién creada. Al copiar los archivos, mantenga los nombres de archivo originales. Los archivos originales se encuentran en:

    ```
    src/org/openbravo/erpCommon/info/Location
    ```

4. Modifique los siguientes archivos para que formen parte de su paquete:

    - **Location_Search_data.xsql**: cambie el paquete definido a: `com.etendoerp.locationexample.info`
    - Cambie el paquete a: `com.etendoerp.locationexample.info`

        Cambie los siguientes mapeos para usar los nuevos mapeos:

        ````
        org/openbravo/erpCommon/info/Location_FS ->  com/etendoerp/locationexample/info/Location_FS
        org/openbravo/erpCommon/info/Location_F1 ->  com/etendoerp/locationexample/info/Location_F1
        org/openbravo/erpCommon/info/Location_F2 ->  com/etendoerp/locationexample/info/Location_F2
        ```

    Después de eso, puede aplicar todos los cambios que desee realizar. En nuestro ejemplo, solo hemos cambiado las etiquetas de los campos.

    !!! note

        Existe un **disparador** `c_bpartner_location_trg` que inserta el nombre de la ubicación en el campo de nombre del `c_bpartner_location` después de cualquier cambio. Ese nombre se crea utilizando la **función** `c_location_name`.

        Si añade nuevos campos en el Selector de ubicación y también quiere usar la información para componer el nombre, deberá hacer lo siguiente:

        - Crear su propia **función** basada en `c_location_name` para componer el nombre que desea guardar.
        - Crear su propio **disparador** basado en `c_bpartner_location_trg` para usar esa nueva función para guardar el nombre.
        - Desactivar el **disparador** `c_bpartner_location_trg` y usar el suyo propio en su lugar.

        Para desactivarlo, tiene que eliminarlo y luego exportar los cambios en una **Plantilla** configurada como `In Development`. En la parte superior de la plantilla `configScript.xml` verá que hay una línea que indica que el disparador fue eliminado (`RemoveTriggerChange`).

5. Cree una nueva referencia de búsqueda para los nuevos archivos de su módulo y con su propio nombre. Defina esa nueva referencia para que use su propia clase Java y sus propios mapeos:

    ![texto alternativo](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-modularize-the-location-selector/how-to-modularize-the-location-selector-1.png)

    ![texto alternativo](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-modularize-the-location-selector/how-to-modularize-the-location-selector-2.png)

6. Defina un nuevo módulo de plantilla y márquelo como `In Development`. Puede usar la plantilla que utilizamos para desactivar el disparador: en la ventana **Tablas y columnas**, busque la columna que desea usar con el Selector de ubicación que hemos creado y cambie el desplegable **Searchkey de referencia** para usar esta nueva referencia. En el ejemplo lo hemos hecho en la tabla `C_Bpartner_location`, en la columna `c_location_Id`.

7. Compile la aplicación con:

    ```   
    ./gradlew smartbuild
    ```

8. Reinicie tomcat y use la columna para comprobar que la nueva referencia está funcionando con los nuevos cambios.

    Los resultados de nuestros cambios son:

    ![texto alternativo](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-modularize-the-location-selector/how-to-modularize-the-location-selector-3.png)

---
Este trabajo es una obra derivada de [How To Modularize The Location Selector](https://wiki.openbravo.com/wiki/How_To_Modularize_The_Location_Selector){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.