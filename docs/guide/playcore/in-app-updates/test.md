---
title: https://developer.android.com/guide/playcore/in-app-updates/test
url: https://developer.android.com/guide/playcore/in-app-updates/test
source: md.txt
---

# Test in-app updates

This guide describes how to test[in-app updates](https://developer.android.com/guide/playcore/in-app-updates)in your app.

## Test with internal app sharing

Use[internal app sharing](https://support.google.com/googleplay/android-developer/answer/9844679)to test in-app updates by performing the following steps:

1. Make sure your test device has a version of your app installed that supports in-app updates and was installed using an internal app sharing URL.

2. Follow the Play Console instructions to[share your app internally](https://support.google.com/googleplay/android-developer/answer/9844679). Upload a version of your app that uses a version code that is higher than the one you already have installed on the test device.

3. On the test device, click the internal app sharing link for the updated version of your app but*do not*install the app from the Play Store page that appears after you click the link.

4. Open the app from the device's app drawer or home screen. The update should now be available to your app, and you can test your implementation of in-app updates.

## Troubleshoot

This section describes some possible solutions to situations where in-app updates might not work as expected during testing:

- In-app updates are only available to user accounts that own the app. Make sure the account that you're using has downloaded your app from Google Play at least once before using the account to test in-app updates.

- Make sure that the app that you are using to test in-app updates has the same[application ID](https://developer.android.com/studio/build/configure-app-module#set_the_application_id)and[signing key](https://developer.android.com/studio/publish/app-signing)as the version available from Google Play.

- Google Play can only update an app to a higher version code. Make sure that the app that you are testing has a lower version code than the update version code.

- The`inAppUpdatePriority`field is not supported when uploading your app to internal app sharing.