---
title: Number To Word
---
The NumberToWord module deploys an infraestructure to define Number to Word conversion modules so that different logics for different languages can be deployed.

This module allows to convert numbers into words. It is specially useful while printing checks. 

Once installed this module creates a new window which can be found in *General Setup > Application*:

![Number To Word Converter](/docs/assets/drive/1LYIhLCeLGa3ARKn1O92vg39RdYnjtWao.png)

Some fields to note are:

* **Organization**: legal entity which requires printing checks in a given language.
* **Language**: language's words into which the amounts to pay needs to be converted.
* **Javaclass**: route where the javaclass that converts amounts into a given language is located. 

The "javaclass" field is required but empty by default unless another module such as the Number to Word (Spanish) or the Number to Word (English) is installed and properly applied to the legal entity for which it is required to print checks.
Additionally, the javaclass can be filled in manually.

---

This work is a derivative of ["Number To Word"](http://wiki.openbravo.com/wiki/NumberToWord) by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo), used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/). This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/) by [Etendo](https://etendo.software).


