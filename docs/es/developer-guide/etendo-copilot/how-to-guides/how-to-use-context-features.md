---
title: Uso de las funcionalidades de contexto de Etendo Copilot
tags:
    - Contexto
    - Copilot
---

# Uso de las funcionalidades de contexto de Etendo Copilot

## Visión general
Esta guía explica cómo utilizar las funcionalidades con reconocimiento de contexto de Etendo Copilot para mejorar las interacciones de usuario en Etendo Classic. Cubre cómo Copilot captura el contexto de ventana, registro y usuario, y cómo configurar prompts predeterminados para obtener respuestas personalizadas.

## Activación de Copilot

1. Abra cualquier ventana en Etendo (p. ej., Pedido de venta, Inventario).
2. Localice el **Botón de Copilot** en la barra de herramientas en la parte superior de la ventana.
3. Haga clic en el botón para iniciar la interfaz de Copilot.
4. Haga una pregunta o proporcione una instrucción (p. ej., "¿Qué información puede darme sobre esta ventana?").

!!! info
    El botón de Copilot está disponible en todas las ventanas de Etendo, lo que facilita acceder a la asistencia esté donde esté.
    
![alt text](../../../assets/developer-guide/etendo-copilot/how-to-guides/how-to-use-context-features/context.png)

## Comprender el contexto en Copilot

Copilot mejora sus respuestas capturando automáticamente el contexto en función de sus acciones en Etendo Classic. Admite tres tipos de contexto clave:

### 1. Contexto de ventana activa

Copilot identifica la ventana activa actualmente, como "Pedido de compra" o "Lista de productos", e incluye esta información en sus respuestas. Por ejemplo:

- **Acción**: Abra la ventana "Pedido de venta" y active Copilot.
- **Pregunta**: "¿Qué información puede darme sobre esta ventana?"
- **Respuesta**: Copilot proporciona detalles relacionados con la ventana "Pedido de venta".

### 2. Contexto de registro seleccionado

Cuando selecciona un registro en una lista o rejilla, Copilot captura sus detalles (p. ej., ID, nombre u otros campos relevantes) y utiliza estos datos para ayudarle. Por ejemplo:

- **Acción**: Seleccione un producto de la rejilla "Producto" y active Copilot.
- **Pregunta**: "¿Qué información puede darme sobre este registro?"
- **Respuesta**: Copilot devuelve información específica del producto seleccionado.

### 3. Contexto de registro editado

Si está editando un registro en un formulario, Copilot detecta el modo de edición del formulario y captura los valores de entrada actuales, incluidos los cambios no guardados. Por ejemplo:

- **Acción**: Edite un registro de "Terceros", cambie el nombre y active Copilot.
- **Pregunta**: "¿Qué información puede darme sobre este registro?"
- **Respuesta**: Copilot incluye el nombre actualizado y otros campos del formulario.

!!! tip
    Asegúrese de que la ventana o el registro correctos estén activos antes de hacer una pregunta a Copilot para obtener la respuesta más precisa.


## Configurar un prompt predeterminado
:material-menu: `Aplicación` > `Configuración General` > `Aplicación` > `Preferencias`

Puede personalizar Copilot configurando un prompt predeterminado que adapte su comportamiento a sus necesidades. Esto se realiza en la sección de Preferencias de Etendo Classic.

1. Vaya a la sección **Preferencias** en Etendo Classic.
2. Cree una nueva preferencia para **Prompt predeterminado de contexto de Copilot**
3. Introduzca un prompt usando placeholders como `@ORG_NAME@` o `@USERNAME@`. Por ejemplo:

``` title="Deafault Prompt"
You are working in the organization '@ORG_NAME@' (ID: @AD_ORG_ID@) under the client '@CLIENT_NAME@' (ID: @AD_CLIENT_ID@). You are logged in as @USERNAME@ (User ID: @AD_USER_ID@) with the role '@ROLE_NAME@' (Role ID: @AD_ROLE_ID@). The current warehouse in use is '@WAREHOUSE_NAME@' (Warehouse ID: @M_WAREHOUSE_ID@).
```

**Placeholders disponibles**

| Placeholder      | Sustituir por el valor                 |
| ---------------- | -------------------------------------- |
| @AD_CLIENT_ID@   | ID de cliente del usuario              |
| @CLIENT_NAME@    | Nombre de cliente del usuario          |
| @AD_ORG_ID@      | ID de la organización actual seleccionada   |
| @ORG_NAME@       | Nombre de la organización actual seleccionada |
| @AD_USER_ID@     | ID de usuario actual                   |
| @USERNAME@       | Nombre de usuario actual               |
| @AD_ROLE_ID@     | ID del rol seleccionado                |
| @ROLE_NAME@      | Nombre del rol seleccionado            |
| @M_WAREHOUSE_ID@ | ID del almacén seleccionado            |
| @WAREHOUSE_NAME@ | Nombre del almacén seleccionado        |

!!! info 
    Su prompt personalizado persiste entre sesiones, garantizando una experiencia consistente.

## Ejemplos de uso

A continuación se muestran ejemplos prácticos basados en escenarios reales:

### 1. Comprobar los detalles de la ventana

- **Escenario**: Está en la ventana "Pedido de compra".
- **Pasos**: Haga clic en el botón de Copilot y pregunte: "¿Qué información puede darme sobre esta ventana?"
- **Resultado**: Copilot describe el propósito de la ventana "Pedido de compra" y sus campos clave.

### 2. Analizar un registro seleccionado

- **Escenario**: Selecciona un registro de cliente en la rejilla "Terceros".
- **Pasos**: Haga clic en el botón de Copilot y pregunte: "¿Qué información puede darme sobre este registro?"
- **Resultado**: Copilot proporciona el ID, el nombre y otros detalles del cliente.

### 3. Revisar un registro editado

- **Escenario**: Está editando el precio de un producto en un formulario.
- **Pasos**: Haga clic en el botón de Copilot y pregunte: "¿Qué información puede darme sobre este registro?"
- **Resultado**: Copilot refleja el nuevo precio y otros campos editados.

### 4. Confirmar el contexto de usuario

- **Escenario**: Quiere verificar su prompt configurado.
- **Pasos**: Haga clic en el botón de Copilot y pregunte: "¿Cuál es mi contexto?"
- **Resultado**: Copilot devuelve su organización, rol y otros detalles del prompt predeterminado.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.