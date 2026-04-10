---
title: https://developer.android.com/jetpack/androidx/releases/viewpager2
url: https://developer.android.com/jetpack/androidx/releases/viewpager2
source: md.txt
---

# ViewPager2

# ViewPager2

[User Guide](https://developer.android.com/guide/navigation/navigation-swipe-view-2)[Code Sample](https://github.com/android/views-widgets-samples/tree/main/ViewPager2)  
API Reference  
[androidx.viewpager.adapter](https://developer.android.com/reference/kotlin/androidx/viewpager2/adapter/package-summary)  
[androidx.viewpager.widget](https://developer.android.com/reference/kotlin/androidx/viewpager2/widget/package-summary)  
Display Views or Fragments in a swipeable format.  

| Latest Update |                                  Stable Release                                   | Release Candidate | Beta Release | Alpha Release |
|---------------|-----------------------------------------------------------------------------------|-------------------|--------------|---------------|
| May 14, 2024  | [1.1.0](https://developer.android.com/jetpack/androidx/releases/viewpager2#1.1.0) | -                 | -            | -             |

## AndroidX Dependencies

To use`ViewPager2`, add the following AndroidX dependency to your project's`build.gradle`file:  

### Groovy

```groovy
dependencies {
    implementation "androidx.viewpager2:viewpager2:1.1.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.viewpager2:viewpager2:1.1.0")
}
```

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:561920+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=561920&template=1422419)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.1.0

### Version 1.1.0

May 14, 2024

`androidx.viewpager2:viewpager2:1.1.0`is released. Version 1.1.0 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/e65db83eb3a66072d236d5e1af59ecdf69f02d26..8c2fe519f8f6a06207ee73a1d02f62121479a59a/viewpager2/viewpager2).

**Important changes since 1.0.0**

- Fixes crashes when used with[RecyclerView`1.3.1-rc01`](https://developer.android.com/jetpack/androidx/releases/recyclerview#recyclerview-1.3.1-rc01)or higher.
- `ViewPager2`now correctly populates the`CollectionInfo`and`CollectionItemInfo`that[RecyclerView`1.2.0-alpha02`](https://developer.android.com/jetpack/androidx/releases/recyclerview#recyclerview-1.2.0-alpha02)and higher no longer populate by default.
- Added`FragmentTransactionCallback`interface for listening to fragment lifecycle changes that happen inside`FragmentStateAdapter`.
- Fixed`FragmentStateAdapter`issue with initial fragment menu visibility when adding a fragment to the`FragmentManager`.
- Fixed dispatch of window insets: all pages now get the same insets. Due to how`WindowInsets`are dispatched on old API versions (\< API 30) that can prevent insets from being available to sibling views, you must opt into this fix via`WindowInsetsApplier.install(viewPager2)`if you want to apply insets on \< API 30 devices.

### Version 1.1.0-rc01

May 1, 2024

`androidx.viewpager2:viewpager2:1.1.0-rc01`is released with no notable changes since 1.1.0-beta02. Version 1.1.0-rc01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/c5bf9bc40dd5d9f0b3f34e7273ac0d4e4f05c41d..e65db83eb3a66072d236d5e1af59ecdf69f02d26/viewpager2/viewpager2).

### Version 1.1.0-beta02

May 24, 2023

`androidx.viewpager2:viewpager2:1.1.0-beta02`is released.[Version 1.1.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d725303accfa9be6d5c3d61c7603ed1b9a780cbd..c5bf9bc40dd5d9f0b3f34e7273ac0d4e4f05c41d/viewpager2/viewpager2)

**API Changes**

- Added Fragment state saving callbacks to`FragmentTransactionCallback`. ([I45b90](https://android-review.googlesource.com/#/q/I45b908759508e431003a192b0bc3bdcf72713a2a))
- `ViewPager2`now no longer tries to fix the broken`WindowInsets`dispatch of old API versions (\< 30), because the fix itself can be harmful to siblings of`ViewPager2`. The fix is still available, but has become an opt-in so developers can decide on a case by case basis. Enable the fix by calling`WindowInsetsApplier.install(viewPager2))`. ([Ic9a85](https://android-review.googlesource.com/#/q/Ic9a85e4d20c35192b783a9436a6f92acec369524))

**Bug Fixes**

- Fix compatibility issues with newer versions of`RecyclerView`. Users of this version of`ViewPager2`should update to at least`RecyclerView`1.3.1-rc01.

### Version 1.1.0-beta01

August 4, 2021

`androidx.viewpager2:viewpager2:1.1.0-beta01`is released.[Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6c98d66b901be2eecdf89477ccd70d2490ca6fc2..d725303accfa9be6d5c3d61c7603ed1b9a780cbd/viewpager2/viewpager2)

**API Changes**

- Upgrade androidx to use Kotlin 1.4 ([Id6471](https://android-review.googlesource.com/#/q/Id647100407925c16d734c8c43392b4e2d108d0e3),[b/165307851](https://issuetracker.google.com/issues/165307851),[b/165300826](https://issuetracker.google.com/issues/165300826))

- Move to targeting Java 8 for all androidx libraries ([2923f39](https://android-review.googlesource.com/#/q/2923f39afb2f019e043f3a8e1d409fa49d90808e))

**Bug Fixes**

- Fixed dispatch of window insets, all pages now get the same insets. ([I47fef](https://android-review.googlesource.com/#/q/I47fef39b5fca4a936c8428b741097974b56a518c))

### Version 1.1.0-alpha01

April 1, 2020

`androidx.viewpager2:viewpager2:1.1.0-alpha01`is released.[Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c4c5f5340c2250ff0b4709448ca82abc915ef6b4..6c98d66b901be2eecdf89477ccd70d2490ca6fc2/viewpager2/viewpager2)

This release accompanies a change in[RecyclerView 1.2.0-alpha02](https://developer.android.com/jetpack/androidx/releases/recyclerview#recyclerview-1.2.0-alpha02)by populating`CollectionInfo`and`CollectionItemInfo`that`RecyclerView`no longer provides by default. When updating to`RecyclerView 1.2.0-alpha02`also update`ViewPager2`to prevent Accessibility regressions.

**New Features**

- Added`FragmentTransactionCallback`interface for listening to fragment lifecycle changes that happen inside`FragmentStateAdapter`. ([Ibda77](https://android-review.googlesource.com/#/q/Ibda7755413ee86f0257b2464a8027187f134ab6e))

**Bug Fixes**

- Fixed`FragmentStateAdapter`issue with initial fragment menu visibility when adding a fragment to the`FragmentManager`. ([I9d2ff](https://android-review.googlesource.com/#/q/I9d2ffa0efcb03b63eeca25f2d4e74c81446a5774),[b/144442240](https://issuetracker.google.com/issues/144442240))

## Version 1.0.0

### Version 1.0.0

November 20, 2019

`androidx.viewpager2:viewpager2:1.0.0`is released with no changes from 1.0.0-rc01.[Version 1.0.0 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/743e7f1c517cfe59c2e2e4149c655888670508d4..c4c5f5340c2250ff0b4709448ca82abc915ef6b4/viewpager2).

**Major features of 1.0.0**

- Improvements from the previous[ViewPager](https://developer.android.com/reference/androidx/viewpager/widget/ViewPager)implementation:
  - RTL (right-to-left) layout support
  - Vertical orientation support
  - Reliable`Fragment`support (including handling changes to the underlying`Fragment`collection)
  - Dataset change animations (including`DiffUtil`support)
- Easy migration from the previous`ViewPager`implementation (API parity where possible). See the[migration guide](https://developer.android.com/training/animation/vp2-migration)and the[sample app](http://goo.gle/viewpager2-sample).

See the[guide](https://developer.android.com/training/animation/screen-slide-2)on using ViewPager2 to slide between Fragments.

### Version 1.0.0-rc01

October 23, 2019

`androidx.viewpager2:viewpager2:1.0.0-rc01`is released with no changes since`1.0.0-beta05`.[Version 1.0.0-rc01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/cb65a71c76ace87c2046f2212ca9031d44cbb256..743e7f1c517cfe59c2e2e4149c655888670508d4/viewpager2).

### Version 1.0.0-beta05

October 9, 2019

`androidx.viewpager2:viewpager2:1.0.0-beta05`is released.[Version 1.0.0-beta05 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/7166ba571d594baa9016e02c3b5fe967da0b8ec0..cb65a71c76ace87c2046f2212ca9031d44cbb256/viewpager2).

**Bug fixes**

- Fix for`requestFocus`on an off-screen page causing a page change. The behaviour is now consistent with the original ViewPager. ([b/140656866](https://issuetracker.google.com/issues/140656866))
- Fix for`focus`remaining on an off-screen page after a page change. Focus is now cleared when changing the page. ([b/140656866](https://issuetracker.google.com/issues/140656866))
- Fix for ordering of`Fragment`pause / resume transactions when changing the page (we now always pause the old primary item before resuming the new one). ([b/139489059](https://issuetracker.google.com/issues/139489059))
- Fix for`canScrollHorizontally(int)`and`canScrollVertically(int)`- they now return whether ViewPager2 can scroll in the given direction. ([b/141848404](https://issuetracker.google.com/issues/141848404))
- An issue in[SwipeRefreshLayout](https://developer.android.com/jetpack/androidx/releases/swiperefreshlayout#1.1.0-alpha03)was fixed to work better with ViewPager2.

### Version 1.0.0-beta04

September 5, 2019

`androidx.viewpager2:viewpager2:1.0.0-beta04`is released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/f3df487541c41b9b0e81199a73eaeda058cab7a9..7166ba571d594baa9016e02c3b5fe967da0b8ec0/viewpager2).

**Bug fixes**

- Fix for`FragmentStateAdapter`edge-case issue with`Fragment`back stack. ([b/139095195](https://issuetracker.google.com/139095195))
- Fix for`EditText`with certain attribute configurations causing a scroll/page jump on typing/focus. ([b/138044582](https://issuetracker.google.com/138044582),[b/139432498](https://issuetracker.google.com/139432498))
- Fix for an issue with`ItemDecoration`instances, and a workaround for overscroll indicator positioning. ([b/139012032](https://issuetracker.google.com/139012032))
- A number of issues were fixed in other components to work better with`ViewPager2`:[RecyclerView](https://developer.android.com/jetpack/androidx/releases/recyclerview#1.1.0-beta04),[NestedScrollView](https://developer.android.com/jetpack/androidx/releases/core#1.2.0-alpha04), and[Navigation](https://developer.android.com/jetpack/androidx/releases/navigation#2.2.0-alpha02).

### Version 1.0.0-beta03

August 7, 2019

`androidx.viewpager2:viewpager2:1.0.0-beta03`is released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/4ec8012fa882d6e001173996e84466244675aa25..f3df487541c41b9b0e81199a73eaeda058cab7a9/viewpager2).

**Bug fixes**

- Fix for`FragmentStateAdapter`issue with transient`Fragment`state.[b/134246546](https://issuetracker.google.com/issues/134246546)
- Fix for`currentItem`and`scrollState`issues when a data-set is changed during a smooth-scroll (edge cases addressed).[b/137642608](https://issuetracker.google.com/issues/137642608)
- Fix for`PageTransformer`(including`MarginPageTransformer`) animations conflicting with data-set change animations.[b/134658996](https://issuetracker.google.com/issues/134658996)
- Fix for smooth-scroll animations in large datasets (`float`integer value limit).[b/134858960](https://issuetracker.google.com/issues/134858960)

### Version 1.0.0-beta02

July 19, 2019

`androidx.viewpager2:viewpager2:1.0.0-beta02`is released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/6fe77d4733bc59a2d99d9266e4b7593952f9667a..4ec8012fa882d6e001173996e84466244675aa25/viewpager2).

**Bug fixes**

- Removed unintentional jacoco dependency that was introduced in`1.0.0-beta01`. ([b/137782951](https://issuetracker.google.com/issues/137782951))

### Version 1.0.0-beta01

July 17, 2019

`androidx.viewpager2:viewpager2:1.0.0-beta01`is released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/75429d194b9c286a3b71cd8bd7468c25dd25cd59..6fe77d4733bc59a2d99d9266e4b7593952f9667a/viewpager2).
| **Caution:** This version contains an unintentional dependency on`org.jacoco:org.jacoco.agent:0.8.3`, which can cause a build failure. Please update to the latest version, in which this dependency has been removed.

**Bug fixes**

- Fix for`ViewPager2.updateCurrentItem`crash while scrolling and updating data-set
- Fix for`NullPointerException`crash related to`ViewPager2.isLayoutRtl`
- `TOUCH_SLOP_PAGING`now a default touch slop
- `OnPageChangeCallback`events fixed for empty adapters (page`0`instead of`-1`for parity with`ViewPager1`)

**Known issues**

- We are still working on the[remaining open issues](https://issuetracker.google.com/issues?q=hotlistid:814487+status:open+targetedto:(6.1+%7C+6.3))before moving to Stable

### Version 1.0.0-alpha06

July 2, 2019

`androidx.viewpager2:viewpager2:1.0.0-alpha06`is released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/abb953b4f55bff29662946b07e361bcbf2d76ca8..75429d194b9c286a3b71cd8bd7468c25dd25cd59/viewpager2).

This is our last planned alpha before freezing the API and moving to beta - please provide us with API feedback.

**New features**

- Foundations for improved Accessibility:`ACTION_PAGE_RIGHT`,`ACTION_PAGE_DOWN`, etc.

**API changes**

- `FragmentStateAdapter`: non-primary-item`Fragment`s are capped at`STARTED`, and their`menuVisibility`is set to false.
- `PageTransformer`,`MarginPageTransformer`,`CompositePageTransformer`: documentation for`position`fixed.

**Bug fixes**

- `currentItem`after data-set change / adapter change fixed.
- `MarginPageTransformer`with`offscreenPageLimit`issue fixed.
- Accessibility actions while in`FakeDrag`behaviour fixed.

### Version 1.0.0-alpha05

June 5, 2019

`androidx.viewpager2:viewpager2:1.0.0-alpha05`is released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/5335d9969ded09ef2812c3ac63c42853375a1c55..ed4dbece666c83542ccb529408f648f7ef53085a/viewpager2).

**New features**

- `ItemDecorator`introduced with a behaviour consistent with`RecyclerView`.
- `MarginPageTransformer`introduced to provide an ability to create space between pages (outside of page inset).
- `CompositePageTransformer`introduced to provide an ability to combine multiple`PageTransformer`s.

**API changes**

- `FragmentStateAdapter#getItem`method renamed to`FragmentStateAdapter#createFragment`- previous method name has proven to be a source of bugs in the past.
- `OFFSCREEN_PAGE_LIMIT_DEFAULT`value changed from`0`to`-1`. No need for a client code change if the`OFFSCREEN_PAGE_LIMIT_DEFAULT`constant used.

**Bug fixes**

- `getCurrentItem()`behaviour corrected when`SCROLL_STATE_SETTLING`gets interrupted by a drag in the opposite direction.
- `FragmentStateAdapter`class loader issues addressed in the "Don't keep activities" context.
- `setOffscreenPageLimit`documentation improved.

### Version 1.0.0-alpha04

May 7, 2019

`androidx.viewpager2:viewpager2:1.0.0-alpha04`is released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/a1c79782eee81abb62c774f0f516ac27852282f2..5335d9969ded09ef2812c3ac63c42853375a1c55/viewpager2).

**New features**

- `offscreenPageLimit`: allows for a tight control of the number of page`View`s /`Fragment`s kept in the view hierarchy

**API changes**

- `orientation`and`isUserScrollable`attributes are no longer part of`SavedState`
- `saveState`and`restoreState`methods made final in`FragmentStateAdapter`
- `ViewPager2.Orientation`and`ViewPager2.ScrollState`annotations made non-public

**Bug fixes**

- `SavedState`: fixed an issue with restoring when`Activity`gets destroyed / recreated
- `SavedState`: delayed restoring until the adapter is set
- `OnPageChangeCallback`: minor edge cases fixed

### Version 1.0.0-alpha03

April 3rd, 2019

`androidx.viewpager2:viewpager2:1.0.0-alpha03`is released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/a6c93820c879141a92612abcf559a1993ceeb716..a1c79782eee81abb62c774f0f516ac27852282f2/viewpager2).

**New features**

- Ability to programmatically scroll ViewPager2:`fakeDragBy(offsetPx)`.

**API changes**

- `FragmentStateAdapter`now requires a`Lifecycle`object. Two utility constructors added to obtain it from the host`FragmentActivity`or the host`Fragment`.

**Bug fixes**

- Numerous`Fragment`support fixes:
  - handling dataset updates while minimised, or during a screen rotation;
  - removing irrelevant Fragments after rotation;
  - removing saved state of removed items.
- `PageChangeCallback`: fixed page offset calculation for pages with margins.

### Version 1.0.0-alpha02

March 13, 2019

`androidx.viewpager2:viewpager2:1.0.0-alpha02`is released. The full list of commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/965e50ae02ab8c0821aa6db4d3296630ee8f4742..a6c93820c879141a92612abcf559a1993ceeb716/viewpager2).

**New features**

- Ability to disable user input (`setUserInputEnabled`,`isUserInputEnabled`)

**API changes**

- ViewPager2 class final

**Bug fixes**

- `FragmentStateAdapter`stability fixes

### Version 1.0.0-alpha01

February 7, 2019

`androidx.viewpager2:viewpager2 1.0.0-alpha01`is released. This is the first release of ViewPager2.

**New features**

- Comparing to its predecessor`android.support.v4.view.ViewPager`(VP1):
  - Right-to-left (RTL) layout support
  - Vertical orientation support
  - `notifyDataSetChanged`fully functional (VP1 bugs addressed)

**API changes**

- `FragmentStateAdapter`replaces`FragmentStatePagerAdapter`
- `RecyclerView.Adapter`replaces`PagerAdapter`
- `registerOnPageChangeCallback`replaces`addPageChangeListener`

**Known issues**

- clipToPadding
- no fakeDrag
- JavaDoc
- nested scrolling parallel to orientation
- no offscreen limit control
- needs better TabLayout integration
- no pageWidth setter (forced 100%/100%)
- page transformer: no hardware/software layer choice; no reverse drawing order
- keep current item visible when inserting a page before current
- keyboard navigation needs work
- `FragmentStateAdapter`stability / performance improvements coming