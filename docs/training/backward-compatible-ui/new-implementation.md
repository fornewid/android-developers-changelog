---
title: Proxy to the new APIs  |  Views  |  Android Developers
url: https://developer.android.com/training/backward-compatible-ui/new-implementation
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Views](https://developer.android.com/develop/ui/views/layout/declaring-layout)

# Proxy to the new APIs Stay organized with collections Save and categorize content based on your preferences.



This lesson shows you how to subclass the `CompatTab` and `TabHelper` abstract classes and use new APIs. Your application can use this implementation on devices running a platform version that supports them.

## Implement tabs using new APIs

The concrete classes for `CompatTab` and `TabHelper` that use newer APIs are a *proxy* implementation. Since the abstract classes defined in the previous lesson mirror the new APIs (class structure, method signatures, etc.), the concrete classes that use these newer APIs simply proxy method calls and their results.

You can directly use newer APIs in these concrete classes—and not crash on earlier devices—because of lazy class loading. Classes are loaded and initialized on first access—instantiating the class or accessing one of its static fields or methods for the first time. Thus, as long as you don't instantiate the Honeycomb-specific implementations on pre-Honeycomb devices, the Dalvik VM won't throw any `VerifyError` exceptions.

A good naming convention for this implementation is to append the API level or platform version code name corresponding to the APIs required by the concrete classes. For example, the native tab implementation can be provided by `CompatTabHoneycomb` and `TabHelperHoneycomb` classes, since they rely on APIs available in Android 3.0 (API level 11) or later.

![Class diagram for the Honeycomb implementation of tabs.](/static/images/training/backward-compatible-ui-classes-honeycomb.png)

**Figure 1.** Class diagram for the Honeycomb implementation of tabs.

## Implement CompatTabHoneycomb

`CompatTabHoneycomb` is the implementation of the `CompatTab` abstract class that `TabHelperHoneycomb` uses to reference individual tabs. `CompatTabHoneycomb` simply proxies all method calls to its contained `ActionBar.Tab` object.

Begin implementing `CompatTabHoneycomb` using the new `ActionBar.Tab` APIs:

### Kotlin

```
class CompatTabHoneycomb internal constructor(val activity: Activity, tag: String) :
        CompatTab(tag) {
    ...
    // The native tab object that this CompatTab acts as a proxy for.
    private var mTab: ActionBar.Tab =
            // Proxy to new ActionBar.newTab API
            activity.actionBar.newTab()

    override fun setText(@StringRes textId: Int): CompatTab {
        // Proxy to new ActionBar.Tab.setText API
        mTab.setText(textId)
        return this
    }

    ...
    // Do the same for other properties (icon, callback, etc.)
}
```

### Java

```
public class CompatTabHoneycomb extends CompatTab {
    // The native tab object that this CompatTab acts as a proxy for.
    ActionBar.Tab mTab;
    ...

    protected CompatTabHoneycomb(FragmentActivity activity, String tag) {
        ...
        // Proxy to new ActionBar.newTab API
        mTab = activity.getActionBar().newTab();
    }

    public CompatTab setText(int resId) {
        // Proxy to new ActionBar.Tab.setText API
        mTab.setText(resId);
        return this;
    }

    ...
    // Do the same for other properties (icon, callback, etc.)
}
```

## Implement TabHelperHoneycomb

`TabHelperHoneycomb` is the implementation of the `TabHelper` abstract class that proxies method calls to an actual `ActionBar`, obtained from its contained `Activity`.

Implement `TabHelperHoneycomb`, proxying method calls to the `ActionBar` API:

### Kotlin

```
class TabHelperHoneycomb internal constructor(activity: FragmentActivity) : TabHelper(activity) {

    private var mActionBar: ActionBar? = null

    override fun setUp() {
        mActionBar = mActionBar ?: mActivity.actionBar.apply {
            navigationMode = ActionBar.NAVIGATION_MODE_TABS
        }
    }

    override fun addTab(tab: CompatTab) {
        // Tab is a CompatTabHoneycomb instance, so its
        // native tab object is an ActionBar.Tab.
        mActionBar?.addTab(tab.getTab() as ActionBar.Tab)
    }
}
```

### Java

```
public class TabHelperHoneycomb extends TabHelper {
    ActionBar actionBar;
    ...

    protected void setUp() {
        if (actionBar == null) {
            actionBar = activity.getActionBar();
            actionBar.setNavigationMode(
                    ActionBar.NAVIGATION_MODE_TABS);
        }
    }

    public void addTab(CompatTab tab) {
        ...
        // Tab is a CompatTabHoneycomb instance, so its
        // native tab object is an ActionBar.Tab.
        actionBar.addTab((ActionBar.Tab) tab.getTab());
    }

    // The other important method, newTab() is part of
    // the base implementation.
}
```

### You should also read

* [Action Bar](/guide/topics/ui/actionbar)
* [Action Bar Tabs](/guide/topics/ui/actionbar#Tabs)

[Previous

arrow\_back

Abstract newer APIs](/training/backward-compatible-ui/abstracting)

[Next

Create an implementation with older APIs

arrow\_forward](/training/backward-compatible-ui/older-implementation)