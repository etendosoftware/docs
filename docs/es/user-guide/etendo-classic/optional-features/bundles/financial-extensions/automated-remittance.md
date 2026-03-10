---
tags:
    - Remesas automatizadas
    - Contabilidad
    - Financiero
    - Protesto de remesas
---

# Remesas automatizadas

:octicons-package-16: Paquete Java: `com.etendoerp.automated.remittance` 

## Visión general

Esta sección describe el módulo de Remesas automatizadas incluido en el bundle Etendo Financial Extensions.

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el bundle Financial Extensions. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).


Esta funcionalidad permite al usuario procesar y protestar remesas automáticamente. Para comprender mejor esta sección, es necesario visitar la [Guía de usuario de Remesas](../../../basic-features/financial-management/receivables-and-payables/transactions.md#remittance).

!!!important
    Esta funcionalidad depende del módulo `org.openbravo.module.remittance` en la versión `3.15.0` o superior. En caso de instalar el bundle Financial Extensions, las dependencias se gestionan automáticamente.

## Configuración

Para poder utilizar esta funcionalidad, es necesario instalar el conjunto de datos de Remesas automatizadas antes de utilizar la ventana Remesas.

Para ello, vaya a la ventana [Gestión del módulo de Empresa](../../../../../user-guide/etendo-classic/basic-features/general-setup/enterprise-model/enterprise-module-management.md) y seleccione el conjunto de datos correspondiente como se muestra a continuación. Esto incluye el método de pago necesario para utilizarse en la funcionalidad de protesto, explicada a continuación.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/automated-protest-remittance/Enterprise%20Module%20Management.png)

## Proceso de remesas automatizadas

Esta funcionalidad permite el procesamiento automático de remesas. Esta funcionalidad se activa seleccionando la casilla de verificación Procesar automáticamente en la cabecera de la ventana [Remesas](../../../basic-features/financial-management/receivables-and-payables/transactions.md#remittance).


1. Activación: Para activar el procesamiento automatizado, marque la casilla de verificación Procesamiento automatizado en la cabecera de Remesas. Si se prefiere el procesamiento manual, mantenga esta opción desmarcada.

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/automated-protest-remittance/process-automated-check.png)

    Una vez utilizado el botón Procesar, Etendo crea automáticamente las líneas correspondientes en las solapas Instrucciones bancarias y Liquidado, tal y como se explica a continuación.

2. Generación de instrucciones bancarias: El sistema genera automáticamente las Instrucciones bancarias correspondientes.

3. Procesamiento de fecha: Las líneas de la remesa se procesarán con la fecha de las facturas o pedidos correspondientes. Estas líneas pueden encontrarse en la solapa Liquidado. Si es necesario, esta fecha puede modificarse manualmente en el campo correspondiente de la solapa Liquidado, tras el procesamiento de la remesa.

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/automated-protest-remittance/remittance.png)

!!!note
    Los pasos de selección, agrupación y procesamiento de facturas ya existían; lo nuevo es la automatización del procesamiento de remesas mediante la selección de la casilla de verificación Procesar automáticamente.

## Protesto de remesas automatizadas

El botón Protestar remesa permite el protesto automático de remesas. Esta función facilita la gestión de protestos y la reliquidación de remesas. Este protesto automático crea un pago negativo, por lo que no es necesario utilizar la ventana Liquidar/Protestar remesa ni añadir un pago manualmente.

1. Selección de remesa: En la solapa Liquidado, de la ventana Remesas, seleccione la remesa que se va a protestar.

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/automated-protest-remittance/remittance-selection.png)

2. Generación de devolución: Al pulsar el botón Protestar remesa y seleccionar una fecha de devolución, el sistema generará automáticamente la devolución de la remesa.

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/automated-protest-remittance/protest-generation.png)

3. Pago negativo de factura: La devolución incluirá la generación de un pago negativo de la factura a devolver, permitiendo que la remesa pueda liquidarse de nuevo en el futuro.

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/automated-protest-remittance/negative-invoice-payment.png)

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/automated-protest-remittance/negative.png)

---
Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L](https://etendo.software){target="_blank"}.