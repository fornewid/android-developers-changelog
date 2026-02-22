---
title: https://developer.android.com/jetpack/androidx/releases/core-uwb
url: https://developer.android.com/jetpack/androidx/releases/core-uwb
source: md.txt
---

# Core Ultra Wideband (UWB)

API Reference  
[androidx.core.uwb](https://developer.android.com/reference/kotlin/androidx/core/uwb/package-summary)  
Implement UWB (ultra-wideband) on supported devices.  

|   Latest Update   | Stable Release | Release Candidate | Beta Release |                                          Alpha Release                                          |
|-------------------|----------------|-------------------|--------------|-------------------------------------------------------------------------------------------------|
| December 11, 2024 | -              | -                 | -            | [1.0.0-alpha10](https://developer.android.com/jetpack/androidx/releases/core-uwb#1.0.0-alpha10) |

## Declaring dependencies

To add a dependency on core, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    // Use to implement UWB (ultra-wideband) on supported devices
    implementation "androidx.core.uwb:uwb:1.0.0-alpha10"
}
```

### Kotlin

```kotlin
dependencies {
    // Use to implement UWB (ultra-wideband) on supported devices
    implementation("androidx.core.uwb:uwb:1.0.0-alpha10")
}
```

For more information about dependencies, see[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:1185313+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1185313&template=1680952)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.0

### Version 1.0.0-alpha10

December 11, 2024

`androidx.core.uwb:uwb:1.0.0-alpha10`and`androidx.core.uwb:uwb-rxjava3:1.0.0-alpha10`are released. Version 1.0.0-alpha10 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/b8a68b0896897fa158508d73a31998a26161d9a7..46295bc0b75a16f452e8e0090e8de41073d4dbb6/core/uwb).

**API Changes**

- Adds reason code`STATE_CHANGE_REASON_UNKNOWN`,`STATE_CHANGE_REASON_SYSTEM_POLICY`and`STATE_CHANGE_REASON_COUNTRY_CODE_ERROR`for UWB state change. ([I43e36](https://android-review.googlesource.com/#/q/I43e36ba788dda7c7138946d66eee188850563396))
- Add new API`RangingResult#RangingResultInitialized`to send event when a ranging session is initialized. ([I386bb](https://android-review.googlesource.com/#/q/I386bbfa6f21f37f4d8f717f6d2c5eacbcf0ecfed))
- Add new APIs`subscribeToUwbAvailability(observer: UwbAvailabilityCallback)`and`unsubscribeFromUwbAvailability()`to listener to the UWB state change event. Add new interface`UwbAvailabilityCallback`for user to define callback function when a UWB state change event is observed. ([I37191](https://android-review.googlesource.com/#/q/I37191518ade2b0fd88314dad6828421f9dd958bf)).

### Version 1.0.0-alpha09

October 16, 2024

`androidx.core.uwb:uwb:1.0.0-alpha09`and`androidx.core.uwb:uwb-rxjava3:1.0.0-alpha09`are released. Version 1.0.0-alpha09 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/51191bc12f96f233fc08995e1b4e8ff8b88bc7ce..b8a68b0896897fa158508d73a31998a26161d9a7/core/uwb).

**API Changes**

- Adds new API`isAvailable()`to check UWB availability. ([If6fc6](https://android-review.googlesource.com/#/q/If6fc66997c1bae03ba0e8529076d7d09ffac88cb))
- Adds new API`addControleeWithSessionParams`to support add controlee p-sts individual key case. ([Ie7849](https://android-review.googlesource.com/#/q/Ie7849e575beab2e719bd71b9eb518196e6d0e088))

### Version 1.0.0-alpha08

January 24, 2024

`androidx.core.uwb:uwb:1.0.0-alpha08`and`androidx.core.uwb:uwb-rxjava3:1.0.0-alpha08`are released.[Version 1.0.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3315f1ef094c312203fe26841287902916fbedf5..51191bc12f96f233fc08995e1b4e8ff8b88bc7ce/core/uwb)

**API Changes**

- Adds new capabilities and parameters to allow 3p app to set ranging interval, slot duration and enable/disable AoA. Adds new API to support reconfiguration of ranging interval and range data notification. ([Iebd18](https://android-review.googlesource.com/#/q/Iebd186e4bd22d588bd3096815420ae8915fc13e9))

### Version 1.0.0-alpha07

August 23, 2023

`androidx.core.uwb:uwb:1.0.0-alpha07`and`androidx.core.uwb:uwb-rxjava3:1.0.0-alpha07`are released.[Version 1.0.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4aed940027a19667e67d155563fc5fa8b7279313..3315f1ef094c312203fe26841287902916fbedf5/core/uwb)

**Bug Fixes**

- Fixed an issue that AOSP backend is not used when CN devices has Google Play Services installed.

### Version 1.0.0-alpha06

July 26, 2023

`androidx.core.uwb:uwb:1.0.0-alpha06`and`androidx.core.uwb:uwb-rxjava3:1.0.0-alpha06`are released.[Version 1.0.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a200cb82769634cecdb118ec4f0bfdf0b086e597..4aed940027a19667e67d155563fc5fa8b7279313/core/uwb)

**New Features**

- Add support for Provisioned STS. Now the users can choose Provisioned STS for UWB ranging if the device is capable of Provisioned STS. ([I19812](https://android-review.googlesource.com/#/q/I1981250cb2ac1d41c21ccd4deb6c7f0ccee05e05))

**API Changes**

- Add`subSessionId`and`subSessionKeyInfo`to`rangingParameters`. Add new config ids to support Provisioned STS. ([I19812](https://android-review.googlesource.com/#/q/I1981250cb2ac1d41c21ccd4deb6c7f0ccee05e05))
- Merged public and experimental API files for a,b,c-paths ([I8cfee](https://android-review.googlesource.com/#/q/I8cfeeb37f9952db225e8d1eea6f471a920ac1dda),[b/278769092](https://issuetracker.google.com/issues/278769092))
- N/A, API file changes are just reordering methods ([I5fa95](https://android-review.googlesource.com/#/q/I5fa95ca42073461bed8e5020c91b4c0894b70753))
- Migrated`androidx.core`group to use merged public API files ([Ifdef4](https://android-review.googlesource.com/#/q/Ifdef4c6a6b2828cba776b82672f2fc0e02c3b3b8),[b/278769092](https://issuetracker.google.com/issues/278769092))
- Add`minRangingInterval`,`supportedChannels`and`supportedConfigIds`to`rangingCapabilities`as new fields. ([I2a204](https://android-review.googlesource.com/#/q/I2a204042abf1c0c4a4970cbd19a8fb1a9031d09c))

**Bug Fixes**

- Fix the issue that the UWB client cannot be created in non-gms area.

### Version 1.0.0-alpha05

April 5, 2023

`androidx.core.uwb:uwb:1.0.0-alpha05`and`androidx.core.uwb:uwb-rxjava3:1.0.0-alpha05`are released.[Version 1.0.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4a2f5e696614339c1ac21f706c1a17c0285780e7..a200cb82769634cecdb118ec4f0bfdf0b086e597/core/uwb)

**API Changes**

- Rename`RangingParameters#CONFIG_ID_1`to`CONFIG_UNICAST_DS_TWR`.
- Add a new config id`RangingParameters#CONFIG_MULTICAST_DS_TWR`. ([I2f1b7](https://android-review.googlesource.com/#/q/I2f1b71082e71725b927b3ff52f77230d45cc01cc))

**Bug Fixes**

- Fix a bug that users cannot start multiple ranging sessions in parallel.

### Version 1.0.0-alpha04

December 7, 2022

`androidx.core.uwb:uwb:1.0.0-alpha04`and`androidx.core.uwb:uwb-rxjava3:1.0.0-alpha04`are released.[Version 1.0.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bea814b246f89ff7244e3c6b0648f0b57e47897c..4a2f5e696614339c1ac21f706c1a17c0285780e7/core/uwb)

**New Features**

- When there's no GMS support, AndroidX API will try to use the AOSP UWB backend service that are distributed to OEMs via AOSP platform.([532de0](https://android-review.googlesource.com/#/q/532de0e7d2ce79392c23654ca709cf69fcfbc0b9))

**API Changes**

- Adding`@JvmDefaultWithCompatibility`annotation ([I8f206](https://android-review.googlesource.com/#/q/I8f2067bb0754a5e9dc70c934403366ca8d319c36))

### Version 1.0.0-alpha03

August 10, 2022

`androidx.core.uwb:uwb:1.0.0-alpha03`and`androidx.core.uwb:uwb-rxjava3:1.0.0-alpha03`are released.[Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8094b683499b4098092c01028b55a38b49e357f2..bea814b246f89ff7244e3c6b0648f0b57e47897c/core/uwb)

**New Features**

- Introducing a new ranging profile, Controller. UWB devices with Controller profile can determine the ranging channel two devices will range with.

**API Changes**

- Adding controller support for UWB ([I52a71](https://android-review.googlesource.com/#/q/I52a71eea6bf3507a7551322a0cb3176224be8541))

### Version 1.0.0-alpha02

June 29, 2022

`androidx.core.uwb:uwb-rxjava3:1.0.0-alpha02`is released.[Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8094b683499b4098092c01028b55a38b49e357f2/core/uwb/uwb-rxjava3)

**New Features**

- Introducing a java interoperable artifact for the uwb module. The new artifact depends on rxjava3 and will be consumable for java clients.

### Version 1.0.0-alpha02

June 15, 2022

`androidx.core.uwb:uwb:1.0.0-alpha02`is released.[Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ca25209860b49786e2067cb4fd696085171b3d01..216d4243e72fc14215f8150e63c8263472cc0120/core/uwb/uwb)

**New Features**

- Introducing a public`UWB_CONFIG_ID_1`

**API Changes**

- Distance of`RangingResultPosition`is now nullable

### Version 1.0.0-alpha01

June 1, 2022

`androidx.core.uwb:uwb:1.0.0-alpha01`is released.[Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ca25209860b49786e2067cb4fd696085171b3d01/core/uwb/uwb)

**New Features**

- The UWB library provides a set of APIs for developers to interact with UWB-enabled devices. The use-case will be limited to partnered devices which already assume the Controller profile of UWB ranging sessions, with the support for Controller profile planned in the near future. Two top level API surfaces are included in this initial release,`UwbManager`and`UwbClientSessionScope`.