---
title: https://developer.android.com/identity/app-set-id
url: https://developer.android.com/identity/app-set-id
source: md.txt
---

For use cases such as analytics or fraud prevention on a given device, you might
need to correlate usage or actions across a set of apps owned by your
organization. [Google Play services](https://developers.google.com/android)
offers a privacy-friendly option called [*app set ID*](https://developers.google.com/android/reference/com/google/android/gms/appset/AppSetIdInfo).

## App set ID scope

The app set ID can have one of the following defined scopes. To determine which
scope a particular ID is associated with, call
[`getScope()`](https://developers.google.com/android/reference/com/google/android/gms/appset/AppSetIdInfo#getScope()).

> [!CAUTION]
> **Caution:** When Google Play services updates from a version that only supports app scope to a version that supports developer scope, the app set ID's value is reset automatically, without any developer action. See [other reasons developers
> shouldn't rely on a cached value of the app set ID](https://developer.android.com/identity/app-set-id#dont-rely-on-cached-value).

### Google Play developer scope

> [!NOTE]
> **Note:** The app set SDK attempts to return app set IDs that have the developer scope without any additional developer action, unless the app satisfies the conditions for app scope, described in the App scope section.

For apps that are installed by the Google Play store, the app set ID API returns
an ID scoped to the set of apps published under the same Google Play developer
account.

For example, suppose you publish two apps under your Google Play developer
account and both apps are installed on the same device through the Google Play
store. The apps share the same app set ID on that device. The ID is the same
even if the apps are signed by different keys.

### App scope

Under any of the following conditions, the app set ID SDK returns an ID unique
to the calling app itself on a given device:

- The app is installed by an installer other than the Google Play store.
- Google Play services is unable to determine an app's Google Play developer account.
- The app is installed on a device without Google Play services.

## Don't rely on a cached value of app set ID

Under any of the following conditions, the app set ID for a given set of Google
Play store-installed apps on a device can be reset:

- The app set ID API hasn't been accessed by the groups of apps that share the same ID value for over 13 months.
- The last app from a given set of apps is uninstalled from the device.
- The user performs a factory reset of the device.

Your app must use the SDK to retrieve the ID value every time it's needed.

## Add the app set ID SDK to your app

The following snippet shows an example `build.gradle` file that uses the app set
ID library:

    dependencies {
        implementation 'com.google.android.gms:play-services-appset:16.1.0'
    }

The following sample snippet demonstrates how you can retrieve the app set ID
asynchronously using the [Tasks API](https://developers.google.com/android/guides/tasks) in Google Play
services:

### Kotlin

    val client = AppSet.getClient(applicationContext) as AppSetIdClient
    val task: Task<AppSetIdInfo> = client.appSetIdInfo as Task<AppSetIdInfo>

    task.addOnSuccessListener({
        // Determine current scope of app set ID.
        val scope: Int = it.scope

        // Read app set ID value, which uses version 4 of the
        // universally unique identifier (UUID) format.
        val id: String = it.id
    })

### Java

    Context context = getApplicationContext();
    AppSetIdClient client = AppSet.getClient(context);
    Task<AppSetIdInfo> task = client.getAppSetIdInfo();

    task.addOnSuccessListener(new OnSuccessListener<AppSetIdInfo>() {
        @Override
        public void onSuccess(AppSetIdInfo info) {
            // Determine current scope of app set ID.
            int scope = info.getScope();

          // Read app set ID value, which uses version 4 of the
          // universally unique identifier (UUID) format.
            String id = info.getId();
        }
    });

For more information about the UUID format, see [Universally unique
identifier](https://en.wikipedia.org/wiki/Universally_unique_identifier).