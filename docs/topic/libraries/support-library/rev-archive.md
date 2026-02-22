---
title: https://developer.android.com/topic/libraries/support-library/rev-archive
url: https://developer.android.com/topic/libraries/support-library/rev-archive
source: md.txt
---

# Support Library Revision Archive

This page provides details about older Support Library package releases. For the most recent Support Library releases, see[Recent Support Library Revisions](https://developer.android.com/topic/libraries/support-library/revisions).

## Revision 26.0.0 Beta 2

#### (June 2017)

Please note that 26.0.0-beta2 is a pre-release version. Its API surface is subject to change, and it does not necessarily include features or bug fixes from the latest stable versions of Support Library.

**Important:** The support libraries are now available through Google's Maven repository. You do not need to download the support repository from the SDK Manager. For more information, see[Support Library Setup](https://developer.android.com/topic/libraries/support-library/setup).

### New APIs

- New[JobIntentService](https://developer.android.com/reference/androidx/core/app/JobIntentService)class, to help developers schedule tasks in a way that complies with the new Android O[background execution limits](https://developer.android.com/about/versions/oreo/background).

### API Diffs

- [26.0.0-beta1 -\> 26.0.0-beta2](https://developer.android.com/sdk/support_api_diff/26.0.0-beta2-incr/changes)
- [25.4.0 -\> 26.0.0-beta2](https://developer.android.com/sdk/support_api_diff/26.0.0-beta2/changes)

### Bug fixes

- Android O SDK drop causes loss of italics in TextViews
- Null pointer exception when connecting to MediaBrowserServiceCompat
- TextInputLayout must set hints on onProvideAutofillStructure()
- Stack overflow when using TextView autosize on O

## Revision 26.0.0 Beta 1

#### (May 2017)

Please note that 26.0.0-beta1 is a pre-release version. Its API surface is subject to change, and it does not necessarily include features or bug fixes from the latest stable versions of Support Library.

**Important:** The support libraries are now available through Google's Maven repository. You do not need to download the support repository from the SDK Manager. For more information, see[Support Library Setup](https://developer.android.com/topic/libraries/support-library/setup).

### Important changes

- `FragmentActivity.setSupportMediaController()`and`FragmentActivity.getSupportMediaController()`have been removed. Please use the new static[MediaControllerCompat.setMediaController()](https://developer.android.com/reference/android/support/v4/media/session/MediaControllerCompat#setMediaController(android.app.Activity, android.support.v4.media.session.MediaControllerCompat))and[MediaControllerCompat.getMediaController()](https://developer.android.com/reference/android/support/v4/media/session/MediaControllerCompat#getMediaController())methods.
- [BottomNavigationView](https://developer.android.com/reference/com/google/android/material/bottomnavigation/BottomNavigationView)now calls[onNavigationItemReselected()](https://developer.android.com/reference/com/google/android/material/bottomnavigation/BottomNavigationView.OnNavigationItemReselectedListener#onNavigationItemReselected(android.view.MenuItem))when an already-selected item is selected, rather than calling[onNavigationItemSelected()](https://developer.android.com/reference/com/google/android/material/bottomnavigation/BottomNavigationView.OnNavigationItemSelectedListener#onNavigationItemSelected(android.view.MenuItem)).
- All instances of the`findViewById()`method now return`
  <T extends View> T`instead of`View`. This change has the following implications:
  - This may result in existing code now having ambiguous return type, for example if there is both`someMethod(View)`and`someMethod(TextView)`that takes the result of a call to`findViewById()`.
  - When using Java 8 source language, this requires an explicit cast to`View`when the return type is unconstrained (for example,`assertNotNull(findViewById(...)).someViewMethod())`.
  - Overrides of non-final`findViewById()`methods (for example,`Activity.findViewById()`) will need their return type updated.

### New APIs

- `FragmentManager`and`Fragment`have an`isStateSaved()`method to allow querying whether or not a transaction will be allowed without state loss. This is especially useful to check when handling an`onClick()`event before executing any transaction.
- Path motion is supported in`AnimatedVectorDrawableCompat`. Path motion allows one object animator to change two properties at the same time based on one path; the path is specified as`android:pathData`in the animator's XML).
- [Physics-based animation](https://developer.android.com/topic/libraries/support-library/preview/physics-based-animation):
  - New`FlingAnimation`that supports animating with an initial velocity and smoothly slows down.
  - Subclasses of`DynamicAnimation`support animating custom property for any object.
  - Both`SpringAnimation`and`FlingAnimation`can now animate a float value without requiring a`View`or an`Object`to be associated with it.

  For more information, see the[Spring animation](https://developer.android.com/topic/libraries/support-library/preview/spring-animation)and[Fling animation](https://developer.android.com/topic/libraries/support-library/preview/fling-animation)preview pages.
- [Font support in XML](https://developer.android.com/guide/topics/ui/look-and-feel/downloadable-fonts#using-downloadable-fonts-as-resources):
  - `ResourcesCompat.getFont`allows loading font resources---including font-family XML---that may be used with`TextView.setTypeface()`.
  - When using AppCompat, TextView supports specifying a font resource or font-family XML via the`android:fontFamily`XML attribute.
  - Use XML font-family to create families of fonts with style and weight variations. (If you use the support library classes to do this, use the`app:`attributes as well as the`android:`attributes.)
- [Downloadable fonts:](https://developer.android.com/guide/topics/ui/look-and-feel/downloadable-fonts)
  - New`FontsContractCompat`that allows you to request fonts from a font provider instead of bundling them in your app.
  - Fonts can also be requested in XML and used in layouts.
- [Emoji compatibility library](https://developer.android.com/topic/libraries/support-library/preview/emoji-compat):
  - `EmojiCompat`can process a given`CharSequence`and add`EmojiSpans`.
  - `EmojiTextView`and other widgets to display emoji.
  - `FontRequestEmojiCompatConfig`to request emoji font from a font provider.
- [Autosizing TextView](https://developer.android.com/guide/topics/ui/look-and-feel/autosizing-textview):
  - New methods in`TextViewCompat`as well as XML attributes to control autosizing in`TextView`.
- Leanback playback controls with seek support:
-
  - New`PlaybackTransportRowPresenter`that renders playback controls with a SeekBar.
  - New`PlaybackTransportControlGlue`that works with`
    PlaybackTransportRowPresenter`and supports seek.
  - New base class`PlaybackSeekDataProvider`for app to provide seek thumbnails to`PlaybackTransportControlGlue`.
- Preferences Data Store:
  - `PreferenceDataStore`now allows you to implement your own preferences storage, set with new methods in`Preference`and`PreferenceManager`.

### Known Issues

- Downloadable Fonts and Emoji compatibility integration with Google Play Services only works on Google Play Services v11+, which is currently available through the[Google Play Services beta program](https://developers.google.com/android/guides/beta-program).

### Bug fixes

- `MediaBrowserCompat.search()`API does not work (AOSP issue[262170](https://code.google.com/p/android/issues/detail?id=262170))
- `ViewCompat.postInvalidateOnAnimation()`throws exception (AOSP issue[80146](https://code.google.com/p/android/issues/detail?id=80146))
- `onActivityCreated()`called for fragments in destroyed Activity
- `RecyclerView.isComputingLayout()`should return true during prefetch
- When a`Fade`transition is interrupted and reversed, the`View`starts the animation from the beginning. (Fix ported from Android Framework.)
- `Transition.Fade`ignores initial alpha of`View`(AOSP issue[221820](https://code.google.com/p/android/issues/detail?id=221820))

## Revision 26.0.0 Alpha 1

#### (March 2017)

Please note that 26.0.0-alpha1 is a pre-release version. Its API surface is subject to change, and it does not necessarily include features or bug fixes from the latest stable versions of Support Library.

### Important changes

**Note:**The minimum SDK version has been increased to 14. As a result, many APIs that existed only for API \< 14 compatibility have been deprecated. Clients of these APIs should migrate to their framework equivalents as noted in the reference page for each deprecated API.

- The support-percent module has been deprecated. Clients of this module should migrate to the new ConstraintLayout widget, which is provided as a separate artifact in SDK Manager.
- The support-fragment module no longer has a dependency on the support-media-compat module.

### New APIs

Many new classes, methods, and constants added to provide backwards-compatible support for platform APIs added in O Preview.

- `IME_FLAG_NO_PERSONALIZED_LEARNING`: IMEs can listen for "no learning" flags for apps that have a private mode, such as browsers. This feature helps IMEs understand if an app is in a private mode, so they can disable their learning or adaptive functionality while the app is in that mode.

For a complete list of API changes between 25.2.0 and 26.0.0-alpha1, see the[support library API differences report](https://developer.android.com/sdk/support_api_diff/26.0.0-alpha1/changes).

### Bug fixes

- In some cases simple[AutoTransition](https://developer.android.com/reference/androidx/transition/AutoTransition)animation can be interrupted by view "jumps". (AOSP issue[221816](https://code.google.com/p/android/issues/detail?id=221816))

## Revision 25.4.0

#### (June 2017)

**Important:** The support libraries are now available through Google's Maven repository. You do not need to download the support repository from the SDK Manager. For more information, see[Support Library Setup](https://developer.android.com/topic/libraries/support-library/setup).

### Important changes

- [executePendingTransactions()](https://developer.android.com/reference/androidx/fragment/app/FragmentManager#executePendingTransactions()),[commitNow()](https://developer.android.com/reference/androidx/fragment/app/FragmentTransaction),[popBackStackImmediate()](https://developer.android.com/reference/androidx/fragment/app/FragmentManager#popBackStackImmediate()), and similar transaction calls are not allowed during[FragmentManager](https://developer.android.com/reference/androidx/fragment/app/FragmentManager)state changes. Reentrant execution of transactions are unsafe and[FragmentManager](https://developer.android.com/reference/androidx/fragment/app/FragmentManager)now enforces this during its state changes.
- Concurrent with this support library release, we are also releasing[multidex](https://developer.android.com/studio/build/multidex)version 1.0.2. This version includes the following important changes:
  - Allows multidexing of instrumentation APK.
  - Deprecates MultiDexTestRunner (AndroidJUnitRunner should be used instead).
  - Provides better protection against some bad archive extraction management of the app.
  - Fixes a bug that could lead to abandoned temporary files.
  - Provides faster installation when done in concurrent process.
  - Fixes an installation bug on API 19 and 20.

### New and Modified APIs

Path morphing and path interpolation are supported in[AnimatedVectorDrawableCompat](https://developer.android.com/reference/androidx/vectordrawable/graphics/drawable/AnimatedVectorDrawableCompat). Path morphing allow the shapes changing from one path (specified as`android:valueFrom`) to another path (specified as`android:valueTo`), in order to provide complex and attractive visual effects. Path interpolation allows the interpolators for[AnimatedVectorDrawableCompat](https://developer.android.com/reference/androidx/vectordrawable/graphics/drawable/AnimatedVectorDrawableCompat)to be specified as paths (specified as`android:pathData`in the interpolator's XML).

### API Diffs

- [25.3.0 -\> 25.4.0](https://developer.android.com/sdk/support_api_diff/25.4.0/changes)

### Fixed issues

- Null pointer exception when connecting to MediaBrowserServiceCompat
- MediaBrowserCompat.search() API does not work (AOSP issue[262170](https://code.google.com/p/android/issues/detail?id=262170))
- BrowseFragment onItemClicked callbacks broken in 25.3.0
- NullPointerException while scrolling up and down in VerticalGridView in 25.3.1
- ClassCastException in SimpleArrayMap.allocArrays()

## Revision 25.3.1

#### (March 2017)

### Fixed issues

- [SwitchCompat](https://developer.android.com/reference/androidx/appcompat/widget/SwitchCompat)requires minimum SDK version of 14 or higher. (AOSP issue[251302](https://code.google.com/p/android/issues/detail?id=251302))
- Physics-based animation`updateListener`skips the first frame.
- [BottomNavigationView](https://developer.android.com/reference/com/google/android/material/bottomnavigation/BottomNavigationView)label animation is broken.

## Revision 25.3.0

#### (March 2017)

### Important changes

Support Library version metadata will automatically be added to`AndroidManifest.xml`when building from Gradle, which simplifies tracking versions in public builds. For example:  

```xml
<meta-data android:name="android.support.VERSION" android:value="25.3.0" />
```

### Deprecations

A number of methods and classes have been deprecated in this release. These deprecated APIs will be removed in a future version and developers should migrate away from them. For more information on how to migrate away from a specific API, refer to its documentation.

[ExifInterface](https://developer.android.com/reference/androidx/exifinterface/media/ExifInterface)
:   The boolean method[getLatLong(float[])](https://developer.android.com/reference/androidx/exifinterface/media/ExifInterface#getLatLong(float[]))is deprecated. Instead, use the new method[getLatLong()](https://developer.android.com/reference/androidx/exifinterface/media/ExifInterface#getLatLong()), which takes no arguments and returns`double[]`.

[mediacompat](https://developer.android.com/reference/android/support/mediacompat/package-summary)
:   [PlaybackStateCompat.Builder.setErrorMessage(CharSequence)](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat.Builder#setErrorMessage(java.lang.CharSequence))is deprecated. Instead, use the new method[setErrorMessage(int, CharSequence)](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat.Builder#setErrorMessage(int, java.lang.CharSequence)), which is passed an error code and an optional description.
:   [EXTRA_SUGGESTION_KEYWORDS](https://developer.android.com/reference/androidx/media/MediaBrowserServiceCompat.BrowserRoot#EXTRA_SUGGESTION_KEYWORDS)is deprecated. Instead, use the[MediaBrowserCompat](https://developer.android.com/reference/android/support/v4/media/MediaBrowserCompat)search functionality.

[v7.recyclerview](https://developer.android.com/reference/android/support/v7/recyclerview/package-summary)
:   `LinearLayoutManager.getInitialItemPrefetchCount()`has been renamed to[LinearLayoutManager.getInitialPrefetchItemCount()](https://developer.android.com/reference/androidx/recyclerview/widget/LinearLayoutManager#getInitialPrefetchItemCount()). The old name is still supported but will be removed in a future release.

### New and Modified APIs

[appcompat-v7](https://developer.android.com/reference/android/support/v7/appcompat/package-summary)
:   The new method[ActionBarDrawerToggle.setDrawerSlideAnimationEnabled(boolean)](https://developer.android.com/reference/androidx/appcompat/app/ActionBarDrawerToggle#setDrawerSlideAnimationEnabled(boolean))simplifies disabling the navigation drawer toggle icon's animation.

[customtabs](https://developer.android.com/reference/android/support/customtabs/package-summary)
:   Added support for message channels. See the[CustomTabsService.requestPostMessageChannel()](https://developer.android.com/reference/androidx/browser/customtabs/CustomTabsService#requestPostMessageChannel(android.support.customtabs.CustomTabsSessionToken,%20android.net.Uri))and[CustomTabsService.postMessage()](https://developer.android.com/reference/androidx/browser/customtabs/CustomTabsService#postMessage(android.support.customtabs.CustomTabsSessionToken, java.lang.String, android.os.Bundle))reference for details.

[dynamic-animation](https://developer.android.com/reference/android/support/animation/package-summary)
:   New physics-based animation library that provides a set of APIs for building animations that dynamically react to user input.

[leanback-v17](https://developer.android.com/reference/android/support/v17/leanback/package-summary)
:   Added support for parallax backgrounds. See the[Parallax](https://developer.android.com/reference/androidx/leanback/widget/Parallax)reference for details.
:   Added[TimePicker](https://developer.android.com/reference/androidx/leanback/widget/picker/TimePicker)widget for picking times on a TV interface.

[mediacompat](https://developer.android.com/reference/android/support/mediacompat/package-summary)
:   Added search functionality. See the[MediaBrowserCompat.search()](https://developer.android.com/reference/android/support/v4/media/MediaBrowserCompat#search(java.lang.String, android.os.Bundle, android.support.v4.media.MediaBrowserCompat.SearchCallback))and[MediaBrowserServiceCompat.onSearch()](https://developer.android.com/reference/androidx/media/MediaBrowserServiceCompat#onSearch(java.lang.String, android.os.Bundle, android.support.v4.media.MediaBrowserServiceCompat.Result<java.util.List<android.support.v4.media.MediaBrowserCompat.MediaItem>>))reference for details.
:   Added support for shuffle and repeat modes. See the[MediaSessionCompat.setRepeatMode()](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat#setRepeatMode(int))and[setShuffleModeEnabled()](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat#setShuffleModeEnabled(boolean))reference for details.

### Fixed issues

- [StaggeredGridLayoutManager](https://developer.android.com/reference/androidx/recyclerview/widget/StaggeredGridLayoutManager)throws[IllegalArgumentException](https://developer.android.com/reference/java/lang/IllegalArgumentException)(AOSP issue[230295](https://code.google.com/p/android/issues/detail?id=230295))
- [RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView)prefetch does not properly handle a[RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView)that is attached but not onscreen
- [LinearLayout](https://developer.android.com/reference/android/widget/LinearLayout)not recognized by Robolectric
- When[Activity](https://developer.android.com/reference/android/app/Activity)is destroyed,[onActivityCreated()](https://developer.android.com/reference/android/app/Fragment#onActivityCreated(android.os.Bundle))is improperly called for its fragments
- [AppCompatImageView](https://developer.android.com/reference/androidx/appcompat/widget/AppCompatImageView)constructor causes[ArrayIndexOutOfBoundsException](https://developer.android.com/reference/java/lang/ArrayIndexOutOfBoundsException)
- Poor UI performance in[Call.Details](https://developer.android.com/reference/android/telecom/Call.Details)activity transition

## Revision 25.2.0

#### (February 2017)

### Important Changes

### Fixed issues

- This release fixes a severe mediarouter issue in which using an A2DP device and media routing APIs could cause the device to become unresponsive, requiring a reboot.
- The[FragmentManager.FragmentLifecycleCallbacks](https://developer.android.com/reference/androidx/fragment/app/FragmentManager.FragmentLifecycleCallbacks)class is now static.

### Fixed issues

- Showing a slide presentation with screen mirroring causes device to disconnect from Wi-Fi
- Media button did not properly handle media apps that did not register themselves with`setMediaButtonReceiver()`
- `VectorDrawable`error with string resource (AOSP issue[232407](https://code.google.com/p/android/issues/detail?id=232407))
- [TextInputLayout](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout)overlays hint and text if text is set by XML (AOSP issue[230171](https://code.google.com/p/android/issues/detail?id=230171))
- Memory leak in[MediaControllerCompat](https://developer.android.com/reference/android/support/v4/media/session/MediaControllerCompat)(AOSP issue[231441](https://code.google.com/p/android/issues/detail?id=231441))
- `RecyclerViewLayoutTest.triggerFocusSearchInOnRecycledCallback()`crashing
- [RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView)crashes when recycling view holders (AOSP issue[225762](https://code.google.com/p/android/issues/detail?id=225762))
- [getAllowGeneratedReplies()](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Action#getAllowGeneratedReplies())incorrectly returns false for actions inside a`WearableExtender`

## Revision 25.1.1

#### (January 2017)

**Important:** There is a known bug in the[android.support.v7.media.MediaRouter](https://developer.android.com/reference/androidx/mediarouter/media/MediaRouter)class in revision 25.1.1 and 25.1.0 of the Support Library. If your app uses the v7[MediaRouter](https://developer.android.com/reference/androidx/mediarouter/media/MediaRouter), you should update to[Support Library Revision 25.2.0](https://developer.android.com/topic/libraries/support-library/rev-archive#25-2-0), which fixes this bug.

### Important Changes

- Fragment transactions can now be optimized within and across transactions. Optimizing fragment transaction operations can eliminate operations that cancel. For example, suppose two transactions are executed together, one that adds a fragment A and a second one that replaces fragment A with fragment B. In this case, the first operation might be canceled, and only fragment B added. That means that fragment A might not go through the creation/destruction lifecycle.

  A side effect of this optimization is that fragments might have state changes out of the expected order. For example, suppose one transaction adds fragment A, a second adds fragment B, then a third removes fragment A. Without optimization, fragment B could expect that while it is being created, fragment A will also exist because fragment A will be removed after fragment B is added. With optimization, fragment B cannot be sure that fragment A will exist while B is being created, because fragment A's creation and destruction may be removed by the optimization.

  This optimization is disabled by default. To enable the optimization, call[FragmentTransaction.setAllowOptimization(true)](https://developer.android.com/reference/androidx/fragment/app/FragmentTransaction#setAllowOptimization(boolean)).
- Fragments can now postpone their transitions and animations until they are ready using[Fragment.postponeEnterTransition()](https://developer.android.com/reference/androidx/fragment/app/Fragment#postponeEnterTransition())and[Fragment.startPostponedEnterTransition()](https://developer.android.com/reference/androidx/fragment/app/Fragment#startPostponedEnterTransition()). This API is similar to[Activity.postponeEnterTransition()](https://developer.android.com/reference/android/app/Activity#postponeEnterTransition())and[Activity.startPostponedEnterTransition()](https://developer.android.com/reference/android/app/Activity#startPostponedEnterTransition())used with Activity Transitions.

### Fixed issues

- `MediaSessionCompatTest`fails with[IllegalArgumentException](https://developer.android.com/reference/java/lang/IllegalArgumentException)
- [DetailsFragment.installTitleView()](https://developer.android.com/reference/androidx/leanback/app/BrandedFragment#installTitleView(android.view.LayoutInflater, android.view.ViewGroup, android.os.Bundle))is not called in 25.1.0
- Fragment transaction keeps ghost view on exit (AOSP issue[230679](https://code.google.com/p/android/issues/detail?id=230679))
- [BottomNavigationView](https://developer.android.com/reference/com/google/android/material/bottomnavigation/BottomNavigationView)needs spacing between item icon and text (AOSP issue[230653](https://code.google.com/p/android/issues/detail?id=230653))
- Selected listeners are missing from the new[PlaybackFragment](https://developer.android.com/reference/androidx/leanback/app/PlaybackFragment)and[PlaybackSupportFragment](https://developer.android.com/reference/androidx/leanback/app/PlaybackSupportFragment)
- [TextInputLayout](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout)focus does not change properly in emulator from support library version 25.1.0 (AOSP issue[230461](https://code.google.com/p/android/issues/detail?id=230461))
- Cannot replace the menu of a[BottomNavigationView](https://developer.android.com/reference/com/google/android/material/bottomnavigation/BottomNavigationView)(AOSP issue[230343](https://code.google.com/p/android/issues/detail?id=230343))
- [RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView)with[StaggeredGridLayoutManager](https://developer.android.com/reference/androidx/recyclerview/widget/StaggeredGridLayoutManager)crashes with full-span items (AOSP issue[230295](https://code.google.com/p/android/issues/detail?id=230295))
- Crash in[MediaSessionCompat](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat)when using[setCallback(null)](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat#setCallback(android.support.v4.media.session.MediaSessionCompat.Callback))
- `PlaybackGlueHostOld`and`PlaybackSupportGlueHostOld`don't notify callbacks when playback row changes
- [PlaybackOverlayFragment](https://developer.android.com/reference/android/support/v17/leanback/app/PlaybackOverlayFragment)example`/test`can not start playing
- `RecyclerViewFocusRecoveryTest`is failing on API 15
- "Screenshots" row is focused to the top of the screen
- `RecyclerViewLayoutTest.triggerFocusSearchInOnRecycledCallback()`crashes on API 15
- `setActions()`in`onSubactionClicked()`is broken
- [RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView)crashes when recycling some view holders

## Revision 25.1.0

#### (December 2016)

**Important:** There is a known bug in the[android.support.v7.media.MediaRouter](https://developer.android.com/reference/androidx/mediarouter/media/MediaRouter)class in revision 25.1.1 and 25.1.0 of the Support Library. If your app uses the v7[MediaRouter](https://developer.android.com/reference/androidx/mediarouter/media/MediaRouter), you should update to[Support Library Revision 25.2.0](https://developer.android.com/topic/libraries/support-library/rev-archive#25-2-0), which fixes this bug.

### Important Changes

- Clients of nested[RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView)widgets (for example, vertical scrolling list of horizontal scrolling lists) can get significant performance benefits by hinting the inner[RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView)widgets' layout managers how many items to prepare before being scrolled on screen. Call`LinearLayoutManager.setInitialPrefetchItemCount(`<var translate="no">N</var>`)`, where<var translate="no">N</var>is the number of views visible per inner item. For example, if your inner, horizontal lists show a minimum of three and a half item views at a time, you can improve performance by calling`LinearLayoutManager.setInitialPrefetchItemCount(4)`. Doing so allows[RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView)to create all relevant views early, while the outer[RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView)is scrolling, which significantly reduces the amount of stuttering during scrolls.
- `FragmentActivity.setSupportMediaController()`and`FragmentActivity.getSupportMediaController()`have been deprecated. Please use the new static[MediaControllerCompat.setMediaController()](https://developer.android.com/reference/android/support/v4/media/session/MediaControllerCompat#setMediaController(android.app.Activity, android.support.v4.media.session.MediaControllerCompat))and[MediaControllerCompat.getMediaController()](https://developer.android.com/reference/android/support/v4/media/session/MediaControllerCompat#getMediaController())methods.
- When a client specifies a widget tint via appcompat tinting (for example,`appcompat:buttonTint`), the client is responsible for providing all necessary states (such as "disabled", "pressed", etc.). This is consistent with how widget tints are specified when using framework tinting.

### New and Modified APIs

- Added[ExifInterface support library](https://developer.android.com/topic/libraries/support-library/features#exif). This library unbundles support for reading Exif information from JPEG and raw formatted files and setting the Exif information on JPEG image files.
- [Snackbar](https://developer.android.com/reference/com/google/android/material/snackbar/Snackbar)has been refactored to allow apps to display custom content.[`
  BaseTransientBottomBar`](https://developer.android.com/reference/com/google/android/material/snackbar/BaseTransientBottomBar)is the new base class that exposes the general sliding and animations behavior.
- Added a new[leanback.media](https://developer.android.com/reference/android/support/v17/leanback/media/package-summary)package which contains helper classes to integrate media players into Android TV applications.
- Added[`SeekBarPreference`](https://developer.android.com/reference/androidx/preference/SeekBarPreference)with customizable layout and attributes to the[v7 preference support library.](https://developer.android.com/reference/android/support/v7/preference/package-summary)
- Added[`ArraySet`](https://developer.android.com/reference/androidx/collection/ArraySet)class to the v4 support library. This class corresponds to the framework[ArraySet](https://developer.android.com/reference/android/util/ArraySet)class that was introduced with API level 23.
- [RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView)RecyclerView item prefetching improvements:
  - Nested[RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView)prefetch enables prefetching of content from a[RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView)within another scrolling[RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView), with API to control how much prefetching is done:
    - [`LinearLayoutManager.setInitialPrefetchItemCount()`](https://developer.android.com/reference/androidx/recyclerview/widget/LinearLayoutManager#setInitialPrefetchItemCount)
    - [`LinearLayoutManager.getInitialPrefetchItemCount()`](https://developer.android.com/reference/androidx/recyclerview/widget/LinearLayoutManager#getInitialPrefetchItemCount)
  - APIs added for custom[LayoutManager](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView.LayoutManager)objects to implement to enable prefetching during scrolls and flings
    - [`RecyclerView.LayoutManager.LayoutPrefetchRegistry()`](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView.LayoutManager#LayoutPrefetchRegistry)
    - [`RecyclerView.LayoutManager.collectAdjacentPrefetchPositions()`](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView.LayoutManager#collectAdjacentPrefetchPositions)
    - [`RecyclerView.LayoutManager.collectInitialPrefetchPositions()`](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView.LayoutManager#collectInitialPrefetchPositions)
  - Improvements to prefetching to do only as much create/bind work as possible in the time between frames

### Fixed issues

- Password visibility toggle fails accessibility tests.
- Appcompat doesn't respect`state_enabled`on pre-L devices.
- Added focus recovery mechanism to[RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView). This also fixed support pref fragments broken focus when using DPAD navigation such as on Android TV devices.
- Leanback: BrowseFragment crashes with headers disabled and empty adapter.
- Appcompat:[AlertDialog](https://developer.android.com/reference/androidx/appcompat/app/AlertDialog)is too wide.
- [InputContentInfoCompat](https://developer.android.com/reference/androidx/core/view/inputmethod/InputContentInfoCompat)calls[requestPermission()](https://developer.android.com/reference/androidx/core/view/inputmethod/InputContentInfoCompat#requestPermission())when it should call[releasePermission()](https://developer.android.com/reference/androidx/core/view/inputmethod/InputContentInfoCompat#releasePermission()).
- [MediaBrowserCompat](https://developer.android.com/reference/android/support/v4/media/MediaBrowserCompat)crashes.
- CoordinatorLayout measures/lays out views when visibility is set to`GONE`.
- Could not tint[AnimatedVectorDrawableCompat](https://developer.android.com/reference/androidx/vectordrawable/graphics/drawable/AnimatedVectorDrawableCompat)on API level below 24
- Leanback library triggers spurious lint errors
- Palette library caused test failures on every API level
- [RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView)failed tests on Leanback
- [RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView)crashes when recycling view holders (AOSP issue[225762](https://code.google.com/p/android/issues/detail?id=225762))
- [Fragment.onDestroy()](https://developer.android.com/reference/androidx/fragment/app/Fragment#onDestroy())not called for fragment in backstack
- [CollapsingToolbarLayout](https://developer.android.com/reference/com/google/android/material/appbar/CollapsingToolbarLayout)scrim is not drawn when collapsed
- `CoordinatorLayout.offsetChildByInset()`throws`IllegalArgumentException`
- Animating[RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView)items detach inner[RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView)s, prevent future prefetches
- Attached[RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView)items can't be nested-prefetched
- Prefetch data for nested[RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView)items is discarded during first layout
- [RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView)prefetch fails if two drag events arrive at same position
- [RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView)should speculatively layout while RenderThread is rendering
- Night-configured color resources converted to Drawables are not always properly purged from Resources cache
- [FloatingActionButton](https://developer.android.com/reference/com/google/android/material/floatingactionbutton/FloatingActionButton): Programmatically setting BackgroundTintList does not work properly (AOSP issue[227428](https://code.google.com/p/android/issues/detail?id=227428))
- [TextInputLayout](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout): Typeface is not getting set for ErrorView (AOSP issue[227803](https://code.google.com/p/android/issues/detail?id=227803))
- [TextInputLayout](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout)always falls back to light error color below API 23 (AOSP issue[221992](https://code.google.com/p/android/issues/detail?id=221992))
- [FloatingActionButton](https://developer.android.com/reference/com/google/android/material/floatingactionbutton/FloatingActionButton)shows as pressed when pointer leaves

A complete list of public bug fixes is available on the[AOSP Issue Tracker](https://code.google.com/p/android/issues/list?can=1&q=label:Target-Support-25.1.0).

### Deprecations

A number of methods and classes have been deprecated in this release. These deprecated APIs will be removed in a future version and developers should migrate away from them. For more information on how to migrate away from a specific API, refer to its documentation.

- [`android.support.design.widget`](https://developer.android.com/reference/android/support/design/widget/package-summary)
  - [Snackbar.setCallback()](https://developer.android.com/reference/com/google/android/material/snackbar/Snackbar#setCallback(android.support.design.widget.Snackbar.Callback))
- [`android.support.v17.leanback.app`](https://developer.android.com/reference/android/support/v17/leanback/app/package-summary)
  - [BackgroundManager.getDefaultDimLayer()](https://developer.android.com/reference/androidx/leanback/app/BackgroundManager#getDefaultDimLayer())
  - [BackgroundManager.getDimLayer()](https://developer.android.com/reference/androidx/leanback/app/BackgroundManager#getDimLayer())
  - [BackgroundManager.setDimLayer()](https://developer.android.com/reference/androidx/leanback/app/BackgroundManager#setDimLayer(android.graphics.drawable.Drawable))
  - [MediaControllerGlue.MediaControllerGlue(Context,PlaybackOverlayFragment,int[])](https://developer.android.com/reference/android/support/v17/leanback/app/MediaControllerGlue#MediaControllerGlue(android.content.Context, android.support.v17.leanback.app.PlaybackOverlayFragment, int[]))
  - [MediaControllerGlue.MediaControllerGlue(Context,PlaybackOverlayFragment,int[],int[])](https://developer.android.com/reference/android/support/v17/leanback/app/MediaControllerGlue#MediaControllerGlue(android.content.Context, android.support.v17.leanback.app.PlaybackOverlayFragment, int[], int[]))
  - [PlaybackControlGlue.PlaybackControlGlue(Context,PlaybackOverlayFragment,int[])](https://developer.android.com/reference/android/support/v17/leanback/app/PlaybackControlGlue#PlaybackControlGlue(android.content.Context, android.support.v17.leanback.app.PlaybackOverlayFragment, int[]))
  - [PlaybackControlGlue.PlaybackControlGlue(Context,PlaybackOverlayFragment,int[],int[])](https://developer.android.com/reference/android/support/v17/leanback/app/PlaybackControlGlue#PlaybackControlGlue(android.content.Context, android.support.v17.leanback.app.PlaybackOverlayFragment, int[], int[]))
  - [PlaybackControlGlue.getFragment()](https://developer.android.com/reference/android/support/v17/leanback/app/PlaybackControlGlue#getFragment())
  - [PlaybackControlGlue.getOnItemViewClickedListener()](https://developer.android.com/reference/android/support/v17/leanback/app/PlaybackControlGlue#getOnItemViewClickedListener())
  - [PlaybackControlGlue.onRowChanged()](https://developer.android.com/reference/android/support/v17/leanback/app/PlaybackControlGlue#onRowChanged(android.support.v17.leanback.widget.PlaybackControlsRow))
  - [PlaybackControlGlue.pausePlayback()](https://developer.android.com/reference/android/support/v17/leanback/app/PlaybackControlGlue#pausePlayback())
  - [PlaybackControlGlue.skipToNext()](https://developer.android.com/reference/android/support/v17/leanback/app/PlaybackControlGlue#skipToNext())
  - [PlaybackControlGlue.skipToPrevious()](https://developer.android.com/reference/android/support/v17/leanback/app/PlaybackControlGlue#skipToPrevious())
  - [PlaybackControlGlue.startPlayback()](https://developer.android.com/reference/android/support/v17/leanback/app/PlaybackControlGlue#startPlayback(int))
  - [PlaybackControlSupportGlue](https://developer.android.com/reference/android/support/v17/leanback/app/PlaybackControlSupportGlue)
  - [PlaybackOverlayFragment](https://developer.android.com/reference/android/support/v17/leanback/app/PlaybackOverlayFragment)
  - [PlaybackOverlaySupportFragment](https://developer.android.com/reference/android/support/v17/leanback/app/PlaybackOverlaySupportFragment)
- [`
  android.support.v17.leanback.widget`](https://developer.android.com/reference/android/support/v17/leanback/widget/package-summary)
  - [BaseCardView.getExtraVisibility()](https://developer.android.com/reference/androidx/leanback/widget/BaseCardView#getExtraVisibility())
  - [BaseCardView.setExtraVisibility()](https://developer.android.com/reference/androidx/leanback/widget/BaseCardView#setExtraVisibility(int))
  - [GuidedActionsStylist.onEditingModeChange()](https://developer.android.com/reference/androidx/leanback/widget/GuidedActionsStylist#onEditingModeChange(android.support.v17.leanback.widget.GuidedActionsStylist.ViewHolder, android.support.v17.leanback.widget.GuidedAction, boolean))
  - [GuidedActionsStylist.setEditingMode()](https://developer.android.com/reference/androidx/leanback/widget/GuidedActionsStylist#setEditingMode(android.support.v17.leanback.widget.GuidedActionsStylist.ViewHolder, android.support.v17.leanback.widget.GuidedAction, boolean))
  - [GuidedActionsStylist.setExpandedViewHolder()](https://developer.android.com/reference/androidx/leanback/widget/GuidedActionsStylist#setExpandedViewHolder(android.support.v17.leanback.widget.GuidedActionsStylist.ViewHolder))
  - [GuidedActionsStylist.startExpandedTransition()](https://developer.android.com/reference/androidx/leanback/widget/GuidedActionsStylist#startExpandedTransition(android.support.v17.leanback.widget.GuidedActionsStylist.ViewHolder))
- [`android.support.v4.app`](https://developer.android.com/reference/android/support/v4/app/package-summary)
  - `FragmentActivity.getSupportMediaController()`
  - `FragmentActivity.setSupportMediaController()`

## Revision 25.0.1

#### (November 2016)

### Fixed issues

- The[TextInputLayout](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout)password toggle is now disabled by default to avoid unnecessarily overwriting developer-specified end drawables. It may be manually enabled via the[passwordToggleEnabled](https://developer.android.com/reference/com/google/android/material/R.attr#passwordToggleEnabled)XML attribute.
- [BottomNavigationView](https://developer.android.com/reference/com/google/android/material/bottomnavigation/BottomNavigationView)items are now single line to match Material spec.
- [RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView)crashes during prefetch if layout manager is null.
- [BottomNavigationView](https://developer.android.com/reference/com/google/android/material/bottomnavigation/BottomNavigationView)elevation is now set properly. (AOSP issue[226182](https://code.google.com/p/android/issues/detail?id=226182))
- [BottomNavigationView](https://developer.android.com/reference/com/google/android/material/bottomnavigation/BottomNavigationView)crashing when adding menu items programmatically. (AOSP issue[225731](https://code.google.com/p/android/issues/detail?id=225731))
- Fix to[TextInputLayout](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout)left+right compound drawables. (AOSP issue[225836](https://code.google.com/p/android/issues/detail?id=225836))
- [RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView)crashes when recycling view holders. (AOSP issue[225762](https://code.google.com/p/android/issues/detail?id=225762))
- Leanback: TalkBack frequently says the word "null" in split-screen views.
- [RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView): Rendering problems in Android Studio. (AOSP issue[225753](https://code.google.com/p/android/issues/detail?id=225753))
- [BottomNavigationView](https://developer.android.com/reference/com/google/android/material/bottomnavigation/BottomNavigationView)still shows menu item as selected after[onNavigationItemSelected()](https://developer.android.com/reference/com/google/android/material/bottomnavigation/BottomNavigationView.OnNavigationItemSelectedListener#onNavigationItemSelected(android.view.MenuItem))returns false. (AOSP issue[225898](https://code.google.com/p/android/issues/detail?id=225898))
- ForwardingListener throws[NoSuchMethodError](https://developer.android.com/reference/java/lang/NoSuchMethodError). (AOSP issue[225647](https://code.google.com/p/android/issues/detail?id=225647))
- [TextInputEditText](https://developer.android.com/reference/com/google/android/material/textfield/TextInputEditText)does not show hints in IME extract mode. (AOSP issue[221880](https://code.google.com/p/android/issues/detail?id=221880))

A complete list of public bug fixes is available on the[AOSP Issue Tracker](https://code.google.com/p/android/issues/list?can=1&q=label:Target-Support-25.0.1).

## Revision 25.0.0

#### (October 2016)

### Important changes

- [ContextCompat](https://developer.android.com/reference/androidx/core/content/ContextCompat)constructor has been made protected. This class should not be publicly instantiated, but it may be extended by support libraries targeting newer API levels.
- [ActivityCompat](https://developer.android.com/reference/androidx/core/app/ActivityCompat)constructor has been made protected. This class should not be publicly instantiated, but it may be extended by support libraries targeting newer API levels.
- [getReferrer(Activity)](https://developer.android.com/reference/androidx/core/app/ActivityCompat#getReferrer(android.app.Activity))has been made static.
- `android.support.design.widget.CoordinatorLayout.Behavior.isDirty(CoordinatorLayout,
  V)`has been removed. Any client implementations of this method should be removed.
- `android.support.v4.media.session.MediaSessionCompat.obtain(Context,
  Object)`has been removed. Usages should be replaced with the more appropriately named method[`fromMediaSession()`](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat#fromMediaSession(android.content.Context,%20java.lang.Object)).
- `android.support.v4.media.session.MediaSessionCompat.QueueItem.obtain(Object)`has been removed. Usages should be replaced with the more appropriately named method[`MediaSessionCompat.QueueItem#fromQueueItem`](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.QueueItem#fromQueueItem(java.lang.Object)).
- `android.support.v7.widget.Space`has been removed. Usages should be replaced with[android.support.v4.widget.Space](https://developer.android.com/reference/androidx/legacy/widget/Space).

### New APIs

- `android.support.design.widget.BottomNavigationView`class implements the[bottom navigation](https://material.google.com/components/bottom-navigation.html)pattern from the Material Design spec.
- New[`
  android.support.v13.view.inputmethod`](https://developer.android.com/reference/android/support/v13/view/inputmethod/package-summary)package includes classes for accessing[android.view.inputmethod.InputConnection](https://developer.android.com/reference/android/view/inputmethod/InputConnection)features introduced after API level 13.
- `android.v7.widget.RecyclerView.DividerItemDecoration`class provides a base implementation for vertical or horizontal dividers between items.
- New decorated styles in`android.support.v7.app.NotificationCompat`,`DecoratedCustomViewStyle`and`DecoratedMediaCustomViewStyle`, mirror classes added in platform API 24.

### Fixed issues

A complete list of public bug fixes is available on the[AOSP Issue Tracker](https://code.google.com/p/android/issues/list?can=1&q=label:Target-Support-25.0.0).

## Revision 24.2.1

#### September 2016

Fixed issues:

- [FloatingActionButton](https://developer.android.com/reference/com/google/android/material/floatingactionbutton/FloatingActionButton)can no longer be anchored to indirect children of[CoordinatorLayout](https://developer.android.com/reference/androidx/coordinatorlayout/widget/CoordinatorLayout). (AOSP issue[220250](https://code.google.com/p/android/issues/detail?id=220250))
- Image inside[CollapsingToolbarLayout](https://developer.android.com/reference/com/google/android/material/appbar/CollapsingToolbarLayout)doesn't scale properly with`fitsSystemWindows=true`. (AOSP issue[220389](https://code.google.com/p/android/issues/detail?id=220389))
- [CoordinatorLayout](https://developer.android.com/reference/androidx/coordinatorlayout/widget/CoordinatorLayout)throws[IndexOutOfBoundsException](https://developer.android.com/reference/java/lang/IndexOutOfBoundsException)when[Snackbar](https://developer.android.com/reference/com/google/android/material/snackbar/Snackbar)is shown and dismissed. (AOSP issue[220762](https://code.google.com/p/android/issues/detail?id=220762))
- [TextInputLayout](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout)fails to resolve error text color. (AOSP issue[220305](https://code.google.com/p/android/issues/detail?id=220305))
- [BatchedCallback.onMoved()](https://developer.android.com/reference/androidx/recyclerview/widget/SortedList.BatchedCallback#onMoved(int, int))calls[BatchedCallback.onInserted()](https://developer.android.com/reference/androidx/recyclerview/widget/SortedList.BatchedCallback#onInserted(int, int)). (AOSP issue[220309](https://code.google.com/p/android/issues/detail?id=220309))
- [TextInputLayout](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout)overrides right compound drawable. (AOSP issue[220728](https://code.google.com/p/android/issues/detail?id=220728))

A complete list of public bug fixes is available on the[AOSP Issue Tracker](https://code.google.com/p/android/issues/list?can=1&q=label:Target-Support-24.2.1).

## Revision 24.2.0

#### August 2016

Release 24.2.0 contains the following changes:

- [v4 Support Library split](https://developer.android.com/topic/libraries/support-library/rev-archive#24-2-0-v4-refactor)
- [API updates](https://developer.android.com/topic/libraries/support-library/rev-archive#24-2-0-api-updates)
- [Behavior changes](https://developer.android.com/topic/libraries/support-library/rev-archive#24-2-0-behavior)
- [Deprecations](https://developer.android.com/topic/libraries/support-library/rev-archive#24-2-0-deprecations)
- [Bug fixes](https://developer.android.com/topic/libraries/support-library/rev-archive#24-2-0-bugfixes)

**Note:**Release 24.2.0 removes support for Android 2.2 (API level 8) and lower. Classes and methods that exist only to serve those system versions are now marked as deprecated and should no longer be used. These deprecated classes and methods may be removed in a future release.

### v4 Support Library split

With this release, the[v4 Support Library](https://developer.android.com/topic/libraries/support-library/features#v4)has been split into several smaller modules:

`support-compat`
:   Provides compatibility wrappers for new framework APIs, such as`Context.getDrawable()`and`View.performAccessibilityAction()`.

`support-core-utils`
:   Provides a number of utility classes, such as[AsyncTaskLoader](https://developer.android.com/reference/androidx/loader/content/AsyncTaskLoader)and[PermissionChecker](https://developer.android.com/reference/androidx/core/content/PermissionChecker).

`support-core-ui`
:   Implements a variety of UI-related components, such as[ViewPager](https://developer.android.com/reference/androidx/viewpager/widget/ViewPager),[NestedScrollView](https://developer.android.com/reference/androidx/core/widget/NestedScrollView), and[ExploreByTouchHelper](https://developer.android.com/reference/androidx/customview/widget/ExploreByTouchHelper).

`support-media-compat`
:   Backports portions of the[media](https://developer.android.com/reference/android/media/package-summary)framework, including[MediaBrowser](https://developer.android.com/reference/android/media/browse/MediaBrowser)and[MediaSession](https://developer.android.com/reference/android/media/session/MediaSession).

`support-fragment`
:   Backports the[fragment](https://developer.android.com/guide/components/fragments)framework. This module has dependencies on`support-compat`,`support-core-utils`,`support-core-ui`, and`support-media-compat`.

For backwards compatibility, if you list`support-v4`in your Gradle script, your APK will include all of these modules. However, to reduce APK size, we recommend that you just list the specific modules your app needs.

### API updates

- Clients using[Custom Tabs](https://developer.android.com/topic/libraries/support-library/features#custom-tabs)can control whether Instant Apps should open. (Note that Instant Apps are not yet generally available.) To enable or disable Instant Apps, call[`CustomTabsIntent.Builder.setInstantAppsEnabled()`](https://developer.android.com/reference/androidx/browser/customtabs/CustomTabsIntent.Builder#setInstantAppsEnabled(boolean))or specify[`EXTRA_ENABLE_INSTANT_APPS`](https://developer.android.com/reference/androidx/browser/customtabs/CustomTabsIntent#EXTRA_ENABLE_INSTANT_APPS). By default, Custom Tabs will default to enabling Instant Apps, when that feature becomes available.
- [TextInputLayout](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout)adds support for the[password visibility toggle](https://material.google.com/components/text-fields.html#text-fields-password-input)from the material design specification.
- The new[`android.support.transition`](https://developer.android.com/reference/android/support/transition/package-summary)package backports the[Transitions](https://developer.android.com/training/transitions)framework to API levels 14 and higher. For more information, see the[`android.support.transition`](https://developer.android.com/reference/android/support/transition/package-summary)reference.
- The[Custom Tabs support library](https://developer.android.com/topic/libraries/support-library/features#custom-tabs)adds support for using[RemoteViews](https://developer.android.com/reference/android/widget/RemoteViews)in the secondary toolbar. The existing[setToolbarItem()](https://developer.android.com/reference/androidx/browser/customtabs/CustomTabsSession#setToolbarItem(int, android.graphics.Bitmap, java.lang.String))method is now deprecated.
- [AppCompatResources](https://developer.android.com/reference/androidx/appcompat/content/res/AppCompatResources)adds the ability to load a`<vector>`(on API level 9 and higher) or`<animated-vector>`(on API level 11 and higher) from a resource ID, by using the new[`getDrawable()`](https://developer.android.com/reference/androidx/appcompat/content/res/AppCompatResources#getDrawable(android.content.Context,%20int))method.
- [CoordinatorLayout](https://developer.android.com/reference/androidx/coordinatorlayout/widget/CoordinatorLayout)now supports defining inset views, and specifying that other views should dodge the inset views. This allows apps to replicate behavior patterns similar to the way[FloatingActionButton](https://developer.android.com/reference/com/google/android/material/floatingactionbutton/FloatingActionButton)moves out of the way of a[Snackbar](https://developer.android.com/reference/com/google/android/material/snackbar/Snackbar), but for any arbitrary view children. For more information, see the[`LayoutParams.insetEdge`](https://developer.android.com/reference/androidx/coordinatorlayout/widget/CoordinatorLayout.LayoutParams#insetEdge)and[`LayoutParams.dodgeInsetEdges`](https://developer.android.com/reference/androidx/coordinatorlayout/widget/CoordinatorLayout.LayoutParams#dodgeInsetEdges)reference documentation.
- The new[`
  DiffUtil`](https://developer.android.com/reference/androidx/recyclerview/widget/DiffUtil)class can calculate the difference between two collections, and can dispatch a list of update operations that are suitable to be consumed by a[RecyclerView.Adapter](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView.Adapter).
- [`
  RecyclerView.OnFlingListener`](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView.OnFlingListener)has been added to support custom behavior in response to flings. The[`SnapHelper`](https://developer.android.com/reference/androidx/recyclerview/widget/SnapHelper)class provides an implementation specifically for snapping child views, and the[`LinearSnapHelper`](https://developer.android.com/reference/androidx/recyclerview/widget/LinearSnapHelper)class extends this implementation to provide center-aligned snapping behavior similar to[ViewPager](https://developer.android.com/reference/androidx/viewpager/widget/ViewPager).
- The Custom Tabs library now allows clients to request the standard browser UI, rather than custom tabs UI, by calling[`CustomTabsIntent.setAlwaysUseBrowserUI()`](https://developer.android.com/reference/androidx/browser/customtabs/CustomTabsIntent#setAlwaysUseBrowserUI(android.content.Intent)). This behavior is useful in cases where the browser defaults to custom tabs UI but the user has expressed a preference for the standard browser UI.

### Behavior changes

- If you use the appcompat library's day/night functionality, the system now automatically recreates your activity whenever the day/night mode changes (either because of the time of day, or because of a call to[AppCompatDelegate.setLocalNightMode()](https://developer.android.com/reference/androidx/appcompat/app/AppCompatDelegate#setLocalNightMode(int))).
- [Snackbar](https://developer.android.com/reference/com/google/android/material/snackbar/Snackbar)now draws behind the navigation bar if the status bar is translucent.

#### MediaRouter library

Bluetooth devices are no longer listed as media routes. Routing audio to Bluetooth devices is now solely controlled at the Android system level.

### Deprecations

Deprecated classes and methods are subject to removal in a future release. You should migrate away from these APIs as soon as possible.

- Several methods on the following classes were only required for API 8 and lower, and should no longer be used. Instead, use the framework implementations.
  - `android.support.v4.view.KeyEventCompat`: Replace with[KeyEvent](https://developer.android.com/reference/android/view/KeyEvent)
  - `android.support.v4.view.MotionEventCompat`: Use[MotionEvent](https://developer.android.com/reference/android/view/MotionEvent)
  - `android.support.v4.view.ViewCompat`: Use[View](https://developer.android.com/reference/android/view/View)
  - `android.support.v4.view.ViewConfigurationCompat`: Use[ViewConfiguration](https://developer.android.com/reference/android/view/ViewConfiguration)
- `AccessibilityServiceInfoCompat.getDescription()`has been deprecated in favor of[AccessibilityServiceInfoCompat.loadDescription()](https://developer.android.com/reference/androidx/core/accessibilityservice/AccessibilityServiceInfoCompat#loadDescription(android.accessibilityservice.AccessibilityServiceInfo, android.content.pm.PackageManager)), which returns a correctly localized description.
- You should not instantiate the`ActivityCompat`class directly. The non-static`getReferrer(Activity)`method will be made static in an upcoming release.
- `CoordinatorLayout.Behavior.isDirty()`has been deprecated and is no longer called by[CoordinatorLayout](https://developer.android.com/reference/androidx/coordinatorlayout/widget/CoordinatorLayout). Any implementations, as well as any calls to this method, should be removed.
- `MediaSessionCompat.obtain()`has been deprecated and replaced with the more appropriately-named method[fromMediaSession()](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat#fromMediaSession(android.content.Context, java.lang.Object)).
- `MediaSessionCompat.QueueItem.obtain()`has been deprecated and replaced with the more appropriately-named method[fromQueueItem()](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.QueueItem#fromQueueItem(java.lang.Object)).
- Several abstract classes have been deprecated and replaced with interfaces that more closely reflect their framework equivalents.
  - `AccessibilityStateChangeListenerCompat`has been replaced by the[`AccessibilityManagerCompat.AccessibilityStateChangeListener`](https://developer.android.com/reference/androidx/core/view/accessibility/AccessibilityManagerCompat.AccessibilityStateChangeListener)interface.
  - `OnCloseListenerCompat`has been replaced by the[`SearchViewCompat.OnCloseListener`](https://developer.android.com/reference/android/support/v4/widget/SearchViewCompat.OnCloseListener)interface.
  - `OnQueryTextListenerCompat`has been replaced by the[`SearchViewCompat.OnQueryTextListener`](https://developer.android.com/reference/android/support/v4/widget/SearchViewCompat.OnQueryTextListener)interface.
- `CustomTabsSession.setToolbarItem()`has been deprecated and replaced by the RemoteViews-based[`setSecondaryToolbarViews()`](https://developer.android.com/reference/androidx/browser/customtabs/CustomTabsSession#setSecondaryToolbarViews).

### Bug fixes

The following known issues have been fixed with release 24.2.0:

- Ensure`SwipeRefreshLayout`indicator is shown when`setRefreshing(true)`is called before the first measurement pass ([AOSP issue 77712](https://code.google.com/p/android/issues/detail?id=77712))
- Prevent`TabLayout`from flickering when changing pages ([AOSP issue 180454](https://code.google.com/p/android/issues/detail?id=180454))
- Avoid`ClassNotFoundException`when unmarshalling`SavedState`on API level 11 and lower ([AOSP issue 196430](https://code.google.com/p/android/issues/detail?id=196430))

A complete list of public bug fixes is available on the[AOSP Issue Tracker](https://code.google.com/p/android/issues/list?can=1&q=Component%3DSupport-Libraries+Target%3DSupport-24.2.0).

## Revision 24.1.1

#### July 2016

Fixed issues:

- Fixes an issue in the 24.1.0 release which affected resource IDs shared between support libraries. This issue caused apps that depended on support libraries with resources (such as design and appcompat) to encounter issues caused by resource ID mismatches.

## Revision 24.1.0

#### July 2016

Changes for[v4 Support Library](https://developer.android.com/tools/support-library/features#v4):
:
    - [NotificationCompat.Action.WearableExtender](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Action.WearableExtender)has new`getHintDisplayActionInline()`and`setHintDisplayActionInline()`methods for compatibility with[Android Wear 2.0 Preview](https://developer.android.com/wear/preview). These methods allow an application to specify that an action should be displayed inline with the notification.
    - Calling[Fragment.setUserVisbileHint()](https://developer.android.com/reference/androidx/fragment/app/Fragment#setUserVisibleHint(boolean))will no longer cause a fragment to become**started** if the hint has been added to a[FragmentTransaction](https://developer.android.com/reference/androidx/fragment/app/FragmentTransaction)that is not yet committed. This affects users of[FragmentPagerAdapter](https://developer.android.com/reference/androidx/fragment/app/FragmentPagerAdapter)that override[setUserVisbileHint()](https://developer.android.com/reference/androidx/fragment/app/Fragment#setUserVisibleHint(boolean))and assume a specific lifecycle state of the fragment after calling`super.setUserVisibleHint()`. For more information, see the reference page for docs for[Fragment.setUserVisbileHint()](https://developer.android.com/reference/androidx/fragment/app/Fragment#setUserVisibleHint(boolean)).

Fixed issues:

- TabLayout.setCustomView(null) results in NullPointerException ([AOSP issue 214753](https://code.google.com/p/android/issues/detail?id=214753))
- TabLayout incorrectly highlights custom tabs ([AOSP issue 214316](https://code.google.com/p/android/issues/detail?id=214316))
- AppCompatTextHelper uses incorrectly sorted attribute array ([AOSP issue 214366](https://code.google.com/p/android/issues/detail?id=214366))
- Unable to reference VectorDrawable from drawable container XML when using custom ContextWrapper ([AOSP issue 214055](https://code.google.com/p/android/issues/detail?id=214055))
- ViewDragHelper.saveLastMotion() throws ArrayIndexOutOfBoundsException ([AOSP issue 212945](https://code.google.com/p/android/issues/detail?id=212945))
- BottomSheetBehavior expands to old content height when using setState(STATE_EXPANDED) ([AOSP issue 213660](https://code.google.com/p/android/issues/detail?id=213660))
- CollapsingToolbarLayout doesn't handle pinnable children with top or bottom margins ([AOSP issue 213001](https://code.google.com/p/android/issues/detail?id=213001))
- Leanback browse title does not support RTL alignment ([AOSP issue 213461](https://code.google.com/p/android/issues/detail?id=213461))
- PagerTabStrip disappears due to missing inherited annotation ([AOSP issue 213359](https://code.google.com/p/android/issues/detail?id=213359))
- Data binding throws NullPointerException when using Boolean to set conditional flags ([AOSP issue 191841](https://code.google.com/p/android/issues/detail?id=191841))
- CoordinatorLayout does not respond to setFitsSystemWindows() ([AOSP issue 212720](https://code.google.com/p/android/issues/detail?id=212720))
- BottomSheetBehavior crashes when setting initial state ([AOSP issue 203114](https://code.google.com/p/android/issues/detail?id=203114))
- ViewPager skips pages if the page index is a large value ([AOSP issue 211734](https://code.google.com/p/android/issues/detail?id=211734))
- BottomSheetBehavior does not work with dynamic layouts ([AOSP issue 205226](https://code.google.com/p/android/issues/detail?id=205226))

## Revision 24.0.0

#### June 2016

Changes for[v4 Support Library](https://developer.android.com/tools/support-library/features#v4):
:
    - Added`Fragment.commitNow()`for synchronous commit
    - Added`NotificationCompat.MessagingStyle`for multi-party conversations
    - Added`NotificationManagerCompat.areNotificationsEnabled()`and`getImportance()`
    - [MediaSessionCompat](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat)now mirrors the functionality of[MediaSession](https://developer.android.com/reference/android/media/session/MediaSession)and no longer calls[setMediaButtonReceiver()](https://developer.android.com/reference/android/media/session/MediaSession#setMediaButtonReceiver(android.app.PendingIntent))automatically

    **Note:** Only[`MediaBrowserServiceCompat`](https://developer.android.com/reference/androidx/media/MediaBrowserServiceCompat)in version 24.0.0 is forward-compatible with future versions of Android beyond API 24. If you are using previous versions, update to this version to ensure compatibility.

Changes for[v7 appcompat library](https://developer.android.com/tools/support-library/features#v7-appcompat):
:
    - Added support for referencing themed[ColorStateList](https://developer.android.com/reference/android/content/res/ColorStateList)objects from XML

Changes for[Design Support Library](https://developer.android.com/tools/support-library/features#design):
:
    - Improvements to[AppBarLayout](https://developer.android.com/reference/com/google/android/material/appbar/AppBarLayout)handling of elevation using[StateListAnimator](https://developer.android.com/reference/android/animation/StateListAnimator)

Changes for[v17 Leanback library](https://developer.android.com/topic/libraries/support-library/features#v17-leanback):
:
    - Added`OnboardingFragment`to provide first-run welcome and setup flow

Changes for[custom tabs](https://developer.android.com/topic/libraries/support-library/features#custom-tabs):
:
    - Added support for providing a[RemoteViews](https://developer.android.com/reference/android/widget/RemoteViews)hierarchy for the secondary toolbar
    - Added`CustomTabsClient.connectAndInitialize()`for one-line warm up

## Revision 23.4.0

#### May 2016

Changes for[v4 Support Library](https://developer.android.com/tools/support-library/features#v4):
:
    - Fixed issue where fragments were added in the wrong order. ([Issue 206901](https://code.google.com/p/android/issues/detail?id=206901))
    - Fixed issue where app bar wasn't drawn after being scrolled offscreen. ([Issue 178037](https://code.google.com/p/android/issues/detail?id=178037))

Changes for[v7 appcompat library](https://developer.android.com/tools/support-library/features#v7-appcompat):
:
    - Added[AppCompatDelegate.setCompatVectorFromResourcesEnabled()](https://developer.android.com/reference/androidx/appcompat/app/AppCompatDelegate#setCompatVectorFromResourcesEnabled(boolean))method to re-enable usage of vector drawables in[DrawableContainer](https://developer.android.com/reference/android/graphics/drawable/DrawableContainer)objects on devices running Android 4.4 (API level 19) and lower. See[AppCompat v23.2 --- Age of the vectors](https://medium.com/@chrisbanes/appcompat-v23-2-age-of-the-vectors-91cbafa87c88#.44uulkfal)for more information.
    - Fixed an issue in API 23 with[`AppCompatDelegate.setDefaultNightMode()`](https://developer.android.com/reference/androidx/appcompat/app/AppCompatDelegate#setDefaultNightMode(int))not loading correct resources in API level 23. ([Issue 206573](https://code.google.com/p/android/issues/detail?id=206573))
    - Fixed issue that could cause[NullPointerException](https://developer.android.com/reference/java/lang/NullPointerException). ([Issue 207638](https://code.google.com/p/android/issues/detail?id=207638))

Changes for[Design Support Library](https://developer.android.com/tools/support-library/features#design):
:
    - Fixed an issue where[TextInputLayout](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout)doesn't clear error tint after[setErrorEnabled(false)](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout#setErrorEnabled(boolean))on API level 21 - 22 ([Issue 202829](https://code.google.com/p/android/issues/detail?id=202829))
    - Fixed an issue where[FloatingActionButton](https://developer.android.com/reference/com/google/android/material/floatingactionbutton/FloatingActionButton)does not return when animations are disabled. ([Issue 206416](https://code.google.com/p/android/issues/detail?id=206416))
    - Fixed issue in[AppBarLayout](https://developer.android.com/reference/com/google/android/material/appbar/AppBarLayout)snap functionality when used with[scroll](https://developer.android.com/reference/com/google/android/material/R.id#scroll)`|`[enterAlways](https://developer.android.com/reference/com/google/android/material/R.id#enterAlways)`|`[enterAlwaysCollapsed](https://developer.android.com/reference/com/google/android/material/R.id#enterAlwaysCollapsed)`|`[snap](https://developer.android.com/reference/com/google/android/material/R.id#snap)scroll flags. ([Issue 207398](https://code.google.com/p/android/issues/detail?id=207398))

Changes forVector Drawable library:
:
    - Fixed a bug where[VectorDrawableCompat](https://developer.android.com/reference/androidx/vectordrawable/graphics/drawable/VectorDrawableCompat)does not render correctly in[TextView](https://developer.android.com/reference/android/widget/TextView)on API level 23. ([Issue 206227](https://code.google.com/p/android/issues/detail?id=206227))

## Revision 23.3.0

#### April 2016

Changes for[v4 Support Library](https://developer.android.com/tools/support-library/features#v4):
:
    - Added`AppLaunchChecker`to help track how your app has been launched by the user in the past.`hasStartedFromLauncher()`lets you know if the user has launched your app from the home screen before, or if it has only been started by other means (for example, to view specific web URLs).
    - Fixed a memory leak in`MediaBrowserServiceCompat.mConnections`. ([Issue 205220](https://code.google.com/p/android/issues/detail?id=205220))
    - Fixed issue where[ViewPager](https://developer.android.com/reference/androidx/viewpager/widget/ViewPager)does not account for page margins when flipping page. ([Issue 203816](https://code.google.com/p/android/issues/detail?id=203816))
    - [Fragment.onRequestPermissionsResult()](https://developer.android.com/reference/androidx/fragment/app/Fragment#onRequestPermissionsResult(int, java.lang.String[], int[]))is now delivered to child fragments.

Changes for[v7 appcompat library](https://developer.android.com/tools/support-library/features#v7-appcompat):
:
    - Fixed an issue in[AppCompatSpinner](https://developer.android.com/reference/androidx/appcompat/widget/AppCompatSpinner)that could cause multiple popups to appear. ([Issue 205052](https://code.google.com/p/android/issues/detail?id=205052))
    - Fixed an issue with how borderless buttons were colored. ([Issue 202967](https://code.google.com/p/android/issues/detail?id=202967))
    - Fixed a compatibility issue between[AppCompatDialogFragment](https://developer.android.com/reference/androidx/appcompat/app/AppCompatDialogFragment)and[AlertDialog](https://developer.android.com/reference/androidx/appcompat/app/AlertDialog). ([Issue 204805](https://code.google.com/p/android/issues/detail?id=204805))
    - Reverted changes to`TintResources`that were causing memory and configuration issues. ([Issue 205236](https://code.google.com/p/android/issues/detail?id=205236))

Changes for[v7 mediarouter library](https://developer.android.com/tools/support-library/features#v7-mediarouter):
:
    - Fixed[MediaRouteControllerDialog](https://developer.android.com/reference/androidx/mediarouter/app/MediaRouteControllerDialog)volume slider's behavior. ([Issue 202299](https://code.google.com/p/android/issues/detail?id=202299))

Changes for[v7 Preference](https://developer.android.com/topic/libraries/support-library/features#v7-preference)library:
:
    - Fixed issue where[PreferenceFragmentCompat](https://developer.android.com/reference/androidx/preference/PreferenceFragmentCompat)would crash if`dividerHeight`is specified. ([Issue 204778](https://code.google.com/p/android/issues/detail?id=204778))

Changes for[v7 recyclerview library](https://developer.android.com/tools/support-library/features#v7-recyclerview):
:
    - Fixed a bug where[RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView)would not invoke scroll callbacks if the range of visible items shrank. ([Issue 200987](https://code.google.com/p/android/issues/detail?id=200987))
    - Fixed a bug where[RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView)would freeze if it was in linear layout, was weighted, and contained images. ([Issue 203276](https://code.google.com/p/android/issues/detail?id=203276))
    - Fixed a crash in[OrientationHelper.getStartAfterPadding()](https://developer.android.com/reference/androidx/recyclerview/widget/OrientationHelper#getStartAfterPadding()). ([Issue 180521](https://code.google.com/p/android/issues/detail?id=180521))
    - Fixed a crash with usages of`android:nestedScrollingEnabled`. ([Issue 197932](https://code.google.com/p/android/issues/detail?id=197932))

Changes for[Design Support Library](https://developer.android.com/tools/support-library/features#design):
:
    - Fixed a bug where a hidden bottom sheet would handle touch events. ([Issue 203654](https://code.google.com/p/android/issues/detail?id=203654))
    - Fixed a layout issue with`BottomSheetBehavior`when`fitsSystemWindows`is true. ([Issue 203057](https://code.google.com/p/android/issues/detail?id=203057))
    - Fixed an accessibility issue with[Snackbar](https://developer.android.com/reference/com/google/android/material/snackbar/Snackbar). ([Issue 182145](https://code.google.com/p/android/issues/detail?id=182145))
    - Fixed a crash on[Snackbar](https://developer.android.com/reference/com/google/android/material/snackbar/Snackbar)swipe. ([Issue 203924](https://code.google.com/p/android/issues/detail?id=203924))
    - Fixed a bug in[AppBarLayout](https://developer.android.com/reference/com/google/android/material/appbar/AppBarLayout)with`enterAlways`. ([Issue 203661](https://code.google.com/p/android/issues/detail?id=203661))
    - Fixed a bug where[TextInputLayout](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout)unnecessarily clears[EditText](https://developer.android.com/reference/android/widget/EditText)object's background color filter. ([Issue 203357](https://code.google.com/p/android/issues/detail?id=203357))

## Revision 23.2.1

#### March 2016

Changes for[v4 Support Library](https://developer.android.com/tools/support-library/features#v4):
:
    - Fixed an exception in[DrawableCompat.wrap()](https://developer.android.com/reference/androidx/core/graphics/drawable/DrawableCompat#wrap(android.graphics.drawable.Drawable))and[LayerDrawable](https://developer.android.com/reference/android/graphics/drawable/LayerDrawable)on API levels 17 to 19. ([Issue 201817](https://code.google.com/p/android/issues/detail?id=201817))
    - Fixed an`ArrayIndexOutOfBoundsException`in[ViewDragHelper.shouldInterceptTouchEvent()](https://developer.android.com/reference/androidx/customview/widget/ViewDragHelper#shouldInterceptTouchEvent(android.view.MotionEvent)). ([Issue 182262](https://code.google.com/p/android/issues/detail?id=182262))
    - Fixed a bug in[ViewPager](https://developer.android.com/reference/androidx/viewpager/widget/ViewPager)related to scroll calculation for size changes.
    - Fixed a`NullPointerException`when`DrawerLayout.removeDrawerListener()`is called without a set[DrawerLayout.DrawerListener](https://developer.android.com/reference/androidx/drawerlayout/widget/DrawerLayout.DrawerListener). ([Issue 202478](https://code.google.com/p/android/issues/detail?id=202478))
    - Fixed a bug where[ViewPager](https://developer.android.com/reference/androidx/viewpager/widget/ViewPager)does not set[AccessibilityEvent](https://developer.android.com/reference/android/view/accessibility/AccessibilityEvent)parameters properly when scrolling.
    - Fixed an issue that caused lag during device rotation when using[Drawable.wrap()](https://developer.android.com/reference/androidx/core/graphics/drawable/DrawableCompat#wrap(android.graphics.drawable.Drawable)). ([Issue 201924](https://code.google.com/p/android/issues/detail?id=201924))

Changes for[v7 appcompat library](https://developer.android.com/tools/support-library/features#v7-appcompat):
:
    - Reverted dependency on vector assets so that developers using the[appcompat library](https://developer.android.com/tools/support-library/features#v7-appcompat)are not forced to use[VectorDrawable](https://developer.android.com/reference/android/graphics/drawable/VectorDrawable)and its associated build flags.
    - Fixed a compatibility issue with Night Mode and API level 23. ([Issue 201910](https://code.google.com/p/android/issues/detail?id=201910))
    - Fixed a compatibility issue with[SwitchCompat](https://developer.android.com/reference/androidx/appcompat/widget/SwitchCompat)and API level 7. ([Issue 201942](https://code.google.com/p/android/issues/detail?id=201942))
    - Fixed an issue with propagating configuration values in Resources objects[Issue 201928](https://code.google.com/p/android/issues/detail?id=201928)
    - Fixed a compatibility issue where the`android.support.v7.app.NotificationCompat.MediaStyle`cancel button becomes invisible on API level 21 and below. ([Issue 202156](https://code.google.com/p/android/issues/detail?id=202156))
    - Fixed a compatibility crash with[AppCompatSpinner](https://developer.android.com/reference/androidx/appcompat/widget/AppCompatSpinner)on API level 21 and below. ([Issue 202246](https://code.google.com/p/android/issues/detail?id=202246))
    - Fixed an issue where the`app:textAllCaps = "false"`style did not work. ([Issue 202117](https://code.google.com/p/android/issues/detail?id=202117))
    - Fixed a crash when restoring[SearchView](https://developer.android.com/reference/android/widget/SearchView). ([Issue 201836](https://code.google.com/p/android/issues/detail?id=201836))
    - Fixed a memory leak that occurs when tinting drawable resources using AppCompat. ([Issue 202379](https://code.google.com/p/android/issues/detail?id=202379))
    - Fixed an issue with[KeyEvent](https://developer.android.com/reference/android/view/KeyEvent)on API level 11 and lower. ([Issue 202939](https://code.google.com/p/android/issues/detail?id=202939))

Changes for[v7 cardview library](https://developer.android.com/tools/support-library/features#v7-cardview):
:
    - Added Night Mode support for[CardView](https://developer.android.com/reference/androidx/cardview/widget/CardView). ([Issue 194497](https://code.google.com/p/android/issues/detail?id=194497))

Changes for[v7 recyclerview library](https://developer.android.com/tools/support-library/features#v7-recyclerview):
:
    - Fixed bugs related to various measure-spec methods. ([Issue 201856](https://code.google.com/p/android/issues/detail?id=201856))
    - Reduced the lockdown period in which[RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView)does not allow adapter changes while calculating a layout or scroll. ([Issue 202046](https://code.google.com/p/android/issues/detail?id=202046))
    - Fixed a crash when calling[notifyItemChanged()](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView.Adapter#notifyItemChanged(int))on an item that is out of view. ([Issue 202136](https://code.google.com/p/android/issues/detail?id=202136))
    - Fixed a crash that occurs when[RecyclerView.LayoutManager](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView.LayoutManager)adds and removes a view in the same measurement pass. ([Issue 193958](https://code.google.com/p/android/issues/detail?id=193958))

Changes for[v7 mediarouter library](https://developer.android.com/tools/support-library/features#v7-mediarouter):
:
    - Fixed a crash that occurs when calling[MediaRouter.getInstance()](https://developer.android.com/reference/androidx/mediarouter/media/MediaRouter#getInstance(android.content.Context))on API level 17. ([Issue 180654](https://code.google.com/p/android/issues/detail?id=180654))

Changes for[v17 Leanback Library](https://developer.android.com/tools/support-library/features#v17-leanback):
:
    - Fixed an issue with`GridLayout.onAddFocusables()`that caused the wrong item to be selected.
    - Fixed issue with[GuidedStepFragment](https://developer.android.com/reference/androidx/leanback/app/GuidedStepFragment)actions disappearing after an action was collapsed.

Changes for[Design Support Library](https://developer.android.com/tools/support-library/features#design):
:
    - Fixed a[TabLayout](https://developer.android.com/reference/com/google/android/material/tabs/TabLayout)crash caused by tab-pooling. ([Issue 201827](https://code.google.com/p/android/issues/detail?id=201827))
    - Fixed a bug in[NavigationView](https://developer.android.com/reference/com/google/android/material/navigation/NavigationView)that caused the wrong color to be selected. ([Issue 201951](https://code.google.com/p/android/issues/detail?id=201951))
    - Fixed a bug where[setBackgroundTintList()](https://developer.android.com/reference/com/google/android/material/floatingactionbutton/FloatingActionButton#setBackgroundTintList(android.content.res.ColorStateList))was no longer able to change the background color. ([Issue 201873](https://code.google.com/p/android/issues/detail?id=201873))
    - Fixed an issue where[AppBarLayout](https://developer.android.com/reference/com/google/android/material/appbar/AppBarLayout)did not completely scroll out of view when used with`android:fitsSystemWindows = "true"`. ([Issue 201822](https://code.google.com/p/android/issues/detail?id=201822))
    - Fixed an issue where`BottomSheetDialog`did not display short content views correctly. ([Issue 201793](https://code.google.com/p/android/issues/detail?id=201793))
    - Fixed an issue where`BottomSheetDialogFragment`moved sporadically when content inside was changed. ([Issue 202125](https://code.google.com/p/android/issues/detail?id=202125))
    - Fixed a crash in TextInputLayout counter[link](https://code.google.com/p/android/issues/detail?id=202051)
    - Fixed a crash that occurred when[TextInputLayout.getCounterMaxLength()](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout#getCounterMaxLength())restored a saved state. ([Issue 202375](https://code.google.com/p/android/issues/detail?id=202375))
    - Fixed a`ClassCastException`that occurred when restoring a[CoordinatorLayout](https://developer.android.com/reference/androidx/coordinatorlayout/widget/CoordinatorLayout)using the saved state of a view that was not a[CoordinatorLayout](https://developer.android.com/reference/androidx/coordinatorlayout/widget/CoordinatorLayout).

Changes for VectorDrawableCompat:
:
    - Fixed a bug where the wrong variable was read for`android:tintMode`. ([Issue 201907](https://code.google.com/p/android/issues/detail?id=201907))

## Revision 23.2.0

#### February 2016

Changes for[v4 Support library](https://developer.android.com/topic/libraries/support-library/features#v4):
:
    - Added`MediaBrowserCompat`for[MediaBrowser](https://developer.android.com/reference/android/media/browse/MediaBrowser)support, and`MediaBrowserServiceCompat`for[MediaBrowserService](https://developer.android.com/reference/android/service/media/MediaBrowserService)support. This is useful when connecting a media app's background service with UI components, and integrating with Android Auto and Android Wear without requiring API level 21 or higher.
    - The system now calls[onActivityResult()](https://developer.android.com/reference/androidx/fragment/app/FragmentActivity#onActivityResult(int, int, android.content.Intent))for a nested[FragmentActivity](https://developer.android.com/reference/androidx/fragment/app/FragmentActivity).

Changes for[v7 AppCompat library](https://developer.android.com/topic/libraries/support-library/features#v7-appcompat):
:
    - Added Night Mode functionality to API level 14 and higher. Switch between[Material Light and Material Dark Themes](https://developer.android.com/training/material/theme)based on the time of day or app-specific setting.
    -
      - Day and night themes can be found here:`<sdk>/extras/android/support/v7/appcompat/res/values/themes_daynight.xml`
      - `AppCompatDelegate.setDefaultNightMode()`: sets the app's default mode by passing one of the following constants:
      -
        - `MODE_NIGHT_AUTO`
        - `MODE_NIGHT_NO`
        - `MODE_NIGHT_YES`
        - `MODE_NIGHT_FOLLOW_SYSTEM`
      - `AppCompatDelegate.setLocalNightMode()`: overrides the night mode setting for the local app component.
      - `AppCompatDelegate.getDefaultNightMode()`: returns the default night mode.

Changes for[v7 mediarouter library](https://developer.android.com/topic/libraries/support-library/features#v7-mediarouter):
:
    - [MediaRouteControllerDialog](https://developer.android.com/reference/androidx/mediarouter/app/MediaRouteControllerDialog)now correctly applies custom app theme colors.

Changes for[Design support library](https://developer.android.com/topic/libraries/support-library/features#design):
:
    - Added support for[bottom sheets](https://material.io/guidelines/components/bottom-sheets.html). An interaction plugin,`BottomSheetBehavior`, allows a child view of a[CoordinatorLayout](https://developer.android.com/reference/androidx/coordinatorlayout/widget/CoordinatorLayout)to act as a bottom sheet. The base class,`BottomSheetCallback`, provides callbacks to monitor bottom sheet events.

Changes for the[CustomTabs support library](https://developer.android.com/topic/libraries/support-library/features#custom-tabs):
:
    - [Chrome Custom Tabs](https://developer.chrome.com/multidevice/android/customtabs)now allows apps to include a bottom bar with action buttons in addition to the existing top action button.
    - `CustomTabsIntent.Builder.addToolBarItem()`: adds an action button to a custom tab. You can use this to add multiple buttons.
    - `CustomTabsSession.setToolBarItem()`: updates the visuals for toolbar items. This method will only succeed if it is given a valid id and the browser session is in the foreground.

Added VectorDrawable support library:
:
    - Added Classes:
    -
      - `VectorDrawableCompat`
      - `AnimatedVectorDrawableCompat`
    - Adds support for[VectorDrawable](https://developer.android.com/reference/android/graphics/drawable/VectorDrawable)assets to apps running on API level 7 or higher.[AnimatedVectorDrawable](https://developer.android.com/reference/android/graphics/drawable/AnimatedVectorDrawable)assets are also supported on API level 11 or higher. Vector assets can be considerably smaller than image assets and should help reduce app size by reducing the amount of assets required to support multiple device screens.
    - This library is now a dependency of the[v7 AppCompat library](https://developer.android.com/topic/libraries/support-library/features#v7-appcompat), allowing developers and[AppCompat](https://developer.android.com/topic/libraries/support-library/features#v7-appcompat)to easily use vector drawables. To use`VectorDrawableCompat`within an[ImageButton](https://developer.android.com/reference/android/widget/ImageButton)or[ImageView](https://developer.android.com/reference/android/widget/ImageView), use the`app:srcCompat`XML attribute or`setImageResource()`method.
    - To keep referencing attribute IDs on API level 20 or lower, add the following`appt`flag to your`build,gradle`file:
    -
      - If you are building with Android Plugin for Gradle 1.5.0 or lower, add the following to your`build.gradle`file:
      -

        ```groovy
        android {
          defaultConfig {
            // Stops the Gradle's automatic rasterization of vectors
            generatedDensities = []
          }
           // Flag that tells aapt to keep the attribute ids
          aaptOptions {
            additionalParameters "--no-version-vectors"
          }
        }
        ```
      - If you are building with Android Plugin for Gradle 2.0.0 or higher, add the following to your`build.gradle`file:
      -

        ```groovy
        android {
          defaultConfig {
            vectorDrawables.useSupportLibrary = true
          }
        }
        ```

Changes for[v17 Leanback Library](https://developer.android.com/topic/libraries/support-library/features#v17-leanback):
:
    - Added new capabilities to[GuidedStepFragment](https://developer.android.com/reference/androidx/leanback/app/GuidedStepFragment), which is a component that guides users through a decision or series of decisions:
    -
      - Added button actions to[GuidedAction](https://developer.android.com/reference/androidx/leanback/widget/GuidedAction):
        - `GuidedStepFragment.setButtonActions()`: sets a list of[GuidedAction](https://developer.android.com/reference/androidx/leanback/widget/GuidedAction)buttons that the user may select from the Actions view.
      - Description fields are now editable:
      -
        - `GuidedAction.Builder.descriptionEditable()`: when passing`true`, sets the action's description to be editable.
        - `GuidedAction.getEditDescription()`: returns the editable description as a`CharSequence`.
      - Added drop-down lists of sub-actions:
      -
        - `GuidedAction.setSubActions()`: sets a[GuidedAction](https://developer.android.com/reference/androidx/leanback/widget/GuidedAction)list as a drop-down menu of sub-actions.
    - Added the`GuidedDatePickerAction`widget for[DatePicker](https://developer.android.com/reference/android/widget/DatePicker)functionality:
    -
      - The date is selected using year, month, and day columns and has a customizable range.
      - `GuidedDatePickerAction.Builder`: builder class for the`GuidedDatePickerAction`object.
      - `GuidedDatePickerAction.Builder.datePickerFormat(String
        datePickerFormat)`: set the desired date format by passing the appropriate three-character`String`, e.g.`"YMD"`or`"MDY"`. Alternatively, use the`datePickerFormat`XML attribute.

Changes for[v7 RecyclerView library](https://developer.android.com/topic/libraries/support-library/features#v7-recyclerview):
:
    - [RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView)now has an opt-in feature called*AutoMeasure* which allows[RecyclerView.LayoutManager](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView.LayoutManager)to easily wrap content or handle various measurement specifications provided by the parent of the[RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView). It supports all existing animation capabilities of the[RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView).
    -
      - If you have a custom[RecyclerView.LayoutManager](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView.LayoutManager), call`setAutoMeasureEnabled(true)`to start using the new AutoMeasure API. All built-in[RecyclerView.LayoutManager](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView.LayoutManager)objects enable auto-measure by default.
      - [RecyclerView.LayoutManager](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView.LayoutManager)no longer ignores some[RecyclerView.LayoutParams](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView.LayoutParams)settings, such as`MATCH_PARENT`in the scroll direction.

        **Note:**These lifted restrictions may cause unexpected behavior in your layouts. Make sure you specify the correct layout parameters.
    - When updating a[RecyclerView.ViewHolder](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView.ViewHolder)with payload information,[DefaultItemAnimator](https://developer.android.com/reference/androidx/recyclerview/widget/DefaultItemAnimator)now disables change animations.
    - You can now modify the[ItemTouchHelper](https://developer.android.com/reference/androidx/recyclerview/widget/ItemTouchHelper)escape velocity to control swipe sensitivity. To make it easier or harder to swipe, override`getSwipeEscapeVelocity(float defaultValue)`and modify`defaultValue`.

## Revision 23.1.1

#### November 2015

Changes for[v7 recyclerview library:](https://developer.android.com/topic/libraries/support-library/features#v7-recyclerview)
:
    - Fixed a crash that occurs when you perform a swipe-to-dismiss action that the`ItemTouchHelper`utility class provides, and then add an item. ([Issue 190500](http://b.android.com/190500))

Changes for[v7 preference library:](https://developer.android.com/topic/libraries/support-library/features#v7-preference)
:
    - Fixed an issue with ProGuard usage. ([Issue 183261](http://b.android.com/183261))

Changes for[v17 Leanback Support library:](https://developer.android.com/topic/libraries/support-library/features#v17-leanback)
:
    - Fixed a number of internal issues in this library.

Changes for[Design Support library:](https://developer.android.com/topic/libraries/support-library/features#design)
:
    - Added the`getHeaderView`method to the`NavigationView`class.
    - Fixed a transparent background issue for a`FloatingActionButton`object on devices running Android 4.0 (API level 15) and lower. ([Issue 183315](http://b.android.com/183315))

## Revision 23.1.0

#### October 2015

Changes for[v4 Support library:](https://developer.android.com/topic/libraries/support-library/features#v4)
:
    - Added`OnScrollChangedListener`interface support to the`NestedScrollView`widget. It allows you to receive callbacks when the scroll X or Y positions change.
    - Added a`MediaButtonReceiver`class to forward received playback controls to a service that's managing the`MediaSessionCompat`class. The`MediaSessionCompat`class has a constructor that can automatically find a media button receiver in the manifest. A media button receiver is a key part to[handling playback controls](https://developer.android.com/training/managing-audio/volume-playback.html#PlaybackControls)from hardware or bluetooth controls.

Changes for[v7 appcompat library:](https://developer.android.com/topic/libraries/support-library/features#v7-appcompat)
:
    - Added material design`Seekbar`and`ImageButton`widgets.
    - Updated the`ImageView`widget to support the tint feature.
    - Updated the look-and-feel of the`SwitchCompat`widget.

Changes for[v7 mediarouter library:](https://developer.android.com/topic/libraries/support-library/features#v7-mediarouter)
:
    - Added the following features to the`MediaRouteChooserDialog`class:
      - Displays a loading page while discovering media route providers.
      - Includes a device type icon for easier device identification.
      - Sorts the routes according to frequency of use in the current app.
      - Supports landscape mode.

    <!-- -->

    - Added the following features to the`MediaRouteControllerDialog`class:
      - Recognizes screen casting and provides a proper description.
      - Supports various album art sizes and aspect ratios, and loads the art asynchronously.
      - Automatically selects the content color based on the primary color of the app.
      - Adjusts the dialog layout based on available screen space on the device.
      - Supports landscape mode.

Changes for[v7 palette library:](https://developer.android.com/topic/libraries/support-library/features#v7-palette)
:
    - Added the`setRegion()`method to support extracting color from a specific region of a`Bitmap`object.

Changes for[v7 recyclerview library:](https://developer.android.com/topic/libraries/support-library/features#v7-recyclerview)
:
    - Added an improved animation API to the`ItemAnimator`class for better customizations:
      - Change animations no longer enforce two copies of the`ViewHolder`object, which enables item content animations. Also, the`ItemAnimator`object decides whether it wants to reuse the same`ViewHolder`object or create a new one.
      - The new information record API gives the`ItemAnimator`class the flexibility to collect data at the correct point in the layout lifecycle. This information is later passed into the animate callbacks.

    <!-- -->

    - Provided an easy transition plan for this backward-incompatible API change:
      - If you've previously extended the`ItemAnimator`class, you can change your base class to`SimpleItemAnimator`and your code should work as before. The`SimpleItemAnimator`class provides the old API by wrapping the new API.
      - Some methods were removed from the`ItemAnimator`class. The following code will no longer compile:  

      ### Kotlin

      ```kotlin
      recyclerView.itemAnimator.supportsChangeAnimations = false
      ```

      ### Java

      ```java
      recyclerView.getItemAnimator().setSupportsChangeAnimations(false)
      ```
      - You can replace it with:  

      ### Kotlin

      ```kotlin
      val animator: SimpleItemAnimator? = recyclerView.itemAnimator as? SimpleItemAnimator
      animator?.supportsChangeAnimations = false
      ```

      ### Java

      ```java
      ItemAnimator animator = recyclerView.getItemAnimator();
      if (animator instanceof SimpleItemAnimator) {
         ((SimpleItemAnimator) animator).setSupportsChangeAnimations(false);
      }
      ```

Changes for[v7](https://developer.android.com/topic/libraries/support-library/features#v7-preference),[v14](https://developer.android.com/topic/libraries/support-library/features#v14-preference), and[v17](https://developer.android.com/topic/libraries/support-library/features#v17-preference)Preference Support library:
:
    - Removed APIs for controlling`EditText`dialogs.

Changes for[v17 Leanback Support library:](https://developer.android.com/topic/libraries/support-library/features#v17-leanback)
:
    - Added a version of the`GuidedStepFragment`class for the Support library (extends`android.support.v4.app.Fragment`), and improved animations and transitions.
    - Updated the`GuidedStepFragment`class so it can be placed on top of existing content.
    - Added the ability to annotate different types of search completions to the`SearchFragment`class.
    - Added staggered slide transition support to the`VerticalGridFragment`class.

Changes for[Design Support library:](https://developer.android.com/topic/libraries/support-library/features#design)
:
    - Added[character counting](https://material.io/guidelines/components/text-fields.html#text-fields-character-counter)support to the`TextInputLayout`widget.
    - Added edge snapping support to the`AppBarLayout`class by adding the`SCROLL_FLAG_SNAP`constant. When scrolling ends, if the view is only partially visible, the view is snapped and scrolled to its closest edge.
    - Added support for custom views to the`NavigationView`class by using the`app:actionLayout`attribute or`MenuItemCompat.setActionView()`method.

Changes for[Custom Tabs Support library:](https://developer.android.com/topic/libraries/support-library/features#custom-tabs)
:
    - Added the`enableUrlBarHiding()`method to the`CustomTabsIntent`class. It lets the client customize whether the URL bar should be hidden automatically on scroll down.
    - Added the`setActionButton()`method to the`CustomTabsSession`class. It lets the client change the icon for a custom action button in an already launched custom tab.
    - Added the`TAB_SHOWN`and`TAB_HIDDEN`constants as new events for the`onNavigationEvent`method of the`CustomTabsCallback`class.

## Revision 23.0.1

#### September 2015

Changes for[v7](https://developer.android.com/topic/libraries/support-library/features#v7-preference)and[v14](https://developer.android.com/topic/libraries/support-library/features#v14-preference)Preference Support library:
:
    - Added the material design layout and style files. ([Issue 183376](http://b.android.com/183376))

Changes for[v7 appcompat library:](https://developer.android.com/topic/libraries/support-library/features#v7-appcompat)
:
    - Fixed crash issues for the[Fragment](https://developer.android.com/reference/android/app/Fragment)class by limiting the use of hardware layers to Android 4.1 (API level 16) and higher. ([Issue 183896](http://b.android.com/183896))
    - Fixed an issue where hardware buttons did not work when an activity had set the[Toolbar](https://developer.android.com/reference/android/widget/Toolbar)class to act as the[ActionBar](https://developer.android.com/reference/android/app/ActionBar)by using the`setSupportActionBar()`method. ([Issue 183334](http://b.android.com/183334))
    - Updated the[AppCompatDialogFragment](https://developer.android.com/reference/androidx/appcompat/app/AppCompatDialogFragment)class so it no longer throws the`Windows feature must be requested before adding content`error. ([Issue 183186](http://b.android.com/183186))

Changes for[Design Support library:](https://developer.android.com/topic/libraries/support-library/features#design)
:
    - Fixed the[AppBarLayout](https://developer.android.com/reference/com/google/android/material/appbar/AppBarLayout)class so it now draws correctly after rotation. ([Issue 183109](http://b.android.com/183109))
    - Fixed the[TabLayout](https://developer.android.com/reference/com/google/android/material/tabs/TabLayout)class so it now behaves correctly when a user clicks after a swipe. ([Issue 183123](http://b.android.com/183123))

Changes for[Custom Tabs Support library:](https://developer.android.com/topic/libraries/support-library/features#custom-tabs)
:
    - Lowered the[`minSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element)value from 16 to 15 for version support.
    - Added a way to generate a[CustomTabsSessionToken](https://developer.android.com/reference/androidx/browser/customtabs/CustomTabsSessionToken)from an intent.

## Revision 23

#### August 2015

Added new support libraries:
:
    - [Custom Tabs Support library](https://developer.android.com/topic/libraries/support-library/features#custom-tabs)
    - [Percent Support library](https://developer.android.com/topic/libraries/support-library/features#percent)
    - [App Recommendation Support library for TV](https://developer.android.com/topic/libraries/support-library/features#recommendation)
    - [v7 Preference Support library](https://developer.android.com/topic/libraries/support-library/features#v7-preference)
    - [v14 Preference Support library](https://developer.android.com/topic/libraries/support-library/features#v14-preference)
    - [v17 Preference Support library for TV](https://developer.android.com/topic/libraries/support-library/features#v17-preference)

For a complete list of the Support Library changes, see the[Support Library API Differences Report](https://developer.android.com/sdk/support_api_diff/23/changes).

## Revision 22.2.1

#### July 2015

Changes for[Design Support library:](https://developer.android.com/topic/libraries/support-library/features#design)
:
    - Added the`hide()`and`show()`methods to the[FloatingActionButton](https://developer.android.com/reference/com/google/android/material/floatingactionbutton/FloatingActionButton)class for programmatic triggering of animations.
    - Added the`LENGTH_INDEFINITE`constant to the[Snackbar](https://developer.android.com/reference/com/google/android/material/snackbar/Snackbar)class for showing a snackbar until it is dismissed or another snackbar is shown. Also, added the[setActionTextColor(int)](https://developer.android.com/reference/com/google/android/material/snackbar/Snackbar#setActionTextColor(int))and[setActionTextColor(ColorStateList)](https://developer.android.com/reference/com/google/android/material/snackbar/Snackbar#setActionTextColor(android.content.res.ColorStateList))methods.
    - Added the`getSelectedTabPosition()`method to the[TabLayout](https://developer.android.com/reference/com/google/android/material/tabs/TabLayout)class for retrieving the currently selected tab.
    - Provided a fully fluent API for the`android.support.v7.app.NotificationCompat.MediaStyle`class for method chaining.
    - Added convenience methods to the[RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView)for batch insertion of items.

For a complete list of the Support Library changes, see the[Support Library API Differences Report](https://developer.android.com/sdk/support_api_diff/22.2.0/changes).

## Revision 22.2.0

#### May 2015

Added[Design Support library:](https://developer.android.com/topic/libraries/support-library/features#design)
:
    - Added[TextInputLayout](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout)for showing[EditText](https://developer.android.com/reference/android/widget/EditText)hint and error text as floating labels.
    - Added[FloatingActionButton](https://developer.android.com/reference/com/google/android/material/floatingactionbutton/FloatingActionButton)for implementing a primary action on your interface as a floating action button, supporting either default or mini sizes.
    - Added[Snackbar](https://developer.android.com/reference/com/google/android/material/snackbar/Snackbar)for providing lightweight feedback with an optional action in an animated snackbar.
    - Added[TabLayout](https://developer.android.com/reference/com/google/android/material/tabs/TabLayout)for implementing fixed and scrollable[tabs](https://developer.android.com/design/building-blocks/tabs)as well as easy integration with[ViewPager](https://developer.android.com/reference/androidx/viewpager/widget/ViewPager).
    - Added[NavigationView](https://developer.android.com/reference/com/google/android/material/navigation/NavigationView)for implementing[navigation drawer](https://developer.android.com/design/patterns/navigation-drawer)contents, including the ability to inflate menu items via a[Menu Resource](https://developer.android.com/guide/topics/resources/menu-resource).
    - Added[CoordinatorLayout](https://developer.android.com/reference/androidx/coordinatorlayout/widget/CoordinatorLayout), a general purpose layout, used for building dependencies between sibling views and allowing easy scrolling reactions between components via[CoordinatorLayout.Behavior](https://developer.android.com/reference/androidx/coordinatorlayout/widget/CoordinatorLayout.Behavior). Many of the Design Library components rely on being a child of a[CoordinatorLayout](https://developer.android.com/reference/androidx/coordinatorlayout/widget/CoordinatorLayout).
    - Added[AppBarLayout](https://developer.android.com/reference/com/google/android/material/appbar/AppBarLayout), a container for a[Toolbar](https://developer.android.com/reference/android/widget/Toolbar)and other views (such as[TabLayout](https://developer.android.com/reference/com/google/android/material/tabs/TabLayout)) for reacting to scrolling events by scrolling off the screen, becoming visible in reaction to a downward scroll, or collapsing/uncollapsing before scrolling off/onto the screen.
    - Added[CollapsingToolbarLayout](https://developer.android.com/reference/com/google/android/material/appbar/CollapsingToolbarLayout)for controlling how a[Toolbar](https://developer.android.com/reference/android/widget/Toolbar)collapses. A toolbar may collapse by: pinning components to the top of the screen while it collapses, introducing parallax scrolling of components such as an[ImageView](https://developer.android.com/reference/android/widget/ImageView), or adding a content scrim color when the view is partially collapsed.

Changes for[v4 support library:](https://developer.android.com/topic/libraries/support-library/features#v4)
:
    - Added the[getContentChangeTypes()](https://developer.android.com/reference/androidx/core/view/accessibility/AccessibilityEventCompat#getContentChangeTypes(android.view.accessibility.AccessibilityEvent))and[setContentChangeTypes()](https://developer.android.com/reference/androidx/core/view/accessibility/AccessibilityEventCompat#setContentChangeTypes(android.view.accessibility.AccessibilityEvent, int))methods and related change type fields to the[AccessibilityEventCompat](https://developer.android.com/reference/androidx/core/view/accessibility/AccessibilityEventCompat)class for accessibility event handling.
    - Added the[getActiveQueueItemId()](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat#getActiveQueueItemId()),[getCustomActions()](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat#getCustomActions()), and[getExtras()](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat#getExtras())methods with related state fields to the[PlaybackStateCompat](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat)class for getting custom actions from the queue.
    - Added the[addCustomAction()](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat.Builder#addCustomAction(android.support.v4.media.session.PlaybackStateCompat.CustomAction)),[setActiveQueueItemId()](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat.Builder#setActiveQueueItemId(long)), and[setExtras()](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat.Builder#setExtras(android.os.Bundle))methods to the[PlaybackStateCompat.Builder](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat.Builder)class for adding custom actions to a playback state.
    - Added the[fromCustomAction()](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat.CustomAction#fromCustomAction(java.lang.Object))and[getCustomAction()](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat.CustomAction#getCustomAction())methods to the[PlaybackStateCompat.CustomAction](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat.CustomAction)class for getting custom actions from the queue.
    - Added the[isAttachedToWindow()](https://developer.android.com/reference/androidx/core/view/ViewCompat#isAttachedToWindow(android.view.View)),[offsetLeftAndRight()](https://developer.android.com/reference/androidx/core/view/ViewCompat#offsetLeftAndRight(android.view.View, int)), and[offsetTopAndBottom()](https://developer.android.com/reference/androidx/core/view/ViewCompat#offsetTopAndBottom(android.view.View, int))methods to the[ViewCompat](https://developer.android.com/reference/androidx/core/view/ViewCompat)class for working with views.
    - Added the[addOnPageChangeListener()](https://developer.android.com/reference/androidx/viewpager/widget/ViewPager#addOnPageChangeListener(android.support.v4.view.ViewPager.OnPageChangeListener)),[clearOnPageChangeListeners()](https://developer.android.com/reference/androidx/viewpager/widget/ViewPager#clearOnPageChangeListeners()), and[removeOnPageChangeListener()](https://developer.android.com/reference/androidx/viewpager/widget/ViewPager#removeOnPageChangeListener(android.support.v4.view.ViewPager.OnPageChangeListener))methods to the[ViewPager](https://developer.android.com/reference/androidx/viewpager/widget/ViewPager)class for responding to page changes.

      Deprecated the`ViewPager.setOnPageChangeListener()`method.
    - Added the[notifySubtreeAccessibilityStateChanged()](https://developer.android.com/reference/androidx/core/view/ViewParentCompat#notifySubtreeAccessibilityStateChanged(android.view.ViewParent, android.view.View, android.view.View, int))method to the[ViewParentCompat](https://developer.android.com/reference/androidx/core/view/ViewParentCompat)class for notifying a view parent that the accessibility state of one of its descendants has changed.
    - Added the[translationZ()](https://developer.android.com/reference/androidx/core/view/ViewPropertyAnimatorCompat#translationZ(float)),[translationZBy()](https://developer.android.com/reference/androidx/core/view/ViewPropertyAnimatorCompat#translationZBy(float)),[z()](https://developer.android.com/reference/androidx/core/view/ViewPropertyAnimatorCompat#z(float)), and[zBy()](https://developer.android.com/reference/androidx/core/view/ViewPropertyAnimatorCompat#zBy(float))methods to the[ViewPropertyAnimatorCompat](https://developer.android.com/reference/androidx/core/view/ViewPropertyAnimatorCompat)class for adding animation.

Changes for[v7 appcompat library](https://developer.android.com/topic/libraries/support-library/features#v7-appcompat):
:
    - Added the[onWindowStartingSupportActionMode()](https://developer.android.com/reference/androidx/appcompat/app/AppCompatActivity#onWindowStartingSupportActionMode(android.support.v7.view.ActionMode.Callback))method to the[AppCompatActivity](https://developer.android.com/reference/androidx/appcompat/app/AppCompatActivity),[AppCompatCallback](https://developer.android.com/reference/androidx/appcompat/app/AppCompatCallback), and[AppCompatDialog](https://developer.android.com/reference/androidx/appcompat/app/AppCompatDialog)classes for handling action modes started from the current window.
    - Added the[isHandleNativeActionModesEnabled()](https://developer.android.com/reference/androidx/appcompat/app/AppCompatDelegate#isHandleNativeActionModesEnabled())and[setHandleNativeActionModesEnabled()](https://developer.android.com/reference/androidx/appcompat/app/AppCompatDelegate#setHandleNativeActionModesEnabled(boolean))methods to the[AppCompatDelegate](https://developer.android.com/reference/androidx/appcompat/app/AppCompatDelegate)class for handling native action modes.

## Revision 22.1.0

#### April 2015