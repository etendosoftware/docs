---
title: Async processes
---

## Async process in Etendo RX

> Asynchronous processing provides a means of distributing the processing that is required by an application between systems in an intercommunication environment. Unlike distributed transaction processing, however, the processing is asynchronous.
> In asynchronous processing, the processing is independent of the sessions on which requests are sent and replies are received. No direct correlation can be made between a request and a reply, and no assumptions can be made about the timing of the reply

Etendo RX allows the development of asynchronous processes in a simplified way. When an internal or external process needs to execute a process it queues it with a POST call to the corresponding endpoint with all the data needed to execute it. First, the service returns a uuid (a random char with a length of 32) if the process is accepted for execution. This first response is for reference only, its execution is not yet confirmed.
Internally it starts the flow needed for this specific task. To know how it’s going and the result, you need to make a GET call to the endpoint of async process including the reference uuid.

| ![01-async-deployment-diagram.svg](/legacy/etendorx/01-async-deployment-diagram.svg) |
| :-------------------------------------------------------------------------------------------------------: |
|                                              <b>Image 1</b>                                               |

| ![00-async-process.svg](/legacy/etendorx/00-async-process.svg) |
| :---------------------------------------------------------------------------------: |
|                                   <b>Image 2</b>                                    |

### asyncprocess module

This module has the following endpoints:

#### POST /async-process/?process={{process name}}

`process name`: The name of the process to start

This endpoint allows you to start the execution of a process that will be executed later.

> This service requires authentication, for more information follow the guide below: [EtendoRX Auth module](/legacy/technical-documentation/etendo-environment/platform/rx-auth)

```
POST /async-process/?process={{process name}} HTTP/1.1
Host: localhost:8099
X-TOKEN: {{token}}
Content-Type: application/json
Content-Length: 2291

{
/// Data needed to execute the process
}

```

Once called the response will be

```
{
   "id": "{{process id}}"
}
```

`process id`: uuid for the process. Is required as reference, to know process status.

#### GET /async-process/{{process id}}

`process id`: uuid for the process.
