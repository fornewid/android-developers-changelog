---
title: https://developer.android.com/guide/playcore/in-app-review/unity
url: https://developer.android.com/guide/playcore/in-app-review/unity
source: md.txt
---

# Integrate in-app reviews (Unity)

This guide describes how to integrate in-app reviews in your app using Unity. There are separate integration guides for if you are using[Kotlin or Java](https://developer.android.com/guide/playcore/in-app-review/kotlin-java),[native code](https://developer.android.com/guide/playcore/in-app-review/native)or[Unreal Engine](https://developer.android.com/guide/playcore/in-app-review/unreal-engine).

## Unity SDK overview

The Play In-App Review API is part of[Play Core SDK](https://developer.android.com/reference/com/google/android/play/core/release-notes)family. The API for Unity offers a[`ReviewManager`](https://developer.android.com/reference/unity/class/Google/Play/Review/ReviewManager)class to request and launch the flow using the[`RequestReviewFlow`](https://developer.android.com/reference/unity/class/Google/Play/Review/ReviewManager#requestreviewflow)and[`LaunchReviewFlow`](https://developer.android.com/reference/unity/class/Google/Play/Review/ReviewManager#launchreviewflow)methods. After a request is made, your app can check the status of the request using[`ReviewErrorCode`](https://developer.android.com/reference/unity/namespace/Google/Play/Review#reviewerrorcode).

## Set up your development environment

### OpenUPM-CLI

If you have the[OpenUPM CLI](https://github.com/openupm/openupm-cli#installation)installed you can install the OpenUPM registry with the following command:  

    openupm add com.google.play.review

### OpenUPM

1. Open the[package manager settings](https://docs.unity3d.com/Manual/class-PackageManager.html)by selecting the Unity menu option**Edit \> Project Settings \> Package Manager**.

2. Add OpenUPM as a scoped registry to the Package Manager window:

       Name: package.openupm.com
       URL: https://package.openupm.com
       Scopes: com.google.external-dependency-manager
         com.google.play.common
         com.google.play.core
         com.google.play.review

3. Open the[package manager menu](https://docs.unity3d.com/Manual/upm-ui-install.html)by selecting the Unity menu option**Window \> Package Manager**.

4. Set the manager scope drop-down to select**My Registries**.

5. Select the**Google Play Integrity plugin for Unity** package from the package list and press**Install**.

### Import from GitHub

1. Download the latest[`.unitypackage`](https://github.com/google/play-in-app-reviews-unity/releases/latest)release from GitHub.

2. Import the`.unitypackage`file by selecting the Unity menu option**Assets \> Import package \> Custom Package**and importing all items.

| **Note:** By downloading and using Google Play Unity Plugins, you agree to the[Play Core Software Development Kit Terms of Service](https://developer.android.com/guide/playcore#license).

## Create the ReviewManager

Create an instance of[`ReviewManager`](https://developer.android.com/reference/unity/class/Google/Play/Review/ReviewManager)that handles communication between your app and the Google Play API.  

    using Google.Play.Review;

    // Create instance of ReviewManager
    private ReviewManager _reviewManager;
    // ...
    _reviewManager = new ReviewManager();

## Request a ReviewInfo object

Follow the guidance about[when to request in-app reviews](https://developer.android.com/guide/playcore/in-app-review#when-to-request)to determine good points in your app's user flow to prompt the user for a review (for example, after a user dismisses the summary screen at the end of a level in a game). When your app gets close one of these points, use the[`ReviewManager`](https://developer.android.com/reference/unity/class/Google/Play/Review/ReviewManager)instance to create an async operation, as shown in the following example:  

    var requestFlowOperation = _reviewManager.RequestReviewFlow();
    yield return requestFlowOperation;
    if (requestFlowOperation.Error != ReviewErrorCode.NoError)
    {
        // Log error. For example, using requestFlowOperation.Error.ToString().
        yield break;
    }
    _playReviewInfo = requestFlowOperation.GetResult();

If the call is successful, the API returns the[`PlayReviewInfo`](https://developer.android.com/reference/unity/class/Google/Play/Review/PlayReviewInfo)object that your app needs to launch the in-app review flow. In the example, the call is made inside a[coroutine](https://docs.unity3d.com/Manual/Coroutines.html)to perform the async operation (this does not block the Main thread). Because the call is made asynchronously, it might take up to a couple of seconds, so your app should make the call before your app reaches the point in your user flow where you want to show the in-app review.

## Launch the in-app review flow

After your app receives the[`PlayReviewInfo`](https://developer.android.com/reference/unity/class/Google/Play/Review/PlayReviewInfo)instance, it can launch the in-app review flow. Note that the`PlayReviewInfo`object is only valid for a limited amount of time, so your app should not wait too long before launching a flow.  

    var launchFlowOperation = _reviewManager.LaunchReviewFlow(_playReviewInfo);
    yield return launchFlowOperation;
    _playReviewInfo = null; // Reset the object
    if (launchFlowOperation.Error != ReviewErrorCode.NoError)
    {
        // Log error. For example, using launchFlowOperation.Error.ToString().
        yield break;
    }
    // The flow has finished. The API does not indicate whether the user
    // reviewed or not, or even whether the review dialog was shown. Thus, no
    // matter the result, we continue our app flow.

## Next steps

[Test your app's in-app review flow](https://developer.android.com/guide/playcore/in-app-review/test)to verify that your integration is working correctly.