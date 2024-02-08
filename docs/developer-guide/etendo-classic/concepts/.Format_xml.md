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

  

#  Format.xml

##  Contents

  * 1  Overview 
  * 2  Format.xml example 
    * 2.1  Attributes 
  * 3  Application dictionary - format name mapping 
  * 4  Important Notes 
  * 5  Export to CSV format 

  
---  
  
##  Overview

Format.xml is a configuration file per Openbravo installation that allows you
configure the format output for numeric values. It's used by the different
numeric  references  in Application Dictionary, but also can be used in
_manual_ code. By default Openbravo ships a Format.xml.template that can be
copied as it is without any modification.

![](/assets/developer-guide/etendo-classic/concepts/Bulbgraph.png){: .legacy-image-style} |  If you
are building Openbravo from sources, the setup-properties binary makes a copy
of it for you.  
---|---  
  
##  Format.xml example

    
    
     
    <?xml version="1.0" encoding="UTF-8" ?>
    <!-- license -->
    <Formats>
    <!-- other formats -->
       <Number name="euroEdition"
           decimal="." grouping="," formatOutput="#0.00" formatInternal="#0.00" />
    <!-- other formats -->
    </Formats>

###  Attributes

  * name: Name of the format, used to identify it 
  * decimal: Symbol (character) to be used as decimal separator 
  * grouping: Symbol (character) to be used as grouping separator (used in thousands) 
  * formatOutput: Format mask used to mask and print numeric inputs. It must be DecimalFormat output format type: See  DecimalFormat  class. 
  * formatInternal: Used internally by XmlEngine 

##  Application dictionary - format name mapping

AD Reference  |  Output format  
---|---  
Decimal, Amount  |  euroEdition  
Quantity  |  qtyEdition  
Price  |  priceEdition  
Integer  |  integerEdition  
Number  |  generalQtyEdition  
Others numeric  |  generalQtyEdition  
  
##  Important Notes

  * You can define a decimal and grouping separator per format type, but the **qtyEdition** format is the one that defines them. Makes no sense to define different decimal and grouping per format type. 
  * Rounding numeric values is also affected by the mask of the input. If you want more precision, change the output format attribute. 
  * Further details on formatting with XmlEngine can be found in the  XmlEngine concepts  page 
  * If you don't already have a Format.xml in the WEB-INF directory of your live Openbravo installation and want to experiment with various settings then copy $openbravo_source/config/Format.xml.template to $live_openbravo_installation/WEB-INF/Format.xml, edit it and restart Tomcat. Ultimately, copy $openbravo_source/config/Format.xml.template as Format.xml and "ant compile -Dtab=xx -Dtr=no" because this way the changes will be permament and won't be lost upon the next rebuild. 

##  Export to CSV format

The export to CSV functionality uses the Format.xml information to format the
data (specifically, it uses the decimal separator defined for the system for
numeric values).

This can be overwritten in case it is needed, by using the following
preferences:

  * CSV Decimal Separator: If this preference is defined, this will be used as the decimal separator for numbers. 
  * CSV Field Separator: If this preference is defined, this will be used as the field separator. Otherwise, a single comma ',' will be used. 
  * CSV Text Encoding: If this preference is set, this will be used as the encoding type of the generated file. The default encoding used is the Windows iso-8859-1, which will work correctly in Windows environments which use Microsoft Excel. Other popular encodings such as UTF-8 can be used in Linux or Mac environments which use other spreadsheets. 

Retrieved from "  http://wiki.openbravo.com/wiki/Format.xml  "

This page has been accessed 11,597 times. This page was last modified on 22
November 2011, at 16:35. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  Concepts

**

