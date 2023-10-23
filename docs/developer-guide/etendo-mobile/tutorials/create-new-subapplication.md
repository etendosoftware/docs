## Overview

This section provides a step-by-step guide on how to run a sub-application in development mode within the Etendo Mobile application. For this you will need the Dummy project with predefined configurations like rollup, http server and settings with Etendo Classic to build a development sub-application and connect it to Etendo Mobile.

!!! info
    Before starting this tutorial requires Etendo, Etendo Mobile, Ngrok and Node.js in the local environment. For more information check the [Getting Started in the Etendo Mobile section](/developer-guide/etendo-mobile/getting-started/){target="_blank"}.

## Fork the dummy application

To start with it requires a fork of our dummy application [com.etendoerp.subapp.base](https://github.com/etendosoftware/com.etendoerp.subapp.base){target="_blank"} and clone it inside the modules folder in our Etendo environment.
    ``` bash title="Terminal"
    git@github.com:etendosoftware/com.etendoerp.subapp.base.git
    ```



![modules.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/modules.png)

## Dynamic app window

This is a window where dynamic applications can be configured to open from the Etendo Mobile application. Forking the dummy app will result in a base sub-application loaded by default in development mode, allowing the developer to use a development URL and not a productive one within Etendo Mobile. For more information check the [Dynamic App](/products/etendo-classic/user-guide/general-setup/application/#dynamic-app){target="_blank"}.

| Variable                | Description                                                      | Default Value                          |
| ----------------------- | ---------------------------------------------------------------- | ------------------                     |
| `Name`                  | Version name                                                     | dev                                    | 
| `File Name`             | Bundle name                                                      | subappexample.js                       |
| `Active`                | If active                                                        | true                                   |
| `Is Development`        | Is the development mode                                          | true                                   |

![dynamicapp-versio.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/dynamicapp-version.png)

In the Role window, the Admin role is found, in the "DYNAMIC APPS - Subapp" tab, the example record Subapp Example with dev version must be added.  

| Variable                | Description                                                      | Default Value                          |
| ----------------------- | ---------------------------------------------------------------- | ------------------                     |
| `Organization`          | Name of organization                                             | *                                      | 
| `App`                   | Name of application                                              | Subapp Example                         |
| `Version`               | Version number                                                   | dev                                    |
| `Active`                | If active                                                        | true                                   |

![role-dynamicapp.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/role-dynamicapp.png)


## Development mode workflow
### Etendo Classic and Etendo Mobile

1. To start in a terminal in `modules/com.etendoerp.subapp.base/resources` and will be executed the following command.

    Install the dependencies 
    ``` bash title="Terminal"
    yarn install 
    ```

2. Etendo Classic should be running.

3. Open the Etendo Mobile application on a mobile device. You can use either an emulator or a physical device.

### Rollup
[Rollup](https://rollupjs.org/){target="_blank"} is a module packer for JavaScript that compiles small pieces of code into something larger and more complex, this is already installed in the module.

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

In the package.json it is defined where the local server will be raised with [Http-server](https://www.npmjs.com/package/http-server){target="_blank"} with the `yarn dev` command (In this case on port 3000).

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

In a terminal I would execute the following commands to build the sub-application and launch it on a local server
    ``` bash title="Terminal"
    cd modules/com.etendoerp.subapp.base/resources
    yarn build && yarn dev
    ```

### Ngrok
So that from Etendo Mobile we can access a sub-application we will use [Ngrok](https://ngrok.com/){target="_blank"} that exposes a local port in a public url. In this case we will expose port 3000 by executing the following command
    ``` bash title="Terminal"
    ngrok http 3000 
    ```
### Etendo Mobile Setup
1. First of all it is necessary to configure the public url that we previously generated with ngrok inside Etendo Mobile.  Accessing with the System Administrator role and change the default role from the backend.
    ![system-default.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/system-default.png)

2. In Etendo Mobile, in the configuration window, save the ngrok url in the debug url field (you must be logged in with the system administrator role for this field to appear).
    ![debug-url.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/debug-url.png)
    
3. Log out of Etendo Mobile and in Etendo Classic change the role to admin by default.
    ![admin-default.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/admin-default.png)

4. In Etendo Mobile you will see the list of subapps. Clicking on Subapp Example will download the build previously generated and exposed in the ngrok url.
    ![app-home.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/app-home.png)
5. Here is the sub-application.
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





