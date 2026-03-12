---
title: Cómo crear un módulo que añada un proceso contable
tags: 
    - Cómo hacer
    - Proceso contable
    - Módulo
---
## Introducción

Este módulo no sirve para cambiar los asientos contables generados por Etendo, sino para ejecutar cualquier proceso adicional que deba ejecutarse en el momento de contabilizar.
 
Desde el punto de vista funcional, no existe ningún requisito especial para el desarrollo de este módulo. Solo se recomienda comprender el papel de los [Esquemas contables](../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup/general-ledger-configuration.md) en la configuración contable general de Etendo.

Etendo permite ejecutar procesos justo después de la lógica de contabilización para cualquier documento que se haya completado correctamente. Este tipo de procesos se denominan posprocesos contables porque se ejecutan después del proceso contable normal.

Desde el punto de vista del desarrollo, esta funcionalidad nos ofrece la posibilidad de cubrir cualquier requisito específico de nuestro país, como por ejemplo mantener un registro actualizado de los documentos que se han contabilizado, crear algún tipo de informes oficiales cada vez que se contabiliza un documento, enviar datos a un servicio web, etc.
 
!!! note
    Dependiendo de los requisitos del país, estos posprocesos contables pueden no ser necesarios. Este tipo de módulos no forman parte del núcleo de una localización, como las traducciones, el plan contable o los impuestos, y deben incluirse en una extensión de localización solo en caso de que realmente sean necesarios.

##  Creación de la definición del módulo

Cada vez que se desarrolla un nuevo módulo, el primer paso siempre debe ser crear la definición del módulo y registrarlo en el Repositorio Central.

Estas son las consideraciones especiales para el módulo:

- Intente seguir las [Directrices de nomenclatura para módulos](../../../developer-guide/etendo-classic/concepts/naming-guidelines-for-modules.md)
- Debe marcarse el indicador Has reference data porque el módulo [contendrá un conjunto de datos](#definición-del-conjunto-de-datos) con la configuración del posproceso contable. Recuerde escribir cualquier información útil dentro del campo Reference Data Description.
- Defina la dependencia obligatoria con Core.
- Incluya un DB Prefix para el módulo en caso de que sea necesario. Por ejemplo, el módulo probablemente definirá nuevos mensajes que requerirán un DB Prefix.
- Si el módulo tiene elementos de UI que pueden traducirse (como mensajes), marque la casilla Translation Required y especifique el Module Language necesario.

![](../../../assets/drive/1GUwtOTGd6LoJPGLquBJJrSTsh4jVXiD6.png)

!!! info
    Ahora exporte la base de datos para generar la estructura de archivos dentro de la carpeta del módulo     ant export.database

 
Finalmente, dentro del directorio del paquete java del posproceso contable del módulo, cree la carpeta src, donde se almacena la clase Java que implementa el código del posproceso contable.

  ![](../../../assets/drive/18i01Ilr0UNLViWoeUAbrJy_qcRhE6koC.png)

## Creación de la configuración del posproceso contable
  
La clase Java que implementa la lógica del posproceso contable se define en la ventana Accounting Process. La definición es bastante sencilla y solo requiere un nombre y el nombre de la clase Java, que debe estar dentro del paquete java del módulo.

![](../../../assets/drive/1gzkW_cziu4nYBGnOqLo3LFoHNupaFH0N.png)

Este posproceso contable se asociará posteriormente a un esquema contable. Por lo tanto, en este paso es importante definir tantas clases Java como posprocesos contables queramos incluir en nuestro módulo, aunque normalmente se recomienda incluir solo un proceso por módulo para mantener la regla general de aislar funcionalidades en módulos separados.
 
### Definición del conjunto de datos
  
La definición del conjunto de datos es un paso clave en este proceso. Una definición incorrecta del conjunto de datos puede echar a perder todo el trabajo anterior, por lo que es importante seguir todas estas consideraciones:

- El conjunto de datos debe pertenecer a su módulo de posproceso contable.
- Intente evitar caracteres extraños en el nombre del conjunto de datos. Esta cadena se utiliza para generar el nombre del archivo XML que almacena el conjunto de datos.
- El Data Access Level debe establecerse en System/Client, lo que significa que permitimos a los usuarios aplicar la configuración solo a nivel de Cliente (Organización *).
- Debe marcarse el indicador Export allowed.
- Dentro de la solapa Table debemos incluir la tabla AD_AcctProcess, que es la que almacena la configuración del proceso contable.
- La cláusula HQL/SQL Where es un campo importante, porque permite filtrar los registros necesarios para incluirlos en el conjunto de datos. En el ejemplo se filtran todos los registros que están dentro del nombre del paquete java de nuestro módulo.

![](../../../assets/drive/1J7nXqk7o0-CB9aE7fPpvs23PoB8HJD4J.png)

La definición del conjunto de datos está lista, por lo que el usuario solo necesita exportarla a un archivo pulsando el botón Export Reference Data. Este proceso consulta las tablas anteriores y obtiene todos los registros que cumplen la cláusula HQL/SQL Where, generando un archivo XML dentro del directorio referencedata/standard del módulo. Como comprobación rápida, este archivo puede abrirse con cualquier editor de texto plano y el usuario puede verificar que contiene varias líneas.
  
!!! info
    En caso de que el archivo esté vacío, el usuario debe revisar de nuevo la definición del conjunto de datos, especialmente la cláusula HQL/SQL Where utilizada para cada tabla. 

---

Este trabajo es una obra derivada de [Guías prácticas](https://wiki.openbravo.com/wiki/Category:HowTo){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.