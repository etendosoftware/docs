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

  

#  How to create QUnit testcases

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
Starting to **PR20Q1** QUnit testing support will be completely removed and
replaced by Jest. See  How to create Jest test cases  for more info  
---|---  
  
##  Contents

  * 1  Overview 
    * 1.1  The flow 
  * 2  Creating a new QUnit test case 
    * 2.1  Declaring JavaScript test resources 
    * 2.2  Implementing a test case 
    * 2.3  Executing 
  * 3  Continuous Integration 

  
---  
  
##  Overview

Openbravo provides  QUnit  library as framework to write JavaScript unit test
cases.

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_QUnit_testcases-1.png){: .legacy-image-style}

###  The flow

QUnit test cases defined within Openbravo are executed by opening `
http(s)://your.server/openbravoContext/web/org.openbravo.client.kernel/ui-
test-suite/ ` URL. When accessing this URL this flow is executed:

  * QUnit library is loaded 
  * SmartClient is loaded 
  * An Openbravo session is created 
  * Openbravo application is loaded without being rendered 
  * Test resources are loaded and executed 

##  Creating a new QUnit test case

###  Declaring JavaScript test resources

Openbravo QUnit test cases are written as JavaScript static resources, which
needs to be declared in the  ComponentProvider  of the module that deploys
them. They must be declared in the ` getTestResources ` method.

    
    
     
    @ApplicationScoped
    @ComponentProvider.Qualifier(ExampleComponentProvider.EXAMPLE_VIEW_COMPONENT_TYPE)
    public class ExampleComponentProvider extends BaseComponentProvider {
        @Override
      public List<String> getTestResources() {
        final List<String> testResources = new ArrayList<String>();
        testResources.add("web/org.openbravo.client.application.examples/js/test/my-test.js");
        return testResources;
      }
    }

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
JavaScript test resources are only loaded when QUnit test cases are executed,
they are not part of the common static resources that compose the application.  
---|---  
  
###  Implementing a test case

Once the file with the test case is declared in the ComponentProvider it will
be loaded when QUnit test cases are executed.

Test cases look like:

    
    
     
    /*global QUnit */
     
    QUnit.module('org.openbravo.my.module');
     
    QUnit.test('Test 1', function () {
      QUnit.expect(2);
      QUnit.ok(isc, 'isc object is present');
      QUnit.ok(OB, 'OB object is present');
    });
     
    QUnit.test('Test 2', function () {
     // ...
    });

  * ` QUnit.module  ` : allows to group different related test cases. It is the equivalent of a  test suite  in JUnit. 
  * ` QUnit.ok  ` : performs the assert, being satisfied whenever 1st parameter is truthy. There is a bunch of other methods to perform different types of  assertions  . 

Comprehensive documentation  can be found in the QUnit site.

###  Executing

All QUnit test cases are executed by just opening `
http(s)://your.server/openbravoContext/web/org.openbravo.client.kernel/ui-
test-suite/ ` URL.

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_QUnit_testcases-3.png){: .legacy-image-style}

##  Continuous Integration

All Qunit test cases defined within Openbravo 3 distribution modules are
automatically executed as part of the  Continuous_Integration  .

All of them appear in ` int-gui >
com.openbravo.test.integration.qunit.testscripts > QUnitExecution `

Retrieved from "  http://wiki.openbravo.com/wiki/How_to_create_QUnit_testcases
"

This page has been accessed 4,718 times. This page was last modified on 18
November 2019, at 12:49. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**

