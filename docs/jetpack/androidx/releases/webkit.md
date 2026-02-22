---
title: https://developer.android.com/jetpack/androidx/releases/webkit
url: https://developer.android.com/jetpack/androidx/releases/webkit
source: md.txt
---

# Webkit

[User Guide](https://developer.android.com/guide/webapps/managing-webview) API Reference  
[androidx.webkit](https://developer.android.com/reference/kotlin/androidx/webkit/package-summary)  
Work with modern WebView APIs on Android 5 and above.

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| February 11, 2026 | [1.15.0](https://developer.android.com/jetpack/androidx/releases/webkit#1.15.0) | - | - | [1.16.0-alpha02](https://developer.android.com/jetpack/androidx/releases/webkit#1.16.0-alpha02) |

## Declaring dependencies

To add a dependency on Webkit, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    implementation "androidx.webkit:webkit:1.15.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.webkit:webkit:1.15.0")
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:460423+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=460423&template=1157790)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 1.16

### Version 1.16.0-alpha02

February 11, 2026

`androidx.webkit:webkit:1.16.0-alpha02` is released. Version 1.16.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/adeb519268e4eeff7d0a5a9d024dbe26d88bb6ad..2e98d140740558dc55710bde96311d2e0e8d5cfd/webkit/webkit).

**New Features**

- Adds `Page#getUrl()` which returns the Url associated with the Page object ([I0a5d7](https://android-review.googlesource.com/#/q/I0a5d7f00b651348a65b62ee1d3e834c5699b97cb), [b/465339942](https://issuetracker.google.com/issues/465339942))
- Add `WebViewBuilder.applyTo` API for applying builder configurations to pre-constructed WebViews ([Iae133](https://android-review.googlesource.com/#/q/Iae133fb226068176af21b656456d314ccc4e127a), [b/463288296](https://issuetracker.google.com/issues/463288296))

### Version 1.16.0-alpha01

January 14, 2026

`androidx.webkit:webkit:1.16.0-alpha01` is released. Version 1.16.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f35ed15ba0388327d2b70a31d141da182ff721c8..adeb519268e4eeff7d0a5a9d024dbe26d88bb6ad/webkit/webkit).

**New Features**

- Added new Web Performance Metrics APIs `onFirstContentfulPaintMillis`, `onLargestContentfulPaintMillis` and `onPerformanceMarkMillis` to `NavigationListener`. These APIs allow developers to track FCP/LCP and performance marks directly in their app instead of using JavaScript to retrieve them. ([I50266](https://android-review.googlesource.com/#/q/I5026615a2d45896a134c0461da9a56205be2d013), [b/432696062](https://issuetracker.google.com/issues/432696062))
- Adds `NAVIGATION_LISTENER_NON_NULL_PAGE_FOR_SAME_DOCUMENT_NAVIGATIONS` to `WebViewFeature`, which can be used to determine whether [`Navigation#getPage`](https://developer.android.com/reference/androidx/webkit/Navigation#getPage()) will return null on same-document navigations. ([I3a2aa](https://android-review.googlesource.com/#/q/I3a2aa6a3e5a14390458cb397bb74c8cbcba4cb33))

**Bug Fixes**

- Correct nullability of string parameters in `getProfilesToLoadDuringStartup` ([Ic2ce5](https://android-review.googlesource.com/#/q/Ic2ce5ee0196899008b38c3276ce9484642350a7f))
- Expose missing `WebViewBuilder` feature check constant ([I95534](https://android-review.googlesource.com/#/q/I9553472758f8854c2853389f0aff3e457762be6f))

## Version 1.15

### Version 1.15.0

December 17, 2025

`androidx.webkit:webkit:1.15.0` is released. Version 1.15.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e0db6d8bb2835e53b913e6bf0a913b68f6aaf6d7..f35ed15ba0388327d2b70a31d141da182ff721c8/webkit/webkit).

**Important changes since 1.14.0**

This release increases the `minSdk` from API 21 to API 23. It also introduces the following new API capabilities:

- Access and set cookies as part of `shouldInterceptRequest` callbacks for WebView and Service Workers. App developers who currently access the `CookieManager` API as part of their `shouldInterceptRequest` can now instead enable cookie headers directly by calling [WebViewCompat#setCookiesIncludedInShouldInterceptRequest](https://developer.android.com/reference/androidx/webkit/WebSettingsCompat#setCookiesIncludedInShouldInterceptRequest(android.webkit.WebSettings,boolean)). This will then cause `WebView` to add a `Cookie` header to the [WebResourceRequest.getRequestHeaders()](https://developer.android.com/reference/android/webkit/WebResourceRequest#getRequestHeaders()) map which will be the exact cookies that apply to the request. This will also correctly handle any partitioned cookies. Apps can provide `Set-Cookie` header values through the newly added [WebResourceResponseCompat#setCookies](https://developer.android.com/reference/androidx/webkit/WebResourceResponseCompat#setCookies(java.util.List%3Cjava.lang.String%3E)) API. The `Set-Cookie` values added there will be processed by `WebView` as part of the response handling.
- Set custom request headers. The [Profile#addCustomHeader](https://developer.android.com/reference/androidx/webkit/Profile#addCustomHeader(androidx.webkit.CustomHeader)) API allows app developers to set a list of static header name-value pairs, which will be sent on any requests that match the specified origin pattern.
- Allow item customization in WebView hyperlink context menu. By calling [WebViewCompat#setHyperlinkContextMenuItems](https://developer.android.com/reference/androidx/webkit/WebSettingsCompat#setHyperlinkContextMenuItems(android.webkit.WebSettings,int)), app developers can specify which items appear in the context menu when a user long-presses a hyperlink.
- Trigger [prerendering](https://developer.chrome.com/docs/web-platform/prerender-pages). [WebViewCompat#prerenderUrlAsync](https://developer.android.com/reference/androidx/webkit/WebViewCompat#prerenderUrlAsync(android.webkit.WebView,java.lang.String,android.os.CancellationSignal,java.util.concurrent.Executor,androidx.webkit.PrerenderOperationCallback)) allows applications to speculatively prerender URLs before they are displayed in a `WebView`. Prerendering can dramatically improve loading performance by fetching the page ahead of time. When the user navigates to the URL, the prerendered page is displayed instantly.
- Control the specifics of the [BackForwardCache](https://developer.chrome.com/blog/back-forward-cache) in `WebView` by calling the [WebSettingsCompat#setBackForwardCacheSettings](http://setBackForwardCacheSettings) API. This API allows you to set the timeout in seconds or adjust the page cache limits.
- Finally, the removal of the `X-Requested-With` header in `WebView` has been canceled, and the header will again be sent on all requests. The [allowlist API](https://developer.android.com/reference/androidx/webkit/WebSettingsCompat#setRequestedWithHeaderOriginAllowList(android.webkit.WebSettings,java.util.Set%3Cjava.lang.String%3E)) is thus no longer necessary, and has been deprecated.

**Experimental APIs added since 1.14.0**

- The `WebView` library has also introduced a number of APIs that currently have experimental status. You can read more about these APIs in the [package summary](https://developer.android.com/reference/kotlin/androidx/webkit/package-summary#experimental-apis). If you have any feedback on these APIs, please share it either by sending an email to [android-webview-dev@chromium.org](mailto:android-webview-dev@chromium.org) or by submitting feedback in our [issue tracker](https://issuetracker.google.com/issues/new?component=460423).

The following features are experimental:

- [ProcessGlobalConfig#setUiThreadStartupMode](https://developer.android.com/reference/androidx/webkit/ProcessGlobalConfig#setUiThreadStartupMode(android.content.Context,int)) allows you to configure WebView's UI thread initialization. In particular, this will let you choose whether startup should run as a single task, or should be split into smaller tasks that yield control to the UI thread Looper.
- Create `WebView` instances with a restricted configuration that cannot be changed afterwards with the [WebViewBuilder](https://developer.android.com/reference/androidx/webkit/WebViewBuilder) API. Initially, this means that it is now possible to add JavaScript interface objects that are only injected in a specified list of origins, which greatly improves the security of using it. This will then also disable any further calls to `addJavascriptInterface` on the constructed `WebView` instance, which ensures an immutable configuration.
- Expanded on the [WebViewCompat#startUpWebView](https://developer.android.com/reference/androidx/webkit/WebViewCompat#startUpWebView(android.content.Context,androidx.webkit.WebViewStartUpConfig,androidx.webkit.WebViewCompat.WebViewStartUpCallback))API:
  - You can now specify a [set of profiles to load](https://developer.android.com/reference/androidx/webkit/WebViewStartUpConfig.Builder#setProfilesToLoadDuringStartup(java.util.Set%3Cjava.lang.String%3E)) synchronously. This allows app developers to skip loading any profiles at all, or specify the exact set of profiles the app uses, to ensure they are all loaded.
  - Debugging async startup is now easier by using the [getUiThreadBlockingStartUpLocations](https://developer.android.com/reference/androidx/webkit/WebViewStartUpResult#getUiThreadBlockingStartUpLocations()) and [getNonUiThreadBlockingStartUpLocations](https://developer.android.com/reference/androidx/webkit/WebViewStartUpResult#getNonUiThreadBlockingStartUpLocations()) callbacks to determine locations in the app where WebView startup blocks either the UI thread or a background thread.
  - You can configure how `WebView`'s [UI thread initialization](https://developer.android.com/reference/androidx/webkit/ProcessGlobalConfig#setUiThreadStartupModeV2(android.content.Context,int)) should be run.
- Warm up the renderer process for a Profile by calling [Profile#warmUpRendererProcess](https://developer.android.com/reference/androidx/webkit/Profile#warmUpRendererProcess()). This API can be used by applications with complex `WebView` lifecycles to ensure that the renderer process is running, even if all WebView instances have been destroyed.
- [Profile#addQuicHints](https://developer.android.com/reference/kotlin/androidx/webkit/Profile#addQuicHints(java.util.Set%3Cjava.lang.String%3E)) allows apps to tell `WebView` to prefer QUIC / HTTP3 when connecting to the provided origins.
- [Profile#preconnect](https://developer.android.com/reference/androidx/webkit/Profile#preconnect(java.lang.String)) allows apps to open a connection to an origin before navigating to it in order to speed up future loads.

**Experimental APIs updated since 1.14.0**

- The [Navigation Listener API](https://developer.android.com/reference/androidx/webkit/NavigationListener) has been updated to allow applications to [provide multiple listener instances](https://developer.android.com/reference/androidx/webkit/WebViewCompat#addNavigationListener(android.webkit.WebView,java.util.concurrent.Executor,androidx.webkit.NavigationListener)), which can optionally be configured with a custom Executor for background thread callbacks. This was previously the [WebNavigationClient API](https://developer.android.com/reference/androidx/webkit/WebViewCompat#setWebNavigationClient(android.webkit.WebView,androidx.webkit.WebNavigationClient)), which has been deprecated in favour of the new API. Additionally, this update also adds timing information to the [onFirstContentfulPaint](https://developer.android.com/reference/androidx/webkit/WebNavigationClient#onFirstContentfulPaint(androidx.webkit.Page)) callback, providing the time information from navigation start to the paint event.

### Version 1.15.0-rc01

December 03, 2025

`androidx.webkit:webkit:1.15.0-rc01` is released. Version 1.15.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4d752a0684fb1bf991cd0d15ebd3649ee8684ca1..1aba8258121ea0952dc94c1b5991fe73d388a8ad/webkit/webkit).

- There are no updates since `androidx.webkit:webkit:1.15.0-beta01`

### Version 1.15.0-beta01

November 19, 2025

`androidx.webkit:webkit:1.15.0-beta01` is released. Version 1.15.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4350deab5806bf95370a4d012d7eeaa70a10be44..4d752a0684fb1bf991cd0d15ebd3649ee8684ca1/webkit/webkit).

**API Changes**

- Add experimental `WebViewBuilder` APIs ([I06828](https://android-review.googlesource.com/#/q/I06828bd759fd3db1aef3ae480f000f964d182002), [b/409740828](https://issuetracker.google.com/issues/409740828))
- Add `UiThreadStartupMode` for async startup that stops `isMultiProcessEnabled()` call from startup up Chromium ([I524ee](https://android-review.googlesource.com/#/q/I524ee59f8aff57b6b614ae2dd3c35ac99751edf2), [b/397372092](https://issuetracker.google.com/issues/397372092))
- Hiding `UserAgent` form factor until 1.16 release ([Ibac8a](https://android-review.googlesource.com/#/q/Ibac8af4262df78af948c855c5c081406e084ff45), [b/430554841](https://issuetracker.google.com/issues/430554841), [b/454438418](https://issuetracker.google.com/issues/454438418))
- Update navigation API to allow applications to provide `NavigationListener` instances, which can optionally be configured with a custom Executor for background thread callbacks. Multiple `NavigationListener` instances can now be added to a single `WebView`.  
  Additionally, this update also adds timing information to the `onFirstContentfulPaint` callback, providing the time information from navigation start to the paint event. ([I6aa8e](https://android-review.googlesource.com/#/q/I6aa8e92eba43e5785309afec4cd2de2cc43d4c32), [b/448580228](https://issuetracker.google.com/issues/448580228))
- Adds `Profile#addQuicHints` which allows apps to tell `WebView` to prefer QUIC / HTTP3 when connecting to the provided origins. ([I8e364](https://android-review.googlesource.com/#/q/I8e36486c3a7188eae0d3c6d59494a1d00a600003), [b/445339041](https://issuetracker.google.com/issues/445339041))
- Updated feature constants with experimental annotations, and updated library README with more information about experimental APIs. ([I1b914](https://android-review.googlesource.com/#/q/I1b914f362b82a65518cfff78ce0f319b67911054))

**Bug Fixes**

- Releasing `androidx.webkit:webkit:1.15.0-beta01` ([I0b1bd](https://android-review.googlesource.com/#/q/I0b1bdeb1a49baa0dbe7d78beb4d6ce3397977782), [b/417241552](https://issuetracker.google.com/issues/417241552))

### Version 1.15.0-alpha03

October 08, 2025

`androidx.webkit:webkit:1.15.0-alpha03` is released. Version 1.15.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cd8ce2bdb21194a81a76325a8e65dad5d7e28681..4350deab5806bf95370a4d012d7eeaa70a10be44/webkit/webkit).

**API Changes**

- Introduces a new API to set custom request headers. This is an iteration on the previous experimental API, and now allows the application to set multiple values for each header, each mapped to a different set of origin patterns. The new API also allows the application to inspect the configured headers. ([Id7d30](https://android-review.googlesource.com/#/q/Id7d30b9a4a8b6c0eab21f081e2ba3d3dea21d0dd), [b/419469873](https://issuetracker.google.com/issues/419469873), [b/429269470](https://issuetracker.google.com/issues/429269470))
- Removal of the X-Requested-With header in `WebView` has been cancelled, and the header will again be sent on all requests by default. The allowlist API is no longer necessary, and has been deprecated. ([I884c3](https://android-review.googlesource.com/#/q/I884c3108ca9632273953fe34e800ec2299d5b6ac), [b/447094379](https://issuetracker.google.com/issues/447094379))
- Add a new API to `WebSettingsCompat` to allow developers to configure `WebView`'s back-forward cache, such as setting the timeout in seconds or page cache limits. ([I642b2](https://android-review.googlesource.com/#/q/I642b28af6201473584001d8987072ae8b80ac9af), [b/432395269](https://issuetracker.google.com/issues/432395269))
- Add `HyperlinkContextMenu` API to allow item customisation in `WebView` hyperlink context menu ([Idb809](https://android-review.googlesource.com/#/q/Idb809ae860d33e08371bff1a86bd769d103f01e8), [b/382654667](https://issuetracker.google.com/issues/382654667))
- Add `getAsyncStartUpLocations` API for debugging cases where `WebView` was started up asynchronously without using the `startUpWebView` API. ([I6bf4b](https://android-review.googlesource.com/#/q/I6bf4bd21d02a243bac3a85e96198bec5c4265e3a), [b/417434566](https://issuetracker.google.com/issues/417434566))

### Version 1.15.0-alpha02

August 27, 2025

`androidx.webkit:webkit:1.15.0-alpha02` is released. Version 1.15.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1b437892629a2cdedb46d9b7232575987b2cc6b5..cd8ce2bdb21194a81a76325a8e65dad5d7e28681/webkit/webkit).

**New Features**

- Adds `Profile#preconnect` which allows apps to open a connection to an origin before navigating to it in order to speed up future loads. ([I8db41](https://android-review.googlesource.com/#/q/I8db410905622dea61d31322d4ad88afe30dccabc))
- A new [`prerenderUrlAsync`](https://developer.android.com/reference/androidx/webkit/WebViewCompat#prerenderUrlAsync(android.webkit.WebView,java.lang.String,android.os.CancellationSignal,java.util.concurrent.Executor,androidx.webkit.PrerenderOperationCallback)) API has been added to `WebViewCompat`, allowing applications to speculatively prerender URLs before they are displayed in a WebView.  
  Prerendering can dramatically improve loading performance by fetching the page ahead of time. When the user navigates to the URL, the prerendered page is displayed instantly.  
  These APIs were previously released as experimental, and can now be used without the `@OptIn` annotation. ([Ie14f5](https://android-review.googlesource.com/#/q/Ie14f5e58ccf53e28bfbf63a0e071d62f991b9a70))
- You can now specify a set of profiles to load synchronously when calling the `startUpWebView` API. This is configured by passing the profile names to a new method in `WebViewStartUpConfig.Builder` ([I9a6e6](https://android-review.googlesource.com/#/q/I9a6e6a25f3f19d79a6b5a5bbbfbe2214559acf9c))
- Add a new API to `WebSettingsCompat` to enabled/disable [BackForwardCache](https://developer.chrome.com/blog/back-forward-cache) on the `WebSettings` object. This API was previously released as experimental, and can now be used without the `@OptIn` annotation. ([Ie413b](https://android-review.googlesource.com/#/q/Ie413ba37340e467e8949d2281b6bd313fc4b3a0d))
- Add support for overriding User-Agent form factors, The `UserAgentMetadata` class has new methods to get and set user-agent metadata form factors. The `UserAgentMetadata.Builder` has a new `setFormFactors()` method for overriding the `Sec-CH-UA-Form-Factors` User-Agent client hint. The current override values can be retrieved via the new `getFormFactors()` method. ([I6d08c](https://android-review.googlesource.com/#/q/I6d08c9c7403bead863182cbbde93fcae809d2d9f), [b/430554841](https://issuetracker.google.com/issues/430554841))

**API Changes**

- Add API to `ProcessGlobalConfig` to configure `WebView`'s UI thread initialization ([I5e85a](https://android-review.googlesource.com/#/q/I5e85a13fd0e0378bcb09b1f9ddc2d2510a3a2018), [b/433273850](https://issuetracker.google.com/issues/433273850), [b/397372092](https://issuetracker.google.com/issues/397372092))
- Add a new feature name for `WebViewStartupConfig.Builder#setProfilesToLoadDuringStartup` API ([I36451](https://android-review.googlesource.com/#/q/I36451e15092610c874e99e9a7d209a79438ed0ae))
- Moving the default minSdk from API 21 to API 23 ([Ibdfca](https://android-review.googlesource.com/#/q/Ibdfca5942dbb414ca07594ba240093db14aad4df), [b/380448311](https://issuetracker.google.com/issues/380448311), [b/435705964](https://issuetracker.google.com/issues/435705964), [b/435705223](https://issuetracker.google.com/issues/435705223))
- Update origin matched header API to allow overwriting header values by calling `setOriginMatchedHeader` multiple times for the same header name. Also adds a new `hasOriginMatchedHeader` method to check if the header name is already in use.  
  This change also marks the API as experimental, as it currently only supports setting a single value and origin mapping for each header value, and it will likely undergo changes in the future to make it support multiple values mapped to different origins. ([I03365](https://android-review.googlesource.com/#/q/I033651e3ea50a4263da7438f7522af7052a85ec5), [b/419469873](https://issuetracker.google.com/issues/419469873), [b/429269470](https://issuetracker.google.com/issues/429269470))
- The UI thread requirement for `Profile#prefetchUrlAsync()` has been removed. It can now be called from any thread. ([I83d57](https://android-review.googlesource.com/#/q/I83d5761e5d2384b66415d770bf0c0dfc54d299be))
- The `OutcomeReceiverCompat` interface has been removed in favor of the official `androidx.core.os.OutcomeReceiverCompat` version. The library now requires `compileSdk` 35 or higher. ([Ie1ea5](https://android-review.googlesource.com/#/q/Ie1ea50e6945402b245416145048213d389c2159e))
- Renames `[is/set]IncludeCookiesOnShouldInterceptRequestEnabled` to `[are/set]CookiesIncludedInShouldInterceptRequest` in `WebSettingsCompat`. ([Ife9e9](https://android-review.googlesource.com/#/q/Ife9e9932b14fd630f41f67168c78c852d4e46a86), [b/428924452](https://issuetracker.google.com/issues/428924452))
- Adding experimental API annotations to `Profile.ExperimentalUrlPrefetch` that had previously been omitted. ([Ic54eb](https://android-review.googlesource.com/#/q/Ic54eb7fc6176a032820f13cf46627d76197e2cc7), [b/417458061](https://issuetracker.google.com/issues/417458061))

### Version 1.15.0-alpha01

July 2, 2025

`androidx.webkit:webkit:1.15.0-alpha01` is released. Version 1.15.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e0db6d8bb2835e53b913e6bf0a913b68f6aaf6d7..1b437892629a2cdedb46d9b7232575987b2cc6b5/webkit/webkit).

**New Features**

- A new API to set HTTP header name-value pairs on requests to specific origins.  
  The `Profile.setOriginMatchedHeader` method lets the application specify that the header name and value should be set on all HTTP/HTTPS requests to the origins that match the provided allowlist when sent from WebViews and service workers that use the given Profile. The API only allows a single mapping for each header name, and will throw an exception if the header name is already set.  
  Use `Profile.clearOriginMatchedHeader` to remove an existing mapping, and `Profile.clearAllOriginMatchedHeaders` to remove all mappings. ([Ida7f1](https://android-review.googlesource.com/#/q/Ida7f131d30731734b9ca29f9e67fca95f9a429d3), [b/419469873](https://issuetracker.google.com/issues/419469873))
- A new API to access and set cookies as part of `shouldInterceptRequest` callbacks for WebView and Service Workers.  
  App developers who currently access the `CookieManager` API as part of their `shouldInterceptRequest` can now enable cookie headers directly by calling `setIncludeCookiesOnShouldInterceptRequest`. This will then cause WebView to add a `Cookie` header to the [WebResourceRequest.getRequestHeaders()](https://developer.android.com/reference/android/webkit/WebResourceRequest#getRequestHeaders()) map which will be the exact cookies that apply to the request. This will also correctly handle any partitioned cookies.  
  Apps can provide `Set-Cookie` header values through the newly added `WebResourceResponseCompat.setCookies` API. The `Set-Cookie` values added there will be processed by WebView as part of the response handling. ([Idbfd1](https://android-review.googlesource.com/#/q/Idbfd14469ebc1eb0278a3eae3ea18ee4272cb2c6), [b/414769380](https://issuetracker.google.com/issues/414769380))
- A new experimental API to warm up the renderer process for a `Profile`.  
  This API can be used by applications with complex WebView lifecycles to ensure that the renderer process is running, even if all WebView instances have been destroyed. ([Ia8fc8](https://android-review.googlesource.com/#/q/Ia8fc858b9b26de3abe9168c47e82cf382638cd05))

**API Changes**

- Add a new method to the experimental [Navigation](https://developer.android.com/reference/androidx/webkit/Navigation) interface to provide the URL of the navigation. ([I1c6c0](https://android-review.googlesource.com/#/q/I1c6c0ee582cb4a6855adc9cd224569fc8bef4aef))
- Update the Profile Prefetch feature name to clarify that the Prefetch API can now be invoked on a background thread. ([I7c83a](https://android-review.googlesource.com/#/q/I7c83ad4effc502e1b19cc4b44e608f5e42bbe793))

## Version 1.14

### Version 1.14.0

June 4, 2025

`androidx.webkit:webkit:1.14.0` is released. Version 1.14.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/dca78d01925c289445e3fc462a376b774107cbbc..e0db6d8bb2835e53b913e6bf0a913b68f6aaf6d7/webkit/webkit).

**Important changes since 1.13.0**

- Introducing the `PaymentRequest` API for invoking Android native payment apps through `org.chromium.intent.action.PAY` intent. `PaymentRequest` is disabled by default and `WebView` host apps can call [WebSettingsCompat.setPaymentRequestEnabled(settings, true)](https://developer.android.com/reference/androidx/webkit/WebSettingsCompat#setPaymentRequestEnabled(android.webkit.WebSettings,boolean)) to enable it. In addition, `PaymentRequest` requires a `<queries>` tag in `AndroidManifest.xml`. See documentation for `setPaymentRequestEnabled()` for more information.
- Introducing the experimental Navigation API for enhanced web navigation tracking and management within `WebView`. These APIs provide detailed information about navigation events. Get started by calling [WebViewCompat.setNavigationClient](https://developer.android.com/reference/androidx/webkit/WebViewCompat#setWebNavigationClient(android.webkit.WebView,androidx.webkit.WebNavigationClient)) with an implementation of the new [WebNaviagationClient](https://developer.android.com/reference/androidx/webkit/WebNavigationClient) interface to get detailed information about page navigation. For more information about the navigation lifecycle, please see the [Life of a Navigation Presentation](https://docs.google.com/presentation/d/1YVqDmbXI0cllpfXD7TuewiexDNZYfwk6fRdmoXJbBlM).

### Version 1.14.0-rc01

May 20, 2025

`androidx.webkit:webkit:1.14.0-rc01` is released. Version 1.14.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6c541571b9fb5471f965fc52612cb280713e5e4..dca78d01925c289445e3fc462a376b774107cbbc/webkit/webkit).

- There are no changes from `1.14.0-beta01`.

### Version 1.14.0-beta01

May 7, 2025

`androidx.webkit:webkit:1.14.0-beta01` is released. Version 1.14.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4c37298a97c16270c139eb812ddadaba03e23a52..b6c541571b9fb5471f965fc52612cb280713e5e4/webkit/webkit).

**API Changes**

- Add context as parameter to `startUpWebView()` API ([Ic29cd](https://android-review.googlesource.com/#/q/Ic29cd0d73e64927eb4ad207919e18f14d0259798), [b/406701301](https://issuetracker.google.com/issues/406701301))

### Version 1.14.0-alpha01

April 9, 2025

`androidx.webkit:webkit:1.14.0-alpha01` is released. Version 1.14.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/41a38e8ec90b022b61301d545a235195bc6a6f9a..4c37298a97c16270c139eb812ddadaba03e23a52/webkit/webkit).

**New Features**

- Introducing the `PaymentRequest` API for invoking Android native payment apps through `org.chromium.intent.action.PAY` intent. `PaymentRequest` is disabled by default and WebView host apps can call `WebSettingsCompat.setPaymentRequestEnabled(settings, true)` to enable it. In addition, `PaymentRequest` requires a `<queries>` tag in `AndroidManifest.xml`. See documentation for `setPaymentRequestEnabled()` for more information. ([I3304e](https://android-review.googlesource.com/#/q/I3304e1745c01af08db25e4367fb579a388d496ea), [b/404920055](https://issuetracker.google.com/issues/404920055))
- Introducing Experimental Navigation Callbacks. This release introduces experimental APIs for enhanced web navigation tracking and management within `WebView`. These APIs provide detailed information about navigation events. Key Features:
  - `WebNavigationClient` Interface: Introduces a new interface, `WebNavigationClient`, with callbacks for navigation events:
  - `onNavigationStarted(Navigation navigation)`: Notifies when a navigation begins.
  - `onNavigationRedirected(Navigation navigation)`: Notifies when a navigation is redirected.
  - `onNavigationCompleted(Navigation navigation)`: Notifies when a navigation completes.
  - `Navigation` Interface: Provides detailed information about a navigation, including: URL, page initiation status, same-document status, reload status, history status, back/forward status, commit status, error page status, status code, and session restore status. The `Navigation` object serves as a unique identifier for each navigation, allowing developers to correlate related navigation events.
  - `Page` class: Introduces the `Page` class, which serves as a key for page-associated data. ([I351a6](https://android-review.googlesource.com/#/q/I351a6012bdba52adecacda05ebf9b5d6d53b1eae))
- Introduce a new experimental API to toggle the behaviour of caching provider objects. ([I14636](https://android-review.googlesource.com/#/q/I146361a920334de704be30bcc46569076516203e))

**API Changes**

- Updated the `PROFILE_URL_PREFETCH` feature value in `WebViewFeature`. ([I606fd](https://android-review.googlesource.com/#/q/I606fd63c5425e96d196a72d5469c05a893669ac6))
- Adds `WebViewCompat#saveState`, akin to `WebView#saveState`, but allows restricting the size of the returned state and deciding whether or not to save forward history entries. ([Iea7d6](https://android-review.googlesource.com/#/q/Iea7d6f518e58aaf4c6e518c85c65271608904561))
- Add `maxPrerenders` config to `SpeculativeLoadingConfig` API ([I67245](https://android-review.googlesource.com/#/q/I67245b2f422f413b92829f7f6ea234bfd9390f74))

## Version 1.13

### Version 1.13.0

March 12, 2025

`androidx.webkit:webkit:1.13.0` is released. Version 1.13.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/36051bdca2a2e600277c429b62ab94b263a4c49b..41a38e8ec90b022b61301d545a235195bc6a6f9a/webkit/webkit).

**Important changes since 1.12.0**

- Introduce a new experimental API for Url prerendering to allow developers to speculative prerender candidate urls resulting in faster navigations. ([I0cfe7](https://android-review.googlesource.com/#/q/I0cfe7ac389969422e56721db7a0cf67d6739d5af))
- Introducing a set of new APIs to delete browsing data stored by `WebView`. The new APIs in `WebStorageCompat` should be preferred over the existing APIs in `android.webkit.WebStorage`, as they will guarantee deletion of all local storage, including the network cache and cookies, as well as any installed service workers. If new storage APIs are introduced in the future, then these new methods will be updated to include them in the storage deleted. ([Iad54f](https://android-review.googlesource.com/#/q/Iad54f46e2fbb2a7369f2b7191519af0b10525ed7), [b/382273208](https://issuetracker.google.com/issues/382273208))
- Add `setPartitionedCookiesEnabled` API. This will allow developers to enable and disable partitioned cookies in `WebView`. ([Ic506a](https://android-review.googlesource.com/#/q/Ic506a23471946d31b797397e2f71aef0f3ae481a), [b/364904765](https://android-review.googlesource.com/#/q/Ic506a23471946d31b797397e2f71aef0f3ae481a))
- Add socket tagging API to `WebView` for accounting of `WebView`'s network traffic using `NetworkStatsManager`/`TrafficStats`. This feature will only be available from `WebView` M133. ([Ica441](https://android-review.googlesource.com/#/q/Ica4412c9432ff479ea728c30c09b1d7bf359d0f0), [b/374932688](https://issuetracker.google.com/issues/374932688))
- Add experimental `WebView` async startup API. ([I94b8a](https://android-review.googlesource.com/#/q/I94b8a3f0c6e11f9e9d157e162173db06d33fae94))
- URL Prefetching in Profile: Introduced a new API in `Profile` to allow developers to trigger URL prefetching. Prefetch Clearing: Added an API to clear ongoing prefetches.([I42c5c](https://android-review.googlesource.com/#/q/I42c5c282a7114b8b72e62b2b24f917a0f9b47123))
- Deprecate `WebView.startSafeBrowsing`. ([If5626](https://android-review.googlesource.com/#/q/If5626d9f0bac4f1b04ee9a8f4ebc7f48598c9dac))

### Version 1.13.0-rc01

February 26, 2025

`androidx.webkit:webkit:1.13.0-rc01` is released. This release contains no changes from the `1.13.0-beta01`release.

### Version 1.13.0-beta01

February 12, 2025

`androidx.webkit:webkit:1.13.0-beta01` is released. Version 1.13.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ad66672b42ec1e9359219e82b7f8189d03df40f5..24c00eb294d9cda579d8d6e48a29497fe0f8d3f7/webkit/webkit).

**API Changes**

- Add Async suffix to prerender API. Rename any Data to Header in `NoVarySearch` to reflect the new name. ([Ie91c9](https://android-review.googlesource.com/#/q/Ie91c92f6b475f07fb903fbef5cac202336082849))
- Add executor parameter to the url prerendering API. Also, restricting the API to be called only from the UI thread. ([I50520](https://android-review.googlesource.com/#/q/I505202159a24e7d5ba494ed1075422c6b0800fbc))
- Add an API to configure cache config for the profile prefetch requests. It also applies to Prerender requests initiated from `WebViews` associated with this Profile. ([Iebb6e](https://android-review.googlesource.com/#/q/Iebb6e3e3c0787906d510a9645ea80482f57c900b))

**Bug Fixes**

- Change behavior of `URLUtilCompat.guessFileName` to only use the `mimeType` parameter to suggest an extension for filenames derived from the URL parameter. ([I53ecd](https://android-review.googlesource.com/#/q/I53ecd6d664efe5747a4451171617a2d33cfb59eb), [b/382864232](https://issuetracker.google.com/issues/382864232))

### Version 1.13.0-alpha03

January 15, 2025

`androidx.webkit:webkit:1.13.0-alpha03` is released. Version 1.13.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/46295bc0b75a16f452e8e0090e8de41073d4dbb6..ad66672b42ec1e9359219e82b7f8189d03df40f5/webkit/webkit).

**New Features**

- Introduce a new experimental API for Url prerendering to allow developers to speculative prerender candidate urls resulting in faster navigations. ([I0cfe7](https://android-review.googlesource.com/#/q/I0cfe7ac389969422e56721db7a0cf67d6739d5af))
- Introducing a set of new APIs to delete browsing data stored by `WebView`. The new APIs in `WebStorageCompat` should be preferred over the existing APIs in `android.webkit.WebStorage`, as they will guarantee deletion of all local storage, including the network cache and cookies, as well as any installed service workers. If new storage APIs are introduced in the future, then these new methods will be updated to include them in the storage deleted. ([Iad54f](https://android-review.googlesource.com/#/q/Iad54f46e2fbb2a7369f2b7191519af0b10525ed7), [b/382273208](https://issuetracker.google.com/issues/382273208))
- Add `setPartitionedCookiesEnabled` API. This will allow developers to enable and disable partitioned cookies in `WebView`. ([Ic506a](https://android-review.googlesource.com/#/q/Ic506a23471946d31b797397e2f71aef0f3ae481a), [b/364904765](https://issuetracker.google.com/issues/364904765))

**API Changes**

- Change thread requirement for Prefetch API to only be called on the UI thread. ([I866b5](https://android-review.googlesource.com/#/q/I866b5410e09ab0dd8865cc6a5592fda3af05eb02))
- Update `WebAuthn` methods to highlight that they must be called on the UI thread. This requirement is enforced by the implementation already, and this change only adds the relevant annotation. ([I6d6ba](https://android-review.googlesource.com/#/q/I6d6ba648648fe1274800b7beb27f2fa0e9961e19))

### Version 1.13.0-alpha02

December 11, 2024

`androidx.webkit:webkit:1.13.0-alpha02` is released. Version 1.13.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6f09cf2ae979e48fdb19485f757a033e4a34bb82..46295bc0b75a16f452e8e0090e8de41073d4dbb6/webkit/webkit).

**New Features**

- Add socket tagging API to `WebView` for accounting of `WebView`'s network traffic using `NetworkStatsManager`/`TrafficStats`. This feature will only be available from `WebView` M133. ([Ica441](https://android-review.googlesource.com/#/q/Ica4412c9432ff479ea728c30c09b1d7bf359d0f0), [b/374932688](https://issuetracker.google.com/issues/374932688))

**API Changes**

- Update Prefetch API by renaming `PrefetchParameter` to `SpeculativeLoadingParamaters`, introducing new `PrefetchNetworkException`, replacing `PrefetchOperationCallback` with `OutcomeReceiverCompat` and update the javadoc. ([If5072](https://android-review.googlesource.com/#/q/If50726ae66737d2a14c0e06a38f91105c1156488))
- Get diagnostic information from WebView async startup API.
- Provide an option for apps to only trigger init that doesn't block the UI thread. ([I9bf2b](https://android-review.googlesource.com/#/q/I9bf2b3b53b835366cf68c938a8bcd1612bd7f3fd))

**Bug Fixes**

- This library now uses [JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler argument to enforce correct usage: `-Xjspecify-annotations=strict` (this is the default starting with version 2.1.0 of the Kotlin compiler). ([I0e4c5](https://android-review.googlesource.com/#/q/I0e4c595aa9288b02dfa563063fedbfd18c667f23), [b/326456246](https://issuetracker.google.com/issues/326456246))

### Version 1.13.0-alpha01

November 13, 2024

`androidx.webkit:webkit:1.13.0-alpha01` is released. Version 1.13.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/89405e05f8d8bbe2fe3efdd62b1152da8450d1ca..6f09cf2ae979e48fdb19485f757a033e4a34bb82/webkit/webkit).

**New Features**

- Add experimental `WebView` async startup API. ([I94b8a](https://android-review.googlesource.com/#/q/I94b8a3f0c6e11f9e9d157e162173db06d33fae94))
- URL Prefetching in Profile: Introduced a new API in Profile to allow developers to trigger URL prefetching. Prefetch Clearing: Added an API to clear ongoing prefetches. ([I42c5c](https://android-review.googlesource.com/#/q/I42c5c282a7114b8b72e62b2b24f917a0f9b47123))

**API Changes**

- Deprecate `WebView.startSafeBrowsing`. ([If5626](https://android-review.googlesource.com/#/q/If5626d9f0bac4f1b04ee9a8f4ebc7f48598c9dac))

## Version 1.12

### Version 1.12.1

October 2, 2024

`androidx.webkit:webkit:1.12.1` is released. Version 1.12.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/3928127eb38f645d470c24d34ea150299b7211f0..89405e05f8d8bbe2fe3efdd62b1152da8450d1ca/webkit/webkit).

**Bug Fixes**

- Resolve the issue that prevented the 1.12.0 APIs from being available in the release.

### Version 1.12.0

September 18, 2024

`androidx.webkit:webkit:1.12.0` is released. Version 1.12.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/203d8b86da1b90e7c35b08e3d59ffaa04c1ba5d1..3928127eb38f645d470c24d34ea150299b7211f0/webkit/webkit).

**Important changes since 1.11.0**

- Add a new API to `WebSettingsCompat` to enable/disable [BackForwardCache](https://developer.chrome.com/blog/back-forward-cache) for this `WebSettings`. This API is experimental and can be changed in the future. ([aosp/3111705](https://android-review.googlesource.com/c/platform/frameworks/support/+/3111705))
- Add a new API to `WebSettingsCompat` to control the Speculative Loading behavior for this `WebSettings`. Only [Prerender](https://developer.chrome.com/docs/web-platform/prerender-pages) is available for now. This API is experimental and can be changed in the future. ([I13962](https://android-review.googlesource.com/#/q/I13962fd09f251fb2629c6d19ad1ec016bc38248d))
- Added a new API to enable [Web Authentication](https://www.w3.org/TR/webauthn-2/) in `WebView`. Developers can enable/disable `WebAuthn` calls in a `WebView` for their apps using `WebSettingsCompat#setWebAuthenticationSupport`. ([I8187f](https://android-review.googlesource.com/#/q/I8187fdee6ee26efbb2c32c668c09f4ab50ecb92c))

### Version 1.12.0-rc01

September 4, 2024

`androidx.webkit:webkit:1.12.0-rc01` is released. This release contains no changes from the `1.12.0-beta01` release.

### Version 1.12.0-beta01

August 21, 2024

`androidx.webkit:webkit:1.12.0-beta01` is released. Version 1.12.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f5541f29d045c6ba9734689ec67891f8d667412b..8c4071562bd7e22b937284d71fb7aca9c4cd662c/webkit/webkit).

**Bug Fixes**

- Removed manual outlining of access to new platform APIs since this happens automatically via API modeling when using R8 with AGP 7.3 or later (e.g. R8 version 3.3) and for all builds when using AGP 8.1 or later (e.g. D8 version 8.1). Clients who are not using AGP are advised to update to D8 version 8.1 or later. See [this article](https://medium.com/androiddevelopers/mitigating-soft-verification-issues-in-r8-and-d8-7e9e06827dfd) for more details. ([Ia60e0](https://android-review.googlesource.com/#/q/Ia60e0ab9f0fd613883a772c8aa34e27cc986cae8), [b/345472586](https://issuetracker.google.com/issues/345472586))

### Version 1.12.0-alpha02

June 12, 2024

`androidx.webkit:webkit:1.12.0-alpha02` is released. Version 1.12.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/67004410fdbff19f90caa4cc43965ab21dca1943..f5541f29d045c6ba9734689ec67891f8d667412b/webkit/webkit).

**New Features**

- Add a new API to `WebSettingsCompat` to enabled/disable [`BackForwardCache`](https://developer.chrome.com/blog/back-forward-cache). This API is experimental and can be changed in the future. ([I64a38](https://android-review.googlesource.com/#/q/I64a38d91f09a386a1b9e791538d37a730c1a12f6))
- Add a new API to `WebSettingsCompat` to control the Speculative Loading behavior for this WebSettings. Only [Prerender](https://developer.chrome.com/docs/web-platform/prerender-pages) is available for now. This API is experimental and can be changed in the future. ([I13962](https://android-review.googlesource.com/#/q/I13962fd09f251fb2629c6d19ad1ec016bc38248d))

**API Changes**

- Some methods are now documented with `@UiThread` where appropriate. ([I6c7e0](https://android-review.googlesource.com/#/q/I6c7e092a07cd47c4b76f5cffd2628eda3127edd9)), ([I44541](https://android-review.googlesource.com/#/q/I44541931ef0aed0a9755de353b098aa96d0c2604))
- Thread-safe methods are now documented with `@AnyThread`. ([I70189](https://android-review.googlesource.com/#/q/I701894e8da5d8e968430f6a0a6c14c101d1ab474))
- Increasing `minSdkVersion` from 19 to 21. ([Id7a43](https://android-review.googlesource.com/#/q/Id7a43dc96264bb58670a90b7de34b9f3a7cc2818))

### Version 1.12.0-alpha01

April 17, 2024

`androidx.webkit:webkit:1.12.0-alpha01` is released. Version 1.12.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/3c9f9abd68ce92e21b76ee69300d54b73132cf6a..67004410fdbff19f90caa4cc43965ab21dca1943/webkit/webkit).

**API Changes**

- Added a new API to enable [Web Authentication](https://www.w3.org/TR/webauthn-2/) in `WebView. Developers` can enable/disable `WebAuthn` calls in a `WebView` for their apps using `WebSettingsCompat#setWebAuthenticationSupport`. ([I8187f](https://android-review.googlesource.com/#/q/I8187fdee6ee26efbb2c32c668c09f4ab50ecb92c))

## Version 1.11

### Version 1.11.0

May 1, 2024

`androidx.webkit:webkit:1.11.0` is released. Version 1.11.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/3c9f9abd68ce92e21b76ee69300d54b73132cf6a..1beb20701084b8d136e08bcdbe34637a3fcfeaa2/webkit/webkit).

**Important changes since 1.10.0**

- Allow apps to control audio playback in `WebView` through the new [`setAudioMuted`](https://developer.android.com/reference/androidx/webkit/WebViewCompat#setAudioMuted(android.webkit.WebView,boolean)) and [`isAudioMuted`](https://developer.android.com/reference/androidx/webkit/WebViewCompat#isAudioMuted(android.webkit.WebView)) APIs, which are analogous to muting a tab in Chrome.
- Introduced [`URLUtilCompat`](https://developer.android.com/reference/androidx/webkit/URLUtilCompat), which supports parsing of `Content-Disposition` headers that use the `filename*` encoded value attribute as defined in [RFC 6266](https://datatracker.ietf.org/doc/html/rfc6266). The compatibility API also directly exposes a method to parse the `Content-Disposition` header where a suggested file name based on URL and MIME-type is not desired.

### Version 1.11.0-rc01

April 3, 2024

`androidx.webkit:webkit:1.11.0-rc01` is released. This release contains no changes from the `1.11.0-beta01` release.

### Version 1.11.0-beta01

March 20, 2024

`androidx.webkit:webkit:1.11.0-beta01` is released without any notable changes. Version 1.11.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e1b82c49c59d8e976ce558aba5586f6c61bc9054..0cea8b8456b6f3cdf8bf3f287dc53659a023a95b/webkit/webkit).

### Version 1.11.0-alpha02

February 21, 2024

`androidx.webkit:webkit:1.11.0-alpha02` is released. [Version 1.11.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ca2a8cf8da3a3502fccc593974f8085653e38261..e1b82c49c59d8e976ce558aba5586f6c61bc9054/webkit/webkit)

**New Features**

- Add `setAudioMuted` and `isAudioMuted` methods for muting (and unmuting) `WebViews`. This method will allow you to prevent a `WebView` from playing audio. ([Ie7a33](https://android-review.googlesource.com/#/q/Ie7a33727f765813fbb2cf07b04999d0d268865b4))

**API Changes**

- `URLUtilCompat` is made final as it should not be subclassed. ([I49ec1](https://android-review.googlesource.com/#/q/I49ec19888f924f119e94d34f0c2a969f50cb8243))

### Version 1.11.0-alpha01

February 7, 2024

`androidx.webkit:webkit:1.11.0-alpha01` is released. [Version 1.11.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/38eb84435df13cec0279ef1222b2155bc3c11d0b..ca2a8cf8da3a3502fccc593974f8085653e38261/webkit/webkit)

**New Features**

- Add compatibility for `URLUtil.guessFileName`. The compatibility version in `URLUtilCompat` supports parsing of `Content-Disposition` headers that use the `filename*` encoded value attribute as defined in [RFC 6266](https://datatracker.ietf.org/doc/html/rfc6266). The compatibility API also directly exposes a method to parse the `Content-Disposition` header where a suggested file name based on URL and MIME-type is not desired. ([If6ae7](https://android-review.googlesource.com/#/q/If6ae780cbb49f2092f22bd796a6eccb34f25e877), [b/309927164](https://issuetracker.google.com/issues/309927164))

## Version 1.10

### Version 1.10.0

January 24, 2024

`androidx.webkit:webkit:1.10.0` is released. [Version 1.10.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/04040f77aaebec1ae7f6906cac613a2024d65443..38eb84435df13cec0279ef1222b2155bc3c11d0b/webkit/webkit)

**Important changes since 1.9.0**

- Added a [new API to WebSettingsCompat](https://developer.android.com/reference/androidx/webkit/WebSettingsCompat#setWebViewMediaIntegrityApiStatus(android.webkit.WebSettings,androidx.webkit.WebViewMediaIntegrityApiStatusConfig)) to control the experimental [Android WebView Media Integrity API](https://android-developers.googleblog.com/2023/11/increasing-trust-for-embedded-media.html) behavior by either disabling the API entirely, or restrict sharing the application identity in the API response. This can be toggled for all origins and on a per origin basis.

### Version 1.10.0-rc01

January 10, 2024

`androidx.webkit:webkit:1.10.0-rc01` is released. This release contains no changes from the `1.10.0-beta01` release.

### Version 1.10.0-beta01

December 13, 2023

`androidx.webkit:webkit:1.10.0-beta01` is released. [Version 1.10.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b5166f9a1e9c047162d1215884c3e2cd41a4a74a..9174577f8a57ba4ae4958cc31787ea4db3b2b44a/webkit/webkit)

- No functional changes from `1.10.0-alpha01`.

### Version 1.10.0-alpha01

November 29, 2023

`androidx.webkit:webkit:1.10.0-alpha01` is released. [Version 1.10.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b5166f9a1e9c047162d1215884c3e2cd41a4a74a/webkit/webkit)

**New Features**

- Added a new API to `WebSettingsCompat` to control the experimental [Android WebView Media Integrity API](https://android-developers.googleblog.com/2023/11/increasing-trust-for-embedded-media.html) behaviour by either disabling the API entirely, or restrict sharing the application identity in the API response. This can be toggled for all origins and on a per origin basis.

## Version 1.9

### Version 1.9.0

November 29, 2023

`androidx.webkit:webkit:1.9.0` is released. [Version 1.9.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/40bb8c8db91df80e03503485d4964664f87cde66..d905464a8027b0af72851565b52e77892405085d/webkit/webkit)

**Important changes since 1.8.0**

- **Added a new multi-profile API for WebViews.**
  - The [Profile](https://developer.android.com/reference/androidx/webkit/Profile) interface has different APIs to use to get associated data with this profile such as its name, [GeoLocationPermissions](https://developer.android.com/reference/android/webkit/GeolocationPermissions), [ServiceWorkerController](https://developer.android.com/reference/android/webkit/ServiceWorkerController), [CookieManager](https://developer.android.com/reference/android/webkit/CookieManager) and [WebStorage](https://developer.android.com/reference/android/webkit/WebStorage). These objects are specific to the profile, and information is not shared between different profiles in the application.
  - The profile used by a `WebView` instance can be changed using the [WebViewCompat#setProfile](https://developer.android.com/reference/androidx/webkit/WebViewCompat#setProfile(android.webkit.WebView,java.lang.String)) method and retrieved using [WebViewCompat#getProfile](https://developer.android.com/reference/androidx/webkit/WebViewCompat#getProfile(android.webkit.WebView))
  - The newly introduced [ProfileStore](https://developer.android.com/reference/androidx/webkit/ProfileStore) let you manage the available profiles in your application, including the default profile.
  - Existing WebView APIs such as [CookieManager#getInstance](https://developer.android.com/reference/android/webkit/CookieManager#getInstance()) will continue to operate on the Default profile.
- **Added an API to inject and run Javascript before page load.**
  - The [WebViewCompat#addDocumentStartJavascript](https://developer.android.com/reference/androidx/webkit/WebViewCompat#addDocumentStartJavaScript(android.webkit.WebView,java.lang.String,java.util.Set%3Cjava.lang.String%3E)) API allows apps to inject scripts into a `WebView` which are guaranteed to run before any page scripts are executed. The API allows the app to specify a target list of origins for the script to be enabled on, ensuring that it only runs on intended pages. Unlike [WebView#evaluateJavascript](https://developer.android.com/reference/android/webkit/WebView#evaluateJavascript(java.lang.String,%20android.webkit.ValueCallback%3Cjava.lang.String%3E)), this API will allow execution of scripts in embedded Iframes when they load. Apps can use this new API in combination with [WebViewCompat#addWebMessageListener](https://developer.android.com/reference/androidx/webkit/WebViewCompat#addWebMessageListener(android.webkit.WebView,java.lang.String,java.util.Set%3Cjava.lang.String%3E,androidx.webkit.WebViewCompat.WebMessageListener)) to set up two-way communication with JavaScript in the page in a reliable way.
- **Added APIs to modify how Privacy Sandbox Attribution Reporting events are registered.**
  - We introduced a new API [WebSettingsCompat#setAttributionRegistrationBehavior](https://developer.android.com/reference/androidx/webkit/WebSettingsCompat#setAttributionRegistrationBehavior(android.webkit.WebSettings,int)) which allows developers to configure whether attribution sources and triggers are registered as coming from the app itself or coming from the web content in the WebView. This method can also be used to disable Attribution Reporting in WebView. Additionally we added a new API `WebSettingsCompat#getAttributionRegistrationBehavior` to get the current behavior.
  - For more information see the [Privacy Sandbox documentation](https://developer.android.com/design-for-safety/privacy-sandbox/attribution-app-to-web#attribution_source_and_trigger_registration_from_webview).
- **Added APIs to override user-agent metadata for client hints.**
  - We introduced a new API, [WebSettingsCompat#setUserAgentMetadata](https://developer.android.com/reference/androidx/webkit/WebSettingsCompat#setUserAgentMetadata(android.webkit.WebSettings,androidx.webkit.UserAgentMetadata)) to override the user-agent metadata for WebView used to populate the user-agent client hints, and we also added another new API [WebSettingsCompat#getUserAgentMetadata](https://developer.android.com/reference/androidx/webkit/WebSettingsCompat#getUserAgentMetadata(android.webkit.WebSettings)) to get current user-agent overrides. We encourage apps to use the new API to set the right override values whenever the app changes the default user agent string using [WebSettings.setUserAgentString](https://developer.android.com/reference/android/webkit/WebSettings#setUserAgentString(java.lang.String)) to ensure the correct values are being used in all situations.

### Version 1.9.0-rc01

November 15, 2023

`androidx.webkit:webkit:1.9.0-rc01` is released. This release contains no changes from the `1.9.0-beta01` release.

### Version 1.9.0-beta01

November 1, 2023

`androidx.webkit:webkit:1.9.0-beta01` is released. [Version 1.9.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/465c5c5b7a0d79793bddb26a695f67aba8ea2f7e..e3ffd7948030a769c857b8c629e0079c54b730ad/webkit/webkit)

**API Changes**

- Address user-agent metadata API's nullability issue. We update `BrandVersion` class to use builder pattern, make the `UserAgentMetadata` class's getters and setters nullability consistent. ([Ibf195](https://android-review.googlesource.com/#/q/Ibf19517c81c8a3228072768791f67087279faef8))
- Annotating `ProfileStore`, `WebViewCompat#setProfile` and `WebViewCompat.getProfile` with `@UiThread`. ([I499b2](https://android-review.googlesource.com/#/q/I499b28e80fbe8109cdfb9bb841df765589d2087b))

### Version 1.9.0-alpha01

October 18, 2023

`androidx.webkit:webkit:1.9.0-alpha01` is released. [Version 1.9.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6d044fc1d7a213f318abade3b2235f9d90b28901..465c5c5b7a0d79793bddb26a695f67aba8ea2f7e/webkit/webkit)

**New Features**

- We added the multi-profile API which allows you to have separate browsing sessions between `WebViews`, each profile has its own data (e.g. cookies). You can create profiles, assign them to `WebView` instances, and retrieve them later for any data access. There is a singleton class `ProfileStore` to help you manage profiles by creation or deletion with APIs; `getOrCreateProfile`, `getProfile`, `getAllProfileNames` and `deleteProfile`. The `Profile` class will have different APIs to use to get associated data with this profile such as its name, [`GeoLocationPermissions`](https://developer.android.com/reference/android/webkit/GeolocationPermissions), [`ServiceWorkerController`](https://developer.android.com/reference/android/webkit/ServiceWorkerController), [`CookieManager`](https://developer.android.com/reference/android/webkit/CookieManager) and [`WebStorage`](https://developer.android.com/reference/android/webkit/WebStorage). Each `WebView` will run with the default profile by default however, you can change that using `WebViewCompat#setProfile` Related to that, a `WebView`'s profile can be retrieved using `WebViewCompat#getProfile`. ([I32d22](https://android-review.googlesource.com/#/q/I32d2278b5028d43bb49a0dbc71d13ab594bcba11))
- Add APIs to modify how Attribution Reporting events are registered. We introduced a new API `WebSettingsCompat#setAttributionRegistrationBehavior` which allows developers to configure whether sources and triggers are registered as coming from the app itself or coming from the web content in the `WebView`. This method can also be used to disable Attribution Reporting in `WebView`. Additionally we added a new API `WebSettingsCompat#getAttributionRegistrationBehavior` to get the current behavior. For more information see the [Privacy Sandbox documentation](https://developer.android.com/design-for-safety/privacy-sandbox/attribution-app-to-web#attribution_source_and_trigger_registration_from_webview). ([I661f2](https://android-review.googlesource.com/#/q/I661f28500fd791c31f20b8d9cab8c09872581d79))
- Add APIs to override user-agent metadata. We introduced a new API `WebSettingsCompat#setUserAgentMetadata` to override the user-agent metadata for WebView, which is used to populate the user-agent client hints, and we also added another new API `WebSettingsCompat#getUserAgentMetadata` to get current user-agent overrides. We encourage apps to use the new API to set the right override values instead of relying on changing user-agent. ([I74500](https://android-review.googlesource.com/#/q/I745009a8c24d287416787802fb29210a78967855))
- Add an API to inject Javascript to be run during page load. The `WebViewCompat.addDocumentStartJavascript` API allows apps to inject scripts into a WebView which will be run before any page scripts are executed. The API allows the app to specify a target list of origins for the script to be enabled on, ensuring that it only runs on intended pages. Unlike `WebView.evaluateJavascript`, this API will allow execution of scripts in embedded Iframes when they load. ([Ide063](https://android-review.googlesource.com/#/q/Ide0637579a8a879c6641bda61dec1448d3c51979))

## Version 1.8

### Version 1.8.0

September 6, 2023

`androidx.webkit:webkit:1.8.0` is released. [Version 1.8.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/78df6a9e6d48c2becce2ec537e22d3a235b38fad..6d044fc1d7a213f318abade3b2235f9d90b28901/webkit/webkit)

**Important changes since 1.7.0**

- Add support for passing `ArrayBuffer` over [`WebMessagePortCompat#postMessage`](https://developer.android.com/reference/androidx/webkit/WebMessagePortCompat#postMessage(androidx.webkit.WebMessageCompat)), [`JavaScriptReplyProxy#postMessage`](https://developer.android.com/reference/androidx/webkit/JavaScriptReplyProxy#postMessage(byte%5B%5D)) and [`WebViewCompat#postWebMessage`](https://developer.android.com/reference/androidx/webkit/WebViewCompat#postWebMessage(android.webkit.WebView,androidx.webkit.WebMessageCompat,android.net.Uri)), receiving `ArrayBuffer` from JavaScript over `WebMessagePortCompat` and `WebMessageListener`, and receiving transferable `ArrayBuffer` from JavaScript over `WebMessagePortCompat`. ([aosp/2596550](https://android-review.googlesource.com/2596550), [b/251152171](https://issuetracker.google.com/251152171))

### Version 1.8.0-rc01

August 9, 2023

`androidx.webkit:webkit:1.8.0-rc01` is released with no changes since `1.8.0-beta01`. [Version 1.8.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4aed940027a19667e67d155563fc5fa8b7279313..78df6a9e6d48c2becce2ec537e22d3a235b38fad/webkit/webkit)

### Version 1.8.0-beta01

July 26, 2023

`androidx.webkit:webkit:1.8.0-beta01` is released with no changes since `1.8.0-alpha01`. [Version 1.8.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/73f902dee011bfe400d8a0330bfd8d4bb632065f..4aed940027a19667e67d155563fc5fa8b7279313/webkit/webkit)

### Version 1.8.0-alpha01

June 7, 2023

`androidx.webkit:webkit:1.8.0-alpha01` is released. [Version 1.8.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1b9b8b9c77f7fe8ed9ea6469e66fcde430eae54a..73f902dee011bfe400d8a0330bfd8d4bb632065f/webkit/webkit)

**API Changes**

- See the External Contribution section.

**External Contribution**

- Add support for passing `ArrayBuffer` over `WebMessagePortCompat#postMessage`, `JsReplyProxy#postMessage` and `WebViewCompat#postWebMessage`, receiving `ArrayBuffer` from JavaScript over `WebMessagePortCompat` and `WebMessageListener`, and receiving transferable `ArrayBuffer` from JavaScript over `WebMessagePortCompat`. Please note that this API will only be available from `WebView` version 116. ([Ie7567](https://android-review.googlesource.com/#/q/Ie756728c63c528c3e36417f7719cead78d7c99eb), [b/251152171](https://issuetracker.google.com/issues/251152171))

## Version 1.7

### Version 1.7.0

May 24, 2023

`androidx.webkit:webkit:1.7.0` is released. [Version 1.7.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/648171e2e68b3e4c6352fad4fd4f0e82acb62367..1b9b8b9c77f7fe8ed9ea6469e66fcde430eae54a/webkit/webkit)

**Important changes since 1.6.0**

- We added support for [Image drag](https://developer.android.com/develop/ui/views/touch-and-input/drag-drop) in `WebView`. You can enable your users to drag images out of the `WebView` by adding the new [`DropDataContentProvider`](https://developer.android.com/reference/androidx/webkit/DropDataContentProvider) to your app's manifest as described in the class documentation.
- We added the [`ProcessGlobalConfig#setDirectoryBasePaths(Context,File,File)`](https://developer.android.com/reference/androidx/webkit/ProcessGlobalConfig#setDirectoryBasePaths(android.content.Context,java.io.File,java.io.File)) API which can be used to set the base directories that `WebView` will use for the current process. As with all methods on `ProcessGlobalConfig`, this method must be called before the first instance of `WebView` is instantiated. This method is added to provide Android framework the capability to tweak `WebView` settings. For general purpose applications, using this method is not recommended.

### Version 1.7.0-rc01

May 10, 2023

`androidx.webkit:webkit:1.7.0-rc01` is released with no changes since `1.7.0-beta01`. [Version 1.7.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a200cb82769634cecdb118ec4f0bfdf0b086e597..648171e2e68b3e4c6352fad4fd4f0e82acb62367/webkit/webkit)

### Version 1.7.0-beta01

April 5, 2023

`androidx.webkit:webkit:1.7.0-beta01` is released. [Version 1.7.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bf83b7ca1e086138c9ffa3ed2a530db3b038c79a..a200cb82769634cecdb118ec4f0bfdf0b086e597/webkit/webkit)

**API Changes**

- Minor change to feature flag and method name and make `setDirectoryBasePaths()` accept File instead of String ([Ib0d0a](https://android-review.googlesource.com/#/q/Ib0d0a8110952beb737a2de94c9b78fd254cb7fce))

### Version 1.7.0-alpha03

March 8, 2023

`androidx.webkit:webkit:1.7.0-alpha03` is released. [Version 1.7.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7d3ac1ab1206c01fae3ebb500b5b942636070155..bf83b7ca1e086138c9ffa3ed2a530db3b038c79a/webkit/webkit)

**API Changes**

- Add `ProcessGlobalConfig#setDirectoryBasePath(String, String)` API which can be used to set the base directories that `WebView` will use for the current process. ([Ibd1a1](https://android-review.googlesource.com/#/q/Ibd1a165dd2739b652b26d3c5f2cfe773cb7eb386), [b/250553687](https://issuetracker.google.com/issues/250553687))

**Bug Fixes**

- Fix invalid `ProGuard` rule causing build errors when using `DexGuard` ([Ia65c2](https://android-review.googlesource.com/#/q/Ia65c2fd50327eda385bc0ec061f4ad08a7afe81d), [b/270034835](https://issuetracker.google.com/issues/270034835))

### Version 1.7.0-alpha02

February 8, 2023

`androidx.webkit:webkit:1.7.0-alpha02` is released. [Version 1.7.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e5dad1e7d1c225f89f7c2d5a39a7a0de8d637d7b..7d3ac1ab1206c01fae3ebb500b5b942636070155/webkit/webkit)

**Bug Fixes**

- Documentation bugs for `DropDataContentProvider`.

### Version 1.7.0-alpha01

January 25, 2023

`androidx.webkit:webkit:1.7.0-alpha01` is released. [Version 1.7.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e5dad1e7d1c225f89f7c2d5a39a7a0de8d637d7b/webkit/webkit)

**New Features**

- We are adding support for [Image drag](https://developer.android.com/develop/ui/views/touch-and-input/drag-drop) in `WebView`. You can enable your users to drag images out of the `WebView` by adding the new `DropDataContentProvider` to your app's manifest. ([05a1a6](https://android.googlesource.com/platform/frameworks/support/+/05a1a61f02f6465fa43fd12693c4890b9c01f90e))

## Version 1.6

### Version 1.6.1

March 22, 2023

`androidx.webkit:webkit:1.6.1` is released. [Version 1.6.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/092d2470b0d71065d37c4ed9d6b46ee88b5fe8f2..5a78ea8f8561ada755d40a422422879e2090d813/webkit/webkit)

**Bug Fixes**

- Fix proguard parse error ([Ia65c2](https://android-review.googlesource.com/#/q/Ia65c2fd50327eda385bc0ec061f4ad08a7afe81d))

### Version 1.6.0

January 25, 2023

`androidx.webkit:webkit:1.6.0` is released. [Version 1.6.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f2cd44abc5d159809c80d203e887a24884dff186..092d2470b0d71065d37c4ed9d6b46ee88b5fe8f2/webkit/webkit)

**Important changes since 1.5.0**

- A new [ProcessGlobalConfig](https://developer.android.com/reference/androidx/webkit/ProcessGlobalConfig) API has been added to allow apps to provide configuration settings that need to be set before loading WebView, such as the WebView data directory suffix. The configuration should be set up and applied as early as possible during application startup, to ensure that it happens before any other thread can call a method that loads `WebView` into the process.
- A new [CookieManagerCompat](https://developer.android.com/reference/androidx/webkit/CookieManagerCompat) API has been added to expand [android.webkit.CookieManager](https://developer.android.com/reference/android/webkit/CookieManager) with a new `getCookieInfo` method, which retrieves all attributes for all cookies set on a specific URL. This differs from the existing getCookie API in `CookieManager` which returns only the name and value attributes of the cookies.
- `WebSettingsCompat` has new methods to [enable/disable](https://developer.android.com/reference/androidx/webkit/WebSettingsCompat#setEnterpriseAuthenticationAppLinkPolicyEnabled(android.webkit.WebSettings,boolean)) the effect of `EnterpriseAuthenticationAppLinkPolicy` if set by admin in `WebView`, and to [get the current setting](https://developer.android.com/reference/androidx/webkit/WebSettingsCompat#getEnterpriseAuthenticationAppLinkPolicyEnabled(android.webkit.WebSettings)). This feature lets WebView open an Authentication app instead of opening the authentication URL. This feature has no effect on devices that are not managed by an enterprise policy.
- Adding [a new API](https://developer.android.com/reference/androidx/webkit/WebSettingsCompat#setRequestedWithHeaderOriginAllowList(android.webkit.WebSettings,java.util.Set%3Cjava.lang.String%3E)) to `WebSettingsCompat` to let applications explicitly send the app package name in the `X-Requested-With` header to allowlisted origins. The header has traditionally been sent on every request from `WebView`.

### Version 1.6.0-rc01

January 11, 2023

`androidx.webkit:webkit:1.6.0-rc01` is released. [Version 1.6.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4a2f5e696614339c1ac21f706c1a17c0285780e7..f2cd44abc5d159809c80d203e887a24884dff186/webkit/webkit)

**Bug Fixes**

- Fixed `NullPointerException` in `WebViewFeature.isStartupFeatureSupported(Context, String)` when running on SDK \< L. ([Ic7292](https://android-review.googlesource.com/#/q/Ic729252e00183a6984bff499bcf0408c8d7ba009))

### Version 1.6.0-beta01

December 7, 2022

`androidx.webkit:webkit:1.6.0-beta01` is released. [Version 1.6.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a1e318590b217ecfce1b2de17eed2f18b6a680bb..4a2f5e696614339c1ac21f706c1a17c0285780e7/webkit/webkit)

**API Changes**

- `ProcessGlobalConfig` has been changed to use a normal constructor and a static apply method. The apply method should only be called once per process, as early as possible, and will throw `IllegalStateException` if called more than once. `ProcessGlobalConfig` objects no longer have any restrictions on how many times setters can be called. ([I456c3](https://android-review.googlesource.com/#/q/I456c366dcd26ff86a8ffcce191220e27adc94b48))

### Version 1.6.0-alpha03

November 9, 2022

`androidx.webkit:webkit:1.6.0-alpha03` is released. [Version 1.6.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/548c8ac2570ae6cf15798fea1380491f7d93796b..a1e318590b217ecfce1b2de17eed2f18b6a680bb/webkit/webkit)

**New Features**

- Add `ProcessGlobalConfig` class enabling users to set process global config before loading `WebView`. `WebView` has some process-global configuration parameters that cannot be changed once `WebView` has been loaded (e.g. the `WebView` data directory). This class allows apps to set these parameters. The configuration should be set up and applied as early as possible during application startup, to ensure that it happens before any other thread can call a method that loads `WebView` into the process. ([I7c0e0](https://android-review.googlesource.com/#/q/I7c0e0e42e91efe45f16e66afead7b9e52240bfe4), [b/250553687](https://issuetracker.google.com/issues/250553687))
- Adding new API to let applications explicitly send the app package name in the X-Requested-With header to allowlisted origins. The header has traditionally been sent on every request from `WebView`. ([I0adfe](https://android-review.googlesource.com/#/q/I0adfea18e5c9b60405af2d62c61786b09c37ffb9), [b/226552535](https://issuetracker.google.com/issues/226552535))

**API Changes**

- The `WebSettingsCompat#setAlgorithmicDarkeningAllowed` API is supported on all Android versions in `WebView` version 105 and later. Previous versions of `WebView` only supported the API on Android Q and later. As a result, this api is no longer marked `@RequiresApi(Build.VERSION_CODES.Q)`. ([I3ac1d](https://android-review.googlesource.com/#/q/I3ac1dd6b5cb464d5b40fddcccd465ad0ba731452))

### Version 1.6.0-alpha02

October 24, 2022

`androidx.webkit:webkit:1.6.0-alpha02` is released. [Version 1.6.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/dd1e45e8550560087f6447a34a9145048b5766f4..548c8ac2570ae6cf15798fea1380491f7d93796b/webkit/webkit)

**New Features**

- Adds a new `CookieManagerCompat` class along with a `getCookieInfo` API which retrieves all attributes for all cookies set on a specific URL. This differs from the existing `getCookie` API in `CookieManager` which returns only the name and value attributes of the cookies. ([I07365](https://android-review.googlesource.com/#/q/I07365e16e0ae20bb13e7326548fc3edd7581b4e2), [b/242161756](https://issuetracker.google.com/issues/242161756))

### Version 1.6.0-alpha01

August 24, 2022

`androidx.webkit:webkit:1.6.0-alpha01` is released. [Version 1.6.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/dd1e45e8550560087f6447a34a9145048b5766f4/webkit/webkit)

**New Features**

- Added APIs in `WebSettingsCompat` to enable/disable the effect of `EnterpriseAuthenticationAppLinkPolicy` if set by admin in `WebView`. This feature lets `WebView` open an Authentication app instead of opening the authentication URL. This feature has no effect on devices that are not managed by an enterprise policy.

## Version 1.5.0

### Version 1.5.0

August 24, 2022

`androidx.webkit:webkit:1.5.0` is released. [Version 1.5.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9bca6bf8a71f062622a44196796a896e29aa1864..b4b62b607a73da9e2234808376ac8d266b787759/webkit/webkit)

**Important changes since 1.4.0**

- A new `setAlgorithmicDarkeningAllowed` API on `WebSettingsCompat` replaces the old `setForceDark` and `setForceDarkStrategy` APIs. Apps targeting SDK 33 and higher (T) should use the new API, as the old API will no longer have any effect for those apps.
- An allow-list of URLs to use the configured proxy can now be set through `ProxyCofig.Builder` by setting `setReverseBypassEnabled` to `true`. When this is in effect, all other URLs will bypass the configured proxy.

### Version 1.5.0-rc01

August 10, 2022

`androidx.webkit:webkit:1.5.0-rc01` is released with no changes since `1.5.0-beta01`. [Version 1.5.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8094b683499b4098092c01028b55a38b49e357f2..9bca6bf8a71f062622a44196796a896e29aa1864/webkit/webkit)

### Version 1.5.0-beta01

June 29, 2022

`androidx.webkit:webkit:1.5.0-beta01` is released. [Version 1.5.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6266a22ad9adaed6fa88fe98aa8adaa46eb96ccc..8094b683499b4098092c01028b55a38b49e357f2/webkit/webkit)

**API Changes**

- Alogrithimic Darkening related APIs are now annotated to require API level Q. The API will not have any effect on API levels \< Q, since dark theme is not an option on these devices. ([I0905e](https://android-review.googlesource.com/#/q/I0905e1bc33fe8b1862549f8e741841b2d487d590))

### Version 1.5.0-alpha01

May 18, 2022

`androidx.webkit:webkit:1.5.0-alpha01` is released. [Version 1.5.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/be8fed3a2ca8490bd8b93503459a1b36640ea5eb..6266a22ad9adaed6fa88fe98aa8adaa46eb96ccc/webkit/webkit)

**New Features**

- Add a new `getVariationsHeader()` method on `WebViewCompat` to get the X-Client-Data header value sent by the `WebView`. The returned value will be a base64 encoded [ClientVariations](https://source.chromium.org/chromium/chromium/src/+/main:components/variations/proto/client_variations.proto) protobuf.
- Add APIs on `WebSettingsCompat` to allow/disallow algorithmic darkening for app with targetSdk \>= 33. ([I29597](https://android-review.googlesource.com/#/q/I2959738a8d71ab509fdcf01e393977398b2179b6))

**API Changes**

- Add a new method in `ProxyCofig.Builder` to set reverse bypass. Setting reverse bypass to true means only URLs in the bypass list will use the proxy settings. ([I9eaa2](https://android-review.googlesource.com/#/q/I9eaa29bbecebecade8cf82d1d65581f0a5715e1a), [b/168728599](https://issuetracker.google.com/issues/168728599))

**Bug Fixes**

- Fixed a typo in dark theme documentation. ([I36ebf](https://android-review.googlesource.com/#/q/I36ebf63c24427e8a19a3ef3d202a5a277d52cc16), [b/194343633](https://issuetracker.google.com/issues/194343633))
- Fixed a bug where `WebViewAssetLoader.Builder` methods were unintentionally order-dependent. ([If420d](https://android-review.googlesource.com/#/q/If420d559a21ea624b2a493d09550ed496ffee392), [b/182196765](https://issuetracker.google.com/issues/182196765))

## Version 1.4.0

### Version 1.4.0

December 16, 2020

`androidx.webkit:webkit:1.4.0` is released. [Version 1.4.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7940308a62309f862f4582dabd65d20ebd607b3c..be8fed3a2ca8490bd8b93503459a1b36640ea5eb/webkit/webkit)

**Major changes since 1.3.0**

- Added a new `setSafeBrowsingAllowlist()` API to replace `setSafeBrowsingWhitelist()`. This helps apps update their code to avoid non-inclusive terminology, while still supporting the same range of Android SDKs and WebView versions as the deprecated API.
- Fixed a bug in setProxyOverride that caused fallback rules not being correctly applied.

### Version 1.4.0-rc02

December 2, 2020

`androidx.webkit:webkit:1.4.0-rc02` is released. [Version 1.4.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8fd35976def09e3e43f398483fc2ed87ad371c19..7940308a62309f862f4582dabd65d20ebd607b3c/webkit/webkit)

**Bug Fixes**

- Fixes fallback rules not being correctly applied when using setProxyOverride.

### Version 1.4.0-rc01

November 11, 2020

`androidx.webkit:webkit:1.4.0-rc01` is released with no changes since `1.4.0-beta01`. [Version 1.4.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f413b8be76bfa0a4d109a3afb583188c580a2aa6..8fd35976def09e3e43f398483fc2ed87ad371c19/webkit/webkit)

### Version 1.4.0-beta01

October 14, 2020

`androidx.webkit:webkit:1.4.0-beta01` is released with no changes since `1.4.0-alpha01`. [Version 1.4.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/18a5639262f8504db530176550e338a5d0e2e044..f413b8be76bfa0a4d109a3afb583188c580a2aa6/webkit/webkit)

### Version 1.4.0-alpha01

September 16, 2020

`androidx.webkit:webkit:1.4.0-alpha01` is released. [Version 1.4.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/17b13af1a2ce83517de3ed926dbc1108ebe5396d..18a5639262f8504db530176550e338a5d0e2e044/webkit/webkit)

**API Changes**

- Added a new `WebViewCompat#setSafeBrowsingAllowlist()` API to replace `setSafeBrowsingWhitelist()`. This helps apps update their code to avoid non-inclusive terminology, while still supporting the same range of Android SDKs and WebView versions as the deprecated API. ([I8d65d](https://android-review.googlesource.com/#/q/I8d65decec81a3f7e900c9efb226c7dd2c42e73ca))

## Version 1.3.0

### Version 1.3.0

August 19, 2020

`androidx.webkit:webkit:1.3.0` is released. [Version 1.3.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/59d1c49043404a019a02e783b0593b78b50e615f..17b13af1a2ce83517de3ed926dbc1108ebe5396d/webkit/webkit)

**Major changes since 1.2.0**

- ForceDarkStrategy API provides more control to WebView darkening (CSS/web content darkening versus auto darkening).
- WebMessageListener and its related APIs provide a simple and secure mechanism to establish communication between web contents and the WebView embedder app.
- `isMultiProcessEnabled` API to check whether WebView is running in multi process. This is possible starting in Android O and it means web content is rendered in a sandboxed renderer process separate to the application process. This sandboxed renderer may be shared with other WebViews in the same application but it's not shared with other application processes.

### Version 1.3.0-rc02

August 5, 2020

`androidx.webkit:webkit:1.3.0-rc02` is released. [Version 1.3.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6038f9f88eeb910506ee40fc6f3cc4fc21e606ff..59d1c49043404a019a02e783b0593b78b50e615f/webkit/webkit)

**Bug Fixes**

- This fixes a compatibility issue where `WebMessageListener` would sometimes crash during local development if your app was started with Android Studio instant run.

### Version 1.3.0-rc01

June 24, 2020

`androidx.webkit:webkit:1.3.0-rc01` is released with no changes since `1.3.0-beta01`. [Version 1.3.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/945594abd75f83bd14daf4fbcd8621796161281e..6038f9f88eeb910506ee40fc6f3cc4fc21e606ff/webkit/webkit)

### Version 1.3.0-beta01

June 10, 2020

`androidx.webkit:webkit:1.3.0-beta01` is released. [Version 1.3.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b752a10305d7cd58a7f50ad094ed54af4d765f27..945594abd75f83bd14daf4fbcd8621796161281e/webkit/webkit)

**New Features**

- `ForceDarkStrategy` API to control WebView darkening (CSS/web content darkening versus auto darkening).
- `WebMessageListener` APIs provide a simple and secure mechanism to establish communication between web contents and the WebView embedder app.
- `MultiProcessEnabled` API to check if WebView is running in multi process mode.

### Version 1.3.0-alpha03

May 27, 2020

`androidx.webkit:webkit:1.3.0-alpha03` is released. [Version 1.3.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b752a10305d7cd58a7f50ad094ed54af4d765f27..c4d097f4335fe6b0268ee9a6d53df43615da0d90/webkit/webkit)

**API Changes**

- `addWebMessageListener` method now receives a `Set<String>` of allowed origin rules (previously a `List<String>`).

### Version 1.3.0-alpha02

April 29, 2020

`androidx.webkit:webkit:1.3.0-alpha02` is released. [Version 1.3.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/24daa503442fcd3e44ada60cf1da41df2815c045..b752a10305d7cd58a7f50ad094ed54af4d765f27/webkit/webkit)

**New Features**

- MultiProcessEnabled API to check if WebView is running in multi process mode.

**API Changes**

- All dark strategy constants are now prefixed with `DARK_STRATEGY`.

### Version 1.3.0-alpha01

April 15, 2020

`androidx.webkit:webkit:1.3.0-alpha01` is released. [Version 1.3.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1dcd3c1b8b7ba53451552c68d4deaa0d60958634..24daa503442fcd3e44ada60cf1da41df2815c045/webkit/webkit)

**New Features**

- `ForceDarkStrategy` API to control `WebView` darkening (CSS/web content darkening versus auto darkening).
- `WebMessageListener` APIs provide a simple and secure mechanism to establish communication between web contents and the WebView embedder app.

## Version 1.2.0

### Version 1.2.0

March 4, 2020

`androidx.webkit:webkit:1.2.0` is released. [Version 1.2.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/0bda71c96ae7ef19673a6a1e7bee8d1d8b8a4877..1dcd3c1b8b7ba53451552c68d4deaa0d60958634/webkit/webkit)

**Major changes since 1.1.0**

- Added the ForceDark API to control if WebViews should be rendered in dark mode.

### Version 1.2.0-rc01

February 19, 2020

`androidx.webkit:webkit:1.2.0-rc01` is released with no changes since `1.2.0-beta01`. [Version 1.2.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/15eb802358e0836378e4daba5db3d88cf09b7f03..0bda71c96ae7ef19673a6a1e7bee8d1d8b8a4877/webkit/webkit)

### Version 1.2.0-beta01

February 5, 2020

`androidx.webkit:webkit:1.2.0-beta01` is released with no changes since `1.2.0-alpha01`. [Version 1.2.0-beta01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/740cde70237dd276f8ad66dfe9528b1cdb5d54bb..15eb802358e0836378e4daba5db3d88cf09b7f03/webkit/webkit).

### Version 1.2.0-alpha01

December 18, 2019

`androidx.webkit:webkit:1.2.0-alpha01` is released. [Version 1.2.0-alpha01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/2a1fc7faf719ace396316bf287f3a2b06f446b86..740cde70237dd276f8ad66dfe9528b1cdb5d54bb/webkit).

**New features**

- ForceDark API to control if WebViews should be rendered in dark mode.

## Version 1.1.0

### Version 1.1.0

November 7, 2019

`androidx.webkit:webkit:1.1.0` is released. [Version 1.1.0 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/2a1fc7faf719ace396316bf287f3a2b06f446b86..40f75b8db6322d0cb774a33a826fc507b3b0b769/webkit).

**Important changes since 1.0.0**

- Getter APIs to complement [setWebViewClient()](https://developer.android.com/reference/android/webkit/WebView#setWebViewClient(android.webkit.WebViewClient)) and [setWebChromeClient()](https://developer.android.com/reference/android/webkit/WebView#setWebChromeClient(android.webkit.WebChromeClient)).
- ProxyController API to set a network request proxy for an app's WebViews.
- WebViewAssetLoader API to simplify loading APK assets, resources, and files from the app data directory via request interception. This allows access to web and local resources without disabling CORS.
- TracingController API to collect WebView tracing information for debugging purposes.
- RenderProcess APIs to manage WebView renderer services, and to detect when poorly behaved content causes WebView renderers to become unresponsive.
- Updated existing APIs to include nullability (`@NonNull`, `@Nullable`) and thread (`@UiThread`, `@WorkerThread`) annotations.

### Version 1.1.0-rc01

October 9, 2019

`androidx.webkit:webkit:1.1.0-rc01` is released. [Version 1.1.0-rc01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/ed022a70892f8519259c687ecb176b38213c8812..2a1fc7faf719ace396316bf287f3a2b06f446b86/webkit).

**Bug fixes**

- Fixed an issue where `setWebViewRenderProcessClient()` could crash if passed a null client.

### Version 1.1.0-beta01

September 5, 2019

`androidx.webkit:webkit:1.1.0-beta01` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/0590008ab8e89f01a6bbac9b20b7f61abc8adce1..ed022a70892f8519259c687ecb176b38213c8812/webkit).

**New features**

- New `InternalStoragePathHandler` in `WebViewAssetLoader` to load files from the app's data directory.

**API changes**

- `ProxyConfig#getProxyRules()` now returns an unmodifiable list of `ProxyRule` instances, which is a new class to hold a scheme filter and its corresponding proxy URL.

**Bug fixes**

- `WebViewAssetLoader` defaults to a "text/plain" MIME type (rather than null) when it can't guess the MIME type from the file path.
- `WebViewAssetLoader` no longer throws a `NullPointerException` when loading files with special characters in their path names.

### Version 1.1.0-alpha02

August 7, 2019

`androidx.webkit:webkit:1.1.0-alpha02` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/a0c2e45e3baa2b73dcdbbd7122900f1a324738c3..ece690f1fdb4481b47c5128fd21d88da7d6850a6/webkit).

**New features**

- `WebViewAssetLoader` exposes the `PathHandler` interface to allow apps to create custom path-handling functionality.

**API changes**

- `WebViewAssetLoader` is now a final class, since it's not meant to be subclassed.
- `WebViewAssetLoader#PathHandler` implementations are now public and final.
- Minor changes to ProxyConfig method names.
- `ProxyController`: added new methods `addDirect()` and `addDirect(String)` to connect directly to servers; removed DIRECT String.
- Updated existing APIs to include nullability (`@NonNull`, `@Nullable`) and thread (`@UiThread`, `@WorkerThread`) annotations.

### Version 1.1.0-alpha01

May 7, 2019

`androidx.webkit:webkit:1.1.0-alpha01` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/50a39caa72955aae0c75225fd9805ab537cbf049..a0c2e45e3baa2b73dcdbbd7122900f1a324738c3/webkit).

**New features**

- Getter APIs to complement `setWebViewClient()` and `setWebChromeClient()`
- ProxyController API to set a network request proxy for an app's WebViews.
- AssetLoader API to simplify loading APK assets and resources via request interception, allowing access to web resources without disabling CORS.
- TracingController API to collect WebView tracing information for debugging purposes.
- RenderProcess APIs to manage WebView renderer services, and to detect when poorly behaved content causes WebView renderers to become unresponsive.

**Bug fixes**

- Minor fixes to documentation formatting for existing APIs.