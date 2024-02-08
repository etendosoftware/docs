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

  

#  How to create JUnit testcases

##  Contents

  * 1  Objective 
  * 2  Preparing development environment 
    * 2.1  Import into Eclipse IDE 
  * 3  Creating the testcase 
    * 3.1  Just before starting 
      * 3.1.1  Test cases in OpenbravoTest 
      * 3.1.2  Inheriting from OB BaseTest 
      * 3.1.3  Execution order of test methods 
    * 3.2  Creating the Java class 
      * 3.2.1  Understanding the class 
    * 3.3  Transaction Handling 
    * 3.4  Side-Effect Free 
    * 3.5  Approach to new features of JUnit 4.11 
      * 3.5.1  Parameterized Tests 
      * 3.5.2  Rules 
      * 3.5.3  Assertions and Hamcrest 1.13 
    * 3.6  Approach to new features of JUnit 4.13 
    * 3.7  JSON Matchers 
      * 3.7.1  equal 
      * 3.7.2  matchesObject 
      * 3.7.3  hasItems 
    * 3.8  Ant Test Tasks 
      * 3.8.1  Skipping test cases 
  * 4  The Result 
  * 5  Testing Requests 
  * 6  Testing CDI 
    * 6.1  Scopes 
    * 6.2  Parameterization 
    * 6.3  DAL event observers 
  * 7  Using Mockito 
  * 8  Run test located in external module locally 

  
---  
  
##  Objective

This how-to will focus on creating a testcase making use of the Openbravo test
base classes. The testcase will check that our system has at least one User
with password. For this, we'll use the new DAL approach to access the
database.

In computer programming, **unit testing** is a software design and development
method where the programmer gains confidence that individual units of source
code are fit for use. A unit is the smallest testable part of an application.
In procedural programming a unit may be an individual program, function,
procedure, etc., while in object-oriented programming, the smallest unit is a
method, which may belong to a base/super class, abstract class or
derived/child class.  [1]

All new developments must belong to a module that is not the _core_ module.
Please follow the  How to create and package a module  section to create a new
module.

##  Preparing development environment

First of all you need to import src-test components of the Openbravo ERP.
Follow the instructions described below.

###  Import into Eclipse IDE

Launch Eclipse.

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
After Eclipse has started go to _Project_ menu and **disable** _Build
Automatically_ option there.  
---|---  
  
Now one new project need to be imported in the workspace (by menu _File_ =>
_Import_ and then _General_ => _Existing Projects into Workspace_ ). Here they
are:

    
    
    OpenbravoTest    XXX\opensource\openbravo\erp\devel\main\src-test
    

Now, you are ready to work with test cases.

##  Creating the testcase

###  Just before starting

####  Test cases in OpenbravoTest

OpenbravoTest provides a set of unit tests, often called 'test cases' for
things such as: runtime model consistency, data access layer features,
webservices features, etc. This test cases are based on  JUnit  testing
framework.

The set of tests you can find and study them in the project _OpenbravoTest_ :

    
    
    openbravo
     |- ...
    OpenbravoCore
     |- ...
    OpenbravoTest
     |- src                <-- source of the testcases
    OpenbravoTrl
     |- ...
    OpenbravoWAD
     |- ...
    

  
Here is a direct link to the testcases in the code repository:  Openbravo test
cases  .

####  Inheriting from OB BaseTest

All the core testcases are subclasses from OBBaseTest
(org.openbravo.test.base.OBBaseTest). This class handles all the necessary
steps to initialize the Data Access Layer, takes care of transaction handling
and provides a set of utilities (methods) for working with the Openbravo
context (OBContext).

####  Execution order of test methods

Until now, the methods were simply invoked in the order returned by the
reflection API. However, using the JVM order is unwise since the Java platform
does not specify any particular order, and in fact JDK 7 returns a more or
less random order. Of course, well-written test code would not assume any
order, but some does, and a predictable failure is better than a random
failure on certain platforms.

###  Creating the Java class

  * Open your Eclipse IDE. 
  * Create a new folder structure under the _modules_ folder: _modules/org.openbravo.test.examples/src-test/org/openbravo/test/examples_ . 
  * Add the newly created **src-test** folder to the _Java sources_ on the project. 
  * Create a new Java class on the org.openbravo.test.examples package with the following content: 

    
    
     
     package org.openbravo.test.examples;
     
     import static org.junit.Assert.assertTrue;
     
     import java.util.List;
     
     import org.junit.Test;
     import org.openbravo.dal.service.OBCriteria;
     import org.openbravo.dal.service.OBDal;
     import org.openbravo.model.ad.access.User;
     import org.openbravo.test.base.OBBaseTest;
     
     public class ExampleTest extends OBBaseTest {
     
      @Test
      public void testUsersCount() {
        setSystemAdministratorContext();
        final OBCriteria<User> uCriteria = OBDal.getInstance().createCriteria(User.class);
        final List<User> uList = uCriteria.list();
        int userCount = 0;
        for (User u : uList) {
          if (u.getPassword().length() > 0)
            userCount++;
        }
        assertTrue(userCount > 0);
        System.out.println("Total of users with password: " + (userCount));
      }
    }
     

####  Understanding the class

You have just created a new class named Example that extends from the
OBBaseTest  class.

    
    
     
    public void testUsersCount() {}

This class has a testUsersCount function. Note that all testing methods _must_
start with test in the function name. e.g. testAllWarehouses(),
testMyFirstTest(), etc

    
    
     
    setSystemAdministratorContext();

Sets the context as if a System Administrator is logged in the application.

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
There is a setUserContext(...) method to select running as another user, this
method can be called in the middle of a testcase to switch user (if required)  
---|---  
      
    
     
    final OBCriteria<User> uCriteria = OBDal.getInstance().createCriteria(User.class);
    final List<User> uList = uCriteria.list();

Uses the  OBDal  instance to create a new  OBCriteria  object, and uses it for
listing all (since we are not filtering) the Users in the database.

    
    
     
    int userCount = 0;
     for (User u : uList) {
       if (u.getPassword().length() > 0)
         userCount++;
     }

We loop trough the uList collection, and we increment the userCount variable
if the user has a password length > 0\.

    
    
     
    assertTrue(userCount > 0);

We assert that the userCount is more than 0.

    
    
     
     System.out.println("Total of users with password: " + (userCount));

Finally we print a total of users with password just for the record.

###  Transaction Handling

A question which might pop-up when looking at the above code: where is the
database transaction handling done? The answer is that this is handled by the
OBBaseTest  class and the Openbravo data access layer:

  * a transaction is automatically started at first database access in the test cases. This is done by the Data Access Layer. 
  * a transaction is either committed (when no exception happened) or rolled-back (when an exception happened). 

The OBBaseTest class detects automatically if an exception happened or not.

There are certainly cases whereby it makes sense to have more control over the
database transactions. There are a number of relevant methods which can be
useful then:

  * OBBaseTest.commitTransaction: a convenience method which commits the transaction for you. This can be useful if you want to check if certain database actions result in exceptions in the database. 
  * OBDal.getInstance().flush(): flushes the update/insert queries in hibernate to the database. 
  * OBDal.getInstance().commitAndClose(): commits the transaction and closes the session. A new session/transaction is automatically started at the next database access. 
  * OBDal.getInstance().rollbackAndClose(): rolls back and closes the transactions. A new session/transaction is automatically started at the next database access. 

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_JUnit_testcases-2.png){: .legacy-image-style} |  DAL event observers  are not
triggered within test cases extending ` OBBaseTest ` class. They to work
require of test cases extending ` WeldBaseTest ` . See  this section  for more
information.  
---|---  
  
###  Side-Effect Free

A test case will often change the data in the underlying database. Most of the
time it is not feasible to setup a completely new test database for each test
run. Therefore test-cases should be developed such that they are side effect
free. This means:

  * When the test-case changes data then it should have a test method which is run as the last test method which cleans up/repairs the data. 
  * This clean-up method should also clean up data which is left from previous test runs.For this common issue should be used @AfterClass notation. This method runs automatically at the end of the class. More info in:  AfterClass-Notation  . 

This last point is important because there can be always reasons why during a
test the clean-up step is not performed. For example because the test run is
stopped before the clean-up is done.

###  Approach to new features of JUnit 4.11

####  Parameterized Tests

More info in:  Parameterized-Test

####  Rules

More info in:  Rules

####  Assertions and Hamcrest 1.13

Hamcrest is a framework for writing matcher objects allowing 'match' rules to
be defined declaratively. There are a number of situations where matchers are
invaluble, such as UI validation, or data filtering, but it is in the area of
writing flexible tests that matchers are most commonly used.

When writing tests it is sometimes difficult to get the balance right between
overspecifying the test, and not specifying enough (making the test less
valuable). Having a tool that allows you to pick out precisely the aspect
under test and describe the values it should have, to a controlled level of
precision, helps greatly in writing tests.

More info in:  Hamcrest

  

###  Approach to new features of JUnit 4.13

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
This feature is available starting from ** 3.0PR22Q3  ** .  
---|---  
  
With the update to version 4.13 it is necessary to do the following changes on
the JUnit tests:

  * "import static org.junit.Assert.assertThat;", must be changed to "import static org.hamcrest.MatcherAssert.assertThat;" 
  * ExpectedException usage must be substituted with the function assertThrows, follow some of the examples already present in the latest version of core, or check the following  Merge Request  . 

  

###  JSON Matchers

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
This feature is available starting from ** 3.0PR22Q2  ** .  
---|---  
  
Openbravo provides a set of matchers that can be useful when asserting
JSONObjects or JSONArrays.

####  equal

Matches when the examined JSONObject has exactly the same number of properties
with the same values as the expected one. The order of the keys is not taken
into account. Supports matcher properties.

    
    
     
      @Test
      public void testEqual() {
        JSONObject json1 = new JSONObject(Map.of("p1", 1, "p2", "abcd"));
        JSONObject json2 = new JSONObject(Map.of("p1", 1, "p2", "abcd"));
        JSONObject json3 = new JSONObject(Map.of("p2", "abcd", "p1", 1));
        JSONObject json4 = new JSONObject(Map.of("p1", 1, "p2", "efgh"));
        JSONObject json5 = new JSONObject(Map.of("p1", 1));
        JSONObject json6 = new JSONObject(Map.of("p1", greaterThan(0), "p2", startsWith("abc"))); // matcher properties
     
        assertThat("JSON objects are equal", json1, equal(json2));
        assertThat("JSON objects are equal", json1, equal(json3));
        assertThat("JSON objects are not equal", json1, not(equal(json4)));
        assertThat("JSON objects are not equal", json1, not(equal(json5)));
        assertThat("JSON objects are equal", json1, equal(json6));
      }

####  matchesObject

Matches when the examined JSONObject contains the properties with the same
values of the expected one. The order of the keys is not taken into account.
Supports matcher properties.

    
    
     
      @Test
      public void testMatchesObject() {
        JSONObject json1 = new JSONObject(Map.of("p1", 1, "p2", "abcd"));
        JSONObject json2 = new JSONObject(Map.of("p1", 1, "p2", "abcd"));
        JSONObject json3 = new JSONObject(Map.of("p2", "abcd", "p1", 1));
        JSONObject json4 = new JSONObject(Map.of("p1", 1, "p2", "efgh"));
        JSONObject json5 = new JSONObject(Map.of("p1", 1));
        JSONObject json6 = new JSONObject(Map.of("p1", 1, "p2", "abcd", "p3", "abcd"));
        JSONObject json7 = new JSONObject(Map.of("p1", greaterThan(0), "p2", "abcd"));
     
        assertThat("JSON object match", json1, matchesObject(json2));
        assertThat("JSON object match", json1, matchesObject(json3));
        assertThat("JSON object does not match", json1, not(matchesObject(json4)));
        assertThat("JSON object match", json1, matchesObject(json5));
        assertThat("JSON object does not match", json1, not(matchesObject(json6)));
        assertThat("JSON object match", json1, matchesObject(json7));
      }

####  hasItems

Used to match the items of a JSONArray. This matcher can be used with two
different kind of arguments.

If an array of objects is passed, then it matches when the examined JSONArray
contains all the received objects. The order of the objects is not taken into
account.

    
    
     
      @Test
      public void testHasItems() {
        JSONObject json1 = new JSONObject(Map.of("p1", 1, "p2", "abcd"));
        JSONObject json2 = new JSONObject(Map.of("p2", 2, "p3", "efgh"));
        JSONArray array = new JSONArray();
        array.put(json1);
        array.put(json2);
        array.put(5);
        JSONObject json3 = new JSONObject(Map.of("p2", 2, "p3", startsWith("e")));
        JSONObject json4 = new JSONObject(Map.of("p2", 2, "p3", "ijkl"));
     
        assertThat("JSON array has items", array, hasItems(5, json3));
        assertThat("JSON array does not have items", array, not(hasItems(4, json3)));
        assertThat("JSON array does not have items", array, not(hasItems(json4)));
      }

It also supports receiving an array of  Hamcrest  matchers. In that case, then
it matches when the examined JSONArray matches with all the received matchers.

    
    
     
      @Test
      public void testHasItems() {
        JSONObject json1 = new JSONObject(Map.of("p1", 1, "p2", "abcd"));
        JSONObject json2 = new JSONObject(Map.of("p2", 2, "p3", "efgh"));
        JSONArray array = new JSONArray();
        array.put(json1);
        array.put(json2);
        array.put(5);
        JSONObject json3 = new JSONObject(Map.of("p2", 2, "p3", startsWith("e")));
        JSONObject json4 = new JSONObject(Map.of("p1", 1));
        JSONObject json5 = new JSONObject(Map.of("p2", 2, "p3", "ijkl"));
     
        assertThat("JSON array has items", array, hasItems(greaterThan(4), equal(json3)));
        assertThat("JSON array has items", array, hasItems(greaterThan(4), matchesObject(json4)));
        assertThat("JSON array does not have items", array, not(hasItems(greaterThan(5))));
        assertThat("JSON array does not have items", array, not(hasItems(equal(json5))));
      }

###  Ant Test Tasks

Openbravo has a number of ant tasks which run the test cases:

  * run.tests: the default, it runs the suite: _org.openbravo.test.AntTaskTests_ . These tests are side effect free and can be run multiple times, after the run the database should be in the same state as before. 
  * run.quick.tests: this task runs test cases which are fast and which test the most important parts of the system. It runs the test suite: _org.openbravo.test.AllQuickAntTaskTests_ . 
  * run.all.tests: runs the suite _org.openbravo.test.AllAntTaskTests_ . This suite contains all the test cases, also tests which can change the database. 

All the test cases are based on the Small Bazaar default data.

When adding new test classes to Openbravo ERP the developer has to always add
the test class to the AllAntTaskTests test suite and if it is side effect free
and quick to the AllQuickAntTaskTests and if it is side effect free but takes
a bit more time to the AntTaskTests test suite.

####  Skipping test cases

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
This feature is available starting from ** 3.0PR17Q2  ** .  
---|---  
  
It's possible to define a list of test cases to be skipped. This is done by
creating a file named ` disabled-tests ` in ` config ` directory. This file
can contain a list of either fully qualified class names to be completely
skipped and/or fully qualified class names followed by a "." and method name
to skip individual test cases.

##  The Result

To be able to execute your testcases:

  * Right click on the ExampleTest class. 
  * Select _Run AS > JUnit Test _ (Eclipse recognizes the class as a JUnit test because inherits from the JUnit OBBaseTest class). 

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_JUnit_testcases-6.png){: .legacy-image-style}

  * You can check the result of the test case on the JUnit view: 

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_JUnit_testcases-7.png){: .legacy-image-style}

  * And the output of your tests in the Console view: 

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_JUnit_testcases-8.png){: .legacy-image-style}

##  Testing Requests

In general unit tests don't require of an Openbravo instance running in Tomcat
to be executed. But in some cases, how requests work is wanted to be tested.
Depending on the request to be tested, different classes should be extended:

  * **REST Webservices** . ` BaseWSTest ` should be extended, it deals with authentication and provides methods to execute requests, parse xml results, etc. 
  * **Other Requests** (such as datasources). ` BaseDataSourceTestNoDal ` or ` BaseDataSourceTestDal ` classes can be extended (depending if the test case requires or not DAL). Similarly to webservices it provides authentication handling as well as utility methods to perform requests. 

##  Testing CDI

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
This feature is available since **PR15Q4**  
---|---  
  
Default test cases extending ` org.openbravo.test.base.OBBaseTest ` class
cannot make use of dependency injection. In order to use it `
org.openbravo.base.weld.test.WeldBaseTest ` class needs to be extended
instead. This is also a subclass of ` OBBaseTest ` , so it makes available all
DAL infrastructure.

` OBBaseTest ` uses internally  Arquillian  runner to create a Weld container.

Example of a test case injecting dependencies:

    
    
     
    public class CdiInfrastructure extends WeldBaseTest {
     
      @Inject
      private ApplicationScopedBean applicationBean;
     
      @Inject
      private SessionScopedBean sessionBean;
     
      @Inject
      private RequestScopedBean requestBean;
     
      /** beans are correctly injected */
      @Test
      public void beansAreInjected() {
        assertThat("application bean is injected", applicationBean, notNullValue());
        assertThat("session bean is injected", sessionBean, notNullValue());
        assertThat("request bean is injected", requestBean, notNullValue());
      }
    }

###  Scopes

Application and session scopes are shared among all test cases in the same
class whereas a new request scope is created for each test case method.
Application scope is reset for each new class.

    
    
     
     /** starts application and session scopes */
      @Test
      @InSequence(1)
      public void start() {
        applicationBean.setValue("application");
        sessionBean.setValue("session");
        requestBean.setValue("request");
     
        assertThat(applicationBean.getValue(), equalTo("application"));
        assertThat(sessionBean.getValue(), equalTo("session"));
        assertThat(requestBean.getValue(), equalTo("request"));
      }
     
      /** application and session scopes are preserved but not request scope */
      @Test
      @InSequence(2)
      public void applicationAndSessionShouldBeKept() {
        assertThat(applicationBean.getValue(), equalTo("application"));
        assertThat(sessionBean.getValue(), equalTo("session"));
        assertThat(requestBean.getValue(), nullValue());
      }

###  Parameterization

Because ` CdiInfrastructure ` class uses `
org.jboss.arquillian.junit.Arquillian ` runner, it is not possible to use
other runners, which also includes ` org.junit.runners.Parameterized ` runner.

This limitation can be workarounded by adding a field annotated as ` @Rule `
with ` org.openbravo.base.weld.test.ParameterCdiTestRule ` type created with
the list of the values for parameters and another field annotated as `
@ParameterCdiTest ` which will take those values. In this case each test case
will be executed as many times as number of items the parameter list contains
each of them the parameter field will take a different item.

    
    
     
    public class ParameterizedCdi extends WeldBaseTest {
      public static final List<String> PARAMS = Arrays.asList("param1", "param2", "param3");
     
      /** defines the values the parameter will take. */
      @Rule
      public ParameterCdiTestRule<String> parameterValuesRule = new ParameterCdiTestRule<String>(
          PARAMS);
     
      /** this field will take the values defined by parameterValuesRule field. */
      private @ParameterCdiTest String parameter;
     
      private static int counterTest1 = 0;
     
      /** Test case to be executed once per parameter value */
      @Test
      public void test1() {
        assertThat("parameter value", parameter, equalTo(PARAMS.get(counterTest1)));
        counterTest1++;
      }
    }

In this example ` test1 ` test case will be executed 3 times having `
parameter ` field "param1", "param2" and "param3" value in each of these
executions.

Unlike when using ` Parameterized.class ` runner, all these 3 executions are
seen as a single execution ( ` Parameterized.class ` would show 3 independent
executions), this causes that if, for example, first execution fails the rest
will not be run.

###  DAL event observers

Because  DAL event observers  make use of CDI to work, they are not executed
in standard test cases extending ` OBBaseTest ` .

This limitation does not apply when using ` WeldBaseTest ` tests.

##  Using Mockito

TO BE DONE

##  Run test located in external module locally

When a test is created in an external module (external of OpenbravoTest
project) some problems are found to execute the testcase in Eclipse. See an
example of a test located in **org.openbravo.client.myob** module.

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_JUnit_testcases-10.png){: .legacy-image-style}

  
As we can see in the previous picture, it is not possible to execute
MyOpenbravoTest.java. The following actions will be done to be able to execute
in local your testcase located in other module (external module of
OpenbravoTest project):

  * First of all, OpenbravoTest project should be configured properly. Steps: 
    * Copy classpahttp://wiki.openbravo.com/wiki/How_to_create_JUnit_testcases#Run_test_located_in_external_module_locallyth: ~/pi/src-test$ cp .classpath.template .classpath 
    * Import in eclipse project folder ~/src-test 
    * Full documentation can be found in the previous sections of this page. 
  * Right click on OpenbravoTest project. 
  * Select Properties > Java Build Path. 
  * Click on ‘Link Source’ button. 
  * Fill the ‘Linked folder location’ field with the src-test folder of the target module. (e.g. openbravo-path/modules/org.openbravo.client.myob/src-test). 
  * Click on ‘Apply’ button. 

Now it is possible to execute a test located in external module locally. See
the image below.

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_JUnit_testcases-11.png){: .legacy-image-style}

Retrieved from "  http://wiki.openbravo.com/wiki/How_to_create_JUnit_testcases
"

This page has been accessed 15,771 times. This page was last modified on 3
October 2023, at 12:03. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**

