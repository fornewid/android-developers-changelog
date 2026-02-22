---
title: https://developer.android.com/topic/google-play-instant/feature-module-migration
url: https://developer.android.com/topic/google-play-instant/feature-module-migration
source: md.txt
---

# Migrate your instant app to support Android App Bundles

**Warning:** Google Play Instant will no longer be available. Starting December 2025, Instant Apps cannot be published through Google Play, and all[Google Play services Instant APIs](https://developers.google.com/android/reference/com/google/android/gms/instantapps/package-summary)will no longer work. Users will no longer be served Instant Apps by Play using any mechanism.

We're making this change based on developer feedback and our continuous investments to improve the ecosystem since the introduction of Google Play Instant.

To continue optimizing for user growth, we encourage developers to refer users to their regular app or game, using[deeplinks](https://support.google.com/googleplay/android-developer/answer/12463044)to redirect them to specific journeys or features when relevant.
| **Note:** From June 2023 on, only instant apps published using app bundles are available to users. Please ensure all APK based instant apps have been updated to instant enabled bundles.

If you're still using the deprecated Feature Android Gradle plugin (`com.android.feature`) for your Android Instant App modules, you need to migrate to using the base app plugin (`com.android.application`) and Dynamic Feature plugin (`com.android.dynamic-feature`).

On Android Gradle plugin 3.3.0 and higher, the base app plugin includes support for instant experiences. That is, if the base app module satisfies the requirements for being an instant experience, you get the benefit automatically. You can then include additional features that users can download on demand as instant experiences using the Dynamic Feature plugin. This setup makes it easier to support both an installed and instant app experience from a single project, and allows you to benefit from publishing with[Android App Bundles](https://developer.android.com/guide/app-bundle).

The following table better describes which plugins you will migrate to:

|                                                Description of module                                                |                   Old plugin                    |                                                                              Current plugin                                                                              |
|---------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| The module that includes the basic code, resources, and functionality for your installed or instant app experience. | `com.android.feature`(with`baseFeature = true`) | `com.android.application` **Note:**This module includes all the manifest and signing information required to build and package your app as an Android App Bundle or APK. |
| Additional, modular features that users can download on demand                                                      | `com.android.feature`                           | `com.android.dynamic-feature`(with`dist:instant="true"`and`dist:onDemand="false"`in the module's manifest)                                                               |
| Code and resource for a feature available only to the installed version of your app.                                | `com.android.application`                       | `com.android.dynamic-feature`(with`dist:instant="false"`and`dist:onDemand="false"`in the module's manifest)                                                              |

This page shows you how to migrate your existing instant app project to build an instant-enabled Android App Bundle. It also describes how to build, test, and publish an instant-enabled Android App Bundle.

If you are creating new instant experiences for your app, instead read[Create an instant-enabled feature module](https://developer.android.com/studio/projects/dynamic-delivery#create_instant_enabled).

## Understand the changes

When you migrate your project to instead use the Dynamic Feature plugin,[Android App Bundles](https://developer.android.com/guide/app-bundle)provide a new way to build and publish your app that substantially simplifies distributing optimized APKs to your users.

App bundles simplifies distribution by packaging all your app's compiled code and resources for upload, but defers APK generation and signing to Google Play. Google Play's new app serving model then uses your app bundle to generate and serve optimized APKs for each user's device configuration, so they download only the code and resources they need to run your app. You no longer have to build, sign, and manage multiple APKs to support different devices, and users get smaller, more optimized downloads.

When using the now-deprecated feature plugin, building an instant app required creating a base feature module, which contained the shared code and resources for all your modules, including your instant app module. The rest of your code was included in multiple non-base feature modules, which contained entry points for your instant experiences. For the installed version of your app, your project might have included a separate app module, which contained the code and activities required only for your installed app.

When you migrate your app to support Android App Bundles, your app module reclaims the role of the base module, and you organize additional installed or instant experiences as feature modules. That is, your project now more closely resembles a standard app project, with an instant-enabled base module and the ability to include additional, modular instant experiences.

To migrate your existing instant app project and adopt Android App Bundle's more optimized distribution model, follow the steps described in the sections below.

## Convert the base feature module into an app module

You first need to edit the base feature module's`build.gradle`file before converting it into the main app module, as follows:

1. Delete the`baseFeature true`line.
2. Remove any dependencies that use the`feature`or`application`dependency configurations.

   ### Groovy

   ```groovy
   dependencies {
       ...
       // delete any lines that look like
       // feature project(":foo")
       // feature project(":bar")
       // application project(":app")
   }
   ```

   ### Kotlin

   ```kotlin
   dependencies {
       ...
       // delete any lines that look like
       // feature(project(":foo"))
       // feature(project(":bar"))
       // application(project(":app"))
   }
   ```
3. Move the`applicationId`, along with any other build script configurations you would expect to be in your base app module, from the current`com.android.application`module to the`com.android.feature`module. Some examples are shown below. For this step, depending on your specific`build.gradle`setup, it might be easier to copy and paste the`android`block of the`build.gradle`from the previous app module into the new app module's`build.gradle`file. However, you should exercise caution when doing so.

   ### Groovy

   ```groovy
   android {
       ...
       defaultConfig {
           // You need to move the application ID from the app module
           // to your feature module.
           applicationId "com.example.myapp"
           ...
       }
       // Some additional build configurations you might want to
       // copy from your current 'app' module may include ProGuard
       // rules and code shrinking settings.
       buildTypes {
           release {
               minifyEnabled true
               proguardFiles getDefaultProguardFile(
                 'proguard-android-optimize.txt'),
                 'proguard-rules.pro'
           }
       }
   }
   ```

   ### Kotlin

   ```kotlin
   android {
       ...
       defaultConfig {
           // You need to move the application ID from the app module
           // to your feature module.
           applicationId = "com.example.myapp"
           ...
       }
       // Some additional build configurations you might want to
       // copy from your current 'app' module may include ProGuard
       // rules and code shrinking settings.
       buildTypes {
           getByName("release") {
               minifyEnabled = true
               proguardFiles(
                   getDefaultProguardFile("proguard-android-optimize.txt"),
                   "proguard-rules.pro"
               )
           }
       }
   }
   ```
4. Mark the feature module as instant-enabled by adding the appropriate bundle distribution tags to the manifest, as shown below.

       <manifest ... xmlns:dist="http://schemas.android.com/apk/distribution">
           <dist:module dist:instant="true" />
           ...
       </manifest>

5. Convert the feature module to your base app module by changing its plugin type to`com.android.application`:

   ### Groovy

   ```groovy
   // Replace  "plugins { id 'com.android.feature' }"
   // with the following
   plugins {
     id 'com.android.application'
   }
   ```

   ### Kotlin

   ```kotlin
   // Replace  "plugins { id("com.android.feature") }"
   // with the following
   plugins {
       id("com.android.application")
   }
   ```

## Convert the old app module into an install-time feature module

If you have no code or resources in the old app module, you can simply delete it---because the steps you followed in the previous section converted your feature module into your app's base app module.

However, if you have code and resources in the old app module that represent functionality you'd like to be available to users when they install your app, follow the steps in this section to convert the app module to a feature module.

Creating a feature module involves changing the plugin type from`com.android.application`to`com.android.dynamic-feature`, along with a few other`build.gradle`changes, as follows:

1. Change the plugin type from`com.android.application`to`com.android.dynamic-feature`.

   ### Groovy

   ```groovy
   // Replace "plugins { id 'com.android.feature' }"
   // with the following:
   plugins {
     id 'com.android.dynamic-feature'
   }
   ```

   ### Kotlin

   ```kotlin
   // Replace "plugins { id("com.android.application") }"
   // with the following:
   plugins {
       id("com.android.dynamic-feature")
   }
   ```
2. As described in the previous section, make sure you've moved build configurations that are required by the`com.android.application`plugin to the base app module, such as`applicationId`or`proguardFiles`rules.

3. Rename the module to something like "installed_feature" as follows:

   1. Open the**Project** pane by selecting**View \> Tool Windows \> Project**from the menu bar.
   2. Right-click on the feature module and select**Refactor \> Rename**.
   3. In the dialog that appears, select**Rename module** and click**OK**.
   4. Enter the new name for the module and click**OK**.
4. Similar to step 3, rename the new app module you created in the previous section to something like "app".

5. Add an implementation dependency on the "app" module in the feature module's`build.gradle`file, as shown below.

   ### Groovy

   ```groovy
   dependencies {
       ...
       // In the feature module, add an implementation dependency
       // on the base app module.
       implementation project(":app")
   }
   ```

   ### Kotlin

   ```kotlin
   dependencies {
       ...
       // In the feature module, add an implementation dependency
       // on the base app module.
       implementation(project(":app"))
   }
   ```
6. Add the feature to the new app module's`build.gradle`file.

   ### Groovy

   ```groovy
   android {
       ...
       // In the base app module, specify each feature module.
       dynamicFeatures = [":installed_feature"]
   }
   ```

   ### Kotlin

   ```kotlin
   android {
       ...
       // In the base app module, specify each feature module.
       dynamicFeatures.addAll(listOf(":installed_feature"))
   }
   ```
7. In the feature module's manifest, mark the feature module as an installable module by adding the appropriate bundle distribution tags to the manifest.

       <manifest ... xmlns:dist="http://schemas.android.com/apk/distribution">
           <dist:module dist:instant="false" dist:onDemand="false"
                   dist:title="@string/title_dynamic_feature">
               <dist:fusing dist:include="true" />
           </dist:module>
           ...
       </manifest>

## Convert other feature modules into instant-enabled feature modules

If you've modularized additional functionality of your app into multiple Feature modules, you need to follow the steps in this section to convert those modules into instant-enabled feature modules.

For each remaining feature module in your project, proceed as follows to convert them into instant-enabled features:

1. Change the plugin type in the`build.gradle`file to`com.android.dynamic-feature`, as shown below:

   ### Groovy

   ```groovy
   // Replace 'com.android.feature' with 'com.android.dynamic-feature'
   plugins {
     id 'com.android.dynamic-feature'
   }
   ```

   ### Kotlin

   ```kotlin
   // Replace "com.android.feature" with "com.android.dynamic-feature"
   plugins {
       id("com.android.dynamic-feature")
   }
   ```
2. Mark each feature module as instant-enabled by adding the following to the manifest.

       <manifest ... xmlns:dist="http://schemas.android.com/apk/distribution">
           <dist:module dist:instant="true" dist:onDemand="false"
                   dist:title="@string/title_dynamic_feature">
               <dist:fusing dist:include="true" />
           </dist:module>
           ...
       </manifest>

3. Add the feature module to the new application module's`build.gradle`file where you added the`installed_feature`to the list of feature modules.

   ### Groovy

   ```groovy
   android {
      ...
      dynamicFeatures = [":installed_feature", ":feature_1", ":feature_2"]
      // or whichever name exists for the instant enabled feature module
   }
   ```

   ### Kotlin

   ```kotlin
   android {
      ...
      dynamicFeatures.addAll(listOf(":installed_feature", ":feature_1", ":feature_2"))
      // or whichever name exists for the instant enabled feature module
   }
   ```

## Build, test, and publish new instant-enabled app bundle

After completing the steps on this page, your project is able to produce a single artifact, an Android App Bundle, that you can use to publish both the installed and instant version of your app to the Google Play Console, and roll out separately for the instant and installed tracks. Additionally with app bundles, you get the benefit of serving optimized APKs for each user's device configuration, so they download only the code and resources they need to run your app. That is, you no longer have to build, sign, and manage multiple APKs to support different devices, and users get smaller, more optimized downloads.

To start building and testing your instant-enabled app bundle, go to[Build the app bundle](https://developer.android.com/topic/google-play-instant/getting-started/instant-enabled-app-bundle#build).