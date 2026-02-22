---
title: https://developer.android.com/training/permissions/usage-notes
url: https://developer.android.com/training/permissions/usage-notes
source: md.txt
---

Permission requests protect sensitive information available from a device and
should only be used when access to information is necessary for the
functioning of your app. This document provides tips on ways you might be
able to achieve the same (or better) functionality without requiring access
to such information; it is not an exhaustive discussion of how permissions
work in the Android operating system.


For a more general look at Android permissions, please see [Permissions overview](https://developer.android.com/guide/topics/permissions/requesting). For details on how to work with permissions in your code,
see [Requesting app permissions](https://developer.android.com/training/permissions/requesting).

## Permissions in Android 6.0+


In Android 6.0 (API level 23) and higher, apps can request permissions from
the user at runtime, rather than prior to installation. This allows apps to
request permissions when the app actually requires the services or data
protected by the services. While this doesn't (necessarily) change overall app
behavior, it does create a few changes relevant to the way sensitive user data
is handled:

### Increased situational context

Users are prompted at runtime, in the context of your app, for permission to
access the functionality covered by those permission groups. Users are more
sensitive to the context in which the permission is requested, and if there's a mismatch
between what you are requesting and the purpose of your app, it's even
more important to provide detailed explanation to the user as to why you're
requesting the permission. Whenever possible, you should provide an
explanation of your request both at the time of the request and in a
follow-up dialog if the user denies the request.

To increase the likelihood of a permission request being accepted, only prompt
when a specific feature is required. For instance, only prompt for microphone
access when a user clicks on the microphone button. Users are more likely to
allow a permission that they are expecting.
| **Note:** Don't overburden the user by requesting every permission at app startup. Be courteous of the user and only request permissions when they need access to a specific feature.

### Greater flexibility in granting permissions

Users can deny access to individual permissions at the time they're requested
*and* in settings, but they may still be surprised when functionality is
broken as a result. It's a good idea to monitor how many users are denying
permissions (e.g. using Google Analytics) so that you can either refactor
your app to avoid depending on that permission or provide a better
explanation of why you need the permission for your app to work properly. You
should also make sure that your app handles exceptions when users
deny permission requests or toggle off permissions in settings.

### Increased transactional burden

Users are asked to grant access for permission groups individually and not as a set. This
makes it extremely important to minimize the number of permissions you're
requesting. This increases the user-burden for granting permissions and therefore
increases the probability that at least one of the requests will be denied.

## Permissions that require becoming a default handler

Some apps depend on access to sensitive user information related to call logs
and SMS messages. If you want to request the permissions specific to call logs
and SMS messages and publish your app to the Play Store, you must prompt the
user to set your app as the *default handler* for a core system function before
requesting these runtime permissions.

For more information on default handlers, including guidance on showing a
default handler prompt to users, [see the guide on permissions used only in
default handlers](https://developer.android.com/guide/topics/permissions/default-handlers).

[](https://developer.android.com/training/permissions/know_the_libraries_you're_working_with)

## Know the libraries you're working with


Sometimes permissions are required by the libraries you use in your app. For
example, ads and analytics libraries may require access to the
`LOCATION` permissions group to implement the required
functionality. But from the user's point of view, the permission request comes
from your app, not the library.


Just as users select apps that use fewer permissions for the same
functionality, developers should review their libraries and select
third-party SDKs that aren't using unnecessary permissions. For example, if
you're using a library that provides location functionality, make sure you
aren't requesting the `FINE_LOCATION` permission unless you're
using location-based targeting functionality.

## Limit background access to location

When your app is running in the background, [access to
location](https://developer.android.com/training/location/background) should be critical to the app's core
functionality and show a clear benefit to users.

## Test for both permissions models


In Android 6.0 (API level 23) and higher, users grant and revoke app
permissions at run time, instead of doing so when they install the app. As a
result, you'll have to test your app under a wider range of conditions. Prior
to Android 6.0, you could reasonably assume that if your app is running at
all, it has all the permissions it declares in the app manifest. Now, the user
can turn permissions on or off for *any* app, regardless of API level.
You should test to ensure your app functions correctly across various
permission scenarios.


The following tips will help you find permissions-related code problems
on devices running API level 23 or higher:

- Identify your app's current permissions and the related code paths.
- Test user flows across permission-protected services and data.
- Test with various combinations of granted or revoked permissions. For example, a camera app might list [CAMERA](https://developer.android.com/reference/android/Manifest.permission#CAMERA), [READ_CONTACTS](https://developer.android.com/reference/android/Manifest.permission#READ_CONTACTS), and [ACCESS_FINE_LOCATION](https://developer.android.com/reference/android/Manifest.permission#ACCESS_FINE_LOCATION) in its manifest. You should test the app with each of these permissions turned on and off, to make sure the app can handle all permission configurations gracefully.
- Use the [adb](https://developer.android.com/tools/help/adb) tool to manage permissions from the command line:
  - List permissions and status by group:  

    ```
    $ adb shell pm list permissions -d -g
    ```
  - Grant or revoke one or more permissions:  

    ```
    $ adb shell pm [grant|revoke] <permission-name> ...
    ```
- Analyze your app for services that use permissions.

## Additional resources

- [Material Design guidelines for Android permissions](https://material.io/design/platform-guidance/android-permissions.html#usage)
- [Android Marshmallow 6.0: Asking For Permission](https://www.youtube.com/watch?v=iZqDdvhTZj0): This video explains the Android runtime permission model and the right way to ask users for permissions.
- [Explain why the app needs permissions](https://developer.android.com/training/permissions/requesting#explain)
- [Best practices for unique identifiers](https://developer.android.com/training/articles/user-data-ids)