---
title: Cómo llamar a un servicio web de Etendo desde Java 
tags:
    - Clase Java
    - Servicio web de Etendo
    - Conexiones HTTP
    - Autenticación
    - procesamiento-xml
status: beta
---

# Cómo llamar a un servicio web de Etendo desde Java 
  
!!! example  "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.

## Visión general

Esta sección explica cómo preparar e implementar una **Clase Java** capaz de invocar servicios web de Etendo y qué **API de Java** se requieren para establecer conexiones HTTP, autenticar solicitudes y procesar respuestas, especialmente aquellas devueltas en formato XML por servicios web XML REST. Usando la propia clase `BaseWSTest.java` de Etendo como referencia, la guía muestra cómo construir y ampliar métodos para diferentes operaciones HTTP (GET, POST, PUT, DELETE), gestionar la autenticación de forma segura y administrar el comportamiento de sesión para integraciones de alta frecuencia o sin estado.

!!!info
    Para más información, visite [Servicios web XML REST](../../../developer-guide/etendo-classic/concepts/.XML_REST_Web_Services.md). 


## Pasos de ejecución

Para llamar a un **servicio web de Etendo** desde una clase Java, utilice varias clases que proporcionan la API de Java adecuada para crear una conexión HTTP mediante la URL del servicio web y para usar clases del `java.iopackage` que permiten leer los flujos de datos. Además, de forma opcional, utilice algunas clases que facilitan el procesamiento de los resultados que se devuelven en **formato XML** en el caso de servicios web del tipo **XML REST**, ya que permiten obtener, analizar y validar un documento XML.

### Código de ejemplo

Etendo dispone de una **clase Java de prueba** que ejemplifica lo anterior. Esta clase es `BaseWSTest.java` y se encuentra dentro del directorio `src-test/org/openbravo/test/webservice`. Para realizar una solicitud al servicio web, disponemos del método **createConnection()**, que utiliza la clase httpURLConnection para realizar una solicitud a un servicio web usando el parámetro de comando específico y especificando las credenciales (usuario/contraseña).

``` java
protected HttpURLConnection createConnection(String wsPart, String method) throws Exception {
    Authenticator.setDefault(new Authenticator() {
        @Override
        protected PasswordAuthentication getPasswordAuthentication() {
            return new PasswordAuthentication(LOGIN, PWD.toCharArray());
        }
    });
    log.debug(method + ": " + getOpenbravoURL() + wsPart);
    final URL url = new URL(getOpenbravoURL() + wsPart + "&basicAuthentication=true");
    final HttpURLConnection hc = (HttpURLConnection) url.openConnection();
    hc.setRequestMethod(method);
    hc.setAllowUserInteraction(false);
    hc.setDefaultUseCaches(false);
    hc.setDoOutput(true);
    hc.setDoInput(true);
    hc.setInstanceFollowRedirects(true);
    hc.setUseCaches(false);
    hc.setRequestProperty("Content-Type", "text/xml");
    return hc;
}
```

!!! note
    Este código de ejemplo utiliza autenticación básica; consulte a continuación para más detalles.

Usando esta función como base, se implementarán otros métodos para los otros comandos `HTTP`: **POST, PUT, GET y DELETE**. Además, esta clase utiliza la `biblioteca org.xml.sax` para analizar los resultados `XML` que se devolverán tras nuestra solicitud `HTTP`. Por ejemplo, la solicitud **GET**:
    
``` java 
protected String doTestGetRequest(String wsPart, String testContent, int responseCode,boolean validate) {
    try {
        final HttpURLConnection hc = createConnection(wsPart, "GET");
        hc.connect();
        final SAXReader sr = new SAXReader();
        final InputStream is = hc.getInputStream();
        final StringBuilder sb = new StringBuilder();
        BufferedReader reader = new BufferedReader(new InputStreamReader(is, "UTF-8"));
        String line;
        while ((line = reader.readLine()) != null) {
            sb.append(line).append("\n");
        }
        try {
            final Document doc = sr.read(new StringReader(sb.toString()));
            final String content = XMLUtil.getInstance().toString(doc);
            if (testContent != null && content.indexOf(testContent) == -1) {
                log.debug(content);
                fail();
            }
            assertEquals(responseCode, hc.getResponseCode());
            is.close();
            // do not validate the xml schema itself, this results in infinite loops
            if (validate) {
                validateXML(content);
            }
            return content;
        } catch (Exception e) {
            log.debug(sb.toString());
            throw e;
            }
    } catch (final Exception e) {
            throw new OBException("Exception when executing ws: " + wsPart, e);
        }
}
```

Por lo tanto, es posible utilizar esta clase como base para el desarrollo e implementar las adaptaciones que se consideren necesarias. Usando esta clase, es posible implementar llamadas a los servicios web que usted elija simplemente especificando su ruta, que se formará con la URL de Etendo `getOpenbravoURL()` más la parte del servicio web **wsPart**.

### Inicio de sesión y seguridad

Los servicios web generales de Etendo proporcionan el mismo control de inicio de sesión y seguridad que el servicio web XML REST.

### Autenticación básica: 

El siguiente código de ejemplo muestra una forma de implementar autenticación básica:

    
``` java    
Authenticator.setDefault(new Authenticator() {
    @Override
    protected PasswordAuthentication getPasswordAuthentication() {
    return new PasswordAuthentication(getLogin(), getPassword().toCharArray());
    }
});
```

Este enfoque necesitará dos solicitudes: 

- La primera fallará con 401, volverá al llamador/cliente y luego llamará al método getPasswordAuthentication anterior para una segunda solicitud con credenciales. Como se necesitan dos solicitudes para esta autenticación, es menos útil para llamadas de alta frecuencia. 

    Para que este tipo de enfoque funcione en el código de Etendo, es necesario pasar el parámetro `basicAuthentication=true` en la URL de la solicitud.

- Otro enfoque consiste en establecer las credenciales en la cabecera de la solicitud de esta forma; esto solo requiere una solicitud, ya que Etendo encontrará directamente la información de autenticación y no lanzará un 401:

     
    ``` java
    String userpass = getLogin() + ":" + getPassword();
    String basicAuth = "Basic " + new String(new Base64().encode(userpass.getBytes()));
    hc.setRequestProperty("Authorization", basicAuth);
    ```

### Alta frecuencia - Sin estado

El código del lado del cliente que llama a servicios web normalmente **no mantiene** la cookie de sesión del servidor. Esto significa que cada solicitud al servicio web puede crear una nueva sesión http en el servidor receptor. Esto no es recomendable para servicios web de alta frecuencia. El implementador del servicio web dentro del sistema Etendo puede **forzar la llamada** para que sea sin estado. Pero el llamador también puede lograrlo pasando un parámetro. 

---
Este trabajo es una obra derivada de [Cómo llamar a un servicio web de Openbravo desde Java](http://wiki.openbravo.com/wiki/How_To_Call_An_Openbravo_Webservice_From_Java){target="\_blank"} de [Wiki de Openbravo](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.