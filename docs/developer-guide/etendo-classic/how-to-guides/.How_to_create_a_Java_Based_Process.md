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

  

#  How to create a Java Based Process

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |  GUI
for processes explained in this document is generated using 2.50
infrastructure and are kept for backwards compatibility. If you are working
with **3.0MP20** or greater, consider implementing a  Standard Process
Definition  instead.  
---|---  
  
##  Contents

  * 1  How to create a Java Based Process 
  * 2  Example Module 
  * 3  Development Steps 
    * 3.1  Java class declaration 
    * 3.2  Defining the user interface 
    * 3.3  Add the process form to the menu 
    * 3.4  Build Step 
  * 4  The result 
  * 5  Variant: Running the process from a button in another window 
  * 6  Variant: Manual UI Pattern 

  
---  
  
##  How to create a Java Based Process

Java processes are one of the mechanisms Openbravo provides to implement
business logic. A java process can be a  background  process or can have a
user interface which allows entering parameters. In this howto we will discuss
a java process supported with a user interface with parameters.

This document discusses the Openbravo infrastructure for Java processes. For a
generic description of java processes see this wiki page:  Processes  .

##  Example Module

This howto is supported by an example module which shows example of the code
shown and discussed in this howto.

The code of the example module can be downloaded from this mercurial
repository:
https://code.openbravo.com/erp/mods/org.openbravo.client.application.examples/

The example module is available through the Central Repository (See 'Client
Application Examples'), for more information see the  Examples Client
Application  project page.

For your specific development you should create a new module. Please follow
the  How to create and package a module  section to create a new module.

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |  The
example module also contains implementations of other howtos.  
---|---  
  
##  Development Steps

The steps to create a java process supported by a user interface are:

  1. create a java class implementing the business logic 
  2. enter a new record in 'Report and Process', defining the pattern, the java class (step 1) and the parameters 
  3. add the new process to the menu 

###  Java class declaration

First at all, take a look at the Java package in which the java class is
defined, it must be included in the java package the module defines. The Java
class implementing the process must implement the
_org.openbravo.scheduling.Process_ interface, this is done usually extending
the class _org.openbravo.service.db.DalBaseProcess_ that provides common code
to use DAL in Processes. Extending this class there only needed to overwrite
one method:

    
    
     
     public void doExecute(ProcessBundle bundle) throws Exception;

This method receives a _ProcessBundle_ , this bundle contains all the
parameters for the process. When the process finishes it must add a result to
this bundle, this result is an _OBError_ instance that will be shown in the
pop-up. For further explanations on messages read the  Messages
documentation.

Let's explain it using a little example (this class and its parameters are
used in the process definition further down in this howto):

    
    
    public class ExampleJavaProcess extends DalBaseProcess {
     
      public void doExecute(ProcessBundle bundle) throws Exception {
        try {
     
          // retrieve the parameters from the bundle
          final String bPartnerId = (String) bundle.getParams().get("cBpartnerId");
          final String organizationId = (String) bundle.getParams().get("adOrgId");
          final String tabId = (String) bundle.getParams().get("tabId"); 
     
          final String myString = (String) bundle.getParams().get("mystring");
     
          // implement your process here
     
          // Show a result
          final StringBuilder sb = new StringBuilder();
          sb.append("Read information:<br/>");
          if (bPartnerId != null) {
            final BusinessPartner bPartner = OBDal.getInstance().get(BusinessPartner.class, bPartnerId);
            sb.append("Business Partner: " + bPartner.getIdentifier() + "<br/>");
          }
          if (organizationId != null) {
            final Organization organization = OBDal.getInstance().get(Organization.class,
                organizationId);
            sb.append("Organization: " + organization.getIdentifier() + "<br/>");
          }
          sb.append("MyString: " + myString + "<br/>");
     
          // OBError is also used for successful results
          final OBError msg = new OBError();
          msg.setType("Success");
          msg.setTitle("Read parameters!");
          msg.setMessage(sb.toString());
     
          bundle.setResult(msg);
     
        } catch (final Exception e) {
          e.printStackTrace(System.err);
          final OBError msg = new OBError();
          msg.setType("Error");
          msg.setMessage(e.getMessage());
          msg.setTitle("Error occurred");
          bundle.setResult(msg);
        }
      }
    }

In this example a parameter named _cBpartnerId_ is expected. It is read by the
following line:

    
    
     
      final String bPartnerId = (String) bundle.getParams().get("cBpartnerId");

The name of the parameter to use in the get method depends on the db column
name entered in the parameters of the process (see below).

Once the process is finished a new OBError is created to handle the message
and it is added as result to the _bundle_ .

    
    
     
      bundle.setResult(msg);

###  Defining the user interface

The java class above shows how to implement the backend business logic. This
section explains how to define a user interface which makes it possible to
enter parameters.

To define process records one should normally be a System Admin.

The first step is to create a process record, go to Application Dictionary >
Report and Process (or easier use quick launch and goto the Report and Process
window directly). Create a new process record like shown in the example below.

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Java_Based_Process-2.png){: .legacy-image-style}

  
The main thing here is to select UI Pattern: Standard. Further below it is
explained what UI Pattern Manual means.

Then create a child record in Process Class and enter the fully qualified
class name of the java class you created below.

**Important: check the default flag! If this is not done then a compile error
will occur in the next build step.**

Now the parameters of the process need to be defined. Or more exactly their
type and visualization. This is done through the Parameter child tab of the
process. The example has three parameters: business partner, organization and
a string. The screenshots below visualize their settings:

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Java_Based_Process-3.png){: .legacy-image-style}

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Java_Based_Process-4.png){: .legacy-image-style}

  
Some notes:

  * the db column name does not have to be a real database column, the value of this field is used to generate the parameter name used in the source code. It is adviced to use simple names without underscores (that's the simplest). 
  * the application element defines the label in the user interface 
  * the 2 reference fields denote the type of the field 

###  Add the process form to the menu

To make the process window available to the user it has to be added to a menu.
This is done like this:

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Java_Based_Process-5.png){: .legacy-image-style}

  

###  Build Step

After creating the process user interface, stop the application and type in
the following command in a console (within the development project):

    
    
    ant compile -Dtab=XXX

This will generate the process window.

If you have eclipse running, refresh the development project.

Then start the application and login with the client administrator (normally
the system administrator will not have access).

##  The result

Goto quick launch and enter the name of the new process or find it in the
correct location in the menu.

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Java_Based_Process-6.png){: .legacy-image-style}

  
Enter some values and press ok. The result:

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Java_Based_Process-7.png){: .legacy-image-style}

##  Variant: Running the process from a button in another window

A process can also be run from another window (from a button). A button in an
Openbravo window needs a (dummy) database column. To accomplish this do the
following:

  * add a column to the table shown in the window 
  * give the column the button reference and select the process 
  * create a window, tab and field for the column 

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Java_Based_Process-8.png){: .legacy-image-style}

  
This will show a button on the right in the window.

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Java_Based_Process-9.png){: .legacy-image-style}

  
When a process is run from another window then the ProcessBundle will contain
extra default parameters which can be useful:

  * recordID: the id of the selected record 
  * tabId: the id of the tab from which the process was called 

##  Variant: Manual UI Pattern

The difference between _Standard_ and _Manual_ _UI Pattern_ is that no pop-up
is automatically generated for _Manual UI_ pattern processes, in this case the
pop-up must be manually generated by the class implementing the process.

As shown above, java classes for standard processes implement the Manual
processes are implemented by a Java class implementing the
_org.openbravo.scheduling.Process_ interface. For manual processes the java
class needs to extend _org.openbravo.base.secureApp.HttpSecureAppServlet_ ,
this is a standard servlet that generates the pop-up.

Retrieved from "
http://wiki.openbravo.com/wiki/How_to_create_a_Java_Based_Process  "

This page has been accessed 40,112 times. This page was last modified on 19
March 2013, at 13:54. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**

