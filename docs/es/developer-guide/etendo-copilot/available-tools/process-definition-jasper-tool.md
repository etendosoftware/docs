---
tags:
    - Copilot
    - Informe Jasper
    - Diccionario de Aplicación de Etendo
    - Informes
---

# Herramienta Jasper

:octicons-package-16: Paquete Java: `com.etendoerp.copilot.devassistant`

## Visión general

La Herramienta Jasper permite a los desarrolladores crear definiciones de proceso para **Informe Jasper** directamente en el **Diccionario de Aplicación de Etendo**. Simplifica la integración de capacidades de informes automatizando la configuración de atributos clave y parámetros necesarios para procesos basados en Jasper.

!!!info
    Esta herramienta es especialmente útil al automatizar o configurar informes como parte de la instalación de módulos o de scripts de despliegue.

## Funcionalidad

Esta herramienta automatiza la creación de **Definición del Proceso** para informes Jasper en Etendo. Utiliza los metadatos proporcionados (clave de búsqueda, ruta del informe, parámetros, etc.) y envía la solicitud API correspondiente a Etendo para registrar el nuevo proceso de informe.

### Capacidades clave:

- Añade una nueva entrada de informe Jasper al Diccionario de Aplicación.
- Admite cadenas de parámetros delimitadas por punto y coma para facilitar la configuración por lotes.
- Da formato automáticamente a la clave de búsqueda y recorta la ruta del informe.
- Utiliza un webhook para registrar la definición del proceso.

### Parámetros

| Nombre           | Tipo   | Descripción |
|------------------|--------|-------------|
| `i_prefix`       | string | Prefijo del módulo en la base de datos. |
| `i_searchkey`    | string | Clave de búsqueda de la definición del proceso. |
| `i_report_name`  | string | Nombre del informe de fácil uso para el usuario. |
| `i_help_comment` | string | Comentario de ayuda opcional para el informe. |
| `i_description`  | string | Descripción opcional del informe. |
| `i_parameters`   | string | Lista de parámetros separados por punto y coma usando el formato: `BD_NAME-NAME-LENGTH-SEQNO-REFERENCE`. |
| `i_report_path`  | string | Ruta al informe almacenado, truncada después de `/web/` para referencia interna. |

## Ejemplo de uso

Desea registrar un informe Jasper llamado `Sales Overview` con los siguientes datos:

- Prefijo: `SALES`
- Clave de búsqueda: `Overview`
- Parámetros:  
  ```
  C_BPARTNER_ID-Business Partner-32-10-30;DATEFROM-Start Date-10-20-15;DATETO-End Date-10-30-15
  ```
- Ruta del informe: `/opt/etendo/modules/com.etendoerp.sales/web/jasper/sales_overview.jrxml`

```json title="Input"
{
  "i_prefix": "SALES",
  "i_searchkey": "Overview",
  "i_report_name": "Sales Overview",
  "i_help_comment": "Generates a report for all sales per customer.",
  "i_description": "This report provides summarized sales per partner.",
  "i_parameters": "C_BPARTNER_ID-Business Partner-32-10-30;DATEFROM-Start Date-10-20-15;DATETO-End Date-10-30-15",
  "i_report_path": "/opt/etendo/modules/com.etendoerp.sales/web/jasper/sales_overview.jrxml"
}
```

## Resultado

La herramienta:

- Dará formato a la clave de búsqueda como `SALES_Overview`
- Analizará y estructurará los parámetros proporcionados
- Truncará la ruta a: `web/jasper/sales_overview.jrxml`
- Llamará al webhook `ProcessDefinitionJasper` con la carga útil procesada

!!!note
    Asegúrese de que la ruta proporcionada contenga `/web/` en algún punto para que pueda truncarse correctamente para Etendo.

---
Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L](https://etendo.software){target="_blank"}.