---
title: https://developer.android.com/topic/performance/baselineprofiles/create-baselineprofile-library
url: https://developer.android.com/topic/performance/baselineprofiles/create-baselineprofile-library
source: md.txt
---

# Create Baseline Profiles for a library

To create Baseline Profiles for a library, use the[Baseline Profile Gradle plugin](https://developer.android.com/topic/performance/baselineprofiles/configure-baselineprofiles).

There are three modules involved in creating Baseline Profiles for a library:

- Sample app module: contains the sample app that uses your library.
- Library module: the module you want to generate the profile for.
- Baseline Profile module: the test module that generates the Baseline Profiles.

To generate a Baseline Profile for a library, perform the following steps:  
1. Create a new`com.android.test`module---for example,`:baseline-profile`.
2. Configure the`build.gradle.kts`file for the`:baseline-profile`module.[The configuration is essentially the same as for an app](https://developer.android.com/topic/performance/baselineprofiles/create-baselineprofile#create-new-profile-plugin), but make sure to set the`targetProjectPath`to the sample app module.
3. Create a Baseline Profile test in the`:baseline-profile`test module. This needs to be specific to the sample app and must use all the functionalities of the library.
4. Update the configuration in`build.gradle.ktss`file in the library module, say`:library`.
   1. Apply the plugin`androidx.baselineprofile`.
   2. Add a`baselineProfile`dependency to the`:baseline-profile`module.
3. Apply the consumer plugin configuration you want, as shown in the following example.  

### Kotlin

```kotlin
plugins {
    id("com.android.library")
    id("androidx.baselineprofile")
}

android { ... }

dependencies {
    ...
    // Add a baselineProfile dependency to the `:baseline-profile` module.
    baselineProfile(project(":baseline-profile"))
}

// Baseline Profile Gradle plugin configuration.
baselineProfile {

    // https://developer.android.com/topic/performance/baselineprofile/configure-baselineprofiles#filter-profile-rules the generated profile rules. 
    // This example keeps the classes in the `com.library` package all its subpackages.
    filter {
        include "com.mylibrary.**"
    }
}
```

### Groovy

```groovy
plugins {
    id 'com.android.library'
    id 'androidx.baselineprofile'
}

android { ... }

dependencies {
    ...
    // Add a baselineProfile dependency to the `:baseline-profile` module.
    baselineProfile ':baseline-profile'
}

// Baseline Profile Gradle plugin configuration.
baselineProfile {

    // https://developer.android.com/topic/performance/baselineprofile/configure-baselineprofiles#filter-profile-rules the generated profile rules. 
    // This example keeps the classes in the `com.library` package all its subpackages.
    filter {
        include 'com.mylibrary.**'
    }
}
```
5. Add the`androidx.baselineprofile`plugin to the`build.gradle.kts`file in the app module`:sample-app`.  

   ### Kotlin

   ```kotlin
   plugins {
       ...
       id("androidx.baselineprofile")
   }
   ```

   ### Groovy

   ```groovy
   plugins {
       ...
       id 'androidx.baselineprofile'
   }
   ```
6. Generate the profile by running the following code:`./gradlew :library:generateBaselineProfile`.

At the end of the generation task, the Baseline Profile is stored at`library/src/main/generated/baselineProfiles`.