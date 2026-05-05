---
title: How to Create Jest Test Cases
tags:
  - How to
  - Jest
  - Test
  - Test Cases
---

# How to Create Jest Test Cases
  
## Overview

[Jest](https://jestjs.io/){target="_blank"} is a testing framework currently used as the default in [create-react-app](https://github.com/facebook/create-react-app){target="_blank"}. It provides its own assertion and mocking methods and runs out-of-the-box with good integration with React, Babel, and TypeScript.

## Installation

From the directory of the module that contains the `package.json`, install all dependencies by running:

```bash
npm install
```

## Writing a Test

### File Placement

!!! info
    Tests should be placed in the `web-test` folder. Files must have the suffix `.test.js` for JavaScript or `.test.ts` for TypeScript.

    This is a valid path for a test file:

    `modules/com.etendoerp.mymodule/web-test/mycomponent.test.js`

See the [Jest documentation](https://jestjs.io/docs/getting-started){target="_blank"} for full reference.

### Core Functions

These are the key functions used to build a Jest test file:

- `describe(name, fn)` — groups related tests under a shared label. Blocks can be nested to reflect a hierarchy of the subject under test.
- `it(name, fn)` — defines a single test case. The name describes the expected behaviour.
- `expect(value)` — wraps the actual value produced by the code under test.
- `toBe(expected)` — asserts strict equality (`===`). Use for primitive values such as strings, numbers, and booleans.
- `toEqual(expected)` — asserts deep equality. Use for objects and arrays.

### Sample Test File

The following example is taken from `org.openbravo.client.application`. It demonstrates the core building blocks of a Jest test file.

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

## Setup and Teardown

Jest provides four lifecycle hooks that run code before or after tests. Use them to prepare shared state and clean it up.

| Hook | Runs |
|------|------|
| `beforeEach` | Before every test in the current `describe` block |
| `afterEach` | After every test in the current `describe` block |
| `beforeAll` | Once before all tests in the current `describe` block |
| `afterAll` | Once after all tests in the current `describe` block |

Use `beforeEach` and `afterEach` when each test needs a fresh, independent instance of the subject. Use `beforeAll` and `afterAll` when setup or teardown is expensive and can be shared safely across all tests — for example, opening and closing a database connection.

The following example is adapted from `NpmDependenciesValidator.test.js`. It uses `beforeEach` to create a fresh validator instance and inject mock dependencies before each test.

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

The following example shows the shape of a `beforeAll` / `afterAll` pair:

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

Here `openDatabaseConnection` runs once for the whole suite instead of before every single test, which reduces test execution time when the operation is costly.

## Mocking

Mocking replaces real implementations with controlled substitutes so tests remain fast and isolated. Jest provides three main mocking tools.

### jest.mock()

`jest.mock(modulePath, factory)` replaces an entire module. Jest intercepts the `require` or `import` call and returns the factory result instead of the real module.

The following example is adapted from `User.test.ts`. It replaces `@react-native-async-storage/async-storage` with an object of tracked functions.

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

`jest.clearAllMocks()` in `beforeEach` resets call counts and return values between tests so one test does not affect the assertions of another.

### jest.fn()

`jest.fn()` creates a standalone mock function. It records every call it receives and the arguments passed to it. Assign a return value with `.mockReturnValue(value)` or a one-time return value with `.mockReturnValueOnce(value)`.

```javascript
const fetchUser = jest.fn().mockReturnValue({ id: 1, name: 'Ana' });

fetchUser(1);

expect(fetchUser).toHaveBeenCalledWith(1);
expect(fetchUser).toHaveReturnedWith({ id: 1, name: 'Ana' });
```

### jest.spyOn()

`jest.spyOn(object, methodName)` wraps an existing method without replacing it. The original implementation still runs unless `.mockImplementation()` is chained. Use it when the real method behaviour is needed but call tracking is also required.

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

## Asynchronous Tests

Jest handles `async`/`await` natively. Mark the test callback as `async` and `await` any promises. Jest waits for the returned promise to settle before evaluating assertions.

The following example is adapted from `User.test.ts`. It verifies that a login call populates the store with user data and a token. The `etrest` mock simulates the server response — `getUserId` returns the user ID used internally by the store, while the token value is set by the store's own login logic after the mocked call resolves.

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
    Always `await` the call under test before asserting. Without `await`, the test finishes before the promise settles, which can produce false positives or flaky failures due to unhandled rejections.

If the test expects a promise to reject, use `expect(...).rejects.toThrow()`:

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

## Parameterized Tests

`it.each` runs the same test logic against multiple input/output pairs. This removes duplicated test code and makes the intention explicit in the test name.

The following example is taken from `ob-utilities-number.test.js`. It verifies that scientific notation strings are correctly converted to decimal notation.

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

The template literal syntax defines a table. The first row is the column header. Each subsequent row is one test run. Jest interpolates `$number` and `$expected` into the test name so each case is distinguishable in the output.

`it.each` also accepts an array of arrays when column headers are not required:

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

## Run Tests and Coverage

From the module directory, run all tests:

```bash
npm test
```

To run a single test file:

```bash
npm test -- web-test/mycomponent.test.js
```

To run tests and generate a coverage report, run:

```bash
npm run coverage
```

The coverage report is generated in the `coverage/` directory. Open `coverage/lcov-report/index.html` in a browser to view a detailed breakdown by file, including line, statement, branch, and function coverage.


This work is a derivative of [How to Create Jest testcases](https://wiki.openbravo.com/wiki/How_to_create_Jest_testcases){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
