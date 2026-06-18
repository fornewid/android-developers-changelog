---
title: https://developer.android.com/develop/ui/compose/migrate/interoperability-apis/wrap-webview-in-compose
url: https://developer.android.com/develop/ui/compose/migrate/interoperability-apis/wrap-webview-in-compose
source: md.txt
---

To use a `WebView` in Jetpack Compose, you must wrap it in an `AndroidView`.
This guide explains common use cases and how to support them in Compose.

> [!WARNING]
> **Warning:** If you have complex use cases for `WebView`, we recommend not migrating that layout to use Compose until the Compose `WebView` equivalent is available. Follow the [issue](https://issuetracker.google.com/329866164) for more information and to track the progress of new API support.

## Wrap a WebView with AndroidView

To use a `WebView` in Compose, wrap it with an `AndroidView`:


```kotlin
@Composable
fun SimpleWebView(
    initialUrl: String,
    modifier: Modifier = Modifier
) {
    AndroidView(
        modifier = modifier.fillMaxSize(),
        factory = { context ->
            WebView(context).apply {
                webViewClient = WebViewClient()
                settings.javaScriptEnabled = true
                loadUrl(initialUrl)			
            }
        }
    )
}
```

<br />

This works for showing a simple URL within your app. However, `WebView` deals
with complex state lifecycles that are separate from the Android View
lifecycle and Compose lifecycle. Integrating Compose can introduce complex
`WebView` scenarios that result in difficult bugs. The following sections
describe use cases that may need specific handling to support those features.

## Persist WebView state

Handling configuration changes and navigation in Compose is challenging because
`WebView` is a legacy `View` bound to its host `Activity`, and it is
**not recommended** that its instance outlive the `Activity` lifecycle.

Therefore, the standard way to persist a `WebView`'s state is by allowing
`WebView` instances to be destroyed and recreated along with the `Activity`. You
can manually persist its internal navigation history and scroll state using a
`Bundle`.

> [!NOTE]
> **Note:** For apps with Compose-only activities, you should ideally avoid Activity recreation altogether by handling configuration changes in the manifest (see [Handle configuration changes](https://developer.android.com/guide/topics/resources/runtime-changes)). Handling changes directly improves performance and helps preserve the `WebView`'s internal state.


```kotlin
@Composable
fun PersistentWebView(url: String) {
    val webViewStateBundle = rememberSaveable { Bundle() }

    AndroidView(
        factory = { context ->
            WebView(context).apply {
                webViewClient = WebViewClient()
                settings.javaScriptEnabled = true

                // Restore the state and history
                if (webViewStateBundle.containsKey("WEBVIEW_STATE")) {
                    restoreState(webViewStateBundle.getBundle("WEBVIEW_STATE")!!)
                } else {
                    loadUrl(url)
                }
            }
        },
        onRelease = { releasedWebView ->
            // Save navigation history before the instance is destroyed
            val bundle = Bundle()
            releasedWebView.saveState(bundle)
            webViewStateBundle.putBundle("WEBVIEW_STATE", bundle)
        },
        modifier = Modifier.fillMaxSize()
    )
}
```

<br />

> [!CAUTION]
> **Caution:** While this approach persists navigation history and scroll state, the DOM state is lost when the `Activity` is recreated.

## Handle back navigation

When a `WebView` has navigation history, the system back gesture should navigate
backward within the `WebView` rather than exiting the screen.

Use the Compose [`BackHandler`](https://developer.android.com/reference/kotlin/androidx/activity/compose/BackHandler.composable) API to intercept the system back event, and
call the `WebView` `goBack()` function:


```kotlin
// ...
@Composable
fun BackNavigationDemoScreen(onBack: () -> Unit) {
    // Hold a reference to the WebView to check its history state
    var webViewReference by remember { mutableStateOf<WebView?>(null) }

    // Intercept the system back press if the WebView has history
    BackHandler(enabled = true) {
        val webView = webViewReference
        if (webView != null && webView.canGoBack()) {
            webView.goBack() // Go back in history
        } else {
            onBack() // Exit screen
        }
    }

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Back Navigation Demo") },
                navigationIcon = {
                    IconButton(onClick = onBack) {
                        Icon(Icons.AutoMirrored.Filled.ArrowBack, contentDescription = "Back")
                    }
                }
            )
        }
    ) { padding ->
        Column(modifier = Modifier.fillMaxSize().padding(padding)) {
            AndroidView(
                modifier = Modifier.fillMaxSize(),
                factory = { context ->
                    WebView(context).apply {
                        settings.javaScriptEnabled = true

                        // Keeps link navigations internal to the WebView instead of opening Chrome
                        webViewClient = WebViewClient() 

                        loadUrl("https://developer.android.com")
                        webViewReference = this
                    }
                },
                onRelease = {
                    webViewReference = null
                }
            )
        }
    }
}
```

<br />

This implementation provides browser-style navigation behavior.

## Nested scrolling

Nested scrolling is not easily supported when using `WebView` in Compose. When
placing a `WebView` inside a scrollable Compose container, such as a
`LazyColumn`, the `WebView` may consume all scroll gestures.
Since `WebView` relies on its own internal rendering engine, nesting it with
`LazyColumn` does not currently work properly.

To track the progress of official nested scrolling support for `WebView`, see
this [issue](https://issuetracker.google.com/issues/148731508).

## Edge-to-edge layouts and window insets

When using edge-to-edge layouts, `WebView` content may appear underneath system
bars such as the status bar. You can use the `windowInsetsPadding` modifier to
push the entire `WebView` into the safe area:


```kotlin
@Composable
fun EdgeToEdgeDemo(url: String) {
    AndroidView(
        modifier = Modifier
            .fillMaxSize()
            .windowInsetsPadding(WindowInsets.systemBars),
        factory = { context ->
            WebView(context).apply {
                loadUrl(url)
            }
        }
    )
}
```

<br />

For more information on insets, see [Understand window insets in WebView](https://developer.android.com/develop/ui/views/layout/webapps/understand-window-insets).

> [!NOTE]
> **Note:** If you control the website content, use the [CSS Safe Area variables](https://developer.android.com/develop/ui/views/layout/webapps/understand-window-insets#core-mechanics). The `WebView` engine automatically calculates the `env(safe-area-inset-top)` based on the device's status bar. Use this in your CSS to add safe padding in your layout.

## Synchronize app theme with WebView content

When the application switches between light and dark mode, `WebView` content can
update automatically without a page reload if handled correctly.

If you own the web page content, to synchronize colors with the app's theme,
handle the media query `prefers-color-scheme` to make sure your web page adapts
to the selected theme.

To enable native elements like dropdowns and popups to detect and match your app
theme, apply a `DayNight` style theme to your `Activity.`

<br />

```xml
<resources>

    <!-- ...
    <!-- Use a DayNight theme in your manifest to handle both modes automatically -->
    <style name="Theme.Webviewdemo.DayNight" parent="Theme.AppCompat.DayNight.NoActionBar" />
</resources>
```

<br />


```kotlin
@Composable
fun ThemeSyncDemo(onBack: () -> Unit) {
    val context = LocalContext.current
    AndroidView(
        modifier = Modifier.fillMaxSize(),
        factory = { _ ->
            WebView(context).apply {
                settings.javaScriptEnabled = true
                webViewClient = WebViewClient()
                val html = """
                            <html>
                            <head>
                                // ...


                                    @media (prefers-color-scheme: dark) {
                                        body {
                                            background-color: #212121;
                                            color: #ffffff;
                                        }
                                        select {
                                            border-color: #BB86FC;
                                            background: #212121;
                                            color: #ffffff;
                                        }
                                    }
                                </style>
                            </head>
                            // ...
                            </html>
                        """.trimIndent()
                loadDataWithBaseURL(null, html, "text/html", "UTF-8", null)
            }
        }
    )
} 
```

<br />

If the web page does not have a dark theme, or if you don't own the web content,
[algorithmic darkening](https://developer.android.com/develop/ui/views/layout/webapps/dark-theme#algorithmic-darkening) may help force a dark theme. Modern websites that
already have dark mode ignore this algorithm and use their own built-in styles
instead.

## Handle web permissions in Compose

When a web page requests hardware or data access (for example, camera,
microphone, or location), `WebView` triggers specific callbacks in its
`WebChromeClient`. You must handle these callbacks and ensure corresponding
Android runtime permissions are granted.

### Handle camera and microphone permissions

When a web page requests camera or microphone access (for example, WebRTC or
video recording), `WebView` calls `WebChromeClient.onPermissionRequest`.

However, before calling `grant()`, you must request the following Android
runtime permissions:

- `Manifest.permission.CAMERA`
- `Manifest.permission.RECORD_AUDIO`

First, define a permission handler for `WebView` that keeps track of the
`PermissionRequest` requested from `WebView`:


```kotlin
class WebViewPermissionHandler(
    private val launcher: ManagedActivityResultLauncher<Array<String>, Map<String, Boolean>>
) {
    var pendingRequest by mutableStateOf<PermissionRequest?>(null)
        private set

    fun handleRequest(request: PermissionRequest) {
        val isTrustedOrigin = request.origin.host == "www.trusted-domain.com" || request.origin.host == "app.local" // Always verify the origin before granting request


        if (!isTrustedOrigin) {
            Log.w("WebViewPermission", "Blocked and denied permission request from untrusted origin: ${request.origin.host}")
            request.deny()
            return
        }

        val androidPermissions = mutableListOf<String>()
        request.resources.forEach { resource ->
            when (resource) {
                PermissionRequest.RESOURCE_VIDEO_CAPTURE -> androidPermissions.add(Manifest.permission.CAMERA)
                PermissionRequest.RESOURCE_AUDIO_CAPTURE -> androidPermissions.add(Manifest.permission.RECORD_AUDIO)
            }
        }

        // Save the request and launch the Android system dialog
        pendingRequest = request
        launcher.launch(androidPermissions.toTypedArray())
    }

    fun onResult(results: Map<String, Boolean>) {
        val allGranted = results.values.all { it }
        Log.d("WebViewPermission", "Kotlin: All permissions granted? $allGranted")

        if (allGranted) {
            pendingRequest?.grant(arrayOf("/* list of permissions */"))
        } else {
            pendingRequest?.deny()
        }
        pendingRequest = null
    }
}
```

<br />

Next, create a composable that remembers the `WebViewPermissionHandler`. Use
`rememberLauncherForActivityResult` to request permissions:

> [!NOTE]
> **Note:** In production, the permission handler should also handle all the partial permission grants and denial use cases and provide UI feedback to the users. For more information, see [Request runtime permissions](https://developer.android.com/training/permissions/requesting).


```kotlin
@Composable
fun rememberWebViewPermissionHandler(): WebViewPermissionHandler {
    val handlerState = remember { mutableStateOf<WebViewPermissionHandler?>(null) }
    val launcher = rememberLauncherForActivityResult(
        ActivityResultContracts.RequestMultiplePermissions()
    ) { results ->
        handlerState.value?.onResult(results)
    }
    return remember {
        WebViewPermissionHandler(launcher).also { handlerState.value = it }
    }
}
```

<br />

Handle the permission from the `onPermissionRequest` callback. This launches the
permission launcher:


```kotlin
@Composable
fun WebViewPermissionScreen() {
    val permissionHandler = rememberWebViewPermissionHandler()

    AndroidView(
        factory = { context ->
            WebView(context).apply {
                settings.javaScriptEnabled = true

                webChromeClient = object : WebChromeClient() {
                    override fun onPermissionRequest(request: PermissionRequest) {
                        // Simply delegate to the handler
                        permissionHandler.handleRequest(request)
                    }
                }

		   // load a web page that needs permissions
            }
        },
        modifier = Modifier.fillMaxSize()
    )
}
```

<br />

> [!NOTE]
> **Note:** Handling geolocation permissions follows the same pattern shown in the preceding snippets. To support location access, override `WebChromeClient.onGeolocationPermissionsShowPrompt` instead of `onPermissionRequest`, and enable `WebView.settings.setGeolocationEnabled(true)`. Before invoking the callback, make sure your app requests the required runtime location permissions: `Manifest.permission.ACCESS_FINE_LOCATION` and `Manifest.permission.ACCESS_COARSE_LOCATION`.

## Alternative to an embedded WebView

If you prefer to avoid embedding `WebView`, Android provides other options for
displaying web content, like [Chrome Custom Tabs](https://developer.chrome.com/docs/android/custom-tabs/guide-get-started). See [Use web content
within your Android app](https://developer.android.com/develop/ui/views/layout/webapps) to understand how to choose the correct approach
for your use cases (like browsing or authentication).