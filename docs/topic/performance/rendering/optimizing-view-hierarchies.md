---
title: https://developer.android.com/topic/performance/rendering/optimizing-view-hierarchies
url: https://developer.android.com/topic/performance/rendering/optimizing-view-hierarchies
source: md.txt
---

# Performance and view hierarchies

The way you manage the hierarchy of your[View](https://developer.android.com/reference/android/view/View)objects can significantly impact your app's performance. This page describes how to assess whether your view hierarchy is slowing your app down, and offers some strategies for addressing issues that might arise.

This page focuses on improving`View`-based layouts. For information about improving Jetpack Compose performance, see[Jetpack Compose performance](https://developer.android.com/jetpack/compose/performance).

## Layout-and-measure performance

The rendering pipeline includes a*layout-and-measure* stage, during which the system appropriately positions the relevant items in your view hierarchy. The*measure* part of this stage determines the sizes and boundaries of`View`objects. The*layout* part determines where on the screen to position the`View`objects.

Both of these pipeline stages incur some small cost per view or layout that they process. Most of the time, this cost is minimal and doesn't noticeably affect performance. However, it can be greater when an app adds or removes`View`objects, such as when a[RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView)object recycles them or reuses them. The cost can also be higher if a`View`object needs to consider resizing to meet its constraints. For example, if your app calls[SetText()](https://developer.android.com/reference/android/widget/TextView#setText(char[], int, int))on a`View`object that wraps text, the`View`might need to resize.

If cases like these take too long, they can prevent a frame from rendering within the allowed 16ms, which can make frames drop and make animation janky.

Because you can't move these operations to a worker thread---your app must process them on the main thread---it's best to optimize them so that they take as little time as possible.

### Manage complex layouts

Android[Layouts](https://developer.android.com/guide/topics/ui/declaring-layout)let you nest UI objects in the view hierarchy. This nesting can also impose a layout cost. When your app processes an object for layout, the app also performs the same process on all children of the layout.

For a complicated layout, sometimes a cost only arises the first time the system computes the layout. For example, when your app recycles a complex list item in a`RecyclerView`object, the system needs to lay out all of the objects. In another example, trivial changes can propagate up the chain toward the parent until they reach an object that doesn't affect the size of the parent.

A common reason for layout taking a long time is when hierarchies of`View`objects are nested within one another. Each nested layout object adds cost to the layout stage. The flatter your hierarchy, the less time it takes for the layout stage to complete.

We recommend using the[Layout Editor](https://developer.android.com/studio/write/layout-editor#intro)to create a[`ConstraintLayout`](https://developer.android.com/develop/ui/views/layout/constraint-layout), instead of[RelativeLayout](https://developer.android.com/reference/android/widget/RelativeLayout)or[LinearLayout](https://developer.android.com/reference/android/widget/LinearLayout), as it's generally both more efficient and reduces the nesting of layouts. However, for simple layouts that can be achieved using[FrameLayout](https://developer.android.com/reference/android/widget/FrameLayout), we recommend using`FrameLayout`.

If you are using the`RelativeLayout`class, you might be able to achieve the same effect at lower cost by using nested, unweighted`LinearLayout`views instead. However, if you are using nested, weighted`LinearLayout`views, the layout cost is much higher because it requires multiple layout passes, as explained in the next section.

We also recommend using`RecyclerView`instead of[ListView](https://developer.android.com/reference/android/widget/ListView), as it can recycle the layouts of individual list items, which is both more efficient and can improve scrolling performance.

### Double taxation

Typically, the framework executes the layout or measure stage in a single pass. However, with some complicated layout cases, the framework might have to iterate multiple times on parts of the hierarchy that require multiple passes to resolve before ultimately positioning the elements. Having to perform more than one layout-and-measure iteration is referred to as*double taxation*.

For example, when you use the`RelativeLayout`container, which lets you position`View`objects with respect to the positions of other`View`objects, the framework performs the following sequence:

1. Executes a layout-and-measure pass, during which the framework calculates each child object's position and size, based on each child's request.
2. Uses this data, taking object weights into account, to figure out the proper position of correlated views.
3. Performs a second layout pass to finalize the objects' positions.
4. Moves to the next stage of the rendering process.

The more levels your view hierarchy has, the greater the potential for performance penalty.

As mentioned earlier,`ConstraintLayout`is generally more efficient than other layouts except`FrameLayout`. It's less prone to multiple layout passes, and in many cases removes the need to nest layouts.

Containers other than`RelativeLayout`might also increase double taxation. For example:

- A`LinearLayout`view can result in a double layout-and-measure pass if you make it horizontal. A double layout-and-measure pass might also occur in a vertical orientation if you add[measureWithLargestChild](https://developer.android.com/reference/android/widget/LinearLayout#attr_android:measureWithLargestChild), in which case the framework might need to do a second pass to resolve the proper sizes of objects.
- The[GridLayout](https://developer.android.com/reference/android/widget/GridLayout)also allows relative positioning, but it normally avoids double taxation by pre-processing the positional relationships among child views. However, if the layout uses weights or fill with the[Gravity](https://developer.android.com/reference/android/view/Gravity)class, the benefit of preprocessing is lost, and the framework might have to perform multiple passes if the container is a`RelativeLayout`.

Multiple layout-and-measure passes aren't necessarily a performance burden. However, they can become a burden if they're in the wrong place. Be careful with situations where one of the following conditions applies to your container:

- It's a root element in your view hierarchy.
- It has a deep view hierarchy beneath it.
- There are many instances of it populating the screen, similar to children in a`ListView`object.

## Diagnose view hierarchy issues

Layout performance is a complex problem with many facets. The following tools can help you identify where performance bottlenecks are occurring. Some tools provide less definitive information but can provide helpful hints.

### Perfetto

[Perfetto](https://developer.android.com/topic/performance/tracing)is a tool that provides data about performance. You can open Android traces in the[Perfetto UI](https://ui.perfetto.dev/#!/).

### Profile GPU rendering

The on-device[Profile GPU rendering](https://developer.android.com/studio/profile/dev-options-rendering)tool, available on devices powered by Android 6.0 (API level 23) and later, can provide you with concrete information about performance bottlenecks. This tool lets you see how long the layout-and-measure stage is taking for[each frame of rendering](https://youtu.be/erGJw8WDV74). This data can help you diagnose runtime performance issues and help you determine what layout-and-measure issues you need to address.

In its graphical representation of the data it captures, Profile GPU rendering uses the color blue to represent layout time. For more information about how to use this tool, see[Profile GPU rendering speed](https://developer.android.com/studio/profile/dev-options-rendering).

### Lint

Android Studio's[Lint](https://developer.android.com/studio/write/lint)tool can help you gain a sense of inefficiencies in the view hierarchy. To use this tool, select**Analyze \> Inspect Code**, as shown in figure 1.
![](https://developer.android.com/static/topic/performance/images/lint-inspect-code.png)**Figure 1.** Select**Inspect Code**in Android Studio.

Information about various layout items appears under**Android \> Lint \> Performance**. To see more detail, click each item to expand it and display more information in the pane on the right side of the screen. Figure 2 shows an example of expanded information.
![](https://developer.android.com/static/topic/performance/images/lint-display.png)**Figure 2.**Viewing information about specific issues the Lint tool identifies.

Clicking an item reveals problems associated with that item in the pane to the right.

To understand more about specific topics and issues in this area, see the[Lint](https://developer.android.com/studio/write/lint)documentation.

### Layout Inspector

Android Studio's[Layout Inspector](https://developer.android.com/studio/debug/layout-inspector)tool provides a visual representation of your app's view hierarchy. It's a good way to navigate the hierarchy of your app, providing a clear visual representation of a particular view's parent chain, and lets you inspect the layouts that your app constructs.

The views that Layout Inspector presents can also help identify performance problems arising from double taxation. It can also provide a way for you to identify deep chains of nested layouts, or layout areas with a large amount of nested children, which can be a source of performance costs. In these cases, the layout-and-measure stages can be costly and result in performance issues.

For more information, see[Debug your layout with Layout Inspector and Layout Validation](https://developer.android.com/studio/debug/layout-inspector).

## Solve view hierarchy issues

The fundamental concept behind solving performance problems that arise from view hierarchies can be difficult in practice. Preventing view hierarchies from imposing performance penalties consists of flattening your view hierarchy and reducing double taxation. This section discusses strategies for pursuing these goals.

### Remove redundant nested layouts

[ConstraintLayout](https://developer.android.com/reference/androidx/constraintlayout/widget/ConstraintLayout)is a Jetpack library with a large number of different mechanisms for positioning views within the layout. This reduces the need to nest one`ConstaintLayout`and can help flatten the view hierarchy. It is usually simpler to flatten hierarchies using`ConstraintLayout`compared to other layout types.

Developers often use more nested layouts than necessary. For example, a`RelativeLayout`container might contain a single child that is also a`RelativeLayout`container. This nesting is redundant and adds unnecessary cost to the view hierarchy.[Lint](https://developer.android.com/topic/performance/rendering/optimizing-view-hierarchies#lint)can flag this problem for you, reducing debugging time.

### Adopt merge or include

A frequent cause of redundant nested layouts is the[<include>](https://developer.android.com/develop/ui/views/layout/improving-layouts/reusing-layouts)tag. For example, you might define a reusable layout as follows:  

```xml
<LinearLayout>
    <!-- some stuff here -->
</LinearLayout>
```

You might then add an`<include>`tag to add the following item to the parent container:  

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:orientation="vertical"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@color/ap>p_bg&q<uot;
    android:gravity="cen>ter_ho<rizontal"

    include layout="@layout/titlebar"/

    TextView android:layout_width="match_parent"
              android:layout_height="wrap_conte>nt"
  <            <>/span>android:text="@string/hello"
              android:padding="10dp" /

    ...

/LinearLayout
```

The preceding include unnecessarily nests the first layout within the second layout.

The[`<merge>`](https://developer.android.com/develop/ui/views/layout/improving-layouts/reusing-layouts#Merge)tag can help prevent this issue. For information about this tag, see[Use the \<merge\> tag](https://developer.android.com/develop/ui/views/layout/improving-layouts/reusing-layouts#Merge).

### Adopt a cheaper layout

You might not be able to adjust your existing layout scheme so that it doesn't contain redundant layouts. In certain cases, the only solution might be to flatten your hierarchy by switching over to an entirely different layout type.

For example, you might find that[TableLayout](https://developer.android.com/reference/android/widget/TableLayout)provides the same functionality as a more complex layout with many positional dependencies. The Jetpack library[`ConstraintLayout`](https://developer.android.com/reference/androidx/constraintlayout/widget/ConstraintLayout)provides similar functionality to`RelativeLayout`, plus more features to help create flatter, more efficient layouts.