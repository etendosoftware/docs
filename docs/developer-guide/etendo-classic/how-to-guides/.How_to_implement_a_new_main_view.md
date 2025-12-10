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

  

#  How to implement a new main view

##  Contents

  * 1  Introduction 
  * 2  Terminology 
  * 3  Example Module 
  * 4  Main flow of view handling 
  * 5  Preferred: Implementing your view in Static javascript 
    * 5.1  Create a javascript file with the class definition of the view 
    * 5.2  Create a view implementation record - handle role access - Add to the menu 
      * 5.2.1  Create a view implementation record 
      * 5.2.2  Role access 
      * 5.2.3  Menu Entry 
    * 5.3  Try it! 
    * 5.4  Working with menu parameters 
    * 5.5  Taking care of history/back button/page refresh 
    * 5.6  A more elaborate view: grid with button, parameterized messages 
  * 6  View API 
  * 7  Dynamically generated javascript 
    * 7.1  Creating a component 
    * 7.2  Creating a template 
    * 7.3  The template source 
    * 7.4  Template Record 
    * 7.5  Register the View Implementation 
    * 7.6  Use the view implementation in a menu entry 
    * 7.7  Try it! 

  
---  
  
##  Introduction

This howto discusses how a new _view_ can be added to Openbravo and made
available through the menu and quick launch options.

A **view** is shown inside the tab of the multi-document-interface (MDI) in
the main content area of the Openbravo user interface. This is illustrated in
the screenshot below which shows several opened tabs, what's shown inside a
tab is called a view.

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_implement_a_new_main_view-0.png){: .legacy-image-style}

  

##  Terminology

This howto uses the following terminology:

  * **view** : is a generic term used to refer to the type of object which is opened through a user action (menu choice for example) and shown inside a tab. 
  * **view type** or **view definition** : corresponds to the concept of a java class, a view type defines the functionality and properties of a view. A view instance is created by calling the create method on the view type. 
  * **view instance** : corresponds to the concept of a java object instance, when a view is created a specific instance of that view is created with its own title or other dynamic information. The view instance is shown in a tab. So multiple tabs can show the same view type but they are different instances. 

##  Example Module

This howto is supported by an example module which shows example of the code
shown and discussed in this howto.

The code of the example module can be downloaded from this mercurial
repository:
https://code.openbravo.com/erp/mods/org.openbravo.client.application.examples/

The example module is available through the Central Repository (See 'Client
Application Examples'), for more information see the  Examples Client
Application  project page.

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |  The
example module also contains implementations of other howtos.  
---|---  
  
![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
When implementing your own components it often makes sense to extend existing
components. Make sure that your module then depends on the module providing
the base types. This ensures that the javascript is loaded in the correct
order. Most of the time it makes sense to add a dependency from your module to
the Client 'User Interface Application/client.application' module  
---|---  
  
##  Main flow of view handling

A view is opened when a user makes a menu choice or uses quick launch (or
through hyperlinks). To obtain and render the view the system goes through a
number of steps:

  * the chosen menu option/quick launch defines the type of view which should be opened and a set of parameters. This is all defined in the Openbravo Menu table. 
  * using the view name Openbravo will check its internal cache of view definition (Smartclient types). 
    * If there is a javascript class with the view name then an instance of the view is created using the parameters which are passed in from the chosen menu option. 
    * if the view is not yet defined then a call to the server is done to check if the view definition can be generated on the basis of a view implementation record. If so it is called and the returned view definition is added to the cache and used in the next step. 
  * a new tab is created, the tab title is obtained from the view instance or from the selected menu. 
  * the view instance is added to the tab 
  * the tab is shown and selected 

The above flow also illustrates that view definitions can be provided in
2-ways to the system:

  * as static javascript resources which are (pre-)loaded on the client when the complete layout is loaded 
  * as dynamic javascript resources which are generated on first use 

The first approach is the preferred approach, the easiest from an
implementation point of view and will probably fit most usecases. The second
approach is best if the view definition depends on dynamic information which
is easier to incorporate on the server (using java) than on the client (using
javascript).

Both implementation methods are discussed below in more detail.

##  Preferred: Implementing your view in Static javascript

Implementing a view as static javascript is the most straight forward method.
Any Smartclient canvas is allowed to be used as a view. When implementing your
view in a static javascript you should take the following steps:

  * Create a javascript file with your view definition and place it in the correct directory 
  * Register the javascript file (and other static resources such as css files) in Openbravo using a  ComponentProvider 
  * Create a view implementation record with the correct name (the same name as the javascript class) 
  * Define a menu entry for the view implementation 

Let's first start with a simple view and go through the steps to create it,
define a view definition record and add it to the menu. Then an example of a
more complex view is shown.

###  Create a javascript file with the class definition of the view

The implementation of the view needs to be done as an extension of Smartclient
canvas class. The most common canvas to extend is the Layout. This is an
example of a layout which contains one label as its content:

    
    
    isc.defineClass("OBEXAPP_HelloWorldLabelView", isc.Layout).addProperties({
      
      labelContent: 'Label content should be passed in as a parameter',
      
      width: '100%',
      height: '100%',
      
      align: 'center',
      defaultLayoutAlign: 'center',
      
      initWidget: function() {
        
        this.children = [isc.Label.create({
          height: 1,
          width: 1,
          overflow: 'visible',
          align: "center",
          valign: "center",
          contents: this.labelContent})];
        
        this.Super("initWidget", arguments);
      }
    });

A short description of this source code:

  * the isc.defineClass method is a Smartclient method call to create a new class, in this case our class (OBEXAPP_HelloWorldLabelView) extends the isc.Layout Smartclient component 
  * the call to addProperties adds specific properties to our class, such as width and height 
  * the labelContent is used later to illustrate the usage of menu parameters 
  * the align properties will force the content of this layout to be center aligned both in height as well as width 
  * the initWidget is like the constructor of the class, it is called when an instance is created. In this case a new child is added a label. The label gets as its text the labelContent of the OBEXAPP_HelloWorldLabelView 

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |

**Note** : For screens that will appear in a standard UI tab, we recommend
extending the  OBBaseView  javascript class instead of the Smartclient layout
(isc.Layout):

    
    
    isc.defineClass("OBEXAPP_HelloWorldLabelView", isc.OBBaseView).addProperties({....});

This will also take care of proper titles on screen refresh and back-button
functionality (see _Taking care of history/back button/page refresh_ section
below).  
  
---|---  
  
The javascript file should be placed inside the module in a directory:
web/[modulejavapackage]/js

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_implement_a_new_main_view-4.png){: .legacy-image-style}

  
The next step is to register the js file in Openbravo. This is done through a
ComponentProvider. For more detailed information on the ComponentProvider
concept visit this  page  .

The example module contains an example of a ComponentProvider, it has this
method to tell Openbravo where to find the javascript file which contains the
view implementation:

    
    
    public List<String> getGlobalComponentResources() {
      final List<String> globalResources = new ArrayList<String>();
      globalResources.add(createStaticResource(
          "web/org.openbravo.client.application.examples/js/example-view-component.js", false));
      globalResources.add(createStaticResource(
          "web/org.openbravo.client.application.examples/js/example-grid-view.js", false));
      globalResources.add(createStaticResource(
          "web/org.openbravo.client.application.examples/js/example-simple-view.js", false));
      return globalResources;
    }

###  Create a view implementation record - handle role access - Add to the
menu

The js file is ready and registered, the next step is to make it accessible
through the menu and quick launch. This requires three steps:

  1. create a view implementation record 
  2. ensure that the correct roles have access 
  3. create a menu entry and place the menu entry in the correct location 

####  Create a view implementation record

Goto the View Implementation Window, either through the menu (Application
Dictionary > User Interface > View Implementation) or through Quick Launch
(type in View Implementation). Create a new record, the most important thing
is that the **Name** of the record should be the same as the class name
defined in the js file (in our case: OBEXAPP_HelloWorldLabelView).

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |  The
field **Name** is the one who must match the class name defined in the .js
file, the _Classname of the view implementation_ is something different and
can be left empty for this example  
---|---  
  
  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_implement_a_new_main_view-6.png){: .legacy-image-style}

####  Role access

Then go to the Role window (General Setup > Security > Role) and check the
View Implementation child tab to check that the intended roles have access:

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_implement_a_new_main_view-7.png){: .legacy-image-style}

  

####  Menu Entry

The view implementation should be accessible from the menu and quick launch.
This is done by entering a menu record and placing the menu entry in the
correct location in the tree. Adding to the menu will automatically make the
view available through quick launch.

Create a new menu record with the action set to 'Open View in MDI', the View
Implementation combo will appear, there choose 'OBEXAPP_HelloWorldLabelView'
(or the view name you have

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_implement_a_new_main_view-8.png){: .legacy-image-style}

  

###  Try it!

Log out and then log in again to refresh the menu (the menu is cached in the
user session). Then access the new view through the menu or through quick
launch. It should show something as illustrated below.

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_implement_a_new_main_view-9.png){: .legacy-image-style}

  
As you can see the text in the middle needs to be replaced. We can control
this with so-called 'Menu Parameters'. This is explained in more detail in the
next secion.

###  Working with menu parameters

Menu parameters allow you to re-use the same class definition in different
menu entries but still ensure different behavior by passing them different
parameters. In this example we will display a different text in the middle of
the new simple view. Go to the menu window and select the menu entry added a
few steps earlier. Then go to the child tab 'Menu Parameters' and add a record
with name: labelContent and a value.

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_implement_a_new_main_view-10.png){: .legacy-image-style}

  
Now log out and log in again, open the view through the menu (don't use any of
the 'recent' links as they store the parameters also), now the result should
be something like this:

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_implement_a_new_main_view-11.png){: .legacy-image-style}

  

###  Taking care of history/back button/page refresh

If you had implemented your view by extending the **isc.Layout** base class,
try to refresh the complete page with the view opened. You will see that the
view get's re-opened but that the tab title is wrong and that the content is
wrong. When opening a view Openbravo will store information to be able to
reconstruct the view when the page is refreshed or when the back/forward
button in the browser is pressed.

The give Openbravo the correct information the view needs to implement a
function (getBookMarkParams):

    
    
    getBookMarkParams: function() {
      var result = {};
      result.viewId = this.getClassName();
      result.labelContent = this.labelContent;
      result.tabTitle = this.tabTitle;
      return result;
    }

Some notes: the getBookMarkParams returns an object which is used to recreate
the view instance when rebuilding the page, as you can see both the tab title
and the labelContent are passed back (as well as the class name of the view).

For a complete overview of the api which Openbravo checks for additional
functionality (opening a help view, preventing multiple tabs of the same
type), see the  View API  section below.

**Note** : To avoid duplicating the above piece of code for your standard
tabbed views, an **OBBaseView** wrapper class is available that includes all
above actions. Hence, instead of extending the isc.Layout class, consider
extending the OBBaseView, e.g.:

    
    
    isc.defineClass("OBEXAPP_HelloWorldLabelView", isc.OBBaseView).addProperties({....});

###  A more elaborate view: grid with button, parameterized messages

In the previous step we created a simple view. This section shows a more
complex example. It is part of the example module in the file example-grid-
view.js. It shows a grid with a button which is enabled when selecting one or
more records in the grid.

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_implement_a_new_main_view-12.png){: .legacy-image-style}

  
The source code of the test view is shown below. It start with the definition
of the grid class and then defines the view itself (further down). The class
name of the view itself is OBEXAPP_SimpleView. So to make use of this view, a
view implementation record with this name (OBEXAPP_SimpleView) should be
created and added to the menu.

    
    
    // This javascript defines a grid and a layout containing the grid 
    // together with a button to show the selected records
     
    // This testgrid shows data from the product table
    isc.defineClass('OBEXAPP_TestGrid', isc.OBGrid);
     
    isc.OBEXAPP_TestGrid.addProperties({
      dataSource: null,
      showFilterEditor: true,
     
      dataProperties: {
        useClientFiltering: false
      },
     
      gridFields: [{
        name: 'name',
        // allow filtering on name
        canFilter: true,
        // filter automatically when the user types
        filterOnKeypress: true
      },
      
      {
        // description is a property of the product
        name: 'description',
        // allow filtering on description
        canFilter: true,
        // filter automatically when the user types
        filterOnKeypress: true
      }],
     
      setDataSource: function(ds) {
        // is called when the datasource is retrieved from the server
        this.Super('setDataSource', [ds, this.gridFields]);
        this.refreshFields();
        this.sort('name');
        this.fetchData();
      },
     
      initWidget: function() {
        // get the datasource, if it is not yet defined
        // it is retrieved from the server and returned
        // Datasources refer to tables using the entity name
        OB.Datasource.get('Product', this, null, true);
        this.Super('initWidget', arguments);
      }
    });
     
    isc.defineClass('OBEXAPP_SimpleView', isc.VLayout);
     
    isc.OBEXAPP_SimpleView.addProperties({
      // do some margins between the members
      membersMargin: 10,
      defaultLayoutAlign: 'center',
      
      initWidget: function() {
        // create a button which is enabled 
        var grid, btn;
        
        // create an instance of the grid
        grid = isc.OBEXAPP_TestGrid.create({
          // add logic to enable/disable the button when
          // the selected records changes
          selectionUpdated: function(record, recordList) {
            if (recordList && recordList.length > 0) {
              btn.setDisabled(false);
            } else {
              btn.setDisabled(true);
            }
          }
        });
        
        // and create a button which refers to the grid
        btn = isc.OBFormButton.create({
            title: OB.I18N.getLabel('OBEXAPP_ClickMe'),
            // let it be enabled when more than one 
            disabled: true,
            action: function() {
              // show the number of selected records
              // illustrates the usage of a parameterized message
              isc.say(OB.I18N.getLabel('OBEXAPP_SelectedRecordsMsg', 
                  [grid.getSelectedRecords().length]));
            } 
          });
        
        // add the grid
        this.addMember(btn);
        this.addMember(grid);
        this.Super('initWidget', arguments);
      },
     
      // the following three methods are related to the view handling
      // api of Openbravo
      isSameTab: function(viewId, params){
        // return false, allows this view to be opened many times
        return false;
      },
     
      // just return the classname and nothing else to be bookmarked
      getBookMarkParams: function() {
        var result = {};
        result.viewId = this.getClassName();
        return result;
      },
      
      // this view does not have a help view
      getHelpView: function(){
        return;
      }
    });

Note that the button click shows a parameterized message. A message can
contain parameters (%0, %1) which are substituted with real values when
showing the message.

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_implement_a_new_main_view-13.png){: .legacy-image-style}

  

##  View API

Any Smartclient canvas can be used as an Openbravo view. When opening a view
Openbravo will check if the view class/instance supports certain methods. If
so then Openbravo will make use of these methods. The methods are reflected in
the OBBaseView type (available from Openbravo 3.0MP3):

    
    
    // = OBBaseView =
    //
    // A class which implements the view api.
    isc.ClassFactory.defineClass('OBBaseView', isc.Layout);
     
    isc.OBBaseView.addProperties({
      
      // ** {{{ OBBaseView.showsItself }}} **
      // If this boolean property is set to true then the Openbravo view manager
      // will not place the view instance in a tab in the main Multi-Document-Interface.
      // Instead it will call the show method on the instance. This makes 
      // it for example possible to define views which are implemented as 
      // popups instead of opened in the main MDI.
      showsItself: false,
      
      // ** {{{ OBBaseView.isSameTab() }}} **
      // Is called by the view manager when opening a view. The view manager
      // will first check if there is already a tab open by calling the 
      // isSameTab method on each opened view. If one of the views returns
      // true then the requested view is opened in that tab (effectively
      // replacing the current open view there). This is needed for cases
      // when a certain view may only be opened once.
      isSameTab: function(viewId, params){
        // a common implementation does this, this allows only 
        // one instance of certain view class to be open at one point 
        // in time.
        // return viewId === this.getClassName();
        // this will allow multiple tabs to be opened:
        return false;
      },
     
      // ** {{{ OBBaseView.getBookMarkParams() }}} **
      // Is used to create a bookmarkable url in the browser's address bar.
      // For each opened view this method is called and the result is added
      // to the address bar. This makes it possible for the user to do 
      // back in the browser, to bookmark the url and to build history in the 
      // browser itself. 
      getBookMarkParams: function() {
        var result = {};
        result.viewId = this.getClassName();
        return result;
      },
      
      // ** {{{ OBBaseView.getHelpView() }}} **
      // This method can return an object containing a view definition. 
      // If this method returns an object then a link is activated in the 
      // help pull-down in the top.
      getHelpView: function(){
        return;
        // an example of returning a view definition, the viewId contains
        // the help view classname, the tabTitle denotes the tab title of the
        // help view
    //    return {
    //        viewId: 'ClassicOBHelp',
    //        tabTitle: this.tabTitle + ' - ' + OB.I18N.getLabel('UINAVBA_Help'),
    //        windowId: this.windowId,
    //        windowType: 'W',
    //        windowName: this.tabTitle
    //    };
      }
     
    });

  

##  Dynamically generated javascript

Instead of creating a static javascript file with a view definition it is also
possible to use dynamically generated javascript. The javascript is generated
at the first usage of the view definition by the user.

To create a dynamically generated view the following parts need to be
implemented:

  * create a java class (the component) which provides the template with information (from the database for example) 
  * create a template which generates the javascript which creates the view definition on the client 

Each of these steps is described in more detail below.

The example module contains a Hello World component with a template
(hello_world_view.js.ftl). This example creates a view with one clickable
button.

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_implement_a_new_main_view-14.png){: .legacy-image-style}

  

###  Creating a component

A component is useful when you want to add runtime information to the view
definition javascript when it gets generated.

_If you don't have the requirement to use dynamic information in the generated
javascript of your component then you don't need to implement a component
(only a template). You can leave the class field empty in the view
implementation record (see below)._

The example module has a hello world component which provides the current
logged in user to the template. The component can be found in the module's src
directory. Here is the code:

    
    
    package org.openbravo.client.application.examples;
     
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

Note: for simplicity we choose to get the user name on the server, this
information is also available on the client in the global OB.User object
(which contains information about the currently logged in user.

###  Creating a template

The template contains the actual javascript. A template consists of two parts:

  1. a template file (the template source) ending on ftl (a  freemarker  extension) which is located in the source tree (in the classpath). 
  2. a record in the template table 

###  The template source

To create the template for your view, create a ftl file in the source tree of
your module. The ftl file should contain plain javascript with possible
freemarker constructs to read information from the component.

As an example, the hello world template can be found in the
org.openbravo.client.application.examples.templates package, it creates a
button which can be clicked. The content of the template is this:

    
    
    isc.defineClass("OBAPPEX_HelloWorldButtonView", "Button").addProperties({
      title: "Click me",
      overflow: "visible",
      width: 100,
      layoutAlign: "center",
      showRollOver: false,
      showFocused: false,
      showDown: false,
      click: function() {
        isc.say(OB.I18N.getLabel('OBAPPEX_SayHello', ['${data.name}']));
      }
    });

Some special things in this template source:

  * as you can see, the templates extends the Smartclient Button class. 
  * the title of the message dialog button is retrieved through the OB.I18N.getLabel method. This is to support translation, see  this wiki page  for more information on this. 
  * See the _${data.name}_ part, this is a  freemarker  template construct whereby information is retrieved from a java object. In the Openbravo templating system the component instance is available as the _data_ object. The _${data.name}_ will call the accessor getName on the HelloWorldComponent. 

###  Template Record

The next step is to let Openbravo know that the template exists. This is done
by registering the template in Openbravo in the Template table. The template
maintenance function can be found here: Application Dictionary > User
Interface > Template.

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_implement_a_new_main_view-15.png){: .legacy-image-style}

  
Some specifics:

  * the component type of the template has to be set to 'UI View Implementation' 
  * the template class path location contains the path to the template file (incl. the file itself) in the source 

For a description of the other fields of the template record, see  here  .

###  Register the View Implementation

To use the view implementation in a menu need to register it in Openbravo.
This is done through the Application Dictionary > User Interface > View
Implementation window.

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_implement_a_new_main_view-16.png){: .legacy-image-style}

  
The client, organization, module, description and active fields are standard
Openbravo fields. The other fields have more specific meanings:

  * name: the name must be unique (it must start with the dbprefix of the module). The name is used to create the view type name on the client. 
  * classname: the classname of a class which extends the org.openbravo.client.kernel.BaseTemplateComponent class. If you don't have any specific component you can leave this field empty. 
  * template: a template set for the UI View Component type. 

_If the view is implemented as static javascript then the classname and
template can remain empty. The name should correspond to the class name used
when calling defineClass (for the example above the name is:
OBAPPEX_HelloWorldLabelView)._

The view implementation can be enabled or disabled by role through the View
Role Access tab. When a new view is created it is automatically enabled for
all roles.

###  Use the view implementation in a menu entry

The next step is to add the view as a menu item. This is done through General
Setup > Application > Menu.

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_implement_a_new_main_view-17.png){: .legacy-image-style}

  
When creating or updating a menu select as an action the _Open View in MDI_
action and select a view implementation in the field which is shown.

###  Try it!

Now log out and log in again and find the menu entry in the menu, select it.
You should see something like the below:

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_implement_a_new_main_view-18.png){: .legacy-image-style}

Retrieved from "
http://wiki.openbravo.com/wiki/How_to_implement_a_new_main_view  "

This page has been accessed 44,889 times. This page was last modified on 16
August 2019, at 12:02. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**

