---
title: https://developer.android.com/build/migrate-to-ksp
url: https://developer.android.com/build/migrate-to-ksp
source: md.txt
---

| **Note:** Kapt is now in maintenance mode, and we recommend that you migrate from kapt to KSP for all processors that support it. In most cases, this migration only requires changes to your project's build configuration.

[Kapt (the Kotlin Annotation Processing Tool)](https://kotlinlang.org/docs/kapt.html) lets you use
Java annotation processors with Kotlin code, even if those processors don't have
specific support for Kotlin. This is done by generating Java stubs from your
Kotlin files that the processors can then read. This stub generation is an
expensive operation and has a significant impact on build speed.

[KSP (Kotlin Symbol Processing)](https://github.com/google/ksp) is a Kotlin-first alternative to
kapt. KSP analyzes Kotlin code directly, which is [up to 2x
faster](https://android-developers.googleblog.com/2021/09/accelerated-kotlin-build-times-with.html). It also has a better understanding of Kotlin
language constructs.

You can run kapt and KSP alongside each other in your project while you're
migrating, and the migration can be done module by module, library by library.
| **Note:** If a module has any kapt processors remaining, stubs are still generated in that module. This means that the majority of performance improvement will occur only when all usages of kapt are removed from the module.

Here's an overview of the migration steps:

1. Check the libraries you use for KSP support
2. Add the KSP plugin to your project
3. Replace annotation processors with KSP
4. Remove the kapt plugin

## Check the libraries you use for KSP support

To get started, check if the libraries you're using with kapt already have KSP
support. This is the case for many popular libraries (including
[Dagger](https://github.com/google/dagger/issues/2349), [Glide](https://bumptech.github.io/glide/doc/download-setup.html#kotlin---ksp), [Room](https://developer.android.com/jetpack/androidx/releases/room#declaring_dependencies),
and [Moshi](https://github.com/square/moshi#codegen)), and others are adding support.

You can check the [list of supported libraries](https://kotlinlang.org/docs/ksp-overview.html#supported-libraries) in the
documentation, or refer to the documentation and issue tracker of the libraries
you're using.
| **Note:** While not a traditionally-included library dependency, [Data Binding](https://developer.android.com/topic/libraries/data-binding) also uses an annotation processor to provide its functionality, and [KSP support
| for Data Binding is not planned](https://issuetracker.google.com/issues/173030256#comment10). You can mitigate the impact of kapt on your build by isolating the usages of Data Binding to separate modules.

## Add the KSP plugin to your project

First, declare the KSP plugin in your top level `build.gradle.kts` file.
You can find a list of releases on the [KSP GitHub page](https://github.com/google/ksp/releases).  

### Kotlin

```kotlin
plugins {
    id("com.google.devtools.ksp") version "2.3.4" apply false
}
```

### Groovy

```groovy
plugins {
    id 'com.google.devtools.ksp' version '2.3.4' apply false
}
```

Then, enable KSP in your module-level `build.gradle.kts` file:  

### Kotlin

```kotlin
plugins {
    id("com.google.devtools.ksp")
}
```

### Groovy

```groovy
plugins {
    id 'com.google.devtools.ksp'
}
```

## Replace annotation processors with KSP

With KSP enabled, you can start replacing usages of kapt with KSP. For a vast
majority of libraries, this just requires changing kapt to ksp at the dependency
declaration, as they ship their annotation processor and KSP processor in the
same artifact.
**Note:** Some libraries (such as [Glide](https://bumptech.github.io/glide/doc/download-setup.html#kotlin---ksp)) might require you to change the dependency to a different artifact as well. Make sure to consult their documentation.  

### Kotlin

```kotlin
dependencies {
    kapt("androidx.room:room-compiler:2.5.0")
    ksp("androidx.room:room-compiler:2.5.0")
}
```

### Groovy

```groovy
dependencies {
    kapt 'androidx.room:room-compiler:2.5.0'
    ksp 'androidx.room:room-compiler:2.5.0'
}
```

After moving to KSP, sync and build your project to see if it still works
correctly.

Some common issues to look out for:

- Some libraries don't support the exact same set of features with kapt and KSP. If your code breaks after migrating, check the library's documentation.
- KSP has more accurate Kotlin type information than kapt (for example, about nullability), which means that KSP processors can be more precise about type requirements. This might require some fixes in your source code as well, in addition to updating your build files.
- If you were previously passing in arguments to the annotation processor, you'll likely need to pass in those arguments to KSP now. Note that the format of the arguments might differ between kapt and KSP. See the [KSP
  documentation](https://kotlinlang.org/docs/ksp-quickstart.html#pass-options-to-processors) and consult the documentation of the library you're using to learn more.

## Remove the kapt plugin

When you have no dependencies included with `kapt` in your module anymore,
remove the kapt plugin.
| **Note:** [Data Binding](https://developer.android.com/topic/libraries/data-binding) also requires kapt to be enabled in the module. In modules where Data Binding is used, kapt can't be removed.

If it was declared in a plugins block:  

### Kotlin

```kotlin
plugins {
    id("org.jetbrains.kotlin.kapt")
}
```

### Groovy

```groovy
plugins {
    id 'org.jetbrains.kotlin.kapt'
}
```

If it was using the apply plugin syntax using Groovy:  

```
apply plugin: 'kotlin-kapt'
```

You should also remove any leftover configuration related to kapt, such as:  

### Kotlin

```kotlin

kapt {
    correctErrorTypes = true
    useBuildCache = true
}
```

### Groovy

```groovy

kapt {
    correctErrorTypes true
    useBuildCache true
}
```

## Additional resources

- [KSP documentation on Kotlinlang.org](https://kotlinlang.org/docs/ksp-overview.html)
- [KSP on GitHub](https://github.com/google/ksp)
- [kapt on Kotlinlang.org](https://kotlinlang.org/docs/kapt.html)