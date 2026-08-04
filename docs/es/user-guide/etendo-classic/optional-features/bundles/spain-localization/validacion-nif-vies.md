---
title: Validación de NIF/VIES para Terceros
tags:
    - Localización Española
    - VIES
    - NIF
    - VAT
    - Terceros
    - Business Partner
status: new
---

# Validación de NIF/VIES para Terceros

:octicons-package-16: Javapackage: `org.openbravo.module.bptaxidkey`

## Introducción

La Localización Española incorpora una **validación del número de IVA (VAT) contra el registro VIES** (*VAT Information Exchange System*) de la Comisión Europea para los terceros (clientes y proveedores) identificados como **operadores intracomunitarios**.

El objetivo es comprobar, de forma automática, que el número de operador intracomunitario de un tercero **existe y es válido** en el registro oficial de la UE, evitando errores posteriores en las declaraciones y en los envíos a los sistemas de facturación (*SII*, *TicketBAI*, *Verifactu*).

## Qué se valida

- Se valida la **existencia y validez del número de IVA intracomunitario** consultando el **servicio web oficial de VIES** de la Comisión Europea.
- La validación se realiza **únicamente** para los terceros cuya **Clave NIF País Residencia** es **`2 - NOI`** (Número de Operador Intracomunitario) y que tengan informado el **Tax ID**.
- El número de IVA debe incluir el **prefijo de país** de dos letras (por ejemplo, `FR12345678901`, `IT15667431009`), a partir del cual se determina el país y el número a consultar.

!!! info "Resultado no bloqueante ante errores de conexión"
    Si el servicio VIES no está disponible, devuelve un error temporal o se agota el tiempo de espera, la validación **no** marca el NIF como inválido: el estado queda como **Pendiente** para poder reintentarse más adelante. De este modo, un problema puntual de conexión con VIES nunca invalida por error un número correcto.

## Cuándo se ejecuta

La validación VIES se ejecuta automáticamente **al guardar el tercero** (alta o modificación) en la ventana **Terceros**, cuando su **Clave NIF País Residencia** es `2 - NOI` y tiene un **Tax ID** informado. Si se modifica el Tax ID o la clave y VIES no está accesible en ese momento, el estado se restablece a **Pendiente** para no conservar un resultado que ya no corresponde al número actual.

El resultado de la validación queda reflejado en el campo **Estado VIES** del tercero (ver más abajo).


## Estado VIES

El resultado de la validación se almacena en el campo de solo lectura **Estado VIES** del tercero, que puede tomar los siguientes valores:

| Valor | Significado |
|---|---|
| **Válido** (`V`) | El número de identificación fiscal ha sido verificado correctamente en el registro VIES. |
| **No válido** (`I`) | El número de identificación fiscal no figura como válido en el registro VIES. |
| **Pendiente** (`P`) | Aún no verificado, o VIES no estaba accesible en el último intento. Es el valor por defecto. |

![](../../../../../../assets/user-guide/etendo-classic/optional-features/bundles/spain-localization/vies/estado-vies.png)

## Comportamiento al cambiar el país

Cuando se establece o cambia el **país** del tercero a un **país de la Unión Europea distinto de España**, y el **Tax ID** del tercero comienza con el prefijo de dos letras de ese país (por ejemplo, `FR…` para Francia), Etendo **actualiza automáticamente la Clave NIF País Residencia a `2 - NOI`** (si no lo era ya).

La validación VIES **no se ejecuta en ese mismo momento**, sino **al guardar la cabecera del tercero**: una vez guardado con la Clave NIF `2 - NOI`, se valida el número y se actualiza el campo **Estado VIES**.

Este cambio automático **no borra otros campos ni cambia la visibilidad de los mismos**: únicamente ajusta la Clave NIF a `2 - NOI`. Si el país seleccionado **no** pertenece a la UE (o es España), o el prefijo del Tax ID no coincide con el país, no se realiza ningún cambio automático.

---

This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.
