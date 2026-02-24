---
title: Enlaces profundos
tags:
    - Enlaces profundos
    - Enlaces
    - URL
    - Parámetros

status: beta
---

#  Enlaces profundos

!!! example  "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.
  
##  Visión general

Según [Wikipedia](https://en.wikipedia.org/wiki/Deep_linking){target="\_blank"}, los enlaces profundos consisten en crear un hipervínculo que apunte a una página o imagen específica dentro de un sitio web, en lugar de a la página principal o de inicio de ese sitio web. A estos enlaces se les denomina "enlaces profundos". En el caso de Etendo, es la forma de enlazar mediante una URL directamente a una funcionalidad específica, por ejemplo, una Ventana/Solapa, un Formulario manual, etc. Este enlace puede construirse y adjuntarse en un correo electrónico, o copiarse/pegarse en una ventana de mensajería instantánea, etc.

##  Obtener un enlace directo/profundo

La interfaz de usuario de Etendo facilita mucho obtener una URL a una ventana, solapa y registro específico (en una solapa hija). Consulte el icono en la parte superior de la ventana de Etendo.

![](../../../assets/developer-guide/etendo-classic/concepts/deep-linking/deeplinking0.png)

Se puede hacer clic en este icono para crear un enlace directo a una solapa:

![](../../../assets/developer-guide/etendo-classic/concepts/deep-linking/deeplinking1.png)
  
Este ejemplo muestra el enlace directo a la solapa de cabecera de la factura de ventas.

##  Estructura de la URL

```  
http://server:port/obcontext/?params
```

* **http://** El protocolo para acceder a la aplicación (puede ser https si se trata de una instancia con SSL habilitado) 
* **server** El nombre o la dirección IP del servidor 
* **port** El puerto de acceso (si está configurado con Apache Httpd delante de Tomcat no es necesario) 
* **/obcontext** El nombre del contexto de Etendo (obligatorio) 
* **?params** La lista de parámetros para acceder a una ventana o formulario específico. 

Para más información, visite [la estructura de una URL](https://skorks.com/2010/05/what-every-developer-should-know-about-urls/){target="\_blank"}.

Se admiten los siguientes parámetros:

* **`tabId`** (obligatorio) el ID de la solapa a la que desea enlazar.
* **`recordId`** el ID del registro que se mostrará en la solapa.
* **`command`** el parámetro command puede utilizarse para mostrar el formulario en modo Nuevo; solo se admite un comando: NEW.

!!! note
    * Enlazar a una solapa (nieta) hija solo tiene sentido cuando también se define un recordId (del registro que se mostrará en la solapa hija). Esto es necesario para determinar qué registro padre cargar en la solapa padre 
    * Cuando se utiliza el parámetro recordId, la solapa siempre se abrirá en modo formulario 

A continuación se muestran algunos ejemplos de hipervínculos:

* http://localhost:8080/etendo/?tabId=263 - Enlace a la cabecera de la factura de ventas 
* http://localhost:8080/etendo/?tabId=263&recordId=FF808181304ACF4201304AE46E4B003E - Enlace a una factura de ventas específica 
* http://localhost:8080/etendo/?tabId=270&recordId=00C1DB5F5AB241D2A574B8CEBF482F8F - Enlace a una línea de factura de ventas específica 
* http://localhost:8080/etendo/?tabId=263&command=NEW - Abre la ventana de cabecera de la factura de ventas en modo NEW 


---

Este trabajo es una obra derivada de [Enlaces profundos](http://wiki.openbravo.com/wiki/Deep_Linking){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.