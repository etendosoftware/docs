---
tags:
    - Copilot
    - Docker
    - Code Execution
    - Python
    - Bash
---

# Docker Tool

:octicons-package-16: Javapackage: `com.etendoerp.copilot.toolpack`

## Overview

The **DockerTool** is a tool that manages Docker containers to execute Python or Bash code. It allows users to run isolated commands, copy files into containers, and clean up containers automatically after a period of inactivity.

!!!info
    To include this functionality, the Copilot Extensions Bundle must be installed. For instructions, visit the marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. For details about versions, core compatibility, and new features, check [Copilot Extensions - Release notes](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

## Functionality

This tool facilitates **code execution in isolated Docker environments**, supporting workflows for development, automation, and system tasks. The primary functionalities include:

### Parameters

- **Executor**: The type of executor for the code (`python` or `bash`).
- **Code**: The code to be executed inside the container.
- **Files to Copy**: An optional list of file paths to copy into the container for execution.

### Execution Workflow

1. **Container Creation**:
    - A Docker container is created if it doesn't already exist.
    - Containers are named using the format `tempenv-copilot-{conversation_id}` for traceability.

2. **File Transfer**:
    - Files specified in the `Files to Copy` parameter are uploaded to the container at the specified paths.

3. **Command Execution**:
    - The tool runs the specified Python or Bash code.
    - The output is captured and returned to the user.

4. **Container Cleanup**:
    - Containers are automatically deleted after 1 hour of inactivity.

### Example Input

```json
{
    "executor": "bash",
    "code": "ping -c 4 google.com",
    "files_to_copy": []
}
```

### Example Output

```json
{
    "message": "PING google.com (172.217.12.206): 56 data bytes\n64 bytes from 172.217.12.206: icmp_seq=0 ttl=115 time=12.5 ms\n64 bytes from 172.217.12.206: icmp_seq=1 ttl=115 time=12.3 ms\n64 bytes from 172.217.12.206: icmp_seq=2 ttl=115 time=12.4 ms\n64 bytes from 172.217.12.206: icmp_seq=3 ttl=115 time=12.6 ms\n\n--- google.com ping statistics ---\n4 packets transmitted, 4 packets received, 0.0% packet loss\nround-trip min/avg/max/stddev = 12.3/12.5/12.6/0.1 ms"
}
```

!!!info
    This tool uses the official **Python 3.10-slim** Docker image for execution and can execute both Python and Bash commands.

## Usage Example: Make a Ping to Google

To demonstrate the **DockerTool**, let's run a `ping` command to check connectivity to Google.

1. **Input**:

    ```json
    {
        "executor": "bash",
        "code": "ping -c 4 google.com",
        "files_to_copy": []
    }
    ```

2. **Output**:

    ```json
    {
        "message": "PING google.com (172.217.12.206): 56 data bytes\n64 bytes from 172.217.12.206: icmp_seq=0 ttl=115 time=12.5 ms\n64 bytes from 172.217.12.206: icmp_seq=1 ttl=115 time=12.3 ms\n64 bytes from 172.217.12.206: icmp_seq=2 ttl=115 time=12.4 ms\n64 bytes from 172.217.12.206: icmp_seq=3 ttl=115 time=12.6 ms\n\n--- google.com ping statistics ---\n4 packets transmitted, 4 packets received, 0.0% packet loss\nround-trip min/avg/max/stddev = 12.3/12.5/12.6/0.1 ms"
    }
    ```