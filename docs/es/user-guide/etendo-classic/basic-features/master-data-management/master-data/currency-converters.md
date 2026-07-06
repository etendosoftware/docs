---
title: Conversores de Moneda
tags:
  - Gestión de datos maestros
  - Etendo
  - Moneda
  - Financial Extensions
  - Tipos de cambio
  - Conversión de moneda
---

# Conversores de Moneda { #currency-converters }

:material-menu: `Aplicación` > `Gestión de Datos Maestros` > `Conversores de Moneda`

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Financial Extensions - Notas de la versión](../../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

## Descripción general { #overview }

La ventana **Conversores de Moneda** es donde se introducen los datos de acceso (como una URL y una clave de API) que Etendo necesita para conectarse a un servicio externo que proporciona tipos de cambio diarios. Una vez configurado, el sistema puede descargar los tipos vigentes de forma automática, sin necesidad de introducirlos manualmente. El módulo [Descargador de rangos de conversión](../../../optional-features/bundles/financial-extensions/conversion-rate-downloader.md) utiliza esta configuración para recuperar dichos tipos.


<figure markdown="span">
  ![Ventana Conversores de Moneda con los campos de configuración para la integración con APILayer Currency Data API](../../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/conversion-rates-downloader/currency-converters.png)
  <figcaption>Ventana Conversores de Moneda con una configuración de APILayer Currency Data API.</figcaption>
</figure>


!!! info 
    La ventana Conversores de Moneda es un paso dentro del proceso general de automatización de tipos de cambio. Para consultar el flujo de configuración completo, incluido cómo programar descargas automáticas y definir reglas de conversión, visite la página [Descargador de rangos de conversión](../../../optional-features/bundles/financial-extensions/conversion-rate-downloader.md).

---

This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.
