---
title: https://developer.android.com/blog/posts/stronger-threat-detection-simpler-integration-protect-your-growth-with-the-play-integrity-api
url: https://developer.android.com/blog/posts/stronger-threat-detection-simpler-integration-protect-your-growth-with-the-play-integrity-api
source: md.txt
---

> Documentation index: https://developer.android.com/blog/llms.txt

[Product News](https://developer.android.com/blog/categories/product-news.md.txt)

# Stronger threat detection, simpler integration: Protect your growth with the Play Integrity API

5 min read ![](https://developer.android.com/static/blog/assets/SS_Alt_Playbrand_Integrity_API_21cd2391d2_Z2k9Cew.webp) 19 Nov 2025 [![View Dom Elliott's profile](https://developer.android.com/static/blog/assets/dom_elliot_d78b0628db_ZAGWES.webp)](https://developer.android.com/blog/authors/dom-elliott.md.txt)[![View Eric Lynch's profile](https://developer.android.com/static/blog/assets/Eric_Lynch_bb0a252f52_ZRW5B5.webp)](https://developer.android.com/blog/authors/eric-lynch.md.txt) [Dom Elliott](https://developer.android.com/blog/authors/dom-elliott.md.txt) \& [Eric Lynch](https://developer.android.com/blog/authors/eric-lynch.md.txt) In the mobile ecosystem, abuse can threaten your revenue, growth, and user trust. To help developers thrive, Google Play offers a resilient threat detection service, [**Play Integrity API**](https://developer.android.com/google/play/integrity/overview.md.txt). Play Integrity API helps you verify that interactions and server requests are genuine---coming from your unmodified app on a certified Android device, installed by Google Play.

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

Apps and games have found success with the Play Integrity API by following the [security considerations](https://developer.android.com/google/play/integrity/overview.md.txt#security-considerations) and taking a phased approach to their anti-abuse strategy.

**Step 1: Decide what you want to protect**: Decide what actions and server requests in your apps and games are important to verify and protect. For example, you could perform integrity checks when a user is launching the app, signing in, joining a multiplayer game, generating AI content, or transferring money.

**Step 2: Collect integrity verdict responses**: Perform integrity checks at important moments to start collecting verdict data, without enforcement initially. That way you can analyze the responses for your install base and see how they correlate with your existing abuse signals and historical abuse data.

**Step 3: Decide on your enforcement strategy**: Decide on your enforcement strategy based on your analysis of the responses and what you are trying to protect. For example, you could change risky traffic at important moments to protect sensitive functionality. The API offers a range of responses so you can implement a tiered enforcement strategy based on the trust level you give to each combination of responses.

**Step 4: Gradually rollout enforcement and support your users:** Gradually roll out enforcement. Have a retry strategy when verdicts have issues or are unavailable and be prepared to support good users who have issues. The new Play in-app remediation prompts, described below, make it easier than ever to get users with issues back to a good state.

### NEW: Let Play recover users with issues automatically

Deciding how to respond to different integrity signals can be complex, you need to handle various integrity responses and API error codes (like network issues or outdated Play services). We're simplifying this with new [**Play in-app remediation prompts**](https://developer.android.com/google/play/integrity/remediation.md.txt). You can show a Google Play prompt to your users to automatically fix a wide range of issues directly within your app. This reduces integration complexity, ensures a consistent user interface, and helps get more users back to a good state.
![get_integrity.gif](https://developer.android.com/static/blog/assets/get_integrity_7d2e165184_1VjSU5.webp)

*GET_INTEGRITY automatically detects the issue (in this example, a network error) and resolves it.*

You can trigger the[GET_INTEGRITY](https://developer.android.com/google/play/integrity/remediation.md.txt#get-integrity-dialog) dialog, available in Play Integrity API library version 1.5.0+, after a range of issues to automatically guide the user through the necessary fixes including:

- **Unauthorized access:**GET_INTEGRITY guides the user back to a Play licensed response in accountDetails.
- **Code tampering:** GET_INTEGRITY guides the user back to a Play recognized response in appIntegrity.
- **Device integrity issues:** GET_INTEGRITY guides the user on how to get back to the MEETS_DEVICE_INTEGRITY state in `deviceIntegrity`.
- **Remediable error codes:** GET_INTEGRITY resolves remediable API errors, such as prompting the user to fix network connectivity or update Google Play Services.

We also offer specialized dialogs including[GET_STRONG_INTEGRITY](https://developer.android.com/google/play/integrity/remediation.md.txt#get-strong-integrity-dialog) (which works like GET_INTEGRITY while also getting the user back to the MEETS_STRONG_INTEGRITY state with no known malware issues in the `playProtectVerdict`), [GET_LICENSED](https://developer.android.com/google/play/integrity/remediation.md.txt#get-licensed-dialog) (which gets the user back to a Play licensed and Play recognized state), and [CLOSE_UNKNOWN_ACCESS_RISK](https://developer.android.com/google/play/integrity/remediation.md.txt#close-unknown-access-risk-dialog) and [CLOSE_ALL_ACCESS_RISK](https://developer.android.com/google/play/integrity/remediation.md.txt#close-all-access-risk-dialog) (which prompt the user to close potentially risky apps).

### Choose modern integrity solutions

In addition to Play Integrity API, Google offers several other features to consider as part of your overall anti-abuse strategy. Both Play Integrity API and Play's automatic protection offer user experience and developer benefits for safeguarding app distribution. We encourage existing apps to migrate to these modern integrity solutions instead of using the [legacy Play licensing library](https://developer.android.com/google/play/licensing.md.txt).

**Automatic protection:** Prevent unauthorized access with Google Play's [automatic protection](https://support.google.com/googleplay/android-developer/answer/10183279) and ensure users continue getting your official app updates. Turn it on and Google Play will automatically add an installer check to your app's code, with no developer integration work required. If your protected app is redistributed or shared through another channel, then the user will be prompted to get your app from Google Play. Eligible Play developers also have access to Play's advanced anti-tamper protection, which uses obfuscation and runtime checks to make it harder and costlier for attackers to modify and redistribute protected apps.

**Android platform key attestation:** Play Integrity API is the recommended way to benefit from hardware-backed [Android platform key attestation](https://developer.android.com/privacy-and-security/security-key-attestation.md.txt). Play Integrity API takes care of the underlying implementation across the device ecosystem, Play automatically mitigates key-related issues and outages, and you can use the API to detect other threats. Developers who directly implement key attestation instead of relying on Play Integrity API should prepare for the upcoming Android Platform [root certificate rotation](https://developer.android.com/privacy-and-security/security-key-attestation.md.txt#root_certificate_rotation) in February 2026 to avoid disruption (developers using Play Integrity API do not need to take any action).

**Firebase App Check** : Developers using Firebase can use [Firebase App Check](https://firebase.google.com/docs/app-check) to receive an app and device integrity verdict powered by Play Integrity API on certified Android devices, along with responses from other platform attestation providers. To detect all other threats and use other Play features, integrate Play Integrity API directly.

**reCAPTCHA Enterprise** : Enterprise customers looking for a complete fraud and bot management solution can purchase [reCAPTCHA Enterprise](https://cloud.google.com/recaptcha-enterprise) for mobile. reCAPTCHA Enterprise uses some of Play Integrity API's anti-abuse signals, and combines them with reCAPTCHA signals out of the box.

### Safeguard your business today

With a strong foundation in hardware-backed security and new automated remediation dialogs simplifying integration, the Play Integrity API is an essential tool for protecting your growth.

[Get started with the Play Integrity API documentation](https://developer.android.com/google/play/integrity/overview.md.txt).
Written by:

-

  ## [Dom Elliott](https://developer.android.com/blog/authors/dom-elliott.md.txt)

  ###### Principal Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/dom-elliott) ![View Dom Elliott's profile](https://developer.android.com/static/blog/assets/dom_elliot_d78b0628db_ZAGWES.webp) ![View Dom Elliott's profile](https://developer.android.com/static/blog/assets/dom_elliot_d78b0628db_ZAGWES.webp)
-

  ## [Eric Lynch](https://developer.android.com/blog/authors/eric-lynch.md.txt)

  ###### Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/eric-lynch) ![View Eric Lynch's profile](https://developer.android.com/static/blog/assets/Eric_Lynch_bb0a252f52_ZRW5B5.webp) ![View Eric Lynch's profile](https://developer.android.com/static/blog/assets/Eric_Lynch_bb0a252f52_ZRW5B5.webp)
Continue reading
- [![View Matthew Forsythe's profile](https://developer.android.com/static/blog/assets/matthew_9c798f0c1d_1FlQLe.webp)](https://developer.android.com/blog/authors/matthew-forsythe.md.txt) 19 Nov 2026 19 Nov 2026 ![](https://developer.android.com/static/blog/assets/ABL_139_Android_developer_verification_Going_global_together_Strapi_01_png_12aa1e5aae_ZkNaef.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Expanding Android developer verification in 2027](https://developer.android.com/blog/posts/android-developer-verification-2027.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/android-developer-verification-2027.md.txt) After over a year of joint preparation with industry leaders, regional partners, app distributors, and Android communities, our user protections successfully went live on September 30 for participating stores across Brazil, Indonesia, Singapore, and Thailand.
  [Matthew Forsythe](https://developer.android.com/blog/authors/matthew-forsythe.md.txt) • 2 min read
  - [#Android](https://developer.android.com/blog/topics/android.md.txt)
- [![View Mekka Okereke's profile](https://developer.android.com/static/blog/assets/unnamed_32_974e21c6be_Z1qBCTw.webp)](https://developer.android.com/blog/authors/mekka-okereke.md.txt) 18 Nov 2026 18 Nov 2026 ![](https://developer.android.com/static/blog/assets/ABL_163_Elevating_Adaptive_App_Quality_Blue_30a2165ec7_Z1hsFPv.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Elevating apps: New adaptive quality standards on Google Play](https://developer.android.com/blog/posts/google-play-adaptive-quality-standards.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/google-play-adaptive-quality-standards.md.txt) To give users the premium experience they expect and ensure your apps shine across every screen size, Google Play is introducing new adaptive app quality requirements that go into effect April 2027.
  [Mekka Okereke](https://developer.android.com/blog/authors/mekka-okereke.md.txt) • 4 min read
  - [#Adaptive Games](https://developer.android.com/blog/topics/adaptive-games.md.txt)
  - [#Foldables](https://developer.android.com/blog/topics/foldables.md.txt)
  - [#Adaptive apps](https://developer.android.com/blog/topics/adaptive-apps.md.txt)
  - +1 ↩
- [![View Aurash Mahbod's profile](https://developer.android.com/static/blog/assets/image3_98854eb3dd_Z2kItkm.webp)](https://developer.android.com/blog/authors/aurash-mahbod.md.txt) 18 Nov 2026 18 Nov 2026 ![](https://developer.android.com/static/blog/assets/ABL_162_2000x1000_1_ce7dba8d2a_72W03.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Elevating games: New large screens and foldables quality standards on Google Play](https://developer.android.com/blog/posts/elevating-game-quality-foldables-large-screens-google-play.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/elevating-game-quality-foldables-large-screens-google-play.md.txt) To give these experiences to players and ensure your games shine across every screen size, Google Play is introducing new large screen quality requirements for games
  [Aurash Mahbod](https://developer.android.com/blog/authors/aurash-mahbod.md.txt) • 4 min read
  - [#Google Play](https://developer.android.com/blog/topics/google-play.md.txt)
  - [#Android](https://developer.android.com/blog/topics/android.md.txt)
  - [#Adaptive Games](https://developer.android.com/blog/topics/adaptive-games.md.txt)
  - [#Foldables](https://developer.android.com/blog/topics/foldables.md.txt)
  - [#Large Screens](https://developer.android.com/blog/topics/large-screens.md.txt)
  - +3 ↩
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)