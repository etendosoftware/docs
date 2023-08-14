---
title: How to Customize the Etendo Skin
---

## Overview

The `cssCompile` task in the **Etendo** Gradle configuration is specifically designed to convert `.scss` files into `.css` files. This documentation aims to provide **Etendo partners** with a comprehensive understanding of its function, usage, and benefits.

## Purpose

With modern web development, **SCSS** offers more power and flexibility compared to traditional **CSS**. As Etendo aims to deliver an impeccable user interface, using `.scss` files allows for better organization, variable definitions, and nested rules. However, browsers understand only CSS. Hence, there's a need to **compile SCSS into CSS**, and that's where our `cssCompile` task steps in.

> **Requirements**
> - npm (Node Package Manager) installed and Sass compiler installed on your system.

!!! info
    ### Installing npm (Node Package Manager)
    If you don't have npm installed on your system, follow these steps:
    
    - Install npm globally using the following command:
    
    ```bash
    npm install -g npm
    ```
    
    - Confirm the installation by checking the versions of node and npm:
    
    ```bash
    node -v
    npm -v
    ```
    
    ### Installing Sass (Syntactically Awesome Style Sheets)
    If you have npm installed and need the Sass compiler, follow these instructions:
    
    - Use npm to install Sass globally on your system:

    ```bash
    npm install -g sass
    ```

    - Confirm the Sass installation by running:

    ```bash
    sass --version
    ```
    
    Seeing the Sass version number means that Sass has been installed correctly.


## How It Works

1. **Directories Scan**: The task scans three primary directories: `modules_core`, `modules`, and `web` for `.scss` files.

2. **Compilation**: For each `.scss` file found, it invokes the `sass` compiler to convert it into a `.css` file.

3. **Output**: The output `.css` file retains the same directory path and filename as the original `.scss`, ensuring easy traceability and debugging.

Below is the actual code for the `cssCompile` task that executes these steps:

```bash
task css_compile() doLast {
    def gen_css = []
    def lookupAt = ['modules_core', 'modules', 'web']
    lookupAt.forEach({dirName ->
        FileTree tree = fileTree(dirName).matching {
            include '**/*.scss'
        }.each {
            def less_fl = it.toString()
            def css_fl = less_fl.replaceAll(".scss", ".css")
            println(it)
            gen_css.add(css_fl)
            exec {
                executable "sass"
                args "$less_fl", "$css_fl"
            }
        }
    })
}
```

This code gives you a clear insight into how the process is automated within the Etendo project.

## How to Use

To customize the skin of Etendo by compiling SCSS to CSS, the `cssCompile` task has been provided.

### Execution

1. Ensure your terminal or **command-line** tool is open.
2. Navigate to the root directory of the **Etendo project**.
3. Run the following **command**:

```bash
./gradlew cssCompile smartbuild --info
```

!!! success
    After execution, you should see an output similar to:
    > Task :cssCompile
    
    > **BUILD SUCCESSFUL**.
    
    This confirms the files that were processed.


## Troubleshooting

If you encounter the error `A problem occurred starting process 'command 'sass''`, it suggests that the `sass` compiler either isn't installed or isn't accessible. Follow these checks:

1. Ensure you've installed the **Sass** compiler.
2. Verify that the `sass` command is available in your system's **PATH**. You can do this by running the `sass --version` command.
3. If the problem persists, **restart your terminal** or ensure you have the necessary permissions to execute commands.


## Conclusion

The `cssCompile` task simplifies the process of working with SCSS in the Etendo project, ensuring that the latest styles are always available in a browser-compatible format. By facilitating the seamless transition from SCSS to CSS, it allows that developers can focus on creativity without being bogged down by manual compilation. The result? A beautiful Etendo user interface with its own styles.