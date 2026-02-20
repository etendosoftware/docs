---
tags: 
  - How to
  - Add Columns
  - Table
  - Configuring Columns
  - Application Dictionary
---

#  Cómo añadir columnas a una tabla 

##  Visión general

En esta sección, el usuario puede encontrar información sobre cómo ampliar la tabla creada en la sección [Cómo crear una tabla](how-to-create-a-table.md) para incluir campos adicionales.

Se añadirán tres campos diferentes para mostrar cómo configurar algunas de las referencias posibles:

  1. _ValidTo_ , un campo de fecha simple que coincide con la fecha ValidFrom ya presente en esta tabla 
  2. _Payment Schedule_ , mostrado al usuario como un cuadro combinado para poder elegir entre tres valores definidos en una lista valores. 
    1. Primer día del mes 
    2. Mitad del mes 
    3. Último día del mes 
  3. _Payment Category_ , un enlace a otra tabla existente que permite seleccionar entre los valores presentes en esa tabla. 

  
Estos cambios se pueden realizar en dos ubicaciones diferentes:

  1. Añadir columnas al módulo *original* (dbprefix `HT` ) 
  2. Crear un *segundo* módulo (dbprefix `HT2` ) que añade las columnas al primer módulo 

La primera opción puede elegirse si el autor del módulo original quiere añadir más columnas a su módulo. La segunda opción es posible para cualquiera, ya que las columnas se añaden mediante un nuevo módulo al existente, que no se modifica directamente.

La principal diferencia entre estos dos métodos son los nombres que deben elegirse para las columnas para cumplir las reglas de nomenclatura de modularidad.

  1. Añadir una columna al mismo módulo: se puede elegir cualquier nombre de columna válido 
  2. Mediante un segundo módulo: el nuevo nombre de columna debe cumplir el patrón `EM_<DBPREFIX>` donde `<DBPREFIX>` debe ser el dbprefix del nuevo módulo que contiene la columna a añadir. En este ejemplo: `EM_HT2`

A partir de ahora, seguiremos este segundo enfoque y colocaremos todos los elementos nuevos en un nuevo módulo con dbprefix `HT2` .

Para mostrar cómo se configuran diferentes tipos de columna, añadiremos 3 columnas nuevas:

  * _Valid To_ una columna simple de tipo fecha 
  * _Payment Schedule_ una lista valores que contiene una lista de valores: _Start of Month_ , _Mid of Month_ , _End of Month_
  * _Salary Category_ una referencia que apunta a la tabla existente _Salary Category_. 

###  Creación del nuevo módulo

Esta sección solo enumera los principales elementos importantes necesarios para el nuevo módulo. Puede encontrar más detalles en [Cómo crear un módulo](How_To_Create_a_Module.md)

  * dbprefix: `HT2`
  * Dependencias: 
    * Core como es habitual 

###  Creación de las columnas en la base de datos

| Nombre de columna     | Tipo   | Longitud | Nota                                                                                                                                   |
| --------------- | ------ | ------ | -------------------------------------------------------------------------------------------------------------------------------------- |
|`em_ht2_validto`  |  DATE  |  |  Fecha hasta la que este salario es válido.  
|`em_ht2_payment_schedule`  |  VARCHAR  |  60  |  Cuándo se paga el salario  
|`em_ht2_c_salary_category_id`  |  VARCHAR  |  32  |  Enlace a la Categoría Salarial  
  
Para crear la tabla anterior dentro de la base de datos, utilice una de las siguientes sentencias `ALTER TABLE` dependiendo de la BD que esté utilizando:

```sql title="SQL script"
ALTER TABLE ht_salary ADD COLUMN em_ht2_validto timestamp without time zone;
ALTER TABLE ht_salary ADD COLUMN em_ht2_payment_schedule VARCHAR(60);
ALTER TABLE ht_salary ADD COLUMN em_ht2_c_salary_category_id VARCHAR(32);
ALTER TABLE ht_salary ADD CONSTRAINT "em_ht2_c_salary_category" FOREIGN KEY (em_ht2_c_salary_category_id) REFERENCES c_salary_category(c_salary_category_id);
```

Como puede verse en el SQL, se añade una clave foránea junto con el nuevo campo que enlaza con la tabla `c_salary_category`. Esto garantiza que solo se puedan seleccionar categorías existentes y también que no se pueda eliminar ninguna categoría salarial mientras se utilice en la tabla `ht_salary`.

###  Añadir y configurar las columnas en el Diccionario de aplicación

En esta parte, añadiremos la columna recién añadida a la lista de columnas ya definidas para la tabla `ht_salary` y luego configuraremos esas definiciones de columna para que coincidan con la descripción indicada en la sección de objetivos anterior.

####  Añadir la nueva columna al Diccionario de aplicación

Los pasos a seguir son:

  1. En la ventana `Tablas y columnas` busque la entrada de la tabla `ht_salary`. 
  2. Con este registro seleccionado, ejecute el proceso *Crear columnas de la base de datos*. Como la tabla ya contiene varias columnas, solo se añadirán las columnas que aún no estén presentes en la definición del Diccionario de aplicación de esa tabla. En esta sección, este proceso añadirá nuestras 3 columnas recién creadas a la lista. Observe que esas nuevas entradas se asocian automáticamente con el nuevo módulo con prefijo `HT2`, ya que el proceso lo detectó a través del nombre de las columnas de la base de datos. 

Al revisar la estructura de carpetas del módulo después de ejecutar `./gradlew export.database`, se muestra que las nuevas columnas se han exportado a un archivo en una carpeta 'modifiedTables' en lugar de la habitual 'tables', para indicar que este módulo no crea la tabla `ht_salary`, sino que está añadiendo nuevos elementos a la misma.

```
org.openbravo.howtos2
└── src-db
    └── database
        └── model
            ├── functions
            └── modifiedTables
            │       └── HT_SALARY.xml
            ├── sequences
            ├── tables
            ├── triggers
            └── views
        └── sourcedata
            ├── AD_MODULE_DBPREFIX.xml
            ├── AD_MODULE_DEPENDENCY.xml
            ├── AD_MODULE.xml
            └── AD_PACKAGE.xml
```  

####  Configuración de las nuevas columnas

Antes de empezar a configurar las nuevas columnas, deben realizarse dos pasos preparatorios.

  1. Crear una _Lista valores_ para la columna _Payment Schedule_ para definir los 3 valores que deberían permitirse para esta lista. 
  2. Crear una referencia _Tabla_ para la columna `em_ht2_c_salary_category_id`, ya que la referencia estándar _TableDir_ no puede utilizarse con columnas de tipo _em_.

Al añadir estos nuevos elementos, recuerde colocarlos en el nuevo módulo con prefijo `HT2`.

El primer paso es crear una nueva *Referencia* para contener la lista de valores de la columna _Payment Schedule_. Los valores importantes a configurar aquí son:

  * _Referencia padre_ = *Lista* en la propia definición de la Referencia, para definirla como una Lista valores. 
  * Para cada entrada en la pestaña _Lista valores_ 
    * _Identificador_ El valor almacenado en el campo de la base de datos cuando un usuario selecciona esta entrada en el cuadro combinado. 
    * _Nombre_ El texto visible para el usuario (traducible) mostrado en la UI. 
    * _Secuencia_ para definir el orden de las entradas que debe utilizarse en la UI. 

La siguiente captura de pantalla muestra cómo se verá la referencia definida.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_add_Columns_to_a_Table-1.png)

  
El segundo paso es crear una *Tabla referenciada* para definir cómo el nuevo campo *Categoría Salarial* se enlaza con la tabla `c_salary_category`.

Para ello, debe crearse una nueva *Referencia*. En este caso, los valores importantes son los siguientes:

  * _Referencia padre_ = *Tabla* para indicar que se trata de una Tabla referenciada. 
  * En la pestaña _Tabla referenciada_: 
    * _Tabla_ = `c_salary_category` ya que esta es la tabla destino a la que apuntará nuestra nueva columna.
    * _Columna clave_ = `c_salary_category_id` ya que esta es la clave primaria de la tabla destino 
    * _Display Column_ = `Name` para indicar el campo de esta tabla que debe mostrarse en la UI para esta columna. 

La siguiente captura de pantalla muestra cómo se verá la referencia definida.  

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_add_Columns_to_a_Table-2.png)

  
Después de estos dos pasos previos, finalmente podemos configurar las nuevas columnas para que utilicen la referencia que acabamos de crear.

En la ventana *Tablas y columnas*, buscamos la entrada de la tabla `ht_salary`. En la pestaña Columna realizamos los siguientes cambios para nuestras nuevas columnas:

  1. _Payment Schedule_, cambie la *Referencia* de esta columna de _String_ a *Lista* y cambie la *Referencia clave* a nuestra Lista valores recién creada con nombre `EM_Ht2_Payment_Schedule`. 
  2. _Salary Category_ , cambie la *Referencia* de esta columna de _TableDir_ a *Tabla* y cambie la *Referencia clave* a la nueva `ht_salary_c_salary_category` . 

  
El paso final sería ejecutar el proceso *Sincronizar términos* y actualizar los elementos creados para que tengan nombres útiles para la UI.

Sin embargo, mientras el issue  10886  no esté corregido, este proceso no mapeará correctamente los elementos existentes para columnas que sigan las reglas de nomenclatura `EM_`.

Como solución alternativa y para reutilizar los elementos core existentes para las dos columnas para las que existe uno ( _validto_ , _Salary Category_ ), asigne manualmente los elementos existentes a esas dos columnas.

Para ello, se necesitan los siguientes cambios en la misma ventana abierta *Tablas y columnas* (aún abierta desde el último paso) y en la pestaña *Columna* de la tabla `ht_salary`.

  1. _ValidTo_ cambie el *Elemento del sistema* a _ValidTo - Valid To Date_
  2. _Salary Category_ cambie el *Elemento del sistema* a _C_Salary_Category_ID - Salary Category_

  
Ahora ejecute el proceso *Sincronizar términos* para establecer el elemento de la última columna, que aún no tiene un elemento coincidente.

Después de esto, las nuevas columnas deberían verse como se muestra en la siguiente captura de pantalla:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_add_Columns_to_a_Table-3.png)
  
Como paso final, ahora actualizamos el elemento `EM_Ht2_Payment_Schedule` recién creado para que tenga una etiqueta útil para la UI.

Navegando a `Application Dictionary` > `Element` buscamos el nuevo elemento y realizamos las siguientes actualizaciones:

  1. *Nombre* cambiar de `EM_Ht2_Payment_Schedule` a *Payment Schedule*
  2. *Print Name* cambiar de `EM_Ht2_Payment_Schedule` a *Payment Schedule*

Estas actualizaciones son necesarias para tener etiquetas útiles en la UI para cualquier ventana definida sobre esta tabla y para evitar que estas utilicen nombres internos con la terminología técnica `EM`.

###  Reconstrucción del sistema

Finalmente, para que las columnas recién añadidas estén disponibles en tiempo de ejecución, debe ejecutarse `./gradlew generate.entities` y desplegarse los cambios en tomcat. Estos dos pasos pueden realizarse juntos ejecutando `./gradlew smartbuild`. Después de eso, debe reiniciarse Tomcat para refrescar el modelo DAL en memoria, de modo que conozca las columnas recién añadidas.

Una vez que las columnas se añaden a la tabla, el usuario puede [exportar](../../../developer-guide/etendo-classic/how-to-guides/How_To_Create_a_Module.md#exporting-a-module) el módulo.

Para añadir las nuevas columnas a la ventana definida sobre esta tabla, visite [Cómo añadir un campo a una pestaña de ventana](../../../developer-guide/etendo-classic/how-to-guides/how-to-add-a-field-to-a-window-tab.md).

---

Este trabajo es una obra derivada de [Cómo añadir columnas a una tabla](http://wiki.openbravo.com/wiki/How_to_add_Columns_to_a_Table){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.