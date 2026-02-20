---
tags:
    - Guía práctica
    - Copilot
    - Consola
    - Ejecutar Copilot
    - Terminal
---

# Cómo ejecutar Copilot a través de la consola

## Visión general

Este artículo explica cómo ejecutar Copilot a través de la consola. Esto es útil cuando desea probar una herramienta o un agente sin utilizar la interfaz de Etendo Classic.

## Requisitos previos
* Acceso al host de Etendo Classic.

## Comando
```bash
./gradlew copilot.do -Phost='https://my.etendo.instance/etendo' -Papp_id="Module Creator" -Pusername=my-user -Ppassword=my-password -Pquestion="Can you create a Module called 'Test Module? "  --console=plain 
```

## Parámetros

* **-Phost**: La URL del host de Etendo Classic. Si no se proporciona, se utilizará el host por defecto http://localhost:8080/etendo.
* **-Pusername**: El nombre de usuario de Etendo Classic, que ejecutará el comando. Este usuario debe tener los permisos necesarios para ejecutar el comando.
* **-Ppassword**: La contraseña de Etendo Classic del usuario que ejecutará el comando.
* **-Prole**: El rol del usuario que ejecutará el comando. Si no se proporciona, se utilizará el rol por defecto.
* **-Papp_id**: El id del agente que se va a ejecutar. Puede ser el nombre **exacto** del agente o el **id** del agente.
* **-Pquestion**: La pregunta que desea hacer al agente.

* **--console=plain**: Este parámetro se utiliza para evitar que la consola de Gradle muestre la barra de progreso.


!!! warning
    - Los parámetros ```username``` y ```password``` son obligatorios.
    - Si no se proporcionan, el script los solicitará. Esto es para evitar almacenar información sensible en el historial de comandos.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L.](https://etendo.software){target="_blank"}.