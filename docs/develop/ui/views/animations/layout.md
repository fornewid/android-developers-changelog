---
title: Auto-animate layout updates  |  Views  |  Android Developers
url: https://developer.android.com/develop/ui/views/animations/layout
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Views](https://developer.android.com/develop/ui/views/layout/declaring-layout)

# Auto-animate layout updates Stay organized with collections Save and categorize content based on your preferences.



Android offers preloaded animation that runs when you change the layout. Set an attribute in the
layout to tell the Android system to animate these layout changes, and it carries out system-default
animations for you.

**Tip**: If you want to supply custom layout animations, create a
`LayoutTransition`
object and supply it to the layout with the
`setLayoutTransition()`
method.

Here's what a default layout animation looks like when adding items to a list:

[



](/static/develop/ui/views/animations/anim_layout_changes.mp4)

**Figure 1.** Layout animation.

## Create the layout

In your activity's layout XML file, set the `android:animateLayoutChanges` attribute
to `true` for the layout that you want to enable animations for:

```
<LinearLayout android:id="@+id/container"
    android:animateLayoutChanges="true"
    ...
/>
```

## Add, update, or remove items from the layout

Add, remove, or update items in the layout, and the items are animated automatically:

### Kotlin

```
lateinit var containerView: ViewGroup
...
private fun addItem() {
    val newView: View = ...

    containerView.addView(newView, 0)
}
```

### Java

```
private ViewGroup containerView;
...
private void addItem() {
    View newView;
    ...
    containerView.addView(newView, 0);
}
```