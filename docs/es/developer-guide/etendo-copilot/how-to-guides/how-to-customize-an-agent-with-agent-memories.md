---
title: Cómo personalizar un agente con memorias de agente
tags:
    - Copilot
    - Memoria de agente
    - Personalización
---

# Cómo personalizar un agente con memorias de agente

## Visión general
Esta guía explica cómo capturar y reutilizar reglas y conocimiento adquiridos en cualquier agente de Copilot mediante las ventanas de **Memoria de agente** entregadas con el módulo Etendo Copilot. Cada memoria que registre está vinculada a un agente específico y se inyecta automáticamente en sus respuestas según el contexto de su organización, rol y usuario.

## Requisitos previos
- Módulo Etendo Copilot instalado y sincronizado.
- Un agente de Copilot ya definido (consulte `Aplicación > Servicios > Copilot > Agente`).
- Rol con acceso a la entrada de menú **Memoria de agente**.
- Opcional: conocimiento de los roles de negocio que deberían recibir cada memoria.

## Ventana Memoria de agente
:material-menu: `Aplicación` > `Servicios` > `Copilot` > `Memoria de agente`

1. Abra la ruta de menú anterior. La ventana se divide en dos solapas: **Memoria de agente** (cabecera) y **Memoria** (detalle).
2. Use la cabecera para seleccionar el agente que desea enriquecer. Puede reutilizar filtros de búsqueda como *Nombre*, *Tipo de aplicación* o *Estado* para encontrar el agente correcto.
3. Cambie a la solapa **Memoria** para revisar o crear entradas asociadas al agente seleccionado.

![Ruta de menú Memoria de agente](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-customize-an-agent-with-agent-memories/how-to-customize-an-agent-with-agent-memories-1.png)

!!! info
	Puede mantener memorias de agente sin salir de Etendo, por lo que no es necesario editar archivos de configuración ni desplegar código.

Campos a tener en cuenta: 

- **Memoria de agente**: la cabecera lista cada agente de Copilot.
- Solapa **Memoria**: la solapa de detalle lista cada memoria adjunta al agente seleccionado. Cada registro representa una frase o párrafo que Copilot añadirá al prompt del usuario siempre que coincidan las reglas de filtrado. Los siguientes campos controlan el alcance:

    | Campo | Propósito | Cómo afecta a Copilot |
    | ----- | --------- | --------------------- |
    | **Organización** | Por defecto, la organización del agente; puede dejarse en blanco para una memoria global. | Copilot solo inyecta entradas que pertenezcan al árbol de organización actual, salvo que el valor esté vacío. |
    | **Activo** | Habilita o deshabilita la memoria sin eliminarla. | Las filas inactivas nunca llegan a la conversación, lo cual es útil para políticas estacionales. |
    | **Usuario** | Propietario de usuario opcional. Déjelo vacío para exponerlo a todos. | Solo el usuario seleccionado ve la memoria; `null` la hace disponible para todos los usuarios de ese agente. |
    | **Rol** | Filtro de rol opcional (admite roles heredados automáticamente). | Cualquier usuario que trabaje bajo el rol elegido (o un rol hijo) recibirá la indicación. |
    | **Campo de texto** | El contenido real que Copilot añadirá (hasta 4.000 caracteres). | Se muestra literalmente como viñetas en el contexto inyectado. |

    !!! tip
        Almacene afirmaciones cortas y orientadas a la acción ("Mencione siempre el SLA de entrega para la organización Norte") en lugar de párrafos largos. El gancho formatea cada memoria como una viñeta dentro de la sección `Use the following relevant previous information`, por lo que el texto conciso funciona mejor.

## Crear una nueva entrada de memoria
1. En la ventana **Memoria de agente**, seleccione el agente a personalizar.
2. Vaya a la solapa **Memoria** y haga clic en **Nuevo**.
3. Rellene los campos:
   - **Organización**: seleccione la organización más específica que deba ver la indicación. Déjelo en blanco solo para hechos corporativos de alcance global.
   - **Usuario** y **Rol**: opcionalmente restrinja la memoria. Mantenerlos vacíos hace que la entrada esté disponible para todos los que tengan permitido usar el agente.
   - **Campo de texto**: describa el conocimiento que Copilot debe recordar. Mencione identificadores o URLs si es necesario; el gancho no altera el texto.
4. Guarde el registro. La memoria se almacena al instante y queda disponible la próxima vez que el agente reciba una pregunta.
5. Repita para tantas entradas como sea necesario. Puede deshabilitar instrucciones obsoletas desmarcando **Activo** sin perder el historial.

!!! info
	Cuando coinciden múltiples memorias, Copilot las lista como viñetas bajo “Use the following relevant previous information.” Considere numerar procedimientos dentro del texto si el orden es importante.

## Editar o eliminar memorias
- **Editar**: cambie los campos de alcance (Organización, Usuario, Rol) para restringir o ampliar la aplicabilidad. Guarde para aplicar al instante.
- **Desactivar**: cambie el estado de la casilla **Activo** para dejar de inyectar la memoria manteniendo un rastro de auditoría.
- **Eliminar**: solo cuando esté seguro de que la instrucción no se reutilizará. 

## Usar el atajo #MEMORY# desde el chat
Además de la ventana de back-office, los usuarios avanzados pueden enviar recordatorios rápidos directamente desde el pop-up del chat de Copilot:

1. Abra cualquier conversación de Copilot.
2. Comience su mensaje con el token literal `#MEMORY#` seguido del texto que desea almacenar, por ejemplo:
   ```
   #MEMORY# Answer in Italian for me going forward.
   ```
3. Envíe el mensaje. Copilot reconoce el prefijo y almacena el texto con el agente, la organización, el rol y el usuario actuales.
4. Copilot responde con normalidad, pero la memoria guardada queda disponible inmediatamente para futuras solicitudes que coincidan con el mismo contexto.

!!! warning
	El atajo siempre guarda memorias en el agente con el que está chateando en ese momento. Cambie de agente antes de usar `#MEMORY#` si necesita persistir la instrucción en otro lugar.

Ejemplo:

- Está chateando con *Bastian* (el agente para la documentación de Etendo). Al enviar `#MEMORY# Always respond in Italian.`, la memoria se guarda bajo el agente *Bastian* y se utilizará en futuras interacciones con ese agente.

![Ejemplo de memoria guardada desde el chat](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-customize-an-agent-with-agent-memories/how-to-customize-an-agent-with-agent-memories-2.png)

![Conversación mostrando el uso de la memoria](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-customize-an-agent-with-agent-memories/how-to-customize-an-agent-with-agent-memories-3.png)

![Respuesta resultante en italiano](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-customize-an-agent-with-agent-memories/how-to-customize-an-agent-with-agent-memories-4.png)

## Buenas prácticas

- Prefiera memorias más pequeñas y componibles frente a una única instrucción monolítica; el gancho puede devolver muchas filas, y las viñetas cortas mantienen los prompts bajo control.
- Use **Usuario** para recordatorios personales y **Rol** para políticas departamentales. Las organizaciones pueden permanecer en **\*** para reglas de toda la empresa.
- Revise periódicamente las entradas inactivas para limpiar políticas obsoletas y mantener las respuestas de Copilot fiables.

---
Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L.](https://etendo.software){target="_blank"}.