---
tags:
  - Etendo Classic
  - Financial Management
  - Doubtful Debt
  - Bad Debt
  - Receivables and Payables
---

# Deuda Dudosa

:material-menu: `Aplicación` > `Gestión Financiera` > `Cobros y Pagos` > `Transacciones` > `Deuda Dudosa`

## Visión General

Las deudas dudosas son aquellas deudas que la empresa probablemente no podrá cobrar. Además, una deuda dudosa se convierte en deuda incobrable cuando ya no existe duda alguna de que la deuda es irrecuperable, por tanto:

- **Deuda Dudosa**: crédito por cobrar que podría convertirse en deuda incobrable en algún momento en el futuro.
- **Deuda Incobrable**: crédito por cobrar que ha sido claramente identificado como no cobrable.

Las deudas dudosas son útiles para hacer provisiones ante posibles pérdidas con antelación.

### Ejemplo de Uso

El siguiente ejemplo ilustra cómo Etendo gestiona la contabilización de Deudas Dudosas en el libro mayor.

El Tercero Healthy Food Supermarkets, Co., que debe a la empresa 1.000 EUR, atraviesa una situación difícil, por lo que su deuda se considera dudosa.

|                       |       |        |
| --------------------- | ----- | ------ |
| Cuenta                | Debe  | Haber  |
| Cuenta de Deuda Dudosa | 1000  |        |
| Créditos de Clientes  |       | 1000   |

|                                          |       |        |
| ---------------------------------------- | ----- | ------ |
| Cuenta                                   | Debe  | Haber  |
| Cuenta de Gastos por Deudas Incobrables  | 1000  |        |
| Provisión para Deudas Dudosas            |       | 1000   |

El Tercero Healthy Food Supermarkets, Co. realiza un Pago de 350 EUR:

|                                       |       |        |
| ------------------------------------- | ----- | ------ |
| Cuenta                                | Debe  | Haber  |
| Cuenta de Cobro en Tránsito           | 350   |        |
| Cuenta de Deuda Dudosa                |       | 350    |

|                                          |       |        |
| ---------------------------------------- | ----- | ------ |
| Cuenta                                   | Debe  | Haber  |
| Provisión para Deudas Dudosas            | 350   |        |
| Cuenta de Ingresos por Deudas Incobrables |       | 350    |

Posteriormente, el tercero quiebra, por lo que su deuda se considera incobrable:

|                        |       |        |
| ---------------------- | ----- | ------ |
| Cuenta                 | Debe  | Haber  |
| Cancelación            | 650   |        |
| Cuenta de Deuda Dudosa |       | 650    |

|                                          |       |        |
| ---------------------------------------- | ----- | ------ |
| Cuenta                                   | Debe  | Haber  |
| Provisión para Deudas Dudosas            | 650   |        |
| Cuenta de Ingresos por Deudas Incobrables |       | 650    |

### Configuración

Antes de comenzar a trabajar con Deudas Dudosas, se requieren algunos pasos de configuración previos:

- Configurar la Contabilidad de Deudas Dudosas. Las cuentas que deben configurarse son:
  - Cuenta de Deuda Dudosa
  - Cuenta de Gastos por Deudas Incobrables
  - Cuenta de Ingresos por Deudas Incobrables
  - y Cuenta de Provisión para Deudas Incobrables.
- Crear una Preferencia para poder ver el importe de una deuda que ha sido clasificada como dudosa al recibir un Pago.  
  Esta preferencia debe definirse para la Entidad y la Organización que necesite verla.  
  Esta preferencia es un Atributo 'Doubtful_Debt_Visibility' cuyo Valor debe ser 'Y'
- Crear un Tipo de Documento para Deudas Dudosas.  
  Este paso no es obligatorio, ya que ya existe un Tipo de Documento Estándar definido para Deudas Dudosas.

### Deuda Dudosa

Las Deudas Dudosas se definen en la ventana Ejecución de Deudas Dudosas. Una vez creadas, aparecerá un registro en la grilla de esta ventana.

Campos a destacar:

- **Ejecución de Deuda Dudosa:** Un enlace a la Ejecución de Deuda Dudosa que generó esta Deuda Dudosa.
- **Plan de Pago de Factura:** Un enlace al Plan de Pago de la Factura a la que está relacionada esta Deuda Dudosa.
- **Importe de Deuda Dudosa Pendiente:** Importe de Deuda Dudosa que permanece pendiente.

Acciones posibles:

- **Reactivar:** Una Deuda Dudosa puede ser Reactivada para ser modificada o eliminada posteriormente. Tenga en cuenta que, como cualquier otro documento, no puede ser Reactivada si está Contabilizada. En ese caso, es necesario Descontabilizarla primero.
- **Contabilizar:** Una Deuda Dudosa puede ser contabilizada, creando un asiento en el Libro Mayor que debería verse así:

|                        |                          |                          |
| ---------------------- | ------------------------ | ------------------------ |
| Cuenta                 | Debe                     | Haber                    |
| Cuenta de Deuda Dudosa | Importe de Deuda Dudosa  |                          |
| Créditos de Clientes   |                          | Importe de Deuda Dudosa  |

|                                         |                          |                          |
| --------------------------------------- | ------------------------ | ------------------------ |
| Cuenta                                  | Debe                     | Haber                    |
| Cuenta de Gastos por Deudas Incobrables | Importe de Deuda Dudosa  |                          |
| Provisión para Deudas Dudosas           |                          | Importe de Deuda Dudosa  |

### Contabilidad

Información contable relacionada con la deuda dudosa.

## Contabilización Masiva

!!! info
    Para poder incluir esta funcionalidad, se debe instalar el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, la compatibilidad con el núcleo y las nuevas funcionalidades, visite [Financial Extensions - Notas de versión](../../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

La funcionalidad de Contabilización Masiva permite al usuario contabilizar o descontabilizar múltiples registros seleccionándolos y haciendo clic en el botón **Contabilización masiva**.

Además, el Estado de Contabilización del/los registro/s se muestra en la barra de estado, en la vista de formulario, o en una columna, en la vista de grilla.

!!! info
    Para más información, visite [la guía de usuario del módulo Contabilización Masiva](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).

---

This work is a derivative of [Financial Management](http://wiki.openbravo.com/wiki/Financial_Management){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
