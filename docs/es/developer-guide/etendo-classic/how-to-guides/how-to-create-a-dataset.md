---
title: Cómo crear un conjunto de datos
tags:
    - Cómo hacer
    - Conjunto de datos
    - Acceso datos
    - Conjunto de datos del módulo
    - Datos de referencia
---

# Cómo crear un conjunto de datos
  
##  Visión general

Este procedimiento se centrará en crear un conjunto de datos en Etendo Classic y también proporcionará algunos ejemplos en detalle en la sección Ejemplos. El conjunto de datos exportará tanto datos de referencia como datos por defecto.

###  Introducción al concepto de conjunto de datos

En primer lugar, es necesario comprender el concepto de conjunto de datos, que permite exportar los conjuntos de datos de diferentes tablas en un solo paso. Esto es especialmente útil para gestionar y distribuir el módulo junto con _datos de referencia_, por ejemplo tipos impositivos, regiones o _datos por defecto_ en una(s) nueva(s) tabla(s) añadida(s) por un módulo.

Un conjunto de datos se define por sus Tablas de conjunto de datos y Columnas de conjunto de datos. Esta configuración detallada determina qué tablas se exportarán y qué columnas de cada tabla se ejecutan y se exportan.

Hay algunas cosas importantes a tener en cuenta:

  * Un conjunto de datos pertenece a un módulo, por lo que los módulos pueden añadir Conjuntos de datos y definir sus propios Conjuntos de datos. 
  * Acceso datos: filtra las tablas que se pueden seleccionar para este conjunto de datos; solo las tablas con el nivel de acceso a datos establecido pueden incluirse en el conjunto de datos.   
  
###  Datos de referencia

Los datos de referencia se publican, distribuyen e instalan junto con la implementación del código del programa del módulo.

En Etendo, el concepto de datos de referencia está generalizado y cualquier dato de la instancia puede exportarse en un módulo e importarse al instalar / aplicar el módulo.

!!!note
    Puede encontrar el campo / opción _Tiene datos de referencia_ en el momento de la creación del módulo.

!!!info
    Para conceptos teóricos detallados sobre conjuntos de datos, consulte [Conjunto de datos](../../../developer-guide/etendo-classic/concepts/datasets.md).
##  Estructura de datos para definir un Conjunto de datos

Existen principalmente tres tablas a las que se hace referencia como estructura de datos para definir conjuntos de datos. Son:

1. 
    * DataSet con las siguientes columnas: _Value, Name, Description, Module y Acceso datos_
    * Los conjuntos de datos tienen un nombre y una descripción para describir el contenido del conjunto de datos. 
    * El valor se utiliza para obtener un objeto `dataSet` desde la factoría proporcionada por DAL (p. ej., `DBSourceManager` obtiene el `AD` `dataSet`). 
    * Un conjunto de datos pertenece a un módulo del mismo modo que todos los componentes del Diccionario de Aplicación. 

    ![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Dataset-2.png)

    !!!note
    Si la columna de permitir exportación está marcada, entonces se muestra un botón **Exportar Datos de Referencia**. 
    

2. 
    * DataSet_Table* con las siguientes columnas: _DataSet, Table, fullBusinessObject, Incluir Todas las Columnas, excludeAuditInfo y whereClause (HQLexpression)_
    * Un conjunto de datos puede tener una o varias tablas de las registradas en `AD_Table`. Para cada una de ellas, los desarrolladores pueden decidir incluir solo registros de esa tabla o exportar el objeto de negocio completo usando la casilla `fullBusinessObject`. 
    * Los desarrolladores también pueden definir, para cada tabla, las columnas que se incluyen en el conjunto de datos. Pueden incluir todas las columnas usando la casilla `includeAllColumns` y después eliminar algunas de ellas en la definición de columnas, o bien incluir únicamente las que se definan explícitamente en la definición de columnas. 
    * The whereClause is a *HQL expression* para filtrar las filas que se incluyen en el DataSet. Los detalles sobre esta expresión se proporcionarán en el proyecto DAL. 
    * Los desarrolladores pueden excluir las columnas de información de auditoría como _created, createdby, updated, etc._ marcando la columna `excludeAuditInfo`. 

    ![](../../../assets/developer-guide/etendo-classic/how-to-guides/how_to_create_a_Dataset-3.png)  
    
    !!!note 
        Si el campo IsBusinessObject está marcado, entonces se exportan los ` child-records ` de la tabla.
        Por ejemplo, si la tabla del conjunto de datos está definida para la tabla ` C_Order ` y este campo está marcado, entonces también se exportan los ` C_OrderLines ` relacionados. 
  
    !!!info
        Un objeto de negocio completo es un registro que incluye todas sus relaciones uno-a-muchos
        tal y como se definen en el AD mediante el atributo isParent de una columna. Un ejemplo de
        un objeto de negocio completo es un producto con sus proveedores, precios, etc. En el proyecto DAL
        se proporciona una descripción completa de los objetos de negocio.

3. 
    * Dataset_column* con las siguientes columnas: *DataSet_Table, Column, isExcluded y conditionClause (Java expression).
    * Para cada tabla de un conjunto de datos, los desarrolladores pueden decidir qué columnas incluir de entre las registradas en el AD para esa tabla. 
    * Pueden excluir columnas usando la casilla `isExcluded` si han marcado la tabla como _Incluir Todas las Columnas_ . Normalmente, la información de auditoría se eliminará del conjunto de datos. 

    ![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Dataset-4.png)   

###  Acceso datos

El Acceso datos se utiliza para definir cómo importar/instalar el módulo en varios niveles, como nivel de Sistema, nivel de Entidad, nivel de Organización, etc. Este valor de nivel de acceso está disponible en la tabla `Dataset`. 

Esta es una explicación detallada de cada nivel de acceso.

  * _Solo sistema:_ los datos se importarán en el momento de la instalación del módulo a nivel de Sistema sin ninguna interacción del usuario. 
  * _Entidad:_ los datos se importarán en `Initial Client Setup` si el usuario elige el módulo en el que se incluye el Conjunto de datos. 
  * _Organización:_ los datos se importarán en `Initial Organization Setup` si el usuario elige el módulo en el que se incluye el Conjunto de datos. 
  * _Entidad/Organización:_ los datos se importarán en `Initial Client Setup` o `Initial Organization Setup` si el usuario elige el módulo en el que se incluye el Conjunto de datos. El módulo no puede aplicarse en ambos niveles al mismo tiempo porque daría lugar a redundancia de datos. Por tanto, si el módulo se aplica a una Entidad no estará disponible para aplicarse en sus Organizaciones y, si el módulo se aplica en una Organización, no estará disponible para aplicarse en su Entidad. 
    
!!!info
    - La relación entre cada entrada de datos importada, el Conjunto de datos del que proviene 
    y el ID original que tiene en el XML del Conjunto de datos se puede encontrar en 
    la tabla `AD_Ref_Data_Loaded`.
    - Los datos de un Conjunto de datos que se importan por primera vez se crearán 
    **con el ID establecido en su archivo XML**. A partir de entonces, se creará un nuevo ID 
    para cada entrada.
    - La tabla `AD_Orginfo` contiene información sobre qué Conjunto de datos se ha importado 
    para qué entidad y/o organización
## Exportación del módulo

Antes de publicar, es necesario exportar el módulo, lo que crea un directorio en el módulo bajo el directorio raíz de Etendo Classic y los archivos XML adecuados para su inclusión en el módulo finalizado.

!!!note
    Los módulos que no estén marcados como en desarrollo no se exportan, por lo que recuerde que debe seleccionar la casilla de verificación **En desarrollo** cuando defina un nuevo módulo.

Cuando finalice el desarrollo del módulo, abra una ventana de comandos/shell y navegue hasta el proyecto de desarrollo de Etendo; a continuación, ejecute el comando `export.database`.

```bash title="Terminal"   
./gradlew export.database
```
## Publicación de un Módulo

El último paso del proceso es publicar el módulo y distribuirlo al usuario final.

!!!info
    Para una guía detallada sobre cómo hacerlo, visite [Cómo publicar módulos en un repositorio de GitHub](../../../developer-guide/etendo-classic/how-to-guides/how-to-publish-modules-to-github-repository.md)
## Ejemplos

A continuación, encontrará ejemplos para saber cómo crear un conjunto de datos y exportarlo junto con los datos de referencia.

### Conjunto de datos de roles y accesos

En esta sección puede encontrar el ejemplo de un conjunto de datos de roles y accesos. Básicamente cubre la definición del rol en la organización y los privilegios que requiere.

**Crear un rol y asignar privilegios**

  * Cambie al rol de administrador de su entidad.
  * Haga clic en `General Setup` y navegue a `Security` > `Role`.
  * Cree un nuevo registro. Rellene los campos obligatorios requeridos para este registro. Son:
    * `Name`: el nombre del rol en la organización del cliente, p. ej., Sales Clerk, Production Manager, Forecaster, etc.
    * `Active`: seleccione la opción para asegurar que este rol aparezca en la aplicación generada. Durante el desarrollo puede requerir que el rol solo aparezca cuando esté completo.
    * `User Level`: esto controla a qué organizaciones tiene acceso el rol. Hay cuatro opciones; las más comunes son:
        - `Organization`: el rol solo tiene acceso a datos específicos de la organización.
        - `Client and Organization`: el rol tiene acceso a datos específicos de la organización y a datos compartidos de la entidad.
    * `Manual`: controla si todos los privilegios existentes se conceden automáticamente al rol o si se asocian manualmente según sea necesario. Se recomienda seleccionar esta opción para control manual.
  * Guarde el registro.
  * Ahora necesita asignar algunos privilegios haciendo clic en el botón `Grant Access`.
  * Seleccione el módulo y el tipo de acceso para asignar los privilegios al rol recién creado.

#### Crear un usuario y asignar el usuario al rol

  * Haga clic en `General Setup` y navegue a `Security` > `User`.
  * Cree un nuevo registro. El campo `Client` mostrará el nombre de su entidad por defecto.
  * Seleccione la organización (esto puede ser para acceso a una o a todas las organizaciones de una entidad).
    - Nombre.
    - Apellido.
    - Nombre (por defecto).
    - Seleccione Activo (por defecto).
    - Nombre de usuario (por defecto es una concatenación del nombre y el apellido).
    - Introduzca la contraseña del usuario (recuerde esto).
  * Guarde el registro.

  * Vuelva a situarse en la ventana `User`.
  * Seleccione la solapa `User Roles`.
  * Cree un nuevo registro y seleccione un rol.
  * Guarde el registro.
  * Añada todos los roles que este nuevo usuario podrá tener/usar (una línea por cada rol).
  * Cierre sesión del rol actual.

#### Crear un nuevo módulo

  * Inicie sesión en Etendo ERP como Administrador del Sistema.
  * Haga clic en el menú `Module` desde el Diccionario de Aplicación.
  * En la lista `Module Type`, seleccione Module.
  * En el campo `Name`, escriba el nombre del paquete Java del módulo (convención de nombres adecuada).
  * Complete los campos `Description` y `Help`. Proporcione la información sobre el plan contable.
  * Seleccione la opción `Tiene datos de referencia`.
  * Desmarque las opciones `Has chart of accounts`, `Translation required` e `Is translation module`.
  * Seleccione la opción In development. Recuerde que no puede trabajar en un módulo a menos que la opción `In development` esté seleccionada.
  * En la solapa `Dependencies`, seleccione Core.
  * Guarde el módulo.

#### Crear un conjunto de datos de roles y accesos

  1. En el menú de la aplicación, seleccione `Application Dictionary` > `Dataset`
  2. Haga clic en Nuevo.
  3. En la lista `Module`, seleccione el módulo creado anteriormente.
  4. Especifique una clave de búsqueda, nombre y descripción.
  5. En la lista `Acceso datos`, seleccione el nivel de acceso de datos como *Organización*.
  6. Seleccione la opción `Export allowed`.
  7. Seleccione la solapa `Table`.
  8. En la lista `Table`, seleccione la tabla cuyo contenido desea incluir en el módulo. Por ejemplo, ad_role_org_access, ad_role, ad_user_roles.
  9. En el campo de cláusula SQL where, especifique la sentencia SQL "WHERE" que identificará el conjunto de filas a exportar, en notación DAL. Por ejemplo, adrole.id='2EA831D59184490E9BA858E9745EF89F'
  10. Seleccione la opción `Incluir Todas las Columnas`.
  11. Seleccione la opción `isBusinessObject`.
  12. Haga clic en Guardar.
  13. Haga clic en el botón `Exportar Datos de Referencia` para exportar los datos de referencia a un archivo .xml que pueda incluir en el módulo.

#### Exportación y publicación del módulo

Después de completar correctamente todos los pasos, ejecute la siguiente tarea de gradle para exportar el módulo:

    ./gradlew export.database

Y publique el módulo.

!!!info
    Para más información, consulte [Cómo publicar módulos en un repositorio de GitHub](../../../developer-guide/etendo-classic/how-to-guides/how-to-publish-modules-to-github-repository.md).

#### Cómo instalar - Datos de referencia con nivel de acceso Organización

  * Instale el módulo siguiendo la guía [Instalar módulos en Etendo](../../../developer-guide/etendo-classic/getting-started/installation/install-modules-in-etendo.md).
  * En este punto, los datos de referencia no se instalarán.
  * Inicie sesión en el ERP como admin.
  * Haga clic en `General Setup` y navegue a `Enterprise` > `Enterprise module Management`.
  * Seleccione el `Organization type`, luego seleccione el módulo correspondiente y haga clic en Ok para instalar los datos de referencia.

### Conjunto de datos de impuestos o alertas

En esta sección puede encontrar el ejemplo de un conjunto de datos de impuestos o alertas. En el proceso de creación de un módulo estándar de datos de referencia para impuestos y alertas, si ha configurado Etendo ERP de una manera particular para cumplir requisitos locales, puede exportar estos datos y convertirlos en un módulo, de modo que pueda compartirlo con otros usuarios.

#### Registro de un módulo de datos para impuestos y alertas:

  * Inicie sesión en Etendo ERP como Administrador del Sistema.
  * Haga clic en el menú `Module` desde el Diccionario de Aplicación.
  * En la lista `Module Type`, seleccione Module.
  * En el campo `Name`, escriba el nombre del paquete Java del módulo (convención de nombres adecuada).
  * Complete los campos `Description` y `Help`. Proporcione la información sobre el plan contable.
  * Seleccione la opción `Tiene datos de referencia`.
  * Desmarque las opciones `Has chart of accounts`, `Translation required` e `Is translation module`.
  * Seleccione la opción `In development`. Recuerde que no puede trabajar en un módulo a menos que la opción `In development` esté seleccionada.
  * En la solapa `Dependencies`, seleccione Core.
  * Guarde el módulo.

#### Definición y exportación del conjunto de datos

  1. En el menú de la aplicación, seleccione `Application Dictionary` > `Dataset`
  2. Haga clic en Nuevo.
  3. En la lista `Module`, seleccione el módulo creado anteriormente.
  4. Especifique una `clave de búsqueda`, `nombre` y `descripción`.
  5. En la lista `Acceso datos`, seleccione el nivel de acceso de datos como Solo sistema.
  6. Seleccione la opción `Export allowed`.
  7. Seleccione la solapa `Table`.
  8. En la lista `Table`, seleccione la tabla cuyo contenido desea incluir en el módulo.
  9. En el campo `SQL where clause`, especifique la sentencia SQL WHERE que identificará el conjunto de filas a exportar, en notación DAL. Por ejemplo, client.id='1000001'
  10. Para exportar todas las columnas, seleccione la opción `Incluir Todas las Columnas`. Para incluir solo las columnas que especifique, seleccione la solapa `Columns` y cree un nuevo registro para cada columna que desee exportar.
  11. Para incluir las columnas de auditoría de seguridad (created, createdby, updated y updatedby) en la exportación, desmarque la casilla `Exclude Audit Info`.
  12. Desmarque la opción `Is Business Object`.
  13. Haga clic en Guardar.
  14. Haga clic en el botón `Exportar Datos de Referencia` para exportar los datos de referencia a un archivo .xml que pueda incluir en el módulo.

#### Exportación y publicación del módulo

Después de completar correctamente todos los pasos, ejecute la siguiente tarea de gradle para exportar el módulo:

    ./gradlew export.database

Y publique el módulo.

!!!info
    Para más información, consulte [Cómo publicar módulos en un repositorio de GitHub](how-to-publish-modules-to-github-repository.md).

#### Cómo instalar - Datos de referencia con nivel de acceso Sistema/Entidad

  * Instale el módulo siguiendo la guía [Instalar módulos en Etendo](../../../developer-guide/etendo-classic/getting-started/installation/install-modules-in-etendo.md).
  * En este punto, los datos de referencia no se instalarán.
  * Inicie sesión en el ERP como admin.
  * Haga clic en `General Setup` y navegue a `Entidad` > `Initial Client Setup`.
  * Rellene todos los campos obligatorios y luego seleccione el módulo correspondiente.
  * Finalmente, haga clic en Ok para instalar los datos de referencia.

### Conjunto de datos de regiones

En esta sección puede exportar los datos de referencia con los ejemplos sobre regiones. A continuación se indican los pasos para crear el conjunto de datos para este módulo:

  * Inicie sesión en Etendo ERP como Administrador del Sistema.
  * Cree un nuevo módulo llamado _Indian States_ para este ejemplo.
  * Asegúrese de que ha seleccionado o marcado el campo `Has Reference Data`.
  * Ahora despliegue el menú `Application Dictionary`.
  * Haga clic en el menú `Dataset` y cree un nuevo registro para este módulo.
  * Por ejemplo, aquí se ha asignado el nombre `Indian States`. Puede asignar el nombre que desee para seleccionar la región.
  * Rellene el formulario de conjunto de datos usando los valores indicados a continuación.

    Campo              |  valor del campo
    ---                |          ---
    Activo             |  marcarlo/poner una marca de verificación
    Módulo             |  seleccionar el valor del desplegable _Indian States - 1.0.0_
    Clave de búsqueda  |  Indian States
    Nombre             |  Indian States
    Acceso datos       |  Solo sistema

  * Antes de asignar las tablas al conjunto de datos, ejecute la siguiente consulta en sqldeveloper o en un IDE de postgres para encontrar el `C_country_Id` de INDIA. Tras ejecutar la consulta, el resultado de `c_country_id` sería 208 para la consulta siguiente.

    ```sql
    select * from c_country where countrycode like 'IN%';
    ```

  * Navegue a la solapa `Table` y cree 2 nuevos registros para el conjunto de datos.
  * Rellene el formulario usando los valores siguientes para la tabla: `C_Country`

    Campo                |  valor del campo
    ---                  |          ---
    Tabla                |  `C_Country`
    Activo               |  Por defecto está marcado. Déjelo tal cual
    Módulo               |  Indian States - 1.0.0
    Cláusula SQL Where   |  id='208'
    Incluir Todas las Columnas  |  Quite la marca (las columnas individuales se añadirán en pasos posteriores)
    Excluir info de auditoría   |  Márquelo/active esta casilla

  * Rellene el formulario usando los valores siguientes para la tabla: `C_Region`

    Campo                |  valor del campo
    ---                  |          ---
    Tabla                |  `C_Region`
    Activo               |  Por defecto está marcado. Déjelo tal cual
    Módulo               |  Indian States - 1.0.0
    Cláusula SQL Where   |  country.id='208'
    Incluir Todas las Columnas  |  Márquelo/active esta casilla
    Excluir info de auditoría   |  Márquelo/active esta casilla

  * Seleccione la tabla `C_Country` desde la vista de cuadrícula de tablas y navegue a la solapa `Column`.
  * Haga clic en el botón para crear un nuevo registro para la tabla anterior. Debe seleccionar tres columnas para esta tabla.
  * Esas columnas son:
      - Name
      - CountryCode
      - HasRegion
  * Rellene los siguientes valores en el formulario.

    Campo   |  valor del campo
    ---     |          ---
    **Columna 1:**
    Columna  |  Name
    Activo  |  Se ha marcado. Déjelo tal cual
    Módulo  |  Indian States - 1.0.0
    **Columna 2:**
    Columna  |  CountryCode
    Activo  |  Se ha marcado. Déjelo tal cual
    Módulo  |  Indian States - 1.0.0
    **Columna 3:**
    Columna  |  HasRegion
    Activo  |  Se ha marcado. Déjelo tal cual
    Módulo  |  Indian States - 1.0.0

  * Finalmente, navegue a la solapa `Dataset` de Indian States y haga clic en el botón `Exportar Datos de Referencia` para exportar los datos.

#### Exportación y publicación del módulo

Después de completar correctamente todos los pasos, ejecute la siguiente tarea de gradle para exportar el módulo:

    ./gradlew export.database

Y publique el módulo.

!!!info
    Para más información, consulte [Cómo publicar módulos en un repositorio de GitHub](../../../developer-guide/etendo-classic/how-to-guides/how-to-publish-modules-to-github-repository.md).

#### Cómo instalar - Datos de referencia con nivel de acceso Solo sistema

  * Instale el módulo siguiendo la guía [Instalar módulos en Etendo](../../../developer-guide/etendo-classic/getting-started/installation/install-modules-in-etendo.md).
  * Se instalará junto con los datos de referencia.

Este trabajo es una obra derivada de [Cómo crear un conjunto de datos](http://wiki.openbravo.com/wiki/How_to_create_a_Dataset){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.