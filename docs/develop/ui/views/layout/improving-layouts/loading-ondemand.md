---
title: https://developer.android.com/develop/ui/views/layout/improving-layouts/loading-ondemand
url: https://developer.android.com/develop/ui/views/layout/improving-layouts/loading-ondemand
source: md.txt
---

Sometimes your layout requires complex views that are rarely used. Whether
they are item details, progress indicators, or undo messages, you can reduce
memory usage and speed up rendering by loading the views only when they're
needed.

You can defer loading resources when you have complex views that your app
needs in the future by defining a
`https://developer.android.com/reference/android/view/ViewStub` for
complex and rarely used views.

## Define a ViewStub

`ViewStub` is a lightweight view with no dimension that doesn't
draw anything or participate in the layout. As such, it requires few resources
to inflate and leave in a view hierarchy. Each `ViewStub` includes
the `android:layout` attribute to specify the layout to inflate.

Suppose you have a layout you want to load later in the user journey of your
app:

```transact-sql
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <ImageView
        android:src="@drawable/logo"
        android:layout_width="match_parent"
        android:layout_height="match_parent"/>
</FrameLayout>
```

You can postpone loading using the following `ViewStub`. To make
it show or load anything, you must make it show the referred layout:

```xml
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
android:id="@+id/root"
android:layout_width="match_parent"
android:layout_height="match_parent">

<ViewStub
    android:id="@+id/stub_import"
    android:inflatedId="@+id/panel_import"
    android:layout="@layout/heavy_layout_we_want_to_postpone"
    android:layout_width="fill_parent"
    android:layout_height="wrap_content"
    android:layout_gravity="bottom" />
</FrameLayout>
```

## Load the ViewStub layout

The code snippets in the previous section produce something like figure
1:
![An image of a empty screen](https://developer.android.com/static/images/ui/viewstub_1.png) **Figure 1.** Initial state of the screen: the `ViewStub` is hiding the heavy layout.

When you want to load the layout specified by the `ViewStub`,
either set it to visible by calling
`https://developer.android.com/reference/android/view/View#setVisibility(int)`
or call
`https://developer.android.com/reference/android/view/ViewStub#inflate()`.

The following code snippet simulates a postponed load. The screen loads as
usual in the `Activity` and `onCreate()`, then it shows
the `heavy_layout_we_want_to_postpone` layout:

### Kotlin

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
  super.onCreate(savedInstanceState)
  setContentView(R.layout.activity_old_xml)

  Handler(Looper.getMainLooper())
      .postDelayed({
          findViewById<View>(R.id.stub_import).visibility = View.VISIBLE
          
          // Or val importPanel: View = findViewById<ViewStub>(R.id.stub_import).inflate()
      }, 2000)
}
```

### Java

```java
@Override
void onCreate(savedInstanceState: Bundle?) {
  super.onCreate(savedInstanceState);
  setContentView(R.layout.activity_old_xml);

  Handler(Looper.getMainLooper())
      .postDelayed({
          findViewById<View>(R.id.stub_import).visibility = View.VISIBLE
          
          // Or val importPanel: View = findViewById<ViewStub>(R.id.stub_import).inflate()
      }, 2000);
}
```
![](https://developer.android.com/static/images/ui/viewstub_2.png) **Figure 2.** The heavy layout is visible. **Note:** The `inflate()` method returns the inflated `View` after it's complete, so you don't need to call `https://developer.android.com/reference/android/app/Activity#findViewById(int)` if you need to interact with the layout.

Once visible or inflated, the `ViewStub` element is no longer part
of the view hierarchy. It is replaced by the inflated layout, and the ID for the
root view of that layout is specified by the `android:inflatedId`
attribute of the `ViewStub`. The ID `android:id` specified
for the `ViewStub` is valid only until the `ViewStub`
layout is visible or inflated.
| **Note:** A drawback of `ViewStub` is that it doesn't support the `<merge>` tag in the layouts to be inflated.

For more information about this topic, see the blog post
[Optimize
with stubs](http://android-developers.blogspot.com/2009/03/android-layout-tricks-3-optimize-with.html).