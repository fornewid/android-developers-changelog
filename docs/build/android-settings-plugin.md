---
title: Configure project-wide build properties with the settings plugin  |  Android Studio  |  Android Developers
url: https://developer.android.com/build/android-settings-plugin
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio](https://developer.android.com/studio)
* [Gradle build guides](https://developer.android.com/build/gradle-build-overview)

# Configure project-wide build properties with the settings plugin Stay organized with collections Save and categorize content based on your preferences.




The settings plugin lets you centralize common build properties that apply to
all modules in one place so you don't need to copy and paste the configurations
across multiple modules.

### Apply the settings plugin

Apply the settings plugin in the `settings.gradle` file. The version must be
the same as the AGP version declared in the `libs.versions.toml` file:

### Kotlin

```
pluginManagement {
    // Add the following.
    plugins {
       id("com.android.settings") version "9.1.0" apply false
    }
}

plugins {
    id("com.android.settings")
}
```

### Groovy

```
pluginManagement {
    // Add the following.
    plugins {
       id("com.android.settings") version "9.1.0" apply false
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

```
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

```
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