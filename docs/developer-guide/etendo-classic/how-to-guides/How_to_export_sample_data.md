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

  

#  How to export sample data

##  Contents

  * 1  Objective 
  * 2  Sample Data Dataset 
  * 3  Exporting the Sample Data 
  * 4  Exporting the sample data extensions 

  
---  
  
##  Objective

The objective of this document is to explain how the Openbravo sample data is
exported using the export.sample.data task.

##  Sample Data Dataset

The tables that will be exported when the export.sample.data task is run are
included in the Client Definition dataset. You can read more about datasets in
this link  .

Note that the way the export.sample.data task currently works, the SQL Where
Clause defined in the dataset tables of the Client Definition dataset will be
ignored and replaced by a client filter.

##  Exporting the Sample Data

To export the sample data of a given client, this export.sample.data ant task,
available from the Openbravo root folder must be run. It has the following
parameters:

  * client: The name of the client whose sample data will be exported 
  * module: The module where the sample.data will be exported. The exported sample data will be stored in the referencedata/sampledata/<clientName> folder relative to the module path. To export to the core sample data folder, 'org.openbravo' must be specified in the client parameter 
  * exportFormat (optional): Available starting from ** 3.0PR17Q1  ** .. It is used to specify the export format of the sample data. Currently there are two available export formats: xml (the default one) and copy. The copy export format will be only available when exporting the sample data from a PostgreSQL database. Sample data exported with the copy format can only be imported in PostgreSQL databases. If the copy parameter is used in an Oracle environment, a warning message will be shown and the xml format will be used instead. 

For instance, to export the sample data of the 'F&B International Group'
client to core using the COPY format, the following command must be used:

    
    
    ant export.sample.data -Dclient="F&B International Group" -Dmodule=org.openbravo -DexportFormat=copy
    

For a more detailed info:  QA_How_To_Export_Sampledata_POS2

##  Exporting the sample data extensions

Sometimes it is required to create extension sampledata, that goes on top of
another sample data (i.e. we want  pos2 sampledata  to go on top of  retail
sampledata  .

Sampledata extensions are built in a very similar way to standard sampledatas.
The main different is that most probably the database tables they include will
define a SQL where clause to specify the subset of records of that table that
shold be included in the extension dataset.

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_export_sample_data-0.png){: .legacy-image-style}

To export a sampledata extension, the following command must be used:

ant export.sample.data.extension -DdataSetName=<sampleDataName>
-Dclient=<clientName> -Dmodule=<moduleJavaPackage>

For instance, to export the sampledata extension of org.openbravo.pos2, the
following command should be executed:

ant export.sample.data.extension -DdataSetName="POS2 SampleData" -Dclient="The
White Valley Group" -Dmodule=org.openbravo.pos2.sampledata

Retrieved from "  http://wiki.openbravo.com/wiki/How_to_export_sample_data  "

This page has been accessed 4,262 times. This page was last modified on 13
November 2023, at 12:10. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**

