---
title: Warehose Extensions Bundle | Technical Documentation
---

:octicons-package-16: Javapackage: `com.etendoerp.warehouse.extensions`

## Overview

In this section, the user can find technical information about the Warehouse Extensions Bundle.

## Stock History 

:octicons-package-16: Javapackage: `com.etendoerp.stock.history`

This module is added to the Create Stock History process and has the following characteristics: 

It takes all the stock data from each product (present in the table `m_storage_detail_history`) and enters them into the table `etst_storage_detail_history`, under the day the process was executed. If there is already data loaded on that date it is overwritten with the new data. The whole process is monitored by logs that can be viewed in the 'Process Request' window under the 'Process Monitor' tab of the process.

If the user would like to make changes on the table, and would like them to be taken into account in the data loading process, it  can be done by means of the hooks functionality present in the module. Just create a class that implements the StockHistoryHooks interface and extends the StockHistoryPioritizer abstract class, and implement the desired functionality under the doExecute method. This method will be executed once for each row added to the table. If multiple instances of the same interface are implemented, the order of execution can be decided by the getPriority method. The priority is given by how close to 0 is the number returned by this method. 

### How to define a Stock History Hook 

- Define the class for the hook, extending the abstract class StockHistoryHookPrioritizer and implementing the interface StockHistoryHook:

    ```java
    import com.etendoerp.stock.history.hooks.StockHistoryHookPrioritizer;
    import com.etendoerp.stock.history.hooks.StockHistoryHook;

    public class ExampleHook extends StockHistoryHookPrioritizer
      implements StockHistoryHook {
    }
    ```

- Implement the abstract methods of the interface and abstract class: 


    ```java
    import com.etendoerp.stock.history.data.ETSTStorageDetailHistory;
    import com.etendoerp.stock.history.hooks.StockHistoryHookPrioritizer;
    import com.etendoerp.stock.history.hooks.StockHistoryHook;

    public class ExampleHook extends StockHistoryHookPrioritizer
      implements StockHistoryHook {

    @Override
    public void exec(ETSTStorageDetailHistory hookObject) throws Exception {
      System.out.println("This is the ExampleHook hook");
    }

    @Override
    public int getPriority() {
      return 0;
    }
    }
    ``` 

### Uninstall module

To uninstall the module and prevent future problems with orphan records, a sequence of steps must be followed:

1. Run the following query in the environment's database
```
DELETE FROM OBUIAPP_GC_TAB 
WHERE AD_TAB_ID = 'C3DB551F2BCA40A79AAF21DBD6D06309';
```

2. After the query successfully finishes, delete the module by the way corresponding to the installation method (Sources/JARs)

---

This work is a derivative of [Developer Guide](https://wiki.openbravo.com/wiki/Category:Developers_Guide){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.