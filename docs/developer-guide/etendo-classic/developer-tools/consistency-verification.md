---
title: Consistency verification
---
## Modules consistency

### Resolution of conflicts
Etendo make uses of the [conflict resolution strategy](https://docs.gradle.org/current/userguide/dependency_resolution.html) offered by GRADLE.

This approach is used to identify conflict between Etendo artifacts published to Nexus.



For example, when you make use of a Etendo module, which depends on the Etendo core.

```groovy
group          = 'com.etendo'
ext.artifact   = "moduleCextract"
version        = '1.0.1'
dependencies {
    // Etendo CORE dependency
    implementation 'com.etendoerp.platform:etendo-core:[22.1.1, 22.1.2]'
}
```

and you are currently working with the Etendo core in `22.1.0`, then a conflict resolution is found.

Depending on the type of conflict, if the problem is with the Etendo Core, then a Exception will be throw.

You can force the resolution using the extension flag

``` groovy
etendo {
	forceResolution = true
}
```

If you want to skip the resolution you can add to the plugin extension the flag
``` groovy
etendo {
	performResolutionConflicts = false
}
```


### Version consistency
The version consistency approach verifies that a extracted Etendo JAR artifact is consistent with the installed one (**Equal** version).

When a new Etendo JAR dependency is added or the version is updated, a `update.database` is need it to run before executing any compilation task (smartbuild, compile.complete, etc).
You can force the compilation tasks adding to the Etendo plugin extension the ignore flag
``` groovy
etendo {
	ignoreConsistencyVerification = true 
}
```
Or run the tasks with the `-PignoreConsistency=true` flag.

By default Etendo not allow you to add a JAR dependency with an old version to the current installed one.
You can ignore this behavior adding the module name to be updated with an old version as a configuration
``` groovy
etendo {
	ignoredArtifacts = ['com.etendoerp.mymodulename']
}
```


