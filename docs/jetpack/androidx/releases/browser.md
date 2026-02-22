---
title: https://developer.android.com/jetpack/androidx/releases/browser
url: https://developer.android.com/jetpack/androidx/releases/browser
source: md.txt
---

# Browser

[User Guide](https://developer.chrome.com/docs/android/custom-tabs/) API Reference  
[androidx.browser.browseractions](https://developer.android.com/reference/kotlin/androidx/browser/browseractions/package-summary)  
[androidx.browser.customtabs](https://developer.android.com/reference/kotlin/androidx/browser/customtabs/package-summary)  
[androidx.browser.trusted](https://developer.android.com/reference/kotlin/androidx/browser/trusted/package-summary)  
Display webpages in the user's default browser.

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| February 11, 2026 | [1.9.0](https://developer.android.com/jetpack/androidx/releases/browser#1.9.0) | - | - | [1.10.0-alpha03](https://developer.android.com/jetpack/androidx/releases/browser#1.10.0-alpha03) |

## Declaring dependencies

To add a dependency on Browser, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    implementation "androidx.browser:browser:1.9.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.browser:browser:1.9.0")
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:460372+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=460372&template=1422468)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 1.10

### Version 1.10.0-alpha03

February 11, 2026

`androidx.browser:browser:1.10.0-alpha03` is released. Version 1.10.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4350deab5806bf95370a4d012d7eeaa70a10be44..e5df9ab1d4893ddbbc5155114703a64b15079303/browser/browser).

**API Changes**

- Set `CustomContentAction#fromBundle` to be visible from tests ([Iaa6a1](https://android-review.googlesource.com/#/q/Iaa6a1d75e521b8f9b574f0b770d2f9c886a7c588))

### Version 1.10.0-alpha02

October 08, 2025

`androidx.browser:browser:1.10.0-alpha02` is released. Version 1.10.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c359e97fece91f3767a7d017e9def23c7caf1f53..4350deab5806bf95370a4d012d7eeaa70a10be44/browser/browser).

**API Changes**

- Made `AuthTabIntent.AuthenticateUserResultContract` public ([I1e598](https://android-review.googlesource.com/#/q/I1e5989b1452df9bcf7340f8c0a8c5191a425749b), [b/425405218](https://issuetracker.google.com/issues/425405218))
- Rename the window controls overlay display mode to be consistent with other modes. ([I10b67](https://android-review.googlesource.com/#/q/I10b671878fd227947b133cafde80822b2515ed6c))

### Version 1.10.0-alpha01

August 13, 2025

`androidx.browser:browser:1.10.0-alpha01` is released. Version 1.10.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6125f3ad483d32d3a08623ebca3785a2dd20f0c1..c359e97fece91f3767a7d017e9def23c7caf1f53/browser/browser).

**API Changes**

- Added support for the `display_override` TWA manifest property ([Ib036b](https://android-review.googlesource.com/#/q/Ib036b53a6c3e361038c783453813b759d02424f1))
- Removing obsolete `@RequiresApi(21)` annotations ([Ic4792](https://android-review.googlesource.com/#/q/Ic47923dcc82f4b7c4638fadb10c2c0268b414fcd))
- Removing obsolete `@RequiresApi(21)` annotations ([I9103b](https://android-review.googlesource.com/#/q/I9103beb2d5f73470f3abfdf034bc2b473be923e6))
- Allow Null for `pageUrl` in `ContentActionSelectedData` ([Ifed54](https://android-review.googlesource.com/#/q/Ifed54faf7bf04bf0f25cbd8a4e1ba0ea58fa1be9))
- Added an Intent to allow launching the initial url in an external app ([Id9349](https://android-review.googlesource.com/#/q/Id9349f17ca5008bb4f4079f451743f9ccdb46915))
- Add an Intent to allow launching the initial url in an external app ([Ifed54](https://android-review.git.corp.google.com/c/platform/frameworks/support/+/3682822))

**Bug Fixes**

- Moving the default `minSdk` from API 21 to API 23. ([Ibdfca](https://android-review.googlesource.com/#/q/Ibdfca5942dbb414ca07594ba240093db14aad4df), [b/380448311](https://issuetracker.google.com/issues/380448311), [b/435705964](https://issuetracker.google.com/issues/435705964), [b/435705223](https://issuetracker.google.com/issues/435705223))
- Allow Null for `pageUrl` in `ContentActionSelectedData`. ([Id9349](https://android-review.git.corp.google.com/c/platform/frameworks/support/+/3682822))

## Version 1.9

### Version 1.9.0

July 30, 2025

`androidx.browser:browser:1.9.0` is released. Version 1.9.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/2c951147109c46f306515146a6def78b5b84e0da..6125f3ad483d32d3a08623ebca3785a2dd20f0c1/browser/browser).

### Version 1.9.0-rc01

July 16, 2025

`androidx.browser:browser:1.9.0-rc01` is released. Version 1.9.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1b437892629a2cdedb46d9b7232575987b2cc6b5..2c951147109c46f306515146a6def78b5b84e0da/browser/browser).

**API Changes**

- Added 'Contextual Menu Items' for custom tabs ([Iab7d0](https://android-review.googlesource.com/#/q/Iab7d008ccee14d2863f1ae00f79b1243a1110af1))

**Bug Fixes**

- Updated JavaDocs for `setOpenInBrowserButtonState` for ([Iae1f2](https://android-review.googlesource.com/#/q/Iae1f2260f89677b272231e711bc67940207a1cee))

### Version 1.9.0-beta01

July 2, 2025

`androidx.browser:browser:1.9.0-beta01` is released. Version 1.9.0-beta01 contains no changes since the previous alpha version.

### Version 1.9.0-alpha05

June 18, 2025

`androidx.browser:browser:1.9.0-alpha05` is released. Version 1.9.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cd41781824511ce4d5c4a05d2df4aaaee669f0bc..e8af6ab7417811bf386c52a59ab5d0b94d194eeb/browser/browser).

**API Changes**

- Remove experimental annotation from ephemeral browsing API ([If8b1b](https://android-review.googlesource.com/#/q/If8b1b6b8f9d765cc8529baafa4bb36197026d87a))

### Version 1.9.0-alpha04

May 20, 2025

`androidx.browser:browser:1.9.0-alpha04` is released. Version 1.9.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/008cbd021e3a2b4d1f36ea7f48200c4692bfc169..cd41781824511ce4d5c4a05d2df4aaaee669f0bc/browser/browser).

**API Changes**

- Added new intent extra for custom tabs ([I911e0](https://android-review.googlesource.com/#/q/I911e0230d6f4be23a10452b4f98407e8a0945953))
- Added `Browser` and `MiminalUi` modes to `TWADisplayMode` ([I230b5](https://android-review.googlesource.com/#/q/I230b50e3c239c9b314e3ae86f3e4367cd2e0d231))
- Added capability check API for Ephemeral Browsing ([I17d42](https://android-review.googlesource.com/#/q/I17d42604d21562f8bb95967488bf4211d21a8515))
- Remove experimental annotation for `PendingSession` API ([Id6fe3](https://android-review.googlesource.com/#/q/Id6fe39d22908ed01e564c5342ae4ed7fb82c1fb2))
- Added Auth Tab capability check API ([Ifc029](https://android-review.googlesource.com/#/q/Ifc0298fbeee7a71964be7efd585c049a0bf8768d))
- Removed Custom Tab minimize signals experimental annotation ([If2b44](https://android-review.googlesource.com/#/q/If2b440cd1afc800f8c2f8bc55deb1843f281e66a))

### Version 1.9.0-alpha03

April 23, 2025

`androidx.browser:browser:1.9.0-alpha03` is released. Version 1.9.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4c37298a97c16270c139eb812ddadaba03e23a52..008cbd021e3a2b4d1f36ea7f48200c4692bfc169/browser/browser).

**API Changes**

- Removed experimental annotation from Auth Tab. ([I786ff](https://android-review.googlesource.com/#/q/I786ffb7e8397bcb40d2e090ae64f9260c193ffd0))

### Version 1.9.0-alpha02

April 9, 2025

`androidx.browser:browser:1.9.0-alpha02` is released. Version 1.9.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4c47131cd5b50c3091fc0874eb606aaac5b168fa..4c37298a97c16270c139eb812ddadaba03e23a52/browser/browser).

**New Features**

- Added support for multiple Progressive Web App APIs, such as [Launch Handler](https://developer.chrome.com/docs/web-platform/launch-handler), [Protocol Handler](https://developer.chrome.com/docs/web-platform/best-practices/url-protocol-handler) and [File Handler](https://developer.chrome.com/docs/capabilities/web-apis/file-handling)

**API Changes**

- Added overloads for `CustomTabsClient#createPendingAuthTabSession`. ([I71c3a](https://android-review.googlesource.com/#/q/I71c3acc51dc82810ca7bbf305a4c1984759e800d))
- Updated Auth Tab APIs ([Iaf9b1](https://android-review.googlesource.com/#/q/Iaf9b1d7812cbb4513f286eb12c7647869b2795bf))
- The `TrustedWebActivityIntent` now includes Launch Handler API client mode that allows a browser to use this API. ([Ifc95c](https://android-review.googlesource.com/#/q/Ifc95c96d3fc0a05b9a7504bcbba3fffb927491e3))
- The `TrustedWebActivityIntent` now includes URIs of files opened via the app's registered intent filters, and grants the browser read-write permissions to those files. ([I2134a](https://android-review.googlesource.com/#/q/I2134a7579830e353add0263e2fb81cd23e8a569f))
- `TrustedWebActivityIntent` now includes the originally launched URL in its extras, adding context for the browser when used by Protocol Handlers. ([I3759a](https://android-review.googlesource.com/#/q/I3759aaa86304c7c050f1a582004508cbbb84b112))
- Added a new API to enable/disable the close button for Custom Tabs. ([I35acd](https://android-review.googlesource.com/#/q/I35acd34edac715e380d64ccb1c7e71385cda53b2))
- Added close button icon customization support to Auth Tab ([Iaf877](https://android-review.googlesource.com/#/q/Iaf8772cca56d2b7e8cce6268c1901ccc67bc76c5))

### Version 1.9.0-alpha01

January 29, 2025

`androidx.browser:browser:1.9.0-alpha01` is released. Version 1.9.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f1d7b329086e978fafe165ca234df67796d9a92e..4c47131cd5b50c3091fc0874eb606aaac5b168fa/browser/browser).

**API Changes**

- Added browser connection/session support to Auth Tab. ([I6e47b](https://android-review.googlesource.com/#/q/I6e47b7a841c377f28cce259de332996500261133))
- Added a new API `CustomTabsSession#isEphemeralBrowsingSupported` that determines whether or not the ephemeral browsing is supported ([Ie4dea](https://android-review.googlesource.com/#/q/Ie4deaf150c7383d103f35d53e8d2b58347c2a658), [b/384548523](https://issuetracker.google.com/issues/384548523))
- Added color scheme params support to Auth Tab APIs. ([I630e1](https://android-review.googlesource.com/#/q/I630e1b376ce3cd83f87dba53ab4b93c5c1d5ff5f))
- Added experimental ephemeral browsing option to Custom Tabs ([I9549d](https://android-review.googlesource.com/#/q/I9549d6225412bc794c14a3287032dd05641e66dd))
- Updated experimental Auth Tab APIs ([I8b674](https://android-review.googlesource.com/#/q/I8b6748d73a92c44e501b7a102e654391de068628))
- Add new API to check if the Custom Tabs provider supports multi-network. ([I4307a](https://android-review.googlesource.com/#/q/I4307ac67e44c1a759dc8a9a26f71a11d957b5d5e))
- Add new service intent filter category to support multi-network. ([I4354a](https://android-review.googlesource.com/#/q/I4354aab54371a98f7704f04628ec5600e88d24d3))
- Add new API to set/get the bound network when launching a URL over a custom tab. ([I493e1](https://android-review.googlesource.com/#/q/I493e126cdc9ff645cc75d3ff5fa5ee3fb1a08f8f))
- Added experimental Auth Tab APIs ([I9b4d4](https://android-review.googlesource.com/#/q/I9b4d43500679ee37e2c1b67db23f92f036122e17))
- New experimental APIs for `PendingSession` ([Ib40e5](https://android-review.googlesource.com/#/q/Ib40e5d1e94c4907e3757a6cbd39c6bab821e0fdf))

**Bug Fixes**

- Updated AuthTabIntent Javadocs ([I2490c](https://android-review.googlesource.com/#/q/I2490cc67381b5ceb8291dfd46186975df5fe5032))
- Fixed session support in Auth Tab ([I4e280](https://android-review.googlesource.com/#/q/I4e280651edcc598641d9fba7af08b11dac0c9fe9))
- This library now uses [JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler argument to enforce correct usage: `-Xjspecify-annotations=strict` (this is the default starting with version 2.1.0 of the Kotlin compiler). ([Ic7bf5](https://android-review.googlesource.com/#/q/Ic7bf5fdbbe82b84a4a02d6eb8f1d808eaf026479), [b/326456246](https://issuetracker.google.com/issues/326456246))
- Removed manual outlining of access to new platform APIs since this happens automatically via API modeling when using R8 with AGP 7.3 or later (e.g. R8 version 3.3) and for all builds when using AGP 8.1 or later (e.g. D8 version 8.1). Clients who are not using AGP are advised to update to D8 version 8.1 or later. See [this article](https://medium.com/androiddevelopers/mitigating-soft-verification-issues-in-r8-and-d8-7e9e06827dfd) for more details. ([I9496c](https://android-review.googlesource.com/#/q/I9496cfaeb50a5c484fbee6521b74a0605fb013dc), [b/345472586](https://issuetracker.google.com/issues/345472586))

**External Contribution**

- Introduce a new IPC call `ICustomTabsService#prefetchWithMultipleUrls` to avoid multiple IPC calls for single URLs. ([Ie5025](https://android-review.googlesource.com/#/q/Ie502555df6938e94add4611b71d6b9496ee22c9c))
- Make `CustomTabsSession#prefetch` propagate `CustomTabsSession`'s session `id(mID)` to `CustomTabsService`. ([I4ec7b](https://android-review.googlesource.com/#/q/I4ec7b0410988299c9f2cedfa9a1e14f3d887f210))
- Add a new experimental API`CustomTabsSession#prefetch(List<Uri>, PrefetchOptions)`, which overloads the existing API to accept multiple URLs. ([I54f35](https://android-review.googlesource.com/#/q/I54f357cc4f070b666bbff75610bd72ac5ffef0d4))
- Add a new experimental API `CustomTabsSession#prefetch(Uri, PrefetchOptions)`, which tries to prefetch the main page (without subresources) for future navigations. ([I340cf](https://android-review.googlesource.com/#/q/I340cf20cf10d1fa124c07d609146de860b0d2cd6))

## Version 1.8

### Version 1.8.0

March 6, 2024

`androidx.browser:browser:1.8.0` is released. Version 1.8.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/09ec43e34886ac2e43b54245cb5a598322cc37e4..f1d7b329086e978fafe165ca234df67796d9a92e/browser/browser).

**Important changes since 1.7.0**

- Added `CustomTabsIntent.Builder#setInitialActivityWidthPx` which allows developers to specify the initial launch width of a Custom Tab. ([I443f6](https://android-review.googlesource.com/#/q/I443f6f3295cde72d0eedf4deb41ada1597b30299))
- Added `CustomTabsIntent.Builder#setActivitySideSheetPosition` which allows developers to specify the Custom Tab's position when acting as a side sheet. ([I443f6](https://android-review.googlesource.com/#/q/I443f6f3295cde72d0eedf4deb41ada1597b30299))
- Added `CustomTabsIntent.Builder#setActivitySideSheetDecorationType` which allows developers to specify the Custom Tab's decoration type when it is acting as a side sheet. ([I443f6](https://android-review.googlesource.com/#/q/I443f6f3295cde72d0eedf4deb41ada1597b30299))
- Added `CustomTabsIntent.Builder#setActivitySideSheetRoundedCornersPosition` which allows developers to specify the position of the rounded corners when the Custom Tab is acting as a side sheet. ([I443f6](https://android-review.googlesource.com/#/q/I443f6f3295cde72d0eedf4deb41ada1597b30299))
- Added `CustomTabsIntent.Builder#setActivitySideSheetMaximizationEnabled` which allows developers to enable or disable the maximization button when the Custom Tab is acting as a side sheet. ([Ie3564](https://android-review.googlesource.com/#/q/Ie3564012ad9de81ce8feca5ddc38f1fb30f19cef))
- Added `onActivityLayout` callback method to interface `CustomTabsCallback` to let developers know the coordinates of the area occupied by the Custom Tab and the state in which it is being displayed. This will be called when the Custom Tab is first displayed on the screen and each time the occupied area changes. ([I443f6](https://android-review.googlesource.com/#/q/I443f6f3295cde72d0eedf4deb41ada1597b30299))
- Added `onWarmupCompleted` callback method to interface `CustomTabsCallback` to let developers know when `CustomTabsClient#warmupfinishes` warming up the browser process. ([I107cf](https://android-review.googlesource.com/#/q/I107cfe713e3a12971123e94b505fce44494dcc0f))
- Added the session id to extras in `CustomTabsSession#setEngagementSignalsCallback` and `CustomTabsSession#isEngagementSignalsApiAvailable`. ([Iba7f1](https://android-review.googlesource.com/#/q/Iba7f1e5be9cfe30ed69274e1fd016ef02cf5e13d))
- Added experimental support for Minimized Custom Tabs APIs. ([I67f2d](https://android-review.googlesource.com/#/q/I67f2d2186806af733b09b225aa48cc7464f69026))

### Version 1.8.0-rc01

February 21, 2024

`androidx.browser:browser:1.8.0-rc01` is released with no changes since 1.8.0-beta02. [Version 1.8.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ca2a8cf8da3a3502fccc593974f8085653e38261..ecf04c25eb8fcd718feb21e48d69764b3df656be/browser/browser)

### Version 1.8.0-beta02

February 7, 2024

`androidx.browser:browser:1.8.0-beta02` is released. [Version 1.8.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b5166f9a1e9c047162d1215884c3e2cd41a4a74a..ca2a8cf8da3a3502fccc593974f8085653e38261/browser/browser)

**API Changes**

- Renamed `CustomTabsIntent.Builder#setActivitySideSheetEnableMaximization` to `CustomTabsIntent Builder#setActivitySideSheetMaximizationEnabled` and made it a public API. It allows developers to enable or disable the maximization button when the Custom Tab is acting as a side sheet. ([Ie3564](https://android-review.googlesource.com/#/q/Ie3564012ad9de81ce8feca5ddc38f1fb30f19cef))

### Version 1.8.0-beta01

November 29, 2023

`androidx.browser:browser:1.8.0-beta01` is released. [Version 1.8.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/312eb9f1ddece3a18317f18515a877e0e745cb2c..b5166f9a1e9c047162d1215884c3e2cd41a4a74a/browser/browser)

**New Features**

- Add experimental support for Minimized Custom Tabs APIs. ([I67f2d](https://android-review.googlesource.com/#/q/I67f2d2186806af733b09b225aa48cc7464f69026))

### Version 1.8.0-alpha01

November 15, 2023

`androidx.browser:browser:1.8.0-alpha01` is released. [Version 1.8.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/312eb9f1ddece3a18317f18515a877e0e745cb2c/browser/browser)

**New Features**

- Added `CustomTabsIntent.Builder#setInitialActivityWidthPx` which allows developers to specify the initial launch width of a Custom Tab. ([I443f6](https://android-review.googlesource.com/#/q/I443f6f3295cde72d0eedf4deb41ada1597b30299))
- Added `CustomTabsIntent.Builder#setActivitySideSheetBreakpointDp` which allows developers to specify the minimum Custom Tabs window width in order for it to act as a side sheet. ([I443f6](https://android-review.googlesource.com/#/q/I443f6f3295cde72d0eedf4deb41ada1597b30299))
- Added `CustomTabsIntent.Builder#setActivitySideSheetPosition` which allows developers to specify the Custom Tab's position when acting as a side sheet. ([I443f6](https://android-review.googlesource.com/#/q/I443f6f3295cde72d0eedf4deb41ada1597b30299))
- Added `CustomTabsIntent.Builder#setActivitySideSheetEnableMaximization` which allows developers to enable or disable the maximization button when the Custom Tab is acting as a side sheet. ([I443f6](https://android-review.googlesource.com/#/q/I443f6f3295cde72d0eedf4deb41ada1597b30299))
- Added `CustomTabsIntent.Builder#setActivitySideSheetDecorationType` which allows developers to specify the Custom Tab's decoration type when it is acting as a side sheet. ([I443f6](https://android-review.googlesource.com/#/q/I443f6f3295cde72d0eedf4deb41ada1597b30299))
- Added `CustomTabsIntent.Builder#setActivitySideSheetRoundedCornersPosition` which allows developers to specify the position of the rounded corners when the Custom Tab is acting as a side sheet. ([I443f6](https://android-review.googlesource.com/#/q/I443f6f3295cde72d0eedf4deb41ada1597b30299))
- Added `onActivityLayout` callback method to interface `CustomTabsCallback` to let developers know the coordinates of the area occupied by the Custom Tab and the state in which it is being displayed. This will be called when the Custom Tab is first displayed on the screen and each time the occupied area changes. ([I443f6](https://android-review.googlesource.com/#/q/I443f6f3295cde72d0eedf4deb41ada1597b30299))
- Added `onWarmupCompleted` callback method to interface `CustomTabsCallback` to let developers know when `CustomTabsClient#warmup`finishes warming up the browser process. ([I107cf](https://android-review.googlesource.com/#/q/I107cfe713e3a12971123e94b505fce44494dcc0f))

**Bug Fixes**

- Added the session id to extras in `CustomTabsSession#setEngagementSignalsCallback` and `CustomTabsSession#isEngagementSignalsApiAvailable`. ([Iba7f1](https://android-review.googlesource.com/#/q/Iba7f1e5be9cfe30ed69274e1fd016ef02cf5e13d))

## Version 1.7

### Version 1.7.0

November 15, 2023

`androidx.browser:browser:1.7.0` is released. [Version 1.7.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9d1512626b03b7b079ea5d8c71ee3b9d2513284e..1067481a829ed7816785e1a9486a02f28cf772e9/browser/browser)

**Important changes since 1.6.0**

- Added `CustomTabsIntent.Builder#setBookmarksButtonEnabled` that enables the bookmarks button in the overflow menu. ([Ia792e](https://android-review.googlesource.com/#/q/Ia792eb29ee8953d83db9bad82d5ee10f1a221048))
- Added `CustomTabsIntent.Builder#setDownloadButtonEnabled` that enables the download button in the overflow menu. ([Ia792e](https://android-review.googlesource.com/#/q/Ia792eb29ee8953d83db9bad82d5ee10f1a221048))
- Added `CustomTabsIntent.Builder#setSendToExtraDefaultHandlerEnabled` that enables sending initial urls to external handler apps. ([Ia792e](https://android-review.googlesource.com/#/q/Ia792eb29ee8953d83db9bad82d5ee10f1a221048))
- Added `CustomTabsIntent.Builder#setTranslateLanguage` that specifies the target language that the Translate UI should be triggered with. ([Ia792e](https://android-review.googlesource.com/#/q/Ia792eb29ee8953d83db9bad82d5ee10f1a221048))
- Added `CustomTabsIntent.Builder#setBackgroundInteractionEnabled` that enables interactions with the background app when a partial Custom Tab is launched. ([Ia792e](https://android-review.googlesource.com/#/q/Ia792eb29ee8953d83db9bad82d5ee10f1a221048))
- Added `CustomTabsIntent.Builder#setShareIdentityEnabled` that allows Custom Tabs to obtain the caller's identity. ([I7bf2b](https://android-review.googlesource.com/#/q/I7bf2b2db541398f64af772f34ede7635a216fde8))
- Added `CustomTabsIntent.Builder#setSecondaryToolbarSwipeUpGesture` that sets a `PendingIntent` to be sent when the user swipes up from the bottom toolbar. ([Id42a2](https://android-review.googlesource.com/#/q/Id42a2a75706c6bd966f417c470ec8a710e383fe7))

### Version 1.7.0-rc01

November 1, 2023

`androidx.browser:browser:1.7.0-rc01` is released with no changes. [Version 1.7.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/465c5c5b7a0d79793bddb26a695f67aba8ea2f7e..9d1512626b03b7b079ea5d8c71ee3b9d2513284e/browser/browser)

- No changes since alpha-01

### Version 1.7.0-beta01

October 18, 2023

`androidx.browser:browser:1.7.0-beta01` is released with no changes. [Version 1.7.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1f7407d4293384a1b91bc142880e3525048b3443..465c5c5b7a0d79793bddb26a695f67aba8ea2f7e/browser/browser)

### Version 1.7.0-alpha01

October 4, 2023

`androidx.browser:browser:1.7.0-alpha01` is released. [Version 1.7.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ea66264efd648941dbef6190bbd7ac87158fbb3c..1f7407d4293384a1b91bc142880e3525048b3443/browser/browser)

**New Features**

- Added `CustomTabsIntent.Builder#setBookmarksButtonEnabled` that enables the bookmarks button in the overflow menu. ([Ia792e](https://android-review.googlesource.com/#/q/Ia792eb29ee8953d83db9bad82d5ee10f1a221048))
- Added `CustomTabsIntent.Builder#setDownloadButtonEnabled` that enables the download button in the overflow menu. ([Ia792e](https://android-review.googlesource.com/#/q/Ia792eb29ee8953d83db9bad82d5ee10f1a221048))
- Added `CustomTabsIntent.Builder#setSendToExtraDefaultHandlerEnabled` that enables sending initial urls to external handler apps. ([Ia792e](https://android-review.googlesource.com/#/q/Ia792eb29ee8953d83db9bad82d5ee10f1a221048))
- Added `CustomTabsIntent.Builder#setTranslateLanguage` that specifies the target language that the Translate UI should be triggered with. ([Ia792e](https://android-review.googlesource.com/#/q/Ia792eb29ee8953d83db9bad82d5ee10f1a221048))
- Added `CustomTabsIntent.Builder#setBackgroundInteractionEnabled` that enables interactions with the background app when a partial Custom Tab is launched. ([Ia792e](https://android-review.googlesource.com/#/q/Ia792eb29ee8953d83db9bad82d5ee10f1a221048))
- Added `CustomTabsIntent.Builder#setShareIdentityEnabled` that allows Custom Tabs to obtain the caller's identity. ([I7bf2b](https://android-review.googlesource.com/#/q/I7bf2b2db541398f64af772f34ede7635a216fde8))
- Added `CustomTabsIntent.Builder#setSecondaryToolbarSwipeUpGesture` that sets a `PendingIntent` to be sent when the user swipes up from the bottom toolbar. ([Id42a2](https://android-review.googlesource.com/#/q/Id42a2a75706c6bd966f417c470ec8a710e383fe7))

## Version 1.6

### Version 1.6.0

August 9, 2023

`androidx.browser:browser:1.6.0` is released with no changes since 1.6.0-rc01. [Version 1.6.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c5e57cbdcd8a7ad77b46e5b6f258c9bbc4dafd9b..ea66264efd648941dbef6190bbd7ac87158fbb3c/browser/browser)

### Version 1.6.0-rc01

July 26, 2023

`androidx.browser:browser:1.6.0-rc01` is released with no changes since 1.6.0-beta01. [Version 1.6.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3b5b931546a48163444a9eddc533489fcddd7494..c5e57cbdcd8a7ad77b46e5b6f258c9bbc4dafd9b/browser/browser)

### Version 1.6.0-beta01

June 21, 2023

`androidx.browser:browser:1.6.0-beta01` is released with no changes since 1.6.0-alpha02. [Version 1.6.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/73f902dee011bfe400d8a0330bfd8d4bb632065f..3b5b931546a48163444a9eddc533489fcddd7494/browser/browser)

### Version 1.6.0-alpha02

June 7, 2023

`androidx.browser:browser:1.6.0-alpha02` is released. [Version 1.6.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6f3ac2bd197d5e61ab2708125b57d6ae4003ad68..73f902dee011bfe400d8a0330bfd8d4bb632065f/browser/browser)

**API Changes**

- Removed `CustomTabsSession#getGreatestScrollPercentage`. ([I6c5ba](https://android-review.googlesource.com/#/q/I6c5bac0dfc95e4f0b71e521bafacf0f32bb20dfb))
- Added a new `requestPostMessageChannel` API which allows specifying the target origin. This means that users can be certain their messages are delivered only to the website they expect. ([Id5b7f](https://android-review.googlesource.com/#/q/Id5b7f9c1b6e6f40552a8c922234e8412f8927016))

**Bug Fixes**

- Updated `EngagementSignalsCallback` documentation. ([Ie833c](https://android-review.googlesource.com/#/q/Ie833cc42e96378b7b33d76114d0873f68a1ce59e))

### Version 1.6.0-alpha01

May 3, 2023

`androidx.browser:browser:1.6.0-alpha01` is released. [Version 1.6.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/aaba505f4fbf7aa68c09dc54b739d051a7e6b30d..6f3ac2bd197d5e61ab2708125b57d6ae4003ad68/browser/browser)

**New Features**

- Added Engagement Signals API, which allows developers to receive callbacks for user interactions on the web page such as scrolls. ([I835e6](https://android-review.googlesource.com/#/q/I835e60827e8f409c8ba490d7a05c1b2b347635a5))

**API Changes**

- Updated Engagement Signals API to simplify the API surface on the Custom Tabs implementation side. ([Iaa6dc](https://android-review.googlesource.com/#/q/Iaa6dcac86483556f0594a9a8254082e4c67c2da0))

## Version 1.5

### Version 1.5.0

February 8, 2023

`androidx.browser:browser:1.5.0` is released. [Version 1.5.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3014ca1f861c35628c0ee39f2a92979b003b4af0..aaba505f4fbf7aa68c09dc54b739d051a7e6b30d/browser/browser)

**Important changes since 1.4.0**

- Added `CustomTabsIntent.Builder#setInitialActivityHeightPx`, which allows developers to specify the initial launch height of a Custom Tab, and optionally the resize behavior (fixed or resizable). ([I48bd3](https://android-review.googlesource.com/c/platform/frameworks/support/+/2201783))
- Added `CustomTabsIntent.Builder#setToolbarCornerRadiusDp` which allows developers to specify the toolbar's top corner radius. ([I48bd3](https://android-review.googlesource.com/c/platform/frameworks/support/+/2201783))
- Added `CustomTabsIntent.Builder#setCloseButtonPosition` which allows developers to set the position of the close button on the toolbar. ([I48bd3](https://android-review.googlesource.com/c/platform/frameworks/support/+/2201783))
- Added an `onActivityResized` callback method to interface `CustomTabsCallback` to let developers know when a Custom Tab is resized. ([Ic864e](https://android-review.googlesource.com/c/platform/frameworks/support/+/2282111))
- Make parts of `CustomTabsCallback` APIs asynchronous. ([Ic86df](https://android-review.googlesource.com/c/platform/frameworks/support/+/2296397))
- Populates the current app's language in Accept-Language by default to align to Android's per-app language experience. ([I3d1d7](https://android-review.googlesource.com/c/platform/frameworks/support/+/2238200))
- Added `@RequiresPermission` to APIs that require granting the `POST_NOTIFICATIONS` permission on SDK 33 and above. This was developed in an internal branch. [b/238790278](https://issuetracker.google.com/issues/238790278) for reference.

### Version 1.5.0-rc01

January 25, 2023

`androidx.browser:browser:1.5.0-rc01` is released. [Version 1.5.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/adf1c279a86ab3886e1666c08e2c3efba783367b..3014ca1f861c35628c0ee39f2a92979b003b4af0/browser/browser)

- No changes since 1.5.0-beta01.

### Version 1.5.0-beta01

January 11, 2023

`androidx.browser:browser:1.5.0-beta01` is released. [Version 1.5.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4a2f5e696614339c1ac21f706c1a17c0285780e7..adf1c279a86ab3886e1666c08e2c3efba783367b/browser/browser)

- No changes since 1.5.0-alpha02

### Version 1.5.0-alpha02

December 7, 2022

`androidx.browser:browser:1.5.0-alpha02` is released. [Version 1.5.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/548c8ac2570ae6cf15798fea1380491f7d93796b..4a2f5e696614339c1ac21f706c1a17c0285780e7/browser/browser)

**API Changes**

- Changed the `CustomTabsCallback#onActivityResized` behavior and added new parameters to it.
- Renamed `EXTRA_ACTIVITY_RESIZE_BEHAVIOR` to `EXTRA_ACTIVITY_RESIZE_HEIGHT_BEHAVIOR` to better reflect that it is height specific. ([Ic864e](https://android-review.googlesource.com/#/q/Ic864e35d84188422f9a40d3535d559dcac23760c))
- Make parts of `CustomTabsCallback` APIs asynchronous. ([Ic86df](https://android-review.googlesource.com/#/q/Ic86df723f86dce0619a0bb0bdfb9ec6111c56711))

### Version 1.5.0-alpha01

October 24, 2022

`androidx.browser:browser:1.5.0-alpha01` is released. [Version 1.5.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/cd9e194d80b7be5c6e04a2eedb05c6451db89138..548c8ac2570ae6cf15798fea1380491f7d93796b/browser/browser)

**New Features**

- Added `CustomTabsIntent.Builder#setInitialActivityHeightPx`, which allows developers to specify the initial launch height of a Custom Tab, and optionally the resize behavior (fixed or resizable). ([I48bd3](https://android-review.googlesource.com/q/I48bd3f5ceebfac5b9a479c0da555d50f1c3e1725))
- Added `CustomTabsIntent.Builder#setToolbarCornerRadiusDp` which allows developers to specify the toolbar's top corner radius. ([I48bd3](https://android-review.googlesource.com/q/I48bd3f5ceebfac5b9a479c0da555d50f1c3e1725))
- Added `CustomTabsIntent.Builder#setCloseButtonPosition` which allows developers to set the position of the close button on the toolbar. ([I48bd3](https://android-review.googlesource.com/q/I48bd3f5ceebfac5b9a479c0da555d50f1c3e1725))
- Added an `onActivityResized` callback method to interface CustomTabsCallback to let developers know when a Custom Tab is resized (expanded to full height or minimized back down to initial launch height). ([Id99ce](https://android-review.googlesource.com/q/Id99ce496f15c9d379d0b29872036053d1c81fcce))
- Populates the current app's language in Accept-Language by default to align to Android's per-app language experience. ([I3d1d7](https://android-review.googlesource.com/q/I3d1d7530dcf6f0d01a1893046cc3f280ac556e9e))

**API Changes**

- Added `@RequiresPermission` to APIs that require granting the `POST_NOTIFICATIONS` permission on SDK 33 and above. This was developed in an internal branch. [b/238790278](https://issuetracker.google.com/issues/238790278) for reference.

## Version 1.4.0

### Version 1.4.0

November 3, 2021

`androidx.browser:browser:1.4.0` is released. [Version 1.4.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bbc22b0da7f8b1bbe5494736312e209292fd0301..cd9e194d80b7be5c6e04a2eedb05c6451db89138/browser/browser)

**Important changes since 1.3.0**

- Mark PendingIntents as PendingIntent.FLAG_IMMUTABLE for Android 12 compatibility.

### Version 1.4.0-rc01

October 13, 2021

`androidx.browser:browser:1.4.0-rc01` is released with no changes since 1.4.0-beta01. [Version 1.4.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1f6bc4d47b7be46a5af151ed726e84db0a1cf9f9..bbc22b0da7f8b1bbe5494736312e209292fd0301/browser/browser)

### Version 1.4.0-beta01

September 29, 2021

`androidx.browser:browser:1.4.0-beta01` is released with no change since `1.4.0-alpha01`. [Version 1.4.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1a3dcfb231517d6104969f17063fcc6c97ba6eeb..1f6bc4d47b7be46a5af151ed726e84db0a1cf9f9/browser/browser)

### Version 1.4.0-alpha01

September 15, 2021

`androidx.browser:browser:1.4.0-alpha01` is released. [Version 1.4.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4436a75295c6b47ff1457df6f8a736bbd1ea6d85..1a3dcfb231517d6104969f17063fcc6c97ba6eeb/browser/browser)

**Bug Fixes**

- Mark PendingIntents as `PendingIntent.FLAG_IMMUTABLE` for Android 12 compatibility.

## Version 1.3.0

### Version 1.3.0

December 2, 2020

`androidx.browser:browser:1.3.0` is released. [Version 1.3.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/845c8ef508496f2f7d15f6969679e18a00036b9a..4436a75295c6b47ff1457df6f8a736bbd1ea6d85/browser/browser)

**Major features since 1.2.0**

- Free form commands can be passed from a browser to a Trusted Web Activity client by calling `TrustedWebActivityServiceConnection#sendExtraCommand`. The client can handle these in `TrustedWebActivityService#onExtraCommand`
- Added `TrustedWebActivityCallback` interface that can be used by a Trusted Web Activity client to return data to the browser.
- Added `CustomTabsIntent#setShareState`, which allows developers to specify whether to show a share option or not (or leave it up to the browser).
- Developers can now set a default screen orientation with `setScreenOrientation` method in `TrustedWebActivityIntentBuilder`
- `setNavigationBarDividerColor` method is added to `CustomTabColorSchemeParams` to support changing the color of the navigation bar divider.
- Added `CustomTabsIntent.Builder#setDefaultColorSchemeParams` to replace the now deprecated `#setNavigationBarColor`, `#setNavigationBarDividerColor`, `#setToolbarColor` and `#setSecondaryToolbarColor` methods
- Added the `CustomTabsClient#bindCustomTabsServicePreservePriority` method, allowing connecting to a Custom Tabs Service without using the `Context.BIND_WAIVE_PRIORITY` flag.

### Version 1.3.0-rc01

November 11, 2020

`androidx.browser:browser:1.3.0-rc01` is released with no changes since `1.3.0-beta01`. [Version 1.3.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/234e23e470a5e7f81291f6acd12d538146dc010b..845c8ef508496f2f7d15f6969679e18a00036b9a/browser)

### Version 1.3.0-beta01

October 28, 2020

`androidx.browser:browser:1.3.0-beta01` is released. [Version 1.3.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f5a2c7477391539d8bc9f65a8f0db1e8a7bf2cf5..234e23e470a5e7f81291f6acd12d538146dc010b/browser/browser)

**API Changes**

- Renamed `bindCustomTabServicePreservePriority` to `bindCustomTabsServicePreservePriority` ([I29ac1](https://android-review.googlesource.com/#/q/I29ac1c28e03286401582b9b8fa70db20cff9da2e))

**Bug Fixes**

- API lint check for `MissingGetterMatchingBuilder` is enabled for androidx ([I4bbea](https://android-review.googlesource.com/#/q/I4bbeacf9869d8338a3d7086acb40bc56ec68c3f9), [b/138602561](https://issuetracker.google.com/issues/138602561))

### Version 1.3.0-alpha06

October 1, 2020

`androidx.browser:browser:1.3.0-alpha06` is released. [Version 1.3.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/316f882e649c600372170f013a18515f590f490d..f5a2c7477391539d8bc9f65a8f0db1e8a7bf2cf5/browser/browser)

**New Features**

- Adds CustomTabsIntent#setShareState which allows the developer to set share state to either enabled, disabled or leave it up to the browser. ([I153fe](https://android-review.googlesource.com/#/q/I153fed30ea5814474c76dada550f49abede472f3))
- Adds CustomTabsIntent.Builder#setDefaultColorSchemeParams which should be used in place of the now deprecated #setNavigationBarColor, #setNavigationBarDividerColor, #setToolbarColor, #setSecondaryToolbarColor methods.([I09012](https://android-review.googlesource.com/#/q/I09012a8e3f03f1f191d48f1b0beaf496b28f0cfb))

**API Changes**

- API lint check for the StaticFinalBuilder is enabled for androidx ([I2b11b](https://android-review.googlesource.com/#/q/I2b11be1bb370e178e3e0d1d1083d43af38eece23), [b/138602561](https://issuetracker.google.com/issues/138602561))
- Adds CustomTabsService#KEY_SUCCESS and TrustedWebActivityService#KEY_SUCCESS that can be used for indicating extraCommand is success. ([I6f7b5](https://android-review.googlesource.com/#/q/I6f7b55d173b4df07e742ba44e3f4b41306fd3640))

### Version 1.3.0-alpha05

August 5, 2020

`androidx.browser:browser:1.3.0-alpha05` is released. [Version 1.3.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b6054a1a7396b962ac2c6d80d21053cf9d2f02db..316f882e649c600372170f013a18515f590f490d/browser/browser)

**New Features**

- Allow setting the orientation of launched Trusted Web Activities.
- Allow setting the navigation bar divider color for Trusted Web Activities and Custom Tabs.

**API Changes**

- Added a `setScreenOrientation` method in `TrustedWebActivityIntentBuilder`.
- Added an `@IntDef` for `ScreenOrientation.LockType` to represent a lock type ([I802d2](https://android-review.googlesource.com/#/q/I802d2f0365a944cb9a4c651d470dbaf847a9e897))
- Added the `setNavigationBarDividerColor` method to `TrustedWebActivityIntentBuilder` and `CustomTabColorSchemeParams`. ([Ia04dd](https://android-review.googlesource.com/#/q/Ia04ddf4f141e6e48ef2e25c88f9f2f101c5b3599))
  - Added `@IntDef`s to `TrustedWebActivityIntentBuilder`methods that take a color scheme.

### Version 1.3.0-alpha04

June 24, 2020

`androidx.browser:browser:1.3.0-alpha04` is released. [Version 1.3.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bea4dafe72ba1ec91a105da3128954d5ed7f1cd0..b6054a1a7396b962ac2c6d80d21053cf9d2f02db/browser/browser)

**New Features**

- Added the `CustomTabsClient#bindCustomTabServicePreservePriority` method, allowing connecting to a Custom Tabs Service without using the `Context.BIND_WAIVE_PRIORITY` flag.

### Version 1.3.0-alpha03

June 10, 2020

`androidx.browser:browser:1.3.0-alpha03` is released. [Version 1.3.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/14041ec7183a12ffd22ec024d26202e0101a3790..bea4dafe72ba1ec91a105da3128954d5ed7f1cd0/browser/browser)

**New Features**

- Added `TrustedWebActivityCallback` interface that can be used by a Trusted Web Activity client to return data to the browser. ([I64dbb](https://android-review.googlesource.com/c/platform/frameworks/support/+/1267733))

**API Changes**

- `TrustedWebActivityServiceConnection.extraCommand` now also takes a `@Nullable` `TrustedWebActivityCallback` parameter. The bundle parameter is now marked as `@NonNull` instead of `@Nullable`. ([I64dbb](https://android-review.googlesource.com/c/platform/frameworks/support/+/1267733))
- `TrustedWebActivityServiceConnection.extraCommand` method has been renamed to `sendExtraCommand` ([Id29a8](https://android-review.googlesource.com/c/platform/frameworks/support/+/1320096))
- `CustomTabsIntent.Builder#addDefaultShareMenuItem()` has been deprecated in favor of the new `#setDefaultShareMenuItemEnabled(boolean)` and `CustomTabsIntent.Builder#enableUrlBarHiding()` has been deprecated in favor of the new `#setUrlBarHidingEnabled(boolean)`. ([Iad702](https://android-review.googlesource.com/c/platform/frameworks/support/+/1321806))

### Version 1.3.0-alpha01

January 8, 2020

`androidx.browser:browser:1.3.0-alpha01` is released. [Version 1.3.0-alpha01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/6e847a4064cdda740b778d560b1db477e13e0772..14041ec7183a12ffd22ec024d26202e0101a3790/browser).

**New features**

- Free form commands can be passed from a browser to a Trusted Web Activity client by calling `TrustedWebActivityServiceConnection#extraCommand`. The client can handle these in `TrustedWebActivityService#onExtraCommand`.

**API changes**

- The URL provided to `CustomTabsSession#mayLauncherUrl` and received in `CustomTabsService#mayLaunchUrl` has been made `@Nullable`.

## Version 1.2.0

### Version 1.2.0

December 18, 2019

`androidx.browser:browser:1.2.0` is released with no changes since `1.2.0-rc01`. [Version 1.2.0 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/2cf2b71971967b7ca0469a45ac470a0d303dc437..6e847a4064cdda740b778d560b1db477e13e0772/browser).

**Major changes since 1.0.0**

- **Trusted Web Activities**
  - Support for [Trusted Web Activities](https://developers.google.com/web/updates/2019/02/using-twa) is now stable.
  - The `TrustedWebActivityIntentBuilder` can be used to customize and create a `TrustedWebActivityIntent`, to launch a Trusted Web Activity.
  - The `TrustedWebActivityService` can be included or extended to allow clients to display web push notifications handed to them by the browser.
  - The `TrustedWebActivityServiceConnectionPool` can be used by browsers to connect to the `TrustedWebActivityService`s in clients. A `TrustedWebActivityServiceConnection` represents such a connection.
  - Trusted Web Activities can be launched providing information to a Web Share Target.
- **Dark Theme**
  - Developers can provide (through `CustomTabColorSchemeParams`) different theme colors to be used when the device is in light or dark mode.
  - Developers can request that the browser itself is in light or dark mode.
- **Session resumption**
  - `CustomTabsSession`s can be created with an id, allowing subsequent Custom Tabs launches from the same client and id to be merged.
- The navigation bar colour can be specified for Custom Tabs.
- Browser Actions related classes are marked deprecated due to incredibly low feature usage and will be removed in a future version of the library.

### Version 1.2.0-rc01

December 4, 2019

`androidx.browser:browser:1.2.0-rc01` is released. [Version 1.2.0-rc01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/134a51a9d15b3760a26431637d27019816a8b4d5..2cf2b71971967b7ca0469a45ac470a0d303dc437/browser).

**Bug fixes**

- Javadoc formatting for code samples was fixed.

### Version 1.2.0-beta01

November 20, 2019

`androidx.browser:browser:1.2.0-beta01` is released with no changes since `1.2.0-alpha09`. [Version 1.2.0-beta01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/5ce6d3ab9df61dc34670503ed762053d336a09c0..134a51a9d15b3760a26431637d27019816a8b4d5/browser).

### Version 1.2.0-alpha09

October 23, 2019

`androidx.browser:browser:1.2.0-alpha09` is released. [Version 1.2.0-alpha09 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/5859e2fea48acda3c5a0216e2973e71a7ce75538..5ce6d3ab9df61dc34670503ed762053d336a09c0/browser).

**New features**

- The `Token` class can be used to represent the identity of a package, it contains both the package name and the signature of the package's signing certificate.
  - It is designed to be serialized to a byte\[\] for persistence.
  - It is used by the `TrustedWebActivityService` to determine what TWA provider is allowed to connect to it.
  - It is used by the `TrustedWebActivityConnectionPool` by the TWA provider to determine which packages are valid to connect to.
- The `TokenStore` interface is now used by the `TrustedWebActivityService` to determine which app is allowed to connect to it.
  - It is up to the client to call `TokenStore#store`, `TrustedWebActivityService` only loads the Tokens.
- The `TrustedWebActivityServiceConnectionPool` (previously TrustedWebActivityServiceConnectionManager) no longer stores the set of verified packages:
  - `registerClient` and `getVerifiedPackages` have now been removed.
  - The collection of verified packages is now provided manually to `execute` (previously `connect`) and `serviceExistsForScope`.
- The `TrustedWebActivityService` delegates to the overriding class to store the verified provider.
  - `setVerifiedProvider` has been removed.
  - The client must implement `getTokenStore` which returns a `TokenStore` that can be used to store and retrieve a `Token`.

**API changes**

- The `TrustedWebActivityServiceConnectionManager` class:
  - Is now called `TrustedWebActivityServiceConnectionPool`.
  - Is now final.
  - Is constructed by the static `create` method instead of a public constructor.
- The `TrustedWebActivityService` class:
  - Has thread annotations on overridable methods.
- The `TrustedWebActivityServiceWrapper` class:
  - Is now called `TrustedWebActivityServiceConnection`.
  - Is now final.
  - Now throws raw RemoteExceptions instead of wrapping them in RuntimeExceptions.
- The `ShareTarget#FileFormField` class is now final.
- The `TrustedWebUtils#splashScreensAreSupported` method has been renamed to `areSplashScreensSupported`.
- The `TrustedWebActivityIntentBuilder#getUrl` method has been renamed to `TrustedWebActivityIntentBuilder#getUri`.
- The `SplashScreenParamKey` static fields have been prefixed with `KEY_`.

### Version 1.2.0-alpha08

September 18, 2019

`androidx.browser:browser:1.2.0-alpha08` is released. [Version 1.2.0-alpha08 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/aa4d9f606c70daf3cbd6033de426e84d21930733..dfdbbcb30249aa226e33ebb323f7d12ad692297a/browser).
| **Note:** This version is dependent on the Java 8 programming language. Please read [Use Java 8 language features](https://developer.android.com/studio/write/java8-support) to learn how to use it in your project.

**New features**

- Introduced new Share Target APIs for Trusted Web Activities. Apps that use Trusted Web Activities can now send data to their Web Share Target, defined by the protocol https://wicg.github.io/web-share-target/level-2/ ([aosp/I47b93](https://android-review.googlesource.com/#/q/I47b938f8d5844023ea65c108f974d5c31a49d61a), [aosp/I0ec3e](https://android-review.googlesource.com/#/q/I0ec3eec2207fa1544c626e2e1da6268ead18f107))

**API changes**

- Added the callback `extraCallbackWithResult` to `ICustomTabsCallback` ([aosp/Ic2cc2](https://android-review.googlesource.com/#/q/Ic2cc2ec9e99c81505b0db255a9abb45aa46e630f))
- Marked some `CustomTabsSession` method parameters as Nullable or NonNull ([aosp/Iec460](https://android-review.googlesource.com/#/q/Iec46074608a642e069869a65fd867788ccbe2f8c))
- `TrustedWebActivityIntentBuilder` now builds a `TrustedWebActivityIntent` instead of a raw intent ([aosp/I03fb6](https://android-review.googlesource.com/#/q/I03fb621220dd24cd59095ded8c55bba70305f6d3))

**Bug fixes**

- `CustomTabsClient` now uses the legacy `requestPostMessageChannel` if needed ([aosp/Ibb324](https://android-review.googlesource.com/#/q/Ibb3240646c931197a5a0ea16e3d3178b1f3f129d))
- Fixed `CustomTabsSessionToken#equals` ([aosp/I7f249](https://android-review.googlesource.com/#/q/I7f24900ab94725bb8e31faf0c3cd93561f2709d6))
- `CustomTabsClient` now uses the legacy `newSession` if possible ([aosp/Ie27dc](https://android-review.googlesource.com/#/q/Ie27dc5443050cc14b5509d1486e56dc73654eae4))

**External contribution**

- API lint check for the MinMaxConstant is enabled for androidx ([aosp/I29b78](https://android-review.googlesource.com/#/q/I29b78a0a024984113ca37145f1cb2a31a82c7b25)) ([b/138602561](https://issuetracker.google.com/issues/138602561))

### Version 1.2.0-alpha07

August 7, 2019
| **Note:** This version is dependent on the Java 8 programming language. Please read [Use Java 8 language features](https://developer.android.com/studio/write/java8-support) to learn how to use it in your project.

`androidx.browser:browser:1.2.0-alpha07` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/50a39caa72955aae0c75225fd9805ab537cbf049..ece690f1fdb4481b47c5128fd21d88da7d6850a6/browser).
| **Note:** This version is dependent on the Java 8 programming language. Please read [Use Java 8 language features](https://developer.android.com/studio/write/java8-support) to learn how to use it in your project.

**New features**

- **Dark Theme**

  - Developers can provide theme colors to be used when the device is in dark mode.
  - Developers can also override whether the launched browser should be in dark or light mode.
  - The navigation bar color can be specified for Custom Tabs.
- **Trusted Web Activities**

  - The `TrustedWebActivityBuilder` can be used to easily create and launch [Trusted Web Activities](https://developers.google.com/web/updates/2019/02/using-twa).
  - The `TrustedWebActivityService` and related classes can be used to communicate with the provider - accepting web push notifications for the linked website and displaying them from the client app. This part of the API is liable to change.
- **Custom Tab Session Ids**

  - Custom Tabs sessions can now be created with ids, allowing the merging of two sessions launched by the same application with the same id.

**API changes**

- Browser Actions related classes and methods have been marked deprecated. Unfortunately, while we had high hopes for the feature, barely anyone ended up using it and only one browser ended up providing support for it. We're deprecating it to keep the code and the API simple.

## Version 1.0.0

### Version 1.0.0

September 21, 2018

browser-1.0.0 is released.