---
title: https://developer.android.com/training/wearables/views/screens
url: https://developer.android.com/training/wearables/views/screens
source: md.txt
---

# App layouts

Try the Compose way  
Jetpack Compose on Wear OS is the recommended UI toolkit for Wear OS.  
[Handle different screen sizes using Compose on Wear OS →](https://developer.android.com/training/wearables/compose/screen-size)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)

After you understand how to[handle different watch shapes](https://developer.android.com/training/wearables/apps/layouts), decide which surface you want to use.

Common app layouts include the following:

- Single screen (simplest): UI elements are limited to what is visible at one time without scrolling.
- Vertical container (most common): content exists beyond the viewable portion of the screen and is accessible by scrolling.
- Other options: lists, paging, or 2D panning.

These layout types are described in the sections that follow. You can use a combination of layout types if you need multiple screens.

**Note:** For your activity, inherit from either a`ComponentActivity`or, if you use fragments, a`FragmentActivity`. The other activity types use mobile-specific UI elements that you don't need for Wear OS.

## Single screen

The user sees all elements in a single screen without scrolling. This means you can include only a small number of elements.
![](https://developer.android.com/static/wear/images/screen_opts_4.png)

**Figure 1.**An example of a single screen layout.

Single screens work well with a[BoxInsetLayout](https://developer.android.com/reference/androidx/wear/widget/BoxInsetLayout)in combination with a[ConstraintLayout](https://developer.android.com/reference/androidx/constraintlayout/widget/ConstraintLayout)to arrange your elements.

## Vertical container

A vertical container is the most common type of app layout. Some content isn't visible on the screen, but it is accessible by scrolling.

Figure 2 shows several complete app layouts in which only a portion of the content can be seen on the circular screen of a watch. In these examples, the main content is in the top portion of the container, and other Critical User Journeys (CUJs) and settings are at the bottom. This is a best practice for laying out content.
![](https://developer.android.com/static/wear/images/screen_opts_2.png)

**Figure 2.**Examples of vertical container layouts.

Unlike in a single screen app layout, don't use`BoxInsetLayout`. Instead, use a`ConstraintLayout`inside a[NestedScrollView](https://developer.android.com/reference/androidx/core/widget/NestedScrollView). Inside the`ConstraintLayout`, place whatever widgets make the most sense for your app. This lets you take advantage of the extra space on the sides of a circular display.
![](https://developer.android.com/static/wear/images/screen_opts_3.gif)

**Figure 3.** Content in a`ConstraintLayout`inside a`NestedScrollView`.

Make sure the content at the top and bottom of your vertical container is small enough to fit in the top and bottom of a circular display, as in the example in figure 3.

**Note:** When possible, add a scroll indicator to your`NestedScrollView`by setting`android:scrollbars="vertical"`in the XML. This helps users identify that there is more content available and helps them see where they are in relation to all the content.

## Other options for app layouts

- **Lists** : display large sets of data with the`WearableRecyclerView`widget optimized for Wearable surfaces. For more information, see[Create lists on Wear OS](https://developer.android.com/training/wearables/apps/lists).
- **Horizontal paging** : for use cases with multiple sibling screens, use a[horizontal swipe](https://developer.android.com/guide/navigation/navigation-swipe-view-2). If you use horizontal paging, you must support swipe-to-dismiss for the left edge.
- **2D Panning** : for use cases like maps, users can[drag to pan](https://developer.android.com/training/gestures/scale#pan)in different directions. Enable[swipe-to-dismiss](https://developer.android.com/training/wearables/apps/exit#swipe-to-dismiss)if your activity takes up the entire screen.