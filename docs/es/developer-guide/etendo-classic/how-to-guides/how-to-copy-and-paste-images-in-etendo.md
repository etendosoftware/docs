---
title: Cómo copiar y pegar imágenes en Etendo
tags:
    - Cómo hacer
    - Copiar imágenes
    - Pegar imágenes
    - Texto enriquecido
    - Base64
---
## Cómo copiar y pegar imágenes en Etendo

### Visión general

Esta sección explica cómo utilizar áreas de texto enriquecido para guardar imágenes en Etendo.

### Cómo incluir imágenes con áreas de texto enriquecido

En primer lugar, el usuario debe definir una columna en la base de datos donde se guarde la imagen correspondiente.

!!! info
    Para ello, es importante recordar que esta columna debe tener el tamaño suficiente para almacenar una imagen codificada en formato base64. Por ejemplo: una imagen de 2 MB contiene 3 millones de caracteres.


![](../../../assets/drive/wO0NOA64kTnYqRjQ8KTrcBJiMmq2AGvuS6oYHOQ75hZ13OvUYgFkAK2S7iE-SGeRh5PcE5eNA8rgbpzg0LwgGGh-R4fk1yHCI9orYLKJJXDD9noH4K0ernCNFMkZCKBo_4owHCPkqrpxgOcFN2NjHMI0NchPj0r1VminCsMvbp0begvcFdO8FI8DjE5jAA.png)

Una vez definida la columna, el usuario debe iniciar sesión con el rol de Administrador del sistema, ir a Diccionario de aplicación | Ventanas, Tablas y Columnas, buscar la tabla correspondiente, en nuestro caso “producto”, y crear columnas desde la base de datos con el botón “Crear columna desde BD”. 

En la columna creada recientemente, debe seleccionarse la referencia “área de texto enriquecido”. 

Además, debe crearse un campo para la imagen correspondiente. 

Por último, es necesario compilar ejecutando:

```bash title="Terminal"
./gradlew smartbuild
```


![](../../../assets/drive/zd0NYsbcmx0ehnHRsCxb21zazxL6sYuBxqjAOoH74QmK1CTccI-dDyqzmMrTiJDrusrcdifTRiiCPPomRAdduh1LipsA2FHTP84kstjAI8SwL3a7-DkSSmCqbVYsyXF_d1El8Z9QqPqphc4oqIB-wFYadh3OODSzp8QCHSyGBAGZSX8OczGKNApmreM8eg.png)

Como se observa en la imagen anterior, se creó el campo “imagen”, en el que es posible pegar contenido para almacenarlo en formato base64 en la base de datos. De este modo, esta información queda disponible para su uso posterior.

---
Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L](https://etendo.software){target="_blank"}.