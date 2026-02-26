---
title: Convenciones de codificación de JavaScript
tags:
    - JavaScript
    - Codificación
    - Convenciones

status: beta
---

#  Convenciones de codificación de JavaScript
  
!!! example  "IMPORTANTE: ESTA ES UNA VERSIÓN BETA"
    Esta página está en desarrollo activo y puede contener **funcionalidades inestables o incompletas**. Úsela **bajo su propia responsabilidad**.

##  Visión general

Este documento se basa en la Guía de estilo de JavaScript de Google y en [Convenciones de código para el lenguaje de programación JavaScript](https://www.crockford.com/code.html){target="\_blank"} de Douglas Crockford.

##  Linting y formato

!!!info
    Para utilizar estas nuevas herramientas, es necesario tener [nodejs/npm](https://nodejs.org/es/){target="\_blank"} instalado en su máquina.
  
[ESLint](https://eslint.org/){target="\_blank"} y [Prettier](https://prettier.io/){target="\_blank"} son las herramientas utilizadas en Etendo para comprobar el formato del código JavaScript. Por comodidad, se han incluido algunos scripts para utilizar estas herramientas, tanto como scripts independientes como hooks de Mercurial para comprobar el código antes de realizar el commit.

###  Scripts independientes

- ESLint: 

    Al ejecutar el script `jslint` sin parámetros, se pasa el linter a todos los archivos `.js` no ignorados del proyecto, escaneando primero los archivos en `core` y todos los módulos que no tengan reglas especiales de ignorado (es decir, que tengan un archivo `.eslintignore` en la raíz del módulo).

    ```    
    ./modules/org.openbravo.client.kernel/jslint/jslint
    ```

    Al añadir el flag `-f`, ESLint intentará corregir todas las advertencias/errores que puedan corregirse automáticamente:
        
    ```    
    ./modules/org.openbravo.client.kernel/jslint/jslint -f
    ```

    Por último, se pueden añadir una o más rutas de archivos para ejecutar ESLint sobre esos archivos específicos.

        
    ```
    ./modules/org.openbravo.client.kernel/jslint/jslint modules/org.openbravo.client.application/web/org.openbravo.client.application/js/utilities/ob-utilities.js modules/org.openbravo.client.application/web/org.openbravo.client.application/js/utilities/ob-utilities-date.js
    ```

- Prettier: 

    Al ejecutar el script `jsformatter` sin parámetros, se pasa el formateador a todos los archivos `.js` no ignorados del proyecto, escaneando primero los archivos en `core` y todos los módulos que no tengan reglas especiales de ignorado (es decir, que tengan un archivo `.prettierignore` en la raíz del módulo).

    ```    
    ./modules/org.openbravo.client.kernel/jsformatter/jsformatter
    ```

    Al añadir el flag `-w`, en lugar de comprobar si los archivos están formateados, realiza el formateo real y los escribe en sus archivos correspondientes:

    ```    
    ./modules/org.openbravo.client.kernel/jsformatter/jsformatter -w
    ```

    Por último, se pueden añadir una o más rutas de archivos para ejecutar Prettier sobre esos archivos específicos.
        
    ```
    ./modules/org.openbravo.client.kernel/jsformatter/jsformatter modules/org.openbravo.client.application/web/org.openbravo.client.application/js/utilities/ob-utilities.js modules/org.openbravo.client.application/web/org.openbravo.client.application/js/utilities/ob-utilities-date.js
    ```

###  Ejecutar el script de npm directamente

Tenga en cuenta que, si su IDE soporta npm, también puede utilizar lo siguiente para comprobar su código:

- ESLint 

    ```
    npm run jslint modules/org.openbravo.client.application/web/org.openbravo.client.application/js/utilities/ob-utilities.js
    ```

- Prettier: 

    ```
    npm run jsformat -- --check modules/org.openbravo.client.application/web/org.openbravo.client.application/js/utilities/ob-utilities.js
    ```

    o, si quiere comprobar un módulo completo:

    ```    
    npm run jsformat -- --check 'modules/org.openbravo.mobile.core/**/*.js'
    ```

### Hooks de Git

Para utilizar estas herramientas como hooks de Git, ejecute este comando desde dentro de un repositorio de Openbravo:

```    
git config core.hooksPath .githooks
```

Para enganchar este script a otro repositorio, copie `.gitHooks` a ese repositorio y ejecute el mismo comando.

Si quiere estos hooks en módulos externos/retail, **desde dentro de `modules/ <name-of-module>`**, ejecute:

```    
git config core.hooksPath ../../.githooks
```

!!!note
    Estos scripts utilizan el comando bash `realpath` para comprobar entre cambios en staging y sin staging. Si no está instalado (lo está por defecto en la mayoría de sistemas), los hooks solo comprobarán los archivos en su estado actual, sin diferenciar entre cambios en staging y sin staging.


**Configurar hooks globalmente**

Es posible configurar esos hooks de git globalmente para todos los repositorios git. Esto significa que `.githooks` se ejecutará en cualquier commit en todos sus repositorios git locales.

```    
git config --global core.hooksPath /absolute/path/to/.githooks
```

Ejemplo (asumiendo que el directorio `myHooks` contiene `.githooks`):

```    
git config --global core.hooksPath /home/etendo/myHooks/.githooks
```

Si por cualquier motivo quiere eliminar esta configuración, ejecute lo siguiente:

```    
git config --global --unset core.hooksPath
```

## Formato de código

!!!info
    El código JavaScript se formatea usando [Prettier](https://prettier.io/){target="\_blank"}. Se aplican las siguientes convenciones, pero consulte [justificación de Prettier](https://prettier.io/docs/rationale.html){target="\_blank"} para algunas de las decisiones relativas al formato.  
  

### Espacios en lugar de tabulaciones

Configure su editor para usar **2 espacios en lugar de tabulaciones**.

### Llaves

Debido a la inserción implícita de punto y coma, comience siempre las llaves en la misma línea que aquello que abren. Por ejemplo:

```
if (something) {
    // ...
} else {
    // ...
}
```

### Declaración de variables

Se prefiere una única sentencia `var`. Todas las variables en una función **deben** declararse al principio de la función.

!!!note
    ¿Por qué necesito declarar las variables al principio de la función? Consulte [JavaScript Hosting explained](https://code.tutsplus.com/javascript-hoisting-explained--net-15092t){target="\_blank"}.
  
Es una buena práctica de codificación inicializar las variables cuando se declaran. Por tanto, debemos declarar e inicializar en una sola línea de código todas las variables de la función. Usando esta convención definiremos todas las variables al principio de la función y "estableceremos" el tipo de la variable añadiendo más información.

```
function f() {
    var a = 0,
        b = '',
        c = null;
}
 
function f() {
    var i = 0, j = 1; // Just one var
    // {...}
}
 
function x() { 
    var i = 0; // one var statement per variable is discouraged
    var j = 0;
    // {...}
}
 
// Variables on top of the function
 
function z() {
    var i, j, k;
    // {...}
}
 
function s() {
    var i;
    for (i = 0; i < 10; i++) {
    // do something
    }
    // {...}
    var j; // Variable declaration in the middle of a function is discouraged
}
```

### Inicializadores de arrays y objetos

Se permiten inicializadores de arrays y objetos en una sola línea cuando caben en una línea:

```
var arr = [1, 2, 3];  // No space after [ or before ].
var obj = {a: 1, b: 2, c: 3};  // No space after { or before }.
```

Los inicializadores de arrays y objetos en varias líneas se indentan con 2 espacios, igual que los bloques.

```
// Object initializer.
var inset = {
    top: 10, // Notice the space after the colon
    right: 20,
    bottom: 15,
    left: 12
};
 
// Array initializer.
this.rows_ = [
    '"Slartibartfast" <fjordmaster@magrathea.com>',
    '"Zaphod Beeblebrox" <theprez@universe.gov>',
    '"Ford Prefect" <ford@theguide.com>',
    '"Arthur Dent" <has.no.tea@gmail.com>',
    '"Marvin the Paranoid Android" <marv@googlemail.com>',
    'the.mice@magrathea.com'
];
 
// Used in a method call.
OB.ViewManager.openView('_140', {
    command: 'DEFAULT'
    icon: 'Window'
    id: '180'
    tabId: '180'
    tabTitle: 'Product'
    viewId: '_140'
    windowId: '140'
});
```

### Comillas simples

Una cadena puede definirse con comillas simples o dobles. Por consistencia, se prefieren las comillas simples.

```
var s = 'Etendo is great!';
```

### Declaración de funciones

Todas las funciones deben declararse antes de usarse. Las funciones internas deben ir después de la sentencia `var`. Esto ayuda a dejar claro qué variables se incluyen en su ámbito.

No debe haber espacio entre el nombre de una función y el `(` (paréntesis izquierdo) de su lista de parámetros. Debe haber un espacio entre el `)` (paréntesis derecho) y el `{` (llave izquierda) que inicia el cuerpo de la sentencia. El cuerpo en sí se indenta con cuatro espacios. El `}` (llave derecha) se alinea con la línea que contiene el inicio de la declaración de la función.

```
function outer(c, d) {
    var e = c * d;
 
    function inner(a, b) {
    return (e * a) + b;
    }
 
    return inner(0, 1);
}
```

Si un literal de función es anónimo, debe haber un espacio entre la palabra `function` y el `(` (paréntesis izquierdo). Si se omite el espacio, puede parecer que el nombre de la función es `function`, lo cual es una lectura incorrecta.
 

```
someObj = {
    method: function () {
    return this.datum;
    },
    datum: 0
};
```

### Argumentos de función

Cuando sea posible, todos los argumentos de una función deben listarse en la misma línea. Si hacerlo excediera el límite de 100 columnas, los argumentos deben partirse en líneas de forma legible. Para ahorrar espacio, puede partir lo más cerca posible de 100, o poner cada argumento en su propia línea para mejorar la legibilidad. La indentación puede ser de cuatro espacios, o alineada con el paréntesis.

```
// Four-space, wrap at 100.  Works with very long function names, survives
// renaming without reindenting, low on space.
OB.foo.bar.doThingThatIsVeryDifficultToExplain = function (
    veryDescriptiveArgumentNumberOne, veryDescriptiveArgumentTwo,
    tableModelEventHandlerProxy, artichokeDescriptorAdapterIterator) {
    // ...
};
 
// Four-space, one argument per line.  Works with long function names,
// survives renaming, and emphasizes each argument.
OB.foo.bar.doThingThatIsVeryDifficultToExplain = function (
    veryDescriptiveArgumentNumberOne,
    veryDescriptiveArgumentTwo,
    tableModelEventHandlerProxy,
    artichokeDescriptorAdapterIterator) {
    // ...
};
 
// Parenthesis-aligned indentation, wrap at 80.  Visually groups arguments,
// low on space.
function foo(veryDescriptiveArgumentNumberOne, veryDescriptiveArgumentTwo,
                tableModelEventHandlerProxy, artichokeDescriptorAdapterIterator) {
    // ...
}
 
// Parenthesis-aligned, one argument per line.  Visually groups and
// emphasizes each individual argument.
function bar(veryDescriptiveArgumentNumberOne,
                veryDescriptiveArgumentTwo,
                tableModelEventHandlerProxy,
                artichokeDescriptorAdapterIterator) {
    // ...
}
```

### Nombrar archivos

Los nombres de archivo deben estar solo en minúsculas y usar guion para separar palabras. Algunos servidores no distinguen mayúsculas/minúsculas y los espacios son una mala idea.

**Ejemplo:**

Incorrecto: LoginModel.js, cashUpWIndow.js...

Correcto: login-model.js, cashup-window.js...

### Devolver objeto

Las funciones que devuelven un objeto devolverán una variable en lugar del objeto. Devolver una variable con un nombre adecuado ayudará a entender mejor qué se devuelve (junto con el nombre de la función) y también será más legible. No es necesario crear una variable para devolver si no vamos a "trabajar" con ese objeto. Al programar, normalmente creamos una variable para devolver porque vamos a asignar algunos valores a ese objeto, pero si las funciones van a devolver un objeto nuevo, podemos hacerlo directamente; vea algunos ejemplos:

```
function myFunction (){
    var myObject =  {};
    myObject.time = new Date();
    myObject.total = getNet() + getTax();
    if(total > 0){
    myObject.isNegative = false;
    }else {
    myObject.isNegative = true;
    }
    return myObject;
}
 
function myFunction (){
    return {name: getName(), address: getDefaultAddress() + getCountry()};
}
```

## Consejos y trucos

### Expresiones booleanas true y false

Los siguientes valores son todos **false** en expresiones booleanas:

```
null
undefined
'' // the empty string
0  // the number
```

Pero tenga cuidado, porque estos valores son todos **true**:

```
'0'  // the string
[]   // the empty array
{}   // the empty object
```

Esto significa que, en lugar de esto:

```
while (x != null) {
```

puede escribir este código más corto (siempre que no espere que `x` sea 0, o la cadena vacía, o false):
 
```
while (x) {
```

Y si quiere comprobar una cadena para ver si es null o está vacía, podría hacer esto:

```
if (y != null && y != '') {
```

Pero esto es más corto y más limpio:
 
```
if (y) {
```

!!! warning
    Hay muchas cosas poco intuitivas sobre las expresiones booleanas. Estas son algunas de ellas:

    ```
    Boolean('0') == true
    '0' != true
    0 != null
    0 == []
    0 == false
    Boolean(null) == false
    null != true
    null != false
    Boolean(undefined) == false
    undefined != true
    undefined != false
    Boolean([]) == true
    [] != true
    [] == false
    Boolean({}) == true
    {} != true
    {} != false
    ```

### Operador condicional (ternario)

En lugar de esto:

```
if (val != 0) {
    return foo();
} else {
    return bar();
}
```

puede escribir esto:

```
return val ? foo() : bar();
```

### Operadores AND y OR

Estos operadores booleanos binarios son de cortocircuito y evalúan hasta el último término evaluado. **||** se ha llamado el operador "por defecto", porque en lugar de escribir esto:

```
function foo(opt_win) {
    var win;
    if (opt_win) {
    win = opt_win;
    } else {
    win = window;
    }
    // ...
}
```

puede escribir esto:

```
function foo(opt_win) {
    var win = opt_win || window;
    // ...
}
```

**&&** también es útil para acortar código. Por ejemplo, en lugar de esto:

```
if (node) {
    if (node.kids) {
    if (node.kids[index]) {
        foo(node.kids[index]);
    }
    }
}
```

podría hacer esto:

```
if (node && node.kids && node.kids[index]) {
    foo(node.kids[index]);
}
```

o esto:

```
var kid = node && node.kids && node.kids[index];
if (kid) {
    foo(kid);
}
```

---

Este trabajo es una obra derivada de [Convenciones de codificación de Javascript](http://wiki.openbravo.com/wiki/JavaScript_Coding_Conventions){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.