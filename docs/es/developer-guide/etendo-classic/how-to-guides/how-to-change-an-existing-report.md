---
title: Cómo cambiar un informe existente

tags:
    - Personalización de informes
    - Módulos
    - jrxml
    - Modificación de plantillas 
    - Informes de Etendo

status: beta

---

# Cómo cambiar un informe existente
 
!!! example  "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.

## Visión general

Al desplegar Etendo, una de las personalizaciones iniciales más comunes es adaptar las plantillas estándar de documentos como **Pedidos, albaranes y facturas** para cumplir con los requisitos funcionales de la empresa y su imagen corporativa. Estos documentos se comparten entre procesos de clientes y proveedores, por lo que es esencial que reflejen información precisa y una identidad visual coherente.
Esta guía describe cómo modificar plantillas de informes existentes de forma modular y mantenible, utilizando el informe de **Pedido de venta** como ejemplo de referencia.

!!! info 
    Para más información, visite [Cómo crear un informe ](../how-to-guides/how-to-create-a-report.md).


## Definición del Módulo

Primero es necesario definir un nuevo módulo que contenga las modificaciones del informe.

!!! info
    Para más información sobre cómo crear un módulo, visite [Cómo crear un Módulo ](../how-to-guides/how-to-create-a-module.md). 

1. Como Administrador del sistema
    - Cree un nuevo registro en la ventana **Módulo**.
    - Rellene todos los campos obligatorios. 
    - Rellene todos los datos obligatorios en las solapas hijas: Dependencia, Prefijo de BD, etc.
    
    ![alt text](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-change-an-existing-report/how-to-change-an-existing-report-1.png)


2. Exporte sus cambios para crear la estructura del módulo

    ``` bash title="Terminal"
    ./gradlew export.database
    ```

## Copia de la plantilla base

Después de exportar los cambios, habrá una nueva carpeta dentro de la carpeta modules.

- Cree una carpeta src. 
- Copie las plantillas base desde `src/org/openbravo/erpReports/C_Order*.jrxml` a la carpeta del módulo.

    Es importante seguir la **estructura de paquetes Java** para terminar con una estructura como esta:

    ![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-change-an-existing-report/how-to-change-an-existing-report-2.png)

## Modificación de la plantilla

Después de hacer una copia de la **plantilla base** en el módulo, es posible realizar todos los cambios que necesite. Simplemente añada una etiqueta sencilla en el encabezado del informe.

- Inicie iReport.
- Abra el archivo `C_OrderJR.jrxml` de su módulo.
- Añada una etiqueta sencilla: **Mi personalización**.

    !!!info
        Es posible personalizar su plantilla con cualquier cambio que desee: más campos, cambio de posición, etc.  

    ![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-change-an-existing-report/how-to-change-an-existing-report-3.png)

- Reconstruya sus cambios para desplegar la estructura del módulo 
    
    ```bash title="Terminal"
    ./gradlew smartbuild
    ```

- Recargue Etendo desde Tomcat Manager 

## Definición de la plantilla de informe a nivel de documento

Las plantillas de informe se definen a **nivel de documento**. Es necesario cambiarlo para que funcione.

- Como rol Administrador del cliente 
- Vaya a: `Gestión financiera > Contabilidad > Configuración > Tipo de documento`

    ![alt text](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-change-an-existing-report/how-to-change-an-existing-report-4.png)

- Busque por Nombre **Pedido estándar** y ábralo. 
    - Abra la solapa **Plantilla de informe** y modifique el campo **Ubicación de la Plantilla**. 
    - Use la ubicación donde se encuentra su copia. Por ejemplo: `@basedesign@/org/openbravo/howto/mysalesorder`
    - Guarde los cambios. 

    ![alt text](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-change-an-existing-report/how-to-change-an-existing-report-5.png)

## Prueba de los cambios

Ya se han realizado todas las definiciones necesarias para usar la plantilla personalizada de **Pedido de venta**. Solo es necesario verificar que la nueva plantilla de documento creada renderiza el documento como se espera con un documento de Pedido de venta existente.

- Abra cualquier **Pedido de venta** usando **Pedido estándar** como tipo de documento.
- Imprímalo.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-change-an-existing-report/how-to-change-an-existing-report-6.png)

---
Este trabajo es una obra derivada de [Cómo cambiar un informe existente](http://wiki.openbravo.com/wiki/How_to_change_an_existing_Report){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, usada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.