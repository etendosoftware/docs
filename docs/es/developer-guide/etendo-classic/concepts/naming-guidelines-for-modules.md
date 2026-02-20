---
title: Directrices de nomenclatura para módulos
tags:
    - Nomenclatura de Módulos
    - Directrices de Etendo
    - Reglas de marca de Módulos
    - Convenciones de idioma
    - Tipos de Módulos
---
## Introducción

Es importante seleccionar un nombre apropiado para su módulo con el fin de facilitar que los usuarios lo reconozcan tanto en Forge como en la ventana de Gestión de Módulos Empresariales.

En el futuro, Etendo también puede utilizar estas convenciones de nomenclatura para categorizar automáticamente los módulos en función de las etiquetas; por lo tanto, es importante que se sigan estas convenciones de nomenclatura.

A continuación se presenta un conjunto de directrices de nomenclatura que solicitamos a los autores de módulos que sigan:

## Reglas de marca

- El nombre del módulo debe coincidir con el nombre del proyecto en Forge (opcional)
- Los nombres de los módulos no deben tener más de 5 o 6 palabras y deben tener menos de 60 caracteres (opcional)
- Los nombres de los módulos no pueden contener la palabra "Etendo"
    - Servicios web JSON REST: :white_check_mark:
    - Etendo Servicios web JSON REST: :no_entry:
- Excepción a la regla anterior: módulos que Etendo decide comercializar como productos en lugar de como módulos:
    - Etendo QuickStart Template: :white_check_mark:
- No es necesario especificar la versión de Etendo en el nombre del módulo:
    - Traducción: Arabic Saudi Arabia (ar_SA): :white_check_mark:
    - Traducción: Arabic Saudi Arabia (ar_SA) for Etendo 2.50: :no_entry:
- Los nombres de los módulos no deben contener la palabra "Módulo"
    - Copiar rol: :white_check_mark:
    - Módulo Copiar rol: :no_entry:

## Convenciones de idioma y gramática

- Todos los nombres de los módulos deben estar en inglés. La descripción y la ayuda del módulo pueden estar en cualquier otro idioma.
- Se aceptan nombres propios no ingleses como parte de un nombre de módulo especificado en inglés
    - Informe fiscal: Modelo 349 (Spain): :white_check_mark:
    - Informe fiscal: Form 349 (Spain): :no_entry: (justificación: Modelo 349 es un nombre propio y no debe traducirse)
    - Informe Fiscal: Modelo 349 (Spain): :no_entry:
- La ayuda del módulo debe diferir de la descripción del módulo
- Gramaticalmente, los nombres de los módulos deben tratarse como nombres propios y debe ponerse en mayúscula la primera letra de cada palabra del nombre del módulo (con la excepción de palabras cortas y acrónimos)
    - Carga inicial de datos: :white_check_mark:
    - Carga inicial de datos: :no_entry:
    - Forma de pago de domiciliación bancaria: :white_check_mark:
    - Forma de pago de Domiciliación Bancaria: :no_entry:
    - Códigos de país ISO de tres dígitos: :white_check_mark:
    - Códigos de país ISO de tres dígitos: :no_entry:
- Debe evitar el uso de caracteres numéricos para expresar cantidades (son aceptables en códigos y fechas)
    - Códigos de país ISO de tres dígitos: :white_check_mark:
    - Códigos de país ISO de 3 dígitos: :no_entry:
    - Plan contable - PGC 2007 General: Spain: :white_check_mark:
    - Informe fiscal: Modelo 349 - Spain
- Los nombres de los módulos no deben terminar con un punto:
    - Carga inicial de datos: :white_check_mark:
    - Carga inicial de datos.: :no_entry:
- La descripción del módulo debe terminar con un punto
    - Generador de declaraciones de impuestos. Traducción al español (español España) del módulo Tax Report Launcher.: :white_check_mark:
    - Generador de declaraciones de impuestos. Traducción al español (español España) del módulo Tax Report Launcher: :no_entry:

## Tipos específicos de módulos

- Las traducciones del core (traducción de Etendo Core) deben seguir la convención:
    - "Traducción: $LANG $COUNTRY ($CODE)"
    - Traducción: Arabic Saudi Arabia (ar_SA) :white_check_mark:
- Las traducciones de módulos (traducciones de módulos distintos de Etendo Core) deben seguir la convención:
    - "$MODULE NAME Traducción: $LANG $COUNTRY ($CODE)"
    - Tax Report Launcher Traducción: Spanish Spain (es_ES) :white_check_mark:
- La descripción de las traducciones de módulos debe incluir una traducción adecuada del nombre del módulo en el idioma de destino, así como tanto el nombre del idioma como el nombre del país en el idioma de destino:
    - + Nombre: Tax Report Launcher Traducción: Spanish Spain (es_ES) + Descripción: Generador de declaraciones de impuestos. Traducción al español (español España) del módulo Tax Report Launcher. :white_check_mark:
- Los módulos de plan contable deben seguir la convención:
    - "Plan contable: $COUNTRY"
    - Plan contable: France :white_check_mark:
- Para países con múltiples planes contables, utilice las convenciones
    - "Plan contable: $TYPE - $COUNTRY"
    - Plan contable: PGC 2007 General - Spain :white_check_mark:
    - Plan contable: PGC 2007 PYMEs - Spain :white_check_mark:
- Los módulos de configuración de impuestos deben seguir la convención:
    - "Configuración de impuestos: $COUNTRY"
    - Configuración de impuestos: France :white_check_mark:
- Los módulos de informes fiscales deben seguir la convención:
    - "Informe fiscal: $FORM_NAME - $COUNTRY"
    - Informe fiscal: Modelo 347 - Spain :white_check_mark:
- Los módulos de regiones deben seguir la convención:
    - "Regiones: $COUNTRY"
    - "Regiones: Brazil" :white_check_mark:
    !!! note
        Siempre que las regiones de un país se denominen de otra forma distinta de regiones, puede usar el término :white_check_mark: en la descripción del módulo. Ejemplo: + Nombre: Regiones: United States of America + Descripción: US states.
- Los módulos de informes (distintos de los informes fiscales) deben seguir la convención:
    - "Informe: $REPORT_NAME"
    - Informe: Envíos pendientes de facturar :white_check_mark:
- Los módulos de skin deben seguir la convención:
    - "Skin: $SKIN_NAME"
    - Skin: Blue Sea :white_check_mark:
- Los módulos de tutorial (proporcionados como ejemplos para ilustrar cómo desarrollar módulos) deben seguir la convención:
    - "Tutorial: $TUTORIAL NAME"
    - Tutorial: Solitaire :white_check_mark:

## Bundles

- No utilice "módulo" en los bundles; todo es un módulo (incluido el core), por lo que sería redundante.
- En general, los módulos no deben usar subpaquetes de otros módulos, ya que podría crear un conflicto. En particular, no utilice subpaquetes para módulos incluidos en un pack (p. ej., varios módulos del pack de localización española usan como paquete un subpaquete del paquete del pack de localización española). Esa inclusión se declara en el propio pack y el uso de subpaquetización crearía una especie de redundancia (el módulo podría sacarse del pack más adelante) o podrían incluirse más adelante módulos originalmente no diseñados para el pack.
- El único caso en el que un subpaquete tiene sentido son las traducciones, ya que esa relación no puede cambiarse.
Para las traducciones, no utilice la palabra "traducción", sino directamente el código de idioma: translatedmodulepackage.languageCode (p. ej., org.openbravo.document.massinvoicing.es_ES).
- Para las traducciones del core, no funciona (org.openbravo.es_ES) porque el paquete del core no es lo suficientemente claro. En ese caso, use org.openbravo.coretranslation.es_ES o simplemente org.openbravo.core.es_ES)
- No utilice el "tipo de artefactos" incluido en el módulo para el empaquetado (p. ej., org.openbravo.report.xxx u org.openbravo.callout.xxx son incorrectos). El contenido de un módulo no debe definirse por los "componentes técnicos" utilizados para implementarlo, sino por el objetivo funcional del módulo. Puede ocurrir que el objetivo funcional pueda alcanzarse de una manera diferente y no debería forzar un reempaquetado.
- En algunos casos, las categorías funcionales y técnicas son las mismas (p. ej., informe); en este caso, ponga la palabra "informe" en el nombre del módulo, pero no como paquete (p. ej., org.openbravo.financial.taxreportXX en lugar de org.openbravo.financial.report.taxXX)
- Un paquete para un módulo desarrollado por Etendo y su personal debería ser:
org.openbravo.functionalcategory.modulename

    - En algunos casos, tiene sentido utilizar un nivel adicional:
        org.openbravo.functionalcategory.functionalsubcategory.modulename

    - Utilice un conjunto común de categorías funcionales y subcategorías (cuando sea necesario). Cada equipo scrum define su propia lista de categorías y subcategorías. Este es un punto de partida (dividido por equipos):

        - applicationdictionary (platform)
        - kernel (platform)
        - utility (platform)
        - setup (erp engineering)
        - common (erp engineering)
        - document (erp engineering)
        - warehouse (erp engineering)
        - project (erp engineering)
        - production (erp engineering)
        - mrp (erp engineering)
        - financial (erp engineering)
        - erputil (erp engineering)
        - localization (localization) ->  subcategorías para cada país (p. ej., localization.spain)
        - localizationutil (localization)
        - quickstart (industry templates / verticals are a category by itself)
        - quickstartspain (industry templates / verticals are a category by itself)

## Elección de un db_prefix

### Módulos creados por Partners
- Use un db_prefix que no comience por las letras ET
- EM es una palabra reservada no permitida como db_prefix

### Módulos creados por Etendo y su personal
- Use un db_prefix ETX donde X: de uno a 5 caracteres para el propio módulo

### Módulos de personalización
- Use un db_prefix que comience por CUST

Normalmente, los módulos de personalización no están pensados para publicarse en Central Repository. En este caso, DBPrefix debe comenzar por CUST. Los módulos con este tipo de DBPrefixes no pueden registrarse en Central Repository, pero son seguros frente a colisiones porque ningún otro módulo en Central Repository puede usar este DBPrefix. Esta es una decisión importante que debe tomarse antes de comenzar el desarrollo del módulo: en caso de que exista alguna posibilidad de publicar el módulo en algún momento, debe seguir la regla estándar; si está absolutamente seguro de que no se publicará, puede usar CUST y no registrarlo.