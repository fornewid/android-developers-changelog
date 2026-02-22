---
title: https://developer.android.com/build/publish-library/prep-lib-release
url: https://developer.android.com/build/publish-library/prep-lib-release
source: md.txt
---

This page describes the properties and options needed to prepare your
[Android library](https://developer.android.com/studio/projects/android-library) project for publication
using the [Android Gradle plugin (AGP)](https://developer.android.com/studio/releases/gradle-plugin).
Even if you set some of these properties at the outset of creating your
library, review the following guidance to optimize your
settings.

## Choose a namespace

Android libraries need to declare a namespace so that they can generate a unique
`R` class when their resources are compiled. This namespace should closely match
the library's root class package to avoid confusion when users import regular
classes from the library and its `R` class.

Starting with AGP 7.0, you can set the
[namespace](https://developer.android.com/reference/tools/gradle-api/7.0/com/android/build/api/dsl/CommonExtension#namespace:kotlin.String)
in the app's `build.gradle` file, as shown in the following code example:  

### Groovy

```groovy
android {
  namespace = 'com.example.library'
}
```

### Kotlin

```kotlin
android {
  namespace = "com.example.library"
}
```

The namespace is a developer-facing property of the library. It is not
related to the application identity, which is set using the
[`applicationId`](https://developer.android.com/studio/build/configure-app-module#set_the_application_id)
property.

In previous versions of AGP, both the `applicationId` property (for an
app) and the `namespace` property (for a library) could be set using the
manifest's [`package`](https://developer.android.com/guide/topics/manifest/manifest-element#package)
attribute, which led to confusion.
| **Note:** A library project does not have an `applicationId`; that is a property of applications only.

## Choose a `minSdkVersion` value

Choosing a [`minSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#min) for
your library is an important aspect of publishing your library. The
`minSdkVersion` should reflect the minimum version of Android that your code can
support.

Be aware of the following considerations when choosing a `minSdkVersion`:

- **Choosing a low `minSdkVersion` generally allows for wider distribution of
  your library.**

  A library's code is generally not executed unless the app
  calls it explicitly. An app can still run on a version of Android that
  is lower than required by a library dependency---if the library is not
  essential to core app functionality---by doing runtime checks before calling
  the library. Therefore, set your library's `minSdkVersion` low enough that
  it can be embedded in apps, and called when possible, to help reach more
  users.
- **Choosing a high `minSdkVersion` might prevent applications from including
  the library.**

  The manifest merger, which is a step in AGP that merges manifest files
  from the app and from its dependencies, enforces that no
  dependencies have a higher `minSdkVersion` than the app.
- **Choosing a high `minSdkVersion` might prompt app developers to disable
  manifest merger safety checks, causing issues later in the build process.**

  Because the manifest merger prevents app projects from including
  libraries with a higher `minSdkVersion` than the app itself, app developers
  might disable the safety checks of the manifest merger to minimize build
  errors. However, this risks true incompatibility issues downstream.
- **Choosing a high `minSdkVersion` might be necessary in special cases where
  a library's manifest includes a broadcast receiver or some other mechanism by
  which its code is triggered automatically.**

  In these cases, choosing a high `minSdkVersion` ensures that code can run.
  Alternatively, you can disable the automated behavior so that the app can opt
  in to executing the library after doing the right checks.

To allow embedding in apps, use the
[`RequiresApi`](https://developer.android.com/reference/androidx/annotation/RequiresApi) annotation in your
library to indicate to its callers that they need to do runtime checks. Android
Lint uses the `RequiresApi` information for its inspections. For more resources
on using annotations to improve your API code and APIs, see [Improve code
inspection with annotations](https://developer.android.com/studio/write/annotations).

## Set up AAR metadata

An Android library is packaged in the form
of an Android Archive (AAR) file. AAR metadata consists of properties that help
AGP consume libraries. If your library is consumed by an incompatible
configuration, and AAR metadata is set up, users are presented with an error
message to help them resolve the issue.
| **Note:** AAR metadata does not contain properties that are important at runtime and therefore is not typically found in compiled Android apps.

### Choose a minCompileSdk value

Starting with version 4.1, AGP supports
[`minCompileSdk`](https://developer.android.com/reference/tools/gradle-api/7.1/com/android/build/api/variant/AarMetadata#mincompilesdk).
This indicates the minimum
[`compileSdk`](https://developer.android.com/reference/tools/gradle-api/7.1/com/android/build/api/dsl/CommonExtension#compileSdk:kotlin.Int)
that consuming projects can use. If your library contains manifest entries or
resources that make use of newer platform attributes, you need to
set this value.

The `minCompileSdk` value can be set in the `defaultConfig{}`,
`productFlavors{}`, and `buildTypes{}` blocks in the module-level `build.gradle`
file:  

### Groovy

```groovy
android {
  defaultConfig {
    aarMetadata {
      minCompileSdk = 29
    }
  }
  productFlavors {
    foo {
      ...
      aarMetadata {
        minCompileSdk = 30
      }
    }
  }
}
```

### Kotlin

```kotlin
android {
  defaultConfig {
    aarMetadata {
      minCompileSdk = 29
    }
  }
  productFlavors {
    register("foo") {
      ...
      aarMetadata {
        minCompileSdk = 30
      }
    }
  }
}
```

If you set `minCompileSdk` in multiple places, Gradle prioritizes the settings
locations as follows during the build process:

1. `buildTypes{}`

2. `productFlavors{}`

3. `defaultConfig{}`

In the preceding example, where `minCompileSdk` is defined in both
`defaultConfig{}` and `productFlavors{}`, `productFlavors{}` is prioritized
and `minCompileSdk` is set to 30.

To learn more about how Gradle
prioritizes settings when combining code and resources, see [Build with source
sets](https://developer.android.com/studio/build/build-variants#sourceset-build).

## Enable test fixtures

[Test fixtures](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestFixtures)
are commonly used to set up the code being tested or facilitate the tests of a
component. Starting with version 7.1, AGP can create test fixtures for library
projects in addition to application and dynamic-feature projects.

When publishing a library for others to consume, consider creating test
fixtures for your API. Test fixtures can be turned on in the module-level
`build.gradle` file:  

### Groovy

```groovy
android {
  testFixtures {
    enable = true
  }
}
```

### Kotlin

```kotlin
android {
  testFixtures {
    enable = true
  }
}
```

When you turn on test fixtures, Gradle automatically creates a
`src/testFixtures` source set where you can write test fixtures.

For more information, refer to Gradle's documentation about [using
test fixtures](https://docs.gradle.org/current/userguide/java_testing.html#sec:java_test_fixtures).