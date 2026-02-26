---
tags:
  - How to
  - Etendo classic
  - crear una tabla
  - tabla
  - diccionario de aplicación
  - reconstrucción del sistema
---

# Cómo crear una tabla

## Cómo crear una nueva tabla

Puede encontrar documentación más genérica sobre las tablas y sus características en Etendo en la página [Tabla](../../concepts/Tables.md). Esa página explica las columnas comunes necesarias para todas las tablas en Etendo, las reglas de nomenclatura y otra información importante.

En primer lugar, es necesario crear las estructuras subyacentes de la base de datos que contendrán los datos. En otras palabras, utilizando una herramienta de administración de bases de datos (p. ej., [pgAdmin 4](https://www.pgadmin.org/){target="\_blank"} o [phpPgAdmin](https://github.com/phppgadmin/phppgadmin){target="\_blank"} para PostgreSQL y [Oracle SQL Developer](https://www.oracle.com/database/sqldeveloper/){target="\_blank"}) primero se debe ejecutar `CREATE TABLE` para crear la tabla que se utilizará para almacenar los datos de la nueva ventana/solapas.

### Objetivo

Imagine que estamos desarrollando un módulo de RR. HH. y necesitamos una ventana que permita al usuario introducir los salarios de los empleados. También necesitamos realizar el seguimiento del salario del empleado, por lo que es necesario conservar los registros históricos. Cada registro de salario debe tener un campo Fecha de vigencia desde (Valid From Date) que indique cuándo entró en vigor un salario determinado. El registro perteneciente a un empleado concreto con la Fecha de vigencia desde más reciente es el salario que es válido hoy. Tenga en cuenta que los empleados ya están dentro del sistema, contenidos en la tabla de base de datos `C_BPARTNER` e indicados por la columna `C_BPARTNER ISEMPLOYEE`. Por lo tanto, solo necesitamos crear una tabla de base de datos que contenga los salarios reales.

### Modularidad

Todos los nuevos desarrollos deben pertenecer a un módulo que no sea el módulo _core_. Siga la sección [Cómo crear un módulo](How_To_Create_a_Module.md) del Manual del desarrollador de Modularidad para crear un nuevo módulo.

Una vez que haya registrado el módulo, debe decidir el prefijo de base de datos que indicará los elementos de BD que pertenecen a este módulo. Esto se hace añadiendo prefijo(s) de base de datos al módulo. De esta forma, cualquier artefacto de base de datos (tabla, trigger, procedimiento almacenado) que pertenezca a ese módulo deberá tener el nombre con dicho prefijo. En nuestro caso, añada el _Prefijo de Base de Datos_ `HT`.

Por último, el paquete de datos debe introducirse en la solapa _Paquete de Datos_ de la ventana _Módulo_. Introduzca allí un nuevo registro con HR Data como _Nombre_ y _{modulePackage}.data_ (tenga en cuenta que este paquete debe ser un subpaquete del que introdujo a nivel de módulo), por ejemplo com.etendoerp.howtos.data en caso de que com.etendoerp.howtos sea el paquete del módulo.

### Crear nuevas tablas en la base de datos

Vamos a introducir una nueva tabla de base de datos llamada `ht_salary` que contendrá los datos requeridos. Observe el prefijo `HT` del nombre de la tabla, que indica el módulo al que pertenece esta tabla.

La nueva tabla `ht_salary` debe incluir los campos `AD_Client_ID`, `AD_Org_ID`, `IsActive`, `Created`, `CreatedBy`, `Updated` y `UpdatedBy`, que son `mandatory` y necesarios por motivos de seguridad y auditoría de la aplicación.

| Nombre de columna | Tipo   | Longitud | Nota                                                                                                                                   |
| ---------------- | ------ | -------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `HT_SALARY_ID`   | CHAR   | 32       | La clave primaria de la tabla, que debe seguir el nombre de la tabla seguido de \_ID.                                                  |
| `AD_CLIENT_ID`   | CHAR   | 32       | Indica a qué cliente (empresa) pertenece el registro (multitenencia).                                                                  |
| `AD_ORG_ID`      | CHAR   | 32       | Indica a qué organización (ciudad/departamento/ubicación) dentro de un cliente pertenece un registro.                                  |
| `ISACTIVE`       | CHAR   | 1        | Está pensado para desactivar registros que ya no son válidos pero están referenciados dentro del sistema y, por tanto, no pueden eliminarse. |
| `CREATED`        | DATE   |          | Fecha/hora de creación de un registro.                                                                                                 |
| `CREATEDBY`      | CHAR   | 32       | Clave foránea a `AD_USER` que indica el usuario que creó este registro.                                                                |
| `UPDATED`        | DATE   |          | Fecha/hora de la última actualización de un registro.                                                                                  |
| `UPDATEDBY`      | CHAR   | 32       | Clave foránea a `AD_USER` que indica el usuario que actualizó por última vez este registro.                                            |
| `C_BPARTNER_ID`  | CHAR   | 32       | Empleado al que pertenece este salario.                                                                                                 |
| `AMOUNT`         | NUMBER | 10       | El importe real del salario.                                                                                                           |
| `C_CURRENCY_ID`  | CHAR   | 32       | Clave foránea a `C_CURRENCY` que indica la divisa en la que está el importe.                                                           |
| `VALIDFROM`      | DATE   |          | Fecha desde la que este salario es válido.                                                                                              |

Para crear la tabla anterior en la base de datos, utilice una de las siguientes sentencias `CREATE TABLE` en función de la BD que esté utilizando:

!!!note
    Todos los identificadores en el SQL deben escribirse en minúsculas. Así podrán utilizarse posteriormente sin necesidad de entrecomillarlos.

```sql title="SQL table creation script"
CREATE TABLE ht_salary
(
  ht_salary_id  CHARACTER VARYING(32)		NOT NULL,
  ad_client_id  CHARACTER VARYING(32)		NOT NULL,
  ad_org_id     CHARACTER VARYING(32)		NOT NULL,
  isactive      CHARACTER(1)                   NOT NULL        DEFAULT 'Y',
  created       TIMESTAMP WITHOUT TIME ZONE 	NOT NULL 	DEFAULT now(),
  createdby     CHARACTER VARYING(32)		NOT NULL,
  updated       TIMESTAMP WITHOUT TIME ZONE 	NOT NULL 	DEFAULT now(),
  updatedby     CHARACTER VARYING(32)         	NOT NULL,
  c_bpartner_id CHARACTER VARYING(32)         	NOT NULL,
  amount	 NUMERIC 	      	        NOT NULL,
  c_currency_id VARCHAR(32)         	        NOT NULL,
  validfrom     TIMESTAMP WITHOUT TIME ZONE    NOT NULL,
    CONSTRAINT ht_salary_isactive_check CHECK (isactive = ANY (ARRAY['Y'::bpchar, 'N'::bpchar])),
    CONSTRAINT ht_salary_key PRIMARY KEY (ht_salary_id),
    CONSTRAINT ht_salary_ad_org FOREIGN KEY (AD_ORG_ID) REFERENCES AD_ORG (ad_org_id),
    CONSTRAINT ht_salary_ad_client FOREIGN KEY (AD_CLIENT_ID) REFERENCES AD_CLIENT (ad_client_id),
    CONSTRAINT ht_salary_c_bpartner FOREIGN KEY (C_BPARTNER_ID) REFERENCES C_BPARTNER (c_bpartner_id),
    CONSTRAINT ht_salary_c_currency FOREIGN KEY (C_CURRENCY_ID) REFERENCES C_CURRENCY (c_currency_id)
);
```

### Registrar la tabla en el Diccionario de Aplicación

Los siguientes pasos registran la tabla recién creada dentro del Diccionario de Aplicación de Etendo Classic.

Para ello, primero inicie sesión en Etendo Classic utilizando un nombre de usuario con acceso a `Administrador del sistema` > `Rol`. Vaya a `Diccionario de Aplicación` > `Tablas y Columnas` y cree un nuevo registro como se muestra en la captura de pantalla siguiente:

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Table-1.png)

Los campos principales de esta ventana son (para más información, consulte la descripción de la tabla `AD_Table`):

- _Paquete de Datos_ especifica a qué paquete de datos Java dentro del módulo pertenecerá la tabla cuando se utilice dentro de [DAL](../concepts/Data_Access_Layer.md) (Data Access Layer).
- _Nombre_ define el nombre que Etendo Classic utiliza para reconocer la tabla de base de datos definida. Este nombre se utiliza en [servicios web REST](../../concepts/xml-rest-web-services.md) y en la [Data Access Layer](../../concepts/Data_Access_Layer.md#entity-naming).
- _Descripción_ proporciona una breve descripción de la tabla.
- _Ayuda/Comentario_ define el texto que se muestra en la ventana de ayuda.
- _Nombre tabla BD_ define el nombre de la tabla de base de datos tal y como se definió mediante `CREATE TABLE` durante su creación.
- _Nombre de la clase Java_ será la clase Java real dentro del Paquete de Datos del módulo a través de la cual podrá acceder a esta tabla cuando utilice DAL.
- _Acceso datos_ determina qué tipo de datos contendrá la tabla debido a la funcionalidad de multitenencia
  - _Solo sistema_: solo se pueden insertar registros de sistema en esta tabla (`AD_CLIENT_ID=0`, `AD_ORG_ID=0`), por ejemplo `AD_TABLE`.
  - _Sistema/Cliente_: aquí se pueden insertar registros de sistema o específicos de cliente (`AD_CLIENT_ID=anything`, `AD_ORG_ID=0`), por ejemplo `AD_ROLE`
  - _Organización_: solo se pueden insertar datos específicos de cliente y organización en esta tabla (`AD_CLIENT_ID<>0`, `AD_ORG_ID<>0`), por ejemplo `C_INVOICE`
  - _Cliente/Organización_: solo se pueden insertar datos específicos de cliente en esta tabla; sin embargo, pueden pertenecer a organizaciones específicas dentro de ese cliente o compartirse entre todas (`AD_CLIENT_ID<>0`,`AD_ORG_ID=anything`), por ejemplo `C_BPARTNER`
  - _Todos_: se puede insertar cualquier combinación de `AD_CLIENT_ID` y `AD_ORG_ID` en esta tabla.

Guarde este registro y, a continuación, pulse el botón _Crear columnas de la base de datos_ para crear columnas automáticamente dentro de la solapa _Columna_.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Table-2.png)

Una vez finalizado el proceso de creación, se le informará del número de columnas que se han añadido a esta tabla.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Table-3.png)

Cambie a la solapa _Columna_ para ver todas las columnas (para más información, consulte la descripción de la tabla AD*Column) que se crearon según su definición en la base de datos. Ahora puede modificar adicionalmente las propiedades de cada columna. A cada columna se le asigna una referencia (que define el tipo de dato) en función de su nombre y su tipo de dato. Ejecute el proceso \_Synchronize Terminology* (`Diccionario de Aplicación` > `Sincronizar terminología`). Dos detalles delicados antes de ejecutarlo:

- Compruebe que ha definido dependencias desde su módulo hacia core y hacia cualquier otro módulo necesario. Sincronizar terminología enlazará sus columnas con Elementos en su módulo o en los módulos de los que depende. Si no declara la dependencia con core, el sistema creará nuevos elementos para columnas estándar como IsActive, CreatedBy, etc.
- No establezca los Elementos enlazados a sus columnas; deje que Sincronizar terminología haga el trabajo. De este modo, el proceso encontrará los elementos apropiados y establecerá los nombres de columna correctos para las columnas estándar (IsActive, CreatedBy, etc.).

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Table-4.png)

Este proceso intenta encontrar un elemento de aplicación existente (dentro del módulo que se está desarrollando actualmente) y, por tanto, su etiqueta, ayuda y descripción; y si no se encuentra, se crea uno nuevo. Esto permite una traducción centralizada de la aplicación/módulo.

![](../../../assets/developer-guide/etendo-classic/how-to-guides/How_to_create_a_Table-5.png)

Cada tabla debe tener al menos una columna marcada como identificador. Los valores reales de las columnas identificadoras se concatenan posteriormente para mostrarse al usuario como representación de un registro concreto (consulte el enlace al Pedido de venta dentro de la ventana Factura de venta). Estos identificadores también se utilizarán para construir listas desplegables de registros de esa tabla concreta. Por defecto, todas las columnas cuyo nombre de columna sea _Nombre_ se establecen como identificador. En caso de que no exista ninguna columna con este _Nombre_, no se establece ningún identificador y es necesario hacerlo manualmente o la compilación fallará.

El nombre se utiliza en la [Data Access Layer](../../concepts/Data_Access_Layer.md) y en [servicios web REST](../../concepts/xml-rest-web-services.md). Para columnas específicas (información de auditoría, cliente/organización, activo) es importante ser preciso en la nomenclatura.

!!!note
    Las columnas que se denominan `line` o `seqNo` se utilizan para contener el número de secuencia de un registro (es decir, el número de una línea en una factura). Toman un valor por defecto como:

    ```
    @SQL=SELECT COALESCE(MAX(ColumnName),0)+10 AS DefaultValue FROM TableName
    WHERE xxParentColumn=@xxParentColumn@
    ```

    La parte `WHERE` de esta cláusula debe sustituirse por los valores requeridos. El código que debe aparecer aquí es el nombre de la columna que enlaza con el _id_ de la tabla padre. Por ejemplo, cada registro de `C_InvoiceLine` pertenece a un registro concreto de `C_Invoice` y todos están secuenciados. `C_Invoice` es la tabla padre de las líneas guardadas en `C_InvoiceLine`. Esta tabla tiene una columna llamada line y el valor por defecto que toma es:

    ```
    @SQL=SELECT COALESCE(MAX(LINE),0)+10 AS DefaultValue FROM C_INVOICELINE
    WHERE C_INVOICE_ID=@C_INVOICE_ID@
    ```

La mayoría de las columnas en nuestro caso específico `HT_SALARY` se detectarán correctamente de forma automática; sin embargo, algunas necesitan revisión:

- _Importe_ : Referencia = _Importe_ , Longitud = _10_
- _C_BPartner_ID_ : Referencia = _Selector_ , Clave de búsqueda de referencia = _Terceros_ , Longitud = _32_ , Enlazar con columna padre = _Y_
- _Valid From_ : Identificador = _Y_
- _Importe_ : Identificador = _Y_

Etendo Classic ahora conoce la nueva tabla de base de datos HT_SALARY y cómo tratarla en términos de su definición y de la representación al usuario.

### Reconstrucción del sistema

Por último, para que la tabla recién añadida esté disponible en tiempo de ejecución, es necesario ejecutar `./gradlew generate.entities` y desplegar los cambios en Tomcat. Estos dos pasos pueden realizarse conjuntamente ejecutando `./gradlew smartbuild`. Después de eso, debe reiniciarse Tomcat para refrescar el modelo en memoria de DAL, de modo que conozca las columnas recién añadidas.

---

Este trabajo es una obra derivada de [Cómo crear una tabla](http://wiki.openbravo.com/wiki/How_to_create_a_Table){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.