---
title: Financial Extensions Bundle | Documentación técnica
---
:octicons-package-16: Paquete Java: `com.etendoerp.financial.extensions`

## Visión general

En esta sección, el usuario puede encontrar información técnica sobre el bundle Financial Extensions.

## Pool bancario

:octicons-package-16: Paquete Java: `com.etendoerp.bankingpool`

### Visión general

Este documento cubre cómo crear un proceso que genere automáticamente un nuevo Plan financiero o actualice un Plan financiero desde la ventana Gestión financiera >> Contabilidad >> Transacciones >> Configuración de tipo financiero. También proporciona una estructura que debe considerarse al crear la clase Java responsable de ejecutar estos nuevos procesos.

### Creación de la nueva clase Java

La clase Java encargada de crear el plan de financiación debe extender la clase Java `FinanceTypeTemplate`. Esta proporciona algunos métodos abstractos que deben implementarse y otros métodos útiles al crear el nuevo proceso. La estructura básica que debe seguir la nueva clase Java es la siguiente:

```java
package com.etendoerp.bankingpool.types;
import com.etendoerp.bankingpool.FinancialTypeConfiguration;
import java.math.BigDecimal;
import java.util.Date;
public class NewFinancialType extends FinanceTypeTemplate {
 @Override
 public void exec(FinancialTypeConfiguration configuration, Date date,
     boolean isNewFinancePlan) {
   if (isNewFinancePlan) {
     for (int paymentNo = 0; paymentNo < configuration.getInstallmentNo(); paymentNo++) {
       //Implement the creation of the new Financing Plan
     }
   } else {
     for (int paymentNo = 0; paymentNo < configuration.getInstallmentNo(); paymentNo++) {
       //Implement the update of the Financing Plan
     }
   }
 }
 @Override
 public BigDecimal getInstallment(FinancialTypeConfiguration configuration,
     BigDecimal totalAmortization, int totalInstallment) {
   //Calculate the value of the Installment
   return null;
 }
 @Override
 public BigDecimal getRecalculatedInstallment(FinancialTypeConfiguration configuration,
     BigDecimal totalAmortization, BigDecimal residualValue, int totalInstallment) {
   //Calculate the value of the installment recalculation
   return null;
 }
}
```

El método Exec es el método que se ejecuta cuando se crea un nuevo Plan financiero o cuando se va a modificar el Plan financiero.

El método Exec recibe 3 parámetros:

-   configuration: El registro de la ventana Configuración de tipo financiero para el que se crea o modifica el nuevo Plan financiero.
-   date: La fecha que se pasa como parámetro al crear un Plan financiero.
-   isNewFinancePlan: Indicador que señala si se está creando o actualizando un nuevo plan financiero. Si se llama desde el botón Crear plan financiero, este parámetro será True y si se llama desde el botón Actualizar plan financiero, el parámetro será False.

La clase abstracta `FinanceTypeTemplate` tiene implementados varios métodos que pueden ser útiles; entre ellos se encuentran:

-   newFinancePlan: Crea un nuevo vencimiento del plan financiero
-   setDate: Asigna una fecha al campo de fecha en un registro de plan financiero
-   setAllDates: Asigna la fecha al nuevo plan de financiación teniendo en cuenta la fecha de pago y la frecuencia definidas en la cabecera
-   getLastFinancePlanWithInvoice: Obtiene el último vencimiento del plan de financiación con una factura
-   getLastFinancePlanWithPayment: Obtiene el último vencimiento del plan de financiación con un pago
-   getMonthlyInterest: Realiza el cálculo (% interés anual/(12/frecuencia))
-   getCapitalizedInterest: (1+% interés mensual)^nº de vencimiento^
-   getResidualValueDivideCapitalizedInterest: Realiza el cálculo Valor residual/Interés capitalizado.
-   setAmortizationRenting: Realiza el cálculo Vencimiento - Interés
-   setTotalAmortization: Calcula el importe total pagado hasta ese momento en el plan financiero
-   setPendingAmortization: Calcula el importe pendiente de pago en el plan financiero
-   setInterest: Realiza el cálculo ((última amortización pendiente\*% interés anual)/12)\*frecuencia
-   setCommission: Asigna la comisión definida en la cabecera
-   setBusinessPartner: Asigna el Banco/Entidad financiera definido en la cabecera
-   setProject: Asigna el Proyecto definido en la cabecera
-   setCostCenter: Asigna el Centro de coste definido en la cabecera
-   setFirstPendingAmortization: Método de cálculo de la amortización pendiente para el primer vencimiento
-   getFinancePlanToRecalculate: Método que obtiene todos los vencimientos del plan de financiación que deben actualizarse si se desea actualizar un plan financiero

Los métodos abstractos deben implementarse en la nueva clase Java y, si se requiere, se puede sobrescribir cualquiera de los métodos de la clase `FinanceTypeTemplate`.

### Creación del nuevo tipo financiero

En la ventana Tipo financiero se crea un nuevo registro con el nuevo tipo financiero y en el campo Nombre de clase se introduce el paquete de la clase Java implementada seguido del nombre de la clase Java.

![](../../../assets/drive/O0wwVyzJUyoTZblrURHjjOMPgcwQ1-NPr8XlI1qaE37Mo0PQ1WVVdHlOV1YPDpBjbzzeDaOgIsWoS01ptNgGT3_VintShkcxoZGdioZ8jTNuk-CyXUxZNjmSa8YaEKwlP58Gv3AXBmqEmdG2IQ.png)

Con solo completar el campo Nombre de clase, serán visibles los botones Crear nuevo plan de financiación y Actualizar plan de financiación.

![](../../../assets/drive/aq3IBl8B85MUhWR_N0Buo6qjtcxAhESwYOpGkh8Hn1X-ka9jGGVpgfaW3jzbzfuY2Bca2F3O-zPaU3GEtdYEVLy2_u0_f1wVNF3rjteWPBBbCFIM4Lv_ZW5FEMni5EVA2IKgtiOckQPrzhSa1g.png)

![](../../../assets/drive/_r4oVdOsDGq8rLR2_c2foimTnGGh66TGlUIs1J_ZiWG4yuSXnNNMLDFAwtN4D6w_GU_XjgJ8Ix5s9KF4jrTAKHsdLliRdPS06BqHgl8hPYmf9QvYfbg9oOwWRUp9pBNbhcIDN6KOtS07OornYw.png)

No es necesario modificar ninguno de los 2 botones, ya que ejecutan automáticamente el método Exec de la clase Java especificada en el Tipo financiero.

## Procesamiento avanzado de documentos financieros

:octicons-package-16: Paquete Java: `com.etendoerp.advanced.financial.docs.processing`

:octicons-package-16: Paquete Java: `com.etendoerp.advanced.financial.docs.processing.template`

### Hooks para deshacer pedidos cerrados / rehabilitar facturas anuladas

Se han añadido nuevos hooks a los procesos "Deshacer cierre" y "Rehabilitar", desde los pedidos de venta/compra y las facturas, respectivamente.  
Estos hooks permiten al desarrollador añadir nuevas validaciones antes y/o después de que se ejecute la acción y, de este modo, crear nuevas automatizaciones más fácilmente.

### Cómo definir una instancia de UnvoidInvoiceHook
- Defina la clase del hook, implementando la interfaz `UnvoidInvoiceHook`. Este hook se ejecuta cuando un usuario intenta rehabilitar una factura anulada:

```
public class UnvoidInvoiceImpl implements UnvoidInvoiceHook {
  @Override
  public OBError preProcess(Invoice invoice) {
    System.out.println("This is an example of pre method hook");
    return new OBError();
  }

  @Override
  public OBError postProcess(Invoice invoice) {
    System.out.println("This is an example of post method hook");
    return new OBError();
  }
}
```

### Cómo definir una instancia de UndoCloseOrderHook
- Defina la clase del hook, implementando la interfaz UndoCloseOrderHook. Este hook se ejecuta cuando un usuario intenta deshacer un pedido cerrado:

```
public class UndoOrderImpl implements UndoCloseOrderHook {

  @Override
  public OBError preProcess(Order order) {
    System.out.println("This is an example of pre method hook");
    return new OBError();
  }

  @Override
  public OBError postProcess(Order order) {
    System.out.println("This is an example  of post method hook");
    return new OBError();
  }
}
```


---
Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L](https://etendo.software){target="_blank"}.