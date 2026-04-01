---
title: https://developer.android.com/google/play/release-audience-restriction
url: https://developer.android.com/google/play/release-audience-restriction
source: md.txt
---

# Use a release audience restriction to limit your app&#39;s distribution

You can greatly reduce the chances of accidentally distributing a version of your app that isn't ready yet by using a release audience restriction in your app bundle or APK. You can use this to prevent a build from being released to production users through Play Console, or even from being distributed through Play Console at all.

## Release audience restrictions usage

To use a release audience restriction, you must add a`<meta-data>`element to the`<application>`element in your`AndroidManifest.xml`file. This element controls how far the distribution of the build can progress. The`<meta-data>`tag must have its`android:value`attribute set to the empty string, and the`android:name`attribute must be one of the following values:

|                                 Name                                  |                                                                                                                                                                    Effect                                                                                                                                                                     |
|-----------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ` com.google.android.play.largest_release_audience.NONPRODUCTION `    | The app bundle or APK can be uploaded to Play Console and distributed to users through Internal App Sharing or any testing track, including open testing. It**cannot** be included in a release on the Production track. This is intended to prevent accidental release of test versions of apps to production users.                         |
| ` com.google.android.play.largest_release_audience.CLOSED_TESTING `   | The app bundle or APK can be uploaded to Play Console and distributed to users through Internal App Sharing or any closed testing track. It**cannot** be included in a release on the Production or Open Testing tracks. This is intended to prevent accidental release of test versions of apps to a large number of users.                  |
| ` com.google.android.play.largest_release_audience.INTERNAL_TESTING ` | The app bundle or APK can be uploaded to Play Console and distributed to users through Internal App Sharing or the Internal Test Track. It**cannot** be included in a release on the Production, Open Testing, or Closed Testing tracks. This is intended to prevent accidental release of test versions of apps outside your immediate team. |
| ` com.google.android.play.largest_release_audience.STOPSHIP `         | The app bundle or APK cannot be uploaded to or distributed through Play Console. This is intended to prevent releasing development-only versions of apps to any users. For example, a build which has key security features disabled for easier debugging.                                                                                    |

| **Note:** Because the restriction is built into your app bundle or APK, you can only change it by compiling a new build of your app with a new versionCode.

For example, to prevent a build being released to production users, update your`AndroidManifest.xml`file as follows:  

    <manifest ... >
        <application ... >
            ...
            <meta-data
              android:name="com.google.android.play.largest_release_audience.NONPRODUCTION"
              android:value="" />
        </application>
    </manifest>

| **Important:** The`<meta-data>`element must be a direct child of the`<application>`element in order for it to be detected by Google Play. It won't be detected if it is part of an`<activity>`or`<service>`element. If there are multiple restrictions in your application manifest, then the most restrictive will be applied.
| **Tip:** If you have an Android library that adds some optional features for testing or internal debugging, you can add the restriction to the library's manifest. Any build which includes the library will then automatically include the release audience restriction.