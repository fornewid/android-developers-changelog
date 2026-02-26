---
title: https://developer.android.com/develop/ui/views/layout/webapps/webview
url: https://developer.android.com/develop/ui/views/layout/webapps/webview
source: md.txt
---

Use [`WebView`](https://developer.android.com/reference/android/webkit/WebView) to deliver a web application
or a web page as a part of a client application. The `WebView` class is an
extension of Android's [`View`](https://developer.android.com/reference/android/view/View) class that lets
you display web pages as a part of your activity layout. It doesn't include the
features of a fully developed web browser, such as navigation controls or an
address bar. All `WebView` does, by default, is show a web page.

`WebView` can help you provide information in your app that you might need to
update, such as an end-user agreement or a user guide. Within your Android app,
you can create an [`Activity`](https://developer.android.com/reference/android/app/Activity) that contains a
`WebView`, then use it to display your document that's hosted online.

`WebView` can also help when your app provides data to the user that requires an
internet connection to retrieve data, such as email. In this case, you might
find that it's easier to build a `WebView` in your Android app that shows a web
page with all the user data, rather than performing a network request, then
parsing the data and rendering it in an Android layout. Instead, you can design
a web page that's tailored for Android-powered devices and then implement a
`WebView` in your Android app that loads the web page.

This document describes how to get started with `WebView`, how to bind
JavaScript from your web page to client-side code in your Android app, how to
handle page navigation, and how to manage windows when using `WebView`.

## Work with WebView on earlier versions of Android

To safely use more-recent `WebView` capabilities on the device your app is
running on, add the [AndroidX
Webkit](https://developer.android.com/reference/androidx/webkit/package-summary) library. This is a static
library you can add to your application to use `android.webkit` APIs that aren't
available for earlier platform versions.

Add it to your `build.gradle` file as follows:

### Kotlin

```kotlin
dependencies {
    implementation("androidx.webkit:webkit:1.8.0")
}
```

### Groovy

```groovy
dependencies {
    implementation ("androidx.webkit:webkit:1.8.0")
}
```

Explore [the `WebView`
example](https://github.com/android/views-widgets-samples/tree/main/WebView)
on GitHub for more details.

## Add a WebView to your app

To add a `WebView` to your app, you can include the `<WebView>` element in your
activity layout or set the entire `Activity` window as a `WebView` in
[`onCreate()`](https://developer.android.com/reference/android/app/Activity#onCreate(android.os.Bundle,%20android.os.PersistableBundle)).

### Add a WebView in the activity layout

To add a `WebView` to your app in the layout, add the following code to your
activity's layout XML file:

```xml
<WebView
    android:id="@+id/webview"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
/>
```

To load a web page in the `WebView`, use
[`loadUrl()`](https://developer.android.com/reference/android/webkit/WebView#loadUrl(java.lang.String)), as
shown in the following example:

### Kotlin

```kotlin
val myWebView: WebView = findViewById(R.id.webview)
myWebView.loadUrl("http://www.example.com")
```

### Java

```java
WebView myWebView = (WebView) findViewById(R.id.webview);
myWebView.loadUrl("http://www.example.com");
```

### Add a WebView in onCreate()

To add a `WebView` to your app in an activity's `onCreate()` method instead, use
logic similar to the following:

### Kotlin

```kotlin
val myWebView = WebView(activityContext)
setContentView(myWebView)
```

### Java

```java
WebView myWebView = new WebView(activityContext);
setContentView(myWebView);
```

Then load the page:

### Kotlin

```kotlin
myWebView.loadUrl("http://www.example.com")
```

### Java

```java
myWebView.loadUrl("https://www.example.com");
```

Or load the URL from an HTML string:

### Kotlin

```kotlin
// Create an unencoded HTML string, then convert the unencoded HTML string into
// bytes. Encode it with base64 and load the data.
val unencodedHtml =
     "<html><body>'%23' is the percent code for '#' </body></html>";
val encodedHtml = Base64.encodeToString(unencodedHtml.toByteArray(), Base64.NO_PADDING)
myWebView.loadData(encodedHtml, "text/html", "base64")
```

### Java

```java
// Create an unencoded HTML string, then convert the unencoded HTML string into
// bytes. Encode it with base64 and load the data.
String unencodedHtml =
     "<html><body>'%23' is the percent code for '#' </body></html>";
String encodedHtml = Base64.encodeToString(unencodedHtml.getBytes(),
        Base64.NO_PADDING);
myWebView.loadData(encodedHtml, "text/html", "base64");
```

> [!NOTE]
> **Note:** There are restrictions on what this HTML can do. See [`loadData()`](https://developer.android.com/reference/android/webkit/WebView#loadData(java.lang.String,%20java.lang.String,%20java.lang.String)) and [`loadDataWithBaseURL()`](https://developer.android.com/reference/android/webkit/WebView#loadDataWithBaseURL(java.lang.String,%20java.lang.String,%20java.lang.String,%20java.lang.String,%20java.lang.String)) for more info about encoding options.

Your app must have access to the internet. To get internet access, request the
[`INTERNET`](https://developer.android.com/reference/android/Manifest.permission#INTERNET) permission in your
manifest file, as shown in the following example:

```xml
<manifest ... >
    <uses-permission android:name="android.permission.INTERNET" />
    ...
</manifest>
```

You can customize your `WebView` by doing any of the following:

- Enabling fullscreen support using [`WebChromeClient`](https://developer.android.com/reference/android/webkit/WebChromeClient). This class is also called when a `WebView` needs permission to alter the host app's UI, such as creating or closing windows or sending JavaScript dialogs to the user. To learn more about debugging in this context, read [Debug web
  apps](https://developer.android.com/guide/webapps/debugging).
- Handling events that impact content rendering, such as errors on form submissions or navigation using [`WebViewClient`](https://developer.android.com/reference/android/webkit/WebViewClient). You can also use this subclass to intercept URL loading.
- Enabling JavaScript by modifying [`WebSettings`](https://developer.android.com/reference/android/webkit/WebSettings).
- Using JavaScript to access Android framework objects that you have injected into a `WebView`.

## Use JavaScript in WebView

If the web page you want to load in your `WebView` uses JavaScript, you must
enable JavaScript for your `WebView`. After you enable JavaScript, you can
create interfaces between your app code and your JavaScript code.

### Enable JavaScript

JavaScript is disabled in a `WebView` by default. You can enable it through the
`WebSettings` attached to your `WebView`. Retrieve `WebSettings` with
[`getSettings()`](https://developer.android.com/reference/android/webkit/WebView#getSettings()), then enable
JavaScript with
[`setJavaScriptEnabled()`](https://developer.android.com/reference/android/webkit/WebSettings#setJavaScriptEnabled(boolean)).

See the following example:

### Kotlin

```kotlin
val myWebView: WebView = findViewById(R.id.webview)
myWebView.settings.javaScriptEnabled = true
```

### Java

```java
WebView myWebView = (WebView) findViewById(R.id.webview);
WebSettings webSettings = myWebView.getSettings();
webSettings.setJavaScriptEnabled(true);
```

`WebSettings` provides access to a variety of other settings that you might find
useful. For example, if you're developing a web application that's designed
specifically for the `WebView` in your Android app, then you can define a custom
user agent string with
[`setUserAgentString()`](https://developer.android.com/reference/android/webkit/WebSettings#setUserAgentString(java.lang.String)),
then query the custom user agent in your web page to verify that the client
requesting your web page is your Android app.

### Bind JavaScript code to Android code

When developing a web application that's designed specifically for the `WebView`
in your Android app, you can create interfaces between your JavaScript code and
client-side Android code. For example, your JavaScript code can call a method in
your Android code to display a [`Dialog`](https://developer.android.com/reference/android/app/Dialog),
instead of using JavaScript's `alert()` function.

To bind a new interface between your JavaScript and Android code, call
[`addJavascriptInterface()`](https://developer.android.com/reference/android/webkit/WebView#addJavascriptInterface(java.lang.Object,%20java.lang.String)),
passing it a class instance to bind to your JavaScript and an interface name
that your JavaScript can call to access the class.

> [!WARNING]
> **Warning:** Using `addJavascriptInterface()` lets JavaScript control your Android app. Although this can be useful, it can also be a dangerous security issue. When the HTML in the `WebView` is untrustworthy---for example, part or all of the HTML is provided by an unknown person or process---then an attacker can include HTML that executes your client-side code and possibly any code of the attacker's choosing. Therefore, don't use `addJavascriptInterface()` unless you wrote all of the HTML and JavaScript that appears in your `WebView`. Don't let the user navigate within your `WebView` to web pages that aren't your own. Instead, let the user's default browser application open foreign links. By default, the user's web browser opens all URL links, so this warning primarily applies if you handle page navigation yourself, as described in the following section.

For example, you can include the following class in your Android app:

### Kotlin

```kotlin
/** Instantiate the interface and set the context.  */
class WebAppInterface(private val mContext: Context) {

    /** Show a toast from the web page.  */
    @JavascriptInterface
    fun showToast(toast: String) {
        Toast.makeText(mContext, toast, Toast.LENGTH_SHORT).show()
    }
}
```

### Java

```java
public class WebAppInterface {
    Context mContext;

    /** Instantiate the interface and set the context. */
    WebAppInterface(Context c) {
        mContext = c;
    }

    /** Show a toast from the web page. */
    @JavascriptInterface
    public void showToast(String toast) {
        Toast.makeText(mContext, toast, Toast.LENGTH_SHORT).show();
    }
}
```

> [!CAUTION]
> **Caution:** If you set your [`targetSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#target) to 17 or later, add the `@JavascriptInterface` annotation to any method that you want to be available to your JavaScript. The method must be public. If you don't provide this annotation, the method isn't accessible by your web page.

In this example, the `WebAppInterface` class lets the web page create a
[`Toast`](https://developer.android.com/reference/android/widget/Toast) message, using the `showToast()`
method.

You can bind this class to the JavaScript that runs in your `WebView` with
`addJavascriptInterface()`, as shown in the following example:

### Kotlin

```kotlin
val webView: WebView = findViewById(R.id.webview)
webView.addJavascriptInterface(WebAppInterface(this), "Android")
```

### Java

```java
WebView webView = (WebView) findViewById(R.id.webview);
webView.addJavascriptInterface(new WebAppInterface(this), "Android");
```

This creates an interface called `Android` for JavaScript running in the
`WebView`. At this point, your web application has access to the
`WebAppInterface` class. For example, here's some HTML and JavaScript that
creates a toast message using the new interface when the user taps a button:

```javascript
<input type="button" value="Say hello" onClick="showAndroidToast('Hello Android!')" />

<script type="text/javascript">
    function showAndroidToast(toast) {
        Android.showToast(toast);
    }
</script>
```

There's no need to initialize the `Android` interface from JavaScript. The
`WebView` automatically makes it available to your web page. So, when a user
taps the button, the `showAndroidToast()` function uses the `Android` interface
to call the `WebAppInterface.showToast()` method.

> [!NOTE]
> **Note:** The object that is bound to your JavaScript runs in another thread and not in the thread in which it is constructed.

## Handle page navigation

When the user taps a link from a web page in your `WebView`, by default, Android
launches an app that handles URLs. Usually, the default web browser opens and
loads the destination URL. However, you can override this behavior for your
`WebView` so links open within your `WebView`. You can then let the user
navigate backward and forward through their web page history that's maintained
by your `WebView`.

> [!NOTE]
> **Note:** For security reasons, the system's browser app doesn't share its application data with your app.

To open links tapped by the user, provide a `WebViewClient` for your `WebView`
using
[`setWebViewClient()`](https://developer.android.com/reference/android/webkit/WebView#setWebViewClient(android.webkit.WebViewClient)).
All links the user taps load in your `WebView`. If you want more control over
where a clicked link loads, create your own `WebViewClient` that overrides the
[`shouldOverrideUrlLoading()`](https://developer.android.com/reference/android/webkit/WebViewClient#shouldOverrideUrlLoading(android.webkit.WebView,%20android.webkit.WebResourceRequest))
method. The following example assumes that `MyWebViewClient` is an inner class
of `Activity`.

### Kotlin

```kotlin
private class MyWebViewClient : WebViewClient() {

    override fun shouldOverrideUrlLoading(view: WebView?, url: String?): Boolean {
        if (Uri.parse(url).host == "www.example.com") {
            // This is your website, so don't override. Let your WebView load
            // the page.
            return false
        }
        // Otherwise, the link isn't for a page on your site, so launch another
        // Activity that handles URLs.
        Intent(Intent.ACTION_VIEW, Uri.parse(url)).apply {
            startActivity(this)
        }
        return true
    }
}
```

### Java

```java
private class MyWebViewClient extends WebViewClient {
    @Override
    public boolean shouldOverrideUrlLoading(WebView view, WebResourceRequest request) {
        if ("www.example.com".equals(request.getUrl().getHost())) {
      // This is your website, so don't override. Let your WebView load the
      // page.
      return false;
    }
    // Otherwise, the link isn't for a page on your site, so launch another
    // Activity that handles URLs.
    Intent intent = new Intent(Intent.ACTION_VIEW, request.getUrl());
    startActivity(intent);
    return true;
  }
}
```

Then create an instance of this new `WebViewClient` for the `WebView`:

### Kotlin

```kotlin
val myWebView: WebView = findViewById(R.id.webview)
myWebView.webViewClient = MyWebViewClient()
```

### Java

```java
WebView myWebView = (WebView) findViewById(R.id.webview);
myWebView.setWebViewClient(new MyWebViewClient());
```

Now when the user taps a link, the system calls the
`shouldOverrideUrlLoading()` method, which checks whether the URL host matches
a specific domain, as defined in the preceding example. If it does match, then
the method returns false and doesn't override the URL loading. It lets the
`WebView` load the URL as usual. If the URL host doesn't match, then an
[`Intent`](https://developer.android.com/reference/android/content/Intent) is created to launch the default
`Activity` for handling URLs, which resolves to the user's default web browser.

### Handle custom URLs

`WebView` applies restrictions when requesting resources and resolving links
that use a custom URL scheme. For example, if you implement callbacks such as
[`shouldOverrideUrlLoading()`](https://developer.android.com/reference/android/webkit/WebViewClient#shouldOverrideUrlLoading(android.webkit.WebView,%20android.webkit.WebResourceRequest))
or
[`shouldInterceptRequest()`](https://developer.android.com/reference/android/webkit/WebViewClient#shouldInterceptRequest(android.webkit.WebView,%20android.webkit.WebResourceRequest)),
then `WebView` invokes them only for valid URLs.

For example, `WebView` might not call your `shouldOverrideUrlLoading()` method
for links like this:

    <a href="showProfile">Show Profile</a>

Invalid URLs, like the one shown in the preceding example, are handled
inconsistently in `WebView`, so we recommend using a well-formed URL instead.
You can use a custom scheme or an HTTPS URL for a domain that your organization
controls.

Instead of using a simple string in a link, as in the previous example, you can
use a custom scheme such as the following:

    <a href="example-app:showProfile">Show Profile</a>

You can then handle this URL in your `shouldOverrideUrlLoading()` method like
this:

### Kotlin

```kotlin
// The URL scheme must be non-hierarchical, meaning no trailing slashes.
const val APP_SCHEME = "example-app:"

override fun shouldOverrideUrlLoading(view: WebView?, url: String?): Boolean {
    return if (url?.startsWith(APP_SCHEME) == true) {
        urlData = URLDecoder.decode(url.substring(APP_SCHEME.length), "UTF-8")
        respondToData(urlData)
        true
    } else {
        false
    }
}
```

### Java

```java
// The URL scheme must be non-hierarchical, meaning no trailing slashes.
private static final String APP_SCHEME = "example-app:";

@Override
public boolean shouldOverrideUrlLoading(WebView view, String url) {
    if (url.startsWith(APP_SCHEME)) {
        urlData = URLDecoder.decode(url.substring(APP_SCHEME.length()), "UTF-8");
        respondToData(urlData);
        return true;
    }
    return false;
}
```

The `shouldOverrideUrlLoading()` API is primarily intended for launching intents
for specific URLs. When implementing it, make sure to return `false` for URLs
the `WebView` handles. You aren't limited to launching intents, though. You can
replace launching intents with any custom behavior in the preceding code
samples.

> [!CAUTION]
> **Caution:** Don't call `loadUrl()`, `reload()`, or similar methods from within `shouldOverrideUrlLoading()`. This leads to inefficient apps. It's more efficient to return `false` to let `WebView` continue loading the URL with its default implementation.

### Navigate web page history

When your `WebView` overrides URL loading, it automatically accumulates a
history of visited web pages. You can navigate backward and forward through the
history with [`goBack()`](https://developer.android.com/reference/android/webkit/WebView#goBack()) and
[`goForward()`](https://developer.android.com/reference/android/webkit/WebView#goForward()).

For example, the following shows how your `Activity` can use the device Back
button to navigate backward:

### Kotlin

```kotlin
override fun onKeyDown(keyCode: Int, event: KeyEvent?): Boolean {
    // Check whether the key event is the Back button and if there's history.
    if (keyCode == KeyEvent.KEYCODE_BACK && myWebView.canGoBack()) {
        myWebView.goBack()
        return true
    }
    // If it isn't the Back button or there isn't web page history, bubble up to
    // the default system behavior. Probably exit the activity.
    return super.onKeyDown(keyCode, event)
}
```

### Java

```java
@Override
public boolean onKeyDown(int keyCode, KeyEvent event) {
    // Check whether the key event is the Back button and if there's history.
    if ((keyCode == KeyEvent.KEYCODE_BACK) && myWebView.canGoBack()) {
        myWebView.goBack();
        return true;
    }
    // If it isn't the Back button or there's no web page history, bubble up to
    // the default system behavior. Probably exit the activity.
    return super.onKeyDown(keyCode, event);
}
```

If you app uses AndroidX `AppCompat` 1.6.0+, you can simplify the previous
snippet even more:

### Kotlin

```kotlin
onBackPressedDispatcher.addCallback {
    // Check whether there's history.
    if (myWebView.canGoBack()) {
        myWebView.goBack()
    }
}
```

### Java

```java
onBackPressedDispatcher.addCallback {
    // Check whether there's history.
    if (myWebView.canGoBack()) {
        myWebView.goBack();
    }
}
```

The [`canGoBack()`](https://developer.android.com/reference/android/webkit/WebView#canGoBack()) method
returns true if there is web page history for the user to visit. Likewise, you
can use [`canGoForward()`](https://developer.android.com/reference/android/webkit/WebView#canGoForward()) to
check whether there is a forward history. If you don't perform this check, then
after the user reaches the end of the history, `goBack()` and `goForward()` do
nothing.

### Handle device configuration changes

During runtime, activity state changes occur when a device's configuration
changes, such as when users rotate the device or dismiss an input method editor
(IME). These changes cause a `WebView` object's activity to be destroyed and a
new activity to be created, which also creates a new `WebView` object that loads
the destroyed object's URL. To modify your activity's default behavior, you can
change how it handles `orientation` changes in your manifest. To learn more
about handling configuration changes during runtime, read [Handle configuration
changes](https://developer.android.com/guide/topics/resources/runtime-changes).

## Manage windows

By default, requests to open new windows are ignored. This is true whether they
are opened by JavaScript or by the target attribute in a link. You can customize
your `WebChromeClient` to provide your own behavior for opening multiple
windows.

To keep your app more secure, it's best to prevent popups and new windows from
opening. The safest way to implement this behavior is to pass `"true"` into
[`setSupportMultipleWindows()`](https://developer.android.com/reference/android/webkit/WebSettings#setSupportMultipleWindows(boolean))
but not override the
[`onCreateWindow()`](https://developer.android.com/reference/android/webkit/WebChromeClient#onCreateWindow(android.webkit.WebView,%20boolean,%20boolean,%20android.os.Message))
method, which `setSupportMultipleWindows()` depends on. This logic prevents any
page that uses `target="_blank"` in its links from loading.