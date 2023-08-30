---
title: Platform Extensions Bundle | Technical Documentation
---
## Overview

This bundle includes enhancements for platform functionalities in Etendo.

The Platform Extensions bundle includes the following modules:

-   **Print Document Web Service**: It allows downloading a PDF from some transaction documents using a web service and returning a PDF with the order, invoice or delivery note. This is useful for companies that use third party applications and require making printables accessible from those applications.
-   **Multiple Business Partner Selector**: It provides a selector which allows selecting multiple business partners in one step.
-   **Number To Word** (English): It provides the infrastructure to convert a number into its equivalent in words. This functionality is especially useful while printing checks.
-   **Javax XML SOAP API**: This module provides SOAP with Attachments API for Java (SAAJ), which was part of JDK until 10. Starting from JDK 11, it was removed, which makes this module required as a dependency for those modules making use of it in order to be able to compile in JDK11+.
-   **Report Cache Management**: This module allows changing or updating a Jasper Report in an Etendo environment without stopping the server.

## Print Document Web Service

### Technical Aspects

This module allows downloading a PDF from some transaction documents using a web service called printDocument. It returns a PDF with the order, invoice or delivery note. This is useful for companies that use third party applications and require making printables accessible from those applications.

The supported documents are:

-   Sales Quotation
-   Invoice
-   Shipment
-   Proforma Order
-   Proforma Quotation

To call the Web Service, the following URL is needed:  
[http://client-url/etendo/sws/com.etendoerp.printdocumentws.printDocument](http://client-url/etendo/sws/com.etendoerp.printdocumentws.printDocument)

It is necessary to configure Token authentication to use the web service.

Values that can be used to call the Web Service are:

-   order
-   invoice
-   shipment
-   quotation
-   orderProforma
-   shipmentValued
-   quotationProforma

This is a RESTful Web Service that returns a .PDF file of the document using the template that is configured. The supported documents are Sales Quotation, Invoice, Shipment, Proforma Order, Proforma Quotation.

It is mandatory to insert the organization ID when you call the web service because it filters by organization.

## Number To Word (English)

### Technical Aspects

The NumberToWord module deploys an infrastructure to define Number to Word conversion modules so that different logics for different languages can be deployed.

To introduce a different language (other than English and Spanish), follow this example to extend this Number to Word extend: 

```java
public class NumberToWord_es extends NumberToWord {
  private static String[] _grupos = { "", "millon", "billon", "trillon" };

  private static String[] _unidades = { "", "un", "dos", "tres", "cuatro", "cinco", "seis",
      "siete", "ocho", "nueve" };

  private static String[] _decena1 = { "", "once", "doce", "trece", "catorce", "quince",
      "dieciseis", "diecisiete", "dieciocho", "diecinueve" };

  private static String[] _decenas = { "", "diez", "veinte", "treinta", "cuarenta", "cincuenta",
      "sesenta", "setenta", "ochenta", "noventa" };

  private static String[] _centenas = { "", "cien", "doscientos", "trescientos", "cuatrocientos",
      "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos" };

  public static String millarATexto(int n) {
    if (n == 0)
      return "";

    int centenas = n / 100;
    n = n % 100;
    int decenas = n / 10;
    int unidades = n % 10;

    String sufijo = "";

    if (decenas == 0 && unidades != 0)
      sufijo = _unidades[unidades];

    if (decenas == 1 && unidades != 0)
      sufijo = _decena1[unidades];

    if (decenas == 2 && unidades != 0)
      sufijo = "veinti" + _unidades[unidades];

    if (unidades == 0)
      sufijo = _decenas[decenas];

    if (decenas > 2 && unidades != 0)
      sufijo = _decenas[decenas] + " y " + _unidades[unidades];

    if (centenas != 1)
      return _centenas[centenas] + " " + sufijo;

    if (unidades == 0 && decenas == 0)
      return "cien";

    return "ciento " + sufijo;
  }

  public static String numeroACastellano(long n) {
    String resultado = "";
    int grupo = 0;
    while (n != 0 && grupo < _grupos.length) {
      long fragmento = n % 1000000;
      int millarAlto = (int) (fragmento / 1000);
      int millarBajo = (int) (fragmento % 1000);
      n = n / 1000000;

      String nombreGrupo = _grupos[grupo];
      if (fragmento > 1 && grupo > 0)
        nombreGrupo += "es";

      if ((millarAlto != 0) || (millarBajo != 0)) {
        if (millarAlto > 1)
          resultado = millarATexto(millarAlto) + " mil " + millarATexto(millarBajo) + " "
              + nombreGrupo + " " + resultado;

        if (millarAlto == 0)
          resultado = millarATexto(millarBajo) + " " + nombreGrupo + " " + resultado;

        if (millarAlto == 1)
          resultado = "mil " + millarATexto(millarBajo) + " " + nombreGrupo + " " + resultado;
      }
      grupo++;
    }
    resultado = resultado.trim().concat(" ");
    return resultado;
  }

  public String convert(BigDecimal number) {

    double num = number.doubleValue();

    num = (double) (Math.round(num * Math.pow(10, 2)) / Math.pow(10, 2));
    int number_whole = (int) num;
    int number_decimal = (int) ((num * 100) - (number_whole * 100));
    String value;
    if (number_decimal == 0) {
      value = numeroACastellano(number_whole).concat("00/100 M.N.");
    } else {
      value = numeroACastellano(number_whole).concat(Integer.toString(number_decimal)).concat(
          "/100 M.N.");
    }
    value = value.substring(0, 1).toUpperCase().concat(value.substring(1));
    return value;
  }

}
```

## Javax XML SOAP API

### Technical Aspects

This module provides SOAP with Attachments API for Java (SAAJ), which was part of JDK until 10. Starting from JDK 11, it was removed, which makes this module required as a dependency for those modules making use of it in order to be able to compile in JDK11+.

## Report Cache Management

### Technical Aspects

This module allows changing or updating a Jasper Report in an Etendo environment without stopping the server. It allows clearing the cache for compiled reports in tomcat.

The reports have to be uploaded in the correct folder, for example: `/var/lib/tomcat/webapps/etendo/…`

Then, in the "Clear report cache" window, click ’Done’:

![Clear Report Cache](/docs/assets/drive/10BWG7z1bmplzWz--wUqI6maavHs4dC1c.png)

When you try to get the Jasper report, this repository should have been updated:

[https://bitbucket.org/koodu\_software/com.exos.erp.reportcachemanagement/src/master/](https://bitbucket.org/koodu_software/com.exos.erp.reportcachemanagement/src/master/)

## Etendo Advanced Security

### Technical Aspects

This module allows customizing several security features related to

- Password Security
- Password History
- User Lockout 
- Multiple Session Verification
- Changing Password after Login
- Expiration Time (Autolock Password)

To make this module work, **authentication Java class** must be configured in the `gradle.properties` file by adding the following line:

```
authentication.class=com.etendoerp.advanced.security.process.AdvancedAuthenticationManager
```

Then `./gradlew setup` must be executed. 

!!! warning
    It is mandatory to execute this step before installing the module. 

