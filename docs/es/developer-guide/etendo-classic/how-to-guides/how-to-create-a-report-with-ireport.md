---
title: Cómo crear un informe con iReport
tags: 
    - Crear
    - Informe
    - iReport
    - Cómo
status: beta
---

# Cómo crear un informe con iReport

!!! example "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.
  
## Visión general

El objetivo de esta sección es describir los pasos necesarios para crear un nuevo informe en Etendo. El ejemplo explicado es un informe sencillo con una lista de productos.

## Configuración de iReport

Debe descargar iReport, una herramienta gráfica que le permite crear y modificar plantillas de JasperReports (archivos .jrxml).
 
  - Descargue [iReport 4.0.1](https://sourceforge.net/directory/build-tools/linux/){target="\_blank"}
  - En Linux: simplemente descargue el archivo `.tar.gz` o `.zip` y descomprímalo, ejecute el binario 
    ``` shell  
    bin/ireport
    ```
  - En Windows: descargue y ejecute el archivo `.exe` 

### Configuración de iReport

Algunas propiedades de iReport deben modificarse para que funcione correctamente. Debe asegurarse de que:

- Ha modificado la propiedad de JasperReport `net.sf.jasperreports.awt.ignore.missing.font` y la ha establecido en **true**
- **No** utilizar ninguna clase de **Scriptlet** 
- Usar **Java** como lenguaje de expresiones predeterminado 

### Configuración del Classpath

- Abra desde las opciones del menú: `Tools` > `Options`
- Vaya a la pestaña **Classpath** 
- Haga clic en el botón **Add Jar** 
- Vaya a su carpeta de fuentes de Etendo. Dentro de la carpeta **lib/runtime**, busque **postgresql*jdbc*.jar** y selecciónelo. 
- Haga clic en **OK**

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-report-with-ireport/how-to-create-a-report-with-ireport-1.png)

### Definición de una conexión a base de datos

1. Haga clic en el icono de orígenes de datos del informe  ![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-report-with-ireport/how-to-create-a-report-with-ireport-2.png)
2. Haga clic en **New**
3. Seleccione **Database JDBC Connection** y haga clic en **Next**
4. Rellene todos los campos:

    - **Name:** etendo (o cualquier nombre que desee, p. ej. pi)
    - **JDBC Driver:** PostgreSQL (`org.postgresql.Driver`)
    - **Server Address:** la dirección de su servidor de base de datos, p. ej. localhost
    - **Database:** pi (o el nombre de su base de datos)
    - **Username:** tad (puede comprobar su usuario/contraseña en el archivo de configuración `gradle.properties`)
    - **Password:** tad

5. Haga clic en el botón Wizard para generar la URL JDBC 
6. Pruebe su conexión 
7. Guarde 

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-report-with-ireport/how-to-create-a-report-with-ireport-3.png)

## Creación de la plantilla

1. Vaya a **File** > **New**
2. Seleccione **Report**
3. Haga clic en **Launch Report Wizard**

    ![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-report-with-ireport/how-to-create-a-report-with-ireport-4.png)

4. Defina un **Report Name**.
5. Defina la **File Location**. Tenga en cuenta que su plantilla `.jrxml` debe colocarse dentro de la carpeta src de su módulo. Más información sobre la [estructura de carpetas del proyecto](../concepts/development-project-structure.md#modules). Una convención habitual es colocar sus informes en una carpeta `ad_reports`, p. ej. `modules/org.your.java.package/src/org/your/java/package/ad_reports`. Esto es una convención, no un requisito, pero debe recordar dónde colocó su plantilla. 

    ![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-report-with-ireport/how-to-create-a-report-with-ireport-5.png)

6. Defina la consulta para extraer los datos 
7. Seleccione el origen de datos del informe definido previamente 
8. Los productos se almacenan en la tabla M_Product 

    ``` sql
    SELECT m_product_id, value, name FROM m_product
    ```
9. Haga clic en **Next** 

    ![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-report-with-ireport/how-to-create-a-report-with-ireport-6.png)

10. iReport define los campos en función de su consulta 
11. Seleccione todos los campos y haga clic en Next 

    ![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-report-with-ireport/how-to-create-a-report-with-ireport-7.png)

12. Recuerde limpiar la clase Scriptlet y modificar el Language para las expresiones 
13. Vaya a **Window** > **Report Inspector**
14. En las propiedades del informe a la derecha, desplácese hacia abajo hasta la sección More:
    
    - Limpie la clase Scriptlet 
    - Elija Java como Language 

15. **Guarde** sus cambios 

    ![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-report-with-ireport/how-to-create-a-report-with-ireport-8.png)

16. Ponga un texto estático como título del informe: `Product List`
17. Coloque los campos en la banda **Detail** y un título en la banda **Column Header** 
18. **Guarde** sus cambios 

    ![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-report-with-ireport/how-to-create-a-report-with-ireport-9.png)


19. Haga clic en el botón **Preview** para obtener una vista previa del informe 

    ![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-report-with-ireport/how-to-create-a-report-with-ireport-10.png)

!!! note
    Se recomienda utilizar fuentes *Dejavu* en los informes Jasper porque estas fuentes soportan la mayoría de los caracteres en casi todos los idiomas. Además, la tipografía Dejavu es la familia de fuentes que Etendo incluyó en la librería `jasperreports-fonts`.
  
## Registro del informe en el Diccionario de Aplicación

### Creación del informe

1. Usando el quick-launch, bajo el rol de Administrador del sistema, abra la ventana **Informes y procesos** 
    - Puede encontrarla en el menú: `Application Dictionary` > `Informes y procesos` 

2. Cree un **nuevo registro** 
3. Rellene todos los campos obligatorios 
    - **Módulo:** seleccione su módulo 
    - **Identificador:** SMPLRProductList (es una buena práctica comenzar con el [DB_Prefix](../concepts/modularity-concepts.md#db-prefix) de su módulo) 
    - **Nombre:** Lista de productos 
    - **Acceso datos:** Cliente/Organización 
    - **Patrón de la Interfaz de Usuario:** Estándar 
    - **Informe Jasper:** Marcar 
    - **Nombre plantilla JR** : 
    
        ```
        @basedesign@/org/openbravo/examples/report/ad_reports/ProductList.jrxml

        ```

        - `@basedesign@` es una **constante** que **debe** usar siempre; a continuación, comenzando con una barra, debe escribir la ruta a su plantilla jrxml. 

    !!! note
        La casilla de verificación **Informe** debe estar desmarcada.  

    ![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-report-with-ireport/how-to-create-a-report-with-ireport-11.png)

### Creación del registro de menú

1. Usando el rol de Administrador del sistema, abra la ventana **Menú** 
2. Cree un **nuevo registro** 
3. Rellene todos los campos obligatorios:

    - **Módulo:** su módulo 
    - **Nombre:** nombre de la entrada de menú (Lista de productos) 
    - **Descripción:** debe introducir una descripción. Aunque no está marcado como obligatorio, lo es para este tipo de informes 
    - **Acción:** seleccione Proceso 
    - **Proceso:** seleccione su proceso (Lista de productos) 

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-report-with-ireport/how-to-create-a-report-with-ireport-12.png)

## Compilación

Después de haber registrado el informe y la entrada de menú en el Diccionario de Aplicación, debe compilar para generar el código necesario.
    
``` shell Title="Terminal"  
./gradlew  smartbuild --info
```

Una vez finalizada la compilación, actualice su proyecto de Eclipse y reinicie su servidor Tomcat.

## Prueba del informe

Si ha completado todos los pasos, debería poder abrir su informe Lista de productos desde el quick-launch o desde la entrada de menú.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-a-report-with-ireport/how-to-create-a-report-with-ireport-13.png)

## Creación de un informe usando una definición de proceso
  
Es posible crear un informe usando una definición de proceso. Para más información, visite [Cómo crear un informe usando una definición de proceso](how-to-create-a-report-using-process-definition.md).

---

Este trabajo es una obra derivada de [Cómo crear un informe con iReports](http://wiki.openbravo.com/wiki/How_to_create_a_Report_with_iReport){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.