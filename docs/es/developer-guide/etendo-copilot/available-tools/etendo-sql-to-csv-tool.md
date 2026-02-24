---
tags:
    - Copilot
    - Tool
    - SQL
    - CSV
    - Database
    - Etendo
---

# Herramienta de Etendo de SQL a CSV

:octicons-package-16: Javapackage: `com.etendoerp.copilot.toolpack`

## Visión general

La **Herramienta de Etendo de SQL a CSV** es una herramienta especializada para ejecutar consultas SQL en la base de datos de Etendo y convertir los resultados a formato CSV. Se conecta a Etendo mediante el webhook DBQueryExec, ejecuta consultas SELECT de forma segura y exporta los resultados JSON como archivos CSV para facilitar el análisis de datos y la elaboración de informes.

!!!info
    Para poder incluir esta funcionalidad, debe estar instalado el bundle Copilot Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. Para obtener más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Copilot Extensions - Notas de la versión](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

## Funcionalidad

Esta herramienta es esencial para tareas de extracción de datos, elaboración de informes y análisis dentro de Etendo. Proporciona una forma segura y estandarizada de consultar la base de datos y exportar resultados. La herramienta gestiona:

- **Integración con la base de datos**: se conecta a la base de datos de Etendo mediante el webhook seguro DBQueryExec
- **Ejecución de consultas**: ejecuta sentencias SELECT con validación de seguridad automática
- **Exportación de datos**: convierte resultados JSON a formato CSV para facilitar la manipulación de datos
- **Aplicación de seguridad**: solo permite consultas SELECT y valida los alias de tablas por seguridad
- **Gestión de autenticación**: gestiona automáticamente la autenticación y la configuración del host

El uso de esta herramienta consta de las siguientes acciones:

- **Parámetros de procesamiento**

    Toma los siguientes parámetros de entrada:

    - `sql_query`: la consulta SELECT que se va a ejecutar (obligatorio, debe incluir alias de tablas)
    - `output_file`: ruta donde guardar el archivo CSV (opcional, crea un archivo temporal si no se especifica)
    - `include_headers`: si se deben incluir los encabezados de columna en la salida CSV (opcional, por defecto: true)

- **Validación de consultas**

    La herramienta valida la consulta SQL por seguridad:

    - Solo se permiten sentencias SELECT
    - Se bloquean palabras clave peligrosas (DROP, DELETE, UPDATE, etc.)
    - Debe cumplir el requisito de Etendo de que todas las tablas tengan alias

- **Ejecución en base de datos**

    Se conecta a Etendo usando el webhook DBQueryExec:

    - Recupera automáticamente el token de autenticación y la configuración del host
    - Ejecuta la consulta con los filtros de seguridad integrados de Etendo
    - Devuelve datos JSON estructurados con columnas y filas

- **Conversión a CSV**

    Convierte la respuesta JSON a formato CSV:

    - Extrae los nombres de columnas y las filas de datos de la respuesta del webhook
    - Gestiona la inclusión opcional de encabezados
    - Escribe el archivo CSV con la codificación adecuada (UTF-8)

- **Informe de resultados**
    Devuelve información detallada sobre la operación:

    ```
    ✅ SQL query executed successfully!
    📊 Result: 150 rows exported
    📁 CSV file saved at: /tmp/etendo_query_result_12345.csv
    📏 File size: 0.25 MB
    🔗 Webhook: DBQueryExec
    🔍 Query: SELECT u.name, u.email FROM ad_user u WHERE...
    ```

## Funcionalidades de seguridad

La Herramienta de Etendo de SQL a CSV implementa múltiples capas de seguridad:

- **Restricción de consultas**: solo se permiten sentencias SELECT, evitando la modificación de datos
- **Filtrado de palabras clave**: bloquea palabras clave y operaciones SQL peligrosas
- **Requisito de alias**: aplica el requisito de seguridad de Etendo para los alias de tablas
- **Autenticación automática**: utiliza autenticación segura basada en token mediante el contexto de Copilot
- **Seguridad del lado del servidor**: aprovecha los controles de acceso y los filtros de datos integrados de Etendo

## Requisitos de consultas SQL

Todas las consultas SQL deben seguir los estándares de seguridad de Etendo:

### Formato requerido

- **Solo SELECT**: solo se permiten sentencias SELECT
- **Alias de tablas**: todas las tablas deben tener alias (p. ej., `FROM ad_user u`, no `FROM ad_user`)
- **Tablas accesibles**: solo se pueden consultar las tablas accesibles para el usuario actual
- **Filtros de seguridad**: Etendo aplica automáticamente filtros de seguridad de organización y cliente

### Ejemplos de consultas válidas

```sql
-- Query active users
SELECT u.name, u.email, u.created 
FROM ad_user u 
WHERE u.isactive = 'Y'

-- Query business partners with contact information
SELECT bp.name as business_partner, bp.taxid, l.phone, l.email
FROM c_bpartner bp
LEFT JOIN c_bpartner_location bpl ON bp.c_bpartner_id = bpl.c_bpartner_id
LEFT JOIN c_location l ON bpl.c_location_id = l.c_location_id
WHERE bp.iscustomer = 'Y'

-- Query sales orders with details
SELECT so.documentno, so.dateordered, so.grandtotal, bp.name as customer
FROM c_order so
JOIN c_bpartner bp ON so.c_bpartner_id = bp.c_bpartner_id
WHERE so.issotrx = 'Y' 
  AND so.docstatus = 'CO'
```

### Ejemplos de consultas no válidas

```sql
-- Missing table alias
SELECT name FROM ad_user WHERE isactive = 'Y'

-- Non-SELECT operation
UPDATE ad_user SET isactive = 'N' WHERE ad_user_id = '123'

-- Dangerous keywords
DROP TABLE temp_table
```

## Ejemplo de uso

Imagine que queremos exportar usuarios activos con sus roles a un archivo CSV para su análisis. Nuestros parámetros serían:

- **sql_query**: `SELECT u.name, u.email, r.name as role FROM ad_user u JOIN ad_user_roles ur ON u.ad_user_id = ur.ad_user_id JOIN ad_role r ON ur.ad_role_id = r.ad_role_id WHERE u.isactive = 'Y'`
- **output_file**: `/tmp/active_users_with_roles.csv`
- **include_headers**: true

La Herramienta de Etendo de SQL a CSV:

1. Validará que la consulta cumple los requisitos de seguridad
2. Ejecutará la consulta mediante el webhook DBQueryExec
3. Convertirá los resultados JSON a formato CSV
4. Guardará el archivo incluyendo los encabezados
5. Devolverá un mensaje de éxito con los detalles de la operación

## Gestión de errores

La herramienta proporciona una gestión de errores completa para escenarios habituales:

- **SQL no válido**: devuelve mensajes de error detallados para infracciones de sintaxis o seguridad
- **Problemas de conexión**: informa de problemas de autenticación o de red con el webhook
- **Errores de permisos**: indica cuándo las tablas o los datos no son accesibles para el usuario
- **Problemas del sistema de archivos**: informa de problemas al crear o escribir el archivo CSV
- **Resultados vacíos**: gestiona de forma adecuada las consultas que no devuelven datos