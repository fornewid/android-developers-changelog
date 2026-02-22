---
title: https://developer.android.com/training/permissions/restrict-interactions
url: https://developer.android.com/training/permissions/restrict-interactions
source: md.txt
---

# Restrict interactions with other apps

Permissions aren't only for requesting system functionality. You can also restrict how other apps can interact with your app's components.

This guide explains how to check the set of permissions that another app has declared. The guide also explains how you can configure activities, services, content providers, and broadcast receivers to restrict how other apps can interact with your app.
| **Note:** When restricting interactions to only apps provided by one developer, such as to secure interprocess communications, we recommend using custom signature permissions. For more info, see[Define a custom app permission](https://developer.android.com/guide/topics/permissions/defining).

## Check another app's permissions

To view the set of permissions that another app declares, use a device or emulator to complete the following steps:

1. Open an app's**App info**screen.
2. Select**Permissions** . The**App permissions**screen loads.

   This screen shows a set of permission groups. The system organizes the set of permissions that an app has declared into these groups.

There are a number of other useful ways to check permissions:

- To check a permission during a call into a service, pass a permission string into[`Context.checkCallingPermission()`](https://developer.android.com/reference/android/content/Context#checkCallingPermission(java.lang.String)). This method returns an integer that indicates whether that permission has been granted to the current calling process. Note that this can only be used when you are executing a call coming in from another process, usually through an IDL interface published from a service or in some other way given to another process.
- To check whether another process has been granted a particular permission, pass the process ID (PID) into[`Context.checkPermission()`](https://developer.android.com/reference/android/content/Context#checkPermission(java.lang.String,%20int,%20int)).
- To check whether another package has been granted a particular permission, pass the package name into[`PackageManager.checkPermission()`](https://developer.android.com/reference/android/content/pm/PackageManager#checkPermission(java.lang.String,%20java.lang.String)).

## Restrict interactions with your app's activities

In the manifest, use the[`<activity>`](https://developer.android.com/guide/topics/manifest/activity-element)tag's`android:permission`attribute to restrict which other apps can start that[`Activity`](https://developer.android.com/reference/android/app/Activity). The permission is checked during[`Context.startActivity()`](https://developer.android.com/reference/android/content/Context#startActivity(android.content.Intent))and[`Activity.startActivityForResult()`](https://developer.android.com/reference/android/app/Activity#startActivityForResult(android.content.Intent,%20int)). If the caller doesn't have the required permission, then a[`SecurityException`](https://developer.android.com/reference/java/lang/SecurityException)occurs.

## Restrict interactions with your app's services

In the manifest, use the[`<service>`](https://developer.android.com/guide/topics/manifest/service-element)tag's`android:permission`attribute to restrict which other apps can start or bind to the associated[`Service`](https://developer.android.com/reference/android/app/Service). The permission is checked during[`Context.startService()`](https://developer.android.com/reference/android/content/Context#startService(android.content.Intent)),[`Context.stopService()`](https://developer.android.com/reference/android/content/Context#stopService(android.content.Intent)), and[`Context.bindService()`](https://developer.android.com/reference/android/content/Context#bindService(android.content.Intent,%20android.content.ServiceConnection,%20int)). If the caller doesn't have the required permission, then a`SecurityException`occurs.

## Restrict interactions with your app's content providers

In the manifest, use the[`<provider>`](https://developer.android.com/guide/topics/manifest/provider-element)tag's`android:permission`attribute to restrict which other apps can access the data in a[`ContentProvider`](https://developer.android.com/reference/android/content/ContentProvider). (Content providers have an important additional security facility available to them called[URI permissions](https://developer.android.com/training/permissions/restrict-interactions#uri), which is described in the following section.) Unlike for the other components, there are two separate permission attributes you can set for content providers:[`android:readPermission`](https://developer.android.com/guide/topics/manifest/provider-element#rprmsn)restricts which other apps can read from the provider, and[`android:writePermission`](https://developer.android.com/guide/topics/manifest/provider-element#wprmsn)restricts which other apps can write to it. Note that if a provider is protected with both a read and write permission, holding only the write permission doesn't permit an app to read from a provider.

The permissions are checked when the provider is first retrieved and when an app performs operations on the provider. If the requesting app doesn't have either permission, a`SecurityException`occurs. Using[`ContentResolver.query()`](https://developer.android.com/reference/android/content/ContentResolver#query(android.net.Uri,%20java.lang.String%5B%5D,%20android.os.Bundle,%20android.os.CancellationSignal))requires the read permission; using[`ContentResolver.insert()`](https://developer.android.com/reference/android/content/ContentResolver#insert(android.net.Uri,%20android.content.ContentValues)),[`ContentResolver.update()`](https://developer.android.com/reference/android/content/ContentResolver#update(android.net.Uri,%20android.content.ContentValues,%20java.lang.String,%20java.lang.String%5B%5D)), or[`ContentResolver.delete()`](https://developer.android.com/reference/android/content/ContentResolver#delete(android.net.Uri,%20java.lang.String,%20java.lang.String%5B%5D))requires the write permission. In all of these cases, not holding the required permission results in a`SecurityException`.

### Give access on a per-URI basis

The system provides you with additional fine-grained control over how other apps can access your app's content providers. In particular, your content provider can protect itself with read and write permissions while still allowing its direct clients to share specific URIs with other apps. To declare your app's support for this model, use the[`android:grantUriPermissions`](https://developer.android.com/guide/topics/manifest/provider-element#gprmsn)attribute or the[`<grant-uri-permission>`](https://developer.android.com/guide/topics/manifest/grant-uri-permission-element)element.

You can also grant permissions on a per-URI basis. When starting an activity or returning a result to an activity, set the[`Intent.FLAG_GRANT_READ_URI_PERMISSION`](https://developer.android.com/reference/android/content/Intent#FLAG_GRANT_READ_URI_PERMISSION)intent flag, the[`Intent.FLAG_GRANT_WRITE_URI_PERMISSION`](https://developer.android.com/reference/android/content/Intent#FLAG_GRANT_WRITE_URI_PERMISSION)intent flag, or both flags. This gives other apps read, write, or read and write permissions, respectively, for the data URI that's included in the intent. Other apps gain these permissions for the specific URI regardless of whether they have permission to access data in the content provider more generally.

For example, suppose that a user is using your app to view an email with an image attachment. Other apps shouldn't be able to access the email contents in general, but they might be interested in viewing the image. Your app can use an intent and the`Intent.FLAG_GRANT_READ_URI_PERMISSION`intent flag to let an image-viewing app see the image.

Another consideration is[app visibility](https://developer.android.com/training/package-visibility). If your app targets Android 11 (API level 30) or higher, the system makes some apps visible to your app automatically and hides other apps by default. If your app has a content provider and has granted URI permissions to another app, your app is[automatically visible](https://developer.android.com/training/package-visibility/automatic)to that other app.

For more information, view the reference material for the[`grantUriPermission()`](https://developer.android.com/reference/android/content/Context#grantUriPermission(java.lang.String,%20android.net.Uri,%20int)),[`revokeUriPermission()`](https://developer.android.com/reference/android/content/Context#revokeUriPermission(android.net.Uri,%20int)), and[`checkUriPermission()`](https://developer.android.com/reference/android/content/Context#checkUriPermission(android.net.Uri,%20int,%20int,%20int))methods.

## Restrict interactions with your app's broadcast receivers

Use the[`<receiver>`](https://developer.android.com/guide/topics/manifest/receiver-element)tag's`android:permission`attribute to restrict which other apps can send broadcasts to the associated[`BroadcastReceiver`](https://developer.android.com/reference/android/content/BroadcastReceiver). The system checks the permission*after* [`Context.sendBroadcast()`](https://developer.android.com/reference/android/content/Context#sendBroadcast(android.content.Intent))returns, as the system tries to deliver the submitted broadcast to the given receiver. This means that a permission failure doesn't result in an exception being thrown back to the caller---it just doesn't deliver the[`Intent`](https://developer.android.com/reference/android/content/Intent).

You can also configure permissions programmatically:

- **To control which other apps can broadcast to a programmatically registered receiver:** Supply a permission to[`Context.registerReceiver()`](https://developer.android.com/reference/android/content/Context#registerReceiver(android.content.BroadcastReceiver,%20android.content.IntentFilter,%20java.lang.String,%20android.os.Handler)).
- **To restrict which broadcast receivers can receive a broadcast:** Supply a permission when calling[`Context.sendBroadcast()`](https://developer.android.com/reference/android/content/Context#sendBroadcast(android.content.Intent,%20java.lang.String)).

Note that both a receiver and a broadcaster can require a permission. When this happens, both permission checks must pass for the intent to be delivered to the associated target. For more information, see[Restricting broadcasts with permissions](https://developer.android.com/guide/components/broadcasts#restrict-broadcasts-permissions).