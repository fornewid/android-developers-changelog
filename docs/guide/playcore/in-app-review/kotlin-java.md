---
title: https://developer.android.com/guide/playcore/in-app-review/kotlin-java
url: https://developer.android.com/guide/playcore/in-app-review/kotlin-java
source: md.txt
---

> Documentation index: https://developer.android.com/guide/playcore/in-app-review/llms.txt

This guide describes how to integrate in-app reviews in your app using either
Kotlin or Java. There are separate integration guides if you are using [native
code](https://developer.android.com/guide/playcore/in-app-review/native), [Unity](https://developer.android.com/guide/playcore/in-app-review/unity.md.txt) or [Unreal Engine](https://developer.android.com/guide/playcore/in-app-review/unreal-engine.md.txt).

## Set up your development environment

The Play In-App Review Library is a part of the [Google Play Core libraries](https://developer.android.com/guide/playcore.md.txt).
Include the following Gradle dependency to integrate the Play In-App Review
Library.

### Groovy

```groovy
// In your app's build.gradle file:
...
dependencies {
    // This dependency is downloaded from the Google's Maven repository.
    // So, make sure you also include that repository in your project's build.gradle file.
    implementation 'com.google.android.play:review:2.0.2'

    // For Kotlin users also add the Kotlin extensions library for Play In-App Review:
    implementation 'com.google.android.play:review-ktx:2.0.2'
    ...
}
```

### Kotlin

```kotlin
// In your app's build.gradle.kts file:
...
dependencies {
    // This dependency is downloaded from the Google's Maven repository.
    // So, make sure you also include that repository in your project's build.gradle file.
    implementation("com.google.android.play:review:2.0.2")

    // For Kotlin users also import the Kotlin extensions library for Play In-App Review:
    implementation("com.google.android.play:review-ktx:2.0.2")
    ...
}
```

## Create the ReviewManager

The [`ReviewManager`](https://developer.android.com/reference/com/google/android/play/core/review/ReviewManager.md.txt) is the interface that lets your app start an in-app
review flow. Obtain it by creating an instance using the
[`ReviewManagerFactory`](https://developer.android.com/reference/com/google/android/play/core/review/ReviewManagerFactory.md.txt).

### Kotlin

```kotlin
val manager = ReviewManagerFactory.create(context)
```

### Java

```java
ReviewManager manager = ReviewManagerFactory.create(context)
```

## Request a ReviewInfo object

Follow the guidance about [when to request in-app reviews](https://developer.android.com/guide/playcore/in-app-review.md.txt#when-to-request) to determine good
points in your app's user flow to prompt the user for a review (for example,
when the user completes a level in a game). When your app reaches one of these
points, use the [`ReviewManager`](https://developer.android.com/reference/com/google/android/play/core/review/ReviewManager.md.txt) instance to create a request task. If
successful, the API returns the [`ReviewInfo`](https://developer.android.com/reference/com/google/android/play/core/review/ReviewInfo.md.txt) object needed to start the
in-app review flow.

### Kotlin

```kotlin
val request = manager.requestReviewFlow()
request.addOnCompleteListener { task ->
    if (task.isSuccessful) {
        // Got the ReviewInfo object
        val reviewInfo = task.result
    } else {
        // There was some problem, log or handle the error code.
        @ReviewErrorCode val reviewErrorCode = (task.getException() as ReviewException).errorCode
    }
}
```

### Java

```java
ReviewManager manager = ReviewManagerFactory.create(this);
Task<ReviewInfo> request = manager.requestReviewFlow();
request.addOnCompleteListener(task -> {
    if (task.isSuccessful()) {
        // Get the ReviewInfo object
        ReviewInfo reviewInfo = task.getResult();
    } else {
        // There was some problem, log or handle the error code.
        @ReviewErrorCode int reviewErrorCode = ((ReviewException) task.getException()).getErrorCode();
    }
});
```

> [!NOTE]
> **Note:** The [`ReviewInfo`](https://developer.android.com/reference/com/google/android/play/core/review/ReviewInfo.md.txt) object is only valid for a limited amount of time. Your app should request a `ReviewInfo` object ahead of time (pre-cache) but only once you are certain that your app will launch the in-app review flow.

## Launch the in-app review flow

Use the [`ReviewInfo`](https://developer.android.com/reference/com/google/android/play/core/review/ReviewInfo.md.txt) instance to launch the in-app review flow. Wait until
the user has completed the in-app review flow before your app continues its
normal user flow (such as advancing to the next level).

### Kotlin

```kotlin
val flow = manager.launchReviewFlow(activity, reviewInfo)
flow.addOnCompleteListener { _ ->
    // The flow has finished. The API doesn't indicate whether the user
    // reviewed or not, or even whether the review dialog was shown. Thus, no
    // matter the result, continue your app flow.
}
```

### Java

```java
Task<Void> flow = manager.launchReviewFlow(activity, reviewInfo);
flow.addOnCompleteListener(task -> {
    // The flow has finished. The API doesn't indicate whether the user
    // reviewed or not, or even whether the review dialog was shown. Thus, no
    // matter the result, continue your app flow.
});
```

> [!IMPORTANT]
> **Important:** If an error occurs during the in-app review flow, don't inform the user or change your app's normal user flow. Continue your app's normal user flow after `onComplete` is called.

## Next steps

[Test your app's in-app review flow](https://developer.android.com/guide/playcore/in-app-review/test.md.txt) to verify that your integration is
working correctly.