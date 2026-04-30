---
title: Centro de costos
tags:
    - Coste
    - Centro
    - Gestión Financiera
    - Configuración
    - Contabilidad
---

# Centro de costos

:material-menu: `Aplicación` > `Gestión Financiera` > `Contabilidad` > `Configuración` > `Centro de costos`

## Visión general

Un **Centro de costos** es una dimensión contable utilizada para clasificar y hacer seguimiento de gastos o ingresos por unidad organizativa. Al contabilizar documentos en el libro mayor, los centros de costos permiten asignar transacciones a áreas específicas del negocio — como departamentos, equipos o proyectos —, lo que posibilita un análisis y una elaboración de informes financieros más detallados.

La ventana Centro de costos sirve como registro maestro de todos los centros de costos dentro de una organización. Desde aquí, los usuarios pueden crear, ver y gestionar los centros de costos disponibles para su uso durante las transacciones contables.

![Ventana Centro de costos](../../../../../../assets/user-guide/etendo-classic/basic-features/financial-management/accounting/setup/cost-center/cost-center.png)

### Creación de un Centro de costos

Para crear un nuevo centro de costos:

1. Navega a `Gestión Financiera` > `Contabilidad` > `Configuración` > `Centro de costos`.
2. Haz clic en **Nuevo** para abrir un registro en blanco.
3. Introduce los siguientes campos:

    - **Nombre** *(obligatorio)*: Un nombre único y descriptivo para el centro de costos (por ejemplo, *Departamento de TI*, *Equipo de ventas*, *Proyecto Alfa*).
    - **Descripción** *(opcional)*: Una breve explicación de lo que representa el centro de costos.
    - **Organización**: Selecciona la organización a la que pertenece este centro de costos. Si se asigna a la organización `(*)`, el centro de costos estará disponible en **todas las organizaciones** del cliente.
    - **Nivel agrupación**: Marca esta opción para indicar el centro de costos como un nodo de resumen, lo que te permite construir una **estructura en árbol jerárquica** de centros de costos con fines de informes.

4. Guarda el registro.

### Jerarquía de centros de costos

Los centros de costos pueden organizarse en una estructura en árbol de padre-hijo utilizando la opción **Nivel agrupación**. Un centro de costos de resumen actúa como un nodo de agrupación y no registra transacciones directamente; se utiliza para agregar los resultados de sus centros de costos hijos en los informes.

Esto es útil cuando quieres, por ejemplo, agrupar centros de costos de equipos individuales bajo un centro de costos departamental más amplio.

## Configuración relacionada

- [Esquema contable](../general-ledger-configuration/) – Configura cómo se utilizan en tu libro mayor las dimensiones contables como los centros de costos.
- [Combinación de cuentas](../account-combination/) – Define cómo se combinan los centros de costos con cuentas y otras dimensiones.
- [Actividad (ABC)](../abc-activity/) – Otra dimensión contable que puede utilizarse junto con los centros de costos.

---

Este trabajo es una obra derivada de [Centro de costos](https://wiki.openbravo.com/wiki/Cost_Center){target="\_blank"} de [Wiki de Openbravo](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizado bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.