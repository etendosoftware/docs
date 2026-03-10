---
tags:
    - How to
    - Esquema contable
    - Crear entidad
    - Crear organización
    - Administrador del sistema
---

#  Cómo ejecutar un proceso de Crear entidad

## Visión general

<iframe width="560" height="315" src="https://www.youtube.com/embed/yGzPXU3nxpk?si=akTrp1_j8RAafSWx" title="reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

El proceso de **Crear entidad** es un proceso crucial en Etendo que permite definir información sobre la **Entidad** y el **esquema contable** que utilizará la organización. La información configurada a través de esta ventana sienta las bases de la estructura organizativa y del **plan de cuentas** que se utilizará con cada organización de la Entidad. 

!!!info
    Puede ejecutarse iniciando sesión en Etendo con el rol de *Administrador del sistema*.

Este proceso permite:

- Introducir el nombre de la Entidad, el nombre de usuario de la Entidad y una contraseña.
- Introducir la moneda base de la Entidad, que será la moneda de la Entidad independientemente de que una Organización que pertenezca a ella pueda tener una moneda diferente.
- Incluir contabilidad para la Entidad.

## Incluir esquema contable

Decida el *esquema contable* que utilizará la organización y configure la contabilidad usando la ventana **Crear entidad**.

### Incluir contabilidad

Para incluir estos datos, existe una casilla de verificación denominada *Incluir contabilidad* que obliga al usuario a introducir un plan de cuentas específico. Para ello, hay dos opciones:

1. Subir un archivo `CSV` con el plan de cuentas, tal y como se explica en la sección [Archivo contable](#archivo-contable) a continuación.
2. Si tiene instalado un bundle de localización, seleccionar uno de los planes de cuentas listados en la sección de Datos de referencia, ya que estos conjuntos de datos ya están instalados.

!!!info
    Se recomienda tener marcada la opción Incluir contabilidad si el usuario necesita aplicar el mismo plan de cuentas a todas sus organizaciones.
    En caso de introducir un plan de cuentas diferente para cada organización específica, debe ejecutar este proceso sin marcar la casilla y, a continuación, configurar el Plan de cuentas en la ventana [Crear organización](../../../user-guide/etendo-classic/basic-features/general-setup/enterprise-model/initial-organization-setup.md).

!!!note
    En la sección Datos de referencia, los conjuntos de datos existentes dependerán de la localización instalada, si la hubiera. 

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_run_an_initial_client_setup_process-1.png)

Si se selecciona la casilla *Incluir contabilidad* y se selecciona un archivo contable o datos de referencia, Etendo crea:

  - un [Calendario anual y periodos](../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup/fiscal-calendar.md) que puede ser compartido por todos los tipos de organización *Legal con contabilidad* que pertenecen a esa Entidad y 
  - un [Árbol de cuentas](../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup/account-tree.md) o *Plan de cuentas* y un [Esquema contable](../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup/general-ledger-configuration.md) que se comparte entre todas las organizaciones creadas dentro de la Entidad.

El **Esquema contable** y el *Plan de cuentas* creados por defecto pueden personalizarse posteriormente. 

!!!info
    Para más información, consulte [Configuración General](../../../user-guide/etendo-classic/basic-features/general-setup/getting-started.md). 


El **Esquema contable** está vinculado al **Árbol de cuentas**, ya que la **Cuenta** es una [Dimensiones](../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup/general-ledger-configuration.md#dimension-tab) obligatoria del esquema contable.

### Archivo contable 

Etendo también permite seleccionar el archivo contable `CSV` con el plan de cuentas correspondiente ([Árbol de cuentas](../../../user-guide/etendo-classic//basic-features/financial-management/accounting/setup/account-tree.mdaccount-tree)) para cargarlo en el sistema desde el campo *Archivo contable*. 

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_run_an_initial_client_setup_process-2.png)

!!!info
    Para más información, consulte [Cómo crear archivos de cuentas](how-to-create-accounts-files.md) 

## Configuración de módulos

Etendo distribuye archivos contables `CSV` como módulos que pueden aplicarse como datos de referencia. Este tipo de módulos forman parte de la localización de Etendo para un país determinado.

!!!info
    La lista de bundles de localización disponibles se encuentra en el [marketplace de Etendo](https://marketplace.etendo.cloud/#/){target="\_blank"}.

Existen algunos módulos adicionales que pueden ser importantes para la configuración inicial de la Entidad.

Los módulos clave incluyen:

- Tipos de documento estándar para pedidos, facturas, etc.; este se selecciona por defecto, ya que es necesario para crear datos transaccionales como pedidos y facturas.

- Datos de referencia como datos maestros o datos de configuración (p. ej., configuración de impuestos) creados para módulos de extensión de Etendo.

Estos módulos son útiles, ya que las configuraciones de impuestos generalmente se aplican a todas las organizaciones de un país, y establecer tipos de documento estándar ayuda a evitar problemas de numeración inconsistente entre diferentes organizaciones.

!!!note
    Se recomienda instalar los módulos necesarios para el correcto funcionamiento de la Entidad, en función de sus requisitos específicos.


!!!info
    Instalación de conjuntos de datos: se pueden añadir módulos adicionales desde la ventana [Gestión del módulo de Empresa](../../../user-guide/etendo-classic/basic-features/general-setup/enterprise-model/enterprise-module-management.md) dentro del sistema.


Cada nueva [Entidad](../../../user-guide/etendo-classic/basic-features/general-setup/client.md) creada en Etendo mantiene de forma centralizada al menos las dimensiones contables obligatorias que se enumeran a continuación:

- Organización
- Tercero
- y Producto

a menos que la casilla *Centralizado* no esté seleccionada para la Entidad, lo que implicaría la configuración y gestión de todas las dimensiones contables (obligatorias y no obligatorias) a nivel de organización.

Para concluir, es importante realizar cuidadosamente la configuración inicial en Etendo, teniendo en cuenta las necesidades y requisitos específicos de la organización. Además, una documentación exhaustiva de la estructura contable y de las configuraciones de módulos es esencial para futuras consultas y para una gestión eficiente del sistema.

!!!info
    Visite [Configuración General](../../../user-guide/etendo-classic/basic-features/general-setup/getting-started.md) para continuar con la configuración inicial de Etendo.

---

Este trabajo es una obra derivada de [Configuración inicial de la Entidad](https://wiki.openbravo.com/wiki/Initial_Client_Setup){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.