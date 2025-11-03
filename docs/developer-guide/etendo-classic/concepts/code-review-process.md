---
title: Code Review Process
tags:
  - Code Review
  - Process
  - Properties
  - Application Dictionary

status: beta
---

# Code Review Process

!!! example  "IMPORTANT: THIS IS A BETA VERSION"
    It is under active development and may contain **unstable or incomplete features**. Use it **at your own risk**. The module behavior may change without notice. Do not use it in production environments.

##  Overview

This document gives a description of the Etendo code review process and the code review checklist.

The general opinion is that code reviewing is very helpful in finding and preventing bugs and in transferring knowledge between development team members. On the other hand traditional (Fagan-like) code reviews are very time consuming and resource intensive. In addition, standard Fagan like code reviews fit less to more agile-like development methods and current development environments with instant compiling and code formatting tools. The result is that it is difficult, in practice, to organize and implement code reviewing processes in the dynamic and time-pressed environment of a development project.

The Etendo code review process tries to combine the advantages of code reviewing with a process that is lightweight and easy to organize and control. The process is very much focused on the code itself and uses the features of development environments and code checking tools. Using code checking tools means that code reviewing can be focused on code quality and correctness instead of code standard conformity.

Before going into further detail, it is good to define the goals which we want to achieve with code reviewing. There are two main goals:

* Improve the quality of the code: 
    * Ensure correctness (functionally) 
    * Minimize the number of bugs 
    * Prevent intellectual property rights problems 
    * Ensure that the code conforms to agreed coding standards 

* Let developers share knowledge, learn from each other and improve the understanding of each others' code. 

The Etendo code review process should be supported by a toolset. Instead of making an upfront choice for a tool, the envisioned process is described. The next step is to determine if an existing tool can be chosen or that a code reviewing tool can be created by customizing current development tools (svn, mantis, eclipse).

But before describing the code review process, lets first emphasize the role of the developer in the software development process. Because high quality code starts and ends with the personal approach and drive of each developer.

##  Code Review Goal

The goal of code review is to exchange knowledge, increase capabilities and support developers in making automatic choices for standard structures. This allows the developer to spend time and effort to the things which are important: create code that runs, code that is readable, elegant, easy to read, easy to adapt, efficient and understandable.

##  Etendo Code Review Process: Personal, Peer review and Team review

The Etendo code review process consists of three types of reviews:

1. Personal,
2. Peer and
3. Team reviews.

###  Personal Review

The developer should automatically follow coding conventions and other good coding practices. To validate this each developer should actively review his own work. The development system should support the developer in performing this task.

The following process is proposed:

* Each developer automatically gets an email with the commits of the day before. 
* The email contains the full list of files committed in the previous day. Only files which have been sent to be reviewed should be part of this email. 
* Each file has a hyperlink which opens a web page showing the diff of the commit. The webpage also shows attention points for the developer to look at: 
    * Is the change correct? 
    * Does the change follow the coding conventions? 
* The developer does not need to fill in a checklist, the personal review should be very lightweight as it is done frequently (daily) 
* The code reviewing system registers which files have been sent to each developer and registers which files have been opened by the developer to be reviewed. 

The personal review should not be done on the same day as the code was written. A longer time between the commit and the personal review will result in a fresher look on the changes made the person himself.

###  Peer Review

The peer review is the most important review as it operates on two goals: issue prevention and knowledge transfer (from the reviewer to the reviewee).

An important question is who is the peer, who will review the code. In the Etendo code review process the peer reviewer is the team lead of the scrum team.

The advantage of the team lead peer is that he understands the functionality the team is working on. He can therefore judge if changes are correct in respect to the functionality the team is working on. In addition, the team lead has direct contact with team members. Also code reviewing is more part of the standard team activities and can be planned. As the team lead is an experienced developer, code reviewing results in knowledge transfer from the team lead to less experienced team members.

The team lead peer approach has as disadvantage that the team lead might get overloaded with review activities. Another disadvantage of a team lead peer is that he might feel less ownership for overall source files and can possibly not determine if code changes interfere with other (unchanged) parts of the code.

The commits by the team leads themselves should also be reviewed. Therefore each team lead also has a personal reviewer assigned to him.

The peer review process consists of the following steps:

* A developer commits one or more files to subversion. 
* A review is triggered (through the commit) and an email is send to the reviewer. The email contains the following information: 
    * The description of the commit message and the committer name and email address 
    * The list of files changed and the amount of lines changed per file 
    * If the commit was for one or more Mantis issues then the hyperlinks to these issues are also present in the email 
    * A hyperlink to start the review process 
* The reviewer clicks on this hyperlink and is taken to the a webpage. The webpage shows: 
    * The commit message, committer name and email address. 
    * If the commit is a bugfix: a hyperlink to the Mantis bug(s) of the solution 
    * The list of files changed with for each file a hyperlink to the diff and checklist page (see below). 
* The reviewer clicks for each file on the diff/checklist page. He is taken to a next page which shows the commit info in the header and the following information: 
    * The diff 
    * List of commits done on the file since the commit triggering this review, hyperlinks to the diffs of these other commits. 
    * Hyperlink to the full current version of the file 
    * The checklist applicable for that file, the reviewer has to check each point on the checklist 
    * A reject button: if the reviewer clicks this button then the committer needs to rework the file. The reviewer must enter a remark when rejecting a file. 
    * An approve button 
* The reviewer fills in the checklist or enters a comment and clicks on reject. The committer is notified that he should change/update the file. If the file is approved then no mails are send. 
* When the last file has been accepted or rejected then the review task is finished. 

!!!note
    All peer reviews should have been done before a branch can be merged with trunk. ?

###  Team Review

Each scrum team should spend at least 45 minutes a week ? on a team review. In the team review one (part of) a file is discussed with the complete team together. The main purpose of the team review is to share knowledge about code and coding practices. The to-be-reviewed file is proposed by the team lead.
The team lead informs the rest of the team which file will be discussed and each team member spends 15 minutes for doing a personal review of the file.

In the team review meeting, the author of the file presents the code and gives a walkthrough. The review meeting should be an exchange of ideas and discussion of implementation strategies. The goal is to share ideas and knowledge and not so much to find bugs or non-conformance to standards.

##  What to Review

The following files are reviewed:

* Java files. 
* Properties templates files. 
* Properties files and XML files in the `src` folder. 
* The content of the Application Dictionary tables (the AD_TABLE.xml etc.). 
* The content of the functions, triggers and views XML files. 

Only committed changes are reviewed. This means that everyone is free to commit without pre-review. This is as it is now. The commit is the trigger of the review.

However not all commits need to be reviewed. The following rules apply. Every commit is reviewed, except:

* A commit with only a limited number of changes per file is not reviewed. For example less then 5 characters (to correct a typo) 
* A commit with only comment changes is not reviewed. 
* A commit with a specific comment which prevents reviews: *No review required*. This makes it possible for a committer to signal that a certain commit really does not need a review. Per committer, the number of commits with this remark is checked in the statistics (see below). 

Different types of files will require different types of review checklist. The proposal is to have different checklists for different files:

* A short Java checklist for small changes (less than five lines of code). 
* A full Java checklist for all other Java changes. 
* A checklist for properties/properties.templates file. 
* A checklist for application dictionary tables. 
* A checklist functions, triggers and views XML file. 

The checklists are discussed below in more detail.

##  Review Statistics

For management purposes, the code review system should register and display the following information:

* Total closed, open, declined reviews. 
* Per reviewer: closed, open, declined reviews. 
* Per reviewer: number of committed files, number of files personally reviewed. 
* Per committer: closed, open, declined reviews, number of commits explicitly set to "No review required". 
* The top 100 files which have not been reviewed, the top 100 most reviewed files. 

##  Code Review Tools

There are different tools available which can be used and adapted for the flow described above. If the decision is made to use an external tool then a proof-of-concept needs to be planned to try one out.

A choice can also be to implement and support the above flow with a custom developed web application integrated with svn and Mantis. Mantis can be used as the registration of review tasks and results. For example a Mantis bug can be used to start a review task. A rejected review can create a Mantis issue
assigned to the committer. The result of a review can be attached to the Mantis issue.

The advantage of developing our own toolset is that it prevents yet-another-tool in the development and systems management environment.

##  Automated Reviews and Bug identification

The manual review process is supported with the following tools which perform automatic code reviewing:

* Eclipse compilers and warnings settings: the standard Etendo settings should be used
* FindBug 
* CheckStyle 
* PMD

##  Checklist

There are different checklists for different situations. Each checklist is short to be effective, referring to external documents for more information.

###  Short Checklist (Java)

* Do you understand what changes have been made and why they have been made? 
* Do the changes correctly implement the required functionality? 
* Does the code adhere to the [coding conventions](../concepts/java-coding-conventions.md)? 

###  Full Checklist (Java)

* Do you understand what changes have been made and why they have been made? 
* Do the changes correctly implement the required functionality? 
* Does the change interfere with other code/functionality? 
* Does the code adhere to the [coding conventions](../concepts/java-coding-conventions.md)? 
    * Check for these topics: copyright statement, documentation, exception handling, Java 1.5 constructs, don'ts 
* Is the code readable and understandable, i.e. skimmable? 
* Has the code been formatted according to the agreed coding format? 
* Has the developer used defensive coding practices? 
* Does Eclipse show any warnings in the code? 
* Intellectual Property: 
    * Does the commit contain a new external Library? If so has the legal advisor checked the license? 
    * Does the commit contain third-party code? Is so, has the third-party contributor signed a contributor agreement and has it been deposited with the Etendo Finance Department? 

###  Properties Files

* Does the change interfere with other parts of the properties file? 
* Are new properties documented, has the change been communicated to other developers? 

###  Application Dictionary Checklist

* Is the naming of tables and columns correct, in English? 
* The javapackage of the table is set correctly? 
* Have the correct types been chosen? Have foreign keys been set? 

##  Links

* http://www.review-board.org/ 
* http://www.developer.com/tech/article.php/3579756 
* http://www.methodsandtools.com/archive/archive.php?id=66 

##  Peer Types

The main review activities are done as part of peer review. An important question is therefore who is the peer who will review the code.

###  Owner

The Owner Peer approach means that the source code of Etendo is divided in different parts and each part is assigned to one owner of that code. The owner of each part is responsible for reviewing the changes to the code made by other developers.

The owner should be someone with experience and an eye for code quality. He should have full understanding of the coding conventions. In addition, the owner should understand the functionality implemented by his part of code. He should feel responsible for his code.

The owner peer approach has as advantage that the reviews are done by a person knowing the overall code (of his assigned part). He can detect when code changes conflict with the broader meaning of the code. Also because the owner peer is an experienced developer he can be more effective in sharing his knowledge with less experienced developers whose code changes are being reviewed.

The main disadvantage of an owner peer approach is that the owner peer is not involved in every project/scrum team that makes changes to his part. Therefore it can be more difficult to understand/follow the reason why code changes are made.

###  Team Lead

The team lead can also act as the peer. The advantage of the team lead peer is that he understands the functionality the team is working on. He can therefore judge if changes are correct in respect to the functionality the team is working on. In addition the team lead has direct contact with team members.
Also code reviewing is more part of the standard team activities and can be planned. As the team lead is an experienced developer, code reviewing results in knowledge transfer from the team lead to less experienced team members.

The team lead peer approach has as disadvantage that he might get overloaded with review activities. Another disadvantage of a team lead peer is that he might feel less ownership for overall source files and can possibly not determine if code changes interfere with other (unchanged) parts of the code.

###  Team Member

In this approach the work of a member of a team is reviewed by another member of that team. The advantage of this approach is that team members exchange knowledge and that team members together grow in their experience and knowledge level. Doing code reviews can help to more quickly develop developers skills. Another advantage is that the review work is divided.

The disadvantage is that also inexperienced developers will do reviews which will probably result in less effective reviews.

###  Second Reviewer

Also the work of a peer reviewer should be reviewed. Therefore every peer (team lead or owner) should have a second peer assigned to him.

---

This work is a derivative of [Code Review Process](http://wiki.openbravo.com/wiki/Code_Review_Process){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}. 