---

tags:
    - Etendo Mobile
    - Etendo RX
    - Configuración de Dynamic App
    - Subapp
    - Crear subaplicación
---

# Crear nueva subaplicación

## Visión general

Este tutorial proporciona una guía paso a paso para crear una nueva subaplicación dentro de **Etendo Mobile**. Siguiendo estas instrucciones, aprenderá a utilizar plenamente las capacidades de **Etendo RX** y a aprovechar los componentes visuales disponibles en la **Etendo UI Library** para construir una subaplicación funcional.

El tutorial le guiará a través de la creación de la *Subapp de Producto*, una aplicación sencilla que permite la adición, eliminación y modificación de productos, así como su visualización en una cuadrícula. Al finalizar, contará con las habilidades necesarias para crear y distribuir subaplicaciones como módulos, ampliando así la funcionalidad móvil de Etendo.

!!! info
    Antes de comenzar, asegúrese de que su entorno local cumple todos los requisitos necesarios revisando la sección [Primeros pasos](../getting-started.md) de Etendo Mobile.
## Configuración del Módulo 

### Crear nuevo Módulo de Etendo Classic

:material-menu: `Aplicación` > `Diccionario de la Aplicación` > `Módulo`

1. Como rol Administrador del Sistema, abra la ventana **Módulo** y cree un nuevo registro. Este módulo se utilizará para desarrollar y distribuir la aplicación.

    <figure markdown="span">
    ![modules-creation.png](../../../assets/developer-guide/etendo-mobile/tutorials/create-new-subapplication/modules-creation.png)
    <figcaption>Ejemplo de configuración del módulo Product Subapp</figcaption>
    </figure>

    !!! tip
        - Tenga en cuenta que el nombre puede ser cualquiera, pero el tipo debe establecerse como Módulo.
        - El campo _descripción_ es libre y también es _obligatorio_.
        - La casilla de verificación _Is Rx_ indica que este módulo incluirá configuraciones de servicios RX; debe especificarse el Javapackage del servicio RX.
        - La casilla de verificación _Is React_ indica que este módulo incluye una subaplicación y se genera código React Native.
        - En este caso, comience desde la versión del módulo `1.0.0` y establezca el prefijo de BD como `ETSAPPP`.


### Configuración de Dynamic App

:material-menu: `Aplicación` > `Configuración General` > `Aplicación` > `Dynamic App`

Configure y exporte aplicaciones dinámicas en Etendo Classic, que se muestran dinámicamente en Etendo Mobile.

En la ventana **Dynamic App**, especifique la ruta y la versión de la subaplicación. 

Para el ejemplo que estamos siguiendo, la Dynamic App en Etendo debe configurarse con los siguientes campos del formulario y sus valores correspondientes:

![](../../../assets/developer-guide/etendo-mobile/tutorials/create-new-subapplication/dynamic-app-creation.png)

Campos a tener en cuenta:

- **Módulo**: El módulo que puede exportar la configuración de la ventana. En nuestro caso de ejemplo, establezca `Product SubApp`.
- **Nombre**: Nombre con el que se mostrará la aplicación. En nuestro caso de ejemplo, establezca `Product Subapp`
- **Directory Location**: La ruta donde se encuentra el bundle de la aplicación compilada. En desarrollo, la ruta está vacía `/`, pero en producción, la ruta es `/web/<javapackage>/`. En nuestro caso de ejemplo, establezca `/`
- **Activo**: Para seleccionar si esta aplicación está activa o no. En nuestro caso de ejemplo, establezca `true`


La solapa **Dynamic App Version** permite versionar la aplicación, habilitando tanto versiones de desarrollo como de producción.

Campos a tener en cuenta:

- **Nombre**: Nombre de la versión de la aplicación, p. ej. `dev` o `1.0.0`. En nuestro caso de ejemplo, establezca `dev`
- **Nombre archivo**: El nombre del bundle de la aplicación compilada; por defecto `dist.js`.
- **Valor por defecto**: Esta marca define que esta versión es productiva. En nuestro caso de ejemplo, establezca `false`
- **Is Development**: Esta marca define que esta versión está en desarrollo y puede desplegarse localmente. En nuestro caso de ejemplo, establezca `true`
- **Activo**: Para seleccionar si esta versión de la aplicación está activa o no. En nuestro caso de ejemplo, establezca `true`

!!! info
    Para más información, visite la guía del desarrollador de [Dynamic App](../../etendo-classic/bundles/platform/dynamic-app.md).

### Configuración de Rol
:material-menu: `Aplicación` > `Configuración General` > `Seguridad` > `Rol`

Con la sesión iniciada como el rol **Group Admin** (que es el rol por defecto para acceder a Etendo Mobile), la configuración se aplica tal y como se especifica a continuación.

![role-configuration.png](../../../assets/developer-guide/etendo-mobile/tutorials/create-new-subapplication/role-configuration.png)

!!! warning "Importante"
    Mantenga esta dynamic app como _activa_.

### Exportar el Módulo

1. Después de guardar toda la configuración, debe exportar los cambios. Abra un terminal en la raíz de su proyecto **Etendo Classic** y ejecute el siguiente comando:
    
    ``` bash title="Terminal"
    ./gradlew export.database --info
    ```

    !!!success "Importante"
        La salida debe ser un mensaje "BUILD SUCCESSFUL".

3. Se crea un nuevo módulo en la carpeta `/modules`, con la siguiente estructura

    ```
    modules
    └── com.etendoerp.subapp.product
        └── src-db 
    ```
## Servicios dockerizados
Antes de iniciar los servicios dockerizados, hay algunas configuraciones que deben realizarse en Etendo Classic.

### Configuración de la Entidad 
:material-menu: `Aplicación` > `Configuración General` > `Entidad` > `Entidad`

Es necesario configurar el token de cifrado para la autenticación en la ventana Entidad con el rol de Administrador del Sistema.  
Si el tiempo de expiración es igual a "0", los tokens no caducan.

Genere una clave aleatoria con el botón "Generar Clave".

![](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-use-secure-web-services/SWS.png)

### Ventana RX Config
:material-menu: `Aplicación` > `Etendo RX` > `RX Config`

Esta ventana de configuración almacena los datos de acceso para los servicios de Etendo RX, que son cruciales para la interacción entre diferentes servicios. En este caso, es necesario crear algunos registros.  
Con el rol `Administrador del Sistema`, en esta ventana es necesario añadir las entradas, una por cada servicio que se vaya a utilizar. Deben incluirse los siguientes campos:

- **Nombre del servicio**: el nombre de cada servicio.
- **URL del servicio**: la URL interna del servicio Docker.
- **Configuraciones actualizables**: marque esta casilla de verificación.
- **URL pública**: configure la URL accesible públicamente para el servicio.

!!!info
    El campo **URL pública** solo necesita configurarse cuando la subaplicación esté configurada para producción.

Consulte los ejemplos de configuración a continuación y replíquelos.

```
application   
auth        http://localhost:8094
config      http://localhost:8888
das         http://localhost:8092  
edge        http://localhost:8096
```

Además, en el caso de los servicios **edge** y **auth** es necesario añadir la clave de parámetro `das.url` con el valor de parámetro `http://das:8092`.

![alt text](../../../assets/developer-guide/etendo-mobile/tutorials/create-new-subapplication/rx-config.png)

!!!info 
    Si utiliza Tomcat dockerizado, las URLs dentro de la red del contenedor son `http://auth:8094`, `http://config:8888`, `http://das:8092` y `http://edge:8096`.

### Ejecutar servicios RX
Antes de continuar, es necesario iniciar los servicios de **Etendo RX**. Estos servicios proporcionan una capa de seguridad (servicio Auth) y una capa de acceso a datos (servicio Das), que son esenciales para consumir o escribir datos en Etendo y el servicio Edge. Además, al seleccionar la casilla **isReact** en el módulo definido previamente, se generará automáticamente código React, lo que permitirá un acceso a datos más sencillo.

Para lanzar todos los servicios, es necesario definir las siguientes variables de configuración en el archivo `gradle.properties`:

```groovy title="gradle.properties"
docker_com.etendoerp.etendorx=true
```

!!!info
    Para más información sobre cómo gestionar las dockerizaciones de Etendo, visite [Gestión de Docker](../../etendo-classic/bundles/platform/dependency-manager.md). 

??? Note "Tomcat y PostgresSQL dockerizados (opcional)"
    También es posible ejecutar el [servicio PostgreSQL](../platform/docker-management.md#postgres-database-service) y el [servicio Tomcat](../platform/tomcat-dockerized-service.md), añadiendo **opcionalmente** el [Platform Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=5AE4A287F2584210876230321FBEE614){target=_isblank} y las siguientes variables de configuración:

    ```groovy title="gradle.properties"
    docker_com.etendoerp.tomcat=true
    docker_com.etendoerp.docker_db=true
    ```

A continuación, para ejecutar los servicios de forma efectiva, es necesario **ejecutar el comando** en el terminal:

```bash title="Terminal"
./gradlew resources.up
```

Aquí pueden verse todos los servicios y sus respectivos logs en ejecución utilizando la herramienta [Docker Desktop](https://www.docker.com/products/docker-desktop/){target=_isblank}.

![Servicios RX en Docker](../../../assets/developer-guide/etendo-mobile/tutorials/create-new-subapplication/rx-services.png)
## Proyecciones y búsqueda

Esta sección cubre la creación de proyecciones, mapeos y búsquedas, que permiten la generación de una API REST dinámica en el servicio RX DAS. Estas configuraciones permiten leer, escribir y filtrar datos. Las proyecciones se aplican a tablas de Etendo Classic, creando un subconjunto de datos con el que se puede interactuar a través de la API.

### Crear una proyección
:material-menu: `Aplicación` > `Etendo RX` > `Projections and Mappings`

1.  Como rol `System Administrator`, es necesario crear una proyección que refleje vistas parciales de la clase Product y contenga únicamente las propiedades necesarias.

2. Para ello, iremos a la ventana `Projections and Mappings` y crearemos una nueva proyección; seleccione el módulo en desarrollo `Product SubApplication - 1.0.0 - English (USA)`, donde se exportarán estas configuraciones, y en el campo `Nombre` definimos `ProdSubApp`.

3. Ahora, con la proyección seleccionada, añadimos en la solapa `Projected Entities` dos proyecciones: una para lectura de datos, seleccionando la tabla `M_Product` y en el campo Mapping Type seleccionamos `Etendo to external system`, y otra proyección para escritura de datos, seleccionando nuevamente la tabla `M_Product` y en el campo Mapping Type `External system to Etendo`. El resto de campos se autocompletan en función de estos valores.

<figure markdown="span">
 	![projection.png](../../../assets/developer-guide/etendo-mobile/tutorials/create-new-subapplication/projections-mappings.png)
	<figcaption>Ejemplo de configuración de Proyección y Projected Entities</figcaption>
</figure>

### Creación de campos de entidad

1. Ahora, definimos qué campos queremos recuperar. Para ello, comenzamos seleccionando la proyección de lectura de datos `PRODSUBAPP - Product - Read` y ejecutamos el proceso `Create Projection Fields`; en la ventana emergente seleccionaremos los campos a proyectar. En nuestro caso de ejemplo:

    - active
    - id
    - name
    - productCategory
    - searchkey
    - taxCategory
    - UOM
    - UPCEAN

    !!! note
        Aunque no todos estos campos se mostrarán en la aplicación, como se permite la edición de registros, también estamos seleccionando todos los campos obligatorios para crear un producto.

    <figure markdown="span">
    ![create-projection-fields.png](../../../assets/developer-guide/etendo-mobile/tutorials/create-new-subapplication/create-projection-fields.png)
    <figcaption>Ejemplo de ejecución del proceso de creación de campos de la proyección de lectura</figcaption>
    </figure>

2. Ahora definimos qué campos deben guardarse al crear o editar un registro; en este caso seleccionamos la proyección de escritura ` PRODSUBAPP - Product - Write` y ejecutamos el proceso `Create Projection Fields` seleccionando los mismos campos que para la de lectura:

    - active
    - id
    - name
    - productCategory
    - searchkey
    - taxCategory
    - UOM
    - UPCEAN

    <figure markdown="span">
    ![create-projection-fields.png](../../../assets/developer-guide/etendo-mobile/tutorials/create-new-subapplication/create-projection-fields.png)
    <figcaption>Ejemplo de campos de entidad creados</figcaption>
    </figure>

3. En el caso de los campos `productCategory`, `taxCategory` y `UOM`, en la aplicación no serán editables, pero deben autocompletarse con un valor por defecto; para ello podemos usar mapeos constantes. Si se crean nuevos productos, se utilizarán estos valores por defecto.

    Para ello, vamos a la ventana `Aplicación` > `Etendo RX` > `Constant Values` y definimos IDs constantes de valores por defecto. A continuación se muestran algunos IDs de ejemplo:

    | Nombre       | Valor por defecto                      |
    | ---------------- | ------------------------------------ |
    | `ProductCategory`|`DC7F246D248B4C54BFC5744D5C27704F`    |
    | `taxCategory`    |`43A120C9377B4537B5D1976D9B1233D7`    |
    | `uOM`            |`100`                                 |
   
    <figure markdown="span">
    ![constant-values.png](../../../assets/developer-guide/etendo-mobile/tutorials/create-new-subapplication/constant-values.png) 
    <figcaption>Ejemplo de definición de valores constantes</figcaption>
    </figure>

4. Por último, seleccionando la proyección de escritura `PRODSUBAPP - Product - Write`, edite los registros `productCategory`, `taxCategory` y `UOM`, modifique el campo `Field Mapping` a `Constant Mapping`, elimine el `Jsonpath` y seleccione el valor correspondiente en la lista desplegable `Constant Value`, definida en el paso anterior.

    <figure markdown="span">
    ![constant-values-definition](../../../assets/developer-guide/etendo-mobile/tutorials/create-new-subapplication/constant-values-definition.png)
    <figcaption>Solapa de campos de entidad, ejemplo de definición de valores constantes</figcaption>
    </figure>

### Crear una búsqueda en datos proyectados

Ahora, al leer datos, es posible crear filtros; para ello debemos asociar estos filtros a una tabla y es posible exportar este filtro en el módulo en desarrollo.  
Para ello, abrimos la ventana `Tables and Columns`; en nuestro ejemplo seleccione la tabla `M_Product`, vaya a la solapa `Repository` y cree un nuevo registro con el módulo en desarrollo. A continuación, cree un nuevo registro en la solapa `Search`.

<figure markdown="span">
    ![repository.png](../../../assets/developer-guide/etendo-mobile/tutorials/create-new-subapplication/repository.png)
    <figcaption>Ejemplo de creación de Repository</figcaption>
</figure>

### Crear una nueva búsqueda y parámetro de búsqueda

A continuación, definiremos un método de búsqueda que se utilizará cuando queramos consumir los productos. Para crear este nuevo método de filtro/búsqueda, en la solapa Repository de la tabla `M_Product`, cree un nuevo registro con el nombre de método `getFilteredProducts` y el filtro de consulta hql.

```
SELECT e FROM Product e WHERE (e.active = true) AND (lower(e.name) LIKE lower('%' || :name || '%') OR lower(e.uPCEAN) LIKE lower('%' || :name || '%')) order by e.updated desc
```

Esta consulta filtra productos activos por nombre o código de barras.

Como podemos ver en la consulta, recibe el parámetro `:name` de tipo String, que definimos en la solapa `Search Parameter`.

<figure markdown="span">
    ![search-parameters.png](../../../assets/developer-guide/etendo-mobile/tutorials/create-new-subapplication/search-parameters.png)
    <figcaption>Ejemplo de creación de Search y Search Parameter</figcaption>
</figure>

### Reiniciar el servicio Etendo RX

Reinicie el servicio Das RX para que reconozca las proyecciones y los mapeos.

```bash title="Terminal"
./gradlew resources.build
```

!!! info 
    Accediendo a [http://localhost:8092/swagger-ui/index.html](http://localhost:8092/swagger-ui/index.html), se puede visualizar el Swagger del servicio RX DAS. Esta interfaz permite consultar los endpoints generados en base a las configuraciones realizadas previamente.

    ![Swagger del servicio RX DAS](../../../assets/developer-guide/etendo-mobile/tutorials/create-new-subapplication/das-api.png)
## Creación de la subaplicación

1. Ahora, cree la subaplicación basada en una plantilla publicada en NPM, [Etendo Subapp Data Template Typescript](https://www.npmjs.com/package/etendo-subapp-data-template-typescript){target="_blank"}. Ejecute el comando de Gradle para crear automáticamente la subaplicación dentro del módulo en desarrollo.

    ``` bash title="Terminal"
    ./gradlew subapp.create -Ppkg=<javapackage> --info
    ```
    En el ejemplo en el que estamos trabajando, utilice el siguiente comando:

    ```bash title="Terminal"
    ./gradlew subapp.create -Ppkg=com.etendoerp.subapp.product --info
    ```
    
    Se creará una nueva subaplicación dentro del módulo, con la siguiente estructura:

    ```
    modules
    └── com.etendoerp.subapp.product
      ├── src-db 
      └── subapp
          ├── .bundle
          ├── _tests_
          ├── android
          ├── ios
          ├── lib
          ├── node_modules
          └── src
          └── App.tsx
    ```
## Ejemplo de Subapp de Producto
Esta sección ofrece una visión general sobre las pantallas del ejemplo de subaplicación de producto y las partes principales de la subaplicación.

!!! info "Consideración"
    Las aplicaciones deben desarrollarse para ambas plataformas: teléfono y tablet. 
   
### Pantalla de Inicio 
 
- Esta es la pantalla principal de la subaplicación. Mostrará una lista de productos. Además, permitirá editar y eliminar un producto, buscar un producto por nombre y navegar al detalle de un producto.

**Vista de Teléfono**
<figure markdown>
![home-screen.png](../../../assets/developer-guide/etendo-mobile/tutorials/create-new-subapplication/home.jpg){ width="300", align=left } 
![remove-product.png](../../../assets/developer-guide/etendo-mobile/tutorials/create-new-subapplication/delete-product.jpg){ width="300", align=right}
</figure>
**Vista de Tablet**
![home-screen-tablet.png](../../../assets/developer-guide/etendo-mobile/tutorials/create-new-subapplication/home-tablet.jpg)


- La ruta a esta pantalla es `src/screens/home/index.tsx` y el contenido:

``` javascript title="src/screens/home/index.tsx"
import React from 'react';
import TableList from '../../components/table/list';
import { NavigationProp } from '@react-navigation/native';
import { INavigationContainerProps } from '../../interfaces';
import locale from '../../localization/locale';
import useProduct from '../../lib/data_gen/useProduct';
import { Product } from '../../lib/data_gen/product.types';

interface TableListProps {
  navigation: NavigationProp<any>;
  route: any;
  navigationContainer: INavigationContainerProps;
}

const Home = (props: TableListProps) => {
  const { getFilteredProducts, updateProduct } = useProduct();
  return (
    <TableList
      deleteDataItem={async (item: Product) => {
        item.active = false;
        await updateProduct(item);
      }}
      {...props}
      columns={[
        {
          key: 'id',
          primary: true,
          visible: false,
        },
        {
          key: 'name',
          label: locale.t('Table.products'),
          visible: true,
          width: '50%',
        },
        {
          key: 'uPCEAN',
          label: locale.t('Table.barcode'),
          visible: true,
          width: '30%',
        },
      ]}
      getData={getFilteredProducts}
      labels={{
        dataName: 'Product',
        navbarTitle: locale.t('Home.welcome'),
        containerTitle: locale.t('Home.productList'),
        buttonNew: locale.t('Home.newProduct'),
        searchPlaceholder: locale.t('Home.typeProduct'),
        successfulDelete: locale.t('Success.deleteProduct'),
        errorDelete: locale.t('Error.deleteProduct'),
      }}
    />
  );
};

export default Home;
```

### Detalle de Producto

![product detail](../../../assets/developer-guide/etendo-mobile/tutorials/create-new-subapplication/product-detail.jpg){ width="300"}

- Esta pantalla mostrará el detalle de un producto. Además, permitirá editar el producto.
- Es la misma pantalla utilizada para crear un nuevo producto, si la prop no tiene ID.
- La ruta a esta pantalla es `src/screens/productDetail/index.tsx`, añada el contenido:

``` javascript title="src/screens/productDetail/index.tsx"
import React, { useState } from 'react';
import TableDetail from '../../components/table/detail';
import { NavigationProp } from '@react-navigation/native';
import locale from '../../localization/locale';
import useProduct from '../../lib/data_gen/useProduct';

interface TableDetailProps {
  navigation: NavigationProp<any>;
  route: any;
}

const ProductDetail = (props: TableDetailProps) => {
  const { createProduct, updateProduct } = useProduct();
  const [id, setId] = useState<string>('');
  const [searchKey, setSearchKey] = useState<string>('');
  const [name, setName] = useState<string>('');
  const [uPCEAN, setUPCEAN] = useState<string>('');
  return (
    <TableDetail
      {...props}
      createData={async () => {
        await createProduct({ searchKey, name, uPCEAN });
      }}
      updateData={async () => {
        await updateProduct({ id, searchKey, name, uPCEAN });
      }}
      fields={[
        {
          key: 'id',
          visible: false,
          setValue: setId,
          getValue: id,
          labels: {
            title: '',
            placeholder: '',
          },
        },
        {
          key: 'searchKey',
          setValue: setSearchKey,
          getValue: searchKey,
          labels: {
            title: locale.t('ProductDetail.searchKey'),
            placeholder: locale.t('ProductDetail.searchKeyExample'),
          },
        },
        {
          key: 'name',
          setValue: setName,
          getValue: name,
          labels: {
            title: locale.t('ProductDetail.products'),
            placeholder: locale.t('ProductDetail.nameExample'),
          },
        },
        {
          key: 'barcode',
          setValue: setUPCEAN,
          getValue: uPCEAN,
          labels: {
            title: locale.t('ProductDetail.barcode'),
            placeholder: locale.t('ProductDetail.barcodePlaceholder'),
          },
        },
      ]}
      labels={{
        editTitle: locale.t('ProductDetail.editProduct'),
        newTitle: locale.t('ProductDetail.newProduct'),
        errorTitle: locale.t('Error.product'),
        successUpdateTitle: locale.t('Success.updateProduct'),
        successCreateTitle: locale.t('Success.saveProduct'),
        connectionError: locale.t('Error.connection'),
        navbarTitle: locale.t('Home.welcome'),
        cancel: locale.t('Common.cancel'),
        save: locale.t('Common.save'),
        successTitle: id
          ? locale.t('Success.updateProduct')
          : locale.t('Success.createProduct'),
      }}
    />
  );
};

export default ProductDetail;

```
    
### Navegación 

Además, es necesario añadir la configuración de navegación en el archivo `app.tsx`, en la sentencia return. Esta configuración proporciona la infraestructura para navegar entre las diferentes pantallas de la aplicación.

``` javascript title="App.tsx"
<Stack.Navigator initialRouteName="Home">
      <Stack.Screen
        options={{ headerShown: false }}
        name="Home"
        initialParams={{ dataUser }}>
        {props => <Home {...props} navigationContainer={navigationContainer} />}
      </Stack.Screen>
      <Stack.Screen
        options={{ headerShown: false }}
        name="ProductDetail"
        initialParams={{ dataUser }}>
        {props => <ProductDetail {...props} />}
      </Stack.Screen>
</Stack.Navigator>
```

!!! info 
    Para más información, visite el concepto [Navigation Stack](../concepts/subapp-structure.md#navigation-stack) en la página Estructura de la Subaplicación.

!!! info 
    Para más información sobre la gestión del idioma y las traducciones, visite el concepto [Languague](../concepts/subapp-structure.md#language).

!!! info 
    Para más información sobre los parámetros de la subaplicación, visite el concepto [Params from Etendo Mobile](../concepts/subapp-structure.md#params-from-etendo-mobile).

### Ejecución de la Subaplicación
1. Una vez creada la subaplicación, debe generarse el código react-native, con tipos y funciones que interactúan con el servicio RX DAS. Para ello, ejecute el comando de Gradle: 

    !!! info
        Asegúrese de que los servicios de Etendo RX estén en ejecución y sin errores antes de ejecutar este comando.

    ``` bash title="Terminal"
    ./gradlew subapp.build -Ppkg=<javapackage> 
    ```

    En nuestro caso de ejemplo: 
    ``` bash title="Terminal"
    ./gradlew subapp.build -Ppkg=com.etendoerp.subapp.product --info
    ```
    Como podemos ver, se generarán en la carpeta `/subapp/src/libs/` las funciones y los tipos que se utilizarán para leer y escribir datos `GET` y `POST`.

    ```
    modules
    └── com.etendoerp.subapp.product
      ├── src-db 
      └── subapp
          └── src
            └── lib
                └── base
                    └── baseservice.ts
                    └── baseservice.types.ts
                └── data_gen
                    └── product.types.ts
                    └── productservice.ts
                    └── useProduct.ts      
    ```

2. En un terminal en la ruta `modules/<javapackage>/subapp`, instale las dependencias declaradas en el `package.json`, siguiendo el comando: 

    ``` bash title="Terminal"
    yarn install 
    ```

3. A continuación, para ejecutar la subaplicación en modo de desarrollo, ejecute: 

    ``` bash title="Terminal"
    yarn dev 
    ```
    !!! note
        Por defecto, la aplicación se ejecuta en modo de desarrollo en `localhost` en el puerto `3000`. Además, los cambios en el directorio `/src` se escanean automáticamente, habilitando actualizaciones dinámicas de la aplicación durante el desarrollo. Esto garantiza que cualquier modificación se refleje en tiempo real sin reiniciar la aplicación.


### Visualización de las subaplicaciones

1. Abra la aplicación [Etendo Mobile](../../../user-guide/etendo-mobile/getting-started.md) en un dispositivo móvil. Puede utilizar un emulador o un dispositivo físico.
    
2. En la configuración de Etendo Mobile, configure la URL del servicio Edge (Edge es un servicio de Etendo RX, que implementa un gateway impulsado por Spring Cloud). Por defecto, la URL del entorno debería ser `http://<local-network-ip>:8096/` y la ruta de contexto por defecto `/etendo`.

    !!! info
        Para averiguar su dirección IP en la red local, puede ejecutar el comando `ifconfig` en un terminal de Mac o Linux, o `ipconfig` en Windows CMD.
  
    ![ip-config](../../../assets/developer-guide/etendo-mobile/tutorials/create-new-subapplication/ip-config.png)

3. Inicie sesión en Etendo Mobile y verá la lista de subapps. Al hacer clic en `Product Subapp` accederá a la aplicación en modo de desarrollo.
    ![app-home.png](../../../assets/developer-guide/etendo-mobile/tutorials/create-new-subapplication/app-home.png)

4. Ahora puede ver, filtrar, crear, editar y eliminar productos.
## Recepción de archivos compartidos desde Etendo Mobile

En esta sección, explicaremos cómo recibir archivos externos desde otra aplicación en **Etendo Mobile**, utilizando como ejemplo la subaplicación [Subapp Documents Manager](../../../user-guide/etendo-mobile/bundles/mobile-extensions/overview.md#documents-manager-subapp).

!!! warning "Importante"
    Asegúrese de que la casilla de verificación **Recibir archivos externos** esté configurada en `true` en la ventana **Dynamic App**. Esto es crucial para que la subaplicación aparezca como una opción al compartir archivos externos.
    ![configuration-docsmanager.png](../../../assets/developer-guide/etendo-classic/bundles/platform/dynamic-app/dynamic-app.png)
    
El parámetro `sharedFiles` se pasa a la subaplicación y se utiliza para procesar los archivos recibidos.

!!! info 
    Para más información, visite el repositorio de [Subapp Documents Manager](https://github.com/etendosoftware/com.etendoerp.subapp.docsmanager){target=“_blank”}. Allí encontrará un ejemplo de subaplicación y la explicación de cómo implementar la funcionalidad de compartición de archivos en su propia aplicación.
## Registro de depuración

Esta sección explica cómo registrar datos en una subaplicación utilizando la función de utilidad `logger`. Para registrar cualquier información, llame a la función `logger` con una clave y un valor:

```javascript
logger('key', value );

```

**Importación de la función Logger**  
Para utilizar el logger en cualquier archivo, impórtelo de la siguiente manera:

``` javascript
import logger from '../../utils/log'; // The path to the file is relative 

```

!!!info "Conversión automática a cadena"
    Los objetos pasados a la función `logger` se convertirán automáticamente a cadenas utilizando la función `JSON.stringify`. Esto garantiza la compatibilidad con el mecanismo de registro.

**Ejemplo de uso**  
A continuación se muestra un ejemplo de cómo utilizar la función logger, incluyendo el manejo de errores:

``` javascript
try {
  // Your code here
} catch (err) {
  logger('Handle Error', err));
  showAlert(labels.connectionError, 'error');
}
```

En este ejemplo:

- El objeto de error `err` se convierte automáticamente a un `String` utilizando `JSON.stringify` y se registra.
- Se muestra una alerta utilizando el componente `showAlert` para informar al usuario de un error de conexión.

Al integrar esta utilidad de registro, los desarrolladores pueden realizar un seguimiento del comportamiento de la aplicación y depurar de forma más eficaz.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.