---
tags:
    - Copilot
    - IA
    - Herramienta
    - Directorio
    - Sistema de archivos
---

# Herramienta de impresión de directorios

:octicons-package-16: Paquete Java: `com.etendoerp.copilot.toolpack`

## Visión general

La **Herramienta de impresión de directorios** es una herramienta diseñada para imprimir archivos y directorios desde el directorio actual o desde un directorio superior especificado. Permite la opción de listar el contenido de forma recursiva.

!!!info
    Para poder incluir esta funcionalidad, debe estar instalado el Copilot Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. Para más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Copilot Extensions - Notas de la versión](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).
    
Esta herramienta es extremadamente valiosa para la gestión y monitorización del sistema de archivos. Facilita la visualización de la estructura de directorios, tanto localmente como hacia niveles superiores, y permite auditorías detalladas de la estructura. Su capacidad para ignorar directorios específicos comunes en entornos de desarrollo garantiza que los listados sean relevantes y limpios, haciendo que la herramienta sea eficiente y práctica.

## Funcionalidad

Esta herramienta se utiliza cuando necesita obtener una visión clara de la estructura de archivos y directorios en un directorio específico del sistema, ya sea el directorio actual o uno de sus directorios padre. Puede ser útil para:

- Auditar y revisar la estructura de archivos.
- Automatizar operaciones que dependen de la existencia de determinados archivos.
- Obtener listados de directorios para su posterior procesamiento.

Este proceso consta de las siguientes acciones:

- **Recepción de parámetros**

    La herramienta recibe dos parámetros clave:

    - Recursive (boolean): Indica si se deben listar los subdirectorios de forma recursiva.
    - `parent_doubledot_qty` (integer): Especifica cuántos directorios padre se deben ascender desde el directorio actual.

    **Ejemplo de entrada**

    ```
    {
    "recursive": true,
    "parent_doubledot_qty": 2
    }
    ```

    Cálculo del directorio a listar:

    - Calcula la ruta del directorio en función del número de directorios padre especificado.
    - Por ejemplo, si `parent_doubledot_qty` es 2, subirá dos niveles desde el directorio actual (../../).

- **Listado de directorios**

    - Si recursive es True, utilizará `os.walk` para listar todos los archivos y subdirectorios de forma recursiva.
    - Si recursive es False, utilizará `os.listdir` para listar únicamente el contenido del directorio especificado.

- **Devolución del resultado**

    Devuelve un diccionario con la lista de archivos y directorios bajo la clave Mensaje.

## Ejemplo de uso

Si desea listar de forma recursiva los archivos y directorios en el directorio abuelo del directorio actual:

- **Entrada**
```
{ "recursive": true, "parent_doubledot_qty": 2 }
```
- **Salida**
```
{ "message": ["/path/to/parent/dir/file1", "/path/to/parent/dir/subdir/file2", ...] }
```

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.