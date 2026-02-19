---
title: Menú de la aplicación
tags: 
  - Concepts
  - Application menu
  - General setup
  - Etendo Classic
---

# Menú de la aplicación

## Visión general

El Menú de la aplicación se muestra en el lado izquierdo de la ventana. Se utiliza para hacer accesibles al usuario todos los elementos de la aplicación.

![](../../../assets/developer-guide/etendo-classic/concepts/Application_Menu-0.png)

### Gestión del menú

El menú se gestiona desde la ventana `Configuración general` > `Aplicación` > `Menú`.

Para crear una nueva entrada de menú:

  1. Cree un nuevo registro en esta ventana.
  2. Seleccione el tipo de elemento para la entrada; esto se realiza configurando el campo **Acción**. Los elementos invocables desde el menú son **Ventana**, **Informe**, **Proceso**, **Formulario**, **Flujo de trabajo**, **Enlace interno/externo** y **Mantenimiento**.
  3. En función de la acción seleccionada, se mostrará una lista desplegable diferente para seleccionar un elemento del tipo seleccionado. Tenga en cuenta que el nombre y la descripción se sobrescribirán cuando se ejecute el proceso de sincronización.
  4. Coloque la nueva entrada de menú en la posición correcta; esto se realiza mediante:
    * Seleccionar un registro en la cuadrícula.
    * Abrir la ventana del árbol haciendo clic en el icono de menú de árbol ![](../../../assets/developer-guide/etendo-classic/concepts/Application_Menu-1.png)
    * Seleccionar la entrada a reubicar y seleccionar la nueva posición.

![](../../../assets/developer-guide/etendo-classic/concepts/Application_Menu-2.png)

Las carpetas se crean marcando el campo **Nivel agrupación**.

### Seguridad

Aunque una entrada de menú esté definida, no se mostrará en caso de que el rol que ha iniciado sesión en la aplicación no tenga concedido permiso para ese elemento.

### Carpeta de información

En la parte inferior del menú, hay una **Carpeta de información** que contiene enlaces a los **Selector**. Los elementos mostrados en esta carpeta son aquellos que se utilizan en al menos una ventana accesible para el rol actual.

---
Este trabajo es una obra derivada de [Menú de la aplicación](http://wiki.openbravo.com/wiki/Application_Menu){target="\_blank"} de [Wiki de Openbravo](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizado bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.