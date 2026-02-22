---
title: https://developer.android.com/studio/services
url: https://developer.android.com/studio/services
source: md.txt
---

# Service integrations in Android Studio

Android Studio offers a set of service integrations to increase your productivity as you develop, release, and maintain Android apps. For example, you have access to Cloud services such as Firebase Device Streaming, Firebase Crashlytics, Play Vitals data, and Gemini in Android Studio.

## Admin controls

As an admin, you have the ability to control the Cloud services available to users in your organization. For some Cloud services, this can be done through the[Google Admin Console](https://support.google.com/a/answer/55955?ref_topic=2413312&sjid=9410998059586788964-EU):

- [Google Cloud](https://support.google.com/a/answer/9197205?sjid=15762865756081758884-EU): If disabled, it would prevent developers in your organization from using services such as Firebase Device Streaming, Firebase Crashlytics, or Gemini Code Assist.

Additionally, you can limit access to Cloud services through permissions. For example, you can limit which developers can access Play Vitals data through[developer account permissions](https://support.google.com/googleplay/android-developer/answer/9844686). Similarly, you can also configure[Google Cloud permissions](https://cloud.google.com/iam/docs/understanding-roles)to limit access to Cloud services and data in Google Cloud and Firebase projects.

## Work account limitations

If you are using Android Studio with a work account, your organization's admin determines what Cloud services and permissions you have access to. Contact your admin to request access to Cloud services.

## Service permissions

When you enable specific cloud service integrations within Android Studio, certain permissions are granted to the IDE to deliver new functionality.

The following table describes the permissions that Android Studio will have when specific cloud services are enabled.

|        Cloud service integration         |                                       Permissions                                       |
|------------------------------------------|-----------------------------------------------------------------------------------------|
| Android Vitals (Google Play)             | Access metrics and data about your apps in your Google Play Developer account.          |
| Gemini in Android Studio                 | Manage your Google Cloud data. Submit data to Google for AI-based developer assistance. |
| Firebase Device Streaming \& Crashlytics | Manage your Google Cloud data. Manage all your Firebase data and settings.              |
| Backup \& Sync                           | Manage Android Studio configuration data in your Google Drive.                          |