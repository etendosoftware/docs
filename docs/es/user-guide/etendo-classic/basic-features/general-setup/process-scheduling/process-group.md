---
title: Grupo de Procesos
tags:
    - Grupo de Procesos
    - Secuencia
    - Planificación
---

# Grupo de Procesos

:material-menu: `Aplicación` > `Configuración General` > `Planificador de procesos` > `Grupo de Procesos`

## Visión general

Un **Grupo de Procesos** permite al usuario definir y planificar una secuencia de procesos que se ejecutarán uno tras otro como un único lote. Esto es útil para automatizar flujos de trabajo que requieren que varios procesos se ejecuten en un orden específico.

Cuando se planifica un Grupo de Procesos:

- Aparece una única entrada en las ventanas **Procesamiento de Peticiones** y **Monitor de Procesos**.
- Cada proceso dentro del grupo también aparece por separado en ambas ventanas con su propio registro y estado, independientemente de si se ejecutó correctamente o falló.

## Ventana Grupo de Procesos 

![alt text](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/process-scheduling/process-group.png)

Campos a tener en cuenta:

- **Nombre**: Identificador del grupo de procesos.
- **Descripción**: Información adicional sobre el grupo.
- **Prevenir ejecuciones concurrentes**: Cuando está habilitado, el sistema comprobará si ya se está ejecutando otra instancia del mismo grupo de procesos (para el mismo cliente y organización) antes de iniciar una nueva ejecución. Si se encuentra una, la ejecución se cancela y aparece un mensaje de error en el registro: "Intento concurrente de ejecución".
- **Detener la ejecución del grupo cuando un proceso falla**: De forma predeterminada, si un proceso del grupo falla, los procesos siguientes se seguirán ejecutando. Cuando se selecciona esta opción, la ejecución de todo el grupo se detendrá inmediatamente al producirse un fallo en un proceso.

    !!! info
        Esto es útil cuando los procesos dependen entre sí.

### Lista de Grupo de Procesos

Lista de procesos individuales, cada uno con un número de secuencia asignado que determina el orden de ejecución.

!!! failure "Resultado de error"
    Un grupo de procesos mostrará un resultado de error si tiene uno o más resultados de error en los procesos que conforman el grupo.

!!! failure "Grupos vacíos"
    No puede lanzar ejecuciones de grupos vacíos. Si lo intenta, recibirá este error: No hay procesos en el grupo: Nombre del Grupo.

!!!warning "Coexistencia de prevenir ejecución concurrente"
    La prevención de ejecuciones de procesos individuales y de procesos de grupo coexistirá. Esto significa que ninguno de ellos anula al otro y ambos pueden configurarse al mismo tiempo.

!!! tip "Permisos"
    Grupo de Procesos es una ventana, por lo que puede gestionar los permisos para la creación de Grupo de Procesos como desee: solo Sistema, algunos clientes, algunas organizaciones, algunos roles, entre otros.

---

Este trabajo es una obra derivada de [Configuración General](https://wiki.openbravo.com/wiki/General_Setup){target="_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="_blank"} por [Etendo](https://etendo.software){target="_blank"}.