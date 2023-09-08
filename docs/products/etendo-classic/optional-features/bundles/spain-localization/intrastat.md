---
title: Intrastat
hide:
    - navigation
---

## Javapakages 
`org.openbravo.module.intrastat` <br>
`org.openbravo.module.intrastat.spain` <br>
`org.openbravo.module.intrastat.es.es`

## Introducción

Esta sección describe el módulo disponible de Etendo para la generación y presentación del informe oficial de Intrastat.

El informe Intrastat se debe presentar a las autoridades mensualmente, dentro de los 12 días posteriores al mes en el que se realizaron las transacciones.

La declaración de Intrastat se debe enviar telemáticamente (a través Internet) en un fichero válido con un determinado formato específico de cada país.

## Descripción de los Módulos

A continuación, se listan los diferentes **módulos** sobre los que se desarrolla la funcionalidad de Intrastat:

-   **Intrastat.** Este módulo proporciona la infraestructura necesaria que permite la configuración, ejecución y generación del fichero de Intrastat. Si sólo instala este módulo, Etendo será capaz de reconocer todas las transacciones que formarán parte del fichero de Intrastat.

Éste es un módulo del que dependen el resto de módulos de Intrastat, proporciona la funcionalidad genérica para los países de la Unión Europea. Sin embargo, tenga en cuenta que cada país de la UE tiene sus propias peculiaridades, y este módulo es incapaz de conocerlas y manejarlas él sólo. Por este motivo, es posible que necesite instalar además el módulo de Intrastat concreto para su país, que será el que proporcione las peculiaridades propias de su país.

-   **Intrastat for Spain (Intrastat para España).** Este módulo complementa al módulo anterior y proporciona las características específicas para España, como por ejemplo:
    -   Excluye las transacciones que tienen como origen o destino las Islas Canarias (como requiere la ley)
    -   Genera un fichero de Intrastat con el formato oficial listo para ser enviado mensualmente a las Autoridades.
-   **Intrastat – Spanish Translation (Intrastat - Traducción al español).** Añade la traducción al español (España) del módulo Intrastat.

Además de los módulos anteriores, necesitará instalar las siguientes dependencias obligatorias:

-   **Incoterms.** Añade la lista de Incoterms oficiales (Condiciones de Entrega) a su instalación de Etendo
-   **European Union Countries.** Añade la lista de países miembros de la Unión Europea a su instalación de Etendo
-   **Provincias de España.** Añade la lista de provincias españolas a su instalación de Etendo

Todas estas dependencias se instalarán automáticamente al instalar los módulos de Intrastat, por lo que no tendrá que hacerse manualmente.

## **Instalación de los módulos**

Para la instalación del módulo “Modelo AEAT 349 - Declaración recapitulativa de operaciones intracomunitarias”, el usuario debe seguir los pasos que se describen a continuación en función de la situación de partida:

-   Instalación de la última versión disponible de Etendo
-   o la instalación del módulo de Localización Española.

!!! info
    Para la instalación del módulo de Localización Española, visite [*Marketplace*](https://marketplace.etendo.cloud/#/product-details?module=003B475055DD421B9483B5BE15AA48C5){target="_blank"}. 


!!! info
    **Nota importante**: Las transacciones realizadas con anterioridad a la instalación del módulo *“Intrastat”* no se tendrán en cuenta a la hora de generar las declaraciones de Intrastat.


Tenga en cuenta que, como es lógico, el sistema solo es capaz de reconocer las transacciones a incluir en el informe de Intrastat desde el momento que se instala y configura dicha funcionalidad en Etendo.

### **Aplicación de los Datasets (Conjuntos de datos)**

Una vez instalado el módulo, se deberán aplicar los datasets incluidos a su instalación.

Si está realizando la configuración inicial de Etendo, puede utilizar el proceso “Crear Organización” para aplicar estos datos.

Si, por el contrario, está instalando estos módulos en un sistema en productivo, deberá aplicar los datasets desde la ventana Configuración General | Organización | Gestión del módulo de Empresa  |  Gestión del módulo de Empresa:

![](/assets/drive/9E8pdSDAB1cQjG039Rhp_c3Z-XDg2LC-1tnuokHzaQ6MVZ1TTuM5YTyX1q0-wYHGGRAH0OtCyMQ6uICIwQHcHfwz7sBTqVtvAKlc6SSyZGiCuCAJhZ8bsQt9m3qLT4Eiw3mR4XSTNY01hZtqqw9IwQKG9zaQzBnRd89An6VyGUsO7DNXkQl1Q19l9A.png)

Seleccione los datos de referencia “Incoterms” e “Intrastat for Spain” y aplíquelos a su organización de nivel de agrupación o a su entidad legal dependiendo de su árbol de organizaciones.

Si el proceso se ha ejecutado correctamente, el sistema debería mostrar la siguiente información:

![](/assets/drive/WFgwGX-k5cQwljyb0pvetphDd1B4qebt3L2mRNX9o2MhfjH5nTqVpG9O4TUCMwn6NJ1cK1bfQhtosDVfnjno3suZce-SgBk9JC9aZgaRntutQfEf7cc5GLPaBmCSu_L29LYfA3n-g6DMfo8M-NnfKSZnQ8TDR6o3VoM1Y9W75yEjs4v_2POlWyUEpA.png)

## **Interfaz de Usuario**

El módulo “Intrastat” proporciona campos, ventanas y solapas necesarios para la configuración y generación de la declaración de Intrastat.

A continuación se muestran unas capturas de pantalla de estos elementos junto a una breve descripción de cada uno de ellos.

###### **Gestión de Datos Maestros | Producto  |  Producto  >>  Intrastat**

![](/assets/drive/G5Llm2flNrOzJt-k1_SvtgklRXnnQtgz0wyBL4ouCXVxOoe30GaKqSgN5KgrXlgH21xq0_T0EUyZlwpaGQgjhcLP8cpt1HqqiAK9EGzkjzgcObg1bTkeIMUdoTtcM7WbTd0oTcgVEi4iAQdWhJ76AyrmUSnh2bw8Zo0tU15gL3AYtIFQr1wMBybNXA.png)

Las transacciones entre países de la UE que incluyan productos de tipo Artículo se deben registrar en la declaración de Intrastat. Cada uno de los productos tiene asociado un código de mercancía obligatorio y una masa neta en Kg (por unidad de facturación). Opcionalmente, y siempre dependiendo del producto, se puede configurar una unidad de medida suplementaria junto a su correspondiente conversión.

En esta solapa, el usuario debe configurar los datos particulares de cada producto.

###### **Gestión de Datos Maestros | Terceros  |  Terceros  >>  Cliente  >>  Envíos de Intrastat y Gestión de Datos Maestros | Terceros  | Terceros  >>  Proveedor/Acreedor  >>  Adquisiciones de Intrastat**

![](/assets/drive/7azhjfSW95mKDO_Umt-b50nUiixohLlwZ1zx_oZKMbNAO7R79nOk7oMsT2Rq-iOC-rY16uPaSnyHXz5_5bwULKS1eSqn7bmhL85Um2Qs-f_RNafxL9RFYkcEXvV_l-7QVXpWVGjPDbIghA2hw-mXyPncKMBU1GIqXCrUt8KkoklL6WlVFouQKsXX8A.png)

Cada tercero con el que trabaje, ya sea cliente o proveedor, tendrá su propia configuración para Intrastat por defecto. Por ejemplo, es posible que su proveedor siempre le envíe la mercancía mediante un medio de transporte determinado.

Desde esta solapa el usuario tiene la oportunidad de configurar esos valores por defecto de cada tercero. El sistema siempre recuperará la información configurada aquí y la utilizará para generar la declaración de Intrastat.

Sin embargo, es posible que en alguna transacción en particular, la modalidad de transporte varíe de la que tiene configurada por defecto en esta ventana. Si éste es el caso, el usuario siempre tiene la oportunidad de cambiar manualmente esta información a nivel de transacción o de declaración de Intrastat como veremos más adelante en este manual.

###### **Gestión de Datos Maestros | Terceros  |  Terceros  >>  Cliente y Gestión de Datos Maestros | Terceros  |  Terceros  >>  Proveedor/Acreedor, campo Incoterms**

![](/assets/drive/FxL2ss3KNP9of-xib9m4PqSBvMrXhhFCKBFlFLq06LGNxkxNzb2A0R55NPFpGogVFQ6Zc9ztwL-EjSxQYPAZTkDgpbCN-Unh4iJGItzb1np0W0YBfO6_PiM-PSbp20vpW5T38UEp2vXdogNtyh-osvVMoIUHGJDlSf4HDqNXCsD2YbFUGULEr1gW0A.png)

El campo Incoterms permite definir el Incoterm (Condición de Entrega) por defecto para el tercero. Es importante tener en cuenta que se pueden configurar dos Incoterms para el tercero, uno cuando el tercero es cliente y otro cuando es proveedor.

!!! info
    El campo "Incoterms" del Tercero, es un campo de Etendo que no se muestra por defecto, pero si se utiliza en los módulos de Intrastat. Recuerde mostrarlo si lo va a utilizar.


###### **Gestión Financiera | Contabilidad | Configuración | Tipo de documento  |  Definición de documento**

![](/assets/drive/IoUclg9rhO_Gqhw_0FuLoJa54gQjUysOPDNlGgbwsbczidBrKgSlXDVgV06YLVDXTwMPbgeJ041zklsHvsDQKu0lhSTvKh3uI3TPmCeYv4qY466B-at_lMNxdR24jh40VhYtkBzLxGKGPkQIFVHGJSLZfwjDeImzQu1key6CJmHNBTfZEDth6QQCeg.png)

Los campos *Tipo de Transacción* y *Regimén estadístico* van asociados al tipo de documento (facturas). En esta ventana puede definir los valores por defecto que, al igual que sucedía con los valores de Intrastat para Producto o Tercero, pueden ser sobrescritos para transacciones o declaraciones de Intrastat en concreto.

###### **Configuración General | Organización | Organización | Organización, campo Calendario de Intrastat**

![](/assets/drive/mVJ1pyaJF0A0_AhDbNggeRZnZvxKq2pl9cs7i7n-0TuQfxS-sucLH8Dj83qvRSIDnttYFzgSMZK5LRnWS5n5Wp6liQUUZnaOeJfKjfHFFm7q5eFQ68kpmuLi_V-SI8N2d28S3lOfQfGwc6Rhq-U_RROZKyUL9fmjd9LM_xCuM2H3pzd__651wvaibg.png)

El campo *Calendario de Intrastat* define el calendario de declaraciones de Intrastat. En España, el Intrastat se debe presentar mensualmente, por lo que el calendario de Intrastat seleccionado debe tener doce periodos que coincidan con los dos meses naturales de un año. Si su calendario fiscal cumple esas condiciones, puede usarlo también como calendario de Intrastat sin necesidad de crear uno nuevo.

En este nuevo campo, sólo aparecerán los calendarios que estén marcados como *“Calendario de Intrastat”* en la configuración del calendario:

![](/assets/drive/bO3u93UFfmKU1W9mLFKYj-ZbmYv8cKLtPjLvC-yacQkkRXAfcnGz3HeIrfsjW08XXL8iBOP656gydvYIYVKSIthvyYK8IEsipoh7XADziIBF77qqffJlwOH11cgdPlb0tWT9wCtR11_P3CSWWbkOUracp5Ui3Ul0irS50FTaDLewU1rdVdJ1TEVmMg.png)

###### **Configuración General | Organización | Organización  |  Organización  >>  Intrastat**

![](/assets/drive/C03LX7XPMO-rvqovv8Gtmu6l-HoRmUqQPf0Q321iltU61rfVQyiGCo1dsu6oQ_oFXHLbF0528kEHLoOx8qWAmbJx0NcgwVmw_Iy-lNzSCRXYB4jO9P0zcaOAU44PXqja7AgrdctRRSNeYtErmY50OYAT0RKfFXgrX6lTf20j5WzMnDQexGT1AqaK0g.png)

En esta solapa se introduce la información de Intrastat relativa a la organización (sólo entidades legales).

Cada año se debe introducir un registro en esta solapa para configurar los siguientes datos:

-   *Formato de Fichero*: Cada país tiene su propio formato de Intrastat. En este campo seleccionamos el formato de fichero concreto que queremos que cree el sistema. En el caso de España, el módulo “Intrastat for Spain” es el encargado de generar el fichero con formato para España.
-   *Ejercicio*: Año de la declaración
-   *Declaración de Intrastat*: Adquisiciones o Entregas
-   *Importe Límite*: Cada año las Autoridades suelen modificar el importe que delimita la obligatoriedad de presentar o no la declaración de Intrastat. En este campo el usuario debe indicar el importe límite de cada año.
-   *Importe Acumulado del año*: Cada vez que se presente una declaración mensual, el sistema irá actualizando automáticamente el valor de este campo con el importe acumulado. Si el año anterior se generó la declaración de Intrastat fuera de Etendo, o desea empezar a generar la declaración una vez empezado el año, puede configurar aquí el importe que declaró en su momento.
-   *Valores por Defecto (Incoterms, Tipo de transacción, Modalidad de transporte, Régimen estadístico, Valor estadístico)*: Como ha visto anteriormente, en las ventanas de *Tercero* o *Tipo de documento* se pueden definir todos estos valores. Sin embargo, definir la misma *Modalidad de transporte* (por ejemplo) para todos los terceros puede resultar un poco molesto. Así que, si lo desea, puede definir la configuración global de estos valores en esta solapa. De esta forma, si por ejemplo no especifica nada en la *Modalidad de Transporte* de un Tercero, el sistema utilizará por defecto la configurada en esta solapa. Podrá modificar manualmente esta configuración siempre que lo desee en cada transacción o declaración de Intrastat.

###### **Solapa Intrastat en Línea de Pedido, Albarán y Factura (compra o venta)**

![](/assets/drive/MPXVxD2cgEZhT-sITSN4LLZJV59vTsxYwzj5fC8IKyIZuUjHq8BWShP7aSB5M5vue9kXWhNUL54W0Q7vNGkN1OJvPXInGUWRPOhsSix8csKzNIAYHwIxwxany7JR3xAeifSGeUfUOLCeOoxyR55QMrajFQjcsrPYt5AnOUALpnHeh82pH3O9mGbIKg.png)

A nivel de línea de Pedido, Albarán y Factura, tanto de compra como de venta, se ha creado una nueva solapa que contiene toda la información de Intrastat relativa a esa transacción en concreto.

Cada vez que se introduce una nueva línea de pedido, albarán o factura, el sistema comprueba si esa transacción se debe incluir en el informe de Intrastat (por ejemplo, si se trata de una compra/venta intracomunitaria) y, en caso afirmativo, genera un registro en la pestaña Intrastat con toda la información de Intrastat que se ha configurado por defecto. El usuario puede modificar manualmente cada uno de esos campos antes de completar el documento.

La razón por la que se ha añadido una solapa de Intrastat tanto en las líneas de pedido como de albarán (teniendo en cuenta que estos documentos no se incluyen en el Intrastat, sino sólo las facturas contabilizadas) es que las facturas en Etendo pueden crearse desde los pedidos y/o los albaranes. Es por ello que si la información relativa a Intrastat se introduce en la línea de un pedido, esa información se trasladará a la correspondiente línea de factura si la factura se genera copiando del pedido.

###### **Intrastat | Herramientas de análisis | Generador de Intrastat**

![](/assets/drive/XxYQ02-DL0rr3DGMZ_FUOn2gVmqY34Iko4NBU_Wr7JXNbchAgTSr_BaLU_6bf9giEwaUVf8c2b2pvk2dc2U6NwRsa7CX8uFXET_eiMgxybpB8swm-0wSw9ln1r_FcRFaFlYvumc30KMLbEhCxNLFPy7NfCiPVYvY41yrCbbhVWZ75HgRrxwNyEYkdg.png)

Una vez finalizado el mes, se debe generar la declaración de Intrastat de ese mes. Desde esta ventana podremos hacerlo. Para ello seleccionamos la Organización (sólo entidades legales), Ejercicio, Periodo, Adquisiciones o Entregas y Tipo de declaración (Normal o Anulativa).

El sistema generará automáticamente una cabecera de declaración junto a sus líneas, accesible desde Intrastat | Herramientas de análisis | Declaración de Intrastat.

###### **Intrastat | Herramientas de análisis | Declaración de Intrastat**

![](/assets/drive/er07E5V7YGKLkaVl1A9lUzWMFj3FREeBMgFaqnjtq6fB2w7ek7q6ztujPw2KNRxtVq45PS7SU6MzaKmrNSdDnNXw6nkGRo0s_Y1aY0KKEyigXKHj9w8_RqGCSKo-Hj3AiqoUKo2sNu19GNJ6xTBoUMHzLYDpfMVL8JcyS1evqol-e3m-weEBCbbB5Q.png)

Al generar una declaración de Intrastat, el sistema crea automáticamente una nueva cabecera (sólo lectura) junto con sus líneas. En este momento la declaración se encuentra en estado borrador, y se permiten modificaciones en las líneas de la declaración. Veamos un ejemplo de la información que contiene una línea:

![](/assets/drive/04R4qED5tjzLbOS_oOdZGSssalCSrO5HjgBFbLPHotJgoHxVqKwB7MzSAGUN9sqiJdzB78R9LBKGA0J8pTtaXgOGJBcI3BzfQoyEXdg3dwLXaDTNG7aqfe6JSU_KAgeVjCkHNZO5kvKhJ5DzooSFsIYSd-hZs3KfJMCSH54KXzVfiXilrW02m280dQ.png)

El sistema ha recuperado toda la información de Intrastat desde las líneas de factura. Si ha configurado toda la información relativa al Tercero, Producto y tipo de documento, el ERP habrá rellenado automáticamente todos estos valores en las líneas de la declaración.

Si por el contrario le falta algún dato, si desea modificar alguno, o incluso si quiere añadir manualmente nuevas líneas o excluir alguna de ellas, puede hacerlo mientras la declaración esté en estado borrador.

En la solapa de líneas de declaración de Intrastat, al margen de los campos relativos a la información de Intrastat, aparecen dos campos de especial importancia para el usuario: el campo *“Incluir”* y el campo *“Modificado Manualmente”:*

-   *Incluir*: Por defecto, todas las líneas de la declaración de Intrastat se incluirán a la hora de generar el fichero de Intrastat. Sin embargo, si desmarca esta casilla, la línea en cuestión se excluirá de la declaración.
-   *Modificado Manualmente*: Cada vez que se modifique un dato de una línea de declaración de Intrastat o añada manualmente una nueva línea, el sistema marcará automáticamente esta casilla.

Mientras la declaración está en estado borrador, la declaración de Intrastat se puede relanzar todo lo necesario. Cuando se haga, el sistema volverá a recalcular de nuevo la declaración, conservando intactas todas las líneas que tengan marcado el campo de *Modificado Manualmente.*

## **Manual de Instrucciones**

Una vez que conoce las ventanas más importantes que proporcionan la funcionalidad de Intrastat en Etendo, es hora de conocer el flujo de trabajo para usar correctamente dicha funcionalidad.

### **Configuración General**

Toda la lógica detrás de la funcionalidad de Intrastat en Etendo se basa en la ubicación física de su organización y de sus terceros. Por ese motivo es fundamental que especifique la dirección completa de cada uno de ellos. Si la dirección es de España, deberá indicar también la Provincia en la que se ubica.

#### **Configuración de Intrastat**

Como habrá podido observar, la configuración para Intrastat se realiza principalmente en los siguientes lugares:

-   **Configuración General | Organización | Organización**. Para cada entidad legal, deberá seleccionar un calendario válido para Intrastat (que tenga ejercicios con 12 periodos que coincidan con los meses naturales). Recuerde marcar la casilla “Calendario de Intrastat” cuando configure su calendario (*Gestión Financiera | Contabilidad | Configuración | Calendario anual y periodos*) para que éste aparezca en el campo de *Calendario de Intrastat* de la ventana de Organización.
-   **Configuración General | Organización | Organización  |**  Organización  **\>>  Intrastat**. Recuerde que en esta solapa se configuran:
-   Los importes y tipos de declaraciones que desea generar para cada entidad legal
-   Los valores por defecto globales que se utilizarán en caso de que no se definan concretamente donde corresponda (*Tercero* o *Tipo de documento*)

El sistema necesita saber cuánto se declaró el año anterior. Para proporcionar esta información, se debe crear un nuevo registro en esta solapa. Solamente a modo de ejemplo, en *2021* para la organización *España*, declaramos un Intrastat de *adquisiciones* por un importe de *0.00* Euros:

![](/assets/drive/9X5udGu8RP0DTGJquv2Li6dXdSXPxg03D1QBGQ6qnrs6VxCayvbcoqtu-IyOzhhT5L2lb7CWeHMST-gvve1CpWU8RyBTrUcgu-CIGup0h6kG9MrY0-DbIZ-LQIrMrLttuy0FAM3Ax2-CPquZMG8IOmqkZGLr6bl1mhCpSe2_IErNZTQfX5RfnIIrfg.png)

!!! info
    Nota: Si su calendario de Intrastat no tiene creado el año 2021, deberá crearlo (junto a sus respectivos periodos) antes de poder introducir este registro.


Ahora repita ese proceso para el año presente. Si ya ha empezado el año y se han realizado transacciones intracomunitarias de bienes (presentando o no la declaración de Intrastat), deberá indicar el importe acumulado de este año. De esta forma, el sistema podrá saber si debe presentar la declaración de Intrastat o no a lo largo del presente año.

También existe la opción de configurar los valores globales por defecto, lo que es especialmente útil si, por ejemplo, casi todos sus Terceros comparten el mismo Incoterm. Posteriormente, a nivel de tercero, se podrá especificar la configuración concreta para cada uno de ellos.

![](/assets/drive/oVnu7ahLXMceKTVmUBhewKFKYODlv-fRnLLXvLdTrg6rsJdYzXk9_nRSj9_6COfueYVEub-2ISJZV49Abl1WRLhdVqzJ5DCV5n0d3vMDePDlcYKGY6pUDeQSSSrpRz6k--F-438sLk7NF_QCydiwA2C2X6nWOSbZ5u0D0Zn7UyfdJsZm1IRoRMPjAQ.png)

-   **Gestión de Datos Maestros | Producto  |**  Producto  **\>>  Intrastat** Como ya vió en el apartado Interface de Usuario, debe definir la información de Intrastat para los productos de tipo *Artículo.*
-   **Gestión de Datos Maestros | Terceros  |**  Terceros  **\>>  Cliente y Gestión de Datos Maestros | Terceros  |**  Terceros  **\>>  Proveedor/Acreedor, campo Incoterms.** Como ya se vió en el apartado Interfaz de Usuario, se puede definir el Incoterm de cada Tercero.
-   **Gestión de Datos Maestros | Terceros  |**  Terceros  **\>>**  Cliente  **\>>  Envíos de Intrastat y Gestión de Datos Maestros | Terceros  |**  Terceros  **\>>**  Proveedor/Acreedor  **\>>  Adquisiciones de Intrastat .** Como ya se vió en el apartado Interfaz de Usuario, se puede definir la información de Intrastat de cada Tercero.
-   **Gestión Financiera | Contabilidad | Configuración | Tipo de documento  |  Definición de documento.** Como ya se vió en el apartado Interfaz de Usuario, puede definir el *Tipo de Transacción* y *Régimen estadístico* para sus documentos de tipo Factura.

### **Creación de transacciones**

Una vez que nuestros datos están perfectamente configurados, es el momento de empezar a crear las transacciones que posteriormente se incluirán en la declaración de Intrastat.

Como ya se ha visto en apartados anteriores, su instalación cuenta con una nueva solapa, llamada *“Intrastat”*, a nivel de línea de pedido, albarán y factura que contiene toda la información relativa al Intrastat. Si se han introducido todos los datos de configuración necesarios anteriormente, se utilizará esta información automáticamente para rellenar esa solapa. Si, por el contrario, no se ha configurado toda esta información, o desea modificar algún dato en concreto, podrá hacerlo de forma manual.

Cada vez que se introduce una línea de pedido, albarán o factura, el sistema comprueba si se cumplen todas estas condiciones:

1.  La organización y el tercero del documento se encuentran en países distintos de la Unión Europea
2.  Todas las direcciones incluidas en la cabecera del documento, que están relacionadas con el tercero, están ubicadas en la UE. Si al menos una de las direcciones no pertenece a la UE, no se generará información de Intrastat
3.  El producto incluido en la línea es un artículo
4.  Si se ha instalado el módulo de *“Intrastat for Spain”*, el sistema también comprobará que tercero y organización no se encuentren ubicados en las Islas Canarias, ya que en este caso las transacciones se deben excluir del Intrastat.

Si todas esas condiciones se cumplen, cada vez que inserte una línea de documento, el sistema creará automáticamente la información en la pestaña de Intrastat.

El sistema recupera los valores por defecto que haya configurado a nivel de tercero, producto, tipo de documento y organización (este último si no encuentra los valores correspondientes anteriormente). Pero recuerde que, independientemente de los valores configurados, el usuario tiene la libertad de modificarlos para cada línea en concreto mientras el documento no se haya completado.

#### **Creación de transacciones desde otras transacciones**

En Etendo existe la posibilidad de crear albaranes desde pedidos; en este caso, el sistema recuperará la información de Intrastat introducida a nivel de pedido y la copiará al albarán.

Imagine que ha creado un pedido y que ha cambiado el Incoterm por defecto. Cuando se cree un albarán desde ese pedido, el Incoterm que se incluirá en la línea de Intrastat del albarán será el que se haya redefinido en el pedido, y no el que estuviera configurado en el sistema por defecto.

Lo mismo sucede para las facturas. En Etendo se pueden crear facturas desde albaranes o pedidos. En este caso, el sistema siempre intentará recuperar la información de Intrastat del albarán o del pedido. Si la factura se crea sin albarán o pedido asociado, Etendo recuperará la configuración del sistema para rellenar la solapa del Intrastat.

### **Generación de declaraciones de Intrastat**

Una vez finalizado el mes natural, llega el momento de generar la declaración de Intrastat. Para hacerlo debemos ir a la ventana Intrastat | Herramientas de análisis | Generador de Intrastat. Seleccionaremos la entidad legal, año, periodo y tipo de declaración.

![](/assets/drive/-xOOy1tCY12Yc8KLtr_QEIiGwyUIQ8O9dXuGoMTnHHhDwYTKty5cP1dog-im2f-iHQoE-UEbMJcoseuQvPEnMqTTwZvEEwMyHin7jQyDByPcGvhswO9pAz2e07LqRCkFPWXTXlMJEwr09pCoiupjWHCQLHRcPRdjgZhysMOmd4ZvJbmmRELeLdO7gg.png)

Actualmente, Etendo soporta dos tipos de declaraciones: *Normales* y *Anulativas*, estas últimas anulan las declaraciones normales procesadas en el periodo seleccionado y generan una nueva declaración normal.

Tenga en cuenta que un mismo periodo sólo puede tener como máximo una declaración normal para adquisiciones y otra para entregas.

Mientras la declaración normal para un periodo se encuentre en estado borrador, el usuario puede lanzar la generación de la declaración tantas veces como quiera. El sistema actualizará todas las líneas de la declaración, conservando todos los cambios manuales realizados por el usuario.

Como veremos más adelante, cuando se procese una declaración ya no se podrá realizar más cambios sobre ella. Sin embargo, el usuario siempre puede anular la declaración procesada para volver a generar una nueva declaración normal para ese periodo.

!!! info
    **Nota importante:** Etendo recomienda cerrar el periodo contable antes de generar la declaración de Intrastat.


#### **Revisión, Modificación y Procesado de la declaración de Intrastat**

Una vez generada la declaración, podemos examinarla antes de procesarla. Para ello utilizaremos la ventana Intrastat | Herramientas de análisis | Declaración de Intrastat. La cabecera de la declaración se encuentra por defecto en estado borrador, con todos los campos de solo lectura.

Si navegamos a las líneas, podemos comprobar los datos que se incluirán en la declaración. Mientras la declaración esté en borrador, podremos modificar datos de las líneas, incluir manualmente nuevas líneas (para transacciones al margen de Etendo), o excluir líneas (mediante el campo *Incluir*) que no queramos que aparezcan en el fichero de Intrastat.


Cuando estemos seguros de que la declaración es correcta, navegaremos a la cabecera y pulsaremos el botón *“Procesar Declaración”.* Este proceso comprobará que todos los datos necesarios para generar el fichero de Intrastat están en el sistema y nos mostrará un error detallado en caso de que encuentre algún fallo. Ejemplo:

![](/assets/drive/YmqOUWlEagUpEcF7v1V8AbomnzuIy8PSzX0CHXiNQTThWHi821JdV-yVpHHydVZOZbxkF1ybQSff-K0KbKoaGSgYekcjm2ofbGreyprdx482TGdM8m4S-076wHnQt16isDz4Vn-gSMkN2Q5qEft7hRWTILjXA2NWVp2G7bVxcmzeCxVVxcfB7Bal7Q.png)

Una vez procesada la declaración, el campo *“Importe Acumulado del año”* a nivel de organización se actualizará automáticamente, sumando el importe de esta declaración a lo acumulado en el año. Si posteriormente anula esta declaración, el sistema restará el importe de la declaración anulada al acumulado del año.

### **Generación del fichero de Intrastat**

Al procesar la declaración, aparece automáticamente el botón de “Generar fichero”.

![](/assets/drive/qZnZAQ6qT2iKqwv_ZgjHxgD_ytT0UxvLoevWs3yIh-DMPFriliEcja2bxMfH3znnY9CkX0Dvzw80Z99vu-3jyD_vSjaqb8Hds-METiaoAqj7KWg5WzgJq2u8FJ5qg2yBrBTlM20qrC_8jDo03XDeametjvbJwchZo4gBISB7-1D6NEtn8k3cp4hVDA.png)

Cuando lo pulsemos, el sistema comprobará si estamos obligados a presentar la declaración para este periodo o no. Para llevar a cabo esta operación, el sistema comprueba el importe declarado el año anterior y el acumulado de este año, por ese motivo es muy importante que configure correctamente estos valores en la ventana Intrastat a nivel de Organización.


Si durante el año anterior superamos el límite de declaración de Intrastat, o lo hemos superado a lo largo del presente año, Etendo nos generará el fichero de Intrastat con el formato apropiado para ser enviado telemáticamente (a través de Internet) a las Autoridades. Ejemplo:

FR;31;FOB;11;3;;85182190;CN;1;115;162;15,37;15,37

DE;28;CIF;11;1;0811;85182190;US;1;2459;1982;4589,46;4589,46

IT;12;FOB;11;3;;02012030;;1;800;;987,00;890,45
!!! info
    Si las líneas de la declaración sobre la que vamos a generar el fichero son superiores a 1000, generará un fichero zip con tantos txt como sean necesarios, ya que cada archivo podrá contener un máximo de 1000 líneas.

!!! info
    Este fichero se puede importar en el enlace web de la AEAT - Cumplimentación en Línea con Importación de Fichero. Para más información, consulte este [*enlace*](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/procedimiento-presentacion-declaraciones-intrastat.html){target="_blank"}.


!!! info
    Es importante recalcar que superado el umbral de presentación en caso de que en un periodo (mes) no se realicen transacciones de intercambio de bienes intracomunitarias, habrá que presentar la correspondiente declaración sin transacciones. 



#### **Finalizar el año. Copia de configuración al siguiente año**

Una vez que hemos generado todas las declaraciones del año, es momento de configurar el sistema para el próximo año. Lo único que debe hacer es ir a la configuración del presente año en Configuración General | Organización | Organización  |  Organización\]  >>  Intrastat y presionar el botón *“Copiar al año siguiente”.* En la ventana emergente aparecerá un campo numérico para que introduzca el nuevo importe límite del siguiente año.

![](/assets/drive/QeFYekMn3a3rRGcEFIkw2MgQ2UNf5EfrCuJM8iaLCP6WqeyL6-0HRqUgzimJiyEkn-vT6XRvDUsNkw2VhlJYRdoo5kgTPOdCa5r1EnNBj8k6CQ45xq-7R2LS4b0Yn8MwpQ2cgLoWrgeZYvCn9NhJNoIFNt6ZuzvNE82NJDn7JL4TtbIoU-OuQWHm4Q.png)

El proceso comprobará que haya procesado todas las declaraciones del presente año y, en ese caso, creará un nuevo registro copiando toda la información de configuración del presente año junto al nuevo importe límite de declaración de Intrastat.