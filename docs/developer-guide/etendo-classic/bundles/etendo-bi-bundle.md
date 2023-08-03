---
title: Etendo BI Bundle | Technical Documentation
---
## Overview

In this section, the user can find technical information about the Etendo BI Bundle.

## Etendo BI Connector

### Technical Aspects

To ensure proper functioning of the script, follow the steps below:

- rsync must be installed in our system, since this is the tool we use to connect to the server.

`sudo apt install rsync`


- Make sure you have python3 installed on your system. You can verify the installation by running

`python3 --version`

If it is not installed, run `sudo apt update && sudo apt install python3`

- It is highly likely that pip3 comes bundled with the installation of python3. Verify if it is installed by running 

`pip3 --version`

If it is not installed, run `sudo apt install python3-pip
`
- The user needs to install libpq-dev to ensure seamless communication and compatibility between our python script and the postgresql database.

To install it, run `sudo apt install libpq-dev`

- The following libraries need to be installed using pip3 for them to work: psycopg2, pandas and requests. You can install them by running:

`pip3 install psycopg2`

`pip3 install pandas`

`pip3 install requests`

### Etendo BI Connector

In the filesystem, two new directories should be created. One will contain the **logs files**, one for the **rsync execution** that will contain information about the file upload to the server; another file called **syncScript.log.{datetime}**, that will contain information about the script execution (most of this information can be seen in the **Logs Monitor window**, but if for any reason the window cannot receive this information, it should be able to be seen using this **.log file**).

In this example, in the path where the script is allocated, a new directory named “Etendo” should be created. Inside it, there should be two folders for the organization that set the background process (F&B US West Coast).

`drwxrwxr-x 1 openbravo openbravo 9,1K jun 8 16:52 ETPBIC_SyncScript.py
`
`drwxrwxr-x 4 openbravo openbravo 4,0K jun 8 17:39 Etendo/
`

Inside the **Etendo/** folder, we have:

`drwxrwxr-x 2 openbravo openbravo 4,0K jun 8 16:54 F+B_US_West_Coast_logs/
`
`drwxrwxr-x 2 openbravo openbravo 4,0K jun 8 16:54 F+B_US_West_Coast_output/
`

The **output directory**, will contain all the **CSVs** that should have been uploaded to the server.

!!! info
    Remember that the main folder is created using the prefix of the “Client” variable that is set on **BI Connection window**. If two connections have the same value for “Client” variable, these directories will be overwritten.


This is the content of Ete\_Example.csv and BASE\_Example.csv files: 

!!! info
    Remember that since any column is not being overridden, these files are the same. 


![](/docs/assets/drive/Y4E0AENgxCWmVoMCapDwvyeO4C0sALvcF7SFWvbxeT5GPcThHq0EgmN1avZxkVhNjWqYYa8phTQ_cnA-RBn1P8-DmePbVoOoN9qTb1uk1kAFG9ccvM2nCxVcHBRpom4t_4SlZkJYdzZX9JtTyEY5Qlg.png)

On the other hand, this is the content of FULL\_Example.csv:

![](/docs/assets/drive/BAPACrYCcoprIrjoMndmxL7d7u1GFOS32ZZMCBXS3S6DsRdZpDRPgRblzPKMTlM2b1QTFLf2mgy7w4LaI_bFnNc9-AwGsl78PIlqpD4o0YkTsXO-qp6h9fFR392DYJRqvZfvefs-hLLbGE04vvU8OoU.png)

!!! warning
    Make sure to have the corresponding permissions to connect to Filews, since an incorrect configuration can lead to an error.


