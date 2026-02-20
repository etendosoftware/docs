---
title: Ciclo de versiones de Etendo

tags:
  - Ciclo de versiones de Etendo
  - Fases de la versión
  - QA
  - Aseguramiento de la calidad
  - Análisis de código
  - Snyk
  - Análisis de vulnerabilidades y obsolescencia
---

# Ciclo de versiones de Etendo

La fase de lanzamiento abarca todos los pasos necesarios para entregar una versión exitosa al mercado, incluyendo (entre otros):

- pruebas de aseguramiento de la calidad (QA)
- pruebas de early adopters (programa de Innovadores)
- y formación

Las soluciones de Etendo se publican de forma trimestral.

- YX es el año y QZ el trimestre del año.

![new-etendo-lifecycle](../assets/whats-new/etendo-release-cycle/new-etendo-lifecycle.png)

Como se muestra en la imagen anterior, la duración de un ciclo de versión es de nueve meses. Por ejemplo, y en el caso de Etendo Y1Q4, las actividades de desarrollo comenzaron en julio y finalizarán con la publicación de la versión en marzo.

## Fases de la versión

El proceso de publicación consta de las siguientes fases: 

- **Ciclo de desarrollo de 3 meses:** el equipo de ingeniería se centra en el desarrollo de código, revisión, pruebas e integración.
- **Ciclo de QA de 3 meses:** el equipo de QA prueba y valida la versión según el Plan de Pruebas, crea la documentación de usuario y forma al equipo de soporte.
- **Programa de Early Adopters de Etendo de 3 meses:** la versión se publica inicialmente como QA Approved (QAA). Esta fase incluye un ciclo de maduración para evolucionar la versión desde QA Approved (QAA) hasta Confirmed Stable (CS).

![etendo-release-cycle-phase.png](../assets/whats-new/etendo-release-cycle/etendo-release-cycle-phase.png)

!!! note
    Etendo recomienda encarecidamente que solo se utilicen en entornos de producción las versiones que hayan alcanzado el estado CS.

En resumen, Etendo publicará versiones Confirmed Stable (CS) en marzo, junio, septiembre y diciembre de cada año.

!!! info
    Etendo dará soporte a las versiones del año en curso y del año anterior.

### Pruebas de Early Adopters (programa de Innovadores)

Como ya se ha mencionado, Etendo ha establecido un programa de innovadores basado en un ciclo de maduración para evolucionar las versiones de Etendo desde QAA hasta Confirmed Stable, en colaboración con un conjunto de clientes finales de Etendo.

Estos clientes instalan las versiones en estado QAA para utilizarlas y ayudar a Etendo a madurarlas.

Las versiones QAA han superado pruebas automatizadas, todos los problemas corregidos se han verificado individualmente y el equipo de QA ha completado un conjunto de pruebas manuales para identificar mejoras adicionales.

Cuando alcanza la fase QAA, la versión todavía no está disponible para un público amplio, pero ya puede utilizarse con fines de producción para quienes tengan un interés particular, asegurando explícitamente la plena alineación con el cliente final.

Como parte del programa de Innovadores, los Partners interesados recibirán soporte en el proceso de actualización del entorno de producción de un cliente a la versión actual QA Approved.

### Versiones de emergencia

Cuando sea necesario, existen versiones de emergencia fuera de calendario que se utilizan para la corrección dirigida de errores muy importantes. Estos errores pueden haber sido reportados por nuestros partners, miembros del equipo de desarrollo o simplemente errores encontrados por nuestras automatizaciones que prueban periódicamente nuestros productos.

Estas versiones pueden identificarse por su versión, que se construye de la siguiente manera: ETXXQY.Z, donde:

- XX es el año de la versión base
- QY es el trimestre de la versión base
- Z es un dígito menor que comienza en 1

y seguirán el mismo estado de madurez y proceso de publicación.

## Aseguramiento de la calidad

En Etendo, llevamos a cabo procesos constantes para garantizar la calidad y la seguridad de nuestro producto a lo largo de todo el ciclo de desarrollo. A continuación se indican los principales pasos de nuestro proceso de aseguramiento de la calidad.

### Análisis de código

Cuando se realizan cambios o incorporaciones de código, este se somete a un análisis exhaustivo utilizando las siguientes herramientas:

- **Sonar:** nuestros repositorios de desarrollo emplean reglas de Sonar para analizar el código en pull requests creadas o actualizadas. Sonar identifica posibles problemas y realiza sugerencias para mejorar la calidad del código.

![sonar-review.png](../assets/whats-new/etendo-release-cycle/sonar-review.png)

- **Revisor automático de código:** hemos desarrollado una herramienta llamada Auto Code Reviewer, que utiliza ChatGPT para analizar los cambios realizados en la Pull Request y hacer sugerencias. Esta herramienta complementa el análisis de Sonar y nos ayuda a mantener altos estándares de calidad en nuestro código y arquitectura.

### Pruebas automatizadas

Una vez que se ha creado o actualizado una pull request, se ejecutan pruebas automatizadas utilizando Jenkins, nuestro sistema de integración continua. Mediante un job programado en Jenkins, se ejecutan los siguientes tipos de pruebas:

- **Pruebas de compilación:** en esta etapa, comprobamos que el código se compila correctamente, identificando posibles errores en tiempo de compilación.
- **Prueba unitaria:** ejecutamos pruebas automatizadas diseñadas para verificar el comportamiento y la funcionalidad de unidades individuales de código. Estas pruebas nos ayudan a identificar errores y a garantizar el correcto funcionamiento de las diferentes partes del sistema.

![jenkins-develop-branch.png](../assets/whats-new/etendo-release-cycle/jenkins-develop-branch.png)

Si se detectan errores en cualquiera de estas pruebas automatizadas, se notifica inmediatamente al equipo de desarrollo para que pueda abordarlos y corregirlos.

Una vez que una pull request ha superado la revisión de código y los procesos de aseguramiento de la calidad específicos de cada desarrollo, se realiza el merge a la rama "develop". En este punto, se vuelven a ejecutar pruebas automatizadas para asegurar que la integración del código no ha introducido nuevos problemas.

En línea con las pruebas automáticas que se realizan, disponemos de pruebas de estrés y de interfaz que se ejecutan mensualmente:

- **Pruebas de estrés:** además de las pruebas automatizadas habituales, realizamos pruebas de estrés en nuestras aplicaciones de forma mensual. Estas pruebas nos ayudan a identificar posibles cuellos de botella, limitaciones de recursos y áreas que pueden causar degradación o fallos bajo cargas elevadas de usuarios. Al simular interacciones concurrentes de usuarios y generar alto tráfico, evaluamos la capacidad de respuesta del sistema, su escalabilidad y su robustez general. Realizar estas pruebas mensualmente garantiza que nuestras aplicaciones puedan gestionar el aumento de la demanda de usuarios y mantener un rendimiento óptimo.
- **Pruebas de interfaz con Selenium:** para garantizar la funcionalidad y la experiencia de usuario de nuestras aplicaciones, realizamos pruebas mensuales de interfaz con Selenium. Selenium nos permite automatizar interacciones del navegador y ejecutar pruebas en distintos navegadores web, como Firefox y Google Chrome. Con Selenium, creamos scripts de prueba que simulan acciones de usuario, navegan por la interfaz de la aplicación y verifican que todos los elementos y funcionalidades funcionan según lo esperado. Esto garantiza la consistencia entre distintos navegadores y nos ayuda a identificar posibles problemas de compatibilidad que puedan surgir. Realizar estas pruebas mensualmente nos permite detectar posibles incidencias de interfaz y asegurar una experiencia de usuario fluida en diversas plataformas.

### Análisis de vulnerabilidades y obsolescencia

De forma trimestral, ejecutamos herramientas de Static Application Security Testing (SAST) y Software Composition Analysis (SCA) para detectar posibles vulnerabilidades u obsolescencias en las librerías y el stack que utilizamos. Este análisis nos permite mantener nuestra aplicación actualizada y segura. En función de los resultados de esta herramienta, iniciamos el proceso de actualización correspondiente, considerando el nivel de prioridad asignado a cada cambio identificado.

![vulnerability-and-deprecation](../assets/whats-new/etendo-release-cycle/vulnerability-and-deprecation-2.png)

- **Actualización con cambios de API (mayor):** este tipo de actualización implica cambios significativos en la interfaz de programación de aplicaciones (API). Una actualización mayor generalmente conlleva modificaciones sustanciales en la forma en que los componentes o módulos del sistema interactúan entre sí, lo que puede requerir cambios extensos en el código existente para hacerlo compatible con la nueva versión. Estos cambios pueden incluir la introducción de nueva funcionalidad, la eliminación de características obsoletas y cambios en la estructura de datos o en los protocolos de comunicación. Debido a la naturaleza de estos cambios, una actualización mayor se programa una vez al año para disponer de tiempo suficiente para planificar, probar y realizar las modificaciones necesarias en el código y en los sistemas que utilizan la API actualizada.
- **Actualización suave:** en una actualización suave, los cambios realizados son menores, no son significativos para la API y, por lo general, se centran en mejoras de rendimiento, corrección de errores, optimización del código existente o actualización de dependencias externas. Estos cambios son menos disruptivos y pueden implementarse con mayor frecuencia, por lo que se realiza una actualización suave de forma trimestral para mantener el sistema al día y aprovechar mejoras continuas. Aunque los cambios no son drásticos, se siguen recomendando pruebas exhaustivas para garantizar la estabilidad y la compatibilidad con dependencias y componentes relacionados.
- **Actualización CRÍTICA:** una actualización crítica aborda una vulnerabilidad o incidencia de seguridad importante que podría ser explotada por atacantes para comprometer la integridad, confidencialidad o disponibilidad del sistema. Este tipo de actualización se considera una emergencia y debe implementarse rápidamente mediante la publicación de un hotfix para resolver el problema de seguridad en el menor tiempo posible. Las actualizaciones críticas pueden incluir parches de seguridad, soluciones temporales o mitigaciones para evitar la explotación de la vulnerabilidad mientras se trabaja en una solución más completa.

---

#### Integración de Snyk en el análisis de vulnerabilidades

![snyk-banner.png](../assets/whats-new/etendo-release-cycle/snyk-banner.png)
En Etendo, estamos comprometidos a garantizar la seguridad de nuestras aplicaciones en todo momento. Por eso, una de las herramientas destacadas que utilizamos es _[Snyk](https://snyk.io/)_, una potente solución de Software Composition Analysis (SCA).

_Snyk_ nos permite realizar un análisis integral de las librerías y dependencias utilizadas en nuestro stack de aplicaciones. Al integrar nuestros repositorios con _Snyk_, obtenemos visibilidad detallada sobre posibles vulnerabilidades y obsolescencias que puedan existir en nuestro código.

_Snyk_ es ampliamente reconocido por su capacidad para identificar vulnerabilidades en dependencias de software de forma precisa y rápida. A través de _Snyk_, podemos realizar un análisis continuo y en tiempo real de nuestras dependencias, lo que nos permite detectar cualquier problema de seguridad de manera temprana y tomar medidas proactivas para abordarlo.

La integración con _Snyk_ nos proporciona información detallada sobre cada vulnerabilidad u obsolescencia identificada, incluyendo descripciones, niveles de severidad y recomendaciones específicas para su resolución. Esta información es invaluable, ya que nos permite evaluar y priorizar los cambios necesarios en función de su impacto potencial en nuestra aplicación.

En función de los resultados del análisis de _Snyk_ y de otras herramientas de seguridad, iniciamos el proceso de actualización correspondiente, considerando el nivel de prioridad asignado a cada cambio identificado. Este enfoque nos permite gestionar eficazmente los riesgos de seguridad y mantener nuestra aplicación actualizada y segura para nuestros usuarios.

## Notas de la versión de Etendo

Cada vez que Etendo publica una nueva versión, todo lo que contiene se documenta en la página wiki correspondiente de Notas de la versión.  
Es importante destacar que, dentro de la página wiki de notas de la versión de Etendo, existen enlaces directos a lo que incluye una versión determinada.  
Las nuevas versiones de Etendo pueden incluir:

- nuevas funcionalidades implementadas según la hoja de ruta del producto correspondiente,
- correcciones de incidencias reportadas por partners de Etendo, corregidas por Etendo de acuerdo con el acuerdo de nivel de servicio correspondiente de los servicios para partners de Etendo,
- y extensiones, módulos que amplían la funcionalidad de Etendo.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.