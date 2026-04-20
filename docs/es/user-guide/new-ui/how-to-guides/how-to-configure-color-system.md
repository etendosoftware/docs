---
tags:
  - How to
  - Color System
  - UI

status: new
---

# Cómo Usar el Sistema de Colores en Workspace UI

## Visión General

El sistema de colores permite asignar una pastilla de color visual a los registros en una ventana maestra. Una vez asignado un color, cada grilla en Workspace UI que referencie esa ventana mostrará automáticamente una etiqueta coloreada en lugar de texto plano, facilitando el escaneo e identificación de registros de un vistazo.

![Visión general de pastillas de color en una grilla](../../../assets/user-guide/newui/how-to-guides/color-system/overview-color-badges-grid.png)

!!! info "Prerequisite"
    Un desarrollador debe configurar primero la columna **Color** en el diccionario de datos para la ventana maestra. Si el campo de color no es visible en el formulario, contacta con tu administrador del sistema o sigue la [developer guide](../../../developer-guide/etendo-classic/how-to-guides/how-to-configure-color-system.md).

---

## Step 1 — Open the Master Record

1. Inicia sesión en **Etendo Classic** con un rol que tenga acceso a la ventana maestra.
2. Navega a la ventana maestra configurada con una columna de color.
3. Abre un registro existente o crea uno nuevo.

---

## Step 2 — Assign a Color

1. Localiza el campo **Color** en el formulario. Acepta un código de color hexadecimal (por ejemplo, `#8E44AD`).
2. Introduce directamente el valor hexadecimal deseado o utiliza el selector de color si está disponible.
3. Haz clic en **Save**.

![Campo Color en el formulario con un valor hexadecimal introducido](../../../assets/user-guide/newui/how-to-guides/color-system/step2-color-field-form.png)

!!! tip
    La UI calcula automáticamente un color de texto con contraste, pero elegir un color de rango medio (ni demasiado claro ni demasiado oscuro) ofrece el mejor resultado visual.

---

## Step 3 — Verify the Color Badge in Workspace UI

1. Abre **Workspace UI** (el frontend de Next.js).
2. Navega a la ventana que contiene una columna de clave foránea que referencia la ventana maestra.
3. En la grilla, localiza la columna que apunta a la ventana maestra.

El valor ahora aparece como una **pastilla de color** en lugar de texto plano, reflejando el color hexadecimal que asignaste.

![Grilla mostrando una pastilla de color en la columna referenciada](../../../assets/user-guide/newui/how-to-guides/color-system/step3-colored-badge-grid.png)

---

## Changing or Removing a Color

- Para **change** el color: abre el registro maestro, introduce un nuevo valor hexadecimal y guarda.
- Para **remove** el color: limpia el campo de color y guarda. La columna volverá a mostrarse como texto plano en todas las grillas.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.