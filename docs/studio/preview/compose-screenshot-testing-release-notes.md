---
title: https://developer.android.com/studio/preview/compose-screenshot-testing-release-notes
url: https://developer.android.com/studio/preview/compose-screenshot-testing-release-notes
source: md.txt
---

> [!WARNING]
> **Experimental:** Compose Preview Screenshot Testing is still in development. Its features and APIs are subject to change substantially during the alpha phase. Report any feedback and issues through the [issue tracker](https://issuetracker.google.com/issues/new?component=192708&template=840533).

### 0.0.1-alpha14

This release includes the following bug fixes and performance improvements:

| Issue | Description |
|---|---|
| [issue #469819154](https://issuetracker.google.com/issues/469819154) | Fixed memory leaks in the Compose renderer. |
| [issue #470058578](https://issuetracker.google.com/issues/470058578) | Fixed UI freezes and memory errors when updating reference images. |
| [issue #422412664](https://issuetracker.google.com/issues/422412664) | Fixed "command line exceeds operating system limits" errors on Windows and GitHub Actions. |
| [issue #437223807](https://issuetracker.google.com/issues/437223807) | Fixed resource and asset resolution issues in multi-module projects. |
| [issue #464899800](https://issuetracker.google.com/issues/464899800) | Fixed a Gradle plugin conflict caused by a naming collision in `version.properties`. |
| [issue #482433854](https://issuetracker.google.com/issues/482433854) | Fixed initialization errors for composables using `kotlin-reflect` or serialization. |

### 0.0.1-alpha13

This release introduces:

- Compatibility with JDK 17 or higher.
- Bug fixes and improved integration with Android Studio.

### 0.0.1-alpha12

This release introduces:

- Compatibility with Android Gradle Plugin (AGP) 9.0.
- Support for running screenshot tests on JDK 24 and higher.
- Support to configure maximum heap size.
- Fixed rendering failures and improved test stability.
- Enhanced the reporting to include percentage difference and other metadata related to new and reference images.

### 0.0.1-alpha11

This release introduces:

- Compatibility with Android Gradle Plugin (AGP) 8.13.
- Added support for parsing XML drawables with decimal values regardless of the host machine's locale.
- For a host machine using JDK 24 or higher, compatible JDK (11-23) will be picked up, provided one is installed.

### 0.0.1-alpha10

This release introduces:

- From this version, you need to mark all of your preview functions with the
  `@PreviewTest` annotation. Previews without the annotation won't be executed.

- Reference image directory is changed from
  `{module}/src/{variant}/screenshotTest/reference` to
  `{module}/src/screenshotTest{Variant}/reference`. This is to make sure those
  generated reference images won't be part of the production code, and to be
  aligned with the [directory structure](https://developer.android.com/studio/test/advanced-test-setup#create-instrumented-test-for-build-variant) of other test types.

- The `{variant}PreviewScreenshotRender` task is removed. Image rendering is
  migrated into JUnit Test Engine.

- The `update{Variant}ScreenshotTest` task will compare new rendering images to
  reference images before updating. It will only update images that have
  differences greater than a specified threshold. The `--updateFilter`
  command-line flag was removed.

### 0.0.1-alpha06

This release introduces:

Image Difference Threshold: This new global threshold setting will allow you to
gain finer control over screenshot comparisons. To configure, update your
module's build.gradle.kts:

        testOptions {
            screenshotTests {
                imageDifferenceThreshold = 0.0001f // 0.01%
            }
        }

This threshold will be applied to all screenshot tests defined in the module.

- Bug Fixes: Some Compose Renderer bugs and added support for empty compose.
- Performance Enhancements: Image diffing algorithm was updated to be faster.