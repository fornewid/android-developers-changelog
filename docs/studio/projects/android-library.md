---
title: https://developer.android.com/studio/projects/android-library
url: https://developer.android.com/studio/projects/android-library
source: md.txt
---

An Android library is structurally the same as an Android app module.
It includes everything needed to build an app, including source code,
resource files, and an Android manifest.

However, instead of compiling into an APK that runs on a device,
an Android library compiles into an Android Archive (AAR) file that you can
use as a dependency for an Android app module. Unlike JAR files,
AAR files offer the following functionality for Android apps:

- AAR files can contain Android resources and a manifest file, which lets you bundle in shared resources like layouts and drawables in addition to Kotlin or Java classes and methods.
- AAR files can contain [C/C++
  libraries](https://developer.android.com/studio/build/dependencies#using-native-dependencies) for use by the app module's C/C++ code.

A library module is useful in the following situations:

- When building multiple apps that use some of the same components, such as activities, services, or UI layouts
- When building an app that exists in multiple APK variations, such as a free and paid version, that share core components

In either case, move the files you want to reuse into a library module and
then add the library as a dependency for each app module.

This page explains how to create and use an Android library
module. For guidance on how to publish a library, see
[Publish your library](https://developer.android.com/build/publish-library)

## Create a library module

To create a new library module in your project, proceed as follows:

1. Click **File \> New \> New Module**.
2. In the **Create New Module** dialog that appears, click **Android Library** , then click **Next** .

   There's also an option to create a Kotlin or Java library,
   which builds a traditional JAR file. While a JAR file is useful for many
   projects---especially when you want to share code with other
   platforms---it doesn't let you include Android resources or manifest
   files, which is very useful for code reuse in Android projects. This guide
   focuses on creating Android libraries.
3. Give your library a name and select a minimum SDK version for the code in the library, then click **Finish** . **Important:** Module package names must be globally unique. You can't have two modules with the same package name in the same project.

Once the Gradle project sync completes, the library module appears in
the **Project** pane. If you don't see the new module
folder, make sure the pane is displaying the [**Android** view](https://developer.android.com/studio/projects#ProjectFiles).

### Convert an app module to a library module

If you have an existing app module with code you want to reuse,
you can turn it into a library module as follows:

1. Open the module-level `build.gradle` file, if you're using Groovy, or the `build.gradle.kts` file, if you're using Kotlin script.
2. Delete the line for the `applicationId`. Only an Android app module can define this.
3. Find the \`plugins\` block at the top of the file that looks like this:  

   ### Groovy

   ```groovy
     plugins {
         id 'com.android.application'
     }
     
   ```

   ### Kotlin

   ```kotlin
     plugins {
         id("com.android.application")
     }
     
   ```

   Change it to the following:  

   ### Groovy

   ```groovy
     plugins {
         id 'com.android.library'
     }
     
   ```

   ### Kotlin

   ```kotlin
     plugins {
         id("com.android.library")
     }
     
   ```
4. Save the file and click **File \> Sync Project with Gradle Files**.

The structure of the module remains the same, but it now
operates as an Android library. The build creates an AAR file
instead of an APK.

When you want to build the AAR file, select the library module in the
**Project** window and click
**Build \> Build APK**.

## Add dependencies with the Project Structure dialog

You can use the **Project Structure** dialog to add dependencies to your
project. The following sections describe how to use the dialog to add
dependencies.

### Use your library from within the same project

To use your new Android library's code in another app or library module within
the same project, add a project-level dependency:

1. Navigate to **File \> Project
   Structure \> Dependencies**.
2. Select the module that you want to add the library.
3. In the **Declared Dependencies** tab, click ![](https://developer.android.com/static/studio/images/buttons/ic_plus.png) and select **Module Dependency** from the menu.   

   ![](https://developer.android.com/static/studio/images/projects/psd-add-module-dependency-dropdown.png)
4. In the **Add Module Dependency** dialog, select your library module.

   ![Add module dependency in the Project Structure
   Dialog](https://developer.android.com/static/studio/images/projects/psd-add-module-dependency.png)
5. Select the configuration that requires this dependency or select
   **implementation** if it applies to all configurations, then click **OK**.

Android Studio edits your module's `build.gradle` or `build.gradle.kts` file to
add the dependency, in the following form:  

### Groovy

```groovy
  implementation project(path: ":example-library")
```

### Kotlin

```kotlin
  implementation(project(":example-library"))
```

### Use your library in other projects

The recommended way to share dependencies (JARs and AARs) is with a Maven
repository, either hosted on a service, such as
[Maven Central](https://maven.apache.org/repository/index.html), or
with a directory structure on your local disk. For more information on using
Maven repositories, see [Remote
repositories](https://developer.android.com/studio/build/dependencies#remote-repositories).

When an Android library is published to a Maven repository, metadata is
included so that the dependencies of the library are included in the
consuming build. This lets the library be automatically deduplicated if
it is used in multiple places.
| **Note:** If you can't publish your library to a Maven repository, you can consume the JAR or AAR file directly using the process described in the [Add your AAR or JAR as a dependency](https://developer.android.com/studio/projects/android-library#psd-add-aar-jar-dependency) section. In this case, you must manually manage any transitive dependencies of that AAR.

To use your Android library's code in another app module in a different project,
proceed as follows:

1. Navigate to **File \>
   Project Structure \>
   Dependencies**.
2. In the **Declared Dependencies** tab, click ![](https://developer.android.com/static/studio/images/buttons/ic_plus.png) and select **Library Dependency** in the menu.   

   ![](https://developer.android.com/static/studio/images/projects/psd-add-library-dependency-dropdown.png)
3. In the **Add Library Dependency** dialog, use the search box to find the
   library to add. This form searches the repositories specified in the
   in the `dependencyResolutionManagement { repositories {...}}` block in the
   `settings.gradle` or `settings.gradle.kts` file.

   ![Add library dependency in the Project Structure
   Dialog](https://developer.android.com/static/studio/images/projects/psd-add-library-dependency.png)
4. Select the configuration that requires this dependency or select
   **implementation** if it applies to all configurations, then click **OK**.

Check your app's `build.gradle` or `build.gradle.kts` file to confirm that a
declaration similar to the following appears (depending on the build configuration
you've selected):  

### Groovy

```groovy
  implementation 'com.example:examplelibrary:1.0.0'
```

### Kotlin

```kotlin
  implementation("com.example:examplelibrary:1.0.0")
```

### Add your AAR or JAR as a dependency

To use your Android library's code in another app module, proceed as follows:

1. Navigate to **File \>
   Project Structure \>
   Dependencies**.
2. In the **Declared Dependencies** tab, click ![](https://developer.android.com/static/studio/images/buttons/ic_plus.png) and select **Jar
   Dependency** in the menu.   

   ![](https://developer.android.com/static/studio/images/projects/psd-add-jar-dependency-dropdown.png)
3. In the **Add Jar/Aar Dependency** dialog, enter the path to your AAR
   or JAR file, then select the configuration to which the dependency
   applies. If the library should be available to all configurations, select the
   **implementation** configuration.

   ![Add AAR dependency in the Project Structure
   Dialog](https://developer.android.com/static/studio/images/projects/psd-add-aar-dependency.png)

   Check your app's `build.gradle` or `build.gradle.kts` file to confirm that a
   declaration similar to the following appears (depending on the build configuration
   you've selected):  

   ### Groovy

   ```groovy
     implementation files('my_path/my_lib.aar')
   ```

   ### Kotlin

   ```kotlin
     implementation(files("my_path/my_lib.aar"))
   ```

To import a dependency on the Gradle build running outside of Android Studio,
add a path to the dependency in
your app's `build.gradle` or `build.gradle.kts` file. For example:  

### Groovy

```groovy
dependencies {
    implementation fileTree(dir: "libs", include: ["*.jar", "*.aar"])
}
```

### Kotlin

```kotlin
dependencies {
    implementation(fileTree(mapOf("dir" to "libs", "include" to listOf("*.jar", "*.aar"))))
}
```

For more about adding Gradle dependencies, see
[Add build dependencies](https://developer.android.com/studio/build/dependencies).
| **Note:** In the previous examples, the `implementation` configuration adds the library as a build dependency for the entire app module. To learn how to configure dependencies only for specific build variants, see [Configure build variants](https://developer.android.com/studio/build/build-variants).

## Declare a public resource

Resources include all files in your project's `res/` directory,
such as images. All resources in a library default to public. To make all
resources implicitly private, you must define at least one specific attribute
as public.

To declare a public resource, add a `<public>` declaration
to your library's `public.xml` file. If you haven't added public
resources before, you need to create the `public.xml` file in the
`res/values/` directory of your library.

The following example code creates two public string resources with the
names `mylib_app_name` and `mylib_public_string`:  

```xml
<resources>
    <public name="mylib_app_name" type="string"/>
    <public name="mylib_public_string" type="string"/>
</resources>
```

To prevent users of your library from accessing resources intended
only for internal use, use this automatic private designation
mechanism by declaring one or more public resources. Alternately, you can make
all resources private by adding an empty `<public />` tag. This
marks nothing as public and makes all resources private.

Any resources that you want to remain visible to
developers using your library should be made public.

Implicitly making attributes private prevents users of your library
from receiving code completion suggestions from internal library resources
and lets users rename or remove private resources without breaking
clients of your library. Private resources are filtered out of code completion,
and the [lint tool](https://developer.android.com/studio/write/lint) warns you when you try
to reference a private resource.


When building a library, the Android Gradle plugin gets the public resource
definitions and extracts them into the `public.txt` file, which is
then packaged inside the AAR file.

## Development considerations for library modules

As you develop your library modules and dependent apps, be aware of the
following behaviors and limitations.

- **Libraries are merged in priority order.**

  Once you have added references to library modules to your Android app module,
  you can set their relative priority. At build time, the
  libraries are merged with the app one at a time, starting from the lowest
  priority to the highest.

  Resource references in a library will refer to the merged resource,
  not necessarily the library resource. A library module can't enforce the usage
  of its own resources over those of the app or other libraries when there are
  resources with the same name.
- **Avoid resource merge conflicts.**

  The build tools merge resources from a library module with those of a
  dependent app module. If a given resource name is defined in both modules, the
  resource from the app is used.

  If conflicts occur between multiple AAR libraries, then the resource from the
  library listed first in the dependencies list (closest to the top of the
  `dependencies` block) is used.

  To avoid resource conflicts, consider using a
  prefix or other consistent naming scheme that is unique to the module (or is
  unique across all project modules).
- **In multi-module builds, JAR dependencies are treated as
  transitive dependencies.**

  When you add a JAR dependency to a library project that outputs an AAR,
  the JAR is processed by the library module and packaged with its AAR.

  However, if your project includes a library module that is consumed by an app
  module, the app module treats the library's local JAR dependency as a
  transitive dependency. In this case, the local JAR is processed by the app
  module that consumes it, and not by the library module. This speeds up
  incremental builds that are caused by changes to a library's code.

  Any Java resource conflicts caused by local JAR dependencies must be resolved
  in the app module that consumes the library.
- **A library module can depend on an external JAR library.**

  You can develop a library module that depends on an external library.
  In this case, the dependent module must build
  against a target that includes the external library.

  Note that both the library module and the dependent app must
  declare the external library in their manifest files in a [`<uses-library>`](https://developer.android.com/guide/topics/manifest/uses-library-element) element.
- **The app module's `minSdkVersion` must be equal to or
  greater than the version defined by the library.**

  A library is compiled as part of the dependent app module, so the APIs used
  in the library module must be compatible with the platform version that the app
  module supports.
- **Each library module creates its own `R` class.**

  When you build the dependent app modules, library modules are compiled into
  an AAR file then added to the app module. Therefore, each library has its own
  `R` class, named according to the library's package name.

  The `R` class generated from main module and the library module is
  created in all the packages that are needed, including the main module's package
  and the libraries' packages.
- **A library module might include its own ProGuard configuration
  file.**

  If you have a library project that you use to build and publish an AAR, you
  can add a ProGuard configuration file to your library's build configuration. If you
  do, the Android Gradle plugin applies the ProGuard rules that you have specified.
  The build tools embed this file within the generated AAR file for the library
  module. When you add the library to an app module, the library's ProGuard file
  is appended to the ProGuard configuration file (`proguard.txt`) of
  the app module.

  By embedding a ProGuard file in your library module, you help ensure that
  app modules that depend on your library don't have to manually update their
  ProGuard files to use your library. When the Android Studio build system builds
  your app, it uses the directives from both the app module and the library. So
  there's no need to run a code shrinker on the library in a separate step.

  To add the ProGuard rules to your library project, specify the
  file's name with the `consumerProguardFiles` property inside the
  `defaultConfig` block of your library's `build.gradle` or
  `build.gradle.kts` file.

  For example, the following snippet sets
  `lib-proguard-rules.txt` as the library's ProGuard configuration
  file:  

  ### Groovy

  ```groovy
  android {
      defaultConfig {
          consumerProguardFiles 'lib-proguard-rules.txt'
      }
      ...
  }
  ```

  ### Kotlin

  ```kotlin
  android {
      defaultConfig {
          consumerProguardFiles("lib-proguard-rules.txt")
      }
      ...
  }
  ```

  However, if your library module is a part of a multi-module build that
  compiles into an APK and doesn't generate an AAR, run code
  shrinking on only the app module that consumes the library. To learn more
  about ProGuard rules and their usage, read
  [Shrink, obfuscate, and optimize your
  app](https://developer.android.com/studio/build/shrink-code).
-
  **Testing a library module is nearly the same as
  [testing an app.](https://developer.android.com/studio/test)**


  The main difference is that the library and its dependencies are
  automatically included as dependencies of the test APK. This means that
  the test APK includes not only its own code but also the library's AAR
  and all its dependencies. Because there is no separate app under test,
  the `androidTest` task installs (and uninstalls) only the test
  APK.


  When [merging
  multiple manifest files](https://developer.android.com/studio/build/manage-manifests#merge-manifests), Gradle follows the default priority order and
  merges the library's manifest into the test APK's main manifest.

## Anatomy of an AAR file

The file extension for an AAR file is `.aar`, and the Maven artifact type is
`aar` as well. The file itself is a ZIP file. The only mandatory entry is
`/AndroidManifest.xml`.

An AAR file can also include one or more of the following optional
entries:

- `/classes.jar`
- `/res/`
- `/R.txt`
- `/public.txt`
- `/assets/`
- `/libs/`<var translate="no">name</var>`.jar`
- `/jni/`<var translate="no">abi_name</var>`/`<var translate="no">name</var>`.so` (where <var translate="no">abi_name</var> is one of the [Android-supported ABIs](https://developer.android.com/ndk/guides/abis#sa))
- `/proguard.txt`
- `/lint.jar`
- `/api.jar`
- `/prefab/` for [exporting native
  libraries](https://developer.android.com/studio/build/dependencies#native-dependencies-aars)