---
title: Cómo rellenar automáticamente los Identificadores
tags: 
    - Identificadores
    - Secuencia
    - Optimización de la entrada de datos
    - Datos de referencia
---

# Cómo rellenar automáticamente los Identificadores
  
##  Visión general

Los **Identificadores** son identificadores o códigos definidos por el usuario que permiten recuperar fácilmente **datos de referencia** como clientes, proveedores, productos, condiciones de pago, etc. Por ejemplo, al introducir una factura, el cliente podría seleccionarse abriendo la ventana del selector y buscándolo o, si usted conociera el identificador del **Cliente** que está buscando, podría introducirlo y pulsar **INTRO**; el sistema buscaría entonces el cliente correcto en base a ese identificador y sustituiría el identificador introducido por el nombre del cliente.

Al comenzar a escribir el **nombre del cliente** en la factura, el sistema sugiere automáticamente los clientes que coinciden con esa entrada a medida que usted escribe; una vez que haya escrito suficientes caracteres para tener una coincidencia única, la selección puede confirmarse simplemente pulsando **INTRO o TAB** y pasando al siguiente campo.

Esta funcionalidad hace que los identificadores ya no sean necesarios para la mayoría de las entidades. Usted puede reutilizar el identificador en el producto para almacenar códigos de producto, si se utilizan códigos de producto, o para almacenar números de cliente en los clientes. 

Los usuarios normalmente acaban introduciendo el mismo valor en el identificador que el que introducen en el nombre.

Esta sección explica cómo configurar Etendo para rellenar automáticamente los **campos de Identificador** y ahorrar tiempo a los usuarios.

## Pasos de ejecución

!!! warning 
    **Secuencia** son campos específicos y deben obedecer una convención de nomenclatura específica (la columna debe llamarse DocumentNo), por lo que una secuencia normal no era una opción en este caso.

En este caso, tome como inspiración la técnica utilizada para numerar automáticamente las líneas de factura (cada línea de factura tiene un número que aumenta automáticamente en 10 por cada línea) y aplíquela a los identificadores.

Supongamos este ejemplo sobre cómo generar el identificador para **Terceros**:

1. Inicie sesión como **administrador del sistema**.
2. Será necesaria una modificación del core, así que asegúrese de que existe una **plantilla de configuración activa** en el sistema con estado **En Desarrollo**. 

    !!!info
        Las plantillas de configuración son módulos que contienen cambios ya sea en el core o en otros módulos. El uso de plantillas de configuración permite personalizar el comportamiento del core del sistema sin afectar a la capacidad de aplicar maintenance packs y actualizaciones. Cree una plantilla de configuración ya sea creando manualmente un módulo de tipo plantilla o poniendo su sistema en modo de configuración.  

  
3. Vaya a la ventana **Ventanas, Pestañas y Campos** y consulte la ventana **Tercero**. Desde allí, elija la pestaña adecuada y luego revise la pestaña **Campo**. 

    Allí, encuentre el campo llamado Identificador e identifique en qué columna de qué tabla se basa. En este caso la columna es `C_BPARTNER.VALUE`. 

4. En esa columna, introduzca una nueva regla de asignación por defecto basada en la siguiente sentencia SQL: 

    ``` SQL
    @SQL=SELECT TO_CHAR(MAX(TO_NUMBER(value))+1,'FM00000000') FROM c_bpartner WHERE ad_client_id =@AD_CLIENT_ID@ AND value LIKE '0%'
    ```
    ![texto alternativo](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-automatically-populate-search-keys.png)


5. Analicemos esta regla:
    - `@SQL` significa que este valor por defecto no se va a interpretar como una constante, sino como una sentencia SQL que se ejecutará, y el valor por defecto es el resultado de esa sentencia. 
    - La sentencia select selecciona el valor máximo anterior del identificador para terceros en este mismo cliente y lo incrementa en uno. 
    - La cláusula where utiliza la expresión `@AD_CLIENT_ID@` que identifica el cliente actual en tiempo de ejecución; esto permite que distintos clientes en un entorno multi-tenant sean independientes entre sí. 
    - La cláusula `LIKE '0%'` se utiliza para evitar interferencias con valores existentes; si usted ya ha creado terceros y tienen identificadores que empiezan por cualquier cosa distinta de **0**, esta cláusula permite ignorarlos. 
    - La sentencia select necesita realizar algunas conversiones de tipo de dato. El valor es una cadena, por lo que su contenido primero debe convertirse a un número; el valor máximo debe incrementarse en uno y convertirse de nuevo a cadena con un formato de 8 dígitos. 
    - Para determinar cuántos dígitos necesita, piense cuál es el número máximo de terceros que usted tendrá alguna vez y añada 2 o 3 órdenes de magnitud solo para ir sobre seguro. 

6. Dado que usted ha creado una plantilla de configuración, asegúrese de exportarla para que no tenga problemas con su próxima actualización. Conéctese a la línea de comandos en su servidor y ejecute el siguiente comando: 

    ```groovy title="Terminal"
    ./gradlew export.database export.config.script -Dforce=true
    ```

7. La próxima vez que vaya a la ventana Tercero y comience a crear un cliente, el sistema generará el Identificador por usted y sus clientes se numerarán sin esfuerzo como 00000001, 00000002, 00000003, 00000004, etc.

8. Por último, el campo Identificador es el **primer campo con foco** de la ventana Tercero. Dado que ya no necesitará introducirlo, quizá quiera omitirlo y poner el foco directamente en el campo Nombre comercial, para que pueda ahorrar un clic en el momento de la entrada de datos. 

  
Este trabajo es una obra derivada de [Cómo rellenar automáticamente los Identificadores](http://wiki.openbravo.com/wiki/How_to_automatically_populate_search_keys){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.