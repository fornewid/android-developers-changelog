---
title: https://developer.android.com/jetpack/androidx/releases/archive/androidx
url: https://developer.android.com/jetpack/androidx/releases/archive/androidx
source: md.txt
---

# AndroidX Release Note Archive

| **Note:** These are the original release notes for AndroidX components that shipped before the AndroidX 1.0.0 release. For the current release notes see the[AndroidX release notes](https://developer.android.com/jetpack/androidx/releases).

## 1.0.0

September 21, 2018

This is the stable release of AndroidX 1.0.0 and is suitable for use in production.

**New features**

- [`AnimatedStateListDrawableCompat`](https://developer.android.com/reference/androidx/appcompat/graphics/drawable/AnimatedStateListDrawableCompat)provides animated transitions between drawable states.
- [`VectorDrawableCompat`](https://developer.android.com/reference/androidx/vectordrawable/graphics/drawable/VectorDrawableCompat)gains support for gradient and[`ColorStateList`](https://developer.android.com/reference/android/content/res/ColorStateList)fills and strokes.

## 1.0.0-rc02

August 27, 2018

This release candidate of AndroidX is considered feature-complete and its public API surface is stable. This release will be shipped as final stable version barring any critical issues that may arise. This release should be safe to use in production. Please report any issues to the[public issue tracker](https://source.android.com/setup/contribute/report-bugs).

**Fixed issues**

- Proguard removes View Model Application constructor (public issue[112230489](https://issuetracker.google.com/issues/112230489))
- Fixed`AnimatedStateListDrawableCompat`constant state
- Removed media2 dependency from mediarouter 1.0.0
- `Fragment.getViewLifecycleOwner()`does not get stopped when hitting the home button ([public issue 113070421](https://issuetracker.google.com/issues/113070421))

## 1.0.0-rc01

August 6, 2018

This release candidate of AndroidX is considered feature-complete and its public API surface is stable. This release will be shipped as final stable version barring any critical issues that may arise. This release should be safe to use in production. Please report any issues to the[public issue tracker](https://source.android.com/setup/contribute/report-bugs).
| **Note:** Some libraries, such as media2, have remained in alpha stage as their API surfaces are not yet finalized. We do not recommend using alpha libraries in production. Libraries should strictly avoid depending on alpha libraries in production, as their API surfaces may change in source- and binary-incompatible ways.

**Fixed issues**

- BottomNavigationView menu is not initialized correctly in design support library
- PositionalDataSource doesn't correctly handle pre-pended item inserts into the database
- Sliders are janky and not responsive
- `SlicesProviderCompat.getPinnedSpecs()`doesn't add user IDs to URIs
- RoutePlayer2: remote playback does not switch back to local playback
- Cached slice parsing is crashing on actions
- Google Search app crash in rendering static Slice
- ConcurrentModificationException in RecyclerView selection library when data set changed with removing selection
- PreferenceThemeOverlay has been updated to the latest material theme. If no custom theme is provided, PreferenceThemeOverlay is used as the default theme.
- PreferenceThemeOverlay.v14 and PreferenceThemeOverlay.v14.Material themes have been deprecated in favour of PreferenceThemeOverlay.
- PreferenceGroup visibility is now tied to its children - hiding a parent group will also prevent its children from being shown in the hierarchy. Use Preference.isShown() to get whether a Preference is actually displayed to the user in the hierarchy.
- Preference.onSetInitialValue(boolean, Object) has been deprecated and replaced with onSetInitialValue(Object). PreferenceDataStore now also correctly restores default values.

## 1.0.0-beta01

July 2, 2018

This beta release of AndroidX is considered feature-complete and its public API surface is stable, barring any critical issues that may arise. While this release is safe to use in production, it may still contain bugs. Please report any issues to the[public issue tracker](https://source.android.com/setup/contribute/report-bugs).

**Fixed issues**

- GestureSelectionHelper eating events on non-selectable items
- Slider slices can have duplicated thumb icon when slider value is being updated
- IconCompat broke TYPE_URI icons in alpha3
- Crash with Preferences using Seekbar
- Crash in Slice.toString()
- OffsettingListUpdateCallback.onMoved() calls mCallback.onRemoved() instead of mCallback.onMoved() (Issue[110711937](https://issuetracker.google.com/issues/110711937))

**Android Studio fixes affecting AndroidX**

- `gradle.properties`file does not update to use AndroidX while creating project with minimum as P
- External libraries can't compile with AndroidX enabled on Windows (Issue[79642238](https://issuetracker.google.com/issues/79642238))
- Converted androidx app crash when deploying
- Failed to resolve: androidx.databinding:databinding-runtime:3.2.0-alpha16
- Unable to deploy Rendering script app after refactoring to Android X
- Crash when executing "Refactor to AndroidX"
- Error: package android.support.annotation does not exist
- ConstraintLayout classes are given the wrong class name during "Refactor to AndroidX"
- Error: package android.support.design.R does not exist

## 1.0.0 alpha 3

June 6, 2018

Bugfix release.

**Fixed issues**

- RecyclerView does not render if two projects with different AndroidX dependencies are open
- Project fails to create and add androidx flags if gradle.properties is not present
- Missing androidx.core.media.MediaMetadataCompat
- Slices are falling over when larger than 64K
- Crash in slice browser
- Unable to migrate App to AppCompact with having androidX dependencies
- Databinding libraries are not updated to androidx
- Cells with large images block rest of cell content
- Incorrect import when refactoring to Androidx
- Slices crashing with NPE in SliceProviderCompat
- Refactor tool error: Should not use a different version (27) than the compileSdkVersion (28)
- Dex merge issues with trying to build refactored project (Android Sunflower)
- AndroidX refactor tool doesn't convert dependencies containing variables
- Espresso Test Recorder does not support androidx dependencies
- NPE in com.example.androidx.slice.demos
- dejetifier flatfoot problems
- androidx.wear has bad dependency on ConstraintLayout libs
- Full loading slices are broken
- After refactoring to androidx adding a new activity is creating with old support code
- dagger-android does not work with jetifier
- Grid templates: Min width of thumbnails for grid row is 1:1 width/height ratio.
- Enforce requiring a primary action on a slice
- Slices for device volume will require setMin on the slider
- Permission slices broken
- Slices needs a new permission system
- Need to allow auto-granting slice perms based on a perm
- Inconsistent sizes in slice
- NullPointerException in FontsContractCompat

## 1.0.0 alpha 2

May 25, 2018

Bugfix release.

**Fixed issues**

- Fixes an issue with[`BuildCompat.isAtLeastP()`](https://developer.android.com/reference/android/support/v4/os/BuildCompat#isatleastp)

## 1.0.0 alpha 1

May 8, 2018

Initial alpha release. The package names are subject to change during the alpha period.

**Known issues**

- The following libraries are not yet compatible with the AndroidX refactor:
  - `com.google.dagger:dagger-android`
  - `com.google.android.support:wearable`
  - `io.fabric.tools:gradle`: Requires 1.25.4 or later
- Upgrade to version`2.16 or later for`com.google.dagger:dagger-android\` to be compatible with the AndroidX refactor.
- The Android Studio refactor tool incorrectly refactors some classes from the`android.arch.persistence.room.*`and`android.support.v4.media.*`namespaces.  
  **Workaround:**Check and correct your import lines after running the refactor tool.
- After using Android Studio refactor tool, full package name is used for some classes in code even though the package was imported.

**Fixed issues**

- BottomNavigationView menu is not initialized correctly (AOSP issue[63375220](https://issuetracker.google.com/issues/63375220))
- RecyclerView getItemDecorationAt has incorrect documentation (AOSP issue[72727717](https://issuetracker.google.com/issues/72727717))