---
title: https://developer.android.com/privacy-and-security/risks/insecure-webview-native-bridges
url: https://developer.android.com/privacy-and-security/risks/insecure-webview-native-bridges
source: md.txt
---

# WebView – Native bridges

<br />

**OWASP category:** [MASVS-PLATFORM: Platform Interaction](https://mas.owasp.org/MASVS/09-MASVS-PLATFORM)

## Overview

A native bridge, sometimes known as a JavaScript bridge, is a mechanism that facilitates communication between a WebView and native Android code, achieved by using the[`addJavascriptInterface`](https://developer.android.com/reference/android/webkit/WebView#addJavascriptInterface(java.lang.Object,%20java.lang.String))method. This allows for two-way communication between JavaScript code running in the WebView and the Android application's Java code. The`addJavascriptInterface`method exposes a Java object to all of a WebView's frames, and any frame can access the object name and call methods on it. However, there is no mechanism for the application to verify the origin of the calling frame within the WebView, which raises security concerns as the trustworthiness of the content remains indeterminate.

A native bridge can also be implemented with HTML message channels using Android's[`WebViewCompat.postWebMessage`](https://developer.android.com/reference/androidx/webkit/WebViewCompat#postWebMessage(android.webkit.WebView,androidx.webkit.WebMessageCompat,android.net.Uri))or[`WebMessagePort.postMessage`](https://developer.android.com/reference/android/webkit/WebMessagePort#postMessage(android.webkit.WebMessage))to communicate with the JavaScript[`Window.postMessage`](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage).`WebViewCompat.postWebMessage`and`WebMessagePort.postMessage`can accept JavaScript messages sent through`Window.postMessage`which will be executed within the WebView.

There are multiple risks associated with native bridges:

- JavascriptInterface-based bridges:
  - The`addJavascriptInterface`method injects a supplied Java object into every frame of the WebView, including iframes, which means it is susceptible to attack by malicious third parties injecting frames into a legitimate website. Applications targeting API level 16 or earlier are particularly at risk of attack because this method can be used to allow JavaScript to control the host application.
  - Reflecting untrusted user-provided content in native bridge-enabled WebViews allows for cross-site scripting (XSS) attacks.
- MessageChannel-based bridges:
  - Lack of origin checks on message channel endpoints means that messages will be accepted from any sender, including those containing malicious code.
  - It is possible to accidentally expose Java to arbitrary JavaScript.

## Impact

The`addJavascriptInterface`,`postWebMessage`, and`postMessage`methods can be leveraged by malicious actors to access, manipulate, or inject code they control into a WebView. This may lead to users being redirected to malicious sites, loading malicious content, or having malicious code run on their devices that can extract sensitive data or achieve privilege escalation.

## Risk: addJavascriptInterface risks

WebView implements basic functionalities of a browser, such as page rendering, navigation, and JavaScript execution. WebView can be used inside an application to display web content as part of an activity layout. Implementing a native bridge within a WebView using the`addJavascriptInterface`method can create security issues such as cross-site scripting (XSS), or allow attackers to load untrusted content through interface injection and manipulate the host application in unintended ways, executing Java code with the permissions of the host application.

### Mitigations

#### Disable JavaScript

In scenarios where WebView doesn't require JavaScript, don't call[`setJavaScriptEnabled`](https://developer.android.com/reference/android/webkit/WebSettings#setJavaScriptEnabled(boolean))within[`WebSettings`](https://developer.android.com/reference/android/webkit/WebSettings)(for example, while displaying static HTML content). By default, JavaScript execution is disabled in WebView.

#### Remove JavaScript interface when loading untrusted content

Ensure objects from the JavaScript interface are removed by calling[`removeJavascriptInterface`](https://developer.android.com/reference/android/webkit/WebView#removeJavascriptInterface(java.lang.String))before untrusted content is loaded by the WebView. For example, this can be done in a call to[`shouldInterceptRequest`](https://developer.android.com/reference/android/webkit/WebViewClient#shouldInterceptRequest(android.webkit.WebView,%20android.webkit.WebResourceRequest)).  

### Kotlin

    webView.removeJavascriptInterface("myObject")

### Java

    webView.removeJavascriptInterface("myObject");

#### Only load web content over HTTPS

If you need to load untrusted content, ensure the WebView loads web content over an encrypted connection (see also our guidelines on[Cleartext Communications](https://developer.android.com/privacy-and-security/risks/cleartext-communications)). Prevent the initial page load from being performed on unencrypted connections by setting`android:usesCleartextTraffic`to`false`in the`AndroidManifest`file or disallow HTTP traffic in a[network security config](https://developer.android.com/training/articles/security-config). See the[`usesCleartextTraffic`](https://developer.android.com/guide/topics/manifest/application-element#usesCleartextTraffic)documentation for more information.  

### Xml

    <application
        android:usesCleartextTraffic="false">
        <!-- Other application elements -->
    </application>

To ensure that redirects and further app browsing doesn't occur on unencrypted traffic, check for the HTTP scheme in[`loadUrl`](https://developer.android.com/reference/android/webkit/WebView#loadUrl(java.lang.String))or`shouldInterceptRequest`:  

### Kotlin

    fun loadSecureUrl(webView: WebView?, url: String?) {
        webView?.let { wv ->  // Ensure valid WebView and URL
            url?.let {
                try {
                    val uri = URI(url)
                    if (uri.scheme.equals("https", ignoreCase = true)) { // Enforce HTTPS scheme for security
                        wv.loadUrl(url)
                    } else {
                        // Log an error or handle the case where the URL is not secure
                        System.err.println("Attempted to load a non-HTTPS URL: $url")
                    }
                } catch (e: Exception) {
                    // Handle exception for improper URL format
                    System.err.println("Invalid URL syntax: $url")
                }
            }
        }
    }

### Java

    public void loadSecureUrl(WebView webView, String url) {
        if (webView != null && url != null) { // Ensure valid WebView and URL
            try {
                URI uri = new URI(url);
                String scheme = uri.getScheme();
                if ("https".equalsIgnoreCase(scheme)) { // Enforce HTTPS scheme for security
                    webView.loadUrl(url);
                } else {
                    // Log an error or handle the case where the URL is not secure
                    System.err.println("Attempted to load a non-HTTPS URL: " + url);
                }
            } catch (URISyntaxException e) {
                // Handle exception for improper URL format
                System.err.println("Invalid URL syntax: " + url);
            }
        }
    }

#### Validate untrusted content

If any external links are loaded in a WebView, validate both scheme and host (allowlist domains). Any domains not in the allowlist should be opened by the default browser instead.

#### Don't load untrusted content

If possible, only load strictly scoped URLs and content owned by the app developer into WebView.

#### Don't expose sensitive data

If your application accesses sensitive data with a WebView, consider using the[`clearCache`](https://developer.android.com/reference/android/webkit/WebView#clearCache(boolean))method to delete any files stored locally, before using the JavaScript interface. You can also use server-side headers, such as no-store, to indicate that an application shouldn't cache particular content.

#### Don't expose sensitive functionalities

If your application requires sensitive permissions or collects sensitive data, ensure that it is called from code within the application and that prominent disclosure is provided to users. Avoid using JavaScript interfaces for any sensitive operations or user data.

#### Target API level 21 or higher

One secure way to use the`addJavascriptInterface`method is to target API level 21 or higher by ensuring the method is called only when running on API level 21 or higher. Before API 21, JavaScript could use reflection to access the public fields of an injected object.

*** ** * ** ***

## Risk: MessageChannel risks

Lack of origin control in`postWebMessage()`and`postMessage()`could allow attackers to intercept messages or send messages to native handlers.

### Mitigations

When setting up`postWebMessage()`or`postMessage()`, only allow messages from trusted domains by avoiding the use of \* as the target origin, and instead explicitly specify the expected sending domain.

*** ** * ** ***

## Resources

- [postMessage() best practices](https://fastercapital.com/content/Channel-messaging--Best-Practices-for-Implementing-Channel-Messaging-in-JavaScript.html)
- [addJavascriptInterface documentation](https://developer.android.com/reference/android/webkit/WebView#addJavascriptInterface(java.lang.Object,%20java.lang.String))
- [postMessage() documentation](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage#the_dispatched_event)
- [WebMessagePort.postMessage() documentation](https://developer.android.com/reference/android/webkit/WebMessagePort#postMessage(android.webkit.WebMessage))
- [WebViewClient.shouldInterceptRequest documentation](https://developer.android.com/reference/android/webkit/WebViewClient#shouldInterceptRequest(android.webkit.WebView,%20android.webkit.WebResourceRequest))
- [Documentation of security advice regarding addJavascriptInterface](https://developer.android.com/docs/quality-guidelines/core-app-quality#sc)
- [clearCache documentation](https://developer.android.com/reference/android/webkit/WebView#clearCache(boolean))
- [removeJavascript documentation](https://developer.android.com/reference/android/webkit/WebView#removeJavascriptInterface(java.lang.String))
- [enabling JavaScript in WebViews](https://developer.android.com/develop/ui/views/layout/webapps/webview#EnablingJavaScript)