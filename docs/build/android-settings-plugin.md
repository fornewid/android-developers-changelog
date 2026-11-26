---
title: https://developer.android.com/build/android-settings-plugin
url: https://developer.android.com/build/android-settings-plugin
source: md.txt
---

> Documentation index: https://developer.android.com/build/llms.txt

The settings plugin lets you centralize common build properties that apply to
all modules in one place so you don't need to copy and paste the configurations
across multiple modules.

### Apply the settings plugin

Apply the settings plugin in the `settings.gradle` file. The version must be
the same as the AGP version declared in the `libs.versions.toml` file:

### Kotlin

```kotlin
pluginManagement {
    // Add the following.
    plugins {
       id("com.android.settings") version "9.5.0" apply false
    }
}

plugins {
    id("com.android.settings")
}
```

### Groovy

```groovy
pluginManagement {
    // Add the following.
    plugins {
       id("com.android.settings") version "9.5.0" apply false
    }
}

plugins {
    id("com.android.settings")
}
```

### Apply build properties

Apply the `android` block in the `settings.gradle` file. Unlike in module-level
`build.gradle` files, apply the `minSdk` and `targetSdk` to the top-level
`android` block:

### Kotlin

```kotlin
android {
    compileSdk {
        version = release(36) {
            minorApiLevel = 1
        }
    }
    minSdk {
        version = release(23)
    }
    targetSdk {
        version = release(36)
    }
}
```

### Groovy

```groovy
android {
    compileSdk {
        version = release(36) {
            minorApiLevel = 1
        }
    }
    minSdk {
        version = release(23)
    }
    targetSdk {
        version = release(36)
    }
}
```

You should remove these build properties from the module-level `build.gradle`
files if you want the versions defined in the `settings.gradle` file to be
applied. Keeping these properties in the module-level `build.gradle` files
overrides those set in the `settings.gradle` file for that particular module.

### Configure the Kotlin Gradle plugin version

Starting with AGP 9.6.0-alpha06, you can set the incubating
`kotlinGradlePluginVersion` property in your `settings.gradle` file to configure
a single Kotlin Gradle plugin (KGP) version for all projects in the build:

### Kotlin

```kotlin
android {
    kotlinGradlePluginVersion = "2.3.10"
}
```

### Groovy

```groovy
android {
    kotlinGradlePluginVersion = '2.3.10'
}
```

When `kotlinGradlePluginVersion` is set:

- The value must be a concrete KGP version of `2.2.10` or higher (the default is `null`, which leaves KGP unmanaged so AGP uses its default version).
- Kotlin Gradle plugins applied in `plugins` blocks use this version automatically, so you don't need to specify a version on each plugin.
- KGP dependencies on `buildscript` classpaths, including AGP's runtime dependency for built-in Kotlin, align to this version using `org.jetbrains.kotlin:kotlin-gradle-plugins-bom`, which must be available in your plugin or `buildscript` repositories.
- Gradle logs a warning if this overrides a different version in a `plugins` block or a higher version on a `buildscript` classpath.
- This setting doesn't apply to `buildSrc` or included builds. AGP logs a warning if a project uses a different KGP version (for example, because `buildSrc` depends on it).

For more information about KGP version selection and compatibility, see
[Separate default and minimum Kotlin Gradle plugin versions](https://developer.android.com/build/releases/agp-9-6-0-release-notes.md.txt#kgp-default-and-minimum-versions).