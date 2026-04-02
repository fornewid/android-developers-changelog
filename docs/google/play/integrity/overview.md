---
title: https://developer.android.com/google/play/integrity/overview
url: https://developer.android.com/google/play/integrity/overview
source: md.txt
---

# Overview of the Play Integrity API

The Play Integrity API helps you check that user actions and server requests are coming from your genuine app, installed by Google Play, running on a genuine and certified Android device. By detecting risky interactions --- like those from tampered app versions, untrustworthy devices, or emulated environments --- your backend server can respond with appropriate actions to prevent abuse and unauthorized access, fight fraud, combat cheating, and protect users from attacks.

![Play Integrity API Overview flow](https://developer.android.com/static/images/google/play/integrity/play-integrity-api-overview.png)

The API returns verdicts that help you detect potential threats, including:

- **Unauthorized access** : The`accountDetails`verdict helps you determine whether the user installed or paid for your app or game on Google Play.
- **Code tampering** : The`appIntegrity`verdict helps you determine whether you're interacting with your unmodified binary that Google Play recognizes.
- **Risky devices and emulated environments** : The`deviceIntegrity`verdict helps you determine whether your app is running on a genuine certified Android device or a genuine instance of Google Play Games for PC.

| **Key Point:** When the Play Integrity API assesses an environment, it uses[hardware-backed security signals](https://developer.android.com/privacy-and-security/security-key-attestation)that are highly resilient to attacks and circumvention. Play Integrity API simplifies developer integration work and ongoing management by abstracting away signal complexity and issue mitigation across Android SDK versions, device manufacturer provisioned keys, and device models.

Google Play developers can also opt-in to receive additional verdicts to detect a broader range of potential threats, including:

- **Unpatched devices** : The`MEETS_STRONG_INTEGRITY`response in the`deviceIntegrity`verdict helps you determine if a device has applied recent security updates (for devices running Android 13 and higher).
- **Risky access by other apps:** The`appAccessRiskVerdict`helps you determine whether apps are running that could be used to capture the screen, display overlays, or control the device (for example, by misusing the accessibility permission).
- **Known malware:** The`playProtectVerdict`helps you determine whether Google Play Protect is turned on and whether it has found risky or dangerous apps installed on the device.
- **Hyperactivity:** The`recentDeviceActivity`level helps you determine whether a device has made an anomalously high volume of requests recently, which could indicate automated traffic and could be a sign of attack.
- **Repeat abuse and reused devices:** `deviceRecall`(beta) helps you determine whether you're interacting with a device that you've previously flagged, even if your app was reinstalled or the device was reset.

The API can be used across Android form factors including phones, tablets, foldables, Android Auto, Android TV, Android XR, ChromeOS, Wear OS, and on Google Play Games for PC.

## Security considerations

Play Integrity API provides the most value for your app when you follow these recommended practices:

### Have an anti-abuse strategy

The Play Integrity API works best when used alongside other signals as part of your overall anti-abuse strategy and not as your sole anti-abuse mechanism. Use this API in conjunction with other appropriate[security best practices](https://developer.android.com/topic/security/best-practices)for your app. By default, your app can make up to 10,000 total requests per day across all installs. You can request to[increase your daily maximum](https://developer.android.com/google/play/integrity/setup#increase-daily).

### Gather telemetry and understand your audience before taking action

Before you change how your app behaves based on Play Integrity API verdicts, you can understand the current situation with your existing audience by implementing the API without enforcement. Once you know what verdicts your current install base is returning, you can estimate the impact of any enforcement you're planning and adjust your anti-abuse strategy accordingly.

### Decide how you'll request integrity verdicts

Play Integrity API offers two options for requesting and receiving integrity verdicts. Whether you make standard requests, classic requests, or a combination of both types of request, the integrity verdict response will be returned in the same format.

**Standard API requests**are suitable for any app or game and can be made on demand to check that any user action or server request is genuine. Standard requests have the lowest latency (a few hundred milliseconds on average) and a high reliability of obtaining a usable verdict. Standard requests make use of smart on-device caching while delegating protection against certain types of attack to Google Play.

**Classic API requests**, the original way to request integrity verdicts, also continue to be available. Classic requests have higher latency (a few seconds on average) and you are responsible for mitigating the risk of certain types of attacks. Classic requests use more of the user's data and battery than standard requests because they initiate a fresh assessment and so they should be made infrequently as a one-off to check whether a highly sensitive or valuable action is genuine. If you are considering making a classic request and caching it to use later, then you should make a standard request instead to reduce the risk of attacks.

The following table highlights some key differences between the two types of requests:

|                                             |               **Standard API request**               |                             **Classic API request**                             |
|---------------------------------------------|------------------------------------------------------|---------------------------------------------------------------------------------|
| Minimum Android SDK required**\***          | Android 6.0 (API level 23) or higher                 | Android 6.0 (API level 23) or higher                                            |
| API warm up required                        | ✔️ (a few seconds)                                   | ❌                                                                               |
| Typical request latency                     | A few hundred milliseconds                           | A few seconds                                                                   |
| Potential request frequency                 | Frequent (on-demand check for any action or request) | Infrequent (one-off check for highest value actions or most sensitive requests) |
| Mitigate against replay and similar attacks | Automatic mitigation by Google Play                  | Use`nonce`field with server side logic                                          |

***\*** For the Play Integrity API library[v1.4.0](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/release-notes#1-4-0)and later, the minimum supported Android SDK is the same for both request types and is determined by the library's`minSdkVersion`. For[v1.3.0](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/release-notes#1-3-0)and earlier releases, the minimum Android SDK required is Android 5.0 (API level 21) for Standard API requests and Android 4.4 (API level 19) for Classic API requests.*

You can see a table with more differences in the[classic request considerations](https://developer.android.com/google/play/integrity/classic#compare-standard).

### Request an integrity verdict at an appropriate moment

You should request an app access risk verdict as close as possible to the time of the action or server request that you want to defend against being accessed, to prevent scammers from working around the integrity check performed by your app.

### Make your API requests hard to replicate

Standard API requests have a field called`requestHash`that is used to protect against tampering and similar attacks. In this field, you should include a digest of all relevant values from your app's request. Follow the guidance on[how to use content binding](https://developer.android.com/google/play/integrity/standard#protect-requests)to protect your app's standard requests.

Classic API requests have a field called`nonce`(short for number once), that is used to protect against certain types of attacks, such as replay and tampering attacks. Follow the guidance on[how to generate nonces](https://developer.android.com/google/play/integrity/classic#nonce)to protect your app's classic requests.
| **Caution:** Data that you use for the`requestHash`and`nonce`fields is visible in cleartext to your app, and to Google. You should encrypt or hash the data before passing it to the Play Integrity API.

### Avoid caching integrity verdicts

Caching integrity verdicts increases the risk of proxying, which is an attack where a bad actor reuses a verdict from a good device for abusive purposes in another environment. Instead of caching responses, you can[make a standard API request](https://developer.android.com/google/play/integrity/standard)to get a verdict on demand.

### Have a tiered enforcement strategy

The Play Integrity API's integrity verdict has a range of possible responses making it possible to build an anti-abuse strategy with multiple tiers of enforcement. You can do this by configuring your app's backend server to behave differently depending on each possible response or group of responses.

It's also possible to tier your enforcement strategy based on device trustworthiness by opting in to receive[additional device labels](https://developer.android.com/google/play/integrity/verdict#device-integrity-field)in your API response from the Play Console. Each device will return all the labels whose criteria it satisfies. For example, after opting in to receive all the device labels, you could choose to trust a device that returns`MEETS_STRONG_INTEGRITY`,`MEETS_DEVICE_INTEGRITY`, and`MEETS_BASIC_INTEGRITY`more than a device that only returns`MEETS_BASIC_INTEGRITY`. You can respond differently from the server in each scenario.
| **Tip:** The`MEETS_STRONG_INTEGRITY`label offers the highest resilience by requiring the device to have[hardware-backed security signals](https://developer.android.com/privacy-and-security/security-key-attestation)in addition to, on Android 13 and higher, a recent security update. Fewer devices return this label compared to the`MEETS_DEVICE_INTEGRITY`label so it is recommended to use it as part of a tiered enforcement strategy in order to reach more users.

### Send a range of responses from your server to your app

Having a range of decision outcomes is harder to replicate than sending a binary Allow/Deny response from the server back to the app for each response. For example, you could use a series of related responses such as Allow, Allow with limits, Allow with limits after CAPTCHA completion, and Deny.

### Detect repeat abuse using device recall, while preserving user privacy

[Device recall](https://developer.android.com/google/play/integrity/device-recall)gives apps the ability to store and recall some custom data associated with a specific device in a way that preserves user privacy. The data is stored on Google's servers, allowing your app to reliably recall per-device data even after your app is reinstalled or the device is reset. This gives you a reliable way to re-identify a device that you found abusive in the past so that you can take action and stop it from being used for abuse again. You can define your own meaning to the three values that make up device recall data:

- You could use them as up to three separate flags or booleans. For example, values could represent that a device has or hasn't created an account, has or hasn't redeemed a free trial, or has or hasn't been known for high severity abuse.
- Alternatively, you could combine all of the states of the values into up to eight custom labels, for example one label for the default state when all three values are unmodified and seven labels with custom meanings. This lets you segment all devices into up to eight groups based on behaviors or actions that you define. In this scenario, the most recently updated of the three`writeDates`indicates when you last updated the label.

Also keep in mind the[prerequisites and other considerations](https://developer.android.com/google/play/integrity/device-recall#device-recall-prerequisites)when working with device recall data.

### Detect large-scale abuse using recent device activity

Use the[recent device activity](https://developer.android.com/google/play/integrity/setup#optional_device_information)feature in the Play Integrity API to find devices requesting large numbers of integrity tokens. High-volume-activity abusers commonly generate valid attestation results from real devices and provide them to bots to automate attacks on rooted devices and emulators. You can use the recent device activity level to check how many attestations were generated by your app on that device in the last hour.

### Show actionable error messages

When possible, provide useful error messages to the user and let them know what they can do to fix it; such as retrying, enabling their Internet connection, or checking that the Play Store app is up-to-date.

### Have a plan for unexpected issues or outages

The[Play status dashboard](https://status.play.google.com)shows information about the service status of Play Integrity API along with information about any disruptions and outages. You should plan in advance how you want your backend server to function in the unlikely event of a large-scale Play Integrity API outage. Note that your backend server should also be ready to function in the case when Android Platform Key Attestation keys specific for devices are[revoked](https://developer.android.com/privacy-and-security/security-key-attestation#certificate_status).

### Consider end to end enterprise fraud solutions

Enterprise customers looking for a complete fraud and bot management solution can purchase[reCAPTCHA Enterprise](https://cloud.google.com/recaptcha-enterprise)for mobile, which includes[SDKs for Android](https://cloud.google.com/recaptcha-enterprise/docs/instrument-android-apps)that provide fraud risk scores to developers. reCAPTCHA Enterprise automatically includes Play Integrity API signals, and combines them with reCAPTCHA network and application signals for customers, providing a frictionless, invisible fraud management solution out of the box. It can also provide protection for Android apps where Play Integrity API is not available.

### Challenge risky traffic when accessing high value or sensitive features

Identify high value or sensitive actions in your app or game to protect with the Play Integrity API instead of denying access outright. When possible, challenge risky traffic before allowing high-value actions to proceed. For example, when the app access risk indicates that an app is running that could capture the screen, ask the user to disable or uninstall apps that can capture the screen before allowing them to proceed to functionality that you want to protect.

## Terms of service and data safety

By accessing or using the Play Integrity API, you agree to the[Play Integrity API Terms of Service](https://developer.android.com/google/play/integrity/terms). Please read and understand all applicable terms and policies before accessing the API.

Google Play has a data safety section for developers to disclose their apps' data collection, sharing, and security practices to keep your users informed. To help you complete your data form, see this information on[how the Play Integrity API handles data](https://developer.android.com/google/play/integrity/terms#data-safety).