![](skins/openbravo/images/social-blogs-sidebar-banner.png){: .legacy-image-style}

######  Toolbox

![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Main Page  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Upload file  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} What links here  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Recent changes  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Help  
  
  

######  Search

######  Participate

![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Communicate  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Report a bug  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Contribute  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Talk to us now!  

  

#  How to create Jest testcases

##  Contents

  * 1  Overview 
  * 2  Installation 
  * 3  Creating a Test Case 
    * 3.1  Sample test file 
  * 4  Run tests/coverage 

  
---  
  
##  Overview

Jest  is a testing framework created by Facebook and currently used as the
default testing framework in  create-react-app  . Unlike Mocha, it is an
opinionated test runner and provides its own assertion and mocking methods.
The main advantage is that it runs out-of-the-box and has good integration
with technologies like React, Babel or Typescript.

##  Installation

Since PR19Q3, with the inclusion of the  new Linter and Formatter tools  ,
nodejs and npm should be installed. All dependencies can be installed just by
running:

    
    
    npm install

##  Creating a Test Case

Unit tests should be created under a **web-test** folder and filename should
be suffixed with **.test.js** .

Now you can require() your subject under test and start creating test cases.
See  Jest documentation  for reference.

####  Sample test file

    
    
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

##  Run tests/coverage

To run all unit tests available in an Openbravo instance (both Core and all
installed modules), run the following command:

    
    
    npm test

Testing can be limited to a particular module adding the path at the end of
the command:

    
    
    npm test modules/org.openbravo.mobile.core/

If, along with the test, you want to see a coverage report, run:

    
    
    npm run coverage

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
Tests should be placed in **web-test** folder, and files should have the
suffix **.test.js** .

This is a valid path for a test class:

**modules/org.openbravo.mymodule/web-test/mycomponent.test.js**  
  
---|---  
  
Retrieved from "  http://wiki.openbravo.com/wiki/How_to_create_Jest_testcases
"

This page has been accessed 4,584 times. This page was last modified on 18
November 2019, at 16:04. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**

