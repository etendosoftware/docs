---
title: Cómo configurar el log
tags:
    - Configuración de logging 
    - Depuración del backend de Etendo 
    - Rotación de logs
    - Verbosidad 
    - Gestión de logs 
---

# Cómo configurar el log

## Visión general

El logging permite a los desarrolladores **registrar mensajes** durante la ejecución del código. Utilice estos mensajes para diagnosticar problemas del backend como errores, advertencias y cuellos de botella de rendimiento.

Para aprender a utilizar el logging en su código personalizado, consulte la guía [Cómo registrar usando Log4j](how-to-log-using-log4j.md).

## Configuración

El logging se configura mediante tres archivos principales de configuración, según el escenario:

- `config/log4j2.xml`: Configuración para tareas de compilación por línea de comandos (p. ej., `./gradlew install`). 
- `config/log4j2-web.xml`: Configuración para la aplicación web ejecutándose en un contenedor como Tomcat. 
- `src-test/src/log4j2-test.xml`: Configuración utilizada específicamente para pruebas y suites JUnit. 

### Archivo

De forma predeterminada, la salida del log se redirige a un archivo. Esto se define mediante la etiqueta `<RollingFile>` dentro de la sección `<Appenders>`. Los valores predeterminados son:

```XML title="log4j2-web.xml"
<RollingFile name="RollingFile" fileName="${logDir}/etendo.log"
                filePattern="${logDir}/etendo-%d{yyyyMMdd}-%i.log.gz">
<PatternLayout pattern="%d [%t] %-5p %c - %m%n"/>
    <Policies>
    <TimeBasedTriggeringPolicy />
    <SizeBasedTriggeringPolicy size="100MB" />
    </Policies>
    <DefaultRolloverStrategy max="30"/>
</RollingFile>
```

Con esta configuración, el log principal se escribe en `etendo.log` dentro del directorio `${logDir}`. En un despliegue estándar de Tomcat, este directorio normalmente se encuentra en la carpeta `logs/` de la instalación de Tomcat.

!!! tip
    Si está ejecutando Etendo desde la línea de comandos, `${logDir}` normalmente apunta al directorio `build/` o a la raíz del proyecto, dependiendo de la ejecución de la tarea.

### Logging en consola

También puede ver los logs en la consola (salida estándar) utilizando el appender `<AppenderRef ref="Console"/>`. Esto es útil para desarrollo, para evitar tener que hacer tail continuamente de un archivo.

```XML
<Loggers>
    <Root level="info">
        <AppenderRef ref="RollingFile"/>
        <AppenderRef ref="Console"/>
    </Root>
</Loggers>
....
<Appenders>
    <Console name="Console" target="SYSTEM_OUT">
        <PatternLayout pattern="%d [%t] %-5p %c - %m%n"/>
    </Console>
    ...
</Appenders>
```

### Verbosidad del log

La verbosidad se controla mediante los niveles de log: `ALL`, `TRACE`, `DEBUG`, `INFO`, `WARN`, `ERROR`, `FATAL` y `OFF`.

| Nivel | Descripción |
|-------|-------------|
| ALL   | Todos los niveles, incluidos los personalizados. |
| TRACE | Eventos informativos extremadamente detallados, más detallados que DEBUG. |
| DEBUG | Eventos informativos detallados, especialmente útiles para depurar aplicaciones. |
| INFO  | Mensajes informativos que destacan el progreso de la aplicación a alto nivel. |
| WARN  | Situaciones potencialmente perjudiciales. |
| ERROR | Eventos de error que podrían permitir que la aplicación continúe ejecutándose. |
| FATAL | Eventos de error graves que probablemente provoquen el fallo de la aplicación. |
| OFF   | Sin mensajes de log. |

!!! warning "Entornos de producción"
    Evite utilizar los niveles `DEBUG` o `TRACE` en entornos de producción, ya que pueden afectar significativamente al rendimiento y consumir grandes cantidades de espacio en disco.

Es posible configurar el nivel de log **globalmente** o **por clase/paquete**.

Esto puede modificarse de dos formas:

- **Configuración estática**: Edite los archivos `log4j2*.xml`. Esto requiere un redespliegue (`./gradlew smartbuild`) y un reinicio de Tomcat para que surta efecto.
    
    - **Globalmente**: Cambie el nivel del Root Logger: 

        ``` XML    
        <Loggers>
            <Root level="debug">
            ...
            </Root>
        </Loggers>
        ```

    - **Por clase o paquete Java**: Añada una entrada `<Logger>`: 

        ``` XML 
        <Loggers>
        ...
        <!-- Set a specific package to debug level -->
        <Logger name="com.etendoerp.copilot" level="debug"/>
        ...
        </Loggers>
        ```

        !!! note
            Estos loggers heredan los appenders del Root logger de forma predeterminada. Para cambiar esto, establezca el atributo `additivity` en `false`. 

        !!! info
            Para más información, consulte la [documentación de Log4j2](https://logging.apache.org/log4j/2.x/manual/configuration.html#Additivity){target="\_blank"}. 

- **Configuración en tiempo de ejecución**: Este método no requiere reinicio, pero no es persistente (la configuración se pierde tras reiniciar Tomcat). Para modificar niveles en tiempo de ejecución:
    1. Inicie sesión en la aplicación como **Administrador del sistema**.
    2. Navegue a `Configuración general > Aplicación > Gestión de logs`. 
    3. Filtre y seleccione los loggers deseados.
    4. Elija el nivel de log a establecer y haga clic en **Aplicar**.

    ![texto alternativo](../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-configure-log-1.png)

!!! info
    Los loggers de clases o paquetes aparecen en esta lista a medida que se ejecutan. Si falta un logger específico, ejecute la funcionalidad que lo utiliza para registrarlo en el sistema. Tenga en cuenta que reiniciar Tomcat limpia esta lista, y deberá volver a ejecutar las funcionalidades para ver los loggers de nuevo. Para depurar durante el arranque de la aplicación, configure el nivel de log directamente en `log4j2-web.xml`.

## Rotación

Para evitar que los archivos de log crezcan indefinidamente, se configura la **rotación** para archivar logs antiguos.

La configuración se gestiona en la sección `<RollingFile>`:
    
``` XML
<Policies>
    <SizeBasedTriggeringPolicy size="100MB" />
    <TimeBasedTriggeringPolicy />
</Policies>
<DefaultRolloverStrategy max="30">
    <Delete basePath="${logDir}">
    <IfFileName glob="etendo-*.log.gz">
        <IfAccumulatedFileCount exceeds="30"/>
    </IfFileName>
    </Delete>
</DefaultRolloverStrategy>
```

De forma predeterminada, el archivo de log está limitado a **100MB**. Se archiva y comprime diariamente o cuando alcanza el límite de tamaño. Se conservan hasta 30 archivos archivados; una vez alcanzado este límite, se elimina el archivo más antiguo.

---
Este trabajo es una obra derivada de [Cómo configurar el log](http://wiki.openbravo.com/wiki/How_To_Configure_Log){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.