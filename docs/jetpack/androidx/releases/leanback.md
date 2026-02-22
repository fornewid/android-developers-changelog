---
title: https://developer.android.com/jetpack/androidx/releases/leanback
url: https://developer.android.com/jetpack/androidx/releases/leanback
source: md.txt
---

# Leanback

# Leanback

[User Guide](https://developer.android.com/training/tv/start/start#leanback-req)[Code Sample](https://github.com/android/tv-samples)  
API Reference  
[androidx.leanback.app](https://developer.android.com/reference/kotlin/androidx/leanback/app/package-summary)  
[androidx.leanback.database](https://developer.android.com/reference/kotlin/androidx/leanback/database/package-summary)  
[androidx.leanback.graphics](https://developer.android.com/reference/kotlin/androidx/leanback/graphics/package-summary)  
[androidx.leanback.media](https://developer.android.com/reference/kotlin/androidx/leanback/media/package-summary)  
[androidx.leanback.preference](https://developer.android.com/reference/kotlin/androidx/leanback/preference/package-summary)  
[androidx.leanback.system](https://developer.android.com/reference/kotlin/androidx/leanback/system/package-summary)  
[androidx.leanback.widget](https://developer.android.com/reference/kotlin/androidx/leanback/widget/package-summary)  
[androidx.leanback.widget.picker](https://developer.android.com/reference/kotlin/androidx/leanback/widget/picker/package-summary)  
Use Compose for TV instead of this artifact.  

| Latest Update  |                                 Stable Release                                  | Release Candidate | Beta Release | Alpha Release |
|----------------|---------------------------------------------------------------------------------|-------------------|--------------|---------------|
| April 23, 2025 | [1.2.0](https://developer.android.com/jetpack/androidx/releases/leanback#1.2.0) | -                 | -            | -             |

## Declaring dependencies

To add a dependency on Leanback, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    def leanback_version = "1.2.0"

    implementation "androidx.leanback:leanback:$leanback_version"

    // leanback-preference is an add-on that provides a settings UI for TV apps.
    implementation "androidx.leanback:leanback-preference:$leanback_version"

    // leanback-paging is an add-on that simplifies adding paging support to a RecyclerView Adapter.
    implementation "androidx.leanback:leanback-paging:1.1.0"

    // leanback-tab is an add-on that provides customized TabLayout to be used as the top navigation bar.
    implementation "androidx.leanback:leanback-tab:1.1.0"
}
```

### Kotlin

```kotlin
dependencies {
    val leanback_version = "1.2.0"

    implementation("androidx.leanback:leanback:$leanback_version")

    // leanback-preference is an add-on that provides a settings UI for TV apps.
    implementation("androidx.leanback:leanback-preference:$leanback_version")

    // leanback-paging is an add-on that simplifies adding paging support to a RecyclerView Adapter.
    implementation("androidx.leanback:leanback-paging:1.1.0")

    // leanback-tab is an add-on that provides customized TabLayout to be used as the top navigation bar.
    implementation("androidx.leanback:leanback-tab:1.1.0")
}
```

For more information about dependencies, see[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:460758+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=460758&template=1422626)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Leanback-Grid Version 1.0.0

### Version 1.0.0

April 23, 2025

`androidx.leanback:leanback-grid:1.0.0`is released. The version does not contain any change, it just moves it to stable.

### Version 1.0.0-rc01

April 9, 2025

`androidx.leanback:leanback-grid:1.0.0-rc01`is released. This does not have any major commits, and only moves the library to stable.

### Version 1.0.0-alpha03

November 15, 2023

`androidx.leanback:leanback-grid:1.0.0-alpha03`is released.[Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9ce75ea1baa2af10dda8f787f69c40c6654bcac1..312eb9f1ddece3a18317f18515a877e0e745cb2c/leanback/leanback-grid)

**Dependency Updates**

- Update to depend on[RecyclerView`1.3.2`](https://developer.android.com/jetpack/androidx/releases/recyclerview#recyclerview-1.3.2)to fix a common crash in TV apps ([I2c3a0](https://android-review.googlesource.com/#/q/I2c3a0f7ae43f72bd6a1dbbe30c269148f824a885),[b/292114537](https://issuetracker.google.com/issues/292114537))

### Version 1.0.0-alpha02

September 6, 2023

`androidx.leanback:leanback-grid:1.0.0-alpha02`is released.[Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/cc1240d00b28657ee0c1a937f60430eaf1b03b09..9ce75ea1baa2af10dda8f787f69c40c6654bcac1/leanback/leanback-grid)

**API Changes**

- Made`setFocusOutAllowed`public to allow the focus out properties to be set programmatically. ([Iebd99](https://android-review.googlesource.com/#/q/Iebd996b00e7b04903261a025d77ddbbd9be81f90))

**Bug Fixes**

- Ensure grids are treated as grids by a11y services by setting an a11y node info class name. ([I12812](https://android-review.googlesource.com/#/q/I128122352a3fc4898cc6ba76d7da8166519bd648))
- Add missing navigation sound when falling to smooth scroll. ([f49767](https://android.googlesource.com/platform/frameworks/support/+/f4976759c48f5a0dd78b14c4e8b3f77645576e98))

### Version 1.0.0-alpha01

November 17, 2021

`androidx.leanback:leanback-grid:1.0.0-alpha01`is released.[Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/cc1240d00b28657ee0c1a937f60430eaf1b03b09/leanback/leanback-grid)

**New Features**

- Moved following classes/interfaces from`leanback`to new`leanback-grid`library:`BaseGridView`,`FacetProvider`,`FacetProviderAdapter`,`GridLayoutManager`,`HorizontalGridView`,`ItemAlignmentFacet`,`OnChildLaidOutListener`,`OnChildSelectedListener`,`OnChildViewHolderSelectedListener`,`VerticalGridView`,`ViewHolderTask`,`Visibility`. This change preserves binary compatibility. Anyone willing to use just the grid view components of leanback can directly use`leanback-grid`as a dependency. ([If1e49](https://android-review.googlesource.com/#/q/If1e490c6a36ba9e8b2e6de7aa0774c5bc374e50d))

## Leanback Leanback-Preference Version 1.2.0

### Version 1.2.0

April 23, 2025

`androidx.leanback:leanback:1.2.0`and`androidx.leanback:leanback-preference:1.2.0`are released. The version does not contain any change, it just moves it to stable.

### Version 1.2.0-rc01

April 9, 2025

`androidx.leanback:leanback:1.2.0-rc01`and`androidx.leanback:leanback-preference:1.2.0-rc01`are released. This does not have any major commits, and only moves the library to stable.

### Version 1.2.0-alpha04

November 15, 2023

`androidx.leanback:leanback:1.2.0-alpha04`and`androidx.leanback:leanback-preference:1.2.0-alpha04`are released.[Version 1.2.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9ce75ea1baa2af10dda8f787f69c40c6654bcac1..312eb9f1ddece3a18317f18515a877e0e745cb2c/leanback)

**Bug Fixes**

- ([I2c3a0](https://android-review.googlesource.com/#/q/I2c3a0f7ae43f72bd6a1dbbe30c269148f824a885),[b/292114537](https://issuetracker.google.com/issues/292114537))

**Dependency Update**

- Update recyclerview requirement to 1.3.2 to fix a common crash in TV apps

### Version 1.2.0-alpha03

September 6, 2023

`androidx.leanback:leanback:1.2.0-alpha03`and`androidx.leanback:leanback-preference:1.2.0-alpha03`are released.[Version 1.2.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/cc1240d00b28657ee0c1a937f60430eaf1b03b09..9ce75ea1baa2af10dda8f787f69c40c6654bcac1/leanback/leanback)

**API Changes**

- Added`GuidedActionAppCompatEditText`to better support the AppCompat theme. ([ab7cf1](https://android.googlesource.com/platform/frameworks/support/+/ab7cf168c7f76e45b2d2923ee6646b403b37a9a4),[dc954d](https://android.googlesource.com/platform/frameworks/support/+/dc954d0176dcdf6d37ee0ad6f9b1fb95d80b3540))

### Version 1.2.0-alpha02

November 17, 2021

`androidx.leanback:leanback:1.2.0-alpha02`and`androidx.leanback:leanback-preference:1.2.0-alpha02`are released.[Version 1.2.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/97264aa4532db7f7db1ffb3f42f3a9204971dbfc..cc1240d00b28657ee0c1a937f60430eaf1b03b09/leanback)

**New Features**

- Moved following classes/interfaces from`leanback`to new`leanback-grid`library:`BaseGridView`,`FacetProvider`,`FacetProviderAdapter`,`GridLayoutManager`,`HorizontalGridView`,`ItemAlignmentFacet`,`OnChildLaidOutListener`,`OnChildSelectedListener`,`OnChildViewHolderSelectedListener`,`VerticalGridView`,`ViewHolderTask`,`Visibility`. This change preserves binary compatibility. Anyone willing to use just the grid view components of leanback can directly use`leanback-grid`as a dependency. ([If1e49](https://android-review.googlesource.com/#/q/If1e490c6a36ba9e8b2e6de7aa0774c5bc374e50d))

### Version 1.2.0-alpha01

July 21, 2021

`androidx.leanback:leanback:1.2.0-alpha01`and`androidx.leanback:leanback-preference:1.2.0-alpha01`are released.[Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bf8af1081ee3ce8c6dbea9e75c37f53dd8c0553b..97264aa4532db7f7db1ffb3f42f3a9204971dbfc/leanback)

**New Features**

- Made leanback GridLayoutManager public and exchangeable in BaseGridView. ([f316b5](https://android.googlesource.com/platform/frameworks/support/+/f316b5dc1f24099be9115c6c39ab62b78e33a6d0))

**API Changes**

- Made leanback GridLayoutManager public and exchangeable in BaseGridView. ([f316b5](https://android.googlesource.com/platform/frameworks/support/+/f316b5dc1f24099be9115c6c39ab62b78e33a6d0))

## Version 1.1.0

### Leanback Version 1.1.0-rc02

July 21, 2021

`androidx.leanback:leanback:1.1.0-rc02`is released.[Version 1.1.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bf8af1081ee3ce8c6dbea9e75c37f53dd8c0553b..634cd131d8f496ae5f0471629cfb1aaadd65ae06/leanback/leanback)

**Bug Fixes**

- Fixed details fragment background bug. ([40d8e3](https://android.googlesource.com/platform/frameworks/support/+/40d8e3cd2f78a1622d1a806cf910c7c961837ed9))

### Leanback Leanback-Preference Version 1.1.0-rc01

April 7, 2021

`androidx.leanback:leanback:1.1.0-rc01`and`androidx.leanback:leanback-preference:1.1.0-rc01`are released.[Version 1.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/38a668d3ef95f40ad28d6e735a2c3eb95ae4cf63..bf8af1081ee3ce8c6dbea9e75c37f53dd8c0553b/leanback)

- Fixed view leaks in`SearchSupportFragment()`([6c47a1](https://android.googlesource.com/platform/frameworks/support/+/6c47a1e08882d4932ace063ff2d1ed11f0fe37da),[b/171909417](https://issuetracker.google.com/issues/171909417))
- Made speech recognizer optional for`SearchSupportFragment`([4ff949](https://android.googlesource.com/platform/frameworks/support/+/4ff949b813f4954533390ed87672771c45d60bc4),[b/169936953](https://issuetracker.google.com/issues/169936953))

## Leanback-Paging Version 1.1

### Version 1.1.0

April 23, 2025

`androidx.leanback:leanback-paging:1.1.0`and`androidx.leanback:leanback-tab:1.1.0`are released. The version does not contain any change, it just moves it to stable.

### Version 1.1.0-rc01

April 9, 2025

`androidx.leanback:leanback-paging:1.1.0-rc01`and`androidx.leanback:leanback-tab:1.1.0-rc01`are released. This does not have any major commits, and only moves the library to stable.

### Version 1.1.0-alpha11

November 15, 2023

`androidx.leanback:leanback-paging:1.1.0-alpha11`is released with no changes.[Version 1.1.0-alpha11 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9ce75ea1baa2af10dda8f787f69c40c6654bcac1..312eb9f1ddece3a18317f18515a877e0e745cb2c/leanback/leanback-paging)

### Version 1.1.0-alpha10

September 6, 2023

`androidx.leanback:leanback-paging:1.1.0-alpha10`is released.[Version 1.1.0-alpha10 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/cc1240d00b28657ee0c1a937f60430eaf1b03b09..9ce75ea1baa2af10dda8f787f69c40c6654bcac1/leanback/leanback-paging)

**New Features**

- Update leanback-paging to Paging 3.1.0. ([882ed1](https://android.googlesource.com/platform/frameworks/support/+/882ed18ddf35bf0189622c10ec4205261fdfa1f6))

### Leanback-Paging Version 1.1.0-alpha09

November 17, 2021

`androidx.leanback:leanback-paging:1.1.0-alpha09`is released.[Version 1.1.0-alpha09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/97264aa4532db7f7db1ffb3f42f3a9204971dbfc..cc1240d00b28657ee0c1a937f60430eaf1b03b09/leanback/leanback-paging)

**Bug Fixes**

- Updated to use latest paging APIs.

### Leanback-Paging Version 1.1.0-alpha08

July 21, 2021

`androidx.leanback:leanback-paging:1.1.0-alpha08`is released.[Version 1.1.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6207afb1646d302c5d29c2c67d332b48db87fb27..97264aa4532db7f7db1ffb3f42f3a9204971dbfc/leanback/leanback-paging)

**API Changes**

- Added`.peek()`and`.snapshot()`APIs to PagingDataAdapter, allowing inspection of presented data without triggering page fetch. ([Ic8917](https://android-review.googlesource.com/#/q/Ic89171a55a10a73b585f130d2a9eb1b8927db1fd))

### Leanback-Paging Version 1.1.0-alpha07

January 13, 2021

`androidx.leanback:leanback-paging:1.1.0-alpha07`is released.[Version 1.1.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/38a668d3ef95f40ad28d6e735a2c3eb95ae4cf63..6207afb1646d302c5d29c2c67d332b48db87fb27/leanback/leanback-paging)

**API Changes**

- Updated the convenience properties,`CombinedLoadStates.refresh`,`CombinedLoadStates.prepend`,`CombinedLoadStates.append`to only transition from`Loading`to`NotLoading`after both mediator and source load states are`NotLoading`to ensure the remote update has been applied. ([I65619](https://android-review.googlesource.com/#/q/I656192632c4ce073ac8e54a3f1c597bbbae77002))

### Leanback Leanback-Preference Leanback-Tab Version 1.1.0-beta01

December 2, 2020

`androidx.leanback:leanback:1.1.0-beta01`,`androidx.leanback:leanback-preference:1.1.0-beta01`, and`androidx.leanback:leanback-tab:1.1.0-beta01`are released.[Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f5a2c7477391539d8bc9f65a8f0db1e8a7bf2cf5..38a668d3ef95f40ad28d6e735a2c3eb95ae4cf63/leanback)

**Bug Fixes**

- Fix view leak when pushing VerticalGridSupportFragment to backstack ([Iaac69](https://android-review.googlesource.com/#/q/Iaac695b36b0c2e1bddddb2e496ad0fc5038d8e1e),[b/171909417](https://issuetracker.google.com/issues/171909417))
- Fix view leak when pushing BrowseSupportFragment to backstack ([I34483](https://android-review.googlesource.com/#/q/I344835e2d429a7bacd2416077f054fee20f59dcb),[b/171909417](https://issuetracker.google.com/issues/171909417))
- Fix view leak when pushing DetailsSupportFragment to backstack ([Ifec9e](https://android-review.googlesource.com/#/q/Ifec9e735bddd83831a07119c26c1e80c71cd0a6d),[b/171909417](https://issuetracker.google.com/issues/171909417))
- Fix view leak when pushing RowsSupportFragment to backstack ([I985d4](https://android-review.googlesource.com/#/q/I985d4b09ef8d137f6f21590fdef615d7dca322cd),[b/171909417](https://issuetracker.google.com/issues/171909417))
- Fix GuidedStepSupportFragment background transition animation. ([I86d15](https://android-review.googlesource.com/#/q/I86d156db92dd90b49f7efbbb4efa0595602ff505),[b/173647688](https://issuetracker.google.com/issues/173647688))
- Fix IllegalArgumentException when restoring GuidedStepSupportFragment ([Ic829f](https://android-review.googlesource.com/#/q/Ic829f9256c1bd825a04bdeb81e673aa2a75527db),[b/172000115](https://issuetracker.google.com/issues/172000115))
- Fix GridLayoutManager NullPointerException in findContainingItemView() when clearFocus() ([Id0e42](https://android-review.googlesource.com/#/q/Id0e42555cfe720eb291f0c80dc3dab340845783e))

### Leanback-Paging Version 1.1.0-alpha06

December 2, 2020

`androidx.leanback:leanback-paging:1.1.0-alpha06`is released.[Version 1.1.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f5a2c7477391539d8bc9f65a8f0db1e8a7bf2cf5..38a668d3ef95f40ad28d6e735a2c3eb95ae4cf63/leanback/leanback-paging)

**API Changes**

- dataRefreshFlow / dataRefreshListener APIs have been removed as they are redundant with loadStateFlow / Listener updates. For those migrating, the loadStateFlow equivalent is:

      loadStateFlow.distinctUntilChangedBy { it.refresh }
          .filter { it.refresh is NotLoading }

  ([Ib5570](https://android-review.googlesource.com/#/q/Ib55709c3f560711200a9eac5a4931d57c76053af),[b/173530908](https://issuetracker.google.com/issues/173530908))
- Full deprecate dataRefreshFlow / Listener methods with a replaceWith clause. ([I6e2dd](https://android-review.googlesource.com/#/q/I6e2dd23b100bc1186dc652e5076b2d15b191c436))

### Version 1.1.0-alpha05

October 1, 2020

`androidx.leanback:leanback-*:1.1.0-alpha05`is released.[Version 1.1.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b1ae31bb42f205dd2c4cf3c1aaf6d6e00ae84038..f5a2c7477391539d8bc9f65a8f0db1e8a7bf2cf5/leanback)

**New Features**

- Let A11Y navigation respect GridLayoutManager focusOutFront and focusOutEnd attributes. ([b/161390258](https://issuetracker.google.com/issues/161390258))

**Bug Fixes**

- Fix View leak in`GuidanceStylist.onDestroyView()`([b/164841457](https://issuetracker.google.com/issues/164841457))
- Fix ConcatAdapter in GridLayoutManager ([b/165694295](https://issuetracker.google.com/issues/165694295))
- leanback-tab: Javadoc improvements and minor code refactoring ([aosp/1393383](https://android-review.googlesource.com/c/platform/frameworks/support/+/1393383))
- Remove setRecyclerView method from API which was added when same method was deprecated on RecyclerView. Update leanback lib to use RecyclerView's new addRecyclerListener API method. ([I14798](https://android-review.googlesource.com/#/q/I14798462b11be3ac2bd0b73fcfe28711effa4379))

### Version 1.1.0-alpha04

August 11, 2020

`androidx.leanback:leanback:1.1.0-alpha04`,`androidx.leanback:leanback-paging:1.1.0-alpha04`,`androidx.leanback:leanback-preference:1.1.0-alpha04`, and`androidx.leanback:leanback-tab:1.1.0-alpha04`are released.[Version 1.1.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/740cde70237dd276f8ad66dfe9528b1cdb5d54bb..b1ae31bb42f205dd2c4cf3c1aaf6d6e00ae84038/leanback)

**New Features**

- The LeanbackTabLayout provides the top navigation (typically displayed horizontally across the top of the app) in the[browse experience](https://developer.android.com/training/tv/playback/browse).
- Paging for Leanback simplifies adding paging support to a[RecyclerView.Adapter](https://developer.android.com/reference/kotlin/androidx/recyclerview/widget/RecyclerView.Adapter).
- Added appcompat themes for leanback that will simplify the creation of a single code base between mobile and TV.

**API Changes**

- Added adapter based on asyncpagingdatadiffer for leanback widgets ([If0dfe](https://android-review.googlesource.com/#/q/If0dfed7c38fd4a20271e9a12d45ab71d3eba0c26))
- Adding a customized TabLayout to be used as the top navigation bar in leanback ([I1e304](https://android-review.googlesource.com/#/q/I1e3048d300106ad0b0f9ef55f14e7070793a579a))

### Version 1.1.0-alpha03

December 18, 2019

`androidx.leanback:leanback:1.1.0-alpha03`and`androidx.leanback:leanback-preference:1.1.0-alpha03`are released.[Leanback Version 1.1.0-alpha03 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/7d95cd5e6358dee8cab72c39e4e99e412c7a450c..740cde70237dd276f8ad66dfe9528b1cdb5d54bb/leanback)and[Leanback-Preference Version 1.1.0-alpha03 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/049b727631e94ea7bd14c2568b65da29a0add661..740cde70237dd276f8ad66dfe9528b1cdb5d54bb/leanback-preference).

**New features**

- BaseGridView now supports custom scrolling speeds ([aosp/952718](https://android-review.googlesource.com/c/952718))
- Made guided step item touch more friendly ([aosp/1167964](https://android-review.googlesource.com/c/1167964))
- Exposed the BaseGridView OnLayoutCompleteListener so apps can perform View transformations after the layout pass. ([aosp/1164409](https://android-review.googlesource.com/c/1164409))

**API changes**

- Added a new API to allow custom BaseGridView scrolling speeds ([aosp/952718](https://android-review.googlesource.com/c/952718))
- Added a new API to add OnLayoutCompleteListener in BaseGridView ([aosp/1164409](https://android-review.googlesource.com/c/1164409))

**Bug fixes**

- Fixed a bug where fast layout pass doesn't update the alignment of a child. ([aosp/1122745](https://android-review.googlesource.com/c/1122745))
- Fixed a stack overflow crash in the Picker widget when the focus is changing ([aosp/1168473](https://android-review.googlesource.com/c/1168473))

**Dependency changes**

- Leanback-preference: pinned the dependency of`androidx.preference`to`1.1.0`([aosp/1181902](https://android-review.googlesource.com/c/1181902))

### Version 1.1.0-alpha02

May 7, 2019

`androidx.leanback:leanback:1.1.0-alpha02`and`androidx.leanback:leanback-preference:1.1.0-alpha02`are released. The commits included in this version can at[leanback commits](https://android.googlesource.com/platform/frameworks/support/+log/612658bcef0ed83d388dc2d49377854857614d7f..7d95cd5e6358dee8cab72c39e4e99e412c7a450c/leanback)and[leanback-preference commits](https://android.googlesource.com/platform/frameworks/support/+log/393699c416e547076b19186fef4968a64cf4971a..049b727631e94ea7bd14c2568b65da29a0add661/leanback-preference).

**New features**

- RowsSupportFragment is now allowed to share ViewHolders with other RowsSupportFragments, which would improve performance for a multiple-tab UI.

**API changes**

- Added`PlaybackSupportFragment.setShowOrHideControlsOverlayOnUserInteraction()`to allow app disable auto hide/show playback controls when DPAD is pressed.

**Bug fixes**

- Fixed broken leanback-preference Fragments theme due to a change in preference library.
- Fix navigation bug when BACK key is pressed on SearchEditText

### Version 1.1.0-alpha01

January 30, 2019

`androidx.leanback:leanback 1.1.0-alpha01`is released.

**New features**

- Added PinPicker widget.
- Outline clipping is now disabled by default on low-ram device.
- Allowed customized PlaybackSupportFragment showing/hiding controls behavior ([b/122918400](https://issuetracker.google.com/122918400))

**API changes**

- Framework fragments were deprecated.
- New PinPicker class.

**Bug fixes**

- Fixed a fragment transaction crash after`BrowseSupportFragment`is stopped
- `GuidedStepSupportFragment`should not clip items in`VerticalGridView`([aosp/787396](https://android-review.googlesource.com/787396))
- `onCreateActionsStylist()`and`onCreateGuidanceStylist()`were moved from constructor to`GuidedSupportFragment.onCreate()`([aosp/787397](https://android-review.googlesource.com/787397))
- Fixed a bug where`SearchSupportFragment`failed to focus to results fragment. ([aosp/798833](https://android-review.googlesource.com/798833))
- Fixed a scrolling bug in`VerticalGridView`and`HorizontalGridView`([aosp/858809](https://android-review.googlesource.com/858809))

`androidx.leanback-preference 1.1.0-alpha01`is released.

**New features**

- Added androidx fragment classes, deprecated framework fragment classes.
- Colors and fonts are now based on framework theme attributes.

**API changes**

- New androidx fragment classes, framework fragment classes were deprecated.