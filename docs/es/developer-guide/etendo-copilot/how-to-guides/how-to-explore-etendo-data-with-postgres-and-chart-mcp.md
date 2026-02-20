---
title: Cómo explorar datos de Etendo con Postgres y Chart MCP
status: beta
tags:
  - Guía práctica
  - Etendo Copilot
  - MCP
  - Postgres MCP
  - Chart MCP
  - Analítica de datos
---

# Cómo explorar datos de Etendo con Postgres y Chart MCP

## Visión general

!!! example "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úselo **bajo su propia responsabilidad**. El comportamiento del módulo puede cambiar sin previo aviso. No lo utilice en entornos de producción.

Esta guía muestra cómo convertir datos transaccionales en bruto en Etendo en información inmediata y accionable usando **Etendo Copilot** junto con dos servidores de **Model Context Protocol (MCP)**:

- **Postgres MCP**: construye y ejecuta SQL dinámico sobre la base de datos de Etendo (sin necesidad de informes predefinidos).
- **Chart MCP**: genera visualizaciones inline rápidas (línea, barras, circular) directamente en la conversación de Copilot.

Usted plantea una pregunta de negocio en lenguaje natural. El agente:
1. Interpreta la intención.
2. Genera SQL (a través de Postgres MCP) dentro del alcance de seguridad permitido.
3. Recupera el conjunto de resultados.
4. Elige un tipo de gráfico adecuado (a través de Chart MCP).
5. Devuelve un breve resumen analítico junto con la visualización.

## Preguntas de negocio habituales

Ejemplos de prompts en lenguaje natural que se benefician de esta configuración:

- "Muestre la evolución mes a mes de compras y ventas del último año."  
- "Compare el importe total por cliente en el último trimestre."  
- "¿Qué porcentaje del total de ventas de enero representa cada producto?"  
- "Muestre el stock promedio de los últimos seis meses."  

## Valor para áreas funcionales

Sin esperar a un equipo de BI ni crear un informe a medida:

- Las reuniones se mantienen orientadas a datos y ágiles.
- Las decisiones se respaldan con cifras actuales, no con exportaciones desactualizadas.
- Etendo se convierte en una superficie interactiva de insights en lugar de ser solo un ERP transaccional.
- Mejora la adopción porque los datos se vuelven conversacionales e inmediatos.

## Arquitectura de un vistazo

```
Pregunta del usuario → Agente de Copilot → (Postgres MCP → SQL → Filas de resultado) → (Chart MCP → Visualización) → Respuesta consolidada
```

## Requisitos previos

- Etendo Copilot instalado y configurado.
- Acceso a la base de datos PostgreSQL de Etendo (se recomiendan credenciales de solo lectura).
- Dos configuraciones de servidor MCP creadas en Etendo Classic (rol System Administrator).

## Paso 1. Configurar Postgres MCP

Cree un nuevo registro de **Configuración del servidor MCP**.

**JSON de configuración recomendado (restringido)**:
```json
{
  "command": "uvx",
  "args": ["postgres-mcp", "--access-mode=restricted"],
  "env": {
    "DATABASE_URI": "postgresql://username:password@localhost:5432/etendo_db"
  }
}
```

### Notas

- Utilice un usuario de base de datos dedicado con los privilegios mínimos de solo lectura necesarios para consultas analíticas.
- El flag `--access-mode=restricted` ayuda a limitar la exposición de catálogos del sistema u objetos no deseados.
- Si su despliegue utiliza un host, puerto o nombre de base de datos diferente, ajuste `DATABASE_URI` en consecuencia.

!!! warning "Seguridad"
    Nunca exponga credenciales de escritura de producción. Utilice un usuario controlado de solo lectura. Aplique restricciones de red (firewall / VPC) según corresponda.

## Paso 2. Configurar Chart MCP

Cree un segundo registro de **Configuración del servidor MCP**.

**JSON de configuración**:
```json
{
  "command": "npx",
  "args": ["-y", "@xingjiexu/quickchart-mcp-server"]
}
```

### Notas

- Este servidor convierte los datos tabulares procedentes de Postgres MCP en gráficos rápidos.
- Selecciona automáticamente tipos de gráfico simples (línea, barras, circular) alineados con el patrón de datos.

## Paso 3. Vincular servidores MCP al agente

1. Abra la ventana **Agente** (System Administrator).
2. Seleccione (o cree) el agente de Copilot objetivo.
3. Vaya a la solapa **MCP**.
4. Añada ambos registros de servidor MCP (Postgres MCP y Chart MCP).
5. Guarde.

## Paso 4. Ajustar el prompt del agente

Asegúrese de que el prompt del sistema / base del agente indique la siguiente secuencia:

1. Primero: generar y ejecutar SQL seguro usando Postgres MCP para obtener estrictamente el conjunto de datos necesario.
2. Después: solicitar una visualización a Chart MCP eligiendo el tipo de gráfico más adecuado.
3. Por último: producir un resumen de negocio conciso junto con el gráfico.

Fragmento de prompt sugerido:

> Cuando un usuario solicite métricas, tendencias, comparaciones o composición:  
> 1) Use Postgres MCP para elaborar el SQL mínimo necesario.  
> 2) Valide el significado de las columnas (evite filtrar tablas irrelevantes).  
> 3) Use Chart MCP para generar un gráfico apropiado (línea para series temporales, barras para ranking, circular para composición).  
> 4) Devuelva: párrafo breve de insight + gráfico.  
> Si los datos son insuficientes, formule una pregunta de aclaración en lugar de suponer.

## Paso 5. Probar el flujo

Pruebe la siguiente conversación:

**Usuario**: "Muestre la evolución mes a mes de compras y ventas del último año."  
**Agente (interno)**: Genera SQL mediante Postgres MCP → Recibe filas con totales mensuales.  
**Agente (interno)**: Llama a Chart MCP → Produce un gráfico de líneas con dos series (Compras vs Ventas).  
**Agente (respuesta)**: Proporciona un insight: tendencia, picos, meses de desaceleración + gráfico.

## Lógica de selección de gráficos (heurística)

| Objetivo | Forma de los datos | Gráfico recomendado |
|------|------------|-------------------|
| Tendencia a lo largo del tiempo | Fecha + 1..N series numéricas | Línea |
| Ranking / Top N | Categoría + métrica | Barras |
| Composición (partes del total) | Categorías que suman el 100% | Circular |

!!! note
    Si el conjunto de datos es demasiado pequeño (p. ej., una sola fila) o un gráfico no aporta valor, el agente debería omitir la generación del gráfico y proporcionar únicamente un resumen textual.

## Resolución de problemas

| Síntoma | Causa posible | Acción |
|---------|----------------|--------|
| No se devuelven datos | Esquema incorrecto o usuario restringido | Valide la cadena de conexión y los permisos del usuario |
| No se genera el gráfico | Chart MCP no está vinculado | Verifique que la solapa MCP incluya Chart MCP |
| Error de SQL | Función no compatible o typo | Simplifique la consulta; reformule la pregunta |
| Se accede a una tabla sensible | El prompt no está acotando el alcance | Refuerce las instrucciones del prompt y restrinja los permisos de la BD |

## Buenas prácticas

- Mantenga el SQL mínimo (solo columnas y filas necesarias).
- Agregue en SQL, no en la capa de razonamiento del agente.
- Devuelva significado de negocio, no solo números.
- Registre las consultas en una tabla de auditoría segura para su revisión si el cumplimiento lo requiere.
- Rote periódicamente la contraseña de solo lectura de la base de datos.

## Ejemplo de respuesta combinada (abstracto)

```
Las ventas mensuales crecieron de forma constante en Q1–Q2, se estabilizaron en julio y cayeron un 8% en agosto antes de recuperarse. Las compras siguieron una curva similar, pero con un mes de retraso, lo que indica una suavización del inventario. Pico de ventas: junio. Pico de compras: julio.

[Gráfico de líneas inline multiserie]
```

## Limitaciones

- Los cálculos complejos de BI (asignaciones multinivel, modelos estadísticos avanzados) quedan fuera del alcance del emparejamiento básico Postgres + Chart MCP.
- Los conjuntos de resultados muy grandes pueden truncarse. Diseñe prompts que fomenten la agregación.
- Los estilos de los gráficos son intencionadamente simples (insight rápido > profundidad estética).

## Referencias relacionadas

- Concepto: [Model Context Protocol (MCP)](../concepts/model-context-protocol.md)
- Cómo configurar servidores MCP: [Cómo configurar servidores MCP en un agente de Etendo](how-to-configure-mcp-servers-on-agents.md)
- [Servidores MCP en GitHub](https://github.com/modelcontextprotocol/servers){target="_blank"}

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.