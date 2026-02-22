---
title: https://developer.android.com/privacy-and-security/risks/unsafe-use-of-deeplinks
url: https://developer.android.com/privacy-and-security/risks/unsafe-use-of-deeplinks
source: md.txt
---

# Unsafe use of deep links

<br />

**OWASP category:** [MASVS-PLATFORM: Platform Interaction](https://mas.owasp.org/MASVS/09-MASVS-PLATFORM)

## Overview

The security risks associated with deep links stem from their core capability of enabling seamless navigation and interaction within mobile applications. Deep link vulnerabilities arise from weaknesses in the implementation or handling of deep links. These flaws can be exploited by malicious actors to gain access to privileged functions or data, potentially resulting in data breaches, privacy violations, and unauthorized actions. Attackers can exploit these vulnerabilities through various techniques, such as deep link hijacking and data validation attacks.

## Impact

The lack of a proper deep link validation mechanism, or the unsafe use of deeplinks, can aid malicious users in performing attacks such as host validation bypass, cross-app scripting, and remote code execution within the permissions context of the vulnerable application. Depending on the nature of the application, this can result in unauthorized access to sensitive data or functions.

## Mitigations

### Prevent deep link hijacking

By design, Android allows multiple apps to register intent filters for the same deep link URI. To prevent malicious apps from intercepting deep links intended for your app, implement the`android:autoVerify`attribute in`intent-filter`within the application's`AndroidManifest`. This allows users to select their preferred app for handling deep links, ensuring the intended operation and preventing malicious applications from automatically interpreting them.

Android 12[introduced](https://developer.android.com/about/versions/12/behavior-changes-all#web-intent-resolution)stricter handling of web intents to improve security. Apps must now be verified to handle links from specific domains, either through Android App Links or user selection in system settings. This prevents apps from hijacking links they shouldn't handle.

To enable link handling verification for your app, add intent filters that match the following format (this example is taken from the[Verify Android App Links](https://developer.android.com/training/app-links/verify-android-applinks)documentation):  

      <!-- Make sure you explicitly set android:autoVerify to "true". -->
      <intent-filter android:autoVerify="true">
          <action android:name="android.intent.action.VIEW" />
          <category android:name="android.intent.category.DEFAULT" />
          <category android:name="android.intent.category.BROWSABLE" />
      
          <!-- If a user clicks on a shared link that uses the "http" scheme, your
               app should be able to delegate that traffic to "https". -->
          <data android:scheme="http" />
          <data android:scheme="https" />
      
          <!-- Include one or more domains that should be verified. -->
          <data android:host="..." />
      </intent-filter>

### Implement robust data validation

Deep links can include additional parameters that are served to the target intent, for example, to perform further actions. The foundation of secure deep link handling is stringent data validation. All incoming data from deep links should be meticulously validated and sanitized by developers to prevent malicious code or values from being injected within the legitimate application. This can be implemented by checking the value of any deep link parameter against a predefined allowlist of expected values.

Apps should check other relevant internal states, such as authentication state, or authorization, before exposing sensitive information. An example might be a reward for completing a level of a game. In this case it's worth validating the precondition of having completed the level, and redirecting to the main screen if not.

## Resources

- [Verify Android App Links](https://developer.android.com/training/app-links/verify-android-applinks)
- [Handling Android App Links](https://developer.android.com/training/app-links)
- [Web intent resolution](https://developer.android.com/about/versions/12/behavior-changes-all#web-intent-resolution)
- [Account takeover intercepting magic link for Arrive app](https://hackerone.com/reports/855618)
- [Deep Links \& WebViews Exploitations Part I](https://www.justmobilesec.com/en/blog/deep-links-webviews-exploitations-part-I)
- [Deep Links \& WebViews Exploitations Part II](https://www.justmobilesec.com/en/blog/deep-links-webviews-exploitations-part-II)
- [Recent suggestion of a deep link issue in Jetpack Navigation](https://swarm.ptsecurity.com/android-jetpack-navigation-go-even-deeper/)