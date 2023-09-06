---
title: Facturación Electrónica 
hide:
    - navigation
---

## Facturación Electrónica

### Introducción

El módulo de integración de Etendo con FACe permite enviar facturas de venta, que se le realizan a la Administración Pública, en forma electrónica al organismo recaudador español. El envío puede realizarse en forma manual o a través de un proceso por background que envía en forma masiva las facturas que estén en condiciones de enviarse.  
Las facturas listas para enviar se pueden visualizar en la ventana **Facturación Electrónica**, desde el menú de aplicación.  
 

![](/docs/assets/drive/FQsij5BgybLWD7w28H757JiwzySIgz1wzzC3mhmVzWCHWKE9FVwsU9ptPc8lidGsu93_yQ_dasFsyaTJKL7yuFd11VSIQQYs17-yT19ShsXyet8v16RjFC1G7dXQVNwoCIGHLvSNEG8EYY3rx2ZhaUoQBTFNwwL3Z-lAlx2WgIeMVwCkTry5WfM1CSZc-Q.png)

## **Descripción general del módulo**

A continuación se describen las ventanas que introduce este módulo:

-   **Puntos de entrada**: en esta ventana se encuentran las configuraciones necesarias para la conexión entre Etendo y los servidores del órgano recaudador español. 

![](/docs/assets/drive/QST5LO3PLmCyJHKRtcKle3bvdz2jHcEe19vCNbN38RKo7zF9JMxzXdhhIVMXFQaDnoEdv7zlCbXuCp2OY4j2r4OKOZzu9Kz9U0DhlnxQfNCmzi9HpAM3QNXSIszQOXumf_nMJRaYLPyYWUsu8CCAXdd6TD4swu7EtyZ5fTv3hlkxSuepn9VCeaB-lGl35w.png)

-   **Parámetros generales de Fact. Elect.**: en esta ventana se pueden visualizar y realizar las configuraciones necesarias para cada organización con la que se quieran enviar facturas en forma electrónica.

![](/docs/assets/drive/moThdzPKVhbWfCNzomhi8GRGb033dokHuw_xvJY_ZqoqwCu0qNfPDT5PtMOH7ZkhJeVcukUO6SCR0lJZZEY_WqF7riJpvZ0vJMZaHJyfvltFfcMj4DYtNYLv2cS0zGA1WzWlDihrLWvaIY2URAwwbFfzlM8IDBFtYWj-cZzUDmFPJn3Zz15f_eeBEJVtiw.png)

-   **Órganos proponentes**: se pueden crear registros con los órganos proponentes que se requieran para cada organización, y luego setearse en las facturas que se registren con la misma organización.

![](/docs/assets/drive/hJfaPtSYbLyCXnlic721pK0m92aoSoaWRgxwfrFD9ohOxgBRZYfoekpy0GUVTkR4Oh4yXIcb-J8UE3P5TIEOylfQf9WrXvigsA4mwUrlmONqTOQVU-HaibYTDecqgnhtbmRbz1BZg_LwODBXEOAyVN_7HdYRoy7vrV7YIjveSIgewbFHcRTiWxtgKpLqGg.png)

-   **Terceros Fact. Elect.**: aquí igual que la anterior, se pueden visualizar y realizar las configuraciones necesarias para cada Tercero con el que se quiera enviar facturas en forma electrónica, incluyendo la selección de unidades tramitadoras y los montos límites para la facturación.

![](/docs/assets/drive/ZG3r8cAnym_v_CWRISRvgEZEeDZFkY3TgE8I3pnde39E5Fj3gdbD966-bxhCqRHigNjvhWQ0-81UF1gFsDrFuLv02Wwm6bPcjXXHvJXNB1c4tOBikYA3wwIm6ZfaQmF2L2hVZO7ltG27hE4Ih5ldwM33HoogK7y2e7aQbV7H96-xR1uG5Ntj8UxfPcyLZQ.png)

-   **Impuestos Fact. Elect.**: en esta ventana se pueden ver y realizar las configuraciones necesarias para cada tipo de Impuesto con el que se quiera enviar facturas en forma electrónica.

![](/docs/assets/drive/E6O2moc-IcqNNKTFYoIOFH5i_exmNxBy0uHjFK_AOZh1Q-E3nh8kNIQUG9robR66rxznLjN3zbxNqzOwfU8jF-7llJwecZyIvR57TaJw3uOGDcSRtcfznMRaPa1s3OuZ5Y1cPfb-_P20cPCKlWrtjzNY-3EGT8szVERizn0HGmjbMCFogA_B-qbNhXaqCQ.png)

-   **Montos Fact. Elect.**: en esta ventana se puede visualizar y configurar el *monto límite mínimo* a partir del cual se deberán enviar las facturas en forma electrónica en forma obligatoria a partir de una fecha determinada.

![](/docs/assets/drive/Zy5UfDKDWTMyvVWjDPI1VgODpWBw7DdREGN2IbCYXkD0WlPSQ_pWky1Y7c3ljJPAj20dPZdQp7GKY4vIJJaez8G9Hy0MgVu2xDrSvQlpe2Q9qtyVcBaI8vQAlHrYbMMYjsWiSMfH_sXJdveW8_Ps-QaVq6S7tk4DW98vVJ95EfvTPfcdf5Bo_KKmWTfAZg.png)

-   **Facturas Electrónicas**: en esta ventana se pueden visualizar aquellas facturas que están en condiciones de ser enviadas al organismo recaudador. 
!!! info
    Podrán enviarse las que se hallen en estado Completada y que cuenten con todas las configuraciones realizadas.


En la cabecera se muestran dos grupos de campos, uno con los principales datos de la factura y otro, que permite visualizar el estado general de la factura una vez que ha sido enviada. Este último contiene los siguientes campos:

-   ***Código de registro***: es el número que identifica la factura enviada en los servidores del gobierno español.
-   ***Fecha de recepción***: es la fecha en que fue recibida con éxito la factura.
-   ***Estado transmisión**:* muestra el estado en el que se encuentra el envío de la factura, puede ser Registrada en RFC, Registrada, Contabilizada, Pagada, No registrada o Rechazada.
-   ***Órgano gestor, Unidad tramitadora y Oficina contable***: son los códigos de las unidades administrativas que se configuraron para el tercero de la factura.
-   ***Identificador emisor**:* es el CIF de la organización con la que se envía la factura.
-   ***Estado anulación***: en este campo se registrará el estado de la factura si se solicita su anulación: Anulada, No solicitada anulación, Solicitada anulación, Aceptada anulación o Rechazada anulación.
-   ***Nº factura**:* identificador de la factura en Etendo.

También están visibles los siguientes check que se activan de acuerdo a la situación en la que se encuentre la factura que se envió:

-   ***Fact. Cancelada**:* activo cuando la factura original en Etendo está anulada.
-   ***Fact. Elect**. Cancelada:* activo cuando la factura electrónica enviada fue anulada.
-   ***Error**:* se activa cuando no se puede enviar debido a un error que no ha sido resuelto.
-   ***En Proc. Aut. de Consulta**:* se activa cuando se solicita la anulación de una factura electrónica enviada.
-   ***En Proc. Aut. de Facturación**:* se activa cuando se envía una factura electrónica pero aún no ha sido recibida.
-   ***Ult. Error Log**:* se activa si el último registro de la bitácora fue error.

Dentro del primer grupo de campos se encuentran ciertos campos relacionados a la obligatoriedad del envío de la facturación:

-   ***Monto de referencia**:* límite configurado en la ventana Montos para facturación electrónica para la fecha de la factura.
-   ***Fecha de referencia**: corresponde a la fecha del registro del monto de referencia.*
-   ***Monto de referencia de tercero**: límite configurado en la solapa Monto Fact. Electr. para la fecha y el tercero de la factura.*
-   ***Fecha de referencia de tercero**: corresponde a la fecha del registro del monto de referencia de tercero.*
-   ***Obligatoria**:* activo cuando el monto de la factura **supera** a aquel configurado en la ventana Montos para facturación electrónica como límite mínimo para el envío de facturación para la fecha de la factura.
-   ***Para Fact. Electr.**:* cuando el monto de la factura (para una fecha determinada) es **mayor** al definido como monto de referencia para el tercero de la factura (en la solapa Monto Fact. Elect. en la ventana Tercero) y/o superior al registrado en la ventana Montos para facturación electrónica.

![](/docs/assets/drive/vNgH90IfboKR89trOO1j_1K2HXAJVbfOZwqGO72Fl12ij-e_bjkp-3GNdMvjtr41-ouQf6Dv9DIMEVOUCOnENsWeOLeOVErnyUsR6CXnNp-a8lLBKTW1a11kvOxpBrCMb49WuJoltjhCi2gMq9tShli7HuyG0u3T0UdhiBV3ZrnGtKgWhbbOSAj2XXcIjQ.png)

En esta ventana se pueden realizar las siguientes acciones sobre las facturas que necesiten enviar:

![](/docs/assets/drive/Lp4Z4YMj79XBb240n5YDd0fH6Lwtjsv5O-KLaEdaQd0VTnacW8k9ZOzdFWbFaTBTQLjKYNMFH53aDnXte69Bs80ECa34P26twRHR4TeoKJEJQsjPc3J2LTDrYX39dXf2ngqBZnVxn92hJwJb20KCgCiXA_v0uwAkeAvY1CHPFIk9gvlgI1O_vw_x1cKcFw.png)  Muestra la vista previa de la factura electrónica en formato HTML.

![](/docs/assets/drive/0BysTo2gaoV7VghVbMeQ2oG3wvq_c5MeQ9M_UBitHR2J3QwROUdQYdOlh1_-L3kXyAvVo8zAfTXL5HSs0kWVMiuCVzoX5llAf3cciXAmkKaxPuQU34V2wzPu73AKVFim7wtYqNgRrdr20zdiOiGXyWuENUYf8Yi6SXEsHrdDCmUU9sPFMOXw3_HXfEXpZw.png)  Envía las facturas al organismo recaudador de los registros seleccionados.

![](/docs/assets/drive/3aNFTBpuhHK92Ep7kO1U2krH8tEPdI4e650Prg169wxnHA4qGPxtqRrYeDdBf0cxyvq_4iNzXvhDDVBBzhOtXnOTQm2nlvBGMZWXokq5MBSC2I_YvG1noz8N0n5oTop8j1ZLt-8VQnUF_39KGwn-EksPx432xwVbm9pwd0eUKd9CTyAAsrT9SZu70xmkOw.png)  Descarga una vista previa del archivo XML que se enviará.

![](/docs/assets/drive/WcZI-j7y2wV1Fvpwk8toKk_fYBdTnvYcH8cjNIkKaIGlpf0cB_z4riJgvobEMR0oKQeDKY7HFC501_NPXP38Xct1LxnGd5NGDQEiAOMW50pPkGXlaVDVE-gCdDxO3C-xSoQ8S2T2rkBiUN2AxruGRiL5UCCn_PRB8_umKIBfgG2aLGXclnvObZpw6yIB-Q.png)  Cancela las facturas electrónicas enviadas de los registros seleccionados. Primero será necesario anular las facturas desde la ventana Factura (cliente) para que se habilite este botón.

![](/docs/assets/drive/QHrU-YCFMIg1RPToFWbFSQXfEfbr2Sclf7slFJdv1BuoTSxm00ZJC5c3exFzGQU_ctsNvLvmPSBnjnBOYvS4XrJUFioKCXhwBacCECq9HTW9qXAAX2gIf6FmU1lQWsG_Z2oI3de6ZCdbH3Oqs-2jVTeOsEKFDdCtcZto0C2omS3n8VZmQbI9RVJBK76NIQ.png)  Consulta el estado de la factura enviada. Crea un nuevo registro en la solapa Bitácora, con el resultado de la consulta.

![](/docs/assets/drive/TikZMLWWL-lRvCmmEv0euSI__lGSx_xTlogxI1cr_2ayQycBOD3vY6oO0QLCSMfhk1AYPYIYab1bPP5rXeccGeldHqIwigoO9q1aL9YmNIQfbKkLkznSM_zBRn7_jqwnDjNIQfdw2O5iPjbbR_nQl9MWotAwK-aGYx02Ea3Vbp-zmXbge29fHwJoItaYLQ.png)  Descarga el archivo XML que se envió al organismo recaudador.

La solapa **Bitácora**, muestra un registro por cada consulta que se realiza a los servidores del gobierno indicando, si lo hubiere, una descripción del error que se devuelve.

En la solapa **Facturas** se podrá visualizar la factura una vez enviada correctamente.

!!! info
    Para la instalacion del modulo de Localizacion Española visite [Marketplace](https://marketplace.etendo.cloud/#/product-details?module=003B475055DD421B9483B5BE15AA48C5). 


## **Configuraciones generales**

Para que el envío de facturas se realice en forma exitosa se deben tener en cuenta las siguientes configuraciones en cada una de las ventanas que se detallan a continuación. A su vez, ciertas configuraciones como las de Organización, Tercero e Impuesto, pueden realizarse directamente en las ventanas que se describieron en el apartado anterior.

-   **Organización**: en la cabecera deberá estar completo el campo Nombre Social. Luego, dentro de la solapa información es necesario que los campos CIF y dirección estén completos (Línea 1ª, Código Postal, Localidad, Región y País). Además, se deben completar en forma *obligatoria* los siguientes campos que corresponden al grupo Facturación electrónica dentro de la misma solapa:
    -   Tipo de persona.
    -   Tipo de residencia y/o extranjería.
    -   Nombre social.
    -   Email para FACe.

Existen otros campos que se deben rellenar en aquellos casos que sea necesario:

-   Identificación del lote: cuando quiera enviarse más de una factura por xml.
-   Días para Consultar Aut.: se utiliza para indicar la cantidad de días que se analizarán para ejecutar el proceso de *consulta de estado de la facturación enviada*.
-   Días para Facturar Aut.: se utiliza para indicar la cantidad de días que se analizarán para ejecutar el proceso de *envío de facturación*.

![](/docs/assets/drive/ReW_UoP2rnPYSKdGIRpizOTnwmLydtYI9GLohSPrbiBtnz3ksQoJCzRojOInz62DKBNNgzXNSc8L9xtIzlS5hOnkCLrWy-MrUUFd4kHZf4SE_-E0vGZA4BpPbDqQZuLEKsurbCb8YVRarJJlgZRp3RDbUs-BU6lN552bBpQpGL-vMBhn2-avwzMfl9nlxg.png)

-   **Terceros**: para cada tercero con el que se quiera enviar facturación en forma electrónica la solapa dirección debe estar completa y, en la cabecera se deberá tener activo el check “**De la administración pública (AAPP)**” dentro del grupo Facturación Electrónica. Una vez activo, se habilitarán nuevos campos a completar de acuerdo al tercero: 
    -   Tipo de persona.
    -   Crédito Límite.
    -   Tipo de residencia y/o extranjería.
    -   Moneda (se rellena automáticamente).
    -   Punto de entrada.

![](/docs/assets/drive/cITmK6BO_cXSbC-n4KyRCNsPFvu5hR8rdZaLq-irCXMkkA90fpQP5dbvBw6l2bOUF1NsNxGd30qRezeJOEvGZCeoI9hg23Z9AWBirP0916c1bjzmdC9jgiIOGaW5y_vJMPOhvG-wNN1VSTRACc-WcpWwOCAuCxox-jVmCK83HUKEGJIRxh5d356pSzXoEA.png)

Dentro de esta misma ventana se pueden configurar las Unidades tramitadoras que  corresponden a cada tercero, accediendo a la solapa Unidades Tramitadoras:

![](/docs/assets/drive/2UyUlXfvrg24KKR24cwoieio8DD7xjy9uhUR9dgtoNl70zkl3Shdb7p0VijcaaDbQCygNYQLX6CicVTE80Lb3xZo_y9YAX0TOgH7Kiqwg0fnziCsWrEQKTioDnFzaKiR8nBSqtgWdnL5rp0CryeUXsuOx_0eftYnRWPA-lWbvdSZamLxBKxbgvNlPOZxSg.png)

La solapa **Montos para facturación electrónica** permitirá configurar el *monto límite mínimo para un tercero* en particular, a partir del cual se deberán enviar las facturas en forma electrónica en forma obligatoria. 
!!! info
    Esta configuración la realiza el usuario de acuerdo a las preferencias para cada tercero y deberá *_siempre ser inferior al monto configurado en la ventana Monto Fact. Electr._* como general para todas las facturas, ya que este es el importe definido por ley para el envío obligatorio (actualmente 5.000 €). Caso contrario, no solo se estará infringiendo la ley, sino que además se estará provocando una inconsistencia que luego generará consecuencias en el envío por background de la facturación.


![](/docs/assets/drive/ID0zd2gG_pvmoSpXoQNpvZ_4_0wRzl1FKZaGiAV3QeKSUsWNCL0Ov4kWhNsC_qdQTEUv-LhvnxHvCMKeTEOho2RMB5T1Ek5JUecUcC1qSsw_b2xLf9p9gqOIDHo_LDp0kVZLU_sN9tUmKz1f69jCBBrF7MnET2Lh6MfF0p4zbyl4TNbmZ4Wq95tb6-n1Gw.png)

-   **Rango de impuesto**: por cada impuesto que se incluya en las facturas que se envíen, se debe configurar el código de la FACe que corresponda. Para esto, existe una lista desplegable dentro del grupo Facturación electrónica en la cabecera de cada impuesto.

![](/docs/assets/drive/4vsqfahI8mYWLozqfE2HKV5NkxSUabfa8kV4nyLTLYs0Zbk3tlPasGxzpqyvnldVFoFxXDS6eNrOH4BuObsoo8k9XZWUfL7Kvs9tdUmXf4O9kMAIb_XOsgsSpAP_AUTq7OZnS23thGvElfSoaxl0HbZnXwvGPx2Wt91Eh564OzJk_p0TdsDBNE1LohcOqg.png)

-   **Método de pago**: similar a la configuración del impuesto, se deberá seleccionar el código de la FACe que corresponda al tipo de método de pago.

![](/docs/assets/drive/CFM2a8xEUEkaLvYOE9d3teiseJcSCUpQtTctwJjLBIZ5yFxUIyXv1Tzf0NA21eL4QMzjG_aLYM_F1ApoLZ0D-r4oN-tT0FI_NDxlU3PZsovb5JE3AJoTftufa3dTmlhmyvCQGkLA2mf3yqYllK5p8vWMA9Zef3nAoGijnEd70NZgRixFFaDouoNcZDTyUw.png)

## **Descripción de procesos en background**

-   **Proceso de actualización de Unidades tramitadoras:** permite actualizar las unidades tramitadoras que corresponden a cada punto de entrada habilitado para la recepción de las facturas.

Se puede actualizar utilizando el botón ![](/docs/assets/drive/ErZpP5BrhJ547pnsT6tST3iALUMPX0pbrrGphcnvnuxzgGcGvme8fIoHCxH89k-kwGkPp7cs0O8Vi7-7WNJC4HuJ-1jMhEy414O5_Y_Y0Xr8Gerz6p0u-5VsCjZffvPYpAAdlOO6MC03fsyURXWdAhjNy7GaIf4WqGGpIj_NKuaLHxFNaMdqmHBZaS8guQ.png) ubicado en la parte superior de la ventana Puntos de entrada.

-   **Proceso en background de envío de Facturación Electrónica**: permite el envío de las facturas que se encuentran completadas y que tienen el check “Para Fact. Electr.”, es decir, aquellas facturas para las que se le ha configurado a su tercero un monto mínimo límite a partir del cual es obligatorio el envío de su facturación en forma electrónica.
-   **Proceso en background de consulta de Facturación Electrónica**: permite consultar el estado de transmisión de una factura que ya ha sido enviada en forma electrónica. Este proceso consulta automáticamente aquellas facturas que tengan el estado Pagada, Rechazada o Anulada.

## **Envío de facturación**

Existen dos formas de enviar la facturación electrónica:

-   En forma manual desde la ventana Facturas Electrónicas.
-   En forma automática, programando el “Proceso de Background Facturación Electrónica“.

A continuación se enumeran los pasos a seguir para el envío exitoso de la facturación:

**Envío Manual:**

1.  Se podrán enviar aquellas facturas completas que tengan realizadas las configuraciones que se desarrollaron en el apartado anterior. También será necesario seleccionar de la lista desplegable la Unidad tramitadora con la que se quiere enviar la factura (en la ventana Factura cliente):

![](/docs/assets/drive/dmU6sYDFWBBQLRql4yAVoPRgX-5FuppoXVZ1JupKA2_K0IXVpPXrGZs1dI2ayE3S4yvyMfElognUImThgvpJ00sGgz7BMUkcuy3nkEmhA0js914PTqqt4yW-fC29SpKweVIxlsPAh_QmUV6zxeBnzkel5j9WCv1w2CDjNVGfuyNHG_RGvAnda2J1ILKufw.png)

2\. En la ventana Facturas Electrónicas, se selecciona el registro con la factura que se quiera enviar y con el botón ![](/docs/assets/drive/0BysTo2gaoV7VghVbMeQ2oG3wvq_c5MeQ9M_UBitHR2J3QwROUdQYdOlh1_-L3kXyAvVo8zAfTXL5HSs0kWVMiuCVzoX5llAf3cciXAmkKaxPuQU34V2wzPu73AKVFim7wtYqNgRrdr20zdiOiGXyWuENUYf8Yi6SXEsHrdDCmUU9sPFMOXw3_HXfEXpZw.png) se procede al envío.

3\. Si el envío se realiza en forma exitosa, es decir sin errores, se muestra el siguiente mensaje:

![](/docs/assets/drive/eZ4-N7W3lKi8wst3giaLSOurJ5AGw8yX8bzpjkLueHQEKsebgs-kj4Vu3AjjnStqIys1Bp-9n8jaFIphFqYvL4Wp5A0c_Tlvt0jt7jN3fADGpfHe1-MUcPBOt-6-3G6-WpItbOQ1Mqr59eu_fj70zQhl_DKagXgbhvuR94eBwEcsN_IpnB05mrgaLK9Xow.png)

En el caso contrario, se devuelve un mensaje similar al siguiente indicando el error. 

![](/docs/assets/drive/LwJKz9A7crKDtMoeQzyVGi8LQTmVqm0F_5b2h2UXqLQ-ijHP-A2nVYJIBgMj-J-hhk1rQBXV2q0hqUGuhqFnyCDWP-IkCX7_sycovKxVzLrTBteHmez_Wn0wLVujQ3oI_8MaP8VZqz7Qf2BqrU91_7vB3x9UxbuEdWi7oV-rW983ypylFOkJ0OOdhaPcYg.png)

!!! info
    También estará disponible con mayor detalle en la solapa Bitácora. 


4\. Con el botón ![](/docs/assets/drive/Lp4Z4YMj79XBb240n5YDd0fH6Lwtjsv5O-KLaEdaQd0VTnacW8k9ZOzdFWbFaTBTQLjKYNMFH53aDnXte69Bs80ECa34P26twRHR4TeoKJEJQsjPc3J2LTDrYX39dXf2ngqBZnVxn92hJwJb20KCgCiXA_v0uwAkeAvY1CHPFIk9gvlgI1O_vw_x1cKcFw.png) se puede consultar el estado de la tramitación y se generará un nuevo registro en la solapa Bitácora con el detalle de la consulta.

**Envío automático:**

Para programar el envío automático de facturas electrónicas, se deben realizar los siguientes pasos:

1.  Ventana Organización: debe estar completo el campo **Días para Facturar Aut.**, que indica la cantidad de días hacia atrás que se analizarán desde la fecha en la que se ejecutara el proceso de facturación automática.

![](/docs/assets/drive/IBma6Op33GRM5osmO6zz4Zk8Wvo3YJs1zGrHewBdALcORRWqzVT-NlvknkFzClGR-UbvsYKUH1DHgIqkfSn0bHaBCAps2Qr3TBgK8KTPr1TV5g8ybMxJFjt5DgR_rAdyhdM-n-LlQBIhZ9wGHoWOnNSMkk3MgfwWw1Ai4M2K8gZY6jNh1octE0CddwOvlw.png)

2\. Ventana Procesamiento de peticiones: se crea un nuevo registro y se programa el proceso *Proceso de Background Facturación Electrónica*.

!!! info
    De la misma forma se deberá programar el *Proceso de Background Consulta de Facturación Electrónica*, pero teniendo en cuenta el campo **Días para Consultar Aut**.
