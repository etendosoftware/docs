---
title: Cómo crear casos de prueba con Jest
tags:
  - Cómo hacer
  - Jest
  - Prueba
  - Casos de prueba
---

# Cómo crear casos de prueba con Jest
  
##  Visión general

[Jest](https://jestjs.io/){target="_blank"} es un framework de pruebas creado por Facebook y actualmente utilizado como framework de pruebas predeterminado en [create-react-app](https://github.com/facebook/create-react-app){target="_blank"}. A diferencia de Mocha, es un ejecutor de pruebas con una filosofía definida y proporciona sus propios métodos de aserción y de mocking. La principal ventaja es que funciona listo para usar y tiene buena integración con tecnologías como React, Babel o Typescript.

##  Instalación

Todas las dependencias se pueden instalar simplemente ejecutando:
    
    npm install

##  Creación de un caso de prueba

!!! info
    Las pruebas deben colocarse en la carpeta `web-test`, y los archivos deben tener el sufijo `.test.js`.

    Esta es una ruta válida para una clase de prueba:

    `modules/com.etendoerp.mymodule/web-test/mycomponent.test.js`  

Ahora puede usar require() para incluir el elemento bajo prueba y empezar a crear casos de prueba. Consulte la [documentación de Jest](https://jestjs.io/docs/getting-started){target="_blank"} como referencia.

####  Archivo de prueba de ejemplo

```javascript title="org.openbravo.client.application/web-test/ob-utilities-date.test.js"
require('../web/org.openbravo.client.application/js/utilities/ob-utilities-date');
 
describe('org.openbravo.client.application - OB.Utilities.Date', () => {
  beforeEach(() => {
    // Execute this before each test
  });
 
  afterEach(() => {
    // Execute this after each test
  });
 
  it('The year where we should change century in 2 digits year format is 50', () => {
    expect(OB.Utilities.Date.centuryReference).toEqual(50);
  });
 
  // Describe blocks can be nested to group test cases
  describe('OB.Utilities.Date.normalizeDisplayFormat', () => {
    it('function works', () => {
      const normalizedFormat = OB.Utilities.Date.normalizeDisplayFormat('DD-MM-YYYY');
      expect(normalizedFormat).toEqual('%d-%m-%Y');
    });
 
    it('function works with other input', () => {
      const normalizedFormat = OB.Utilities.Date.normalizeDisplayFormat('DD-MM-YY');
      expect(normalizedFormat).toEqual('%d-%m-%y');
    });
  });
});
```

##  Ejecutar pruebas/cobertura

Para ejecutar todas las pruebas unitarias disponibles en una instancia de Etendo (tanto Core como todos los módulos instalados), ejecute el siguiente comando:

    npm test

Las pruebas se pueden limitar a un módulo concreto añadiendo la ruta al final del comando:    
    
    npm test modules/com.etendoerp.mymodule/

Si, junto con la prueba, desea ver un informe de cobertura, ejecute:
    
    npm run coverage

Este trabajo es una obra derivada de [Cómo crear casos de prueba con Jest](https://wiki.openbravo.com/wiki/How_to_create_Jest_testcases){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.