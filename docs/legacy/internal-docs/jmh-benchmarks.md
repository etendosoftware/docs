---
title: JMH Benchmarks
---
## JMH Benchmarks
Running benchmarks using JMH in Etendo.

### How to run a benchmark

Use `./gradlew djmh` and specify the benchmark to run with `-Pbenchmark`
For Example:
```
./gradlew djmh -Pbenchmark="com.etendrerp.sequences.transactional.TransactionalSequenceClassicVSNew"
```

### How to create a Benchmark

Read the JMH [documentation](https://github.com/openjdk/jmh) and [samples](https://github.com/openjdk/jmh/tree/master/jmh-samples/src/main/java/org/openjdk/jmh/samples).
The sample code in the JMH Repo contains useful example code with explanations. You may also refer to already created benchmarks inside the Etendo Core repo.

Begin by creating a class that extends either the `BaseBenchmark` or the `WeldBenchmark` depending on your needs.

After creating the benchmark methods, run the benchmark with the command explained above. 

### How to debug a benchmark

Please note that the benchmark results observed after debugging will ***not*** be representative of the actual performance. 
Debug should only be used when something is not working properly, and once fixed, the benchmark should be run in a normal way.

Use the following command to debug a benchmark
```
./gradlew -Dorg.gradle.debug=true djmh -PbenchmarkName="com.etendrerp.sequences.transactional.TransactionalSequenceClassicVSNew" --debug-jvm
```

From your IDE, create a standard debug configuration. Then attach to the JVM when the gradle shows the message `Listening in port 5005`.

#### Notes
If the gradle daemon is stuck in "Starting daemon", attach to it using your IDE (with the debug config created) and keep attached to it until it shows the message `Listening in port 5005`. Then disconnect an reconnect.

Since JMH runs various forks depending on configuration, you may see the message `Listening in port 5005` several times. You need to disconnect & recconect every time to let the execution continue. Dependending on the JMH configuration and the amount of benchmarks, you may need to do this several times.

### Caveats

The jmh task (`./gradlew jmh`) that runs all benchmarks from a jar, while it is the recommended way by JMH to run the benchmarks, does not work for now as some required resource files are not being packed in the JAR that JMH generates.

This may work once the core is packaged as single JAR file, but even then the recommended setup is to create a separate repo for the benchmarks, with a dependency to the core.
