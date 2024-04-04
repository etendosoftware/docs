---
tags: 
  - Etendo
  - documentation
  - documentation page
  - style
  - format
---

# How to create a documentation page in Etendo documentation

## Overview
This guide contains basic rules, tips, and suggestions for people intending to develop documentation for Etendo. When different documents use the same guidelines, they are more user friendly, consistent and more simple to combine and reuse. We therefore strongly encourage all contributors to follow these guidelines for the benefit of the readers.


## Requirements
[Python 3](link){target="\_blank"}

## Steps
1. Clone the docs repository 
	
    ```bash title="terminal" 
        git clone git@github.com:etendosoftware/docs.git
    ```

2. Install dependencies

    ```bash title="terminal" 
        python3 -m venv venv
        source venv/bin/activate
        pip install mkdocs-material
        pip install pillow cairosvg
        pip install mkdocs-glightbox
        pip install mike
        pip install mkdocs-rss-plugin
    ```

3. Create a new branch with [gitflow](link){target="\_blank"}, where the related pages, assets and configurations are stored.

    ```bash title="terminal" 
        # This command should be executed only the first time.
        git flow init 
    ```

    ```bash title="terminal" 
        git flow feature start <task key>
    ```
4. Etendo documentation is structured in sections, in general the sections where most of the documentation is found are user guide and developer guide, within these there are subsections according to products and categories, you must decide the location within the structure and create a file with the `.md` format, the name must be camelcase separated by underscores. 

    ``` title="Documentation Structure" 

    └── docs
    ├── developer-guide 
    │   └── ..
    │       └── how-to
    │           ├── ..
    │           ├── ..
    │           ├── ..
    │           └── ..
    ├── user-guide
    │   └── basic-feature
    ```

    In order to display the page in the menu, add this page in the `mkdocs.yml` file in the nav section.

    !!!important
        The directory and navigation structure must be the same.

    The documentation should be worked on following the [style guide](#style-guide) described in the next section.

    Once the documentation is finished:

5. create a PR to develop with all the related changes
6. once all the comments are resolved, and you have two approved, merge the PR
7. a new version of the documentation will be automatically deployed in [https://docs.etendo.software](https://docs.etendo.software){target="\_blank"}.

## Style Guide

### Format

#### Bold, Italics and Paths

- **Bold**. Use sparingly for emphasis, or to highlight file paths or option names, for example:
            From the **File** menu, select **New**.

- *Italic*. Use it when quoting a piece of a text from another source, a piece of text in another language or to give an example, such as sample text to be typed in a text field.

- backticks ` `. Use them for paths both in functional and technical documentation. For menu navigation (for example starting a new document) bold the whole thing and use > to separate the menu items. For example:
            `Document` >`New`> `Template`.

#### Tabs for different platforms
When documenting a feature that varies by platform (Windows or Linux, for example), use the following tabs to include information relevant for each platform. Readers can then choose the corresponding tab with the necessary information.

```bash title="tabs"
=== "Windows"

    ``` c
    #include <stdio.h>

    int main(void) {
      printf("Hello world!\n");
      return 0;
    }
    ```

=== "Linux"

    ``` c++
    #include <iostream>

    int main(void) {
      std::cout << "Hello world!" << std::endl;
      return 0;
    }
    ```
```

=== "Windows"

    ``` c
    #include <stdio.h>

    int main(void) {
      printf("Hello world!\n");
      return 0;
    }
    ```

=== "Linux"

    ``` c++
    #include <iostream>

    int main(void) {
      std::cout << "Hello world!" << std::endl;
      return 0;
    }
    ```


### Writing Rules

#### Keep it simple
Use short sentences and punctuation to keep ideas clear and simple. Introduce a single idea, concept or action per sentence.

- **Wrong**<br>
The manufacturing module allows users to define the process plans, work requirements and work efforts; this is how the processes that produce intermediate and final goods work.

- **Correct**<br>
The manufacturing module allows users to define the process plans, work requirements and work efforts. This section describes how processes that produce intermediate and final goods function.


#### Tenses
Always use the present tense. Avoid past or future tenses if possible.
In addition, try to refrain from using must, have to, need to, will, should and similar forms.
Keep in mind that a manual describes mandatory procedures to follow to accomplish a certain task.

- **Wrong**<br>
You will have to press return to reboot the system.
- **Correct**<br> 
Press return to reboot the system.


#### Use third person
Where possible, use the third person imperative. 

- **Wrong**<br>
You should run the installation script
- **Correct**<br>
Run the installation script

However, as long as you don't overdo it, it is fine to address the user directly using *you* if it makes the documentation easier to follow or use *the user* when necessary.

#### Avoid gender discrimination
Readers of software documentation are men and women. Avoid using expressions that refer to specific gender forms.
You can avoid gender forms or use *they*/*their* as a generic third-person singular pronoun to refer to a person whose gender is unknown or irrelevant to the context of the usage.

- **Wrong**<br>
Every user has his home directory.

- **Correct**<br>
Every user has a home directory.<br>
Every user has their home directory.


#### Only describe current functionality
Avoid talking about future features or plans for a product or an application.

- **Wrong**<br>
Graphics can be saved as a GIF image. Support for new formats will be added in future versions.

- **Correct**<br>
Graphics can be saved as a GIF image.


#### Writing for a global audience
Keep in mind that people from all over the globe can use Etendo and its related documentation.
Some important recommendations:

- Avoid using names of people, addresses, and other sample information that are not common in the English language.
- Remember that currencies and formats to represent dates and numbers are not the same in every part of the world.

#### Other conventions

- If you have a list of items (for example a list of files to be downloaded) order them alphabetically unless there is a more obvious logical order.
- Do not use contractions (don't, you're, etc).

## Page format

### Page structure

```
---
tags: 
  - Tag example 1
  - Tag example 2
---
 
# Title
  
## Overview


(General description of the section)


## Title 1


### Subtitle
```
!!!note
    If the page was extrated from OB wiki, add the following footer editing the title and the link of the original page:
    ```
    ---
    
    This work is a derivative of [Datasets](http://wiki.openbravo.com/wiki/Datasets){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
    ```

### Useful references


- \`code\` -> `code`


- Images -> ![]\(path/to/the/image.png)


- Admonitions -> !!!note


Example:

```
!!!note
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.
```
!!!note
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.


- How to show locations:


```
modules
└── org.openbravo.localization.spain.referencedata.taxes
    └── referencedata 
        └── standard
            ├── Impuestos_ES.xml
            └── Spanish_Tax_Alerts.xml
```


- Links -> \[Google Example](https://google.com){target="_blank"} 


Example:
[Google Example](https://google.com){target="_blank"} 


- Article reference -> \[Article Example](../../how-to-guides/Article_Example)


Example:
[Article Example](../../how-to-guides/Article_Example)


- Italic format -> \*italic* 


Example: *italic*


- Bullet points for lists -> `- Bullet point`


Example:

- Bullet point a
- Bullet point b

!!!info
        For more info about mkdocs, visit [Mkdocs reference](https://squidfunk.github.io/mkdocs-material/reference/admonitions/){target="_blank"}.

---

This work is a derivative of [Documentation Style Guide](https://wiki.openbravo.com/wiki/Documentation_Style_Guide){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.