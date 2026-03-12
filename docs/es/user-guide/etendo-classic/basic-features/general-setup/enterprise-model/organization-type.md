---
title: Tipo de Organización
tags:
    - Organización
    - Tipo
    - Entidad Legal
    - Unidad de Negocio
---

# Tipo de Organización

:material-menu: `Aplicación` > `Configuración General` > `Organización` > `Tipo de Organización`

## Visión general

Una **organización** puede ser una Entidad Legal, una Unidad de Negocio o ninguna de las dos. En esta ventana, también puede seleccionar si las transacciones están permitidas o no para este tipo de organización.

## Ventana Tipo de Organización

![alt text](../../../../../assets/user-guide/etendo-classic/basic-features/general-setup/enterprise-model/organization-type.png)

Los tipos de Organización predeterminados de Etendo son:

- **Organización** - una organización que no es una entidad legal y no permite la introducción de datos transaccionales.

    - Este tipo de organización permite la creación y configuración de datos maestros para ser compartidos entre un grupo de organizaciones de cualquier tipo que pertenezcan a ella, por ejemplo, Terceros, Plan de Cuentas, etc.
    - No requiere un libro mayor, ya que no permite introducir transacciones, pero puede tener una configuración de Libro Mayor determinada para ser compartida entre las organizaciones dependientes.
    - Los periodos contables no pueden abrirse y cerrarse de forma independiente en su nivel.
    - Y puede haber tantos tipos de organización **Organización** en una rama como sea necesario.

- **Entidad legal con contabilidad** - una entidad legal independiente con un número de identificación fiscal único que requiere contabilidad, por lo tanto:

    - esta organización requiere Libro Mayor y, por tanto, un Árbol de Cuentas o Plan de Cuentas, así como un Calendario Fiscal, ya que los periodos contables pueden y deben abrirse y cerrarse en su nivel.
    - Este tipo de organización permite la consolidación del Balance de Situación y de los informes de Pérdidas y Ganancias solo para el Plan de Cuentas que tenga asignado.
    - Las transacciones están permitidas para este tipo de organización.
    - Y, por último, solo puede haber una entidad legal por rama del árbol; por lo tanto, las organizaciones dependientes heredan la configuración del Libro Mayor y el Calendario Fiscal de la organización de entidad legal con contabilidad.

- **Entidad legal sin contabilidad**\- una entidad legal independiente con un número de identificación fiscal único que no requiere contabilidad porque se gestiona en un sistema separado, por lo tanto:

    - este tipo de organización no necesita un libro mayor ni un plan de cuentas y no admitirá informes financieros en su nivel.
    - Las transacciones están permitidas para este tipo de organización. Transacciones que no se contabilizarán en el libro mayor.
    - No puede tener otra entidad legal en un nivel superior/inferior de la estructura del árbol empresarial.

- **Genérica** - una organización que no es una entidad legal, pero debe pertenecer a una entidad legal situada en un nivel superior en la estructura del árbol de organización. Por ejemplo, departamentos o divisiones dentro de una organización o entidad legal.

    - Puede haber tantas organizaciones genéricas como sea necesario por rama del árbol, pero siempre bajo una entidad legal.
    - Este tipo de organización permite la introducción de datos transaccionales, puede tener su propia configuración de libro mayor y puede heredar la configuración del libro mayor de la entidad legal con contabilidad a la que pertenece.
    - Los periodos contables no pueden abrirse y cerrarse de forma independiente en su nivel.

Adicionalmente, un tipo de organización puede configurarse como:  

- **Entidad Legal**  
- **Unidad de Negocio**
- **Entidad Legal con contabilidad**  
- **Transacciones Permitidas**

!!! info
    Tenga en cuenta que ninguno de los tipos de Organización de Etendo está configurado como Unidad de Negocio.

---

Este trabajo es una obra derivada de [Configuración General](https://wiki.openbravo.com/wiki/General_Setup){target="_blank"} de [Wiki de Openbravo](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="_blank"} por [Etendo](https://etendo.software){target="_blank"}.