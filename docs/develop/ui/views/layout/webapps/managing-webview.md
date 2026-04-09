---
title: https://developer.android.com/develop/ui/views/layout/webapps/managing-webview
url: https://developer.android.com/develop/ui/views/layout/webapps/managing-webview
source: md.txt
---

Android provides several APIs to help you manage the
`https://developer.android.com/reference/android/webkit/WebView`
objects that display web content in your app.

This page describes how to use these APIs to work with `WebView`
objects more effectively, improving your app's stability and security.

## Version API

Starting in Android 7.0 (API level 24), users can choose among several
different packages for displaying web content in a `WebView` object.
The [AndroidX.webkit](https://developer.android.com/reference/androidx/webkit/package-summary)
library includes the
`https://developer.android.com/reference/androidx/webkit/WebViewCompat#getCurrentWebViewPackage(android.content.Context)`
method for fetching information related to the package that is displaying web
content in your app. This method is useful when analyzing errors that occur only
when your app tries to display web content using a particular package's
implementation of `WebView`.

To use this method, add the logic shown in the following code snippet:

### Kotlin

```kotlin
val webViewPackageInfo = WebViewCompat.getCurrentWebViewPackage(appContext)
Log.d("MY_APP_TAG", "WebView version: ${webViewPackageInfo.versionName}")
```

### Java

```java
PackageInfo webViewPackageInfo = WebViewCompat.getCurrentWebViewPackage(appContext);
Log.d("MY_APP_TAG", "WebView version: " + webViewPackageInfo.versionName);
```
| **Note:** The `getCurrentWebViewPackage()` method can return `null` if the device is set up incorrectly; doesn't support using `WebView`, such as a Wear OS device; or lacks an updatable `WebView` implementation.

## Google Safe Browsing Service

To provide your users with a safer browsing experience, `WebView`
objects verify URLs using
[Google Safe Browsing](https://developers.google.com/safe-browsing/),
which lets your app show users a warning when they try to navigate to a
potentially unsafe website.

Although the default value of `EnableSafeBrowsing` is true, there
are cases when you might want to only enable Safe Browsing conditionally or
disable it. Android 8.0 (API level 26) and later supports using
[`setSafeBrowsingEnabled()`](https://developer.android.com/reference/androidx/webkit/WebSettingsCompat#setSafeBrowsingEnabled(android.webkit.WebSettings,%20boolean))
to toggle Safe Browsing for an individual `WebView` object.

If you want all `WebView` objects to opt out of Safe Browsing
checks, add the following `<meta-data>` element to your app's
manifest file:
| **Note:** The safe browsing manifest opt out doesn't apply to `WebView` within the [SDK Runtime.](https://developer.android.com/design-for-safety/privacy-sandbox/sdk-runtime)

```xml
<manifest>
    <application>
        <meta-data android:name="android.webkit.WebView.EnableSafeBrowsing"
                   android:value="false" />
        ...
    </application>
</manifest>
```
| **Caution:** We recommend keeping Google Safe Browsing enabled at all times and designing your app around any constraints this causes.

### Define programmatic actions

When an instance of `WebView` attempts to load a page that is
classified by Google as a known threat, the `WebView` by default
shows an interstitial that warns users of the known threat. This screen gives
users the option to load the URL anyway or return to a previous page that's
safe.

If you target Android 8.1 (API level 27) or later, you can define
programmatically how your app responds to a known threat in the following
ways:

- You can control whether your app reports known threats to Safe Browsing.
- You can make your app automatically perform a particular action---such as going back to safety---each time it encounters a URL that's classified as a known threat.

| **Note:** For optimal protection against known threats, wait until you initialize Safe Browsing before you invoke a `WebView` object's `https://developer.android.com/reference/android/webkit/WebView#loadUrl(java.lang.String)` method.

The following code snippets show how to instruct your app's instances of
`WebView` to always go back to safety after encountering a known
threat:


MyWebActivity.java

### Kotlin

```kotlin
private lateinit var superSafeWebView: WebView
private var safeBrowsingIsInitialized: Boolean = false

// ...

override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)

    superSafeWebView = WebView(this)
    superSafeWebView.webViewClient = MyWebViewClient()
    safeBrowsingIsInitialized = false

    if (WebViewFeature.isFeatureSupported(WebViewFeature.START_SAFE_BROWSING)) {
        WebViewCompat.startSafeBrowsing(this, ValueCallback<Boolean> { success ->
            safeBrowsingIsInitialized = true
            if (!success) {
                Log.e("MY_APP_TAG", "Unable to initialize Safe Browsing!")
            }
        })
    }
}
```

### Java

```java
private WebView superSafeWebView;
private boolean safeBrowsingIsInitialized;

// ...

@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);

    superSafeWebView = new WebView(this);
    superSafeWebView.setWebViewClient(new MyWebViewClient());
    safeBrowsingIsInitialized = false;

    if (WebViewFeature.isFeatureSupported(WebViewFeature.START_SAFE_BROWSING)) {
        WebViewCompat.startSafeBrowsing(this, new ValueCallback<Boolean>() {
            @Override
            public void onReceiveValue(Boolean success) {
                safeBrowsingIsInitialized = true;
                if (!success) {
                    Log.e("MY_APP_TAG", "Unable to initialize Safe Browsing!");
                }
            }
        });
    }
}
```


MyWebViewClient.java

### Kotlin

```kotlin
class MyWebViewClient : WebViewClientCompat() {
    // Automatically go "back to safety" when attempting to load a website that
    // Google identifies as a known threat. An instance of WebView calls this
    // method only after Safe Browsing is initialized, so there's no conditional
    // logic needed here.
    override fun onSafeBrowsingHit(
            view: WebView,
            request: WebResourceRequest,
            threatType: Int,
            callback: SafeBrowsingResponseCompat
    ) {
        // The "true" argument indicates that your app reports incidents like
        // this one to Safe Browsing.
        if (WebViewFeature.isFeatureSupported(WebViewFeature.SAFE_BROWSING_RESPONSE_BACK_TO_SAFETY)) {
            callback.backToSafety(true)
            Toast.makeText(view.context, "Unsafe web page blocked.", Toast.LENGTH_LONG).show()
        }
    }
}
```

### Java

```java
public class MyWebViewClient extends WebViewClientCompat {
    // Automatically go "back to safety" when attempting to load a website that
    // Google identifies as a known threat. An instance of WebView calls this
    // method only after Safe Browsing is initialized, so there's no conditional
    // logic needed here.
    @Override
    public void onSafeBrowsingHit(WebView view, WebResourceRequest request,
            int threatType, SafeBrowsingResponseCompat callback) {
        // The "true" argument indicates that your app reports incidents like
        // this one to Safe Browsing.
        if (WebViewFeature.isFeatureSupported(WebViewFeature.SAFE_BROWSING_RESPONSE_BACK_TO_SAFETY)) {
            callback.backToSafety(true);
            Toast.makeText(view.getContext(), "Unsafe web page blocked.",
                    Toast.LENGTH_LONG).show();
        }
    }
}
```

## HTML5 Geolocation API

For apps targeting Android 6.0 (API level 23) and later, the Geolocation API
is only supported on secure origins, such as HTTPS. Any request to the
Geolocation API on non-secure origins is automatically denied without invoking
the corresponding `onGeolocationPermissionsShowPrompt()` method.

## Opt out of metrics collection

`WebView` has the ability to upload anonymous diagnostic data to
Google when the user gives their consent. Data is collected on a per-app basis
for each app that instantiates a `WebView`. You can opt out of this
feature by creating the following tag in the manifest's
`<application>` element:

```xml
<manifest>
    <application>
    ...
    <meta-data android:name="android.webkit.WebView.MetricsOptOut"
               android:value="true" />
    </application>
</manifest>
```

Data is only uploaded from an app if the user consents **and**
the app doesn't opt out. For more information on opting out of diagnostic data
reporting, see [User privacy in WebView
reporting](https://developer.android.com/develop/ui/views/layout/webapps/webview-privacy).

## Termination Handling API

The Termination Handling API handles cases where the renderer process for a
`WebView`
object goes away, either because the system kills the renderer to reclaim
necessary memory or because the renderer process crashes. By using this API, you
let your app continue executing, even though the renderer process goes away.
| **Caution:** If your app continues executing after the renderer process goes away, the associated instance of `WebView` can't be reused, even if the renderer process is killed or crashes. Your app must remove the instance from the view hierarchy and destroy the instance to continue executing. Your app must then create a new instance of `WebView` to continue rendering web pages.

If a renderer crashes while loading a particular web page, attempting to
load that same page again can cause a new `WebView` object to
exhibit the same rendering crash behavior.

The following code snippet illustrates how to use this API within an
`Activity`:

### Kotlin

```kotlin
    
inner class MyRendererTrackingWebViewClient : WebViewClient() {
    private var mWebView: WebView? = null

    override fun onRenderProcessGone(view: WebView, detail: RenderProcessGoneDetail): Boolean {
        if (!detail.didCrash()) {
            // Renderer is killed because the system ran out of memory. The app
            // can recover gracefully by creating a new WebView instance in the
            // foreground.
            Log.e("MY_APP_TAG", ("System killed the WebView rendering process " +
                "to reclaim memory. Recreating..."))

            mWebView?.also { webView ->
                val webViewContainer: ViewGroup = findViewById(R.id.my_web_view_container)
                webViewContainer.removeView(webView)
                webView.destroy()
                mWebView = null
            }

            // By this point, the instance variable "mWebView" is guaranteed to
            // be null, so it's safe to reinitialize it.

            return true // The app continues executing.
        }

        // Renderer crashes because of an internal error, such as a memory
        // access violation.
        Log.e("MY_APP_TAG", "The WebView rendering process crashed!")

        // In this example, the app itself crashes after detecting that the
        // renderer crashed. If you handle the crash more gracefully and let
        // your app continue executing, you must destroy the current WebView
        // instance, specify logic for how the app continues executing, and
        // return "true" instead.
        return false
    }
}
```

### Java

```java
public class MyRendererTrackingWebViewClient extends WebViewClient {
    private WebView mWebView;

    @Override
    public boolean onRenderProcessGone(WebView view,
            RenderProcessGoneDetail detail) {
        if (!detail.didCrash()) {
            // Renderer is killed because the system ran out of memory. The app
            // can recover gracefully by creating a new WebView instance in the
            // foreground.
            Log.e("MY_APP_TAG", "System killed the WebView rendering process " +
                    "to reclaim memory. Recreating...");

            if (mWebView != null) {
                ViewGroup webViewContainer =
                        (ViewGroup) findViewById(R.id.my_web_view_container);
                webViewContainer.removeView(mWebView);
                mWebView.destroy();
                mWebView = null;
            }

            // By this point, the instance variable "mWebView" is guaranteed to
            // be null, so it's safe to reinitialize it.

            return true; // The app continues executing.
        }

        // Renderer crashes because of an internal error, such as a memory
        // access violation.
        Log.e("MY_APP_TAG", "The WebView rendering process crashed!");

        // In this example, the app itself crashes after detecting that the
        // renderer crashed. If you handle the crash more gracefully and let
        // your app continue executing, you must destroy the current WebView
        // instance, specify logic for how the app continues executing, and
        // return "true" instead.
        return false;
    }
}
```

## Renderer Importance API

When `WebView` objects
[operate in
multiprocess mode](https://developer.android.com/about/versions/oreo/android-8.0-changes#security-all), you have some flexibility in how your app handles
out-of-memory situations. You can use the Renderer Importance API, introduced in
Android 8.0, to set a priority policy for the renderer assigned to a particular
`WebView` object. In particular, you might want the main part of your
app to continue executing when a renderer that displays your app's
`WebView` objects is killed. You might do this, for example, if you
expect to not show the `WebView` object for a long time so that the
system can reclaim memory that the renderer was using.

The following code snippet shows how to assign a priority to the renderer
process associated with your app's `WebView` objects:

### Kotlin

```kotlin
val myWebView: WebView = ...
myWebView.setRendererPriorityPolicy(RENDERER_PRIORITY_BOUND, true)
```

### Java

```java
WebView myWebView;
myWebView.setRendererPriorityPolicy(RENDERER_PRIORITY_BOUND, true);
```

In this particular snippet, the renderer's priority is the same as---or
is bound to---the default priority for the app. The `true`
argument decreases the renderer's priority to
`https://developer.android.com/reference/android/webkit/WebView#RENDERER_PRIORITY_WAIVED`
when the associated `WebView` object is no longer visible. In other
words, a `true` argument indicates that your app doesn't care whether
the system keeps the renderer process alive. In fact, this lower priority level
makes it likely that the renderer process is killed in out-of-memory
situations.
| **Warning:** To maintain app stability, don't change the renderer priority policy for a `WebView` object unless you also use the [Termination Handling API](https://developer.android.com/develop/ui/views/layout/webapps/managing-webview#termination-handle) to specify how the `WebView` reacts when its associated renderer goes away.

To learn more about how the system handles low-memory situations, see
[Processes and app
lifecycle](https://developer.android.com/guide/topics/processes/process-lifecycle).