---
title: Multi Business Partner Selector
---
This module allows the user to select multiple business partners in the user interface.

The multiple business partner selector can be integrated into other pages. The selector consists of two main parts:

-   A widget which should be included in each page using this business partner selector
-   A popup window which is delivered as part of this module

## Example page

After installing this module there will be a menu-entry 'Multi Business Partner Selector'. This menu item starts an example page for the business partner selector. The example page can be found in the module inside the directory: `modules/org.openbravo.module.multibpselector/src/org/openbravo/module/multibpselector`

The example page consists of the following parts:

-   **ExampleSelectorUsage.java**: the servlet filling form data and capturing the selected business partners.
-   **ExampleSelectorUsage\_W1.html (and its xml)**: the first page of the example
-   **ExampleSelectorUsage\_W2.html (and its xml)**: the second page of the example

The example code contains markers where the multiple business partner selector code has been added. Look for this mark in the code: `+++++++++ MULTIBPSelector +++++++`. That is where the specific selector handling has been added.

## Integrating the widget in your page

To integrate this widget and make use of it, the following steps are needed:

-   Add specific html on the page (for the widget itself)
-   Add javascript which is executed just before the form is submitted
-   Retrieve the selected business partners on the server (in the servlet)

### HTML Widget

The HTML for the widget itself is shown below. The content of the widget is controlled by a HTML select tag.

```plaintext
<table class="Main_Client_TableEdition">
    <tr>
        <td class="TableEdition_OneCell_width"></td>
        <td class="TableEdition_OneCell_width"></td>
        <td class="TableEdition_OneCell_width"></td>
        <td class="TableEdition_OneCell_width"></td>
        <td class="TableEdition_OneCell_width"></td>
        <td class="TableEdition_OneCell_width"></td>
    </tr>

    <tr>
        <td class="TitleCell"><span class="LabelText">Business Partner</span></td>
        <td class="List_ContentCell" colspan="2">

        <table border="0" cellspacing="0" cellpadding="0">
        <tr>
            <td>
               <select class="List_width List_height"
                     name="inpcBPartnerId_IN" multiple="" id="reportCBPartnerId_IN">
                  <div id="sectionBusinessPartners" />
               </select></td>
            <td class="List_Button_ContentCell">
               <table border="0" cellspacing="0" cellpadding="0">
               <tr>
                  <td><a class="List_Button_TopLink" href="#"
                      onclick="openMultiSearch(null, null, '../multibpselector/BusinessPartnerSelectorMULTIBP.html', 'SELECTOR_BUSINESS', false, 'frmMain', 'inpcBPartnerId_IN');return false;"
                      onfocus="setWindowElementFocus(this); window.status='Add'; return true;"
                      onblur="window.status=''; return true;"
                      onkeypress="this.className='List_Button_TopLink_active'; return true;"
                      onkeyup="this.className='List_Button_TopLink_focus'; return true;">
                       
                       <table class="List_Button_Top"
                             onmousedown="this.className='List_Button_Top_active'; return true;"
                             onmouseup="this.className='List_Button_Top'; return true;"
                             onmouseover="this.className='List_Button_Top_hover'; window.status='Add'; return true;"
                             onmouseout="this.className='List_Button_Top'; window.status=''; return true;">
                             <tr>
                                <td class="List_Button_Top_bg">
                                   <img class="List_Button_Icon List_Button_Icon_Add"
                                        src="../../../../../web/images/blank.gif" alt="Add"
                                        title="Add" /></td>
                             </tr>
                       </table>
                       </a>
                   </td>
                </tr>
                <tr>
                   <td class="List_Button_Separator"></td>
                </tr>
                <tr>
                   <td><a class="List_Button_MiddleLink" href="#"
                           onclick="clearSelectedElements(document.frmMain.inpcBPartnerId_IN);return false;"
                           onfocus="setWindowElementFocus(this); window.status='Delete selected elements'; return true;"
                           onblur="window.status=''; return true;"
                           onkeypress="this.className='List_Button_MiddleLink_active'; return true;"
                           onkeyup="this.className='List_Button_MiddleLink_focus'; return true;">
                           <table class="List_Button_Middle"
                              onmousedown="this.className='List_Button_Middle_active'; return true;"
                              onmouseup="this.className='List_Button_Middle'; return true;"
                              onmouseover="this.className='List_Button_Middle_hover'; window.status='Delete selected elements'; return true;"
                              onmouseout="this.className='List_Button_Middle'; window.status=''; return true;">
                              <tr>
                                 <td class="List_Button_Middle_bg">
                                 <img class="List_Button_Icon List_Button_Icon_Delete"
                                      src="../../../../../web/images/blank.gif"
                                      alt="Delete selected elements"
                                      title="Delete selected elements" /></td>
                              </tr>
                            </table>
                           </a></td>
                        </tr>
                        <tr>
                           <td class="List_Button_Separator"></td>
                        </tr>
                        <tr>
                           <td><a class="List_Button_BottomLink" href="#"
                                  onclick="clearList(document.frmMain.inpcBPartnerId_IN);return false;"
                                  onfocus="setWindowElementFocus(this); window.status='Delete all elements'; return true;"
                                  onblur="window.status=''; return true;"
                                  onkeypress="this.className='List_Button_BottomLink_active'; return true;"
                                  onkeyup="this.className='List_Button_BottomLink_focus'; return true;">
                                  <table class="List_Button_Bottom"
                                      onmousedown="this.className='List_Button_Bottom_active'; return true;"
                                      onmouseup="this.className='List_Button_Bottom'; return true;"
                                      onmouseover="this.className='List_Button_Bottom_hover'; window.status='Delete all elements'; return true;"
                                      onmouseout="this.className='List_Button_Bottom'; window.status=''; return true;">
                            <tr>
                               <td class="List_Button_Bottom_bg">
                                  <img class="List_Button_Icon List_Button_Icon_DeleteAll"
                                       src="../../../../../web/images/blank.gif"
                                       alt="Delete all elements" title="Delete all elements" />
                                </td>
                             </tr>
                         </table>
                     </a></td>
                 </tr>
            </table>
        </td>
    </tr>
</table>
```

The name of the `select` in the HTML is `inpcBPartnerId_IN` and its id is `reportCBPartnerId_IN`. The name is used for server side handling of the selected business partners, the id is used for client side handling.

```plaintext
<select class="List_width List_height" name="inpcBPartnerId_IN" multiple="" id="reportCBPartnerId_IN">
 <div id="sectionBusinessPartners" />
</select>
```

Inside the `select` there is a `div`. The `div` is used by the xml engine to fill the select. Initially the select is empty.

If you have multiple business partner widgets on one page then you have to give hem a unique id and name. Also the `div` inside the `select` needs to have a unique id.

### JavaScript

The selector popup will return the selected business partners, which are displayed in the widget (converted to select options). None of the shown business partners (in the widget) is selected. So if the form is posted, no information is shown serverside. Therefore a piece of JavaScript is required. This code should be executed when the form is submitted.

In a standard Etendo page there should be a validate JavaScript method.  
Just before the form submit, the method `markCheckedAllElements` should be called with the `select` element as the JS parameter. The `markCheckedAllElements` method is available in the JS library `web/js/utils.js`, which is part of the **Etendo** distribution.

```plaintext
// this method is called just before form submit  
function validate() {
  // +++++++++ MULTIBPSelector +++++++++++++++++++
  // required otherwise are multi-selected values not passed back  
  var frm = document.frmMain;
  markCheckedAllElements(frm.inpcBPartnerId_IN);
  // +++++++++ MULTIBPSelector +++++++++++++++++++
  return true;
}
```

### Server Side Handling

When the page with the business partner selector widget is posted to the server, the id's of the selected business partners is passed to the server in the `inpcBPartnerId_IN` request parameter (the name of the HTML select tag in the widget). The value is a multi-valued request parameter. So its value should be retrieved using the `getParameterValues` method of the HttpServletRequest object:

`request.getParameterValues("inpcBPartnerId_IN")`

The example page shows how the selected business partners are displayed in the second page and also how to support moving back to the first page and re-displaying the selected business partners.

---

This work is a derivative of ["Multibpselector/Programmers Guide"](http://wiki.openbravo.com/wiki/Projects:Multibpselector/Programmers_Guide) by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo), used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/). This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/) by [Etendo](https://etendo.software).