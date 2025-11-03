---
tags: 
  - How to
  - Create Page
  - Documentation Page
  - Style
  - Format
---

# How to Create a Page in Etendo Documentation

## Overview
This guide contains basic rules, tips, and suggestions for people intending to develop documentation for Etendo. When different documents use the same guidelines, they are more user friendly, consistent and more simple to combine and reuse. We therefore strongly encourage all contributors to follow these guidelines for the benefit of the readers.


## Requirements
- Python version ^3.11. To install it, follow [the Python installation guide](https://www.python.org/downloads/){target="\_blank"}.


## Steps

1. Clone the [docs](https://github.com/etendosoftware/docs){target="\_blank"} repository 
	
    ```bash title="Terminal" 
    git clone git@github.com:etendosoftware/docs.git
    ```

2. Install dependencies

    ```bash title="Terminal" 
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Create a new branch with [GitFlow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow){target="\_blank"}, where the related pages, assets and configurations are stored.

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

5. Etendo documentation is structured in sections, in general the sections where most of the documentation is found are user guide and developer guide, within these there are subsections according to products and categories, you must decide the location within the structure and create a file with the `.md` format, the name must be in lowercase separated by hyphens. 

    ``` title="Documentation Structure" 
    └── docs
    ├── developer-guide 
    │   └── etendo-classic
    │       └── how-to-guides
    │           ├── new-page.md
    │           ├── ..
    │           ├── ..
    │           └── ..
    ├── user-guide
    │   └── basic-feature
    ```

    In order to display the page in the menu, add this page in the `mkdocs.yml` file in the **nav** section.
    
    !!!important
        - When adding pages to the navigation structure, remember to organize them in alphabetical order.
        - The directory and navigation structure must be the same.

    Example

    ``` title="mkdocs.yml"
    nav: 
    - Home : index.md
    - User Guide:
        ...
        - How-To:
            ...
            - New Page: developer-guide/etendo-classic/how-to-guides/new-page.md
            ...
    - Developer Guide
    ...
    ```

    The documentation should be worked on following the [page format](#page-format) described in the next section.

    Once the documentation is finished:


6. Create a PR to `develop` with all the related changes.
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
    Add the following license statement as a footer on all pages of the Etendo documentation produced internally:
    ```
    ---
    
    This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}. 

    ```

### Useful References

#### Bold

Use sparingly for emphasis, or to highlight option names, for example:
From the **Sales order** window, select **New**

```
**Bold**
```

This is shown as: **Bold**

#### Italics 

Use it when quoting a piece of a text from another source, a piece of text in another language or to give an example, such as sample text to be typed in a text field.

```
*Italic*
```

This is shown as: *Italic*

#### Backticks

Use them to refer to paths, inline code and for menu navigation. For example:

- Path:
    ```
    `/directory/filename.txt`
    ```
    This is shown as: `/directory/filename.txt`
- Inline Code:
    ```
    `./gradlew update.database --info`
    ```
    This is shown as: `./gradlew update.database --info`

- Menu navigation:
    ```
    `Document`>`New`>`Template`
    ```              
    This is shown as: `Document`>`New`>`Template`

#### Admonitions

Admonitions are used to include extra content without interrupting the flow of the page. As shown below, there are different types: 

```
!!!note
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

!!!success
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

!!!warning
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

!!!error
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.
```
This is shown as:

!!!note
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

!!!success
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

!!!warning
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

!!!failure
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

It is also possible to edit the title of the blockquote by adding:

```
!!!failure "Edited title example"
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.
```
This is shown as:

!!!failure "Edited title example"
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

For more information, visit [Admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/){target="\_blank"}.

#### Content Tabs

When documenting a feature with different options (JAR or Source, Windows or Linux, C or C++ for example), use the following tabs to include information relevant for each option. Readers can then choose the corresponding tab with the necessary information and skip reading non-relevant information.

```bash title="Content Tabs"
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
This is shown as:

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

#### Directory Structure

In order to the directory structure, it is necessary to apply the following format:

```
modules
└── org.openbravo.localization.spain.referencedata.taxes
    └── referencedata 
        └── standard
            ├── Impuestos_ES.xml
            └── Spanish_Tax_Alerts.xml
```


#### External Links

To include external links in the documentation, use the following path format: 

```
[Google Example](https://google.com){target="_blank"}
```

This is shown as: [Google Example](https://google.com){target="_blank"} 

#### Internal links (Redirection)

To include internal links, use the relative paths from the current page such as the following example:

```
[Internal Link](../../how-to-guides/example-page.md)
```

This is shown as: [Internal Link](../../how-to-guides/example-page.md)

It is also possible to refer to a specific section inside a page using

```
[Specific section](../../how-to-guides/example-page.md#specific-section)
```

This is shown as: [Specific section](../../how-to-guides/example-page.md#specific-section)

#### Lists

To include lists in the documentation, use the following formats:

Bullet points:

```
List:

- Bullet point a
- Bullet point b
```

This is shown as:

List:

- Bullet point a
- Bullet point b

Numbered list:

```
List:

1. Numbered option 1
    - item 1
    - item 2
2. Numbered option 2
```
This is shown as:

List:

1. Numbered option 1
    - item 1
    - item 2
2. Numbered option 2

!!!info
    Remember respecting the tabs is essential for the continuity of lists, this means that the content of different items must be tabulated.  

#### Images

To include images in the documentation, use the relative paths from the current page with the following format: 

```
![](../../assets/developer-guide/how-to-guides/new-page/new-image.png)
```

!!!info
    Remember to upload the image to the **assets** folder with the corresponding specific location.

For example, if the image location is `developer-guide`> `how-to-guides` >`new-page`, the location of the image should be:

```

 assets 
    └── developer-guide
         └── how-to-guides
                └── new-page
                    └── new-image.png
```
#### More references

For more information about mkdocs, visit [Mkdocs reference](https://squidfunk.github.io/mkdocs-material/reference){target="_blank"}.

## Writing Rules

### Keep it simple
Use short sentences and punctuation to keep ideas clear and simple. Introduce a single idea, concept or action per sentence.

- **Wrong**<br>
*The manufacturing module allows users to define the process plans, work requirements and work efforts; this is how the processes that produce intermediate and final goods work.*

- **Correct**<br>
*The manufacturing module allows users to define the process plans, work requirements and work efforts. This section describes how processes that produce intermediate and final goods function.*


### Tenses
Always use the present tense. Avoid past or future tenses if possible.
In addition, try to refrain from using must, have to, need to, will, should and similar forms.
Keep in mind that a manual describes mandatory procedures to follow to accomplish a certain task.

- **Wrong**<br>
*You will have to press return to reboot the system.*
- **Correct**<br> 
*Press return to reboot the system.*


### Use third person
*Where possible, use the third person imperative.* 

- **Wrong**<br>
*You should run the installation script*
- **Correct**<br>
*Run the installation script*

However, as long as you do not overdo it, it is accepted to address the user directly using *you* if it makes the documentation easier to follow or use *the user* when necessary.

### Avoid gender discrimination
Readers of software documentation are men and women. Avoid using expressions that refer to specific gender forms.
You can avoid gender forms or use *they*/*their* as a generic third-person singular pronoun to refer to a person whose gender is unknown or irrelevant to the context of the usage.

- **Wrong**<br>
*Every user has his home directory.*

- **Correct**<br>
*Every user has a home directory.*<br>
*Every user has their home directory.*


### Only describe current functionality
Avoid talking about future features or plans for a product or an application.

- **Wrong**<br>
*Graphics can be saved as a GIF image. Support for new formats will be added in future versions.*

- **Correct**<br>
*Graphics can be saved as a GIF image.*


### Writing for a global audience
Keep in mind that people from all over the globe can use Etendo and its related documentation.
Some important recommendations:

- Avoid using names of people, addresses, and other sample information that are not common in the English language.
- Remember that currencies and formats to represent dates and numbers are not the same in every part of the world.

### Other conventions

- If you have a list of items (for example a list of files to be downloaded) order them alphabetically unless there is a more obvious logical order.
- Do not use contractions (don't, you're, etc).

---

This work is a derivative of [Documentation Style Guide](https://wiki.openbravo.com/wiki/Documentation_Style_Guide){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.