---
title: https://developer.android.com/develop/ui/views/animations/layout
url: https://developer.android.com/develop/ui/views/animations/layout
source: md.txt
---

# Auto-animate layout updates

Android offers preloaded animation that runs when you change the layout. Set an attribute in the layout to tell the Android system to animate these layout changes, and it carries out system-default animations for you.
| **Tip** : If you want to supply custom layout animations, create a[LayoutTransition](https://developer.android.com/reference/android/animation/LayoutTransition)object and supply it to the layout with the[setLayoutTransition()](https://developer.android.com/reference/android/view/ViewGroup#setLayoutTransition(android.animation.LayoutTransition))method.

Here's what a default layout animation looks like when adding items to a list:  
**Figure 1.** Layout animation.  

## Create the layout

In your activity's layout XML file, set the`android:animateLayoutChanges`attribute to`true`for the layout that you want to enable animations for:  

```xml
<LinearLayout android:id="@+id/container"
    android:animateLayoutChanges="true"
    ...
/>
```

## Add, update, or remove items from the layout

Add, remove, or update items in the layout, and the items are animated automatically:  

### Kotlin

```kotlin
lateinit var containerView: ViewGroup
...
private fun addItem() {
    val newView: View = ...

    containerView.addView(newView, 0)
}
```

### Java

```java
private ViewGroup containerView;
...
private void addItem() {
    View newView;
    ...
    containerView.addView(newView, 0);
}
```