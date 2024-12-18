---
tags:
    - Copilot
    - IA
    - Machine Learning
---

# How to execute Copilot through the console

## Overview

This article explains how to execute Copilot through the console. This is useful when you want to test a tool or assistant without using the Etendo Classic interface.

## Prerequisites
* Been able to access to the Etendo Classic host.

## Command
```bash
./gradlew copilot.do -Phost='https://my.etendo.instance/etendo' -Papp_id="Module Creator" -Pusername=my-user -Ppassword=my-password -Pquestion="Can you create a Module called 'Test Module? "  --console=plain 
```

## Parameters
* **host**: The URL of the Etendo Classic host. If not provided, the default host http://localhost:8080/etendo will be used.
* **username**: The username of the user who will execute the command. This user must have the necessary permissions to execute the command.
* **password**: The password of the user who will execute the command. 
* **role**: The role of the user who will execute the command. If not provided, the default role will be used.
* **app_id**: The ID of the application where the assistant is located. It can be the **exact** name of the assistant or the **ID** of the assistant.
* **question**: The question you want to ask the assistant.

* **--console=plain**: This parameter is used to avoid the Gradle console from showing the progress bar.

!!! note
    These parametes (except ```--console=plain```) need to be used with starting with `-P` and separated by spaces.

!!! warning
    The parameters ```username``` and ```password``` are mandatory. If not provided, the script will ask for them. This is to avoid storing sensitive information in the command history.