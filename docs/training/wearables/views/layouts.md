---
title: https://developer.android.com/training/wearables/views/layouts
url: https://developer.android.com/training/wearables/views/layouts
source: md.txt
---

Try the Compose way  
Jetpack Compose on Wear OS is the recommended UI toolkit for Wear OS.  
[Try Compose on Wear OS →](https://developer.android.com/training/wearables/compose)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)


Apps on Wear OS use the same layout techniques as other Android devices
but need to be designed with watch-specific constraints.


**Note:** Don't port the exact functionality and UI from a mobile app to Wear OS and expect
a good user experience.


If you design your app for a rectangular handheld device, content near the corners of the screen
might be cropped on round watches. If you are using a scrollable vertical list, this is less of
an issue, as the user can scroll to center the content. However, for single screens, it can
provide a bad user experience.


If you use the following settings for your layout, text displays incorrectly on devices
with round screens:  

```xml
<androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <TextView
        android:id="@+id/text"
        android:layout_width="0dp"
        android:layout_height="0dp"
        android:text="@string/very_long_hello_world"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

</androidx.constraintlayout.widget.ConstraintLayout>
```


To solve this problem, use layouts in the [Wear OS UI Library](https://developer.android.com/training/wearables/views) that support round devices.

- You can use a [`BoxInsetLayout`](https://developer.android.com/reference/androidx/wear/widget/BoxInsetLayout) to prevent views from being cropped near the edges of round screens.
- You can use a [WearableRecyclerView](https://developer.android.com/reference/androidx/wear/widget/WearableRecyclerView) to create a curved layout when you want to display and manipulate a vertical list of items optimized for round screens.


For more information about designing apps, read the
[Wear OS design guidelines](https://developer.android.com/training/wearables/design).

## Use a BoxInsetLayout

![](https://developer.android.com/static/wear/images/02_uilib.png)


**Figure 2.** Window insets on a round screen.


The [`BoxInsetLayout`](https://developer.android.com/reference/androidx/wear/widget/BoxInsetLayout) class in the Wear OS UI Library lets
you define a layout that works for round screens. This class lets you
easily align views on the center or near the edges of the screen.


The gray square in figure 2 shows the area where the `BoxInsetLayout`
can automatically place its child views on round screens after applying
the required window insets. To be displayed inside this area, child
views specify the `layout_boxedEdges` attribute with the following values:

- A combination of `top`, `bottom`, `left`, and `right`. For example, a `"left|top"` value positions the child's left and top edges inside the gray square in figure 2.
- The `"all"` value positions all the child's content inside the gray square in figure 2. This is the most common approach with a [`ConstraintLayout`](https://developer.android.com/reference/androidx/constraintlayout/widget/ConstraintLayout) inside.


The layout shown in figure 2 uses the `<BoxInsetLayout>`
element and works on round screens:  

```xml
<androidx.wear.widget.BoxInsetLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_height="match_parent"
    android:layout_width="match_parent"
    android:padding="15dp">

    <androidx.constraintlayout.widget.ConstraintLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:padding="5dp"
        app:layout_boxedEdges="all">

        <TextView
            android:layout_height="wrap_content"
            android:layout_width="match_parent"
            android:text="@string/sometext"
            android:textAlignment="center"
            app:layout_constraintEnd_toEndOf="parent"
            app:layout_constraintStart_toStartOf="parent"
            app:layout_constraintTop_toTopOf="parent" />

        <ImageButton
            android:background="@android:color/transparent"
            android:layout_height="50dp"
            android:layout_width="50dp"
            app:layout_constraintBottom_toBottomOf="parent"
            app:layout_constraintStart_toStartOf="parent"
            android:src="@drawable/cancel" />

        <ImageButton
            android:background="@android:color/transparent"
            android:layout_height="50dp"
            android:layout_width="50dp"
            app:layout_constraintBottom_toBottomOf="parent"
            app:layout_constraintEnd_toEndOf="parent"
            android:src="@drawable/ok" />

    </androidx.constraintlayout.widget.ConstraintLayout>

</androidx.wear.widget.BoxInsetLayout>
```


Notice the parts of the layout marked in bold:

-
  `android:padding="15dp"`


  This line assigns padding to the `<BoxInsetLayout>`
  element.
-
  `android:padding="5dp"`


  This line assigns padding to the inner `ConstraintLayout` element.
-
  `app:layout_boxedEdges="all"`


  This line ensures that the `ConstraintLayout` element
  and its children are boxed inside the area defined by the window
  insets on round screens.

## Use a curved layout

The [WearableRecyclerView](https://developer.android.com/reference/androidx/wear/widget/WearableRecyclerView) class in the Wear OS UI Library
lets you opt-in to a curved layout optimized for round screens.
To enable a curved layout for scrollable lists in your
app, see [Create lists on Wear OS](https://developer.android.com/training/wearables/ui/lists#creating).