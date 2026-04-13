---
title: Cómo definir el tiempo de espera de una consulta
tags:
    - definir 
    - tiempo de espera
    - consulta
    - cómo
---

# Cómo definir el tiempo de espera de una consulta

## Visión general

Definir el tiempo de espera de una consulta permite cancelar su ejecución una vez que ha transcurrido una determinada **cantidad de tiempo desde que se inició**. Esto ayuda a proteger la base de datos evitando que las consultas queden bloqueadas.

## Clase `QueryTimeOutUtil`

La clase `QueryTimeOutUtil` proporciona métodos `setQueryTimeOut` que definen el tiempo de espera de:

- Sentencias SQL.
- Consultas Hibernate. 
- Criterios Hibernate (`OBCriteria` es una subclase de `Criteria`) 

El primer argumento del método `setQueryTimeOut` es el objeto cuyo tiempo de espera de consulta se va a establecer. El segundo argumento es una cadena que representa un perfil de tiempo de espera (consulte la siguiente sección).

Esta clase también proporciona métodos `resetQueryTimeOut` para restablecer el tiempo de espera a 0.

## Perfiles de tiempo de espera

Los tiempos de espera de las consultas se definen mediante perfiles de tiempo de espera. Un perfil de tiempo de espera representa una actividad del lado del servidor. Por ejemplo, el perfil de tiempo de espera GRID, definido en el core, es utilizado por `DefaultJsonDataService` en las consultas que se realizan para recuperar los registros que se mostrarán en la cuadrícula.

Los tiempos de espera de las consultas se declaran en el archivo `gradle.properties`, usando `db.queryTimeout.<profile_name>=#profile_timeout_in_seconds`.

Por ejemplo, para definir un nuevo perfil llamado `MY_PROCESS` con un tiempo de espera de consulta de 5 segundos, debe añadirse la siguiente línea a `gradle.properties`: 

``` bash
db.queryTimeout.MY_PROCESS=5
```

!!! info 
    Si el tiempo de espera se establece en 0, las consultas que utilicen ese perfil no tendrán un límite en su tiempo de ejecución. Los perfiles de tiempo de espera del core se establecen en 0 de forma predeterminada.

Etendo define en su core estos perfiles de tiempo de espera:

- **`db.queryTimeout.grid`**: consulta utilizada para rellenar la cuadrícula de las ventanas generadas.
- **`db.queryTimeout.jsonWebService`**: consultas utilizadas en el servicio web REST JSON.
- **`db.queryTimeout.xmlWebService`**: consultas utilizadas en el servicio web REST XML.
- **`db.queryTimeout.scheduledProcess`**: consultas ejecutadas en procesos programados.
- **`db.queryTimeout.manualProcess*`**: consultas ejecutadas en procesos manuales.

Si usted crea un proceso y no establece un perfil de consulta para sus consultas, se utilizará de forma predeterminada `db.queryTimeout.scheduledProcess` o `db.queryTimeout.manualProcess`. Puede sobrescribir estos perfiles predeterminados ejecutando `QueryTimeOutUtil.getInstance().setQueryTimeOut` sobre su consulta.

## Ejemplo

Supongamos que un desarrollador está utilizando una consulta que previsiblemente consumirá mucho tiempo, por lo que quiere permitir especificar un límite en su tiempo de ejecución. El desarrollador puede reutilizar un perfil de consulta existente o crear uno nuevo. En este caso, ninguno de los perfiles de consulta existentes aplica, por lo que utiliza uno nuevo al que llama `MY_TIME_CONSUMING_QUERY`.

``` java
String hql = "update ...";
Query qry = OBDal.getInstance().getSession().createQuery(hql);
QueryTimeOutUtil.getInstance().setQueryTimeOut(qry, queryType);
try {
    qry.executeUpdate();
} catch (Exception e) {
    if (e instanceof SQLTimeoutException || e instanceof QueryTimeoutException) {
    // Handle query cancelation due to query timeout
    }
}
```

Si el desarrollador quiere reutilizar el objeto de consulta y quiere restablecer su tiempo de espera de consulta, debe ejecutar este comando:

``` java
QueryTimeOutUtil.getInstance().resetQueryTimeOut(qry);
```

Cuando se instale el módulo que contiene este código, la consulta en realidad no tendrá ningún tiempo de espera hasta que se añada el parámetro `db.queryTimeout.MY_TIME_CONSUMING_QUERY` a `gradle.properties` con un valor superior a 0.

---
Este trabajo es una obra derivada de [Cómo definir el tiempo de espera de una consulta](http://wiki.openbravo.com/wiki/How_to_Define_the_Timeout_of_a_Query){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizado bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.