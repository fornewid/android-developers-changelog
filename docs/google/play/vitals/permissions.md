---
title: https://developer.android.com/google/play/vitals/permissions
url: https://developer.android.com/google/play/vitals/permissions
source: md.txt
---

Most apps require that users grant them certain
[app permissions](https://developer.android.com/guide/topics/permissions/overview) in order to function
properly. However, in some cases, users might not grant the permissions:

- They think the permission isn't needed for the app's core functionality.
- They don't use the functionality associated with the permission.
- They are concerned about the permission's impacting device performance.
- They're simply uncomfortable, for example due to sensitivities regarding privacy.

> [!NOTE]
> **Note:** For information on how to diagnose and resolve this issue, see [Permission Denials](https://developer.android.com/topic/performance/issues/permissions).

## Use Android vitals to gauge user perceptions

Android vitals can help you gauge your users' privacy preferences and engagement
by informing you about the percentage of permission denials your app
is receiving. Via the Play Console, Android vitals shows the percentage
of daily permission sessions during which users denied permissions for your app.

A *daily permission session* refers to a day during which your app requested
at least one permission from a user. When a given user has to make multiple
decisions for the same permission, only the final decision at the end of a
session is recorded.

Android vitals shows you users' decisions at the permission-group
level. Android vitals also provides benchmarks to help compare where your app
stands with respect to other top apps in the same Play store category.
For information on how Google Play collects Android vitals data, see the
[Play Console documentation](https://support.google.com/googleplay/android-developer/answer/7385505).