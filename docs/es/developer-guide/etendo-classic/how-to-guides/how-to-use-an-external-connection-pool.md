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

# Cómo usar un pool de conexiones externo { #how-to-use-an-external-connection-pool }

!!! example "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.

## Visión general { #overview }

Etendo incluye el [Apache JDBC Connection Pool](https://github.com/etendosoftware/etendo_core/tree/main/modules_core/org.openbravo.apachejdbcconnectionpool){target="\_blank"} habilitado de forma predeterminada, a través del módulo core `org.openbravo.apachejdbcconnectionpool`. Este módulo implementa la abstracción `ExternalConnectionPool` de Etendo sobre el [Apache Tomcat JDBC Connection Pool](https://tomcat.apache.org/tomcat-9.0-doc/jdbc-pool.html){target="\_blank"}. No se requiere ningún paso de instalación: `Openbravo.properties` ya establece

```properties title="Openbravo.properties"
db.externalPoolClassName=org.openbravo.apachejdbcconnectionpool.JdbcExternalConnectionPool
```

Dado que el pool ya está activo en toda instalación, el trabajo descrito en esta página consiste en ajustar sus propiedades — consulte [Configuración del pool](#pool-configuration) más abajo. Cambiar `db.externalPoolClassName` por otra clase solo es necesario para conectar una implementación de pool de conexiones externo **personalizada** en lugar de la incluida por defecto; consulte [Cómo crear un pool de conexiones externo](how-to-create-an-external-connection-pool.md) para ese escenario.

Las propiedades del pool se establecen en `gradle.properties`. Después de añadir o modificar cualquiera de ellas, aplique el cambio con:

```bash
./gradlew setup
```

Esto regenera `Openbravo.properties`, que es el archivo que `JdbcExternalConnectionPool` lee en tiempo de ejecución para construir el pool.

## Configuración del pool { #pool-configuration }

Una instalación nueva de Etendo viene con las siguientes propiedades ya establecidas:

```properties title="Openbravo.properties (generado)"
db.pool.initialSize=1
db.pool.minIdle=5
db.pool.maxActive=10000
db.pool.timeBetweenEvictionRunsMillis=60000
db.pool.minEvictableIdleTimeMillis=120000
db.pool.removeAbandoned=false
db.pool.testOnBorrow=true
db.pool.testWhileIdle=false
db.pool.testOnReturn=false
db.pool.validationQuery=SELECT 1 FROM DUAL
db.pool.validationInterval=30000
db.pool.jmxEnabled=false
```

Puede sobrescribir cualquiera de ellas estableciendo la propiedad correspondiente en `gradle.properties`:

| Propiedad | Descripción | Valor predeterminado |
| --- | --- | --- |
| `db.pool.initialSize` | Conexiones establecidas cuando arranca el pool. Se reduce automáticamente si supera `db.pool.maxActive`. | `1` |
| `db.pool.minIdle` | Número mínimo de conexiones establecidas que se mantienen en el pool en todo momento. El pool de conexiones inactivas no se reduce por debajo de este valor durante una ejecución de desalojo, pero puede bajar más si `db.pool.validationQuery` falla y se cierran conexiones. | `5` |
| `db.pool.maxActive` | Número máximo de conexiones activas que el pool puede entregar al mismo tiempo. Se mantiene alto de forma predeterminada porque la planificación de capacidad se delega a la base de datos; debería ser al menos tan alto como el número máximo de conexiones de la propia base de datos. Si se reduce por debajo de ese valor, `db.pool.maxWait` pasa a ser relevante. | `10000` |
| `db.pool.timeBetweenEvictionRunsMillis` | Cada cuánto (ms) el hilo sweeper revisa las conexiones inactivas y abandonadas. Consulte [¿Cómo funciona el hilo sweeper?](#how-does-the-sweeper-thread-work). No debería establecerse por debajo de `1000`. | `60000` |
| `db.pool.minEvictableIdleTimeMillis` | Tiempo mínimo (ms) que una conexión puede permanecer inactiva antes de que el sweeper la desaloje. | `120000` |
| `db.pool.removeAbandoned` | Si es `true`, las conexiones retenidas más tiempo que `db.pool.removeAbandonedTimeout` se recuperan por la fuerza. | `false` |
| `db.pool.testOnBorrow` | Valida una conexión antes de entregarla; si no es válida, la descarta y lo intenta de nuevo. Requiere que `db.pool.validationQuery` esté establecida. | `true` |
| `db.pool.testOnReturn` | Valida una conexión cuando se devuelve al pool. | `false` |
| `db.pool.testWhileIdle` | Valida periódicamente las conexiones inactivas. | `false` |
| `db.pool.validationQuery` | SQL utilizada para validar una conexión. No debe lanzar una excepción. Es obligatoria para que `testOnBorrow`, `testOnReturn` y `testWhileIdle` tengan algún efecto. | `SELECT 1 FROM DUAL` |
| `db.pool.validationInterval` | Milisegundos mínimos entre validaciones de la misma conexión, para evitar comprobaciones redundantes. | `30000` |
| `db.pool.jmxEnabled` | Expone las métricas del pool a través de JMX. | `false` |

El pool también admite las siguientes propiedades. Etendo no establece un valor predeterminado para ninguna de ellas — cuando una propiedad no está establecida en `gradle.properties`, se aplica el valor predeterminado del [Apache Tomcat JDBC Connection Pool](https://tomcat.apache.org/tomcat-9.0-doc/jdbc-pool.html#Common_Attributes){target="\_blank"} subyacente:

| Propiedad | Descripción |
| --- | --- |
| `db.pool.maxIdle` | Número máximo de conexiones inactivas que se mantienen en el pool cuando el sweeper está deshabilitado. |
| `db.pool.maxWait` | Milisegundos que el pool espera a que se devuelva una conexión antes de lanzar una excepción, una vez alcanzado `db.pool.maxActive`. |
| `db.pool.numTestsPerEvictionRun` | Número de conexiones examinadas en cada ejecución del sweeper. |
| `db.pool.removeAbandonedTimeout` | Segundos que una conexión puede estar retirada antes de considerarse abandonada. Solo es relevante cuando `db.pool.removeAbandoned=true`. |
| `db.pool.testOnConnect` | Valida una conexión justo después de que se crea físicamente. |
| `db.pool.validatorClassName` | Clase validadora personalizada que se usa en lugar de `db.pool.validationQuery`. |
| `db.pool.initSQL` | SQL que se ejecuta una vez, justo después de crear una conexión física. |
| `db.pool.defaultAutoCommit` | Estado predeterminado de auto-commit de las conexiones que entrega el pool. |
| `db.pool.defaultReadOnly` | Estado de solo lectura predeterminado de las conexiones que entrega el pool. |
| `db.pool.defaultTransactionIsolation` | Nivel de aislamiento de transacción predeterminado de las conexiones que entrega el pool. |
| `db.pool.defaultCatalog` | Catálogo predeterminado de las conexiones que entrega el pool. |
| `db.pool.connectionProperties` | Propiedades de conexión adicionales específicas del driver, como una lista de pares `nombre=valor` separados por punto y coma. |
| `db.pool.accessToUnderlyingConnectionAllowed` | Permite obtener la conexión física subyacente a través del envoltorio de la conexión del pool. |
| `db.pool.logAbandoned` | Registra la traza de pila de dónde se tomó prestada una conexión una vez que ha estado retirada más tiempo que `db.pool.suspectTimeout`. Añade sobrecarga a cada solicitud de conexión, porque se debe generar una traza de pila. |
| `db.pool.suspectTimeout` | Segundos que una conexión puede estar retirada antes de registrarse como sospechosa. Solo es relevante cuando `db.pool.logAbandoned=true`. Es independiente de `db.pool.removeAbandoned` — una conexión sospechosa solo se registra, no se recupera. |
| `db.pool.name` | Nombre asignado al pool, útil para distinguir pools cuando hay varios configurados. |

!!!info
    Cualquiera de estas propiedades puede limitarse a un pool con nombre específico —por ejemplo, el pool de solo lectura— insertando el nombre del pool después de `db.`, por ejemplo `db.readonly.pool.maxActive`. Un valor específico de un pool tiene prioridad sobre el valor predeterminado `db.pool.*` para ese pool; un pool que no define su propio valor recurre al predeterminado.

### ¿Cómo funciona el hilo sweeper? { #how-does-the-sweeper-thread-work }

El sweeper es el hilo en segundo plano que se ejecuta cada `db.pool.timeBetweenEvictionRunsMillis` milisegundos para validar las conexiones inactivas y comprobar si hay conexiones abandonadas. Que esté habilitado o no cambia el comportamiento del pool de conexiones inactivas:

- **Sweeper deshabilitado**: si el pool de conexiones inactivas crece por encima de `db.pool.maxIdle`, una conexión se cierra en cuanto se devuelve al pool en lugar de mantenerse inactiva.
- **Sweeper habilitado**: el número de conexiones inactivas puede crecer por encima de `db.pool.maxIdle`, pero vuelve a bajar hasta `db.pool.minIdle` una vez que una conexión ha estado inactiva más tiempo que `db.pool.minEvictableIdleTimeMillis`.

La lista completa de atributos configurables del Tomcat JDBC Connection Pool está disponible en la [documentación de Apache Tomcat](https://tomcat.apache.org/tomcat-9.0-doc/jdbc-pool.html#Common_Attributes){target="\_blank"}, junto con [indicaciones para ajustar el pool en entornos de alta concurrencia](https://www.tomcatexpert.com/blog/2010/04/01/configuring-jdbc-pool-high-concurrency){target="\_blank"}.

---
Este trabajo es una obra derivada de [Cómo usar un pool de conexiones externo](http://wiki.openbravo.com/wiki/How_to_Use_an_External_Connection_Pool){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.
