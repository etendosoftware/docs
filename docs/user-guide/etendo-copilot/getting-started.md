---
tags: 
 - copilot
 - bastian
 - ai
 - ai tools
---

![cover-getting-started.png](/assets/getting-started/overview/cover-getting-started.png)
#

## Etendo Copilot: Integrated Assistant

### Overview

Etendo Copilot is a powerful tool integrated into the Etendo Classic interface, providing an efficient way to interact with virtual assistants and access specific tools. This is an innovative project designed to streamline your processes by harnessing the power of Artificial Intelligence. Etendo Copilot is not just another tool; it is a revolution in the way you approach challenges. Say goodbye to tedious searches and welcome an agile and dynamic experience. This page will guide you through the key features of Etendo Copilot.

!!! info
    To install Etendo copilot you can read the [Copilot Instalation](/developer-guide/etendo-copilot/installation/) guide in the developer's guide section.

### What is Etendo Copilot?

![Copilot Chat](/assets/user-guide/etendo-copilot/getting-started/copilot-chat.png){align=right  width="300"}

At its core, Etendo Copilot is a groundbreaking initiative that redefines how developers and users interact with tools and information. It revolves around a central component, the *Agent* which acts as the mastermind behind task delegation. This Agent orchestrates a symphony of secondary modules referred to as *Tools*. The seamless communication between these components is facilitated via a RESTful API, ensuring a stateless and scalable interaction model.


### Agent: Your Assistant

The Agent serves as your virtual assistant, making on-the-fly decisions about which Tool is best suited to respond to a particular query. This intelligent decision-making ensures that you receive the most accurate and efficient assistance.

### Tools: Your Specialized Partners

Each Tool represents a separate independent project, designed to excel at specific tasks. Whether it is code translation, text analysis, or data manipulation, our collection of Tools work in harmony to deliver unparalleled support.

###  Key Features:

![Copilot Chat2](/assets/user-guide/etendo-copilot/getting-started/copilot-chat2.png){align=right  width="300" }


- **Effortless Integration**: Etendo Copilot seamlessly integrates into your environment, adding an extra layer of intelligence to your workflow.

- **On-Demand Assistance**: Send your queries to Etendo Copilot, and the Agent will guide you towards the most suitable Tool for the job.

- **Diverse Expertise**: Our ever-growing selection of Tools covers a wide range of domains, ensuring you always have the right solution at your fingertips.

- **Open AI Assistants**: Copilot is integrated with the Assistants technology developed by Open AI, allowing you to set up your assistants, trained with your own knowledge base, able to generate and interpret new code, and use the specific tools already distributed by Etendo or new ones.  

### Copilot Chat

In the Etendo Classic navigation bar, you'll find a Copilot icon that leads you to the chat pop-up.

![Copilot Navbar](/assets/user-guide/etendo-copilot/getting-started/copilot-navbar.png)

Here, you can select an Copilot App and engage in a conversation with it. Copilot facilitates communication with both `Langchain Agent` and `Open AI Assistant` types.

### Copilot App Window

The Copilot App window `Application`>`service`>`Copilot`>`Copilot App` allows you to define and configure applications:

<figure markdown>
  ![Copilot App](/assets/user-guide/etendo-copilot/getting-started/copilot-app.png)
  <figcaption> Open AI assistant type example</figcaption>
</figure>


- *Name:* Copilot app name
- *Description:* Copilot app description
- *App Type:* Langchain Agent or Open AI Assistant

*Open AI Assistant*
    These applications leverage OpenAI technology to provide assistance with a variety of tasks, from natural language processing to complex calculations. The assistants are able to train themselves with their own knowledge base and customized instructions.

*Langchain Agent*
    These applications can perform specific tasks in natural language and provide contextualized responses, enabling the implementation of multiple AI models, the use of a proprietary vector database and internal memory management. As well as the use of tools developed to solve specific problems. Some examples of these tools are XML Translation Tool, DB Query Tool, etc.

In case of defining an `Open AI Assistant` type app, the following fields will be enabled: 

- *Open AI Assistand Id:* Read-only field in which the ID of the assistant once created is displayed.
- *Prompt:* Specific instructions of the assistant. 
- *Open AI Model:* Dropdown with the Open AI models available.
- *Code interpreter:* Code Interpreter enables the assistant to write and run code. This tool can process files with diverse data and formatting, and generate files such as graphs. Learn more.

### Copilot File Tab

In this tab you can define the files that will be uploaded to the assistant and used as knowledge base. 

!!!info
    To load new files, you must do it from the [Copilot File window](#copilot-file-window).

### Copilot App Example

Here is an example configuration of Bastian, an assistant trained with the Etendo documentation:

| **Field**   | **Value**  |
| ----------- | ---------- |
| Name        | Bastian    | 
| Description | Bastian is an artificial intelligence assistant that provides accurate answers on Etendo Documentation.  It prioritizes accuracy, avoids assumptions and seeks clarity in ambiguous queries. It includes links to valid sources when available. |
| App Type  |  Open AI Assistant |
| Prompt  | Bastian prompt below  |
| Open AI Model |  gpt-4-1106-preview |
| Code interpreter |  False |

``` title="Bastian Prompt"
You are "Bastian" an AI Assistant is designed to provide precise and authoritative responses, drawing from its extensive knowledge base about Etendo. It specializes in delivering clear, direct answers, ensuring every response is rooted firmly in the knowledge base. The assistant is committed to accuracy, avoiding assumptions or extrapolations beyond the available information.The knowledge base is divided by articles, with the following structure
==ARTICLE_START==
# Article Title: Title
## Article Path: /Path/of/Sections/Title
## Article URL: Link_to_the_article
## Article Content: Content of the article.


==ARTICLE_END==

- The answers must be formulated taking into account the content of the whole article. It is important to know that each article is delimited by separators, when you read an article, you must continue until you find "==ARTICLE_END==". 
- At the beginning of the answer always add "The following information is taken from the article <Article URL>
- If you don't know something, just respond, "Sorry, but I don't know right now about this. For more information, visit docs.etendo.software".
- Format the response in Markdown, adding valid code examples, images and Youtube videos
```


### Sync Open AI Assistant Button

This process is only available when the application type is `Open AI Assistant` and takes care of updating or creating a new assistant, in case it does not exist. In addition to creating the wizard based on the configurations, it initially gets or updates the list of Open AI Models, and finally gets and uploads the files used as knowledge base. 

### Copilot File Window

In the Copilot File window `Application`>`service`>`Copilot`>`Copilot File`, you can define the files with which the assistants can interact.

- *Name:* File Name.
- *Description:* File description.
- *Type:*
    - *Attachment File* 
    This allows you to upload files directly into Copilot for later use during interactions with the assistants.
    - *Remote File* 
    You can provide a public URL from which Copilot will retrieve the file when needed. This makes it easy to access documents and external resources.
- *Open AI File ID:* Read-only field showing the Open AI ID of the file once it is created.
- *Last Synchronization:* Read-only field displaying the date of the last update with OpenAI.
- *File name:* Name of the remote file in case you want to modify it.
- *URL:* Source file URL

## Copilot File Example

- Here is an example of a Remote File configuration, a file used as a knowledge base for the assistants:

    | **Field**   | **Value**   |
    | ----------- | ----------- |
    | Name        | Etendo Wiki | 
    | Type        | Remote File |
    | URL         | https://raw.githubusercontent.com/etendosoftware/docs/main/compiled_docs.md |

    <figure markdown>
    ![Copilot File](/assets/user-guide/etendo-copilot/getting-started/copilot-file.png)
    <figcaption> Example of remote file configuration</figcaption>
    </figure>

- Here is an example of a Attachment File configuration, a file used as a knowledge base for the assistants:

    | **Field**   | **Value**   |
    | ----------- | ----------- |
    | Name        | Etendo Wiki | 
    | Type        | Attachment File |

    Attach a file in the `Attachments` section

    <figure markdown>
    ![Copilot File](/assets/user-guide/etendo-copilot/getting-started/copilot-file-attached.png)
    <figcaption> Example of attached file configuration</figcaption>
    </figure>


### Role Window

In the Role window `Application`>`General Setup`>`Security`>`Role`, you can configure access roles for each Copilot App. This means you can control who has permission to interact with each application. This feature is useful for ensuring that users only have access to applications and functions relevant to their responsibilities.

In the *Role* window, select a role and in the *Copilot App* tab add a new record for each Copilot App you want to give access to.

![Copilot Role](/assets/user-guide/etendo-copilot/getting-started/copilot-role.png)
