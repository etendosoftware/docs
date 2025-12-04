---
title: How To Log
tags:
    - log
    - howto
    - level
    - context

status: beta
---

#  How To Log

!!! example "IMPORTANT: THIS IS A BETA VERSION"
    This page is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**.
  
##  Overview

This section provides some guidelines on what and how to log.

Etendo generates a log file which serves different purposes:

* Notify about functional errors such as misconfiguration, incorrect flow execution, etc. 
* Alert about unexpected errors which are usually due to problems in the code. 
* In case of problems, help to debug and understand their root causes. 


It is intended to be consumed by technical staff such as system administrators, developers, support team, etc.

To learn how to configure logs, read [this document](../how-to-guides/how-to-configure-log.md) .

##  How to log

!!!warning
    Standard output `System.out`, `System.err` or `printStackTrace` **should never be used** .

They write log in a different file `catalina.out`, which has several inconvenients:

* Having a single source of logs makes much easier to look for problems. 
* ` catalina.out ` is not automatically rotated, so its size might increase without limit. 
* Important information is not automatically included: it does not include timestamp nor class generating the log.
  
  
Etendo includes log4j2 as logging framework, so all logs should be written making use of it. ???

The following snippet shows how to write a warning line in log:
 
```
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
 
private class Example {
// gets logger for this class
private static final Logger log = LogManager.getLogger();
 
private void process(Invoice invoice) {
    // ...
    log.warn("Invoice {} could not be processed because config XXX is missing", invoice.getId());
}
}
```

###  Dissecting a Line of Log

The log produced by any of the two previous snippets will look like follows (assuming this code is executed in Tomcat with the default config. Test and build configurations may have slight differences in format):

```
2018-11-14 13:37:08,377 [http-nio-8080-exec-4] WARN org.openbravo.example.Example - Invoice AAA could not be processed because config XXX is missing
----------------------- ---------------------- ---- -----------------------------   ----------------------------------------------------------------
            |                       |              |              |                                         |-> Actual message
            |                       |              |              |-> Java class producing the message
            |                       |              |-> Message level
            |                       |-> Thread name
            |-> Timestamp when the log was generated
```

##  What to Log

Logs are a very important part of the application, as such, it is key to carefully think what is the relevant information to be logged. Note that, usually, logs are going to be read time after they are created, so they should contain whatever it is needed to reproduce problems in future.

###  Level

Logging can be written at different levels. When a logging level is enabled, all messages written at that level or at any higher one will be saved in the log file. By default, `INFO` and higher levels are written skipping lower levels. This can be modified permanently or at runtime to a different level
for every logger or for specific ones.

The available levels, ordered from higher to lowest priority are:

* **FATAL**: This level is used for a severe error that will prevent the application from continuing. 
* **ERROR**: this level should be reserved for the cases where immediate action should be taken. Such as unexpected problems that can be caused by bugs in the code, functional severe problems, etc. 
* **WARN**: this category should be used for problems that might require an action, but is not required to be immediate. 
* **INFO**: relevant information that helps to understand system use when everything worked as expected. 
* **DEBUG**: in case of problematic areas, messages at this level should provide information to developers to reproduce the problem and understand where it comes from. 
* **TRACE**: similar to DEBUG, to be used to complement previous level with a much more fine grained information. 

###  Context

As log should provide enough information to know what is going on, it is of paramount importance to include relevant context to every line of log. This context, will depend on what the code is doing, in general, it should include the relevant parameter values to allow to reproduce the execution.

For example:

```
// DO NOT do this!
log.warn("Could not process invoice.");
```

this code warns about an invoice that could not be processed, but it does not provide any information about which invoice and why it failed.

The following would be slightly better:

```
log.warn("Invoice {} could not be processed", invoice.getId());
```

because it indicates the invoice that failed, so it would help to try to reproduce the problem. Depending on the process itself, it might also require to include some other parameters, for example:

```
log.warn("Invoice {} could not be processed with action: {}", invoice.getId(), action);
```

####  Caveats

Logging can create performance overhead, be careful when selecting what to log at each level. For example, if you only have a Business Partner ID, it may be preferable to only log it than its name if it is necessary to retrieve it from database.

Be careful when logging context not to create new exceptions. For example, the following log line could throw a `NullPointerException` in case `invoice` variable is `null` when it is executed: `log.debug("Processing invoice", **invoice** .getId());`

!!!note
    For performance reasons, log4j avoids using varargs for log calls with up to 10 placeholder values. Using more than 10 parameters, the varargs version of the call will be used.

###  Stack traces

Stack traces show the call stack of a thread in the moment they were generated, this is, recursively the line of code that was in execution as well as the line that invoked current method, the line that invoked that method and so on.

Sometimes, they can give a great context to developers to find causes of problems.

The following code will log an error message and the stack trace of that thread when it occurred:

```
try {
// ...
} catch (MyException e) {
log.error("could not process invoice " + invoice.getId(), e);
// handle error here: just logging won't fix it
}
```

!!!note
    The following code **will not** include any stack trace:

    ```
    } catch (MyException e) {
    log.error(e); // no stack trace!!
    }
    ```
    as it is equivalent to:

    ```
    } catch (MyException e) {
    log.error(e.getMessage());  // no stack trace!!
    }  
    ```
  
Although they can be useful in some occasions, they also tend to be very verbose. Log files with too many stack traces are usually difficult to read. So, as any other context information, it is required to carefully select whether to include them or not. As a basic guideline:

**Include them** for:

* Technical unexpected errors (ie. `NullPointerException`). 
* Errors detected in APIs that can be consumed from many different places. This will help to understand where they were invoked from. 

But **do not include** them for:

* Validations. 
* Functional errors. 
* Expected and handled errors. 
* Cases where it does not provide valuable information, for example if there is only a possible invocation flow for that code. 

####  OBException

`OBException` is an unchecked exception. Before  3.0PR17Q4 ???  when a new instance was created, it was logged by default including stack trace. It is possible to change this behavior using overloaded constructors:
 
```
// Pre 3.0PR17Q4 ???
throw new OBException("Something failed"); // logs exception with stack trace

throw new OBException("Something failed", false); // does not log anything
```
  
Since 3.0PR17Q4, default behavior has changed not to log by default. ???

```
// Post 3.0PR17Q4
throw new OBException("Something failed"); // does not log anything

throw new OBException("Something failed", true); // logs exception with stack trace
```

It is possible, though, to automatically generate log whenever a new `OBException` instance is created by setting `org.openbravo.base.exception.OBException` logger at `DEBUG` level.

---

This work is a derivative of [How To Log](http://wiki.openbravo.com/wiki/How_To_Log){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
