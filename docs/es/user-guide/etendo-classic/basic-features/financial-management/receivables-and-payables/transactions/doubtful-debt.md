---
tags:
  - Etendo Classic
  - Financial Management
  - Doubtful Debt
  - Bad Debt
  - Receivables and Payables
---

# Dudoso cobro

:material-menu: `Aplicación` > `Gestión Financiera` > `Cobros y Pagos` > `Transacciones` > `Dudoso cobro`

## Visión General

Los dudosos cobros son aquellas deudas que la empresa probablemente no podrá cobrar. Además, un dudoso cobro se convierte en deuda incobrable cuando ya no existe duda alguna de que la deuda es irrecuperable, por tanto:

- **Dudoso cobro**: crédito por cobrar que podría convertirse en deuda incobrable en algún momento en el futuro.
- **Deuda Incobrable**: crédito por cobrar que ha sido claramente identificado como no cobrable.

Los dudosos cobros son útiles para hacer provisiones ante posibles pérdidas con antelación.

### Ejemplo de Uso

El siguiente ejemplo ilustra cómo Etendo gestiona la contabilización de Dudosos cobros en el libro mayor.

El Tercero Healthy Food Supermarkets, Co., que debe a la empresa 1.000 EUR, atraviesa una situación difícil, por lo que su deuda se considera de dudoso cobro.

|                       |       |        |
| --------------------- | ----- | ------ |
| Cuenta                | Debe  | Haber  |
| Cuenta de Dudoso cobro | 1000  |        |
| Créditos de Clientes  |       | 1000   |

|                                          |       |        |
| ---------------------------------------- | ----- | ------ |
| Cuenta                                   | Debe  | Haber  |
| Cuenta de Gastos por Deudas Incobrables  | 1000  |        |
| Provisión para Deudas de Dudoso cobro    |       | 1000   |

El Tercero Healthy Food Supermarkets, Co. realiza un Pago de 350 EUR:

|                                       |       |        |
| ------------------------------------- | ----- | ------ |
| Cuenta                                | Debe  | Haber  |
| Cuenta de Cobro en Tránsito           | 350   |        |
| Cuenta de Dudoso cobro                |       | 350    |

|                                          |       |        |
| ---------------------------------------- | ----- | ------ |
| Cuenta                                   | Debe  | Haber  |
| Provisión para Deudas de Dudoso cobro    | 350   |        |
| Cuenta de Ingresos por Deudas Incobrables |       | 350    |

Posteriormente, el tercero quiebra, por lo que su deuda se considera incobrable:

|                        |       |        |
| ---------------------- | ----- | ------ |
| Cuenta                 | Debe  | Haber  |
| Cancelación            | 650   |        |
| Cuenta de Dudoso cobro |       | 650    |

|                                          |       |        |
| ---------------------------------------- | ----- | ------ |
| Cuenta                                   | Debe  | Haber  |
| Provisión para Deudas de Dudoso cobro    | 650   |        |
| Cuenta de Ingresos por Deudas Incobrables |       | 650    |

### Configuración

Antes de comenzar a trabajar con Dudosos cobros, se requieren algunos pasos de configuración previos:

- Configurar la Contabilidad de Dudosos cobros. Las cuentas que deben configurarse son:
  - Cuenta de Dudoso cobro
  - Cuenta de Gastos por Deudas Incobrables
  - Cuenta de Ingresos por Deudas Incobrables
  - y Cuenta de Provisión para Deudas Incobrables.
- Crear una Preferencia para poder ver el importe de una deuda que ha sido clasificada como dudosa al recibir un Pago.  
  Esta preferencia debe definirse para la Entidad y la Organización que necesite verla.  
  Esta preferencia es un Atributo 'Doubtful_Debt_Visibility' cuyo Valor debe ser 'Y'
- Crear un Tipo de Documento para Dudosos cobros.  
  Este paso no es obligatorio, ya que ya existe un Tipo de Documento Estándar definido para Dudosos cobros.

### Dudoso cobro

Los Dudosos cobros se definen en la ventana Procesado del dudoso cobro. Una vez creados, aparecerá un registro en la grilla de esta ventana.

Campos a destacar:

- **Procesado del dudoso cobro:** Un enlace al Procesado del dudoso cobro que generó este Dudoso cobro.
- **Plan de pago de Factura:** Un enlace al Plan de Pagos de la Factura a la que está relacionado este Dudoso cobro.
- **Importe de Dudoso cobro Pendiente:** Importe de Dudoso cobro que permanece pendiente.

Acciones posibles:

- **Reactivar:** Un Dudoso cobro puede ser Reactivado para ser modificado o eliminado posteriormente. Tenga en cuenta que, como cualquier otro documento, no puede ser Reactivado si está Contabilizado. En ese caso, es necesario Descontabilizarlo primero.
- **Contabilizar:** Un Dudoso cobro puede ser contabilizado, creando un asiento en el Libro Mayor que debería verse así:

|                        |                          |                          |
| ---------------------- | ------------------------ | ------------------------ |
| Cuenta                 | Debe                     | Haber                    |
| Cuenta de Dudoso cobro | Importe de Dudoso cobro  |                          |
| Créditos de Clientes   |                          | Importe de Dudoso cobro  |

|                                         |                          |                          |
| --------------------------------------- | ------------------------ | ------------------------ |
| Cuenta                                  | Debe                     | Haber                    |
| Cuenta de Gastos por Deudas Incobrables | Importe de Dudoso cobro  |                          |
| Provisión para Deudas de Dudoso cobro   |                          | Importe de Dudoso cobro  |

### Contabilidad

Información contable relacionada con el dudoso cobro.

## Contabilización Masiva

!!! info
    Para poder incluir esta funcionalidad, se debe instalar el Financial Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, la compatibilidad con el núcleo y las nuevas funcionalidades, visite [Financial Extensions - Notas de versión](../../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

La funcionalidad de Contabilización Masiva permite al usuario contabilizar o descontabilizar múltiples registros seleccionándolos y haciendo clic en el botón **Contabilización masiva**.

Además, el Estado Contable del/los registro/s se muestra en la barra de estado, en la vista de formulario, o en una columna, en la vista de grilla.

!!! info
    Para más información, visite [la guía de usuario del módulo Contabilización Masiva](../../../../optional-features/bundles/financial-extensions/bulk-posting.md).

---

This work is a derivative of [Financial Management](http://wiki.openbravo.com/wiki/Financial_Management){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
