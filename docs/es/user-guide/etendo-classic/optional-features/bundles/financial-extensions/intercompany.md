---
title: Intercompany
tags:
    - Intercompany
    - Organization
    - Reverse
    - Order
    - Invoice
---
# Intercompañía

## Visión general

Esta sección describe el módulo de Intercompañía incluido en el bundle **Financial Extensions**.

En caso de que el usuario tenga que crear pedidos o facturas entre dos o más organizaciones que son diferentes pero pertenecen al mismo cliente, esta funcionalidad permite generar automáticamente el **documento inverso correspondiente**. 

Por ejemplo, si la organización *A* realiza una transacción de venta a la organización *B*, una vez que la factura de venta es creada manualmente por la organización *A*, esta funcionalidad creará automáticamente una factura de compra para la organización *B*.

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el bundle Financial Extensions. Para ello, siga las instrucciones del marketplace: [Bundle Financial Extensions](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

## Configuración

### Ventana Organización

Es necesario que cada organización que utilice este módulo tenga un tercero asignado.

![](../../../../../assets/drive/PlutLfL7AlJBR18T2om4NqgG3qgdPhgtV7vE876GFmU80QIrKOSgJX2AScc0eWEB2TBUAOdVRFIdaOoMIiVZ3FM2IbIHsHSURbzG6sWX0BHArpvjqEk68iMCrwqirI3OD8I2PH3UnFQWiCYW3t5bDK5G8vtpRioFkYRiBab_zup8KCnjTzk6WAUwHw.png)

### Ventana Tercero

!!! info
    Al configurar un nuevo Tercero, tenga en cuenta que este tercero debe ser visible en la organización inversa. 


El Tercero debe configurarse como **Proveedor** y **Cliente**, utilizando las casillas de verificación correspondientes.

![](../../../../../assets/drive/7bSIJF7R9TzP-VYXO5gkqySKt7G-7YEM5ZRdplKDfRLtoEfc0FUlhr-JctNSn3vItINYI7hiRVZX1l7BV2yoOydAPlu7K4lTb3oKuPdI-k6X5-4JKmDT-q24OQYAHo3FYxFMoB57JitDmgZ3w9Krhf9sXSkXevDHLO00EHXHOjC_zMSY3mgEse7YyA.png)

![](../../../../../assets/drive/_S08VOtX0-6seijELCJ5kmLXfIJ93cNS9rIryuyqFFqOMeEC2Uq6zb_HCWjaeg8N-LtXuMRX074PBOERYCsZyV1xibJMiuZe4mde_uyxgvQJjPV9BdEsJK-w8YEeORUaQPXcPebVv3r4QhqCD-3D06jGhZM__U36rx0V2wYbN37w9fHG8o2NRrdYgw.png)

En la solapa Documentos de Intercompañía, es necesario seleccionar los tipos de documento requeridos para este tercero.

!!! info
    No es obligatorio crear nuevos tipos de documento, pero se recomienda.

![](../../../../../assets/drive/VT8AxdS0bU_4bD7b8fEIrQF-HK9e2ngLCS5TFjlUBl9ee8W1sysEH9un6GgYTL418D4rvxpIuNOt5JUxLlT2KlJ2UgbXjAZVg4mx6-VexJIx9pwA7yFoY4P0YH1RRd2-hWgMEAnGjZnn9NX53631-9T7MBsxg_RCQP4g1dvj6HqAWMbaECgUfTDT1w.png)

!!! info
    La información tanto en el tercero origen como en el tercero destino debe ser la misma.

## Facturas y pedidos

!!! info
    La siguiente información puede aplicarse no solo a facturas de venta y compra, sino también a pedidos de venta y compra.

### Cabecera

Los campos relevantes se describen a continuación:

-   Organización: es necesario seleccionar una organización configurada para trabajar como una organización de intercompañía (en el siguiente ejemplo, la organización *F&B US East Coast*).
-   Tercero: es necesario seleccionar un tercero configurado para trabajar como un tercero de intercompañía (en el siguiente ejemplo, *Be Soft Drinker, Inc.*).
-   Documento de transacción: es necesario seleccionar el tipo de documento definido en la solapa de documentos de intercompañía del tercero (en el siguiente ejemplo, el tipo de documento *AR Invoice Intercompany*).

![](../../../../../assets/drive/CBJAHylu5avoOLB0cuF8RTZZUJFtzQYm24KaV3eRWOB_6H7njxPoJ4ujK_0ZcvPokD8O3q3NZ2B3P4rEASGLEjM9Dadp9YnTsO1hSFBzAMdea3A_OfAUO-T0-BxhX2zqRF_Mh0UsY9ujTx2Pbrjy1TOxp5kpd4QC8fklcmTtfsJMnfrVwUvT7CexMA.png)

### Líneas

Los campos relevantes se describen a continuación:

-   Producto: el producto debe ser visible para ambas organizaciones (en el siguiente ejemplo, *Lemonade*). 
-   Apuntes de mayor: los apuntes de mayor necesarios deben ser visibles para ambas organizaciones.

![](../../../../../assets/drive/Q8Xn1rgR7uOHOSOr_h_l0ITlepOcHfRklfLTj8awb46t_jUCBKoV3-91JsVU5eGDQY2std_xbpvz0b-APJI11e2o9W4epq9rzioSoPB4XdWsnUpZhnCO2jkLmRinTSv4sPHUM3aODSmHiXfyQL320QR_lE8xpOD3whK6lYeLaMCafXC0G9UrVzZakA.png)

#### Producto

Los campos relevantes se describen a continuación:

-   Precio: el precio debe ser equivalente y estar disponible en cada tarifa. 
-   Moneda: la moneda debe ser la misma para ambas organizaciones.
-   Impuesto: el impuesto en cada organización debe ser equivalente.

### Completar o contabilizar documentos

Cuando **completa** facturas o **contabiliza** pedidos, estos procesos generan el documento inverso correspondiente y completan o contabilizan tanto los documentos origen como los documentos destino.

![](../../../../../assets/drive/op4ZxMClAuIecT10AFiO_n2ecoldgryLCVCYAnyWtjFgkDTaghYPrLdZ6bnDxWnykm_HGTLSmG6SkKQOtp45GnOVk3AgLm2Tbud2Lf1zR0Hsie0HE74sD93Rvl1GDfnFOWEWQVKEAfiuVZzja68OrmqgedNsOCsQ2TbrxzB41wmakZZvGBAscWqiEA.png)

#### Reactivar documentos

Para reactivar documentos de intercompañía, ambos documentos no deben tener un pago asociado.

!!! info
    Este proceso solo está permitido para documentos origen.

---

This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.