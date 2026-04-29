---
title: https://developer.android.com/training/cars/parked/browser
url: https://developer.android.com/training/cars/parked/browser
source: md.txt
---

The Browsers category is in beta At this time, anyone can publish browsers to internal testing tracks on the Play Store. Publishing to closed testing, open testing, and production tracks will be permitted at a later date. [Nominate yourself to be an early access partner →](https://forms.gle/VsXEdDEBidxw8q8u8) ![](https://developer.android.com/static/images/picto-icons/test-tube-2.svg)

Beyond the requirements described in [Build parked apps for cars](https://developer.android.com/training/cars/parked) and
[Add support for Android Automotive OS to your parked app](https://developer.android.com/training/cars/parked/automotive-os),
there are a few additional requirements specific to browsers that are detailed
on this page.

> [!IMPORTANT]
> **Important:** Make sure your app meets the [quality guidelines for
> browsers](https://developer.android.com/docs/quality-guidelines/car-app-quality?category=browser), as it is reviewed against them when submitted to tracks other than internal testing.

## Mark your app as a browser

To indicate that your app is a browser, it must include an intent filter such as
the following within an exported `<activity>` element:

    <activity ...
        android:exported="true">
      ...
      <intent-filter>
        <action android:name="android.intent.action.MAIN"/>
       ...
        <category android:name="android.intent.category.APP_BROWSER"/>
      </intent-filter>
    </activity>

For more information, see
[`android.intent.category.APP_BROWSER`](https://developer.android.com/reference/android/content/Intent#CATEGORY_APP_BROWSER).

## Allow users to block access to sensitive data

Unlike many Android devices, Android Automotive OS vehicles are often shared
devices. To give users the ability to protect their sensitive data such as
passwords and payments information, browsers built for Android Automotive OS
[must not save or allow access to passwords or payment information unless the
user can block access to passwords using a profile lock](https://developer.android.com/docs/quality-guidelines/car-app-quality?category=browser#SD-1).
Authentication can be accomplished either by using the device credential or by
building an authentication system within your app.

Additionally, before syncing sensitive data, browsers built for Android
Automotive OS [must prompt the user to authenticate and provide messaging to let
the user know that their data is being synchronized to the car](https://developer.android.com/docs/quality-guidelines/car-app-quality?category=browser#SD-2).
If the user does not have any method of authentication set up, you can prompt
them to set one up when they try to sync sensitive data, using either the
[device credential](https://developer.android.com/training/cars/parked/browser#open-settings) or one specific to your app.

## Use the device credential for authentication

This section provides guidance on how to use the device credential and
system authentication APIs to meet the sensitive data requirements described
prior.

### Check if there is a device credential set

To determine if the user has secured their device with a PIN, pattern, or
password, you can use the [`KeyguardManager::isDeviceSecure`](https://developer.android.com/reference/android/app/KeyguardManager#isDeviceSecure())
method.


```kotlin
val keyguardManager = context.getSystemService<KeyguardManager>()
val isDeviceSecure = keyguardManager?.isDeviceSecure == truehttps://github.com/android/snippets/blob/4fe2def8df52a175e66e770f90d72528db7d4c9a/cars/src/main/java/com/example/cars/parked/Browser.kt#L27-L28
```

<br />

### Open the lock screen settings

To reduce user friction in the case they need to set a device credential, you
can open up the Security screen within the Settings app using the
[`Settings.ACTION_SECURITY_SETTINGS`](https://developer.android.com/reference/android/provider/Settings#ACTION_SECURITY_SETTINGS)
intent action.


```kotlin
context.startActivity(
    Intent(Settings.ACTION_SECURITY_SETTINGS)
        .addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
)
```

<br />

### Prompt the user to authenticate

To prompt the user to authenticate, you can use the `BiometricPrompt` API as
described in [Show a biometric authentication dialog](https://developer.android.com/training/sign-in/biometric-auth).

> [!CAUTION]
> **Caution:** Despite the name, you should only use the [`DEVICE_CREDENTIAL`](https://developer.android.com/reference/androidx/biometric/BiometricManager.Authenticators#DEVICE_CREDENTIAL) authenticator and not any of the biometric ones, as Android Automotive OS vehicles with Google built-in don't have biometric sensors.