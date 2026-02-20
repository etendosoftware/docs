---
title: Cómo usar secuencias avanzadas

tags:
	- Cómo hacer
    - Secuencias
    - Secuencias transaccionales
    - Secuencias no transaccionales
    - Gestión de secuencias de base de datos
---

# Secuencias

## Visión general

Este documento cubre cómo utilizar la implementación de secuencias, explica todas las funcionalidades y ofrece algunos casos de ejemplo de implementación.

Existen dos implementaciones base de referencia definidas que puede utilizar o ampliar:

- **Secuencias transaccionales**: estas secuencias bloquean la tabla en la base de datos para garantizar la generación de identificadores de forma secuencial y evitar duplicados o saltos.
- **Secuencias no transaccionales**: en este caso, el proceso para crear secuencias utiliza Secuencias de base de datos y debe usarse en casos en los que los saltos entre números no sean un problema.

!!! warning "Importante"
	Tenga en cuenta que tanto las Secuencias transaccionales como las Secuencias no transaccionales, tal y como están configuradas en nuestro sistema, no están soportadas dentro de Procedimientos almacenados de base de datos (PL). Esto incluye procesos específicos como POSOrder, que no puede utilizar estas secuencias. Implementar estas secuencias en PL, por ejemplo dentro del proceso POSOrder, puede provocar fallos o errores del sistema. Estas secuencias están diseñadas para la capa de aplicación y pueden no ajustarse al contexto procedimental de operaciones directas en base de datos.

## Configuración rápida de secuencias

1. En primer lugar, inicie sesión como “Administrador del sistema”. Abra `Application` > `Application Dictionary ` >`Tables and Columns`. Seleccione la columna que desea configurar como secuencia y cambie el campo **Referencia** a Secuencia transaccional o Secuencia no transaccional.
	
	!!! info
		Si desea definir una nueva referencia de secuencia, debe añadirla en el campo **Referencia clave** y el padre (Secuencia base) debe estar en el campo **Referencia**.
		Consulte cómo crear una nueva referencia en [nueva referencia de secuencia](../../../developer-guide/etendo-classic/how-to-guides/how-to-use-advanced-sequences.md#new-sequence-reference).
	
	<figure markdown>
  ![Image title](../../../assets/legacy/technicaldocumentation/platform/quicksequence.png){ width="700" }
  <figcaption>Añadiendo secuencia transaccional en la tabla de facturas</figcaption>
	</figure>


2. A continuación, es necesario ejecutar un proceso en `Application` > `General Setup`\> `Application`\> `Create Sequences` para generar las secuencias, seleccionando la **Organización** raíz donde se crearán.

	!!! warning
		Para ejecutar este proceso, el usuario debe haber iniciado sesión con el rol que gestiona la secuencia, no como administrador del sistema.


	!!! warning
		Este proceso solo generará las combinaciones para organización y tipos de documento. En caso de que quiera generar secuencias para las nuevas dimensiones descritas a continuación, debe ampliar la acción `SequencesGenerator` y sobrescribir los métodos `generateSequenceCombination` y `setSequenceValues` para generar las combinaciones relevantes y establecer las dimensiones recién añadidas.
		También puede crear manualmente las secuencias necesarias.

	<figure markdown>
  ![Image title](../../../assets/legacy/technicaldocumentation/platform/createsequencesprocess.png){ width="700" }
  <figcaption>Ejecutando el proceso para crear nuevas secuencias</figcaption>
	</figure>


	---

	Después de eso, en la ventana `Document Sequence` puede ver las secuencias generadas.

	<figure markdown>
  ![Image title](../../../assets/legacy/technicaldocumentation/platform/sequenceslist.png){ width="700" }
  <figcaption>Lista de secuencias generadas por el proceso</figcaption>
	</figure>

	Cuando edite el registro, puede ver:

	<figure markdown>
  ![Image title](../../../assets/legacy/technicaldocumentation/platform/formviewad_sequence.png){ width="700" }
  <figcaption>Vista de formulario de secuencia</figcaption>
	</figure>

	- **Organización:** organización propietaria asociada a la secuencia.
	- **Nombre:** un identificador usando la **Tabla** y la **Columna** asociadas a la secuencia.
	- **Descripción:** campo para añadir información o detalles sobre la secuencia.
	- **Numeración automática:** marque para definir el incremento y la numeración inicial.
	- **Incrementar:** valor numérico para definir el incremento de la secuencia.
	- **Valor actual:** número inicial de la secuencia.
	- **Prefijo:** cadena al inicio de la secuencia **(**admite enmascaramiento**).**
	- **Sufijo:** cadena al final de la secuencia **(**admite enmascaramiento**).**
	- **Tipo de documento :** en caso de que la tabla tenga tipos de documento, se habrá creado una secuencia para cada tipo de documento.
	- **Máscara:** es una cadena que define un formato de análisis, con la posibilidad de definir una fecha dinámica o una subcadena literal, además del número incremental formateado. 

	!!! info
		Para más información sobre el enmascaramiento, consulte la [guía de usuario de enmascaramiento de secuencias](../../../user-guide/etendo-classic/basic-features/financial-management/accounting/setup/document-sequence.md#sequence-masking).

	- **Tabla:** define la tabla en la que se encuentra la columna de tipo secuencia.
	- **Columna:** la columna donde se define la secuencia.

3. En caso de que la secuencia se aplique en el campo DocumentNo, el usuario debe asegurarse de que el **Tipo de documento** asociado tenga la propiedad `sequenced document` desmarcada para evitar que se ejecute el proceso heredado. Para ello, primero inicie sesión como usuario y, a continuación, abra `Aplication>Finantial Management>Accounting>Setup>Document Type`, seleccione el **Tipo de documento** asociado y, por último, edítelo.

	!!! warning
		_Si no se sigue este paso, se ejecutará el proceso heredado._

	<figure markdown>
  ![Image title](../../../assets/legacy/technicaldocumentation/platform/doctypesettings.png){ width="700" }
  <figcaption>Ejemplo de Tipo de documento</figcaption>
	</figure>


4. Por último, debe compilar la aplicación. Para ello, ejecute:

	```bash title="Terminal"
	./gradlew compile.complete smartbuild
	```

5. Para exportar los cambios a su módulo, no olvide ejecutar:

	```bash title="Terminal"
 	./gradlew export.database
	```

### **Nueva referencia de secuencia**

Si desea definir una nueva referencia con referencia padre transaccional o no transaccional, debe crear un nuevo registro en la ventana Referencia (`Application` > `Application Dictionary ` >`Reference`) y establecer:

<figure markdown>
  ![Image title](../../../assets/legacy/technicaldocumentation/platform/new_sequence_reference.png){ width="700" }
  <figcaption>Ejemplo de nueva referencia de secuencia</figcaption>
</figure>


- **Nombre:** identificador de la nueva referencia.
- **Descripción:** campo para añadir información o detalles sobre la referencia.
- **Referencia padre:** seleccione secuencia transaccional o secuencia no transaccional.

&nbsp;
&nbsp;

#### Solapa Configuración de secuencia: 

![sequence_config.png](../../../assets/legacy/technicaldocumentation/platform/sequence_config.png)

- **Clase Java generadora:** clase que genera el siguiente valor de secuencia usando las definiciones de secuencia de documento. (Si está vacío, se utiliza un generador por defecto).

Al crear una secuencia no transaccional, debe definir:

- **Nombre de secuencia de BD:** nombre de la secuencia definida en la base de datos.
- **Valor inicial de secuencia de BD**: número inicial de la secuencia.
- **Valor de incremento de secuencia de BD:** valor numérico para definir el incremento de la secuencia.

Puede usar una Secuencia definida o crear una nueva usando SQL:

```sql
CREATE SEQUENCE [ IF NOT EXISTS ] sequence_name
    [ AS { SMALLINT | INT | BIGINT } ]
    [ INCREMENT [ BY ] increment ]
    [ MINVALUE minvalue | NO MINVALUE ]
    [ MAXVALUE maxvalue | NO MAXVALUE ]
    [ START [ WITH ] start ]
    [ CACHE cache ]
    [ [ NO ] CYCLE ]
    [ OWNED BY { table_name.column_name | NONE } ]
```

| _Sintaxis de Postgres para crear una nueva secuencia_ |

!!! info
    En caso de que el padre sea Secuencia transaccional, solo aparecerá el campo Clase Java generadora, pero en caso de que el padre sea una Secuencia no transaccional debe definir todos los campos.

&nbsp;

### Lista de dimensiones

Una dimensión es una nueva cláusula de filtro utilizada para seleccionar la secuencia que se usará al crear o guardar un nuevo registro. Las dimensiones por defecto son:

- Cliente
- Organización
- Tipo de documento

De este modo, puede tener dos secuencias diferentes dependiendo, por ejemplo, de la **Organización** del registro. Lo mismo aplica a las otras dimensiones por defecto.

!!! info
    Actualmente, las dimensiones solo están soportadas en **Secuencias transaccionales**.

![dimension_graph1.png](../../../assets/legacy/technicaldocumentation/platform/dimension_graph1.png)

&nbsp;

#### Añadir dimensiones personalizadas

Si desea añadir una nueva dimensión para filtrar secuencias, esta dimensión debe ser una columna en ambas tablas `AD_Sequence` y en la tabla donde se utiliza la secuencia transaccional. También debe crear una nueva referencia y crear un nuevo registro en la solapa `Dimension List` con esta columna (consulte cómo crear una nueva referencia de secuencia arriba).


#### Cuando una dimensión es una columna de clave foránea

1. Para definir una nueva dimensión, debe comenzar añadiendo una columna en la tabla `AD_Sequence` y una clave foránea a la columna referenciada en una tabla específica. La columna de dimensión debe crearse en la tabla correspondiente (`M_Product` en este ejemplo), a menos que decida utilizar una columna existente como dimensión.

	!!! warning
		El nombre de las columnas debe ser el mismo en ambas tablas.

	```sql
	ALTER TABLE AD_Sequence ADD COLUMN <dimension>_id varchar(32),
	ADD CONSTRAINT ad_sequence_<dimension> FOREIGN KEY (<dimension>_id) REFERENCES <table> (<dimension>_id)

	ALTER TABLE M_Product ADD COLUMN <dimension>_id varchar(32),
	ADD CONSTRAINT M_product_<dimension> FOREIGN KEY (<dimension>_id) REFERENCES <table> (<dimension>_id)
	```
	!!!note
		Recuerde sustituir `<dimension>` por el nombre deseado.

2. A continuación, debe crear el registro correspondiente de `AD_Column` en el Diccionario de aplicación. `Application` > `Application Dictionary ` > `Tables and Columns`, busque la **Tabla** `AD_Sequence` y cree la nueva columna.
   Después debe establecer el campo **Referencia** de la dimensión apuntando a la tabla de clave foránea.

	!!! warning
		Si la tabla con los registros de dimensión es una tabla nueva, debe crearse en `Application` > `Application Dictionary ` >`Reference`, estableciendo la Referencia base como Tabla y añadiendo la tabla en la solapa `Table Reference`.

3.  Además, debe crear el campo en la ventana `Document Sequence`. `Application` > `Application Dictionary ` >`Windows, Tabs and Fields`, busque la ventana `Document Sequence` y en la solapa `Sequence` ejecute el proceso para crear el nuevo campo.

4.  Si la dimensión es una columna nueva, debe repetir el paso anterior para crear el campo en la tabla donde se utiliza la secuencia.

5.  Por último, vuelva a la **Referencia** creada previamente y cree un nuevo registro en la solapa `Dimension List`, seleccionando la nueva columna que acaba de crear; a continuación, ejecute:

```bash title="Terminal"
  ./gradlew smartbuild
```


#### Cuando una dimensión es una Lista

1. En primer lugar, debe crear una nueva columna en la tabla AD_Sequence para referenciar una lista y hacer lo mismo en la tabla que utiliza la secuencia. La otra opción es utilizar una existente.

	!!! warning
		El nombre de las columnas debe ser el mismo en ambas tablas.

	```sql
	ALTER TABLE public.ad_sequence
	ADD COLUMN <list_name> character varying(60);

	ALTER TABLE public.m_product
	ADD COLUMN <list_name> character varying(60);

	```
	
	!!! note
		Recuerde sustituir `<list_name>` por el nombre deseado.	

2. A continuación, debe crear la columna en `Application` > `Application Dictionary ` >`Tables and Columns`, buscar la **Tabla** `AD_Sequence` y crear la nueva columna.
   Debe establecer el campo **Referencia** de la nueva **Columna** a `List` e indicar la **Referencia clave** correspondiente (o definir una nueva). En el campo Default puede establecer el id de uno de los elementos de la lista y, cuando se cree una nueva Secuencia, la referencia se establecerá automáticamente.
   También debe hacer lo mismo en la tabla que utiliza la secuencia, o puede utilizar una existente.

3. Por último, vuelva a la **Referencia** creada previamente y cree un nuevo registro en la solapa `Dimension List` seleccionando la nueva columna que acaba de crear; a continuación, ejecute:

```bash title="Terminal"
  ./gradlew smartbuild.
```


#### Cambiar secuencia al cambiar dimensión

- Si desea que la secuencia cambie automáticamente cuando cambie la dimensión o la lista configurada, debe implementar un callback o ampliarlo si ya existe.
  El siguiente ejemplo explica cómo implementar el callout, teniendo en cuenta que la dimensión utilizada es la Categoría de producto y que el pedido se introduce automáticamente en el campo Search Key.

```java
public class ChangeSequenceAfterChangeProductCategory extends SimpleCallout {
  @Override
  protected void execute(SimpleCallout.CalloutInfo info) throws ServletException {
    final String strcProductId = info.vars.getStringParameter("inpmProductId");

    if (StringUtils.isBlank(strcProductId)) {
      try {
        OBContext.setAdminMode();
        Tab tab = OBDal.getInstance().get(Tab.class,info.getTabId());
        Field field = tab.getADFieldList()
        .stream()
        .filter(f -> ("inp" + Sqlc.TransformaNombreColumna(f.getColumn().getDBColumnName())).equals("inpvalue"))
        .findFirst()
        .orElse(null);
        String sequenceNumber = Utilities.getDocumentNo(field);
        info.addResult("inpvalue", "<" + sequenceNumber + ">");
      } finally {
        OBContext.restorePreviousMode();
      }
    }
  }
}
```

---
This work is licensed under :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} by [Futit Services S.L](https://etendo.software){target="_blank"}.