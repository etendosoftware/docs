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

  

#  How to create a Navigation Bar Component

##  Contents

  * 1  Introduction 
  * 2  Example Module 
  * 3  Main flow of the navigation bar generation 
  * 4  Implementing a navigation bar component 
    * 4.1  Creating a component 
    * 4.2  Creating a template 
      * 4.2.1  The template source 
      * 4.2.2  Template Record 
    * 4.3  Registering the component as a Navigation Bar Component 
    * 4.4  The result 
    * 4.5  Static Navigation Bar Components 

  
---  
  
##  Introduction

This howto discusses how a component can be added to the Openbravo main
navigation bar. Navigation bar components are shown in the top of the
Openbravo layout. They are positioned from left to right.

Some main features of the Openbravo navigation bar components:

  * a navigation bar component can be any  Smartclient  canvas. 
  * modules can provide new navigation bar components. 
  * the position of a navigation bar component can be controlled. 
  * navigation bar components can be enabled by role. 

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Navigation_Bar_Component-0.png){: .legacy-image-style}

##  Example Module

This howto is supported by an example module which shows examples of the code
shown and discussed.

The code of the example module can be downloaded from this mercurial
repository:
https://code.openbravo.com/erp/mods/org.openbravo.client.application.examples/

The example module is available through the Central Repository (See 'Client
Application Examples'), for more information see the  Examples Client
Application  project page.

##  Main flow of the navigation bar generation

The navigation bar generation goes through a number of steps:

  1. the user logs in, and is navigated to the start page 
  2. the start page builds the main layout consisting of the navigation bar and the main content area (with tabs) 
  3. the navigation bar is generated on the server as javascript (which is send to the browser). 
  4. this is done by the main layout component. This component creates the overall javascript structure and then reads the navigation bar components from the navigation bar component table (using role information). 
  5. each navigation bar component is instantiated, its template is set and the generate method is called which generates the javascript of that component (using the template). 
  6. the javascript of each component is assumed to create a single canvas or an array of Smartclient canvasses. The javascript (i.e. navigation bar component) is placed as a member of the horizontal layout, which builds the navigation bar. 

This main flow illustrates that each navigation bar component can implement
its own visualization by providing/using a custom template and component.

##  Implementing a navigation bar component

To create a component which is shown in the navigation bar the following parts
need to be implemented:

  * create a java class (the component) which represents the navigation bar component on the server 
  * create a template which generates the javascript which creates the component on the client 
  * register the navigation bar component in the navigation bar component table 

Each of these steps is described in more detail below.

The example module contains a Hello World component with a template. This
example adds a button to the navigation bar which (when clicked) will say
hello to the current user.

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Navigation_Bar_Component-1.png){: .legacy-image-style}

  

###  Creating a component

A component is useful when you want to add runtime information to the
navigation bar component javascript when it gets generated. For example the
user name or other role or user information.

_If you don't have the requirement to use dynamic information in the generated
javascript of your component then you don't need to implement a component
(only a template). You can make use of the standard Openbravo template
component: org.openbravo.client.kernel.BaseTemplateComponent, in the
navigation bar component definition table._

The example module has a hello world component which provides the current
logged in user to the template. The component can be found in the module's
src  directory. Here is the code:

    
    
    package org.openbravo.examples.client.application;
     
    import org.openbravo.client.kernel.BaseTemplateComponent;
    import org.openbravo.dal.core.OBContext;
     
    /**
     * Provides a widget which shows a hello world message when clicked.
     * 
     * @author mtaal
     */
    public class HelloWorldComponent extends BaseTemplateComponent {
     
      public String getName() {
        return OBContext.getOBContext().getUser().getName();
      }
    }

###  Creating a template

The template contains the actual javascript. A template consists of two parts:

  1. a template file (the template source) ending on ftl (a  freemarker  extension) which is located in the source tree (in the classpath). 
  2. a record in the template table 

The template is a powerful mechanism of the Openbravo system as it makes it
possible to combine dynamic generated information and allows overriding of
templates by other modules.

####  The template source

To create the template for your navigation bar component, create a ftl file in
the source tree of your module. The ftl file should contain plain javascript
with possible freemarker constructs to read information from the component.
The javascript should create one Smartclient canvas or a javascript array with
Smartclient canvas instances.

As an example, the hello world template can be found in the
org.openbravo.client.application.examples.templates  package, it creates a
button which can be clicked to say hello. The content of the template is this:

    
    
    /* jslint */
    isc.Button.create({
      baseStyle: 'navBarButton',
      title: OB.I18N.getLabel('OBEXAPP_HelloWorld'),
      overflow: "visible",
      width: 100,
      layoutAlign: "center",
      showRollOver: false,
      showFocused: false,
      showDown: false,
      click: function() {
        isc.say(OB.I18N.getLabel('OBEXAPP_SayHello', ['${data.name}']));
      }
    })

Some special things in this javascript source:

  * The _/* jslint */_ tells Openbravo to do a check on the generated javascript. Errors are printed in the console or output log. 
  * as you can see, the templates creates a canvas (the Button). It is also allowed to create an array of canvasses. 
  * the title of the button is retrieved through the OB.I18N.getLabel method. This is to support translation, see a later section in this howto for more information. 
  * See the _${data.name}_ part, this is a  freemarker  template construct whereby information is retrieved from a java object. In the Openbravo templating system the component instance is available as the _data_ object. The _${data.name}_ will call the accessor getName on the HelloWorldComponent. 

####  Template Record

The next step is to let Openbravo know that the template exists. This is done
by registering the template in Openbravo in the Template table. The template
maintenance function can be found here: Application Dictionary > User
Interface > Template.

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Navigation_Bar_Component-2.png){: .legacy-image-style}

###  Registering the component as a Navigation Bar Component

The last step is to add the component to the navigation bar. This is done
through the navigation bar components table/window. You can find it through
quick launch or in the menu here: Application Dictionary > User Interface >
Navigation Bar Components.

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Navigation_Bar_Component-3.png){: .legacy-image-style}

###  The result

After executing the above steps you should see a 'Hello World' button in the
navigation bar. Clicking it will popup a small hello message.

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Navigation_Bar_Component-4.png){: .legacy-image-style}

  

###  Static Navigation Bar Components

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
This feature is available starting from ** 3.0PR17Q3  ** .  
---|---  
  
By checking the **Static Component** flag of a a navigation bar component in
_Application Dictionary > User Interface > Navigation Bar Components _ it is
declared as **static** . This kind of components differ from their
counterparts in the way they are created. _Static Navigation Bar Components_
are loaded at the beginning of the _javascript_ content used within the
application and they do not require an extra request to be loaded.

Besides, the content of the template of a _Static Navigation Bar Components_
is defined in a slightly different way:

    
    
    /* jslint */
    {
      className: 'OBApplicationMenuButton',
      properties: {
        title: 'UINAVBA_APPLICATION_MENU',
        initWidget: function () {
          this.Super('initWidget', arguments);
          this.baseData = isc.clone(OB.Application.menu);
        }
      }
    }

Note that the template defines a JSON object with two properties:

  * **className** : the class name of the navigation bar component. 
  * **properties** : contains the set of attributes and functions that will be used to configure the component. 

Retrieved from "
http://wiki.openbravo.com/wiki/How_to_create_a_Navigation_Bar_Component  "

This page has been accessed 16,330 times. This page was last modified on 18
April 2017, at 06:36. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**

