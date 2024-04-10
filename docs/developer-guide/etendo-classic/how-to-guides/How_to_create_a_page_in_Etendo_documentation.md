---
tags: 
  - Etendo
  - documentation
  - documentation page
  - style
  - format
---

# How to create a page in Etendo documentation

## Overview
This guide contains basic rules, tips, and suggestions for people intending to develop documentation for Etendo. When different documents use the same guidelines, they are more user friendly, consistent and more simple to combine and reuse. We therefore strongly encourage all contributors to follow these guidelines for the benefit of the readers.


## Requirements
- Python version ^3.10. To install it, follow [The Official Installation Guide](https://www.python.org/downloads/){target="\_blank"}.


## Steps

1. Clone the docs repository 
	
    ```bash title="Terminal" 
        git clone git@github.com:etendosoftware/docs.git
    ```

2. Install dependencies

    ```bash title="Terminal" 
        python3 -m venv venv
        source venv/bin/activate
        pip install mkdocs-material
        pip install pillow cairosvg
        pip install mkdocs-glightbox
        pip install mike
        pip install mkdocs-rss-plugin
    ```

3. Create a new branch with [gitflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow){target="\_blank"}, where the related pages, assets and configurations are stored.

    ```bash title="Terminal" 
	# This command should be executed only the first time after cloning the repository.
	git flow init 
    ```

    ```bash title="Terminal" 
    git flow feature start <task key>
    ```

4. To run the Etendo documentation locally, execute:

    ```bash title="Terminal"
    source venv/bin/activate
    mkdocs serve
    ```

5. Etendo documentation is structured in sections, in general the sections where most of the documentation is found are user guide and developer guide, within these there are subsections according to products and categories, you must decide the location within the structure and create a file with the `.md` format, the name must be camelcase separated by underscores. 

    ``` title="Documentation Structure" 
    └── docs
    ├── developer-guide 
    │   └── ..
    │       └── how-to
    │           ├── New-Page.md
    │           ├── ..
    │           ├── ..
    │           └── ..
    ├── user-guide
    │   └── basic-feature
    ```

    In order to display the page in the menu, add this page in the `mkdocs.yml` file in the nav section.
    
    !!!important
        - When adding pages to the navigation structure, remember to organize them in alphabetical order.
        - The directory and navigation structure must be the same.


    The documentation should be worked on following the [style guide](#style-guide) described in the next section.

    Once the documentation is finished:


6. Create a PR to develop with all the related changes.
7. Once all the comments are resolved, and you have two approved, merge the PR.
8. A new version of the documentation will be automatically deployed in [https://docs.etendo.software](https://docs.etendo.software){target="\_blank"}.

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
    If the page was extracted from OB wiki, add the following footer editing the title and the link of the original page:
    ```
    ---
    
    This work is a derivative of [Datasets](http://wiki.openbravo.com/wiki/Datasets){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
    ```

### Useful references

#### Code
- \`code\` -> `code`

#### Images path format
- Images -> ![]\(path/to/the/image.png)

For more information about how to add images to pages, read the [Images](#images) section

#### Admonitions
- Admonitions have the following syntax: !!! to start the block, a single keyword used according to the type of admonition. After four spaces, the content of the block is added.

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


#### Locations:
In order to show locations, it is important to apply the following format:

```
modules
└── org.openbravo.localization.spain.referencedata.taxes
    └── referencedata 
        └── standard
            ├── Impuestos_ES.xml
            └── Spanish_Tax_Alerts.xml
```


#### Links
- Links -> \[Google Example](https://google.com){target="_blank"} 


Example:
[Google Example](https://google.com){target="_blank"} 

#### Article Reference
- Article reference -> \[Article Example](../../how-to-guides/Article_Example)


Example:
[Article Example](../../how-to-guides/Article_Example)

???? 
- Italic format -> \*italic* 


Example: *italic*

#### Lists
- Bullet points for lists -> `- Bullet point`


Example:

- Bullet point a
- Bullet point b

!!!info
    For more info about mkdocs, visit [Mkdocs reference](https://squidfunk.github.io/mkdocs-material/reference/admonitions/){target="_blank"}.

### Images

In order to add images to the page, remember to upload the image to the **assets** folder with the corresponding specific location.

For example, if the image location is `Documentation`>`Section 1`>`New Page`, the location of the image should be:

```

 Assets 
    └── Documentation
         └── Section 1
                └── New Page
                    └── new image
```


## Style Guide

### Format

#### Bold, Italics and Paths

- **Bold**. Use sparingly for emphasis, or to highlight option names, for example:
From the **File** menu, select **New**

- *Italic*. Use it when quoting a piece of a text from another source, a piece of text in another language or to give an example, such as sample text to be typed in a text field.

- backticks ` `. Use them for paths both in functional and technical documentation. For menu navigation (for example starting a new document) bold the whole thing and use > to separate the menu items. 

For example:

        `Document` >`New`> `Template`.

This is shown as: `Document` >`New`> `Template`.

#### Tabs for different platforms
When documenting a feature that varies by platform (Windows or Linux, for example), use the following tabs to include information relevant for each platform. Readers can then choose the corresponding tab with the necessary information.

```bash title="Tabs"
=== "C"

    ``` c
    #include <stdio.h>

    int main(void) {
      printf("Hello world!\n");
      return 0;
    }
    ```

=== "C++"

    ``` c++
    #include <iostream>

    int main(void) {
      std::cout << "Hello world!" << std::endl;
      return 0;
    }
    ```
```

=== "C"

    ``` c
    #include <stdio.h>

    int main(void) {
      printf("Hello world!\n");
      return 0;
    }
    ```

=== "C++"

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
*You will have to press return to reboot the system.*
- **Correct**<br> 
*Press return to reboot the system.*


#### Use third person
*Where possible, use the third person imperative.* 

- **Wrong**<br>
*You should run the installation script*
- **Correct**<br>
*Run the installation script*

However, as long as you don't overdo it, it is fine to address the user directly using *you* if it makes the documentation easier to follow or use *the user* when necessary.

#### Avoid gender discrimination
Readers of software documentation are men and women. Avoid using expressions that refer to specific gender forms.
You can avoid gender forms or use *they*/*their* as a generic third-person singular pronoun to refer to a person whose gender is unknown or irrelevant to the context of the usage.

- **Wrong**<br>
*Every user has his home directory.*

- **Correct**<br>
*Every user has a home directory.*<br>
*Every user has their home directory.*


#### Only describe current functionality
Avoid talking about future features or plans for a product or an application.

- **Wrong**<br>
*Graphics can be saved as a GIF image. Support for new formats will be added in future versions.*

- **Correct**<br>
*Graphics can be saved as a GIF image.*


#### Writing for a global audience
Keep in mind that people from all over the globe can use Etendo and its related documentation.
Some important recommendations:

- Avoid using names of people, addresses, and other sample information that are not common in the English language.
- Remember that currencies and formats to represent dates and numbers are not the same in every part of the world.

#### Other conventions

- If you have a list of items (for example a list of files to be downloaded) order them alphabetically unless there is a more obvious logical order.
- Do not use contractions (don't, you're, etc).

---

This work is a derivative of [Documentation Style Guide](https://wiki.openbravo.com/wiki/Documentation_Style_Guide){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.