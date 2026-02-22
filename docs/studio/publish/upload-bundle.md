---
title: https://developer.android.com/studio/publish/upload-bundle
url: https://developer.android.com/studio/publish/upload-bundle
source: md.txt
---

# Upload your app to the Play Console

After you[sign the release version of your app](https://developer.android.com/studio/publish/app-signing#sign-apk), the next step is to upload it to Google Play to inspect, test, and publish your app. Before you get started, you must meet the following requirements:

- If you haven't already done so,[enroll in Play App Signing](https://developer.android.com/studio/publish/app-signing#enroll), which is the mandatory way to upload and sign all new apps since August 2021.

- Ensure that your app meets Google Play's size requirements. Google Play supports a cumulative total download size of 4 GB. This size includes all modules and install-time asset packs. To learn more, read[Google Play maximum size limits](https://support.google.com/googleplay/android-developer/answer/9859372#size_limits).

After you've met the preceding requirements,[upload your app to the Play Console](https://support.google.com/googleplay/android-developer/answer/7159011).

This page also describes how you can test and update your app bundle after it's been uploaded.

## Inspect APKs using Latest releases and bundles

If you upload your app as an Android App Bundle, the Play Console automatically generates split APKs and multi-APKs for all device configurations your app supports. In the Play Console, you can use the "Latest bundles" section in the "Latest releases and bundles" page to see all APK artifacts that Google Play generates, inspect data such as supported devices and APK size savings, and download generated APKs to deploy and test locally.

To see more details about your app bundle, see the Play Console help topic

[Inspect app versions with Latest releases and bundles](https://support.google.com/googleplay/android-developer/answer/9006925).

## Test your app internally

There are several ways to share your app internally for testing:

- Upload and distribute your app internally using[Firebase App Distribution](https://firebase.com/docs/app-distribution).
- Upload and distribute your app internally using[Play Console's internal app sharing tool](https://play.google.com/console/internal-app-sharing).

Each of these offers slightly different benefits, so use the one that works best for your team.

- Firebase app distribution lets you deploy any kind of build and distribute it to a list of users. This can be a good way of distributing builds from a continuous integration system so that testers can access specific builds for testing.

- Play console internal track is faster to deploy compared to the alpha or beta tracks and gives you access to services such as Subscriptions, In-App purchases, and ads. This also goes through Play Console signing and shrinking so is the closest to what is distributed to end users through the play store. It is possible to defer the Play Store review until later to avoid having to wait for review to complete. However, the review is required before you can fully distribute your app to end-users through the Play Store.

## Update your app bundle

To update your app after you upload it to the Play Console, you need to increase the version code included in the base module, then build and upload a new app bundle. Google Play then generates updated APKs with new version codes and serves them to users as needed.