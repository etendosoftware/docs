## Overview

This section provides a step-by-step guide on how to run a sub-app in developer mode to work with Etendo. This requires that your project has dependencies installed so that you can generate a bundle of it, be able to set it as developer mode and start incorporating this sub-app into Etendo Mobile. 

!!! info
    Before starting this tutorial you must have Etendo, Etendo Mobile and Node.js in your environment. For more information check the [Getting Started in the Etendo Mobile section](/developer-guide/etendo-mobile/getting-started/)

## Fork the dummy application

To begin with we must make a fork of our dummy application com.etendoerp.subapp.base https://github.com/etendosoftware/com.etendoerp.subapp.base and clone it inside the modules folder in our Etendo environment.

![modules.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/modules.png)

## Configuring the Etendo

Log in to your account as an administrator. The default login credentials for this administrative account are:

    Username: admin
    Password: admin

Once you are logged in, switch your role to Admin, as the image shows:

![admin.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/admin.png)


Enter the Dynamic App tab, find the name Subapp Example, select it and in the lower tab under DYNAMIC APP VERSION add a record with the version name, the application bundle name and set Is Development to true.

| Variable                | Description                                                      | Default Value                          |
| ----------------------- | ---------------------------------------------------------------- | ------------------                     |
| `Name`                  | Version name                                                     | dev                                    | 
| `File Name`             | Bundle name                                                      | subappexample.js                       |
| `Version`               | Version number                                                   | 1.0.0                                  |
| `Active`                | If active                                                        | true                                   |
| `Is Development`        | Is the development mode                                          | true                                   |
| `Default`               | By default                                                       | false                                  |

![dynamicapp-versio.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/dynamicapp-version.png)

Enter the Role tab, filter by the name F&B International Group Admin, select it and at the bottom select the DYNAMIC APPS - Subapp tab in which you must add the example record Subapp Example with version 1.0.0.  

| Variable                | Description                                                      | Default Value                          |
| ----------------------- | ---------------------------------------------------------------- | ------------------                     |
| `Organization`          | Name of organization                                             | *                                      | 
| `App`                   | Name of application                                              | Subapp Example                         |
| `Version`               | Version number                                                   | 1.0.0                                  |
| `Active`                | If active                                                        | true                                   |

![role-dynamicapp.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/role-dynamicapp.png)

Finally open in a terminal in modules/com.etendoerp.subapp.base/resources and execute the following command

Install the dependencies 
    ``` bash title="Terminal"
    yarn install 
    ```

## Development mode workflow

1. The tomcat server should be up with Etendo.

2. Open the Etendo Mobile application on a mobile device. If you don't have it you can download it from the [Playstore here](https://play.google.com/store/apps/details?id=com.smf.mobile.etendo_app_loader&pli=1)

3. In a terminal in modules/com.etendoerp.subapp.base/resources and run the following command to build the changes to the application and to lift it on a server
    ``` bash title="Terminal"
    rollup -c && yarn dev
    ```
4. Use ngrok on port 3000 with the following command
    ``` bash title="Terminal"
    ngrok http 3000
    ```
5. Log in as system administrator in Etendo and set the "set as default" check to true.
    ![system-default.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/system-default.png)

6. Log into the Etendo Mobile with your credentials and enter the settings section and save the ngrok url in debug url.
    ![debug-url.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/debug-url.png)
    
7. Log out of the application and go to Etendo to change your role to admin by default.
    ![admin-default.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/admin-default.png)

8. Log in to the Etendo Mobile application and try to access the sub-application by clicking on the letter with your name.
    ![app-home.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/app-home.png)
9. It should navigate you to the sub-application
    ![sub-app.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/sub-app.png)
10. Show a change in the sub-application and the procedure
    1. Add any change for example en src/screens/home/index.tsx:

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
            typeStyle={'primary'}
            text={locale.t('Home.back')}
            iconLeft={<BackIcon />}
            onPress={() => {
            navigationContainer.navigate('Home');
            }}
        />
        <Text>Hello</Text> // Add this change
        </View>
    );
    };

    export default Home;
    ```
    2.  In a terminal in modules/com.etendoerp.subapp.base/resources and run the following command to build the changes to the application and to lift it on a server
        ``` bash title="Terminal"
        rollup -c && yarn dev
        ```
    3.  Exit the subapp and log back in to see the change.
     ![app-test.png](/assets/developer-guide/etendo-mobile/create-new-subapplication/app-test.png)





