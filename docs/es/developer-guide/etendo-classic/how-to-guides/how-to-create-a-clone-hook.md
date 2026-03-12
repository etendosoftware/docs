---
title: Cómo crear un Hook de clonación
tags:
  - Cómo
  - Hook
  - Hook de clonación
---
## Introducción

Etendo permite que cualquier ventana o solapa tenga un botón **Clonar**. Por defecto, utilizará el método `Dal.copy()`, pero esto puede sobrescribirse mediante hooks, para implementar una lógica de clonación personalizada para entidades específicas.

![](../../../assets/drive/0MigjYdnUWzz7TltzquaKnHZBJkr6dhSt8o-c6WbrEYVqHL8R8SNC3lvoTFs-_XOI1qhnCopBhqqzL1THLQ61n4sYhGsRGyT-BtGPes-kykNZO79OUtW55PAmcjxNOA-i9gEK2uaDivHwfJTUdYykeDqL5-qk0UzbVmuGJIpaVufYYmX02sjk3fr.png)

## ¿Cómo crear un Hook de clonación?

Para crear un Hook de clonación, solo tiene que seguir unos pocos pasos:

1. Crear una clase Java de tipo `CloneRecordHook`
2. Usar la anotación `@Qualifier` para definir qué entidad clonará esta clase
3. Sobrescribir los métodos requeridos e implementar su lógica según sus necesidades
4. Habilitar el botón **Clonar** dentro de la solapa asociada con la entidad utilizada en el hook `ExampleCloningHook.java`

```java
@ApplicationScoped

@Qualifier(Invoice.ENTITY_NAME)

public class ExampleCloningHook extends CloneRecordHook {

  @Override
  public boolean shouldCopyChildren(boolean uiCopyChildren) {
    //Implementation
  }

  @Override
  public BaseOBObject preCopy(BaseOBObject originalRecord) {
  	//Implementation
  }

  @Override
  public BaseOBObject postCopy(BaseOBObject originalRecord, BaseOBObject newRecord) {
    //Implementation
  }
}

```

## API del Hook de clonación

Para crear un Hook de clonación, solo tiene que seguir unos pocos pasos:

1. ### `boolean shouldCopyChildren(boolean uiCopyChildren)`

    Este método devolverá un booleano indicando si el hook utilizará `DalUtil.copy()` para copiar las entidades hijas.
    Por ejemplo, clonar una factura y sus entidades hijas significará que las líneas, impuestos, etc. también se clonan en el nuevo documento.

2. ### `BaseOBObject preCopy(BaseOBObject originalRecord)`

    Este método debe devolver el objeto original, que es el parámetro recibido.
    Aquí puede realizar validaciones especiales o lógica adicional relacionada con el registro original, antes de que sea clonado.

3. ### `BaseOBObject postCopy(BaseOBObject originalRecord, BaseOBObject newRecord)`

    Aquí tiene acceso al registro recién creado, resultado de `DalUtil.copy()`.
    Este método es donde debe implementar la lógica especial después de que el registro sea clonado.
    Por ejemplo, si el método `shouldCopyChildren` devuelve `false`, entonces aquí copiaría las entidades hijas con todas las consideraciones especiales necesarias.

4. ### `BaseOBObject copy(BaseOBObject bob, boolean copyChildren)`

    Opcional: sobrescriba este método solo cuando la funcionalidad existente no sea suficiente; aquí debe implementar la funcionalidad de clonación manualmente y llamar a `postCopy()` por su cuenta.

5. ### `boolean shouldResetId()`

    Sobrescriba este método cuando no quiera que `DalUtil.copy()` restablezca los IDs de los objetos copiados. Consulte la documentación de `DalUtil.copy()` para más información. Este método devuelve `true` por defecto.

6. ### `int getPriority()`

    Sobrescriba este método cuando exista un hook para la entidad seleccionada (por ejemplo, ya existe un proceso de clonación implementado para facturas y pedidos) y quiera que se utilice su propio hook en su lugar.
    Se seleccionará y ejecutará el hook con la prioridad más baja por entidad. Devuelve `100` por defecto.

## ¿Cómo ampliar un Hook de clonación ya existente?
La acción de clonación es una acción particular que puede ampliarse creando un nuevo hook, para implementar una lógica personalizada para una entidad específica. Esto tiene la desventaja de que solo se puede usar un hook por entidad, pero existen mecanismos para ampliar esta funcionalidad. Estos son los `preActionHooks` y `postActionHooks`. Puede encontrar más información en la siguiente página: [Cómo crear trabajos y acciones](./how-to-create-jobs-and-actions.md#how-to-extend-an-action-using-preaction-and-postaction-hooks)

---

Este trabajo es una obra derivada de [Guías prácticas](https://wiki.openbravo.com/wiki/Category:HowTo){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.