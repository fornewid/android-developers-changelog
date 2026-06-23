---
title: https://developer.android.com/develop/ui/views/layout/webapps/optimize-webview-startup
url: https://developer.android.com/develop/ui/views/layout/webapps/optimize-webview-startup
source: md.txt
---

When your app first uses a WebView, the system performs specific startup tasks.
This startup process is heavy. By default, it happens implicitly on the UI
thread the first time the application calls many APIs within the
`android.webkit` or `androidx.webkit` packages, or inflates a layout that
contains a WebView tag.

## Why this matters

Because this implicit startup happens entirely on the main thread, it blocks
your app from processing user input and drastically increases the risk of
Application Not Responding (ANR) errors. For more information about how Android
handles the single-threaded execution model, see [Processes and threads
overview](https://developer.android.com/guide/components/processes-and-threads).

### Triggers for implicit startup

Implicit startup can be triggered in the following ways:

- **Programmatically** : Calling APIs like `WebSettings.getUserAgentString()`.
- **Using layouts** : Calling `setContentView()` or `layoutInflater.inflate()` on an XML resource that includes a `<WebView>`.

Implicit startup can also negatively affect your business metrics, such as [app
startup time](https://developer.android.com/topic/performance/vitals/launch-time) and time-to-first-display. If implicit initialization isn't
optimal for your app, use [`startUpWebView`](https://developer.android.com/reference/androidx/webkit/WebViewCompat#startUpWebView(android.content.Context,androidx.webkit.WebViewStartUpConfig,androidx.webkit.WebViewCompat.WebViewStartUpCallback)) instead.

This page discusses how to optimize WebView startup performance using the
`startUpWebView` API.

## Take control of WebView startup

To improve performance and minimize ANRs, use the `startUpWebView` API available
in the Jetpack Webkit library. This API gives you explicit control over when
WebView starts up. It shifts a significant amount of the startup workload to a
background thread and enables any work that must happen on the UI thread to be
done in chunks, rather than one big monolithic block. This frees up your UI
thread to handle other critical app tasks in parallel, reducing the chance of
blocking the user experience.

The API uses the `androidx.webkit.WebViewOutcomeReceiver` callback, letting you
track successful initializations.

To use this API, add the Jetpack Webkit library to your `build.gradle` file.
Ensure you use version 1.16.0 or higher:

    dependencies {
        implementation("androidx.webkit:webkit:1.16.0")
    }

## Use the `startUpWebView` API

How you optimize your startup flow depends on when your app actually needs to
display the WebView.

### When WebView isn't on the critical path

If your app doesn't need to load a WebView immediately, you can hide the
initialization cost completely. Call `startUpWebView` early in your app's
lifecycle and wait for the success callback to fire.

Ideally, you should wait for the callback before calling other WebView APIs. If
you trigger `startUpWebView` but don't wait for it to finish before touching
other WebView components, the system blocks the UI thread while waiting for the
initialization to complete. Your app might get some performance benefit from
the background work already completed, but not the maximum benefit.

### When WebView is on the critical path

If your app's core user journey requires a WebView immediately, you probably
can't afford to wait for WebView startup to complete. In this scenario, you
should still call `startUpWebView` as early as possible in the app lifecycle
(such as in [`Application.onCreate`](https://developer.android.com/reference/android/app/Application#onCreate())), but don't wait for the callback to
trigger. Instead, use WebView APIs directly when they are required.

To get the maximum benefit from asynchronous startup, crucially defer
instantiating a WebView or calling WebView APIs until there are no other
critical-path UI thread operations left to run (such as inflating layout
hierarchies, initializing other SDKs, or drawing the initial frame).

If you call `startUpWebView` and immediately invoke WebView APIs afterward on
the main thread, the UI thread blocks waiting for the initialization to catch
up. In this scenario, there is no performance benefit.

If WebView usage can become on the critical path but you don't want to startup
WebView entirely, you can choose to selectively run the WebView startup tasks
that are capable of running on a background thread, freeing up the UI thread for
other app critical tasks. For this, you can use
`shouldRunUiThreadStartUpTasks(false)`.

Later in your app's lifecycle, you can call `startUpWebView` again with
`shouldRunUiThreadStartUpTasks(true)` to finish the remaining startup tasks on
the UI thread. Whether you wait for the callback at that point depends on
whether WebView usage is on the critical path.

### Implementation example

The API uses the `androidx.webkit.WebViewOutcomeReceiver` callback, letting you
track successful initializations or handle diagnostic failures.

It is safe to call `startUpWebView` multiple times from different parts of your
app. We recommend that you avoid implementing a naive retry loop.

The following code sample demonstrates how to use the
`WebViewCompat.startUpWebView` API for asynchronous initialization.

### Kotlin

    import android.content.Context
    import android.util.Log
    import androidx.webkit.WebViewCompat
    import androidx.webkit.WebViewOutcomeReceiver
    import androidx.webkit.WebViewStartUpConfig
    import androidx.webkit.WebViewStartUpResult
    import androidx.webkit.WebViewStartupException
    import java.util.concurrent.Executors

    fun initializeWebView(context: Context) {
        // 1. Create a startup configuration specifying the background thread
        // that WebView will use to run its initialization tasks.
        val startUpConfig = WebViewStartUpConfig.Builder(
            Executors.newSingleThreadExecutor()
        ).build()

        // 2. Trigger WebView startup asynchronously
        WebViewCompat.startUpWebView(
            context,
            startUpConfig,
            object : WebViewOutcomeReceiver<WebViewStartUpResult, WebViewStartupException> {

                override fun onResult(result: WebViewStartUpResult) {
                    // Success: The WebView has finished its background initialization.
                    // This callback is guaranteed to be invoked on the UI thread.
                    setupWebView()
                }

                override fun onError(error: WebViewStartupException) {
                    // Failure: The initialization encountered a startup exception.
                    Log.e("WebViewStartup", "Failed to initialize WebView", error)
                }
            }
        )
    }

### Java

    import android.content.Context;
    import android.util.Log;
    import androidx.annotation.NonNull;
    import androidx.webkit.WebViewCompat;
    import androidx.webkit.WebViewOutcomeReceiver;
    import androidx.webkit.WebViewStartUpConfig;
    import androidx.webkit.WebViewStartUpResult;
    import androidx.webkit.WebViewStartupException;
    import java.util.concurrent.Executors;

    public void initializeWebView(Context context) {
        // 1. Create the startup configuration specifying the background thread pool
        // to handle internal non-UI initialization processes.
        WebViewStartUpConfig startUpConfig = new WebViewStartUpConfig.Builder(
                Executors.newSingleThreadExecutor()
        ).build();

        // 2. Trigger WebView startup asynchronously
        WebViewCompat.startUpWebView(
                context,
                startUpConfig,
                new WebViewOutcomeReceiver<WebViewStartUpResult, WebViewStartupException>() {

                    @Override
                    public void onResult(@NonNull WebViewStartUpResult result) {
                        // Success: The WebView has finished its background initialization.
                        // This callback is invoked directly on the UI thread.
                        setupWebView();
                    }

                    @Override
                    public void onError(@NonNull WebViewStartupException error) {
                        // Failure: Handled using the concrete WebViewStartupException
                        Log.e("WebViewStartup", "Failed to initialize WebView", error);
                    }
                }
        );
    }

## Debug asynchronous startup issues

If `startUpWebView` doesn't yield expected performance benefits, it's often
because WebView is being initialized implicitly elsewhere in your app before
your call executes. This could be due to the following reasons:

- **Third-party libraries** or SDKs initialized early in the app lifecycle.

- **`ContentProviders`** injected into your APK that trigger WebView APIs during
  app startup.

- **Layout inflations** or programmatic calls (like fetching user agent strings)
  that occur unexpectedly early.

To help you diagnose where and why these unexpected initializations are
happening, the `WebViewStartUpResult` object provides built-in auditing
capabilities:

- `getUiThreadBlockingStartUpLocations()`: Returns a list of `StartUpLocation`
  objects representing locations where WebView startup tasks blocked the main UI
  thread.

- `getNonUiThreadBlockingStartUpLocations()`: Returns specific call sites where
  running startup tasks blocked background threads.

Each `StartUpLocation` contains a stack trace that you can log or inspect to
find the exact class and method that triggered the initialization.

### Implementation example

You can inspect these locations inside your `onResult` callback to audit your
startup path:

    override fun onResult(result: WebViewStartUpResult) {
        // Check if WebView startup was blocked on the UI thread prior to or during initialization
        val uiBlockingLocations = result.getUiThreadBlockingStartUpLocations()
        if (!uiBlockingLocations.isNullOrEmpty()) {
            for (location in uiBlockingLocations) {
                // Log the stack trace of the call site that triggered the UI-blocking startup
                Log.w("WebViewDebug", "WebView startup blocked the UI thread here:", location.getStack())
            }
        } else {
            Log.i("WebViewDebug", "Excellent! No UI-blocking WebView startup detected.")
        }

        // Check where background initialization tasks were executed
        val backgroundLocations = result.getNonUiThreadBlockingStartUpLocations()
        backgroundLocations?.forEach { location ->
            Log.d("WebViewDebug", "WebView background startup occurred at: ${location.getStack()}")
        }

        setupWebView()
    }

## How to use this data during an audit

When auditing your app's WebView startup, use the following strategies to
analyze the diagnostic data and address performance bottlenecks:

- **Look for unexpected stack traces:** If
  `getUiThreadBlockingStartUpLocations()` isn't empty, look at the printed
  stack traces. If you see classes belonging to third-party SDKs or unexpected
  components, you have found an implicit initialization bottleneck.

- **Verify call order:** If your log outputs show that an implicit
  initialization occurred before your manual `startUpWebView` call, you should
  move your `startUpWebView` initialization earlier in your app or configure the
  offending SDK to delay its WebView-dependent tasks.

## Migrate from previous workarounds

In the past, you might have used explicit workarounds to force WebView
initialization on a background thread, such as fetching the user agent string.

These workarounds are considered unsupported practices, and their underlying
behavior can change in upcoming releases. If your app relies on any explicit,
undocumented workarounds to trigger or manage WebView startup, we recommend
using the `startUpWebView` API instead. The `startUpWebView` API works on all
versions of Android and WebView that are supported by the Jetpack Webkit
library.

Using the Jetpack Webkit implementation helps ensure consistent behavior across
the entire Android ecosystem. A key advantage of this API is its resilience: on
legacy devices where newer optimizations aren't available, the API maintains
performance parity with manual workarounds. This lets you adopt modern startup
benefits on newer devices without incurring a performance penalty on older ones.

If you encounter issues or have feedback about the `startUpWebView` API, file a
bug on the [public issue tracker](https://issuetracker.google.com/issues/new?component=460423).