---
title: Conceptos de modularidad
tags:
    - Módulo
    - Modularidad
    - Conceptos
    - Extensiones

status: beta
---

# Conceptos de modularidad

!!! example  "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.
## Visión general

Etendo incorporó el nuevo concepto de **Modularidad**: la capacidad de que los desarrolladores creen, empaqueten y distribuyan **Módulos de Extensión** y de que los usuarios instalen, desinstalen y actualicen **Módulos de Extensión**.

Un **Módulo de Extensión** es una pieza de funcionalidad adicional que puede desplegarse de forma opcional e independiente sobre Etendo. Algunos ejemplos de módulos son: informes adicionales, ventanas adicionales, conectores, paquetes de contenido (traducciones, plan de cuentas, lista de códigos de impuestos, Categorías de Productos, etc.).

Los objetivos de la modularidad son:

- Facilitar la contribución a Etendo permitiendo un desarrollo y mantenimiento distribuido y desacoplado de funcionalidades opcionales.
- Proporcionar a la Comunidad un conjunto amplio de extensiones para satisfacer sus requisitos empresariales específicos sin sobrecargar el producto core.
- Acortar los ciclos de implantación permitiendo a los integradores de sistemas desarrollar plantillas microverticales.

Este documento contiene una visión general del proceso de desarrollo de Módulos de Etendo.
## Conceptos

Antes de comenzar, es necesario comprender algunos conceptos. Estos conceptos se describen en detalle en las siguientes secciones.

### Tipos de módulos de extensión

Existen tres tipos de **módulos de extensión**:

- **Módulo**: Contenedor de contenido base. Dentro de un **Módulo**, puede incluir todo tipo de artefactos excepto **scripts de configuración**: componentes del Diccionario de Aplicación, recursos de software y datos de referencia. Los **Módulos** son la forma de añadir nuevos elementos a Etendo. En un **Módulo**, no puede modificar elementos de otros módulos (incluido el core). El motivo es evitar dependencias cruzadas entre ellos.
- **Bundle**: un **Bundle** es una colección de módulos y nada más. Están pensados para simplificar el despliegue y para fomentar módulos de grano fino. Los bundles especiales son los bundles de localización y de verticalización.
- **Plantillas**: una combinación de un **Módulo** y un **script de configuración** que es capaz de modificar el comportamiento de los componentes del Diccionario de Aplicación en **Módulos**.

!!! info
    Los tres se denominan genéricamente **Módulos**.

### Artefactos en un módulo de extensión

Existen cuatro tipos de artefactos que se pueden incluir en un **módulo de extensión**:

- **Componentes del Diccionario de Aplicación**: metadatos que describen Etendo, como Ventanas, Solapas, Campos, Mensajes, etc.
- **Recursos de software**: componentes de Etendo no expresados como metadatos, como la definición `XML` de objetos del esquema de base de datos, clases Java, archivos XML, etc.
- **Datos de referencia**: información de negocio referida por las transacciones y que tiende a no cambiar con frecuencia, como *planes contables*, *códigos de impuestos*, *Banco-Sucursal*, *Categorías de Productos*, etc. Se pueden definir a nivel de sistema, cliente u organización.
- **Script de configuración**: cambios en *componentes del Diccionario de Aplicación* aplicados a otros módulos para soportar un conjunto específico de procesos de negocio, como **ocultar / mostrar** solapas o campos, sustituir procesos estándar, etc. Solo se permiten cambios significativos.

La propia plataforma Etendo no se puede modificar mediante módulos. En particular, no está permitido modificar wad (código src-wad) en un módulo. No debería ser una limitación, ya que la plataforma está diseñada para ser extensible.

### Empaquetado y archivos .zip y .jar

Todo el contenido de un módulo (código, archivos de utilidad, datos) se contiene en una carpeta separada para cada módulo. Todo el contenido de esa carpeta está relacionado con, y solo con, ese módulo. Existe una carpeta dentro de la carpeta principal de Etendo llamada **modules** donde se encuentran todos los módulos que usted ha instalado o desarrollado. Para cada módulo existe una carpeta identificada por el paquete Java del módulo. En esa carpeta, la estructura del código fuente de Etendo (config, src, src-db, lib, etc.) se replica según sea necesario para almacenar el contenido del módulo.

!!! info
    Los módulos se distribuyen como archivos `.zip` o `.jar`, que son archivos comprimidos de la carpeta del módulo.

![alt text](../../../assets/developer-guide/etendo-classic/concepts/modularity-concepts/modularity-concepts-0.png)

### Repositorio de Etendo Software en GitHub

Los módulos soportados de Etendo se publican como paquetes bajo la organización Etendo Software en GitHub. Los desarrolladores con licencia y los partners con acceso pueden explorar y descargar cualquier paquete o repositorio disponible allí.

!!!info
    Puede encontrar una descripción detallada sobre los repositorios de Etendo en las guías [Publicación de módulos](../how-to-guides/how-to-publish-modules-to-github-repository.md) y [Uso de repositorios en Etendo](../getting-started/installation/use-of-repositories-in-etendo.md).
## Introducción al proceso de desarrollo de un Módulo

El proceso de desarrollo de un Módulo tiene tres pasos principales:

1. **Registrar** su Módulo en el Diccionario de Aplicación.
2. **Desarrollar** los artefactos incluidos en su Módulo. Dependiendo de la especificación funcional y del diseño técnico de su módulo, podría incluir solo un tipo de artefactos o una combinación de ellos. En las siguientes secciones, cada tipo de artefacto se describe en detalle.

El paso 1 es común a todos los tipos de módulos. El paso 2 depende de los requisitos de su módulo. No ha cambiado significativamente respecto a la forma en que ha desarrollado código de Etendo en versiones anteriores.  
Tenga en cuenta que, a partir de ahora, cada pieza de código de Etendo pertenece a un módulo (puede ver, por ejemplo, que la distribución de Etendo de hecho incluye varios módulos, y uno de ellos es **Core**). Debe realizar todos sus nuevos desarrollos mediante módulos, incluidas sus personalizaciones. Aun así, puede realizar cambios directamente en otros módulos —incluido el core de Etendo—, pero se recomienda encarecidamente no hacerlo. El mantenimiento será mucho mejor si mantiene sus cambios aislados realizándolos mediante módulos, ya que puede actualizar módulos individuales sin realizar cambios en otros (por ejemplo, puede actualizar los módulos de la distribución de Etendo sin realizar ningún cambio en sus módulos).

Las siguientes secciones describirán cada paso en detalle.

### Registrar un Módulo

Lo primero que debe hacer es crear una nueva entrada de Módulo en la ventana Módulo dentro de la carpeta de menú Diccionario de Aplicación.

![alt text](../../../assets/developer-guide/etendo-classic/concepts/modularity-concepts/modularity-concepts-1.png)

Hay algunos detalles que debe tener en cuenta:

- Cada módulo tiene su propio **Idioma** nativo (base). En las siguientes secciones se describe el proceso de traducción; por ahora, simplemente elija el idioma que prefiera para desarrollar la UI de su módulo. Por supuesto, si elige inglés será más fácil difundirlo (p. ej., encontrar personas que lo traduzcan a otros idiomas).
- `Name`, `description` y `help` son las propiedades utilizadas para explicar en el Repositorio Central qué es su módulo. Escríbalas en estilo natural usando el idioma nativo que haya elegido.
- El **Número de Versión** se compone de tres números separados por dos puntos para ajustarse a la plantilla de Etendo para números de versión. En este campo, debe indicar la versión actual en la que está trabajando (puede haber múltiples versiones de su módulo). Más adelante en este documento, se explican en detalle los [Números de versión](#números-de-versión-y-cómo-se-gestionan-las-dependencias-y-las-inclusiones).
- El **Paquete Java** es un identificador único de su módulo y debe cumplir las reglas de nombres de empaquetado Java tal y como se describe en la especificación de Java ([Nombre](https://docs.oracle.com/javase/specs/){target="\_blank"} y [nombres de paquetes](https://docs.oracle.com/javase/specs/#6.8.1){target="\_blank"}). Debe establecer este valor cuidadosamente porque no se le permite cambiarlo una vez que su módulo se publica. Si su módulo incluye archivos java, deben empaquetarse dentro del paquete java de su módulo o en subpaquetes dentro de este. Ejemplos de paquetes java para un módulo son `com.yourcompany.yourPackage`, `org.yourfoundation.yourPackage.yourSubpackage`, etc. Observará que los módulos publicados por Etendo comienzan por `com.etendoerp`. Debe nombrar sus módulos con un paquete Java que no comience por `com.etendoerp`, sino con un identificador suyo, de su empresa o del proyecto al que pertenezca.
- Elija el tipo (Módulo, Pack, Plantilla) tal y como se describe en la sección [Conceptos](#conceptos).
- **En Desarrollo** es una propiedad booleana para que el sistema sepa que usted está desarrollando ese módulo. Solo los módulos **En Desarrollo** serán exportados por las herramientas de desarrollo y el Sistema mostrará un error si intenta modificar algún componente en un módulo que no esté En Desarrollo.
- Aunque pueda tener más de un módulo En Desarrollo, puede establecer cuál se elige por **Valor por defecto** al desarrollar. Esto es solo una forma de establecer un valor por defecto para el módulo cuando edita el Diccionario de Aplicación.

    !!! info
        Se recomienda reiniciar la instancia después de cambiar el estado de desarrollo de un módulo para actualizar el estado de la caché. Tenga en cuenta también que las instancias de producción no pueden tener módulos en estado "En Desarrollo".

- Algunos módulos no tendrán UI (p. ej., un conector a un sistema bancario o un servicio web), por lo que no es necesario traducirlos.
- Si su módulo es un módulo de traducción de otro módulo, debe marcar el campo **Es un módulo de traducción** para permitir que los usuarios busquen traducciones. Más adelante en este documento hay una descripción completa de cómo crear un módulo de [Traducción](#traducción).
- Si su módulo tiene un **Plan contable**, debe marcar este indicador para permitir que el Sistema lo utilice durante los procesos de Crear entidad/Crear organización. Más adelante en este documento hay una descripción completa de cómo añadir un [Plan contable (CoA)](#plan-contable-coa) a su módulo.
- Si su módulo tiene **Datos de Referencia** estándar, debe marcar este indicador para permitir que el Sistema los utilice durante los procesos de Crear entidad/Crear organización. Más adelante en este documento hay una descripción completa de cómo añadir [Datos de Referencia estándar](#datos-de-referencia-estándar) a su módulo.
- También debe elegir la licencia que está utilizando para distribuir su módulo. Seleccione un **Tipo de Licencia** de la lista desplegable y escriba el acuerdo de licencia que se mostrará al usuario al instalar o actualizar su módulo. Tenga en cuenta que Etendo no supervisa el contenido de su módulo ni la licencia que haya elegido. Usted es responsable de establecer esta información correctamente.
- El autor del módulo se mostrará al Usuario durante la instalación. Además, el Usuario podrá navegar desde allí a la **URL** del módulo.
- Si está trabajando en una nueva versión de su módulo, puede explicar cuáles son los cambios que incluye esta nueva versión (errores corregidos en versiones menores, nuevas funcionalidades en las mayores) en el campo **Información de la Actualización**.

La solapa **Incluir** está destinada únicamente a **Packs** y **Plantillas de Industria**. En esta solapa, incluye todos los módulos que son miembros del Pack. Solo puede elegir entre los que tenga instalados en su instancia. Debe proporcionar el **Número de Versión** para cada uno de ellos siguiendo la plantilla de Etendo tal y como se describe. En una sección posterior se describe cómo el sistema gestiona los [Números de versión](#números-de-versión-y-cómo-se-gestionan-las-dependencias-y-las-inclusiones) de **Incluir** (para Packs y Plantillas de Industria) y de **Dependencias** (para Módulos).

La solapa **Dependencia** está destinada únicamente a Módulos. En esta solapa, declara todos los Módulos de los que depende su Módulo. Es de suma importancia que los declare correctamente, ya que el sistema comprobará que las dependencias se cumplen cuando el Usuario instale o actualice su módulo. También es importante declararlas tan pronto como sea consciente de ellas, porque algunas herramientas y procesos del desarrollo tienen en cuenta las dependencias y el resultado podría ser incorrecto si no se declaran durante el desarrollo de su módulo. Usted declara dependencias entre los módulos que tiene instalados en su instancia.  
Normalmente, un módulo dependerá de User Interface Application y, a su vez, este tiene una dependencia del core de Etendo y, eventualmente, de otros módulos. Debe proporcionar el **Número de Versión** para cada Módulo del que dependa siguiendo la plantilla de Etendo. Opcionalmente, puede proporcionar un segundo **Número de Versión** (mayor que el anterior) para expresar que su Módulo depende de cualquier Número de Versión de ese módulo entre los dos proporcionados. Más adelante en este documento hay una explicación completa de [Números de versión y cómo se gestionan las dependencias y las inclusiones](#números-de-versión-y-cómo-se-gestionan-las-dependencias-y-las-inclusiones).

No es necesario editar la solapa **Traducción**. Es una herramienta para traductores y se describirá en la sección de [Traducción](#traducción).

![alt text](../../../assets/developer-guide/etendo-classic/concepts/modularity-concepts/modularity-concepts-2.png)

Si su Módulo incluye una tabla en el Diccionario de Aplicación, entonces necesita registrar uno (o varios) **Paquete de Datos** en su Módulo. Para una descripción completa de cómo se utilizan los paquetes, visite el [manual de desarrolladores de DAL](../concepts/data-access-layer.md). Para cada paquete debe establecer las siguientes propiedades:

- **Nombre**, que se utilizará en las entidades xml de las tablas asignadas a este
- **Descripción**, utilizada para explicar para qué sirve su paquete
- **Paquete Java**, que debe cumplir las reglas de nombres de empaquetado Java tal y como se describe en la especificación de Java ([Nombre](https://docs.oracle.com/javase/specs/){target="\_blank"} y [nombres de paquetes](https://docs.oracle.com/javase/specs/#6.8.1){target="\_blank"}). Debe ser igual al nombre del paquete del Módulo (si solo hay un paquete) o un subpaquete de este.

Si su Módulo incluye cualquier objeto del esquema de base de datos (una tabla, un procedimiento almacenado, etc.) o un mensaje de AD, entonces necesita definir el `DB_Prefix`. Es una cadena de hasta siete caracteres. Todos los nombres de sus objetos del esquema de base de datos deben comenzar con este prefijo, por lo que debe cumplir los requisitos de nombres de Oracle y PostgreSql (no distingue mayúsculas/minúsculas y se almacena en mayúsculas, caracteres alfanuméricos y debe comenzar por un carácter alfabético). Solo puede registrar un `DB_Prefix`; únicamente el Módulo core de Etendo puede tener más de uno. El `DB_Prefix` es necesario para garantizar que no haya colisiones de nombres al instalar módulos.

Una vez que haya completado la configuración de su módulo, es necesario asegurarse de que su `DB_Prefix` y su paquete java no estén ya registrados por otros Módulos, y es importante hacerlo incluso si no planea publicar su módulo.

### Nombres

Es de suma importancia utilizar nombres adecuados para los módulos, especialmente para **Paquete Java** y **Prefijo de Base de Datos**. Esta es la única garantía de que no habrá conflictos al instalar otros módulos. Puede encontrar algunas reglas de nombres [aquí](../concepts/naming-guidelines-for-modules.md).

### Paquete Java

**Paquete Java** debe ser un Paquete Java único y válido (véase arriba). Estas son instrucciones de [java.sun.com](https://docs.oracle.com/javase/specs/#40169){target="\_blank"}:

Usted forma un nombre de paquete único teniendo primero (o perteneciendo a una organización que tenga) un nombre de dominio de Internet, como sun.com. Luego invierte este nombre, componente por componente, para obtener, en este ejemplo, com.sun, y utiliza esto como prefijo para sus nombres de paquete, usando una convención desarrollada dentro de su organización para administrar adicionalmente los nombres de paquete.

!!!example
    Si su empresa se llama **Alimentos y Bebidas** y tiene un dominio de Internet llamado fandb.com, todos sus paquetes java deberían comenzar por `com.fandb`. Si crea un módulo de CRM, su paquete java podría ser `com.fandb.crm`.

!!!Note
    Tenga en cuenta que los paquetes java que comienzan por `com.etendoerp` o `com.smf` solo deberían ser utilizados por módulos distribuidos por Etendo.

### Prefijo de Base de Datos

Es una buena práctica utilizar un prefijo corto para su empresa seguido de un prefijo para su módulo. Siguiendo el ejemplo anterior, todos sus prefijos de base de datos podrían comenzar por `FB`, y el del módulo de CRM podría ser `FBCRM`.

Para determinar si el Prefijo de Base de Datos deseado ya está en uso:

- Acceda a la lista de módulos en Openbravo Forge ???
- Haga clic en el enlace Filters en la parte superior derecha de la tabla de módulos
- Asegúrese de que DB Prefix sea el criterio de filtro seleccionado
- Escriba el Prefijo de Base de Datos deseado en el cuadro de edición
- Haga clic en el botón Apply

Si no aparece ningún módulo, entonces su Prefijo de Base de Datos no se ha utilizado y debería registrarlo. Si otro módulo tiene el Prefijo de Base de Datos deseado, repita los dos últimos pasos hasta que haya creado uno no utilizado con el que esté satisfecho.

!!!info "Acerca de los módulos de personalización"  
    Normalmente, los módulos de personalización no están pensados para publicarse en el Repositorio Central. En este caso, el Prefijo de Base de Datos debería comenzar por `CUST`. Los módulos con este tipo de prefijos de base de datos no se pueden registrar en el Repositorio Central, pero son seguros frente a colisiones porque ningún otro módulo en el Repositorio Central puede usar este prefijo de base de datos. Esta es una decisión importante que debe tomarse antes de comenzar el desarrollo del módulo: en caso de que exista alguna posibilidad de publicar el módulo en algún momento, debería seguir la regla estándar; si está absolutamente seguro de que no se publicará, puede usar `CUST`.
## Desarrollo de artefactos del Módulo

Tal y como se indica en la sección de Conceptos, existen cuatro tipos de artefactos: **Componentes del Diccionario de Aplicación**, **Recursos de software**, **Datos de Referencia** y **Script de configuración**. Los requisitos de su Módulo y su diseño técnico definirán los artefactos necesarios para construir su Módulo. Este documento explica, uno por uno, los detalles que debe tener en cuenta para cada tipo de artefacto, relacionados con la modularidad. No explica cómo utilizarlos conjuntamente para construir soluciones; esto se describe en la Guía del desarrollador de Etendo. Al final de este documento, hay una explicación de varios ejemplos sencillos de `Hello World` que cubren todos los diferentes tipos de soluciones.
### Componentes del Diccionario de Aplicación (componentes AD)

La mayoría de los componentes AD se pueden incluir en su módulo, pero existen algunas excepciones que se explican más adelante en esta sección. La regla general para describir cómo se incluyen los componentes del Diccionario de Aplicación en su módulo es simple: establezca el campo de **Módulo** de ese componente a su módulo. Si solo tiene un módulo en desarrollo o está trabajando en su módulo por defecto, el sistema lo hará automáticamente.

Un componente AD solo será editable cuando el módulo al que pertenece esté **En Desarrollo**, o si existe una Plantilla de Industria en desarrollo en el sistema. Si cambia una propiedad en un componente AD que no está en desarrollo, el sistema mostrará un error para evitar que realice cambios no deseados.

Las traducciones se gestionan de una forma particular y no necesita preocuparse por ellas durante el desarrollo. Existe una descripción detallada del proceso de traducción en la sección [Traducción](#traducción). Pero recuerde que su módulo tiene un idioma nativo (base), por lo que los componentes de UI (ventanas, solapas, campos, elementos, mensajes, interfaces de texto, etc.) que desarrolle deben crearse en ese idioma.

La información de acceso no se incluye en los módulos, por lo que puede olvidarla al desarrollar su módulo. En una sección posterior se explicará cómo incluir una configuración específica para Etendo RBAC (control de acceso basado en roles).
  
![](../../../assets/developer-guide/etendo-classic/concepts/modularity-concepts/modularity-concepts-3.png)
  
Existen algunos detalles por encima de la regla general que debe comprender para tener un mejor control del contenido de su módulo. Merece la pena revisar cada tipo de componente AD.

#### Tabla y Columna

El registro de tablas en el AD es la primera excepción a la regla general. Las tablas no se asignan directamente a un módulo, sino a un paquete de datos dentro de un módulo. Esto es necesario para que el DAL gestione correctamente el empaquetado de las entidades generadas y el nombrado de XML. Solo los paquetes de los módulos **En Desarrollo** están disponibles cuando edita una tabla. El módulo de una tabla es el módulo del paquete de la tabla.

Las columnas se asignan por defecto al módulo de su tabla. Pero puede querer añadir en su módulo una columna dentro de una tabla de un módulo diferente (p. ej., añadir una nueva columna a la tabla M_Product en el módulo core). Para hacerlo, está obligado a usar una regla de nomenclatura para esa columna: su nombre físico (propiedad `ColumnName`) debe comenzar por el prefijo `EM_XXX_` donde `XXX` es el `DB_Prefix` de su módulo (teniendo en cuenta que el nombre completo de la columna no debe superar los 30 caracteres). `EM` significa `External Module`. El proceso `Create Columns from DB` tiene en cuenta todas estas reglas al importar columnas desde la base de datos. La misma regla es aplicable para la propiedad **Nombre**, que se utiliza para generar las propiedades del DAL y, por lo tanto, debe ser única entre distintos módulos.
  
![](../../../assets/developer-guide/etendo-classic/concepts/modularity-concepts/modularity-concepts-4.png)

#### Ventanas, Solapas y Campos

Ventanas, Solapas y Campos siguen la regla general. Los tres están vinculados a un módulo. Por defecto, cuando añade una solapa a una ventana, quedará vinculada al módulo de su ventana y, cuando añade un campo a una solapa, quedará vinculado al módulo de su solapa. Esto es cierto, pero cuando los módulos de la ventana o de la solapa no están **En Desarrollo**, entonces se propondrá el módulo por defecto. El proceso `Create fields` tiene en cuenta todas estas reglas al crear campos a partir de columnas de tabla.

Al editar la secuencia de campos, el sistema garantizará que no cambie el número de secuencia de campos que no están en su módulo, por lo que si añade un nuevo campo en una solapa de otro módulo, el número de secuencia de los campos originales no se modificará. Si edita manualmente esta información, tenga en cuenta que no puede modificar información en un módulo que no esté **En Desarrollo**. Esto también aplica si está añadiendo una solapa adicional a una ventana de otro módulo.

La clase y el mapeo de la solapa se gestionan automáticamente por el sistema y no necesita ocuparse de ello. En una sección posterior se explica cómo se gestionan Clase y Mapeo y qué puede hacer para añadir entradas adicionales.

#### Referencia

Existen cuatro tipos de referencias: tipo de dato, validación de lista, validación de búsqueda y validación de tabla. Solo las validaciones de lista y las validaciones de tabla se pueden incluir en un módulo distinto del core de Etendo. Los tipos de dato y las validaciones de búsqueda se soportarán en módulos en futuras versiones (actualmente requiere modificar Etendo WAD).

Todos los valores incluidos en una validación de lista se incluyen en el módulo donde se define la validación de lista. No puede añadir en su módulo nuevos valores a una validación de lista de un módulo diferente ni modificar los valores incluidos en ella.
  
![](../../../assets/developer-guide/etendo-classic/concepts/modularity-concepts/modularity-concepts-5.png)

#### Informes y procesos

Los informes y procesos siguen la regla general. Puede declarar un nuevo proceso o informe en su módulo simplemente creando una nueva entrada en la ventana **Informes y procesos** y vinculando esa entrada a su módulo. Todos los parámetros de un informe o proceso se incluirán en el módulo donde se declare el informe o proceso.

Para informes y procesos manuales es necesario definir el mapeo del proceso; este mapeo puede ser cualquier cosa dentro del paquete del módulo, por ejemplo `/org.mycompany.mymodule.report/MyReport.html`.

#### Formulario

Los formularios también siguen la regla general. Puede declarar un nuevo formulario en su módulo simplemente creando una nueva entrada en la ventana **Formulario** y vinculando esa entrada a su módulo.

Para formularios es necesario definir el mapeo del formulario; este mapeo puede ser cualquier cosa dentro del paquete del módulo, por ejemplo `/org.mycompany.mymodule.form/MyForm.html`.

#### Mensaje

Los mensajes siguen la regla general, pero con un detalle adicional que debe revisar. Puede declarar un nuevo mensaje en su módulo simplemente creando una nueva entrada en la ventana **Mensaje** y vinculando esa entrada a su módulo, y la clave de búsqueda del mensaje debe comenzar por el prefijo de base de datos de su módulo (para evitar colisiones entre mensajes de distintos módulos). Esto significa que no puede incluir en su módulo un mensaje con una clave de búsqueda numérica para ser lanzado por un objeto PL/SQL mediante la función RAISE_APPLICATION_ERROR. Para más información, visite [Mensaje](../concepts/messages.md).

#### Texto interfaces

La ventana **Texto interfaces** normalmente no se edita manualmente, sino que las entradas se generan automáticamente mediante el proceso de traducción cuando analiza los archivos a traducir. Este proceso tiene en cuenta el empaquetado del archivo que se está traduciendo y la entrada de interfaz de texto se asigna correctamente al módulo. Este proceso debería ser transparente para los desarrolladores, pero puede explorar las entradas que sus desarrollos manuales han creado y editarlas.

Existe una descripción detallada del proceso de traducción en la sección [Traducción](#traducción).

#### Elemento

Los elementos normalmente se generan automáticamente mediante el proceso de sincronización de terminología cuando crea nuevas columnas. Este proceso tiene en cuenta el nombre de las columnas que ha incluido en su módulo y busca en su módulo y en los módulos de los que su módulo depende un elemento con ese nombre de columna. Si se encuentra, su columna quedará vinculada a ese elemento; si no, se creará un nuevo elemento en su módulo. Este proceso debería ser transparente para los desarrolladores, pero puede explorar los elementos incluidos en su módulo y editarlos.

#### Categoría de campo, Entrada auxiliar, Callouts y Validaciones

Estos cuatro componentes del Diccionario de Aplicación también siguen la regla general. Puede declarar un nuevo componente de estos en su módulo simplemente creando una nueva entrada en la ventana correspondiente y vinculando esa entrada a su módulo.

El nombre de la entrada auxiliar debe comenzar con el prefijo de base de datos del módulo.

#### Mapeo Modelo - Implementación

El mapeo Modelo - Implementación es una generalización del concepto Modelo-Objeto que estaba presente en versiones anteriores. Puede ver una descripción detallada en la explicación del [concepto Modelo - Implementación](#concepto-modelo---implementación).

A través de esta nueva ventana puede incluir en su módulo las entradas que necesita añadir al archivo `web.xml` del contexto de Etendo.
  
![](../../../assets/developer-guide/etendo-classic/concepts/modularity-concepts/modularity-concepts-6.png)

Los mapeos Modelo - Implementación siguen la regla general. Puede declarar una nueva entrada en su módulo simplemente creando un nuevo registro en la ventana de mapeo Modelo - Implementación y vinculando esa entrada a su módulo. Todos los mapeos y parámetros asignados a ella se incluirán en el módulo donde se declare el mapeo Modelo - Implementación.
### Recursos de software

Para desarrollar su módulo puede necesitar incluir algunos recursos de software. Los recursos de software son componentes de Etendo que no se expresan como metadatos, como por ejemplo la definición en XML de un objeto del esquema de base de datos, clases Java, librerías JAR, archivos XML, etc. Todo lo que necesite añadir a su módulo debe empaquetarse dentro de `EtndoMainFolder/modules/yourModuleJavaName` (p. ej., para el módulo `com.etendoerp.examples.helloworld` el empaquetado es `/opt/EtendoERP/modules/com.etendoerp.examples.helloworld` en Linux). Dentro de esta carpeta, tiene las carpetas estándar de Etendo para alojar sus recursos de software (`src`, `src-db`, `lib`, etc.).

El proceso de build de Etendo tiene en cuenta la estructura del código fuente, que está dividida en módulos. Tenga en cuenta que este concepto es completamente diferente de `srcClient`, que Etendo utilizaba en versiones anteriores: no se le permite sobrescribir físicamente un archivo en la distribución del Core de Etendo. De hecho, el empaquetado de sus recursos de software debería ubicarse en `com.suEmpresa.xxx` u `org.suEmpresa.xxx`, por lo que ya no utilizará `com.etendoerp.xxx` para empaquetar su código.

De forma similar a los componentes del Diccionario de Aplicación, aunque esta regla general de empaquetado se aplica a todos los recursos de software, existen algunos detalles para cada tipo de recurso de software (objetos del esquema de base de datos, clases Java, librerías JAR, contenido estático web, etc.) que debe tener en cuenta al desarrollar su módulo.

#### Objetos del esquema de base de datos

El flujo típico para añadir un nuevo objeto del esquema de base de datos (tabla, columna, restricción, índice, trigger, vista, procedimiento almacenado, función) o modificarlo en Etendo es el siguiente:

- un desarrollador utiliza su herramienta preferida como cliente de base de datos para el desarrollo en Oracle o PostgreSql
- usando scripts SQL o herramientas GUI, crea o modifica el objeto del esquema de base de datos en la base de datos siguiendo los estándares de Etendo.
- si el objeto del esquema de base de datos está mapeado con algún componente del Diccionario de Aplicación (Tablas y Columnas, Informes y procesos), entonces el desarrollador importa el nuevo objeto del esquema de base de datos desde la base de datos al Diccionario de Aplicación. Este proceso añade algunas nuevas líneas en las tablas del Diccionario de Aplicación. Después de eso, el desarrollador normalmente ajusta la información importada (p. ej., ejecutando el proceso de sincronizar terminología) y completa la información del Diccionario de Aplicación para describir completamente la solución objetivo. También puede requerir crear algo de código de Etendo (archivos Java, archivos XSQL, etc.) para completar la solución.
- una vez que la solución está completamente descrita, el desarrollador construye el sistema para probar que funciona como se desea
- el último proceso es exportar la base de datos a archivos `.xml` mediante `DBSourceManager`. Esta herramienta exporta cada objeto del esquema de base de datos a un archivo `.xml` que utiliza una sintaxis común tanto para Oracle como para PostgreSql, de modo que pueda tener diferentes entornos de desarrollo haciendo commit sobre la misma línea de código. Los datos del Diccionario de Aplicación también se exportan en este proceso. Por tanto, hay dos tipos diferentes de archivos `.xml` exportados por `DBSourceManager`: model (objetos del esquema de base de datos) y sourcedata (metadatos del Diccionario de Aplicación).

Desde una perspectiva de modularidad, no es necesario realizar ninguna tarea adicional para ocuparse de los metadatos del Diccionario de Aplicación, ya que el sistema los gestiona tal y como se describe en la sección anterior de [Componentes del Diccionario de Aplicación](#application-dictionary-components-ad-components). Pero para evitar colisiones de nombres en la base de datos y permitir que `DBSourceManager` conozca el módulo de los objetos del esquema de base de datos no mapeados, es necesario seguir la siguiente regla de nomenclatura para los objetos del esquema de base de datos:

- Todos los objetos principales (tablas, triggers, vistas, funciones, procedimientos almacenados) deben comenzar por el prefijo de base de datos del módulo seguido del símbolo de guion bajo ("_") (p. ej., `MYMOD_MYTABLE`, `MYMOD_MYPROCEDURE`, etc.).
- Cada objeto (tablas, restricciones, índices, funciones, triggers) necesita tener un nombre único en la base de datos. Para evitar cualquier tipo de duplicación, los nombres de restricciones e índices en particular deben comenzar con el nombre de su tabla. Esto garantiza que no habrá duplicación de nombres en toda la base de datos.
- Se supone que las subpartes de los objetos principales (columnas, restricciones, índices) pertenecen al módulo de la parte principal, excepto si su nombre comienza por `"EM_"` + prefijo de base de datos + `"_"` (p. ej., `EM_MYMOD_MYCOLUMN`, `EM_MYMOD_MYCONSTRAINT`, etc.). EM significa External Module (Módulo Externo). Por tanto, puede usar nombres de columna estándar en sus tablas (p. ej., `C_BPARTNER_ID`, `M_PRODUCT_ID`, `NAME`, etc.), pero si quiere añadir en su módulo una "parte" (columna, restricción, índice) a una tabla de otro módulo, necesita usar el prefijo `"EM_"` + prefijo de base de datos + `"_"` para el nombre de esa parte. En cualquier caso, las restricciones e índices en el mismo módulo y su tabla deben comenzar con el prefijo de base de datos del módulo; esto es así porque su nombre debe ser único en toda la base de datos.

Siguiendo esta regla simple, puede incluir en su módulo tantos objetos del esquema de base de datos como quiera. Pero tenga en cuenta que no puede modificar objetos del esquema de base de datos en otros módulos, ya que rompería la regla principal: "un módulo no puede modificar componentes en otros módulos".

Cuando `DBSourceManager` exporta la base de datos, solo tendrá en cuenta los módulos "En Desarrollo"; los demás no se exportarán. Los archivos XML exportados se ubicarán dentro de la carpeta `src-db/database` dentro de la carpeta del módulo.

Al final de este documento se explican algunos ejemplos que muestran cómo incluir en su módulo cualquier tipo de objeto del esquema de base de datos. Puede utilizarlos como referencia para desarrollar su módulo.

**Excepciones de Nombres**

Es posible definir objetos del esquema de base de datos dentro de un módulo que no sigan las reglas de nomenclatura explicadas en la sección anterior. Esto es especialmente útil para migrar a módulos instancias de Etendo existentes en versiones antiguas. Es importante señalar que **esta funcionalidad no debería utilizarse para nuevos desarrollos en general**. Si un módulo contiene una excepción de nombres, no será posible publicarlo en el Repositorio Central, porque no sería posible garantizar que el objeto definido como excepción de nombres no colisione con otro objeto definido en un módulo diferente.

Cuando un objeto del esquema de base de datos se define como una excepción para un módulo, se exporta a ese módulo en lugar de al que correspondería según su nombre y las reglas de nomenclatura.

Las excepciones se definen en `Application Dictionary` > `Module` > `Module` > solapa `Excepciones de Nombres`, que contiene dos campos:

* **Tipo de Objeto de Base de Datos** : Define el tipo de objeto de base de datos (tabla, función, índice...)
* **Nombre del Objeto** : Es el nombre del objeto de base de datos. Tenga en cuenta que es el nombre en la base de datos, no en el Diccionario de Aplicación.

**Puntos de Extensión**

Los Puntos de Extensión permiten al desarrollador adjuntar código de ejecución a puntos específicos predefinidos dentro de funciones PL/SQL de Etendo. Esta funcionalidad puede utilizarse para ampliar la funcionalidad de algunas funciones del Core, sin sobrescribirlas de ninguna manera. Esta forma de ampliar la funcionalidad encaja muy bien con la modularidad, ya que permite la extensión pero también mantiene la mantenibilidad y la capacidad de actualización.

Puede encontrar más información sobre los Puntos de Extensión [aquí](../concepts/extensionpoints.md) y [aquí](../how-to-guides/how-to-use-an-extension-point.md).

#### Clases Java, otros objetos MVC de Etendo y librerías JAR

Las clases Java, otros objetos MVC de Etendo (archivos HTML, XML y XSQL) y las librerías JAR siguen la regla general para añadir recursos de software en su módulo. Debe empaquetar este código dentro de la carpeta `src` ubicada en la carpeta de su módulo.

![](../../../assets/developer-guide/etendo-classic/concepts/modularity-concepts/modularity-concepts-7.png)

Cuando Etendo construye el sistema, añadirá dinámicamente a su proyecto Java todas las carpetas `src` dentro de todos los módulos instalados como recursos Java del proyecto. Utiliza una ubicación intermedia, la carpeta `build`, para generar código a partir de archivos XSQL y para compilar todos los recursos Java y unirlos. Puede incluir en su módulo librerías JAR hechas por usted o por cualquier tercero y utilizarlas junto con su código. Todas las librerías JAR incluidas en la carpeta `lib\runtime` dentro de su módulo se añaden al classpath en tiempo de compilación y finalmente se despliegan en el contexto de Etendo.

Al trabajar con Eclipse, si los módulos se añaden manualmente al workspace (es decir, no a través de la Consola de Gestión de Módulos), la carpeta `src/` del módulo debe añadirse manualmente al build path.

Después de la generación de código y el proceso de compilación, el proceso de build despliega todo el contenido en el contexto de Etendo en el contenedor de servlets. Hay dos modos de despliegue —class y war— que se explican más adelante en la sección de Conceptos avanzados.

#### Contenido estático web (archivos css, imágenes, javaScript)

Si necesita añadir contenido estático web (css, imágenes y javaScript) a su módulo, debe colocar estos recursos en la carpeta `web` de su módulo, dentro de una carpeta nombrada como el paquete Java de su módulo para evitar colisiones de archivos al desplegar recursos de diferentes módulos.

Cuando se construye el sistema, todos los archivos en la carpeta `web` de su módulo se copian a `WebContent` y desde ahí se despliegan al contexto de Etendo de forma estándar, de modo que estos recursos puedan ser accedidos desde las páginas de su módulo referenciándolos. Tenga en cuenta que `xmlEngine` realiza una traducción automática de URLs mediante un reemplazo de `"../../../../../web"` (parámetro replaceWhat) por `"@actual_url_context@/web"` (parámetro replacWith), siendo `"@actual_url_context@"` la ruta absoluta a su contexto de Etendo (p. ej., http://localhost:8880/openbravo  _ ).

El módulo Solitaire está diseñado para demostrar cómo incluir contenido estático web típico en su módulo. A través de este ejemplo es sencillo entender cómo funciona. Por ejemplo, este es un fragmento de Solitaire.html para referenciar el archivo solitaire.js que se encuentra dentro de la carpeta `web/org.openbravo.examples.solitaire` del módulo Solitaire:

```
<script language="JavaScript" src="../../../../../web/org.openbravo.examples.solitaire/solitaire.js" type="text/javascript"></script>
```

En tiempo de ejecución, una vez que el contexto de openbravo está desplegado y cargado, puede obtener la librería JavaScript solitaire.js desde @actual_url_context@/web/org.openbravo.examples.solitaire/solitaire.js. Cuando se entrega la página principal del módulo Solitaire, xmlEngine reemplazará `"../../../../../web"` por `"@actual_url_context@/web"` y así referenciará correctamente el recurso disponible.

También puede referenciar otros recursos de contenido estático web incluidos en el Core u otros módulos. En ese caso, recuerde declarar explícitamente la dependencia a ese módulo.

##### Archivos de configuración

También puede necesitar incluir algunos archivos de configuración en la carpeta `config` de su módulo. Estos archivos se copiarán a `WebContent/WEB-INF` cuando el sistema se construya y se despliegue en el contexto de Etendo.

Por ejemplo, en el módulo HelloWorldService hay un archivo llamado `com.etendoerp.examples.webservice-provider-config.xml` dentro de la carpeta `config`. Este archivo se copia al contexto de Etendo y, por este medio, se declara la clase que implementa el servicio web.

Para evitar colisiones de archivos desplegados por diferentes módulos, los archivos dentro de la carpeta `config` deberían estar prefijados con el PackageName del módulo.
### Datos de Referencia

La modularidad de Etendo admite **Datos de Referencia**: información de negocio a la que hacen referencia las transacciones y que tiende a no cambiar con frecuencia, como traducciones, planes contables, códigos de impuestos, Banco-Sucursal, Categorías de Productos, etc. Pueden definirse a nivel de sistema, cliente u organización y esto definirá cuándo se cargan en la instancia: la información de sistema se cargará en el momento de la instalación, mientras que la información de cliente y organización se cargará durante los procesos **Crear entidad** o **Gestión del módulo de Empresa**.

Los módulos de datos de referencia también se versionan y pueden publicar actualizaciones y mejoras durante su ciclo de vida.

Se admiten tres tipos de datos de referencia: Traducción, Plan contable y Datos de Referencia estándar.

#### Traducción

Los módulos de traducción son un tipo especial de módulo. Deben marcarse como **Es un módulo de traducción** en la ventana Módulo. No se permite ningún otro contenido que no sean traducciones en los módulos de traducción, y solo se permiten traducciones de un único módulo a un único idioma, el idioma nativo declarado para el módulo (por ejemplo, traducción del módulo core al español, traducción del módulo HR al francés). Los módulos de traducción solo dependen del módulo que traducen.

Crear un módulo de traducción es un proceso sencillo. Primero debe crear su módulo como de costumbre. Recuerde definirlo como "módulo de traducción" y definir su idioma nativo como el idioma al que va a traducir, y utilizar el idioma nativo del módulo al escribir su nombre, descripción, etc. Deje sin marcar las otras propiedades relacionadas con los datos de referencia (`Translation required`, `Has chart of accounts` y `Has reference data`). Este módulo no necesita ninguna solapa Incluir, Paquete de Datos ni Prefijo de Base de Datos y solo dependerá de la versión del módulo que está traduciendo.

A continuación, cree la carpeta principal de su módulo (nombrada como su `javapackage`) dentro de la carpeta `modules`; puede hacerlo manualmente o simplemente ejecutando la tarea Ant `export.database` (recuerde que el módulo debe estar `In Development`).

Después, todo lo que tiene que hacer es instalar el módulo que planea traducir y declarar la dependencia de su módulo de traducción respecto a ese módulo, y seguir el proceso estándar de traducción siguiendo este documento. El proceso de exportación de idiomas divide los archivos xml en diferentes carpetas para cada módulo instalado: core se exporta directamente a la carpeta del idioma (por ejemplo, es_ES) y cualquier otro módulo instalado se exportará a una carpeta nombrada con el nombre del paquete del módulo dentro de la carpeta del idioma (por ejemplo, `es_ES/org.openbravo.examples.helloworld`). Una vez completada la traducción, debe copiar los archivos xml traducidos del módulo traducido (solo esos) a la carpeta `referencedata/translation` dentro de la carpeta de su módulo, y empaquetarlo como de costumbre ejecutando la tarea ant `package.module-Dmodule="yourModuleJavaPackage"`, que creará un archivo `.obx` listo para publicarse o distribuirse.

La información de traducción siempre está a nivel de sistema. Cuando se instala un módulo de traducción, el proceso se encarga de todos los detalles para importar un paquete de traducción: marcará el Idioma como Idioma de Sistema si no lo era y cargará todas las traducciones en el Diccionario de Aplicación de Etendo.

#### Plan contable (CoA)

Normalmente debería añadir solo un plan contable en su módulo, aunque puede crear tantos módulos que incluyan CoA como desee y luego agruparlos en un pack si es necesario. Los planes contables se almacenan en un archivo .csv específico.

Es fácil crear un módulo que incluya un plan contable una vez que haya preparado el archivo .csv. Todo lo que necesita hacer es crear un nuevo módulo y marcar la propiedad `Has a chart of Accounts`. Deje sin marcar las otras propiedades relacionadas con los datos de referencia (`Translation required`, `Istranslation module` y `Has reference data`). Este módulo no necesita ninguna solapa Incluir, Paquete de Datos ni Prefijo de Base de Datos y solo dependerá de la versión del core que esté utilizando (la estructura del archivo .csv se define en core).

A continuación, cree la carpeta principal de su módulo (nombrada como su `javapackage`) dentro de la carpeta `modules`; puede hacerlo manualmente o simplemente ejecutando la tarea ant `export.database -Dmodule=yourModuleJavaPackage` (recuerde que el módulo debe estar `In Development`). Dentro de la carpeta principal debe crear la subcarpeta `referencedata` (todo en minúsculas) y dentro de ella la carpeta `accounts` y colocar allí su archivo .csv. Recuerde que las carpetas distinguen entre mayúsculas y minúsculas, por lo que la carpeta debe nombrarse de forma idéntica y usar la capitalización correcta.

Ahora su módulo está listo para ser empaquetado. Ejecute la tarea ant `package.module-Dmodule="yourModuleJavaPackage"` y creará un archivo .obx listo para publicarse o distribuirse.

Los planes contables siempre están a nivel Cliente/Organización, por lo que al instalar este tipo de módulos no ocurre nada más que el plan contable queda disponible para aplicarse a nuevos clientes (durante Crear organización), nuevas organizaciones (durante Crear organización) o a Cliente/Organizaciones existentes (mediante Gestión del módulo de Empresa).

#### Datos de Referencia estándar

También puede incluir cualquier otro dato en su módulo mediante datos de referencia estándar usando conjuntos de datos.

Primero necesita crear en su instancia los datos que desea incluir. Podrían ser impuestos para un país concreto, Categorías de Productos o una colección de alertas para un sector específico, o cualquier otro dato. Puede combinar diferentes datos de distintas tablas en su módulo.

Después, el siguiente paso es crear un módulo y marcar la propiedad `Has reference data`. Deje sin marcar las otras propiedades relacionadas con los datos de referencia (`Translation required`, **Es un módulo de traducción** y `Has chart of accounts`). Complete `Reference data description` con información sobre los datos que está incluyendo (esta descripción puede ser diferente de la descripción del módulo, ya que el módulo podría incluir otro contenido). Este módulo no necesita ninguna solapa Incluir, Paquete de Datos ni Prefijo de Base de Datos y dependerá de las versiones de los módulos que definen la estructura de datos que pretende incluir (por ejemplo, si sus datos provienen de una tabla definida en core 2.50.1234, entonces solo dependerá de esa versión de módulo).

A continuación, debe crear dentro de su módulo tantos conjuntos de datos como necesite para definir sus datos. Un conjunto de datos es una colección de datos definida por las tablas donde se almacenan esos datos, las filas incluidas (definidas mediante una cláusula de filtro para cada tabla) y las columnas que desea incluir para cada tabla. Los conjuntos de datos admiten una definición avanzada de datos para incluir objetos de negocio completos (por ejemplo, al incluir una factura puede solicitar al sistema que incluya también todos sus miembros: líneas, impuestos, etc.). Haga clic aquí para una descripción general de los conjuntos de datos.

Puede crear conjuntos de datos en la ventana **Data Set** dentro de la carpeta de menú Diccionario de Aplicación.

![](../../../assets/developer-guide/etendo-classic/concepts/modularity-concepts/modularity-concepts-8.png)

Hay algunos detalles que debe tener en cuenta al crear conjuntos de datos:

* El conjunto de datos debe asignarse a su módulo, en el que distribuirá esos datos.
* El nivel de acceso a datos está relacionado con el nivel de acceso a datos en las tablas del Diccionario de Aplicación; lea aquí para más detalles. Define el nivel al que se importarán esos datos (por supuesto, estará restringido a los niveles permitidos por la tabla donde se almacenan los datos) y cuándo se importan los datos en la instancia que instala el módulo:
    * **System only**: se importará a nivel de sistema en el momento de la instalación. Solo se permiten tablas con nivel de acceso a datos `System only`, `System/client` y `All` en conjuntos de datos **System only** (por ejemplo, Roles, reglas de alerta, etc.).
    * **System/client**: se importará a nivel de cliente durante los procesos "Crear entidad" o "Gestión del módulo de Empresa". Solo se permiten tablas con nivel de acceso a datos `System/client`, `Client/organization` y `All` en conjuntos de datos **System/client** (por ejemplo, Roles, Categorías de Productos, etc.).
    * **Client/organization**: se importará a nivel de cliente u organización durante los procesos **Crear entidad**, **Crear organización** o **Gestión del módulo de Empresa**. Solo se permiten tablas con nivel de acceso a datos **Client/Organization** y **Organization** en conjuntos de datos **Client/Organization** (por ejemplo, Categorías de Productos, terceros, etc.).
    * **Organization**: se importará a nivel de organización durante los procesos "Crear organización" o "Gestión del módulo de Empresa". Solo se permiten tablas con nivel de acceso a datos **Client/Organization**, **Organization** y **All** en conjuntos de datos **Organization** (por ejemplo, terceros, pedidos de venta, etc.).
* Marque el campo **Permitir exportar** para mostrar el botón **Exportar Datos de Referencia**. Con este botón, podrá exportar sus datos a archivos xml y de este modo incluirlos en su archivo .obx.

El siguiente paso es definir la colección de tablas incluidas en su conjunto de datos.

![alt text](../../../assets/developer-guide/etendo-classic/concepts/modularity-concepts/modularity-concepts-9.png)

De nuevo, algunos detalles que debe tener en cuenta:

* Puede añadir tantas tablas como necesite en su conjunto de datos.
* Para cada tabla puede añadir una `SQL where clause` para filtrar los datos en la tabla. En el ejemplo anterior, se filtra por Categorías de Productos en un cliente concreto. Haga clic aquí para más información sobre las cláusulas where de DatasetTable.
* Puede incluir todas las columnas de la tabla o declarar una por una las que desea incluir.
* Normalmente no querrá incluir información de auditoría en sus datos; puede excluir las columnas de información de auditoría.
* Por defecto, su conjunto de datos incluye solo los registros de las tablas del conjunto de datos que coinciden con los criterios de la cláusula SQL where. Pero puede definir la tabla en su conjunto de datos como **Is business object**. Si lo hace, entonces el sistema exportará no solo los registros de la tabla que coinciden con su cláusula SQL where, sino de forma recursiva cualquier otro registro del sistema que tenga una clave foránea a esos registros y que esté definido como miembro del registro referenciado (objeto de negocio) mediante el atributo **Is parent** en la columna del Diccionario de Aplicación.

Tenga en cuenta que el sistema exportará no solo los datos definidos por su conjunto de datos, sino también cualquier información referenciada por él. De este modo se garantiza que el sistema podrá importar esos datos en cualquier otra instancia aunque los datos referenciados no existan allí. Si ese es el caso, el proceso de importación también importará cualquier dato referenciado necesario para completar la operación.

Ahora debe definir las columnas incluidas para cada tabla.

![alt text](../../../assets/developer-guide/etendo-classic/concepts/modularity-concepts/modularity-concepts-10.png)

Normalmente no es necesario definir columnas en su tabla, ya que normalmente desea incluir todas excepto la información de auditoría, y puede hacerlo en la propia tabla como se describió antes. En algunas ocasiones puede querer excluir algunas otras columnas marcando el campo **Excluido**.

Una vez que haya completado la definición de todos sus conjuntos de datos, debe exportarlos a archivos xml para que se incluyan en su archivo .obx al empaquetar su módulo. Para ello debe hacer clic en el botón **Exportar Datos de Referencia** en la cabecera del conjunto de datos. Creará un archivo xml con el mismo nombre que el conjunto de datos en la subcarpeta `referencedata/standard` dentro de la carpeta de su módulo. Por supuesto, puede ejecutar este proceso tantas veces como necesite para ajustar sus datos. Finalmente, empaquételo como de costumbre ejecutando la tarea ant `package.module-Dmodule="yourModuleJavaPackage"`, que creará un archivo `.obx` listo para publicarse o distribuirse.

Como se describió antes, también puede publicar nuevas versiones de sus módulos de datos de referencia. Tenga en cuenta que, para garantizar la consistencia de los datos, los datos de referencia no se eliminan de la instancia al aplicar una actualización/mejora en la que el nuevo conjunto de datos no incluya algunos registros incluidos originalmente. Por lo tanto, en lugar de eliminarlos del conjunto de datos, debería inactivarlos.

#### Temas avanzados

Hay casos especiales que deben tenerse en cuenta al incluir tablas y columnas en datos de referencia.

**Todas las columnas del conjunto de datos siempre se restablecen al actualizar los datos de referencia**

En caso de que esté desarrollando un módulo que contiene un conjunto de datos con un nivel de acceso a datos **System/client**, **Client/Organization** u **Organization** (en realidad, todos los posibles excepto **System only**), debe tener en cuenta que cada vez que el usuario actualiza la aplicación de datos de referencia (a través de la ventana **Gestión del módulo de Empresa**) se actualizarán todas las columnas incluidas. Esto es útil, pero también un poco peligroso:

Imagine que necesita añadir registros pertenecientes a la tabla AD_Sequence en un conjunto de datos, e incluye todas las columnas de la tabla en el conjunto de datos.

Las secuencias se utilizan, por ejemplo, por los documentos. Cada documento tiene una secuencia asociada. Cada vez que se crea y guarda una nueva factura, la secuencia proporciona un nuevo número (almacenado en la columna `CurrentNext`) e incrementa su valor para la siguiente vez que se solicite un nuevo número.

El usuario aplica el conjunto de datos y todo va bien: las secuencias se importan a la base de datos (por ejemplo, con `CurrentNext` ='1000000'). El usuario empieza a usar la secuencia, por lo que el valor `CurrentNext` se incrementa (digamos que ahora `CurrentNext` ='1000123'). Ahora se publica una nueva versión del conjunto de datos porque, por ejemplo, se incluyen algunas secuencias más. El usuario actualiza el módulo y actualiza el conjunto de datos en la ventana Gestión del módulo de Empresa. En esa acción, el valor `CurrentNext` de la secuencia original se restablece de '100123' a '1000000' de nuevo.

¿Qué se puede hacer para evitar este tipo de problemas? Simplemente no incluya ese valor en el conjunto de datos y establézcalo mediante el valor por defecto de la columna.
### Scripts de Módulo y Validaciones de Compilación

Es posible que su módulo necesite comprobar si el sistema cumple alguna regla específica antes de instalarlo. Si este es el caso, se puede utilizar una Validación de Compilación para verificarlo. Una Validación de Compilación es básicamente un proceso, definido como una clase Java, que puede conectarse a la base de datos y a las fuentes de Etendo, comprobar lo que el desarrollador desee y, finalmente, devolver un resultado de la validación. Si el resultado no es positivo, el módulo no se aplica en el sistema.

Además, es posible que su módulo necesite realizar transformaciones específicas en el sistema durante la instalación. Estos cambios pueden ser de prácticamente cualquier tipo, como modificar algunos datos en el sistema o añadir algún objeto de base de datos que utilice sintaxis específica de Oracle o PostgreSQL, lo que hace que no sea posible añadirlo mediante nuestros archivos estándar dbsourcemanager+xml. Para ello, puede utilizar Scripts de Módulo que, al igual que las Validaciones de Compilación, se definen como una clase Java que puede conectarse a la base de datos y realizar cualquier tipo de modificaciones en los datos del cliente.

Si desea saber más sobre cómo crear Validaciones de Compilación y Scripts de Módulo, puede consultar este [enlace](../how-to-guides/how-to-create-build-validations-and-module-scripts.md). Si tiene previsto utilizar un script de módulo para crear un objeto de base de datos que use algún tipo de sintaxis o funcionalidad específica de la base de datos, debe excluirlo del modelo estándar de dbsourcemanager. Para saber cómo hacerlo, lea [este documento](../how-to-guides/how-to-exclude-database-physical-objects-from-model.md).
### Script de configuración

Hasta ahora hemos visto cómo ampliar Etendo mediante módulos. Como recordará, los módulos pueden añadir nuevos artefactos —componentes del Diccionario de Aplicación, recursos de software y datos de referencia—, pero no tienen permitido modificar otros módulos para evitar dependencias cruzadas entre ellos.

Pero existe un tipo especial de módulos —plantillas de industria— que puede incluir cambios en otros módulos dentro de la propia plantilla. Esto se realiza mediante scripts de configuración. Un script de configuración es una colección de cambios que su plantilla de industria realiza en otros módulos incluidos en la plantilla de industria.

Crear un script de configuración es sencillo. No necesita editarlo manualmente, ya que el sistema lo generará automáticamente a medida que usted avance. Solo necesita crear una plantilla de industria en su instancia. Solo puede tener una plantilla de industria «en desarrollo» a la vez y cualquier cambio que realice se incluirá en el script de configuración de esa plantilla de industria.

!!!info
    Si quiere saber más sobre cómo crear plantillas de industria y scripts de configuración, puede consultar este documento.
### Tareas de desarrollo

Lea [Tareas de compilación de desarrollo](../developer-tools/etendo-gradle-plugin.md#build-tasks) para obtener una explicación completa de todas las tareas de desarrollo disponibles.


## Conceptos avanzados

Esta sección explica en detalle algunos conceptos avanzados de la modularidad de Etendo. No es estrictamente necesario que lea todos estos detalles, pero merece la pena hacerlo, ya que le ayudará a evitar errores al crear sus módulos.  

### Números de versión y cómo se gestionan las dependencias y las inclusiones

Las distintas versiones de un Módulo de Etendo se identifican mediante un **número de versión**. Un número de versión de Etendo es una cadena de hasta 10 caracteres de longitud que sigue el formato x.y.z, donde:

* x es un número que indica la generación del módulo (p. ej., cambios muy relevantes en funcionalidad, interfaz de usuario o tecnología) 
* y es un número que indica la versión mayor (p. ej., nuevas funcionalidades disponibles de forma regular) 
* z es un número que indica la versión menor. Las versiones menores no deberían añadir ninguna funcionalidad nueva, sino únicamente corregir errores dentro de su versión mayor con el objetivo de aumentar la estabilidad 

Una versión mayor se identifica por los dos primeros dígitos (x e y). Por ejemplo, core 3.0.13642 y core 3.0.13921 son dos versiones menores diferentes dentro de la versión mayor core 3.0.

Los módulos deben declarar cualquier dependencia entre ellos y todos deben depender finalmente del módulo core. Las dependencias se declaran para una versión mayor concreta de un módulo o para un rango de versiones mayores, comenzando desde una versión menor concreta. Por ejemplo, el módulo A depende de core 2.50 o el módulo B depende de cualquier versión del módulo A desde la versión 1.0 hasta la versión 1.6. De forma similar, los Packs y las Plantillas de Industria declaran los módulos (incluyendo otros packs y Plantillas de Industria) que se incluyen dentro de ellos. En este caso no se admiten rangos; solo se puede incluir en un Pack/Plantilla de Industria una versión mayor de un módulo. Tenga en cuenta que tanto las dependencias como las inclusiones utilizan un número de versión completo (x.y.z) para identificar la versión; la versión menor se tiene en cuenta para definir la versión inicial de la dependencia, pero no para el campo **to version**. En este caso, la versión menor (.z) se utiliza únicamente para llevar el control de la versión real que se usó cuando se desarrolló el módulo.

Normalmente, una versión mayor madura mediante un proceso con tres fases de estabilidad creciente: alpha, beta y producción. Se pueden publicar muchas versiones menores en cada fase, pero la versión no puede considerarse lo suficientemente estable como para construir algo encima de ella hasta que se alcanza la fase beta. No debería desarrollar un módulo que dependa de una versión alpha de otro módulo para evitar inestabilidades inherentes a esta etapa.

Para mejorar la mantenibilidad, las versiones menores de los módulos no se tienen en cuenta al gestionar dependencias. Esto significa que, en el ejemplo anterior, el módulo A debería ser compatible con cualquier versión menor de core 2.50 (es una buena idea especificar también la versión menor en la que se desarrolló el módulo, para evitar la necesidad de probarlo en versiones menores anteriores). Esto provoca algunas limitaciones sobre lo que los desarrolladores pueden hacer cuando trabajan en una versión menor, pero mejora enormemente la mantenibilidad al minimizar el esfuerzo de comprobación de dependencias. Solo necesita revisar si su módulo sigue siendo compatible con un módulo del que depende cuando se publica una versión mayor de ese módulo. ???

Para imponer este comportamiento, es de suma importancia indicar claramente qué cambios están prohibidos dentro de una versión menor y hacer que se validen antes de publicar. La regla general es que la API pública del módulo no debería cambiar, y puede expresarse con más detalle mediante el siguiente conjunto de cambios no permitidos dentro de una versión menor:

* Modelo de datos 
    * Añadir una columna obligatoria en una tabla sin un valor por defecto o oncreatedefault. Se permiten nuevas columnas no anulables solo si tienen un valor por defecto u oncreatedefault correspondiente, que pueda aplicarse a los registros existentes sin esta columna. Para más información, visite [Valores por defecto al crear](../how-to-guides/how-to-define-an-on-create-default.md).  
    * Cambiar el tipo de dato o reducir longitud/precisión en una columna 
    * Eliminar una columna 
    * Renombrar una columna: es equivalente a eliminar y crear esa columna 
    * Añadir una nueva restricción a una tabla que anteriormente no era aplicada por la aplicación. Se permiten restricciones para evitar comportamientos incorrectos, pero deberían advertirse. 
* Lógica de negocio 
    * Cambios en la firma de métodos/procedimientos/webServices públicos: nombre del método, número y tipo de parámetros, tipo de retorno y excepciones lanzadas 
    * Cambios en el comportamiento funcional esperado (p. ej., significado de una columna/atributo concreto, etc.) 
* Navegación 
    * Cambios en las URL para navegación directa a componentes web (ventanas, informes, etc.) 

Estas restricciones hacen que el ejercicio de corregir errores sea más difícil, pero son un factor clave para crear un ecosistema mantenible. Deben garantizarse durante la fase beta y de producción de cualquier versión de cualquier módulo. Durante la fase alpha —cuando la actividad de corrección de errores es alta— podría romper esta regla para obtener cierta flexibilidad, teniendo en cuenta que no debería haber ningún otro módulo que dependa de él.

#### Tipos de dependencia

El tipo de dependencia se define mediante el campo **Obligación de dependencia**; los valores posibles que puede tomar son:

* **Versión mayor** : Esta es la obligación por defecto y funciona como se describe arriba. 
    * **Primera versión** es la primera versión menor con la que la dependencia es compatible. Por tanto, si la primera versión es 1.1.5, será compatible con todas las versiones menores 1.1.x a partir de 1.1.5, pero no con ninguna otra versión mayor como 1.2.0, a menos que se defina **Última versión**. 
    * En caso de que se defina **Última versión**, solo se tiene en cuenta si es una versión mayor distinta de la primera versión; en ese caso define la última versión mayor compatible, pero su versión menor no se tiene en cuenta. Por ejemplo, si la dependencia se define de 1.1.5 a 1.3.6, el módulo será compatible con todas las 1.1.x a partir de 1.1.5, con cualquier versión 1.2.y y con cualquier 1.3.z (incluyendo versiones menores de 1.3 superiores a 1.3.6). 
    * Si **Última versión** está en blanco o está dentro de la misma versión mayor en la que está **Primera versión**, la compatibilidad se define para todas las versiones dentro de la misma versión mayor en la que está **Primera versión**, a partir de la versión menor que define **Primera versión**. 
* **Versión menor** : En caso de que estén definidas tanto **Primera versión** como **Última versión**, la compatibilidad va desde la versión menor en **Primera versión** hasta la versión menor en **Última versión** (aunque pertenezcan a la misma versión mayor). Si **Última versión** está en blanco, la única versión compatible será la definida por **Primera versión**. 
* **Ninguna** : No hay restricción entre versiones mayores; **Primera versión** define la primera versión menor compatible y la compatibilidad es para todas las versiones superiores a esta, incluyendo versiones mayores. Normalmente no debería usarse este tipo. 

##### Obligación editable

El propietario del módulo puede definir si la obligación puede ser sobrescrita por el usuario. Por defecto, no lo es.

En caso de que sea posible sobrescribir la obligación de la dependencia del módulo, el usuario podrá establecer una obligación diferente para esta dependencia en su instancia, siendo este valor el que se utilice para calcular dependencias.

Los usuarios pueden seleccionar la obligación para dependencias con **Obligación editable** desde la solapa **Settings** en la ventana **Gestión de Módulo**.

### Concepto Modelo - Implementación

AD_Model_Object es una tabla en el Diccionario de Aplicación de Etendo para enlazar componentes del Diccionario de Aplicación y la clase (servlet) que implementa ese objeto. Por tanto, esta tabla es un mapeo entre el lado lógico (componentes AD) y el lado físico (clases). Es útil por dos motivos principales:

1. Permite implementar de forma genérica reglas que aplican a todos los componentes AD, como seguridad, navegación y otras. 
2. Es el mecanismo para poblar automáticamente el archivo web.xml donde se declaran las clases (servlets). AD_Model_Object_Mapping es una utilidad para crear las entradas de mapeo en el archivo web.xml. 

Hay un pequeño número de excepciones a esta descripción: algunos servlets que se despliegan en el contexto de Etendo pero no están enlazados a ningún componente AD, como los servlets DataGrid o AuditInfo. Se invocan desde componentes manuales o estándar (ventanas, formularios, etc.) mediante peticiones http, codificando de forma fija su url-mapping en la petición. Aun así, puede interpretarse como un mapeo de clases reales que implementan una funcionalidad que no está descrita en el modelo actual de Etendo, aunque podría estarlo en el futuro.

Mediante el uso de módulos, se permite el despliegue de cualquier tipo de contenido opcional en una instancia de Etendo, incluyendo entradas adicionales en el archivo web.xml del contexto de Etendo. Esto se realiza a través de la tabla AD_Model_Object. Los desarrolladores pueden crear entradas en esta ventana no enlazadas a ningún componente AD.
Para soportar cualquier tipo de contenido de web.xml (servlet, listeners, filtros, etc.) se añade una nueva columna a AD_Model_Object para representar el tipo de entrada de web.xml que el desarrollador está añadiendo. También pueden declarar un conjunto de mapeos para la entrada y un conjunto de parámetros si es necesario.

El módulo de una entrada de AD_Model_Object se calcula con la siguiente regla: si está enlazada a algún componente AD, entonces el módulo es el asignado a ese componente AD; en caso contrario, el módulo es el asignado al propio registro de AD_Model_Object.

Con esta extensión, el archivo web.xml en el contexto de Etendo es extensible mediante módulos.

Puede encontrar más información sobre el mapeo de objetos del modelo de Etendo [aquí](../concepts/model-object-mapping.md).
## Ejemplo de cómo crear su módulo

Ahora es el momento de ponerlo en práctica. Puede seguir [esta sección](../how-to-guides/how-to-create-a-module.md) que le guiará paso a paso sobre cómo crear su primer módulo.

---

Este trabajo es una obra derivada de [Conceptos de modularidad](http://wiki.openbravo.com/wiki/Modularity_Concepts){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.