---
title: Mejoras de la interfaz de usuario
tags:
    - Nueva UI
    - Mejoras
status: new
---

# Mejoras de la interfaz de usuario

## Visión general

Esta sección detalla las mejoras de la interfaz de usuario disponibles en la **Nueva UI de Etendo**.

## Mejoras y ampliaciones de la UI de Etendo

### Formato regional de fechas

Todas las fechas mostradas en la interfaz de usuario ahora se adaptan automáticamente a la configuración regional de tu navegador. Esto proporciona una vista personalizada y localizada de la información de fechas, haciendo la interfaz más intuitiva y fácil de leer para usuarios de distintas regiones.

!!! warning

    Este formato regional se aplica exclusivamente a la capa de visualización de la interfaz de usuario. El procesamiento de datos subyacente sigue estas reglas:

    - **Visualización/Vista:** las fechas se formatean según la configuración regional de tu navegador
    - **Operaciones de backend:** los valores de fecha se procesan y almacenan usando la configuración especificada en `gradle.properties`
    - **Las fechas se muestran automáticamente en tu formato regional preferido** sin configuración manual.

**Ejemplo UI clásica de Etendo**

<figure markdown="span">
    ![Formato de fecha en Etendo Classic](../../assets/user-guide/newui/classic-date-1.png)
    <figcaption>UI clásica de Etendo: las fechas en la UI clásica de Etendo se muestran en el formato estándar configurado en el sistema.
    </figcaption>
</figure>

**Ejemplo UI de Etendo con configuración regional (en-US):**

<figure markdown="span">
    ![Formato de fecha en la nueva UI con configuración regional](../../assets/user-guide/newui/newui-date-1.png)
    <figcaption>UI de Etendo: en la UI de Etendo la misma tabla muestra las fechas formateadas automáticamente. En este ejemplo se aplica `en-US` (Estados Unidos), por lo que las fechas aparecen en formato `MM/DD/YYYY`. </figcaption>
</figure>

### Gestión de adjuntos

La **UI de Etendo** incorpora un sistema de gestión de adjuntos completamente rediseñado que proporciona una forma más ágil, visual y completa de gestionar archivos adjuntos, tanto desde la **vista de formulario** como directamente desde los **registros de la rejilla**.

#### Sección de adjuntos en la vista de formulario

La sección de adjuntos se ha rediseñado para ser más intuitiva. Ahora los archivos se muestran como etiquetas o chips, lo que permite una identificación rápida.

![Sección de adjuntos expandida](../../assets/user-guide/newui/attachment-section-expanded-1.png)

**Subida de archivos**

![Vista previa del modal de subida](../../assets/user-guide/newui/upload-modal-preview-1.png){align=right width=300}

Hay dos formas principales de subir archivos dentro de un registro:

1. **Arrastrar y soltar:** arrastra uno o varios archivos directamente desde tu equipo a la **zona de soltado** punteada en la sección de adjuntos.

    !!! note
        Al soltar el archivo, se abrirá un modal de confirmación donde podrás verificar el archivo seleccionado y añadir una descripción opcional antes de subirlo.

2. **Explorador de archivos:** haz clic en la zona de subida (o en el icono de subida) para abrir el selector de archivos de tu sistema operativo.

#### Vista previa y edición rápida

![Modal de subida con archivo](../../assets/user-guide/newui/upload-modal-with-file-1.png){align=right width=300}

Al hacer clic en el nombre de cualquier adjunto subido se abrirá una ventana de vista previa avanzada.

**Funcionalidades dentro de la vista previa:**

- **Visor integrado:** visualiza imágenes y documentos PDF directamente sin necesidad de descargarlos.
- **Edición de la descripción:** puedes modificar la descripción del archivo _in situ_. Haz clic en el icono de **Lápiz**, edita el texto y guarda los cambios con el icono de **Comprobación**, todo sin salir de la vista previa.
- **Gestión individual:** botones dedicados para **Descargar** o **Eliminar** el archivo que estás visualizando.

#### Acciones masivas de adjuntos

![Acciones masivas](../../assets/user-guide/newui/bulk-actions-1.png)

Para facilitar la gestión de múltiples archivos, se han incorporado botones de acción global en la cabecera de la sección de adjuntos:

- **Descargar todo:** genera y descarga un archivo comprimido (`.zip`) que contiene todos los adjuntos asociados al registro.
- **Eliminar todo:** permite eliminar todos los adjuntos del registro en un solo paso (requiere confirmación de seguridad).

#### Subida rápida desde la rejilla (arrastrar y soltar en filas)

Es posible adjuntar archivos sin necesidad de entrar en cada registro. Desde la vista principal de la rejilla:

![](../../assets/user-guide/newui/drop-file-in-grid-1.gif)

### Filtros avanzados

![](../../assets/user-guide/newui/advanced-filters-modal.png)

El modal de **Filtros avanzados** es un potente componente de filtrado que permite a los usuarios crear filtros complejos, con múltiples condiciones, directamente desde la interfaz de la rejilla. Proporciona una forma intuitiva de construir consultas sofisticadas usando operadores lógicos y múltiples grupos de filtros.

!!! info "Características clave"
    - **Múltiples tipos de filtro:** soporte para campos de tipo texto, número, fecha, booleano y selección.
    - **Operadores lógicos:** combina condiciones usando operadores AND/OR.
    - **Grupos de filtros:** anida múltiples condiciones dentro de grupos para una lógica de consulta compleja.
    - **Operadores dinámicos:** los operadores disponibles cambian según el tipo de campo seleccionado.
    - **Añadir/Quitar condiciones:** añade o elimina dinámicamente condiciones de filtro individuales.
    - **Añadir/Quitar grupos:** crea grupos de filtros anidados para organizar lógica compleja.
    - **Limpiar todo:** restablece todos los filtros para empezar de nuevo.
    - **Aplicar/Validación:** solo se aplican condiciones válidas (con columna, operador y valor).

#### Operadores compatibles por tipo de campo

| Tipo de campo | Operadores compatibles |
|-----------|---------------------|
| **Texto** | - `=` Igual<br> - `≠` Distinto<br>Contiene<br>No contiene<br>Empieza por<br>Termina en<br>Está vacío<br>No está vacío |
| **Número** | `=` Igual<br>`≠` Distinto<br>`>` Mayor que<br>`<` Menor que<br>`≥` Mayor o igual<br>`≤` Menor o igual |
| **Fecha** | `=` Igual<br>`≠` Distinto<br>Antes de<br>Después de<br>Hoy<br>Esta semana<br>Este mes |
| **Booleano** | sí<br>no |
| **Selección (desplegable)** | `=` Igual<br>`≠` Distinto |

#### Uso de los filtros avanzados

1. **Haz clic en el icono de filtro** en la cabecera de la rejilla para abrir el modal de Filtros avanzados.
2. **Selecciona una columna** en el desplegable de la primera fila de filtro.
3. **Elige un operador** adecuado para el tipo de campo.
4. **Introduce o selecciona un valor** según el tipo de operador.
5. **Añade más condiciones** haciendo clic en el botón *Añadir condición*.
6. **Crea grupos de filtros** para lógica compleja usando el botón *Añadir grupo*.
7. **Revisa tus filtros**: el estado muestra el número de filtros activos.
8. **Haz clic en el botón Aplicar filtros** para ejecutar la consulta.
9. **Limpia los filtros** haciendo clic en el botón *Limpiar todo* para restablecer y empezar de nuevo.

#### Escenarios de ejemplo

<figure markdown="span">
    ![Ejemplo 1 de filtros avanzados](../../assets/user-guide/newui/advanced-filters-modal-1-example.png)
    <figcaption>Ejemplo 1: filtro simple con una condición seleccionando una organización específica.</figcaption>
</figure>

<figure markdown="span">
    ![Ejemplo 2 de filtros avanzados](../../assets/user-guide/newui/advanced-filters-modal-2-example.png)
    <figcaption>Ejemplo 2: múltiples condiciones combinadas con lógica AND para acotar los resultados de búsqueda.</figcaption>
</figure>

<figure markdown="span">
    ![Ejemplo 3 de filtros avanzados](../../assets/user-guide/newui/advanced-filters-modal-3-example.png)
    <figcaption>Ejemplo 3: filtro complejo con una condición agrupada. El filtro principal comprueba si el estado del documento es contabilizado, Y el grupo comprueba si el importe bruto total es mayor que 10 Y menor que 100.</figcaption>
</figure>

---

Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"} por [Futit Services S.L](https://etendo.software){target="\_blank"}.