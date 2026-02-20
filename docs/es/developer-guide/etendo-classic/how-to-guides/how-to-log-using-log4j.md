---
title: Cómo registrar usando Log4j
tags:
    - log
    - nivel de registro
    - contexto
    - registro
    - errores de log
    - log4j
status: beta
---

# Cómo registrar usando Log4j

!!! example "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.
  
## Visión general

Esta sección proporciona algunas directrices sobre qué y cómo registrar.

Etendo genera un archivo de log que sirve para diferentes propósitos:

- Notificar errores funcionales como una configuración incorrecta, una ejecución de flujo incorrecta, etc. 
- Alertar sobre errores inesperados que normalmente se deben a problemas en el código. 
- En caso de problemas, ayudar a depurar y comprender sus causas raíz. 

Está pensado para ser consumido por personal técnico como administradores de sistemas, desarrolladores, equipo de soporte, etc.

Para aprender a configurar los logs, lea [este documento](./how-to-configure-log.md) .

## Cómo registrar

!!!warning
    La salida estándar `System.out`, `System.err` o `printStackTrace` **nunca debe utilizarse**.

    Escriben el log en un archivo diferente `catalina.out`, que tiene varios inconvenientes:

    - Tener una única fuente de logs facilita mucho la búsqueda de problemas. 
    - ` catalina.out ` no se rota automáticamente, por lo que su tamaño podría aumentar sin límite. 
    - La información importante no se incluye automáticamente: no incluye marca de tiempo ni la clase que genera el log.
    
  
Etendo incluye **log4j2** como framework de registro, por lo que todos los logs deben escribirse haciendo uso de este.

El siguiente fragmento muestra cómo escribir una línea de advertencia en el log:
 
``` java
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
 
private class Example {
// gets logger for this class
private static final Logger log = LogManager.getLogger();
 
private void process(Invoice invoice) {
    // ...
    log.warn("Invoice {} could not be processed because config XXX is missing", invoice.getId());
}
}
```

### Desglosando una línea de log

El log producido por cualquiera de los dos fragmentos anteriores se verá como sigue (asumiendo que este código se ejecuta en Tomcat con la configuración por defecto. Las configuraciones de test y build pueden tener ligeras diferencias en el formato):

```
2018-11-14 13:37:08,377 [http-nio-8080-exec-4] WARN org.openbravo.example.Example - Invoice AAA could not be processed because config XXX is missing
----------------------- ---------------------- ---- -----------------------------   ----------------------------------------------------------------
            |                       |           |              |                                         |-> Actual message
            |                       |           |              |-> Java class producing the message
            |                       |           |-> Message level
            |                       |-> Thread name
            |-> Timestamp when the log was generated
```

## Qué registrar

Los logs son una parte muy importante de la aplicación; por ello, es clave pensar cuidadosamente cuál es la información relevante que debe registrarse. Tenga en cuenta que, normalmente, los logs se van a leer tiempo después de que se creen, por lo que deben contener todo lo necesario para reproducir problemas en el futuro.

### Nivel

El registro puede escribirse en diferentes niveles. Cuando un nivel de registro está habilitado, todos los mensajes escritos en ese nivel o en cualquier nivel superior se guardarán en el archivo de log. Por defecto, se escriben `INFO` y niveles superiores, omitiendo los niveles inferiores. Esto puede modificarse de forma permanente o en tiempo de ejecución a un nivel diferente para cada logger o para loggers específicos.

Los niveles disponibles, ordenados de mayor a menor prioridad, son:

- **FATAL**: este nivel se utiliza para un error grave que impedirá que la aplicación continúe. 
- **ERROR**: este nivel debe reservarse para los casos en los que deba tomarse una acción inmediata. Por ejemplo, problemas inesperados que pueden estar causados por bugs en el código, problemas funcionales graves, etc. 
- **WARN**: esta categoría debe utilizarse para problemas que podrían requerir una acción, pero no es necesario que sea inmediata. 
- **INFO**: información relevante que ayuda a entender el uso del sistema cuando todo funcionó como se esperaba. 
- **DEBUG**: en caso de áreas problemáticas, los mensajes en este nivel deben proporcionar información a los desarrolladores para reproducir el problema y entender de dónde proviene. 
- **TRACE**: similar a DEBUG, se utiliza para complementar el nivel anterior con información mucho más detallada. 

### Contexto

Dado que el log debe proporcionar suficiente información para saber qué está ocurriendo, es de suma importancia incluir el contexto relevante en cada línea de log. Este contexto dependerá de lo que esté haciendo el código; en general, debe incluir los valores de parámetros relevantes para permitir reproducir la ejecución.

Por ejemplo:

``` java
// DO NOT do this!
log.warn("Could not process invoice.");
```

Este código advierte sobre una factura que no pudo procesarse, pero no proporciona ninguna información sobre qué factura es y por qué falló.

Lo siguiente sería ligeramente mejor:

``` java
log.warn("Invoice {} could not be processed", invoice.getId());
```

porque indica la factura que falló, por lo que ayudaría a intentar reproducir el problema. Dependiendo del propio proceso, también podría ser necesario incluir otros parámetros; por ejemplo:

``` java
log.warn("Invoice {} could not be processed with action: {}", invoice.getId(), action);
```

#### Advertencias

El registro puede generar sobrecarga de rendimiento; tenga cuidado al seleccionar qué registrar en cada nivel. Por ejemplo, si solo dispone de un ID de Tercero, puede ser preferible registrar únicamente ese ID en lugar de su nombre si es necesario recuperarlo de la base de datos.

Tenga cuidado al registrar el contexto para no crear nuevas excepciones. Por ejemplo, la siguiente línea de log podría lanzar una `NullPointerException` en caso de que la variable `invoice` sea `null` cuando se ejecute: `log.debug("Processing invoice", invoice.getId());`

!!!note
    Por motivos de rendimiento, **log4j** evita usar varargs en llamadas de log con hasta 10 valores de placeholder. Al usar más de 10 parámetros, se utilizará la versión varargs de la llamada.

### Trazas de pila

Las trazas de pila muestran la pila de llamadas de un hilo en el momento en que se generaron; es decir, de forma recursiva, la línea de código que estaba en ejecución, así como la línea que invocó el método actual, la línea que invocó ese método y así sucesivamente.

En ocasiones, pueden aportar un gran contexto a los desarrolladores para encontrar las causas de los problemas.

El siguiente código registrará un mensaje de error y la traza de pila de ese hilo cuando ocurrió:

``` java
try {
// ...
} catch (MyException e) {
log.error("could not process invoice " + invoice.getId(), e);
// handle error here: just logging won't fix it
}
```

!!!note
    El siguiente código **no** incluirá ninguna traza de pila:

    ``` java
    } catch (MyException e) {
    log.error(e); // no stack trace!!
    }
    ```
    ya que es equivalente a:

    ``` java
    } catch (MyException e) {
    log.error(e.getMessage());  // no stack trace!!
    }  
    ```
  
Aunque pueden ser útiles en algunas ocasiones, también tienden a ser muy verbosas. Los archivos de log con demasiadas trazas de pila suelen ser difíciles de leer. Por tanto, como cualquier otra información de contexto, es necesario seleccionar cuidadosamente si incluirlas o no. Como directriz básica:

**Inclúyalas** para:

- Errores técnicos inesperados (p. ej., `NullPointerException`). 
- Errores detectados en APIs que pueden consumirse desde muchos lugares diferentes. Esto ayudará a entender desde dónde se invocaron. 

Pero **no las incluya** para:

- Validaciones. 
- Errores funcionales. 
- Errores esperados y gestionados. 
- Casos en los que no aporta información valiosa; por ejemplo, si solo existe un flujo de invocación posible para ese código. 

#### OBException

`OBException` es una excepción no comprobada. 

``` java
throw new OBException("Something failed"); // does not log anything

throw new OBException("Something failed", true); // logs exception with stack trace
```

No obstante, es posible generar automáticamente un log cada vez que se crea una nueva instancia de `OBException` configurando el logger `org.openbravo.base.exception.OBException` en el nivel `DEBUG`.

---
Este trabajo es una obra derivada de [Cómo registrar](http://wiki.openbravo.com/wiki/How_To_Log){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.