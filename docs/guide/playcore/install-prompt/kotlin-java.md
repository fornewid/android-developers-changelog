---
title: https://developer.android.com/guide/playcore/install-prompt/kotlin-java
url: https://developer.android.com/guide/playcore/install-prompt/kotlin-java
source: md.txt
---

This guide describes how to integrate in-app install prompts in your app using
either Kotlin or Java.
| **Note:** Only early access partners can display in-app install prompts. [Learn about participating in the early access program](https://developer.android.com/guide/playcore/install-prompt).

## Set up your development environment

The Play In-App Install Prompts Library is part of the [Google Play Core
libraries](https://developer.android.com/guide/playcore). To use the library, include the following Gradle
dependency:  

### Groovy

    // In your app's build.gradle file:
    ...
    dependencies {
        // This dependency is downloaded from the <a href="/studio/build/dependencies#google-maven">Google's Maven repository</a>.
        // So, make sure you also include that repository in your project's build.gradle file.
        implementation 'com.google.android.play:crossdeviceprompt:0.0.1-eap01'
        ...
    }

### Kotlin

    // In your app's build.gradle.kts file:
    ...
    dependencies {
        // This dependency is downloaded from the <a href="/studio/build/dependencies#google-maven">Google's Maven repository</a>.
        // So, make sure you also include that repository in your project's build.gradle file.
        implementation("com.google.android.play:crossdeviceprompt:0.0.1-eap01")
        ...
    }

## Create the CrossDevicePromptManager

The `CrossDevicePromptManager` is the interface that lets your app request
information and launch the install prompt flow. Create an instance to obtain it:  

### Kotlin

    import com.google.android.play.core.crossdeviceprompt.CrossDevicePromptInfo
    import com.google.android.play.core.crossdeviceprompt.CrossDevicePromptManager
    import com.google.android.play.core.crossdeviceprompt.CrossDevicePromptManagerFactory
    import com.google.android.play.core.crossdeviceprompt.model.CrossDevicePromptInstallationRequest

    ...

    val crossDevicePromptManager: CrossDevicePromptManager =
        CrossDevicePromptManagerFactory.create(context)

### Java

    import com.google.android.play.core.crossdeviceprompt.CrossDevicePromptInfo;
    import com.google.android.play.core.crossdeviceprompt.CrossDevicePromptManager;
    import com.google.android.play.core.crossdeviceprompt.CrossDevicePromptManagerFactory;
    import com.google.android.play.core.crossdeviceprompt.model.CrossDevicePromptInstallationRequest;

    ...

    CrossDevicePromptManager crossDevicePromptManager =
        CrossDevicePromptManagerFactory.create(context);

## Request a CrossDevicePromptInstallationRequest object

Determine the best moment in your app's flow to prompt the user to install your
app on another device (for example, when they cast a video from their phone to a
TV). When your app reaches one of these points, perform the following steps:

1. Create a `CrossDevicePromptInstallationRequest`.
2. Use the `CrossDevicePromptManager` to create a request task that accepts the request as a parameter.

If the task is successful, the API returns the `CrossDevicePromptInfo` object in
the success callback. Otherwise, the API returns an `Exception` in the failure
callback.  

### Kotlin

    val request: CrossDevicePromptInstallationRequest? =
        CrossDevicePromptInstallationRequest.create()
    val result: Task<CrossDevicePromptInfo?> =
        crossDevicePromptManager.requestInstallationPromptFlow(request)

    result.addOnSuccessListener { crossDevicePromptInfo ->
        // Requested a prompt flow successfully
    }

    result.addOnFailureListener { e ->
        // Failed to request a prompt flow
    }

### Java

    CrossDevicePromptInstallationRequest request =
        CrossDevicePromptInstallationRequest.create();
    Task<CrossDevicePromptInfo> result =
        crossDevicePromptManager.requestInstallationPromptFlow(request);

    result.addOnSuccessListener(crossDevicePromptInfo -> {
        // Requested a prompt flow successfully
    });

    result.addOnFailureListener(e -> {
        // Failed to request a prompt flow
    });

| **Important:** If an error occurs during the in-app install prompt flow, don't inform the user or change your app's normal flow. Continue your app's normal flow after `onComplete` is called.

To verify your implementation, see [Test in-app install prompts](https://developer.android.com/guide/playcore/install-prompt/test).