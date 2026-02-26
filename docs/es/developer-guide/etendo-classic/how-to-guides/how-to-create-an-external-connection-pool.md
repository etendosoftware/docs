---
title: Cómo crear un pool de conexiones externo
tags: 
    - Pool de conexiones
    - Desarrollo de Etendo
    - Configuración de base de datos
    - externalConnectionPool
status: beta
---

# Cómo crear un pool de conexiones externo

!!! example "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.

  
## Visión general

Etendo utiliza **pools de conexiones** para reutilizar conexiones/consultas preparadas existentes, evitando el coste de iniciar una conexión, parsear SQL, etc. Por defecto, Etendo utiliza dos pools de conexiones diferentes:

- Pool de conexiones por defecto de **Hibernate** para consultas relacionadas con el DAL 
- **Apache DBCP** para las conexiones proporcionadas por ConnectionProviderImpl. 

Etendo proporciona un módulo en `modules_core` que implementa el **Tomcat JDBC Connection Pool**, pero es posible que los
desarrolladores publiquen un módulo e implementen su propio pool de conexiones.

## Clase abstracta ExternalConnectionPool

Para implementar un pool de conexiones externo, es necesario crear una subclase de la clase abstracta `ExternalConnectionPool`. Esta clase tiene tres métodos:

``` java    
/**
     * 
     * @param externalConnectionPoolClassName
     *          The full class name of the external connection pool
     * @return An instance of the external connection pool
     */
public final synchronized static ExternalConnectionPool getInstance(
    String externalConnectionPoolClassName) throws InstantiationException,
    IllegalAccessException, ClassNotFoundException;
```

El método `getInstance` se encarga de instanciar el pool de conexiones externo. El nombre de la clase que implementa el pool de conexiones se pasa como parámetro; su valor se toma de la propiedad `db.externalPoolClassName` de `gradle.properties`

``` java
/**
    * @return A Connection from the external connection pool
    */
public abstract Connection getConnection()
```

Este es el método principal que debe ser sobrescrito por todos los proveedores de conexiones externos. No recibe argumentos y debe devolver una conexión que haya sido tomada del pool.

    
```java   
/**
     * If the external connection pool supports interceptors this method should be overwritten
     * 
     * @param interceptors
     *          List of PoolInterceptorProvider comprised of all the interceptors injected with Weld
     */
public void loadInterceptors(List<PoolInterceptorProvider> interceptors)
```

Este método debe ser sobrescrito si el pool de conexiones soporta interceptores y permite que se instancien interceptores personalizados usando inyección de dependencias. Se pasará como argumento una lista de `PoolInterceptorProvider`, que contiene el nombre completo de la clase de los interceptores.

## Consideraciones de diseño

- Incluya un archivo de configuración para que los usuarios puedan personalizar el pool de conexiones externo para satisfacer sus necesidades.
- Si el pool necesita ejecutar algún código de inicialización, colóquelo en el método `getConnection` y asegúrese de que solo se ejecute la primera vez que se invoque ese método. 
- Para todas las conexiones devueltas por el pool:

    - Debe ejecutarse `SessionInfo.setDBSessionInfo(Connection conn, String rdbms)`.
    - La consulta `sql` incluida en la propiedad `bbdd.sessionConfig` debe ejecutarse usando esa conexión.

- Tenga en cuenta que estas dos operaciones deben ejecutarse sobre la conexión devuelta solo cuando la conexión se crea realmente, no cada vez que se devuelve desde el pool.

---
Este trabajo es una obra derivada de [Cómo crear un pool de conexiones externo](http://wiki.openbravo.com/wiki/How_to_Create_an_External_Connection_Pool){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.