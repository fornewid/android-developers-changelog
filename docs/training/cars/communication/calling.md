---
title: https://developer.android.com/training/cars/communication/calling
url: https://developer.android.com/training/cars/communication/calling
source: md.txt
---

Calling experiences are in beta At this time, anyone can publish communication apps with calling experiences to internal testing and closed testing tracks on the Play Store. Publishing to open testing and production tracks will be permitted at a later date. [Nominate yourself to be an early access partner →](https://forms.gle/VsXEdDEBidxw8q8u8) ![](https://developer.android.com/static/images/picto-icons/test-tube-2.svg)

Apps that support making voice calls can improve their experience on Android
Auto by integrating with the [Telecom Jetpack library](https://developer.android.com/develop/connectivity/telecom) and
providing a templated user interface built using the [Android for Cars App
Library](https://developer.android.com/training/cars/apps).

## Integrate with the Jetpack Telecom library

To support answering and controlling calls on Android Auto, your app must
integrate with the Telecom Jetpack library as described in [Build a calling
app](https://developer.android.com/develop/connectivity/telecom/voip-app). In particular, your app must support the callbacks
described in [Remote surface support](https://developer.android.com/develop/connectivity/telecom/voip-app/telecom#remote-surface-support). Your app must also use
its telecom integration at all times, not just when a user's phone is running
Android Auto.
| **Important:** Additional requirements for your app's telecom integration will be provided in this guide soon.

## Build a templated calling experience

In addition to the in-call view that Android Auto provides and which is powered
by your app's telecom integration, your app can provide a templated experience
to let users access your app's content on their car screen. For example, your
app can display a list of contacts with actions to start a call, an agenda view
of upcoming calls, a call log, and more. While a call is ongoing, Android Auto
automatically displays its in-call view for the duration of the call, replacing
your app's templated screens.

Follow the guidance in [Use the Android for Cars App Library](https://developer.android.com/training/cars/apps) and [Add
support for Android Auto to your templated app](https://developer.android.com/training/cars/apps/auto) to get started
building your app's templated experience. Then, refer to the guidance on this
page to understand the specific requirements for calling apps.

### Configure your app's manifest files

To inform Android Auto of your app's capabilities, your app must do the
following:

#### Declare category support in your manifest

Your app needs to declare the `androidx.car.app.category.CALLING`
[car app category](https://developer.android.com/training/cars/apps#supported-app-categories) in the intent
filter of its [`CarAppService`](https://developer.android.com/reference/androidx/car/app/CarAppService).

    <application>
        ...
       <service
           ...
            android:name=".MyCarAppService"
            android:exported="true">
          <intent-filter>
            <action android:name="androidx.car.app.CarAppService" />
            <category android:name="androidx.car.app.category.CALLING"/>
          </intent-filter>
        </service>
        ...
    <application>

| **Important:** If your app supports both calling and [messaging](https://developer.android.com/training/cars/communication/messaging), include both `androidx.car.app.category.CALLING` and `androidx.car.app.category.MESSAGING` `<category>` elements in the same intent filter.

## Distribute calling apps

Because apps that support calling can only be published to Internal Testing and
Closed Testing tracks on Google Play, you shouldn't promote builds that include
support to Open Testing or Production tracks, as submissions containing builds
on those tracks will be rejected.