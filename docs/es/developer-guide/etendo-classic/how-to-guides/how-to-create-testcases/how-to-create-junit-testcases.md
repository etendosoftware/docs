---
title: Cómo crear casos de prueba JUnit
tags:
  - Cómo hacer
  - JUnit
  - Prueba
  - Casos de prueba
---

# Cómo crear casos de prueba JUnit

## Visión general

Este procedimiento se centrará en crear un caso de prueba haciendo uso de las clases `OBBaseTest` y `WeldBaseTest`. El caso de prueba comprobará que nuestro sistema tiene al menos un Usuario con contraseña. Para ello, utilizaremos el nuevo enfoque DAL para acceder a la base de datos.

En programación informática, las **pruebas unitarias** son un método de diseño y desarrollo de software en el que el programador adquiere confianza en que las unidades individuales del código fuente son aptas para su uso. Una unidad es la parte más pequeña comprobable de una aplicación. En programación procedimental, una unidad puede ser un programa individual, una función, un procedimiento, etc., mientras que en programación orientada a objetos, la unidad más pequeña es un método, que puede pertenecer a una clase base/superclase, una clase abstracta o una clase derivada/subclase.

Todos los nuevos desarrollos deben pertenecer a un módulo que no sea el módulo _core_.
## Preparación del entorno de desarrollo

!!! info
    Asegúrese de que en el archivo raíz **build.gradle** ha incluido el plugin `com.etendoerp.testing.gradleplugin`. Si no lo tiene, consulte la documentación del [Plugin de pruebas de Etendo](../../developer-tools/etendo-testing-plugin.md#installation) para instalarlo y, por último, recargue *Gradle* desde *IntelliJ*.

En primer lugar, necesita crear un directorio **src-test** en el directorio del paquete de su módulo en el proyecto Etendo.

``` 
modules
└── com.etendoerp.example
    └── src-test                <-- source of the test cases 
        └── src
            └── com.etendoerp.example
                └── EtendoTest.java
```

Ahora, está listo para trabajar con casos de prueba.
## Creación del caso de prueba

### Heredar de `OBBaseTest`

Todos los casos de prueba del core son subclases de `OBBaseTest` (`org.openbravo.test.base.OBBaseTest`). Esta clase gestiona todos los pasos necesarios para inicializar la *Capa de Acceso a Datos*, se encarga de la gestión de transacciones y proporciona un conjunto de utilidades (métodos) para trabajar con el contexto de Openbravo (OBContext).

!!! info
    Al escribir casos de prueba para Etendo que impliquen inyección de dependencias o requieran la ejecución de observadores de eventos de DAL, se recomienda extender `org.openbravo.base.weld.test.WeldBaseTest` en lugar de `org.openbravo.test.base.OBBaseTest`.
    `OBBaseTest` tiene limitaciones relacionadas con **Contexts and Dependency Injection (CDI)**, y no admite determinadas funcionalidades que están disponibles al usar pruebas con WeldBaseTest. Esta última es una subclase de `OBBaseTest` y proporciona acceso a la infraestructura completa de DAL, lo que la hace más adecuada para escenarios que implican CDI y observadores de eventos.
    Asegúrese de usar `WeldBaseTest` para aprovechar todas las capacidades de la inyección de dependencias y de los observadores de eventos de DAL en sus casos de prueba.


### Creación de la Clase Java

  - Abra IntelliJ IDE. 
  - Cree una nueva estructura de carpetas bajo la carpeta `modules`: `modules/com.etendoerp.examples/src-test/src/com.etendoerp.example` 
  - Cree una nueva *Clase Java* con el siguiente contenido: 

  ```java title="ExampleTest.java" 
  package com.etendoerp.example;
  
  import static org.junit.Assert.assertTrue;
  
  import java.util.List;
  
  import org.junit.jupiter.api.BeforeEach;
  import org.junit.jupiter.api.Test;
  import org.junit.jupiter.api.TestMethodOrder;
  import org.junit.jupiter.api.MethodOrderer.OrderAnnotation;
  import org.openbravo.dal.core.OBContext;
  import org.openbravo.dal.service.OBCriteria;
  import org.openbravo.dal.service.OBDal;
  import org.openbravo.model.ad.access.User;
  import org.openbravo.base.weld.test.WeldBaseTest;
  import org.openbravo.test.base.TestConstants;
  import org.openbravo.client.kernel.RequestContext;
  import org.openbravo.base.secureApp.VariablesSecureApp;


  @TestMethodOrder(OrderAnnotation.class)
  public class ExampleTest extends WeldBaseTest {

    @Override
    @BeforeEach
    public void setUp() throws Exception {
      super.setUp();
      OBContext.setOBContext(TestConstants.Users.SYSTEM, TestConstants.Roles.SYS_ADMIN,
          TestConstants.Clients.SYSTEM, TestConstants.Orgs.MAIN);
      VariablesSecureApp vsa = new VariablesSecureApp(
          OBContext.getOBContext().getUser().getId(),
          OBContext.getOBContext().getCurrentClient().getId(),
          OBContext.getOBContext().getCurrentOrganization().getId(),
          OBContext.getOBContext().getRole().getId()
      );
      RequestContext.get().setVariableSecureApp(vsa);
    }
  
    @Test
    public void testUsersCount() {
      final OBCriteria<User> uCriteria = OBDal.getInstance().createCriteria(User.class);
      final List<User> uList = uCriteria.list();
      int userCount = 0;
      for (User u: uList) {
        if (u != null && u.getPassword() != null && !u.getPassword().isEmpty())
          userCount++;
      }
      assertTrue(userCount > 0, "There should be at least one user with password");
      System.out.println("Total of users with password: " + (userCount));
    }
  }
  ```

**Comprender la clase**

Acaba de crear una nueva clase llamada *ExampleTest* que extiende de la clase `WeldBaseTest`.

```java
@TestMethodOrder(OrderAnnotation.class)
```

Esta anotación especifica que los métodos de prueba se ejecutarán en el orden indicado por la anotación `@Order`. Puede usar `@Order` en los métodos de prueba para definir su orden de ejecución.

!!! note "Orden de ejecución de los métodos de prueba"
    Hasta ahora, los métodos simplemente se invocaban en el orden devuelto por la *API* de reflexión. Sin embargo, usar el orden de la *JVM* no es recomendable, ya que la plataforma Java no especifica ningún orden en particular. Por supuesto, un código de prueba bien escrito no debería asumir ningún orden, pero algunos lo hacen, y un fallo predecible es mejor que un fallo aleatorio en determinadas plataformas.


```java
public void testUsersCount() {}
```

Esta clase tiene una función *testUsersCount*. Tenga en cuenta que en **JUnit 5** ya no se requiere la convención de nombres de métodos, ya que la anotación `@Test` es la que identifica un método de prueba. No obstante, por claridad, sigue siendo una buena práctica usar una convención de nombres para los métodos de prueba.

```java
@Override
@BeforeEach
public void setUp() throws Exception {
  super.setUp();
  OBContext.setOBContext(TestConstants.Users.SYSTEM, TestConstants.Roles.SYS_ADMIN,
      TestConstants.Clients.SYSTEM, TestConstants.Orgs.MAIN);
  VariablesSecureApp vsa = new VariablesSecureApp(
      OBContext.getOBContext().getUser().getId(),
      OBContext.getOBContext().getCurrentClient().getId(),
      OBContext.getOBContext().getCurrentOrganization().getId(),
      OBContext.getOBContext().getRole().getId()
  );
  RequestContext.get().setVariableSecureApp(vsa);
}
```

!!! note
    Observe la anotación `@BeforeEach` en lugar de `@Before` de JUnit 4. Este método establece el contexto como si un **Administrador del sistema** hubiera iniciado sesión en la aplicación. También puede establecer el contexto como si otro usuario hubiera iniciado sesión en la aplicación.

```java
final OBCriteria<User> uCriteria = OBDal.getInstance().createCriteria(User.class);
final List<User> uList = uCriteria.list();
```

Utiliza la instancia `OBDal` para crear un nuevo objeto `OBCriteria`, y lo usa para listar todos (ya que no estamos filtrando) los usuarios en la base de datos.

```java
int userCount = 0;
for (User u: uList) {
  if (u != null && u.getPassword() != null && !u.getPassword().isEmpty())
    userCount++;
}
```

Recorremos la colección uList e incrementamos la variable userCount si el usuario tiene contraseña.

```java
assertTrue(userCount > 0, "There should be at least one user with password");
```

Afirmamos que userCount es mayor que 0.  
Observe el parámetro de mensaje opcional en los métodos de aserción de JUnit 5.

```java
System.out.println("Total of users with password: " + (userCount));
```

Por último, imprimimos el total de usuarios con contraseña solo a modo de registro.

### Gestión de transacciones

Una pregunta que puede surgir al ver el código anterior es: ¿dónde se realiza la gestión de transacciones de base de datos? La respuesta es que esto lo gestiona la clase `WeldBaseTest` y la capa de acceso a datos de Etendo:

  * Una transacción se inicia automáticamente en el primer acceso a base de datos en los casos de prueba. Esto lo realiza la *Capa de Acceso a Datos*. 
  * Una transacción se confirma (cuando no se produce ninguna excepción) o se revierte (cuando se produce una excepción). 

La clase `WeldBaseTest` detecta automáticamente si se ha producido una excepción o no.

Sin duda, hay casos en los que tiene sentido tener más control sobre las transacciones de base de datos. Hay varios métodos relevantes que pueden ser útiles en ese caso:

  * `OBDal.getInstance().flush()`: vuelca las consultas de actualización/inserción en hibernate a la base de datos. 
  * `OBDal.getInstance().commitAndClose()`: confirma la transacción y cierra la sesión. Se inicia automáticamente una nueva sesión/transacción en el siguiente acceso a base de datos. 
  * `OBDal.getInstance().rollbackAndClose()`: revierte y cierra las transacciones. Se inicia automáticamente una nueva sesión/transacción en el siguiente acceso a base de datos. 

!!! info
    Los observadores de eventos de DAL no se disparan dentro de los casos de prueba que extienden la clase `OBBaseTest`. Para que funcionen, se requieren casos de prueba que extiendan `WeldBaseTest`. 

**Sin efectos secundarios**

Un caso de prueba a menudo cambiará los datos en la base de datos subyacente. La mayoría de las veces, no es viable configurar una base de datos de prueba completamente nueva para cada ejecución de pruebas. Por lo tanto, los casos de prueba deben desarrollarse de forma que no tengan efectos secundarios. Esto significa:

  * Cuando el caso de prueba cambia datos, entonces debería tener un método de prueba que se ejecute como el último método de prueba y que limpie/repare los datos. 
  * Este método de limpieza también debería limpiar los datos que hayan quedado de ejecuciones de prueba anteriores. Para este problema común debe usarse la anotación `@AfterAll`. Este método se ejecuta automáticamente al final de la clase.

Este último punto es importante porque siempre puede haber razones por las que durante una prueba no se realice el paso de limpieza. Por ejemplo, porque la ejecución de pruebas se detiene antes de que se complete la limpieza.

### Ejecutar pruebas

Etendo dispone de varias tareas de Gradle que ejecutan los casos de prueba:

``` bash title="Terminal"
./gradlew test`
```
Esta tarea ejecutará todas las pruebas definidas en Etendo y en los módulos instalados.

``` bash title="Terminal"
./gradlew test --tests <package>
```

Esta tarea le permite ejecutar pruebas específicamente para un paquete o clase.

Por ejemplo: `./gradlew test --tests "com.etendoerp.example.ExampleTest"` o `./gradlew test --tests "com.etendoerp.example.*"`

!!! info
    Si se han implementado o modificado pruebas para [etendo_core](https://github.com/etendosoftware/etendo_core.git) y el paquete pertenece a org.openbravo, asegúrese de que la clase esté incluida en `StandaloneTestSuite` o `WebserviceTestSuite`.

**El resultado**

Para poder ejecutar sus casos de prueba:

- Haga clic derecho en la clase `ExampleTest`. 
- Seleccione Ejecutar `ExampleTest`.
    ![](../../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-junit-testcases/how-to-create-junit-testcases-6.png)
- Puede comprobar el resultado del caso de prueba en la vista de JUnit y la salida de sus pruebas en la vista de Consola:

    ![](../../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-junit-testcases/how-to-create-junit-testcases-7.png)

    Además, en la carpeta build puede encontrar el informe de la ejecución de las pruebas, y puede abrirlo en su navegador.

    ``` 
    build
    └── reports
        └── tests 
            └── test
                └── index.html
    ```

### Ejecutar pruebas con cobertura

Para ejecutar sus pruebas y visualizar la **cobertura de código** de su módulo:

-  En **IntelliJ IDEA**, localice su paquete de pruebas (por ejemplo: `src-test/java/com.etendoerp.example`).
-  Haga clic derecho en la carpeta o clase de prueba.
-  Seleccione **Ejecutar pruebas en 'com.etendoerp.example' con cobertura**.

    ![Ejecutar con cobertura](../../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-junit-testcases/how-to-create-junit-testcases-8.png)

**El informe de cobertura**

Una vez que finalicen las pruebas, **IntelliJ** mostrará la **ventana de herramientas Cobertura**, indicando el porcentaje de código cubierto por sus pruebas.

![Resultado de cobertura](../../../../assets/developer-guide/etendo-classic/how-to-guides/how-to-create-junit-testcases/how-to-create-junit-testcases-9.png)

| Métrica        | Descripción                                                              |
|---------------|---------------------------------------------------------------------------|
| **Clase %**   | Porcentaje de clases que tienen al menos una prueba que las cubra.        |
| **Método %**  | Porcentaje de métodos ejecutados durante las pruebas.                     |
| **Línea %**   | Porcentaje de líneas de código fuente que se ejecutaron.                  |
| **Rama %**    | Cobertura de ramas condicionales (`if`, `else`, `switch`, etc).           |
## Funcionalidades avanzadas de pruebas


### Pruebas parametrizadas

!!! info 
    Para más información, visite: [Prueba parametrizada de JUnit](https://junit.org/junit5/docs/current/user-guide/#writing-tests-parameterized-tests){target="_blank"}.

### Extensiones

En **JUnit 5**, el concepto de Rules ha sido reemplazado por las *Extensiones*.

!!! info
    Para más información, visite la guía de [Extensión](https://junit.org/junit5/docs/current/user-guide/#extensions){target="_blank"}.

### Aserciones y Hamcrest 1.13

Hamcrest es un framework para escribir objetos matcher que permite definir reglas de *conciliación* de forma declarativa. Hay varias situaciones en las que los matchers son invaluables, como la *validación de la UI* o el *filtrado de datos*, pero es en el ámbito de escribir pruebas flexibles donde los matchers se usan con mayor frecuencia.

Al escribir pruebas, a veces es difícil encontrar el equilibrio adecuado entre sobreespecificar la prueba y no especificar lo suficiente (haciendo que la prueba sea menos valiosa). Disponer de una herramienta que le permita seleccionar con precisión el aspecto bajo prueba y describir los valores que debería tener, con un nivel de precisión controlado, ayuda enormemente a la hora de escribir pruebas.

!!! info 
    Para más información, visite: [Hamcrest](https://hamcrest.org/){target="_blank"}.

### Matchers JSON
  
Etendo proporciona un conjunto de matchers que pueden ser útiles al realizar aserciones sobre JSONObjects o JSONArrays.

**equal**

Concuerda cuando el `JSONObject` examinado tiene exactamente el mismo número de propiedades con los mismos valores que el esperado. El orden de las claves no se tiene en cuenta. Admite propiedades matcher.

```java  
@Test
public void testEqual() {
  JSONObject json1 = new JSONObject(Map.of("p1", 1, "p2", "abcd"));
  JSONObject json2 = new JSONObject(Map.of("p1", 1, "p2", "abcd"));
  JSONObject json3 = new JSONObject(Map.of("p2", "abcd", "p1", 1));
  JSONObject json4 = new JSONObject(Map.of("p1", 1, "p2", "efgh"));
  JSONObject json5 = new JSONObject(Map.of("p1", 1));
  JSONObject json6 = new JSONObject(Map.of("p1", greaterThan(0), "p2", startsWith("abc"))); // matcher properties
 
  assertThat("JSON objects are equal", json1, equal(json2));
  assertThat("JSON objects are equal", json1, equal(json3));
  assertThat("JSON objects are not equal", json1, not(equal(json4)));
  assertThat("JSON objects are not equal", json1, not(equal(json5)));
  assertThat("JSON objects are equal", json1, equal(json6));
}
```

**matchesObject**

Concuerda cuando el JSONObject examinado contiene las propiedades con los mismos valores que el esperado. El orden de las claves no se tiene en cuenta. Admite propiedades matcher.

```java
@Test
public void testMatchesObject() {
  JSONObject json1 = new JSONObject(Map.of("p1", 1, "p2", "abcd"));
  JSONObject json2 = new JSONObject(Map.of("p1", 1, "p2", "abcd"));
  JSONObject json3 = new JSONObject(Map.of("p2", "abcd", "p1", 1));
  JSONObject json4 = new JSONObject(Map.of("p1", 1, "p2", "efgh"));
  JSONObject json5 = new JSONObject(Map.of("p1", 1));
  JSONObject json6 = new JSONObject(Map.of("p1", 1, "p2", "abcd", "p3", "abcd"));
  JSONObject json7 = new JSONObject(Map.of("p1", greaterThan(0), "p2", "abcd"));
 
  assertThat("JSON object match", json1, matchesObject(json2));
  assertThat("JSON object match", json1, matchesObject(json3));
  assertThat("JSON object does not match", json1, not(matchesObject(json4)));
  assertThat("JSON object match", json1, matchesObject(json5));
  assertThat("JSON object does not match", json1, not(matchesObject(json6)));
  assertThat("JSON object match", json1, matchesObject(json7));
}
```

**hasItems**

Se utiliza para conciliar los elementos de un `JSONArray`. Este matcher puede utilizarse con dos tipos diferentes de argumentos.

Si se pasa un array de objetos, entonces concuerda cuando el `JSONArray` examinado contiene todos los objetos recibidos. El orden de los objetos no se tiene en cuenta.

```java   
@Test
public void testHasItems() {
  JSONObject json1 = new JSONObject(Map.of("p1", 1, "p2", "abcd"));
  JSONObject json2 = new JSONObject(Map.of("p2", 2, "p3", "efgh"));
  JSONArray array = new JSONArray();
  array.put(json1);
  array.put(json2);
  array.put(5);
  JSONObject json3 = new JSONObject(Map.of("p2", 2, "p3", startsWith("e")));
  JSONObject json4 = new JSONObject(Map.of("p2", 2, "p3", "ijkl"));
 
  assertThat("JSON array has items", array, hasItems(5, json3));
  assertThat("JSON array does not have items", array, not(hasItems(4, json3)));
  assertThat("JSON array does not have items", array, not(hasItems(json4)));
}
```

También admite recibir un array de matchers de Hamcrest. En ese caso, concuerda cuando el JSONArray examinado concuerda con todos los matchers recibidos.

```java
@Test
public void testHasItems() {
  JSONObject json1 = new JSONObject(Map.of("p1", 1, "p2", "abcd"));
  JSONObject json2 = new JSONObject(Map.of("p2", 2, "p3", "efgh"));
  JSONArray array = new JSONArray();
  array.put(json1);
  array.put(json2);
  array.put(5);
  JSONObject json3 = new JSONObject(Map.of("p2", 2, "p3", startsWith("e")));
  JSONObject json4 = new JSONObject(Map.of("p1", 1));
  JSONObject json5 = new JSONObject(Map.of("p2", 2, "p3", "ijkl"));
 
  assertThat("JSON array has items", array, hasItems(greaterThan(4), equal(json3)));
  assertThat("JSON array has items", array, hasItems(greaterThan(4), matchesObject(json4)));
  assertThat("JSON array does not have items", array, not(hasItems(greaterThan(5))));
  assertThat("JSON array does not have items", array, not(hasItems(equal(json5))));
}
```

### Simulación con Mockito en JUnit

Al escribir pruebas unitarias, a menudo es necesario simular el comportamiento de dependencias externas. [Mockito](https://site.mockito.org/) es una biblioteca popular de simulación para Java que le permite crear objetos mock para aislar el código bajo prueba de sus dependencias.

**Formas de crear mocks**

Hay dos enfoques principales para crear mocks en Mockito:

1. Uso de anotaciones

    La forma más limpia es usar anotaciones:

    ```java
    @ExtendWith(MockitoExtension.class)
    class UserServiceTest {
        
        @Mock
        private UserRepository userRepository;
        
        @InjectMocks
        private UserService userService;
        
        @Test
        void testGetUserById() {
            // Arrange
            String userId = "123";
            User mockUser = new User(userId, "John Doe");
            when(userRepository.findById(userId)).thenReturn(mockUser);
            
            // Act
            User result = userService.getUserById(userId);
            
            // Assert
            assertEquals(mockUser.getName(), result.getName());
            verify(userRepository).findById(userId);
        }
    }
    ```

    En este ejemplo:

    - `@ExtendWith(MockitoExtension.class)` integra Mockito con **JUnit 5**
    - `@Mock` crea una implementación mock de UserRepository
    - `@InjectMocks` inyecta los mocks creados en UserService

2. Creación manual de mocks

    También puede crear mocks manualmente:

    ```java
    @Test
    void testUserServiceManualMocks() {
        // Create mocks manually
        UserRepository mockRepo = mock(UserRepository.class);
        UserService service = new UserService(mockRepo);
        
        // Configure behavior
        User mockUser = new User("123", "Jane Doe");
        when(mockRepo.findById("123")).thenReturn(mockUser);
        
        // Execute and verify
        User result = service.getUserById("123");
        assertEquals("Jane Doe", result.getName());
    }
    ```

#### Simulación de métodos estáticos

Para simular métodos estáticos, debe usar `mockito-inline`. Esto permite simular clases con métodos estáticos, como utilidades o fachadas de servicio.

**Ejemplo con MockedStatic:**

```java
@Test
void testWithStaticMock() {
    // The static mock must be created inside a try-with-resources block
    // or closed manually to prevent memory leaks
    try (MockedStatic<DateUtils> dateUtilsMock = mockStatic(DateUtils.class)) {
        // Configure the behavior of the static method
        LocalDate fixedDate = LocalDate.of(2025, 4, 8);
        dateUtilsMock.when(DateUtils::getCurrentDate).thenReturn(fixedDate);
        
        // Now DateUtils.getCurrentDate() will return our fixed date
        LocalDate result = DateUtils.getCurrentDate();
        
        assertEquals(fixedDate, result);
        dateUtilsMock.verify(DateUtils::getCurrentDate);
    }
}
```

#### Simulación de dependencias normales y estáticas

A continuación se muestra un ejemplo que combina mocks normales y estáticos:

```java
@ExtendWith(MockitoExtension.class)
class PaymentProcessorTest {
    
    @Mock
    private PaymentGateway paymentGateway;
    
    @InjectMocks
    private PaymentProcessor paymentProcessor;
    
    @Test
    void testProcessPayment() {
        // Regular object mock
        Payment payment = new Payment("123", 100.00);
        TransactionResult mockResult = new TransactionResult(true, "Approved");
        when(paymentGateway.submitPayment(payment)).thenReturn(mockResult);
        
        // Static method mock for current date
        try (MockedStatic<TransactionUtils> transUtilsMock = mockStatic(TransactionUtils.class)) {
            LocalDateTime fixedDateTime = LocalDateTime.of(2025, 4, 8, 15, 30);
            transUtilsMock.when(TransactionUtils::getCurrentDateTime).thenReturn(fixedDateTime);
            
            // Act
            TransactionResponse response = paymentProcessor.processPayment(payment);
            
            // Assert
            assertTrue(response.isSuccessful());
            assertEquals(fixedDateTime, response.getTransactionDate());
            
            // Verify that methods were called correctly
            verify(paymentGateway).submitPayment(payment);
            transUtilsMock.verify(TransactionUtils::getCurrentDateTime);
        }
    }
}
```

#### Buenas prácticas de simulación

1. **Cerrar mocks estáticos**: los mocks estáticos deben cerrarse para evitar fugas de memoria.

    ```java
    try (MockedStatic<UtilityClass> mock = mockStatic(UtilityClass.class)) {
        // Use the static mock
    } // Automatically closed
    ```

2. **Verificar interacciones**: use `verify()` para confirmar que se llamaron los métodos esperados.

    ```java
    verify(mockObject).someMethod();
    verify(mockObject, times(3)).someMethod();
    verify(mockObject, never()).otherMethod();
    ```

3. **Usar anotaciones para casos simples**: anotaciones como `@Mock` y `@InjectMocks` hacen que el código sea más legible.

4.  **Restablecer mocks cuando sea necesario**: si necesita reutilizar un mock con un comportamiento diferente:

    ```java
    reset(mockObject);
    ```

### Pruebas de solicitudes

En general, las pruebas unitarias no requieren que se ejecute una instancia de Etendo en *Tomcat*. Pero en algunos casos se desea probar cómo funcionan las solicitudes. Dependiendo de la solicitud que se quiera probar, se deben extender diferentes clases:

  - _Servicios web REST_. Se debe extender `BaseWSTest`; gestiona la autenticación y proporciona métodos para ejecutar solicitudes, analizar resultados `XML`, etc.
  - _Otras solicitudes_ (como datasources). Se pueden extender las clases `BaseDataSourceTestNoDal` o `BaseDataSourceTestDal` (dependiendo de si el caso de prueba requiere o no DAL). De forma similar a los **servicios web**, proporciona gestión de autenticación, así como métodos de utilidad para realizar solicitudes.

### Pruebas de Contexts and Dependency Injection (CDI)
  
Los casos de prueba por defecto que extienden la clase `org.openbravo.test.base.OBBaseTest` no pueden hacer uso de la inyección de dependencias. Para poder usarla, es necesario extender la clase `org.openbravo.base.weld.test.WeldBaseTest`. Esta también es una subclase de `OBBaseTest`, por lo que pone a disposición toda la infraestructura de DAL.

`WeldBaseTest` utiliza internamente contenedores **Weld SE** para el soporte de CDI.

Ejemplo de un caso de prueba inyectando dependencias:

```java
public class CdiInfrastructure extends WeldBaseTest {
 
  @Inject
  private ApplicationScopedBean applicationBean;
 
  @Inject
  private SessionScopedBean sessionBean;
 
  @Inject
  private RequestScopedBean requestBean;
 
  /** beans are correctly injected */
  @Test
  public void beansAreInjected() {
    assertNotNull(applicationBean, "application bean is injected");
    assertNotNull(sessionBean, "session bean is injected");
    assertNotNull(requestBean, "request bean is injected");
  }
}
```

#### Ámbitos

Los ámbitos de aplicación y de sesión se comparten entre todos los casos de prueba de la misma clase, mientras que se crea un nuevo ámbito de solicitud para cada método de caso de prueba. El ámbito de aplicación se restablece para cada nueva clase.

```java
/** starts application and session scopes */
@Test
@Order(1)
public void start() {
  applicationBean.setValue("application");
  sessionBean.setValue("session");
  requestBean.setValue("request");
 
  assertEquals("application", applicationBean.getValue());
  assertEquals("session", sessionBean.getValue());
  assertEquals("request", requestBean.getValue());
}
 
/** application and session scopes are preserved but not request scope */
@Test
@Order(2)
public void applicationAndSessionShouldBeKept() {
  assertEquals("application", applicationBean.getValue());
  assertEquals("session", sessionBean.getValue());
  assertNull(requestBean.getValue());
}
```

#### Parametrización

En **JUnit 5**, las pruebas parametrizadas se admiten de forma nativa mediante la anotación `@ParameterizedTest`, eliminando la necesidad de runners o rules especiales:

```java
public class ParameterizedCdi extends WeldBaseTest {
  
  @ParameterizedTest
  @ValueSource(strings = {"param1", "param2", "param3"})
  public void testWithParameters(String parameter) {
    assertNotNull(parameter);
    assertTrue(parameter.startsWith("param"));
  }
  
  @ParameterizedTest
  @CsvSource({
    "param1, 1",
    "param2, 2",
    "param3, 3"
  })
  public void testWithMultipleParameters(String name, int value) {
    assertNotNull(name);
    assertTrue(name.endsWith(String.valueOf(value)));
  }
  
  @ParameterizedTest
  @MethodSource("provideParameters")
  public void testWithMethodSource(String parameter) {
    assertNotNull(parameter);
    assertTrue(parameter.startsWith("param"));
  }
  
  static Stream<String> provideParameters() {
    return Stream.of("param1", "param2", "param3");
  }
}
```

En este ejemplo, el primer caso de prueba (testWithParameters) se ejecutará 3 veces, cada vez con los valores de parámetro param1, param2 y param3.

A diferencia de cuando se usa el runner `Parameterized.class`, estas 3 ejecuciones se ven como una única ejecución (`Parameterized.class` mostraría 3 ejecuciones independientes), lo que provoca que, si por ejemplo falla la primera ejecución, el resto no se ejecutará.

#### Observadores de eventos DAL

Dado que los observadores de eventos DAL hacen uso de CDI para funcionar, no se ejecutan en casos de prueba estándar que extienden `OBBaseTest`.

Esta limitación no aplica cuando se usan pruebas `WeldBaseTest`.

---

Este trabajo es una obra derivada de [Cómo crear casos de prueba JUnit](https://wiki.openbravo.com/wiki/How_to_create_JUnit_testcases){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Este trabajo está licenciado bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.