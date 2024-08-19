---
tags:
    - Copilot
    - IA
    - Etendo Classic
    - API
    - Webhooks
---

# How to Create Tools that Interact with Etendo Classic

## Overview

When creating tools that need to interact with Etendo Classic, the best approach is to use the Etendo Classic Event Webhooks API. This API facilitates authentication through an authentication token and triggers a Webhook, which can receive a dictionary with information as a parameter and perform various actions.

!!!note
    It is recommended to read [How to Create Copilot Tools](../how-to-guides/how-to-create-copilot-tools.md) before continuing with this section.

## Utilizing Etendo Classic Event Webhooks API

The Etendo Classic Event Webhooks API is a standard feature in Etendo, and it allows for easier integration with tools through Copilot utilities. For example, if you need to trigger a WebHook named `UpdateOrderDescription` to update an order in Etendo Classic, receiving a document number and a description as parameters, you can do so by creating a specific tool.

## Example Tool: UpdateSOTool

Here is an example of a tool that triggers the `UpdateOrderDescription` WebHook:

```python

from typing import Type, Dict

from copilot.core.etendo_utils import call_webhook, get_etendo_token, get_etendo_host
from copilot.core.tool_input import ToolInput, ToolField
from copilot.core.tool_wrapper import ToolWrapper, ToolOutput, ToolOutputMessage

class UpdateSOToolInput(ToolInput):
   documentNo: str = ToolField(description="DocumentNo of the Sales Order")
   description: str = ToolField(description="New description to set in the Sales Order")

class UpdateSOTool(ToolWrapper):
   name = "UpdateSOTool"
   description = "Set description in a Sales Order by DocumentNo2"
   args_schema: Type[ToolInput] = UpdateSOToolInput
   return_direct: bool = False

   def run(self, input_params: Dict = None, *args, **kwargs) -> ToolOutput:
       documentNo = input_params['documentNo']
       description = input_params['description']
       token = get_etendo_token()
       # Build the body of the request
       body = {
           "documentNo": documentNo,
           "description": description
       }
       url = get_etendo_host()
       response = call_webhook(url=url, webhook_name="UpdateOrderDescription", access_token=token, body_params=body)
       return ToolOutputMessage(message=response)
```

## Explanation of Tool Components

The above tool leverages utilities provided by Copilot Core:

- `get_etendo_token`: This function returns the authentication token for Etendo Classic, allowing the tool to operate within the user's session. Copilot, acting as a "proxy," manages these sessions.

- `get_etendo_host`: This function returns the URL of the Etendo Classic instance, which is required to trigger the WebHook. This host URL is configured in the gradle.properties configuration file.

- `call_webhook`: This function triggers the WebHook, passing the Etendo Classic URL, the WebHook name, the authentication token, and the parameters needed by the WebHook.

## Conclusion: Simplified WebHook Integration

By using these utilities, you can easily call Etendo Classic WebHooks, leaving only the logic of building the request body and the specific tool's logic itself. This approach streamlines the process of creating tools that interact with Etendo Classic.