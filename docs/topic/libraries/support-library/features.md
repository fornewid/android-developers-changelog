---
title: Support Library Features Guide  |  Android Developers
url: https://developer.android.com/topic/libraries/support-library/features
source: html-scrape
---

* [Android Developers](https://developer.android.com/)

# Support Library Features Guide Stay organized with collections Save and categorize content based on your preferences.



**Note:** With the release of Android 9.0 (API level 28) there is
a new version of the support library called
[AndroidX](/jetpack/androidx) which is part of [Jetpack](/jetpack).
The AndroidX library
contains the existing support library and also includes the latest Jetpack components.
  
  
You can continue to use the support library.
Historical artifacts (those versioned 27 and earlier, and packaged as `android.support.*`) will
remain available on Google Maven. However, all new library development
will occur in the [AndroidX](/jetpack/androidx) library.
  
  
We recommend using the AndroidX libraries in all new projects. You should also consider
[migrating](/jetpack/androidx/migrate) existing projects to AndroidX as well.

The Support Libraries provide a wide range of classes for building apps, from
fundamental app components, to user interface widgets, to media handling, to
TV app components. Many of the classes are backward compatible
implementations, but some of them are new features in their own right.

This document provides an overview of the important categories of features
available in the support library, and specific classes you should know about
when building your app.

For information about how to add support library code to your app development
project, see [Support
Library Setup](https://developer.android.com/topic/libraries/support-library/setup.html). For information on how to include specific support library
packages in your project, see [Support Library Packages](https://developer.android.com/topic/libraries/support-library/packages.html).

## App Components

These Support Library classes provide backward-compatible implementations of
important, core platform features. These implementation typically extend
earlier versions of the class to handle new methods and features added in
more recent releases of the platform. Some of these classes are complete,
static implementations of the framework APIs.

* Activities
  + `ActivityCompat` - Includes
    backward-compatible implementation for recent, key features of
    activities, such as a [Runtime Permissions](/about/versions/marshmallow/android-6.0-changes#behavior-runtime-permissions) and animation transitions.
  + `FragmentActivity` - Provides
    backward-compatible implementation for activities to use the support
    library versions of `Fragment` and `Loader` APIs.
  + `AppCompatActivity` - Provides Material
    color themes, widget tinting, and [app bar](https://developer.android.com/training/appbar/index.html)
    support to earlier devices. Use of this class requires that you use
    `Theme.AppCompat` themes for consistent visual presentation.
* `Fragment` - Provides a stand-alone
  implementation of the framework `Fragment` class. This
  class must be used with `FragmentActivity`.
* `ContextCompat` - Provides support
  for features introduced in more recent releases of the `Context` class, including permissions support, file
  access, and color information.
* `IntentCompat` - Provides support
  for features introduced in more recent releases of the `Intent` class, including methods for selecting and
  starting specific activities.
* `Loader` - Provides a static
  implementation of the framework `Loader` class, and
  is the base class for the `AsyncTaskLoader` and `CursorLoader` support classes.
* `Preference` - This class and its
  sub-classes provide implementations of app settings user interface in a
  backward-compatible way.
* `ContentResolverCompat` - Provides
  support for features introduced in more recent releases of the `ContentResolver` class, specifically the `query()` method
  with support for cancelling a query in progress.

## User Interface

These support library classes provide implementations of key user interface
widgets and behaviors, and help you create more modern app interfaces on
earlier devices. A few of these widgets are only available through the
support library.

### General-purpose layout containers

These support classes provide user interface containers that can be adapted
for different design use cases.

* `RecyclerView` - Creates a layout for
  displaying long lists, using a strategy to avoid high memory consumption.
  This class allows you to create a limited window view into a larger data set,
  thus avoiding consuming large amounts of memory when displaying the list.
  For more information about using `RecyclerView`,
  see the [Recycler View](/guide/topics/ui/layout/recyclerview)
  guide.
* `ViewPager` - Provides a layout that allows
  the user to flip left and right through pages of data.
* `GridLayout` - Provides a layout with its
  children in a rectangular grid, supporting arbitrary spans of contiguous
  cells and flexible space distribution. This class provides a backward
  compatible version of the `GridLayout` class, introduced
  in Android 4.0 (API level 14).
* `PercentFrameLayout` and `PercentRelativeLayout` - Provide layouts that support
  percentage based dimensions and margins for its child views and content.

**Note:** The `ViewPager`, `RecyclerView`, `PercentFrameLayout` and `PercentRelativeLayout` classes are only available
from the Support Libraries.

### Special-purpose layout containers

These support classes provide compatible implementations of specific layout
patterns, such as drawer views that can be pulled from the edge of the
screen, sliding panels, and nesting lists within lists.

* `DrawerLayout` - Creates a layout that
  allows for interactive [drawer views](/training/implementing-navigation/nav-drawer) to be pulled out from the edge of the view window.
* `SlidingPaneLayout` - Provides a
  horizontal, multi-pane layout for use at the top level of an app user
  interface for creating layouts that can smoothly adapt across many different
  screen sizes, expanding on larger screens and collapsing to fit on smaller
  screens.
* `NestedScrollView` - A scrolling layout
  that supports nesting of other scrolling views, allowing you to create lists,
  with items containing an additional, child lists. These nested lists can
  contain items that scroll horizontally or vertically, separately from the
  parent list.
* `SwipeRefreshLayout` - Provides a layout
  to support refreshing data for lists or other layout with a finger swipe
  gesture.

### Views, dialogs, and widgets

The support libraries provide a number of classes for displaying content and
providing user interaction elements in a layout.

* `CardView` - A support library custom
  class for creating Material Design style display cards. This class is based
  on FrameLayout with rounded corners and a drop shadow.
* `AppCompatDialogFragment` - Provides a
  consistently styled dialogs by extending `DialogFragment` and using `AppCompatDialog`.
* `NotificationCompat` - Provides support for
  newer notification styles in a backward compatible way.
* `SearchView` - Provides a class for the
  user to enter a search query and submit a request to a search provider, which
  is primarily intended for use in an app bar.

## Material Design

The support libraries provide a number of classes for implementing Material
Design user interface recommendations.

* `CoordinatorLayout` - Provides a
  top-level container for layouts incorporating Material Design components and
  behavior. This class can also be used as a container for specific interaction
  with one or more child views.
* `AppBarLayout` - Provides an
  implementation of many of the scrolling features of Material Design's
  [app bar concept](http://www.google.com/design/spec/layout/structure.html#structure-app-bar).
* `FloatingActionButton` - Creates
  floating button for displaying a special type of promoted action. This
  Material Design user interface element is shown as a circled icon floating
  above the app user interface. For more information, see [Add a Floating Action Button](/guide/topics/ui/floating-action-button).
* `DrawerLayout` - Creates a navigation drawer—a
  UI panel that shows your app's main navigation menu. It appears when the user
  swipes a finger from the left edge of the screen or taps the drawer icon in the app bar.
  For more information, see [Create a Navigation Drawer](/training/implementing-navigation/nav-drawer).* `TabLayout` - Provides a layout for
    displaying tabbed pages. This widget is designed for use with the `ViewPager` class.
  * `Snackbar` - Provides a widget for
    displaying lightweight feedback about an operation using the [snackbar pop-up](/training/snackbar).

## Graphics

The `android.support.graphics.drawable` package provides support for
[vector drawables](https://www.youtube.com/watch?v=wlFVIIstKmA).
By using vector drawables, you can replace multiple PNG assets with a single
vector graphic, defined in XML.

`VectorDrawableCompat` provides
support for vector drawables on API level 9 and above. `AnimatedVectorDrawableCompat` provides
support for animated vector drawables on API level 11 and above.

## Accessibility

The `android.support.v4.view.accessibility` package provides
compatibility classes for implementing accessibility features introduced in
API level 14 and later, which allow accessibility services to observe and
identify user interaction with items displayed on screen.

* `ExploreByTouchHelper` - Provides
  accessibility support in a custom [View](https://developer.android.com/reference/android/view/View.html)
  that represent a collection of view-like logical items.

## Media Playback

The Android Support Library provides a backport of the [media
router](https://developer.android.com/guide/topics/media/mediarouter.html) functionality to devices running versions of the platform earlier
than Android 4.1 (API level 16). These classes allow control of media
playback across connected Android devices:

* `MediaRouter` - Enables applications to
  control the routing of media channels and streams from the current device to
  external speakers and destination devices.
* `MediaControllerCompat` - Allows
  an app to interact with an ongoing media session. Apps can provide media
  control buttons through this mechanism and send other playback commands to
  the session.
* `MediaSessionCompat` - Provides a
  remote control interface for media playback, enabling interaction with media
  controllers, volume keys, media buttons, and transport controls in other apps
  or on separate devices.

## TV Apps

The Android SDK provides libraries to support form factors such as large screens
and their associated controllers. An app can depend on the appropriate support
library to provide functionality across a wide range of platform versions,
and can provide content on external screens, speakers, and other destination
devices.

* [android.support.v17.leanback](https://developer.android.com/reference/android/support/v17/leanback/package-summary.html).\* packages

## Wear Apps

The Android SDK provides libraries to support watches. These libraries provide functionality
to apps that is available to users whenever they are wearing a watch.

* [android.support.wear](https://developer.android.com/reference/android/support/wear/package-summary.html).\* packages

## Utilities

The Android Support Library offers a number of features that are not built
into the framework. These libraries offer a range of utilities that apps can
use.

* [android.support.v4.util](/reference/android/support/v4/util/package-summary) package