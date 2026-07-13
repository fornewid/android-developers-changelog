---
title: https://developer.android.com/develop/ui/views/layout/webapps/handle-termination
url: https://developer.android.com/develop/ui/views/layout/webapps/handle-termination
source: md.txt
---

WebView runs its web content in a separate renderer process. Sometimes, this
process can be terminated. This happens if the system kills the renderer to
reclaim memory or if the process itself crashes. If you don't handle these
terminations, your app will exit too.

## Why handling process termination is critical

On lower versions of Android, users were less likely to notice an issue when an
app failed to handle renderer process termination. However, newer versions of
Android use more complex mechanisms to manage the resource consumption of
background processes. Consequently, if your app doesn't implement a handler for
[`onRenderProcessGone`](https://developer.android.com/reference/android/webkit/WebViewClient#onRenderProcessGone(android.webkit.WebView,%20android.webkit.RenderProcessGoneDetail)), it's now more likely that users will observe visible
foreground terminations when returning to the app. Implementing the Termination
Handling API is required to ensure your app recovers gracefully and maintains a
stable user experience.

## Use the Termination Handling API

You can handle these situations by overriding `onRenderProcessGone` in your
`WebViewClient`.

### Key requirements for recovery

To keep your app running after a renderer process terminates, each WebView in
your app must follow these rules:

- **Don't reuse the WebView instance.** Once the renderer is gone, that specific WebView object is useless. You must remove the WebView object from your view hierarchy, destroy it, and clear any references to it in your Activity or Fragment to avoid accidentally continuing to call methods on the destroyed WebView instance.
- **Create a new instance.** If you want to continue showing web content, you need a new WebView instance.
- **Return true.** Your implementation must return `true` to tell the WebView code you've handled the situation. If any `WebView` using that renderer process doesn't return `true`, WebView will kill or crash your app in correspondence with the renderer process exit reason.

## Implementation example

The following example shows how to handle these terminations within a complete
Activity. It uses `detail.didCrash()` to log whether the process crashed or if
the system killed the renderer to reclaim memory. Regardless of the cause, the
code cleans up by removing the dead WebView from the layout, destroying it,
and clearing the Activity's references to prevent [`NullPointerException`](https://developer.android.com/reference/java/lang/NullPointerException).
It then prepares a fresh instance and returns `true` so the app doesn't close.

**Note:** The following example always returns `true` to keep the app running.
If you specifically want your app to terminate when the WebView renderer
terminates, you can return `false` from this callback. However, we recommend
handling the recreation and returning `true` for a stable user experience.

    class MyWebViewActivity : AppCompatActivity() {

        private var webViewContainer: ViewGroup? = null
        private var myWebView: WebView? = null

        private var crashCount = 0
        private val MAX_CRASHES = 3

        // NEW FLAG: Tracks if the WebView crashed while the activity was hidden
        private var isWebViewPendingRecovery = false

        override fun onCreate(savedInstanceState: Bundle?) {
            super.onCreate(savedInstanceState)
            setContentView(R.layout.activity_my_web_view)
            webViewContainer = findViewById(R.id.my_web_view_container)

            initWebView()
        }

        // NEW LIFECYCLE HOOK: Triggers when the user brings the app back to the foreground
        override fun onResume() {
            super.onResume()
            // If a crash happened in the background, rebuild it now that the user can see it
            if (isWebViewPendingRecovery) {
                isWebViewPendingRecovery = false
                Log.i("MY_APP_TAG", "Activity resumed. Recovering pending WebView now.")
                recoverWebView()
            }
        }

        private fun initWebView() {
            val webView = WebView(this)
            myWebView = webView

            webViewContainer?.addView(webView)

            webView.webViewClient = object : WebViewClient() {
                override fun onRenderProcessGone(view: WebView, detail: RenderProcessGoneDetail): Boolean {
                    if (detail.didCrash()) {
                        Log.e("MY_APP_TAG", "The WebView rendering process crashed!")
                    } else {
                        Log.e("MY_APP_TAG", "System killed the WebView rendering process to reclaim memory.")
                    }

                    // Safely clean up the dead WebView
                    webViewContainer?.removeView(webView)
                    webView.destroy()
                    myWebView = null

                    // MODIFIED LOGIC: Check the lifecycle state of the Activity
                    // lifecycle.currentState.isAtLeast(Lifecycle.State.RESUMED) means the activity is visible and active
                    if (lifecycle.currentState.isAtLeast(Lifecycle.State.RESUMED)) {
                        Log.i("MY_APP_TAG", "Activity is in foreground. Recovering immediately.")
                        recoverWebView()
                    } else {
                        // The app is in the background. Mark it for later!
                        Log.w("MY_APP_TAG", "Activity is in background. Postponing recovery until user returns.")
                        isWebViewPendingRecovery = true
                    }

                    return true
                }
            }
            webView.loadUrl("https://www.example.com")
        }

        // HELPER FUNCTION: Extracted the recovery logic to reuse it
        private fun recoverWebView() {
            if (crashCount < MAX_CRASHES) {
                crashCount++
                Log.w("MY_APP_TAG", "Recovering WebView... Attempt $crashCount")
                initWebView()
            } else {
                Log.e("MY_APP_TAG", "WebView crashed too many times. Showing error UI.")
                showErrorUI()
            }
        }

        private fun showErrorUI() {
            // Example: Inflate an error view
        }

        override fun onDestroy() {
            super.onDestroy()
            myWebView?.let {
                webViewContainer?.removeView(it)
                it.destroy()
            }
            myWebView = null
        }
    }

## Important considerations

When implementing `onRenderProcessGone`, keep the following considerations in
mind to ensure app stability and maintain visibility into termination events:

- **Repeated crashes:** If a renderer crashes while loading a specific page, don't just reload the same page immediately. It might cause the new WebView to crash again.
- **Visibility:** App kills caused by missing this callback aren't yet reflected in Play Console crash reports. While future updates might address this gap, you must resolve these issues now to ensure app stability. Implementing this handler provides immediate visibility into why your app exits.