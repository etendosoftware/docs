---
title: Cómo crear un trigger
tags: 
    - Integridad de datos
    - Triggers
    - Personalización modular
    - PostgreSQL 
    - Oracle
status: beta
---

# Cómo crear un trigger

!!! example "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.

## Visión general

Esta sección se basa en la tabla `HT_Salary` creada en la guía [Cómo crear una tabla](../how-to-guides/how-to-create-a-table.md) y explica cómo aplicar una regla de negocio a nivel de base de datos: los registros de salario solo pueden asignarse a terceros marcados como empleados. Por lo tanto, el sistema debe impedir la introducción de información salarial para terceros definidos únicamente como clientes o proveedores.

Dado que esta regla depende de consultar datos relacionados, no puede implementarse mediante una restricción estándar de comprobación (check constraint) de base de datos. En su lugar, se aplica mediante un **trigger de base de datos**, que es código que se ejecuta automáticamente cuando la tabla se modifica mediante operaciones **INSERT, UPDATE o DELETE**.

!!!info
    Para más información sobre los triggers, visite [Restricciones](../concepts/constraints.md).

## Módulo

Todos los nuevos desarrollos deben pertenecer a un módulo que no sea el módulo **core**.

!!!info
    Siga la sección [Cómo crear un módulo](../how-to-guides/how-to-create-a-module.md) para crear un nuevo módulo.


## Añadir el trigger a la base de datos

Los triggers no requieren ninguna descripción dentro del Diccionario de la Aplicación. Solo necesitan añadirse a la **Base de datos**, siguiendo la regla de `DB Prefix` que indica a qué módulo pertenecen.

Primero añadamos el trigger a la base de datos y después lo comentaremos. Tenga en cuenta que el **código SQL** real varía en función del motor de base de datos utilizado, **Postgres u Oracle**. Aquí tiene un ejemplo para ambos:

``` SQL title="Oracle"
        
    CREATE OR REPLACE TRIGGER ht_salary_trg
    AFTER INSERT OR UPDATE
    ON ht_salary FOR EACH ROW
    
    DECLARE
        v_IsEmployee CHAR(1);
        
    BEGIN
            
        IF AD_isTriggerEnabled()='N' THEN 
            RETURN;
        END IF;

        SELECT IsEmployee
            INTO v_IsEmployee
            FROM C_BPartner
        WHERE C_BPartner_ID = :new.C_BPartner_ID;
    
        IF v_IsEmployee = 'N' THEN
            RAISE_APPLICATION_ERROR(-20000, '@HT_SALARY_NOT_EMPLOYEE@');
        END IF;
    
    END ht_salary_trg;
```


```SQL title="Postgres"        

    CREATE OR REPLACE FUNCTION ht_salary_trg()
        RETURNS TRIGGER AS
    $BODY$ DECLARE 
    
    DECLARE
        v_IsEmployee CHAR(1);
    
    BEGIN
    
        IF AD_isTriggerEnabled()='N' THEN IF TG_OP = 'DELETE' THEN RETURN OLD; ELSE RETURN NEW; END IF; 
        END IF;
    
        SELECT IsEmployee
            INTO v_IsEmployee
            FROM C_BPartner
        WHERE C_BPartner_ID = NEW.C_BPartner_ID;
        
        IF v_IsEmployee = 'N' THEN
            RAISE EXCEPTION '%', '@HT_SALARY_NOT_EMPLOYEE@'; --OBTG:-20000--
        END IF;
    
        IF TG_OP = 'DELETE' THEN RETURN OLD; ELSE RETURN NEW; END IF; 
    
    END; 
    $BODY$ LANGUAGE plpgsql;
    
    CREATE TRIGGER ht_salary_trg AFTER INSERT OR UPDATE ON ht_salary
            FOR EACH ROW EXECUTE PROCEDURE ht_salary_trg();
```

Un desglose aproximado de la estructura de principio a fin es:

- **Nombre del trigger**: el nombre del trigger sigue las convenciones de nomenclatura de modularidad, por lo que si queremos incluir el trigger en nuestro módulo cuyo `DBprefix` es **HT**, el trigger comenzará por **HT**. En este caso, su nombre es `HT_SALARY_TRG`. 
- **Cuándo se ejecuta y para qué tabla**: después del nombre del trigger, defina cuándo se va a ejecutar el trigger. En este caso, defina que se lanzará cada vez que haya una inserción o una actualización en nuestra tabla `HT_SALARY`. Observe la diferencia entre Oracle y Postgres. 
- **Definir variables**: defina las variables locales que necesite; en este caso solo necesitamos una variable para almacenar el indicador de si el tercero es empleado o no. 
- **Habilitar la desactivación suave de triggers**: este código habilita la desactivación suave de triggers, que se utiliza para desactivar todos los triggers de la aplicación dentro de una sesión concreta:

     
    ``` SQL title="Oracle"
    IF AD_isTriggerEnabled()='N' THEN 
        RETURN;
    END IF;
    ```

    ```SQL title="Postgres"    
    IF AD_isTriggerEnabled()='N' THEN
        IF TG_OP = 'DELETE' THEN RETURN OLD; ELSE RETURN NEW; END IF;
    END IF;
    ```
        

- **Seleccionar si es un empleado**: lo siguiente guarda el indicador `IsEmployee` en una variable local que indica si el registro actual es un empleado o no. Tenga en cuenta que para obtener los valores del registro actual podemos usar la variable `:New.C_BPartner_ID`; en caso de que sea una actualización (no una inserción) también existe un conjunto de variables `:Old` con los valores antiguos antes de que se produzca la actualización. 

        
    ```SQL           
        SELECT IsEmployee
        INTO v_IsEmployee
        FROM C_BPartner
        WHERE C_BPartner_ID = :new.C_BPartner_ID;
    ```
        

- **Lanzar un error si no es correcto y revertir la transacción**: una vez que tenemos `v_IsEmployee`, podemos comprobar si es empleado o no y, en caso de que no lo sea, lanzar un error y abortar la transacción. 

    !!!note
        Siempre que un trigger lanza un error, la transacción se revierte. Aquí existe una restricción con la modularidad. Oracle permite un rango de códigos de error de -20000 a -20999 para mensajes personalizados, pero los módulos no pueden definir mensajes personalizados en el Diccionario de la Aplicación porque no pueden seguir las reglas de nomenclatura. Por tanto, al lanzar un error en un trigger dentro de un módulo, debe usarse uno de los códigos existentes (y para enfatizar que no se usa ningún código especial, debe usarse siempre -20000), pero los mensajes mostrados en la UI no serán tan útiles como si se crearan específicamente para este caso. 

        ``` sql
        IF v_IsEmployee = 'N' THEN RAISE_APPLICATION_ERROR(-20000, '@HT_SALARY_NOT_EMPLOYEE@');END IF;
        ```

        

- Para exportar correctamente un **RAISE EXCEPTION** de `postgresql` a archivos `xml`, debe añadir el siguiente comentario al final del comando: `--OBTG:-20000--`. 

    ``` SQL     
    RAISE EXCEPTION '%', '@HT_SALARY_NOT_EMPLOYEE@' ; --OBTG:-20000--
    ```    

- **Devolver la versión correcta del objeto** en el caso de **Postgres**, donde un trigger consiste en una función más una asignación del trigger. 

    ``` SQL 
    IF TG_OP = 'DELETE' THEN RETURN OLD; ELSE RETURN NEW; END IF;
    ```
        

    !!! note
        Si se necesita establecer/cambiar los valores del registro que se está actualizando/insertando dentro del trigger, DEBE usarse la sentencia **BEFORE** INSERT OR UPDATE en lugar de **AFTER** INSERT OR UPDATE.  
 
    
## Añadir mensaje traducible

En el trigger creado anteriormente, el texto del mensaje mostrado al usuario no está **codificado de forma fija**, sino que es simplemente el nombre de una entrada de Mensaje del **Diccionario de la Aplicación**. Definir el mensaje de esta forma permite añadir traducciones del mensaje para distintos idiomas.

!!!info
    Para más información, visite [Mensaje](../concepts/messages.md). 

Como breve resumen:

En la ventana `Diccionario de la Aplicación > Mensaje` cree un nuevo registro. 

Campos a tener en cuenta: 

- **Módulo**: `Etendo Howto`, ya que este es el módulo que contiene la restricción. 
- **Identificador**: `HT_SALARY_NOT_EMPLOYEE`, ya que este es el valor utilizado para buscar el mensaje en el trigger. 
- **Tipo de mensaje**: dependiendo del tipo, la UI del cuadro de mensaje será diferente (verde para éxito, amarillo para advertencia...), en nuestro caso queremos un cuadro de mensaje de error en rojo, así que seleccione **Error**. 
- **Mensaje de texto**: es el mensaje amigable para el usuario que se mostrará dentro del cuadro de mensaje. Por tanto, introduzca: **No se puede añadir salario para un no empleado**. 

## Oracle vs Postgres

Escribir triggers para **Postgres u Oracle** es algo diferente, así que describamos las principales diferencias:

- Los **triggers en Postgres** son funciones que devuelven un objeto trigger asociado a una tabla para una acción específica (INSERT, UPDATE y/o DELETE). En **Oracle**, su definición es ligeramente más simple. Por ello, en Postgres se requieren dos sentencias CREATE (una para la función y otra para asignar la función como trigger de una tabla) frente a una en Oracle. 
- El uso de las palabras reservadas **NEW/OLD** para referenciar el nuevo registro (que se está insertando o actualizando) o el antiguo (que se está eliminando o actualizando) es diferente (`:NEW` en Oracle frente a `NEW` en Postgres). 
- La **función de trigger de Postgres** debe encargarse explícitamente de devolver el objeto trigger, también en función del tipo de trigger (p. ej., la última línea es `IF TG_OP = 'DELETE' THEN RETURN OLD; ELSE RETURN NEW; END IF;`). 



## Exportar triggers como parte del módulo

Siempre que se modifica el Diccionario de la Aplicación o la base de datos física, es posible **exportar** esa información a **archivos xml** pertenecientes al módulo específico. De este modo, es posible mantener los datos de la base de datos de Etendo como **archivos XML de código fuente** que luego pueden controlarse por versiones.

Para ello, ejecute:

        
``` bash title="Terminal"
./gradlew  export.database
```
        

Esto exportará todos los artefactos del módulo actualmente marcados como **En Desarrollo** dentro del Diccionario de la Aplicación.

!!!info
    Para más información, visite la documentación de [Tareas de desarrollo](../developer-tools/etendo-gradle-plugin.md#detailed-build-tasks).

---
Este trabajo es una obra derivada de [Cómo crear un trigger](https://wiki.openbravo.com/wiki/How_To_Create_a_Trigger){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/How_To_Create_a_Trigger){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.