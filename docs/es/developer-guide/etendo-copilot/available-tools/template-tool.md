---
tags:
    - Etendo Copilot
    - Plantilla de herramienta en Python
    - Estandarización del desarrollo
    - Prototipado rápido
    - Herramienta
---

# Herramienta de plantilla

:octicons-package-16: Javapackage: `com.etendoerp.copilot.toolpack`

## Visión general

La **Herramienta de plantilla** es una plantilla para crear nuevas herramientas en aplicaciones basadas en Python. Está diseñada para proporcionar una estructura básica sobre la que construir funcionalidad personalizada. Los parámetros de entrada que acepta son: input1 e input2. La salida consiste en un mensaje que confirma una acción predeterminada.

!!!info
    Para poder incluir esta funcionalidad, debe estar instalado el Copilot Extensions Bundle. Para ello, siga las instrucciones del marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. Para más información sobre las versiones disponibles, la compatibilidad con el core y las nuevas funcionalidades, visite [Copilot Extensions - Notas de la versión](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

## Funcionalidad

Esta herramienta es útil para desarrolladores que desean crear nuevas herramientas rápidamente siguiendo un formato estándar. Puede utilizarse como punto de partida para desarrollar funciones específicas sin tener que preocuparse por la configuración inicial del código. Proporciona al usuario:

- Estandarización: facilita la creación de nuevas herramientas siguiendo un formato estándar, garantizando la consistencia en el desarrollo.
- Velocidad de desarrollo: acelera el proceso de desarrollo proporcionando una estructura básica predefinida.
- Flexibilidad: permite a los desarrolladores modificar y personalizar la funcionalidad según las necesidades específicas de su aplicación.

El uso de esta herramienta consiste en las siguientes acciones:

- **Procesamiento de argumentos**

    Toma parámetros de entrada que están en formato JSON. Si la entrada es una cadena, la convierte en un objeto JSON; si ya es un objeto JSON, lo utiliza directamente.

- **Acceso a parámetros**
    
    Extrae los valores de input1 e input2 del objeto JSON proporcionado.

- **Código personalizado**
    
    Contiene un espacio donde puede añadir código específico para realizar las acciones deseadas usando input1 e input2.

- **Devolución del resultado**

    Devuelve un mensaje que actualmente indica `{“message”: “Mail sent successfully”}`, pero puede personalizarse según la acción realizada.

## Ejemplo de uso

Imagine que desea crear una herramienta que sume dos números. Utilizaríamos la Herramienta de plantilla de la siguiente manera:
    
- input1: 3
- input2: 5

Podemos añadir el código necesario dentro de la sección **código aquí** para realizar la suma:

```
result = p_input1 + p_input2
return {“message”: f “Sum result is {result}”}
```

---
Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L](https://etendo.software){target="_blank"}.