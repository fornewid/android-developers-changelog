---
title: https://developer.android.com/develop/ui/views/layout/webapps/navigate
url: https://developer.android.com/develop/ui/views/layout/webapps/navigate
source: md.txt
---

[`WebViewCompat.navigate`](https://developer.android.com/reference/androidx/webkit/WebViewCompat#navigate(android.webkit.WebView,java.lang.String,androidx.webkit.NavigationParameters)) is an enhanced alternative to
[`WebView.loadUrl`](https://developer.android.com/reference/android/webkit/WebView#loadUrl(java.lang.String)) that provides fine-grained control over web page loading,
history management, and navigation lifecycle tracking in `WebView`.

Previously, initiating page navigations using `loadUrl` had notable limitations:

- **No history entry replacement:** You couldn't replace the current history entry, making it impossible to navigate to a new page without adding an entry to the back stack.
- **Decoupled callbacks:** There was no direct mechanism to correlate a specific `loadUrl` call with subsequent callback events in `WebViewClient`.
- **Extra headers not saved:** Custom headers passed to `loadUrl` were not saved as part of the `WebView` state, so they were lost when restoring state.

The `WebViewCompat.navigate` API resolves these issues by introducing the
following features:

- **Navigation history entry replacement:** Lets you replace the current page in the `WebView` history stack.
- **Correlated callback tracking:** Returns a [`Navigation`](https://developer.android.com/reference/androidx/webkit/Navigation) object that serves as a unique identifier across all stages of a navigation lifecycle.
- **Saved state header support:** Extra headers are reliably saved in the `WebView` state bundle so that they can be reused upon state restore.

## Key capabilities and limitations

Before adopting `WebViewCompat.navigate`, consider the following operational
rules and constraints:

- **Thread safety:** You must invoke `WebViewCompat.navigate` on the UI
  (main) thread.

- **Cancellation and precedence:** In-flight navigations cannot be explicitly
  cancelled. However, initiating a new `navigate` call on the same `WebView`
  supersedes any active navigation.

- **URI scheme support:** Standard (such as `https:` and `http:`) and custom
  URI schemes are supported. The `javascript:` scheme isn't supported.

- **URL size limit:** The maximum supported URL string length is 2 MB.

- **Feature check:** Always check feature availability using
  [`WebViewFeature.isFeatureSupported`](https://developer.android.com/reference/androidx/webkit/WebViewFeature#isFeatureSupported(java.lang.String)) before invoking the API to
  maintain compatibility across different WebView APK versions.

## Initiate navigation and track lifecycle

To configure navigation and track its lifecycle, do the following:

1. Register a [`NavigationListener`](https://developer.android.com/reference/androidx/webkit/NavigationListener) implementation using [`WebViewCompat.addNavigationListener`](https://developer.android.com/reference/androidx/webkit/WebViewCompat#addNavigationListener(android.webkit.WebView,androidx.webkit.NavigationListener)) during `WebView` setup to receive structured lifecycle callbacks. Register the listener once (rather than on every navigation call) to prevent memory leaks and duplicate callback executions.
2. Construct a [`NavigationParameters`](https://developer.android.com/reference/androidx/webkit/NavigationParameters) instance using [`NavigationParameters.Builder`](https://developer.android.com/reference/androidx/webkit/NavigationParameters.Builder) to specify optional behaviors, such as history replacement or custom HTTP headers.
3. Call [`WebViewCompat.navigate`](https://developer.android.com/reference/androidx/webkit/WebViewCompat#navigate(android.webkit.WebView,java.lang.String,androidx.webkit.NavigationParameters)), passing your `WebView` instance, the destination URL, and the parameters.

`WebViewCompat.navigate` returns a [`Navigation`](https://developer.android.com/reference/androidx/webkit/Navigation) object that uniquely
identifies the request. In your [`NavigationListener`](https://developer.android.com/reference/androidx/webkit/NavigationListener) callbacks, compare
this object with the incoming `Navigation` parameter to track that specific
navigation.

### Implementation example

The following example demonstrates how to configure navigation parameters,
invoke `WebViewCompat.navigate`, and listen for navigation lifecycle events:

### Kotlin

    class WebNavigationManager(private val webView: WebView) {
        // Track the navigation instance returned by the API
        private var currentNavigation: Navigation? = null

        init {
            // 1. Define listener to observe navigation lifecycle events
            val listener = object : NavigationListener {
                override fun onNavigationStarted(navigation: Navigation) {
                    if (navigation == currentNavigation) {
                        // Navigation started
                    }
                }

                override fun onNavigationRedirected(navigation: Navigation) {
                    if (navigation == currentNavigation) {
                        // Navigation encountered a redirect
                    }
                }

                override fun onNavigationCompleted(navigation: Navigation) {
                    if (navigation == currentNavigation) {
                        if (navigation.didCommit()) {
                            // Navigation committed successfully
                        } else if (navigation.didCommitErrorPage()) {
                            // Navigation committed an error page
                            val statusCode = navigation.statusCode
                            val error = navigation.webResourceError
                        }
                    }
                }

                override fun onFirstContentfulPaintMillis(page: Page, durationMillis: Long) {
                    // Match page with current navigation
                    if (page == currentNavigation?.page) {
                        // Page rendering started (First Contentful Paint achieved)
                    }
                }
            }

            // 2. Register listener on the main thread
            WebViewCompat.addNavigationListener(webView, listener)
        }

        @UiThread
        fun navigateToPage(url: String) {
            // Check feature availability
            if (!WebViewFeature.isFeatureSupported(WebViewFeature.WEBVIEW_NAVIGATE_EXPERIMENTAL_V1)) {
                // Fall back to standard loadUrl if navigate API is unavailable
                webView.loadUrl(url)
                return
            }

            // 3. Configure navigation parameters
            val params = NavigationParameters.Builder()
                .setShouldReplaceCurrentEntry(true)
                .addAdditionalHeaders(
                    mapOf("X-Test-Navigate-Header" to "TestValue")
                )
                .build()

            // 4. Initiate navigation on the UI thread
            currentNavigation = WebViewCompat.navigate(webView, url, params)
        }
    }

### Java

    public class WebNavigationManager {

        private Navigation mCurrentNavigation;
        private final WebView mWebView;

        public WebNavigationManager(@NonNull WebView webView) {
            mWebView = webView;
            setupListener();
        }

        private void setupListener() {
            // 1. Define listener to observe navigation lifecycle events
            NavigationListener listener = new NavigationListener() {
                @Override
                public void onNavigationStarted(@NonNull Navigation navigation) {
                    if (navigation.equals(mCurrentNavigation)) {
                        // Navigation started
                    }
                }

                @Override
                public void onNavigationRedirected(@NonNull Navigation navigation) {
                    if (navigation.equals(mCurrentNavigation)) {
                        // Navigation encountered a redirect
                    }
                }

                @Override
                public void onNavigationCompleted(@NonNull Navigation navigation) {
                    if (navigation.equals(mCurrentNavigation)) {
                        if (navigation.didCommit()) {
                            // Navigation committed successfully
                        } else if (navigation.didCommitErrorPage()) {
                            // Navigation committed an error page
                            int statusCode = navigation.getStatusCode();
                            WebResourceErrorCompat error = navigation.getWebResourceError();
                        }
                    }
                }

                @Override
                public void onFirstContentfulPaintMillis(@NonNull Page page, long durationMillis) {
                    if (mCurrentNavigation != null && page.equals(mCurrentNavigation.getPage())) {
                        // Page rendering started (First Contentful Paint achieved)
                    }
                }
            };

            // 2. Register listener on the main thread
            WebViewCompat.addNavigationListener(mWebView, listener);
        }

        @UiThread
        public void navigateToPage(@NonNull String url) {
            // Check feature availability
            if (!WebViewFeature.isFeatureSupported(WebViewFeature.WEBVIEW_NAVIGATE_EXPERIMENTAL_V1)) {
                // Fall back to standard loadUrl if navigate API is unavailable
                mWebView.loadUrl(url);
                return;
            }

            // 3. Configure navigation parameters
            NavigationParameters params = new NavigationParameters.Builder()
                .setShouldReplaceCurrentEntry(true)
                .addAdditionalHeaders(Collections.singletonMap(
                    "X-Test-Navigate-Header", "TestValue"
                ))
                .build();

            // 4. Initiate navigation on the UI thread
            mCurrentNavigation = WebViewCompat.navigate(mWebView, url, params);
        }
    }

## Failure modes and error handling

The `WebViewCompat.navigate` API provides distinct mechanisms for handling
configuration errors and runtime navigation failures:

### Invalid argument exceptions

Passing invalid arguments triggers a synchronous `IllegalArgumentException`.
Common causes include the following:

- Passing `null` for required non-null parameters (`webView`, `url`, or `params`).
- Supplying an unsupported URL scheme, such as `javascript:`.
- Passing malformed HTTP header keys or values that don't conform to RFC 2616 specifications.

### Navigation process errors

If a failure occurs during the network request or page load (such as a HTTP 404
status code, DNS resolution failure, or SSL error), `WebViewCompat.navigate`
still returns a valid [`Navigation`](https://developer.android.com/reference/androidx/webkit/Navigation) object.

When the navigation finishes, inspect the following methods on the `Navigation`
instance inside your [`onNavigationCompleted`](https://developer.android.com/reference/androidx/webkit/NavigationListener#onNavigationCompleted(androidx.webkit.Navigation)) callback to diagnose the
failure:

- [`getStatusCode`](https://developer.android.com/reference/androidx/webkit/Navigation#getStatusCode()): Returns the HTTP response status code (for example, `404` or `500`).
- [`getWebResourceError`](https://developer.android.com/reference/androidx/webkit/Navigation#getWebResourceError()): Returns a [`WebResourceErrorCompat`](https://developer.android.com/reference/androidx/webkit/WebResourceErrorCompat) object detailing network errors, such as connection timeouts or host lookup failures.
- [`didCommitErrorPage`](https://developer.android.com/reference/androidx/webkit/Navigation#didCommitErrorPage()): Indicates whether `WebView` committed and displayed an error page to the user.
- [`didCommit`](https://developer.android.com/reference/androidx/webkit/Navigation#didCommit()): Indicates whether the navigation successfully committed into a target page without being aborted.

## Save state bundle management

When you pass additional headers with `NavigationParameters`, `WebView` saves
these headers in its saved state bundle so that they can be reused upon state
restore. However, large collections of headers can substantially increase the
size of the saved state `Bundle`.

If you need to constrain bundle size to prevent `TransactionTooLargeException`
during Android state saves, use [`WebViewCompat.saveState`](https://developer.android.com/reference/androidx/webkit/WebViewCompat#saveState(android.webkit.WebView,android.os.Bundle,int,boolean)). This method
lets you set a maximum bundle size limit in bytes and optionally exclude forward
history items:

### Kotlin

    // Save state with a maximum bundle size limit (for example, 64 KB)
    val maxSizeBytes = 64 * 1024
    val includeForwardState = false
    val outState = Bundle()

    WebViewCompat.saveState(webView, outState, maxSizeBytes, includeForwardState)

### Java

    // Save state with a maximum bundle size limit (for example, 64 KB)
    int maxSizeBytes = 64 * 1024;
    boolean includeForwardState = false;
    Bundle outState = new Bundle();

    WebViewCompat.saveState(webView, outState, maxSizeBytes, includeForwardState);

The resulting bundle remains compatible with the standard
[`WebView.restoreState`](https://developer.android.com/reference/android/webkit/WebView#restoreState(android.os.Bundle)) method.

## Migration and implementation recommendations

To ensure optimal performance and stability when navigating in `WebView`,
follow these recommendations:

- **Migrate from `loadUrl` to `navigate`:** Migrate all legacy
  `WebView.loadUrl` calls to `WebViewCompat.navigate`. This ensures uniform
  history management and ensures headers are always saved as part of the
  saved state.

- **Always verify feature support:** Before invoking the API, confirm
  runtime support with `WebViewFeature.isFeatureSupported` to safeguard
  against older WebView versions.

- **Correlate navigation instances:** Use the returned `Navigation` object to
  differentiate concurrent navigations or filter callbacks when managing
  multiple `WebView` instances.

- **Register listener once during initialization:** Because
  `WebViewCompat.addNavigationListener` adds a listener rather than replacing
  an existing one, register your `NavigationListener` once during `WebView`
  setup to avoid memory leaks and duplicate callback executions across
  subsequent navigations.

- **Monitor save state size:** When passing large header payloads, use
  `WebViewCompat.saveState` with explicit size boundaries to avoid saving
  excessive state data.

## Additional resources

To learn more about embedded web capabilities and performance optimization, see
the following guides:

- [Simplify your WebView implementation with Jetpack Webkit](https://developer.android.com/develop/ui/views/layout/webapps/jetpack-webkit-overview)
- [Speculative loading in WebView](https://developer.android.com/develop/ui/views/layout/webapps/speculative-loading)
- [Optimize WebView startup](https://developer.android.com/develop/ui/views/layout/webapps/optimize-webview-startup)
- [Handle WebView renderer process termination](https://developer.android.com/develop/ui/views/layout/webapps/handle-termination)