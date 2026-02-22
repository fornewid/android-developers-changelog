---
title: https://developer.android.com/develop/ui/views/layout/recyclerview-custom
url: https://developer.android.com/develop/ui/views/layout/recyclerview-custom
source: md.txt
---

# Customize a dynamic list
Part of [Android Jetpack](https://developer.android.com/jetpack).

Try the Compose way  
Jetpack Compose is the recommended UI toolkit for Android. Learn how to work with layouts in Compose.  
[Lazy Lists and Grids →](https://developer.android.com/jetpack/compose/lists#lazy)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)

You can customize
[RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView)
objects to meet your specific needs. The standard classes described in
[Create dynamic lists with
RecyclerView](https://developer.android.com/guide/topics/ui/layout/recyclerview) provide all the functionality that most developers need. In
many cases, you only need to design the view for each view holder and write the
code to update those views with the appropriate data. However, if your app has
specific requirements, you can modify the standard behavior in a number of ways.
This document describes some of the possible customizations.

## Modify the layout

`RecyclerView` uses a layout manager to position the individual
items on the screen and to determine when to reuse item views that are no longer
visible to the user. To reuse---or *recycle* ---a view, a layout
manager might ask the adapter to replace the contents of the view with a
different element from the dataset. Recycling views this way improves
performance by avoiding the creation of unnecessary views or performing
expensive
[findViewById()](https://developer.android.com/reference/android/app/Activity#findViewById(int))
lookups. The Android Support Library includes three standard layout managers,
ach of which offers many customization options:

- [LinearLayoutManager](https://developer.android.com/reference/androidx/recyclerview/widget/LinearLayoutManager): arranges the items in a one-dimensional list. Using a `RecyclerView` with `LinearLayoutManager` provides functionality like a [ListView](https://developer.android.com/reference/android/widget/ListView) layout.
- [GridLayoutManager](https://developer.android.com/reference/androidx/recyclerview/widget/GridLayoutManager): arranges the items in a two-dimensional grid, like the squares on a checkerboard. Using a `RecyclerView` with `GridLayoutManager` provides functionality like a [GridView](https://developer.android.com/reference/android/widget/GridView) layout.
- [StaggeredGridLayoutManager](https://developer.android.com/reference/androidx/recyclerview/widget/StaggeredGridLayoutManager): arranges the items in a two-dimensional grid, with each column slightly offset from the one before, like the stars on an American flag.

If these layout managers don't suit your needs, you can create your own by
extending the
[RecyclerView.LayoutManager](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView.LayoutManager)
abstract class.

## Add item animations

Whenever an item changes, `RecyclerView` uses an *animator*
to change its appearance. This animator is an object that extends the abstract
[RecyclerView.ItemAnimator](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView.ItemAnimator)
class. By default, the `RecyclerView` uses
[DefaultItemAnimator](https://developer.android.com/reference/androidx/recyclerview/widget/DefaultItemAnimator)
to provide the animation. If you want to provide custom animations, you can
define your own animator object by extending
`RecyclerView.ItemAnimator`.

## Enable list-item selection

The
[`recyclerview-selection`](https://developer.android.com/reference/androidx/recyclerview/selection/package-summary)
library lets users select items in a `RecyclerView` list using touch
or mouse input. This lets you retain control over the visual presentation of a
selected item. You can also retain control over policies controlling selection
behavior, such as which items are eligible for selection and how many items can
be selected.

To add selection support to a `RecyclerView` instance, follow
these steps:

1. Determine which selection key type to use, then build an [`ItemKeyProvider`](https://developer.android.com/reference/androidx/recyclerview/selection/ItemKeyProvider).

   There are three key types you can use to identify selected items:
   - [Parcelable](https://developer.android.com/reference/android/os/Parcelable) and its subclasses, like [Uri](https://developer.android.com/reference/android/net/Uri)
   - [String](https://developer.android.com/reference/java/lang/String)
   - [Long](https://developer.android.com/reference/java/lang/Long)

   For detailed information about selection-key types, see
   [SelectionTracker.Builder](https://developer.android.com/reference/androidx/recyclerview/selection/SelectionTracker.Builder).
2. Implement [ItemDetailsLookup](https://developer.android.com/reference/androidx/recyclerview/selection/ItemDetailsLookup).
3. `ItemDetailsLookup` lets the selection library access information about `RecyclerView` items given a [MotionEvent](https://developer.android.com/reference/android/view/MotionEvent). It is effectively a factory for [`ItemDetails`](https://developer.android.com/reference/androidx/recyclerview/selection/ItemDetailsLookup.ItemDetails) instances that are backed up by, or extracted from, a [RecyclerView.ViewHolder](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView.ViewHolder) instance.
4. Update item [View](https://developer.android.com/reference/android/view/View) objects in the `RecyclerView` to reflect whether the user selects or unselects them.

   The selection library doesn't provide a default visual decoration for the
   selected items. Provide this when you implement
   [onBindViewHolder()](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView.Adapter#onBindViewHolder(VH, int)).
   We recommend the following approach:
   - In `onBindViewHolder()`, call [setActivated()](https://developer.android.com/reference/android/view/View#setActivated(boolean))---**not** [setSelected()](https://developer.android.com/reference/android/view/View#setSelected(boolean))---on the `View` object with `true` or `false`, depending on whether the item is selected.
   - Update the styling of the view to represent the activated status. We recommend using a [color state
     list resource](https://developer.android.com/guide/topics/resources/color-list-resource) to configure the styling.
5. Use [ActionMode](https://developer.android.com/reference/androidx/appcompat/view/ActionMode) to provide the user with tools to perform an action on the selection.
6. Register a [SelectionTracker.SelectionObserver](https://developer.android.com/reference/androidx/recyclerview/selection/SelectionTracker.SelectionObserver) to be notified when a selection changes. When a selection is first created, start `ActionMode` to present this to the user and provide selection-specific actions. For example, you can add a delete button to the `ActionMode` bar and connect the back arrow on the bar to clear the selection. When the selection becomes empty---if the user clears the selection the last time---terminate action mode.
7. Perform any interpreted secondary actions.
8. At the end of the event processing pipeline, the library might determine that the user is attempting to activate an item, by tapping it, or is attempting to drag an item or set of selected items. React to these interpretations by registering the appropriate listener. For more information, see [SelectionTracker.Builder](https://developer.android.com/reference/androidx/recyclerview/selection/SelectionTracker.Builder).
9. Assemble everything with `SelectionTracker.Builder`.
10. The following example shows how to put these pieces together:  

### Kotlin

```kotlin
    var tracker = SelectionTracker.Builder(
        "my-selection-id",
        recyclerView,
        StableIdKeyProvider(recyclerView),
        MyDetailsLookup(recyclerView),
        StorageStrategy.createLongStorage())
            .withOnItemActivatedListener(myItemActivatedListener)
            .build()
    
```

### Java

```java
    SelectionTracker tracker = new SelectionTracker.Builder<>(
            "my-selection-id",
            recyclerView,
            new StableIdKeyProvider(recyclerView),
            new MyDetailsLookup(recyclerView),
            StorageStrategy.createLongStorage())
            .withOnItemActivatedListener(myItemActivatedListener)
            .build();
    
```
11. To build a [SelectionTracker](https://developer.android.com/reference/androidx/recyclerview/selection/SelectionTracker) instance, your app must supply the same [RecyclerView.Adapter](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView.Adapter) that you use to initialize `RecyclerView` to `SelectionTracker.Builder`. For this reason, after you create the `SelectionTracker` instance, inject it into your `RecyclerView.Adapter`. Otherwise, you can't check an item's selected status from the `onBindViewHolder()` method.
12. Include selection in the [activity
    lifecycle](https://developer.android.com/guide/components/activities/activity-lifecycle) events.
13. To preserve selection state across the activity lifecycle events, your app must call the selection tracker's [onSaveInstanceState()](https://developer.android.com/reference/androidx/recyclerview/selection/SelectionTracker#onSaveInstanceState(android.os.Bundle)) and [onRestoreInstanceState()](https://developer.android.com/reference/androidx/recyclerview/selection/SelectionTracker#onRestoreInstanceState(android.os.Bundle)) methods from the activity's [onSaveInstanceState()](https://developer.android.com/reference/android/app/Activity#onSaveInstanceState(android.os.Bundle)) and [onRestoreInstanceState()](https://developer.android.com/reference/android/app/Activity#onRestoreInstanceState(android.os.Bundle)) methods, respectively. Your app must also supply a unique selection ID to the `SelectionTracker.Builder` constructor. This ID is required because an activity or a fragment might have more than one distinct, selectable list, all of which need to be persisted in their saved state.

## Additional resources

See the following references for additional information.

- [Sunflower
  demo app](https://github.com/googlesamples/android-sunflower), which uses `RecyclerView`.
- [Use
  RecyclerView to display a scrollable list](https://developer.android.com/codelabs/basic-android-kotlin-training-recyclerview-scrollable-list#0) codelab.
- [Android
  Kotlin Fundamentals: RecyclerView fundamentals](https://developer.android.com/codelabs/kotlin-android-training-recyclerview-fundamentals) codelab.