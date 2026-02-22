---
title: https://developer.android.com/topic/libraries/support-library/setup
url: https://developer.android.com/topic/libraries/support-library/setup
source: md.txt
---

**Note:** With the release of Android 9.0 (API level 28) there is
a new version of the support library called
[AndroidX](https://developer.android.com/jetpack/androidx) which is part of [Jetpack](https://developer.android.com/jetpack).
The AndroidX library
contains the existing support library and also includes the latest Jetpack components.

<br />


You can continue to use the support library.
Historical artifacts (those versioned 27 and earlier, and packaged as `android.support.*`) will
remain available on Google Maven. However, all new library development
will occur in the [AndroidX](https://developer.android.com/jetpack/androidx) library.

<br />


We recommend using the AndroidX libraries in all new projects. You should also consider
[migrating](https://developer.android.com/jetpack/androidx/migrate) existing projects to AndroidX as well.

How you setup the Android Support Libraries in your development project depends on what features
you want to use and what range of Android platform versions you want to support with your
application.

This document guides you through downloading the Support Library package and adding libraries
to your development environment.

The support libraries are now available through Google's Maven
repository. We no longer support downloading the libraries through the SDK
Manager, and that functionality will be removed soon..

## Choosing Support Libraries

Before adding a Support Library to your application, decide what features you want to include
and the lowest Android versions you want to support. For more information on the features
provided by the different libraries, see
[Support Library Features](https://developer.android.com/tools/support-library/features).

## Adding Support Libraries

In order to use a Support Library, you must modify your application's project's
classpath dependencies within your development environment. You must perform this procedure for
each Support Library you want to use.

To add a Support Library to your application project:

1. Include Google's Maven repository in your project's `settings.gradle` file.  

   ```groovy
   dependencyResolutionManagement {
       repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
       repositories {
           google()

           // If you're using a version of Gradle lower than 4.1, you must
           // instead use:
           //
           // maven {
           //     url 'https://maven.google.com'
           // }
       }
   }
   ```
2. For each module in which you want to use a Support Library, add the library in the `dependencies` block of the module's `build.gradle` file. For example, to add the v4 core-utils library, add the following:  

   ```groovy
   dependencies {
       ...
       implementation "com.android.support:support-core-utils:28.0.0"
   }
   ```


**Caution:** Using dynamic dependencies (for example,
`palette-v7:23.0.+`) can cause unexpected version updates and
regression incompatibilities. We recommend that you explicitly specify a
library version (for example, `palette-v7:28.0.0`).

## Using Support Library APIs

Support Library classes that provide support for existing framework APIs typically have the
same name as framework class but are located in the `android.support` class packages,
or have a `*Compat` suffix.  
**Caution:** When using classes from the Support Library, be certain you import
the class from the appropriate package. For example, when applying the `ActionBar`
class:

- `android.support.v7.app.ActionBar` when using the Support Library.
- `android.app.ActionBar` when developing only for API level 11 or higher.


**Note:** After including the Support Library in your application project, we
strongly recommend that you [shrink, obfuscate, and optimize
your app](https://developer.android.com/studio/build/shrink-code) for release. In addition to protecting your source code with obfuscation, shrinking
removes unused classes from any libraries you include in your application, which keeps the
download size of your application as small as possible.

Further guidance for using some Support Library features is provided in the Android developer
[training classes](https://developer.android.com/training),
[guides](https://developer.android.com/guide/components)
and samples. For more information about the individual Support Library classes and methods, see
the [android.support](https://developer.android.com/reference/android/support/v4/app/package-summary) packages in the API reference.

### Manifest Declaration Changes

If you are increasing the backward compatibility of your existing application to an earlier
version of the Android API with the Support Library, make sure to update your application's
manifest. Specifically, you should update the `android:minSdkVersion`
element of the [`<uses-sdk>`](https://developer.android.com/guide/topics/manifest/uses-sdk-element) tag in the manifest to the new, lower version number, as
shown below:  

```xml
  <uses-sdk
      android:minSdkVersion="14"
      android:targetSdkVersion="23" />
```

The manifest setting tells Google Play that your application can be installed on devices with Android
4.0 (API level 14) and higher.

If you are using Gradle build files, the `minSdkVersion` setting in the build file
overrides the manifest settings.  

```groovy
plugins {
  id 'com.android.application'
}

android {
    ...

    defaultConfig {
        minSdkVersion 16
        ...
    }
    ...
}
```

In this case, the build file setting tells Google Play that the default build variant of your
application can be installed on devices with Android 4.1 (API level 16) and higher. For more
information about build variants, see
[Build System Overview](https://developer.android.com/studio/build).


**Note:** If you are including several support libraries, the
minimum SDK version must be the *highest* version required by any of
the specified libraries. For example, if your app includes both the [v14 Preference Support library](https://developer.android.com/topic/libraries/support-library/features#v14-preference) and the
[v17 Leanback library](https://developer.android.com/topic/libraries/support-library/features#v17-leanback), your minimum
SDK version must be 17 or higher.