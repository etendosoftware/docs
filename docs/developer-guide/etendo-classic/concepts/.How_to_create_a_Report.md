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

  

#  How to create a Report

##  Contents

  * 1  Objetive 
  * 2  Acknowledgments 
  * 3  Setting up Jaspersoft Studio 
    * 3.1  Configuring Jaspersoft Studio 
    * 3.2  Setting up Classpath 
  * 4  Creating the Template 
    * 4.1  Openbravo Runtime Environment 
    * 4.2  Adding images and logos to a report using the ShowImage API 
  * 5  Registering the Report in Application Dictionary 
    * 5.1  Creating the Report 
    * 5.2  Creating the Menu record 
  * 6  Compiling 
  * 7  Testing the Report 
  * 8  Further Details 
    * 8.1  Layout 
    * 8.2  Configuring Cell Type in XLS Reports 
    * 8.3  Creating a Report Using Report and Process 
    * 8.4  Creating a Reports in old releases 
    * 8.5  Report Compilation 
    * 8.6  Barcodes 
  * 9  Migration to JasperReports 6.17.0 

  
---  
  
##  Objetive

The goal of this how to is to describe the steps required to create a new
report in Openbravo 3. The example explained is a simple report with a list of
products.

##  Acknowledgments

Before starting make sure that you have read the  prerequisite knowledge
article. And you are confident with Openbravo  modularity concepts

##  Setting up Jaspersoft Studio

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |
Jaspersoft Studio design client is supported since **3.0PR15Q3** . For older
releases check  this section  .  
---|---  
  
![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |  Use
Jaspersoft Studio version 6.17.0 from **3.0PR22Q1** onward as it is the
recommended version.  
---|---  
  
You need to download Jaspersoft Studio, a graphical tool that allows you
create and modify JasperReports templates (.jrxml files).

  * Download  Jaspersoft Studio  version **6.0.0** (v6.0.0). If using a higher version then it is necessary to ensure that the reports are generated for the **JasperReport 6.0.0** version. More info can be found  here  . 
  * On Linux: just download the .tgz file and uncompress it, execute the binary _Jaspersoft Studio_ located inside the main folder 
  * On Windows: Download and execute the .exe file 

###  Configuring Jaspersoft Studio

Some properties of Jaspersoft Studio need to be modified in order to work
properly. In short, you need to make sure:

  * You modified the JasperReport property _net.sf.jasperreports.awt.ignore.missing.font_ and set it to **true** . It can be changed in Properties -> Jaspersoft Studio -> Properties 
  * **Not** use any **Scriplet** class 
  * Use **Java** as default expression language 

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |
Jasperreport can be used in hw manager, but the version should be 1.0.2801 or
higher  
---|---  
  
###  Setting up Classpath

In Jaspersoft Studio, each report is supposed to be part of a project. So, you
first need to create a new project ( _File > New > Project _ ).

The project has a classpath, and here is where you can add the jars you need.

  * Right-click on the project name: _Properties > Java Build Path _
  * Move to **Libraries** tab 
  * Click **Add External Jars** button 
  * Add the desired library. 
  * Click **OK**

##  Creating the Template

  * Go to **File** > **New**
  * Pick **Jasper Report**
  * The **New Report Wizard** will be opened 

![](/assets/developer-guide/etendo-
classic/concepts/How_to_create_a_Report-3.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-
classic/concepts/How_to_create_a_Report-4.png){: .legacy-image-style}

  * Select a Report Template, ( _Blank_ following our example) 
  * Define a Report Name 
  * Define the file Location in the project. 

Later on we will copy this .jrxml file inside our Openbravo module that is
going to keep our Report and the required configuration in the Application
Dictionary also.

  * Define the Report Data Source: by clicking on "New", a new database connection can be configured using the **Data Adapter Wizard**
  * Click **New**
  * Pick **Database JDBC Connection** and click _Next_
  * Fill all the fields 
    * **Name:** openbravo (or any name you like, e.g. pi) 
    * **JDBC Driver:** PostgreSQL (org.postgresql.Driver). In this case we'll use PostgreSQL 
    * **JDBC URL:** jdbc:postgresql://localhost:5432/openbravo where _5432_ is the port where PostgresSQL is running and _openbravo_ is the SSID of our database 
    * **Username:** tad (you can check your username/password in  Openbravo.properties  configuration file) 
    * **Password:** tad 
  * Click Finish button to generate the JDBC Connection 
  * Test your connection 
  * Save 

![](/assets/developer-guide/etendo-
classic/concepts/How_to_create_a_Report-5.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-
classic/concepts/How_to_create_a_Report-6.png){: .legacy-image-style}

Now we have to configure the query: we are going to list the products present
in the database.

  * Right-click on the Report Outline menu, and select **Dataset and Query** . Here is where we have to set the query of the report and it is also possible to switch between the available database connections in case we want to test the query. 

![](/assets/developer-guide/etendo-
classic/concepts/How_to_create_a_Report-7.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-
classic/concepts/How_to_create_a_Report-8.png){: .legacy-image-style}

  * The products are stored in the M_Product table 
    
        SELECT m_product_id, value, name FROM m_product

  * We have to add the fields based on your query which we want to use in the report, so we are going to add: 
    * m_product_id 
    * value 
    * name 

![](/assets/developer-guide/etendo-
classic/concepts/How_to_create_a_Report-9.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-
classic/concepts/How_to_create_a_Report-10.png){: .legacy-image-style}

  * Click OK 

  * Remember to clear the Scriptlet class and modify the Language for expressions 
  * Right-click on the Report Outline menu, and select **Show Properties** . 
  * In the report properties in the right, look for the following: 
    * Clear the Scriptlet class 
    * Choose Java as Language 
  * Save your changes 

![](/assets/developer-guide/etendo-
classic/concepts/How_to_create_a_Report-11.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-
classic/concepts/How_to_create_a_Report-12.png){: .legacy-image-style}

Let's now design the Report Layout

  * Put a static text as report title: _Product List_
  * Place the fields in the **Detail** band and a title in the **Column Header** band 
  * Save your changes 

![](/assets/developer-guide/etendo-
classic/concepts/How_to_create_a_Report-13.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-
classic/concepts/How_to_create_a_Report-14.png){: .legacy-image-style}

  

  * Switch to the **Preview** subtab to get a report preview 

![](/assets/developer-guide/etendo-
classic/concepts/How_to_create_a_Report-15.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-
classic/concepts/How_to_create_a_Report-16.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |  Note: It
is recommended to use Dejavu fonts in jasper reports because this fonts
support most of the characters in almost all languages​​. Besides, Dejavu
typography is the family of fonts that Openbravo included in jasperreports-
fonts library.  
---|---  
  
###  Openbravo Runtime Environment

The standard reports in Openbravo ( _src/org/openbravo/erpReports_ ) make use
of several methods that reside inside the **Openbravo Runtime Environment** ,
which cannot be executed at design time. For this reason, we provide the
following ** .jar file  ** that encapsulates the following adapted methods of
the _org.openbravo.erpCommon.utility.Utility_ Class:

  * **public static BufferedImage showImageLogo** : returns a logo image that is already included in the JAR archive 
  * **public static String applyCountryDateFormat** : always returns the date formatted in this pattern dd-MM-yyyy 
  * **public static DecimalFormat getCountryNumberFormat** : just returns the same DecimalFormat received as parameter 

For this, to be able to preview the standard Openbravo reports from
**JasperStudio** , it suffices just to import the .jar file into the classpath
of the project within JasperStudio.

###  Adding images and logos to a report using the ShowImage API

You can use the Image BLOB reference to display an image for a specific
report, or one of the Company logos in the application. First you need to add
an image object to your report, set the expression class to "java.awt.Image"
and the expression image to a call to the ShowImage function of the Utility
class (if you want it to display a standard ImageBLOB image reference, that
corresponds to a field added to a tab), or to the ShowImageLogo function if
you want to display the logo of an Organization or Client.

Images loaded with this method must not have alpha channel. A transparency
layer is not supported by the function that loads images in Jasper Reports.

  * If you want to use the ShowImage function, you need to make the expression image look like: 
    * org.openbravo.erpCommon.utility.Utility.showImage("IMAGEID") 

IMAGEID needs to be the UUID of the image you want to show. You could set this
value using a Jasper parameter.

  * If you want to use the ShowImageLogo function to show one of the logos, you have several options. 
    * This one will show the Company logo at System level: 
      * org.openbravo.erpCommon.utility.Utility.showImageLogo("yourcompanylogin") 
    * This one will show the Company log at Client level (the client used will be the one the user logged at): 
      * org.openbravo.erpCommon.utility.Utility.showImageLogo("yourcompanymenu") 
    * This one will show the Company logo at Organization level: 
      * org.openbravo.erpCommon.utility.Utility.showImageLogo("yourcompanydoc", "ORGANIZATIONID") 

ORGANIZATIONID needs to be the UUID of the Organization whose log you want to
show. You could set this value using a Jasper argument. An example could be
**org.openbravo.erpCommon.utility.Utility.showImageLogo("yourcompanydoc",
"4387D62C6486481AB3D148442A6AD34E")** being 4387D62C6486481AB3D148442A6AD34E
the organization ID.

##  Registering the Report in Application Dictionary

###  Creating the Report

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |  This
feature is available from **3.0PR15Q2**  
---|---  
  
From **3.0PR15Q2** it is possible to create a report using a process
definition. For more information see  here  .

  * Using the System Administrator role 
  * Using the quick-launch, open: **Process Definition** window 
    * You can find it in the menu: Application Dictionary > Process Definition 

  * Create a new record 
  * Fill all required fields 
    * **Module:** Pick your module 
    * **Search Key:** OBPF_ProductList (Is a best practice to start with your module's  DB_Prefix  ) 
    * **Name:** Product List 
    * **UI Pattern:** Report (Using JR templates) 
    * **Data Access Level:** Client/Organization 
    * **Handler** : use the default _org.openbravo.client.application.report.BaseReportActionHandler_

![](/assets/developer-guide/etendo-
classic/concepts/How_to_create_a_Report-19.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-
classic/concepts/How_to_create_a_Report-20.png){: .legacy-image-style}

We must copy the .jrxml template file generated with Jaspersoft Studio into
our module. When using Process Definition to generate a Report, templates need
to be stored in the web folder of the module. In our example we place it in
the following location: _/web/org.openbravo.platform.features/jasper_

  * Navigate to the **Report Definition** tab 
  * Fill the PDF template field with the location of the .jrxml file 

  

![](/assets/developer-guide/etendo-
classic/concepts/How_to_create_a_Report-21.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-
classic/concepts/How_to_create_a_Report-22.png){: .legacy-image-style}

###  Creating the Menu record

  * Using the System Administrator role 
  * Open the Menu window 
  * Create a new record 
  * Fill all required fields: 
    * **Module:** Your module 
    * **Name:** Name of the menu entry (Product List) 
    * **Description:** Description of the action related to the menu entry 
    * **Action:** Pick Process Definition 
    * **Process Definition:** Pick your Process Definition (Product List) 

![](/assets/developer-guide/etendo-
classic/concepts/How_to_create_a_Report-23.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-
classic/concepts/How_to_create_a_Report-24.png){: .legacy-image-style}

##  Compiling

After you have registered the report and menu entry in the Application
Dictionary, you need to compile to generated the the necessary code.

    
    
    ant smartbuild

Once the compilation has completed, refresh your  Eclipse project  , and
restart your tomcat server.

##  Testing the Report

If you have completed all the steps, you should be able to open your Product
List report form the quick-lauch, or menu entry.

![](/assets/developer-guide/etendo-
classic/concepts/How_to_create_a_Report-25.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-
classic/concepts/How_to_create_a_Report-26.png){: .legacy-image-style}

##  Further Details

###  Layout

For information on how JasperReports handles the layout check  Making HTML,
XLS or CSV friendly reports

Also, a tutorial with the basics of how to design a report can be found  here
.

###  Configuring Cell Type in XLS Reports

Starting from **3.0PR15Q3** , by default, Openbravo reporting engine exports
the XLS data as strings. This is done in order ensure that the exported data
can be read after opening the report with the vast majority of spreadsheet
applications.

If we want to have a particular format in a cell of our XLS report, and for
example, display numbers inside a numeric cell, this default configuration can
be overridden at template level.

To override this configuration, the following must be done inside the .jrxml
report template:

  1. Add the **net.sf.jasperreports.export.xls.detect.cell.type** property with true as its value. 
  2. Add a **pattern** for the text field that will be displayed in the XLS cell. With ** <pattern> ** tag a fixed pattern can be set and with the ** <patternExpression> ** tag it is possible to define a dynamic pattern. 

Please note that the decimal and thousands **separators** used for the numeric
cells exported in this way, will be those defined inside the spreadsheet
program itself (LibreOffice Calc, Excel,...). An example of report which
applies this configuration can be found  here  .

###  Creating a Report Using Report and Process

**Report and Process** window was the habitual way to define reports before
PR15Q2, as the **Process Definition** option was not available. In the
following  tutorial  you can find an example about how to create a Report in
this way.

###  Creating a Reports in old releases

Before **3.0PR15Q3** version, another report design client was used, called
**iReport** .

To get more information about this and further details on reporting in old
releases, you can go  here  .

###  Report Compilation

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |  This
feature is available starting from ** 3.0PR18Q3  ** .  
---|---  
  
When printing a report in the application, it is previously compiled at
runtime. The result of this report compilation is cached if there are no
modules in _in development_ status.

Besides, it is possible to handle the state of this cache through a  JMX
extension. Thus, this extension allows to:

  * See if the cache is enabled. 
  * Enable/Disable the cache. 
  * See the list of reports whose compilation is stored in cache. 
  * Clear the cache contents. 

###  Barcodes

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |  This
feature is available starting from ** 3.0PR19Q2  ** .  
---|---  
  
It is possible to generate barcodes from JasperReports, using barcode4j or
barbecue libraries. These libraries are included in
Barcode_generation_in_reports  module.

In Platform Features module there is an example of a report making use of
different barcode styles, see here the  jrxml template  .

  

##  Migration to JasperReports 6.17.0

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |  This
feature is available starting from ** 3.0PR22Q1  ** .  
---|---  
  
When updating from JasperReports 6.0.0, several steps are required to make the
JasperReports file behave properly in the 6.17.0 version.

This warning may appear in the 6.0.0 reports when updating: WARNING: The
'isStretchWithOverflow' attribute is deprecated. Use the 'textAdjust'
attribute instead.

To fix the warnings, there is a tool provided  here  . The tool updates all
the jasperreports from a provided directory/folder to the updated version
6.17.0.

  1. Clone the repository: git clone  https://gitlab.com/openbravo/tools/platform/jrxmlUpdateTool 
  2. cd jrxmlUpdateTool 
  3. Clone or copy the module to update jasperreports from: for example -> cp /path/to/openbravo/modules/moduleWithReports . 
  4. Execute: ant update -DreportPath=/path/to/your/reports 
  5. All modified reports will be available in jrxmlUpdateTool/build/reports, they keep original file/folder structure. To copy them back to the original folder: cp build/reports/* /path/to/your/reports -r 
  6. Check the changes(git status, git diff), then commit and push to the corresponding branch/fork. 

Retrieved from "  http://wiki.openbravo.com/wiki/How_to_create_a_Report  "

This page has been accessed 77,753 times. This page was last modified on 20
November 2023, at 08:31. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**

