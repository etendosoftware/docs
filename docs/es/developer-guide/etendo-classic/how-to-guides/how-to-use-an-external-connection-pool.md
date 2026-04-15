---
title: Cómo usar un pool de conexiones externo
tags: 
    - Uso
    - Externo
    - Conexión
    - Pool 
    - Cómo

status: beta
---

# Cómo usar un pool de conexiones externo

!!! example "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.

## Visión general

De forma predeterminada, Etendo utiliza dos pools de conexiones:

- Pool de conexiones predeterminado de Hibernate para consultas relacionadas con DAL 
- [Apache DBCP](https://commons.apache.org/proper/commons-dbcp/){target="\_blank"} para las conexiones proporcionadas por `ConnectionProviderImpl`. 

!!!info
    Es posible especificar un proveedor de conexiones externo que Etendo utilizará para obtener las *conexiones JDBC*. Para ello, es necesario instalar un módulo que contenga una subclase de `ExternalConnectionPool`, y se debe establecer la propiedad `db.externalPoolClassName` en el archivo `gradle.properties`.

## Ejemplo: uso del pool de conexiones JDBC de Apache

El módulo core [Apache JDBC Connection Pool](https://github.com/etendosoftware/etendo_core/tree/main/modules_core/org.openbravo.apachejdbcconnectionpool){target="\_blank"} proporciona una implementación del pool de conexiones JDBC de Apache.

La propiedad `db.externalPoolClassName` debe establecerse en `gradle.properties`. Este módulo implementa la clase del pool de conexiones externo en la clase `org.openbravo.apachejdbcconnectionpool.JdbcExternalConnectionPool`, por lo que se debe añadir esta línea a `gralde.properties`:

``` title="Gradle.properties"
db.externalPoolClassName=org.openbravo.apachejdbcconnectionpool.JdbcExternalConnectionPool
```

Este módulo contiene una plantilla de archivo de configuración: `modules_core/org.openbravo.apachejdbcconnectionpool/config/connectionPool.properties.template`. Para personalizar las propiedades del pool de conexiones JDBC, este archivo debe copiarse a `modules_core/org.openbravo.apachejdbcconnectionpool/config/connectionPool.properties`. El usuario puede entonces configurar las propiedades del pool según sus necesidades. Puede encontrar indicaciones sobre cómo configurar estas propiedades [aquí](https://tomcat.apache.org/){target="\_blank"}.

---
Este trabajo es una obra derivada de [Cómo usar un pool de conexiones externo](http://wiki.openbravo.com/wiki/How_to_Use_an_External_Connection_Pool){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.