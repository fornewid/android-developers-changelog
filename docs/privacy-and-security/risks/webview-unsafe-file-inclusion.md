---
title: https://developer.android.com/privacy-and-security/risks/webview-unsafe-file-inclusion
url: https://developer.android.com/privacy-and-security/risks/webview-unsafe-file-inclusion
source: md.txt
---

# WebViews – Unsafe File Inclusion

<br />

**OWASP category:** [MASVS-STORAGE: Storage](https://mas.owasp.org/MASVS/05-MASVS-STORAGE)

## Overview

This document covers several issues related to file inclusion that share similar
mitigations. These issues center on vulnerabilities stemming from access to
files within WebViews and range from dangerous [`WebSettings`](https://developer.android.com/reference/android/webkit/WebSettings) allowing file
access, or enabling JavaScript, to a WebKit method that creates a file selection
request. This document should be helpful if you are looking for guidance on
remediation of issues within WebView arising from the use of the `file://`
scheme, unrestricted access to local files, and cross-site scripting.

More concretely, this document covers the following topics:

- `WebSettings` is a class containing methods which manage the setting states for WebViews. These methods can open WebViews to different attacks which will be outlined later. In this document we will look at the methods that pertain to how files can be accessed, and the setting that allows JavaScript to be executed:
- The [`setAllowFileAccess`](https://developer.android.com/reference/android/webkit/WebSettings#setAllowFileAccess(boolean)), [`setAllowFileAccessFromFileURLs`](https://developer.android.com/reference/android/webkit/WebSettings#setAllowFileAccessFromFileURLs(boolean)), and [`setAllowUniversalAccessFromFileURLs`](https://developer.android.com/reference/android/webkit/WebSettings#setAllowUniversalAccessFromFileURLs%28boolean%29) methods can be used to grant access to local files, using a file scheme URL (`file://`). However, they can be exploited by malicious scripts to access arbitrary local files that the application has access to, such as their own `/data/` folder. For this reason, these methods have been flagged as insecure and were deprecated in API 30 in favor of safer alternatives, such as [`WebViewAssetLoader`](https://developer.android.com/reference/androidx/webkit/WebViewAssetLoader).
- The [`setJavascriptEnabled`](https://developer.android.com/reference/android/webkit/WebSettings#setJavaScriptEnabled(boolean)) method can be used to enable the execution of JavaScript within WebViews. This leaves applications vulnerable to file-based XSS. Especially when configured to allow loading of local files or untrusted web content which may contain executable code, configured to allow access to files that can be created or changed by external sources, or allowing WebViews to execute JavaScript, users and their data are put at risk.
- [`WebChromeClient.onShowFileChooser`](https://developer.android.com/reference/android/webkit/WebChromeClient#onShowFileChooser(android.webkit.WebView,%20android.webkit.ValueCallback%3Candroid.net.Uri%5B%5D%3E,%20android.webkit.WebChromeClient.FileChooserParams)) is a method belonging to the `android.webkit` package, which provides web browsing tools. This method can be used to allow users to select files within a WebView. However, this feature can be abused because WebViews don't enforce restrictions on which file is selected.

## Impact

The impact of file inclusion can depend on which WebSettings are configured in
WebView. Overly broad file permissions can allow attackers to access local files
and steal sensitive data, PII (Personally Identifiable Information), or private
app data. Enabling JavaScript execution can allow attackers to run JavaScript
within a WebView or on a user's device. Files selected using the
`onShowFileChooser` method could compromise user security since there is no way
for the method or WebView to ensure that the file source is trusted.

## Risk: Risky Access to Files through file://

Enabling `setAllowFileAccess`, `setAllowFileAccessFromFileURLs`, and
`setAllowUniversalAccessFromFileURLs` can allow malicious intents and WebView
requests with a `file://` context to access arbitrary local files, including
WebView cookies and app private data. Further, using the `onShowFileChooser`
method can allow users to select and download files from untrusted sources.

These methods can all lead to the exfiltration of PII, login credentials, or
other sensitive data, depending on the application configuration.

### Mitigations

#### Validate file URLs

If your app requires access to files through `file://` URLs, it is important to
allowlist only specific URLs that are known to be legitimate, avoiding [common
mistakes](https://blog.oversecured.com/Android-security-checklist-webview/).

#### Use WebViewAssetLoader

Use [`WebViewAssetLoader`](https://developer.android.com/reference/androidx/webkit/WebViewAssetLoader) instead of the mentioned methods. This method uses
the `http(s)//:` scheme instead of a `file://` scheme to access local file
system assets and is not vulnerable to the described attack.  

### Kotlin

    val assetLoader: WebViewAssetLoader = Builder()
      .addPathHandler("/assets/", AssetsPathHandler(this))
      .build()

    webView.setWebViewClient(object : WebViewClientCompat() {
      @RequiresApi(21)
      override fun shouldInterceptRequest(view: WebView?, request: WebResourceRequest): WebResourceResponse {
        return assetLoader.shouldInterceptRequest(request.url)
      }

      @Suppress("deprecation") // for API < 21
      override fun shouldInterceptRequest(view: WebView?, url: String?): WebResourceResponse {
        return assetLoader.shouldInterceptRequest(Uri.parse(url))
      }
    })

    val webViewSettings: WebSettings = webView.getSettings()
    // Setting this off for security. Off by default for SDK versions >= 16.
    webViewSettings.allowFileAccessFromFileURLs = false
    // Off by default, deprecated for SDK versions >= 30.
    webViewSettings.allowUniversalAccessFromFileURLs = false
    // Keeping these off is less critical but still a good idea, especially if your app is not
    // using file:// or content:// URLs.
    webViewSettings.allowFileAccess = false
    webViewSettings.allowContentAccess = false

    // Assets are hosted under http(s)://appassets.androidplatform.net/assets/... .
    // If the application's assets are in the "main/assets" folder this will read the file
    // from "main/assets/www/index.html" and load it as if it were hosted on:
    // https://appassets.androidplatform.net/assets/www/index.html
    webView.loadUrl("https://appassets.androidplatform.net/assets/www/index.html")

### Java

    final WebViewAssetLoader assetLoader = new WebViewAssetLoader.Builder()
             .addPathHandler("/assets/", new AssetsPathHandler(this))
             .build();

    webView.setWebViewClient(new WebViewClientCompat() {
        @Override
        @RequiresApi(21)
        public WebResourceResponse shouldInterceptRequest(WebView view, WebResourceRequest request) {
            return assetLoader.shouldInterceptRequest(request.getUrl());
        }

        @Override
        @SuppressWarnings("deprecation") // for API < 21
        public WebResourceResponse shouldInterceptRequest(WebView view, String url) {
            return assetLoader.shouldInterceptRequest(Uri.parse(url));
        }
    });

    WebSettings webViewSettings = webView.getSettings();
    // Setting this off for security. Off by default for SDK versions >= 16.
    webViewSettings.setAllowFileAccessFromFileURLs(false);
    // Off by default, deprecated for SDK versions >= 30.
    webViewSettings.setAllowUniversalAccessFromFileURLs(false);
    // Keeping these off is less critical but still a good idea, especially if your app is not
    // using file:// or content:// URLs.
    webViewSettings.setAllowFileAccess(false);
    webViewSettings.setAllowContentAccess(false);

    // Assets are hosted under http(s)://appassets.androidplatform.net/assets/... .
    // If the application's assets are in the "main/assets" folder this will read the file
    // from "main/assets/www/index.html" and load it as if it were hosted on:
    // https://appassets.androidplatform.net/assets/www/index.html
    webview.loadUrl("https://appassets.androidplatform.net/assets/www/index.html");

#### Disable dangerous WebSettings methods

The values of the methods `setAllowFileAccess()`,
`setAllowFileAccessFromFileURLs()`, and `setAllowUniversalAccessFromFileURLs()`
are by default set to `TRUE` in API level 29 and lower, and `FALSE` in API level
30 and higher.

If there is a need to configure other `WebSettings`, it would be best to
**explicitly** disable these methods, especially for apps targeting API levels
less than or equal to 29.

*** ** * ** ***

## Risk: File-Based XSS

Setting the `setJavacriptEnabled` method to `TRUE` allows JavaScript to be
executed within a WebView, and in combination with file access enabled as
outlined earlier, file-based XSS is possible through execution of code within
arbitrary files, or malicious websites opened within the WebView.

### Mitigations

#### Prevent WebViews from loading local files

As with the previous risk, file-based XSS can be avoided if
`setAllowFileAccess()`, `setAllowFileAccessFromFileURLs()`, and
`setAllowUniversalAccessFromFileURLs()` are set to `FALSE`.

#### Prevent WebViews executing JavaScript

Set the method `setJavascriptEnabled` to `FALSE` so that JavaScript can't be
executed within WebViews.

#### Ensure WebViews don't load untrusted content

Sometimes enabling these settings is necessary within WebViews. In this case, it
is important to ensure that only trusted content is loaded. Limiting the
execution of JavaScript to only that which you control and disallowing arbitrary
JavaScript is one good way to ensure content is trustworthy. Otherwise,
preventing cleartext traffic from being loaded ensures that WebViews with
dangerous settings are at least not able to load HTTP URLs. This can be done
either through the manifest, setting [`android:usesCleartextTraffic`](https://developer.android.com/guide/topics/manifest/application-element#usesCleartextTraffic) to
`False`, or by setting a [`Network Security Config`](https://developer.android.com/training/articles/security-config) that disallows HTTP
traffic.

*** ** * ** ***

## Resources

- [setAllowUniversalAccessFromFileURLs API reference page](https://developer.android.com/reference/android/webkit/WebSettings#setAllowUniversalAccessFromFileURLs%28boolean%29)
- [setAllowFileAccessFromFileURLs API reference page](https://developer.android.com/reference/android/webkit/WebSettings#setAllowFileAccessFromFileURLs%28boolean%29)
- [WebViewAssetLoader API reference page](https://developer.android.com/reference/androidx/webkit/WebViewAssetLoader)
- [CodeQL documentation](https://codeql.github.com/codeql-query-help/java/java-android-websettings-file-access/)
- [Oversecured blog](https://blog.oversecured.com/Android-security-checklist-webview/#attacks-where-universal-file-access-from-file-urls-is-enabled)
- [onShowFileChooser reference page](https://developer.android.com/reference/android/webkit/WebChromeClient#onShowFileChooser(android.webkit.WebView,%20android.webkit.ValueCallback%3Candroid.net.Uri%5B%5D%3E,%20android.webkit.WebChromeClient.FileChooserParams))