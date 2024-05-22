---
tags:
    - Copilot
    - IA
    - Machine Learning
    - Database
    - DB query tool
---

# Database Query Tool

:octicons-package-16: Javapackage: `com.etendoerp.copilot.dbquerytool`

## Overview

Generate SQL queries and retrieve data with Etendo's contextual knowledge from natural language.

## Functionality


1. Add Copilot DB Query Tool dependency in the Etendo Classic project, In `build.gradle`, add:
    ```groovy
    implementation('com.etendoerp:copilot.dbquerytool:1.0.3')
    ```

2. In `gradle.properties` file, you must add `OPENAI_MODEL` environment variables. 

    ```groovy title="gradle.properties"
    OPENAI_MODEL=gpt-4-1106-preview
    ```
  
3. Restart Docker image using `./gradlew copilot.stop` and `./gradlew copilot.start` tasks

4. The tool can be executed with:

``` bash title="Terminal"
./gradlew copilot.do -Pprompt="Query's description"
``` 
Copilot will infer from the prompt that it must use the DBQueryTool and will execute it. By default, it will access the Etendo Classic database, but you can select another database in the prompt.

5. The tool will execute an agent that will ask the database for the information necessary to generate a query that provides the necessary information to respond to the user's prompt.

## Examples

!!! info 
    It is important to clarify that this is a first version subject to improvements.  While it has database context, it should provide enough information in the prompt.
    Note that it is possible to see the log of the call chain made by dbquerytool from the terminal where `copilot.start` is running. You will be able to see the tables involved, the query formed and its execution, if necessary. 


### SQL query generation

1. 
    ``` bash title="Terminal"    
    ./gradlew copilot.do -Pprompt="query to know the name of the best 5 customer of junuary 2021?"  
    ```
    The tool will generate the following answer:
    ```
    🤖 👋 Hello Human!
    🤖 I'm working on your request: query to know the name of the best 5 customer of junuary 2021?
    🤖 The SQL query to retrieve the names of the top 5 customers based on purchase amount for January 2021 is:

    SELECT bp.name, SUM(inv.grandtotal) AS total_purchase_amount
    FROM c_invoice inv
    JOIN c_bpartner bp ON inv.c_bpartner_id = bp.c_bpartner_id
    WHERE inv.issotrx = 'N' AND inv.isactive = 'Y'
    AND inv.docstatus IN ('CO', 'CL')
    AND inv.dateinvoiced BETWEEN '2021-01-01' AND '2021-01-31'
    GROUP BY bp.name
    ORDER BY total_purchase_amount DESC
    LIMIT 5;

    This query will select the names of the business partners (`bp.name`) and the sum of their total purchase amounts (`total_purchase_amount`) from the invoices table (`c_invoice`) for the month of January 2021. It will group the results by the business partner's name and order them in descending order by the total purchase amount, limiting the results to the top 5 customers.
    🤖 Glad to help you! 😃
    ```
    
2. 
    ``` bash title="Terminal"    
    ./gradlew copilot.do -Pprompt="Query to obtain which is the invoice with the highest registered amount?" 
    ```
    The tool will generate the following answer:
    ```
    🤖 👋 Hello Human!
    🤖 I'm working on your request: Query to obtain which is the invoice with the highest registered amount?
    🤖 The SQL query to find the invoice with the highest registered amount is:
    
    SELECT c_invoice_id, grandtotal FROM c_invoice WHERE isactive = 'Y' ORDER BY grandtotal DESC LIMIT 1;

    This query selects the invoice ID and the grand total amount from the `c_invoice` table where the invoice is active (`isactive = 'Y'`), orders the results by the grand total in descending order, and limits the results to only the top record.
    🤖 Glad to help you! 😃
    ```



### Natural Language Queries for Data Retrieval

1. 
    ``` bash title="Terminal"    
    ./gradlew copilot.do -Pprompt="What is the amount of the last F&B España - Región Sur organization sales invoice?" 
    ```
    The tool will generate the following answer:

    ```
    🤖 👋 Hello Human!
    🤖 I'm working on your request: What is the amount of the last sales invoice?
    🤖 The amount of the last sales invoice is $249.00.
    🤖 Glad to help you! 😃
    ```

2.  
    ``` bash title="Terminal"    
    ./gradlew copilot.do -Pprompt="Can you execute which is the invoice (c_invoice) with the highest registered amount?"
  
    ```
    The tool will generate the following answer:
    ```
    🤖 👋 Hello Human!
    🤖 I'm working on your request: Can you execute which is the invoice (c_invoice) with the highest registered amount?
    🤖 The invoice with the highest registered amount in the `c_invoice`
    table has the ID '2D6314F246FE4C21AAE57F12EFD341C5' and the amount is 17,440,824.40.
    🤖 Glad to help you! 😃
    ```
3. 
    ``` bash title="Terminal"    
    ./gradlew copilot.do -Pprompt="Can you execute the sum of the orders in the last month"
    
    ```
    The tool will generate the following answer:
    ```
    🤖 👋 Hello Human!
    🤖 I'm working on your request: can you execute the sum of the orders in the last month
    🤖 The sum of the orders in the last month is $7,063.59.
    🤖 Glad to help you! 😃
    ```