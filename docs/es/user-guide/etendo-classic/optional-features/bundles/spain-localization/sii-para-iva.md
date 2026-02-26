---
title: Suministro Inmediato de Información (SII) - España
tags:
    - SII
    - Localizacion Española
    - Facturas en RECC
    - Monitor SII
---
## Javapackages 

:octicons-package-16: Javapackage: `org.openbravo.module.sii`

:octicons-package-16: Javapackage: `org.openbravo.module.sii.es_es`

:octicons-package-16: Javapackage: `org.openbravo.module.sii.template`

## **Introducción**

Esta sección explica el contenido del nuevo módulo comercial de Etendo, "**Spain AEAT SII template**", compatible con Etendo 21Q4 y posteriores, bajo licencia comercial "**Etendo Commercial License**".

Este módulo forma parte del bundle (paquete) de Localización para España en su versión para Etendo.

## **Descripción del Módulo**

El módulo "Spain AEAT SII template" permite que las organizaciones puedan gestionar el Impuesto sobre el Valor Añadido y el Impuesto General Indirecto Canario de forma telemática, dentro del marco del proyecto "Suministro Inmediato de Información (SII)".

Este proyecto consiste en la gestión de los Libros registro de IVA a través de la Sede Electrónica de la Agencia Estatal de Administración Tributaria (AEAT), mediante el suministro casi inmediato de los registros de facturación. También se lleva la gestión de IGIC a través de la sede electrónica de la Agencia Tributaria Canaria.

El objetivo final de este trámite online del IVA es proporcionar a las empresas información contrastada sobre su liquidación del IVA, esto es un "borrador" de su declaración del IVA, siempre que los clientes/proveedores de dichas empresas se encuentren también acogidos al SII.

Existen dos posibilidades de envío o alta/modificación de los registros de facturas a SII:

1. por **vía telemática mediante Servicios Web** basados en el intercambio de mensajes XML
2. a través del Formulario de alta web, que la AEAT pone a disposición de los contribuyentes.  
   En este portal se pueden consultar, modificar o dar de baja facturas ya enviadas.

![](../../../../../assets/drive/NcapLkTK0dSBkBKnjlIi4vrC9hJzMZL9ZBod26PJNUbKwihAng4l6CYr99qkDa4oF13Qu117ZzDoaMx3Fxlo1K9Xv65A3akDmFWkF0WYKZlNNU-SN0z9vcHkE8a_dZGxs05lrXEjgsv8EVRPzAQ.png)

Desde Etendo es posible enviar (dar de alta o modificar) los registros de facturas por vía telemática, opción 1 anterior, lo cual se traduce en la generación de un fichero XML con el siguiente contenido por cada envío a SII:

- una **cabecera común** con la información del titular de cada libro, así como la información del ejercicio y periodo en que se registran dichas operaciones
- un **bloque con el contenido de las facturas**.

En definitiva, desde Etendo vamos a poder:

- enviar fácilmente y de forma automática o manual, estos ficheros XML a la AEAT con la información requerida, tanto para el "alta" como para la "modificación" de los registros de facturas.
- recibir los XML de respuesta de la AEAT, respecto de cada tipo de comunicación (alta/modificación)
- consultar en qué estado se encuentra la información ya suministrada a la AEAT, dentro del proceso de contrastación.

Con carácter obligatorio, SII afecta a:

- Inscritos en REDEME (Registro de Devolución Mensual del IVA), salvo renuncia antes de junio de 2017
- Grandes empresas con una facturación superior a 6.101.121,04 €
- Grupos de IVA
- Empresarios o profesionales no establecidos que tengan condición de sujetos pasivos con un periodo de liquidación mensual
- Resto de sujetos pasivos establecidos o no, que voluntariamente quieran acogerse, a través del Modelo 036 de Declaración Censal, que implica autoliquidar el IVA mensualmente, y permanecer el año natural por el que se opte

El nuevo SII conlleva para el contribuyente, entre otras, las siguientes ventajas:

- Reducción de las obligaciones formales, suprimiendo la obligación de presentación de los modelos 347, 340 y 390. Es decir, sólo se tendrá que presentar el Modelo 303 de autoliquidación de IVA
- Obtención de “Datos Fiscales”, ya que en la Sede electrónica dispondrá de un Libro Registro “declarado” y “contrastado” con la información de contraste procedente de terceros que pertenezcan al colectivo de este sistema.  
  Estos datos fiscales serán una útil herramienta de asistencia en la elaboración de la declaración, reduciendo errores y permitiendo una simplificación y una mayor seguridad jurídica.
- Ampliación en diez días del plazo de presentación de las autoliquidaciones periódicas (Modelo 303).

A partir del 1 de julio de 2017 comienza la fase obligatoria de aplicación de este sistema.

Los sujetos pasivos que apliquen el SII desde el 1 de julio de 2017 están obligados a remitir los registros de facturación del primer semestre de 2017 en el periodo desde el 1 de julio al 31 de diciembre de 2017; excepto sujetos en REDEME.

Las facturas de fecha del 1er semestre de 2017 se envían (alta en SII) a través de ficheros XML con un contenido sin las validaciones aplicables a las facturas de fecha desde 1 de julio de 2017.

La AEAT pone a disposición del contribuyente las siguientes URLs que entendemos son de gran utilidad:

- Proyecto SII, en el que se puede encontrar toda la información sobre SII
- Herramienta de cálculo de plazos para la remisión de registros de facturas a SII, que permite calcular la "fecha fin de plazo", el "periodo", y el "ejercicio" para cada tipo de factura en función de su fecha de devengo/recepción y fecha de expedición/registro contable.

## **Contenido del Módulo**

Al instalar este módulo, el usuario podrá comprobar que:

1. Se crea un **nuevo menú** dentro de `Gestión Financiera` > `Sistemas de Facturación`, denominado "**AEAT SII**". Este nuevo menú contiene las siguientes pantallas:
    1. **Configuración SII**, en la que se podrán configurar todos los parámetros necesarios para el envío correcto de los registros de facturas a SII.
    2. **Consulta Facturas SII**, en esta pantalla el usuario tendrá información sobre el estado de cuadre de las facturas enviadas a SII, estado de cuadre recibido de la AEAT.
    3. **Descripciones SII**, en esta pantalla se pueden dar de alta descripciones tipo para las operaciones de compra y venta que realice la organización acogida a SII.
    4. **Conexiones a SII**, nos muestra el estado de todas las conexiones online con la AEAT referenciadas al Código CSV (Código Seguro de Verificación), proporcionado por la AEAT en cada conexión.  
       La AEAT responde con un CSV para cada factura enviada. Si se envía un fichero XML con varias facturas, en el XML de respuesta aparecerá un CSV para cada una de ellas.
    5. **Monitor SII**, desde la que se puede gestionar el estado de las facturas, en relación con su envío a SII, así como realizar envíos de las mismas, según su estado.
2. Se crean **nuevos campos y pestañas relativos a SII** en las ventanas de "**Pedidos y Facturas**", tanto de compra como de venta, con el fin de añadir la información requerida por parte de SII, respecto del "Alta"/"Modificación" del registro de las facturas.
3. Se genera un nuevo campo en la cabecera de las facturas denominado "**Modificada por error registral**", que permite modificar una factura dada ya de alta en SII.
4. Se crea un nuevo campo en la cabecera de las facturas de compra, ventana "Factura (Proveedor)", que permite recoger la "**fecha de registro contable**" al registrar las facturas recibidas.
5. Igualmente, se añaden dos botones en las ventanas de Facturas, tanto de compra como de venta, con el fin de dar de alta (**Alta en SII**) y, si fuera necesario, modificar (**Modificación en SII**) el registro de las facturas.
6. Se generan dos nuevos procesos en la ventana "Procesamiento de Peticiones", denominados "**Proceso de alta en SII**" y "**Proceso de Modificación en SII por error registral**", configurables para cada Organización o "Entidad Legal".  
   Estos nuevos procesos permitirán el alta/modificación masiva de facturas en SII con la cadencia de envío configurada.
## **Configuración**

Para conseguir un uso correcto del módulo SII es muy importante revisar la configuración de **Terceros**, **Productos** e **Impuestos**.

Los productos/servicios tienen que tener correctamente configurado su **Grupo/Categoría de Impuestos** (de producto o servicio).

Los terceros (clientes/proveedores) tienen que tener correctamente configurada su **Categoría de impuestos de Tercero**, si aplica, así como su **CIF/NIF** o **Clave NIF País Residencia**.

Además, los impuestos tienen que estar configurados correctamente, tal y como se explica en el siguiente apartado.

### **Proceso de actualización de Fecha de Operación**

Se recomienda ejecutar el proceso [**Rellenar Fechas de Operación**](./funcionalidades-generales-para-sifs.md#rellenar-fechas-de-operacion) si se está actualizando el módulo a las versiones **1.34.0**, **2.10.0** o posteriores, para actualizar los valores de **Fecha de operación** en facturas previas a la actualización.

### **Configuración de impuestos**

El proyecto SII amplía el contenido de los libros registro de facturas, tal y como se describe a continuación:

- Al enviar el registro de una factura emitida a SII, debemos indicar si esa factura está **Sujeta** a IVA o, por el contrario, se trata de una operación no sujeta a IVA. Igualmente, las operaciones sujetas a IVA se deben diferenciar entre **Exentas** y **No Exentas**.
- Al enviar el registro de una factura recibida a SII, debemos indicar si esa factura es de **Inversión de Sujeto Pasivo** o se trata de una **Adquisición Intracomunitaria de Bienes y/o Servicios**, por ejemplo.

!!! info
    La utilización del módulo **Spain AEAT SII** requiere la versión **1.2.204500** o posterior del módulo de impuestos para España, versión que ya incluye toda la configuración de impuestos requerida para el correcto funcionamiento del envío de registros de factura a SII (alta/modificación).

### **Configuración de terceros**

Todos los terceros, ya sean del tipo **Cliente** o **Proveedor/Acreedor**, deben configurarse en la ventana **Terceros**.

Es muy importante indicar para cada tercero:

- Sus datos de contacto (Nombre Comercial, Nombre Fiscal (Razón Social) o Nombre/Apellidos).
- Su **Clave NIF País Residencia**:

| Código | Descripción | Cuándo se usa | Ejemplo práctico |
|---------|--------------|----------------|------------------|
| **1 - NIF** | Número de Identificación Fiscal español | Cuando el tercero **tiene NIF español** (empresa o persona física residente en España). | Cliente nacional con CIF/NIF. |
| **2 - NOI** | Número de Operador Intracomunitario (número de IVA intracomunitario) | Cuando el tercero es una **empresa de la UE registrada como operador intracomunitario**. | Empresa francesa con VAT `FR123456789`. |
| **3 - Pasaporte** | Documento de identidad personal extranjero | Para **personas físicas extranjeras** que no tienen NIF ni NIE, pero actúan en operaciones sujetas a IVA (casos poco comunes). | Turista extranjero con factura de venta. |
| **4 - Documento oficial de identificación expedido por el país** | Documento fiscal o identificación nacional emitido por otro país | Cuando el tercero **no tiene NIF ni VAT**, pero posee un documento oficial de identificación de su país. | Empresa argentina con CUIT, o persona con DNI argentino. |
| **5 - Certificado de residencia fiscal** | Documento expedido por la administración tributaria extranjera | Se usa en operaciones donde **la residencia fiscal extranjera se acredita con certificado**, por ejemplo, para aplicar convenios de doble imposición. | Empresa con certificado fiscal mexicano. |
| **6 - Otro documento probatorio** | Cualquier otro documento válido para acreditar identidad fiscal | Casos excepcionales donde los anteriores no aplican. | Documentación de ONG u organismo sin identificación estándar. |
| **7 - No censado** | El tercero **no figura en ningún censo fiscal** | Puede usarse en casos de prueba, errores o entidades sin identificación fiscal conocida. | Tercero genérico o error en datos. |

- Su número de identificación fiscal; en el caso del NOI se debería incluir el código ISO de país (por ejemplo, **DE** en el caso de Alemania o **FR** en el caso de Francia).
- La categoría de impuestos de tercero (por ejemplo: Servicios Profesionales Normal, Servicios Profesional Reducido, Autónomo, Recargo de Equivalencia, Revendedores, Régimen Agrario...).
- Su localización (País, provincia, dirección).

**Tercero con NIF no censado**

Se ha creado una nueva **Clave NIF País Residencia**, de valor **7 - No censado**.

Un NIF no censado es un NIF que se ha dado de baja.

Esta nueva clave habrá que configurarla para aquellos terceros con un NIF español válido pero no censado, respecto de los que sea necesario emitir facturas de venta o recibir facturas de compra.

![](../../../../../assets/drive/x32lggVwaGGuN2LEHAcmdiTxQkiGQmJy-C-c1aJE_PtbYs-wEPOGsmF60MeJ-dy-mCyeV5bMha-AGazmPGsm8zJNwXbnA03--9vbE9SM3kBh1NFa23UUVAm58gGNEmODILze76yjrlb8PoaCM2Q.png)

Las facturas con un NIF no censado que se den de alta en SII quedarán en un estado **Aceptado con errores**.

Es muy importante recalcar que la AEAT comprueba en los envíos a SII que el NIF español introducido se corresponda con el nombre/apellidos del tercero persona física (cliente/proveedor).

Si damos de alta un tercero (persona física) con su nombre y un solo apellido, por ejemplo, o con un apellido correcto y el otro no, al enviar la factura de dicho tercero a SII obtendremos un error del tipo: **NIF no identificado**.

Puede comprobar los NIF de sus terceros en la siguiente URL de la AEAT: [Comprobación NIF terceros a efectos censales](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-030/comprobacion-nif-terceros-efectos-censales.html){target="_blank"}.

Respecto de las personas jurídicas o empresas, parece que no se está realizando dicha comprobación (correspondencia Empresa-NIF), pero aun así recomendamos revisar que los terceros estén configurados correctamente.

**Gastos de empleado no declarables**

Los empleados de la organización que incurran en gastos a reembolsar deben darse de alta como terceros de tipo Empleado en la ventana **Terceros**. Se les debe asociar la categoría de impuestos de tercero **No declarable SII**, con el fin de que las facturas de gasto registradas para el reembolso de los gastos no se incluyan en SII.

### **Configuración del Local Arrendado**

Los locales arrendados sujetos a IVA se deben configurar en la ventana **Producto**, con al menos los siguientes datos:

- **Grupo de Impuestos** = IVA Normal
- **Local arrendado**: este campo se debe seleccionar
- **Situación del inmueble**: en este campo se debe seleccionar la opción que corresponda:
  - Locales en el extranjero
  - Referencia catastral válida en el País Vasco o en Navarra
  - Referencia catastral válida, excepto de País Vasco o Navarra
  - Sin referencia catastral
- **Referencia catastral**: en este campo se informa de la referencia catastral del local arrendado.

Dependiendo de si el tercero se configura con la categoría de impuestos de tercero **Arrendamiento con retención** o **Arrendamientos sin retención**, el arrendamiento del local de negocio estará o no sujeto a retención.

### **Configuración Transmisión de Bienes Inmuebles**

Los bienes inmuebles se configuran en la ventana **Producto**, asociándolos la categoría de impuestos **IVA Normal B. Inmuebles**, por ejemplo.

### **Configuración SII**

:material-menu: `Aplicación` > `Gestión Financiera` > `Sistemas de Facturación` > `Suministro Inmediato de Información (SII)` > `Configuración SII`

En la ventana **Configuración SII** se configuran todos los parámetros necesarios para un correcto envío de registros de facturas a SII (alta/modificación).

![](../../../../../assets/drive/PUUxVQZw1yZL9b2ewXHB-XVmzsLyPo5faDW1aeCsJFwhbChyd9ruI4NLYICeHXrV48LcMdddkTCLen33qEYscOjGen7klkPxS8qHfCLTiL9IlOByRZvbjg9lRVFUsnmjV3Tu-DwuITRpXYEC6lo.png)

Tal y como se muestra en la imagen anterior, los parámetros de configuración de SII son los siguientes:

- **Organización**: organización (entidad legal) para la que se configura el envío de registros a SII.  
  Seleccionada una entidad legal (con o sin contabilidad), todas sus organizaciones hijas quedarán igualmente acogidas a SII.
- **Fecha acogida a SII**: **Comprobación** que permite configurar que la organización seleccionada se acoja al SII; esto es, que los registros de sus facturas se envíen (alta/modificación) a la AEAT a través de ficheros XML.  
  Una vez seleccionada, se muestra el resto de parámetros de configuración de SII.  
  El usuario la puede desmarcar con posterioridad, en el caso de que la organización ya no esté acogida a SII.  
  Si se desmarca esta comprobación, todos los demás campos aparecerán como no editables y la organización ya no estará acogida a SII; es decir, ya no será necesario ni se podrá enviar el registro de sus facturas a SII (alta/modificación).
- **Fecha acogida a SII**: campo de fecha en el que se puede indicar la fecha en la que la organización se acoge a SII. En general, esta fecha es el **01-07-2017**.
- **Ruta de ubicación del certificado electrónico**: el usuario debe especificar la ruta en la que se encuentra el certificado de la AEAT válido para dicha organización.
- **Contraseña certificada**: una vez informado el campo anterior, el usuario debe indicar la contraseña de dicho certificado. El contenido se guardará como texto cifrado.
- **Plazo límite de alta en SII**: campo informativo que por defecto mostrará **8 días** como plazo límite de alta en SII, ya que para 2017 y para este tipo de comunicación Alta (A0) ese es el plazo límite.  
  El usuario tendrá que modificarlo a **4 días** o al número de días que indique la AEAT para el alta de registros de factura a realizar a partir del 1 de enero de 2018.
- **Cadencia Proceso Alta Facturas Venta a SII**: en este campo, el usuario puede configurar el número de días naturales de margen que necesita para revisar/modificar las facturas de venta, antes de que estas se envíen de forma automática por el proceso de alta en SII, proceso que se recomienda programar para que sea ejecutado diariamente. Además, se recomienda que el número de días introducido en este campo no supere el **plazo límite de alta en SII**, que en el caso de las facturas de venta es de 8 días (sin contar sábados, domingos y festivos nacionales) desde la fecha de expedición de la factura (fecha factura).  
  En todo caso, las facturas expedidas se tienen que dar de alta en SII antes del día 16 del mes siguiente al que se produjo el devengo de la operación.  
  En concreto:
  - Una factura con fecha de operación 10-07-2017 (devengo) y fecha de expedición 14-07-2017 (fecha factura) tendría que darse de alta en SII antes del día 25-07-2017.  
    Si introducimos una cadencia de 8 días, tendremos 8 días de margen para su revisión/modificación, ya que dicha factura se enviará a SII de forma automática el día 22-07-2017.  
    Es decir, el proceso automático de alta que se ejecute el día 22 de julio enviará todas las facturas de venta con fecha factura 14 de julio (22 de julio - 8 días).
  - Una factura con fecha de operación 10-06-2017 (devengo) y fecha de expedición 14-07-2017 (fecha factura) tendrá que darse de alta en SII antes del día 16-07-2017.  
    Es decir, el proceso automático de alta que se ejecute el día 14 de julio ya enviará dicha factura, sin tener en cuenta el número de días introducido en el campo de cadencia.
- **Cadencia Proceso Alta Facturas Compra a SII**: en este campo el usuario puede configurar el número de días de margen que necesita para revisar/modificar las facturas de compra, antes de que estas se envíen de forma automática por el proceso de alta en SII, proceso que se recomienda programar para que sea ejecutado diariamente. Además, se recomienda que el número de días introducido en este campo no supere el **plazo límite de alta en SII**, que en el caso de las facturas de compra es de 8 días (sin contar sábados, domingos y festivos nacionales) desde la fecha contable de la factura.  
  En todo caso, las facturas de compra se tienen que dar de alta en SII antes del día 16 del mes siguiente al que se liquidó la operación a efectos de IVA.  
  En concreto:
  - Una factura con fecha de operación 10-07-2017 y fecha factura/fecha contable 14-07-2017 tendría que darse de alta en SII antes del día 25-07-2017.  
    Si introducimos una cadencia de 8 días, tendremos 8 días de margen para su revisión/modificación, ya que dicha factura se enviará a SII de forma automática el día 22-07-2017.  
    Es decir, el proceso automático de alta que se ejecute el día 22 de julio enviará todas las facturas de compra con fecha contable 14 de julio (22 de julio - 8 días).
  - Una factura con fecha de operación 10-06-2017, que se quiera liquidar en la declaración de junio y con fecha contable 14-07-2017, tendrá que darse de alta en SII antes del día 16-07-2017.  
    Es decir, el proceso automático de alta que se ejecute el día 14 de julio ya enviará dicha factura, sin tener en cuenta el número de días introducido en el campo de cadencia.
- **Entorno de producción SII**: este entorno tiene que estar seleccionado para aquellos entornos productivos de organizaciones cuyos registros de factura se tienen que enviar al entorno productivo (final) de SII de la AEAT.  
  Por defecto se muestra como seleccionado; en cuyo caso las facturas se enviarán al entorno de producción de la AEAT.  
  Si el usuario quiere realizar pruebas de envío, siempre desde un entorno de test o entidad/organización de pruebas, deberá desmarcarlo.
- **Adjuntar archivos XML**: este campo permite indicar si los ficheros XML enviados a la AEAT y los recibidos como respuesta por parte de la AEAT se deben guardar como ficheros adjuntos en la factura correspondiente.
- **Enviar desde 1 de enero 2017**: este campo permite que el proceso automático de alta en SII considere o no las facturas con fecha desde 01-01-2017 hasta 30-06-2017.  
  Este proceso considera en todo caso las facturas con fecha desde la fecha acogida a SII configurada (01-07-2017).
  - Si está seleccionado, las facturas con fecha desde 01-01-2017 hasta el 30-06-2017 también serán incluidas en el proceso automático de alta en SII.
  - Si no está seleccionado, las facturas con fecha desde 01-01-2017 hasta el 30-06-2017 no serán incluidas en el proceso de alta automático y, por tanto, habrá que enviarlas de forma manual o a través de Monitor SII, o no enviarlas, como es el caso para los sujetos acogidos a REDEME.
- **Afectada RECC**: este parámetro permite configurar que, para una organización no acogida al **Régimen Especial del Criterio de Caja** (RECC), pero sí afectada por recibir facturas de proveedores acogidos, se muestre o no la pestaña **Cobros/ Pagos Criterio Caja** dentro de la pantalla **Monitor SII**.  
  Si la organización, llegado un punto, no se viera ya afectada por dicho régimen, podría desactivar este campo, y la pestaña **Cobros/ Pagos Criterio Caja** se dejaría de mostrar en el Monitor SII.
- **Sujeto inscrito en REDEME**: si se selecciona este campo, se está indicando que la organización es un sujeto pasivo inscrito en REDEME que, por tanto, no tiene obligación de enviar las facturas del primer semestre de 2017 a SII.  
  Con este campo se controla que las facturas del primer semestre de este tipo de sujetos pasivos no se puedan dar de alta en SII de forma manual; esto es, desde la ventana de factura de venta.
- **Fecha desde visualización "Monitor SII"**: en este campo podemos introducir la fecha desde la cual se visualizarán las facturas de compra/venta y los cobros/pagos en RECC en la ventana **Monitor SII** para su alta en SII. Por ejemplo:
  - si una organización se acoge al SII el 01-07-2017 y no está inscrita en REDEME, la fecha a introducir en este campo será el 01-01-2017
  - si una organización se acoge al SII el 01-07-2017 y está inscrita en REDEME, la fecha a introducir en este campo será el 01-07-2017.

### **Descripciones SII**

En esta ventana es posible introducir descripciones tipo para las operaciones de compra/venta que la organización acogida a SII realiza.

Las descripciones introducidas en esta pantalla:

- solo se podrán seleccionar en las facturas de compra si la descripción está configurada como **Descripción factura de compra**
- solo se podrán seleccionar en las facturas de venta si la descripción está configurada como **Descripción factura de venta**
- se podrán seleccionar tanto en las facturas de compra como de venta si las dos comprobaciones **Descripción factura de compra** y **Descripción factura de venta** están seleccionadas
- será la que por defecto se seleccione tanto en facturas de compra como de venta si, además, se selecciona la comprobación **Por defecto**.

![](../../../../../assets/drive/x5SNFYObWJ09RINUVFsSyaz2GXjEz9dgzB8uii8Aop2bTJzFPhKiRl1DQn0U_ftwny6e4YRNo-48sriTWNDSvvOX-J0Riu4Vih2WmesHgfYJR10cNFG54mM1I6fXN2UpnoclPpOSgD7GKqH5tVw.png)

Además, en las ventanas de:

- Pedido de Venta
- Pedido de Compra
- Factura de Venta
- Factura de Compra

existe otro campo de texto libre que se denomina **Descripción SII** que siempre se puede utilizar.

Si en una factura seleccionamos una descripción en el campo **Descripción maestro SII**, el campo **Descripción SII** heredará esa descripción para que, para esa operación en concreto, podamos modificar/completar dicha descripción.

Si una factura tiene ambas descripciones **Descripción SII** y **Descripción maestro SII**, siempre prevalece la primera; es decir, será la **Descripción SII** la que se incluya en el fichero XML de alta/modificación en SII.

Si en un pedido se informa la **Descripción SII** y la correspondiente factura se crea desde dicho pedido, la descripción introducida en el campo **Descripción SII** del pedido se rellenará de forma automática en el campo **Descripción SII** de la factura.

Si se copiara desde más de un pedido, solo se trasladaría la primera descripción.

### **Configuración de la Organización en RECC**

Si una organización se acoge al régimen del IVA de Caja, deberán seleccionarse el campo **IVA de Caja** y el campo **Criterio de caja doble** en la ventana **Organización**, pestaña **Información**.

En este caso, tanto las facturas de compra como de venta nacionales estarán sujetas al RECC y tendrán que darse de alta como tales en SII.

!!! info
    La clave de **RÉGIMEN ESPECIAL / IDENTIFICACIÓN OPERACIONES CON TRASCENDENCIA TRIBUTARIA** del RECC es la **07**. Esta clave prevalece sobre las demás.

Esto significa que las operaciones de arrendamiento con RECC no se informarán con la clave propia de los arrendamientos, sino con la de RECC, que es la 07.

### **Configuración de proveedores en RECC**

Si una organización no se acoge al régimen del IVA de Caja, pero recibe facturas de proveedores acogidos al RECC, tendrá que configurar dichos proveedores como acogidos al RECC en la ventana **Terceros**, pestaña **Proveedor/Acreedor**, campo **IVA de Caja**.

### **Configuración de los métodos de pago**

Los cobros/pagos de facturas en RECC (IVA de Caja) tienen que darse de alta en SII.

Al dar de alta este tipo de cobros/pagos tenemos que informar del **importe**, la **fecha** de cobro/pago y el **medio** de cobro/pago utilizado, conforme a una definición propia de la AEAT:

- Transferencia "01"
- Cheque "02"
- Otros "04"

Es por ello que en la ventana **Método de Pago** tendremos que configurar el tipo de método de pago, tal y como se explica a continuación:

- los métodos de pago que configuremos con el tipo **Cuenta Bancaria** serán del tipo 01 = Transferencia
- los métodos de pago que configuremos con el tipo **Comprobación** serán del tipo 02 = Cheque
- y los métodos de pago que configuremos con el tipo **Asociado en Otros** serán del tipo 04 = Otros.

![](../../../../../assets/drive/6RIBz5XNdlOJZfAYW9noDPVGUdVjzgJ-odzlxR_I1kl4zuYXuKJeVqJ-oFz2l39Lk3LFBcIOpFh-JT6v4sa4TseyUaT6AXWHwV7_uD-XTTRasQSsjYBhZUzzVR12IJXodchVfGWSmlPZRVFQ8Zs.png)

### **Causas de exención**

Tratándose de una operación de venta exenta, la AEAT permite consignar la causa de exención dentro del bloque **Desglose Factura** como **Sujeta** y **Exenta**, utilizando una de las siguientes claves:

“E1: exenta por el artículo 20”

“E2: exenta por el artículo 21”

“E3: exenta por el artículo 22”

“E4: exenta por los artículos 23 y 24”

“E5: exenta por el artículo 25”

“E6: exenta por otros”

En Etendo existen dos opciones para indicar la causa de exención junto con la base imponible:

- En la **ventana Factura (Cliente)**, dentro del grupo de campos AEAT SII, se cumplimentará la causa de exención relacionada con las bases exentas de la factura. El usuario tendrá que asignar un valor del desplegable de forma manual que trasladará al XML la clave que hace referencia a la base imponible exenta en factura.
- En la **ventana Causa de exención** existe la opción de establecer una clave por defecto que se asignará en factura cuando se incorporen líneas que utilicen un impuesto configurado como exento. Es decir, cuando en una factura de venta se introduzca una línea exenta, automáticamente en la cabecera se seleccionará la causa asignada por defecto, siendo modificable si el usuario quisiera elegir otra.

![](../../../../../assets/drive/68wFWHAUwNPb9pxqJ74XV0_7GWE9NTOwLRq_zcsu_25D9eEKbCC0yAZGot3P-LRyMP3m9ofSVHjHV_ayL7VWhPK_FCONObalaYedgxtIYblbAHMwbOQxRJxU94A9dUIyPYu3cvxn397kT5FKRK0.png)

### **Configuración alta de factura de compra solo tras su contabilización**

Para organizaciones que desean dar de alta una factura de compra solo tras su contabilización, existe la opción de controlarlo mediante la activación de la comprobación **Alta en SII facturas de compra tras su contabilización** ubicada en la ventana **Configuración SII**, de manera que la fecha registro contable únicamente se rellenará en el momento en que la factura sea contabilizada, con el día en el que se produzca el asiento contable, independientemente de la fecha imputada en el libro diario, completando así la información necesaria para dar de alta la factura en SII.

![](../../../../../assets/drive/wDYzHV8OVfCzUR5nY9mJRuHgfVRARdfad7C_5joSfI3YHj-oIZ5jlqbHpoEAnmFdR2foIajkDQ4kWPpS7263-7CMJnIGChmJVinY3s7Pan3paaZYYICZgySArMwH4Aa1QKNgveg43dODi9zPD5I.png)

!!! info
    Si se decide optar por esta funcionalidad, es conveniente que la organización no tenga activo el proceso de contabilización automático, ya que imputará la fecha registro contable en el momento de realizar la contabilización.

### Configuración de rangos de impuestos - Prorrata SII

Los rangos de impuestos para la prorrata se tendrán que crear siempre de manera manual (tanto el rango “padre” como los rangos “hijos” necesarios). Esto es debido a que el porcentaje de deducción varía año a año al no ser un porcentaje fijo.

En la ventana **Rango impuesto** se ha creado una nueva comprobación denominada **Is prorate**:

![screenhunter_01_sep._01_11.08.gif](../../../../../assets/legacy/enduserdocumentation/screenhunter_01_sep._01_11.08.gif)

Al tener activa esta comprobación, se mostrará una segunda comprobación nueva, dentro de la cabecera en el detalle **More Information**, que se llamará **Prorrata SII - XML** y que estará marcada por defecto como **Sí**:

![screenhunter_02_sep._01_11.09.gif](../../../../../assets/legacy/enduserdocumentation/screenhunter_02_sep._01_11.09.gif)

Estas comprobaciones permitirán, con la configuración correcta que realicemos, enviar al SII información sobre facturas de compra afectadas por la prorrata del IVA.

A continuación, utilizaremos como ejemplo el IVA del 10% para mostrar la configuración que debe realizarse para que la información se envíe de forma correcta al SII:

![unnamed.gif](../../../../../assets/legacy/enduserdocumentation/unnamed.gif)

1 – Crear un rango padre “Prorrata Gener.22 (77%) IVA 10%”:  
Lo haremos con la misma configuración que puede tener cualquier rango nacional de la misma categoría, por ejemplo “Prestación servicios nacional 10%“. Las únicas particularidades que debemos tener en cuenta serán indicar en el campo **Indice** el valor total del impuesto (en los rangos “padres” estándar es un campo en el que se indica 0) y activar la comprobación **Is Prorate**. En nuestro ejemplo indicaremos en el campo **Indice** el valor 10 y posteriormente marcaremos la comprobación de **Nivel de agrupación**.

![screenhunter_04_sep._01_11.16.gif](../../../../../assets/legacy/enduserdocumentation/screenhunter_04_sep._01_11.16.gif)

![screenhunter_05_sep._01_11.16.gif](../../../../../assets/legacy/enduserdocumentation/screenhunter_05_sep._01_11.16.gif)

2 – Crear un rango hijo deducible “Prorrata Gener.22 (77%) IVA 10% (+77%)”:  
Al igual que en el punto anterior, crearemos un rango “hijo” con la misma configuración que puede tener cualquier rango nacional de la misma categoría, por ejemplo “Prestación servicios nacional 10%“, e indicaremos cuál es el rango “padre” (el creado en el punto 1). Las únicas particularidades que debemos tener en cuenta serán indicar en el campo **Indice** el valor del porcentaje de impuesto deducible (según nuestro ejemplo indicaremos 7,7) y activar la comprobación **Is Prorate**:

![screenhunter_06_sep._01_11.17.gif](../../../../../assets/legacy/enduserdocumentation/screenhunter_06_sep._01_11.17.gif)

3 – Crear un rango hijo no deducible “Prorrata Gener.22 (77%) IVA 10% (-23%)”:  
Crearemos el segundo rango “hijo” de la misma manera que el anterior. Además de indicar en el campo **Indice** el valor del porcentaje de impuesto no deducible (según nuestro ejemplo indicaremos 2,3) y activar la comprobación **Is Prorate**, tendremos que marcar la comprobación de **Impuesto no deducible** que se encuentra dentro del detalle **More Information**:

![screenhunter_07_sep._01_11.18.gif](../../../../../assets/legacy/enduserdocumentation/screenhunter_07_sep._01_11.18.gif)

![screenhunter_08_sep._01_11.19.gif](../../../../../assets/legacy/enduserdocumentation/screenhunter_08_sep._01_11.19.gif)
## **Submission of invoice records to SII**

Once all the parameters for submission to SII have been configured, it is now possible to register/modify the records of issued/received invoices in SII.

From Etendo, we can send these records (registration/modification) manually or automatically in accordance with the AEAT requirements, as explained below.

### **Manual Submission**

**Registration in SII**

##### **Sales Invoices**

From the "Invoice (Customer)" window, a new sales invoice is created, in the same way sales invoices are created in Etendo.

Within the "AEAT SII" field group, we must indicate, as shown in the following image:

![](../../../../../assets/drive/9JpfQqGKF7-_z1OT14yslxXsujho_F52LKKra1oEchhjCvNqSuKeeAFl-I_8R9ZLicY5kC7xFZWE0pKjKoL37cWY460b3-oxGq8rCAF0jeNDnY9zW-1kx3JeANgejmqgjvbjC3dOTHStPYt8ag8.png)

- the "**Fecha operación**", which by default is filled in with the same date as the "Invoice Date", although the user can modify it.
- the **Invoice Type Key**, which by default will be filled in with the value "**Invoice**", invoice type key "F1".  
   Other possible values are: - "**Simplified invoice**", invoice type key "F2", for simplified invoices created from each registered ticket/order. - "**Corrective invoice**", invoice type key "R1 to R5", depending on the selected "Correction Reason". - "**Summary entry for simplified invoices**", invoice type key "F4", for simplified invoices that group registered tickets/orders.

!!! info
    It is not possible to automatically fill in this field as "Corrective Invoice" when creating invoices of type "Reverse Sales Invoice", because it is possible to create Corrective Invoices by "Substitution" as "AR Invoice" (not Reverse).

It will be validated that when creating an invoice of type "Corrective Invoice" "By Differences", the transaction document must be of type "Reverse".

- The **SII master description** of the operation, since in the XML files we will not include information about the invoice lines. In this case, we select a master description.
- Or we directly enter a description of the operation in the free text field "**SII Description**".  
  If we select a master description, it is shown in the "SII Description" field by default so it can be modified/completed for that operation/invoice.
  - If the invoice is created from an order and that order included an "SII Description", that description will be automatically incorporated into the invoice, provided that the invoice "SII Description" field is empty.
  - If the invoice is created from several orders, and all of them have an "SII Description", only the one from the first selected order will be incorporated into the invoice.

It is important to emphasize that in the case of sales invoices, we must consider two dates for submission (registration) in SII:

- **the invoice date**, since this is the date from which the registration deadline in SII must be counted, which in 2017 is 8 days (excluding Saturdays, Sundays and national holidays).
- the **operation date**, since this is the date to be considered as the tax accrual date corresponding to the operation being recorded.

Issued invoices must be sent to SII (registration in SII) within 8 days (4 days from 01-01-2018) from the invoice issue date and, in any case, before the 16th day of the month following the month in which the tax accrual corresponding to the recorded operation occurred.

For example, a businessperson A provides a service to another businessperson on August 2, 2017 (operation date), issuing the corresponding invoice on September 13, 2017 (invoice date). The deadline to issue the invoice and submit the record of this invoice through SII ends on September 15.

In this example, the period will be August (operation date) and the fiscal year 2017.

Once this information has been entered, we can complete and post the invoice, or only complete it.

At this point, the "**Alta en SII**" button is enabled.

![](../../../../../assets/drive/7cFVkpUUzmAnQ82GFakllefI21kNGCJOtphTnAVpQM-249bn8AgShm_73EiSU6YnkQ2Th2bfw7xfX36ohWf7LMrZP_CbAAjUv8E3Sns6qsP5BZXOzjP-wQ9TsS_Fu_ncK0Gfg1pFoOW_Pdu4yUU.png)

By clicking that button, we start the process of registering the record of that invoice in SII (Communication type A0).

Etendo shows a message indicating that:

"_This non-reversible action (except in case of communication error or registry error) generates the "registration" of the invoice in the AEAT electronic office. Once registered, it will only be possible to "Post" and "Unpost" the invoice, with no further changes allowed except the accounting accounts to be considered in posting, and the accounting date only in the case of issued invoices. Once correctly "registered" in SII, it will be possible to "modify" the invoice in case of registry error if the invoice field "modified due to registry error" is enabled. In that case, only the submission to SII of the "modification" record of the invoice will be possible_".

That is, it is always possible to post/unpost the invoice after registering it in SII, but it will only be possible to reactivate it in the following cases:

- **Communication error** - the registration in SII has resulted "Incorrect" due to an accepted error or due to a connection error. In that case it will be possible to reactivate the invoice to correct the error and register it again in SII.
- **Registry error** - the status of the registration in SII of the invoice is "Correct", however a registry error occurred that must be corrected. In that case it will be possible to reactivate the invoice, selecting the field "Modified registry error", make the appropriate changes and send the "modification" of the invoice record. See section: Modification in SII.

In the "SII Data" tab of the invoice, we will have access to the following data:

- "**Communication Type**", with the value "Registration".
- number of "**SII Connection**" which will also be reflected in the "SII Connections" window.
- the "**CSV Code**" or secure verification code that AEAT has indicated related to the registration of this invoice in SII.  
  AEAT responds with a CSV for each invoice sent. If an XML file with several invoices is sent, the response XML will include a CSV for each of them.
- the "**SII Record Status**", which at this point can be:
  - "**Correct**" - the invoice has been successfully registered in the AEAT electronic office.
  - "**Incorrect**" - the invoice has been totally rejected and, therefore, is not registered. In this case, AEAT will inform us of the incorrect data. We must correct them and resend the invoice.
  - "**Accepted with errors**" - the invoice has been registered but contains errors that we must correct and resend. Likewise, AEAT will indicate the errors to be corrected.
  - "**Error sending**" - the invoice is not registered, since an error occurred in the online connection with AEAT. We must resend the invoice.
  - "**Cancelled**" - this is a status that we can obtain in the responses received when performing an "SII Query". This status has been added so that we can also "manage" it.
  - "**Not Reportable in SII**" - the invoice is not registered, since all its lines are associated with a tax configured as "Not Reportable in SII"

**For AEAT, "Admissible" errors** are those that will be admitted by AEAT.

They correspond to errors derived from business validations of invoices or records.

These errors must be corrected through a new correct modification request on those invoices or records accepted with errors.

**For AEAT, "Non-Admissible" errors** are those errors that under no circumstances can be admitted by the Agency in the submission of invoices or records of each register book.

They correspond to errors caused by not passing the structural and syntactic validations of the submission and to errors already typified by AEAT.

These errors must be corrected through a new correct submission request of the incorrect invoices or records.

- **SII Error Reason**, communicated by AEAT

This tab also includes information about the invoice "reconciliation", sent by AEAT after performing the corresponding "Query". The reconciliation fields are:

- **SII Reconciliation Status**
- and **Reconciliation Date**

And, in the "**Attachments**" field group, we can find the registration and AEAT response XML files, if we have configured the organization to store these files.

Finally, in the header of the sales invoice sent to SII manually or automatically, we will have information about the "**Fiscal Year**" and the "**Period**" that were included in the registration in SII of that invoice.

![](../../../../../assets/drive/g2N7zkHFiQI0VRRrWd1wUiRbD_YMkUTZbPjj55rc-J27t0yuKU8a53rk49H79ww5LD3qEXTg6YF5TReKkRhcxZYX4ZN2e7_G_LsptRjA5Wm5jDmezbpqjEJXtxGIFho5QDNvJEKSpLX4FNfcO5Q.png)

##### **Corrective Sales Invoices**

It is possible to correct a sales invoice correctly registered in SII if a merchandise return occurs, discounts after the sale (sales rappels) or situations of uncollectible debt or insolvency proceedings.

The correction of sales invoices must be managed and registered in SII either "By Differences" or "By Substitution", as explained below:

**By Differences**, in this case an invoice of type "Reverse" is recorded for the corresponding negative amount.

This would be the case where a sale was made for 1527.77 € which was correctly registered in SII and, later, the customer returns merchandise for a value of -27.77 € (15 units of product).

In this case, when recording the corrective invoice by differences, within the "AEAT SII" field group we must indicate the following information:

- **Invoice type key** = Corrective Invoice
- **Correction Type** = By Differences
- **Correction Reason** = R1...R4, to be selected by the user according to the reason for the correction.

These types of corrective invoices must be created with documents of type "Reverse" (for example: "Reverse Sales Invoice"), and negative amounts, as shown on the screen. Etendo will show an error otherwise.

![](../../../../../assets/drive/vTuKPdCz4_8FyY4_zSO6LA157zXc_9Nr_D8zgcKv0O4rP5aKXnKOTp6T4ga6SwbHN29oEgD3MZBP_lEyZ4uTmZY43pXsiFapBmKqvowAp_z9xCeRLmituMo4UW7FG0zv2wbDhZuUvIiRR2diRP0.png)

When registering that invoice in SII, the XML file will automatically record the following information:

- Invoice Type = R1
- Correction Type = I
- Total amount = -27.77

![](../../../../../assets/drive/SeBxMk8qhA3rmNFmPr8rDLDp0Te2HvbQ6RS9HV_BlXMUelz5MFQEFTIvC_pg7HDHeh4joNbWJekXn4gGPcPBVhqE4JWeIrEuGE-vXyWDbF0EYfTQVeXUS_9SIqTt-hIk5IGmO4BKrjnfCwV7cVs.png)

**By Substitution**, in this case the original invoice (already registered in SII) is cancelled and a new invoice is created with the correct amounts.

The cancellation of the original invoice can be performed through the "**Reactivate-Cancel**" option in Etendo. This action will create a "Reverse" invoice with the following data:

- **Document type** = Reverse Sales Invoice
- **Fecha operación** = operation date of the original invoice
- **Invoice type key** = Invoice

When registering that cancellation invoice in SII, the XML file will automatically record the following information:

- Invoice Type = F1
- Total amount = -185.13

Subsequently, the new invoice is created with the correct amounts and with the following data:

- **Document type** = AR Invoice (no reverse)
- **Invoice type key** = Corrective Invoice
- **Correction Type** = By Substitution
- **Correction Reason** = R1...R4, to be selected by the user according to the reason for the correction.
- **Fecha operación** = operation date of the original invoice

![](../../../../../assets/drive/rdC0SMKqwDEIs85X9vxqT-gH-nz2YhzthhfKlLB_r9C21y2DwmdHFH5IAjvQSuPjMhDh68W3XBvEA1suciw55sUz01nQtcCjXQLCPLy4GM79hmE-0TnTPJWtlT9wqsIQiSjLi7NSbJQYNjLoePI.png)

When registering this corrective invoice by substitution in SII, the XML file will automatically record the following information:

- Invoice Type = R1
- Correction Type = S
- Total amount = 92.57

![](../../../../../assets/drive/lnYFE3_FU4bzz-1q2uHRiBxo8WEjg6PJjEZxg7iqFzPwM5kUFVzoXW7eGuF7vCCciW59Ls5jRsSI6vksPNZ6nvMYFB2yBLMgqjW6oausvB8IvBPlj3mVYTv9qAbRfhLQaTat-jaFOxSIpzrRrPw.png)

Both in corrective sales invoices by differences and by substitution, the user must assign the operation date corresponding to the original invoice (accrual of the operation). However, **in corrective invoices the registration period in SII will correspond to the invoice date**, being incorporated into the VAT return in that month.

##### **Purchase Invoices**

The process of recording and registering this type of invoices in SII is very similar to that of sales invoices.

The information for registering the purchase invoice record in SII will be taken from the "Invoice (Vendor)" window, once the corresponding purchase invoice is in "Completed" status.

Within the "AEAT SII" field group, we must indicate, as shown in the following image:

![](../../../../../assets/drive/cqDeUP_hKuC8VbLZevAo4OeHT3UwNZ3jdR2d30gp4MCdn2Gt3BmAwtXG_808xBrfS_VOHrta0oBdhRVjlUlB959b2ZuhfP4oPjpw1tL_d1VyK6m-0V7YwTkcq7Y_UvYuDQCGARgGz0hkuCdYgA0.png)

- the "**Fecha operación**", which by default is filled in with the same date as the "Invoice Date", current date or invoice creation date in Etendo, although the user can modify it.
- the "**Accounting registration date**", which by default and for invoices created manually is filled in with the current date, or invoice creation date in Etendo and, therefore, registration of the received invoice in Etendo.  
  This accounting registration date does not have to match the accounting date of the purchase invoice.
- the **Invoice Type Key**, which can be filled in with the following values:
  - "**Invoice**", which corresponds to an invoice type key "F1"
  - "**Import (DUA)**", which corresponds to an invoice type key "F5"
  - "**Supplementary Customs Settlement VAT on import**", which corresponds to an invoice type key "LC"
  - "**Accounting voucher**", which corresponds to an invoice type key "F6"

In the case of purchase invoices it is not necessary to indicate whether it is a corrective invoice or not.

- The **SII master description** of the operation, since in the XML files we will not include information about the invoice lines. In this case, we select a master description.
- Or we directly enter a description of the operation in the free text field "**SII Description**".  
  If we select a master description, it is shown in the "SII Description" field by default so it can be modified/completed for that operation/invoice.
  - If the invoice is created from an order and that order included an "SII Description", that description will be automatically incorporated into the invoice, provided that the invoice "SII Description" field is empty.
  - If the invoice is created from several orders, and all of them have an "SII Description", only the one from the first selected order will be incorporated into the invoice.

And, in addition, we must reflect the supplier invoice number in the **"Vendor Reference"** field.

Received invoices must be sent to SII (registration in SII) within 8 days (4 days from 01-01-2018) calendar days from the accounting registration date of the invoice, excluding Saturdays, Sundays, and nationally recognized holidays and, in any case, before the 16th day of the month following the settlement period in which the corresponding operations have been included (period in which input VAT is deducted). The deadline period may be shorter than the initial days of the term. If the 15th is Saturday, Sunday or holiday, the deadline is extended to the next business day.

Therefore, in the case of purchase invoices, we must consider the **accounting registration date** of the invoice as the date to be taken into account regarding registration in SII.

!!! info
    The [Tax Agency Deadline Calculator](https://www2.agenciatributaria.gob.es/wlpl/AVAC-CALC/LanzadorCalculadoraPlazos) can be used to run simulations for different cases and help clarify any doubts regarding settlement deadlines.

And, in addition, we have to take into account the following dates for calculating the tax settlement period reflected in the XML within the "Settlement Period" section (Fiscal Year/Period):

- the **operation date** of the invoice
- the **accounting registration date** of the invoice
- and the **registration date in SII** of the invoice.

So that:

- if the operation date is in the same month (for example, July) as the accounting registration date and registration in SII, the period reflected in the XML will be that same one (July, in our example)
- if the operation date is in June, the accounting registration date in July and the registration date in SII is before July 16, the period reflected in the XML will be June.
- If, on the contrary, and with the same previous dates, the registration date in SII is after July 15, the period reflected in the XML will be July.

For example:

A businessperson A sells goods to another businessperson B on July 3, 2022. Businessperson A issues the invoice on July 4. Businessperson B receives the invoice on July 30 and performs its accounting registration on October 10.

There are two possibilities:

- Businessperson B submits the invoice records on October 15, stating in the Register Book of received invoices, Fiscal Year: 2022, Period: 09.
- Businessperson B submits the invoice records on October 16, stating in the Register Book of received invoices, Fiscal Year: 2022, Period: 10.

Once this information has been entered, we can complete and post the invoice, or only complete it.

At this point, the "**Alta en SII**" button is enabled.

![](../../../../../assets/drive/W1rkgnVrH0mKDQ0NA-IAK1sLYniuAWMvnbMWL0uzeVoFAitGq8m9p_nu1zpcBthrvEmYnuJpHAvGF1iK6xfsCBwukRa6Si97mEssOkn6thGnWEhTyPyopkGdd-5pEsKpggQZEd4BjTqOFxy_LLY.png)

By clicking that button, we start the process of registering the record of that invoice in SII (Communication type A0).

Etendo shows a message indicating that:

"_This non-reversible action (except in case of communication error or registry error) generates the "registration" of the invoice in the AEAT electronic office. Once registered, it will only be possible to "Post" and "Unpost" the invoice, with no further changes allowed except the accounting accounts to be considered in posting, and the accounting date only in the case of issued invoices. Once correctly "registered" in SII, it will be possible to "modify" the invoice in case of registry error if the invoice field "modified due to registry error" is enabled. In that case, only the submission to SII of the "modification" record of the invoice will be possible_".

That is, it is always possible to post/unpost the invoice after registering it in SII, but it will only be possible to reactivate it in case of communication error or registry error, as explained for sales invoices.

!!! info
    In the case of purchase invoices, it will not be possible to change the accounting date of invoices correctly registered in SII.

Finally, in the header of the purchase invoice sent to SII manually or automatically, we will have information about the "**Fiscal Year**" and the "**Period**" that were included in the registration in SII of that invoice.

![](../../../../../assets/drive/Qj4R1IM6iiRpAwD5W06pJn2eqh9uR_mlF5dhG82eF3WkUc7_9mVb9jrw8EinOCeDZJL2U1kSXGoHnWZQ7vTV-ykEAu_PUGcAfengKKCFtGrRR89qnQGMNryBR9kWqseAky2pyK-f5XwISH1dPl4.png)

##### **Import Invoices (DUA)**

**Imports with DUA** must be recorded in the Register Book of Received Invoices with invoice type key “F5”.

As invoice number and issue date, the reference number shown in the DUA itself and the date of its admission by the Customs Administration must be stated, respectively.

In the identifying data corresponding to the supplier, those of the importer and holder of the register book must be stated, i.e. the Etendo organization.

Finally, and regarding the **freight forwarder invoice,** only the provision of services subject and not exempt will be stated, with invoice type key "**F1**".

To record in Etendo this type of operations "Imports with DUA" we must follow the steps below in the "Invoice (Vendor)" window:

- Create a new invoice for the business partner "Freight forwarder" with its invoice number or "Vendor Reference", with the following information in the "AEAT SII" and "Import (DUA)" field group:
  - Invoice type key: Import (DUA)
  - DUA: reference number shown in the DUA itself
  - DUA date: date of admission of the DUA by the Customs Administration
- in the "Lines" tab enter the freight forwarder invoice data, including its provision of services subject and not exempt.
- in the "Taxes" tab manually include a new tax line for taxes of type "Imports 21%", including the import taxable base and its corresponding amount.

Once completed and registered in SII, we will obtain an XML with the information required by AEAT.

In cases where an "Import (DUA)" operation is **related to more than one DUA**, it will be possible to select the "**Multiple DUA**" check.

When selecting this option:

- the "**DUA**" and "**DUA date**" fields in the invoice header are no longer shown since these fields **must be informed in the "Taxes" tab**, in order to relate the DUA and its date with the corresponding import taxable base, as shown in the following image.

![](../../../../../assets/drive/lFZBqb1lzXOH1Y1FtRibpnZJ3Rh9aXTirC2xlThC9N6okNSa2pFWBQa0582MMpvssLILoOwm27vTXyXK4Vxi0qIAN537ODDJZ8GuVDik669avGDaIn2K3ShmyjKRcwSBXiGJ6Hz_YNCazPDxOh8.png)

##### **Purchase Invoices (registration after posting)**

Organizations that enable the check "Register purchase invoices in SII after posting" in the SII Configuration window will be able to send their purchase invoices to SII after posting.

The process of recording and registering this type of invoices in SII is very similar to the rest of purchase invoices.

The information for registering the purchase invoice record in SII will be taken from the "Invoice (Vendor)" window, once the corresponding purchase invoice is in **"Completed"** and **"Posted"** status.

Within the "AEAT SII" field group, the fields will be filled in:

- the _"Fecha operación"_, which by default is filled in with the same date as the "Invoice Date", current date or invoice creation date in Etendo, although the user can modify it.
- the "**Accounting registration date**", which by default will be blank until the invoice is posted with the date on which the entry has been made, regardless of the date on which the accounting entries have been posted in the general journal. The Register in SII button will remain disabled until the document is posted. If the invoice is unposted before supplying it to SII, the accounting registration date will clear its content. In case the registration has already occurred, and it is necessary to perform a Modification due to registry error, the accounting registration date will not change when unposting and reactivating the invoice.
- the _Invoice Type Key_, which can be filled in with the following values:
  - "_Invoice_", which corresponds to an invoice type key "F1"
  - "_Import (DUA)_", which corresponds to an invoice type key "F5"
  - "_Supplementary Customs Settlement VAT on import_", which corresponds to an invoice type key "LC"
  - "_Accounting voucher_", which corresponds to an invoice type key "F6"

In the case of purchase invoices it is not necessary to indicate whether it is a corrective invoice or not.

- the _SII master description_ of the operation, since in the XML files we will not include information about the invoice lines. In this case we select a master description.
- or we directly enter a description of the operation in the free text field "_SII Description_".  
  If we select a master description, it is shown in the "SII Description" field by default so it can be modified/completed for that operation/invoice.
  - If the invoice is created from an order and that order included an "SII Description", that description will be automatically incorporated into the invoice, provided that the invoice "SII Description" field is empty.
  - If the invoice is created from several orders, and all of them have an "SII Description", only the one from the first selected order will be incorporated into the invoice.

And, in addition, we must reflect the supplier invoice number in the _"Vendor Reference"_ field.

Received invoices must be sent to SII (registration in SII) within 8 days (4 days from 01-01-2018) from the accounting registration date of the invoice and, in any case, before the 16th day of the month following the settlement period in which the corresponding operations have been included (period in which input VAT is deducted).

Therefore, in the case of purchase invoices, we must consider the **accounting registration date** of the invoice as the date to be taken into account regarding registration in SII.

And, in addition, we have to take into account the following dates for calculating the tax settlement period reflected in the XML within the "Settlement Period" section (Fiscal Year/Period):

- the _operation date_ of the invoice
- the _accounting registration date_ of the invoice
- and the _registration date in SII_ of the invoice.

So that:

- Only an invoice that is in "Completed" and "Posted" status will be registered in SII.
- When the user posts the invoice, the Accounting registration date field will be automatically filled in with the date of the day on which the accounting entry is recorded.
- If the document is unposted before performing the registration, the Accounting registration date field will clear its content.
- If the document is unposted after performing the registration to proceed with a modification due to registry error, the accounting registration date field will keep its content and the accounting registration date will continue to be the same as reported in the registration communication.

For example:

A businessperson A sells goods to another businessperson B on April 26, 2022. Businessperson A issues the invoice on April 27. Businessperson B receives the invoice on April 30 and performs its accounting registration on May 1, submitting the invoice records on July 12, so the assigned period will be 07, fiscal year 2022.

Once this information has been entered, we can complete and post the invoice.

After posting the document, the "**Alta en SII**" button is enabled.

![](../../../../../assets/drive/1UMsgNf7I6yPu5bwhqBTR6B6CoBqaRXmv.png)

By clicking that button, we start the process of registering the record of that invoice in SII (Communication type A0).

Etendo shows a message indicating that:

"_This non-reversible action (except in case of communication error or registry error) generates the "registration" of the invoice in the AEAT electronic office. Once correctly "registered" in SII, it will be possible to "modify" the invoice in case of registry error if the invoice field "modified due to registry error" is enabled. In that case, only the submission to SII of the "modification" record of the invoice will be possible_".

It is always possible to post/unpost the invoice after registering it in SII, but it will only be possible to reactivate it in case of communication error or registry error.

On July 26, businessperson B realizes that there was an error when entering the product price in the invoice line, so it is necessary to perform a modification due to registry error (Communication type A1). The process to follow is "Unpost", enable the check "Modify due to registry error" and "Reactivate" the document. After making the corresponding modification, the document is completed and posted again before pressing the "Modification in SII" button, keeping the accounting registration date that was initially reported in SII.

![](../../../../../assets/drive/1GfPbKvhLR_HiB8Cg0zq63hbOvKGyMtIA.png)

In the case of purchase invoices, it will also not be possible to change the accounting date of invoices correctly registered in SII.

!!! info
    If you decide to opt for this functionality, it is advisable that the organization does not have the automatic posting process active, since it will assign the accounting registration date at the time of posting.

#### **Modification in SII**

This type of communication implies the modification of invoice records already registered in SII due to registry errors that do not affect:

- the "invoice issuer", i.e. the organization or legal entity that issues/receives the invoice
- the "invoice date", i.e. the invoice date (issue) of sales invoices, invoice date in purchase invoices
- and the "invoice number", or "vendor reference" in purchase invoices which in no case can be modified.

For example, we realize an error in the selected tax range in an invoice that is already registered in SII.

In those cases we will have to modify the invoice and send it again to SII, with a different communication type which is A1 "Modification (Correction due to registry errors).

A new field has been created in the invoice header (both purchase and sales), section "AEAT SII" called, "**Modified due to registry error**". This new field is only enabled if:

- the invoice is in "Completed" status
- and, in addition, it is registered in SII (Register in SII= Yes) correctly, "SII Record Status" = Correct.

When selecting this new field, it is possible to unpost and reactivate the invoice, modify the error made, and finally complete the invoice again.

In no case will it be possible to modify:

- the invoice issuer (Organization)
- the invoice date (issue date in sales invoices/invoice date in purchase invoices)
- the invoice number (Document No. in sales invoices/Vendor Reference in purchase invoices)

The "**Modificación en SII**" button will allow us to send the modification of the invoice record to SII, as shown in the following screen:

![](../../../../../assets/drive/662noKMIVCrzTjC2DZyK9mKmy-suka3TFRNe707uHDJqd_LF2rhWbpV50_BnPRTsYT1cWx7KZ6JPOvO5IKs4A1KJpQLlBeYg0587HHMHVgh0zBRf-1NT1VWvysRKzeD-_Owkm-sYIYPiv8VkOAM.png)

The supply of this type of "modification" records must be carried out before the 16th day of the month following the period to which the return in which said modification must be taken into account refers.

### **Automatic Submission**

Within the "Request Processing" window, two new processes have been created: "SII registration process" and "SII modification process due to registry error", which can be configured for each organization or legal entity.

As with other Etendo processes, these can be configured to be executed immediately, planned or scheduled with a certain frequency.

It is recommended that this process be scheduled with a "daily" frequency, since, as explained below, this process will take into account the number of cadence days configured both for registration in SII of purchase invoices and sales invoices, for the organization.

It would also be possible that the daily option only included weekdays and, therefore, weekends were not taken into account for its execution.

#### **Registration in SII**

This process allows the mass "registration" (communication type A0) in SII of all purchase and sales invoices in "completed" status.

![](../../../../../assets/drive/w1ekffFhD9rdzVfeuBL6r7EuYU8QgRufj8cyg-0mKZNIEPgr69BvsDWLgP6xvlBCiwe1yYbGt3ROyHqcfeOqH4aDs_2TsY2Mfxb7cOtY_pbzlL_nGXeqptJosBJWmGXWUDZ0jVARQj6PlmMA7OI.png)

In the case of **sales invoices**, this process will take into account:

- the "operation date" and the "issue date" of the invoices
- and the "cadence of the registration process in SII", established for sales invoices in the "SII Configuration" window, for each Organization

For example, in the following scenario:

- sales invoice with operation date 01-07-2022
- issue date 05-07-2022
- submission cadence set to 8 days

even if we schedule the registration process in SII with a daily frequency, this invoice will only be registered in SII automatically, through this process, on 13-07-2022.

In other words, on 13-07-2022 the invoices with issue date 05-07-2022 will be sent (13-07-2022 - 8 days).

The deadline for registering this invoice in SII for 2022 would be 17-07-2022, since Saturdays, Sundays and national holidays must not be taken into account in this calculation.

In the following scenario:

- sales invoice with operation date 20-06-2022
- issue date 13-07-2022
- submission cadence set to 8 days

even if we schedule the registration process in SII with a daily frequency, this invoice will be registered in SII automatically on the same day it is issued, since the operation date and the invoice date are in different periods.

The deadline for registering this invoice in SII for 2022 would be 15-07-2022

In the case of **purchase invoices**, this process will take into account:

- the accounting date and the accounting registration date of the invoice
- and the "cadence of the registration process in SII", established for sales invoices in the "SII Configuration" window, for each Organization

For example, in the following scenario:

- purchase invoice with accounting date 05-07-2022
- accounting registration date 14-07-2022 (since the company decides to deduct VAT in July)
- submission cadence set to 8 days

even if we schedule the registration process in SII with a daily frequency, this invoice will only be registered in SII automatically, through this process, on 22-07-2022.

In other words, on 22-07-2022 the invoices with accounting registration date 14-07-2022 will be sent (22-07-2022 - 8 days).

The deadline for registering this invoice in SII would be 26-07-2022.

In the following scenario:

- purchase invoice with accounting date 20-06-2022
- accounting registration date 13-07-2022
- submission cadence set to 8 days

even if we schedule the registration process in SII with a daily frequency, this invoice will be registered in SII automatically on the same day as its accounting registration date, since the accounting date and the accounting registration date are in different periods.

The deadline for registering this invoice in SII would be 15-07-2022.
## **Management and submission of records from the "SII Monitor"**

From the "SII Monitor" window we can manage and perform mass submissions of issued/received invoices to SII, as well as the collections/payments of invoices under RECC and cash collections, the latter information to be sent annually.

As shown in the following screen, we filter by:

- SII Registration = No
- Document Status = Completed
- Business Partner = Spain Customer

we select several invoices and proceed with their SII Registration.

![](../../../../../assets/drive/OOCosDIgqaozTNviBVAylAHt_OtM1Xs1MCqkHr8ZwFcnzZ365gqZH7PMx4QVCXEjC6AHI7FYUQlG_HLFCToPyy4es_b5DUxJMU03G2dnnNWgmhz2LQ6lZnC_f-QSZsbRwH2h6vUZCeRfp71BG-XyKpg.png)

The same applies to the mass submission of modifications of issued/received invoices. In that case, those invoices must be marked as "Modified due to registration error" = YES.

As shown in the following screen, we filter by:

- SII Registration = YES
- Record Status = Correct
- Business Partner = Spain Customer

we select several invoices and proceed with their Modification in SII.

![](../../../../../assets/drive/GDKayCFFhT9bAkhr68IiFXboS51M5wwZQs89d7pc9uW3Uo1dXDTlfMgSrfBQZl6ZjHmIuJlSSTiXfOP_MdskUK7Rhbqw6l3RWQ506xpkixCHok3iH0RJ4-bd3RtElOGY0LlpuPEWUzEfAljwwuUNf4U.png)

## **Automatic creation of sales invoices**

### **Generate invoices (manually)**

The "Generate invoices (manually)" process allows creating sales invoices of type "AR Invoice" in completed status.

Because of this, in sales orders two new fields have been created within the field groups "Data for Invoicing Systems" and "AEAT SII", in order to indicate in each sales order:

- the "**Fecha operación**", if it is known
- and the "**SII Description**" of the operation.

In no case is it possible to send sales orders to SII (registration/modification).

As shown on the screen, it is possible to select the orders to invoice, and indicate an invoice date:

![](../../../../../assets/drive/Ew-3GmSHo4SC8MYPB1b_faB3t50XX3uNoBlp8hK4o8NQ_NNQGk0Rlfkgjxvmvp7QJn-acYuicdRzLB8eZ_EgDfvgBKxcOSoolmbX-kn6oROckmVoCBYZKrtoA55jIXX51NQ1-wp7DLVY5ETVjxvHSdk.png)

When processing, Etendo informs us that the corresponding invoices have been created, which will already have a "Completed" status.

!!! info
    Each of these invoices will inherit the operation date and the SII description entered in the order. It is important to note that the user can always modify them, if necessary, before registering that invoice in SII.

!!! info
    The invoice type key is not filled in by default, therefore the user, before registering in SII, will have to select the value "Invoice".

![](../../../../../assets/drive/aMgaLXe4tY4nipPDVT33nXXZCbiZiuddcE0lErcIFB-8SKN3BRIzIRw88im-00dJUrIlUoROIE7koQT9TfNhz81rTmkaR1EoLZZ_B53WfMtum0QRsdwvaxFUT3ruMFTNiMGL-m6NJVySFnQTXvyxn30.png)

If the sales order or sales orders were negative, this process would generate invoices of type "AR Invoice" that we will have to reactivate and modify before registering in SII:

- The document type must be changed to a "reverse" type such as "Reverse Sales Invoice".
- The invoice type key must be selected as "Corrective Invoice", and enter:
  - the corrective type
  - and the reason for the correction.

![](../../../../../assets/drive/pwCBP_ahyxDvNz_-q3IcT0IJBo4B1r05w3AhJLrmfTGMoX9-BFL41vf4-CH6DMC_RN-pZBjBp0LlOigea-baElLEvjiaMlZt52aVaw7SmLR6EW5QwzM86iNtmfaQcygSC21OipvaKGRLLiK4v2w1YeU.png)

### **Create Lines From** 

**Orders**

Purchase/sales invoices can be created from orders with the "**Create Lines From**" option. Several orders can be selected to be included in an invoice.

Regarding SII information, we must take into account that:

- If the sales/purchase invoice being created **does not have information in the "SII Description" field**, the "SII Description" entered in the first selected sales/purchase order will be taken.
- The invoice **operation** date will by default be the invoice date and will not be modified when copying the orders. The user will have to modify it manually if it is different from the invoice date.
- If the **first order that is copied is negative** (in the case of sales invoices), the corresponding sales invoice will be created as "Corrective Invoice", "By differences", with the "Correction Reason" R1, and the user can change that information if necessary, when adding additional positive or negative order lines.
- **Purchase invoices created from positive orders** will be created with invoice type key "**Invoice**", with document type "AP Invoice".
- **Purchase invoices created from negative orders** will be created with invoice type key "**Invoice**", and the user should create them with a reverse document type "Reverse Purchase Invoice", since in the case of received invoices  
  it is not mandatory to indicate whether an invoice is corrective or not, whether positive or negative.

**Goods Shipments** (Goods Shipment (Customer)/Return from Customer or Goods Receipt (Vendor)/Return to Vendor Shipment)

Purchase/sales invoices can be created from shipments/returns with the "**Create Lines From**" option. Several shipments/returns can be selected to be included in an invoice.

Regarding SII information, we must take into account that:

- These **shipments and returns do not include SII information**, therefore, the SII information in the invoice header must be filled in by the user, both the operation date, the invoice type key and the SII description.

## Invoice integrity through digital fingerprint (HMAC)

:material-menu: `Application` > `Financial Management` > `Invoicing Systems` > `Suministro Inmediato de Información (SII)` > `SII Configuration`

Each invoice reportable to SII includes a digital fingerprint (HMAC), calculated from identifying invoice fields that remain unchanged once issued.

This fingerprint allows checking that the content is not modified after issuance.  
To detect changes in issued (completed) invoices, the system provides the **Validate Hash** process in the **SII Configuration** window.

In this process, a date range is queried and the invoices included in that period are verified.

If the system detects modifications, it records the result in the **Log Hash** tab, indicating which invoice has alterations.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/sii/validacion-hash-sii.png)
## **Casos de uso**

Dentro de este apartado se describen diferentes casos de uso tanto para las facturas de venta (LRFE) como de compra (LRFR), y su registro de "Alta" en SII.

!!! info
    Es importante recalcar que las fechas de operación que se muestran en los XML no coinciden con las fechas descritas en los casos de uso, ya que a fecha de junio no es posible enviar facturas con fechas de julio (fechas ejemplo).

### **Libro de Facturas Emitidas**

La información del registro de alta/modificación de las facturas de venta se obtiene de la ventana "Factura (Cliente)", que como ya se ha explicado se ha modificado para incluir información requerida por SII (Fecha operación, clave tipo factura, descripción SII, etc.).

El registro de alta/modificación en SII de las facturas de venta varía en función de las siguientes variables:

- la **localización del "Tercero"** (Cliente), ya sea éste extranjero, intracomunitario o nacional, que conlleva la sujeción o no al IVA y dentro de la sujeción, su exención.
- el **tipo de factura emitida**, esto es "Factura"(F1), "Factura Rectificativa"(RX), "Factura Simplificada" (F2) o "Asiento Resumen de Factura Simplificada" (F4).
- **la sujeción al RECC** de la organización
- la venta a minoristas en las que se incluye "**Recargo de Equivalencia**"
- la venta a revendedores en **Inversión del Sujeto Pasivo**

y en función de que la factura emitida incluya:

- **el arrendamiento de local de negocio** sujeto o no a retención
- **una operación sujeta a IPSI/IGIC**
- o una **transmisión de un bien inmueble** sujeta a IVA

así como que la factura emitida:

- se liquide con un **cobro en metálico superior a 6000.00€**
- o tenga una **fecha de factura** (expedición) **anterior al día 1 de julio de 2017.**

En los apartados siguientes se analiza la información que debemos recoger en las facturas de venta de Etendo para cada caso de uso, así como la información relevante que el XML de alta/modificación del registro de dichas facturas debe incluir.

La principal diferencia entre los XML de alta/modificación de los registros de facturas de venta de cualquier tipo es que:

- Los XML de alta incluirán un tipo de comunicación  
  \<sii:TipoComunicacion\>A0</sii:TipoComunicacion>
- Los XML de modificación incluirán un tipo de comunicación  
  \<sii:TipoComunicacion>A1</sii:TipoComunicacion>, junto con los datos de la factura correcta a modificar.

##### **Tercero (Cliente) Nacional**

Factura emitida con IVA Nacional por entrega de bienes y prestación de servicios.

La organización F&B España presta un servicio a su cliente "Alimentos y Supermercados", identificado con un NIF válido de España.

La operación se realiza el 2 de agosto de 2017. F&B España emite la correspondiente factura de venta con fecha 7 de agosto de 2017.

En este caso, y dado que el IVA se ha devengado en el periodo de agosto (fecha operación 2 de agosto), el plazo límite de expedición de la factura de venta y su alta en SII sería el 15 de septiembre.

Al expedirse la factura con fecha 7 de agosto, se está en plazo. Dicha factura se tendrá que dar de alta en SII antes del día 18 de agosto de 2017 (aplica cómputo 8 días, sin incluir sábados, domingos ni festivos nacionales).

Al expedir esta factura en Etendo, los tipos de impuestos que se seleccionan por defecto serán del tipo:

- Entregas IVA 10%
- Prestación servicios nacional 21%

Una vez completada la factura, se procede a su Alta en SII, bien de forma manual o automática.

El XML de alta en SII contendrá la siguiente información:

- un tipo de Factura "F1"
- con clave régimen especial "01" (Régimen General)
- Sujeta No Exenta "S1"
- con desglose por detalle de IVA.

![](../../../../../assets/drive/CDES62-nQ75UdtctVvQydN6-vDcqgQcFcdf3rRCeadKiYdCTTh4dXbX70wFVbxAC4sAuX10W_4MWkj7T-Z8xzuenunrPQ3FfIy6iHs7SvZOcX7eLi5RNKQdU8g0nhLtcG-RtZCWsFxP2sPRRW-x9TnE.png)

Es importante recalcar que:

- si la factura de venta nacional incluye más de un bien/servicio al mismo tipo impositivo, en el XML la información se mostrará agrupada por dicho tipo impositivo (por ejemplo 21%)
- si la factura de venta incluye más de un bien/servicio con distintos tipos impositivos, en el XML la información se mostrará desglosada por "Detalle de IVA" o tipo impositivo.

#### **Tercero (Cliente) extranjero**

Factura emitida por la exportación de bienes y prestación de servicios en el extranjero.

La organización F&B España emite el 13 de septiembre de 2017 una factura a la Empresa Z situada en Marruecos por la venta de un equipo y el servicio de instalación. La operación se produjo el día 29 de agosto. Este tercero debe identificarse en Etendo con un "Clave NIF País Residencia", distinta de 1 (NIF) y 2 (NOI).

En este caso, y dado que el IVA se ha devengado en el periodo de agosto (fecha operación 29 de agosto), el plazo límite de expedición de la factura de venta y su alta en SII sería el 13 de septiembre.

Al expedirse la factura con fecha 13 de septiembre, opera ficha límite, es decir, esta factura tendrá que enviarse a SII antes del día 15 de septiembre.

Al expedir esta factura en Etendo, los tipos de impuestos que se seleccionan por defecto serán del tipo:

- Exportaciones (%N=>0%)
- Servicios prestados internacional (%N=>0%)

La entrega del bien es una operación sujeta pero exenta de IVA.

La prestación del servicio es una operación no sujeta por reglas de localización.

Una vez completada la factura, se procede a su Alta en SII, bien de forma manual o automática.

El XML de alta en SII contendrá la siguiente información:

- un tipo de Factura "F1"
- con clave régimen especial "02" (Exportación)
- con desglose por tipo de Operación
- prestación del servicio "No sujeto por reglas de localización"
- exportación del bien "Sujeta y Exenta", con clave de causa de exención "E2" (Exportación).

![](../../../../../assets/drive/5zXCAlCIBhJiUvUE2u4IPU47L16nNpn96Y-FbZ5SXgiiHoocMWiyDbeUoVD8UY7LVRTxk75wW3hqZnOjC0rDk2OSh5zZgWu07ggeMiRrDfJVAY01TQ-e8SaS2IdbuHMtJ8DQPAA-1n1f9fBVVFuwepE.png)

Es importante recalcar que:

- si la factura incluye una entrega de un bien a Canarias (tipo impositivo "Entregas a Canarias,Ceuta y Melilla (%N=>0%)")
- y una prestación de servicios que se localiza en Canarias (tipo impositivo "Servicios a Canarias, Ceuta y Melilla (%N=>0%)")

el XML generado incluye igualmente:

- un tipo de Factura "F1"
- con clave régimen especial "02" (Exportación)
- con desglose por tipo de Operación
- prestación del servicio "No sujeto por reglas de localización"
- exportación del bien "Sujeta y Exenta", con clave de causa de exención "E2" (Exportación). Esta clave se puede configurar para que aparezca por defecto en la ventana "Causa de exención" o indicar en la cabecera de la factura.

![](../../../../../assets/drive/BnMTWAUJv3Itf0gbWYlfNV0RuyNPonFy4GFIpV9Ahh81Y2KK9JiI1p7dVLY79EidOqX8eOuGrGYYwN6Y6cVERAU_iNjULVsQUU_FKxk30SLRq1Nz-WDyW2SCC_YKC1gDqGXGt87ofjEjs9ka8oiiiQY.png)

#### **Tercero (Cliente) Intracomunitario**

Factura emitida con IVA Intracomunitario por entrega de bienes y prestación de servicios.

La organización F&B España emite el día 18 de agosto de 2017 una factura por la entrega de hardware (por importe de 1000.00 €) y su instalación (por importe de 800.00 €) a un cliente localizado en Francia. La operación se realiza el día 10 de agosto de 2017.

Este cliente localizado en Francia, debe estar identificado en Etendo con una "Clave NIF País Residencia" de tipo 2 = NOI.

En este caso, y dado que el IVA se ha devengado en el periodo de agosto (fecha operación 10 de agosto), el plazo límite de expedición de la factura de venta y su alta en SII sería el 15 de septiembre.

Al expedirse la factura con fecha 18 de agosto, se está en plazo. Dicha factura se tendrá que dar de alta en SII antes del día 30 de agosto de 2017 (aplica cómputo 8 días, sin incluir sábados, domingos ni festivos nacionales).

Al expedir esta factura en Etendo, los tipos de impuestos que se seleccionan por defecto serán del tipo:

- Entregas intracomunitarias (%N=>0%)
- Servicios prestados UE (%N=>0%)

La entrega del bien es una operación sujeta pero exenta de IVA.

La prestación del servicio es una operación no sujeta por reglas de localización.

Una vez completada la factura, se procede a su Alta en SII, bien de forma manual o automática.

El XML de alta en SII contendrá la siguiente información:

- un tipo de Factura "F1"
- con clave régimen especial "01" (Régimen General)
- con desglose por tipo de Operación
- prestación del servicio "No sujeto por reglas de localización"
- exportación del bien "Sujeta y Exenta", con clave de causa de exención "E5" (Entrega intracomunitaria). Esta clave se puede configurar para que aparezca por defecto en la ventana "Causa de exención" o indicar en la cabecera de la factura.

![](../../../../../assets/drive/luCZJQdNJOYe_30B8lauePugxFfIgv8TCOATfe2t1uFBz-FVINtxs0KooEAXdaTMGE9o44PXUQF4lS5hwGljNUQU-1G_x5GqakdHzFPBerOuzHQr3am409yP-YwDbE1YEknU8jFIatjxrkzkuUEiCHY.png)

Es importante recalcar que:

- si la factura de venta intracomunitaria incluye más de un bien al mismo/distinto tipo impositivo, en el XML la información se mostrará agrupada, dentro del nodo "Entrega/Sujeta/Exenta".
- si la factura de venta intracomunitaria incluye más de un servicio al mismo o distinto tipo impositivo, en el XML la información se mostrará agrupada por operación no sujeta por reglas de localización, dentro del nodo "PrestaciónServicios/NoSujeta"

#### **Organización acogida al RECC**

F&B España se encuentra acogida al régimen especial de criterio de caja.

Ésta organización vende bienes y un servicio a un cliente español el día 6 de julio de 2017, expidiendo la correspondiente factura ese mismo día.

Al registrar esta factura de venta en Etendo, los tipos de impuestos que se selecciona por defecto serán del tipo:

- Entregas IVA 10% IVA de Caja.
- Prestación servicios nacional 21% IVA de Caja.

La información de estas operaciones se suministrará en los plazos generales como si a las mismas no les hubiera sido de aplicación el régimen especial, por tanto y, en este caso, al emitirse la factura en el mismo periodo en el que se produce el devengo de la operación (Julio), el plazo límite de alta en SII para la factura sería el 18 de julio de 2017.

Una vez completada la factura, se procede a su Alta en SII, bien de forma manual o automática.

El XML de alta en SII contendrá la siguiente información:

- un tipo de Factura "F1"
- con clave régimen especial "07" (Regimen especial del criterio de caja)
- Sujeta No Exenta "S1"
- con desglose por detalle de IVA.

![](../../../../../assets/drive/-vN1cdTs45fGesRdAFTV6SOW8rbFfLo_9e32RSYXjKQkjKOCm4htirPAxfxUPkJZiu595v01C7vEC0iKxCiz7QDmp_ihz41rxp_O563v357xtRFwjToD69L_nGu6_B_e2bX_anYMqi0WCy-w3Cce6Wg.png)

#### **Cobros de facturas en Régimen Especial de Criterio de Caja (RECC)**

Los cobros totales o parciales de facturas en RECC deben darse de alta en SII en el momento de producirse.

Desde la ventana "Monitor SII" podemos filtrar por el número de cobro y proceder a su envío a SII.

Una vez dado de alta en SII, el XML generado informa de los siguientes datos del cobro, referenciados al número de la factura de venta:

- **Fecha**
- **Importe**
- **Medio**

![](../../../../../assets/drive/zNO7__LCn0RS6lT_b-IqOr-5UI7FWlcdIhnJAiPhseee-s6Wc1FTV4EtmD9Ujp_R_Q7WEKcPY-LBi9xWWe_hj2Q28fkR-JnyV3NVvoPKGxhptTlVq6VOhKpIVhfkkUsi6H_Dj1eCS8kcA2T6YgkonZg.png)

El Medio que en nuestro ejemplo es el 02 (Cheque), debe configurarse en el Método de Pago, campo "**Tipo**".

**Anulación de cobros**

En el caso de los libros registro de cobros en RECC, no se utilizará el tipo de comunicación A1 de "Modificación de facturas/registros por error registral".

La modificación de un cobro en RECC ya dado de alta en SII se efectuará enviando el cobro que se pretende anular en negativo.

Lo anterior implica que en Etendo, no podremos reactivar un cobro en RECC ya dado de alta en SII, si no que tendremos que revertirlo, con la opción "Revertir pago" que se muestra en la siguiente imagen:

![](../../../../../assets/drive/1aPMk2pmJYGzATaN_B1dI0Ri4wunDMRoW.png)

Al revertir el cobro, Etendo genera un nuevo cobro por el mismo importe en negativo que tendremos que dar de alta en SII desde la ventana "Monitor SII", tal y como se muestra en la siguiente imagen:

![](../../../../../assets/drive/10k-gBCn4bUmQfxOqxjngiqdb-sgzhskD.png)

El XML generado contendrá la siguiente información:

- el importe del cobro en negativo
- referido a la factura

![](../../../../../assets/drive/pi-8xhxVCAgUYqm35_0jxct9_B8i6lAHxBLIJ0rCGmfu44v4C47P8iWd02KZ7XTF2kwbYe8F2FvU9YelFpyCORry5_1vIHqvwjuDNFIE09Ns1bA9myQEb0Ar5j01RihIO-Wk_AoTlNOxPl4tODJwAMo.png)

**Facturas en RECC no cobradas en el año natural** (en desarrollo).

Como parte de la funcionalidad del RECC, Etendo permite la "liquidación manual del IVA de Caja" para aquellas facturas en RECC que no fuesen cobradas total o parcialmente antes del 31 de diciembre del año posterior al año de su expedición, produciéndose así el devengo del impuesto.

Por tanto, las facturas en RECC de fecha 2017 que no estén cobradas a 31-12-2018, tendrán que enviarse a SII en dicha fecha, y con la siguiente información:

- **Fecha** (de cobro) = 31-12-2018 (fecha de la liquidación manual del IVA)
- **Importe** = importe pendiente de cobro de la factura
- **Medio** = 03 (No se cobra/No se paga)

Desde la ventana de "Liquidación manual del IVA de Caja" será posible enviar estas liquidaciones manuales a SII, con fecha 31 de diciembre del año posterior al año de su expedición (devengo del impuesto).

#### **Ventas con recargo de equivalencia**

F&B España realiza una venta a un cliente acogido al recargo de equivalencia.

Al expedir la factura por la entrega correspondiente el tipo impositivo seleccionado será del tipo “Entregas IVA+RE 21+5.2%.

Una vez completada la factura, se procede a su Alta en SII, bien de forma manual o automática.

El XML de alta en SII contendrá la siguiente información:

- un tipo de Factura "F1"
- con clave regimen especial "01" (Régimen General)
- Sujeta No Exenta "S1"
- con desglose por detalle de IVA de haber más de un tipo impositivo diferente
- con información en los nodos:
  - tipo recargo de equivalencia
  - cuota del recargo de equivalencia

![](../../../../../assets/drive/T3uUXF3GgSV_UnjkKYJeJT1TvMTg-mly1C1HdKbirdRo3sdYKRAU_-hTXitit3t6jnZoEeMHJ98cgMIHKA4u4u0wJ-eZipjPEFC6vpd89qTTwDpBcOSwNsL350kqL3WZMpUsXmeVxA3o42FhhrZJAZM.png)

#### **Operaciones de venta con ISP**

En el caso de producirse una venta por parte de F&B España a un cliente revendedor español, el tipo impositivo utilizado será:

- Entregas sin IVA por ISP

es decir:

- el vendedor emitirá la factura de venta sin aplicar el IVA
- El comprador que recibe la factura sin IVA declarará este IVA como una Inversión del Sujeto Pasivo. Ver escenario de compra Inversión del Sujeto Pasivo.

Una vez completada la factura, se procede a su Alta en SII, bien de forma manual o automática.

El XML de alta en SII contendrá la siguiente información:

- un tipo de Factura "F1"
- con clave régimen especial "01" (Operación de régimen general.)
- y la operación dentro del bloque funcional ”Desglose factura”, "Sujeta - No Exenta – Con Inversión sujeto pasivo” (S2).
- Los campos “tipo impositivo” “cuota repercutida” se informarán con importe cero

![](../../../../../assets/drive/ZEqqB3TgdDl7PnFVsTpM5FtOKACsXZ1wU2VmDKspeWJQCkSuqpJCREyAK2NtnDT9QweIYdz-H89Bh74hcqr1ATWVgxjZm15zPTXzGRBLkZvGnq0uFrFAJIp1HochquU5YMhUpboj3HTmXg1eJe7beRo.png)

#### **Arrendamiento de local de negocio**

F&B España emite el día 1 de septiembre de 2017 una factura por el arrendamiento de un local de negocio con una base imponible de 850 €.

F&B España emite una factura con los siguientes datos:

- **Fecha de expedición de la factura** (fecha factura): 1 de septiembre de 2017
- **Fecha de operación**: 30 de Agosto de 2017 (cubriendo el alquiler del mes de Agosto).

En este caso, tenemos hasta el 13 de septiembre para dar de alta la factura emitida en SII, contando 8 días naturales desde la fecha de expedición de la factura.

En este caso, la fecha límite de expedición de la factura y de envío a SII, sería antes del día 16 del mes siguiente a aquel en que se hubiera producido el devengo de la operación, esto es el 15-09-2017.

Al registrar esta factura en Etendo, los tipos de impuestos que se seleccionan por defecto serán del tipo:

- Arrendamiento 21% (cobros)

Una vez completada la factura, se procede a su Alta en SII, bien de forma manual o automática.

El XML de alta en SII contendrá la siguiente información:

- un tipo de Factura "F1"
- con clave regimen especial "12" (Operaciones de arrendamiento de local de negocio no sujetos a retención)
- Sujeta No Exenta "S1"
- con el detalle del Inmueble, que se obtiene de la configuración realizada para el "local arrendado" en la ventana "Producto":
  - Situación del inmueble
  - Referencia catastral

![](../../../../../assets/drive/mtf9dUeo9KXFMRhgM2rj868eBLugn6FjnystCp18gska41BDKkO60I5tH3m99sf-T4l0Hmo2_9-ZJvMPMvpCXSmqnSEZ5TIVEQ1CshWlVxKkItpZ_renVXmVhQIJVbdLrOOKP67AH_txpy4JoY8dKn0.png)

En el caso de que el arrendamiento incluya retención, el tipo impositivo a utilizar sería del tipo "Arrendamientos 21% -19%R (cobros)" y la información del XML la siguiente:

- un tipo de Factura "F1"
- con clave régimen especial "11" (Operaciones de arrendamiento de local de negocio sujetas a retención)
- Sujeta No Exenta "S1"

![](../../../../../assets/drive/u3q1KqomFK1gk_RK0zXOfJ0_Rzk3WlN5GkS0mr7t0UfP_Wza_qXiAf6FXXatfzGxod5gHiJNkirgqTm8URkstrpTCBGd-TBL0O9CuYm5Jq4_s2nQd8tl_iCpOrrRtNgd1guBelPfd-kcdMXzl7yqBj8.png)

En el caso de locales arrendados sujetos a retención, no es necesario especificar la información del inmueble, por incluirse ésta en el modelo de retenciones (Modelo 180) correspondiente.

Por último recalcar que:

- Si una misma factura incluye más de un arrendamiento con y sin retención, se dará de alta en SII con la clave "13" e información (referencia catastral/situación del inmueble) del local(es) que no estén sujetos a retención.
- Si una factura de arrendamiento está sujeta al régimen especial del criterio de caja, prevalecerá la clave 07 de Operación Sujeta a RECC.

#### **Operación de venta sujeta a IPSI/IGIC**

F&B España con domicilio fiscal en Madrid, adquiere una máquina en Canarias y la vende en dicho territorio junto con un servicio de instalación de la misma, que también adquiere/presta en Canarias.

La operación se realiza el 29 de agosto. F&B España emite la factura el día 13 de septiembre.

En este caso y dado que el IVA se ha devengado en agosto, el plazo límite de expedición de la factura de venta y su alta en SII sería el 15 de septiembre (opera fecha límite).

Al registrar esta factura en Etendo, los tipos de impuestos que se deben seleccionar son del tipo:

- Entregas IGIC 13,5%
- Servicios Prestados en Canarias 13.5%

Tanto la entrega de bienes como la prestación del servicio se adquieren y localizan en Canarias, por lo que no es aplicable ningún tipo de IVA.

Esta operación está sujeta a IGIC y por tanto, debe registrarse en SII como una operación no sujeta por reglas de localización (tanto en lo relativo a bienes como servicios).

Una vez completada la factura, se procede a su Alta en SII, bien de forma manual o automática.

El XML de alta en SII contendrá la siguiente información:

- un tipo de Factura "F1"
- con clave régimen especial "08" (Operaciones sujetas a IPSI/IGIC)
- y todo el importe de la operación (bases imponibles) tanto de bienes como servicios, en el nodo "Operación no sujeta por reglas de localización"

![](../../../../../assets/drive/MvYNDpfiSbbn9wkjDb_pvc0rMIlv0l1_DQuAarhiNZfGz3apN6HhQaeSl_MGMhkmhXW2wMj2MimCCnviAA5U9rxNuVFcK4fG_jGtfzqLGAzJPFyfudlMA3yKBMqFMO_KIpL_Yje6DeDTIpQkN3RCWSw.png)

#### **Transmisión de bienes inmuebles**

F&B España expide el día 1 de septiembre de 2017 una factura por la venta de un bien inmueble en Madrid por 150.000 €.

La operación se realiza el 1 de septiembre, expidiendo factura el día 5 de septiembre.

En este caso, la fecha límite de alta en SII sería de 8 días (hábiles) contando desde la fecha de expedición de la factura, esto es el 15 de septiembre de 2017.

Al registrar esta factura en Etendo, los tipos de impuestos que se seleccionan por defecto serán del tipo:

- Transmisión de bienes inmuebles 21%

Una vez completada la factura, se procede a su Alta en SII, bien de forma manual o automática.

El XML de alta en SII contendrá la siguiente información:

- un tipo de Factura "F1"
- con un importe por transmisión de bienes inmuebles de

![](../../../../../assets/drive/YvejK7Py-383mQDuU6vqd4psPpJzCR5oLQ3vMFcCHWdEVw33FtvP_yX8ZzHiiROQ9sQmQNYMZTaJ1E_2J9mtdaa5cIpHIYXkUY2vLnjeB9uB5FSKrfi91Qt-2onjt5AP-aSWZMI7eIOOlHFhuQKhUeU.png)

#### **Cobros en metálico**

La información correspondiente a los importes superiores a 6.000 euros percibidos en metálico durante el ejercicio de una misma persona o entidad, deberá suministrarse con carácter anual, durante los primeros 30 días del mes de enero siguiente al ejercicio al que se refieran.

En Etendo se ha creado una nueva ventana denominada "SII Cobros en metálico" que permite gestionar la generación de dichos cobros y su posterior "alta" o "Modificación" en SII.

**Alta Cobros en Metálico**

En la ventana "SII Cobros en metálico" se puede introducir la "Organización" y el Ejercicio (por ejemplo 2021), para el cual se necesita suministrar este tipo de información de carácter anual.

Una vez introducida dicha información, el botón "**Actualizar Cobros Metálicos SII**" lanza un proceso que tiene en cuenta:

- todas las transacciones del tipo **“BP Deposit”** o **“Cobro”** con estado **"Cobro depositado"** o **"Conciliado"**, realizadas en cuentas bancarias de tipo **“Caja”** con **"fecha de transacción”** durante el año natural especificado (Ejercicio).
- respecto de operaciones/transacciones bancarias relacionadas con **Facturas y Conceptos Contables**, asociadas a un “Tercero” identificado con un **CIF/NIF** (por ejemplo NIF)
- y que, **agrupadas por dicho tercero**, superen el importe de 6.000,00 €

![](../../../../../assets/drive/1SFZL1-iAvHxq27c-zACBqx-a-EKd5Rzt.png)

Una vez generado el cobro/cobros, se puede realizar su "**Alta en SII**". Una vez dado de alta en SII, los campos "Alta en SII", "Estado registro SII", "Importe", "Importe enviado" e "Importe enviado" se actualizarán.

Si se produjera un error al dar de alta en SII, se mostraría el código de error y el mensaje del error para su subsanación.

**Modificación Cobros en Metálico**

La ventana "SII Cobros metálico" permite además, controlar incidencias que se podrían producir con posterioridad al alta del cobro(s). Incidencias que puedan deberse a la incorporación de nuevos cobros, modificación/eliminación de cobros existentes para un tercero.

Para ello, se diferencian los siguientes campos:

- **Importe**: corresponde a la suma total de los cobros depositados en una cuenta financiera de tipo caja, que supere la cantidad de 6.000,00 €, respecto de un tercero
- **Importe enviado** a SII
- **Importe pendiente** de envío a SII
- **Totalmente enviado**: tomará los valores, "Sí" cuando no existan diferencias entre el campo "importe" e "importe enviado"; "No" cuando un aumento/disminución del importe provoque una diferencia al ya enviado.

Por ejemplo para un tercero determinado se realizaron varias facturas durante el año 2021 que se cobran en metálico. El importe total de dichas facturas y, por tanto, el importe recibido en metálico de este tercero asciende a 151,000.00. Tanto las facturas como el cobro en metálico se han dado de alta en SII.

![](../../../../../assets/drive/1u1oUThSf80IxxOdRGouxAHwQraXG2w1o.png)

Con posterioridad se realiza una nueva factura por importe de 1,800.00 €, que también se cobra en efectivo, y que por tanto debe darse de alta en SII.

En la ventana "SII Cobros en Metálico", tendremos que:

- actualizar la información para que se refleje el nuevo cobro creado como "Importe pendiente" de alta en SII, tal y como se muestra en la imagen siguiente:

![](../../../../../assets/drive/1BbyKHAgfLYfW2n4tXqhw9n18lsO9eRxF.png)

- y activar el check "**Modificada error registral**" en el cobro.

Una vez hecho esto se podrá proceder a la modificación en SII de dicho cobro para el tercero, a través del botón "**Modificación en SII**".

![](../../../../../assets/drive/1e8dQ5G3FbWKQue-E1ZCfu-LwgtpxD0PF.png)

Es importante recalcar que si de un tercero se recibiera un cobro en metálico con fecha del ejercicio a declarar (por ejemplo 2017), respecto de una factura de fecha anterior (por ejemplo 2016), dicho cobro también se incluirá en la selección, para su alta en SII, siempre que el importe total recibido/cobrado de ese tercero supere los 6000.00 €.

#### **Factura emitida con fecha de expedición anterior al 01-07-2017**

Respecto de las facturas emitidas con fecha de expedición anterior al 01-01-2017, existe también la obligación de su alta en SII, pero con un esquema XML con las siguientes particularidades:

- **Clave de régimen especial** = 16 (Primer semestre 2017).
- **Descripción de la operación**: “Registro del Primer semestre 2017”.

Y, en el caso de las facturas emitidas, con independencia de su calificación cuando son "No Exentas", se informarán bajo la siguiente clave:

- **Tipo no exenta: S1**.

Lo anterior aplica excepto para sujetos pasivos en REDEME que ya las habrán enviado en el Modelo 340 correspondiente.

En Etendo, al dar de alta en SII una factura con fecha anterior al 01-07-2017, comprobaremos que el esquema XML es del tipo siguiente:

![](../../../../../assets/drive/4o687WK4KAze5LKKh6DcmXN0Jqu4THxG1BB-V_FpI_5XiZa81XzP251gWHKh-Cz0-rrVi4psJ8-QAlLPOpukxkxn-QYlxf1DdNzAycfo9bYHX1PIZGe6BVaO93zMFRtbn5h7BjemISBttCGvqH8s9bU.png)

En Etendo se ha desarrollado un proceso "Es en segundo plano" que adapta las facturas de venta del primer semestre para que puedan darse de alta en SII.

Este proceso se denomina "**Proceso de adaptación a SII de Facturas de Venta del primer semestre de 2017**" y configura las facturas de venta del primer semestre, de la siguiente forma:

- como "**Factura**", es decir, con la **"Clave de tipo Factura" = F1**.
  - las facturas de venta positivas, con/sin pedido relacionado, y tercero con NIF.
- como "**Factura Rectificativa por Diferencias y error fundado"**, es decir, con la "**Clave de tipo Factura" = R1**
  - las facturas de venta negativas, con/sin pedido relacionado, y tercero con NIF.
- como "**Factura Simplificada**", es decir, con "**Clave tipo Factura" = F2**
  - las facturas positivas o negativas sin/con un ticket/pedido relacionado y tercero sin NIF.
- como "**Asiento Resumen de Factura Simplificada**", es decir, con "**Clave tipo Factura" = F4**
  - las facturas positivas o negativas con más de un ticket/pedido relacionado, y tercero sin NIF.
- añade la descripción tipo "**Registro del Primer semestre**"
- e indica como "**Fecha de operación**" la fecha de la factura tal y como requiere la AEAT.

!!! info
    El usuario siempre podrá revisar la configuración otorgada a dichas facturas antes de darlas de alta en SII.

La ventana "**Monitor SII**" incluye también una pestaña "**Facturas de Venta Primer Semestre 2017**" desde dónde se pueden gestionar estás facturas, una vez configuradas de forma correcta por el proceso.

#### **Factura emitidas rectificativa fuera de plazo**

Factura emitida rectificativa por sustitución en un periodo posterior al de presentación de la declaración de IVA - Modelo 303, de la factura original.

La organización F&B España realiza una entrega de bienes por valor de 2420 € (IVA incluido) La operación se realiza el 2 de enero de 2018. F&B España emite la correspondiente factura de venta con fecha 2 de enero de 2022.

En este caso, y dado que el IVA se ha devengado en el periodo de enero (fecha operación 2 de enero), el plazo límite de expedición de la factura de venta y su alta en SII sería el 15 de febrero.

Una vez completada la factura, se procede a su Alta en SII el día 2 de enero.

El XML de alta en SII contendrá la siguiente información:

Clave tipo factura = F1-Factura

Importe total = 2420

Fecha Factura: 02-01-2022

Fecha Contable: 02-01-2022

**Fecha de Operación: 02-01-2022**

**Periodo SII: 01 - Enero**

**Ejercicio SII: 2022**

![](../../../../../assets/drive/HJdwEipVS4djsZugPA3zso45tgrG6enxXhlP_KOSpe4a9r2v8EcytimONV_AMoVyaMIE8oJ3f4oLSpzObpdoRRgJ3HsTjWRAijIB94bZdAt45OvJPcGz-rwKdw2x1ykj9oX6_eoMKw02eqNaAk01Tjs.png)

El día 1 de marzo, se produce una devolución por mal estado del 20% de la mercancía con un valor de 484 € (IVA incluido) por lo que F&B España procede a la anulación de la factura original y emisión de una nueva con el importe final correcto.

Se produce una anulación de la factura original (ya dada de alta en SII e incorporada a la declaración de IVA del mes de enero) a través de la opción "Reactivar-Anular" de Etendo. Esta acción creará una factura del tipo "Reverse" con los siguientes datos:

Clave Tipo Factura = F1-Factura

Importe total = -2420

Tipo de documento = Reverse Sales Invoice

Fecha Factura: 01-03-2018

Fecha Contable: 01-03-2018

**Fecha de Operación: 02-01-2018** (fecha de operación de la factura original)

![](../../../../../assets/drive/fetQO0nNF-Q3kkLURvyOFzQ46wSUEIIjymSsJCfk9GkiUMInhKjnvjWnmvgsZdi2_oM-dpdLGenWjw9a1h6OFBxj7CUAfQBzNLrTT64XL0pA6zhIrcE8hJxoOFD-KP6Uywr6ZuOKqbzsVSUCIt3J2EE.png)

Al dar de Alta esa factura de anulación en SII, el fichero XML registrará de forma automática la siguiente información:

**Periodo SII: 07 - Julio**

**Ejercicio SII: 2022**

El periodo asignado en SII no se corresponde con la fecha de operación, si no con la Fecha Factura (julio), por lo que **pasará a formar parte de la liquidación del impuesto del mes de julio**.

![](../../../../../assets/drive/qPqZ-pAmr6pO6ALY0z4_PrmOrkEnqWO5b-YqmEbVPZX3DSUQUEd36VwA5LmUZciyEqR4l70kFCR9QIv0u2VgUf-HJEWUEDJcp9mCuBe5J_sW6o8wC5PSAesUXAsH3e_0cOVbsnHg4LmSx3XFpJIQtfs.png)

Posteriormente, se crea la nueva factura con los importes correctos y con los siguientes datos:

Tipo de documento = AR Invoice (no reverse)

Clave tipo factura = Factura Rectificativa

Tipo Rectificativa = Por Sustitución

Motivo de la rectificación = R1...R4, a seleccionar por el usuario según el motivo de la rectificación.

Fecha Factura: 01-03-2018

Fecha Contable: 01-03-2018

**Fecha de Operación: 02-01-2018** (fecha de operación de la factura original que tendrá que seleccionar el usuario de forma manual)

![](../../../../../assets/drive/Ln5HvZyVHOBK-JEMdCGGj7N__H5Bzn8mAm3xqW2jRUNOpDdeOdBXNWaa6F-0lWrHDbXbVFXclkYHFqsQ5e-IJWVuo_o8871Y0TTpk7apWwr7W6lwixlux5lbKxTfBsJBHP1o1RsigQrozwyHTJSuGPk.png)

Al dar de Alta esa factura de anulación en SII, el fichero XML registrará de forma automática la siguiente información:

**Periodo SII: 07 - Julio**

**Ejercicio SII: 2022**

![](../../../../../assets/drive/WmCrqgr1mzfFPN73yfGGt5a6jseoeH0wUEAWYyzaOROUsZtcVEtmljTWDUh_CT6KpHmza0a2Oc6P1ZqnczOZF8COnXiEXg2_W2FiQU8vz_fgIINsqydZnwSpojBEjhBGMcJgJXFss9Ihy4eIjKWzgPo.png)

Al igual que la anterior factura que anula el importe de la original, el periodo asignado en SII, no se corresponde con la fecha de operación si no con la Fecha Factura (Julio), por lo que **pasará a formar parte de la liquidación del impuesto del mes de julio**.

Si la emisión de una factura rectificativa, ya sea por diferencias o por sustitución, se produce en el mismo período del devengo de la operación. Es decir, la emisión de las distintas facturas (Factura original, anulación y rectificativa con motivos R1,R2,R3 Y R4) se emiten en un mismo mes, podrán liquidarse en la declaración del impuesto del mismo periodo.

En el resto de casos en los que la fecha de operación de la factura original sea distinta a la emisión de las facturas correctivas posteriores, el periodo de liquidación será distinto.

### **Libro de Facturas Recibidas**

La información del registro de alta de las facturas de compra se obtiene de la ventana "Factura (Proveedor)".

En todo caso, será obligatorio introducir el número de factura del proveedor en el campo "Referencia del Proveedor", con el fin de identificar y cruzar la información de las facturas.

El registro de alta en SII de las facturas de compra varían en función de las siguientes variables:

- la **localización del "Tercero"** (Proveedor), ya sea éste extranjero, intracomunitario o nacional
- el **tipo de factura recibida**, esto es "Factura", "Factura de Importación (con DUA)", "Justificante Contable".
- **la sujeción al RECC** de la operación reflejada en la factura de compra
- **la sujeción al RECC** de la organización que recibe (registra) la factura de compra.
- que la factura de compra incluya operaciones por las que los empresarios satisfacen compensaciones en las adquisiciones a **personas acogidas al REAGYP**.

y en función de que la factura recibida incluya:

- **una operación sujeta a IPSI/IGIC**
- **un arrendamiento de local de negocio** sujeta a IVA
- o **gastos de personal** que son en todo caso no declarables y, por tanto, no deben darse de alta en SII

así como que la factura recibida refleje:

- una "**Inversión del Sujeto Pasivo**"
- o su **fecha contable sea anterior al 1 de Julio de 2017**

#### **Tercero (Proveedor) Nacional**

Factura recibida con IVA Nacional por la adquisición de un bien y la prestación de un servicio.

La organización F&B España recibe una factura de un proveedor nacional, que incluye tanto bienes como servicios.

La operación se realiza el 2 de agosto de 2017 y la factura se expide con fecha 7 de agosto de 2017.

F&B España recibe la factura el día 9 de agosto de 2017 y decide consignar y deducir la cuota soportada en el modelo 303 del mes de agosto, procediendo a su registro contable el 13 de septiembre.

El plazo para remitir el registro de esa factura a través del SII finaliza el 15 de septiembre, en este caso (antes del día 16 del mes siguiente al que se devenga la operación).

Al registrar esta factura en Etendo, los tipos de impuestos que se seleccionan por defecto serán del tipo:

- Adquisiciones IVA 21%
- Prestación servicios nacional 21%

Es importante registrar:

- como fecha de factura de compra, la fecha de expedición de la factura de venta
- como referencia de proveedor, el número de factura de la factura de venta

Una vez completada la factura, se procede a su Alta en SII, bien de forma manual o automática.

El XML de alta en SII contendrá la siguiente información:

- un tipo de Factura "F1"
- con clave regimen especial "01" (Régimen General)
- con información sobre la cuota deducible y la fecha contable.
- con desglose factura y detalle de IVA, de existir tipos de IVA diferentes.

Después de su alta en SII, es posible contabilizar y descontabilizar la factura de compra, si fuera necesario, pero no será posible cambiar la fecha contable de la factura por ser este campo obligatorio respecto de las facturas de compra.

![](../../../../../assets/drive/AH_zdSOXyQVvw8Vxt60YW-gZbSimeZlJnn0v0oX2nrUZSpfkNn1B_sf8RCGyM5a1GP-thIUBE0HVOVI5rR_59xkcn4dWgR6JmeeqGbuG4fHFz5fPoKe_Gdg-izeDXm0f1yLl_YBFcSN7ce6s42Oto-g.png)

Es importante recalcar que:

- si la factura de compra nacional incluye más de un bien/servicio al mismo/distinto tipo impositivo, en el XML la información se mostrará agrupada por tipo impositivo, dentro del nodo "DesgloseIVA/DetalleIVA"

#### **Tercero (Proveedor) extranjero**

##### **Caso 1 - Factura recibida de un proveedor extranjero (antes del DUA)**

F&B España recibe una factura de compra de un proveedor extranjero, localizado en USA, por la adquisición de unos bienes. Todavía no se ha recibido el DUA ni la factura del transitario que realizará la importación de los bienes.

En este caso, la factura del proveedor extranjero se debe registrar con la siguiente información dentro del grupo de campos "AEAT SII":

- **Fecha de la operación** si es diferente a la fecha de la factura
- **Clave tipo factura** como "Justificante Contable" (F6)
- **Descripción SII** que corresponda

Al registrar esta factura, el impuesto seleccionado será del tipo:

- Importaciones 21%=0%

Podemos indicar el tipo de cambio de la divisa (USD) a EUR en la factura, pestaña "Tipo de cambio", ya que todas las operaciones que se registren en SII deberán estar en euros. De no indicarse tipo de cambio en esta pestaña se tomará el tipo de cambio configurado en la ventana "Rangos de conversión" para la fecha de la factura.

Una vez completada la factura, se procede a su Alta en SII, bien de forma manual o automática.

El XML de alta en SII contendrá la siguiente información:

- un tipo de Factura "F6"
- con clave régimen especial "13" (Factura correspondiente a una importación (informada sin asociar a un DUA).)
- e información en euros de la base imponible de la factura del proveedor extranjero.

![](../../../../../assets/drive/yv6n8NS37hU1NicRu2Rw0r0TtaClew1amM4KkLpPf2jCiX6AbV1oE2XVroCIIsOOvMZRfE1phnO6hcgL_CPUyyq8bn2gUpowhkQ2WOaCotbfNO-CeFwKXv1QR-GrBsvGJctagqLNNobK8eDZMyVaQLg.png)

Es importante recalcar que habiendo registrado un DUA (Caso 3 siguiente) no es necesario registrar la factura del proveedor extranjero.

##### **Caso 2 - Factura de transitario (un DUA)**

F&B España recibe una factura de transitario, junto con el correspondiente DUA, y referenciada a la aduana de destino de la mercancía, con posterioridad recibe la factura del proveedor extranjero.

La forma de registrar en Etendo la factura de transitario que incluye el IVA de importación será la siguiente:

- en la ventana "**Factura (Proveedor)**" creamos una nueva factura de compra, y seleccionamos el "Transitario" en el campo "Tercero".  
  Introducimos en el campo "Referencia del Proveedor", el número de factura del transitario.
- en el grupo de campos "**AEAT SII**" introducimos la siguiente información:
  - **fecha de operación**, si es distinta de la fecha factura del transitario
  - **clave tipo factura** como "**Importación (DUA)**" (F5)
  - seleccionamos la "**Descripción SII**" correspondiente
- en el grupo de campos "**Import (DUA)**" introducimos:
  - el **número de DUA**
  - la **fecha de admisión del DUA**, que aparece en el DUA en la sección "Control por la aduana de destino"
- en la pestaña "**Líneas**" introducimos la prestación de servicios del transitario sujeta y no exenta, en euros, con una base imponible de 500 €, por ejemplo; así como el resto de líneas de la factura del transitario por conceptos exentos de IVA del tipo "seguro" o "flete".
- en la pestaña "**Impuestos**" creamos una nueva línea de impuestos con el tipo de impuesto "Importaciones 21%". En el campo "Base Imponible" introducimos la base imponible de importación, reflejada en la casilla 47 del DUA.

![](../../../../../assets/drive/vQSib6h0rlB988u0S84IkPdDUQWZOVwPLTHBjgTRPXDjrmWMLf4Ix0K901j0Cw-5coy52rLVU5M-Bzki63aleZoqmv2BtYqrKxpQe7qms2C8DNJLn77KoQZpoUnBBnfLrx83uf6_HzeGpa68qGnIerU.png)

Una vez completada la factura, se procede a su Alta en SII, bien de forma manual o automática.

El XML de alta en SII contendrá la siguiente información:

- el alta/registro del DUA con
  - la clave tipo de factura "F5"
  - el número de DUA que se verá reflejado en la etiqueta del XML \<sii:NumSerieFacturaEmisor>
  - la fecha de admisión del DUA como fecha de registro contable, que se verá reflejado en la etiqueta del XML \<sii:FechaExpedicionFacturaEmisor>
  - F&B España como "contraparte" de la operación (Importador)
  - la clave de régimen especial 01 (Régimen General)
  - y los importes correspondientes a la base imponible, tipo y cuota del impuesto (cuota deducible) en euros

![](../../../../../assets/drive/ZJPF4ktKtyLgWY4KCQFHWYC_C5ZQJEg0t000RLzZGUTlFRCBJFL1THMSRDs_bJADn_rImCucvOFJpYvR75hrwmrNdg77Phspx5yAfSb_skBHnDhkxueRi7cUrz5nPdqn2MaBrF2_vAPkarH6n8BYtko.png)

- el alta/registro de la factura del proveedor (Transitario) con
  - la clave tipo de factura "F1"
  - el número de referencia/factura del transitario
  - la fecha contable de la factura del transitario como fecha de registro contable
  - el "Transitario" como contrapartida de la operación
  - la clave de régimen especial 01 (Régimen General)
  - y los importes correspondientes a la base imponible, tipo y cuota del impuesto (cuota deducible) en euros, por la prestación de servicios sujeta y no exenta.

![](../../../../../assets/drive/4pMaJ6g3yMj7fZotizXLbgwfpFLPziqoQOUdxahcLyupnKiZgG-VwpIhhDTTzXoSxbsx4-5NKG7CtYwDIDaVGWm_Hts8AiKdQQ4Vlv3zF4rFnWMwLJLZoPbkRCSnCa7K9gmxiqUCuO_RU1L9xcZHM8w.png)

Respecto de la factura del proveedor extranjero, ésta se deberá registrar también en la ventana "Factura Proveedor", en la divisa que corresponda y, con la clave de tipo de factura "Factura" (F1).

Al registrar este tipo de facturas en Etendo, el rango de impuestos utilizado será del tipo "Importaciones 21%=>0%", dado que dichas facturas de proveedor extranjero no incluyen IVA.

La AEAT no obliga a dar de alta en SII este tipo de facturas de proveedor extranjero, siempre que se reciban con posterioridad al DUA correspondiente, pero es posible enviarlas, en cuyo caso se darán de alta con la siguiente información:

- clave tipo de factura "F1"

##### **Caso 3 - Factura de transitario (Varios DUAS)**

F&B España recibe una factura de transitario, acompañada de tres DUAS que corresponden a diferentes partidas de mercancía importadas. Con posterioridad, recibe la factura del proveedor extranjero.

La forma de registrar en Etendo la factura de transitario que incluye varios documentos referentes al IVA liquidado en la aduana de destino es la siguiente:

- en la ventana "**Factura (Proveedor)**" creamos una nueva factura de compra, y seleccionamos el "Transitario" en el campo "Tercero".  
  Introducimos en el campo "Referencia del Proveedor", el número de factura del transitario.
- en el grupo de campos "**AEAT SII**" introducimos la siguiente información:
  - **fecha de operación**, si es distinta de la fecha factura del transitario
  - **clave tipo factura** como "**Importación (DUA)**" (F5)
  - seleccionamos la "**Descripción SII**" correspondiente
- en este escenario no rellenamos los campos "**Import (DUA)**" de la cabecera, ya que los datos **número de DUA** y **fecha de admisión del DUA** los vamos a asociar a la línea de impuesto correspondiente al IVA liquidado en aduana.  
  Para ello activamos el check "**Multiple DUA**" que va a permitir introducir líneas sin haber informado los campos anteriores.
- en la pestaña "**Lineas**" introducimos la prestación de servicios del transitario sujeta y no exenta, en euros, con una base imponible de 700 €, por ejemplo; así como el resto de líneas de la factura del transitario por conceptos exentos de IVA del tipo "seguro" o "flete".
- en la pestaña "**Impuestos**" creamos tantas líneas de impuestos como DUAS, con el tipo de impuesto "Importaciones 21%" o "Importaciones 10%" con la siguiente información:
  - en el campo "Base Imponible" introducimos la base imponible de importación, reflejada en la casilla 47 del DUA.
  - el **número de DUA**
  - la **fecha de admisión del DUA**, que aparece en el DUA en la sección "Control por la aduana de destino"

##### **Caso 4 - IVA de importación Diferido (sólo un DUA)**

El diferimiento del IVA de importación permite que las empresas importadoras puedan incluir las cuotas de IVA devengadas en las importaciones en el Modelo 303 mensual de autoliquidación del IVA, como un parámetro de entrada, sin necesidad de anticipar el ingreso de dicho IVA en la aduana. La cuota de IVA se liquida en la aduana pero su pago se pospone al momento de liquidar el impuesto.

Hacienda pone a disposición de las empresas importadoras un servicio de [_Agencia Tributaria: Cómo consultar el IVA importación con diferimiento de pago_](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/consulta-iva-importacion.html){target="_blank"} para su liquidación en el Modelo 303 mensual correspondiente.

En estos casos, no se registra factura de transitario, pero si DUA y, por tanto, el DUA, esto es la deducibilidad del IVA de importación soportado, debe registrarse en Etendo junto a la factura del proveedor extranjero de la siguiente forma:

- en el grupo de campos "**AEAT SII**" introducimos la siguiente información:
  - **fecha de operación**, si es distinta de la fecha factura del transitario
  - **clave tipo factura** como "**Importación (DUA)**" (F5)
  - seleccionamos la "**Descripción maestro SII**" correspondiente
- en el grupo de campos "**Import (DUA)**" introducimos:
  - el **número de DUA**
  - la **fecha de admisión del DUA**, que aparece en el DUA en la sección "Control por la aduana de destino".
- en la pestaña "**Líneas**" introducimos en euros los conceptos incluidos en la factura del proveedor extranjero relacionados con tipos impositivos del tipo "Importaciones 21%=0%".

Finalmente, el usuario de forma manual, deberá realizar los cambios que se indican a continuación, en la pestaña "Impuestos":

- creación de una nueva línea relacionada con el impuesto "**Importaciones 21%**", con el fin de reflejar la base imponible (casilla 47 del DUA) y, por tanto, el IVA de importación correspondiente.
- creación de una nueva línea relacionada con el impuesto "**Importaciones 21%=0%**", con una base imponible y cuota negativa del mismo importe que la anterior, para evitar duplicar la base imponible.

Hay que tener en cuenta que el importe del DUA vendrá indicado en euros. No es posible mezclar líneas en diferentes divisas en la misma factura, por lo que al introducir la factura de proveedor extranjero junto al DUA deberá existir una única divisa en euros.

![](../../../../../assets/drive/hQRaZcDRImXLJ1uxBUsDD45E2fdO1ljdl_vdmoJYdQ3zxWNLNCDwiU6Nl2mXF2XA92JGyxnwkfXlOuiK9uIEv0pjGxeQF1d_jzYdZTsoreulXX2HU3ExUFsjQQE7l2td1kyuZEfOZ5LLB7nOblD44Fg.png)

Una vez completada la factura, se procede a su Alta en SII, bien de forma manual o automática.

El XML de alta en SII contendrá únicamente la información de la parte correspondiente al DUA con la siguiente estructura:

![](../../../../../assets/drive/41ktdG4IiR4yFuhrvP8jBdJPBedtzT2ibeHHHiiznkxlcR7S9cV2ZEqEbz42RLvmRO7QUkOKEJSz2D0QBGGdR_DAAwX4DtZUateDK6RV-PUIn_kcGyfdlI9t6m2jQsbfXcF0KOHytWPSLapBl_-yh_E.png)

_Al introducir la línea de impuestos del tipo "Importaciones 21" referido al IVA de importación soportado, no hay que volver a introducir esta línea en la factura del transitario si en su caso la hubiera._

_En tal caso, al registrar la factura del transitario independientemente sólo habría que indicar las líneas correspondientes a dicha factura indicando como Clave tipo factura = Factura (F1)_

#### **Tercero (Proveedor) Intracomunitario**

Factura recibida por una adquisición intracomunitaria de bienes y servicios.

La empresa F&B España compra una partida de mercancía de un país comunitario.

Dicha compra incluye también la prestación de un servicio que presta el mismo proveedor intracomunitario. Dicho servicio se localiza en TAI (Territorio de aplicación del impuesto).

La empresa F&B España recibe la factura de fecha 27-11-2017, con fecha 30-11-2017, registrando dicha operación contablemente ese mismo día. La operación se realizó con fecha 15-10-2017.

En este caso al ser la fecha contable de la factura posterior al 16-11-2017, habiéndose realizado ésta en octubre, se incluirá en el Modelo 303 de noviembre.

La fecha límite de registro y envío al SII es el 14 de diciembre, contando a partir del registro contable de la factura (30-11-2017) y teniendo en cuenta los festivos nacionales (6 y 8 de diciembre).

Al registrar esta factura en Etendo, los tipos de impuestos que se seleccionan por defecto serán del tipo:

- Adquisiciones intracomunitarias 21% (para la adquisición de la mercancía)
- Inversión Sujeto Pasivo UE 21% (para la prestación del servicio y localización del mismo en España).

Una vez completada la factura, se procede a su Alta en SII, bien de forma manual o automática.

El XML de alta en SII contendrá la siguiente información:

- un tipo de Factura "F1"
- con clave régimen especial "09" (Adquisiciones Intracomunitarias de bienes y prestaciones de servicios)

![](../../../../../assets/drive/mMuCVKFYyjCifvhuXcjK52_gRt7sDUvQu_W3ZOzNLJ_zm12hQcpGkPR4j1PSFUkeZiGGL2YdbtiiGZHYX-g63Wa8O0w275WkSQaoHvu5nt3ykRCXDw876iQBgNdTCtMJulXfB2J3WrmNFsuck8I74UI.png)

Es importante recalcar que:

- si la factura de compra intracomunitaria incluye más de un bien al mismo/distinto tipo impositivo, en el XML la información se mostrará agrupada por tipo impositivo, dentro del nodo "DesgloseIVA/DetalleIVA"
- si la factura de compra intracomunitaria incluye más de un servicio al mismo/distingo tipo impositivo, en el XML la información se mostrará agrupada por tipo impositivo, dentro del nodo "InversiónSujetoPasivo/DetalleIVA"

#### **Organización/Operación acogida al RECC**

F&B España se encuentra acogida al régimen especial de criterio de caja, o bien se ve afectada por este régimen al recibir facturas de compra de algún proveedor nacional acogido al criterio de caja.

Al registrar este tipo de factura de compra en Etendo, los tipos de impuestos que se selecciona por defecto serán del tipo:

- Adquisiciones IVA 10% IVA de Caja.
- Prestación servicios nacional 21% IVA de Caja.

Al igual que en las facturas de venta con IVA de Caja, la información de estas operaciones se suministrará en los plazos generales como si a las mismas no les hubiera sido de aplicación el régimen especial.

Una vez completada la factura, se procede a su Alta en SII, bien de forma manual o automática.

El XML de alta en SII contendrá la siguiente información:

- un tipo de Factura "F1"
- con clave régimen especial "07" (Régimen especial del criterio de caja)

![](../../../../../assets/drive/mO8mH-cFpIjIEhf7x8OIEFtgg6cbSDoi6Bma3vizcThfAP1A4BFdemNNaydfBiIG2WQkpsNn83DjhVPR5bqoAsDkk0sG6fqOpuvGn3KMcgyvVjq_DtdjZVdVOxAuWLzq3UfxQbIy794DJKj219pOy6M.png)

Es importante recalcar que:

- si la factura de compra nacional incluye más de un bien/servicio al mismo/distinto tipo impositivo de IVA de Caja, en el XML la información se mostrará agrupada por tipo impositivo, dentro del nodo "DesgloseIVA/DetalleIVA"

#### **Pagos de facturas en RECC**

Los pagos totales o parciales de facturas en RECC deben darse de alta en SII en el momento de producirse.

Desde la ventana "Monitor SII" podemos filtrar por el número de pago y proceder a su envío a SII.

Una vez dado de alta en SII, el XML generado informa de los siguientes datos del pago, referenciados al número de la factura de compra:

- **Fecha**
- **Importe**
- **Medio**

![](../../../../../assets/drive/pTf6aP4P4yYSU7eESj_WiuFr1XYE_4hk8WEz5XcZ6g8pe7TApPwnYGTNX201Hfibrhyjd09RryZ8HEAJp0kROlrZP-88pas8JvfcfbY6wHWI-I8H0gOWndeLzJf9r23nigKinsyKyPNVnc3ew_RAUyA.png)

El Medio que en nuestro ejemplo es el 02 (Cheque), debe configurarse en el Método de Pago, campo "**Tipo**".

**Anulación de pagos**

En el caso de los libros registro de pagos en RECC no se utilizará el tipo de comunicación A1 de "Modificación de facturas/registros por error registral".

La modificación de un pago en RECC ya dado de alta en SII se efectuará enviando el pago que se pretende anular en negativo.

Lo anterior implica que en Etendo, al igual que se ha explicado para los cobros en RECC, no podremos reactivar un pago en RECC dado de alta en SII, si no que tendremos que revertirlo, con la opción "Revertir pago".

Al revertir el pago, Etendo genera un nuevo pago por el mismo importe en negativo que tendremos que dar de alta en SII desde la ventana "Monitor SII", tal y como se muestra en la siguiente imagen:

![](../../../../../assets/drive/1aPMk2pmJYGzATaN_B1dI0Ri4wunDMRoW.png)

El XML generado contendrá la siguiente información:

- el importe de pago negativo
- referencia a la factura original del proveedor.

![](../../../../../assets/drive/y6EpMi-6Kruil15GnhETYhDk_slSzWNJ9PON68Q7NnT5k1DkUiqK7izhcAOMC7Hrg5bpI3V2elPMiHTUhsCNIYVca7tBMjhr6Uytqd_Bt9Wa6_JEtOfigV6nZjbIU4rknuZoYjqOXuk1Bg_X0RSSioI.png)

**Facturas en RECC no pagadas en el año natural** (en desarrollo).

Como parte de la funcionalidad del RECC, Etendo permite la "liquidación manual del IVA de Caja" para aquellas facturas en RECC que no fuesen pagadas total o parcialmente antes del 31 de diciembre del año posterior al año de su expedición, produciéndose así el devengo del impuesto.

Por tanto, las facturas en RECC de fecha 2017 que no estén pagadas a 31-12-2018, tendrán que enviarse a SII en dicha fecha, y con la siguiente información:

- **Fecha** (de pago) = 31-12-2018 (fecha de la liquidación manual del IVA)
- **Importe** = importe pendiente de pago de la factura
- **Medio** = 03 (No se cobra/No se paga)

Desde la ventana de "Liquidación manual del IVA de Caja" será posible enviar estas liquidaciones manuales a SII, con fecha 31 de diciembre del año posterior al año de su expedición (devengo del impuesto).

#### **Compensaciones en las adquisiciones a personas acogidas al REAGYP**

Cuando se realicen operaciones por las que se satisfacen compensaciones agrarias del REAGYP se utilizarán impuestos específicos que por su naturaleza estarán configurados como REAGYP = SI.

Este tipo de impuestos de compensación agraria, están relacionados con las siguientes categorías de impuestos de terceros:

- Régimen Especial Agrario sobre "bruto" (IVA Incl.) (12%)
- Régimen Especial Agrario sobre base imponible (12%)
- Régimen Especial Agrario sobre base imponible (10,5%)

Al registrar este tipo de factura de compra en Etendo, en función del Tercero (Proveedor) seleccionado y su categoría de impuestos de tercero, los tipos de impuestos aplicables serán los siguientes:

- "Compensación REAGYP 12% -2%R (sobre bruto) SR", al calcularse el importe de la retención en el importe bruto, incluida la compensación.
- "Compensación REAGYP 12% -2%R (sobre BI) SR", al calcularse el importe de la retención directamente sobre la base imponible
- "Compensación REAGYP 10.5% -2%R (sobre BI) SR", al calcularse el importe de la retención directamente sobre la base imponible

F&B España S.A. compra una partida de mercancía a un proveedor nacional con un porcentaje de compensación del 12%. La compra se efectúa el 4 de septiembre, fecha en la que se expide la factura, recibiendo la misma cuatro días más tarde, el día 8. La empresa procede a su registro contable el día 11 de septiembre.

- Fecha de Operación: 4 de septiembre de 2017
- Fecha expedición de factura de venta: 4 de septiembre de 2017
- Fecha factura de compra: 4 de septiembre de 2017
- Fecha registro contable: 11 de septiembre
- Fecha límite de alta en SII: El plazo para emitir el registro es el 21 de septiembre, 8 días naturales desde la fecha del registro contable.

Además, este tipo de operación debe marcarse como una factura Tipo Justificante contable "F6".

Una vez completada la factura, se procede a su Alta en SII, de forma manual o automática.

![](../../../../../assets/drive/wud2a7NpPuk_Q-UxAlIHJUjblYTHj5NyUT8K2j5mhNIWHEbsLzYEK98yd8peDWvhmzXgTRss4hXNpJqe3TcWWx0MySWmd2M6VcZMcCioQnWVYOUrVQyNGuLTtm0fPBa9dJ9nalvW2oBwWPH6CEbYT38.png)

El XML de alta en SII contiene la siguiente información específica de este tipo de operación:

- Tipo de Factura "F6" (Justificante contable)
- Clave régimen especial "02" (Operaciones sujetas a REAGYP)
- Porcentaje Compensación REAGYP
- Importe compensación REAGYP

Consignará como **Base Imponible** la base sobre la que se calcula la compensación; como **Importe total** de la factura asignará el importe total de la contraprestación.

Al no ser un impuesto de IVA, los campos _tipo impositivo_ y _cuota soportada_ no se informarán.

![](../../../../../assets/drive/Aq-l5YH6S7ULiAFSK3xuSLR-ILBVh9mf-5nulQEGy7OQ9eAsi33K7Op31vjxp_QgXSe-zzjJkqVpWTslEHmMwTioPISRFsNrGcMRQUS4PKGUdr6Or8EcKZ30aavNtKW6BvRk3ncCf6BTZ2p_A7DdUaA.png)

En este régimen, podría producirse "autofacturación", es decir el receptor de la operación realiza la emisión de la factura en nombre del proveedor.

Para esos casos se ha creado el check "**Autofactura**" en el grupo de campos "AEAT SII" de la cabecera de las facturas de compra, que permite que el "Nº de Documento" de factura de Etendo se traslade al campo "Referencia de proveedor", tal y como se muestra en la imagen adjunta:

![](../../../../../assets/drive/kVdQsySjrBFfrCYtwfJcPCfQMeNJBmZnZJTnnuVdNPZbq5xZ1_7wpSwMcu8xqeJUCs6ctB1MmFhRPWVpZQwxA2C53rni_TYzg8NvsYv_CvI9C4mS0Ie17IGB8YIn5EPls_HN11zCuvtSDvfvlKTIVEs.png)

#### **Operación de compra sujeta a IPSI/IGIC**

F&B España S.A. compra una partida de mercancía en Canarias a un proveedor localizado en Canarias:

- La mercancía no se transporta a TAI, se queda en Canarias
- además la operación de compra incluye la prestación de un servicio que se localiza en Canarias y que por tanto también está sujeta a IGIC.

La compra y prestación del servicio se efectúa el día 15 de julio, con esa misma fecha se expide la factura, recibiendo la factura el día 26 de julio. La empresa procede a su registro contable el día 2 de agosto.

- Fecha de Operación: 15 de julio de 2017
- Fecha expedición de la factura de venta: 15 de julio de 2017
- Fecha factura de compra: 15 de julio de 2017
- Fecha Contable: 2 de agosto de 2017
- Fecha límite de alta en SII: El plazo para emitir el registro es el 14 de agosto, contando 8 días naturales desde la fecha del registro contable.

Al registrar este tipo de factura de compra en Etendo, los tipos de impuestos que se deberán seleccionar serán del tipo:

- Adquisiciones IGIC 9.5%
- Prestación servicios en Canarias 9.5%

Una vez completada la factura, se procede a su Alta en SII, bien de forma manual o automática.

El XML de alta en SII contendrá la siguiente información:

- un tipo de Factura "F1"
- con clave régimen especial "08" (Operaciones sujetas al IPSI / IGIC)

![](../../../../../assets/drive/4Uai4_Y5oJDKR3tpXAPMEsJbk-D7Dd7z6tNf8OppThhAN-RpmxWBPqy24eVOrsRymKC-gG7dqkPr9Q7L0BlLiCvUvxuqRR-aqNVdGrtcg4ZXmCb4W-GTLLiLbLeaASfDoYu8DpMGkP44lSGmPTT7KPY.png)

Es importante recalcar que:

- si la factura de compra incluye más de un bien/servicio al mismo/distinto tipo de IGIC, en el XML la información se mostrará agrupada por tipo impositivo, dentro del nodo "DesgloseIVA/DetalleIVA"

#### **Arrendamiento de local de negocio**

El arrendatario del local de negocio se limitará a registrar la factura recibida por el arrendamiento en Etendo.

Incluya o no retención el arrendamiento, la factura se deberá dar de alta con la clave de régimen especial 12.

Una vez completada la factura, se procede a su Alta en SII, bien de forma manual o automática.

El XML de alta en SII contendrá la siguiente información:

- un tipo de Factura "F1"
- con clave 12 (Operaciones de arrendamiento de local de negocio.)

![](../../../../../assets/drive/qTvK0Nls1j9WXhnmg_GjDdVSJ3f1SoSM2ZQ4HDVfH2PJxTHz1RbsB1-SVuGGtT7lsMY0uYAwxZwqYl4TXTpqYE-JqZp8YVnZRpp4i2wH39PvRWoCi5OvgM9XfH7jHAis1XGEejjA7EqIwaNeZG30-zI.png)

!!! info
    Si una factura de arrendamiento está sujeta al régimen especial del criterio de caja, prevalecerá la clave 07 de Operación Sujeta a RECC.

#### **Gastos de personal no declarables**

En el caso del registro de facturas de compra a empleados de la organización, por gastos de personal tales como dietas, se debe tener en cuenta lo siguiente:

- los empleados de la organización que incurran en gastos a reembolsar, tienen que tener la categoría de impuestos de tercero “No declarable SII” asociada.
- los gastos (productos de tipo “Gasto”) tienen que estar relacionados con el grupo de impuesto “No Sujeto Servicios”

en ese caso, las facturas de compra creadas en la organización para el reembolso de gastos a dichos empleados, se crearán con el rango de impuesto “No declarable gastos de empleado".

El registro de estas facturas de compra no se enviarán a SII, en ningún caso.

Una vez completada, si intenta enviar dichas facturas a SII se obtendrá el siguiente error:

![](../../../../../assets/drive/_50ZEl68hydwoSJZ27J5MrhxojDwPXnaTWRNM9OWNzJmoTTVcZBYBS70S5U82w9QE3Ln8r9EGQ_WXOeyV1mNNwRXp0Ym2gZIsgph7RVck2vAedl5DiyWn826OZtexzPRKEErqUuE6jwnd0x54Ybc604.png)

#### **Inversión del Sujeto Pasivo**

**Caso 1 = Inversión Sujeto Pasivo - Proveedor Extranjero**

La empresa F&B España adquiere de un proveedor extranjero una prestación de servicios que se localiza en TAI. Este proveedor se encuentra localizado en USA y tiene asociada una tarifa de precios en dólares.

Al registrar esta factura de compra los impuestos utilizados serán del tipo:

- Inversión Sujeto Pasivo no UE 21%.

El importe de la operación en dólares es de 500.00 USD, con un contravalor en EUR de 446.62, ya que:

- será posible utilizar el tipo de conversión según la fecha de factura configurado a nivel de sistema en la ventana "Rangos de conversión"
- o bien, el "Tipo de cambio" introducido en la propia factura de compra.

Una vez completada la factura, se procede a su Alta en SII, bien de forma manual o automática.

El XML de alta en SII contendrá la siguiente información:

- un tipo de Factura "F1"
- con clave regimen especial "01" (Régimen General)
- con información en "EUR" de la base imponible, tipo impositivo y cuota del impuesto dentro del nodo "Desglose Factura/InversiónSujetoPasivo/DetalleIVA".

![](../../../../../assets/drive/hrEpwYN4FiCksO7FAiQzwIZ39yOlBukNGoPtMKYvmdpGF5IXO1D_urMrMfXKD0t8aCcJlw8KCHM5J6q1gV3Ug9Y0L_e5M16s2AVszoG0iK1jOvBmI29xB45RE56Ce3d-LIK9NwdVgQT9WAoH6AxssRE.png)

Es importante recalcar que si este tipo de facturas incluyen más de un tipo impositivo igual/diferente respecto de la prestación del servicio, se agrupará por tipo impositivo dentro del nodo "Desglose Factura/InversiónSujetoPasivo/DetalleIVA".

**Caso 2 = Inversión Sujeto Pasivo - Proveedor Nacional**

F&B España recibe una factura de otro empresario que emite su factura sin IVA por producirse dicha operación bajo la figura fiscal de "Inversión del Sujeto Pasivo", de modo que F&B España registra dicha operación a través de una factura de compra con Inversión del Sujeto Pasivo.

Al registrar esta factura de compra los impuestos utilizados serán del tipo:

- Inversión Sujeto Pasivo nacional 21%.

Una vez completada la factura, se procede a su Alta en SII, bien de forma manual o automática.

El XML de alta en SII contendrá la siguiente información:

- un tipo de Factura "F1"
- con clave regimen especial "01" (Régimen General)
- con información de la base imponible, tipo impositivo y cuota del impuesto dentro del nodo "Desglose Factura/InversiónSujetoPasivo/DetalleIVA".

![](../../../../../assets/drive/3da4kENkcjtstpllmIbdw0WajedAkdQIXOaDaagog0swox0L6wRRShSz49ALoQUizqHVOHueaLugaUmJMsC0uIrFnHxVM4uKal40DBmzs143qQSoZ0iiWf-6KfE8-68P6bM1u2P9K07zORWCNzsUwxA.png)

#### **Factura recibida con fecha contable anterior al 01-07-2017**

Respecto de las facturas recibidas antes del día 01-07-2017, existe también la obligación de su alta en SII, pero con un esquema XML con las siguientes particularidades:

- **Clave de régimen especial** = 14 (Primer semestre 2017).
- **Descripción de la operación**: “Registro del Primer semestre 2017”.

Y, en el caso de las facturas recibidas:

- la "**Fecha registro contable**" será la fecha del envío o alta en SII
- y la "**Cuota deducible**" se fija a 0.00

Lo anterior aplica excepto para sujetos pasivos en REDEME que ya las habrán enviado en el Modelo 340 correspondiente.

En Etendo, al dar de alta en SII una factura recibida con fecha anterior al 01-07-2017, comprobaremos que el esquema XML es del tipo siguiente:

![](../../../../../assets/drive/zt8vxem5cYRQdfY3JQx8syUeoOnxML5LP-obvW0mPL9cfBSER1CL7cMmMUwuWdC33x9F4qsfeI56hCUmnkXN0Y2q-N-tDqAFQD8kp-6U5EVa3vhdokk9P9cckJmUv2D9STo_Orr-eejl2_5Yb8ZcViw.png)

En Etendo se ha desarrollado un proceso "Es en segundo plano" que adapta las facturas de venta del primer semestre para que puedan darse de alta en SII.

Este proceso se denomina "**Proceso de adaptación a SII de Facturas de Compra del primer semestre de 2017**" y configura dichas facturas con:

- la clave tipo factura **"Factura" = "F1"**, en el caso de facturas de compra positivas y negativas
- o **"Importación (DUA)" = "F5"**, en el caso de facturas de compra que incluyan un impuesto del tipo "Importaciones", en la pestaña "Impuestos".  
  En estos casos el usuario final tendrá que informar los campos "**DUA**" y "**DUA date**", antes de dar de alta en SII dichas facturas.
- añade la descripción tipo "**Registro del Primer semestre**"
- e indica como "**Fecha de operación**" la fecha de la factura tal y como requiere la AEAT.  
  El usuario siempre podrá revisar la configuración otorgada a dichas facturas antes de darlas de alta en SII

Al dar de alta en SII la factura de compra del primer semestre ya adaptada por el proceso, se informará el campo "**Fecha registro contable**" con la fecha de alta en SII.

La ventana "Monitor SII" incluye también una pestaña "Facturas de Compra Primer Semestre 2017" desde dónde se pueden gestionar estás facturas, una vez configuradas de forma correcta por el proceso.

#### **Factura recibida con IVA soportado no deducible**

Etendo permite la configuración de impuestos de compra no deducibles, tal y como se muestra en la siguiente imagen.

![](../../../../../assets/drive/Qu8LkkDz0cuEFwv-abefDr6gMz7pBewViFk3FdE9eOSzKvZAwucoYjgDvD4zckjxG--t75cmEUxloTFi8SDuureO55V5W1XY9Xbdc3EE0TKG4LW87ZOM3DZ_Rzq7ZJXozBXIRVNwNyBAL8la_J4LTJU.png)

Las facturas de compra que incluyan ese tipo de impuestos, tendrán que darse de alta en SII, tal y como se describe a continuación:

- en la etiqueta "Cuota Soportada", se refleja la cuota soportada
- y en la etiqueta "Cuota Deducible'', se refleja un "0".

![](../../../../../assets/drive/gpb9xZr8kbpoaTim4gGCbBGzKjz393sov8TOW8yBBqIMYfJ-4-vO9ZjaIBP6PDtFc5YiYJd8sDYupg4PeWM0dHltwqIczfMO_XxzbsCPXD-IJLEYZPyN850pc7lbBaeFBGnfZgtGEtysZ28nPehDpt8.png)

En el caso de impuestos que incluyan parte deducible y parte no deducible, la información a enviar será tal y como se muestra en la siguiente imagen:

- en la etiqueta "Cuota Soportada", se refleja la cuota soportada
- y en la etiqueta "Cuota Deducible'', se refleja el importe de esa cuota que sea deducible.

![](../../../../../assets/drive/itUfZLKo8uBuD5Cv1_2yx5gKK7-0cSLb0MbxoEccSV_OAov_gQtTJL7Q69Inaw8SJm-moaZwoa-N2nqPwxe4SHtAQyEGu4rT5eQbemFSyUzWWYNEMzkDxRzD-nGiBFw0dhNQB1sSZKAPYyShYSA1a1k.png)

### **Informes de comprobación SII (Consultas)**

Desde la ventana “**Consulta Facturas SII**” es posible establecer una comunicación inmediata con la AEAT. En esta comunicación, la AEAT proporciona un listado informativo de las facturas emitidas y recibidas en SII con estado “Correcto”.

Esta información es básica para poder conocer el proceso de contraste de los LFRE y LFRR.

![](../../../../../assets/drive/7ntfirTf-NO6P8Tp-1jGiD2XKOkzSe-CanqYwZTIHgjMZ_d4oROIuvLTrf6suQ3pF50VOpJjyJoDs1Mpwxty4lBUkRL7F80m9ilSnh_Axoiv744HoOe-H2_4K7U9PenR41VVk0X-SdFZ5_a06wb7M70.png)

Seleccionando la organización que va a ser objeto de consulta, accedemos a través de “Nueva Consulta Facturas a SII” a una ventana emergente en la que filtraremos por diferentes criterios para obtener la correspondiente relación de facturas.

Los diferentes criterios que se pueden aplicar para seleccionar la información a consultar a la AEAT, son los siguientes:

- **Libro de facturas**
  - Emitidas
  - Recibidas
- **Ejercicio**: carácter anual.
- **Periodo**: carácter mensual.  
  Este periodo se refiere a la fecha de emisión de la factura.
- **Fecha presentación (desde)**
- **Fecha presentación (hasta)**
- **Estado de cuadre SII**: Una vez validado el envío de facturas presentado, de forma casi inmediata se procede a ejecutar el proceso de contraste, cuyo primer paso es tipificar la factura como contrastable o no:
  - **No contrastable**: implica que nunca va a ser contrastada. Esta circunstancia se va a producir cuando el emisor o receptor no está en el sistema SII. En estos supuestos no se va a disponer en el sistema de posibilidad de contrastar esa información. Si la factura no resulta contrastable, la factura permanece en el estado “No contrastable” y no se intenta su cuadre. Ejemplos: las facturas simplificadas o las facturas cuya contraparte no aplica el SII.
  - **Contrastable**: comprobada la posibilidad de efectuar el contraste, se procede a determinar si esa información de registro remitida por una parte ha sido remitida por la contraparte. Los estados resultantes pueden ser:
  - **No contrastada**: No está la factura de la contraparte dada de alta en SII.

Si no se localiza la factura queda en estado de **no contrastada.**

Si la factura se localiza en el sistema, se ejecuta un proceso adicional para contrastar la información contenida en ambos registros remitidos por las partes:

- Si coinciden los criterios de contraste que se determinen, se considera **Contrastada**.
- Si no coinciden todos ellos será **parcialmente contrastada**. En este último caso, se proporcionará al contribuyente los resultados de contraste no coincidentes para su revisión.

Para poder efectuar la consulta, será obligatorio completar los campos: _Libro de facturas, ejercicio y periodo_.

Tal y como se muestra en la siguiente imagen, obtenemos un listado actualizado según los filtros establecidos anteriormente, ya que una organización acogida a SII podrá consultar los datos enviados (Libros registro declarados) desde la ventana "Consultas Facturas SII"

![](../../../../../assets/drive/FTSFjSPwCBgmtGl6WUOV-8tWW64aCeDEpEzCAWGKk4ISvRPZveZSbdG7kMVRrTmZpqm6ZGeKxdB-NN-DBH6bb36VKP-BvRtFQFemHI8AuchI7eH3SG2Dm9aXRAioiXgsZvfXWzGKy8U3wSaPlPxG8UU.png)

---

Este trabajo es una obra derivada de [Openbravo Localización Española](https://wiki.openbravo.com/wiki/Openbravo_Localizaci%C3%B3n_Espa%C3%B1a){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo licencia [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.