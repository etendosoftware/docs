---
tags:
  - How to
  - Particionado
  - Database Extended
  - PostgreSQL
  - Rendimiento
  - Etendo
status: beta
---

# Cómo particionar tablas con el módulo Etendo Database Extended

## Visión general

!!!warning "MÓDULO BETA"
    El módulo Etendo Database Extended se encuentra actualmente en **BETA**. Las funcionalidades pueden cambiar sin previo aviso. No lo utilice en producción sin una validación previa.

Esta guía explica cómo particionar tablas grandes de PostgreSQL utilizando el módulo **Etendo Database Extended** (id de módulo: `com.etendoerp.db.extended`). El particionado de tablas mejora el rendimiento y el mantenimiento de tablas de alto volumen (consultas por rango más rápidas, índices más pequeños, archivado más sencillo).

Usted:

- Configurará una tabla para particionado anual por rango (mediante una columna de fecha / marca de tiempo) en el Application Dictionary (AD).
- Ejecutará el script de orquestación `migrate.py` para crear la estructura particionada y migrar los datos existentes.
- Actualizará el modelo de datos para que Etendo sea consciente de los cambios estructurales.
- (Opcional) Revertirá el particionado usando `unpartition.py` para desarrollo u operaciones de `export.database`.

## Requisitos previos

- PostgreSQL 16+
- Python 3 (disponible en el entorno)
- Etendo con DBSM 1.2.0+ configurado correctamente
- Módulo Etendo Database Extended instalado
- Capacidad para detener Tomcat temporalmente (recomendado para consistencia)

## Componentes implicados

### Application Dictionary (AD)
Ventana `Partitioned Table Config`: define la tabla objetivo y la columna de fecha/marca de tiempo utilizada como clave de particionado.

### Herramientas del módulo (Python)
- `tool/migrate.py`: orquesta la creación de particiones y la migración de datos.
- `tool/unpartition.py`: revierte una tabla particionada a una estructura plana (sin particionado) (necesario antes de ejecutar `export.database`).

### PostgreSQL
Crea la tabla padre particionada, las particiones anuales, migra los datos y vuelve a adjuntar dependencias (índices, triggers, claves foráneas, vistas).

### DBSM / Gradle
`./gradlew update.database -Dforce=yes smartbuild` alinea los metadatos del modelo de datos con la nueva estructura física tras particionar o revertir.

## Flujo de extremo a extremo (alto nivel)

```
[1] Definir en AD (tabla + columna de fecha)
        |
        v
[2] Detener Tomcat (recomendado)
        |
        v
[3] Orquestar
    $ python3 modules/com.etendoerp.db.extended/tool/migrate.py
        - Valida y prepara
        - Crea padre + particiones anuales
        - Migra datos y vuelve a adjuntar dependencias
        |
        v
[4] Actualizar modelo
    $ ./gradlew update.database -Dforce=yes smartbuild
```

Para revertir:
```
$ python3 modules/com.etendoerp.db.extended/tool/unpartition.py "table1,table2"
$ ./gradlew update.database -Dforce=yes smartbuild
```

## Funcionamiento interno de migrate.py (paso a paso)

### 1. Configuración y conexión

- Lee las credenciales de base de datos desde el entorno de Etendo.
- Lee las entradas AD de `Partitioned Table Config`.

### 2. Prevalidaciones

- Garantiza que la tabla existe y que no está ya particionada.
- Valida que la columna de particionado existe y es de tipo `date` o `timestamp`.
- Recopila objetos dependientes (índices, triggers, claves foráneas, vistas).

### 3. Preparación de tablas relacionadas (si es necesario)

- Añade columnas auxiliares de fecha faltantes en tablas relacionadas (cuando sea necesario para mantener la integridad referencial/temporal).

### 4. Transformación

- Inicia una transacción (rollback seguro en caso de fallo).
- Crea la tabla padre particionada (refleja la estructura original).
- Precrea particiones anuales RANGE (p. ej. `FOR VALUES FROM ('2023-01-01') TO ('2024-01-01')`).
- Migra los datos desde la tabla original (enrutamiento automático hacia las particiones).
- Intercambia nombres para que la nueva tabla padre conserve el nombre lógico original de la tabla.

### 5. Re-adjunción de dependencias

- Recrea índices.
- Reconstruye triggers.
- Vuelve a vincular las claves foráneas al nuevo padre.
- Garantiza que las vistas sigan siendo válidas.

### 6. Finalización

- Confirma (commit) si tiene éxito (rollback en caso contrario, se preserva la tabla original).
- Requiere: `./gradlew update.database -Dforce=yes smartbuild` posteriormente.

## Procedimiento operativo

### 1. Preparar el entorno

```bash
./gradlew update.database smartbuild
python3 -m venv modules/com.etendoerp.db.extended/.venv
source modules/com.etendoerp.db.extended/.venv/bin/activate
pip3 install pyyaml psycopg2-binary
```

### 2. Configurar la definición de particionado en AD

`Application`>`Partition`>`Partitioned Table Config`

Seleccione:
- Tabla
- Columna de fecha/marca de tiempo (alta cardinalidad, p. ej. `dateordered`, `created`)

### 3. Ejecutar el particionado

```bash
# 1) Detener Tomcat (recomendado)
# 2) Ejecutar migración
python3 modules/com.etendoerp.db.extended/tool/migrate.py
# 3) Actualizar modelo
./gradlew update.database -Dforce=yes smartbuild
```

## ModuleScript: PartitionedConstraintsHandling.java

Este ModuleScript se ejecuta durante `./gradlew update.database ...` y automatiza los ajustes de restricciones cuando una tabla se particiona o se revierte.

### Propósito

- Crea copias de seguridad de seguridad en el esquema `etarc_backups` (`<table>_backup_<timestamp>`).
- Mantiene `backup_metadata` (limpia automáticamente copias antiguas: retención ~7 días / máx. 5 por tabla).
- Reconstruye la clave primaria (PK): compuesta `(id, <partition_column>)` si está particionada; simple `id` si no lo está.
- Recrea claves foráneas (FK) en tablas hijas, añadiendo la columna auxiliar `etarc_<partition_column>__<fkname>` cuando sea necesario para referencias compuestas.

### Esquema del proceso

- Detecta el estado de particionado mediante `pg_partitioned_table`.
- Lee definiciones del modelo XML para metadatos de PK/FK.
- Realiza DROP / ADD controlado de PK y FKs.
- Añade y (cuando es posible) rellena columnas auxiliares en tablas hijas.
- Genera logs detallados y seccionados para trazabilidad.

### Señales de log a tener en cuenta

- Separadores tipo banner: `=======================================================`
- Títulos: `Partitioning process info`, `Partitioning processing summary (ms)`
- Mensajes de backup: detalles de creación y limpieza
- Mensajes de restricciones: `Recreating constraints for <table>`, `Added helper column ...`

### Problemas comunes

- Falta definición de PK en XML → verifique el XML de la entidad.
- Errores de permisos al crear el esquema `etarc_backups`.
- Nomenclatura de FK inesperada o FKs multicolumna.
- Columna auxiliar NULL (no se puede inferir) → rellénela manualmente antes de forzar la FK compuesta.

## Revertir (desparticionado)
`export.database` no soporta tablas particionadas. Revierta antes de exportar o para reinicios de desarrollo.

```bash
# Una o varias tablas (separadas por comas, sin espacios)
python3 modules/com.etendoerp.db.extended/tool/unpartition.py "c_order,c_invoice"
./gradlew update.database -Dforce=yes smartbuild
```

### Pasos internos de unpartition.py

- Crea una tabla de reemplazo sin particionado.
- Copia los datos desde el padre + particiones.
- Recrea índices / FKs / triggers.
- Elimina la jerarquía de particiones y deja una tabla plana con el nombre lógico original.

## Buenas prácticas y advertencias

- Pruebe siempre primero en preproducción (módulo BETA).
- Elija una clave de particionado con buena distribución y predicados por rango frecuentes.
- Planifique de forma proactiva la creación de futuras particiones anuales.
- Considere índices por partición (PostgreSQL no dispone de índices globales).
- Detenga Tomcat durante la transformación para evitar escrituras concurrentes.
- Mantenga nombres de FK convencionales (simplifica el reemplazo mediante scripts).
- Valide que la lógica de negocio puede inferir la clave de particionado para filas hijas.

## Lista rápida de verificación de éxito

- `\d+ <table>` en `psql` muestra `Partitioned table` con particiones anuales (p. ej. 2023, 2024 ...).
- Las consultas por rango leen menos bloques (poda de particiones visible en `EXPLAIN`).
- `./gradlew update.database -Dforce=yes smartbuild` finaliza sin errores.
- La aplicación opera de forma transparente contra el mismo nombre lógico de tabla.

## Resumen ejecutivo del flujo

1. Defina el particionado en AD (tabla + columna de fecha).
2. Ejecute `migrate.py` (valida, crea el padre, particiones anuales, migra datos, vuelve a adjuntar dependencias).
3. Ejecute `update.database` para sincronizar el modelo.
4. (Opcional) Ejecute `unpartition.py` + `update.database` para revertir.

## Consultas de verificación (ejemplos)

```sql
-- Check partitioned status
SELECT relname FROM pg_partitioned_table pt
JOIN pg_class c ON c.oid = pt.partrelid
WHERE relname = 'c_order';

-- List partitions
SELECT inhrelid::regclass AS partition
FROM pg_inherits WHERE inhparent = 'c_order'::regclass
ORDER BY 1;

-- Explain pruning
EXPLAIN ANALYZE SELECT * FROM c_order WHERE dateordered >= '2024-01-01' AND dateordered < '2024-07-01';
```

## Documentación relacionada

- [Módulo Etendo Database Extended Module](../developer-tools/etendo-database-extended-module.md)

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.