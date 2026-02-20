---
title: Estructura de subaplicaciones en Etendo Mobile
tags:
    - Etendo Mobile
    - Estructura de subaplicaciones
    - React-Native
    - Gestión de Idioma
    - Etendo UI Library
---

# Estructura de subaplicaciones en Etendo Mobile

## Visión general
Esta página proporciona una guía completa sobre la estructura de las subaplicaciones en Etendo Mobile. Explica conceptos clave como el archivo `App.tsx`, que sirve como el punto de entrada principal de las subaplicaciones, y detalla cómo se utilizan los parámetros de Etendo Mobile para la inicialización. Además, la guía cubre la gestión de idioma, la navegación entre pantallas mediante la pila de navegación y el uso de Etendo UI Library para un diseño y una funcionalidad coherentes en todas las subaplicaciones. Estos elementos constituyen la base para desarrollar subaplicaciones dinámicas y bien integradas dentro de Etendo Mobile.

## Archivo de la aplicación
En `App.tsx`, se encuentra el archivo principal ubicado en la raíz de la subaplicación. En este archivo, definiremos las rutas y los componentes que se renderizarán en cada ruta. Además, este archivo es responsable de la inicialización de la subaplicación y obtiene los Parámetros de Etendo Mobile.

### Parámetros de Etendo Mobile
Etendo Mobile _envía_ Parámetros a la subaplicación y todos están listos para usarse; son:

!!! abstract "Parámetros"
    - _ _id_: ID de la subaplicación
    - _url_: la URL del entorno (configurada en los ajustes de Etendo Mobile)
    - _contextPathUrl:  la ruta de contexto del entorno (configurada en los ajustes de Etendo Mobile)
    - _navigationContainer_: una instancia del contenedor de navegación de Etendo Mobile
    - _token_: token
    - _language_: Idioma
    - _dataUser_: todos los datos relacionados con el usuario. Tiene una interfaz tipada que puede encontrarse en el archivo `src/interfaces/index.ts`
    - _isDev_: booleano que identifica si la aplicación está configurada en modo desarrollo (true) o producción (false).
    - _Camera_: un componente previamente integrado en Etendo Mobile que ahora se ha transferido sin problemas a las subaplicaciones. Este componente en particular incluye una destacada capacidad de escaneo de códigos QR, mejorando la funcionalidad general de las subaplicaciones.
    - _sharedFiles_: array de IFile; si un archivo se comparte con Etendo Mobile desde una aplicación externa, al compartirlo y seleccionar una subaplicación se añadirá el archivo al array de archivos de la subaplicación correspondiente.

### Idioma
El Idioma es una cadena que sirve como representación del Idioma seleccionado por el usuario. Esta configuración de Idioma es configurable dentro de los ajustes de la aplicación Etendo Mobile y desempeña un papel crucial a la hora de determinar el Idioma en el que se presentan los textos dentro de la subaplicación. En este ejemplo, utilizaremos el parámetro _language_ recibido como entrada para inicializar los aspectos restantes de la aplicación en el archivo `App.tsx`.

``` typescript title="App.tsx"
  locale.init();
  locale.setCurrentLanguage(locale.formatLanguageUnderscore(language));
```
!!! tip
    Todas las subaplicaciones deben desarrollarse en inglés _en-US_ y pueden incluir traducciones como español _es-ES_.  

Como puede ver, utilizamos `locale` para establecer el Idioma de la subaplicación. Este `locale` es una instancia de un gestor personalizado del Idioma que está basado en `i18n` y definido en la ruta `subapp/src/localization/locale.ts`.

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

!!! info
    - Carpeta de traducciones: las traducciones se organizan en la carpeta `subapp/src/lang`
    - Archivos JSON por Idioma: cada archivo de traducción corresponde a un Idioma y una configuración regional, siguiendo una estructura que incluye el código de Idioma y la región. Por ejemplo:

    ```
    └── subapp
          └── src
            └── lang
                └── enEN.json
                └── esES.json
    ```

Entre las funciones del gestor `locale`, algunas de las más importantes son:

- `t(key, params)`: esta función recibe una clave (y otros Parámetros opcionales) y devuelve el texto traducido al Idioma de la subaplicación. Esta función se basa en [i18n](https://github.com/fnando/i18n#readme){target="_blank"} y las claves se definen en archivos `.json` en `subapp/src/lang`. 

- `setCurrentLanguage(input)`: obtiene un Idioma como parámetro y establece este Idioma como predeterminado en la subaplicación.

Los archivos de definición de traducciones pueden agrupar la información; por ejemplo, en el archivo de traducciones en inglés `/subapp/src/lang/enUS.json` podemos agrupar los mensajes o etiquetas por pantallas, componentes o como sea óptimo según el desarrollo. Por ejemplo:

``` json title="enUS.json"
{
  "ScreenOne": {
    "LabelOne": "Label 1 Example",
    "LabelTwo": "Label 2 Example",
  },
  "ScreenTwo": {
    "LabelOne": "Label 1 Example",
    "LabelTwo": "Label 2 Example",
  },

```

Luego, para utilizarlo, use la función `local.t`, por ejemplo: `locale.t('ScreenOne.LabelOne')`

### Pila de navegación
La parte de la pila de navegación de `App.tsx` nos permite navegar entre pantallas. Es un componente proporcionado por `@react-navigation/stack` en una aplicación React Native. Conceptualmente, una pila de navegación gestiona el flujo entre diferentes pantallas en la aplicación, permitiendo a los usuarios navegar hacia adelante y hacia atrás entre estas pantallas.

**Conceptos clave**

1. **Inicialización de la pila de navegación**:  
    La función `createStackNavigator()` de `@react-navigation/stack` se utiliza para crear una pila de navegación. Esta pila gestiona una secuencia de pantallas, y cada pantalla se trata como una "ruta" dentro de la pila.

    ```typescript
    const Stack = createStackNavigator();
    ```

2. **Definiciones de pantalla:** Cada pantalla en la aplicación se define utilizando el componente `Stack.Screen`. La prop `name` especifica el identificador único de la pantalla, y el componente asociado a la pantalla se define dentro de los children o se pasa como una función usando render props (`{props => <Component {...props} />}`).
    
    Ejemplo de definiciones de pantalla:

    ``` typescript
    <Stack.Screen
    name="Home"
    options={{ headerShown: false }}
    initialParams={{ dataUser }}>
    {props => <Home {...props} navigationContainer={navigationContainer} />}
    </Stack.Screen>   
    ```

3. **Ruta inicial:** La prop `initialRouteName` en `Stack.Navigator` especifica qué pantalla se cargará primero cuando se inicie la aplicación. En el siguiente caso de ejemplo, la pantalla Home se define como la ruta inicial:

    ```typescript
    <Stack.Navigator initialRouteName="Home">
    ```

### Etendo UI Library
Etendo UI Library es una biblioteca de componentes de UI que sigue el estilo y el diseño de Etendo, y que debe utilizarse durante el desarrollo de subaplicaciones. Esta biblioteca se basa en _React Native Elements_ y está disponible en [NPM - Etendo UI Library ](https://www.npmjs.com/package/etendo-ui-library){target="_blank"}. Puede utilizarla en todas sus subaplicaciones. En esta biblioteca, podemos encontrar componentes como: Button, Input, Navbar, Cards, Icons, etc.

!!! info 
    Para más información, visite [Etendo UI Library - Storybook](https://main--65785998e8389d9993e8ec4c.chromatic.com){target="_blank"}, donde puede ver todos los componentes de la biblioteca. Además, puede ver el código de cada componente y cómo utilizarlo.

    ![storybook.png](../../../assets/developer-guide/etendo-mobile/concepts/subapplication-structure/storybook.png)

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.