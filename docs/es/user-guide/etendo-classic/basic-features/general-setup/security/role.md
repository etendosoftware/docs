---
title: Rol
tags:
    - Rol
    - Administrador
    - Permisos
---
# Rol

:material-menu: `Aplicación` > `Configuración General` > `Seguridad` > `Rol`

## Visión general

El objetivo de un rol es agrupar usuario/s en función de a qué partes de Etendo tienen permitido acceder y, por lo tanto, en cuáles pueden trabajar.

!!! info
    Etendo incluye un usuario **superusuario** llamado **admin** (contraseña **admin**) que puede utilizarse para iniciar sesión por primera vez.

El usuario admin tiene varios roles asignados:

- el **Rol de Administrador del Sistema** (este se le asigna por defecto)
    - este rol permite a los usuarios admin tener permisos de administración sobre todas las Entidades existentes.
- los datos de demostración del **Rol de Administrador del Grupo Internacional F&B** (este también se le asigna por defecto)
    - este rol permite a los usuarios admin tener permisos de administración de la Entidad de **datos de demostración de F&B**.
- y además:
    - cada vez que se crea una nueva **Entidad** ejecutando el proceso [Initial Client Setup process](../../../../../developer-guide/etendo-classic/how-to-guides/how-to-run-an-initial-client-setup-process.md), Etendo crea automáticamente para esa Entidad un usuario **Administrador de la Entidad** vinculado a un **rol de Administrador de la Entidad**:
      - el rol de administrador de la entidad permite al usuario Administrador de la Entidad tener permisos de acceso de administración a esa Entidad y a todas las organización/es de esa entidad una vez iniciada la sesión.
      - el rol de administrador de la entidad recién creado también se asigna al usuario admin por defecto, por lo tanto será posible que el usuario admin acceda a la Entidad recién creada.

Por último, cada vez que se crea una nueva Organización ejecutando el proceso de Configuración Inicial de la Organización, se crean un nuevo usuario y un nuevo rol y se vinculan entre sí; en este caso, el nuevo rol de usuario solo permitirá al usuario acceder a esa Organización una vez iniciada la sesión.

Dicho esto, Etendo permite la creación de tantos roles nuevos como sea necesario para asignarlos posteriormente a los usuarios existentes y/o nuevos.

!!! info
    Los roles agrupan usuario/s en función de las tareas que realizan y, por lo tanto, de las partes de Etendo a las que deberían tener acceso, como ventanas, procesos, formularios, widgets y vistas.
## Herencia de permisos

Es posible configurar los roles para que obtengan su acceso a los diferentes elementos de Etendo de forma automática, heredándolos de otros roles padre. Esta configuración es posible gracias a una funcionalidad conocida como **Herencia de Roles**.

Teniendo un rol, es posible asignarle uno o más roles plantilla. De este modo, todos los elementos a los que estos roles plantilla tengan acceso estarán disponibles automáticamente también para ese rol.

Además, cualquier cambio realizado en un permiso de un rol plantilla se propagará automáticamente a todos los roles que hereden de él.

!!! note
    Solo es posible heredar permisos de roles plantilla, que además sean roles manuales.

Al heredar de varios roles, el orden de aplicación de los permisos viene determinado por la **Secuencia** de cada herencia. Esto significa que, si un permiso concreto se hereda desde varias herencias, el permiso se tomará de la herencia con mayor **Secuencia**.

Este proceso facilita la gestión de roles, especialmente cuando el número de roles definidos para una **Entidad** es elevado. Así, es posible definir roles plantilla para dar acceso a un conjunto concreto de elementos y, a continuación, crear múltiples combinaciones de roles funcionales para proporcionar accesos personalizados a los distintos usuarios. Esto se ilustra en la imagen siguiente.

![](../../../../../assets/drive/vyHTH7_aVNAVElZ2_BGWT5QcVh9MD3w_DCfz20k4Bu6mxa_QCvrKo2ufgIMmvqericF1SZnMm4ONeysEKiw2kON-47niJ5HlcjaVqGiiqPkcNyg9k0FOmnZHHfbqpioJ9At6rbTI.png)

La lista actual de elementos heredables incluye los siguientes: organizaciones, ventanas, solapas, campos, procesos, formularios, widgets, vistas, definiciones de proceso, preferencias y destinatarios de alertas.

Para el caso de preferencias y destinatarios de alertas, existen algunas restricciones para hacerlos heredables:

- Una preferencia es heredable si tiene establecido un rol plantilla en el campo **Visible At Role**.
- No es posible crear más de una preferencia con exactamente los mismos ajustes de visibilidad para un rol plantilla.
- Un destinatario de alerta es heredable si tiene el campo **User** vacío.
- No es posible crear más de un destinatario de alerta heredable con la misma regla de alerta para un rol plantilla.

!!! note
    Este mecanismo tiene en cuenta los permisos otorgados manualmente a los roles. Este tipo de acceso no heredado no se ve afectado (no se modifica) en ningún caso por el proceso de herencia.

También es posible forzar el recálculo de los permisos de un rol utilizando el proceso **Recalculate Permissions**. Sin embargo, siguiendo los flujos habituales de configuración de un **Rol**, todas las herencias se calculan automáticamente, por lo que este proceso no es necesario. Por este motivo, permanece oculto.

Tal y como se ha mencionado anteriormente, los cambios (crear, editar o eliminar) realizados en un permiso que pertenece a un rol plantilla se propagarán automáticamente a todos los roles que estén heredando de él en ese momento. Por este motivo, se muestra un mensaje de advertencia en la interfaz de usuario para informar a los usuarios sobre las implicaciones de este tipo de acción.

Este mensaje de advertencia es similar al que se muestra a continuación. Aparece al crear o editar un registro que pertenece a un rol plantilla, en una solapa de una entidad heredable.

![](../../../../../assets/drive/ibtK-OMAXBsv2UVQXFaPN7YvQMlh2rgo41Vt21hwrkhk0Grj3gy0Y_7tYhGZU4JZaX7i75-eo6xHmT7P7bHhUWyy2xIpcK5VB8rC7PqSxERaqBP7HXaLXKSeiyNf_1Sj_ZXhxDzb.png)
## Ventana Rol

:material-menu: `Aplicación` > `Configuración General` > `Seguridad` > `Rol`

La ventana Rol permite al usuario revisar, crear, configurar y mantener los roles que se utilizarán en una entidad determinada.

![](../../../../../assets/drive/8MOJrcJaif8MbvpR7NwOIA6JjqOIlmOf3df8nsTRJa7Zq02aanCB7SGImtBiEGqou4crWjRy_nGJNhUVj3rHpcNyYOVw8H-F_X4veFkEtGw_6KCGoJxom1R_MkOlm0pJhIbEYzMB.png)

Tal y como ya se ha descrito, existen roles creados automáticamente por Etendo que pueden revisarse en esta ventana.

Además, esta ventana permite al usuario crear nuevos roles para una entidad determinada. La creación de roles puede realizarse correctamente utilizando un usuario y rol de Administrador de la Entidad.

Los campos a cumplimentar son:

- el **Nombre** y una breve **Descripción** del rol
- el **Nivel de usuario**, que es un paso adicional del Nivel de Acceso a Datos que se define a nivel de Rol.
    - El nivel de usuario permite al usuario limitar los registros a los que se podrá acceder en entidades como ventanas, procesos o formularios para un rol; o incluso limitar el acceso a una entidad determinada para un rol:
      - Cada tabla en Etendo tiene definido un Nivel de Acceso a Datos. Las opciones disponibles son:
        - Sistema: este nivel permite al usuario ver registros de la Entidad Sistema y registros de la organización (\*), por ejemplo registros del diccionario de la aplicación.
        - Sistema/Entidad: este nivel permite al usuario ver cualquier registro de Entidad y registros de la organización (\*), por ejemplo registros relacionados con datos maestros como Países.
        - Entidad/Organización: este nivel permite al usuario ver cualquier registro de Entidad excepto los de la Entidad Sistema y cualquier Organización incluyendo la organización (\*), por ejemplo registros relacionados con datos maestros como Productos.
        - Organización: este nivel permite al usuario ver cualquier registro de Entidad excepto los de la Entidad Sistema y cualquier registro de Organización excepto los registros de la organización (\*), por ejemplo registros de datos transaccionales como Pedidos de compra.
    - Las opciones disponibles de Nivel de usuario son:
      - **Sistema**: si una tabla está definida con nivel de acceso a datos Sistema, un rol de usuario que tenga asignado este nivel de usuario podrá ver los registros de cualquier Entidad, incluyendo los registros de la Entidad Sistema, en una entidad como una ventana o formulario determinado.
      - **Entidad**: si una tabla está definida con nivel de acceso a datos Sistema/Entidad, un rol de usuario que tenga asignado este nivel de usuario podrá ver los registros pertenecientes a cualquier Entidad excepto la Entidad Sistema, en una entidad como una ventana o formulario determinado.
        - Por otro lado, si una tabla está definida con nivel de acceso a datos Sistema, un rol de usuario que tenga asignado este nivel de usuario no podrá ver ningún registro, ya que todos pertenecerán a la Entidad Sistema.
      - **Entidad + Organización**: si una tabla está definida con nivel de acceso a datos Entidad/Organización, un rol de usuario que tenga asignado este nivel de usuario podrá ver los registros pertenecientes a cualquier Entidad excepto la Entidad Sistema y a cualquier Organización incluyendo la organización (\*), en una entidad como una ventana o formulario determinado.
      - **Organización**: si una tabla está definida con nivel de acceso a datos Entidad/Organización, un rol de usuario que tenga asignado este nivel de usuario solo podrá ver los registros pertenecientes a una organización determinada excepto la organización (\*), en una entidad como una ventana o formulario determinado.
    - Adicionalmente, dependiendo del nivel de usuario del rol, puede que no sea visible ningún dato en función del nivel de acceso de la tabla. Esta restricción puede omitirse configurando la preferencia Bypass Access Level Entity Check a Y; los casos en los que la entidad no es accesible son:
      - Si el nivel de acceso es Sistema y el nivel de usuario no es Sistema
      - Si el nivel de acceso es Organización y el nivel de usuario no es Organización o Entidad+Organización
      - Si el nivel de acceso es Entidad/Organización y el nivel de usuario no es Entidad, Organización o Entidad/Organización
      - Si el nivel de acceso es Sistema/Entidad y el nivel de usuario no es Sistema o Entidad/Organización
- Marcado **Manual**. El rol obtiene automáticamente todos los privilegios estándar de usuario más los de administrador, incluso cuando se añaden nuevos elementos como ventanas, procesos, formularios, clases de widget u organizaciones, a menos que se habilite el marcado Manual.
    - Si el marcado manual está habilitado, será posible asignar manualmente el acceso a ventanas, procesos, etc. seleccionándolos manualmente en la pestaña correspondiente o utilizando el botón de proceso **Insertar permisos**.
    - El botón de proceso Insertar permisos permite al usuario seleccionar:
      - el **Módulo** o área de aplicación para la que se requiere acceso, módulos como Financial Management o Production Management, entre otros.
      - y las **entidades** del módulo seleccionado para las que se requiere acceso, entidades como ventanas, procesos o formularios, entre otros.
    - Si el proceso Insertar permisos se ejecuta para un rol marcado como **Plantilla**, los accesos concedidos se propagarán automáticamente a los roles que hereden de él.
- El marcado **Plantilla** se muestra para roles que tienen una asignación de acceso manual (el indicador Manual es Sí). Los roles marcados como plantilla son aquellos que pueden ser utilizados por otros roles para recuperar sus permisos automáticamente, utilizando el mecanismo de Herencia de Roles.
    - Por este motivo, solo los roles plantilla pueden seleccionarse en el campo **Hereda De** de la pestaña Herencia de Roles.
- **Restringir acceso al backend**: si está marcado, este rol no tendrá acceso al backend (ERP). Sin embargo, tendrá acceso a otras aplicaciones (como WebPOS).
- **Para usuarios del portal**: si está marcado, este rol tendrá una interfaz simplificada (portal), donde solo tendrá disponibles los widgets del espacio de trabajo. La interfaz del portal cambia el aspecto del espacio de trabajo. El menú superior de la página y el menú lateral izquierdo quedan ocultos. Normalmente, un rol para usuarios del portal da acceso a los usuarios únicamente a su propia información mediante widgets.
- **Administrador del portal**: si está marcado, el rol de portal tendrá privilegios de Administrador del portal.
- **Web Services habilitados**: si está marcado, los servicios web podrán obtener datos para usuarios con este rol. Aplica tanto a servicios web JSON REST como XML REST.
- El marcado **Avanzado** se muestra para roles que tienen una asignación de acceso automática (el indicador Manual es No) y concede automáticamente acceso para dichos roles a todas las funcionalidades avanzadas.
    - Los roles creados manualmente (el indicador Manual es Sí) tienen su propia configuración, que puede incluir funcionalidades avanzadas o no, por lo que este indicador no se muestra para ellos.
- La casilla **Administrador de la Entidad** permite que un rol administre el espacio de trabajo de otros usuarios, así como los Formularios Personalizados:
    - En otras palabras, un rol de administrador de la entidad puede asignar widgets al espacio de trabajo de cualquier usuario de la entidad, así como formularios personalizados.

### Permiso a organizaciones

La pestaña Permiso a organizaciones permite al usuario definir la(s) organización(es) a las que un rol determinado tendrá derechos de acceso.

Como ya se ha mencionado, cada registro en Etendo pertenece a una organización; por lo tanto, la única forma de que un rol de usuario edite un registro que pertenece a una organización es proporcionar a ese rol de usuario acceso a dicha organización.

![](../../../../../assets/drive/vE-K35fSEj9-BIvgbMGezZvFFgFx4-bfY-LNbMosiyjun4B_-bSKiWnHr-K7bpJSnYwrSypNacZYFmcO9x46g3yGgrHxrywB-z2Agfywx-qVesqxPN9ruiBg45aTxqkyn15BsOkb.png)

- La casilla **Administrador de la Organización** permite que un rol administre el espacio de trabajo de otros usuarios, así como los Formularios Personalizados:
    - En otras palabras, un administrador de la organización puede asignar widgets al espacio de trabajo de cualquier usuario de la organización, así como formularios personalizados.

### Asignación de usuarios

La pestaña Asignación de usuarios permite al usuario añadir usuarios a un rol determinado.

![](../../../../../assets/drive/iBeXu8RdIKr-srDU5Q-1Y5e5wYtbvNbXqD8KtMx8MK2gHEXc9BJUcYsA19OgHzCNv7chh30Ws8bVjbtjFkllwl5w8kZZ2ZoAbiXLOeFJDzwEisQu04z8dGAj3CmIy0OOxneMJtz6.png)

La casilla **Administrador de Rol** permite al usuario administrar el rol indicado para:

- **Widgets**: podrán establecer widgets por defecto que serán vistos por otros usuarios con el mismo rol.
- **Vistas guardadas**: este usuario podrá compartir con otros usuarios con el mismo rol las vistas que haya guardado.

!!! info
    Dado que el indicador **Administrador de Rol** permite al usuario modificar el comportamiento de otros usuarios con el mismo rol, solo debería concederse a usuarios de confianza.

### Permiso a ventanas

Esta pestaña lista y/o permite al usuario añadir las ventanas a las que un rol tendrá acceso.

Como ya se ha mencionado, cada vez que se crea y guarda un nuevo rol sin seleccionar la casilla **Manual**, Etendo rellena automáticamente todas las ventanas en la pestaña Permiso a ventanas.

Lo anterior significa que el rol recién creado tendrá acceso a todas las ventanas de Etendo.

![](../../../../../assets/drive/vt5fH1QoVLs_KcIpoESYAQqhSe01e6oHVVFbF-UQy6fwJnDu8B4qOgQDCI34dQheclrgChwDy-IuurthKMqxAljaRU-jVczgUCGnXrXDTv2vERvhxlgGjRy7SA6ivWpqpYMBhcmQ.png)

Dicho esto, si se selecciona la casilla **Manual**, será necesario añadir manualmente un subconjunto de ventanas que serán accesibles para un rol determinado, o será necesario añadirlas automáticamente utilizando el proceso de acción **Insertar permisos**. Este proceso permitirá el acceso a ventanas para un módulo o área de Etendo determinada, como Projects, Finance o Sales.

La casilla **Lectura y escritura** define si los datos accesibles en una ventana pueden ser editados por el rol o no.

#### Acceso a Solapas

Define si una solapa es editable o de solo lectura para un rol concreto.

En una ventana accesible por un rol, es posible definir para cada una de sus solapas si son editables o no mediante el marcado **Pestaña Editable**.

Si la ventana es editable (está marcada **Lectura y escritura**), por defecto todas sus solapas serán editables. Pero es posible definir que algunas no sean editables para este rol añadiéndolas en esta pestaña y estableciendo a falso el marcado **Pestaña Editable**. Tenga en cuenta que esto solo es cierto si la tabla detrás de la solapa es editable para el rol.

Del mismo modo, teniendo una ventana no editable, es posible definir algunas de sus solapas como editables marcando **Pestaña Editable**.

#### Acceso a Campos

Define si un campo es editable o de solo lectura para un rol concreto.

La pestaña **Campo** funciona de forma muy similar a la pestaña Acceso a Solapas, permitiendo al usuario definir acceso de escritura hasta un nivel de granularidad de campo.

Así, si una solapa es editable para un rol, un conjunto concreto de campos puede hacerse de solo lectura para ese rol, añadiendo una nueva fila en esta pestaña para cada campo y estableciendo a falso **Lectura y escritura** en cada uno de ellos. O a la inversa: en una solapa no editable, los campos pueden ser editables si se añaden y su propiedad **Lectura y escritura** está marcada.

Al editar una solapa con algunos campos definidos como no editables de esta forma, el backend comprueba las modificaciones en esa solapa para evitar que esto ocurra. Tenga en cuenta que esto también afecta al campo en caso de que se haya modificado, por ejemplo, mediante un callout o una expresión por defecto. Esto se controla mediante la propiedad **Comprobar al Guardar**; al desmarcarla, esta comprobación no se realizará, permitiendo así que el campo sea modificado por un callout.

### Permiso a procesos

Esta pestaña lista y/o permite al usuario añadir los informes y procesos a los que un rol tendrá acceso.

Como ya se ha mencionado, cada vez que se crea y guarda un nuevo rol sin seleccionar la casilla **Manual**, Etendo rellena automáticamente todos los informes y procesos en la pestaña Permiso a procesos.

Lo anterior significa que el rol recién creado tendrá acceso a todos los informes y procesos de Etendo.

![](../../../../../assets/drive/jeSO8cKGRMnO5jlOseLchbPh4OE2fDeLeAAS0VSOIngREivxtfTmTPmNLaDwnn7ujstw7z6Pgqp0oZLZAHxwT1XwtyGmlZdj-vuNEBXnBq1dFNo5UvBFIC_CIAJc6Tn2gweJJPKq.png)

Dicho esto, si se selecciona la casilla **Manual**, será necesario añadir manualmente un subconjunto de informes y procesos que serán accesibles para un rol determinado, o será necesario añadirlos automáticamente utilizando el proceso de acción **Insertar permisos**. Este proceso permitirá el acceso a informes o procesos para un módulo o área de Etendo determinada, como Projects, Finance o Sales.

La casilla **Lectura y escritura** define si los datos accesibles en un informe o proceso pueden ser editados por el rol o no.

Por defecto, el acceso a procesos en una ventana estándar proporcionado desde un botón se hereda del permiso a la ventana. Por lo tanto, si el rol tiene acceso a la ventana, será posible ejecutar todos los procesos definidos en esa ventana, independientemente de si existen entradas explícitas para ellos en la pestaña **Permiso a procesos**. Este comportamiento por defecto puede cambiarse de dos formas diferentes:

- Para revocar este acceso heredado y decidir manualmente caso por caso cuáles son los procesos accesibles, es posible definir una preferencia de **Proceso seguro** (a nivel de sistema o para esa ventana específica) con valor Y.
- Si el desarrollador definió el proceso como Requires Explicit Access Permission. En este caso, los permisos nunca se heredarán para ese proceso.

### Permiso a formularios

Esta pestaña lista y/o permite añadir los formularios a los que un rol tendrá acceso.

Como ya se ha mencionado, cada vez que se crea y guarda un nuevo rol sin seleccionar la casilla Manual, Etendo rellena automáticamente todos los formularios en la pestaña Permiso a formularios.

Lo anterior significa que el rol recién creado tendrá acceso a todos los formularios de Etendo.

![](../../../../../assets/drive/h71SGbrOND-3ZRiDfheu69SJe6ZUIfQdyVOKmL_RaRtqSCRmQ84JoLrhPok37CDsfNRt0BbqoKwNzchby0i1ffWbKxN1JZZy2wBjC_akKrtaYwtR9FNCgEJaYGEFtse9xsx2kG4_.png)

Dicho esto, si se selecciona la casilla Manual, será necesario añadir manualmente un subconjunto de formularios que serán accesibles para un rol determinado, o será necesario añadirlos automáticamente utilizando el proceso de acción Insertar permisos. Este proceso permitirá el acceso a formularios para un módulo o área de Etendo determinada, como Projects, Finance o Sales.

La casilla Lectura y escritura define si los datos accesibles en un formulario pueden ser editados por el rol o no.

### Permiso de la Clase de Widget

Esta pestaña lista y/o permite añadir las clases de widget a las que un rol tendrá acceso.

![](../../../../../assets/drive/UJdYTlYdE7iCbPZXvMLbM-FtRsvCjm1H0ogLpoAgaHlt18r4-hS0gB0jXOCtea26kAn3l9phNMuoqFO5uvrKDqHnd_99mcY6FqmqGhHKwcwIiozXLsji0LHlgp6KWLzKuvVYq6S_.png)

Los widgets son elementos de la interfaz de usuario que pueden colocarse en la pestaña de espacio de trabajo de los usuarios o formar parte de una ventana generada.

### Implementacion de Vista

La pestaña Implementacion de Vista permite al usuario seleccionar vistas personalizadas.

Una implementación de vista es una implementación completamente personalizada de una vista principal.

El acceso a una vista personalizada puede controlarse mediante esta pestaña de acceso del rol.

![](../../../../../assets/drive/5OCz4Fl8K2i8uYaKdMnh3lg-DT_9IQBDjimbD37HCtwzOs74M-OTqbTorDwTzxEQaWJBKZRxkhNJc_jF-4kjLOllZSlfZe_9kcngt9KUQB0X3KVYFyeOblGXuzo0LCGDI-C_QlvI.png)

Para información adicional sobre vistas, visite How to implement a new main view.

### Definición del Proceso

Concede acceso a Definición del Proceso. Por defecto, el acceso a definiciones de proceso en una ventana (proporcionado desde un botón) se hereda del permiso a la ventana. Para cancelar este acceso heredado y decidir manualmente caso por caso cuáles son los procesos accesibles, es necesario definir una preferencia de Proceso seguro (a nivel de sistema o para esa ventana específica) con valor Y.

![](../../../../../assets/drive/IFXcBPxniL5TViWp3QIr2LiircvQoutdDPZ4K-zMHibWBRtwsI2fNh8dTXWG5H8_GROHo17oFdKjb-Kuj696jezS3flqH9VJL8yAlFYFV0__mtN4aDKFHrIuosLt28EfSLpfT5iR.png)

El acceso cuando el proceso se invoca desde un botón de ventana estándar se hereda de la misma manera que para Procesos.

### Herencia de Roles

Permite definir una herencia para un rol. Una herencia es una relación entre dos roles: si el rol A hereda del rol B, significa que todos los permisos que el rol B tiene para diferentes elementos de la aplicación como organizaciones, ventanas, informes, procesos, widgets, etc. serán heredados automáticamente por el rol A, permitiéndole acceder a esos elementos de la misma manera que B. También es posible definir una jerarquía de herencia; es decir, un rol puede heredar de diferentes roles, y la prioridad (orden) para heredar los permisos se define mediante la **Secuencia**.

Esto significa que si dos herencias tienen accesos en común, los accesos de la herencia con un número de secuencia menor serán sobrescritos por los accesos de la herencia con un número de secuencia mayor.

Dentro de esta pestaña es donde se configura la Herencia de Roles de un rol en particular.

![](../../../../../assets/drive/KI9-ImqA0ErnTQS_fepHzt63s_3ExEUeRwCXREoaE2NKc1e13FAmtPhHnCQC4CPLwWzbUvWZbertcWG81CDPmYaZzLhN8IrliDLcJ9V48S3VxosZwI2vzSlPc0suV5WKwYcPi8JF.png)

Los campos a cumplimentar son:

- **Hereda De**: en este campo debe seleccionarse el rol cuyos permisos se heredarán. Define el rol que se utilizará para recuperar automáticamente el acceso a sus permisos.
- **Secuencia**: define el orden en la aplicación de la herencia de roles, cuando existen múltiples registros en la pestaña. Cuanto menor sea este valor, antes se recuperarán los permisos del rol plantilla relacionado. Esto significa que si el mismo permiso es accedido por dos roles plantilla seleccionados para heredar de ellos, el permiso relacionado con la herencia con mayor número de secuencia sobrescribirá al otro.

---

Este trabajo es una obra derivada de [Configuración General](https://wiki.openbravo.com/wiki/General_Setup){target="_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="_blank"} por [Etendo](https://etendo.software){target="_blank"}.