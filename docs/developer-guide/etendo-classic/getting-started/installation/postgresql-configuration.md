---
title: PostgreSQL Configuration 
---

## Overview

This section explains how to set up postgres to work properly with Etendo Classic, once you have installed postgres, you need to make sure that the configuration is set up properly.

## System User configuration
When you install postgres, it creates a system user called `postgres`, if you not set up a password for this user, you can do it by running the following command
```bash
sudo -u postgres psql
```
And you will inmediatly enter the postgresql shell, then you can set up the password by running the following command
``` postgresql
ALTER USER postgres PASSWORD 'system_user_password';
```


!!! note
    Make sure to remember the password you set up for the `postgres` user, you will need it later for the gradle configuration

## Etendo Classic User configuration
Additionaly, you need to create a user for the etendo classic application, you can do it by running the following command
```bash
PGPASSWORD=system_user_password psql -U postgres -d postgres -h localhost
```

And you will inmediatly enter the postgresql shell, then you can create the user by running the following command
``` postgresql
CREATE ROLE etendo_user LOGIN PASSWORD 'etendo_user_password'  CREATEDB CREATEROLE VALID UNTIL 'infinity';
```
!!! note
    Make sure to remember the password you set up for the `etendo_user` user, you will need it later for the gradle configuration

## Required Configuration
Make sure you have the following PostgreSQL configuration in your `postgresql.conf`, this file is located wherever you have postgresql installed
```
lc_numeric = 'en_US.UTF-8'
max_locks_per_transaction = 128
```        

### Required PostgreSQL extensions
Etendo Classic currently requires two PostgreSQL extensions to be available:

**uuid-ossp** to generate UUID's
**pg_trgm** to have index support for fast contains search

**Since version 10 those are part of the normal PostgreSQL server installation.**

!!! note
    After modifying the file restart postgresql
