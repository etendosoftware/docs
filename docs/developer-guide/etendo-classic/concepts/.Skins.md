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

  

#  Skins

  

##  Contents

  * 1  Introduction 
  * 2  Navigation bar 
    * 2.1  Global 
      * 2.1.1  Closed dropdown button 
      * 2.1.2  Over button 
      * 2.1.3  Opened dropdown button 
    * 2.2  Create New 
    * 2.3  Quick Launch 
    * 2.4  Application Menu 
    * 2.5  Alerts 
    * 2.6  Help 
    * 2.7  User Profile 
    * 2.8  End Session 
  * 3  Parent/Top/Main tabs 
    * 3.1  Background 
    * 3.2  Tab button 
    * 3.3  Tab overflow buttons 
  * 4  Child tabs 
    * 4.1  Background 
    * 4.2  Tab button 
    * 4.3  Tab overflow buttons 
  * 5  Toolbar 
    * 5.1  Background 
    * 5.2  Icon button 
    * 5.3  Text button 
    * 5.4  Save view button 
  * 6  Status Bar 
  * 7  View 
  * 8  Grid 
    * 8.1  Filter row 
    * 8.2  Header 
    * 8.3  Cells 
    * 8.4  Grid view buttons 
    * 8.5  Link button (just the text is the link) 
    * 8.6  Link cell (the whole cell is the link) 
    * 8.7  Empty grid link text 
  * 9  Form 
    * 9.1  Common 
    * 9.2  Check box 
    * 9.3  Combo box 
    * 9.4  Selector 
    * 9.5  Date field 
    * 9.6  Spinner 
    * 9.7  Image field 
    * 9.8  Widget 
    * 9.9  Button 
    * 9.10  Link button 
    * 9.11  Notes 
    * 9.12  Sections 
    * 9.13  Form layout personalization window 
  * 10  Popup 
    * 10.1  Border 
    * 10.2  Header 
    * 10.3  Maximize button 
    * 10.4  Minimize button 
    * 10.5  Restore button 
    * 10.6  Close button 
  * 11  Dialog 
  * 12  Workspace 
    * 12.1  Left items 
    * 12.2  Widgets 
      * 12.2.1  Border 
      * 12.2.2  Edit button 
      * 12.2.3  Maximize button 
      * 12.2.4  Minimize button 
      * 12.2.5  Restore button 
      * 12.2.6  Close button 

  
---  
  
##  Introduction

This document describes different UI components and most significant
files/pieces of code that are needed to build/customize them.

In order to learn how to build a skin module, please go to  _How to create a
New Skin_

There is also a skin module available:  _Project_ \-  _Repositories_

##  Navigation bar

![](/assets/developer-guide/etendo-classic/concepts/Skins-0.png){: .legacy-image-style}

###  Global

Top margin:

  * org.openbravo.client.application/ob-application-styles.js -> OB.Styles.TopLayout.layoutTopMargin 

Bottom margin:

  * org.openbravo.client.application/ob-application-styles.js -> OB.Styles.TopLayout.layoutBottomMargin 

Left margin:

  * org.openbravo.client.application/ob-navigation-bar-styles.css -> .OBNavBarToolStrip -> margin-left 

Background color:

  * org.openbravo.client.application/ob-application-styles.css -> .OBTopLayout -> background-color 

####  Closed dropdown button

Background Color:

  * org.openbravo.client.application/ob-navigation-bar-styles.css -> .OBNavBarComponent -> background-color 
  * org.openbravo.client.application/ob-navigation-bar-styles.css -> .OBNavBarComponent -> border-top-color 

####  Over button

Background color:

  * org.openbravo.client.application/ob-navigation-bar-styles.css -> .OBNavBarComponent:hover -> background-color 

Border color:

  * org.openbravo.client.application/ob-navigation-bar-styles.css -> .OBNavBarComponent:hover -> border-top-color 
  * org.openbravo.client.application/ob-navigation-bar-styles.css -> .OBNavBarComponent:hover -> border-bottom-color 
  * org.openbravo.client.application/ob-navigation-bar-styles.css -> .OBNavBarComponent:hover -> border-left-color 

  * org.openbravo.client.application/ob-navigation-bar-styles.css -> .OBNavBarComponent:hover -> background-image 
  * org.openbravo.client.application/images/navbar/navbar-right-border.png 

####  Opened dropdown button

Background color:

  * org.openbravo.client.application/ob-navigation-bar-styles.css -> .OBNavBarComponentSelected -> background-color 
  * org.openbravo.client.application/ob-navigation-bar-styles.css -> .OBFlyoutLayout -> background-color 
  * org.openbravo.client.application/ob-navigation-bar-styles.css -> .OBNavBarComponentHideLine -> background-color 
  * org.openbravo.client.application/ob-navigation-bar-styles.css -> .OBNavBarComponentFormTabButtonTopSelected* -> border-bottom-color 
  * org.openbravo.client.application/ob-application-menu-styles.css -> .OBApplicationMenuTreeTable -> background-color 

Border color:

  * org.openbravo.client.application/ob-navigation-bar-styles.css -> .OBNavBarComponentSelected -> border-top-color 
  * org.openbravo.client.application/ob-navigation-bar-styles.css -> .OBNavBarComponentSelected -> border-left-color 

  * org.openbravo.client.application/ob-navigation-bar-styles.css -> .OBNavBarComponentSelected -> background-image 
  * org.openbravo.client.application/images/navbar/navbar-right-border.png 

  * org.openbravo.client.application/ob-navigation-bar-styles.css -> .OBFlyoutLayout -> border-color 
  * org.openbravo.client.application/ob-application-menu-styles.css -> .OBApplicationMenuTree -> border-color 

###  Create New

Icon:

  * org.openbravo.client.application/ob-navigation-bar-styles.js -> isc.OBQuickLaunch -> createNew_src 
  * org.openbravo.client.application/images/navbar/iconCreateNew.png 

Icon (RTL):

  * org.openbravo.client.application/ob-rtl-styles.js -> isc.OBQuickLaunch -> createNew_src 
  * org.openbravo.client.application/images/navbar/iconCreateNew-RTL.png 

Recent item icon: shared with "Application Menu: Content icons"

Recent item text:

  * org.openbravo.client.application/ob-navigation-bar-styles.css -> .OBQuickLaunchRecentLinkButton 

Label + Combo box: shared with "Form" one

###  Quick Launch

Icon:

  * org.openbravo.client.application/ob-navigation-bar-styles.js -> isc.OBQuickLaunch -> quickLaunch_src 
  * org.openbravo.client.application/images/navbar/iconQuickLaunch.png 

Icon (RTL):

  * org.openbravo.client.application/ob-rtl-styles.js -> isc.OBQuickLaunch -> quickLaunch_src 
  * org.openbravo.client.application/images/navbar/iconQuickLaunch-RTL.png 

Recent item icon: shared with "Application Menu: Content icons"

Recent item text:

  * org.openbravo.client.application/ob-navigation-bar-styles.css -> .OBQuickLaunchRecentLinkButton* 

Label + Combo box: shared with "Form" one

###  Application Menu

Icon:

  * org.openbravo.client.application/ob-application-menu-styles.js -> isc.OBApplicationMenuButton -> icon -> src 
  * org.openbravo.client.application/images/navbar/iconOpenDropDown.png 

Content icons:

  * org.openbravo.client.application/ob-application-menu-styles.js -> OB.Styles.OBApplicationMenu.folderOpened 
  * org.openbravo.client.application/images/application-menu/iconFolderOpened.png 
  * org.openbravo.client.application/ob-application-menu-styles.js -> OB.Styles.OBApplicationMenu.folderClosed 
  * org.openbravo.client.application/images/application-menu/iconFolderClosed.png 
  * org.openbravo.client.application/ob-application-menu-styles.js -> OB.Styles.OBApplicationMenu.window 
  * org.openbravo.client.application/images/application-menu/iconWindow.png 
  * org.openbravo.client.application/ob-application-menu-styles.js -> OB.Styles.OBApplicationMenu.process 
  * org.openbravo.client.application/images/application-menu/iconProcess.png 
  * org.openbravo.client.application/ob-application-menu-styles.js -> OB.Styles.OBApplicationMenu.processManual 
  * org.openbravo.client.application/images/application-menu/iconProcess.png 
  * org.openbravo.client.application/ob-application-menu-styles.js -> OB.Styles.OBApplicationMenu.report 
  * org.openbravo.client.application/images/application-menu/iconReport.png 
  * org.openbravo.client.application/ob-application-menu-styles.js -> OB.Styles.OBApplicationMenu.task 
  * org.openbravo.client.application/images/application-menu/iconTask.png 
  * org.openbravo.client.application/ob-application-menu-styles.js -> OB.Styles.OBApplicationMenu.form 
  * org.openbravo.client.application/images/application-menu/iconForm.png 
  * org.openbravo.client.application/ob-application-menu-styles.js -> OB.Styles.OBApplicationMenu.externalLink 
  * org.openbravo.client.application/images/application-menu/iconExternalLink.png 
  * org.openbravo.client.application/ob-application-menu-styles.js -> OB.Styles.OBApplicationMenu.view 
  * org.openbravo.client.application/images/application-menu/iconForm.png 
  * org.openbravo.client.application/ob-application-menu-styles.js -> OB.Styles.OBApplicationMenu.document 
  * org.openbravo.client.application/images/application-menu/iconDocument.png 

Content border color:

  * org.openbravo.client.application/ob-application-menu-styles.css -> OBApplicationMenuTree -> border-color 

Icon-Text separator color:

  * org.openbravo.client.application/ob-application-menu-styles.css -> OBApplicationMenuTreeItemCellIconFieldDisabled -> background-image 
  * org.openbravo.client.application/images/application-menu/menuSeparator.png 

  * org.openbravo.client.application/ob-application-menu-styles.css -> OBApplicationMenuTreeItemCellIcon -> border-right-color 
  * org.openbravo.client.application/ob-application-menu-styles.css -> OBApplicationMenuTreeItemCellIconField -> border-right-color 
  * org.openbravo.client.application/ob-application-menu-styles.css -> OBApplicationMenuTreeItemCellIconFieldSelected -> border-right-color 
  * org.openbravo.client.application/ob-application-menu-styles.css -> OBApplicationMenuTreeItemCellIconFieldOver -> border-right-color 
  * org.openbravo.client.application/ob-application-menu-styles.css -> OBApplicationMenuTreeItemCellIconFieldSelectedOver -> border-right-color 
  * org.openbravo.client.application/ob-application-menu-styles.css -> OBApplicationMenuTreeItemCellIconFieldDisabled -> border-right-color 

Icon-Text separator color (RTL):

  * org.openbravo.client.application/ob-rtl-styles.css -> OBApplicationMenuTreeItemCellIconFieldDisabled -> background-image 
  * org.openbravo.client.application/images/application-menu/menuSeparator-RTL.png 

Icon over background color:

  * org.openbravo.client.application/ob-application-menu-styles.css -> OBApplicationMenuTreeItemCellIconFieldOver -> background-color 
  * org.openbravo.client.application/ob-application-menu-styles.css -> OBApplicationMenuTreeItemCellIconFieldSelectedOver -> background-color 
  * org.openbravo.client.application/ob-application-menu-styles.css -> OBApplicationMenuTreeItemCellIconFieldSubmenuFieldOver -> background-color 
  * org.openbravo.client.application/ob-application-menu-styles.css -> OBApplicationMenuTreeItemCellIconFieldSubmenuFieldSelectedOver -> background-color 
  * org.openbravo.client.application/ob-application-menu-styles.css -> OBApplicationMenuTreeItemCellIconFieldKeysFieldOver -> background-color 
  * org.openbravo.client.application/ob-application-menu-styles.css -> OBApplicationMenuTreeItemCellIconFieldKeysFieldSelectedOver -> background-color 
  * org.openbravo.client.application/ob-application-menu-styles.css -> OBApplicationMenuTreeItemCellIconFieldTitleFieldOver -> background-color 
  * org.openbravo.client.application/ob-application-menu-styles.css -> OBApplicationMenuTreeItemCellIconFieldTitleFieldSelectedOver -> background-color 

Text over background color:

  * org.openbravo.client.application/ob-application-menu-styles.css -> OBApplicationMenuTreeItemCellOver -> background-color 
  * org.openbravo.client.application/ob-application-menu-styles.css -> OBApplicationMenuTreeItemCellSelectedOver -> background-color 
  * org.openbravo.client.application/ob-application-menu-styles.css -> OBApplicationMenuTreeItemCellSubmenuFieldOver -> background-color 
  * org.openbravo.client.application/ob-application-menu-styles.css -> OBApplicationMenuTreeItemCellSubmenuFieldSelectedOver -> background-color 
  * org.openbravo.client.application/ob-application-menu-styles.css -> OBApplicationMenuTreeItemCellKeysFieldOver -> background-color 
  * org.openbravo.client.application/ob-application-menu-styles.css -> OBApplicationMenuTreeItemCellKeysFieldSelectedOver -> background-color 
  * org.openbravo.client.application/ob-application-menu-styles.css -> OBApplicationMenuTreeItemCellTitleFieldOver -> background-color 
  * org.openbravo.client.application/ob-application-menu-styles.css -> OBApplicationMenuTreeItemCellTitleFieldSelectedOver -> background-color 

Text over font color:

  * org.openbravo.client.application/ob-application-menu-styles.css -> OBApplicationMenuTreeItemCellOver -> color 
  * org.openbravo.client.application/ob-application-menu-styles.css -> OBApplicationMenuTreeItemCellSelectedOver -> color 
  * org.openbravo.client.application/ob-application-menu-styles.css -> OBApplicationMenuTreeItemCellSubmenuFieldOver -> color 
  * org.openbravo.client.application/ob-application-menu-styles.css -> OBApplicationMenuTreeItemCellSubmenuFieldSelectedOver -> color 
  * org.openbravo.client.application/ob-application-menu-styles.css -> OBApplicationMenuTreeItemCellKeysFieldOver -> color 
  * org.openbravo.client.application/ob-application-menu-styles.css -> OBApplicationMenuTreeItemCellKeysFieldSelectedOver -> color 
  * org.openbravo.client.application/ob-application-menu-styles.css -> OBApplicationMenuTreeItemCellTitleFieldOver -> color 
  * org.openbravo.client.application/ob-application-menu-styles.css -> OBApplicationMenuTreeItemCellTitleFieldSelectedOver -> color 

###  Alerts

Icon:

  * org.openbravo.client.application/ob-navigation-bar-styles.js -> isc.OBAlertIcon -> alertIcon -> src 
  * org.openbravo.client.application/images/navbar/iconAlert.png 

###  Help

Icon:

  * org.openbravo.client.application/ob-navigation-bar-styles.js -> isc.OBHelpAbout -> icon -> src 
  * org.openbravo.client.application/images/navbar/iconOpenDropDown.png 

Item text:

  * org.openbravo.client.application/ob-navigation-bar-styles.css -> .OBHelpAboutLinkButton* 

###  User Profile

Icon:

  * org.openbravo.client.application/ob-navigation-bar-styles.js -> isc.OBUserProfile -> icon -> src 
  * org.openbravo.client.application/images/navbar/iconOpenDropDown.png 

Form components: shared with "Form" ones

Sub-section border color:

  * org.openbravo.client.application/ob-navigation-bar-styles.css -> .OBNavBarComponentFormTabSetContainer -> border-top-color 
  * org.openbravo.client.application/ob-navigation-bar-styles.css -> .OBNavBarComponentFormTabButtonTopSelected* -> border-top-color 
  * org.openbravo.client.application/ob-navigation-bar-styles.css -> .OBNavBarComponentFormTabButtonTopSelected* -> border-right-color 
  * org.openbravo.client.application/ob-navigation-bar-styles.css -> .OBNavBarComponentFormTabButtonTopSelected* -> border-left-color 

###  End Session

Icon:

  * org.openbravo.client.application/ob-navigation-bar-styles.js -> isc.OBLogout -> src 
  * org.openbravo.client.application/images/navbar/iconClose.png 

Icon (RTL):

  * org.openbravo.client.application/ob-rtl-styles.js -> isc.OBLogout -> src 
  * org.openbravo.client.application/images/navbar/iconClose-RTL.png 

##  Parent/Top/Main tabs

![](/assets/developer-guide/etendo-classic/concepts/Skins-1.png){: .legacy-image-style}

###  Background

Background color:

  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarMain -> background-color 

Background image:

  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarMain -> background-image 

Bottom border:

  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabSetMainContainer -> border-top-color 

###  Tab button

Selected active:

  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonMainTopSelected -> background-image 
  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonMainTopSelectedFocused -> background-image 
  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonMainTopSelectedFocusedOver -> background-image 
  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonMainTopSelectedFocusedDown -> background-image 
  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonMainTopSelectedDown -> background-image 
  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonMainTopSelectedDisabled -> background-image 
  * org.openbravo.client.application/images/tab/tabBarButtonMain_Selected.png 

Selected active over:

  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonMainTopSelectedOver -> background-image 
  * org.openbravo.client.application/images/tab/tabBarButtonMain_Selected_Over.png 

Selected inactive:

  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonMainTopSelectedInactive -> background-image 
  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonMainTopSelectedFocusedInactive -> background-image 
  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonMainTopSelectedFocusedOverInactive -> background-image 
  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonMainTopSelectedFocusedDownInactive -> background-image 
  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonMainTopSelectedDownInactive -> background-image 
  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonMainTopSelectedDisabledInactive -> background-image 
  * org.openbravo.client.application/images/tab/tabBarButtonMain_Selected_Inactive.png 

Selected inactive over:

  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonMainTopSelectedOverInactive -> background-image 
  * org.openbravo.client.application/images/tab/tabBarButtonMain_Selected_Inactive_Over.png 

Unselected:

  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonMainTop -> background-image 
  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonMainTopDown -> background-image 
  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonMainTopDisabled -> background-image 
  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonMainTopInactive -> background-image 
  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonMainTopDownInactive -> background-image 
  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonMainTopDisabledInactive -> background-image 
  * org.openbravo.client.application/images/tab/tabBarButtonMain_Unselected.png 

Unselected over:

  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonMainTopOver -> background-image 
  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonMainTopOverInactive -> background-image 
  * org.openbravo.client.application/images/tab/tabBarButtonMain_Unselected_Over.png 

###  Tab overflow buttons

Move left/right buttons:

  * org.openbravo.client.application/ob-tab-styles.js -> isc.OBTabSetMain -> scrollerSrc 
  * org.openbravo.client.application/images/tab/tabBarButtonMain_OverflowIcon.png 

Pick list button:

  * org.openbravo.client.application/ob-tab-styles.js -> isc.OBTabSetMain -> pickerButtonSrc 
  * org.openbravo.client.application/images/tab/tabBarButtonMain_OverflowIconPicker.png 

##  Child tabs

###  Background

Background color:

  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarChild -> background-color 

Background image:

  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarChild -> background-image 

Bottom border:

  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabSetChildContainer -> border-top-color 

###  Tab button

Selected active:

  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonChildTopSelected -> background-image 
  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonChildTopSelectedFocused -> background-image 
  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonChildTopSelectedFocusedOver -> background-image 
  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonChildTopSelectedFocusedDown -> background-image 
  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonChildTopSelectedDown -> background-image 
  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonChildTopSelectedDisabled -> background-image 
  * org.openbravo.client.application/images/tab/tabBarButtonChild_Selected.png 

Selected active over:

  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonChildTopSelectedOver -> background-image 
  * org.openbravo.client.application/images/tab/tabBarButtonChild_Selected_Over.png 

Selected inactive:

  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonChildTopSelectedInactive -> background-image 
  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonChildTopSelectedFocusedInactive -> background-image 
  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonChildTopSelectedFocusedOverInactive -> background-image 
  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonChildTopSelectedFocusedDownInactive -> background-image 
  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonChildTopSelectedDownInactive -> background-image 
  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonChildTopSelectedDisabledInactive -> background-image 
  * org.openbravo.client.application/images/tab/tabBarButtonChild_Selected_Inactive.png 

Selected inactive over:

  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonChildTopSelectedOverInactive -> background-image 
  * org.openbravo.client.application/images/tab/tabBarButtonChild_Selected_Inactive_Over.png 

Unselected:

  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonChildTop -> background-image 
  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonChildTopDown -> background-image 
  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonChildTopDisabled -> background-image 
  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonChildTopInactive -> background-image 
  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonChildTopDownInactive -> background-image 
  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonChildTopDisabledInactive -> background-image 
  * org.openbravo.client.application/images/tab/tabBarButtonChild_Unselected.png 

Unselected over:

  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonChildTopOver -> background-image 
  * org.openbravo.client.application/ob-tab-styles.css -> .OBTabBarButtonChildTopOverInactive -> background-image 
  * org.openbravo.client.application/images/tab/tabBarButtonChild_Unselected_Over.png 

###  Tab overflow buttons

Move left/right:

  * org.openbravo.client.application/ob-tab-styles.js -> isc.OBTabSetChild -> scrollerSrc 
  * org.openbravo.client.application/images/tab/tabBarButtonChild_OverflowIcon.png 

Pick list:

  * org.openbravo.client.application/ob-tab-styles.js -> isc.OBTabSetChild -> pickerButtonSrc 
  * org.openbravo.client.application/images/tab/tabBarButtonChild_OverflowIconPicker.png 

##  Toolbar

![](/assets/developer-guide/etendo-classic/concepts/Skins-2.png){: .legacy-image-style}

###  Background

Background:

  * org.openbravo.client.application/ob-toolbar-styles.js -> .OBToolbar -> background 
  * org.openbravo.client.application/images/toolbar/toolbar-bg.png 

###  Icon button

Border:

  * org.openbravo.client.application/ob-toolbar-styles.css -> .OBToolbarIconButton* -> border-color 

Icon:

  * org.openbravo.client.application/ob-toolbar-styles.css -> OBToolbarIconButton_icon* -> background-image 
  * org.openbravo.client.application/images/toolbar/iconButton-*.png 

###  Text button

Background:

  * org.openbravo.client.application/ob-toolbar-styles.css -> .OBToolbarTextButton* -> background-image 
  * org.openbravo.client.application/images/toolbar/textButton-bg-*.png 

Border:

  * org.openbravo.client.application/ob-toolbar-styles.css -> .OBToolbarTextButton* -> border-color 

###  Save view button

![](/assets/developer-guide/etendo-classic/concepts/Skins-3.png){: .legacy-image-style}

Background:

  * org.openbravo.client.application/ob-personalization-styles.css -> .OBPersonalizationPullDownMenu -> background-color 

Cell state background:

  * org.openbravo.client.application/ob-personalization-styles.css -> .OBPersonalizationPullDownMenuCellDark* -> background-color 

Border:

  * org.openbravo.client.application/ob-personalization-styles.css -> .OBPersonalizationPullDownMenu -> border-color 

Internal separator color:

  * org.openbravo.client.application/ob-personalization-styles.css -> .OBPersonalizationPullDownMenuCellIcon* -> border-color 
  * org.openbravo.client.application/ob-personalization-styles.css -> .OBPersonalizationPullDownMenuCellSeparator* -> border-color 

##  Status Bar

![](/assets/developer-guide/etendo-classic/concepts/Skins-4.png){: .legacy-image-style}

Background:

  * org.openbravo.client.application/ob-statusbar-styles.css -> .OBStatusBar -> background-image 

Icons:

  * org.openbravo.client.application/ob-statusbar-styles.js -> isc.OBStatusBar -> savedIconDefaults -> src 
  * org.openbravo.client.application/images/statusbar/ico-saved.png 

  * org.openbravo.client.application/ob-statusbar-styles.js -> isc.OBStatusBar -> newIconDefaults -> src 
  * org.openbravo.client.application/images/statusbar/ico-new.png 

  * org.openbravo.client.application/ob-statusbar-styles.js -> isc.OBStatusBar -> editIconDefaults -> src 
  * org.openbravo.client.application/images/statusbar/ico-edit.png 

Buttons:

  * org.openbravo.client.application/ob-statusbar-styles.js -> isc.OBStatusBarIconButton -> genericIconSrc 
  * org.openbravo.client.application/images/statusbar/iconButton.png 

Link icon:

  * org.openbravo.client.application/ob-statusbar-styles.js -> isc.OBStatusBar -> titleLinkImageSrc 

Link color:

  * org.openbravo.client.application/ob-statusbar-styles.css -> .OBStatusBarTextLink_Title* -> color 

##  View

Active view left bar background color:

  * org.openbravo.client.application/ob-application-styles.css -> .OBViewActive -> background-color 

Inactive view left bar background color:

  * org.openbravo.client.application/ob-application-styles.css -> .OBViewInActive -> background-color 

##  Grid

![](/assets/developer-guide/etendo-classic/concepts/Skins-5.png){: .legacy-image-style}

###  Filter row

Background color:

  * org.openbravo.client.application/ob-grid-styles.css -> .OBGridFilterCell -> background-color 

Funnel button background color:

  * org.openbravo.client.application/ob-grid-styles.css -> .OBGridFilterFunnelBackground -> background-color 

  * org.openbravo.client.application/ob-grid-styles.css -> .OBGridFilterFunnelIconDown -> background-color 
  * org.openbravo.client.application/ob-grid-styles.css -> .OBGridFilterFunnelIconSelected -> background-color 
  * org.openbravo.client.application/ob-grid-styles.css -> .OBGridFilterFunnelIconFocused -> background-color 
  * org.openbravo.client.application/ob-grid-styles.css -> .OBGridFilterFunnelIcon -> background-color 

Border color:

  * org.openbravo.client.application/ob-grid-styles.css -> .OBGridFilterCell -> border-left-color 
  * org.openbravo.client.application/ob-grid-styles.css -> .OBGridFilterBase -> border-top-color 

###  Header

Button:

  * org.openbravo.client.application/ob-grid-styles.js -> isc.OBGrid -> sorterDefaults -> src 
  * org.openbravo.client.application/images/grid/gridHeader_bg.png 

  * org.openbravo.client.application/ob-grid-styles.js -> isc.OBGrid -> headerButtonDefaults -> src 
  * org.openbravo.client.application/images/grid/gridHeader_bg.png 

  * org.openbravo.client.application/ob-grid-styles.css -> .OBGridHeaderCell -> background-color 

Menu button:

  * org.openbravo.client.application/ob-grid-styles.js -> isc.OBGrid -> headerMenuButtonSrc 
  * org.openbravo.client.application/images/grid/gridHeaderMenuButton.png 

###  Cells

Border color:

  * org.openbravo.client.application/ob-grid-styles.css -> .OBGridCell* -> border-right-color 
  * org.openbravo.client.application/ob-grid-styles.css -> .OBGridCell* -> border-bottom-color 

Odd cell background color:

  * org.openbravo.client.application/ob-grid-styles.css -> .OBGridCell -> background-color 

Even cell background color:

  * org.openbravo.client.application/ob-grid-styles.css -> .OBGridCellDark -> background-color 
  * org.openbravo.client.application/ob-grid-styles.css -> .OBGridCellEditDark -> background-color 

Over cell background color:

  * org.openbravo.client.application/ob-grid-styles.css -> .OBGridCellOver -> background-color 
  * org.openbravo.client.application/ob-grid-styles.css -> .OBGridCellOverDark -> background-color 
  * org.openbravo.client.application/ob-grid-styles.css -> .OBGridCellEditOver -> background-color 
  * org.openbravo.client.application/ob-grid-styles.css -> .OBGridCellEditOverDark -> background-color 

Selected cell background color:

  * org.openbravo.client.application/ob-grid-styles.css -> .OBGridCell*Selected* -> background-color 
  * org.openbravo.client.application/ob-grid-styles.css -> .OBGridFilterStaticTextLink:hover -> background-color 
  * org.openbravo.client.application/ob-grid-styles.css -> .OBGridFilterStaticTextLink:active -> background-color 

###  Grid view buttons

Icons:

  * org.openbravo.client.application/ob-grid-styles.js -> isc.OBGridToolStripIcon -> genericIconSrc 
  * org.openbravo.client.application/images/grid/gridButton-edit*.png 
  * org.openbravo.client.application/images/grid/gridButton-cancel*.png 
  * org.openbravo.client.application/images/grid/gridButton-form*.png 
  * org.openbravo.client.application/images/grid/gridButton-save*.png 

Button separator:

  * org.openbravo.client.application/ob-grid-styles.js -> isc.OBGridToolStripSeparator -> src 
  * org.openbravo.client.application/images/grid/gridButton-separator.png 

###  Link button (just the text is the link)

Color:

  * org.openbravo.client.application/ob-grid-styles.css -> .OBGridLinkButton* -> color 

###  Link cell (the whole cell is the link)

Color:

  * org.openbravo.client.application/ob-grid-styles.css -> .OBGridLinkCell* -> color 

Border color:

  * org.openbravo.client.application/ob-grid-styles.css -> .OBGridLinkCell* -> border-right-color 
  * org.openbravo.client.application/ob-grid-styles.css -> .OBGridLinkCell* -> border-bottom-color 

###  Empty grid link text

Color:

  * org.openbravo.client.application/ob-grid-styles.css -> .OBGridNotificationTextLink* -> color 

##  Form

![](/assets/developer-guide/etendo-classic/concepts/Skins-6.png){: .legacy-image-style}

###  Common

Form background color:

  * org.openbravo.client.application/ob-form-styles.css -> .OBFormContainerLayout -> background-color 

Label color:

  * org.openbravo.client.application/ob-form-styles.css -> .OBFormFieldLabel* -> color 

Label link color:

  * org.openbravo.client.application/ob-form-styles.css -> .OBFormFieldLinkButton -> color 

Label link hover color:

  * org.openbravo.client.application/ob-form-styles.css -> .OBFormFieldLinkButton:hover -> color 

Label link icon:

  * org.openbravo.client.application/ob-form-styles.js -> isc.OBFKItem -> newTabIconSrc 
  * org.openbravo.client.application/ob-form-styles.js -> OB.Styles.OBFormField.DefaultSearch.newTabIconSrc 
  * org.openbravo.userinterface.selector/ob-selector-item-styles.js -> isc.OBSelectorItem -> newTabIconSrc 
  * org.openbravo.userinterface.selector/ob-selector-item-styles.js -> isc.OBSelectorLinkItem -> newTabIconSrc 
  * org.openbravo.client.application/images/form/ico-to-new-tab.png 

Clear icon:

  * org.openbravo.client.application/ob-form-styles.js -> OB.Styles.OBFormField.DefaultSearch.clearIcon.src 
  * org.openbravo.client.application/ob-selector-item-styles.js -> isc.OBSelectorLinkItem -> clearIcon-> src 

Field border color:

  * org.openbravo.client.application/ob-form-styles.css -> .OBFormFieldInput* -> border-color 
  * org.openbravo.client.application/ob-form-styles.css -> .OBFormFieldSelectInput* -> border-color 
  * org.openbravo.client.application/ob-form-styles.css -> .OBFormFieldDateInput* -> border-color 
  * org.openbravo.client.application/ob-form-styles.css -> .OBFormFieldNumberInput* -> border-color 
  * org.openbravo.client.application/ob-form-styles.css -> .OBFormFieldImageInput* -> border-color 

Field background color:

  * org.openbravo.client.application/ob-form-styles.css -> .OBFormFieldInput* -> background-color 
  * org.openbravo.client.application/ob-form-styles.css -> .OBFormFieldSelectInput* -> background-color 
  * org.openbravo.client.application/ob-form-styles.css -> .OBFormFieldDateInput* -> background-color 
  * org.openbravo.client.application/ob-form-styles.css -> .OBFormFieldNumberInput* -> background-color 
  * org.openbravo.client.application/ob-form-styles.css -> .OBFormFieldImageInput* -> background-color 

###  Check box

Icon:

  * org.openbravo.client.application/ob-form-styles.js -> OB.Styles.OBFormField.DefaultCheckbox.checkedImage 
  * org.openbravo.client.application/images/form/checked.png 

  * org.openbravo.client.application/ob-form-styles.js -> OB.Styles.OBFormField.DefaultCheckbox.uncheckedImage 
  * org.openbravo.client.application/images/form/unchecked.png 

###  Combo box

Picker icon:

  * org.openbravo.client.application/ob-form-styles.js -> OB.Styles.OBFormField.DefaultComboBox.pickerIconSrc 
  * org.openbravo.client.application/ob-form-styles.js -> isc.RelativeDateItem -> valueFieldDefaults -> pickerIconSrc 
  * org.openbravo.client.application/images/form/comboBoxPicker.png 

Pick list background color:

  * org.openbravo.client.application/ob-form-styles.css -> .OBFormFieldPickListCell -> background-color 
  * org.openbravo.client.application/ob-form-styles.css -> .OBFormFieldPickListCellFocused -> background-color 
  * org.openbravo.client.application/ob-form-styles.css -> .OBFormFieldPickListCellDark -> background-color 

Pick list selected background color:

  * org.openbravo.client.application/ob-form-styles.css -> .OBFormFieldPickListCellSelected -> background-color 
  * org.openbravo.client.application/ob-form-styles.css -> .OBFormFieldPickListCellSelectedFocused -> background-color 
  * org.openbravo.client.application/ob-form-styles.css -> .OBFormFieldPickListCellSelectedDark -> background-color 

###  Selector

Search icon:

  * org.openbravo.userinterface.selector/ob-selector-item-styles.js -> isc.OBSelectorItem -> popupIconSrc 
  * org.openbravo.userinterface.selector/ob-selector-item-styles.js -> isc.OBSelectorLinkItem -> pickerIconSrc 
  * org.openbravo.client.application/ob-form-styles.css -> OB.Styles.OBFormField.DefaultSearch.pickerIconSrc 
  * org.openbravo.client.application/images/form/search_picker.png 

Pick list background color: shared with "Form: Combo box"

###  Date field

Icon:

  * org.openbravo.client.application/ob-form-styles.js -> OB.Styles.OBFormField.DefaultDateInput.pickerIconSrc 
  * org.openbravo.client.application/ob-form-styles.js -> isc.OBMiniDateRangeItem -> pickerIconDefaults -> src 
  * org.openbravo.client.application/ob-form-styles.js -> isc.RelativeDateItem -> valueFieldDefaults -> calendarIconSrc 
  * org.openbravo.client.application/images/form/date_control.png 

Calendar border:

  * org.openbravo.client.application/ob-form-styles.js -> isc.OBDateRangeDialog -> edgeImage 

Calendar buttons:

  * org.openbravo.client.application/ob-form-styles.css -> .OBDateChooserBottomButton 
  * org.openbravo.client.application/ob-form-styles.css -> .OBDateChooserBottomButtonSelected 
  * org.openbravo.client.application/images/form/dateChooser-bg-button.png 

Calendar buttons hover:

  * org.openbravo.client.application/ob-form-styles.css -> .OBDateChooserBottomButtonOver 
  * org.openbravo.client.application/ob-form-styles.css -> .OBDateChooserBottomButtonSelectedOver 
  * org.openbravo.client.application/images/form/dateChooser-bg-button_Over.png 

Calendar buttons pressed:

  * org.openbravo.client.application/ob-form-styles.css -> .OBDateChooserBottomButtonDown 
  * org.openbravo.client.application/ob-form-styles.css -> .OBDateChooserBottomButtonSelectedDown 
  * org.openbravo.client.application/images/form/dateChooser-bg-button_Down.png 

Calendar days:

  * org.openbravo.client.application/ob-form-styles.css -> .OBDateChooserWeekday* 
  * org.openbravo.client.application/ob-form-styles.css -> .OBDateChooserWeekend* 

###  Spinner

Increase icon:

  * org.openbravo.client.application/ob-form-styles.js -> isc.OBSpinnerItem.INCREASE_ICON -> src 
  * org.openbravo.client.application/images/form/spinnerControlIncrease.png 

Decrease icon:

  * org.openbravo.client.application/ob-form-styles.js -> isc.OBSpinnerItem.DECREASE_ICON -> src 
  * org.openbravo.client.application/images/form/spinnerControlDecrease.png 

###  Image field

Upload icon:

  * org.openbravo.client.application/ob-form-styles.js -> isc.OBImageItemButton -> uploadIconSrc 
  * org.openbravo.client.application/images/form/upload_icon.png 

Erase icon:

  * org.openbravo.client.application/ob-form-styles.js -> isc.OBImageItemButton -> eraseIconSrc 
  * org.openbravo.client.application/images/form/erase_icon.png 

Not Available Image image:

  * org.openbravo.client.application/ob-form-styles.js -> isc.OBImageCanvas-> imageNotAvailableSrc 
  * org.openbravo.client.application/images/form/imageNotAvailable.png 

###  Widget

Border color:

  * org.openbravo.client.myob/ob-widget-styles.js -> isc.OBWidgetInFormItem -> edgeImage 
  * org.openbravo.client.myob/images/form/border.png 

###  Button

Background:

  * org.openbravo.client.application/ob-form-styles.css -> .OBFormButton* -> background-image 
  * org.openbravo.client.application/images/form/textButton-bg-*.png 

Border:

  * org.openbravo.client.application/ob-form-styles.css -> .OBFormButton* -> border-color 

###  Link button

Normal color:

  * org.openbravo.client.application/ob-form-styles.css -> .OBLinkButtonItem -> color 
  * org.openbravo.client.application/ob-form-styles.css -> .OBLinkButtonItemOver -> color 
  * org.openbravo.client.application/ob-form-styles.css -> .OBLinkButtonItem:hover -> color 

Hover color:

  * org.openbravo.client.application/ob-form-styles.css -> .OBLinkButtonItemDown -> color 
  * org.openbravo.client.application/ob-form-styles.css -> .OBLinkButtonItem:active -> color 

Pressed color:

  * org.openbravo.client.application/ob-form-styles.css -> .OBLinkButtonItemFocused -> color 
  * org.openbravo.client.application/ob-form-styles.css -> .OBLinkButtonItemFocusedOver -> color 
  * org.openbravo.client.application/ob-form-styles.css -> .OBLinkButtonItemFocusedDown -> color 
  * org.openbravo.client.application/ob-form-styles.css -> .OBLinkButtonItem:focus -> color 

###  Notes

Other user note background color:

  * org.openbravo.client.application/ob-form-styles.css -> .OBNoteListGridOtherUserNoteCell -> background-color 
  * org.openbravo.client.application/ob-form-styles.css -> .OBNoteListGridOtherUserNoteCellOver -> background-color 

Delete note text color:

  * org.openbravo.client.application/ob-form-styles.css -> .OBNoteListGridDelete -> color 

###  Sections

Sections title underline color:

  * org.openbravo.client.application/ob-form-styles.js -> isc.OBSectionItemButton -> backgroundDefaults -> src 

Sections title underline color (RTL):

  * org.openbravo.client.application/ob-rtl-styles.js -> isc.OBSectionItemButton -> backgroundDefaults -> src 

Sections icon:

  * org.openbravo.client.application/ob-form-styles.js -> isc.OBSectionItemButton -> backgroundDefaults -> icon 

###  Form layout personalization window

Border color:

  * org.openbravo.client.application/ob-personalization-styles.css -> .OBFormPersonalizerPreviewPanel -> border-color 

Content icons:

  * org.openbravo.client.application/ob-personalization-styles.js -> OB.Styles.Personalization.Icons.fieldGroup 
  * org.openbravo.client.application/images/personalization/iconFolder.png 
  * org.openbravo.client.application/images/personalization/iconFolder_closed.png (not declared in the .js but needed) 
  * org.openbravo.client.application/images/personalization/iconFolder_open.png (not declared in the .js but needed) 
  * org.openbravo.client.application/ob-personalization-styles.js -> OB.Styles.Personalization.Icons.field 
  * org.openbravo.client.application/images/personalization/item.png 
  * org.openbravo.client.application/ob-personalization-styles.js -> OB.Styles.Personalization.Icons.fieldDisplayLogic 
  * org.openbravo.client.application/images/personalization/itemDisplayLogic.png 
  * org.openbravo.client.application/ob-personalization-styles.js -> OB.Styles.Personalization.Icons.fieldDisplayLogicHidden 
  * org.openbravo.client.application/images/personalization/itemDisplayLogicHidden.png 
  * org.openbravo.client.application/ob-personalization-styles.js -> OB.Styles.Personalization.Icons.fieldHidden 
  * org.openbravo.client.application/images/personalization/itemHidden.png 
  * org.openbravo.client.application/ob-personalization-styles.js -> OB.Styles.Personalization.Icons.fieldRequired 
  * org.openbravo.client.application/images/personalization/itemRequired.png 
  * org.openbravo.client.application/ob-personalization-styles.js -> OB.Styles.Personalization.Icons.fieldRequiredDisplayLogic 
  * org.openbravo.client.application/images/personalization/itemRequiredDisplayLogic.png 
  * org.openbravo.client.application/ob-personalization-styles.js -> OB.Styles.Personalization.Icons.fieldRequiredDisplayLogicHidden 
  * org.openbravo.client.application/images/personalization/itemRequiredDisplayLogicHidden.png 
  * org.openbravo.client.application/ob-personalization-styles.js -> OB.Styles.Personalization.Icons.fieldRequiredHidden 
  * org.openbravo.client.application/images/personalization/itemRequiredHidden.png 

Content icons (RTL):

  * org.openbravo.client.application/ob-rtl-styles.js -> OB.Styles.Personalization.Icons.fieldGroup 
  * org.openbravo.client.application/images/personalization/iconFolder-RTL.png 
  * org.openbravo.client.application/images/personalization/iconFolder-RTL_closed.png (not declared in the .js but needed) 
  * org.openbravo.client.application/images/personalization/iconFolder-RTL_open.png (not declared in the .js but needed) 

Selected tree element background color:

  * org.openbravo.client.application/ob-personalization-styles.css -> .OBPersonalizationTreeGridCellSelected -> background-color 
  * org.openbravo.client.application/ob-personalization-styles.css -> .OBPersonalizationTreeGridCellSelectedOver -> background-color 
  * org.openbravo.client.application/ob-personalization-styles.css -> .OBPersonalizationTreeGridCellSelectedHiddenOver -> background-color 

##  Popup

![](/assets/developer-guide/etendo-classic/concepts/Skins-7.png){: .legacy-image-style}

###  Border

Color:

  * org.openbravo.client.application/ob-popup-styles.js -> isc.OBPopup -> edgeImage 
  * org.openbravo.client.application/images/popup/border.png 
  * org.openbravo.client.application/ob-popup-styles.js -> isc.Dialog -> edgeImage 
  * org.openbravo.client.application/images/popup/border.png 

###  Header

Background:

  * org.openbravo.client.application/ob-popup-styles.css -> .OBPopupHeaderText -> background 

###  Maximize button

Icon:

  * org.openbravo.client.application/ob-popup-styles.js -> isc.OBPopup -> maximizeButtonDefaults -> src 
  * org.openbravo.client.application/images/popup/maximize.png 
  * org.openbravo.client.application/ob-dialog-styles.js -> isc.Dialog -> maximizeButtonDefaults -> src 
  * org.openbravo.client.application/images/popup/maximize.png 

Border color:

  * org.openbravo.client.application/ob-popup-styles.css -> .OBPopupIconMaximize* -> border-color 

###  Minimize button

Icon:

  * org.openbravo.client.application/ob-popup-styles.js -> isc.OBPopup -> minimizeButtonDefaults -> src 
  * org.openbravo.client.application/images/popup/minimize.png 
  * org.openbravo.client.application/ob-dialog-styles.js -> isc.Dialog -> minimizeButtonDefaults -> src 
  * org.openbravo.client.application/images/popup/minimize.png 

Border color:

  * org.openbravo.client.application/ob-popup-styles.css -> .OBPopupIconMinimize* -> border-color 

###  Restore button

Icon:

  * org.openbravo.client.application/ob-popup-styles.js -> isc.OBPopup -> restoreButtonDefaults -> src 
  * org.openbravo.client.application/images/popup/restore.png 
  * org.openbravo.client.application/ob-dialog-styles.js -> isc.Dialog -> restoreButtonDefaults -> src 
  * org.openbravo.client.application/images/popup/restore.png 

Border color:

  * org.openbravo.client.application/ob-popup-styles.css -> .OBPopupIconRestore* -> border-color 

###  Close button

Icon:

  * org.openbravo.client.application/ob-popup-styles.js -> isc.OBPopup -> closeButtonDefaults -> src 
  * org.openbravo.client.application/images/popup/close.png 
  * org.openbravo.client.application/ob-dialog-styles.js -> isc.Dialog -> closeButtonDefaults -> src 
  * org.openbravo.client.application/images/popup/close.png 

Border color:

  * org.openbravo.client.application/ob-popup-styles.css -> .OBPopupIconClose* -> border-color 

##  Dialog

![](/assets/developer-guide/etendo-classic/concepts/Skins-8.png){: .legacy-image-style}

Text:

  * org.openbravo.client.application/ob-dialog-styles.css -> .OBDialogLabel 

Link color:

  * org.openbravo.client.application/ob-styles.css -> .OBDialogLabel a -> color 
  * org.openbravo.client.application/ob-styles.css -> .OBDialogLabel a:hover -> color 
  * org.openbravo.client.application/ob-styles.css -> .OBDialogLabel a:active -> color 
  * org.openbravo.client.application/ob-styles.css -> .OBDialogLabel a:focus -> color 

##  Workspace

![](/assets/developer-guide/etendo-classic/concepts/Skins-9.png){: .legacy-image-style}

###  Left items

Sections title underline color:

  * org.openbravo.client.myob/ob-myopenbravo-styles.css -> .OBMyOBRecentViews -> border-bottom-color 

Recent Views icon: shared with "Application Menu: Content icons"

Create new in "Recent views" icon:

  * org.openbravo.client.myob/ob-myopenbravo-styles.js -> OB.Styles.OBMyOpenbravo.recentViewsLayout.newIcon.src 
  * org.openbravo.client.myob/images/management/iconCreateNew.png 

Add Widget and Admin Others dialog:

  * org.openbravo.client.myob/ob-myopenbravo-styles.js -> isc.OBMyOBDialog -> edgeImage 
  * org.openbravo.client.myob/images/dialog/window.png 

  * org.openbravo.client.myob/ob-widget-styles.css -> .OBMyOBDialog -> background-color 

Add Widget combo box: done as "Form" one (but not shared). Defined in:

  * org.openbravo.client.myob/ob-myopenbravo-styles.js -> OB.Styles.OBMyOBAddWidgetDialog.* 
  * org.openbravo.client.myob/ob-myopenbravo-styles.js -> OB.Styles.OBMyOBAddWidgetDialog.pickerIconSrc 
  * org.openbravo.client.application/images/form/comboBoxPicker.png 
  * org.openbravo.client.myob/ob-myopenbravo-styles.css -> .OBMyOBDialog -> background-color 

Admin Others combo box: done as "Form" one (but not shared). Defined in:

  * org.openbravo.client.myob/ob-myopenbravo-styles.js -> OB.Styles.OBMyOBAdminModeDialog.* 
  * org.openbravo.client.myob/ob-myopenbravo-styles.js -> OB.Styles.OBMyOBAdminModeDialog.pickerIconSrc 
  * org.openbravo.client.application/images/form/comboBoxPicker.png 
  * org.openbravo.client.myob/ob-myopenbravo-styles.css -> .OBMyOBDialog -> background-color 

###  Widgets

####  Border

Color:

  * org.openbravo.client.myob/ob-widget-styles.js -> isc.OBWidget -> edgeImage 
  * org.openbravo.client.myob/images/widget/window.png 

####  Edit button

Icon:

  * org.openbravo.client.myob/ob-widget-styles.js -> isc.OBWidgetMenuItem -> menuButtonImage 
  * org.openbravo.client.myob/images/widget/edit.png 

Border color:

  * org.openbravo.client.myob/ob-widget-styles.css -> .OBWidgetMenuButton* img -> background 

Dialog border color:

  * org.openbravo.client.myob/ob-widget-styles.css -> .OBWidgetMenu -> border-color 

Dialog background color:

  * org.openbravo.client.myob/ob-widget-styles.css -> .OBWidgetMenuTable -> background 
  * org.openbravo.client.myob/ob-widget-styles.css -> .OBWidgetMenuTable -> border-color 

Dialog separator color:

  * org.openbravo.client.myob/ob-widget-styles.css -> .OBWidgetMenuCellTitleFieldDisabled hr -> border-color 
  * org.openbravo.client.myob/ob-widget-styles.css -> .OBWidgetMenuCellIconFieldDisabled hr -> border-color 

Dialog entry text color:

  * org.openbravo.client.myob/ob-widget-styles.css -> .OBWidgetMenuCell* -> color 

Dialog disabled entry text color:

  * org.openbravo.client.myob/ob-widget-styles.css -> .OBWidgetMenuCellDisabled -> color 
  * org.openbravo.client.myob/ob-widget-styles.css -> .OBWidgetMenuCellIconFieldDisabled -> color 
  * org.openbravo.client.myob/ob-widget-styles.css -> .OBWidgetMenuCellTitleFieldDisabled -> color 

####  Maximize button

Icon:

  * org.openbravo.client.myob/ob-widget-styles.js -> isc.OBWidget -> maximizeButtonDefaults -> src 
  * org.openbravo.client.myob/images/widget/maximize.png 

Border color:

  * org.openbravo.client.myob/ob-widget-styles.css -> .OBWidgetIconMaximize* -> border-color 

####  Minimize button

Icon:

  * org.openbravo.client.myob/ob-widget-styles.js -> isc.OBWidget -> minimizeButtonDefaults -> src 
  * org.openbravo.client.myob/images/widget/minimize.png 

Border color:

  * org.openbravo.client.myob/ob-widget-styles.css -> .OBWidgetIconMinimize* -> border-color 

####  Restore button

Icon:

  * org.openbravo.client.myob/ob-widget-styles.js -> isc.OBWidget -> restoreButtonDefaults -> src 
  * org.openbravo.client.myob/images/widget/restore.png 

Border color:

  * org.openbravo.client.myob/ob-widget-styles.css -> .OBWidgetIconRestore* -> border-color 

####  Close button

Icon:

  * org.openbravo.client.myob/ob-widget-styles.js -> isc.OBWidget -> closeButtonDefaults -> src 
  * org.openbravo.client.myob/images/widget/close.png 

Border color:

  * org.openbravo.client.myob/ob-widget-styles.css -> .OBWidgetIconClose* -> border-color 

Retrieved from "  http://wiki.openbravo.com/wiki/Skins  "

This page has been accessed 18,312 times. This page was last modified on 21
May 2012, at 14:28. Content is available under  Creative Commons Attribution-
ShareAlike 2.5 Spain License  .

  
**

Category  :  Concepts

**

