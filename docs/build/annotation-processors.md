---
title: https://developer.android.com/build/annotation-processors
url: https://developer.android.com/build/annotation-processors
source: md.txt
---

This page includes detailed guidance on how to add and configure annotation
processors as project dependencies. To learn more about annotation processors,
see the entry in
[Configure dependencies](https://developer.android.com/build/dependencies#dependency_configurations).

If you add annotation processors to your compile classpath, you'll see
an error message similar to the following:

```
Error: Annotation processors must be explicitly declared now.
```

To resolve this error, add annotation processors to your project by configuring
your dependency using `annotationProcessor` as shown below:

### Kotlin

```kotlin
dependencies {
    // Adds libraries defining annotations to only the compile classpath.
    compileOnly("com.google.dagger:dagger:version-number")
    // Adds the annotation processor dependency to the annotation processor classpath.
    annotationProcessor("com.google.dagger:dagger-compiler:version-number")
}
```

### Groovy

```groovy
dependencies {
    // Adds libraries defining annotations to only the compile classpath.
    compileOnly 'com.google.dagger:dagger:version-number'
    // Adds the annotation processor dependency to the annotation processor classpath.
    annotationProcessor 'com.google.dagger:dagger-compiler:version-number'
}
```

**Note:** Android plugin for Gradle 3.0.0+ no longer
supports [`android-apt` plugin.](https://github.com/littlerobots/android-apt)

## Pass arguments to annotation processors

If you need to pass arguments to an annotation processor, you can do so using
the [`AnnotationProcessorOptions`](https://developer.android.com/reference/tools/gradle-api/current/com/android/build/api/dsl/AnnotationProcessorOptions)
block in your module's build configuration. For example, if you want to pass
primitive data types as key-value pairs, you can use the `argument` property,
as shown below:

### Kotlin

```kotlin
android {
    ...
    defaultConfig {
        ...
        javaCompileOptions {
            annotationProcessorOptions {
                arguments += mapOf("key1" to "value1",
                                   "key2" to "value2")
            }
        }
    }
}
```

### Groovy

```groovy
android {
    ...
    defaultConfig {
        ...
        javaCompileOptions {
            annotationProcessorOptions {
                argument 'key1', 'value1'
                argument 'key2', 'value2'
            }
        }
    }
}
```

However, when using Android Gradle plugin 3.2.0 and higher, you need to
pass processor arguments that represent files or directories using Gradle's
[`CommandLineArgumentProvider`](https://docs.gradle.org/current/javadoc/org/gradle/process/CommandLineArgumentProvider.html) interface.

Using `CommandLineArgumentProvider` allows you or the
annotation processor author to improve the correctness and performance of
incremental and cached clean builds by applying [incremental build property type
annotations](https://docs.gradle.org/current/userguide/more_about_tasks.html#sec:up_to_date_checks)
to each argument.

For example, the class below implements `CommandLineArgumentProvider` and
annotates each argument for the processor.

> [!NOTE]
> **Note:** Typically, annotation processor authors provide either this class or instructions on how to write such a class. That's because each argument needs to specify the correct build property type annotation in order to work as intended.

### Kotlin

```kotlin
class MyArgsProvider(
    // Annotates each directory as either an input or output for the
    // annotation processor.
    @get:InputFiles
    // Using this annotation helps Gradle determine which part of the file path
    // should be considered during up-to-date checks.
    @get:PathSensitive(PathSensitivity.RELATIVE)
    val inputDir: FileCollection,

    @get:OutputDirectory
    val outputDir: File
) : CommandLineArgumentProvider {
    // Specifies each directory as a command line argument for the processor.
    // The Android plugin uses this method to pass the arguments to the
    // annotation processor.

    override fun asArguments(): Iterable<String> {
        // Use the form '-Akey[=value]' to pass your options to the Java compiler.
        return listOf("-AinputDir=${inputDir.singleFile.absolutePath}",
                      "-AoutputDir=${outputDir.absolutePath}")
    }
}

android {...}
```

### Groovy

```groovy
class MyArgsProvider implements CommandLineArgumentProvider {

    // Annotates each directory as either an input or output for the
    // annotation processor.
    @InputFiles
    // Using this annotation helps Gradle determine which part of the file path
    // should be considered during up-to-date checks.
    @PathSensitive(PathSensitivity.RELATIVE)
    FileCollection inputDir

    @OutputDirectory
    File outputDir

    // The class constructor sets the paths for the input and output directories.
    MyArgsProvider(FileCollection input, File output) {
        inputDir = input
        outputDir = output
    }

    // Specifies each directory as a command line argument for the processor.
    // The Android plugin uses this method to pass the arguments to the
    // annotation processor.
    @Override
    Iterable<String> asArguments() {
        // Use the form '-Akey[=value]' to pass your options to the Java compiler.
        ["-AinputDir=${inputDir.singleFile.absolutePath}",
         "-AoutputDir=${outputDir.absolutePath}"]
    }
}

android {...}
```

After you define a class that implements `CommandLineArgumentProvider`, you need
to create an instance and pass it to the Android plugin using the
[`annotationProcessorOptions.compilerArgumentProvider`](https://developer.android.com/reference/tools/gradle-api/current/com/android/build/api/dsl/AnnotationProcessorOptions#compilerArgumentProvider(org.gradle.process.CommandLineArgumentProvider))
method, as shown below.

### Kotlin

```kotlin
// This is in your module's build.gradle file.
android {
    defaultConfig {
        javaCompileOptions {
            annotationProcessorOptions {
                // Creates a new MyArgsProvider object, specifies the input and
                // output paths for the constructor, and passes the object
                // to the Android plugin.
                compilerArgumentProvider(MyArgsProvider(files("input/path"),
                                                          file("output/path")))
            }
        }
    }
}
```

### Groovy

```groovy
// This is in your module's build.gradle file.
android {
    defaultConfig {
        javaCompileOptions {
            annotationProcessorOptions {
                // Creates a new MyArgsProvider object, specifies the input and
                // output paths for the constructor, and passes the object
                // to the Android plugin.
                compilerArgumentProvider new MyArgsProvider(files("input/path"),
                                         new File("output/path"))
            }
        }
    }
}
```

To learn more about how implementing `CommandLineArgumentProvider` helps
improve build performance, read
[Caching Java projects](https://docs.gradle.org/current/userguide/build_cache_use_cases.html).

## Disable the annotation processor error check

If you have dependencies on the compile classpath that include annotation
processors you don't need, you can disable the error check by adding
the following to your `build.gradle.kts` file. Keep in mind, the annotation
processors you add to the compile classpath are still not added to the
processor classpath.

### Kotlin

```kotlin
android {
    ...
    defaultConfig {
        ...
        javaCompileOptions {
            annotationProcessorOptions {
                argument("includeCompileClasspath", "false")
            }
        }
    }
}
```

### Groovy

```groovy
android {
    ...
    defaultConfig {
        ...
        javaCompileOptions {
            annotationProcessorOptions {
                includeCompileClasspath false
            }
        }
    }
}
```

If you use Kotlin and [kapt](https://kotlinlang.org/docs/kapt.html):

### Kotlin

```kotlin
android {
    ...
    defaultConfig {
        ...
        kapt {
            includeCompileClasspath = false
        }
    }
}
```

### Groovy

```groovy
android {
    ...
    defaultConfig {
        ...
        kapt {
            includeCompileClasspath false
        }
    }
}
```

If you experience issues after migrating your project's annotation processors to
the processor classpath, you can allow annotation processors on the compile
classpath by setting `includeCompileClasspath` to `true`. However, setting this
property to `true` is not recommended, and the option to do so will be removed
in a future update of the Android plugin.