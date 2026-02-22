---
title: https://developer.android.com/jetpack/androidx/releases/compose-kotlin
url: https://developer.android.com/jetpack/androidx/releases/compose-kotlin
source: md.txt
---

# Compose to Kotlin Compatibility Map

| **Note:** If you're using Kotlin 2.0 or higher, configure Compose using the[Compose Compiler Gradle plugin](https://developer.android.com/develop/ui/compose/compiler). When you use the Compose Compiler Gradle plugin, you don't have to check Compose to Kotlin compatibility.

## Declaring dependencies

To add a dependency on the Compose Compiler, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
android {
    buildFeatures {
        compose true
    }

    composeOptions {
        kotlinCompilerExtensionVersion = "1.5.15"
    }

    kotlinOptions {
        jvmTarget = "19"
    }
}
```

### Kotlin

```kotlin
android {
    buildFeatures {
        compose = true
    }

    composeOptions {
        kotlinCompilerExtensionVersion = "1.5.15"
    }

    kotlinOptions {
        jvmTarget = "19"
    }
}
```

## Pre-release Kotlin Compatibility

For Compose Compiler versions that are compatible with pre-release versions of Kotlin, please check out<https://androidx.dev/storage/compose-compiler/repository>for more details.

|                                               Compose Compiler Version                                               | Compatible Kotlin Version |
|----------------------------------------------------------------------------------------------------------------------|---------------------------|
| Use the[Compose Compiler Gradle plugin](https://developer.android.com/develop/ui/compose/compiler)to enable Compose. | 2.0.0+                    |
| 1.5.15                                                                                                               | 1.9.25                    |
| 1.5.14                                                                                                               | 1.9.24                    |
| 1.5.13                                                                                                               | 1.9.23                    |
| 1.5.12                                                                                                               | 1.9.23                    |
| 1.5.11                                                                                                               | 1.9.23                    |
| 1.5.10                                                                                                               | 1.9.22                    |
| 1.5.9                                                                                                                | 1.9.22                    |
| 1.5.8                                                                                                                | 1.9.22                    |
| 1.5.7                                                                                                                | 1.9.21                    |
| 1.5.6                                                                                                                | 1.9.21                    |
| 1.5.5                                                                                                                | 1.9.20                    |
| 1.5.4                                                                                                                | 1.9.20                    |
| 1.5.3                                                                                                                | 1.9.10                    |
| 1.5.2                                                                                                                | 1.9.0                     |
| 1.5.1                                                                                                                | 1.9.0                     |
| 1.5.0                                                                                                                | 1.9.0                     |
| 1.4.8                                                                                                                | 1.8.22                    |
| 1.4.7                                                                                                                | 1.8.21                    |
| 1.4.6                                                                                                                | 1.8.20                    |
| 1.4.5                                                                                                                | 1.8.20                    |
| 1.4.4                                                                                                                | 1.8.10                    |
| 1.4.3                                                                                                                | 1.8.10                    |
| 1.4.2                                                                                                                | 1.8.10                    |
| 1.4.1                                                                                                                | 1.8.0                     |
| 1.4.0                                                                                                                | 1.8.0                     |
| 1.4.0-alpha02                                                                                                        | 1.7.21                    |
| 1.4.0-alpha01                                                                                                        | 1.7.20                    |
| 1.3.2                                                                                                                | 1.7.20                    |
| 1.3.1                                                                                                                | 1.7.10                    |
| 1.3.0                                                                                                                | 1.7.10                    |
| 1.3.0-rc02                                                                                                           | 1.7.10                    |
| 1.3.0-rc01                                                                                                           | 1.7.10                    |
| 1.3.0-beta01                                                                                                         | 1.7.10                    |
| 1.2.0                                                                                                                | 1.7.0                     |
| 1.2.0-rc02                                                                                                           | 1.6.21                    |
| 1.2.0-rc01                                                                                                           | 1.6.21                    |
| 1.2.0-beta03                                                                                                         | 1.6.21                    |
| 1.2.0-beta02                                                                                                         | 1.6.21                    |
| 1.2.0-beta01                                                                                                         | 1.6.21                    |
| 1.2.0-alpha08                                                                                                        | 1.6.20                    |
| 1.2.0-alpha07                                                                                                        | 1.6.10                    |
| 1.2.0-alpha06                                                                                                        | 1.6.10                    |
| 1.2.0-alpha05                                                                                                        | 1.6.10                    |
| 1.2.0-alpha04                                                                                                        | 1.6.10                    |
| 1.2.0-alpha03                                                                                                        | 1.6.10                    |
| 1.2.0-alpha02                                                                                                        | 1.6.10                    |
| 1.2.0-alpha01                                                                                                        | 1.6.10                    |
| 1.1.1                                                                                                                | 1.6.10                    |
| 1.1.0                                                                                                                | 1.6.10                    |
| 1.1.0-rc03                                                                                                           | 1.6.10                    |
| 1.1.0-rc02                                                                                                           | 1.6.10                    |
| 1.1.0-rc01                                                                                                           | 1.6.0                     |
| 1.1.0-beta04                                                                                                         | 1.6.0                     |
| 1.1.0-beta03                                                                                                         | 1.5.31                    |
| 1.1.0-beta02                                                                                                         | 1.5.31                    |
| 1.1.0-beta01                                                                                                         | 1.5.31                    |
| 1.1.0-alpha06                                                                                                        | 1.5.31                    |
| 1.1.0-alpha05                                                                                                        | 1.5.31                    |
| 1.0.5                                                                                                                | 1.5.31                    |
| 1.0.4                                                                                                                | 1.5.31                    |
| 1.1.0-alpha04                                                                                                        | 1.5.30                    |
| 1.1.0-alpha03                                                                                                        | 1.5.30                    |
| 1.0.3                                                                                                                | 1.5.30                    |
| 1.1.0-alpha02                                                                                                        | 1.5.21                    |
| 1.1.0-alpha01                                                                                                        | 1.5.21                    |
| 1.0.2                                                                                                                | 1.5.21                    |
| 1.0.1                                                                                                                | 1.5.21                    |
| 1.0.0                                                                                                                | 1.5.10                    |
| 1.0.0-rc02                                                                                                           | 1.5.10                    |
| 1.0.0-rc01                                                                                                           | 1.5.10                    |