---
tags:
  - How to
  - New UI
  - JavaScript Migration
  - Process Definition

status: new
---

# How to Migrate Classic Process JavaScript to the New UI

## Overview

In **Etendo Classic**, a *Defined Process* (a process configured in the Application Dictionary, with or
without parameters) can carry hand-written JavaScript that customizes its dialog: pre-filling fields
when it opens, validating and transforming input as the user types, gating execution behind a
confirmation, showing in-dialog banners, launching nested processes, or post-processing the server
response. In Classic this JavaScript runs inside the SmartClient runtime.

The **new Workspace UI** reproduces that behavior **without SmartClient**. The custom JavaScript is no
longer attached to a SmartClient module; instead it is stored as plain text in a set of metadata
columns on the process and its parameters. At runtime the new UI compiles that text and runs it against
a curated context that emulates the Classic APIs the scripts expect. This makes the capability
**fully metadata-driven**: any process becomes scriptable simply by filling in its columns — no new code
is deployed to the UI.

This guide explains **how to migrate the JavaScript of a Defined Process** from Classic to the new UI in
your own environment. If you maintain a productive instance with custom Defined Processes whose Classic
JavaScript personalizes their behavior, those scripts will **not** run in the new UI until they are
migrated into the metadata columns. This document is your reference for doing that.

!!! info "Who this guide is for, and what your role is"
    This guide is written for developers who must migrate Classic process JavaScript **without access to
    the new UI source code**. Your tools are **this documentation**, the **architecture
    reference** it points to, and the **"New UI Migrations" Team**. Concretely, your job is to:

    1. Produce the migrated code (manually, or with the **"New UI Migrations" Team** — see
       [Migrating with the "New UI Migrations" Team](#migrating-with-the-new-ui-migrations-team)).
    2. Paste it into the correct metadata fields (see [The metadata fields](#the-metadata-fields-where-the-migrated-code-goes)).
    3. **Validate the result manually** in the running dialog.
    4. If something does not work, **report the problem** — describe exactly what fails and where.

!!! warning "Automation is assisted, not autonomous"
    The **"New UI Migrations" Team** accelerates migration, but it **can make mistakes**. Every migration it produces
    **must be validated manually** by a developer before it is considered done. Treat the team's output
    as a first draft to verify, never as a finished, trusted result.

---

## Background: the five Classic hook points

A Classic Defined Process can attach behavior at up to five points. The new UI maps each one to a
metadata column:

| # | Classic hook | Fires when… | Scope |
|---|---|---|---|
| 1 | `onLoad` | The process dialog opens | Process(`OBUIAPP_Process`) |
| 2 | `onProcess` | The user presses the execute / OK button | Process(`OBUIAPP_Process`) |
| 3 | `onRefresh` | The dialog needs to re-pull its data (e.g. after a nested process closes) | Process(`OBUIAPP_Process`) |
| 4 | `onChange` | A parameter's value is committed | Parameter(`OBUIAPP_Parameter`) |
| 5 | `onGridLoad` | An embedded grid parameter finishes loading rows | Parameter(`OBUIAPP_Parameter`) |

Beyond these entry points, a Classic process file is a single JavaScript *module*: the entry points call
shared helpers, constants, and closure state declared in the same file. The new UI reproduces this with
a dedicated **module-scope** column (see [`em_etmeta_payscript_logic`](#4-em_etmeta_payscript_logic-shared-module-scope)).

The **goal of migration is behavioral parity**: a migrated process must behave the same as its Classic
counterpart, with the JavaScript living in metadata instead of in a SmartClient module.

---

## What the new UI can do

This section describes the capabilities available to migrated scripts — the **what**, the **why**, and
**how you use them** — without going into how they are implemented internally. If a script touches
something the new UI does not implement, it throws a clear `"<api> is not implemented yet"` error rather
than failing silently, so gaps surface during migration instead of in production.

### The execution-model contract you must respect

A few rules govern every field. They are not optional — a body that breaks them will not run:

- **Each hook is a bare arrow-function expression.** A field value must be a single arrow function such
  as `async (process, view) => { … }`. It must **not** be wrapped in an immediately-invoked function
  expression (IIFE, e.g. `(async () => { … })()`) and must **not** be an object literal. Anything that does not evaluate to a
  function is rejected at compile time.
- **`onLoad` / `onProcess` / `onChange` / `onGridLoad` are arrow functions; module scope is different.**
  The module-scope field (`em_etmeta_payscript_logic`) is a *module body* — a sequence of declarations
  ending in `return { … };` — not an arrow function. See its field description below.
- **Helpers resolve by bare name.** Anything returned from the module-scope field is available, by its
  bare name, inside all five hooks. Globals such as `OB`, `callAction`, `confirm`, `messageBar`, and
  `BigDecimal` are likewise injected and callable directly.
- **`onChange` does not fire during initial seeding.** Just like Classic, parameter `onChange` runs only
  on a genuine user change, never while the dialog seeds its initial/default values. Put load-time
  computation in `em_etmeta_onload`, not in `on_parameter_change`.

### Capability catalog

| Capability | What it gives migrated scripts |
|---|---|
| **The `view` object** | Mirrors the Classic `OBStandardView`. Read-only context (`view.theForm`, `view.messageBar`, `view.getContextInfo()`, `view.selectedRecords`, `view.tabId`, …) is always available; action methods (`view.refresh()`, `view.openProcess(...)`, `view.executeProcess()`, the footer buttons, the OK button) are available inside the hooks that need them. |
| **`form`, `item` proxies** | `view.theForm.getItem(name)` and field methods: `getValue()` / `setValue(v)`, `show()` / `hide()` / `isVisible()`, `setRequired(bool)` / `setDisabled(bool)`, `setTitle(text)`, `setValueMap(map)` / `getValueMap()`, `setValueFromRecord({ id, _identifier })`, and more. Numeric parameters return real `number`s, so Classic comparisons keep working. |
| **`grid` proxy** | For embedded (Window-Reference / Pick&Execute) grids: selection (`getSelectedRecords`, `selectRecord`, …), row reads, edit values (`setEditValue`, `getEditValues`), visibility (`show()` / `hide()`), per-row action buttons, and runtime hooks registered from `onGridLoad` (`onRecordChange`, `onSelectionToggle`, `setColumnOnChange`, `setColumnValidator`, `fireOnPause`). |
| **Server execution — `view.executeProcess()`** | The new-UI equivalent of the Classic `actionHandlerCall()`. It builds the standard execution payload and submits it to the process's configured Java class. Use it in `onProcess` instead of hand-building a payload. |
| **HTTP helpers** | `callAction(handler, payload)`, `callDatasource(entity, payload)`, `callServlet(path, payload)` — POST to backend handlers/datasources with auth and CSRF handled automatically. |
| **Modal dialogs** | `confirm` / `warn` / `say` (and `isc.confirm` / `ask` / `warn` / `say`). Promise-based and also accept the Classic callback shape. |
| **In-dialog message bar** | `view.messageBar.setMessage(severity, title, text, actions?)` and `view.messageBar.hide()`, with `OB.MessageBar.TYPE_*` / `isc.OBMessageBar.TYPE_*` severities. Clickable links must be expressed as a structured `actions` array, not as inline `<a onclick>` HTML. |
| **Nested processes** | `view.openProcess(params)` (and `view.standardWindow.openProcess(...)`) layers another process dialog on top; the parent's `onRefresh` fires when the child closes. |
| **The `OB.*` shim** | A shared `OB` namespace mirroring the Classic globals: `OB.I18N.getLabel`, `OB.Format.*`, `OB.Utilities.Number.JSToOBMasked`, `OB.Utilities.Action.set/execute/executeJSON`, `OB.PropertyStore`, `OB.RemoteCallManager.call` (callback↔Promise adapter), `OB.Datasource.create`, `OB.Constants`, severity constants. |
| **Decimal arithmetic — `BigDecimal`** | The Classic `BigDecimal` is injected as a global, so money math (`add`, `subtract`, `multiply`, `divide`, `compareTo`, `setScale`, …) is migrated verbatim. **Never** rewrite money math with `Number` / `parseFloat`, which drifts and breaks parity with the server. |
| **Action-JSON dispatcher** | `OB.Utilities.Action.executeJSON(actions)` dispatches a backend `responseActions` array (message bar, toast, navigate to tab, refresh grid, download/browse report, …). |
| **Custom UI component** | When the process's custom-component flag is set, `onLoad` returns a UI *schema* and the dialog renders a bespoke component instead of the standard parameter form. |

### What is not (yet) supported

The new UI is generic and metadata-driven, with **no per-process special-casing**. A handful of Classic
mechanisms are either intentionally changed or not supported:

- **Inline-onclick HTML in messages** is not allowed. Message text is sanitized (formatting tags only);
  use the structured `actions` array for clickable affordances.
- **SmartClient UI primitives** (`isc.ClassFactory.defineClass`, `isc.DynamicForm`, `isc.OBPopup`, …)
  are not available. Their equivalents are the declarative `grid.setRowActions(...)` and
  `openDynamicForm({ fields })`.
- **Anything the platform does not implement** throws `"<api> is not implemented yet"`. If you hit such
  an error during validation, that is a capability gap to **report** (see
  [Reporting issues](#reporting-issues)) — not something to work around in your environment.

---

## The metadata fields (where the migrated code goes)

Seven custom columns carry the migrated code. Four belong to the **process**, two to each **parameter**,
and one is a rendering flag on the process. You enter the migrated JavaScript in the field corresponding
to each column on the **Process Definition** window (and its **Parameters** tab) in the Application
Dictionary.

| Field (column) | Entity | Hook | Code shape |
|---|---|---|---|
| `em_etmeta_onload` | Process | `onLoad` | `async (process, view) => { … }` |
| `em_etmeta_onprocess` | Process | `onProcess` | `async (process, view) => { … }` |
| `em_etmeta_on_refresh` | Process | `onRefresh` | `(view) => { … }` |
| `em_etmeta_payscript_logic` | Process | shared module scope | module body ending in `return { … };` |
| `em_etmeta_on_parameter_change` | Parameter | `onChange` | `(item, view, form, grid) => { … }` |
| `em_etmeta_on_grid_load` | Parameter | `onGridLoad` | `(grid, view, parameters) => { … }` |
| `em_etmeta_custom_component` | Process | rendering flag | boolean (Yes/No) |

!!! tip "Any field may be left empty"
    A process rarely uses all five hooks. Fill only the fields that correspond to hooks the Classic file
    actually implements; leave the rest empty. An empty field simply means "no script for this hook".

Below is the purpose, signature, and a simple example for each field.

### 1. `em_etmeta_onload` — process `onLoad`

- **Entity:** process · **Signature:** `async (process, view) => { … }`
- **Fires:** once, when the dialog opens, after the defaults have been seeded and before the form is
  interactive.
- **Purpose:** seed or compute default values, hide or require fields, pre-select grid rows, gate the
  open behind a `confirm`, or (with the custom-component flag) return a UI schema.
- **Returns (optional):** a map of `paramName: value` pairs to seed fields; a falsy return is a no-op.

```js
async (process, view) => {
  const form = view.theForm;
  // Hide an advanced field unless the launching record is a sales transaction.
  const ctx = view.getContextInfo();
  if (ctx.inpissotrx !== 'Y') {
    form.getItem('credit_to_use').hide();
  }
  // Seed a sensible default and make a field mandatory.
  form.getItem('payment_date').setValue(ctx.inpdateordered);
  form.getItem('reference_no').setRequired(true);
};
```

### 2. `em_etmeta_onprocess` — process `onProcess`

- **Entity:** process · **Signature:** `async (process, view) => { … }`
- **Fires:** when the user presses the execute / OK button.
- **Purpose:** client-side validation before submit, calling the backend, and post-processing the
  response.
- **Key rule:** call `view.executeProcess()` to run the process's own Java class (the equivalent of the
  Classic `actionHandlerCall()`). To abort with an error, return `{ severity: 'error', text }`.

```js
async (process, view) => {
  const form = view.theForm;
  const amount = form.getItem('actual_payment').getValue(); // numeric → a real number
  if (amount <= 0) {
    const text = OB.I18N.getLabel('ETP_AmountMustBePositive');
    view.messageBar.setMessage(isc.OBMessageBar.TYPE_ERROR, null, text);
    return { severity: 'error', text }; // aborts; the modal stays open
  }
  const response = await view.executeProcess(); // = actionHandlerCall()
  return response && response.message;
};
```

!!! note "Pick&Execute / Window-Reference processes behave differently"
    For a process whose pattern is Pick&Execute, or that has a Window-Reference grid parameter, the
    platform submits the grid selection itself. There, `onProcess` runs as a **pre-submit validation
    hook**: return `{ severity: 'error', text }` to abort, or `undefined` to let the submit proceed —
    and do **not** call `view.executeProcess()` (it would double-submit).

### 3. `em_etmeta_on_refresh` — process `onRefresh`

- **Entity:** process · **Signature:** `(view) => { … }`
- **Fires:** when the dialog needs to re-pull its data — for example, when a nested process closes, the
  parent's `onRefresh` is invoked automatically.
- **Purpose:** refresh grid/form data after an external change.

```js
(view) => {
  // Re-pull the embedded grid after a nested process modified the data.
  view.theForm.getItem('order_invoice').canvas.viewGrid.invalidateCache();
};
```

### 4. `em_etmeta_payscript_logic` — shared module scope

- **Entity:** process · **Shape:** a **module body** (declarations and helper functions) that ends with
  `return { … };` — **not** an arrow function.
- **Purpose:** hold everything the Classic file declared at module level — shared helpers, constants, and
  closure state — that the entry points reference by bare name. It is evaluated once per dialog open, and
  whatever it returns is made available inside all five hooks.

```js
const PAID_FULLY = 'PPM';

function remaining(form) {
  const total = new BigDecimal(String(form.getItem('total').getValue()));
  const paid = new BigDecimal(String(form.getItem('actual_payment').getValue()));
  return total.subtract(paid);
}

return { PAID_FULLY, remaining };
```

!!! tip "Namespaced self-registration"
    If the Classic file registers a namespace such as `OB.APRM.AddPayment = { … }`, you can do the same
    inside this module body; the `OB` shim tolerates `OB.<Module>.<Process>` writes.

### 5. `em_etmeta_on_parameter_change` — parameter `onChange`

- **Entity:** parameter (one per parameter that has an onChange) · **Signature:**
  `(item, view, form, grid) => { … }` — `item` is the changed field; `grid` is `null` for scalar
  parameters.
- **Fires:** when the parameter's value is committed by the user (never during initial seeding).
- **Purpose:** react to a value change — recompute dependent fields, toggle required/disabled, refresh a
  value map, show a banner.

```js
(item, view, form) => {
  // When the document type changes, recompute the suggested amount.
  const isCredit = item.getValue() === 'CR';
  form.getItem('credit_amount').setDisabled(!isCredit);
  if (!isCredit) {
    form.getItem('credit_amount').setValue(0);
  }
};
```

### 6. `em_etmeta_on_grid_load` — parameter `onGridLoad`

- **Entity:** parameter (the grid parameter) · **Signature:** `(grid, view, parameters) => { … }`
- **Fires:** each time the embedded grid receives a delivered datasource result (including an **empty**
  result, exactly once).
- **Purpose:** post-process loaded rows (default selection, per-row components, derived columns), register
  per-column edit hooks/validators, or react to an empty grid (e.g. an info banner when no rows match).

```js
(grid, view) => {
  if (grid.getData().getLength() === 0) {
    view.messageBar.setMessage(isc.OBMessageBar.TYPE_INFO, null,
      OB.I18N.getLabel('ETP_NoOutstandingDocuments'));
    return;
  }
  // Recompute a total whenever an editable amount cell changes.
  grid.onRecordChange((record, changes) => {
    // …re-sum settlement amounts over the selected rows…
  });
};
```

### 7. `em_etmeta_custom_component` — custom-component flag

- **Entity:** process · **Type:** boolean (Yes/No).
- **Purpose:** it selects *how the process dialog is rendered*:
    - **`No` (false) — the normal case.** The dialog renders the **standard metadata-driven form**: the
      process's parameters, their metadata, and the migrated JavaScript hooks (`onLoad`, `onProcess`,
      `onChange`, …) described in this guide. This is what you use for virtually every migration.
    - **`Yes` (true) — a bespoke UI.** The dialog does **not** render the standard parameter form.
      Instead, the new UI must contain a **dedicated custom component built specifically for that
      process**, and `onLoad` returns the schema that drives it. This mirrors Classic, where such a
      process also has its own hand-built UI rather than a generic parameter dialog. It is reserved for
      the rare process whose dialog is not a flat list of fields (e.g. a specialized picker).

!!! warning "A custom component cannot be produced from metadata alone"
    Setting this flag to `Yes` is **not** a migration you can complete by filling in fields. A custom
    component is real code that must be added to the new UI for that specific process — and you do
    **not** have access to the new UI source code. If a process genuinely needs a custom component,
    **contact the platform team** to have it built. For all other processes, leave this flag as `No`
    and migrate using the standard fields above.

---

## Migrating with the "New UI Migrations" Team

For most processes you do not have to write the migration by hand. The **"New UI Migrations" Team**
provided by Fyso translates a Classic Defined-Process JavaScript file into the metadata columns described
above, using its internal migration agent. You interact with it **in Spanish** (the activation message
and its deliverables are in Spanish), as shown in the steps below.

!!! note "Migrating by hand"
    Steps 4 to 6 apply to you too: substitute your own migrated bodies for the team's labeled code blocks,
    and derive your own manual test plan in place of the team's checklist.

### What the team does — and does not do

**The team does:** read the Classic `.js` file and the process metadata; check feasibility against the
architecture document; generate the migrated code for each column as a bare arrow function; self-check
that each body compiles; and hand you a per-column output ready to paste, along with a manual-test
checklist.

**The team never:** paste the code into the UI for you (you do that); change application source code; commit
or push anything; or invent platform support that does not exist. If a process uses something the new UI
cannot do, the team **stops and reports the gap** instead of producing code that looks migrated but breaks.

!!! warning "You must still validate"
    The team's output is a **draft to verify**, not a finished result. It can misread an edge case or a
    Classic idiom. Always run the manual checklist before considering the migration done, and
    [report](#reporting-issues) anything that fails.

### Step 1 — Identify the inputs

You need two things:

1. **The path to the Classic `.js` file** of the Defined Process (the file that holds its custom
   JavaScript).
2. **The process id** — the 32-character `obuiapp_process_id` of the Defined Process. You can read it
   from the Process Definition window's record, or from the URL/help of that record.

### Step 2 — Engage the team

The team's migration agent only acts when your message matches its activation template **exactly** (the
quotes may be single or double). Send it, in Spanish, the file path and the process id:

```text
Quiero migrar el javascript del proceso definido. El path del archivo original es '<path>' y el id del proceso es '<process-id>'.
```

For example:

```text
Quiero migrar el javascript del proceso definido. El path del archivo original es 'modules/com.example.payments/web/js/ob-myprocess.js' y el id del proceso es '9BED7889E1034FE68BD85D5D16857320'.
```

If the message does not match the template, the team will not act — it will simply restate the template you
must use.

### Step 3 — Review the team's output

The team returns, in Spanish for the deliverables:

- A **coverage report**: a table classifying every Classic API the file uses as *supported*,
  *best-effort*, or *unsupported*. **If anything is unsupported, the team stops here** and explains exactly
  what the new UI lacks — that is a gap to report, not to work around.
- The **migrated code per column**, each in its own code block, clearly labeled with the column it goes
  into. Columns with no code are marked **"LEAVE EMPTY"**.
- A list of **advisories** (dead code dropped, cloning notes, semantic differences).
- A **manual-test checklist** — the concrete steps you must run to confirm parity.

Read the coverage report and advisories before pasting anything. They tell you what to expect and what to
test.

### Step 4 — Paste the code into the fields

For each labeled block, copy the body into the matching field on the Process Definition window (or its
Parameters tab), following [The metadata fields](#the-metadata-fields-where-the-migrated-code-goes).
Paste **only** the code the team delivered, exactly as given, into the indicated column. Save the record.

!!! danger "Match the field to the column"
    Pasting an `onProcess` body into the `onLoad` field (or a parameter hook into the wrong parameter)
    will produce wrong behavior that is hard to diagnose. Double-check each block's label against the
    field you are editing.

### Step 5 — Validate manually

Open the process dialog in the new UI and run **every** item in the team's manual-test checklist: confirm
the dialog opens correctly, that `onLoad` seeding/hiding happened, that each `onChange` reacts as in
Classic, that grids load and validate as expected, and that execution returns the same result as Classic.
Compare side-by-side with the Classic dialog where possible.

### Step 6 — Report problems (do not fix)

If a test fails — a hook does not fire, a value is wrong, or you see a `"… is not implemented yet"`
error — **report it**. Describe the symptom precisely (which process, which hook, what you did, what you
expected, what happened) and include any error text. If you engaged the **"New UI Migrations" Team**, you can also tell it
`"el test X falló: <síntoma>"` and it will re-analyze and re-emit the corrected field(s) for that
process.

Do **not** attempt to patch the new UI in your environment. Capability gaps and substrate bugs are
resolved by the platform team; your contribution is a clear, reproducible report.

---

## Reporting issues

Because you do not have access to the new UI source code, a good report is the most valuable thing you
can produce when a migration does not behave like Classic. Include:

- **The process** — name and `obuiapp_process_id`.
- **The hook / field** involved (`onLoad`, `onProcess`, a specific parameter's `onChange`, etc.).
- **Steps to reproduce** — exactly what you did in the dialog.
- **Expected vs actual** — what Classic does vs what the new UI does.
- **Any error text** shown in the dialog or the browser console (especially
  `"<api> is not implemented yet"`, which names the missing capability).
- **The relevant migrated body** you pasted, and the coverage report if you engaged the **"New UI Migrations" Team**.

---

## Reference

- **Architecture & capability reference (source of truth):**
  [new-javascript-code.md](https://github.com/etendosoftware/com.etendorx.workspace-ui/blob/main/docs/process/definition/new-javascript-code.md)
  — the authoritative description of every supported API, signature, and migration rule.
- **The "New UI Migrations" Team:** see the [full list of available agents](https://fyso.world/app/teams/),
  including the migration agent used to translate Classic process JavaScript.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.
