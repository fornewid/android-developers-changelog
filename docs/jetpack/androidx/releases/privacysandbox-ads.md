---
title: https://developer.android.com/jetpack/androidx/releases/privacysandbox-ads
url: https://developer.android.com/jetpack/androidx/releases/privacysandbox-ads
source: md.txt
---

# privacysandbox ads

# privacysandbox ads

API Reference  
[androidx.privacysandbox.ads.adservices.adid](https://developer.android.com/reference/kotlin/androidx/privacysandbox/ads/adservices/adid/package-summary)  
[androidx.privacysandbox.ads.adservices.adselection](https://developer.android.com/reference/kotlin/androidx/privacysandbox/ads/adservices/adselection/package-summary)  
[androidx.privacysandbox.ads.adservices.appsetid](https://developer.android.com/reference/kotlin/androidx/privacysandbox/ads/adservices/appsetid/package-summary)  
[androidx.privacysandbox.ads.adservices.common](https://developer.android.com/reference/kotlin/androidx/privacysandbox/ads/adservices/common/package-summary)  
[androidx.privacysandbox.ads.adservices.customaudience](https://developer.android.com/reference/kotlin/androidx/privacysandbox/ads/adservices/customaudience/package-summary)  
[androidx.privacysandbox.ads.adservices.measurement](https://developer.android.com/reference/kotlin/androidx/privacysandbox/ads/adservices/measurement/package-summary)  
[androidx.privacysandbox.ads.adservices.topics](https://developer.android.com/reference/kotlin/androidx/privacysandbox/ads/adservices/topics/package-summary)  
This library enables integration with Privacy Preserving APIs, which are part of Privacy Sandbox on Android.  

| Latest Update | Stable Release | Release Candidate |                                              Beta Release                                               | Alpha Release |
|---------------|----------------|-------------------|---------------------------------------------------------------------------------------------------------|---------------|
| May 7, 2025   | -              | -                 | [1.1.0-beta13](https://developer.android.com/jetpack/androidx/releases/privacysandbox-ads#1.1.0-beta13) | -             |

## Declaring dependencies

To add a dependency on privacysandbox-ads, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
 
    implementation "androidx.privacysandbox.ads:ads-adservices:1.1.0-beta13"
   
    implementation "androidx.privacysandbox.ads:ads-adservices-java:1.1.0-beta13"
 
}
```

### Kotlin

```kotlin
dependencies {

    implementation("androidx.privacysandbox.ads:ads-adservices:1.1.0-beta13")

    implementation "androidx.privacysandbox.ads:ads-adservices-java:1.1.0-beta13"
   
}
```

For more information about dependencies, see[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:1300620+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1300620&template=1773865)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.1

### Version 1.1.0-beta12

March 12, 2025

`androidx.privacysandbox.ads:ads-adservices:1.1.0-beta12`and`androidx.privacysandbox.ads:ads-adservices-java:1.1.0-beta12`are released. Version 1.1.0-beta12 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/ccd90a76bd7c4acf4f4f01eca76350e383bc441e..7a145e052ae61e272e91ffe285e9451b8ab71870/privacysandbox/ads).

**New Features**

- Custom Audience Priority: We have added a priority field in the custom audience. This allows buyers to specify a priority value in a`CustomAudience`. This value would be used to identify custom audiences which should be included in an auction if the set of buyer custom audiences exceed the per-buyer size limits
- Seller Configuration: This feature allows sellers to define auction parameters to control payload size and auction participants. The seller auction configuration would allow sellers to specify:
  - Allowed buyer list
  - For auctions initiated by the given seller, only the buyers in the allowlist would be able to contribute`CustomAudiences`for the auction
  - Per-buyer size limit
  - Sellers could specify a per-buyer limit to regulate the data size uploaded by each buyer into the payload being sent to`SellerFrontendService`. If the buyer exceeds the per-buyer size limit, the`CustomAudience`priority set in buyer payload configuration would be used to get the data in the expected limits.
  - Max size limit for the payload
  - Different sellers might have different resource allocation and might want to set a max size limit for the per-request auction payload. The max size limit would respect the fixed size buckets set by the`ProtectedAudience`API.
- Delayed Custom Audience Updates: This feature enables buyers to schedule deferred updates for Custom Audiences. Each update request allows the caller to schedule a delayed update using the new`scheduleCustomAudienceUpdate()`API. For each update, the user can specify sets of Custom Audiences to join or leave.

**API Changes**

- Add Seller Configuration in`GetAdSelectionRequest`API ([Ibb5c7](https://android-review.googlesource.com/#/q/Ibb5c7779ed444054b54552adf727597b7c31998f))
- Introduce`ScheduleCustomAudienceUpdate`API as experimental ([I6b905](https://android-review.googlesource.com/#/q/I6b905a319902f77eed2a43e9f8a574f1e76a7429))

### Version 1.1.0-beta11

October 30, 2024

`androidx.privacysandbox.ads:ads-adservices:1.1.0-beta11`and`androidx.privacysandbox.ads:ads-adservices-java:1.1.0-beta11`are released. Version 1.1.0-beta11 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/8c4071562bd7e22b937284d71fb7aca9c4cd662c..ccd90a76bd7c4acf4f4f01eca76350e383bc441e/privacysandbox/ads).

**New Features**

- This update removes support for privacysandbox measurement and adid APIs on Android R, which has been deprecated. Calls to get the manager classes on Android R will now return null.

### Version 1.1.0-beta10

August 21, 2024

`androidx.privacysandbox.ads:ads-adservices:1.1.0-beta10`and`androidx.privacysandbox.ads:ads-adservices-java:1.1.0-beta10`are released. Version 1.1.0-beta10 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/56579bc30499ce39f0d7a6713a065b00c6194206..8c4071562bd7e22b937284d71fb7aca9c4cd662c/privacysandbox/ads).

**API Changes**

- Add missing Java constructor overloads for`GetAdSelectionDataOutcome`,`PersistAdSelectionResultRequest`,`ReportEventRequest`, and`FetchAndJoinCustomAudienceRequest`Experimental APIs. ([I19e7f](https://android-review.googlesource.com/#/q/I19e7fe6208ed53e81895261716385db1bd24ccc5))

### Version 1.1.0-beta09

July 10, 2024

`androidx.privacysandbox.ads:ads-adservices:1.1.0-beta09`and`androidx.privacysandbox.ads:ads-adservices-java:1.1.0-beta09`are released. Version 1.1.0-beta09 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/948119be341fa4affc055418e695d8c4c7e5e2e4..56579bc30499ce39f0d7a6713a065b00c6194206/privacysandbox/ads).

**API Changes**

- Add missing Java constructor overloads for`GetAdSelectionDataRequest`Experimental API. ([Ifbf88](https://android-review.googlesource.com/#/q/Ifbf88b1b7a189585e15c04c8a111594c74ec6278)).

### Version 1.1.0-beta08

June 26, 2024

`androidx.privacysandbox.ads:ads-adservices:1.1.0-beta08`and`androidx.privacysandbox.ads:ads-adservices-java:1.1.0-beta08`are released. Version 1.1.0-beta08 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/6a69101fd0edc8d02aa316df1f43e0552fd2d7c4..948119be341fa4affc055418e695d8c4c7e5e2e4/privacysandbox/ads).

**New Features**

- Added support for protected app signals.
- Support multiple cloud providers for B\&A server auctions.

**API Changes**

- Experimental API`GetAdSelectionDataRequest::seller`is non-nullable. ([I68044](https://android-review.googlesource.com/#/q/I680448540a29283fe627ec191d8b30585edc293c))
- Add`GetAdSelectionDataRequest::coordinatorOriginUri`Experimental API. ([I18c0b](https://android-review.googlesource.com/#/q/I18c0bd8074a5366a2c2ab03e789da395abe29790))
- Added`updateSignals`API. ([Ia8512](https://android-review.googlesource.com/#/q/Ia8512411048824718f8e0acce00607a1deb3fb3c))

### Version 1.1.0-beta07

May 14, 2024

`androidx.privacysandbox.ads:ads-adservices:1.1.0-beta07`and`androidx.privacysandbox.ads:ads-adservices-java:1.1.0-beta07`are released. Version 1.1.0-beta07 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/67004410fdbff19f90caa4cc43965ab21dca1943..6a69101fd0edc8d02aa316df1f43e0552fd2d7c4/privacysandbox/ads).

**New Features**

- `GetTopics`now supports encrypted responses as part of`GetTopicsResponse`.

**API Changes**

- Added`EncryptedTopic`to`GetTopicResponse`class. ([Iab362](https://android-review.googlesource.com/#/q/Iab3629f5572e21640c0d92d64d7464de36164e16))

### Version 1.1.0-beta06

April 17, 2024

`androidx.privacysandbox.ads:ads-adservices:1.1.0-beta06`and`androidx.privacysandbox.ads:ads-adservices-java:1.1.0-beta06`are released. Version 1.1.0-beta06 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/02b55f664eba38e42e362e1af3913be1df552d55..67004410fdbff19f90caa4cc43965ab21dca1943/privacysandbox/ads).

**Note**

- As of privacysandbox-ads jetpack release 1.1.0-beta06, all flags-enabled Android R devices will be able to access the PPAPIs. For any use case that should not support Android R, additional guards will be required within the code using privacysandbox-ads jetpack code.

**New Features**

- Backward compatibility support for Android R.

### Version 1.1.0-beta05

April 3, 2024

`androidx.privacysandbox.ads:ads-adservices:1.1.0-beta05`and`androidx.privacysandbox.ads:ads-adservices-java:1.1.0-beta05`are released. Version 1.1.0-beta05 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/fbeccfb9423a7b810c9d248da7ddae2860bcffdc..02b55f664eba38e42e362e1af3913be1df552d55/privacysandbox/ads).

**Bug Fixes**

- Added error catching when a class definition is not found on Android S devices due to missing uses-library tag in manifest.

### Version 1.1.0-beta04

January 24, 2024

`androidx.privacysandbox.ads:ads-adservices:1.1.0-beta04`and`androidx.privacysandbox.ads:ads-adservices-java:1.1.0-beta04`are released.[Version 1.1.0-beta04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/15b45436d846a1cbb8f82f449405f97a8a19839a..fbeccfb9423a7b810c9d248da7ddae2860bcffdc/privacysandbox/ads)

**New Features**

- New API to support post-auction user event reporting
- Added support for Frequency cap filtering for remarketing ads
- Supporting Join Custom Audience delegation
- Waterfall mediation chain truncation support
- Support for Protected Auctions on Bidding and Auction Servers

**API Changes**

- Introduce`AdSelectionManager::selectAds(AdSelectionFromOutcomesConfig)`experimental API ([I86cd2](https://android-review.googlesource.com/#/q/I86cd2b0124d0b7702629a738672f0772472f0755))
- Introduce`ReportEventRequest::inputEvent`experimental API ([Ib94f3](https://android-review.googlesource.com/#/q/Ib94f3c25c2be855eb2491d158de442516ab3a8d1))
- Make`ReportImpressionRequest::adSelectionConfig`optional ([Ief280](https://android-review.googlesource.com/#/q/Ief280f27af7c7dc591f4e5c5a7cab9f0363be248))
- Introduce`AdSelectionManager::getAdSelectionData`and`AdSelectionManager::persistAdSelectionResultUnified`experimental APIs ([Ie4d0e](https://android-review.googlesource.com/#/q/Ie4d0e1e8aee708527be9a40594953d48ae737805))
- Introduce`CustomAudienceManager::fetchAndJoinCustomAudience`experimental API ([I09152](https://android-review.googlesource.com/#/q/I09152828d72b3eaef8e32854d7d0398d9daaca37))
- Introduce`AdSelectionManager::reportEvent`experimental API ([I0d7dc](https://android-review.googlesource.com/#/q/I0d7dca4f20cb1f8fcb0f090d8c609af645c7eebd))
- Introduced`AdSelectionManager::updateAdCounterHistogram`experimental API and altered`AdData`to indicate a series of`AdFilters`([I87b83](https://android-review.googlesource.com/#/q/I87b83101d35af061615dd3c2dc56ef637d6ad8e6))

**Bug Fixes**

- Input URIs are now matched on a shared site/origin instead of requiring an exact host name match.
- Fix test failing due to missing HTTPS scheme ([d573058](https://android.googlesource.com/platform/frameworks/support/+/d5730580dc99b73564afe2ab7de1ca378e07dcaa))
- Fix missing HTTPS scheme from web URLs ([cecdcb8](https://android.googlesource.com/platform/frameworks/support/+/cecdcb80bbb238b41b218083cc4d6f836918f335))
- Add throws annotation to the measurement APIs ([2dba359](https://android.googlesource.com/platform/frameworks/support/+/2dba359ce37ce3db7670a1324d81d5b3f5aacb65))

### Version 1.1.0-beta03

November 15, 2023

`androidx.privacysandbox.ads:ads-adservices:1.1.0-beta03`and`androidx.privacysandbox.ads:ads-adservices-java:1.1.0-beta03`are released.[Version 1.1.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1f7407d4293384a1b91bc142880e3525048b3443..15b45436d846a1cbb8f82f449405f97a8a19839a/privacysandbox/ads)

**New Features**

- Backward compatibility support for Android S.

### Version 1.1.0-beta02

October 4, 2023

`androidx.privacysandbox.ads:ads-adservices:1.1.0-beta02`and`androidx.privacysandbox.ads:ads-adservices-java:1.1.0-beta02`are released.[Version 1.1.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3315f1ef094c312203fe26841287902916fbedf5..1f7407d4293384a1b91bc142880e3525048b3443/privacysandbox/ads)

**API Changes**

- Removed T+ version check from measurement request classes. Clients do not need a T+ platform version check on their side to access the privacysandbox`MeasurementManager`request classes.[MeasurementManager](https://developer.android.com/reference/androidx/privacysandbox/ads/adservices/java/measurement/MeasurementManagerFutures#from(android.content.Context))will be null with the new behaviour. ([Ieb105](https://android-review.googlesource.com/#/q/Ieb105c82e5dbca17e1acec722171a6dc04adbf66))

### Version 1.1.0-beta01

August 23, 2023

`androidx.privacysandbox.ads:ads-adservices:1.1.0-beta01`and`androidx.privacysandbox.ads:ads-adservices-java:1.1.0-beta01`are released with no changes.[Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5d7dd999525725bd038a00ca4e89e0fef624a6da..3315f1ef094c312203fe26841287902916fbedf5/privacysandbox/ads)

### Version 1.1.0-alpha01

August 9, 2023

`androidx.privacysandbox.ads:ads-adservices:1.1.0-alpha01`and`androidx.privacysandbox.ads:ads-adservices-java:1.1.0-alpha01`are released.[Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/73f902dee011bfe400d8a0330bfd8d4bb632065f..5d7dd999525725bd038a00ca4e89e0fef624a6da/privacysandbox/ads)

**API Changes**

- Introduce`registerSource`list ([Iae92f](https://android-review.googlesource.com/#/q/Iae92f73b77d4a69b51a7db9e4f355e77d9770491))
- Removed usages of experimental`isAtLeastU()`API ([Ie9117](https://android-review.googlesource.com/#/q/Ie9117598f70e8873011f98ebbe0e6cd502772c87),[b/289269026](https://issuetracker.google.com/issues/289269026))

**Bug Fixes**

- Merge experimental and public API files ([I15da3](https://android-review.googlesource.com/#/q/I15da3600327c59450a55d78e37d4ae0157e277bb),[b/278769092](https://issuetracker.google.com/issues/278769092))

## Version 1.0

### Version 1.0.0-beta05

June 7, 2023

`androidx.privacysandbox.ads:ads-adservices:1.0.0-beta05`and`androidx.privacysandbox.ads:ads-adservices-java:1.0.0-beta05`are released.[Version 1.0.0-beta05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6f3ac2bd197d5e61ab2708125b57d6ae4003ad68..73f902dee011bfe400d8a0330bfd8d4bb632065f/privacysandbox/ads)

**Bug Fixes**

- Adds an sdk extension 5 check to`TopicsManager`
- Bumps Kotlin coroutines dependency to 1.7.1 to prevent duplicate class build errors in gradle

### Version 1.0.0-beta04

May 10, 2023

`androidx.privacysandbox.ads:ads-adservices:1.0.0-beta04`and`androidx.privacysandbox.ads:ads-adservices-java:1.0.0-beta04`are released.[Version 1.0.0-beta04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/01bd392d5702480f8bfe61a8f8bbbea64cf362a0..6f3ac2bd197d5e61ab2708125b57d6ae4003ad68/privacysandbox/ads)

**Bug Fixes**

- Resolve deadlock issue when adservices measurement APIs are invoked on main thread by the caller. ([I65361](https://android.googlesource.com/platform/frameworks/support/+/83d25e40e2dccb98fa65a9bc3bc5b8efc9f820cb))

### Version 1.0.0-beta03

April 19, 2023

`androidx.privacysandbox.ads:ads-adservices:1.0.0-beta03`and`androidx.privacysandbox.ads:ads-adservices-java:1.0.0-beta03`are released.[Version 1.0.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5e7d256f82fbafb6d059ab7b18fddd87c7531553..01bd392d5702480f8bfe61a8f8bbbea64cf362a0/privacysandbox/ads)

**New Features**

- Enabled Preview API for Topics.

### Version 1.0.0-beta02

March 22, 2023

`androidx.privacysandbox.ads:ads-adservices:1.0.0-beta02`and`androidx.privacysandbox.ads:ads-adservices-java:1.0.0-beta02`are released.[Version 1.0.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/905b302ac8f059ed625383676c68ee4bf78e07da..59c835714673e6432bd1ccd1d6b4742cec3c7a9f/privacysandbox/ads)

**Bug Fixes**

- Enabled the`MeasurementManager`APIs for SDK Extension version 5 and above.
- Disabled the`MeasurementManager`APIs for SDK Extension version 4 and below.

### Version 1.0.0-beta01

February 22, 2023

`androidx.privacysandbox.ads:ads-adservices:1.0.0-beta01`and`androidx.privacysandbox.ads:ads-adservices-java:1.0.0-beta01`are released with no notable changes. Version 1.0.0-beta01 was released from an internal branch.

**Behavior Changes**

- Attribution Reporting has been disabled and is not available for use in this release.

### Version 1.0.0-alpha01

January 11, 2023

`androidx.privacysandbox.ads:ads-adservices:1.0.0-alpha01`and`androidx.privacysandbox.ads:ads-adservices-java:1.0.0-alpha01`are released. Version 1.0.0-alpha01 was released from an internal branch.

- This is a new Jetpack library that enables integration with Privacy Sandbox's Privacy Preserving APIs ([Topics](https://developer.android.com/design-for-safety/privacy-sandbox/guides/topics),[FLEDGE](https://developer.android.com/design-for-safety/privacy-sandbox/guides/fledge)and[Attribution Reporting](https://developer.android.com/design-for-safety/privacy-sandbox/guides/attribution)).
- The Jetpack Privacy Sandbox APIs can be used as a drop-in replacement for the Privacy Sandbox APIs provided in the[Extension SDK 4](https://developer.android.com/guide/sdk-extensions).