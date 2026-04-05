---
title: Add a floating action button  |  Views  |  Android Developers
url: https://developer.android.com/develop/ui/views/components/floating-action-button
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Views](https://developer.android.com/develop/ui/views/layout/declaring-layout)

# Add a floating action button Stay organized with collections Save and categorize content based on your preferences.



Try the Compose way

Jetpack Compose is the recommended UI toolkit for Android. Learn how to add components in Compose.

[Floating Action Button →](https://developer.android.com/develop/ui/compose/components/fab)

![](/static/images/android-compose-ui-logo.png)

A floating action button (FAB) is a circular button that triggers the primary
action in your app's UI. This document shows how to add a FAB to your layout,
customize some of its appearance, and respond to button taps.

To learn more about how to design a FAB for your app according to the Material
Design Guidelines, see [Material Design
FAB](https://m3.material.io/components/floating-action-button/overview)
.

![An image showing an app screen containing a red FloatingActionButton](/static/training/material/images/fab.png)


**Figure 1.** A floating action button (FAB).

## Add the floating action button to your layout

The following code shows how the
[`FloatingActionButton`](/reference/com/google/android/material/floatingactionbutton/FloatingActionButton)
appears in your layout file:

```
<com.google.android.material.floatingactionbutton.FloatingActionButton
        android:id="@+id/fab"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_gravity="end|bottom"
        android:src="@drawable/ic_my_icon"
        android:contentDescription="@string/submit"
        android:layout_margin="16dp" />
```

By default, a FAB is colored by the `colorAccent` attribute, which you can
[customize with the theme's color
palette](/guide/topics/ui/look-and-feel/themes#ColorPalette).

You can configure other FAB properties using XML attributes or corresponding
methods, such as the following:

* The size of the FAB, using the `app:fabSize` attribute or the
  [`setSize()`](/reference/com/google/android/material/floatingactionbutton/FloatingActionButton#setSize(int))
  method
* The ripple color of the FAB, using the `app:rippleColor` attribute or the
  [`setRippleColor()`](/reference/com/google/android/material/floatingactionbutton/FloatingActionButton#setRippleColor(int))
  method
* The FAB icon, using the `android:src` attribute or the
  [`setImageDrawable()`](/reference/android/widget/ImageView#setImageDrawable(android.graphics.drawable.Drawable))
  method

## Respond to button taps

You can then apply an
[`View.OnClickListener`](/reference/android/view/View.OnClickListener) to
handle FAB taps. For example, the following code displays a
[`Snackbar`](/reference/com/google/android/material/snackbar/Snackbar) when
the user taps the FAB:

### Kotlin

```
val fab: View = findViewById(R.id.fab)
fab.setOnClickListener { view ->
    Snackbar.make(view, "Here's a Snackbar", Snackbar.LENGTH_LONG)
            .setAction("Action", null)
            .show()
}
```

### Java

```
FloatingActionButton fab = findViewById(R.id.fab);
fab.setOnClickListener(new View.OnClickListener() {
    @Override
    public void onClick(View view) {
        Snackbar.make(view, "Here's a Snackbar", Snackbar.LENGTH_LONG)
                .setAction("Action", null).show();
    }
});
```

For more information about the capabilities of the FAB, see the API reference
for the
[`FloatingActionButton`](/reference/com/google/android/material/floatingactionbutton/FloatingActionButton).