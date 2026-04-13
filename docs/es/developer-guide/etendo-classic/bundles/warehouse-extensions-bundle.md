---
title: Bundle de extensiones de almacén | Documentación técnica
---

:octicons-package-16: Javapackage: `com.etendoerp.warehouse.extensions`

## Visión general

En esta sección, el usuario puede encontrar información técnica sobre el Bundle de extensiones de almacén.

## Historial de stock

:octicons-package-16: Javapackage: `com.etendoerp.stock.history`

Este módulo se añade al proceso Create Stock History y tiene las siguientes características:

Toma todos los datos de stock de cada producto (presentes en la tabla `m_storage_detail_history`) y los introduce en la tabla `etst_storage_detail_history`, bajo el día en que se ejecutó el proceso. Si ya hay datos cargados en esa fecha, se sobrescriben con los nuevos datos. Todo el proceso se monitoriza mediante logs que pueden visualizarse en la ventana "Solicitud de proceso", en la pestaña "Monitor de proceso" del proceso.

Si el usuario desea realizar cambios en la tabla y quiere que se tengan en cuenta en el proceso de carga de datos, puede hacerlo mediante la funcionalidad de hooks presente en el módulo. Simplemente cree una clase que implemente la interfaz StockHistoryHooks y extienda la clase abstracta StockHistoryPioritizer, e implemente la funcionalidad deseada en el método doExecute. Este método se ejecutará una vez por cada fila añadida a la tabla. Si se implementan múltiples instancias de la misma interfaz, el orden de ejecución puede decidirse mediante el método getPriority. La prioridad viene dada por lo cerca de 0 que esté el número devuelto por este método.

### Cómo definir un hook de Historial de stock

- Defina la clase para el hook, extendiendo la clase abstracta StockHistoryHookPrioritizer e implementando la interfaz StockHistoryHook:

    ```java
    import com.etendoerp.stock.history.hooks.StockHistoryHookPrioritizer;
    import com.etendoerp.stock.history.hooks.StockHistoryHook;

    public class ExampleHook extends StockHistoryHookPrioritizer
      implements StockHistoryHook {
    }
    ```

- Implemente los métodos abstractos de la interfaz y de la clase abstracta:

    ```java
    import com.etendoerp.stock.history.data.ETSTStorageDetailHistory;
    import com.etendoerp.stock.history.hooks.StockHistoryHookPrioritizer;
    import com.etendoerp.stock.history.hooks.StockHistoryHook;

    public class ExampleHook extends StockHistoryHookPrioritizer
      implements StockHistoryHook {

    @Override
    public void exec(ETSTStorageDetailHistory hookObject) throws Exception {
      System.out.println("This is the ExampleHook hook");
    }

    @Override
    public int getPriority() {
      return 0;
    }
    }
    ```

### Desinstalar módulo

Para desinstalar el módulo y evitar problemas futuros con registros huérfanos, debe seguirse una secuencia de pasos:

1. Ejecute la siguiente consulta en la base de datos del entorno
```
DELETE FROM OBUIAPP_GC_TAB 
WHERE AD_TAB_ID = 'C3DB551F2BCA40A79AAF21DBD6D06309';
```

2. Tras finalizar correctamente la consulta, elimine el módulo según el método correspondiente a la instalación (Sources/JARs)

---

Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L.](https://etendo.software){target="_blank"}.