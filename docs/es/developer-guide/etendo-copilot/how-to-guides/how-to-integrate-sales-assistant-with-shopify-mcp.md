---
title: Cómo integrar un asistente de ventas con Shopify MCP
status: beta
tags: 
  - Cómo
  - Servidor MCP
  - Shopify
  - Asistente de ventas
  - Comercio electrónico
  - Integración de Copilot
  - Prompts de agente
---

# Cómo integrar un asistente de ventas con Shopify MCP

## Visión general

!!!example "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úselo **bajo su propia responsabilidad**. El comportamiento del módulo puede cambiar sin previo aviso. No lo utilice en entornos de producción.

Esta guía explica cómo configurar un **asistente de ventas inteligente** en **Etendo Copilot** que se conecta a un **servidor Shopify Model Context Protocol (MCP)** para ofrecer una experiencia de compra guiada y conversacional.

El asistente puede:

- Buscar en el catálogo de productos en tiempo real
- Recuperar información detallada de productos
- Gestionar el carrito de compra
- Acceder a políticas y preguntas frecuentes
- Proporcionar recomendaciones contextuales y consultivas

## Requisitos previos

- Etendo Copilot instalado y configurado
- Al menos un proveedor de LLM de OpenAI / compatible configurado (o un modelo interno mediante Ollama)
- Un endpoint de servidor Shopify MCP operativo que exponga herramientas (transporte HTTP o SSE)
- Acceso de red desde el backend de Copilot al endpoint de Shopify MCP

## Herramientas Shopify MCP compatibles (ejemplos)

Las implementaciones típicas de servidor Shopify MCP exponen herramientas similares a:

| Propósito | Nombre de herramienta de ejemplo |
|---------|-------------------|
| Búsqueda en el catálogo | `search_shop_catalog` |
| Detalles del producto | `get_product_details` |
| Estado del carrito | `get_cart` |
| Actualizar carrito | `update_cart` |
| Políticas y preguntas frecuentes | `search_shop_policies_and_faqs` |

Los nombres de las herramientas pueden variar según la implementación del servidor MCP. Confírmelo inspeccionando la respuesta de capacidades del servidor.

## Paso 1. Configurar el servidor Shopify MCP

:material-menu: `Aplicación` > `Servicios` > `Copilot` > `Configuración de servidores MCP`

1. Abra la ventana **Configuración de servidores MCP** (rol Administrador del sistema).
2. Cree un nuevo registro y pegue la configuración JSON.
3. Guarde. El sistema valida y normaliza la estructura.

### Ejemplos de configuración JSON

Configuración mínima basada en HTTP:

```json
{
  "mcp": {
    "servers": {
      "shopify": {
        "url": "https://your-shop.example/api/mcp",
        "transport": "streamable_http"
      }
    }
  }
}
```

## Paso 2. Vincular el servidor MCP a un agente

:material-menu: `Aplicación` > `Servicios` > `Copilot` > `Agente`

1. Abra (o cree) un agente.
2. Vaya a la pestaña **MCP**.
3. Añada un nuevo registro seleccionando la configuración de Shopify MCP.
4. Guarde.

## Paso 3. Redactar un prompt especializado

Proporcione instrucciones de comportamiento claras para que el asistente actúe como un vendedor digital consultivo.

Prompt base sugerido:

```text
You are a professional e-commerce sales assistant for a Shopify-powered store integrated into Etendo.
Objectives:

- Understand the user's intent (need, preference, constraints: price, category, use case).
- Use catalog search BEFORE answering if more context is required.
- When recommending products: list 3–5 options (if available) with: Name | Key benefit | Differentiator.
- When the user asks for differences: respond with a concise comparison table (textual) and a short recommendation.
- Always confirm before adding or updating cart items.
- Use cart tools to reflect real state before confirming.
- If policy / FAQ info is requested, call the policies/faq tool.
- Ask one clarifying question if intent is ambiguous.
- Avoid hallucinating unavailable products.
Tools to consider (call only when needed): search_shop_catalog, get_product_details, get_cart, update_cart, search_shop_policies_and_faqs.
Return final answers in clear, concise business English.
```

!!!tip "Ajuste del prompt"
    Itere en función de las transcripciones. Añada guardarraíles para precios, avisos de disponibilidad o lógica de upselling.

## Paso 4. Probar el asistente

1. Inicie una conversación con el agente configurado.
2. Pruebe primero consultas de descubrimiento (p. ej., *"Necesito una zapatilla de running ligera"*).
3. Solicite comparaciones (p. ej., *"Compare las dos primeras que sugirió"*).
4. Añada al carrito (p. ej., *"Añada la segunda zapatilla en talla 42"*). El agente debe llamar a `update_cart` tras la confirmación.
5. Pregunte por políticas (p. ej., *"¿Cuál es la política de devoluciones?"*).

## Conversación de ejemplo

**Usuario**: *"¿Qué producto recomienda para preparar café en casa?"*

**Agente**: *(Calls `search_shop_catalog`)*

*"Aquí tiene tres opciones: ... ¿Desea una comparación o más detalles de alguna de ellas?"*

**Usuario**: *"Compare las dos primeras."*

**Agente**: *(Calls `get_product_details` twice)*

*"Comparación: 1) Modelo A – Compacto | Calentamiento rápido | Ideal para principiantes. 2) Modelo B – Mayor capacidad | Control dual de temperatura | Mejor para experimentar. Recomendación: si valora la simplicidad, elija el Modelo A; para mayor control, elija el Modelo B."*

**Usuario**: *"Añada el Modelo B a mi carrito."*

**Agente**: *"Confirmar: ¿añadir el Modelo B (configuración por defecto) al carrito?"*

**Usuario**: *"Sí."*

**Agente**: *(Calls `update_cart`, then `get_cart`)*

*"Añadido. Su carrito ahora contiene: ..."*


## Páginas relacionadas

- [Model Context Protocol (MCP)](../concepts/model-context-protocol.md)
- [Cómo configurar servidores MCP en un agente de Etendo](how-to-configure-mcp-servers-on-agents.md)
- [Cómo crear un agente](how-to-create-an-agent.md)

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.