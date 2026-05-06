---
title: Plantillas de Contabilidad
tags:
    - Contabilidad
    - Plantillas
    - Gestión Financiera
    - Configuración
---

# Plantillas de Contabilidad 



## Visión general

Las Plantillas de Contabilidad permiten a las organizaciones personalizar cómo Etendo genera los asientos de diario para tipos de documento específicos, sin modificar la aplicación core. Esto suele ser necesario cuando las normas legales o de negocio locales exigen una lógica de contabilización distinta del comportamiento predeterminado; por ejemplo, un tratamiento fiscal específico por país para facturas o un método de devengo personalizado para entradas de mercancías.

Un administrador del sistema registra la plantilla en esta ventana. Un desarrollador Java implementa y despliega previamente la clase correspondiente como parte de un módulo. Una vez configurada, la plantilla se aplica automáticamente cada vez que se contabiliza un documento coincidente; los usuarios finales no se ven afectados por el cambio.

!!! warning
    Esta es una funcionalidad potente que debe utilizarse con precaución. La clase de contabilización personalizada debe probarse en profundidad antes de desplegarla en un entorno de producción.

## Creación de la configuración de la Plantilla de Contabilidad
:material-menu: `Aplicación` > `Gestión Financiera` > `Contabilidad` > `Configuración` > `Plantillas de Contabilidad`

!!! warning
    Aunque esta es una ventana de configuración funcional gestionada a nivel de administrador, las Plantillas de Contabilidad deben ser desarrolladas por un desarrollador Java. La clase Java referenciada en el campo **Nombre de la clase Java** debe estar implementada y desplegada como parte de un módulo antes de poder registrarse aquí.

La ventana **Plantillas de Contabilidad** se utiliza para registrar la clase Java que implementa la lógica de contabilización personalizada. Cada plantilla requiere un nombre, el nombre completo de la clase Java (dentro del paquete Java del módulo) y la tabla de base de datos que corresponde al tipo de documento a personalizar; por ejemplo, `C_Invoice` para facturas o `M_InOut` para albaranes de entrada y salida de mercancías.

![Ventana de Plantillas de Contabilidad mostrando un registro de plantilla configurado](../../../../../../assets/drive/1QFEgaMk9QRkcpsjLLGOZJNKRJo75LvKr.png)

Cada plantilla se asocia posteriormente con tablas activas o tipos de documento específicos. Puede definir una única plantilla que cubra todos los documentos de un tipo dado (por ejemplo, todas las facturas), o crear plantillas separadas que se dirijan solo a [categorías de documento](document-type.md) específicas (por ejemplo, solo facturas de compra), manteniendo el comportamiento predeterminado para el resto.

### Campos

- **Nombre**: Un identificador descriptivo para la plantilla de contabilidad. Use un nombre claro que refleje la regla de contabilización o el tipo de documento al que afecta.
- **Nombre de la clase Java**: El identificador técnico de la lógica de contabilización personalizada. El desarrollador proporciona este valor; introdúzcalo exactamente como se indica.
- **Tabla**: El tipo de documento que esta plantilla sobrescribe. Seleccione la tabla correspondiente a las transacciones que desea personalizar. En la lista desplegable, busque nombres como `C_Invoice` (facturas) o `M_InOut` (albaranes de mercancías); estos son los nombres internos de tabla que Etendo usa para identificar cada tipo de documento.
- **Descripción**: Información adicional opcional sobre el propósito o comportamiento de esta plantilla (no se muestra en la vista de cuadrícula anterior).
- **Activo**: Indica si esta plantilla está actualmente en uso. Desactivar una plantilla restaura el comportamiento de contabilización predeterminado para el tipo de documento asociado.

Una vez configurada la plantilla, se asocia con las tablas activas o documentos correspondientes. Los asientos que genera aparecerán en los informes de [Esquema contable](general-ledger-configuration.md) junto con los asientos estándar, siguiendo las reglas definidas en el [Árbol de cuentas](account-tree.md).

## Definición del conjunto de datos

!!!warning
    Esta sección está pensada para equipos de desarrollo que necesitan empaquetar y distribuir una plantilla de contabilidad personalizada como un módulo instalable. Si es un administrador que registra una plantilla existente en la ventana Plantillas de Contabilidad, omita esta sección y la sección Prueba del conjunto de datos por completo; no se aplican a su flujo de trabajo.

La definición del conjunto de datos determina qué registros se exportan con el módulo de plantilla de contabilidad para que la plantilla pueda instalarse en otros entornos. Una definición correcta del conjunto de datos es esencial: una incorrecta puede dejar la plantilla completamente inutilizable tras la instalación. Para obtener información de fondo sobre cómo interactúan las organizaciones y los conjuntos de datos durante la configuración, consulte [Crear organización](../../../general-setup/enterprise-model/initial-organization-setup.md).

Siga estas directrices al definir el conjunto de datos:

- El conjunto de datos **debe pertenecer al módulo de la plantilla de contabilidad**.
- **Evite caracteres especiales** en el nombre del conjunto de datos. Esta cadena se utiliza para generar el nombre del archivo XML que almacena el conjunto de datos.
- **Nivel de acceso a datos** debe establecerse en `Sistema/Cliente`, lo que significa que los usuarios pueden aplicar la configuración solo a nivel de Cliente (Organización `*`). Nota: la captura de pantalla siguiente puede mostrar un valor diferente según la versión de Etendo.
- El indicador **Permitir exportar** debe estar marcado.
- Dentro de la pestaña **Tabla**, incluya la tabla `AD_CreateFact_template` (la tabla de base de datos que almacena los registros de Plantillas de Contabilidad; cada fila de la ventana Plantillas de Contabilidad corresponde a una fila de esta tabla).
- La **Cláusula Where HQL/SQL** filtra qué filas de la tabla se incluyen en el conjunto de datos exportado (HQL y SQL son lenguajes de consulta utilizados para seleccionar registros específicos de la base de datos). Normalmente, esta cláusula selecciona todos los registros cuyo nombre de clase Java se encuentra dentro del paquete Java del módulo, de modo que solo se exporten las plantillas pertenecientes a este módulo.

![Ventana de definición del conjunto de datos](../../../../../../assets/drive/1stuKmJOwNnsth6RG3HX9tj5_6v3OY83U.png)

Una vez completada la definición del conjunto de datos, expórtelo pulsando el botón **Exportar Datos de Referencia**. Este proceso consulta las tablas configuradas, recupera todos los registros que coinciden con la Cláusula Where HQL/SQL y genera un archivo XML en el directorio `referencedata/standard` del módulo.

!!!info
    Como comprobación rápida, abra el archivo XML generado con un editor de texto y verifique que contiene datos. Si el archivo está vacío, revise la definición del conjunto de datos, especialmente la Cláusula Where HQL/SQL de cada tabla.

## Prueba del conjunto de datos

La forma recomendada de verificar que el conjunto de datos es correcto es crear un nuevo cliente dentro de la instancia de desarrollo mediante el proceso [Crear entidad](../../../general-setup/getting-started.md#initial-client-setup), seleccionando durante la configuración el nuevo conjunto de datos de plantilla de contabilidad.

![Selección de datos de referencia de Configuración Inicial del Cliente](../../../../../../assets/drive/14yYG4b3onJefyFiz6sV8KlImkfi5ijCf.png)

!!!info
    Si los datos dentro del conjunto de datos son consistentes, el proceso de Crear entidad debería completarse correctamente. De lo contrario, fallará con una descripción del error que indique qué ha ocurrido.

Tras una configuración correcta, inicie sesión en el nuevo cliente, vaya a la ventana **Plantillas de Contabilidad** y confirme que el registro de la plantilla está presente. A continuación, puede proceder a probar la contabilización creando documentos de ejemplo y verificando que se generan correctamente los asientos contables personalizados. Esta validación se aplica a cualquier entorno en el que se haya instalado la plantilla, no solo durante el desarrollo del módulo.

## Referencia técnica

!!!info
    Esta sección describe el diseño interno de las Plantillas de Contabilidad. Está pensada para desarrolladores y no es necesaria para la configuración diaria.

### Background

De forma predeterminada, Etendo genera asientos de diario para los documentos utilizando la lógica de contabilización integrada. Las Plantillas de Contabilidad introducen un mecanismo que permite a los **módulos sobrescribir este comportamiento predeterminado** sin modificar el código de la aplicación core. Esto significa que las organizaciones pueden adaptar cómo se generan los asientos contables para cumplir requisitos legales o de negocio específicos mediante módulos independientes e instalables.

### How It Works

Las Plantillas de Contabilidad funcionan insertando una **nueva capa entre el documento y la lógica de contabilización**. En la ventana Plantillas de Contabilidad, cada tipo de documento se asigna a la clase que implementa su comportamiento de contabilización. Para cambiar cómo se contabiliza un documento:

1. Un desarrollador crea una nueva clase que implementa la lógica de contabilización deseada.
2. La plantilla se configura en esta ventana para asignar el tipo de documento correspondiente a la nueva clase.
3. A partir de ese momento, todos los documentos de ese tipo utilizan la lógica personalizada.

Este enfoque es transparente para los usuarios finales: el proceso de contabilización se ve y funciona igual desde la interfaz de la aplicación. La única diferencia está en los asientos contables generados, que siguen las reglas definidas por la plantilla personalizada en lugar de los valores predeterminados integrados.

!!!info
    La interfaz de la aplicación no se ve afectada por estos cambios. Todas las modificaciones en el comportamiento de contabilización ocurren entre bastidores. La ventana Plantillas de Contabilidad es la única configuración adicional necesaria y se configura automáticamente cuando se instala el módulo de la plantilla.

---

Este trabajo es una obra derivada de [Plantillas de Contabilidad](https://wiki.openbravo.com/wiki/Projects:Accounting_Templates){target="\_blank"} de [Wiki de Openbravo](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.