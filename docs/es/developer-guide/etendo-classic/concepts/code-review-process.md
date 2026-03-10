---
title: Proceso de revisión de código
tags:
  - Revisión de código
  - Proceso
  - Propiedades
  - Diccionario de aplicación

status: beta
---

# Proceso de revisión de código

!!! example  "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.

##  Visión general

Este documento ofrece una descripción del proceso de revisión de código de Etendo y de la lista de verificación de revisión de código.

La opinión general es que la revisión de código es muy útil para encontrar y prevenir errores y para transferir conocimiento entre los miembros del equipo de desarrollo. Por otro lado, las revisiones de código tradicionales (tipo Fagan) consumen mucho tiempo y requieren muchos recursos. Además, las revisiones estándar tipo Fagan encajan peor con métodos de desarrollo más ágiles y con los entornos de desarrollo actuales con compilación instantánea y herramientas de formateo de código. El resultado es que, en la práctica, es difícil organizar e implementar procesos de revisión de código en el entorno dinámico y con presión de plazos de un proyecto de desarrollo.

El proceso de revisión de código de Etendo intenta combinar las ventajas de la revisión de código con un proceso ligero y fácil de organizar y controlar. El proceso está muy centrado en el propio código y utiliza las funcionalidades de los entornos de desarrollo y las herramientas de comprobación de código. El uso de herramientas de comprobación de código implica que la revisión de código puede centrarse en la calidad y la corrección del código en lugar de en la conformidad con estándares.

Antes de entrar en más detalle, conviene definir los objetivos que queremos alcanzar con la revisión de código. Hay dos objetivos principales:

* Mejorar la calidad del código:
    * Garantizar la corrección (funcional)
    * Minimizar el número de errores
    * Prevenir problemas de derechos de propiedad intelectual
    * Garantizar que el código cumple los estándares de codificación acordados

* Permitir que los desarrolladores compartan conocimiento, aprendan unos de otros y mejoren la comprensión del código de los demás.

El proceso de revisión de código de Etendo debería estar respaldado por un conjunto de herramientas. En lugar de tomar una decisión previa sobre una herramienta, se describe el proceso previsto. El siguiente paso es determinar si puede elegirse una herramienta existente o si puede crearse una herramienta de revisión de código personalizando herramientas de desarrollo actuales (github, Sonar, IntelliJ).

Pero antes de describir el proceso de revisión de código, destaquemos primero el papel del desarrollador en el proceso de desarrollo de software. Porque el código de alta calidad empieza y termina con el enfoque personal y la motivación de cada desarrollador.

##  Objetivo de la revisión de código

El objetivo de la revisión de código es intercambiar conocimiento, aumentar capacidades y apoyar a los desarrolladores para que tomen decisiones automáticas sobre estructuras estándar. Esto permite al desarrollador dedicar tiempo y esfuerzo a las cosas que son importantes: crear código que funcione, código que sea legible, elegante, fácil de leer, fácil de adaptar, eficiente y comprensible.

##  Proceso de revisión de código de Etendo: revisión personal, revisión por pares y revisión de equipo

El proceso de revisión de código de Etendo consta de tres tipos de revisiones:

1. Personal,
2. Por pares y
3. De equipo.

###  Revisión personal

El desarrollador debería seguir automáticamente las convenciones de codificación y otras buenas prácticas de codificación. Para validarlo, cada desarrollador debería revisar activamente su propio trabajo. El sistema de desarrollo debería ayudar al desarrollador a realizar esta tarea.

Se propone el siguiente proceso:

* Cada desarrollador recibe automáticamente un correo electrónico con los commits del día anterior.
* El correo electrónico contiene la lista completa de archivos confirmados el día anterior. Solo los archivos que se hayan enviado para ser revisados deberían formar parte de este correo.
* Cada archivo tiene un hipervínculo que abre una página web que muestra el diff del commit. La página web también muestra puntos de atención para que el desarrollador los revise:
    * ¿Es correcto el cambio?
    * ¿Sigue el cambio las convenciones de codificación?
* El desarrollador no necesita rellenar una lista de verificación; la revisión personal debería ser muy ligera, ya que se realiza con frecuencia (diariamente).
* El sistema de revisión de código registra qué archivos se han enviado a cada desarrollador y registra qué archivos ha abierto el desarrollador para revisarlos.

La revisión personal no debería realizarse el mismo día en que se escribió el código. Un mayor tiempo entre el commit y la revisión personal dará como resultado una mirada más fresca sobre los cambios realizados por la propia persona.

###  Revisión por pares

La revisión por pares es la revisión más importante, ya que opera sobre dos objetivos: prevención de incidencias y transferencia de conocimiento (del revisor al revisado).

Una pregunta importante es quién es el par, quién revisará el código. En el proceso de revisión de código de Etendo, el revisor par es el team lead del equipo scrum.

La ventaja del team lead como par es que entiende la funcionalidad en la que está trabajando el equipo. Por lo tanto, puede juzgar si los cambios son correctos con respecto a la funcionalidad en la que trabaja el equipo. Además, el team lead tiene contacto directo con los miembros del equipo. Asimismo, la revisión de código forma más parte de las actividades estándar del equipo y puede planificarse. Como el team lead es un desarrollador con experiencia, la revisión de código da lugar a transferencia de conocimiento del team lead a los miembros del equipo con menos experiencia.

El enfoque del team lead como par tiene como desventaja que el team lead podría sobrecargarse con actividades de revisión. Otra desventaja de un team lead como par es que podría sentir menos responsabilidad sobre los archivos fuente globales y posiblemente no pueda determinar si los cambios de código interfieren con otras partes (sin cambios) del código.

Los commits de los propios team leads también deberían revisarse. Por lo tanto, a cada team lead también se le asigna un revisor personal.

El proceso de revisión por pares consta de los siguientes pasos:

* Un desarrollador hace commit de uno o más archivos en subversion.
* Se desencadena una revisión (a través del commit) y se envía un correo electrónico al revisor. El correo contiene la siguiente información:
    * La descripción del mensaje del commit y el nombre y la dirección de correo electrónico de quien hace el commit
    * La lista de archivos modificados y la cantidad de líneas modificadas por archivo
    * Si el commit era para una o más incidencias de Mantis, entonces los hipervínculos a dichas incidencias también están presentes en el correo
    * Un hipervínculo para iniciar el proceso de revisión
* El revisor hace clic en este hipervínculo y se le dirige a una página web. La página web muestra:
    * El mensaje del commit, el nombre de quien hace el commit y su dirección de correo electrónico.
    * Si el commit es una corrección de error: un hipervínculo al/los error(es) de Mantis de la solución
    * La lista de archivos modificados con, para cada archivo, un hipervínculo al diff y a la página de lista de verificación (véase más abajo).
* El revisor hace clic, para cada archivo, en la página de diff/lista de verificación. Se le dirige a una página siguiente que muestra la información del commit en el encabezado y la siguiente información:
    * El diff
    * Lista de commits realizados sobre el archivo desde el commit que desencadena esta revisión, con hipervínculos a los diffs de esos otros commits.
    * Hipervínculo a la versión completa actual del archivo
    * La lista de verificación aplicable a ese archivo; el revisor debe marcar cada punto de la lista de verificación
    * Un botón de rechazo: si el revisor hace clic en este botón, entonces quien hizo el commit necesita rehacer el archivo. El revisor debe introducir una observación al rechazar un archivo.
    * Un botón de aprobación
* El revisor rellena la lista de verificación o introduce un comentario y hace clic en rechazar. Se notifica a quien hizo el commit que debe cambiar/actualizar el archivo. Si el archivo se aprueba, entonces no se envían correos.
* Cuando el último archivo ha sido aceptado o rechazado, la tarea de revisión finaliza.

!!!note
    Todas las revisiones por pares deberían haberse realizado antes de que una rama pueda fusionarse con trunk. ?

###  Revisión de equipo

Cada equipo scrum debería dedicar al menos 45 minutos a la semana ? a una revisión de equipo. En la revisión de equipo, se discute uno (o parte de un) archivo con todo el equipo en conjunto. El propósito principal de la revisión de equipo es compartir conocimiento sobre el código y las prácticas de codificación. El archivo a revisar es propuesto por el team lead.
El team lead informa al resto del equipo qué archivo se discutirá y cada miembro del equipo dedica 15 minutos a realizar una revisión personal del archivo.

En la reunión de revisión de equipo, el autor del archivo presenta el código y realiza un recorrido. La reunión de revisión debería ser un intercambio de ideas y una discusión de estrategias de implementación. El objetivo es compartir ideas y conocimiento y no tanto encontrar errores o no conformidades con los estándares.

##  Qué revisar

Se revisan los siguientes archivos:

* Archivos Java.
* Archivos de plantillas de propiedades.
* Archivos de propiedades y archivos XML en la carpeta `src`.
* El contenido de las tablas del Diccionario de aplicación (el AD_TABLE.xml, etc.).
* El contenido de los archivos XML de funciones, triggers y vistas.

Solo se revisan los cambios confirmados (committed). Esto significa que todo el mundo es libre de hacer commit sin revisión previa. Esto es como es ahora. El commit es el desencadenante de la revisión.

Sin embargo, no todos los commits necesitan revisarse. Se aplican las siguientes reglas. Se revisa cada commit, excepto:

* Un commit con solo un número limitado de cambios por archivo no se revisa. Por ejemplo, menos de 5 caracteres (para corregir un error tipográfico)
* Un commit con solo cambios en comentarios no se revisa.
* Un commit con un comentario específico que evita revisiones: *No se requiere revisión*. Esto hace posible que quien hace el commit indique que un determinado commit realmente no necesita una revisión. Por cada committer, el número de commits con esta observación se comprueba en las estadísticas (véase más abajo).

Diferentes tipos de archivos requerirán diferentes tipos de listas de verificación de revisión. La propuesta es tener diferentes listas de verificación para diferentes archivos:

* Una lista de verificación Java corta para cambios pequeños (menos de cinco líneas de código).
* Una lista de verificación Java completa para el resto de cambios Java.
* Una lista de verificación para archivos properties/properties.templates.
* Una lista de verificación para tablas del diccionario de aplicación.
* Una lista de verificación para archivos XML de funciones, triggers y vistas.

Las listas de verificación se tratan a continuación con más detalle.

##  Estadísticas de revisión

Para fines de gestión, el sistema de revisión de código debería registrar y mostrar la siguiente información:

* Total de revisiones cerradas, abiertas y rechazadas.
* Por revisor: revisiones cerradas, abiertas y rechazadas.
* Por revisor: número de archivos confirmados, número de archivos revisados personalmente.
* Por committer: revisiones cerradas, abiertas y rechazadas, número de commits establecidos explícitamente como "No se requiere revisión".
* Los 100 principales archivos que no se han revisado, los 100 archivos más revisados.

##  Herramientas de revisión de código

Hay diferentes herramientas disponibles que pueden utilizarse y adaptarse al flujo descrito anteriormente. Si se decide utilizar una herramienta externa, entonces debe planificarse una prueba de concepto para probar una.

Otra opción puede ser implementar y soportar el flujo anterior con una aplicación web desarrollada a medida integrada con svn y Mantis. Mantis puede utilizarse como registro de tareas de revisión y resultados. Por ejemplo, un error de Mantis puede utilizarse para iniciar una tarea de revisión. Una revisión rechazada puede crear una incidencia de Mantis asignada a quien hizo el commit. El resultado de una revisión puede adjuntarse a la incidencia de Mantis.

La ventaja de desarrollar nuestro propio conjunto de herramientas es que evita otra-herramienta-más en el entorno de desarrollo y gestión de sistemas.

##  Revisiones automatizadas e identificación de errores

El proceso de revisión manual se apoya en las siguientes herramientas que realizan revisión de código automática:

* Configuración de compiladores y advertencias de IntelliJ: deberían utilizarse las configuraciones estándar de Etendo
* FindBug
* CheckStyle
* PMD

##  Lista de verificación

Hay diferentes listas de verificación para diferentes situaciones. Cada lista de verificación es corta para ser efectiva, remitiendo a documentos externos para más información.

###  Lista de verificación corta (Java)

* ¿Entiende qué cambios se han realizado y por qué se han realizado?
* ¿Implementan los cambios correctamente la funcionalidad requerida?
* ¿Cumple el código las [convenciones de codificación](../concepts/java-coding-conventions.md)?

###  Lista de verificación completa (Java)

* ¿Entiende qué cambios se han realizado y por qué se han realizado?
* ¿Implementan los cambios correctamente la funcionalidad requerida?
* ¿Interfiere el cambio con otro código/funcionalidad?
* ¿Cumple el código las [convenciones de codificación](../concepts/java-coding-conventions.md)?
    * Compruebe estos temas: declaración de copyright, documentación, gestión de excepciones, constructos Java, cosas a evitar
* ¿Es el código legible y comprensible, es decir, se puede ojear?
* ¿Se ha formateado el código según el formato de codificación acordado?
* ¿Ha utilizado el desarrollador prácticas de codificación defensiva?
* ¿Muestra IntelliJ alguna advertencia en el código?
* Propiedad intelectual:
    * ¿Contiene el commit una nueva biblioteca externa? Si es así, ¿ha revisado el asesor legal la licencia?
    * ¿Contiene el commit código de terceros? Si es así, ¿ha firmado el contribuidor tercero un acuerdo de contribución y se ha depositado en el Departamento Financiero de Etendo?

###  Archivos de propiedades

* ¿Interfiere el cambio con otras partes del archivo de propiedades?
* ¿Están documentadas las nuevas propiedades, se ha comunicado el cambio a otros desarrolladores?

###  Lista de verificación del Diccionario de aplicación

* ¿Es correcta la denominación de tablas y columnas, en inglés?
* ¿Está configurado correctamente el javapackage de la tabla?
* ¿Se han elegido los tipos correctos? ¿Se han configurado las claves foráneas?


##  Tipos de pares

Las principales actividades de revisión se realizan como parte de la revisión por pares. Por lo tanto, una pregunta importante es quién es el par que revisará el código.

###  Propietario

El enfoque de par propietario significa que el código fuente de Etendo se divide en diferentes partes y cada parte se asigna a un propietario de ese código. El propietario de cada parte es responsable de revisar los cambios en el código realizados por otros desarrolladores.

El propietario debería ser alguien con experiencia y con ojo para la calidad del código. Debería tener plena comprensión de las convenciones de codificación. Además, el propietario debería entender la funcionalidad implementada por su parte del código. Debería sentirse responsable de su código.

El enfoque de par propietario tiene como ventaja que las revisiones las realiza una persona que conoce el código global (de su parte asignada). Puede detectar cuando los cambios de código entran en conflicto con el significado más amplio del código. Además, como el par propietario es un desarrollador con experiencia, puede ser más efectivo al compartir su conocimiento con desarrolladores menos experimentados cuyos cambios de código están siendo revisados.

La principal desventaja de un enfoque de par propietario es que el par propietario no participa en cada proyecto/equipo scrum que realiza cambios en su parte. Por lo tanto, puede ser más difícil entender/seguir la razón por la que se realizan cambios de código.

###  Team Lead

El team lead también puede actuar como el par. La ventaja del team lead como par es que entiende la funcionalidad en la que está trabajando el equipo. Por lo tanto, puede juzgar si los cambios son correctos con respecto a la funcionalidad en la que trabaja el equipo. Además, el team lead tiene contacto directo con los miembros del equipo.
Asimismo, la revisión de código forma más parte de las actividades estándar del equipo y puede planificarse. Como el team lead es un desarrollador con experiencia, la revisión de código da lugar a transferencia de conocimiento del team lead a los miembros del equipo con menos experiencia.

El enfoque del team lead como par tiene como desventaja que podría sobrecargarse con actividades de revisión. Otra desventaja de un team lead como par es que podría sentir menos responsabilidad sobre los archivos fuente globales y posiblemente no pueda determinar si los cambios de código interfieren con otras partes (sin cambios) del código.

###  Miembro del equipo

En este enfoque, el trabajo de un miembro de un equipo es revisado por otro miembro de ese equipo. La ventaja de este enfoque es que los miembros del equipo intercambian conocimiento y que los miembros del equipo crecen juntos en su nivel de experiencia y conocimiento. Hacer revisiones de código puede ayudar a desarrollar más rápidamente las habilidades de los desarrolladores. Otra ventaja es que el trabajo de revisión se reparte.

La desventaja es que también los desarrolladores sin experiencia harán revisiones, lo que probablemente dará lugar a revisiones menos efectivas.

---

Este trabajo es una obra derivada de [Proceso de revisión de código](http://wiki.openbravo.com/wiki/Code_Review_Process){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.