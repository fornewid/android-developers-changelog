---
title: https://developer.android.com/jetpack/androidx/releases/media
url: https://developer.android.com/jetpack/androidx/releases/media
source: md.txt
---

# Media

# Media

[User Guide](https://developer.android.com/guide/topics/media-apps/media-apps-overview)[Code Sample](https://github.com/android/media-samples)  
API Reference  
[androidx.media](https://developer.android.com/reference/kotlin/androidx/media/package-summary)  
[androidx.media.app](https://developer.android.com/reference/kotlin/androidx/media/app/package-summary)  
[androidx.media.session](https://developer.android.com/reference/kotlin/androidx/media/session/package-summary)  
Share media contents and controls with other apps. Superseded by media3.  

|  Latest Update  |                                Stable Release                                | Release Candidate | Beta Release | Alpha Release |
|-----------------|------------------------------------------------------------------------------|-------------------|--------------|---------------|
| August 13, 2025 | [1.7.1](https://developer.android.com/jetpack/androidx/releases/media#1.7.1) | -                 | -            | -             |

## Declaring dependencies

To add a dependency on Media, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    implementation "androidx.media:media:1.7.1"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.media:media:1.7.1")
}
```

For more information about dependencies, see[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:461042+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=461042&template=1238510)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.7

### Version 1.7.1

August 13, 2025

`androidx.media:media:1.7.1`is released. Version 1.7.1 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/3919950349304b3de3fad474f9afb11e8d87b211..8f8c367f941ee15ad7c404ac711649af99140d1e/media/media).

**Bug Fixes**

- Improve performance of`MediaSession.setMetadata()`by reducing the number of intermediate allocations and removing unnecessary parceling/unparceling of bitmaps.

### Version 1.7.0

November 29, 2023

`androidx.media:media:1.7.0`is released.[Version 1.7.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/372e1696caa87356c2b67083315d3e55b29a5da3..3919950349304b3de3fad474f9afb11e8d87b211/media/media)

**Important changes since 1.6.0**

- Catch`ForegroundServiceStartNotAllowedException`in`MediaButtonReceiver`and forward it to`onForegroundServiceStartNotAllowedException`. ([I0c939](https://android-review.googlesource.com/#/q/I0c9392298a93add391bfaae2b47e06d06258ab78))
- Add`BROWSER_SERVICE_EXTRAS_KEY_FAVORITES_MEDIA_ITEM`for passing Favorites media item in`MediaBrowserCompat`root extras. ([Id3a11](https://android-review.googlesource.com/#/q/Id3a11251c96b7e7727081840e36fe0e5cff24c5d))
- Add extras to set browse custom actions in`MediaBrowserCompat`root extras and`MediaItem`descriptions. ([Iab163](https://android-review.googlesource.com/#/q/Iab16398066d6e83661aa0806aefe1f1934a1fed1))
- Fix`IllegalStateException`caused by returning null from`MediaBrowserService.onLoadChildren`on older Android versions.

### Version 1.7.0-rc01

November 15, 2023

`androidx.media:media:1.7.0-rc01`is released with no changes.[Version 1.7.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e3ffd7948030a769c857b8c629e0079c54b730ad..372e1696caa87356c2b67083315d3e55b29a5da3/media/media)

### Version 1.7.0-beta01

November 1, 2023

`androidx.media:media:1.7.0-beta01`is released.[Version 1.7.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7d3ac1ab1206c01fae3ebb500b5b942636070155..e3ffd7948030a769c857b8c629e0079c54b730ad/media/media)

**Bug Fixes**

- Fix potential memory leak of`MediaBrowserService`and`MediaBrowserServiceCompat`.[b/37137738](https://issuetracker.google.com/37137738).
- Fix`IllegalStateException`caused by returning null from`MediaBrowserService.onLoadChildren`on older Android versions.

### Version 1.7.0-alpha01

February 8, 2023

`androidx.media:media:1.7.0-alpha01`is released.[Version 1.7.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c2abb1a63ad5d8a92cd723550b6989c767f86175..7d3ac1ab1206c01fae3ebb500b5b942636070155/media/media)

**New Features**

- Catch`ForegroundServiceStartNotAllowedException`in`MediaButtonReceiver`and forward it to`onForegroundServiceStartNotAllowedException`. ([I0c939](https://android-review.googlesource.com/#/q/I0c9392298a93add391bfaae2b47e06d06258ab78))
- Add`BROWSER_SERVICE_EXTRAS_KEY_FAVORITES_MEDIA_ITEM`for passing Favorites media item in`MediaBrowserCompat`root extras. ([Id3a11](https://android-review.googlesource.com/#/q/Id3a11251c96b7e7727081840e36fe0e5cff24c5d))
- Add extras to set browse custom actions in`MediaBrowserCompat`root extras and`MediaItem`descriptions. ([Iab163](https://android-review.googlesource.com/#/q/Iab16398066d6e83661aa0806aefe1f1934a1fed1))

## Version 1.6.0

### Version 1.6.0

April 20, 2022

`androidx.media:media:1.6.0`is released.[Version 1.6.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/096a5a510b8fff3cdaee42a3f5f761f18e2e139d..c2abb1a63ad5d8a92cd723550b6989c767f86175/media/media)

**Important changes since 1.5.0**

- Add extras necessary to set up signIn/Settings page using`CarAppLibrary`on a media app for Android Auto.

### Version 1.6.0-rc01

April 6, 2022

`androidx.media:media:1.6.0-rc01`is released.[Version 1.6.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5ef5671233460b844828e14a816255dbf7904868..096a5a510b8fff3cdaee42a3f5f761f18e2e139d/media/media)

### Version 1.6.0-beta01

March 23, 2022

`androidx.media:media:1.6.0-beta01`is released.[Version 1.6.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8..5ef5671233460b844828e14a816255dbf7904868/media/media)

- No changes since the last alpha release.

### Version 1.6.0-alpha01

February 23, 2022

`androidx.media:media:1.6.0-alpha01`is released.[Version 1.6.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f3fbc72301a7099f3d49ce84f5a148d9ab5672c9..9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8/media/media)

**API Changes**

- Add extras necessary to set up signIn/Settings page using`CarAppLibrary`on a media app for Android Auto. ([Ifb3ca](https://android-review.googlesource.com/#/q/Ifb3ca10a7f66ddaec81775017f5c14c7760728d9))

## Version 1.5

### Version 1.5.0

February 9, 2022

`androidx.media:media:1.5.0`is released.[Version 1.5.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2da63a517f051d08f9fbd355d1dca4900e691038..f3fbc72301a7099f3d49ce84f5a148d9ab5672c9/media/media)

**Important changes since 1.4.0**

- Add`isVolumeFixed`to`AudioManagerCompat`
- Add`MediaConstants`for single item styling and completion percentage.
- For API level 30 or higher, the library won't inject the package visibility filter for`MediaBrowserCompat`. You need to specify a`<queries>`element in your apps manifest.
- Fix the unexpected change of extras of`getMediaDescription()`on API 21
- Prevent some`IllegalStateException`on API 19.
- Fix a crash in`MediaSessionCompat`when targeting Android 12
- Fix a crash in`NotificationCompat`on KitKat

### Version 1.5.0-rc01

January 26, 2022

`androidx.media:media:1.5.0-rc01`is released with no changes since`1.5.0-beta01`.[Version 1.5.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/75784ce6dbac6faa5320e5898e9472f02ab8710c..2da63a517f051d08f9fbd355d1dca4900e691038/media/media)

### Version 1.5.0-beta01

December 1, 2021

`androidx.media:media:1.5.0-beta01`is released with no changes since`1.5.0-alpha01`.[Version 1.5.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f07d12061370a603549747200c79b60239706330..75784ce6dbac6faa5320e5898e9472f02ab8710c/media/media)

### Version 1.5.0-alpha01

November 3, 2021

`androidx.media:media:1.5.0-alpha01`is released.[Version 1.5.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1f259226090fde0d482f2b0713630c8ee1328d73..f07d12061370a603549747200c79b60239706330/media/media)

**New Features**

- Update dependency on core for media to 1.6.0

**API Changes**

- Add isVolumeFixed to AudioManagerCompat
- Add MediaConstants for single item styling and completion percentage.

**Bug Fixes**

- For API level 30 or higher, the library won't inject the package visibility filter for`MediaBrowserCompat`. You need to specify a`<queries>`element in your apps manifest.
- Fix the unexpected change of extras of getMediaDescription() on API 21
- Fix inefficient use of ArrayList by setting default size.
- Prevent some IllegalStateException on API 19.
- Fix a crash in MediaSessionCompat when targeting Android 12
- Fix a crash in NotificationCompat on KitKat

## Version 1.4

### Version 1.4.3

October 13, 2021

`androidx.media:media:1.4.3`is released.[Version 1.4.3 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/eec2516768db31d15b880824523c0eb380d978e6..1f259226090fde0d482f2b0713630c8ee1328d73/media/media)

**Bug Fixes**

- The library won't inject the package visibility filter for`MediaBrowserCompat`anymore. Please specify a`<queries>`element in your apps manifest when targeting API level 30 or higher. ([I0a964](https://android-review.googlesource.com/#/q/I0a964e51887211650279b9bd1efd79ce4c5bb5c2),[b/185314633](https://issuetracker.google.com/issues/185314633))

### Version 1.4.2

September 15, 2021

`androidx.media:media:1.4.2`is released.[Version 1.4.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/05c3ad7166c3859d0a8da6e8786a9d3b6f54efbe..eec2516768db31d15b880824523c0eb380d978e6/media/media)

**Bug Fixes**

- Fix side-effect of`getMediaDescription()`on API 21 ([I5c05f](https://android-review.googlesource.com/#/q/I5c05ff1f995820a2c3efb7d8861b3514ddfb2ae7))

### Version 1.4.1

August 4, 2021

`androidx.media:media:1.4.1`is released.[Version 1.4.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1d797e449a5d71eb3b46febbc8dddc1d5e57eb27..05c3ad7166c3859d0a8da6e8786a9d3b6f54efbe/media/media)

**Bug Fixes**

- Fix mutability flag for creating`PendingIntent`to prevent crash when targeting Android S.
- Fix ClassVerificationFailure for`NotificationCompat.MediaStyle`.

### Version 1.4.0

July 21, 2021

`androidx.media:media:1.4.0`is released.[Version 1.4.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/dbd565a0becb2aa026b58af3b04c56b35c554290..1d797e449a5d71eb3b46febbc8dddc1d5e57eb27/media/media)

**Important changes since 1.3.0**

- Added a new bundle key`METADATA_KEY_SERIES_CONTENT_ID`used for the TV series's media content ID in MediaMetadataCompat
- Added a new bundle key`METADATA_KEY_NEXT_EPISODE_CONTENT_ID`used for the TV episode's next episode content ID in MediaMetadataCompat
- Deprecate`MediaControllerCompat.TransportControls#EXTRA_LEGACY_STREAM_TYPE`and add`MediaConstants#TRANSPORT_CONTROLS_EXTRAS_KEY_LEGACY_STREAM_TYPE`instead
- Add an extra key to shuffle media for playFromUri
- Add @Nullable annotation to Result class
- Fix missing`EXTRA_KEY_EVENT`of intent for MediaButtonReceiver

### Version 1.4.0-rc01

June 30, 2021

`androidx.media:media:1.4.0-rc01`is released with no changes since`1.4.0-beta01`.[Version 1.4.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6c4d1b95a2dbd4dabd5d15d99b18b691a943d32a..dbd565a0becb2aa026b58af3b04c56b35c554290/media/media)

### Version 1.4.0-beta01

June 17, 2021

`androidx.media:media:1.4.0-beta01`is released.[Version 1.4.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3d6f168394d1dd14e1d6f5b6dc4a0d405cb1a26a..6c4d1b95a2dbd4dabd5d15d99b18b691a943d32a/media/media)

**API Changes**

- Added a new bundle key`METADATA_KEY_SERIES_CONTENT_ID`used for the TV series's media content ID in`MediaMetadataCompat`

- Added a new bundle key`METADATA_KEY_NEXT_EPISODE_CONTENT_ID`used for the TV episode's next episode content ID in`MediaMetadataCompat`

### Version 1.4.0-alpha01

May 5, 2021

`androidx.media:media:1.4.0-alpha01`is released.[Version 1.4.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/612741347a477b0647a2a8b94b1e7d40aa91abaa..3d6f168394d1dd14e1d6f5b6dc4a0d405cb1a26a/media/media)

**API Changes**

- Deprecate`MediaControllerCompat.TransportControls#EXTRA_LEGACY_STREAM_TYPE`and add`MediaConstants#TRANSPORT_CONTROLS_EXTRAS_KEY_LEGACY_STREAM_TYPE`instead ([I62f17](https://android-review.googlesource.com/#/q/I62f172373ac24f4c883f46c86740651264c3c049))
- Add an extra key to shuffle media for playFromUri ([Ibc63c](https://android-review.googlesource.com/#/q/Ibc63c77f4f79c9279d809aab837c7d25a621930e))
- Add @Nullable annotation to Result class ([I2d617](https://android-review.googlesource.com/#/q/I2d61708d314224ac945f34699f1f46a21aed32fb))

**Bug Fixes**

- Fix missing`EXTRA_KEY_EVENT`of intent for MediaButtonReceiver ([If7557](https://android-review.googlesource.com/#/q/If755747418aca8b76b12cbce13ffed2c7dedb038))

## Version 1.3.1

### Version 1.3.1

May 5, 2021

`androidx.media:media:1.3.1`is released.[Version 1.3.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/612741347a477b0647a2a8b94b1e7d40aa91abaa..51bc56c58cf5159c3df4a8b324914e16695e33ed/media/media)

**Bug Fixes**

- Fix missing EXTRA_KEY_EVENT of intent for MediaButtonReceiver ([If7557](https://android-review.googlesource.com/#/q/If755747418aca8b76b12cbce13ffed2c7dedb038))

## Version 1.3.0

### Version 1.3.0

April 7, 2021

`androidx.media:media:1.3.0`is released.[Version 1.3.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b676241c1174d10580a889743248a2cd1b315dd0..612741347a477b0647a2a8b94b1e7d40aa91abaa/media/media)

**Major changes since 1.2.0**

- Migrated Android Auto extras into MediaConstants.

### Version 1.3.0-rc02

March 24, 2021

`androidx.media:media:1.3.0-rc02`is released.[Version 1.3.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f3234e2c593978c340dcbd7bf815df23317517ef..b676241c1174d10580a889743248a2cd1b315dd0/media/media)

**Bug Fixes**

- Set`FLAG_IMMUTABLE`to the PendingIntent of MediaButtonReceiver which is required for apps targeting Android 12.
- Fixed a`NullPointerException`in`MediaSessionCompat`with API 27 after`setCallback(null)`.

### Version 1.3.0-rc01

March 10, 2021

`androidx.media:media:1.3.0-rc01`is released.[Version 1.3.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/602cf9bff5e74e4355760aa47d3fc73a2e6d779b..f3234e2c593978c340dcbd7bf815df23317517ef/media/media)

No changes since`1.3.0-beta01`.

### Version 1.3.0-beta01

February 10, 2021

`androidx.media:media:1.3.0-beta01`is released.[Version 1.3.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/adda37c5227583112f0eec016de90fe5071fde10..602cf9bff5e74e4355760aa47d3fc73a2e6d779b/media/media)

**API Changes**

- Added a new constant`PlaybackStateCompat.ACTION_SET_PLAYBACK_SPEED`([I9d076](https://android-review.googlesource.com/#/q/I9d076e2a6fe371dffec7996ccebeb40d47d9aad4))
- Migrate Android Auto extras into MediaConstants. ([I290ab](https://android-review.googlesource.com/#/q/I290ab73e28b3b21fb990f233c1744a03300eb79a))
- Add constants for constraining root children of MediaBrowserService. ([Ifcebd](https://android-review.googlesource.com/#/q/Ifcebdc8d31d0d5ccbda8f89584b67e8bf0222045))

**Bug Fixes**

- Add`FLAG_RECEIVER_FOREGROUND`for media button pending intent.

## Version 1.2.1

### Media Version 1.2.1

December 2, 2020

`androidx.media:media:1.2.1`is released.[Version 1.2.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c4c67254615340e5557e3a1a3be0483f6e0c69c8..adda37c5227583112f0eec016de90fe5071fde10/media/media)

**Bug Fixes**

- Fix NPE after calling`MediaSessionCompat#setCallback(null)`in API 27

## Version 1.2.0

### Version 1.2.0

September 16, 2020

`androidx.media:media:1.2.0`is released.[Version 1.2.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/15854c1bc7a06d62e37507d9c4132bd229904da2..c4c67254615340e5557e3a1a3be0483f6e0c69c8/media/media)

**Major changes since 1.1.0**

- Added support for`AudioAttributesCompat#setLegacyStreamType`for SDK \< 21
- Support volume control for the`androidx.mediarouter`library
- Better support of interoperability between`androidx.media`and`androidx.media2`

### Version 1.2.0-rc01

September 2, 2020

`androidx.media:media:1.2.0-rc01`is released with no changes since`1.2.0-beta01`.[Version 1.2.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/96eb302ee1740ba656c90c9fb27df3723a1a89c1..15854c1bc7a06d62e37507d9c4132bd229904da2/media/media)

### Version 1.2.0-beta01

August 19, 2020

`androidx.media:media:1.2.0-beta01`is released.[Version 1.2.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b6054a1a7396b962ac2c6d80d21053cf9d2f02db..96eb302ee1740ba656c90c9fb27df3723a1a89c1/media/media)

**New Features**

- Added support for`AudioAttributesCompat#setLegacyStreamType`for API Leves Pre-21

**API Changes**

- Added`MediaConstants#PLAYBACK_STATE_EXTRAS_KEY_MEDIA_ID`for the media id in`PlaybackStateCompat`extras, which is expected to be same as`MediaMetadataCompat#METADATA_KEY_MEDIA_ID`of the current metadata.

**Bug Fixes**

- Fixed an issue with`AudioAttributesCompat.Builder#setContentType`

### Version 1.2.0-alpha04

June 24, 2020

`androidx.media:media:1.2.0-alpha04`is released.[Version 1.2.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/945594abd75f83bd14daf4fbcd8621796161281e..b6054a1a7396b962ac2c6d80d21053cf9d2f02db/media/media)

**New Features**

- Provided a way to support volume control for mediarouter library

**API Changes**

- Added`AudioManagerCompat#getStreamMaxVolume`
- Added`AudioManagerCompat#getStreamMinVolume`

**Bug Fixes**

- Fixed an interoperability issue between media and media2 on SDK \< 21

### Version 1.2.0-alpha03

June 10, 2020

`androidx.media:media:1.2.0-alpha03`is released.[Version 1.2.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/24daa503442fcd3e44ada60cf1da41df2815c045..945594abd75f83bd14daf4fbcd8621796161281e/media/media)

**API Changes**

- `MediaConstants.SESSION_EXTRAS_KEY_AUTHTOKEN`has been removed

**Bug Fixes**

- Fixed an issue with`equals()`of`RemoteUserInfo`

### Version 1.2.0-alpha02

April 15, 2020

`androidx.media:media:1.2.0-alpha02`is released.[Version 1.2.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f14ad350142290622d1645e1d0e280cbe8ca4c2f..24daa503442fcd3e44ada60cf1da41df2815c045/media/media)

**Bug Fixes**

- Prevent modifications of VersionedParcelable classes

### Version 1.2.0-alpha01

October 23, 2019

`androidx.media:media:1.2.0-alpha01`is released.[Version 1.2.0-alpha01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/de87d1aef00e890a6117a03ca8af2168b2227bc5..f14ad350142290622d1645e1d0e280cbe8ca4c2f/media).

**API changes**

- Added the following methods:
  - `MediaSessionCompat.Callback.onSetPlaybackSpeed()`
  - `MediaControllerCompat.setPlaybackSpeed()`
  - `MediaControllerCompat.getSessionInfo()`

**Bug fixes**

- Implemented prevention against a`BadParcelableException`when passing a Bundle object via an IPC call
- The constructor of`MediaControllerCompat`no longer throws a`RemoteException`
- Implemented prevention against the calling of callback methods after`MediaSessionCompat.release()`

## Version 1.1.0

### Version 1.1.0

September 5, 2019

`androidx.media:media:1.1.0`is released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/592463aebbf62f711611f85522f69023d72ced1e..460368c87954857d895ce075cb139fd1c4eb53ee/media).

**Import changes since 1.0.0**

- Introduced`AudioAttributesCompat`

### Version 1.1.0-rc01

June 13, 2019

`androidx.media:media:1.1.0-rc01`is released with no changes from`1.1.0-beta02`. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/032065fa1470140b8cc92df73ebaac6479d2e2a6..592463aebbf62f711611f85522f69023d72ced1e/media).

### Version 1.1.0-beta02

June 5, 2019

`androidx.media:media:1.1.0-beta02`is released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/2c7181c30858d401daba909d0a9400d5fc8d16d9..047b66e9ecaa38df8f4977ef7b6f9392a2a48da8/media).

**Bug fixes**

- The restriction scope of hidden methods that are used by`media2-session`has been relaxed to`LIBRARY_GROUP_PREFIX`.

### Version 1.1.0-beta01

May 7, 2019

`androidx.media:media:1.1.0-beta01`is released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/38c07ac6fed103450aa5949a4c12729d1480d72f..2c7181c30858d401daba909d0a9400d5fc8d16d9/media).

**New features**

- Changed`IllegalPointerException`to`NullPointerException`for the null arguments which marked as`@NonNull`.

### Version 1.1.0-alpha04

April 3, 2019

`androidx.media:media:1.1.0-alpha04`is released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/8c6ad7c45d31d86030e9ad2d43f59472fb771a10..38c07ac6fed103450aa5949a4c12729d1480d72f/media).

**Bug fixes**

- Tweak on a version-compat-test constant ([aosp/933656](https://android-review.googlesource.com/c/platform/frameworks/support/+/933656))

### Version 1.1.0-alpha03

March 21st, 2019

`androidx.media:media:1.1.0-alpha03`is released. The full list of commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/e5cd630912f6f9165114ab5ae9b2aead36cfc713..8c6ad7c45d31d86030e9ad2d43f59472fb771a10/media).

**Bug fixes**

- Fixed crash of`MedaBrowserServiceCompat`when multiple`MediaBrowserCompat`try to connect to it. ([aosp/930246](https://android-review.googlesource.com/930246))

### Version 1.1.0-alpha02

March 13, 2019
| **Note:** Please upgrade to version[1.1.0-alpha03](https://developer.android.com/jetpack/androidx/releases/media#1.1.0-alpha03)if you'd like to use these new features. Version[1.1.0-alpha03](https://developer.android.com/jetpack/androidx/releases/media#1.1.0-alpha03)contains a critical bugfix to`MedaBrowserServiceCompat`;[aosp/930246](https://android-review.googlesource.com/930246).

`androidx.media:media:1.1.0-alpha02`is released. The full list of commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/b9925c3695ce7da0625a2fd3ded0149b7153826c..e5cd630912f6f9165114ab5ae9b2aead36cfc713/media).

**Bug fixes**

- Fixed crash of`MediaBrowserCompat`while connecting
- Fixed`IllegalStateException`happened in`getCurrentBrowserInfo()`/`getBrowserRootHints()`
- Make`MediaBrowserServiceCompat.getCurrentBrowserInfo()`return the same`RemoteUserInfo`instance for the same`MediaBrowserCompat`in`onGetRoot()`

## Version 1.0.1

### Version 1.0.1

January 30, 2019

`androidx.media:media 1.0.1`is released.

**Bug fixes**

- Fixed bug of an unexpected IllegalStateException while using`MediaBrowserCompat.connect()`([aosp/858075](https://android-review.googlesource.com/858075))

## Version 1.0.0

### Version 1.0.0-alpha06

December 17, 2018

**API changes**

Renamed the`media.widget`package and class names as follows:

- `androidx.media.widget.VideoView2`→`androidx.media2.widget.VideoView`
- `androidx.media.widget.MediaControlView2`→`androidx.media2.widget.MediaControlView`

### Version 1.0.0-alpha01

December 3, 2018

**API changes**

- Deprecated two`MediaSessionCompat`flags:
  - `FLAG_HANDLES_MEDIA_BUTTONS`
  - `FLAG_HANDLES_TRANSPORT_CONTROLS`