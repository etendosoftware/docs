---
title: PostgreSQL Configuration 
tags:
    - PostgreSQL Configuration
    - User configuration
    - Database
    - PostgreSQL Extension
---

# PostgreSQL Configuration 

## Overview

This section explains how to set up postgres to work properly with Etendo Classic, once you have installed postgres, you need to make sure that the configuration is set up properly.

## System User configuration
When you [install postgres](https://www.postgresql.org/download/){target="_blank"}, it creates a system user called `postgres`, if you not set up a password for this user, you can do it by running the following command

```bash title="Terminal"
sudo -u postgres psql
```
You will inmediatly enter the postgresql shell, then you can set up the password by running the following example:

``` sql title="Postgresql Shell"
ALTER USER postgres PASSWORD 'syspass';
```

!!! info
    Etendo Classic has `syspass` preconfigured as the default password for the postgres user. In case of changing the system password, this configuration variable should be changed by following the Etendo Classic [installation guide](../../../../getting-started/installation.md).

## Etendo Classic User configuration

!!! warning
    In case of installing Etendo from scratch by executing the command `./gradlew install`, the installation process creates the default user and password `tad` automatically, and they are already includes preconfigured. In case you do not need to change the `tad` user, you can skip this section.

If you need to create a Postgres user and password for the Etendo application, you can do it by running the following command

```bash title="Terminal"
PGPASSWORD=system_password psql -U postgres -d postgres -h localhost
```

You will inmediatly enter the postgresql shell, then you can create the user by running the following example:

``` sql title="Postgresql Shell"
CREATE ROLE tad LOGIN PASSWORD 'tad'  CREATEDB CREATEROLE VALID UNTIL 'infinity';
```

!!! note
    The user and password created can be configured in the `gradle.properties` file, as can be seen in the Etendo Classic [installation guide](../../../../getting-started/installation.md#install-etendo).


## Required Configuration
Make sure you have the following PostgreSQL configuration in your `postgresql.conf`, this file is located wherever you have postgresql installed

``` title="postgresql.conf"
lc_numeric = 'en_US.UTF-8'
max_locks_per_transaction = 128
```        

### Required PostgreSQL extensions
Etendo Classic currently requires two PostgreSQL extensions to be available:

**uuid-ossp** to generate UUID's
**pg_trgm** to have index support for fast contains search

**Since version 10 those are part of the normal PostgreSQL server installation.**

!!! note
    After modifying the file restart postgresql service

---

This work is a derivative of [Developer Guide](https://wiki.openbravo.com/wiki/Category:Developers_Guide){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.