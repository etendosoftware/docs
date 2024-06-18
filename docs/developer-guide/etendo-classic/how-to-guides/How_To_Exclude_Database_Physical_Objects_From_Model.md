---
title: "How To Exclude Database Physical Objects From Model"
tags:
    - model
    - database
    - exclude
--- 

##  Objective

Etendo Classic keeps track of the database physical objects (such as tables, views,
functions, sequences or triggers) through an utility called dbsourcemanager.
This utility is able to export all the database model object definitions to
XML files, which are stored in the src-db/database/model folder (both in Core
and in modules).

This tool is designed to work in a multiplatform environment, both supporting
Oracle and PostgreSQL. This means that sometimes if specific syntax or
features of a particular Database Management System are used, the tool might
not support them.

In these cases, a possible approach is to create these specific objects using
a Module Script (you can find more about them  here  ), and then exclude them
from the database physical model of Etendo Classic.

##  Excluding objects in modules

Objects are excluded through a file called excludeFilter.xml. This file should
be located inside the src-db/database/model/ folder of the module (if it
doesn't exist, you will need to create it), and it follows a very simple XML
format. Here is an example:

    
    
    <?xml version="1.0"?>
      <vector>
        <excludedTable name="TEST_TABLE"/>
        <excludedView name="TEST_VIEW"/>
        <excludedFunction name="TEST_FUNCTION"/>
        <excludedTrigger name="TEST_TRIGGER"/>
        <excludedSequence name="TEST\_%"/>
      </vector>

This file will exclude the table TEST_TABLE, the view TEST_VIEW, the function
TEST_FUNCTION, and the trigger TEST_TRIGGER from the model, and therefore they
will be neither exported nor removed, nor modified in any way during the
normal database management tasks (update.database and export.database).

The use of  SQL Wildcards  is supported, so the same treatment will be done to
all sequences whose name begins with **TEST_** . All exclusions whose name
contain the '%' character will be treated as wildcards. When defining the an
exclusion using a wildcard, remember to escape with a backslash the '_'
characters, unless it is meant to be used as a substitute for any single
character.

