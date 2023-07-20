---
title: Modelo 349
---
## **Introducción**

Esta sección aplica al módulo “**Modelo AEAT 349 - Declaración recapitulativa de operaciones intracomunitarias”** incluído en el módulo de Localización Española de Etendo.

### **Descripción del módulo**

El nuevo módulo de generación del Modelo 349 como un fichero “.txt” válido de acuerdo a los requisitos establecidos por la Hacienda Española (Orden HAC/360/2002 de 19 de febrero y modificada en última instancia por la Orden HAC/174/2020 de 28 de diciembre) permitirá a las empresas españolas cumplir con sus obligaciones fiscales de presentación de la declaración recapitulativa de las entregas y adquisiciones intracomunitarias de bienes que realicen.

De acuerdo con el reglamento del IVA, están obligados a presentar el modelo 349, los sujetos pasivos del Impuesto que realicen cualquiera de las siguientes operaciones:

-   Las entregas de bienes destinados a otro Estado miembro, entregas de bienes exentas del impuesto.
-   Las adquisiciones intracomunitarias de bienes sujetas al impuesto.
-   Las adquisiciones intracomunitarias de bienes y entregas subsiguientes exentas conocidas como “Operaciones Triangulares”

El contenido de la declaración recapitulativa de operaciones Intracomunitarias es:

-   Las operaciones citadas en el párrafo anterior, así como las rectificaciones a cualquiera de las operaciones anteriores ya incluidas en la correspondiente declaración recapitulativa.
-   Los datos de identificación de los proveedores y adquirientes
-   así como la base imponible en euros de las operaciones intracomunitarias de bienes declaradas.

En general, la declaración recapitulativa deberá presentarse por cada mes natural durante los veinte primeros días naturales del mes inmediato siguiente, salvo la correspondiente al mes de julio, que podrá presentarse durante el mes de agosto y los veinte primeros días naturales del mes de septiembre y la correspondiente al último período del año, que deberá presentarse durante los 30 primeros días naturales del mes de enero.

Cuando ni durante el trimestre de referencia ni en cada uno de los cuatro trimestres naturales anteriores el importe total de las entregas de bienes y prestaciones de servicios que deban consignarse en la declaración recapitulativa sea superior a 50.000 euros, excluido el Impuesto sobre el Valor Añadido, la declaración recapitulativa deberá presentarse durante los veinte primeros días naturales del mes inmediato siguiente al correspondiente período trimestral.

Si al final de cualquiera de los meses que componen cada trimestre natural se superará el importe mencionado en el párrafo anterior, deberá presentarse una declaración recapitulativa para el mes o los meses transcurridos desde el comienzo de dicho trimestre natural durante los veinte primeros días naturales inmediatos siguientes.

!!! info
    Desde 2020 se suprime el período anual de declaración.

Las operaciones se entenderán realizadas el día en que se expida la factura o documento equivalente que sirva de justificante de las mismas.

Debido a que en el modelo 349 se deben diferenciar aquellas notas de abono que son rectificación a facturas incluidas en modelos del 349 ya enviados a Hacienda y las notas de abono que no lo son, ha sido necesario crear una funcionalidad que relaciona las notas de abono con las facturas que están siendo abonadas o rectificadas, tal y como se explica en este documento en la sección “Casos de usuario. Operaciones rectificativas del 349”

!!! info
    El módulo de generación del Modelo 349 no incluye las operaciones triangulares, puesto que dichas operaciones no se gestionan en Etendo. 

Este módulo no tiene en cuenta las transacciones correspondientes al tipo de documento de Etendo “AP/AR credit memo” como facturas de abono, ya que dicho tipo de transacciones no reflejan devoluciones de mercancía, es por ello que el módulo 349 tendrá en cuenta los tipos de documento AP/AR invoice (como facturas de compra y venta) y los tipos de documento AP/AR invoice negativos (como notas de abono o facturas rectificativas).

Además, no se incluye en el módulo de funcionalidad el supuesto de Declaración Complementaria para aquellos casos en que deban incluirse solo las operaciones que, debiendo haber sido declaradas en otra declaración del mismo ejercicio presentada con anterioridad, no se incluyeron. Estas operaciones deberán ser incluidas por el usuario manualmente, a través de la página de la AEAT tal y como se explica en la sección de este documento “Declaración Complementaria”.

## **Instalación del módulo**

Para la instalación del módulo “Modelo AEAT 349 - Declaración recapitulativa de operaciones intracomunitarias”, el usuario debe seguir los pasos que se describen a continuación en función de la situación de partida:

-   Instalación de la última versión disponible de Etendo
-   o la instalación del módulo de Localización Española.

!!! info
    Para la instalación del módulo de Localización Española, visite [*Marketplace*](https://marketplace.etendo.cloud/#/product-details?module=003B475055DD421B9483B5BE15AA48C5). 

Es importante recalcar que:

-   El módulo del Modelo AEAT 349 incluye el correspondiente conjunto de datos que relaciona los tipos/rangos de impuestos con los parámetros del 349.
-   Una vez instalado el módulo, éste se debe aplicar a la Organización para la cual se requiere obtener el modelo 349, tal y como se describe en el apartado siguiente.

### **Aplicación del Módulo**

Una vez instalado el módulo del 349, el usuario debe aplicar el módulo del 349 a la organización legal con contabilidad que corresponda.

Es fundamental recalcar que el usuario debe tener el módulo de impuestos para España instalado y aplicado a la organización (\*) y, por tanto, a la organización legal para que se quiera obtener el 349, dicho módulo de impuestos para España es válido para todos los modelos de declaración de impuestos, en este caso el modelo de declaración del 349, y debe estar instalado previamente.

El usuario deberá navegar a "Configuración General / Gestión del módulo de Empresa", seleccionar la organización legal con contabilidad y aplicar los módulos en el orden especificado (primero el módulo de impuestos, si no está aplicado previamente, y después el módulo del 349).

### **Configuración del módulo para la organización con contabilidad**

Una vez instalado el módulo del 349 por cualquiera de los procedimientos anteriores, el usuario debe aplicar el módulo del 349 a la organización legal con contabilidad que corresponda.

Es fundamental recalcar que el usuario debe tener el módulo de impuestos para España instalado y aplicado a la organización legal con contabilidad previamente, dicho módulo de impuestos para España es válido para todos los modelos de declaración de impuestos, en este caso el modelo de declaración del 349, y debe estar instalado y aplicado a la organización previamente.

El usuario deberá navegar a "Configuración General / Gestión del módulo de Empresa", seleccionar la organización legal con contabilidad y aplicar los módulos en el orden especificado (primero el módulo de impuestos si no está aplicado previamente y después el módulo del 349).

## **Configuración del módulo**

### **Configuración del modelo 349**

Este módulo de generación del modelo 349 como un fichero de texto (“\*.txt”) válido conforme a los requerimientos de la Hacienda Pública Española, se basa en la funcionalidad del “Generador de declaraciones de impuestos”.

El usuario puede comprobar en la ruta de aplicación: Gestión Financiera / Contabilidad / Configuración / Declaración de Impuestos, que el modelo 349 está creado como informe anual, trimestral o mensual de impuestos, todos con la misma configuración:

![](https://lh4.googleusercontent.com/H0HWfOy7IdB5yLwjirTyqV4jjt9pCbVBTk0lZlXCnufLFyy1zAos1vJiKc0Wgsydgfs3H5RtRsFpPg7UcQXvX924p8_3Taq958X892bGQbJCsMqKjxmenrRR7j3NPFZTcbTE9oQgv9zdWwU9-ngWWh1cIdzW-78QmhNv6SBuuTAUSn_h_N9dotFwXQ)

En la pestaña “Secciones de la declaración” se han creado 4 secciones:

![](https://lh5.googleusercontent.com/vgoWI1diiY_P5qHvQxVKR-bl45Z8XjklTv3NmDsdvGUs47FO_5rOG-1iHbXUXJvJgbMrIVFi4o6K2uExaU-quP9Dhj8z5E4T5bLhOaC-UfkPdriINML5ZQldERE6KkGqjl3A1-eqqIrcqJmCxujcgbe6loYARcfVDZWZVLggYf9-f7LUz3gdGa5IxQ)

-   **Fichero** esta primera sección contiene un parámetro de tipo entrada para que el usuario pueda introducir el nombre del fichero del 349 como parámetro de entrada a la hora de generar el fichero.
-   **Identificación y Totales** esta segunda sección tiene:
    -   **4 parámetros de tipo “entrada”** que se mostrarán en el momento de generar el 349 con el fin de que el usuario los introduzca manualmente:
        -   Persona de contacto: Apellidos y nombre de la persona de contacto. Este parámetro de tipo entrada podría ser modificado a tipo constante y, por tanto, se debería especificar el valor de dicha constante que en este caso sería el nombre de la persona de contacto, para los escenarios en que la misma persona presenta la declaración. De ser así, este parámetro no tendría que informarse cada vez que se genera la declaración.
        -   Teléfono de contacto: Número de teléfono de la persona de contacto. Este parámetro de tipo entrada podría ser modificado a tipo constante y, por tanto, se debería especificar el valor de dicha constante que en este caso sería el teléfono de la persona de contacto, para los escenarios en que la misma persona presenta la declaración. De ser así, este parámetro no tendría que informarse cada vez que se genera la declaración.
        -   Declaración sustitutiva (si/no)
        -   Identificador declaración anterior: Número de la declaración a sustituir.
    -   **3 parámetros de tipo “salida”** que el sistema recogerá de la base de datos:
        -   Año
        -   Nombre de la organización
        -   NIF/CIF de la organización
-   **Operaciones** esta tercera sección tiene 2 parámetros de tipo “salida” que asociados a los tipos impositivos correspondientes incluirán las operaciones en el 349:
    -   Entregas intracomunitarias de bienes – Clave tributaria E
    -   Adquisiciones intracomunitarias de bienes – Clave tributaria A
-   **Constantes** esta cuarta sección tiene 11 parámetros de tipo “constante”:
    -   Constante en caso de informe anual (0A)
    -   Constante para el primer trimestre (1T)
    -   Constante para el segundo trimestre (2T)
    -   Constante para el tercer trimestre (3T)
    -   Constante para el cuarto trimestre (4T)
    -   Número de declaración del 349 (349 se reemplaza al remitir el fichero)
    -   Tipo de declaración (349)
    -   Línea tipo 1 (1)
    -   Línea tipo 2 operaciones (2)
    -   Línea tipo 2 correcciones (2)
    -   Presentación (T)

### **Configuración de impuestos**

Este nuevo módulo de generación del modelo 349 se basa en el módulo de impuestos para España y en uno específico para el 349.

El usuario puede comprobar en la ruta de aplicación: Gestión Financiera / Contabilidad / Configuración / Rango impuesto - pestaña Parámetro de Impuesto que los “tipos impositivos/impuestos” que deben incluirse en el 349 se han asociado al correspondiente parámetro de impuesto del 349:

-   Los tipos de IVA de adquisiciones intracomunitarias se han asociado con el parámetro “Adquisiciones intracomunitarias de bienes” que se corresponde con la clave de operación del 349: “A”

![](https://lh6.googleusercontent.com/KfmRrt9yoEP7_JdY9pGj74eYjDSqeyfBKSdPOhVonW4dkyhp_ooo6fq_VvIR-JcZsvSLAqbAMCowQduY6t-bMNJ_XJCHhqpkFCqo9Fkddj0GPykc5YhEp8TZKoOmZTXyWLYNY2PgG-JTVAdV2I6h_gZLLB-n48YQGkJdC5M8_iKRF7lv0W6I93sY6w)

-   Los tipos de IVA de entregas intracomunitarias se han asociado con el parámetro “Entregas intracomunitarias de bienes” que se corresponde con la clave de operación del 349: “E”

![](https://lh5.googleusercontent.com/M9IdlZd-5bo-JKwXpqzeEiWsaa3ONYSfKXANXvyS8TFgbYrOUVg4LjLNidbkGB9lpDkSyNFJQeaV3JpBU_U6IFw2deN8Hi7v5zQhzvAuZNHfE4C2cXoxZu6orkao7wqoXLbdfN40AkRo2obRJexQcI_PQAlOY85AwyUL_-pfUnFrUBHBkhkiMN8Odg)

## **Generación del modelo 349**

El modelo 349 se genera desde la ruta de aplicación: Gestión Financiera / Contabilidad / Herramientas de análisis / Generador de declaraciones de impuestos. El usuario puede generar el modelo 349 para cualquier mes natural, trimestre natural o bien para el año que desea, tal y como se muestra en las pantallas siguientes:

![](https://lh5.googleusercontent.com/ajXlOv6TaSCfuNPH4ti4kb0oWm2V4BommSomzro0ZtwUi9P_MqK2QydL8RjnbP9dZ0jdU_iXnYr958xhg5mmGYK1msnKIQqnGKVrNVT6EqQYsqK4hGfKR7VV21YB2EvluSKzXnC4AWnPo2ZLENR5mSWIlsKMKbGdPJ2kZn8VilJkc7KVL20L9bW8pg)

![](https://lh6.googleusercontent.com/bexJeVp33GqVPTWs2j-Z5_3gP2ywX0ej3VPCpQBrbBBkogNFQZ02p_hkUr2y9GipS0Z8uZ8zIj_zFIli04pNqqzK4FGSbPFiFgPlYShPVMCcvSuBIGxAZhBT2gbMtxm2nV_omJ3BguAthe6i320j95im5TmxSCsnmech5ZFWUyUhhks4MFsTvxIVqw)

![](https://lh5.googleusercontent.com/lj6JxfJvSCO3n4p3kIK_SIXgIbUVY0Oqt4iJJMZPJGYy-JhM3rp6C96LMeAGmK5p33pacEBtCOb0Llmm1G4IoWG6KiEpvPY_IQjyDXZ2lf5uqZBt2_geN7M-aG-97lFUFC16BLcCK6XAB5hC-e18eBunH1RQfRX2_tOwNBJEFVgVwOkf5POwOFWRuw)

En la ventana de generación de informes, el usuario deberá introducir los siguientes datos para generar el modelo 349:

**Organización** para la cual quiere generar el Modelo 349. El sistema mostrará el calendario asociado a la organización en un campo no editable.

**Esquema contable**

**Declaración de impuestos**. El usuario debería seleccionar aquí el modelo 349 mensual, trimestral o anual.

**Ejercicio**. El usuario puede seleccionar el año para el cual quiere obtener el 349.

**Periodo**. Si el usuario ha seleccionado el modelo 349 mensual, podrá seleccionar aquí el período (por ejemplo, enero 22), si ha seleccionado el modelo 349 trimestral, podrá seleccionar aquí el período (por ejemplo, enero 22 – marzo 22) y si ha seleccionado el modelo 349 anual, este campo mostrará, como valor por defecto, “Anual”.

Una vez introducidos los datos anteriores, el usuario puede introducir los parámetros de entrada del 349 en el botón de proceso “Parámetros de entrada”

![](https://lh3.googleusercontent.com/5i9PO0yuY0M54bcqQ5wMi6y9VjSP18KJBqhgyUFL5pfn5NST30ZaM-zOyqWJZ4KfkX_0m7B_jNUUfhUKNDOI5iNYxD6xlx0b54ajbT0_26cnQGYRKIBLdzoDcCEiYz-08U-TOsJ9Q8vKm_XeSi7AChRNm-sSwhL8zmq99ULTHXlMTXTTXGuM1kZP)

y una vez introducidos los parámetros de entrada, el usuario puede generar el 349 a través del botón de proceso “Generar fichero”.

### Navarra y Guipúzcoa

Se incluyen 2 nuevos check que permiten generar el fichero con la parametrización correcta para poder realizar su presentación en Hacienda Navarra y Hacienda Guipúzcoa:

![](https://lh6.googleusercontent.com/yM3HJ5ASqiH4Qs-ZgFfKANQSIVTin-DqGq0zKSmvduihJS7WOddNRd448Wv5eni03bNiwWYjVCVtZU47t4sUIyIfF18hUY-JL-oA2B_0374_CXHpXvsPICoc0TtxcvEnrrJ_ZK6ezf1gUzdsvhxXdr8)

Anteriormente, el fichero generado del modelo 349 sólo se podía presentar en AEAT. Con esta mejora, se permite la presentación tanto en Navarra como en Guipúzcoa en función del check que marquemos (si no se marca ninguno, el fichero se genera con la parametrización para la AEAT).

## **Casos de usuario**

### **Generación del modelo 349 como un fichero de texto válido**

Esta funcionalidad permitirá a las empresas españolas generar el modelo 349 como un fichero de texto conforme a los requisitos establecidos por la normativa española, para un periodo determinado.

Durante el año/trimestre/mes natural, el usuario registrará en Etendo las transacciones de compra y/o devolución con sus proveedores de la Unión Europea así como las transacciones de venta y/o devoluciones de ventas con sus clientes de la unión europea.

Las transacciones de compra y venta, se deberán introducir en el sistema normalmente a través de los tipos de documento de compra (albarán de compra y factura de compra =AP invoice) y de venta (albarán de venta y factura de venta =AR invoice), respectivamente.

Las transacciones de devolución, tanto de compra como de venta, se deberán introducir en el sistema normalmente a través de los tipos de documento de compra (albarán de compra y abono de compra =AP invoice Negativa) y de venta (albarán de venta y abono de venta=AR invoice Negativa).

Además, deberá asegurarse de que todos los productos tienen la parametrización adecuada en relación con las categorías de impuestos que tienen asociadas (21%-10%-4%).

Una vez que todas las operaciones se han registrado en el sistema, el usuario podrá generar el fichero del modelo 349 tal y como se explicó en la sección de este documento “Generación del Modelo 349”. El fichero txt del 349 tiene la siguiente estructura:

![349 4T.png](https://lh5.googleusercontent.com/4_Ps-YvMKdQKgeHJ_8HkhOwYAerhc8oX6OB58UG1NX5nSoSPBvgsR6vpY2MjmJk1pOhsFk4SmLv_ETEI4Fm4ZBDkWuxdFH4ZcDSJ83NIb3m9QNrqqWssPrfkpRjovNPC2MpEfj9CTun2h_BQgo0TNyAt5gyqhJFR6Qr5dt5T91F5tH-HCYkaJABLfw)

### **Tipo registro 1 – Registro de declarante:**

|     |     |
| --- | --- |
| **Posiciones** | **Descripción** |
| **1** | Tipo de Registro (constante = 1) |
| **2-4** | Modelo Declaración (constante = 349) |
| **5-8** | Ejercicio |
| **9-17** | NIF del declarante |
| **18-57** | Apellidos y nombre o razón social del declarante |
| **58** | Blanco |
| **59-107** | Persona con quién relacionarse: Teléfono / Apellidos y nombre |
| **108-120** | Número identificativo de la declaración |
| **121-122** | Declaración complementaria o substitutiva |
| **123-135** | Número identificativo de la declaración anterior |
| **136-137** | Periodo (predeterminado = 1T,2T,3T,4T,0A,01,02,03,04,05,06,07,08,09,10,11,12) |
| **138-146** | Número total de operadores intracomunitarios |
| **147-161** | Importe de las operaciones intracomunitarias |
| **162-170** | Número total de operadores intracomunitarios con rectificaciones |
| **171-185** | Importe de las rectificaciones |
| **186** | Indicador cambio periodicidad en la obligación de declarar |
| **187- 390** | Blancos |
| **391 - 399** | NIF del representante legal |
| **400 - 500** | Blancos |

### **Tipo de Registro 2 – Registro de operador intracomunitario**

|     |     |
| --- | --- |
| **Posiciones** | **Descripción** |
| **1** | Tipo de Registro (constante = 2) |
| **2-4** | Modelo Declaración (constante = 349) |
| **5-8** | Ejercicio |
| **9-17** | NIF del declarante |
| **18-75** | Blancos |
| **76-92** | NIF del operador comunitario |
| **93-132** | Apellidos y nombre o razón social del operador intracomunitario |
| **133** | Clave de operación (E, M, H, A, T, S, I, R, D o C) |
| **134-146** | Base Imponible o Importe |
| **147-178** | Blancos |
| **179- 195** | NIF Empresario o Profesional Destinatario final sustituto |
| **196- 235** | Apellidos y Nombre o Razón social del sujeto pasivo sustituto |
| **236- 500** | Blancos |

### **Tipo de Registro 2 – Registro de rectificaciones**

|     |     |
| --- | --- |
| **Posiciones** | **Descripción** |
| **1** | Tipo de Registro (constante = 2) |
| **2-4** | Modelo Declaración (constante = 349) |
| **5-8** | Ejercicio |
| **9-17** | NIF del declarante |
| **18-75** | Blancos |
| **76-92** | NIF del operador comunitario |
| **93-132** | Apellidos y nombre o razón social del operador intracomunitario |
| **133** | Clave de operación (E, M, H, A, T, S, I, R, D o C) |
| **134-146** | Blancos |
| **147-178** | Rectificaciones   <br>  <br>\- 147-150 ejercicio (de la declaración que se corrige)   <br>\- 151-152 periodo (de la declaración que se corrige)   <br>\- 153-165 base imponible (para el tercero y el periodo) rectificada   <br>\- 166-178 base imponible (para el tercero y el periodo) declarada anteriormente |
| **179- 195** | NIF Empresario o Profesional Destinatario final sustituto |
| **196- 235** | Apellidos y Nombre o Razón social del sujeto pasivo sustituto |
| **236- 500** | Blancos |

### **Operaciones rectificativas del 349**

En el modelo/fichero del 349 hay que diferenciar de forma específica en el registro tipo 2 de "Rectificaciones aquellas notas de abono a facturas que ya fueron incluidas en una declaración 349 para un periodo anterior al corriente, por ejemplo:

-   **Declaración 349 Mensual** = Una nota de abono de fecha agosto del 2022 que abona una factura de fecha julio del 2022 que ya fue incluída en la declaración del 349 del mes de julio del 2022. La nota de abono de fecha agosto debe incluirse en la declaración del mes de agosto como rectificativa a la declaración del mes de julio para el proveedor/cliente que aplique, indicando además el importe total (base imponible) de compra/venta que se incluyó en la declaración de julio para ese cliente/proveedor.
-   **Declaración 349 Trimestral** = Lo mismo aplica en el caso de presentación de la declaración del 349 de forma trimestral, lo único que varía en este escenario es que en vez de tener en cuenta meses se tendrán en cuenta trimestres.
-   **Declaración 349 Anual** = Lo mismo aplica en el caso de presentación de la declaración del 349 de forma anual, lo único que varía en este escenario es que en vez de tener en cuenta meses/trimestres se tendrán en cuenta el año natural.

Y las que no y deben acumularse para el periodo, por ejemplo:

-   **Declaración 349 Mensual** = Una nota de abono de fecha de agosto 2022 que abona una factura de fecha de agosto 2022 que todavía no ha sido incluida en la Declaración del 349 para el mes de agosto del 2022, se incluirá en la declaración de agosto como un menor valor del importe de compra/venta con el correspondiente proveedor/cliente.
-   **Declaración 349 Trimestral o Anual** = Lo mismo aplica en el caso de presentación de la declaración del 349 de forma trimestral o Anual, lo único que varía en este escenario es que en vez de tener en cuenta meses se tendrán en cuenta trimestres o el año natural.

Es por ello que se ha introducido en el sistema una funcionalidad que permite al usuario, a la hora de crear una nota de abono o devolución, indicar si dicha nota de abono/devolución es una “rectificativa del 349” o no, es decir, si rectifica a una factura (factura rectificada) de un año/mes/trimestre natural anterior y que, por tanto, ya se incluyó en una declaración del 349 anterior.

Para introducir esta información, el usuario deberá navegar a Gestión de compras o Ventas / Transacciones / Factura (Proveedor) o Factura (Cliente), crear una nueva factura como:

-   una AP/AR invoice negativa (devolución de mercancía al proveedor/cliente)
-   una AP/AR credit Memo
-   una Reversed Purchase/Sales Invoice
-   o incluso la anulación total de una factura de compra/venta;

e introducir los datos relativos al abono y devolución de mercancía y, en la pestaña “Factura Rectificativa”, crear un nuevo registro con el fin de:

-   seleccionar la factura (original) que esta abonándose o rectificándose - esa selección ya vendŕa dada en caso de anulación total de una factura.
-   y además seleccionar el nuevo campo “Rectificativa del 349”, con el fin de indicar además:
    -   el Año de la factura original que se rectifica
    -   el Periodo de la factura original y, por tanto, el periodo en el cual dicha factura original se incluyó en un 349
    -   La base imponible del 349 de productos o, lo que es lo mismo, El importe total de compra/venta (que para operaciones intracomunitarias coincide con la Base Imponible total) que para dicho periodo y para dicho proveedor/cliente se informó en el 349 anterior con respecto a la compra/venta de productos (Clave A en compras, Clave E en ventas)
    -   y la base imponible del 349 servicios o, lo que es lo mismo, El importe total de compra/venta (que para operaciones intracomunitarias coincide con la Base Imponible total) que para dicho periodo y para dicho proveedor/cliente se informó en el 349 anterior con respecto a la compra/venta de servicios Clave I en compras, Clave S en ventas)

![](https://lh3.googleusercontent.com/vi_SXEIsX7fl_bwkI5sm1XIKSMs7Ts0Z2mbdjIKBZTPCCmetky4ch7u-EhHzPh2ZgHf5UNYO9M36vkH2CG_lLB6hYJ8KhiF1pNVahoUxgovjB1mVJbFKtbr01lqAvGkctdWmJ7skW2umwSjvRobDk0_lAQtQkW7-W-FwN8EBjlO5eK_m3H2iyZG1Qw)

Tal y como se muestra en la pantalla anterior, esta funcionalidad requiere mostrar en Etendo las columnas que se detallan a continuación:

-   Correctiva del 349
-   Año
-   Periodo
-   Base Imponible del 349 Productos
-   Business Partner
-   Base Imponible del 349 Servicios

!!! info
    No todas las notas de abono o devoluciones de mercancía serán rectificativas del 349, sólo aquellas que así se configuren por el usuario. 

En caso de que la nota de abono o devolución de mercancía y la factura original pertenezcan al mismo periodo, por ejemplo al 1er mes del año 2022 (Enero 2022, en caso de declaración del 349 mensual), al 1er periodo del año 2022 (Enero 2022 a Marzo 2022, en caso de declaración del 349 trimestral) o al mismo mes (Enero 2022, en el caso de declaración del 349 mensual), tan sólo será necesario relacionar ambos documentos en la nueva pestaña “Factura Rectificativa” sin tener que seleccionar el parámetro “Rectificativa del 349”.

En este último escenario, el sistema, para un mismo proveedor o cliente y periodo, acumulará las facturas positivas y los abonos con el fin de generar el computo global del importe de las transacciones de compra/venta efectuadas con dicho proveedor/cliente (operador intracomunitario) que debe incluirse en la declaración del 349 para un periodo determinado.

### **Presentación del modelo 349 en formato electrónico**

La presentación telemática del modelo 349 en formato electrónico requiere que las empresas tenga un NIF español así como un Certificado electrónico emitido por la “Fábrica Nacional de Moneda y Timbre” (FNMT) u otro Certificado válido y reconocido por Hacienda.

La presentación telemática puede realizarse a través de la página web de la Hacienda Pública española, desde el enlace “Oficina virtual”-”Presentación de declaraciones” - “Todas las declaraciones” - “Modelo 349”\]

!!! info
    Existe una “Guía de presentación telemática” en la página web de Hacienda que nos explica cómo debe realizarse la presentación telemática de las declaraciones y que se puede descargar [*aquí*](https://sede.agenciatributaria.gob.es/static_files/Sede/Procedimiento_ayuda/GI28/instr_mod_349.pdf).


### **Presentación de declaraciones sustitutivas**

Es necesario presentar una declaración sustitutiva cuando dicha declaración tenga por objeto anular y sustituir completamente a otra declaración anterior para el mismo periodo ya enviada a Hacienda, en la cual se hubieran incluido datos inexactos o erróneos.

Para ello el usuario deberá realizar en la aplicación los cambios en los datos/transacciones pertinentes y volver a generar una nueva declaración 349 como fichero indicando en este caso que la nueva declaración que se presenta es sustitutiva de una anterior, e indicando además el número de la declaración original a la que sustituye, tal y como se muestra en la siguiente pantalla:

![](https://lh6.googleusercontent.com/iSU9FGfN3pSTIsHPTAKpZsKZsCB7C0BhZa1RBDpzcJQ8uaOHAUmMPFuYQkhQbrQ2izd9kDfZ0TCiEHdGvHIE7iHOc-uDNoBEhDS5cF9x__Bf2rQgvz47h3U88ViVeZimkAUXctFTFhF9gZYbywo3Nb23iqRQ0Tfq03VSTqcEOcsQQnYJVi6MGxDajA)