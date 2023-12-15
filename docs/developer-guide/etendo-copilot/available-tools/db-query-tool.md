---
title: "Query generation from Natural Language: DBQueryTool"
tags:
    - Copilot
    - IA
    - Machine Learning
    - Database
---
:octicons-package-16: Javapackage: com.etendoerp.copilot.dbquerytool

# Overview
Generate SQL queries with Etendo's contextual knowledge from natural language.

### Functionality


1. Add Copilot DB Query Tool dependency in the Etendo Classic project, In `build.gradle`, add:
    ```groovy
    implementation('com.etendoerp:copilot.dbquerytool:1.0.1')
    ```

  
2. Restart Docker image using `./gradlew copilot.stop` and `./gradlew copilot.start` tasks


3. The tool can be executed with:

``` bash title="Terminal"
./gradlew copilot.do -Pprompt="Query's description"
``` 
Copilot will infer from the prompt that it must use the DBQueryTool and will execute it. By default, it will access the etendo classic database, but you can tell it in the prompt to access another database.


4. The tool will execute an agent that will ask to the database for the information necessary to generate a query that provides the necessary information to respond to the user's prompt.

### Example

Having Copilot running, we can execute the following command:

``` bash title="Terminal"    
./gradlew copilot.do -Pprompt="Can you generate a query to know  the name of the best 5 customer of junuary 2021" 
```
The tool will generate the following answer:

***Here is the SQL query to get the names of the top 5 customers for January 2021:***

``` sql
SELECT bp.name, SUM(inv.grandtotal) AS total_sales 
FROM c_invoice inv 
JOIN c_bpartner bp ON inv.c_bpartner_id = bp.c_bpartner_id 
WHERE inv.issotrx = 'Y' 
AND inv.isactive = 'Y' 
AND inv.docstatus = 'CO' 
AND inv.dateinvoiced BETWEEN '2021-01-01' AND '2021-01-31' 
GROUP BY bp.name 
ORDER BY total_sales DESC 
LIMIT 5;
```