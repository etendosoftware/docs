---
title: Cuadrícula y formularios

tags:
    - Vista de cuadrícula
    - Vista de formulario
    - Filtrado de datos
    - Personalización del usuario
    - Atajos de teclado
---
## Vista de cuadrícula y formulario

Etendo permite la personalización de las vistas de cuadrícula y de formulario. Las ventanas personalizadas y las vistas de formulario se almacenan una vez guardadas en la ventana Personalización de ventana.

### Vista de cuadrícula

![Ejemplo de vista de cuadrícula](../../assets/drive/1Fc2LfvRYeixaOCFt6qKl-GG4ycr0tyhR.png)

### Vista de formulario

![Ejemplo de vista de formulario](../../assets/drive/1BFjhtuYG6q5bsfwuSCVt_c4qmaj46vdY.png)

### Mostrar tabla y formulario

Con este botón ![](../../assets/getting-started/user-interface/grid-and-forms/tandf.png) en la barra de herramientas, el usuario puede disponer tanto de la vista de cuadrícula como de la vista de formulario del mismo registro y utilizarlas de forma más eficiente.

![](../../assets/getting-started/user-interface/grid-and-forms/tableandform.png)

## Vista de cuadrícula

La vista de cuadrícula funciona como la vista base y, a menudo, como punto de partida para filtrar y profundizar. El usuario puede abrir un registro en la vista de formulario sobre la cuadrícula. La metáfora de interacción utilizada es la de un explorador de archivos de un sistema operativo. La cuadrícula es la carpeta con archivos; un doble clic abre el registro. El registro en vista de formulario puede cerrarse en cualquier momento haciendo clic en el botón de cierre (X) en la esquina superior derecha del formulario.

Un registro (vista de formulario) en la cuadrícula puede abrirse mediante:

-   Un doble clic en la fila.
-   Pulsando ENTER en el teclado.
-   Haciendo clic en el icono de formulario/documento en el lado izquierdo de la fila.

### Filtrado de columnas

En la parte superior de las columnas de una cuadrícula, el usuario encontrará filtros de columna. Estos filtros pueden aplicarse para encontrar registros específicos. Existen varios tipos de filtros de columna:

-   Filtros de columna normales: son campos que están vacíos por defecto, pero una vez que el usuario empieza a escribir los primeros caracteres de un término de búsqueda, la cuadrícula se filtrará en tiempo real.
-   Filtros de columna de fecha: al hacer clic se abrirá un diálogo donde el usuario puede establecer un rango, por ejemplo, *hace 8 días hasta hoy*.
-   Filtros de columna de referencia desplegable: filtran referencias a otros datos, por ejemplo, de un pedido de venta a un tercero. Puede filtrar por múltiples valores; si hay muchos valores por los que filtrar, puede desplazarse en el cuadro desplegable.
-   Filtros de columna desplegable: filtros que contienen un conjunto limitado de valores. Solo tiene que abrir el desplegable y seleccionar un valor. 

![Filtrado](../../assets/drive/1kul74WVN4g1YXarFm12iaPTJNpC0YfCw.png)

Los siguientes símbolos pueden utilizarse en los campos de filtro de columna normales para crear expresiones de filtro más complejas. Tenga en cuenta que, una vez que empiece a escribir una expresión de filtro en una columna de valor numérico, el filtrado en tiempo real se desactiva y deberá pulsar Enter para aplicar el filtro.

|     |     |     |     |
| --- | --- | --- | --- |
| **Símbolo** | **Filtro** | **Ejemplo** | **Significado** |
| <   | menor que (también funciona para cadenas) | <100 | Solo muestra importes inferiores a 100 |
| \>  | mayor que (también funciona para cadenas) | \>100 | Solo muestra importes superiores a 100 |
| !   | distinto de (también funciona para cadenas) | !100 | Muestra todo excepto los importes que sean iguales a 100 |
| ^   | empieza por | ^H  | Solo muestra valores que empiezan por "H" |
| \|  | termina en | H   | Solo muestra valores que terminan en "H" |
| !^  | no empieza por | !^H | Solo muestra valores que no empiezan por "H" |
| !@  | no termina en | !@H | Solo muestra valores que no terminan en "H" |
| ~   | contiene (este es el valor por defecto para la mayoría de los filtros de columna) | ~buenas | Solo muestra valores que contienen "buenas" |
| !~  | no contiene | !~buenas | Solo muestra valores que no contienen "buenas" |
| ##   | es Nulo | ##   | Solo muestra registros sin valor en esta columna (funciona en filtros de columna normales y de fecha) |
| !##  | no es Nulo | !##  | Solo muestra registros con un valor en esta columna (funciona en filtros de columna normales y de fecha) |
| \== | coincidencia exacta (para campos donde 'contiene' es el valor por defecto) | \==FV/1 | Solo muestra valores que sean exactamente iguales a "FV/1" |
| a...b | rango (entre a y b) | 0...100 | Solo muestra valores entre 0 y 100. |
| or  | booleano OR | cheque or efectivo | Solo muestra registros que contienen "cheque" o "efectivo". Tenga en cuenta que, si desea usar el término 'or' como valor de filtro, debe anteponerle una '\\'. Por tanto, para obtener todos los registros que contengan el valor 'or', filtre usando este valor: \\or. |
| and | booleano AND | cheque and efectivo | Solo muestra registros que contienen "cheque" y "efectivo". Tenga en cuenta que, si desea usar el término 'and' como valor de filtro, debe anteponerle una '\\'. Por tanto, para obtener todos los registros que contengan el valor 'and', filtre usando este valor: \\and. |

Los filtros pueden borrarse haciendo clic en el icono de embudo en la parte superior derecha de la cuadrícula.

### Clic derecho

El clic derecho puede utilizarse para encontrar más opciones sobre cualquier sección de la vista de cuadrícula. En este menú desplegable se muestran los atajos de teclado, se pueden añadir columnas a la vista y se pueden encontrar opciones de resumen.

![Opciones de clic derecho](../../assets/drive/1QNBKfBUaLNkhLHC6Y7G8GYcOReRcHMzZ.png)

### Procesamiento masivo

Etendo permite al usuario procesar registros de forma masiva. Este motor de procesos permite al usuario seleccionar una entidad de entrada, crear criterios para obtener resultados, ejecutar acciones para la entrada o definir una salida que posteriormente puede utilizarse como entrada para otras acciones. 

![](../../assets/getting-started/user-interface/grid-and-forms/bulkposting.gif)
                                    
!!!info
    Las acciones de documento mostradas al seleccionar más de un documento serán todas las disponibles en función de los estados de los registros seleccionados, dependiendo del tipo de documento que se esté seleccionando.

### Guardar vista

Guardar vista almacena la configuración de la cuadrícula y del formulario, los filtros de columna e incluso toda la disposición de la pantalla; por ejemplo, la posición de la barra divisoria entre la cabecera y las líneas. Con esta opción, el usuario puede reorganizar la cuadrícula, adaptarla a su tarea y guardar esta vista para abrirla en otro momento. El usuario puede acceder a las vistas guardadas a través de un menú desplegable situado debajo del botón Guardar vista en la barra de herramientas.

![](../../assets/getting-started/user-interface/grid-and-forms/saveview.png)

Una vista guardada puede establecerse como predeterminada y puede eliminarse. La vista activa se indica mediante una pequeña flecha delante del nombre de la vista.

!!!info
    Como administrador, puede guardar vistas predefinidas en diferentes niveles (cliente, organización, rol) que se ponen a disposición de los usuarios. Como usuario normal, solo puede editar/guardar vistas en sus propios niveles y no cambiar las vistas introducidas por un administrador.

### Atajos de teclado

|     |     |
| --- | --- |
| **Atajo** | **Acción** |
| Ctrl + Shift + f | Saltar a los filtros de columna |
| Esc | Vuelve a la cuadrícula manteniendo el valor del filtro |
| Alt + Del | Borrar filtros de columna |
| Ctrl + i | Insertar fila |
| Del | Eliminar fila |
| F2  | Editar fila |
| Ctrl + F2 | Cambiar a vista de formulario (mientras se edita) |
| Enter | Abrir fila (en vista de formulario) |
| Ctrl + Alt + Shift + <Letter> | Ejecutar proceso (botones amarillos) |
| Esc | Cancelar edición |

## Vista de formulario

En la vista de formulario, el usuario tiene acceso a información detallada sobre cada registro.

En esta vista, cada título de campo puede ir seguido de dos iconos diferentes:

|     |     |
| --- | --- |
| ![Icono de flecha](../../assets/drive/1sK4lTD4FNi3-WZDkGzPpE3Px7brhZZWd.png) | Al hacer clic aquí, el usuario puede abrir una nueva solapa con información más específica. 
| ![Icono de asterisco](../../assets/drive/15aZZ-UGcGfakPeYAImHnx4gRwRp2fmP6.png) | Esto muestra que el campo es obligatorio de completar. El campo tiene un fondo amarillo. 

### Personalización de formulario

Este botón en la barra de herramientas ![](../../assets/getting-started/user-interface/grid-and-forms/logo.png) permite al usuario personalizar formularios para incluir los campos y funcionalidades necesarios que mejor se adapten a sus necesidades.

![](../../assets/getting-started/user-interface/grid-and-forms/formpersonalization.png)

### Mensajes de usuario

Los mensajes de usuario se muestran en la parte superior de la vista y su función es informar o advertir al usuario sobre una excepción, error u otra situación en la aplicación que requiera la atención del usuario. Existen cuatro tipos diferentes de mensajes de usuario.

**Información:** este tipo de mensaje se utiliza para comunicar información interesante pero no esencial.

![Mensaje de información](../../assets/drive/1atlScOy_dksTaOEundWmIu203B7jO02D.png)

**Éxito:** este tipo de mensaje se muestra tras la ejecución correcta de un proceso.

![Mensaje de éxito](../../assets/drive/1wus0cnCi2Ou9eQ1eIADpTQ0SVOAuSMGS.png)

**Error:** este tipo de mensaje se utiliza para excepciones y errores. Un caso típico es un proceso que no se ejecutó correctamente.

![Mensaje de error](../../assets/drive/1yKisLYaiB95bt1wRMLXNhprmONuf7NQR.png)

**Advertencia:** este tipo de mensaje se utiliza para informar al usuario sobre un estado o evento del sistema que podría causar un problema.

![Mensaje de advertencia](../../assets/drive/19f47PVut5FN5_iXv_RszQsO28MvmWyqT.png)

### Barra de estado

La barra de estado transmite el estado de edición del documento (Nuevo, Editando o Guardado) junto con un conjunto de atributos de solo lectura definidos por el usuario. Estos permiten al usuario obtener una visión general del documento sin tener que revisar el resto del formulario. La barra de estado solo es visible en la vista de formulario.

![Barra de estado](../../assets/drive/1d5GpX_oOyNMvqvy94JBtOeg4FJnWSZZI.png)

|     |     |
| --- | --- |
| 1   | Estado |
| 2   | Botones |

En el lado derecho de la barra de estado, están disponibles los siguientes botones:

|     |     |
| --- | --- |
| ![Navegar al registro anterior](../../assets/drive/1jP4R73D1bYKd-qSAiRwK2HH0NKmODj-4.png) | Navegar al siguiente registro 
| ![Navegar al registro anterior](../../assets/drive/1YeC8yk9CzwM5hTScn4JNIcvA44ut80vq.png) | Navegar al registro anterior 
| ![Maximizar formulario](../../assets/drive/1xRCMAPS6c3GyMd4ygc5TbULgR7TUkX1Q.png) | Maximizar formulario 
| ![Restaurar tamaño](../../assets/drive/1fiogmu4e5r1nP5g0Aa7L8dFfZG2xcvzF.png) | Restaurar el formulario al tamaño anterior 
| ![Cerrar formulario](../../assets/drive/1KU3xBqPUVQKl43Je-S9ij3Vr031G2LCf.png) | Cerrar formulario (guardar y volver a la cuadrícula.png) |

### Atajos de teclado

|     |     |
| --- | --- |
| **Atajo** | **Acción** |
| Alt + ArrowDown | Abrir desplegable |
| Space | Una vez abierta una lista desplegable de selección múltiple, (des)selecciona el elemento enfocado. Se utiliza en referencias FK y de lista en el filtro de cuadrícula |
| Ctrl + Enter | Abrir selector |
| Ctrl + Alt + Enter | Abrir en solapa ("enlace externo") |
| Alt + Shift + Enter | Maximizar o restaurar la vista de formulario |
| Ctrl + Shift + x | Guardar y cerrar |
| Esc | Cerrar (igual que el icono X de la esquina superior derecha) |
| Alt + Shift + PageUp | Siguiente registro |
| Alt + Shift + PageDown | Registro anterior |
| Ctrl + Del | Eliminar |
| Ctrl + s | Guardar |
| Ctrl + d | Nuevo registro en vista de formulario |

### Actualización de la función de resumen de la cuadrícula al seleccionar 

Mediante la función de establecer resumen a través del botón de clic derecho, es posible seguir actualizando el número de registros seleccionados en la cuadrícula. Esta función permite al usuario obtener dinámicamente funciones de resumen de un subconjunto de registros en la ventana filtrada. 
  
## Solapa

Etendo permite al usuario tener múltiples transacciones abiertas al mismo tiempo en diferentes solapas. Puede cambiar entre solapas activas. La solapa activa se resalta en color azul con una fina línea amarilla en la parte superior. Las solapas inactivas permanecen atenuadas en gris.

![Solapa](../../assets/drive/1L_S4knqCWJRPXPKIAn6_W-ompY7O4zZT.png)

Las solapas pueden cerrarse pulsando el botón X:

Es posible reordenar la posición de las solapas. Para hacerlo, arrastre la solapa y suéltela en la posición deseada:

En caso de desbordamiento de solapas, cuando el ancho total de las solapas supera el espacio horizontal disponible, aparecen tres flechas amarillas a la derecha de la última solapa que le permiten desplazarse por las solapas y navegar fácilmente hasta una:

![Solapa](../../assets/drive/1_K-cBXnCPoABJJmRfAowo3u58fyol43O.png)
  
---
Este trabajo es una obra derivada de [Introducción a la interfaz de usuario](http://wiki.openbravo.com/wiki/User_Interface_Introduction){target="_blank"} de [Wiki de Openbravo](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="_blank"} por [Etendo](https://etendo.software){target="_blank"}.