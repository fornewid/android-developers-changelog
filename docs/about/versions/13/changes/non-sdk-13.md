---
title: https://developer.android.com/about/versions/13/changes/non-sdk-13
url: https://developer.android.com/about/versions/13/changes/non-sdk-13
source: md.txt
---

Android 13 includes updated lists of restricted non-SDK
interfaces based on collaboration with Android developers and the latest
internal testing. Whenever possible, we make sure that public alternatives are
available before we restrict non-SDK interfaces.

If your app does not target Android 13, some of these changes
might not immediately affect you. However, while you can currently use some
non-SDK interfaces ([depending on your app's target API
level](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#list-names)),
using any non-SDK method or field always carries a high risk of breaking your
app.

If you are unsure if your app uses non-SDK interfaces, you can [test your
app](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#test-for-non-sdk)
to find out. If your app relies on non-SDK interfaces, you should begin planning
a migration to SDK alternatives. Nevertheless, we understand that some apps have
valid use cases for using non-SDK interfaces. If you cannot find an alternative
to using a non-SDK interface for a feature in your app, you should [request a
new public API](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#feature-request).

## List changes for Android 13

The list changes in Android 13 fall into the following category:

- Non-SDK interfaces that were unsupported in Android 12 (API level 31) that are [blocked in Android 13](https://developer.android.com/about/versions/13/changes/non-sdk-13#new-blocked).

For a complete list of all non-SDK interfaces for Android 13, download the
following file:

File: [`hiddenapi-flags.csv`](https://dl.google.com/developers/android/tm/non-sdk/hiddenapi-flags.csv)

SHA-256 checksum: `233a277aa8ac475b6df61bffd95665d86aac6eb2ad187b90bf42a98f5f2a11a3`

### Non-SDK interfaces that are now blocked in Android 13

The following code box lists all of the non-SDK interfaces that were unsupported
in Android 12 (API level 31) that are blocked in Android 13 (API level 33). That
is, these interfaces belong to the `max-target-s` list, so your app can only use
these interfaces if it targets Android 12 (API level 31) or lower.

Our goal is to make sure that public alternatives are available before we
restrict non-SDK interfaces, and we understand that your app might have a valid
use case for using these interfaces. If an interface that your app uses in a
prior version is now blocked in Android 13, you should [request a new public
API](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#feature-request)
for that interface.

```
Landroid/app/Activity;->setDisablePreviewScreenshots(Z)V # Use https://developer.android.com/reference/android/app/Activity#setRecentsScreenshotEnabled(boolean) instead.
Landroid/os/PowerManager;->isLightDeviceIdleMode()Z # Use https://developer.android.com/reference/android/os/PowerManager#isDeviceLightIdleMode() instead.
Landroid/os/Process;->setArgV0(Ljava/lang/String;)V # In general, do not try to change the process name. If you must change the process name (for instance, for debugging), you can use pthread_setname_np() instead, though be aware that doing this might confuse the system.
Landroid/view/accessibility/AccessibilityInteractionClient;->clearCache(I)V # Use https://developer.android.com/reference/android/accessibilityservice/AccessibilityService#clearCache() instead.
```