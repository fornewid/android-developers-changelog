---
title: https://developer.android.com/training/backward-compatible-ui/using-component
url: https://developer.android.com/training/backward-compatible-ui/using-component
source: md.txt
---

# Use the version-aware component

Now that you have two implementations of`TabHelper`and`CompatTab`---one for Android 3.0 and later and one for earlier versions of the platform---it's time to do something with these implementations. This lesson discusses creating the logic for switching between these implementations, creating version-aware layouts, and finally using the backward-compatible UI component.

## Add the switching logic

The`TabHelper`abstract class acts as a[factory](https://en.wikipedia.org/wiki/Factory_(software_concept))for creating version-appropriate`TabHelper`and`CompatTab`instances, based on the current device's platform version:  

### Kotlin

```kotlin
sealed class TabHelper(protected val mActivity: FragmentActivity, protected val tag: String) {

    abstract fun setUp()

    abstract fun addTab(tab: CompatTab)

    // Usage is tabHelper.newTab("tag")
    fun newTab(tag: String): CompatTab =
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.HONEYCOMB) {
                CompatTabHoneycomb(mActivity, tag)
            } else {
                CompatTabEclair(mActivity, tag)
            }

    companion object {
        // Usage is TabHelper.createInstance(activity)
        fun createInstance(activity: FragmentActivity): TabHelper =
                if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.HONEYCOMB) {
                    TabHelperHoneycomb(activity)
                } else {
                    TabHelperEclair(activity)
                }
    }
}
```

### Java

```java
public abstract class TabHelper {
    ...
    // Usage is TabHelper.createInstance(activity)
    public static TabHelper createInstance(FragmentActivity activity) {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.HONEYCOMB) {
            return new TabHelperHoneycomb(activity);
        } else {
            return new TabHelperEclair(activity);
        }
    }

    // Usage is tabHelper.newTab("tag")
    public CompatTab newTab(String tag) {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.HONEYCOMB) {
            return new CompatTabHoneycomb(mActivity, tag);
        } else {
            return new CompatTabEclair(mActivity, tag);
        }
    }
    ...
}
```

## Create a version-aware activity layout

The next step is to provide layouts for your activity that can support the two tab implementations. For the older implementation (`TabHelperEclair`), you need to ensure that your activity layout contains a[TabWidget](https://developer.android.com/reference/android/widget/TabWidget)and[TabHost](https://developer.android.com/reference/android/widget/TabHost), along with a container for tab contents:

**res/layout/main.xml:**  

```xml
<!-- This layout is for API level 5-10 only. -->
<TabHost xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@android:id/tabhost"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <LinearLayout
        android:orientation="vertical"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:padding="5dp">

        <TabWidget
            android:id="@android:id/tabs"
            android:layout_width="match_parent"
            android:layout_height="wrap_content" />

        <FrameLayout
            android:id="@android:id/tabcontent"
            android:layout_width="match_parent"
            android:layout_height="0dp"
            android:layout_weight="1" />

    </LinearLayout>
</TabHost>
```

For the`TabHelperHoneycomb`implementation, all you need is a[FrameLayout](https://developer.android.com/reference/android/widget/FrameLayout)to contain the tab contents, since the tab indicators are provided by the[ActionBar](https://developer.android.com/reference/android/app/ActionBar):

**res/layout-v11/main.xml:**  

```xml
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@android:id/tabcontent"
    android:layout_width="match_parent"
    android:layout_height="match_parent" />
```

At runtime, Android will decide which version of the`main.xml`layout to inflate depending on the platform version. This is the same logic shown in the previous section to determine which`TabHelper`implementation to use.

## Use TabHelper in your activity

In your activity's[onCreate()](https://developer.android.com/reference/android/app/Activity#onCreate(android.os.Bundle))method, you can obtain a`TabHelper`object and add tabs with the following code:  

### Kotlin

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
    ...
    setContentView(R.layout.main)

    TabHelper.createInstance(this).apply {
        setUp()

        newTab("photos")
                .setText(R.string.tab_photos)
                .also { photosTab ->
                    addTab(photosTab)
                }

        newTab("videos")
                .setText(R.string.tab_videos)
                .also { videosTab ->
                    addTab(videosTab)
                }
    }
}
```

### Java

```java
@Override
public void onCreate(Bundle savedInstanceState) {
    setContentView(R.layout.main);

    TabHelper tabHelper = TabHelper.createInstance(this);
    tabHelper.setUp();

    CompatTab photosTab = tabHelper
            .newTab("photos")
            .setText(R.string.tab_photos);
    tabHelper.addTab(photosTab);

    CompatTab videosTab = tabHelper
            .newTab("videos")
            .setText(R.string.tab_videos);
    tabHelper.addTab(videosTab);
}
```

When running the application, this code inflates the correct activity layout and instantiates either a`TabHelperHoneycomb`or`TabHelperEclair`object. The concrete class that's actually used is opaque to the activity, since they share the common`TabHelper`interface.

Below are two screenshots of this implementation running on an Android 2.3 and Android 4.0 device.
![Example screenshot of tabs running on an Android 2.3 device (using TabHelperEclair).](https://developer.android.com/static/images/training/backward-compatible-ui-gb.png)![Example screenshots of tabs running on an Android 4.0 device (using TabHelperHoneycomb).](https://developer.android.com/static/images/training/backward-compatible-ui-ics.png)

**Figure 1.** Example screenshots of backward-compatible tabs running on an Android 2.3 device (using`TabHelperEclair`) and an Android 4.0 device (using`TabHelperHoneycomb`).