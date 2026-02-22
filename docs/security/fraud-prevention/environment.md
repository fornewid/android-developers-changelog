---
title: https://developer.android.com/security/fraud-prevention/environment
url: https://developer.android.com/security/fraud-prevention/environment
source: md.txt
---

# Secure the environment

Google offers a set of APIs and services to help you detect if your app is running in a safe and trusted environment. The centerpiece is the Play Integrity API, which helps check that interactions are genuine by detecting potentially risky and fraudulent interactions. In addition to app and device integrity, Play Integrity API now offers information about[access and accessibility risks](https://developer.android.com/google/play/integrity/verdicts#app_access_risk_verdict),[Google Play Protect](https://developer.android.com/google/play/integrity/verdicts#play_protect_verdict), and[recent device activity](https://developer.android.com/google/play/integrity/verdicts#recent-device-activity). To further harden your anti-fraud strategy the Android platform offers APIs for specific scenarios that might be relevant to your app.

## Play Integrity API

![Play Integrity API features](https://developer.android.com/static/images/security/fraud-prevention/play-integrity-api-features.png)

The[Play Integrity API](https://developer.android.com/google/play/integrity/overview)lets you learn about the security state of the device their app is running on. This helps you be confident that the right user is accessing sensitive information.

It helps you check that interactions and server requests are coming from your genuine app binary in a trustworthy environment:

- **Genuine app binary**: Determine whether you're interacting with your unmodified binary that Google Play recognizes.
- **Genuine Play install**: Determine whether the current user account is licensed, which means that the user installed or paid for your app or game on Google Play.
- **Genuine Android device**: Determine whether your app is running on a genuine Android-powered device powered by Google Play services.
- **Free of known malware**: Determine whether Google Play Protect is turned on and whether it has found risky or dangerous apps installed on the device.
- **Low risk of access by other apps**: Determine whether other apps are running that could capture the screen or control the device and inputs into your app.

### How this helps mitigate fraud

When a user performs an important action in your app, you can call the Play Integrity API. If it didn't, then your app's backend server can decide what to do to defend against attacks and fraud. For example, you could require additional user verification or deny access to sensitive functionality.

![The Play Integrity API decision flow](https://developer.android.com/static/images/security/fraud-prevention/play-integrity-decision-flow.png)

### App Access Risk

The[App Access Risk](https://developer.android.com/google/play/integrity/verdicts#app_access_risk_verdict)signal was introduced to help you assess whether other apps on a device could be viewing and capturing the screen when your app is running or accessing your app using accessibility permissions. Verified accessibility apps are automatically excluded from these verdicts. App access risk helps developers protect their apps while preserving user privacy because the requesting app does not obtain the identity of installed apps and the verdict is not linked to user or device identifiers.

![Screenshot of phone requiring the user to close certain apps.](https://developer.android.com/static/images/security/fraud-prevention/app-access-risk-signal.png)
> *Thanks to this collaborative effort, we are able to get the signals needed to give us deeper insights to protect our customers more effectively.
> **---Nubank, early access partner***

App Access Risk has different risk levels:

- A capturing response means other apps are running that can capture the screen.
- A controlling response means other apps are running that can control the device, and hence they could both capture the screen and control the inputs into your app.

### App Access Risk enforcement

Identify high value or sensitive actions in your app or game to protect with the Play Integrity API instead of denying access outright. When possible, challenge risky traffic before allowing high-value actions to proceed. For example, when the app access risk indicates that an app is running that could capture the screen, ask the user to disable or uninstall apps that can capture the screen before allowing them to proceed to functionality that you want to protect.

This table contains some example verdicts:

|                                  Example app access risk verdict response                                  |                                                                                                                                        Interpretation                                                                                                                                         |
|------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `appsDetected:` `["KNOWN_INSTALLED"]`                                                                      | There are only apps installed that are recognized by Google Play or preloaded on the system partition by the device manufacturer. There are no apps running that would result in the capturing, controlling, or overlays verdicts.                                                            |
| `appsDetected:` `["KNOWN_INSTALLED",` `"UNKNOWN_INSTALLED",` `"UNKNOWN_CAPTURING"]`                        | There are apps installed by Google Play or preloaded on the system partition by the device manufacturer. There are other apps running and have permissions enabled that could be used to view the screen or capture other inputs and outputs.                                                 |
| `appsDetected:` `["KNOWN_INSTALLED",` `"KNOWN_CAPTURING",` `"UNKNOWN_INSTALLED",` `"UNKNOWN_CONTROLLING"]` | There are Play or system running that have permissions enabled that could be used to view the screen or capture other inputs and outputs. There are also other apps running that have permissions enabled that could be used to control the device and directly control inputs into your app. |
| `appAccessRiskVerdict: {}`                                                                                 | App access risk is not evaluated because a necessary requirement was missed. For example, the device was not trustworthy enough.                                                                                                                                                              |

### Play Protect Signal

The Play Protect Signal tells your app whether Play Protect is turned on and whether it has found known harmful apps installed on the device.  

    environmentDetails:{
      playProtectVerdict: "NO_ISSUES"
    }

If malware is a particular concern for your app or your users' data, you can check this verdict and ask your users to turn on Play Protect or remove harmful apps before proceeding.

![Turn on Play Protect dialog](https://developer.android.com/static/images/security/fraud-prevention/turn-on-play-protect.png)

`playProtectVerdict`can have one of the following values:

|     Verdict     |                                                                                             Explanation                                                                                             |                                                                                                 Recommended Action                                                                                                  |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `NO_ISSUES`     | Play Protect is turned on and did not find any app issues on the device.                                                                                                                            | Play Protect is on and hasn't found any issues so no user action is required.                                                                                                                                       |
| `NO_DATA`       | Play Protect is turned on but no scan has been performed yet. The device or the Play Store app may have been recently reset.                                                                        | Play Protect is on and hasn't found any issues so no user action is required.                                                                                                                                       |
| `POSSIBLE_RISK` | Play Protect is turned off.                                                                                                                                                                         | Play Protect is on and hasn't found any issues so no user action is required.                                                                                                                                       |
| `MEDIUM_RISK`   | Play Protect is turned on and has found potentially harmful apps installed on the device.                                                                                                           | Depending on your risk tolerance, you can ask the user to launch Play Protect and take action on the Play Protect warnings. If the user can't fulfill these requirements you may block them from the server action. |
| `HIGH_RISK`     | Play Protect is turned on and has found dangerous apps installed on the device.                                                                                                                     | Depending on your risk tolerance, you can ask the user to launch Play Protect and take action on the Play Protect warnings. If the user can't fulfill these requirements you may block them from the server action. |
| `UNEVALUATED`   | The Play Protect verdict was not evaluated. This could happen for several reasons, including the following: - The device is not trustworthy enough. - Games only: The user account is not LICENSED. |                                                                                                                                                                                                                     |

### Recent device activity

You can also opt-in to recent device activity, which tells you how many times your app requested an integrity token on a specific device in the last hour. You can use recent device activity to protect your app against unexpected, hyperactive devices that could be an indication of an active attack. You can decide how much to trust each recent device activity level based on how many times you expect your app installed on a typical device to request an integrity token each hour.

If you opt-in to receive`recentDeviceActivity`the`deviceIntegrity`field will have two values:  

    deviceIntegrity: {
      deviceRecognitionVerdict: ["MEETS_DEVICE_INTEGRITY"]
      recentDeviceActivity: {
        // "LEVEL_2" is one of several possible values.
        deviceActivityLevel: "LEVEL_2"
      }
    }

First, you should check the data to see what the typical device activity levels for your app are across all your devices. Then, you can decide how your app should respond when a device is making too many requests. If the activity is a little high, you might want to ask the user to try again later. If the activity is very high, you might want to take stronger enforcement action.

### Standard versus classic requests

As part of your implementation of Play Integrity, it is important to consider the two types of requests. You should use**standard** requests in most cases, to provide the fastest response - and**classic requests**should be used where a newly generated request against the device attestation record is needed.

|                                                                                  Classic request                                                                                  |                                                                                              Standard request                                                                                              |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Requests take longer and should be made less frequently. For example as an occasional one-off to check if a highly valuable or sensitive action is genuine. **Use infrequently**. | Requests are low latency and can be used on demand. A standard request consists of two parts: - Prepare the integrity token provider (one off) - Request an integrity token (on demand) **Use on demand**. |

Read the Play Integrity documentation for more information on[standard](https://developer.android.com/google/play/integrity/standard)and[classic](https://developer.android.com/google/play/integrity/classic)requests.

### Implementation

To get started with the Play Integrity API:

- [Enable Play Integrity API](https://developer.android.com/google/play/integrity/setup#set-integrity-responses)responses in your Google Play Console and link to a Google Cloud project.
- [Integrate the Play Integrity API](https://developer.android.com/google/play/integrity/setup#integrate-in-app)in your app.
- Decide how you'll[handle verdicts](https://developer.android.com/google/play/integrity/overview#have-tiered).

By default, Play Integrity API allows up to 10K requests per app per day. To express interest in increasing your daily maximum requests,[follow these instructions](https://developer.android.com/google/play/integrity/setup#increase-daily). To be eligible for an increase in your daily maximum number of requests, your app must implement Play Integrity API correctly and be available on Google Play in addition to any other distribution channels.

### Things to keep in mind for the Play Integrity API

- It is essential you handle errors in the Play Integrity APIs responses, appropriately. Follow the[guide here on retry and enforcement strategies](https://developer.android.com/google/play/integrity/error-codes)based on error codes.
- The Play Integrity API offers[testing tools for responses](https://developer.android.com/google/play/integrity/additional-tools#test-different).
- To see the integrity result from your device,[follow these steps](https://developer.android.com/google/play/integrity/additional-tools#check-device).
- Read these[security considerations](https://developer.android.com/google/play/integrity/overview#security-considerations)for recommended practices using the Play Integrity API.

## Automatic integrity protection (API \>= 23)

Automatic integrity protection is an anti-tamper code protection service that protects your app against integrity abuse in the form of unauthorized modification and redistribution. It works without a data connection and requires no developer work before testing and no backend server integration.

### How this helps mitigate fraud

When you turn on automatic integrity protection, Google Play adds checks to your app's code and makes them hard to remove with advanced obfuscation and anti-reverse engineering techniques. At runtime, the protection checks if your app has been tampered or redistributed:

- If the installer check fails, users will be prompted to get on your app on Google Play
- If the modification check fails, the app won't run

This helps keep users safe from modified versions of your app.

### Implementation

Automatic integrity protection is only available to select Play Partners at this time. Contact Google Play developer support if the feature is not available in your Google Play Console and you would like to express interest in getting access.

You can either turn on protection when creating a release or on the[App integrity](https://play.google.com/console/developers/app/app-integrity/overview)page (Release \> App integrity). Automatic integrity protection requires your app to use[Play App Signing](https://support.google.com/googleplay/android-developer/answer/9842756).

**Be sure to test your protected app before promoting the release to production**.

### Things to keep in mind

- Don't release unprotected app versions
- Take care when mixing anti-tamper protection solutions
- Test your protected app before releasing it to production
- Monitor stats as normal for any increase in crashes
- You can report cracked versions of your app to Google Play