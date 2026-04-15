---
title: Cómo crear un script de configuración
tags: 
    - Crear
    - Configuración
    - Script 
    - configScript
status: beta
---
  
# Cómo crear un script de configuración

!!! example "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.

## Visión general

Los módulos son una excelente forma de ampliar y personalizar una instancia de Etendo. Sin embargo, tienen una limitación principal: se pueden utilizar para **añadir** nuevos objetos (como nuevas ventanas, solapas, tablas o incluso columnas para tablas existentes y campos para solapas existentes), pero no se pueden utilizar para modificar objetos existentes (como campos existentes del Core), y en ocasiones esto no es suficiente. 

Una Plantilla de industria (que incluye un script de configuración) puede utilizarse para modificar objetos existentes. La mayoría de las veces, esta capacidad se utilizará para modificar el comportamiento del Core, pero en algunas situaciones también puede utilizarse para modificar la funcionalidad de un módulo (en particular, cuando un desarrollador no es el propietario de un módulo y quiere utilizarlo, pero desea personalizar parte de su funcionalidad).

Esta sección describe qué es un script de configuración (el objeto más importante de una Plantilla de industria), cómo se puede generar y cómo se puede modificar posteriormente.

Es muy recomendable que esté familiarizado con el proceso de desarrollo de Etendo antes de leer este documento. En particular, es muy importante que esté familiarizado con el contenido del documento [Cómo crear un módulo](../how-to-guides/how-to-create-a-module.md).

## Qué es un script de configuración

Un script de configuración es básicamente un archivo `XML` que contiene información sobre cambios realizados en valores de columnas de filas de tablas de base de datos.

Esto se explica fácilmente mediante un ejemplo. Esta sería la información que contendría el script para un cambio en la tabla `AD_MENU`, en la columna `ISACTIVE`, que se cambió de 'Sí' a 'No', para la fila con AD_Menu_Id='113':

``` XML
    <columnDataChange tablename="AD_MENU" columnname="ISACTIVE" pkRow="113">
        <oldValue><![CDATA[Y]]></oldValue>
        <newValue><![CDATA[N]]></newValue>
    </columnDataChange>
```

Si está familiarizado con el proceso de desarrollo de Etendo, probablemente ya pueda imaginar qué tipo de personalizaciones son posibles con los scripts de configuración. Ocultar campos existentes, cambiar la referencia de una columna concreta o cambiar el nombre de algún campo son solo algunos ejemplos.

## ¿Cómo se generan los scripts de configuración?

Los scripts de configuración se generan automáticamente mediante una tarea de Gradle llamada `export.config.script`. Primero necesita crear un módulo de tipo **Plantilla** en Etendo y establecerlo como **En Desarrollo**. Después, realice los cambios que quiera (por ejemplo, cambiar las etiquetas de algunos campos u ocultarlos usando las ventanas del Diccionario de Aplicación). Por último, asegúrese de que no haya otros módulos en desarrollo en el sistema y ejecute las siguientes tareas:
 
```
    ./gradlew  export.database
    ./gradlew  export.config.script
```

La primera (que ya debería conocer por la documentación *How to* relacionada con módulos) se utiliza para exportar los datos del Diccionario de Aplicación del módulo. La segunda exporta el script de configuración.

Este script de configuración se crea comparando la información actual dentro de los archivos `XML` del Core de Etendo y de sus módulos instalados frente a la información de su base de datos. Cada cambio de datos de columna encontrado en el Diccionario de Aplicación se exporta al archivo `XML`, que se creará dentro de la carpeta `src-db/database` de su *Plantilla*, dentro de la carpeta de módulos de Etendo.

## Instalar más de un script de configuración en el sistema

En ocasiones, puede ser interesante tener más de una Plantilla de industria (y, por tanto, más de un script de configuración) en el sistema. Por ejemplo, imagine que alguien ha desarrollado una Plantilla de industria para el sector de automoción. Esta plantilla podría incluir varios módulos adicionales y un script de configuración que adapta parte de la funcionalidad del Core para ajustarse mejor a las necesidades de ese sector. Puede que quiera usarla en su proyecto, pero también puede necesitar personalizar varios aspectos adicionales del Core o incluso de los módulos que incluye esa plantilla. Por tanto, sería necesaria una Plantilla de industria adicional (con su script correspondiente).

Es posible tener tantas plantillas funcionando en el mismo sistema como quiera, pero debe cumplirse una regla muy importante: **debe existir una jerarquía de dependencias definida para las plantillas**. Esto significa que debe existir una cadena lineal de dependencias entre las plantillas. En nuestro ejemplo anterior, esto significa que nuestra plantilla de personalización debería depender de la plantilla genérica de automoción. Si cuatro plantillas (A, B, C, D) deben funcionar en la misma instancia, entonces debe existir una cadena de dependencias que las enlace (por ejemplo, A->B->C->D). **No puede haber dos plantillas diferentes en el mismo nivel de la jerarquía**.

La razón de esta regla es fácil de explicar: los scripts de configuración se utilizan para modificar objetos, y es muy posible que, si hay más de un script de configuración en el sistema, existan modificaciones solapadas sobre el mismo objeto. La tarea que aplica los scripts de configuración necesita saber en qué orden deben aplicarse los cambios, y la única forma de hacerlo es definir un orden explícito en el que deben aplicarse las plantillas.

Otra regla muy importante que debe cumplirse: **solo es posible desarrollar la plantilla que está en el extremo exterior de la cadena de dependencias**. En nuestro ejemplo anterior, usted podría desarrollar su propia plantilla de personalización (es decir, cambiar el script de configuración), pero no podría desarrollar la plantilla genérica de industria de automoción, porque ya existe una plantilla que depende de ella.

## Procesos para alimentar scripts de configuración

En algunas situaciones, podría parecer una buena idea incluir un script de configuración dentro de un módulo normal. Por ejemplo, un módulo podría añadir un *callout* o una nueva referencia, pero el desarrollador también querría asociar el *callout* a un campo existente del Core o cambiar la referencia de una columna del Core a la nueva.

No es posible añadir un script de configuración a un módulo precisamente por las razones explicadas en la sección anterior (los módulos están pensados para ser independientes en muchas situaciones, pero los scripts de configuración necesitan ejecutarse en un orden específico y, por tanto, debe existir una dependencia explícita entre ellos). Sin embargo, existe una alternativa para casos como los descritos anteriormente: un módulo puede incluir un proceso para realizar los cambios en el Diccionario de Aplicación, diseñado para ejecutarse en un entorno con una Plantilla de industria de personalización activa.

Este proceso se ejecutaría en la instancia después de que el módulo haya sido instalado y, una vez ejecutado, las modificaciones podrían exportarse a la Plantilla de industria de personalización específica que esa instancia ya tenga.

Una buena forma de hacerlo sería crear un proceso Java estándar de Etendo. Puede leer más sobre estos procesos en [Cómo crear una definición de proceso estándar](./how-to-create-a-standard-process-definition.md). El proceso tendría que realizar los siguientes pasos:

- Primero tendría que comprobar si existe una Plantilla de industria en desarrollo en el sistema (esto es un requisito para la ejecución del proceso). Esto se puede hacer con una consulta DAL de una forma muy sencilla: 


    ``` java
    public String returnIdOfTemplateInDevelopment(){
        OBCriteria<Module> tCriteria = OBDal.getInstance().createCriteria(Module.class);
        tCriteria.add(Expression.and(Expression.eq(Module.PROPERTY_TYPE, "T"), Expression.eq(
            Module.PROPERTY_INDEVELOPMENT, true)));

        if (tCriteria.list().size() > 0) {
        return tCriteria.list().get(0).getId();
        }else{
        //We didn't find any template in development
        return null;
        }
    }
    ```

- Si existe una, entonces se pueden realizar los cambios. Estos cambios se harían en Java (posiblemente mediante consultas y actualizaciones DAL) y podrían ser estáticos (es decir, podría estar cambiando un conjunto específico codificado de objetos del Diccionario de Aplicación) o dinámicos (podría estar cambiando objetos del Diccionario de Aplicación que cumplan alguna regla específica). Esto significa que, de hecho, este proceso podría ser incluso más potente que un script de configuración (que por diseño es estático), porque podría estar cambiando, por ejemplo, las referencias de todas las columnas de la instancia que actualmente estén usando una referencia específica. Por ejemplo, este código: 

    ``` java
    final String whereClause = "as c where c.reference.id = :ref_id"
        + " and c.referenceSearchKey.id = :ref_val_id";
    OBQuery<Column> cQuery = OBDal.getInstance().createQuery(Column.class, whereClause);
    cQuery.setNamedParameter("ref_id", "10");
    cQuery.setNamedParameter("ref_val_id", oldRef);
    if (cQuery.count() == 0) {
        pLogger.logln("No columns to update");
    }
    String logMessage = "Processing column: @AD_COLUMN_ID@";
    for (Column c : cQuery.list()) {
        pLogger.logln(logMessage.replaceAll("@AD_COLUMN_ID@", c.getId()));
        c.setReference(newRef);
        c.setReferenceSearchKey(newRefSearch);
        OBDal.getInstance().save(c);
    }
    ```     

    cambiaría la referencia de todas las columnas con referencia de tipo cadena (`id=10`) a una nueva referencia (`newRef`).

- Después de realizar los cambios, debería mostrar un mensaje claro al usuario indicándole que necesita exportar de nuevo su script de configuración (el desarrollador responsable de la instancia que tiene la plantilla de personalización deberá ejecutar `./gradlew  export.config.script` en este punto). 

## Consideraciones adicionales relacionadas con los scripts de configuración

Los scripts de configuración se utilizan principalmente para exportar cambios que usted no quiere exportar al propietario de los datos que está cambiando. En el ejemplo anterior, usted no quiere exportar la información modificada de la entrada `AD_Menu` a los archivos del Core, sino que quiere exportar el cambio a un script de configuración específico y localizado que pertenece a su Plantilla de industria de personalización. Por tanto, sería incoherente tener tanto el Core como su Plantilla de industria en desarrollo al mismo tiempo. Es más, si tuviera ambos en desarrollo al mismo tiempo, los cambios se exportarían a los archivos del Core mediante la tarea `export.database` y el script de configuración que obtendría estaría vacío.

Lo mismo puede decirse cuando se utilizan scripts de configuración para modificar módulos existentes. No tiene sentido tener tanto el módulo como la plantilla en desarrollo al mismo tiempo. Hacerlo provocaría que los cambios se exportaran a los archivos del módulo y el script de configuración estaría vacío.

## Cambios no deseados/inútiles dentro de los scripts de configuración

En versiones anteriores de Etendo, era posible que, cuando los módulos instalados en la instancia se desarrollaron con un MP anterior al que está actualmente instalado en el sistema, se exportaran cambios innecesarios dentro del script de configuración. Esto incluía cambios como este:

``` XML
    <columnDataChange tablename="AD_COLUMN" columnname="ISAUTOSAVE" pkRow="FEFAAABCCCCC1001FEFAAABCCCCC1001">
        <oldValue/>
        <newValue><![CDATA[N]]></newValue>
    </columnDataChange>
```    

Estos cambios corresponden a nuevas columnas añadidas en el MP utilizado, que no existían en el MP en el que se crearon los módulos. Estos cambios no son necesarios y, aunque son inofensivos, pueden recargar el script de configuración, haciendo a veces difícil leerlo y analizarlo manualmente.

Existe un mecanismo integrado para evitar que esto ocurra. Sin embargo, si el script de configuración se generó en una versión antigua de Etendo, es posible que estos cambios ya estén dentro de él. Existe un proceso para "limpiar" el script, que implica los siguientes pasos:

- Elimine temporalmente el script de configuración del sistema (solo necesita mover el archivo fuera de su ubicación correcta, en `modules/java_package_of_template/src-db/database/configScript.xml`) y ejecute `./gradlew  update.database`.
- Haga una copia del archivo `src-db/database/formalChangesScript.xml`, dentro de la carpeta principal de Etendo. 
- Vuelva a colocar el script de configuración en su ubicación y ejecute `./gradlew  update.database` de nuevo. 
- Vuelva a colocar la copia del archivo `formalChangesScript.xml` en su ubicación, reemplazando el archivo existente. 
- Ejecute `./gradlew  export.config.script` con su plantilla establecida como en desarrollo. 

Después de seguir estos pasos, el archivo resultante del script de configuración debería estar limpio y sin estos cambios inútiles.

---

Este trabajo es una obra derivada de [Cómo crear un script de configuración de una tabla](http://wiki.openbravo.com/wiki/How_To_Create_a_Configuration_Script){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.