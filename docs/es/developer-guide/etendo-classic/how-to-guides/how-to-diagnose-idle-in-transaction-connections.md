---
title: Cómo diagnosticar conexiones en estado idle in transaction
tags:
  - Pool de conexiones
  - Solución de problemas
  - Base de datos
  - PostgreSQL
  - Hibernate
  - DAL
status: beta
---

# Cómo diagnosticar conexiones en estado idle in transaction { #how-to-diagnose-idle-in-transaction-connections }

!!! example "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.

## Visión general { #overview }

Etendo atiende la mayoría de las solicitudes a través de `DalFilter`, que abre una sesión de Hibernate/DAL al inicio de la solicitud y la cierra una vez enviada la respuesta. Los servlets, procesos o endpoints de servicios web personalizados que llaman a `OBDal.getInstance()` o abren una sesión de `SessionHandler` fuera de ese ciclo de vida son responsables de cerrar la sesión ellos mismos.

Una sesión que nunca se cierra mantiene su conexión JDBC subyacente retirada del pool con una transacción abierta. PostgreSQL informa esa conexión como `idle in transaction`. Si no se controla, esto bloquea el autovacuum en las tablas que tocó la transacción, provoca hinchazón de las tablas y degrada el rendimiento de la base de datos con el tiempo. Reiniciar Tomcat vacía el pool y oculta el síntoma temporalmente, por lo que la fuga subyacente puede pasar inadvertida durante un tiempo.

## Detección del problema { #detecting-the-problem }

Consulte PostgreSQL para buscar conexiones atascadas en este estado:

```sql
SELECT pid, now() - xact_start AS duration, state, LEFT(query, 80) AS query_snippet
FROM pg_stat_activity
WHERE state = 'idle in transaction';
```

Un número creciente de filas que nunca se despeja hasta que se reinicia Tomcat indica que, en algún punto del recorrido de la solicitud, no se está cerrando una sesión.

## Cómo encontrar la fuga { #finding-the-leak }

Revise los caminos de código personalizados que abren una sesión DAL o de Hibernate directamente en lugar de depender de `DalFilter`. Esto es habitual en servlets que extienden directamente `HttpServlet` o `HttpBaseServlet`, evitando la cadena de filtros estándar. Cada uno de estos caminos debe cerrar su sesión explícitamente en un bloque `finally`:

```java
try {
  // ... procesamiento de la solicitud que usa OBDal.getInstance() ...
} finally {
  OBDal.getInstance().commitAndClose();
}
```

O, cuando se usa `SessionHandler` directamente:

```java
try {
  // ... procesamiento de la solicitud ...
} finally {
  SessionHandler.getInstance().commitAndClose();
}
```

Para confirmar qué camino de código es responsable antes de cambiar nada, habilite el registro de conexiones abandonadas. Esto registra la traza de pila de dónde se tomó prestada una conexión una vez que ha estado retirada más tiempo del esperado, sin cerrar nada:

```properties title="gradle.properties"
db.pool.logAbandoned=true
db.pool.suspectTimeout=<segundos>
```

Aplique el cambio con:

```bash
./gradlew setup
```

!!! warning
    Registrar las conexiones abandonadas añade sobrecarga a cada solicitud de conexión, porque se debe generar una traza de pila. Utilícelo para diagnosticar la fuga y luego deshabilítelo una vez identificado el camino de código responsable.

## Mitigación a nivel de pool { #mitigating-at-the-pool-level }

Mientras se desarrolla e implementa la corrección de código, el pool de conexiones puede configurarse para recuperar por la fuerza las conexiones que se han retirado durante demasiado tiempo. Añada las siguientes propiedades a `gradle.properties`:

```properties title="gradle.properties"
db.pool.removeAbandoned=true
db.pool.removeAbandonedTimeout=<segundos>
```

Luego aplique el cambio:

```bash
./gradlew setup
```

Consulte [Cómo usar un pool de conexiones externo](how-to-use-an-external-connection-pool.md#pool-configuration) para ver la referencia completa de las propiedades de configuración del pool.

!!! warning
    Establezca `removeAbandonedTimeout` con un margen amplio por encima de la duración de la transacción o el proceso en segundo plano legítimo más largo del entorno. Cualquier operación que siga en ejecución más allá de ese tiempo de espera tendrá su conexión recuperada mientras está en uso, lo que corrompe esa operación. Este ajuste es una red de seguridad temporal, no un sustituto de cerrar la sesión en el código.

---

This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.
