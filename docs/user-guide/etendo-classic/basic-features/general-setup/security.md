---
title: Security
---

Security folder allows creating and configuring basic security entities such as users, user roles and access rights.

## User

### Introduction

A user is an entity which can log into Etendo whenever it has a password and at least one role assigned to it.

![](/assets/drive/uYk0-n-xUoagkerOKb87gcQ11qfxJ4C2C_uPR-SR_HlmbDw89FyUm7UY86xbdoD3TjOPpEBVFu0aITdVibP7fnpylt_fn8SttMp0fH3HkNOAle71cVvxAmMtvbMPkBN4rHrhr21j.png)

As shown in the image above, Etendo allows the user to sign in by entering a username and a password previously created in Etendo. The user assigned to that username will be able to sign in only in case it has at least one user role assigned to it.

### User

User window allows the user to create as many Etendo users as required. Each person accessing Etendo can have a different user assigned.

![](/assets/drive/Xu1oqRnWMgbWI8-qp1RP-stpJ2YwNnKLJr04-gRcVOrIEkJm_er9fWwpe4F2Ncy_u3pATEEGw7t59JJrUW2y9QSsmNWTT9XXlC0cZuqlakWhF2KIfYfw6IaJhrseTY1tKjE0Uavl.png)

As shown in the image above, a user can be created by entering the basic information below:

- the _User First and Last Name_
- the _"User Name"_ and the _"Password"_ to use for logging into Etendo
- and in the case of being an "Employee", the employee business partner records in the field "Business Partner", under the "More Information" section.
- the _"Expired Password"_ checkbox: if it is checked, the user's password will be set as expired and when the user logs in, he will be forced to change it.

### User Roles

Roles are the connection between users and access rights. Each user can have more than one role assigned, however, a user can only log into Etendo by using just one role.

![](/assets/drive/IdpYeASr5qFi9zCa5EgsKRJfg54EoyBsxbVbj3d7DIbN-8XztHzj2QI35lguEXIKt6FxAmkozQnh7sGeMaKYD4m7-x5QSemv2M48ShmpCxhVWCLFwGa4e94oA1yl4K7-JprsrIcf.png)

For instance, it is possible to create and configure a role for Sales, a role for Finance, a role for Warehouse, and another role for Procurement.

Those roles will have to be configured to allow access to either sales, finance, warehouse or procurement windows, processes and forms. To learn more about how to do this, visit Role.

Whenever there is a new member in the organization, a new user could be created and assigned to any of the existing roles instead of creating and configuring new users permissions every time.

There can be a user having a given role set up as "Role Administrator", that user will be able to add new users to that role.

![](/assets/drive/6lcpMBWvPHq9NQ2VCpAiYVfd_SBR-7j3aDTZ9c4QyqmQi7Nguuid_7y8TQNEXkh7pLH26YU7fKgqpdMEgi1L3aXyKnoyf6PTz-tutOmotGaFFhh7BG_2-QoafKz4JSrmS8mpXVzS.png)

## Role

### Introduction

The aim of a role is to group user/s depending on what parts of Etendo they are allowed to access to and therefore to work in.

!!! info
    Etendo comes with a "super" user named "admin" (_password "admin"_) which can be used to sign in for the first time.

The admin user has several roles assigned:

- the _System Administrator Role_ (this one is assigned to it by default)
    - this role enables admin users to have admin rights to all the existing Clients.
- the _F&B International Group Admin Role_ demo data (this one is also assigned to it by default)
    - this role enables admin users to have "F&B demo data" Client admin rights.
- and besides:
    - every time a new "Client" is created by running the Initial Client Setup process, Etendo automatically creates for that Client a _"Client Admin"_ user linked to a _"Client Admin role"_:
      - the client admin role enables "Client Admin" user to have admin access rights to that Client and all the organization/s of that client once signed in.
      - the newly created client admin role is also assigned to the admin user by default, therefore it will be possible for the admin user to access the newly created Client.

Finally, every time a new "Organization" is created by running the Initial Organization Setup process, a new user and a new role are created and linked to each other, this time the new user role will only enable the user to access that Organization once signed in.

Having said that, Etendo allows the creation of as many new "Roles" as required to be later on assigned to the existing and/or new users.

!!! info
    Roles group user/s depend on the tasks they do and therefore the parts of Etendo they should have access to parts such as windows, processes, forms, widgets and views.

### Permissions Inheritance

It is possible to configure roles to retrieve their access to the different Etendo elements automatically, by inheriting them from other "parent" roles. This configuration is possible thanks to a feature known as Role Inheritance.

Having a role, it is possible to assign one or more template roles to it. This way, all the elements which are accessible by these template roles will be available automatically for that role as well.

Besides, any change done in a permission of a template role will be propagated automatically to every role inheriting from it.

!!! note
    It is only possible to inherit permissions from template roles, which are manual roles as well.

When inheriting from multiple roles, the permission application order is determined by the sequence number of each inheritance. This means that if a particular permission is inherited from multiple inheritance, the permission will be taken from the inheritance with higher sequence number.

This process eases the role management, specially when the number of roles defined for a Client is high. Thus, it is possible to define template roles to give access for a particular set of elements, and then create multiple combinations of functional roles in order to give personalized access for the different users. This is illustrated in the picture below.

![](/assets/drive/vyHTH7_aVNAVElZ2_BGWT5QcVh9MD3w_DCfz20k4Bu6mxa_QCvrKo2ufgIMmvqericF1SZnMm4ONeysEKiw2kON-47niJ5HlcjaVqGiiqPkcNyg9k0FOmnZHHfbqpioJ9At6rbTI.png)

The current list of inheritable elements include the following: organizations, windows, tabs, fields, processes, forms, widgets, views, process definitions, preferences and alert recipients.

For the case of preferences and alert recipients, there are some restrictions to make them inheritable:

- A preference is inheritable if it has a template role set in the Visible At Role field.
- It is not possible to create more than one preference with exactly the same visibility settings for a template role.
- An alert recipient is inheritable if it has the User field empty.
- It is not possible to create more than one inheritable alert recipient with the same alert rule for a template role.

!!! note
    This mechanism takes into account the permissions manually given to the roles. This kind of not inherited access is not affected (not modified) in any case by the inheritance process.

It is also possible to force the recalculation of the permissions of a role, using the _Recalculate Permissions_ process. But following the common flows of a Role configuration, all the inheritances are calculated automatically, so this process is not necessary. For this reason, it remains hidden.

As mentioned before, the changes (create, edit or remove) done in a permission which belongs to a template role will be propagated automatically to all the roles currently inheriting from it. For this reason, a warning message is displayed on the _User Interface_ in order to inform users about the implications of this kind of action.

This warning message is similar to the one shown below. It appears when creating or editing a record that belongs to a template role, in a tab of an inheritable entity.

![](/assets/drive/ibtK-OMAXBsv2UVQXFaPN7YvQMlh2rgo41Vt21hwrkhk0Grj3gy0Y_7tYhGZU4JZaX7i75-eo6xHmT7P7bHhUWyy2xIpcK5VB8rC7PqSxERaqBP7HXaLXKSeiyNf_1Sj_ZXhxDzb.png)

### Role

The Role window allows the user to review, create, configure and maintain the roles to use in a given client.

![](/assets/drive/8MOJrcJaif8MbvpR7NwOIA6JjqOIlmOf3df8nsTRJa7Zq02aanCB7SGImtBiEGqou4crWjRy_nGJNhUVj3rHpcNyYOVw8H-F_X4veFkEtGw_6KCGoJxom1R_MkOlm0pJhIbEYzMB.png)

As already described, there are roles automatically created by Etendo which can be reviewed in this window.

Besides, this window allows the user to create new roles for a given client. Roles creation can properly be done by using a Client Admin user & role.

The fields to fill in are:

- the Name and a brief Description of the role
- the "User level" which is a step forward _"Data Access Level"_ to be defined at Role level.
    - User level allows the user to limit the records which will be accessible in entities such as windows, processes or forms for a role; or even to limit the access to a given entity for a role:
      - Every table in Etendo has a "Data Access Level" defined. The options available are:
        - System, this level allows the user to see System Client records and (\*) organization records, for instance application dictionary records.
        - System/Client, this level allows the user to see any Client record and (\*) organization records, for instance master data related records such as Countries.
        - Client/Organization, this level allows the user to see any Client record but System Client and any Organization including (\*) Organization, for instance master data related records such as Products.
        - Organization, this level allows the user to see any Client record but System Client and any Organization record but (\*) Organization records, for instance transactional data records such as Purchase Orders.
    - User Level available options are:
      - _System_, if a table is defined as "System" data access level, a user role which has this user level assigned will be able to see the records of any Client including System Client records, in an entity such as a given window or form.
      - _Client_, if a table is defined as "System/Client" data access level, a user role which has this user level assigned will be able to see the records belonging to any Client but System Client, in an entity such as a given window or form.
        - On the other hand, if a table is defined as "System" data access level, a user role which has this user level assigned will not be able to see any record as all of them will belong to System Client.
      - _Client + Organization_, if a table is defined as "Client/Organization" data access level, a user role which has this user level assigned will be able to see the records belonging to any Client but System Client and any Organization including (\*) organization, in an entity such as a given window or form.
      - _Organization_, if a table is defined as "Client/Organization" data access level, a user role which has this user level assigned will only be able to see the records belonging to a given organization but (\*) organization, in an entity such as a given window or form.
    - Additionally, depending on the role's user level, no data at all is visible based on the table's access level. This restriction can be bypassed by setting _Bypass Access Level Entity Check_ preference to _Y_, the cases when entity is not accessible are:
      - If access level is System and user level is not System
      - If access level is Organization and user level is not Organization or Client+Organization
      - If access level is Client/Organization and user level is not Client, Organization not Client/Organization
      - If access level is System/Client and user level is not System or Client/Organization
- Manual check. The role automatically gets all standard user plus admin privileges, even when new elements such as windows, processes, forms, widget classes, organizations are added unless the Manual check is enabled.
    - If the manual check is enabled, it will be possible to manually assign access to windows, processes, etc by manually selecting them in the corresponding tab or by using the process button "Grant Access".
    - Grant Access process button allows the user to select:
      - the _module_ or application area for which access is required, modules such as Financial Management or Production Management among others.
      - and the _entities_ of the module selected for which access is required, entities such as windows, processes or forms among others.
    - If the Grant Access process is executed for a role marked as _template_, the granted accesses will be propagated automatically to the roles inheriting from it.
- Template check is shown for roles which have a manual access assignment (Manual flag is Yes). Roles marked as template are those that can be used by other roles to retrieve their permissions automatically, using the Role Inheritance mechanism.
    - For this reason, just template roles can be selected in the Inherit From field of the Role Inheritance tab.
- Restrict backend access: If checked, this role will not have access to the backend (ERP). It will however have access to other applications (such as the WebPOS).
- For Portal Users: If checked, this role will have a simplified (portal) interface, where he only has available the workspace widgets. Portal interface changes the look and feel of the workspace. Top page menu and left-side menu are hidden. Usually a role for Portal Users gives access to users only to their own information using widgets.
- Portal Admin: If checked, the Portal Role will have Portal Administrator privileges.
- Is Web Service Enabled: If checked, web services will be able to obtain data for users with this role. It applies to both JSON REST and XML REST web services.
- Advanced check is shown for roles that have an automatic access assignment (Manual flag is _No_) and automatically grants access for such roles to all Advanced Features.
    - Manually created roles (Manual flag is _Yes_) have their own configuration which can include advanced features or not so this flag is not shown for them.
- Client Administrator checkbox allows a role to admin other users' _Workspace_ as well as _Customized Forms"_:
    - In other words, a client administrator role can assign widgets to the workspace of any client user as well as customized forms.

### Org Access

Org Access tab allows the user to define the organization/s to which a given role will have access rights to.

As already mentioned, every record in Etendo belongs to an organization, therefore the only way for a user role to edit a record which belongs to an organization is to provide that user role with access to that organization.

![](/assets/drive/vE-K35fSEj9-BIvgbMGezZvFFgFx4-bfY-LNbMosiyjun4B_-bSKiWnHr-K7bpJSnYwrSypNacZYFmcO9x46g3yGgrHxrywB-z2Agfywx-qVesqxPN9ruiBg45aTxqkyn15BsOkb.png)

- _Organization Administrator_ checkbox allows a role to admin other users' "_Workspace_ as well as _Customized Forms_":
    - In other words, an organization administrator can assign widgets to the workspace of any user of the organization as well as customized forms.

### User Assignment

The User Assignment tab allows the user to add users to a given role.

![](/assets/drive/iBeXu8RdIKr-srDU5Q-1Y5e5wYtbvNbXqD8KtMx8MK2gHEXc9BJUcYsA19OgHzCNv7chh30Ws8bVjbtjFkllwl5w8kZZ2ZoAbiXLOeFJDzwEisQu04z8dGAj3CmIy0OOxneMJtz6.png)

"_Role Administrator_" checkbox allows the user to administer the given role for:

- Widgets: they will be able to set default widgets that will be seen by other users with the same role.
- Saved Views: this user will be able to share with other users with the same role the views she saved.

!!! info
    As _Role Administrator_ flag allows the user to modify behavior of other users with the same role, it should only be granted to trusted users.

### Window Access

This tab lists and/or allows the user to add the windows to which a role will have access to.

As already mentioned, every time a new role is created and saved without selecting the "Manual" checkbox, Etendo automatically fills in all the windows in the Window Access tab.

The information above means that the newly created role will have access to every Etendo window.

![](/assets/drive/vt5fH1QoVLs_KcIpoESYAQqhSe01e6oHVVFbF-UQy6fwJnDu8B4qOgQDCI34dQheclrgChwDy-IuurthKMqxAljaRU-jVczgUCGnXrXDTv2vERvhxlgGjRy7SA6ivWpqpYMBhcmQ.png)

Having said that, if the "Manual" checkbox is selected, it will be required to _manually_ add a subset of windows which will be accessible for a given role, or it will be required to automatically add them by using the action process "Grant Access". This process will allow window access for a given Etendo module or area such as Projects, Finance or Sales.

_Editable Field_ checkbox defines if the accessible data in a window can be edited by the role or not.

### Tab Access

It defines whether a tab is editable or read-only for a concrete role.

In a window accessible by a role, it is possible to define for each of its tabs if they are editable or not through the _Editable Tab_ check.

If the window is editable (_Editable Field_ is checked), by default all its tabs will be editable. But it is possible to define some of them not to be editable for this role by adding them in this tab and setting to false the _Editable Tab_ check. Note this is only true if the table behind the tab is editable for the role.

In the same way, having a non-editable window, it is possible to define some of its tabs as editable by checking _Editable Tab_.

### Field Access

It defines whether a field is editable or read-only for a concrete role.

Field Access tab works very similarly to Tab Access tab, allowing the user to define write access up to a field granularity level.

So if a tab is editable for a role, a concrete set of fields can be made read-only for that role, adding a new row in this tab for each field and setting false _Editable Field_ of each of them. Or in the other way around: in a non-editable tab, fields can be editable if they are added and their _Editable Field_ property is checked.

When editing a tab with some fields defined not to be editable in this way, backend checks modifications in that tab to prevent this to happen. Note this also affects the field in case it was modified by, for example, a callout or a default expression. This is controlled by the _Check on Save_ property, unflagging it, this check will not be performed allowing thus the field to be modified by a callout.

### Report and Process Access

This tab lists and/or allows the user to add the reports and processes to which a role will have access to.

As already mentioned, every time a new role is created and saved without selecting the "Manual" checkbox, Etendo automatically fills in all the reports and processes in the Report and Process Access tab.

Above means that the newly created role will have access to every Etendo report and process.

![](/assets/drive/jeSO8cKGRMnO5jlOseLchbPh4OE2fDeLeAAS0VSOIngREivxtfTmTPmNLaDwnn7ujstw7z6Pgqp0oZLZAHxwT1XwtyGmlZdj-vuNEBXnBq1dFNo5UvBFIC_CIAJc6Tn2gweJJPKq.png)

Having said that, if the "Manual" checkbox is selected, it will be required to manually add a subset of report and process which will be accessible for a given role, or it will be required to automatically add them by using the action process "Grant Access". This process will allow report or process access for a given Etendo module or area such as Projects, Finance or Sales.

_Editable Field_ checkbox defines if the accessible data in a report or process can be edited by the role or not.

By default, access to processes in a standard window given from a button is inherited from the permission to the window. So if the role has access to the window, it will be possible to execute all the processes defined in that window, regardless if there are explicit entries for them in _Report and Process Access_ tab. This default behavior can be changed in two different ways:

- To revoke this inherited access and manually decide case by case which are the accessible processes, it is possible to define a "Secured Process" Preference (at system level or for that specific window) with "Y" as value.
- If the developer defined the process as _Requires Explicit Access Permission_. In this case, permissions will never be inherited for that process.

### Form Access

This tab lists and/or allows adding the forms to which a role will have access to.

As already mentioned, every time a new role is created and saved without selecting the "Manual" checkbox, Etendo automatically fills in all the forms in the Form Access tab.

The information above means that the newly created role will have access to every Etendo form.

![](/assets/drive/h71SGbrOND-3ZRiDfheu69SJe6ZUIfQdyVOKmL_RaRtqSCRmQ84JoLrhPok37CDsfNRt0BbqoKwNzchby0i1ffWbKxN1JZZy2wBjC_akKrtaYwtR9FNCgEJaYGEFtse9xsx2kG4_.png)

Having said that, if the "Manual" checkbox is selected, it will be required to manually add a subset of forms which will be accessible for a given role, or it will be required to automatically add them by using the action process "Grant Access". This process will allow form access for a given Etendo module or area such as Projects, Finance or Sales.

Editable Field checkbox defines if the accessible data in a form can be edited by the role or not.

### Widget Class Access

This tab lists and/or allows adding the widget classes to which a role will have access to.

![](/assets/drive/UJdYTlYdE7iCbPZXvMLbM-FtRsvCjm1H0ogLpoAgaHlt18r4-hS0gB0jXOCtea26kAn3l9phNMuoqFO5uvrKDqHnd_99mcY6FqmqGhHKwcwIiozXLsji0LHlgp6KWLzKuvVYq6S_.png)

Widgets are _User Interface_ elements which can either be placed in the Users' Workspace tab or be part of a generated window.

### View Implementation

View implementation tab allows the user to select customized views.

A view implementation is a completely custom implementation of a main view.

The access to a _custom view_ can be controlled through this role access tab.

![](/assets/drive/5OCz4Fl8K2i8uYaKdMnh3lg-DT_9IQBDjimbD37HCtwzOs74M-OTqbTorDwTzxEQaWJBKZRxkhNJc_jF-4kjLOllZSlfZe_9kcngt9KUQB0X3KVYFyeOblGXuzo0LCGDI-C_QlvI.png)

For additional information about views, visit How to implement a new main view.

### Process Definition

Grants access to Process Definition. By default, access to process definitions in a window (given from a button), is inherited from the permission to the window. To cancel this inherited access and manually decide case by case which are the accessible processes, it is necessary to define a "Secured Process" Preference (at system level or for that specific window) with "Y" as value.

![](/assets/drive/IFXcBPxniL5TViWp3QIr2LiircvQoutdDPZ4K-zMHibWBRtwsI2fNh8dTXWG5H8_GROHo17oFdKjb-Kuj696jezS3flqH9VJL8yAlFYFV0__mtN4aDKFHrIuosLt28EfSLpfT5iR.png)

Access when the process is invoked from a standard window button is inherited in the same way that for Processes.

### Role Inheritance

It allows defining an inheritance for a role. An inheritance is a relationship between two roles: if role A inherits from role B, that means that all the permissions that role B has for different application elements like organizations, windows, reports, processes, widgets etc. will be automatically inherited by role A, allowing it to access those elements in the same way as B. It is also possible to define an inheritance hierarchy, i.e., a role can inherit from different roles, and the priority (order) to inherit the permissions is defined by the sequence number. This means that if two inheritances have accesses in common, the accesses of the inheritance with lower sequence number will be overridden with the accesses of the inheritance with higher sequence number.

Within this tab is where the Role Inheritance configuration of a particular role is set.

![](/assets/drive/KI9-ImqA0ErnTQS_fepHzt63s_3ExEUeRwCXREoaE2NKc1e13FAmtPhHnCQC4CPLwWzbUvWZbertcWG81CDPmYaZzLhN8IrliDLcJ9V48S3VxosZwI2vzSlPc0suV5WKwYcPi8JF.png)

The fields to fill in are:

- **Inherit From**: In this field, it should be selected the role whose permissions will be inherited. It defines the role that will be used to retrieve access to its permissions automatically.
- **Sequence Number**: It defines the order in the application of the role inheritance, when having multiple records in the tab. The lower this value is, the earlier will be retrieved the permissions of the related template role. This means that if the same permission is accessed by two template roles selected to inherit from them, the permission related to the inheritance with higher sequence number will override the other one.

### Dynamic App

!!! info

    To be able to include this functionality, the Financial Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Platform Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=5AE4A287F2584210876230321FBEE614){target="_blank"}.

In this tab, you can configure the dynamic applications that the selected role has access to.

![](/assets/user-guide/etendo-classic/basic-features/general-setup/security/DynamicAppRoleTab.png)

Fields to note:

- **App:** In this drop-down menu, you select the application that you want to assign to the role.
- **Version:** Here we assign the version of the application we want to use in this role.
- **Active:** To select if this application is active or not.

## Role Access

This window defines access to DB /database tables and columns for selected roles.  
Edit a role to give or withhold the necessary access to tables and columns tables.

### Table Access

Create or edit access to DB tables for a selected role. The user can give access to the needed information by selecting the options displayed in the table tab.

![](/assets/drive/ltwp9ZQne8C_2iz5c7u3hay0dodgaB28TeFFxVkLJqhFV3Zgq9LMahoeVrH2BRiz6NH9n1QeCsDSrOoPD_CtKV8cYZULNDDPG5Fly-WhZo5h7_2ASJRlnoS_GinX2nYC6efQebJ6uZYnYAeyabg.png)

## Audit Trail

### Introduction

Audit Trail allows the user to monitor every data change done in any table or entity through the user interface.

Audit trail feature monitors data changes such as:

- Insert
- Update
- Delete

Audit trail feature must be enabled by the "System Administrator Role" in the Application Dictionary, as the first thing to do is to configure the table/s for which this feature is going to be enabled.

Once a change has been made in a table for which the audit trail feature has been enabled, it is possible to monitor that change through the user interface by using the action button "Audit Trail".

![](/assets/drive/V-wLKxec4uzSuG-eFItBU00cQYeO5SNhiLTDkY78kPRaK6e-P_R_z39-K5icHtUSX-WjoeFL34_Iv45c0aym2FRV9_F_e0W6QA0U8Lim_qkovbX44ihOl-nH-mKEio1pSpfQDqlm.png)

### Audit Trail

Audit Trail view displays read-only information about all the recorded data changes done in the tables for which the audit trail feature has been enabled.

![](/assets/drive/CkScAz_BHFw9uZIejCEG18y9IOkyiO23K5CMqCRWCkc-DEAWZ0x5G8RyDwjqApky49FILfUisRIJUnqS_Sfob0j128cKfhFFQhfOI92bmbTAPsN1TyfGVMaPXeoj9tbBzqsTB-r4.png)

The changes done in a given table, column and record are viewed by showing the corresponding record ID or UI of the records in the database.

### Configuration

In order to track audit information, the system administrator needs to perform two tasks:

- Enable the audit trail for one or more tables in the system
- Run the 'Update Audit Trail infrastructure' process

In the following sections, a step-by-step guide with more detailed information is provided.

### Enabling audit trail for a table

Enabling/disabling the audit trail feature for a table is done in the Table definition in the Application Dictionary.

- Switch to the System Administrator role
- Go to Application Dictionary > Tables and Columns
- Navigate to the table for which you want to enable the Audit Trail
- Switch to Edit View
- Mark the "Fully Audited" checkbox and save

#### Audit Inserts

When a table is flagged as Fully Audited, the users can decide if they want to audit the insertions done in that table.

![](/assets/drive/ebTtUMQskmHQd1Fd5BWoW0_lKwtwgNTn41V1uJKV4RGTKR_uXKuR_PqU4rzTUBVQct38OejbovWWycB-z1A7YEvwNedzpv6VCi38eHb2telDh9994cV4vCW1QEOGlDw1Ojs11Und.png)

If the Audit Inserts field is checked in a table, when a new row is inserted in that table several records will be inserted in the Audit Trail table, one for each column in the audited table. These records will contain the original value of the columns of the new row.

Usually, it is not necessary to store this information, because the original value of a column could be easily obtained by using the Old Value and New Value fields of the Audit Trial table that correspond with that column. If the Audit Inserts field is left unchecked, only one row will be inserted in the Audit Trial table for each record inserted in the audited table. At least this one record needs to be inserted in the Audit Trial table to be able to store which process was used to create the record in the audited table.

#### Excluding columns

By default, when a table is audited, modifications in any of its columns are audited. In some cases, it makes sense not to audit changes for some of them. This can be configured by setting the _Exclude Audit_ flag in _Tables and Columns > Table > Column_ tab.

![](/assets/drive/Xy3wTyW3wrUeerAoND_Rw2c6wVVhxkq_AEzzTjBLLpiBg6VsMWcQjAn6T4te4akp_o-x381v3wT3012cttvLqjKWRsd-Tfe0Go0FX1KGlG_vSG57Bm4yo8ZnB0gxdTSV3qi7f-4b.png)

### Running the System Compilation

The audit trail system uses a number of generated triggers (one per table to be audited) to collect the audit data for all changes.

These triggers need to be regenerated, when executing a system compilation, once the following actions have been performed:

- The Audit Trail feature has been enabled or disabled for a table
- There has been any structural change to a table being audited (i.e. new columns, changed columns)

### The Audit Trail Popup

For the set of tables for which the audit trail feature has been enabled, the button ![](/assets/drive/tmlPernhlkGB49t7gLt12N3zfxbYevzxuPC65DZavmEO8p5UBe2_sO_YD6lBTkhBvnNrQ64jkRAnuahaKRTGnLPGUvmSEX_K5_Ekh5Ojd-21ZyZ4KWEFIjujNg_xqg_PCFahXdJo.png) is shown in the toolbar of the corresponding windows. It gives access to the Audit Trail Popup.

This popup allows examination of the history of the record which is currently shown in the window. It has two main view modes which allow examining the following data:

- 'Record history' of a single record
- 'Deleted records' of a single tab

### The 'Record History' view

This view is displayed when the popup is opened from an existing record via the new toolbar button.

The top area always shows a reference to the entity (i.e. Sales Order) and the record "1000175 - 2016-04-03 00:00:00.0-0.00" for which the history is displayed.

Then a number of filters are available which allow some restriction on the changes displayed to ease the use of records with many modifications.

The grid in the lower area shows all changes done to this record while the audit trail feature was enabled. The changes are shown sorted from the most recent change back to earlier changes.

!!! info
    Only fields which are visible in the corresponding tab are shown here.

A row in this grid corresponds to a single changed field. For changes to an existing record, the number of grid entries shown correspond to the number of fields changed. For new record creations or record deletion, one row in the grid is shown per field of the inserted/deleted record.

![](/assets/drive/xuE5w_TI2LS9M4nl1fyqWctoD-pU08N6dq7mQJT7qr-wsocs2FehRp7Gu1jGCsJUu_UZeo1hmDjBPQRFV_d1aM26q9zxMjXPX5GbX-SZOJYuZTwo1PYtoD-oi3XRzlyS723rbaWL.png)

Finally, a link just on top of the grid allows switching to the 'Deleted Records' view. Following that link will show deleted records for the tab from which the Audit Trail popup was opened.

#### Disable filtering by User

The User filter can be removed from both the 'Record History' and the 'Deleted Records' view. This can be interesting for performance reasons when the number of users available is high. In order to do this, go to General Setup|Application|Preference and add the following preference: Show Audit Trail User filter with value Y.

### The 'Deleted Records' view

This view allows examination of records which have been deleted from a tab and are otherwise no longer accessible in the user interface.

The general layout of the view is similar to the record history view.

An info on the top shows a reference to the entity for which the deleted records are shown. Directly below, a number of filters is available to restrict the records shown.

Then a grid displays all deleted records belonging to this tab/entity. Here one row shown corresponds to a single deleted record and the columns shown are the same as the ones shown in the normal grid view of the same tab.

![](/assets/drive/lsX2HjGHdMbgCKFRs-_KuE1qmeMs2u9cZ5PXrJ5RmYw08PYbdJ6KB_dY93TwaW9ycfaNUc9fEWmsMFKPipMYza0ZCPZdMcl4c9sjFemg7ndkntS2ai5Rs-eePUDaFXXNdKFJ6VOV.png)

This view offers a number of navigation choices to view related or more detailed information.

#### Navigation: Back to history

The first one is Back to history. Following this link, the view is just switched back to 'Record History' showing the same records as shown before going to the deleted records view.

#### Navigation: History of selected record

The next one, View history of selected deleted record below, allows examining the detailed history of a deleted record, instead of the summary view which is shown here.

This detailed history is displayed in the same 'Record History' view, however its top info area notes the fact that the history of a deleted record is displayed.

The following screenshot shows an example of the history view of the same deleted 'Sales Order' entry. Compared with the previous example of this view, new history entries corresponding to the deletion are shown in addition to the older information about the record creation and modification.

![](/assets/drive/GtW2mnbfKHPPLTLwrt_Kqjlbdm7lo_7CLDntpxMg4vRZnjAaRkOeUzxOg19gnju2DAgUuLBNrm0szABl1MVSV5Ft9_5ASwBs9jTI9IYuQt1iBTBU3r2z5J-octdDlOzNknRzXKKz.png)

#### Navigation: Child Tabs

As the last method of navigation, the popup allows filtering records based on a parent record. This can be useful to search for deleted lines belonging to a sales order.

There are two possible ways based on the status of the parent record: still existent or already deleted.

If the parent record (i.e. a Sales Order) does still exist, then the following steps can be done two view its deleted lines:

- Go to the lines tab of the Sales Order
- Click the audit trail icon to open the record history view
- Use the 'Deleted Records' links to switch to deleted records view

As the lines tab is not a top level tab (it has a parent tab Sales Order) the deleted records view is automatically filtered to only show lines belonging to the current Sales Order. As visual information that the information shown is filtered, the top info area shows:

![](/assets/drive/TLPq4qy1yN9UkGD66_5njmuYw_ks8rUXRuOSuS6oXS_BmY92i1kLNyPns4CRsopMKIif0JPp6uJfWpDHgeKgtD07RAR8XcmrVEafUyhiVJ-OEUHhxUF3i77gURAyQPl8yK7PZMLk.png)

If the parent record (i.e. a Sales Order) does not exist anymore, then the same can be accomplished by using the following steps:

- Go to the 'Deleted Records' view of the Sales Order tab
- Search the Sales Order for which the deleted lines should be shown
- Click the _Lines_ link just below the grid

Then the deleted records view will show the deleted lines belonging to the selected (deleted) Sales Order.

### A generated Audit Trail Window

The second interface to view audit data is a normal generated window which is based on the AuditTrail entity, and allows browsing all audit information filtered by the currently active client. Open the Application menu and navigate to General Setup, Security and select Audit Trail.

It offers a raw view of the audit data, meaning that no translation of raw values is done, but instead the raw column values of each change are displayed.

Simultaneously, this window allows a much more flexible filtering/searching.

![](/assets/drive/rw7tPRLbT6ngBKyscK7lPe8F8irNUTp74vKBpDDST539eM5zHpl99Sr2fMXFLMcFks6BVhyNsMfFaSeWHgHYSr2vF2GDYjZ6a5fyAa3Nj2QEcpUhGAL6xOPIVwY177LL6kESljcr.png)

### Limitations

The audit trail feature will record all data changes (for the table for which it has been enabled) with the following exceptions:

- text fields of types (char,varchar) with a length >= 4k will not be audited
- text fields of types (nchar,nvarchar) with a length >= 2k will not be audited
- BLOB fields (binary stored inside the database) will not be audited

### Etendo Advanced Security

The **Etendo Advanced Security** module allows the user to customize several security features such as the following:

- Password Security
- Password History
- User Lockout
- Multiple Session Verification
- Changing Password after Login
- Expiration Time (Autolock Password)

!!! info
    For more information, visit the [Etendo Advanced Security module User Guide](/user-guide/etendo-classic/optional-features/bundles/platform-extensions/etendo-advanced-security/).