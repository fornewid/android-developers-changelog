---
title: https://developer.android.com/health-and-fitness/health-connect/publish
url: https://developer.android.com/health-and-fitness/health-connect/publish
source: md.txt
---

To get your health app published on Google Play, you must complete a few
required steps in the Play Console. These steps verify your app is compliant
with Google's policies and provides a safe and transparent experience for users.

1. [Review the Google Play policies](https://developer.android.com/health-and-fitness/health-connect/publish#review-policies)
2. [Fill out the Data Safety section in the console](https://developer.android.com/health-and-fitness/health-connect/publish#data-safety-section)
3. [Fill out the Health Apps declaration form](https://developer.android.com/health-and-fitness/health-connect/publish#declare-access) in the console

## Review the Google Play policies

Be sure your app is in compliance with the following Google Play policies:

- [User data](https://support.google.com/googleplay/android-developer/answer/10144311#personal-sensitive)
- [Permissions and APIs that access sensitive information (including additional
  requirements for Health Connect)](https://support.google.com/googleplay/android-developer/answer/9888170#ahp)

## Provide information for Google Play's Data safety section

As part of your app publishing process, you must provide information for Google
Play's [Data safety section](https://support.google.com/googleplay/android-developer/answer/10787469#type-health-info&zippy=data-types). This helps users understand your
app's data collection, sharing, and security practices.

## Declare access to Health Connect data types

When your app is ready for release, the next step is to declare uses of the
data types you [reviewed](https://developer.android.com/health-and-fitness/guides/health-connect/data-and-data-types/data-types) earlier. You complete this declaration process
while preparing your app for publishing on Google Play.

This process must be completed for all publishing requests, both for a new app
that has not been published yet, or when updating an existing, already published
app that now uses a different set of data types.

To verify this process goes smoothly:

- Only request permissions and access data types that support the specific, user-facing health features you offer. Don't request broader access than necessary. Provide as much detail as possible when documenting the reason for using a particular data type.
- [Post your app's privacy policies](https://support.google.com/googleplay/android-developer/answer/9859455) on its Play store page. This must be the same privacy policy that is displayed to users when they [click the privacy policy link in Health Connect](https://developer.android.com/health-and-fitness/health-connect/get-started#show-privacy-policy).

## Explain why your app uses Health Connect data types

To use Health Connect data types in your app, go to the Play Console and fill
out the **Health apps** form on the **App content** page:

1. Indicate which health features your app supports from the following list,
   based on the Health Connect data types that your app accesses, as shown in
   figure 1.

   **Note:** If your app doesn't access any health or fitness information, select the checkbox next to **My app does not have any health features**.  
   ![A checkbox appears next to each health feature](https://developer.android.com/static/images/health-and-fitness/health-features-play-console.png) **Figure 1.** Declare health features used in your app in the Play Console.  
   ![Each explanation is a text area where you enter an
   explanation](https://developer.android.com/static/images/health-and-fitness/health-apps-permissions-play-console.png) **Figure 2.** Explain how your app uses each Health Connect data type in the Play Console.

   The Play Console page includes these health features:
   - Health and fitness
     - Activity and fitness
     - Nutrition and weight management
     - Period tracking
     - Sleep management
     - Stress management, relaxation, mental acuity
     - Diseases and conditions management
   - Medical
     - Clinical decision support
     - Disease prevention and public health
     - Emergency and first aid
     - Healthcare services and management
     - Medical device apps
     - Mental and behavioral health
     - Medical reference and education
     - Medication and pain management
     - Physical therapy and rehabilitation
     - Reproductive and sexual health
   - Human subjects research: Research studies, clinical trials, and patient communities
2. On the following screen, provide an explanation of how your app uses each
   listed Health Connect data type. The data types appear in the following
   categories, as shown in figure 2:

   - Activity and fitness
   - Body composition
   - Energy
   - Nutrition
   - Reproductive and sexual health
   - Respiratory system
   - Sleep management

   Make sure to follow these guidelines when explaining your app's usage of
   Health Connect data types:
   - For each permission requested, provide a clear and detailed justification explaining how your app uses the data to benefit the user.
   - If your app does not require access to specific data types, you must not request access to them.
   - Be as detailed as possible in documenting the purpose for your access requests.
   - Request the minimum data types needed and provide a valid use case for each request.

   See the example on the
   [Android Health Permissions support page](https://support.google.com/googleplay/android-developer/answer/12991134#zippy=%2Cfitness-wellness-and-coaching).

Learn more about how to
[provide information for the Health apps declaration form](https://support.google.com/googleplay/android-developer/answer/14738291).

## Reapply for updates

If your app has a new data type requirement, or if your app no longer supports
a data type, fill out the **Health apps declaration form** again. Take note of
the following:

- Include all of the existing health features the app still uses.
- Include all of the new health features the app requires.
- Exclude all of the health features that the app no longer needs.
- Make sure you justify every requested access.

If you have requested before and you have a new app version, you don't have to
file a new request just to change the app version. The data type accesses are
allow-listed for a package name regardless of app version.
| **Note:** When you submit a new app version, your app's declaration may be reviewed again.

## If you previously filled out the Google Health Connect API Request form

In the past, developers requested access to Health Connect data types by
filling out the Google Health Connect API Request form. If you
used this form, **you must declare uses of these data types in the Play Console
by January 22, 2025.**

Follow the process in this guide to update your app registration in the Play
Console and declare access to the data types you are already using.
| **Warning:** If you fail to complete the declaration form before the deadline, you will be unable to send any changes to your app registration for review until you have completed and submitted the declaration.

## Unable to access Health Connect

If your health app is published in the Play store and released to the public,
but you didn't request for data type accesses, your end users receive the
following dialog when attempting to link with Health Connect:

![A dialog showing users that the app can't access Health Connect.](https://developer.android.com/static/health-and-fitness/health-connect/images/cant-access-hc.png)

## Further questions

If you have any questions or encounter issues in your access, submit a ticket to
[Health Connect Developer Support](https://issuetracker.google.com/issues/new?component=1676744&template=2072671).