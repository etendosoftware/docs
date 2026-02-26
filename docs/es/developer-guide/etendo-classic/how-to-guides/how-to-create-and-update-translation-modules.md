---
title: Cómo crear y actualizar módulos de traducción
---

# Cómo crear y actualizar módulos de traducción

## Visión general

Esta sección describe el proceso de creación y actualización de módulos de traducción en Etendo, incluido el módulo Core.

## Crear un nuevo módulo de traducción desde cero

### Crear la definición del módulo

Lo primero que debe hacer es crear la definición del módulo de traducción en el Diccionario de aplicación.

Con la sesión iniciada con el rol de Administrador del sistema, el usuario selecciona la ventana `Application Dictionary` > `Module` desde el menú de Aplicación y crea un nuevo registro.

Los módulos de traducción son un tipo especial de módulos. Deben marcarse como módulo de traducción en la ventana Módulo, y deben definir el idioma de traducción en el campo Idioma del módulo.

En los módulos de traducción no se permite ningún otro contenido que no sean traducciones. Un módulo de traducción solo puede contener la traducción de un único módulo. Por ejemplo, en la captura de pantalla siguiente, estamos creando un módulo de traducción *Español (España)* para el módulo User Interface Application cuyo idioma declarado es English (USA).

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-and-update-translation-modules/how-to-create-and-update-translation-modules-0.png)

Además de marcar que es un módulo de traducción y establecer el Idioma del módulo, necesitamos añadir una dependencia al módulo y a la versión que estamos traduciendo. En el ejemplo, nuestro módulo *User Interface Application Translation Spanish (Spain)* en la versión 1.0.0 depende del módulo *User Interface Application* versión 2.1.0.

### Preparar las cadenas que se van a traducir

Con la sesión iniciada con el rol de *Administrador del sistema*, seleccione la ventana `General Setup`> `Application` > `Language` desde el menú de Aplicación. Busque el idioma en el que el usuario quiere crear el módulo de traducción y marque el campo de casilla de verificación Idioma del sistema. Esta casilla permite que este idioma pueda seleccionarse en la interfaz de usuario (ventana emergente Cambiar rol) en el siguiente inicio de sesión.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-and-update-translation-modules/how-to-create-and-update-translation-modules-1.png)

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-and-update-translation-modules/how-to-create-and-update-translation-modules-2.png)

### Comprobar idiomas

Cada vez que sea necesario crear una traducción para un nuevo idioma, es necesario preparar las cadenas que se van a traducir. Existe un proceso automático, llamado Comprobar idiomas (disponible también en la ventana Idioma), en el que el ERP crea las copias necesarias de las cadenas originales de todos los módulos disponibles en el sistema desde sus idiomas base al idioma de traducción correspondiente.

Por ejemplo, en el caso de crear una traducción *Español (España)* para el módulo Core, cuyo idioma base es *English (USA)*, el sistema copiará todas las cadenas originales en inglés a la traducción al español. Esto mismo se extiende al resto de módulos instalados en el sistema con sus respectivos idiomas base.

Al usar el botón Comprobar idiomas, la aplicación mostrará el número de registros creados. Si este número es igual a 0, significa que algo ha ido mal, y la causa probable es que se haya olvidado marcar el campo Idioma del sistema.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-and-update-translation-modules/how-to-create-and-update-translation-modules-3.png)

### Exportar la traducción

La exportación de la traducción es un proceso automático disponible en la ventana `General Setup` > `Application` > `Import/Export Translations`.

Con el rol de Administrador del sistema, seleccione el idioma en el que el usuario quiere exportar los archivos de traducción. El indicador Export Reduced Version puede establecerse en Sí para tener una versión reducida de la traducción. Esto excluiría todos los candidatos de traducción que estén vinculados directa o indirectamente al Menú que tenga la estrategia de traducción como "Excluir de la traducción reducida". El usuario puede establecer este indicador en No para tener una versión completa de la traducción pulsando el botón Exportar. El proceso tarda varios segundos en exportar todos los archivos XML.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-and-update-translation-modules/how-to-create-and-update-translation-modules-4.png)

Dentro de la carpeta attachments de Etendo, se encuentra un nuevo directorio llamado lang y, dentro de él, uno nuevo con el código de idioma de dos letras en minúsculas y el código de país de dos letras en mayúsculas separados por un carácter de subrayado ('\_'). Ejemplo: `/home/EtendoERP/attachments/lang/es_ES`

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-and-update-translation-modules/how-to-create-and-update-translation-modules-5.png)

Dentro de este directorio, el usuario puede encontrar los archivos de traducción para todos los módulos disponibles en la instancia. Los archivos de traducción del Core se almacenan directamente en el directorio raíz; el resto de módulos tienen su propia carpeta nombrada como sus paquetes Java. Por tanto, el usuario solo necesita encontrar la carpeta del *módulo original* que se va a traducir (*no el módulo de traducción*) y obtener sus archivos XML.

### Traducir el módulo

La traducción del módulo puede realizarse modificando manualmente los archivos XML exportados, lo cual es un método conveniente para módulos con pocas cadenas que traducir, o utilizando el asistente de Etendo Copilot, [Module Translation Creator](../../etendo-copilot/bundles/dev-assistant.md#module-translation-creator).

#### Traducir directamente en los archivos XML

Si se elige este método, solo es necesario abrir cada archivo XML que esté dentro del directorio del módulo que se va a traducir y editarlo. Es muy importante abrir estos archivos con un editor de texto.

El texto que debe cambiarse para realizar una traducción es el contenido de cada etiqueta value. No es necesario editar ningún atributo porque se actualizarán automáticamente al importar y exportar los archivos en el ERP en un paso posterior.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-and-update-translation-modules/how-to-create-and-update-translation-modules-6.png)

### Importar y exportar las traducciones

Después de completar la traducción, o incluso en mitad de un proceso de traducción, es una buena práctica importar los archivos XML en el ERP para revisar la traducción en contexto.

Por último, una vez que la traducción es correcta, es necesario volver a exportarla. Al hacerlo, se garantiza que los archivos XML tengan la estructura final, con todos los atributos correctamente establecidos.

!!! info
    Todos los archivos XML que se vayan a importar deben estar dentro de la carpeta del módulo correspondiente de su directorio *attachments*, sobrescribiendo los archivos XML originales exportados al inicio de este proceso.

Ahora, en la ventana `Import/Export Translations`, podemos seleccionar el idioma utilizado para las traducciones y pulsar el botón Importar. A continuación, se completa el proceso y se pulsa el botón Exportar, que exportará de nuevo los archivos XML.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-and-update-translation-modules/how-to-create-and-update-translation-modules-4.png)

!!! info
    Durante este proceso, se recomienda encarecidamente mantener una copia de seguridad de sus archivos XML traducidos.

### Información específica si está traduciendo Core

#### Archivo buildstructure.xml

El Core de Etendo proporciona un archivo adicional llamado `buildStructure.xml`. Este archivo contiene la información relacionada con los nombres de las diferentes etapas por las que pasa el proceso de construcción del sistema de Etendo, y los mensajes de error y advertencia que pueden mostrarse durante una reconstrucción. También es necesario traducir este archivo.

La estructura de este archivo es un poco diferente en comparación con los archivos XML estándar de traducción de Etendo, pero también es muy fácil de entender. Solo necesita traducir el contenido de todos los atributos que comienzan por “translated”, como *translatedName*, *translatedErrorMessage*, etc. Este es un ejemplo del archivo `buildstructure.xml` traducido al español.

```xml title="buildstructure.xml"
<?xml version='1.0' ?>
<BuildTranslation>
  <language>es_ES</language>
  <mainStepTranslations>
    <mainStepTranslation code="RB11" originalName="Initial Build Validation" translatedName="Validación de la construcción del sistema" translatedErrorMessage="La validación ha fallado. El sistema no se ha modificado y continua estable, pero los problemas descritos en la parte inferior de la ventana deberían resolverse (ya sea desinstalando los módulos afectados, o resolviendo los problemas de la forma descrita), y una nueva construcción del sistema debería iniciarse.">
      <stepTranslations/>
    </mainStepTranslation>
    <mainStepTranslation code="RB20" originalName="Build" translatedName="Construcción del sistema" translatedSuccessMessage="La construcción del sistema se ha completado con éxito." translatedWarningMessage="Se produjeron alertas durante la compilación. La aplicación se ejecutará, pero debería comprobarlas para ver si son importantes. Ir a &lt;a href=&quot;http://wiki.openbravo.com/wiki/ERP/2.50/Update_Tips&quot; target=&quot;_blank&quot; class=&quot;MessageBox_TextLink&quot;&gt; este enlace &lt;/a&gt; para más información. &lt;b&gt;Ahora debe reiniciar el contenedor de servlets&lt;/b&gt; para que los cambios tengan efecto." translatedErrorMessage="Ha ocurrido un error durante la construcción del sistema. Para saber qué pasos realizar a continuación, vaya a &lt;a href=&quot;http://wiki.openbravo.com/wiki/ERP/2.50/Update_Tips&quot; target=&quot;_blank&quot; class=&quot;MessageBox_TextLink&quot;&gt;este enlace&lt;/a&gt;">
      <stepTranslations>
        <stepTranslation code="RB12" originalName="Database update" translatedName="Actualización de la base de datos"/>
        <stepTranslation code="RB31" originalName="Reference data" translatedName="Datos de referencia"/>
        <stepTranslation code="RB43" originalName="Compilation" translatedName="Compilación"/>
      </stepTranslations>
    </mainStepTranslation>
  </mainStepTranslations>
</BuildTranslation>
```

#### Conjunto de datos Masterdata

Todos los archivos XML exportados a través de la ventana *Import/Export Translation* y el archivo buildstructure.xml representan todas las cadenas disponibles de la interfaz de usuario en el ERP. Si traducimos todos estos archivos, tendremos una aplicación completamente traducida. Sin embargo, el ERP incluye algunas otras cadenas no relacionadas con la UI que también pueden traducirse. Dentro de este grupo, llamado Masterdata, incluimos: nombres de países, monedas, unidades de medida y nombres de meses. Todos estos datos no se exportan a los archivos XML; sin embargo, esto no significa que no podamos traducirlos.

La forma de traducir los datos maestros es crear un conjunto de datos a nivel de sistema que solo contenga las cadenas traducidas para países, monedas, unidades de medida y meses.

Como *Administrador del sistema*, creamos un nuevo registro dentro de la ventana Dataset para nuestro módulo de traducción del Core. Es importante definir este conjunto de datos a nivel Solo sistema para garantizar que se aplicará automáticamente cuando instalemos el módulo.

Como puede ver en la captura de pantalla, las tablas que deben incluirse son: `AD_Month_Trl C_Country_Trl`, `C_Currency_Trl` y `C_UOM_Trl`. Todas ellas tienen una cláusula de filtro que utiliza la columna de idioma, en el ejemplo `es_ES`.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-and-update-translation-modules/how-to-create-and-update-translation-modules-7.png)

Ahora, nuestro módulo de traducción del Core tiene un conjunto de datos, por lo que debemos recordar marcar el indicador Tiene datos de referencia en la definición del módulo.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-and-update-translation-modules/how-to-create-and-update-translation-modules-8.png)

La definición del conjunto de datos está lista, pero queda pendiente la traducción en sí. Para traducir este conjunto de datos, tenemos dos posibilidades:

-   En el ERP, como Administrador del sistema, podemos ir a las ventanas País, región y ciudad, Moneda, Unidad de medida y Mes y traducir el registro correspondiente dentro de la pestaña Traducción (método recomendado).  
    Cuando finalice, exporte el conjunto de datos usando el botón Exportar datos de referencia en la ventana Dataset.  

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-and-update-translation-modules/how-to-create-and-update-translation-modules-9.png)

-   Exportar el conjunto de datos con las cadenas sin traducir y editar el archivo XML usando un editor de texto. El archivo XML del conjunto de datos se almacenará dentro del directorio referencedata/standard de su módulo de traducción.
 

### Paquete de traducción

Como probablemente sepa, Etendo es una distribución de módulos, incluido Core. Eso significa que, para tener una aplicación completamente traducida, debe traducir todos los módulos que forman parte de la distribución.

Es una buena idea crear un paquete de traducción que cubra todos los módulos.

#### Publicar el módulo de traducción

El proceso de publicación de un módulo de traducción es similar al proceso estándar de publicación con una única consideración importante: necesitamos copiar los archivos XML traducidos a la carpeta `referencedata/translation` del módulo correspondiente dentro de la carpeta de su módulo.

El proceso resumido es:

1.   *Solo Core:* Si hemos traducido el conjunto de datos Masterdata directamente en el ERP, necesitamos exportarlo mediante el botón Exportar datos de referencia en la ventana Dataset.
2.   Exportar la base de datos ejecutando
    ```bash title="Terminal"
    ./gradlew export.database 
    ```

3. Copiar los archivos XML traducidos a la carpeta referencedata/translation del módulo de traducción. 
La estructura del directorio del módulo de traducción debería ser:

    ```plaintext
    <translation module java package name>
    ├── referencedata
    │ ├── standard
    │ │ └── Masterdata.xml (only for core)
    │ └── translation
    │     └── es_ES
    │         ├── AD_ELEMENT_TRL_es_ES.xml
    │         ├── AD_FIELDGROUP_TRL_es_ES.xml
    │         ├── AD_FIELD_TRL_es_ES.xml
    │         ├── AD_FORM_TRL_es_ES.xml
    │         ├── AD_MENU_TRL_es_ES.xml
    │         ├── AD_MESSAGE_TRL_es_ES.xml
    │         ├── AD_MODULE_TRL_es_ES.xml
    │         ├── AD_PROCESS_PARA_TRL_es_ES.xml
    │         ├── AD_PROCESS_TRL_es_ES.xml
    │         ├── AD_REFERENCE_TRL_es_ES.xml
    │         ├── AD_REF_LIST_TRL_es_ES.xml
    │         ├── AD_TAB_TRL_es_ES.xml
    │         ├── AD_TEXTINTERFACES_TRL_es_ES.xml
    │         ├── AD_WF_NODE_TRL_es_ES.xml
    │         ├── AD_WINDOW_TRL_es_ES.xml
    │         ├── AD_WORKFLOW_TRL_es_ES.xml
    │         ├── buildStructureTrl.xml
    │         ├── C_DOCTYPE_TRL_es_ES.xml
    │         ├── CONTRIBUTORS_es_ES.xml
    │         ├── OBKMO_WIDGET_CLASS_TRL_es_ES.xml
    │         ├── OBUIAPP_PARAMETER_TRL_es_ES.xml
    │         ├── OBUISEL_SELECTOR_FIELD_TRL_es_ES.xml
    │         └── OBUISEL_SELECTOR_TRL_es_ES.xml
    └── src-db
       └── database
           ├── model
           │ ├── functions
           │ ├── sequences
           │ ├── tables
           │ ├── triggers
           │ └── views
           └── sourcedata
               ├── AD_DATASET_TABLE.xml (only for core)
               ├── AD_DATASET.xml (only for core)
               ├── AD_MODULE_DEPENDENCY.xml
               └── AD_MODULE.xml
    ```

4. Por último, recuerde publicar el módulo. Para más información, consulte [Publicar módulos en un repositorio de GitHub](../../../developer-guide/etendo-classic/how-to-guides/how-to-publish-modules-to-github-repository.md).

#### Actualizar módulos de traducción

Estas son las primeras consideraciones para actualizar un módulo de traducción:

-   Necesitamos instalar/actualizar en nuestra instancia la última versión del módulo original y sus módulos de traducción. Para ello, encuentre más información en [Instalar módulos en Etendo](../../../developer-guide/etendo-classic/getting-started/installation/install-modules-in-etendo.md). 
-   Se conservan las cadenas ya traducidas para este módulo. Solo las nuevas o modificadas quedarán sin traducir, por lo que no se pierde el trabajo previo realizado.
-   Antes de publicar el módulo de traducción, recuerde actualizar la dependencia de Primera versión a la nueva versión del módulo traducido, como vimos en el capítulo “Crear la definición del módulo”. Además, es necesario actualizar la versión del módulo original en el archivo build.gradle. Aparte de eso, también es una buena práctica incluir una descripción de los cambios de esta nueva versión dentro del campo Información de actualización de la ventana Módulo.
-   Para aplicar las actualizaciones, es necesario ejecutar el comando 

``` bash title="Terminal"
./gradlew install.translation -Dmodule=javapackage
./gradlew smartbuild -Dlocal=no
```

Los pasos principales para actualizar un módulo de traducción son casi los mismos que al crear un nuevo módulo de traducción desde cero. La única diferencia es que no es necesario declarar el Idioma del sistema ni ejecutar el proceso Comprobar idiomas. El resto del proceso es exactamente el mismo, comenzando por la sección “Exportar la traducción”.

### Consejos y trucos

Esta sección intenta proporcionar un conjunto de consejos y trucos útiles de traducción. Tenga en cuenta que algunos de estos trucos pueden requerir conocimientos de desarrollo.

#### Encontrar el contexto

Hacer una buena traducción requiere conocer el contexto exacto donde aparece la cadena que estamos traduciendo. Desafortunadamente, el contexto en el archivo XML no es nada claro y, en ocasiones, es necesario profundizar en la aplicación para obtener el contexto exacto. Aquí tiene una lista de consejos para encontrarlo:

-   Lo primero y más obvio que debe tener en cuenta es el archivo que está traduciendo. `AD_MENU_TRL` representa las entradas del menú de Aplicación, `AD_MESSAGE_TRL` contiene todos los mensajes, `AD_PROCESS_TRL` se encarga de los procesos e informes, `AD_PROCESS_PARA_TRL` son los parámetros del proceso, etc.
-   La funcionalidad Elementos vinculados de Etendo puede mostrarle todos los lugares donde se utiliza un registro. En la captura de pantalla siguiente, puede ver los lugares donde se utiliza el elemento con el nombre “Moneda de crédito del libro mayor”. En este caso, los elementos vinculados muestran que el elemento solo se utiliza en una columna, por lo que el usuario puede navegar a esta columna y, posteriormente, navegar al campo relacionado, que mostrará la ventana donde se utiliza.  
     
    ![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-and-update-translation-modules/how-to-create-and-update-translation-modules-10.png)

---

Este trabajo es una obra derivada de [Cómo crear y actualizar módulos de traducción](https://wiki.openbravo.com/wiki/How_to_Create_and_Update_Translation_Modules){target="\_blank"} de [Openbravo Wiki](https://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.