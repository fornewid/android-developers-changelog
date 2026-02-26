---
title: https://developer.android.com/develop/ui/views/layout/webapps/in-app-browsing-embedded-web
url: https://developer.android.com/develop/ui/views/layout/webapps/in-app-browsing-embedded-web
source: md.txt
---

In-app browsers give your users a full web experience without making them leave
your app. Android offers two primary APIs for implementing in-app browsers:
[Custom Tabs](https://developer.android.com/develop/ui/views/layout/webapps/overview-of-android-custom-tabs) and [WebViews](https://developer.android.com/reference/android/webkit/WebView). Use an in-app browser when you
have a link or an ad that leads to a web page. You can open that page right
inside your app, as you can see in **Figure 1.**
![An in-app link in a red box, and an arrow pointing to another screen
showing the link opened with a custom tab.](https://developer.android.com/static/develop/ui/views/layout/webapps/InAppLinking1.png) **Figure 1.** Clicking on an in-app link (left) and opening an in-app browser using a Custom Tab (right).

Choosing between Custom Tabs and WebViews is a big architectural decision that
affects your development speed, user experience, and how much control you have
over the UI.

## Quick comparison

Use the following table to help you decide which tool fits your needs:

| Feature | WebView | Custom Tabs |
|---|---|---|
| **Primary use case** | Building hybrid apps with web as primary or supporting content, displaying ads, in-app campaigns, or terms of service pages. | Displaying content from external websites (like news articles or product pages). |
| **UI control** | **Full.** It is a `View` component you can place anywhere. You control all the surrounding UI. | **Limited.** You can theme the toolbar color and add a few custom actions. |
| **Data and sessions** | **Sandboxed.** It doesn't share cookies or logins with the user's main browser. | **Shared.** It uses the user's default browser session, including cookies and saved passwords. |
| **Native \<-\> Web bridge** | **Yes.** You can use a JavaScript bridge for deep, bidirectional communication between web content and native app code. | **Limited.** You can use the `https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage` method for basic string passing. |
| **Developer effort** | **High.** You need to manage the lifecycle, navigation, and performance yourself. | **Low.** You can implement it with just a few lines of code. |

> [!NOTE]
> **Note:** You can also choose to not use an in-app browser at all. Instead, use an [Android Intent](https://developer.android.com/guide/components/intents-filters) to link out of your app to the user's default browser. Doing so launches the browser and takes the user to the website in the user's default browser app. However, keep in mind that this approach takes users out of your app.

## WebView

A WebView is a view that makes web pages an integral part of your app's layout.
It is powerful, but it's a bit more complex to handle compared to Custom Tabs.

WebView can load remote or local web content, execute JavaScript, and enable
bidirectional communication between your web content and native app code. To
learn more about its capabilities, see [What WebView can do](https://developer.android.com/develop/ui/views/layout/webapps/embed-web-content-in-app#what-webview-can-do).

You can also use WebView to deliver a web application or display an online web
page as part of your app. For example, an end-user agreement that you need to
update periodically. To learn more, see [Build web apps in WebView](https://developer.android.com/develop/ui/views/layout/webapps/webview).

### Why you should choose WebView

The following are some scenarios where WebView is a good fit:

- **Hybrid apps:** You're building an app where web content and native components (like a navigation bar or a floating action button) live side-by-side.
- **First-party content:** Your web content is a core, interactive part of the app experience, like a document editor or a design canvas.
- **Full UI control:** You need to modify the contents of the web page itself or overlay native UI elements on top of it.
- **Deep analytics:** You need detailed insight into user engagement and activity within the web view.

### Key trade-offs

The following are some key trade-offs to consider when using WebView:

- **Performance:** WebView can be memory-intensive. If you don't manage it carefully, you can run into performance issues or ANRs (App Not Responding errors).
- **Security and maintenance:** You're responsible for hardening the security and managing the lifecycle. However, WebView updates roll out globally through Google Play, so you don't have to worry about the underlying engine getting outdated.

## Custom Tabs

Custom Tabs are a great choice for directing users to external URLs, as they
provide a fast, secure, and user-friendly browser window that slides over
your app.

### Why you should choose Custom Tabs

The following are some scenarios where Custom Tabs are a good fit:

- **External Links:** When a user taps a link to a website you don't own, Custom Tabs keep them in your app's context while providing a full browser experience.
- **Ease of integration:** It is the simplest way to get an embedded web experience up and running.
- **Shared state:** Because it shares cookies with the user's default browser, users don't have to sign in again to sites they have already visited.
- **Third-party sign-in:** They are well-suited for third-party sign-in flows (such as "Sign in with Google" or "Sign in with Facebook") as the browser handles credentials securely.

Although most browsers support Custom Tabs, some offer more customization than
others. For more information, see [Browser support](https://developer.chrome.com/docs/android/custom-tabs/browser-support).

## Use web content in Jetpack Compose

You can use both Custom Tabs and WebView when building with Jetpack Compose:

- **Custom Tabs:** Since Custom Tabs use an [`Intent`](https://developer.android.com/reference/android/content/Intent), you can launch them from any [`Context`](https://developer.android.com/reference/android/content/Context) in your Compose functions, making for a seamless integration.
- **WebView:** Compose doesn't have a native WebView composable yet, so you'll need to use [`AndroidView`](https://developer.android.com/reference/kotlin/androidx/compose/ui/viewinterop/package-summary#AndroidView(kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Function1)) to embed a standard WebView into your layout.

### Additional resources

To develop web pages for Android-powered devices using WebViews or Custom Tabs
APIs, see the following documents:

- [Embedding web content into your app as primary or supporting content](https://developer.android.com/develop/ui/views/layout/webapps)
- [API Reference: WebView](https://developer.android.com/reference/android/webkit/WebView)
- [Custom Tabs Overview](https://developer.android.com/develop/ui/views/layout/webapps/overview-of-android-custom-tabs)
- [Overview of Trusted Web Activities](https://developer.android.com/develop/ui/views/layout/webapps/trusted-web-activities)
- [Browser support](https://developer.chrome.com/docs/android/custom-tabs/browser-support)