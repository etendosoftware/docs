---
title: Cómo crear tests con Jest
tags:
  - Cómo hacer
  - Jest
  - Test
  - Tests
---

# Cómo crear tests con Jest

## Visión general

[Jest](https://jestjs.io/){target="_blank"} es un framework de testing actualmente utilizado como predeterminado en [create-react-app](https://github.com/facebook/create-react-app){target="_blank"}. Proporciona sus propios métodos de aserción y de mocking, y funciona listo para usar con buena integración con React, Babel y TypeScript.

## Instalación

Desde el directorio del módulo que contiene el `package.json`, instale todas las dependencias ejecutando:

```bash
npm install
```

## Escritura de un test

### Ubicación del archivo

!!! info
    Los tests deben colocarse en la carpeta `web-test`. Los archivos deben tener el sufijo `.test.js` para JavaScript o `.test.ts` para TypeScript.

    Esta es una ruta válida para un archivo de test:

    `modules/com.etendoerp.mymodule/web-test/mycomponent.test.js`

Consulte la [documentación de Jest](https://jestjs.io/docs/getting-started){target="_blank"} como referencia completa.

### Funciones principales

Estas son las funciones clave para construir un archivo de test Jest:

- `describe(name, fn)` — agrupa tests relacionados bajo una etiqueta común. Los bloques pueden anidarse para reflejar la jerarquía del elemento bajo test.
- `it(name, fn)` — define un test individual. El nombre describe el comportamiento esperado.
- `expect(value)` — envuelve el valor real producido por el código bajo test.
- `toBe(expected)` — verifica la igualdad estricta (`===`). Úselo para valores primitivos como cadenas, números y booleanos.
- `toEqual(expected)` — verifica la igualdad profunda. Úselo para objetos y arrays.

### Archivo de test de ejemplo

El siguiente ejemplo está tomado de `org.openbravo.client.application`. Muestra los bloques fundamentales de un archivo de test Jest.

```javascript title="org.openbravo.client.application/web-test/ob-utilities-date.test.js"
require('../web/org.openbravo.client.application/js/utilities/ob-utilities-date');
 
describe('org.openbravo.client.application - OB.Utilities.Date', () => {
  it('The year where we should change century in 2 digits year format is 50', () => {
    expect(OB.Utilities.Date.centuryReference).toEqual(50);
  });
 
  // Describe blocks can be nested to group test cases
  describe('OB.Utilities.Date.normalizeDisplayFormat', () => {
    it('function works', () => {
      const normalizedFormat = OB.Utilities.Date.normalizeDisplayFormat('DD-MM-YYYY');
      expect(normalizedFormat).toEqual('%d-%m-%Y');
    });
 
    it('function works with other input', () => {
      const normalizedFormat = OB.Utilities.Date.normalizeDisplayFormat('DD-MM-YY');
      expect(normalizedFormat).toEqual('%d-%m-%y');
    });
  });
});
```

## Configuración y desmontaje

Jest proporciona cuatro hooks de ciclo de vida que ejecutan código antes o después de los tests. Úselos para preparar el estado compartido y limpiarlo.

| Hook | Se ejecuta |
|------|------|
| `beforeEach` | Antes de cada test en el bloque `describe` actual |
| `afterEach` | Después de cada test en el bloque `describe` actual |
| `beforeAll` | Una vez antes de todos los tests en el bloque `describe` actual |
| `afterAll` | Una vez después de todos los tests en el bloque `describe` actual |

Use `beforeEach` y `afterEach` cuando cada test necesite una instancia nueva e independiente del elemento bajo test. Use `beforeAll` y `afterAll` cuando la configuración o el desmontaje sean costosos y puedan compartirse de forma segura entre todos los tests; por ejemplo, al abrir y cerrar una conexión a base de datos.

El siguiente ejemplo está adaptado de `NpmDependenciesValidator.test.js`. Usa `beforeEach` para crear una instancia nueva del validador e inyectar dependencias simuladas antes de cada test.

```javascript title="NpmDependenciesValidator.test.js"
const { NpmDependenciesValidator } = require('./NpmDependenciesValidator');

describe('NpmDependenciesValidator', () => {
  let validator;

  beforeEach(() => {
    validator = new NpmDependenciesValidator();
    validator.getModules = jest.fn(() => ['module1', 'module2']);
    validator.getPackageJsonPath = jest.fn(module => `${module}/package.json`);
  });

  it('does not return warnings or errors if dependency is not shared between modules', () => {
    validator.readPackageJson = jest.fn(path => {
      if (path === 'module1/package.json') {
        return { dependencies: { lodash: '4.17.15' } };
      } else if (path === 'module2/package.json') {
        return { dependencies: { jest: '26.6.0' } };
      }
      return {};
    });

    const { warnings, errors } = validator.validate();
    expect(warnings).toHaveLength(0);
    expect(errors).toHaveLength(0);
  });
});
```

El siguiente ejemplo muestra la estructura de un par `beforeAll` / `afterAll`:

```javascript
describe('Database integration', () => {
  let connection;

  beforeAll(() => {
    connection = openDatabaseConnection();
  });

  afterAll(() => {
    connection.close();
  });

  it('reads a record', () => {
    const record = connection.find(1);
    expect(record).not.toBeNull();
  });
});
```

Aquí `openDatabaseConnection` se ejecuta una sola vez para toda la suite en lugar de antes de cada test individual, lo que reduce el tiempo de ejecución cuando la operación es costosa.

## Mocking

El mocking reemplaza implementaciones reales con sustitutos controlados para que los tests sigan siendo rápidos y aislados. Jest proporciona tres herramientas principales de mocking.

### jest.mock()

`jest.mock(modulePath, factory)` reemplaza un módulo completo. Jest intercepta la llamada `require` o `import` y devuelve el resultado de la función factory en lugar del módulo real.

El siguiente ejemplo está adaptado de `User.test.ts`. Reemplaza `@react-native-async-storage/async-storage` con un objeto de funciones rastreadas.

```typescript title="User.test.ts"
jest.mock('@react-native-async-storage/async-storage', () => ({
  setItem: jest.fn(),
  getItem: jest.fn(),
  removeItem: jest.fn(),
}));

const AsyncStorage = require('@react-native-async-storage/async-storage');
const User = require('./User');

describe('User Store', () => {
  let userStore;

  beforeEach(() => {
    userStore = new User();
    jest.clearAllMocks();
  });

  it('clears user data and removes stored tokens on logout', async () => {
    userStore.token = 'testToken';
    userStore.user = 'testUser';

    await userStore.logout();

    expect(AsyncStorage.removeItem).toHaveBeenCalledWith('token');
    expect(AsyncStorage.removeItem).toHaveBeenCalledWith('user');
    expect(userStore.token).toBeUndefined();
  });
});
```

`jest.clearAllMocks()` en `beforeEach` restablece los contadores de llamadas y los valores de retorno entre tests para que un test no afecte las aserciones de otro.

### jest.fn()

`jest.fn()` crea una función simulada independiente. Registra cada llamada que recibe y los argumentos que se le pasan. Asigne un valor de retorno con `.mockReturnValue(value)` o un valor de retorno de uso único con `.mockReturnValueOnce(value)`.

```javascript
const fetchUser = jest.fn().mockReturnValue({ id: 1, name: 'Ana' });

fetchUser(1);

expect(fetchUser).toHaveBeenCalledWith(1);
expect(fetchUser).toHaveReturnedWith({ id: 1, name: 'Ana' });
```

### jest.spyOn()

`jest.spyOn(object, methodName)` envuelve un método existente sin reemplazarlo. La implementación original sigue ejecutándose a menos que se encadene `.mockImplementation()`. Úselo cuando se necesita el comportamiento real del método pero también se requiere el seguimiento de llamadas.

```javascript
const { NpmDependenciesValidator } = require('./NpmDependenciesValidator');

describe('NpmDependenciesValidator - spy', () => {
  let validator, spy;

  beforeEach(() => {
    validator = new NpmDependenciesValidator();
    spy = jest.spyOn(validator, 'validate');
  });

  afterEach(() => {
    spy.mockRestore(); // restores the original method and prevents the spy from persisting across tests
  });

  it('calls validate once', () => {
    validator.validate();
    expect(spy).toHaveBeenCalledTimes(1);
  });
});
```

## Tests asíncronos

Jest maneja `async`/`await` de forma nativa. Marque el callback del test como `async` y use `await` en las promesas. Jest espera a que la promesa devuelta se resuelva antes de evaluar las aserciones.

El siguiente ejemplo está adaptado de `User.test.ts`. Verifica que una llamada de inicio de sesión rellena el store con los datos del usuario y un token. El mock de `etrest` simula la respuesta del servidor: `getUserId` devuelve el ID de usuario utilizado internamente por el store, mientras que el valor del token es establecido por la propia lógica de inicio de sesión del store tras resolver la llamada simulada.

```typescript title="User.test.ts"
jest.mock('etrest', () => ({
  OBRest: {
    loginWithUserAndPassword: jest.fn(),
    getInstance: jest.fn(() => ({
      getOBContext: jest.fn(() => ({
        getUserId: () => 'testUserId',
      })),
    })),
  },
}));

const { OBRest } = require('etrest');
const User = require('./User');

describe('login', () => {
  let userStore;

  beforeEach(() => {
    userStore = new User();
    jest.clearAllMocks();
  });

  it('logs in the user and sets up store data', async () => {
    const username = 'testUser';
    const password = 'testPass';

    await userStore.login(username, password);

    expect(OBRest.loginWithUserAndPassword).toHaveBeenCalledWith(username, password);
    expect(userStore.token).toBe('testToken');
    expect(userStore.user).toBe(username);
  });
});
```

!!! warning
    Siempre use `await` en la llamada bajo test antes de realizar las aserciones. Sin `await`, el test finaliza antes de que la promesa se resuelva, lo que puede generar falsos positivos o tests inestables por rechazos no manejados.

Si el test espera que una promesa sea rechazada, use `expect(...).rejects.toThrow()`:

```javascript
const User = require('./User');

describe('login - invalid credentials', () => {
  let userStore;

  beforeEach(() => {
    userStore = new User();
    jest.clearAllMocks();
  });

  it('throws on invalid credentials', async () => {
    await expect(userStore.login('', '')).rejects.toThrow('Invalid credentials');
  });
});
```

## Tests parametrizados

`it.each` ejecuta la misma lógica de test con múltiples pares de entrada/salida. Esto elimina código de test duplicado y hace que la intención quede explícita en el nombre del test.

El siguiente ejemplo está tomado de `ob-utilities-number.test.js`. Verifica que las cadenas en notación científica se conviertan correctamente a notación decimal.

```javascript title="org.openbravo.client.application/web-test/ob-utilities-number.test.js"
describe('OB.Utilities.Number.ScientificToDecimal', () => {
  const decimalSeparator = '.';
  it.each`
    number       | expected
    ${'-5E-4'}   | ${'-0.0005'}
    ${'-5E4'}    | ${'-50000'}
    ${'5E7'}     | ${'50000000'}
  `('converts $number to $expected', ({ number, expected }) => {
    expect(OB.Utilities.Number.ScientificToDecimal(number, decimalSeparator)).toEqual(expected);
  });
});
```

La sintaxis de plantilla literal define una tabla. La primera fila es el encabezado de columna. Cada fila siguiente es una ejecución de test. Jest interpola `$number` y `$expected` en el nombre del test para que cada caso sea distinguible en la salida.

`it.each` también acepta un array de arrays cuando no se requieren encabezados de columna:

```javascript
const decimalSeparator = '.';
it.each([
  ['-5E-4', '-0.0005'],
  ['-5E4',  '-50000'],
  ['5E7',   '50000000'],
])('converts %s to %s', (number, expected) => {
  expect(OB.Utilities.Number.ScientificToDecimal(number, decimalSeparator)).toEqual(expected);
});
```

## Ejecutar tests y cobertura

Desde el directorio del módulo, ejecute todos los tests:

```bash
npm test
```

Para ejecutar un único archivo de test:

```bash
npm test -- web-test/mycomponent.test.js
```

Para ejecutar los tests y generar un informe de cobertura, ejecute:

```bash
npm run coverage
```

El informe de cobertura se genera en el directorio `coverage/`. Abra `coverage/lcov-report/index.html` en un navegador para ver un desglose detallado por archivo, incluyendo cobertura de líneas, sentencias, ramas y funciones.


Este trabajo es una obra derivada de [How to Create Jest testcases](https://wiki.openbravo.com/wiki/How_to_create_Jest_testcases){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.
