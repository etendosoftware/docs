---
title: Cómo crear un proceso de escaneo
tags:
    - Cómo hacer
    - Proceso de escaneo
    - Definición del Proceso
---

## Visión general

Este documento explica cómo definir un proceso de escaneo que pueda ejecutarse desde la aplicación móvil para escanear códigos utilizando la cámara del móvil.

Es importante tener en cuenta que cualquier proceso de escaneo **debe tener** estos pasos específicos:

- **Agrupador:** Los elementos que se van a escanear deben agruparse bajo un contenedor.
- **Elementos**: Aquí puede escanear diferentes tipos de códigos de barras (en todas las codificaciones) o QR que representen diferentes elementos como productos, facturas, activos, etc...

Opcional:

- Cantidad: Es posible especificar la cantidad de los elementos escaneados.

## Definición del proceso de escaneo en Etendo

!!! warning
    El entorno debe tener al menos un módulo en desarrollo, y el identificador del proceso debe incluir el prefijo de ese módulo.

1. En primer lugar, debe crear un proceso. Inicie sesión como "Administrador del sistema". Abra la ventana `Application` > `Application Dictionary` > `Definición del Proceso` y cree un nuevo registro.

    ![scanprocessdefinition.png](../../../assets/legacy/technicaldocumentation/platform/scanprocessdefinition.png)

    - **Módulo**: Hace referencia al módulo donde se añadirá el proceso.
    - **Identificador**: Es el identificador utilizado para guardar el proceso en la base de datos.
    - **Nombre**: Es el nombre asignado al proceso, que se mostrará en la aplicación.
    - **Patrón de la Interfaz de Usuario**: debe seleccionar estándar.
    - **Handler**: aquí se introduce la clase Java que se ejecuta cuando se invoca el proceso.
    - **Acceso a datos**: debe seleccionar Entidad/Organización.
    - **Ayuda/Comentario**: Esta sección se muestra cuando se inicia el proceso. Describe brevemente al usuario de qué tratará el proceso.
    - **Parámetro**:
    - **Módulo**: Módulo al que pertenece el parámetro; por defecto es el mismo que el asignado al proceso padre.
    - **Nombre**: Es el nombre que se mostrará dentro de las entradas en la aplicación móvil.
    - **Nombre columna BD**: Es el nombre con el que el parámetro se almacena en la base de datos.
    - **Secuencia**: Es un identificador del orden en el que se muestran los campos.
    - **Referencia**: Es un identificador del tipo de referencia almacenada.
    - **Referencia clave**: Es el tipo específico de los datos referenciados.
    - **Elemento del sistema**: Este campo hace referencia al tipo de datos asociado al parámetro.
    - **Ayuda/Comentario**: Debe completarse en caso de que quiera mostrar ayuda sobre cómo continúa el proceso cuando se muestra el parámetro.


    !!! info
        Es importante definir todos los parámetros especificados en la captura de pantalla, y con los mismos tipos de referencias, para que el proceso móvil se comporte correctamente.  
        El nombre de cada parámetro debe personalizarse para cada proceso.
        Opcional: Es posible añadir un selector (en caso de que el elemento a escanear tenga selectores definidos) y el parámetro de cantidad (para definir la cantidad de elementos escaneados).

2. Defina una columna de BD en la tabla en la que quiera añadir un proceso de escaneo, para añadir un botón que ejecute el proceso. Por ejemplo:

    ```sql
    ALTER TABLE a_asset ADD COLUMN smfms_scan_process CHARACTER(1);
    ```

3. Para asociar el proceso con el botón, abra `Aplication` > `Aplication Dictionary` > `Tables and Colums`, busque la tabla y pulse **CREAR COLUMNAS DE LA BASE DE DATOS**. Este proceso creará la columna.

4. Cambie la **referencia** a Botón y en **Definición del Proceso** seleccione el proceso creado recientemente.

    ![scanprocess2](../../../assets/developer-guide/etendo-classic/how-to-guides/scanprocess2.png)

5. En `Application` > `Application Dictionary` > `Windows,Tabs and Fields`, busque las ventanas donde quiera el proceso.
   Por ejemplo, busque **ventanas de activos** y luego el **campo de escaneo de activos** en la búsqueda de la solapa principal. Desmarque "Mostrado" (porque el escaneo solo debe mostrarse en la aplicación móvil).

    ![sacnprocess1](../../../assets/developer-guide/etendo-classic/how-to-guides/scanprocess1.png)


!!! success
    Cuando el proceso se ejecuta desde la aplicación móvil, se enviará un JSON al backend con toda la información escaneada. Estos datos deben procesarse desde la clase Java definida en el handler y debe ejecutarse la funcionalidad esperada.
    Un ejemplo de esta clase Java es `InventoryScan`, que puede encontrarse en el módulo `com.smf.mobile.scan`.

---
Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L](https://etendo.software){target="_blank"}.