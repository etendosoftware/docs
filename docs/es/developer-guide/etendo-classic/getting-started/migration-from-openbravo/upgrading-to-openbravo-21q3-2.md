---
title: Actualización a Openbravo 21Q3.2
tags: 
    - Actualización
    - Openbravo
    - Versión objetivo
    - 21Q3.2
---

#Actualización a Openbravo 21Q3.2

## Visión general

Esta guía explica cómo actualizar su entorno actual de Openbravo a la versión 21Q3.2. Esto implica dos pasos principales:

-   Identificar y extraer los parches personalizados realizados en su versión actual de Openbravo
-   Actualizar a Openbravo 21Q3.2

!!! info
    Esta actualización es necesaria para migrar Openbravo a Etendo.

## Cómo actualizar a Openbravo 21Q3.2

!!! info "Requisitos"
    - Git  
    - Una herramienta de comparación/fusión si es necesario generar parches
    

### Identificar y extraer los parches personalizados realizados en su versión actual de Openbravo

1.  Clonar el repositorio core en la nueva versión

    ``` bash title="Terminal" 

    git clone --depth 1 --branch YOURVERSIONTAG git@gitlab.com:openbravo/product/openbravo.git
    ```

    !!! info
        Sustituya la etiqueta *YOURVERSIONTAG* por su versión actual de Openbravo, por ejemplo: 3.0PR19Q4

2.  Identificar los parches aplicados al core en la instalación actual, para volver a aplicarlos más adelante:

-   Utilice una herramienta de comparación como Meld o Kdiff3 para comparar las diferencias entre su entorno y el Openbravo estándar que acaba de clonar.
-   Extraiga los parches personalizados (evite generar parches para cambios que sean correcciones de errores, ya que deberían estar incluidos en la nueva versión).

### Actualizar a Openbravo 21Q3.2

1.  Clonar el repositorio core en la nueva versión:

    ``` bash title="Terminal" 

    git clone --depth 1 --branch 3.0PR21Q3.2 git@gitlab.com:openbravo/product/openbravo.git
    ```

2.  Configurar Openbravo.properties y otros archivos para que coincidan con su instalación actual.
3.  Copiar todos los módulos de su instalación anterior al nuevo entorno.
4.  Aplicar los parches extraídos en los pasos anteriores (puede que sea necesario adaptarlos a la nueva versión).
5.  Realizar una compilación completa:

    ``` bash title="Terminal" 

    ant update.database compile.complete.deploy
    ```

6.  Corregir problemas con módulos personalizados.

    !!! warning
        Consulte las [Notas de la versión de Openbravo](http://wiki.openbravo.com/wiki/Release_Notes/3.0PR21Q3.2){target="_blank"} para cambios en la API y otras consideraciones al actualizar.

7.  Iniciar el servidor.
8.  Probar si hay errores funcionales o de ejecución y corregirlos.


!!! success
    Su entorno está listo para ser migrado a Etendo.

    Consulte la [Guía de la herramienta de migración](/developer-guide/etendo-classic/getting-started/migration-from-openbravo/migrating-to-etendo-from-openbravo/).

---

Este trabajo es una obra derivada de la [Guía del desarrollador](https://wiki.openbravo.com/wiki/Category:Developers_Guide){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.