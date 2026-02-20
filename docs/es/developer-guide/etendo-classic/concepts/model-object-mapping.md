---
title: Mapeo de objetos del modelo
tags:
    - Objeto del modelo 
    - Mapeo
    - Despliegue
    - Servlets

status: beta
---
# Mapeo de objetos del modelo

!!! example  "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.

## Visión general

Las aplicaciones web (como Etendo) tienen un **descriptor de despliegue**. En realidad, es un archivo `XML` (`web.xml`) que define todo lo que el servidor necesita saber sobre la aplicación (servlets, mapeos y otros componentes).

Etendo genera este archivo en tiempo de compilación con la información almacenada en las tablas `AD_Model_Object` y `AD_Model_Object_Mapping`. Este documento explica estas dos tablas.

## Modelo - Concepto de implementación

`AD_Model_Object` es una tabla en el Diccionario de Aplicación de Etendo para vincular componentes del Diccionario de Aplicación y la clase (servlet) que implementa ese objeto. Por tanto, esta tabla es un mapeo entre el lado lógico (componentes AD) y el lado físico (clases). Es útil por dos razones principales:

1. Permite implementar de forma genérica reglas que aplican a todos los componentes `AD`, como seguridad, navegación y otras.
2. Es el mecanismo para poblar automáticamente el archivo web.xml donde se declaran las clases (servlets). `AD_Model_Object_Mapping` es una utilidad para crear las entradas de mapeo en el archivo web.xml.

    Existen algunas excepciones a esta descripción: algunos servlets que se despliegan en el contexto de Etendo pero no están vinculados a ningún componente AD, como los servlets `DataGrid` o `AuditInfo`. Se invocan desde componentes manuales o estándar (ventanas, formularios, etc.) mediante solicitudes HTTP, codificando de forma fija su url-mapping en la solicitud. Aun así, puede interpretarse como un mapeo de clases reales que implementan una funcionalidad que no está descrita en el modelo actual de Etendo, aunque podría estarlo en el futuro.

    Las siguientes secciones explican cómo se definen los distintos elementos.

### Servlets

#### Objetos del Diccionario de Aplicación

En versiones anteriores de Etendo, cuando se creaba una solapa, se creaban nuevos objetos del modelo para ella. Esto ya no ocurre, ya que las entradas de web.xml para solapas se añaden automáticamente al archivo web.xml directamente cuando se realiza la compilación, sin leer información de las tablas de objetos del modelo.

#### Otros servlets

Como se explica en la [sección Modelo - Concepto de implementación](#modelo---concepto-de-implementación), existen algunas situaciones en las que es necesario definir un servlet que no implementa un objeto del Diccionario de Aplicación.

Estos casos se definen en la ventana `Application Dictionary` > `AD Implementation Mapping`. Seleccionando en la solapa **Objeto** el tipo de objeto `Servlet`, configurando la clase Java con la implementación del servlet y añadiendo en la solapa **Mapeo** el mapeo para acceder al servlet.

### Filtro

Los filtros también pueden definirse en la ventana `Application Dictionary` > `AD Implementation Mapping`. Seleccione el tipo de objeto `Filter` y configure la clase Java que implementa el filtro. En la solapa **Mapeo**, añada los patrones de URL para el objeto a filtrar y, en caso de que el filtro reciba algún parámetro, configúrelos en la solapa **Parámetros** con los valores que tendrán. Para recuperar los valores de los parámetros en la implementación, implemente el método `init` como se muestra a continuación:

```
public void init(FilterConfig config) throws ServletException {
encoding = config.getInitParameter("requestEncoding");
if (encoding == null)
    encoding = "UTF-8";
}
```

### Listeners

Los listeners se definen en la ventana `Application Dictionary` > `AD Implementation Mapping` con el tipo `Listener`. En este caso, no es necesario definir `Mapping` ni `Parameters`, solo la clase Java que lo implementa. Tenga en cuenta que los listeners deben ejecutarse en un orden determinado; este orden se define mediante el campo `Sequence number`.

### Recursos

Los recursos se definen en la ventana `Application Dictionary`> `AD Implementation Mapping` con el tipo `Resource`.

Veamos el siguiente ejemplo en `web.xml`:

```
<resource-ref>
<description>Oracle Datasource example</description>
<res-ref-name>jdbc/openbravo</res-ref-name>
<res-type>javax.sql.DataSource</res-type>
<res-auth>Container</res-auth>
</resource-ref>
```

Este recurso se define asignando los siguientes valores a los siguientes campos:

- `Object.Name` : jdbc/openbravo
- `Object.Java Class Name`: javax.sql.DataSource
- `Parameters.Name`: auth
- `Parameters.Search Key`: Container

### Páginas de error
  
Las páginas de error pueden definirse en la ventana `Application Dictionary` > `AD Implementation Mapping` usando el tipo `Error page`.

Si se encuentran múltiples páginas del mismo tipo (p. ej., múltiples páginas 404), la última en `web.xml` será la que se utilizará para gestionar el error. Este orden viene determinado por el número de secuencia del objeto de código de error.

El módulo Core implementa una página de error por defecto con número de secuencia 10. Para sobrescribir esta página, la página creada debe tener un número de secuencia superior a 10 o ser una página de código de error o de tipo de excepción.

Los objetos `Error page` aceptan los siguientes parámetros:

- `location`: la ubicación de la página HTML de error relativa a la ruta de diseño por defecto.
- `error-code` : el código de error HTTP asociado a la página de error, p. ej. 404.
- `exception-type` : el tipo de excepción Java que gestionará la página de error, p. ej. java.lang.RuntimeException

Dependiendo de los parámetros definidos, se generarán los siguientes tipos de páginas de error:

#### Página de error por defecto

Parámetros:

- `location`: org/openbravo/erpCommon/security/Error.html

    ``` 
    <error-page>
    <location>/src-loc/design/org/openbravo/erpCommon/security/Error.html</location>
    </error-page>
    ```

#### Tipo de excepción

Parámetros:

- `location`: org/openbravo/erpCommon/security/Exception.html
- `exception-type`: javax.servlet.ServletException
    
    ```
    <error-page>
    <exception-type>javax.servlet.ServletException</exception-type>
    <location>/src-loc/design/org/openbravo/erpCommon/security/Exception.html</location>
    </error-page>
    ```
  
#### Código de error

Parámetros:

* `location`: org/openbravo/erpCommon/security/Error404.html
* `error-code`: 404

    ```
    <error-page>
    <error-code>404</error-code>
    <location>/src-loc/design/org/openbravo/erpCommon/security/Error404.html</location>
    </error-page>
    ```

## Modularidad y la definición del objeto del modelo

La modularidad de Etendo tiene como objetivo permitir, mediante módulos, el despliegue de cualquier tipo de contenido opcional en una instancia de Etendo, incluidas entradas adicionales en el archivo `web.xml` del contexto de Etendo. Esto se realiza a través de la tabla `AD_Model_Object`. Los desarrolladores pueden crear entradas en esta ventana no vinculadas a ningún componente AD. Para soportar cualquier tipo de contenido de web.xml (servlet, listeners, filtros, etc.), se añade una nueva columna a `AD_Model_Object` para representar el tipo de entrada de `web.xml` que el desarrollador está añadiendo. También pueden declarar un conjunto de mapeos para la entrada y un conjunto de parámetros si es necesario.

El módulo de una entrada `AD_Model_Object` se calcula con la siguiente regla: si está vinculada a algún componente AD, entonces el módulo es el asignado a ese componente AD; en caso contrario, el módulo es el asignado al propio registro `AD_Model_Object`. Tenga en cuenta que el módulo para las tablas hijas de `AD_Model_Object` (`AD_Model_Object_Mapping` y `AD_Model_Object_Para`) es el mismo que el de su registro padre.

Con esta ampliación, el archivo `web.xml` en el contexto de Etendo es totalmente extensible mediante módulos.

En versiones anteriores, la tabla `AD_Model_Object` definía únicamente servlets; otros objetos en el archivo `web.xml` se añadían directamente a su plantilla. En r2.50 el modelo se amplió para permitir la definición de otros objetos (filtros, listeners, recursos y servlets no vinculados a elementos AD) añadiendo la tabla AD_Model_Object_Para y la ventana `Application Dictionary` > `AD Implementation Mapping` para gestionarlo.

---

Este trabajo es una obra derivada de [Mapeo de objetos del modelo](http://wiki.openbravo.com/wiki/Model_Object_Mapping){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.