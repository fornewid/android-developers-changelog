---
title: https://developer.android.com/guide/playcore/install-prompt/kotlin-java
url: https://developer.android.com/guide/playcore/install-prompt/kotlin-java
source: md.txt
---

This guide describes how to integrate in-app install prompts in your app using
either Kotlin or Java.

## Set up your development environment

The Play In-App Install Prompts Library is part of the [Google Play Core
libraries](https://developer.android.com/guide/playcore). To use the library, include the following Gradle
dependency:

    // In your app's build.gradle.kts file:
    ...
    dependencies {
        implementation("com.google.android.play:crossdeviceprompt:0.0.1")
        ...
    }

## Show the cross device install prompt

Determine the best moment in your app's flow to prompt the user to install your
app on another device (for example, when they cast a video from their phone to a
TV). When your app reaches one of these points, perform the following steps:

1. Create a `CrossDevicePromptInstallationRequest`.
2. Use the `CrossDevicePromptManager` to create a request task that accepts the request as a parameter.
3. Use the resulting `CrossDevicePromptInfo` object with `launchPromptFlow()` to show the prompt to the user.

If an error occurs either in obtaining the `CrossDevicePromptInfo` or showing
the prompt, an exception is thrown.

    val crossDevicePromptManager = CrossDevicePromptManagerFactory.create(activity)
    val request = CrossDevicePromptInstallationRequest.create()

    try {
        val info = crossDevicePromptManager.requestInstallationPromptFlow(request).await()
        crossDevicePromptManager.launchPromptFlow(activity, info).await()
    } catch (e: CrossDevicePromptException) {
        Log.e(TAG, "Cross-device prompt failed with error: ${e.errorCode}", e)
    }https://github.com/android/snippets/blob/6ecfaf2718475a5b9fcc2e030c3ff17802e4b205/installprompt/src/main/java/com/example/crossdeviceinstallprompt/MainActivity.kt#L83-L91

> [!IMPORTANT]
> **Important:** If an error occurs during the in-app install prompt flow, don't inform the user or change your app's normal flow. Continue your app's normal flow.

To verify your implementation, see [Test in-app install prompts](https://developer.android.com/guide/playcore/install-prompt/test).