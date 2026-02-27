---
title: Descargador de rangos de conversión
tags:
    - Rango de conversión
    - Moneda
    - Regla de descarga
    - Currency Data API
    - Monedas
---

# Descargador de rangos de conversión

:octicons-package-16: Javapackage: `com.smf.currency.conversionrate`  
:octicons-package-16: Javapackage: `com.smf.currency.apiconfig`

## Visión general

El módulo Descargador de rangos de conversión **automatiza la obtención** de tipos de cambio de moneda desde proveedores externos y los inserta en el sistema. Ayuda a mantener la precisión de las operaciones financieras al garantizar que siempre haya disponibles rangos de conversión actualizados, reduciendo el trabajo manual y minimizando errores.

En general, el proceso de configuración implica tres pasos principales:

1. **Configurar la conexión con la API externa de divisas**
2. **Definir los pares de divisas que se descargarán**
3. **Planificar el proceso de descarga automática**

Una vez completados estos pasos, el sistema recupera los rangos de conversión automáticamente según la planificación, y los valores más recientes quedan disponibles para todas las transacciones financieras que requieran conversión de moneda.

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

## Configuración inicial 

### Convertidores de moneda

:material-menu: `Aplicación` > `Gestión de Datos Maestros` > `Convertidores de moneda`

Este módulo puede ampliarse para soportar diferentes **API de conversión de moneda**. Por defecto, se integra con [APILayer – Currency Data API](https://marketplace.apilayer.com/currency_data-api?utm_source=apilayermarketplace&utm_medium=featured){target="_blank"}.

![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/conversion-rates-downloader/currency-data-api.png)

Para configurar la conexión:

1. Regístrese en [APILayer](https://marketplace.apilayer.com/){target="_blank"} y cree una cuenta.
2. Suscríbase a la **Currency Data API**. El plan gratuito ofrece 100 peticiones mensuales, suficiente para múltiples actualizaciones diarias. Copie el token de acceso proporcionado.
3. En la ventana **Convertidores de moneda**, complete los siguientes campos:

    ![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/conversion-rates-downloader/currency-converters.png)

    - **Nombre de clase del servicio**: Clase Java utilizada para la conexión con la API. Por defecto: `com.smf.currency.apiconfig.CurrencyLayerConverter`
    - **Entidad/Cliente**: Entidad/Cliente autorizada a usar esta configuración.
    - **Organización**: Organización autorizada a usar esta configuración. Use `*` para permitir todas las organizaciones.
    - **Nombre del servicio**: Identificador de esta configuración, p. ej., `Currency Data API`.
    - **URL del servicio**: Endpoint de la API. Por defecto: `https://api.apilayer.com/currency_data/`
    - **Token**: Token de acceso a la API.
    - **Usuario** *(opcional)*: No es necesario para esta configuración.
    - **Contraseña** *(opcional)*: No es necesario para esta configuración.
    - **Seleccionado**: Debe ser **True** para activar esta configuración para el proceso de descarga.
    - **Activo**: Debe ser **True** para que la configuración esté disponible.

### Regla de descarga de rangos de conversión

:material-menu: `Aplicación` > `Configuración General` > `Aplicación` > `Regla de descarga de rangos de conversión`

Después de configurar la API, defina los pares de divisas que se descargarán.

!!! info
    Se recomienda definir reglas en ambas direcciones. Por ejemplo, *USD → EUR* y *EUR → USD*, para evitar problemas en escenarios contables que requieran conversiones en ambos sentidos.

![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/conversion-rates-downloader/conversion-rate-download-rule.png)

Campos a tener en cuenta:

- **De Moneda**: Moneda de origen.  
- **A Moneda**: Moneda de destino.  
- **Tolerancia**: Diferencia máxima permitida entre el nuevo rango y el anterior. Esto evita insertar valores extremos durante periodos de volatilidad.

### Procesamiento de Peticiones

:material-menu: `Aplicación` > `Configuración General` > `Planificador de procesos` > `Procesamiento de Peticiones`

Para planificar la descarga automática:

1. Cree un nuevo registro y seleccione **`Conversion Rate Downloader`** en el campo *Proceso*.
2. Establezca la frecuencia deseada (p. ej., una vez al día).
3. Planifique y guarde el proceso.

!!! info
    La pestaña **Monitor de Procesos** permite revisar el estado de ejecución y posibles errores.

![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/conversion-rates-downloader/process-request.png)

## Ejecución

### Rangos de conversión

:material-menu: `Aplicación` > `Configuración General` > `Aplicación` > `Rangos de conversión`

El sistema descargará e insertará los rangos de conversión automáticamente según la planificación definida.

!!! info
    Para más información, visite la documentación de [Rangos de conversión](../../../basic-features/general-setup/application/conversion-rates.md).

![alt text](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/conversion-rates-downloader/conversion-rates.png)


---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.