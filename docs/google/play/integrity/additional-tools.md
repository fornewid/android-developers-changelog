---
title: https://developer.android.com/google/play/integrity/additional-tools
url: https://developer.android.com/google/play/integrity/additional-tools
source: md.txt
---

# Additional tools and support

The following tools and resources will help you make the most of the Play Integrity API as part of your anti-abuse strategy.

## Monitor Play Integrity API status

The[Play status dashboard](https://status.play.google.com)shows status information for the Play Integrity API. Information will be posted about service status including any disruptions and outages. If you're experiencing an issue not listed on the page, please contact[Google Play developer support](https://support.google.com/googleplay/android-developer/contact/piaqr).

## Test different Play Integrity API responses within your app

You can create tests to evaluate how the Play Integrity API interacts with your app. For email addresses you specify, you can select the integrity verdicts or error code they should get in your app from Google Play's servers. This lets you test how your app reacts to all possible responses and errors.

You can set up a test in your Play Console. In the**Release** section of the left menu, go to**App integrity** . Next to**Play Integrity API** , click**Settings** and find**Testing** to get started. For detailed instructions, see the[Play Console help center](https://support.google.com/googleplay/android-developer/answer/11395166).

Note that for test responses an additional`testingDetails`field appears in the[returned payload](https://developer.android.com/google/play/integrity/verdicts#returned-verdict-format).  

```json
"testingDetails": {
  "isTestingResponse": true
}
```

## Analyze the Play Integrity API responses your app is receiving

You can access reporting for the Play Integrity API in your Play Console to understand the responses your app is receiving and identify potential issues. To see your report, go to the**App integrity** page and click**View report**in Play Integrity API section.

The report shows:

- The volume of standard and classic requests that your app is making.
- A breakdown of each verdict response for device, app, and account details. Optional verdicts are not yet shown on the report.
- The most common error codes that your app is encountering.
- The most common certificates from unrecognized app versions.

You can filter the report by app version, country, and Android OS version to get a more detailed view of your integrity verdicts. Data is not shown when the request volume is low to protect user privacy.
| **Tip:** Integrating the Play Integrity API so that you can analyze responses from your install base is a good first step to help you determine your enforcement strategy.

## Check the device integrity verdict from any device

If you need to verify what integrity verdict the Play Integrity API returns for your app on a particular device---for example, while debugging or troubleshooting a user-reported issue---you can use the Play Store app to generate a Play Integrity API verdict for that device.

First, enable the Play Store's developer options on the device. Tap your profile icon and then tap**Settings** . Open the**About** menu and tap the row labeled**Play Store version**seven times to unlock developer mode.

Then, to generate a verdict from an Android device, open the Play Store app. Tap your profile icon and then tap**Settings** . Open the**General** menu and then tap**Developer options** . In**Play Integrity** settings, tap**Check integrity**to generate a verdict.
| **Tip:** The verdict generated when you tap**Check integrity** on a device contains all default and optional verdicts. Your app will only receive the optional verdicts when it calls Play Integrity API if you[have configured](https://developer.android.com/google/play/integrity/setup#configure-api)them in the Play Console.

## Help users fix integrity issues

The Play Integrity API provides various[Play remediation dialogs](https://developer.android.com/google/play/integrity/remediation)that you can trigger within your app to assist users in resolving specific verdict issues.

To guide users towards resolving device integrity issues, you can direct them to the troubleshooting feature within the Play Store app. To fix the device integrity issues, instruct the user to do the following steps:

1. Open the Google Play Store app.
2. At the top right, tap the profile icon.
3. Tap**Settings \> About \> Play Protect certification**.
4. Tap**Fix device issue**. This button is only visible to users whose devices don't pass Play device integrity checks. The user will then see a series of prompts that will help them troubleshoot and, if possible, fix the device issue.

## Consider end to end Enterprise fraud solutions

Enterprise customers looking for a complete fraud and bot management solution can purchase[reCAPTCHA Enterprise](https://cloud.google.com/recaptcha-enterprise)for mobile, which includes[SDKs for Android](https://cloud.google.com/recaptcha-enterprise/docs/instrument-android-apps)that provide fraud risk scores to developers. reCAPTCHA Enterprise automatically includes Play Integrity API signals, and combines them with reCAPTCHA network and application signals for customers, providing a frictionless, invisible fraud management solution out of the box. It can also provide protection for Android apps where Play Integrity API is not available.

## Get support

To report an unexpected Play Integrity API verdict, please[submit an issue](https://issuetracker.google.com/issues/new?component=1152695)with all of the information requested.

To ask questions or to provide feedback about the Play Integrity API, you can either:

- Contact Google Play developer support directly from your Play Console.
- Complete[this form](https://support.google.com/googleplay/android-developer/contact/piaqr)in the Play Console Help Center.

If you're requesting to increase the number of daily requests your app makes, it can take up to a week. We strongly recommend monitoring your Play Integrity API usage in your Google Play Console or in your Google Cloud Console, where you can also set up[quota alerts](https://cloud.google.com/docs/quota?&_ga=2.68760982.-685660492.1676978684#monitoring_quota_metrics), to avoid interruptions to your service.