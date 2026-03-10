---
title: Configuración General - Primeros pasos
tags: 
 - Primeros pasos
 - Instalaciones
 - Configuración de entidad
 - Configuración de organización
---

![cover-getting-started.png](../../../../assets/getting-started/overview/cover-getting-started.png)
# Configuración General - Primeros pasos

## Visión general

Esta sección describe los pasos que deben realizarse primero para configurar Etendo.
Las instalaciones de Etendo requieren al menos una [Entidad](../../../../user-guide/etendo-classic/basic-features/general-setup/client.md) y una [Organización](../../../../user-guide/etendo-classic/basic-features/general-setup/enterprise-model/organization.md). Entidad y Organización son los dos conceptos clave dentro de la Configuración General.

En otras palabras, no es posible emitir una factura o contabilizar un asiento en el libro mayor en Etendo si no existe una Entidad y una Organización creadas y configuradas correctamente.

Los primeros pasos a seguir para configurar Etendo son:

#### Instalación del Localization Bundle si está disponible para el país

!!!info
    Lea la documentación de [Instalar módulos](../../../../developer-guide/etendo-classic/getting-started/installation/install-modules-in-etendo.md) para instalar el bundle de localización. 

Esto puede considerarse el primer paso básico al configurar instancias de Etendo, ya que es necesario instalar primero el bundle de localización, si existe, para aplicar los datos de referencia contables o el plan de cuentas al crear posteriormente la Entidad o la Organización.

Un Localization Bundle puede incluir al menos:

- la **traducción** completa para el/los idioma(s) oficial(es) del país.
El idioma está disponible automáticamente una vez que el bundle de localización se ha instalado correctamente; por lo tanto, puede seleccionarse tal y como se describe en [perfil](../../../../getting-started/user-interface/workspace.md#profile).

- el **plan de cuentas** que define la estructura contable, si existe, para cumplir con las prácticas y leyes locales aprobadas.
El plan de cuentas está disponible para su selección únicamente al ejecutar Crear entidad o Crear organización.

- y la configuración de los **impuestos** que cumplen con los requisitos de las autoridades fiscales del país.
La configuración de los impuestos también está disponible para su selección al ejecutar [Crear entidad](../../../../developer-guide/etendo-classic/how-to-guides/how-to-run-an-initial-client-setup-process.md) o [Crear organización](../general-setup/enterprise-model/initial-organization-setup.md), e incluso en la ventana de gestión de módulos de empresa.

#### Crear entidad

Una [Entidad](../general-setup/client.md) en Etendo es el nivel más alto de configuración y datos dentro de Etendo.

Lo anterior significa que determinadas configuraciones como Usuario, clientes, proveedores y otros [datos maestros](../master-data-management/master-data.md) pueden gestionarse en una entidad y, por lo tanto, estar disponibles en todas las organizaciones dentro de la entidad.

!!! info
    Cada entidad puede alojar al menos una o incluso más de una organización que puede utilizarse para modelar su empresa.

[Crear entidad](../../../../developer-guide/etendo-classic/how-to-guides/how-to-run-an-initial-client-setup-process.md) es el proceso que crea una Entidad en Etendo. Una Entidad no puede crearse manualmente.

Este proceso, además de crear una Entidad, permite seleccionar los datos de referencia incluidos en el/los bundle/s ya instalados.
Todos esos datos, si se aplican a la Entidad, serán compartidos por todas las organizaciones que pertenecen a la Entidad.

!!! info
    Existe una Entidad de Sistema que Etendo crea automáticamente como parte del proceso de instalación de Etendo.
    Esta entidad gestiona datos de la aplicación como tablas, columnas y campos, y también gestiona algunos datos que pueden compartirse entre todas las Entidades, como monedas, países y regiones y unidades de medida.

#### Crear organización

Una **Organización** es el segundo nivel de configuración y datos.

Las organizaciones pueden estructurarse de forma jerárquica dentro de una Entidad, proporcionando múltiples opciones al modelar su empresa.

Existen diferentes tipos de organizaciones que pueden ser o no entidades legales independientes.
Las entidades legales pueden requerir contabilidad o no, y las no entidades legales pueden permitir datos transaccionales o no.

[Crear organización](../general-setup/enterprise-model/initial-organization-setup.md) es el **proceso** que crea Organizaciones en Etendo.

!!! info
    Una Organización puede crearse una vez que se ha creado la Entidad a la que pertenece.

Una Organización no puede crearse manualmente.

Del mismo modo, este proceso, además de crear una Organización, permite seleccionar los datos de referencia incluidos en el/los bundle/s ya instalados.

En este caso, los datos, si se aplican a la Organización, estarán disponibles únicamente para la Organización que se está creando.

!!! info
    Existe una Organización denominada (\*) que se crea automáticamente al mismo tiempo que se crea la Entidad de Sistema. Cada organización creada posteriormente se ubicará jerárquicamente por debajo de ella.

#### Configuración de Usuario y Rol

La seguridad de Etendo puede dividirse en seguridad funcional y seguridad de datos.
La seguridad **funcional** gestiona los derechos de acceso a entidades de Etendo como ventanas y procesos mediante la correcta configuración de [Usuario](../general-setup/security/user.md) y [Rol](../general-setup/security/role.md):

Un **Usuario** es una entidad que puede iniciar sesión en Etendo siempre que tenga una contraseña y al menos un rol asignado.
Cada persona que acceda a Etendo debe tener un usuario diferente asignado y correctamente configurado.

Un **Rol** es la conexión entre usuarios y derechos de acceso a Organizaciones, ventanas, procesos y formularios en Etendo.
Los derechos de acceso se configuran primero a nivel de rol; posteriormente, los roles se asignan al/los usuario/s.

Etendo crea dos usuarios por defecto: el usuario Sistema y el usuario Admin:

- el usuario **Sistema** es el propietario de los datos de la aplicación de Etendo. No es posible iniciar sesión en Etendo como usuario Sistema.
- el usuario **Admin** es un usuario **super** que tiene acceso a cualquier Entidad de Etendo.

La contraseña asignada a este usuario es Etendo; sin embargo, puede cambiarse si es necesario en la ventana de [Usuario](../general-setup/security/user.md).

Este usuario está asignado al Rol de Administrador del Sistema, un rol sin restricciones de acceso.
La **seguridad de datos** es una configuración avanzada, ya que gestiona los derechos de acceso a subconjuntos de datos dentro de entidades de Etendo como ventanas y procesos, mediante la correcta configuración del [Acceso datos](../general-setup/security/role-access.md) a nivel de tabla y del [Rol](../general-setup/security/role.md):

!!! info
    El Acceso datos define desde qué entidad y/o organización será visible cada registro.

Cada [Tabla](../general-setup/security/role-access.md) en Etendo tiene una columna Acceso datos.

El nivel de acceso de usuario permite limitar los registros que serán accesibles en entidades como ventanas, procesos, formularios, clases de widget y vistas para un [Rol](../general-setup/security/role.md), o incluso limitar el acceso a una entidad determinada.

### Diagrama de configuración básica

El diagrama siguiente muestra el flujo básico de Configuración General de Etendo para una entidad legal con contabilidad. Este flujo es una parte del flujo global de configuración del negocio.

![](../../../../assets/user-guide/etendo-classic/basic-features/general-setup/getting-started/basic-general-setup.png)

En el ejemplo anterior, los datos de **Contabilidad** no pueden compartirse entre todas las organizaciones de la entidad porque no se aplicaron a nivel de entidad, sino a la Organización que se está creando.

Esta configuración encajaría en el caso de una Entidad que tiene **una o más entidades legales independientes con contabilidad por debajo**, igual que la entidad de ejemplo incluida por defecto con Etendo (entidad de ejemplo F&B).

Existe una relación estrecha entre la configuración general, que permite la creación y configuración de una empresa, y el área de configuración contable, ya que para establecer una Organización Legal con Contabilidad como lista, requiere que los siguientes elementos contables se creen y configuren correctamente primero:

1. un [Calendario anual y periodos](../financial-management/accounting/setup/fiscal-calendar.md)

2. y el [Esquema contable](../financial-management/accounting/setup/general-ledger-configuration.md) de una organización, que incluye una dimensión que es el [Árbol de cuentas](../financial-management/accounting/setup/account-tree.md) o plan de cuentas.

!!! info
    El Calendario anual y periodos, una vez creado manualmente, puede estar disponible para todas las organizaciones dentro de la entidad si se crea para la organización (\* (asterisco)).

Un **Esquema contable** por defecto y el **plan de cuentas** pueden crearse automáticamente si se instala y aplica a la Organización un dato de referencia de **Contabilidad**, como un **Localization Bundle** que contenga un módulo de plan de cuentas. Además, en caso de que no exista un Localization Bundle para su país, Etendo proporciona un módulo genérico de plan de cuentas que, si se instala y aplica, crea un plan de cuentas de ejemplo y un Esquema contable por defecto que posteriormente puede personalizarse para satisfacer las necesidades de su organización.

## Diagrama de configuración del negocio

El diagrama siguiente muestra el flujo de configuración del negocio.
Este flujo de configuración del negocio va desde las áreas de configuración genérica y datos maestros hasta las áreas de configuración de contabilidad y almacén.

![](../../../../assets/user-guide/etendo-classic/basic-features/general-setup/getting-started/Quick_Guide_Diagram_new.png)

Si desea conocer más sobre la configuración básica de las configuraciones de negocio en Etendo, revise los diferentes artículos en la sección de Configuración General.

Siguiendo este flujo de configuración, debería poder tener su propia versión de Etendo lista para ejecutar los flujos de negocio básicos.

---

Este trabajo es una obra derivada de [Configuración General](https://wiki.openbravo.com/wiki/General_Setup){target="_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="_blank"} por [Etendo](https://etendo.software){target="_blank"}.