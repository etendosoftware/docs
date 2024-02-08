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

  

#  Modules:How to create a Carrier Integration Module

##  Contents

  * 1  Objective 
  * 2  Module Definition 
  * 3  Application Dictionary 
    * 3.1  Parametrization window 
    * 3.2  Other extended entities 
  * 4  CarrierIntegration Java Class implementation 
    * 4.1  Overview 
    * 4.2  Initialization 
    * 4.3  Validation 
    * 4.4  Process 
      * 4.4.1  Create SOAP Message 
      * 4.4.2  Send SOAP Message 
      * 4.4.3  Read response 

  
---  
  
##  Objective

The objective of this _How to_ article is to describe how to develop a new
module Integrating a Carrier platform with Openbravo using the  Freight
Management  .

The development of the integration might differ between carriers. They might
need different parameters in different formats. And they can use different
protocols to connect to their platforms. In this _how to_ document is used as
example the  Seur Spain Integration  module. This carrier has a web service
platform using the SOAP protocol. To connect to that web services and properly
integrate the deliveries some parameters that are not included in Openbravo
are needed, so a new table and window is needed to store them.

Before starting to develop your own _Carrier Integration Module_ is strongly
recommended to be in contact with the Carrier. You need to know how to connect
with their platform. In case web services are used how to format the XML or
the JSON that has to be sent and the information that needs to be included.
Having this information it has to be decided if a parametrization table/window
is needed or existing entities like _Pack_ or _Box_ needs to be extended.

##  Module Definition

The module is defined as a regular extension module. The dependency must be
set on  Carrier Base Integration  module. Additional dependencies might be
added when needed.

##  Application Dictionary

The module needs to include a record in the _Carrier Integration_ window of
_System Administrator_ . In this window is defined the _Java Class_ that
includes the integration process. This record is exported as  sourcedata  so
it is not needed to create any _Dataset_ . This is needed as later when each
_Carrier_ is configured it will be needed to select the _Carrier Integration_
.

###  Parametrization window

The Seur platform needs some Entity specific parameters that are not in
Openbravo by default. For example a User and password, a company
identifier,.... To store them a Configuration table  OBEUSES_Seur_Conf  is
created. As the parameters are Entity specific the table is created with
_System/Client_ _Data Access Level_ . This allows to have a different
parametrization on each Entity in the Openbravo's instance.

**OBEUSES_Seur_Conf** table's columns  Name  |  Columnname  |  Type  |
Default Value  
---|---|---|---  
Obeuses_Seur_Conf_ID  |  Obeuses_Seur_Conf_ID  |  ID  |  
Client  |  AD_Client_ID  |  TableDir  |  @AD_CLIENT_ID@  
Organization  |  AD_Org_ID  |  TableDir  |  @AD_ORG_ID@  
Active  |  Isactive  |  YesNo  |  Y  
Creation Date  |  Created  |  DateTime  |  SYSDATE  
Created By  |  Createdby  |  Search  |  
Updated  |  Updated  |  DateTime  |  SYSDATE  
Updated By  |  Updatedby  |  Search  |  
Name  |  Name  |  String  |  
URL  |  Url  |  String  |  
Carrier Conf  |  Obeuci_Carrier_ID  |  TableDir  |
_65E310719961414F8CF63F685B24A996_  
Username  |  Username  |  String  |  
Password  |  Password  |  Password (decryptable)  |  
Printer_Brand  |  Printer_Brand  |  String  |  
Printer_Model  |  Printer_Model  |  String  |  
Print_Format  |  Print_Format  |  List  |  
File_Name  |  File_Name  |  String  |  
Franchise_Code  |  Franchise_Code  |  String  |  
CC_Code  |  CC_Code  |  String  |  
Invoker  |  Invoker  |  String  |  
CCC_Code  |  CCC_Code  |  String  |  
Code_CI  |  Code_CI  |  String  |  
  
The table has a foreign key to the _Carrier Integration_ window. The column
has as default value _UUID_ of the record added by the module. As that
information is stored as sourcedata this ID won't change on different
instances of Openbravo. This makes easier to retrieve the configuration
parameters having from the _Carrier Integration_ record.

The rest of the _Columns_ includes values that need to be included in the XML
sent to Seur platform and are not available in the System.

###  Other extended entities

The Seur platform also includes some other parameters that can be different on
each delivery. Instead of defining them on the _Parametrization_ table these
values are included extending existing entities.

When a delivery is registered in the platform it is needed to choose a
_Service_ ( _24 hours, same day,48 hours,..._ ) and a _Seur Product_ (
_Standard_ , _Multipack_ , _Cold_ ). These values are configured on each
_Freight_ defined on the _Carrier_ . New fields and columns are added in the
_Freight_ tab of the _Carrier_ window ( _OBMFM_Freight_ table). These fields
uses new Lists references with all available values provided by Seur. When the
SOAP Message is being built the _Service_ and _Seur Product_ are retrived from
the _Freight_ assigned to the delivered _Pack_ .

The integration process returns a _Print Trace_ for each delivered _Pack_ with
box's labels. This is stored as a hidden _blob_ column in the
_OBWPACK_PackingH_Id_ table. So it can be used later by additional custom
processes.

##  _CarrierIntegration_ Java Class implementation

Once the Application Dictionary data is created it is time to create the Java
Class extending _CarrierIntegration_ where the integration process is
developed. The name of this  class  has to match the Java Class defined in the
_Carrier Integration_ window.

` `

    
    
    public class SeurIntegration extends CarrierIntegration 
    

###  Overview

The _CarrierIntegration_ class managed the integration process. This class is
initialized and executed by any process in the ERP that launches an
integration with a Carrier platform.

Each _Pack_ is integrated separately in different integrations. This means
that each _Pack_ uses its own instance of the _CarrierIntegration_ class. If
more than one pack is going to be delivered they are sent in different
instances.

A delivery of a _Pack_ is done in 3 steps. The first one is to initialize the
_CarrierInstance_ . This steps initializes some global variables. The _Pack_
and its _Boxes_ ordered by the _Box Number_ . And the _result_ to _unfinish_
and sets the _Error Msg_ to empty String.

The second step are the validations. There are two validations common to all
Carriers that are always checked, the existence of a _Business Partner_ and a
_Partner Address_ in the _Pack_ . If they are empty an exception is thrown. It
also checks the integration status of the _Pack_ to avoid sending again to the
platform the same pack. Each carrier integration might add new validations
implementing the _doValidate()_ abstract method. Any failure in a validation
should throw an exception.

The last step is the process. The process must be implemented by the
_Integration Modules_ extending the _doProcess()_ abstract method. This method
implements the needed actions to connect to the Carrier Platform and integrate
the delivery of the _Pack_ to the _Business Partner_ in the pack's _Partner
Address_ . This process must update the _Tracking Numbers_ of each box with
the result of the integration. The process can set any error message or change
the result using the _setResult()_ and _setErrorMsg()_ . This values are read
when the process is finished to build the message that it is shown to the user
when the process is finished. Any exception is caught by the
CarrierIntegration process, in this case a rollback is performed and the
result is set to _Error_ also the exception message is parsed and set in the
_Error Msg_ .

###  Initialization

The class includes an additional class private object with the _SeurConf_
record to be used. The _init()_ method is overridden to initialize it.

` `

    
    
      private SeurConf seurConf = null;
    
      @Override
      public void init(Packing _pack) {
        super.init(_pack);
        List<SeurConf> seurConfs = pack.getOBEUCIFreight().getCarrier().getOBEUCICarrierIntegration()
            .getOBEUSESSeurConfList();
        if (seurConfs.size() > 0) {
          seurConf = seurConfs.get(0);
        }
      }
    

Note that _getOBEUSESSeurConfList()_ automatically filters the list by the
Client. So only the records of the current client will be retrieved. As it
should only be one the first record of the List is used.

###  Validation

The next method that needs to be overridden is the _doValidate_ . In this case
4 additional validations are done.

  * Existence of a _SeurConf_ record. 
  * Existence of a _Seur Product_ in the _Pack's Freight_ . 
  * Existence of a _Seur Service_ in the _Pack's Freight_ . 
  * Existence of a _Document Number_ in the _Pack_ . The Seur platform requires a unique reference number for each pack delivered. The _Document Number_ is used on this purpose. 

` `

    
    
      @Override
      public void doValidate() {
        if (seurConf == null) {
          throw new OBException("@OBEUSES_ConfNotFound@");
        }
        if (pack.getOBEUCIFreight().getOBEUSESProduct() == null) {
          throw new OBException("@OBEUSES_SeurProductNotFound@");
        }
        if (pack.getOBEUCIFreight().getOBEUSESService() == null) {
          throw new OBException("@OBEUSES_SeurServiceNotFound@");
        }
        if (StringUtils.isEmpty(pack.getDocumentNo())) {
          throw new OBException("@OBEUSES_PackNoDocumentNumber@");
        }
    
      }
    

###  Process

Finally the _doProcess()_ method is implemented. In the case of the Seur
platform the integration is done with web services using the  SOAP  protocol.
To create and manage SOAP protocol the classes in _javax.xml.soap_ package are
used.

The process is structure on 3 steps. **Create** SOAP message, **Send** it and
**Read** the response.

` `

    
    
      @Override
      public void doProcess() {
        // Create SOAP Envelop
        SOAPMessage msg = createSOAPMessage();
    
        SOAPMessage response = sendSOAPMsg(msg);
    
        readResponse(response);
    
      }
    

  

####  Create SOAP Message

The message is created using standard methods adding a custom _Namespace_ to
the Envelope.

` `

    
    
         MessageFactory msgFactory = MessageFactory.newInstance();
         SOAPMessage msg = msgFactory.createMessage();
         SOAPPart part = msg.getSOAPPart();
         SOAPEnvelope envelope = part.getEnvelope();
         envelope.addNamespaceDeclaration("imp", "http://{service url}");
         SOAPBody body = envelope.getBody();
    

Once we have the _SOAPBody_ it is time to add the parameters needed for the
_Service_ that we are going to use. In this case we are using a service that
integrates the _Pack_ that it is being delivered and returns a _Tracking
Number_ for each _Box_ of the _Pack_ and a _Print Trace_ for the labels. This
service has 10 input parameters. In the below code snippet is shown how some
of them are added to the body;

` `

    
    
         SOAPElement printElement = body.addChildElement("{service name}", "imp");
         printElement.addChildElement("in0", "imp").addTextNode(seurConf.getUsername());
         final String strPassword = FormatUtilities.encryptDecrypt(seurConf.getPassword(), false);
         printElement.addChildElement("in1", "imp").addTextNode(strPassword);
    ...
         printElement.addChildElement("in5", "imp").addTextNode(getBoxesXML());
    ...
         printElement.addChildElement("in7", "imp").addTextNode(getNIF());
    ...
         String strInvoker = seurConf.getInvoker();
         if (StringUtils.isEmpty(strInvoker)) {
           strInvoker = "Openbravo";
         }
         printElement.addChildElement("in10", "imp").addTextNode(strInvoker);
    

  * A new _SOAPElement_ is added to the body with the _service_ that is desired to use. 
  * The User Name is retrieved from global _seurConf_ object. 
  * The password is sent decrypted. The FormatUtilities class is used to decrypt it. 
  * The 5th parameter is the boxes definition that it is described below. In this case the content is an xml file that is built in the _getBoxesXML()_ method. 
  * The 7th parameter is the _NIF_ or the Entity's _Tax ID_ . It is used the value defined in the Legal Entity Organization of the Pack. 
  * The 10th parameter is the _Invoker_ . If it is empty _Openbravo_ is sent. 

**getBoxesXML method**

The getBoxesXML method creates the XML with the information of the Boxes and
the Delivery contact and address. To create the XML the _org.dom4j_ package is
used.

` `

    
    
       final Document boxesXML = DocumentHelper.createDocument();
       final Element root = boxesXML.addElement("root");
       final Element exp = root.addElement("exp");
    

Inside the _exp_ element is added a _bulto_ element for each delivered box.
Each box contains all the information needed for the delivery. All the
elements of the box are stored in a _Map <String, Object> _ later this _Map_
is converted to elements inside the _bulto_ element.

` `

    
    
       for (PackingBox box : boxes) {
         final Element bulto = exp.addElement("bulto");
         Map<String, Object> boxDef = new HashMap<String, Object>();
         ...
         boxDef.put("servicio", pack.getOBEUCIFreight().getOBEUSESService());
         boxDef.put("producto", pack.getOBEUCIFreight().getOBEUSESProduct());
         boxDef.put("total_bultos", Integer.toString(pack.getOBWPACKBoxList().size()));
         boxDef.put("total_kilos", pack.getTotalweight());
         boxDef.put("pesoBulto", box.getWeight());
         ...
         // Customer contact
         if (!OBDao.getActiveOBObjectList(customer, BusinessPartner.PROPERTY_ADUSERLIST).isEmpty()) {
           User contact = (User) OBDao.getActiveOBObjectList(customer,
               BusinessPartner.PROPERTY_ADUSERLIST).get(0);
           boxDef.put("email_consignatario", contact.getEmail());
           boxDef.put("sms_consignatario", contact.getPhone());
           ...
         }
         for (String key : boxDef.keySet()) {
           Object value = boxDef.get(key);
           if (value == null) {
             value = "";
           }
           if (value instanceof Long) {
             value = Long.toString((Long) value);
           }
           if (value instanceof BigDecimal) {
             value = ((BigDecimal) value).toPlainString();
           }
           bulto.addElement(key).addText((String) value);
         }
    

Finally the encoding required by Seur is set and the XML file is generated.
The xml needs to be included in _CDATA_ tags, they are also included.

` `

    
    
       try {
         final OutputFormat format = OutputFormat.createPrettyPrint();
         format.setEncoding("ISO-8859-1");
         format.setTrimText(false);
         final StringWriter out = new StringWriter();
         final XMLWriter writer = new XMLWriter(out, format);
         writer.startCDATA();
         writer.write(boxesXML);
         writer.endCDATA();
         writer.close();
         return out.toString();
       } catch (final Exception e) {
         throw new OBException(e);
       }
    

The result is a XML with the following structure:

` `

    
    
    <?xml version="1.0" encoding="ISO-8859-1"?>
    <root><exp>
      <bulto>
        <nif>BXXXXXXXX</nif>
        <servicio>31</servicio>
        <producto>2</producto>
        <total_bultos>2</total_bultos>
        <total_kilos>14</total_kilos>
        <pesoBulto>10.0000</pesoBulto>
        <referencia_expedicion>DEMO-01</referencia_expedicion>
        <ref_bulto>DEMO-01-1</ref_bulto>
        ...
      </bulto>
      <bulto>
        <nif>BXXXXXXXX</nif>
        <servicio>31</servicio>
        <producto>2</producto>
        <total_bultos>2</total_bultos>
        <total_kilos>14</total_kilos>
        <pesoBulto>4.0000</pesoBulto>
        <referencia_expedicion>DEMO-01</referencia_expedicion>
        <ref_bulto>DEMO-01-2</ref_bulto>
        ...
      </bulto>
    </exp></root>
    

The resulting SOAP message has the following structure:

` `

    
    
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:imp="http://{webservice url}">
      <soapenv:Header/>
      <soapenv:Body>
        <imp:{service name}>
          <imp:in0>{username}</imp:in0>
          <imp:in1>{password}</imp:in1>
          <imp:in2>{printer brand}</imp:in2>
          <imp:in3>{printer model}</imp:in3>
          <imp:in4>{print format}</imp:in4>
          <imp:in5><![CDATA[<?xml version="1.0" encoding="ISO-8859-1"?>
          </imp:in5>
          ...
          <imp:in10>{invoker}</imp:in10>
        </imp:{service name}>
      </soapenv:Body>
    </soapenv:Envelope>
    

####  Send SOAP Message

The SOAP Message is sent using the SOAPConnection class. The call method sends
the message to the specified _URL_ and returns the response SOAP MEssage.

` `

    
    
       try {
         SOAPConnectionFactory connectionFactory = SOAPConnectionFactory.newInstance();
         SOAPConnection connection = connectionFactory.createConnection();
         URL url = new URL(seurConf.getURL());
         SOAPMessage response = connection.call(msg, url);
         return response;
       } catch (SOAPException e) {
         throw new OBException("Error conecting to web service: " + e.getMessage(), e);
       } catch (MalformedURLException e) {
         throw new OBException("@OBEUSES_WrongURL@" + e.getMessage(), e);
       }
    

####  Read response

The final step is to read the response to retrieve the tracking numbers and
the print trace. Or getting the error message in case there has been any issue
in the process.

When the integration has been successful the SOAP Message contains an element
_ECB_ which contains as many parameters as boxes with the Tracking Numbers.
And an element _traza_ with the print trace.

` `

    
    
    <ns1:{service name} xmlns:ns1="{webservice url}">
      <ns1:out>
        < **ECB** xsi:nil="true" xmlns="{}">
          <imp:out0>{ **tracking number 0** }</imp:out0>
          ...
          <imp:outN>{ **tracking number N** }</imp:outN>
        </ **ECB** >
        <mensaje xmlns="{}">
        < **traza** xsi:nil="true" xmlns="{}">{ **print trace** }</ **traza** >
      </ns1:out>
    </ns1:{servicename}>
    

When the integration return an error the SOAP Message has the error message in
an element called _mensaje_ and no tracking number or print trace is included.

` `

    
    
    <ns1:{service name} xmlns:ns1="{webservice url}">
      <ns1:out>
        <ECB xsi:nil="true" xmlns="{}"/>
        < **mensaje** xmlns="{}">{ **Error message** }</ **mensaje** >
        <traza xsi:nil="true" xmlns="{}"/>
      </ns1:out>
    </ns1:{service name}>
    

  
These messages are parsed with the following code. First the message is parsed
to get the _out_ element. That contains the relevant elements with the desired
information.

` `

    
    
    SOAPBody body = response.getSOAPBody();
    SOAPElement base = (SOAPElement) body.getChildNodes().item(0);
    SOAPElement out = (SOAPElement) base.getChildNodes().item(0);
    

Then is checked the _mensaje_ element to retrieve any error message. In case
there is any message it is parsed and an exception is thrown. The message can
be an XML so it is loaded to print it.

` `

    
    
    NodeList errorMsgList = out.getElementsByTagName("mensaje");
    String strErrorMsg = errorMsgList.item(0).getTextContent();
    if (StringUtils.isNotEmpty(strErrorMsg) && !"OK".equals(strErrorMsg)) {
      OBDal.getInstance().rollbackAndClose();
      try {
        final Document errorMsgXml = DocumentHelper.parseText(strErrorMsg);
        throw new OBException(errorMsgXml.toString());
      } catch (DocumentException e) {
        throw new OBException(strErrorMsg);
      }
    }
    

If there isn't any message the _ECBs_ and the _traza_ is read to store them in
the corresponding fields of the _Boxes_ and the _Pack_ . Note that the List of
_boxes_ has been initializated ordered by the box number so they are always
iterated in the same order.

` `

    
    
    SOAPElement ecbElement = (SOAPElement) out.getElementsByTagName("ECB").item(0);
    Iterator<?> ecbs = ecbElement.getChildElements();
    int boxNo = 0;
    while (ecbs.hasNext()) {
      SOAPElement ecb = (SOAPElement) ecbs.next();
      String strTrackingNo = ecb.getTextContent();
      PackingBox box = boxes.get(boxNo);
      box.setTrackingNo(strTrackingNo);
      OBDal.getInstance().save(box);
      boxNo++;
    }
    
    SOAPElement printTraceElement = (SOAPElement) out.getElementsByTagName("traza").item(0);
    String strPrintTrace = printTraceElement.getTextContent();
    pack.setOBEUSESPrintTrace(strPrintTrace.getBytes());
    OBDal.getInstance().save(pack);
    

In order to be able to debug the SOAP Messages an private method is created to
convert them to String.

` `

    
    
     private String getMsgAsString(SOAPMessage message) {
       String msg = null;
       try {
         ByteArrayOutputStream baos = new ByteArrayOutputStream();
         message.writeTo(baos);
         msg = baos.toString();
       } catch (Exception e) {
         e.printStackTrace();
       }
       return msg;
     }
    

Retrieved from "
http://wiki.openbravo.com/wiki/Modules:How_to_create_a_Carrier_Integration_Module
"

This page has been accessed 7,523 times. This page was last modified on 14
March 2014, at 09:25. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**

