---
title: Configuración de PostgreSQL 
tags:
    - Configuración de PostgreSQL
    - Configuración de usuario
    - Base de datos
    - Extensión de PostgreSQL
---

# Configuración de PostgreSQL 

## Visión general

Esta sección explica cómo configurar postgres para que funcione correctamente con Etendo Classic. Una vez que haya instalado postgres, debe asegurarse de que la configuración esté establecida correctamente.

## Configuración del usuario del sistema
Cuando [instala postgres](https://www.postgresql.org/download/){target="_blank"}, se crea un usuario del sistema llamado `postgres`. Si no ha configurado una contraseña para este usuario, puede hacerlo ejecutando el siguiente comando

```bash title="Terminal"
sudo -u postgres psql
```
Entrará inmediatamente en la shell de postgresql; a continuación, puede configurar la contraseña ejecutando el siguiente ejemplo:

``` sql title="Postgresql Shell"
ALTER USER postgres PASSWORD 'syspass';
```

!!! info
    Etendo Classic tiene `syspass` preconfigurado como contraseña predeterminada para el usuario postgres. En caso de cambiar la contraseña del sistema, esta variable de configuración debe modificarse siguiendo la [guía de instalación](../../../../getting-started/installation.md) de Etendo Classic.

## Configuración del usuario de Etendo Classic

!!! warning
    En caso de instalar Etendo desde cero ejecutando el comando `./gradlew install`, el proceso de instalación crea automáticamente el usuario y la contraseña predeterminados `tad`, y ya están incluidos preconfigurados. En caso de que no necesite cambiar el usuario `tad`, puede omitir esta sección.

Si necesita crear un usuario y una contraseña de Postgres para la aplicación Etendo, puede hacerlo ejecutando el siguiente comando

```bash title="Terminal"
PGPASSWORD=system_password psql -U postgres -d postgres -h localhost
```

Entrará inmediatamente en la shell de postgresql; a continuación, puede crear el usuario ejecutando el siguiente ejemplo:

``` sql title="Postgresql Shell"
CREATE ROLE tad LOGIN PASSWORD 'tad'  CREATEDB CREATEROLE VALID UNTIL 'infinity';
```

!!! note
    El usuario y la contraseña creados pueden configurarse en el archivo `gradle.properties`, tal y como puede verse en la [guía de instalación](../../../../getting-started/installation.md#install-etendo) de Etendo Classic.


## Configuración requerida
Asegúrese de tener la siguiente configuración de PostgreSQL en su `postgresql.conf`. Este archivo se encuentra en la ubicación donde tenga instalado postgresql

``` title="postgresql.conf"
lc_numeric = 'en_US.UTF-8'
max_locks_per_transaction = 128
```        

### Extensiones de PostgreSQL requeridas
Actualmente, Etendo Classic requiere que estén disponibles dos extensiones de PostgreSQL:

**uuid-ossp** para generar UUID
**pg_trgm** para disponer de soporte de índices para búsquedas rápidas de tipo "contiene"

**Desde la versión 10, estas forman parte de la instalación normal del servidor PostgreSQL.**

!!! note
    Después de modificar el archivo, reinicie el servicio postgresql

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.