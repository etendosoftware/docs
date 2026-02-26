---
title: Migración a Etendo (desde Openbravo)
tags:
    - Migración
    - Openbravo
    - Configuración de Adjuntos
---

# Migración a Etendo (desde Openbravo)

## Visión general

Esta guía proporciona la información necesaria para migrar una instancia existente de Openbravo a una nueva instancia de Etendo (en su última versión). 

### Requisitos

Antes de que comience el proceso de migración, tanto si se realiza en Linux como en Windows, asegúrese de disponer de los siguientes elementos:

!!! info
    - Instancia actual de Openbravo actualizada a 21Q3.2 ([¿Cómo actualizar?](../../../../developer-guide/etendo-classic/getting-started/migration-from-openbravo/upgrading-to-openbravo-21q3-2.md))
    - Si la instalación anterior tenía parches personalizados aplicados, deben estar listos para aplicarse en un entorno actualizado a 21Q3.2.
    - La base de datos no debe tener cambios locales.
    - Espacio en disco suficiente para la nueva instalación.
    - Licencia del entorno y nombre y token de GitHub (cree las credenciales siguiendo esta [guía](../../../../developer-guide/etendo-classic/getting-started/installation/use-of-repositories-in-etendo.md)).

!!! warning
    - El servidor donde se aloja la base de datos debe tener suficiente espacio libre para albergar una copia de la base de datos actual.  
    - El servidor donde se alojan las fuentes también debe poder albergar una copia de las fuentes actuales.  
    - Los adjuntos se mantienen en el mismo lugar en el que estaban anteriormente.



## Instrucciones para el proceso de migración

### Antes de iniciar la migración
Es necesario asegurarse de seguir los siguientes pasos:

1.  Detenga el servidor Tomcat.

    ``` bash title="Terminal" 

    sudo /etc/init.d/tomcat stop
    ```

    !!! info
        Dependiendo de su servidor, puede ser necesario cambiar este comando.


2. Cree una copia de seguridad de su instancia.


### Proceso de migración manual

Estos son los pasos a seguir para la migración manual de OpenbravoERP a Etendo Classic:

1. Cree y acceda a la carpeta Etendo Classic.

2. Inserte las fuentes de **etendo_base** en la carpeta Etendo Classic. Se pueden extraer tras descargar Etendo desde [Recursos](https://etendo.software/es/recursos){target="_blank"}. Para ello, utilice su usuario y token de GitHub.

3. El archivo `gradle.properties` tiene parámetros por defecto, pero si es necesario se pueden cambiar.  

    ???+Note
        Recuerde configurar el usuario y el token de GitHub, ya que se utilizan para expandir módulos privados. Cree las credenciales siguiendo la [guía técnica de uso de repositorios](../../../../developer-guide/etendo-classic/getting-started/installation/use-of-repositories-in-etendo.md).
        

    ``` groovy title="gradle.properties"
    githubUser=
    githubToken=

    context.name=etendo

    bbdd.sid=etendo
    bbdd.port=5432
    bbdd.systemUser=postgres
    bbdd.systemPassword=syspass
    bbdd.user=tad
    bbdd.password=tad
    ```

    !!! info
        Compruebe si es necesario mantener la base de datos de Openbravo o crear una nueva para Etendo. En caso de crear una nueva, utilice la anterior de Openbravo como base.



4. En un nuevo terminal abierto en la carpeta `EtendoERP`, ejecute: 
    ``` bash title="Terminal" 
    ./gradlew expandCore
    ```
5. Ejecute en el terminal: 
    ``` bash title="Terminal"
    ./gradlew setup
    ```
6. Mueva los módulos existentes de la carpeta `Openbravo/modules` a la carpeta `EtendoERP/modules`, excepto los siguientes:

    !!! warning
        com.smf.securewebservices<br>
        com.smf.smartclient.boostedui<br>
        com.smf.smartclient.debugtools<br>
        org.openbravo.advpaymentmngt<br>
        org.openbravo.apachejdbcconnectionpool<br>
        org.openbravo.base.weld<br>
        org.openbravo.client.application<br>
        org.openbravo.client.htmlwidget<br>
        org.openbravo.client.kernel<br>
        org.openbravo.client.myob<br>
        org.openbravo.client.querylist<br>
        org.openbravo.client.widgets<br>
        org.openbravo.financial.paymentreport<br>
        org.openbravo.reports.ordersawaitingdelivery<br>
        org.openbravo.service.datasource<br>
        org.openbravo.service.integration.google<br>
        org.openbravo.service.integration.openid<br>
        org.openbravo.service.json<br>
        org.openbravo.userinterface.selector<br>
        org.openbravo.userinterface.skin.250to300Comp<br>
        org.openbravo.userinterface.smartclient<br>
        org.openbravo.utility.cleanup.log<br>
        org.openbravo.v3<br>
        org.openbravo.v3.datasets<br>
        org.openbravo.v3.framework<br>

        
        Estos módulos ya estarán en la carpeta `EtendoERP/modules_core` ya que son módulos core en Etendo. 

7. Ejecute:
    ``` bash title="Terminal" 
    ./gradlew update.database compile.complete.deploy --info
    ```
!!! info
    Pueden producirse errores de compilación asociados a cambios de API debido al cambio de versión en módulos personalizados. Si esto ocurre, asegúrese de corregirlos utilizando las [incidencias documentadas en GitHub](https://github.com/etendosoftware/etendo_core/issues?q=is%3Aissue+){target="_blank"}. 



## Configuración posterior a la migración

### Eliminar el contexto desplegado de la instancia anterior

``` bash title="Terminal"
rm -r /var/lib/tomcat/webapps/openbravo
```
!!! warning
    Asegúrese de que este paso se realiza antes de iniciar Tomcat; de lo contrario, se arriesga a tener dos entornos ejecutándose al mismo tiempo, lo que puede causar problemas (especialmente cuando intervienen procesos en segundo plano).


### Iniciar Tomcat

!!! info
    Dependiendo de su servidor, puede ser necesario cambiar este comando.

  
``` bash title="Terminal" 

sudo /etc/init.d/tomcat start
```



### Configuración de Adjuntos

!!! warning
    Antes de eliminar su instancia anterior, asegúrese de migrar sus archivos adjuntos.


En el proceso de migración, la configuración del directorio de adjuntos no se modifica. Para moverlos a una nueva carpeta (por ejemplo `/opt/EtendoERP/attachments`), debe editar el archivo `Openbravo.properties`:

``` bash title="Terminal" 
vi /opt/EtendoERP/config/Openbravo.properties
## Change the attach.path property like this (do not include the #):
## attach.path=/opt/EtendoERP/attachments
```

 y mover los adjuntos manualmente: 

``` bash title="Terminal" 
mv /opt/OpenbravoERP/attachments /opt/EtendoERP/attachments
## Deploy changes to tomcat
./gradlew smartbuild
```
!!! info
    Puede ser necesario tener una consideración especial si su carpeta de adjuntos está en una unidad de red o en una partición diferente (con o sin un enlace simbólico).  
    Tenga cuidado al cambiar la configuración de adjuntos y asegúrese de disponer de una copia de seguridad reciente.


### Personalizaciones en el Core

Vuelva a aplicar los parches al core si es necesario y compile.

!!! info
    Las tareas de compilación ahora se pueden realizar con el Gradle Wrapper.


``` bash title="Terminal" 

patch -p1 < customPatchToCore.patch
## Apply other patches as needed
./gradlew smartbuild
sudo /etc/init.d/tomcat restart
```

### Configuración de Apache

1.  Si es necesario, cambie la configuración de Apache para usar jkmount en el contexto correcto ("openbravo" por defecto en la instalación antigua).  
    El archivo de configuración debería estar en `/etc/apache2/conf-enabled/openbravo.conf`, `/etc/apache2/conf-available/openbravo.conf`o `/etc/apache2/sites-available/000-default.conf` / `/etc/apache2/sites-available/000-default-le-ssl.conf`<br>
    Sustituya `jkMount /openbravo* ajp13_worker` por `jkMount /etendo* ajp13_worker`
    
2.  Cambie la configuración de Apache para redirigir al nuevo contexto ("openbravo" por defecto en la instalación antigua).  
        El archivo de configuración debería estar en `/var/www/html/index.html`.  
        Sustituya `<META HTTP-EQUIV="Refresh" CONTENT="0; URL=openbravo">` por `<META HTTP-EQUIV="Refresh" CONTENT="0; URL=etendo"> `  
        
    !!! warning
        Asegúrese de sustituir  por el contexto que eligió en el archivo `gradle.properties`.


3.  Reinicie Apache:
    

``` bash title="Terminal" 

sudo service apache2 restart
```

### Activar su instancia

1.  Inicie sesión como Administrador del sistema y utilice la ventana Activación de instancia para activar su instancia.
2.  Utilice Actualizar en línea
3.  Introduzca el propósito de su instancia y su clave de activación.

!!! success
    ¡Su instancia está activada!


### Cambiar el script de copia de seguridad y restauración

1.  Asegúrese de que el script de copia de seguridad ahora obtiene sus datos del `Openbravo.properties` correcto, por ejemplo en la carpeta `/opt/EtendoERP/`  
        El script de copia de seguridad suele estar ubicado en `/usr/share/openbravo/backup/backup`. Debe cambiar las líneas para que apunten al archivo `Openbravo.properties` real. Por ejemplo:
        

    ```bash title="Terminal"

    db_login=$(awk -F = '/^bbdd.user/ {print $2}' /opt/OpenbravoERP/config/Openbravo.properties)
    ```

    Debería cambiarse por algo como esto:

    ```bash title="Terminal"

    db_login=$(awk -F = '/^bbdd.user/ {print $2}' /opt/EtendoERP/config/Openbravo.properties)
    ```

    Esto variará dependiendo de la ruta que se haya seleccionado para la migración.

    !!! warning
        Recuerde que, en el estado actual, `Openbravo.properties` no cambia su nombre. Esto no debe cambiarse hasta nuevo aviso del equipo de desarrollo. Además, no debe cambiar el nombre Openbravo en ningún otro lugar. Hágalo solo en las rutas del archivo de propiedades.


    !!! info
        Se está desarrollando una herramienta de copias de seguridad dedicada.


2.  Lo mismo debe hacerse para `/usr/bin/openbravo-restore`. Dado que los scripts están altamente hardcodeados, tiene que cambiar algunas líneas manualmente.

La base de datos que debe eliminarse debería ser la base de datos de Etendo, pero el script eliminará la base de datos openbravo. Esto debe cambiarse para eliminar la base de datos de Etendo. 

- Cambie:

    ```bash

    su - postgres -c "psql -U postgres -c "drop database openbravo"" || true
    ```

    por:
    ```bash

    su - postgres -c "psql -U postgres -c "drop database etendo"" || true

    ```

- Cambie la línea que crea la base de datos:

    ```bash

    su - postgres -c "psql -U postgres -c "create database openbravo WITH ENCODING='UTF8' OWNER=TAD;""

    ```

    por

    ```bash

    su - postgres -c "psql -U postgres -c "create database etendo WITH ENCODING='UTF8' OWNER=TAD;""

    ```

- Cambie la base de datos destino en las líneas en las que se realiza el pg\_restore, por ejemplo:

    ```bash

    PGPASSWORD=tad pg_restore -U tad -h localhost -d openbravo -O $TEMP_FOLDER/db_backup.dmp || true

    ```

    por

    ```bash

    PGPASSWORD=tad pg_restore -U tad -h localhost -d etendo -O $TEMP_FOLDER/db_backup.dmp || true

    ```

- Cambie la línea que borra los archivos de Tomcat:

    ```bash

    rm -rf /var/lib/tomcat/webapps/openbravo || true

    ```

    por

    ```bash

    rm -rf /var/lib/tomcat/webapps/etendo || true

    ```

- Cambie la ruta de las fuentes por la nueva ruta creada para Etendo, por ejemplo:

    ```bash

    sudo chown openbravo:openbravo /opt/OpenbravoERP/

    ```

    por

    ```bash

    sudo chown openbravo:openbravo /opt/EtendoERP/

    ```
!!! warning
    El mismo aviso para las copias de seguridad aplica aquí. Tenga cuidado con lo que renombra. Si ve un error, por favor solicite soporte.


### Cambiar el directorio inicial al iniciar sesión

Dentro de `~/.bashrc` puede tener un comando que le permite iniciar sesión directamente en la carpeta `/opt/OpenbravoERP`. Cámbielo para que apunte a la carpeta de su nueva instancia:

``` bash title=".bashrc" 

## Change
cd /opt/Openbravo
## To
cd /opt/EtendoERP
```

### Cambiar el usuario del servidor

Puede cambiar el usuario actual de Openbravo a Etendo, si lo desea. Esta guía no cubre cómo hacerlo.

### Eliminar la instalación anterior

1.  Elimine el contexto de Openbravo de la carpeta de Tomcat:

    ``` bash title="Terminal"

    rm -r /var/lib/tomcat/webapps/openbravo
    ```

2.  Elimine la instalación de Openbravo:

    ``` bash title="Terminal"

    rm -r /opt/OpenbravoERP
    ```

3.  Elimine la base de datos de Openbravo:

    ``` bash title="Terminal"

    psql -h localhost -U postgres -d etendo -c "DROP DATABASE openbravo;"
    ```
!!! warning
    Asegúrese de que los comandos anteriores apuntan a las bases de datos, el usuario y el host correctos, y de que ha realizado una copia de seguridad antes de ejecutar el comando.

### Aplicar correcciones de impuestos 303 e informe de impuestos

Este paso solo es necesario si se dan las siguientes condiciones en su entorno:

* Los módulos `org.openbravo.module.aeat303.temporal.taxes.es`, `org.openbravo.module.aeat303.temporal.taxparameters.es`, `org.openbravo.localization.spain.referencedata.taxes.es` y `org.openbravo.module.aeat303.es` están instalados y sus conjuntos de datos aplicados en el ERP
* Quiere actualizar el bundle `Spain Localization Extensions` a la versión `1.8.0` o superior; en caso contrario, quiere actualizar los módulos mencionados a estas versiones:
    * `org.openbravo.localization.spain.referencedata.taxes.es`: versión `1.8.0` o superior
    * `org.openbravo.module.aeat303.es`: versión `1.14.0` o superior

Para resolver los problemas con impuestos derivados de que estos módulos se migren de Openbravo a Etendo, consulte la [incidencia conocida](../../../../whats-new/release-notes/etendo-classic/known-issues.md/#ee-808-problem-when-trying-to-import-the-taxes-configuration-for-spain-dataset-if-the-environment-already-has-imported-the-dataset-related-to-the-303-temporary-taxes-of-openbravo) relacionada. 

### Aplicar correcciones de impuestos 390 e informe de impuestos

Este paso solo es necesario si se dan las siguientes condiciones en su entorno:

* Los módulos `org.openbravo.module.aeat303.temporal.taxes.es`, `org.openbravo.module.aeat303.temporal.taxparameters.es`, `org.openbravo.localization.spain.referencedata.taxes.es` y `org.openbravo.module.aeat390.es` están instalados y sus conjuntos de datos aplicados en el ERP
* Quiere actualizar el bundle `Spain Localization Extensions` a la versión `1.8.0` o superior; en caso contrario, quiere actualizar los módulos mencionados a estas versiones:
    * `org.openbravo.localization.spain.referencedata.taxes.es`: versión `1.8.0` o superior
    * `org.openbravo.module.aeat390.es`: versión `3.9.0` o superior

Para resolver los problemas con impuestos derivados de que estos módulos se migren de Openbravo a Etendo, consulte la [incidencia conocida](../../../../whats-new/release-notes/etendo-classic/known-issues.md/#ee-856-390-tax-report-dataset-duplicates-data-for-2022-when-applied-on-a-server-migrated-from-ob-to-etendo-after-01-2023) relacionada. 

## Conclusión

!!! info
    Con estos pasos, debería haber migrado correctamente sus datos de Openbravo a Etendo, tanto en un sistema Linux como en un sistema Windows. Si encuentra algún problema durante el proceso, póngase en contacto con el [equipo de soporte de Etendo](https://etendoproject.atlassian.net/servicedesk/customer/portals){target="_blank"} para obtener asistencia.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.