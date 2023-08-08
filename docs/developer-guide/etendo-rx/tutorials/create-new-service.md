# Creating a New Spring Boot Service

Before proceeding, make sure you've successfully completed the [Configure Spring boot project](/docs/developer-guide/etendo-rx/tutorials/create-spring-boot-project.md) step.

Follow the instructions below to create a new service:

1. Create a new file at the following path:

```
modules_rx/com.tutorial.rxtutorial/src/main/java/com/tutorial/rxtutorial/RxtutorialService.java
```

2. Then, copy and paste the following code into the file:

```java
package com.tutorial.rxtutorial;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.etendorx.clientrest.base.RestUtils;
import com.etendorx.clientrest.base.RestUtilsException;
import com.tutorial.rxtutorial.entities.org.openbravo.model.common.order.OrderRxtutorialModel;

@RestController
@RequestMapping(path = "/api")
public class RxtutorialService {
  @Autowired
  RestUtils restUtils;

  @GetMapping(path = "/")
  public String get() throws RestUtilsException {
    String url = "/Order/search/findSalesOrder?documentType=AB22CE8FFA5E4AF29F2AC90FCDD400D8&projection=rxtutorial";
    var orders = restUtils.getList(url, OrderRxtutorialModel.class);
    StringBuilder html = new StringBuilder("<html>");
    html.append("<head>");
    html.append("<style type=\"text/css\">html {font-family: sans-serif;}</style>");
    html.append("</head>");
    html.append("<title>Orders</title></head>");
    html.append("<body>");
    html.append("<h2>Orders</h2>");
    html.append("<table>");
    for (OrderRxtutorialModel o : orders) {
      html.append(
          "<tr>" +
              "<td>" + o.getDocumentNo() + "</td>" +
              "<td>" + o.getBusinessPartnerName() + "</td>" +
              "<td>" + o.getDocumentTypeName() + "</td>" +
              "<td>" + o.getGrandTotalAmount() + "</td>" +
              "</tr>"
      );
    }
    html.append("</table></body></html>");
    return html.toString();
  }
}
```

Well done! You've successfully created a new service for consuming data from Etendo RX. To continue with the tutorial, please navigate to the [**Tutorials**](/docs/developer-guide/etendo-rx/tutorials) section.
