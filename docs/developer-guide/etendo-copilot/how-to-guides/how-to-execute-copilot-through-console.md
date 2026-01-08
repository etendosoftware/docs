---
tags:
    - How to
    - Copilot
    - Console
    - Execute Copilot
    - Terminal
---

# How to execute Copilot through the console

## Overview

This article explains how to execute Copilot through the console. This is useful when you want to test a tool or agent without using the Etendo Classic interface.

## Prerequisites
* Access to the Etendo Classic host.

## Command
```bash
./gradlew copilot.do -Phost='https://my.etendo.instance/etendo' -Papp_id="Module Creator" -Pusername=my-user -Ppassword=my-password -Pquestion="Can you create a Module called 'Test Module? "  --console=plain 
```

## Parameters

* **-Phost**: The URL of the Etendo Classic host. If not provided, the default host http://localhost:8080/etendo will be used.
* **-Pusername**: The Etendo Classic username, who will execute the command. This user must have the necessary permissions to execute the command.
* **-Ppassword**: The Etendo Classic password who will execute the command. 
* **-Prole**: The role of the user who will execute the command. If not provided, the default role will be used.
* **-Papp_id**: The ID of the agent to be executed. It can be the **exact** name of the agent or the **ID** of the agent.
* **-Pquestion**: The question you want to ask the agent.

* **--console=plain**: This parameter is used to avoid the Gradle console from showing the progress bar.


!!! warning
    - The parameters ```username``` and ```password``` are mandatory.
    - If not provided, the script will ask for them. This is to avoid storing sensitive information in the command history.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.