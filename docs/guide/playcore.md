---
title: https://developer.android.com/guide/playcore
url: https://developer.android.com/guide/playcore
source: md.txt
---

This page describes the Google Play Core libraries and how to add them to your
project.
| **Important:** The Google Play Core Java and Kotlin library have been split into multiple separate libraries, one for each feature. Update to the new libraries to benefit from new product additions. For more information, see the [migration guide](https://developer.android.com/guide/playcore#playcore-migration).

The Google Play Core libraries are your app's runtime interface with the Google Play
Store. Some of the things you can do include the following:

- [Download additional language resources](https://developer.android.com/guide/playcore/feature-delivery/on-demand#lang_resources)
- [Manage delivery of feature modules](https://developer.android.com/guide/playcore/feature-delivery)
- [Manage delivery of asset packs](https://developer.android.com/guide/playcore/asset-delivery)
- [Trigger in-app updates](https://developer.android.com/guide/playcore/in-app-updates)
- [Request in-app reviews](https://developer.android.com/guide/playcore/in-app-review)

The Play Core libraries are available in
[Java](https://developer.android.com/reference/com/google/android/play/core/packages),
[native](https://developer.android.com/reference/native/play/core), and [Unity](https://developer.android.com/reference/unity). For more
information about the latest releases, see the
[Release notes](https://developer.android.com/reference/com/google/android/play/core/release-notes).

## Migration from the Play Core Java and Kotlin Library

The Play Core Java and Kotlin Library has been partitioned into multiple
per-feature Android libraries. This reduces the size Play Core libraries add to
your app and allows for faster release cycles of the individual features.

The behavior of each feature has stayed consistent in this migration, the only
notable change is that the new versions have adopted [Google Play Services' Task API](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task).

Use the list below to migrate to the new libraries and benefit from new features
and bug fixes. If you use multiple Play features, you can simply import multiple
libraries in your `build.gradle` file at once.

### Common migration steps

1. Update any existing import statements of Task objects from `import com.google.android.play.core.tasks.*;` to `import com.google.android.gms.tasks.*;`. All class names are unchanged.
2. Remove any imports of the old Play Core libraries in your `build.gradle` file.

### Integrate the Play Asset Delivery Library

### Groovy

```groovy
// In your app's build.gradle file:
...
dependencies {
    // This dependency is downloaded from the https://developer.android.com/studio/build/dependencies#google-maven.
    // So, make sure you also include that repository in your project's build.gradle file.
    implementation 'com.google.android.play:asset-delivery:2.3.0'

    // For Kotlin users also add the Kotlin extensions library for Play Asset Delivery:
    implementation 'com.google.android.play:asset-delivery-ktx:2.3.0'
    ...
}
```

### Kotlin

```kotlin
// In your app's build.gradle.kts file:
...
dependencies {
    // This dependency is downloaded from the https://developer.android.com/studio/build/dependencies#google-maven.
    // So, make sure you also include that repository in your project's build.gradle file.
    implementation("com.google.android.play:asset-delivery:2.3.0")

    // For Kotlin users also import the Kotlin extensions library for Play Asset Delivery:
    implementation("com.google.android.play:asset-delivery-ktx:2.3.0")
    ...
}
```

### Integrate the Play Feature Delivery Library

### Groovy

```groovy
// In your app's build.gradle file:
...
dependencies {
    // This dependency is downloaded from the https://developer.android.com/studio/build/dependencies#google-maven.
    // So, make sure you also include that repository in your project's build.gradle file.
    implementation 'com.google.android.play:feature-delivery:2.1.0'

    // For Kotlin users, also add the Kotlin extensions library for Play Feature Delivery:
    implementation 'com.google.android.play:feature-delivery-ktx:2.1.0'
    ...
}
```

### Kotlin

```kotlin
// In your app's build.gradle.kts file:
...
dependencies {
    // This dependency is downloaded from the https://developer.android.com/studio/build/dependencies#google-maven.
    // Make sure you also include that repository in your project's build.gradle file.
    implementation("com.google.android.play:feature-delivery:2.1.0")

    // For Kotlin users, also import the Kotlin extensions library for Play Feature Delivery:
    implementation("com.google.android.play:feature-delivery-ktx:2.1.0")
    ...
}
```

### Integrate the Play In-App Review Library

### Groovy

```groovy
// In your app's build.gradle file:
...
dependencies {
    // This dependency is downloaded from the https://developer.android.com/studio/build/dependencies#google-maven.
    // Make sure you also include that repository in your project's build.gradle file.
    implementation 'com.google.android.play:review:2.0.2'

    // For Kotlin users, also add the Kotlin extensions library for Play In-App Review:
    implementation 'com.google.android.play:review-ktx:2.0.2'
    ...
}
```

### Kotlin

```kotlin
// In your app's build.gradle.kts file:
...
dependencies {
    // This dependency is downloaded from the https://developer.android.com/studio/build/dependencies#google-maven.
    // Make sure you also include that repository in your project's build.gradle file.
    implementation("com.google.android.play:review:2.0.2")

    // For Kotlin users, also import the Kotlin extensions library for Play In-App Review:
    implementation("com.google.android.play:review-ktx:2.0.2")
    ...
}
```

### Integrate the Play In-App Update Library

### Groovy

```groovy
// In your app's build.gradle file:
...
dependencies {
    // This dependency is downloaded from the https://developer.android.com/studio/build/dependencies#google-maven.
    // Make sure you also include that repository in your project's build.gradle file.
    implementation 'com.google.android.play:app-update:2.1.0'

    // For Kotlin users, also add the Kotlin extensions library for Play In-App Update:
    implementation 'com.google.android.play:app-update-ktx:2.1.0'
    ...
}
```

### Kotlin

```kotlin
// In your app's build.gradle.kts file:
...
dependencies {
    // This dependency is downloaded from the https://developer.android.com/studio/build/dependencies#google-maven.
    // Make sure you also include that repository in your project's build.gradle file.
    implementation("com.google.android.play:app-update:2.1.0")

    // For Kotlin users, also import the Kotlin extensions library for Play In-App Update:
    implementation("com.google.android.play:app-update-ktx:2.1.0")
    ...
}
```

## Play Core Software Development Kit Terms of Service

Last modified: September 24, 2020

1. By using the Play Core Software Development Kit, you agree to these terms in addition to the [Google APIs Terms of Service](https://developers.google.com/terms) ("API ToS"). If these terms are ever in conflict, these terms will take precedence over the API ToS. Please read these terms and the API ToS carefully.
2. For purposes of these terms, "APIs" means Google's APIs, other developer services, and associated software, including any Redistributable Code.
3. "Redistributable Code" means Google-provided object code or header files that call the APIs.
4. Subject to these terms and the terms of the API ToS, you may copy and distribute Redistributable Code solely for inclusion as part of your API Client. Google and its licensors own all right, title and interest, including any and all intellectual property and other proprietary rights, in and to Redistributable Code. You will not modify, translate, or create derivative works of Redistributable Code.
5. Google may make changes to these terms at any time with notice and the opportunity to decline further use of the Play Core Software Development Kit. Google will post notice of modifications to the terms at <https://developer.android.com/guide/playcore/license>. Changes will not be retroactive.