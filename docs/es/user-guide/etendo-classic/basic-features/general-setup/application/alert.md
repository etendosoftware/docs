---
title: Alertas
tags:
    - Alertas
    - Notificaciones
    - Monitor
    - Regla de alerta
---

# Alertas

## Visión general

Las alertas son notificaciones que informan sobre eventos que ocurren siempre que se haya definido correctamente una regla de alerta para monitorizar dichos eventos.

A continuación se describe cómo funcionan las **Alertas** en Etendo:

- Las reglas de alerta deben definirse previamente como consultas SQL. Las consultas SQL definen el evento que se va a monitorizar.  
  Por ejemplo, *Productos sin un precio definido*, *Productos bajo stock* o *Cuenta bancaria sin información contable*
- Una regla de alerta puede aplicarse a todos los usuarios de Etendo o solo a un conjunto de ellos. Los receptores de alertas son los usuarios de Etendo para los que se va a monitorizar un evento determinado.
- Un proceso en segundo plano de Etendo comprueba permanentemente si la consulta SQL definida en cada una de las reglas de alertas activas devuelve algún registro.
  - Si ese es el caso, Etendo crea y devuelve una nueva *instancia de alerta*, que se guarda en la ventana *Gestión de Alertas* en estado *Nuevo*.

El *número de instancias de alertas* que informan sobre eventos monitorizados que están ocurriendo se muestra en el menú de **Navegación superior**:

![](../../../../../assets/drive/z341Sqx0_VIs2wSRDSm-6Jlq_2MmxWxxFa406LPjtgffjFTdFIds94ov5CwjlKGP7vDSEyxAdiYnVGN3m0AaIZjGIz2WkrZSmPlCagaI-KmACHhix0-qaazsTFjJ3D9sG0sTkbHv.png)


## Vista de alertas
Las instancias de alertas pueden visualizarse y gestionarse en la ventana *Gestión de Alertas*, que se abre haciendo clic en la opción **Alertas** del menú de Navegación superior.

![](../../../../../assets/drive/-wFUIZt2K33Chbp-czLqJmO7f1hP5fcD2jkcZaI7CtnhlHHbdh7lk1_ayiFKbrcfx8slOlIXVjeiIe15gmt_CkcTwhWQGhAbfXXGCMaF6-ba5l_OGBnMsKpP8CkL23o7AwzywwMX.png)

Las alertas pueden tener 4 estados diferentes:

- **Nuevo**: nuevas instancias de alertas que reflejan que los eventos monitorizados están ocurriendo.
- **Pendiente**: instancias de alertas reconocidas para las que está pendiente una acción del usuario final para resolverlas o corregirlas.
- **Ignorar**: instancias de alertas no aplicables que deben ignorarse.
- **Resuelto**: instancias de alertas resueltas, ya que el evento que ocurre está corregido o resuelto.

La forma de gestionar las instancias de alertas es seleccionarlas manualmente y moverlas al estado siguiente o anterior una vez que se hayan reconocido, ignorado o resuelto manualmente.

## Ventana Alertas
:material-menu: `Aplicación` > `Configuración General` > `Aplicación` > `Alertas`

La ventana Alertas permite la definición de reglas de alerta como consultas SQL que definen el evento a monitorizar y cómo se monitorizará.

![](../../../../../assets/drive/7FDlwrebuc8IysmRIryYm81mF7QPheC-khbM3NdpZUdAIlXzkhZMDvasxwUPYPDMEyJcP_oM5t16sfAW3ZOCyVNUmR8nE4WWZkLYexMWFuKDHaCb0j8Axa1AetNm9j5rEVq36Kri.png)

Las alertas se definen introduciendo los siguientes datos:

- El *Nombre* de la alerta, que es el evento a monitorizar.
- La consulta *SQL*.
- y la *Solapa* donde la instancia de alerta puede corregirse o resolverse.


### Traducción

Las alertas pueden traducirse a cualquier idioma requerido.

### Receptor de Alerta

![alt text](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/application/alert-recipient.png)

Las alertas pueden asignarse a usuarios o contactos específicos o a todos ellos.

!!! warning
    Si no se configura ningún *Rol* o *Usuario* en la *solapa Receptor de Alerta* de una alerta determinada, esa alerta se aplicará a cualquier usuario o rol de Etendo.

Etendo admite la notificación de alertas a usuarios o roles por correo electrónico: para ello, es necesario configurar correctamente el servidor, la cuenta y la contraseña del **correo electrónico** para la entidad correspondiente en la cabecera de la ventana [Entidad](../client/client.md#email-configuration), sección *Configuración del correo electrónico*.

### Alertas

La solapa Alertas lista los eventos que ocurren y que generan la alerta correspondiente.

![](../../../../../assets/drive/qRqaP9bx7a04XzXIrzdpZZ3eS3OaglF9SMM3xvRYaL3Vrkhcxz_EI5BxPbtrnQoW_DXad8d-_oQBJntpSgZdchM9RtWisxif2I3GWPM2Yda4XlbPG_kkWIqlvgDl5cvOObV43F4W.png)

---

Este trabajo es una obra derivada de [Configuración General](https://wiki.openbravo.com/wiki/General_Setup){target="_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="_blank"} por [Etendo](https://etendo.software){target="_blank"}.