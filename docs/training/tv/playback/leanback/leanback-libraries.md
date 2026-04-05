---
title: Leanback UI toolkit libraries  |  Android TV  |  Android Developers
url: https://developer.android.com/training/tv/playback/leanback/leanback-libraries
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android TV](https://developer.android.com/training/tv)

# Leanback UI toolkit libraries Stay organized with collections Save and categorize content based on your preferences.




Build better with Compose

Create beautiful UIs with minimal code using Jetpack Compose for Android TV OS.

[Compose for TV →](https://developer.android.com/training/tv/playback/compose)

![](/static/images/android-compose-tv-logo.png)

**Warning:** The Leanback library is deprecated. Use [Jetpack Compose for
Android TV OS](/training/tv/playback/compose) instead.

The deprecated Leanback UI toolkit provides some
TV-specific libraries exclusive to apps developed for Android TV OS. These
libraries include the following:

* [Leanback](/training/tv/playback) library: provides UI templates that
  simplify creating Android TV apps.
* [Leanback Preferences](/reference/androidx/leanback/preference/package-summary)
  library: provides preferences and settings screens that are consistent with
  the platform but can be themed to match your app.
* [Leanback Paging](#leanback-paging-library) library: supports the
  AndroidX paging model for `ObjectAdapters`, which are commonly used with the
  Leanback templates.
* [Leanback Tabs](#leanback-tabs-library) library: supports tabbed
  navigation on Android TV.

## Leanback paging library

Paging inside the Leanback UI toolkit works the same as the AndroidX
[Paging 3](/topic/libraries/architecture/paging/v3-overview) library, which
simplifies adding paging to a
[`RecyclerView.Adapter`](/reference/kotlin/androidx/recyclerview/widget/RecyclerView.Adapter).
With the Leanback Paging library, the adapter that is exposed is typically an
[`ObjectAdapter`](/reference/kotlin/androidx/leanback/widget/ObjectAdapter)
instead, so the library adds paging support to `ObjectAdapter`.

To add a paging adapter to your app, first add the library dependency to your project:

```
implementation "androidx.leanback:leanback-paging:$version"
```

Then follow the
[Paging 3 documentation](/topic/libraries/architecture/paging/v3-overview) using
`androidx.leanback.paging.PagingDataAdapter` instead of
`androidx.paging.PagingDataAdapter`. The only difference is that you’re now able
to pass in a [`Presenter`](/reference/kotlin/androidx/leanback/widget/Presenter)
or
[`PresenterSelector`](/reference/kotlin/androidx/leanback/widget/PresenterSelector).
This works anywhere you would ordinarily use an `ObjectAdapter`, such as in a
[`ListRow`](/reference/kotlin/androidx/leanback/widget/ListRow):

### Kotlin

```
val adapter: PagingDataAdapter<MyItem> = PagingDataAdapter(myPresenter,
   object : DiffUtil.ItemCallback<MyItem>() {
       override fun areItemsTheSame(
           oldItem: MyItem,
           newItem: MyItem
       ): Boolean {
           return oldItem.id === newItem.id
       }

       override fun areContentsTheSame(
           oldItem: MyItem,
           newItem: MyItem
       ): Boolean {
           return oldItem == newItem
       }
   })

val header = HeaderItem(headerTitle)
val row = ListRow(header, adapter)
```

### Java

```
PagingDataAdapter<MyItem> adapter = new PagingDataAdapter(myPresenter, new DiffUtil.ItemCallback<MyItem>() {
    @Override
    public boolean areItemsTheSame(@NonNull MyItem oldItem, @NonNull MyItem newItem) {
        return oldItem.getId().equals(newItem.getId());
    }

    @Override
    public boolean areContentsTheSame(@NonNull MyItem oldItem, @NonNull MyItem newItem) {
        return oldItem.equals(newItem);
    }
});

HeaderItem header = new HeaderItem(headerTitle);
Row row = new ListRow(header, adapter);
```

## Leanback Tabs library

The Leanback UI toolkit templates provide side navigation in the
[browse screen](/training/tv/playback/browse). To add a row of tabs horizontally
across the top of the app, you can instead use Leanback Tabs instead.

Add the library dependency to your project:

```
implementation "androidx.leanback:leanback-tab:$version"
```

Then implement tabs using `LeanbackTabLayout` and `LeanbackViewPager` by
following the existing
[ViewPager guide](/guide/navigation/navigation-swipe-view). Note that
`LeanbackViewPager` is based on `ViewPager`, not `ViewPager2`.

The following is an example:

### Kotlin

```
val leanbackTabLayout = findViewById<LeanbackTabLayout>(R.id.tab_layout)
val leanbackViewPager = findViewById<LeanbackViewPager>(R.id.view_pager)

leanbackViewPager.setAdapter(adapter)
leanbackTabLayout.setupWithViewPager(leanbackViewPager)
```

### Java

```
LeanbackTabLayout leanbackTabLayout = findViewById(R.id.tab_layout);
LeanbackViewPager leanbackViewPager = findViewById(R.id.view_pager);

leanbackViewPager.setAdapter(adapter);
leanbackTabLayout.setupWithViewPager(leanbackViewPager);
```

### Limitations

The Leanback Tabs library has limitations in the themes it supports and how focus
movement is handled.

#### Supported themes

Only themes that are derived from `Theme.AppCompat` are supported. `TabLayout`
contains a theme enforcement constraint, which prevents any nondescendant theme
of `Theme.AppCompat` from being used. You can also use the bridge theme for the
Leanback UI toolkit.

#### Focus movement from tabs to top

When the layout height is greater than the screen height and you press the D-pad
up button, control moves back to the tab instead of staying inside the fragment
and navigating to an item above it (see figure 1). To handle this issue, contents
inside the fragment must override focus search; for example, use
[`RowsSupportFragment`](/reference/androidx/leanback/app/RowsSupportFragment).
[`BrowseSupportFragment`](/reference/androidx/leanback/app/BrowseSupportFragment)
cannot be used inside a tab as it has an overridden focus search method which
prevents the focus from moving back to the tab.

[

](/static/training/tv/images/scrolling-limitation.webm)


**Figure 1.** D-pad up button moves focus to tab instead of preceding item.

[Previous

arrow\_back

In this guide](/training/tv/playback/leanback)

[Next

Create a catalog browser

arrow\_forward](/training/tv/playback/leanback/browse)