---
tags:
    - Finalización masiva
    - Completar
    - Contabilizar
    - Cerrar
---

# Finalización masiva

:octicons-package-16: Javapackage: `com.etendoerp.bulk.completion` 

## Visión general

Esta sección describe el módulo de Finalización masiva incluido en el bundle Essentials Extensions Bundle.

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el bundle Essentials Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Essentials Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=39AC2D9F72124AC7A1D0A3D005293C9E){target="_blank"}. Para más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Essentials Extensions - Notas de la versión](../../../../../whats-new/release-notes/etendo-classic/bundles/essentials-extensions/release-notes.md).

!!! warning
    Antes de utilizar esta funcionalidad, recuerde que procesar múltiples registros al mismo tiempo puede afectar al rendimiento del sistema, especialmente al gestionar un gran volumen de datos.

La funcionalidad de Finalización masiva permite al usuario completar, reactivar o cerrar múltiples registros seleccionándolos y haciendo clic en el botón **Finalización masiva**. Esto facilita y hace más eficiente la gestión de registros, reduciendo el tiempo dedicado a procesar registros individuales.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/essentials-extensions/salesinvoice1.png)

## Completando
Como se muestra aquí, puede seleccionar múltiples registros al mismo tiempo, borradores en este caso, y hacer clic en el botón Finalización masiva para completarlos o contabilizarlos todos a la vez.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/essentials-extensions/salesinvoice2.png)

## Reactivando
Una vez que los registros están completados o contabilizados, el usuario puede reactivar registros de forma masiva. Al reactivar, el registro pasa de estado Completado o Contabilizado a estado Borrador para que pueda modificarse. 

## Anulando
En el caso de facturas, albaranes de proveedor y albaranes de cliente, el usuario puede seleccionar la opción Anular para generar masivamente los documentos revertidos correspondientes.

## Cerrando
Para pedidos, presupuestos y documentos de devolución es posible cerrar múltiples documentos al mismo tiempo.

Esta funcionalidad está disponible en las siguientes ventanas:

- [Presupuesto de ventas](../../../basic-features/sales-management/transactions.md#bulk-completion)
- [Pedido de venta](../../../basic-features/sales-management/transactions.md#bulk-completion_1)
- [Albarán (Cliente)](../../../basic-features/sales-management/transactions.md#bulk-completion_2)
- [Devolución de cliente](../../../basic-features/sales-management/transactions.md#bulk-completion_3)
- [Factura (Cliente)](../../../basic-features/sales-management/transactions.md#bulk-completion_4)
- [Pedido de compra](../../../basic-features/procurement-management/transactions.md#bulk-completion)
- [Albarán (Proveedor)](../../../basic-features/procurement-management/transactions.md#bulk-completion_1)
- [Factura (Proveedor)](../../../basic-features/procurement-management/transactions.md#bulk-completion_2)
- [Devolución a proveedor](../../../basic-features/procurement-management/transactions.md#bulk-completion_3)


Como se ha explicado, el uso de Finalización masiva mejora la eficiencia al permitir a los usuarios realizar acciones sobre documentos de forma masiva, agilizando las operaciones y ahorrando tiempo.

---
Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L](https://etendo.software){target="_blank"}.