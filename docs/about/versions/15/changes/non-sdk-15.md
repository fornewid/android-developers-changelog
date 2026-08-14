---
title: https://developer.android.com/about/versions/15/changes/non-sdk-15
url: https://developer.android.com/about/versions/15/changes/non-sdk-15
source: md.txt
---

Android 15 includes updated lists of restricted non-SDK
interfaces based on collaboration with Android developers and the latest
internal testing. Whenever possible, we make sure that public alternatives are
available before we restrict non-SDK interfaces.

If your app does not target Android 15, some of these changes
might not immediately affect you. However, while it's possible for your app to
access some non-SDK interfaces
[depending on your app's target API level](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#list-names)), using any non-SDK
method or field always carries a high risk of breaking your app.

If you are unsure if your app uses non-SDK interfaces, you can
[test your app](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#test-for-non-sdk) to find out. If your app relies on non-SDK
interfaces, you should begin planning a migration to SDK alternatives.
Nevertheless, we understand that some apps have valid use cases for using
non-SDK interfaces. If you can't find an alternative to using a non-SDK
interface for a feature in your app, you should
[request a new public API](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#feature-request).

For a complete list of all non-SDK interfaces for Android 15, download the
following file:

File: [`hiddenapi-flags.csv`](https://dl.google.com/developers/android/vic/non-sdk/hiddenapi-flags.csv)

SHA-256 checksum: `40134e205e58922a708c453726b279a296e6a1f34a988abd90cec0f3432ea5a9`