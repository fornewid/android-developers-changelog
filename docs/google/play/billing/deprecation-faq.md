---
title: https://developer.android.com/google/play/billing/deprecation-faq
url: https://developer.android.com/google/play/billing/deprecation-faq
source: md.txt
---

All versions of the Google Play Billing Library have a two-year deprecation
cycle. Google announced this deprecation cycle at Google I/O 2019 and in the
[Meet Google Play Billing Library Version 3](https://android-developers.googleblog.com/2020/06/meet-google-play-billing-library.html "Play Billing Library Version 3 Blog") blog post.

This page answers common questions about the Google Play
Billing Library version deprecation and migrating to higher versions.


**Important:** You can now use an agent skill to migrate
to the latest Play Billing Library (PBL) version. Explore the
[PBL migration skill on GitHub](https://github.com/android/skills/tree/main/play/play-billing-library-version-upgrade).

<br />

## Support timeline for different versions

The following table shows the deprecation and extension deadlines for each
Google Play Billing Library version.

| Version | New app and update deadline | Extension deadline |
|---|---|---|
| 5 | August 31, 2024 | November 1, 2024 |
| 6 | August 31, 2025 | November 1, 2025 |
| 7 | August 31, 2026 | November 1, 2026 |
| 8 | August 31, 2027 | November 1, 2027 |
| 9 | August 31, 2028 | November 1, 2028 |

**How do you find which APKs use a deprecated Play Billing Library version?**
:   Check your `build.gradle` file. Apps must use a supported version from the
    table. These dependencies only appear in APKs that require the
    `com.android.vending.BILLING` permission.

**Do you need to update unmaintained APKs?**
:   We recommend updating maintained APKs. Unmaintained APKs don't need updates;
    existing apps still work, but new apps and updates must use supported
    versions.

\*\*How do you fix a deprecation warning if you've already updated your
app to a supported version?\*\*
:   Make sure your `AndroidManifest.xml` file contains
    `com.google.android.play.billingclient.version`. If it's missing,
    check whether [manifest merging](https://developer.android.com/studio/build/manage-manifests#merge-manifests) removes this attribute.

\*\*How do you upgrade from a lower version of the Google Play Billing
Library?\*\*

:   Update the dependency in your release to use a supported version from
    the table. To learn what changed between releases, see the
    [release notes](https://developer.android.com/google/play/billing/release-notes).

    To migrate, see the [migration guide for version 9](https://developer.android.com/google/play/billing/migrate-gpblv9).

\*\*Where do you find the extension form to continue distributing to users
until the extension deadline?\*\*

:   If your app uses an unsupported Google Play Billing Library version, you'll
    receive a warning in the Google Play Console. On the warning's details page
    on the [**Policy status**](https://play.google.com/console/developers/app/policy-center "Policy Center") page,
    open the extension form.