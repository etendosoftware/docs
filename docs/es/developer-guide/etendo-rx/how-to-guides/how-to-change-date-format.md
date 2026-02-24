# Cambio del Formato de fecha y la Zona horaria en una solicitud

## Visión general

Este documento describe los pasos para que los desarrolladores cambien el formato de fecha y la zona horaria al realizar una solicitud HTTP a la aplicación. Estas funcionalidades son útiles para garantizar que los valores de fecha y hora se interpreten correctamente según la configuración regional del usuario o requisitos específicos.

## Requisitos previos

- Familiaridad con solicitudes HTTP y APIs REST.
- Acceso a la documentación de la API de la aplicación para obtener detalles de los endpoints.

## Añadir parámetros de Formato de fecha y Zona horaria

### Formato de fecha

Para especificar un formato de fecha personalizado, añada un parámetro `_dateFormat` a su solicitud HTTP. El valor debe ser una cadena que represente el formato de fecha deseado, siguiendo las convenciones de Java `SimpleDateFormat`.

**Ejemplo:**

```http
GET /OBMAPBusinessPartner/2C4C71BC828B47A0AF2A79855FD3BA7A?_dateFormat=yyyy-MM-dd
```

En este ejemplo, el Formato de fecha se establece en `"yyyy-MM-dd"`, lo que formateará las fechas como `"2023-08-29"`.

### Zona horaria

Para especificar una zona horaria personalizada, añada un parámetro `_timeZone` a su solicitud HTTP. El valor debe ser una cadena que represente la zona horaria deseada, siguiendo las convenciones de Java `TimeZone`. Este parámetro requiere disponer de `_dateFormat` y no puede utilizarse como parámetro único.

**Ejemplo:**

```http
GET /OBMAPBusinessPartner/2C4C71BC828B47A0AF2A79855FD3BA7A?_dateFormat=yyyy-MM-dd&_timeZone=America/New_York
```

En este ejemplo, el Formato de fecha se establece en `"yyyy-MM-dd"` y la zona horaria se establece en `"America/New_York"`.

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.