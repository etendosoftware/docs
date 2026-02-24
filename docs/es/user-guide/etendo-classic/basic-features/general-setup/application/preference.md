---
title: Preferencias
tags:
    - Preferencias
    - Sesión
    - Atributo
    - Propiedad
---

# Preferencias

:material-menu: `Aplicación` > `Configuración General` > `Aplicación` > `Preferencias`

## Visión general

Una preferencia es un tipo de valor de sesión que puede ser un atributo o una propiedad.

!!! info
    Cada vez que un usuario inicia sesión en Etendo, se abre una nueva sesión.

Durante el inicio de sesión, el usuario introduce varias variables como el **Rol**, la **Entidad** y la **Organización** y, una vez dentro, el usuario navega a una **Ventana**.

Todas esas variables tienen una influencia clave en los valores de sesión que obtendrá el usuario.

En otras palabras, las **Preferencias** permiten al usuario definir valores de sesión, valores de sesión que pueden ser una propiedad o un atributo definidos para una única entidad o para todas ellas, o para una única organización o para todas ellas.

!!! info
    Las preferencias pueden asignarse al sistema o a un módulo específico; por lo tanto, al exportar ese módulo, también se exportarán las preferencias que tenga asignadas, de modo que esos ajustes generales puedan reutilizarse.

Por ejemplo, existe una **Propiedad** denominada *Implementa un botón alternativo de Proceso de Factura*. Esa propiedad existente está actualmente asignada al módulo "Advanced Payables and Receivables Management" con un valor = "Y" para cualquier entidad, organización, usuario, rol y ventana:

- La preferencia anterior significa que, si el módulo Advanced Payables and Receivables Management está instalado, utilizará un botón alternativo de proceso de factura; además, todos los usuarios que inicien sesión en Etendo tendrán esa funcionalidad activa independientemente de su rol, usuario y de la entidad u organización en la que estén trabajando.

Por ejemplo, existe un **Atributo** denominado *Autoguardado* que actualmente está asignado al sistema con un valor "Y". Este atributo es visible y, por tanto, aplicable a la entidad Sistema y a la organización (\*) para cualquier usuario, rol y ventana.

- La preferencia anterior significa que todos los usuarios que inicien sesión en Etendo tendrán esa funcionalidad activa independientemente de su rol y usuario y de la entidad u organización en la que estén trabajando.

## Preferencias

La ventana Preferencias permite al usuario definir y mantener valores de sesión que pueden ser visibles y, por tanto, aplicarse a diferentes niveles como **Entidad**, **Organización**, **Usuario**, **Rol** y **Ventana**.

### Definición de Preferencias

![](../../../../../assets/drive/ORFZT6LvzmxT-rOY-l1Xw07GvftHNxLMJU6RxtHo8LmMioTFNJMYUcITNJlA5xrvFyW8PMzRi2grIoMM-tFBiotCV4s3YNbUzC5G7UyavRacVSjEpYLuQQtdo9v_aTHWIgVHoM1w.png)

Como se muestra en la imagen anterior, existe un campo denominado *Lista de Propiedades* que es clave para definir una preferencia como propiedad o como atributo:

- Si la casilla de verificación *Lista de Propiedades* está marcada, la preferencia se configura como una **propiedad** que se tomará de una lista existente de propiedades.  
  Ya existen muchos tipos de propiedades creadas; además, **los módulos pueden añadir nuevas propiedades a esa lista** con el objetivo de que esos otros módulos o incluso el sistema puedan utilizarlas estableciendo los valores de propiedad correspondientes.  
  Algunas de las propiedades disponibles se listan y se explican brevemente a continuación:

    ![](../../../../../assets/drive/U-6eYqg2DbvQutUsYua4ZGYyN6m1Eg0Kf0kmS2ONtUO0l12g9IUSmE9NWCAHuLBjiy9IQt_dS1PG71TEorFR55Jg3z2S_UUBUq8NwYaCp-BUa1b5d6q9ZIquttmiYsoQzFKV4rR6.png)

    - **Habilitar la gestión de UdM**  
    Si se establece en Valor = "Y" a nivel "Sistema", permite al usuario definir una UdM alternativa para un producto, además de la UdM del producto.  
    Del mismo modo, se mostrará un nuevo campo denominado "_Cantidad Operativa_" en documentos de transacciones de compras, inventario y ventas; por lo tanto, "Cant. pedido", "Cant. movida" y "Cant.facturada" siempre muestran la "Cantidad Operativa" introducida por el usuario final, convertida a la UdM del producto.  
    - **Habilitar correcciones automáticas de diferencias de precio**  
    Si se establece en Valor = "Y", permite la creación de ajustes de coste de corrección de diferencias de precio.
    - **Habilitar correcciones de stock negativo**  
    Si se establece en Valor = "Y", permite la creación de ajustes de coste de corrección de stock negativo.
    - **Habilitar Cancelar y Reemplazar**  
    Si se establece en Valor = "Y", permite Cancelar y Reemplazar pedidos de venta contabilizados.
    - **Cancelar y Reemplazar - Asociar líneas de albarán al nuevo pedido**  
    Esta preferencia requiere que la preferencia "Habilitar Cancelar y Reemplazar" esté habilitada, y solo funciona si la preferencia "Crear albarán de compensación en Cancelar y Reemplazar" no está habilitada.  
    Si se establece en Valor = "Y", asigna el/los albarán/es relacionados con las líneas del pedido de venta cancelado a las líneas del pedido de venta reemplazado.
    - **Cancelar y Reemplazar - Crear albarán de mercancías de compensación**  
    Esta preferencia requiere que la preferencia "Habilitar Cancelar y Reemplazar" esté habilitada, y solo funciona si la preferencia "Cancelar y Reemplazar - Asociar líneas de albarán al nuevo pedido" no está habilitada.  
    Si se establece en Valor = "Y", crea y completa automáticamente un albarán de mercancías de "compensación" relacionado con los pedidos de venta cancelados, anulados y reemplazados.
    - **Codificación de texto CSV**  
    Si se establece en Valor = "Y" permite especificar la codificación que se utilizará en el proceso Exportar a CSV.
    - **Configuración de la cuadrícula**  
    Si se establece en Valor = "Y", cada vez que un usuario cambia una vista de cuadrícula, esos cambios se guardan en esta ventana vinculada a esta propiedad.
    - **Implementa el cálculo de Crédito Usado del cliente**  
    Esta propiedad está actualmente asignada al módulo Advanced Payables and Receivables Management con un valor de propiedad ="Y". Esta propiedad evita el cálculo de la función C_BP_SOCREDITUSED_REFRESH.
    - **Implementa un botón alternativo de Proceso de Factura**  
    Esta propiedad también está asignada al módulo Advanced Payables and Receivables Management con un valor de propiedad ="Y". Esta propiedad evita el uso del botón estándar del proceso de factura.
    - **Implementa una Gestión Financiera alternativa**  
    Lo mismo aplica a esta, que permite una gestión financiera alternativa para ese módulo.
    - **Implementa la gestión del Monitor de Pagos**  
    Lo mismo aplica a esta, que deshabilita el proceso en segundo plano estándar y el botón en la cabecera de la factura que gestionan el monitor de pagos.
    - **Vistas recientes mostradas en el espacio de trabajo** propiedad establecida en "Y"  
    Esto permite que las vistas recientes se muestren en el espacio de trabajo del usuario.
    - **Mostrar campos de MRP y Producción** propiedad establecida en "Y"  
    Esto permite que se muestren los campos de MRP y producción.
    - **No permitir cambiar el tipo de cambio y el importe**  
    Si establece esta propiedad con valor = "Y", el tipo de cambio y el importe son de solo lectura en Añadir Pago desde Factura de Venta, Factura de Compra, Cobro, Pago, Cuenta Financiera, en Seleccionar Pagos Esperados desde Propuesta de Pago y en Transferencia de Fondos desde Cuenta Financiera.
    - **Límite de cancelación**  
    Esta propiedad con un valor de propiedad ="Y" permite configurar el límite de cancelación en Añadir Pago desde Factura de Venta, Factura de Compra, Cobro, Pago, Cuenta Financiera y en Seleccionar Pagos Esperados desde Propuesta de Pago. El límite de cancelación se establece para cada Cuenta Financiera en la ventana Cuenta Financiera.
    - **Mostrar padres de Características de Producto**  
    Los valores pueden ser 1,2,3,4, etc. El número indica cuántos Nivel en el árbol jerárquico desea mostrar el usuario en la vista de formulario en la ventana Producto. Por ejemplo, si el árbol es: Color->Verde->Verde claro->0034
    - **Permitir múltiples pestañas de Ventana**  
    Si se establece en Valor = _'Y'_ permite abrir más de una pestaña de una misma ventana.
    - **Adjuntar por defecto**
    - Si se establece en Valor = 'Y' no se mostrará el popup "Imprimir documento"; este popup es el que pregunta si el usuario desea adjuntar el documento o, en su lugar, simplemente imprimirlo sin adjuntarlo. Cuando el valor de la preferencia se establece en 'Y', el documento se adjuntará automáticamente.
    - Si se establece en Valor = 'N' no se mostrará el popup "Imprimir documento"; este popup es el que pregunta si el usuario desea adjuntar el documento o, en su lugar, simplemente imprimirlo sin adjuntarlo. Cuando el valor de la preferencia se establece en 'N', el documento no se adjuntará.
    - Si el Valor no está definido, se mostrará el popup "Imprimir documento" con dos opciones: "Sí" y "No, solo imprimirlo". Si se selecciona "Sí", el documento se adjuntará. Si se selecciona "No, solo imprimirlo", el documento no se adjuntará.
    - **Impresión directa**
    Si se establece en Valor = 'Y' se habilita el modo de Impresión directa.
    Si se establece en Valor = 'N' o no está definido, se utiliza el modo de impresión estándar.
    - **Permitir parámetro Where**
    Si se establece en Valor = 'Y', permite obtener el parámetro "\_where" de datasources manuales. Se mostrará una advertencia si se envía el parámetro "\_where".
    Si se establece en Valor = 'N' o no está definido, no permitirá obtener el parámetro "\_where" de datasources manuales. Se lanzará una excepción si se envía el parámetro "\_where".
    - **Permitir solicitud de Datasource no segura**
    Si se establece en Valor = 'Y', permite realizar una solicitud de datasource no segura. Se mostrará una advertencia si el rol actual no tiene acceso.
    Si se establece en Valor = 'N' o no está definido, no permitirá realizar una solicitud de datasource no segura. Se requiere un rol con permisos de acceso suficientes. Se lanza una OBSecurityException si el rol actual no tiene acceso.
    - **Reconstrucción externa**, cuando esta preferencia se define a nivel de sistema con su valor establecido en _Y_, no será posible reconstruir el sistema desde la Consola del Gestor de Módulos después de instalar/actualizar módulos. Obliga a reconstruir el sistema desde la línea de comandos.
    - **Omitir comprobación de nivel de acceso de Entidad**, cuando esta preferencia se define con su valor establecido en _Y_, permitirá omitir la comprobación que compara el nivel de usuario del rol con el nivel de acceso de la entidad para evitar completamente el acceso a esta última.
    - **Traducir referencia Sí/No en Exportar a CSV**, cuando esta preferencia se define con su valor establecido en _Y_, el valor de las columnas cuya referencia es _Sí/No_ se traducirá al idioma del contexto actual al exportar la cuadrícula de una ventana estándar a CSV.
    - **Deshabilitar sección de elementos vinculados**, cuando esta preferencia se define para una ventana con su valor establecido en _Y_, la sección Elementos vinculados se deshabilitará para esa ventana. Si no hay ninguna ventana definida en los ajustes de visibilidad, esta sección se deshabilitará para todas las ventanas de la aplicación.
    - **Habilitar lector de pantalla**, si esta preferencia se establece en _Y_ se habilitará el lector de pantalla completo. Esto mejorará la accesibilidad para personas con discapacidad visual.
    - **Formato de exportación a Excel**, esta preferencia permite establecer el formato de exportación que se utilizará al generar informes de Excel. Se admiten dos valores: _XLS_ o _XLSX_. Cuando esta preferencia no está definida, _XLSX_ es el formato de exportación a Excel por defecto.
    - **Filtrar por documentos procesados desde hace N días** está relacionado con Crear líneas desde en Factura de Venta/Compra. Limita las transacciones desde la fecha actual hasta los días definidos hacia atrás. Si la preferencia no está definida, las consultas recuperan todos los registros creados desde hace un año (365 días); en caso contrario, se filtrará por el número de días definido como valor de la preferencia.
    
- Si la casilla de verificación *Lista de Propiedades* no está marcada, la preferencia se configura como un **atributo**. Un atributo es un atributo de texto libre que puede tomar cualquier valor.

    ![](../../../../../assets/drive/t1vw7KGogAD0Tqp1UIoVESm6KBOrDcv9f2BuzzDGdaNP9yXkId4n_YODwWpbnzvGiSKEktpKJqAUtwwlUpKH3DR1Z6t51QShE5mUAWtuaksNDKhgeu-_YxYsnlwXySWaLwsyOfaU.png)

    - **"ShowAuditDefault"** el atributo permite habilitar la funcionalidad de Auditoría. La funcionalidad de Auditoría permite rastrear cada cambio realizado en cualquier tabla o entidad de Etendo.
    - **"ShowAcct"** el atributo permite mostrar los botones de Contabilizar y la solapa Sistema siempre que su valor se establezca en "Y".
    - **"ForcedLinkWindowDBTableName"** donde "DBTableName" es el nombre de la tabla en la base de datos.  
    Este atributo permite una navegación directa a la ventana cuyo UUID se establece como valor del atributo, en lugar de utilizar la lógica de navegación estándar.
    - **"ModalModuleModuleJavaPackage"** donde "ModuleJavaPackage" es el nombre del paquete Java del módulo o _"ModalModuleModuleUUID"_ donde el UUID del módulo es el identificador único del módulo en la base de datos.  
    Este atributo define si los procesos dentro de un módulo invocados desde un menú o un botón o una solapa se abren en popups del navegador (valor del atributo = "N") o en popups modales (valor del atributo ="Y").
    - _Popups del navegador_ implica el despliegue del proceso en una nueva ventana en el navegador.
    - _Popups modales_ implica el despliegue del proceso en otra capa dentro de la ventana de la aplicación.
    - **"ModalProcessProcessUUID"** donde el UUID del proceso es el UUID del proceso.  
    Este atributo define si un proceso determinado se abre en un popup modal (valor del atributo ="Y") o en un popup del navegador (valor del atributo ="N").
    - Este atributo tiene una preferencia superior a ModalModule; por lo tanto, es posible definir que todos los procesos de un módulo se abran en popups modales excepto algunos de ellos.
    - **"SaveAttachmentsOldWay"**  
    Este atributo define si los adjuntos deben guardarse utilizando el modelo antiguo de adjuntos.

### Visibilidad de Preferencias

La sección de visibilidad de preferencias define el *Nivel* donde se va a utilizar una preferencia y, por tanto, se aplicará.

Los niveles de preferencia pueden establecerse en un valor determinado o dejarse vacíos. Si un nivel se deja vacío, la preferencia será válida para cualquier valor de ese nivel.

Por ejemplo, si el nivel de usuario está vacío, cualquier usuario podrá ver esa preferencia. En caso de que la misma preferencia tenga valores en diferentes niveles, se utilizará el más específico.

Los niveles disponibles son:

- **Entidad**: si este nivel se establece vacío o en Sistema, la preferencia será visible desde cualquier entidad utilizada para iniciar sesión.
- **Organización**: si este nivel se establece vacío o en (\*), la preferencia será visible desde cualquier organización utilizada para iniciar sesión.
- **Usuario**: si este nivel se establece en un usuario determinado, solo ese usuario podrá ver esa preferencia una vez iniciada la sesión.
- **Rol**: si este nivel se establece en un rol determinado, solo ese rol podrá ver esa preferencia.
- **Ventana**: si este nivel se establece en una ventana determinada, solo esa ventana podrá ver esa preferencia.

#### Prioridad de Preferencias

La sección Prioridad de Preferencias define la **Prioridad** de múltiples preferencias definidas para la misma Propiedad.

La Prioridad de Preferencias se aplicará al cargar las Preferencias por defecto del Rol con el que se ha iniciado sesión.

- Comprobar prioridad por Entidad **(Visible at client)**:

    - La visibilidad de entidad no definida se gestiona como SISTEMA.
    - Si pref1 o pref2, cualquiera de ellas que no se establezca en ENTIDAD SISTEMA, se tendrá en cuenta.
    - Si pref1 o pref2 tienen valor establecido y ambas no están establecidas en ENTIDAD SISTEMA, entonces se comprobará el siguiente nivel de prioridad.

- Comprobar prioridad por Organización **(Visible at Organization)**:

    - Si pref1 o pref2, cualquiera de ellas que tenga valor establecido, se tendrá en cuenta.
    - Si pref1 o pref2 tienen ambos valores establecidos, entonces se comprobará la profundidad del valor en el árbol de organizaciones y se tendrán en cuenta las Preferencias de la organización de nivel más alto.
    - Si pref1 o pref2 tienen ambos el mismo valor establecido, entonces se comprobará el siguiente nivel de prioridad.

- Comprobar prioridad por Usuario **(Visible at User)**:

    - Si pref1 o pref2, cualquiera de ellas que tenga valor establecido, se tendrá en cuenta.
    - Si pref1 o pref2 tienen ambos valor establecido, entonces se comprobará el siguiente nivel de prioridad.

- Comprobar prioridad por Rol **(Visible at Role)**:

    - Si pref1 o pref2, cualquiera de ellas que tenga valor establecido, se tendrá en cuenta.
    - Si pref1 o pref2 tienen ambos un valor establecido, entonces se comprobará el siguiente nivel de prioridad.

- Comprobar prioridad por Ventana **(Visible at Window)**:

    - Si pref1 o pref2, cualquiera de ellas que tenga valor establecido, se tendrá en cuenta.
    - Si pref1 o pref2 tienen ambos un valor establecido, entonces se comprobará el siguiente nivel de prioridad.

- **MISMA PRIORIDAD**:

  - Si todos los niveles anteriores son iguales, entonces se considerará la preferencia con la columna **Seleccionado** marcada.

#### Valores de Preferencias

Al iniciar sesión en Etendo o al entrar en el rol o la organización, las preferencias visibles para ese usuario, rol, entidad, organización o ventana se almacenan en la sesión de Etendo. Esos valores de sesión pueden obtenerse utilizando el método: `org.openbravo.erpCommon.utility.Utility.getContext`.

Adicionalmente:

- Es posible buscar el valor de una preferencia determinada utilizando el método: `org.openbravo.erpCommon.businessUtility.Preferences.getPreferenceValue`. Este método muestra una excepción en caso de que:

    - Una propiedad de preferencia no tenga un valor definido para el nivel de visibilidad requerido.
    - o exista un conflicto causado por la definición de más de un valor de propiedad para la misma propiedad de preferencia para un nivel de visibilidad determinado. Los conflictos pueden resolverse manualmente comprobando y modificando la preferencia.

---

Este trabajo es una obra derivada de [Configuración General](https://wiki.openbravo.com/wiki/General_Setup){target="_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="_blank"} por [Etendo](https://etendo.software){target="_blank"}.