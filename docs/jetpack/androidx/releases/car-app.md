---
title: https://developer.android.com/jetpack/androidx/releases/car-app
url: https://developer.android.com/jetpack/androidx/releases/car-app
source: md.txt
---

# Car App

# Car App

[User Guide](https://developer.android.com/training/cars)[Code Sample](https://github.com/android/car-samples)[Codelab](https://developer.android.com/codelabs/car-app-library-fundamentals)  
API Reference  
[androidx.car.app](https://developer.android.com/reference/kotlin/androidx/car/app/package-summary)  
[androidx.car.app.model](https://developer.android.com/reference/kotlin/androidx/car/app/model/package-summary)  
[androidx.car.app.navigation](https://developer.android.com/reference/kotlin/androidx/car/app/navigation/package-summary)  
[androidx.car.app.notification](https://developer.android.com/reference/kotlin/androidx/car/app/notification/package-summary)  
[androidx.car.app.serialization](https://developer.android.com/reference/kotlin/androidx/car/app/serialization/package-summary)  
[androidx.car.app.validation](https://developer.android.com/reference/kotlin/androidx/car/app/validation/package-summary)  
[androidx.car.app.versioning](https://developer.android.com/reference/kotlin/androidx/car/app/versioning/package-summary)  
Build templated apps for Android Auto and Android Automotive OS.  

|   Latest Update   |                                 Stable Release                                 | Release Candidate | Beta Release |                                         Alpha Release                                          |
|-------------------|--------------------------------------------------------------------------------|-------------------|--------------|------------------------------------------------------------------------------------------------|
| November 19, 2025 | [1.7.0](https://developer.android.com/jetpack/androidx/releases/car-app#1.7.0) | -                 | -            | [1.8.0-alpha03](https://developer.android.com/jetpack/androidx/releases/car-app#1.8.0-alpha03) |

## Declaring dependencies

To add a dependency on the Car App Library, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    implementation "androidx.car.app:app:1.7.0"

    // For Android Auto specific functionality
    implementation "androidx.car.app:app-projected:1.7.0"

    // For Android Automotive specific functionality
    implementation "androidx.car.app:app-automotive:1.7.0"

    // For testing
    testImplementation "androidx.car.app:app-testing:1.7.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.car.app:app:1.7.0")

    // For Android Auto specific functionality
    implementation("androidx.car.app:app-projected:1.7.0")

    // For Android Automotive specific functionality
    implementation("androidx.car.app:app-automotive:1.7.0")

    // For testing
    testImplementation("androidx.car.app:app-testing:1.7.0")
}
```

For more information about dependencies, see[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:460472+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=460472&template=1554359)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.8

### Version 1.8.0-alpha03

November 19, 2025

`androidx.car.app:app-*:1.8.0-alpha03`is released. Version 1.8.0-alpha03 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/e8af6ab7417811bf386c52a59ab5d0b94d194eeb..4d752a0684fb1bf991cd0d15ebd3649ee8684ca1/car/app).

**New Features**

- Added an Image to Rows, which enables new list use cases.
- Add`SectionedItemTemplate#alphabeticalIndexingStrategy`to allow different alphabetic indexing for list accelerators.

**API Changes**

- Added an`endImageType`for`endImages`in Rows ([I8865b](https://android-review.googlesource.com/#/q/I8865bd1f704f3c58dcf865f3bf827c1fd2c69b41))
- Add`SectionedItemTemplate#alphabeticalIndexingStrategy`. This is a replacement to`#isAlphabeticalIndexingAllowed`and gives developers more options for alphabetical indexing. ([Ia164d](https://android-review.googlesource.com/#/q/Ia164dd88866ec0c8caf99bb5f61b8e0721851a1c),[b/410092683](https://issuetracker.google.com/issues/410092683))
- Add support for an end Image to a car app Row. ([If93f0](https://android-review.googlesource.com/#/q/If93f0ed10b30a90f597c246823a41dee9b87f9c2))
- Added`CarIcon MediaPlayback`to simplify use of standard action`MediaPlayback`. ([Ib6cb7](https://android-review.googlesource.com/#/q/Ib6cb7469c686b3730642d305e95001420133bb9f))

**Bug Fixes**

- Moving the default`minSdk`from API 21 to API 23 ([Ibdfca](https://android-review.googlesource.com/#/q/Ibdfca5942dbb414ca07594ba240093db14aad4df),[b/380448311](https://issuetracker.google.com/issues/380448311),[b/435705964](https://issuetracker.google.com/issues/435705964),[b/435705223](https://issuetracker.google.com/issues/435705223))

### Version 1.8.0-alpha02

June 18, 2025

`androidx.car.app:app-*:1.8.0-alpha02`is released. Version 1.8.0-alpha02 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/cd41781824511ce4d5c4a05d2df4aaaee669f0bc..e8af6ab7417811bf386c52a59ab5d0b94d194eeb/car/app).

**New Features**

- Added support for`Action.MEDIA_PLAYBACK`which displays an indicator based on media playback state.
- Added support for controlling a user's scroll position upon refresh of the`SectionedItemTemplate`.

**API Changes**

- Add support for saving a user's scroll position within the`SectionedItemTemplate`between refreshes. ([Ia4c51](https://android-review.googlesource.com/#/q/Ia4c51896708926b206214e45227efcff683f8eef))
- Updated`MEDIA_PLAYBACK`action to enable it for row end action ([I05cc4](https://android-review.googlesource.com/#/q/I05cc4575be8484199e48445fabc64874a32ebce0))
- Add a new action type ([I6cc5a](https://android-review.googlesource.com/#/q/I6cc5a4314f378b06deaf7dedaf58cb511786cf07))
- Add`CarAppExtender#addAction(Action)`so that any type of action can be added to the`CarAppExtender`. ([Idc4d7](https://android-review.googlesource.com/#/q/Idc4d77b7c3fa2b154786a30de75dc7b799de0841))
- Made`SectionedItemTemplate`accessible for API 8 and above. ([I9a079](https://android-review.googlesource.com/#/q/I9a079a969cfb396d9b48c6a51bfcdf8d837dee7f))

### Version 1.8.0-alpha01

May 20, 2025

`androidx.car.app:app-*:1.8.0-alpha01`is released. Version 1.8.0-alpha01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/77659d22ebee60efbb441aaec2e91b529f6a4329..cd41781824511ce4d5c4a05d2df4aaaee669f0bc/car/app).

**New Features**

All capabilities are temporarily only available on Android Auto. The same API's will be leveraged across AAOS

- Added Media category to create custom application, as an alternative to`MediaBrowse`based ones
- Added Playback Template which allows to control the top actions during in Media Playback View (only available to Media apps)
- Added full support for Sectioned Item Template on Android Auto, which allows combinations of sub-sections made of Lists/Grids.
- Added Extra-Large as an additional size for Grid Items.

**API Changes**

- Add an extra size option for Grid items ([I35b58](https://android-review.googlesource.com/#/q/I35b58fdfcc1c9d1aee536ac9c8557942cfc79a21))
- Adds category and permission for media apps to Car App Library ([I8e100](https://android-review.googlesource.com/#/q/I8e10065cd0452a7f1842def68816df7287d19834))
- Added new api for apps to detect whether the`CarAppLibrary`media category is supported ([Ic4b08](https://android-review.googlesource.com/#/q/Ic4b08492bbe06ab94b27407c204d9cb7fd9ef240))
- Added`OnItemVisibilityChangeListener`to Section. ([I2c2fd](https://android-review.googlesource.com/#/q/I2c2fd79fbc1d254b4b93d590b606d185acd749ad))
- Added`Mileage#getOdometerKilometers`and deprecate`Mileage#getOdometerMeters`([Ic91af](https://android-review.googlesource.com/#/q/Ic91afc7a4ff0e1c93a51aa67f044aa1c61ac9d89))

**Bug Fixes**

- Fix typo in Javadoc of`CarIcon.setTint`([Iabd72](https://android-review.googlesource.com/#/q/Iabd72cd9290a4376b4a3a104c944e169bd456d76))
- Updated`Row.Builder#setNumericDecoration`documentation to reflect how 1 action + numeric decoration is not supported; however 0 or 2 actions + numeric decoration is. ([Ic0b08](https://android-review.googlesource.com/#/q/Ic0b081cb0df33827104d9b14a3cf09875bedc662))
- Added field for badge icon background color for grid items. ([I2b6ae](https://android-review.googlesource.com/#/q/I2b6ae41a27a399e849917412cab812cc707a393a))

## Version 1.7

### Version 1.7.0

July 16, 2025

`androidx.car.app:app-*:1.7.0`is released. Version 1.7.0 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/77659d22ebee60efbb441aaec2e91b529f6a4329..dd0029781d89efa8a4e0cde206734e5ebef5f6ec/car/app).

- This is the first stable release that includes the fix for[CVE-2024-10382](https://www.cve.org/cverecord?id=CVE-2024-10382)patched on beta03. If you are using a lower version than 1.7-beta03, please update to use this version.

### Version 1.7.0-rc01

January 15, 2025

`androidx.car.app:app-*:1.7.0-rc01`is released with no notable changes from beta03. Version 1.7.0-rc01 is a contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/6c15cce3eea03b52bcfe2b5921f930096a8929e5..77659d22ebee60efbb441aaec2e91b529f6a4329/car/app).

- This is the first RC that includes the fix for[CVE-2024-10382](https://www.cve.org/cverecord?id=CVE-2024-10382)patched on beta03. If you are using a lower version than 1.7-beta03, please update to use this version.

### Version 1.7.0-beta03

November 13, 2024

Fixed a security vulnerability and other general bug fixes. If you are using a lower version,**please update to use this version**.

`androidx.car.app:app-*:1.7.0-beta03`is released. Version 1.7.0-beta03 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/0431b84980e97d6bafdfda7c9038bc4d9529564f..6c15cce3eea03b52bcfe2b5921f930096a8929e5/car/app).

**API Changes**

- Update CAL Serialization / De-serialization code to only handle objects which have the annotation`@CarProtocol`declared on them. ([Ic730e](https://android-review.googlesource.com/#/q/Ic730e341d18c7ec2525ad8d5a4f1123380c251d1))
- `CarAppExtender`can now be used to extend the framework`Notification.Builder`instead of only`NotificationCompat.Builder`. ([Id3ad7](https://android-review.googlesource.com/#/q/Id3ad735f9de699c6a6d69bdd2349f4920570c4b4))
- Add`KEY_EXCLUDE_MEDIA_ITEM_FROM_MIXED_APP_LIST`extra. ([I201f9](https://android-review.googlesource.com/#/q/I201f987a71848357e031af899f145918b56a1c1a))
- Deprecate the empty Builder constructor on`ConversationItem`and replace it with a constructor that takes required parameters. Also adds a check to guard against null messages. ([Ic8221](https://android-review.googlesource.com/#/q/Ic8221e2ad26bf3165cfa985347d7a63bb20fb4b0))

**Bug Fixes**

- Ensure`PlaceList`map uses string (Text-only) Header title. ([Ic992f](https://android-review.googlesource.com/#/q/Ic992f3574d5e4be1c8c2319472b1d667c3c50ad4))
- This library now uses[JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler argument to enforce correct usage:`-Xjspecify-annotations=strict`(this is the default starting with version 2.1.0 of the Kotlin compiler). ([Ib5367](https://android-review.googlesource.com/#/q/Ib5367ca20eb37c80c0f2d51c8682e81eda1f9a2a),[b/326456246](https://issuetracker.google.com/issues/326456246))

### Version 1.7.0-beta02

September 18, 2024

`androidx.car.app:app-*:1.7.0-beta02`is released. Version 1.7.0-beta02 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/948119be341fa4affc055418e695d8c4c7e5e2e4..0431b84980e97d6bafdfda7c9038bc4d9529564f/car/app).

**API Changes**

- Add`KEY_ROOT_HINT_MEDIA_HOST_VERSION`extra ([I8796b](https://android-review.googlesource.com/#/q/I8796b6a140e35fadd7731d80d82310500b42bc3c))
- Replace`TabContents.Api8Builder`class with`@ExperimentalCarApi`constructor in`TabContents.Builder`class ([I26fbe](https://android-review.googlesource.com/#/q/I26fbef0a1f3fc21a72557288e30efef50b61902b))
- Add intent action and extras for`CarMediaApp`([I50782](https://android-review.googlesource.com/#/q/I50782ebd51bb3e39ea96c95929e35fbea49427a5))
- Mark messaging APIs as non-experimental ([I0b070](https://android-review.googlesource.com/#/q/I0b0700c03fe032f433db8e3de4bb0b4c8867948d))
- Add remote item loading to`SectionedItemTemplate`(allows long lists to load without crashing) ([I0d122](https://android-review.googlesource.com/#/q/I0d122185a54a70a5eddb709e422ad958b594f449))
- Add`SectionedItemTemplate`to list of supported templates inside`TabTemplate`in API 8. ([Idc5d6](https://android-review.googlesource.com/#/q/Idc5d69119989929448c6125235b8b206adf530ba))

**Bug Fixes**

- Removed manual outlining of access to new platform APIs since this happens automatically via API modeling when using R8 with AGP 7.3 or later (e.g. R8 version 3.3) and for all builds when using AGP 8.1 or later (e.g. D8 version 8.1). Clients who are not using AGP are advised to update to D8 version 8.1 or later. See[this article](https://medium.com/androiddevelopers/mitigating-soft-verification-issues-in-r8-and-d8-7e9e06827dfd)for more details. ([I9496c](https://android-review.googlesource.com/#/q/I9496cfaeb50a5c484fbee6521b74a0605fb013dc),[b/345472586](https://issuetracker.google.com/issues/345472586))

### Version 1.7.0-beta01

June 26, 2024

`androidx.car.app:app-*:1.7.0-beta01`is released. Version 1.7.0-beta01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/5c17ac8d339b80b5f509f83792f5923e337612c7..948119be341fa4affc055418e695d8c4c7e5e2e4/car/app). Features are the same as published in alpha01, which are repeated below:

**New Features**

- *Map with Content:* New template a Map Canvas plus a content template, which for now can be List / Grid / Pane / Message.
  - `RoutePreview`,`PlaceListNavigation`,`MapTemplate`are now deprecated. Templates will continue to work as-is.
  - Sample apps have been updated to show`MapWithContent`usage instead of deprecated templates
- *Conversation Item:*New APIs for displaying conversations (IM, SMS), and Assistant readout in the car.
- *Vehicle Dimensions:*New API to retrieve vehicle measures (data on AAOS at the moment).

**API Changes**

- Add`@ExperimentalCarApi`tag to`MediaPlaybackTemplate.Builder`. ([Ic1957](https://android-review.googlesource.com/#/q/Ic195773f56a9f10234f232413b72404f95434ec6))
- Adds a new`SectionedItemTemplate`in experimental. ([I5958a](https://android-review.googlesource.com/#/q/I5958aaacf42d05e9a28774f2c2b468a0c6d8c6de))
- Introduce`CarAppApiLevel 8`([I3fa22](https://android-review.googlesource.com/#/q/I3fa220efd1382a4d0146f58f505991e55163ba44))
- Adds`MediaPlaybackTemplate`for displaying content during media playback in Car App Library. ([I3c10d](https://android-review.googlesource.com/#/q/I3c10d979e8fbf2f9240fad946bc42220cda2ac4b))
- Added new api for apps to detect whether the system supports background audio while driving ([I0f868](https://android-review.googlesource.com/#/q/I0f868508078908bd80f8fd013ce8847dcd3844aa))

**Bug Fixes**

- Fixes certain instances of memory leaks and crashes in CAL client code and in CAL Navigation Sample App. ([I55e04](https://android-review.googlesource.com/#/q/I55e04addc90298c44103806ae5c4de681a2506cf))
- Replace`requireNotNull instances`in`BaseCarAppActivity`'s`onDestroy`method with if-null checks to avoid crashes. ([Iec676](https://android-review.googlesource.com/#/q/Iec6767110cf8839cb57b71cdc31444b6124a6950))

### Version 1.7.0-alpha02

April 17, 2024

`androidx.car.app:app-*:1.7.0-alpha02`is released. Version 1.7.0-alpha02 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/02b55f664eba38e42e362e1af3913be1df552d55..5c17ac8d339b80b5f509f83792f5923e337612c7/car/app).

**New Features**

- Added deprecated flags for map-based templates which`MapWithContent`template will power moving forward.

**API Changes**

- Deprecate old`MapTemplate`,`RoutePreviewNavigationTemplate`,`PlaceListNavigationTemplate`and encourage use of new`MapWithContentTemplate`([Ib0a08](https://android-review.googlesource.com/#/q/Ib0a080e3225149eab2a373c58dabe32696a9a6fe))

### Version 1.7.0-alpha01

April 3, 2024

`androidx.car.app:app-*:1.7.0-alpha01`is released. We have moved our library versioning scheme to match the active CarApi version. This is to reduce confusion on the naming scheme based on developer feedback. As a result, we will skip versions 1.5 / 1.6 directly moving to 1.7 Version 1.7.0-alpha01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/58b48b8bcb6426d3e53ef28caf8ce6717b694223..02b55f664eba38e42e362e1af3913be1df552d55/car/app).

**New Features**

- *Map with Content* : New template named`MapWithContent`which supports List / Grid / Pane / Message as Content inside a map.
  - `RoutePreview`,`PlaceListNavigation`, Map templates are now deprecated.
  - Sample apps have been updated to show functionality of deprecated templates using`MapWithContent`.
- *Conversation Item*: New APIs for displaying conversations (IM, SMS), and Assistant readout in the car.
- *Vehicle Dimensions*: New API to retrieve vehicle measures (data on AAOS at the moment).

**API Changes**

- Mark extra small row image type as experimental ([I5184b](https://android-review.googlesource.com/#/q/I5184be4d7e8767f6b6320fdf2eebcd25ce1d9926))
- Added`CarInfo#fetchExteriorDimensions`API which allows access to vehicle exterior dimension information such as height, width, etc ([Ia40c5](https://android-review.googlesource.com/#/q/Ia40c5384a74cfa9a5b2132d332e1487d239aa19b))
- Removed`ExperimentalAPI`tag from`MapWithContentTemplate`([I66db8](https://android-review.googlesource.com/#/q/I66db8377b81c4bc8629f725b0973ef2b042a0938))
- Update`GridItem#setTitle`parameter to be nullable. ([I3d610](https://android-review.googlesource.com/#/q/I3d6105ff3d2754e076fa95d1a9f3abed1b8c62b9))
- `GetHeader`API does not require API 7 because it is backwards compatible ([I8c812](https://android-review.googlesource.com/#/q/I8c812f929ada3075d38a7b525b9fa62d6ccf5d73))
- Add support for`Header`in`ListTemplate`, deprecate`headerAction`,`headerTitle`,`actionStrip`([I7ae01](https://android-review.googlesource.com/#/q/I7ae0197b39ee122d8b609ea7529d034f0fb1d730))
- Deprecate`title`,`headerAction`,`actionStrip`in`GridTemplate`and add support for`Header`([I41a9c](https://android-review.googlesource.com/#/q/I41a9c540b65be36d55467e43842cf83ee67b7205))
- Remove level 7 requirement for experimental APIs: Badge,`GridTemplate`item size and image shape getters/setters,`GridItem`methods for getting/setting Badge. ([Id71eb](https://android-review.googlesource.com/#/q/Id71ebebeb082828a78a2b1672ebc949236c3269d))
- Deprecate`title`,`headerAction`,`actionStrip`in`PaneTemplate`, add new`Header`support ([I23154](https://android-review.googlesource.com/#/q/I2315483aeb8176c73e4a24a1c67bb81594d400ca))
- Changed Media Center telemetry from`BroadcastReceiver`to Browse Custom Action. ([I4185f](https://android-review.googlesource.com/#/q/I4185f7cafac42b7c42403e75c2fda8b487431200))
- Added`Header`attribute support in`MessageTemplate`. Deprecated support for`ActionStrip`,`headerAction`and`title`. ([Ie2de8](https://android-review.googlesource.com/#/q/Ie2de8c2d92ef2dc21e50cbd3e33574d2a75b67db))
- Modify alert constant visibility ([Icf8a8](https://android-review.googlesource.com/#/q/Icf8a84222bfacfc348e2fd4dc229bc7e9d0b3884))
- Remove`isLoading`attribute from the parent template ([I651e6](https://android-review.googlesource.com/#/q/I651e6f54b145b65b04a709c78bc68f4084fca284))
- Add extras to inform media apps of the main UI parameters ([I85ca2](https://android-review.googlesource.com/#/q/I85ca2b238beecfde7d0831bb69f09c464e2c8f55))
- Add media center analytics feature to`MediaExtensions`([I7ce28](https://android-review.googlesource.com/#/q/I7ce286c278e900c83e0a9e2f0bdd9ab96acdc578))
- Added option for extra small image on rows. ([I72c03](https://android-review.googlesource.com/#/q/I72c03bccc23d4b52d1292ae4047b314d9ab637dc))

**Bug Fixes**

- Update javadoc on`ConversationItem`to state that messages should be sorted in order from oldest to newest. ([I77a2a](https://android-review.googlesource.com/#/q/I77a2ab080485b8abf37d431dea8b7d12cb3ee3bd))
- Update`ListTemplate`truncation logic to remove oldest messages from`ConversationItem`([Ie0a61](https://android-review.googlesource.com/#/q/Ie0a614ec809f08106f38fabd3735bfb1e2d927d7))

## Version 1.4

### Version 1.4.0

May 29, 2024

`androidx.car.app:app-*:1.4.0`is released. Version 1.4.0 is a promotion of 1.4.0-rc02.

**Important changes since 1.3.0**

- Instrument Cluster map rendering for Navigation apps
- New Tab Template for improved app layout / usability
- Support for Adaptive task limits
- Secondary actions on list elements

### Version 1.4.0-rc02

December 13, 2023

`androidx.car.app:app-*:1.4.0-rc02`is released.[Version 1.4.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1280f3ae888e7721f7739bda09baae721af398c3..58b48b8bcb6426d3e53ef28caf8ce6717b694223/car/app). Minor fixes only

**Bug Fixes**

- Update javadoc on`ConversationItem`to state that messages should be sorted in order from oldest to newest ([I77a2a](https://android-review.googlesource.com/#/q/I77a2ab080485b8abf37d431dea8b7d12cb3ee3bd))
- Update`ListTemplate`truncation logic to remove oldest messages from`ConversationItem`([Ie0a61](https://android-review.googlesource.com/#/q/Ie0a614ec809f08106f38fabd3735bfb1e2d927d7))

### Version 1.4.0-rc01

November 1, 2023

`androidx.car.app:app-*:1.4.0-rc01`is released with no notable changes.[Version 1.4.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1780af2e94fd353709acd675b7574f8e52ba04dc..1280f3ae888e7721f7739bda09baae721af398c3/car/app).

### Version 1.4.0-beta02

September 20, 2023

`androidx.car.app:app-*:1.4.0-beta02`is released.[Version 1.4.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5d7dd999525725bd038a00ca4e89e0fef624a6da..1780af2e94fd353709acd675b7574f8e52ba04dc/car/app). This is almost identical to beta01, but lowers the`compileSdk`requirement to 33.

**Bug Fixes**

- Fix a bug where loading screens on Tabs would not be displayed appropriately. ([cae860](https://android.googlesource.com/platform/frameworks/support/+/ecf032b13b5050d0ca43f03b8a23712b1bcae860))

### Version 1.4.0-beta01

August 9, 2023

`androidx.car.app:app-*:1.4.0-beta01`is released.[Version 1.4.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/79023d0401db64cc121bf9505ed3eb83e20adee8..5d7dd999525725bd038a00ca4e89e0fef624a6da/car/app).
> **Note:** 1.4-beta01 requires compileSdk34, which is still in dev status. 1.4-beta02 will correct this issue. Alternatively, you can add`android.suppressUnsupportedCompileSdk=34`to your project's`settings.gradle`file to safely temporarily suppress the warning.

**New Features**

- Instrument[Cluster](https://developers.google.com/cars/design/create-apps/sample-flows/view-map-in-cluster)map rendering for Navigation apps
- New[Tab Template](https://developers.google.com/cars/design/create-apps/apps-for-drivers/templates/tab-template#requirements)for improved app layout / usability
- Support for[Adaptive task limits](https://developers.google.com/cars/design/create-apps/apps-for-drivers/plan-task-flows#task-limits)
- Secondary actions on list elements

**API Changes**

- See alpha02

### Version 1.4.0-alpha02

July 26, 2023

`androidx.car.app:app-*:1.4.0-alpha02`is released.[Version 1.4.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/87533b4ff06971ed59028936cd9b6da988cd4522..79023d0401db64cc121bf9505ed3eb83e20adee8/car/app)

- Release of Alpha02 is intended to be a preparation for an upcoming release of beta01.

**New Features**

- Map rendering on Instrument Cluster support for navigation apps
- Added Tabs for apps to improve layout experience
- Added List / Grid template rendering options
- Added new categories for Weather and Comms
- Move several API's to the next CarApi 7 release

**API Changes**

- Add multimedia fields to`CarMessage`([I5aaf6](https://android-review.googlesource.com/#/q/I5aaf6a2284428ef2cfc22cc39aa17f6bdabeae2f))
- Adds custom actions to`ConversationItem`in Car App Library ([Ie5ed6](https://android-review.googlesource.com/#/q/Ie5ed6d88ff386062a788b911df344aee576b5d0c))
- Add extras to indicate a media item is played with an immersive audio format and showcase its content format logo ([Icb5bb](https://android-review.googlesource.com/#/q/Icb5bb0cb7cf962b553245b2b6a14655bb4c88a2c))
- Add new Action type,`ActionsConstraints`API to support compose button. ([I31661](https://android-review.googlesource.com/#/q/I31661d61bce65a557a5f7d9abb4d889d855e4f92))
- Made`set/getTemplate`as`set/get ContentTemplate`([Ica036](https://android-review.googlesource.com/#/q/Ica036ae308375dbff27fdfdb1dc2a5f1072e21c3))
- Template parameter would now be`@NonNull`. Updated`MapWithContentTemplate`API documentation ([I0f8ed](https://android-review.googlesource.com/#/q/I0f8ed7a613dd265e6b34df59447481cc5d79a6e0))
- Removes`@ExperimentalCarApi`tag for Actions in`ListTemplate`for launch in CAL 1.4 ([I2cfcb](https://android-review.googlesource.com/#/q/I2cfcbbc90097e56611fd98ab1b58972b5f73cc0b))
- Removes`@ExperimentalCarApi`tag for`TabTemplate`([Ifcb82](https://android-review.googlesource.com/#/q/Ifcb829284dba1f63564633d85f24954d603250e6))
- Remove`@ExperimentalCarApi`annotations from Row secondary actions and decorations ([I8487e](https://android-review.googlesource.com/#/q/I8487ee9f2492411128c37e3b3de1a26d514e0ba0))
- Adds active tab content ID to`TabTemplate`and deprecates active state on Tabs ([I96932](https://android-review.googlesource.com/#/q/I9693206d30e91c20a5cfc07e613f53838b5a7756))
- Add`ItemImageShape`property to`GridTemplate`([Ibf431](https://android-review.googlesource.com/#/q/Ibf431e8965f506395e376d1fc2f7cfd10caaa902))
- Add`ItemSize`property to`GridTemplate`, which controls grid item sizing according to relative small, medium, large buckets. ([Icdb3b](https://android-review.googlesource.com/#/q/Icdb3bccfc7e9f72d580a9d3e88ce306ce3edbb08))
- Open up the API access for developers to gain a copy of the current screen stack. ([I48107](https://android-review.googlesource.com/#/q/I481076770ab23cc79b9d18791f0208e54a6a2c49))
- Adds category for weather apps to Car App Library ([I2be44](https://android-review.googlesource.com/#/q/I2be44c28676591de57eae4a61c4ba2de23e0841e))
- Adds category for calling apps to Car App Library ([Icab33](https://android-review.googlesource.com/#/q/Icab33174a1ae61a6db493e0453ea1dae49a5a764))
- Replaced`GridItem.Builder#setBadge()`with overloaded`setImage()`methods ([Id2000](https://android-review.googlesource.com/#/q/Id200086be38764876c358e3d1eb0bea42fb1c328))
- Add icon property to Badge ([I629b2](https://android-review.googlesource.com/#/q/I629b2a0b78ab0cb4eb8dd41b8f933eb68acc2f3e))
- Add method to set dot badge background color ([I6411c](https://android-review.googlesource.com/#/q/I6411c3665b26ecf058808271ab6b4882d59a633b))
- Add Badge property to`GridItem`, allowing a badge to be displayed on top of a`GridItem`image. ([I95de7](https://android-review.googlesource.com/#/q/I95de7ad195e7128bc00a9af832a3474f70d4ce8a))
- Added an experimental Badge object that will represent a badge to be displayed over an image. ([I9878d](https://android-review.googlesource.com/#/q/I9878dc4aabb1f061689f392f66197f7bdce0ce1b))

### Version 1.4.0-alpha01

February 22, 2023

`androidx.car.app:app-*:1.4.0-alpha01`is released.[Version 1.4.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c8c86434ca07058aada4c87ef7ff13b5249d4849..87533b4ff06971ed59028936cd9b6da988cd4522/car/app)

**API Changes**

- Adds top-level actions to`GridTemplate`in Car App Library ([Id0191](https://android-review.googlesource.com/#/q/Id0191ec171c0fafa2b48c0efef7f1fa50b30b50f))
- Adds top-level actions to`ListTemplate`in Car App Library ([I9efab](https://android-review.googlesource.com/#/q/I9efabdc1545bfe3685eba3cff5891dfe79f6f235))
- Add extras to link a media item's subtitle or its description to other media items ([Ic84bf](https://android-review.googlesource.com/#/q/Ic84bf7b41cb166e374e2d58866f98387ab3be250))
- Update api level for row actions to level 6. ([Ie0a69](https://android-review.googlesource.com/#/q/Ie0a6957df1175de597aa6130afd7a18089d83118))
- Add messaging callbacks to A4C ([Ie3986](https://android-review.googlesource.com/#/q/Ie39867b9f967c61d11c02a300844213c20417e2a))

**Bug Fixes**

- Add missing java doc references for`CarMessage`. ([I5db1c](https://android-review.googlesource.com/#/q/I5db1c7487a7a8b949759cf0e0aabdfb750f63464))
- Override`equals()`and`hashCode()`for`ConversationItem`and`CarMessage`([I6fd10](https://android-review.googlesource.com/#/q/I6fd102d9b073bdf1ade395df3dcad369dd967f30))
- Improve`ConversationItem.mMessages`validation (require non-null, non-empty ([Iafc51](https://android-review.googlesource.com/#/q/Iafc51da450c980769b3c85c5b456ee2e30b26b72))
- Add`@Keep`annotations to`ConversationItem`fields ([I5d250](https://android-review.googlesource.com/#/q/I5d250906be17b846ce0a57aeb6014deccdd6913a))
- Update java docs for the Row decoration and secondary actions. ([I000b6](https://android-review.googlesource.com/#/q/I000b6ed321fe34244a3677ba2e117406da40ce3d))

## Version 1.3

### Version 1.3.0-rc01

December 7, 2022

`androidx.car.app:app-*:1.3.0-rc01`is released.[Version 1.3.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/cce7b70f6a5ebf955cf748a73c18b63228b22c74..c8c86434ca07058aada4c87ef7ff13b5249d4849/car/app)

- Minor bug fixes from beta01. No Major Changes.

### Version 1.3.0-beta01

September 7, 2022

`androidx.car.app:app:1.3.0-beta01`,`androidx.car.app:app-projected:1.3.0-beta01`,`androidx.car.app:app-automotive:1.3.0-beta01`, and`androidx.car.app:app-testing:1.3.0-beta01`are released.[Version 1.3.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/aedf95b57a697bcad1a8259033140b5291466f2b..cce7b70f6a5ebf955cf748a73c18b63228b22c74/car/app)

- Car apps built using this library can now go to the Play Store using API Level 5 (see our[development guide](https://developer.android.com/training/cars/apps)). Features annotated with API level 5 and under are compatible with both[Android Auto 8.1+](https://play.google.com/store/apps/details?id=com.google.android.projection.gearhead)and the[Google Automotive App Host 1.4+](https://play.google.com/store/apps/details?id=com.google.android.apps.automotive.templates.host).

**New Features**

In addition to capabilities added in Car App Library 1.3.0-alpha01, the following features have been added as part of beta01 (All features here only involve with host side changes without any API changes):

- The floating navigation bar will continue to show even when a user is in a map-based selection screen in`PlaceListNavigationTemplate`,`RoutePreviewNavigationTemplate`, and`MapTemplate`. This can be done by updating navigation info through[`NavigationManager.updateTrip()`](https://developer.android.com/reference/androidx/car/app/navigation/NavigationManager#updateTrip(androidx.car.app.navigation.model.Trip)).
- Enable the action button with`FLAG_DEFAULT`to have a timeout animation. This button will be clicked by default after the timeout. (`[API 5 - All Templates]`)
- A`Row`s subtext is not truncated when the car is parked, but truncated to 2 lines while driving. (`[API 5 - All Templates]`)
- Support disabled state for`Action`,`Toggle`,`Row`(`[API 5 - All Templates]`)

**API Changes**

- Relax constraints in`MapTemplate`list to support selectable lists ([I961ed](https://android-review.googlesource.com/#/q/I961ed1e23955e37ee3713ea2b3b796231bc614c8))
- Remove the constraint for Header Actions to allow for custom icons. ([Iad28f](https://android-review.googlesource.com/#/q/Iad28fc25e466e70eadd0a52d61502509956e61c7))
- Add a constraint`setOnClickListenerAllowed()`to`ActionsConstraints`. Where it allowed`Action`to set`OnClickDelegate()`to actions except the standard icon types. (`TYPE_APP_ICON`,`TYPE_BACK`, and`TYPE_PAN`) ([I3c745](https://android-review.googlesource.com/#/q/I3c7457accf3322974b002d4510d319616e0d949a))

**Bug Fixes**

- Added compatibility of[Android Automotive Template Host 1.4+](https://play.google.com/store/apps/details?id=com.google.android.apps.automotive.templates.host)with curved displays (`[Host change]`)

### Version 1.3.0-alpha01

July 27, 2022

`androidx.car.app:app:1.3.0-alpha01`,`androidx.car.app:app-projected:1.3.0-alpha01`,`androidx.car.app:app-automotive:1.3.0-alpha01`, and`androidx.car.app:app-testing:1.3.0-alpha01`are released.[Version 1.3.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d3f07ea1e402004486b0708cf7799fc889fbcf72..aedf95b57a697bcad1a8259033140b5291466f2b/car/app)

Features annotated with API level 5 are compatible with Android Auto 7.9 and above.

**New Features**

- API Level 5: new`MapTemplate`that can be used by navigation apps to display pane or list content alongside a map ([If5826](https://android-review.googlesource.com/#/q/If5826aab9e25a7ae68c5330ffdd1821427a6d404),[If44b8](https://android-review.googlesource.com/#/q/If44b84a5981b9a5cc8880a9365f26c0786dc9364))
- API Level 5: new`CarAudioRecord`API to allow recording audio input via the host vehicle's microphone ([I5e71a](https://android-review.googlesource.com/#/q/I5e71a0443e12594c99c35e83817abdef649c402f))
- API Level 5: new`SuggestionManager`API to allow apps to provide suggestions to the host ([I5c103](https://android-review.googlesource.com/#/q/I5c103a93946975d52599da516ea6120d658086b2))
- API Level 5: new`Alert`API to display in context notifications on the`NavigationTemplate`([I163a7](https://android-review.googlesource.com/#/q/I163a7b908155218b0d0d1d55f3d31fa5ba920449),[I5ad70](https://android-review.googlesource.com/#/q/I5ad7085f163b8ea5b003a35a97242ac228d4d397))
- API Level 5: new`Header`and`MapController`components to facilitate re-use across templates ([If5826](https://android-review.googlesource.com/#/q/If5826aab9e25a7ae68c5330ffdd1821427a6d404))
- Added`androidx.car.app.category.POI`as a category for enabling POI apps (and deprecated`androidx.car.app.category.PARKING`and`androidx.car.app.category.CHARGING`) ([I59da1](https://android-review.googlesource.com/#/q/I59da1a3c2a12fd90fee78c7b18a10f0427840783))

**API Changes**

- API Level 5: new`onClick`method in the`SurfaceCallback`interface to allow for tap on map interactivity ([Ia9777](https://android-review.googlesource.com/q/Ia9777690c21f2d211e7b8277130ae5aaffe075b4))
- API Level 5: new flags`Action.FLAG_IS_PERSISTENT`and`Action.FLAG_DEFAULT`to describe`Action`s ([I96318](https://android-review.googlesource.com/q/I9631882873a539faedc93e9947b29a05279cb195),[I5ad70](https://android-review.googlesource.com/q/I5ad7085f163b8ea5b003a35a97242ac228d4d397))
- API Level 5: new enabled/disabled state for the`Action`,`Row`, and`Toggle`components (host support coming around the 1.3.0-beta01 release of the library) ([Id8a09](https://android-review.googlesource.com/#/q/Id8a0992b23d7b9f2ba3427b716d1ae8775753131))
- API Level 5: Favor the new`Header`component via`setHeader`on the`PlaceListNavigationTemplate.Builder`and`RoutePreviewNavigationTemplate.Builder`, deprecating the existing`setTitle`and`setHeaderAction`methods ([I30e6a](https://android-review.googlesource.com/#/q/I30e6a49ef1b7ecaefb4371770b92003f5b761cb5))
- API Level 5: new`setOnContentRefreshListner`method on the`PlaceListMapTemplate.Builder`and`PlaceListNavigationTemplate.Builder`for use with implementations of the new`OnContentRefreshListner`interface.
- API Level 5: New`setTripText`and`setTripIcon`on the`TravelEstimate.Builder`to customise the travel estimate card ([Idcc6d](https://android-review.googlesource.com/#/q/Idcc6d013d240f5af5a78f9cae7c545b94de38b71),[Ic620d](https://android-review.googlesource.com/#/q/Ic620dfdb9f78d69bae6bdbbb1a10ae40080550e1))
- Add support for`CarIconSpan`s in the`PaneTemplate`'s title ([Ia1ee0](https://android-review.googlesource.com/#/q/Ia1ee0a4ab2e16a4fc29f5714ec29a4c72e3ccab2))
- Add support for`CarIconSpan`s in a`Row`'s title and text ([Ic1e3c](https://android-review.googlesource.com/q/Ic1e3cbbb45ff48830bf4917488b94c757ca8aab6))
- Map`ActionStrip`s can now have up to four actions ([If3522](https://android-review.googlesource.com/q/If35227e3cf7a1d9f3b77aef0029b8546e4df449e))
- Update Car App API level to 5 ([I26b8e](https://android-review.googlesource.com/#/q/I26b8e99ddbb82e1034cff3935555b93baadaa308))
- Headers/titles are now optional for the`PlaceListMapTemplate`,`PlaceListNavigationTemplate`,`RoutePreviewNavigationTemplate`,`GridTemplate`,`ListTemplate`,`LongMessageTemplate`,`MessageTemplate`,`PaneTemplate`, and`SignInTemplate`([I2078d](https://android-review.googlesource.com/q/I2078d67ac04bbcc9441f9fab277500b986d5b3bd),[Icadde](https://android-review.googlesource.com/q/Icaddef163c3d8e3c0c6b9c2917981b5571153178))

**Bug Fixes**

- Updated`PaneTemplate`image sizing rules to be a square bounding box ([Idd72e](https://android-review.googlesource.com/#/q/Idd72e4584dfa066f8db113afb567a71017fcca85))
- Fixed an exception that happens if the screen stack is modified after`State.DESTROYED`. ([I3c8eb](https://android-review.googlesource.com/#/q/I3c8eb1bda220f9c5e7b3a642d0ca39e796f2cf07))
- Added a null check for retriving the app icon ([I3f710](https://android-review.googlesource.com/#/q/I3f7102831dcf4d515c257112b4498488200125df))
- Update Car Hardware API to use`STATUS_UNKNOWN`instead of`STATUS_UNAVAILABLE`by default ([Ic9444](https://android-review.googlesource.com/#/q/Ic9444da7867b609e6cba0d049e00649d024f4d9f))
- Check if display exists before creating surface ([Ice027a](https://android-review.googlesource.com/q/Ice027a6cd28bb02620233b2a9352a69aa45f107d))
- Fix`CarValue.equals()`bug involving`STATUS_UNIMPLEMENTED`([I24451](https://android-review.googlesource.com/q/I24451ec53a3adc9b2bc652437e171b46cfbead2c))

## Version 1.2

### Version 1.2.0

November 9, 2022

`androidx.car.app:app-*:1.2.0`is released.[Version 1.2.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d3f07ea1e402004486b0708cf7799fc889fbcf72..4ca60855ccea04eba8c9da0846c862bfc93741e8/car/app)

- This is a stabilization release, and there are no changes compared to v1.2.0-rc01.

### Version 1.2.0-rc01

March 23, 2022

`androidx.car.app:app-*:1.2.0-rc01`is released.[Version 1.2.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e1bc5848802c2aa69a3cd97f991cb16e51430099..d3f07ea1e402004486b0708cf7799fc889fbcf72/car/app)

- This is a stabilization release, and there are no API changes compared to`v1.2.0-beta02`. New experimental features (API level 5) have been added that are intended for future Android Auto and Android Automotive releases.

**Bug Fixes**

- Fixed an exception that happens if the screen stack is modified after`State.DESTROYED`. ([I3c8eb](https://android-review.googlesource.com/#/q/I3c8eb1bda220f9c5e7b3a642d0ca39e796f2cf07))
- Updated`CarSensors`API to indicate that they are not implemented for AAOS ([Idd57b](https://android-review.googlesource.com/#/q/Idd57bffb79c800d0418abd0efdecc18f8c1f4e01))
- Updated`PlaceListMapTempalte.Builder#setCurrentLocationEnabled`to indicate that ACCESS_COARSE_LOCATION would be sufficient for the feature ([I510c2](https://android-review.googlesource.com/#/q/I510c23f78aa740233dd9913e100835a6ae17b163))
- Made exit number optional for roundabout-with-angle maneuver types ([Ife7d1](https://android-review.googlesource.com/#/q/Ife7d1f3e35aac0ff0e5b52d3e324366fc33f41fb))

### Version 1.2.0-beta02

January 26, 2022

`androidx.car.app:app-*:1.2.0-beta02`is released.[Version 1.2.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8fd49d11e627a0e8e9ba4e5101b4d947152dda3f../car/app)

Car apps built with this library version targeting the`Android Automotive OS`platform can now be published to the Play Store open testing channel. Refer to the[development guide](https://developer.android.com/training/cars/apps)for more details.

Features annotated with API level 4 and under are compatible with both`Android Auto`7.2+ and the new`Android Automotive OS`platform. See the`Known Issues`section below for caveats.

**API Changes**

- Added experimental`setOnContentRefreshListener`API to POI templates ([I6bf22](https://android-review.googlesource.com/#/q/I6bf22fc1d0c2fe1e62f811173dc5c5ecb4a6e581))

**Bug Fixes**

- Fixed a memory leak in`CarAppService`when the car host unbinds. ([I5c9ca](https://android-review.googlesource.com/#/q/I5c9caf05797ea257ef21cbd96dab5fdfbc85a70e),[b/203594731](https://issuetracker.google.com/issues/203594731))
- Updated`CarAppActivity`javadoc to include requirements for singleTask launchmode ([Id2f95](https://android-review.googlesource.com/#/q/Id2f954ad2bce2cb66da443ace5220c6b12fd3ba3))
- Reduces the visual glitch on resume. ([Iff7e0](https://android-review.googlesource.com/#/q/Iff7e07b38369d82620d5245e0d204d27eae6cfd0))

**Known Issue(s)**

- The map`ActionStrip`s in the`PlaceListNavigationTemplate`and`RoutePreviewNavigateTemplate`will start becoming available in the next`Android Auto`and`Android Automotive OS`releases.

### Version 1.2.0-alpha02

December 15, 2021

`androidx.car.app:app-*:1.2.0-alpha02`is released.[Version 1.2.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f07d12061370a603549747200c79b60239706330..8fd49d11e627a0e8e9ba4e5101b4d947152dda3f/car/app)

Features annotated with API level 4 has been upgraded from experimental to stable, including the map`ActionStrip`s in the`PlaceListNavigationTemplate`and`RoutePreviewNavigateTemplate`, the`CarIcon`image in`Pane`s, the`QRCodeSignInMethod`and the ability to set rendering hints (e.g. flags) in`Action`s.

**New Features**

- In Android Auto 7.1+, the item limit for`Pane`has been increased from 2 to 4.

**API Changes**

- Added an experimental`toString()`method to`CarUnit`([I36a3b](https://android-review.googlesource.com/#/q/I36a3bc7c514403329af7ab2dd7636d77b9ff2bf7))

**Bug Fixes**

- Fixed a crash that happened in`CarAppPermissionActivity`if the callback is dead ([If9823](https://android-review.googlesource.com/#/q/If98232a57a4a05186e77e0c414b0cdd9b04ce20d))
- Changed`Pane`default list limit to 4 ([I0068b](https://android-review.googlesource.com/#/q/I0068b6dcb80b6a13d5e7bea6f9f981a1a2abfe12))

### Version 1.2.0-alpha01

November 3, 2021

`androidx.car.app:app-*:1.2.0-alpha01`is released.[Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ef3b5fed8cbec46a41f2d3b8cf11551fb19f282c..f07d12061370a603549747200c79b60239706330/car/app)

All new`v1.2.0`features (API 4+) are currently experimental targeting future Android Auto and Android Automotive OS releases. Refer to the[development guide](https://developer.android.com/training/cars/apps)for more details.

**API Changes**

- Made`AutomotiveCarInfo`API experimental. ([Ia13e5](https://android-review.googlesource.com/#/q/Ia13e57579056baee54edf81a7e6e083b419ad0a9))
- Added Car App Library API level 4 ([I2a2e7](https://android-review.googlesource.com/#/q/I2a2e7807b4c964c08fdf1e858f5f102559b3d299))
- API Level 4: Added support for setting a`CarIcon`in`Pane`([Ifcc12](https://android-review.googlesource.com/#/q/Ifcc125bed378969e35b0f51068b1a496bd8486e1))
- API Level 4: Added QR code sign in method ([Ib623e](https://android-review.googlesource.com/#/q/Ib623e16fe35735bedfc204fe1eaf26f197125639))
- API Level 4: Added set/getFlags to`Action`([Ic03ab](https://android-review.googlesource.com/#/q/Ic03abf3a1f793db7e123f3431aee2b5585ec9de2))
- API Level 4: Added support for panning and zooming in`PlaceListNavigationTemplate`and`RoutePreviewNavigationTemplate`([I9d8a3](https://android-review.googlesource.com/#/q/I9d8a3ff7751ffd5423201b2f29886adff38e8bde))

**Bug Fixes**

- API Level 4: Add mechanism to allow apps to send location updates to the car host ([I3bad3](https://android-review.googlesource.com/#/q/I3bad3e2a2343ba817442ed96b8d8818b586a30f9))
- Fix an issue where the host validation logic was not finding the TEMPLATE_RENDERER permission properly ([I62618](https://android-review.googlesource.com/#/q/I626184386c346a4017424a7eecbf91145f04fed3))

## Version 1.1.0

### Version 1.1.0

December 15, 2021

`androidx.car.app:app-*:1.1.0`is released.[Version 1.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ec1427b1107ee0f4fea226a288599a73f4533ba0..cad4d78106e40db724042eec73ccf8a5c308e793/car/app)

This is a stabilization release, and there are no changes compared to`v1.1.0-rc01`. Also see the release notes for`v1.2.0-alpha02`for more details on new features for the car app library.

**Important changes since 1.0.0**

- API Level 2:`SignInTemplate`and`LongMessageTemplate`that can be used for sign-in flows when the vehicle is parked
- API Level 2: map interactivity support within the`NavigationTemplate`
- API Level 2: multiple-length text support to allow apps to provide multiple versions of string for display depending on the car screen sizes.
- API Level 3:`CarHardwareManager`that can be used to query vehicle's hardware data, such as model and make, fuel levels and other sensors.

### Version 1.1.0-rc01

November 3, 2021

`androidx.car.app:app-*:1.1.0-rc01`is released.[Version 1.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ef3b5fed8cbec46a41f2d3b8cf11551fb19f282c..ec1427b1107ee0f4fea226a288599a73f4533ba0/car/app)

This is a stabilization release, and there are no API changes compared to`v1.1.0-beta01`. New experimental features (API level 4) have been added that are intended for future Android Auto releases. See the release notes for`v1.2.0-alpha01`for more details on the experimental APIs.

### Version 1.1.0-beta01

September 1, 2021

`androidx.car.app:app-*:1.1.0-beta01`is released.[Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/97264aa4532db7f7db1ffb3f42f3a9204971dbfc..ef3b5fed8cbec46a41f2d3b8cf11551fb19f282c/car/app)

All`v1.1.0`features (API 2+) are fully compatible with Android Auto 6.7 and above. Refer to the[development guide](https://developer.android.com/training/cars/apps)for more details.

**API Changes**

- Removed`Manager`as a public interface ([Ie381b](https://android-review.googlesource.com/#/q/Ie381b8d63a1e73ef0a145d047c5bd5b1456ac074))
- Added ability to set a custom branded background for permission request ([I74b76](https://android-review.googlesource.com/#/q/I74b767b7d5f04928c0210a8685e486330e8df870))
- Added`ScreenManager.getStackSize`([I0b16a](https://android-review.googlesource.com/#/q/I0b16a8aa29a89b2244ba41a3ccfa8082669c0e98))
- Removed`ScreenController`constructor that explicit takes`TestCarContext`([Iefebc](https://android-review.googlesource.com/#/q/Iefebcd8154b8437a4db7cc82401ed30a72b0d95d))

**Bug Fixes**

- Added API level check when creating`CarHardwareManager`([I48f9b](https://android-review.googlesource.com/#/q/I48f9be001f5e55ed7a125102c7535a94e664b88e))
- Added checks for invalid`CarSpan`usage across the API ([I65ae6](https://android-review.googlesource.com/#/q/I65ae657b8b0e9e0243e993bfd5743e55d271e1b1))
- Fixed an issue where if a`Screen`is marked as finished during its creation, it would leave the stack in a broken state ([I81b13](https://android-review.googlesource.com/#/q/I81b13909a2342846ec46157dc1a2a529b85e6e30))
- Fix an issue where`CarNotificationManager.notify`would log an error for AutomotiveOS if there were actions with icons in the`CarAppExtender`([I3633d](https://android-review.googlesource.com/#/q/I3633d343d2c9d706828a5fb747ddcc49914a0802))
- Added a handshake method for app and host to establish an API version ([I7d6f8](https://android-review.googlesource.com/#/q/I7d6f816dffd54e30ec14dff70c2c7499f6838d55))

### Version 1.1.0-alpha02

July 21, 2021

`androidx.car.app:app-*:1.1.0-alpha02`is released.[Version 1.1.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/cffcc074543c8c27a9fa134f558d332f2f5acf61..97264aa4532db7f7db1ffb3f42f3a9204971dbfc/car/app)

**New Features**

- API Level 3: Added a`CarHardwareManager`that can be used to query vehicle's hardware data, such as model and make, fuel levels and other sensors. Currently, this feature is only available for Android Auto 6.7+ in the open-testing channel. Testing this in a desktop environment requires a new version of`Desktop Head Unit`which will be released separately. Stay tuned on[Test Android apps for cars page](https://developer.android.com/training/cars/testing)for details on when the new version becomes available.
- Follow the[development guide](https://developer.android.com/training/cars/apps)and the library reference for additional details and design guidelines on how to use these features in car hosts that are compatible with API level 3.

**API Changes**

- Consolidated`SessionController`and`ScreenController`lifecycle methods into a single`moveToState`method ([I1ed00](https://android-review.googlesource.com/#/q/I1ed00d9e4df59af59643da25d9385f7a9326a3be))
- Added`CarContext#getHostInfo()`([I8977e](https://android-review.googlesource.com/#/q/I8977e05be0746c1160bcee0b28e245e6bd18cb26))
- Removed deprecated fields. ([I67168](https://android-review.googlesource.com/#/q/I671682a7b8071cb93c140e734af56a1d7fd84a12))
- Updated`SessionController`and`ScreenController`to expose constructors directly ([Iabf22](https://android-review.googlesource.com/#/q/Iabf22d3bc74e9f18db7e763a2ce6a93de8796cb5))
- Removed`PinSignInMethod.Builder`and`ProviderSignInMethod.Builder`([I9f0cb](https://android-review.googlesource.com/#/q/I9f0cb418805ce421545f7ca9f4681e050ceb8d0d))
- Added 'setCarAppResult()' to enable using templated apps 'for result' in AAOS ([I37741](https://android-review.googlesource.com/#/q/I37741edda17f20e598774e8735a4b69cde6c593c))
- Annotated`CarHardware`interfaces with`@MainThread`. ([Ib2f85](https://android-review.googlesource.com/#/q/Ib2f851610b8e1d12b6b59345dff28e7218fb5585))
- Renamed`OnCarDataListener`to`OnCarDataAvailableListener`([I518ca](https://android-review.googlesource.com/#/q/I518ca17f196c6e251eadb189edaec1ff3ce61aa1))
- Updated`CarInfo`,`Speed`,`Mileage`method names and javadoc. ([I86672](https://android-review.googlesource.com/#/q/I866723b47136e2bee9b5f7fb770672d2813f4a71))
- Renamed`Toll`to`TollCard`. ([I3e7c8](https://android-review.googlesource.com/#/q/I3e7c8d02668bcbfc706f8794dfec334e350ae427))
- Removed deprecated`PinSignInMethod.getPin`which is replaced by`PinSignInMethod.getPinCode`([I996ce](https://android-review.googlesource.com/#/q/I996ce02262fc36a6686de682432bdbf4af9c05bc))
- Removed`OnInputCompletedListener`(replaced with`InputCallback`). ([Ib5be1](https://android-review.googlesource.com/#/q/Ib5be1385276c86a62f3460716a2cd423bd268577))
- Changed`PinSignInMethod`to take`CharSequence`instead of`String`([I275d5](https://android-review.googlesource.com/#/q/I275d5db8128dac97c85663493118dc279d3fbae5))

**Bug Fixes**

- Javadoc fixes for car hardware. ([I2abbc](https://android-review.googlesource.com/#/q/I2abbccc5fa3c48cbcb1901d6c1c90ddd8bf0aaad))

**External Contribution**

**Known Issues**

- In the`SignInTemplate`, using the`InputSignInMethod`may result in a`NullPointerException`in the car host. This will be addressed in the next release of the library. To workaround the issue, include this line in your app's Proguard config:`-keep class androidx.car.app.model.signin.InputSignInMethod { *; }`

### Version 1.1.0-alpha01

June 16, 2021

`androidx.car.app:app:1.1.0-alpha01`,`androidx.car.app:app-automotive:1.1.0-alpha01`, and`androidx.car.app:app-testing:1.1.0-alpha01`are released.[Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1c07c69c4d9e26c6ce13e671fad1ae314a4cca5e..cffcc074543c8c27a9fa134f558d332f2f5acf61/car/app)

**New Features**

- API Level 2: new`SignInTemplate`and`LongMessageTemplate`that can be used for sign-in flows when the vehicle is parked.
- API Level 2: new map interactivity support within the`NavigationTemplate`
- API Level 2: new multiple-length text support to allow apps to provide multiple versions of string for display depending on the car screen sizes.
- Follow the[development guide](https://developer.android.com/training/cars/apps)and the library Javadoc for additional details and design guidelines on how to use these features in car hosts that are compatible with API level 2.

**API Changes**

- Made all`*Callback`interface methods default and renamed`OnRequestPermissionsCallback`-\>`OnRequestPermissionsListener`([Ib3ec9](https://android-review.googlesource.com/#/q/Ib3ec9dedec7e736755324bba918e47494f5bc018))
- Updated`androidx.car.app.hardware`classes to remove unnecessary builders and parameter classes. ([I67beb](https://android-review.googlesource.com/#/q/I67bebfc9f418e125d28072171561375095aa518c))
- Added`androidx.car.app.hardware`classes for access to car specific data such as fuel, battery and speed. ([Iff3c9](https://android-review.googlesource.com/#/q/Iff3c92ebca831557ce2e475c5294e2701f6e5a2e))
- Added`ActionStrip`support on`MessageTemplate`([Ida657](https://android-review.googlesource.com/#/q/Ida657287b4412787c304e000a905a26866e2b248))
- Added`setLoading`to`MessageTemplate`. ([I2a4b5](https://android-review.googlesource.com/#/q/I2a4b58208c2239a42a2e0c3c14b19cc285de7cd4))
- Renamed`ConnectionToCar`to`CarConnection`([Ife9bd](https://android-review.googlesource.com/#/q/Ife9bd6fcf4d6732ab3a3a0ccd2eebad8ab51eb8e))
- Changed`NavigationTemplate`to return an explicit`PanModeDelegate`([I13877](https://android-review.googlesource.com/#/q/I1387739add55e0bccbea10007e24f702640cdb72))
- Updated parameter order for`CarContext.requestPermissions`([Ib890a](https://android-review.googlesource.com/#/q/Ib890ac96c0d884b4a3a2ce9690694c33365697f9))
- Updated metadata key to define min car api level to`androidx.car.api.minCarApiLevel`([Ib0d41](https://android-review.googlesource.com/#/q/Ib0d4118767db4046f790e49661b3bd9cfb40e994))
- Created an API that allows observing car connection state ([Ifc935](https://android-review.googlesource.com/#/q/Ifc935900b9541360961ed871338c4ba7da6c828f))
- Added support for setting a toggle for an`Action`, and added the pan mode`Action`type ([Ica6af](https://android-review.googlesource.com/#/q/Ica6afbd94a10d2c6d007b6d45d76daeb3a22dfa7))
- Created`CarNotificationManager`to support sending notification in the car ([I10d7a](https://android-review.googlesource.com/#/q/I10d7a2d36e8c13f1a96c29885257b82ddfce391a))
- Added`ConstraintManager`for providing list limits from the host ([I8690e](https://android-review.googlesource.com/#/q/I8690ef57bbb60d2f452412856d663fbc297edf17))
- Added pan mode and map action strip API in`NavigationTemplate`([I77aa6](https://android-review.googlesource.com/#/q/I77aa6564c78707d7e11155949bfce68a4b415cf7))
- Added pan and zoom API in`SurfaceCallback`for navigation apps ([Id5e9d](https://android-review.googlesource.com/#/q/Id5e9d408595073b168aa0df1453a9f0c62f28c8b))
- Updated`CarAppApiLevel`to 2 ([Ic1540](https://android-review.googlesource.com/#/q/Ic154052d277af26fcb9d33bd267ebf4ba1f55ffe))
- Added ability to request permissions from a`CarAppService`([I5421e](https://android-review.googlesource.com/#/q/I5421e9c7ec3c3ffed5e343562e93d0d35df3e492))
- Added`RequiresCarApi(2)`annotation to multi-text API ([Iacb62](https://android-review.googlesource.com/#/q/Iacb62fc4c193189fe6cf5655c077e70ce168e7c3))
- Allowed multiple text variants in the half-list template title ([Ib8df7](https://android-review.googlesource.com/#/q/Ib8df78f07f9a3dda85f809c60ddf88550e33cf05))
- Added new`LongMessageTemplate`(requires Car API level 2) ([Ic5cee](https://android-review.googlesource.com/#/q/Ic5cee5763339b60c8d4b13f1b741768f25345d6a))

**Bug Fixes**

- Updated image size requirements to account for larger car screens ([I116dc](https://android-review.googlesource.com/#/q/I116dcf33020d600e6d1da1f9da99c97b26c2b5f9))
- Disallowed adding more than 2 actions in template bodies ([I32157](https://android-review.googlesource.com/#/q/I32157e7ed8c1d908c7e3360d3b5b5419d733e04e))
- Ensured all creation of`PendingIntent`s in the car app library set flags. ([If84fe](https://android-review.googlesource.com/#/q/If84fe02a5e14d27c6af72b7fd78d5f7ff9a73e8c),[b/186394900](https://issuetracker.google.com/issues/186394900))
- Updated javadoc to allow`Row`'s text changes as refreshes ([If3f9c](https://android-review.googlesource.com/#/q/If3f9c4825e7c92de9c8a873440d9b93f8c1f8688))
- `androidx.activity:activity:1.2.0`is now an api dependency ([Id1cb9](https://android-review.googlesource.com/#/q/Id1cb9178b1343c98f78f36af3d19ed88a6aa5857))
- Made`SignInTemplate`and`LongMessageTemplate`to require parked-only actions in their body and update documentation to indicate they will only be shown when the car is parked ([Iddaa9](https://android-review.googlesource.com/#/q/Iddaa95a90cba2731e2a52f89738fd9f906a381e5))
- Fixed an exception that occurs when popping a`Screen`during start ([Ifcf40](https://android-review.googlesource.com/#/q/Ifcf409400e2af8e4aa7920b5fa469fc95ceb3322),[b/184664896](https://issuetracker.google.com/issues/184664896))
- Allowed custom text color in`ForegroundCarColorSpan`([I69e59](https://android-review.googlesource.com/#/q/I69e59837ee60f5768af1e26ba9a9dd6ead0a01af))
- Fixed an issue where`ON_DESTROY`on a`Session`is observed after a`Screen`'s`ON_DESTROY`([I52e01](https://android-review.googlesource.com/#/q/I52e01fe22e4e6dc8130735ebae49a1575928ee5a),[b/183696617](https://issuetracker.google.com/issues/183696617))
- Updated javadoc on when setting a`TravelEstimate`'s remaining time to an unknown time is allowed. ([I99610](https://android-review.googlesource.com/#/q/I9961081b996822fae8f8763abe578cb622a3d23d),[b/183632456](https://issuetracker.google.com/issues/183632456))
- Updated`Action`to support`ForegroundColorSpan`in the title and any custom background color ([I578e4](https://android-review.googlesource.com/#/q/I578e4ad96cfb5def8dc899e5e0ed3ee9975c4574))
- Do not execute`NavigationManagerCallback#onStopNavigation`if the callback is cleared before the executor executes ([I7fc5e](https://android-review.googlesource.com/#/q/I7fc5ebe1f371b0530f084f76236ab058f71f2a5c),[b/181143772](https://issuetracker.google.com/issues/181143772))
- Fixed an issue that require the app to explicitly take on a dependency on lifecycle-common-java8 ([I8b8c8](https://android-review.googlesource.com/#/q/I8b8c831d1fe033a2f8b8e653f373b10539dd0969))

**Known Issues**

- In the`SignInTemplate`, the on-screen keyboard shows a "search" icon instead of an "enter" icon when the user wants to confirm the input. As a workaround, users can access the phone keyboard that activates when the input field is in focus.
- In Android Auto version 6.5, the pan and zoom callbacks in`SurfaceCallback`may be incorrectly invoked for some touch gestures.

## Car App Testing Version 1.0.0

### Version 1.0.0-alpha01

March 24, 2021

`androidx.car.app:app-testing:1.0.0-alpha01`is released.[Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1c07c69c4d9e26c6ce13e671fad1ae314a4cca5e/car/app/app-testing)

This is the first Jetpack release of the previously closed source testing library. Refer to our[samples](https://github.com/android/car-samples/tree/main/car_app_library)on how to use this library in your tests.

**New Features**

- The controllers for the model classes have been removed. Model getters are now part of the public API surface which allows for validating values that were set in the builders.
- The previous`CarAppServiceController`has been replaced by the new`SessionController`for testing logic related to the lifetime of the connection to the hots.

## Version 1.0.0

### Version 1.0.0

April 21, 2021

`androidx.car.app:app:1.0.0`is released.[Version 1.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e3a516e6a35300705fe998d142ca4fcea7e582e5..a280dff6f64923829d75febea7a060c507084b56/car/app/app)

**Major features of 1.0.0**

- In early April, we[announced](https://android-developers.googleblog.com/2021/04/start-your-engines-launch-new-android.html)that apps can start publishing to the production channel using`androidx.car.app:app:1.0.0-rc01`. Car App Library v1.0.0 is now stable and is fully compatible with Android Auto 6.1 and above.
- Follow the[development guide](https://developer.android.com/training/cars/navigation)for details on how to build navigation, parking, and charging apps for Android Auto using the library.

**Bug Fixes**

- Fixed an exception that occurs when popping a`Screen`during start ([70aae1](https://android-review.googlesource.com/#/q/70aae171125c78d30f59e10be727c8ee3e345a64),[b/184664896](https://issuetracker.google.com/issues/184664896))
- Fixed an issue where`ON_DESTROY`on a`Session`is observed after a`Screen`'s`ON_DESTROY`([0ceecb](https://android-review.googlesource.com/#/q/0ceecba883de1438896a21bd94193ad925b1ba76),[b/183696617](https://issuetracker.google.com/issues/183696617))

### Version 1.0.0-rc01

March 24, 2021

`androidx.car.app:app:1.0.0-rc01`is released.[Version 1.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9f4c909a46b4d538ee280141d444dc3bf8acca7c..e3a516e6a35300705fe998d142ca4fcea7e582e5/car/app/app)

**Bug Fixes**

- Fixed a race condition bug where`NavigationManagerCallback#onStopNavigation`was being called after the callback was cleared. This happened if the callback was cleared before the callback executor actually ran ([I7fc5e](https://android-review.googlesource.com/#/q/I7fc5ebe1f371b0530f084f76236ab058f71f2a5c),[b/181143772](https://issuetracker.google.com/issues/181143772))
- Fixed an issue that required the app to explicitly take a dependency on`lifecycle-common-java8`([I8b8c8](https://android-review.googlesource.com/#/q/I8b8c831d1fe033a2f8b8e653f373b10539dd0969))
- Fixed a`NullPointerException`that was thrown when the app receives a`stopNavigation`call when it has already removed a callback ([Ib8b89](https://android-review.googlesource.com/#/q/Ib8b89f43bd5891ef9f8b53944b5ef00979d8e607),[b/181143772](https://issuetracker.google.com/issues/181143772))
- Improvements to not dispatch calls to app if its lifecycle is not at least in a`CREATED`state ([I86965](https://android-review.googlesource.com/#/q/I8696503d1a9859411c4a52fa73d2852c8b3383d9),[b/179800224](https://issuetracker.google.com/issues/179800224),[b/177921120](https://issuetracker.google.com/issues/177921120))
- Fixed an issue where an invalid min API specified in the app's manifest would throw, causing an ANR on the host. ([Iffedd](https://android-review.googlesource.com/#/q/Iffeddb795639f3a62611814784be7cffd59d2f7d),[b/174231592](https://issuetracker.google.com/issues/174231592))

### Version 1.0.0-beta01

February 24, 2021

`androidx.car.app:app:1.0.0-beta01`is released.[Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9f4c909a46b4d538ee280141d444dc3bf8acca7c/car/app/app)

This is the first Jetpack release of the previously closed source library, and is compatible with Android Auto 6.1 or above. Follow the[development guide](https://developer.android.com/training/cars/navigation)for details on how to build car apps using the library.

**New Features**

- Introduced a[`GridTemplate`](https://developer.android.com/reference/androidx/car/app/model/GridTemplate)which your app can use to show a list of UI elements in a grid layout.
- Introduced a[`CarAppService.createHostValidator`](https://developer.android.com/reference/androidx/car/app/CarAppService#createHostValidator())method to validate that a host connection is from a trusted source (for example, Android Auto).
- Added a[`CarAppExtender.Builder.setColor`](https://developer.android.com/reference/androidx/car/app/notification/CarAppExtender.Builder#setColor(androidx.car.app.model.CarColor))API. ([b/174231592](https://issuetracker.google.com/issues/174231592))

**Bug Fixes**

- Fixed an issue where the wrong`Screen`is resumed when popping screens sequentially. ([b/177590791](https://issuetracker.google.com/issues/177590791))