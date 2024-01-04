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

  

#  Reports obsolete

##  Contents

  * 1  Introduction 
  * 2  iReport Configuration 
    * 2.1  Fonts 
    * 2.2  Scriplet Class 
    * 2.3  Language 
    * 2.4  Openbravo Runtime Environment 
  * 3  Jasper Reports (Standard UI) 
    * 3.1  Parameters 
    * 3.2  Adding images and logos to a report using the ShowImage API 
  * 4  Java servlet reports (UI Manual) 
    * 4.1  When to use this kind of reports 
    * 4.2  How to use this kind of reports 
    * 4.3  Example of this type of report 
      * 4.3.1  Display of the parameter window (method: printPageDataSheet) 
      * 4.3.2  Rendering of the jasper report 

  
---  
  
##  Introduction

Reports are defined in Application Dictionary in the same window as processes:
**Application Dictionary || Report and Process** .

Openbravo ERP support two types of reports: _JasperReports_ with automatically
generated interface and servlet reports which are just a servlet that
generates all the page contents.

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |  This
page contains obsolete information. Please visit the following  **link** to
learn how to create reports since **3.0PR15Q3** version.  
---|---  
  
##  iReport Configuration

iReport  is a graphical tool you can use to create/edit templates (jrxml
files) that will be later processed by JasperReports engine.

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |  You
**must** use  **iReport 4.0.1**  
---|---  
  
###  Fonts

JasperReports introduced a change in version **3.6.1** that it should fail
(throw an exception) when you're trying to use a font that is not available.

    
    
    JasperReports 3.6.1 (2009-10-26, SVN 3170)
    ---------------------------------------------
    - net.sf.jasperreports.awt.ignore.missing.font configuration property added
    to control font availability verifications during report filling and report
    AWT rendering;
    

If you open a JasperReports template and is using a font not available in your
system, you won't see the text of label. To avoid this problem you need to
configure your iReport to skip this check.

  * Go to Tools > Options > JasperReports Properties 
  * Set to **true** the property _net.sf.jasperreports.awt.ignore.missing.font_

![](/assets/developer-guide/etendo-classic/concepts/Reports_obsolete-2.png){: .legacy-image-style}

###  Scriplet Class

Openbravo 3 doesn't support out of the box any Scriplet class. Make sure your
template doesn't contain any class in the template properties.

  * _Window_ > _Report Inspector_
  * Scroll down in the **More** section 
  * Make sure the **Scriptlet class** property is empty 

![](/assets/developer-guide/etendo-classic/concepts/Reports_obsolete-3.png){: .legacy-image-style}

###  Language

The default language for expressions in Openbravo 3 is **Java** . Make sure
that your template uses Java as language expression.

  * _Window_ > _Report Inspector_
  * Scroll down to the **More** section 
  * Pick **Java** in the Language property 

![](/assets/developer-guide/etendo-classic/concepts/Reports_obsolete-4.png){: .legacy-image-style}

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
**iReport** , it suffices just to import this file into **iReport** . The
import of a .jar file within iReport is done via _**Tools > Options >
Classpath > Add JAR ** _ .

##  Jasper Reports (Standard UI)

Openbravo 3 can automatically generate the user interface for requesting the
parameters for a jasper report. The UI is similar to the one generated for
processes.

![](/assets/developer-guide/etendo-classic/concepts/Reports_obsolete-5.png){: .legacy-image-style}

The first step is to create the report template. This is explained in the
How_to_create_a_Report  .

These reports are defined by:

  * **UI Pattern** : Set _Standard_ to automatically generate the UI. 
  * **Jasper Report** : Set this field to _Yes_ . 
  * **Report** : Set this field to _No_ . 
  * **JR Template name** : It is the full path to the main Jasper Report template file ( _jrxml_ ) for the report. To make reference to the server root use _@basedesign_ , thus a template file located in _src/org/openbravo/erpCommon/ad_reports/ReportPurchaseOrder.jrxml_ should have as _JR Template name_ _@basedesign@/org/openbravo/erpCommon/ad_reports/ReportPurchaseOrder.jrxml_ . 

###  Parameters

Parameters can be defined for this kind of reports, it is done in the same way
as  parameters for processes  . These parameters must be managed by the
template.

###  Adding images and logos to a report using the ShowImage API

You can use the new Image BLOB reference to display an image for a specific
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

##  Java servlet reports (UI Manual)

The second type of reports are the ones implemented as regular Java servlets.
Here Openbravo does not manage the parameter window and does also not manage
the actual report rendering automatically. Instead the report definition just
defines how to call the servlet which then has to manage all of this tasks on
its own.

###  When to use this kind of reports

This kind of report is used when either the automatic UI generation of
Openbravo is not sufficient or when the report should be produced by a
different reporting system than Jasper reports. An example for the first case
is shown further down.

###  How to use this kind of reports

These reports are defined by:

  * **UI Pattern** : Set Manual 
  * **Report** : Set this field to Yes. 
  * **Jasper Report** : Set this field to No. 
  * **Process Class** (tab): specify the Java class (servlet) implementing the report 
  * **Process Mapping** (sub-tab of Process Class (tab)): add all relative URLs which should be mapped to this servlet. Normally each entry here corresponds to an HTML template. 

###  Example of this type of report

As an example for this the report **Discount Invoice Report** ( _Sales
Management || Analysis Tools || Discount Invoice Report || Discount Invoice
Report_ ) will be used.

This report does not use the generated UI as its parameter window uses the
**Business Partner Multiple Selector** . Using this selector more than one
Business Partner can be selected to be used in a report. However the _Standard
UI_ does not support this type of selector, so that the parameter window has
to be coded manually.

This report consists of a number of individual files in the
_org/openbravo/erpCommon/ad_reports_ folder:

  * ** ReportInvoiceDiscountJR.java  ** : This file is the Java servlet implementing the display of the parameter window and the start of the Jasper report rendering. 
  * ** ReportInvoiceDiscount_data.xsql  ** : This file is the sqlc input and contains the SQL statements needed for this report. 
  * ** ReportInvoiceDiscountJR.html  ** : This file is the HTML template used by XmlEngine to render the parameter window. 
  * ** ReportInvoiceDiscountJR.xml  ** : This file is the XML control file used by XmlEngine to render the parameter window. 
  * ** ReportInvoiceDiscountJR.jrxml  ** : This file is the Jasper report source file implementing the real report output. 

This example focuses on the first four files, as the jrxml file has not
special changes compared to a report with a Standard UI.

The controlling part of our report is the Java servlet. It serves two purposes
in the report:

  1. Displaying the parameter window with the various widgets and a button to start the report execution. 
  2. The report execution itself. 

When looking at the source code of the servlet the main entry point is the
**doGet** method. In this method the distinction between the different actions
is made and the execution flow splits according to the requested action.

When the report is called from the menu then the servlet is called with the
command **DEFAULT** . In the doGet method this is checked and after reading
some necessary parameters the execution continues in the mod
**printPageDataSheet** . This method is responsible of displaying the
parameter window with its various widgets and the HTML button which starts the
report rendering.

####  Display of the parameter window (method: printPageDataSheet)

This method needs to generate and output the HTML code needed to display the
parameter window. In Openbravo a template engine named XmlEngine is used to
produce the HTML output based on templates and data inserted at runtime.

Find more information regarding XmlEngine in the  _XmlEngine_ _article._

The following stripped down version of the _printPageDataSheet_ method shows
the general use of XmlEngine:

    
    
    // load the HTML template and xml control file
    XmlDocument xmlDocument = xmlEngine.readXmlTemplate(
            "org/openbravo/erpCommon/ad_reports/ReportInvoiceDiscountJR").createXmlDocument();
     
    // set parameter and data for the template
    xmlDocument.setParameter("ccurrencyid", strCurrencyId);
    xmlDocument.setData("reportC_Currency_ID", "liststructure", comboTableData.select(false));
    ...
     
    // produce html output and write the servlet response
    response.setContentType("text/html; charset=UTF-8");
     
    PrintWriter out = response.getWriter();
    out.println(xmlDocument.print());
    out.close();

What is now missing to be able to render the widgets is how the HTML code does
look like for each and which parameter need to be specified for the widget by
the Java servlet. The description of the widgets used in Openbravo can be
found in the  skins  article.

The first four common elements used in any page which is shown inside the main
Openbravo window are:

  1. NavigationBar 
  2. LeftTabsBar 
  3. ToolBar 
  4. WindowTabs 

The **NavigationBar** is the widget which displays the Go back and reload
button and the Breadcrumb (Location of the current window in the menu
structure). The following Java snippet prepares the HTML for this widget and
passes it to the XmlEngine via the parameter toolbar.

    
    
    ToolBar toolbar = new ToolBar(this, vars.getLanguage(),
        "ReportInvoiceDiscountReportInvoiceDiscountJR", false, "", "", "", false, "ad_reports",
        strReplaceWith, false, true);
    toolbar.prepareSimpleToolBarTemplate();
    xmlDocument.setParameter("toolbar", toolbar.toString());

This parameter for the template is defined in the xml control file of the
report:

    
    
    <PARAMETER id="paramToolBar" name="toolbar" default=""/>

This tag defines a parameter for XmlEngine with the name toolbar and a default
value "". The value of the parameter will then be placed at the position of an
element in the HTML template with id="paramToolBar".

    
    
    <div class="Main_ContentPane_ToolBar" id="paramToolBar"></div>

In a similar fashion the HTML for the **LeftTabsBar** is prepared. This widget
is shown in the vertical space between the menu and the content area. Example
for it are the buttons for switching between Form View and Grid View in the
normal generated windows.

The **ToolBar** widget is responsible for showing the different button just
below the NavigationBar. In our example this part has no visible buttons.

Finally the **WindowTabs** widget renders the area where in generated windows
the different tabs of the windows are shown. In our example report it just
shows the report name at the right side of the window.

The next common widget in most of the windows is the **MessageBox** part which
displays feedback information like infos, warnings and error message to the
user.

As a user visible interaction can last several individual server requests the
info if a message should be shown and the message details are stored in the
server side session. The key for this data needs to be unique per window and
is the report (filename) in this example. The following Java snippets
retrieves this message (if one is available) and sets it as XmlEngine
parameters to be displayed in the HTML page.

    
    
    OBError myMessage = vars.getMessage("ReportInvoiceDiscountJR");
    vars.removeMessage("ReportInvoiceDiscountJR");
    if (myMessage != null) {
      xmlDocument.setParameter("messageType", myMessage.getType());
      xmlDocument.setParameter("messageTitle", myMessage.getTitle());
      xmlDocument.setParameter("messageMessage", myMessage.getMessage());
    }

As an example of how an individual widget can be used the combo box for
displaying and selecting a currency will be explained.

Our HTML template needs two different inputs to render this widget. First one
is the list of entries which includes both the internal value for each element
and the user visible text for each. The user visible text should be translated
according to the currently selected UI language.

The second needed input is which entry should be selected when rendering the
page. In our example report this default value is the base currency of the
currently selected client. The following snippet shows the needed Java code
which creates the data for both inputs.

    
    
    xmlDocument.setParameter("ccurrencyid", strCurrencyId);
    try {
      ComboTableData comboTableData = new ComboTableData(vars, this, "TABLEDIR", "C_Currency_ID",
          "", "", Utility.getContext(this, vars, "#AccessibleOrgTree", "ReportInvoiceDiscountJR"), Utility
              .getContext(this, vars, "#User_Client", "ReportInvoiceDiscountJR"), 0);
      Utility.fillSQLParameters(this, vars, null, comboTableData, "ReportInvoiceDiscountJR",
              strCurrencyId);
      xmlDocument.setData("reportC_Currency_ID", "liststructure", comboTableData.select(false));
      comboTableData = null;
    } catch (Exception ex) {
      throw new ServletException(ex);
    }

This snippets uses the **ComboTableData** class to get the list of currency
values including translation to be by the combobox widget. The result list is
passed to the template with the _setData_ method. The default value is passed
as usual with a _setParameter_ call.

Finally the HTML template in the example report contains a button which is
used to start the rendering of the Jasper report. This report has the
following Javascript method call assigned to _onClick_ .

    
    
    openServletNewWindow('FIND', true, 'ReportInvoiceDiscountJR.html', 'ReportInvoiceDiscountJR', null, false, '700', '1000', true);

This will first call the **validate** method defined in the HTML template. It
is used to check if all needed inputs have been provided by the user. In our
example report it checks if the mandatory fields have been filled.

Then the relative URL **ReportInvoiceDiscountJR.html** will the called with
the **FIND** command value. The output of this request will be shown in a new
pop-up window as the Javascript method name indicates. This will again call
into the same servlet, but now the _doPost_ method will dispatch the call to
the **printPageDataHtml** Java method which start the report rendering.

####  Rendering of the jasper report

The **printPageDataHtml** has the responsibility of finally rendering the
Jasper report. The following snippet gives a short overview about the needed
task on the Java side:

    
    
    // relative report filename, same as in automatic UI case
    String strReportName = "@basedesign@/org/openbravo/erpCommon/ad_reports/ReportInvoiceDiscountJR.jrxml";
     
    // output format: html,pdf,xls
    String strOutput = "html";
     
    // get needed data from database
    ReportInvoiceDiscountData[] data = null;
    data = ReportInvoiceDiscountData.select(this, strCurrencyId, Utility.getContext(this, vars,
        "#User_Client", "ReportInvoiceDiscountJR"), Utility.getContext(this, vars, "#AccessibleOrgTree",
        "ReportInvoiceDiscountJR"), strDateFrom, strDateTo, strcBpartnerId, (strDiscount
        .equals("N")) ? "" : "discount");
     
    // pass extra parameters to jasper report template
    HashMap<String, Object> parameters = new HashMap<String, Object>();
    String strSubTitle = Utility.messageBD(this, "From", vars.getLanguage()) + " " + strDateFrom
         + " " + Utility.messageBD(this, "To", vars.getLanguage()) + " " + strDateTo;
    parameters.put("REPORT_SUBTITLE", strSubTitle);
     
    // start jasper report rendering
    renderJR(vars, response, strReportName, strOutput, parameters, data, null);

The real rendering is started by the last method call: **renderJR** .

This method reads the report template (a jrxml file) and runs it through the
Openbravo translation engine. Then the Jasper template is compiled and the
provided data (here read from the database) and other parameters are sent to
the Jasper engine. Finally the finished report will be exported to the
specified format (html, xls or pdf) and sent to the browser.

Retrieved from "  http://wiki.openbravo.com/wiki/Reports_obsolete  "

This page has been accessed 4,901 times. This page was last modified on 11
March 2016, at 07:35. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  Concepts

**

