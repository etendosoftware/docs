---
title: Cómo imprimir informes con subinformes
tags: 
    - Imprimir
    - Informes
    - Subinformes

status: beta
---

# Cómo imprimir informes con subinformes

!!! example "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.

## Visión general

En esta sección se explica cómo imprimir informes que incluyen subinformes.

## Pasos de ejecución

Existen tres formas posibles de imprimir informes que incluyen subinformes:

1. Usando el parámetro `$P{SUBREP_report_name}` para buscar automáticamente el subinforme que se mostrará. 

    Esta opción solo funciona en informes que han sido procesados usando el botón **Imprimir** en las ventanas **Factura de ventas/compras, Pedido de ventas/compras, Recepción/Envío de mercancías y Cobro/Pago**. En esos casos no es necesario incluir el `.jasper` del subinforme, ya que el `.jrxml` es suficiente, porque en el momento de la ejecución se compila y se pasa al informe principal como un parámetro.

2. La siguiente opción consiste en definir el `.jrxml` para un proceso (en la ventana **Informes y procesos**) y, a continuación, incluir este proceso en el menú.

    En este caso, la única opción posible es usar el subinforme precompilado (Jasper) y referenciarlo desde el `.jrxml` usando `BASE_DESIGN` seguido de la ruta del jasper. La principal desventaja de usar subinformes precompilados es que no se traducen en tiempo de ejecución, por lo que solo es posible tener el subinforme en un único idioma.

3. La última posibilidad es llamar a **renderJR** desde un servlet Java propio, compilando el `.jrxml` y pasándolo como un parámetro, tal y como se describe en el primer método. Esto se realiza en la clase **PrintController** (`PrintController.java`). 

---
Este trabajo es una obra derivada de [Cómo imprimir informes con subinformes](http://wiki.openbravo.com/wiki/How_to_Print_Reports_with_Subreports){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, usado bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.