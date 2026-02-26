---
title: Cómo implementar un nuevo tipo de descuento y promoción
tags: 
    - Descuento
    - Promoción
    - Tipo
    - Cómo hacer
status: beta
---

# Cómo implementar un nuevo tipo de descuento y promoción

!!! example "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.

## Visión general

Un tipo de descuento y promoción es una implementación de una regla para [Modificación de precios](../../../user-guide/etendo-classic/basic-features/master-data-management/pricing.md#discounts-and-promotions-window). Estas reglas definen la lógica que se aplicará para calcular el descuento cuando el descuento o la promoción puedan aplicarse.

Este procedimiento está dirigido a desarrolladores que deseen implementar este tipo de reglas. Los usuarios que necesiten configurar las existentes deberían leer [Modificación de precios](../../../user-guide/etendo-classic/basic-features/master-data-management/pricing.md#discounts-and-promotions-window) en su lugar.

Es posible definir tipos que se encarguen de una sola línea, como **descuento del X por ciento** en un único producto, y tipos que analicen todo el pedido o la factura para determinar si el descuento es aplicable, por ejemplo **comprando los productos X e Y, Z es gratis**.

## Implementación

La implementación de un *Tipo de descuento y promoción* se realiza dentro de un módulo. Este procedimiento asume que ya existe un [módulo](how-to-create-a-module.md) creado.

### Especificación del tipo

Este documento explica cómo crear un tipo **Compre X pague Y del mismo producto**. Esta regla se aplica cuando hay al menos X unidades en una línea; en este caso, por cada grupo de X unidades, solo se pagan Y.

Por ejemplo, si la regla puede aplicarse al producto A (cuyo precio es 10€), X es 4 e Y es 3. Un pedido que incluya 4 unidades de A tendría un descuento de 10€. Un pedido que incluya 9 unidades de A tendría un descuento de 20€.

### Infraestructura

Lo primero que debe hacerse es ampliar la tabla que define Modificación de precios (`M_Offer`) en caso de que las columnas que tiene no soporten los requisitos de nuestro tipo de descuento. En este caso necesitamos las columnas X e Y.

``` SQL
ALTER TABLE M_Offer ADD COLUMN em_obdisc_X numeric;
ALTER TABLE M_Offer ADD COLUMN em_obdisc_Y numeric;
```

!!!note
    En este caso, el DBPrefix de nuestro módulo es `OBDISC`.

Ahora deben crearse las columnas en el *Diccionario de la Aplicación* para la tabla `M_Offer`: vaya a la ventana **Tablas y columnas**, busque la tabla `M_Offer` y haga clic en el **botón Crear columnas desde BD**.

Después, sus campos correspondientes en la ventana Modificación de precios: vaya a la ventana **Windows, Tabs and Fields**, busque la ventana **Modificación de precios**, la solapa **Modificación de precios** y haga clic en el botón **Crear campos**.

### Definición del tipo de descuento y promoción

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-implement-a-new-discount-and-promotion-type/discount-promotion-type.png)

Para poner a disposición el nuevo tipo, solo necesita registrarlo en la ventana **Tipos de descuentos y promociones**. Cree allí un nuevo registro, seleccione el módulo en el que está trabajando y añada un nombre descriptivo.

El campo **Implementador PL/SQL** indica cuál es la función PL que implementa este tipo. En este caso la hemos llamado `OBDISC_XY_Same_Product`.

Una vez creado, este tipo estará disponible desde la ventana **Modificación de precios** al definir nuevas reglas.

Tenga en cuenta que es una buena práctica, para mantener esta ventana disponible, mostrar los campos creados en la sección anterior por si este tipo se selecciona. Esto puede lograrse añadiéndoles una lógica de visualización que debería ser similar a `@M_Offer_Type_ID@='E08EE3C23EBA49358A881EF06C139D63'`, donde `'E08EE3C23EBA49358A881EF06C139D63'` es el UUID del registro que se acaba de crear en **Tipos de descuentos y promociones**.

### Implementación PL/SQL

El código que implementa el tipo es:

``` SQL
CREATE OR REPLACE FUNCTION obdisc_xy_same_product(p_type character varying, p_rule_id character varying, p_line_id character varying, p_priceprecision numeric, p_stdprecision numeric, p_user_id character varying, p_taxincluded character varying)
  RETURNS character varying AS
$BODY$ DECLARE 
  v_x NUMERIC;
  v_y NUMERIC;
  v_apply_next VARCHAR(1);
  v_mod NUMERIC;
  v_chunks NUMERIC;
  v_tax VARCHAR(32);
  v_qty NUMERIC;
  v_unitPrice NUMERIC;
  v_newUnitPrice NUMERIC;
  v_newGrossAmt NUMERIC;
  v_newNetAmt NUMERIC;
  v_newNetLine NUMERIC;
  v_priceactual NUMERIC;
  v_basePrice NUMERIC;
  v_origGrossAmt NUMERIC;
  v_origLineNetAmt NUMERIC;
  v_totalPromotion NUMERIC;
BEGIN
  -- 1. Obtain information about how the rule is configured
  SELECT em_obdisc_x, em_obdisc_y, apply_next
    INTO v_x, v_y, v_apply_next
    FROM m_offer
   WHERE m_offer_id = p_rule_id;
 
  -- 2. Obtain information about the line the promotion can be 
  -- applied to
  IF (p_type ='O') then -- Get info from Order
    SELECT gross_unit_price, c_tax_id, qtyordered, priceactual,
           line_gross_amount, linenetamt
      INTO v_unitprice, v_tax, v_qty, v_priceactual,
           v_origGrossAmt, v_origLineNetAmt
      FROM c_orderline
     WHERE c_orderline_id = p_line_id;
  else -- Get info from Invoice
   SELECT gross_unit_price, c_tax_id, qtyinvoiced, priceactual,
          line_gross_amount, linenetamt
     INTO v_unitprice, v_tax, v_qty, v_priceactual,
          v_origGrossAmt, v_origLineNetAmt
     FROM c_invoiceline
    WHERE c_invoiceline_id = p_line_id;
  end IF;
 
   -- 3. Decide whether the rule can be applied
   IF (v_qty < v_x) then
     RETURN 'Y'; -- rule not applied, apply next one if present
   end IF;
 
   -- 4. Calculate the discount
   v_mod := mod (v_qty, v_x); -- Units without discount
   v_chunks := floor(v_qty / v_x); -- How many times the discount is applied
   
   IF (p_taxIncluded = 'Y') then
     v_newGrossAmt := round(v_chunks * v_y * v_unitprice + v_unitprice * v_mod, p_stdprecision);
     v_newUnitPrice := round(v_newGrossAmt / v_qty, p_priceprecision);
 
     v_newNetLine := c_get_net_price_from_gross(v_tax, v_newGrossAmt, v_newGrossAmt, p_priceprecision, v_qty);
     v_newNetAmt := round(v_newNetLine * v_qty, p_stdprecision);
     v_basePrice := v_unitprice;
     v_totalPromotion := v_origGrossAmt - v_newGrossAmt;
   else
     v_newNetAmt := round(v_chunks * v_y * v_priceactual + v_priceactual * v_mod, p_stdprecision);
     v_newNetLine := round(v_newNetAmt / v_qty, p_priceprecision);
     v_basePrice := v_priceactual;
     v_totalPromotion := v_origLineNetAmt - v_newGrossAmt;
   end IF;
 
   PERFORM M_PROMOTION_ADD(p_type, p_line_id, p_rule_id, p_taxIncluded, 
                           v_newUnitPrice, v_newGrossAmt, v_newNetLine, 
                           v_newNetAmt, v_totalPromotion, v_totalPromotion, 
                           v_basePrice, p_user_id);
 
   -- 5. return whether other discounts can be applied to this same line                           
   RETURN v_apply_next;
END ; $BODY$
  LANGUAGE plpgsql VOLATILE
```

**Explicación del código**

Las siguientes secciones explican este código. Los números del título se refieren a los números en los comentarios anteriores.

#### Parámetros

Cualquier función que implemente un tipo de descuento y promoción debe recibir los siguientes parámetros:

- `p_type`: Los valores posibles son O o I. O significa pedido e I significa factura. Indica si la regla se está aplicando a una línea de pedido o a una línea de factura.
- `p_rule_id`: ID de la regla (M_Offer.M_Offer_ID) que se está comprobando.
- `p_line_id`: ID de la línea (línea de pedido o línea de factura) a la que se está aplicando la promoción.
- `p_priceprecision`: En función de la divisa del documento, la precisión que se utilizará al redondear precios.
- `p_stdprecision`: En función de la divisa del documento, la precisión que se utilizará al redondear importes.
- `p_user_id`: ID del usuario que ha invocado el proceso, utilizado al crear el descuento real con fines de auditoría.
- `p_taxincluded`: Los valores posibles son Y o N. Indica si la [Tarifa](../../../user-guide/etendo-classic/basic-features/master-data-management/pricing.md#price-list) aplicada al documento actual incluye (Y) o no (N) impuestos.

#### 1. Obtener la configuración de la regla

El descuento y promoción que se está comprobando normalmente tiene cierta configuración de instancia. En nuestro caso, valores para X e Y, y si otras promociones y descuentos pueden encadenarse a esta misma línea después de aplicar este.

#### 2. Obtener la información de la línea

Debe recuperarse la información de la línea. Tenga en cuenta que la misma función se invoca para pedidos y facturas, determinado por p_type, por lo que ambos casos deben tenerse en cuenta.

#### 3. Decidir si la regla puede aplicarse

Este código se ejecuta para todas las promociones y descuentos que son candidatos a aplicarse a cada línea (consulte la [siguiente sección](#cuándo-se-ejecuta-este-código)). Dependiendo de las reglas que defina el tipo, es posible que esta regla candidata sea rechazada.

En este caso, si la cantidad en la línea es inferior al valor de X, la regla se rechaza. Tenga en cuenta que, como la regla no se aplica, se devuelve Y; esto significa que siempre pueden aplicarse otros descuentos.

#### 4. Calcular el descuento

En este punto sabemos que el descuento debe aplicarse a esta línea. Es el momento de implementar realmente los importes a descontar.

Aquí es importante tener en cuenta las diferencias entre tarifas que incluyen impuestos y las que no, así como el redondeo correcto.

Finalmente, cuando todo está calculado, el descuento se inserta invocando la función `M_Promotion_Add`. Esta creará un nuevo registro en la tabla `C_OrderLine_Offer` o `C_InvoiceLine_Offer`.

#### 5. Devolver

Se espera que estas funciones devuelvan un valor booleano (Y o N). Si se devuelve Y, el algoritmo continuará buscando descuentos y promociones adicionales para aplicar a esta línea; mientras que, en caso de N, el algoritmo se detendrá después de aplicar este.

### Cuándo se ejecuta este código

El código que comprueba Modificación de precios (`M_Promotion_Calculate`) se ejecuta cuando *Pedidos y facturas* se **completan** o cuando se hace clic en el **botón** *Calcular promociones* en cualquiera de estas ventanas.

Este código restablece los precios eliminando todos los posibles descuentos y promociones aplicados previamente y busca candidatos de descuentos y promociones para aplicarlos a cada línea del documento.

Un candidato a descuento es un descuento que puede aplicarse a la línea en función de los filtros generales que define este descuento. Finalmente, el PL/SQL que implementa el tipo se encarga de decidir si el descuento se aplica o no. Por ejemplo, si X es 4 y la regla puede aplicarse a A, cualquier línea con el producto A tendrá esta regla como candidata, pero solo aquellas con una cantidad igual o superior a 4 deberían aplicarse con el descuento.

---
Este trabajo es una obra derivada de [Cómo implementar un nuevo tipo de descuento y promoción](https://wiki.openbravo.com/wiki/How_to_implement_a_new_Discount_and_Promotion_Type){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.