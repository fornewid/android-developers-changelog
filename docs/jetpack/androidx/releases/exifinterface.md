---
title: https://developer.android.com/jetpack/androidx/releases/exifinterface
url: https://developer.android.com/jetpack/androidx/releases/exifinterface
source: md.txt
---

# Exifinterface

[Code Sample](https://github.com/android/camera-samples/blob/master/CameraUtils/lib/src/main/java/com/example/android/camera/utils/ExifUtils.kt)  
API Reference  
[androidx.exifinterface.media](https://developer.android.com/reference/kotlin/androidx/exifinterface/media/package-summary)  
Read and write image file EXIF tags.  

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| December 3, 2025 | [1.4.2](https://developer.android.com/jetpack/androidx/releases/exifinterface#1.4.2) | - | - | - |

## Declaring dependencies

To add a dependency on Exifinterface, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:  

### Groovy

```groovy
dependencies {
    implementation "androidx.exifinterface:exifinterface:1.4.2"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.exifinterface:exifinterface:1.4.2")
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:460705+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=460705&template=1238586)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 1.4

### Version 1.4.2

December 03, 2025

`androidx.exifinterface:exifinterface:1.4.2` is released. Version 1.4.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/63af1a240d10ff7128cb64b905ae0efde6b94270..68ebfa7071e3aace695af9332e7b0193a45f5d53/exifinterface/exifinterface).

**Bug Fixes**

- Support parsing JPEGs with additional (permitted ) 0xFF bytes before any marker.

### Version 1.4.1

April 23, 2025

`androidx.exifinterface:exifinterface:1.4.1` is released. Version 1.4.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/dd9ccceb1eca63c154ca56cd6d17792bff160082..63af1a240d10ff7128cb64b905ae0efde6b94270/exifinterface/exifinterface).

**Bug Fixes**

- Fix bug where passing null to `setAttribute` for `TAG_XMP` would throw an exception.

### Version 1.4.0

February 26, 2025

`androidx.exifinterface:exifinterface:1.4.0` is released. Version 1.4.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/324bc08271a8808e541d9261189b5ed572076528..dd9ccceb1eca63c154ca56cd6d17792bff160082/exifinterface/exifinterface).

### Version 1.4.0-rc01

January 29, 2025

`androidx.exifinterface:exifinterface:1.4.0-rc01` is released with no changes since beta01. Version 1.4.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ad66672b42ec1e9359219e82b7f8189d03df40f5..324bc08271a8808e541d9261189b5ed572076528/exifinterface/exifinterface).

### Version 1.4.0-beta01

January 15, 2025

`androidx.exifinterface:exifinterface:1.4.0-beta01` is released. Version 1.4.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6f09cf2ae979e48fdb19485f757a033e4a34bb82..ad66672b42ec1e9359219e82b7f8189d03df40f5/exifinterface/exifinterface).

**API Changes**

- Update HEIC XMP handling to prefer XMP data from a separate segment in the file, rather than tag 700 in the Exif data.

**Bug Fixes**

- Fix `ExifInterface.getThumbnail*()` method to work correctly after a call to `saveAttributes()` (previously the calls would succeed, but the result would be incorrect/undefined)
- Fix PNG XMP handling to read and write the separate iTXt XMP chunk instead of tag 700 inside the eXIf chunk.
- Fix `WebP` image corruption when handling image files with trailing non-WebP data. ([b/385766064](https://issuetracker.google.com/385766064)).

### Version 1.4.0-alpha01

November 13, 2024

`androidx.exifinterface:exifinterface:1.4.0-alpha01` is released. Version 1.4.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/90d685e3591d448bbd5ebdaab90653d87ae3d91e..6f09cf2ae979e48fdb19485f757a033e4a34bb82/exifinterface/exifinterface).

**New Features**

- Add support for reading XMP data from HEIF images.
- Add support for reading Exif and XMP from AVIF images.

**API Changes**

- Indicate that the `location` param for `setGpsInfo` is `@Nullable` and that passing `null` will result in a No-Op. ([If924c](https://android-review.googlesource.com/#/q/If924cd23c58f32cbb112db98cdd3d988105c9429), [b/236484611](https://issuetracker.google.com/issues/236484611))

**Bug Fixes**

- Continue parsing after encountering an invalid IFD offset ([b/264729367](https://issuetracker.google.com/264729367)).
- Handle WebP images which incorrectly contain a JPEG APP1 marker before their Exif data ([b/281638358](https://issuetracker.google.com/281638358)).
- Ensure XMP changes in JPEGs with a separate XMP segment are stored into the same separate XMP segment by `saveAttributes()`, instead of being written to TIFF/Exif tag 700 which is not supported by the XMP spec and where many tools won't find them.
- Avoid duplicating XMP data from a separate segment into the TIFF preview directory when saving ([b/309843390](https://issuetracker.google.com/309843390)).
- Improve precision of double to rational conversions. ([b/312680558](https://issuetracker.google.com/312680558)).
- Accept rational format (x/y) to `setAttribute` for 'legacy' rational tags which are auto-converted to decimal when returned from `getAttribute` ([b/312680558](https://issuetracker.google.com/312680558)).
- Ensure XMP data added to a JPEG image which doesn't already contain XMP is written to a separate segment, as specified by the XMP spec. `ExifInterface` is documented to prefer the XMP in the Exif 700 tag in JPEG images (violating the spec), so this behavior is preserved when reading/writing images with existing XMP data.
- Fix corrupted output when writing WebP images with a height or width greater than 8191px ([b/342697059](https://issuetracker.google.com/342697059)).
- This library now uses [JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler argument to enforce correct usage: `-Xjspecify-annotations=strict` (this is the default starting with version 2.1.0 of the Kotlin compiler). ([I5cd0f](https://android-review.googlesource.com/#/q/I5cd0fe313cfeb326ac1b9348f85113af2d5fd676), [b/326456246](https://issuetracker.google.com/issues/326456246))
- Removed manual outlining of access to new platform APIs since this happens automatically via API modeling when using R8 with AGP 7.3 or later (e.g. R8 version 3.3) and for all builds when using AGP 8.1 or later (e.g. D8 version 8.1). Clients who are not using AGP are advised to update to D8 version 8.1 or later. See [this article](https://medium.com/androiddevelopers/mitigating-soft-verification-issues-in-r8-and-d8-7e9e06827dfd) for more details. ([If6b4c](https://android-review.googlesource.com/#/q/If6b4ccfca0a943b45971a422b58949b13a10bada), [b/345472586](https://issuetracker.google.com/issues/345472586))

## Version 1.3.7

### Version 1.3.7

December 13, 2023

`androidx.exifinterface:exifinterface:1.3.7` is released. [Version 1.3.7 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/00bc5313008ea35c4c78635d300238697527b76b..90d685e3591d448bbd5ebdaab90653d87ae3d91e/exifinterface/exifinterface)

**Bug Fixes**

- Throw an exception from `ExifInterface.saveAttributes()` when trying to write a JPEG APP1 segment that's too large (previously we would write an invalid APP1 segment with an incorrect, truncated, length:([b/263747161](https://issuetracker.google.com/263747161))). Continue parsing after encountering an invalid IFD offset (previously parsing would halt immediately, which could result in incorrect values being returned: ([b/264729367](https://issuetracker.google.com/264729367))).

## Version 1.3.6

### Version 1.3.6

February 8, 2023

`androidx.exifinterface:exifinterface:1.3.6` is released. [Version 1.3.6 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d612296ef9c639d7fb1830a1b668692204d6786c..00bc5313008ea35c4c78635d300238697527b76b/exifinterface/exifinterface)

**Bug Fixes**

- Fix reading of alpha bit from WebP VP8L chunks ([b/255405635](https://issuetracker.google.com/255405635)).

## Version 1.3.5

### Version 1.3.5

October 24, 2022

`androidx.exifinterface:exifinterface:1.3.5` is released. [Version 1.3.5 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/655c07001b4cd48fc380eb24b6be95583a2e67f3..d612296ef9c639d7fb1830a1b668692204d6786c/exifinterface/exifinterface)

**Bug Fixes**

- Fix two cases of `saveAttributes()` producing invalid WebP files.

## Version 1.3.4

### Version 1.3.4

October 5, 2022

`androidx.exifinterface:exifinterface:1.3.4` is released. [Version 1.3.4 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2a2663bc8cbda3f59b4c0387b92ce9c74c3492b6..655c07001b4cd48fc380eb24b6be95583a2e67f3/exifinterface/exifinterface)

**Bug Fixes**

- Remove support for saving attributes to DNG files. The support added in 1.3.3 was incomplete and produced corrupted files.

## Version 1.3.3

### Version 1.3.3

August 4, 2021

`androidx.exifinterface:exifinterface:1.3.3` is released. [Version 1.3.3 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a54af0aba131d0a6fff39aaf991e9e713ab9777f..2a2663bc8cbda3f59b4c0387b92ce9c74c3492b6/exifinterface/exifinterface)

**Bug Fixes**

- Fix parsing subsec-related tags. ([aosp/1508143](https://android-review.googlesource.com/c/platform/frameworks/support/+/1508143))
- Prevent RuntimeException when calling setDataSource. ([c8e66e9](https://android.googlesource.com/platform/frameworks/support/+/c8e66e9039c7bccb3bce6d9b40b80f12f1f42eba))
- Prevent skipBytes from infinitely looping. ([fdbe88b](https://android.googlesource.com/platform/frameworks/support/+/fdbe88b8753e72d1c6136aa3df29b55c0c8e704e))
- Catch RuntimeException from MediaMetadataRetriever. ([389b21a](https://android.googlesource.com/platform/frameworks/support/+/389b21a687663a13b894d69dde9a10ca6de9f548))
- Add support for saving attributes for DNG files ([3017dbc](https://android.googlesource.com/platform/frameworks/support/+/3017dbcbebc1868f0e541c65138a6d875aeb1e49))
- Replace non-thumbnail tags with thumbnail tags. ([e1b916d](https://android.googlesource.com/platform/frameworks/support/+/e1b916d1f235df260f6ec5d8ecc1c1797634e232))

## Version 1.3.2

### Version 1.3.2

December 2, 2020

`androidx.exifinterface:exifinterface:1.3.2` is released. [Version 1.3.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1a06c0f440d56e6f7f092c0b32a6143fe303adf5..a54af0aba131d0a6fff39aaf991e9e713ab9777f/exifinterface/exifinterface)

**Bug Fixes**

- Allows `SRATIONAL` for `GPS_LATITUDE` and `GPS_LONGITUDE`.
- Added support for reading/writing a secondary format (2020-01-01 00:00:00) of the DateTime tag.
- Prevented the temporary removal of the origin file while calling saveAttribute().

## Version 1.3.1

### Version 1.3.1

October 14, 2020

`androidx.exifinterface:exifinterface:1.3.1` is released. [Version 1.3.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d86967e221b1c0b8c6e0de2de52df614e028685e..1a06c0f440d56e6f7f092c0b32a6143fe303adf5/exifinterface/exifinterface)

**Bug Fixes**

- Fix saveAttributes implementation to keep the image data in MediaProvider

## Version 1.3.0

### Version 1.3.0

September 16, 2020

`androidx.exifinterface:exifinterface:1.3.0` is released. [Version 1.3.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/15854c1bc7a06d62e37507d9c4132bd229904da2..d86967e221b1c0b8c6e0de2de52df614e028685e/exifinterface/exifinterface)

**Major changes since 1.2.0**

- Extended WebP EXIF writing support to include files that only contain VP8 or VP8L chunks.
- Removed unnecessary buffering, which was causing OutOfMemory exceptions for large image files.
- Removed `INVALID_DATE_TIME`. Instead use `NULL` to return invalid datetime values.
- Made `getGpsDateTime` return `Long.MIN_VALUE` instead of `-1` for an invalid value.

### Version 1.3.0-rc01

September 2, 2020

`androidx.exifinterface:exifinterface:1.3.0-rc01` is released with no changes since `1.3.0-beta01`. [Version 1.3.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/96eb302ee1740ba656c90c9fb27df3723a1a89c1..15854c1bc7a06d62e37507d9c4132bd229904da2/exifinterface/exifinterface)

### Version 1.3.0-beta01

August 19, 2020

`androidx.exifinterface:exifinterface:1.3.0-beta01` is released. [Version 1.3.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6f7b9ed69dc63e3c2c2b02ee1155b6009a9d5f82..96eb302ee1740ba656c90c9fb27df3723a1a89c1/exifinterface/exifinterface)

**New Features**

- Extended WebP EXIF writing support to include files that only contain VP8 or VP8L chunks.

**API Changes**

- Removed `INVALID_DATE_TIME`. Instead use `NULL` to return invalid datetime value.

**Bug Fixes**

- Made `getGpsDateTime` return `Long.MIN_VALUE` instead of `-1` becuase `-1` is a valid value
- Made DateTime-related getters consider offset value (+/-) of date string.
- Removed unnecessary buffering, which was causing OutOfMemory exceptions for large image files.
- Set default locale to US
- Replaced adding ".tmp" for creating temp files to adding a prefix.

### Version 1.3.0-alpha01

February 19, 2020

`androidx.exifinterface:exifinterface:1.3.0-alpha01` is released. [Version 1.3.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d5e6675db6f6b1c9317dc1c82b8f0bed06694a87..6f7b9ed69dc63e3c2c2b02ee1155b6009a9d5f82/exifinterface/exifinterface)

**API Changes**

- Added a new method: `ExifInterface.getGpsDateTime()`

## Version 1.2.0

### Version 1.2.0

April 1, 2020

`androidx.exifinterface:exifinterface:1.2.0` is released. [Version 1.2.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/986ebacc6810b886802b3e4175bb0b96c64f5d0b..c9821580a88632050c4599dcb02f6cf8e231f7e3/exifinterface/exifinterface)

**Major changes since 1.1.0**

- Added support for adding EXIF to PNG files
- Added support for WebP files and EXIF data only stream
- Added an API to check if the specified mime type is supported
- Added more tags for offset time: `TAG_OFFSET_TIME`, `TAF_OFFSET_TIME_DIGITIZED`, and `TAG_OFFSET_TIME_ORIGINAL`

### Version 1.2.0-rc01

February 19, 2020

`androidx.exifinterface:exifinterface:1.2.0-rc01` is released. [Version 1.2.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d5e6675db6f6b1c9317dc1c82b8f0bed06694a87..986ebacc6810b886802b3e4175bb0b96c64f5d0b/exifinterface/exifinterface)

**Bug Fixes**

- Fixed an issue where JPEG files were incorrected saved if the JPEG had XMP data

### Version 1.2.0-beta01

December 18, 2019

`androidx.exifinterface:exifinterface:1.2.0-beta01` is released. [Version 1.2.0-beta01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/4075a57e3d23631e5690a18b9c73e137957e8faa..d5e6675db6f6b1c9317dc1c82b8f0bed06694a87/exifinterface).

**New features**

- Added support for adding EXIF to PNG files
- Added support support for reading and writing EXIF from WebP files
- Added support for an EXIF data only stream

**API changes**

- Added an API to check if the specified mime type is supported
- Exposed the read and write OffsetTime\* tags

**Bug fixes**

- Fixed an issue where the incorrect offsets were being returned for `getAttributeRange()`

## Version 1.1.0

### Version 1.1.0

November 20, 2019

`androidx.exifinterface:exifinterface:1.1.0` is released. [Version 1.1.0 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/c4b30ffe0c8946d8a2e37d6a977dd2108c45d3e1..f7d68d8a9811421537d90837f94eed93cc732754/exifinterface).

**Important changes since 1.0.0**

- Support for HEIF format and more XMP tags
- Added support for constructing an `ExifInterface` object from a `File` or `FileDescriptor`
- Added more methods for getting attribute: `hasAttribute`, `getAttributeBytes`, and `getAttributesRange`

### Version 1.1.0-rc01

October 9, 2019

`androidx.exifinterface:exifinterface:1.1.0-rc01` is released. [Version 1.1.0-rc01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/d6a77c87bb913a6393a2185e5552eae55267b204..4075a57e3d23631e5690a18b9c73e137957e8faa/exifinterface).

**Bug fixes**

- Added a missing format name (IFD) to prevent an `ArrayIndexOutOfBoundsException` on `loadAttributes`
- Prevented the deletion of the origin file when an exception happens while calling `saveAttributes`
- Fixed an exception issue when there is a call to `saveAttributes()` after overwriting a file.

### Version 1.1.0-beta01

July 2, 2019

`androidx.exifinterface:exifinterface:1.1.0-beta01` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/0b2c8b5a3ea18e80b32b57c49dba74c2812946ee..d6a77c87bb913a6393a2185e5552eae55267b204/exifinterface).

**New features**

- Throws `NullPointerException` when `null` is set for `@NonNull` arguments
- Support for XMP tags

**API changes**

- Added more methods for getting attribute info
- `hasAttribute`, `getAttributeBytes`, and `getAttributesRange`

**Bug fixes**

- Prevent file descriptor memory leak

### Version 1.1.0-alpha01

March 13, 2019

`androidx.exifinterface:exifinterface:1.1.0-alpha01` is released. The full list of commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/3478ef7cbc6b27d8c1497d76c3ffff688771380e..0b2c8b5a3ea18e80b32b57c49dba74c2812946ee/exifinterface).

**New features**

- Support HEIF format

**API changes**

- Added more constructors of ExifInterface
- Fixed Typo: `TAG_CAMARA_OWNER_NAME` -\> `TAG_CAMERA_OWNER_NAME`

**Bug fixes**

- Fixed the check of possible overflow for thumbnail image ([aosp/748608](https://android-review.googlesource.com/c/748608))