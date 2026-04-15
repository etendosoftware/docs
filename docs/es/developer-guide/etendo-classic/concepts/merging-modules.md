---
title: Fusión de módulos
tags:
    - Fusión
    - Módulos
    - Proceso
    - Conceptos

status: beta
---

# Fusión de módulos

!!! example  "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.

## Visión general

El objetivo de esta sección es explicar qué son las fusiones y cómo se pueden fusionar módulos.

## Qué es la fusión

Un módulo (**B**) puede fusionarse dentro de otro (**A**). Tras fusionar estos dos módulos, **B** deja de estar disponible porque queda incluido dentro de **A**.

En caso de que una instancia tenga una versión antigua de **A** e intente instalar la nueva versión de **B** o actualizar a esta. El proceso de instalación/actualización desinstalará **A**; después de esto, el único módulo instalado será **B** y no será posible instalar en esa instancia ninguna otra versión de **A**.


## Cuándo fusionar

La fusión de módulos debería realizarse solo en muy pocos casos; no debería convertirse en una práctica habitual.

Dos módulos son susceptibles de fusionarse en caso de que uno de ellos no tenga sentido sin el otro. Inicialmente podrían haberse concebido como módulos separados por algún motivo (funcionalidad diferente, pensados para usarse por separado, etc.), pero con la evolución de ambos se da cuenta de que deberían haberse diseñado como un único módulo.

La primera decisión que debe tomarse en esta situación es cuál es el módulo que se fusionará (por lo que desaparecerá) y cuál contendrá la funcionalidad del otro.

Además, tenga en cuenta que será necesario publicar una nueva versión mayor del módulo que fusiona al otro. Esto ampliará las dependencias de todos los módulos que dependan de este. Asimismo, los módulos que dependan del módulo fusionado no serán compatibles con el nuevo módulo fusionado, por lo que estas dependencias deberán eliminarse, obligando a publicar una nueva versión mayor de dichos módulos.

## Proceso de fusión

Esta sección explica cuáles son los pasos que deben seguirse para fusionar dos módulos en uno.

### Fusión del código

#### Base de datos

El objetivo aquí es reasignar todos los artefactos de la base de datos que pertenecen al módulo fusionado (**B**) al módulo en el que se fusiona (**A**) sin regenerar todos esos artefactos.

La forma más sencilla de hacerlo es editando directamente los archivos `database/sourcedata` dentro del módulo **B**. En todos estos archivos será necesario reemplazar el UUID del módulo **B** por el UUID del módulo **A**.

Después de hacer eso, establezca ambos módulos en desarrollo en la aplicación, ejecute `ant update.database` y luego `ant export.database`. Esta exportación moverá todos los artefactos de base de datos de **B** a **A**.

También es necesario cambiar el paquete de datos de **B** a uno dentro del espacio de nombres de **A** (comenzando por el nombre del paquete Java de **A**).

!!!note
    Este último cambio provocará un cambio en la API porque todas las clases DAL generadas para los artefactos de **B** se reempaquetarán.

#### Java

Todas las clases Java en **B** deben reempaquetarse para incluirse dentro del paquete Java de **A** y los .java deben copiarse dentro del directorio del módulo **A**.

De nuevo, este reempaquetado provocará un cambio en la API para todas las clases originales de **B**.

Debido al cambio de paquete para los artefactos de base de datos, también será necesario adaptar todas las partes en las que se utilizó DAL para ellos al nuevo paquete.

### Definición de la fusión

El último paso es definir la fusión y publicar una nueva versión mayor de **B**.
  
Antes de establecer cuál es el módulo fusionado, es necesario eliminar las dependencias de **B** hacia **A**, porque no está permitido definir un módulo como fusionado y como dependencia al mismo tiempo.

La fusión se define en la solapa `Merges` de la ventana `Module`; aquí es necesario insertar el UUID del módulo fusionado y su nombre. Como el módulo fusionado no forma parte del módulo instalado, no es una relación de clave foránea con la tabla de módulos, sino que se identifica por su UUID como una cadena (String) simple; el nombre se utiliza únicamente para hacerlo legible para las personas.


![alt text](../../../assets/developer-guide/etendo-classic/concepts/merging-modules.png)

### Versión

Todos estos cambios se empaquetarán como una nueva versión del módulo **A**. Es obligatorio que sea una nueva versión mayor, ya que esta nueva versión incluye cambios importantes en toda la API original de **B**.

!!!Note
    Este cambio de versión mayor obligará a todos los módulos que ya dependen de **A** a ampliar su dependencia de **A** para ser compatibles con la última versión mayor.

Además, los módulos que dependen de **B** no serán compatibles con la nueva versión de **A** (ya que no está permitido tener instalado un módulo que fusiona otro módulo junto con un módulo que depende del módulo fusionado), por lo que también deberían publicar una nueva versión mayor eliminando esta dependencia; ahora podrían depender de **A**, ya que incluye la funcionalidad antigua de **B**.

---

Este trabajo es una obra derivada de [Fusión de módulos](http://wiki.openbravo.com/wiki/Merging_Modules){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.