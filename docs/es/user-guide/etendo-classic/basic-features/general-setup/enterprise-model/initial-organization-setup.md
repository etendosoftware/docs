---
title: Crear organización
tags:
    - Organización
    - Configuración
    - Entidad
    - Enterprise
    - Model
---

# Crear organización

:material-menu: `Aplicación` > `Configuración General` > `Organización` > `Crear organización`

## Visión general

Una **Organización** es una empresa de una entidad. Una entidad puede tener al menos una o incluso más de una organización como forma de configurar diferentes tipos de modelos empresariales.

En general, las organizaciones pueden ser:

- entidades legales independientes con un NIF diferente
- grupos empresariales con el objetivo de obtener cifras agregadas para el grupo
- o áreas de negocio de la entidad, como departamentos

Además, las organizaciones pueden estructurarse:

- por **país o región**
- por **área o función**
- y así sucesivamente, según las necesidades del modelo empresarial.

Todo lo anterior proporciona una visión de los diferentes escenarios que deben cubrirse al modelar la empresa.

- Podría haber organizaciones que necesiten compartir datos maestros como terceros y productos, manteniendo su propio plan contable, impuestos, informes financieros y datos transaccionales. Ese podría ser el caso de entidades legales independientes que pertenecen al mismo grupo empresarial.

- Podría haber organizaciones que compartan datos maestros e incluso el mismo plan contable. Ese podría ser el caso de divisiones o departamentos dentro de la misma entidad legal independiente.

- Podría haber organizaciones creadas con el objetivo de solo agrupar datos, para las cuales no se requieren datos transaccionales propios.

Todo lo anterior es posible debido a que existen diferentes [tipos de Organizaciones](../enterprise-model/organization-type.md) y, además, las organizaciones pueden estructurarse de forma jerárquica:

- En el nivel más alto del árbol, existe una organización denominada (\*).
    - La organización (\*) se crea al mismo tiempo que se crea la _entidad del sistema_, y se comparte entre las diferentes _entidades_ del sistema.
    - Los datos maestros creados a nivel de la organización (\*) son accesibles para todas las organizaciones por debajo de ella.
    - La organización (\*) no es una entidad legal independiente, por lo tanto no se permiten datos transaccionales.
    - Toda organización creada posteriormente se creará por debajo de la organización (\*).
- En un nivel inferior del árbol, puede haber organización/es padre que pueden tener organización/es hija por debajo.
    - Los datos maestros como terceros y productos creados a nivel de la organización padre son accesibles para todas las organizaciones hija por debajo.
- En el nivel más bajo del árbol, puede haber organización/es hija sin organizaciones por debajo.
    - Los datos maestros como terceros y productos creados a nivel de la organización hija no serán accesibles para el resto de organizaciones hija, si las hubiera.

## Crear organización

Como ya se ha mencionado, las Organizaciones se crean ejecutando el proceso Crear organización y, además, una vez creada una organización debe establecerse como **Lista** en la ventana Organización.

![](../../../../../assets/drive/jaLNPOFQoCLMgujXvhC3sL--3PKbCLcfdvQubK5VvyRy85PwL7t_4V38fCTBCmrioEfhBQKvWWVq87sbLZsuP9D-YMUodiBeLsQrhbY-cnruPAjkkigHou5kknI1D0ZYc4-G0RiB.png)

Como se muestra en la imagen anterior, una organización puede crearse proporcionando los datos relevantes a continuación:

- el nombre de la organización
- el nombre del usuario de la organización
    - Etendo crea un nuevo usuario y un nuevo rol que solo tiene acceso a la organización recién creada.
        - Este usuario puede modificarse posteriormente asignándole nuevos roles.
        - Y el rol también puede modificarse posteriormente asignándole nuevas organizaciones.
- el tipo de organización. Las opciones disponibles son:
    - Organización - una organización que no es una entidad legal y no permite la introducción de datos transaccionales.
        - Este tipo de organización permite la creación y configuración de datos maestros para ser compartidos entre un grupo de organizaciones de cualquier tipo que pertenezcan a ella, por ejemplo Terceros, Plan contable, etc.
        - No requiere libro mayor, ya que no permite introducir transacciones, pero puede tener una configuración de Libro mayor determinada para ser compartida entre las organizaciones por debajo.
        - Los periodos contables no pueden abrirse y cerrarse de forma independiente a su nivel.
        - Y puede haber tantas organizaciones de tipo **Organización** en una rama como sea necesario.
    - Legal con contabilidad - una entidad legal independiente con un NIF único que requiere contabilidad, por lo tanto:
        - Esta organización requiere un Libro mayor y, por tanto, un Árbol de cuentas o Plan contable, así como un Calendario fiscal, ya que los periodos contables pueden y deben abrirse y cerrarse a su nivel.
        - Este tipo de organización permite la **consolidación** del Balance de situación y de los informes de PyG solo para el Plan contable que tenga asignado.
        - Se permiten transacciones para este tipo de organización.
        - Y, por último, solo puede haber una entidad legal por rama del árbol; por lo tanto, las organizaciones por debajo heredan la configuración del Libro mayor y el Calendario fiscal de la organización legal con contabilidad.
    - Legal sin contabilidad - una entidad legal independiente con un NIF único que no requiere contabilidad porque se gestiona en un sistema separado, por lo tanto:
        - Este tipo de organización no necesita un libro mayor ni un plan contable y no admitirá informes financieros a su nivel.
        - Se permiten transacciones para este tipo de organización. Transacciones que no se contabilizarán en el libro mayor.
        - No puede tener otra entidad legal en un nivel superior/inferior de la estructura del árbol empresarial.
    - Genérica - una organización que no es una entidad legal, pero debe pertenecer a una entidad legal situada en un nivel superior en la estructura del árbol de organizaciones. Por ejemplo, departamentos o divisiones dentro de una organización o entidad legal.
        - Puede haber tantas organizaciones genéricas como sea necesario por rama del árbol, pero siempre bajo una entidad legal.
        - Este tipo de organización permite la introducción de datos transaccionales, puede tener su propia configuración de libro mayor y puede heredar la configuración del libro mayor de la entidad legal con contabilidad a la que pertenece.
        - Los periodos contables no pueden abrirse y cerrarse de forma independiente a su nivel.
- la organización padre. Al crear una organización, es posible seleccionar la organización a la que pertenecerá la organización que se está creando. La organización padre deberá estar establecida como **Sumario**.
    - Una organización genérica no puede ser la organización padre de una organización de entidad legal, pero sí al revés.
- la ubicación/dirección de la organización
- y la moneda de la organización

Además:

- Existe una casilla de verificación denominada **Incluir contabilidad** que permite al usuario seleccionar para una organización:
    - un archivo CSV de contabilidad en el campo **Archivo de contabilidad**
    - o datos de referencia de un módulo de Plan contable en la sección **Datos de referencia**. Los datos de referencia procedentes de módulos de extensiones son datos maestros como Impuestos, Plan contable, etc., que se aplican desde los módulos ya instalados.

Esta acción crea:

- una configuración de Libro mayor que se vincula automáticamente a la Organización que se está creando
- y un Árbol de cuentas o Plan contable que también se vincula a la Organización que se está creando

Este paso no crea un Calendario fiscal como lo hace el proceso [Crear entidad](../../../../../developer-guide/etendo-classic/how-to-guides/how-to-run-an-initial-client-setup-process.md), porque los Calendarios fiscales deben crearse ad hoc para las Organizaciones **Legal con contabilidad** para las cuales se va a habilitar la funcionalidad **Permitir Control de Periodos**.

!!! note
    Este paso no implica gestionar la contabilidad dentro de una organización, sino únicamente incluir un archivo contable o datos de referencia contables en una organización.

La gestión contable depende del tipo de organización que se esté creando.

No es obligatorio seleccionar la casilla **Incluir contabilidad** al crear, por ejemplo, una organización de entidad legal con contabilidad, porque:

- una entidad legal con contabilidad puede heredar el plan contable de la entidad
- o, posteriormente, tanto el Plan contable como la configuración del Libro mayor pueden crearse manualmente y vincularse a la organización.
- si se selecciona la casilla **Incluir contabilidad**, es posible seleccionar para la organización que se está creando las siguientes dimensiones que se utilizarán al contabilizar los documentos de la organización en el libro mayor:
    - Dimensiones de contabilidad obligatorias como Tercero y Producto, y dimensiones de contabilidad no obligatorias como Proyecto y Región de ventas, al crear una Organización en una entidad que no mantiene centralmente las dimensiones contables.  
    En ese caso, las dimensiones seleccionadas aquí se listarán en la pestaña de dimensiones de la configuración del libro mayor de la organización, por lo tanto estarán disponibles solo para esa organización.
    - Dimensiones de contabilidad adicionales como Proyecto o Campaña al crear una Organización en una entidad que mantiene centralmente las dimensiones contables.  
    Una vez más, las dimensiones seleccionadas aquí se listarán en la pestaña de dimensiones de la configuración del libro mayor de la organización, por lo tanto estarán disponibles solo para esa organización.

Es posible aplicar datos de referencia como:

- Tipos de documento y algoritmo por defecto para el emparejamiento automático de extractos bancarios; esto es similar a lo anterior, pero para flujos financieros específicos como Pagos emitidos, Pagos recibidos y Cuentas financieras.
- o datos de referencia como datos maestros o datos de configuración (p. ej., configuración de impuestos) creados para módulos de extensión de Etendo.

Por último, es importante remarcar que:

- Cada organización, de cualquier tipo, puede tener su propia/s configuración/es de libro mayor y moneda/s (aparte de la heredada de su organización padre) si está configurada para ello en la Organización.
- Un calendario es obligatorio solo para las entidades legales con contabilidad. Este tipo de organización es el único que puede tener un calendario asignado; el resto puede heredarlo.
- Los informes financieros se ejecutan por configuración de libro mayor y, por lo tanto, por moneda, ya que cada configuración de libro mayor solo permite una moneda.
- Los informes financieros como el Balance de situación y la PyG, así como los informes fiscales, solo pueden crearse a nivel de Entidad legal con contabilidad.
    - El resto de informes, como informes de ventas, compras y almacén, pueden lanzarse para cualquier tipo de organización.
- No debería asignarse una configuración de libro mayor a la organización (\*), porque entonces se compartirá con todas las organizaciones por debajo.

## Ejemplos

1. **Datos de demostración de Etendo**:

    Etendo incluye datos de demostración con fines de demostración, que incluyen un Modelo empresarial compuesto por un conjunto de organizaciones.

    ![](../../../../../assets/drive/Vuf4G00AIK2uWFXjxHE733lf2QkM1WNhX1Eh29LCef9KNoZMGGnkD0O1vnkML26wZ7V_PHQHSgKtBgTxaB5Y3od9pFqzriF1nCYm7ysoMCJKrPf9-6jKp017i2QCIHKCBbV82bZn.png)

    - Una organización de tipo **Organización** denominada F&B International Group.
        - Esta organización no es una entidad legal y no permite transacciones.
        - Esta organización permite la creación y configuración de datos maestros para ser compartidos entre un grupo de organizaciones por debajo.
    - Dos **entidades legales con contabilidad** denominadas *F&B España* y *F&B US* que pertenecen a F&B International Group.
    - Por debajo de las organizaciones de entidades legales con contabilidad hay cuatro organizaciones **Genéricas**, que no son entidades legales pero pertenecen a una entidad legal y, además, permiten la introducción de datos transaccionales:
        - F&B US West Coast
        - F&B US East Coast
        - F&B España - Region Norte
        - F&B España - Region Sur

2. **Cómo crear cada tipo de Organización**:

    Las variables básicas a tener en cuenta al crear una organización del tipo **Organización** son:

    - Tipo de Organización = Organización
    - Incluir contabilidad = Sí  
        Si la configuración contable a este nivel necesita compartirse con todas las organizaciones por debajo de la que se está creando.
    - Dimensión de contabilidad = Tercero, Producto y Proyecto

    Las variables básicas a tener en cuenta al crear una organización del tipo **Legal con contabilidad** son:

    - Tipo de Organización = Legal con contabilidad
    - Incluir contabilidad = Sí
    - Dimensión de contabilidad = Tercero, Producto y Proyecto

    Las variables básicas a tener en cuenta al crear una organización del tipo **Legal sin contabilidad** son:

    - Tipo de Organización = Legal sin contabilidad
    - Incluir contabilidad = No

    Las variables básicas a tener en cuenta al crear una organización del tipo **Genérica** son:

    - Tipo de Organización = Genérica
    - Incluir contabilidad = Sí  
        Si esta organización requiere su propia configuración contable además de la heredada; en caso contrario, incluir contabilidad = No
    - Organización padre = debería ser una organización **Legal con contabilidad**.

3. **Ejemplos de modelos empresariales**:

    ![](../../../../../assets/drive/h9cS1Sgl07mpOdqMyrCNa-D3w4typy34vJcGl9wb5xk8vnpOkO4dPBwmBwY1JygGfPEeaQvh7katpn2-_fdTLWn5FyeIEPwZcNdkhkkKn0FUjTCTRLUosk2YcYwMoBegzLlVMzmCFCRzQztOKA.png)

    ![](../../../../../assets/drive/0mFr7Nl9jVy9ZVIfNVOl8pKVHpLv2h6waw6r0iGBnpjTs8A0P4wYIWAHFbYJKGrduahpu1QbmH4UXDq9n27_ffdvfgAcd8_plxvBEXx8cY7c7eWRjIvLBtByLU0-9Zw1iKsVttxtv3ecG9oNZA.png)

    ![](../../../../../assets/drive/2IIoZGBxPH1gigLWVMWKxE0GxWoAtAFJX2yheNUuOYoy_orJdRJII2rVZUpGcA8j4aJavDIoRIi1WJDymLDxqAbg-r-u6z4E91SRafrj9bX-EK4M8nhpqUqM1ufnYsgBc51D3HXAxZDPuy7R5A.png)

---

Este trabajo es una obra derivada de [Configuración General](https://wiki.openbravo.com/wiki/General_Setup){target="_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="_blank"} por [Etendo](https://etendo.software){target="_blank"}.