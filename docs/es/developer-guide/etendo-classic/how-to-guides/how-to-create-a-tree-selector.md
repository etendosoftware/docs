---
title: Cómo crear un selector de árbol
tags: 
    - Selector de árbol
    - Selector personalizado
    - Configuración de referencia 
    - Campos del selector
status: beta
---

# Cómo crear un selector de árbol

!!! example "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.


## Visión general

El **Selector de árbol** es una variante especializada del selector estándar de Etendo, diseñada específicamente para tablas que tienen una estructura de árbol asociada. Su configuración y uso siguen los mismos principios que un **selector estándar**, con una diferencia clave: en lugar de mostrar los datos en una cuadrícula tradicional, presenta tanto el **desplegable y la ventana emergente** usando una cuadrícula en árbol, lo que permite a los usuarios navegar por datos jerárquicos de forma más intuitiva.

Árbol desplegable:


![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-tree-selector/how-to-create-a-tree-selector-1.png){: .legacy-image-style}

Árbol emergente:
  
![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-tree-selector/how-to-create-a-tree-selector-2.png){: .legacy-image-style}

## Definición de un selector de árbol

Definir un selector de árbol es muy similar a definir un **selector estándar**.

### Definir una referencia

Abra la **ventana Referencia** y cree un nuevo registro en la solapa de cabecera. Estos son los campos más relevantes:

  * **Nombre, Descripción y Ayuda** deben establecerse con un valor específico para la referencia que está creando 
  * **Referencia base** debe establecerse en false 
  * **Referencia padre** debe establecerse en Referencia de árbol 
  * **Implementación de Modelo, WAD y UI en tiempo de ejecución** puede dejarse vacío la mayoría de las veces si la referencia no es una referencia base. 

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-tree-selector/how-to-create-a-tree-selector-3.png){: .legacy-image-style}

### Definir el selector de árbol

Cree un nuevo registro en la solapa **Referencia de árbol**.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-tree-selector/how-to-create-a-tree-selector-4.png){: .legacy-image-style}

Algunos campos a tener en cuenta: 

- **Tabla**: tabla de árbol a la que apunta este selector. 
- **Categoría de árbol**: Categoría de árbol de tabla que se utilizará para representar jerárquicamente los datos de la tabla seleccionada. 
- **Columna**: la columna en la tabla referenciada a la que apunta la columna de clave foránea. Si no se establece nada aquí (valor por defecto), entonces se utiliza la columna de clave primaria. 
- **Campo de Valor**: este campo del selector de árbol se establece como el valor y se almacena en la base de datos como el campo de clave foránea. 
- **Campo Mostrado**: este campo del selector se muestra en el desplegable del cuadro de sugerencias. 
- **Cláusula HQL 'where'**: esta cláusula where se utiliza para filtrar los datos leídos desde la base de datos. 
- **Clásula HQL Where para nodos raíz**: esta cláusula where se utiliza para especificar cuáles son los nodos raíz de este árbol. Si no se establece, entonces los nodos raíz serán aquellos que tengan parentId = null o parentId = '0'. 

En este punto, todavía no se han definido Campos del selector de árbol, por lo que los campos Campo de Valor y Campo Mostrado están vacíos.

### Definir los campos del selector de árbol

El siguiente paso es definir los **Campos del selector de árbol**. Un campo del selector puede tener varios propósitos:

- Ser usado como Campo de Valor 
- Ser usado como Campo Mostrado 
- Ser mostrado en el árbol desplegable 
- Ser mostrado en el árbol emergente. 

Un selector debe tener al menos dos campos:

- Un campo se utilizará como Campo de Valor 
- El otro campo se utilizará como Campo Mostrado y se mostrará en el árbol desplegable y en el árbol emergente. 

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-tree-selector/how-to-create-a-tree-selector-5.png){: .legacy-image-style}

Algunos campos a tener en cuenta:

- **Nombre**: nombre del campo. Se utilizará en el título de la columna en la ventana emergente. 
- **Propiedad**: es una columna/propiedad de la tabla seleccionada en la solapa Referencia de árbol. 
- **Centralizado**: si está marcado, entonces el nombre, la descripción y la ayuda/comentario se copian/se usan desde la columna. 
- **Mostrar en la Lista**: si está marcado, este campo será visible en el árbol desplegable. 
- **Usado en el cuadro de sugerencias**: si está marcado, este campo se utilizará para filtrar los resultados cuando se introduzca texto en el elemento de formulario del árbol. 
- **Mostrar en grid**: si está marcado, este campo será visible en el árbol emergente. 
- **Nº de orden de registro**: número de secuencia del campo. Se utiliza para establecer el orden de los campos en el árbol desplegable y en el árbol emergente. 
- **Filtro**: si se establece, este campo será filtrable en la ventana emergente 
- **Ordenar**: si se establece, este campo será ordenable en la ventana emergente 

### Establecer los campos Campo de Valor y Campo Mostrado del selector de árbol

Una vez que se han definido los Campos del selector de árbol, se pueden establecer los campos Campo de Valor y Campo Mostrado de la solapa **Referencia de árbol**.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-tree-selector/how-to-create-a-tree-selector-6.png){: .legacy-image-style}


Este trabajo es una obra derivada de [Cómo crear un selector de árbol](http://wiki.openbravo.com/wiki/How_to_Create_a_Tree_Selector){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.