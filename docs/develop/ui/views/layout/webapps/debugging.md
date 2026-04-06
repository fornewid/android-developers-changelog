---
title: Debug web apps  |  Views  |  Android Developers
url: https://developer.android.com/develop/ui/views/layout/webapps/debugging
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Views](https://developer.android.com/develop/ui/views/layout/declaring-layout)

# Debug web apps Stay organized with collections Save and categorize content based on your preferences.




Investigating the behavior of the code running in your WebView, also known as
debugging, is an essential part of developing Android applications that display
web content.

This section covers the following WebView debugging methodologies:

* [**JavaScript console logging**](/develop/ui/views/layout/webapps/debug-javascript-console-logs): If you're familiar with debugging web pages
  with Chrome DevTools or Safari Web Inspector, then you might be familiar with
  using `console` (such as `console.log()`). You can view console messages in
  Chrome DevTools or Logcat. Android's WebKit framework supports most of the
  same APIs, so you can receive logs from your web page when debugging in your
  [`WebView`](/reference/android/webkit/WebView).
* [**Chrome DevTools**](/develop/ui/views/layout/webapps/debug-chrome-devtools): Enables live remote inspection of HTML, CSS, and
  JavaScript code in your app's WebView using developer tools in the Chrome
  browser on your development machine.
* [**Access local server**](/develop/ui/views/layout/webapps/access-local-server): Serve content from a local web server on your
  development machine and access it from a WebView on a test device or emulator
  to quickly see your changes without deploying to a remote server.
* [**WebView DevTools app**](/develop/ui/views/layout/webapps/debug-webview-devtools-app): An on-device utility dedicated to device-wide
  configuration, command-line flag management, and crash analysis of Android's
  WebView component.

## Related resources

* [Remote debug Android devices](https://developer.chrome.com/docs/devtools/remote-debugging/)
* [Debug your app](/studio/debug)