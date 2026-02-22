---
title: https://developer.android.com/training/cars/testing/aaos-on-pixel
url: https://developer.android.com/training/cars/testing/aaos-on-pixel
source: md.txt
---

![Android Automotive OS running on Pixel Tablet](https://developer.android.com/static/training/cars/images/aaos-on-pixel.png)

In addition to the[Android Automotive OS emulator](https://developer.android.com/training/cars/testing/emulator),[Pixel Tablet](https://store.google.com/product/pixel_tablet)can be used as a physical hardware device to test your app on Android Automotive OS.

## Request access

Access to the Android Automotive OS on Pixel Tablet system image requires inclusion on an allow list. You can submit the[Android Automotive OS on Pixel Tablet access form](https://goo.gle/Tablet-AAOS)to gain access.
| **Note:** When filling out the form, if you are signed into your Google Account, the email associated with your account isn't included when you submit the form. Only the email address you provide for the first question is submitted.

## System images

The following targets have builds available on the`git_udc-car-release`branch:

|            Target             | `adb`root | [Google Play services](https://developer.android.com/training/cars/platforms/automotive-os/google-play/google-services) | [Google Automotive App Host](https://play.google.com/store/apps/details?id=com.google.android.apps.automotive.templates.host) | Google Play Store | Google Maps | Google Assistant | [Android Auto](https://developer.android.com/training/cars/testing/aaos-on-pixel#android-auto) |
|-------------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|-------------------|-------------|------------------|------------------------------------------------------------------------------------------------|
| `tangorpro_car_ext-user`      |           | ✔                                                                                                                       | ✔                                                                                                                             | ✔                 | ✔           | ✔                | ✔                                                                                              |
| `tangorpro_car_ext-userdebug` | ✔         | ✔                                                                                                                       | ✔                                                                                                                             |                   |             |                  |                                                                                                |

## Flash your device

To flash your device, follow the steps detailed in[Flash with Android Flash Tool](https://source.android.com/docs/setup/build/flash). Make sure you're signed in to the tool using the Google Account that's enrolled in the program, or you won't see the builds. When asked to select a build, select one from[System images](https://developer.android.com/training/cars/testing/aaos-on-pixel#system-images)that fits your needs.

### Return to public build

If you would like to revert your device's software, you can follow the instructions in[Return Pixel to public build](https://source.android.com/docs/setup/build/flash#latest-public-build).

## Use the device as an Android Auto receiver

On`user`images (UAA1.250513.001 or later), you can use the device as an Android Auto receiver. To connect your phone to your Pixel Tablet running Android Automotive OS, open the Android Auto app from the launcher grid on the tablet and follow the onscreen instructions to pair using Bluetooth.
| **Caution:** There are[known issues with wired connections](https://developer.android.com/training/cars/testing/aaos-on-pixel#issues-android-auto). Use a wireless connection if possible.

## Emulate hardware state

As with the[Android Automotive OS emulator](https://developer.android.com/training/cars/testing/emulator#emulate-state), the Android Automotive OS image for Pixel Tablet supports emulating hardware state.
| **Important:** To emulate hardware state using`adb`, you must use a[system image](https://developer.android.com/training/cars/testing/aaos-on-pixel#system-images)with`adb`root access.

### Simulate driving

#### Simulate driving using a quick setting

On`userdebug`images (UAA1.250207.001 or later), you can simulate driving by using a quick setting menu:

1. Enable[Developer options](https://developer.android.com/studio/debug/dev-options).
2. Toggle*Set driving*in the quick setting menu, as shown in the following image:

![Quick setting](https://developer.android.com/static/training/cars/images/quick-setting.png)Quick setting

#### Simulate driving using adb

To simulate a driving state using`adb`, you can use the following command:  

    adb shell cmd car_service inject-vhal-event 0x11600207 30 -t 2000 \
    && adb shell cmd car_service inject-vhal-event 0x11400400 8 \
    && adb shell cmd car_service inject-vhal-event 0x11200402 false

This command does three things:

1. Sets[`PREF_VEHICLE_SPEED`](https://developer.android.com/reference/android/car/VehiclePropertyIds#PERF_VEHICLE_SPEED)to 30 meters per second (about 67 mph or 108 km/h), ramping the change over 2 seconds.
2. Sets[`GEAR_SELECTION`](https://developer.android.com/reference/android/car/VehiclePropertyIds#GEAR_SELECTION)to[`GEAR_DRIVE`](https://developer.android.com/reference/android/car/VehicleGear#GEAR_DRIVE).
3. Sets[`PARKING_BRAKE_ON`](https://developer.android.com/reference/android/car/VehiclePropertyIds#PARKING_BRAKE_ON)to`false`.

To simulate a parked state (the default state upon boot), you can use the following command:  

    adb shell dumpsys car_service inject-vhal-event 0x11600207 0 \
    && adb shell dumpsys car_service inject-vhal-event 0x11400400 4

This command does two things:

1. Sets[`PREF_VEHICLE_SPEED`](https://developer.android.com/reference/android/car/VehiclePropertyIds#PERF_VEHICLE_SPEED)to 0 meters per second (stopped).
2. Sets[`GEAR_SELECTION`](https://developer.android.com/reference/android/car/VehiclePropertyIds#GEAR_SELECTION)to[`GEAR_PARK`](https://developer.android.com/reference/android/car/VehicleGear#GEAR_PARK).

| **Note:** You can create an[alias](https://en.wikipedia.org/wiki/Alias_(command))for each command to simplify their use.

## Known issues

Android Automotive OS for Pixel Tablet is not[CTS](https://source.android.com/docs/compatibility/cts)certified and shouldn't be treated as a production device. This section describes known issues and potential workarounds.

If you run into an issue or have a feature request while using Android Automotive OS on Pixel Tablet, you can report it using the Google Issue Tracker. Be sure to fill out all the requested information in the issue template. Before filing a new issue, check whether it is already reported in the[issues list](https://issuetracker.google.com/issues?q=componentid:1588058). You can subscribe and vote for issues by clicking the star for an issue in the tracker. For more information, see[Subscribing to an Issue](https://developers.google.com/issue-tracker/guides/subscribe#starring_an_issue).

[Create a new issue](https://issuetracker.google.com/issues/new?component=1588058)

### Location

Because the Pixel Tablet doesn't have a GPS sensor and Android Automotive OS devices[aren't required to support network location](https://developer.android.com/training/cars/platforms/automotive-os/coarse-location), Pixel Tablets running Android Automotive OS don't report their own location.
| **Important:** All cars with Google built-in must have a GPS receiver and make location information accessible to apps. In addition to the options in this section, you can also use the[Android Automotive OS emulator](https://developer.android.com/training/cars/testing/emulator)to test any location-based experiences using the[location extended controls](https://developer.android.com/studio/run/emulator-extended-controls#location).

#### Mock location using an app

To test an app that requires location readings,[enable developer options](https://developer.android.com/studio/debug/dev-options#enable)and[install a mock location app](https://developer.android.com/studio/debug/dev-options#debugging).

#### Mock location using`adb`

Alternatively, you can use`adb`to mock location by using the following commands:  

    # Turn on the system location setting
    adb shell cmd location set-location-enabled true

    # Enable the developer option to allow mock locations
    adb shell appops set 2000 android:mock_location allow

    # Add a mock location provider named <var translate="no">PROVIDER_NAME</var>
    # If your app uses a specific type of location provider, you should use the standard
    # name of that provider, such as https://developer.android.com/reference/android/location/LocationManager#FUSED_PROVIDER, https://developer.android.com/reference/android/location/LocationManager#GPS_PROVIDER, https://developer.android.com/reference/android/location/LocationManager#NETWORK_PROVIDER, or https://developer.android.com/reference/android/location/LocationManager#PASSIVE_PROVIDER
    adb shell cmd location providers add-test-provider <var translate="no">PROVIDER_NAME</var>

    # Use the mock location provider named <var translate="no">PROVIDER_NAME</var>
    adb shell cmd location providers set-test-provider-enabled <var translate="no">PROVIDER_NAME</var> true

    # Set the location provided by <var translate="no">PROVIDER_NAME</var>,
    # where latitude and longitude are a comma separated pair such as "37.4215,-122.0843"
    adb shell cmd location providers set-test-provider-location <var translate="no">PROVIDER_NAME</var> --location <var translate="no">LATITUDE</var>,<var translate="no">LONGITUDE</var>

    # Confirm that the location has been set
    adb shell dumpsys location | grep "last location"

To stop using the mock location provider, use the following command:  

    adb shell cmd location providers set-test-provider-enabled <var translate="no">PROVIDER_NAME</var> false

| **Tip:** Run`adb shell cmd location -h`to see additional information and options for mocking locations using`adb`.

### Bluetooth

Support for[Bluetooth profiles](https://www.bluetooth.com/specifications/specs/), such as the Hands-Free Profile (HFP) and Advanced Audio Distribution Profile (A2DP), may be missing or not fully functional.

### Radio

The default Radio app does not work.

### Android Auto

Wired Android Auto connections are not working consistently. Use a wireless connection if you can. See[Set up Android Auto](https://support.google.com/androidauto/answer/6348029)for step-by-step instructions.

## Release notes

### UAA1.250513.001 (May 13, 2025)

#### Updates

- The`tangorpro_car_ext-user`build now supports acting as an Android Auto receiver.

### UAA1.250207.001 (Feb 7, 2025)

#### Updates

- Adds support for[Car Ready Mobile Apps](https://developer.android.com/training/cars/car-ready-mobile-apps#test).
- Improves audio stability for volume control.
- Disables wake up from unplugging a USB cable and performing a tap gesture to reduce battery consumption.
- Enables camera services.
- Supports a**Quick Settings**menu in the status bar for developers. (Only available on userdebug builds.)

#### Bug fixes

- Audio volume changes per stream.
- Music volume now persists, and volume control doesn't pop up when booted.
- No longer crashes when changing volume in settings.
- Wi-Fi is disabled after reboot.
- Switches between Rotary IME and Carboard automatically.
- Removes unavailable features, such as`android.software.app_widgets`.