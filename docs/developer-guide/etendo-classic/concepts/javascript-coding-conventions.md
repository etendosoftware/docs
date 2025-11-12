---
title: Javascript Coding Conventions
tags:
    - Javascript
    - Coding
    - Conventions

status: beta
---

#  JavaScript Coding Conventions
  
!!! example  "IMPORTANT: THIS IS A BETA VERSION"
    It is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**.

##  Overview

This document is based on Google's JavaScript Style Guide and Douglas Crockford's [Code Conventions for the JavaScript Programming Language](https://www.crockford.com/code.html){target="\_blank"}.

##  Linting and Formatting

!!!info
    To use these new tools, it is required to have [nodejs/npm](https://nodejs.org/es/){target="\_blank"} installed in your machine.
  
[ESLint](https://eslint.org/){target="\_blank"}  and  [Prettier](https://prettier.io/){target="\_blank"}  are the tools used in Etendo to format check Javascript code. For convenience, has bundled some scripts in order to use these tools, either as standalone scripts and as Mercurial hooks to check the code before commiting it.

###  Standalone scripts

* ESLint: 

Running the jslint script without parameters passes the linter to all non-ignored .js files in the project, scanning first the files in core and all modules that has no special ignore rules (i.e. that has a .eslintignore file in the root of the module).

```    
./modules/org.openbravo.client.kernel/jslint/jslint
```

Adding the -f flag, ESLint will try to fix all warnings/errors that can be autofixed:
    
```    
./modules/org.openbravo.client.kernel/jslint/jslint -f
```

Finally, one or more files paths can be added to run ESLint for those specific files.

    
```
./modules/org.openbravo.client.kernel/jslint/jslint modules/org.openbravo.client.application/web/org.openbravo.client.application/js/utilities/ob-utilities.js modules/org.openbravo.client.application/web/org.openbravo.client.application/js/utilities/ob-utilities-date.js
```

* Prettier: 

Running the jsformatter script without parameters passes the formatter to all non-ignored .js files in the project, scanning first the files in core and all modules that has no special ignore rules (i.e. that has a .prettierignore file in the root of the module).

```    
./modules/org.openbravo.client.kernel/jsformatter/jsformatter
```

Adding the -w flag, instead of checking whether the files are formatted, performs the actual formatting and writes them in their corresponding files:

```    
./modules/org.openbravo.client.kernel/jsformatter/jsformatter -w
```

Finally, one or more files paths can be added to run Prettier for those specific files.
    
```
./modules/org.openbravo.client.kernel/jsformatter/jsformatter modules/org.openbravo.client.application/web/org.openbravo.client.application/js/utilities/ob-utilities.js modules/org.openbravo.client.application/web/org.openbravo.client.application/js/utilities/ob-utilities-date.js
```

###  Running npm script directly

Note that if your IDE supports npm, the following can be used as well to check your code:

* ESLint 

```
npm run jslint modules/org.openbravo.client.application/web/org.openbravo.client.application/js/utilities/ob-utilities.js
```

* Prettier: 

```
npm run jsformat -- --check modules/org.openbravo.client.application/web/org.openbravo.client.application/js/utilities/ob-utilities.js
```

or, if you want to check a whole module:

```    
npm run jsformat -- --check 'modules/org.openbravo.mobile.core/**/*.js'
```

###  Git hooks

For using these tools as Git hooks, run this command from inside an openbravo repository:

```    
git config core.hooksPath .githooks
```

To hook this script to another repository, copy the .gitHooks to that repo and run the same command.

If you want this hooks in external/retail modules, **from inside modules/ <name-of-module> ** , execute:

```    
git config core.hooksPath ../../.githooks
```

!!!note
    Those scripts use realpath bash command to check between staged andunstaged changes. If not installed(it is by default on most systems) hooks will only check files in their current state, not differentiating between staged and unstaged changes.

####  Set hooks globally

It is possible to set those git hooks globally for all git repositories. This means .githooks will be executed on any commit in all your git repositories locally.

```    
git config --global core.hooksPath /absolute/path/to/.githooks
```

Example (assuming myHooks dir contains .githooks):

```    
git config --global core.hooksPath /home/openbravo/myHooks/.githooks
```

If for any reason you want to remove this configuration execute the following:

```    
git config --global --unset core.hooksPath
```

###  Mercurial hooks

For using these tools as Mercurial hooks, add the following at the end of **.hg/hgrc** :

```
[hooks]
pretxncommit= ./modules/org.openbravo.client.kernel/jslint/jslint-hg
pre-commit = ./modules/org.openbravo.client.kernel/jsformatter/jsformatter-hg
```

Or the following if working in a module:
  
```
[hooks]
pretxncommit= ../org.openbravo.client.kernel/jslint/jslint-hg
pre-commit = ../org.openbravo.client.kernel/jsformatter/jsformatter-hg
```

!!!note
    You can hook the script to another mercurial hooks. See [this page](https://hgbook.red-bean.com/read/handling-repository-events-with-hooks.html){target="\_blank"}.

##  Code Formatting

!!!info
   Javascript code is formatted using [Prettier](https://prettier.io/){target="\_blank"}. The following conventions apply, but check [Prettier rationale](https://prettier.io/docs/rationale.html){target="\_blank"} for some of the choices regarding formatting.  
  
###  Spaces instead of Tabs

Configure your editor to use **2 spaces instead of tabs** .

###  Curly Braces

Because of implicit semicolon insertion, always start your curly braces on the same line as whatever they're opening. For example:

``` 
if (something) {
    // ...
} else {
    // ...
}
```

###  Variable Declaration

A single var statement is preferred. All the variables in a function **must** be declared on top of the function.

!!!note
    Why do I need to declare the variables on top of the function? Check [JavaScript Hosting explained](https://code.tutsplus.com/javascript-hoisting-explained--net-15092t){target="\_blank"}.
  
It is a good coding practice to initialize variables when you declare them. So we must declare and initialize in one coding line all vars of the function. Using this convention we will define all vars at the top of the function and we will "set" the type of the var adding more info to it.

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

###  Array and Object Initializers

Single-line array and object initializers are allowed when they fit on a line:

``` 
var arr = [1, 2, 3];  // No space after [ or before ].
var obj = {a: 1, b: 2, c: 3};  // No space after { or before }.
```

Multiline array initializers and object initializers are indented 2 spaces, just like blocks.

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

###  Single Quotes

A string can be defined with single or double quotes. For consistency, single quotes are preferred.

```
var s = 'Etendo is great!';
```

###  Function Declaration

All functions should be declared before they are used. Inner functions should follow the var statement. This helps make it clear what variables are included in its scope.

There should be no space between the name of a function and the ( (left parenthesis) of its parameter list. There should be one space between the ) (right parenthesis) and the { (left curly brace) that begins the statement body. The body itself is indented four spaces. The } (right curly brace) is aligned with the line containing the beginning of the declaration of the function.

``` 
function outer(c, d) {
    var e = c * d;
 
    function inner(a, b) {
    return (e * a) + b;
    }
 
    return inner(0, 1);
}
```

If a function literal is anonymous, there should be one space between the word function and the ( (left parenthesis). If the space is omitted, then it can appear that the function's name is function, which is an incorrect reading.
 
```
someObj = {
    method: function () {
    return this.datum;
    },
    datum: 0
};
```

###  Function Arguments

When possible, all function arguments should be listed on the same line. If doing so would exceed the 100-column limit, the arguments must be line-wrapped in a readable way. To save space, you may wrap as close to 100 as possible, or put each argument on its own line to enhance readability. The indentation may be either four spaces, or aligned to the parenthesis.

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

###  Naming files

Files name must be only in lower case and dash to separate words. Some servers are not case sensitive and spaces are a bad idea.

**Example:**

Wrong: LoginModel.js, cashUpWIndow.js...

**Right: login-model.js, cashup-window.js...**

###  Return object

Functions which returns an object will return a variable instead of the object. Returning a variable well named will help us to understand better what is returned (together with the function name) and will be also more readable. There is no need of creating a variable to return if we won't "work" with that object. Coding, we usually create a var to return because we will assign some values to that object but if the functions will return a new object we can do it directly, see some examples:

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

##  Tips and Tricks

###  True and False Boolean Expressions

The following are all **false** in boolean expressions:

``` 
    null
    undefined
    '' // the empty string
    0  // the number
```

But be careful, because these are all **true** :

``` 
    '0'  // the string
    []   // the empty array
    {}   // the empty object
```

This means that instead of this:

```    
while (x != null) {
```

you can write this shorter code (as long as you don't expect x to be 0, or the empty string, or false):
 
```    
while (x) {
```

And if you want to check a string to see if it is null or empty, you could do this:

```     
if (y != null && y != '') {
```

But this is shorter and nicer:
 
```    
if (y) {
```

**Caution:** There are many unintuitive things about boolean expressions. Here are some of them:

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

###  Conditional (Ternary) Operator (?:)

Instead of this:

``` 
if (val != 0) {
    return foo();
} else {
    return bar();
}
```

you can write this:

```    
return val ? foo() : bar();
```

###  && and ||

These binary boolean operators are short-circuited, and evaluate to the last evaluated term. **||** has been called the 'default' operator, because instead of writing this:

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

you can write this:

``` 
function foo(opt_win) {
    var win = opt_win || window;
    // ...
}
```

** && ** is also useful for shortening code. For instance, instead of this:

``` 
if (node) {
    if (node.kids) {
    if (node.kids[index]) {
        foo(node.kids[index]);
    }
    }
}
```

you could do this:

``` 
if (node && node.kids && node.kids[index]) {
    foo(node.kids[index]);
}
```

or this:

```
var kid = node && node.kids && node.kids[index];
if (kid) {
    foo(kid);
}
```

---

This work is a derivative of [Javascript Coding Conventions](http://wiki.openbravo.com/wiki/JavaScript_Coding_Conventions){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.