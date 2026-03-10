---
title: Cómo usar un Punto de Extensión
tags: 
    - Uso
    - Extensión
    - Punto 
    - Cómo

status: beta
---


# Cómo usar un Punto de Extensión

!!! example "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.

## Visión general

Los Puntos de Extensión son puntos de ejecución que se pueden establecer en cualquier **Procedimiento PL/SQL** y que pueden llamar a otros Procedimientos PL/SQL incluidos en cualquier módulo. Esto es útil para ampliar la funcionalidad de procedimientos existentes que contienen dicho punto de extensión. Por ejemplo, usando el Punto de Extensión *C_Invoice_Post - Finish Process*. Es posible que cualquier módulo añada un procedimiento PL/SQL para que se ejecute cada vez que se procese una factura. Esto se ha utilizado en el módulo Advanced Payables and Receivables para generar el calendario de pagos de la factura procesada.

Los Puntos de Extensión se gestionan en la ventana `Application Dictionary` > `Setup` > `Puntos de Extensión` . Aquí se pueden definir nuevos puntos de extensión y nuevos procedimientos PL/SQL asociados a Puntos de Extensión existentes. 

Existe una lista completa de puntos de extensión disponibles y de los parámetros utilizados en el documento [Puntos de Extensión](../concepts/extensionpoints.md).

### Procedimientos

Para asociar un procedimiento PL/SQL a un Punto de Extensión existente, debe crear un nuevo registro en la solapa **Procedimientos** y completar el campo **Procedimiento** con el nombre del procedimiento PL/SQL que desea que se invoque en el Punto de Extensión seleccionado.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-use-an-extension-point/extensionpoints.png)

Finalmente, defina el procedimiento PL/SQL con el mismo nombre definido en el campo **Procedimiento** y con un único parámetro **character varying** que hará referencia al registro `AD_EP_INSTANCE` que contiene todos los valores de parámetros utilizados para invocar el procedimiento PL/SQL. Por ejemplo, todos los procedimientos PL/SQL asociados al Punto de Extensión **C_Invoice_Post - Finish Process** se invocan con los siguientes parámetros: `Record_ID`, `DocAction`, `User`, `Message` y `Result`. La definición del PL/SQL y cómo se leen los parámetros puede verse en el siguiente ejemplo:
 
``` SQL
CREATE OR REPLACE FUNCTION aprm_gen_paymentschedule_inv(p_ep_instance character varying)
    RETURNS void AS
$BODY$ DECLARE 
 
p_record_id VARCHAR(60);
p_message VARCHAR(2000);
p_docAction VARCHAR(60);
p_user VARCHAR(60);
p_result NUMERIC;
 
--TYPE RECORD IS REFCURSOR;
Cur_Params RECORD;
 
BEGIN
 
    FOR Cur_Params IN (
    SELECT *
    FROM ad_ep_instance_para
    WHERE ad_ep_instance_id = p_ep_instance
    ) LOOP
    IF (cur_params.parametername LIKE 'DocAction') THEN
        p_docaction := Cur_Params.p_string;
    ELSIF (cur_params.parametername LIKE 'Record_ID') THEN
        p_record_id := cur_params.p_string;
    ELSIF (cur_params.parametername LIKE 'User') THEN
        p_user := cur_params.p_string;
    ELSIF (cur_params.parametername LIKE 'Message') THEN
        p_message := cur_params.p_text;
    ELSIF (cur_params.parametername LIKE 'Result') THEN
        p_result := cur_params.p_number;
    END IF;
    END LOOP;
 
-- The code goes here
 
END ; $BODY$
    LANGUAGE plpgsql VOLATILE
    COST 100;
```

Existe un bucle para obtener todos los parámetros; este bucle itera por todos los parámetros definidos. Observe aquí que el parámetro se identifica por `parametermame`, que coincide con el parámetro definido en el Punto de Extensión y, dependiendo de su tipo, el valor real se almacena en una de las siguientes columnas: `p_string`, `p_number` o `p_date`.

Después de que se haya definido la asociación al Punto de Extensión y se haya creado el procedimiento PL/SQL, este se ejecutará bajo las condiciones definidas para el Punto de Extensión en el documento [Puntos de Extensión](../concepts/extensionpoints.md).

---

Este trabajo es una obra derivada de [Cómo usar un Punto de Extensión](http://wiki.openbravo.com/wiki/How_to_use_an_Extension_Point){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.