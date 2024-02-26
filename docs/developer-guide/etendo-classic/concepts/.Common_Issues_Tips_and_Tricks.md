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

  

#  Common Issues Tips and Tricks

##  Contents

  * 1  Common Issues, Tips and Tricks 
  * 2  Java Development Issues, Build Path problems 
  * 3  Client side coding, JavaScript 
    * 3.1  javascript error on OB object: OB undefined 
    * 3.2  Use Javascript Linter 
      * 3.2.1  Use ESLint (Starting from PR19Q3) 
      * 3.2.2  Use jslint (Older than PR19Q3) 
    * 3.3  Read this book: JavaScript The Good Parts 
    * 3.4  Debugging JavaScript 
    * 3.5  JavaScript Coding Conventions 
    * 3.6  Client side API 
    * 3.7  Smartclient 
    * 3.8  Working in WebContent 
      * 3.8.1  Visual Studio Code 
    * 3.9  Videos 
      * 3.9.1  Session 1: Introduction to JavaScript 
      * 3.9.2  Session 2: Introduction to SmartClient 
      * 3.9.3  Session 3: Introduction to New Architecture 
    * 3.10  Resources 
  * 4  Weld 
    * 4.1  My component is not found 
    * 4.2  Can I run logic when the application starts? 
  * 5  Data Access Layer 
    * 5.1  SQL Functions in HQL: no data type for node error 
    * 5.2  Getting warning: Unbalanced calls to enableAsAdminContext and resetAsAdminContext 
    * 5.3  How to call a Stored Procedure/Process through the DAL 
    * 5.4  How to read data visible only from a specific Organization 
    * 5.5  When flushing/committing a trigger throws an exception, but I can't see/display the real trigger message 
    * 5.6  Test your HQL: the HQL Query Tool 
    * 5.7  How can I see what SQL is executed? 
    * 5.8  My query does not return my newly created object! 
    * 5.9  My query does not return anything! 
    * 5.10  not-null property references a null or transient value: *.creationDate 
    * 5.11  not-null property references a null or transient value: *.updated 
    * 5.12  org.hibernate.TransientObjectException: object references an unsaved transient instance - save the transient instance before flushing: .... 
    * 5.13  Performance: getting the id of a BaseOBObject 
    * 5.14  Classloading 
    * 5.15  NPE when calling a getter of a Business Object 
    * 5.16  DAL Queries do not return or do not see changes in the database 
    * 5.17  ERROR org.hibernate.LazyInitializationException - could not initialize proxy - no Session 
  * 6  REST Web Services 
    * 6.1  I am getting: 'Caused by: Object Entity(null) is new but not writable' 
    * 6.2  My REST webservice does not return anything 
    * 6.3  Using the REST XML Schema to generate (de-)serialization code 
    * 6.4  Implementing your own webservice 
    * 6.5  Firefox Add-On:Poster, to test webservices 
    * 6.6  I am getting: 'message: "OBUIAPP_ActionNotAllowed" type: "user"' 
  * 7  Application Dictionary Data Model 
    * 7.1  Grids with CLOB fields fail on Oracle 
    * 7.2  Using search references not to show a drop down in non-editable fields 
    * 7.3  Application Dictionary syntax 
      * 7.3.1  Default values 
      * 7.3.2  Display logics 
      * 7.3.3  Read-only logics 
      * 7.3.4  Validations 
  * 8  Build tasks 
    * 8.1  After export.database all the xml headers use double quotes 

  
---  
  
##  Common Issues, Tips and Tricks

This part of the developers guide is dedicated to discussing common issues and
answering frequently asked questions. It tries to provide tips and tricks for
common obstacles encountered when developing and extending Openbravo.

##  Java Development Issues, Build Path problems

To check for a cause and solution check the  Setup for Eclipse guide  and
specifically the section on  Build Path  problems.

##  Client side coding, JavaScript

This section highlights specific topics related to client side coding in
JavaScript.

###  javascript error on OB object: OB undefined

This can happen if the javascript you created is loaded before the general
Openbravo javascript code. To repair this you have to make sure that your
module depends on the User Interface Application module. Based on this the
Openbravo system will load your javascript after the base javascript provided
by Openbravo.

In general if your module depends on javascript provided by other modules, you
should set the correct dependency in the module dependencies.

See  here  for more information.

###  Use Javascript Linter

When you do your own client-side javascript, it would be convenient to use a
linter to detect potential errors and bad practices in your code. Depending on
the ERP version used, we use a different linter

####  Use ESLint (Starting from PR19Q3)

Starting from PR19Q3, Openbravo switched to  ESLint  to check all Javascript
code. In order to use this linter, it is required to install npm in your
machine and run 'npm ci' at the root folder of Openbravo to install all
required tools.

This check can be done either for core or for any module by running the
following script:

    
    
    modules/org.openbravo.client.kernel/jslint

There is also a variant of this script to be run as a mercurial hook:

    
    
    [hooks]
    pretxncommit = modules/org.openbravo.client.kernel/jslint-hg

####  Use jslint (Older than PR19Q3)

For versions after PR19Q3, javascript code check is performed using  jslint  .
At Openbravo we run jslint for all the javascript code being committed to the
repository. We use  JSLint4Java  for this, we enable the automatic check by
adding this to the hgrc file in the .hg directory:

    
    
     
    [hooks]precommit = modules/org.openbravo.client.kernel/jslint/jscheck-hg

If you work in a custom module then from MP31, there is another script which
you should use, add a hook like this in the hgrc file in the .hg directory in
your module:

    
    
     
    [hooks]pretxncommit = ../org.openbravo.client.kernel/jslint/jscheck-module-hg

###  Read this book: JavaScript The Good Parts

JavaScript is not Java. **To really understand JavaScript it is crucial to
read this book** :  JavaScript The Good Parts  .

  

![](/assets/developer-guide/etendo-
classic/concepts/Common_Issues_Tips_and_Tricks-0.png){: .legacy-image-style}

###  Debugging JavaScript

All the static JavaScript code (from all modules) is concatenated into one
large JavaScript file which is stored in the web application directory (in
web/js/gen). The name of the file is based on a hash of the content (see the
image below). You can check out the contents of the file using the browsers
debugger. From there you can debug your code. At Openbravo we use Chromium and
its  debugger  most of the time.

  

![](/assets/developer-guide/etendo-
classic/concepts/Common_Issues_Tips_and_Tricks-1.png){: .legacy-image-style}

  
When working with client side code it is important to learn how to use the
Chromium or Firefox debugger and console. Also check out the network tabs of
the debugging tools to analyze the requests being done by the system. Search
the internet for more information.

**To see non-minimized code in the debugger you need to have the
core/kernel/application modules in development.**

###  JavaScript Coding Conventions

Check out the  JavaScript_Coding_Conventions  for specific tips on coding in
JavaScript.

###  Client side API

Openbravo provides and implements several client side components for sending
requests to the server, internationalization etc. See the  Client Side
JavaScript API  for more information.

###  Smartclient

Openbravo uses the  Smartclient  client side user interface library for
implementing components. To work and development in Openbravo and create new
widgets you need to understand Smartclient. Check out these resources:

  * Smartclient demo 
  * Smartclient forum 
  * Smartclient reference 

It can help to have the Smartclient source code and reference material in your
Eclipse workspace, it is very easy to search source code then. The latest
Smartclient source code is available in this Mercurial repository:
https://code.openbravo.com/erp/mods/org.openbravo.userinterface.smartclient.dev/

###  Working in WebContent

When we are working with javascript files it is common to work directly in
WebContent folder to check changes immediately in the browser. Afterwards, we
copy our changes from WebContent to the source code to be able to push it to
the corresponding repository. The smartbuild task copies the js source code in
WebContent. When working directly in WebContent we could loose our changes
after doing smartbuild so we suggest to do it like this:

####  Visual Studio Code

1.- Working with VS Code, into your workspace launch VS Code Quick Open
(Ctrl+P), paste the following command, and press enter: _ext install
emeraldwalk.RunOnSave_

2.- Launch Show All Commands (Ctrl+Shift+P) and select: _Run On Save: Enable_

3.- Go to Manage(Setting icon) in the botton-left corner and select _Settings_

4.- In User Settings expand Extensions, select _Run On Save command_
configuration. _and click on_ Edit in settings.json _._

5.- Finally, put this inside the settins.json:

    
    
    "emeraldwalk.runonsave": {
            "commands": [
                {
                    "match": "WebContent/web/(?!org.openbravo.userinterface.smartclient|org.openbravo.userinterface.smartclient.dev|userinterface.skin.250to300Comp)",
                    "cmd": "dir=$( echo ${file} | sed -r 's#.*WebContent/web/([^/]+)/.*#\\1#') && file_mod=$(echo ${file} | sed -r 's#WebContent/web/'$dir'/#modules/'$dir'/web/'$dir'/#' ) && cp ${file} $file_mod"
                }
            ]
        }

After doing these steps, if we are working in WebContent with VSCode, it will
copy the file we are editing in the corresponding folder when we save it.
Remember that the copy will be done only when we save the file.

###  Videos

Here you have a list of 3 sessions of _"Introduction to JavaScript"_ , the
sessions were held on Nov. 26th, 30th and Dec 1st 2010.

![](/assets/developer-guide/etendo-
classic/concepts/Common_Issues_Tips_and_Tricks-2.png){: .legacy-image-style} The sessions recorded
and listed here are in _**Spanish** _  
---  
  
####  Session 1: Introduction to JavaScript

  * Part 1:  http://openbravo.emea.acrobat.com/p58999753/ 
  * Part 2:  http://openbravo.emea.acrobat.com/p58999753/ 

####  Session 2: Introduction to SmartClient

  * Part 1:  http://openbravo.emea.acrobat.com/p84569149/ 

####  Session 3: Introduction to New Architecture

  * Part 1:  http://openbravo.emea.acrobat.com/p14323450/ 

###  Resources

  * JavaScript: The Good Parts  http://oreilly.com/catalog/9780596517748/ 
  * JavaScript: The Good Parts (video)  http://video.yahoo.com/video/play?vid=630959 
  * Douglas Crockford — The JavaScript Programming Language  http://developer.yahoo.com/yui/theater/ 
  * JavaScript in Ten (arbitrarily long) Minutes  https://github.com/spencertipping/js-in-ten-minutes 
  * Slides sources (Markdown) used with  showoff  http://bitbucket.org/iperdomo/js-training/get/tip.zip 
  * A nice tutorial on closures and function scoping:  [http://nathansjslessons.appspot.com/ 

##  Weld

###  My component is not found

If your component is not found maybe it falls within the exclusion filter
defined in the Weld module. See  here  for more information.

###  Can I run logic when the application starts?

Yes you can see  here  for more information.

##  Data Access Layer

###  SQL Functions in HQL: no data type for node error

See this  wiki page  for information on how to use SQL functions in HQL.

###  Getting warning: Unbalanced calls to enableAsAdminContext and
resetAsAdminContext

This warning is displayed (together with a stacktrace) when setting
administrator mode is not done correctly. See  this part  of the developers
guide.

###  How to call a Stored Procedure/Process through the DAL

See these  notes  in the howto on calling a process through the DAL.

###  How to read data visible only from a specific Organization

The default DAL behavior (of OBQuery and OBCriteria) is to read information
from all readable organizations. This is all organizations to which the
current role has access. However, sometimes you want to read information which
is only accessible/visible from a specific organization. The code snippet
below shows how this can be accomplished:

    
    
    final OBCriteria<PaymentTerm> obc = OBDal.getInstance().createCriteria(PaymentTerm.class);
    obc.add(Expression.in("organization.id", OBContext.getOBContext().getOrganizationStructureProvider().getNaturalTree(orgId)));
    obc.setFilterOnReadableOrganization(false);
    final List<PaymentTerm> pts = obc.list();

This code snippet shows that you have to add an in expression to the
OBCriteria and then disable the standard organization filtering. A similar
approach can be implemented for OBQuery.

###  When flushing/committing a trigger throws an exception, but I can't
see/display the real trigger message

Hibernate and JDBC will wrap the exception thrown by the trigger in another
exception (the java.sql.BatchUpdateException) and this exception is sometimes
wrapped again. Also the java.sql.BatchUpdateException stores the underlying
trigger exception in the nextException and not in the cause property. The
following method can help you to get to the underlying trigger message:

    
    
    private String getExceptionMessage(Throwable t) {
        if (t.getCause() instanceof BatchUpdateException
            && ((BatchUpdateException) t.getCause()).getNextException() != null) {
          final BatchUpdateException bue = (BatchUpdateException) t.getCause();
          return bue.getNextException().getMessage();
        }
        return t.getMessage();
    }

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |
Openbravo API provides a method called **getUnderlyingSQLException()** on the
**DbUtility** class which already does this checks and covers other cases
also.  
---|---  
  
###  Test your HQL: the HQL Query Tool

Openbravo forge contains a  module  which offers a query tool which allows you
to try a HQL query directly in the Openbravo web interface. The HQL Query Tool
is also available through the central repository. See  here  for the manual of
this utility module.

###  How can I see what SQL is executed?

To see the SQL queries fired by Hibernate, the following log4j property has to
be set (in the WEB-INF/classes/log4j.properties or better in
openbravo/src/log4j.properties):

    
    
    ### log just the SQL
    log4j.logger.org.hibernate.SQL=debug

From **PR19Q1** , the following should be set in WEB-INF/log4j2-web.xml or in
config/log4j2-web.xml:

    
    
    <Loggers>
      ...
      <Logger name="org.hibernate.SQL" level="debug"/>
      ...
    </Loggers>

For seeing the binding of values to query parameters set this property:

    
    
    ### log JDBC bind parameters ###
    log4j.logger.org.hibernate.type=debug

Or if using version **PR19Q1** onwards:

    
    
    <Loggers>
      ...
      <Logger name="org.hibernate.type" level="debug"/>
      ...
    </Loggers>

If it does not work for you, it is possible that the log4j.properties file is
read from another location than you expect. To see where log4j reads its
properties from set this jvm parameter:

    
    
    -Dlog4j.debug

Or this parameter if using version **PR19Q1** onwards:

    
    
    -Dlog4j2.debug=true

###  My query does not return my newly created object!

This can occur when you do not explicitly set the active property to true in
the new business object.

The main Openbravo query classes (  OBCriteria  and  OBQuery  ) automatically
add different filter criteria. One of the filter criteria is the active
property. As a default the query classes will only return objects with active
is true (or 'Y' in the database).

When creating a business object the active property has to be explicitly set
to true (setActive(true)). This ensures that the active-filter will not miss
it in queries.

###  My query does not return anything!

There are cases where Hibernate will perform an inner-join when executing a
query. If there is no related data in the joined table then the complete query
will return nothing.

As an example take the following query:

    
    
    SELECT p.id, p.image FROM Product AS p

This query seems pretty simple. However, in fact the image is a seperately
persisted object and a many-to-one reference from the product to the image
table. This query therefore results in an inner-join to the image table. In
this case that table was empty and nothing was returned.

To solve this issue, the image has to be joined in an outer join:

    
    
    SELECT p.id, p.image FROM Product AS p LEFT OUTER JOIN p.image

###  not-null property references a null or transient value: *.creationDate

This exception is thrown when you try to save a new business object with its
Id set. It makes sense to set an id if you want to control the id-setting (and
not let hibernate create one for you). However, if the id is set then
Hibernate/Openbravo will think it is an existing object and not set the audit
info properties.

To solve this also call setNewOBObject(true) on the new business object. This
signals to Openbravo that the object is new eventhough its id is set.

###  not-null property references a null or transient value: *.updated

Same issue as the previous one.

###  org.hibernate.TransientObjectException: object references an unsaved
transient instance - save the transient instance before flushing: ....

This exception occurs when you save an object which refers to another object
which has not yet been saved. It applies to so-called many-to-one references,
for example from Order to Currency (many orders use the same currency).
Openbravo maps the many-to-one associations without cascading. This is for
performance reasons.

To prevent this exception save the refered-to instance before the refering
instance.

Note that in practice this exception does not happen that often as most
references are from transactional to master data, and master data is
traditionally setup before transactional data is created.

The import data/REST webservices take care of persisting objects in the
correct order so therefore this exception does not occur when importing data
through these processes.

###  Performance: getting the id of a BaseOBObject

To improve performance of single-ended associations, the DAL makes use of the
Hibernate proxy functionality. The Hibernate proxy functionality wraps an
object inside a Hibernate (cglib) proxy object. The Hibernate proxy object
takes care of loading the business object when it is actually accessed and not
before.

In many cases a developer just wants access to the id or entityname of an
object. To prevent loading of the business object when retrieving just this
information, the  DalUtil  class in _org.openbravo.dal.core_ offers a _getId_
method and a _getEntityName_ method. These methods work directly with the
HibernateProxy object and do not load the underlying business object.

###  Classloading

The DAL loads classes when initializing the DAL. The DAL as a default uses the
context class loader of the thread. In some cases this does not work correctly
(for example when using the DAL in Ant). The DAL uses the  OBClassLoader
class to make the classloader configurable. By calling
_OBClassLoader.setInstance_ with your own OBClassLoader you can control the
class loader used by the DAL.

###  NPE when calling a getter of a Business Object

All getters of Openbravo business objects return an Object. This is also the
case for primitive type properties. In this way Openbravo can support null
values in the database (will result in a null value for the property).
However, null values result in NPE's when used directly in expressions. For
example take this code:

    
    
    SystemInformation sys = OBDal.getInstance().get(SystemInformation.class, "0");
    return sys.isEnableHeartbeat();

When the value of 'enableHeartbeat' is null in the database then the call to
isEnableHeartbeat will result in a NPE eventhough the sys variable is set
correctly.

The same will happen when using results of getter-calls directly in numeric
expressions.

###  DAL Queries do not return or do not see changes in the database

This can occur in the following situation:

  1. your program reads objects from the database using the DAL 
  2. then you update the database directly without going through the DAL (either through direct sql or through a stored procedure), the database updates the objects/data you read through the DAL in step 1 
  3. then your program uses the same objects as read in step 1 or you read them again from the database 

The problem you encounter then is that the objects do not reflect the database
state (they are not up-to-date). This is caused by the following:

When Hibernate reads data from the database it is stored in a cache for that
session. This session cache is not auto-updated when data changes in the
database outside of your hibernate session. So when in the last step you read
the objects again from the database, you get the objects from the session-
cache and not from the database.

There are 2 solutions:

  1. clear the session cache completely 

    
    
    OBDal.getInstance().getSession().flush();
    OBDal.getInstance().getSession().clear();

  1. force reread of specific objects 

    
    
    OBDal.getInstance().getSession().refresh(myObject);

The first approach makes sense if there are many updates in the database or
you don't know exactly which objects have changed. The second approach makes
sense if you know exactly which object(s) have changed and there are not that
many.

In case of the first solution you have to note that objects that have been
read (through the DAL) before flushing/clearing can not be used anymore after
flush/clear. These objects need to be re-attached to the session or read
completely new from the database:

    
    
    // reattach an object from the database, only if it is not already part of it
    if (OBDal.getInstance().getSession().contains(myObject)) {
          OBDal.getInstance().getSession().lock(myObject.getEntity().getName(), myObject, LockMode.NONE);
    }
    // or reread it again, this example assumes that the object 
    // is a Business Partner
    BusinessPartner businessPartner = OBDal.getInstance().get(BusinessPartner.class, myPreviouslyReadBP.getId());

When choosing the 'lock' strategy it is important to choose the correct lock
order. First lock the objects which are used by the other objects.

###  ERROR org.hibernate.LazyInitializationException - could not initialize
proxy - no Session

Hibernate will lazily load objects which are referenced from other objects. So
when an object A references an object B, then when reading A from the
database, hibernate will create a so-called proxy object B, which is used by
A. The B proxy object is not initialized (its data is not set), this
initialization is done when B is accessed directly (calling a method on it for
example). To do this initialization hibernate needs the original hibernate
session which was used to read A and create the B proxy object.

The LazyInitializationException occurs when this session is not valid anymore.
This happens for example when OBDal.getInstance().commitAndClose() is called,
this will close and remove the session. If an uninitialized proxy object is
accessed after the commitAndClose call then this exception is thrown.

To prevent this make sure that the objects that you need after the
commitAndClose are all initialized. This can be done using the
Hibernate.initialize(object) call or by calling an arbitrary method on the
object (for example getIdentifier()).

##  REST Web Services

###  I am getting: 'Caused by: Object Entity(null) is new but not writable'

The REST webservice uses the **default role, client and organization** of the
user. The error _Caused by: Object Order(null) is new but not writable_ is
caused by the fact that either the role or the organization of the user do not
allow the writing/creating the entity you are passing in.

See this  topic  in the Openbravo forum.

And see  this issue  for a related bug fix.

###  My REST webservice does not return anything

If your REST webservice only returns this:

    
    
    <ob:Openbravo/>

Then most of the time the user you used to log in is not authorised to see the
requested information. Another reason for not seeing information is that the
system will automatically add client and organization filtering to the REST
query and only show objects which have active==true.

###  Using the REST XML Schema to generate (de-)serialization code

The  REST XML Schema  can be used to generate java or C# code which can be
used to (de-)serialize the REST xml content in a type safe way. One thing to
be aware of is that primitive typed elements (such as a name or description)
have attributes defined in the XML Schema. This means that code generators
will not create a String (or other primitive type) member/accessor but will
instead use a separate generated type to encapsulate the primitive type value.
This separately generated type also holds the other attributes.

See this  forum post  for a discussion around this.

###  Implementing your own webservice

There is a howto on this topic  here  .

###  Firefox Add-On:Poster, to test webservices

To support web service testing, Firefox has a nice add-on:  Poster  . This
add-on allows you to POST/PUT XML to a URL and do GET and DELETE requests.

###  I am getting: 'message: "OBUIAPP_ActionNotAllowed" type: "user"'

You need to add the table you are trying to edit to the user profile in Role
Access > Table Access

##  Application Dictionary Data Model

###  Grids with CLOB fields fail on Oracle

Before 3.0MP4 CLOB fields are not supported in the grid in combination with
Oracle. From 3.0MP4 onwards this is solved.

See these related issues:

  * https://issues.openbravo.com/view.php?id=18517  (solved in MP4) 
  * https://issues.openbravo.com/view.php?id=15556 
  * https://issues.openbravo.com/view.php?id=13153 

As a workaround: do not show the CLOB fields in the grid in Oracle, the form
view should work fine.

###  Using search references not to show a drop down in non-editable fields

For the complete reference about Search reference, read the Search section in
Data Model  document.

A _Search_ reference does not show a drop down list but just text box with the
selected value and a button to call the search next to it. When the field is
non writable the button is not shown and only appears the textbox.

If a column is known to be used always in non-editable fields and it follows
the naming rule defined for _TableDir_ references. It is a good practice not
to set it as _TableDir_ reference but as _Search_ one, in this case is not
necessary to set the _Reference Search Key_ field. Doing this the generated
page will be lighter because instead of generating a drop down list with all
the elements it will just generate a textbox.

###  Application Dictionary syntax

Application Dictionary contains many examples of **default values** ,
**display logics** , **read-only logics** and **validations** syntax. Just
query your database to find out how they are defined (you can execute these
queries inside Openbravo ERP, logged with an user with _System Administrator_
role inside _Application Dictionary || Maintenance || SQL Query_ ). Find more
info about dynamic expressions in the  _Dynamic Expressions_ chapter of the
Developer's Guide.

####  Default values

    
    
    SELECT t.name AS table_name, c.name AS column_name, c.defaultvalue AS default_value
    FROM ad_table t, ad_column c  
    WHERE c.defaultvalue IS NOT NULL
    --AND c.defaultvalue like '%+%'
    --AND c.defaultvalue like '%SQL%'
    AND c.ad_table_id = t.ad_table_id
    ORDER BY t.name, c.name;

  

####  Display logics

    
    
    SELECT w.name AS window, t.name AS tab, f.name AS FIELD, f.displaylogic AS display_logic  
    FROM ad_window w, ad_tab t, ad_field f
    WHERE f.displaylogic IS NOT NULL
    AND w.ad_window_id = t.ad_window_id
    AND t.ad_tab_id = f.ad_tab_id
    ORDER BY w.name, t.name, f.name;

**Example 1** If you want to restrict the access to a child tab based on the
value of a field of its father tab you have to:

  1. Mark the column of the field inside the father's tab as _Stored in Session_ . 
  2. Add to all the fields of the child tab a display logic in the form @Father_Column_Name@ = 'Value' 

See, for instance, how it is done in _Master Data Management || Product Setup
|| Attribute || Attribute >> Attribute Value _ when un-checking _List_ check-
box in _Attribute_ tab by querying:

    
    
    SELECT w.name AS window, t.name AS tab, f.name AS FIELD, f.displaylogic AS display_logic 
    FROM ad_window w, ad_tab t, ad_field f
    WHERE f.displaylogic IS NOT NULL
    AND w.ad_window_id = t.ad_window_id
    AND t.ad_tab_id = f.ad_tab_id
    AND UPPER(t.name) LIKE '%ATTRIBUTE VALUE%'
    ORDER BY w.name, t.name, f.name;

  

####  Read-only logics

    
    
    SELECT t.name AS table_name, c.name AS column_name, c.readonlylogic AS read_only_logic
    FROM ad_table t, ad_column c  
    WHERE c.readonlylogic IS NOT NULL  
    AND c.ad_table_id = t.ad_table_id
    ORDER BY t.name, c.name;

  

####  Validations

    
    
    SELECT t.name AS table_name, c.name AS column_name, vr.code AS validation_rule  
    FROM ad_val_rule vr, ad_table t, ad_column c  
    WHERE c.ad_val_rule_id = vr.ad_val_rule_id  
    AND c.ad_table_id = t.ad_table_id
    ORDER BY t.name, c.name;

##  Build tasks

###  After export.database all the xml headers use double quotes

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |  This
section applies just for versions prior to **3.0PR19Q2** .  
---|---  
  
After export.database you see this in the top of the header:

    
    
    <?xml version="1.0" encoding="UTF-8"?>

when diffing this with the repository you see that the repository has this
(uses single quotes):

    
    
    <?xml version='1.0' encoding='UTF-8'?>

The standard in Openbravo is to use single quotes. To solve this issue copy to
_**src-db/database/lib/wstx-asl-3.0.2.jar** _ file to _lib_ folder inside your
Ant folder.

Once it is copied to the _lib_ folder inside your Ant folder, make sure the
files have execution rights.

Retrieved from "  http://wiki.openbravo.com/wiki/Common_Issues_Tips_and_Tricks
"

This page has been accessed 50,545 times. This page was last modified on 24
January 2020, at 11:08. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  Concepts

**

