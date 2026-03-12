---
tags: 
    - Transacción bancaria
    - Salt Edge
    - Integración bancaria
    - Extractos bancarios
    - Pagos bancarios
    - Open Banking
    - PSD2
    - PIS
---

# Integración bancaria con Salt Edge

:octicons-package-16: Javapackage: `com.etendoerp.psd2.bank.integration`

## Visión general

Este módulo proporciona funcionalidad de **integración bancaria automática** para Etendo ERP mediante dos capacidades principales:

- **AIS (Account Information Service)**: Conecta de forma segura tus cuentas bancarias y descarga automáticamente las transacciones bancarias.
- **PIS (Payment Initiation Service)**: Inicia pagos bancarios directamente desde Etendo, con la autorización gestionada de forma segura a través de tu banco.

La integración funciona con **Salt Edge**, una plataforma líder de Open Banking que proporciona acceso seguro a miles de bancos en todo el mundo.

### ¿Qué es Salt Edge?

[Salt Edge](https://www.saltedge.com/){target="_blank"} es una plataforma de Open Banking que actúa como intermediario seguro entre Etendo ERP y las entidades bancarias. Salt Edge:

- **Es compatible con miles de bancos** en múltiples países
- **Gestiona toda la autenticación** y los requisitos de seguridad con cada banco
- **Cumple con PSD2** y la normativa de Open Banking
- **Proporciona una interfaz unificada** independientemente del banco utilizado

### ¿Cómo funciona?

La integración utiliza un **middleware centralizado** desarrollado por Etendo que actúa como capa intermedia entre Etendo ERP y Salt Edge. Esta arquitectura proporciona:

- **Integración simplificada**: Etendo ERP no necesita gestionar la complejidad técnica de Open Banking
- **Seguridad mejorada**: el middleware gestiona toda la autenticación y el cifrado
- **Escalabilidad**: múltiples instancias de Etendo pueden usar el mismo middleware
- **Mantenibilidad**: las actualizaciones de las APIs bancarias se gestionan a nivel de middleware

### Beneficios clave

**Información de cuenta (AIS):**

- **Importación automatizada de transacciones**: no es necesario subir manualmente ficheros de extractos bancarios
- **Sincronización en tiempo real**: obtén las últimas transacciones directamente desde tu banco
- **Soporte para múltiples bancos**: conecta cuentas de distintos bancos simultáneamente
- **Prevención de duplicados**: filtra automáticamente transacciones duplicadas

**Iniciación de pagos (PIS):**

- **Pagos bancarios directos**: inicia pagos desde Etendo sin salir del ERP
- **Soporte multi-plantilla**: plantillas de pago SEPA (EUR), FPS (GBP) y DOMESTIC
- **Seguimiento de estado en tiempo real**: monitoriza el progreso del pago desde el inicio hasta la ejecución
- **Actualizaciones automáticas de estado**: recibe actualizaciones del estado del pago automáticamente mediante webhooks

**General:**

- **Autenticación segura**: las credenciales bancarias nunca se almacenan en Etendo
- **Histórico de auditoría**: registro completo de todas las operaciones de sincronización y pagos
- **Gestión de conexiones**: monitoriza, sincroniza, reconecta y desconecta conexiones bancarias desde Etendo

!!!info
    Para poder incluir esta funcionalidad, debe estar instalado el **Financial Extensions Bundle**. Para ello, sigue las instrucciones del marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para más información sobre las versiones disponibles, compatibilidad con core y nuevas funcionalidades, visita [Financial Extensions - Release notes](https://docs.etendo.software/whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes/).

## Requisitos previos

Antes de usar la funcionalidad de Integración bancaria, asegúrate de que:

1. **Configuración de propiedades de Gradle**: la integración requiere una configuración correcta del contexto en tu fichero `gradle.properties`. Debes configurar las siguientes propiedades:

    ```properties
    context.name=etendo
    context.url=https://my-domain/
    ```

    - **context.name**: el nombre de tu contexto de Etendo (normalmente "etendo")
    - **context.url**: la URL completa donde tu instancia de Etendo es accesible, incluyendo el protocolo y la barra final

    Tras configurar estas propiedades, debes ejecutar el comando de setup:

    ```bash
    ./gradlew setup
    ```

    !!!warning "Importante"
        Sin una configuración correcta de `context.name` y `context.url`, la integración no funcionará correctamente. La URL del contexto la utiliza Salt Edge para redirigir a los usuarios de vuelta a Etendo tras la autenticación bancaria y para recibir notificaciones webhook de actualizaciones del estado de los pagos.

2. **Clave API de Salt Edge**: tu organización debe disponer de una clave API de Salt Edge. Esta clave la proporciona **Futit Services** y es necesaria para acceder al middleware de integración.

3. **Configuración de usuario**: la clave API debe configurarse en tu perfil de usuario de Etendo (detallado en la sección de configuración más abajo).

4. **Cuentas financieras**: debes tener creadas Cuentas financieras en Etendo que se vincularán a tus cuentas bancarias.

5. **Visibilidad de botones**: los botones y campos de integración (como **Connect Bank Account**, **Get Bank Statement**, **Generate Bank Payment**, etc.) solo son visibles en la interfaz cuando el usuario conectado tiene configurada una **PSD2 API Key**. Sin la clave API, estos elementos no aparecerán.

!!!warning
    La clave API de Salt Edge la proporciona Futit Services como parte del servicio de integración. Contacta con tu administrador de Etendo o con el soporte de Futit Services para obtener tu clave API.

## Configuración

### Paso 1: Configurar la clave API de Salt Edge

:material-menu: `Aplicación` > `Configuración General` > `Seguridad` > `Usuario`

Como **Administrador** o usuario con permisos adecuados:

1. Navega a la ventana **Usuario**.
2. Selecciona el registro de usuario que realizará las operaciones bancarias.
3. Localiza el campo **PSD2 API Key** e introduce la clave API proporcionada por Futit Services.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/bank-integration/psd2-bank-integration-1.png)

!!!info
    Cada usuario que vaya a realizar sincronización bancaria o iniciación de pagos debe tener configurada su propia clave API. La clave API es específica por usuario y debe mantenerse confidencial.

!!!warning "Visibilidad de botones y campos"
    Todos los botones y campos de integración PSD2 **solo son visibles** cuando el usuario conectado tiene configurada una PSD2 API Key. Esto incluye:
    
    - En la ventana **Cuenta financiera**: el botón **Connect Bank Account**, el botón **Get Bank Statement**, el selector **Bank Provider**, y los campos **Import From Date**, **Import To Date** y **Statement Frequency**.
    - En la ventana **Pago**: el botón **Generate Bank Payment**.
    
    Si no ves estos elementos, verifica que el usuario actual tenga una clave API válida introducida en el campo **PSD2 API Key** de la ventana Usuario.

### Paso 2: Configurar Cuentas financieras

:material-menu: `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Transacciones` > `Cuenta financiera`

Para cada cuenta financiera que quieras sincronizar con un banco:

#### 2.1 Establecer el rango de fechas de importación

En la pestaña o sección **PSD2 Bank Integration** de la Cuenta financiera:

- **Import From Date**: especifica la fecha de inicio para importar transacciones. 
    - Si se deja vacío, el sistema usará la fecha del último extracto bancario importado
    - Establece esta fecha para controlar hasta dónde atrás deben recuperarse las transacciones

- **Import To Date**: especifica la fecha de fin para importar transacciones.
    - Si se deja vacío, el sistema usará la fecha actual
    - Útil para importar datos históricos hasta un punto concreto

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/bank-integration/psd2-bank-integration-2.png)

!!!tip
    **Mejor práctica para la configuración inicial:**
    - Establece **Import From Date** en la fecha desde la que quieres empezar a seguir las transacciones (p. ej., inicio del ejercicio fiscal)
    - Deja **Import To Date** vacío para importar siempre hasta la fecha actual
    - Tras la primera importación, puedes dejar **Import From Date** vacío para continuar automáticamente desde la última importación

!!!note
    **Cómo funciona la lógica de fechas:**
    - El sistema registra automáticamente la última fecha de importación para cada cuenta
    - En importaciones posteriores, si **Import From Date** está vacío, comenzará desde la última fecha de importación
    - Esto evita importar las mismas transacciones varias veces

#### 2.2 Configurar el proveedor bancario

Opcionalmente, puedes asignar un proveedor bancario a cada cuenta financiera. Esta configuración afecta tanto al flujo de **Bank Connection (AIS)** como al de **Bank Payment Initiation (PIS)**:

- **Bank Provider**: selecciona el banco que corresponde a esta cuenta financiera de la lista de proveedores disponibles.
    - **Al conectar con un banco (AIS):** el widget de Salt Edge **omitirá el paso de selección de banco** y conectará directamente con el banco asignado.
    - **Al iniciar pagos (PIS):** el widget de autorización de pago **omitirá el paso de selección de banco** e irá directamente a la pantalla de autorización del pago.
    - Si se deja vacío, se pedirá al usuario que seleccione un banco cada vez.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/bank-integration/psd2-bank-integration-3.png)

!!!tip
    Se recomienda encarecidamente asignar un proveedor bancario cuando la cuenta financiera esté siempre asociada al mismo banco. Esto agiliza tanto el proceso de conexión como el de pago para los usuarios finales.

!!!note
    La lista de proveedores bancarios disponibles debe sincronizarse primero. Consulta **Paso 3: Synchronize Bank Providers** más abajo.

#### 2.3 Establecer la frecuencia de extracto

El campo **Statement Frequency** controla cómo se agrupan las transacciones importadas en extractos bancarios:

| Opción | Comportamiento |
|---|---|
| **One per run** *(por defecto)* | Crea un nuevo extracto bancario cada vez que se ejecuta el proceso de importación |
| **One per week** | Agrupa las transacciones en extractos bancarios semanales (un extracto por semana natural) |
| **One per month** | Agrupa las transacciones en extractos bancarios mensuales (un extracto por mes natural) |

!!!tip
    - Usa **One per run** si importas transacciones con frecuencia y prefieres que cada importación sea un extracto bancario independiente.
    - Usa **One per week** o **One per month** para mantener los extractos bancarios más organizados y reducir el número total de extractos, especialmente al importar a diario.

!!!note
    Al usar **One per week** o **One per month**, el sistema añadirá nuevas transacciones a un extracto bancario existente si ya existe uno para el periodo actual. Si el extracto existente ha sido procesado, el sistema lo reactivará automáticamente para añadir las nuevas transacciones.

### Paso 3: Sincronizar proveedores bancarios

Antes de iniciar pagos bancarios o conectar con un banco, el sistema necesita una lista actualizada de proveedores bancarios. Esto se realiza ejecutando manualmente desde el menú el proceso **Synchronize Bank Providers**.

:material-menu: `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Configuración` > `PSD2` > `Synchronize Bank Providers`

1. Navega a la entrada de menú anterior y ejecuta el proceso.
2. El proceso:
    - Se conectará a Salt Edge a través del middleware.
    - Descargará todos los bancos que soportan iniciación de pagos (plantillas SEPA, FPS o DOMESTIC).
    - Creará o actualizará la lista de proveedores en Etendo.

!!!info
    Este proceso debe ejecutarse manualmente cuando sea necesario — por ejemplo, al configurar el módulo por primera vez o periódicamente (p. ej., una vez por semana) para mantener actualizada la lista de proveedores. La lista de bancos soportados no cambia con frecuencia.

!!!note
    El proceso Synchronize Bank Providers utiliza cualquier clave API disponible de usuarios configurados. No requiere que un usuario específico lo ejecute.

## Flujo de conexión bancaria (AIS)

### Paso 4: Conectar cuenta bancaria

Una vez que tu usuario tenga la clave API configurada y las fechas de la cuenta financiera estén establecidas:

!!!tip
    Asegúrate de que tu Cuenta financiera tenga configurado el campo **IBAN** antes de conectar. El sistema lo utiliza para ayudar a emparejar correctamente tus cuentas bancarias. Si falta el IBAN, verás un mensaje de advertencia.

1. Abre la **Cuenta financiera** que quieres conectar
2. Haz clic en el botón **Connect Bank Account**
3. Se abrirá un **widget de conexión de Salt Edge** en una ventana emergente

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/bank-integration/psd2-bank-integration-5.png)

4. En el widget:
    - **Busca o selecciona tu banco** de la lista de bancos soportados
    - Haz clic en tu banco para continuar

    !!!info
        Si has asignado un **Bank Provider** a la Cuenta financiera (ver Paso 2, sección 2.2), el paso de selección de banco se **omite automáticamente** y se te llevará directamente a la página de autenticación de tu banco.

5. Serás **redirigido a la página de inicio de sesión de tu banco**

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/bank-integration/psd2-bank-integration-6.png)

6. **Inicia sesión con tus credenciales bancarias** (usuario, contraseña y cualquier autenticación adicional requerida por tu banco)

    !!!warning
        **Nota importante de seguridad:**
        - Tus credenciales bancarias se introducen directamente en el sitio web de tu banco, no en Etendo
        - Salt Edge nunca almacena tus credenciales bancarias
        - Etendo nunca tiene acceso a tu usuario o contraseña del banco

7. **Autoriza la conexión**:
    - Tu banco te pedirá que confirmes el permiso para que Salt Edge acceda a la información de tu cuenta
    - Revisa los permisos y confirma

8. **Sincronización automática**:
    - Tras una autenticación correcta, el sistema **recupera automáticamente tus cuentas bancarias**
    - Serás redirigido a una **página de éxito** que muestra:
        - Un mensaje de confirmación de que la conexión bancaria se ha realizado correctamente
        - Confirmación de que tus cuentas se han sincronizado
        - Instrucciones para cerrar la ventana emergente

    !!!success
        **¡Conexión y sincronización completadas!**
        - Se ha establecido la conexión bancaria
        - Tus cuentas bancarias se han sincronizado automáticamente
        - Los detalles de la conexión ya son visibles en la pestaña **Bank Connections**
        - Ya puedes empezar a importar transacciones

9. **Siguientes pasos**:
    - Cierra la ventana emergente
    - Vuelve a tu ventana de Etendo
    - Ya puedes proceder a importar transacciones (consulta la sección Importación de transacciones más abajo)

!!!info
    **Qué ocurre automáticamente:**
    - El sistema crea la conexión con Salt Edge
    - Recupera todas las cuentas asociadas a tu conexión bancaria
    - Vincula tus cuentas de Salt Edge con tu cuenta financiera de Etendo
    - Todos los detalles de la conexión se almacenan en la pestaña **Bank Connections**
    
    No necesitarás ejecutar manualmente "Synchronize Bank Connections" después de conectar: se hace automáticamente.

## Importación de transacciones

Hay dos formas de importar transacciones bancarias:

### Opción 1: Importación manual (cuenta única)

Para importar transacciones bajo demanda para cuentas específicas:

1. Abre la ventana **Cuenta financiera**.
2. Selecciona una o más cuentas financieras.
3. Haz clic en el botón **Get Bank Statement**.

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/bank-integration/psd2-bank-integration-7.png)

4. El sistema:
    - Se conectará a Salt Edge.
    - Recuperará transacciones dentro del rango de fechas configurado.
    - Filtrará transacciones duplicadas.
    - Creará o actualizará extractos bancarios.
    - Creará líneas de extracto bancario para cada transacción.

5. Un mensaje resumen mostrará los resultados:
    - Número de nuevas transacciones importadas.
    - Cualquier advertencia o error encontrados.

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/bank-integration/psd2-bank-integration-8.png)

!!!tip
    Usa esta opción cuando necesites importar transacciones inmediatamente para cuentas específicas o cuando quieras revisar los resultados de la importación al momento.

### Opción 2: Importación automática (proceso planificado)

Para importaciones regulares y automatizadas en todas las cuentas conectadas:

:material-menu: `Configuración General` > `Planificador de procesos` > `Procesamiento de Peticiones`

1. Planifica el proceso **Get Bank Statements**
2. Configura la frecuencia (p. ej., diaria, horaria)
3. El proceso automáticamente:
    - Comprobará todos los usuarios con claves API configuradas
    - Procesará todas las cuentas financieras con conexiones bancarias activas
    - Importará nuevas transacciones para cada cuenta
    - Registrará los resultados

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/bank-integration/psd2-bank-integration-9.png)

    !!!info
        **Planificación recomendada:**
        - Para la mayoría de empresas: ejecutar una o dos veces al día (p. ej., 6:00 y 18:00)
        - Para cuentas de alto volumen: ejecutar cada pocas horas
        - Ten en cuenta la frecuencia de actualización de tu banco y las necesidades de tu negocio

## Comprender los resultados

### Creación de extractos bancarios

Cuando se importan transacciones, el sistema automáticamente:

1. **Crea o actualiza extractos bancarios**:
    - Un extracto bancario por periodo de importación
    - La fecha del extracto refleja el rango de fechas de importación
    - Los extractos se vinculan a la Cuenta financiera

2. **Crea líneas de extracto bancario**:
    - Una línea por transacción
    - Incluye fecha de la transacción, descripción e importe
    - Almacena el ID de transacción de Salt Edge para evitar duplicados

3. **Registra la operación**:
    - Todas las operaciones de sincronización se registran en la pestaña **Bank Transaction Logs**.
    - Los logs incluyen fecha de ejecución, estado, datos de solicitud/respuesta y detalles de error.
    - Accesible desde la ventana Cuenta financiera para monitorización y resolución de incidencias.
    - Útil para auditoría y depuración de problemas de integración.

### Detalles de la transacción

Cada transacción importada incluye:

- **Fecha de la transacción**: cuándo ocurrió la transacción
- **Importe**: importe de la transacción (positivo para abonos, negativo para cargos)
- **Descripción**: descripción de la transacción desde el banco
- **Referencia**: referencia o ID de la transacción
- **Estado**: estado de la transacción (booked, pending, etc.)

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/bank-integration/psd2-bank-integration-10.png)

### Prevención de duplicados

El sistema evita importaciones duplicadas mediante:

- El seguimiento de los IDs de transacción de Salt Edge
- La comprobación de si una transacción ya fue importada
- Omitir transacciones marcadas como duplicadas por Salt Edge
## Gestión de conexiones

### Estado de la conexión

Las conexiones bancarias pueden tener diferentes estados:

- **Activo (AC)**: la conexión funciona con normalidad
- **Inactivo (IN)**: la conexión existe, pero no se está utilizando para transacciones
- **Deshabilitado (DI)**: la conexión se ha deshabilitado (p. ej., la autenticación ha caducado)

### Ver conexiones bancarias

Para ver todas tus conexiones bancarias:

1. Abre la ventana **Cuenta financiera**
2. Navega a la pestaña **Bank Connections**
3. Aquí puedes ver todas las conexiones asociadas a la cuenta financiera, incluyendo:
    - Nombre del proveedor
    - ID de conexión de Salt Edge
    - Estado de la conexión
    - Fecha de última actualización
    - Ámbitos de obtención (permisos concedidos)

### Sincronizar conexiones bancarias

El proceso **Synchronize Bank Connections** te permite actualizar manualmente la información de conexión de tus cuentas financieras. Ejecútalo desde:

:material-menu: `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Configuración` > `PSD2` > `Synchronize Bank Connections`

El proceso:

- Comprueba el estado actual de todas las conexiones bancarias de las cuentas financieras configuradas.
- Actualiza los estados de conexión para reflejar el estado en tiempo real desde Salt Edge.
- Actualiza la información de cuenta asociada a cada conexión.

Un mensaje de resumen mostrará los resultados.

!!!tip
    Normalmente no necesitas ejecutar este proceso a menudo. Las conexiones bancarias se sincronizan automáticamente cuando conectas un banco por primera vez. Úsalo solo si sospechas que el estado de una conexión está desactualizado o después de realizar cambios en tu banco (p. ej., añadir nuevas cuentas).

### Desconectar una conexión bancaria

Si necesitas eliminar una conexión bancaria:

1. Abre la ventana **Cuenta financiera**
2. Navega a la pestaña **Bank Connections**
3. Selecciona la(s) conexión(es) que quieres desconectar
4. Haz clic en el botón **Disconnect Connection**

    !!!warning
        **Importante:**
        - Desconectar una conexión la eliminará permanentemente tanto de Etendo como de Salt Edge
        - Tendrás que reconectar si quieres volver a usar esta conexión bancaria
        - Esta acción no se puede deshacer
        - Cualquier transacción pendiente no se verá afectada, pero no se podrán importar nuevas transacciones desde esta conexión

5. Tras la desconexión:
    - La conexión se elimina de la base de datos
    - La conexión se elimina de Salt Edge
    - Puedes verificar que la desconexión se ha realizado correctamente comprobando la pestaña Bank Connections

### Reconectar una conexión bancaria

Si una conexión bancaria ha pasado a **Inactivo** o **Deshabilitado** (por ejemplo, porque la autenticación del banco ha caducado), puedes reconectarla directamente desde Etendo:

1. Abre la ventana **Cuenta financiera**.
2. Navega a la pestaña **Bank Connections**.
3. Selecciona la conexión que quieres restaurar.
4. Haz clic en el botón **Reconnect Connection**.

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/bank-integration/psd2-bank-integration-11-a.png)
    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/bank-integration/psd2-bank-integration-11-b.png)

5. Se abrirá un **Salt Edge reconnect widget** en una ventana emergente.
6. Vuelve a autenticarte con tu banco introduciendo tus credenciales y confirmando la conexión.
7. Tras una autenticación correcta, verás una **página de confirmación**.
8. Cierra la ventana emergente y vuelve a Etendo. El estado de la conexión se actualizará a **Activo**.

!!!info
    El botón Reconectar primero comprueba el estado de la conexión en tiempo real desde Salt Edge:
    
    - Si la conexión **ya está activa**, recibirás un mensaje de éxito y no será necesaria ninguna acción adicional.
    - Si la conexión está **Inactivo** o **Deshabilitado**, se abrirá el widget de reconexión para volver a autenticar.

!!!note
    **Qué ocurre cuando fallan las conexiones durante la importación de transacciones:**
    
    Cuando se ejecuta el proceso **Get Bank Statements** y encuentra un problema de conexión, el sistema automáticamente:
    
    - Marca la conexión que falla como **Deshabilitado**.
    - Registra un mensaje de advertencia.
    - Prueba la siguiente conexión disponible para la misma cuenta financiera.
    - Continúa hasta encontrar una conexión operativa o agotar todas las disponibles.
    
    Las conexiones fallidas aparecerán con estado **Deshabilitado** en la pestaña **Bank Connections**. Usa el botón **Reconnect Connection** para restaurarlas.

## Iniciación de pagos bancarios (PIS)

Además de importar transacciones bancarias (AIS), este módulo te permite **iniciar pagos bancarios directamente desde Etendo**. Cuando creas un registro de **Pago** en Etendo, puedes enviarlo a tu banco para su autorización y ejecución, sin salir del ERP.

### Cómo funcionan los pagos bancarios

El flujo de iniciación de pagos funciona así:

1. Creas un registro de **Pago** en Etendo como de costumbre.
2. Desde el registro del pago, haces clic en el botón **Generate Bank Payment**.
3. Aparece un formulario con valores precargados (importe, acreedor, plantilla, etc.).
4. Tras revisar y confirmar, se abre un **popup de autorización bancaria**.
5. Autorizas el pago en el entorno seguro de tu banco.
6. El estado del pago se rastrea automáticamente en Etendo.

!!!info
    Tus credenciales bancarias nunca se introducen en Etendo. La autorización se gestiona completamente en la página de autenticación segura de tu banco, a la que se accede mediante el widget de Salt Edge.

### Plantillas de pago

El sistema soporta tres plantillas de pago, que determinan el formato y la información requerida para el pago:

| Plantilla | Moneda | Campos obligatorios | Caso de uso |
|---|---|---|---|
| **SEPA** | Solo EUR | IBAN del acreedor | Transferencias bancarias en la zona euro |
| **FPS** | Solo GBP | Código sort + Número de cuenta | UK Faster Payments |
| **DOMESTIC** | Cualquiera | Al menos uno de: IBAN, BBAN o Número de cuenta | Otras transferencias nacionales |

!!!note
    La plantilla se **selecciona automáticamente** en función de la moneda del pago:
    
    - EUR → SEPA
    - GBP → FPS
    - Cualquier otra moneda → DOMESTIC
    
    Si es necesario, puedes cambiar la plantilla manualmente en el formulario.

### Generar un pago bancario

:material-menu: `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Pago`

1. Abre un registro existente de **Pago**.
2. Haz clic en el botón **Generate Bank Payment**.

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/bank-integration/psd2-bank-integration-12.png)

3. Aparece un **formulario de proceso** con los siguientes campos precargados:

    | Campo | Valor por defecto | Descripción |
    |---|---|---|
    | **Plantilla** | Según la moneda | Plantilla de pago (SEPA, FPS o DOMESTIC) |
    | **Importe** | Importe del pago | Importe a transferir |
    | **Moneda** | Moneda del pago | Moneda de la transferencia |
    | **Nombre del acreedor** | Nombre del tercero | Nombre del beneficiario del pago |
    | **ID End-to-End** | Número de documento | Referencia única del pago (máx. 35 caracteres) |
    | **Descripción** | Descripción del pago | Descripción del pago |
    | **IBAN del acreedor** | IBAN del tercero | Obligatorio para SEPA y opcional para DOMESTIC |
    | **Número de cuenta del acreedor** | Cuenta del tercero | Obligatorio para FPS, opcional para DOMESTIC |

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/bank-integration/psd2-bank-integration-13.png)

    !!!tip
        Los valores del formulario se calculan automáticamente a partir de los datos del Pago y del Tercero. Asegúrate de que tus Terceros tengan configurada su **información de cuenta bancaria** (IBAN o número de cuenta) para una mejor experiencia.

4. Revisa los valores y haz clic en **Done** para iniciar el pago.

5. Se abre un **popup de autorización bancaria** donde debes autorizar el pago con tu banco.

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/bank-integration/psd2-bank-integration-14.png)

    !!!warning
        **No cierres el popup** hasta haber completado el proceso de autorización con tu banco. El pago no puede continuar sin tu autorización.

6. Tras completar la autorización, verás una **página de confirmación** indicando que el pago se ha registrado.

7. Cierra el popup y vuelve a Etendo. El estado del pago se actualizará automáticamente.

!!!info
    **Qué ocurre en segundo plano:**
    
    - Si hay un **Bank Provider** configurado en la Cuenta financiera, el paso de selección del banco se omite automáticamente.
    - Si no hay proveedor configurado, se te pedirá que selecciones tu banco en el widget.
    - El registro del pago se guarda en la pestaña **Bank Payments** con un estado inicial "requested".

### Ciclo de vida del estado del pago

Tras iniciar un pago bancario, pasa por varias etapas de estado:

| Estado | Descripción |
|---|---|
| **Requested** | El pago se ha creado en Etendo, pendiente de envío a Salt Edge |
| **Initiated** | La solicitud de pago se ha enviado a Salt Edge |
| **Authorizing** | El usuario está completando la autorización con el banco |
| **Authorized** | El usuario ha autorizado el pago en el banco |
| **Processing** | El banco está procesando el pago |
| **Executed** | El pago se ha completado correctamente ✅ |
| **Liquidado** | El pago ha sido liquidado por el banco ✅ |
| **Failed** | El pago ha fallado ❌ |

!!!note
    Una vez que un pago alcanza un **estado destino** (Executed, Liquidado o Failed), no se puede modificar. Si un pago falla, puedes crear un nuevo intento de pago desde el mismo registro de Pago.

### Ver pagos bancarios

Todos los pagos bancarios iniciados se registran en la pestaña **Bank Payments**:

:material-menu: `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Pago` > pestaña **Bank Payments**

Esta pestaña muestra:

- **Salt Edge Payment ID**: identificador único del pago en Salt Edge
- **Status**: estado actual del pago (ver ciclo de vida anterior)
- **Status Detail**: información adicional de estado desde el banco (p. ej., códigos de estado en bruto del banco)
- **Plantilla**: plantilla de pago utilizada (SEPA, FPS, DOMESTIC)
- **Importe y Moneda**: importe y moneda del pago
- **Nombre del acreedor e IBAN**: información del beneficiario
- **Nombre del deudor e IBAN**: información de la cuenta de tu empresa (se completa automáticamente)
- **ID End-to-End**: referencia única del pago
- **Provider Code**: proveedor bancario utilizado para el pago
- **Last Status Update**: cuándo se actualizó por última vez el estado
- **Descripción**: descripción del pago

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/bank-integration/psd2-bank-integration-15.png)

### Actualizar el estado del pago

El estado del pago se actualiza automáticamente mediante dos mecanismos:

#### Actualizaciones automáticas (Webhooks)

Salt Edge envía notificaciones automáticas de estado a Etendo cada vez que el estado del pago cambia en el banco. Estas actualizaciones se procesan inmediatamente y el registro del pago se actualiza en tiempo real.

!!!info
    Las actualizaciones por webhook se producen automáticamente: no se requiere ninguna acción del usuario. Cuando el banco procese tu pago, el estado en Etendo se actualizará en cuestión de segundos.

#### Actualización manual

Si quieres comprobar el último estado inmediatamente:

1. Navega a la pestaña **Bank Payments**.
2. Selecciona uno o varios registros de pago.
3. Haz clic en el botón **Refresh Payment**.

    ![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/bank-integration/psd2-bank-integration-16.png)

4. El sistema consultará a Salt Edge el estado actual y actualizará el registro.

!!!tip
    Usa la actualización manual cuando quieras verificar el estado actual de un pago sin esperar a la siguiente actualización automática.

#### Actualización automática programada

Para mayor fiabilidad, el módulo incluye un **proceso programado preconfigurado** que actualiza automáticamente el estado de los pagos pendientes. El proceso **Refresh Pending Payments** se importa como parte del dataset de sistema del módulo y se ejecuta cada **10 minutos** por defecto.

El proceso:

- Encuentra todos los pagos en estados no finales (Initiated, Authorizing, Authorized, Processing).
- Consulta a Salt Edge el estado más reciente de cada pago.
- Actualiza los registros de pago en consecuencia.

!!!info
    El proceso de actualización programada actúa como red de seguridad que complementa el mecanismo de webhooks. Garantiza que los estados de pago se actualicen finalmente incluso si una notificación webhook se retrasa o se pierde. El proceso respeta los límites de tasa de la API comprobando solo los pagos que no se han actualizado en los últimos 5 minutos.

!!!tip
    **Ajustar la frecuencia de actualización:**
    
    Si necesitas una frecuencia diferente (p. ej., cada 5 minutos), puedes crear una nueva entrada de **Procesamiento de Peticiones** para el proceso **Refresh Pending Payments** con tu programación preferida. En ese caso, asegúrate de **desprogramar primero la entrada importada por el sistema** para evitar que ambas se ejecuten simultáneamente.
    
    :material-menu: `Configuración General` > `Planificador de procesos` > `Procesamiento de Peticiones`

## Problemas comunes y soluciones

### Problemas comunes

- **"No API Key Available"**
    - Asegúrate de que tu usuario tiene configurada la Salt Edge API Key.
    - Comprueba que la API Key es correcta y está activa.

- **"Invalid or expired API Key"**
    - Tu API Key ha caducado o ya no es válida.
    - Contacta con tu administrador de Etendo o con el soporte de Futit Services para obtener una nueva API Key.
    - Actualiza la API Key en la ventana Usuario (campo **PSD2 API Key**).

- **"Could not get redirect link"**
    - El servicio de conexión bancaria puede no estar disponible temporalmente.
    - Inténtalo de nuevo en unos minutos.
    - Contacta con soporte si el problema persiste.

- **"No new transactions found"**
    - Revisa la configuración de fechas Import From/To Date.
    - Verifica que realmente hay nuevas transacciones en tu cuenta bancaria.
    - Asegúrate de que el rango de fechas cubre el periodo esperado.

- **Errores de límite de tasa**
    - El sistema ha superado el número permitido de solicitudes a la API.
    - Normalmente es un error transitorio: espera unos minutos e inténtalo de nuevo.
    - Si usas procesos programados, evita ejecutarlos con demasiada frecuencia (ver Buenas prácticas).

- **Servicio temporalmente no disponible**
    - Salt Edge o el middleware pueden estar en mantenimiento.
    - Estos errores son transitorios y se resolverán automáticamente.
    - El sistema reintentará automáticamente en procesos programados.

- **El Estado de la conexión muestra "Disabled"**
    - Una conexión puede mostrarse como **Deshabilitado** debido a:
        - Caducidad de la autenticación con el banco.
        - Errores de comunicación con Salt Edge.
        - Indisponibilidad temporal del servicio del banco.
    - **Pasos de resolución recomendados:**
        1. Primero, ejecuta el proceso **Synchronize Bank Connections** (desde **Gestión Financiera > Gestión de Cobros y Pagos > Configuración > PSD2 > Synchronize Bank Connections**) para verificar el estado actual de la conexión y actualizar su estado.
        2. Intenta ejecutar **Get Bank Statements** de nuevo para ver si el problema persiste.
        3. Si la conexión sigue apareciendo como **Deshabilitado**, haz clic en el botón **Reconnect Connection** en la pestaña **Bank Connections** para volver a autenticarte con tu banco (ver [Reconectar una conexión bancaria](#reconectar-una-conexión-bancaria)).

#### Problemas de iniciación de pagos (PIS)

- **"Template Required"**
    - No se pudo determinar automáticamente la plantilla de pago.
    - Asegúrate de que el pago tiene una moneda válida configurada.

- **"Creditor Name Required"**
    - Falta el nombre del Tercero.
    - Verifica que el pago tiene asignado un Tercero con un nombre válido.

- **"IBAN Required for SEPA"**
    - Los pagos SEPA requieren el IBAN del acreedor.
    - Configura la cuenta bancaria del Tercero con un IBAN válido.

- **"SEPA Requires EUR" / "FPS Requires GBP"**
    - Los pagos SEPA solo pueden usar EUR y FPS solo puede usar GBP.
    - Comprueba la moneda del pago o cambia a la plantilla DOMESTIC.

- **"Sort Code Required for FPS" / "Account Number Required for FPS"**
    - Los pagos FPS (UK) requieren tanto sort code como número de cuenta.
    - Configura la cuenta bancaria del Tercero con estos datos.

- **El estado del pago se queda en "Initiated" o "Authorizing"**
    - Es posible que el usuario no haya completado la autorización en el banco.
    - Prueba a hacer clic en **Refresh Payment** para comprobar el estado más reciente.
    - Si el problema persiste, el banco puede haber rechazado el pago: revisa el campo **Status Detail** para más información.

- **El popup de autorización bancaria fue bloqueado**
    - Tu navegador puede haber bloqueado la ventana emergente.
    - Permite popups para el sitio de Etendo e inténtalo de nuevo.

- **"Payment Not Found" tras volver del banco**
    - Esto puede ocurrir si la sesión del navegador caducó durante la autorización.
    - Revisa la pestaña **Bank Payments**: el pago puede haberse procesado correctamente vía webhooks aunque el redirect haya fallado.

### Obtener soporte

Si encuentras problemas:

1. Revisa la ventana **PSD2 Logs** para obtener información detallada del error (ver [Monitorización y logs](#monitorización-y-logs) más abajo).
2. Verifica que tu API Key está configurada correctamente y no ha caducado.
3. Asegúrate de que el rango de fechas es adecuado para la operación.
4. Para problemas de conexión, prueba el botón **Reconnect Connection** antes de contactar con soporte.
5. Contacta con el soporte de Futit Services con:
    - El mensaje de error mostrado en Etendo.
    - Las entradas de log relevantes de la ventana **PSD2 Logs**.
    - La cuenta financiera afectada.
    - La fecha y hora en que ocurrió el problema.

## Monitorización y logs

El módulo proporciona ventanas dedicadas para monitorizar la actividad de integración y revisar logs detallados.

### PSD2 Logs

La ventana **PSD2 Logs** te permite revisar toda la actividad y los logs de error generados por la integración. Accede desde:

:material-menu: `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Configuración` > `PSD2` > `PSD2 Logs`

Cada entrada de log incluye la siguiente información:

| Campo | Descripción |
|-------|-------------|
| **Cuenta financiera** | La cuenta financiera asociada al evento. |
| **Día de ejecución** | La fecha y hora en que ocurrió el evento. |
| **Estado** | El resultado de la operación (p. ej., *Success*, *Error*). |
| **Fuente** | El proceso o acción que generó el log (p. ej., *Get Transactions*, *Generate Payment*). |
| **Log** | Una descripción legible del evento. |
| **Información JSON** | La respuesta técnica en bruto de la API, útil para diagnóstico. |

!!! tip "Uso de PSD2 Logs para diagnóstico"
    Al investigar un problema, filtra los logs por **Cuenta financiera** y ordena por **Día de ejecución** (descendente) para encontrar rápidamente los eventos más recientes. El campo **Información JSON** contiene la respuesta completa de la API, lo cual es valioso al contactar con soporte.

### Ventana Bank Provider

La ventana **Bank Provider** muestra la lista de bancos disponibles a través de Salt Edge que soportan la integración. Accede desde:

:material-menu: `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Configuración` > `PSD2` > `Bank Provider`

Cada entrada muestra:

| Campo | Descripción |
|---|---|
| **Provider Code** | El identificador único que utiliza Salt Edge para el banco. |
| **Provider Name** | El nombre visible del banco proporcionado por Salt Edge. |

!!! info "Mantener actualizada la lista de proveedores"
    La lista de proveedores se rellena y actualiza mediante el proceso **Synchronize Bank Providers** (disponible desde el menú: **Gestión Financiera > Gestión de Cobros y Pagos > Configuración > PSD2 > Synchronize Bank Providers**). Se recomienda ejecutar este proceso periódicamente (p. ej., semanalmente) para asegurar que los nuevos bancos estén disponibles y que se eliminen los proveedores obsoletos.
## Buenas Prácticas

1. **Sincronización regular**: Programa las importaciones automáticas para que se ejecuten a diario o varias veces al día.

2. **Configuración de fechas**: 
    - Utiliza **Import From Date** solo para la configuración inicial.
    - Déjalo vacío después para continuar automáticamente desde la última importación.

3. **Conciliación**: 
    - Revisa regularmente las transacciones importadas.
    - Utiliza las funcionalidades de conciliación de Etendo para emparejar transacciones con pagos.

4. **Mantenimiento de conexiones**:
    - Supervisa regularmente el estado de la conexión en la pestaña **Bank Connections**.
    - Si una conexión aparece como **Disabled** o **Inactive**, utiliza el botón **Reconnect Connection** para volver a autenticarte con tu banco.
    - Las cuentas bancarias se sincronizan automáticamente cuando conectas un banco por primera vez.
    - Ejecuta el proceso **Synchronize Bank Connections** solo si necesitas actualizar manualmente el estado de la conexión o la información de la cuenta (p. ej., tras añadir nuevas cuentas en tu banco).
    - Utiliza el botón **Disconnect Connection** para eliminar conexiones que ya no necesites.

5. **Múltiples bancos**:
    - Configura cada banco por separado.
    - Utiliza convenciones de nombres claras para las cuentas financieras.
    - Cada conexión bancaria recuperará y vinculará automáticamente todas las cuentas disponibles.

6. **Seguridad**:
    - Mantén las claves API confidenciales.
    - No compartas credenciales de usuario.
    - Desconecta las conexiones bancarias cuando ya no sean necesarias usando el botón **Disconnect Connection**.
    - Al desconectar, la conexión se elimina de forma permanente tanto de Etendo como de Salt Edge.

7. **Pagos bancarios (PIS)**:
    - Asigna un **Bank Provider** a cada cuenta financiera para agilizar el proceso de autorización de pagos.
    - El proceso **Refresh Pending Payments** está preconfigurado para ejecutarse cada 10 minutos. Ajusta la frecuencia solo si tu negocio requiere actualizaciones más rápidas.
    - Asegúrate de que los terceros tengan correctamente configurados sus **datos de cuenta bancaria** (IBAN o número de cuenta) antes de iniciar pagos.
    - Revisa regularmente la pestaña **Bank Payments** para monitorizar el estado de los pagos iniciados.
    - Si un pago falla, revisa el campo **Status Detail** para ver el mensaje de error específico del banco antes de reintentar.

8. **Proveedores bancarios**:
    - Ejecuta periódicamente el proceso **Synchronize Bank Providers** (p. ej., semanalmente) para mantener actualizada la lista de proveedores.
    - Solo los bancos que soportan iniciación de pagos (SEPA, FPS o DOMESTIC) aparecerán en la lista de proveedores.

9. **Monitorización**:
    - Revisa periódicamente la ventana **PSD2 Logs** para detectar incidencias recurrentes.
    - Presta atención a los logs con estado **Error**, especialmente los relacionados con claves API caducadas o fallos de conexión.
    - Comparte las entradas de log relevantes (incluyendo los datos de **Información JSON**) al contactar con soporte para una resolución más rápida.

## Recursos adicionales

- [Documentación de Salt Edge](https://docs.saltedge.com/){target="_blank"}
- [Notas de la versión del Financial Extensions Bundle](https://docs.etendo.software/whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes/){target="_blank"}
- [Guía de conciliación bancaria](../basic-features/financial-management/receivables-and-payables/transactions.md#bank-reconciliation){target="_blank"}