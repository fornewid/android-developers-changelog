---
title: Create Baseline Profiles for a library  |  App quality  |  Android Developers
url: https://developer.android.com/topic/performance/baselineprofiles/create-baselineprofile-library
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App quality](https://developer.android.com/quality)
* [Technical quality](https://developer.android.com/quality/technical)

# Create Baseline Profiles for a library Stay organized with collections Save and categorize content based on your preferences.




To create Baseline Profiles for a library, use the
[Baseline Profile Gradle plugin](/topic/performance/baselineprofiles/configure-baselineprofiles).

There are three modules involved in creating Baseline Profiles for a library:

* Sample app module: contains the sample app that uses your library.
* Library module: the module you want to generate the profile for.
* Baseline Profile module: the test module that generates the Baseline Profiles.

To generate a Baseline Profile for a library, perform the following steps:

1. Create a new `com.android.test` module—for example,
   `:baseline-profile`.
2. Configure the `build.gradle.kts` file for the
   `:baseline-profile` module. [The configuration is
   essentially the same as for an app](/topic/performance/baselineprofiles/create-baselineprofile#create-new-profile-plugin), but make sure to set the
   `targetProjectPath` to the sample app module.
3. Create a Baseline Profile test in the `:baseline-profile`
   test module. This needs to be specific to the sample app and must use all
   the functionalities of the library.
4. Update the configuration in `build.gradle.ktss` file in the
   library module, say `:library`.

1. Apply the plugin `androidx.baselineprofile`.
2. Add a `baselineProfile` dependency to the
   `:baseline-profile` module.
3. Apply the consumer plugin configuration you want, as shown in the
   following example.

### Kotlin

```
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

    // Filters the generated profile rules. 
    // This example keeps the classes in the `com.library` package all its subpackages.
    filter {
        include "com.mylibrary.**"
    }
}
```

### Groovy

```
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

    // Filters the generated profile rules. 
    // This example keeps the classes in the `com.library` package all its subpackages.
    filter {
        include 'com.mylibrary.**'
    }
}
```

5. Add the `androidx.baselineprofile` plugin to the
   `build.gradle.kts` file in the app module
   `:sample-app`.

   ### Kotlin

   ```
   plugins {
       ...
       id("androidx.baselineprofile")
   }
   ```

   ### Groovy

   ```
   plugins {
       ...
       id 'androidx.baselineprofile'
   }
   ```
6. Generate the profile by running the following code:
   `./gradlew :library:generateBaselineProfile`.

At the end of the generation task, the Baseline Profile is stored at
`library/src/main/generated/baselineProfiles`.

[Previous

arrow\_back

Create Baseline Profiles](/topic/performance/baselineprofiles/create-baselineprofile)

[Next

Configure Baseline Profile generation

arrow\_forward](/topic/performance/baselineprofiles/configure-baselineprofiles)