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

  

#  SQLC

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |  In
general any new code should be written user the newer  Data Access Layer  .
SqlC/xsql-based code should only be used in special cases or in existing older
code.  
---|---  
  
##  Contents

  * 1  Introduction 
  * 2  A simple example 
  * 3  Basics 
    * 3.1  Naming convention 
    * 3.2  Structure of the source & generated files 
    * 3.3  Visibility of the generated class 
    * 3.4  SqlMethod definition: common parts 
    * 3.5  Connection / Transaction handling 
  * 4  Types of statements 
    * 4.1  Queries 
      * 4.1.1  Returning multiple rows 
      * 4.1.2  Returning a single row 
      * 4.1.3  Returning a single value 
    * 4.2  Parameters & Runtime modification of the query 
      * 4.2.1  Mandatory parameters 
      * 4.2.2  Optional parameters 
      * 4.2.3  Optional parameters without type 
      * 4.2.4  Optional parameters of type none 
      * 4.2.5  Optional parameters of type argument 
      * 4.2.6  Optional parameters of type replace 
    * 4.3  Scrollable Queries (memory-efficient) 
    * 4.4  Extra fields 
    * 4.5  Updates 
    * 4.6  PL Function calls 
    * 4.7  Constants 

  
---  
  
##  Introduction

SqlC is a tool that builds a java class from a file with SQL statements. The
java class contains the code necessary to connect it to a database, format the
statement, execute it and return the resultset from the database. This is a
common function for any statement execution. SqlC avoids this repetitive task
building the java code from the definitions of the desired statements.

##  A simple example

This simple example shows how to use SqlC with a simple SQL select statement.

    
    
     
      SELECT Attribute, Value, AD_Window_ID 
      FROM AD_Preference 
      WHERE AD_User_ID = ?

To let SqlC generate a java class which does execute this query it needs to be
placed in a xml file: i.e. src/org/openbravo/howto/Howto_data.xsql

    
    
     
    <?xml version="1.0" encoding="UTF-8" ?>
     
    <SqlClass name="HowtoData" package="org.openbravo.howto">
      <SqlMethod name="select" type="preparedStatement" return="multiple">
        <Sql>
          SELECT Attribute, Value, AD_Window_ID 
          FROM AD_Preference 
          WHERE AD_User_ID = ? 
        </Sql>
        <Parameter name="adUserId"/>
      </SqlMethod>
    </SqlClass>

This tells SqlC that a java class org.openbravo.howto.HowtoData should be
generated. This class will be used to hold the result of the query and it will
contain a method named select with a parameter named adUserId. The method will
execute the select statement and return an array of HowtoData objects which do
contain the result of the query.

The following snippet displays the interesting parts of the generated class
from the perspective of its user.

    
    
     
    package org.openbravo.howto;
     
    class HowtoData implements FieldProvider {
     
      public String attribute;
      public String value;
      public String adWindowId;
     
      public String getField(String fieldName) {
        if (fieldName.equalsIgnoreCase("attribute"))
          return attribute;
        else if (fieldName.equalsIgnoreCase("value"))
          return value;
        else if (fieldName.equalsIgnoreCase("ad_window_id") || fieldName.equals("adWindowId"))
          return adWindowId;
       else {
         log4j.debug("Field does not exist: " + fieldName);
         return null;
       }
     }
     
      public static HowtoData[] select(ConnectionProvider connectionProvider, String adUserId) throws ServletException {

As shown the class contains three public attributes of type String which do
correspond to the result-columns in the select statement. However the names of
the attributes have been changed to conform to camelCase style which is
usually used with java.

In addition a single getField method was generated to allow getting data via
the fieldname, which can be passed either in camelCase style or via the
original column name in the select statement.

Finally for the select statement a java method named select was generated
which takes a parameter corresponding to the parameter definition in the xsql
file. The method does execute the query and returns its result via an array of
type of the generated class.

##  Basics

After the short example this section explains the basics which are applicable
for all use cases of SqlC. After these have been shown the next section splits
up into the different types of statements and how to use each of them with
SqlC.

###  Naming convention

The source files for SqlC are xml files with the file ending xsql. Only files
with this ending will be picked up by the openbravo build scripts. When the
SqlC tool is run a single java class is generated per xsql file. This class
contains one method per statement defined in the xsql file. The filename
patterns for the source files and the resulting generated file look like the
following:

  * <arbitrary part>_data.xsql => <arbitrary part>Data.java 

Each file needs to reside inside a folder matching the java package in which
the generated file is expected. The location of the xsql source file in the
directory structure needs to match the declared package inside the file.

###  Structure of the source & generated files

There is no formal DTD or XSD for the structure of xsql files. Instead the
structure is informally explained here.

As each xsql file corresponds to a single generated java file it must contain
exactly one xml tag to define the java class. Optionally a single class
comment may be specified which is carried over to a class level javadoc
comment in the generated java file.

    
    
     
      <SqlClass name="HowtoData" package="org.openbravo.howto">
        <SqlClassComment>Example for a sqlc generated class</SqlClassComment>
      </SqlClass>

The two attributes for the SqlClass define the java class- and package-name
and need to be allowed names for java classes and packages.

The generated java class does implement a simple interface named
FieldProvider.

    
    
     
      public interface FieldProvider {
        public String getField(String fieldName);
      }

As already shown in the previous example this methods is one way of accessing
the class data. Alternatively the generated attributes can be accessed
directly.

###  Visibility of the generated class

By default the generated java class will not contain a special access
modifier. This means that the class can only be used from inside the java
package it is defined in. It is not visible from all other java packages.

If a generated class should have a different visibility then the optional
attribute **accessModifier** can be used. The value of this attribute will be
used to define the visibility of the generated class.

The following example shows how to define a generated class as public, so it
can be used from any package.

    
    
     
      <SqlClass name="PublicHowtoData" package="org.openbravo.howto" accessModifier="public">
        ...
      </SqlClass>
    
    
     
    package org.openbravo.howto;
     
    public class PublicHowtoData implements FieldProvider {
      ...
    }

###  SqlMethod definition: common parts

The central part of an xsql file are the statements defined within. Here the
common parts the definition of a SqlMethod are shown. The attributes which are
specific to each statement type are explained in the corresponding later
chapters.

    
    
     
      <SqlMethod
        name="name"
        static="true,false"
        type="{constant,preparedStatement,statement,callableStatement}"
        connection="true,false"
        <SqlMethodComment></SqlMethodComment>
        <Sql>
          sql statement
        </Sql>
      </SqlMethod>

This xml tag defines a single statement / java-method. The name attribute does
directly correspond to the java method which will be created to the statement.

By default all methods are generated as static methods, this behavior can be
changed with the static attribute.

The type attribute does distinguish between the following:

  * constant 
    * No database access 
    * Utility function to populate an data class instance 

  * preparedStatement,statement 
    * These are the main types and correspond to either database queries or select. 
    * The difference between the two is the use of either a JDBC statement or a JDBC PreparedStatement to execute the statement. 

  * callableStatement 
    * This type is only used for PL-method calls 

###  Connection / Transaction handling

By default each invocation of a SqlC generated method is executed inside a
single transaction which is committed automatically. Moreover each invocation
does get an new database connection from the connection pool to execute the
statement in.

For this purpose each generated java method contains an extra parameter of
type ConnectionProvider which is not contained in the parameter list defined
in the xsql file.

    
    
     
      public static HowtoData[] select(ConnectionProvider connectionProvider, String adUserId) throws ServletException {

The generated method retrieves its database connection via this interface.

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |  If the
method invocation is made from a java Servlet which extends the openbravo
HttpSecureAppServlet class, then the servlet class itself can be passed here
as it indirectly implements that interface.  
---|---  
  
However in some circumstances this default behavior is not intended. If
several statements should be executed inside a single transaction this
automatic transaction management in not sufficient.

In this case the optional connection attribute allows for a more fine granular
transaction/connection handling. If it is added with value true the generated
method signature is slightly different as shown here:

    
    
     
      public static HowtoData[] select(Connection conn, ConnectionProvider connectionProvider, String adUserId) throws ServletException {

Here a connection object can be explicitely passed to the function. If the
caller does disable autocommit for this connection and then passes the same
connection on several method invocations he can control the transaction in
more detail.

##  Types of statements

The following chapter explain a single statement type in more detail and
explains the various extra attributes which are needed / useful in its
context.

###  Queries

This first group and most common type of statements issues queries to the
database. This group can be further divided by looking at the type of data
returned by the query:

####  Returning multiple rows

This type of an sql statement was already covered in the first simple example
of this concepts document. The query does return a number of zero or more rows
and the generated java function returns an array of the generated class where
each entry in the array represents a single row of the ResultSet.

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |  If the
user of the function does only need the first row of the result then the next
type of query statement should be used instead.  
---|---  
  
####  Returning a single row

This type of sql statement differs only in the way the query result is
returned. The query itself is sent to the database in the same way as for
queries returning multiple rows. However the generated java code reads only
the first row of the ResultSet from the database and returns it to the user.

This leads approach has a number of benefits compared to reading multiple rows
and just using the first row.

The first benefit happens when the ResultSet of the query is huge. When
reading multiple rows the complete huge result needs to be transfered from the
database to java. Additionally a huge array needs to be allocated in java to
store the result which can easily overflow the available memory.

The second benefit it better usability and more readable code when using the
generated function. The next short example does outline some sample code doing
the same activity using the two different types of statements.

    
    
     
      // sampleCall is defined as returns="multiple"
      SampleData[] rows = SampleData.sampleCall(this);
      if (rows != null && rows.length > 0) {
        SampleData row = rows[0];
        ...
      }
    
    
     
      // sampleCall is defined as returns="single"
      SampleData row = SampleData.sampleCall(this);
        ...
      }

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |  This
type of query does return a single row but does not tell the database that
only a single row is needed. The database still needs to query and return all
rows with potentially comes with a big overhead. To avoid this the select
statement does needs to have the respective LIMIT/OFFSET or ROWNUM parts
added.  
---|---  
  
####  Returning a single value

If the user of a query needs only a single value then an even simpler way is
possible by directly returning a single value instead of one record or even an
array of records.

This type of statement is similar to the one which returns only a single row.
It sends the query to the database and fetches the first row of the ResultSet.

The difference is that here only the first column of the first ResultSet row
is read and returned to the user.

The most general way to pass this column to the caller is to specify a return
type of "String". This way the value is read from the ResultSet with getString
and passed to the user unmodified. In the case that no record was returned by
the query a value of null is returned.

When the return type is specified as "boolean" then a value of true is
returned is the first column is not equals to "0", in all other cases a value
of false is returned.

When the return type is specified as "date" then a String is returned which is
constructed by reading the first column from the database as a date and then
formatting it as a String using the date format "dateFormat.java" which is
specified in the config file "Openbravo.properties". If the query does not
return any rows then a value of null is returned to the caller.

For these three types of return values it is possible to specify a default
value. This is done by adding optional 'default=<value>' attribute to the
SqlMethod definition. In this case the defaultValue is returned to the caller,
if the query does not return any rows.

###  Parameters & Runtime modification of the query

This part explains how to pass parameters to the database statement to fill in
values at runtime or even modify part of the complete SQL statement at
runtime. This applies to all types of statements which are described here.

The parameters which are defined in the xsql file will end up as parameters if
type String for the generated java class. The datatype of all parameters will
always be "String". The parameters of the generated class will be in the same
order as the parameters appear in the xsql file.

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |  If you
modify a existing statement in some xsql file and reorder some parameters then
remember to check if the order of the parameters of the java file changed. If
yes all callers need to be updated to pass the parameter values at the correct
location. As all parameters are of type String this changes will not be
catched by the java compiler and can lead to hard to find errors if the caller
does pass a specific value into a different parameter (after the order
change).  
---|---  
  
![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |  If the
same parameter (with the same name) is specified multiple times for a
statement it will still generate only a single java parameter. The placement
of this single parameter corresponds to the location of the first parameter
(of the duplicates) in the xsql file.  
---|---  
  
####  Mandatory parameters

The most common type of parameters are non-optional parameters. These do
simply specify a single value and a predefined position in the SQL statement.
An example of this is the adUserId parameter in the first example. At runtime
the value of it is passed as a parameter to the JDBC statement or
preparedStament and the location of the corresponding question mark "?" in the
statement.

####  Optional parameters

The second group are the optional parameters. These allow to optionally add
and/or modify parts of the sql statement at runtime.

To be able to modify a part of the statement at runtime a location needs to be
defined for the modification. This can be done in two ways.

The first way is to not explicitely define a location for the runtime change.
In this case the location used is directly after the word "WHERE" in the sql
statement. However to make the change more explicit the location this shortcut
is not recommended.

The second, recommended way is to specify the location explicitely using the
"after" attribute in the parameter definition. This way a explicit part of the
query can be referenced for this purpose. The following example will outline
how this looks like in practice.

####  Optional parameters without type

The simplest way is to add an optional where clause to a query is a parameter
for it is passed at runtime and to ignore the optional part otherwise.

The following example uses this to either query for all orders in the database
or to query for all orders of a specific business partner.

    
    
     
      <SqlMethod name="selectOrders" type="preparedStatement" return="multiple">
        <Sql>
          SELECT * from C_Order c
          WHERE 1=1
          ORDER BY c.documentno
        </Sql>
        <Parameter name="bpartner" optional="true" after="WHERE 1=1">
          <![CDATA[ AND c.C_BPARTNER_ID = ? ]]>
        </Parameter>
      </SqlMethod>

What happens at runtime for this example is defined by the value of the
parameter bpartner. If the value is not null and not the empty String "", then
the executed SQL statement is the following:

    
    
     
      SELECT * FROM C_Order c
      WHERE 1=1
      AND c.C_BPARTNER_ID = ?
      ORDER BY c.documentno

If the value for the parameter is null or the empty String "" then the
optional parameter is completely ignored for the statements' execution.

The recommended way to specify the AFTER location is to add extra clauses like
"WHERE 1=1" or "AND 2=2" to the statement. This will not change the queries
behavior and they always evaluate to true and provide an easy way to see the
places in the query where optional parts will be placed.

####  Optional parameters of type none

A variation of this is an optional parameter of type="none". Using this it is
possible to add a constant String to an SQL statement depending on a
parameters' value.

    
    
     
      <SqlMethod name="selectOrders" type="preparedStatement" return="multiple">
        <Sql>
          SELECT * from C_Order c
          WHERE 1=1
          ORDER BY c.documentno
        </Sql>
        <Parameter name="processed" optional="true" type="none" after="WHERE 1=1" text="AND c.processed = 'Y'"/>
      </SqlMethod>

In this example if the parameters' value is the parameter name (here:
processed) then the option part defined by the parameter is added to the
statement, otherwise the optional part is ignored for the statement execution.

####  Optional parameters of type argument

A second variation is an optional parameter of type="argument". This can be
used to optionally add a fixed part and to pass the complete value of the
parameter (an arbitrary) to the query.

    
    
     
      <SqlMethod name="selectOrders" type="preparedStatement" return="multiple">
        <Sql>
          SELECT * from C_Order c
          WHERE 1=1
          ORDER BY c.documentno
        </Sql>
        <Parameter name="processed" optional="true" type="argument" after="WHERE 1=1">
          <![CDATA[ AND c.C_BPARTNER_ID IN ]]>
        </Parameter>
      </SqlMethod>

Here, again the optional parameter is completely ignored, if the parameters'
value is null or the empty String "". Otherwise the executed statement does
include the fixed part of the parameter followed by the parameters value,
without using a placeholder of "?" of the statement/preparedStament.

Assume that the value of the parameter at runtime is "('17','18','19') then
the executed statement will be:

    
    
     
      SELECT * FROM C_Order c
      WHERE 1=1
      AND c.C_BPARTNER_ID IN ('17','18','19')
      ORDER BY c.documentno
     

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |  Note
that the parameters' value is passed exactly as specified and not escaped
encoded. The caller of the function needs to take care that no unchecked
values are passed into the parameter to avoid SQL injections.  
---|---  
  
####  Optional parameters of type replace

The last variation of optional parameters are defined with the type="replace".
These allow to completely replace a part of an SQL statement with a new part.

    
    
     
    <SqlMethod name="countFrom" type="preparedStatement" return="String" default="">
      <Sql>
        <![CDATA[
          SELECT COUNT(*) FROM FACT_ACCT
        ]]>
      </Sql>
      <Parameter name="tablename" optional="true" type="replace" after="FROM " text="FACT_ACCT"/>
    </SqlMethod>

In this example the parameter tablename can be used to change the name of the
table on which the count is executed on.

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |  Again it
is important to note that the parameters' value is passed exactly as specified
and not escaped encoded. The caller of the function needs to take care that no
unchecked values are passed into the parameter to avoid SQL injections.  
---|---  
  
###  Scrollable Queries (memory-efficient)

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |  This
feature is only availble starting with the 3.0PR14Q2 release.  
---|---  
  
The queries returning multiple rows as described  SQLC#Returning_multiple_rows
above  can consume a huge amount of memory when returning many rows.

This is not a problem if returning only few rows (<1000) but if the number of
rows is unbounded and can be much higher then scrollable queries as described
here can perform much better.

This type of queries only change how to call the SqlcMethod from java, the SQL
text itself does not need to be modified.

The change interface allows to get the result-rows one by one instead of a big
array containing all data.

To use this type use a return scrollable type.

    
    
     
    <?xml version="1.0" encoding="UTF-8" ?>
     
    <SqlClass name="HowtoData" package="org.openbravo.howto">
      <SqlMethod name="select" type="preparedStatement" return="scrollable">
        <Sql>
          SELECT Attribute, Value, AD_Window_ID 
          FROM AD_Preference 
          WHERE AD_User_ID = ? 
        </Sql>
        <Parameter name="adUserId"/>
      </SqlMethod>
    </SqlClass>

This will create a java class like the following:

    
    
     
    package org.openbravo.howto;
     
    class HowtoData implements FieldProvider, ScrollableFieldProvider {
     
      public boolean hasData() {}
      public boolean next() throws ServletException {}
      public ReportGeneralLedgerData get() throws ServletException {}
      public void close() {}
     
      public static HowtoData select(ConnectionProvider connectionProvider, String adUserId) throws ServletException {

As can be seen the select-method does no longer return an HowtoData[] but
instead a instance of the class HowtoData. This instance can then be used to
row by row retrieve the result.

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |  It is
very important to always call the close()-method when using a scrollable
SqlMethod. This is best done using a try-finally block as shown in the
examples below.  
---|---  
  
If you want to pass the data to Jasper Reports using the standard renderJR
method nothing special needs to be done as a version of renderJR exists which
can directly use those scrollable SqlMethod as seen below:

    
    
     
    HowtoData data = null;
    try {
      data= HowtoData.select( .... );
      renderJR(..., data, ....);
    } finally {
      if (data != null) {
        data.close();
      }
    }

  
If you want to just use a scrollable SqlMethod in your own code you can get
the results row by row as seen in the following example. A simple loop is
sufficient.

    
    
     
    HowtoData data = null;
    try {
      data= HowtoData.select( .... );
      while (data.next()) {
        HowtoData oneRow = data.get();
      }
    } finally {
      if (data != null) {
        data.close();
      }
    }

###  Extra fields

The optional field tag allows to add additional non-ResultSet columns to the
class which are filled and returned on the method executions.

There tag needs two mandatory attributes "name" and "value". The name
attributes specifies the user-defined name of the extra field. The value
attribute specifies the value which the field should contain.

Two possible values can be used:

  * void 
    * Using the void value the extra field will be filled with the empty String "" and is just an extra filled which can be used by the methods' caller. 
  * count 
    * Using the value each record will contain its index inside the ResultSet where the first record has the index one. 

###  Updates

The second group of possible statement are database updates. This does include
the following sql statements:

  * INSERT 
  * UPDATE 
  * DELETE 

For all of these statements the database does return the number of affected
rows instead of a query result. In SqlC the corresponding returnType for the
SqlMethod is "rowCount". Specifying this returnType results in two actions.
First the return type of the generated java function is changed to int
corresponding to the number of affected rows of the statement. Second this
type is implicitely used by SqlC to now that the sql statement is an update
rather than a query.

Another short example shows how the xsql file and the generated java method do
look like for update type statements.

    
    
     
      <SqlMethod name="setInDevelopment" type="preparedStatement" return="rowCount">
        <Sql>
             UPDATE ad_module
             SET isIndevelopment = 'Y'
             WHERE ad_module_id = ?
        </Sql>
        <Parameter name="adModuleId"/>
      </SqlMethod>
    
    
      
     
    public static int setInDevelopment(ConnectionProvider connectionProvider, String adModuleId) throws ServletException {
     
        ...
     
        return(updateCount);
      }

###  PL Function calls

This section describes how SqlC can be used to call PL-functions and PL-
procedures. PL-procedures are methods which run inside the DBMS and which do
not return a result value (This can be compared to a method returning void in
java) . PL-function are similar but do return a function result. In addition
both types of PL-methods can have out-type Parameters. These to not accept an
input value but are used to pass one result value back via this parameter.
Using this facility a PL-method can return more than one result value per
function call. If a PL-method does not contain out-type parameters, then a
select statement can be used as an alternative way to call the method, which
is considered to be more intuitive by some developers. However if out-type
parameters are present a SqlC function all as present in here has to be used.

First a simple example if the pl-function has no parameter of type out.

    
    
     
      <SqlMethod name="process1003900000" type="callableStatement" return="object" object="ActionButtonData">
          <Sql><![CDATA[
            CALL C_TAXPAYMENT_POST(?)
          ]]></Sql>
          <Parameter name="adPinstanceId"></Parameter>
       </SqlMethod>
    
    
     
      public static ActionButtonData process1003900000(ConnectionProvider connectionProvider, String adPinstanceId) throws ServletException {
     
        ...
     
        return (objectActionButtonData);
      }

The definition is similar to the definition of update statements. The needed
attributes to define the pl function call are:

  * type="callableStatement" 
    * This tells SqlC that the SqlMethod is a PL function call. It will generate code for it using a JDBC callableStatement 
  * return="object" 
    * This specifies that the return value of the java function will be an object 
  * object="ActionButtonData" 
    * This specifies the java class which whould be used as return value. Attributes of the java class are used to carry the return values of the PL method back to the caller. 
  * import="<fully qualified classname>" (optional) 
    * This optional attribute can be used if the class for the object-attribute is not in the same java package as the sqlc generated class. The value of the import statement is then used to generate a java import statement which does import the class from a different package. Only the import-attribute of the first SqlMethod will be used for this purpose. 

In this example we did not have any return values to carry back to the java
code. SqlC does still use an object as return value but its type can be just
the SqlC generated class and is essentially unused.

The second class of PL function calls are the ones with do return some data to
the caller via parameter of type out. These are rarely used in the openbravo
core as most of the PL methods which return data are PL functions which can be
much easier used as part of a simple SQL select statement.

Another example does outline the usage for this class of function calls

    
    
     
       <SqlMethod name="nextDocType" type="callableStatement" return="object" object="CSResponse">
          <Sql><![CDATA[
            CALL AD_Sequence_DocType(?,?,?,?)
          ]]></Sql>
          <Parameter name="cDocTypeId"/>
          <Parameter name="adClientId"/>
          <Parameter name="updateNext"/>
          <Parameter name="razon" type="out"/>
       </SqlMethod>
    
    
     
     
    class CSResponse {
      String razon;
    }
     
    class DocumentNoData implements FieldProvider {
      public static CSResponse nextDocType(ConnectionProvider connectionProvider, String cDocTypeId, String adClientId, String updateNext) throws ServletException {
        CSResponse objectCSResponse = new CSResponse();
     
        ...
        objectCSResponse.razon = ...
        ...
     
        return(objectCSResponse);
      }
    }

The difference from the previous example is that here the PL procedure
AD_Sequence_DocType has a fourth parameter "razon" of type out. SqlC does
expect the java class which is used to transport the result to have a
accessible attribute of the same name "razon". The out parameters value will
be fetched after the function call and stored in the attribute of an instance
of the result class (here: objectCSResponse.razon). This value can then later
easily be read from the caller.

In this example a class (CSResponse) different from the sqlc-generated class
(DocumetNoData) is used to transport the return value. Alternatively the sqlc-
generated class could have been used to achieve the same effect.

###  Constants

The type of statement is different from the ones described above. It does not
do any database interaction.

Instead the purpose of the generated java function is to create, populate and
return a single instance of the data class with values provides as parameters.

The generated function does create a new object of the type of the data class.
Then all fields which correspond to a column returned by the last processed
function in the xsql file are initialized with some value. If the field
corresponds to a 'Parameter' subtag of the method, then the field is
initialized with the provided parameter value, if not it is initialized with
an empty string “”.

The parameter list of the generated function does exactly contain the
specified parameter from present 'Parameter' subtags, all of the functions
parameters are of type String.

Retrieved from "  http://wiki.openbravo.com/wiki/SQLC  "

This page has been accessed 6,118 times. This page was last modified on 20 May
2014, at 17:23. Content is available under  Creative Commons Attribution-
ShareAlike 2.5 Spain License  .

  
**

Category  :  Concepts

**

