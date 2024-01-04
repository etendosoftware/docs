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

  

#  How to Create Your Own Import Process with IDL

##  Contents

  * 1  Introduction 
  * 2  Objective 
  * 3  Step by step explanation 
    * 3.1  Installing Required Modules 
    * 3.2  Creating Process File 
    * 3.3  Registering the Process 

  
---  
  
##  Introduction

The import loader process is used to load data into the openbravo windows from
input files. Openbravo is providing the options to load product, business
partner, etc., Now we have the option of creating import process for our own
modules with a simple java file(Refer [  [1]  ]). Right now this process reads
data from csv file(The Input format is parsed using the file
IdlServiceJava.java file). This can also be extended to read input from other
formats by creating a service file similar to IdlServiceJava. To try this out
you need the Professional Subscription License.

##  Objective

This how-to will focus on creating an import loader process in Openbravo ERP
and also explain, with an example, how to load data in custom modules using
the import loader process.

##  Step by step explanation

###  Installing Required Modules

  * Activate the Professional subscription License. 
  * Go to General Setup -> Application -> Module Management -> Add Modules 
  * Search and install the following modules. 
    * Initial Data Load (Refer [  [2]  ]) 
    * Initial Data Load Extension for Java (Refer[  [3]  ]) 

###  Creating Process File

    
    
     
     
     package com.fugoconsulting.xyzz.module.template.erpCommon.ad_process;
     
     import org.openbravo.idl.proc.Parameter;
     import org.openbravo.idl.proc.Validator;
     import java.text.DateFormat;
     import java.text.SimpleDateFormat;
     import java.text.ParseException;
     import java.math.BigDecimal;
     import java.util.Date;
     import org.apache.log4j.*;
     
     import org.openbravo.base.exception.OBException;
     import org.openbravo.base.provider.OBProvider;
     import org.openbravo.base.structure.BaseOBObject;
     import org.openbravo.dal.service.OBDal;
     import org.openbravo.erpCommon.utility.Utility;
     import org.openbravo.idl.proc.Value;
     import org.openbravo.module.idljava.proc.IdlServiceJava;
     import com.fugoconsulting.xyzz.module.template.XYZZFrequency;
     
     /**
     *
     * @author Pandeeswari@FugoConsulting
     */
     public class ImportFrequency extends IdlServiceJava {
     
     private static Logger log=Logger.getLogger(ImportFrequency.class);
     
     @Override
     public String getEntityName() {
     return "Simple Frequency";
     }
     
     @Override
     public Parameter[] getParameters() {
     return new Parameter[] {
     new Parameter("Organization", Parameter.STRING),
     new Parameter("SearchKey", Parameter.STRING),
     new Parameter("Name", Parameter.STRING),
     new Parameter("Description", Parameter.STRING),
     new Parameter("Factor", Parameter.STRING),
     new Parameter("Date", Parameter.STRING) };
     }
     
     @Override
     protected Object[] validateProcess(Validator validator, String... values) throws Exception {
     validator.checkOrganization(values[0]);
     validator.checkNotNull(validator.checkString(values[1], 40), "SearchKey");
     validator.checkNotNull(validator.checkString(values[2], 60), "Name");
     validator.checkString(values[3], 255);
     validator.checkBigDecimal(values[4]);
     validator.checkDate(values[5]);
     return values;
     }
     
    @Override
     public BaseOBObject internalProcess(Object... values) throws Exception {
     
     return createFrequency((String) values[0], (String) values[1], (String) values[2],
     (String) values[3], (String) values[4], (String) values[5]);
     }
     
     public BaseOBObject createFrequency(final String Organization, final String searchkey,
     final String name, final String description, final String factor,
     final String aDate)
     throws Exception {
     
     // Frequency
     XYZZFrequency frequencyExist = findDALInstance(false, XYZZFrequency.class, new Value("searchKey", searchkey));
     if (frequencyExist != null) {
     throw new OBException(Utility.messageBD(conn, "XYZZ_FREQ_EXISTS", vars.getLanguage())
     + searchkey);
     }
     XYZZFrequency frequency = OBProvider.getInstance().get(XYZZFrequency.class);
     
     try {
     frequency.setActive(true);
     frequency.setOrganization(rowOrganization);
     frequency.setSearchKey(searchkey);
     frequency.setName(name);
     frequency.setDescription(description);
     frequency.setFactor(new BigDecimal(factor));
     Date&nbsp; date = new Date();
     frequency.setDate(date);
     
     OBDal.getInstance().save(frequency);
     OBDal.getInstance().flush();
     } catch (Exception e) {
     e.printStackTrace();
     }
     
    // End process
     OBDal.getInstance().commitAndClose();
     
    return frequency;
     }
     }
     

The Java File in the above example is created inside <Openbravo Source
folder>/modules/mymodule/erpCommon/ad_process. You can place it where ever you
want to, but just be careful to provide the proper Java package name. Also,
ensure that you place the Java file in the correct module, so that it is
packaged, when you run an "export.database".

    
    
     
     public Parameter[] getParameters() {
     return new Parameter[] {
     new Parameter("Organization", Parameter.STRING),
     new Parameter("SearchKey", Parameter.STRING),
     new Parameter("Name", Parameter.STRING),
     new Parameter("Description", Parameter.STRING),
     new Parameter("Factor", Parameter.STRING),
     new Parameter("Date", Parameter.STRING) };
     }

The parameters in the above method should be in the same order as they appear
in the input file. However, the parameter names used in the method need not be
the same as the column header in the input file.

    
    
     
    public BaseOBObject createFrequency(final String Organization, final String searchkey,
     final String name, final String description, final String factor,
     final String aDate)
     throws Exception {
     
    // Frequency
     XYZZFrequency frequencyExist = findDALInstance(false, XYZZFrequency.class, new Value("searchKey", searchkey));
     if (frequencyExist != null) {
     throw new OBException(Utility.messageBD(conn, "XYZZ_FREQ_EXISTS", vars.getLanguage())
     + searchkey);
     }
     XYZZFrequency frequency = OBProvider.getInstance().get(XYZZFrequency.class);
     
    try {
     frequency.setActive(true);
     frequency.setOrganization(rowOrganization);
     frequency.setSearchKey(searchkey);
     frequency.setName(name);
     frequency.setDescription(description);
     frequency.setFactor(new BigDecimal(factor));
     Date date = new Date();
     frequency.setDate(date);
     
    OBDal.getInstance().save(frequency);
     OBDal.getInstance().flush();
     } catch (Exception e) {
     e.printStackTrace();
     }
     
    // End process
     OBDal.getInstance().commitAndClose();
     
    return frequency;
     }

The createFrequency() method inserts values into the desired table using
OBProvider. The internalProcess() method, which is inherited from
IdlServiceJava class, is used to call the appropriate method with appropriate
parameters.

  

###  Registering the Process

  * Go to Master Data Management -> Initial Data Load -> Setup -> Entity Default Value 
  * Register your Java file here as shown in the screen shot. 

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_Create_Your_Own_Import_Process_with_IDL-0.png){: .legacy-image-style}

Pay special attention on the class name while adding the entity default value.

  * Import the data using import window 
  * Go to Master Data Management -> Initial Data Load -> Process -> Import 
  * Choose the input file 
  * Choose the entity as Frequency 

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_Create_Your_Own_Import_Process_with_IDL-1.png){: .legacy-image-style}

  * Validate the input file. If the file has invalid data, it will show the invalid data in the log. 

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_Create_Your_Own_Import_Process_with_IDL-2.png){: .legacy-image-style}

  * Once the input values are validated, the data can be loaded into the actual table by clicking on the process. 
  * If there are any issues while processing the input data, appropriate messages will be logged in the message box provided under the Log header in the import screen. 

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_Create_Your_Own_Import_Process_with_IDL-3.png){: .legacy-image-style}

Retrieved from "
http://wiki.openbravo.com/wiki/How_to_Create_Your_Own_Import_Process_with_IDL
"

This page has been accessed 13,281 times. This page was last modified on 21
May 2013, at 07:52. Content is available under  Creative Commons Attribution-
ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**

