---
title: https://developer.android.com/develop/ui/views/layout/webapps/embed-web-content-in-app
url: https://developer.android.com/develop/ui/views/layout/webapps/embed-web-content-in-app
source: md.txt
---

Android lets you build on the power of the web within your app. So, you can
benefit from the flexibility and efficiency of displaying certain types of
content.

## Embedding content using `WebView`

The [`WebView`](https://developer.android.com/reference/android/webkit/WebView) API gives you access to the capabilities of a mini-browser
for displaying web content within your app. This lets you provide web-powered
experiences as a core or supporting part within your app, as seen in **Figure
1**.
![Android app open to Google Play, with the primary web view highlighted in a red box](https://developer.android.com/static/develop/ui/views/layout/webapps/EmbedpageWebView.png) ![Android app open with supporting text inside a red box.](https://developer.android.com/static/develop/ui/views/layout/webapps/EmbedpageKids1.png) **Figure 1.** Web content embedded within the app with \`WebView\` objects as primary (left) and supporting content (right).

## What `WebView` can do

You can do the following with `WebView` in your app:

- **Embed web** : A `WebView` is integrated into an app's user interface as a
  component, much like a button or text field.

- **Load content** : `WebView` can load web content from various sources:

  - Remote URLs: It can fetch and display web pages from the internet, just like a regular browser.
  - Local files: It can load HTML, CSS, and JavaScript files stored within the app's resources.
  - Dynamically generated content: The app can generate HTML content dynamically and provide it to the `WebView`.
- **Render** : `WebView` uses its browser engine to parse and render the HTML,
  CSS, and JavaScript, displaying the resulting web page within its designated
  area in the app's UI.

- **Execute JavaScript** : `WebView` can execute JavaScript code within the
  context of the loaded web page. This allows for dynamic interactions and
  updates within the `WebView`.

- **Interact with your app** : This is where `WebView` gets more powerful. It
  enables bidirectional communication between the web page and the app.

  - **JavaScript to app code** : JavaScript code running in a `WebView` can call
    host APIs of the app, enabling access to device features like camera, GPS,
    or sensors.

  - **App code to JavaScript** : The app can also inject JavaScript code into a
    `WebView`, manipulate the web page's content, or respond to events triggered
    by the web page.

## How `WebView` differs from a browser

A `WebView` is a highly custom component that provides the core functionality of
a window into the web. Unlike a browser, which provides a navigation bar and
other user interface elements to navigate the web more broadly, the overall
experience of a `WebView` is shaped by your app's design and purpose.

To better understand how `WebView` differs from standard browsers, see the
following explanations:

**UI** : A `WebView` is used for displaying web content and doesn't have its own
header or UI like most other common browsers, for example, a home button,
address bar, or settings menu.

**Features**: Many browsers have built-in features to augment the
browsing experience, such as bookmarks, permissions, or history.

**Updates** : Because Android `WebView` is a system service on Android, updates
are pushed and integrated into the apps automatically on a monthly basis.
Browsers rely on their corresponding app updates and then for end users to apply
the update on their devices.

## Get started

For information on how to use `WebView` in your app, see the document
[Build web apps in `WebView`](https://developer.android.com/guide/webapps/webview).

### Additional resources

To develop web pages for Android-powered devices using `WebView` objects or
Custom Tabs, see the following documents:

- [Build web apps in `WebView`](https://developer.android.com/guide/webapps/webview)
- [Manage `WebView` objects](https://developer.android.com/guide/webapps/managing-webview)
- [Support different screens in web apps](https://developer.android.com/guide/webapps/targeting)
- [Debug web apps](https://developer.android.com/guide/webapps/debugging)
- [Best practices for web apps](https://developer.android.com/guide/webapps/best-practices)
- [Opt-in to `WebView` Beta](https://play.google.com/apps/testing/com.google.android.webview)
- [In-app browsing using embedded web](https://developer.android.com/develop/ui/views/layout/webapps/in-app-browsing-embedded-web)
- [Overview of Android Custom Tabs](https://developer.android.com/develop/ui/views/layout/webapps/overview-of-android-custom-tabs)