---
title: Capture a heap dump (Views)  |  Android Developers
url: https://developer.android.com/studio/profile/views/capture-heap-dump-views
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio](https://developer.android.com/studio)
* [Views](https://developer.android.com/studio/profile/views/capture-heap-dump-views)

# Capture a heap dump (Views) Stay organized with collections Save and categorize content based on your preferences.





[Jetpack Compose implementationarrow\_forward](/studio/profile/capture-heap-dump)

This page includes information about finding and triggering memory leaks that is
unique to View-based layouts. For the core information about capturing and
analyzing heap dumps, see [Capture a heap dump](/studio/profile/capture-heap-dump).

## Find memory leaks

To quickly filter to classes that might be associated with memory leaks, open
the class drop-down and select **Show activity/fragment leaks**. Android Studio
shows classes that it thinks indicate memory leaks for
[`Activity`](/reference/android/app/Activity) and
[`Fragment`](/reference/android/app/Fragment) instances in your app. The types
of data that the filter shows include the following:

* `Activity` instances that have been destroyed but are still being referenced.
* `Fragment` instances that don't have a valid
  [`FragmentManager`](/reference/android/app/FragmentManager) but are still
  being referenced.

Be aware that the filter might yield false positives in the following
situations:

* A `Fragment` is created but has not yet been used.
* A `Fragment` is being cached but not as part of a
  [`FragmentTransaction`](/reference/android/app/FragmentTransaction).

To look for memory leaks more manually, browse the class and instance lists to
find objects with large **Retained Size**. Look for memory leaks caused by any
of the following:

* Long-lived references to [`Activity`](/reference/android/app/Activity),
  [`Context`](/reference/android/content/Context),
  [`View`](/reference/android/view/View),
  [`Drawable`](/reference/android/graphics/drawable/Drawable), and other objects
  that might hold a reference to the `Activity` or `Context` container.
* Non-static inner classes, such as a
  [`Runnable`](/reference/java/lang/Runnable), that can hold an `Activity`
  instance.
* Caches that hold objects longer than necessary.

When you find potential memory leaks, use the **Fields** and **References** tabs
in **Instance Details** to jump to the instance or source code line of interest.

## Trigger memory leaks for testing

To provoke memory leaks to test in your app, you can trigger leaks in one of
the following ways:

* Rotate the device from portrait to landscape and back again multiple times
  while in different activity states. Rotating the device can often cause an app
  to leak an [`Activity`](/reference/android/app/Activity),
  [`Context`](/reference/android/content/Context), or
  [`View`](/reference/android/view/View) object because the system recreates the
  `Activity`, and if your app holds a reference to one of those objects
  somewhere else, the system can't garbage collect it.
* Switch between your app and another app while in different activity states.
  For example, navigate to the home screen, then return to your app.