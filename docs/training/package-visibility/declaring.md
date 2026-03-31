---
title: Declare package visibility needs  |  App architecture  |  Android Developers
url: https://developer.android.com/training/package-visibility/declaring
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App architecture](https://developer.android.com/topic/architecture/intro)

# Declare package visibility needs Stay organized with collections Save and categorize content based on your preferences.




As you create your app, it's important to consider the other apps on the device
that your app needs to interact with. If your app targets
Android 11 (API level 30) or higher, the system makes [some apps visible to your
app automatically](/training/package-visibility/automatic), but it filters out
other apps by default. This guide describes how to make those other apps visible
to your app.

If your app targets Android 11 or higher and needs to interact
with apps other than the ones that are visible automatically, add the
[`<queries>`](/guide/topics/manifest/queries-element) element in your app's
manifest file. Within the `<queries>` element, specify the other apps [by
package name](#package-name), [by intent signature](#intent-filter-signature),
or [by provider authority](#provider-authority), as described in the following
sections.

## Specific package names

If you know the specific apps that you want to query or interact with, such as
apps that integrate with your app or apps whose services you use, include their
package names in a set of [`<package>`](/guide/topics/manifest/queries-element)
elements inside the `<queries>` element:

```
<manifest package="com.example.game">
    <queries>
        <package android:name="com.example.store" />
        <package android:name="com.example.services" />
    </queries>
    ...
</manifest>
```

**Note:** If you declare a `<package>` element in your app's manifest, then the app
associated with that package name appears in the results of any query to
`PackageManager` that matches a component from that app.

### Communicate with a host app in a library

If you develop an Android library, you can declare your package visibility needs
by adding a `<queries>` element in your [AAR manifest
file](/studio/projects/android-library). This `<queries>` element has the same
functionality as the element that apps can declare in their own manifests.

If your library involves communication with a host app, such as using a [bound
service](/guide/components/bound-services), include a `<package>` element that
specifies the host app's package name:

```
<!-- Place inside the <queries> element. -->
<package android:name=PACKAGE_NAME />
```

By including this declaration, you can check if the host app is installed and
interact with it, such as by calling
[`bindService()`](/reference/android/content/Context#bindService(android.content.Intent,%20int,%20java.util.concurrent.Executor,%20android.content.ServiceConnection)).
The calling app that uses your library [automatically becomes
visible](/training/package-visibility/automatic) to the host app as a result of
this interaction.

## Packages that match an intent filter signature

Your app might need to query or interact with a set of apps that serve a
particular purpose, but you might not know the specific package names to
include. In this situation, you can list
[intent filter signatures](/training/basics/intents/filters) in your
`<queries>` element. Your app can then discover apps that have
matching
[`<intent-filter>`](/guide/topics/manifest/intent-filter-element)
elements.

The following code example shows an `<intent>` element that would allow the app
to see other installed apps that support JPEG image sharing:

```
<manifest package="com.example.game">
    <queries>
        <intent>
            <action android:name="android.intent.action.SEND" />
            <data android:mimeType="image/jpeg" />
        </intent>
    </queries>
    ...
</manifest>
```

The `<intent>` element has a few restrictions:

* You must include exactly one `<action>` element.
* You cannot use the `path`, `pathPrefix`, `pathPattern`, or `port` attributes
  in a `<data>` element. The system behaves as if you set each attribute's value
  to the generic wildcard character (`*`).
* You cannot use the `mimeGroup` attribute of a `<data>` element.
* Within the `<data>` elements of a single `<intent>` element, you can use each
  of the following attributes at most once:

  + `mimeType`
  + `scheme`
  + `host`

  You can distribute these attributes across multiple `<data>` elements or use
  them in a single `<data>` element.

The `<intent>` element supports the generic wildcard character (`*`) as the
value for a few attributes:

* The `name` attribute of the `<action>` element.
* The subtype of the `mimeType` attribute of a `<data>` element (`image/*`).
* The type and subtype of the `mimeType` attribute of a `<data>` element
  (`*/*`).
* The `scheme` attribute of a `<data>` element.
* The `host` attribute of a `<data>` element.

Unless otherwise specified in the previous list, the system doesn't support a
mix of text and wildcard characters, such as `prefix*`.

## Packages that use a specific authority

If you need to query a [content
provider](/guide/topics/providers/content-provider-basics#ContentURIs) but
don't know the specific package names, you can declare the provider authority
in a [`<provider>`](/guide/topics/manifest/provider-element) element, as shown
in the following snippet:

```
<manifest package="com.example.suite.enterprise">
    <queries>
        <provider android:authorities="com.example.settings.files" />
    </queries>
    ...
</manifest>
```

**Note:** If your `<queries>` element includes a `<provider>` element, you might see
an editor warning in Android Studio related to the `<provider>` element. As long
as you're using the latest dot release of the Android Gradle plugin, your
build is unaffected, so you can disregard the warning. Learn more in the blog
post about [Preparing your Gradle build for package visibility in
Android 11](https://android-developers.googleblog.com/2020/07/preparing-your-build-for-package-visibility-in-android-11.html).

You can declare provider authorities in a single `<queries>` element. Within the
`<queries>` element, you can declare one or more `<provider>` elements. A
`<provider>` element can include a single provider authority or a
semicolon-delimited list of provider authorities.

## All apps (not recommended)

In rare cases, your app might need to query or interact with all installed apps
on a device, independent of the components they contain. To allow your app to
see all other installed apps, the system provides the
[`QUERY_ALL_PACKAGES`](/reference/android/Manifest.permission#QUERY_ALL_PACKAGES)
permission.

Some examples of use cases where the
`QUERY_ALL_PACKAGES` permission is appropriate to include are:

* Accessibility apps
* Browsers
* Device management apps
* Security apps
* Antivirus apps

However, it's usually possible to fulfill your app's use
cases by interacting with the set of apps that are [visible automatically](/training/package-visibility/automatic) and by declaring the other apps
that your app needs to access in your manifest file. To
respect user privacy, your app should request the smallest amount of package
visibility necessary in order for your app to work.

This [policy update from Google
Play](https://support.google.com/googleplay/android-developer/answer/10158779)
provides guidelines for apps that need the `QUERY_ALL_PACKAGES` permission.

[Previous

arrow\_back

Know which packages are visible automatically](/training/package-visibility/automatic)

[Next

Fulfill common use cases

arrow\_forward](/training/package-visibility/use-cases)