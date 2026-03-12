---
tags: 
  - Cómo hacer
  - Crear página
  - Página de documentación
  - Estilo
  - Formato
---

# Cómo crear una página en la documentación de Etendo

## Visión general
Esta guía contiene reglas básicas, consejos y sugerencias para las personas que tengan la intención de desarrollar documentación para Etendo. Cuando diferentes documentos utilizan las mismas directrices, son más fáciles de usar, más consistentes y más simples de combinar y reutilizar. Por lo tanto, se recomienda encarecidamente a todos los colaboradores que sigan estas directrices en beneficio de los lectores.


## Requisitos
- Versión de Python ^3.11. Para instalarla, siga [la guía de instalación de Python](https://www.python.org/downloads/){target="\_blank"}.


## Pasos

1. Clone el repositorio [docs](https://github.com/etendosoftware/docs){target="\_blank"} 
	
    ```bash title="Terminal" 
    git clone git@github.com:etendosoftware/docs.git
    ```

2. Instale las dependencias

    ```bash title="Terminal" 
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Cree una nueva rama con [GitFlow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow){target="\_blank"}, donde se almacenan las páginas, los activos y las configuraciones relacionadas.

    ```bash title="Terminal" 
	# This command should be executed only the first time after cloning the repository.
	git flow init 
    ```

    ```bash title="Terminal" 
    git flow feature start <task key>
    ```

4. Para ejecutar la documentación de Etendo localmente, ejecute:

    ```bash title="Terminal"
    source venv/bin/activate
    mkdocs serve
    ```

5. La documentación de Etendo está estructurada en secciones; en general, las secciones donde se encuentra la mayor parte de la documentación son la guía de usuario y la guía del desarrollador. Dentro de estas, hay subsecciones según productos y categorías; debe decidir la ubicación dentro de la estructura y crear un archivo con el formato `.md`; el nombre debe estar en minúsculas y separado por guiones. 

    ``` title="Estructura de la documentación" 
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

    Para mostrar la página en el menú, añada esta página en el archivo `mkdocs.yml` en la sección **nav**.
    
    !!!important
        - Al añadir páginas a la estructura de navegación, recuerde organizarlas en orden alfabético.
        - La estructura de directorios y la estructura de navegación deben ser las mismas.

    Ejemplo

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

    La documentación debe elaborarse siguiendo el [formato de página](#formato-de-página) descrito en la siguiente sección.

    Una vez finalizada la documentación:


6. Cree una PR a `develop` con todos los cambios relacionados.
7. Una vez resueltos todos los comentarios y con dos aprobaciones, fusione la PR.
8. Una nueva versión de la documentación se desplegará automáticamente en [https://docs.etendo.software](https://docs.etendo.software){target="\_blank"}.

## Formato de página

### Estructura de la página

```
---
tags: 
  - Ejemplo de etiqueta 1
  - Ejemplo de etiqueta 2
---
 
# Tratamientos
  
## Visión general


(Descripción general de la sección)


## Tratamientos 1


### Subtítulo
```
!!!note
    Añada la siguiente declaración de licencia como pie de página en todas las páginas de la documentación de Etendo producidas internamente:
    ```
    ---
    
    This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}. 

    ```

### Referencias útiles

#### Negrita

Úsela con moderación para dar énfasis o para resaltar nombres de opciones; por ejemplo:
Desde la ventana **Pedido de venta**, seleccione **Nuevo**

```
**Negrita**
```

Esto se muestra como: **Negrita**

#### Cursiva 

Úsela al citar un fragmento de texto de otra fuente, un fragmento de texto en otro idioma o para dar un ejemplo, como texto de muestra que se debe escribir en un campo de texto.

```
*Cursiva*
```

Esto se muestra como: *Cursiva*

#### Backticks

Úselos para referirse a rutas, código en línea y para la navegación por menús. Por ejemplo:

- Ruta:
    ```
    `/directory/filename.txt`
    ```
    Esto se muestra como: `/directory/filename.txt`
- Código en línea:
    ```
    `./gradlew update.database --info`
    ```
    Esto se muestra como: `./gradlew update.database --info`

- Navegación por menús:
    ```
    `Document`>`New`>`Template`
    ```              
    Esto se muestra como: `Document`>`New`>`Template`

#### Admonitions

Los admonitions se utilizan para incluir contenido adicional sin interrumpir el flujo de la página. Como se muestra a continuación, existen diferentes tipos: 

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
Esto se muestra como:

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

También es posible editar el título del bloque de cita añadiendo:

```
!!!failure "Ejemplo de título editado"
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.
```
Esto se muestra como:

!!!failure "Edited title example"
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

Para más información, visite [Admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/){target="\_blank"}.

#### Pestañas de contenido

Al documentar una funcionalidad con diferentes opciones (JAR o Source, Windows o Linux, C o C++ por ejemplo), utilice las siguientes pestañas para incluir información relevante para cada opción. Los lectores pueden entonces elegir la pestaña correspondiente con la información necesaria y omitir la lectura de información no relevante.

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
Esto se muestra como:

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

#### Estructura de directorios

Para la estructura de directorios, es necesario aplicar el siguiente formato:

```
modules
└── org.openbravo.localization.spain.referencedata.taxes
    └── referencedata 
        └── standard
            ├── Impuestos_ES.xml
            └── Spanish_Tax_Alerts.xml
```


#### Enlaces externos

Para incluir enlaces externos en la documentación, utilice el siguiente formato de ruta: 

```
[Ejemplo de Google](https://google.com){target="_blank"}
```

Esto se muestra como: [Google Example](https://google.com){target="_blank"} 

#### Enlaces internos (Redirección)

Para incluir enlaces internos, utilice las rutas relativas desde la página actual, como en el siguiente ejemplo:

```
[Enlace interno](../../how-to-guides/example-page.md)
```

Esto se muestra como: [Internal Link](../../how-to-guides/example-page.md)

También es posible referirse a una sección específica dentro de una página usando

```
[Sección específica](../../how-to-guides/example-page.md#specific-section)
```

Esto se muestra como: [Specific section](../../how-to-guides/example-page.md#specific-section)

#### Lista

Para incluir listas en la documentación, utilice los siguientes formatos:

Viñetas:

```
Lista:

- Viñeta a
- Viñeta b
```

Esto se muestra como:

Lista:

- Viñeta a
- Viñeta b

Lista numerada:

```
Lista:

1. Opción numerada 1
    - elemento 1
    - elemento 2
2. Opción numerada 2
```
Esto se muestra como:

Lista:

1. Numbered option 1
    - item 1
    - item 2
2. Numbered option 2

!!!info
    Recuerde que respetar las tabulaciones es esencial para la continuidad de las listas; esto significa que el contenido de diferentes elementos debe estar tabulado.  

#### Imagen

Para incluir imágenes en la documentación, utilice las rutas relativas desde la página actual con el siguiente formato: 

```
![](../../assets/developer-guide/how-to-guides/new-page/new-image.png)
```

!!!info
    Recuerde subir la imagen a la carpeta **activos** con la ubicación específica correspondiente.

Por ejemplo, si la ubicación de la imagen es `developer-guide`> `how-to-guides` >`new-page`, la ubicación de la imagen debería ser:

```

 assets 
    └── developer-guide
         └── how-to-guides
                └── new-page
                    └── new-image.png
```
#### Más referencias

Para más información sobre mkdocs, visite [Referencia de Mkdocs](https://squidfunk.github.io/mkdocs-material/reference){target="_blank"}.

## Reglas de redacción

### Manténgalo simple
Utilice frases cortas y puntuación para mantener las ideas claras y simples. Introduzca una única idea, concepto o acción por frase.

- **Incorrecto**<br>
*El módulo de fabricación permite a los usuarios definir los planes de proceso, los requisitos de trabajo y los esfuerzos de trabajo; así es como funcionan los procesos que producen bienes intermedios y finales.*

- **Correcto**<br>
*El módulo de fabricación permite a los usuarios definir los planes de proceso, los requisitos de trabajo y los esfuerzos de trabajo. Esta sección describe cómo funcionan los procesos que producen bienes intermedios y finales.*


### Tiempos verbales
Utilice siempre el tiempo presente. Evite los tiempos pasado o futuro si es posible.
Además, intente abstenerse de usar must, have to, need to, will, should y formas similares.
Tenga en cuenta que un manual describe procedimientos obligatorios que se deben seguir para completar una determinada tarea.

- **Incorrecto**<br>
*Tendrá que pulsar Intro para reiniciar el sistema.*
- **Correcto**<br> 
*Pulse Intro para reiniciar el sistema.*


### Use la tercera persona
*Cuando sea posible, utilice el imperativo en tercera persona.* 

- **Incorrecto**<br>
*Debería ejecutar el script de instalación*
- **Correcto**<br>
*Ejecute el script de instalación*

Sin embargo, siempre que no se abuse, se acepta dirigirse al usuario directamente usando *usted* si hace que la documentación sea más fácil de seguir o usar *el usuario* cuando sea necesario.

### Evite la discriminación de género
Los lectores de documentación de software son hombres y mujeres. Evite usar expresiones que se refieran a formas de género específicas.
Puede evitar las formas de género o usar *they*/*their* como pronombre genérico de tercera persona del singular para referirse a una persona cuyo género es desconocido o irrelevante para el contexto de uso.

- **Incorrecto**<br>
*Cada usuario tiene su directorio de inicio (masculino).*

- **Correcto**<br>
*Cada usuario tiene un directorio de inicio.*<br>
*Cada usuario tiene su directorio de inicio.*


### Describa únicamente la funcionalidad actual
Evite hablar sobre funcionalidades o planes futuros para un producto o una aplicación.

- **Incorrecto**<br>
*Los gráficos se pueden guardar como una imagen GIF. Se añadirá soporte para nuevos formatos en versiones futuras.*

- **Correcto**<br>
*Los gráficos se pueden guardar como una imagen GIF.*


### Redacción para una audiencia global
Tenga en cuenta que personas de todo el mundo pueden utilizar Etendo y su documentación relacionada.
Algunas recomendaciones importantes:

- Evite usar nombres de personas, direcciones y otra información de ejemplo que no sea común en el idioma inglés.
- Recuerde que las monedas y los formatos para representar fechas y números no son los mismos en todas las partes del mundo.

### Otras convenciones

- Si tiene una lista de elementos (por ejemplo, una lista de archivos para descargar), ordénelos alfabéticamente a menos que exista un orden lógico más evidente.
- No utilice contracciones (don't, you're, etc).

---

Este trabajo es una obra derivada de [Guía de estilo de documentación](https://wiki.openbravo.com/wiki/Documentation_Style_Guide){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.