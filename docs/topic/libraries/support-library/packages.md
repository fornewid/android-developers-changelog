---
title: Support Library Packages  |  Android Developers
url: https://developer.android.com/topic/libraries/support-library/packages
source: html-scrape
---

* [Android Developers](https://developer.android.com/)

# Support Library Packages Stay organized with collections Save and categorize content based on your preferences.



**Note:** With the release of Support Library 28.0.0, the `android.support`-packaged
libraries are deprecated and replaced by individually-versioned [Jetpack](/jetpack)
libraries packaged as [`androidx`](/jetpack/androidx). The initial 1.0.0
release of the Jetpack libraries provides parity with Support Library 28.0.0 and provides a
starting point for [migrating](/jetpack/androidx/migrate) to the new `androidx`
packaging.
  
  
The existing `android.support`-packaged libraries will continue to work; however, they
will not receive any updates beyond 28.0.0 and will not be compatible with new Jetpack libraries.
Historical artifacts (those versioned 27 and earlier, and packaged as `android.support`)
will remain available on Google Maven. All new artifacts will be packaged as `androidx`
and will require [migration](/jetpack/androidx/migrate) from `android.support`
to `androidx`.
  
  
We recommend using the `androidx` libraries in all new projects. You should also
consider [migrating](/jetpack/androidx/migrate) existing projects to ensure they
continue to receive bug fixes and other library improvements.

The Android Support Library contains several library packages that can be included
in your application. Each of these libraries supports a specific range of Android platform
versions and set of features.

In order to use any of the following libraries, you must download the library files to your
Android SDK installation. Follow the directions for downloading the Support Libraries in
[Support Library Setup](/tools/support-library/setup#download) to
complete this step. You must take additional steps to include a specific Support Library in
your application. See the end of each library section below for important information on how to
include the library in your application.

**Note:** The minimum SDK version for all support
library packages is at least API level 14. Some packages require a higher API
level, as noted below.

## v4 Support Libraries

These libraries include the largest set of APIs compared to the other libraries,
including support for application components, user interface features,
accessibility, data handling, network connectivity, and programming
utilities.

For complete, detailed information about the classes and methods provided by
the v4 support libraries, see the `android.support.v4` package in the API reference.

**Note:** Prior to Support Library revision 24.2.0, there was a
single v4 support library. That library was divided into multiple modules to
improve efficiency. For backwards compatibility, if you list
`support-v4` in your Gradle script, your app will include all of
the v4 modules. However, to reduce app size, we recommend that you just list
the specific modules your app needs.

### v4 compat library

Provides compatibility wrappers for a number of framework APIs, such as
`Context.obtainDrawable()` and
`View.performAccessibilityAction()`.

The Gradle build script dependency identifier for this library is as follows:

```
com.android.support:support-compat:28.0.0
```

### v4 core-utils library

Provides a number of utility classes, such as `AsyncTaskLoader` and `PermissionChecker`.

The Gradle build script dependency identifier for this library is as follows:

```
com.android.support:support-core-utils:28.0.0
```

### v4 core-ui library

Implements a variety of UI-related components, such as `ViewPager`, `NestedScrollView`, and `ExploreByTouchHelper`.

The Gradle build script dependency identifier for this library is as follows:

```
com.android.support:support-core-ui:28.0.0
```

### v4 media-compat library

Backports portions of the [media](/reference/android/media/package-summary) framework,
including `MediaBrowser` and `MediaSession`.

The Gradle build script dependency identifier for this library is as follows:

```
com.android.support:support-media-compat:28.0.0
```

### v4 fragment library

Adds support for encapsulation of user interface and functionality with
[fragments](/guide/components/fragments),
enabling applications to provide layouts that adjust between small and
large-screen devices. This module has dependencies on [compat](#v4-compat), [core-utils](#v4-core-utils), [core-ui](#v4-core-ui), and [media-compat](#v4-media-compat).

**Note:** The [v13 support library](#v13)
provides a `FragmentCompat` class. The v4
`Fragment` class is a standalone class that
provides bugfixes which were added in later platform versions, whereas the
v13 `FragmentCompat` class provides
compatibility shims for the framework implementation of the
`Fragment` class.

The Gradle build script dependency identifier for this library is as follows:

```
com.android.support:support-fragment:28.0.0
```

## Multidex Support Library

This library provides support for building apps with multiple Dalvik Executable (DEX) files.
Apps that reference more than 65536 methods are required to use multidex configurations. For
more information about using multidex, see [Building Apps with Over 64K Methods](/tools/building/multidex).

The Gradle build script dependency identifier for this library is as follows:

```
com.android.support:multidex:1.0.0
```

## v7 Support Libraries

These libraries provide specific feature sets and can be included in your application
independently from each other.

### v7 appcompat library   Part of [Android Jetpack](/jetpack).

**Note:**The appcompat library has migrated into the
[AndroidX](/jetpack/androidx) library, which is an [Android
Jetpack](/jetpack) component. See it in use in the
[Sunflower](https://github.com/android/sunflower) demo app.

This library adds support for the
[Action Bar](/guide/topics/ui/actionbar) user
interface [design
pattern](/design/patterns/actionbar). This library includes support for
[material design](/design/material) user interface
implementations.

**Note:**
This library depends on the v4 Support Library.

Here are a few of the key classes included in the v7 appcompat library:

* `ActionBar` - Provides an implementation of the action bar
  [user interface pattern](/design/patterns/actionbar). For more
  information on using the Action Bar, see the
  [Action Bar](/guide/topics/ui/actionbar) developer guide.
* `AppCompatActivity` - Adds an application activity class that can
  be used as a base class for activities that use the Support Library action bar
  implementation.
* `AppCompatDialog` - Adds a dialog class that can be used as a base
  class for AppCompat themed dialogs.
* `ShareActionProvider` - Adds support for a standardized
  sharing action (such as email or posting to social applications) that can be included in an
  action bar.

The Gradle build script dependency identifier for this library is as follows:

```
com.android.support:appcompat-v7:28.0.0
```

### v7 cardview library

This library adds support for the `CardView`
widget, which lets you show information inside cards that have a consistent look
on any app. These cards are useful for material design
implementations, and are used extensively in layouts for TV apps.

The Gradle build script dependency identifier for this library is as follows:

```
com.android.support:cardview-v7:28.0.0
```

### v7 gridlayout library

After you download the Android Support Libraries, this library adds support for the
`GridLayout` class, which
allows you to arrange user interface elements using a grid of rectangular cells.
For detailed information about the v7 gridlayout library APIs, see the
`android.support.v7.widget` package in the API reference.

The Gradle build script dependency identifier for this library is as follows:

```
com.android.support:gridlayout-v7:28.0.0
```

### v7 mediarouter library

This library provides `MediaRouter`, `MediaRouteProvider`, and related media classes that
support [Google Cast](https://developers.google.com/cast/).

In general, the APIs in the v7 mediarouter library provide a means of
controlling the routing of media channels and streams from the current device to
external screens, speakers, and other destination devices. The library includes
APIs for publishing app-specific media route providers, for discovering and
selecting destination devices, for checking media status, and more. For detailed
information about the v7 mediarouter library APIs, see the
`android.support.v7.media` package in the API
reference.

The Gradle build script dependency identifier for this library is as follows:

```
com.android.support:mediarouter-v7:28.0.0
```

The v7 mediarouter library APIs introduced in Support Library
r18 are subject to change in later revisions of the Support Library. At this
time, we recommend using the library only in connection with [Google Cast](https://developers.google.com/cast/).

### v7 palette library

The v7 palette support library includes the
`Palette` class, which lets you extract
prominent colors from an image. For example, a music app could use a
`Palette` object to extract the major colors
from an album cover, and use those colors to build a color-coordinated song
title card.

The Gradle build script dependency identifier for this library is as follows:

```
com.android.support:palette-v7:28.0.0
```

### v7 recyclerview library

The recyclerview library adds the `RecyclerView`
class. This class provides support for the
[RecyclerView](/training/material/lists-cards)
widget, a view for efficiently displaying large data sets by providing a
limited window of data items.

The Gradle build script dependency identifier for this library is as follows:

```
com.android.support:recyclerview-v7:28.0.0
```

### v7 Preference Support Library

The
[preference](/reference/android/support/v7/preference/package-summary)
package provides APIs to support adding preference objects, such as
`CheckBoxPreference` and
`ListPreference`, for
users to modify UI settings.

The v7 Preference library adds support for interfaces, such as
`Preference.OnPreferenceChangeListener` and
`Preference.OnPreferenceClickListener`, and classes,
such as `CheckBoxPreference` and
`ListPreference`.

The Gradle build script dependency identifier for this library is as follows:

```
com.android.support:preference-v7:28.0.0
```

## v8 Support Library

This library provides specific feature sets and can be included in your application
independently from other libraries.

### v8 renderscript library

This library adds support for
the [RenderScript](/guide/topics/renderscript/compute) computation
framework. These APIs are included in the `android.support.v8.renderscript` package. You
should be aware that the steps for including these APIs in your application is *very
different* from other support library APIs. For more information about using these APIs
in your application, see the
[RenderScript](/guide/topics/renderscript/compute#access-rs-apis)
developer guide.

**Note:** Use of RenderScript with the support library is supported with Android
Studio and Gradle-based builds. The
renderscript library is located in the `build-tools/$VERSION/renderscript/` folder.

The following example shows the Gradle build script properties for this library:

```
defaultConfig {
    renderscriptTargetApi 18
    renderscriptSupportModeEnabled true
}
```

## v13 Support Library

This library adds support
for the [Fragment](/guide/components/fragments) user interface pattern
with the (`FragmentCompat`) class and additional fragment support
classes. For more information about fragments, see the
[Fragments](/guide/components/fragments) developer guide. For detailed
information about the v13 Support Library APIs, see the `android.support.v13` package in the API reference.

**Note:** The [v4 fragment library](#v4-fragment)
provides a `Fragment` class. The v4
`Fragment` class is a standalone class that
provides bugfixes which were added in later platform versions, whereas the
v13 `FragmentCompat` class provides
compatibility shims for the framework implementation of the
`Fragment` class.

The Gradle build script dependency identifier for this library is as follows:

```
com.android.support:support-v13:28.0.0
```

## v14 Preference Support Library

The `android.support.v14.preference` package provides APIs to add support
for preference interfaces such as
`PreferenceFragment.OnPreferenceStartFragmentCallback`
and
`PreferenceFragment.OnPreferenceStartScreenCallback`,
along with classes, such as
`MultiSelectListPreference` and
`PreferenceFragment`. For detailed
information about the v14 Preference Support Library APIs, see the
[preference](/reference/android/support/v14/preference/package-summary)
package in the API reference.

The Gradle build script dependency identifier for this library is as follows:

```
com.android.support:preference-v14:28.0.0
```

## v17 Preference Support Library for TV

The `android.support.v17.preference` package provides APIs for providing preference
interfaces on TV devices, including support for the
`LeanbackListPreferenceDialogFragment.ViewHolder.OnItemClickListener`
interface and classes, such as
`BaseLeanbackPreferenceFragment` and
`LeanbackPreferenceFragment`. For detailed
information about the v17 Preference Support Library APIs, see the
[preference](/reference/android/support/v17/preference/package-summary)
package in the API reference.

This package requires API level 17 or higher. The Gradle build script
dependency identifier for this library is as follows:

```
 com.android.support:preference-leanback-v17:28.0.0
```

## v17 Leanback Library

The `android.support.v17.leanback` package provides APIs to support
building user interfaces
on TV devices. It provides a number of important widgets for TV apps. Some of the notable classes include:

* `BrowseFragment` - A fragment for
  creating a primary layout for browsing categories and rows of media
  items.
* `DetailsFragment` - A wrapper
  fragment for Leanback details screens.
* `PlaybackOverlayFragment` - A
  subclass of `DetailsFragment` for
  displaying playback controls and related content.
* `SearchFragment` - A fragment to
  handle searches. The fragment receives the user's search request and passes
  it to the application-provided `SearchResultProvider`. The `SearchResultProvider` returns the search results to the
  `SearchFragment`, which renders them
  into a `RowsFragment`.

This package requires API level 17 or higher. The Gradle build script
dependency identifier for this library is as follows:

```
com.android.support:leanback-v17:28.0.0
```

## Vector Drawable Library

Provides support for static vector graphics.

The Gradle build script dependency identifier for this library is as
follows:

```
com.android.support:support-vector-drawable:28.0.0
```

## Animated Vector Drawable Library

Provides support for animated vector graphics.

The Gradle build script dependency identifier for this library is as
follows:

```
com.android.support:animated-vector-drawable:28.0.0
```

## Annotations Support Library

The [Annotation](/reference/android/support/annotation/package-summary)
package provides APIs to support adding annotation metadata to your apps.

The Gradle build script dependency identifier for this library is as follows:

```
com.android.support:support-annotations:28.0.0
```

## Design Support Library

The
[Design](/reference/android/support/design/package-summary) package
provides APIs to support adding material design components and patterns to your apps.

The Design Support library adds support for various material design components and patterns for
app developers to build upon, such as navigation drawers, floating action buttons (*FAB*),
snackbars, and [tabs](/design/building-blocks/tabs).

The Gradle build script dependency identifier for this library is as follows:

```
com.android.support:design:28.0.0
```

## Custom Tabs Support Library

The
[Custom Tabs](/reference/android/support/customtabs/package-summary)
package provides APIs to support adding and managing custom tabs in your apps.

The Custom Tabs Support library adds support for various classes, such as
[Custom Tabs
Service](/reference/androidx/browser/customtabs/CustomTabsService)
and
[Custom Tabs
Callback](/reference/androidx/browser/customtabs/CustomTabsCallback).

This package requires API level 15 or higher.
The Gradle build script dependency identifier for this library is as follows:

```
com.android.support:customtabs:28.0.0
```

## Percent Support Library

The
[Percent](/reference/android/support/percent/package-summary)
package provides APIs to support adding and managing percentage based
dimensions in your app.

**Note:** As of release 26.0.0, the Percent Support library is deprecated.
Clients of this module should migrate to the new [`ConstraintLayout`](/reference/androidx/constraintlayout/widget/ConstraintLayout)
widget, which is provided as a separate artifact in SDK Manager.

The Percent Support library adds support for the
[PercentLayoutHelper.PercentLayoutParams](/reference/androidx/percentlayout/widget/PercentLayoutHelper.PercentLayoutParams) interface
and various classes, such as
[PercentFrameLayout](/reference/androidx/percentlayout/widget/PercentFrameLayout)
and
[PercentRelativeLayout](/reference/androidx/percentlayout/widget/PercentRelativeLayout).

The Gradle build script dependency identifier for this library is as follows:

```
com.android.support:percent:28.0.0
```

## ExifInterface Support Library

Exif tags store information such as the orientation, date and time, camera
information, and the location directly in a JPEG or RAW file. The [`ExifInterface`](/reference/androidx/exifinterface/media/ExifInterface)
class unbundles support for reading Exif information from JPEG
and raw (DNG, CR2, NEF, NRW, ARW, RW2, ORF, PEF, SRW and RAF) formatted
files, and setting the Exif information on JPEG image files.

The Gradle build script dependency identifier for this library is as follows:

```
com.android.support:exifinterface:28.0.0
```

## App Recommendation Support Library for TV

The
[App
Recommendation](/reference/android/support/app/recommendation/package-summary)
package provides APIs to support adding content recommendations in your app running on TV devices.

The App library adds support for annotations, such as
[ContentRecommendation.ContentMaturity](/reference/androidx/recommendation/app/ContentRecommendation.ContentMaturity) and various classes, such as
[ContentRecommendation](/reference/androidx/recommendation/app/ContentRecommendation)
and
[RecommendationExtender](/reference/androidx/recommendation/app/RecommendationExtender).

This package requires API level 21 or higher.
The Gradle build script dependency identifier for this library is as follows:

```
com.android.support:recommendation:28.0.0
```

## Wear UI Library

This library has APIs for building user interfaces for Wear apps.
The APIs, available in the
[android.support.wear.widget](/reference/android/support/wear/widget/package-summary) package,
replace the corresponding APIs in the Wearable Support Library.

For more information, see
[Using the Wear UI Library](/training/wearables/ui/wear-ui-library).

The Gradle build script dependency identifier for this library is as follows:

```
com.android.support:wear:28.0.0
```