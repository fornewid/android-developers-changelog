---
title: https://developer.android.com/develop/ui/views/layout/webapps/webview-testing
url: https://developer.android.com/develop/ui/views/layout/webapps/webview-testing
source: md.txt
---

The WebView Beta program gives you early access to new releases of Android
WebView. We encourage all developers using WebView in their apps to join the
Beta program so you can try out new WebView versions 4 weeks before they're
released to the public.

> [!CAUTION]
> **Caution:** Beta releases may be less stable than the main release track. Beta users are the first to try out new features, but may also experience more crashes and some apps may not work properly.

## How do I subscribe to the Beta program?

You can subscribe to WebView Beta on Android 10 and higher by joining the
[WebView testing program](https://play.google.com/apps/testing/com.google.android.webview) with the account you use on your device. You can do
this by clicking the **"Become a tester"** button:
![Become a tester](https://developer.android.com/static/develop/ui/views/layout/webapps/beta-become-a-tester.png) **Figure 1**: Become a tester.

You're now a Beta tester for WebView! If you visit the Play Store on your
device, you should now see an update available for the Beta track. Install this
update to start using WebView Beta.

## How do I unsubscribe from the Beta program?

To leave the [WebView testing program](https://play.google.com/apps/testing/com.google.android.webview) and unsubscribe from receiving Beta
updates in the future, click the **"Leave the program"** button.

After you unsubscribe, WebView Beta is still installed on your device, but it
automatically updates to the main (Stable) track as soon as the next Stable
release comes out.

> [!CAUTION]
> **Caution:** If you don't want to wait for the next Stable release, you can uninstall WebView updates to immediately get back to Stable. However, we don't recommend doing this, because uninstalling WebView updates may delete user data if apps on your device use WebView to store data.

## Other ways to test WebView

- Did you know WebView also has other testing tracks? For a more bleeding edge experience, try out the [Dev or Canary channels](https://chromium.googlesource.com/chromium/src/+/HEAD/android_webview/docs/prerelease.md#trichrome-dev).
- If you want to try out experimental features or report crashes back to Google, you can install the separate [WebView Beta package](https://play.google.com/store/apps/details?id=com.google.android.webview.beta) instead.

## Webview DevTools

WebView DevTools are a set of on-device tools to help debug your WebView apps.

The best way to launch WebView DevTools is to download WebView Beta, Dev, or
Canary. These channels contain a launcher icon which launches WebView DevTools.
![You can debug your WebView apps with WebView DevTools.](https://developer.android.com/static/develop/ui/views/layout/webapps/devtools.png) **Figure 2**: WebView DevTools.

### Webview Crashes

Within the WebView Beta, Dev, and Canary apps, you can view WebView crashes that
have occurred on the device.

- Similar to `chrome://crashes`.
- Crashes from all apps on the device.
- File a bug to provide more info.

### Webview Flags

Similarly, the testing apps contain a series of [flags](https://developer.android.com/guide/webapps/debugging#Testing) you may use to
enable/disable experimental features.

## Using WebView on older versions of Android

Jetpack's [androidx.webkit](https://developer.android.com/jetpack/androidx/releases/webkit) enables you to use WebView APIs on older versions
of Android that would otherwise not support them. There are several benefits to
Jetpack Webkit:

- It is a Jetpack library updated regularly.
- It is easy to use by design,
- It enables your WebView apps to work on more devices.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    implementation "androidx.webkit:webkit:1.15.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.webkit:webkit:1.15.0")
}
```

## Developer resources

The following are additional resource for developers.

### Video

- [Jetpack Webkit](https://www.youtube.com/watch?v=7Wq8Lwt_Cbg)
- [Modern WebView best practices - Android Dev Summit '18](https://www.youtube.com/watch?v=HGZYtDZhOEQ)

### Documentation

- [Web-based content](https://developer.android.com/guide/webapps)
- [Espresso Web](https://developer.android.com/training/testing/espresso/web)
- [Bug template for reporting issues](https://issues.chromium.org/issues/new?component=1456456&template=1923373)