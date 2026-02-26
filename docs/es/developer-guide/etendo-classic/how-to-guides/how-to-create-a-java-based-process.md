---
title: Cómo crear un proceso basado en Java (obsoleto)
tags: 
    - Proceso Java
    - Configuración de Etendo
    - Parámetros del proceso 
    - Desarrollo de módulos
    - Obsoleto
---


# Cómo crear un proceso basado en Java (obsoleto)

## Visión general

!!! warning
    La forma recomendada de implementar procesos es mediante [Definición del Proceso](./how-to-create-a-standard-process-definition.md)

Los **procesos Java** son uno de los mecanismos que Etendo proporciona para implementar lógica de negocio. Un proceso Java puede ejecutarse en el [proceso en segundo plano](../how-to-guides/how-to-develop-a-dal-background-process.md) u ofrecer una interfaz de usuario que permita introducir parámetros. Esta sección explica cómo crear un proceso Java que incluya una interfaz de usuario con **parámetros** definidos por el usuario. También describe la infraestructura subyacente utilizada para dar soporte a los procesos Java en Etendo.

!!! info
    Para una descripción genérica de los procesos Java, visite [Procesos](../concepts/processes.md).

## Módulo de ejemplo

Esta sección se apoya en un módulo de ejemplo que muestra un ejemplo del código que se presenta y se comenta aquí. 

El código del módulo de ejemplo puede descargarse del repositorio [com.etendoerp.client.application.examples](https://github.com/etendosoftware/com.etendoerp.client.application.examples){target="\_blank"}. 

!!! info
    Para cualquier desarrollo específico, cree un nuevo módulo. Para más información, visite [Cómo crear un módulo](../how-to-guides/how-to-create-a-module.md).


## Pasos de desarrollo

Los pasos para crear un proceso Java soportado por una interfaz de usuario son:

  1. Crear una **clase Java** que implemente la lógica de negocio.
  2. Introducir un nuevo registro en **Informes y procesos**, definiendo el patrón, la clase Java (paso 1) y los parámetros. 
  3. Añadir el **nuevo proceso** al menú.

### Declaración de la clase Java

En primer lugar, revise el paquete Java en el que se define la clase Java; debe estar incluido en el paquete Java que define el módulo. La clase Java que implementa el proceso debe implementar la interfaz `org.openbravo.scheduling.Process`; esto se hace normalmente extendiendo la clase `org.openbravo.service.db.DalBaseProcess`, que proporciona código común para usar **DAL** en procesos. 

Al extender esta clase, solo es necesario sobrescribir un método:

``` java
public void doExecute(ProcessBundle bundle) throws Exception{...}
```

Este método recibe un `ProcessBundle`; este bundle contiene todos los parámetros del proceso. Cuando el proceso finaliza, debe añadir un resultado a este bundle; este resultado es una instancia de `OBError` que se mostrará en el pop-up. 

!!! info
    Para más explicaciones sobre mensajes, consulte la documentación de [Mensaje](../concepts/messages.md).

Veamos un ejemplo (esta clase y sus parámetros se utilizan en la definición del proceso más abajo en esta sección):  

``` java
public class ExampleJavaProcess extends DalBaseProcess {

  @Override
  public void doExecute(ProcessBundle bundle) throws Exception {
    try {

      // retrieve the parameters from the bundle
      final String bPartnerId = (String) bundle.getParams().get("cBpartnerId");
      final String organizationId = (String) bundle.getParams().get("adOrgId");
      final String myString = (String) bundle.getParams().get("mystring");

      // implement your process here

      // Show a result
      final StringBuilder sb = new StringBuilder();
      sb.append("Read information:<br/>");
      if (bPartnerId != null) {
        final BusinessPartner bPartner = OBDal.getInstance().get(BusinessPartner.class, bPartnerId);
        sb.append("Business Partner: " + bPartner.getIdentifier() + "<br/>");
      }
      if (organizationId != null) {
        final Organization organization = OBDal.getInstance()
            .get(Organization.class, organizationId);
        sb.append("Organization: " + organization.getIdentifier() + "<br/>");
      }
      sb.append("MyString: " + myString + "<br/>");

      // OBError is also used for successful results
      final OBError msg = new OBError();
      msg.setType("Success");
      msg.setTitle("Read parameters!");
      msg.setMessage(sb.toString());

      bundle.setResult(msg);

    } catch (final Exception e) {
      e.printStackTrace(System.err);
      final OBError msg = new OBError();
      msg.setType("Error");
      msg.setMessage(e.getMessage());
      msg.setTitle("Error occurred");
      bundle.setResult(msg);
    }
  }
}
```

En este ejemplo se espera un parámetro llamado `cBpartnerId`. Se lee mediante la siguiente línea:

``` java
final String bPartnerId = (String) bundle.getParams().get("cBpartnerId");
```

El nombre del parámetro que se debe usar en el método `get` depende del **Nombre columna BD** introducido en los parámetros del proceso.

Una vez finalizado el proceso, se crea un nuevo `OBError` para gestionar el mensaje y se añade como resultado al **bundle**.

``` java
bundle.setResult(msg);
```

### Definición de la interfaz de usuario
:material-menu: `Diccionario de la Aplicación` > `Informes y procesos`

La clase Java anterior muestra cómo implementar la **lógica de negocio del backend**. Esta sección explica cómo definir una interfaz de usuario que permita introducir parámetros.

Para definir registros de proceso, es necesario ser **Prueba**.

El primer paso es crear un registro de proceso; vaya a `Diccionario de la Aplicación > Informes y procesos`. Cree un nuevo registro de proceso como se muestra en el ejemplo siguiente.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-java-based-process/how-to-create-a-java-based-process-1.png)

  
El aspecto principal aquí es seleccionar **Patrón de UI: Estándar**. 

A continuación, cree un registro hijo en **Process class** e introduzca el nombre de clase completamente cualificado de la clase Java creada anteriormente.

!!! note
    Marque el indicador por defecto. Si no se hace, se producirá un error de compilación en el siguiente paso de construcción.

Ahora es necesario definir los parámetros del proceso, o más exactamente su tipo y visualización. Esto se realiza mediante la solapa hija **Parámetros** del proceso. El ejemplo tiene tres parámetros: **tercero, organización y una cadena**. Las imágenes siguientes muestran su configuración:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-java-based-process/how-to-create-a-java-based-process-2.png)

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-java-based-process/how-to-create-a-java-based-process-3.png)

!!! note 
    - El **Nombre columna BD** no tiene por qué ser una columna real de base de datos; el valor de este campo se utiliza para generar el nombre del parámetro usado en el código fuente. Se recomienda usar nombres simples sin guiones bajos.
    - El **Elemento del sistema** define la etiqueta en la interfaz de usuario.
    - Los 2 campos de referencia indican el **tipo del campo**.

### Añadir el formulario del proceso al menú

Para que la ventana del proceso esté disponible para el usuario, debe añadirse a un **menú**.

Esto se hace así:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-java-based-process/how-to-create-a-java-based-process-4.png)


### Paso de construcción

Después de crear la interfaz de usuario del proceso, detenga la aplicación y escriba el siguiente comando en una consola (dentro del proyecto de desarrollo):

``` bash title="Terminal"
./gradlew compile.complete smartbuild
```

Esto generará la ventana del proceso. Si IntelliJ está en ejecución, actualice el proyecto de desarrollo. A continuación, inicie la aplicación e inicie sesión con el administrador del cliente (normalmente el administrador del sistema no tendrá acceso).

## El resultado

Vaya al lanzamiento rápido e introduzca el nombre del nuevo proceso o búsquelo en la ubicación correcta del menú.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-java-based-process/how-to-create-a-java-based-process-5.png)

Introduzca algunos valores y pulse Aceptar. El resultado:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-java-based-process/how-to-create-a-java-based-process-6.png)

## Variante: ejecutar el proceso desde un botón en otra ventana

Un proceso también puede ejecutarse desde otra ventana usando un **botón**. En Etendo, los botones mostrados en una ventana se definen mediante una **columna AD** con **Referencia = Botón**, vinculada a un **proceso** específico.

Para ejecutar un proceso desde un botón en una ventana existente, siga estos pasos:

#### 1. Añadir una columna a la tabla utilizada por la ventana de destino
- Vaya a `Diccionario de la Aplicación > Table and Columns`.
- Localice la tabla que se muestra en la ventana donde desea que aparezca el botón.
- Cree una nueva columna.

#### 2. Configurar la columna como un botón vinculado a su proceso
- Establezca la **Referencia** de la columna en **Botón**.
- En la configuración de la columna, seleccione el **Proceso** que debe ejecutarse cuando se pulse el botón.
- Use un nombre significativo (este será la base para la etiqueta que se mostrará posteriormente mediante el **Elemento del sistema** / **Campo**).

#### 3. Exponer el botón en la ventana
- Vaya a `Diccionario de la Aplicación > Window, Tabs and Fields`.
- Localice la **Ventana** y la **Solapa** de destino.
- Cree un **Campo** vinculado a la columna que creó.
- Ajuste su ubicación según sea necesario para que aparezca en la sección deseada de la solapa.

#### 4. Usar el botón en la UI
- Una vez que la ventana se haya generado y el campo esté presente, el usuario verá un botón en la ventana (por ejemplo, un botón como **"Acción de documento de ejemplo"**).
- Al hacer clic en el botón, se ejecutará el proceso configurado.
  
Cuando un proceso se ejecuta desde otra ventana, el **ProcessBundle** contendrá parámetros por defecto adicionales que pueden ser útiles:

- **recordID**: el id del registro seleccionado.
- **tabId**: el id de la solapa desde la que se llamó al proceso.

## Variante: patrón de UI manual

La diferencia entre el **patrón de UI estándar y manual** es que no se genera automáticamente ningún pop-up para los procesos con patrón **UI manual**; en este caso, el pop-up debe generarse manualmente por la clase que implementa el proceso.

Como se ha mostrado anteriormente, las clases Java para **procesos estándar** implementan los procesos manuales que se implementan mediante una clase Java que implementa la interfaz `org.openbravo.scheduling.Process`. 

Para los **procesos manuales**, la clase Java necesita extender `org.openbravo.base.secureApp.HttpSecureAppServlet`, que es un servlet estándar que genera el pop-up.