---
title: https://developer.android.com/develop/ui/views/layout/webapps/debugging
url: https://developer.android.com/develop/ui/views/layout/webapps/debugging
source: md.txt
---

Investigating the behavior of the code running in your WebView, also known as debugging, is an essential part of developing Android applications that display web content.

This section covers the following WebView debugging methodologies:

- [**JavaScript console logging**](https://developer.android.com/develop/ui/views/layout/webapps/debug-javascript-console-logs): If you're familiar with debugging web pages with Chrome DevTools or Safari Web Inspector, then you might be familiar with using`console`(such as`console.log()`). You can view console messages in Chrome DevTools or Logcat. Android's WebKit framework supports most of the same APIs, so you can receive logs from your web page when debugging in your[`WebView`](https://developer.android.com/reference/android/webkit/WebView).

- [**Chrome DevTools**](https://developer.android.com/develop/ui/views/layout/webapps/debug-chrome-devtools): Enables live remote inspection of HTML, CSS, and JavaScript code in your app's WebView using developer tools in the Chrome browser on your development machine.

- [**Access local server**](https://developer.android.com/develop/ui/views/layout/webapps/access-local-server): Serve content from a local web server on your development machine and access it from a WebView on a test device or emulator to quickly see your changes without deploying to a remote server.

- [**WebView DevTools app**](https://developer.android.com/develop/ui/views/layout/webapps/debug-webview-devtools-app): An on-device utility dedicated to device-wide configuration, command-line flag management, and crash analysis of Android's WebView component.

## Related resources

- [Remote debug Android devices](https://developer.chrome.com/docs/devtools/remote-debugging/)
- [Debug your app](https://developer.android.com/studio/debug)