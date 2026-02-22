---
title: https://developer.android.com/about/versions/14/changes/data-safety
url: https://developer.android.com/about/versions/14/changes/data-safety
source: md.txt
---

# Data safety information is more visible

To enhance user privacy, Android 14 increases the number of places where the system shows the information you have declared in the Play Console form. Currently, users can view this information in the**Data safety**section on your app's listing in Google Play.

We encourage you to review your app's location data sharing policies and take a moment to make any applicable updates to your app's[Google Play Data safety section](https://support.google.com/googleplay/android-developer/answer/10787469).

## Permission rationale

For some permissions, the system runtime permission dialog now includes a clickable section that highlights your app's data sharing practices. This section of the system dialog includes information, such as why your app may decide to share data with third parties, and links users to where they can control your app's data access.
| **Note:** In Android 14, this data sharing information only appears in permission dialogs related to location permissions if your app has declared that it[shares location data with third parties](https://support.google.com/googleplay/android-developer/answer/10787469#zippy=%2Cwhat-users-will-see-if-your-app-shares-user-data). However, the system might include this information within additional dialogs in upcoming releases.

## System notification

If the user shares their location in your app, and if your app then broadens its location-sharing practices in one of the following ways, the user see a system notification within 30 days:
![When the user taps anywhere on the system notification, the 'Data sharing updates for location' page loads in system settings. A list near the middle of the screen shows the apps that have changed their data-sharing practices](https://developer.android.com/static/about/versions/14/images/data-safety-system-notification.png)**Figure 1**: System notification that appears when some installed apps change their data-sharing practices

- Your app starts sharing location data with third parties.
- Your app starts sharing location data for ads-related purposes.

When users tap on this notification, they're taken to a new location data sharing updates page that shows a detailed list of apps that made relevant changes, along with an easy way to change each app's permission settings. Figure 1 shows an example of this flow.

The new location data sharing updates page is permanently accessible from the device's**Settings \> Privacy** or**Settings \> Security \& Privacy**page, and shows recent increases to location data sharing.