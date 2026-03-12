---
tags:
    - Facturas de compra
    - Validación
    - Prevención de duplicados
    - Funcionalidades de Etendo
---

# Validaciones de facturas de compra
:octicons-package-16: Paquete Java: `com.etendoerp.purchase.invoice.validations` 

## Visión general
<iframe width="560" height="315" src="https://www.youtube.com/embed/V80-YymMjFg?si=lYvSX9UxojxZVzTG" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Este módulo permite a los usuarios evitar la duplicación de facturas de compra dentro del sistema, siguiendo algunas reglas establecidas. Esta prevención se llevará a cabo mediante una validación que prohibirá el guardado de una factura de compra duplicada. La activación de esta validación estará determinada por una preferencia configurable.

## Criterios de duplicación de facturas

Etendo considerará una factura de compra como duplicada si ya existe otra factura de compra con los mismos datos clave, a saber:

- Tercero
- Referencia del proveedor
- Fecha de factura (año)

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/procurement-extensions/purchaseinvoicevalidation1.png)

Las facturas de compra en el sistema deben tener un número de referencia de proveedor único para cada tercero. Esto significa que si dos facturas de compra, para el mismo tercero, tienen el mismo número de referencia, se consideran duplicadas.

## Preferencias

:material-menu: `Aplicación` > `Configuración General` > `Aplicación` > `Preferencias`

Se utilizará una preferencia configurable del sistema para habilitar o deshabilitar la validación que evita la duplicación de facturas de compra. Esto permite al cliente decidir si utiliza esta funcionalidad o no. La versatilidad de las preferencias permite modificar su visibilidad, determinando si la validación estará activa para todos los usuarios, roles, organizaciones, etc.

Desde la ventana Preferencias, el usuario puede crear una nueva preferencia, eligiendo la propiedad correspondiente, que para esta funcionalidad será Validar facturas de compra duplicadas. En el campo Valor, es necesario añadir Y para habilitar la preferencia o N para deshabilitarla.

!!!note
    De forma predeterminada, existe una preferencia con la propiedad Validar facturas de compra duplicadas y el valor N, lo que significa que está deshabilitada. En caso de que el usuario quiera habilitar esta preferencia, es necesario crear una nueva y marcar la casilla de verificación seleccionada. Para más información, visite [preferencias](../../../../../user-guide/etendo-classic/basic-features/general-setup/application/preference.md)

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/procurement-extensions/purchaseinvoicevalidation2.png)

## Validación

La validación evitará el guardado de una factura de compra que se considere duplicada según los criterios establecidos. Si el sistema detecta que la factura que se está guardando está duplicada, se informará al usuario mediante un mensaje que indicará la naturaleza de la duplicación, tal y como se muestra aquí:

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/procurement-extensions/purchaseinvoicevalidation3.png)

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.