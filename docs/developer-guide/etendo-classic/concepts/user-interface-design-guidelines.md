---
tags: 
  - User Interface
  - Design Guidelines
  - Etendo Classic
---

#  User Interface Design Guidelines
  
##  Overview

This document provides a basic set of user interface design guidelines for Etendo modules as well as for core development. Related to these guidelines are the following documents:

  * For technical guidance, refer to the Developer's Guide. 
  * For guidance on writing documentation, refer to the Documentation Style Guide 

Etendo's modular architecture makes simple development of extension modules possible.

Modularity allows people to develop extensions and to distribute them independently, as well as to leverage distribution channels. Etendo has a central repository that allows users to download and install modules directly from the Etendo user interface, similarly to downloading a plug-in for a browser.

Modules can be shared via the Etendo Exchange, the marketplace for modules. Third parties are encouraged to develop modules and monetize on them by selling them via the Exchange.

It is expected that over the course of time, the number of available commercial and non-commercial modules will grow and dissemination of modules will grow alongside.

A concern is that without guidance or quality assurance, a proliferation of inconsistently designed modules will take place. To avoid this, guidance must be given to the community on how to create high quality, usable, enjoyable and consistent modules.

Currently, Etendo has little or no documented standards for interaction and visual design.

For everyday design & development practice, existing design patterns need to be found in the actual product to be reused. Since most development for Etendo Classic took place inside the Etendo company in a small team, this hasn't been a problem so far, but as Etendo's community grows, not having design standards makes it very difficult to retain consistency in the core product and its modules. It also stirs inefficiency, as good solutions are not reused all the time.

##  Etendo Design Philosophy

The GUI for Etendo was designed with the following objectives in mind:

  1. Efficiency of use. Both one-off and repetitive tasks need to be executed in a highly efficient manner. 
  2. Consistency. Due to its large functional breadth, common denominators in functionality and behavior were identified and made consistent in the GUI. Consistency reduces the user's learning curve, reduces task execution effort and simplifies custom development. Although in specific cases a fully dedicated GUI to a task is justified, the general guideline is that consistency is king. 
  3. Customizability. Enterprise level business applications will never be one size fits all. This also applies to the GUI. Its actual usage is explained in the User Interface Introduction. 

##  Editable Standard GUI Elements

The Etendo desktop GUI contains a limited set of elements that can be reused to adapt existing or build new functionality in a relative simple manner using the available tools [LINK TO TOOLS SECTION]. Any creation or modification that is done outside this scope is considered custom development.

The main editable elements are:

  * Workspace 
  * Top Navigation 
  * Toolbar 
  * Help 
  * Forms 
  * Messages 

The subsequent sections in this document will provide more detail on the individual elements.

##  Workspace

The workspace area is the starting point for back office users. It contains a set of personalized widgets that help users perform their tasks. Most widgets show a summarized view of the underlying Etendo transactional data such as sales per region and invoices to be paid. Other widgets point to external data provided by the web or third party applications. Users can freely choose the
quantity and contents of widgets and this guideline document does not want to impose rigid rules on those. It is recommended to follow generic usability guidelines to ensure a great user experience. In specific, widget content should adhere to the following rules of thumb:

  * Since the width of widgets depends on the available horizontal screen space, content should have a fluid layout meaning that text and graphics are rendered nicely for different screen resolutions. 
  * The entire Etendo workspace area may have a vertical slider bar. To avoid more than one slider bar, care should be taken to use additional scroll bars inside a widget and double vertical scroll bars inside a widgets are prohibited as they seriously impede proper usage. Note that widget height can be easily adjusted to avoid vertical scrolling. 
  * It is recommended to reuse Etendo GUI components and styles, especially for widget content that use or point to Etendo data and windows. Widgets of type Query List have the possibility to be maximized. By clicking the maximize button on the right-hand side of the title bar, a new tab will be opened to display the maximized content. The content style is identical to that of the workspace widget with the only difference that different columns can be selected to be shown in maximized state. 

##  Top Navigation

At the top of the screen sits the main navigation that is used to browse and launch the application windows. It also shows possible notifications, help, user profile and a logout button. To the outmost right of this area the customer's company logo sits besides the Etendo logo. None of these elements are customizable apart from the customer's logo that can be uploaded via the System Info window in the Logo Settings section. A height of 34 pixels is required and logos that exceed this will be reduced in size when uploading.

##  Toolbar

In the top part of a window the toolbar can be found. It is contains buttons to actions and processes that are related to the active window and often also to the selected object(s). Action buttons are square and use icons to indicate their function. Process buttons are rectangle shaped and use labels to indicate their function. In most cases the difference between an action and a process is clear, at least on system level. On user level, the difference may not always be clear. As a rule of thumb, a process button should be used for events that change the status of a document and are specific to a certain window and object type. Actions are much more generic, think delete, print, export, create.

###  Icons

Icons are used in the toolbar and in process windows. Tips for designing and using icons:

  * For good-looking icons, use a professional graphic designer to create them. 
  * Use universal imagery that is easy to recognize. Avoid focusing on a secondary aspect of an element. For example, for a mail icon, a rural mailbox would be less recognizable than a postage stamp. 
  * Strive for simplicity. Try to use a single object that captures the icon’s action or represents the control. 
  * Start with a basic shape. 
  * Use color judiciously to help the icon tell its story; don’t add color just to make the icon more colorful. In fact, Etendo 3 using monochrome colors and it is strongly recommended not to use additional colors 
  * Be careful with using icons from free libraries as sometimes copyrights apply. Never "reuse" commercial icons or icons from other applications without written permission from the owners. 
  * Don’t reuse Etendo system icons in your modules as this can be confusing. Currently used toolbar icons can be found in the  wiki GUI documentation 

###  Buttons

Buttons are generated via the application dictionary using references. The following rules of thumb should be adhered when defining buttons:

  * Do not deviate from the standard button design by creating them manually. 
  * Do not create buttons with labels longer than 24 characters. 
  * The button should be named after the action that you are going to perform by pressing the button, not after the current status of the object before the action. The label starts with a verb followed by the object to which the action is going to be executed upon, for example Update Quantity. If it is clear that the action is going to be performed upon the active document the user is editing, then the noun can be omitted, for example Complete. 

##  Help

Context-sensitive help can be accessed by clicking the item Help in the top navigation. This opens a new tab. Administrators can edit the help texts by clicking the pen icon. Although it is possible to use various styles via The WYSIWYG edit tool, it is recommended to use the different styles sparingly.

##  Forms

Form fields visibility and order is first defined in the Application Dictionary. Via Form Personalization (Professional Subscription users only) the same can be done within the available set on user level. Field are an important part in the usability of a form. The following guidelines must be adhered:

  1. Labels: 
    * Capitalization rules for labels: Nouns are always capitalized, for example Purchase Order. Articles (the, a) should be avoided but when used they need to be in lowercase, for example Attach a File, unless they are at the beginning of the label, in which case they need to be capitalized. 
    * Abbreviations should be avoided but can be used for space reasons. Common abbreviations used in the English version are: 
      * No. for Number. For example in Document No. 
      * G/L for General Ledger. For example in G/L Category. 
  2. Field order. In service of speed and accuracy, required fields should be placed first. 
  3. Fields with default values that are not likely to be modified by the users should be placed together so they can be skipped easily by hitting the TAB key on the keyboard. This also reduces cognitive strain when the user scans the form. The ideal position is at the top of the form and combined with an first focus directly after the last field with default values. An alternative acceptable position is directly after the fields that are to be modified. The preference is for the first option as this increases the chance that the user scans and approves the default values. Note that the first focus can be set in Form Personalization. 
  4. Column span and row span. This is also defined in Form Personalization. By default a field spans one column and one row which can be changed to maximum four columns and nine rows (multi-line fields only). 
  5. New row. Fields can be place on a new row. This is typically done to draw attention to it or to visually disconnect it from its preceding field. It is recommended to use this effect with prudence as it will increase the form's total length hereby possibly forcing the user to scroll or enlarge the active view. 
  6. Sections. Fields can be grouped into sections and sections can be collapsed. This makes it easier to keep forms organized and not too crowded at first sight. Which fields go in what section is defined in Form Personalization. It is recommended to place required and frequently modified fields in the main area at the top of the form. Optional and less frequently modified fields can be placed in a section. 
  7. Status bar. This is the shaded row at the top of the form. Via Form Personalization users can define which fields will be displayed there. It is recommended to place fields of a generic nature here. Examples are Document Status, Total Amount, Currency. 

##  Messages

User Messages are displayed at the top of the view and their function is to inform or warn the user about an exception, error or other situation in the application that needs the user's attention. There are four different types of user messages.

**Error** : This type of message is used for exceptions and errors. A typical case is a process that was not executed successfully. The message need to be concise, friendly (i.e. the user is never to blame) and a suggestion on how to solve the problem should be given.

**Success** : This type of message is displayed after successful process execution. In general this type of message can be kept short (to avoid forcing the user to read too much without any reason) along the lines of " _Process ABC completed successfully_ ". In some cases it can be good to add a suggestion for a next step, for example: "...You can now proceed to...".

**Info** : This type of message is used to communicate interesting but not essential information.

**Warning** : This type of message is used to inform the user about a system status or event that might cause a problem.

**Tip** (not in use yet): Typically used to provide information that would help the user to be more successful, although task completion does not depend on it.

##  Tools

###  Integrated Tools

The available tools for creation and modification that are provided with Etendo are:

  * Application Dictionary 
  * Form Customization 
  * Saving Views 
  * Column Filters 

###  Wireframing Tool

In addition to these integrated tools, application developers are also recommended to make use of design tools before starting development.
Functional and interaction design is typically done using dedicated wireframe tools. Since most wireframe tools are geared towards web design, Etendo has produced a simple  web-based modeling tool. The community can freely use it to create Etendo modules and extensions.

It should be used as follows:

  1. First, make a copy in Google Docs so you can start editing and building your own wireframes. 
  2. Use the predefined templates and library components in the document to design your own windows and flows 
  3. When done, remove all slides that are not needed 
  4. Annotate the slides explaining behavior and business logic 
  5. Share the presentation with the stakeholders 

---

This work is a derivative of [User Interface Design Guidelines](http://wiki.Etendo.com/wiki/User_Interface_Design_Guidelines){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}. 