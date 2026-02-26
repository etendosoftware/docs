---
title: Cómo definir un valor por defecto al crear (on Create Default)
tags:
    - definir 
    - al crear
    - por defecto
    - desarrollo
    - cómo
status: beta
---
# Cómo definir un valor por defecto al crear

!!! example  "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.

## Visión general

En esta sección se explica brevemente qué es un **onCreateDefault**, en qué situaciones es útil y cómo definirlo correctamente.

## Concepto

Los `OnCreateDefaults` son sentencias `SQL` que se ejecutan mediante la tarea `update.database` cuando se crea una columna en la base de datos. Normalmente se utilizan para insertar datos en una columna recién creada. Es importante tener en cuenta que solo se ejecutan cuando la columna se está creando. Si la columna ya existe en la base de datos, `update.database` no ejecutará la sentencia `onCreateDefault`. Para rellenar datos en una columna ya creada, puede utilizar un Script de módulo. Para más información sobre los Scripts de módulo, visite [Cómo crear validaciones de compilación y Scripts de módulo](../how-to-guides/how-to-create-build-validations-and-module-scripts.md).

## Proceso de desarrollo

Las sentencias `onCreateDefault` se añaden directamente al archivo `XML` de la tabla. Esto significa que los pasos principales de desarrollo deberían ser:

- Añadir la nueva columna en la base de datos 
- Ejecutar la tarea `export.database` para exportar la columna al archivo `XML` 
- Editar el archivo `XML` para añadir el `onCreateDefault` 

Una sentencia `onCreateDefault` debe ser un `SQL` válido que pueda añadirse al final en dos tipos diferentes de comandos `SQL`. Supongamos que la tabla `C_BPARTNER` se va a ampliar, añadiendo una columna `MYCOLUMN`. Necesitamos diseñar una sentencia `onCreateDefault` que funcione con los dos tipos siguientes de comandos `SQL`:

```sql
INSERT INTO C_BPARTNER (Column1, Column2, ..., MYCOLUMN) SELECT (Column1, Column2, ..., MYCOLUMN_ONCREATEDEFAULT) FROM C_BPARTNER_
 
UPDATE C_BPARTNER SET Column1=ValueForCol1, Column2=ValueForCol2, ..., MYCOLUMN=(MYCOLUMN_ONCREATEDEFAULT)
```

Así, en este caso, imaginemos que `MYCOLUMN` es una columna `Sí/No`, y queremos establecerla como 'N' para las filas existentes de `C_BPARTNER` cuando la columna se cree por primera vez. Modificaríamos la definición de la columna para que se vea así:

``` XML
<column name="MYCOLUMN" primaryKey="false" required="true" type="CHAR" size="1" autoIncrement="false">
<default><![CDATA[N]]></default>
<onCreateDefault><![CDATA['N']]></onCreateDefault>
</column>
```

Observe la diferencia de sintaxis en el `onCreateDefault`, en comparación con el valor por defecto estándar. Necesitamos añadir comillas ahí, debido al tipo de comando `SQL` en el que se insertará el `onCreateDefault`.

!!! note "Importante"
        
    - La sentencia SQL `onCreateDefault` **debe devolver solo una fila**. 
    - La ejecución del `onCreateDefault` tiene lugar mientras la tabla se está reconstruyendo. Esto significa que, si la sentencia falla, podría haber pérdida de datos en la base de datos del cliente cuando se instale el módulo. Por lo tanto, **la sentencia debe construirse de forma que siempre pueda ejecutarse**. 

Una limitación de la implementación actual de `onCreateDefaults` es que, debido a la necesidad de soportar los dos tipos diferentes de sintaxis `SQL`, no puede hacer referencia a una columna distinta de la tabla que está modificando. Esto significa que puede ser muy complicado diseñar un `onCreateDefault` correcto en situaciones en las que necesita crear un enlace a otra tabla. Para estas situaciones, podría utilizarse un **Script de módulo** en lugar de un `onCreateDefault`, y se puede lograr el mismo resultado de esta manera.

## Cómo eliminar correctamente un `onCreateDefault`

Los `onCreateDefaults` también se eliminan editando el archivo `XML`. La forma correcta de eliminarlo es borrar el contenido dentro de la etiqueta <onCreateDefault>, pero dejando la propia etiqueta. Si elimina todo, incluida la etiqueta, la próxima vez que exporte el módulo (o el Core, si está editando una columna del Core), habrá una inconsistencia, ya que [DBSourceManager](../concepts/dbsourcemanager.md) creará un elemento `onCreateDefault` vacío. En un ejemplo práctico, la siguiente columna tiene un `onCreateDefault`:

``` xml
<column name="MYCOLUMN" primaryKey="false" required="true" type="CHAR" size="1" autoIncrement="false">
<default><![CDATA[N]]></default>
<onCreateDefault><![CDATA['N']]></onCreateDefault>
</column>
```

Si queremos eliminarlo, la forma correcta sería dejar la columna así:

``` xml
<column name="MYCOLUMN" primaryKey="false" required="true" type="CHAR" size="1" autoIncrement="false">
<default><![CDATA[N]]></default>
<onCreateDefault/>
</column>
```

---
Este trabajo es una obra derivada de [How to Define an on Create Default](http://wiki.openbravo.com/wiki/How_to_define_an_on_Create_Default){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.