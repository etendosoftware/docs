---
tags:
  - How to
  - Etendo classic
  - Crear un procedimiento almacenado
---

# Cómo crear un procedimiento almacenado

## Cómo crear un procedimiento almacenado

Los procedimientos almacenados son uno de los mecanismos que Openbravo ERP proporciona para implementar lógica de negocio. Los procedimientos almacenados son ejecutados por el motor de base de datos y se implementan en el lenguaje estándar PL/pgSQL (para PostgreSQL) o PL/SQL (para Oracle). Se deben comprender las particularidades sobre cómo estos procedimientos PL/SQL se integran con el resto de la aplicación. También es necesario seguir algunas reglas de codificación para que sea posible exportar/importar a archivos XML usando DBSourceManager.

Este documento trata la infraestructura de Openbravo para procedimientos almacenados PL/SQL. Estos actúan como Procesos en el Diccionario de Aplicación.

## Tablas AD_PInstance y AD_PInstance_Para

Antes de implementar un procedimiento PL/SQL es importante entender cómo será llamado desde la aplicación.

Cuando se llama a un procedimiento PL/SQL se crea un nuevo registro dentro de la tabla _AD_PInstance_. Este registro contiene la información sobre el ID del registro desde el que se llamó al procedimiento PL/SQL (en caso de que el proceso se invoque desde un botón dentro de una ventana/solapa). Este registro en la tabla _AD_PInstance_ también es utilizado por la interfaz de usuario para recuperar y mostrar el mensaje resultante que el procedimiento genera cuando finaliza (error o éxito).

En caso de que el proceso tenga parámetros adicionales introducidos por el usuario, se crea un nuevo registro para cada uno de ellos dentro de la tabla _AD_PInstance_Para_. Cada registro contiene la información relacionada con uno de los parámetros, como su nombre (_Nombre columna BD_) y el valor que el usuario le asignó.

Por último, tenga en cuenta que el ID del registro recién creado en la tabla _AD_PInstance_ es el ÚNICO parámetro que se pasa al procedimiento PL/SQL. Es responsabilidad del procedimiento almacenado leer el/los registro(s) de AD_PInstance y AD_PInstance_Para para obtener cualquier parámetro que requiera y escribir el mensaje resultante de vuelta en la tabla _AD_PInstance_.

## Definición del procedimiento

La cabecera de un procedimiento PL/SQL que implementa un proceso tiene este aspecto:

**PostgreSQL**

```
CREATE OR REPLACE FUNCTION HR_TEST(p_PInstance_ID character varying) RETURNS void
```

**Oracle**

```
CREATE OR REPLACE PROCEDURE HR_TEST(p_PInstance_ID IN VARCHAR2)
```

En primer lugar, observe el nombre del procedimiento PL/SQL: sigue las reglas de nomenclatura de modularidad; es decir, comienza con el _DBPrefix_ del módulo.

Tenga en cuenta que el único parámetro que recibe el procedimiento PL/SQL es una cadena; contendrá el UUID de la clave del registro _AD_PInstance_ generado para su invocación.

## Recuperación de parámetros

**PostgreSQL** y **Oracle**

```
SELECT 
  Record_ID, 
  CreatedBy
INTO 
  v_Record_ID, 
  v_User_ID
FROM 
  AD_PInstance
WHERE 
  AD_PInstance_ID = p_PInstance_ID;

FOR Cur_Parameter IN 
(
  SELECT 
    p.ParameterName,
    p.P_String,
    p.P_Number,
    p.P_Date
  FROM 
    AD_PInstance_Para p
  WHERE 
    AD_PInstance_ID=p_PInstance_ID
  ORDER BY 
    p.SeqNo
)
LOOP
  IF(Cur_Parameter.ParameterName='DateFrom') THEN
    v_DateFrom:=Cur_Parameter.P_Date;
  ELSIF(Cur_Parameter.ParameterName='Activate') THEN
    v_Activate:=Cur_Parameter.P_String;
  END IF;
END LOOP; -- Get Parameter
```

El fragmento de código anterior es un ejemplo de cómo se pueden recuperar los parámetros.

El primer `SELECT` obtiene de _AD_PInstance_ los IDs (UUIDs) del usuario que invocó el proceso y el ID del registro desde el que se llamó. El ID del registro solo tiene sentido en caso de que el proceso se llame usando un botón en una solapa. En este caso, este ID identifica el registro en la tabla sobre la que se basa la solapa que contiene el botón. Esto se utiliza para procesos que afectan al registro actual.

A continuación, un bucle obtiene todos los parámetros e itera solo en caso de que el proceso tenga parámetros definidos. Observe que el parámetro se identifica por _ParameterName_, que coincide con el _Nombre columna BD_ definido en el parámetro. Dependiendo de su tipo, el valor real se almacena en una de las siguientes columnas: `P_String`, `P_Number` o `P_Date`. El procedimiento almacenado necesita saber qué esperar y recuperarlo en consecuencia.

## Actualización de _AD_PInstance_

La tabla _AD_PInstance_ tiene una columna `IsProcessing`, que indica si una instancia se está procesando actualmente o no. Al inicio del proceso, la instancia debe marcarse como en procesamiento con:

```
AD_UPDATE_PINSTANCE(p_PInstance_ID, NULL, 'Y', NULL, NULL);
```

Una vez finalizado el proceso, la instancia debe volver a marcarse como no en procesamiento. Además, esta instancia se utilizará para mostrar el resultado del proceso, que se mostrará en la interfaz de usuario. Esto se realiza con:

```
AD_UPDATE_PINSTANCE(p_PInstance_ID, v_User_ID, 'N', v_Result, v_Message);
```

Aquí, el parámetro `v_Result` es un valor numérico: puede ser 0 para error o 1 para éxito. `v_Message` es el mensaje que se mostrará; para más información sobre cómo gestionar mensajes, lea la sección siguiente.

## Gestión de excepciones

Las excepciones en un procedimiento PL/SQL deben capturarse para insertar el mensaje adecuado en la tabla _PInstance_ y que se muestre correctamente al usuario. Por ello, es una buena práctica disponer de una sección _EXCEPTION_ para capturar todas las excepciones en el cuerpo del procedimiento.

Este sería un procedimiento completo con la sección _EXCEPTION_.

**PostgreSQL**

```
CREATE OR REPLACE FUNCTION HR_TEST(p_PInstance_ID character varying)
RETURNS void
$BODY$
  BEGIN
  -- Your code here

  EXCEPTION
  WHEN OTHERS THEN
    v_ResultStr:= '@ERROR=' || SQLERRM;
  RAISE NOTICE '%',v_ResultStr;
  IF(p_PInstance_ID IS NOT NULL) THEN
    PERFORM AD_UPDATE_PINSTANCE(p_PInstance_ID, NULL, 'N', 0, v_ResultStr);
  END IF;
  RETURN;
  END; 
$BODY$
LANGUAGE 'plpgsql' VOLATILE
```

**Oracle**

```
CREATE OR REPLACE PROCEDURE HR_TEST(p_PInstance_ID IN VARCHAR2)

BEGIN

  -- Your code here

  EXCEPTION
  WHEN OTHERS THEN
    v_ResultStr:= '@ERROR=' || SQLERRM;
  DBMS_OUTPUT.PUT_LINE(v_ResultStr);
  IF(p_PInstance_ID IS NOT NULL) THEN
    ROLLBACK;
    AD_UPDATE_PINSTANCE(p_PInstance_ID, NULL, 'N', 0, v_ResultStr);
  ELSE
    RAISE;
  END IF;
END HR_TEST;
```

Como todas las excepciones en el cuerpo se capturan para tomar correctamente el mensaje y añadirlo al _PInstance_ estableciendo el resultado a 0 (error), es posible lanzar excepciones personalizadas cuando se produce algún error lógico durante la ejecución, porque también se capturarán. Por ejemplo, el siguiente fragmento de código realiza algunas comprobaciones y, en caso de fallar, se lanza una excepción.

**PostgreSQL**

```
IF checkFails THEN
  RAISE EXCEPTION '%', '@HR_SomeNiceMessage@';
END IF;
```

**Oracle**

```
IF checkFails THEN
  RAISE_APPLICATION_ERROR(-20000, '@HR_SomeNiceMessage@');
END IF;
```

Para más explicaciones sobre los mensajes, consulte la documentación de Mensajes.

## Funciones

También se admiten funciones de base de datos.

### Volatilidad

Las funciones pueden definir diferentes niveles de volatilidad. Tenga en cuenta que Oracle no implementa ningún equivalente para funciones estables; en caso de que una función se marque en PostgreSQL como estable, se implementará como una función estándar en Oracle añadiendo un comentario para que el XML exportado conserve esta información.

Equivalencias PostgreSQL - Oracle:

| PostgreSQL         | Oracle             |
|--------------------|--------------------|
| Volatile (default) | Valor por defecto  |
| Stable             | N/A                |
| Immutable          | Deterministic      |

---
Este trabajo es una obra derivada de [Cómo crear un procedimiento almacenado](http://wiki.openbravo.com/wiki/How_to_create_a_Stored_Procedure){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.