---
title: https://developer.android.com/jetpack/androidx/releases/ads
url: https://developer.android.com/jetpack/androidx/releases/ads
source: md.txt
---

# Ads

# Ads

[User Guide](https://developer.android.com/training/articles/ad-id)  
API Reference  
[androidx.ads.identifier](https://developer.android.com/reference/androidx/ads/identifier/package-summary)  
[androidx.ads.identifier.provider](https://developer.android.com/reference/androidx/ads/identifier/provider/package-summary)  
The Advertising ID library defines an interface to interact with system-level ad providers across the devices running your app. This interface allows your app to receive consistent advertising ID values.  

| Latest Update | Stable Release | Release Candidate | Beta Release |                                       Alpha Release                                        |
|---------------|----------------|-------------------|--------------|--------------------------------------------------------------------------------------------|
| March 8, 2023 | -              | -                 | -            | [1.0.0-alpha05](https://developer.android.com/jetpack/androidx/releases/ads#1.0.0-alpha05) |

## Declaring dependencies

To add a dependency on Ads, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    implementation 'androidx.ads:ads-identifier:1.0.0-alpha05'

    // Optional - add if you're using Guava to handle
    // return values of type ListenableFuture.
    implementation 'com.google.guava:guava:28.0-android'
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.ads:ads-identifier:1.0.0-alpha05")

    // Optional - add if you're using Guava to handle
    // return values of type ListenableFuture.
    implementation("com.google.guava:guava:28.0-android")
}
```

For more information about dependencies, see[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:807287+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=807287&template=1390045)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.0.0

### Version 1.0.0-alpha05

March 8, 2023

`androidx.ads:ads-identifier:1.0.0-alpha05`,`androidx.ads:ads-identifier-common:1.0.0-alpha05`, and`androidx.ads:ads-identifier-provider:1.0.0-alpha05`are released.[Version 1.0.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/0a3d894e8fe0217f1312fb163a89ad51bf15794e..ad9ba647b7548818fc9d4796a03a3b5510166fb3/ads)

**API Changes**

- Deprecated`androidx.ads:ads-identifier`\&`androidx.ads:ads-identifier-provider`. Please migrate to the[Advertising ID API that's available as part of Google Play Services](https://developers.google.com/android/reference/com/google/android/gms/ads/identifier/AdvertisingIdClient)instead. ([I57791](https://android-review.googlesource.com/#/q/I57791965848891725f98e373d10708e1e525f334))

### Version 1.0.0-alpha04

January 22, 2020

`androidx.ads:ads-identifier:1.0.0-alpha04`,`androidx.ads:ads-identifier-common:1.0.0-alpha04`, and`androidx.ads:ads-identifier-provider:1.0.0-alpha04`are released.[Version 1.0.0-alpha04 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/73974afa0b122e423606439e6d8e249da523534e..0a3d894e8fe0217f1312fb163a89ad51bf15794e/ads).

**New features**

- Performance improvements.

**API changes**

- `AdvertisingIdInfo.getId()`now returns the Advertising ID from`AdvertisingIdProvider`directly, so the ID could be any format now.

### Version 1.0.0-alpha03

November 20, 2019

`androidx.ads:ads-identifier:1.0.0-alpha03`and`androidx.ads:ads-identifier-common:1.0.0-alpha03`are released.[Version 1.0.0-alpha03 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/561afade39b67853e2b54301e6b0cd16d19ce0a7..73974afa0b122e423606439e6d8e249da523534e/ads).

**Bug fixes**

- Removed dependency on the Java 8 programming language. This library now targets the Java 7 programming language.

### Version 1.0.0-alpha02

September 18, 2019

`androidx.ads:ads-identifier:1.0.0-alpha02`and`androidx.ads:ads-identifier-common:1.0.0-alpha02`are released.[Version 1.0.0-alpha02 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/886c5f552be88f0d404fbae205244e074a75bb03..561afade39b67853e2b54301e6b0cd16d19ce0a7/ads).

**API changes**

- Changed the return type of`AdvertisingIdUtils.getAdvertisingIdProviderServices()`from`List<ResolveInfo>`to`List<ServiceInfo>`

**Bug fixes**

- Changed the`AdvertisingIdNotAvailableException`message to more accurately read "No compatible AndroidX Advertising ID Provider available."

### Version 1.0.0-alpha01

August 7, 2019

`androidx.ads:ads-identifier:1.0.0-alpha01`,`androidx.ads:ads-identifier-common:1.0.0-alpha01`, and`androidx.ads:ads-identifier-provider:1.0.0-alpha01`are released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/b2b23e833fc78420c0e1212c35ff1fbf9b327eaf..886c5f552be88f0d404fbae205244e074a75bb03/ads).