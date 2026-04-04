---
title: Configure manifest files  |  Android for Cars  |  Android Developers
url: https://developer.android.com/training/cars/media/configure-manifest
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android for Cars](https://developer.android.com/training/cars)

# Configure manifest files Stay organized with collections Save and categorize content based on your preferences.



.
keywords\_public: Android Auto, Android Automotive OS, AAOS, Manifest, Media Browser Service, App Icons, Car UI, Manifest Configuration, Media App, Car Development

Configure your app's manifest files to integrate with Android Auto and Android
Automotive OS (AAOS). To enable discovery and connection by these platforms,
declare your media browser service in the manifest. Specify the required app
icons, including a launcher icon for an attribution
icon for use by system UI components such as media controls.

To learn more about manifest files, see [App manifest overview](/guide/topics/manifest/manifest-intro).

## Declare your media browser service

Android Auto and AAOS connect to your app through your media browser service to
browse media items. Declare your media browser service in your manifest to let
Android Auto and AAOS discover the service and connect to your app.

This code snippet shows how to declare your media browser service in your
manifest. The next section of this guide, [Create a media browser service](/training/cars/media/create-media-browser),
details the process of implementing the service.

```
<application>
    ...
    <service android:name=".MyMediaBrowserService"
             android:exported="true">
        <intent-filter>
            <action android:name="android.media.browse.MediaBrowserService"/>
        </intent-filter>
    </service>
    ...
</application>
```

**Caution:** You might see a lint warning because the service is exported, but
doesn't set the [`android:permission`](/guide/topics/manifest/service-element#prmsn) attribute. It's generally safe to
ignore this warning because you can [Add package validation](/training/cars/media/create-media-browser/content-hierarchy#package-validation), which provides
more control over which host apps can connect to your app.

## Specify app icons

To represent your app in the system UI, specify the app icons that Android Auto
and AAOS should use. These two icons are required:

* [Define the launcher icon](#launcher-icon)
* [Define the attribution icon](#attribution-icon)

**Design guidelines:**
[Branding elements](/design/ui/cars/guides/app-cuj/branding-elements).

### Define the launcher icon

The launcher icon represents your app in the system UI, such as on the launcher
and in the tray of icons.

By default, the [`android:icon`](/guide/topics/manifest/application-element#icon) attribute of your app's
[`<application>`](/guide/topics/manifest/application-element) element is used as the launcher icon:

```
<application
    ...
    android:icon="@mipmap/ic_launcher"
>
```

To use a different icon, set the `android:icon` attribute of your media browser
service's [`<service>`](/guide/topics/manifest/service-element) element:

```
<application>
    ...
    <service
        ...
        android:icon="@mipmap/ic_car_launcher"/>
</application>
```

### Define the attribution icon

The attribution icon is used in places where media content takes precedence,
such as on media cards. Consider reusing the small icon used for notifications.
This icon must be monochrome. We strongly recommend using a vector asset to
avoid a blurry icon.

![Attribution icon on media card](/static/images/training/cars/attribution-icon.png)

**Figure 1.** Attribution icon on media card.

You can specify an icon that is used to represent your app using this manifest
declaration:

```
<application>
    ...
    <meta-data
        android:name="androidx.car.app.TintableAttributionIcon"
        android:resource="@drawable/ic_status_icon" />
    ...
</application>
```

## Specify your app's label

By default, the value of the [`android:label`](/guide/topics/manifest/application-element#label) attribute of your app's
`<application>` element is used as the display name for your app on the car
screen.

To use a different display name – or if your app has multiple media browser
services – set the `android:label` attribute of the media browser service's
`<service>` element.

## Specify your app's accent color

Your app's accent color is used by Android Auto and AAOS to style playback
controls and other UI elements.

By default, the accent color is pulled from the [`colorAccent`](/reference/android/R.attr#colorAccent) item of the
[`android:theme`](/guide/topics/manifest/application-element#theme) style resource of your app's `<application>` element.

To use a different accent color for your in-car experience, include a
[`<meta-data>`](/guide/topics/manifest/meta-data-element) element for a different style resource containing a
`colorAccent` item:

```
<application>
    ...
    <meta-data
        android:name="com.google.android.gms.car.application.theme"
        android:resource="@style/THEME_NAME"/>
    ...
</application>
```

## Platform-specific configuration

In addition to the configuration detailed on this page, see the following
sections for platform-specific requirements:

* [Add support for Android Auto to your media app](/training/cars/media/auto#manifest-car-app)
* [Add support for Android Automotive OS to your media app](/training/cars/media/automotive-os#automotive-module)