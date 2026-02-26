---
tags:
    - Etendo BI
    - Configuration
    - PowerBI Reports
    - Inclusion/Exclusion
    - Entity Management
---

# Configuración de inclusión/exclusión de Etendo BI
:octicons-package-16: Javapackage: `com.etendoerp.powerbi.inclusion.exclusion` 

## Visión general

!!! info
    Para poder incluir esta funcionalidad, debe estar instalado el bundle Etendo BI. Para ello, siga las instrucciones de [Marketplace](https://marketplace.etendo.cloud/?#/product-details?module=11372FBD87F34F80AAADBE1C9369CF83){target="_blank"}.

Con el fin de permitir a los usuarios personalizar y configurar la información y los filtros en los informes de PowerBI, se ha desarrollado un nuevo módulo que permite la creación de diferentes configuraciones que facilitan la selección y la exclusión de entidades específicas dentro de los informes.

A continuación, se proporciona una descripción detallada de la ventana de configuración y sus componentes.

## Ventana **Configuración de inclusión/exclusión de Etendo BI**:

La ventana consta de dos solapas principales: "Cabecera" y "Líneas". Estas solapas se utilizan para definir y ajustar los filtros de los informes de PowerBI según los requisitos específicos del usuario.

### _Cabecera_

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/etendobi-extensions/inclusion-exclusion-configuration/header-bi.png)

**Nombre y descripción**: campos de texto que permiten al usuario identificar fácilmente la configuración y comprender su propósito.

**Tipo:** indica el tipo de entidad que se incluirá o excluirá según la configuración. Este campo proporciona información adicional para comprender el contexto de la configuración.  
Las opciones son:

- Grupos de Terceros
- Concepto contable
- Producto
- Categoría del producto
- Tipo de documento
- Cuenta: si es necesario introducir cuentas, al seleccionar este tipo se habilita un selector de Nivel de elemento, Tipo de cuenta y Árbol de cuentas (obligatorio)
- Terceros
- Agente comercial

!!! note
    Si el campo "Tipo" se deja vacío, se asume que la información de la línea viene dada por uno de los datos auxiliares (campos de número, cadena o Sí/No). Además, en la solapa Líneas, es posible combinar todas las opciones mencionadas anteriormente para incluirlas o excluirlas.

**Fecha desde y fecha hasta:** campos de fecha para definir la duración de la configuración creada. Si se especifican en la cabecera, las líneas adquieren ese periodo definido. Si desea que las líneas tengan periodos diferentes, establezca estas fechas en las líneas correspondientes.

**Tiene número, tiene cadena, tiene booleano:** estas casillas de verificación permiten al usuario habilitar campos adicionales de valor numérico, de cadena o de Sí/No en las líneas de configuración. Estos campos auxiliares se utilizan según sea necesario en los informes.

### _Solapa Líneas_

Esta solapa contiene las líneas de configuración asociadas a la cabecera. Cada línea representa un elemento que puede utilizarse para incluir o excluir entidades en los informes. A continuación se describen los campos de las líneas:

**Línea:** número de la línea dentro de la configuración. Este número proporciona una referencia para identificar y ordenar las líneas.

**Tipo de documento:** si la configuración es "Tipo de documento", permite seleccionar un tipo de documento específico. Este campo solo se muestra si el tipo de entidad es "Tipo de documento".

**Terceros:** si la configuración es "Terceros", permite seleccionar un tercero. Este campo solo se muestra si el tipo de entidad es "Terceros".

**Grupos de Terceros:** si la configuración es "Grupos de Terceros", permite seleccionar un grupo de terceros. Este campo solo se muestra si el tipo de entidad es "Grupos de Terceros".

**Agente comercial:** si la configuración es "Agente comercial", permite seleccionar un agente comercial. Este campo solo se muestra si el tipo de entidad es "Agente comercial".

**Cuenta**: si la configuración es "Cuenta", permite seleccionar una cuenta, prefiltrada por los campos relacionados en la cabecera. Este campo solo se muestra si el tipo de entidad es "Cuenta".

**Categoría del producto:** si la configuración es "Categoría del producto", permite seleccionar una categoría del producto. Este campo solo se muestra si el tipo de entidad es "Categoría del producto".

**Producto:** si la configuración es "Producto", permite seleccionar un producto específico. Este campo solo se muestra si el tipo de entidad es "Producto".

**Concepto contable**: si la configuración es "Concepto contable", permite seleccionar un concepto contable. Este campo solo se muestra si el tipo de entidad es "Concepto contable".

**Número:** campo auxiliar para introducir un número adicional. Este campo solo se muestra si la casilla "Tiene número" está marcada.

**Cadena:** cadena de texto auxiliar. Se muestra solo si está marcada la casilla "Tiene cadena" en la cabecera.

**Sí/No:** verificación auxiliar de Sí/No. Se muestra solo si está marcada la casilla "Tiene Sí/No" en la cabecera.

## **Ejemplos**

Configuración de cuentas de Etendo para tomar los saldos y reflejarlos en los informes financieros en BI:

### _Configuración en Etendo_

Categorías principales para la configuración de cuentas:

- Caja
- Bancos
- Clientes
- Proveedores
- Ventas
- Costes de ventas

#### Configuración de cuentas de caja:

![cash.png](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/etendobi-extensions/inclusion-exclusion-configuration/cashpng.png)

#### Configuración de cuentas bancarias:

![bank.png](../../../../../assets/legacy/bank.png)

#### Configuración de cuentas de clientes:

![customers.png](../../../../../assets/legacy/customers.png)

#### Configuración de cuentas de proveedores:

![suppliers.png](../../../../../assets/legacy/suppliers.png)

#### Configuración de cuentas de ventas:

![sales.png](../../../../../assets/legacy/sales.png)

#### Configuración de cuentas de costes de ventas:

![sales_cost.png](../../../../../assets/legacy/sales_cost.png)

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.