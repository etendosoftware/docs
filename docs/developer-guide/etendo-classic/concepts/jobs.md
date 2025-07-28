---
tags:
   - Jobs
   - Actions
   - Concepts
   - Developer
   - Job Result
---

# Jobs

## Overview

This section explains the Job concept that is part of Etendo. It is used both in the Job and the Job Result windows, available under the System Administrator role.

## What is a Job?

A Job is a predefined task or process that runs automatically in Etendo at scheduled intervals or under certain conditions. Jobs are used to automate routine operations such as data updates, report generation, or system maintenance tasks.

## Job Window

:material-menu: `Application` > `Jobs` > `Job`

This window is used to define and configure automated or scheduled background processes that Etendo needs to execute regularly. Here, the user can set up automated tasks such as data imports, financial postings, report generation, or stock updates. To execute one of these defined jobs, the **Run** button is used.

VA

Fields to note:

- **Organization**: Indicates the organization the job belongs to. Jobs can be defined globally or for a specific organization.
- **Active**: A checkbox to enable or disable the job. If unchecked, the job won’t run.
- **Name**: The name or title of the job. It should be descriptive (e.g., "Recalculate Stock Levels").
- **Description**: Optional field to describe what the job does or what its purpose is.
- **Stops on Error**: If checked, the job stops running when an error occurs. Useful for controlling chains of jobs or data integrity.
- **Module**: Optional field. It indicates the module where this job will be exported.

Example:

A job could be set up to automatically:

- Generate financial reports every Friday at 6 PM.
- Sync data from a mobile app every 15 minutes.
- Close old sales orders nightly.

### Lines

These lines break a job into manageable, trackable actions. They allow jobs to be modular and flexible and to integrate with other modules and systems.

VA

Fields to note:

- **Line No**: Defines the order of the execution of the actions.
- **Active**: A checkbox to enable or disable the action.
- **Is a filter**: Marks the line as a filtering step. A filter step prepares or limits the data the job will work with. If checked, it enables the following specific filtering-related fields.
   - **Filter Template**: Selects a predefined filter configuration template, which defines the layout and logic for filtering.
   - **Filter Definition**: The actual definition or logic used for filtering, possibly using criteria like dates, statuses, IDs, etc.


- **Action**: Specifies what the line will do. Common types of actions can be Add payment, Create packing, Post, etc.

    !!! info

        - The available actions may vary depending on the installed modules.
        - For more information, visit [How to Create Jobs and Actions](../how-to-guides/how-to-create-jobs-and-actions.md).


- **Module**: Optional field. It indicates the module where this action will be exported.
- **Parameters**: Optional input values passed to the action. These control how the action behaves.

    !!! info

        These can often be dynamic or use context variables (e.g., ${today}).

### Results

This tab has the same content as the [Job Result Window](#job-result-window).

## Job Result Window

:material-menu: `Application` > `Jobs` > `Job Result`

This window records the execution results of each job defined in the [Job](#job-window) window. A Job Result is the record of a job’s execution, showing when it was run, whether it was successful, and any errors or messages generated. It helps users monitor system activity and troubleshoot issues related to scheduled processes.

VA

Fields to note:

- **Job**: Refers to the job executed.
- **Status**: Shows if the status of the job is `error`, `info`, `pending`, `running`, `success` or `warning`.
- **Message**: Description of the execution, including errors or success messages.

### Kill Job button

This button is used to manually stop a job that is currently running. It allows administrators or users with the right permissions to interrupt or cancel a background process that is taking too long, stuck or frozen, creating system performance issues, or producing unexpected results.

!!! warning
    - The job must be in a "Running" status for the button to work.
    - Killing a job may leave partial changes in the system (e.g., partially processed records).