---
title: https://developer.android.com/develop/ui/views/layout/webapps/jetpack-webkit-overview
url: https://developer.android.com/develop/ui/views/layout/webapps/jetpack-webkit-overview
source: md.txt
---

This guide describes the benefits of the Jetpack Webkit library, explains how it
works, and how you can implement it in your projects.

## Overview

WebViews are an essential part of Android development, but they can sometimes be
challenging to manage due to inconsistencies in features across different
Android OS versions. Each Android OS version provides a fixed set of WebView
APIs. Because Android ships at a slower cadence than WebView, Android APIs might
not cover every available WebView feature. This leads to slower feature rollout
and increased testing costs.

Jetpack Webkit solves these problem by acting as a compatibility layer and
leveraging the up-to-date WebView APK on the user's device. It also contains new
and modern APIs that are exclusively available in this library.

## Why use Jetpack Webkit?

In addition to offering cross-version compatibility, Jetpack Webkit also offers
new and modern APIs that can simplify development and improve your app's
functionality:

- **Enables modern authentication** : WebView can seamlessly handle modern web
  authentication standards like [WebAuthn](https://webauthn.guide), enabling passkey-based sign-ins.
  The `androidx.webkit` library gives you full control over this integration
  using the [`WebSettingsCompat.setWebAuthenticationSupport()`](https://developer.android.com/reference/androidx/webkit/WebSettingsCompat#setWebAuthenticationSupport(android.webkit.WebSettings,int)) method, which
  you can use to configure the level of support your app requires.

- **Improves performance** : Fine-tune WebView's performance for your app's use
  cases using APIs such as [`prefetchUrlAsync`](https://developer.android.com/reference/androidx/webkit/Profile#prefetchUrlAsync(java.lang.String,android.os.CancellationSignal,java.util.concurrent.Executor,androidx.core.os.OutcomeReceiverCompat%3Cjava.lang.Void,androidx.webkit.PrefetchException%3E)), [`prerenderUrlAsync`](https://developer.android.com/reference/androidx/webkit/WebViewCompat#prerenderUrlAsync(android.webkit.WebView,java.lang.String,android.os.CancellationSignal,java.util.concurrent.Executor,androidx.webkit.PrerenderOperationCallback)),
  and the [`setBackForwardCacheEnabled`](https://developer.android.com/reference/androidx/webkit/WebSettingsCompat#setBackForwardCacheEnabled(android.webkit.WebSettings,boolean)).

- **Increases stability** : Recover stalled or unresponsive renderer processes
  without crashing. For more information, see
  [`WebViewRenderProcess#terminate()`](https://developer.android.com/reference/androidx/webkit/WebViewRenderProcess#terminate()).

- **Offers granular control over browsing data** : To delete browsing data stored
  by WebView for specific origins, use the [`WebStorageCompat`](https://developer.android.com/reference/kotlin/androidx/webkit/WebStorageCompat) class.

## Understand the components

To use Jetpack Webkit effectively, you must understand the relationship between
the following components:

- **Android System WebView**: This is the Chromium-based rendering engine that
  Google updates regularly through the Google Play Store at the same cadence as
  Chrome. It contains the most up-to-date features and provides the underlying
  implementation code for all WebView APIs.

- **Framework APIs (`android.webkit`)** : These are the APIs that are fixed to a
  specific Android OS version. For example, an app on Android 10 can only access
  the APIs that were available when that version was released. So, it can't use
  new features added to the WebView APK in more recent updates. For example, to
  get a handle on an unresponsive renderer with
  [`WebView#getWebViewRenderProcess()`](https://developer.android.com/reference/android/webkit/WebView#getWebViewRenderProcess()), you can only call this on Android 10
  and higher.

- **Jetpack Webkit Library (`androidx.webkit`)** : This is a small library
  bundled in your application. This library acts as a bridge that calls into the
  WebView APK, rather than calling into the APIs defined in the Android
  platform, which has a fixed OS version. This way, even when an application is
  installed on a device running an older OS version like Android 10, the
  application can use the latest WebView features. For example,
  [`WebViewCompat.getWebViewRenderProcess()`](https://developer.android.com/reference/androidx/webkit/WebViewCompat#getWebViewRenderProcess(android.webkit.WebView)) works similar to the Framework
  API, except this can also be called on all OS versions before Android 10.

If an API is available in both the framework and Jetpack Webkit, we recommend
that you choose the Jetpack Webkit version. This helps ensure consistent
behavior and compatibility across the widest range of devices.

## Jetpack Webkit and APK interaction

The APIs in Jetpack Webkit are implemented in two parts:

- **Static Jetpack Webkit**: The static Jetpack Webkit library contains
  a minority of the code responsible for implementing the API.

- **WebView APK**: The WebView APK contains most of the code.

Your app calls the Jetpack Webkit API, which then calls the WebView APK.

While you control the Jetpack Webkit version in your app, you can't control the
WebView APK updates on users' devices. Generally, most users have up-to-date
versions of the WebView APK, but your app must still be cautious to not call
into APIs that that particular version of the WebView APK doesn't support.

Jetpack Webkit also abstracts away the need to check WebView versions manually.
To determine if a feature is available, check for its feature constant. For
example, [`WebViewFeature.WEB_AUTHENTICATION`](https://developer.android.com/reference/androidx/webkit/WebViewFeature#WEB_AUTHENTICATION()).

## How they work together

Jetpack Webkit bridges the gap between the static Framework API and the
frequently updated WebView APK. When you use the Jetpack Webkit API with the
feature-detection pattern, the library performs a check to see if the feature is
supported by the WebView APK installed on the user's device. This provides the
benefit of not needing to check the Android OS (framework) version.

If the WebView APK is a recent enough version, the library invokes the feature.
If not, it reports that the feature is unavailable, preventing your app from
crashing and enabling you to handle the situation gracefully.

## Compare Jetpack Webkit and Framework APIs

This section compares implementation methods with and without the Jetpack Webkit
library:

### Enable modern authentication (WebAuthn)

**Without Jetpack Webkit**

Not possible through framework APIs.

**With Jetpack Webkit**

Leverages `WebViewFeature.WEB_AUTHENTICATION` for compatibility checks.

    if (WebViewFeature.isFeatureSupported(WebViewFeature.WEB_AUTHENTICATION)) {
      WebSettingsCompat.setWebAuthenticationSupport(
          webView.settings,
          WebSettingsCompat.WEB_AUTHENTICATION_SUPPORT_FOR_APP
      )
    }

### Delete data for an origin (site-specific storage)

**Without Jetpack WebKit**

No direct API to clear specific origin data. Often requires clearing all data.

**With Jetpack WebKit**

Uses compatibility APIs for precise data deletion. You can use either of the
following options:

    WebStorageCompat.getInstance().deleteBrowsingData()

Or

    WebStorageCompat.getInstance().deleteBrowsingDataForSite()

### Get WebView version

**Without Jetpack WebKit**

Uses the standard framework class.

    val webViewPackage = WebView.getCurrentWebViewPackage()

**With Jetpack WebKit**

Uses the compatibility layer for safer retrieval.

    val webViewPackage = WebViewCompat.getCurrentWebViewPackage()

### Handle unresponsive renderer (renderer client)

**Without Jetpack WebKit**

Uses the standard framework method.

    webView.setWebViewRenderProcessClient(myClient)

**With Jetpack WebKit**

Uses WebViewCompat and a feature check for setting the client.

    if (WebViewFeature.isFeatureSupported(WebViewFeature.WEB_VIEW_RENDERER_CLIENT_BASIC_USAGE)) {
      WebViewCompat.setWebViewRenderProcessClient(webView, myClient)
    }

For more information, see [`androidx.webkit` reference documentation](https://developer.android.com/reference/kotlin/androidx/webkit/package-summary).

## Integrate Jetpack Webkit into your code

Using Jetpack Webkit augments the capabilities of the standard WebView class,
but it doesn't entirely replace the original WebView class.

You can continue to use the [`android.webkit.WebView`](https://developer.android.com/reference/android/webkit/WebView) class. You can add
it to your XML layouts, and get a reference to the instance in your code. To
access standard framework features, you can still call methods directly on the
WebView instance or its settings object.

To access modern features, you use the static helper methods provided by
Jetpack Webkit, such as `WebViewCompat` and `WebSettingsCompat`. You
pass your existing WebView instance to these methods.

### Kotlin

    import android.webkit.WebView
    import androidx.webkit.WebSettingsCompat
    import androidx.webkit.WebViewFeature

    // You still get your WebView instance the standard way.
    val webView: WebView = findViewById(R.id.my_webview)

    // To enable a modern feature, you pass that instance to a Jetpack Webkit helper.
    if (WebViewFeature.isFeatureSupported(WebViewFeature.FORCE_DARK)) {
        WebSettingsCompat.setForceDark(webView.settings, WebSettingsCompat.FORCE_DARK_ON)
    }

### Java

    import android.webkit.WebView;
    import androidx.webkit.WebSettingsCompat;
    import androidx.webkit.WebViewFeature;

    // You still get your WebView instance the standard way.
    WebView webView = findViewById(R.id.my_webview);

    // To enable a modern feature, you pass that instance to a Jetpack Webkit helper.
    if (WebViewFeature.isFeatureSupported(WebViewFeature.FORCE_DARK)) {
        WebSettingsCompat.setForceDark(webView.settings, WebSettingsCompat.FORCE_DARK_ON);
    }

## Implement Jetpack Webkit

To implement Jetpack Webkit, use the following procedure.

**Step 1: Add the dependency**

In your module's `build.gradle.kts` or `build.gradle` file, include the
following dependency to add Jetpack Webkit:

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

Jetpack Webkit contains thin wrappers, so the impact on your application's size
is minimal.

**Step 2: Adopt the feature-detection pattern**

To prevent crashes when invoking unavailable APIs, use feature checks. We
recommend surrounding each API invocation with a feature check, and possibly
considering fallback logic for when the API is unavailable.

We recommend the following pattern for using a modern WebView API:

### Kotlin

    import android.webkit.WebView
    import androidx.webkit.WebSettingsCompat
    import androidx.webkit.WebViewFeature

    val webView: WebView = findViewById(R.id.my_webview)

    // Before you use a modern API, first check if it is supported.
    if (WebViewFeature.isFeatureSupported(WebViewFeature.FORCE_DARK)) {
        // If the check passes, it is safe to call the API.
        WebSettingsCompat.setForceDark(webView.settings, WebSettingsCompat.FORCE_DARK_ON)
    } else {
        // Optionally, provide a fallback for older WebView versions.
    }

### Java

    import android.webkit.WebView;
    import androidx.webkit.WebSettingsCompat;
    import androidx.webkit.WebViewFeature;

    WebView webView = findViewById(R.id.my_webview);

    // Before you use a modern API, first check if it is supported.
    if (WebViewFeature.isFeatureSupported(WebViewFeature.FORCE_DARK)) {
        // If the check passes, it is safe to call the API.
        WebSettingsCompat.setForceDark(webView.getSettings(), WebSettingsCompat.FORCE_DARK_ON);
    } else {
        // Optionally, provide a fallback for older WebView versions.
    }

This pattern helps ensure the application is robust. Because the feature check
runs first, the application doesn't crash if the feature isn't available. The
performance overhead of the [`WebViewFeature#isFeatureSupported()`](https://developer.android.com/reference/androidx/webkit/WebViewFeature#isFeatureSupported(java.lang.String)) check is
negligible.