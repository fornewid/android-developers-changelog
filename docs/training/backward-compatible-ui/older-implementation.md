---
title: https://developer.android.com/training/backward-compatible-ui/older-implementation
url: https://developer.android.com/training/backward-compatible-ui/older-implementation
source: md.txt
---

# Create an implementation with older APIs

This lesson discusses how to create an implementation that mirrors newer APIs yet supports older devices.

## Decide on a substitute solution

The most challenging task in using newer UI features in a backward-compatible way is deciding on and implementing an older (fallback) solution for older platform versions. In many cases, it's possible to fulfill the purpose of these newer UI components using older UI framework features. For example:

- Action bars can be implemented using a horizontal[LinearLayout](https://developer.android.com/reference/android/widget/LinearLayout)containing image buttons, either as custom title bars or as views in your activity layout. Overflow actions can be presented under the device*Menu*button.

- Action bar tabs can be implemented using a horizontal[LinearLayout](https://developer.android.com/reference/android/widget/LinearLayout)containing buttons, or using the[TabWidget](https://developer.android.com/reference/android/widget/TabWidget)UI element.

- [NumberPicker](https://developer.android.com/reference/android/widget/NumberPicker)and[Switch](https://developer.android.com/reference/android/widget/Switch)widgets can be implemented using[Spinner](https://developer.android.com/reference/android/widget/Spinner)and[ToggleButton](https://developer.android.com/reference/android/widget/ToggleButton)widgets, respectively.

- [ListPopupWindow](https://developer.android.com/reference/android/widget/ListPopupWindow)and[PopupMenu](https://developer.android.com/reference/android/widget/PopupMenu)widgets can be implemented using[PopupWindow](https://developer.android.com/reference/android/widget/PopupWindow)widgets.

There generally isn't a one-size-fits-all solution for backporting newer UI components to older devices. Be mindful of the user experience: on older devices, users may not be familiar with newer design patterns and UI components. Give some thought as to how the same functionality can be delivered using familiar elements. In many cases this is less of a concern---if newer UI components are prominent in the application ecosystem (such as the action bar), or where the interaction model is extremely simple and intuitive (such as swipe views using a[ViewPager](https://developer.android.com/reference/androidx/viewpager/widget/ViewPager)).

## Implement tabs using older APIs

To create an older implementation of action bar tabs, you can use a[TabWidget](https://developer.android.com/reference/android/widget/TabWidget)and[TabHost](https://developer.android.com/reference/android/widget/TabHost)(although one can alternatively use horizontally laid-out[Button](https://developer.android.com/reference/android/widget/Button)widgets). Implement this in classes called`TabHelperEclair`and`CompatTabEclair`, since this implementation uses APIs introduced no later than Android 2.0 (Eclair).
![Class diagram for the Eclair implementation of tabs.](https://developer.android.com/static/images/training/backward-compatible-ui-classes-eclair.png)

**Figure 1.**Class diagram for the Eclair implementation of tabs.

The`CompatTabEclair`implementation stores tab properties such as the tab text and icon in instance variables, since there isn't an[ActionBar.Tab](https://developer.android.com/reference/android/app/ActionBar.Tab)object available to handle this storage:  

### Kotlin

```kotlin
class CompatTabEclair internal constructor(val activity: FragmentActivity, tag: String) :
        CompatTab(tag) {

    // Store these properties in the instance,
    // as there is no ActionBar.Tab object.
    private var text: CharSequence? = null
    ...

    override fun setText(resId: Int): CompatTab {
        // Our older implementation simply stores this
        // information in the object instance.
        text = activity.resources.getText(resId)
        return this
    }

    ...
    // Do the same for other properties (icon, callback, etc.)
}
```

### Java

```java
public class CompatTabEclair extends CompatTab {
    // Store these properties in the instance,
    // as there is no ActionBar.Tab object.
    private CharSequence text;
    ...

    public CompatTab setText(int resId) {
        // Our older implementation simply stores this
        // information in the object instance.
        text = activity.getResources().getText(resId);
        return this;
    }

    ...
    // Do the same for other properties (icon, callback, etc.)
}
```

The`TabHelperEclair`implementation makes use of methods on the[TabHost](https://developer.android.com/reference/android/widget/TabHost)widget for creating[TabHost.TabSpec](https://developer.android.com/reference/android/widget/TabHost.TabSpec)objects and tab indicators:  

### Kotlin

```kotlin
class TabHelperEclair internal constructor(activity: FragmentActivity) : TabHelper(activity) {

    private var tabHost: TabHost? = null
    ...

    override fun setUp() {
        // Our activity layout for pre-Honeycomb devices
        // must contain a TabHost.
        tabHost = tabHost ?: mActivity.findViewById<TabHost>(android.R.id.tabhost).apply {
            setup()
        }
    }

    override fun addTab(tab: CompatTab) {
        ...
        tabHost?.newTabSpec(tab.tag)?.run {
            setIndicator(tab.getText()) // And optional icon
            ...
            tabHost?.addTab(this)
        }
    }
    // The other important method, newTab() is part of
    // the base implementation.
}
```

### Java

```java
public class TabHelperEclair extends TabHelper {
    private TabHost tabHost;
    ...

    protected void setUp() {
        if (tabHost == null) {
            // Our activity layout for pre-Honeycomb devices
            // must contain a TabHost.
            tabHost = (TabHost) mActivity.findViewById(
                    android.R.id.tabhost);
            tabHost.setup();
        }
    }

    public void addTab(CompatTab tab) {
        ...
        TabSpec spec = tabHost
                .newTabSpec(tag)
                .setIndicator(tab.getText()); // And optional icon
        ...
        tabHost.addTab(spec);
    }

    // The other important method, newTab() is part of
    // the base implementation.
}
```

You now have two implementations of`CompatTab`and`TabHelper`: one that works on devices running Android 3.0 or later and uses new APIs, and another that works on devices running Android 2.0 or later and uses older APIs. The next lesson discusses using these implementations in your application.