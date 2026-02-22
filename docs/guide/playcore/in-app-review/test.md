---
title: https://developer.android.com/guide/playcore/in-app-review/test
url: https://developer.android.com/guide/playcore/in-app-review/test
source: md.txt
---

# Test in-app reviews

Follow the steps in this guide to test your integration of in-app reviews in your app or game.

## Test using the Google Play Store

In-app reviews require your app to be published in Play Store. However, you can test your integration without publishing your app to production using either internal test tracks or internal app sharing. Both methods are described in this section.

### Test using an internal test track

Upload your app to the internal test track and install it on a device with a user account that has access to the internal test track. When using an internal test track, the following conditions must be met:

1. The user account is part of the Internal Test Track.
2. The user account is the primary account and it's selected in the Play Store.
3. The user account has downloaded the app from the Play Store (the app is listed in the user's Google Play library).
4. The user account does not currently have a review for the app.

After the account on the device has downloaded the app at least once from the internal test track and is part of the testers list, you can deploy new versions of the app locally to that device (for example, using Android Studio).
| **Note:** The quota limits are**not**enforced if the app is downloaded from the internal test track.

### Test using internal app sharing

Alternatively, for rapid iteration you can use[internal app sharing](https://play.google.com/console/internal-app-sharing/)to test your integration. This method lets you quickly test changes by skipping some of the verification that happens with other test tracks.
| **Important:** When using an app installed with internal app sharing, reviews**can't be submitted**. To emphasize this difference, the button is disabled in the UI.

## Test using FakeReviewManager

The in-app review artifact contains a`FakeReviewManager`implementation that allows you to fake the behavior of the API.

This should only be used for unit or integration tests to verify the behaviour of the app once the review is completed. To use the`FakeReviewManager`, replace the`ReviewManager`instance with an instance of`FakeReviewManager`, as shown in the following example:  

### Kotlin

```kotlin
val manager = FakeReviewManager(context)
```

### Java

```java
ReviewManager manager = new FakeReviewManager(context);
```
| **Note:** `FakeReviewManager`does not simulate the UI. It only fakes the API method result by always providing a fake`ReviewInfo`object and returning a success status when the in-app review flow is launched.

## Troubleshooting

As you integrate and test in-app reviews, you might run into some issues. The following table outlines the most common issues that can prevent the in-app review dialog from displaying in your app:

|                                        Issue                                        |                                                                                                            Solution                                                                                                             |
|-------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Your app is not published yet in the Play Store.                                    | Your app doesn't have to be published to test, but your app's`applicationID`must be available at least in the internal testing track.                                                                                           |
| The user account can't review the app.                                              | Your app must be in the user's Google Play library. To add your app to the user's library, download your app from the Play Store using that user's account.                                                                     |
| The primary account is not selected in the Play Store.                              | When multiple accounts are available in the device, ensure that the primary account is the one selected in the Play Store.                                                                                                      |
| The user account is protected (for example, with enterprise accounts).              | Use a Gmail account instead.                                                                                                                                                                                                    |
| The user has already reviewed the app.                                              | Delete the review directly from Play Store.                                                                                                                                                                                     |
| The quota has been reached.                                                         | Use an[internal test track](https://developer.android.com/guide/playcore/in-app-review/test#internal-test-track)or[internal app sharing](https://developer.android.com/guide/playcore/in-app-review/test#internal-app-sharing). |
| There is an issue with the Google Play Store or Google Play Services on the device. | This commonly occurs when the Play Store was sideloaded onto the device. Use a different device that has a valid version of the Play Store and Google Play Services.                                                            |