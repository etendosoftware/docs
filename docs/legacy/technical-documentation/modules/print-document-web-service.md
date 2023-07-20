---
title: Print Document Web Service
---
This module provides a web service called **printDocument**. To call the Web Service, the following URL is needed:
`http://client-url/etendo/sws/com.etendoerp.printdocumentws.printDocument
`
It is necessary to configure Token authentication to use the web service. 

This is a RESTful Web Service that returns a .pdf file of the document using the template that is configured.
The supported documents are:
- Sales Quotation
- Invoice
- Shipment
- Proforma Order
- Proforma Quotation
