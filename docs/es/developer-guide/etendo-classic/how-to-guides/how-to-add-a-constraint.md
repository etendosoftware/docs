---
title: Cómo añadir una restricción
tags: 
    - Restricción
    - Tabla
    - Crear mensaje
    - Base de datos
status: beta
---


# Cómo añadir una restricción

!!! example "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.


## Visión general

Al añadir nuevas columnas a una tabla como la **fecha Válido hasta** en la **tabla ht_salary**, a menudo es necesario aplicar reglas lógicas para que los datos se mantengan consistentes. En este caso, la fecha Válido hasta debe ser siempre igual o posterior a la fecha Válido desde. Esta regla puede aplicarse añadiendo una **restricción de base de datos**, que es una `SQL-Expression`, que comprueba la validez de los datos cada vez que se insertan o actualizan filas.

!!!info
    Para más información, visite [Cómo añadir columnas a una tabla](./how-to-add-columns-to-a-table.md).


## Modularidad

Como la restricción se colocará en el módulo con dbprefix `HT2` pero la tabla **ht_salary** está definida en otro módulo `HT`, el nombre de la restricción debe seguir la regla habitual y comenzar con `EM_HT2`.

Si la restricción se añadiera en el mismo módulo que su tabla, entonces no sería necesaria esta `regla de nomenclatura EM_`. Sin embargo, la mejor práctica es que, en ese caso, comience con el **nombre completo de la tabla** para garantizar que su nombre sea único en toda la base de datos.

!!! info
    Recuerde que, en todos los casos, el nombre completo de la restricción (como cualquier otro nombre de `db-object`) no puede tener más de 30 caracteres.  
 
  
## Añadir restricción a la base de datos

Para añadir la restricción, ejecute la siguiente cláusula en la base de datos:

``` SQL title="PostgreSQL"
ALTER TABLE ht_salary ADD constraint em_ht2_ht_salary_date_chk CHECK (em_ht2_validto>=validfrom);
```

``` SQL title="Oracle"
ALTER TABLE HT_SALARY ADD CONSTRAINT EM_HT2_HT_SALARY_DATES_CHK CHECK  (VALIDTO>=VALIDFROM) ENABLE;
```

!!! note
    Añadir una **restricción única** a un módulo existente se considera un cambio de API y podría afectar a entornos existentes ya poblados. Antes de añadirla, evalúe el riesgo y considere crear una buildvalidation para comprobar si los datos existentes cumplen. Si no lo hacen, la buildvalidation puede detener el proceso de actualización y mostrar un mensaje adecuado.  
 
  
## Añadir un mensaje adecuado

Ahora, al editar datos en la pestaña `Employee Salary > Salary` e intentar usar una fecha **Válido hasta** anterior a la fecha **Válido desde**, obtenemos un mensaje de error como se muestra a continuación.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-add-a-constraint-2.png)

Sin embargo, este mensaje de error todavía no es demasiado útil para el usuario, ya que no indica en absoluto por qué no se realizó la acción de guardado.
  
Sería mejor que dijera algo como **La fecha Válido hasta no puede ser anterior a la fecha Válido desde** para ayudar al usuario a especificar correctamente las dos fechas.
Esto se hace añadiendo un nuevo Mensaje. Esto aprovecha el sistema de traducciones de Etendo para que el mensaje pueda traducirse y mostrarse en el idioma del usuario.

!!! info
    Para más información sobre cómo crear una nueva entrada de mensaje, visite [Mensaje](../../etendo-classic/concepts/messages.md).

Como breve resumen:

En la ventana `Application Dictionary > Message` cree un nuevo registro usando los siguientes detalles:

  * **Módulo** `Example HT2 Module` ya que este es el módulo que también contiene la restricción.
  * **Identificador** : El identificador debe ser exactamente el mismo que el de la restricción; en este caso `_em_ht2_ht_salary_dates_chk_`, ya que este es el vínculo entre la restricción y el mensaje. 
  * **Tipo de mensaje** : Dependiendo del tipo, la UI del cuadro de mensaje será diferente (verde para éxito, amarillo para advertencia...), en nuestro caso queremos un cuadro de mensaje de error en rojo, por lo que seleccionamos **Error**. 
  * **Mensaje de texto** : Es el mensaje amigable para el usuario que se mostrará dentro del cuadro de mensaje. Así que introduzca: **La fecha Válido hasta no puede ser anterior a la fecha Válido desde**. 

Entonces, tendremos un mensaje como:


![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-add-a-constraint-3.png)

## Exportar base de datos

Siempre que se modifique el Diccionario de Aplicación o la base de datos física, es posible exportar esa información a archivos `XML`; esta es la forma en que Etendo mantiene los datos de base de datos como parte de sus archivos de código fuente. 
Para hacerlo, simplemente ejecute:

```groovy title="Terminal"
./gradlew export.database
```

!!! info
    Para más información, visite [Documento de tareas de desarrollo](../developer-tools/etendo-gradle-plugin.md#build-tasks).



Este trabajo es una obra derivada de [Cómo añadir una restricción](http://wiki.openbravo.com/wiki/How_to_add_a_Constraint){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.