---
title: Monitor de Procesos
tags:
    - Monitor de Procesos
    - Estado
    - Proceso en segundo plano
---

# Monitor de Procesos

:material-menu: `Aplicación` > `Configuración General` > `Planificador de procesos` > `Monitor de Procesos`

## Visión general

La ventana Monitor de Procesos permite **revisar el estado de los procesos** ejecutados por un usuario, así como los programados en la ventana de solicitud de proceso.

En otras palabras, hay dos tipos de procesos que se pueden monitorizar en esta ventana:

- Procesos **transaccionales**, como Generar coste medio o Generar facturas.
- Procesos **Es en segundo plano** programados en la solicitud de proceso.

En cualquier caso, solo los usuarios que tengan un rol con acceso a un proceso/procesos determinado(s) podrán monitorizarlo(s) en esta ventana.

Además, y tal y como ya se ha explicado, la definición de **Seguridad basada en el Rol** a nivel de solicitud de proceso permitirá definir los usuarios que podrán monitorizar un proceso en segundo plano determinado en esta ventana.


## Ventana Monitor de Procesos

La ventana Monitor de Procesos muestra información de solo lectura sobre la ejecución individual de procesos.

![](../../../../../assets/drive/1n5-1WsQVWLDXUzuynPBRi1mruhlS9uPb.png)

Tal y como se muestra en la imagen anterior, la ventana Monitor de Procesos proporciona la siguiente información por cada proceso ejecutado:

- Proceso
- Grupo de procesos
- Usuario que ejecuta el proceso
- Hora de inicio y fin
- Duración
- Estado
- Canal. Las opciones disponibles son:
    - Directo: proceso transaccional ejecutado manualmente por el usuario
    - Planificador de procesos: para procesos en segundo plano programados en la ventana Solicitud de proceso.
- Registro del proceso

### Procesos en Grupo

En caso de que el proceso ejecutado sea un grupo de procesos, aquí encontrará la información sobre las ejecuciones de los procesos del grupo.
 
![](../../../../../assets/drive/1-YKBRq-gs3FtBuSize6FhzqtgT17IZlE.png)

---

Este trabajo es una obra derivada de [Configuración General](https://wiki.openbravo.com/wiki/General_Setup){target="_blank"} de [Wiki de Openbravo](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="_blank"} por [Etendo](https://etendo.software){target="_blank"}.