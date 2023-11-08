## Overview

This section provides a step-by-step guide on how to run a subapplication in development mode within the Etendo Mobile application. For this you will need the Dummy project with predefined configurations like rollup, http server and settings with Etendo Classic to build a development subapplication and connect it to Etendo Mobile.

!!! info
    Before starting this tutorial requires Etendo, Etendo Mobile, Ngrok and Node.js in the local environment. For more information check the [Getting Started in the Etendo Mobile section](/developer-guide/etendo-mobile/getting-started/){target="_blank"}.

## Create a new Etendo Classic module

Once Loged in, go to the modules window, and create a new one as the image shows:

| Variable                | Description                                                      | Example Value                          |
| ----------------------- | ---------------------------------------------------------------- | ------------------                     |
| `Java Package`          | Java Package                                                     | com.etendoerp.subapp.base              | 
| `Name`                  | Module name                                                      | Subapp Base                            |
| `Type`                  | Module type                                                      | Module                                 |
| `Description`           | Description                                                      | An subapp example to develop into dynamic app |
| `Version`               | Version name                                                     | 1.0.0                                   |


![create-module..png](/assets/developer-guide/etendo-mobile/create-new-subapplication/create-module.png)

!!! Tip
    - Notice that the name can be anything you want, but the type have to be setted as Module.
    - The description field is free and also required.

In this case we going to start from 1.0.0 version and set the DB prefix as ETAPP.

After save all the configuration, you have to export it. Open a terminal in the root of your etendo classic and execute the following command:
    ``` bash title="Terminal"
    ./gradlew export.database
    ```

!!! success "Important"
    The output must be a "BUILD SUCCESSFUL" message.


## Add the dummy application
1. To start you must download the latest version of the [Dummy subapplication zip](https://github.com/etendosoftware/subapp/releases){target="_blank"} file and unzip it inside the module just created in the `subapp` folder.
    ![modules.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/modules.png)

2. In a terminal on path `modules/<javapackage>/subapp` install the depedencies declared in the package.json and for it the following command would be executed.
    ``` bash title="Terminal"
    yarn install 
    ```

## Dynamic app window
In the `Dynamic App` window the dynamic applications are configured to use them from the Etendo Mobile application. To do this, a record is created in which the module to which it belongs, the name of the application and the location of the build of the subapplication is declared.

After selecting this record in the `Dynamic App Version` tab we must add the version name, the name of the build file and check the box "is Development" to true, which will allow the developer to use a development URL and not a productive one inside Etendo Mobile. For more information check the [Dynamic App](/user-guide/etendo-classic/basic-features/general-setup/application/#dynamic-app){target="_blank"}.

| Variable                | Description                                                      | Example Value                          |
| ----------------------- | ---------------------------------------------------------------- | ------------------                     |
| `Module`                | Module name                                                      | Subapp Base - 1.0.0 - English (USA)    | 
| `Name`                  | Subapplication Name                                             | Subapp Example                         |
| `Dyrectory Location`    | Subapplication build location                                   | /                                      |
| `Active`                | If active                                                        | true                                   |

### Dynamic app version

| Variable                | Description                                                      | Example Value                          |
| ----------------------- | ---------------------------------------------------------------- | ------------------                     |
| `Name`                  | Version name                                                     | dev                                    | 
| `File Name`             | Bundle name                                                      | subappexample.js                       |
| `Active`                | If active                                                        | true                                   |
| `Is Development`        | Is the development mode                                          | true                                   |

![dynamicapp-versio.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/dynamicapp-version.png)

Permissions must be given to the Admin role in order to view the application within the Etendo Mobile subapplication.
From the `Role` window, look for the name Admin and in the `DYNAMIC APPS - Subapp` tab, add the example record Subapp Example with dev version.

| Variable                | Description                                                      | Example Value                          |
| ----------------------- | ---------------------------------------------------------------- | ------------------                     |
| `Organization`          | Name of organization                                             | *                                      | 
| `App`                   | Name of Subapplication                                          | Subapp Example                         |
| `Version`               | Version number                                                   | dev                                    |
| `Active`                | If active                                                        | true                                   |

![role-dynamicapp.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/role-dynamicapp.png)

## Concepts

In this section we will explain the main parts and files of the subapplication that we will use.

#### App.tsx
  This file is located in the root of the subapplication and is the main file. In this file we will define the routes and the components that will be rendered in each route. In addition, this file is responsible of the initialization of the subapplication and gets the params from Etendo Mobile.

![path-to-app-file.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/path-to-app-file.png)

#### Params from Etendo Mobile
Etendo Mobile _sends_ the following params to the subapplication:

!!! abstract "Params"
    - _ _id_: id of the subapplication
    - _url_: the environment url (setted in setting's Etendo Mobile)
    - _navigationContainer_: an instance of the navigation container of Etendo Mobile
    - _token_: Token
    - _language_: Language
    - _dataUser_: all data related to the user. It has a typed interface that can be found in the file `src/interfaces/index.ts`

In this example, we will receive these params in App.tsx of the subapp:

``` typescript title="App.tsx"
  interface AppProps {
    language: string;
    dataUser: IData;
    navigationContainer: INavigationContainerProps;
  }

  const App = ({language, navigationContainer, dataUser}: AppProps) => {

```

#### Language
The language is a string that serves as a representation of the user's selected language. This language setting is configurable within the Etendo Mobile application's settings and plays a crucial role in determining the language in which texts are presented within the subapplication. In this example, we will utilize the _language parameter received as input_ to initialize the remaining aspects of the application in the "App.tsx" file.

``` typescript title="App.tsx"
  locale.init();
  locale.setCurrentLanguage(locale.formatLanguageUnderscore(language));
```
!!! tip
    All subapps have to have at least two languages: _en-US_ and _es-ES_.  

As you can see, we use `locale` to set the language of the subapplication. This `locale` is an instace of a custom handler of the language which is based in `i18n` and defined in this path `subapp/src/localization/locale.ts`.

``` typescript title="locale.ts"
const locale: LocaleModule = {
  currentDateLocale: null,

  i18n,
  init() {...}

  t(key, params) {...}

  setCurrentLanguage(input) {...}

};

export default locale;

```

Between the functions of the `locale` handler, some of the most important are:

!!! info "Functions"
    - _t(key, params)_: this function receive a key (and other optional params) and returns the text translated to the language of the subapplication. This function is based in [i18n](https://github.com/fnando/i18n#readme){target="_blank"} and the keys are defined in .json files in `subapp/src/lang`. 
    - _setCurrentLanguage(input)_: gets a language as a param and sets this language as default in the subapplication.


#### Navigation Stack
The navigation stack is a component in App.tsx that allows us to navigate between screens. It is a component provided by react-navigation. In this example we will use only one screen called Home which is the main screen of the subapplication (initialRouteName in stack).

``` typescript title="App.tsx"
import React from 'react';
import Home from './src/screens/home';
import {createStackNavigator} from '@react-navigation/stack';
import locale from './src/localization/locale';
import {IData, INavigationContainerProps} from './src/interfaces';

interface AppProps {
  language: string;
  dataUser: IData;
  navigationContainer: INavigationContainerProps;
}

const App = ({language, navigationContainer, dataUser}: AppProps) => {
  const Stack = createStackNavigator();

  locale.init();
  locale.setCurrentLanguage(locale.formatLanguageUnderscore(language));

  return (
    <Stack.Navigator initialRouteName="Home">
      <Stack.Screen
        options={{headerShown: false}}
        name="Home"
        initialParams={{dataUser}}>
        {props => <Home {...props} navigationContainer={navigationContainer} />}
      </Stack.Screen>
    </Stack.Navigator>
  );
};

export {App};
export default App;

```

#### Etendo UI
Etendo UI is a _library of components_ that will be used throughout the example subapplication. This library is based on React Native Elements and it is available on [NPM](https://www.npmjs.com/package/etendo-ui-library){target="_blank"}. You can use it in all of your subapplications.
  In this library we can find components like:  Button, Input, Navbar etc.

![etendo-ui-library-npm.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/etendo-ui-library-npm.png)

You can find more information about in [Etendo UI Library](https://develop--649b07373a33e896f7881dd9.chromatic.com/?path=/docs/how-to-install-steps--docs){target="_blank"} 

_Storybook_ is a place where you can try and see all the components of the library. Also, you can see the code of each component and how to use it.

![storybook.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/storybook.png)

## Development mode setup

### Etendo Classic and Etendo Mobile

1. Etendo Classic should be running.

2. Open the Etendo Mobile application on a mobile device. You can use either an emulator or a physical device.

### Rollup
[Rollup](https://rollupjs.org/){target="_blank"} is a module packer for JavaScript that compiles small pieces of code into something bigger and more complex, this is already installed in the module.

Inside the project there is a file rollup.config.js where the path where the packaged file with .js extension will be generated is defined.

It is necessary to modify this path adding the `javapackage` of the generated module.

```groovy title="rollup.config.js"
import typescript from '@rollup/plugin-typescript';
import peerDepsExternal from 'rollup-plugin-peer-deps-external';
import json from '@rollup/plugin-json';

const pkg = JSON.parse(
  require('fs').readFileSync(
    require('path').resolve('./package.json'),
    'utf-8',
  ),
);

const external = Object.keys(pkg.dependencies || {});

export default {
  input: './App.tsx',
  output: [
    {
    //Change the javapackge in the path where the application build will be generated. 
      file: '../web/<javapackage>/subappexample.js', 
      format: 'cjs',
      exports: 'auto',
      strict: false,
      sourcemap: 'inline',
    },
  ],
  plugins: [peerDepsExternal(), json({compact: true}), typescript()],
  external,
};
```

In the package.json you define the path where the local server will be raised with [Http-server](https://www.npmjs.com/package/http-server){target="_blank"} with the `yarn dev` command.
This path must coincide with the path where the build of the application was generated. Also the local port to be exposed is defined here (in this case port 3000).


```groovy title="package.json"
"scripts": {
    "android": "react-native run-android",
    "ios": "react-native run-ios",
    "start": "react-native start",
    "test": "jest",
    "lint": "eslint .",
    "build": "rollup -c",
    "dev": "http-server -p 3000 ../web/<javapackage>/subapp"
  },
```

In a terminal on path `modules/<javapackage>/subapp`, run the following commands to build the subapplication and deploy it to a local server.
    ``` bash title="Terminal"
    yarn build && yarn dev
    ```

### Ngrok
So that from Etendo Mobile we can access a subapplication in development mode we will use [Ngrok](https://ngrok.com/){target="_blank"} that exposes a local port in a public url. In this case we will expose port 3000 by executing the following command.
    ``` bash title="Terminal"
    ngrok http 3000 
    ```

 ![ngrok-terminal.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/ngrok-terminal.png)
### Etendo Mobile Setup
1. First we need to configure the public URL that we have previously generated with Ngrok inside Etendo Mobile. To do this we must access the `System Administrator` role and set `set as default` to true, since when entering the Etendo Mobile application it will log in with the default role.
    ![system-default.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/system-default.png)

2. In Etendo Mobile, in the `Settings` window, save the Ngrok URL in the `Debug URL` field (you must be logged in with the `System Administrator` role for this field to appear).
    ![debug-url.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/debug-url.png)
    
3. Log out of Etendo Mobile and in Etendo Classic change the role to admin by default again.
    ![admin-default.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/admin-default.png)

4. In Etendo Mobile you will see the list of subapps. Clicking on `Subapp Example` will download the build previously generated and exposed in the Ngrok URL.
    ![app-home.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/app-home.png)
5. Here is the subapplication.
    ![sub-app.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/sub-app.png)
## Applying changes workflow
1. Add any changes for example in `modules/<javapackage>/subapp/src/screens/home/index.tsx` to the prop typeStyle of the Button component change it to `secondary`.

    ```groovy title="index.tsx"
    import React from 'react';
    import {Text, View} from 'react-native';
    import locale from '../../localization/locale';
    import {styles} from './style';
    import {Button, BackIcon} from 'etendo-ui-library';

    interface NavigationContainerProps {
    navigate: (screenName: string, params?: any) => void;
    }

    interface HomeProps {
    navigationContainer: NavigationContainerProps;
    }

    const Home: React.FC<HomeProps> = ({navigationContainer}) => {
    return (
        <View style={styles.container}>
        <Text style={styles.text}>{locale.t('Home.welcome')}</Text>
        <Button
            typeStyle={'secondary'} //Change this prop
            text={locale.t('Home.back')}
            iconLeft={<BackIcon />}
            onPress={() => {
            navigationContainer.navigate('Home');
            }}
        />
        </View>
    );
    };

    export default Home;
    ```
2.  In a terminal on path `modules/<javapackage>/subapp`, run the following commands to build the subapplication and deploy it to a local server.
    ``` bash title="Terminal"
    yarn build && yarn dev
    ```
3.  Exit and re-enter the subapplication to visualize the changes.(No need to log out).
     ![app-test.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/app-test.png)





