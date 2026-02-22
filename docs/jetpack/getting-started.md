---
title: https://developer.android.com/jetpack/getting-started
url: https://developer.android.com/jetpack/getting-started
source: md.txt
---

# Getting started with Android Jetpack

Jetpack encompasses a collection of Android libraries that incorporate best practices and provide backwards compatibility in your Android apps.

The[Jetpack guide to app architecture](https://developer.android.com/jetpack/guide)provides an overview of the best practices and recommended architecture to consider as you build your Android app.

The following sections cover how you can get started using Jetpack components.
| **Note:** Jetpack libraries don't send any user data to a backend service of any kind. This means that integrating a Jetpack library into your app has no impact on your app's[Data safety form](https://developer.android.com/guide/topics/data/collect-share)in the Play Console.

## Use a Jetpack library in your app

All Jetpack components are available on the[Google Maven repository](https://dl.google.com/dl/android/maven2/index.html).

Open the`settings.gradle`file add the`google()`repository in the`dependencyResolutionManagement { repositories {...}}`block as shown below:  

### Groovy

```groovy
dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        jcenter()
    }
}
```

### Kotlin

```kotlin
dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        jcenter()
    }
}
```
| **Warning:** The JCenter repository became read-only on March 31st, 2021. For more information, see[JCenter service update](https://developer.android.com/studio/build/jcenter-migration).

You can then add Jetpack components, such as architecture components like[LiveData](https://developer.android.com/topic/libraries/architecture/livedata)and[ViewModel](https://developer.android.com/topic/libraries/architecture/viewmodel), in your module's`build.gradle`file, as shown here:  

### Groovy

```groovy
dependencies {
    def lifecycle_version = "2.2.0"

    implementation "androidx.lifecycle:lifecycle-livedata-ktx:$lifecycle_version"
    implementation "androidx.lifecycle:lifecycle-viewmodel-ktx:$lifecycle_version"
    ...
}
```

### Kotlin

```kotlin
dependencies {
    val lifecycle_version = "2.2.0"

    implementation("androidx.lifecycle:lifecycle-livedata-ktx:$lifecycle_version")
    implementation("androidx.lifecycle:lifecycle-viewmodel-ktx:$lifecycle_version")
    ...
}
```

Many Jetpack libraries provide[Android KTX extensions](https://developer.android.com/kotlin/ktx)as shown above with`lifecycle-livedata-ktx`and`lifecycle-viewmodel-ktx`. The KTX extensions build upon the Java-based API, taking advantage of Kotlin-specific language features.

To learn of new Jetpack library releases, check out the[Releases](https://developer.android.com/jetpack/androidx/releases)page.

[Kotlin-based](https://developer.android.com/reference/kotlin/androidx/packages)and[Java-based](https://developer.android.com/reference/androidx/packages)API reference pages are available for all Jetpack libraries.

### Verify Jetpack dependencies (optional)

| **Note:** Signature verification is an opt-in feature for Gradle builds. If needed, you can[enable signature verification](https://docs.gradle.org/current/userguide/dependency_verification.html).

As of June 2023, the Jetpack team signs Jetpack libraries. These signatures allow developers to verify that the library artifacts are built and signed by Google. A library is eligible for signature verification once it publishes an update.
| **Note:** Libraries released prior to June 2023 don't contain signatures and don't pass signature verification.

If your Android project has signature verification enabled, follow these steps to verify Jetpack dependencies in the Gradle project:

1. Add Google's trusted keys to the`<trusted-keys>`section in`$PROJECT_ROOT/gradle/verification-metadata.xml`:

       <trusted-keys>
           \<trusted-key id="8461efa0e74abae010de66994eb27db2a3b88b8b"\>
               ...
           \</trusted-key\>
           \<trusted-key id="a5f483cd733a4ebaea378b2ae88979fb9b30acf2"\>
               ...
           \</trusted-key\>
           \<trusted-key id="0f06ff86beeaf4e71866ee5232ee5355a6bc6e42"\>
               ...
           \</trusted-key\>
           \<trusted-key id="0e225917414670f4442c250dfd533c07c264648f"\>
               ...
           \</trusted-key\>
           ...
       </trusted-keys>

2. Add a`<trusting group>`entry for each library that the project is using. Here's an example for the`androidx.fragment`and`androidx.emoji2`libraries:

       <trusted-keys>
           <trusted-key id="8461efa0e74abae010de66994eb27db2a3b88b8b">
               \<trusting group="androidx.fragment"/\>
               \<trusting group="androidx.emoji2"/\>
           </trusted-key>
           <trusted-key id="a5f483cd733a4ebaea378b2ae88979fb9b30acf2">
               \<trusting group="androidx.fragment"/\>
               \<trusting group="androidx.emoji2"/\>
           </trusted-key>
           ...
       </trusted-keys>

For issues with dependency verification, visit Gradle's guide on[troubleshooting dependency verification](https://docs.gradle.org/current/userguide/dependency_verification.html#sub:enabling-verification).

Finally, details on our trusted key can be viewed on[Ubuntu's keyserver site](https://keyserver.ubuntu.com/pks/lookup?search=0x8461efa0e74abae010de66994eb27db2a3b88b8b&fingerprint=on&op=index).

## Take advantage of Jetpack

Jetpack libraries may be used alone or in combination to address different needs in your apps.

- [WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager)for your background scheduling needs.
- [Room](https://developer.android.com/topic/libraries/architecture/room)for data storage persistence.
- [Navigation](https://developer.android.com/guide/navigation/navigation-getting-started)to manage your application navigation flow.
- [CameraX](https://developer.android.com/training/camerax)for your camera app needs.
- See the[Overview](https://developer.android.com/jetpack/androidx/versions#version-table)of all the Jetpack libraries.

Jetpack libraries are published in the`androidx`namespace. If your project currently uses the Android Support Library, read how to[migrate to the androidx namespace](https://developer.android.com/jetpack/androidx/migrate).

To learn more about using Jetpack, check out these pages:

- [Android Architecture Components](https://developer.android.com/topic/libraries/architecture)
- [Complete list of Jetpack components](https://developer.android.com/jetpack/androidx/explorer)

## Additional resources

### Online training

- [Developing Android Apps with Kotlin](https://www.udacity.com/course/developing-android-apps-with-kotlin--ud9012)(Udacity course)

### Sample code

- The[Sunflower](https://github.com/android/sunflower)demo app uses many different Jetpack components to demonstrate Android development best practices.

### Codelabs

- [Android Lifecycles](https://codelabs.developers.google.com/codelabs/android-lifecycles/index.html)
- [Room with a View](https://codelabs.developers.google.com/codelabs/android-room-with-a-view-kotlin)

### Videos

- [Assembling your Jetpack](https://youtu.be/2h-vuXC0SF8)