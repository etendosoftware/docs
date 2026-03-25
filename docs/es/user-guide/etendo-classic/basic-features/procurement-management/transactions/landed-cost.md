---
title: Landed Cost
tags:
    - Proceso de Compras
---

# Landed Cost

:material-menu: `Aplicación` > `Gestión de Compras` > `Transacciones` > `Landed Cost`

La ventana **Landed Cost** permite al usuario asignar costes adicionales como transporte, seguro o aranceles a albarán(es), por lo tanto el coste de los productos incluidos en el/los albarán(es) se ajusta según corresponda.

Todos esos costes son necesarios para colocar el producto en el almacén de la organización.

Cada vez que se contabiliza un landed cost para un albarán de producto valorado a coste "Average", se crea un ajuste de landed cost.

Los landed costs distribuidos y asignados a productos valorados a coste "Average" implican un cambio en el valor de inventario del producto. En otras palabras, el coste calculado ("Coste Total") del albarán del producto deberá ajustarse del mismo modo que el coste "Average" del producto.

!!! info
    Ten en cuenta que el "Coste Unitario" de la transacción del albarán no cambiará, ya que este tipo de ajuste no es un ajuste de coste unitario sino un coste "extra".

Todo lo anterior tendrá un impacto contable, por lo tanto el valor de inventario del producto puede ser el mismo que el valor contable del producto.

Por otro lado, si se contabiliza un landed cost para un albarán de producto valorado a coste "Standard", no se creará ningún ajuste de coste, sino una "Desviación" entre el coste "standard" definido para el producto y su coste "actual". Esta desviación deberá contabilizarse en una cuenta de "Landed Cost Variance", para que pueda analizarse posteriormente.

La ventana **Landed Cost** permite:

- o bien contabilizar landed cost "**estimado**" que posteriormente puede asociarse con landed cost "actual" por tipo de landed cost,
- o contabilizar directamente landed cost "**actual**" por tipo de landed cost.

La ventana **Landed Cost** también permite contabilizar los landed costs una vez procesados.

Escenario de Landed Cost "**estimado**":

- Se registra un pedido de compra y, después, el correspondiente albarán y la factura de compra.
  En este punto se calcula el coste "average" de los productos incluidos en el albarán.
- Después, los landed costs "estimados" (p. ej. costes de transporte) se asignan al albarán y se registran en la ventana **Landed Cost**.
  El coste de los productos incluidos en el albarán se ajusta entonces del mismo modo que la contabilidad del activo del producto.
- Después, se registra una factura de compra que incluye el importe real del coste de transporte y se contabiliza en el libro mayor.
- A continuación, es posible asociar el landed cost "estimado" con el landed cost "facturado".
  El coste de los productos incluidos en el albarán se ajusta una vez más si existen diferencias entre los importes de landed cost estimado y real.

Escenario de Landed Cost "**actual**":

- Se registra un pedido de compra y, después, el correspondiente albarán y la factura de compra.
  En este punto se calcula el coste "average" de los productos incluidos en el albarán.
- Después, se crea un documento de landed cost para registrar el landed cost real del albarán.
  El coste de los productos incluidos en el albarán se ajusta entonces del mismo modo que la contabilidad del activo del producto.

En resumen, la funcionalidad de landed cost sigue los siguientes pasos detallados:

- **Landed Cost Process**:
  - Se crea un documento de landed cost incluyendo tantos tipos e importes de landed cost diferentes como sea necesario.
  - Este documento de landed cost puede relacionarse con un único albarán, con varios albaranes o con líneas específicas de albarán.
  - Este documento de landed cost puede registrar landed cost "actual" en caso de seleccionar la factura correspondiente, por lo tanto el proceso y la asociación del landed cost se realizan en un solo paso.
  - Se procesa el landed cost.
    - Esta acción crea un *ajuste de landed cost* vinculado al documento de landed cost.
      Este ajuste de coste tiene tantas líneas de ajuste como productos incluidos en el/los albarán(es) seleccionados, por lo tanto el coste de esos productos se ajusta según corresponda.
- **Landed Cost Post**:
  - Una vez procesado un documento de landed cost, puede contabilizarse en el libro mayor, por lo tanto también se ajusta la contabilidad del activo del/de los producto(s).
- **Landed Cost Matching**:
  - La factura de landed cost se registra y se contabiliza en el libro mayor posteriormente.
  - Después, el landed cost "estimado" registrado en el documento de landed cost puede asociarse con los landed costs reales por tipo de landed cost en la factura de landed cost.
  - La asociación de landed cost puede generar un ajuste de coste adicional para el/los producto(s) si los importes de landed cost estimado no fueron los mismos que los importes de landed cost real.
- **Landed Cost Matching Post**:
  - Una vez que el/los landed cost(s) están asociados, pueden contabilizarse, por lo tanto:
    - la contabilidad del activo del/de los producto(s) se ajusta una vez más si aplica,
    - y la contabilización del landed cost obtiene las *dimensiones contables* de la factura de landed cost.
## Cabecera

Un documento de **Landed Cost** puede crearse, procesarse y contabilizarse en esta ventana.

![Landed cost header](../../../../../assets/drive/1YND6qqNXSCzLiiq_PICSVr3GymXZi6_o.png)

Algunos campos a tener en cuenta son:

- **Organización**: es la organización o entidad legal para la cual se necesita registrar el landed cost.
- **Fecha de Referencia**: es la fecha en la que se está creando el documento de landed cost.

**Coste**

Un Documento de Landed Cost puede tener tantas líneas de coste como tipos de landed cost a asignar a los Albaranes seleccionados.

![Landed cost tabs](../../../../../assets/drive/1jbfoYTDqyRZiF3bTwPQkG8OmjpLr0zau.png)

Algunos campos a tener en cuenta son:

- Tipo de Landed Cost: es el tipo de landed cost que se va a asignar a la(s) entrega(s) o línea(s) de entrega seleccionadas en la pestaña **Entrega**.
- **Línea de la factura**: sirve para seleccionar la línea de factura de landed cost correspondiente, si ya está contabilizada, que coincida con el tipo de landed cost que se está introduciendo.  
  Si se selecciona una línea de factura, el importe de la línea de factura se rellena en el siguiente campo "**Importe**".
- **Importe**: es el importe del tipo de landed cost. Este importe puede ser "estimado" o "real" en caso de seleccionar una línea de factura.
- **Moneda**: es la moneda del tipo de landed cost.
  - Es importante remarcar que un documento de landed cost puede incluir tantos tipos de landed cost como se requiera en la moneda requerida.  
    Por ejemplo, un documento de landed cost puede incluir dos líneas de tipo de landed cost, una en USD y otra en EUR.  
    En este escenario, se creará un ajuste de landed cost que incluirá dos líneas. Los importes del ajuste de coste se calcularán en la moneda configurada para la entidad legal a la que pertenece la transacción de producto.
- **Algoritmo de Distribución de Landed Cost**: hay un algoritmo disponible distribuido por Etendo que es "Distribution by Amount".  
  Este algoritmo distribuye el importe del tipo de landed cost proporcionalmente por el importe de la(s) línea(s) de entrega entre la(s) entrega(s) seleccionadas.

Una vez seleccionada(s) la(s) entrega(s) en la pestaña **Entrega**, el documento de landed cost (cabecera) puede procesarse usando el botón de proceso "**Proceso**".

Esta acción crea un ajuste de landed cost vinculado al documento de landed cost.

Este ajuste de coste tiene tantas líneas de ajuste como productos incluidos en el/los albarán(es) seleccionado(s); por tanto, el coste de esos productos se ajusta según corresponda.

Una vez procesado, un documento de landed cost puede:

- **"Reactivated"**: esta acción anula el ajuste de landed cost vinculado al documento de landed cost.
- o **"Post"**, por lo que la contabilidad del activo del producto también se ajusta en consecuencia.

La contabilización de **Landed Cost** crea los siguientes asientos contables en el caso de un tipo de landed cost de "Producto":

|                 |                                                                                                                                                           |                                |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| Cuenta          | Debe                                                                                                                                                      | Haber                          |
| Activo Producto | Importe de Landed Cost "Estimado".<br><br>(\*)Este apunte contable toma las "dimensiones contables" del albarán, como "Proveedor" o "Producto". Ver enlace "Detalle". |                                |
| Gasto Producto  |                                                                                                                                                           | Importe de Landed Cost "Estimado" |

La contabilización de **Landed Cost** crea los siguientes asientos contables en el caso de un tipo de landed cost de "Cuenta":

|                   |                                                                                                                                                           |                                |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| Cuenta            | Debe                                                                                                                                                      | Haber                          |
| [*Activo Producto*] | Importe de Landed Cost "Estimado".<br><br>(\*)Este apunte contable toma las "dimensiones contables" del albarán, como "Proveedor" o "Producto". Ver enlace "Detalle". |                                |
| [*Apunte contable*] |                                                                                                                                                           | Importe de Landed Cost "Estimado" |

#### Procesar Asociación

La asociación entre un landed cost "estimado" y un landed cost "facturado" puede procesarse en:

**1.** La ventana **ALBARÁN** antes de procesar y usando el botón de proceso "**Complete**"

Este escenario tiene lugar siempre que toda la información relacionada con landed cost indicada a continuación esté disponible e introducida en la pestaña Landed Cost del **Albarán**:

- tipos de landed cost
- importes de landed cost
- líneas de factura de landed cost relacionadas

Este escenario crea automáticamente:

- un documento de landed cost en la ventana **Landed Cost** relacionado con el albarán, que contiene toda la información introducida en la pestaña "Landed Cost" del Albarán.  
  Este documento de landed cost ya está procesado y asociado; por tanto, las únicas acciones pendientes son contabilizar el documento de landed cost (cabecera) y contabilizar la asociación de landed cost.
- un ajuste de landed cost que ajusta el coste de cada producto incluido en el Albarán.

**2**. La ventana **Landed Cost PURCHASE INVOICE**, usando el botón de proceso Match LC Cost que se puede encontrar en cada línea de factura de compra de landed cost. Después se selecciona la casilla **"Process Matching"**.

Este escenario tiene lugar cuando:

- se introdujeron todos los datos relacionados con landed cost excepto la información de la línea de factura de landed cost en la pestaña Landed Cost de la ventana **Albarán**.
- se introdujeron todos los datos relacionados con landed cost excepto la información de la línea de factura de landed cost en la pestaña **Coste** de la ventana **Landed Cost**.

Este escenario crea automáticamente:

- un nuevo ajuste de landed cost que ajusta una vez más el coste de cada producto incluido en el Albarán si:
  - el importe del tipo de landed cost registrado no es el mismo que el facturado
  - y se selecciona la casilla "Is matching adjusted".
- la única acción pendiente es contabilizar la asociación de landed cost.

**3.** La ventana **LANDED COST**, usando el botón de proceso "**Procesar Asociación**"

Este escenario tiene lugar cuando la asociación se ha ejecutado en la factura de compra de landed cost (ver escenario 2 anterior), pero allí no se seleccionó la casilla "Process Matching".

Este escenario crea automáticamente:

- un nuevo ajuste de landed cost que ajusta una vez más el coste de cada producto incluido en el Albarán si el importe del tipo de landed cost registrado no es el mismo que el facturado y se selecciona la casilla "Is matching adjusted".
- la única acción pendiente es contabilizar la asociación de landed cost.

**4.** La ventana **LANDED COST**, usando el botón de proceso "**Proceso**".

Este escenario tiene lugar cuando toda la información relacionada con landed cost se introduce en la ventana **Landed Cost**:

- tipos de landed cost
- importes de landed cost
- líneas de factura de landed cost relacionadas
- y albarán(es)

Este escenario crea automáticamente:

- un ajuste de landed cost que ajusta el coste de cada producto incluido en el/los Albarán(es).
- las únicas acciones pendientes son contabilizar el documento de landed cost (cabecera) y contabilizar la asociación de landed cost.

#### Contabilizar Asociación

Una asociación de landed cost puede contabilizarse después de ser procesada. Esta contabilización tendrá diferentes asientos contables dependiendo de los escenarios listados a continuación:

1\. Landed cost "**Estimado**" **igual** a landed cost "**facturado**"

- En el caso de un tipo de landed cost de "producto"

|                     |                                           |                                                                                                                                                                        |
| ------------------- | ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cuenta              | Debe                                      | Haber                                                                                                                                                                  |
| [*Gasto Producto*]  | Importe de Landed Cost "Estimado"="Facturado" |                                                                                                                                                                        |
| [*Gasto Producto*]  |                                           | Importe de Landed Cost "Estimado"="Facturado"<br><br>(\*)Este apunte contable toma las "dimensiones contables" de la factura de landed cost, como "Tercero". Ver enlace "Detalle". |

- En el caso de un tipo de landed cost de "cuenta"

|              |                                           |                                                                                                                                                                        |
| ------------ | ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cuenta       | Debe                                      | Haber                                                                                                                                                                  |
| [*Apunte contable*] | Importe de Landed Cost "Estimado"="Facturado" |                                                                                                                                                                        |
| [*Apunte contable*] |                                           | Importe de Landed Cost "Estimado"="Facturado"<br><br>(\*)Este apunte contable toma las "dimensiones contables" de la factura de landed cost, como "Tercero". Ver enlace "Detalle". |

El propósito de los asientos anteriores es que la contabilidad del gasto de landed cost tome las "dimensiones contables" de la factura de landed cost.

2\. Landed cost "**Estimado**" no igual a landed cost "**facturado**" & **"Is matching adjusted" = No**.

Esta última configuración ("Is matching adjusted" = No) implica NO crear un ajuste de landed cost que lleve la diferencia al coste del producto (contabilidad del producto); por tanto, esa diferencia permanece bien en el haber (estimado>facturado) o bien en el debe (estimado<facturado) de la cuenta de gasto de producto.

- En el caso de un tipo de landed cost de "producto"

|                     |                               |                                                                                                                                                            |
| ------------------- | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cuenta              | Debe                          | Haber                                                                                                                                                     |
| [*Gasto Producto*]  | Importe de Landed Cost "Facturado" |                                                                                                                                                            |
| [*Gasto Producto*]  |                               | Importe de Landed Cost "Facturado"<br><br>(\*)Este apunte contable toma las "dimensiones contables" de la factura de landed cost, como "Tercero". Ver enlace "Detalle". |

- En el caso de un tipo de landed cost de "cuenta"

|              |                               |                                                                                                                                                            |
| ------------ | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cuenta       | Debe                          | Haber                                                                                                                                                     |
| [*Apunte contable*] | Importe de Landed Cost "Facturado" |                                                                                                                                                            |
| [*Apunte contable*] |                               | Importe de Landed Cost "Facturado"<br><br>(\*)Este apunte contable toma las "dimensiones contables" de la factura de landed cost, como "Tercero". Ver enlace "Detalle". |

3\. Landed cost "**Estimado**" **mayor** que landed cost "**facturado**". **"Is matching adjusted" = Yes**

Esta última configuración ("Is matching adjusted" = Yes) implica crear un ajuste de landed cost que lleva la diferencia al coste del producto (haber de la contabilidad del producto).

- En el caso de un tipo de landed cost de "producto"

|                     |                                |                                                                                                                                                            |
| ------------------- | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cuenta              | Debe                           | Haber                                                                                                                                                     |
| [*Gasto Producto*]  | Importe de Landed Cost "Estimado" |                                                                                                                                                            |
| [*Gasto Producto*]  |                                | Importe de Landed Cost "Facturado"<br><br>(\*)Este apunte contable toma las "dimensiones contables" de la factura de landed cost, como "Tercero". Ver enlace "Detalle". |
| [*Activo Producto*] |                                | Diferencia (estimado>facturado) Importe de Landed Cost                                                                                                     |

- En el caso de un tipo de landed cost de "cuenta"

|                   |                                |                                                                                                                                                            |
| ----------------- | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cuenta            | Debe                           | Haber                                                                                                                                                     |
| [*Apunte contable*] | Importe de Landed Cost "Estimado" |                                                                                                                                                            |
| [*Apunte contable*] |                                | Importe de Landed Cost "Facturado"<br><br>(\*)Este apunte contable toma las "dimensiones contables" de la factura de landed cost, como "Tercero". Ver enlace "Detalle". |
| [*Activo Producto*] |                                | Diferencia (estimado>facturado) Importe de Landed Cost                                                                                                     |

4\. Landed cost "**Estimado**" **menor** que landed cost "**facturado**". **"Is matching adjusted" = Yes**

Esta última configuración ("Is matching adjusted" = Yes) implica crear un ajuste de landed cost que lleva la diferencia al coste del producto (debe de la contabilidad del producto).

- En el caso de un tipo de landed cost de "producto"

|                     |                                                    |                                                                                                                                                            |
| ------------------- | -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cuenta              | Debe                                               | Haber                                                                                                                                                     |
| [*Activo Producto*] | Diferencia (estimado<facturado) Importe de Landed Cost |                                                                                                                                                            |
| [*Gasto Producto*]  | Diferencia (estimado<facturado) Importe de Landed Cost |                                                                                                                                                            |
| [*Gasto Producto*]  |                                                    | Importe de Landed Cost "Facturado"<br><br>(\*)Este apunte contable toma las "dimensiones contables" de la factura de landed cost, como "Tercero". Ver enlace "Detalle". |

- En el caso de un tipo de landed cost de "cuenta".

|                   |                                                    |                                                                                                                                                            |
| ----------------- | -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cuenta            | Debe                                               | Haber                                                                                                                                                     |
| [*Activo Producto*] | Diferencia (estimado<facturado) Importe de Landed Cost |                                                                                                                                                            |
| [*Apunte contable*] | Diferencia (estimado<facturado) Importe de Landed Cost |                                                                                                                                                            |
| [*Apunte contable*] |                                                    | Importe de Landed Cost "Facturado"<br><br>(\*)Este apunte contable toma las "dimensiones contables" de la factura de landed cost, como "Tercero". Ver enlace "Detalle". |

#### Cancelar Asociación

Una asociación de landed cost puede cancelarse usando el botón de proceso de cabecera "**Cancelar Asociación**". Antes de eso, la asociación de landed cost necesita ser "Unpost".

La acción de cancelar la asociación implica que:

- Los importes asociados actuales no se eliminan de la pestaña **Importe Asociado**.
- Se debe ejecutar una nueva asociación en la(s) factura(s) de compra de landed cost correspondiente(s).
- Los importes de asociación correctos se actualizarán entonces en la pestaña **Importe Asociado**.

### Importe Asociado

La pestaña **Importe Asociado** es de solo lectura y permite revisar las líneas de factura de compra asociadas contra las líneas de landed cost.

### Contabilidad Coste

Esta pestaña proporciona información contable del documento de Landed Cost.

Como cualquier otra pestaña de contabilidad, esta pestaña muestra los asientos del libro mayor de la contabilización del landed cost.

### Entrega

La pestaña **Entrega** permite al usuario seleccionar la(s) entrega(s) o línea(s) de entrega a las que se van a asignar los tipos de landed cost registrados.

Una vez que la cabecera de **Landed Cost** se ha rellenado correctamente y se ha guardado, se puede registrar una línea de entrega en esta pestaña.

Los importes de landed cost introducidos en la pestaña "Coste" pueden entonces asignarse/distribuirse entre la(s) entrega(s) introducidas aquí.

Algunos campos relevantes a tener en cuenta son:

- **Good Receipt**: sirve para seleccionar un albarán; por tanto, los importes de landed cost se distribuirán entre todas las líneas del albarán.
- **Good Receipt Line**: sirve para seleccionar una línea específica de albarán.

Ten en cuenta que en un registro debe seleccionarse o bien un albarán o bien una línea de albarán.

### Importe de la Línea de Albarán

**Importe de la Línea de Albarán** es una pestaña de solo lectura que muestra información detallada sobre la línea de tipo de landed cost asignada a cada línea de entrega, así como el importe de landed cost distribuido a cada línea de entrega.

Es importante remarcar que el "Importe" distribuido se calcula teniendo en cuenta la precisión de "Costing" definida para la Moneda.

### Contabilidad

Esta pestaña proporciona información contable de la asociación de Landed Cost.
## Contabilización Masiva

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el *Financial Extensions Bundle*. Para ello, sigue las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="\_blank"}. Para más información sobre las versiones disponibles, compatibilidad con el core y nuevas funcionalidades, visita [Financial Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

La funcionalidad de **Contabilización Masiva** permite al usuario contabilizar o descontabilizar múltiples registros seleccionando los registros correspondientes y haciendo clic en el botón **Contabilización Masiva**. En este caso, esta funcionalidad puede utilizarse en la ventana **Landed Cost** y en la pestaña **Coste**.

Además, el Estado Contable del/de los registro/s se muestra en la barra de estado, en vista de formulario, o en una columna, en vista de cuadrícula.

!!! info
    Para más información, visita [the Bulk Posting module user guide](../../../../../user-guide/etendo-classic/optional-features/bundles/financial-extensions/bulk-posting.md).

---

Este trabajo es una obra derivada de [Procurement Management](http://wiki.openbravo.com/wiki/Procurement_Management){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.

---
Esta obra está licenciada bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L.](https://etendo.software){target="_blank"}.