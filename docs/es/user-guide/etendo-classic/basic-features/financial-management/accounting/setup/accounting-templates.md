---
title: Plantillas de Contabilidad
tags:
    - Contabilidad
    - Plantillas
    - Gestión Financiera
    - Configuración
---

# Plantillas de Contabilidad

:material-menu: `Aplicación` > `Gestión Financiera` > `Contabilidad` > `Configuración` > `Plantillas de Contabilidad`

## Visión general

Las Plantillas de Contabilidad permiten a las organizaciones **reemplazar los asientos contables predeterminados de Etendo con reglas de contabilización personalizadas** para tipos de documento específicos. Cuando se contabiliza un documento, el motor contable comprueba si existe una plantilla definida para ese tipo de documento y, si es así, ejecuta la lógica personalizada en lugar del comportamiento de contabilización estándar.

Esto suele ser necesario cuando:

- **Country-specific legal requirements** exigen un tratamiento contable diferente para ciertas transacciones (por ejemplo, facturas, albaranes de entrada/salida de mercancías o pagos).
- Deben aplicarse **Special posting rules** a un subconjunto de documentos, como generar líneas de libro mayor adicionales o distribuir importes de forma diferente.

!!!info
    Configurar una Plantilla de Contabilidad es una tarea colaborativa. Un **developer** escribe la lógica de contabilización personalizada (una clase Java) y un **finance administrator** configura la plantilla en esta ventana para activarla. Si su organización necesita una plantilla personalizada, coordínese con su equipo de desarrollo antes de realizar cambios.

Puede definir una única plantilla que cubra todos los documentos de un tipo dado (por ejemplo, todas las facturas), o crear plantillas separadas que se dirijan solo a categorías de documento específicas [document categories](document-type.md) (por ejemplo, solo facturas de compra), dejando el comportamiento predeterminado para el resto.

## Cabecera

![Vista de cuadrícula de Plantillas de Contabilidad](../../../../../../assets/drive/1QFEgaMk9QRkcpsjLLGOZJNKRJo75LvKr.png)

Campos a tener en cuenta:

- **Nombre**: Un identificador descriptivo para la plantilla de contabilidad. Use un nombre claro que refleje la regla de contabilización o el tipo de documento al que afecta.
- **Nombre de la clase Java**: El identificador técnico de la lógica de contabilización personalizada. Su desarrollador le proporcionará este valor; péguelo exactamente tal como se indique.
- **Tabla**: El tipo de documento que esta plantilla sobrescribe. Seleccione la tabla correspondiente a las transacciones que desea personalizar. En el desplegable, busque nombres como `C_Invoice` (facturas) o `M_InOut` (albaranes de mercancías); estos son nombres internos de tabla que Etendo usa para identificar cada tipo de documento.
- **Descripción**: Información adicional opcional sobre el propósito o comportamiento de esta plantilla (no se muestra en la vista de cuadrícula anterior).
- **Activo**: Un indicador que señala si esta plantilla está actualmente en uso. Desactivar una plantilla restaura el comportamiento de contabilización predeterminado para el tipo de documento asociado.

!!!warning
    Las Plantillas de Contabilidad sobrescriben la lógica de contabilización estándar para el tipo de documento seleccionado. Antes de activar una plantilla en un entorno de producción:

    - **Test thoroughly** en una instancia de desarrollo o preproducción contabilizando documentos de ejemplo y revisando los asientos contables generados.
    - **Involve your development team** para confirmar que la lógica personalizada gestiona todos los escenarios esperados.
    - **Have an auditor or accounting manager review** los asientos resultantes para asegurarse de que cumplen los requisitos legales y organizativos.

Una vez configurada la plantilla, queda asociada a las tablas activas o documentos correspondientes. Los asientos que genere aparecerán en los informes de [General Ledger Configuration](general-ledger-configuration.md) junto con las contabilizaciones estándar, siguiendo las reglas definidas en [Account Tree](account-tree.md).

## Definición del conjunto de datos

!!!info
    Esta sección está destinada a equipos de desarrollo que necesitan empaquetar una plantilla de contabilidad personalizada como un módulo distribuible. Si solo está configurando una plantilla existente, puede omitir esta sección.

La definición del conjunto de datos determina qué registros se exportan con el módulo de la plantilla de contabilidad para que la plantilla pueda instalarse en otros entornos. Una definición correcta del conjunto de datos es esencial: una incorrecta puede dejar toda la plantilla inutilizable después de la instalación. Para obtener información general sobre cómo interactúan las organizaciones y los conjuntos de datos durante la configuración, consulte [Initial Organization Setup](../../../general-setup/enterprise-model/initial-organization-setup.md).

Siga estas directrices al definir el conjunto de datos:

- El conjunto de datos **debe pertenecer al módulo de la plantilla de contabilidad**.
- **Evite caracteres especiales** en el nombre del conjunto de datos. Esta cadena se utiliza para generar el nombre del archivo XML que almacena el conjunto de datos.
- **Nivel de Acceso a Datos** debe establecerse en `Sistema/Cliente`, lo que significa que los usuarios pueden aplicar la configuración solo a nivel de Cliente (Organización `*`). Nota: la captura de pantalla siguiente puede mostrar un valor diferente según la versión de Etendo.
- El indicador **Permitir exportar** debe estar marcado.
- Dentro de la pestaña **Tabla**, incluya la tabla `AD_CreateFact_template`, que almacena la configuración de la Plantilla de Contabilidad.
- La **Cláusula Where HQL/SQL** es fundamental para filtrar qué registros se incluyen en el conjunto de datos. Normalmente, la cláusula filtra todos los registros cuyo nombre de clase Java se encuentra dentro del paquete Java del módulo.

![Ventana de definición del conjunto de datos](../../../../../../assets/drive/1stuKmJOwNnsth6RG3HX9tj5_6v3OY83U.png)

Una vez completada la definición del conjunto de datos, expórtelo pulsando el botón **Exportar Datos de Referencia**. Este proceso consulta las tablas configuradas, recupera todos los registros que coinciden con la Cláusula Where HQL/SQL y genera un archivo XML en el directorio `referencedata/standard` del módulo.

!!!info
    Como comprobación rápida, abra el archivo XML generado con un editor de texto y verifique que contiene datos. Si el archivo está vacío, revise la definición del conjunto de datos, especialmente la Cláusula Where HQL/SQL de cada tabla.

## Prueba del conjunto de datos

La forma recomendada de verificar que el conjunto de datos es correcto es crear un nuevo cliente dentro de la instancia de desarrollo usando el proceso [Crear entidad](../../../general-setup/getting-started.md#initial-client-setup), seleccionando durante la configuración el nuevo conjunto de datos de plantilla de contabilidad.

![Selección de datos de referencia de Crear entidad](../../../../../../assets/drive/14yYG4b3onJefyFiz6sV8KlImkfi5ijCf.png)

!!!info
    Si los datos dentro del conjunto de datos son consistentes, el proceso de Crear entidad debería completarse correctamente. En caso contrario, fallará mostrando una descripción del error que indique qué ha ocurrido.

Tras una configuración correcta de Crear entidad, inicie sesión en el nuevo cliente, vaya a la ventana **Plantillas de Contabilidad** y confirme que el registro de la plantilla está presente. A continuación, puede proceder a probar la contabilización creando documentos de ejemplo y verificando que se generan correctamente los asientos contables personalizados.

## Cómo funcionan las Plantillas de Contabilidad

Esta sección explica el diseño técnico que hay detrás de las Plantillas de Contabilidad. Se proporciona como referencia y no es necesaria para la configuración diaria.

### Visión general

De forma predeterminada, Etendo genera asientos contables para los documentos mediante una lógica de contabilización integrada. Las Plantillas de Contabilidad introducen un mecanismo que permite a los **módulos sobrescribir este comportamiento predeterminado** sin modificar el código de la aplicación core. Esto significa que las organizaciones pueden adaptar cómo se generan los asientos contables para cumplir requisitos legales o de negocio específicos mediante módulos independientes e instalables.

### Alcance

El objetivo de las Plantillas de Contabilidad es permitir que los módulos **modifiquen cómo se generan los asientos contables** cuando se contabilizan documentos. En lugar de requerir cambios en el código core, un módulo puede proporcionar su propia lógica de contabilización, que el motor contable utilizará en lugar de la predeterminada.

### Consideraciones de diseño

Las Plantillas de Contabilidad funcionan insertando una **nueva capa entre el documento y la lógica de contabilización**. En la ventana Plantillas de Contabilidad, cada tipo de documento se asigna a la clase que implementa su comportamiento de contabilización. Para cambiar cómo se contabiliza un documento:

1. Un desarrollador crea una nueva clase que implementa la lógica de contabilización deseada.
2. La plantilla se configura en esta ventana para asignar el tipo de documento correspondiente a la nueva clase.
3. A partir de ese momento, todos los documentos de ese tipo usan la lógica personalizada.

Este enfoque es transparente para los usuarios finales: el proceso de contabilización se ve y funciona igual desde la interfaz de la aplicación. La única diferencia está en los asientos contables generados, que siguen las reglas definidas por la plantilla personalizada en lugar de los valores predeterminados integrados.

!!!info
    La interfaz de la aplicación no se ve afectada por estos cambios. Todas las modificaciones en el comportamiento de contabilización ocurren en segundo plano. La ventana Plantillas de Contabilidad es la única configuración adicional necesaria y se establece automáticamente cuando se instala el módulo de la plantilla.

---

Este trabajo es una obra derivada de [Plantillas de Contabilidad](https://wiki.openbravo.com/wiki/Projects:Accounting_Templates){target="\_blank"} de [Wiki de Openbravo](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.