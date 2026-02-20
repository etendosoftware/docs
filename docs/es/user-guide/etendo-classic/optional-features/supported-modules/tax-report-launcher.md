---
title: Lanzador de informes de impuestos
---
## Visión general
### Propósito

El objetivo de este documento es describir las especificaciones funcionales para un nuevo módulo de extensión que es el “Lanzador de informes de impuestos”.
El módulo lanzador de informes de impuestos permite a los usuarios finales crear y presentar informes de impuestos ante las autoridades fiscales según lo requerido por las autoridades fiscales del país.
Estas especificaciones funcionales se implementarán posteriormente de acuerdo con la documentación técnica. 

!!! info
    Es importante tener en cuenta que esta especificación funcional está orientada por ahora al paquete de localización profesional español, principalmente en relación con la configuración y los escenarios cubiertos, independientemente de que la funcionalidad del lanzador de informes de impuestos deba implementarse de la forma más genérica posible para cubrir escenarios de otros países.

También es un hecho que la especificación actual está principalmente relacionada con las necesidades españolas, ya que son las que se conocen actualmente; por lo tanto, la documentación actual y la implementación del lanzador de informes de impuestos se mejorarán o ajustarán más adelante si fuese necesario.

### Alcance
El lanzador de informes de impuestos es un **módulo de impuestos ampliado** que permite al usuario final:
1. configurar diferentes **“parámetros de impuestos”** así como **"parámetros de informes de impuestos"** en función del tipo de impuesto y de los requisitos del informe de impuestos, respectivamente
2. configurar diferentes **“informes de impuestos”** en una única ventana y de acuerdo con los requisitos fiscales del país
3. "lanzar" un informe de impuestos seleccionado para un periodo específico
4. y obtener la **"salida de impuestos como un archivo"** requerida para ser presentada ante las autoridades fiscales en un formato válido.

Además, el lanzador de informes de impuestos es un **framework** que permitirá al usuario final desarrollar nuevos informes de impuestos según sea necesario.
## Consideraciones de diseño
### Dependencias
Dado que probablemente se deban implementar más informes de impuestos nuevos para el mismo país u otros, e incluso los existentes podrían cambiar, el módulo lanzador de informes de impuestos debe implementarse de manera que la lógica de negocio de cada informe de impuestos quede aislada del resto, de modo que, en caso de que sea necesario modificar un informe de impuestos existente, ese cambio no afecte al resto y, en caso de que haya nuevos informes de impuestos que implementar, esos nuevos tendrán su propia lógica de negocio.

### Restricciones
Etendo ya proporciona configuración de impuestos, transacciones de impuestos y, en general, funcionalidades relacionadas con impuestos; por lo tanto, y con el fin de ser coherentes, las funcionalidades existentes relacionadas con impuestos se tienen en cuenta como parte de este nuevo módulo. Además, podría ocurrir que algunas de las funcionalidades de impuestos existentes deban mejorarse para obtener la información fiscal requerida para que este módulo de extensión funcione.

### Entrega
!!! info
    Esta funcionalidad se va a entregar como un módulo. Los datos de configuración se entregarán como un módulo adicional que podría ser importado por el usuario final, conteniendo una configuración por defecto; además, cada informe se incluirá en un módulo particular.
## Requisitos funcionales
### Roles de usuario y perfiles
Los siguientes roles están involucrados:

- Responsable de contabilidad (Mary): Mary es la responsable de contabilidad. Debe saber qué informes de impuestos deben presentarse a las autoridades fiscales en función de los requisitos de las autoridades fiscales del país, así como de las particularidades del negocio. Por lo tanto, debe asegurarse de que, una vez instalada la extensión "Datos de configuración", entregada como un módulo adicional para el Lanzador de informes de impuestos, los datos por defecto o la configuración requerida para los informes de impuestos específicos que necesita presentar a las autoridades fiscales estén correctamente configurados en el sistema. Mary lo hará en colaboración con Peter.
- Personal de contabilidad (Peter): Peter es un empleado que forma parte del personal de contabilidad. Será responsable de ayudar a Mary comprobando o configurando los parámetros necesarios, así como introduciendo las transacciones contables correspondientes en colaboración con ventas (Mike) y el personal de compras (Alice), y ejecutando los informes de impuestos y, finalmente, obteniendo la salida del informe de impuestos para presentarla a las autoridades fiscales.
### Tipo informe
El módulo Tax Report Launcher permite definir los tipos de informes de impuestos descritos a continuación:

- **informes de impuestos de extracto**, que son los informes destinados únicamente a **listar un tipo específico de transacciones de impuestos** para que las autoridades fiscales estén informadas al respecto. Por ejemplo, las autoridades fiscales necesitan ser informadas de cada transacción de venta y/o compra que supere un importe específico o de aquellas realizadas dentro de países de la UE.
- informes de impuestos, que son los informes destinados a recopilar importes de base imponible, rangos de impuesto e importes de impuesto de forma que se obtengan los importes netos de **liquidación de impuestos o recaudación de impuestos** o cualquier otro tipo de resultado fiscal.

Los informes de impuestos más comunes y relevantes que deben presentarse a las autoridades fiscales son:
- Impuesto sobre el Valor Añadido (VAT)
- e informes de impuestos de Retención  
en relación con esos impuestos, hay algunos conceptos importantes a tener en cuenta, que se enumeran a continuación:

- **Impuesto sobre el valor añadido** es un impuesto indirecto sobre el consumo y aplicable a prestaciones de servicios o entregas de bienes, importaciones de bienes y adquisiciones intracomunitarias de bienes; por lo tanto, la configuración del VAT depende del tipo de transacción y del tipo de bienes/servicios que se compren y/o vendan.
- **Retención** son importes detraídos por el retenedor (p. ej., una empresa) al contribuyente (p. ej., un empleado) por rentas pagadas (p. ej., un salario), que son abonados por el retenedor como un importe “a cuenta” del impuesto que el contribuyente debe pagar al final del ejercicio fiscal a las autoridades fiscales; por lo tanto, la configuración del impuesto de Retención depende de quién genera una renta, así como del propio tipo de renta.

En algunos países, como España, existe otro tipo de retención comúnmente conocido como Pagos a cuenta. **Pago a cuenta** es una retención. Es un importe “pagado” por las empresas a las autoridades fiscales para determinados conceptos de renta (bienes) como anticipo del importe del impuesto que debe pagar el beneficiario de esa renta; por lo tanto, la configuración del impuesto de pago a cuenta depende de quién generó una renta, así como del propio tipo de renta.
- **Tipos de renta** pueden ser “en efectivo” (monetarias/por ejemplo, un salario o un honorario pagado a un profesional) o “en especie” (no monetarias/por ejemplo, un coche de empresa o un piso de empresa)
- el término **Retención** aplica a las **rentas en efectivo**
y el término **Pago a cuenta** aplica a las **rentas en especie** en algunos países como España.
### Historias de usuario
Mary es la responsable de Contabilidad de una empresa ubicada en España y es la encargada de decidir qué informes de impuestos deben presentarse ante las autoridades fiscales. Con seguridad, los informes de **IVA** y de **Retención** deberán presentarse ante las autoridades fiscales. En función de los "tipos impositivos del país", así como de los requisitos de las autoridades fiscales nacionales y del tipo de actividad de la empresa, Mary debe saber exactamente qué informes de **IVA** y de **Retención** deben presentarse obligatoriamente ante las autoridades fiscales por su empresa.

Mary sabe que, como regla general, los informes de impuestos relacionados con el **IVA** **reconocen la obligación tributaria** en el momento en que los bienes se entregan y, por tanto, se facturan, o en el momento en que los servicios se han ejecutado y, por tanto, se facturan; y que los informes de **Retención** **reconocen la obligación tributaria** en el momento en que se contabiliza la factura de bienes o servicios, pero en otros países como España, en el momento en que se satisfacen o se pagan los ingresos en efectivo o en especie ya facturados y contabilizados.

Por lo tanto, y teniendo en cuenta que su empresa está ubicada en España, Etendo debe cubrir sus necesidades contables, que son:

**Los importes de IVA deben contabilizarse** y, por tanto, incluirse en contabilidad, **en el momento en que se contabiliza una factura** que contiene IVA, siempre que la fecha de la factura sea la misma que la fecha de expedición de los bienes o la fecha de ejecución del servicio.  
**Los importes de Retención deben contabilizarse** y, por tanto, incluirse en contabilidad, **en el momento en que se contabiliza una factura que contiene Retención**, ya que hay algunos países como España en los que los importes de retención deben contabilizarse al mismo tiempo que los importes de IVA, es decir, en el momento en que se contabiliza una factura que contiene retención, independientemente de que la obligación tributaria para este tipo de impuestos se reconozca en el momento en que se paga dicha factura.

Mary también debe ser consciente de que la mayoría de las transacciones sujetas a impuestos se introducirán en el sistema como una transacción de compra o de venta y, por tanto, como una factura de compra o de venta, pero también habrá algunas que no tendrán una factura asociada. Estos últimos casos están principalmente relacionados con la retención, que deberá introducirse en el sistema como **liquidaciones manuales vinculadas a los Concepto contable correspondientes.**  
**La liquidación manual generará el asiento contable de retención** en el caso de retenciones que no tengan una factura vinculada y, por tanto, deban introducirse en el sistema como una liquidación manual, lo que implicará posteriormente un pago en efectivo o por banco.
#### Configuración general del sistema
Mary informa al personal de contabilidad sobre qué informes fiscales deben presentarse a las autoridades tributarias por parte de la empresa, para que Peter pueda **comprobar la configuración** o **configurar** los parámetros fiscales, las categorías fiscales de terceros y los informes fiscales y los parámetros de informes fiscales necesarios; después, introducir las transacciones contables correspondientes en colaboración con el personal de ventas y compras, para finalmente ejecutar los informes fiscales y obtener la salida del informe fiscal que se presentará a las autoridades tributarias.

##### Primer paso:
El **primer** paso que Peter debe realizar es **comprobar la configuración** o **configurar** los parámetros fiscales requeridos según el flujo de trabajo que se indica a continuación:

1. Peter va a **Gestión Financiera / Contabilidad / Configuración / Categoría de Impuestos de Terceros** para crear las **categorías fiscales de terceros** necesarias en función de quién haya generado una transacción de venta o compra sujeta a IVA o quién haya generado un ingreso sujeto a retención. Por ejemplo, debe introducir como categoría fiscal de tercero: Proveedor nacional, Proveedor UE, Proveedor internacional, Cliente nacional, Cliente UE, Cliente internacional, Empleados, Empleados no residentes, Profesionales, Profesionales UE, Profesional internacional, Alquiler, Actividades económicas, etc. 
2. Peter va a **Gestión Financiera / Contabilidad / Configuración / Código de transacción** para comprobar que los "códigos de transacción" de IVA requeridos para transacciones de compra o de venta están configurados por defecto. Como ya se ha indicado, los más comunes son => Suministros (por ejemplo, este tipo de código de transacción en España es ="E") y Adquisiciones (por ejemplo, este tipo de código de transacción en España es ="A")
3. Después, Peter va a **Gestión Financiera / Contabilidad / Configuración / Clave de impuesto** para comprobar que las **claves de impuesto y subclaves** requeridas están configuradas por defecto en función del tipo de ingreso y del tercero que haya generado ese ingreso. Por ejemplo, en el caso del informe fiscal español 110, debe saber que tiene que crear una clave de impuesto = "A" para ingresos del trabajo, una clave de impuesto = "G" para ingresos por actividades profesionales, una clave de impuesto = "K" para premios, etc. 
4. Una vez hecho lo anterior, Peter va a **Gestión Financiera / Contabilidad / Configuración / Categoría de Impuesto** ya que puede ser necesario crear nuevas categorías de impuesto. Por ejemplo IVA (en caso de IVA soportado), IVA ventas, IVA intracomunitario, IVA ventas intracomunitario, IVA importación, IVA exportación, IVA+EC, IVA ventas+EC, WSalary, WProfessionals, WPrizes, PSalary, PProfessionals, PPrizes.
5. Y una vez hecho lo anterior, Peter va a **Gestión Financiera / Contabilidad / Configuración / Rangos de impuesto** ya que puede ser necesario crear nuevos **Impuestos** y nuevos **rangos de retención**. Los rangos de IVA dependen del tipo de transacción, de si es una compra o una venta, y del tipo de bienes que se compran o venden; y los rangos de retención dependen del tipo de ingreso que se paga y del tercero que haya generado ese ingreso.

!!! info
    Al utilizar esta forma de configuración de retenciones, Peter debe asegurarse de que desea contabilizar la retención en el momento en que se contabiliza una factura que contiene un ingreso sujeto a retención, independientemente de que la obligación de retención se reconozca en la fecha de pago, y no en el momento en que se paga esa factura. Los rangos de impuesto deben estar vinculados a la categoría fiscal de tercero correspondiente y debe configurarse la contabilidad correspondiente.

Rangos de IVA = por ejemplo VAT21%, VAT10%, VAT4%, VAT21%+EC4%, VAT10%+EC1,5%, VAT4%+EC0,5%, SalesVAT21%, SalesVAT10%, SalesVAT4%, SalesVAT21%+EC4%, SalesVAT10%+EC1,5%, SalesVAT4%+EC0,5%, Intra-VAT21%/-21%, Intra-VAT0%, ImportVAT21%, ExportVAT0%. Además, los rangos de IVA existentes y los nuevos deberán estar **vinculados** a los **Códigos de transacción** correspondientes en función de la dirección del IVA.  
Rangos de retención = por ejemplo WSalary35%, WPrizes18%, WProfessionals15%, WProfessionals7%. Además, los rangos de retención existentes y los nuevos, así como los rangos fiscales de pagos a cuenta, deben estar **vinculados** a las **claves y subclaves** tributarias correspondientes en función de los informes fiscales en los que se vayan a incluir esos rangos.

6. El paso anterior también podría realizarlo Peter desde **Gestión de datos maestros / Configuración de tercero / Retención**. Deberá elegir esta vía y no la anterior en relación con los rangos de retención en caso de que necesite contabilizar los importes de retención en el momento en que se paga una factura y no en el momento en que se contabiliza la factura. Por ejemplo WSalary35%, WPrizes18%, WProfessionals15%, WProfessionals7%. Además, los rangos de retención existentes y los nuevos deben estar **vinculados** a las **claves y subclaves** tributarias correspondientes en función de los informes fiscales en los que se vayan a incluir esos rangos. 

##### Segundo paso:
El **segundo** paso que Peter debe realizar es comprobar que los **Informes de impuestos** y los **parámetros de informes fiscales** están correctamente configurados por defecto. Para ello, deberá navegar a **Gestión Financiera / Contabilidad / Configuración / Informe fiscal.**
 
**Informe fiscal.** Debe existir un registro para cada informe fiscal que deba presentarse a las autoridades tributarias. Cada informe fiscal debe incluir la siguiente información:

a) **Grupos de informe fiscal.** Para algunos países como España, los informes fiscales de retenciones tienen una estructura fija de secciones denominada grupos de informe fiscal. Por ejemplo, en el caso de España, los informes fiscales de retenciones tienen 7 secciones por defecto, que son:
(1) Identificación  
(2) Devengo  
(3) Liquidación del impuesto  
(4) Recaudación tributaria  
(5) Declaración negativa  
(6) Declaración complementaria y  
(7) Firma.

!!! info
    En general, los informes de IVA no tienen ese tipo de secciones porque no son informes fiscales como tales, sino informes fiscales de tipo extracto, por lo que debe crearse una única sección de salida para este tipo de informes. 

 b) **Parámetros de informes fiscales**. Cada informe fiscal tendrá parámetros de informe fiscal específicos que Peter debe conocer para realizar la configuración correcta.  
***Parámetros de entrada**. Son parámetros de informe fiscal específicos que se necesitan en el momento en que se ejecuta un informe fiscal o un informe fiscal de tipo extracto; por tanto, este tipo de parámetros deberán ser **introducidos manualmente** por él al ejecutar un informe fiscal.  
Por ejemplo, "Nombre de archivo del informe fiscal", "persona de contacto" u otros más específicos en función del tipo de informe fiscal.  
***Parámetros constantes.** Parámetros constantes específicos del informe fiscal que deben **configurarse por defecto**, ya que siempre serán los mismos.  
Por ejemplo, en el caso del informe fiscal español 110, debe comprobar que el parámetro constante "Modelo fiscal" se introduce como "110", y "01" como número de página.  
***Parámetros de salida**. Peter debe saber que los parámetros de salida son parámetros del informe fiscal que obtendrán información del sistema, como "Nombre de la empresa", "NIF de la empresa", así como datos/salidas más complejos relacionados con transacciones vinculadas, por ejemplo, a unas **"claves de impuesto y/o subclaves"** específicas. Es el momento de comprobar que esos parámetros de salida están configurados por defecto correctamente y vinculados a un informe fiscal específico.
#### Configuración específica y transacciones

En colaboración con el equipo de ventas (Mike) y el personal de compras (Alice), Peter necesita introducir en el sistema las transacciones de actividad normal que se incluirán en uno u otro informe de impuestos en función del tipo de transacción del que estemos hablando:

##### Compras – Escenario general

Alice crea una **necesidad de material** en función de las necesidades de artículos y/o servicios de la empresa o entidad. En cuanto Dan, el responsable de compras, confirma las necesidades de material, ella convierte la(s) necesidad(es) de material en uno o varios **pedido de compra** y los envía al tercero correspondiente (proveedor o acreedor o profesional).
Una vez que su empresa ha **recibido los bienes** o que el acreedor ha **ejecutado los servicios** solicitados por su empresa, el proveedor o acreedor emitirá una factura. Esa factura deberá ser introducida por Alice en el sistema como una **Factura (Proveedor)**.
En general, las transacciones de compra y, por tanto, la Factura (Proveedor) pueden ser el resultado de la adquisición de bienes o de servicios prestados por proveedores ubicados en España, en la UE o en el extranjero; por ello, en función del origen de los bienes y del tipo de bienes/servicios intercambiados, el tipo de IVA a pagar (IVA-crédito fiscal), así como el código de transacción, serán diferentes.
Además, existen algunos tipos de transacciones de compra para las que será aplicable la retención, así como las claves tributarias correspondientes, en función del tipo de ingreso generado y del tipo de tercero que los haya generado.

##### Compras - Escenarios específicos y configuración requerida

Alice podría introducir en el sistema cualquiera de las Factura (Proveedor) de compra listadas a continuación, ya que son escenarios de compra muy comunes para una empresa pequeña-mediana ubicada en un país de la UE como España. Peter y Alice deberán comprobar que, al menos, la información listada a continuación por transacción de Factura (Proveedor) de compra está correctamente configurada antes de introducir cualquier transacción de compra.

1- **Compra de bienes a un proveedor nacional**
1. Ruta del sistema: Gestión de aprovisionamiento / Transacciones / Factura (Proveedor)
2. Categoría de Impuestos de Terceros: Proveedor nacional
3. Categoría de Impuesto: IVA
4. Rango impuesto (Impuesto de compra): VAT21% y/o VAT10% y/o VAT4%
5. Rango impuesto - código de transacción: "A" (adquisición)

2- **Compra de bienes a un proveedor nacional (escenario EC)**
1. Categoría de Impuestos de Terceros: Proveedor nacional
2. Categoría de Impuesto (impuesto de compra): VAT+EC
3. Rango impuesto (Impuesto de compra): VAT21%+EC4% y/o VAT10%+EC1,5% y/o VAT4%+EC0,5%
4. Rango impuesto - código de transacción: "A" (adquisición)

3- **Compra de bienes a un proveedor de la UE**
1. Ruta del sistema: Gestión de aprovisionamiento / Transacciones / Factura (Proveedor)
2. Categoría de Impuestos de Terceros: Proveedor UE
3. Categoría de Impuesto: IntraVAT
4. Rango impuesto (IVA de compra e IVA de venta): IntraVAT21%/-21%
5. Rango impuesto - código de transacción: "A" (adquisición)

4- **Compra de bienes a un proveedor internacional**

1. Ruta del sistema: Gestión de aprovisionamiento / Transacciones / Factura (Proveedor)
2. Categoría de Impuestos de Terceros: Proveedor internacional
3. Categoría de Impuesto: ImportVAT
4. Rango impuesto (Impuesto de compra): ImportVAT21%
5. Rango impuesto - código de transacción: "A" (adquisición)

5- **Compra de servicios profesionales a un profesional nacional**
1. Ruta del sistema: Gestión de aprovisionamiento / Transacciones / Factura (Proveedor)
2. Categoría de Impuestos de Terceros: Profesionales nacionales
3. Categoría de Impuesto: VAT+WProfessionals
4. Rango impuesto (Impuesto de compra): VAT21%+WProfessionals15%
5. Rango impuesto - clave tributaria: "G-01 o G-02 o G-03
6. Rango impuesto - código de transacción: "A" (adquisición)

6- **Compra de servicios profesionales a un profesional de la UE**
1. Ruta del sistema: Gestión de aprovisionamiento / Transacciones / Factura (Proveedor)
2. Categoría de Impuestos de Terceros: Profesionales UE
3. Categoría de Impuesto: IntraVAT+WProfessionals
4. Rango impuesto (IVA de compra e IVA de venta): IntraVAT21%/-21%+WProfessionals24%
5. Rango impuesto - clave tributaria: "19"
6. Rango impuesto - código de transacción: "A" (adquisición)

7- **Compra de servicios profesionales a un profesional internacional**
1. Ruta del sistema: Gestión de aprovisionamiento / Transacciones / Factura (Proveedor)
2. Categoría de Impuestos de Terceros: Profesionales internacionales
3. Categoría de Impuesto: ImportVAT+WProfessionals
4. Rango impuesto (Impuesto de compra):ImportVAT21%+WProfessionals24%
5. Rango impuesto - clave tributaria: "19"
6. Rango impuesto - código de transacción: "A" (adquisición)


###### Factura (Proveedor) de compra de bienes

Al introducir una Factura (Proveedor) de compra de bienes en el sistema, Alice debe asegurarse de que el IVA se va a calcular correctamente tal y como se ha descrito anteriormente:
Proveedor nacional:
Importe de la factura = 100.000 € => Importe de la base imponible = 100.000 €
VAT21% = 100.000 € x 21% = 21.000 € => Importe de IVA = 21.000 €
Importe total de la factura a pagar al proveedor = 121.000 €
Proveedor UE;
Importe de la factura = 100.000 € => Importe de la base imponible = 100.000 €
IntraVAT21%/-21% = [100.000 € x 21% = 21.000] + [100.000 € x -21% = -21.000] = 0 € => Importe de IVA = 0 €
Importe total de la factura a pagar al proveedor = 100.000 €
Proveedor internacional:
Importe de la factura = 100.000 € => Importe de la base imponible = 100.000 €
ImportVAT21% = 100.000 € x 21% = 21.000 € => Importe de IVA = 21.000 €
Importe total de la factura a pagar al proveedor = 121.000 €

###### Recargo de equivalencia

En este caso, la empresa de Alice (entidad legal de Etendo) es una empresa minorista que compra bienes únicamente a proveedores nacionales y bajo este régimen específico de IVA.
Aunque la empresa de Alice no está obligada a realizar el seguimiento del IVA-crédito fiscal y del IVA-débito fiscal y no está obligada a liquidar el IVA, sí está obligada a informar a sus proveedores de que está sujeta al régimen especial de recargo de equivalencia (EC), con el objetivo de permitir que sus proveedores le apliquen un tipo impositivo adicional denominado tipo de recargo de equivalencia (EC).
Al introducir una Factura (Proveedor) de compra de bienes en el sistema bajo este régimen específico de IVA, Alice debe asegurarse de que los impuestos de IVA y EC se calculan correctamente tal y como se ha descrito anteriormente:

Importe de la factura = 100.000 € => Importe de la base imponible = 100.000 €
VAT21% = 100.000 € x 21% = 21.000 => Importe de IVA = 21.000 €
EC4% = 100.000 € x 4% = 4.000 €
Importe total de la factura a pagar al proveedor nacional = 100.000 € + 21.000 € + 4.000 € = 125.000 €

###### Factura (Proveedor) de compra de servicios profesionales

Al introducir una Factura (Proveedor) de compra de servicios en el sistema, Alice debe asegurarse de que el IVA y la retención se van a calcular correctamente tal y como se ha descrito anteriormente:

Importe de la factura = 100.000 € => Importe de la base imponible = 100.000 €
VAT21% = 100.000 € x 21% = 21.000 => Importe de IVA = 21.000 €
W-18% = 100.000 € x -15% = -15.000 => Importe de la retención = -15.000 €
Importe total de la factura a pagar a un proveedor profesional = 100.000 € + 21.000 € -15.000 € = 106.000 €

###### Inversión del sujeto pasivo

Alice debe saber que un tipo IntraVAT podría marcarse como “Inversión del sujeto pasivo” únicamente en el caso de servicios prestados por profesionales de la UE, ya que ya no es obligatorio para las adquisiciones de bienes en la UE. En ese caso, la empresa tendrá que crear una autofactura después de recibir la Factura (Proveedor) de compra de servicios con un tipo de IVA = 0%
Por lo tanto, deberá haber 3 asientos para cada factura bajo este escenario con un código de operación = "I":

- la línea de la autofactura del IVA-crédito fiscal (IntraVAT21%=21%)
- la línea de la autofactura del IVA-débito fiscal (SalesIntraVAT=-21%)
- y la línea de la Factura (Proveedor) original como importación o exenta (ImportVAT = 0%).

!!! info
    Tenga en cuenta que la línea de IVA-crédito fiscal y la línea de IVA de importación o exento se mostrarán y almacenarán como IVA soportado/recibido (IVA-crédito fiscal), mientras que la línea de IVA-débito fiscal se mostrará y almacenará como IVA repercutido/emitido.


##### Abonos de compra

En caso de que exista algún error en las Factura (Proveedor) de compra de bienes o servicios prestados por un tercero, o en caso de que haya que devolver bienes a un proveedor por falta de calidad o cualquier otro tipo de error, Alice y el personal de contabilidad deberán anular la Factura (Proveedor) correspondiente y crear y contabilizar una nueva factura de abono de compra (nota de crédito de compra). En este caso, los escenarios aplicables son los mismos que los descritos en la sección anterior, pero:
1. Los importes de las facturas de abono de compra serán importes negativos
2. Peter debe asegurarse de que facturas de abono de compra similares no se agrupen al incluirse en los informes de IVA.

##### Ventas - Escenario general

Mike crea un **Pedido de venta** en función de la(s) necesidad(es) de un cliente. Una vez que su empresa ha **enviado los bienes** mediante un albarán de salida, le es posible emitir una **Factura (Cliente)** y enviarla al cliente junto con la documentación del envío de mercancía, por ejemplo, un albarán de entrega.
En general, las transacciones de venta y, por tanto, las **Factura (Cliente)** podrían ser el resultado de envíos de bienes o de servicios prestados por una empresa a un cliente o tercero ubicado en España, en la UE o en el extranjero; por ello, en función del destino de los bienes y del tipo de bienes/servicios prestados, el tipo de IVA a cobrar (IVA-débito fiscal), así como el código de transacción, serán diferentes.
Además, existen algunos tipos de transacciones de venta para las que será aplicable la retención, así como las claves tributarias correspondientes, en función del tipo de ingreso generado.

##### Ventas - Escenarios específicos y configuración requerida

Mike podría introducir en el sistema cualquiera de las transacciones de venta listadas a continuación, ya que son escenarios de venta muy comunes para una empresa pequeña-mediana ubicada en un país de la UE como España. Peter y Mike deberán comprobar que, al menos, la información listada a continuación por transacción de Factura (Cliente) de venta está correctamente configurada antes de introducir cualquier transacción de venta.

1- **Venta de bienes a un cliente nacional (España)**
1. Ruta del sistema: Gestión de ventas / Transacciones / Factura (Cliente)
2. Categoría de Impuestos de Terceros: Cliente nacional
3. Categoría de Impuesto: SalesVAT
4. Rango impuesto (Impuesto de venta): SalesVAT21% y/o SalesVAT10% y/o SalesVAT4%
5. Rango impuesto - código de transacción: "E" (suministro)


2- **Venta de bienes a un minorista nacional (escenario EC)**
1. Y Categoría de Impuestos de Terceros: Minorista nacional
2. Categoría de Impuesto: SalesVAT+EC
3. Rango impuesto (Impuesto de venta): SalesVAT21%+EC4% y/o SalesVAT10%+EC1,5% y/o SalesVAT4%+EC0,5%
4. Rango impuesto - código de transacción: "E"(suministro)

3- **Venta de bienes a un cliente de la UE**
1. Ruta del sistema: Gestión de ventas / Transacciones / Factura (Cliente)
2. Categoría de Impuestos de Terceros: Cliente UE
3. Categoría de Impuesto: SalesIntraVAT
4. Rango impuesto (Impuesto de venta): SalesIntraVAT0%
5. Rango impuesto - código de transacción: "E" (suministro)

4- **Venta de bienes a un cliente internacional**
1. Ruta del sistema: Gestión de aprovisionamiento / Transacciones / Factura (Proveedor)
2. Categoría de Impuestos de Terceros: Proveedor internacional
3. Categoría de Impuesto: ExportVAT
3. Rango impuesto (Impuesto de venta): ExportVAT0%
4. Rango impuesto - código de transacción: "E" (suministro)

5- **Servicio prestado a un cliente nacional**
1. Ruta del sistema: Gestión de ventas / Transacciones / Factura (Cliente)
2. Categoría de Impuestos de Terceros: Clientes nacionales
3. Categoría de Impuesto: SalesVAT+SalesW
4. Rango impuesto (impuesto de venta9 : SalesVAT21%+SalesWProfessionals15%
5. Rango impuesto - clave tributaria: no aplicable
5. Rango impuesto - código de transacción: "E" (suministro)

6- **Servicio prestado a un cliente de la UE**
1. Ruta del sistema: Gestión de ventas / Transacciones / Factura (Cliente)
2. Categoría de Impuestos de Terceros: Cliente UE
3. Categoría de Impuesto: SalesIntaVAT+SalesW
4. Rango impuesto (Impuesto de venta): SalesIntraVAT0%+SalesWProfessionals15%
5. Rango impuesto - clave tributaria: no aplicable
6. Rango impuesto - código de transacción: "E" (suministro)

7- **Servicio prestado a un cliente internacional**
1. S1. Ruta del sistema: Gestión de ventas / Transacciones / Factura (Cliente)
2. Categoría de Impuestos de Terceros: Clientes internacionales
3. Categoría de Impuesto: ExportVAT+SalesW
4. Rango impuesto (Impuesto de venta):ExportVAT0%+SalesWProfessionals15%
5. Rango impuesto - clave tributaria: no aplicable
6. Rango impuesto - código de transacción: "E" (suministro)


###### Factura (Cliente) de venta de bienes
Al introducir una Factura (Cliente) de venta de bienes en el sistema, Mike debe asegurarse de que el IVA repercutido se va a calcular correctamente tal y como se ha descrito anteriormente:
Cliente nacional:
Importe de la factura = 100.000 € => Importe de la base imponible = 100.000 €
SalesVAT21% = 100.000 € x 21% = 21.000 => Importe de IVA repercutido = 21.000 €
Importe total de la factura a cobrar al cliente = 121.000 €
Proveedor UE;
Importe de la factura = 100.000 € => Importe de la base imponible = 100.000 €
SalesIntraVAT0% = 100.000 € x 0% = 0 €=> Importe de IVA repercutido = 0 €
Importe total de la factura a cobrar al cliente = 100.000 €
Proveedor internacional:
Importe de la factura = 100.000 € => Importe de la base imponible = 100.000 €
Export0% = 100.000 € x 0% = 0 € => Importe de IVA = 0 €
Importe total de la factura a cobrar al cliente = 100.000 €

###### Recargo de equivalencia

En este caso, la empresa de Mike vende bienes a una empresa minorista nacional y debe aplicarle un tipo impositivo adicional denominado tipo de recargo de equivalencia (EC).
Por lo tanto, al introducir una Factura (Cliente) de venta de bienes en el sistema bajo este régimen específico de IVA, Mike debe asegurarse de que el IVA repercutido y los impuestos EC se calculan correctamente tal y como se ha descrito anteriormente:
Importe de la factura = 100.000 € => Importe de la base imponible = 100.000 €
SalesVAT21% = 100.000 € x 21% = 21.000 € => Importe de IVA repercutido = 21.000 €
EC4% = 100.000 € x 4% = 4.000 €
Importe total de la factura a cobrar al minorista = 100.000 € + 21.000 € + 4.000 € = 125.000 €

###### Factura (Cliente) de venta de servicios profesionales

Al introducir una Factura (Cliente) de venta de servicios en el sistema, Mike debe asegurarse de que el IVA repercutido y la retención se van a calcular correctamente tal y como se ha descrito anteriormente:
Importe de la factura = 100.000 € => Importe de la base imponible = 100.000 €
Sales VAT21% = 100.000 € x 21% = 21.000 => Importe de IVA = 21.000 €
SalesWProfessionals15% = 100.000 € x -15% = -15.000 => Importe de la retención = -15.000 €
Importe total de la factura a cobrar al cliente = 100.000 € + 21.000 € -15.000 € = 106.000 €


##### Facturas de abono de venta

En caso de que exista un error en las Factura (Cliente) de venta de bienes o servicios que la empresa de Mike está prestando a sus clientes, o en caso de que un cliente quiera devolver bienes por falta de calidad o cualquier otro tipo de error, Mike y el personal de contabilidad deberán anular la Factura (Cliente) correspondiente y crear y contabilizar una nueva factura de abono de venta (nota de crédito de venta). En este caso, los escenarios aplicables son los mismos que los descritos en la sección anterior, pero:
1. Los importes de las facturas de abono de venta serán importes negativos
2. Mike debe asegurarse de que facturas de abono de venta similares no se agrupen al incluirse en los informes de IVA.

##### Liquidación manual

Peter tendrá que utilizar la funcionalidad de Etendo de **Liquidación manual** para **introducir en el sistema el resto de ingresos sujetos a impuestos** **que no pueden introducirse en el sistema** ni como una transacción de compra y, por tanto, como una Factura (Proveedor), ni como una transacción de venta y, por tanto, como una Factura (Cliente).
Peter tendrá que utilizar **Concepto contable** al introducir liquidaciones manuales, ya que no habrá una factura detrás de este tipo de transacciones, sino un tercero y un ingreso satisfecho o pagado por su empresa, o un ingreso cobrado por su empresa; por lo tanto, Peter tendrá que crear tantos Concepto contable como sea necesario en función del **tipo de ingresos** cobrados o pagados y del **tipo de terceros** implicados en la generación del ingreso.

**La creación de Concepto contable está principalmente relacionada con los informes de Retención** ya que esos informes son los que contienen transacciones de ingresos sujetos a impuestos no soportadas ni por Factura (Proveedor) ni por Factura (Cliente).
!!! info
    Peter tendrá que asegurarse de que los Concepto contable están vinculados al rango impuesto correspondiente y a los tipos de retención, si aplica; además, Peter tendrá que asegurarse de que los Concepto contable tienen la configuración contable correspondiente con antelación.

Los escenarios siguientes explican que Peter tendrá que crear al menos dos Concepto contable por transacción; no utilizará la funcionalidad de contabilización directa, ya que estos tipos de retención, los introducidos en el sistema como liquidación manual, solo pueden contabilizarse en el momento del pago mediante diario de caja o diario de pagos.

###### Pagos de salarios de empleados

Peter sabe que Etendo no automatiza las transacciones de pago de nóminas, por lo que, para registrar en el sistema una transacción de pago de salario de un empleado, Peter tendrá que utilizar la funcionalidad de "liquidación manual" como primer paso y, a continuación, liquidarla o pagarla utilizando un pago en efectivo o un pago bancario.
Al hacerlo, debe asegurarse de que la transacción está vinculada a los Concepto contable específicos creados para ese fin y, además, Peter debe introducir la retención correspondiente, ya que este tipo de pagos están sujetos a retención, que deberá presentarse posteriormente ante la administración tributaria.

Para llevar a cabo el escenario anterior, Peter tendrá que navegar a:

- Gestión financiera / Contabilidad / configuración / **Categoría de Impuestos de Terceros** para crear la categoría fiscal del tercero => "Operarios" (pendiente de discutir)
- Gestión financiera / Contabilidad / configuración / **Categoría de Impuesto** para crear la categoría de impuesto => "WSalary"
- Gestión financiera / Contabilidad / configuración / **Clave de impuesto** para comprobar que la clave de impuesto y subclaves correspondientes están configuradas por defecto => "A = Employment Income"
- Gestión financiera / Contabilidad / configuración / **Rango impuesto** para crear el rango impuesto => "WSalary35%"; en esta misma pantalla y en la pestaña **"Parámetro de impuesto"** Peter debe configurar el parámetro de informe de impuestos correspondiente para que el rango impuesto pueda vincularse al informe de impuestos correspondiente (110), grupo de informes de impuestos (Evaluaciones), parámetro de impuesto (Retenciones y pagos a cuenta) y clave tributaria (A-Employment income).
- Gestión financiera / Contabilidad / configuración / **Concepto contable** para crear el Concepto contable => "Employee income in cash withholding", que debe estar vinculado al rango impuesto "WSalary35%" y a la configuración contable correspondiente.
- Gestión financiera / Contabilidad / configuración / **Concepto contable** para crear el Concepto contable => "Outstanding salary payments" con la configuración contable correspondiente.


Una vez que lo anterior esté configurado en el sistema, Peter debe navegar a Gestión financiera / Cuentas a cobrar y a pagar / Transacciones / Liquidación manual y crear una nueva liquidación manual como se describe a continuación:
Fecha de transacción => 26-June-2021
Fecha contable => 30-June-2021
Descripción => Salario de Alice

A continuación, Peter va a la ventana **Efectos manuales** e introduce dos nuevos como se describe a continuación:
Tercero => Alice (creada previamente como empleada con categoría fiscal del tercero = Operarios
Descripción => Salario de Alice junio
Importe => 1000
Entrega => No
Contabilización directa => No

A continuación, Peter va a la ventana **Conceptos** e introduce uno nuevo como se describe a continuación:
Concepto contable => Employment income in cash withholding
Importe debe => 350
y Concepto contable => "Outstanding salary payments"
Importe debe => 650

Una vez hecho todo lo anterior, Peter procesa la liquidación manual y navega a Gestión financiera / Cuentas a cobrar y a pagar / Transacciones / Diario de caja y crea uno nuevo e introduce:
Fecha de transacción=> 30-June-2021
Fecha contable=> 30-June-2021

y luego va a Líneas y crea una nueva como:
Tipo de caja => Pago-deuda y luego hace clic en la funcionalidad Deuda/pago para entrar en el Selector de pago de deuda.

Una vez en el Selector de pago de deuda, Peter tiene que desmarcar "Entrega" y buscar por pendientes para seleccionar el que acaba de introducir.

Después de eso, Peter procesa y contabiliza.
Peter puede navegar al asiento contable y luego a las líneas del diario de caja, y luego al pago, y una vez allí Peter puede seleccionar y contabilizar "Liquidación cancelada" para generar y comprobar la contabilización final.

Finalmente, Peter tiene que verificar que los informes de Retención correspondientes muestran un importe de retención de 350 vinculado al tipo WSalary35%.

###### Pagos de premios

La empresa de Peter organizó una competición entre sus empleados. Alice ganó ese premio, que fue un premio "en efectivo" de 500 €, que debe incluirse en el sistema. Para ello, Peter tendrá que utilizar la funcionalidad de "liquidación manual" como primer paso y, a continuación, liquidarlo o pagarlo utilizando un pago en efectivo o un pago bancario.
Al hacerlo, debe asegurarse de que la transacción está vinculada a los Concepto contable específicos creados para ese fin y, además, Peter debe introducir la retención correspondiente, ya que este tipo de pagos están sujetos a retención, que deberá presentarse posteriormente ante la administración tributaria.

Para llevar a cabo el escenario anterior, Peter tendrá que navegar a:

- Gestión financiera / Contabilidad / configuración / **Categoría de Impuestos de Terceros** para crear la categoría fiscal del tercero => "Operarios"
- Gestión financiera / Contabilidad / configuración / **Categoría de Impuesto** para crear la categoría de impuesto => "WPrize"
- Gestión financiera / Contabilidad / configuración / **Clave de impuesto** para crear la clave de impuesto y subclaves correspondientes => "K_01=Prizes_01"
- Gestión financiera / Contabilidad / configuración / **Rango impuesto** para crear el rango impuesto => "WPrize18%"; en esta misma pantalla y en la pestaña **"Parámetro de impuesto"** Peter debe configurar el parámetro de informe de impuestos correspondiente para que el rango impuesto pueda vincularse al informe de impuestos correspondiente (110), grupo de informes de impuestos (Evaluaciones), parámetro de impuesto (Retenciones y pagos a cuenta) y clave tributaria (K_01 - Prizes 01).
- Gestión financiera / Contabilidad / configuración / **Concepto contable** para crear el Concepto contable => "Prizes income in cash withholding", que debe estar vinculado al rango impuesto "WPrize18%" y a la contabilidad correspondiente.
- Gestión financiera / Contabilidad / configuración / **Concepto contable** para crear el Concepto contable => "Prizes in cash" con la configuración contable correspondiente.

Una vez que lo anterior esté configurado en el sistema, Peter debe navegar a Gestión financiera / Cuentas a cobrar y a pagar / Transacciones / Liquidación manual y crear una nueva liquidación manual como se describe a continuación:

Fecha de transacción => 01-July-2021
Fecha contable => 01-July-2021
Descripción => Premio de Alice (mejor diseño de producto X)

A continuación, Peter va a la ventana **Efectos manuales** e introduce uno nuevo como se describe a continuación:
Tercero => Alice (creada previamente como empleada con categoría fiscal del tercero = Operarios
Descripción => Premio de Alice
Importe => 500
Entrega => No
Contabilización directa => No

A continuación, Peter va a la ventana **Conceptos** e introduce dos nuevos como se describe a continuación:
Concepto contable => Prizes in cash
Importe debe => 450
y Concepto contable => Prizes income in cash withholding
Importe debe => 50

Una vez hecho todo lo anterior, Peter procesa la liquidación manual y navega a Gestión financiera / Cuentas a cobrar y a pagar / Transacciones / Diario de caja y crea uno nuevo e introduce:
Fecha de transacción=> 01-July-2021
Fecha contable=> 01-July-2021
y luego va a Líneas y crea una nueva como:

Tipo de caja => Pago-deuda y luego hace clic en la funcionalidad Deuda/pago para entrar en el Selector de pago de deuda.

Una vez en el Selector de pago de deuda, Peter tiene que desmarcar "Entrega", y buscar por pendientes, para que se pueda seleccionar el de "premio" que acaba de crear.

Después de eso, Peter procesa y contabiliza.
Peter puede navegar al asiento contable y luego a las líneas del diario de caja, y luego al pago, y una vez allí Peter puede seleccionar y contabilizar "Liquidación cancelada" para generar y comprobar la contabilización final.

Finalmente, Peter tiene que verificar que los informes de Retención correspondientes muestran un importe de retención de 50 vinculado al tipo WPrize18%.

**Alquiler de edificio en caso de edificio de un tercero**

La empresa de Peter alquila un edificio propiedad de un tercero en el que se encuentra la oficina de la empresa de Peter. El propietario de ese edificio emite cada mes a la empresa de Peter un "extracto o un recibo" para que se le pague ese alquiler. La empresa de Peter tiene que pagar ese alquiler e introducir en el sistema el extracto y el pago correspondientes; por lo tanto, Peter tendrá que utilizar la funcionalidad de "liquidación manual" como primer paso y, a continuación, pagarlo utilizando un pago en efectivo o un pago bancario.

!!! info
    Al hacerlo, debe asegurarse de que la transacción está vinculada a los Concepto contable específicos creados para ese fin y, además, Peter debe introducir la retención correspondiente, ya que este tipo de pagos están sujetos a retención, que deberá presentarse posteriormente ante la administración tributaria.

Para llevar a cabo el escenario anterior, Peter tendrá que navegar a:

- Gestión financiera / Contabilidad / configuración / **Categoría de Impuestos de Terceros** para crear la categoría fiscal del tercero => "Arrendador"
- Gestión financiera / Contabilidad / configuración / **Categoría de Impuesto** para crear la categoría de impuesto => "WRenting"
- Gestión financiera / Contabilidad / configuración / **Clave de impuesto** para crear la clave de impuesto y subclaves correspondientes => "P -Renting"
- Gestión financiera / Contabilidad / configuración / **Rango impuesto** para crear el rango impuesto => "WRenting18%"; en esta misma pantalla y en la pestaña **"Parámetro de impuesto"** Peter debe configurar el parámetro de informe de impuestos correspondiente para que el rango impuesto pueda vincularse al informe de impuestos correspondiente (115), grupo de informes de impuestos (Evaluaciones), parámetro de impuesto (Retenciones y pagos a cuenta) y clave tributaria (P-Renting).
- Gestión financiera / Contabilidad / configuración / **Concepto contable** para crear el Concepto contable => "3rd party rent in cash Withholding", que debe estar vinculado al rango impuesto "WRenting18%" y a la configuración contable correspondiente.
- Gestión financiera / Contabilidad / configuración / **Concepto contable** para crear el Concepto contable => "3rd party rent" con la configuración contable correspondiente.

Una vez que lo anterior esté configurado en el sistema, Peter debe navegar a Gestión financiera / Cuentas a cobrar y a pagar / Transacciones / Liquidación manual y crear una nueva liquidación manual como se describe a continuación:

Fecha de transacción => 29-August-2021
Fecha contable => 01-September-2021
Descripción => Alquiler de septiembre

A continuación, Peter va a la ventana **Efectos manuales** e introduce uno nuevo como se describe a continuación:
Tercero => Tercero arrendador (creado previamente como acreedor y con categoría fiscal del tercero = Arrendador
Descripción => Alquiler de septiembre
Importe => 2000
Entrega => No
Contabilización directa => No

A continuación, Peter va a la ventana **Conceptos** e introduce dos nuevos como se describe a continuación:
Concepto contable => "3rd party rent in cash withholding"
Importe debe => 360
Concepto contable => "3rd party rent in cash"
Importe debe => 1640

Una vez hecho todo lo anterior, Peter procesa la liquidación manual y navega a Gestión financiera / Cuentas a cobrar y a pagar / Transacciones / Diario de caja y crea uno nuevo e introduce:

Fecha de transacción=> 01-September-2021
Fecha contable=> 01-September-2021
y luego va a Líneas y crea una nueva como:
Tipo de caja => Pago-deuda y luego hace clic en la funcionalidad Deuda/pago para entrar en el Selector de pago de deuda.

Una vez en el Selector de pago de deuda, Peter tiene que desmarcar "Entrega", y buscar por pendientes, para que se pueda seleccionar el de "alquiler" que acaba de crear.

Después de eso, Peter procesa y contabiliza.
Peter puede navegar al asiento contable y luego a las líneas del diario de caja, y luego al pago, y una vez allí Peter puede seleccionar y contabilizar "Liquidación cancelada" para generar y comprobar la contabilización final.

Finalmente, Peter tiene que verificar que los informes de Retención correspondientes muestran un importe de retención de 360 vinculado al tipo WRenting18%.


###### Alquiler en caso de un edificio no vinculado a una actividad económica
La empresa de Peter es propietaria de un edificio no relacionado con la actividad económica de la empresa de Peter. Ese edificio se alquila a un tercero o arrendatario. La empresa de Peter emite un extracto o un recibo y lo envía al arrendatario para que se pague mensualmente. La empresa de Peter debe cobrar el dinero e introducir en el sistema el pago correspondiente; para registrar esto en el sistema, Peter tendrá que utilizar la funcionalidad de "liquidación manual" como primer paso y, a continuación, cobrarlo utilizando un cobro en efectivo o un cobro bancario.

!!! info
    Al hacerlo, debe asegurarse de que la transacción está vinculada a un Concepto contable específico creado para ese fin y, además, Peter debe introducir la retención correspondiente, ya que este tipo de pagos están sujetos a retención, que deberá presentarse posteriormente ante la administración tributaria.

Para llevar a cabo el escenario anterior, Peter tendrá que navegar a:

- Gestión financiera / Contabilidad / configuración / **Categoría de Impuestos de Terceros** para crear la categoría fiscal del tercero => "Arrendatario"
- Gestión financiera / Contabilidad / configuración / **Categoría de Impuesto** para crear la categoría de impuesto => "WPropertyRent"
- Gestión financiera / Contabilidad / configuración / **Clave de impuesto** para crear la clave de impuesto y subclaves correspondientes => "C_04-Property Rent"
- Gestión financiera / Contabilidad / configuración / **Rango impuesto** para crear el rango impuesto => "WPropertyRent18%"; en esta misma pantalla y en la pestaña **"Parámetro de impuesto"** Peter debe configurar el parámetro de informe de impuestos correspondiente para que el rango impuesto pueda vincularse al informe de impuestos correspondiente (123), grupo de informes de impuestos (Evaluaciones), parámetro de impuesto (Retenciones y pagos a cuenta) y clave tributaria (C_04-Property Rent).
- Gestión financiera / Contabilidad / configuración / **Concepto contable** para crear el Concepto contable => "Property Rent in cash withholding", que debe estar vinculado al rango impuesto "WPropertyRent18%"
- Gestión financiera / Contabilidad / configuración / **Concepto contable** para crear el Concepto contable => "Property Rent in cash" con la configuración contable correspondiente.


Una vez que lo anterior esté configurado en el sistema, Peter debe navegar a Gestión financiera / Cuentas a cobrar y a pagar / Transacciones / Liquidación manual y crear una nueva liquidación manual como se describe a continuación:

Fecha de transacción => 29-September-2021
Fecha contable => 01-October-2021
Descripción => Alquiler de octubre

A continuación, Peter va a la ventana **Efectos manuales** e introduce uno nuevo como se describe a continuación:
Tercero => Tercero arrendatario (creado previamente como acreedor y con categoría fiscal del tercero = Arrendatario)
Descripción => Alquiler de octubre
Importe => -3500
Entrega => Sí
Contabilización directa => No

A continuación, Peter va a la ventana **Conceptos** e introduce dos nuevos como se describe a continuación:
Concepto contable => "Property Rent in cash withholding"
Importe debe => -630
Concepto contable => "Property Rent in cash"
Importe debe => -2870

Una vez hecho todo lo anterior, Peter procesa la liquidación manual y navega a Gestión financiera / Cuentas a cobrar y a pagar / Transacciones / Diario de caja y crea uno nuevo e introduce:
Fecha de transacción=> 01-October-2021
Fecha contable=> 01-October-2021
y luego va a Líneas y crea una nueva como:
Tipo de caja => Pago-deuda y luego hace clic en la funcionalidad Deuda/pago para entrar en el Selector de pago de deuda.

Una vez en el Selector de pago de deuda, Peter tiene que marcar "Entrega" y buscar por pendientes, para que se pueda seleccionar el de "alquiler propietario" que acaba de crear.

Después de eso, Peter procesa y contabiliza.
Peter puede navegar al asiento contable y luego a las líneas del diario de caja, y luego al pago, y una vez allí Peter puede seleccionar y contabilizar "Liquidación cancelada" para generar y comprobar la contabilización final.

Finalmente, Peter tiene que verificar que los informes de Retención correspondientes muestran un importe de retención de 630 vinculado al tipo WPropertyRent18%.
### Configuración del Lanzador de informes de impuestos

Tal y como se ha descrito anteriormente, Mary, la responsable de contabilidad, debe decidir qué informes de impuestos deben presentarse ante las autoridades fiscales en función de la actividad de su empresa y de los requisitos de las autoridades fiscales del país. Peter le ayudaría aquí, ya que es responsable de comprobar la configuración por defecto y/o configurar los parámetros de impuestos, los informes de impuestos y los parámetros de informes de impuestos, así como de introducir las transacciones contables correspondientes en colaboración con el equipo de ventas (Mike) y el personal de compras (Alice). Lo último que tendrá que hacer será lanzar los informes de impuestos y, por último, obtener la salida del informe de impuestos para presentarla ante las autoridades fiscales.

Una vez que Peter sepa qué informes de impuestos deben presentarse ante las autoridades fiscales hablando con Mary, tendrá que **instalar el módulo de datos de configuración** entregado como parte del módulo Tax Report Launcher; una vez hecho, deberá navegar a Financial Management / Accounting / Setup / Tax Report Launcher para comprobar que la configuración por defecto para cada informe de impuestos está configurada tal y como se describe a continuación:

1-Peter tendrá que comprobar que existe un **nuevo registro para cada informe de impuestos** que deba presentarse ante las autoridades fiscales, que contenga la siguiente información:

1. **Identificador** = id del informe de impuestos (en nuestro ejemplo, el informe de impuestos español "110")
2. **Nombre** = Nombre del informe de impuestos (en nuestro ejemplo "Retenciones y pagos a cuenta del impuesto sobre la renta (IRPF) - España")
3. **Descripción** = Descripción del informe de impuestos incluyendo el tipo de informe de impuestos y el propósito principal "Retenciones y pagos a cuenta realizados sobre rentas satisfechas por las empresas durante un periodo de tiempo"
4. **Periodo** = puede ser mensual, trimestral o anual, dependiendo de los requisitos de las autoridades fiscales y del tamaño de la empresa.
5. **Nombre de la clase Java** = aquí debe introducirse una clase Java independiente por cada informe de impuestos.
6. **Activo** = establecido en "Sí"

2- Para un informe específico (el que se acaba de crear) y una vez realizado lo anterior, Peter tendrá que navegar a la solapa **"Grupo de informes de impuestos"** y comprobar que se han creado los 7 grupos de informes de impuestos siguientes para informes de retenciones, así como 1 grupo de informe de impuestos de salida en el caso de informes de IVA:

1. **Identificación** (1) - Este grupo de informe de impuestos debe contener datos generales como el nombre de la empresa, el NIF, la dirección, etc., dependiendo del informe de impuestos que se esté introduciendo en el sistema.  
*Esos datos se consideran **parámetros del informe de impuestos** para ese grupo de informe de impuestos específico; por lo tanto, Peter tendrá que navegar a la solapa de parámetros del informe de impuestos y comprobar los parámetros. Cada parámetro debe ser un **"constante"**, en cuyo caso deberá introducirse un valor constante en el campo correspondiente; o un "parámetro de entrada", en cuyo caso deberá seleccionarse un parámetro de tipo entrada de una lista (casilla de verificación o texto); o un "parámetro de salida", en cuyo caso deberá seleccionarse una clave tributaria y subclave tributaria o un código de transacción.

*La sección de Identificación tendrá todo tipo de parámetros de impuestos: parámetros **"constantes"** como "id del informe de impuestos", **"parámetros de entrada"** que debe introducir el usuario al lanzar el informe, como "nombre de contacto", así como **"parámetros de salida"** obtenidos del sistema, como "nombre de la Organización/Entidad" y "NIF de la Organización/Entidad", además de aquellas transacciones fiscales vinculadas a una clave fiscal y subclave o a un código de transacción (en el caso de la sección de IVA, véase la nota siguiente).

2. **Devengo** (2) - Esta sección debe contener los datos de año y periodo en función de cuándo deba lanzarse un informe de impuestos específico y presentarse ante las autoridades fiscales.  
*Esos datos son "parámetros de entrada" que deberá introducir al lanzar el informe desde Financial Management / Accounting / Analysis tools / Tax Report Launcher".

3. **Liquidación de impuestos** (3) - Esta sección debe contener información relacionada con impuestos, como el número de beneficiarios de una renta, el tipo de renta, los importes de renta y los importes de impuestos para un periodo determinado. El contenido de esta sección dependerá del informe de impuestos que estemos introduciendo en el sistema.

*Esos datos se consideran **parámetros del informe de impuestos** para ese grupo de informe de impuestos específico; por lo tanto, Peter tendrá que navegar a la solapa de parámetros del informe de impuestos y comprobar que los parámetros correspondientes están ahí.

*La sección de Liquidación de impuestos tendrá **"parámetros de entrada"** que debe introducir el usuario, como "Importe a deducir solo en caso de escenario de declaración complementaria"; en general, los "parámetros de entrada" serán todo tipo de información fiscal necesaria para el grupo de informe de impuestos que no puede obtenerse del sistema porque no existe una lógica de negocio detrás. Además, también tendrá **"parámetros de salida"** como la suma de todos los "importes de rentas monetarias vinculadas a un tipo impositivo específico", independientemente de la forma en que se haya introducido en el sistema (ya sea como una Factura (Proveedor), una Factura (Cliente) o como una Liquidación manual). En general, los "parámetros de salida" serán todos aquellos parámetros cuyo valor puede obtenerse del sistema porque existe una lógica de negocio detrás.

4. I**ngresos fiscales** (4) - Esta sección debe contener principalmente el importe neto del impuesto a pagar a las autoridades fiscales en base al resultado de la sección (3).  
* Esos datos se consideran **parámetros del informe de impuestos** para ese grupo de informe de impuestos específico; por lo tanto, Peter tendrá que navegar a la solapa de parámetros del informe de impuestos y comprobar que los parámetros correspondientes están ahí.

* La sección de Ingresos fiscales tendrá **"parámetros de entrada"** que debe introducir el usuario al lanzar un informe de impuestos, como una "X" en el caso de que un ingreso fiscal positivo vaya a pagarse en efectivo o una "D" en caso de que un ingreso fiscal positivo vaya a pagarse mediante domiciliación bancaria. En general, los "parámetros de entrada" serán todo tipo de información fiscal necesaria para el grupo de informe de impuestos que no puede obtenerse del sistema porque no existe una lógica de negocio detrás. Además, también tendrá **"parámetros de salida"** como "importe de ingresos fiscales", cuyo valor deberá ser un valor calculado en función de la sección (3). En general, los "parámetros de salida" serán todos aquellos parámetros cuyo valor puede obtenerse del sistema porque existe una lógica de negocio detrás.

5. **Declaración negativa** (5) - Esta sección se mostrará en un informe de retenciones solo en caso de que el importe neto del impuesto calculado (sección de Ingresos fiscales (4)) sea = 0; por lo tanto, esta sección solo tendrá un "parámetro de salida" basado en el valor de ingresos fiscales.

6. **Declaración complementaria** (6) - Esta sección se mostrará en un informe de retenciones solo en caso de que el informe de impuestos que se esté lanzando sea un informe de impuestos complementario a uno o más informes de impuestos ya presentados ante las autoridades fiscales por el mismo concepto y para el mismo periodo.

* Esos datos se consideran **parámetros del informe de impuestos** para ese grupo de informe de impuestos específico; por lo tanto, Peter tendrá que navegar a la solapa de parámetros del informe de impuestos y comprobar que los parámetros correspondientes están ahí en caso de que necesite crear un informe de impuestos complementario.

* La sección de Declaración complementaria tendrá **"parámetros de entrada"** que debe introducir el usuario, como "Código electrónico del informe de impuestos anterior".

7. y **Firma** (7). Esta sección contendrá la firma del retenedor/declarador (empresa), que solo es necesaria en caso de formato impreso, no al generar un formato electrónico; por lo tanto, no es necesario que creemos este grupo de informe de impuestos.

!!! info
    Los informes de impuestos de IVA no tienen ese tipo de secciones anteriores porque no son informes de impuestos como tales, sino informes fiscales de extracto; por lo tanto, deberá crearse un grupo fiscal genérico vinculado a un parámetro genérico de informe de impuestos de salida relacionado con el parámetro de código de transacción, para ese tipo de informes de impuestos de IVA.
### Salida del informe de impuestos

Los informes de impuestos pueden presentarse ante las autoridades fiscales como archivos *.pdf, lo que significa un formato impreso, o como archivos *.txt, lo que significa una presentación electrónica que puede enviarse a las autoridades fiscales por Internet. Ambos formatos deben cumplir los requisitos bien conocidos de las autoridades fiscales, por lo que, tras obtener los archivos de salida correspondientes, Peter tendrá que verificar que los formatos son los correctos.

Además, los archivos *.txt pueden presentarse ante las autoridades fiscales utilizando las aplicaciones web de las autoridades fiscales, por lo que Peter debe asegurarse de obtener la certificación fiscal correspondiente requerida para presentar los archivos, así como de que los archivos no sean rechazados.

Peter también debe tener en cuenta que, en función del número de transacciones que deban incluirse en un informe de impuestos, así como del tamaño de la empresa, el formato de presentación debería ser o bien el formato impreso obligatorio o bien el formato electrónico obligatorio.

Peter tendrá que navegar a Gestión financiera / Contabilidad / Herramientas de análisis / Lanzador de informes de impuestos para obtener las salidas del informe de impuestos.  
Una vez allí, la información que Peter tendrá que introducir como parámetros de entrada es:
- Organización
- Informe de impuestos
- Esquema contable
- Año
- Periodo
- y el nombre del archivo *.txt, por ejemplo, como parámetro de entrada  
Una vez completado lo anterior, Peter puede pulsar "Generar archivo electrónico" para generar el archivo *.txt.

---

Este trabajo es una obra derivada de [Lanzador de informes de impuestos](https://wiki.openbravo.com/wiki/Tax_Report_Launcher/Functional_Documentation){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo), utilizado bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/). Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/) por [Etendo](https://etendo.software){target="_blank"}.