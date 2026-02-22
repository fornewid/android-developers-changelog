---
title: https://developer.android.com/studio/write/java8-support
url: https://developer.android.com/studio/write/java8-support
source: md.txt
---

# Use Java 8 language features and APIs

The Android Gradle plugin 3.0.0 and later supports all Java 7 language features and a subset of Java 8 language features that vary by platform version. When building your app using the Android Gradle plugin 4.0.0 and higher, you can use some Java 8 language APIs without requiring a minimum API level for your app.

This page describes the Java 8 language features you can use, how to properly configure your project to use them, and any known issues you may encounter. See the following video for an overview of Java 8 language features.  
| **Note:** When developing apps for Android, using Java 8 language features is optional. You can keep your project's source and target compatibility values set to Java 7, but you still need to compile using JDK 8.

The Android Gradle plugin provides built-in support for using certain Java 8 language features and third-party libraries that use them. The default toolchain implements the new language features by performing bytecode transformations, called`desugar`, as part of the D8/R8 compilation of class files into DEX code, as shown in figure 1.
![Java 8 language feature support using `desugar` bytecode transformations](https://developer.android.com/static/studio/images/write/desugar_diagram.png)**Figure 1.** Java 8 language feature support using`desugar`bytecode transformations.**Note:** Your choice of bytecode level is a balance between functionality and build speed. Bytecode level 6 has a faster build and fewer features, whereas bytecode level 7 has a balance of features and build speed, and bytecode 8 is more feature rich with slower builds.

## Java 8 language feature support (Android Gradle Plugin 3.0.0+)

To start using supported Java 8 language features:

1. [Update the Android Gradle plugin](https://developer.android.com/studio/releases/gradle-plugin#updating-plugin)to 3.0.0 or higher.
2. For each module that uses Java 8 language features (either in its source code or through dependencies), update the module's`build.gradle`or`build.gradle.kts`file as shown below:

### Kotlin

```kotlin
android {
    ...
    // Configure only for each module that uses Java 8
    // language features (either in its source code or
    // through dependencies).
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_1_8
        targetCompatibility = JavaVersion.VERSION_1_8
    }
    // For Kotlin projects
    kotlinOptions {
        jvmTarget = "1.8"
    }
}
```

### Groovy

```groovy
android {
    ...
    // Configure only for each module that uses Java 8
    // language features (either in its source code or
    // through dependencies).
    compileOptions {
        sourceCompatibility JavaVersion.VERSION_1_8
        targetCompatibility JavaVersion.VERSION_1_8
    }
    // For Kotlin projects
    kotlinOptions {
        jvmTarget = "1.8"
    }
}
```

When building your app using the Android Gradle plugin 3.0.0 and higher, the plugin doesn't support all Java 8 language features. The following language features are available on any API level:

|                                            Java 8 language feature                                             |                                                                                                                                       Notes                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Lambda expressions](https://docs.oracle.com/javase/tutorial/java/javaOO/lambdaexpressions.html)               | Android doesn't support the serialization of lambda expressions.                                                                                                                                                                                                                   |
| [Method references](https://docs.oracle.com/javase/tutorial/java/javaOO/methodreferences.html)                 |                                                                                                                                                                                                                                                                                    |
| [Type annotations](https://docs.oracle.com/javase/tutorial/java/annotations/type_annotations.html)             | Type annotation information is only available at compile time, not at runtime. The platform supports[`TYPE`](https://developer.android.com/reference/java/lang/annotation/ElementType#TYPE)in API level 24 and below, but not`ElementType.TYPE_USE`or`ElementType.TYPE_PARAMETER`. |
| [Default and static interface methods](https://docs.oracle.com/javase/tutorial/java/IandI/defaultmethods.html) |                                                                                                                                                                                                                                                                                    |
| [Repeating annotations](https://docs.oracle.com/javase/tutorial/java/annotations/repeating.html)               |                                                                                                                                                                                                                                                                                    |

In addition to these Java 8 language features, Android Gradle plugin versions 3.0.0 and higher extend support for[`try`-with-resources](https://docs.oracle.com/javase/tutorial/essential/exceptions/tryResourceClose.html)to all Android API levels.

Desugar doesn't support[`MethodHandle.invoke`](https://docs.oracle.com/javase/8/docs/api/java/lang/invoke/MethodHandle.html#invoke-java.lang.Object...-)or[`MethodHandle.invokeExact`](https://docs.oracle.com/javase/8/docs/api/java/lang/invoke/MethodHandle.html#invokeExact-java.lang.Object...-). If your source code or one of your module dependencies uses one of these methods, you need to specify`minSdkVersion 26`or higher. Otherwise, you receive the following error:  

    Dex: Error converting bytecode to dex:
    Cause: signature-polymorphic method called without --min-sdk-version >= 26

In some cases, your module might not be using the`invoke`or`invokeExact`methods even when they're included in a library dependency. To keep using that library with`minSdkVersion 25`or lower,[enable code shrinking](https://developer.android.com/studio/build/shrink-code#shrink-code)to remove unused methods. If that doesn't work, consider using an alternative library that doesn't use the unsupported methods.

Java 8+ language features desugaring on the Android Gradle plugin 3.0.0 and higher and doesn't make any additional classes and APIs (such as`java.util.stream.*`) available for use on older Android releases. Support for partial Java API desugaring is available from the Android Gradle plugin 4.0.0 or higher, as described in the following section.

## Java 8+ API desugaring support (Android Gradle Plugin 4.0.0+)

If you're building your app using the Android Gradle plugin 4.0.0 or higher, the plugin extends support for using a number of Java 8 language APIs without requiring a minimum API level for your app. With Android Gradle plugin 7.4.0 or higher, a number of Java 11 language APIs are also available with desugared library 2.0.0 or higher.

This additional support for older platform versions is possible because plugin 4.0.0 and higher extends the desugaring engine to also desugar Java language APIs. You can include standard language APIs that were available only in recent Android releases (such as`java.util.streams`) in apps that support older versions of Android.

The following set of APIs are supported when building your app using Android Gradle plugin 4.0.0 or higher:

- Sequential streams (`java.util.stream`)
- A subset of`java.time`
- `java.util.function`
- Recent additions to`java.util.{Map,Collection,Comparator}`
- Optionals (`java.util.Optional`,`java.util.OptionalInt`, and`java.util.OptionalDouble`) and some new classes
- Some additions to`java.util.concurrent.atomic`(new methods on`AtomicInteger`,`AtomicLong`, and`AtomicReference`)
- `ConcurrentHashMap`(with bug fixes for Android 5.0)

With Android Gradle plugin 7.4.0 or higher, additional Java 11 APIs are supported such as a subset of the`java.nio.file`package.

For a complete list of supported APIs, visit[Java 8+ APIs available through desugaring](https://developer.android.com/studio/write/java8-support-table)and[Java 11+ APIs available through desugaring](https://developer.android.com/studio/write/java11-default-support-table).

To support these language APIs, the plugin compiles a separate DEX file that contains an implementation of the missing APIs and includes it in your app. The desugaring process rewrites your app's code to instead use this library at runtime. The source code compiled into the separate DEX file is available in the[desugar_jdk_libs](https://github.com/google/desugar_jdk_libs)GitHub repository.

To enable support for these language APIs on any version of the Android platform:

1. [Update the Android Gradle plugin](https://developer.android.com/studio/releases/gradle-plugin#updating-plugin)to 4.0.0 (or higher).
2. Include the following in your**app module** 's`build.gradle`or`build.gradle.kts`file:

### Kotlin

```kotlin
android {
    defaultConfig {
        // Required when setting minSdkVersion to 20 or lower
        multiDexEnabled = true
    }

    compileOptions {
        // Flag to enable support for the new language APIs

        // For AGP 4.1+
        isCoreLibraryDesugaringEnabled = true
        // For AGP 4.0
        // coreLibraryDesugaringEnabled = true

        // Sets Java compatibility to Java 8
        sourceCompatibility = JavaVersion.VERSION_1_8
        targetCompatibility = JavaVersion.VERSION_1_8
    }
}

dependencies {
    // For AGP 7.4+
    coreLibraryDesugaring("com.android.tools:desugar_jdk_libs:2.0.3")
    // For AGP 7.3
    // coreLibraryDesugaring("com.android.tools:desugar_jdk_libs:1.2.3")
    // For AGP 4.0 to 7.2
    // coreLibraryDesugaring("com.android.tools:desugar_jdk_libs:1.1.9")
}
```

### Groovy

```groovy
android {
    defaultConfig {
        // Required when setting minSdkVersion to 20 or lower
        multiDexEnabled true
    }

    compileOptions {
        // Flag to enable support for the new language APIs
        coreLibraryDesugaringEnabled true
        // Sets Java compatibility to Java 8
        sourceCompatibility JavaVersion.VERSION_1_8
        targetCompatibility JavaVersion.VERSION_1_8
    }
}

dependencies {
    // For AGP 7.4+
    coreLibraryDesugaring 'com.android.tools:desugar_jdk_libs:2.0.3'
    // For AGP 7.3
    // coreLibraryDesugaring 'com.android.tools:desugar_jdk_libs:1.2.3'
    // For AGP 4.0 to 7.2
    // coreLibraryDesugaring 'com.android.tools:desugar_jdk_libs:1.1.9'
}
```

Note that you may also need to include the previous code snippet in a library module's`build.gradle`or`build.gradle.kts`file if:

- The library module's instrumented tests use these language APIs (either directly or through the library module or its dependencies). This is so that the missing APIs are provided for your instrumented test APK.

- You want to run lint on the library module in isolation. This is to help lint recognize valid usages of the language APIs and avoid reporting false warnings.

Also note that API desugaring can be combined with shrinking, but only when using the R8 shrinker.

### Versions

The following table shows the versions of the Java 8+ API library and the minimum Android Gradle plugin version that supports each version:

| Version | Minimum Android Gradle plugin version |
|---------|---------------------------------------|
| 1.1.9   | 4.0.0                                 |
| 1.2.3   | 7.3.0                                 |
| 2.0.3   | 7.4.0-alpha10                         |

For details on the versions of the Java 8+ API library, see the[CHANGELOG.md file](https://github.com/google/desugar_jdk_libs/blob/master/CHANGELOG.md)in the`desugar_jdk_libs`GitHub repository.