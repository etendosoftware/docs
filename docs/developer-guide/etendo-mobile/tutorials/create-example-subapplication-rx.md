## Overview

This tutorial provides an extensive, step-by-step guide to help you create a new sub-app by forking it from our base project, which can be found on Github [com.etendoerp.subapp.base](https://github.com/etendosoftware/com.etendoerp.subapp.base){target="_blank"}. By following these instructions, you will gain the capability to create a fully functional standalone sub-application, utilizing the power of RX, as explained in this [RX tutorial](link to RX tutorial), and harnessing the potential of Etendo UI Library components, detailed in our comprehensive guide on installation and usage on the [documentation](https://develop--649b07373a33e896f7881dd9.chromatic.com/?path=/docs/how-to-install-steps--docs){target="_blank"}. This process not only enables you to develop a unique sub-app but also contributes to the expansion of your application ecosystem by integrating a classic module, thereby enhancing its overall functionality and versatility.

!!! info
    Before starting this tutorial must have done [how to create a new subapp](/developer-guide/etendo-mobile/tutorials/create-new-subapplication){target="_blank"} tutorial.

## Configuring the Etendo classic

### Module and export database

Once Loged in, go to the `modules` window, and create a new one as the image shows:

![modules-creation.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/modules-creation.png)

!!! tip
    - Notice that the name can be anything you want, but the type have to be setted as Module.
    - The _description field_ is free and also _required_.
In this case we going to start from 1.0.0 version and set the DB prefix as ETAPP.

After save all the configuration, you have to export it.
Open a terminal in the root of your etendo classic and execute the following command:

```bash title="Terminal"
   ./gradlew export.database
```

!!! Success "Important"
    The output must be a _"BUILD SUCCESSFUL"_ message.

### Dynamic app and role configuration

#### Dynamic app
1. First _select_ the module that you want to configure.
2. Type a _name_ for the dynamic app, in this case we going to use the same name as the module.
3. The _directory location_ in this is the root because this example is just running in developer mode.

    !!! warning "Important"
        Check this subapp as _active_.

4. In the section below you going to set two important values:

    - _Name_: TODO: ask why is 1.0.0 (the same as the module version?)
    - _File Name_: is the name of the bundle that you going to create.

The final result must be like this:

![dynamic-app-creation.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/dynamic-app-creation.png)

Then you have to relate the dynamic app with the role allowed to use it.

#### Role configuration
1. Go to `role` window and select the role that you want to use.
2. In this case we going to use the _admin role_, so select it.
3. In the section bellow, select which _organization, App and Version_ you want to relate.

!!! warning "Important"
    Keep this dynamic app as _active_.

At this point you have _done_ with the etendo classic configuration.
The following steps are center about a new subapp forking from our base app example.

## Fork the base sub-application

To begin with we must make a _fork_ of our base sub app [com.etendoerp.subapp.base](https://github.com/etendosoftware/com.etendoerp.subapp.base){target="_blank"}.
In this case we going to use this name: _com.etendorx.subapp.product_ (TODO: ask about the name, com.etendorx.subapp.XXXX is for all subapps?)

![create-fork-base.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/create-fork-base.png)

After fork, _clone_ the repository inside the modulesrx folder in our Etendo environment.

![repository-cloned.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/repository-cloned.png)

!!! warning "Important"
    Whole process to run a subapp in _developer mode_ among with etendo classic and etendo mobile is detailed in this link [here](/developer-guide/etendo-mobile/tutorials/create-new-subapplication){target="_blank"}

[here](image of dynamic app empty rendered in etendo mobile) TODO: pedir imaagen a lean

## Customizing and Programming a Sub-Application

In this section we will explain how to customize and program a sub-application. We will use our example of a product sub-application, which will allow us to manage the products of our company. This sub-application will have a list of products, a form to create and edit products and a detail of the product.

But first, we will explain the _main parts and files of the sub-application_ that we will use.

### Main parts and files

#### App.tsx
  This file is located in the _root_ of the sub-application and is the main file of the sub-application. In this file we will define the _routes_ of the sub-application and the components that will be rendered in each route. In addition, this file is responsible of the _initialization_ of the sub-application and gets the _params_ from Etendo Mobile.

![path-to-app-file.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/path-to-app-file.png)

#### Params from Etendo Mobile
Etendo Mobile _sends_ the following params to the sub-application:

!!! abstract "Params"
    - _ _id_: id of the sub-application
    - _url_: the url setted in setting's Etendo Mobile
    - _navigationContainer_: an instance of the navigation container of Etendo Mobile
    - _token_: Token
    - _language_: Language
    - _dataUser_: all data related to the user. It has a typed interface that can be found in the file `src/interfaces/index.ts`

In our example, we will receive these params in App.tsx of the subapp:

![params-of-app-file.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/params-of-app-file.png)

#### Language
The language is a string that serves as a representation of the user's selected language. This language setting is configurable within the Etendo Mobile application's settings and plays a crucial role in determining the language in which texts are presented within the sub-application. In our example, we will utilize the _language parameter received as input_ to initialize the remaining aspects of the application in the "App.tsx" file.

![language-initalization.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/language-initalization.png)

As you can see, we use `locale` to set the language of the sub-application. This `locale` is an instace of a custom handler of the language which is based in `i18n` and defined in this path `resources/src/localization/locale.ts`.

![locale-functions.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/locale-functions.png)

Between the functions of the `locale` handler, some of the most important are:

!!! info "Functions"
    - _t(key, params)_: this function receive a key (and other optional params) and returns the text translated to the language of the sub-application. This function is based in `i18n.t` and the keys are defined in .json files in `resources/src/lang`.
    - _setCurrentLanguage(input)_: gets a language as a param and sets this language as default in the sub-application.


#### Navigation Stack
The navigation stack is a component in App.tsx that allows us to navigate between screens. It is a component that is provided by _react-navigation_.
In our example we will use just two screens:

- _Home_: this is the main screen of the sub-application (`initialRouteName` in stack). It will show a list of products.
- _ProductDetail_: this screen will show the detail of a product. Also, it will allow us to edit the product.

![all-app-file.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/all-app-file.png)

#### Etendo UI
Etendo UI is a _library of components_ that we use along our sub-application example. This library is based on React Native Elements and it is available on [NPM](https://www.npmjs.com/package/etendo-ui-library){target="_blank"}. You can use it in all of your sub-applications.
  In this library we can find components like: - Button - Input - Text - Navbar etc.

![etendo-ui-library-npm.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/etendo-ui-library-npm.png)

You can find more information about this library in this [link](https://develop--649b07373a33e896f7881dd9.chromatic.com/?path=/docs/how-to-install-steps--docs){target="_blank"} TODO: get the prod link
_Storybook_ is a place where you can try and see all the components of the library. Also, you can see the code of each component and how to use it.

![storybook.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/storybook.png)

### Product subapp example

In this section we will do an overview about the product sub-application example screens. principal parts of the sub-application where covered in the previous section.

#### Home
  - This is the main screen of the sub-application. It will show a list of products. Also, it will allow us to edit and remove a product, find a product by name and navigate to the detail of a product.
  - The route to this screen is `src/screens/home/index.tsx`.
    <figure markdown>
      ![home-screen.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/home-screen.png){ width="300", align=left } 
      ![remove-product.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/remove-product.png){ width="300", align=right}
    </figure>

#### ProductDetail
  - This screen will show the detail of a product. Also, it will allow us to edit the product.
  - It's the same screen used to create a new product. there is a flag to know if the product is new or not (productItem).
  - The route to this screen is `src/screens/productDetail/index.tsx`.
    <figure markdown>
      ![add-product.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/add-product.png){ width="300", align=left } 
      ![edit-product.png](/assets/developer-guide/etendo-mobile/create-example-subapplication/edit-product.png){ width="300", align=right}
    </figure>
