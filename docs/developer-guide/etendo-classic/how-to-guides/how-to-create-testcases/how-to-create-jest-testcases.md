---
title: How to Create Jest Test Cases
---
  
##  Overview

[Jest](https://jestjs.io/){target="_blank"} is a testing framework created by Facebook and currently used as the default testing framework in  [create-react-app](https://github.com/facebook/create-react-app){target="_blank"}  . Unlike Mocha, it is an opinionated test runner and provides its own assertion and mocking methods. The main advantage is that it runs out-of-the-box and has good integration with technologies like React, Babel or Typescript.

##  Installation

All dependencies can be installed just by
running:
    
    npm install

##  Creating a Test Case

!!! info
    Tests should be placed in `web-test` folder, and files should have the
    suffix `.test.js` .

    This is a valid path for a test class:

    `modules/com.etendoerp.mymodule/web-test/mycomponent.test.js`  

Now you can require() your subject under test and start creating test cases. See  [Jest documentation](https://jestjs.io/docs/getting-started){target="_blank"}  for reference.

####  Sample test file

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

##  Run tests/coverage

To run all unit tests available in an Etendo instance (both Core and all installed modules), run the following command:

    npm test

Testing can be limited to a particular module adding the path at the end of the command:    
    
    npm test modules/com.etendoerp.mymodule/

If, along with the test, you want to see a coverage report, run:
    
    npm run coverage

This work is a derivative of [How to Create Jest testcases](https://wiki.openbravo.com/wiki/How_to_create_Jest_testcases){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
  
