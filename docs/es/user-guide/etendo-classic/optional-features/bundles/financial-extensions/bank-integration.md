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

# Integración bancaria con Salt Edge { #bank-integration-with-salt-edge }

:octicons-package-16: Javapackage: `com.etendoerp.psd2.bank.integration`

!!!info "Antes de comenzar"
    Este módulo requiere que el **Financial Extensions Bundle** esté instalado en su entorno de Etendo. Si no está seguro de si está instalado, contacte con su administrador de sistemas antes de continuar. Para instrucciones de instalación, visite el marketplace: [Financial Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=9876ABEF90CC4ABABFC399544AC14558){target="_blank"}. Para las versiones disponibles y compatibilidad con el core, visite [Financial Extensions - Release notes](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md).

## Visión general { #overview }

Esta página explica cómo conectar cuentas bancarias a Etendo para que las transacciones se importen automáticamente y los pagos salientes puedan iniciarse directamente desde el sistema. Está dirigida al personal de finanzas y contabilidad que realiza conciliaciones bancarias y ejecuciones de pagos a proveedores, y a los administradores que realizan la configuración inicial.

El módulo proporciona dos capacidades principales, ambas impulsadas por **[Salt Edge](https://www.saltedge.com/){target="_blank"}** — una plataforma de Open Banking que actúa como intermediario seguro entre Etendo y las entidades bancarias, conforme a la directiva PSD2. Etendo gestiona la conexión con Salt Edge en su nombre; no se requiere ninguna cuenta directa con Salt Edge.

- **AIS (Account Information Service)**: Conecte de forma segura cuentas bancarias y descargue automáticamente las transacciones para su conciliación.

    ``` mermaid
    flowchart LR
        A([Connect bank account]) --> B[Grant permissions]
        B --> C[Download transactions]
        C --> D([Bank statement ready\nfor reconciliation ✅])
    ```
- **PIS (Payment Initiation Service)**: Inicie pagos a proveedores directamente desde Etendo, con la autorización gestionada a través del banco.

    ``` mermaid
    flowchart LR
        A([Create Payment OUT]) --> B[Generate bank payment]
        B --> C[Authorize at bank portal]
        C --> D[Check payment status]
        D --> E([Payment executed ✅])
    ```

| | AIS | PIS |
|---|---|---|
| :material-bank-transfer: | Importación automatizada de transacciones | Iniciación directa de pagos |
| :material-sync: | Sincronización en tiempo real | Seguimiento de estado en tiempo real |
| :material-bank-outline: | Múltiples bancos simultáneamente | Plantillas SEPA, FPS y DOMESTIC |
| :material-shield-check: | Las credenciales bancarias nunca se almacenan en Etendo | La autorización la gestiona el banco |


## Requisitos previos { #prerequisites }

Confirme lo siguiente antes de utilizar la funcionalidad de Integración bancaria:

- :material-server: **Configuración del servidor**: Su administrador de sistemas ha configurado la URL de la aplicación `context.url` en el servidor de Etendo y ha ejecutado el proceso de configuración. Contacte con su equipo de IT o con el partner de implementación para confirmar que esto está hecho.
- :material-key: **Clave API de Salt Edge**: Su organización dispone de una clave API de Salt Edge. Contacte con el [Soporte de Etendo](../../../../../help-and-support/support-service.md) para solicitarla.
- :material-account: **Configuración de usuario**: La clave API está configurada en su perfil de usuario de Etendo (detallado en la sección de Configuración a continuación).
- :material-bank-outline: **Cuentas financieras**: Las cuentas financieras que se vincularán a sus cuentas bancarias existen en Etendo.
- :material-eye: **Visibilidad de botones**: Confirme que el usuario conectado tiene una **PSD2 API Key** configurada. Los botones y campos de integración (**Connect Bank Account**, **Get Bank Statement**, **Generate Bank Payment**, etc.) solo son visibles cuando la clave API está configurada.

## Configuración { #setup }

### 1. Configurar la clave API de Salt Edge { #configure-salt-edge-api-key }

:material-menu: `Aplicación` > `Configuración General` > `Seguridad` > `Usuario`

Como **Administrador** o usuario con permisos adecuados:

1. Navegue a la ventana **Usuario**.
2. Seleccione el registro de usuario que realizará las operaciones bancarias.
3. Localice el campo **API Key** en la sección **PSD2 Bank Integration** e introduzca la clave API proporcionada por el servicio de soporte.

![Campo PSD2 API Key en la ventana Usuario](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/bank-integration/bank-integration-1.png)

!!!info
    Cada usuario que vaya a realizar sincronización bancaria o iniciación de pagos debe tener configurada su propia clave API. La clave API es específica por usuario — manténgala confidencial.

!!!warning "Visibilidad de botones y campos"
    Todos los botones y campos de integración PSD2 **solo son visibles** cuando el usuario conectado tiene configurada una PSD2 API Key. Esto incluye:
    
    - En la ventana **Cuenta Financiera**: el botón **Connect Bank Account**, el botón **Get Bank Statement**, el selector **Bank Provider**, y los campos **Import From Date**, **Import To Date** y **Statement Frequency**.
    - En la ventana **Pago**: el botón **Generate Bank Payment**.
    
    Si no ve estos elementos, verifique que el usuario actual tenga una clave API válida introducida en el campo **PSD2 API Key** de la ventana Usuario.

### 2. Configurar Cuentas Financieras { #configure-financial-accounts }

:material-menu: `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Transacciones` > `Cuenta Financiera`

Para cada cuenta financiera que desee sincronizar con un banco, ábrala y complete los siguientes campos en la pestaña **PSD2 Bank Integration**:

![Campos de la pestaña PSD2 Bank Integration en la ventana Cuenta Financiera](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/bank-integration/bank-integration-2.png)

| Campo | Descripción |
|---|---|
| **Bank Provider** | El banco asociado a esta cuenta. Si está configurado, el paso de selección de banco se omite al conectar (AIS) o al iniciar pagos (PIS). Déjelo vacío para seleccionar el banco manualmente cada vez. La lista de proveedores debe sincronizarse primero — consulte el Paso 3. |
| **Import From Date** | Fecha de inicio para importar transacciones. Si se deja vacío, el sistema utiliza la fecha del último extracto bancario importado. Establezca esta fecha solo para la importación inicial (p. ej., inicio del ejercicio fiscal) — déjela vacía después para que las importaciones continúen automáticamente desde donde se detuvieron. |
| **Import To Date** | Fecha de fin para importar transacciones. Si se deja vacío, el sistema utiliza la fecha actual. Déjela vacía en la operación habitual. |
| **Statement Frequency** | Controla cómo se agrupan las transacciones importadas en extractos bancarios: **One per run** (por defecto) crea un nuevo extracto en cada importación; **One per week** o **One per month** agrupa las transacciones en un único extracto por periodo, reactivándolo si ya ha sido procesado. Use la agrupación semanal o mensual al importar a diario para reducir el número total de extractos. |

### 3. Sincronizar proveedores bancarios { #synchronize-bank-providers }

:material-menu: `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Configuración` > `PSD2` > `Synchronize Bank Providers`

Ejecute este proceso una vez durante la configuración inicial. Vuelva a ejecutarlo bajo demanda si un proveedor bancario no aparece en la lista o desea verificar si un banco concreto está soportado por Salt Edge. Ejecute el proceso desde el menú indicado — no se requiere un usuario específico.

!!!info
    Este paso es necesario antes de asignar un **Bank Provider** a una cuenta financiera o de iniciar pagos.

## Flujo de conexión bancaria (AIS) { #bank-connection-flow-ais }

### Conectar cuenta bancaria { #connect-bank-account }

Una vez que su usuario tenga la clave API configurada y las fechas de la cuenta financiera establecidas:

!!!tip
    Asegúrese de que su Cuenta Financiera tenga configurado el campo **IBAN** antes de conectar. El sistema lo utiliza para ayudar a emparejar correctamente sus cuentas bancarias. Si falta el IBAN, verá un mensaje de advertencia.

1. Abra la **Cuenta Financiera** (banco) que desea conectar.
2. Haga clic en el botón **Connect Bank Account**.
3. Se abrirá un **widget de conexión de Salt Edge** en una ventana emergente.

    ![Widget de selección de banco de Salt Edge](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/bank-integration/bank-integration-3.png)

    - **Busque o seleccione su banco** de la lista de bancos soportados
    - Haga clic en su banco para continuar
    
    !!!info
        Si ha asignado un **Bank Provider** a la Cuenta Financiera (consulte [Configuración - Paso 2](#configure-financial-accounts)), el paso de selección de banco se **omite automáticamente** y será llevado directamente a la página de autenticación de su banco.

4. **Autorice la conexión**:
    
    ![Pantalla de consentimiento de autorización bancaria](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/bank-integration/bank-integration-4.png)
    
    - Su banco le pedirá que confirme el permiso para que Salt Edge acceda a la información de su cuenta
    - Revise los permisos y confirme
 
5. Será **redirigido a la página de inicio de sesión de su banco**

    ![Página de inicio de sesión del banco para introducir credenciales](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/bank-integration/bank-integration-5.png)

    **Inicie sesión con sus credenciales bancarias** (usuario, contraseña y cualquier autenticación adicional requerida por su banco)

    !!!warning "Nota importante de seguridad"
       
        - Sus credenciales bancarias se introducen directamente en el sitio web de su banco, no en Etendo
        - Salt Edge nunca almacena sus credenciales bancarias
        - Etendo nunca tiene acceso a su usuario o contraseña del banco

6. Tras una autenticación correcta, una página de confirmación confirma la conexión. El sistema sincroniza automáticamente sus cuentas bancarias — los detalles de la conexión aparecen en la pestaña **Bank Connections**. Cierre la ventana emergente y proceda a importar transacciones.

    !!!info
        No es necesario ejecutar **Synchronize Bank Connections** manualmente tras conectar — se ejecuta automáticamente.

### Importación de transacciones { #importing-transactions }

Hay dos formas de importar transacciones bancarias:

#### Opción 1: Importación manual (cuenta única) { #option-1-manual-import-single-account }

Para importar transacciones bajo demanda para cuentas específicas:

1. Abra la ventana **Cuenta Financiera**.
2. Seleccione una o más cuentas financieras.
3. Haga clic en el botón **Get Bank Statement**.

    ![Botón Get Bank Statement en la ventana Cuenta Financiera](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/bank-integration/bank-integration-6.png)

4. El sistema:
    - Se conectará a Salt Edge.
    - Recuperará transacciones dentro del rango de fechas configurado.
    - Filtrará transacciones duplicadas.
    - Creará o actualizará extractos bancarios.
    - Creará líneas de extracto bancario para cada transacción.

5. Un mensaje resumen mostrará los resultados:
    - Número de nuevas transacciones importadas.
    - Cualquier advertencia o error encontrados.

    ![Mensaje resumen con los resultados de la importación](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/bank-integration/bank-integration-7.png)

    !!!tip
        Use esta opción cuando necesite importar transacciones inmediatamente para cuentas específicas o cuando desee revisar los resultados de la importación al momento.

    ![Líneas de extracto bancario creadas tras la importación de transacciones](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/bank-integration/bank-integration-8.png)

#### Opción 2: Importación automática (proceso planificado) { #option-2-automatic-import-scheduled-process }

Para importaciones regulares y automatizadas en todas las cuentas conectadas:

:material-menu: `Configuración General` > `Planificador de procesos` > `Procesamiento de Peticiones`

1. Haga clic en **Nuevo** para crear una nueva solicitud de proceso.
2. En el campo **Proceso**, seleccione **Get Bank Statements**.
3. Establezca el campo **Programado** con la frecuencia que necesite (por ejemplo, Diaria).
4. Guarde el registro. El proceso se ejecutará automáticamente en el intervalo elegido e importará nuevas transacciones para todas las cuentas conectadas.

    ![Solicitud de proceso planificado para la importación automática de extractos bancarios](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/bank-integration/bank-integration-9.png)

    !!!info
        **Planificación recomendada:**

        - Para la mayoría de empresas: ejecutar una o dos veces al día (p. ej., 6:00 y 18:00).
        - Para cuentas de alto volumen: ejecutar cada pocas horas.
        - Tenga en cuenta la frecuencia de actualización de su banco y las necesidades de su negocio.

## Gestión de conexiones { #connection-management }

:material-menu: `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Transacciones` > `Cuenta Financiera`

Para ver todas sus conexiones bancarias:

1. Abra la ventana **Cuenta Financiera**
2. Navegue a la pestaña **Bank Connections**
3. Aquí puede ver todas las conexiones asociadas a la cuenta financiera, incluyendo:
    - Nombre del proveedor
    - ID de conexión de Salt Edge
    - Estado de la conexión
    - Fecha de última actualización
    - Ámbitos de obtención (permisos concedidos)

### Estado de la conexión { #connection-status }

Las conexiones bancarias pueden tener diferentes estados:

- :material-check-circle:{ .green } **Activo (AC)**: la conexión funciona con normalidad
- :material-minus-circle:{ .orange } **Inactivo (IN)**: la conexión existe pero no se está utilizando para transacciones
- :material-close-circle:{ .red } **Deshabilitado (DI)**: la conexión ha sido deshabilitada (p. ej., la autenticación ha caducado)

### Sincronizar conexiones bancarias { #syncing-bank-connections }

:material-menu: `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Configuración` > `PSD2` > `Synchronize Bank Connections`

El proceso **Synchronize Bank Connections** permite actualizar manualmente la información de conexión de sus cuentas financieras.

El proceso:

- Comprueba el estado actual de todas las conexiones bancarias de las cuentas financieras configuradas.
- Actualiza los estados de conexión para reflejar el estado en tiempo real desde Salt Edge.
- Actualiza la información de cuenta asociada a cada conexión.

Un mensaje resumen mostrará los resultados.

!!!tip
    Ejecute este proceso solo si sospecha que el estado de una conexión está desactualizado o tras realizar cambios en su banco (p. ej., añadir nuevas cuentas). Las conexiones bancarias se sincronizan automáticamente cuando conecta un banco por primera vez.

### Desconectar una conexión bancaria { #disconnecting-a-bank-connection }

Si necesita eliminar una conexión bancaria:

1. Abra la ventana **Cuenta Financiera**
2. Navegue a la pestaña **Bank Connections**
3. Seleccione la(s) conexión(es) que desea desconectar
4. Haga clic en el botón **Disconnect Connection**

    !!!warning
        **Importante:**
        - Desconectar una conexión la elimina permanentemente tanto de Etendo como de Salt Edge
        - Vuelva a conectar si desea usar esta conexión bancaria de nuevo
        - Esta acción no se puede deshacer
        - Las transacciones pendientes no se ven afectadas, pero no se podrán importar nuevas transacciones desde esta conexión

5. Tras la desconexión, verifique la eliminación en la pestaña **Bank Connections**.

### Reconectar una conexión bancaria { #reconnecting-a-bank-connection }

Si una conexión aparece como **Inactivo** o **Deshabilitado**, selecciónela en la pestaña **Bank Connections** y haga clic en **Reconnect Connection**. Se abrirá un widget de Salt Edge — vuelva a autenticarse con su banco para restaurar la conexión a **Activo**.

![Botón Reconnect Connection en la pestaña Bank Connections](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/bank-integration/bank-integration-10.png)

!!!note
    Si la conexión ya está activa cuando hace clic en **Reconnect Connection**, recibirá un mensaje de confirmación y no será necesaria ninguna acción adicional. Si **Get Bank Statements** encuentra un problema de conexión, marca automáticamente esa conexión como **Deshabilitado** e intenta la siguiente disponible.

## Iniciación de pagos bancarios (PIS) { #bank-payment-initiation-pis }

Además de importar transacciones bancarias (AIS), este módulo permite **iniciar pagos bancarios directamente desde Etendo**. Cuando crea un registro de Pago en Etendo, puede enviarlo a su banco para su autorización y ejecución — sin salir del ERP.

### Cómo funcionan los pagos bancarios { #how-bank-payments-work }

El flujo de iniciación de pagos funciona de la siguiente manera:

1. Cree un registro de **Pago** en Etendo como de costumbre.
2. Desde el registro del pago, haga clic en el botón **Generate Bank Payment**.
3. Aparece un formulario con valores precargados (importe, acreedor, plantilla, etc.).
4. Tras revisar y confirmar, se abre un **popup de autorización bancaria**.
5. Autorice el pago en el entorno seguro de su banco.
6. El estado del pago se rastrea automáticamente en Etendo.

### Plantillas de pago { #payment-templates }

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
    
    Cambie la plantilla manualmente en el formulario si es necesario.

### Configuración requerida { #required-configuration }

Antes de generar pagos bancarios, asegúrese de que el método de pago asignado a la cuenta financiera está configurado correctamente.

:material-menu: `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Transacciones` > `Cuenta Financiera`

1. Abra la **Cuenta Financiera** vinculada a la conexión bancaria.
2. Vaya a la pestaña **Método de Pago**.
3. Seleccione el método de pago utilizado para transferencias bancarias.
4. En la sección **Pago**, asegúrese de que **Reintegro automático en cuenta** está **desactivado** (sin marcar).

![Método de pago — Reintegro automático en cuenta desactivado](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/bank-integration/bank-integration-11.png)

!!!warning
    Si **Reintegro automático en cuenta** está activado, el sistema procesa el reintegro automáticamente y el botón **Generate Bank Payment** no aparece en el registro de Pago. Desactive esta opción para permitir la iniciación manual de pagos bancarios a través de Salt Edge.

### Generar un pago bancario { #generating-a-bank-payment }

:material-menu: `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Pago`

1. Abra un registro existente de **Pago**.
2. Haga clic en el botón **Generate Bank Payment**.

    ![Botón Generate Bank Payment en la ventana Pago](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/bank-integration/bank-integration-12.png)

3. Aparece un **formulario de proceso** con los siguientes campos precargados:

    | Campo | Valor por defecto | Descripción |
    |---|---|---|
    | **Template** | Según la moneda | Plantilla de pago (SEPA, FPS o DOMESTIC) |
    | **End-to-End** | Número de documento | Referencia única del pago (máx. 35 caracteres) |
    | **Creditor Name** | Nombre del tercero | Nombre del beneficiario del pago |
    | **Amount** | Importe del pago | Importe a transferir |
    | **Currency** | Moneda del pago | Moneda de la transferencia |
    | **Description** | Descripción del pago | Descripción del pago |
    | **Creditor IBAN** | IBAN del tercero | Obligatorio para SEPA y opcional para DOMESTIC |
    | **Creditor Account Number** | Cuenta del tercero | Obligatorio para FPS, opcional para DOMESTIC |

    ![Formulario del proceso de pago bancario con campos precargados](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/bank-integration/bank-integration-13.png)

    !!!tip
        Los valores del formulario se calculan automáticamente a partir de los datos del Pago y del tercero. Asegúrese de que sus terceros tengan configurada su **información de cuenta bancaria** (IBAN o número de cuenta) para una mejor experiencia.

4. Revise los valores y haga clic en **Done** para iniciar el pago.

5. Se abre un **popup de autorización bancaria** donde debe autorizar el pago con su banco.

    ![Popup de autorización bancaria para la confirmación del pago](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/bank-integration/bank-integration-14.png)

    !!!warning
        No cierre el popup hasta haber completado el proceso de autorización con su banco. El pago no puede continuar sin su autorización.

6. Tras completar la autorización, verá una **página de confirmación** indicando que el pago ha sido registrado.

7. Cierre el popup y vuelva a Etendo. El estado del pago se actualizará automáticamente.

### Ciclo de vida del estado del pago { #payment-status-lifecycle }

Tras iniciar un pago bancario, pasa por varias etapas de estado:

| Estado | Descripción |
|---|---|
| **Requested** | El pago se ha creado en Etendo, pendiente de envío a Salt Edge |
| **Initiated** | La solicitud de pago se ha enviado a Salt Edge |
| **Authorizing** | El usuario está completando la autorización con el banco |
| **Authorized** | El usuario ha autorizado el pago en el banco |
| **Processing** | El banco está procesando el pago |
| **Executed** | El pago se ha completado correctamente ✅ |
| **Settled** | El pago ha sido liquidado por el banco ✅ |
| **Failed** | El pago ha fallado ❌ |

!!!note
    Una vez que un pago alcanza un **estado final** (Executed, Settled o Failed), no se puede modificar. Si un pago falla, cree un nuevo intento de pago desde el mismo registro de Pago.

### Ver pagos bancarios { #viewing-bank-payments }

Todos los pagos bancarios iniciados se registran en la pestaña **Bank Payments** del registro de Pago (:material-menu: `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Pago`). Los campos clave a monitorizar son **Status**, **Status Detail** (notas específicas del banco), **Amount** y **Creditor Name**. Use **Refresh Payment** para consultar el estado más reciente bajo demanda.

![Pestaña Bank Payments con los registros y estados de pago](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/bank-integration/bank-integration-15.png)

### Actualizar el estado del pago { #refreshing-payment-status }

El estado del pago se actualiza automáticamente mediante dos mecanismos:

#### Actualizaciones automáticas (Webhooks) { #automatic-updates-webhooks }

Salt Edge envía notificaciones automáticas de estado a Etendo cada vez que el estado del pago cambia en el banco. Estas actualizaciones se procesan inmediatamente y el registro del pago se actualiza en tiempo real.

!!!info
    Las actualizaciones por webhook se producen automáticamente — no se requiere ninguna acción del usuario. Cuando el banco procese su pago, el estado en Etendo se actualizará en cuestión de segundos.

#### Actualización manual { #manual-refresh }

Si desea consultar el estado más reciente inmediatamente:

1. Navegue a la pestaña **Bank Payments**.
2. Seleccione uno o varios registros de pago.
3. Haga clic en el botón **Refresh Payment**.

    ![Botón Refresh Payment en la pestaña Bank Payments](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/financial-extensions/bank-integration/bank-integration-16.png)

4. El sistema consultará a Salt Edge el estado actual y actualizará el registro.

!!!tip
    Use la actualización manual cuando desee verificar el estado actual de un pago sin esperar a la siguiente actualización automática.

#### Actualización automática programada { #scheduled-automatic-refresh }

El proceso **Refresh Pending Payments** se ejecuta cada **10 minutos** por defecto y actúa como red de seguridad ante cualquier notificación webhook perdida. Para ajustar la frecuencia, cree una nueva entrada de **Procesamiento de Peticiones** para este proceso y desactive la entrada importada por el sistema (:material-menu: `Configuración General` > `Planificador de procesos` > `Procesamiento de Peticiones`).

## Problemas comunes y soluciones { #common-issues-and-solutions }

**Conexión y clave API**

??? failure "No API Key Available"
    - Asegúrese de que su usuario tiene configurada la Salt Edge API Key.
    - Compruebe que la API Key es correcta y está activa.

??? failure "Invalid or expired API Key"
    - Su API Key ha caducado o ya no es válida.
    - Contacte con su administrador de Etendo o con el Soporte de Etendo para obtener una nueva API Key.
    - Actualice la API Key en la ventana Usuario (campo **PSD2 API Key**).

??? warning "Could not get redirect link"
    - El servicio de conexión bancaria puede estar temporalmente no disponible.
    - Inténtelo de nuevo en unos minutos. Contacte con soporte si el problema persiste.

??? warning "No new transactions found"
    - Revise la configuración de **Import From Date** / **Import To Date**.
    - Verifique que hay nuevas transacciones en su cuenta bancaria y que el rango de fechas cubre el periodo esperado.

??? warning "Rate limit or service temporarily unavailable"
    - El sistema ha superado el número permitido de solicitudes a la API, o Salt Edge está en mantenimiento.
    - Estos errores son transitorios — espere unos minutos e inténtelo de nuevo. Los procesos planificados reintentarán automáticamente.

??? failure "Connection Status shows Disabled"
    Una conexión puede aparecer como **Deshabilitado** debido a la caducidad de la autenticación, errores de comunicación con Salt Edge o indisponibilidad temporal del banco.

    1. Ejecute **Synchronize Bank Connections** (`Gestión Financiera` > `Gestión de Cobros y Pagos` > `Configuración` > `PSD2` > `Synchronize Bank Connections`) para verificar el estado de la conexión.
    2. Ejecute **Get Bank Statements** de nuevo para ver si el problema persiste.
    3. Si sigue apareciendo como **Deshabilitado**, haga clic en **Reconnect Connection** en la pestaña **Bank Connections** (consulte [Reconectar una conexión bancaria](#reconnecting-a-bank-connection)).

**Iniciación de pagos**

??? failure "Template Required / Creditor Name Required"
    - No se pudo determinar la plantilla de pago, o falta el nombre del tercero.
    - Asegúrese de que el pago tiene una moneda válida y un tercero con nombre válido asignado.

??? failure "IBAN Required for SEPA"
    - Los pagos SEPA requieren el IBAN del acreedor.
    - Configure la cuenta bancaria del tercero con un IBAN válido.

??? failure "SEPA Requires EUR / FPS Requires GBP / Sort Code or Account Number Required for FPS"
    - Los pagos SEPA solo usan EUR; FPS solo usa GBP y requiere tanto el código sort como el número de cuenta.
    - Compruebe la moneda del pago, cambie a la plantilla DOMESTIC si es necesario y verifique los datos de la cuenta bancaria del tercero.

??? warning "Payment status stuck in Initiated or Authorizing"
    - Es posible que el usuario no haya completado la autorización en el banco.
    - Haga clic en **Refresh Payment** para comprobar el estado más reciente. Si el problema persiste, revise el campo **Status Detail** para ver el mensaje de error específico del banco.

??? warning "Bank authorization popup was blocked / Payment Not Found after returning from bank"
    - Su navegador puede haber bloqueado la ventana emergente — permita popups para el sitio de Etendo e inténtelo de nuevo.
    - Si el redireccionamiento falló, revise la pestaña **Bank Payments**. El pago puede haberse procesado correctamente vía webhooks.

!!!tip "Obtener soporte"
    Antes de contactar con soporte, revise la ventana **PSD2 Logs** para obtener detalles del error, verifique su API Key e intente el botón **Reconnect Connection** para problemas de conexión. Al contactar con el Soporte de Etendo, incluya el mensaje de error, las entradas de log relevantes (incluyendo **JSON Info**), la cuenta financiera afectada y la fecha y hora del problema.

## Monitorización y logs { #monitoring-and-logs }

El módulo proporciona dos ventanas dedicadas para monitorizar la actividad de integración.

**PSD2 Logs**

:material-menu: `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Configuración` > `PSD2` > `PSD2 Logs`

Muestra toda la actividad y los logs de error generados por la integración. Cada entrada incluye:

| Campo | Descripción |
|-------|-------------|
| **Financial Account** | La cuenta financiera asociada al evento. |
| **Execution Day** | La fecha y hora en que ocurrió el evento. |
| **Status** | El resultado de la operación (*Success*, *Error*, etc.). |
| **Source** | El proceso que generó el log (p. ej., *Get Transactions*, *Generate Payment*). |
| **Log** | Una descripción legible del evento. |
| **JSON Info** | La respuesta técnica en bruto de la API, útil para diagnóstico y soporte. |

!!!tip
    Filtre por **Financial Account** y ordene por **Execution Day** descendente para encontrar rápidamente los eventos más recientes.

**Bank Provider**

:material-menu: `Gestión Financiera` > `Gestión de Cobros y Pagos` > `Configuración` > `PSD2` > `Bank Provider`

Lista todos los bancos disponibles a través de Salt Edge. Cada entrada muestra el **Provider Code** y el **Provider Name**. Ejecute **Synchronize Bank Providers** periódicamente (p. ej., semanalmente) para mantener esta lista actualizada.

## Buenas prácticas { #best-practices }

- **Deje Import From Date vacío** tras la importación inicial — el sistema continúa automáticamente desde la última fecha importada.
- **Revise Status Detail** cuando un pago bancario falla — contiene el mensaje de error específico del banco antes de reintentar.
- **Desconecte las conexiones bancarias no utilizadas** — las conexiones eliminadas aquí se borran permanentemente tanto de Etendo como de Salt Edge.

## Recursos adicionales { #additional-resources }

- [Documentación de Salt Edge](https://docs.saltedge.com/){target="_blank"}
- [Notas de la versión del Financial Extensions Bundle](../../../../../whats-new/release-notes/etendo-classic/bundles/financial-extensions/release-notes.md)
- [Guía de conciliación bancaria](../basic-features/financial-management/receivables-and-payables/transactions/financial-account.md#reconciliations)

*[AIS]: Servicio de Información de Cuentas
*[PIS]: Servicio de Iniciación de Pagos
*[SEPA]: Zona Única de Pagos en Euros
*[FPS]: Faster Payments Service (Reino Unido)
*[IBAN]: Número de Cuenta Bancaria Internacional
*[PSD2]: Directiva de Servicios de Pago 2
*[BBAN]: Número de Cuenta Bancaria Básico

---

This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.
