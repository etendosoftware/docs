---
title: Autenticación
tags:
  - Autenticación
  - Identidad
  - Nombre de usuario
  - Contraseña

status: beta
---
#  Autenticación
  
##  Visión general

!!! example  "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.
    
La **autenticación** es el acto de verificar la identidad de un usuario. Esto se puede hacer solicitando Nombre de usuario y Contraseña y verificándolo contra la tabla integrada `AD_User` o cualquier otro mecanismo.

##  Cómo funciona la autenticación en Etendo

Cuando un usuario quiere tener acceso a un recurso de Etendo, Etendo solicita al gestor de autenticación el Id de usuario de la aplicación del usuario que solicita acceso al recurso de Etendo. Si el usuario no ha sido autenticado previamente, el proveedor de autenticación tiene la responsabilidad de autenticar a este usuario.

A continuación se describe el flujo de eventos que ocurre al utilizar `DefaultAuthenticationManager`:

1. Visite cualquier URL de Etendo por primera vez; se envía una cookie de vuelta al navegador para permitir la creación habitual de una sesión HTTP (HTTP-Session) que permita agrupar las solicitudes del usuario. 
2. Se llama al método `authenticate` del Gestor de autenticación para comprobar si la sesión ya ha sido autenticada. La implementación de DefaultAuthenticationManager comprueba un atributo especial en el objeto HTTP-Session para decidir si esta sesión está autenticada o no. Como todavía no lo está, redirige al usuario a la página de inicio de sesión estándar de Etendo solicitando Usuario y Contraseña. 
3. Cuando se envía el formulario de inicio de sesión, la clase `LoginHandler` verifica esas credenciales contra la tabla `AD_User` y, si se aceptan, establece un atributo especial en HttpSession para marcar esta sesión como autenticada y almacenar el userID del usuario autenticado.
4. A continuación, se realiza una redirección a la página solicitada previamente. 
5. Para esta solicitud, se llama de nuevo al método `authenticate` de AuthenticationManager. Como ahora el atributo está establecido en la HttpSession correspondiente a esta solicitud, devuelve el userID del usuario autenticado y la solicitud continúa gestionándose de la forma habitual. 
6. Lo mismo ocurre ahora para cualquier solicitud posterior mientras se utiliza normalmente la aplicación. 
7. Esta sesión se invalidará por cualquiera de los siguientes tres eventos: 
    * Cierre de sesión explícito por parte del usuario 
    * Tiempo de espera de la sesión (invalidación de la HttpSession) 
    * Borrar la cookie del navegador por parte del usuario 
8. En ese caso, el flujo vuelve al primer paso y el mismo ciclo comienza de nuevo. 

!!!Note
    Esto solo describe el flujo de eventos al utilizar `DefaultAuthenticationManager`. Cualquier otra implementación puede implementar esto de forma diferente, por ejemplo, no utilizando en absoluto la página de inicio de sesión estándar de Etendo o utilizando otro mecanismo para marcar la HTTP-Session como autenticada.

##  Cómo configurar el gestor de autenticación en Etendo

El gestor de autenticación utilizado en Etendo se define en el archivo de configuración `gradle.properties`. En la propiedad `authentication.class` tiene que escribir el nombre de la clase del proveedor de autenticación que Etendo utilizará para este propósito.

Etendo incluye tres implementaciones de `AuthenticationManager`:

###  Gestor de autenticación predeterminado

Este es el gestor de autenticación predeterminado proporcionado por Etendo. Es el método de autenticación clásico que utiliza la página de inicio de sesión actual de Etendo para autenticar a los usuarios.

Después de instalar Etendo, no necesita configurar nada si desea utilizar este gestor de autenticación, que es el método clásico con el que Etendo autentica a los usuarios de la aplicación.

##  Obtener el gestor de autenticación

!!!info
    Para obtener una instancia del Gestor de autenticación definido en `gradle.properties`, es posible utilizar el método `AuthenticationManager.getAuthenticationManager`.

##  Desarrolle su propio gestor de autenticación
  
También puede desarrollar su propio gestor de autenticación. Para ello, tiene que crear una nueva clase Java que extienda la clase abstracta `org.openbravo.authentication.AuthenticationManager`. Esta interfaz tiene los siguientes métodos:

    ```
    public void init(HttpServlet s) throws AuthenticationException;
     
    public final String authenticate(HttpServletRequest request, HttpServletResponse response)
        throws AuthenticationException, ServletException, IOException
 
    public final String webServiceAuthenticate(HttpServletRequest request)
        throws AuthenticationException
 
    public final String webServiceAuthenticate(String user, String password)
        throws AuthenticationException
 
    public final String connectorAuthenticate(HttpServletRequest request)
        throws AuthenticationException
 
    public final String connectorAuthenticate(String user, String password)
        throws AuthenticationException
 
    protected abstract String doAuthenticate(HttpServletRequest request, HttpServletResponse response)
        throws AuthenticationException, ServletException, IOException
 
    protected String doWebServiceAuthenticate(HttpServletRequest request)
 
    protected String doWebServiceAuthenticate(String user, String password)
 
    public final void logout(HttpServletRequest request, HttpServletResponse response)
        throws ServletException, IOException
 
    protected abstract void doLogout(HttpServletRequest request, HttpServletResponse response)
        throws ServletException, IOException
    ```

El método `init` se llama después de que la clase se instancie. Puede utilizarse para leer los parámetros de configuración del gestor de autenticación si es necesario.

El método `authenticate` se llama para cada solicitud individual realizada que requiera autenticación. Invoca el método abstracto `doAuthenticate` que, si esta solicitud está autenticada, debe devolver el userid del usuario autenticado. Este id debe ser un ad_user_id válido de una entrada existente en la tabla `AD_User`.

De lo contrario, el método debe realizar los pasos necesarios para obtener alguna autenticación y luego devolver null como valor de retorno de la función. Normalmente, esto consiste en redirigir al usuario a algún tipo de página de inicio de sesión y solicitar credenciales. Después de que estas se hayan verificado, se llamará de nuevo al método **authenticate** para la siguiente solicitud y ahora tendrá éxito y devolverá el userId como se describió anteriormente.

El método **logout** se llama cuando el usuario solicita cerrar la sesión actual. Este método invoca el método abstracto `doLogout`. El trabajo que se espera que realice el gestor de autenticación es invalidar la sesión existente y redirigir al usuario a una página donde se pueda realizar un nuevo inicio de sesión.

!!!info
    `AuthenticationManager` es donde se sirve la página de autenticación fuera del código de Etendo; por ejemplo, desde un servicio de inicio de sesión único (Single Sign On). Debe sobrescribir el método `useExternalLoginPage`, devolviendo `true`.  
  
!!!Note
    Para la implementación: el método **authenticate** siempre se llama con DAL adminMode activo, por lo que el código dentro de él no necesita gestionar el adminMode por sí mismo.  
  
###  Servicios web y conectores

!!!info
    Todos los servicios externos autenticados **deben** hacer uso de la autenticación `webServiceAuthenticate`. Los **conectores** autorizados pueden usar `connectorAuthenticate`.  
  
La autenticación de servicios web invoca `webServiceAuthenticate` y los conectores invocan `connectorAuthenticate`; ambos llaman a `doWebServiceAuthenticate`. Este método está implementado para realizar la autenticación estándar: primero busca si el usuario **l** y la contraseña **p** se envían como parámetros de la solicitud; si no, se realiza autenticación básica. El método `doWebServiceAuthenticate` puede ser implementado por los gestores de autenticación en caso de que se necesite una autenticación diferente.

`webServiceAuthenticate` y `connectorAuthenticate` están sobrecargados para aceptar tanto el parámetro `HttpServletRequest` (el predeterminado) como los parámetros `String, String`. Este segundo debe ser utilizado por otros servicios donde el predeterminado no sea adecuado; este recibe los parámetros de usuario y contraseña.


---

Este trabajo es una obra derivada de [Autenticación](http://wiki.openbravo.com/wiki/Authentication){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.