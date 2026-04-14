---
title: Formato XML
tags:
  - Configuración
  - Formato numérico
  - Configuración XML
  - Máscara de formato
  - Precisión decimal
  - Separador decimal
  - Límite de precisión
---

# Formato XML

## Visión general

`Format.xml` es un archivo de configuración para la instalación de Etendo que permite configurar el formato de salida para valores numéricos. Es utilizado por las diferentes **referencias numéricas** en el Diccionario de aplicación, pero también puede utilizarse en código **Manual**. Por defecto, Etendo incluye un `Format.xml.template` que puede copiarse tal cual sin ninguna modificación.

!!!info
    Si está construyendo Etendo desde el código fuente, el binario setup-properties crea una copia por usted.

## Ejemplo de Format.xml

```xml
    <?xml version="1.0" encoding="UTF-8" ?>
    <!-- license -->
    <Formats>
    <!-- other formats -->
       <Number name="euroEdition"
           decimal="." grouping="," formatOutput="#0.00" formatInternal="#0.00" />
    <!-- other formats -->
    </Formats>
```

### Atributo

  * **name**: Nombre del formato, utilizado para identificarlo.
  * **decimal**: Símbolo (carácter) que se utilizará como separador decimal.
  * **grouping**: Símbolo (carácter) que se utilizará como separador de agrupación (utilizado en miles).
  * **formatOutput**: Máscara de formato utilizada para enmascarar e imprimir entradas numéricas. Debe ser un tipo de formato de salida `DecimalFormat`: para más información, consulte la clase [DecimalFormat](https://docs.oracle.com/javase/tutorial/java/data/numberformat.html){target="\_blank"}.
  * **formatInternal**: Utilizado internamente por `XmlEngine`.

## Diccionario de aplicación - mapeo de nombre de formato

| AD Reference     | Formato de salida     |
|------------------|-----------------------|
| Decimal, Amount  | `euroEdition`         |
| Cantidad         | `qtyEdition`          |
| Precio           | `priceEdition`        |
| Entero           | `integerEdition`      |
| Número           | `generalQtyEdition`   |
| Otros numéricos  | `generalQtyEdition`   |

## Notas importantes

En última instancia, copie `$EtendoERP/config/Format.xml.template` como `Format.xml` y ejecute `./gradlew compile.complete -Dtab=xx -Dtr=no` porque, de este modo, los cambios serán permanentes y no se perderán en la siguiente reconstrucción.

## Exportar a formato CSV

La funcionalidad de exportación a CSV utiliza la información de `Format.xml` para dar formato a los datos (en concreto, utiliza el separador decimal definido para el sistema para los valores numéricos).

Esto puede sobrescribirse en caso de ser necesario, utilizando las siguientes preferencias:

  * **Separador decimal CSV**: si se define esta preferencia, se utilizará como separador decimal para los números.
  * **Separador de campo CSV**: si se define esta preferencia, se utilizará como separador de campo. En caso contrario, se utilizará una única coma `,`.
  * **Codificación de texto CSV**: si se establece esta preferencia, se utilizará como tipo de codificación del archivo generado. La codificación por defecto utilizada es Windows iso-8859-1, que funcionará correctamente en entornos Windows que utilicen Microsoft Excel. Otras codificaciones populares como UTF-8 pueden utilizarse en entornos Linux o Mac que utilicen otras hojas de cálculo.

Este trabajo es una obra derivada de [Format xml](http://wiki.openbravo.com/wiki/Format.xml){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.