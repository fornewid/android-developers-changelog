---
title: https://developer.android.com/jetpack/androidx/releases/health-connect
url: https://developer.android.com/jetpack/androidx/releases/health-connect
source: md.txt
---

# Health Connect

# Health Connect

API Reference  
[androidx.health.connect.client](https://developer.android.com/reference/kotlin/androidx/health/connect/client/package-summary)  
Allows developers to read or write user's health and fitness records.  

|  Latest Update  |                                    Stable Release                                     | Release Candidate | Beta Release |                                             Alpha Release                                             |
|-----------------|---------------------------------------------------------------------------------------|-------------------|--------------|-------------------------------------------------------------------------------------------------------|
| October 8, 2025 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/health-connect#1.1.0) | -                 | -            | [1.2.0-alpha02](https://developer.android.com/jetpack/androidx/releases/health-connect#1.2.0-alpha02) |

## Requesting access to data types

To help us strengthen user privacy and security, developers integrating with Health Connect**must[declare read and/or write access](https://developer.android.com/health-and-fitness/guides/health-connect/publish/declare-access)for the[data types](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/package-summary#classes)** that their apps use. Developers must include valid use cases for the data types they use based on the app's purpose. For more information, visit[Provide information for the Health apps declaration form](https://support.google.com/googleplay/android-developer/answer/14738291)and[Health Connect by Android Permissions](https://support.google.com/googleplay/android-developer/answer/9888170).

## Declaring dependencies

To add a dependency on health, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    // Use to implement health connects
    implementation "androidx.health.connect:connect-client:1.2.0-alpha02"
}
```

### Kotlin

```kotlin
dependencies {
    // Use to implement health connects
    implementation("androidx.health.connect:connect-client:1.2.0-alpha02")
}
```

For more information about dependencies, see[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:1676744+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1676744&template=2072671)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Health Connect Testing Version 1.0

### Version 1.0.0-alpha03

April 9, 2025

`androidx.health.connect:connect-testing:1.0.0-alpha03`is released. Version 1.0.0-alpha03 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/fd7408b73d9aac0f18431c22580d9ab612278b1e..4c37298a97c16270c139eb812ddadaba03e23a52/health/connect/connect-testing).

**Bug Fixes**

- `Metadata.populatedWithTestValues`will preserve original values if an override is not provided. ([I3ee27](https://android-review.googlesource.com/#/q/I3ee275a32bd1124da47710d7cbb1d41327a96133))
- Only update changelogs when deleting existing records. ([I74a16](https://android-review.googlesource.com/#/q/I74a1622801821a41f3d36d4d307577d0212106c3))

### Version 1.0.0-alpha02

February 26, 2025

`androidx.health.connect:connect-testing:1.0.0-alpha02`is released. Version 1.0.0-alpha02 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/e454e4f29db8080452f57057fb04a8121981043b..fd7408b73d9aac0f18431c22580d9ab612278b1e/health/connect/connect-testing).

**API Changes**

- Introduce`MetadataTestHelper#populatedWithTestValues`to use in tests after metadata changes introduced in`androidx.health.connect:connect-client:1.1.0-alpha12`([I1f7f1](https://android-review.googlesource.com/#/q/I1f7f1bd207cadaaaf8a75fbb74bbe986986af9fc))
- Removes`ExperimentalTestingApi`annotation in`connect-testing`([I97a57](https://android-review.googlesource.com/#/q/I97a57f34998ae84484b02dfa79f8b849be36c749))
- Adds full stubs for records and changes in`FakeHealthConnectClient`([I15a4c](https://android-review.googlesource.com/#/q/I15a4ce39424b7dbeff86e0da7b6f6ba00ea9e6c3))

### Version 1.0.0-alpha01

September 4, 2024

`androidx.health.connect:connect-testing:1.0.0-alpha01`is released. Version 1.0.0-alpha01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/e454e4f29db8080452f57057fb04a8121981043b/health/connect/connect-testing).

**New Features**

The Health Connect Testing library simplifies the creation of automated tests. You can use this library to verify the behavior of your application and validate that it responds correctly to uncommon cases, which are hard to test manually.

You can use the library to create local unit tests, which typically verify the behavior of the classes in your app that interact with the Health Connect client.

The entry point to the library is the`FakeHealthConnectClient`class, which you use in tests to replace the`HealthConnectClient`. It has the following features:

- An in-memory representation of records, so you can insert, remove, delete and read them
- Generation of change tokens and change tracking
- Pagination for records and changes
- Aggregation responses are supported with stubs
- Allows any function to throw exceptions
- A`FakePermissionController`that can be used to emulate permissions checks

**API Changes**

- Add`FakeHealthConnectClient`[e8469](https://android-review.googlesource.com/#/q/e8469f9dddbe1d00508be828613d901e9a9f8f04)
- Add Stub overrides for`FakeHealthConnectClient`[e8469](https://android-review.googlesource.com/#/q/1b6e46ddae7d887376c989f01714283c32bedf24)

## Version 1.2

### Version 1.2.0-alpha02

October 08, 2025

`androidx.health.connect:connect-client:1.2.0-alpha02`,`androidx.health.connect:connect-client-external-protobuf:1.2.0-alpha02`, and`androidx.health.connect:connect-client-proto:1.2.0-alpha02`are released. Version 1.2.0-alpha02 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/5fa9d0954ece0376736164b0f7bc2ef33506ab70..4350deab5806bf95370a4d012d7eeaa70a10be44/health/connect).

**API Changes**

- Adds new Device Type enums ([I86ce3](https://android-review.googlesource.com/#/q/I86ce38c98ff3990c778f1e65d3c2ed876a96b426))

### Version 1.2.0-alpha01

July 30, 2025

`androidx.health.connect:connect-client:1.2.0-alpha01`,`androidx.health.connect:connect-client-external-protobuf:1.2.0-alpha01`, and`androidx.health.connect:connect-client-proto:1.2.0-alpha01`are released. Version 1.2.0-alpha01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/498142189ccc4299e3f4ad2b998a27686431272d..5fa9d0954ece0376736164b0f7bc2ef33506ab70/health/connect).

**New Features**

- Add backwards compatibility support for Skin Temperature ([d04b1df](https://android.googlesource.com/platform/frameworks/support/+/d04b1df6acd8ef0474c8050f625f7f7e9cdb1b36))
- Add backwards compatibility support for Mindfulness ([444eda2](https://android.googlesource.com/platform/frameworks/support/+/444eda2a30bab7b2d9a397323daceeba46819490))
- Add Activity Intensity API for Android 14+ ([d10f67b](https://android.googlesource.com/platform/frameworks/support/+/d10f67b1cbb147b99f4ea8072fc86c84c42cca19))

## Version 1.1

### Version 1.1.0

October 08, 2025

`androidx.health.connect:connect-client:1.1.0`,`androidx.health.connect:connect-client-external-protobuf:1.1.0`, and`androidx.health.connect:connect-client-proto:1.1.0`have been promoted to its first stable release with no changes since its previous RC release.

### Version 1.1.0-rc03

July 16, 2025

`androidx.health.connect:connect-client:1.1.0-rc03`,`androidx.health.connect:connect-client-external-protobuf:1.1.0-rc03`, and`androidx.health.connect:connect-client-proto:1.1.0-rc03`are released. Version 1.1.0-rc03 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/8ff90930ee1c084c0f4cc9b3eecd9cd7b4c3d8d5..498142189ccc4299e3f4ad2b998a27686431272d/health/connect).

**Bug Fixes**

- Fixed`IllegalArgumentException`for aggregations over a DST boundary. ([Ic9e4f](https://android-review.googlesource.com/#/q/Ie3e81b22b23fa9b55e62d1874747ea2e193593b0))

### Version 1.1.0-rc02

June 4, 2025

`androidx.health.connect:connect-client:1.1.0-rc02`,`androidx.health.connect:connect-client-external-protobuf:1.1.0-rc02`, and`androidx.health.connect:connect-client-proto:1.1.0-rc02`are released. Version 1.1.0-rc02 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/8877830981271e343c44dc34861cade7ae0281bc..8ff90930ee1c084c0f4cc9b3eecd9cd7b4c3d8d5/health/connect).

**Bug Fixes**

- Added support for missing device types ([Ied486](https://android-review.googlesource.com/#/q/Ied486c58dc3fba73fe4d66a4350cb31067de484a))
- Updated mindfulness sessions permission string ([I13ab5](https://android-review.googlesource.com/#/q/I13ab5eb7ac9d95f462ac57579d029fcefc3aed1e))

### Version 1.1.0-rc01

April 23, 2025

`androidx.health.connect:connect-client:1.1.0-rc01`,`androidx.health.connect:connect-client-external-protobuf:1.1.0-rc01`, and`androidx.health.connect:connect-client-proto:1.1.0-rc01`are released. Version 1.1.0-rc01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/4c37298a97c16270c139eb812ddadaba03e23a52..8877830981271e343c44dc34861cade7ae0281bc/health/connect).

**API Changes**

- Added mindfulness feature availability flag for developers. ([I936a8](https://android-review.googlesource.com/#/q/I936a85f757748bd395659008ca52aa528877f796))

### Version 1.1.0-beta02

April 9, 2025

`androidx.health.connect:connect-client:1.1.0-beta02`,`androidx.health.connect:connect-client-external-protobuf:1.1.0-beta02`, and`androidx.health.connect:connect-client-proto:1.1.0-beta02`are released. Version 1.1.0-beta02 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/7a145e052ae61e272e91ffe285e9451b8ab71870..4c37298a97c16270c139eb812ddadaba03e23a52/health/connect).

**New Features**

- Added experimental Personal Health Record (PHR) APIs for reading and writing medical data, based on the Fast Healthcare Interoperability Resources (FHIR®) format. PHR APIs include:
  - A`FEATURE_PERSONAL_HEALTH_RECORD`constant to check if PHR is available through the feature availability API.
  - APIs for applications writing medical data sources and records.
  - APIs for applications reading medical data sources and records based on user-granted permissions.
- Added experimental Mindfulness Session Record APIs ([I51c13](https://android-review.googlesource.com/#/q/I51c13f4c9eedf5698aedeeb176844ac58082d83a)), including:
  - APIs for applications writing mindfulness session data.
  - APIs for applications reading mindfulness session data based on user-granted permissions.

**Bug Fixes**

- For Android U and higher, Jetpack's validation for`ElevationGainedRecord`,`FloorsClimbedRecord`,`HeartRateVariabilityRmssdRecord`,`HeightRecord`,`HydrationRecord`,`LeanBodyMassRecord`,`NutritionRecord`,`OxygenSaturationRecord`,`RespiratoryRateRecord`,`RestingHeartRateRecord`,`StepsRecord`,`TotalCaloriesBurnedRecord`,`Vo2MaxRecord`,`WeightRecord`, and`WheelchairPushesRecord`values has been replaced with the platform's validation. ([I0f40d](https://android-review.googlesource.com/#/q/I0f40d8aaff9a3379039e7ca9bff72cd717ec5cac))

### Version 1.1.0-beta01

March 12, 2025

`androidx.health.connect:connect-client:1.1.0-beta01`,`androidx.health.connect:connect-client-external-protobuf:1.1.0-beta01`, and`androidx.health.connect:connect-client-proto:1.1.0-beta01`are released. Version 1.1.0-beta01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/fd7408b73d9aac0f18431c22580d9ab612278b1e..7a145e052ae61e272e91ffe285e9451b8ab71870/health/connect).

**Bug Fixes**

- Enable calculation for all aggregation types across all android versions. ([I8edf](https://android-review.googlesource.com/#/q/I8edf03915d507abb1159606a59c75d2ce8775196))

### Version 1.1.0-alpha12

February 26, 2025

`androidx.health.connect:connect-client:1.1.0-alpha12`,`androidx.health.connect:connect-client-external-protobuf:1.1.0-alpha12`, and`androidx.health.connect:connect-client-proto:1.1.0-alpha12`are released. Version 1.1.0-alpha12 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/ad66672b42ec1e9359219e82b7f8189d03df40f5..fd7408b73d9aac0f18431c22580d9ab612278b1e/health/connect).

**API Changes**

- Make Metadata constructor internal ([I1fb8f](https://android-review.googlesource.com/#/q/I1fb8ff1d8e8d93766d775660a2141a05b58896bb)
- Removed experimental annotation for feature availability API. ([I5b54f](https://android-review.googlesource.com/#/q/I5b54fca1075b9dfb9ee0e000bccf424ccfc5c715))
- Introduce Metadata factory methods ([I8418b](https://android-review.googlesource.com/#/q/I8418baa04580d82208857bcc1b917cef53a1288b))
- Make recording method mandatory when creating Metadata objects ([I3a13e](https://android-review.googlesource.com/#/q/I3a13e8fdee25ac270dc75adc0e050ec9d361affc))
- Make device type mandatory when creating Device objects ([Ibc325](https://android-review.googlesource.com/#/q/Ibc325a826020c02899c017f3b3fbc4f0aa9d3c4a))

**Bug Fixes**

- Fixed missing descriptions from planned exercise steps and blocks. ([I84039](https://android-review.googlesource.com/#/q/I84039e0cba85afc1039975cfa281e5fc278949e7))
- Update java doc for blood pressure value limits. ([I8d3d4](https://android-review.googlesource.com/#/q/I8d3d4073cc3e67da8658b9f38cbd91f5bf2b91c7))
- For Android U and higher, Jetpack's validation for blood pressure record values has been replaced with the platform's validation. ([I08bf5](https://android-review.googlesource.com/#/q/I08bf51004b8d942875c55c6ca73da424f45e1651))
- Add contributing data origins for bucketed results on Android U and above. ([Ie7651](https://android-review.googlesource.com/#/q/Ie76512d912b0e34ce96a04185ad7e26cc48da874))

### Version 1.1.0-alpha11

January 15, 2025

`androidx.health.connect:connect-client:1.1.0-alpha11`,`androidx.health.connect:connect-client-external-protobuf:1.1.0-alpha11`, and`androidx.health.connect:connect-client-proto:1.1.0-alpha11`are released. Version 1.1.0-alpha11 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/b8a68b0896897fa158508d73a31998a26161d9a7..ad66672b42ec1e9359219e82b7f8189d03df40f5/health/connect).

**New Features**

- Updated background and history read permissions to support Android 13 and below.

**API Changes**

- Added inline reified overloads for`HealthPermission.getReadPermission`and`HealthPermission.getWritePermission`([I59a2e](https://android-review.googlesource.com/#/q/I59a2e473760d2a464de937dd261f7aa22f79940c))

**Bug Fixes**

- Remove legacy permission methods ([Ifd080](https://android-review.googlesource.com/#/q/Ifd080d1c35ded2a246fea165b2ab326a07358c31))
- This library now uses[JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler argument to enforce correct usage:`-Xjspecify-annotations=strict`(this is the default starting with version 2.1.0 of the Kotlin compiler). ([Iaf73a](https://android-review.googlesource.com/#/q/Iaf73a787b8b07034e55d1ec8e3495728849dc127),[b/326456246](https://issuetracker.google.com/issues/326456246))
- Fixed documentation for`HealthPermission.READ_HEALTH_DATA_HISTORY`, specifically by pointing out that reads without this permission only fail when attempting to read a single data point. ([Id5b5a](https://android-review.googlesource.com/#/q/Id5b5a8f707faac0075bd7a9119cddf8ea8c63741))

### Version 1.1.0-alpha10

October 16, 2024

`androidx.health.connect:connect-client:1.1.0-alpha10`,`androidx.health.connect:connect-client-external-protobuf:1.1.0-alpha10`, and`androidx.health.connect:connect-client-proto:1.1.0-alpha10`are released. Version 1.1.0-alpha10 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/a7476052c7a41998112966dbe93531f8538c8c54..b8a68b0896897fa158508d73a31998a26161d9a7/health/connect).

**New Features**

- Added`SkinTemperature`aggregation types. ([Ibe123](https://android-review.googlesource.com/#/q/Ibe1238dd4658f3cd786e3daf0ee37700f91d6643))
- Added`FEATURE_PLANNED_EXERCISE`constant ([Ie02a3](https://android-review.googlesource.com/#/q/Ie02a3205b4354d97d38ad894637a70076f66379d))
- Added History Reads permissions. ([I5cf41](https://android-review.googlesource.com/#/q/I5cf4146e51b6e2abfd2281e9e984fc799962fd88))
- Added Training plans API ([If5be1](https://android-review.googlesource.com/#/q/If5be153d22605ed1603a616b3a76c9351a8b4e8c))
- Added`SkinTemperatureRecord`API. ([I5605d](https://android-review.googlesource.com/#/q/I5605def92b7c16c6c816f057f735f4c27163ed11))

**Security Fixes**

- As of[this change](https://android-review.googlesource.com/q/topic:%22protobuf-4.28.2%22), androidx compiles against protobuf 4.28.2 in order to address[CVE-2024-7254](https://nvd.nist.gov/vuln/detail/CVE-2024-7254). Upgrade your dependency on`androidx.health:connect:connect-client-proto`and`androidx.health:connect:connect-client-external-protobuf`to the latest 1.1.0-alpha10 to address the vulnerability risk.

### Version 1.1.0-alpha09

September 18, 2024

`androidx.health.connect:connect-client:1.1.0-alpha09`,`androidx.health.connect:connect-client-external-protobuf:1.1.0-alpha09`, and`androidx.health.connect:connect-client-proto:1.1.0-alpha09`are released. Version 1.1.0-alpha09 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/e454e4f29db8080452f57057fb04a8121981043b..8d1527954030063e76b0d674b22ded8f606c454b/health/connect).

**New Features**

- Add background reads permission, guarded by feature availability. ([I01036](https://android-review.googlesource.com/#/q/I010365b23f72eb5c025c15d537c23b9c4475a40a),[I44db9](https://android-review.googlesource.com/#/q/I44db96cff10a6219f29a134785435f61ab557c54))

### Version 1.1.0-alpha08

September 4, 2024

`androidx.health.connect:connect-client:1.1.0-alpha08`,`androidx.health.connect:connect-client-external-protobuf:1.1.0-alpha08`, and`androidx.health.connect:connect-client-proto:1.1.0-alpha08`are released. Version 1.1.0-alpha08 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/e454e4f29db8080452f57057fb04a8121981043b/health).

**API Changes**

- Set default value for features variable in`HealthConnectClient`. ([I788dc](https://android-review.googlesource.com/#/q/I788dc0fb412ee0859e6508f5bd3010ef3ccd2c84))
- Add an API to check feature availability. ([Iedd43](https://android-review.googlesource.com/#/q/Iedd43f5e57eab7d3eb0d9c908c8377869ab4b007))

**Bug Fixes**

- Return`SDK_UNAVAILABLE`in`HealthConnectClient.getSdkStatus()`when`HealthConnectManager`is null in U+[5802f](https://android-review.googlesource.com/#/q/5802f95a03a0fb06a453b0890bc87eb52c6631e4)
- Add`toString`overrides to`RecordClasses`[aa5dc](https://android-review.googlesource.com/#/q/aa5dc8885748bcc3ed3f688e806ea52efb6c3aa0)
- Removed manual outlining of access to new platform APIs since this happens automatically via API modeling when using R8 with AGP 7.3 or later (e.g. R8 version 3.3) and for all builds when using AGP 8.1 or later (e.g. D8 version 8.1). Clients who are not using AGP are advised to update to D8 version 8.1 or later. See[this article](https://medium.com/androiddevelopers/mitigating-soft-verification-issues-in-r8-and-d8-7e9e06827dfd)for more details. ([If6b4c](https://android-review.googlesource.com/#/q/If6b4ccfca0a943b45971a422b58949b13a10bada),[b/345472586](https://issuetracker.google.com/issues/345472586))

### Version 1.1.0-alpha07

January 10, 2024

`androidx.health.connect:connect-client:1.1.0-alpha07`is released.[Version 1.1.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/465c5c5b7a0d79793bddb26a695f67aba8ea2f7e..7a45f0bc9e0a73744b3780a6f92e1b570de58bba/health/connect/connect-client)

**API Changes**

- Return`SDK_UNAVAILABLE`when`#getSdkStatus`is called from a profile user context. ([I91df3](https://android-review.googlesource.com/#/q/I91df303b90a324aee70244032cd7cbb7b1336bbd))
- Remove`SleepStageRecord`. ([/If6ada](https://android-review.googlesource.com/#/q/If6adae7a722f69806e1e634422dbaf6b60fb096a))

**Bug Fixes**

- Throw`RemoteException`instead of`IllegalStateException`on binding failures. ([Id2233](https://android-review.googlesource.com/#/q/Id2233a995510aad98f1d0da5c83cdb2f4609a571))

### Version 1.1.0-alpha06

October 18, 2023

`androidx.health.connect:connect-client:1.1.0-alpha06`is released.[Version 1.1.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1f7407d4293384a1b91bc142880e3525048b3443..465c5c5b7a0d79793bddb26a695f67aba8ea2f7e/health/connect/connect-client)

**API Changes**

- Makes`recordingMethod`definitions public. ([I401fb](https://android-review.googlesource.com/#/q/I401fbce35a8166cb85fd74777195b4596819fe89))

**Bug Fixes**

- Add documentation to exercise route specifying that location should be before end time of the session. ([0e51e6](https://android-review.googlesource.com/#/q/0e51e65666d49852f2724fc24b66c48cbfde0851))

### Version 1.1.0-alpha05

October 4, 2023

`androidx.health.connect:connect-client:1.1.0-alpha05`is released.[Version 1.1.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9ce75ea1baa2af10dda8f787f69c40c6654bcac1..1f7407d4293384a1b91bc142880e3525048b3443/health/connect/connect-client)

**API Changes**

- Added intent that navigates to health connect data management screen. ([Ibf591](https://android-review.googlesource.com/#/q/Ibf59142a73845d5f015b97e9882e1b231fc0128e))
- Removed deprecated methods in`AggregationResult`. ([Idbda9](https://android-review.googlesource.com/#/q/Idbda97d493c5832c8903366dc530dd9f24090fe6))
- Added convenience API for creating`ReadRecordsRequest`, as well as deleting and reading records, with a reified record type. ([If58a5](https://android-review.googlesource.com/#/q/If58a5c2c9acea1c22b322537daa4fa513065e393))

**Bug Fixes**

- Fixed a bug in Android 14 where null nutrition fields were being returned as`Double.MIN_VALUE`. ([1aa1d1](https://android-review.googlesource.com/#/q/1aa1d190af7cb2bed0aa1a5acd5bee31d3ea5992))
- Fixed a bug in Android 14 where aggregation by Monthly/Yearly period was throwing an exception in the response due to buckets having the same start/end time. ([281313](https://android-review.googlesource.com/#/q/28131369888d194d29614e2ea5448f8a42c63f7f))

### Version 1.1.0-alpha04

September 6, 2023

`androidx.health.connect:connect-client:1.1.0-alpha04`is released.[Version 1.1.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4aed940027a19667e67d155563fc5fa8b7279313..9ce75ea1baa2af10dda8f787f69c40c6654bcac1/health/connect/connect-client)

**API Changes**

- Java only: rename the`getHasMore()`field on[`ChangesResponse`](https://developer.android.com/reference/androidx/health/connect/client/response/ChangesResponse)to`hasMore()`. ([I80695](https://android-review.googlesource.com/#/q/I80695aa085da7707fdd97438d40e136f73c28712))
- Align[`HealthPermissionsRequestContract#createIntent`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/contracts/HealthPermissionsRequestContract#createIntent(android.content.Context,kotlin.collections.Set))check across Android versions. The contract checks that all permissions are health-related permissions. ([I143fc](https://android-review.googlesource.com/#/q/I143fc7dda5445d529278425025ff598a573a3205))

**Bug Fixes**

- Fix exception that is thrown when[`ExerciseSessionRecord`](https://developer.android.com/reference/androidx/health/connect/client/records/ExerciseSessionRecord)is created with an[`ExerciseRoute`](https://developer.android.com/reference/androidx/health/connect/client/records/ExerciseRoute)containing empty list of location. ([I45c16](https://android-review.googlesource.com/#/q/I45c16914d99df445c3716726bb5157e6ee8e91d6))
- Update[`SleepSessionRecord`](https://developer.android.com/reference/androidx/health/connect/client/records/SleepSessionRecord)documentation and sample code for reading sleep sessions. ([Idf0de](https://android-review.googlesource.com/#/q/Idf0de7ae204f8c591f40ae075bf70211644ca949))

### Version 1.1.0-alpha03

July 26, 2023

`androidx.health.connect:connect-client:1.1.0-alpha03`is released.[Version 1.1.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3b5b931546a48163444a9eddc533489fcddd7494..4aed940027a19667e67d155563fc5fa8b7279313/health/connect/connect-client)

**New Features**

- API for reading and writing Exercise routes:
  - Added`ExerciseRouteResult`to`ExerciseSessionRecord`
  - Added`ExerciseRouteRequestContract`

**API Changes**

- Added`ExerciseRouteResult`and its subclasses:`Data`,`NoData`and`ConsentRequiredStates`.
- Added`ExerciseRoute`as a standalone class, which holds location data for the route. ([I22eed](https://android-review.googlesource.com/#/q/I22eedcdd68b0842e538c602db058525a556c5ed2))
- Added`PERMISSION_WRITE_EXERCISE_ROUTE`. ([I92fc4](https://android-review.googlesource.com/#/q/I92fc45026728161584420281cfbcc094c1212bbc))
- Added`ExerciseRouteRequestContract`, added`HealthPermissionsRequestContract`. ([Ief0e5](https://android-review.googlesource.com/#/q/Ief0e516cb08662c97cbee429bad1a3d284acb5b2))

**Bug Fixes**

- Fixed construction of Energy in kilojoules ([Ie8791](https://android-review.googlesource.com/#/q/Ie87917c0316974fe19d478923d5a3ad1e86c385f))

### Version 1.1.0-alpha02

June 21, 2023

`androidx.health.connect:connect-client:1.1.0-alpha02`is released.[Version 1.1.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/95657d008c8886de1770adf1d52e01e6e952b5b0..3b5b931546a48163444a9eddc533489fcddd7494/health/connect/connect-client)

**Bug Fixes**

- Fixed`HealthDataSdkService`leak ([Ia3ba5](https://android-review.googlesource.com/#/q/Ia3ba52b7052cca528b033c2562f287a8c6b3f857))
- Always redirect to the right`HealthConnect`Client when requesting permissions on Android U.([I6415a](https://android-review.googlesource.com/#/q/I6415afb038718618e06d435a57624be7ad969f55))

### Version 1.1.0-alpha01

June 7, 2023

`androidx.health.connect:connect-client:1.1.0-alpha01`is released. This version is developed in an internal branch.
| **Note:** This version will only compile against the Android 14 (Upside Down Cake) Beta 1 SDK or higher.

**New Features**

- Support for the Android 14 framework version of Health Connect. This SDK is a prerequisite for Android 14. Apps will not be able to integrate with Health Connect on Android 14 without it.
- Added recording method to record metadata.

**API Changes**

- Session API changes:
  - Added various sleep stages into`SleepSessionRecord`and removed`SleepStageRecord`.
  - Added`ExerciseLap`and`ExerciseSegment`into`ExerciseSessionRecord`.
- Periodic and daily rate limits (including memory limits), for read, changelog, insertion and deletion operations.
- Added validation for all`NutritionRecord`fields.
- Added validation for`HeartRateVariabilityRmssdRecord`.
- Removed two deprecated APIs:`HealthConnectClient#isProviderAvailable`and`HealthConnectClient#isApiSupported`.

**Bug Fixes**

- Fixed units equality for all unit types, equality no longer depends on type used for unit initialization. E.g. Mass.grams(1000) is now equal to Mass.kilograms(1).

## Version 1.0

### Version 1.0.0-alpha11

February 22, 2023

`androidx.health.connect:connect-client:1.0.0-alpha11`is released.[Version 1.0.0-alpha11 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e5dad1e7d1c225f89f7c2d5a39a7a0de8d637d7b..87533b4ff06971ed59028936cd9b6da988cd4522/health/connect/connect-client)

**API Changes**

- Adding an intent to use for opening Health Connect. ([Ic8055](https://android-review.googlesource.com/#/q/Ic80557de25d163b45f1ea2bdd54efb9d6079a704))
- Removing some exercise types. Use`EXERCISE_TYPE_STRENGTH_TRAINING`,`EXERCISE_TYPE_HIGH_INTENSITY_INTERVAL_TRAINING`or`EXERCISE_TYPE_CALISTHENICS`in place of the removed types. ([I7291c](https://android-review.googlesource.com/#/q/I7291c98b7f6098cd5c6424e883bfee3c42b09a9a))
- Adding new API`sdkStatus()`that combines the two now deprecated APIs`isSdkSupported()`and`isProviderAvailable()`. ([Iac89d](https://android-review.googlesource.com/#/q/Iac89db1d65ca0147f7a724e8961f7f3b85e5b7b7))
- Changing APIs that accept`providerPackageName`to accept a single string rather than a list. ([I67e0f](https://android-review.googlesource.com/#/q/I67e0f12722d63acc4bc5ee41571b9c28e600b9eb))

### Version 1.0.0-alpha10

January 25, 2023

`androidx.health.connect:connect-client:1.0.0-alpha10`is released.[Version 1.0.0-alpha10 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/adf1c279a86ab3886e1666c08e2c3efba783367b..e5dad1e7d1c225f89f7c2d5a39a7a0de8d637d7b/health/connect/connect-client)

**API Changes**

- `ExerciseEventRecord`,`ExerciseLapRecord`,`ExerciseRepititionRecord`and`SwimmingStrokesRecord`are no longer supported as`RecordTypes`. They can no longer be written or read from`HealthConnect`. Remove any reference to these data types from the`HealthConnect`integration. ([If7ca2](https://android-review.googlesource.com/#/q/If7ca2475c91d472006d0a2304177f958d2f26cac))
- Changes in permissions APIs to accept permissions in a new string based format. This change also requires changing permission declaration to the standard android permissions format. ([Ib0a2f](https://android-review.googlesource.com/#/q/Ib0a2f8b61bfedf2d864de9c947fb4771b732ed50))

### Version 1.0.0-alpha09

January 11, 2023

`androidx.health.connect:connect-client:1.0.0-alpha09`is released.[Version 1.0.0-alpha09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4a2f5e696614339c1ac21f706c1a17c0285780e7..adf1c279a86ab3886e1666c08e2c3efba783367b/health/connect/connect-client)

**New Features**

- Added 2 new female health datatypes for Health Connect:`IntermenstrualBleedingRecord`, and`MenstruationPeriodRecord`.`MenstruationFlow.ENUMs`are Light, Medium, Heavy, and Unknown.

**API Changes**

- Added`IntermenstrualBleedingRecord`([Idc470](https://android-review.googlesource.com/#/q/Idc470d09a80f02a47d9a1691756e0fef8f6c6762))
- Added`MenstruationPeriodRecord`record type ([Iea545](https://android-review.googlesource.com/#/q/Iea5451c5ea60a9f3a2dff97023f85ad1d3197ba8))

### Version 1.0.0-alpha08

December 7, 2022

`androidx.health.connect:connect-client:1.0.0-alpha08`is released.[Version 1.0.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/548c8ac2570ae6cf15798fea1380491f7d93796b..4a2f5e696614339c1ac21f706c1a17c0285780e7/health/connect/connect-client)

**API Changes**

- Adds`BodyWaterMass`,`HeartRateVariabilityRmssdRecord`as new supported Record Types. ([Ifd58f](https://android-review.googlesource.com/#/q/Ifd58fa6924f83f155ca9c771d2cef67138caab1d))
- Removes`HipCircumferenceRecord`,`WaistCircumferenceRecord`as supported`RecordTypes`. ([I62fb9](https://android-review.googlesource.com/#/q/I62fb944fecb0916fd96e374351838d1d1c93c322))
- Changed`MenstruationFlowRecord.flow`from`stringdef`to`intdefs`. ([I0369f](https://android-review.googlesource.com/#/q/I0369f1dbd5f853311694347c63cb4504b4e8880c))
- Changed enum-like Record fields with`Strings`to`Integers`for better performance. ([I3b295](https://android-review.googlesource.com/#/q/I3b295be1c89cef14b37dd87d00c358450f37f430))
- Changed`ExerciseSession`,`ExerciseRepetitions`,`SleepStage`enum-like fields from string to integer types. ([Id32a9](https://android-review.googlesource.com/#/q/Id32a90d9b866dced5a1a6f1257d3176449873295))
- Renamed`ExerciseSessionRecord.ACTIVE_TIME_TOTAL->EXERCISE_DURATION_TOTAL`. ([I5d7bd](https://android-review.googlesource.com/#/q/I5d7bdc112ea601fb47e842b77d9a1d13dd480e3b))
- Adds "Unusual" to`CervicalMucus`enums. Rename "Clear" to "Eggwhite" for more specificity. Changed`CervicalMucus#appearance`and #sensation from`StringDefs`to IntDefs. ([I3ac51](https://android-review.googlesource.com/#/q/I3ac51c9583a1362030bad96b96e636a5c8e686f1))
- `StringDef`of`DeviceTypes`enum is now moved into`IntDefs`under Device. ([I3abf3](https://android-review.googlesource.com/#/q/I3abf324d8d734d614ad163131277d982d4d90946))
- Adds`HealthConnectClient.isApiSupported()`, which returns false on SDK versions with no compatible implementations. Renamed`HealthConnectClient.isAvailable->isProviderAvailable`. ([I3674e](https://android-review.googlesource.com/#/q/I3674ea3c306e2d58c37dc83fe17e966464313ada))

**Bug Fixes**

- Disallow`HeartRate beatsPerMinute`values less than 1 ([I6052f](https://android-review.googlesource.com/#/q/I6052fc98f475e137578f7d6e340795b61e66cdea))
- Adding`@JvmDefaultWithCompatibility`annotation ([I8f206](https://android-review.googlesource.com/#/q/I8f2067bb0754a5e9dc70c934403366ca8d319c36))

### Version 1.0.0-alpha07

October 24, 2022

`androidx.health.connect:connect-client:1.0.0-alpha07`is released.[Version 1.0.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4586cf6e518f0c59410ef2b291e34ff9fdcff4e1..548c8ac2570ae6cf15798fea1380491f7d93796b/health/connect/connect-client)

**API Changes**

- Record arguments without default values are placed before arguments with default values. For consistency,`Instant`and`ZoneOffset`arguments are always placed at the very beginning. ([Id618c](https://android-review.googlesource.com/#/q/Id618c2846792ea8c8a167eafa51ec6ddc8707722))
- Rename`HealthConnectClient.getOrCreate#packageNames`to`providerPackageNames`. ([Id81e4](https://android-review.googlesource.com/#/q/Id81e48f62b25453e4f2df9c84342c78011281eb1))

**Bug Fixes**

- Adds Record field value validations. Extremely wrong values will throw`IllegalArgumentExceptions`when provided value is out of reasonable bounds. ([Ie171d](https://android-review.googlesource.com/#/q/Ie171d9fb0b2692c2968d011ab1e889503c4b4728))
- Validates record start time before end time where relevant. ([I02460](https://android-review.googlesource.com/#/q/I02460111a49a792bdbe92accd0ba3c2ed89368fd))

### Version 1.0.0-alpha06

October 5, 2022

`androidx.health.connect:connect-client:1.0.0-alpha06`is released.[Version 1.0.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/96df3817383b33803b9d2220d7201f3b129b2464..4586cf6e518f0c59410ef2b291e34ff9fdcff4e1/health/connect/connect-client)

**Bug Fixes**

- Improves service connection lifecycle. ([If2bd5](https://android-review.googlesource.com/#/q/If2bd590a72b5490f76348e32726bdf2966279238))
- Fix an NPE crash bug when exception raised in service connection. ([I13546](https://android-review.googlesource.com/#/q/I13546e899cb4ed4370130c5c91d2713b507c93b8))

### Version 1.0.0-alpha05

September 21, 2022

`androidx.health.connect:connect-client:1.0.0-alpha05`is released.[Version 1.0.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/dd1e45e8550560087f6447a34a9145048b5766f4..6e22d4de9cd483fa47ac538bb7b562a39a7edbdf/health/connect/connect-client)

**API Changes**

- Renamed`Metadata.uid`-\>`Metadata.id`and used the terminology`recordId`consistently throughout related CRUD APIs. ([I3d1d2](https://android-review.googlesource.com/#/q/I3d1d20383132a36df0f8a19929965f3bf5ae00e6))
- Made`PermissionController.createRequestPermissionActivityContract`a static method instead of an instance method. Renamed to`PermissionController.createRequestPermissionResultContract`. ([Icd2fe](https://android-review.googlesource.com/#/q/Icd2feb117b6b14f0dae9cac36daa2f98daf44fef))
- Added`BloodGlucose`unit type for`BloodGlucoseRecord`([I97678](https://android-review.googlesource.com/#/q/I97678d2a35a06d6286c03fa685f5331933f371d7))
- Rename`MenstruationRecord`-\>`MenstruationFlowRecord`. ([I3b88e](https://android-review.googlesource.com/#/q/I3b88e57e099afc4b6ca86dc30550c06656555c65))

**Bug Fixes**

- Fix unintended behavior not propagating foreground stats from client process. ([Ifb44c](https://android-review.googlesource.com/#/q/Ifb44cb3a338d07d5944547c76fc5b290dd1ad089))

### Version 1.0.0-alpha04

August 24, 2022`androidx.health.connect:connect-client:1.0.0-alpha04`is released.[Version 1.0.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/dd1e45e8550560087f6447a34a9145048b5766f4/health/connect/connect-client)

**Migration to \`androidx.health.connect**

As of 1.0.0-alpha04,`androidx.health:health-connect-client`was migrated to`androidx.health.connect:connect-client`. For previous versions of Health Connect, please visit the[androidx.health](https://developer.android.com/jetpack/androidx/releases/health#health-connect-client-1.0.0-alpha04)page.

To migrate, simply change your dependency import from`androidx.health:health-connect-client:1.0.0-alpha03`to`androidx.health.connect:connect-client:1.0.0-alpha04`.

**New Features**

- Included optional debug logs builtin for API calls ([link](https://android-review.googlesource.com/c/platform/frameworks/support/+/2168135))

**API Changes**

- Renamed Metadata`clientId`to`clientRecordId`,`clientVersion`to`clientRecordVersion`. ([link](https://android-review.googlesource.com/c/platform/frameworks/support/+/2183441))
- Made Metadata uid more friendly to readers, no longer nullable. ([link](https://android-review.googlesource.com/c/platform/frameworks/support/+/2127532))
- Added pounds to Mass unit ([link](https://android-review.googlesource.com/c/platform/frameworks/support/+/2179438))
- Renamed`DeletionChange.deleteUid`to uid ([link](https://android-review.googlesource.com/c/platform/frameworks/support/+/2165064))
- Rename Permission -\> HealthPermission. This avoids ambiguity with Android Framework permissions. ([link](https://android-review.googlesource.com/c/platform/frameworks/support/+/2143892))

**Bug Fixes**

- Fixed regression issues with incorrect calories unit with Energy ([link](https://android-review.googlesource.com/c/platform/frameworks/support/+/2179435))
- Fixed regression issue with aggregation for few record types ([link](https://android-review.googlesource.com/c/platform/frameworks/support/+/2170323))