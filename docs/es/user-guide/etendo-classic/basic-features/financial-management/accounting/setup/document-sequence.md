---
title: Secuencia de documento (numeración)
tags:
    - Documento
    - Secuencia
    - Gestión Financiera
    - Configuración
    - Contabilidad
---

# Secuencia de documento (numeración)

:material-menu: `Aplicación` > `Gestión Financiera` > `Contabilidad` > `Configuración` > `Secuencia de documento (numeración)`

## Visión general

Cada documento en Etendo puede numerarse y, por lo tanto, vincularse a una secuencia de documento.

Los "datos de referencia" de Etendo, incluida la lista estándar de tipos de documento, también incluyen una lista estándar de secuencias de documento vinculadas a aquellos documentos que tiene sentido numerar.

Las secuencias de documento "estándar" se listan en la ventana de secuencia de documento.

Es importante remarcar que:

-   es posible *cambiar las secuencias de documento "estándar"*, por ejemplo:
    -   el tipo de documento "Factura de proveedor" se crea por defecto vinculado a una secuencia de documento que está configurada como Numeración automática
    -   esa secuencia puede cambiarse desmarcando la casilla Numeración automática, lo que implicaría que los números de "Factura de proveedor" deberán introducirse manualmente de acuerdo con el número de factura del proveedor.
-   El escenario más común es que diferentes tipos de documento tengan diferentes secuencias de documento; sin embargo, también es posible que un conjunto de diferentes tipos de documento comparta la misma secuencia de documento para obtener la misma numeración consecutiva.

## Secuencia

La ventana de secuencia de documento (numeración) permite al usuario definir cómo se van a comportar las secuencias de documento.

![](../../../../../../assets/drive/1cqBJ-LRNEyws3SX80mIMk8SbXVlAmEKI.png)

Como se muestra en la imagen anterior, una secuencia de numeración de documentos puede configurarse como *"Numeración automática"*, lo que significa que el documento vinculado a esa secuencia obtendrá un número de documento generado automáticamente por la secuencia.

También es posible definir cómo se van a comportar las secuencias de documento de tipo "Numeración automática" en términos de:

-   cómo se va a *incrementar* la numeración
-   cuál va a ser el *siguiente número asignado*
-   si requiere un *prefijo* o un *sufijo* determinados

!!! info
    La lógica de numeración se aplica al guardar el documento.

## Secuencias enmascaradas

Las secuencias transaccionales y no transaccionales pueden utilizarse en cualquier documento y en cualquier campo.
En estas nuevas secuencias, las máscaras pueden añadirse con fechas dinámicas o cadenas.

El usuario puede filtrar la nueva secuencia según la organización, el tipo de documento y la máscara; la máscara es `#######` por defecto. Estas secuencias podrían crearse con el proceso `Create sequences` en la ventana `General Setup > Aplication > Create Sequences`.

![Creación de secuencias](../../../../../../assets/drive/1PP0CkomMyGlx20kQe3l7D0hW5Jn__2q-.png)

- Máscara: es una cadena para definir un formato de análisis, con la posibilidad de crear una fecha dinámica o una subcadena literal, además del número incremental formateado.

## Enmascaramiento de secuencias

El enmascaramiento de secuencias siempre utiliza una clave numérica para analizar la entrada. Por lo tanto, la máscara debe tener al menos el mismo número de caracteres '#' o '\*' que la longitud del campo `Next Assigned Number`. (Siete es la longitud de este campo por defecto)

### Formato de fecha y hora

| Letra | Tipo | Presentación | Ejemplos |
| :--- | :--- | :--- | ---: |
| G   | Designador de era | Texto | AD  |
| y   | Ejercicio | Ejercicio | 1996; 96 |
| Y   | Ejercicio de semana | Ejercicio | 2009; 09 |
| M   | Mes en el año | Mes | July; Jul; 07 |
| w   | Semana en el año | Número | 27  |
| W   | Semana en el mes | Número | 2   |
| D   | Día en el año | Número | 189 |
| d   | Día del Mes | Número | 10  |
| F   | Día de la semana en el mes | Número | 2   |
| E   | Nombre del día en la semana |     | Tuesday; Tue |
| u   | Número de día de la semana (1 = lunes) | Número | 1   |
| a   | Marcador am/pm | Texto | PM  |
| H   | Hora del día (0-23) | Número | 0   |
| k   | Hora del día (1-24) | Número | 24  |
| K   | Hora en am/pm (0-11) | Número | 0   |
| h   | Hora en am/pm (1-12) | Número | 12  |
| m   | Minuto en la hora | Número | 30  |
| s   | Segundo en el minuto | Número | 55  |
| S   | Milisegundo | Número | 978 |
| z   | Zona horaria | Zona horaria general | Pacific Standard Time; PST; GMT-08:00 |
| Z   | Zona horaria | Zona horaria RFC 822 | \-0800 |
| X   | Zona horaria | Zona horaria ISO 8601 | \-08; -0800; -08:00 |
| ‘ ’ | Literal | Texto |     |

### Formato de análisis

| Letra | Tipo | Presentación | Ejemplos |
| :--- | :--- | :--- | ---: |
| ##   | Clave de dígito | Dígito | 9   |
| !   | Clave literal | Literal |     |
| l   | Minúscula | Carácter | a   |
| x   | Hexadecimal | Número | 10F |
| U   | Mayúscula | carácter | A   |
| A   | *Alfanumérico* | Número | h0l4 |
| ?   | Carácter | Carácter | h   |
| \*  | Cualquier cosa | \*  | \*  |

!!! info
    El análisis se resuelve en dos pasos: primero las fechas y después los tipos. Por este motivo, si se utilizan caracteres de formato de análisis como ‘l’, ‘x’, ‘U’ o ‘A’, debe utilizarse el carácter ‘!’ para escapar cada carácter.

## Ejemplos

| Máscara | Entrada | Resultado |
| :--- | ---: | ---: |
| ##-### | 1   | 00-01 |
| #!### | 12  | 1#2 |
| ##-'YE!AR'-### | 21  | 00-YEAR-21 |
| yy-MM-dd/### | 1   | 21-08-31/01 |
| y-#### | 25  | 2021-025 |

---

Este trabajo es una obra derivada de [Secuencia de documento (numeración)](https://wiki.openbravo.com/wiki/Document_Sequence){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.