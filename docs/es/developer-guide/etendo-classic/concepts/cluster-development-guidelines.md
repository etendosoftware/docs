---
title: Directrices de desarrollo en clúster
tags:
    - Desarrollo en clúster
    - Directrices
    - Caché
    - Implementaciones

status: beta
---

#  Directrices de desarrollo en clúster

!!! example  "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.
  
##  Visión general

La siguiente sección describe los elementos básicos que deben tenerse en cuenta para garantizar que los desarrollos sean compatibles en un entorno en clúster.

Para el alcance de este documento, consideramos que un **entorno en clúster** es una aplicación de Etendo distribuida en múltiples JVM.

Los entornos en clúster están pensados para mejorar el rendimiento, permitiendo atender más procesos de forma concurrente, así como para ofrecer alta disponibilidad, permitiendo que el sistema continúe funcionando incluso si algunos de los nodos del clúster están caídos.

##  Cachés

Una **caché** es un objeto destinado a almacenar elementos que son costosos de crear y se utilizan con frecuencia; de este modo, se crean una sola vez y se reutilizan muchas veces, ahorrando su cálculo en usos posteriores.

La principal preocupación respecto a las cachés en entornos en clúster es que habrá tantas instancias de caché como nodos en el clúster. Esto puede llevar a la posibilidad de tener nodos con información desactualizada debido a que se cambia un valor en un nodo sin notificar al resto de nodos sobre el cambio.

Para entornos en clúster, debemos prestar atención a la implementación de una caché cuando su ciclo de vida es superior al de la petición y también si está manteniendo información de instancia.

En ese caso, es obligatorio disponer de un mecanismo que permita refrescar el contenido de la caché en cada nodo del clúster.

!!! example
    Si actualmente tenemos una clase que extiende `EntityPersistenceEventObserver` (`@ApplicationScoped`) que se encarga de actualizar algún tipo de caché cuando detecta un cambio en la JVM donde se está ejecutando, esta implementación por sí sola no es suficiente para un entorno en clúster, ya que el resto de nodos no serán notificados del cambio.

###  Cachés seguras

En resumen, no necesitamos tener un cuidado especial con las cachés en los siguientes escenarios:

* Si el ciclo de vida de la caché ocurre en el ámbito de la petición o inferior (por ejemplo, el ciclo de vida de la caché está dentro de un método).

    !!!note 
        Si la caché es `@SessionScoped`, puede utilizarse de forma segura siempre que Etendo use sesiones persistentes (sticky sessions). 

* Si la caché se utiliza internamente por un objeto (es un campo privado) cuyo ciclo de vida no va más allá de `@SessionScoped`.

* Si la caché mantiene información estática, entonces es seguro tener una instancia de la caché por nodo. Algunos ejemplos de información estática son: 
    * Información basada únicamente en el Diccionario de Aplicación.
    * Información basada en la configuración de la aplicación: p. ej., información tomada del archivo `Openbravo.properties`. 

###  Implementaciones de caché

Aunque una clase no esté diseñada para ser utilizada como caché, a efectos de esta discusión, cualquier clase que encaje en cualquiera de las siguientes categorías debe considerarse como caché y, por lo tanto, revisarse especialmente.

####  Clases `@ApplicationScoped`

`@ApplicationScoped` es una anotación CDI que permite definir una clase cuya instancia única por JVM está garantizada, por lo que, a todos los efectos, se comporta como clases Singleton.

Las clases `@ApplicationScoped` pueden considerarse cachés siempre que tengan estado; es decir, que tengan campos de instancia. Esos campos de instancia son, en la práctica, elementos en caché.

####  Clases Singleton

Una [clase singleton](https://en.wikipedia.org/wiki/Singleton_pattern){target="\_blank"} garantiza que exista una única instancia por JVM de esa clase.

Pueden considerarse como cachés con el mismo criterio que las clases `@ApplicationScoped`.

####  Campos estáticos

Cualquier campo estático puede considerarse una caché, ya que su ciclo de vida es de ámbito de aplicación; es decir, existe una única instancia de ese campo para toda la JVM.

Solo en los siguientes casos, un campo estático puede considerarse seguro en este sentido:

* Es inmutable: es `final` y todos los campos dentro de él también son inmutables. 
* Es privado y la clase que lo contiene garantiza una gestión adecuada del estado. 

##  Sincronización en la JVM

Los [bloques synchronized de Java](https://docs.oracle.com/javase/tutorial/essential/concurrency/sync.html){target="\_blank"} permiten definir fragmentos de código que se garantiza que no tendrán ejecuciones en paralelo. Pero esta sincronización ocurre a nivel de JVM, por lo que no podemos garantizar con un bloque synchronized que no haya ejecuciones en paralelo de este bloque entre diferentes nodos del clúster.

Por lo tanto, en un entorno en clúster, no deben utilizarse bloques synchronized para sincronizar utilidades destinadas a ejecutarse de forma sincronizada a nivel de sistema.

Si necesitamos sincronizar algún tipo de tarea a nivel de sistema, entonces debemos usar otro tipo de mecanismo de sincronización, por ejemplo, utilizando la capa de base de datos.

##  Archivos

También debemos tener cuidado al manejar archivos en un entorno en clúster. En general, debemos:

* Evitar escribir/leer archivos desde la ruta del código fuente: los nodos del clúster no deberían requerir acceso a directorios de código fuente. 
* Evitar escribir archivos en `WebContent`
* Unificar el uso de archivos temporales 

---

Este trabajo es una obra derivada de [Directrices de desarrollo en clúster](http://wiki.openbravo.com/wiki/Cluster_Development_Guidelines){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.