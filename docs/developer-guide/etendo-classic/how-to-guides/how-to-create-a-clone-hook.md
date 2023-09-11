---
title: How to Create a Clone Hook
---
## Introduction

Etendo allows for any window or tab to have a Clone button. By default, it will use the Dal.copy() method, but this can be overridden using hooks, to implement custom Cloning logic for specific entities.

![](/assets/drive/0MigjYdnUWzz7TltzquaKnHZBJkr6dhSt8o-c6WbrEYVqHL8R8SNC3lvoTFs-_XOI1qhnCopBhqqzL1THLQ61n4sYhGsRGyT-BtGPes-kykNZO79OUtW55PAmcjxNOA-i9gEK2uaDivHwfJTUdYykeDqL5-qk0UzbVmuGJIpaVufYYmX02sjk3fr.png)

## How to create a Clone Hook?

To create a Clone Hook, you only have to follow a few steps:

1. Create a Java Class of type CloneRecordHook
2. Use the @Qualifier annotation to define which entity this class will clone
3. Override the required methods and implement their logic according to your needs
4. Enable the clone button inside the tab associated with the Entity used in the hook ExampleCloningHook.java

```java
@ApplicationScoped

@Qualifier(Invoice.ENTITY_NAME)

public class ExampleCloningHook extends CloneRecordHook {

  @Override
  public boolean shouldCopyChildren(boolean uiCopyChildren) {
    //Implementation
  }

  @Override
  public BaseOBObject preCopy(BaseOBObject originalRecord) {
  	//Implementation
  }

  @Override
  public BaseOBObject postCopy(BaseOBObject originalRecord, BaseOBObject newRecord) {
    //Implementation
  }
}

```

## Clone Hook API

To create a Clone Hook, you only have to follow a few steps:

1. ### `boolean shouldCopyChildren(boolean uiCopyChildren)`

    This method will return a boolean indicating if the Hook will use the DalUtil.copy() to copy the children entities.
    For example, cloning an Invoice and its children will mean that Lines, Taxes, etc. are also cloned into the new document.

2. ### `BaseOBObject preCopy(BaseOBObject originalRecord)`

    This method must return the original object, which is the parameter received.
    Here you can make special validations or extra logic involving the original record, before it is cloned.

3. ### `BaseOBObject postCopy(BaseOBObject originalRecord, BaseOBObject newRecord)`

    Here you have access to the newly created record, a result of the DalUtil.copy().
    This method is where you should implement special logic after the record is cloned.
    For example, if the method shouldCopyChildren returns false, then here you would copy the children with all special considerations needed.

4. ### `BaseOBObject copy(BaseOBObject bob, boolean copyChildren)`

    Optional: Only override this method when the existing functionality is not enough, here you must implement the cloning functionality manually and call postCopy()on your own.

5. ### `boolean shouldResetId()`

    Override this method when you don’t want the DalUtil.copy()to reset the copied objects IDs. Refer to the DalUtil.copy() documentation for more information. This method returns true by default.

6. ### `int getPriority()`

    Override this method when there is an existing hook for your selected Entity (for example, there is a cloning process already implemented for Invoices and Orders), and you want your own hook to be used instead.
    The hook with the lowest priority per Entity will be selected and executed. It returns 100 by default.