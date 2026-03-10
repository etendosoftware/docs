---
title: Cómo cambiar las fuentes en los informes de Etendo
tags:
    - Informes de Etendo
    - Fuentes personalizadas
    - JasperReports
    - Personalización de informes

status: beta
---

# Cómo cambiar las fuentes en los informes de Etendo
 
!!! example  "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úselo **bajo su propia responsabilidad**.

## Visión general

Esta sección explica cómo **cambiar las fuentes** utilizadas en los informes de Etendo. Actualizar las fuentes predeterminadas puede ser útil en dos escenarios principales: mejorar la apariencia visual de los informes con una **tipografía** más legible o alineada con la marca, o garantizar la correcta visualización de **Idioma** cuyos caracteres no están soportados por el conjunto de fuentes estándar, como japonés, árabe o vietnamita. Sustituir las fuentes predeterminadas por otras que soporten los conjuntos de caracteres requeridos permite que los informes se rendericen correctamente en distintos idiomas.

!!!info
    Para más información, visite [Cómo crear un módulo](../how-to-guides/how-to-create-a-module.md) y [Cómo crear un informe](../how-to-guides/how-to-create-a-report.md). 

Etendo utiliza la herramienta **Informe Jasper** para crear informes:


## Cambiar la fuente en Informe Jasper

Al cambiar la fuente en **Informe Jasper**, el software [Jaspersoft Studio](https://community.jaspersoft.com/download-jaspersoft/){target="\_blank"} será de gran ayuda.

En el enlace anterior, encontrará un tutorial detallado que describe **cómo gestionar** fuentes personalizadas en Jaspersoft Studio. En resumen, estos son los pasos a realizar:

1. Obtenga el archivo deseado `font's .ttf` desde el PC o desde Internet. 
2. Cree la extensión de fuente; vaya a la **ventana de Preferencias**.

    ![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-change-fonts-in-etendo-reports/how-to-change-fonts-in-Etendo-reports-0.png)

3. Haga clic en `JasperSoft Studio > Fonts`. Haga clic en **Añadir**. En este punto, proporcione un nombre único para la extensión de fuente y la ruta a su extensión seleccionando la ruta del archivo `.ttf file` descargado. 
4. Una vez hecho, establezca un tipo de codificación PDF para la nueva fuente en el asistente. 
5. Cambie los **fontName** y **pdfFontName** utilizados en los campos de texto que se deseen mostrar con la nueva fuente en el informe. Hágalo usando Jaspersoft Studio o realizando cambios directamente en el archivo `.jrxml` mediante un editor de texto. 
6. Y, para el/los documento(s), no olvide elegir el mismo tipo de codificación PDF que el establecido para la fuente en el paso 4. 
7. Exporte la fuente a un archivo `.jar`. Una vez más, Jaspersoft Studio puede ayudarle a hacerlo: vaya a `JasperSoft Studio > Fonts` y esta vez haga clic en **Exportar**. Seleccione la fuente y expórtela a un archivo `.jar`. 
8. Cree un nuevo módulo para mantener el archivo `.jar`. Dentro de la carpeta del módulo, cree una subcarpeta `/lib/runtime` y coloque allí el archivo `.jar` exportado. 

    ![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-change-fonts-in-etendo-reports/how-to-change-fonts-in-Etendo-reports-1.png)

9. Detenga tomcat.
10. Ejecute `./gradlew smartbuild`
11. Reinicie tomcat. 

## Resultado

Las siguientes capturas de pantalla muestran los resultados tras realizar correctamente los pasos mencionados anteriormente:

 **Informe Jasper** en el que la fuente del título ha sido sustituida por otra fuente:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-change-fonts-in-etendo-reports/how-to-change-fonts-in-Etendo-reports-2.png)
  
---
Este trabajo es una obra derivada de [Cómo cambiar las fuentes en los informes de Openbravo](http://wiki.openbravo.com/wiki/How_to_Change_Fonts_in_Openbravo_Reports){target="\_blank"} de [Wiki de Openbravo](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.