---
title: https://developer.android.com/blog/posts/stronger-threat-detection-simpler-integration-protect-your-growth-with-the-play-integrity-api
url: https://developer.android.com/blog/posts/stronger-threat-detection-simpler-integration-protect-your-growth-with-the-play-integrity-api
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# Stronger threat detection, simpler integration: Protect your growth with the Play Integrity API

###### 5-min read

![](https://developer.android.com/static/blog/assets/SS_Alt_Playbrand_Integrity_API_21cd2391d2_Z1L3CHW.webp) 19 Nov 2025 [![](https://developer.android.com/static/blog/assets/dom_elliot_d78b0628db_flDQk.webp)](https://developer.android.com/blog/authors/dom-elliott)[![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](https://developer.android.com/blog/authors/eric-lynch)

##### [Dom Elliott](https://developer.android.com/blog/authors/dom-elliott)
\&
[Eric Lynch](https://developer.android.com/blog/authors/eric-lynch)

In the mobile ecosystem, abuse can threaten your revenue, growth, and user trust. To help developers thrive, Google Play offers a resilient threat detection service, [**Play Integrity API**](https://developer.android.com/google/play/integrity/overview). Play Integrity API helps you verify that interactions and server requests are genuine---coming from your unmodified app on a certified Android device, installed by Google Play.

The impact is significant: apps using Play integrity features see **80% lower unauthorized usage** on average compared to other apps. Today, leaders across diverse categories---including Uber, TikTok, Stripe, Kabam, Wooga, Radar.com, Zimperium, Paytm, and Remini---use it to help safeguard their businesses.

We're continuing to improve the Play Integrity API, making it easier to integrate, more resilient against sophisticated attacks, and better at recovering users who don't meet integrity standards or encounter errors with new Play in-app remediation prompts.

### Detect threats to your business

The Play Integrity API offers verdicts designed to detect specific threats that impact your bottom line during critical interactions.

- **Unauthorized access** : The `accountDetails` verdict helps you determine whether the user installed or paid for your app or game on Google Play.
- **Code tampering** : The `appIntegrity` verdict helps you determine whether you're interacting with your unmodified binary that Google Play recognizes.
- **Risky devices and emulated environments** : The `deviceIntegrity` verdict helps you determine whether your app is running on a genuine Play Protect certified Android device or a genuine instance of Google Play Games for PC.
- **Unpatched devices** : For devices running Android 13 and higher, `MEETS_STRONG_INTEGRITY` response in the `deviceIntegrity` verdict helps you determine if a device has applied recent security updates. You can also opt in to `deviceAttributes` to include the attested Android SDK version in the response.
- **Risky access by other apps:** The `appAccessRiskVerdict` helps you determine whether apps are running that could be used to capture the screen, display overlays, or control the device (for example, by misusing the accessibility permission). This verdict automatically excludes apps that serve genuine accessibility purposes.
- **Known malware:** The `playProtectVerdict` helps you determine whether Google Play Protect is turned on and whether it has found risky or dangerous apps installed on the device.
- **Hyperactivity:** The recentDeviceActivity level helps you determine whether a device has made an anomalously high volume of integrity token requests recently, which could indicate automated traffic and could be a sign of attack.
- **Repeat abuse and reused devices:** `deviceRecall` (beta) helps you determine whether you're interacting with a device that you've previously flagged, even if your app was reinstalled or the device was reset. With device recall, you can customize the repeat actions you want to track.

The API can be used across Android form factors including phones, tablets, foldables, Android Auto, Android TV, Android XR, ChromeOS, Wear OS, and on Google Play Games for PC.

### Make the most of Play Integrity API

Apps and games have found success with the Play Integrity API by following the [security considerations](https://developer.android.com/google/play/integrity/overview#security-considerations) and taking a phased approach to their anti-abuse strategy.

**Step 1: Decide what you want to protect**: Decide what actions and server requests in your apps and games are important to verify and protect. For example, you could perform integrity checks when a user is launching the app, signing in, joining a multiplayer game, generating AI content, or transferring money.

**Step 2: Collect integrity verdict responses**: Perform integrity checks at important moments to start collecting verdict data, without enforcement initially. That way you can analyze the responses for your install base and see how they correlate with your existing abuse signals and historical abuse data.

**Step 3: Decide on your enforcement strategy**: Decide on your enforcement strategy based on your analysis of the responses and what you are trying to protect. For example, you could change risky traffic at important moments to protect sensitive functionality. The API offers a range of responses so you can implement a tiered enforcement strategy based on the trust level you give to each combination of responses.

**Step 4: Gradually rollout enforcement and support your users:** Gradually roll out enforcement. Have a retry strategy when verdicts have issues or are unavailable and be prepared to support good users who have issues. The new Play in-app remediation prompts, described below, make it easier than ever to get users with issues back to a good state.

### NEW: Let Play recover users with issues automatically

Deciding how to respond to different integrity signals can be complex, you need to handle various integrity responses and API error codes (like network issues or outdated Play services). We're simplifying this with new [**Play in-app remediation prompts**](https://developer.android.com/google/play/integrity/remediation). You can show a Google Play prompt to your users to automatically fix a wide range of issues directly within your app. This reduces integration complexity, ensures a consistent user interface, and helps get more users back to a good state.
![get_integrity.gif](https://developer.android.com/static/blog/assets/get_integrity_7d2e165184_1gShAt.webp)

*GET_INTEGRITY automatically detects the issue (in this example, a network error) and resolves it.*

You can trigger the[GET_INTEGRITY](https://developer.android.com/google/play/integrity/remediation#get-integrity-dialog) dialog, available in Play Integrity API library version 1.5.0+, after a range of issues to automatically guide the user through the necessary fixes including:

- **Unauthorized access:**GET_INTEGRITY guides the user back to a Play licensed response in accountDetails.
- **Code tampering:** GET_INTEGRITY guides the user back to a Play recognized response in appIntegrity.
- **Device integrity issues:** GET_INTEGRITY guides the user on how to get back to the MEETS_DEVICE_INTEGRITY state in `deviceIntegrity`.
- **Remediable error codes:** GET_INTEGRITY resolves remediable API errors, such as prompting the user to fix network connectivity or update Google Play Services.

We also offer specialized dialogs including[GET_STRONG_INTEGRITY](https://developer.android.com/google/play/integrity/remediation#get-strong-integrity-dialog) (which works like GET_INTEGRITY while also getting the user back to the MEETS_STRONG_INTEGRITY state with no known malware issues in the `playProtectVerdict`), [GET_LICENSED](https://developer.android.com/google/play/integrity/remediation#get-licensed-dialog) (which gets the user back to a Play licensed and Play recognized state), and [CLOSE_UNKNOWN_ACCESS_RISK](https://developer.android.com/google/play/integrity/remediation#close-unknown-access-risk-dialog) and [CLOSE_ALL_ACCESS_RISK](https://developer.android.com/google/play/integrity/remediation#close-all-access-risk-dialog) (which prompt the user to close potentially risky apps).

### Choose modern integrity solutions

In addition to Play Integrity API, Google offers several other features to consider as part of your overall anti-abuse strategy. Both Play Integrity API and Play's automatic protection offer user experience and developer benefits for safeguarding app distribution. We encourage existing apps to migrate to these modern integrity solutions instead of using the [legacy Play licensing library](https://developer.android.com/google/play/licensing).

**Automatic protection:** Prevent unauthorized access with Google Play's [automatic protection](https://support.google.com/googleplay/android-developer/answer/10183279) and ensure users continue getting your official app updates. Turn it on and Google Play will automatically add an installer check to your app's code, with no developer integration work required. If your protected app is redistributed or shared through another channel, then the user will be prompted to get your app from Google Play. Eligible Play developers also have access to Play's advanced anti-tamper protection, which uses obfuscation and runtime checks to make it harder and costlier for attackers to modify and redistribute protected apps.

**Android platform key attestation:** Play Integrity API is the recommended way to benefit from hardware-backed [Android platform key attestation](https://developer.android.com/privacy-and-security/security-key-attestation). Play Integrity API takes care of the underlying implementation across the device ecosystem, Play automatically mitigates key-related issues and outages, and you can use the API to detect other threats. Developers who directly implement key attestation instead of relying on Play Integrity API should prepare for the upcoming Android Platform [root certificate rotation](https://developer.android.com/privacy-and-security/security-key-attestation#root_certificate_rotation) in February 2026 to avoid disruption (developers using Play Integrity API do not need to take any action).

**Firebase App Check** : Developers using Firebase can use [Firebase App Check](https://firebase.google.com/docs/app-check) to receive an app and device integrity verdict powered by Play Integrity API on certified Android devices, along with responses from other platform attestation providers. To detect all other threats and use other Play features, integrate Play Integrity API directly.

**reCAPTCHA Enterprise** : Enterprise customers looking for a complete fraud and bot management solution can purchase [reCAPTCHA Enterprise](https://cloud.google.com/recaptcha-enterprise) for mobile. reCAPTCHA Enterprise uses some of Play Integrity API's anti-abuse signals, and combines them with reCAPTCHA signals out of the box.

### Safeguard your business today

With a strong foundation in hardware-backed security and new automated remediation dialogs simplifying integration, the Play Integrity API is an essential tool for protecting your growth.

[Get started with the Play Integrity API documentation](https://developer.android.com/google/play/integrity/overview).

###### Written by:

-

  ## [Dom Elliott](https://developer.android.com/blog/authors/dom-elliott)

  ###### Group Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/dom-elliott) ![](https://developer.android.com/static/blog/assets/dom_elliot_d78b0628db_flDQk.webp) ![](https://developer.android.com/static/blog/assets/dom_elliot_d78b0628db_flDQk.webp)
-

  ## [Eric Lynch](https://developer.android.com/blog/authors/eric-lynch)

  ###### Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/eric-lynch) ![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg) ![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)](https://developer.android.com/blog/authors/thomas-ezan) 17 Apr 2026 17 Apr 2026 ![](https://developer.android.com/static/blog/assets/Hybrid_inference_solution_for_Android_Blog_1_518db36e12_gOJm.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Experimental hybrid inference and new Gemini models for Android](https://developer.android.com/blog/posts/experimental-hybrid-inference-and-new-gemini-models-for-android)

  [arrow_forward](https://developer.android.com/blog/posts/experimental-hybrid-inference-and-new-gemini-models-for-android) If you are an Android developer looking to implement innovative AI features into your app, we recently launched powerful new updates.

  ###### [Thomas Ezan](https://developer.android.com/blog/authors/thomas-ezan) •
  3 min read

- [![](https://developer.android.com/static/blog/assets/dgalpin_30033d2d42_Z1EXpfD.webp)](https://developer.android.com/blog/authors/daniel-galpin) 16 Apr 2026 16 Apr 2026 ![](https://developer.android.com/static/blog/assets/android17banner_359909419a_Z1HMAIH.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [The Fourth Beta of Android 17](https://developer.android.com/blog/posts/the-fourth-beta-of-android-17)

  [arrow_forward](https://developer.android.com/blog/posts/the-fourth-beta-of-android-17) Android 17 has reached beta 4, the last scheduled beta of this release cycle, a critical milestone for app compatibility and platform stability.

  ###### [Daniel Galpin](https://developer.android.com/blog/authors/daniel-galpin) •
  4 min read

- [![](https://developer.android.com/static/blog/assets/Bennet_Manuel_4be9960838_MydbH.webp)](https://developer.android.com/blog/authors/bennet-manuel) 15 Apr 2026 15 Apr 2026 ![](https://developer.android.com/static/blog/assets/260409_Uyo_policy_bundle_Header_dae9a057fb_2u7Yfb.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Boosting user privacy and business protection with updated Play policies](https://developer.android.com/blog/posts/boosting-user-privacy-and-business-protection-with-updated-play-policies)

  [arrow_forward](https://developer.android.com/blog/posts/boosting-user-privacy-and-business-protection-with-updated-play-policies) Making Google Play the safest and most trusted experience possible. Today, we're announcing a new set of policy updates and an account transfer feature to boost user privacy and protect your business from fraud.

  ###### [Bennet Manuel](https://developer.android.com/blog/authors/bennet-manuel) •
  3 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)