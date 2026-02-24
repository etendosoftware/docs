---
title: Cómo informar de errores
tags:
    - Informe de errores
    - Etendo
    - Descripción del error
    - Plantilla de informe
---

## Plantilla para informar de errores

!!! warning
    *Esta estructura debe respetarse siempre para informar de un error en el [Centro de ayuda de Etendo](https://incidencias.atlassian.net/servicedesk/customer/portal/35/group/43/create/132){target="_blank"} .*

!!! sucess
    Recuerde reproducir el error previamente en un entorno limpio. La versión de Etendo debe estar soportada [Versión de Openbravo](../whats-new/release-notes/etendo-classic/release-notes.md)

Para informar de un error, debe seguirse una estructura estándar. Esta estructura se representa en la siguiente plantilla:

-   **Descripción del error**
     Descripción breve del error.
    
-   **Pasos para reproducir el error**
    Descripción detallada de la configuración y de los pasos que deben seguirse para reproducir el error. Puede incluir vídeos de pantalla y/o capturas de pantalla.
    
-   **Comportamiento esperado** 
    Descripción del comportamiento esperado sin el error.

-   **Versión afectada**
    Versión de **Etendo** en la que se produce el error.
    (*Navegador y versión - SO y versión*)

-   **Diseño de la solución (opcional)**
    Tras analizar el error, describa cómo se resolverá y, si es necesario, los detalles de la implementación.

-   **Otros casos de prueba**
    Si es necesario, añada más casos de prueba.
 
 ```
  # Descripción del error
  
  # Pasos para reproducir el error

  ### Configuraciones necesarias (si es necesario)

  1. <paso>
  2. <paso>
  ...
  
  # Comportamiento esperado

  # Versión afectada
  ¿Última/Específica?
  Número de versión:
  
  # Diseño de la solución (opcional)
  
  # Otros casos de prueba
  **Dado:**
  **Cuando:**
  **Entonces:**
 

 ```