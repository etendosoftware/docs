---
title: Etendo RX plugin
---
## Etendo RX plugin


#### Plugin flags

The plugin flags needs to be declared in the 'etendo plugin block'.

The etendorx plugin block can be specified in the build.gradle

``` groovy
etendorx {
	
}
```

##### Flags and variables

``` groovy
Action<? super AbstractBaseService> configServerAction = {}

Action<? super AbstractBaseService> authAction = {}

Action<? super AbstractBaseService> asyncProcessAction = {}

Action<? super AbstractBaseService> dasAction = {}

Action<? super AbstractBaseService> edgeAction = {}

Action<? super AbstractExecutableJar> codeGenAction = {}

List<String> excludedServices = new ArrayList<>()
```

The Actions allows you to configure the Etendo rx services

For example to configure the dependency version with custom environment variables of the code generation:
``` groovy
etendorx {
    codeGenAction({
        it.dependencyVersion = "1.0.0"
        it.environment([
                ENV_KEY : "ENV_VALUE"
        ])
    })
}
```
