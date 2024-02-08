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

  

#  How to define an on Create Default

##  Contents

  * 1  Objective 
  * 2  Concept 
  * 3  Development process 
  * 4  How to correctly remove an onCreateDefault 

  
---  
  
##  Objective

The objective of this document is to briefly explain what an
**onCreateDefault** is, in what situations it's useful, and to describe how to
correctly define one.

##  Concept

OnCreateDefaults are SQL statements which are executed by the update.database
task when a database column is created. They are normally used to insert data
into a newly created column. It's important to note that they are only
executed when the column is being created. If the column is already in the
database, update.database will not execute the onCreateDefault statement. To
fill data into an already created column, you can use a Module Script. To find
more about the Module Scripts, you can see  this  document in our Developers
Guide.

##  Development process

onCreateDefault statements are added directly to the XML file of the table.
This means that the main development steps should be:

  * Add the new column in the database 
  * Run export.database to export the column to the XML file 
  * Edit the xml file to add the onCreateDefault 

An onCreateDefault statement should be valid SQL which can be appended in two
different kinds of SQL commands. Let's assume that the table C_BPARTNER is
going to be extended, adding a MYCOLUMN column. We need to design an
onCreateDefault statement which works with the following two kinds of SQL
commands:

    
    
     
    INSERT INTO C_BPARTNER (Column1, Column2, ..., MYCOLUMN) SELECT (Column1, Column2, ..., MYCOLUMN_ONCREATEDEFAULT) FROM C_BPARTNER_
     
    UPDATE C_BPARTNER SET Column1=ValueForCol1, Column2=ValueForCol2, ..., MYCOLUMN=(MYCOLUMN_ONCREATEDEFAULT)

So, in this case, let's imagine that MYCOLUMN is a Yes/No column, and we want
to set it as 'N' for the existing rows of C_BPARTNER when the column is first
created. We would modify the column definition, so it looks like this:

    
    
     
          <column name="MYCOLUMN" primaryKey="false" required="true" type="CHAR" size="1" autoIncrement="false">
            <default><![CDATA[N]]></default>
            <onCreateDefault><![CDATA['N']]></onCreateDefault>
          </column>

Notice the difference in syntax in the onCreateDefault, compared to the
standard default. We need to add quotes there, because of the type of SQL
command the onCreateDefault will be inserted in.

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
Importantant Notes:

  * the onCreateDefault SQL statement **must return only one row** . 

  * the execution of the onCreateDefault takes place while the table is being rebuilt. This means that if the statement fails, there could be data loss in the customer database when the module is installed. Therefore **the statement must be built so that it always can be executed** . 

  
  
---|---  
  
One limitation of the current implementation of onCreateDefaults is that, due
to having to support the two different kinds of SQL syntax, you cannot make
reference to a different column of the table you are modifying. This means
that it can be very tricky to design a correct onCreateDefault in situations
in which you need to make a link to a different table. For these situations, a
Module Script could be used instead of an onCreateDefault, and the same result
can be achieved this way.

##  How to correctly remove an onCreateDefault

onCreateDefaults are also removed by editing the XML file. The correct way to
remove it is to delete the contents inside the <onCreateDefault> tag, but
leave the tag itself there. If you delete everything, including the tag, next
time you export the module (or Core, if you are editing a Core column), there
will be an inconsistency, as  DBSourceManager  will create an empty
onCreateDefault element. In a practical example, the following column has an
onCreateDefault:

    
    
     
          <column name="MYCOLUMN" primaryKey="false" required="true" type="CHAR" size="1" autoIncrement="false">
            <default><![CDATA[N]]></default>
            <onCreateDefault><![CDATA['N']]></onCreateDefault>
          </column>

If we want to remove it, the correct way would be to leave the column like
this:

    
    
     
          <column name="MYCOLUMN" primaryKey="false" required="true" type="CHAR" size="1" autoIncrement="false">
            <default><![CDATA[N]]></default>
            <onCreateDefault/>
          </column>

Retrieved from "
http://wiki.openbravo.com/wiki/How_to_define_an_on_Create_Default  "

This page has been accessed 8,632 times. This page was last modified on 13
July 2011, at 09:52. Content is available under  Creative Commons Attribution-
ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**

