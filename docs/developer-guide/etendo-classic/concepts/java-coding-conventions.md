---
title: Java Coding Conventions
tags:
    - Java
    - Coding
    - Conventions

status: beta
---

#  Java Coding Conventions

!!! example  "IMPORTANT: THIS IS A BETA VERSION"
    It is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**.

##  Overview

This document gives a description of the coding standards and coding principles used in the development of Etendo.

At Etendo we use Eclipse 3.7 (Indigo), for a description on how-to setup Eclipse see this [How To](../how-to-guides/how-to-set-up-eclipse-ide.md).

##  Standard Code Conventions

Etendo uses the standard coding conventions as defined by Sun in [Code Conventions for the JavaTM Programming Language](https://www.oracle.com/java/technologies/javase/codeconventions-contents.html){target="\_blank"}.

##  Skimmable Code: Easy to Read, Easy to Change

Skimmable code has one main characteristic (next to being readable and understandable): it is code for which it is possible to read and change parts of the code without needing to fully understand the complete codebase (the rest of the code). Skimmable code is therefore naturally robust and easier to maintain than non-skimmable code.

When creating skimmable code one abstract term is important: lexical encapsulation. Lexical encapsulation concretely means that code is grouped together in clearly defined methods which are not longer than one
window/screen.

Other principles which help to create skimmable and therefore maintainable and understandable code:

* Use clear, readable and intention revealing names for variables, methods and classes 
* Use intermediate variables to increase readability (see below) 
* Make short methods which fit in one window/screen 
* Define variables and methods within the scope and close to where they are used 
* Use horizontal spacing to group statements together 
* Keep methods clear and focused. let a method do one thing: retrieve a value or change a value 

These are the main principles which help skimmability, other do's discussed in this document also facilitate maintainability, correctness, quality, robustness.

##  Main Coding Principles

##  Do's

In addition to the skimmability enablers and the standard (more formatting related) Coding Conventions an Etendo programmer should follow these guidelines:

###  Formatting

####  Use an IDE with automatic code formatting at save

Although Eclipse may be adviced there are other popular IDE's available. In any case, the source code should always be automatically formatted (when a file is saved) using the standard Sun Java code conventions as defined above.

To enable code formatting when saving and to use the Etendo code formatting standard make sure to import the preferences provided in the config/eclipse folder in the development projects. This import step is described [here](../how-to-guides/how-to-set-up-eclipse-ide.md#import-preferences).

####  Etendo Copyright on Etendo Intellectual Property (must-do)

Each file which is Etendo Intellectual Property should have the following copyright message in the top: ???

```
*************************************************************************
* The contents of this file are subject to the Openbravo  Public  License
* Version  1.0  (the  "License"),  being   the  Mozilla   Public  License
* Version 1.1  with a permitted attribution clause; you may not  use this
* file except in compliance with the License. You  may  obtain  a copy of
* the License at http://www.openbravo.com/legal/license.html
* Software distributed under the License  is  distributed  on  an "AS IS"
* basis, WITHOUT WARRANTY OF ANY KIND, either express or implied. See the
* License for the specific  language  governing  rights  and  limitations
* under the License.
* The Original Code is Openbravo ERP.
* The Initial Developer of the Original Code is Openbravo SLU
* All portions are Copyright (C) 201 Openbravo SLU
* All Rights Reserved.
* Contributor(s):  ______________________________________.
************************************************************************
```    

The year in the copyright statement is the current year when the file is new
and contains two dates if the file is updated in a different year than it was
created. For example a file created in 2006 and changed for the last time in
2011 will have the following years: 2006 - 2011 specified near the (C) sign:

```
* All portions are Copyright (C) 2006 - 2011 Openbravo SLU
```

####  Vertical Spacing

Use vertical spacing to separate different parts of the code and to make the code less dense to read. Here is an example without vertical spacing:


```
try {
    configuration = new Configuration();
    mapModel(configuration);
    setInterceptor(configuration);
    configuration.addProperties(getOpenbravoProperties());
    // add a default second level cache
    if (configuration.getProperties().get(
        Environment.CACHE_PROVIDER) == null) {
    configuration.getProperties().setProperty(
    Environment.CACHE_PROVIDER,
    HashtableCacheProvider.class.getName());
    }
    sessionFactory = configuration.buildSessionFactory();
    log.debug("Session Factory initialized");
} catch (final Throwable t) {
    throw new OBException(t);
}
```

And here is the same example with horizontal spacing to make it easier to read:

```
try {
    configuration = new Configuration();
 
    mapModel(configuration);
 
    setInterceptor(configuration);
 
    configuration.addProperties(getOpenbravoProperties());
 
    // add a default second level cache
    if (configuration.getProperties().get(
            Environment.CACHE_PROVIDER) == null) {
    configuration.getProperties().setProperty(
    Environment.CACHE_PROVIDER,
    HashtableCacheProvider.class.getName());
    }
 
    sessionFactory = configuration.buildSessionFactory();
 
    log.debug("Session Factory initialized");
} catch (final Throwable t) {
    // this is done to get better visibility of the exceptions
    t.printStackTrace(System.err);
    throw new OBException(t);
}
```

###  Code Documentation Policy

Well documented and commented code is great and helps to understand the meaning of the code thereby improving productivity and preventing future bugs.

The Etendo code documentation policy aims to combine a light-weight code documentation process which adds value to a developer navigating through the Etendo code in his/her IDE. Comments and documentation should be easy to maintain and be up-to-date with the code it describes.

Documentation and comments can be divided in two main parts: Javadoc and inline commenting.

In Etendo Javadoc comments have two main uses: to be used as the basis to generate Javadoc html pages and technical documentation and to support specific features of current IDEs, e.g. show Javadoc when hovering with the mouse over methods and constants.

Inline commenting is used to clarify the meaning of the code and underlying implementation decisions which may influence future coding decisions.

Note that all comments and documentation must be in English using the US notation (for example: organization instead of organisation).

####  Class Javadoc (a must-do)

Each class must have a well-formatted Javadoc section in the top. The class doc comment must describe the overall function of the class and its relation to other classes.

The class doc comments may not contain implementation details as they may change quickly with the risk of having outdated comments.

The class Javadoc must contain @author annotations with the name/login of the developers who have worked on that class.

While writing Javadoc class comments also provide @link and @see annotations to related classes. This helps to place the class in the context of other classes.

Here is an example of a class doc of the Entity class:

```
/**
    * Models the business object type. The Entity is the main concept in the
    * in-memory model. An entity corresponds to a {@link Table} in the database. An
    * Entity has properties which are primitive typed, references or lists of child
    * entities.
    * 
    * @see Property
    * @see ModelProvider
    * 
    * @author iperdomo
    * @author mtaal
    */
```

####  Method Javadoc (a must-do)

Every public method in the Etendo code base must have a Javadoc comment.

There is one exception on this rule: getters/setters which do not more than get or set a member of the class, should not have a Javadoc comment. The main reason is that Javadoc for these methods does not add much value.

The Javadoc of a method must describe the general logic of the method without too many implementation details. The input and output of the method should be described. Some other rules which must be followed:

* Every parameter must be described using the @param annotation (do not have empty @param annotation) 
* The return value must be described using the @return annotation (also here, prevent empty return annotations) 
* If the method throws an UncheckedException then this exception must be mentioned in the Javadoc using the @throws annotation. 
* It must specifically be documented if a method can return null so that the caller can take that into account. 

```
/**
* The main entry point. This method walks through the elements in the root
* and parses them. The children of a business object (in the xml) are also
* parsed. Referenced objects are resolved through the
* {@link EntityResolver}.
* <p/>
* After a call to this method the to-be-inserted objects can be retrieved
* through the {@link #getToInsert()} method and the to-be-updated objects
* through the {@link #getToUpdate()} method.
* 
* @param xml
*   the xml string
* @return the list of BaseOBObject present in the root of the xml. This
*   list contains the to-be-updated, to-be-inserted as well as the
*   unchanged business objects
*/
```

or

```
/**
* Validates the values of the properties of the entityObject. The
* validation messages are collected into one ValidationException.
* 
* @param entityObject
*   the entity instance
* @throws ValidationException
*/
public void validate(Object entityObject) {
    ....
}
```

####  Javadoc for Class members

Members should not have Javadoc, as a class member is always private.

####  Javadoc for Constants

Public final static Constants must have JavaDoc. Private constants should not have Javadoc.

####  Javadoc Formatting

The JavaDoc must use standard doc constructs like linking to Javadoc of other classes and use Javadoc formatting. Visit [this page](https://www.oracle.com/java/technologies/){target="\_blank"} for more information.

####  Inline Commenting

Inline comments can be crucial for a developer to understand the meaning of code and to be informed about earlier implementation decision. However when commenting keep the following in mind:

* The general philosophy is that there is only a minimal need for comments: the code itself should be readable (using descriptive names and variables to store intermediate results). 
* Comments should only be added if they add value and provide deeper insight which is not directly visible in the code itself. 
* Inline comments are hard to maintain and are quickly outdated because code changes quickly. So therefore comments must be placed as closely as possible to the code they refer to. 
* Remove outdated comments! 

Here is an example of some inline comments from the OBQuery class. In this case the inline comments are used to show examples which are handled by that part of the code.

    
```
// The following if is there because the clauses which are added should
// all be and-ed. Special cases which need to be handled:
// left join a left join b where a.id is not null or b.id is not null
// id='0' and exists (from ADModelObject as mo where mo.id=id)
// id='0'
boolean addWhereClause = true;
if (whereClause.trim().length() > 0) {
    if (!whereClause.toLowerCase().contains("where")) {
    // simple case: id='0'
    whereClause = " where (" + whereClause + ")";
        addWhereClause = false;
    } else {
    // check if the where is before the from
    final int fromIndex = whereClause.toLowerCase().indexOf("from");
    int whereIndex = -1;
    if (fromIndex == -1) {
        // already there and no from
        // now find the place where to put the brackets
        // case: left join a left join b where a.id is not null or
        // b.id is not null
 
        whereIndex = whereClause.toLowerCase().indexOf("where");
        check.isTrue(whereIndex != -1, "Where not found in string: " + whereClause);
    } else {
        // example: id='0' and exists (from ADModelObject as mo
        // where mo.id=id)
        // example: left join x where id='0' and x.id=id and exists
        // (from ADModelObject as mo where mo.id=id)
 
        // check if the whereClause is before the first from
        whereIndex = whereClause.toLowerCase().substring(0, fromIndex).indexOf("where");
    }
 
    if (whereIndex != -1) {
        // example: left join x where id='0' and x.id=id and exists
        // (from ADModelObject as mo where mo.id=id)
        addWhereClause = false;
        // now put the ( at the correct place
        final int endOfWhere = whereIndex + "where".length();
        whereClause = whereClause.substring(0, endOfWhere) + " (" + whereClause.substring(endOfWhere) + ")";
    } else { // no whereclause before the from
        // example: id='0' and exists (from ADModelObject as mo
        // where mo.id=id)
        whereClause = " where (" + whereClause + ")";
        addWhereClause = false;
    }
    }
}
```

###  Exception Handling

####  Only create Exceptions which do not need to be caught (Runtime Exception)

Often you can use the standard OBException or another existing exception within the Etendo codebase. However, when you know that calling code will want to catch a specific exception then it can make sense to create an own exception for the specific module which is being developed.

####  Extend OBException

When creating a new exception always extend the OBException. The OBException takes care of logging. In addition this exception is an unchecked Exception. All new exceptions should be unchecked exceptions.

####  Add context info to your Exception

When throwing a new Exception or catching, packaging and re-throwing an exception it is vital that context information is added to the Exception message. Only then it is possible to determine for which business object or which situation a method fails

```
if ((p = propertiesByName.get(propName)) == null) {
    throw new OBException("Property " + propName
        + " not defined for entity " + this);
}
```

!!!info
    In this case, the 'this' makes sense because the object implements the `toString` method (see the next do).

!!!note
    when adding context information to an exception then be aware of possible new exceptions when creating the exception.

    ``` 
        
        try {
        ...
        } catch (Exception e)
        throw new OBException("Exception when submitting order " +
            order.getId() + " with customer " + 
            order.getCustomer().getId(), e);
        }
    ```

This exception throw will fail when the order is null or the customer of the order is null. This NPE will then hide the real exception.

###  Use Java 1.5 Constructs

Make use of the following Java 1.5 Constructs:

* Typed collections (a must-do)   
    
    So don't use any of these constructs: 

    List businessPartners = new ArrayList();
    List<Object> businessPartners = new ArrayList<Object>();
    List<?> businessPartners = new ArrayList<?>();

    But do it like this:
    
    List<BusinessPartner> businessPartners = new ArrayList<BusinessPartner>();


* Enhanced for-loop (a must-do)   
    
    Don't use the old for loop:
        
    for (int i = 0; i < businessPartners.size(); i++) {
        ...
    }

    But use this:

    for (BusinessPartner businessPartner : businessPartners) {
        ...
    }

* Enums (when appropriate)


###  Implement sensible methods

Methods should be small and focused, a method should do one thing and have no sideeffects beyond what is revealed by the name. The name of the method should be inline with the abstraction level of the class and should be intention revealing, descriptive and easy to read.

A method should either answer a question, i.e. return a (computed) value, or make one change (set a value).

Methods should not have more than one, two or three parameters. More parameters should be encapsulated in an object.

The parameters of a method should be treated as input and not be changed by the method.

###  Naming

Naming is very important. Good names make programs readable, increase productivity and prevent bugs when developers change existing code. Here are a few important guidelines when naming classes, methods and members/parameters in Etendo:

* Names must always be in English (US notation) 
* Names must be pronounceable and searchable 
* A class and interface name must be a noun, while a method name always contains a verb 
* It should be clear to the reader what the name means: the name should be intention revealing 
* A name should consist of the words/terms which correspond to the mental frame of the reader 

###  Defensive Coding

Defensive coding is a development approach whereby the developer explicitly takes into account that application error situations will occur. This is made explicit by adding invariant and post/pre-condition checking statements in the code.

####  Guard for not-implemented cases

When handling a specific list of cases always guard for a new case which is not handled in the code. For example, don't do this:
    
    if (value.equals(CASE_ONE)) {
      handleCaseOne();
    } else if (value.equals(CASE_TWO) {
      handleCaseTwo();
    } else if (value.equals(CASE_THREE) {
      handleCaseThree();
    }

But always handle the situation that a new case is added without the code knowing about it:

    if (value.equals(CASE_ONE)) {
      handleCaseOne();
    } else if (value.equals(CASE_TWO) {
      handleCaseTwo();
    } else if (value.equals(CASE_THREE) {
      handleCaseThree();
    } else {
      throw new ArgumentException("Unhandled case: "  + value);
    }

####  Do invariant checking (defensive coding)

The previous "Do" is an example of defensive coding. With defensive coding you assume that illegal conditions will occur and that you will check for this. So a (very) good programmer will have pre- and postcondition checking statements throughout his/her code. Although java provides the assert statement it is better to use a specific Etendo utility class for this: the `org.openbravo.base.util.Check` class.

This class provides methods to check for false, true, null, instanceof etc.

###  Use intermediate variables to increase readability

```
// less readable
if (writable && (!hasReferenceAttribute || 	
    businessObject.isNewOBObject())) {
    ....
}
    
// more readable, intention revealing
final boolean allowUpdate = writable && 
    (!hasReferenceAttribute || 	
    businessObject.isNewOBObject());
    
if (allowUpdate) {
    ...
}
```

###  Use logging - when appropriate

Logging is especially appropriate when the system is configuring or initializing itself. So that later in the log, it can be validated that the system initialized correctly.

Also, in case of specific computations (such as generating a sql statement or executing a script), it can make sense to log the input and output.

However, the main issue with logging is that the log can fill up fairly quickly with less-useful information. So, in many cases, it can make more sense to combine defensive coding with exceptions with a lot of context information than to opt for extensive logging.

Here is an example for how to make use of logging in Etendo:

* create a static (private and final) log member which is the log4j Logger 
* the logger name is the class name 
* when logging an error/exception do: log.error("string", error) (the order of the parameters is important here). Add context information to the message. 

```  
public class MyClass {
  private static final Logger log = Logger.getLogger(MyClass.class);
     
  public void myMethod(String param) {
    log.debug('debug code');
    try {
        ....
    } catch (Exception e) {
        log.error("Exception in myMethod with parameter " + param, e);
        ....
    }    
    }
```

###  Code and name at one level of abstraction/genericity

A class/type should be created for one specific generic level/abstraction level.

For example consider a Order class with two subclasses SalesOrder and PurchaseOrder. The Order is defined at a generic level, which means that the methods of Order should be defined at that same generic level. A getPrice method would for example be a strange method on Order level, but logical on SalesOrder level. On the other hand a getCost method would be logical on Order level as both a SalesOrder and PurchaseOrder have a cost characteristic.

###  Prefer class/type-branching over if-branching

Every if-then-else statement is an example of if-branching, based on some condition a method behaves in one way or another. If-branching is easy to code and quick.

However, in some cases it makes sense to consider subclassing to separate branched behavior in different classes. This especially applies in case several if-statements are related, check for the same condition and the condition is related to the state of the instance.

After separating the branches in different subtypes, the only remaining if-branch is the factory which supplies the correct subclass based on some parameters.

Consider this example:

```
public class Property {
    private boolean isPrimitive;
        
    public String getTypeName() {		
    final String typeName;
    if (isPrimitive()) {
        typeName = getPrimitiveType().getName();
    } else {
        typeName = getTargetEntity().getClassName();
    }
    return typeName;
    }
    
    public boolean allowNullValues() {
    if (!isPrimitive()) {
        return true;
    }
    return (getPrimitiveType().getName().indexOf('.') != -1);
    }
        
    ....
}
```

In this case it makes sense to split the Property class in a PrimitiveProperty and a ReferenceProperty class which both extend a Property class. The result is much more readable:

```
public class PrimitiveProperty extends Property {
    public String getTypeName() {		
    return getPrimitiveType().getName();
    }
    
    public boolean allowNullValues() {
    return (getPrimitiveType().getName().indexOf('.') != -1);
    }
 
    ....
}
    
public class ReferenceProperty extends Property {
    public String getTypeName() {		
    return getTargetEntity().getClassName();
    }
    
    public boolean allowNullValues() {
    return true;
    }		
    
    ....
}
```

###  Use is/has/can prefixes for boolean Getters

IDE's will as a standard generate the correct getter for a boolean. However, when manually coding getters one should always use one of the prefixes: is/has/can.

###  Implement toString in specific cases

When implementing a new set of objects consider implementing the toString method of these objects. This makes it much easier to use these objects in logging and exception messages.

##  Don'ts

There are also a set of commonly made mistakes which should be avoided when doing Java programming within Etendo:

###  Exception Handling Don'ts

####  Prevent non-handling Catch block

A common mistake is to have a catch block (in a try-catch structure) which only prints the exception but does not handle it further. For example:

```
try {
    properties.load(new FileInputStream(theFile));
} catch (FileNotFoundException e) {
    // TODO Auto-generated catch block
    e.printStackTrace();
} catch (IOException e) {
    // TODO Auto-generated catch block
    e.printStackTrace();
}
```

This should either be changed to a catch block which rethrows the exception with new context information or a comment why the exception does not need to be handled further.

####  Don't hide caught exceptions

This "don't" relates to the use of catching an exception but not passing it on as the cause of the new thrown Exception:

```
try {
    properties.load(new FileInputStream(theFile));
} catch (Exception e) {
    throw new MyException("Something went wrong: " + e.getMessage());
}
```

The correct approach is this (see the second parameter in the constructor
call):

```
try {
    properties.load(new FileInputStream(theFile));
} catch (Exception e) {
    throw new MyException("Something went wrong: " + e.getMessage() + " when calling with params " + param, e);
}
```

!!!Note
    See that in the second case context information was added to the exception message.

####  Don't throw instances of Exception or Error

Throwing a direct instance of Exception or Error is not considered to be good coding practice:

```
if (errorOccurred) {
    throw new Exception("An error occurred");
}
```

Instead of Error/Exception always an instance of an OBException (or its subclass) should be thrown. If you are developing a set of classes for a common domain then introducing one Exception class for that domain can make sense. Only introduce a new Exception if it makes sense for another piece of code to catch it.

A new exception class should inherit from OBException.

```
if (errorOccurred) {
    throw new MySpecificException("An error occurred: " + additionalContextInformation);
}
```

####  Don't create empty catch blocks without comment

There can be a reason to have an empty catch block. However, always a comment needs to be placed in the empty catch block to make clear why the exception is not carried further. For example, this is wrong:

```
boolean isALong = false;
try {
    Long.parseLong(myStringLong);
    isALong = true;
} catch (NumberFormatException e) {
}
```

and this is correct (also repeating the isALong = false makes the code clearer):

```
boolean isALong = false;
try {
    Long.parseLong(myStringLong);
    isALong = true;
} catch (NumberFormatException e) {
    // Exception ignore on purpose
    // is not a long in this case	
    isALong = false;
}
```

###  Don't forget to remove auto-generated TODO's

The above code also shows another mistake, leaving auto-generated TODO's in the code. This should be avoided as it makes the impression that the developer did not finish his/her work here ("keep the campground tidy").

###  Don't use Vector (only when it is really needed)

In many parts of the code of Etendo a Vector is used for a sorted collection. The main difference between an ArrayList and a Vector is that a Vector is synchronized and an ArrayList is not. However the fast majority of Etendo code is accessed single-threaded. It is therefore better to use an ArrayList. Only in the rare case of multi-threaded access a Vector should be used.

###  Don't extend/implement an interface just for its Constants

For example:

```
public interface TheConstants {
    public final String YES = "yes";
}
    
public class MyClass implements TheConstants {
    
    public boolean isYes(String value) {
    return YES.equals(value);
    }
}
```

As the YES is declared in another source file it is not directly obvious for the reader of the code where it is coming from.

###  Don't use double/float

The java double (and float) are very inprecise for decimal computations (for example for invoices or inventory management). For example the following program:

```
final double a = 0.58;
System.err.println(a * 100);
```

will print this:

```    
57.99999999999999
```

For decimal computations, always use a BigDecimal.

###  Don't pass Null

Although it cannot always be avoided, one should always be on the watch when passing a null argument to a method. A method which can handle null arguments should explicitly state this in a comment.

###  Don't return Null

As for passing null arguments, the same applies to return values. Return values of a method should preferably never be null. It is preferred to use an exception instead to signal that an object was not found or another error situation occurred. Of course there are cases when it makes sense to return null values. This should be done with care and the method should explicitly state in a comment that it can return null values.

###  Don't keep commented out code

Code which is commented out should be removed as quickly as possible. Commenting out code is common when working on existing code. However, when the main work is finished the commented-out code should be removed. There are rare cases were it make sense to keep commented out code for a while. In this case,additional comments should be added to explain why the code is still there (and commented out).

###  Be carefull with boolean (or other so-called selector) parameters

A method with boolean parameters can be confusing as often boolean arguments are used to perform if-branching inside a method. When viewing the method call it is not directly clear what the meaning is of a boolean (or other constant) parameter. For example with this method call:

```    
BigDecimal mainInventory = computeInventory(product, quantity, false);
``` 

it is not directly clear what the last parameter means. This can be re-written in two separate ways:

* Method 1: add a boolean variable (with a descriptive name) to store the value and use the variable in the method call: 

```
final boolean computeForMainLocation = false;
BigDecimal mainInventory = computeInventory(product, quantity, computeForMainLocation);
```

* Method 2: create two separate methods each covering one case: 

```
BigDecimal mainInventory = computeInventoryMainLocation(product, quantity);
BigDecimal subInventory = computeInventorySubLocation(product, quantity);
```

The second case is much more expressive.

The trade-off between the two methods is that for the second approach many more methods (with similar names) are created, while for the first approach an extra variable is required.

###  Avoid negative conditionals

Negative conditionals are difficult to read, and double negative conditionals are virtually impossible to read. For example:

```
// less readable
if (!file.exists()) {
    ...
}
    
// almost unreadable
if (!file.wasNotRemoved()) {
    ...
}
```

###  Don't do this...

Some things which should not be present in a Java source file:

* Non-private, non-final static members 
* Non-private instance members (always generate an accessor for those) 

###  Don't use constant values directly, use named constants

The java code should never contain direct constant values:

```
return "yes".equals(usage);
// or
if (fieldName.equalsIgnoreCase("TABNAME"))
```

Always place constants in a separate public static final member of the same class or a separate Constants class.

###  Don't change input parameters

Avoid changing the value of method inputs. A caller of a method (in java) normally does not expect this. If a parameter value really needs to be changed then make this explicit in the method naming.

###  String comparision using ==

Don't do String comparison using ==:

```    
if (newC_ValidCombination_ID == "") {...}
```

Do this:
 
```
if ("".equals(newC_ValidCombination_ID)) {
```

###  Be careful with the type of the argument using equals

Consider the following example:

```
BigDecimal fAmortizationvalue = ....
if (!fAmortizationvalue.equals(0)) {...}
```

This is wrong (the if-clause is always false!) as the argument 0 is cast to a double by java. A double is always unequal to a bigdecimal.

###  Immutable types: methods which returns the adapted object

There are certain methods in the java api which do not change the method but return an adapted object. Note that this especially applies to immutable objects. Here are two examples of wrong code:

```
BigDecimal priceList = new BigDecimal(0);
String str = "aaa";
priceList.setScale(PricePrecision, BigDecimal.ROUND_HALF_UP);
str.replace("aaa", "bbb");
```

The setScale and replace methods will not change the priceList resp. str
object but will instead return a new instance. The correct code is:

```
BigDecimal priceList = new BigDecimal(0);
String str = "aaa";
priceList = priceList.setScale(PricePrecision, BigDecimal.ROUND_HALF_UP);
str = str.replace("aaa", "bbb");
```

###  Use static or non-static members in a servlet

One running Etendo instance will only have one or a few instances of each servlet object. The servlet container (Tomcat) can use one servlet instance for multiple threads at the same time. This means that multiple threads access the same servlet instance and call its methods, having access to the same
member (static or non-static).

To prevent multi-thread issues no servlet class should have static or non-static members which are manipulated by the post or get methods.

###  Naming Don'ts

Don't use Spanish or other non-English words or terminology.

Don't use encoding in names: hungarian or member (the preceding underscore), don't start an interface name with a capital I.

##  Test Driven Development

It is crucial that for new functionality one or more testcases are created in the Etendo testsuite. It makes a lot of sense to support your coding with testcases:

* A testcase proofs that the functionality is implemented and works correctly. 
* A testcase can validate that the functionality still works in the future. 
* Testcases provide a much easier (and therefore more productive) entry point for testing functionality than starting Etendo and going through the webinterface. 
* A testcase can be used as a demonstration and a description on how the software should operate. 

Etendo testcases need to be created in the src-test folder of the Etendo project.

See this [How To](../how-to-guides/how-to-create-testcases/how-to-create-jest-testcases.md) and this [How To](../how-to-guides/how-to-create-testcases/how-to-create-junit-testcases.md) for more information on how to create test cases in Etendo.

##  Quality and Conventions

For information about this point, visit [quality and conventions](http://www.slideshare.net/srikanthps/practices-for-becoming-a-better-programmer-presentation?src=related_normal&rel=1443810){target="\_blank"}.

##  Be-aware-of

There are also some standard Java constructs which should be used with some care and with some understanding of the underlying processes:

###  ThreadLocal and Tomcats re-use of Thread objects

A ThreadLocal is a great mechanism to store singleton instances per thread and make them only available in that thread. However, when using ThreadLocals one needs to understand that Tomcat re-uses thread instances from one request to another (not the at the same time). This means that data stored in a ThreadLocal in one thread can re-appear in another request (re-using that same Thread object).

###  Class.forName and classloading

When you dynamically need to load a class you have different classloading options. Within tomcat using Class.forName works. However, it is important that you understand how java classloading works when using dynamic classloading mechanism. For some background see this and its references: [Java classes and class loading](https://developer.ibm.com/languages/java/){target="\_blank"}.

###  Synchronized Blocks

Synchronized blocks are not always a safe way of handle multi-threaded access. See here for a detailed description of the underlying processes and possible solutions:  [Double-Checked locking](https://www.cs.umd.edu/~pugh/java/memoryModel/DoubleCheckedLocking.html){target="\_blank"}.

---

This work is a derivative of [Java Coding Conventions](http://wiki.openbravo.com/wiki/Java_Coding_Conventions){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.