# Run RX Services

Before you begin, please ensure that you've completed the [Create new Spring Boot service](/docs/developer-guide/etendo-rx/tutorials/create-new-service.md)

To simplify RX executions you have a simplified run task:

```
./gradlew rx:rx
```

# Configure auth project

Check Auth log file in:

src-rx/logs/auth.log

You will find something like this:

---

Populate the auth.yaml file with the following property:
token: eyJhbGciOiJSUzI1NiJ9... (truncated)

---

Copy the value of token line and replace the token value in the file:

src-rx/rxconfig/auth.yaml

replace default empty token value with log content

```
 token: eyJhbGciOiJSUzI1NiJ9... (truncated)
```

# Run tutorial project:

```
./gradlew :com.tutorial.rxtutorial:bootRun
```

# Open in your browser

You can view the generated page:

[**http://localhost:8101/api/**](http://localhost:8101/api/)

Great job! You've successfully created a fully working rx service.
