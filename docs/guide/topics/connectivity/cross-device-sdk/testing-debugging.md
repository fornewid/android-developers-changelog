---
title: https://developer.android.com/guide/topics/connectivity/cross-device-sdk/testing-debugging
url: https://developer.android.com/guide/topics/connectivity/cross-device-sdk/testing-debugging
source: md.txt
---

## Preconditions

The Developer Preview isn't intended for use in production applications. Hence, it requires using a beta version of Google Play Services. See [this guide on how to enroll in the Beta Program](https://developers.google.com/android/guides/beta-program).

To run and test multidevice experiences, you must have at least two Android
devices (for example, a phone and a tablet). The devices must:

- Have Google Play Services Beta installed
- Use the same primary Google Account
- Have [Quick Share enabled](https://support.google.com/android/answer/9286773) and be visible to nearby devices
- Be in close proximity of each other

## Deploy your apps

### Deploy through Android Studio

When deploying through Android Studio, complete the following steps:

1. Open the Android Studio project for your app.
2. Go to **Run \> Edit Configurations** . The **Run/Debug Configuration** window appears.
3. Under **Launch Options** , set **Launch** to your app main or multidevice activity.
4. Click **Apply** , and then **OK**.
5. Click **Run** to install the app on your test device.

### Deploy using the command line

When deploying using the command line, repeat the steps for all devices used in
testing the multidevice experience. This section assumes that the name of your
app module is `crossdevice-app`.

    ./gradlew crossdevice-app:installDebug
    # Start the app's activity. This example uses the sample app.
    adb shell am start -n \
      com.example.dtdi/com.example.crossdevice.MainActivity

## Tips for Debugging

To debug the app, click the **Debug** button in Android Studio.

Given the asynchronous and distributed nature of multidevice experiences, it
might be difficult to rely only on debugging. Take advantage
of logging and analytics. The Cross device SDK is designed to provide callbacks
for both successful and failed operations, so it's important to handle those
callbacks and log outputs for easier debugging.

If your transfer failed and you can't initiate device discovery or a new session, you can try turning Airplane Mode ON and OFF to quickly reset the quick share state.

## Share your feedback

Your feedback is a crucial part of the Cross device SDK Developer Preview! Let us know of [any issues](https://issuetracker.google.com/issues/new?component=1205991&template=1706309) you find or ideas for improving the Cross device SDK on Android.