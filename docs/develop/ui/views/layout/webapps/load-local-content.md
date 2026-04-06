---
title: https://developer.android.com/develop/ui/views/layout/webapps/load-local-content
url: https://developer.android.com/develop/ui/views/layout/webapps/load-local-content
source: md.txt
---

You can provide web-based content---such as HTML, JavaScript, and
CSS---for your app to use that you statically compile into the app rather
than fetch over the internet.

In-app content doesn't require internet access or consume a user's bandwidth. If
the content is designed specifically for `WebView` only---that is, it
depends on communicating with a native app---then users can't accidentally
load it in a web browser.

However, there are some drawbacks to in-app content. Updating web-based content
requires shipping a new app update, and there is the possibility of mismatched
content between what's on a website and what's in the app on your device if
users have outdated app versions.

## WebViewAssetLoader

[`WebViewAssetLoader`](https://developer.android.com/reference/androidx/webkit/WebViewAssetLoader) is a
flexible and performant way to load in-app content in a
[`WebView`](https://developer.android.com/reference/android/webkit/WebView) object. This class supports the
following:

- Loading content with an HTTP(S) URL for compatibility with the [same-origin
  policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy).
- Loading subresources such as JavaScript, CSS, images, and iframes.

Include `WebViewAssetLoader` in your main activity file. The following is an
example of loading simple web content from the assets folder:

### Kotlin

```kotlin
private class LocalContentWebViewClient(private val assetLoader: WebViewAssetLoader) : WebViewClientCompat() {
    @RequiresApi(21)
    override fun shouldInterceptRequest(
        view: WebView,
        request: WebResourceRequest
    ): WebResourceResponse? {
        return assetLoader.shouldInterceptRequest(request.url)
    }

    // To support API < 21.
    override fun shouldInterceptRequest(
        view: WebView,
        url: String
    ): WebResourceResponse? {
        return assetLoader.shouldInterceptRequest(Uri.parse(url))
    }
}
```

### Java

```java
private static class LocalContentWebViewClient extends WebViewClientCompat {

    private final WebViewAssetLoader mAssetLoader;

    LocalContentWebViewClient(WebViewAssetLoader assetLoader) {
        mAssetLoader = assetLoader;
    }

    @Override
    @RequiresApi(21)
    public WebResourceResponse shouldInterceptRequest(WebView view,
                                     WebResourceRequest request) {
        return mAssetLoader.shouldInterceptRequest(request.getUrl());
    }

    @Override
    @SuppressWarnings("deprecation") // To support API < 21.
    public WebResourceResponse shouldInterceptRequest(WebView view,
                                     String url) {
        return mAssetLoader.shouldInterceptRequest(Uri.parse(url));
    }
}
```

Your app must configure a `WebViewAssetLoader` instance to suit its needs. The
next section has an example.

### Create in-app assets and resources

`WebViewAssetLoader` relies on
[`PathHandler`](https://developer.android.com/reference/androidx/webkit/WebViewAssetLoader.PathHandler)
instances to load resources corresponding to a given resource path. Although you
can implement this interface to retrieve resources as needed by your app, the
Webkit library bundles
[`AssetsPathHandler`](https://developer.android.com/reference/kotlin/androidx/webkit/WebViewAssetLoader.AssetsPathHandler)
and
[`ResourcesPathHandler`](https://developer.android.com/reference/kotlin/androidx/webkit/WebViewAssetLoader.ResourcesPathHandler)
for loading Android assets and resources, respectively.

To get started, create assets and resources for your app. Generally, the
following applies:

- Text files like HTML, JavaScript, and CSS belong in assets.
- Images and other binary files belong in resources.

To add text-based web files to a project, do the following:

1. In Android Studio, right-click the **app \> src \> main** folder and then choose **New \> Directory** . ![An image showing Android Studio create-directory menus](https://developer.android.com/static/images/guide/webapps/create-assets-directory.png) **Figure 1.** Create an assets folder for your project.
2. Name the folder "assets". ![An image showing the asset folder](https://developer.android.com/static/images/guide/webapps/name-assets-directory.png) **Figure 2.** Name the assets folder.
3. Right-click the **assets** folder and then click **New \> File** . Enter `index.html` and press the <kbd>Return</kbd> or <kbd>Enter</kbd> key. ![An image of Android Studio create file menu](https://developer.android.com/static/images/guide/webapps/create-webview-file.png) **Figure 3.** Create the `index.html` file.
4. Repeat the previous step to create an empty file for `stylesheet.css`.
5. Fill in the empty files you created with the content in the next two code samples.

    ```html
    <!-- index.html content -->

    <html>
      <head>
        <!-- Tip: Use relative URLs when referring to other in-app content to give
                  your app code the flexibility to change the scheme or domain as
                  necessary. -->
        <link rel="stylesheet" href="/assets/stylesheet.css">
      </head>
      <body>
        <p>This file is loaded from in-app content.</p>
        <p><img src="/res/drawable/android_robot.png" alt="Android robot" width="100"></p>
      </body>
    </html>
    ```

    ```css
    <!-- stylesheet.css content -->

    body {
      background-color: lightblue;
    }
    ```

To add an image-based web file to your project, do the following:

1. Download the
   [`Android_symbol_green_RGB.png`](https://source.android.com/setup/images/Android_symbol_green_RGB.png)
   file to your local machine.

2. Rename the file to `android_robot.png`.

3. Manually move the file into your project's `main/res/drawable` directory on
   your hard drive.

Figure 4 shows the image you added and the text from the preceding code samples
rendered in an app.
![An image showing app rendered output](https://developer.android.com/static/images/guide/webapps/rendered-html.png) **Figure 4.** In-app HTML file and image file rendered in an app.

To complete the app, do the following:

1. Register the handlers and configure the `AssetLoader` by adding the
   following code to the `onCreate()` method:

   ### Kotlin

   ```kotlin
   val assetLoader = WebViewAssetLoader.Builder()
                          .addPathHandler("/assets/", AssetsPathHandler(this))
                          .addPathHandler("/res/", ResourcesPathHandler(this))
                          .build()
   webView.webViewClient = LocalContentWebViewClient(assetLoader)
   ```

   ### Java

   ```java
   final WebViewAssetLoader assetLoader = new WebViewAssetLoader.Builder()
            .addPathHandler("/assets/", new WebViewAssetLoader.AssetsPathHandler(this))
            .addPathHandler("/res/", new WebViewAssetLoader.ResourcesPathHandler(this))
            .build();
   mWebView.setWebViewClient(new LocalContentWebViewClient(assetLoader));
   ```
2. Load the content by adding the following code to the `onCreate()` method:

   ### Kotlin

   ```kotlin
   webView.loadUrl("https://appassets.androidplatform.net/assets/index.html")
   ```

   ### Java

   ```java
   mWebView.loadUrl("https://appassets.androidplatform.net/assets/index.html");
   ```

### Mix in-app content with resources from your website

Your app might need to load a mix of in-app content and content from the
internet, such as an in-app HTML page styled by your website's CSS.
`WebViewAssetLoader` supports this use case. If none of the registered
`PathHandler` instances can find a resource for the given path, `WebView` falls
back to loading content from the internet. If you mix in-app content with
resources from your website, reserve directory paths, such as `/assets/` or
`/resources/`, for in-app resources. Avoid storing any resources from your
website in those locations.

### Kotlin

```kotlin
val assetLoader = WebViewAssetLoader.Builder()
                        .setDomain("example.com") // Replace this with your website's domain.
                        .addPathHandler("/assets/", AssetsPathHandler(this))
                        .build()

webView.webViewClient = LocalContentWebViewClient(assetLoader)
val inAppHtmlUrl = "https://example.com/assets/index.html"
webView.loadUrl(inAppHtmlUrl)
val websiteUrl = "https://example.com/website/data.json"

// JavaScript code to fetch() content from the same origin.
val jsCode = "fetch('$websiteUrl')" +
        ".then(resp => resp.json())" +
        ".then(data => console.log(data));"

webView.evaluateJavascript(jsCode, null)
```

### Java

```java
final WebViewAssetLoader assetLoader = new WebViewAssetLoader.Builder()
           .setDomain("example.com") // Replace this with your website's domain.
           .addPathHandler("/assets/", new AssetsPathHandler(this))
           .build();

mWebView.setWebViewClient(new LocalContentWebViewClient(assetLoader));
String inAppHtmlUrl = "https://example.com/assets/index.html";
mWebView.loadUrl(inAppHtmlUrl);
String websiteUrl = "https://example.com/website/data.json";

// JavaScript code to fetch() content from the same origin.
String jsCode = "fetch('" + websiteUrl + "')" +
      ".then(resp => resp.json())" +
      ".then(data => console.log(data));";

mWebView.evaluateJavascript(jsCode, null);
```

See the [`WebView` demo on
GitHub](https://github.com/android/views-widgets-samples/tree/main/WebView)
for an example of an in-app HTML page fetching web-hosted JSON data.

## loadDataWithBaseURL

When your app only needs to load an HTML page and doesn't need to intercept
subresources, consider using
[`loadDataWithBaseURL()`](https://developer.android.com/reference/android/webkit/WebView#loadDataWithBaseURL(java.lang.String,%20java.lang.String,%20java.lang.String,%20java.lang.String,%20java.lang.String)),
which doesn't require app assets. You can use it as shown in the following code
sample:

### Kotlin

```kotlin
val html = "<html><body><p>Hello world</p></body></html>"
val baseUrl = "https://example.com/"

webView.loadDataWithBaseURL(baseUrl, html, "text/html", null, baseUrl)
```

### Java

```java
String html = "<html><body><p>Hello world</p></body></html>";
String baseUrl = "https://example.com/";

mWebView.loadDataWithBaseURL(baseUrl, html, "text/html", null, baseUrl);
```

Choose argument values carefully. Consider the following:

- `baseUrl`: this is the URL your HTML content is loaded as. This must be an HTTP(S) URL.
- `data`: this is the HTML content you want to display, as a string.
- `mimeType`: this must usually be set to `text/html`.
- `encoding`: this is unused when `baseUrl` is an HTTP(S) URL, so it can be set to `null`.
- `historyUrl`: this is set to the same value as `baseUrl`.

We strongly recommend using an HTTP(S) URL as the `baseUrl`, as this helps
ensure your app complies with the same-origin policy.

If you can't find a suitable `baseUrl` for your content and prefer to use
[`loadData()`](https://developer.android.com/reference/android/webkit/WebView#loadData(java.lang.String,%20java.lang.String,%20java.lang.String)),
you **must encode the content** with
[percent-encoding](https://developer.mozilla.org/en-US/docs/Glossary/percent-encoding)
or
[Base64
encoding](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URIs#encoding_data_into_base64_format).
We strongly recommend choosing Base64 encoding and using Android APIs to encode
this programmatically, as shown in the following code sample:

### Kotlin

```kotlin
val encodedHtml: String = Base64.encodeToString(html.toByteArray(), Base64.NO_PADDING)

webView.loadData(encodedHtml, mimeType, "base64")
```

### Java

```java
String encodedHtml = Base64.encodeToString(html.getBytes(), Base64.NO_PADDING);

mWebView.loadData(encodedHtml, mimeType, "base64");
```

> [!CAUTION]
> **Caution:** By default, `loadData()` expects the HTML data to be percent-encoded. Percent-encoding by hand is error prone, and there are no Android APIs to do this programmatically. We strongly recommend switching to `loadDataWithBaseURL()` to avoid this requirement or using Base64 APIs to encode the content, as shown in the preceding code sample.

## Things to avoid

There are several other ways to load in-app content, but we strongly recommend
against them:

- `file://` URLs and `data:` URLs are considered to be *opaque origins* , meaning they can't take advantage of powerful web APIs such as [`fetch()`](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) or [`XMLHttpRequest`](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest). `loadData()` internally uses `data:` URLs, so we encourage using `WebViewAssetLoader` or `loadDataWithBaseURL()` instead.
- Although [`WebSettings.setAllowFileAccessFromFileURLs()`](https://developer.android.com/reference/android/webkit/WebSettings#setAllowFileAccessFromFileURLs(boolean)) and [`WebSettings.setAllowUniversalAccessFromFileURLs()`](https://developer.android.com/reference/android/webkit/WebSettings#setAllowUniversalAccessFromFileURLs(boolean)) can work around the issues with `file://` URLs, we recommend against setting these to `true` because doing so leaves your app vulnerable to file-based exploits. We recommend explicitly setting these to `false` on all API levels for the strongest security.
- For the same reasons, we recommend against `file://android_assets/` and `file://android_res/` URLs. The `AssetsHandler` and `ResourcesHandler` classes are meant to be drop-in replacements.
- Avoid using [`MIXED_CONTENT_ALWAYS_ALLOW`](https://developer.android.com/reference/android/webkit/WebSettings#MIXED_CONTENT_ALWAYS_ALLOW). This setting generally isn't necessary and weakens the security of your app. We recommend loading your in-app content over the same scheme---HTTP or HTTPS---as your website's resources and using [`MIXED_CONTENT_COMPATIBILITY_MODE`](https://developer.android.com/reference/android/webkit/WebSettings#MIXED_CONTENT_COMPATIBILITY_MODE) or [`MIXED_CONTENT_NEVER_ALLOW`](https://developer.android.com/reference/android/webkit/WebSettings#MIXED_CONTENT_NEVER_ALLOW), as appropriate.