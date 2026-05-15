---
title: https://developer.android.com/develop/better-together/continue-on/setup
url: https://developer.android.com/develop/better-together/continue-on/setup
source: md.txt
---

Because the Continue On feature and APIs are only available on Android 17 (API
level 37) which is currently in beta, you need to set up your devices and
development environment with the appropriate Android versions and SDK tools to
get started.

## Device setup

To test Continue On, obtain two Pixel devices (one mobile, one tablet) that are
[eligible](https://www.google.com/android/beta#faq) for the Android Beta, and do the following setup on both devices:

- Enroll the devices in the [Android Beta for Pixel program](https://www.google.com/android/beta). Learn more about [Android Beta for developers](https://developer.android.com/about/versions/16/qpr2/overview).
- Setup both devices with the same Google user account to use [cross-device
  services](https://support.google.com/android/answer/14997291).
- Enroll in the Cross-Device Services [public Beta](https://play.google.com/apps/testing/com.google.android.ambient.streaming) in Play and install the latest version.
- Enroll in the Google system services [public Beta](https://play.google.com/apps/testing/com.google.android.gms) in Play and install the latest version. Learn more about the [Google system services public beta
  program](https://developers.google.com/android/guides/beta-program).
- Network requirements
  - Bluetooth is on
  - Both devices are on the same wifi network
- Set up cross-device services:
  - Open the Settings app.
  - Go to **Connected devices \> Connection preferences \> Cross-device
    services \> Continue activity**
  - Click **Set up** and allow requested permissions.
  - Enable **Tasks**.

## Development setup

- Use the SDK Manager in Android Studio to download:
  - SDK and tools for the Beta release
  - (Optional) Emulator system images for mobile devices
- Implement and customize the Continue On feature for at least one activity in your app with the provided APIs
- Install this version of the app to both Pixel devices (See [Device
  setup](https://developer.android.com/develop/better-together/continue-on/setup#device).).

## Test

With your two Pixel devices (phone and tablet) properly set up, install your app
on both devices (or just the phone if you want to test the web handoff
functionality).

1. On the tablet, access [desktop windowing mode](https://support.google.com/android/answer/16928875).
2. On the phone, launch your app and navigate to the activity that has enabled the Continue On feature.
3. Back on the tablet device, you should see in the bottom taskbar in the right-most spot, your app icon shows up with the Continue On suggestion badging treatment. Tap on it.
4. Your app should launch to the activity you requested handoff to in your implementation.