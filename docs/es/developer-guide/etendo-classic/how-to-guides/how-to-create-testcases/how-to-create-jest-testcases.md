---
title: Cómo crear casos de prueba con Jest
tags:
  - Cómo hacer
  - Jest
  - Prueba
  - Casos de prueba
---

# Cómo crear casos de prueba con Jest

## Visión general

[Jest](https://jestjs.io/){target="_blank"} es un framework de pruebas y actualmente utilizado como framework de pruebas predeterminado en [create-react-app](https://github.com/facebook/create-react-app){target="_blank"}. A diferencia de Mocha, es un ejecutor de pruebas con una filosofía definida y proporciona sus propios métodos de aserción y de mocking. La principal ventaja es que funciona listo para usar y tiene buena integración con tecnologías como React, Babel y TypeScript.

## Instalación

Instale todas las dependencias ejecutando:

```bash
npm install
```

## Creación de un caso de prueba

!!! info
    Las pruebas deben colocarse en la carpeta `web-test`. Los archivos deben tener el sufijo `.test.js` para JavaScript o `.test.ts` para TypeScript.

    Esta es una ruta válida para un archivo de prueba:

    `modules/com.etendoerp.mymodule/web-test/mycomponent.test.js`

Incluya mediante `require` el elemento bajo prueba y comience a crear casos de prueba. Consulte la [documentación de Jest](https://jestjs.io/docs/getting-started){target="_blank"} como referencia.

### Archivo de prueba de ejemplo

El siguiente ejemplo está tomado de `org.openbravo.client.application`. Muestra los bloques fundamentales de un archivo de prueba Jest.

```javascript title="org.openbravo.client.application/web-test/ob-utilities-date.test.js"
require('../web/org.openbravo.client.application/js/utilities/ob-utilities-date');
 
describe('org.openbravo.client.application - OB.Utilities.Date', () => {
  beforeEach(() => {
    // Execute this before each test
  });
 
  afterEach(() => {
    // Execute this after each test
  });
 
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

Las funciones clave utilizadas en este archivo son:

- `describe(name, fn)` — agrupa pruebas relacionadas bajo una etiqueta común. Los bloques pueden anidarse para reflejar la jerarquía del elemento bajo prueba.
- `it(name, fn)` — define un caso de prueba individual. El nombre describe el comportamiento esperado.
- `expect(value)` — envuelve el valor real producido por el código bajo prueba.
- `toEqual(expected)` — verifica que el valor real coincide con el valor esperado mediante igualdad profunda.

## Configuración y desmontaje

Jest proporciona cuatro hooks de ciclo de vida que ejecutan código antes o después de las pruebas. Úselos para preparar el estado compartido y limpiarlo.

| Hook | Se ejecuta |
|------|------|
| `beforeEach` | Antes de cada prueba en el bloque `describe` actual |
| `afterEach` | Después de cada prueba en el bloque `describe` actual |
| `beforeAll` | Una vez antes de todas las pruebas en el bloque `describe` actual |
| `afterAll` | Una vez después de todas las pruebas en el bloque `describe` actual |

Use `beforeEach` y `afterEach` cuando cada prueba necesite una instancia nueva e independiente del elemento bajo prueba. Use `beforeAll` y `afterAll` cuando la configuración o el desmontaje sean costosos y puedan compartirse de forma segura entre todas las pruebas; por ejemplo, al abrir y cerrar una conexión a base de datos.

El siguiente ejemplo está adaptado de `NpmDependenciesValidator.test.js`. Usa `beforeEach` para crear una instancia nueva del validador e inyectar dependencias simuladas antes de cada prueba.

```javascript title="NpmDependenciesValidator.test.js"
const { NpmDependenciesValidator } = require('./NpmDependenciesValidator');

describe('NpmDependenciesValidator', () => {
  let validator;

  beforeEach(() => {
    validator = new NpmDependenciesValidator();
    validator.getModules = jest.fn(() => ['module1', 'module2']);
    validator.getPackageJsonPath = jest.fn(module => `${module}/package.json`);
  });

  it('does not return warnings or errors if dependency is not shared between modules', async () => {
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

Aquí `openDatabaseConnection` se ejecuta una sola vez para toda la suite en lugar de antes de cada prueba individual, lo que reduce el tiempo de ejecución cuando la operación es costosa.

## Mocking

El mocking reemplaza implementaciones reales con sustitutos controlados para que las pruebas sigan siendo rápidas y aisladas. Jest proporciona tres herramientas principales de mocking.

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

`jest.clearAllMocks()` en `beforeEach` restablece los contadores de llamadas y los valores de retorno entre pruebas para que una prueba no afecte las aserciones de otra.

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

const validator = new NpmDependenciesValidator();
const spy = jest.spyOn(validator, 'validate');

validator.validate();

expect(spy).toHaveBeenCalledTimes(1);

spy.mockRestore(); // restores the original method
```

Llame a `spy.mockRestore()` en `afterEach` para evitar que el spy persista entre pruebas.

## Pruebas parametrizadas

`it.each` ejecuta la misma lógica de prueba con múltiples pares de entrada/salida. Esto elimina código de prueba duplicado y hace que la intención quede explícita en el nombre de la prueba.

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

La sintaxis de plantilla literal define una tabla. La primera fila es el encabezado de columna. Cada fila siguiente es una ejecución de prueba. Jest interpola `$number` y `$expected` en el nombre de la prueba para que cada caso sea distinguible en la salida.

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

## Pruebas asíncronas

Jest maneja `async`/`await` de forma nativa. Marque el callback de la prueba como `async` y use `await` en las promesas. Jest espera a que la promesa devuelta se resuelva antes de evaluar las aserciones.

El siguiente ejemplo está adaptado de `User.test.ts`. Verifica que una llamada de inicio de sesión rellena el store con los datos del usuario y un token.

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
    const mockUser = 'testUser';
    const mockPass = 'testPass';

    await userStore.login(mockUser, mockPass);

    expect(OBRest.loginWithUserAndPassword).toHaveBeenCalledWith(mockUser, mockPass);
    expect(userStore.token).toBe('testToken');
    expect(userStore.user).toBe(mockUser);
  });
});
```

!!! warning
    Siempre use `await` en la llamada bajo prueba antes de realizar las aserciones. Sin `await`, las aserciones se ejecutan antes de que la promesa se resuelva y la prueba pasa independientemente del resultado real.

Si la prueba espera que una promesa sea rechazada, use `expect(...).rejects.toThrow()`:

En el siguiente ejemplo, `userStore` es la misma instancia configurada en `beforeEach`.

```javascript
it('throws on invalid credentials', async () => {
  await expect(userStore.login('', '')).rejects.toThrow('Invalid credentials');
});
```

## Ejecutar pruebas y cobertura

Para ejecutar todas las pruebas unitarias en una instancia de Etendo (tanto Core como todos los módulos instalados), ejecute:

```bash
npm test
```

Limite las pruebas a un módulo concreto añadiendo la ruta al final del comando:

```bash
npm test modules/com.etendoerp.mymodule/
```

Para ejecutar las pruebas y generar un informe de cobertura, ejecute:

```bash
npm run coverage
```

---
Este trabajo es una obra derivada de [How to Create Jest testcases](https://wiki.openbravo.com/wiki/How_to_create_Jest_testcases){target="\_blank"} de [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, utilizada bajo [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. Esta obra está licenciada bajo [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} por [Etendo](https://etendo.software){target="\_blank"}.
