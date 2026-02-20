---
title: Elemento y Sincronizar términos  
tags:
  - Conceptos
  - Diccionario de Aplicación
  - Elemento
  - Etiquetas de campo
  - Traducción
  - Sincronizar términos
---

# Elemento y Sincronizar términos

## Elemento

Los elementos definen el texto de la etiqueta que se mostrará para cada campo en la aplicación, así como su ayuda relacionada. Cada columna en el Diccionario de Aplicación está vinculada a un elemento; tenga en cuenta que más de una columna puede estar vinculada a un único elemento. Esta es la forma de reutilizar el mismo texto para diferentes columnas (y, finalmente, campos) en la aplicación.

Por ejemplo, `C_BPartner_ID` es el nombre de varias columnas en la aplicación; todas ellas son una referencia a un tercero y, por tanto, el texto que se mostrará, así como la ayuda para todas ellas, es el mismo. En lugar de mantener esa información de forma redundante en cada columna, todas estas columnas usan el mismo elemento.

### Mantenimiento de Elemento

Los elementos se pueden editar en la ventana `Application Dictionary` > `Setup` > `Elemento` (como *Administrador del sistema*); pero, normalmente, los elementos no se crean directamente usando esta ventana, sino mediante *Sincronizar términos*. Una vez creado el elemento, esta ventana se utiliza para editar su contenido.

### Sincronizar términos

Es el proceso que crea los elementos para las columnas que todavía no tienen uno asociado y copia la información de los elementos a las columnas y campos que están vinculados a ellos.

Para ejecutarlo, vaya a `Application Dictionary` > `Sincronizar términos` como *Administrador del sistema*.

Básicamente, este proceso busca todas las columnas que no tienen un elemento vinculado. En caso de que exista un elemento con el mismo nombre de columna que el de la columna huérfana, este elemento se vincula a esa columna; en caso contrario, se crea un nuevo elemento con el mismo nombre de columna que tiene la columna.

Todo esto se realiza teniendo en cuenta el módulo; por tanto, un elemento solo se reutiliza si está definido en el mismo módulo que la columna, o en otro dependiente del módulo de la columna. También copia el texto de los elementos a los campos que representan las columnas para esos elementos.

!!!info
    Al crear/editar campos, no tiene sentido escribir un buen texto para los campos de nombre, descripción y ayuda, ya que se sobrescribirán con los del elemento. Cuando se ejecute este proceso, simplemente déjelos vacíos (o con algunas letras en los obligatorios). Por otro lado, al crear una nueva columna, si se crea un nuevo elemento a partir de esta columna, el elemento tendrá el contenido de esos campos de la columna.

!!!note 
    Tenga en cuenta que, una vez creado el elemento, los cambios en los campos de la columna también se sobrescribirán en este proceso.

  
#### En detalle

Estos son todos los pasos que ejecuta el proceso *Sincronizar términos*.

  1. Para todas las columnas y parámetros de proceso del diccionario sin elemento, crear un elemento en caso de que no exista un elemento con el mismo nombre de columna en el mismo módulo o en uno dependiente, copiando al nuevo elemento el nombre, la ayuda y la descripción desde la columna/parámetro.
  2. Eliminar todos los elementos que ya no se usan.
  3. Para el resto de columnas y parámetros de proceso sin elementos, asociar el elemento existente en el mismo módulo o en uno dependiente que tenga el mismo nombre de columna.
  4. Actualizar columnas y parámetros de proceso con los valores de nombre, ayuda y descripción de sus elementos asociados.
  5. Actualizar los campos mantenidos centralizadamente con el nombre, la ayuda y la descripción de los elementos asociados a sus columnas asociadas.
  6. Actualizar los nodos de flujo de trabajo con el nombre y la descripción de sus ventanas vinculadas.
  7. Actualizar las entradas de menú con el nombre y la descripción de sus ventanas, procesos, formularios o flujos de trabajo vinculados.

###  Mantenimiento centralizado para campos

En la mayoría de los casos, el proceso definido anteriormente cubre todos los requisitos para las etiquetas de campo. Pero en algunas ocasiones se desea tener un campo con un conjunto diferente de etiqueta, ayuda y descripción que el resto de campos asociados a la misma columna.

!!!info
    Para estos casos, es posible establecer a no la casilla *Centralizado* en `Application Dictionary` > `Windows, Tabs and Fields` > `Window >> Tab >> Field`; al hacerlo, el nombre, la ayuda y la descripción del campo no se sobrescribirán con los del elemento.

Veamos cómo se utiliza con un ejemplo:

Un nombre de columna muy común es `AD_Language`; estas columnas son una referencia a los idiomas almacenados en la tabla `AD_Language`. El nombre del elemento `AD_Language` es *Idioma* y su ayuda es *El Idioma identifica el idioma que se utilizará para la visualización*, lo cual es muy general.

Los módulos tienen un idioma (que podría ser distinto del inglés) en el que tienen definida la UI. La etiqueta y la ayuda del campo `AD_Language` en `Application Dictionary` > `Módulo` son *Idioma del Módulo* y este idioma define el idioma utilizado como base para los elementos de la interfaz de usuario en el módulo. Esto se realiza configurando el campo de la columna `AD_Language` en la solapa *Traducción* como no mantenido centralizadamente y escribiendo directamente en el campo el nombre y la ayuda.

### Traducción

Como los elementos se utilizan para definir el texto que se mostrará en la UI, se pueden traducir a diferentes idiomas.

El texto del elemento debe escribirse en el idioma que define su módulo, y luego puede traducirse a otros.

!!!note
    La forma estándar de traducir es creando un nuevo módulo sin funcionalidad adicional, pero solo con traducciones para el módulo.

### Asientos de compra

Si observa los campos en `Application Dictionary` > `Setup` > `Elemento`, notará que hay campos estándar (nombre, ayuda...) y otros similares, pero para compras.

En Etendo, hay algunas tablas que se utilizan para transacciones de ventas y compras; por ejemplo, la tabla `C_Invoice` contiene tanto facturas de venta como de compra. Esto significa que las solapas `Purchase Invoice` > `Header` y `Sales Invoice` > `Header` usan la misma tabla. Pero es muy habitual etiquetar campos de la misma columna de forma diferente dependiendo de si se trata de una ventana de venta o de compra.

En lugar de hacerlo configurando todos los campos en las ventanas de compra como `not centrally maintained`, esto se consigue completando, en los elementos correspondientes, los nombres estándar y los de compra. Después, las ventanas se distinguen entre ventas y compras usando la casilla *Operación de venta* en `Application Dictionary` > `Windows, Tabs, and Fields` > `Window` > solapa.

---
  
Este trabajo es una obra derivada de [Elemento y Sincronizar términos](http://wiki.openbravo.com/wiki/Element_and_Synchronize_Terminology){target="\_blank"} de [Wiki de Openbravo](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.