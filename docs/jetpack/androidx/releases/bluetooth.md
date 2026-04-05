---
title: https://developer.android.com/jetpack/androidx/releases/bluetooth
url: https://developer.android.com/jetpack/androidx/releases/bluetooth
source: md.txt
---

# bluetooth

# bluetooth

API Reference  
[androidx.bluetooth](https://developer.android.com/reference/kotlin/androidx/bluetooth/package-summary)  
Use the Android platform's Bluetooth features with backward-compatible APIs.  

|   Latest Update   | Stable Release | Release Candidate | Beta Release |                                          Alpha Release                                           |
|-------------------|----------------|-------------------|--------------|--------------------------------------------------------------------------------------------------|
| November 29, 2023 | -              | -                 | -            | [1.0.0-alpha02](https://developer.android.com/jetpack/androidx/releases/bluetooth#1.0.0-alpha02) |

## Declaring dependencies

To add a dependency on Bluetooth, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    
    implementation "androidx.bluetooth:bluetooth:1.0.0-alpha02"
}
```

### Kotlin

```kotlin
dependencies {
    
    implementation("androidx.bluetooth:bluetooth:1.0.0-alpha02")
}
```

For more information about dependencies, see[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:1190075+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1190075&template=1683949)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

There are no release notes for this artifact.

## Version 1.0

### Version 1.0.0-alpha02

November 29, 2023

`androidx.bluetooth:bluetooth:1.0.0-alpha02`and`androidx.bluetooth:bluetooth-testing:1.0.0-alpha02`are released.[Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/91bb8c1f81dcb031bda00fcd8e55f1e890b56f06..b5166f9a1e9c047162d1215884c3e2cd41a4a74a/bluetooth)

**New Features**

- Lower`minSdkVersion`to 21

**API Changes**

- `GattServerConnectFlow#updateServices`becomes a suspend function ([I0237d](https://android-review.googlesource.com/#/q/I0237d90173df024f4052a781ba41dd72a9a54343))
- Change`AdvertiseParams.durationMillis`to Long ([If6771](https://android-review.googlesource.com/#/q/If6771fb2a9de564dd194d62bf100420e4b6a16d0))
- Convert`openGattServer`to Flow ([Icef54](https://android-review.googlesource.com/#/q/Icef5495059e5fd5d7db9aa1eed779b798142d2d8))
- Throw`ScanException`on scan fail and set scanner to`setLegacy(false)`by default ([Ib337c](https://android-review.googlesource.com/#/q/Ib337c25327a8c2a9611352b804a8ae6c71a99656))
- Throw`AdvertiseException`on advertise fail ([I0e691](https://android-review.googlesource.com/#/q/I0e691b67dfb11f0e67e6c61845f38b5a2bcfd44c))
- Add general bluetooth exception to catch ([I0130d](https://android-review.googlesource.com/#/q/I0130d754ada8ec78577936ca65bbd56f97feb69c))
- Convert advertise to Flow and change maximum duration ([I32fd8](https://android-review.googlesource.com/#/q/I32fd8522085028d20735749cd9ca2f18fcae9851))
- Add`serviceData`and`serviceSolicitationUuids`to`ScanResult`([I6d7f0](https://android-review.googlesource.com/#/q/I6d7f0a36e15b168a374ad3ea8d28f18bc6b7cb79))
- Change`durationMillis`from Long to Duration ([I89d49](https://android-review.googlesource.com/#/q/I89d4936165a43600862521673605d2e533bc9677))
- Add rssi, and`periodicAdvertisingInterval`to`ScanResult`([I60b51](https://android-review.googlesource.com/#/q/I60b514a7893ec07bcc0eec2a8706e635c4c51c1f))
- Add`serviceSolicitationUuid`and`solicitationUuidMask`to`ScanFilter`([Ic2206](https://android-review.googlesource.com/#/q/Ic220683ef400b7d707424b250ef497194fad450d))
- Added`GattServerSessionScope#subscribedCharacteristics`([I0edab](https://android-review.googlesource.com/#/q/I0edabd53e1af3dcd64abd42470887a36de236144))
- Add`serviceSolicitationUuids`to`AdvertiseParams`([Ic9aa7](https://android-review.googlesource.com/#/q/Ic9aa78cad8da049ccfabbe48f468e5e193fbaad0))
- Change`AdvertiseParams.durationMillis`from Int to Long ([I6873f](https://android-review.googlesource.com/#/q/I6873f3b2c222f02ab0f53c04e66c23a6106d86a5))
- `GattServerSessionScope#notify`does not return but throws an exception if it fails ([Ifc26f](https://android-review.googlesource.com/#/q/Ifc26fac2a3b8fbd0aa404fb4e6d5d9fa4c59f9d5))

**Bug Fixes**

- Extract scan functionality ([I4d43f](https://android-review.googlesource.com/#/q/I4d43f370b201c942bea0eda1230fef7ff6ef8aca))

### Version 1.0.0-alpha01

September 20, 2023

`androidx.bluetooth:bluetooth:1.0.0-alpha01`and`androidx.bluetooth:bluetooth-testing:1.0.0-alpha01`are released.[Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/91bb8c1f81dcb031bda00fcd8e55f1e890b56f06/bluetooth)

**New Features**

- This is the initial release of AndroidX Bluetooth APIs that provides a Kotlin API surface covering Bluetooth LE scanning and advertising, and GATT client and server use cases. It provides a minimal API surface, clear thread model with async and sync operations, and ensures all methods be executed and provides the results.