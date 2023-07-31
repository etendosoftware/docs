---
title: Libro de facturas
---
## **Introducción**

Este módulo de funcionalidad española se denomina “Libros Registro de IVA” o “Libros Registro de Facturas emitidas/recibidas”.

## **Descripción del módulo**

Este módulo de los libros registro de IVA permite a las empresas españolas generar los libros registro de IVA, tanto los libros de facturas recibidas (IVA soportado) como los libros de facturas emitidas (IVA repercutido). Las empresas españolas tienen que guardar registro de cada una de las facturas recibidas y emitidas con el fin de poder determinar el importe total de IVA a liquidar con la Hacienda Pública para un periodo de tiempo determinado, como diferencia entre el IVA repercutido y el IVA soportado deducible.

El contenido de los libros de facturas se ajusta a los requerimientos de la Hacienda Pública española. Los libros de facturas contienen información sobre:

-   Número de registro
    -   este número será generado automáticamente por el sistema una vez que el correspondiente libro se marque como "Final"
-   Número de factura emitida/recibida
    -   este número tanto en el caso de facturas recibidas como emitidas se corresponde con el campo "Nº documento"
    -   en el caso de las facturas recibidas dicho campo no debería llevar secuencia numérica asociada con el fin de que el usuario final pueda introducir el número de factura del proveedor.
-   Fecha factura emitida/recibida o fecha de expedición/recepción de los bienes/servicio, en caso de ser diferentes
-   Nombre y breve descripción del cliente/proveedor
-   NIF del cliente/proveedor
-   Base imponible
-   Tipo impositivo de IVA
-   Cuota de IVA repercutido/soportado
-   Cuota de IVA soportado deducible
-   Tipo impositivo de recargo de equivalencia
-   Cuota de recargo de equivalencia
-   Importe total de la factura

!!! info
    Los importes deben consignarse en Euros.


El tipo de cambio que se utiliza en las transacciones que deban incluirse en los libros cuyos importes no sean en Euros, es el definido para un rango de fecha determinado en la ventana "Rangos de Conversión".

Este módulo de funcionalidad incluye además las claves de libro correspondientes al modelo tributario español 340 de declaración informativa de operaciones incluidas en los libros registro

-   “E”= en el caso del libro de facturas emitidas  
      
-   “R”= en el caso del libro de facturas recibidas  

y también las claves de operación correspondientes al modelo tributario español 340 de declaración informativa de operaciones incluidas en los libros registro:

-   “ “= en el caso de operación habitual de compra/venta  
      
     
-   “C”= en el caso de factura de compra o venta con varios tipos impositivos  
      
     
-   “D”= en el caso de factura de compra o venta rectificativa o nota de abono  
      
     
-   “I”= en el caso de inversión de sujeto pasivo  
      
     
-   “R” = en caso de facturas de arrendamiento de local de negocio (nueva clave para 2012)

En los libros registro de IVA se consideran las siguientes operaciones de compra relacionadas con los tipos de documento de Etendo que se listan a continuación:

-   Facturas de compra (Tipo de documento = “AP invoice” )
-   Facturas de compra negativas (Tipo de documento = “AP invoice”) o abonos (Tipo de documento = "Reverse Purchase Invoice"). Ambos tipos implican una nota de abono en negativo.
-   Notas de abono de compra (Tipo de documento = “AP CreditMemo”), lo cual implicaría una factura rectificativa o nota de abono en positivo. En este caso, hay que tener en cuenta que el libro de IVA de facturas recibidas marcará este tipo de operaciones como “D” con importes en positivo, aunque impliquen un IVA soportado negativo y, por tanto, menor IVA soportado/soportado deducible.

En los libros registro de IVA se consideran las siguientes operaciones de venta relacionadas con los tipos de documento de Etendo que se listan a continuación:

-   Facturas de venta (Tipo de documento = “AR invoice” )
-   Facturas de venta negativas (Tipo de documento = “AR invoice”) o abonos (Tio de documento="Reverse Sales Invoice"). Ambos tipos implican una nota de abono en negativo.
-   Notas de abono de venta (Tipo de documento = “AR CreditMemo”), lo cual implicaría una factura rectificativa o nota de abono en positivo. En este caso hay que tener en cuenta que el libro de IVA de facturas emitidas listará este tipo de operaciones en positivo, aunque impliquen un IVA repercutido negativo y, por tanto, menor IVA repercutido.

No se consideran los libros registro de IVA del tipo:

-   Libro registro de ciertas operaciones Intracomunitarias
-   Libro registro de bienes de Inversión

así como las:

-   Operaciones de nota de abono de compra/venta negativas (Tipo de documento = “AP/AR CreditMemo”), lo cual implicaría una factura de compra/venta.

## **Instalación del módulo**

Para la instalación del módulo “Libro de facturas”, el usuario debe seguir los pasos que se describen a continuación en función de la situación de partida:

-   Instalación de la última versión disponible de Etendo 
-   o la instalación del módulo de Localización Española.

!!! info
    Para la instalación del módulo de Localización Española, visite [_Marketplace_](https://marketplace.etendo.cloud/#/product-details?module=003B475055DD421B9483B5BE15AA48C5). 


Este módulo de funcionalidad requiere el módulo de Impuestos para España de Etendo. Es importante tener en cuenta que a la hora de instalar el módulo del libro de facturas, los módulos dependientes se instalarán automáticamente.
> 
!!! info
    **Nota importante**: Las transacciones realizadas con anterioridad a la instalación del módulo de libro registro de facturas aparecerán en el correspondiente libro de facturas pero sin la clave de operación. Hay que tener en cuenta que la clave de operación solamente es necesaria en el modelo tributario 340. Para generar la clave de operación, las transacciones deberán completarse de nuevo.

## **Interfaz de usuario**

Tal y como se ha explicado en la sección “*Instalación del Módulo*”, los “Libros registro de IVA” requieren del módulo de impuestos para España mejorado que incluye 3 campos que permiten:

1.- la identificación de los importes de **recargo de equivalencia** tanto en el libro de facturas recibidas como emitidas de forma separada a los importes de IVA, si bien hay que tener en cuenta que los rangos de impuestos de recargo de equivalencia tienen que ir referidos al régimen del cliente/proveedor como una categoría de impuestos del cliente/proveedor.

2.- la identificación de las operaciones de **inversión de sujeto pasivo** para los casos de operaciones de servicios suministrados por parte de proveedores europeos/extranjeros a empresas españolas.

3.- la selección del **tipo de libro** aplicable a cada impuesto, debido a que por la configuración actual de los tipos impositivos se darán casos de impuestos de tipo compra que se deben incluir en el libro de facturas emitidas como IVA repercutido/venta. Un ejemplo es el IVA Intracomunitario de compras. El IVA Intracomunitario de compras implica un apunte al debe (como IVA repercutido) y otro al haber (como IVA soportado).

Estos 3 nuevos campos se encuentran en la ruta de aplicación “**Gestión Financiera / Contabilidad / Configuración / Rango impuesto”**.

!!! info
    **Nota importante:** En caso de que no se utilice el módulo de impuestos para España proporcionado por Etendo, el usuario debe tener en cuenta que necesita configurar de forma adecuada y manualmente los 3 parámetros básicos del libro de facturas explicados en esta sección. 

Además este módulo cuenta con dos ventanas para la configuración de los libros registro de IVA y la generación de los mismos, tal y como se muestra a continuación:

**Configuración de los libros de IVA**

Ruta: Gestión Financiera / Contabilidad / Configuración / Configuración de Libro de Facturas

![](/docs.etendo.software/assets/drive/GrG6D0PyhdbT_TLRpP-ucIUxQWXB195QfgnnOoCooFMRK3_UdE3CVkl5e-u4JKIm9XaZa5jlgs3MKgRXNtxUWKv5ZUSPy8jn96u3UzeFgFAM9xK1K3iQaadEg4m-4tJzEekLb2QEmIUReL3FFSu2T3GhAwhqXYbEUj2bWFTahFcOb_5QbJBoJUODVWN_CA.png)

**Generación de los libros de IVA**

Ruta: Gestión Financiera / Contabilidad / Herramientas de análisis/ Libro de facturas

![](/docs.etendo.software/assets/drive/loPMP2zWkOWGQYfmN6LTMPKteM1c0FpDnobtXCpuevnoP_ymLRTTP17h6YhVPEbK0Jxvi_Er9fhCfcGHAmifvo__4Oa0B4iLGjknSLMFgaC8T1GUkaqyKv_b7axuA6vYViAQYr5AAnnCRI9cQes9jvV-QT48duPSsMzBwN9QADTKJZsyqGc7LmNQOZiFyw.png)

## **Casos de usuario**

Esta funcionalidad permitirá a las empresas españolas llevar a cabo los escenarios que se explican a continuación una vez que las correspondientes facturas/abonos de compra y venta se han completado/contabilizado en Etendo para un determinado año/periodo, por ejemplo 2021/Enero/Febrero.

### **Configuración y creación de los libros**

Es necesario crear y configurar los libros de facturas recibidas y emitidas, para ello deberá seguir los pasos que se detallan a continuación o bien instalar y aplicar a la entidad legal con contabilidad el módulo de configuración de los libros de facturas.

El módulo de configuración de los libros:

-   crea los libros tanto de facturas recibidas como emitidas
-   y los configura añadiendo todos los impuestos por tipo de documento a tener en cuenta a la hora de generar los libros de facturas.

Es importante recalcar que el usuario puede crear los libros de facturas para un determinado periodo de tiempo tantas veces como sea necesario con tan solo volver a presionar el botón de proceso “Crear” para el correspondiente Libro, de esta forma se incluirán en el libro nuevas facturas o abonos que no se tuvieron en cuenta al crear el libro.

#### **Libro de Facturas Recibidas**

##### **Configuración**

Configuración del Libro de Facturas recibidas en la ruta de aplicación Gestión Financiera – Contabilidad – Configuración – Configuración de Libro de Facturas.

Una vez aplicado el dataset del módulo [Configuración de impuestos para el libro de facturas](https://docs.etendo.software/en/modules/spain-localization/manual-de-usuario/configuracion-de-impuestos-para-libro-de-facturas), el usuario puede comprobar la configuración de los libros de facturas que se ha creado por defecto para el libro de facturas recibidas.


Campos a tener en cuenta:

-   **Nombre** : Libro de Facturas Recibidas 2021
-   **Descripción** : Libro de Facturas Recibidas 2021
-   **Activo** : Sí
-   **Tipo**: R – Recibidas
-   **Nº inicial**: Este número se tendrá en cuenta al crear el libro como final, ya que a todas las transacciones o facturas incluidas en el libro habrá que asignarles un número de registro correlativo. El primer número asignado por defecto será el 1.

![](/docs.etendo.software/assets/drive/IXk_LbHGPAuvnqJO0OgUVrfZ-SOpTuzA9Wdl-wKAtmqZyaLqjv5om5qoPtpYl-508VUqsTJWgPPhnbLlYh1P9-drRWRiE3ZgN58uiycr6MdIYXayaz1hfLWPS0lJYV4ktVApRw9gKP7nbn5ezHlyCPRoO9D1tqo5W1e2DednQyS0Krh4qpRfakqWFyT8PA.png)

*Nota:* El usuario puede definir el **Número de Documento** que aparecerá en cada una de las líneas del libro, pudiendo ser: 
-   El Nº Factura (campo "Nº documento" de la factura de compra)
-   o el Nº Documento Proveedor (campo "Referencia del Proveedor" de la factura de compra) 

En la pestaña "**Impuestos**" el usuario puede comprobar el listado de todos los impuestos por tipo de documento que se han incluido en la configuración del libro de facturas recibidas y que, por tanto, se tendrán en cuenta a la hora de crear el libro.

##### **Creación**

La **creación del libro de facturas recibidas** se debe llevar a cabo desde la ruta de aplicación Gestión Financiera – Contabilidad – Herramientas de Análisis – Libro de facturas. El usuario debe crear un nuevo registro e introducir la siguiente información para el correspondiente Cliente/Organización:

-   **Nombre** : Libro de Facturas Recibidas Enero 2021
-   **Descripción** : Libro de Facturas Recibidas Enero 2021
-   **Activo** : Sí
-   **Libro de Facturas** : el usuario debe seleccionar el libro de facturas ya configurado, por ejemplo "Libro de Facturas Recibidas 2021".
-   **Ejercicio**: el usuario debe introducir el año (en el ejemplo, 2021)
-   **Desde Periodo** : el usuario debe introducir el periodo para el cual quiere que la fecha de las facturas se tenga en cuenta al lanzar el libro de facturas, por ejemplo enero 2021. El sistema incluirá las facturas con fecha desde el 1 de enero 2021.
-   **Hasta Periodo** : el usuario debe introducir el periodo hasta el cual quiere que la fecha de las facturas se tenga en cuenta al lanzar el libro de facturas, por ejemplo enero 2021. El sistema incluirá las facturas con fecha hasta el 31 de enero 2021.

Una vez introducida la información anterior, el usuario puede crear el libro mediante el botón de proceso “Crear” y comprobar las transacciones generadas en la pestaña “Líneas”.

![](/docs.etendo.software/assets/drive/GvTXD6nqhWoDk09XBU4LNxXPn81wG8PznqfHtMS3lI4NuiNwNZc1ogkyhqki6kcJnPsjkefAdwu2hyX7kqcvtxqwwLZ5m7q_U_93v-tu-TYnHSsn3-yP0Umnd-GvwqcUgJ280R80kJtIO9aCko3KN7HnJlw8ePE7avYq3kvhTfXn8ZFZsO4YzsvruBWF.png)

La información contenida en las líneas del libro es la que se muestra a continuación:

![](/docs.etendo.software/assets/drive/qk68QXzdYHjO1yKVcIG-WHMqCFoX0pJN8oCzkZP5CSVgReXjk0C43dB4ucckSUhXzLwG09yagjJvl14pAbhdBM1G_c6Y_enkOgCxfnSEPdrRGK6zUVxoIaTaoP6TOw3ejSKC4OrdJ740nB8ev0mERhCCHkhoIuT8dkk6g6tqayPEbcAgnsDde48ZxtUv.png)

#### **Libro de Facturas Emitidas**

##### **Configuración**

Configuración del Libro de Facturas emitidas en la ruta de aplicación Gestión Financiera – Contabilidad – Configuración – Configuración de Libro de Facturas.

Una vez aplicado dataset del módulo [Configuración de impuestos para el libro de facturas](https://docs.etendo.software/en/modules/spain-localization/manual-de-usuario/configuracion-de-impuestos-para-libro-de-facturas), el usuario puede comprobar la configuración de los libros de facturas que se ha creado por defecto para el libro de facturas emitidas.

Campos a tener en cuenta:

-   **Nombre** : Libro de Facturas Emitidas 2021
-   **Descripción** : Libro de Facturas Emitidas 2021
-   **Activo** : Sí
-   **Tipo**: E – Emitidas
-   **Nº inicial**: Este número se tendrá en cuenta al crear el libro como final, ya que a todas las transacciones o facturas incluidas en el libro habrá que asignares un número de registro correlativo.

![](/docs.etendo.software/assets/drive/U7zyB9bCxJ53qXJTCwT0NxvIDJ4gMZ3c5G9QLmsMWGRYYV1mKdK90kPhbtf9l8Ee7hhsNZApVcmY-2fnalHXgl8xf3BcPEDM3VNbqspYjkVZyysWBhR_QXGJA0-vnGn_20c8luy3ZIeqVbnyJ8pghgvC7dfkSuO9AmajeRFq-uqqHy8o9IoMQFu0azbj.png)

En la pestaña "Impuestos" el usuario puede comprobar el listado de todos los impuestos por tipo de documento que se han incluido en la configuración del libro de facturas emitidas y que, por tanto, se tendrán en cuenta a la hora de crear el libro.

##### **Creación**

La creación del libro de facturas emitidas se debe llevar a cabo desde la ruta de aplicación Gestión Financiera – Contabilidad – Herramientas de Análisis – Libro de facturas. El usuario debe crear un nuevo registro e introducir la siguiente información para el correspondiente Cliente/Organización:

-   **Nombre** : Libro de Facturas Emitidas Febrero 2021
-   **Descripción** : Libro de Facturas Emitidas Febrero 2021
-   **Activo** : Sí
-   **Libro de Facturas** : el usuario debe seleccionar el libro de facturas emitidas ya configurado que quiere crear, por ejemplo "Libro de Facturas Emitidas 2021".
-   **Ejercicio**: el usuario debe introducir el año (2021)
-   **Desde Periodo** : el usuario debe introducir el periodo para el cual quiere que la fecha de las facturas se tenga en cuenta al lanzar el libro de facturas, por ejemplo febrero 2012. El sistema incluirá las facturas con fecha desde 1 febrero 2012.
-   **Hasta Periodo** : el usuario debe introducir el periodo hasta el cual quiere que la fecha de las facturas se tenga en cuenta al lanzar el libro de facturas, por ejemplo febrero 2012. El sistema incluirá las facturas con fecha hasta el 28 de febrero de 2012.

Una vez introducida la información anterior, el usuario puede crear el libro mediante el botón de proceso “Crear” y comprobar las transacciones generadas en la pestaña “Lineas”.

![](/docs.etendo.software/assets/drive/4PIfpdoRUi3Yr61UjSdmHK4-wjU2TnkBEFbFqev8C0CbUrrIxM5c_gpKnY8zz2RyzNa2TvRTXEmgQzB_-tXJKUc11kRLCv-pHzX00pJhI_NAIzDlmTRxWw3R4xXZI2A4Ns87C9tAa9P6icxTDkN8yyHo4SXbOXGJbx620JaN4BUNPYFsRzr_ZTwgIksZtg.png)

La información contenida en las líneas del libro es la que se muestra a continuación:

![](/docs.etendo.software/assets/drive/7fv5JlzALOzMrSXXDvFubccNZBrZwSJm1VSNpczqK4u03ULPED0uOMR_TbM-q3uEwc0W_J9fqUZAdHFvaWt8K9G3zTL0vXz-N7nXENJdFG7-PuBSMVa0PiF1uTWabKTHJToOaoiJX8y9A7KUN7bUEvUKPXZz0BkBg6daCzUA7tze8XfVeFtaVw_cisfZEw.png)

### **Inclusión manual de transacciones**

El usuario puede añadir manualmente facturas/abonos tanto emitidos como recibidos que por cualquier motivo no estén registrados en Etendo, pero que deban ser incluidos en el libro correspondiente. Para ello el usuario deberá seguir los pasos que a continuación se detallan:

En la ruta Gestión Financiera / Contabilidad / Herramientas de Análisis / Libro de Facturas / Cabecera >> Líneas, el usuario puede crear un nuevo /s registro/s e introducir facturas o abonos tanto emitidos como recibidos de sus proveedores, en el libro correspondiente, con tal solo presionar el botón de menú “Nuevo”.

En ese caso, el usuario deberá introducir la información que se lista a continuación para cada nuevo registro creado manualmente:

-   Nº de documento (obligatorio)
-   Tercero (obligatorio)
-   Clave de operación
-   Base imponible (obligatorio)
-   Tipo impositivo (obligatorio)
-   Tipo de Recargo de equivalencia
-   Fecha documento
-   NIF del tercero (no editable, debe rellenarse al seleccionar el tercero)
-   Cuota del impuesto (obligatorio)
-   Cuota recargo de equivalencia (obligatorio). En caso de que no aplique el recargo de equivalencia se debe rellenar como 0,00
-   Importe total de la factura (obligatorio)

### **No inclusión de transacciones**

El usuario puede marcar manualmente facturas/abonos tanto emitidos como recibidos que por cualquier motivo no deban ser incluidos en el correspondiente libro y que estén registrados en Etendo, para ello el usuario deberá seguir los pasos que a continuación se detallan:

En la ruta Gestión Financiera / Contabilidad / Herramientas de Análisis / Libro de Facturas / Cabecera >> Líneas, el usuario puede “desmarcar” cualquier transacción que esté marcada por la aplicación como “Incluida”, dichas transacciones no se incluirán al crear el correspondiente libro como Final (documento impreso en formato \*.pdf).

### **Libros de facturas marcados como "Final"**

El usuario puede procesar los libros de facturas como “Finales”, una vez que se asegure de que las transacciones incluidas en el libro son las correctas, dicho proceso implicará la numeración correlativa de las facturas incluidas en dicho libro, siempre que el periodo o periodos a los que se refieren las facturas incluidas en el libro estén cerrados, al menos temporalmente.

Desde “Gestión Financiera / Contabilidad / Transacciones – Abrir/Cerrar Periodos”, el usuario debe cerrar temporalmente aquellos periodos para los que no se van a introducir nuevas facturas ni transacciones y que, por tanto, pueden cerrarse.

Una vez cerrados los periodos desde “Gestión Financiera / Herramientas de Análisis / Libro de Facturas”, el usuario puede "Crear y Marcar como Final" el correspondiente libro, con lo que el sistema dará opción a partir de ese momento tan solo de “Desprocesar”.

El usuario puede imprimir el libro mediante el botón de la barra de herramientas “Imprimir”.

El libro impreso (\*.pdf) de facturas recibidas incluye la siguiente información:

-   Número registro
-   Número factura
-   Nº Doc / Ref. Prov - esta columna relaciona ambos números de documento, el número de Etendo y el número o referencia del proveedor.
-   Fecha operación
-   Tercero
-   NIF
-   Clave
-   Base imponible
-   Tipo impositivo
-   Cuota impuesto
-   Cuota deducible
-   Importe factura
-   Fecha de pago
-   Cuenta Financiera
-   Método de Pago
-   Importe de Pago

El libro impreso (\*.pdf) de facturas emitidas incluye la siguiente información:

-   Número registro
-   Número factura
-   Fecha factura
-   Fecha operación
-   Tercero
-   NIF
-   Clave
-   Base imponible
-   Tipo impositivo
-   Cuota del impuesto
-   Recargo
-   Cuota RE
-   Importe factura
-   Fecha de cobro
-   Cuenta Financiera
-   Método de Pago
-   Importe de cobro

En caso de error u omisión en los libros, el usuario deberá desprocesar el correspondiente libro, reabrir el periodo/periodos, añadir o modificar la/las facturas emitidas o recibidas y volver a empezar el proceso de creación y procesamiento como final del correspondiente libro, teniendo en cuenta el/los periodos de facturación debido a que la numeración de registro debe ser correlativa en función de las fechas de factura.

Si el usuario tiene que introducir una factura de fecha de marzo y ya ha cerrado y generado como finales los libros de abril y mayo, deberá desprocesar los libros de mayo, abril y marzo; reabrir los periodos de mayo, abril y marzo; contabilizar la factura con fecha de marzo y finalmente, crear el libro de marzo para comprobar que la nueva factura se ha incluido en el libro de marzo, cerrar los periodos y crear y marcar como finales los libros de marzo, abril y mayo por ese orden.