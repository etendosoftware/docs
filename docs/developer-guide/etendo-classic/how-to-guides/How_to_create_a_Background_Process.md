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

  

#  How to create a Background Process

##  Contents

  * 1  How to create a Background Process 
    * 1.1  Defining a Background Process 
      * 1.1.1  Run Immediately 
      * 1.1.2  Run Later 
      * 1.1.3  Schedule 
    * 1.2  Schedule and Unschedule a Background Process 
    * 1.3  Monitoring executions of Background Processes 

  
---  
  
##  How to create a Background Process

Background Processes are  Processes  that are executed without the direct
action of the user. There can be set different rules to schedule when the
process is executed.

This document discusses about the Openbravo infrastructure for Background
Processes. How to define, schedule and monitorize Background Processes.

###  Defining a Background Process

Background Processes are defined in the window **General Setup || Process
Scheduling || Process Request** . First you select in the field **Process**
the process to execute and in the field **Timing** when it will be executed.

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Background_Process-0.png){: .legacy-image-style}

Depending the **Timing** selected there is needed to define more fields to
define this timing:

####  Run Immediately

This timing option will execute the Background Process only time at the moment
the button to schedule the process is pressed. After it has been scheduled, it
can be rescheduled as many times as needed.

This option is very similar to executing a process from a menu option. The
difference is that when scheduling a _Run Immediately_ Background Process,
there will not be any pop-up that indicates when the execution finished and
instead it will be registered its execution in the **Process Monitor** .

####  Run Later

This option is similar to the previous option. In this case the Background
Process will be executed only one time in one moment in the future.

The moment when the Background Process will be executed is defined in the
fields **Start Date** and **End Date**

####  Schedule

This is the most versatile option that allows to execute a Background Process
periodically. These are the fields used to define the schedule plan of a
Background Process:

  * **Start Date** and **Start Time** : Defines the moment when the schedule plan for this Background Process will start. 
  * **Frequency** : Defines the frequency to execute the Background Process. It can be **Every n seconds** , **Every n minutes** , **Hourly** , **Daily** , **Weekly** , **Monthly** , or **Cron expression** . Depending on the option selected you can define the specific details for each frequency option. 
  * **Finish Date** and **Finish Time** : These fields can be defined only when the option **Finished** is selected. And it defines when to stop the schedule plan for this Background Process. 

###  Schedule and Unschedule a Background Process

After the Background Process has been completely defined it can be scheduled
pressing the button **Schedule Process** . When a process is scheduled, it
will be executed according the **Timing** options selected, and every
execution will be registered in the Process Monitor.

To stop future executions of an Background Process just press the button
**Unschedule Process** . After a Background Process has been unscheduled it
can be scheduled again in any moment pressing the button **Reschedule
Process** .

###  Monitoring executions of Background Processes

All the executions of Background Processes can be monitored in **General Setup
|| Process Scheduling || Process Monitor** .

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_create_a_Background_Process-1.png){: .legacy-image-style}

In this window there is one entry for each Background Process execution and
the information of each execution. The most important fields are:

  * **Process** : The Process executed. 
  * **Start Time** , **End Time** and **Duration** : When the execution started, when finished and the time it took to complete. 
  * **Status** : The final result of the execution of the Process. 
  * **Process Log** : The information logged during the execution of the Process. For example if the **Status** of the execution is _Error_ here in the **Process Log** can be detected the reason of the error. 

Retrieved from "
http://wiki.openbravo.com/wiki/How_to_create_a_Background_Process  "

This page has been accessed 14,179 times. This page was last modified on 12
July 2011, at 17:05. Content is available under  Creative Commons Attribution-
ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**

