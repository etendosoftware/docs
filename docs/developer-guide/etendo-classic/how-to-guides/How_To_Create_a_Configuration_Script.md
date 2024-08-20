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

  

#  How To Create a Configuration Script

##  Contents

  * 1  Objective 
  * 2  What is a configuration script 
  * 3  How are configuration scripts generated 
  * 4  Installing more than one configuration script in the system 
  * 5  Processes to feed configuration scripts 
  * 6  Additional considerations related to configuration scripts 
  * 7  Unwanted/useless changes inside configuration scripts 

  
---  
  
##  Objective

Modules are an excellent way to extend and customize an Openbravo instance.
However, they have one main limitation: they can be used to **add** new
objects (such as new windows, tabs, tables, or even columns for existing
tables and fields for existing tabs), but they cannot be used to modify
existing objects (such as existing Core fields) , and sometimes this is not
enough. An Industry Template (which includes a Configuration Script) can be
used to modify existing objects. Most of the times, this capability will be
used to modify Core behaviour, but in some situations, it can also be used to
modify module functionality (in particular, when a developer is not the owner
for a module, and wants to use it, but wants to customize some of its
functionality).

This short how-to describes what a Configuration Script (the most important
object of an Industry Template) is, how it can be generated, and how it can be
modified afterwards.

It is highly advisable that you are familiar with the Openbravo development
process before you read this document. In particular, it is very important
that you are familiar with the content in the  How To Create and Package a
Module  document.

##  What is a configuration script

A configuration script is basically an XML file which contains information
about changes done to column values of database table rows.

This is easily explained through an example. This would be the information the
script would contain for a change in the AD_MENU table, in the ISACTIVE
column, which was changed from 'Yes' to 'No', for the row with
AD_Menu_Id='113':

    
    
       <columnDataChange tablename="AD_MENU" columnname="ISACTIVE" pkRow="113">
          <oldValue><![CDATA[Y]]></oldValue>
          <newValue><![CDATA[N]]></newValue>
        </columnDataChange>
    

If you are familiar with the development process of Openbravo, you can
probably already imagine which kind of customizations are possible with
Configuration Scripts. The hiding of existing fields, the change of the
reference of a particular column, or the change of the name of some field are
only some examples.

##  How are configuration scripts generated

Configuration scripts are automatically generated through an ant task called
export.config.script. You first need to create a module of type 'Template' in
Openbravo, and set it as 'In Development'. After that, do the changes you want
to do (for example, change the labels of some fields, or hide them using the
Application Dictionary windows). Finally, make sure that no other modules are
in development in the system, and then execute the following tasks:

    
    
        ant export.database
        ant export.config.script
    

The first one (which you should already know from reading the How to document
related to modules) is used to export the module Application Dictionary data.
The second one exports the configuration script.

This configuration script is created by comparing the current information
inside the XML files of Openbravo Core and your installed modules versus the
information in your database. Every column data change found in the
Application Dictionary is exported to the XML file, which will be created
inside the src-db/database folder of your Template, inside the modules folder
of Openbravo.

##  Installing more than one configuration script in the system

Sometimes, it might be interesting to have more than one Industry Template
(and therefore more than one configuration script) in the system. For example,
imagine that somebody has developed an Industry Template for the Automotive
Industry. This template could include several additional modules, and one
configuration script which adapts some Core functionality to better suit the
needs of this particular industry. You might want to use it in your project,
but you might also need to customize several additional aspects of Core, or
even the modules this template includes. Therefore, an additional Industry
Template (with its corresponding script) would be needed.

It is possible to have as many templates working in the same system as you
want, but one very important rule must be followed: **there needs to be a
defined dependency hierarchy for the templates** . This means that there needs
to be a linear chain of dependencies between the templates. In our previous
example, this means that our customization template would need to depend on
the generic Automotive Template. If four templates (A, B, C, D) are meant to
work on the same instance, then there needs to be a chain of dependencies
which links them (for example, A->B->C->D). **There cannot be two different
templates at the same level of the hierarchy** .

The reason for this rule is in fact easy to explain: configuration scripts are
used to modify objects, and it is very possible that if more than one
configuration script is in the system, there might be overlapping
modifications to the same object. The task which applies the configuration
scripts needs to know in which order the changes need to be applied, and the
only way for this is to define an explicit order in which the templates need
to be applied.

Another very important rule which must be followed: **it is only possible to
develop the template which is in the outer side of the dependency chain** . In
our previous example, you would be able to develop your own customization
template (that is, to change the configuration script), but you wouldn't be
able to develop the generic Automotive Industry template, because there is
already one template which depends on it.

##  Processes to feed configuration scripts

In some situations, it could seem to be a good idea to include a configuration
script inside a normal module. For example, a module might add a callout, or a
new reference, but the developer would also want to associate the callout to
an existing Core field, or to change the reference of a Core column to the new
one.

It is not possible to add a configuration script to a module precisely for the
reasons explained in the section above (modules are meant to be independent in
lots of situations, but configuration scripts need to be executed in an
specific order, and therefore, there needs to be an explicit dependency
between them). However, there is an alternative for cases similar to the ones
described above: a module can include a process to do the changes in the
Application Dictionary, designed to be executed in an environment with an
active customization Industry Template.

This process would be executed in the instance after the module has been
installed, and after it has been executed, the modifications can then be
exported to the specific customization Industry Template that instance already
has.

A good way to do this would be to create an standard Openbravo Java process.
You can read more about these processes  here  . The process would need to do
the following steps:

  * It would first need to check if there is an Industry Template in development in the system (this is a requirement for the execution of the process). This can be done with a DAL query in a very easy way: 

    
    
         public String returnIdOfTemplateInDevelopment(){
              OBCriteria<Module> tCriteria = OBDal.getInstance().createCriteria(Module.class);
              tCriteria.add(Expression.and(Expression.eq(Module.PROPERTY_TYPE, "T"), Expression.eq(
                  Module.PROPERTY_INDEVELOPMENT, true)));
     
             if (tCriteria.list().size() > 0) {
               return tCriteria.list().get(0).getId();
             }else{
                //We didn't find any template in development
               return null;
             }
        }
    

  * If there is one, then the changes can be done. This changes would be done in Java (possibly through DAL queries and updates) and they could be either static (that is, you could be changing a specific hardcoded set of Application Dictionary objects) or dynamic (you could be changing Application Dictionary objects which comply with some specific rule). This means that in fact, this process could be even more powerful than a configuration script (which are by design static), because you could be changing, for example, the references for all columns in the instance which currently are using some specific reference. For example, this code: 

  

    
    
           final String whereClause = "as c where c.reference.id = :ref_id"
               + " and c.referenceSearchKey.id = :ref_val_id";
           OBQuery<Column> cQuery = OBDal.getInstance().createQuery(Column.class, whereClause);
           cQuery.setNamedParameter("ref_id", "10");
           cQuery.setNamedParameter("ref_val_id", oldRef);
           if (cQuery.count() == 0) {
             pLogger.logln("No columns to update");
           }
           String logMessage = "Processing column: @AD_COLUMN_ID@";
           for (Column c : cQuery.list()) {
             pLogger.logln(logMessage.replaceAll("@AD_COLUMN_ID@", c.getId()));
             c.setReference(newRef);
             c.setReferenceSearchKey(newRefSearch);
             OBDal.getInstance().save(c);
           }
         
    

would change the reference of all the columns with String reference (id=10) to
a new reference (newRef).

  * After the changes have been done, you should output a clear message to the user telling him that he needs to export his configuration script again (the developer in charge of the instance which has the customization template will need to do ant export.config.script at this point). 

##  Additional considerations related to configuration scripts

Configuration scripts are mainly used to export changes you don't want to
export to the owner of the data you are changing. In the previous example, you
don't want to export the changed information of the AD_Menu entry to Core
files, but instead, you want to export the change to a specific, localized
configuration script which belongs to your customization Industry Template.
Therefore, it would be inconsistent to have both Core and your Industry
Template in development at the same time. Even more, if you had both in
development at the same time, the changes would get exported into Core files
through the export.database task, and the configuration script you would get
would therefore be empty.

The same thing can be said when you are using configuration scripts to modify
existing modules. It doesn't make sense to have both the module and the
template in development at the same time. Doing so would cause the changes to
get exported into the module files, and the configuration script will be
empty.

##  Unwanted/useless changes inside configuration scripts

In earlier versions of Openbravo, it was possible that when the modules
installed in the instance were developed with an earlier MP than the one
currently installed in the system, unnecessary changes could be exported
inside the configuration script. This included changes such as this one:

  

    
    
       <columnDataChange tablename="AD_COLUMN" columnname="ISAUTOSAVE" pkRow="FEFAAABCCCCC1001FEFAAABCCCCC1001">
          <oldValue/>
          <newValue><![CDATA[N]]></newValue>
        </columnDataChange>
    

These changes correspond to new columns added in the MP used, which didn't
exist in the MP in which the modules were created. These changes are not
necessary, and although they are harmless, they might clutter the
configuration script, sometimes making it difficult to read and manually
analyze.

There is a built in mechanism to prevent this from happening. However, if the
configuration script was generated in an early version of OB, these changes
might be inside it already. There is a process to "clean" the script, which
involves the following steps:

  * Temporarily remove the configuration script from the system (you only need to move the file out of its correct place, in modules/java_package_of_template/src-db/database/configScript.xml), and execute ant update.database 
  * Make a copy of the file src-db/database/formalChangesScript.xml, inside the main Openbravo folder. 
  * Put the configuration script back in its place, and execute ant update.database again. 
  * Place the copy of the formalChangesScript.xml file back in its place, replacing the file there. 
  * Execute ant export.config.script with your template set as in development. 

After following these steps, the resulting configuration script file should be
clean, and without these useless changes.

Retrieved from "
http://wiki.openbravo.com/wiki/How_To_Create_a_Configuration_Script  "

This page has been accessed 13,802 times. This page was last modified on 17
June 2011, at 15:18. Content is available under  Creative Commons Attribution-
ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**

