---
tags:
  - Cómo hacer
  - Exportar datos de ejemplo
  - Extensiones
  - Etendo Classic
---

# Cómo exportar datos de ejemplo

## Visión general

El objetivo de este documento es explicar cómo se exportan los datos de ejemplo de Etendo utilizando la tarea `export.sample.data`.

## Conjunto de datos de datos de ejemplo

Las tablas que se exportarán cuando se ejecute la tarea `export.sample.data` están incluidas en el conjunto de datos Definición de cliente. Puede leer más sobre los conjuntos de datos en [Conjunto de datos](../concepts/datasets.md).

!!!note 
    La forma en que funciona actualmente la tarea `export.sample.data`, la cláusula SQL Where definida en las tablas del conjunto de datos del conjunto de datos Definición de cliente se ignorará y se reemplazará por un filtro de cliente.

## Exportación de los datos de ejemplo

Para exportar los datos de ejemplo de un cliente determinado, debe ejecutarse esta tarea de gradle `export.sample.data`, disponible desde la carpeta raíz de Etendo. Tiene los siguientes parámetros:

  * Cliente: El nombre del cliente cuyos datos de ejemplo se exportarán.
  * Módulo: El módulo donde se exportarán los datos de ejemplo. Los datos de ejemplo exportados se almacenarán en la carpeta referencedata/sampledata/clientName relativa a la ruta del módulo. Para exportar a la carpeta de datos de ejemplo del core, debe especificarse 'org.openbravo' en el parámetro de cliente.
  * FormatoDeExportación (opcional): Se utiliza para especificar el formato de exportación de los datos de ejemplo. Actualmente hay dos formatos de exportación disponibles: xml (el predeterminado) y copy. El formato de exportación copy solo estará disponible al exportar los datos de ejemplo desde una base de datos PostgreSQL. Los datos de ejemplo exportados con el formato copy solo pueden importarse en bases de datos PostgreSQL. Si se utiliza el parámetro copy en un entorno Oracle, se mostrará un mensaje de advertencia y se utilizará el formato xml en su lugar.

Por ejemplo, para exportar los datos de ejemplo del cliente 'F&B International Group' al core utilizando el formato COPY, debe utilizarse el siguiente comando:

```bash title="Terminal"
./gradlew export.sample.data -Dclient="F&B International Group" -Dmodule=org.openbravo -DexportFormat=copy
```

Para obtener información más detallada, visite [Exportación de datos de ejemplo de QA](../how-to-guides/QA-sampledata-export.md).

---

Este trabajo es una obra derivada de [Cómo exportar datos de ejemplo](http://wiki.openbravo.com/wiki/How_to_export_sample_data){target="\_blank"} de [Wiki de Openbravo](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizado bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.