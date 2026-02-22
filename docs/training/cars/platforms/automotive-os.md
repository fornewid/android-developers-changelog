---
title: https://developer.android.com/training/cars/platforms/automotive-os
url: https://developer.android.com/training/cars/platforms/automotive-os
source: md.txt
---

![Android Automotive OS user interface](https://developer.android.com/static/images/training/cars/android-automotive-os.png) **Figure 1**: Android Automotive OS

Android Automotive OS is a version of Android optimized for in-car use that
extends upon the core Android platform. [Cars with Google built-in](https://built-in.google/cars/) run
Android Automotive OS and come with Google apps and services including Google
Play, Google Assistant, and Google Maps.
| **Note:** Android Automotive OS and [Android Auto](https://developer.android.com/training/cars/platforms/android-auto) are not exclusive. That is, a car can run Android Automotive OS and also support Android Auto.

## Learn about Android Automotive OS hardware

To learn more about the minimum hardware specifications for Android Automotive
OS devices, see the *Automotive Requirements* section of the [Android
Compatibility Definition Document (CDD)](https://source.android.com/docs/compatibility/cdd) for the Android version(s) your app
supports.
| **Note:** All vehicles with Google built-in run Android 9 or higher.

### Display cutouts

As with other Android form factors, display cutouts are supported by Android
Automotive OS devices with non-rectangular displays. However, the size and shape
of cutouts found in cars can be quite different than those found in other form
factors. See [Work with window insets and display cutouts](https://developer.android.com/training/cars/parked/automotive-os#insets-and-cutouts) for detailed
guidance.

### Audio

Android Automotive OS devices are generally fixed-volume devices. To learn more
about how this may affect your app, see [Working with fixed-volume devices](https://developer.android.com/media/platform/output#fixed-volume).

## Understand Android Automotive OS software

While Android Automotive OS is based on the same core operating system as used
by other form factors, there are some additional features unique to it that can
impact the way that apps can be developed and used.

### System UI

There are some differences in how these system UI elements function in cars that
you should be aware of.
| **Tip:** The [Android Automotive OS compatibility mode](https://developer.android.com/training/cars/platforms/automotive-os/compatibility-mode) present on some devices addresses many of the implications of these differences.

#### Navigation

Unlike other form factors, there is no requirement for Android Automotive OS
devices to have a hardware or software back affordance. When not run in
compatibility mode, activities implemented by your app should include UI
affordances to enable in-app navigation to meet the [`AN-1`](https://developer.android.com/docs/quality-guidelines/car-app-quality#AN-1) quality
guideline.

#### System bar layout

As with other form factors, Android Automotive OS includes [system bars](https://developer.android.com/design/ui/mobile/guides/foundations/system-bars)
such as status bars and navigation bars. In cars, these bars may be sized and
positioned differently than on other form factors. For example, navigation bars
may be positioned on the left, right, or bottom of the screen. Even in the case
that there is a status bar on top and a navigation bar on the bottom (as is the
case with most phones and tablets), the size of these elements will likely be
much greater in cars.

Additionally, while display cutouts on mobile devices are generally contained
within the bounds of the system bars, this isn't the case in cars.

See [Work with window insets and display cutouts](https://developer.android.com/training/cars/parked/automotive-os#insets-and-cutouts) for detailed
guidance.

#### Immersive mode

Android Automotive OS allows OEMs to control whether or not apps can [show or
hide the system bars to enter and exit immersive mode](https://developer.android.com/develop/ui/views/layout/immersive). By preventing apps
from hiding the system bars, OEMs can ensure that vehicle controls, such as
climate controls, are always accessible on screen.

### User experience restrictions

User experience (UX) restrictions are the capability built into Android
Automotive OS to handle driver distraction considerations. UX restrictions are
responsible for automatically preventing the use of apps that haven't been
optimized for use while driving.
![The activity blocking activity being displayed over an app not marked as
distraction optimized.](https://developer.android.com/static/training/cars/images/activity-blocking-activity.png) **Figure 2**: An app being blocked by UX restrictions

The exact set of rules that determine how and when UX restrictions are active
are determined by vehicle manufacturers. These rules can vary by geography -- for
example, the same vehicle sold in Europe may have different rules than those
sold in the United States.

UX restriction rules can also vary by display within a vehicle. For example,
it is possible for a center display in the driver's line of sight to be
restricted while the vehicle is in motion while a passenger display would
remain unrestricted.

If your app needs to adapt to UX restrictions, reference them directly -- don't
attempt to reverse engineer their implementation. For example, if you assume
that UX restrictions are active when the gear is not Park, you might
unnecessarily restrict an app running on a passenger display.

#### Distraction optimization

By default, activities cannot be run while UX restrictions are
active to limit driver distractions. To indicate to the system that an activity
should continue running while the vehicle is motion, the following `<meta-data>`
element can be added within the corresponding `<activity>` element.  

    <activity ...>
      <meta-data android:name="distractionOptimized" android:value="true">
    </activity>

When developing apps for Android Automotive OS, the only time this metadata
should be present in your manifest is when [declaring the `<activity>` manifest
element for the `CarAppActivity`](https://developer.android.com/training/cars/apps/automotive-os#car-app-activity) of an app built using the Car App Library.
No other activities should be marked as distraction optimized - if one is, your
app will be rejected when submitted to the Google Play Store.

### Accessibility

Accessibility support for Android Automotive OS is not as expansive as on other
form factors. [TalkBack](https://developer.android.com/guide/topics/ui/accessibility/testing#talkback), [Switch Access](https://developer.android.com/guide/topics/ui/accessibility/testing#switch-access), and [Voice Access](https://developer.android.com/guide/topics/ui/accessibility/testing#voice-access) are
not available on Android Automotive OS devices.

Captioning preferences are supported on Android Automotive OS devices. See
[Adopt system caption settings](https://developer.android.com/training/tv/accessibility/system-caption-settings) for integration details.

### Network selection

Android Automotive OS supports [*Per-application network selection* (PANS)](https://source.android.com/docs/automotive/connectivity#configure-a-network),
which allows OEMs to route mobile network traffic to different networks on an
application-by-application basis.

Most apps use only the [default network](https://developer.android.com/develop/connectivity/network-ops/reading-network-state#listening-events) assigned to them and only stand to
benefit from this feature -- for example, the OEM may pay for network traffic
from your app even if the user doesn't have their own data plan. If your app (or
one of its dependencies) relies on networks other than the default, it may not
benefit from preferences set by the OEM. See [Read network state](https://developer.android.com/develop/connectivity/network-ops/reading-network-state#additional-networks) for more
guidance on using networks other than the default.

## System features

You can detect whether a given feature is available using
[`PackageManager::hasSystemFeature`](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String)) and adjust your app's behavior
accordingly.
| **Tip:** You can use the [Device catalog](https://play.google.com/console/about/devicecatalog/) in the Google Play Console to determine which vehicles support any given feature by using the *Form factor* filter with value *Car* combined with the *System feature* filter.

### Hardware features

As with other non-mobile form-factors, the hardware features available in cars
may differ from those found on mobile devices.

#### Screen orientation

Like TVs, cars are fixed orientation devices. Unlike TVs, they come in both
portrait and landscape orientations. To ensure that apps built for Android
Automotive OS can be distributed to all vehicles, apps must ensure that they
have no explicit or implicit feature requirement for either the
`android.hardware.screen.landscape` or `android.hardware.screen.portrait`
features.

#### Network location

Many Android Automotive OS devices don't implement the telephony stack used
to provide network location and thus don't report the
[`android.hardware.location.network`](https://developer.android.com/guide/topics/manifest/uses-feature-element#location-hw-features) system feature. Although network
location may not be available, accessing coarse location is still supported --
see [Coarse location on Android Automotive OS](https://developer.android.com/training/cars/platforms/automotive-os/coarse-location).

### Software features

Some software features that are commonly found on other form factors may not be
supported on Android Automotive OS devices. For example, the following features
are not available on many Android Automotive OS vehicles:

- [App Widgets](https://developer.android.com/develop/ui/views/appwidgets/overview)
  ([`FEATURE_APP_WIDGETS`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_APP_WIDGETS))

- [Picture-in-picture](https://developer.android.com/develop/ui/views/picture-in-picture)
  ([`FEATURE_PICTURE_IN_PICTURE`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_PICTURE_IN_PICTURE))

### Meet Google Play feature requirements

To be distributed to cars through Google Play, apps built for Android Automotive
OS must include a [`<uses-feature>`](https://developer.android.com/guide/topics/manifest/uses-feature-element) element in the
[`AndroidManifest.xml`](https://developer.android.com/guide/topics/manifest/manifest-intro) file for the `android.hardware.type.automotive`
feature:  

    <manifest ...>
      ...
      <!--
        See https://developer.android.com/training/cars/distribute#choose-track-aaos
        for details on how to choose which value to use for the android:required attribute.
      -->
      <uses-feature
          android:name="android.hardware.type.automotive"
          android:required="[true|false]">
      ...
    </manifest>

Additionally, if your app has any [explicit feature declaration](https://developer.android.com/guide/topics/manifest/uses-feature-element#declared) with
`android:required="true"` or [implicit feature requirement](https://developer.android.com/guide/topics/manifest/uses-feature-element#implicit) for any of the
following features, you must update or remove them so that your app's feature
requirements don't prevent its distribution to otherwise compatible vehicles:

- [`android.hardware.wifi`](https://developer.android.com/guide/topics/manifest/uses-feature-element#wi-fi-hw-features)
- [`android.hardware.screen.portrait`](https://developer.android.com/guide/topics/manifest/uses-feature-element#screen-hw-features)
- [`android.hardware.screen.landscape`](https://developer.android.com/guide/topics/manifest/uses-feature-element#screen-hw-features)
- [`android.hardware.camera`](https://developer.android.com/guide/topics/manifest/uses-feature-element#camera-hw-features)

| **Tip:** Use the [Merged Manifest view](https://developer.android.com/build/manage-manifests#inspect_the_merged_manifest_and_find_conflicts) when validating your app's feature requirements as dependencies can introduce requirements you might not be aware of.

For features explicitly declared with `android:required="true"`, you can do
one of the following:

- Delete the `<uses-feature>` element if the feature isn't otherwise implicitly required.
- Explicitly declare the feature with `android:required="false"`.

For implicitly required features, you can do one of the following:

- Explicitly declare the feature with `android:required="false"`.
- Remove or update the manifest values that introduce the implicit requirement on the feature.

Changing the feature declarations in your manifest doesn't impact the actual
functioning of your app, so check that your app still functions properly without
these features.

## Frequently asked questions

### Which vehicles come with Google built-in?

See the [Cars with Google built-in](https://built-in.google/cars/#explore-cars) site for a list of OEMs that have models
with Google built-in. Hardware specifications and other device details can be
obtained using the Play Console's Device Catalog.