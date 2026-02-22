---
title: https://developer.android.com/develop/ui/views/layout/improving-layouts/reusing-layouts
url: https://developer.android.com/develop/ui/views/layout/improving-layouts/reusing-layouts
source: md.txt
---

Try the Compose way Jetpack Compose is the recommended UI toolkit for Android. Learn how to work with layouts in Compose. [Slot-based layouts →](https://developer.android.com/develop/ui/compose/layouts/basics#slot-based-layouts) ![](https://developer.android.com/static/images/android-compose-ui-logo.png)

Although Android offers a variety of widgets to provide small, reusable, interactive elements,
you might also need to reuse larger components that require a special layout. To efficiently reuse
complete layouts, use the `<include>` and `<merge>` tags to embed
one layout inside another.

This lets you create complex layouts---such as a yes or no button panel or a custom progress
bar with description text. And it means that you can extract any elements of your application that
are common across multiple layouts, manage them separately, and include them in each layout. While
you can create individual UI components by writing a custom
`https://developer.android.com/reference/android/view/View`, you can do it more easily by
reusing a layout file.

## Create a reusable layout

Start by creating a new XML file and defining the layout you want to be able to reuse. For
example, here's a layout that defines a title bar to include in each activity
(`titlebar.xml`):

```xml
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:background="@color/titlebar_bg"
    tools:showIn="@layout/activity_main" >

    <ImageView android:layout_width="wrap_content"
               android:layout_height="wrap_content"
               android:src="@drawable/gafricalogo" />
</FrameLayout>
```

The root `View` must be exactly how you want it to appear in each
layout where you plan to add this layout.
| **Note:** The [`tools:showIn`](https://developer.android.com/studio/write/tool-attributes#toolsshowin) attribute in the preceding XML file is a special attribute that is used only at design time in Android Studio and is removed during compilation. It specifies a layout that *includes* this file, so you can preview and edit this file as it appears while embedded in a parent layout.

## Use the \<include\> tag

Inside the layout where you want to add the reusable component, add the
`<include>` tag. For example, here's a layout that includes the title bar from
the preceding example:

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:orientation="vertical"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@color/app_bg"
    android:gravity="center_horizontal">

    <include layout="@layout/titlebar"/>

    <TextView android:layout_width="match_parent"
              android:layout_height="wrap_content"
              android:text="@string/hello"
              android:padding="10dp" />
    ...
</LinearLayout>
```

You can also override all the layout parameters---any `android:layout_*`
attributes---of the included layout's root view by specifying them in the
`<include>` tag. This is shown in the following example:

```xml
<include android:id="@+id/news_title"
         android:layout_width="match_parent"
         android:layout_height="match_parent"
         layout="@layout/title"/>
```

However, if you want to override layout attributes using the `<include>` tag,
also override `android:layout_height` and `android:layout_width` to make the
other layout attributes take effect.

## Use the \<merge\> tag

The `<merge>` tag helps eliminate redundant view groups in your view hierarchy
when including one layout within another. One use case of `<merge>` is when you
implement a custom view by extending a `ViewGroup`.

For example, if your main layout is a vertical
`https://developer.android.com/reference/android/widget/LinearLayout` in which two
consecutive views can be reused in multiple layouts, then the reusable layout where you place the
two views requires its own root view. However, using another `LinearLayout` as the root
for the reusable layout results in a vertical `LinearLayout` inside a vertical
`LinearLayout`. The nested `LinearLayout` serves no real purpose and slows
down your UI performance.

Instead, you can extend a `LinearLayout` to create a custom view and use a layout XML
to describe its child views. The top tag in the XML is `<merge>`, rather than
`LinearLayout`, as shown in the following example:

```xml
<merge xmlns:android="http://schemas.android.com/apk/res/android">

    <Button
        android:layout_width="fill_parent"
        android:layout_height="wrap_content"
        android:text="@string/add"/>

    <Button
        android:layout_width="fill_parent"
        android:layout_height="wrap_content"
        android:text="@string/delete"/>

</merge>
```

When you include this layout in another layout---using the `<include>`
tag---the system ignores the `<merge>` element and places the two buttons
directly in the layout, in place of the `<include>` tag.

For more information about `<include>`, see
[Layout resource](https://developer.android.com/guide/topics/resources/layout-resource#include-element).