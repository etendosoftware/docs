---
tags:
  - Copilot
  - AI
  - Tool
  - Test
  - Run Test
  - Test Excecution
  - Gradle
---

# Test Run Tool

:octicons-package-16: Javapackage: `com.etendoerp.copilot.toolpack`

## Overview

The **Test Run Tool** is designed to execute Java tests using Gradle, providing an efficient way to run tests in Java projects within a specific environment.

!!!info
    To include this functionality, the Copilot Extensions Bundle must be installed. For more information, follow the instructions in the marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. For information about available versions, core compatibility, and new features, visit [Copilot Extensions - Release notes](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

## Functionality

This tool is especially useful for running and validating Java test suites. It can be used in various scenarios, such as:

- Running specific tests or groups of tests to ensure functionalities are correctly implemented.
- Integrating automated tests into the development workflow.

The process consists of the following actions:

**Receiving Parameters**

The tool receives the following input parameters:

- `test_targets`: One or more tests or packages to execute.
- `working_directory`: The directory where the `gradlew` script is located.

**Running Tests**

- A Gradle command is constructed and executed with the specified tests.
- The execution is performed in the specified working directory.

**Returning the Result**

Returns a summary of the test execution along with details of passed and failed tests.

## Usage Example

If you want to run specific tests in the `/path/to/erp` directory, the input and output format would be as follows:

- **Input**

```json
{
  "test_targets": ["com.etendoerp.webhookevents.WebhookSetupTest"],
  "working_directory": "/path/to/erp"
}
```

- **Output**

```json
{
  "summary": "Some tests failed. Review the details below.",
  "details": {
    "passed_tests": [
      "Test 1 PASSED>"
    ],
    "failed_tests": [
      "Test 2 FAILED> Reason"
    ]
  },
  "raw_logs": "Complete logs in case of failure"
}
```