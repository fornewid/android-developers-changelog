---
title: https://developer.android.com/distribute/marketing-tools/inline-installs-3pas
url: https://developer.android.com/distribute/marketing-tools/inline-installs-3pas
source: md.txt
---

This page describes how third-party app stores enrolled in the Catalog Access
program can integrate Google Play **inline installs**, a feature that allows third-party US
Android app stores to direct users to the download of Play's apps through Google
Play on the same terms as any other download that is made directly through the
Google Play Store.

## Prerequisites

Before integrating the inline install API in your third-party app store, you
must complete the following setup in the Google Play Console:

1. **Enroll in the Play Catalog Access Program:** Follow the [enrollment instructions](https://support.google.com/googleplay/android-developer/answer/17117200).
2. **Opt-in to Catalog Access:** Enroll in the Catalog Access program via your Play Console settings.
3. **Retrieve delivery tokens:** Process the Play App Catalog export provided to you. This export contains the necessary `catalog_token` (delivery token) for each app you are eligible to distribute.

## Requirements

For the half-sheet interface to successfully appear to users, the following
requirements must be met:

- The user must be located in the **US**.
- The minimum Google Play version on the device must be **52.3**.
- The Android API level must be **24 or higher**.
- You must provide a valid, unexpired `catalog_token` for access to the Play Store.

## Invoke inline installs from your app store

To invoke the inline install half-sheet, create an instance of the
[`Intent`](https://developer.android.com/reference/android/content/Intent) class that targets the Google Play
deep link URL and includes your unique `catalog_token`.

Use the following sample code (Kotlin or Java) as a guideline:

### Kotlin

```kotlin
val intent = Intent(Intent.ACTION_VIEW)
val referrer = "<Your referrer string>"
val id = "<Package name of the app to be installed>"
val callerId = "<Package name of your third-party app store>"

// Retrieve the app-specific token from your processed catalog export
val catalogToken = getVerificationTokenByDocId(id)

intent.setPackage("com.android.vending")
val deepLinkUrl = "https://play.google.com/d?id=$id&referrer=$referrer"
intent.data = Uri.parse(deepLinkUrl)

// Set the required intent extras
intent.putExtra("overlay", true)
intent.putExtra("callerId", callerId)
intent.putExtra("catalog_token", catalogToken)

val packageManager = context.getPackageManager()
if (intent.resolveActivity(packageManager) != null) {
  startActivityForResult(intent, 0) // Call with a request code to receive ActivityResults
}
```

### Java

```java
Intent intent = new Intent(Intent.ACTION_VIEW);
String referrer = "<Your referrer string>";
String id = "<Package name of the app to be installed>";
String callerId = "<Package name of your third-party app store>";

// Retrieve the app-specific token from your processed catalog export
byte[] catalogToken = getVerificationTokenByDocId(id);

intent.setPackage("com.android.vending");
String deepLinkUrl = "https://play.google.com/d?id=" + id + "&referrer=" + referrer;
intent.setData(Uri.parse(deepLinkUrl));

// Set the required intent extras
intent.putExtra("overlay", true);
intent.putExtra("callerId", callerId);
intent.putExtra("catalog_token", catalogToken);

PackageManager packageManager = context.getPackageManager();
if (intent.resolveActivity(packageManager) != null) {
  startActivityForResult(intent, 0); // Call with a request code to receive ActivityResults
}
```

## Inline install API parameters

The following parameters must be passed in your Intent URL or as Intent Extras
to authorize the inline install:

| Field | Location | Description | Required |
|---|---|---|---|
| `id` | URL Query | The package name of the target app to be installed. | Yes |
| `referrer` | URL Query | An optional referrer tracking string. | No |
| `overlay` | Intent Extra | Set to `true` to request the inline half-sheet interface. | Yes |
| `callerId` | Intent Extra | The package name of your approved third-party app store. | Yes |
| `catalog_token` | Intent Extra | The unique delivery token provided in your Catalog Access export. **Note:** Tokens are validated for freshness, target package match, and caller package match. | Yes |

## (Optional) Google Play Inline Install with installation status overlay

To show an installation status overlay with the inline install flow, you will need to integrate the Google Play Inline Install with the Persistent Affordance feature using the Google Play HSDP SDK.

For the inline install flow with persistent affordance to appear:

- The target device's minimum Google Play Store version must be **52.5** or higher.
- The Android API level must be **24** (Android M) or higher.
- Integrate with [HSDP SDK](https://maven.google.com/web/index.html#com.google.android.play:hsdp) with version **2.0.2 (coming soon)** or higher.

### Integration example

```kotlin
// Step 1: Initialize HSDP Service
// Note: Calling create(activity) automatically configures useServiceBasedHsdp = false
// (Activity Path) under the hood without requiring manual boolean flags.
val hsdpService = HsdpDeepLinkServiceFactory.create(activity)

// Step 2: Construct Extra Query Parameters with Catalog Token
val extraQueryParams = mapOf("catalog_token" to "YOUR_SECURE_CATALOG_TOKEN_VALUE")

// Step 3: Trigger Inline Install Flow
hsdpService.open(
    targetAppPackageName = "com.example.targetapp",
    referrer = "3pas_ad_campaign_123",
    listener = object : HsdpDeepLinkServiceListener {
        override fun onDeepLinkStarted() {
            // Inline details dialog started successfully
        }
        override fun onAffordanceStarted() {
            // HPOA persistent affordance UI attached
        }
        override fun onAffordanceEnded() {
            // Affordance UI detached
        }
        override fun onError(errorMessage: String) {
            // Handle error or fallback
        }
    },
    extraQueryParams = extraQueryParams
)
```

### Stop affordance tracking example

Allows the caller app to manually stop tracking the installation state and dismiss
the HPOA overlay. Note: This will not dismiss the HSDP install sheet itself, only the
affordance.

```kotlin
// Stop tracking the installation state and dismiss the affordance overlay
hsdpService.stopAffordance(
    targetAppPackageName = "com.example.targetapp",
    listener = object : HsdpDeepLinkService.AffordanceListener {
        override fun onAffordanceStopped() {
            // Affordance overlay stopped successfully
        }
    }
)
```

### Affordance States \& UX

The Google Play Inline Install with the Persistent Affordance feature has two visual states:

1. **Installing State**: Displays a thumbnail of the target app and an installation progress spinner. Clicking the thumbnail relaunches the HSDP install sheet.
2. **Post-Install State**: Displays the target app icon with an "Open" action. Clicking the thumbnail opens the newly installed app.

| **Installing** | **Post-install** |
|---|---|
| ![Installing State (Expanded)](https://developer.android.com/static/distribute/images/inline-install-installing-state_with_affordance.png) ![Installing State (Collapsed)](https://developer.android.com/static/distribute/images/inline-install-installing-state-collapsed_with_affordance.png) | ![Post-install State](https://developer.android.com/static/distribute/images/inline-install-post-install-state_with_affordance.png) |