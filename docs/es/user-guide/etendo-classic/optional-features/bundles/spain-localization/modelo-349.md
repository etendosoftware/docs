---
title: Modelo 349
tags:
    - Modelo 349
    - Localizacion Española
    - Gestión Financiera
    - Contabilidad
    - Herramientas de análisis
---

# Modelo 349

:octicons-package-16: Javapackage: `org.openbravo.module.aeat349.es`

Esta sección describe el módulo **Modelo AEAT 349 - Declaración recapitulativa de operaciones intracomunitarias**, incluido en la Localización Española de Etendo.

## Descripción del módulo

El módulo de generación del Modelo 349 genera un fichero `*.txt` válido conforme a los requisitos establecidos por la Hacienda Española.

Esto permite a las empresas españolas cumplir con sus obligaciones fiscales relacionadas con la declaración recapitulativa de las entregas y adquisiciones intracomunitarias de bienes.

La funcionalidad sigue la Orden HAC/360/2002, modificada por última vez por la Orden HAC/174/2020.

De acuerdo con el reglamento del IVA, deben presentar el modelo 349 los sujetos pasivos del impuesto que realicen cualquiera de las siguientes operaciones:

-   Las entregas de bienes destinados a otro Estado miembro, entregas de bienes exentas del impuesto.
-   Las adquisiciones intracomunitarias de bienes sujetas al impuesto.
-   Las adquisiciones intracomunitarias de bienes y entregas subsiguientes exentas conocidas como Operaciones Triangulares.

La declaración recapitulativa de operaciones intracomunitarias incluye:

-   Las operaciones citadas en el apartado anterior, así como las rectificaciones de operaciones ya incluidas en la correspondiente declaración recapitulativa.
-   Los datos de identificación de los proveedores y adquirientes.
-   La base imponible en euros de las operaciones intracomunitarias de bienes declaradas.

En general, la declaración recapitulativa debe presentarse por cada mes natural dentro de los veinte primeros días naturales del mes siguiente.

Hay dos excepciones:

- La correspondiente al mes de julio puede presentarse durante el mes de agosto y los veinte primeros días naturales de septiembre.
- La correspondiente al último período del año debe presentarse durante los treinta primeros días naturales de enero.

Si el importe total de las operaciones intracomunitarias no supera los 50.000 € (sin IVA) en el trimestre en curso ni en los cuatro trimestres anteriores, la declaración puede presentarse de forma trimestral, dentro de los veinte primeros días naturales del mes siguiente al trimestre. Si al final de cualquiera de los meses que componen un trimestre natural se supera ese importe, debe presentarse una declaración recapitulativa para el mes o meses transcurridos desde el inicio del trimestre, dentro de los veinte primeros días naturales siguientes.

!!! info
    Desde 2020 se suprime el período anual de declaración.

Las operaciones se entenderán realizadas el día en que se expida la factura o documento equivalente que sirva de justificante de las mismas.

El modelo 349 diferencia las notas de abono que rectifican facturas ya incluidas en declaraciones anteriores de las que no lo hacen. Para cubrir ese caso, el sistema incorpora una funcionalidad que relaciona las notas de abono con las facturas que están siendo abonadas o rectificadas, como se explica en la sección [Operaciones rectificativas del 349](#operaciones-rectificativas-del-349).

!!! info
    El módulo no incluye las operaciones triangulares porque Etendo no registra este tipo de operaciones. Si su empresa realiza operaciones triangulares, deberá declararlas manualmente a través de la sede electrónica de la AEAT.

Este módulo no tiene en cuenta las transacciones correspondientes al tipo de documento de Etendo `AP/AR Credit Memo` (notas de crédito) como facturas de abono, ya que ese tipo de transacción no refleja devoluciones de mercancía.

Por ello, el módulo 349 sí tiene en cuenta:

- los tipos de documento `AP/AR invoice`, como facturas de compra y venta
- los tipos de documento `AP/AR invoice` negativos, como notas de abono o facturas rectificativas

Además, el módulo no contempla el supuesto de **Declaración Complementaria** para los casos en que deban incluirse solo operaciones que, aun debiendo haberse declarado en otra declaración del mismo ejercicio ya presentada, no se incluyeron.

Estas operaciones deben incorporarse manualmente a través de la página de la AEAT, tal y como se explica en la sección [Declaración Complementaria](#declaracion-complementaria).

## Instalación del módulo

Para la instalación del módulo **Modelo AEAT 349 - Declaración recapitulativa de operaciones intracomunitarias**, el usuario debe seguir los pasos que se describen a continuación en función de la situación de partida:

-   Instalación de la última versión disponible de Etendo
-   o la instalación del [módulo de Localización Española](overview.md).

!!! info
    Para la instalación del módulo de Localización Española, visite [*Marketplace*](https://marketplace.etendo.cloud/#/product-details?module=003B475055DD421B9483B5BE15AA48C5){target="_blank"}. 

Es importante recalcar que el módulo del Modelo AEAT 349 incluye el correspondiente conjunto de datos que relaciona los tipos/rangos de impuestos con los parámetros del 349.

### Requisitos previos

Antes de aplicar el módulo del 349, deben estar instalados y aplicados a la organización los siguientes módulos:

-   [Módulo de impuestos para España](impuestos-para-españa.md) — necesario para todos los modelos de declaración de impuestos de la Localización Española.
-   **Modelo AEAT 349 - Declaración recapitulativa de operaciones intracomunitarias** — incluido en el Bundle de Localización Española.

### Aplicación del módulo

Una vez instalado el módulo del 349, es necesario cargar su configuración inicial — denominada "conjunto de datos" o dataset — en la organización de su empresa que gestiona la contabilidad y tiene obligaciones fiscales en España.

Para aplicar el módulo, siga estos pasos:

1. Navegar a `Configuración General` > `Organización` > `Gestión del módulo de Empresa`.
2. Seleccionar la **Organización** legal con contabilidad correspondiente. (Es la organización que representa a la entidad legal con obligaciones fiscales en España y que tiene configurada una contabilidad activa. Si no está seguro, consulte con el administrador del sistema.)
3. En la solapa **Dataset**, marcar primero el dataset del módulo de impuestos para España (si no está aplicado previamente) y después el dataset del módulo del **Modelo AEAT 349**, y hacer clic en **Aplicar**.

![Gestión del módulo de Empresa](../../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/modelo-349/gestion-modulo-empresa.png)

!!! note
    Un "conjunto de datos" contiene los valores de configuración que el módulo necesita para funcionar correctamente. Solo es necesario aplicarlo una vez por organización.

!!! note
    El dataset del módulo solo aparece disponible en esta ventana una vez que el módulo está instalado.

## Configuración del módulo

### Configuración del modelo 349

Una vez aplicado el conjunto de datos, la configuración del Modelo 349 se crea automáticamente. Solo necesitará revisar o modificar los parámetros de **Entrada** si desea personalizar datos fijos como el nombre o el teléfono de contacto de la declaración.

Puede verificar la configuración en `Gestión Financiera` > `Contabilidad` > `Configuración` > `Declaración de Impuestos`.

![Declaración de Impuestos - Modelo 349](../../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/modelo-349/declaracion-de-impuestos-349.png)

??? info "Detalle de parámetros (avanzado)"

    Esta sección es para administradores del sistema. Los usuarios de contabilidad o compras no necesitan modificar estos parámetros.

    En la solapa **Sección de declaración** se han creado 4 secciones:

    ![Secciones de la declaración 349](../../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/modelo-349/secciones-declaracion.png)

    -   **Fichero**. Esta sección contiene un parámetro de tipo entrada para introducir el nombre del fichero del 349 al generar el fichero.
    -   **Identificación y Totales**. Esta sección tiene:
        -   **4 parámetros de tipo entrada** que se mostrarán en el momento de generar el 349 con el fin de que el usuario los introduzca manualmente:
            -   Persona de contacto: Apellidos y nombre de la persona de contacto. Este parámetro de tipo entrada podría ser modificado a tipo constante y, por tanto, se debería especificar el valor de dicha constante que en este caso sería el nombre de la persona de contacto, para los escenarios en que la misma persona presenta la declaración. De ser así, este parámetro no tendría que informarse cada vez que se genera la declaración.
            -   Teléfono de contacto: Número de teléfono de la persona de contacto. Este parámetro de tipo entrada podría ser modificado a tipo constante y, por tanto, se debería especificar el valor de dicha constante que en este caso sería el teléfono de la persona de contacto, para los escenarios en que la misma persona presenta la declaración. De ser así, este parámetro no tendría que informarse cada vez que se genera la declaración.
            -   Declaración sustitutiva (si/no)
            -   Identificador declaración anterior: Número de la declaración a sustituir.
        -   **3 parámetros de tipo salida** que el sistema recogerá de la base de datos:
            -   Año
            -   Nombre de la organización
            -   NIF/CIF de la organización
    -   **Operaciones**. Esta sección tiene 2 parámetros de tipo salida que, asociados a los tipos impositivos correspondientes, incluyen las operaciones en el 349:
        -   Entregas intracomunitarias de bienes – Clave tributaria E
        -   Adquisiciones intracomunitarias de bienes – Clave tributaria A
    -   **Constantes**. Esta sección tiene 11 parámetros de tipo constante:
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

### Configuración de impuestos

La asignación de los tipos de IVA a los parámetros del Modelo 349 se realiza automáticamente al aplicar el conjunto de datos del módulo. En la mayoría de los casos no es necesario realizar ninguna acción adicional en este apartado.

??? info "Detalle de asignación de impuestos (avanzado)"

    Este módulo de generación del modelo 349 se basa en el módulo de impuestos para España y en uno específico para el 349.

    El usuario puede comprobar en la ruta de aplicación `Gestión Financiera` > `Contabilidad` > `Configuración` > `Rango impuesto`, en la solapa `Parámetro de declaración`, que los tipos impositivos que deben incluirse en el 349 se han asociado al correspondiente parámetro de impuesto del 349:

    -   Los tipos de IVA de adquisiciones intracomunitarias se han asociado con el parámetro **Adquisiciones intracomunitarias de bienes**, que se corresponde con la clave de operación del 349: `A`.

    ![Rango impuesto - Adquisiciones intracomunitarias](../../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/modelo-349/rango-impuesto-adquisiciones-intracomunitarias.png)

    -   Los tipos de IVA de entregas intracomunitarias se han asociado con el parámetro **Entregas intracomunitarias de bienes**, que se corresponde con la clave de operación del 349: `E`.

    ![Rango impuesto - Entregas intracomunitarias](../../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/modelo-349/rango-impuesto-entregas-intracomunitarias.png)

## Generación del modelo 349

El modelo 349 se genera desde la ruta de aplicación `Gestión Financiera` > `Contabilidad` > `Herramientas de análisis` > `Generador de declaraciones de impuestos`. El usuario puede generar el modelo 349 para cualquier mes natural, trimestre natural o para el año deseado, tal y como se muestra en las pantallas siguientes:

![Generador de declaraciones de impuestos - selección](../../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/modelo-349/generador-declaraciones-1.png)

![Generador de declaraciones de impuestos - periodo](../../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/modelo-349/generador-declaraciones-2.png)

![Generador de declaraciones de impuestos - resultado](../../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/modelo-349/generador-declaraciones-3.png)

En la ventana de generación de informes, el usuario debe introducir los siguientes datos para generar el modelo 349:

-   **Organización**. Organización para la cual se genera el Modelo 349. El sistema muestra el calendario asociado en un campo no editable.
-   **Esquema contable.** Seleccione el plan de cuentas que utiliza su organización. Si no sabe cuál elegir, consulte con el administrador del sistema — normalmente ya estará preconfigurado.
-   **Declaración de impuestos**. Aquí se selecciona el modelo 349 mensual, trimestral o anual.
-   **Ejercicio**. Año para el cual se obtiene el 349.
-   **Periodo**. Si el usuario selecciona el modelo 349 mensual, puede elegir un período mensual (por ejemplo, enero del ejercicio). Si selecciona el modelo 349 trimestral, puede elegir un período trimestral (por ejemplo, enero – marzo del ejercicio). Si selecciona el modelo 349 anual, este campo muestra por defecto `Anual`.

Una vez introducidos los datos anteriores, el usuario puede completar los parámetros de entrada del 349 desde el botón de proceso **Parámetros de entrada**.

![Parámetros de entrada - Modelo 349](../../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/modelo-349/parametros-entrada-349.png)

Una vez introducidos esos parámetros, el usuario puede generar el 349 desde el botón de proceso **Generar fichero**.

### Navarra y Guipúzcoa (opcional)

Navarra y el País Vasco (incluida Guipúzcoa) son territorios forales con administración tributaria propia. Las empresas domiciliadas en estos territorios deben presentar el Modelo 349 ante su Hacienda foral, no ante la AEAT, y el fichero requiere una parametrización específica.

Se incluyen dos checks que permiten generar el fichero con la parametrización correcta para su presentación en **Hacienda Navarra** y **Hacienda Guipúzcoa**:

!!! note
    Si no se marca ningún check, el fichero se genera con la parametrización estándar de la AEAT.

![Checks Navarra y Guipúzcoa](../../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/modelo-349/navarra-guipuzcoa-checks.png)

Anteriormente, el fichero generado del modelo 349 solo se podía presentar en la AEAT. Con esta mejora, el usuario puede presentarlo también en Navarra o en Guipúzcoa, según el check seleccionado.

### Edición de Número de Justificante (opcional)

Si la declaración se presentará a la AEAT utilizando la opción **Ejercicio 202X. Presentación mediante fichero**, deberá editar el fichero `.txt` generado antes de enviarlo. Para ello:

1. Abra el fichero con un editor de texto (por ejemplo, el Bloc de notas en Windows).
2. Localice la primera línea del fichero — es el registro del declarante.
!!! tip "Consejo práctico"
    Si usa un editor con indicador de columna (como Notepad++ o Visual Studio Code), posicione el cursor al inicio de la primera línea y desplácese hasta la columna 108. Si usa el Bloc de notas estándar de Windows, cuente los caracteres manualmente desde el inicio de la línea.

3. En esa primera línea, entre los caracteres 108 y 120, encontrará el número de justificante. Este número no puede ser el código de modelo (182) seguido de ceros (por ejemplo, `1820000000000` no es válido).
4. Sustitúyalo por un número válido, como `1820000000001`, o bien 182 seguido del año y un correlativo, por ejemplo `182AAAA000001` donde AAAA es el año del ejercicio declarado.

Si presenta la declaración utilizando la opción **Ejercicio 202X. Presentación (hasta 40.000 registros)**, no es necesario realizar este cambio.

### Generación del modelo 349 como un fichero de texto válido

Esta funcionalidad permite a las empresas españolas generar el modelo 349 como un fichero de texto conforme a los requisitos establecidos por la normativa española, para un periodo determinado.

Durante el año/trimestre/mes natural, el usuario registrará en Etendo las transacciones de compra y/o devolución con sus proveedores de la Unión Europea así como las transacciones de venta y/o devoluciones de ventas con sus clientes de la unión europea.

Las transacciones de compra y venta se deberán introducir en el sistema normalmente a través de los tipos de documento de compra (albarán de compra y **Factura (Proveedor)**) y de venta (albarán de venta y **Factura (Cliente)**), respectivamente.

Las transacciones de devolución, tanto de compra como de venta, se deberán introducir en el sistema normalmente a través de los tipos de documento de compra (albarán de compra y **Factura (Proveedor)** negativa) y de venta (albarán de venta y **Factura (Cliente)** negativa).

Además, deberá asegurarse de que todos los productos tienen la parametrización adecuada en relación con las categorías de impuestos que tienen asociadas (21%-10%-4%).

Una vez que todas las operaciones se han registrado en el sistema, el usuario puede generar el fichero del modelo 349 tal y como se explicó en la sección de este documento [Generación del Modelo 349](#generacion-del-modelo-349). El fichero `txt` del 349 tiene la siguiente estructura:

![Estructura del fichero 349](../../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/modelo-349/estructura-fichero-349.png)

??? info "Estructura técnica del fichero (solo para edición manual)"
    Solo necesita consultar estas tablas si va a editar el fichero manualmente, como se describe en la sección [Edición de Número de Justificante](#edicion-de-numero-de-justificante-opcional).

    ### Tipo de registro 1 – Registro de declarante

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

    ### Tipo de registro 2 – Registro de operador intracomunitario

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

    ### Tipo de registro 2 – Registro de rectificaciones

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

## Operaciones rectificativas del 349

En el modelo 349, el registro de tipo 2 de rectificaciones distingue dos casos:

-   Notas de abono que rectifican una factura ya incluida en una declaración 349 de un periodo anterior.
-   Notas de abono que no rectifican una declaración anterior y que, por tanto, se acumulan en el periodo actual.

### Cuándo una nota de abono es rectificativa

Una nota de abono es rectificativa cuando corrige una factura incluida en una declaración 349 ya presentada.

Ejemplo mensual:

-   Una nota de abono del mes siguiente rectifica una factura del mes anterior ya incluida en la declaración de ese mes.
-   En este caso, la nota de abono se incluye en la declaración del mes en curso como rectificativa de la declaración del mes anterior.
-   Además, se informa el importe total o base imponible de compra o venta que se declaró en ese mes anterior para ese proveedor o cliente.

La misma lógica aplica a las declaraciones trimestrales y anuales. Solo cambia el periodo de referencia.

### Cuándo una nota de abono no es rectificativa

Una nota de abono no es rectificativa cuando corrige una factura del mismo periodo que todavía no se ha incluido en una declaración 349 presentada.

Ejemplo mensual:

-   Una nota de abono rectifica una factura del mismo mes.
-   Como la factura todavía no se ha incluido en una declaración previa, la nota de abono se acumula en la declaración del mes en curso como un menor importe de compra o venta para ese proveedor o cliente.

La misma lógica aplica a las declaraciones trimestrales y anuales.

### Cómo informar una operación rectificativa

Para cubrir este caso, el sistema incorpora una funcionalidad que permite indicar si una nota de abono o devolución es una `rectificativa del 349`.

Para introducir esta información, el usuario debe navegar a `Gestión de Compras` o `Gestión de Ventas` > `Transacciones` > `Factura (Proveedor)` o `Factura (Cliente)`.

Allí debe crear una nueva factura utilizando una de las siguientes opciones:

-   **Abono de compra o venta** (en el sistema: `AP/AR Invoice` con importe negativo)
-   **Nota de crédito** (en el sistema: `AP/AR Credit Memo`)
-   **Factura revertida** (en el sistema: `Reversed Purchase/Sales Invoice`)
-   **Anulación total** de una factura de compra o venta

Después, en la solapa `Factura Rectificativa`, debe crear un nuevo registro para:

-   seleccionar la factura original que se abona o rectifica
-   marcar el campo `Rectificativa del 349`, cuando corresponda
-   completar estos datos:
    -   Año de la factura original que se rectifica
    -   Periodo de la factura original y periodo en el que se incluyó en un 349 anterior
    -   Base imponible del 349 de productos, es decir, el importe total de compra o venta informado previamente para ese proveedor o cliente en productos
    -   Base imponible del 349 de servicios, es decir, el importe total de compra o venta informado previamente para ese proveedor o cliente en servicios

Si la nota de abono o devolución y la factura original pertenecen al mismo periodo, basta con relacionar ambos documentos en la solapa `Factura Rectificativa`.

En ese caso, no es necesario marcar el parámetro `Rectificativa del 349`.

En este escenario, el sistema acumula las facturas positivas y los abonos del mismo proveedor o cliente para el mismo periodo. Así genera el cómputo global del importe de las transacciones de compra y venta que debe incluirse en la declaración del 349.

![Solapa Factura Rectificativa del 349](../../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/modelo-349/factura-rectificativa-349.png)

Tal y como se muestra en la pantalla anterior, esta funcionalidad requiere mostrar en Etendo las columnas que se detallan a continuación:

-   Correctiva del 349
-   Año
-   Periodo
-   Base Imponible del 349 Productos
-   Tercero (Business Partner)
-   Base Imponible del 349 Servicios

!!! info
    No todas las notas de abono o devoluciones de mercancía son rectificativas del 349, solo aquellas que así configure el usuario.

## Presentación del modelo 349 en formato electrónico

La presentación telemática del modelo 349 en formato electrónico requiere que la empresa tenga un NIF español y un certificado electrónico (documento digital que acredita la identidad de su empresa ante Hacienda) emitido por la **Fábrica Nacional de Moneda y Timbre (FNMT)** u otro certificado válido y reconocido por Hacienda. Si aún no dispone de uno, puede solicitarlo en la web de la FNMT.

La presentación telemática puede realizarse a través de la página web de la Hacienda Pública española, desde `Oficina virtual` > `Presentación de declaraciones` > `Todas las declaraciones` > `Modelo 349`.

!!! info
    Existe una **Guía de presentación telemática** en la página web de Hacienda que explica cómo debe realizarse este trámite y que se puede descargar [**aquí**](https://sede.agenciatributaria.gob.es/static_files/Sede/Procedimiento_ayuda/GI28/instr_mod_349.pdf){target="_blank"}.

## Presentación de declaraciones sustitutivas

Es necesario presentar una declaración sustitutiva cuando se debe anular y sustituir por completo una declaración anterior del mismo periodo que contiene datos inexactos o erróneos.

Para ello, el usuario debe realizar los cambios necesarios en la aplicación y volver a generar una nueva declaración 349 como fichero. En esa nueva declaración, debe indicar que se trata de una declaración sustitutiva e informar el número de la declaración original que sustituye, tal y como se muestra en la siguiente pantalla:

![Declaración sustitutiva - Modelo 349](../../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/modelo-349/declaracion-sustitutiva-349.png)

## Declaración Complementaria

El módulo no genera declaraciones complementarias de forma automática.

Debe presentar una declaración complementaria cuando operaciones que debían haberse incluido en una declaración del mismo periodo ya presentada fueron omitidas.

Para incluir esas operaciones, acceda a la página web de la AEAT y añádalas manualmente desde `Oficina virtual` > `Presentación de declaraciones` > `Todas las declaraciones` > `Modelo 349`.

!!! warning
    No realice cambios en la declaración original ya presentada. La declaración complementaria se presenta como un trámite independiente desde la sede electrónica de la AEAT.

*[AEAT]: Agencia Estatal de Administración Tributaria
*[CIF]: Código de Identificación Fiscal
*[FNMT]: Fábrica Nacional de Moneda y Timbre
*[IVA]: Impuesto sobre el Valor Añadido
*[NIF]: Número de Identificación Fiscal

---

This work is a derivative of [Openbravo Localización Española](https://wiki.openbravo.com/wiki/Openbravo_Localizaci%C3%B3n_Espa%C3%B1a){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
