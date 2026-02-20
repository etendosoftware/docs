---
title: Verifactu
tags:
    - Localización Española
    - Veri*Factu
    - Verifactu
    - Facturación Electrónica
status: new
---

# Verifactu

:octicons-package-16: Paquete Java: `com.etendoerp.verifactu`

:octicons-package-16: Paquete Java: `com.etendoerp.verifactu.template`
## Introducción

<iframe width="560" height="315" src="https://www.youtube.com/embed/bOCK7A1cFms?si=VAfNntVPqse58GnU" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Las funcionalidades de *Verifactu* en Etendo proporcionan una solución integral para el cumplimiento de los nuevos requisitos establecidos por la **Agencia Estatal de Administración Tributaria Española** en materia de facturación. Su objetivo es garantizar la transparencia, prevenir el fraude fiscal y asegurar la integridad y trazabilidad de las facturas emitidas por empresas y profesionales.

*Veri\*Factu* forma parte del marco legal derivado del **Real Decreto 1007/2023** y la **Ley Antifraude (Ley 11/2021)**, que establecen la obligatoriedad de utilizar sistemas informáticos de facturación que cumplan con criterios técnicos específicos. Permite el envío automático y en tiempo real de los registros de facturación a la Agencia Tributaria.

Este módulo permite a Etendo automatizar procesos clave como la generación, el registro estructurado y el envío electrónico de facturas, cumpliendo con los estándares de *Verifactu*. El sistema garantiza la inalterabilidad de los datos, la inclusión de códigos QR y la generación de eventos asociados, aportando total trazabilidad a cada operación registrada.

!!! warning
    Al utilizar este módulo, **se restringirán** las siguientes funcionalidades:

    - Reactivación de facturas.
    - Anulación de facturas.
    - Eliminación de facturas, pedidos o albaranes (incluso en estado borrador).
    - Modificación del Rango de un impuesto ya creado.
    - Configuración simultánea para un mismo emisor de:
        - *Verifactu* + *SII*.
        - *Verifactu* + *TBAI*.
        - La combinación *SII* + *TBAI* **sí está permitida**.
    - Eliminación de registros de facturación *Verifactu* y de su respuesta asociada (deben conservarse copias de seguridad de los registros y de las *llamadas/respuestas XML* durante el plazo legal correspondiente).
## Descripción del módulo

El módulo permite:

- Generar automáticamente los archivos `XML` de registro de facturación al emitir una factura, conforme a la estructura exigida por la AEAT.
- Enviar estos archivos en tiempo real a la Agencia Tributaria.
- Recibir las respuestas electrónicas de la AEAT con el resultado del procesamiento.
- Incluir en las facturas los códigos QR y la marca *Verifactu* exigidos por la normativa.
- Consultar un historial detallado de todos los registros enviados, incluyendo sus estados de validación por parte de la AEAT.

La implementación cubre:

1. **Cumplimiento** técnico de los requisitos de *Verifactu*.  
2. **Automatización** del envío de registros desde Etendo a la AEAT.  
3. **Integración** con la generación de facturas en Etendo.  
4. **Trazabilidad** y **control** del proceso de facturación, con registro de errores, rechazos y confirmaciones.  
5. **Generación** de códigos QR compatibles con el visor de la AEAT.
## Contenido del módulo

### Ventanas nuevas

- [Configuración Verifactu](#configuracion-verifactu): permite configurar emisores, seleccionar el impuesto aplicable (IVA, IPSI o IGIC) y monitorear incidencias en los envíos.

- [Monitor Verifactu](#monitor-verifactu): permite consultar el estado de las facturas enviadas, así como identificar aquellas que han quedado inválidas por no superar validaciones previas.

- [Consulta Facturas Verifactu](#consulta-facturas-verifactu): permite obtener un informe de las facturas enviadas a *Verifactu*, consultando la información directamente desde la Agencia Tributaria.

### Nuevos campos

Se añaden campos y pestañas específicas de *Verifactu* en las ventanas **Factura (Cliente)**, **Rango de Impuesto**, **Tipo de Documento**, **Pedido de Venta**.
## Configuration

!!! info
    It is recommended that the following configurations be carried out by a user with the **administrator** role, as they require technical adjustments.

### Verifactu Configuration
:material-menu: `Application` > `Financial Management` > `Verifactu` > `Verifactu Configuration`

In the **Verifactu Configuration** window, you define who will act as the **invoice issuer** and with which **tax the invoices will be generated**. In this case, **each legal organization that is created will be responsible for issuing**, so it is necessary to configure these fields so that the system can issue invoices with the correct tax data and the corresponding tax treatment.

- **Organization**: issuing legal entity.
- **Applicable Tax**: VAT, IPSI or IGIC.
- **Default QR**: if selected, a predefined implementation will be used. Otherwise, the report must be customized following [this specification](https://www.agenciatributaria.es/static_files/AEAT_Desarrolladores/EEDD/IVA/VERI-FACTU/DetalleEspecificacTecnCodigoQRfactura.pdf){target="_blank"}.

In addition, there is a **Monitoring** section where the **System Start** and **System Stop** fields indicate, respectively, when the environment began to be operational and when it stopped being so. This information is useful to accurately identify the periods in which **Verifactu was available** and those in which **it was not**.

On the other hand, the **Incident Detail** field will be completed when a submission presents an incident caused by factors external to the content of the invoice, such as lack of internet connection, server errors, timeouts, or other infrastructure or communication issues.

  ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/verifactu/configuracion-verifactu.png)


### Digital Certificate
:material-menu: `Application` > `General Setup` > `Organization` > `Organization`

!!! info
    For more information on how to obtain a digital certificate from the FNMT, [you can follow this guide](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/firma-digital-sistema-clave-pin-tecnica/informacion-pasos-obtencion-certificado-electronico.html){target="_blank"}

In order to issue electronic invoices through the *Verifactu* system, it is essential to have a digital certificate. This certificate ensures the authenticity of the issuer’s identity and guarantees that the transmitted data has not been altered during submission. Follow the steps below to correctly configure your **Digital Certificate**:

1. Access the **Organization** window

2. **Select the Legal Organization**: Choose the legal organization that will be responsible for issuing electronic invoices.

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/verifactu/certificado.png)

3. Click the **Add Digital Certificate** button.
    
4. **Upload the Certificate**: In the process, you will be able to upload your digital certificate by entering the corresponding password.

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/verifactu/certificado-contrasena.png)

5. **Save the configuration**: By pressing the **Done** button, the system will save the digital certificate information in the **Digital Certificate** tab.
    
    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/verifactu/certificado-cargado.png)

    Once these steps are completed, the digital certificate will be correctly configured and ready to be used for issuing electronic invoices.

### Tax Range
:material-menu: `Application` > `Financial Management` > `Accounting` > `Setup` > `Tax Range`

In the **Tax Range** window, the required information must be completed for each tax used when issuing invoices. This data is necessary to correctly classify taxes according to the applicable regime and the type of transaction.

It is recommended to consult your tax advisor to determine the applicable regime, as it may vary depending on the activity carried out.

- For VAT as applicable tax: **Special VAT Regime**

    | VALUES | DESCRIPTION OF THE REGIME KEY FOR BREAKDOWNS WHERE THE APPLICABLE TAX IS VAT |
    |---|---|
    | 01 | General regime operation. |
    | 02 | Export. |
    | 03 | Transactions to which the special regime for second-hand goods, works of art, antiques and collectors’ items applies. |
    | 04 | Special regime for investment gold. |
    | 05 | Special regime for travel agencies. |
    | 06 | Special regime for group of entities in VAT (Advanced Level) |
    | 07 | Special regime for cash accounting criterion. |
    | 08 | Transactions subject to IPSI / IGIC (Tax on Production, Services and Importation / Canary Islands General Indirect Tax). |
    | 09 | Invoicing of services provided by travel agencies acting as intermediaries in the name and on behalf of others<br>(D.A.4ª RD1619/2012) |
    | 10 | Collections on behalf of third parties of professional fees or rights derived from industrial property, authorship or others on behalf of their members, associates or registered professionals carried out by companies, associations, professional bodies or other entities performing these collection functions. |
    | 11 | Lease transactions for business premises. |
    | 14 | Invoice with VAT pending accrual in work certifications whose recipient is a Public Administration. |
    | 15 | Invoice with VAT pending accrual in successive tract operations. |
    | 17 | Transaction covered by one of the regimes provided for in Chapter XI of Title IX (OSS and IOSS) |
    | 18 | Surcharge of equivalence. |
    | 19 | Transactions of activities included in the Special Regime for Agriculture, Livestock and Fishing (REAGYP) |
    | 20 | Simplified regime |

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/verifactu/regimen-iva.png)


- For IGIC as applicable tax: **Special IGIC Regime**

    | VALUES | DESCRIPTION OF THE REGIME KEY FOR BREAKDOWNS WHERE THE APPLICABLE TAX IS IGIC |
    |---|---|
    | 01 | General regime operation. |
    | 02 | Export. |
    | 03 | Transactions to which the special regime for second-hand goods, works of art, antiques and collectors’ items applies. |
    | 04 | Special regime for investment gold. |
    | 05 | Special regime for travel agencies. |
    | 06 | Special regime for group of entities in IGIC (Advanced Level) |
    | 07 | Special regime for cash accounting criterion. |
    | 08 | Transactions subject to IPSI / VAT (Tax on Production, Services and Importation / Value Added Tax). |
    | 09 | Invoicing of services provided by travel agencies acting as intermediaries in the name and on behalf of others<br>(D.A.4ª RD1619/2012) |
    | 10 | Collections on behalf of third parties of professional fees or rights derived from industrial property, authorship or others on behalf of their members, associates or registered professionals carried out by companies, associations, professional bodies or other entities performing these collection functions. |
    | 11 | Lease transactions for business premises. |
    | 14 | Invoice with IGIC pending accrual in work certifications whose recipient is a Public Administration. |
    | 15 | Invoice with IGIC pending accrual in successive tract operations. |
    | 17 | Special regime for retail trader |
    | 18 | Special regime for small entrepreneur or professional |
    | 19 | Exempt domestic transactions by application of article 25 Law 19/1994 |

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/verifactu/regimen-igic.png)

- For IPSI as applicable tax: **Special IPSI Regime**

    | VALUES | DESCRIPTION OF THE REGIME KEY FOR BREAKDOWNS WHERE THE APPLICABLE TAX IS IPSI |
    |---|---|
    | 01 | General regime operation. |
    | 08 | Transactions subject to IGIC / VAT (Canary Islands General Indirect Tax / Value Added Tax). |
    | 11 | Lease transactions for business premises. |
    | 18 | Transactions included in article 73.4 and 73.5 of the IPSI tax ordinance (Ceuta only). |
    | 19 | Exempt domestic transactions. |
    | 20 | Objective estimation regime. |

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/verifactu/regimen-ipsi.png)


- If no tax applies: **Non-Subject Cause**
    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/verifactu/causa-no-sujecion.png)

- If exempt: **Exemption Cause**

    | VALUES | DESCRIPTION |
    |---|---|
    | E1 | Exempt under article 20 |
    | E2 | Exempt under article 21 |
    | E3 | Exempt under article 22 |
    | E4 | Exempt under articles 23 and 24 |
    | E5 | Exempt under article 25 |
    | E6 | Exempt for others |


    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/verifactu/causa-exencion.png)

!!! note
    If equivalence surcharges are used, it is enough to complete the field in the main tax. For example, for the tax **Deliveries VAT+RE 21+5.2%**, which includes the sub-taxes **Deliveries VAT+RE 21+5.2% (+21%)** and **Deliveries VAT+RE 21+5.2% (+5.2%)**, it is only necessary to fill in the field in the tax Deliveries **VAT+RE 21+5.2% (+21%)**.


### Configuration for Processes that Generate Invoices
:material-menu: `Application` > `Financial Management` > `Accounting` > `Setup` > `Document Type`

To send to *Verifactu* the invoices generated from other processes (for example, processes that **create invoices directly in Completed status**), you must **configure the Document Type beforehand**.


In the **Document Type** window, in the document that will be assigned to the invoice, the fields in the **Verifactu** section must be filled in.  
The following fields are **mandatory**:

- **Invoice Type**
- **Operation Description**

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/verifactu/tipo-documento.png)

The values entered in this configuration will be used to generate the invoicing record that will later be sent to *Verifactu*.

### Settings for Corrective Invoices by Substitution or F3
With the new invoicing procedures introduced by the AEAT, it is no longer possible to reactivate or modify an invoice that has already been issued (completed and sent to *Verifactu*). To correct errors in a previously issued invoice, the concept of a **Corrective Invoice** is introduced, which is issued specifically to correct incidents or rectify data from a previous invoice.
Therefore, using this functionality requires certain configuration settings to ensure that the recorded and submitted information is correct.

### Accounting Settings

Issuing a substitute invoice requires adjusting accounting entries, since the only accounting data that must be preserved are those corresponding to the invoice created to replace the previous one.

To do this, an accounting template has been developed that:

- Detects the related original invoice.
- Copies its accounting entries.
- Generates reverse entries (swapping Debit and Credit), canceling the original accounting impact.

### Accounting Template Configuration
:material-menu: `Application` > `Financial Management` > `Accounting` > `Setup` > `Accounting Templates`

In the **Accounting Templates** window, create a record with the following values:

- **Entity**: Current Client
- **Organization**: Root Organization
- **Table**: `C_Invoice`
- **Name**: `Verifactu Accounting Template`
- **Java Class**: `com.etendoerp.verifactu.accounting.DocInvoiceVerifactu`

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/verifactu/plantilla-contabilidad.png)

!!! note
    If the system already has an accounting template, you must apply the changes that were in your template to the *Verifactu* accounting template, since it is only possible to have a single template configured.

### Accounting Schema Configuration
:material-menu: `Application` > `Financial Management` > `Accounting` > `Setup` > `Accounting Schema`

In the **Accounting Schema** window, in the **Tables to Post** tab, locate the `Invoice` table and link the created template in the **Accounting Template** field (the field may be hidden by application logic).

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/verifactu/esquema-contable.png)

### Zero Collection

When the **original invoice** has not been collected, but has a defined **payment plan**, upon completing the **substitute invoice** the system automatically generates a **zero collection** on the original invoice.

This collection is recorded on the **original invoice** using the **accounting account associated with the business partner**, in order to insert the necessary **accounting concept** and leave the original invoice without an active payment plan. In this way, the **only active payment plan** is linked to the **new substitute invoice**.

To configure this **accounting concept**, go to the window :material-menu: `Application` > `Financial Management` > `Accounting` > `Setup` > `Accounting Concept`, select the legal organization used and, in the **Accounting** tab, add a record with the **accounting schema** and finally complete the `Credit account` field with the **account associated with the business partner** used.
    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/verifactu/concepto-contable.png)


This account is the one shown in the window :material-menu: `Application` > `Master Data` > `Business Partner`, subtab **Customer Accounting**, in the `Customer Receipts` field of the accounting schema used.
    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/verifactu/tercero.png)
## Proceso de Envío a Verifactu

A continuación se detallan los pasos necesarios para que una factura se dé de alta en *Verifactu*.  

!!! note 
    Es importante aclarar que únicamente se envían a *Verifactu* las **facturas de venta**, facturas emitidas desde la ventana **Factura (Cliente)**.

### Creación de Factura Manualmente

Para iniciar el proceso, cree una factura de venta utilizando una organización que esté incluida en el árbol de organizaciones de aquella que ha sido configurada en la ventana :material-menu: `Aplicación` > `Gestión Financiera` > `Verifactu` > `Configuración Verifactu`.

Debe completar los siguientes campos obligatorios en la Factura:

  ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/verifactu/sales-invoice-normal.png)

- **Tipo de Factura**

    | VALORES | DESCRIPCIÓN |
    |---|---|
    | F1 | Factura (art. 6, 7.2 y 7.3 del RD 1619/2012) |
    | F2 | Factura simplificada y Facturas sin identificación del destinatario art. 6.1.d) RD 1619/2012 |
    | F3 | Factura emitida en sustitución de facturas simplificadas facturadas y declaradas |
    | R1 | Factura Rectificativa (Error fundado en derecho y Art. 80 Uno Dos y Seis LIVA) |
    | R2 | Factura Rectificativa (Art. 80.3) |
    | R3 | Factura Rectificativa (Art. 80.4) |
    | R4 | Factura Rectificativa (Resto) |
    | R5 | Factura Rectificativa en facturas simplificadas |

- **Descripción de la Operación**: Fecha en la que se ha realizado la operación.
- **Fecha de la Operación**: Descripción del objeto de la factura.

!!! note
    Si para un **Tipo de Documento** se emiten siempre facturas del **mismo tipo** o con la **misma descripción**, este proceso puede agilizarse rellenando una única vez estos campos en la ventana **Tipo de Documento**, correspondiente al documento utilizado por la factura.  

    Así, cada vez que se cree una factura con este documento, se rellenarán automáticamente los campos **Tipo de Factura** y **Descripción de la Operación**.

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/verifactu/tipo-documento.png)


Opcionalmente, puede completar:

- **Referencia Externa**: Dato adicional de contenido libre con el objetivo de que se pueda asociar opcionalmente información interna del sistema informático de facturación al registro de facturación. Este dato puede ayudar a completar la identificación o calificación de la factura y/o su registro de facturación.
- **Factura Simplificada Art. 7.2 y 7.3**: Indicar cuando se trate de una factura simplificada emitida al amparo de lo previsto en los artículos 7.2 o 7.3 del Real Decreto [1619/2012](https://www.boe.es/buscar/act.php?id=BOE-A-2012-14696){target="_blank"}.
- **FacturaSinIdentifDestinatarioArt61d**: Indicar cuando se trate de una factura completa sin identificación del destinatario, de conformidad con lo dispuesto en el artículo 6.1.d del Real Decreto [1619/2012](https://www.boe.es/buscar/act.php?id=BOE-A-2012-14696){target="_blank"}.

#### Completar Factura de Venta

Al completar la factura:

- Se genera un archivo adjunto con el **Registro de Facturación (RF)**, que será utilizado para dar de **Alta** la factura en *Verifactu*.

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/verifactu/rf-adjunto.png)

- Una vez generado el RF, un proceso automático (no requiere configuración previa y se activa automáticamente al instalar el módulo de *Verifactu*) se encargará de enviarlo a la **Agencia Tributaria**. Por defecto, este proceso se ejecuta cada *60 segundos*.

- El estado del envío puede consultarse en la solapa **Verifactu** de la factura o en la ventana **Monitor Verifactu** refrescando los datos.

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/verifactu/estado-envio-alta.png)

### Creación Automática de Facturas de Venta

Para aquellas facturas de venta en estado **Completado** que se generen desde procesos externos al flujo manual de facturación, el sistema ejecuta automáticamente un proceso interno —habilitado por defecto tras la instalación del módulo *Verifactu* y sin necesidad de configuración previa— que **genera el registro de facturación** y **remite dicho registro de forma inmediata a Verifactu**, utilizando los datos configurados en el **Tipo de Documento**, tal como se describe en la sección [Configuración para Procesos que Generan Facturas](#configuracion-para-procesos-que-generan-facturas).  

!!! example

    1. Se crea un **Pedido de Venta**.
        ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/verifactu/pedido.png)
      
    2. Mediante el proceso **Crear Facturas Desde Pedidos** (o cualquier otro proceso utilizado para la generación de facturas), se genera la **Factura**, la cual tomará los datos configurados en el **Tipo de Documento** utilizado.
        ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/verifactu/crear-factura-desde-pedido.png)

    3. Al quedar la factura en estado **Completado**, se genera el **registro de facturación** y se envía a *Verifactu*.
        ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/verifactu/factura-desde-pedido.png)

!!! warning  
    Es fundamental asegurar el cumplimiento de **todas las validaciones previas necesarias** para que la factura se envíe correctamente a *Verifactu*.  
    En este flujo automático **pueden no aplicarse** validaciones previas desarrolladas, lo que podría provocar el **rechazo** de la factura por parte de *Verifactu*.
## Proceso de Anulación de Factura

Según lo establecido en la normativa vigente (**RD 1007/2023**) y en las directrices de la Agencia Tributaria, el uso del sistema *Verifactu* en entornos de prueba está **restringido exclusivamente a fabricantes de Sistemas Informáticos de Facturación (SIF)** durante sus fases de desarrollo.

Por tanto, los **clientes finales deben operar únicamente en entorno productivo**, lo que implica que **toda factura emitida será tratada como real** y su **registro será enviado automáticamente a la Agencia Tributaria**. El uso del entorno de pruebas de *Verifactu* **no está permitido para entornos de demostración, usuarios finales o actividades de formación**.

En caso de necesitar realizar simulaciones en entorno productivo (por ejemplo, pruebas de funcionamiento o demostraciones), la Agencia Tributaria permite una operativa específica:

- Utilizar **series diferenciadas** (como `PRU-XXXXX`) para identificar las facturas de prueba.
- Añadir textos visibles que indiquen su carácter no real, como **DEMO** o **PRUEBA**.
- Generar de forma obligatoria el **registro de alta y su correspondiente registro de anulación**, enviados ambos a la AEAT.

Etendo implementa esta lógica de forma segura **exclusivamente en entornos de desarrollo**, permitiendo que las facturas se creen y anulen automáticamente como parte del flujo de testeo. **Este comportamiento no se encuentra disponible en entorno productivo**, donde las anulaciones deben gestionarse conforme al procedimiento fiscal establecido.

!!! info
    Para más información, consulte: [FAQs para desarrolladores Verifactu – Agencia Tributaria](https://www.agenciatributaria.es/static_files/AEAT_Desarrolladores/EEDD/IVA/VERI-FACTU/FAQs-Desarrolladores.pdf), apartado 11.
## Tratamiento de Errores en Facturación

Esta sección describe cómo actuar ante errores durante la emisión de facturas o registros de facturación (RF), conforme al *RD 1619/2012* y al *RD 1007/2023*.

### Subsanación

**Sin Factura Rectificativa**

Debe utilizarse cuando el error afecta únicamente al `XML` (registro de facturación) y **no** al contenido de la factura original.

**Ejemplos comunes:**

- Hash incorrecto
- NIF no censado
- Error en el campo **ImporteTotal**

**Acción:**

1. Marcar el **check de Subsanación** en la factura.
2. Corregir los datos que ocasionaron el rechazo o se aceptó con errores.
3. El proceso automático genera un nuevo **Registro de Facturación** de **alta de subsanación** (`Subsanacion = "S"`) y lo enviará nuevamente.

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/verifactu/subsanacion.png)
    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/verifactu/subsanacion-aceptada.png)

    !!! warning
        No debe aplicarse subsanación si el error requiere una **factura rectificativa**, conforme al Reglamento de Facturación (ROF).

### Rectificación

**Con Factura Rectificativa**

Se utiliza cuando:

- El error afecta a elementos **patrimoniales**: base imponible, cuota, tipo de IVA, etc.
- La corrección es obligatoria conforme al *RD 1619/2012 (Reglamento de Facturación - ROF)*.

!!! info
    Puede consultar ejemplos sobre cómo proceder ante rectificaciones en el siguiente enlace: [Procedimientos de facturación](https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/preguntas-frecuentes/procedimientos-facturacion.html).

#### Claves Verifactu

Para crear una factura rectificativa, debe seleccionarse uno de los siguientes tipos, según corresponda:

- `R1`: Factura rectificativa (error fundado en derecho y Art. 80 Uno, Dos y Seis de la LIVA)
- `R2`: Factura rectificativa (Art. 80.3)
- `R3`: Factura rectificativa (Art. 80.4)
- `R4`: Factura rectificativa (otros casos)
- `R5`: Factura rectificativa en facturas simplificadas

#### Rectificación por diferencias

Se informa únicamente la **variación de importes** con respecto a la factura original.

**Acción:**  
Crear una nueva factura de venta utilizando un **tipo de documento para facturas rectificativas**, en una **serie distinta** a la original. Luego:

1. Seleccionar el tipo de factura correspondiente (`R1` a `R5`).
2. Indicar que se trata de una **Rectificativa por Diferencias**.
3. Enlazar la factura original en la solapa **Factura Rectificativa**.

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/verifactu/factura-rectifica-inc-orig.png)  
    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/verifactu/factura-rectifica-inc-rect.png)  
    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/verifactu/solapa-reversed-diferencia.png)

    !!! example
        En este ejemplo, la factura original declaraba 20 unidades del producto, pero en realidad se debían facturar 21. Por lo tanto, la factura rectificativa incluye una línea adicional por esa unidad faltante.

#### Rectificación por Sustitución

Se reemplaza por completo la factura original.

**Acción:**  
Crear una nueva factura de venta utilizando un **tipo de documento para facturas rectificativas**, en una **serie distinta** a la original. Luego:

1. Seleccionar el tipo de factura correspondiente (`R1` a `R5`).
2. Indicar que se trata de una **Rectificativa por Sustitución**.
3. Enlazar la factura original en la solapa **Factura Rectificativa**.

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/verifactu/factura-rectificativa-sust-orig.png)  
    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/verifactu/factura-rectificativa-sust-rect.png)  
    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/verifactu/contabilidad-ajustada.png)

    !!! example
        En este ejemplo, la factura original incluía un producto incorrecto. Se genera una factura rectificativa **por sustitución** con el producto correcto y se ajusta la contabilidad para reflejar la operación correctamente.

#### Cobros Asociados

Si la factura que se está sustituyendo ya tiene cobros asociados, al enlazarla en la solapa **Factura Rectificativa** se mostrará una advertencia informando que se deben regularizar dichos cobros.

Para tener mayor control, se puede configurar una **alerta** para recibir información sobre facturas sustitutivas que tengan cobros relacionados en sus facturas enlazadas, utilizando la siguiente consulta:

```sql
SELECT DISTINCT ON (cir.C_Invoice_ID)
  cir.C_Invoice_ID AS referencekey_id,
  cir.documentno AS record_id,
  0 AS ad_role_id,
  NULL AS ad_user_id,
  cir.description AS description,
  'Y' AS isActive,
  cir.ad_org_id,
  cir.ad_client_id,
  now() AS created,
  0 AS createdBy,
  now() AS updated,
  0 AS updatedBy
FROM FIN_Payment_Schedule p
JOIN FIN_Payment_ScheduleDetail d 
  ON d.FIN_Payment_Schedule_Invoice = p.FIN_Payment_Schedule_id
JOIN c_invoice_Reverse r 
  ON r.reversed_c_invoice_id = p.C_Invoice_ID
JOIN (
  SELECT DISTINCT AD_ORG_ID, AD_GET_ORG_LE_BU(AD_ORG_ID, 'LE') AS LE_ORG_ID
  FROM c_invoice_reverse
) r_org ON r_org.AD_ORG_ID = r.ad_org_id
JOIN etvfac_verifactu_config v 
  ON v.AD_ORG_ID = r_org.LE_ORG_ID
JOIN C_Invoice ci 
  ON ci.C_Invoice_ID = p.C_Invoice_ID
JOIN C_Invoice cir 
  ON cir.C_Invoice_ID = r.C_Invoice_ID
WHERE p.created >= v.created
  AND ci.issotrx = 'Y'
  AND ci.processed = 'Y'
  AND (cir.em_etvfac_reverseinvtype = 'S' OR cir.em_etvfac_inv_type = 'F3')
  AND EXISTS (
    SELECT 1
    FROM FIN_Payment_ScheduleDetail d2
    WHERE d2.FIN_Payment_Schedule_Invoice = p.FIN_Payment_Schedule_id
      AND d2.em_etvfac_payment_zero = 'N'
      AND d2.FIN_Payment_Detail_ID IS NOT NULL
  )
```

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/verifactu/alerta.png)

!!! note
    Puede consultar más información sobre cómo crear una [Alerta](../../../basic-features/general-setup/application/alert.md)

### Rectificaciones desde Pedidos de Venta o Devolución de Cliente

Se pueden generar **facturas rectificativas** a partir de un **Pedido de Venta** o una **Devolución de Cliente**.

Para hacerlo:

1. Seleccionar un tipo de documento rectificativo, en el **tipo de documento** del pedido o la devolución, seleccionar uno configurado como **rectificativo** (es decir, que tenga marcado el check **Es Rectificativo**).

2. Completar los campos de la sección **Verifactu** del **documento** indicando el **tipo de rectificación** que se usará.

3. Indicar la factura a rectificar. En la sección **Verifactu** del pedido o la devolución, completar el campo **Factura Rectificada** con la **factura original** que se va a rectificar.

Con esta configuración, al **generar la factura** desde el pedido o la devolución, el sistema emitirá automáticamente una **factura rectificativa**, utilizando la configuración definida en el **tipo de documento**.
## Consulta del Estado de Envío de Facturas

Existen dos ventanas desde las cuales es posible consultar el estado de envío de una factura. La principal diferencia entre ambas es que una **obtiene la información almacenada en el sistema**, mientras que la otra realiza la consulta **directamente contra los datos de la Agencia Tributaria**.

### Monitor Verifactu
:material-menu: `Aplicación` > `Gestión Financiera` > `Verifactu` > `Monitor Verifactu`

Permite consultar facturas en estado Rechazada, Parcialmente Aceptada, Aceptada e Inválida. Los tres primeros estados provienen de la AEAT; el último indica errores previos. Se debe pulsar Refrescar Datos para obtener los últimos registros.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/verifactu/monitor-verifactu.png)

### Consulta Facturas Verifactu
:material-menu: `Aplicación` > `Gestión Financiera` > `Verifactu` > `Consulta Facturas Verifactu`

Este proceso permite obtener un **informe detallado de las facturas enviadas a Verifactu**, ofreciendo múltiples opciones de filtrado para facilitar la consulta:

- **Emisor**
- **Período**
- **Número de serie**
- **Fechas**
- **Tercero**

Cuando el resultado de la consulta **supera los 10.000 registros**, es posible aplicar **paginación** utilizando como referencia la **última factura consultada**. Para ello, se deben informar los siguientes campos:

- **Emisor**: Número de Identificación Fiscal (NIF) del obligado a expedir la factura correspondiente al **último registro consultado**.
- **Número de Serie**: Número de serie y número de factura que identifican el **último registro de facturación consultado**.
- **Fecha de Emisión**: Fecha de emisión del **último registro de facturación consultado**.

  ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/verifactu/consulta-facturas.png)
## QR Tributario

Al imprimir una factura, se incorpora un **código QR** diseñado para facilitar la verificación de su emisión y registro ante la Agencia Tributaria (AEAT).

### Beneficios

- **Verificación por el receptor:** permite comprobar si la factura ha sido efectivamente enviada a la AEAT a través del sistema *Verifactu*.
- **Transparencia fiscal:** incrementa la confianza del cliente y contribuye a la prevención del fraude.
- **Integridad documental:** garantiza la inalterabilidad y trazabilidad de las facturas una vez emitidas.

  ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/verifactu/qr-factura.png)

### Resultados Posibles al Escanear el QR

- **Factura encontrada en AEAT:**
  
  ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/verifactu/qr-alta.png)

- **Factura no encontrada en AEAT:**
  
  ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/verifactu/qr-baja.png)
## Desinstalar el Módulo

Para desinstalar el módulo y evitar futuros problemas con registros huérfanos, se debe seguir una secuencia de pasos:

1. Ejecute la siguiente consulta en la base de datos del entorno

  ```
  DELETE FROM c_attachment_conf WHERE c_attachment_method_id = 'E30F0DBF1C164251B6163AA6B078F2AD';
  ```

2. Una vez finalizada correctamente la consulta, [elimine el módulo](../../../../../developer-guide/etendo-classic/developer-tools/etendo-gradle-plugin.md#uninstall-modules-uninstallmodule) siguiendo el procedimiento correspondiente al método de instalación (Sources/JARs)

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.