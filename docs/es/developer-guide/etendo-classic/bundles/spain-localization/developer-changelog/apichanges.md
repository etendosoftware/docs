---
tags:
    - API Changes
    - Etendo 26
    - Etendo 25
    - Migrate to Etendo 25
    - Spain Localization
    - Update Etendo
    - Updating Guide
    - Developer Changelog
---

# Documentación de Cambios de API

## Resumen

Este documento explica todos los cambios ocurridos en la API pública de los módulos contenidos en el bundle de Localización Española.

Estos cambios representan un riesgo potencial de rotura de módulos, por lo que todos han sido revisados y aprobados explícitamente. Cada vez que se produzca un nuevo cambio, será incluido en esta lista. Antes de actualizar un entorno, se recomienda revisar también la guía oficial de actualización: [Actualizar Etendo a Cualquier Versión](../../../getting-started/upgrade/upgrade-etendo-to-any-version.md).

Los cambios se agrupan por **versión del bundle** de Localización Española y, dentro de cada versión, por **tipo de cambio**.

## 4.x

### Eliminación del "Destino" de TicketBAI (reemplazado por el "Territorio" de sif.general)

*Versión del bundle: [4.4.0](https://github.com/etendosoftware/com.etendoerp.localization.spain.extensions/releases/tag/4.4.0){target="_blank"} · Módulos: `com.smf.ticketbai`, `com.etendoerp.sif.general` · Riesgo: Medio*

El campo/tabla **Destino** de TicketBAI (Gipuzkoa / Bizkaia / Álava), que resolvía las URLs y *endpoints* de cada hacienda foral, ha sido **eliminado**. TicketBAI resuelve ahora el territorio a través del campo **Territorio** del módulo `com.etendoerp.sif.general`, que se apoya en el catálogo centralizado de *endpoints* `ETSG_SIF_Channel_Endpoint` compartido por SII, TicketBAI y Verifactu.

**Tablas Eliminadas**

Se ha eliminado por completo la siguiente tabla, junto con todas sus columnas, pestañas y entradas del Diccionario de Aplicación. Cualquier módulo personalizado que consulte o referencie directamente esta entidad Hibernate debe actualizarse:

| Tabla | Clase Entidad Hibernate | Descripción |
|---|---|---|
| `TBAI_Destiny_Config` | `TbaiDestinyConfig` | Configuración por destino de TicketBAI (URLs de alta/anulación/QR, licencia, NIF del desarrollador, URIs de esquema, etc.) |

**Columnas Eliminadas**

| Tabla | Columna | Descripción |
|---|---|---|
| `TBAI_Config` | `Tbai_Destiny_Config_ID` | Referencia (FK `TBAI_CONFIG_DESTINY_CONFIG_ID`) al destino de TicketBAI. Sustituida por el campo Territorio. |

**Columna Nueva (reemplazo)**

| Tabla | Columna | Entidad / Propiedad Hibernate | Descripción |
|---|---|---|---|
| `TBAI_Config` | `ETSG_SIF_Territory` | `TBAI_Config` / `eTSGSIFTerritory` | Territorio SIF (lista: `GIPUZKOA`, `BIZKAIA`, `ARABA`). Referencia de lista "Territorio SIF" definida en `com.etendoerp.sif.general`. |
| `ETSG_SIF_Channel_Endpoint` | `Territory` | `SifChannelEndpoint` | Catálogo centralizado de *endpoints* por territorio (en `com.etendoerp.sif.general`), contra el que TicketBAI resuelve ahora sus URLs. |

!!! warning "Acción Requerida para Desarrollos Personalizados"
    Los módulos o reportes personalizados que referencien la tabla/columna eliminada del destino de TicketBAI (`TBAI_Destiny_Config`, `TbaiDestinyConfig`, `TBAI_Config.Tbai_Destiny_Config_ID`) deben actualizarse para leer el territorio desde el campo `ETSG_SIF_Territory` de `com.etendoerp.sif.general` (y, si resuelven *endpoints*, contra la tabla `ETSG_SIF_Channel_Endpoint`) **antes** de la actualización.

## 3.x

### Flujo unificado de carga de certificado digital

*Versión del bundle: [3.13.0](https://github.com/etendosoftware/com.etendoerp.localization.spain.extensions/releases/tag/3.13.0){target="_blank"} · Módulos: `com.etendoerp.sif.general`, `com.etendoerp.verifactu`, `com.smf.ticketbai`, `org.openbravo.module.sii` · Riesgo: Bajo*

Verifactu, SII y TicketBAI ahora utilizan la misma funcionalidad para cargar un Certificado Digital desde la ventana de Organización, usando el proceso "Añadir Certificado Digital" en la organización legal deseada.

### Unificación del campo "Fecha de Operación"

*Versión del bundle: [3.9.0](https://github.com/etendosoftware/com.etendoerp.localization.spain.extensions/releases/tag/3.9.0){target="_blank"} · Módulos: `com.etendoerp.sif.general`, `com.etendoerp.verifactu`, `com.smf.ticketbai`, `org.openbravo.module.sii` · Riesgo: Medio*

Cada sistema de facturación disponía de su propia columna de **Fecha de Operación** en la factura. Estas columnas se han **deprecado** en favor de una única columna unificada `EM_Etsg_Date_Operation`, definida en `com.etendoerp.sif.general` y utilizada por Verifactu, TicketBAI y SII.

!!! note "Deprecadas, no eliminadas"
    Las columnas antiguas **no se eliminan** de la base de datos: siguen presentes y activas, conservando sus datos. Sin embargo, **dejan de ser la fuente de verdad**: la nueva lógica escribe y lee únicamente en `EM_Etsg_Date_Operation`, por lo que las columnas antiguas ya no se pueblan para las facturas nuevas.

**Columnas Deprecadas**

| Tabla | Columna | Entidad / Propiedad Hibernate | Módulo |
|---|---|---|---|
| `C_Invoice` | `EM_Etvfac_Date_Operation` | `Invoice` / `eTVFACDateOperation` | com.etendoerp.verifactu |
| `C_Invoice` | `EM_Tbai_Date_Operation` | `Invoice` / `tbaiDateOperation` | com.smf.ticketbai |
| `C_Invoice` (y `C_Order`) | `EM_Aeatsii_Fecha_Operacion` | `Invoice` / `aeatsiiFechaOperacion` (y `Order`) | org.openbravo.module.sii |

**Columna Nueva (reemplazo)**

| Tabla | Columna | Entidad / Propiedad Hibernate | Descripción |
|---|---|---|---|
| `C_Invoice` | `EM_Etsg_Date_Operation` | `Invoice` / `eTSGDateOperation` (`Invoice.PROPERTY_ETSGDATEOPERATION`) | Fecha de Operación unificada (en `com.etendoerp.sif.general`). Valor por defecto `@DateInvoiced@`. |

!!! note "SII en pedidos"
    La columna `EM_Aeatsii_Fecha_Operacion` de SII existe también en la tabla `C_Order`. La columna unificada **solo** se define en `C_Invoice`; **no** existe un equivalente unificado en `C_Order`, por lo que el uso de la Fecha de Operación de SII en pedidos permanece inalterado.

Para poblar la nueva columna con los valores de las columnas antiguas en facturas previas a la actualización, se dispone del proceso **Rellenar Fechas de Operación** (ver la sección [Rellenar Fechas de Operación](../../../../../user-guide/etendo-classic/optional-features/bundles/spain-localization/funcionalidades-generales-para-sifs.md#rellenar-fechas-de-operacion) de la guía de usuario). La copia es solo hacia adelante (no sobrescribe valores ya informados), por lo que **no hay pérdida de datos**.

!!! warning "Acción Requerida para Desarrollos Personalizados"
    Los módulos, reportes o consultas personalizados que lean las columnas/propiedades antiguas (`EM_Etvfac_Date_Operation` / `eTVFACDateOperation`, `EM_Tbai_Date_Operation` / `tbaiDateOperation`, `EM_Aeatsii_Fecha_Operacion` / `aeatsiiFechaOperacion`) deben actualizarse para leer la Fecha de Operación desde `EM_Etsg_Date_Operation` (`Invoice.PROPERTY_ETSGDATEOPERATION`) **antes** de la actualización. Aunque las columnas antiguas siguen existiendo, ya no se pueblan para las facturas nuevas, por lo que el código que dependa de ellas verá valores vacíos o desactualizados.

---

This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.
