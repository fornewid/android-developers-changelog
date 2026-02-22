---
title: https://developer.android.com/google/play/integrity/setup
url: https://developer.android.com/google/play/integrity/setup
source: md.txt
---

This page explains how to set up your app, game or SDK to use the Play
Integrity API. To integrate the API, you must have a Google Cloud
project, which is necessary to begin making requests. You
can then link your Google Cloud project in the Google Play Console (for apps)
or the Google Play SDK Console (for SDKs). **Linking your project is required
to access additional configuration options, testing features, API reporting,
and to request an increase to your daily request quota.**

## Enable Play Integrity API

Every app or SDK calling the Play Integrity API must have a Google Cloud project
to use the API and monitor usage. This is the mandatory first step for all
integrations. You can enable the Play Integrity API in the Google Cloud Console
or you can skip directly to linking your Cloud project to Google Play
and Play Integrity API will be enabled for you.

In your [Google Cloud Console](https://console.cloud.google.com/), create a new Cloud project or choose an
existing Cloud project that you want to use with the Play Integrity API.

1. Navigate to **APIs and services**.
2. Select **Enable APIs and services**.
3. Search for **[Play Integrity API](https://console.cloud.google.com/marketplace/product/google/playintegrity.googleapis.com)**.
4. Click **Enable**.

You can now integrate the Play Integrity API into your app. To access
advanced features and quota increases, you must proceed to the linking step.
| **Note:** Projects that are enabled in the Google Cloud Console but not linked in the Play Console or Play SDK Console are not eligible for additional configuration options or quota increases.

## Link to Google Play (recommended)

Link your app or SDK to Google Play using these instructions.

### For apps and games on Google Play

Apps distributed on Google Play should link their Google Cloud project in the
Google Play Console to enable additional features and request increased
daily API quota.

1. Open the [Google Play Console](https://play.google.com/console/developers) and select your app.
2. Navigate to **Test and release** \> **[App integrity](https://play.google.com/console/developers/app/app-integrity/overview)**.
3. Under **Play Integrity API** click **Link a Cloud project**.
4. Choose the Google Cloud project you plan to use with the Play Integrity API; if the Play Integrity API is not already enabled for the project, it will be enabled automatically upon linking.

### For SDK providers on Play SDK Console

SDK providers using the [Google Play SDK Console](https://play.google.com/sdk-console/) can link their
Google Cloud project to attribute API usage to the SDK rather than the
individual apps using it, enable additional features, and request
increased daily API quota. Note that access to the Google Play SDK Console
is subject to [eligibility criteria](https://support.google.com/googleplay/android-developer/answer/12244916#SDK_eligibility).

1. Open the [Google Play SDK Console](https://play.google.com/sdk-console/) and select your SDK.
2. Navigate to **SDK integrity**
3. Under **Play Integrity API** click **Link a Cloud project**.
4. Choose the Google Cloud project you plan to use with the Play Integrity API; if the Play Integrity API is not already enabled for the project, it will be enabled automatically upon linking.

## Understand Play Integrity API usage limits

Your app or SDK has a default daily limit of 10,000 total requests, tied
to the associated Cloud Project Number. If you anticipate a higher volume,
you can request a quota increase.

| Action | Daily quota | Notes |
|---|---|---|
| Token requests | 10,000 | Shared between classic requests and standard token preparations |
| Token decryptions on Google's servers | 10,000 | Shared between classic and standard requests |

### Increase your daily maximum number of requests

Quota increase is subject to eligibility criteria. Quota increases apply to
both client-side token generation and server-side decryption calls. Processing
requests can take up to a week. We recommend monitoring your Play Integrity
API usage in your Google Cloud Console and setting [quota alerts](https://cloud.google.com/docs/quota?&_ga=2.68760982.-685660492.1676978684#monitoring_quota_metrics) to
avoid interruptions to your service.

Even with higher quota, continue to limit
[classic requests](https://developer.android.com/google/play/integrity/classic) to infrequent, high-value actions to preserve
user battery and data usage.
| **Caution:** Very high volume changes should be rolled out gradually. Sudden traffic spikes may cause throttling.

#### For apps and games on Google Play

To be eligible for a quota increase, your app must be available on Google Play
in addition to any other distribution channels. You must link your Google
Cloud project to your app in the [Play Console](https://play.google.com/console/developers/app/app-integrity/integrity-api-settings). Quota requests
from unlinked projects will be rejected.

To request an increase:

1. Link the relevant Google Cloud project in the **[Play Console](https://play.google.com/console/developers/app/app-integrity/integrity-api-settings)**.
2. Verify you have correctly implemented API logic including proper retry strategies.
3. Submit the [quota request form](https://support.google.com/googleplay/android-developer/contact/piaqr).

#### For SDK providers on Play SDK Console

To be eligible for a quota increase, your SDK must be claimed on the Google
Play SDK Console and your Cloud project must be linked to your SDK there.
Access to the Google Play SDK Console is subject to [eligibility criteria](https://support.google.com/googleplay/android-developer/answer/12244916#SDK_eligibility).

To request an increase:

1. Link your Google Cloud project in the **[Google Play SDK Console](https://play.google.com/sdk-console/)**.
2. Complete the [developer support form](https://support.google.com/googleplay/android-developer/answer/10357403).

In the open comments, provide your SDK details, describe your use case,
the type of API requests that you're making (standard, classic, or both),
how often you're making requests, and the daily maximum requests that you want.

## Integrate Play Integrity API into your app

To integrate the Play Integrity API into your app or SDK, do one of the
following depending on your development environment:

### Kotlin or Java

The latest Android library for the Play Integrity API is available from
[Google's Maven Repository](https://maven.google.com/web/index.html#com.google.android.play:integrity). Add the following dependency to your app's
`build.gradle` file:  

```groovy
implementation 'com.google.android.play:integrity:1.6.0'
```

### Unity

The following sections describe how to integrate and set up the Google Play
Integrity API for Unity projects, covering supported Unity versions,
installation methods, and environment setup.

#### Supported Unity versions

- All versions of 2019.x, 2020.x, and newer are supported.
- If you use Unity 2018.x, version 2018.4 or newer are supported.
- Unity 2017.x and older aren't supported.

#### Set up your development environment

### OpenUPM-CLI

If you have the [OpenUPM CLI](https://github.com/openupm/openupm-cli#installation)
installed you can install the OpenUPM registry with the following command:  

    openupm add com.google.play.integrity

### OpenUPM

1. Open the [package manager settings](https://docs.unity3d.com/Manual/class-PackageManager.html)
   by selecting the Unity menu option
   **Edit \> Project Settings \> Package Manager**.

2. Add OpenUPM as a scoped registry to the Package Manager window:

       Name: package.openupm.com
       URL: https://package.openupm.com
       Scopes: com.google.external-dependency-manager
         com.google.play.common
         com.google.play.core
         com.google.play.integrity

3. Open the [package manager menu](https://docs.unity3d.com/Manual/upm-ui-install.html) by selecting the Unity
   menu option **Window \> Package Manager**.

4. Set the manager scope drop-down to select **My Registries**.

5. Select the **Google Play Integrity plugin for Unity** package from the
   package list and press **Install**.

### Import from GitHub

1. Download the latest [`.unitypackage`](https://github.com/google/play-integrity-unity/releases/latest)
   release from GitHub.

2. Import the `.unitypackage` file by selecting the Unity menu option
   **Assets \> Import package \> Custom Package** and importing all items.

| **Note:** By downloading and using Google Play Unity Plugins, you agree to the [Play Core Software Development Kit Terms of Service](https://developer.android.com/guide/playcore#license).

### Unreal Engine

The following sections describe how to integrate and set up the Google Play
Integrity API for Unreal Engine projects.

#### Supported Unreal Engine versions

The plugin supports **Unreal Engine 5.0** and all subsequent versions.

#### Set up your development environment

| **Note:** If you have already used the In-app Reviews or In-app Updates plugins in Unreal Engine, you can skip to the final step.

1. Download the [Play Unreal Engine Plugin](https://github.com/google/play-unreal-engine-plugin) from the GitHub
   repository.

2. Copy the `GooglePlay` folder inside your `Plugins` folder in your Unreal
   Engine project.

3. Open your Unreal Engine project and click **Edit → Plugins**.

4. Search for **Google Play** and check the **Enabled** checkbox.

5. Restart the game project and trigger a build.

6. Open your project's `Build.cs` file and add the `PlayIntegrity` module
   to `PublicDependencyModuleNames`:

       using UnrealBuildTool;

       public class MyGame : ModuleRules
       {
         public MyGame(ReadOnlyTargetRules Target) : base(Target)
         {
           // ...

           PublicDependencyModuleNames.Add("PlayIntegrity");

           // ...
         }
       }

### Native

Follow the [native setup guide](https://developer.android.com/google/play/integrity/native-setup). For more details, see Play Integrity's
[native API reference documentation](https://developer.android.com/reference/native/play/core/group/integrity).

## Configure API responses (optional)

The API response includes default verdicts returned in every request. If you
have linked your Cloud project in the Play Console or Play SDK Console, you can
customize your API response to include additional information.

### Default integrity verdicts

The following integrity verdicts are returned in the Play Integrity API response
by default:

| Response field | Value | Description |
|---|---|---|
| Device integrity | `MEETS_DEVICE_INTEGRITY` | The app is running on a genuine and certified Android device. On Android 13 and higher, there is hardware-backed proof that the device bootloader is locked and the loaded Android OS is a certified device manufacturer image. |
|   | Empty (a blank value) | The app is running on a device that has signs of attack (such as API hooking) or system compromise (such as being rooted), or the app is not running on a physical device (such as an emulator that does not pass Google Play integrity checks). |
| Play account details | `LICENSED` | The user has an app entitlement. In other words, the user installed or updated your app from Google Play on their device. |
|   | `UNLICENSED` | The user doesn't have an app entitlement. This happens when, for example, the user sideloads your app or doesn't acquire it from Google Play. |
|   | `UNEVALUATED` | Licensing details were not evaluated because a requirement was missed. This could happen for several reasons, including the following: - The device is not trustworthy enough. - The user is not signed in to Google Play. - The version of your app installed on the device is unknown to Google Play. |
| Application integrity | `PLAY_RECOGNIZED` | The app and certificate match the versions distributed by Google Play. |
|   | `UNRECOGNIZED_VERSION` | The certificate or package name does not match Google Play records. |
|   | `UNEVALUATED` | Application integrity was not evaluated. A necessary requirement was missed, such as the device not being trustworthy enough. |

### Google Play Games for PC

If you distribute to [Google Play Games for PC](https://developer.android.com/games/playgames/overview), you will automatically be
opted in to receive an additional label in the device integrity verdict:

| Response field | Label | Description |
|---|---|---|
| Device integrity | `MEETS_VIRTUAL_INTEGRITY` | The app is running on an Android emulator powered by Google Play services. The emulator passes system integrity checks and meets core Android compatibility requirements. |

### Optional integrity verdicts

If you have linked your Cloud project in the Play Console or
Play SDK Console, you can opt in to receive additional information.

To make changes, visit the Play Console and navigate to
**Test and release** \> **App integrity** . Next to **Play Integrity API** click
**[Settings](https://play.google.com/console/developers/app/app-integrity/integrity-api-settings)** . Click **Change responses**, edit and save your
changes.
| **Caution:** Changes to integrity responses take effect immediately, including for apps and SDKs in production. Make sure your server is prepared to accept new responses before saving changes.

#### Device information

**Additional device labels** in the `deviceIntegrity`
verdict tell you more about the device environment the app is running on.
A single device returns multiple labels if it meets the criteria for each.
You can use these labels to create a tiered enforcement strategy. For example,
you might choose to trust a device that returns three labels
(`MEETS_STRONG_INTEGRITY`, `MEETS_DEVICE_INTEGRITY`, and
`MEETS_BASIC_INTEGRITY`) more than a device that returns only one label
(`MEETS_BASIC_INTEGRITY`).

**Device attributes** tells you the Android SDK version of the Android OS on
the device. In the future, it may be extended with other device
attributes.

**Recent device activity** returns a level ranging from `LEVEL_1` (low number
of requests) to `LEVEL_4` (high number of requests). High activity levels may
indicate a device being used to generate excessive tokens for abusive
distribution to untrusted devices.

**Device recall** lets you store some custom, per-device data with specific
devices that you can reliably retrieve when your app is installed again later
on the same device.
| **Note:** [Device recall](https://developer.android.com/google/play/integrity/device-recall) is available in beta to apps and subject to change. Pricing for high-scale usage may apply after general release. SDKs cannot use device recall.

After you opt in to optional information, your API response will include new
fields and responses in the verdict:

| Response field | Label | Description |   |
|---|---|---|---|
| Device integrity | `MEETS_BASIC_INTEGRITY` | The app is running on a device that passes basic system integrity checks. The device bootloader can be locked or unlocked, and the boot state can be verified or unverified. The device may not be certified, in which case Google cannot provide any security, privacy, or app compatibility assurances. On Android 13 and higher, the `MEETS_BASIC_INTEGRITY` verdict requires that the attestation [root of trust](https://developer.android.com/privacy-and-security/security-key-attestation#root_certificate) is provided by Google. ||
|   | `MEETS_STRONG_INTEGRITY` | The app is running on a genuine and certified Android device with a recent security update. - On Android 13 and higher, the `MEETS_STRONG_INTEGRITY` verdict requires `MEETS_DEVICE_INTEGRITY` and security updates in the last year for all partitions of the device, including an Android OS partition patch and a vendor partition patch. - On Android 12 and lower, the `MEETS_STRONG_INTEGRITY` verdict only requires hardware-backed proof of boot integrity and **does not** require the device to have a recent security update. Therefore, when using the `MEETS_STRONG_INTEGRITY`, it is recommended to also take into account the Android SDK version in the `deviceAttributes` field. ||
| Device attributes | `sdkVersion: 19, 20, ..., 36` | The SDK version of the Android OS running on the device. The number returned maps to [`Build.VERSION_CODES`](https://developer.android.com/reference/android/os/Build.VERSION_CODES). ||
|   | Empty (a blank value) | The SDK version is not evaluated because a necessary requirement was missed. In this case, the `sdkVersion` field is unset; thus, the `deviceAttributes` field is empty. This could happen because: - The device is not trustworthy enough. - There were technical issues on the device. ||
|   |   | **Standard API integrity token requests on this device in the last hour per app** | **Classic API integrity token requests on this device in the last hour per app** |
| Recent device activity | `LEVEL_1` (lowest) | 10 or fewer | 5 or fewer |
|   | `LEVEL_2` | Between 11 and 25 | Between 6 and 10 |
|   | `LEVEL_3` | Between 26 and 50 | Between 11 and 15 |
|   | `LEVEL_4 ` (highest) | More than 50 | More than 15 |
|   | `UNEVALUATED` | Recent device activity was not evaluated. This could happen because: - The device is not trustworthy enough. - The version of your app installed on the device is unknown to Google Play. - There were technical issues on the device. ||
| Device recall | `values: bitFirst, bitSecond, bitThird` | These are the bit values that you set in the past for the specific device. You decide the meaning of each bit. The three bit values are false by default. ||
|   | `writeDates: yyyymmFirst, yyyymmSecond, yyyymmThird` | These are the bit value write dates in UTC accurate to the year and month. The write date of a recall bit is updated every time the bit is set to true and is removed when the bit is set to false. ||

#### Environment details

**App access risk** tells you whether other apps are running that could be used
to capture the screen, display overlays, or control the device. Verified
accessibility services that are known to Google Play are automatically excluded
from this verdict.

**Play Protect verdict** tells you whether Google Play Protect is enabled on the
device and whether it has found known malware.

After you opt in to optional information, your API response will include new
fields and responses in the verdict:

| Response field | Value | Description |
|---|---|---|
| App access risk verdict | `KNOWN_INSTALLED` | Apps are installed by Google Play or preloaded on the system partition by the device manufacturer. |
|   | `KNOWN_CAPTURING` | Apps installed by Google Play or preloaded on the device are running that could be used to read or capture inputs and outputs of the requesting app, such as screen recording apps. |
|   | `KNOWN_CONTROLLING` | Apps installed by Google Play or preloaded on the device are running that could be used to control the device and inputs and outputs of the requesting app, such as remote controlling apps. |
|   | `KNOWN_OVERLAYS` | Apps installed by Google Play or preloaded on the device are running that might be displaying overlays on the requesting app. |
|   | `UNKNOWN_INSTALLED` | Other apps are installed, which were not installed by Google Play or preloaded on the system partition by the device manufacturer. |
|   | `UNKNOWN_CAPTURING` | Other apps are running (not installed by Play or preloaded on the device) that could be used to read or capture inputs and outputs of the requesting app, such as screen recording apps. |
|   | `UNKNOWN_CONTROLLING` | Other apps are running (not installed by Play or preloaded on the device) that could be used to control the device and inputs and outputs of the requesting app, such as remote controlling apps. |
|   | `UNKNOWN_OVERLAYS` | Other apps are running (not installed by Play or preloaded on the device) that might be displaying overlays on the requesting app. |
|   | Empty (a blank value) | App access risk is not evaluated if a necessary requirement was missed. In this case the `appAccessRiskVerdict` field is empty. This could happen for several reasons, including the following: - The device is not trustworthy enough. - The device form factor is not a phone, tablet, or foldable. - The device is not running Android 6 (API level 23) or higher. - The version of your app installed on the device is unknown to Google Play. - The version of the Google Play Store on the device is outdated. - **Games only**: The user account does not have a Play license for the game. - A standard request was used with the `verdictOptOut` parameter. - A standard request was used with a Play Integrity API library version that doesn't yet support app access risk for standard requests. |
| Play Protect verdict | `NO_ISSUES` | Play Protect is turned on and did not find any app issues on the device. |
|   | `NO_DATA` | Play Protect is turned on but no scan has been performed yet. The device or the Play Store app may have been recently reset. |
|   | `POSSIBLE_RISK` | Play Protect is turned off. |
|   | `MEDIUM_RISK` | Play Protect is turned on and has found potentially harmful apps installed on the device. |
|   | `HIGH_RISK` | Play Protect is turned on and has found dangerous apps installed on the device. |
|   | `UNEVALUATED` | The Play Protect verdict was not evaluated. A necessary requirement was missed, such as the device not being trustworthy enough. |

| **Note:** The app access risk verdict automatically exempts verified accessibility services known to Google Play. These services will not trigger a capturing, controlling, or overlay response, meaning legitimate accessibility tools are not flagged as risks.

## Configure classic request settings (optional)

Skip this section if you only plan to make [standard API requests](https://developer.android.com/google/play/integrity/standard).

By default, Google Play manages response encryption, meaning your backend calls
Google's server to decrypt verdicts. Alternatively, you can manage keys yourself
to decrypt locally within your secure server environment.

### Let Google manage your response encryption (recommended)

We recommend allowing Google to generate and manage keys to protect your app's
security. Your backend will call Google Play's server to decrypt and verify
responses.

### Manage your own encryption keys

To decrypt locally within your own secure server environment, you can download
encryption keys from the Play Console or the Play SDK Console. Your app must be
available on Google Play to use this feature.

Before you change your response encryption management strategy in the Play
Console, make sure your server is correctly configured to decrypt and verify
integrity tokens on Google Play's servers to avoid disruption.
| **Caution:** Never decrypt tokens or expose keys within your client app.
| **Tip:** Even when self-managing keys, your app can still fall back to Google Play's server for decryption.

### Switch between Google-managed and self-managed encryption keys

1. Open the **Play Console** and select your app .
2. Go to **Test and release** \> **App integrity**.
3. Next to **Play Integrity API** , click **[Settings](https://play.google.com/console/developers/app/app-integrity/integrity-api-settings)**.
4. Under **Classic requests** , next to **Response encryption** , click **Edit**.

To switch to self-managed keys:

1. Select **Manage and download my response encryption keys** and upload your public key.
2. Click **Save** to automatically download your encrypted keys.
3. Update your secure backend server to decrypt locally using these keys.

To switch to Google-managed keys:

1. Select **Let Google manage my response encryption (recommended)**.
2. Click **Save changes**.

| **Caution:** Switching to Google-managed encryption immediately invalidates previously downloaded keys, even in production. Before switching, make sure your server is configured to handle the change to avoid disruption.