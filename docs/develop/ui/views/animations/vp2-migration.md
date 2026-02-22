---
title: https://developer.android.com/develop/ui/views/animations/vp2-migration
url: https://developer.android.com/develop/ui/views/animations/vp2-migration
source: md.txt
---

[`ViewPager2`](https://developer.android.com/jetpack/androidx/releases/viewpager2) is an improved version of the `ViewPager` library that offers
enhanced functionality and addresses common difficulties with using `ViewPager`.
If your app already uses `ViewPager`, read this page to learn more about
migrating to `ViewPager2`.

If you want to use `ViewPager2` in your app and are not currently using
`ViewPager`, read [Slide between fragments using
ViewPager2](https://developer.android.com/training/animation/screen-slide-2) and [Create swipe views with
tabs using ViewPager2](https://developer.android.com/guide/navigation/navigation-swipe-view-2) for more
information.

## Benefits of migrating to ViewPager2

The primary reason to migrate is that `ViewPager2` is receiving active
development support and `ViewPager` is not. However, `ViewPager2` also offers
several other specific advantages.

### Vertical orientation support

`ViewPager2` supports vertical paging in addition to traditional horizontal
paging. You can enable vertical paging for a `ViewPager2` element by setting its
`android:orientation` attribute:

    <androidx.viewpager2.widget.ViewPager2
        xmlns:android="http://schemas.android.com/apk/res/android"
        android:id="@+id/pager"
        android:orie>ntation="vertical" /

You can also set this attribute programmatically using the
[setOrientation()](https://developer.android.com/reference/kotlin/androidx/viewpager2/widget/ViewPager2#setorientation)
method.

### Right-to-left support

`ViewPager2` supports right-to-left (RTL) paging. RTL paging is enabled
automatically where appropriate based on locale, but you can also manually
enable RTL paging for a `ViewPager2` element by setting its
`android:layoutDirection` attribute:

    <androidx.viewpager2.widget.ViewPager2
        xmlns:android="http://schemas.android.com/apk/res/android"
        android:id="@+id/pager"
        android:lay>outDirection="rtl" /

You can also set this attribute programmatically using the
[setLayoutDirection()](https://developer.android.com/reference/kotlin/android/view/View#setlayoutdirection)
method.

### Modifiable fragment collections

`ViewPager2` supports paging through a modifiable collection of fragments,
calling
[`notifyDatasetChanged()`](https://developer.android.com/reference/kotlin/androidx/recyclerview/widget/RecyclerView.Adapter#notifydatasetchanged)
to update the UI when the underlying collection changes.

This means that your app can dynamically modify the fragment collection at
runtime, and `ViewPager2` will correctly display the modified collection.

### DiffUtil

`ViewPager2` is built on [`RecyclerView`](https://developer.android.com/reference/kotlin/androidx/recyclerview/widget/RecyclerView),
which means it has access to the
[`DiffUtil`](https://developer.android.com/reference/kotlin/androidx/recyclerview/widget/DiffUtil) utility
class. This results in several benefits, but most notably it means that
`ViewPager2` objects natively take advantage of the dataset change animations
from the `RecyclerView` class.

## Migrate your app to ViewPager2

Follow these steps to update `ViewPager` objects in your app to `ViewPager2`:

### Update XML layout files

First, replace the `ViewPager` elements in your XML layout files with
`ViewPager2` elements:

    <!-- A ViewPager element -->
    <android.support.v4.view.ViewPager
        xmlns:android="http://schemas.android.com/apk/res/android"
        android:id="@+id/pager"
        android:layout_width="match_parent"
        android:>la<yout_height="match_par>e<nt" /

    !-- A ViewPager2 element --
    androidx.viewpager2.widget.ViewPager2
        xmlns:android="http://schemas.android.com/apk/res/android"
        android:id="@+id/pager"
        android:layout_wid>th="match_parent"
        android:layout_height="match_parent" /

### Update adapter classes

When using `ViewPager`, you had to extend the adapter class that
supplied new pages to the object. Depending on the use case, `ViewPager` used
three different abstract classes. `ViewPager2` only uses two abstract classes.

For each `ViewPager` object you are converting to a `ViewPager2` object,
update the adapter class to extend the appropriate abstract class as follows:

- When `ViewPager` used [`PagerAdapter`](https://developer.android.com/reference/kotlin/androidx/viewpager/widget/PagerAdapter) to page through views, use [`RecyclerView.Adapter`](https://developer.android.com/reference/kotlin/androidx/recyclerview/widget/RecyclerView.Adapter) with `ViewPager2`.
- When `ViewPager` used [`FragmentPagerAdapter`](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentPagerAdapter) to page through a small, fixed number of fragments, use [`FragmentStateAdapter`](https://developer.android.com/reference/kotlin/androidx/viewpager2/adapter/FragmentStateAdapter) with `ViewPager2`.
- When `ViewPager` used [`FragmentStatePagerAdapter`](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentStatePagerAdapter) to page through a large or unknown number of fragment, use [`FragmentStateAdapter`](https://developer.android.com/reference/kotlin/androidx/viewpager2/adapter/FragmentStateAdapter) with `ViewPager2`.

#### Constructor parameters

Fragment-based adapter classes inheriting from `FragmentPagerAdapter` or
`FragmentStatePagerAdapter` always accept a single [`FragmentManager`](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager) object
as a constructor parameter. When you extend `FragmentStateAdapter` for a
`ViewPager2` adapter class, you have the following options for constructor
parameters instead:

- The [`FragmentActivity`](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentActivity) object or [`Fragment`](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment) object where the `ViewPager2` object resides. In most cases, this is the better option.
- A `FragmentManager` object and a [`Lifecycle`](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle) object.

View-based adapter classes inheriting directly from `RecyclerView.Adapter` do
not require a constructor parameter.

#### Override methods

Your adapter classes also need to override different methods for `ViewPager2`
than they did for `ViewPager`:

- Instead of `getCount()`, override [`getItemCount()`](https://developer.android.com/reference/kotlin/androidx/recyclerview/widget/RecyclerView.Adapter#getitemcount). Other than the name, this method is unchanged.
- Instead of `getItem()`, override [`createFragment()`](https://developer.android.com/reference/kotlin/androidx/viewpager2/adapter/FragmentStateAdapter#createfragment) in fragment-based adapter classes. Make sure that your new `createFragment()` method always supplies a new fragment instance each time the function is called instead of reusing instances.

| **Note:** The [`DiffUtil`](https://developer.android.com/reference/kotlin/androidx/recyclerview/widget/DiffUtil) utility class relies on identifying items by ID. If you are using `ViewPager2` to page through a mutable collection, you must also override [`getItemId()`](https://developer.android.com/reference/kotlin/androidx/viewpager2/adapter/FragmentStateAdapter#getitemid) and [`containsItem()`](https://developer.android.com/reference/kotlin/androidx/viewpager2/adapter/FragmentStateAdapter#containsitem).   
| Additionally, The [`getPageWidth()`](https://developer.android.com/reference/kotlin/androidx/viewpager/widget/PagerAdapter#getpagewidth) method is not supported for use with `ViewPager2`. If you currently use `getPageWidth()` with `ViewPager` to enable peeking on adjacent pages, you must instead use the [`clipToPadding`](https://developer.android.com/reference/kotlin/androidx/recyclerview/widget/RecyclerView#getcliptopadding) attribute of `RecyclerView` as demonstrated in the [sample app](https://github.com/android/views-widgets-samples/blob/87e58d1c6d0c832c5b362d33390148679182d314/ViewPager2/app/src/main/java/androidx/viewpager2/integration/testapp/PreviewPagesActivity.kt).

#### Summary

In summary, to convert a `ViewPager` adapter class for use with `ViewPager2`,
you must make the following changes:

1. Change the superclass to `RecyclerView.Adapter` for paging through views, or `FragmentStateAdapter` for paging through fragments.
2. Change the constructor parameters in fragment-based adapter classes.
3. Override `getItemCount()` instead of `getCount()`.
4. Override `createFragment()` instead of `getItem()` in fragment-based adapter classes.

### Kotlin

```kotlin
// A simple ViewPager adapter class for paging through fragments
class ScreenSlidePagerAdapter(fm: FragmentManager) : FragmentStatePagerAdapter(fm) {
    override fun getCount(): Int = NUM_PAGES

    override fun getItem(position: Int): Fragment = ScreenSlidePageFragment()
}

// An equivalent ViewPager2 adapter class
class ScreenSlidePagerAdapter(fa: FragmentActivity) : FragmentStateAdapter(fa) {
    override fun getItemCount(): Int = NUM_PAGES

    override fun createFragment(position: Int): Fragment = ScreenSlidePageFragment()
}
```

### Java

```java
// A simple ViewPager adapter class for paging through fragments
public class ScreenSlidePagerAdapter extends FragmentStatePagerAdapter {
    public ScreenSlidePagerAdapter(FragmentManager fm) {
        super(fm);
    }

    @Override
    public Fragment getItem(int position) {
        return new ScreenSlidePageFragment();
    }

    @Override
    public int getCount() {
        return NUM_PAGES;
    }
}

// An equivalent ViewPager2 adapter class
private class ScreenSlidePagerAdapter extends FragmentStateAdapter {
    public ScreenSlidePagerAdapter(FragmentActivity fa) {
        super(fa);
    }

    @Override
    public Fragment createFragment(int position) {
        return new ScreenSlidePageFragment();
    }

    @Override
    public int getItemCount() {
        return NUM_PAGES;
    }
}
```

### Refactor TabLayout interfaces

`ViewPager2` introduces changes to [`TabLayout`](https://developer.android.com/reference/com/google/android/material/tabs/TabLayout) integration. If you
currently use a `ViewPager` with a `TabLayout` object to display horizontal
tabs for navigation, you need to refactor the `TabLayout` object for
integration with `ViewPager2`.

`TabLayout` has been decoupled from `ViewPager2` and is now available as part of
[Material components](https://developer.android.com/guide/topics/ui/look-and-feel). This means that in order to use it, you need to add
the appropriate dependency to your `build.gradle` file:

### Groovy

```groovy
implementation "com.google.android.material:material:1.1.0-beta01"
```

### Kotlin

```kotlin
implementation("com.google.android.material:material:1.1.0-beta01")
```

You also need to change the `TabLayout` element's location in the hierarchy of
your XML layout file. With `ViewPager`, the `TabLayout` element is declared as a
child of the `ViewPager` element; but with `ViewPager2`, the `TabLayout` element
is declared directly above the `ViewPager2` element, on the same level:

    <!-- A ViewPager element with a TabLayout -->
    <androidx.viewpager.widget.ViewPager
        xmlns:android="http://schemas.android.com/apk/res/android"
        android:id="@+id/pager"
        android:layout_width="match_parent"
        androi>d:layo<ut_height="match_parent"

        com.google.android.material.tabs.TabLayout
            android:id="@+id/tab_layout"
            android:layout_width="match>_p<arent"
            android:layout_h>ei<ght="wrap_content" /

    /androidx.vi>e<wpager.widget.ViewPager

    !-- A ViewPager2 element with a TabLayout --
    LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
        android:layout_width="matc>h_pare<nt"
        android:layout_height="match_parent"
        android:orientation="vertical"

        com.google.android.material.tabs.TabLayout
            android:i>d=&quo<t;@+id/tab_layout"
            android:layout_width="match_parent"
            android:layout_height="wrap_content" /

        androidx.viewpager2.widget.ViewPager2
           > a<ndroid:id=&qu>ot;@+id/pager"
            android:layout_width="match_parent"
            android:layout_height="0dp"
            android:layout_weight="1" /

    /LinearLayout

Finally, you must update the code that attaches the `TabLayout` object to the
`ViewPager` object. While `TabLayout` uses its own [`setupWithViewPager()`](https://developer.android.com/reference/com/google/android/material/tabs/TabLayout#setupwithviewpager)
method to integrate with `ViewPager`, it requires a [`TabLayoutMediator`](https://developer.android.com/reference/com/google/android/material/tabs/TabLayoutMediator)
instance to integrate with `ViewPager2`.

The `TabLayoutMediator` object also handles the task of generating page titles
for the `TabLayout` object, which means that the adapter class does not need to
override `getPageTitle()`:

### Kotlin

```kotlin
// Integrating TabLayout with ViewPager
class CollectionDemoFragment : Fragment() {
    ...
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        val tabLayout = view.findViewById(R.id.tab_layout)
        tabLayout.setupWithViewPager(viewPager)
    }
    ...
}

class DemoCollectionPagerAdapter(fm: FragmentManager) : FragmentStatePagerAdapter(fm) {

    override fun getCount(): Int  = 4

    override fun getPageTitle(position: Int): CharSequence {
        return "OBJECT ${(position + 1)}"
    }
    ...
}

// Integrating TabLayout with ViewPager2
class CollectionDemoFragment : Fragment() {
    ...
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        val tabLayout = view.findViewById(R.id.tab_layout)
        TabLayoutMediator(tabLayout, viewPager) { tab, position ->
            tab.text = "OBJECT ${(position + 1)}"
        }.attach()
    }
    ...
}
```

### Java

```java
// Integrating TabLayout with ViewPager
public class CollectionDemoFragment extends Fragment {
    ...
    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        TabLayout tabLayout = view.findViewById(R.id.tab_layout);
        tabLayout.setupWithViewPager(viewPager);
    }
    ...
}

public class DemoCollectionPagerAdapter extends FragmentStatePagerAdapter {
    ...
    @Override
    public int getCount() {
        return 4;
    }

    @Override
    public CharSequence getPageTitle(int position) {
        return "OBJECT " + (position + 1);
    }
    ...
}

// Integrating TabLayout with ViewPager2
public class CollectionDemoFragment : Fragment() {
    ...
    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        TabLayout tabLayout = view.findViewById(R.id.tab_layout);
        new TabLayoutMediator(tabLayout, viewPager,
                (tab, position) -> tab.setText("OBJECT " + (position + 1))
        ).attach();
    }
    ...
}
```

### Support nested scrollable elements

`ViewPager2` does not natively support nested scroll views in cases where the
scroll view has the same orientation as the `ViewPager2` object that contains
it. For example, scrolling would not work for a vertical scroll view inside a
vertically-oriented `ViewPager2` object.

To support a scroll view inside a `ViewPager2` object with the same orientation,
you must call
[`requestDisallowInterceptTouchEvent()`](https://developer.android.com/reference/android/view/ViewGroup#requestDisallowInterceptTouchEvent(boolean)) on the `ViewPager2` object when you
expect to scroll the nested element instead. The [ViewPager2 nested scrolling
sample](https://github.com/android/views-widgets-samples/blob/master/ViewPager2/app/src/main/res/layout/item_nested_recyclerviews.xml#L43) demonstrates one way of solving this problem with a versatile
[custom wrapper layout](https://github.com/android/views-widgets-samples/blob/master/ViewPager2/app/src/main/java/androidx/viewpager2/integration/testapp/NestedScrollableHost.kt).

## Additional resources

To learn more about `ViewPager2`, see the following additional resources.

### Samples

- [ViewPager2 samples](https://goo.gle/viewpager2-sample) on GitHub

### Videos

- [Turning the Page: Migrating to ViewPager2](https://www.youtube.com/watch?v=lAP6cz1HSzA) (Android Dev Summit '19)