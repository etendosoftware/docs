---
title: Bundle de extensiones de plataforma | Documentación técnica
---

:octicons-package-16: Javapackage: `com.etendoerp.platform.extensions`

## Visión general

Este bundle incluye mejoras para funcionalidades de la plataforma en Etendo.

## Gestión de Docker

:octicons-package-16: Javapackage: `com.etendoerp.docker`

Este módulo permite el uso de contenedores dockerizados en Etendo Classic.

!!!info
    Para más información, visite la [Guía del desarrollador de Gestión de Docker](../platform/docker-management.md).

## Servicio Tomcat dockerizado

:octicons-package-16: Javapackage: `com.etendoerp.tomcat`

Este módulo permite la dockerización de Tomcat dentro de Etendo Classic. 

!!!info
    Para más información, visite la [Guía del desarrollador de Servicio Tomcat dockerizado](../platform/dockerized-tomcat-service.md).

## Aplicación dinámica 

:octicons-package-16: Javapackage: `com.etendoerp.dynamic.app`

Aplicación dinámica le permite crear subaplicaciones en Etendo Mobile.

!!! info
    Para más información, visite la [Guía del desarrollador de Aplicación dinámica](./dynamic-app.md)

## EAN 128

### Aspectos técnicos

Es un módulo para la transmisión de información entre los agentes de la cadena de suministro bajo las especificaciones del código de barras Code 128. Esto proporciona utilidades genéricas para la definición y el parseo de EAN128.

Es un módulo basado en Java para gestionar códigos de barras EAN-128 en un contexto de Etendo ERP. A continuación, se muestra una visión general de lo que parece hacer cada archivo:

### SelectorFieldPropertyDataSource.java

**Propósito**: Implementa una fuente de datos para un selector de campo personalizado.  
**Operaciones principales**: Verifica si un usuario tiene el derecho de acceso para obtener datos desde la fuente de datos.  
Filtra propiedades Blob y OneToMany al obtener propiedades de la entidad.

### EAN128Utils.java

**Propósito**: Clase de utilidades para gestionar el parseo y la manipulación de datos EAN-128.

**Operaciones principales**: Define formatos de fecha estándar y claves JSON.  
Parsea el JSON de datos EAN128 entrante y extrae información relevante como lote, número de serie, fechas de caducidad, etc.  
Si se parseó la cantidad de la línea de inventario, modifica la cantidad del BaseOBObject correspondiente.  
Proporciona métodos para editar objetos base de OpenBravo (BaseOBObject) en función de los datos EAN-128 parseados.

### EANType.java

**Propósito**: Servicio web para gestionar tipos EAN-128.

**Operaciones principales**: Gestiona solicitudes HTTP GET y recupera información del tipo EAN-128.  
La información obtenida depende del almacén especificado en los parámetros de la solicitud.  
Si no hay disponible un tipo EAN-128 específico del almacén, intenta obtener el predeterminado.  
Convierte el tipo EAN-128 a un objeto JSON y lo devuelve como respuesta.

**Bibliotecas clave utilizadas**:

- Etendo DAL para la interacción con la base de datos.
- Apache Commons Lang para manipulaciones de cadenas.
- JSON y Jettison para el parseo de JSON.

### SMFEANComponentProvider.java

**Propósito**: Define los recursos globales necesarios para el funcionamiento de los componentes que proporciona.

## Etendo Advanced Security

:octicons-package-16: Javapackage: `com.etendoerp.advanced.security`

:octicons-package-16: Javapackage: `com.etendoerp.advanced.security.template`

### Aspectos técnicos

Este módulo permite personalizar varias funcionalidades de seguridad relacionadas con:

- Seguridad de contraseñas
- Historial de contraseñas
- Bloqueo de usuario
- Verificación de múltiples sesiones
- Cambio de contraseña después del inicio de sesión
- Tiempo de expiración (bloqueo automático de contraseña)

Para que este módulo funcione, se debe configurar la clase Java de autenticación en el archivo `gradle.properties` añadiendo la siguiente línea:

```groovy title="gradle.properties"
authentication.class=com.etendoerp.advanced.security.process.AdvancedAuthenticationManager
```

!!! warning
    Este módulo no puede configurarse junto con [Etendo RX - SSO Login](./etendo-rx.md#etendo-sso-login) porque ambos usan la propiedad `authentication.class`. 

A continuación, debe ejecutarse `./gradlew setup`.

!!! warning
    Es obligatorio ejecutar este paso antes de instalar el módulo. 

## Etendo Webhooks

Permite ejecutar acciones mediante una llamada a una URL, proporcionando una forma potente de integrarse con servicios externos.

!!! info
    Para más información, visite la [Guía del desarrollador de Etendo Webhooks](../../../../developer-guide/etendo-classic/bundles/platform/etendo-webhooks.md).

## Número a palabra

:octicons-package-16: Javapackage: `org.openbravo.numbertoword_en`

:octicons-package-16: Javapackage: `org.openbravo.numbertoword`

### Visión general

Este módulo proporciona la infraestructura para convertir un número en su equivalente en palabras. Esta funcionalidad es especialmente útil al imprimir cheques.

### Ventanas del conversor de número a palabra

:material-menu: `Aplicación` > `Configuración General` > `Aplicación` > `Conversor de número a palabra`

Una vez instalado, este módulo añade una nueva ventana de configuración llamada **Conversor de número a palabra**, donde puede especificar, para cada organización, la clase Java responsable de convertir números a palabras. El módulo `org.openbravo.numbertoword_en` proporciona la implementación de la clase que realiza la conversión al inglés.

![](../../../../assets/drive/1YjGbvShn-Mwb6iNpbajKgNo77ukscR3n.png)

Algunos campos a tener en cuenta son:

**Organización** que es la entidad legal que requiere imprimir cheques en un idioma determinado.  
**Idioma** que es el idioma a cuyas palabras deben convertirse los importes a pagar.  
**Clase Java** que es la ruta donde se encuentra la clase Java que convierte importes a un idioma determinado.

El campo **Clase Java** es obligatorio, pero está vacío por defecto, a menos que se instale y se aplique correctamente a la entidad legal para la que se requiere imprimir cheques otro módulo como Número a palabra (español) o Número a palabra (inglés). Además, la **Clase Java** puede completarse manualmente.

### Aspectos técnicos

El módulo NumberToWord despliega una infraestructura para definir módulos de conversión de **Número a palabra**, de modo que puedan desplegarse lógicas diferentes para distintos idiomas.

Para introducir un idioma diferente (distinto de inglés y español), siga este ejemplo para ampliar esta extensión de Número a palabra:

```java
public class NumberToWord_es extends NumberToWord {
  private static String[] _grupos = { "", "millon", "billon", "trillon" };

  private static String[] _unidades = { "", "un", "dos", "tres", "cuatro", "cinco", "seis",
      "siete", "ocho", "nueve" };

  private static String[] _decena1 = { "", "once", "doce", "trece", "catorce", "quince",
      "dieciseis", "diecisiete", "dieciocho", "diecinueve" };

  private static String[] _decenas = { "", "diez", "veinte", "treinta", "cuarenta", "cincuenta",
      "sesenta", "setenta", "ochenta", "noventa" };

  private static String[] _centenas = { "", "cien", "doscientos", "trescientos", "cuatrocientos",
      "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos" };

  public static String millarATexto(int n) {
    if (n == 0)
      return "";

    int centenas = n / 100;
    n = n % 100;
    int decenas = n / 10;
    int unidades = n % 10;

    String sufijo = "";

    if (decenas == 0 && unidades != 0)
      sufijo = _unidades[unidades];

    if (decenas == 1 && unidades != 0)
      sufijo = _decena1[unidades];

    if (decenas == 2 && unidades != 0)
      sufijo = "veinti" + _unidades[unidades];

    if (unidades == 0)
      sufijo = _decenas[decenas];

    if (decenas > 2 && unidades != 0)
      sufijo = _decenas[decenas] + " y " + _unidades[unidades];

    if (centenas != 1)
      return _centenas[centenas] + " " + sufijo;

    if (unidades == 0 && decenas == 0)
      return "cien";

    return "ciento " + sufijo;
  }

  public static String numeroACastellano(long n) {
    String resultado = "";
    int grupo = 0;
    while (n != 0 && grupo < _grupos.length) {
      long fragmento = n % 1000000;
      int millarAlto = (int) (fragmento / 1000);
      int millarBajo = (int) (fragmento % 1000);
      n = n / 1000000;

      String nombreGrupo = _grupos[grupo];
      if (fragmento > 1 && grupo > 0)
        nombreGrupo += "es";

      if ((millarAlto != 0) || (millarBajo != 0)) {
        if (millarAlto > 1)
          resultado = millarATexto(millarAlto) + " mil " + millarATexto(millarBajo) + " "
              + nombreGrupo + " " + resultado;

        if (millarAlto == 0)
          resultado = millarATexto(millarBajo) + " " + nombreGrupo + " " + resultado;

        if (millarAlto == 1)
          resultado = "mil " + millarATexto(millarBajo) + " " + nombreGrupo + " " + resultado;
      }
      grupo++;
    }
    resultado = resultado.trim().concat(" ");
    return resultado;
  }

  public String convert(BigDecimal number) {

    double num = number.doubleValue();

    num = (double) (Math.round(num * Math.pow(10, 2)) / Math.pow(10, 2));
    int number_whole = (int) num;
    int number_decimal = (int) ((num * 100) - (number_whole * 100));
    String value;
    if (number_decimal == 0) {
      value = numeroACastellano(number_whole).concat("00/100 M.N.");
    } else {
      value = numeroACastellano(number_whole).concat(Integer.toString(number_decimal)).concat(
          "/100 M.N.");
    }
    value = value.substring(0, 1).toUpperCase().concat(value.substring(1));
    return value;
  }

}
```

## OpenAPI

:octicons-package-16: Javapackage: `com.etendoerp.openapi`

Este módulo sirve como una capa de integración para documentar y exponer APIs dentro del ecosistema de Etendo. Permite a los desarrolladores definir, organizar y documentar endpoints de API usando la especificación OpenAPI, garantizando la compatibilidad con herramientas como Swagger para visualización y pruebas.

!!!info
    Para más información, visite [Cómo documentar un endpoint con OpenAPI](../../how-to-guides/how-to-document-an-endpoint-with-openapi.md). 

## Servicio web de impresión de documentos

:octicons-package-16: Javapackage: `com.etendoerp.printdocumentws`

:octicons-package-16: Javapackage: `com.smf.ws.printdocument`

### Aspectos técnicos

Este módulo permite descargar un PDF de algunos documentos de transacción usando un servicio web llamado printDocument. Devuelve un PDF con el pedido, la factura o el albarán. Esto es útil para empresas que usan aplicaciones de terceros y requieren hacer accesibles los imprimibles desde esas aplicaciones.

Los documentos soportados son:

- Presupuesto de ventas
- Factura
- Remesa
- Pedido proforma
- Presupuesto proforma

Para llamar al servicio web, se necesita la siguiente URL:

```
http://<client-url/etendo>/sws/com.etendoerp.printdocumentws.printDocument
```

Es necesario configurar la autenticación por token para usar el servicio web.

Los valores que pueden usarse para llamar al servicio web son:

- order
- invoice
- shipment
- quotation
- orderProforma
- shipmentValued
- quotationProforma

Este es un servicio web RESTful que devuelve un archivo .PDF del documento usando la plantilla que esté configurada. Los documentos soportados son Presupuesto de ventas, Factura, Remesa, Pedido proforma, Presupuesto proforma.

Es obligatorio insertar el ID de la organización cuando se llama al servicio web porque filtra por organización.

## Gestión de caché de informes

:octicons-package-16: Javapackage: `com.exos.erp.reportcachemanagement`

Este módulo permite cambiar o actualizar un **Informe Jasper** en un entorno Etendo sin detener el servidor.

### Aspectos técnicos

Este módulo permite limpiar la caché de informes compilados en Tomcat. Los informes deben subirse a la carpeta correcta, por ejemplo: `/var/lib/tomcat/webapps/etendo/…`

A continuación, en la ventana **Limpiar caché de informes**, haga clic en *Hecho*:

![Limpiar caché de informes](../../../../assets/developer-guide/etendo-classic/bundles/platform/overview/clear-report-cache.png)

En esta ventana, el usuario, por lo general un desarrollador, puede eliminar los datos de la caché de informes haciendo clic en el **botón Hecho**. Esto tiene fines técnicos.  
Después de hacer clic, se mostrará un mensaje de éxito indicando la finalización del proceso.

---

Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L.](https://etendo.software){target="_blank"}.