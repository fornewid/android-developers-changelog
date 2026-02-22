---
title: https://developer.android.com/build/releases/agp-2-1-0-release-notes
url: https://developer.android.com/build/releases/agp-2-1-0-release-notes
source: md.txt
---

<br />

# Android Gradle Plugin 2.1.0 (April 2016)

<br />


**2.1.3 (August 2016)**

This update requires Gradle 2.14.1 and higher. Gradle 2.14.1 includes
performance improvements, new features, and an important [security fix](https://docs.gradle.org/2.14/release-notes#local-privilege-escalation-when-using-the-daemon). For more details, see the
[Gradle release notes](https://docs.gradle.org/2.14.1/release-notes).

Dependencies:
New:
:
    - Added support for the N Developer Preview, JDK 8, and [Java 8 language features](https://developer.android.com/preview/j8-jack) using the Jack toolchain. To find out more, read the [N Preview guide](https://developer.android.com/about/versions/nougat).


      **Note:** [Instant
      Run](https://developer.android.com/tools/building/building-studio#instant-run) does not currently work with Jack and will be disabled while
      using the new toolchain. You only need to use Jack if you are developing
      for the N Preview and want to use the supported Java 8 language features.
    - Added default support for incremental Java compilation to reduce compilation time during development. It does this by only recompiling portions of the source that have changed or need to be recompiled. To disable this feature, add the following code to your module-level `build.gradle` file:

      ### Groovy

      ```groovy
      android {
        ...
        compileOptions {
          incremental false
        }
      }
      ```

      ### Kotlin

      ```kotlin
      android {
        ...
        compileOptions {
          incremental = false
        }
      }
      ```
    -
      Added support for dexing-in-process which performs dexing within the build
      process rather than in a separate, external VM processes. This not only makes
      incremental builds faster, but also speeds up full builds. The feature is
      enabled by default for projects that have set the Gradle daemon's maximum heap
      size to at least 2048 MB. You can do this by including the following in your
      project's `gradle.properties` file:

      \`\`\`none org.gradle.jvmargs = -Xmx2048m \`\`\`


      If you have defined a value for [`javaMaxHeapSize`](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.DexOptions.html#com.android.build.gradle.internal.dsl.DexOptions:javaMaxHeapSize) in your module-level `build.gradle`
      file, you need to set `org.gradle.jvmargs` to the value of
      `javaMaxHeapSize` + 1024 MB. For example, if you have set
      `javaMaxHeapSize` to "2048m", you need to add the following to your
      project's `gradle.properties` file:
      \`\`\`none org.gradle.jvmargs = -Xmx3072m \`\`\`


      To disable dexing-in-process, add the following code to your module-level `build.gradle` file:

      ### Groovy

      ```groovy
      android {
        ...
        dexOptions {
            dexInProcess false
        }
      }
      ```

      ### Kotlin

      ```kotlin
      android {
        ...
        dexOptions {
            dexInProcess = false
        }
      }
      ```