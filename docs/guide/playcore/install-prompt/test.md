---
title: https://developer.android.com/guide/playcore/install-prompt/test
url: https://developer.android.com/guide/playcore/install-prompt/test
source: md.txt
---

This guide explains how to test your integration of in-app install prompts in
your app or game.

## Test the API

To test the API, follow these steps:

1. Verify that the test account owner has one or more alternate form factor devices, for example, a watch, phone, tablet, foldable, TV, or Android Automotive OS vehicle.
2. Verify that the test account is signed in to the Play Store on the other form factors.
3. Verify that the test account is running Play Store version 42.2 or higher on a phone.

## Test using the Google Play Store

In-app install prompts require your app to be published in the Play Store. You
can test your integration without publishing your app to production by using
internal test tracks or internal app sharing. This section describes both
methods.

### Test using an internal test track

Upload your app to the internal test track. Then, install it on a device with a
user account that has access to the internal test track. When doing so, confirm
that these conditions are met:

1. The user account is part of the internal test track.
2. The user account is the primary account and is selected in the Play Store.
3. The user account has downloaded the app from the Play Store. The app is listed in the user's Google Play library.
4. The user account has not installed the app on all eligible devices.

After the account on the device downloads the app at least once from the
internal test track and is part of the testers list, you can deploy new app
versions locally to that device, for example, using Android Studio.

### Test using internal app sharing

For rapid iteration, you can use [internal app sharing](https://play.google.com/console/internal-app-sharing/) to
test your integration. This method lets you test changes quickly by skipping
some verification that occurs with other test tracks.

## Troubleshooting

The following table describes common issues that can prevent the in-app install
prompt dialog from displaying in your app:

| Issue | Solution |
|---|---|
| Your app is not published in the Play Store. | Your app doesn't have to be published to test. However, your app's [`applicationId`](https://developer.android.com/build/configure-app-module#set-application-id) must be available in at least the internal test track. |
| The in-app install prompt does not appear. | Confirm that the \[eligibility\](.#eligibility) and \[testing criteria\](.#test) are met. |
| The user's account is not eligible to install the app. | The user has already installed the app on all eligible devices. Uninstall the app from eligible devices. |
| The primary account is not selected in the Play Store. | When multiple accounts are available on the device, verify that the primary account is selected in the Play Store. |
| The user's account is protected, for example, with enterprise accounts. | Use a Gmail account instead. |
| The quota has been reached. | Use an [internal test track](https://developer.android.com/guide/playcore/install-prompt/test#internal-test-track) or [internal app sharing](https://developer.android.com/guide/playcore/install-prompt/test#internal-app-sharing). |
| There is an issue with the Google Play Store or Google Play services on the device. | This commonly occurs when the Play Store was sideloaded onto the device. Use a different device that has a valid version of the Play Store and Google Play services. |