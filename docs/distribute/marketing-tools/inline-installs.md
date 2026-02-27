---
title: https://developer.android.com/distribute/marketing-tools/inline-installs
url: https://developer.android.com/distribute/marketing-tools/inline-installs
source: md.txt
---

This page describes how app developers can integrate *inline install*, a new
test feature for Google Play that presents Google Play app product details in a
half sheet interface. Inline install enables users to experience a seamless app
install flow without leaving the context of the app. App developers can
integrate and test the inline install feature for Play distributed or updated
apps.

## Requirements

For the half sheet interface to appear in an app:

- The minimum Google Play version must be **40.4**.
- The Android API level must be **23 or higher**.

## Invoke inline installs from an app

To invoke inline install half sheet from an app, create an instance of the
[`Intent`](https://developer.android.com/reference/android/content/Intent) class, which opens a deep link
URL. Use the following sample code (Kotlin or Java) as a guideline.

### Kotlin

```kotlin
val intent = Intent(Intent.ACTION_VIEW)
val referrer = "<Your referrer string>"
val id = "<Package name of the app that is to be installed>"
val callerId = "<Package name of your app>"
intent.setPackage("com.android.vending")
val deepLinkUrl = "https://play.google.com/d?id=$id&referrer=$referrer&listing=$csl_id"
intent.data = Uri.parse(deepLinkUrl)
intent.putExtra("overlay", true)
intent.putExtra("callerId", "$callerId")
val packageManager = context.getPackageManager()
if (intent.resolveActivity(packageManager) != null) {
  startActivityForResult(intent, 0)
} else {
  // Fallback to deep linking to full Play Store.
}
```

### Java

```java
Intent intent = new Intent(Intent.ACTION_VIEW);
String referrer = "<Your referrer string>";
String id = "<Package name of the app that is to be installed>";
String callerId = "<package name of your app>";
String csl_id = "<Custom store listing id>";
intent.setPackage("com.android.vending");
String deepLinkUrl = "https://play.google.com/d?id=" + id + "&referrer=" + referrer + "&listing=" + csl_id;
intent.setData(Uri.parse(deepLinkUrl));
intent.putExtra("overlay", true);
intent.putExtra("callerId", callerId);
PackageManager packageManager = context.getPackageManager();
if (intent.resolveActivity(packageManager) != null) {
  startActivityForResult(intent, 0);
} else {
  // Fallback to deep linking to full Play Store.
}
```

## Inline install API parameters

| Field | Description | Required |
|---|---|---|
| `referrer` | An optional [referrer](https://developer.android.com/google/play/installreferrer) tracking string | No |
| `id` | The [package name](https://support.google.com/admob/answer/9972781) of the app to be installed | Yes |
| `overlay` | Set to `true` if inline half sheet is requested; if `false`, the intent deep links to Google Play | Yes |
| `callerId` | The [package name](https://support.google.com/admob/answer/9972781) of the caller app | Yes |
| `listing` | An optional parameter to specify the target for a custom store listing | No |

If the app install flow doesn't display the Google Play inline install half
sheet interface, a direct (deep link) to the Google Play listing is shown
instead.