## Puede filtrar cualquier solicitud por filas activas o todas las filas

El parámetro `_noActiveFilter` puede utilizarse en cualquier método de solicitud para filtrar registros activos o todos los registros (activos e inactivos). De este modo, permite un mayor control al obtener los resultados.

---

## Ejemplo de solicitud GET para todos los registros

Abra Postman y realizaremos una solicitud GET.

    Verbose: GET

    URL: http://localhost:8094/BusinessPartner?_noActiveFilter=true

    Body: empty

    Return: un objeto JSON con todos los businessPartners activos o inactivos

---

## Ejemplo de solicitud GET solo para registros activos

Abra Postman y realizaremos una solicitud GET.

    Verbose: GET

    URL: http://localhost:8094/BusinessPartner?_noActiveFilter=false

    Body: empty

    Return: un objeto JSON con todas las filas activas de BusinessPartner

---

Otra forma de obtener filas activas es eliminar el parámetro `_noActiveFilter parameter`, ya que, por defecto, el filtro de filas activas siempre se aplica.

---
Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L](https://etendo.software){target="_blank"}.