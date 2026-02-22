---
title: https://developer.android.com/training/package-visibility
url: https://developer.android.com/training/package-visibility
source: md.txt
---

When an app targets Android 11 (API level 30) or higher and queries for
information about the other apps that are installed on a device, the system
filters this information by default. This filtering behavior means that your app
can't detect all the apps installed on a device, which helps minimize the
potentially sensitive information that your app can access but doesn't need
to fulfill its use cases.

Also, filtered package visibility helps app
stores like Google Play assess the privacy and security that your app provides
for users. For example, Google Play considers the list of installed apps to be
[personal and sensitive user
data](https://support.google.com/googleplay/android-developer/answer/10144311#zippy=%2Cexamples-of-common-violations).

Limited app visibility affects the results returned by methods that give
information about other apps, such as
[`queryIntentActivities()`](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities(android.content.Intent,%20int)),
[`getPackageInfo()`](https://developer.android.com/reference/android/content/pm/PackageManager#getPackageInfo(java.lang.String,%20int)),
and
[`getInstalledApplications()`](https://developer.android.com/reference/android/content/pm/PackageManager#getInstalledApplications(int)).
The limited visibility also affects explicit interactions with other apps, such
as starting another app's service.

Some packages are [visible
automatically](https://developer.android.com/training/package-visibility/automatic). Your app can always
detect these packages in its queries for other installed apps. To view other
packages, [declare your app's need for increased package
visibility](https://developer.android.com/training/package-visibility/declaring) using the
[`<queries>`](https://developer.android.com/guide/topics/manifest/queries-element) element. The [use
cases](https://developer.android.com/training/package-visibility/use-cases) page provides examples of how you
can selectively expand package visibility. The workflows described there allow
you to fulfill common app interaction scenarios while protecting user privacy.

In the rare cases where the `<queries>` element doesn't provide adequate package
visibility, you can use the `QUERY_ALL_PACKAGES` permission. If you publish your
app on Google Play, your app's use of this permission is
[subject to approval](https://support.google.com/googleplay/android-developer/answer/10158779).

The page about
[testing package visibility behavior](https://developer.android.com/training/package-visibility/testing)
offers suggestions for how to test behavior changes based on package visibility
when your app relies on interactions with other apps.

## Additional resources

To learn more about package visibility on Android, view the following materials:

### Blog posts

- [Package visibility in
  Android 11](https://medium.com/androiddevelopers/package-visibility-in-android-11-cc857f221cd9), available on Medium.