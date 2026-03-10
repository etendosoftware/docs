---
title: Plantillas de Contabilidad
tags:
    - Contabilidad
    - Plantillas
    - Gestión Financiera
    - Configuración
    - Contabilidad
---

# Plantillas de Contabilidad 

:material-menu: `Aplicación` > `Gestión Financiera` > `Contabilidad` > `Configuración` > `Plantillas de Contabilidad`

## Visión general 
 
Las plantillas de contabilidad en Etendo sobrescriben el comportamiento contable predeterminado. Cada plantilla está relacionada con una tabla específica.

Los asientos contables generados por Etendo normalmente necesitan generarse de una forma diferente para cumplir los requisitos legales de un país concreto. Para dar soporte a este tipo de requisitos, Etendo permite sobrescribir el código que genera los asientos contables mediante lo que se denomina Plantillas de Contabilidad. Cada vez que se contabiliza un documento, el motor contable comprueba si existe alguna Plantilla de Contabilidad definida para la tabla asociada o para el documento concreto y la ejecuta en lugar del código predeterminado del Core.
 
!!! warning
    Esta es una funcionalidad potente que debe utilizarse con precaución. El código que genera los asientos contables debe probarse en profundidad antes de desplegarlo en una instancia real.

## Creación de la configuración de la Plantilla de Contabilidad

La clase Java que implementa la generación de los nuevos asientos contables se define en la ventana Plantillas de Contabilidad. La definición es bastante sencilla y solo requiere un nombre, el nombre de la clase Java (que debe estar dentro del paquete Java del módulo) y la tabla para la que el usuario desea sobrescribir sus asientos contables (por ejemplo, C_Invoice para facturas, M_InOut para albaranes de entrada/salida de mercancías, etc.).

![](../../../../../../assets/drive/1QFEgaMk9QRkcpsjLLGOZJNKRJo75LvKr.png)

Esta Plantilla de Contabilidad se asociará posteriormente a las Tablas Activas o a un Documento. Por ello, en este paso es importante definir tantas clases Java como Tablas Activas o Documentos para los que se desee sobrescribir su comportamiento contable.
Por ejemplo, se puede definir una única clase Java para sobrescribir el comportamiento contable de todas las facturas (facturas de venta, facturas de compra, abonos de compra/venta, etc.) o, alternativamente, definir una clase para sobrescribir únicamente los asientos contables de las facturas de compra (factura AP) y mantener el comportamiento predeterminado para el resto de facturas.

### Definición del conjunto de datos

La definición del conjunto de datos es un paso clave en este proceso. Una definición incorrecta del conjunto de datos puede echar a perder todo el trabajo previo, por lo que es importante seguir todas estas consideraciones:

- El conjunto de datos debe pertenecer al módulo de la plantilla de contabilidad.
- Intente evitar caracteres extraños en el nombre del conjunto de datos. Esta cadena se utiliza para generar el nombre del archivo XML que almacena el conjunto de datos.
- El Nivel de Acceso a Datos debe establecerse en Sistema/Cliente, lo que significa que permitimos a los usuarios aplicar la configuración solo a nivel de Cliente (Organización *).
- El indicador Permitir exportación debe estar marcado.
- Dentro de la pestaña Tabla, incluya la tabla AD_CreateFact_template, que es la que almacena la configuración de la Plantilla de Contabilidad.
- La cláusula Where HQL/SQL es un campo importante, ya que permite filtrar los registros que el usuario desea incluir en el conjunto de datos. En el ejemplo se han filtrado todos los registros que están dentro del nombre del paquete Java del módulo. 

![](../../../../../../assets/drive/1stuKmJOwNnsth6RG3HX9tj5_6v3OY83U.png)

La definición del conjunto de datos está lista, por lo que el usuario solo necesita exportarla a un archivo pulsando el botón Exportar datos de referencia. Este proceso consulta las tablas anteriores y obtiene todos los registros que cumplen la cláusula Where HQL/SQL, generando un archivo XML dentro del directorio referencedata/standard del módulo. Como comprobación rápida, este archivo puede abrirse con cualquier editor de texto plano y el usuario puede verificar que contiene varias líneas.
En caso de que el archivo esté vacío, el usuario debe revisar de nuevo la definición del conjunto de datos, especialmente la cláusula Where HQL/SQL utilizada para cada tabla.

#### Prueba del conjunto de datos

La prueba real para asegurar que el conjunto de datos de impuestos es correcto puede realizarse dentro de la instancia de desarrollo. La prueba consiste en crear un nuevo cliente ejecutando la Configuración Inicial del Cliente y seleccionando el nuevo conjunto de datos de plantilla de contabilidad de prueba.

![](../../../../../../assets/drive/14yYG4b3onJefyFiz6sV8KlImkfi5ijCf.png)

!!! info
    Si los datos dentro del conjunto de datos son consistentes, el Proceso de Configuración Inicial del Cliente debería completarse correctamente; de lo contrario, fallará mostrando una descripción del error.

 
Tras una Configuración Inicial del Cliente correcta, inicie sesión en el nuevo cliente, vaya a la ventana Plantillas de Contabilidad y compruebe que el registro está ahí.

## Especificación funcional

### Visión general

Actualmente, Etendo construye asientos asociados a documentos siguiendo un comportamiento codificado de forma rígida. Para modificar el asiento generado, debe modificarse el código. El código actual se ha convertido en un módulo llamado core. Si un módulo quiere modificar los asientos contables generados por documentos, debe modificarse core, y esto no es deseable en absoluto.
Con este nuevo desarrollo en core, los módulos podrán modificar fácilmente los asientos generados por cada documento.

### Alcance
El objetivo de este proyecto es permitir que los módulos modifiquen la forma en que se generan los asientos al contabilizar documentos.

### Consideraciones de diseño
Se incluirá una nueva capa entre el documento y la lógica que contabiliza dicho documento. En una nueva ventana, cada documento se asigna al servlet que implementa la lógica para contabilizarlo. De este modo, con solo modificar los valores en esta ventana, se cambia el comportamiento contable. Si un nuevo módulo quiere cambiar el asiento generado al contabilizar una factura, se desarrolla un nuevo servlet siguiendo el comportamiento deseado. Al mismo tiempo, se cambiará la asignación de las facturas al servlet que contabiliza por el servlet desarrollado en el módulo. De este modo, se cambia el comportamiento de toda la aplicación.

### Requisitos funcionales

!!! info
    La Aplicación no se ve afectada por estos desarrollos, porque todos los cambios en la forma en que se contabilizan los documentos son transparentes para el usuario. Solo es necesaria una nueva ventana, que se configura automáticamente para el usuario al actualizar.

---

Este trabajo es una obra derivada de [Plantillas de Contabilidad](https://wiki.openbravo.com/wiki/Projects:Accounting_Templates){target="\_blank"} de [Wiki de Openbravo](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.