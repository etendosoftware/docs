---
tags:
  - Guía práctica
  - Etendo Classic
  - Localización
  - Plan contable
  - Módulos
  - Creación de módulos
---

# Cómo crear un Módulo de plan contable

## Visión general

El plan contable (también llamado árbol de cuentas) es una lista de las cuentas disponibles para contabilizar asientos, que puede estructurarse de forma que permita obtener informes financieros significativos como el Balance de situación y la Cuenta de pérdidas y ganancias.

En algunos países, es obligatorio disponer de un plan contable específico para su uso en los libros oficiales; en otros países este requisito legal no existe y un plan contable “de ejemplo” debería ser suficiente. Por último, también debería ser posible que un país tenga más de un plan contable oficial, dependiendo, por ejemplo, del tamaño de la organización o de su actividad principal.

!!!important
    Un Módulo de plan contable para Etendo solo puede contener un único plan contable. Por tanto, si está trabajando en un proyecto de localización para un país en el que se puedan utilizar varios planes contables, debe crear módulos independientes que incluyan el archivo CSV de cada plan contable. Corresponderá al usuario instalar y aplicar el módulo de plan contable que se ajuste a sus necesidades particulares.

## Creación del archivo CSV

El primer paso para crear un módulo de plan contable es escribir el archivo CSV con la lista de cuentas que queremos incluir. Toda la información puede encontrarse en [Cómo crear archivos de cuentas](how-to-create-accounts-files.md).

## Prueba del archivo CSV

Antes de crear el módulo de plan contable, primero debemos comprobar que el archivo CSV no tiene errores estructurales o lógicos. Esto puede hacerse fácilmente en dos pasos:

1. El primero consiste en utilizar una hoja de cálculo de prueba proporcionada por Etendo que detectará cualquier error estructural, como claves de búsqueda ausentes, valores incorrectos en las columnas Element Level, Parent_Value o Show Value Condition, etc.

2. La segunda comprobación puede ejecutarse directamente a través del ERP. Consiste simplemente en importar nuestro archivo CSV al ejecutar el proceso Initial Client Setup.
Finalmente, también se recomienda crear algunos asientos contables para cada documento transaccional y asegurarse de que la información de los informes contables es correcta.

## Creación del módulo de plan contable

El paso restante es claramente el más sencillo, que consiste únicamente en incluir el archivo CSV en nuestro módulo de plan contable.

Un módulo de plan contable es como cualquier otro módulo, pero tiene únicamente las siguientes consideraciones:

- El archivo CSV debe incluirse en el directorio `referencedata/accounts/` de nuestro módulo.

- El archivo debe renombrarse a `COA.csv`. Por tanto, la estructura de directorios de nuestro módulo debería verse así:

```
 <module java package name>
   ├── referencedata 
   │   └── accounts 
   │       └── COA.csv 
   └── src-db 
       └──  database 
           └── sourcedata 
             ├── AD_DATASET.xml 
             ├── AD_MENU.xml 
             ├── AD_MODULE_DBPREFIX.xml 
             ├── AD_MODULE_DEPENDENCY.xml 
             ├── AD_MODULE.xml 
             ├── AD_PACKAGE.xml 
             ├── AD_PROCESS_PARA.xml 
             ├── AD_PROCESS.xml 
             └── AD_TREENODE.xml            
```

- Al definir el módulo dentro del Diccionario de aplicación, las únicas consideraciones importantes que debemos tener son:

    - Establecer el tipo de módulo como *Módulo*

    - Marcar la casilla *Tiene plan contable*

    - Recordar añadir la *dependencia de Core*

### Publicación del Módulo de plan contable

La forma de empaquetar un módulo de plan contable es similar al proceso de [cómo publicar módulos en el repositorio de GitHub](../../../developer-guide/etendo-classic/how-to-guides/how-to-publish-modules-to-github-repository.md).

El proceso resumido es:

- Crear la definición del módulo en el Diccionario de aplicación. Debe seguir las [Directrices de nomenclatura para módulos](../../../developer-guide/etendo-classic/concepts/naming-guidelines-for-modules.md). Recuerde registrar el módulo en caso de que quiera publicarlo en la Forge.

- Marcar la casilla *Tiene plan contable* y añadir una *dependencia de Core*.

- Exportar la base de datos para crear la estructura de archivos

``` gradle title="Terminal"
  ./gradlew export.database
```

- Guardar el archivo `COA.csv` dentro del directorio `referencedata/accounts/` del módulo. Debe crear manualmente esta estructura de directorios si fuese necesario.

- Publicar el módulo de plan contable

``` gradle title="Terminal"
  ./gradlew publishVersion -Ppkg=<module javapackage>
```

## Traducción de un plan contable

En algunos países puede ser útil disponer del mismo plan contable traducido a varios idiomas. Desafortunadamente, Etendo todavía no soporta la traducción de planes contables.

Si se encuentra en esta situación, tiene dos posibles alternativas:

- Crear varios módulos de plan contable para distintos idiomas. La estructura del archivo del plan contable será exactamente la misma, cambiando únicamente los nombres y descripciones de las cuentas para cada idioma. Esta solución es perfecta para empresas que quieren trabajar en un único idioma, aunque existan varios idiomas oficiales en el país. En este caso, el administrador debe decidir al inicio de la implantación del ERP el idioma a utilizar para el plan contable y no podrá cambiarlo en el futuro.

- La otra posibilidad es crear un único módulo de plan contable y, una vez aplicado en una instancia, traducir manualmente los valores de los elementos dentro de la ventana Árbol de cuentas. El inconveniente de este método es que la traducción no puede distribuirse a otras instancias y el proceso de traducción debe repetirse manualmente, o mediante la implementación de un script que traduzca automáticamente los elementos basándose en la clave de búsqueda del Valor del elemento.

---

Este trabajo es una obra derivada de [Cómo crear un módulo de plan contable](https://wiki.openbravo.com/wiki/How_to_create_a_Chart_of_Accounts_Module){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizado bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.