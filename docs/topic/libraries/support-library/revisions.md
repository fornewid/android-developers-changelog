---
title: https://developer.android.com/topic/libraries/support-library/revisions
url: https://developer.android.com/topic/libraries/support-library/revisions
source: md.txt
---

# Recent Support Library Revisions

This page provides details about the most recent Support Library package releases. For earlier releases, see the[Support Library Revisions Archive](https://developer.android.com/topic/libraries/support-library/rev-archive).

## Revision 28.0.0 Production

#### (September 21, 2018)

This is the stable release of Support Library 28.0.0 and is suitable for use in production. This will be the last feature release under the`android.support`packaging, and developers are encouraged to migrate to[AndroidX](https://developer.android.com/jetpack/androidx).

### New features

- `AnimatedStateListDrawableCompat`provides animated transitions between drawable states.
- [`VectorDrawableCompat`](https://developer.android.com/reference/androidx/vectordrawable/graphics/drawable/VectorDrawableCompat)gains support for gradient and[`ColorStateList`](https://developer.android.com/reference/android/content/res/ColorStateList)fills and strokes.

## Revision 28.0.0 RC 2

#### (August 27, 2018)

This release candidate of the support library is considered feature-complete and its public API surface is stable. This release will be shipped as final stable version barring any critical issues that may arise. This release should be safe to use in production. Please report any issues to the[public issue tracker](https://source.android.com/setup/contribute/report-bugs).

### Fixed issues

- Proguard removes View Model Application constructor (public issue[112230489](https://issuetracker.google.com/issues/112230489))
- Fixed \`AnimatedStateListDrawableCompat\` constant state
- Removed media2 dependency from mediarouter 1.0.0
- \`Fragment.getViewLifecycleOwner()\` does not get stopped when hitting the home button (public issue[113070421](https://issuetracker.google.com/issues/113070421)) (\[public issue 113070421\](https://issuetracker.google.com/issues/113070421))

## Revision 28.0.0 RC 1

#### (August 6, 2018)

This release candidate of the support library is considered feature-complete and its public API surface is stable. This release will be shipped as final stable version barring any critical issues that may arise. This release should be safe to use in production. Please report any issues to the[public issue tracker](https://source.android.com/setup/contribute/report-bugs).

**Note:**Some libraries, such as media2, have remained in alpha stage as their API surfaces are not yet finalized. We do not recommend using alpha libraries in production. Libraries should strictly avoid depending on alpha libraries in production, as their API surfaces may change in source- and binary-incompatible ways.

### Fixed issues

- BottomNavigationView menu is not initialized correctly in design support library
- PositionalDataSource doesn't correctly handle pre-pended item inserts into the database
- Sliders are janky and not responsive
- \`SlicesProviderCompat.getPinnedSpecs()\` doesn't add user IDs to URIs
- RoutePlayer2: remote playback does not switch back to local playback
- Cached slice parsing is crashing on actions
- Google Search app crash in rendering static Slice
- ConcurrentModificationException in RecyclerView selection library when data set changed with removing selection
- PreferenceThemeOverlay has been updated to the latest material theme. If no custom theme is provided, PreferenceThemeOverlay is used as the default theme.
- PreferenceThemeOverlay.v14 and PreferenceThemeOverlay.v14.Material themes have been deprecated in favour of PreferenceThemeOverlay.
- PreferenceGroup visibility is now tied to its children - hiding a parent group will also prevent its children from being shown in the hierarchy. Use Preference.isShown() to get whether a Preference is actually displayed to the user in the hierarchy.
- Preference.onSetInitialValue(boolean, Object) has been deprecated and replaced with onSetInitialValue(Object). PreferenceDataStore now also correctly restores default values.

## Revision 28.0.0 Beta 1

#### (July 2018)

This beta release of the Support Library is considered feature-complete and its public API surface is stable, barring any critical issues that may arise. While this release is safe to use in production, it may still contain bugs. Please report any issues to the[public issue tracker](https://source.android.com/setup/contribute/report-bugs).

### Fixed issues

- GestureSelectionHelper eating events on non-selectable items
- Slider slices can have duplicated thumb icon when slider value is being updated
- IconCompat broke TYPE_URI icons
- Crash with Preferences using Seekbar
- Crash in Slice.toString()
- OffsettingListUpdateCallback.onMoved() calls mCallback.onRemoved() instead of mCallback.onMoved() (Issue[110711937](https://issuetracker.google.com/issues/110711937))

## Revision 27.1.1

#### (April 2018)

### Fixed issues

- AsyncListDiffer doesn't call getChangePayload (AOSP issue[73961809](https://issuetracker.google.com/issues/73961809))
- Fragment ViewModel's onCleared not called (AOSP issue[74139250](https://issuetracker.google.com/issues/74139250))
- RecyclerView.setRecycledViewPool() increases attachCount even when adapter is null
- RecyclerView NPE if SmoothScroller.onStop calling stop() or startSmoothScroller()
- Fragment Replacement transaction causes previous fragment to flicker after new fragment is shown (AOSP issue[74051124](https://issuetracker.google.com/issues/74051124))
- Loader callback breaking change in 27.1.0 (AOSP issue[74135998](https://issuetracker.google.com/issues/74135998))
- RTL layout does not work when the vertical grid view set column \>1
- onLoadFinished called multiple times in ViewPager with FragmentPagerAdapter
- AsyncListDiffer should dispatch updates after setting current list (AOSP issue[74003309](https://issuetracker.google.com/issues/74003309))
- ShareActionProvider throws ClassCastException in 27.1.0
- Fragment lifecycle change with ViewPager (AOSP issue[73976255](https://issuetracker.google.com/issues/73976255))

## Revision 28.0.0 Alpha 1

#### (March 2018)

**Note:**28.0.0-alpha1 is a pre-release version to support the Android P developer preview. Its API surface is subject to change, and it does not necessarily include features or bug fixes from the latest stable versions of Support Library.

### Important changes

- As previously noted in the[Android KTX announcement](https://android-developers.googleblog.com/2018/02/introducing-android-ktx-even-sweeter.html), we are continuing to adopt the`androidx`package prefix across our libraries. A selection of brand-new libraries, including`heifwriter`and`recyclerview-selection`, are starting out in this new package. We hope the division between`android.*`and`androidx.*`makes it more obvious which APIs are bundled with the platform, and which are static libraries for app developers that work across different versions of Android.
- We have split parts of support-core-ui, support-core-utils, and support-compat into smaller libraries. This change will help us detangle support library dependencies in the future. We now have the following new libraries:
  - asynclayoutinflater (from support-core-ui)
  - collections (from support-compat)
  - coordinatorlayout (from design)
  - cursoradapter (from support-core-ui)
  - customview (from support-core-ui)
  - documentfile (from support-core-utils)
  - drawerlayout (from support-core-ui)
  - interpolator (from support-core-ui)
  - loader (from support-fragments and core-utils)
  - localbroadcastmanager (from support-core-utils)
  - print (from support-core-utils)
  - slidingpanelayout (from support-core-ui)
  - swiperefreshlayout (from support-core-ui)
  - viewpager (from support-core-ui)

### New APIs

- [`recyclerview-selection`](https://developer.android.com/reference/androidx/recyclerview/selection/package-summary)provides item selection support for[`RecyclerView`](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView). The package provides:
  - Support for creating, modifying, inspecting, and monitoring changes to a set of selected items in a RecyclerView list.
  - Support for intuitive multi-selection actions:
    - Touch-driven selection allows users to select ranges of items with an intuitive long-press-and-drag gesture.
    - Mouse-driven band selection allows users to a select block of items in a RecyclerView list using traditional mouse pointer band/lasso actions.
  - Support for touch-centric devices, including phone and touch-enabled laptop form-factors, as well as pointer-centric devices.
- HEIF Writer provides support for writing HEIF-format still images.
- Design Library
  - We've introduced a new application theme,`Theme.MaterialComponents`, with new attributes and updated styles for components.
  - We've added the following components:
    - BottomAppBar
    - Chip
    - ChipGroup
    - MaterialButton
    - MaterialCardView
- *Slices* provides a framework for apps to embed templated content from other apps.
  - slices-builders contains methods to build content in a template format.
  - slices-view contain methods to present that content.
- *Browser actions*provides a protocol for app developers to launch a consistent (but customizable) context menu for URLs. This feature is dependent on the presence of a browser app (such as Chrome, where this feature is still under development) that implements support for browser actions.
- [`ContextCompat.getSystemService()`](https://developer.android.com/reference/androidx/core/content/ContextCompat#getSystemService(android.content.Context, java.lang.Class<T>))and[`getSystemServiceName()`](https://developer.android.com/reference/androidx/core/content/ContextCompat#getSystemServiceName(android.content.Context, java.lang.Class<?>))allow system service lookups by type on all API levels.

### Bug fixes

- Fragment ViewModel's onCleared not called (AOSP issue[74139250](https://issuetracker.google.com/issues/74139250))
- onLoadFinished() called multiple times in ViewPager with FragmentPagerAdapter (AOSP issue[74182171](https://issuetracker.google.com/issues/74182171))
- RecyclerView's LinearLayoutManager's smoothScrollToPosition() displays erratic (back and forth) movement under certain circumstances (AOSP issue[71567765](https://issuetracker.google.com/issues/71567765))

## Revision 27.1.0 Release

#### (February 2018)

### Important Changes

- The underlying implementation of[Loaders](https://developer.android.com/guide/components/loaders)has been rewritten to use[Lifecycle](https://developer.android.com/topic/libraries/architecture/lifecycle). While the API remains unchanged, there are a number of behavior changes:
  - `initLoader()`,`restartLoader()`, and`destroyLoader()`can now only be called on the main thread.
  - A Loader's`onStartLoading()`and`onStopLoading()`are now called when the containing FragmentActivity/Fragment is started and stopped, respectively.
  - `onLoadFinished()`will only be called between`onStart()`and`onStop`. As a result, Fragment transactions can now safely be done in`onLoadFinished()`.
  - The FragmentController methods related to Loaders are now deprecated.
- DialogFragment's`getDialog()`will now be non-null up until`onDestroyView()`, instead of becoming null in`dismiss()`. You can now determine if the Dialog was manually dismissed in`onStop()`by checking if`getDialog().isShowing()`returns false.

### New APIs

- [`ListAdapter`](https://developer.android.com/reference/androidx/recyclerview/widget/ListAdapter)for`RecyclerView`(along with[`AsyncListDiffer`](https://developer.android.com/reference/androidx/recyclerview/widget/AsyncListDiffer)) make it easier to compute list diffs on a background thread. These can help your RecyclerView animate content changes automatically, with minimal work on the UI thread. They use[`DiffUtil`](https://developer.android.com/reference/androidx/recyclerview/widget/DiffUtil)under the hood.
- `SortedList.ReplaceAll`enables updating all data in a SortedList, which runs all appropriate animations for inserts, removals, changes, and moves (moves are treated as removals and inserts).
- FragmentActivity and Fragment now implement[`ViewModelStoreOwner`](https://developer.android.com/reference/androidx/lifecycle/ViewModelStoreOwner)and can now be used with the[`ViewModelProvider`](https://developer.android.com/reference/androidx/lifecycle/ViewModelProvider)constructors as an alternative to using`ViewModelProviders.of()`
- Fragments now have`requireContext()`,`requireActivity()`,`requireHost()`, and`requireFragmentManager()`methods, which return a`NonNull`object of the equivalent get methods or throw an`IllegalStateException`.
- `requireViewById()`, a`@NonNull`compat version of`findViewById()`has been added to`WindowCompat`,`ActivityCompat`, and`ViewCompat`, which throw an`IllegalArgumentException`when the target cannot be found.
- [`LoaderCallbacks`](https://developer.android.com/reference/androidx/loader/app/LoaderManager.LoaderCallbacks)methods now have the appropriate`@Nullable`and`@NonNull`annotations.
- [`FileProvider`](https://developer.android.com/reference/androidx/core/content/FileProvider)now supports[`getExternalMediaDirs()`](https://developer.android.com/reference/android/content/Context#getExternalMediaDirs())on API 21 and higher devices via the new`<external-media-path>`element.

### Bug fixes

- Fragment that initializes Loader in onCreate has broken lifecycle inside ViewPager
- LoaderManager throws IllegalStateException in onLoadFinished
- LoaderViewModel does not clear its Loaders in onCleared
- Class file for android.arch.lifecycle.ViewModelStoreOwner not found
- DialogFragment onDismiss not called immediately after dismiss()
- Country flag emoji don't work on release keys devices when using downloadable fonts
- Preferences library uses attributes that will not work on old versions of Android
- MediaCompat's testlib artifact types are incorrectly documented (AOSP issue[71559905](https://issuetracker.google.com/issues/71559905))
- Google Sans crash in TypefaceCompatUtil
- Expose ArraySet constructor that takes in Collection.
- updateApi removes .ignore files that should be preserved
- redundant MainFragments created in BrowseFragment
- Remove use of reflection from CarRecyclerView
- java.lang.IllegalStateException at FragmentManagerImpl.checkStateLoss
- Got (undocumented) java.lang.SecurityException when using android.support.v4.content.PermissionChecker.checkSelfPermission
- RecyclerView IndexOutOfBoundsException because State.mPreviousLayoutItemCount not cleared in setAdapter (AOSP issue[37657125](https://issuetracker.google.com/issues/37657125))
- Fragment that initializes Loader in onCreate has broken lifecycle inside ViewPager (AOSP issue[34831613](https://issuetracker.google.com/issues/34831613))
- FragmentManagerImpl.execSingleAction crashes

## Revision 27.0.2 Release

#### (November 2017)

### Bug fixes

- `EmojiEditTextHelper`throws`NullPointerException`.
- `IllegalStateException`: Fragment has not been attached yet.
- Unable to dismiss 'Cast' icon pop-up by tapping anywhere on the screen.
- `MediaMetadataCompat`throws`BadParcelableException`.

## Revision 27.0.1 Release

#### (November 2017)

### Bug fixes

- LifecycleRegistry is in the wrong state after[`startActivityForResult()`](https://developer.android.com/reference/androidx/core/app/ActivityCompat#startActivityForResult(android.app.Activity, android.content.Intent, int, android.os.Bundle))is called. (Issue[65665621](https://issuetracker.google.com/65665621))
- The color of disabled buttons is too light on older API levels.
- After a user scrolls, they cannot click on an item in a[`RecyclerView`.](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView)(AOSP issue[66996774](https://issuetracker.google.com/66996774))
- In[Talkback](https://support.google.com/accessibility/android/answer/6283677), clicking on more options does not cause the system to announce the new popup or to add focus to the new options.

## Revision 27.0.0 Release

#### (October 2017)

### API Diffs

- [26.1 → 27.0.0 Differences Report](https://developer.android.com/sdk/support_api_diff/27.0.0/changes)

### API Changes

- Nullability annotations were added to a variety of APIs, including the following:
  - [`Fragment.getActivity()`](https://developer.android.com/reference/androidx/fragment/app/Fragment#getactivity)
  - [`Fragment.getContext()`](https://developer.android.com/reference/androidx/fragment/app/Fragment#getcontext)
  This can cause Kotlin compilation errors when the nullable return types aren't properly handled.
- `Fragment`can use support library versions of`Transition`for fragment transitions, including shared-element transitions.
- Content paging library ([`android.support.content.ContentPager`](https://developer.android.com/reference/androidx/contentpager/content/ContentPager)) provides support for paging content exposed via a[ContentProvider](https://developer.android.com/reference/android/content/ContentProvider). Use of this library allows a client to avoid expensive interprocess "cursor window swaps" on the UI thread, providing a compatibility library for the Android 8.0 feature.
- `ViewCompat`now adds wrappers for autofill methods, including`getImportantForAutofill()`,`isImportantForAutofill()`,`setAutofillHints()`, and`setImportantForAutofill()`.
- [Leanback](https://developer.android.com/reference/android/support/v17/leanback/package-summary)gets new features and polish, and loses some deprecated classes, such as:
  - [`
    Picker`](https://developer.android.com/reference/androidx/leanback/widget/picker/Picker)now can use different separators between each column using the[`setSeparators()`](https://developer.android.com/reference/androidx/leanback/widget/picker/Picker#setSeparators(java.util.List%3Cjava.lang.CharSequence%3E))method.
  - [`
    DiffCallback`](https://developer.android.com/reference/androidx/leanback/widget/DiffCallback)has been added to allow`ArrayObjectAdapter`to take advantage of the output provided by`DiffUtil`.
  - Infrastructure added to support media players with variable controls, adding optional controls for fast-forward, repeat, shuffle, next, previous, and rewind.
  - Removal of`MediaControllerGlue`, PlaybackControlGlue,`PlaybackControlSupportGlue`, and`PlaybackOverlayFragment`.
- For testing, the PollingCheck utility is ported from AOSP CTS. It polls for a condition to happen within a timeout window.
- Infrastructure added to support runtime permissions on Instant Apps for Android 5.0, using`PermissionCompatDelegate`.
- Trusted custom tabs now supported, along with the ability to define a relationship between an application and an origin URI.
- Android Wear ambient mode support is simplified with the use of the AmbientMode headless fragment, which also makes supporting ambient mode compatible with the use of Architecture Components.

<!-- -->

- The Wear team seeks developer feedback around this significant change. For more information, see the[Android Wear Release Notes](https://developer.android.com/wear/releases).

<!-- -->

- Some deprecated classes removed as we move away from old pre-V14 APIs, such as`android.support.v7.NotificationCompat`(use v4[NotificationCompat](https://developer.android.com/reference/androidx/core/app/NotificationCompat)instead),`KeyEventCompat`,`ParallelExecutorCompat`, and`
  SearchViewCompat`.
- Migrated wear manifest metadata constants are all now available via[`
  android.support.wear.utils.MetadataConstants`](https://developer.android.com/reference/androidx/wear/utils/MetadataConstants).
- Ambient mode support is now available for all Activities, not just WearableActivity. For more information, see the[`AmbientMode`](https://developer.android.com/reference/androidx/wear/ambient/AmbientMode)reference.
- [RoundedDrawable](https://developer.android.com/reference/androidx/wear/widget/RoundedDrawable)now supports XML inflation.

### Bug fixes

- Application crashes with support library 27 and downloadable font
- Downloadable fonts not working for new projects created after updating SDK
- SpeechRecognizer API is broken in latest upgrade
- Fragment-related crash during draw after removing animated View
- support-leanback-demos media playback are all broken
- Android Support Library is adding \<meta-data\> into manifest
- FontResourcesParserCompat should understand android: attrs
- Leanback Glue does not support Pause input key
- Unresolved symbol in IDE when multiple packages share the same artifact id.
- Null Pointer Exception in CarExtender
- Wrong shuffle / repeat mode set PlaybackState after creating MediaController
- Library cluster default posters are running onto next cluster while navigating
- Recommendation card metadata is cut off
- IllegalArgumentException at RecyclerView.attachViewToParent()
- ClassNotFoundException when unmarshalling SavedState (AOSP issue[37133281](https://issuetracker.google.com/issues/37133281))
- Focus gets stuck in RecyclerView
- Fix ANR in Leanback LayoutManager

## Revision 26.1.0 Release

#### (September 2017)

This is a special release to integrate the Support Library with[Lifecycles](https://developer.android.com/topic/libraries/architecture/lifecycle)from[Architecture Components](https://developer.android.com/topic/libraries/architecture). If you are not using the Lifecycles library, you don't need to update from 26.0.2. For more information, see the[Architecture Components release notes](https://developer.android.com/topic/libraries/architecture/release-notes).

### Important changes

- [Fragment](https://developer.android.com/reference/androidx/fragment/app/Fragment)and[FragmentActivity](https://developer.android.com/reference/androidx/fragment/app/FragmentActivity)(the base class for[AppCompatActivity](https://developer.android.com/reference/androidx/appcompat/app/AppCompatActivity)) now implement the[`LifecycleOwner`](https://developer.android.com/reference/androidx/lifecycle/LifecycleOwner)interface from[Architecture Components](https://developer.android.com/topic/libraries/architecture).

## Revision 26.0.2 Release

#### (August 2017)

### Bug fixes

- Menu icons are flattened on Support Library 26.0.0
- `GuidedAction.multilineDescription`doesn't work properly with Leanback

## Revision 26.0.1 Release

#### (August 2017)

### Bug fixes

- FontCompat 26.0.0 crashes on O-MR1 devices
- 26.0.0 Design Support Library should not include multidex support (issue[63999442](https://issuetracker.google.com/issues/63999442)))
- AppBarLayout now has 300px of left padding since 26.0.0
- PlaybackTransportControl navigation is broken
- Fragment.onCreateView is called sometime before onCreate finishes
- android.os.BadParcelableException: ClassNotFoundException when unmarshalling: android.support.v4.media.MediaMetadataCompat

## Revision 26.0.0 Release

#### (July 2017)

**Important:** The support libraries are now available through Google's Maven repository. You do not need to download the support repository from the SDK Manager. For more information, see[Support Library Setup](https://developer.android.com/topic/libraries/support-library/setup).

### Important changes

- The minimum SDK version has been increased to 14. As a result, many APIs that existed only for compatibility with pre-14 API levels have been deprecated. Clients of these APIs should migrate to their framework equivalents as noted in the reference page for each deprecated API.
- The Wear UI Library contains classes that help you implement patterns and layouts that work on Wear devices. For more information, see[Using the Wear UI Library](https://developer.android.com/training/wearables/ui/wear-ui-library).
- The[Percent Support module](https://developer.android.com/topic/libraries/support-library/packages#percent)has been deprecated. Clients of this module should migrate to the new[`ConstraintLayout`](https://developer.android.com/reference/androidx/constraintlayout/widget/ConstraintLayout)widget, which is provided as a separate artifact in SDK Manager.
- `android.support.v7.app.NotificationCompat`and its containing classes has been deprecated and will be removed in a future release:
  - Use[NotificationCompat.Builder](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder)instead of`v7.app.NotificationCompat.Builder`. Functionality that previously relied on using the v7 AppCompat Builder has now been folded into the v4 Compat Builder.
  - `DecoratedCustomViewStyle`has moved to the[`android.support.v4.app`](https://developer.android.com/reference/android/support/v4/app/package-summary)package.
  - `MediaStyle`and`DecoratedMediaCustomViewStyle`are now part of the[media-compat library](https://developer.android.com/topic/libraries/support-library/packages#v4-media-compat)and can be found in the[android.support.v4.media.app](https://developer.android.com/reference/android/support/v4/media/app/package-summary)package.

### New APIs

- New`fastScrollEnabled`boolean flag for[RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView). If enabled,`fastScrollHorizontalThumbDrawable`,`fastScrollHorizontalTrackDrawable`,`fastScrollVerticalThumbDrawable`, and`fastScrollVerticalTrackDrawable`must be set.

### API Diffs

- [26.0.0-beta2 → 26.0.0 Release](https://developer.android.com/sdk/support_api_diff/26.0.0-incr/changes)
- [25.4.0 → 26.0.0 Release](https://developer.android.com/sdk/support_api_diff/26.0.0/changes)

### Bug fixes

- Infinite loop in RecyclerView.toString()
- ResourceNotFoundException running Kotlin project on API 16 AVD after upgrading to Canary 6
- java.lang.AssertionError in design view with support library 26.0.0-beta2
- Android Studio layout preview broken for Support Library widgets
- Preference.setSingleLineTitle() is ignored if the Preference was not created with attributes
- DAC "Since" annotations are wrong for 25.3.0 / 25.4.0 revisions of Support Library
- ResourcesCompat.getFont() throws exception
- Toolbar title not in bold font
- Auto sizing with maxLines produces unexpected results
- NullPointerException in TextView.checkForRelayout()
- AppCompatTextViewAutoSizeHelper.setRawTextSize() calls requestLayout() during layout
- EmojiAppCompatTextView crashes
- Autosize TextView does not adjust automatically when text is changed
- Screen corruption in Instacart
- UnsupportedOperationException in MenuItemCompat
- NotificationCompat doesn't fully extract actions on API 24 or higher
- CoordinatorLayout anchoring problems on layout updates