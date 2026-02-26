---
title: Restricciones
tags: 
  - Concepts
  - Constraint
  - Indexes
---

# Restricciones

## Visión general

Tanto las restricciones de comprobación como los triggers son objetos definidos físicamente en la base de datos. Este documento no explicará los fundamentos de las restricciones, sino únicamente las particularidades que Etendo Classic tiene en su uso.

##  Nomenclatura

Al añadir una restricción de comprobación, triggers e índices, deben tenerse en cuenta las reglas de nomenclatura de modularidad. Esto es necesario porque los triggers y los índices son objetos globales para una base de datos. 

La regla de nomenclatura de modularidad es la siguiente: 
el nombre de la restricción, índice o trigger debe comenzar con el prefijo de BD del módulo al que pertenece la restricción. 

Por ejemplo,`MYMODULEDBPREFIX_CONSTRAINTNAME`.

En el caso de índices y restricciones, si el índice/restricción se añade a una
tabla de otro módulo, entonces se requiere un prefijo adicional `EM_`:

`EM_MYMODULEDBPREFIX_CONSTRAINTNAME`.

Siguiendo esta regla de nomenclatura, el índice/trigger/restricción se exporta al
directorio del módulo y se empaqueta con el módulo.

!!!info
    El nombre de las restricciones no debe exceder los 30 caracteres, ya que la longitud máxima del nombre de un objeto en Oracle es de 30 caracteres.  

##  Restricciones

Las restricciones de comprobación no tienen ninguna particularidad en Etendo, excepto por cómo deben nombrarse y cómo el back-end las trata para mostrar mensajes.

!!!info
    Para más información, lea [Cómo añadir una restricción](../how-to-guides/how-to-add-a-constraint.md).

###  Mensaje

Es posible definir un mensaje que se mostrará cuando no se satisfaga la regla definida por la restricción. 

!!!info
    Cómo hacerlo se explica en la documentación de [Mensaje](Messages.md#checks).

###  Compatibilidad hacia atrás

Los módulos deberían permitir compatibilidad con otros construidos sobre ellos al menos entre versiones menores; adicionalmente, podría haber datos de usuario ya existentes en la aplicación si se encuentra en un entorno productivo. 
Esto significa que los datos de usuario u otros módulos podrían depender del modelo actual de base de datos y, en caso de que se añada una nueva restricción o se modifique una existente para que sea más restrictiva
de lo que era, podría romperse la compatibilidad hacia atrás. Por lo tanto, debe evitarse añadir nuevas restricciones o modificar las existentes para hacerlas más restrictivas entre versiones.

##  Índices

###  Clases de operador

  
En PostgreSQL, determinadas [Clases de operador](https://www.postgresql.org/docs/9.3/indexes-opclass.html){target="\_blank"} (`text_pattern_ops`,
`varchar_pattern_ops` y `bpchar_pattern_ops`) permiten usar índices en consultas
que implican expresiones de coincidencia de patrones. Por ejemplo, la siguiente consulta:

    
```sql   
    SELECT name
    FROM c_bpartner
    WHERE name LIKE 'John%'
```
no usaría un índice creado así:

    
```sql   
    CREATE INDEX c_bpartner_name
      ON c_bpartner
      USING btree
      (name COLLATE pg_catalog."default");
```

pero sí usaría un índice definido con una clase de operador:

    
```sql 
    CREATE INDEX c_bpartner_name
      ON c_bpartner
      USING btree
      (name COLLATE pg_catalog."default" varchar_pattern_ops);
```

Las clases de operador no son necesarias en Oracle para usar un índice en la consulta definida anteriormente; en ese caso, si la columna del índice define una clase de operador, la clase de operador no tendrá efecto.

###  Índices basados en funciones

  
Etendo admite el uso de funciones en índices. Por ejemplo, esto, junto con el uso de una clase de operador, permitiría el uso de índices en consultas sin distinción de mayúsculas y minúsculas que usan el operador iStartsWith, como esta:

    
```sql
    SELECT name
    FROM c_bpartner
    WHERE UPPER(name) LIKE 'JOHN%'
```

El siguiente índice podría ser usado por la consulta anterior:

    
```sql
    CREATE INDEX c_bpartner_name
      ON c_bpartner
      USING btree
      (upper(name) COLLATE pg_catalog."default" varchar_pattern_ops);
```

Cualquier función puede usarse en los índices, siempre que sea determinista. Incluso
se admiten funciones anidadas:

    
```sql 
    CREATE INDEX c_bpartner_name
      ON c_bpartner
      USING btree
      (UPPER(REPLACE(name, 'a', 'b')));
```
El siguiente índice también puede usarse.

    
```sql
    CREATE INDEX c_bpartner_name_id
      ON c_bpartner
      USING btree
      (UPPER(REPLACE(name, 'a', 'b')),
       UPPER(c_bpartner_id));
```


  
###  Índices parciales
  
`PostgreSQL` admite la definición de [índices parciales](https://www.postgresql.org/docs/9.3/indexes-partial.html){target="\_blank"}. Un índice parcial es un índice en el que es posible especificar las filas que se indexan. Este tipo de índices es útil para condiciones _WHERE_ de uso común que utilizan valores constantes.

Así, con un índice parcial es posible indexar solo los datos de la tabla que se usan con mayor frecuencia, ayudando a reducir la cantidad de espacio en disco utilizado por el índice.

Un índice parcial puede crearse de la siguiente manera:

    
```sql
    CREATE INDEX a_amortization_active 
      ON a_amortization (isactive)
      WHERE isactive = 'Y';
```

Oracle todavía no admite la creación de índices parciales de forma explícita. Por esta razón, si se encuentra un índice parcial en el modelo XML de Etendo al usar una base de datos Oracle, la definición del índice parcial no se tiene en cuenta y se crea como un índice normal.
  
####  Índices parciales NOT NULL en columnas anulables

En una base de datos Oracle, no se incluyen filas en un índice si las columnas indexadas son NULL. Eso significa que, para el caso en el que se está indexando una columna de clave externa anulable, cada índice es un índice parcial.

Este no es el comportamiento en las `bases de datos PostgreSQL`, donde necesitaremos definir el índice como parcial para obtener el mismo comportamiento. Por ejemplo:

    
```sql 
    CREATE INDEX c_order_return_reason 
      ON c_order (c_return_reason_id)
      WHERE c_return_reason_id IS NOT NULL;
```

###  Índices para búsqueda por contiene

  
Los índices para búsqueda por *contiene* son aquellos destinados a proporcionar una búsqueda rápida de subcadenas dentro de los valores almacenados en una columna concreta de la base de datos.

En PostgresSQL podemos definir un índice de búsqueda por contiene de la siguiente manera:

    
```sql
    CREATE INDEX c_bpartner_value_basic ON c_bpartner USING gin (value gin_trgm_ops);
```

!!!note
    Para definir este tipo de índices, tenemos que hacer uso del método de
    acceso ` gin ` junto con la clase de operador ` gin_trgm_ops ` para
    la columna indexada. Ambos elementos están disponibles gracias a la extensión
    ` pg_trgm ` que se incluye en la distribución de Etendo por defecto.

Además, esta funcionalidad permite definir un [índice basado en funciones](#índices-basados-en-funciones) para mejorar la búsqueda icontains (sin distinción de mayúsculas y minúsculas):

    
```sql
    `CREATE INDEX c_bpartner_value_basic ON c_bpartner USING gin (UPPER(value) gin_trgm_ops);`
```

!!!info
    Este tipo de índices todavía no está soportado en Oracle: si están presentes en el modelo XML, se crearán como índices normales en la base de datos.

---

Este trabajo es una obra derivada de [Restricciones y triggers](http://wiki.openbravo.com/wiki/Constraints_and_Triggers){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, usado bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.