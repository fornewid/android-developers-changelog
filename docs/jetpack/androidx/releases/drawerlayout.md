---
title: https://developer.android.com/jetpack/androidx/releases/drawerlayout
url: https://developer.android.com/jetpack/androidx/releases/drawerlayout
source: md.txt
---

# Drawerlayout

# Drawerlayout

[User Guide](https://developer.android.com/guide/navigation/navigation-ui#add_a_navigation_drawer)[Code Sample](https://github.com/android/views-widgets-samples/tree/main/ConstraintLayoutExamples)  
API Reference  
[androidx.drawerlayout.widget](https://developer.android.com/reference/kotlin/androidx/drawerlayout/widget/package-summary)  
Implement a Material Design drawer widget.  

| Latest Update  |                                   Stable Release                                    | Release Candidate | Beta Release | Alpha Release |
|----------------|-------------------------------------------------------------------------------------|-------------------|--------------|---------------|
| March 22, 2023 | [1.2.0](https://developer.android.com/jetpack/androidx/releases/drawerlayout#1.2.0) | -                 | -            | -             |

## Declaring dependencies

To add a dependency on DrawerLayout, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    implementation "androidx.drawerlayout:drawerlayout:1.2.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.drawerlayout:drawerlayout:1.2.0")
}
```

For more information about dependencies, see[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:460398+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=460398&template=1422651)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.2

### Version 1.2.0

March 22, 2023

`androidx.drawerlayout:drawerlayout:1.2.0`is released.[Version 1.2.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/fbc749d6e72aa21157e8005fb3517a6d4853fe47..5fb21d2c2b331b0950b9de94e8364c3e5a64b0ea/drawerlayout/drawerlayout)

**Important changes since 1.1.0**

- `DrawerLayout`now integrates with Android 13's`OnBackPressedInvoked`APIs to automatically intercept the system back button when the drawer is open. This requires that your app[opts into the predictive back gesture](https://developer.android.com/guide/navigation/predictive-back-gesture#opt-predictive).
- Calling`open`and`close`now consistently work even if the drawer is locked. Locking the drawer still prevents users from interacting with the drawer via gestures.

### Version 1.2.0-rc01

March 8, 2023

`androidx.drawerlayout:drawerlayout:1.2.0-rc01`is released with no changes.[Version 1.2.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7d3ac1ab1206c01fae3ebb500b5b942636070155..fbc749d6e72aa21157e8005fb3517a6d4853fe47/drawerlayout/drawerlayout)

### Version 1.2.0-beta01

February 8, 2023

`androidx.drawerlayout:drawerlayout:1.2.0-beta01`is released with no changes.[Version 1.2.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bdce26bd7556b92d2d4d2af3de881dd8e2c51459..7d3ac1ab1206c01fae3ebb500b5b942636070155/drawerlayout/drawerlayout)

### Version 1.2.0-alpha01

September 21, 2022

`androidx.drawerlayout:drawerlayout:1.2.0-alpha01`is released.[Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/37cbd85ea1cbab57834490e88e4f31208d20bfaf..bdce26bd7556b92d2d4d2af3de881dd8e2c51459/drawerlayout/drawerlayout)

**New Features**

- Integrate new`OnBackPressedInvoked`APIs for Android 13 ([0c84661](https://android.googlesource.com/platform/frameworks/support/+/0c84661be14b979f3588811f4a4374719f1a5bbe))

**Bug Fixes**

- Ensure`open()`and`close()`work programmatically when drawer is locked ([ae09f6e](https://android.googlesource.com/platform/frameworks/support/+/ae09f6e6686b32c5677c086d51d5737553e2aeb9))

## Version 1.1.1

| **Note:** This version is dependent on the Java 8 programming language. Please read[Use Java 8 language features](https://developer.android.com/studio/write/java8-support)to learn how to use it in your project.

### Version 1.1.1

September 2, 2020

`androidx.drawerlayout:drawerlayout:1.1.1`is released.[Version 1.1.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c8d28fbc5476c828cb1cf34b6e7f5ec6f7920c24..37cbd85ea1cbab57834490e88e4f31208d20bfaf/drawerlayout/drawerlayout)

**Bug Fixes**

- Fixed an issue where`open()`and`close()`would not work when using`LOCK_MODE_LOCKED_CLOSED`or`LOCK_MODE_LOCKED_OPEN`. ([b/162253907](https://issuetracker.google.com/162253907))

## Version 1.1.0

| **Note:** This version is dependent on the Java 8 programming language. Please read[Use Java 8 language features](https://developer.android.com/studio/write/java8-support)to learn how to use it in your project.

### Version 1.1.0

June 24, 2020

`androidx.drawerlayout:drawerlayout:1.1.0`is released.[Version 1.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/75f3faf4ff897611ef2e732ed0be0187917d797e..c8d28fbc5476c828cb1cf34b6e7f5ec6f7920c24/drawerlayout/drawerlayout)

**Major changes since 1.0.0**

- `DrawerLayout`now takes into account the size of any gesture navigation insets, expanding the area available to users to long press and swipe to open the drawer when gesture navigation is enabled.
- `DrawerLayout`now supports setting a default style using the`drawerLayoutStyle`theme attribute.
- `DrawerLayout`now implements the[`Openable`](https://developer.android.com/reference/androidx/customview/widget/Openable)interface added in[CustomView`1.1.0`](https://developer.android.com/jetpack/androidx/releases/customview#1.1.0).

### Version 1.1.0-rc01

May 20, 2020

`androidx.drawerlayout:drawerlayout:1.1.0-rc01`is released with no changes since`1.1.0-beta01`.[Version 1.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6c98d66b901be2eecdf89477ccd70d2490ca6fc2..75f3faf4ff897611ef2e732ed0be0187917d797e/drawerlayout/drawerlayout)

### Version 1.1.0-beta01

April 1, 2020

`androidx.drawerlayout:drawerlayout:1.1.0-beta01`is released with no changes since`1.1.0-alpha04`.[Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/666ae665acfcfa2a20eccc18e4494808169742f4..6c98d66b901be2eecdf89477ccd70d2490ca6fc2/drawerlayout/drawerlayout)

### Version 1.1.0-alpha04

March 4, 2020

`androidx.drawerlayout:drawerlayout:1.1.0-alpha04`is released.[Version 1.1.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d38639de31ef1465359504032e1dbf994d2b58b5..666ae665acfcfa2a20eccc18e4494808169742f4/drawerlayout/drawerlayout)

**API Changes**

- `DrawerLayout`now implements the`Openable`interface added in[CustomView`1.1.0-alpha02`](https://developer.android.com/jetpack/androidx/releases/customview#1.1.0-alpha02). ([b/129979320](https://issuetracker.google.com/issues/129979320))

### Version 1.1.0-alpha03

August 15, 2019

`androidx.drawerlayout:drawerlayout:1.1.0-alpha03`is released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/4b4213f254744094416b5c3e0a6779783ddae7f7..d38639de31ef1465359504032e1dbf994d2b58b5/drawerlayout).
| **Note:** This version is dependent on the Java 8 programming language. Please read[Use Java 8 language features](https://developer.android.com/studio/write/java8-support)to learn how to use it in your project.

**Bug fixes**

- Fixed binary incompatibility with`androidx.core:core:1.2.0-alpha03`([b/139103874](https://issuetracker.google.com/issues/139103874))

### Version 1.1.0-alpha02

June 13, 2019

`androidx.drawerlayout:drawerlayout:1.1.0-alpha02`is released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/36911a611ba90ce46111bdae943108297ee998a1..4b4213f254744094416b5c3e0a6779783ddae7f7/drawerlayout).
| **Note:** This version is dependent on the Java 8 programming language. Please read[Use Java 8 language features](https://developer.android.com/studio/write/java8-support)to learn how to use it in your project.

**New features**

- Can now set default style using new`drawerLayoutStyle`theme attribute.
- Removed deprecated behavior when used with gesture navigation on Android 10. Drawers are now swiped open using a long press and swipe

### Version 1.1.0-alpha01

May 7, 2019

`androidx.drawerlayout:drawerlayout:1.1.0-alpha01`is released.
| **Note:** This version will only compile against the Q Beta 3 SDK.

**New features**

- Update for Gesture Nav Support:`DrawerLayout`now sets system gesture exclusion`rects`to permit swiping drawers open.

## Version 1.0.0

### Version 1.0.0

September 21, 2018

`androidx.drawerlayout:drawerlayout:1.0.0`is released.