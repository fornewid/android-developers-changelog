---
title: https://developer.android.com/build/releases/agp-2-2-0-release-notes
url: https://developer.android.com/build/releases/agp-2-2-0-release-notes
source: md.txt
---

<br />

# Android Gradle Plugin 2.2.0 (September 2016)

Dependencies:
New:
:
    - Uses Gradle 2.14.1, which includes performance improvements and new features, and fixes a security vulnerability that allows local privilege escalation when using the Gradle daemon. For more details, see the [Gradle release notes](https://docs.gradle.org/2.14.1/release-notes).
    - Using the [`externalNativeBuild {}`](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.ExternalNativeBuild.html) DSL, Gradle now lets you link to your native sources and compile native libraries using CMake or ndk-build. After building your native libraries, Gradle packages them into your APK. To learn more about using CMake and ndk-build with Gradle, read [Add C and C++ Code to Your
      Project](https://developer.android.com/studio/projects/add-native-code).
    - When you [run a
      build from the command line](https://developer.android.com/studio/build/building-cmdline), Gradle now attempts to auto-download any missing SDK components or updates that your project depends on. To learn more, read [Auto-download
      missing packages with Gradle](https://developer.android.com/studio/intro/update#download-with-gradle).
    - A new experimental caching feature lets Gradle speed up build times by pre-dexing, storing, and reusing the pre-dexed versions of your libraries. To learn more about using this experimental feature, read the [Build
      Cache](https://developer.android.com/studio/build/build-cache) guide.
    - Improves build performance by adopting a new default packaging pipeline which handles zipping, signing, and [zipaligning](https://developer.android.com/studio/command-line/zipalign) in one task. You can revert to using the older packaging tools by adding `android.useOldPackaging=true` to your `gradle.properties` file. While using the new packaging tool, the `zipalignDebug` task is not available. However, you can create one yourself by calling the `createZipAlignTask(String taskName, File inputFile, File
      outputFile)` method.
    - APK signing now uses [APK Signature Scheme
      v2](https://developer.android.com/about/versions/nougat/android-7.0#apk_signature_v2) in addition to traditional JAR signing. All Android platforms accept the resulting APKs. Any modification to these APKs after signing invalidates their v2 signatures and prevents installation on a device. To disable this feature, add the following to your module-level `build.gradle` file:

      ### Groovy

      ```groovy
      android {
        ...
        signingConfigs {
          config {
            ...
            v2SigningEnabled false
          }
        }
      }
            
      ```

      ### Kotlin

      ```kotlin
      android {
        ...
        signingConfigs {
          create("config") {
            ...
            v2SigningEnabled = false
          }
        }
      }
            
      ```
    - For multidex builds, you can now use ProGuard rules to determine which classes Gradle should compile into your app's *main* DEX file. Because the Android system loads the main DEX file first when starting your app, you can prioritize certain classes at startup by compiling them into the main DEX file. After you create a ProGuard configuration file specifically for your main DEX file, pass the configuration file's path to Gradle using `https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.BuildType.html#com.android.build.gradle.internal.dsl.BuildType:multiDexKeepProguard`. Using this DSL is different from using [`buildTypes.proguardFiles`](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.BuildType.html#com.android.build.gradle.internal.dsl.BuildType:proguardFiles(java.lang.Object[])), which provides general ProGuard rules for your app and does not specify classes for the main DEX file.
    - Adds support for the `android:extractNativeLibs` flag, which can reduce the size of your app when you install it on a device. When you set this flag to `false` in the [`<application>`](https://developer.android.com/guide/topics/manifest/application-element) element of your app manifest, Gradle packages uncompressed and aligned versions of your native libraries with your APK. This prevents [`PackageManager`](https://developer.android.com/reference/android/content/pm/PackageManager) from copying out your native libraries from the APK to the device's file system during installation and has the added benefit of making delta updates of your app smaller.
    - You can now specify [`versionNameSuffix`](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.ProductFlavor.html#com.android.build.gradle.internal.dsl.ProductFlavor:versionNameSuffix) and [`applicationIdSuffix`](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.ProductFlavor.html#com.android.build.gradle.internal.dsl.ProductFlavor:applicationIdSuffix) for product flavors. ([Issue 59614](http://b.android.com/59614))


Changes:
:
    - `getDefaultProguardFile` now returns the default ProGuard files that Android plugin for Gradle provides and no longer uses the ones in the Android SDK.
    - Improved Jack compiler performance and features:
      - Jack now supports Jacoco test coverage when setting `https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.BuildType.html#com.android.build.gradle.internal.dsl.BuildType:testCoverageEnabled` to `true`.
      - Improved support for annotation processors. Annotation processors on your classpath, such as any `compile` dependencies, are automatically applied to your build. You can also specify an annotation processor in your build and pass arguments by using the [`javaCompileOptions.annotationProcessorOptions {}`](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.AnnotationProcessorOptions.html) DSL in your module-level `build.gradle` file:

        ### Groovy

        ```groovy
        android {
          ...
          defaultConfig {
            ...
            javaCompileOptions {
              annotationProcessorOptions {
                className 'com.example.MyProcessor'
                // Arguments are optional.
                arguments = [ foo : 'bar' ]
              }
            }
          }
        }
            
        ```

        ### Kotlin

        ```kotlin
        android {
          ...
          defaultConfig {
            ...
            javaCompileOptions {
              annotationProcessorOptions {
                className = "com.example.MyProcessor"
                // Arguments are optional.
                arguments(mapOf(foo to "bar"))
              }
            }
          }
        }
            
        ```


        If you want to apply an annotation processor at compile
        time but not include it in your APK, use the
        `annotationProcessor` dependency scope:

        ### Groovy

        ```groovy
        dependencies {
            compile 'com.google.dagger:dagger:2.0'
            annotationProcessor 'com.google.dagger:dagger-compiler:2.0'
           // or use buildVariantAnnotationProcessor to target a specific build variant
        }
            
        ```

        ### Kotlin

        ```kotlin
        dependencies {
            implementation("com.google.dagger:dagger:2.0")
            annotationProcessor("com.google.dagger:dagger-compiler:2.0")
           // or use buildVariantAnnotationProcessor to target a specific build variant
        }
            
        ```
      - For a list of parameters you can set, run the following from the command line:

      ```
      java -jar /build-tools/jack.jar --help-properties
      ```
      - By default, if the Gradle daemon's heap size is at least 1.5 GB, Jack now runs in the same process as Gradle. To adjust the daemon heap size, add the following to your `gradle.properties` file:

        <br />

        ```
        # This sets the daemon heap size to 1.5GB.
        org.gradle.jvmargs=-Xmx1536M
        ```

        <br />


<br />