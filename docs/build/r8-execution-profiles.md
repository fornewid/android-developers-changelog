---
title: https://developer.android.com/build/r8-execution-profiles
url: https://developer.android.com/build/r8-execution-profiles
source: md.txt
---

The settings plugin lets you create execution profiles for the R8 tool, letting
you configure how R8 runs so it doesn't slow down your build. Depending on the
environment, you can use profiles to run R8 in a separate JVM process and set
JVM arguments, such as maximum heap size.

### Declare an execution profile

[Apply the settings plugin](https://developer.android.com/studio/build/android-settings-plugin#apply-settings-plugin), and then add the `android` block to
the `settings.gradle` file. In this block, you can define different profiles and
then set a default, as shown in the following example:  

### Kotlin

```kotlin
android {
    execution {
        profiles {
            create("server") {
                r8 {
                    runInSeparateProcess = true
                    jvmOptions += listOf("-Xms2048m", "-Xmx8192m", "-XX:+HeapDumpOnOutOfMemoryError")
                }
            }
            create("local") {
                r8 {
                    runInSeparateProcess = true
                    jvmOptions += listOf("-Xms256m", "-Xmx2048m", "-XX:+HeapDumpOnOutOfMemoryError")
                }
            }
            defaultProfile = "server"
        }
    }
}
```

### Groovy

```groovy
android {
    execution {
        profiles {
            register("server") {
                r8 {
                    runInSeparateProcess = true
                    jvmOptions += ["-Xms2048m", "-Xmx8192m", "-XX:+HeapDumpOnOutOfMemoryError"]
                }
            }
            register("local") {
                r8 {
                    runInSeparateProcess = true
                    jvmOptions += ["-Xms256m", "-Xmx2048m", "-XX:+HeapDumpOnOutOfMemoryError"]
                }
            }
            defaultProfile = "server"
        }
    }
}
```

### Override the default profile

To override the current default execution profile, add the following property
to the `gradle.properties` file.  

    android.settings.executionProfile=example-profile