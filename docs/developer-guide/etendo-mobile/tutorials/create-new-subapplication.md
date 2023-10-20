## Overview

This section provides a step-by-step guide on how to run a sub-application in development mode within the Etendo Mobile application. For this we will use a Dummy project with predefined configurations such as rollup, http server and settings with Etendo Classic to build a build sub-application and connect it to our Etendo Mobile.

!!! info
    Before starting this tutorial you must have Etendo, Etendo Mobile and Node.js in your environment. For more information check the [Getting Started in the Etendo Mobile section](/developer-guide/etendo-mobile/getting-started/)

## Fork the dummy application

To begin with we must make a fork of our dummy application [com.etendoerp.subapp.base](https://github.com/etendosoftware/com.etendoerp.subapp.base) and clone it inside the modules folder in our Etendo environment.
    ``` bash title="Terminal"
    git@github.com:etendosoftware/com.etendoerp.subapp.base.git
    ```



![modules.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/modules.png)

## Dynamic app window

It is a window in which you can configure dynamic applications to open them from the Etendo Mobile application. With this configuration you have an application loaded in the module to have a default base sub application in development mode within Etendo Mobile. For more information check the [Dynamic App](/products/etendo-classic/user-guide/general-setup/application/#dynamic-app)

| Variable                | Description                                                      | Default Value                          |
| ----------------------- | ---------------------------------------------------------------- | ------------------                     |
| `Name`                  | Version name                                                     | dev                                    | 
| `File Name`             | Bundle name                                                      | subappexample.js                       |
| `Version`               | Version number                                                   | 1.0.0                                  |
| `Active`                | If active                                                        | true                                   |
| `Is Development`        | Is the development mode                                          | true                                   |
| `Default`               | By default                                                       | false                                  |

![dynamicapp-versio.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/dynamicapp-version.png)

Enter the Role window, search rol Admin, select it and at the bottom select the DYNAMIC APPS - Subapp tab in which you must add the example record Subapp Example with version dev.  

| Variable                | Description                                                      | Default Value                          |
| ----------------------- | ---------------------------------------------------------------- | ------------------                     |
| `Organization`          | Name of organization                                             | *                                      | 
| `App`                   | Name of application                                              | Subapp Example                         |
| `Version`               | Version number                                                   | dev                                    |
| `Active`                | If active                                                        | true                                   |

![role-dynamicapp.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/role-dynamicapp.png)

Finally open in a terminal in modules/com.etendoerp.subapp.base/resources and execute the following command

Install the dependencies 
    ``` bash title="Terminal"
    yarn install 
    ```

## Development mode workflow
### Etendo Classic and Etendo Mobile
1. Etendo Classic should be running.

2. Open the Etendo Mobile application on a mobile device. You can use either an emulator or a physical device.

### Rollup
[Rollup](https://rollupjs.org/) is a module packer for JavaScript that compiles small pieces of code into something larger and more complex, this is already installed in the module.

Inside the project there is a file rollup.config.js where it is defined where the packaged file with .js extension is going to be generated.

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
    //Path where the application build will be generated. 
      file: '../web/com.etendorx.subapp.base/subappexample.js', 
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

In the package.json it is defined where the local server will be raised with [Http-server](https://www.npmjs.com/package/http-server) with the `yarn dev` command (In this case on port 3000).

```groovy title="package.json"
"scripts": {
    "android": "react-native run-android",
    "ios": "react-native run-ios",
    "start": "react-native start",
    "test": "jest",
    "lint": "eslint .",
    "build": "rollup -c",
    "dev": "http-server -p 3000 ../web/com.etendorx.subapp.base/"
  },
```

 In a terminal run the following commands to build the sub-application and to lift it on a local server
    ``` bash title="Terminal"
    cd modules/com.etendoerp.subapp.base/resources
    yarn build && yarn dev
    ```

### Ngrok
So that from Etendo Mobile we can access a sub-application we will use [Ngrok](https://ngrok.com/) that exposes a local port in a public url. In this case we will expose port 3000 by executing the following command
    ``` bash title="Terminal"
    ngrok http 3000 
    ```
### Etendo Mobile Setup
1. First of all it is necessary to configure the public url that we previously generated with ngrok inside Etendo Mobile. For this we need to login with the System Administrator role changing the default role from the backend.
    ![system-default.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/system-default.png)

2. Log in to Etendo Mobile with your credentials and enter the configuration window and save the ngrok url in the debug url field (you must be logged in with the system administrator role for this field to be displayed).
    ![debug-url.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/debug-url.png)
    
3. Log out of Etendo Mobile and into Etendo Classic change your role to admin by default again.
    ![admin-default.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/admin-default.png)

4. Log in to the Etendo Mobile application and you will be able to view the list of sub-applications. Clicking on Subapp Example will download the build previously generated and exposed in the ngrok url.
    ![app-home.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/app-home.png)
5. Here you can see the sub-application.
    ![sub-app.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/sub-app.png)
### Applying changes
1. Add any changes for example in `modules/com.etendoerp.subapp.base/resources/src/screens/home/index.tsx` to the prop typeStyle of the Button component change it to `secondary`

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
2.  In a terminal run the following commands to build the sub-application and to lift it on a local server
        ``` bash title="Terminal"
        cd modules/com.etendoerp.subapp.base/resources
        yarn build && yarn dev
        ```
3.  Exit and re-enter the sub-application to visualize the changes.
     ![app-test.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/app-test.png)





