---
title: https://developer.android.com/privacy-and-security/risks/cross-app-scripting
url: https://developer.android.com/privacy-and-security/risks/cross-app-scripting
source: md.txt
---

# Cross-app scripting

<br />

**OWASP category:** [MASVS-CODE: Code Quality](https://mas.owasp.org/MASVS/10-MASVS-CODE)

## Overview

A WebView is an embedded browser component in Android applications that facilitates the display of web content within an app. It renders HTML, CSS, and JavaScript within the app's user interface.

Cross-App Scripting is broadly associated with the execution of malicious code in the context of a victim application. For the purposes of this documentation, the subject will be constrained specifically to the injection of malicious JavaScript code into a vulnerable WebView.

When an app accepts malicious JavaScript into a WebView without sufficient validation or sanitization, the application is vulnerable to cross-app Scripting.

## Impact

Cross-app scripting vulnerabilities can be exploited when attacker-controlled JavaScript content is passed to the vulnerable app's WebView without being validated or sanitized. As a result, the JavaScript code provided by the attacker is executed in the context of the victim application's WebView. The malicious JavaScript code can then use the same permissions as the victim app's, which may lead to theft of sensitive user data, and account hijacking.

## Mitigations

### Disable JavaScript

If your application does not require JavaScript, disabling it will ensure it does not become a threat:  

### Kotlin

    // Get the WebView Object
    val webView = findViewById<WebView>(R.id.webView)
    val webSettings = webView.settings

    // Disable JavaScript
    webSettings.javaScriptEnabled = false

### Java

    // Get the WebView Object
    WebView webView = (WebView) findViewById(R.id.webView);
    WebSettings webSettings = webView.getSettings();

    // Disable JavaScript for the WebView
    webSettings.setJavaScriptEnabled(false);

If your application does require JavaScript, ensure that you own or control any JavaScript passed to WebView. Avoid allowing WebView to execute arbitrary JavaScript, see the guidance in the next section.

### Ensure only expected content is loaded into WebView

When using methods like[`shouldOverrideUrlLoading()`](https://developer.android.com/reference/android/webkit/WebViewClient#shouldOverrideUrlLoading(android.webkit.WebView,%20android.webkit.WebResourceRequest)),[`loadUrl()`](https://developer.android.com/reference/android/webkit/WebView#loadUrl(java.lang.String)), or[`evaluateJavascript()`](https://developer.android.com/reference/android/webkit/WebView#evaluateJavascript(java.lang.String,%20android.webkit.ValueCallback%3Cjava.lang.String%3E))`,`make sure that any URLs passed to them are checked. As stated earlier, any JavaScript passed to the WebView should only come from expected domains, so it is important to verify what is being loaded.

Check OWASP's input validation[documentation](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)and this Android security[checklist](https://blog.oversecured.com/Android-security-checklist-webview/)for WebViews for good advice and examples.

### Set secure file access settings for WebView

Ensuring that files are not accessible can prevent arbitrary JavaScript from being executed within WebViews.The following[`WebSettings`](https://developer.android.com/reference/android/webkit/WebSettings)should be considered when securing file access:

- Disable file access. By default,[`setAllowFileAccess`](https://developer.android.com/reference/android/webkit/WebSettings#setAllowFileAccess(boolean))is set to`True`in API level 29 and lower which will permit access to local files. In API level 30 and higher the default is`False`. To ensure file access is not permitted, explicitly set`setAllowFileAccess`to`False`
- Disable content access. The default setting of[`setAllowContentAccess`](https://developer.android.com/reference/android/webkit/WebSettings#setAllowContentAccess(boolean))is`True`. Content URL access allows WebView to load content from a content provider installed in the system. If your app does not require content access, set`setAllowContentAccess`to`False`to prevent potential misuse in case of a cross-app scripting attack.

- kotlin`kotlin
  webView.settings.javaScriptEnabled = false
  webView.settings.domStorageEnabled = true
  webView.settings.allowFileAccess = false
  webView.settings.allowContentAccess = false`

- java`java
  webView.getSettings().setJavaScriptEnabled(false);
  webView.getSettings().setDomStorageEnabled(true);
  webView.getSettings().setAllowFileAccess(false);
  webView.getSettings().setAllowContentAccess(false);`

### Enable Safe Browsing

Enable Safe Browsing in[`AndroidManifest.xml`](https://developer.android.com/guide/topics/manifest/manifest-intro)to scan URLs passed to WebView for phishing or malicious domains.:  

    <meta-data android:name="android.webkit.WebView.EnableSafeBrowsing"
       android:value="true" />

## Resources

- [Safe Browsing documentation](https://developer.android.com/privacy-and-security/safetynet/safebrowsing)
- [WebView developer reference](https://developer.android.com/reference/android/webkit/WebView)
- [WebSettings for WebView developer reference](https://developer.android.com/reference/android/webkit/WebSettings)
- [setAllowFileAccess developer documentation](https://developer.android.com/reference/android/webkit/WebSettings#setAllowFileAccess(boolean))
- [setAllowContentAccess developer reference](https://developer.android.com/reference/android/webkit/WebSettings#setAllowContentAccess(boolean))