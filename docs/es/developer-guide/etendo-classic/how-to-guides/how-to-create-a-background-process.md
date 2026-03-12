---
title: Cómo crear un Proceso en segundo plano
tags:
    - Cómo hacer
    - Proceso en segundo plano
    - Programación de procesos
    - Ejecutar más tarde
    - Desprogramar
---
  
#  Cómo crear un Proceso en segundo plano

##  Descripción general

Los Procesos en segundo plano son [Procesos](../../../developer-guide/etendo-classic/concepts/Processes.md) que se ejecutan sin la acción directa del usuario. Se pueden establecer diferentes reglas para programar cuándo se ejecuta el proceso.

Este documento trata sobre la infraestructura de Etendo para los Procesos en segundo plano: cómo definir, programar y monitorizar los Procesos en segundo plano.

##  Definir un Proceso en segundo plano

Los Procesos en segundo plano se definen en la ventana `General Setup` > `Process Scheduling ` > `Process Request`. Primero, en el campo *Proceso* seleccione el proceso a ejecutar y, en el campo *Programado*, cuándo se ejecutará.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Background_Process-0.png)
Dependiendo del *Programado* seleccionado, es necesario definir más campos para definir esta programación:

###  Ejecutar inmediatamente

Esta opción de programación ejecutará el Proceso en segundo plano solo una vez en el momento en que se pulse el botón para programar el proceso. Después de ser programado, se puede reprogramar tantas veces como sea necesario.

Esta opción es muy similar a ejecutar un proceso desde una opción de menú. La diferencia es que, al programar un Proceso en segundo plano de _Ejecutar inmediatamente_, no habrá ninguna ventana emergente que indique cuándo finalizó la ejecución y, en su lugar, su ejecución se registrará en el *Monitor de Procesos*.

### Ejecutar más tarde

Esta opción es similar a la opción anterior. En este caso, el Proceso en segundo plano se ejecutará solo una vez en un momento futuro.

El momento en el que se ejecutará el Proceso en segundo plano se define en los campos *Fecha inicio* y *Fecha fin*.

###  Programar

Esta es la opción más versátil, ya que permite ejecutar un Proceso en segundo plano de forma periódica. Estos son los campos utilizados para definir el plan de programación de un Proceso en segundo plano:

  * *Fecha inicio* y *Hora inicio*: define el momento en el que comenzará el plan de programación para este Proceso en segundo plano. 
  * *Frecuencia*: define la frecuencia con la que se ejecutará el Proceso en segundo plano. Puede ser *Cada n segundos*, *Cada n minutos*, *Cada hora*, *Diario*, *Semanal*, *Mensual* o *Expresión cron*. Dependiendo de la opción seleccionada, puede definir los detalles específicos para cada opción de frecuencia. 
  * *Fecha fin* y *Hora fin*: estos campos solo se pueden definir cuando se selecciona la opción *Finalizado*. Y define cuándo detener el plan de programación para este Proceso en segundo plano. 

###  Programar y desprogramar un Proceso en segundo plano

Después de que el Proceso en segundo plano se haya definido completamente, se puede programar pulsando el botón *Programar Proceso*. Cuando un proceso está programado, se ejecutará según las opciones de *Programado* seleccionadas, y cada ejecución se registrará en el Monitor de Procesos.

Para detener futuras ejecuciones de un Proceso en segundo plano, simplemente pulse el botón *Desprogramar Proceso*. Después de que un Proceso en segundo plano haya sido desprogramado, se puede programar de nuevo en cualquier momento pulsando el botón *Reprogramar Proceso*.

###  Monitorización de ejecuciones de Procesos en segundo plano

Todas las ejecuciones de Procesos en segundo plano se pueden monitorizar en `General Setup` > `Process Scheduling ` > `Process Monitor`.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Background_Process-1.png)

En esta ventana, hay una entrada por cada ejecución de Proceso en segundo plano y la información de cada ejecución. Los campos más importantes son:

  * *Proceso*: el Proceso ejecutado. 
  * *Hora inicio*, *Hora fin* y *Duración*: cuándo comenzó la ejecución, cuándo finalizó y el tiempo que tardó en completarse. 
  * *Estado*: el resultado final de la ejecución del Proceso. 
  * *Registro del Proceso*: la información registrada durante la ejecución del Proceso. Por ejemplo, si el *Estado* de la ejecución es _Error_, aquí en el *Registro del Proceso* se puede detectar el motivo del error. 

Este trabajo es una obra derivada de [Cómo crear un Proceso en segundo plano](http://wiki.openbravo.com/wiki/How_to_create_a_Background_Process){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.