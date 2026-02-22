---
title: https://developer.android.com/studio/projects/gradle-external-native-builds
url: https://developer.android.com/studio/projects/gradle-external-native-builds
source: md.txt
---

# Link Gradle to your native library

To include your native library project as a Gradle build dependency, you need to provide Gradle with the path to your CMake or ndk-build script file. When you build your app, Gradle runs CMake or ndk-build, and packages shared libraries with your app. Gradle also uses the build script to know which files to pull into your Android Studio project, so you can access them from the**Project** window. If you don't have a build script for your native sources, you need to[create a CMake build script](https://developer.android.com/studio/projects/configure-cmake)before you proceed.

Each module in your Android project can link to only one CMake or ndk-build script file. So, for example, if you want to build and package outputs from multiple CMake projects, you need to use one`CMakeLists.txt`file as your top-level CMake build script (which you then link Gradle to) and[add other CMake projects](https://developer.android.com/studio/projects/configure-cmake#include-other-cmake-projects)as dependencies of that build script. Similarly, if you're using ndk-build, you can[include other Makefiles](https://www.gnu.org/software/make/manual/html_node/Include.html)in your top-level[`Android.mk`](https://developer.android.com/ndk/guides/android_mk)script file.

Once you link Gradle to a native project, Android Studio updates the**Project** pane to show your source files and native libraries in the**cpp** group, and your external build scripts in the**External Build Files**group.

**Note:** When making changes to the Gradle configuration, make sure to apply your changes by clicking**Sync Project** ![](https://developer.android.com/static/studio/images/buttons/toolbar-sync-gradle.png)in the toolbar. Additionally, when making changes to your CMake or ndk-build script file after you have already linked it to Gradle, you should sync Android Studio with your changes by selecting**Build \> Refresh Linked C++ Projects**from the menu bar.

## Use the Android Studio UI

You can link Gradle to an external CMake or ndk-build project using the Android Studio UI:

1. Open the**Project** pane from the left side of the IDE and select the**Android**view.
2. Right-click on the module you would like to link to your native library, such as the**app** module, and select**Link C++ Project with Gradle**from the menu. You should see a dialog similar to the one shown in figure 4.
3. From the drop-down menu, select either**CMake** or**ndk-build** .
   1. If you select**CMake** , use the field next to**Project Path** to specify the`CMakeLists.txt`script file for your external CMake project.
   2. If you select**ndk-build** , use the field next to**Project Path** to specify the[`Android.mk`](https://developer.android.com/ndk/guides/android_mk)script file for your external ndk-build project. Android Studio also includes the[`Application.mk`](https://developer.android.com/ndk/guides/application_mk)file if it is located in the same directory as your`Android.mk`file.

   ![](https://developer.android.com/static/studio/images/projects/link-cpp-project_2-2_2x.png)

   **Figure 4.**Linking an external C++ project using the Android Studio dialog.
4. Click**OK**.

## Manually configure Gradle

To manually configure Gradle to link to your native library, you need to add the[`externalNativeBuild`](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.ExternalNativeBuild.html)block to your module-level`build.gradle`file and configure it with either the[`cmake`](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.CmakeOptions.html)or[`ndkBuild`](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.NdkBuildOptions.html)block:  

### Groovy

```groovy
android {
  ...
  defaultConfig {...}
  buildTypes {...}

  // Encapsulates your external native build configurations.
  externalNativeBuild {

    // Encapsulates your CMake build configurations.
    cmake {

      // Provides a relative path to your CMake build script.
      path "CMakeLists.txt"
    }
  }
}
```

### Kotlin

```kotlin
android {
  ...
  defaultConfig {...}
  buildTypes {...}

  // Encapsulates your external native build configurations.
  externalNativeBuild {

    // Encapsulates your CMake build configurations.
    cmake {

      // Provides a relative path to your CMake build script.
      path = file("CMakeLists.txt")
    }
  }
}
```

**Note:** If you want to link Gradle to an existing ndk-build project, use the[`ndkBuild`](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.NdkBuildOptions.html)block instead of the[`cmake`](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.CmakeOptions.html)block, and provide a relative path to your[`Android.mk`](https://developer.android.com/ndk/guides/android_mk)file. Gradle also includes the[`Application.mk`](https://developer.android.com/ndk/guides/application_mk)file if it is located in the same directory as your[`Android.mk`](https://developer.android.com/ndk/guides/android_mk)file.

### Specify optional configurations

You can specify optional arguments and flags for CMake or ndk-build by configuring another[`externalNativeBuild`](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.ExternalNativeBuildOptions.html)block within the`defaultConfig`block of your module-level`build.gradle`file. Similar to other properties in the`defaultConfig`block, you can override these properties for each product flavor in your build configuration.

For example, if your CMake or ndk-build project defines multiple native libraries and executables, you can use the[`targets`](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.ExternalNativeCmakeOptions.html#com.android.build.gradle.internal.dsl.ExternalNativeCmakeOptions:targets)property to build and package only a subset of those artifacts for a given product flavor. The following code sample describes some of the properties you can configure:  

### Groovy

```groovy
android {
  ...
  defaultConfig {
    ...
    // This block is different from the one you use to link Gradle
    // to your CMake or ndk-build script.
    externalNativeBuild {

      // For ndk-build, instead use the ndkBuild block.
      cmake {

        // Passes optional arguments to CMake.
        arguments "-DANDROID_ARM_NEON=TRUE", "-DANDROID_TOOLCHAIN=clang"

        // Sets a flag to enable format macro constants for the C compiler.
        cFlags "-D__STDC_FORMAT_MACROS"

        // Sets optional flags for the C++ compiler.
        cppFlags "-fexceptions", "-frtti"
      }
    }
  }

  buildTypes {...}

  productFlavors {
    ...
    demo {
      ...
      externalNativeBuild {
        cmake {
          ...
          // Specifies which native libraries or executables to build and package
          // for this product flavor. The following tells Gradle to build only the
          // "native-lib-demo" and "my-executible-demo" outputs from the linked
          // CMake project. If you don't configure this property, Gradle builds all
          // executables and shared object libraries that you define in your CMake
          // (or ndk-build) project. However, by default, Gradle packages only the
          // shared libraries in your app.
          targets "native-lib-demo",
                  // You need to specify this executable and its sources in your CMakeLists.txt
                  // using the https://cmake.org/cmake/help/latest/command/add_executable.html command. However, building executables from your
                  // native sources is optional, and building native libraries to package into
                  // your app satisfies most project requirements.
                  "my-executible-demo"
        }
      }
    }

    paid {
      ...
      externalNativeBuild {
        cmake {
          ...
          targets "native-lib-paid",
                  "my-executible-paid"
        }
      }
    }
  }

  // Use this block to link Gradle to your CMake or ndk-build script.
  externalNativeBuild {
    cmake {...}
    // or ndkBuild {...}
  }
}
```

### Kotlin

```kotlin
android {
  ...
  defaultConfig {
    ...
    // This block is different from the one you use to link Gradle
    // to your CMake or ndk-build script.
    externalNativeBuild {

      // For ndk-build, instead use the ndkBuild block.
      cmake {

        // Passes optional arguments to CMake.
        arguments += listOf("-DANDROID_ARM_NEON=TRUE", "-DANDROID_TOOLCHAIN=clang")

        // Sets a flag to enable format macro constants for the C compiler.
        cFlags += listOf("-D__STDC_FORMAT_MACROS")

        // Sets optional flags for the C++ compiler.
        cppFlags += listOf("-fexceptions", "-frtti")
      }
    }
  }

  buildTypes {...}

  productFlavors {
    ...
    create("demo") {
      ...
      externalNativeBuild {
        cmake {
          ...
          // Specifies which native libraries or executables to build and package
          // for this product flavor. The following tells Gradle to build only the
          // "native-lib-demo" and "my-executible-demo" outputs from the linked
          // CMake project. If you don't configure this property, Gradle builds all
          // executables and shared object libraries that you define in your CMake
          // (or ndk-build) project. However, by default, Gradle packages only the
          // shared libraries in your app.
          targets += listOf("native-lib-demo",
                  // You need to specify this executable and its sources in your CMakeLists.txt
                  // using the https://cmake.org/cmake/help/latest/command/add_executable.html command. However, building executables from your
                  // native sources is optional, and building native libraries to package into
                  // your app satisfies most project requirements.
                  "my-executible-demo")
        }
      }
    }

    create("paid") {
      ...
      externalNativeBuild {
        cmake {
          ...
          targets += listOf("native-lib-paid",
                  "my-executible-paid")
        }
      }
    }
  }

  // Use this block to link Gradle to your CMake or ndk-build script.
  externalNativeBuild {
    cmake {...}
    // or ndkBuild {...}
  }
}
```

To learn more about configuring product flavors and build variants, go to[Configure Build Variants](https://developer.android.com/studio/build/build-variants). For a list of variables you can configure for CMake with the`arguments`property, see[Using CMake Variables](https://developer.android.com/ndk/guides/cmake#variables).

### Include prebuilt native libraries

If you want Gradle to package prebuilt native libraries that are not used in any external native build, add them to the`src/main/jniLibs/`<var translate="no">ABI</var>directory of your module.

Versions of the Android Gradle Plugin prior to 4.0 required including CMake`IMPORTED`targets in your`jniLibs`directory for them to be included in your app. If you're migrating from an earlier version of the plugin, you may encounter an error like the following:  

    * What went wrong:
    Execution failed for task ':app:mergeDebugNativeLibs'.
    > A failure occurred while executing com.android.build.gradle.internal.tasks.Workers$ActionFacade
       > More than one file was found with OS independent path 'lib/x86/libprebuilt.so'

If you are using Android Gradle Plugin 4.0, move any libraries that are used by`IMPORTED`CMake targets out of your`jniLibs`directory to avoid this error.

### Specify ABIs

By default, Gradle builds your native library into separate`.so`files for the[Application Binary Interfaces (ABIs) the NDK supports](https://developer.android.com/ndk/guides/abis#sa)and packages them all into your app. If you want Gradle to build and package only certain ABI configurations of your native libraries, you can specify them with the[`ndk.abiFilters`](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.NdkOptions.html)flag in your module-level`build.gradle`file, as shown below:  

### Groovy

```groovy
android {
  ...
  defaultConfig {
    ...
    externalNativeBuild {
      cmake {...}
      // or ndkBuild {...}
    }

    // Similar to other properties in the `defaultConfig` block,
    // you can configure the ndk block for each product flavor
    // in your build configuration.
    ndk {
      // Specifies the ABI configurations of your native
      // libraries Gradle should build and package with your app.
      abiFilters 'x86', 'x86_64', 'armeabi', 'armeabi-v7a',
                   'arm64-v8a'
    }
  }
  buildTypes {...}
  externalNativeBuild {...}
}
```

### Kotlin

```kotlin
android {
  ...
  defaultConfig {
    ...
    externalNativeBuild {
      cmake {...}
      // or ndkBuild {...}
    }

    // Similar to other properties in the `defaultConfig` block,
    // you can configure the ndk block for each product flavor
    // in your build configuration.
    ndk {
      // Specifies the ABI configurations of your native
      // libraries Gradle should build and package with your app.
      abiFilters += listOf("x86", "x86_64", "armeabi", "armeabi-v7a",
                   "arm64-v8a")
    }
  }
  buildTypes {...}
  externalNativeBuild {...}
}
```

In most cases, you only need to specify`abiFilters`in the`ndk`block, as shown above, because it tells Gradle to both build and package those versions of your native libraries. However, if you want to control what Gradle should build, independently of what you want it to package into your app, configure another`abiFilters`flag in the[`defaultConfig.externalNativeBuild.cmake`](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.ExternalNativeCmakeOptions.html#com.android.build.gradle.internal.dsl.ExternalNativeCmakeOptions:abiFilters)block (or[`defaultConfig.externalNativeBuild.ndkBuild`](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.ExternalNativeNdkBuildOptions.html#com.android.build.gradle.internal.dsl.ExternalNativeNdkBuildOptions:abiFilters)block). Gradle builds those ABI configurations but only packages the ones you specify in the[`defaultConfig.ndk`](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.NdkOptions.html)block.

It is recommended to publish using Android App Bundles to further reduce the size of your app, as only native libraries matching the ABI of a user's device will be delivered with the download.

For legacy apps publishing using APKs (created before August 2021), consider[configuring multiple APKs based on ABI](https://developer.android.com/studio/build/configure-apk-splits#configure-abi-split)---instead of creating one large APK with the all versions of your native libraries, Gradle creates a separate APK for each ABI you want to support and only packages the files each ABI needs. If you configure multiple APKs per ABI without specifying the`abiFilters`flag as shown in the code sample above, Gradle builds all supported ABI versions of your native libraries, but only packages those you specify in your multiple APK configuration. To avoid building versions of your native libraries that you don't want, provide the same list of ABIs for both the`abiFilters`flag and your per-ABI multiple APK configuration.