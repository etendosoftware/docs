---
title: Abrir/Cerrar periodos
tags:
    - Abrir
    - Cerrar
    - Periodo
    - Control
    - Gestión Financiera
    - Configuración
    - Contabilidad
---

# Abrir/Cerrar periodos

:material-menu: `Aplicación` > `Gestión Financiera` > `Contabilidad` > `Configuración` > `Abrir/Cerrar periodos`

## Visión general

La funcionalidad **Abrir/Cerrar periodos** permite al usuario gestionar qué periodos contables están abiertos o cerrados para una determinada organización.

Antes de utilizar esta ventana, asegúrese de que:

- [x] Su organización tiene definido un **[Calendario fiscal](#calendario-fiscal)**.
- [x] El calendario fiscal contiene **Ejercicio** y **Periodo** (normalmente mensuales).
- [x] El tipo de la organización es **Legal con contabilidad** y tiene habilitado **[Permitir Control de Periodos](../../../general-setup/enterprise-model/organization.md#organization-1)**.

Así es como funciona el proceso en Etendo:

1. **Crear ejercicios y periodos** en la ventana **[Calendario fiscal](#calendario-fiscal)**.
2. **Abrir todos los periodos** (incluido el "Periodo 13" para ajustes) en la ventana Abrir/Cerrar periodos.
3. **Cerrar los periodos estándar** (excepto el Periodo 13) una vez que todas las transacciones de esos periodos estén contabilizadas.

    !!!note
        Se recomienda cerrar los periodos estándar antes de ejecutar el proceso [Crear asiento de regularización](../../accounting/transactions.md#end-year-close) para una mejor supervisión, pero no es obligatorio.

4. **Contabilizar cualquier ajuste final** en el Periodo 13 utilizando diarios de mayor (G/L).
5. **Ejecutar el proceso [Crear asiento de regularización](../../accounting/transactions.md#end-year-close)** en la ventana de cierre de fin de ejercicio. Esto crea los asientos de cierre y cierra permanentemente todos los periodos del ejercicio.  

    !!!warning
        Los periodos cerrados permanentemente no se pueden reabrir a menos que primero ejecute Borrar asiento de regularización.

6. Si es necesario, **ejecute [Borrar asiento de regularización](../../accounting/transactions.md#undo-close-year)** para reabrir periodos y permitir más cambios. Después de realizar los cambios, puede ejecutar de nuevo Crear asiento de regularización.

!!!important
    - No puede crear ejercicios ni periodos en la ventana Abrir/Cerrar periodos; para ello utilice la ventana Calendario fiscal.
    - No puede generar asientos de cierre aquí; utilice la ventana de cierre de fin de ejercicio.
    - También puede comprobar el estado de cualquier periodo en la pestaña [Control de Periodos](../../../general-setup/enterprise-model/organization.md#period-control) de la Organización.

### ¿Por qué utilizar esta funcionalidad?

El control de periodos ayuda al usuario a:

- Realizar el seguimiento de la actividad financiera controlando qué periodos están abiertos para contabilizar.
- Evitar cambios no deseados en periodos cerrados.
- Gestionar los asientos de cierre durante los procesos de fin de ejercicio.

## Control de Periodos

La ventana **Abrir/Cerrar periodos** permite al usuario revisar y gestionar todos los periodos contables creados en el **[Calendario fiscal](#calendario-fiscal)**. Puede **abrir**, **cerrar** o **cerrar permanentemente** periodos según sea necesario para su organización.

![Ventana Abrir/Cerrar periodos](../../../../../../assets/drive/1wWBwXFdqFKBcXY9i19M7U8nE0jiUYMJt.png)

**Campos a tener en cuenta:**

- **Estado:** Se muestra en dos columnas: una con un código de color y otra con el nombre del estado. Los estados incluyen:
    - *Todos nunca abiertos* (gris): periodos recién creados.
    - *Todos abiertos* (verde): todos los tipos de documento están abiertos.
    - *Todos cerrados* (rojo): todos los tipos de documento están cerrados.
    - *Mixto* (naranja): algunos tipos de documento están abiertos y otros están cerrados.
    - *Todos cerrados permanentemente* (rojo): todos los tipos de documento están cerrados permanentemente.
- **Calendario:** Muestra el calendario de la organización (solo lectura).
- **Organización**
- **Ejercicio**
- **Nº de periodo**
- **Nombre:** Nombre del periodo.
- **Fecha de inicio:** Cuándo comienza el periodo.
- **Fecha final:** Cuándo termina el periodo.

Puede utilizar estos campos para filtrar y encontrar los periodos que necesita. Por ejemplo, filtre por calendario, organización y ejercicio para ver todos los periodos de un ejercicio específico.

**Filtros por defecto:** 

Por defecto, esta ventana solo muestra periodos que:

- **No** están cerrados.
- Pertenecen a la organización con la que ha iniciado sesión.

    !!!info
        Recuerde que puede eliminar estos filtros haciendo clic en el icono del embudo.

**Botones disponibles:**

- **Abrir periodo:** Permite contabilizar en el/los periodo(s).
- **Cerrar periodo:** Bloquea la contabilización en el/los periodo(s). Puede reabrir un periodo cerrado si es necesario.

    !!!info
        Es posible seleccionar varios registros para abrir o cerrar periodos de forma masiva.

    !!!important 
        - Solo se pueden abrir o cerrar periodos de organizaciones de tipo "Legal con contabilidad" con "Permitir Control de Periodos" habilitado. 
        - Si un periodo está abierto para todos los tipos de documento excepto uno (por ejemplo, factura de proveedor), puede contabilizar todas las transacciones excepto las de ese tipo de documento en ese periodo.

### Ejemplo de Control de Periodos

A continuación se muestra un ejemplo sencillo de cómo funciona el control de periodos:

Una organización ha creado y abierto todos los periodos de tres ejercicios, incluido el "Periodo 13" para ajustes.

![](../../../../../../assets/drive/1dOWq4RquxSziuUbqVYpORdf9eA4Ts7g5.png)

Con la configuración mostrada arriba, puede contabilizar cualquier documento en cualquier periodo dentro de esos ejercicios. Si intenta contabilizar en un periodo que no existe (como diciembre de 2018, en este ejemplo), Etendo mostrará un error.

Imagine que quiere cerrar el ejercicio 2019. Antes de ejecutar el proceso "Crear asiento de regularización", debería cerrar todos los periodos estándar de 2019 (excepto el Periodo 13) para evitar contabilizaciones adicionales. Así es como hacerlo:

1. Vaya a la ventana **Abrir/Cerrar periodos**.
2. Filtre por Calendario, Organización y Ejercicio (por ejemplo, 2019) para mostrar los periodos correspondientes.
3. Debería ver los 13 periodos del ejercicio.
4. Seleccione todos los periodos excepto el Periodo 13.
5. Haga clic en **Cerrar periodo** y confirme.

![](../../../../../../assets/drive/1AxEefqisj3SW_FqBBXGfF6Th0rWpaJrn.png)

Después de esto, todos los periodos estándar de 2019 quedan cerrados. Solo puede:

- Contabilizar diarios de mayor (G/L) en el Periodo 13.
- Contabilizar los asientos de cierre creados por el proceso Crear asiento de regularización.

!!!important
    Si necesita realizar cambios en un periodo cerrado, debe reabrirlo, lo cual solo es posible si el ejercicio no está cerrado permanentemente; de lo contrario, ejecute primero Borrar asiento de regularización.

## Pestaña Documentos

Cada periodo contable en Etendo puede abrirse o cerrarse para todos los tipos de documento a la vez, o para tipos de documento específicos.

- Cuando abre un periodo, se abren todos los tipos de documento de ese periodo, por lo que puede contabilizar cualquier tipo de transacción.
- También puede abrir o cerrar tipos de documento individuales (como factura de proveedor o diario de mayor (G/L)) dentro de un periodo.

Esto es útil en caso de que el usuario necesite evitar la creación de más documentos de un determinado tipo para un periodo específico.

![](../../../../../../assets/drive/18LHnWB8IGtMlKvBlGEkFcvMl4MtUzfWD.png)

**Columnas de estado:**  
Cada tipo de documento muestra su estado con un color y un nombre:

- **Nunca abierto** (gris): aún no se ha abierto.
- **Abierto** (verde): se permite contabilizar.
- **Cerrado** (rojo): la contabilización está bloqueada.
- **Cerrado permanentemente** (rojo): bloqueado; solo se puede reabrir deshaciendo el cierre del ejercicio.

!!!important
    - El Periodo 13 solo permite asientos de diario de mayor (G/L).
    - Si un periodo está abierto para todos los tipos de documento excepto uno (por ejemplo, factura de proveedor), puede contabilizar todas las transacciones excepto las de ese tipo.

**Cómo abrir o cerrar un tipo de documento en un periodo:**

1. Seleccione un periodo en la pestaña Periodo.
2. Vaya a la pestaña Documentos para ver todos los tipos de documento de ese periodo.
3. Utilice filtros para encontrar los tipos de documento que desea.
4. Seleccione los tipos de documento.
5. Haga clic en **Abrir/Cerrar periodo**, elija la acción y haga clic en OK.

Etendo confirmará cuando el proceso se haya completado.

---

Este trabajo es una obra derivada de [Abrir/Cerrar periodos](https://wiki.openbravo.com/wiki/Open/Close_Period_Control){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.