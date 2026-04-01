---
title: https://developer.android.com/google/play/billing/deprecation-faq
url: https://developer.android.com/google/play/billing/deprecation-faq
source: md.txt
---

# Google Play Billing Library version deprecation

As announced at Google I/O in 2019 and the[Meet Google Play Billing Library Version 3](https://android-developers.googleblog.com/2020/06/meet-google-play-billing-library.html "Play Billing Library Version 3 Blog")blog post, all versions of Play Billing Library will follow a two year deprecation cycle.

This topic answers common questions regarding Billing Library version deprecation and migrating to newer versions.

## Support timeline For different versions

| Version (including minor versions) | Last date version can be used to release new apps or updates to existing apps | Extension request can be made up to date |
|------------------------------------|-------------------------------------------------------------------------------|------------------------------------------|
| 5                                  | Aug-31-2024                                                                   | Nov-1-2024                               |
| 6                                  | Aug-31-2025                                                                   | Nov-1-2025                               |
| 7                                  | Aug-31-2026                                                                   | Nov-1-2026                               |
| 8                                  | Aug-31-2027                                                                   | Nov-1-2027                               |

**How can I find which APK or App Bundle is triggering a deprecation warning?**
:   Review your project's imported dependencies (for example, those found in your project's`build.gradle`file). To be compliant, apps must import a supported version as indicated in the table. Note that Billing dependencies would be found only in APKs that require the`com.android.vending.BILLING`permission.

**An APK or App Bundle that I no longer maintain is using a deprecated version of the Play Billing Library. Do I need to update?**
:   We strongly recommend updating all APKs to the latest version of the Play Billing Library. However, if an APK is no longer maintained, then no action is required for the APK at this time. This deprecation prevents only new apps and updates from using older versions of the Play Billing Library. Existing apps that use a deprecated version of the library will continue to function as expected. Please ensure that all actively maintained APKs are updated.

**How to fix APK or App Bundle updated to latest Play Billing Library but still triggering deprecation warning?**
:   Make sure your`AndroidManifest.xml`contains an entry with name`com.google.android.play.billingclient.version`. If the entry isn't present, check your[manifest merge settings](https://developer.android.com/studio/build/manage-manifests#merge-manifests)to see if the manifest attribute is being dropped during manifest merging.

**How can I upgrade from an earlier version of Play Billing Library?**

:   Update the dependency in your release to use a supported version as indicated in the table. To see what changed between releases, read the[release notes](https://developer.android.com/google/play/billing/release-notes).

    In addition, we have an in-depth guide for migrating[to PBL 8](https://developer.android.com/google/play/billing/migrate-gpblv8).

**Where can I find the extension form to continue distributing to all Google Play users until 1 November?**

If your app is still using an out of date Play Billing Library version, you'll receive a warning and an inbox message in Play Console. The extension form is available through the details page of the warning or issue on the[Policy status](https://play.google.com/console/developers/app/policy-center "Policy Center")page in Play Console.