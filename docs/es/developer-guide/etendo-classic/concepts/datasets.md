---
title: Conjunto de datos
tags:
  - Conceptos
  - Conjunto de datos
  - Tabla del Conjunto de Datos
  - Datos de Referencia
  - Objetos de Negocio
---

# Conjunto de datos
  
## Visión general

El concepto de Conjunto de datos le permite definir **conjuntos de datos** de diferentes tablas y exportar estos datos en un solo paso. Los conjuntos de datos son especialmente útiles para gestionar datos de referencia de un módulo, por ejemplo tipos impositivos o datos por defecto en nuevas tablas añadidas por un módulo. Los datos de referencia se publican, distribuyen e instalan junto con el código del programa que implementa el módulo.

El contenido de un Conjunto de datos se define mediante sus **Tabla del Conjunto de Datos** y **Columna del Conjunto de Datos**. La primera define qué tablas se exportan; la segunda, qué columnas de esas tablas se exportan.

Los conjuntos de datos pueden definirse a nivel de **Sistema, Organización o Entidad/Organización**. Los conjuntos de datos a nivel de sistema se aplican cuando el módulo que los contiene se instala en el sistema. Sus datos son a nivel de sistema.

- Los conjuntos de datos a nivel de organización pueden aplicarse en [Crear organización](../../../user-guide/etendo-classic/basic-features/general-setup/enterprise-model/initial-organization-setup.md) (al crear una nueva organización) o también pueden aplicarse a una organización existente usando la ventana **Gestión del módulo de Empresa**. Contienen **información a nivel de organización**.
- Los conjuntos de datos a nivel de entidad/organización funcionan como los conjuntos de datos a nivel de organización, pero también pueden aplicarse en [Crear entidad](../../../developer-guide/etendo-classic/how-to-guides/how-to-run-an-initial-client-setup-process.md) al crear una nueva entidad. Contienen **información a nivel de organización/entidad**.

## Ventana Conjunto de datos

:material-menu: `Aplicación` > `Diccionario de la Aplicación` > `Conjunto de datos`

Un Conjunto de datos es una agrupación de diferentes tablas (entidades) que se exportan conjuntamente. Los conjuntos de datos se definen mediante la ventana **Conjunto de datos**. A continuación se muestra un ejemplo de un Conjunto de datos.

![](../../../assets/developer-guide/etendo-classic/concepts/datasets-0.png)

  
Algunas cosas importantes a tener en cuenta:

  * Un **Conjunto de datos** pertenece a un módulo, por lo que los módulos pueden añadir nuevos conjuntos de datos a una instancia de Etendo. 
  * **Acceso datos**: filtra las tablas que pueden seleccionarse para este conjunto de datos; solo las tablas con el nivel de acceso de datos establecido pueden incluirse en el conjunto de datos.
 

Si la columna **Permitir exportar** está marcada, entonces se muestra un botón **Exportar Datos de Referencia**. Al hacer clic en este botón, los datos se exportan al directorio de módulos del módulo al que pertenece el Conjunto de datos:

```
modules
└── org.openbravo.localization.spain.referencedata.taxes
    └── referencedata 
        └── standard
            ├── Impuestos_ES.xml
            └── Spanish_Tax_Alerts.xml
```

### Solapa Tabla

La solapa Tabla define qué datos de **una tabla se van a exportar**. Define tanto los registros (mediante una cláusula where) como las columnas por registro.

!!!note
    Un Conjunto de datos debe tener una o más Tablas del Conjunto de Datos; una Tabla del Conjunto de Datos siempre pertenece exactamente a un Conjunto de datos.

![](../../../assets/developer-guide/etendo-classic/concepts/dataset-2.png)


Algunos aspectos importantes:

- Una Tabla del Conjunto de Datos tiene un módulo, por lo que el usuario puede añadir una nueva Tabla del Conjunto de Datos a un Conjunto de datos existente (de otro módulo).
- La cláusula where HQL es una cláusula where [HQL](https://docs.jboss.org/hibernate/core/3.6/reference/en-US/html/queryhql.html){target="_blank"}. Las propiedades que pueden utilizarse en la cláusula son las propiedades de la **entidad** de la tabla de la DatasetTable.
- **Incluir Todas las Columnas**: si está marcada, se exportan todas las columnas, excepto las excluidas en la Columna del Conjunto de Datos; si no está marcada, entonces se utiliza la definición de la solapa Columna.
- **Excluir Información de Auditoría**: solo es relevante si está marcada Incluir Todas las Columnas; en ese caso, este campo puede utilizarse para excluir la información de auditoría. En la mayoría de situaciones, *tiene sentido activar este indicador*, ya que la información de auditoría (información sobre qué usuario creó y actualizó cada registro, y en qué fecha ocurrió) la mayoría de las veces es irrelevante al exportar datos de negocio a un conjunto de datos que pretende ser genérico y utilizarse en varios sistemas diferentes.
- **Es Objeto de Negocio**: si está marcada, entonces también se exportan los **registros hijo** de la tabla; por ejemplo, si la Tabla se define para la tabla `C_Order` y este campo está marcado, entonces también se exportan los `C_OrderLines` relacionados.
  
!!!info
    Para más información sobre cómo se definen las estructuras, consulte [Objeto de Negocio](../concepts/data-access-layer.md#business-object). 

**Cláusula where de la tabla**

Para seleccionar objetos específicos de la tabla que se incluirán en el conjunto de datos, es posible definir una **cláusula where en la DatasetTable**. La cláusula where HQL es una cláusula where [HQL](https://docs.jboss.org/hibernate/core/3.6/reference/en-US/html/queryhql.html){target="_blank"}. Las propiedades que pueden utilizarse en la cláusula son las propiedades de la **entidad** de la tabla de la DatasetTable. Los nombres de entidad y propiedad ofrecen una visión general de todas las propiedades por su entidad. Hay dos parámetros estándar que pueden utilizarse en la cláusula HQL:

  * `ClientID`: indica la entidad actual del usuario que exporta los datos. 
  * `moduleid`: el id del módulo para el que se exportan los datos. 

La sintaxis para utilizar estos parámetros en la cláusula where es la misma que para los parámetros con nombre en HQL en general.

A continuación se muestran algunos ejemplos de cláusulas where:

  * `client.id = :ClientID`, exporta todos los objetos de la entidad actual 
  * `client.id = '0'`, exporta solo los objetos de la entidad '0' 
  * `processed = true and chargeAmount > 0`, exporta solo los objetos que han sido procesados y para los que el importe del cargo > 0 
  * `client.id in ('0', '1000000')`, selecciona todos los objetos con una entidad '0' o '1000000' 
  * `name like '%Product%'`, selecciona objetos con un nombre que contiene la cadena Product 

!!!info
    La cláusula puede contener selecciones internas y otras funcionalidades HQL más avanzadas. Sin embargo, **no se admiten las cláusulas order-by, group-by y having**, por lo que el contenido de este campo debe ser solo la cláusula where y nada más.

### Solapa Columnas

La Columna del Conjunto de Datos define las **columnas/propiedades** que se exportan para un determinado objeto de negocio. Una Columna del Conjunto de Datos siempre pertenece a una Tabla del Conjunto de Datos, y una Tabla del Conjunto de Datos puede tener cero o más Columnas del Conjunto de Datos.
El concepto de Columna del Conjunto de Datos puede utilizarse de dos maneras:

  * Marque **Incluir Todas las Columnas** en la Tabla del Conjunto de Datos y defina exclusiones en la Columna del Conjunto de Datos. 
  * No marque **Incluir Todas las Columnas** en la Tabla del Conjunto de Datos y defina las Columnas exactas a exportar en la Columna del Conjunto de Datos.

![](../../../assets/developer-guide/etendo-classic/concepts/dataset-3.png)

  
Los campos principales:

  * Una **Columna** del Conjunto de datos tiene un módulo, por lo que el usuario puede añadir una nueva Columna del Conjunto de Datos a una Tabla del Conjunto de Datos existente (de otro módulo). 
  * **Excluido**: si está marcado, entonces esta columna se define para no exportarse. 

##  Uso de Conjunto de datos

El propósito principal de los conjuntos de datos es definir **datos de referencia** para los módulos.

Para exportar un conjunto de datos, es muy importante seguir estos pasos:

  * Primero, haga clic en el botón **Exportar Datos de Referencia** en la ventana **Conjunto de datos**. Esto exportará el contenido del conjunto de datos a un archivo `XML` y también generará el checksum de este conjunto de datos. 
  * Después, ejecute `./gradlew export.database` para exportar la información del checksum a los datos fuente del módulo. 

Después de esto, **el módulo puede publicarse**, e incluirá el contenido del conjunto de datos.

!!!info
    Para más información, consulte [Cómo publicar módulos en el repositorio de Github](../how-to-guides/how-to-publish-modules-to-github-repository.md).
    
!!!note
    Los datos de referencia se insertan cuando se aplica un módulo (se compila y se instala). O pueden importarse por separado.

##  Propiedad de los datos

Los datos definidos por un conjunto de datos **son propiedad de este conjunto de datos**. Esto significa que cuando hay una actualización de este conjunto de datos, cualquier cambio en estos datos se sobrescribirá de nuevo para ajustarse a la definición de la nueva versión del conjunto de datos.

Es posible marcar un conjunto de datos como **Valores por defecto del Dataset**. Tener este indicador hace que el conjunto de datos no asuma la propiedad de los datos que inserta, sino que traslada esta propiedad a la instancia. Por tanto, los nuevos registros proporcionados por el conjunto de datos se insertan, incluso en versiones más nuevas de este conjunto de datos, pero cualquier cambio realizado en la instancia se conservará.

!!!note
    En caso de que un registro proporcionado por uno de estos conjuntos de datos se elimine de la instancia, se recuperará en la siguiente actualización; la forma correcta de deshacerse de registros no deseados es marcarlos como inactivos.

##  Importación de Datos de Referencia a nivel de organización

:material-menu: `Aplicación` > `Configuración General` > `Organización` > `Gestión del módulo de Empresa`

Los datos de referencia del módulo pueden importarse en una organización usando la ventana **Gestión del módulo de Empresa**.

![](../../../assets/developer-guide/etendo-classic/concepts/datasets-4.png)


En esta lista, solo se mostrarán los **módulos relevantes** que contienen conjuntos de datos. Esto significa que si un conjunto de datos no ha cambiado desde la última vez que se aplicó a la organización seleccionada, no se mostrará.

Seleccione la organización y el módulo desde el que importar los datos de referencia a la organización. A continuación, pulse **Aceptar**. Al cabo de un tiempo, se muestra la página de resultados:


![](../../../assets/developer-guide/etendo-classic/concepts/datasets-5.png)


!!!note
    Si un conjunto de datos se define a nivel de *Organización/Entidad*, entonces también puede importarse al utilizar la utilidad [Crear entidad](../../../developer-guide/etendo-classic/how-to-guides/how-to-run-an-initial-client-setup-process.md) para crear una nueva entidad.

---
  
Este trabajo es una obra derivada de [Conjunto de datos](http://wiki.openbravo.com/wiki/Datasets){target="\_blank"} de [Wiki de Openbravo](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.